#!/usr/bin/env python3
"""referee_checks_theoremA.py — MATHS REFEREE independent verification for
theoremA_assembly_20260811.md (wave 3). New file; nothing existing modified.

Independent of assembly_checks.py (own code paths, exact Fraction/integer
arithmetic for every verdict). Sections:

  (1) plug arithmetic: R3 bound 1 - B_m - C_A/m^2 at m = 401, both flavors;
      C_A sums from the cited components.
  (2) R2 budget: eps*, band budgets, conclusion, floors v(c)m; tilt caps via
      an independent exact lower bound on e^0.89 (22-term partial sum).
  (3) R3 w^2 bracket at the plugged C; AND the referee's B.0(ii)-based
      all-m >= 401 positivity proof (the assembly script only scans to 2000
      and appeals to unproved global B_m monotonicity beyond that).
  (4) R1a / R1b row values at m = 401.
  (5) H(4, 367) recompute; B_m*m values.
  (6) independent Mahonian rebuild to m = 40 (row-recurrence, different code
      shape from assembly block E): varfit(6) = 187/216, varfit(40), argmin.
  (7) the 27/25-form constant gap: (1.08/m - B_m)*m^2 measured — showing the
      B_m -> (27/25)/m replacement carries its own O(m^-2) constant (~0.53)
      which is NOT part of C_A and is nowhere explicit (finding MR-2).
  (8) crossover m* replication (G4 note only).
"""
from fractions import Fraction as F
import math

def S4(m):  return F(m*(m+1)*(2*m+1)*(3*m*m+3*m-1), 30)
def lam(m): return F(m*(m-1)*(2*m+5), 72)
def B(m):   return (S4(m) - m) / (240 * lam(m)**2)

C_KER4 = F(378100442, 10000)
GRID   = F(532, 100) + C_KER4          # 5.32 + 37810.0442
CLOSED = F(1878, 10) + C_KER4          # 187.8 + 37810.0442
E4     = F(248992, 100000000)
RHO4   = F(72711, 100000)
TARGET = F(187, 216)

print("(1) plug arithmetic")
print("  C_A grid   = %s = %.4f (doc: 37815.3642): %s" % (GRID, float(GRID), GRID == F(378153642, 10000)))
print("  C_A closed = %s = %.4f (doc: 37997.8442): %s" % (CLOSED, float(CLOSED), CLOSED == F(379978442, 10000)))
for tag, C in (("grid", GRID), ("closed", CLOSED)):
    v = 1 - B(401) - C / F(401*401)
    print("  R3(401) %-6s = %.6f  (doc %s)" % (tag, float(v), "0.762141" if tag == "grid" else "0.761006"))

print("(2) R2 budget")
eps = 1 - F(102, 100) * RHO4
print("  eps* = %s = %.7f (doc 0.2583478): %s" % (eps, float(eps), eps == F(1291739, 5000000)))
f1 = F(7,10) * (1 + F(7,10)) / 6 * 401          # v(7/10)*401
f2 = F(1,3) * 1581
print("  v(7/10)*401 = %s = %.4f >= 79: %s ; v(1)*1581 = %s >= 527: %s"
      % (f1, float(f1), f1 >= 79, f2, f2 >= 527))
b1, b2 = F(20,1)/F(795,10), F(136, 527)
print("  band1 20/79.5 = %.6f <= eps*: %s ; band2 136/527 = %.7f <= eps*: %s (margin %.2e)"
      % (float(b1), b1 <= eps, float(b2), b2 <= eps, float(eps - b2)))
print("  R2 concl (1-20/79.5)/rho = %.6f >= 1.02: %s" % (float((1-b1)/RHO4), (1-b1)/RHO4 >= F(102,100)))
elo = sum(F(89,100)**n / math.factorial(n) for n in range(22))   # 22 terms, indep of doc's 18
print("  e^0.89 > %.9f ; > 17/7: %s ; > 2: %s  => log(17/7), log2 < 0.89"
      % (float(elo), elo > F(17,7), elo > 2))

print("(3) R3 w^2 bracket")
def bracket(m, C): return F(685,100)*E4*(1 - 17*B(m) - C/F(m*m)) - B(m)
for tag, C in (("grid", GRID), ("closed", CLOSED)):
    print("  bracket(401) %-6s = %.6f > 0: %s" % (tag, float(bracket(401, C)), bracket(401, C) > 0))
