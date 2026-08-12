#!/usr/bin/env python3
"""SL2 / E3 -- float truth scan: band infima of A/m = lam^2 s2/m at
m = 401 and m = 802, compared against (truth >= E2 certified floor >=
stated c_A); plus a pointwise spot check of the master inequality
A/m >= V(w) - v(lam) (Lemma SL2.2), and the plan-consistency points.

A/m is computed from the exact identity of Lemma SL2.0:
    A/m = h(lam) - (1/m) sum_{j=1}^m h(j lam),   lam = w/m,
    h(x) = x^2 e^{-x}/(1 - e^{-x})^2.
Float display-grade; the PROOF constants are E2's exact rationals.
"""
import math

def h(x):
    ex = math.exp(-x)
    return x * x * ex / (1.0 - ex)**2

def v(x):
    return 0.0 if x == 0.0 else 1.0 - h(x)

def A_over_m(m, w):
    lam = w / m
    return h(lam) - sum(h(j * lam) for j in range(1, m + 1)) / m

def V_num(wv, steps=20000):
    """Midpoint rule for V(wv) -- display-grade confirmation only."""
    dx = wv / steps
    return sum(v((i + 0.5) * dx) for i in range(steps)) * dx / wv

BANDS = [("W1 ", 4.0, 5.0, 0.28), ("W2 ", 5.0, 6.0, 0.35),
         ("W3 ", 6.0, 8.0, 0.42), ("W4 ", 8.0, 10.0, 0.52),
         ("W5 ", 10.0, 20.0, 0.60), ("W6b", 20.0, 40.0, 0.70),
         ("W7 ", 40.0, None, 0.80)]
# E2 certified floors (floor-rounded prints of exact Fractions):
CERT = {"W1 ": 0.287499, "W2 ": 0.381808, "W3 ": 0.462885,
        "W4 ": 0.584512, "W5 ": 0.665138, "W6b": 0.831552,
        "W7 ": 0.852716}

for m in (401, 802):
    print("E3 truth scan at m = %d (201-point grid per band, plus w0+1e-6):"
          % m)
    print("    band   min A/m   at w      cert.floor  c_A   truth>=floor>=c_A")
    for name, w0, w1, ca in BANDS:
        hi = w1 if w1 is not None else 0.89 * m
        ws = [w0 + 1e-6] + [w0 + i * (hi - w0) / 200.0 for i in range(1, 201)]
        mn, wmin = min((A_over_m(m, w), w) for w in ws)
        ok = mn >= CERT[name] >= ca
        print("    %s   %.4f   %-8.4f  %.6f    %.2f  %s"
              % (name, mn, wmin, CERT[name], ca, "PASS" if ok else "FAIL"))

print("E3 band-edge value (outside the open band): A/m at w = 4.0, m = 401:"
      " %.4f   [NC-PL1 quotes 0.2992]" % A_over_m(401, 4.0))

print("E3 pointwise master-inequality spot check at m = 401")
print("   (all differences must be >= 0):")
for w in (4.2, 5.5, 7.0, 9.0, 15.0, 30.0, 100.0, 300.0):
    lam = w / 401
    lhs = A_over_m(401, w)
    rhs = V_num(w) - v(lam)
    print("   w = %6.1f : A/m = %.6f, V(w)-v(lam) = %.6f, diff = %+.6f"
          % (w, lhs, rhs, lhs - rhs))
