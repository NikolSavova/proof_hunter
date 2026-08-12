#!/usr/bin/env python3
"""assembly_checks.py — independent re-verification for theoremA_assembly_20260811.md
(wave 3, 2026-08-11/12).

Re-derives, in exact Fraction/integer arithmetic wherever a verdict depends on it,
every synthesis-level number the assembly document states:

  (A) the cross-package plug: wp2-a2 Theorem D.5's C_ker(4) into wp3-a2 Theorem S's
      R3 row (STATUS_wave2 §2 plug note), independently of status_wave2_checks.py;
  (B) the part-(c)/G4 crossover thresholds m* (a caveat for G4, NOT for Theorem A);
  (C) Theorem S's R2 error-budget arithmetic with the REPAIRED constants
      (wp3-a2 repair R2: rho(4) <= 0.72711), incl. exact tilt-cap proofs
      log(17/7) < 0.89 and log 2 < 0.89 via positive-series lower bounds of e^0.89;
  (D) positivity of the R3 w^2-bracket WITH the actual plugged C_ker(4) (the
      wp3-a2 derivation-note-2 bracket was written before C_ker landed);
  (E) an independent exact rebuild of the Mahonian harness on 4 <= m <= 60,
      re-anchoring the harness_m200_20260811.md claims C2/C3/C5/C6 on the overlap;
  (F) B_m * m -> 27/25 and H(4, 367) (wp2-a2 NC-A5(2)'s Lin-discharge value).

Constants (provenance):
  C_KER4 = 37810.0442   wp2_draft_a2 Theorem D.5 (per-piece table row m=367, K=4);
                        constant flavor C_ker(4) = 37811 is the safe round-up
  M4 = 367              wp2_draft_a2 Theorem D.5 threshold M(4)
  CRPT4_GRID = 5.32     wp2-b C_R^PT(4) grid flavor per repair B3 (PW+T+Lin)
  CRPT4_CLOSED = 187.8  wp2-b closed all-m flavor (187.414 + 0.01402 + 0.3719)
  CR1 = 41.17, LIN1m2 = 0.2308   wp2_draft_a2 Theorem T.9-final, K = 1
  CR4_CLOSED = 37998, CR4_GRID = 37815   wp2_draft_a2 Theorem T.9-final, K = 4
  RHO4 = 0.72711        wp3-a2 P.7 rho(4) as REPAIRED (referee R2/F1 reprint)
  E4 = 0.00248992       wp3-a2 P.7 certified lower decimal for E(4) (safe as printed)
  C0S = 79, CS = 20, LAMS = 0.89   the CL spec (wp3_draft_a2 §6.1, frozen)
  TARGET = 187/216      part-(c) sharp constant (F2_PROOF_DRAFT / harness C5)
Exact formulas: lambda = m(m-1)(2m+5)/72, S_4 = m(m+1)(2m+1)(3m^2+3m-1)/30,
  B_m = (S_4 - m)/(240 lambda^2).
"""
from fractions import Fraction as F
import math

def S4(m):   return F(m*(m+1)*(2*m+1)*(3*m*m+3*m-1), 30)
def lam(m):  return F(m*(m-1)*(2*m+5), 72)            # lambda = sigma^2 (exact)
def B(m):    return (S4(m) - m) / (240 * lam(m)**2)   # B_m (exact Fraction)

C_KER4       = F(378100442, 10000)   # 37810.0442 (m = 367 value; round-up 37811)
M4           = 367
CRPT4_GRID   = F(532, 100)
CRPT4_CLOSED = F(1878, 10)
CR1          = F(4117, 100)
LIN1m2       = F(2308, 10000)
CR4_CLOSED   = F(37998)
CR4_GRID     = F(37815)
RHO4         = F(72711, 100000)      # repaired rho(4) upper bound
E4           = F(248992, 100000000)  # certified LOWER bound for E(4)
TARGET       = F(187, 216)

def r3_bound(m, C):  # Theorem S final display: 1 - B_m - C/m^2
    return 1 - B(m) - C / F(m*m)

