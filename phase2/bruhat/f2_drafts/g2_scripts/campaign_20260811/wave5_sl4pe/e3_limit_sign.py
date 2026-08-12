#!/usr/bin/env python3
# e3_limit_sign.py -- wave-5 SL4'-E: (i) certification of Lemma E.4 (limit-level
# fourth-cumulant positivity): G_4(4) > 0.23 with rigorous series tail bound,
# h_4(4) < 6, and the term-wise monotonicity fact behind G_4' > 0 on [4, oo);
# (ii) the sign-boundary bracket w* (record-only diagnostic); (iii) the
# lam -> 0 limit functions r31_lim, r42_lim, J_lim = roadmap table for the
# SL1' prover of hypothesis (E3), with per-band max vs J0(W).
#
# Limit frame (h_n(x) := x^n phi_n(x), phi_n(x) = sum_{k>=1} k^{n-1} e^{-kx};
# h_2(0+)=1, h_3(0+)=2, h_4(0+)=6):  at fixed w = m lam, lam -> 0,
#   lam^3 s2      -> G_2(w) = w   - pi^2/3 + sum_k e^{-kw} (w^2 + 2w/k + 2/k^2)
#   lam^4 kappa_3 -> G_3(w) = 2w  - pi^2   + sum_k e^{-kw} (k w^3 + 3w^2 + 6w/k + 6/k^2)
#   lam^5 kappa_4 -> G_4(w) = 6w  - 4pi^2  + sum_k e^{-kw} P(kw)/k^2 ,
#                    P(y) = y^4 + 4y^3 + 12y^2 + 24y + 24 ,
# hence r31 -> G_3/G_2, r42 -> G_4/G_2, J -> (G_3/G_2)^2 - G_4/(2 G_2).
import mpmath as mp
mp.mp.dps = 30
K = 300

def P4(y): return y**4 + 4*y**3 + 12*y*y + 24*y + 24
def G2(w): return w - mp.pi**2/3 + mp.fsum(mp.e**(-k*w)*(w*w + 2*w/k + 2/k**2) for k in range(1, K+1))
def G3(w): return 2*w - mp.pi**2 + mp.fsum(mp.e**(-k*w)*(k*w**3 + 3*w*w + 6*w/k + 6/k**2) for k in range(1, K+1))
def G4(w): return 6*w - 4*mp.pi**2 + mp.fsum(mp.e**(-k*w)*P4(k*w)/k**2 for k in range(1, K+1))
def h4(x):
    q = mp.e**(-x)
    return x**4 * q*(1 + 4*q + q*q)/(1-q)**4

print("== [1] Lemma E.4 certification ==")
g44 = G4(mp.mpf(4))
# rigorous tail bound for truncation at K, w >= 3.3: P(y) <= 2 y^4 for y >= 13.3
# (holds since 4/y+12/y^2+24/y^3+24/y^4 <= 1 there); term_k = e^{-kw}P(kw)/k^2
# <= 2 w^4 k^2 e^{-kw}; for w >= 3.3, k > K = 300: sum < 2 w^4 (K+1)^2
# e^{-(K+1)w}/(1 - e^{-w} ((K+2)/(K+1))^2) -- printed:
def tailbound(w):
    r = mp.e**(-w)*((K+2)/(K+1))**2
    return 2*w**4*(K+1)**2*mp.e**(-(K+1)*w)/(1-r)
print(f"  G_4(4) = {mp.nstr(g44, 12)}  (> 0.23: {g44 > mp.mpf('0.23')}); "
      f"series tail (k > {K}) < {mp.nstr(tailbound(mp.mpf(4)), 3)}")
