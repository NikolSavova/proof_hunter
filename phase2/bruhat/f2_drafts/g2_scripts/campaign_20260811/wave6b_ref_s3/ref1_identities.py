#!/usr/bin/env python3
"""wave6b numerics referee for sol_s3_20260812.md — script 1: identities & lemma-level checks.

Blocks:
 [A1] Lambert closed forms of phi_n (n=2,3,4)  (q-series comparison to q^30, exact)
 [A2/A3] h_n(0) values + SOL.2 Bernoulli-expansion coefficients through x^10 (exact,
      via h_n(x) = (-1)^{n-1} sum_j B_j/j! * prod_{i=1}^{n-1}(j-i) * x^j)
 [A4] EM constants: 2 zeta(8)/(2 pi)^8 = 1/1209600 (exact); honest kernel constant
 [A5] zeta(2) rational enclosure of the recipe
 [A6] P_n polynomials + tail identity  int_w^inf h_n = sum_k e^{-kw} P_n(kw)/k^2
 [A7] Lemma SOL.1 vs brute-force tilted Mahonian cumulants (m=6, lam=0.37; m=9, lam=0.11)
 [A8] negative-tilt reflection claim (kappa_3 flips, kappa_2/kappa_4 invariant)
 [A9] G_n via SOL.2 (K=64) vs direct quadrature; G_4(4) vs scout guard 0.2323483
 [A10] EM remainder audit: E_actual vs the draft's SOL.4 bound (lam^8/1209600)*int|h^(8)|
 [A11] true max of |h_n^{(8)}| on (0,40] and int_0^60 |h_n^{(8)}| vs the claimed 1e12
"""
import sympy as sp
import mpmath as mp

x, q, y = sp.symbols('x q y')

print("=== [A1] Lambert closed forms of phi_n (q-series to q^30) ===", flush=True)
targets = {2: q/(1-q)**2, 3: q*(1+q)/(1-q)**3, 4: q*(1+4*q+q**2)/(1-q)**4}
for n, tgt in targets.items():
    ser = sp.Poly(sp.series(tgt, q, 0, 31).removeO(), q)
    ok = all(ser.coeff_monomial(q**kk) == kk**(n-1) for kk in range(1, 31))
    print(f"  phi_{n} = sum k^{n-1} q^k  matches draft's closed form to q^30: {ok}", flush=True)

print("=== [A2]/[A3] exact series of h_n at 0 (Bernoulli formula) ===", flush=True)
def h_series_coeff(n, j):
    """exact coefficient of x^j in h_n"""
    c = (-1)**(n-1) * sp.bernoulli(j) / sp.factorial(j)
    for i in range(1, n):
        c *= (j - i)
    return sp.nsimplify(c)
claimed = {
    2: {0: sp.Integer(1), 2: sp.Rational(-1, 12), 4: sp.Rational(1, 240),
        6: sp.Rational(-1, 6048), 8: sp.Rational(1, 172800), 10: sp.Rational(-1, 5322240)},
    3: {0: sp.Integer(2), 2: sp.Integer(0), 4: sp.Rational(-1, 120),
        6: sp.Rational(1, 1512), 8: sp.Rational(-1, 28800), 10: sp.Rational(1, 665280)},
    4: {0: sp.Integer(6), 2: sp.Integer(0), 4: sp.Rational(1, 120),
        6: sp.Rational(-1, 504), 8: sp.Rational(1, 5760), 10: sp.Rational(-1, 95040)},
}
NSER = 42
hser = {n: [h_series_coeff(n, j) for j in range(NSER)] for n in (2, 3, 4)}
for n in (2, 3, 4):
    allok = True
    for pw, cl in claimed[n].items():
        got = hser[n][pw]
        if sp.simplify(got - cl) != 0:
            print(f"    h_{n}: coeff x^{pw}: draft {cl}  ACTUAL {got}  MISMATCH", flush=True)
            allok = False
    odd0 = all(hser[n][p] == 0 for p in range(1, NSER, 2))
    print(f"  h_{n}(0) = {hser[n][0]}; all printed SOL.2 coeffs match: {allok}; odd coeffs vanish: {odd0}", flush=True)

