"""NC-W2: the master far-region bound (Lemma W.3):

    -log|phi_lam(t)| >= m * q(M, r),   M = m sin(t/2),  r = sinh^2(lam/2)/sin^2(t/2),

    q(M, r) = I(M, r)/(2M),
    I(M, r) = M log[(1+r)M^2/(rM^2+1)] - (2/sqrt r)(arctan(sqrt r M) - arctan(sqrt r)),
    I(M, 0) = 2 (M log M - M + 1),      (q := 0 when M <= 1)

checked three ways:

(a) closed form I(M,r) vs numerical quadrature of f(u) = log[(1+r)u^2/(ru^2+1)]
    over [1, M]  (mpmath.quad, dps=30);
(b) the bound itself against the true |phi_lam(t)| (exact modulus factorization,
    log-space product) on dense grids over m, lam, t — the certified quantity is
    ratio := m q / (-log|phi|) <= 1 wherever M > 1;
(c) monotonicity spot grids: q nondecreasing in M (M >= 1), nonincreasing in r
    (both proved analytically in the draft; grids are belt-and-suspenders).

Run: python3 wp1c_nc2_master.py     (stdlib + mpmath for (a) only)
"""
import math, sys

def I_closed(M, r):
    if M <= 1.0:
        return 0.0
    if r == 0.0:
        return 2.0 * (M * math.log(M) - M + 1.0)
    sr = math.sqrt(r)
    return (M * math.log((1.0 + r) * M * M / (r * M * M + 1.0))
            - (2.0 / sr) * (math.atan(sr * M) - math.atan(sr)))

def q(M, r):
    if M <= 1.0:
        return 0.0
    return I_closed(M, r) / (2.0 * M)

def log_abs_phi(m, lam, t):
    """log|phi_lam(t)| via the exact modulus factorization (Lemma W.1)."""
    s = math.sin(t / 2.0) ** 2
    if lam == 0.0:
        tot = 0.0
        for j in range(2, m + 1):
            sj = math.sin(j * t / 2.0) ** 2
            if sj == 0.0:
                return -math.inf
            tot += 0.5 * (math.log(sj) - math.log(j * j * s))
        return tot
    S = math.sinh(lam / 2.0) ** 2
    tot = 0.0
    for j in range(2, m + 1):
        Sj = math.sinh(lam * j / 2.0) ** 2
        sj = math.sin(j * t / 2.0) ** 2
        tot += 0.5 * (math.log(Sj + sj) + math.log(S)
                      - math.log(S + s) - math.log(Sj))
    return tot

def main():
    ok = True

    # (a) closed form vs quadrature
    from mpmath import mp, mpf, quad, log as mlog, atan as matan, sqrt as msqrt
    mp.dps = 30
    worst = mpf(0)
    for M in (1.2, 2.2194, 3.1359, 10.0, 100.0):
        for r in (0.0, 1e-6, 0.05156, 0.5, 1.0, 3.0, 10.0):
            Mm, rm = mpf(M), mpf(r)
            f = lambda u: mlog((1 + rm) * u * u / (rm * u * u + 1))
            Iq = quad(f, [1, Mm])
            Ic = I_closed(M, r)
            rel = abs(Iq - Ic) / max(mpf(1e-30), abs(Iq))
            worst = max(worst, rel)
    print(f"NC-W2(a) closed form vs quadrature: max rel dev = {mp.nstr(worst,3)}"
          f"  (PASS iff < 1e-12)")
    ok &= worst < mpf("1e-12")

    # (b) the master bound vs true |phi|
    print("NC-W2(b) master bound: ratio = m q(M,r)/(-log|phi|) (must be <= 1)")
    global_max = 0.0
    g_arg = None
    for m in (30, 60, 100):
        lams = [0.0, 0.5 / m, 1.0 / m, math.pi / m, 4.0 / m,
                0.05, 0.1, 0.3, 0.5, 1.0, 1.5, 2.5]
        for lam in lams:
            S = math.sinh(lam / 2.0) ** 2
            mx = 0.0
            arg = None
            for i in range(1, 1200):
                t = math.pi * i / 1199.0
                sn = math.sin(t / 2.0)
                M = m * sn
                if M <= 1.0:
                    continue
                r = S / sn ** 2
                bound = m * q(M, r)
                if bound <= 0.0:
                    continue
                lp = log_abs_phi(m, lam, t)
                if lp == -math.inf:
                    continue
                ratio = bound / (-lp)
                if ratio > mx:
                    mx, arg = ratio, t
            if mx > global_max:
                global_max, g_arg = mx, (m, lam, arg)
            print(f"  m={m:4d} lam={lam:8.5f}: max ratio = {mx:.6f}")
            ok &= mx <= 1.0 + 1e-12
    print(f"  GLOBAL max ratio = {global_max:.6f} at (m, lam, t) = "
          f"({g_arg[0]}, {g_arg[1]:.5f}, {g_arg[2]:.5f})  (PASS iff <= 1)")

    # (c) monotonicity spot grids
    okc = True
    rs = [0.0, 0.01, 0.05156, 0.2, 0.5, 1.0, 2.0, 5.0, 20.0]
    Ms = [1.0 + 0.05 * i for i in range(200)] + [20.0, 50.0, 200.0]
    for r in rs:
        prev = -1.0
        for M in Ms:
            v = q(M, r)
            if v < prev - 1e-13:
                okc = False
            prev = v
    for M in (1.2, 1.5701, 2.2194, 3.1359, 8.0, 50.0):
        prev = math.inf
        for r in rs:
            v = q(M, r)
            if v > prev + 1e-13:
                okc = False
            prev = v
    print(f"NC-W2(c) q monotone (incr in M, decr in r) spot grids: "
          f"{'PASS' if okc else 'FAIL'}")
    ok &= okc

    print(f"NC-W2 VERDICT: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
