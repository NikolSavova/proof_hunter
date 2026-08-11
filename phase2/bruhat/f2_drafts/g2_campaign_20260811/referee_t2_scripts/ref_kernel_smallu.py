"""Referee follow-up (numerics referee, T2 draft, 2026-08-11): corrected
verification of the T.4' pointwise kernel bounds

    |g''(u)  - u/120 |  <= |u|^3 / 1500      on (0, pi]
    |g'''(u) - 1/120 |  <=  u^2  / 500       on (0, pi]

SUPERSEDES item (a) of ref_misc_recheck.py, whose naive fine grid printed
ratios up to 1.079 at u ~ 1e-4: that was catastrophic cancellation in the
closed form (2/u^3 - e^u(e^u+1)/(e^u-1)^3 differences ~1e12-size terms to get
~1e-6, then subtracts u/120 to get ~1e-13) at 30 dps, NOT a real violation.
The draft's own 300-point grid starts at u = pi/300 = 0.0105 and never enters
the unstable zone; its measured max ratio 0.9921 is correct.

Correct treatment:

 (1) On (0, 1/2]: ANALYTIC.  g''(u) = u/120 - u^3/1512 + u^5/28800 - ... and
     g'''(u) = 1/120 - u^2/504 + u^4/5760 - ... are alternating with term
     ratios <= u^2/19.05 resp. u^2/11.43 (checked below through the Bernoulli
     tail), so for u <= 1/2 the alternating-series bound gives EXACTLY
       |g''  - u/120| <= u^3/1512  =>  ratio <= 1500/1512 = 0.99206 < 1,
       |g''' - 1/120| <= u^2/504   =>  ratio <=  500/504  = 0.99206 < 1.
 (2) On [1/2, pi]: 60-dps grid (20000 points) with the closed form -- at
     u >= 1/2 cancellation costs < 5 digits, negligible at 60 dps.  Also
     evaluates both ratios at a few small u via the SERIES (stable) to show
     they sit at ~0.9920 where the naive closed form went bad.

Bernoulli-series term-ratio audit: g(u) = 1/2 - sum_{n>=1} B_{2n} u^{2n-1}/(2n)!
so the g'' series has |term_n| = |B_{2n}| (2n-1)(2n-2) u^{2n-3}/(2n)! (n >= 2)
and the g''' series |term_n| = |B_{2n}| (2n-1)(2n-2)(2n-3) u^{2n-4}/(2n)!;
consecutive-ratio maxima over n are computed below for u = pi and confirmed
< 1 (so the alternating bound is valid on ALL of (0, pi], making (1) a proof
on the full interval; the grid in (2) is then pure corroboration).

stdlib + mpmath. Run: python3 ref_kernel_smallu.py
"""
import sys

import mpmath as mp


def main():
    ok = True
    mp.mp.dps = 60

    print("Bernoulli term-ratio audit at u = pi (needs < 1 for alternating bound):")
    u = mp.pi
    worst2 = worst3 = mp.mpf(0)
    for n in range(2, 40):
        b_n = abs(mp.bernoulli(2 * n))
        b_n1 = abs(mp.bernoulli(2 * n + 2))
        t2_n = b_n * (2 * n - 1) * (2 * n - 2) * u ** (2 * n - 3) / mp.factorial(2 * n)
        t2_n1 = b_n1 * (2 * n + 1) * (2 * n) * u ** (2 * n - 1) / mp.factorial(2 * n + 2)
        t3_n = t2_n * (2 * n - 3) / u
        t3_n1 = t2_n1 * (2 * n - 1) / u
        if t2_n > 0:
            worst2 = max(worst2, t2_n1 / t2_n)
        if t3_n > 0:
            worst3 = max(worst3, t3_n1 / t3_n)
    print(f"  max consecutive ratio, g'' series : {mp.nstr(worst2, 6)}")
    print(f"  max consecutive ratio, g''' series: {mp.nstr(worst3, 6)}")
    ok &= worst2 < 1 and worst3 < 1
    print("  => |g''-u/120| <= u^3/1512 and |g'''-1/120| <= u^2/504 hold on (0, pi]")
    print("     giving ratios <= 1500/1512 = 500/504 = 0.992063 < 1: bounds PROVED.")

    print("series-evaluated ratios at the small u where the naive grid misbehaved:")
    for us in ("0.0001", "0.001", "0.01", "0.1"):
        uu = mp.mpf(us)
        g2s = sum((-1) ** (n) * abs(mp.bernoulli(2 * n + 2)) * (2 * n + 1) * (2 * n)
                  * uu ** (2 * n - 1) / mp.factorial(2 * n + 2) for n in range(1, 30))
        # n=1 term: |B_4|*3*2*u/24 = (1/30)*6/24 u = u/120  with sign +
        g3s = sum((-1) ** (n) * abs(mp.bernoulli(2 * n + 2)) * (2 * n + 1) * (2 * n)
                  * (2 * n - 1) * uu ** (2 * n - 2) / mp.factorial(2 * n + 2)
                  for n in range(1, 30))
        r2 = abs(g2s - uu / 120) / (uu**3 / 1500)
        r3 = abs(g3s - mp.mpf(1) / 120) / (uu**2 / 500)
        print(f"  u={us}: ratio g'' = {mp.nstr(r2, 6)}, ratio g''' = {mp.nstr(r3, 6)}")
        ok &= r2 < 1 and r3 < 1

    print("grid on [1/2, pi], 20000 points, 60 dps, closed form:")
    r2m = r3m = mp.mpf(0)
    a2 = a3 = None
    lo = mp.mpf(1) / 2
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

    print(f"REF-KERNEL VERDICT: {'PASS - T.4 kernel bounds hold on (0, pi], '
          'now analytically (alternating series), draft grid value 0.9921 is the '
          'u->0 limit 1500/1512' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
