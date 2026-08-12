# NC-SL3-2: measured-truth sanity for wp4_sl_SL3.md (floats, LABELED SANITY;
# the proof rests on NC-SL3-1's certificates, not on this file).
# (a) variance formula check; (b) A <= m on grids (SL3.B); (c) min of
# -log|phi|/(s2 t^2) on tier-1/tier-2 ranges vs c1/c2 (SL3.1); (d) exact
# eps_j vs Eps(lam,x0) (SL3.D/SL3.A); (e) true T_u vs the SL3.2 bound.
import math

def q_of(lam): return math.exp(-lam)

def var_uj(j, lam):  # closed form: q/(1-q)^2 - j^2 q^j/(1-q^j)^2
    q = q_of(lam)
    if j == 1: return 0.0
    return q/(1-q)**2 - j*j*q**j/(1-q**j)**2

def var_uj_direct(j, lam):
    q = q_of(lam)
    ws = [q**i for i in range(j)]; Z = sum(ws)
    m1 = sum(i*w for i, w in enumerate(ws))/Z
    return sum((i-m1)**2*w for i, w in enumerate(ws))/Z

print("(a) variance closed form vs direct sum:")
worst = 0.0
for j, lam in [(2, .1), (7, .5), (40, .89), (170, .02), (401, .01)]:
    a, b = var_uj(j, lam), var_uj_direct(j, lam)
    worst = max(worst, abs(a-b)/b)
print(f"    max rel dev = {worst:.2e}  (PASS iff < 1e-10)")

def s2_of(m, lam): return sum(var_uj(j, lam) for j in range(1, m+1))

print("(b) SL3.B  A = lam^2 s2 <= m :")
viol = 0; amax = 0.0
for m in (401, 900):
    for iw in range(1, 90):
        lam = min(0.89, iw*0.01)
        A = lam*lam*s2_of(m, lam); amax = max(amax, A/m)
        if A > m: viol += 1
print(f"    violations = {viol}, max A/m = {amax:.4f}  (PASS iff 0 violations)")

def absphi(m, lam, t, qpow):  # prod_j |nu_j(t)| via T.6(i) closed form
    q = q_of(lam); den0 = (1-q)**2 + 4*q*math.sin(t/2)**2
    lp = 0.0
    for j in range(2, m+1):
        qj = qpow[j]; zj = (1-qj)/(1-q)
        num = (1-qj)**2 + 4*qj*math.sin(j*t/2)**2
        lp += 0.5*(math.log(num) - math.log(zj*zj*den0))
    return math.exp(lp)

print("(c) SL3.1 measured min of -log|phi|/(s2 t^2)  [tier1 on [lam/2,.8lam], tier2 on [.8lam,1.074lam]]:")
c1, c2 = 0.1317175, 0.0871362
for m, wt in [(401, 4.05), (401, 4.2), (401, 5.0), (401, 7.0), (401, 20.0),
              (401, 100.0), (401, 356.89), (900, 4.05), (900, 356.89)]:
    lam = min(0.89, wt/m); s2 = s2_of(m, lam)
    qpow = [q_of(lam)**j for j in range(m+1)]
    t0 = 2*math.asin(math.sinh(lam/2))
    def scan(ta, tb, n=160):
        mn = 1e9
        for i in range(n+1):
            t = ta + (tb-ta)*i/n
            if t <= 0: continue
            p = absphi(m, lam, t, qpow)
            mn = min(mn, -math.log(max(p, 1e-300))/(s2*t*t))
        return mn
    mn1 = scan(lam/2, 0.8*lam); mn2 = scan(0.8*lam, min(1.074*lam, t0))
    print(f"    m={m} w={wt:7.2f}: tier1 min={mn1:.4f} (>=c1? {mn1>=c1}) "
          f"tier2 min={mn2:.4f} (>=c2? {mn2>=c2})  [t0/lam={t0/lam:.4f}]")

print("(d) exact eps_j vs Eps(lam,x0)  [b1 = pi/(0.8 lam), b2 = pi/(1.074 lam)]:")
def eps_exact(j, lam, b):
    q = q_of(lam)
    num = den = 0.0
    for d in range(1, j):
        p = q**d*(1-q**(2*(j-d)))   # unnormalized, common factor cancels
        den += d*d*p
        if d > b: num += d*d*p
    return num/den if den > 0 else 0.0
def Eps(lam, x0):
    q = q_of(lam)
    return math.exp(-x0)*((x0/lam)**2*(1-q)**2/(q*(1+q))
                          + 2*(x0/lam)*(1-q)/(1+q) + 1)
x1, x2 = 3.9269, 2.9251
for lam in (0.1, 0.5, 0.89):
    for j in (5, 50, 401):
        e1 = eps_exact(j, lam, math.pi/(0.8*lam))
        e2 = eps_exact(j, lam, math.pi/(1.074*lam))
        E1, E2 = Eps(lam, x1), Eps(lam, x2)
        print(f"    lam={lam:.2f} j={j:3d}: eps1={e1:.4f}<=Eps1={E1:.4f}? {e1<=E1} | "
          f"eps2={e2:.4f}<=Eps2={E2:.4f}? {e2<=E2}")

print("(e) true T_u (Simpson, 4000 panels on [lam/2, pi]) vs SL3.2 bound, m=401:")
m = 401
for wt in (4.05, 5.0, 20.0):
    lam = wt/m; s2 = s2_of(m, lam); A = lam*lam*s2
    qpow = [q_of(lam)**j for j in range(m+1)]
    a, b, n = lam/2, math.pi, 4000
    h = (b-a)/n; tot = 0.0
    for i in range(n+1):
        t = a + i*h
        wgt = 1 if i in (0, n) else (4 if i % 2 else 2)
        tot += wgt*absphi(m, lam, t, qpow)
    Tu = A*math.sqrt(s2/(2*math.pi))*tot*h/3
    bound = (3.192*math.sqrt(A)*math.exp(-A/32)
             + 2.87*math.sqrt(A)*math.exp(-0.0556*A)
             + 0.3134*m**2.5*math.exp(-0.0741*m))
    print(f"    w={wt:6.2f}: A={A:8.3f}  T_u(true)={Tu:.4f}  bound={bound:.4f}  "
          f"ratio={bound/Tu:.2f}")
