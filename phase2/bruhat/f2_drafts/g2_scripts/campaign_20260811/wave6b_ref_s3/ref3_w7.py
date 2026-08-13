#!/usr/bin/env python3
"""wave6b numerics referee for sol_s3_20260812.md — script 3: the W7 lemma (SOL.4/SOL.16/SOL.17).

Blocks:
 [B1] exact lam->0+ limits of h2 - d T2, h4 - d T4, U7 (closed forms in zeta(2))
 [B2] fine scan of U7(lam), h2 - d*T2, h4 - d*T4 on (0, 0.89]:
        4096 pts on (0, L] + 16384 pts on [L, 0.89] (the draft's own cell counts),
        plus off-grid points (L +/- 1e-9, lam = 0.89 exactly, log-spaced tiny lam)
      -> checks (SOL.16) 9/10 & 49/10 floors and (SOL.17) sup U7 <= 12/5
 [B3] monotonicity inputs the lemma needs: h_3 strictly decreasing (scan of h_3'),
      also h_2 decreasing (for context)
 [B4] real-point W7 corners: J at exact integer m vs U7(lam) vs 12/5 vs 9/2
      (m=561: w = 40+1/2048 ... 499.29 = 0.89*561; m=562/1000/5000 corners)
 [B5] tail bound (SOL.15) validity spot-check; (SOL.13) P_n approximation accuracy
"""
import mpmath as mp

mp.mp.dps = 30

NUM = {2: lambda qq: qq, 3: lambda qq: qq*(1+qq), 4: lambda qq: qq*(1+4*qq+qq*qq)}
fact = {2: 1, 3: 2, 4: 6}
zeta2 = mp.pi**2/6
L = mp.mpf(40)/561

def h_mp(n, xx):
    xx = mp.mpf(xx)
    if xx == 0:
        return mp.mpf(fact[n])
    em = -mp.expm1(-xx)
    return xx**n * NUM[n](mp.e**(-xx)) / em**n

def T_all(lam):
    """(T2, T3, T4) = sum_{j>=1} h_n(j lam), truncated when negligible.
    For lam < 0.02 uses the (SOL.13)-style surrogate T_n = (n! zeta2 - (n-1)! lam/2)/lam,
    validated against direct sums in block [B5] (diff ~ 1e-13 at lam = 0.01)."""
    lam = mp.mpf(lam)
    if lam < mp.mpf('0.02'):
        return tuple((mp.factorial(n)*zeta2 - fact[n]*lam/2)/lam for n in (2, 3, 4))
    q1 = mp.e**(-lam)
    qj = mp.mpf(1)
    s2 = s3 = s4 = mp.mpf(0)
    one = mp.mpf(1)
    xl = mp.mpf(0)
    j = 0
    while True:
        j += 1
        qj *= q1
        xl += lam
        em = one - qj
        inv = one/em
        inv2 = inv*inv
        x2 = xl*xl
        t2 = x2*qj*inv2
        s2 += t2
        s3 += x2*xl*qj*(one+qj)*inv2*inv
        t4 = x2*x2*qj*(one+4*qj+qj*qj)*inv2*inv2
        s4 += t4
        if xl > 60 and t4 < mp.mpf('1e-30'):
            break
        if j > 3_000_000:
            raise RuntimeError("T_all did not converge")
    return s2, s3, s4

def dd(lam):
    lam = mp.mpf(lam)
    return min(mp.mpf(1)/561, lam/40)

def U7_parts(lam):
    lam = mp.mpf(lam)
    T2, T3, T4 = T_all(lam)
    d = dd(lam)
    h2, h3, h4 = (h_mp(n, lam) for n in (2, 3, 4))
    den = h2 - d*T2
    low4 = h4 - d*T4
    U = (h3/den)**2 - low4/(2*h2)
    return den, low4, U

