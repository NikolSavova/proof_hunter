#!/usr/bin/env python3
"""ref_r1_margins.py — referee addendum: exact R1a/R1b margin checks for
theoremA_assembly_20260811.md §2.3 rows R1a ('>= 10^5 at m >= 401') and
R1b ('>= 1879 at m = 401'). Exact Fractions; floats display-only."""
from fractions import Fraction as F

m = 401
lam = F(m*(m-1)*(2*m+5), 72)
print("lambda(401) =", lam, "=", float(lam))
r1a = lam * F(m-1, 2*(m+1))
print("R1a: lambda*(m-1)/(2(m+1)) = %.1f >= 1e5: %s" % (float(r1a), r1a >= 100000))
# R1b: lambda*(m-1)/(2k(m+k)) minimized over the band k <= cm (c = 7/10).
# integer worst case k = floor(0.7*401) = 280; safe continuous floor k = cm exactly:
k_int = 280
r1b_int = lam * F(m-1, 2*k_int*(m+k_int))
c = F(7, 10)
kc = c * m                                    # 280.7 exactly
r1b_cont = lam * (m - 1) / (2 * kc * (m + kc))
print("R1b integer k=280:      %.1f" % float(r1b_int))
print("R1b continuous k=280.7: %.2f >= 1879: %s (doc/NC-P4 floor 1879 safe: %s)"
      % (float(r1b_cont), r1b_cont >= 1879, r1b_cont >= 1879))
print("both R1a/R1b exceed 1.02 by >= 1842x: %s" % (min(r1a, r1b_cont) / F(102, 100) >= 1842))
print("DONE")
