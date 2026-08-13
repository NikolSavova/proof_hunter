#!/usr/bin/env python3
"""wave6b numerics referee for sol_s3_20260812.md — script 5: scan-gap control.

The ref2/ref3 scans are finite; this script bounds what can hide between grid points:
 [D1] per band W1..W6b: sampled max |dJ/dw| (limit row and m=561 row) and the max
      m-direction spread |J(561) - J(limit)|; compares worst-possible unsampled
      excursion (max|dJ/dw| * half the coarsest ref2 gap + m-spread) against the
      band's measured headroom to the claimed SOL.7 sup bound.
 [D2] W7: sampled max |dU7/dlam| on (0, 0.89] and the excursion bound for ref3's
      cell structure vs the measured 12/5 margin; same for the two SOL.16 floors.
All derivatives are central finite differences at dps 30 (h = 1e-6), reported with a
2x safety factor.  This is scan-class evidence, not a certificate; it is the check
that the draft's recipe omits (its grid is asserted, never justified).
"""
import mpmath as mp

mp.mp.dps = 30
NUM = {2: lambda qq: qq, 3: lambda qq: qq*(1+qq), 4: lambda qq: qq*(1+4*qq+qq*qq)}
fact = {2: 1, 3: 2, 4: 6}
zeta2 = mp.pi**2/6
P = {2: lambda t: t*t + 2*t + 2, 3: lambda t: t**3 + 3*t*t + 6*t + 6,
     4: lambda t: t**4 + 4*t**3 + 12*t*t + 24*t + 24}
L = mp.mpf(40)/561

def h_mp(n, xx):
    xx = mp.mpf(xx)
    if xx == 0:
        return mp.mpf(fact[n])
    em = -mp.expm1(-xx)
    return xx**n * NUM[n](mp.e**(-xx)) / em**n

def G_n(n, w):
    w = mp.mpf(w)
    s = mp.mpf(0)
    for kk in range(1, 200):
        t = mp.e**(-kk*w)*P[n](kk*w)/kk**2
        s += t
        if t < mp.mpf('1e-40'):
            break
    return fact[n]*w - mp.factorial(n)*zeta2 + s

def J_limit(w):
    F = tuple(G_n(n, w) for n in (2, 3, 4))
    return (F[1]/F[0])**2 - F[2]/(2*F[0])

def J_m(m, w):
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
    F = tuple(lam*(m*h_mp(n, lam) - s) for n, s in ((2, s2), (3, s3), (4, s4)))
    return (F[1]/F[0])**2 - F[2]/(2*F[0])

BANDS = [("W1", 4, 5, mp.mpf(1)/2, mp.mpf('0.46031849')),
         ("W2", 5, 6, mp.mpf(13)/20, mp.mpf('0.55031731')),
         ("W3", 6, 8, mp.mpf(9)/10, mp.mpf('0.66462617')),
         ("W4", 8, 10, mp.mpf(11)/10, mp.mpf('0.7235812')),
         ("W5", 10, 20, mp.mpf(3)/2, mp.mpf('0.84252011')),
         ("W6b", 20, 40, mp.mpf(17)/10, mp.mpf('0.92059223'))]
print("=== [D1] band-scan gap control ===", flush=True)
hstep = mp.mpf('1e-6')
for (name, a, b, bound, maxJ) in BANDS:
    a, b = mp.mpf(a), mp.mpf(b)
    maxd, spread = mp.mpf(0), mp.mpf(0)
    for i in range(33):
        w_ = a + (b-a)*i/32
        if w_ <= a: w_ = a + (b-a)/1000
        dJl = abs(J_limit(w_+hstep) - J_limit(w_-hstep))/(2*hstep)
        dJm = abs(J_m(561, w_+hstep) - J_m(561, w_-hstep))/(2*hstep)
        maxd = max(maxd, dJl, dJm)
        spread = max(spread, abs(J_m(561, w_) - J_limit(w_)))
    gap = (b-a)/128/2          # half the coarsest ref2 gap
    exc = 2*maxd*gap + spread  # 2x safety on the derivative
    head = bound - maxJ
    print(f"  {name}: max|dJ/dw| ~= {mp.nstr(maxd, 5)}; m-spread <= {mp.nstr(spread, 5)}; "
          f"worst unsampled excursion (2x safety) = {mp.nstr(exc, 5)} vs headroom {mp.nstr(head, 5)}; "
          f"spike-proof at scan resolution: {exc < head}", flush=True)

print("=== [D2] W7 gap control ===", flush=True)
def T_all(lam):
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
        s2 += x2*qj*inv2
        s3 += x2*xl*qj*(one+qj)*inv2*inv
        t4 = x2*x2*qj*(one+4*qj+qj*qj)*inv2*inv2
        s4 += t4
        if xl > 60 and t4 < mp.mpf('1e-30'):
            break
    return s2, s3, s4
def U7_parts(lam):
    lam = mp.mpf(lam)
    T2, T3, T4 = T_all(lam)
    d = min(mp.mpf(1)/561, lam/40)
    h2, h3, h4 = (h_mp(n, lam) for n in (2, 3, 4))
    den = h2 - d*T2
    low4 = h4 - d*T4
    return den, low4, (h3/den)**2 - low4/(2*h2)
maxdU = maxdden = maxdlow = mp.mpf(0)
for i in range(1, 65):
    lam = mp.mpf('0.89')*i/64
    d1, l1, u1 = U7_parts(lam - hstep)
    d2, l2, u2 = U7_parts(lam + hstep)
    maxdU = max(maxdU, abs(u2-u1)/(2*hstep))
    maxdden = max(maxdden, abs(d2-d1)/(2*hstep))
    maxdlow = max(maxdlow, abs(l2-l1)/(2*hstep))
cell = (mp.mpf('0.89') - L)/16384/2
excU = 2*maxdU*cell
print(f"  max|dU7/dlam| ~= {mp.nstr(maxdU, 5)}; half-cell = {mp.nstr(cell, 4)}; "
      f"excursion (2x safety) = {mp.nstr(excU, 5)} vs margin to 12/5 (~0.156): {excU < mp.mpf('0.156')}")
print(f"  max|d(h2-dT2)/dlam| ~= {mp.nstr(maxdden, 5)}; excursion = {mp.nstr(2*maxdden*cell, 5)} "
      f"vs floor margin (~0.0177): {2*maxdden*cell < mp.mpf('0.0177')}")
print(f"  max|d(h4-dT4)/dlam| ~= {mp.nstr(maxdlow, 5)}; excursion = {mp.nstr(2*maxdlow*cell, 5)} "
      f"vs floor margin (~0.11): {2*maxdlow*cell < mp.mpf('0.11')}", flush=True)
print("DONE ref5", flush=True)
