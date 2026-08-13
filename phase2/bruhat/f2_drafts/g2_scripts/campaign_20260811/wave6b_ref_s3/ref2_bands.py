#!/usr/bin/env python3
"""wave6b numerics referee for sol_s3_20260812.md — script 2: SOL.7 band-bound truth attack.

For each band W1..W6b, scan J(w, lam) = (F3/F2)^2 - F4/(2 F2) over:
  - exact integer-m points m in {561, 562, 563, 570, 600, 750, 1000, 2500} (lam = w/m, exact sums)
  - the m -> infinity limit row (F_n -> G_n(w))
  - w-grid: step 1/128 across the band + step ~1/2050 in the last 0.1 before the right edge
    + the exact right edge and off-grid points (edge - 1/3000, edge - pi/10000)
Track per-band max J, argmax, min F2; compare against the draft's claimed sup bounds
(SOL.7): 1/2, 13/20, 9/10, 11/10, 3/2, 17/10.  Also reproduce the binding point
(m, w) = (561, 5): r31/r42/J/(J/J0) vs draft (0.8864/0.6506/0.4603/0.6740) and scout
truth (0.88636/0.65065).  dps-30 mpmath scans; exact-sum F_n cross-validated against
the G_n limit at m = 10000.
"""
import mpmath as mp

mp.mp.dps = 30

NUM = {2: lambda qq: qq, 3: lambda qq: qq*(1+qq), 4: lambda qq: qq*(1+4*qq+qq*qq)}
fact = {2: 1, 3: 2, 4: 6}
zeta2 = mp.pi**2/6
P = {2: lambda t: t*t + 2*t + 2,
     3: lambda t: t**3 + 3*t*t + 6*t + 6,
     4: lambda t: t**4 + 4*t**3 + 12*t*t + 24*t + 24}

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

def F_all(m, w):
    """(F2, F3, F4) by exact summation, shared q-powers."""
    lam = mp.mpf(w)/m
    q1 = mp.e**(-lam)
    qj = mp.mpf(1)
    s2 = s3 = s4 = mp.mpf(0)
    xl = mp.mpf(0)
    one = mp.mpf(1)
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

def J_of(F):
    return (F[1]/F[0])**2 - F[2]/(2*F[0])

BANDS = [("W1", 4, 5, mp.mpf(1)/2), ("W2", 5, 6, mp.mpf(13)/20), ("W3", 6, 8, mp.mpf(9)/10),
         ("W4", 8, 10, mp.mpf(11)/10), ("W5", 10, 20, mp.mpf(3)/2), ("W6b", 20, 40, mp.mpf(17)/10)]
MS = [561, 562, 563, 570, 600, 750, 1000, 2500]

print("=== cross-validation: exact sums vs limit (w=5) ===", flush=True)
F10k = F_all(10000, 5)
for i, n in enumerate((2, 3, 4)):
    g = G_n(n, 5)
    print(f"  n={n}: F(m=10000)={mp.nstr(F10k[i],12)}  G_n={mp.nstr(g,12)}  diff={mp.nstr(abs(F10k[i]-g),3)}",
          flush=True)

print("=== binding point (m, w) = (561, 5) ===", flush=True)
Fb = F_all(561, 5)
r31, r42 = Fb[1]/Fb[0], Fb[2]/Fb[0]
Jb = J_of(Fb)
J0W1 = mp.mpf(57118994397115584673581017925677)/mp.mpf(83636677924642268545373517242925)
print(f"  r31 = {mp.nstr(r31, 8)}   (draft 0.8864, scout 0.88636)")
print(f"  r42 = {mp.nstr(r42, 8)}   (draft 0.6506, scout 0.65065)")
print(f"  J   = {mp.nstr(Jb, 8)}   (draft 0.4603)")
print(f"  J/J0(W1) = {mp.nstr(Jb/J0W1, 8)}   (draft 0.6740)", flush=True)

print("=== per-band scan (this is the SOL.7 attack) ===", flush=True)
overall_ok = True
for (name, a, b, bound) in BANDS:
    a, b = mp.mpf(a), mp.mpf(b)
    ws = []
    n128 = int((b-a)*128)
    ws += [a + (b-a)*i/n128 for i in range(1, n128+1)]
    ws += [b - mp.mpf('0.1') + mp.mpf('0.1')*i/205 for i in range(1, 205)]
    ws += [b - mp.mpf(1)/3000, b - mp.pi/10000]
    ws = sorted(set([w_ for w_ in ws if a < w_ <= b]))
    maxJ, arg, minF2 = mp.mpf('-inf'), None, mp.mpf('inf')
    for w_ in ws:
        Fl = tuple(G_n(n, w_) for n in (2, 3, 4))
        Jl = J_of(Fl)
        if Jl > maxJ: maxJ, arg = Jl, (w_, 'limit')
        if Fl[0] < minF2: minF2 = Fl[0]
        Fm = F_all(561, w_)
        Jm = J_of(Fm)
        if Jm > maxJ: maxJ, arg = Jm, (w_, 561)
        if Fm[0] < minF2: minF2 = Fm[0]
    # dense m-scan on a coarser w-grid + the edge-adjacent fine points
    ws2 = [a + (b-a)*i/16 for i in range(1, 17)] + [b - mp.mpf(1)/3000, b - mp.pi/10000, b]
    ws2 = sorted(set([w_ for w_ in ws2 if a < w_ <= b]))
    for w_ in ws2:
        for m in MS[1:]:
            Fm = F_all(m, w_)
            Jm = J_of(Fm)
            if Jm > maxJ: maxJ, arg = Jm, (w_, m)
            if Fm[0] < minF2: minF2 = Fm[0]
    ok = maxJ <= bound
    okF2 = minF2 > mp.mpf(1)/10
    overall_ok &= ok and okF2
    print(f"  {name}: max J = {mp.nstr(maxJ, 8)} at (w, m) = ({mp.nstr(arg[0], 8)}, {arg[1]}); "
          f"claimed sup {mp.nstr(bound, 4)}; J <= sup: {ok} "
          f"(headroom {mp.nstr((bound-maxJ)/bound*100, 4)}%); min F2 = {mp.nstr(minF2, 6)} > 1/10: {okF2}",
          flush=True)
print(f"ALL BAND CHECKS PASS (truth level, scan class): {overall_ok}", flush=True)
print("DONE ref2", flush=True)
