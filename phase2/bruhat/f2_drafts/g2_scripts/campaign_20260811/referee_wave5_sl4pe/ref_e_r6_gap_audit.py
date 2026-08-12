#!/usr/bin/env python3
# ref_e_r6_gap_audit.py -- REFEREE (numerics, wave-5 sl4pe): quantify two
# commentary claims of the draft.
#  (a) S6 roadmap bullet 1: "The measured limit-vs-561 gap is <= 5e-4 in J"
#      -- measure J(m=561, w) - J_lim(w) at every W1-W6b band right edge
#      (the per-band J maxima), where the O(lam) discretization gap is
#      largest within each band.
#  (b) S3 sentence: envelope "100x-1000x looser than truth and still
#      30x-100x smaller than the budgets" -- compute REM*/REMact_worst,
#      (0.3 R31*^2)/REM*, and price/REM* per band.
import mpmath as mp
mp.mp.dps = 40
K = 800

def P4(y): return y**4 + 4*y**3 + 12*y*y + 24*y + 24
def G2(w): return w - mp.pi**2/3 + mp.fsum(mp.e**(-k*w)*(w*w + 2*w/k + 2/k**2) for k in range(1, K+1))
def G3(w): return 2*w - mp.pi**2 + mp.fsum(mp.e**(-k*w)*(k*w**3 + 3*w*w + 6*w/k + 6/k**2) for k in range(1, K+1))
def G4(w): return 6*w - 4*mp.pi**2 + mp.fsum(mp.e**(-k*w)*P4(k*w)/k**2 for k in range(1, K+1))
def phis(x):
    q = mp.e**(-x); r1 = 1 - q
    return q/r1**2, q*(1+q)/r1**3, q*(1+4*q+q*q)/r1**4
def cums(m, lam):
    p2, p3, p4 = phis(lam)
    s2 = m*p2; k3 = m*p3; k4 = m*p4
    for j in range(1, m+1):
        jl = j*lam
        if jl > 150: break
        q2, q3, q4 = phis(jl)
        s2 -= j**2*q2; k3 -= j**3*q3; k4 -= j**4*q4
    return s2, k3, k4

print("== (a) J(m=561, w) - J_lim(w) at W1-W6b right edges ==")
for w in (5, 6, 8, 10, 20, 40):
    lam = mp.mpf(w)/561
    s2, k3, k4 = cums(561, lam)
    r31 = abs(k3)*lam/s2; r42 = k4*lam*lam/s2
    J = r31**2 - r42/2
    g2v, g3v, g4v = G2(mp.mpf(w)), G3(mp.mpf(w)), G4(mp.mpf(w))
    Jl = (g3v/g2v)**2 - g4v/(2*g2v)
    print(f"  w = {w:2d}: J(561) = {mp.nstr(J, 8)}  J_lim = {mp.nstr(Jl, 8)}  "
          f"gap = {mp.nstr(J - Jl, 4)}  (<= 5e-4: {abs(J - Jl) <= mp.mpf('5e-4')})")

print()
print("== (b) envelope-vs-truth and envelope-vs-budget ratios ==")
REM = {'W1': 0.017058068129, 'W2': 0.029318577604, 'W3': 0.059379577439,
       'W4': 0.080548451464, 'W5': 0.132066143949, 'W6b': 0.144939416193,
       'W7': 0.156030179162}
R31 = {'W1': 1.0, 'W2': 1.2, 'W3': 1.5, 'W4': 1.7, 'W5': 2.0, 'W6b': 2.1, 'W7': 2.2}
R42 = {'W1': 0.8, 'W2': 1.4, 'W3': 2.6, 'W4': 3.5, 'W5': 5.2, 'W6b': 6.0, 'W7': 6.6}
# worst REMact per band over e2 [B] (m = 561 probe set, verified in re-run)
REMACT = {'W1': 9.97e-5, 'W2': 9.47e-5, 'W3': 8.85e-5, 'W4': 5.73e-5,
          'W5': 3.34e-5, 'W6b': 5.84e-6, 'W7': 9.59e-4}
for b in REM:
    slack = 0.3*R31[b]**2
    price = R42[b]/2 + 0.3*R31[b]**2
    print(f"  {b:3s}: REM*/REMact = {REM[b]/REMACT[b]:7.0f}x   (0.3R31*^2)/REM* = "
          f"{slack/REM[b]:5.1f}x   price/REM* = {price/REM[b]:5.1f}x")