print("== (A) the plug: C_ker(4) [wp2-a2 D.5] into Theorem S R3 [wp3-a2] ==")
print("  A1. scope: M(4) = %d <= 401 = Theorem S analytic start: %s" % (M4, M4 <= 401))
print("      D.5 band |w| <= 4 == R3 band |w| <= 4 (w-uniform, T.9-final note): True by statement")
for name, C in [("grid   C = 5.32 + 37810.0442", CRPT4_GRID + C_KER4),
                ("closed C = 187.8 + 37810.0442", CRPT4_CLOSED + C_KER4)]:
    v = r3_bound(401, C)
    print("  A2. %s = %.4f ; R3 bound at m=401 = %.6f (>0: %s)"
          % (name, float(C), float(v), v > 0))
# monotonicity of the bound in m (B_m and C/m^2 both decrease):
mono = all(B(m) > B(m+1) for m in range(401, 3001))
print("  A3. B_m strictly decreasing on [401, 3001] (exact scan): %s ;"
      " C/m^2 trivially decreasing => R3 bound increasing -> 1" % mono)

print("== (B) part-(c)/G4 crossovers: smallest m with 1 - B_m - C/m^2 >= 187/216 ==")
for name, C in [("K=4 grid   (C = 37815.3642)", CRPT4_GRID + C_KER4),
                ("K=4 closed (C = 37997.8442)", CRPT4_CLOSED + C_KER4),
                ("K=1 center (C = 41.17 + 0.2308)", CR1 + LIN1m2)]:
    mstar = next(m for m in range(6, 6000) if r3_bound(m, C) >= TARGET)
    stays = all(r3_bound(m, C) >= TARGET for m in range(mstar, mstar + 300))
    print("  %-32s m* = %d (stays beyond: %s; harness gap: %s)"
          % (name, mstar, stays,
             "NONE" if mstar <= 400 else "[401, %d]" % (mstar - 1)))

print("== (C) Theorem S R2 budget, REPAIRED constants (rho(4) <= 0.72711) ==")
v07 = F(7, 10) * F(17, 10) / 6            # v(7/10) = c(1+c)/6 = 119/600
v1  = F(1, 3)
f1  = v07 * 401                            # s2 floor, band [401, 1581)
f2  = v1 * 1581                            # s2 floor, band [1581, inf)
eps_star = 1 - F(102, 100) * RHO4
print("  C1. s2 floors: v(7/10)*401 = %s = %.4f >= 79 (C_0* met: %s);"
      % (f1, float(f1), f1 >= 79))
print("      v(1)*1581 = %s = %.1f >= 527" % (f2, float(f2)))
print("  C2. eps* = 1 - 1.02*rho = %s = %.7f" % (eps_star, float(eps_star)))
b1 = F(20, 1) / F(795, 10)                 # 20/79.5 (draft's floored value)
b1x = F(20, 1) / f1                        # exact-floor version
b2 = F(136, 1) / f2                        # band-2 budget 136/527
print("  C3. band-1 budget 20/79.5 = %.6f  (exact-floor 20/%.4f = %.6f)  <= eps*: %s / %s"
      % (float(b1), float(f1), float(b1x), b1 <= eps_star, b1x <= eps_star))
print("      band-2 budget 136/527 = %.7f <= eps*: %s  (margin %.2e)"
      % (float(b2), b2 <= eps_star, float(eps_star - b2)))
concl = (1 - b1) / RHO4
print("  C4. R2 conclusion (1 - 20/79.5)/rho = %.6f >= 1.02: %s"
      % (float(concl), concl >= F(102, 100)))
# C5: tilt caps, PROVED via exact positive-series lower bound of e^0.89:
elo = sum(F(89, 100)**n / math.factorial(n) for n in range(0, 18))  # < e^0.89
print("  C5. e^0.89 > %.9f (18-term positive partial sum, exact Fractions)" % float(elo))
print("      17/7 = %.9f < e^0.89 => log(17/7) < 0.89 (cap, c=7/10): %s"
      % (float(F(17, 7)), F(17, 7) < elo))
