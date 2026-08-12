#!/usr/bin/env python3
"""ref_indep_checks.py — INDEPENDENT re-derivation for the numerics referee pass on
theoremA_assembly_20260811.md (wave 3, 2026-08-12).

Deliberately different code paths from assembly_checks.py:
  - B_m built from a RAW exact power sum (loop over j, no closed S_4 formula), then
    cross-checked against the closed form the assembly script uses;
  - Mahonian polynomials built via PREFIX-SUM window recurrence (not the in-place
    running-sum convolution of assembly_checks.py block E);
  - crossover scans start at m = 5 (re-deriving the m* = 22 vs "30" note);
  - e^0.89 lower bound recoded with 25 terms;
  - extra checks the assembly did not run: all three H(K, M(K)); the
    (27/25)-form remainder bound (1.08 - B_m m) m in (0, 0.55]; bracket spot
    values at m = 3000/5000; band-2 actual budget 20/527.
All verdict-bearing arithmetic is exact Fraction/integer.
"""
from fractions import Fraction as F

# ---------- exact frame ----------
def S4_raw(m):      # RAW power sum (independent of the closed formula)
    return sum(F(j)**4 for j in range(1, m + 1))
def S4_closed(m):
    return F(m*(m+1)*(2*m+1)*(3*m*m+3*m-1), 30)
def lam(m):  return F(m*(m-1)*(2*m+5), 72)
_Bcache = {}
def B(m):
    if m not in _Bcache:
        _Bcache[m] = (S4_closed(m) - m) / (240 * lam(m)**2)
    return _Bcache[m]

print("== R0. closed-form S_4 cross-check (raw exact sum vs closed formula) ==")
ok = all(S4_raw(m) == S4_closed(m) for m in (4, 30, 180, 367, 401, 1581))
print("  S4 raw == closed at m in {4,30,180,367,401,1581}: %s" % ok)
print("  B_401 exact = %s = %.10f" % (B(401), float(B(401))))

# ---------- constants (independently transcribed from the SOURCE files) ----------
C_KER4   = F(378100442, 10000)      # wp2_a2 NC-A5 table, K=4 row, m=367
CA_GRID  = F(532, 100) + C_KER4     # C_R^PT grid 5.32 (repairs B3) + C_ker
CA_CLOSED= F(1878, 10) + C_KER4     # C_R^PT closed 187.8 + C_ker
TARGET   = F(187, 216)
E4       = F(248992, 100000000)     # wp3_a2 certified lower decimal (referee-safe)
RHO4     = F(72711, 100000)         # repaired rho(4)
CR_CLOSED = {1: F(411647, 10000), 2: F(2300864, 10000), 4: F(379974722, 10000)}
                                     # wp2_a2 NC-A5 exact assembled C_R closed
M_OF_K    = {1: 180, 2: 181, 4: 367}
CW        = {1: F(407, 1000), 2: F(466, 1000), 4: F(1)}   # repaired c_w

def r3(m, C): return 1 - B(m) - C / F(m*m)

print("== R1. the plug, independently ==")
print("  M(4) = 367 <= 401: %s" % (M_OF_K[4] <= 401))
for tag, C in (("grid", CA_GRID), ("closed", CA_CLOSED)):
    v = r3(401, C)
    print("  %-6s C_A = %.4f ; r3(401) = %s ~ %.6f ; >0: %s"
          % (tag, float(C), str(v)[:24] + "...", float(v), v > 0))
# strict monotone INCREASE of the r3 bound itself (stronger than A3's two-piece argument):
inc = all(r3(m + 1, CA_GRID) > r3(m, CA_GRID) for m in range(401, 3001))
print("  r3 bound strictly increasing on [401, 3001] (exact, grid C_A): %s" % inc)

print("== R2. crossovers m* (scan from m = 5, independent) ==")
for tag, C in (("K=4 grid", CA_GRID), ("K=4 closed", CA_CLOSED),
               ("K=1 center", F(4117, 100) + F(2308, 10000))):
    mstar = next(m for m in range(5, 10000) if r3(m, C) >= TARGET)
    below_prev = r3(mstar - 1, C) < TARGET
    stays = all(r3(m, C) >= TARGET for m in range(mstar, mstar + 500))
    print("  %-11s m* = %d (prev below: %s; stays 500 beyond: %s)" % (tag, mstar, below_prev, stays))

print("== R3. R2-region budget arithmetic, independently ==")
v07  = F(7, 10) * (1 + F(7, 10)) / 6
print("  v(7/10) = %s (= 119/600: %s) ; v(7/10)*401 = %s = %.4f >= 79: %s"
      % (v07, v07 == F(119, 600), v07 * 401, float(v07 * 401), v07 * 401 >= 79))
print("  v(1)*1581 = %s >= 527: %s" % (F(1, 3) * 1581, F(1, 3) * 1581 >= 527))
eps = 1 - F(102, 100) * RHO4
print("  eps* = %s = %.7f (doc: 0.2583478 -> match: %s)" % (eps, float(eps), eps == F(1291739, 5000000)))
b1, b1x, b2 = F(20) / F(795, 10), F(20) / (v07 * 401), F(136, 527)
print("  band1 20/79.5 = %.6f <= eps*: %s ; exact-floor %.6f <= eps*: %s"
      % (float(b1), b1 <= eps, float(b1x), b1x <= eps))
