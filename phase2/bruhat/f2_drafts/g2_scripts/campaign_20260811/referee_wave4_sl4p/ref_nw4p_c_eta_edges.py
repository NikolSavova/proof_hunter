#!/usr/bin/env python3
# ref_nw4p_c_eta_edges.py -- adversarial numerics referee, wave4_sl4p.
# SL4'-E pricing probed at the points the prover's 17-point set MISSED: the
# band RIGHT edges (where |eta|/u is largest within a band but the banded
# price is fixed), the w -> 4+ edge, and the exact lam = 0.89 corner.
# Independent re-implementation (dps 35, direct pmf central moments).
# Checks: ratio <= 1 (the SL4'-E hypothesis) and whether the draft's
# 'never above 0.65 of its budget' generalizes off the 17 points.
import mpmath as mp
mp.mp.dps = 35

def cums(m, lam):
    s2 = k3 = k4 = mp.mpf(0)
    for j in range(1, m+1):
        ws = [mp.e**(-lam*i) for i in range(j)]
        Z = mp.fsum(ws)
        mu = mp.fsum(i*x for i, x in enumerate(ws))/Z
        c2 = mp.fsum((i-mu)**2*x for i, x in enumerate(ws))/Z
        c3 = mp.fsum((i-mu)**3*x for i, x in enumerate(ws))/Z
        c4 = mp.fsum((i-mu)**4*x for i, x in enumerate(ws))/Z - 3*c2**2
        s2 += c2; k3 += c3; k4 += c4
    return s2, k3, k4

def He(n, x):
    return {3: x**3-3*x, 4: x**4-6*x**2+3, 6: x**6-15*x**4+45*x**2-15}[n](x) \
        if callable({}.get(n)) else {3: x**3-3*x, 4: x**4-6*x**2+3,
                                     6: x**6-15*x**4+45*x**2-15}[n]

def qhat(d, s2, k3, k4):
    g = mp.e**(-d*d/(2*s2))/mp.sqrt(2*mp.pi*s2); z = d/mp.sqrt(s2)
    return g*(1 + k3/(6*s2**mp.mpf('1.5'))*(z**3-3*z)
                + k4/(24*s2**2)*(z**4-6*z*z+3)
                + k3**2/(72*s2**3)*(z**6-15*z**4+45*z*z-15))

def eta_of(s2, k3, k4):
    q0 = qhat(0, s2, k3, k4); qm = qhat(-1, s2, k3, k4); qp = qhat(1, s2, k3, k4)
    return s2*((q0*q0 - qm*qp)/(qm*qp)) - 1

BAND = lambda w: ('W1' if w<=5 else 'W2' if w<=6 else 'W3' if w<=8 else
                  'W4' if w<=10 else 'W5' if w<=20 else 'W6b' if w<=40 else 'W7')
R31S = {'W1':1.0,'W2':1.2,'W3':1.5,'W4':1.7,'W5':2.0,'W6b':2.1,'W7':2.2}
R42S = {'W1':0.8,'W2':1.4,'W3':2.6,'W4':3.5,'W5':5.2,'W6b':6.0,'W7':6.6}

def probe(m, wstr):
    w = mp.mpf(wstr); lam = w/m
    if lam > mp.mpf('0.89'):
        print(f"  m={m} w={wstr}: lam > 0.89, out of band"); return None
    s2, k3, k4 = cums(m, lam)
    A = lam*lam*s2; u = 1/A
    e = eta_of(s2, k3, k4)
    b = BAND(float(w))
    price = R42S[b]/2 + mp.mpf('0.3')*R31S[b]**2 + lam*lam/2
    ratio = abs(e)/u/price
    print(f"  m={m} w={wstr} [{b}]: |eta|/u={float(abs(e)/u):.4f} price={float(price):.4f} "
          f"ratio={float(ratio):.4f} k4>0:{k4>0} {'<= 0.65' if ratio<=0.65 else '** > 0.65 **'}"
          f" {'PASS(<=1)' if ratio<=1 else '** VIOLATION **'}")
    return ratio

print("== [C1] cross-check vs prover nc2 at its own points (w = 4.9, 356.8; m = 401) ==")
probe(401, '4.9')      # prover: |eta|/u = 0.4503, ratio 0.6432
probe(401, '356.8')    # prover: |eta|/u = 0.9285, ratio 0.1804

print("\n== [C2] band RIGHT edges + w->4+ + exact-0.89 corner, m = 401 ==")
worst = 0
for wstr in ['4.001','5.0','6.0','8.0','10.0','20.0','40.0','356.89']:
    r = probe(401, wstr)
    if r is not None: worst = max(worst, float(r))
print(f"  worst ratio at the edge points = {worst:.4f}"
      f"   (draft SS0/SS3 claim 'never above 0.65 of its budget': {'HOLDS here' if worst <= 0.65 else 'FAILS at an off-sample point'})")

print("\n== [C3] scope spot-checks: m = 402 (CL threshold parity) and m = 1000 ==")
for (m, wstr) in [(402, '4.9'), (402, '5.0'), (1000, '5.0')]:
    probe(m, wstr)
