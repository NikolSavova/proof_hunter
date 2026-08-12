"""NC-A1: certify Lemma A.1 (tilted Gaussian domination + model approximation)
and Lemma A.2 (model kernel identity).

 (a) eps_K(m) table; structural check that V_Re(t)/(s2 t^2/2) is maximized at
     t = t1 (each term is a positive multiple of t^{r-2}, r >= 4; verified on a
     grid as well).
 (b) TRUTH of (A.1a): |phi_lam^c(t)| <= exp(-(1-eps) s2min t^2/2) on (0, t1],
     against the exact factor product at mpmath dps 40,
     m in {30, 60, 120}, K in {1, 2, 4}, w in {K/4, K/2, K}, 48-point t-grids.
 (c) TRUTH of (A.1b): |phi_lam^c(t) - phihat(t)| <= e^{-(1-eps) s2min t^2/2}
     * W_A(t) on the same grids, where phihat = e^{-s2 t^2/2} hatQ(t) with the
     TRUE cumulants of (m, lam) and W_A uses the BOX coefficients at (K, m).
 (d) Lemma A.2 (model kernel identity, Hermitian psi): with psi := phihat,
       (1/4pi^2) intint psi(s)psi(t)(1 - cos(s-t)) ds dt
         = q(0)^2 - q(1)q(-1),
     via the 1-D reduction  q(1)q(-1) = (1/4pi^2)[(int psi cos)^2 +
     (int psi sin)^2]  (mp.quad, m = 30, w = 1 and m = 60, w = 2), and
     q(x) = Z(y) P(y) cross-check (Fourier rule).

Run: python3 wp2a2_nc1_model_err.py
"""
import math
import os
import sys

import mpmath as mp

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import wp2a2_lib as L
lib = L.lib

mp.mp.dps = 40


# ---- high-precision tilted cf and cumulants ----
def phi_c(m, lam, t):
    """phi_lam^c(t) = e^{-it mu} prod_j z_j(lam - it)/z_j(lam), mpmath."""
    lam = mp.mpf(lam)
    t = mp.mpf(t)
    mu = mp.mpf(0)
    prod = mp.mpc(1)
    for j in range(1, m + 1):
        u = lam * j
        mu += j * mp_g0(u) - mp_g0(lam)
        zj_l = (1 - mp.e**(-u)) / (1 - mp.e**(-lam)) if lam != 0 else mp.mpf(j)
        zj_c = (1 - mp.e**(-(lam - 1j * t) * j)) / (1 - mp.e**(-(lam - 1j * t)))
        prod *= zj_c / zj_l
    return mp.e**(-1j * t * mu) * prod


def mp_g0(u):
    if abs(u) < mp.mpf("1e-8"):
        return mp.mpf(0.5) - u / 12 + u**3 / 720
    return 1 / u - 1 / mp.expm1(u)


def mp_gk(u, k):
    """k-th derivative of g via mp.diff of the closed form (dps-safe)."""
    return mp.diff(lambda x: 1 / x - 1 / mp.expm1(x), u, k)


def mp_cumulants(m, lam):
    lam = mp.mpf(lam)
    out = []
    for r in range(2, 7):
        k = r - 1
        gl = mp_gk(lam, k)
        s = mp.mpf(0)
        for j in range(1, m + 1):
            s += j**r * mp_gk(lam * j, k) - gl
        # kappa_r = (-1)^{r+1} [ sum_j j^r g^{(r-1)}(lam j) - m g^{(r-1)}(lam) ]
        # (T.2: kappa_r = (-1)^r d^r/dlam^r log z_j, log z_j = log j + f(lam j)
        #  - f(lam), f^{(r)} = -g^{(r-1)}; matches lib.cumulants' signs.)
        out.append(s * ((-1) ** (r + 1)))
    return out


def true_model_coeffs(m, lam):
    """(s2, alpha, beta, delta, gamma) at mpmath precision, via lemma T.2:
    kappa_r = (-1)^r [ sum_j j^r f^{(r)}(lam j)... ] -- use the verified float
    lib for a cross-check and mp.diff for precision."""
    k2, k3, k4, k5, k6 = mp_cumulants(m, lam)
    s2 = k2
    return s2, k3 / 6, -k4 / 24, k5 / 120, k6 / 720


def hatQ(t, alpha, beta, delta, gamma):
    t = mp.mpf(t)
    E2 = [(-1j * alpha, 3), (-beta, 4), (1j * delta, 5), (-gamma, 6)]
    q = mp.mpc(1)
    for c, n in E2:
        q += c * t**n
    # + degree <= 8 part of E^2/2
    q += (-alpha**2 / 2) * t**6
    q += (1j * alpha * beta) * t**7
    q += (beta**2 / 2 + alpha * delta) * t**8
    return q


