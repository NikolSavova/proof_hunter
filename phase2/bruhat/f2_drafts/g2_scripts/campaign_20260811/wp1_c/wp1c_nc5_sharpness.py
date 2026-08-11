"""NC-W5: slack of the new bounds against the true |phi_lam|, and the
crossover clause (W.6).

(a) Corollary W.4 on [t_1, pi], lam = K/m: measured max|phi| vs exp(-c_1(K) m).
(b) Untilted clause on [2pi/m, pi] at m = 40 vs exp(-c_1'(0) m); compare the
    ledger's NC-5 value (max|phi| = 1.1e-16 at m = 40).
(c) Corollary W.5 (deep tilt) on [t_0(lam), pi]: measured max|phi| vs
    exp(-m q(m sinh(lam/2), 1)).
(d) Clause W.6 (crossover lower bound) pointwise on [pi/m, t_0(lam)]:
      -log|phi| >= m ((M-1)/(2M)) [log(1 + 1/r) - 1/(rM)]
    wherever the bracket is positive (min margin ratio reported; must be >= 1).

Run: python3 wp1c_nc5_sharpness.py    (stdlib only)
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
    return 0.0 if M <= 1.0 else I_closed(M, r) / (2.0 * M)

def log_abs_phi(m, lam, t):
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

def max_abs_phi(m, lam, ta, tb, n=4000):
    mx = -math.inf
    for i in range(n + 1):
        t = ta + (tb - ta) * i / n
        mx = max(mx, log_abs_phi(m, lam, t))
    return mx

C1 = {1: 0.2259, 2: 0.1802, 4: 0.1019}

def main():
    ok = True
    print("NC-W5(a) Cor W.4 on [t_1, pi] (lam = K/m): measured vs bound")
    for m in (30, 60, 100):
        t1 = math.sqrt(2) * math.pi / m
        for K in (1, 2, 4):
            lp = max_abs_phi(m, K / m, t1, math.pi)
            b = -C1[K] * m
            print(f"  m={m:4d} K={K}: max|phi| = e^{lp:9.3f}  bound = e^{b:9.3f}"
                  f"   slack e^{b - lp:7.2f}  ok={lp <= b}")
            ok &= lp <= b
    print("NC-W5(b) untilted clause on [2pi/m, pi], m = 40")
    lp = max_abs_phi(40, 0.0, 2 * math.pi / 40, math.pi, n=8000)
    b = -0.4617 * 40
    print(f"  measured max|phi| = {math.exp(lp):.3e} (ledger NC-5: 1.1e-16)"
          f"   bound = {math.exp(b):.3e}   ok={lp <= b}")
    ok &= lp <= b

    print("NC-W5(c) Cor W.5 (deep tilt) on [t_0(lam), pi]")
    for m in (100, 300):
        for lam in (0.1, 0.3, 0.5, 1.0):
            sh = math.sinh(lam / 2)
            t0 = 2 * math.asin(sh)
            c = q(m * sh, 1.0)
            lp = max_abs_phi(m, lam, t0, math.pi)
            print(f"  m={m:4d} lam={lam}: max|phi| = e^{lp:9.3f}  "
                  f"bound = e^{-c * m:9.3f}  ok={lp <= -c * m}")
            ok &= lp <= -c * m

    print("NC-W5(d) crossover clause W.6 on [pi/m, t_0(lam)]")
    worst = math.inf
    warg = None
    for m in (100, 300):
        for lam in (0.1, 0.3, 0.5):
            S = math.sinh(lam / 2) ** 2
            t0 = 2 * math.asin(math.sinh(lam / 2))
            ta = math.pi / m
            for i in range(1, 400):
                t = ta + (t0 - ta) * i / 400
                sn = math.sin(t / 2)
                M = m * sn
                if M <= 1.0:
                    continue
                r = S / sn ** 2
                br = math.log(1 + 1 / r) - 1 / (r * M)
                if br <= 0:
                    continue
                lb = m * ((M - 1) / (2 * M)) * br
                lp = log_abs_phi(m, lam, t)
                ratio = (-lp) / lb
                if ratio < worst:
                    worst, warg = ratio, (m, lam, t)
    print(f"  min (-log|phi|)/(W.6 lower bound) = {worst:.4f} at (m, lam, t) = "
          f"({warg[0]}, {warg[1]}, {warg[2]:.4f})   (PASS iff >= 1)")
    ok &= worst >= 1.0

    print(f"NC-W5 VERDICT: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
