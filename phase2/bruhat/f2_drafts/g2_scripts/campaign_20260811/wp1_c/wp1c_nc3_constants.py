"""NC-W3: chain-constant certificates and the named constants of Corollaries
W.4 / W.5 (rounded in the safe direction; mpmath dps=50 confirmations).

Chain (all for m >= 30, |K| <= m/4):
  (1) M_1  := m sin(sqrt2 pi/(2m))  >= 2.2194   (increasing in m; min at m=30)
  (2) M'   := m sin(pi/m)           >= 3.1358
  (3) M_V  := m sin(pi/(2m))        >= 1.5700
  (4) cosh^2(1/8) <= 1.0157066  =>  sinh^2(lam/2) <= 0.253927 K^2/m^2 for |lam| <= K/m
  (5) sin^2(t_1/2) >= (2.2194/m)^2 = 4.9257/m^2    (t_1 = sqrt2 pi/m)
      sin^2(pi/m)  >= (3.1358/m)^2 = 9.8332/m^2
  (6) r_1(K) := 0.253927 K^2/4.9257 <= 0.05156 K^2      [t >= t_1 cut]
      r'(K)  := 0.253927 K^2/9.8332 <= 0.02583 K^2      [t >= 2pi/m cut]
  (7) r_V := sup_{m>=30} [sinh(pi/(2m))/sin(pi/(2m))]^2 <= 1.00183
      (ratio increasing in the argument; worst at m = 30)

Named constants (round DOWN, they are lower bounds on decay exponents):
  c_1(K)  := q(2.2194, 0.05156 K^2)    far bound on [t_1, pi],   |lam| <= K/m
  c_1'(K) := q(3.1358, 0.02583 K^2)    far bound on [2pi/m, pi], |lam| <= K/m
  c_V     := q(1.5700, 1.00183)        far bound on [pi/m, pi],  |lam| <= pi/m
  c_5     := q(pi/2, 1)                deep-tilt floor, exact arguments

Run: python3 wp1c_nc3_constants.py    (stdlib + mpmath)
"""
import math, sys
from mpmath import mp, mpf, sin as msin, sinh as msinh, cosh as mcosh, \
    log as mlog, atan as matan, sqrt as msqrt, pi as mpi, asinh as masinh, \
    asin as masin

mp.dps = 50

def q_mp(M, r):
    M, r = mpf(M), mpf(r)
    if r == 0:
        return (M * mlog(M) - M + 1) / M
    sr = msqrt(r)
    I = (M * mlog((1 + r) * M * M / (r * M * M + 1))
         - (2 / sr) * (matan(sr * M) - matan(sr)))
    return I / (2 * M)

