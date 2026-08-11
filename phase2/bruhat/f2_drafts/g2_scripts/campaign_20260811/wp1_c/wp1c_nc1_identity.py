"""NC-W1: the exact sinh/sin modulus factorization (Lemma W.1) and the
per-factor envelope (Lemma W.2), verified from scratch.

(a) Per-factor identity, high precision (mpmath dps=40):
      |nu_j(t)|^2 = (S_j + sin^2(jt/2)) * S / ((S + sin^2(t/2)) * S_j),
    S := sinh^2(lam/2), S_j := sinh^2(lam*j/2),
    against the direct weight sum nu_j(t) = sum_{i<j} e^{(it-lam) i} / z_j(lam).

(b) Whole-cf product check at m = 12: |phi_lam(t)| = prod_{j=2}^m |nu_j(t)|
    against the tilted Mahonian sum  |sum_k a_k e^{-lam k} e^{itk}| / Z
    (a_k exact integers from the generating-product DP).

(c) Envelope check: |nu_j(t)|^2 <= (S + min(s, 1/j^2))/(S + s) on a large
    random + adversarial grid (min margin reported; must be >= -1e-30).

(d) Spot grids for the two elementary inequalities used in W.2's proof
    (both proved by induction in the text): sinh(j u) >= j sinh(u),
    |sin(j v)| <= j |sin v|.

Run: python3 wp1c_nc1_identity.py     (stdlib + mpmath)
"""
import sys, random
from mpmath import mp, mpf, mpc, sin, sinh, exp, sqrt, fabs, pi

mp.dps = 40

def nu_direct(j, lam, t):
    z = sum(exp(-lam * i) for i in range(j))
    v = sum(exp(mpc(-lam, t) * i) for i in range(j))
    return v / z

def nu2_formula(j, lam, t):
    S = sinh(lam / 2) ** 2
    Sj = sinh(lam * j / 2) ** 2
    s = sin(t / 2) ** 2
    sj = sin(j * t / 2) ** 2
    return (Sj + sj) * S / ((S + s) * Sj)

def mahonian(m):
    poly = [1]
    for d in range(1, m + 1):
        out = [0] * (len(poly) + d - 1)
        run = 0
        for k in range(len(out)):
            if k < len(poly):
                run += poly[k]
            if k - d >= 0:
                run -= poly[k - d]
            out[k] = run
        poly = out
    return poly

def main():
    ok = True
    rng = random.Random(20260811)

    # (a) per-factor identity
    worst = mpf(0)
    warg = None
    for _ in range(400):
        j = rng.choice([2, 3, 5, 8, 13, 21, 47, 100, 200])
        lam = mpf(rng.choice(["0.001", "0.01", "0.1", "0.5", "1.0", "3.0"]))
        t = mpf(rng.uniform(1e-4, float(pi) - 1e-4))
        d = nu_direct(j, lam, t)
        lhs = (d.real ** 2 + d.imag ** 2)
        rhs = nu2_formula(j, lam, t)
        rel = fabs(lhs - rhs) / rhs
        if rel > worst:
            worst, warg = rel, (j, float(lam), float(t))
    print(f"NC-W1(a) per-factor identity: max rel dev = {mp.nstr(worst, 3)} "
          f"at (j, lam, t) = {warg}  (dps=40; PASS iff < 1e-30)")
    ok &= worst < mpf("1e-30")

    # (b) whole-cf product vs tilted Mahonian sum, m = 12
    m = 12
    a = mahonian(m)
    worstb = mpf(0)
    for lam_s in ("0.05", "0.5"):
        lam = mpf(lam_s)
        Z = sum(a[k] * exp(-lam * k) for k in range(len(a)))
        for t_s in ("0.3", "1.7", "3.0"):
            t = mpf(t_s)
            v = sum(a[k] * exp(mpc(-lam, t) * k) for k in range(len(a)))
            lhs = sqrt(v.real ** 2 + v.imag ** 2) / Z
            rhs = mpf(1)
            for j in range(2, m + 1):
                rhs *= sqrt(nu2_formula(j, lam, t))
            rel = fabs(lhs - rhs) / rhs
            worstb = max(worstb, rel)
    print(f"NC-W1(b) product vs tilted-Mahonian sum (m=12): max rel dev = "
          f"{mp.nstr(worstb, 3)}  (PASS iff < 1e-30)")
    ok &= worstb < mpf("1e-30")

    # (c) envelope
    min_margin = mpf("inf")
    marg = None
    cases = []
    for _ in range(2000):
        j = rng.randint(2, 300)
        lam = mpf(rng.choice(["0.001", "0.01", "0.1", "0.3", "0.5", "1.0", "2.5"]))
        t = mpf(rng.uniform(1e-4, float(pi) - 1e-4))
        cases.append((j, lam, t))
    # adversarial: t near zeros of sin(jt/2) and near-resonant points
    for j in (2, 3, 5, 10, 50, 200):
        for l_s in ("0.01", "0.3", "1.0"):
            for kk in range(1, j):
                t = mpf(2) * pi * kk / j
                if 0 < t < pi:
                    cases.append((j, mpf(l_s), t - mpf("1e-6")))
                    cases.append((j, mpf(l_s), min(t + mpf("1e-6"), pi - mpf("1e-8"))))
    for (j, lam, t) in cases:
        S = sinh(lam / 2) ** 2
        s = sin(t / 2) ** 2
        env = (S + min(s, mpf(1) / j ** 2)) / (S + s)
        val = nu2_formula(j, lam, t)
        margin = env - val
        if margin < min_margin:
            min_margin, marg = margin, (j, float(lam), float(t))
    print(f"NC-W1(c) envelope: min (bound - value) = {mp.nstr(min_margin, 4)} "
          f"at (j, lam, t) = {marg}  over {len(cases)} cases  (PASS iff >= -1e-30)")
    ok &= min_margin >= mpf("-1e-30")

    # (d) inequality spot grids
    okd = True
    for j in range(1, 60):
        for iu in range(1, 40):
            u = mpf(iu) / 10
            if sinh(j * u) < j * sinh(u) - mpf("1e-30"):
                okd = False
        for iv in range(1, 63):
            v = mpf(iv) / 10
            if fabs(sin(j * v)) > j * fabs(sin(v)) + mpf("1e-30"):
                okd = False
    print(f"NC-W1(d) sinh(ju) >= j sinh(u) and |sin(jv)| <= j|sin v| spot grids: "
          f"{'PASS' if okd else 'FAIL'}")
    ok &= okd

    print(f"NC-W1 VERDICT: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