# numeric cross-check of the series vs the q-form at x = 0.5
mp.mp.dps = 40
def h_mp(n, xx):
    xx = mp.mpf(xx)
    if xx == 0:
        return mp.mpf([1, 2, 6][n-2])
    em = -mp.expm1(-xx)
    qq = mp.e**(-xx)
    num = {2: qq, 3: qq*(1+qq), 4: qq*(1+4*qq+qq**2)}[n]
    return xx**n * num / em**n
for n in (2, 3, 4):
    sv = mp.fsum(mp.mpf(str(sp.N(c, 45)))*mp.mpf('0.5')**j for j, c in enumerate(hser[n]))
    rel = abs(sv - h_mp(n, '0.5'))/h_mp(n, '0.5')
    print(f"  series(h_{n})(0.5) vs closed form rel.err = {mp.nstr(rel, 3)}", flush=True)

print("=== [A4] EM constants ===", flush=True)
c_draft = sp.simplify(sp.Rational(2) * sp.zeta(8) / (2*sp.pi)**8)
print(f"  2 zeta(8)/(2 pi)^8 = {c_draft} == 1/1209600 : {c_draft == sp.Rational(1, 1209600)}", flush=True)
B8 = sp.bernoulli(8)
c_kernel = (2 - sp.Rational(2)**(1-8)) * abs(B8) / sp.factorial(8)
print(f"  |B_8|/8! = {abs(B8)/sp.factorial(8)}  (draft's SOL.4 constant)")
print(f"  honest kernel constant without the B_8 boundary term: (2-2^-7)|B_8|/8! = {c_kernel} "
      f"~ {float(c_kernel):.4e}; ratio to draft = {float(c_kernel*1209600):.6f}", flush=True)

print("=== [A5] zeta(2) enclosure ===", flush=True)
z2 = mp.pi**2/6
lo = mp.mpf(1644934066848226)/mp.mpf(10)**15
hi = mp.mpf(1644934066848227)/mp.mpf(10)**15
print(f"  zeta(2) = {mp.nstr(z2, 25)};  lo < zeta(2) < hi : {bool(lo < z2 < hi)}", flush=True)

print("=== [A6] P_n and the tail identity ===", flush=True)
P = {n: sp.factorial(n)*sum(y**r/sp.factorial(r) for r in range(n+1)) for n in (2, 3, 4)}
claimP = {2: y**2+2*y+2, 3: y**3+3*y**2+6*y+6, 4: y**4+4*y**3+12*y**2+24*y+24}
Pl = {}
for n in (2, 3, 4):
    print(f"  P_{n} == draft: {sp.expand(P[n] - claimP[n]) == 0}", flush=True)
    Pl[n] = sp.lambdify(y, P[n], 'mpmath')
mp.mp.dps = 30
for n in (2, 3, 4):
    for w in (4, 7.5):
        wf = mp.mpf(w)
        quad = mp.quad(lambda t: h_mp(n, t), [wf, wf+5, wf+20, wf+60, wf+200])
        ssum = mp.nsum(lambda kk: mp.e**(-kk*wf)*Pl[n](kk*wf)/kk**2, [1, mp.inf])
        rel = abs(quad-ssum)/ssum
        print(f"  n={n} w={w}: int_w^inf h_n = {mp.nstr(ssum, 12)}  quad rel.err = {mp.nstr(rel, 3)}", flush=True)

print("=== [A7] Lemma SOL.1 vs brute force ===", flush=True)
mp.mp.dps = 50
def mahonian_coeffs(m):
    poly = [1]
    for j in range(1, m+1):
        new = [0]*(len(poly)+j-1)
        for i, c in enumerate(poly):
            for r in range(j):
                new[i+r] += c
        poly = new
    return poly
def brute_kappas(m, lam):
    lam = mp.mpf(lam)
    cs = mahonian_coeffs(m)
    ws = [c*mp.e**(-lam*s) for s, c in enumerate(cs)]
    Z = mp.fsum(ws)
    mean = mp.fsum(s*w_ for s, w_ in enumerate(ws))/Z
    mu = {r: mp.fsum((s-mean)**r*w_ for s, w_ in enumerate(ws))/Z for r in (2, 3, 4)}
    return mu[2], mu[3], mu[4]-3*mu[2]**2