print("  band2 cap 136/527 = %.7f <= eps*: %s ; margin = %.3e ; actual C*=20: 20/527 = %.4f"
      % (float(b2), b2 <= eps, float(eps - b2), float(F(20, 527))))
print("  137/527 = %.7f > eps*: %s  (so 136 is the max integer C* on band 2)"
      % (float(F(137, 527)), F(137, 527) > eps))
concl = (1 - b1) / RHO4
print("  R2 conclusion (1 - 20/79.5)/rho = %.6f >= 1.02: %s" % (float(concl), concl >= F(102, 100)))
# e^0.89 lower bound, 25 exact terms (recoded):
t, s = F(1), F(1)
for n in range(1, 25):
    t *= F(89, 100) / n
    s += t
print("  e^0.89 > %.9f (25 terms) ; > 17/7: %s ; > 2: %s" % (float(s), s > F(17, 7), s > 2))

print("== R4. the w^2 bracket, independently (+ spot values beyond 2000) ==")
def br(m, C): return F(685, 100) * E4 * (1 - 17 * B(m) - C / F(m*m)) - B(m)
for tag, C in (("grid", CA_GRID), ("closed", CA_CLOSED)):
    v401 = br(401, C)
    scan = all(br(m, C) > 0 for m in range(401, 2001))
    print("  %-6s br(401) = %.6f > 0: %s ; scan 401..2000: %s ; br(3000) = %.6f ; br(5000) = %.6f"
          % (tag, float(v401), v401 > 0, scan, float(br(3000, C)), float(br(5000, C))))
inc = all(br(m + 1, CA_GRID) > br(m, CA_GRID) for m in range(401, 2001))
print("  bracket strictly increasing on the scan (grid): %s ; limit 6.85 E(4) = %.6f"
      % (inc, float(F(685, 100) * E4)))

print("== R5. H(K, M(K)) all three, independently ==")
for K in (1, 2, 4):
    M = M_OF_K[K]
    H = B(M) * (1 + CW[K] * K * K) + CR_CLOSED[K] / F(M * M)
    print("  K=%d: H(%d) = %.4f <= 1/2: %s" % (K, M, float(H), H <= F(1, 2)))

print("== R6. (27/25)-form remainder: (1.08 - B_m*m)*m in (0, 0.55] ==")
worst_lo, worst_hi = None, None
ok = True
for m in list(range(30, 2001)) + [3000, 5000, 10000, 100000]:
    d = (F(27, 25) - B(m) * m) * m
    if not (0 < d <= F(55, 100)): ok = False
    worst_lo = d if worst_lo is None or d < worst_lo else worst_lo
    worst_hi = d if worst_hi is None or d > worst_hi else worst_hi
print("  scan m in [30, 2000] + {3e3, 5e3, 1e4, 1e5}: all in (0, 0.55]: %s (range %.4f .. %.4f)"
      % (ok, float(worst_lo), float(worst_hi)))
print("  (=> B_m*m < 1.08 on the scan, g1_b B.0(ii) direction confirmed;")
print("      C_A also bounds the 1 - (27/25)/m form two-sidedly since 0.55 + 1.8 << C_A)")

print("== R7. independent Mahonian rebuild (prefix-sum recurrence), 4 <= m <= 80 ==")
poly = [1, 1]          # I_2
fails = 0
prev = None
mono = True
vals = {}
for m in range(3, 81):
    pref = [0] * (len(poly) + 1)
    for i, c in enumerate(poly): pref[i + 1] = pref[i] + c
    n_new = len(poly) + m - 1
    poly = [pref[min(i + 1, len(poly))] - pref[max(0, i + 1 - m)] for i in range(n_new)]
    if m < 4: continue
    N = m * (m - 1) // 2
    assert len(poly) == N + 1 and poly == poly[::-1] and min(poly) > 0
    bk, bn, bd = None, None, None
    for k in range(1, N):
        nu, de = poly[k] * poly[k], poly[k - 1] * poly[k + 1]
        if bk is None or nu * bd < bn * de: bk, bn, bd = k, nu, de
    vf = lam(m) * (F(bn, bd) - 1)
    vals[m] = vf
    kc = N // 2
    okA = (bk == 2) if m == 4 else (bk == kc)
    okC = (m == 4) or (bn * poly[kc - 1] * poly[kc + 1] == poly[kc]**2 * bd)
    ok5 = (m == 4) or (vf >= TARGET and ((vf == TARGET) == (m == 6)))
    if m >= 7 and prev is not None and vf <= prev: mono = False
    if m >= 6: prev = vf
    if not (okA and okC and ok5): fails += 1
print("  failures (argmin/min=central/C5) on 4..80: %d ; strict increase 6..80: %s" % (fails, mono))
print("  varfit(4) = %s (= 91/108: %s) ; varfit(5) = %s (= 7/8: %s)"
      % (vals[4], vals[4] == F(91, 108), vals[5], vals[5] == F(7, 8)))
print("  varfit(6) == 187/216: %s ; varfit(40) = %.6f ; varfit(60) = %.6f ; varfit(80) = %.6f"
      % (vals[6] == TARGET, float(vals[40]), float(vals[60]), float(vals[80])))
print("DONE")
