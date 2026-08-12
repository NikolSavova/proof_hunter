#!/usr/bin/env python3
# REFEREE (numerics, wave4_sliver): INDEPENDENT exact Mahonian spot-audit of
# the m560 harness rows consumed by Fact SLV.2.  Freshly written convolution
# (not imported from any campaign script).  Exact integers/Fractions only in
# every verdict.
#   * spot rows compared BYTE-WISE against the results files:
#       honored (m540): 401, 450   |   fresh (m560): 482, 536, 554, 560
#   * full exact argmin/min-ratio scan at m = 450 (the sliver boundary):
#     C1 symmetry+positivity, C2 argmin = mid, C3 min == central, C4 odd tie
#   * C5 (varfit > 187/216) exact at every spot m; C6 (strict increase)
#     across the resume boundaries 481->482 and 495->496, and at 449->450->451
#   * footer checkpoint varfit values (534/535/536/537/540/560) re-derived
#     exactly and compared to 12 digits.
import os, time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, "..", "..", "g2_scripts", "campaign_20260811")
RES_540 = os.path.join(BASE, "wave2_repairs", "results_m540.txt")
RES_560 = os.path.join(BASE, "harness_m560", "results_m560.txt")

SPOT_ROWS = {401: RES_540, 450: RES_540, 482: RES_560, 536: RES_560,
             554: RES_560, 560: RES_560}
VARFIT_AT = sorted({401, 449, 450, 451, 481, 482, 495, 496,
                    534, 535, 536, 537, 540, 554, 560})
FOOTER = {534: "0.997978810615", 535: "0.997982586007", 536: "0.997986347205",
          537: "0.997990094521", 540: "0.998001253256", 560: "0.998072591511"}

def mul_qint(poly, d):
    """poly * (1 + q + ... + q^{d-1}) via prefix sums (independent rewrite)."""
    n = len(poly)
    out = [0] * (n + d - 1)
    acc = 0
    for i in range(len(out)):
        if i < n:
            acc += poly[i]
        if i >= d:
            acc -= poly[i - d]
        out[i] = acc
    return out

def central_varfit(m, a):
    N = m * (m - 1) // 2
    mid = N // 2
    r = Fraction(a[mid] * a[mid], a[mid - 1] * a[mid + 1])
    var = Fraction(m * (m - 1) * (2 * m + 5), 72)
    return r, (r - 1) * var, N, mid

def file_row(path, m):
    for line in open(path):
        p = line.split()
        if p and p[0].isdigit() and int(p[0]) == m:
            return line.rstrip("\n")
    return None

t0 = time.time()
poly = [1]
varfits = {}
rows_out = {}
scan450 = None
C_SHARP = Fraction(187, 216)

for m in range(2, 561):
    poly = mul_qint(poly, m)
    if m in VARFIT_AT:
        r, vf, N, mid = central_varfit(m, poly)
        varfits[m] = vf
        if m in SPOT_ROWS:
            mfit = float(m * (1 - vf))
            rows_out[m] = (f"{m:>4} {N:>6} {mid:>6} {mid:>6} "
                           f"{float(r - 1):>12.4e} {float(vf):>12.10f} {mfit:>8.5f} "
                           f"{'PASS':>6}")
    if m == 450:
        # full exact certificate battery at the sliver boundary
        N = m * (m - 1) // 2
        a = poly
        c1 = (len(a) == N + 1) and (a == a[::-1]) and all(c > 0 for c in a)
        mid = N // 2
        bn = bd = bk = None
        for k in range(1, N):          # FULL scan 1..N-1, no symmetry shortcut
            num = a[k] * a[k]
            den = a[k - 1] * a[k + 1]
            if bn is None or num * bd < bn * den:
                bn, bd, bk = num, den, k
        rmin = Fraction(bn, bd)
        rc = Fraction(a[mid] * a[mid], a[mid - 1] * a[mid + 1])
        c2 = (bk == mid)
        c3 = (rmin == rc)
        c4 = True
        if N % 2 == 1:
            rc2 = Fraction(a[mid + 1] * a[mid + 1], a[mid] * a[mid + 2])
            c4 = (rc == rc2)
        scan450 = (N, mid, bk, c1, c2, c3, c4, (rmin - 1) * Fraction(450 * 449 * 905, 72))

print(f"[build] polynomial to m = 560 rebuilt independently in {time.time()-t0:.1f} s")

print("\n[R] spot rows, my independently formatted line vs results-file line (byte compare)")
all_rows_ok = True
for m, path in sorted(SPOT_ROWS.items()):
    mine = rows_out[m]
    theirs = file_row(path, m)
    ok = (mine == theirs)
    all_rows_ok &= ok
    tag = "IDENTICAL" if ok else "MISMATCH"
    print(f"  m={m:>3} [{os.path.basename(path)}]: {tag}")
    if not ok:
        print(f"    mine  : '{mine}'")
        print(f"    theirs: '{theirs}'")

print("\n[450] full exact certificate battery at the sliver boundary m = 450")
N, mid, bk, c1, c2, c3, c4, vf450 = scan450
print(f"  N = {N} (odd: {N % 2 == 1}), mid = {mid}, argmin(full scan) = {bk}")
print(f"  C1 sym+pos: {c1};  C2 argmin==mid: {c2};  C3 min==central: {c3};  C4 odd tie: {c4}")
print(f"  varfit(450) = {float(vf450):.10f}  > 187/216: {vf450 > C_SHARP}")

print("\n[C5/C6] exact varfit checks at the sampled m")
c5_ok = all(varfits[m] > C_SHARP for m in varfits)
pairs = [(449, 450), (450, 451), (481, 482), (495, 496), (534, 535),
         (535, 536), (536, 537), (554, 560)]
c6_ok = all(varfits[a] < varfits[b] for a, b in pairs)
print(f"  C5 varfit > 187/216 at all sampled m: {c5_ok}")
print(f"  C6 strict increase across sampled pairs incl. resume boundaries "
      f"481->482, 495->496: {c6_ok}")

print("\n[F] footer checkpoint varfit values (12 digits) vs my exact recomputation")
foot_ok = True
for m, s in sorted(FOOTER.items()):
    mine = f"{float(varfits[m]):.12f}"
    ok = (mine == s)
    foot_ok &= ok
    print(f"  varfit({m}) = {mine}  vs footer {s} : {'MATCH' if ok else 'MISMATCH'}")

overall = all_rows_ok and c1 and c2 and c3 and c4 and c5_ok and c6_ok and foot_ok
print(f"\nOVERALL: {'PASS' if overall else 'FAIL'}")
