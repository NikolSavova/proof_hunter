#!/usr/bin/env python3
# ref_e_r5_e4_limits.py -- REFEREE (numerics, wave-5 sl4pe): independent
# verification of Lemma E.4 (limit-level kappa_4 positivity) and of the
# e3_limit_sign.py limit machinery.  dps 60, K = 1200 (vs prover's 30/300).
#   [1] G_4(4), h_4(4), tail bound; structural identities G_4(0) = 0,
#       G_4' = 6 - h_4 (finite differences), G_4(w) = int_0^w (6 - h_4).
#   [2] w* bracket by independent bisection.
#   [3] Riemann-limit claims: lam^3 s2 -> G_2, lam^4 k3 -> G_3,
#       lam^5 k4 -> G_4 at w = 5 with m = 2000 / 20000 (finite-m truth from
#       the cross-validated phi route).
#   [4] limit-table spot values quoted in the draft; P(y) <= 2 y^4 for
#       y >= 13.3; actual truncation tail vs the claimed bound.
import mpmath as mp
mp.mp.dps = 60
K = 1200

def P4(y): return y**4 + 4*y**3 + 12*y*y + 24*y + 24
def G2(w): return w - mp.pi**2/3 + mp.fsum(mp.e**(-k*w)*(w*w + 2*w/k + 2/k**2) for k in range(1, K+1))
def G3(w): return 2*w - mp.pi**2 + mp.fsum(mp.e**(-k*w)*(k*w**3 + 3*w*w + 6*w/k + 6/k**2) for k in range(1, K+1))
def G4(w): return 6*w - 4*mp.pi**2 + mp.fsum(mp.e**(-k*w)*P4(k*w)/k**2 for k in range(1, K+1))
def h4(x):
    q = mp.e**(-x)
    return x**4*q*(1 + 4*q + q*q)/(1-q)**4

print("== [1] Lemma E.4 point values (dps 60, K = 1200) ==")
g44 = G4(mp.mpf(4))
print(f"  G_4(4)     = {mp.nstr(g44, 20)}   (draft: 0.23234829889; > 0.23: {g44 > mp.mpf('0.23')})")
print(f"  h_4(4)     = {mp.nstr(h4(mp.mpf(4)), 20)}   (draft: 5.420211696; < 6: {h4(mp.mpf(4)) < 6})")
print(f"  6 - h_4(4) = {mp.nstr(6 - h4(mp.mpf(4)), 12)}   (draft: 0.5798 / 0.579788)")
print(f"  G_4(0+) sanity: -4 pi^2 + 24 zeta(2) = {mp.nstr(-4*mp.pi**2 + 24*mp.zeta(2), 5)} (should be 0)")
# G_4' = 6 - h_4 via central differences at w = 4, 6, 10
for w in (4, 6, 10):
    w = mp.mpf(w); h = mp.mpf('1e-15')
    fd = (G4(w+h) - G4(w-h))/(2*h)
    print(f"  G_4'({w}) fd = {mp.nstr(fd, 15)} vs 6 - h_4 = {mp.nstr(6-h4(w), 15)} "
          f"(match: {abs(fd - (6-h4(w))) < mp.mpf('1e-25')})")
# integral identity
I = mp.quad(lambda t: 6 - h4(t), [mp.mpf('1e-12'), 1, 2, 3, 4])
print(f"  int_0^4 (6 - h_4) = {mp.nstr(I, 15)} vs G_4(4) = {mp.nstr(g44, 15)} "
      f"(match to quad tol: {abs(I - g44) < mp.mpf('1e-20')})")

print()
print("== [2] independent w* bisection (dps 60) ==")
lo, hi = mp.mpf('3.3'), mp.mpf('3.5')
assert G4(lo) < 0 < G4(hi)
for _ in range(120):
    mid = (lo+hi)/2
    if G4(mid) < 0: lo = mid
    else: hi = mid