def sol1_kappas(m, lam):
    lam = mp.mpf(lam)
    return tuple((m*h_mp(n, lam) - mp.fsum(h_mp(n, j*lam) for j in range(1, m+1)))/lam**n
                 for n in (2, 3, 4))
for (m, lam) in ((6, '0.37'), (9, '0.11')):
    bk = brute_kappas(m, lam)
    sk = sol1_kappas(m, lam)
    rels = [abs(b-s)/abs(b) for b, s in zip(bk, sk)]
    print(f"  m={m} lam={lam}: kappa_2,3,4 rel.err = " + ", ".join(mp.nstr(r, 3) for r in rels)
          + f"   (kappa_3 sign: {mp.sign(bk[1])})", flush=True)

print("=== [A8] reflection claim ===", flush=True)
for (m, lam) in ((6, '0.37'),):
    kp = brute_kappas(m, lam)
    kn = brute_kappas(m, '-0.37')
    print(f"  m={m}: |k2+ - k2-|/k2 = {mp.nstr(abs(kp[0]-kn[0])/kp[0],3)}, "
          f"|k3+ + k3-|/|k3| = {mp.nstr(abs(kp[1]+kn[1])/abs(kp[1]),3)}, "
          f"|k4+ - k4-|/|k4| = {mp.nstr(abs(kp[2]-kn[2])/abs(kp[2]),3)}", flush=True)

print("=== [A9] G_n via SOL.2 vs quadrature; G_4(4) guard ===", flush=True)
mp.mp.dps = 40
fact = {2: 1, 3: 2, 4: 6}
def G_sol2(n, w, K=80):
    w = mp.mpf(w)
    s = mp.fsum(mp.e**(-kk*w)*Pl[n](kk*w)/kk**2 for kk in range(1, K+1))
    return fact[n]*w - mp.factorial(n)*mp.pi**2/6 + s
def G_quad(n, w):
    w = mp.mpf(w)
    return fact[n]*w - mp.quad(lambda t: h_mp(n, t), [0, w/2, w])
for n in (2, 3, 4):
    for w in (4, 5, 20, 40):
        a, b = G_sol2(n, w), G_quad(n, w)
        print(f"  G_{n}({w}) = {mp.nstr(a, 20)}  rel.err vs quad = {mp.nstr(abs(a-b)/abs(a), 3)}", flush=True)
print(f"  G_4(4) = {mp.nstr(G_sol2(4, 4), 10)}  (scout guard 0.2323483)", flush=True)

print("=== [A10]/[A11] 8th-derivative machinery ===", flush=True)
# closed-form 8th derivative via sympy diff of the q-form (one-time)
hn_expr = {n: x**n * targets[n].subs(q, sp.exp(-x)) for n in (2, 3, 4)}
h8_l, hd_l, hd0 = {}, {}, {}
for n in (2, 3, 4):
    h8_l[n] = sp.lambdify(x, sp.diff(hn_expr[n], x, 8), 'mpmath')
    for d in (1, 3, 5, 7):
        hd_l[(n, d)] = sp.lambdify(x, sp.diff(hn_expr[n], x, d), 'mpmath')
        # derivative at 0 from the exact series
        c = hser[n][d+1]*sp.factorial(d+1)/sp.factorial(1) if False else None
    print(f"  built derivatives for n={n}", flush=True)
# exact derivative values at 0 from the series: d-th deriv at 0 = d! * coeff_d (coeff odd = 0)
for n in (2, 3, 4):
    for d in (1, 3, 5, 7):
        hd0[(n, d)] = 0  # odd-order derivatives vanish at 0 (verified: odd coeffs vanish)
h8_at0 = {n: sp.factorial(8)*claimed[n][8] for n in (2, 3, 4)}
# series-based h8 near 0: differentiate exact series termwise
h8_ser_coeffs = {n: [(sp.factorial(j)/sp.factorial(j-8))*hser[n][j] for j in range(8, NSER)]
                 for n in (2, 3, 4)}