def main():
    ok = True
    print("NC-W3 chain certificates (m >= 30)")

    # (1)-(3): m sin(c/m) increasing in m (sin x/x decreasing); min at m = 30
    for name, c, floor in (("M_1 (c = sqrt2 pi/2)", msqrt(2) * mpi / 2, "2.2194"),
                           ("M'  (c = pi)        ", mpi, "3.1358"),
                           ("M_V (c = pi/2)      ", mpi / 2, "1.5700")):
        v30 = 30 * msin(c / 30)
        incr = all(
            (mm + 1) * msin(c / (mm + 1)) >= mm * msin(c / mm) - mpf("1e-45")
            for mm in range(30, 400))
        good = v30 >= mpf(floor)
        print(f"  {name}: value at m=30 = {mp.nstr(v30, 10)}  >= {floor}: {good}"
              f"   monotone incr (m=30..400 spot): {incr}")
        ok &= good and incr

    # (4)
    c4 = mcosh(mpf(1) / 8) ** 2
    good = c4 <= mpf("1.0157066")
    print(f"  cosh^2(1/8) = {mp.nstr(c4, 10)} <= 1.0157066: {good}")
    ok &= good
    good = mpf("1.0157066") / 4 <= mpf("0.253927")
    print(f"  1.0157066/4 = {mp.nstr(mpf('1.0157066')/4, 10)} <= 0.253927: {good}")
    ok &= good

    # (5)-(6)
    r1 = mpf("0.253927") / mpf("4.9257")
    rp = mpf("0.253927") / mpf("9.8332")
    good = (mpf("2.2194") ** 2 >= mpf("4.9257")) and (mpf("3.1358") ** 2 >= mpf("9.8332"))
    print(f"  2.2194^2 = {mp.nstr(mpf('2.2194')**2, 8)} >= 4.9257 and "
          f"3.1358^2 = {mp.nstr(mpf('3.1358')**2, 8)} >= 9.8332: {good}")
    ok &= good
    good = (r1 <= mpf("0.05156")) and (rp <= mpf("0.02583"))
    print(f"  r_1 coeff = {mp.nstr(r1, 8)} <= 0.05156: {r1 <= mpf('0.05156')}; "
          f"r' coeff = {mp.nstr(rp, 8)} <= 0.02583: {rp <= mpf('0.02583')}")
    ok &= good

    # (7)
    x = mpi / 60
    rv = (msinh(x) / msin(x)) ** 2
    incr = all((msinh(mpf(i) / 1000) / msin(mpf(i) / 1000))
               <= (msinh(mpf(i + 1) / 1000) / msin(mpf(i + 1) / 1000))
               for i in range(1, 1500))
    good = rv <= mpf("1.00183")
    print(f"  r_V at m=30: {mp.nstr(rv, 10)} <= 1.00183: {good}; "
          f"sinh/sin increasing (grid to x=1.5): {incr}")
    ok &= good and incr

    print()
    print("Named constants (mpmath dps=50; quote = value rounded DOWN)")
    tab = []
    for K in (0, 1, 2, 3, 4, 5, 6):
        v = q_mp("2.2194", mpf("0.05156") * K * K)
        tab.append((f"c_1({K})", v))
    tab.append(("c_1(pi)", q_mp("2.2194", mpf("0.05156") * mpi ** 2)))
    tab.append(("c_1(1.7)", q_mp("2.2194", mpf("0.05156") * mpf("1.7") ** 2)))
    tab.append(("c_1(1.75)", q_mp("2.2194", mpf("0.05156") * mpf("1.75") ** 2)))
    for K in (0, 1, 2, 4):
        v = q_mp("3.1358", mpf("0.02583") * K * K)
        tab.append((f"c_1'({K})", v))
    tab.append(("c_V", q_mp("1.5700", "1.00183")))
    tab.append(("c_5 = q(pi/2, 1)", q_mp(mpi / 2, 1)))
    tab.append(("q(2,0) (= log2 - 1/2, Lemma 1.4 check)", q_mp(2, 0)))
    for name, v in tab:
        print(f"  {name:14s} = {mp.nstr(v, 12)}")
    l14 = mlog(2) - mpf(1) / 2
    dev = abs(q_mp(2, 0) - l14)
    print(f"  |q(2,0) - (log2 - 1/2)| = {mp.nstr(dev, 3)}  (exact-identity check)")
    ok &= dev < mpf("1e-45")

    print()
    print("Comparison with the T2 draft's proved far constants")
    for K in (1, 2, 3, 4):
        c_new = float(q_mp("2.2194", mpf("0.05156") * K * K))
        c_t7c = 0.06 * math.exp(-2 * K)
        print(f"  K={K}: c_1(K) = {c_new:.4f}  vs T.7c 0.06 e^(-2K) = {c_t7c:.3e}"
              f"   improvement x{c_new / c_t7c:.0f}")
    c_v = float(q_mp("1.5700", "1.00183"))
    t7b = (1 / math.pi) / 4730
    print(f"  c_V = {c_v:.5f}  vs T.7b-final exponent/m -> (1/pi)/4730 = {t7b:.3e}"
          f"   improvement x{c_v / t7b:.0f}")

    print()
    print("Deep-tilt table: t_0(lam) = 2 arcsin(sinh(lam/2)), "
          "c(lam, m) = q(m sinh(lam/2), 1)")
    print("  lam     t_0(lam)   c(lam,100)  c(lam,300)")
    for lam_s in ("0.05", "0.1", "0.2", "0.3", "0.5", "0.8", "1.0", "1.3", "1.6", "1.7"):
        lam = mpf(lam_s)
        sh = msinh(lam / 2)
        t0 = 2 * masin(sh) if sh <= 1 else None
        c100 = q_mp(100 * sh, 1)
        c300 = q_mp(300 * sh, 1)
        t0s = mp.nstr(t0, 6) if t0 is not None else "  --  "
        print(f"  {lam_s:5s}  {t0s:9s}  {mp.nstr(c100, 6):10s} {mp.nstr(c300, 6):10s}")
    lam_max = 2 * masinh(1)
    print(f"  scope end: 2 asinh(1) = {mp.nstr(lam_max, 8)}")

    print(f"\nNC-W3 VERDICT: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
