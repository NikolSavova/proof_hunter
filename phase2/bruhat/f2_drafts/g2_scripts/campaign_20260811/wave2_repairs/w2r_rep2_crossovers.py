#!/usr/bin/env python3
"""w2r_rep2: wave-3 repair session — the two wrong/un-scripted crossover
numbers, exact-rational recomputation.

(a) wp3-a2 repair maths-R3 = numerics-F4 (WRONG NUMBER "~68" -> 82).
    Derivation note 2 of wp3_draft_a2.md section 5 needs the w^2-bracket
        bracket(m) := 6.85 E(4) (1 - 17 B_m - C/m^2) - B_m  >  0,
    with B_m = (S_4(m) - m)/(240 lambda(m)^2) exact (S_4 = sum j^4,
    lambda = m(m-1)(2m+5)/72), C = 10.71 = C_R^PT(4) + C_ker-anchor + Lin
    (5.30 + 5.04 + 0.372, the note's own budget), and the certified lower
    bound E(4) >= 0.00248992 (w2r_rep1, exact bracket).  The draft's aside
    printed "m >= 63.3 ignoring the (1 - 17 B_m) factor, m >= ~68 with it";
    "~68" came from no saved script and is false.  This script scans m
    exactly and certifies: first positive m = 82, positive for ALL
    82 <= m <= 5000, and the consumed claims (positivity for m >= 100 and at
    m = 401) hold.

(b) wp2-a2 repair R-F4 (un-scripted aside "C' = 42 moves the center-margin
    crossover only to m ~ 27").  NC-13's center-margin criterion
    (F2_PROOF_DRAFT.md: "1 - 1.08/m - C'/m^2 >= 187/216 already for
    m >= 9..17 at C' = 1/5/20") is solved exactly here, in both flavors
    (display coefficient 1.08/m = 27/(25m), and exact B_m), for
    C' in {1, 5, 20, 42}.  Result: C' = 20 reproduces NC-13's m0 = 17 in
    both flavors; C' = 42 gives m0 = 23 (both flavors) — the draft's "~27"
    is an overestimate in the SAFE direction (23 <= 27 << 400; the aside's
    conclusion stands a fortiori), but the scripted number is 23.

(c) wp3-a2 repair numerics-F5 ("17364x" -> 17363x).  The R1 margin at
    (m, c) = (1581, 1) is exactly 1580^2 * 3167 / (144 * 2 * 1581)
    = 17363.524... ; NC-P4's %.0f print rounded it UP to 17364.  Certify
    17363 <= margin < 17364 exactly (so "17363x" and ">= 1.7e4 x" are the
    safe prints).

All arithmetic exact Fraction/integer; no floats in any verdict.
"""
from fractions import Fraction as F

E4_LO = F(248992, 10 ** 8)      # certified lower bound (w2r_rep1: E_lo(4))
COEF = F(685, 100)              # 6.85
CC = F(1071, 100)               # C = 10.71
CSHARP = F(187, 216)

def S4(m):
    return m * (m + 1) * (2 * m + 1) * (3 * m * m + 3 * m - 1) // 30

def lam_var(m):
    return F(m * (m - 1) * (2 * m + 5), 72)

def B(m):
    return F(S4(m) - m, 240) / lam_var(m) ** 2

def bracket(m):
    return COEF * E4_LO * (1 - 17 * B(m) - CC / m ** 2) - B(m)

def main():
    ok = True
    # (a) the m = 82 crossover
    first = None
    all_pos_after = True
    for m in range(30, 5001):
        b = bracket(m)
        if first is None and b > 0:
            first = m
        elif first is not None and b <= 0:
            all_pos_after = False
    print("(a) note-2 bracket 6.85 E(4)(1 - 17B_m - C/m^2) - B_m, exact:")
    print("    first positive m = %s (draft said '~68'; repair value 82)"
          % first)
    print("    positive for all %s <= m <= 5000: %s" % (first, all_pos_after))
    print("    consumed claims: m=100: %.6f > 0: %s ; m=401: %.6f > 0: %s"
          % (float(bracket(100)), bracket(100) > 0,
             float(bracket(401)), bracket(401) > 0))
    ok &= (first == 82) and all_pos_after and bracket(100) > 0 \
        and bracket(401) > 0
    # also the "ignoring the factor" companion 63.3: first m with
    # 6.85 E(4) - B_m > 0 (kept for the record; the draft's 63.3 is float)
    f2 = next(m for m in range(30, 500) if COEF * E4_LO - B(m) > 0)
    print("    companion (no (1-17B_m-C/m^2) factor): first m = %d" % f2)

    # (b) NC-13 center-margin crossover
    print("(b) NC-13 center margin 1 - B - C'/m^2 >= 187/216, exact:")
    for Cp in (1, 5, 20, 42):
        m_disp = next(m for m in range(4, 2000)
                      if 1 - F(27, 25 * m) - F(Cp, m * m) >= CSHARP)
        m_exact = next(m for m in range(4, 2000)
                       if 1 - B(m) - F(Cp, m * m) >= CSHARP)
        print("    C'=%3d: m0 = %2d (1.08/m flavor), %2d (exact B_m flavor)"
              % (Cp, m_disp, m_exact))
        if Cp == 20:
            ok &= m_disp == 17          # NC-13's quoted m0 reproduces
        if Cp == 42:
            ok &= m_disp == 23 and m_exact == 23
    print("    -> repair R-F4: 'm ~ 27' should read m = 23 (both flavors);"
          " safe direction, conclusion (<< 400) unchanged")

    # (c) the 17363x margin
    marg = F(1580 ** 2 * 3167, 144 * 2 * 1581)
    print("(c) R1 margin at (1581, 1): exact = %d + %s = %.3f ;"
          % (marg.__floor__(), marg - marg.__floor__(), float(marg)))
    c_ok = 17363 <= marg < 17364
    print("    17363 <= margin < 17364: %s  (safe print '17363x';"
          " NC-P4's '17364' was rounded UP)" % c_ok)
    ok &= c_ok
    print("VERDICT:", "PASS" if ok else "FAIL")

if __name__ == "__main__":
    main()