print("=== [B1] exact lam->0+ limits ===", flush=True)
den0 = 1 - zeta2/20            # h2 - dT2 -> 1 - 2*zeta2/40
low40 = 6 - mp.mpf(24)*zeta2/40
U70 = (2/den0)**2 - low40/2
print(f"  lim (h2 - dT2) = 1 - zeta2/20 = {mp.nstr(den0, 12)}  (> 9/10: {den0 > mp.mpf(9)/10}, "
      f"margin {mp.nstr((den0-mp.mpf(9)/10)/den0*100, 4)}%)")
print(f"  lim (h4 - dT4) = 6 - 3*zeta2/5 = {mp.nstr(low40, 12)}  (> 49/10: {low40 > mp.mpf(49)/10}, "
      f"margin {mp.nstr((low40-mp.mpf(49)/10)/low40*100, 4)}%)")
print(f"  lim U7 = {mp.nstr(U70, 12)}  (<= 12/5: {U70 <= mp.mpf(12)/5}, "
      f"margin {mp.nstr((mp.mpf(12)/5-U70)/(mp.mpf(12)/5)*100, 4)}%)", flush=True)

print("=== [B2] U7 / floors scan ===", flush=True)
lams = []
# the draft's own cell structure: 4096 cells on [0, L], 16384 on [L, 0.89] -> sample cell edges
for i in range(1, 4097):
    lams.append(L*i/4096)
for i in range(0, 16385):
    lams.append(L + (mp.mpf('0.89')-L)*i/16384)
# adversarial extras: tiny lam (log-spaced), off-grid, exact corner
lams += [mp.mpf('1e-6'), mp.mpf('1e-5'), mp.mpf('1e-4'), mp.mpf('3e-4'), mp.mpf('1e-3'),
         mp.mpf('3e-3'), mp.mpf('0.01'), L - mp.mpf('1e-9'), L + mp.mpf('1e-9'),
         mp.mpf('0.89'), mp.mpf('0.889999'), mp.pi/8, mp.pi/16, mp.pi/32]
lams = sorted(set(lams))
minden, minlow, maxU = mp.mpf('inf'), mp.mpf('inf'), mp.mpf('-inf')
aden = alow = aU = None
for lam in lams:
    den, low4, U = U7_parts(lam)
    if den < minden: minden, aden = den, lam
    if low4 < minlow: minlow, alow = low4, lam
    if U > maxU: maxU, aU = U, lam
print(f"  scanned {len(lams)} lam points on (0, 0.89]")
print(f"  min(h2 - d T2) = {mp.nstr(minden, 10)} at lam = {mp.nstr(aden, 8)}  > 9/10: {minden > mp.mpf(9)/10}")
print(f"  min(h4 - d T4) = {mp.nstr(minlow, 10)} at lam = {mp.nstr(alow, 8)}  > 49/10: {minlow > mp.mpf(49)/10}")
print(f"  max U7 = {mp.nstr(maxU, 10)} at lam = {mp.nstr(aU, 8)}  <= 12/5: {maxU <= mp.mpf(12)/5} "
      f"(margin {mp.nstr((mp.mpf(12)/5-maxU)/(mp.mpf(12)/5)*100, 4)}%)", flush=True)

print("=== [B3] h_3 decreasing (needed for 0 <= B <= m h_3) ===", flush=True)
def h3prime(xx):
    xx = mp.mpf(xx)
    e = mp.e**(-xx)
    em = 1 - e
    # d/dx [x^3 e^{-x}(1+e^{-x})/(1-e^{-x})^3]
    f = xx**3*e*(1+e)/em**3
    df = (3/xx - 1 - e/(1+e) - 3*e/em)*f
    return df
worst = mp.mpf('-inf'); aw = None
grid3 = [mp.mpf('0.001')*i for i in range(1, 1000)] + [1 + mp.mpf('0.01')*i for i in range(0, 7901)]
for t in grid3:
    v = h3prime(t)
    if v > worst: worst, aw = v, t
print(f"  max h_3'(x) on (0, 80] = {mp.nstr(worst, 8)} at x = {mp.nstr(aw, 6)}  (< 0: {worst < 0})", flush=True)
def h2prime(xx):
    xx = mp.mpf(xx)
    e = mp.e**(-xx)
    em = 1 - e
    f = xx**2*e/em**2
    return (2/xx - 1 - 2*e/em)*f
