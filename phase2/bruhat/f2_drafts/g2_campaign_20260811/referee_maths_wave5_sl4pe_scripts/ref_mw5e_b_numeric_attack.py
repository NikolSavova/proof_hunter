#!/usr/bin/env python3
# ref_mw5e_b_numeric_attack.py -- MATHS REFEREE, wave5_sl4pe. Independent
# numeric attack at dps 50 via a DIFFERENT route from the prover's e2/e3:
# phi_n computed by direct series summation (not closed forms).
# [C] truth probes (m, w) incl. the binding W1 right edge and the deep corner;
# [D] Prop E.3 non-derivability point recomputed;
# [E] Lemma E.4 point values at dps 50, K = 800 (vs e3's dps 30, K = 300);
# [F] limit J at w = 5 (roadmap anchor 0.45984).
import mpmath as mp
mp.mp.dps = 50

def phi_series(n, x):        # sum_{k>=1} k^{n-1} e^{-kx}, direct summation
    s = mp.mpf(0); k = 1
    while True:
        t = mp.mpf(k)**(n-1)*mp.e**(-k*x)
        s += t
        if t < mp.mpf(10)**(-60)*max(s, mp.mpf(1)) and k > 3:
            return s
        k += 1

def cums(m, lam):
    s2 = m*phi_series(2, lam); k3 = m*phi_series(3, lam); k4 = m*phi_series(4, lam)
    for j in range(1, m+1):
        jl = j*lam
        if jl > 200 and j > 1:
            break
        s2 -= j**2*phi_series(2, jl); k3 -= j**3*phi_series(3, jl)
        k4 -= j**4*phi_series(4, jl)
    return s2, k3, k4

def He(n, x):
    return {3: x**3-3*x, 4: x**4-6*x*x+3, 6: x**6-15*x**4+45*x*x-15}[n]
def eta_of(s2, k3, k4):
    def qh(d):
        g = mp.e**(-d*d/(2*s2))/mp.sqrt(2*mp.pi*s2); z = d/mp.sqrt(s2)
        return g*(1 + k3/(6*s2**mp.mpf('1.5'))*He(3,z) + k4/(24*s2**2)*He(4,z)
                    + k3**2/(72*s2**3)*He(6,z))
    q0, qm, qp = qh(0), qh(-1), qh(1)
    return s2*((q0*q0 - qm*qp)/(qm*qp)) - 1

BAND = {'W1': (mp.mpf('1.0'), mp.mpf('0.8')), 'W7': (mp.mpf('2.2'), mp.mpf('6.6'))}
print("== [C] independent truth probes (series route, dps 50) ==")
for m, wstr, b in [(401, '4.9', 'W1'), (561, '5.0', 'W1'), (561, '4.5', 'W1'),
                   (561, '499.29', 'W7'), (1000, '5.0', 'W1')]:
    w = mp.mpf(wstr); lam = w/m
    s2, k3, k4 = cums(m, lam)
    A = lam*lam*s2; u = 1/A
    R31, R42 = BAND[b]
    r31 = abs(k3)*lam/s2; r42 = k4*lam*lam/s2
    J = r31**2 - r42/2
    e = eta_of(s2, k3, k4)
    price = R42/2 + mp.mpf('0.3')*R31**2 + lam*lam/2
    print(f"  m={m} w={wstr}: r31={mp.nstr(r31,6)} r42={mp.nstr(r42,6)} "
          f"J={mp.nstr(J,6)} |eta|/u={mp.nstr(abs(e)/u,6)} ratio={mp.nstr(abs(e)/u/price,6)} "
          f"k4>0:{k4>0}")

print()
print("== [D] Prop E.3 point recomputed (dps 50) ==")
m = 561; w = mp.mpf('4.5'); lam = w/m
s2x = mp.mpf('0.28')*m/lam**2
k3x = s2x/lam; k4x = mp.mpf(0)
e = eta_of(s2x, k3x, k4x); u = 1/(lam*lam*s2x)
price = mp.mpf('0.7') + lam*lam/2
print(f"  eta/u = {mp.nstr(e/u, 10)}   price = {mp.nstr(price, 10)}   "
      f"|eta|/(price*u) = {mp.nstr(abs(e)/u/price, 8)}  (> 1: {abs(e)/u/price > 1})")

print()
print("== [E] Lemma E.4 point values (dps 50, K = 800) ==")
K = 800
def P4(y): return y**4 + 4*y**3 + 12*y*y + 24*y + 24
def G4(w): return 6*w - 4*mp.pi**2 + mp.fsum(mp.e**(-k*w)*P4(k*w)/k**2 for k in range(1, K+1))
h44 = mp.mpf(256)*phi_series(4, mp.mpf(4))
print(f"  G_4(4)  = {mp.nstr(G4(mp.mpf(4)), 15)}   (e3 claimed 0.23234829889; > 0.23: {G4(mp.mpf(4)) > mp.mpf('0.23')})")
print(f"  h_4(4)  = {mp.nstr(h44, 13)}   (e3 claimed 5.420211696; < 6: {h44 < 6})")
print(f"  G_4(3.3) = {mp.nstr(G4(mp.mpf('3.3')), 6)}  G_4(3.5) = {mp.nstr(G4(mp.mpf('3.5')), 6)}  "
      f"(sign change: {G4(mp.mpf('3.3')) < 0 < G4(mp.mpf('3.5'))})")
# independent check of the kx>=4 termwise fact at a boundary point x = 4:
tw = mp.mpf(4)*phi_series(5, mp.mpf(4)) - 4*phi_series(4, mp.mpf(4))
print(f"  x phi_5 - 4 phi_4 at x = 4: {mp.nstr(tw, 6)} (>= 0: {tw >= 0})")

print()
print("== [F] limit J at w = 5 (roadmap anchor) ==")
def G2(w): return w - mp.pi**2/3 + mp.fsum(mp.e**(-k*w)*(w*w + 2*w/k + 2/k**2) for k in range(1, K+1))
def G3(w): return 2*w - mp.pi**2 + mp.fsum(mp.e**(-k*w)*(k*w**3 + 3*w*w + 6*w/k + 6/k**2) for k in range(1, K+1))
w = mp.mpf(5)
Jlim = (G3(w)/G2(w))**2 - G4(w)/(2*G2(w))
print(f"  J_lim(5) = {mp.nstr(Jlim, 8)}  (e3 claimed 0.45984)")