print(f"  w* = {mp.nstr((lo+hi)/2, 12)}   (draft: 3.367175; < 4: True)")
print(f"  G_4(3.3) = {mp.nstr(G4(mp.mpf('3.3')), 8)}  G_4(3.5) = {mp.nstr(G4(mp.mpf('3.5')), 8)}")

print()
print("== [3] Riemann-limit claims at w = 5 (finite-m phi-route truth) ==")
def phis(x):
    q = mp.e**(-x); r1 = 1 - q
    return q/r1**2, q*(1+q)/r1**3, q*(1+4*q+q*q)/r1**4
def cums(m, lam):
    p2, p3, p4 = phis(lam)
    s2 = m*p2; k3 = m*p3; k4 = m*p4
    for j in range(1, m+1):
        jl = j*lam
        if jl > 200: break
        q2, q3, q4 = phis(jl)
        s2 -= j**2*q2; k3 -= j**3*q3; k4 -= j**4*q4
    return s2, k3, k4
w5 = mp.mpf(5)
tg2, tg3, tg4 = G2(w5), G3(w5), G4(w5)
for m in (2000, 20000):
    lam = w5/m
    s2, k3, k4 = cums(m, lam)
    print(f"  m={m}: lam^3 s2 = {mp.nstr(lam**3*s2, 10)} vs G_2(5) = {mp.nstr(tg2, 10)} "
          f"(gap {mp.nstr(abs(lam**3*s2 - tg2), 3)})")
    print(f"         lam^4 k3 = {mp.nstr(lam**4*k3, 10)} vs G_3(5) = {mp.nstr(tg3, 10)} "
          f"(gap {mp.nstr(abs(lam**4*k3 - tg3), 3)})")
    print(f"         lam^5 k4 = {mp.nstr(lam**5*k4, 10)} vs G_4(5) = {mp.nstr(tg4, 10)} "
          f"(gap {mp.nstr(abs(lam**5*k4 - tg4), 3)})")
r31l, r42l = tg3/tg2, tg4/tg2
print(f"  limit at w=5: r31_lim = {mp.nstr(r31l, 8)} (draft 0.88544), "
      f"r42_lim = {mp.nstr(r42l, 8)} (draft 0.64832), "
      f"J_lim = {mp.nstr(r31l**2 - r42l/2, 8)} (draft 0.45984)")

print()
print("== [4] limit-table spots, P-cap, actual tail vs claimed bound ==")
for w, expJ in [(6, '0.54987'), (8, '0.66427'), (10, '0.72327'), (20, '0.84187'),
                (40, '0.91841'), (1000, '0.99671')]:
    g2v, g3v, g4v = G2(mp.mpf(w)), G3(mp.mpf(w)), G4(mp.mpf(w))
    J = (g3v/g2v)**2 - g4v/(2*g2v)
    print(f"  w = {w}: J_lim = {mp.nstr(J, 6)}  (e3 quotes {expJ})")
y = mp.mpf('13.3')
print(f"  P(y)/(2 y^4) at y = 13.3: {mp.nstr(P4(y)/(2*y**4), 6)} (<= 1: {P4(y) <= 2*y**4}); "
      f"P monotone-ratio => cap holds for all y >= 13.3")
# actual truncation tail of G_4 at K0 = 300, w = 4 vs prover's bound 6.08e-516
K0 = 300
tail_actual = mp.fsum(mp.e**(-k*mp.mpf(4))*P4(k*mp.mpf(4))/k**2 for k in range(K0+1, K0+200))
r = mp.e**(-mp.mpf(4))*((K0+2)/(K0+1))**2
bound = 2*mp.mpf(4)**4*(K0+1)**2*mp.e**(-(K0+1)*mp.mpf(4))/(1-r)
print(f"  actual tail (k in 301..500) = {mp.nstr(tail_actual, 4)}; prover bound = "
      f"{mp.nstr(bound, 4)}; actual <= bound: {tail_actual <= bound}")