print("      2 < e^0.89 => log 2 < 0.89 (cap, c=1): %s" % (F(2) < elo))
print("      => Lambda* = 0.89 covers every residual-band tilt (Lemma P.8): True")

print("== (D) R3 w^2-bracket WITH the plugged C (positivity => w^2 term discardable) ==")
def bracket(m, C):   # 6.85*E(4)*(1 - 17 B_m - C/m^2) - B_m, all exact
    return F(685, 100) * E4 * (1 - 17 * B(m) - C / F(m*m)) - B(m)
for name, C in [("grid", CRPT4_GRID + C_KER4), ("closed", CRPT4_CLOSED + C_KER4)]:
    br = bracket(401, C)
    scan_ok = all(bracket(m, C) > 0 for m in range(401, 2001))
    print("  %-6s bracket(401) = %.6f > 0: %s ; exact scan 401..2000 all > 0: %s"
          % (name, float(br), br > 0, scan_ok))
print("  (limit 6.85*E(4) = %.6f > 0; B_m, C/m^2 decreasing => positive for all m >= 401)"
      % float(F(685, 100) * E4))

print("== (E) independent exact harness rebuild, 4 <= m <= 60 ==")
poly = [1]
fails = 0
prev_varfit = None
mono_from6 = True
for m in range(2, 61):
    new = [0] * (len(poly) + m - 1)   # multiply by (1 + q + ... + q^{m-1})
    run = 0
    for i in range(len(new)):
        if i < len(poly): run += poly[i]
        if i - m >= 0:    run -= poly[i - m]
        new[i] = run
    poly = new
    if m < 4: continue
    N = m * (m - 1) // 2
    assert len(poly) == N + 1 and poly == poly[::-1] and min(poly) > 0  # C1
    best_k, bn, bd = None, None, None   # min r(k) by integer cross-multiplication
    for k in range(1, N):
        num, den = poly[k] * poly[k], poly[k-1] * poly[k+1]
        if best_k is None or num * bd < bn * den:
            best_k, bn, bd = k, num, den
    varfit = lam(m) * (F(bn, bd) - 1)
    ok_arg = (best_k == 2) if m == 4 else (best_k == N // 2)          # C2
    kc = N // 2
    ok_min = (m == 4) or (bn * (poly[kc-1] * poly[kc+1]) ==
                          poly[kc] * poly[kc] * bd)                    # C3
    # C5 scope is 5 <= m (run_m200.py exempts m=4 by design; varfit(4) = 91/108
    # < 187/216 — harness REPORT §3's "4 <= m" display is loose, erratum recorded):
    if m == 4:
        print("  [C5 scope check] varfit(4) = %s = %.6f < 187/216: %s (the m=4 record row)"
              % (varfit, float(varfit), varfit < TARGET))
    ok_c5 = (m == 4) or (varfit >= TARGET and ((varfit == TARGET) == (m == 6)))  # C5
    if m >= 7 and prev_varfit is not None and varfit <= prev_varfit:
        mono_from6 = False                                             # C6
    if m >= 6: prev_varfit = varfit
    if not (ok_arg and ok_min and ok_c5): fails += 1
    if m in (4, 6, 40, 60):
        print("  m=%2d argmin=%4d (expect %s)  varfit=%.6f%s"
              % (m, best_k, "2 [exception]" if m == 4 else str(N // 2), float(varfit),
                 "  [= 187/216 exactly: %s]" % (varfit == TARGET) if m == 6 else ""))
print("  C1-C3/C5 failures on 4..60: %d ; C6 varfit strictly increasing 6..60: %s"
      % (fails, mono_from6))

print("== (F) B_m*m -> 27/25 = 1.08 ; H(4, 367) recompute ==")
for m in (30, 401, 1581, 100000):
    print("  m = %6d  B_m*m = %.6f" % (m, float(B(m) * m)))
H4 = B(367) * (1 + 1 * 16) + CR4_CLOSED / F(367 * 367)   # c_w(4) = 1
print("  H(4, 367) = B_367*(1 + c_w(4)*16) + C_R(4)closed/367^2 = %.4f <= 0.5: %s"
      % (float(H4), H4 <= F(1, 2)))
print("DONE")
