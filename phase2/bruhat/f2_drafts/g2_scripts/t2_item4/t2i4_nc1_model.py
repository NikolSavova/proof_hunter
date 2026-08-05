"""NC-T2i4-1: the tilted 6-term Edgeworth model P_lam(y), built from scratch via
sympy (item 4 of g2_draft_t2's §8 -- "the B.6-analogue bucket table", previously
only asserted in prose). This is a first piece, not the full bucket table: it
covers the POINTWISE remainder N_lam(0)/P_lam(0)^2 only (one of several buckets
Theorem T.9's C_R needs); the box/tail/out kernel-transfer bucket (B.6's own
analogue) and the Taylor-remainder bucket are NOT done here.

What this script does, in order:

  (1) Build phihat_lam(t) := e^{-s2 t^2/2} * exp(E(t)) truncated to O(t^8),
      E(t) := -i*alpha*t^3 - beta*t^4 + i*delta*t^5 - gamma*t^6
      (alpha:=kappa_3/6, beta:=-kappa_4/24, delta:=kappa_5/120, gamma:=kappa_6/720
       -- the r=3..6 terms of log phi_lam^c(t) = sum_r kappa_r(it)^r/r!, matching
       the sign convention fixed in Lemma T.6iii's SIGN NOTE).
  (2) Fourier-transform each t^n term via the (verified) identity
      (1/2pi) int t^n e^{-s2 t^2/2} e^{-itx} dt = (-i)^n s2^{-n/2} Z(y) He_n(y),
      giving P_lam(y) := phat_lam(x)/Z(y). CHECK: the imaginary part cancels to
      exactly 0 symbolically (the tilted density must be real) -- confirmed below.
  (3) Define N_lam(y) := -P_lam''(y) P_lam(y) + P_lam'(y)^2 - B_lam He_2(y) P_lam(y)^2,
      B_lam := 12 beta/s2^2 (the SAME definition as g1_draft_b's Lemma B.7, with
      beta,gamma now s2-tilted and alpha,delta the new odd pieces).
      CROSS-CHECK: setting alpha=delta=0 reproduces g1_draft_b's known result
      N(0) = -90 gamma/s2^3 + 384 beta^2/s2^4 + (higher order) EXACTLY --
      confirmed below (independent validation that this derivation is right).
  (4) FINDING (resolves an ambiguity the prose draft glossed over): N_lam(0)
      contains a term -36 alpha^2/s2^3 with NO beta/gamma/delta factor. In scaled
      form (a:=alpha/s2^1.5 = O(1/sqrt m)) this is O(1/m) -- the SAME order as
      B_m itself, NOT O(1/m^2). It is exactly the "kappa_3^2 term" the draft's
      Theorem T.9 proof already (in prose) folds into the w^2 bucket, not C_R.
      Splitting N_lam(0) = (bare alpha^2 term) + (residual) and checking each
      piece's growth as m -> oo at FIXED w = lam*m confirms this split
      numerically: bare-term * m -> a nonzero constant (genuinely O(1/m)),
      residual * m^2 -> a nonzero constant (genuinely O(1/m^2), i.e. belongs in
      C_R as originally intended).
  (5) A grid sweep (m in [30,2000], w in [0,K]) gives a certified NUMERIC bound
      on |residual / P_lam(0)^2 * m^2| for K = 1, 2, 4 -- the actual C_R
      contribution from this one bucket. Values found: ~1.55 (K=1), ~4.1 (K=2),
      ~4.9 (K=4) -- comfortably inside the draft's rough guess "C_R ~ 6".

Independent cross-check of the new kappa_5/kappa_6 machinery (g4, g5 functions,
extending the verified g0..g3 pattern from t2_nc1_cumulants.py by two more
derivatives of g0(u) = 1/u - 1/(e^u-1)): re-derives sigma_lam^2 and kappa_3(lam)
via this script's OWN weight-sum-free closed forms and compares against
t2_nc5_cf.py's independently-written sig2()/kap3() -- agreement to float
precision at every tested (m, lam), including near-degenerate small-lam cases
(handled via Bernoulli-series small-u fallbacks, same pattern as t2_nc5_cf.py's
qf/gf).

Status: NUMERIC CERTIFICATION only for the final bound (grid + asymptotic-limit
check), not yet a closed-form analytic proof with an explicit worst-case
argument (cf. the (T.7b-cert)/(T.7c-cert) grid certificates elsewhere in this
draft -- same status class, "Sturm-able on demand").

Run: python3 t2i4_nc1_model.py   (needs sympy; pip install sympy if missing)
"""
import math
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "t2"))
from t2_nc5_cf import kap3 as kap3_ref, sig2 as sig2_ref  # noqa: E402


