#!/usr/bin/env python3
"""NC-PL1: cumulant-scale profiles on the residual band (architect sanity).
Per-factor exact moments of truncated geometrics via mpmath (dps 40).
Checks the constants to be stated in SL1 (kappa scales), SL2 (lam^2 s2 floor,
variance monotonicity in j, anchors), and the budget quantity 20*A/min(m,s2).
"""
import mpmath as mp
mp.mp.dps = 40

def factor_moments(j, lam):
    # U_j^lam on {0..j-1}, weights e^{-lam i}
    q = mp.e**(-lam)
    ws = [q**i for i in range(j)]
    Z = mp.fsum(ws)
    m1 = mp.fsum([i*w for i, w in enumerate(ws)])/Z
    c2 = mp.fsum([(i-m1)**2*w for i, w in enumerate(ws)])/Z
    c3 = mp.fsum([(i-m1)**3*w for i, w in enumerate(ws)])/Z
    c4 = mp.fsum([(i-m1)**4*w for i, w in enumerate(ws)])/Z - 3*c2**2
    return m1, c2, c3, c4

def sum_cumulants(m, lam):
    s2 = mp.mpf(0); k3 = mp.mpf(0); k4 = mp.mpf(0)
    for j in range(1, m+1):
        _, c2, c3, c4 = factor_moments(j, lam)
        s2 += c2; k3 += c3; k4 += c4
    return s2, k3, k4

print("== profiles at m=401 (and spot m=1581): A=lam^2*s2, R31=|k3|lam/s2, R42=|k4|lam^2/s2 ==")
print("m      w        lam        s2/m     A/m      R31      R42     20A/min(m,s2)")
for m, wlist in [(401, [4.2, 5, 6, 8, 10, 14, 20, 40, 80, 150, 250, 356.9]),
                 (1581, [4.2, 8, 20, 150, 1094])]:
    for w in wlist:
        lam = mp.mpf(w)/m
        if lam > mp.mpf('0.89'):
            continue
        s2, k3, k4 = sum_cumulants(m, lam)
        A = lam**2*s2
        budget = 20*A/min(mp.mpf(m), s2)
        print(f"{m:5d} {float(w):7.1f} {float(lam):9.5f} {float(s2/m):9.3f} "
              f"{float(A/m):7.4f} {float(abs(k3)*lam/s2):8.4f} "
              f"{float(abs(k4)*lam**2/s2):8.4f}  {float(budget):8.3f}")

print("\n== SL2 checks: Var(U_j^lam) monotone in j; anchors; ledger floor ==")
viol = 0
for lamf in ['0.01', '0.05', '0.1', '0.2', '0.4', '0.6', '0.89']:
    lam = mp.mpf(lamf)
    prev = mp.mpf(-1)
    for j in range(1, 61):
        _, c2, _, _ = factor_moments(j, lam)
        if c2 < prev - mp.mpf('1e-30'):
            viol += 1
            print(f"  VIOLATION lam={lamf} j={j}")
        prev = c2
print(f"variance-monotone-in-j violations (lam grid x j<=60): {viol}")
_, v3, _, _ = factor_moments(3, mp.mpf('0.89'))
print(f"anchor: Var(U_3^0.89)*lam^2 = {float(v3*mp.mpf('0.89')**2):.4f}  (>= 0.25 needed)")
# worst-case A/m over dense w-grid at m=401 (min over the band)
m = 401
worst = (None, mp.mpf(10))
for wi in [mp.mpf(4) + mp.mpf(k)/4 for k in range(0, 33)] + list(range(13, 357, 6)):
    lam = mp.mpf(wi)/m
    if lam > mp.mpf('0.89'):
        continue
    s2, _, _ = sum_cumulants(m, lam)
    r = lam**2*s2/m
    if r < worst[1]:
        worst = (float(wi), r)
print(f"min over band of lam^2*s2/m at m=401: {float(worst[1]):.4f} at w={worst[0]}")
# continuum block-route value at w=4 (what a prover can certify):
# lam^2 s2 >= m * (1/w) * sum over blocks [a_i,a_{i+1}] of (a_{i+1}-a_i)*v(a_i),
# v(a) = 1 - a^2 e^{-a}/(1-e^{-a})^2, using v at LEFT endpoints (safe: v increasing)
def vcont(a):
    a = mp.mpf(a)
    return 1 - a**2*mp.e**(-a)/(1 - mp.e**(-a))**2
blocks = [mp.mpf(k)/8 for k in range(0, 33)]  # [0,4] step 1/8
val = mp.fsum([(blocks[i+1]-blocks[i])*vcont(blocks[i]) for i in range(len(blocks)-1) if blocks[i] > 0])
print(f"block-route certified-style lower bound at w=4 (continuum): {float(val/4):.4f} * m")
