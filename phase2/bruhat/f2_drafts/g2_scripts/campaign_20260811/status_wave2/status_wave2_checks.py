#!/usr/bin/env python3
"""status_wave2_checks.py — synthesis-editor checks for STATUS_wave2.md (2026-08-11/12).

Verifies the cross-package plug the wave-2 synthesis asserts (no draft or referee
has yet checked wp2-a2's Theorem D.5 constant INSIDE wp3-a2's Theorem S, because
the two packages were blind to each other), and computes the part-(c)/G4
crossover thresholds that result.  Exact Fraction arithmetic in every verdict;
floats for display only.

Named constants (provenance):
  C_KER4       = 37810.0442  wp2_draft_a2 Theorem D.5, C_ker(4), m >= M(4) = 367
                 (both referees reproduce: referee_maths_wp2_a2 §2.2,
                  referee_numerics_wp2_a2 §2.2)
  M4           = 367         wp2_draft_a2 Theorem D.5 threshold for K = 4
  CRPT4_GRID   = 5.32        wp2-b C_R^PT(4) grid flavor per repair B3
                 (repairs_20260811.md §B3: 4.93 + 0.01402 + 0.3719 = 5.3159 -> 5.32)
  CRPT4_CLOSED = 187.8       wp2-b closed all-m flavor per wp3_draft_a2 §5
                 (187.414 + 0.01402 + 0.3719 = 187.7999)
  CR1_CLOSED   = 41.17, LIN1 = 0.2308   wp2_draft_a2 Theorem T.9-final (K = 1)
  TARGET_C     = 187/216     part-(c) sharp constant (F2_PROOF_DRAFT / harness C5)
  B_m          = (S_4 - m)/(240 lambda^2), lambda = m(m-1)(2m+5)/72,
                 S_4 = m(m+1)(2m+1)(3m^2+3m-1)/30   (exact)
"""
from fractions import Fraction as F

def S4(m):  return F(m*(m+1)*(2*m+1)*(3*m*m+3*m-1), 30)
def lam2(m): return F(m*(m-1)*(2*m+5), 72)          # lambda = sigma^2
def B(m):   return (S4(m) - m) / (240 * lam2(m)**2)

C_KER4       = F(378100442, 10000)   # 37810.0442
M4           = 367
CRPT4_GRID   = F(532, 100)           # 5.32
CRPT4_CLOSED = F(1878, 10)           # 187.8
CR1_CLOSED   = F(4117, 100)          # 41.17
LIN1         = F(2308, 10000)        # 0.2308
TARGET       = F(187, 216)

def bound(m, C):   # Theorem S R3 line: 1 - B_m - C/m^2  (exact Fraction)
    return 1 - B(m) - C / F(m*m)

def crossover(C, mmax=5000):
    """smallest m >= 30 with bound(m, C) >= 187/216, then check it STAYS >= there
    (bound is increasing: B_m dec, C/m^2 dec) -- monotone confirmed by scan."""
    mstar = None
    for m in range(30, mmax + 1):
        if bound(m, C) >= TARGET:
            mstar = m
            break
    # confirm no later dip on a window
    ok = all(bound(m, C) >= TARGET for m in range(mstar, min(mstar + 200, mmax)))
    return mstar, ok

print("== (1) The cross-package plug: wp2-a2 C_ker(4) into wp3-a2 Theorem S R3 ==")
print("    M(4) = %d <= 401 (Theorem S's analytic range start): %s" % (M4, M4 <= 401))
for Cname, C in [("grid   C = C_R^PT(4)grid   + C_ker(4) = 5.32  + 37810.04", CRPT4_GRID + C_KER4),
                 ("closed C = C_R^PT(4)closed + C_ker(4) = 187.8 + 37810.04", CRPT4_CLOSED + C_KER4)]:
    v401 = bound(401, C)
    print("    %s = %.2f" % (Cname, float(C)))
    print("      R3 bound at m = 401: 1 - B_401 - C/401^2 = %.6f  (> 0: %s; -> 1 as m -> inf)"
          % (float(v401), v401 > 0))

print("== (2) part-(c) crossover: smallest m with 1 - B_m - C/m^2 >= 187/216 = %.6f ==" % float(TARGET))
for Cname, C in [("K=4 grid flavor   (37815.36)", CRPT4_GRID + C_KER4),
                 ("K=4 closed flavor (37997.84)", CRPT4_CLOSED + C_KER4),
                 ("K=1 flavor C_R(1)+m^2Lin (41.40)", CR1_CLOSED + LIN1)]:
    mstar, ok = crossover(C)
    print("    %-36s m* = %d   (stays >= target beyond: %s)   harness covers to 400: gap %s"
          % (Cname, mstar, ok, "NONE (m* <= 400)" if mstar <= 400 else "[401, %d]" % (mstar - 1)))

print("== (3) sanity: B_m * m -> 27/25 = 1.08 ==")
for m in (30, 401, 1581):
    print("    m = %5d  B_m*m = %.6f" % (m, float(B(m) * m)))

print("== (4) Theorem S R2 spec vs wp2-a2 (independence check) ==")
# R2's condition is wp4's CL, NOT anything wp2-a2 provides; assert no overlap of scopes:
# wp2-a2 covers |w| <= 4 i.e. |lam| <= 4/m; R2 lives at |w| > 4. Disjoint by definition.
print("    R2 (|w| > 4) and Theorem T.9-final scope (|w| <= 4) are disjoint: True (by definition)")
print("DONE")