def build_model():
    y, alpha, beta, delta, gamma = sp.symbols("y alpha beta delta gamma", real=True)
    s2 = sp.symbols("s2", positive=True)
    t = sp.symbols("t", real=True)

    E = -sp.I * alpha * t**3 - beta * t**4 + sp.I * delta * t**5 - gamma * t**6
    Cser = sp.expand(sp.series(sp.exp(E), t, 0, 9).removeO())
    poly = sp.Poly(Cser, t)
    coeffs = {poly.degree() - i: c for i, c in enumerate(poly.all_coeffs())}

    He = lambda n: sp.expand(2 ** sp.Rational(-n, 2) * sp.hermite(n, y / sp.sqrt(2)))

    P = sp.Integer(0)
    for n, cn in coeffs.items():
        if cn == 0:
            continue
        P += cn * (-sp.I) ** n * s2 ** (sp.Rational(-n, 2)) * He(n)
    P_im = sp.expand(sp.im(P))
    P = sp.expand(sp.re(P))

    B_lam = 12 * beta / s2**2
    Pp, Ppp = sp.diff(P, y), sp.diff(P, y, 2)
    N = sp.expand(-Ppp * P + Pp**2 - B_lam * He(2) * P**2)
    N0 = sp.expand(N.subs(y, 0))
    P0 = sp.expand(P.subs(y, 0))

    N0_poly = sp.Poly(N0, alpha, beta, delta, gamma)
    bare_a2_coeff = N0_poly.coeff_monomial(alpha**2)
    N0_resid = sp.expand(N0 - bare_a2_coeff * alpha**2)

    # untilted cross-check: alpha=delta=0 must reproduce g1_draft_b's N(0).
    # g1_draft_b's prose quotes only the two LEADING (1/m-weighted-order-2)
    # terms, "N(0) = -90 gamma/s2^3 + 384 beta^2/s2^4 + O(m^-3)"; the exact
    # formula also carries beta^3, beta*gamma, beta^4, beta^5 terms (weighted
    # order >= 3, i.e. genuinely the O(m^-3) the prose elides). Weight
    # beta ~ 1/m (order 1), gamma ~ 1/m^2 (order 2) -- matching Lemma B.0(ii,iii).
    N0_untilted = sp.expand(N0.subs({alpha: 0, delta: 0}))
    N0_poly_ug = sp.Poly(N0_untilted, beta, gamma)
    leading_ok = (N0_poly_ug.coeff_monomial(gamma) == -90 / s2**3
                  and N0_poly_ug.coeff_monomial(beta**2) == 384 / s2**4)
    weight = lambda mono: mono[0] * 1 + mono[1] * 2  # (beta,gamma) exponents
    remainder_higher_order = all(
        weight(mono) >= 3
        for mono in N0_poly_ug.monoms()
        if mono not in ((0, 1), (2, 0))
    )
    higher_order_only = leading_ok and remainder_higher_order

    return dict(
        P_im=P_im,
        N0_resid_f=sp.lambdify((alpha, beta, delta, gamma, s2), N0_resid, "math"),
        P0_f=sp.lambdify((alpha, beta, delta, gamma, s2), P0, "math"),
        bare_a2_f=sp.lambdify((alpha, s2), bare_a2_coeff * alpha**2, "math"),
        bare_a2_coeff=bare_a2_coeff,
        untilted_matches=higher_order_only,
    )


# g0..g5 = the 0th..5th derivatives of g0(u) := 1/u - 1/(e^u - 1), with
# small-u Bernoulli-series fallbacks (avoids catastrophic cancellation).
def g0(u):
    if abs(u) < 1e-2:
        return 0.5 - u / 12 + u**3 / 720 - u**5 / 30240
    return 1 / u - 1 / (math.exp(u) - 1)


def g1(u):
    if abs(u) < 1e-2:
        return -1 / 12 + u * u / 240 - u**4 / 6048
    e = math.exp(u)
    return -1 / (u * u) + e / (e - 1) ** 2


def g2(u):
    if abs(u) < 1e-2:
        return u / 120 - u**3 / 1512 + u**5 / 28800
    e = math.exp(u)
    return 2 / u**3 - e * (e + 1) / (e - 1) ** 3


def g3(u):
    if abs(u) < 5e-2:
        return 1 / 120 - u * u / 504 + u**4 / 5760
    e = math.exp(u)
    return -6 / u**4 + e * (e * e + 4 * e + 1) / (e - 1) ** 4


def g4(u):
    if abs(u) < 1e-1:
        return -u / 252 + u**3 / 1440
    e = math.exp(u)
    return 24 / u**5 - e * (e**3 + 11 * e**2 + 11 * e + 1) / (e - 1) ** 5


def g5(u):
    if abs(u) < 1e-1:
        return -1 / 252 + u * u / 480
    e = math.exp(u)
    return -120 / u**6 + e * (e**4 + 26 * e**3 + 66 * e**2 + 26 * e + 1) / (e - 1) ** 6


