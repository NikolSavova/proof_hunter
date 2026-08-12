#!/usr/bin/env python3
"""w2r_rep1: wave-3 repair session — certified E(w0) decimals (wp3-a2 repairs
maths-R2 = numerics-F1, and numerics-F2), with the full propagated chain.

Replaces the float 50000-term partial sums of wp3a2_nc3_handoff.py (whose
%.8f NEAREST rounding printed E(1), E(2), E(3), E(6) one ulp HIGH) by fully
EXACT INTEGER arithmetic:

  E(u) = sum_{n>=1} 2 (3 v_n^2 + u^2) / (v_n^2 (v_n^2 + u^2)^2),  v_n = 2 pi n.

pi is bracketed by the rationals
  PI_LO = 314159265358979323846 / 10^20 < pi < 314159265358979323847 / 10^20 = PI_HI
(Archimedes-style certified digits; 3.14159265358979323846 26... is pi).
With v_n^2 = 4 n^2 p^2 / q^2 (p integer numerator of the pi bound, q = 10^20),
each term equals num/den with
  num = 2 (12 n^2 p^2 + u^2 q^2) q^4 ,   den = 4 n^2 p^2 (4 n^2 p^2 + u^2 q^2)^2
— pure integers.  Per term we take
  floor lower bound  = min over p in {p_lo, p_hi} of  num * 10^30 // den
  ceil  upper bound  = max over p in {p_lo, p_hi} of (num * 10^30 // den) + 1
(min/max over BOTH pi endpoints, so no monotonicity-in-v^2 claim is needed).
Summing N = 50000 terms gives certified integers S_lo <= 10^30 * partial_sum
<= S_hi.  Rigorous tail bound (all terms positive; u <= 8 < v_n for n > N):
  term_n <= 2*(4 v_n^2)/(v_n^2 * v_n^4) = 8 / (2 pi n)^4   (since u^2 <= v_n^2)
  tail   <= (1/(2 PI_LO^4)) * sum_{n>N} n^-4 <= (1/(2 PI_LO^4)) * 1/(3 N^3)
(integral comparison, exact Fraction).  Hence, as exact rationals,
  S_lo/10^30  <=  E(u)  <=  S_hi/10^30 + TAIL.

Checks performed (all exact-rational comparisons):
 (1) The corrected certified lower decimals of repair R2/F1:
     E(1) >= 0.00400692, E(2) >= 0.00358718, E(3) >= 0.00304035,
     E(4) >= 0.00248992, E(5) >= 0.00200652, E(6) >= 0.00161240
     (E(4), E(5) as originally printed; the other four one ulp lower), and
     that the ORIGINAL prints for 1, 2, 3, 6 are indeed NOT lower bounds.
 (2) F2 restatement: the rigorous truncation (tail) bound is < 2e-15
     (indeed < 2e-17 here; the original "< 2e-21" was false, and the float
     script's summation error ~6e-16 dominated — this script has none).
 (3) Propagated P.7 floors (truncate-DOWN displays):
     deficit(2) >= 0.0982, rho(2) <= 0.9018,
     deficit(4) >= 0.27289, rho(4) <= 0.72711 (0.7271048 certified).
 (4) The Theorem S R2-row chain with the SAFE rho(4):
     eps* = 1 - 1.02*rho >= C*/min(m, s2) = 20/79.5, and the R2 value
     (1 - 20/79.5)/rho >= 1.0292 >= 1.02  (referee cross-check band
     1.02928..1.029462).
 (5) Derivation-note-2 first term: 6.85*E(4)_lo*(1 - 17 B_401 - C/401^2)
     >= 0.01627 with exact B_m = (S_4 - m)/(240 lambda^2), C = 10.71.

Named constants: SCALE = 10^30 (integer fixed point), N = 50000 terms,
COEF = 6.85 = 137/20 (P.7), CSTAR = 20, S2FLOOR = 79.5 = 159/2 (v(7/10)*401
floor as used in the draft), CC = 10.71 = 1071/100 (C_R^PT + C_ker-anchor +
Lin as in derivation note 2 / referee F4).
"""
from fractions import Fraction as F

Q = 10 ** 20
P_LO = 314159265358979323846          # P_LO/Q < pi
P_HI = 314159265358979323847          # pi < P_HI/Q
SCALE = 10 ** 30
N = 50000
COEF = F(685, 100)                    # 6.85
CSHARP = F(187, 216)

