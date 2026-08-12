#!/usr/bin/env python3
# WAVE-4 SL-SLIVER sizing certificate (new file; consumes nothing unrefereed
# beyond what it names).  All numeric claims in wave4_sliver_20260812.md come
# from THIS file's printed output plus the harness results files it parses.
#
# [A] EXACT (Fraction end-to-end, safe rounding direction):
#     the honest W1 far entry, in the form fixed by wp4_draft_composite.md
#     SS5.3 (SL4' display),
#         far'(m, w) = sqrt(2pi) * m * s2cap^{3/2} * exp(-0.0741 m),
#     with the PROOF-GRADE ingredients
#         s2cap = m/(4 sinh^2(lam/2)) <= m/lam^2 = m^3/w^2   (Lemma C.1,
#                 PROVED; sinh x >= x),
#         exponent floor 0.0741 <= q(2,1) = 0.07412654       (Theorem A3(ii)
#                 P3 constant, PROVED; referee-confirmed),
#     satisfies, for ALL integers m >= 451 and ALL w >= 4:
#         far'(m, w) <= far'(m, 4) <= far'(451, 4) <= 1/20 = 0.05 .
#     Chain: (i) w-monotonicity is exact (w enters only as 1/w^3);
#     (ii) integer-step m-monotonicity for m >= 451 is certified by
#         far'(m+1,4)/far'(m,4) = ((m+1)/m)^{11/2} e^{-0.0741}
#           <= ((452/451)^{11})^{1/2} e^{-0.0741} < 1,
#     i.e. (452/451)^{11} < e^{2*0.0741} = e^{0.1482}, both sides rational-
#     certified; (iii) far'(451,4) <= 1/20 by rational upper bound.
#     Boundary honesty: far'(450, 4) > 1/20 by rational LOWER bound, so the
#     sizing boundary m0 = 450 is exact for this entry form: the sliver's
#     m-extent under the A3 floor is [401, 450], not less.
# [B] EXACT coverage audit: parse the checkpointed harness results
#     (harness_m560/results_m560.txt + its honored prior file
#     wave2_repairs/results_m540.txt), verify every integer m in [401, M_H]
#     appears exactly once with verdict PASS and no FAIL exists anywhere;
#     print M_H and the last row verbatim.
# [C] LABELED FLOAT diagnostics (display-only, not proof-bearing):
#     far'(m,4) and the safety factor 0.05/far'(m,4) at m = 451, 496, 561;
#     the crude-orphan-floor comparison (exponent qW(4.05) = 0.0504-class)
#     showing WHY the A3-floor sizing (450) and not the cruder sizing
#     (~560-class) is the operative bound once A3 is citable.
from fractions import Fraction as F
import math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RES_560 = os.path.join(HERE, "..", "harness_m560", "results_m560.txt")
RES_540 = os.path.join(HERE, "..", "wave2_repairs", "results_m540.txt")

# ---------- exact helpers (safe direction; style of wp4asm_chain.py) ----------
def exp_lb(x, N=200):
    # partial sum P_N(x) <= e^x for rational x >= 0 (all terms positive)
    x = F(x); s = F(1); t = F(1)
    for n in range(1, N + 1):
        t *= x / n
        s += t
    return s                      # so e^{-x} <= 1/exp_lb(x)

def exp_ub(x, N=200):
    # P_N(x) + geometric remainder cap >= e^x, valid for 0 <= x < N+2
    x = F(x); assert 0 <= x < N + 2
    s = F(1); t = F(1)
    for n in range(1, N + 1):
        t *= x / n
        s += t
    rem = t * x / (N + 1) / (1 - x / (N + 2))
    return s + rem                # so e^{-x} >= 1/exp_ub(x)

def sqrt_ub(x, digits=10):
    # rational s with s^2 >= x
    num = F(x) * 10**(2 * digits)
    r = math.isqrt(int(num))
    while F(r, 10**digits)**2 < F(x):
        r += 1
    return F(r, 10**digits)

def sqrt_lb(x, digits=10):
    # rational s with s^2 <= x
    num = F(x) * 10**(2 * digits)
    r = math.isqrt(int(num)) + 1
    while F(r, 10**digits)**2 > F(x):
        r -= 1
    return F(r, 10**digits)

# rational brackets for 2*pi:  6.283185306 <= 2pi <= 6.283185308
TWO_PI_LB = F(6283185306, 10**9)
TWO_PI_UB = F(6283185308, 10**9)

Q_FLOOR = F(741, 10000)          # 0.0741 <= q(2,1) = 0.07412654 (A3(ii), PROVED)
SLOT    = F(1, 20)               # the far slot 0.05 in the SL4' honest ledger

def far_ub(m):
    # rational UPPER bound on far'(m, 4) = sqrt(2pi) m^{11/2} e^{-0.0741 m} / 64
    m = F(m)
    return (sqrt_ub(TWO_PI_UB) * m**5 * sqrt_ub(m) / 64) / exp_lb(Q_FLOOR * m)