def main():
    ok = True
    print("NC-A1: Lemma A.1 / A.2 certification (mpmath dps = %d)" % mp.mp.dps)

    # ---------- (a) eps table ----------
    print("(a) eps_K(m)  [Gaussian-domination weakening; must be < 1]:")
    print("      m     K=1      K=2      K=4")
    for m in (30, 60, 120, 180, 379, 500, 2000):
        row = [L.coef_boxes(K, m)["eps"] for K in (1, 2, 4)]
        print("   %4d  %7.4f  %7.4f  %7.4f" % (m, *row))
        ok &= all(e < 1 for e in row)
    # ratio V_Re(t)/(s2 t^2/2) increasing in t: check on grid at (30, K=4)
    B = L.coef_boxes(4, 30)
    prev, mono = -1.0, True
    for i in range(1, 101):
        t = B["t1"] * i / 100
        val = (B["A4"]*t**4 + B["A6"]*t**6 + B["A7"]*t**7) / (B["s2min"]*t*t/2)
        mono &= val >= prev - 1e-15
        prev = val
    print("    V_Re/(s2min t^2/2) nondecreasing on (0, t1] (m=30, K=4):", mono)
    ok &= mono

    # ---------- (b), (c) truth of A.1a / A.1b ----------
    print("(b,c) |phi| vs Gaussian majorant and |phi - phihat| vs W_A bound:")
    print("      m  K    w     max |phi|/dom   max |phi-phihat|/(dom*W_A)")
    worst_a = worst_b = 0.0
    for m in (30, 60, 120):
        for K in (1, 2, 4):
            B = L.coef_boxes(K, m)
            WA = L.wa_poly(K, m, B)
            eps, t1, s2min = B["eps"], B["t1"], B["s2min"]
            for wfrac in (0.25, 0.5, 1.0):
                w = K * wfrac
                lam = w / m
                s2, al, be, de, ga = true_model_coeffs(m, lam)
                ra = rb = 0.0
                for i in range(1, 49):
                    t = t1 * i / 48
                    ph = phi_c(m, lam, t)
                    dom = mp.e**(-(1 - eps) * s2min * t * t / 2)
                    ra = max(ra, float(abs(ph) / dom))
                    phat_t = mp.e**(-s2 * t * t / 2) * hatQ(t, al, be, de, ga)
                    WAt = sum(c * t**n for n, c in WA.items())
                    if WAt > 0:
                        rb = max(rb, float(abs(ph - phat_t) / (dom * WAt)))
                if wfrac == 1.0:
                    print("   %4d %2d %5.2f   %12.6f   %12.6f" % (m, K, w, ra, rb))
                worst_a, worst_b = max(worst_a, ra), max(worst_b, rb)
    print("    GLOBAL max ratios: (A.1a) %.6f  (A.1b) %.6f   (PASS iff <= 1)"
          % (worst_a, worst_b))
    ok &= worst_a <= 1.0 and worst_b <= 1.0

    # cross-check the mp cumulants against the (fixed) float lib
    m, lam = 60, 2.0 / 60
    mu_f, s2_f, k3_f, k4_f, k5_f, k6_f = lib.cumulants(m, lam)
    k2m, k3m, k4m, k5m, k6m = [float(x) for x in mp_cumulants(m, lam)]
    devs = [abs(s2_f - k2m) / abs(k2m), abs(k3_f - k3m) / abs(k3m),
            abs(k4_f - k4m) / abs(k4m), abs(k5_f - k5m) / abs(k5m),
            abs(k6_f - k6m) / abs(k6m)]
    print("    lib-vs-mp cumulant rel devs (m=60, w=2): max = %.2e" % max(devs))
    ok &= max(devs) < 1e-9

    # ---------- (d) Lemma A.2 ----------
    print("(d) model kernel identity (Hermitian psi), 1-D reduction:")
    for (m, w) in ((30, 1.0), (60, 2.0)):
        lam = w / m
        s2, al, be, de, ga = true_model_coeffs(m, lam)

        def psi(t):
            return mp.e**(-s2 * t * t / 2) * hatQ(t, al, be, de, ga)

        T = 14 / mp.sqrt(s2)
        I1 = mp.quad(psi, [-T, 0, T])
        Ic = mp.quad(lambda t: psi(t) * mp.cos(t), [-T, 0, T])
        Is = mp.quad(lambda t: psi(t) * mp.sin(t), [-T, 0, T])
        lhs = (I1**2 - Ic**2 - Is**2) / (4 * mp.pi**2)   # Dhat via 1-D pieces
        # q(x) via the Fourier rule = Z(y) P(y)
        a_s = al / s2**mp.mpf(1.5); b_s = be / s2**2
        d_s = de / s2**mp.mpf(2.5); g_s = ga / s2**3
        h = 1 / mp.sqrt(s2)

        def ZP(y):
            He = lambda n: mp.hermite(n, y / mp.sqrt(2)) / mp.mpf(2) ** (n / mp.mpf(2))
            P = (1 + a_s * He(3) - b_s * He(4) + d_s * He(5)
                 + (g_s + a_s**2 / 2) * He(6) - a_s * b_s * He(7)
                 + (b_s**2 / 2 + a_s * d_s) * He(8))
            return mp.e**(-y * y / 2) / mp.sqrt(2 * mp.pi * s2) * P

        rhs = ZP(mp.mpf(0))**2 - ZP(h) * ZP(-h)
        # direct quadrature of q(x) for the cross-check
        q0 = I1 / (2 * mp.pi)
        dev_q = abs(q0 - ZP(mp.mpf(0))) / ZP(mp.mpf(0))
        dev = abs(lhs - rhs) / abs(rhs)
        im_ok = abs(mp.im(lhs)) < mp.mpf("1e-30")
        print("    (m,w)=(%d,%g): |Dhat_1D - (q0^2-q1q-1)|/|.| = %.2e ; "
              "q(0) vs Z*P rel dev = %.2e ; Im ~ 0: %s"
              % (m, w, float(dev), float(dev_q), im_ok))
        ok &= float(dev) < 1e-25 and float(dev_q) < 1e-20 and im_ok

    print("\nNC-A1 VERDICT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
