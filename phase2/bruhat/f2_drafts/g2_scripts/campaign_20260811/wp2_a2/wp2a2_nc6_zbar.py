"""NC-A6: spot check of the zbar magnitude claim in Theorem D.5's proof
(zbar < 1e-6 at every (K, m) the theorem uses).
Run: python3 wp2a2_nc6_zbar.py"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import wp2a2_lib2 as L2


def main():
    worst = 0.0
    for K, M in ((1, 180), (2, 181), (4, 367)):
        for m in (M, 400, 1000, 3000):
            r = L2.delta_ker_bound2(K, m)
            worst = max(worst, r["zbar"])
            print("  K=%d m=%4d  zbar = %.3e" % (K, m, r["zbar"]))
    print("max zbar = %.3e  (< 1e-6: %s)" % (worst, worst < 1e-6))
    print("NC-A6 VERDICT:", "PASS" if worst < 1e-6 else "FAIL")
    return 0 if worst < 1e-6 else 1


if __name__ == "__main__":
    sys.exit(main())