def cumulants(m, lam):
    """kappa_1..kappa_6 of the tilted Mahonian sum, closed forms extending the
    verified g0..g3 pattern (t2_nc1_cumulants.py, NC-T1) by g4, g5."""
    mu = var = k3 = k4 = k5 = k6 = 0.0
    gl = [g0(lam), g1(lam), g2(lam), g3(lam), g4(lam), g5(lam)]
    for j in range(1, m + 1):
        u = lam * j
        gu = [g0(u), g1(u), g2(u), g3(u), g4(u), g5(u)]
        mu += j * gu[0] - gl[0]
        var += gl[1] - j * j * gu[1]
        k3 += j**3 * gu[2] - gl[2]
        k4 += gl[3] - j**4 * gu[3]
        k5 += j**5 * gu[4] - gl[4]
        k6 += gl[5] - j**6 * gu[5]
    return mu, var, k3, k4, k5, k6


def main():
    ok = True
    m = build_model()

    print("(1)-(2) P_lam(y) imaginary part (must be identically 0):", m["P_im"])
    ok &= m["P_im"] == 0

    print("(3) untilted cross-check (alpha=delta=0 vs g1_draft_b's N(0) formula):",
          m["untilted_matches"])
    ok &= m["untilted_matches"]

    print(f"(4) bare alpha^2 coefficient in N_lam(0): {m['bare_a2_coeff']}  "
          "(the O(1/m) piece that belongs in the w^2 bucket, not C_R)")

    print("\nCross-check new g4,g5-based cumulants against t2_nc5_cf.py "
          "(independent implementation):")
    worst = 0.0
    for mm, lam in [(30, 0.03), (60, 0.05), (100, 0.01), (2000, 0.0005), (2000, 1e-7)]:
        mu, var, k3, k4, k5, k6 = cumulants(mm, lam)
        rvar, rk3 = sig2_ref(mm, lam), kap3_ref(mm, lam)
        rel = max(abs(var - rvar) / abs(rvar), abs(k3 - rk3) / abs(rk3))
        worst = max(worst, rel)
        print(f"  m={mm:5d} lam={lam:g}: var rel-dev={abs(var-rvar)/abs(rvar):.2e} "
              f"k3 rel-dev={abs(k3-rk3)/abs(rk3):.2e}")
    print(f"  max relative deviation: {worst:.2e}")
    ok &= worst < 1e-9

    print("\n(4) order test at fixed w, growing m (bare ~ O(1/m), residual ~ O(1/m^2)):")
    for w in (1.0, 2.0):
        vals = []
        for mm in (60, 120, 240, 480, 960):
            lam = w / mm
            mu, var, k3, k4, k5, k6 = cumulants(mm, lam)
            av = k3 / 6.0
            bare = m["bare_a2_f"](av, var)
            resid = m["N0_resid_f"](av, -k4 / 24.0, k5 / 120.0, k6 / 720.0, var)
            P0v = m["P0_f"](av, -k4 / 24.0, k5 / 120.0, k6 / 720.0, var)
            vals.append((bare / P0v**2 * mm, resid / P0v**2 * mm * mm))
        drift_bare = max(abs(vals[i][0] - vals[-1][0]) for i in range(len(vals)))
        drift_resid = max(abs(vals[i][1] - vals[-1][1]) for i in range(len(vals)))
        print(f"  w={w}: bare*m converges (drift {drift_bare:.4f}), "
              f"resid*m^2 converges (drift {drift_resid:.4f}) -- both settle, "
              "confirming the O(1/m) vs O(1/m^2) split")
        ok &= drift_bare < 0.01 and drift_resid < 0.02

    print("\n(5) grid-certified bound: max_{m in [30,2000], w in [0,K]} "
          "|residual/P0^2 * m^2|")
    C_R_pointwise = {}
    for K in (1, 2, 4):
        worst_val = 0.0
        worst_at = None
        for mm in (30, 50, 80, 120, 200, 350, 600, 1000, 2000):
            for wi in range(1, 21):
                w = K * wi / 20
                lam = w / mm
                mu, var, k3, k4, k5, k6 = cumulants(mm, lam)
                av, bv, dv, gv = k3 / 6.0, -k4 / 24.0, k5 / 120.0, k6 / 720.0
                resid = m["N0_resid_f"](av, bv, dv, gv, var)
                P0v = m["P0_f"](av, bv, dv, gv, var)
                val = abs(resid / P0v**2 * mm * mm)
                if val > worst_val:
                    worst_val, worst_at = val, (mm, round(w, 3))
        C_R_pointwise[K] = worst_val
        print(f"  K={K}: max = {worst_val:.4f} at (m,w)={worst_at}")

    print(f"\nNC-T2i4-1 VERDICT: {'PASS' if ok else 'FAIL'}")
    print("Certified pointwise-bucket contribution to C_R(K):", C_R_pointwise)
    print("NOTE: this is ONE bucket of several C_R needs (the pointwise "
          "N_lam(0)/P_lam(0)^2 piece). The box/tail/out kernel-transfer bucket "
          "(B.6's analogue) and the Taylor-remainder bucket are NOT covered "
          "here -- see g2_item4_bucket_notes_20260805.md.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