def certified_E(u, n_terms=N):
    """Return (E_lo, E_hi) as exact Fractions bracketing E(u), u integer."""
    u2q2 = u * u * Q * Q
    s_lo = 0
    s_hi = 0
    for n in range(1, n_terms + 1):
        fl = []
        for p in (P_LO, P_HI):
            a = 4 * n * n * p * p                    # v_n^2 * q^2
            num = 2 * (3 * a + u2q2) * Q ** 4
            den = a * (a + u2q2) ** 2
            fl.append(num * SCALE // den)
        s_lo += min(fl)
        s_hi += max(fl) + 1
    tail_hi = F(Q ** 4, 2 * P_LO ** 4) * F(1, 3 * n_terms ** 3)
    return F(s_lo, SCALE), F(s_hi, SCALE) + tail_hi

def _dec(n, d):
    s = str(n).rjust(d + 1, "0")
    return s[:-d] + "." + s[-d:]

def trunc(x, d):
    """Truncate Fraction x DOWN to d decimals (string; certified <= x)."""
    return _dec((x * 10 ** d).__floor__(), d)

def ceil_dec(x, d):
    """Round Fraction x UP to d decimals (string; certified >= x)."""
    return _dec(-((-x * 10 ** d).__floor__()), d)

def S4(m):
    return m * (m + 1) * (2 * m + 1) * (3 * m * m + 3 * m - 1) // 30

def lam_var(m):
    return F(m * (m - 1) * (2 * m + 5), 72)

def B(m):
    return F(S4(m) - m, 240) / lam_var(m) ** 2

def main():
    ok = True
    # -- (1) certified decimals --------------------------------------------
    corrected = {1: F(400692, 10**8), 2: F(358718, 10**8), 3: F(304035, 10**8),
                 4: F(248992, 10**8), 5: F(200652, 10**8), 6: F(161240, 10**8)}
    original = {1: F(400693, 10**8), 2: F(358719, 10**8), 3: F(304036, 10**8),
                4: F(248992, 10**8), 5: F(200652, 10**8), 6: F(161241, 10**8)}
    Elo = {}
    Ehi = {}
    print("(1) certified E(u) brackets (exact integer arithmetic, N = 50000):")
    for u in range(1, 7):
        lo, hi = certified_E(u)
        Elo[u], Ehi[u] = lo, hi
        c_ok = lo >= corrected[u]
        if original[u] > hi:            # certified: original print > E(u)
            o_note = "original print %.8f NOT a lower bound (> E_hi)" \
                     % float(original[u])
        elif original[u] <= lo:
            o_note = "original print safe"
        else:
            o_note = "original print UNRESOLVED"
            ok = False
        if original[u] > corrected[u] and original[u] <= hi:
            ok = False                  # claimed-unsafe print not refuted
        print("  E(%d): %s <= E <= %s ; corrected print %.8f is lower bound:"
              " %s ; %s"
              % (u, trunc(lo, 12), ceil_dec(hi, 12), float(corrected[u]),
                 c_ok, o_note))
        ok &= c_ok
    # -- (2) truncation restatement ----------------------------------------
    tail = F(Q ** 4, 2 * P_LO ** 4) * F(1, 3 * N ** 3)
    print("(2) rigorous tail bound = %.3e  (< 2e-15 restated claim: %s;"
          " < 2e-17: %s; original '< 2e-21' FALSE: %s)"
          % (float(tail), tail < F(2, 10**15), tail < F(2, 10**17),
             tail > F(2, 10**21)))
    ok &= tail < F(2, 10**15)
    # -- (3) propagated floors ---------------------------------------------
    print("(3) propagated P.7 floors (deficit >= 6.85 w0^2 E_lo; rho <= 1-d):")
    dr = {}
    for w0 in (1, 2, 3, 4, 5, 6):
        d = COEF * w0 * w0 * Elo[w0]
        rho = 1 - d
        dr[w0] = (d, rho)
        print("  w0=%d: deficit >= %s   rho <= %s" % (w0, trunc(d, 7),
                                                      ceil_dec(rho, 7)))
    c1 = dr[2][0] >= F(982, 10**4)
    c2 = dr[2][1] <= F(9018, 10**4)
    c3 = dr[4][0] >= F(27289, 10**5)
    c4 = dr[4][1] <= F(72711, 10**5)
    print("  deficit(2) >= 0.0982: %s ; rho(2) <= 0.9018: %s ;"
          " deficit(4) >= 0.27289: %s ; rho(4) <= 0.72711: %s" %
          (c1, c2, c3, c4))
    ok &= c1 and c2 and c3 and c4
    # -- (4) R2-row chain with safe rho ------------------------------------
    rho4 = dr[4][1]
    eps_star = 1 - F(102, 100) * rho4
    budget = F(20) / F(159, 2)                     # 20/79.5
    val = (1 - budget) / rho4
    print("(4) R2 chain: eps* = 1 - 1.02 rho = %s >= 20/79.5 = %s : %s ;"
          % (trunc(eps_star, 6), ceil_dec(budget, 6), eps_star >= budget))
    print("    R2 value (1 - 20/79.5)/rho = %s >= 1.0292: %s ; >= 1.02: %s"
          % (trunc(val, 6), val >= F(10292, 10**4), val >= F(102, 100)))
    ok &= eps_star >= budget and val >= F(10292, 10**4)
    # -- (5) derivation-note-2 first term ----------------------------------
    CC = F(1071, 100)
    m = 401
    first = COEF * Elo[4] * (1 - 17 * B(m) - CC / m ** 2)
    brk = first - B(m)
    print("(5) note-2 at m=401: 6.85 E(4)_lo (1 - 17 B_m - C/m^2) = %s"
          " >= 0.01627: %s ; full bracket = %s > 0: %s"
          % (trunc(first, 6), first >= F(1627, 10**5), trunc(brk, 6),
             brk > 0))
    ok &= first >= F(1627, 10**5) and brk > 0
    print("VERDICT:", "PASS" if ok else "FAIL")

if __name__ == "__main__":
    main()