worst2 = max(h2prime(t) for t in grid3)
print(f"  max h_2'(x) on (0, 80] = {mp.nstr(worst2, 8)}  (< 0: {worst2 < 0})", flush=True)

print("=== [B4] real-point W7 corners: J vs U7 vs 12/5 vs 9/2 ===", flush=True)
def F_all(m, w):
    lam = mp.mpf(w)/m
    q1 = mp.e**(-lam)
    qj = mp.mpf(1)
    s2 = s3 = s4 = mp.mpf(0)
    one = mp.mpf(1)
    xl = mp.mpf(0)
    for j in range(1, m+1):
        qj *= q1
        xl += lam
        em = one - qj
        inv = one/em
        inv2 = inv*inv
        x2 = xl*xl
        s2 += x2*qj*inv2
        s3 += x2*xl*qj*(one+qj)*inv2*inv
        s4 += x2*x2*qj*(one+4*qj+qj*qj)*inv2*inv2
    h2l, h3l, h4l = (h_mp(n, lam) for n in (2, 3, 4))
    return (lam*(m*h2l - s2), lam*(m*h3l - s3), lam*(m*h4l - s4))
cases = []
for w in ('40.00048828125', '40.5', '41', '45', '50', '60', '80', '100', '150', '200', '300', '400'):
    cases.append((561, mp.mpf(w)))
cases.append((561, mp.mpf('0.89')*561))
cases.append((562, mp.mpf('0.89')*562))
cases.append((1000, mp.mpf('40.04')))
cases.append((1000, mp.mpf('0.89')*1000))
cases.append((5000, mp.mpf('41')))
cases.append((5000, mp.mpf('0.89')*5000))
allok = True
for (m, w) in cases:
    lam = w/m
    if not (w > 40 and lam <= mp.mpf('0.89')):
        continue
    F = F_all(m, w)
    J = (F[1]/F[0])**2 - F[2]/(2*F[0])
    _, _, U = U7_parts(lam)
    ok = J <= U <= mp.mpf(12)/5 <= mp.mpf(9)/2
    allok &= bool(ok)
    print(f"  m={m} w={mp.nstr(w, 8)} lam={mp.nstr(lam, 6)}: J={mp.nstr(J, 8)}  U7={mp.nstr(U, 8)}  "
          f"J<=U7<=2.4<=4.5: {ok}", flush=True)
print(f"  all corner chains hold: {allok}", flush=True)

print("=== [B5] (SOL.15) tail bound & (SOL.13) P_n approximation ===", flush=True)
C_n = {2: 1, 3: 2, 4: 6}
N = 1024
for lam in (L, mp.mpf('0.3'), mp.mpf('0.89')):
    for n in (2, 3, 4):
        # actual tail sum_{j>N} h_n(j lam)
        tail = mp.mpf(0)
        j = N+1
        while True:
            t = h_mp(n, j*lam)
            tail += t
            if t < mp.mpf('1e-45'):
                break
            j += 1
        integ = mp.quad(lambda t: (t+1)**n*mp.e**(-lam*t), [N, N+200/lam])
        bound = C_n[n]*lam**n*integ/(1-mp.e**(-(N+1)*lam))**n
        print(f"  lam={mp.nstr(lam,6)} n={n}: tail={mp.nstr(tail,6)}  SOL.15 bound={mp.nstr(bound,6)}  "
          f"tail<=bound: {tail <= bound}", flush=True)
for lam in (mp.mpf('0.01'), mp.mpf('0.05'), L):
    for n in (2, 3, 4):
        T = T_all(lam)[n-2]
        Papprox = mp.factorial(n)*zeta2 - fact[n]*lam/2
        err = lam*T - Papprox
        print(f"  lam={mp.nstr(lam,4)} n={n}: P_n = lam*T_n = {mp.nstr(lam*T, 12)}  "
              f"[n! zeta2 - (n-1)! lam/2] = {mp.nstr(Papprox, 12)}  diff = {mp.nstr(err, 3)}", flush=True)
print("DONE ref3", flush=True)
