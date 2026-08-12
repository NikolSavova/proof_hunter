#!/usr/bin/env python3
"""SL2 / E2 -- rigorous exact-rational certificate for the banded floor
(Theorem SL2.4 = SL2(ii) of wp4_sl_SL2.md), via the master inequality
(Lemma SL2.2):
    A/m = lam^2 s2 / m >= V(w) - v(lam),   w = m lam,
with v(a) = 1 - h(a), h(a) = a^2 e^a/(e^a - 1)^2 (v strictly increasing),
V(w) = (1/w) int_0^w v(x) dx (increasing).

Certificates (all exact Fractions, safe-direction rounding only):
  (a) LBV(w0) <= V(w0), w0 in {4, 5, 6, 8, 10, 20, 40}: left-endpoint
      Riemann sum of the increasing integrand v, step 1/8. At each node
      a = k/8, h(a) is bounded ABOVE by a^2 g(E_lo(k)), where
      g(E) = E/(E-1)^2 is strictly decreasing for E > 1 and
      E_lo(k) = (rational lower bound for e^{1/8})^k <= e^{k/8}; the bound
      is then rounded UP at 12 decimals (still an upper bound on h(a),
      hence 1 - (rounded bound) is still a lower bound on v(a)).
  (b) UBv(cap) >= v(cap) at the per-band tilt caps
      cap in {5/401, 6/401, 8/401, 10/401, 20/401, 40/401, 89/100}:
      h(cap) bounded BELOW via a rational UPPER bound on e^{cap},
      rounded DOWN at 12 decimals.
  (c) per band: floor := LBV(w0) - UBv(cap) >= c_A(band); margins printed.
  (d) corollary arithmetic for SL2(iii): 0.28*401/0.89^2 vs 141;
      0.80/0.89^2 vs 1; per-band chains c_A * m / cap^2 at m = 401.
e^t brackets (0 < t <= 1): Taylor to N = 18 with the explicit tail cap
  0 < e^t - S_N(t) <= t^{N+1}/(N+1)! * 1/(1 - t/(N+2)).
"""
from fractions import Fraction
from math import floor

N_TAYLOR = 18

def exp_interval(t):
    """Return (lo, hi) exact Fractions with lo <= e^t <= hi, 0 < t <= 1."""
    assert Fraction(0) < t <= 1
    term = Fraction(1)
    S = Fraction(1)
    for n in range(1, N_TAYLOR + 1):
        term = term * t / n
        S += term
    tail = term * t / (N_TAYLOR + 1) / (1 - t / (N_TAYLOR + 2))
    return S, S + tail

def g(E):
    """E/(E-1)^2, strictly decreasing for E > 1."""
    return E / (E - 1)**2

def fceil(x, digits=12):
    d = 10**digits
    return Fraction(-floor(-x * d), d)

def ffloor(x, digits=12):
    d = 10**digits
    return Fraction(floor(x * d), d)

def show_dn(x, places=6):
    """Floor-rounded decimal print (safe for lower bounds)."""
    d = 10**places
    return "%.*f" % (places, floor(x * d) / d)

def show_up(x, places=8):
    """Ceil-rounded decimal print (safe for upper bounds)."""
    d = 10**places
    return "%.*f" % (places, -floor(-x * d) / d)

E8lo, E8hi = exp_interval(Fraction(1, 8))
print("E2.0 e^(1/8) bracket: lo = %.15f, width <= %.3e"
      % (float(E8lo), float(E8hi - E8lo)))

# (a) left-endpoint lower Riemann sums, nodes a = k/8, k = 0..319
targets = {32: 4, 40: 5, 48: 6, 64: 8, 80: 10, 160: 20, 320: 40}
LBV = {}
vlo_sum = Fraction(0)
Elo_k = Fraction(1)          # = E8lo^k at the top of iteration k
for k in range(320):
    if k > 0:
        a = Fraction(k, 8)
        h_hi = fceil(a * a * g(Elo_k))   # e^a >= E8lo^k, g decreasing
        vlo = 1 - h_hi
        if vlo < 0:
            vlo = Fraction(0)
        vlo_sum += vlo
    if (k + 1) in targets:               # k+1 nodes processed = 8*w0
        w0 = targets[k + 1]
        LBV[w0] = vlo_sum / 8 / w0
    Elo_k = Elo_k * E8lo

# (b), (c) per-band caps and the certificate table
caps = {4: Fraction(5, 401), 5: Fraction(6, 401), 6: Fraction(8, 401),
        8: Fraction(10, 401), 10: Fraction(20, 401), 20: Fraction(40, 401),
        40: Fraction(89, 100)}
cA = {4: Fraction(28, 100), 5: Fraction(35, 100), 6: Fraction(42, 100),
      8: Fraction(52, 100), 10: Fraction(60, 100), 20: Fraction(70, 100),
      40: Fraction(80, 100)}
names = {4: "W1  (4,5]  ", 5: "W2  (5,6]  ", 6: "W3  (6,8]  ",
         8: "W4  (8,10] ", 10: "W5  (10,20]", 20: "W6b (20,40]",
         40: "W7  (40,oo)"}
print("E2.1 band certificates (exact Fractions; prints floor-rounded for")
print("     lower bounds, ceil-rounded for upper bounds):")
print("     band        w0  LBV(w0)   cap     UBv(cap)    floor     c_A   margin  verdict")
all_ok = True
floors = {}
for w0 in (4, 5, 6, 8, 10, 20, 40):
    cap = caps[w0]
    lo, hi = exp_interval(cap)
    h_lo = ffloor(cap * cap * g(hi))     # e^cap <= hi, g decreasing
    UBv = 1 - h_lo
    fl = LBV[w0] - UBv
    floors[w0] = fl
    margin = fl - cA[w0]
    ok = margin > 0
    all_ok = all_ok and ok
    print("     %s %3d  %s  %-7s %s  %s  %.2f  %s  %s"
          % (names[w0], w0, show_dn(LBV[w0]), str(cap), show_up(UBv),
             show_dn(fl), float(cA[w0]), show_dn(margin),
             "PASS" if ok else "FAIL"))
print("E2.2 all seven bands PASS: %s" % all_ok)

# (d) corollary arithmetic
s2_crude = Fraction(28, 100) * 401 / Fraction(89, 100)**2
print("E2.3 crude global chain 0.28*401/0.89^2 = %s = %s >= 141: %s"
      % (s2_crude, show_dn(s2_crude, 4), s2_crude >= 141))
ratio = Fraction(80, 100) / Fraction(89, 100)**2
print("E2.4 W7 chain c_A(W7)/0.89^2 = %s = %s > 1: %s"
      % (ratio, show_dn(ratio, 6), ratio > 1))
print("E2.5 per-band chains  s2 >= c_A(band) * 401 / cap^2  at m = 401")
print("     (cap = w1/401 on the finite bands, 89/100 on W7):")
worst = None
for w0 in (4, 5, 6, 8, 10, 20, 40):
    chain = cA[w0] * 401 / caps[w0]**2
    worst = chain if worst is None else min(worst, chain)
    print("     %s : s2 >= %s" % (names[w0], show_dn(chain, 2)))
print("     minimum over bands (attained on W7): s2 >= %s ;"
      % show_dn(worst, 2))
print("     per-m, the W7 chain reads s2 >= (8000/7921) m = 1.009973... m"
      " > m.")
