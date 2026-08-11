"""Referee follow-up v2 (numerics referee, T2 draft, 2026-08-11): corrected
verification of the T.4' pointwise kernel bounds

    |g''(u)  - u/120 |  <= |u|^3 / 1500      on (0, pi]
    |g'''(u) - 1/120 |  <=  u^2  / 500       on (0, pi]

SUPERSEDES ref_kernel_smallu.py (v1), which had two implementation bugs of its
own: (i) its series spot-evaluation used the wrong overall sign (first term
-u/120 instead of +u/120), making the printed small-u "ratios" meaningless;
(ii) its Bernoulli term-ratio audit for g''' compared the TAIL's first term
u^2/504 against the CONSTANT term 1/120 (ratio 120 u^2/504 = 2.35 at u = pi,
irrelevant): the alternating-series remainder bound only needs the ratios
WITHIN the tail (from the u^2/504 term onward).  v1's [1/2, pi] grid block was
correct and is reproduced here.  (And ref_misc_recheck.py item (a)'s naive
closed-form grid was numerically invalid below u ~ 0.01: catastrophic
cancellation, not a real violation.)

Correct argument, fully checked here:

  g''(u)  =  u/120 - u^3/1512 + u^5/28800 - u^7/665280 + ...   (tail T2 from u^3 on)
  g'''(u) =  1/120 - u^2/504  + u^4/5760  - u^6/95040  + ...   (tail T3 from u^2 on)
  (coefficients (-1)^n |B_{2n}| (2n-1)(2n-2) / (2n)! and
                (-1)^n |B_{2n}| (2n-1)(2n-2)(2n-3) / (2n)!, n >= 2)

  (1) TAIL term-ratio audit at u = pi (worst case; ratios scale as u^2):
      all consecutive ratios within T2 (from n=3 on) and within T3 (from n=3
      on) are < 1, so each tail is alternating with strictly decreasing terms
      on (0, pi], and the alternating remainder bound gives EXACTLY
        |g''(u)  - u/120| <= u^3/1512   =>  ratio vs u^3/1500 <= 1500/1512 = 0.99206,
        |g'''(u) - 1/120| <= u^2/504    =>  ratio vs u^2/500  <=  500/504  = 0.99206.
      This proves both T.4' kernel bounds on ALL of (0, pi] analytically.
  (2) Corroborating grids: series-evaluated ratios (stable) at small u, and a
      60-dps closed-form grid on [0.1, pi] (cancellation <= ~7 digits there).

stdlib + mpmath. Run: python3 ref_kernel_smallu2.py
"""
import sys

import mpmath as mp


def coeffs(nmax):
    """(c2_n, c3_n) with g'' = sum_n (-1)^n c2_n u^{2n-3},
    g''' = sum_n (-1)^n c3_n u^{2n-4}, n = 2..nmax; c_n > 0."""
    out = []
    for n in range(2, nmax + 1):
        b = abs(mp.bernoulli(2 * n))
        c2 = b * (2 * n - 1) * (2 * n - 2) / mp.factorial(2 * n)
        c3 = c2 * (2 * n - 3)
        out.append((n, c2, c3))
    return out


def main():
    ok = True
    mp.mp.dps = 60
    cs = coeffs(45)

    print("first terms sanity: c2_2 = 1/120, c2_3 = 1/1512, c2_4 = 1/28800;"
          " c3_2 = 1/120, c3_3 = 3/1512 = 1/504, c3_4 = 5/28800 = 1/5760")
    for n, c2, c3 in cs[:3]:
        print(f"  n={n}: c2 = 1/{mp.nstr(1/c2, 8)}   c3 = 1/{mp.nstr(1/c3, 8)}")

    print("(1) TAIL consecutive-term ratios at u = pi (need < 1):")
    u = mp.pi
    worst2 = worst3 = mp.mpf(0)
    for i in range(1, len(cs) - 1):        # from n=3 on: tail terms only
        n, c2, c3 = cs[i]
        n1, c2n, c3n = cs[i + 1]
        r2 = (c2n * u ** (2 * n1 - 3)) / (c2 * u ** (2 * n - 3))
        r3 = (c3n * u ** (2 * n1 - 4)) / (c3 * u ** (2 * n - 4))
        worst2 = max(worst2, r2)
        worst3 = max(worst3, r3)
    print(f"  max ratio within g'' tail  = {mp.nstr(worst2, 6)}")
    print(f"  max ratio within g''' tail = {mp.nstr(worst3, 6)}")
    ok &= worst2 < 1 and worst3 < 1
    print("  => alternating remainder bounds |g''-u/120| <= u^3/1512,"
          " |g'''-1/120| <= u^2/504 hold on (0, pi]:")
    print(f"     T.4' ratios <= 1500/1512 = {mp.nstr(mp.mpf(1500)/1512, 6)} < 1"
          "  -- both kernel bounds PROVED analytically.")

    print("(2a) series-evaluated ratios at small u (stable; correct signs):")
    for us in ("0.0001", "0.01", "0.1", "0.3"):
        uu = mp.mpf(us)
        g2s = sum((-1) ** n * c2 * uu ** (2 * n - 3) for n, c2, _ in cs)
        g3s = sum((-1) ** n * c3 * uu ** (2 * n - 4) for n, _, c3 in cs)
        r2 = abs(g2s - uu / 120) / (uu**3 / 1500)
        r3 = abs(g3s - mp.mpf(1) / 120) / (uu**2 / 500)
        print(f"  u={us}: ratio g'' = {mp.nstr(r2, 6)}, ratio g''' = {mp.nstr(r3, 6)}")
        ok &= r2 < 1 and r3 < 1

    print("(2b) closed-form grid on [0.1, pi], 20000 points, 60 dps:")
    r2m = r3m = mp.mpf(0)
    a2 = a3 = None
    lo = mp.mpf("0.1")
    for i in range(20001):
        uu = lo + (mp.pi - lo) * i / 20000
        e = mp.e**uu
        g2v = 2 / uu**3 - e * (e + 1) / (e - 1) ** 3
        g3v = -6 / uu**4 + e * (e * e + 4 * e + 1) / (e - 1) ** 4
        q2 = abs(g2v - uu / 120) / (uu**3 / 1500)
        q3 = abs(g3v - mp.mpf(1) / 120) / (uu * uu / 500)
        if q2 > r2m:
            r2m, a2 = q2, uu
        if q3 > r3m:
            r3m, a3 = q3, uu
    print(f"  max ratio g'': {mp.nstr(r2m, 8)} at u = {mp.nstr(a2, 6)}")
    print(f"  max ratio g''': {mp.nstr(r3m, 8)} at u = {mp.nstr(a3, 6)}")
    ok &= r2m < 1 and r3m < 1

    print(f"REF-KERNEL-V2 VERDICT: "
          f"{'PASS - T.4 kernel bounds hold on (0, pi], now analytically; the '
             'draft grid max 0.9921 is the u->0 limit 1500/1512' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