print(f"  h_4(4) = {mp.nstr(h4(mp.mpf(4)), 10)}  (< 6: {h4(mp.mpf(4)) < 6})")
print("  term-wise fact: x phi_5(x) - 4 phi_4(x) = sum_k k^3 e^{-kx} (kx - 4) >= 0")
print("  for x >= 4 (every summand >= 0), so h_4' = x^3 (4 phi_4 - x phi_5) <= 0:")
xs = [mp.mpf(t)/10 for t in range(40, 121, 10)]
vals = [h4(x) for x in xs]
dec = all(vals[i] > vals[i+1] for i in range(len(vals)-1))
print("  h_4 on x = 4..12 step 1: " + " ".join(mp.nstr(v, 6) for v in vals) + f"  decreasing: {dec}")
grid = [4 + mp.mpf(k)/4 for k in range(0, 145)]
mins = min(6 - h4(x) for x in grid)
print(f"  G_4'(w) = 6 - h_4(w) on [4, 40]: min over grid = {mp.nstr(mins, 6)} "
      f"(>= 6 - h_4(4) = {mp.nstr(6 - h4(mp.mpf(4)), 6)} for all w >= 4 by the term-wise fact)")

print()
print("== [2] sign boundary w* of G_4 (record-only diagnostic) ==")
lo, hi = mp.mpf('3.3'), mp.mpf('3.5')
assert G4(lo) < 0 < G4(hi)
for _ in range(40):
    mid = (lo + hi)/2
    if G4(mid) < 0: lo = mid
    else: hi = mid
print(f"  G_4(3.3) = {mp.nstr(G4(mp.mpf('3.3')), 6)} < 0 < G_4(3.5) = {mp.nstr(G4(mp.mpf('3.5')), 6)}")
print(f"  w* = {mp.nstr((lo+hi)/2, 8)}  (the lam -> 0 kappa_4 sign boundary; "
      f"in-band w > 4 clears it by {mp.nstr(4 - (lo+hi)/2, 3)} in w)")

print()
print("== [3] lam -> 0 limit roadmap for hypothesis (E3): J_lim vs J0(W) ==")
J0 = {'W1': 0.682942, 'W2': 1.10268, 'W3': 1.91562, 'W4': 2.53645,
      'W5': 3.66793, 'W6b': 4.17806, 'W7': 4.59597}   # e1 certified (floats)
def band_of(w):
    w = float(w)
    return ('W1' if w<=5 else 'W2' if w<=6 else 'W3' if w<=8 else
            'W4' if w<=10 else 'W5' if w<=20 else 'W6b' if w<=40 else 'W7')
def Jlim(w):
    g2, g3, g4 = G2(w), G3(w), G4(w)
    return (g3/g2)**2 - g4/(2*g2), g3/g2, g4/g2
worst = {}
wgrid = ([4 + mp.mpf(k)/20 for k in range(0, 21)] +
         [5 + mp.mpf(k)/10 for k in range(1, 51)] +
         [10 + mp.mpf(k)/2 for k in range(1, 61)] +
         [mp.mpf(v) for v in (45, 50, 60, 80, 100, 150, 200, 300, 500, 1000)])
for w in wgrid:
    J, r3, r4 = Jlim(w)
    b = band_of(w)
    if b not in worst or J > worst[b][0]: worst[b] = (J, w, r3, r4)
for b in ['W1','W2','W3','W4','W5','W6b','W7']:
    J, w, r3, r4 = worst[b]
    print(f"  {b:3s}: max J_lim = {mp.nstr(J, 5)} at w = {mp.nstr(w, 5)} "
          f"(r31_lim = {mp.nstr(r3, 5)}, r42_lim = {mp.nstr(r4, 5)})  "
          f"vs J0 = {J0[b]:.4f}: margin {float(1 - J/J0[b])*100:.1f}%")
Jinf = (mp.mpf(2))**2 - mp.mpf(6)/2
print(f"  w -> oo limit: r31 -> 2, r42 -> 6, J -> {mp.nstr(Jinf, 3)}; the deep-tilt "
      f"(lam -> 0.89) corner is the 2D W7 direction, measured in e2 [B]/[C] (J <= 1.332)")