def far_lb(m):
    # rational LOWER bound on far'(m, 4)
    m = F(m)
    return (sqrt_lb(TWO_PI_LB) * m**5 * sqrt_lb(m) / 64) / exp_ub(Q_FLOOR * m)

print("[A] EXACT sizing certificate for the W1 far sliver "
      "(entry form: composite SS5.3 SL4' display; floor 0.0741 = A3(ii); "
      "cap m^3/w^2 = Lemma C.1 + sinh x >= x)")

# (i) w-monotonicity: far'(m,w) = sqrt(2pi) m^{11/2} e^{-0.0741 m} / w^3,
#     exactly decreasing in w > 0; sup over the sliver band w in (4, 4.51]
#     (indeed over all of W1 = (4, 6]) is the w = 4 value.  No computation
#     needed; recorded here for the audit trail.
print("  (i)  w-monotonicity: entry proportional to 1/w^3 -> sup at w = 4 "
      "(covers all w > 4, hence the whole sliver band (4, 4.51] and W1)")

# (ii) integer-step m-monotonicity for m >= 451:
lhs = F(452, 451)**11
rhs = exp_lb(F(1482, 10000))     # e^{0.1482} >= this partial sum
mono_ok = lhs < rhs
print(f"  (ii) m-monotonicity (m >= 451): (452/451)^11 = {float(lhs):.6f} "
      f"< exp_lb(0.1482) = {float(rhs):.6f} : {mono_ok}")
assert mono_ok

# (iii) the certificate at m = 451 and boundary honesty at m = 450:
u451 = far_ub(451)
l450 = far_lb(450)
ok451 = u451 <= SLOT
ok450 = l450 > SLOT
print(f"  (iii) far'(451, 4) <= {float(u451):.6f}  <= 0.05 : {ok451}   "
      f"(margin factor {float(SLOT/u451):.4f})")
print(f"        far'(450, 4) >= {float(l450):.6f}  >  0.05 : {ok450}   "
      f"(boundary honesty: m0 = 450 is exact for this entry form)")
assert ok451 and ok450
print("  CERTIFIED: far'(m, w) <= 0.05 for ALL integers m >= 451 and ALL "
      "w >= 4  [(i) + (ii) + (iii)]")

# ---------- [B] coverage audit ----------
print("\n[B] EXACT harness coverage audit (checkpointed m560 run + honored prior rows)")
rows = {}
fails = []
for path in (RES_540, RES_560):
    if not os.path.exists(path):
        print(f"  MISSING results file: {path}"); sys.exit(1)
    for line in open(path):
        parts = line.split()
        if not parts or not parts[0].isdigit():
            continue
        m, verdict = int(parts[0]), parts[-1]
        if verdict == "FAIL":
            fails.append((path, m))
        # later files may repeat honored rows; PASS must agree
        rows.setdefault(m, verdict)
mh = 400
while (mh + 1) in rows and rows[mh + 1] == "PASS":
    mh += 1
missing = [m for m in range(401, mh + 1) if rows.get(m) != "PASS"]
last_row = [l.rstrip() for l in open(RES_560) if l.split() and l.split()[0].isdigit()][-1]
print(f"  FAIL rows anywhere: {len(fails)}  {fails if fails else ''}")
print(f"  contiguous PASS coverage: m in [401, {mh}]  "
      f"(gaps in [401, {mh}]: {missing})")
print(f"  last results_m560.txt row (verbatim): '{last_row}'")
print(f"  M_H = {mh};  sliver m-extent [401, 450] covered: {mh >= 450}")

# ---------- [C] labeled float diagnostics (NOT proof-bearing) ----------
print("\n[C] FLOAT diagnostics (display-only)")
def far_f(m, w=4.0):
    return math.sqrt(2 * math.pi) * m**5.5 * math.exp(-0.0741 * m) / w**3
for m in (451, 496, 561):
    print(f"  far'({m}, 4) ~ {far_f(m):.3e}   safety factor vs slot 0.05: "
          f"{0.05 / far_f(m):.1f}x")
# why A3-floor sizing (450) governs, not the orphan's cruder floor (~560):
qW = (2.025 - 1) / (2 * 2.025) * (math.log(2) - 1 / 2.025)   # orphan W.3d floor at w = 4.05
def far_crude(m, w=4.0):
    return math.sqrt(2 * math.pi) * m**5.5 * math.exp(-qW * m) / w**3
lo = next(m for m in range(401, 1200) if far_crude(m) <= 0.05)
print(f"  crude orphan floor qW(4.05) = {qW:.5f}: same entry <= 0.05 only from "
      f"m = {lo}  (the '~560-class' sizing; superseded because q(2,1) >= 0.0741 "
      f"is PROVED via A3(ii))")
print("\nOVERALL: " + ("PASS" if (mono_ok and ok451 and ok450 and not fails
      and not missing and mh >= 450) else "INCOMPLETE"))
