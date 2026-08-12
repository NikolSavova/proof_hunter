"""Referee check R1 (wp2-a2 numerics): off-grid monotonicity of C_ker2(K, m).

The draft's Theorem D.5 constant flavor rests on C_ker2(K, m) <= C_ker2(K, M(K)),
certified by NC-A3(3) on a grid: unit step on [M(K), 1000], step 10 on
(1000, 3000], plus the single spot pair (3000, 10^4) in NC-A5(3).
Wave-1 precedent: a K=4 grid bound was exceeded just beyond the grid edge.

Checks here:
 (a) Faulhaber closed forms for S4, S5, S6 verified against wp2b_lib_fixed.S
     for m in {30, 181, 367, 1000} (exact Fraction equality), then used to
     speed the big-m scans (bit-identical floats confirmed at m = 3000).
 (b) UNIT-step scan of C_ker2 on [1000, 3000] for K in {1,2,4} (fills the
     draft's step-10 grid), verifying monotone decrease.
 (c) Step-20 scan on [3000, 10000] (fills the endpoint-only band).
 (d) Beyond the draft's last point: m in {10^4, 2e4, 5e4, 1e5, 2e5, 5e5, 1e6}
     -- verify C_ker2(K, m) < C_ker2(K, M(K)) (the actual theorem-level need)
     and print the trend (limit behaviour of the pure-alpha quartic rows).

Run: python3 ref_a2_monotone_offgrid.py
"""
import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_WP = os.path.normpath(os.path.join(_HERE, "..", "..", "g2_scripts",
                                    "campaign_20260811", "wp2_a2"))
sys.path.insert(0, _WP)
import wp2a2_lib as L        # noqa: E402
import wp2a2_lib2 as L2      # noqa: E402


def faulhaber(r, m):
    m = Fraction(m)
    if r == 4:
        return m*(m+1)*(2*m+1)*(3*m*m + 3*m - 1)/30
    if r == 5:
        return m*m*(m+1)*(m+1)*(2*m*m + 2*m - 1)/12
    if r == 6:
        return m*(m+1)*(2*m+1)*(3*m**4 + 6*m**3 - 3*m + 1)/42
    raise ValueError(r)


_cache = {}


def fast_exact_sums(m):
    if m not in _cache:
        _cache[m] = tuple(int(faulhaber(r, m)) for r in (4, 5, 6))
    return _cache[m]


def main():
    ok = True
    print("R1: off-grid monotonicity / large-m checks for C_ker2")

    # (a) verify Faulhaber vs the library's direct Fraction sums
    for m in (30, 181, 367, 1000):
        direct = L.exact_sums(m)
        fast = fast_exact_sums(m)
        same = direct == fast
        print("  (a) m=%4d  Faulhaber == direct sums: %s" % (m, same))
        ok &= same
    # patch in the fast version (bit-identical check at m = 3000, K = 4)
    ref = L2.delta_ker_bound2(4, 3000)["Cker"]
    L.exact_sums = fast_exact_sums
    ref2 = L2.delta_ker_bound2(4, 3000)["Cker"]
    print("  (a) K=4 m=3000 Cker with fast sums: %.10f vs %.10f  equal: %s"
          % (ref2, ref, ref2 == ref))
    ok &= ref2 == ref

    MK = {1: 180, 2: 181, 4: 367}
    CKER_M = {}
    for K, M in MK.items():
        CKER_M[K] = L2.delta_ker_bound2(K, M)["Cker"]

    # (b) unit-step 1000..3000
    print("  (b) unit-step monotone decrease on [1000, 3000]:")
    for K in (1, 2, 4):
        prev, mono, where = None, True, None
        for m in range(1000, 3001):
            c = L2.delta_ker_bound2(K, m)["Cker"]
            if prev is not None and c > prev + 1e-12:
                mono, where = False, m
                break
            prev = c
        print("      K=%d: %s%s" % (K, mono,
                                    "" if mono else " FAILS at m=%d" % where))
        ok &= mono

    # (c) step-20 3000..10000
    print("  (c) step-20 monotone decrease on [3000, 10000]:")
    for K in (1, 2, 4):
        prev, mono, where = None, True, None
        for m in range(3000, 10001, 20):
            c = L2.delta_ker_bound2(K, m)["Cker"]
            if prev is not None and c > prev + 1e-12:
                mono, where = False, m
                break
            prev = c
        print("      K=%d: %s%s" % (K, mono,
                                    "" if mono else " FAILS at m=%d" % where))
        ok &= mono

    # (d) beyond 10^4
    print("  (d) large m: C_ker2(K, m) vs headline C_ker2(K, M(K)):")
    for K in (1, 2, 4):
        head = CKER_M[K]
        prev = None
        for m in (10000, 20000, 50000, 100000, 200000, 500000, 1000000):
            c = L2.delta_ker_bound2(K, m)["Cker"]
            below = c < head
            trend = "" if prev is None else ("  (%s prev)" %
                                             ("<" if c < prev else ">="))
            print("      K=%d m=%7d  Cker2 = %12.4f  < %10.4f: %s%s"
                  % (K, m, c, head, below, trend))
            ok &= below
            prev = c

    print("R1 VERDICT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