def h8_safe(n, t):
    t = mp.mpf(t)
    if t < mp.mpf('0.05'):
        return mp.fsum(mp.mpf(str(sp.N(c, 40)))*t**j for j, c in enumerate(h8_ser_coeffs[n]))
    with mp.workdps(130):
        return mp.mpf(h8_l[n](t))
def int_abs_h8(n, w, N=300):
    ts = [mp.mpf(w)*i/N for i in range(N+1)]
    vals = [h8_safe(n, t) if t > 0 else mp.mpf(str(sp.N(h8_at0[n], 40))) for t in ts]
    pts = [mp.mpf(0)]
    nsc = 0
    for i in range(N):
        if vals[i]*vals[i+1] < 0:
            a, b = ts[i], ts[i+1]
            fa = vals[i]
            for _ in range(40):
                mid = (a+b)/2
                if h8_safe(n, mid)*fa < 0: b = mid
                else: a = mid
            pts.append((a+b)/2); nsc += 1
    pts.append(mp.mpf(w))
    tot = mp.fsum(abs(mp.quad(lambda t: h8_safe(n, t), [pts[i], pts[i+1]]))
                  for i in range(len(pts)-1))
    return tot, nsc
def F_exact(n, m, lam):
    lam = mp.mpf(lam)
    return lam*(m*h_mp(n, lam) - mp.fsum(h_mp(n, j*lam) for j in range(1, m+1)))
def F_sol3(n, m, lam):
    lam = mp.mpf(lam)
    w = m*lam
    t = G_sol2(n, w, K=80) + w*(h_mp(n, lam) - fact[n])
    t -= lam/2*(h_mp(n, w) - fact[n])
    t -= lam**2/12*(mp.mpf(hd_l[(n, 1)](w)))
    t += lam**4/720*(mp.mpf(hd_l[(n, 3)](w)))
    t -= lam**6/30240*(mp.mpf(hd_l[(n, 5)](w)))
    return t
print("=== [A10] EM remainder audit (SOL.3/SOL.4) ===", flush=True)
mp.mp.dps = 60
I8cache = {}
for (m, w) in ((561, 5), (561, 10), (561, 40), (1000, 20)):
    lam = mp.mpf(w)/m
    for n in (2, 3, 4):
        E = F_exact(n, m, lam) - F_sol3(n, m, lam)
        if (n, w) not in I8cache:
            I8cache[(n, w)] = int_abs_h8(n, w)
        I8, nsc = I8cache[(n, w)]
        b1 = lam**8/1209600*I8
        d7 = mp.mpf(hd_l[(n, 7)](mp.mpf(w)))
        bd = lam**8/1209600*abs(d7)
        print(f"  m={m} w={w} n={n}: |E|={mp.nstr(abs(E),4)}  b1(draft)={mp.nstr(b1,4)} "
              f"(int|h8|={mp.nstr(I8,4)}, sign changes={nsc})  |E|<=b1: {bool(abs(E)<=b1)}  "
              f"|E|<=2b1: {bool(abs(E)<=2*b1)}  B8-bdry-term~{mp.nstr(bd,3)}", flush=True)

print("=== [A11] true size of h_n^{(8)} ===", flush=True)
for n in (2, 3, 4):
    best, bestx = mp.mpf(0), None
    grid = [mp.mpf('0.05')*i for i in range(1, 41)] + [2 + mp.mpf('0.1')*i for i in range(0, 381)]
    for t in grid:
        v = abs(h8_safe(n, t))
        if v > best:
            best, bestx = v, t
    I8inf, _ = int_abs_h8(n, 60)
    print(f"  max|h_{n}^(8)| on (0,40] ~= {mp.nstr(best, 6)} at x={mp.nstr(bestx, 4)}; "
          f"h_{n}^(8)(0) = {sp.N(h8_at0[n], 6)}; int_0^60 |h^(8)| ~= {mp.nstr(I8inf, 6)}; "
          f"both < 1e12: {bool(best < 1e12 and I8inf < 1e12)}", flush=True)
print("DONE ref1", flush=True)