# referee's all-m proof via B.0(ii) (B_m <= 1.080/m, m >= 30; g1_draft_b, proof-grade):
# bracket(m) >= g(m) := 6.85*E4*(1 - 17*1.080/m - C/m^2) - 1.080/m, g increasing in m.
def g(m, C): return F(685,100)*E4*(1 - 17*F(1080,1000)/m - C/F(m*m)) - F(1080,1000)/m
for tag, C in (("grid", GRID), ("closed", CLOSED)):
    g401 = g(401, C)
    incr = all(g(m+1, C) > g(m, C) for m in (401, 1000, 5000, 10**5))  # term-by-term monotone anyway
    print("  B.0(ii) floor g(401) %-6s = %.6f > 0: %s (g term-by-term increasing: %s)"
          % (tag, float(g401), g401 > 0, incr))
print("  [g > 0 for ALL m >= 401 follows: each of -1/m, -1/m^2 terms increases in m]")
# check the assembly's monotonicity appeal really was only scan-based:
print("  1 - 17*B(401) - C_grid/401^2 = %.4f > 0 (chain multiplier validity)" % float(1 - 17*B(401) - GRID/F(401*401)))

print("(4) R1a/R1b at m = 401")
r1a = lam(401) * F(400, 2*402)
print("  R1a: lambda*400/804 = %.1f >= 1e5: %s" % (float(r1a), r1a >= 100000))
r1b = F(400*400*807, 1) / (F(144) * F(7,10) * F(17,10) * 401)
print("  R1b: (m-1)^2(2m+5)/(144 c(1+c) m) = %.1f (doc: 1879)" % float(r1b))

print("(5) H(4, 367) and B_m*m")
H4 = B(367) * 17 + F(37998) / F(367*367)
print("  H(4,367) = %.4f <= 1/2: %s (doc 0.3321)" % (float(H4), H4 <= F(1,2)))
print("  B_m*m: m=401: %.6f ; m=100000: %.6f (doc 1.078693 / 1.079995)"
      % (float(B(401)*401), float(B(100000)*100000)))

print("(6) independent Mahonian rebuild to m = 40")
row = [1]
for mm in range(2, 41):
    # I_m = I_{m-1} * (1+q+...+q^{mm-1}) via cumulative sums (independent shape)
    cum = [0]*(len(row)+1)
    for i, v in enumerate(row): cum[i+1] = cum[i] + v
    row = [cum[min(i+1, len(row))] - cum[max(0, i+1-mm)] for i in range(len(row)+mm-1)]
    if mm in (6, 40):
        N = mm*(mm-1)//2
        assert row == row[::-1] and len(row) == N+1
        best, bn, bd = None, None, None
        for k in range(1, N):
            n_, d_ = row[k]*row[k], row[k-1]*row[k+1]
            if best is None or n_*bd < bn*d_: best, bn, bd = k, n_, d_
        vf = lam(mm) * (F(bn, bd) - 1)
        print("  m=%d: argmin=%d (central %d), varfit=%s%s" % (mm, best, N//2,
              float(vf), " == 187/216: %s" % (vf == TARGET) if mm == 6 else " (doc 0.973381)"))

print("(7) the 27/25-form constant (finding MR-2 evidence)")
for m in (401, 1000, 10000, 100000):
    d = (F(108,100)/m - B(m)) * m * m
    print("  m=%6d  (1.08/m - B_m)*m^2 = %.4f" % (m, float(d)))
print("  => |B_m - (27/25)/m| ~ 0.53/m^2: real, O(m^-2), but its explicit constant is")
print("     NOT in C_A and nowhere displayed; B.0(ii) gives only 0.012/m at this scale.")

print("(8) G4 crossovers (replication)")
for tag, C in (("grid", GRID), ("closed", CLOSED)):
    ms = next(m for m in range(6, 6000) if 1 - B(m) - C/F(m*m) >= TARGET)
    print("  %-6s m* = %d (doc: %s)" % (tag, ms, "535" if tag == "grid" else "537"))
print("DONE")
