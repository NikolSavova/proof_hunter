"""NC-W1: symbolic derivation + verification of the 6-term tilted model polynomial
P_lam(y) in SCALED variables, the N_lam(0) = -36 a^2 + residual split, and the
derivative formulas the Taylor bucket (wp2b_nc3) consumes.

Steps:
 (1) Build phihat_lam(t) = e^{-s2 t^2/2} exp(-i alpha t^3 - beta t^4 + i delta t^5
     - gamma t^6) truncated to O(t^8); Fourier-transform term-by-term via
     (1/2pi) int t^n e^{-s2 t^2/2} e^{-itx} dt = (-i)^n s2^{-n/2} Z(y) He_n(y).
     CHECK: Im P == 0 symbolically.
 (2) Substitute alpha = a s2^{3/2}, beta = b s2^2, delta = d s2^{5/2},
     gamma = g s2^3. CHECK: all s2 powers cancel; the result equals
     P = 1 + a He3 - b He4 + d He5 + (g+a^2/2) He6 - a b He7 + (b^2/2+a d) He8
     (the closed form hardcoded in wp2b_lib.P_coeffs).
 (3) Untilted limit a=d=0: P = 1 - b He4 + g He6 + (b^2/2) He8  (= g1_draft_b's P).
 (4) N(y) := -P''P + P'^2 - 12 b He2 P^2 (pure polynomial in a,b,d,g,y — no s2).
     At y=0: CHECK bare alpha^2 term coefficient is exactly -36; untilted limit
     of N(0) reproduces -90 g + 384 b^2 at weight 2 (weights: a:1, b:2, d:3, g:4
     in half-powers of 1/m, i.e. a ~ m^{-1/2}, b ~ m^{-1}, d ~ m^{-3/2}, g ~ m^{-2}).
     CHECK: every residual monomial has weight >= 4 half-powers (i.e. O(1/m^2)).
     PRINT the full residual monomial table (consumed by nc4's closed-form bound).
 (5) CHECK the He-shift derivative formulas (P^(r) = sum c_n n!/(n-r)! He_{n-r})
     against sympy diff, r = 1..4, and the lib's numeric P_eval at random points.
 (6) CHECK the quotient-rule bound form for (log P)'''' used by nc3:
     |L''''| <= p4/Pm + 4 p3 p1/Pm^2 + 3 p2^2/Pm^2 + 12 p2 p1^2/Pm^3 + 6 p1^4/Pm^4
     via the exact identity L'''' = P''''/P - (4 P''' P' + 3 P''^2)/P^2
     + 12 P'' P'^2/P^3 - 6 P'^4/P^4 (sympy-verified), then numerically:
     |L''''(y*)| <= bound at random scaled points.

Run: python3 wp2b_nc1_model_poly.py
"""
import os
import random
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wp2b_lib as lib


def main():
    ok = True
    y, t = sp.symbols("y t", real=True)
    a, b, d, g = sp.symbols("a b d g", real=True)
    s2 = sp.symbols("s2", positive=True)
    alpha, beta, delta, gamma = a * s2 ** sp.Rational(3, 2), b * s2**2, \
        d * s2 ** sp.Rational(5, 2), g * s2**3

    He = lambda n: sp.expand(2 ** sp.Rational(-n, 2) * sp.hermite(n, y / sp.sqrt(2)))

    # (1) model, truncated to O(t^8), Fourier rule
    E = -sp.I * alpha * t**3 - beta * t**4 + sp.I * delta * t**5 - gamma * t**6
    ser = sp.expand(sp.series(sp.exp(E), t, 0, 9).removeO())
    P = sp.Integer(0)
    for n in range(0, 9):
        cn = ser.coeff(t, n)
        if cn != 0:
            P += cn * (-sp.I) ** n * s2 ** (sp.Rational(-n, 2)) * He(n)
    Pim = sp.simplify(sp.im(P))
    P = sp.expand(sp.re(P))
    print("(1) Im P == 0 :", Pim == 0)
    ok &= Pim == 0

    # (2) s2 cancels; closed form matches lib.P_coeffs
    print("(2) P free of s2 :", s2 not in P.free_symbols)
    ok &= s2 not in P.free_symbols
    P_closed = (1 + a * He(3) - b * He(4) + d * He(5) + (g + a**2 / 2) * He(6)
                - a * b * He(7) + (b**2 / 2 + a * d) * He(8))
    diff_closed = sp.expand(P - P_closed)
    print("(2) P == 1 + a He3 - b He4 + d He5 + (g+a^2/2) He6 - ab He7 "
          "+ (b^2/2+ad) He8 :", diff_closed == 0)
    ok &= diff_closed == 0

    # (3) untilted limit
    P_unt = sp.expand(P.subs({a: 0, d: 0}))
    P_b8 = sp.expand(1 - b * He(4) + g * He(6) + sp.Rational(1, 2) * b**2 * He(8))
    print("(3) untilted limit == g1_draft_b P :", sp.expand(P_unt - P_b8) == 0)
    ok &= sp.expand(P_unt - P_b8) == 0

    # (4) N(y), split at y=0
    Pp, Ppp = sp.diff(P, y), sp.diff(P, y, 2)
    N = sp.expand(-Ppp * P + Pp**2 - 12 * b * He(2) * P**2)
    N0 = sp.expand(N.subs(y, 0))
    N0p = sp.Poly(N0, a, b, d, g)
    bare = N0p.coeff_monomial(a**2)
    print("(4) coefficient of bare a^2 in N(0):", bare, " (must be -36)")
    ok &= bare == -36
    resid = sp.expand(N0 + 36 * a**2)
    residp = sp.Poly(resid, a, b, d, g)
    wt = lambda mono: mono[0] * 1 + mono[1] * 2 + mono[2] * 3 + mono[3] * 4
    rows = sorted(zip(residp.monoms(), residp.coeffs()), key=lambda z: (wt(z[0]), z[0]))
    print("    N(0) residual monomials  [half-power weight | monomial | coeff]:")
    minw = min(wt(mo) for mo, _ in rows)
    for mo, co in rows:
        mono_str = "*".join(f"{v}^{e}" for v, e in zip("abdg", mo) if e) or "1"
        print(f"      w={wt(mo):2d}  {mono_str:<12s} {co}")
    print("    min weight =", minw, "(need >= 4, i.e. O(1/m^2)) :", minw >= 4)
    ok &= minw >= 4
    unt = sp.expand(resid.subs({a: 0, d: 0}))
    lead = sp.expand(unt - (-90 * g + 384 * b**2))
    lead_p = sp.Poly(lead, b, g)
    lead_hi = all(mo[0] * 2 + mo[1] * 4 >= 6 for mo in lead_p.monoms())
    print("    untilted residual = -90 g + 384 b^2 + (weight>=6 terms) :", lead_hi)
    ok &= lead_hi

    # machine-readable residual table for nc4
    tbl = [(list(mo), str(co)) for mo, co in rows]
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wp2b_n0_resid_table.py")
    with open(out, "w") as f:
        f.write("# generated by wp2b_nc1_model_poly.py -- N(0) residual monomials\n")
        f.write("# rows: ((ea, eb, ed, eg), integer coefficient as string)\n")
        f.write("RESID = %r\n" % (tbl,))
    print("    table written ->", os.path.basename(out))

    # (5) derivative formulas + lib numeric agreement
    coeffs = {0: sp.Integer(1), 3: a, 4: -b, 5: d, 6: g + a**2 / 2, 7: -a * b,
              8: b**2 / 2 + a * d}
    all_ok = True
    for r in range(1, 5):
        Pr = sp.diff(P, y, r)
        Pr_formula = sp.expand(sum(
            c * sp.ff(n, r) * He(n - r) for n, c in coeffs.items() if n >= r))
        all_ok &= sp.expand(Pr - Pr_formula) == 0
    print("(5) He-shift derivative formulas r=1..4 :", all_ok)
    ok &= all_ok
    rng = random.Random(7)
    fP = [sp.lambdify((a, b, d, g, y), sp.diff(P, y, r), "math") for r in range(5)]
    worst = 0.0
    for _ in range(200):
        av, bv, dv, gv = (rng.uniform(-0.3, 0.3) for _ in range(4))
        yv = rng.uniform(-0.5, 0.5)
        for r in range(5):
            v1 = fP[r](av, bv, dv, gv, yv)
            v2 = lib.P_eval(av, bv, dv, gv, yv, r)
            worst = max(worst, abs(v1 - v2) / max(1.0, abs(v1)))
    print(f"    lib.P_eval vs sympy, r=0..4, 200 random pts: max rel dev = {worst:.2e}")
    ok &= worst < 1e-12

    # N0/P0 numeric split agreement with lib
    worst2 = 0.0
    fN0 = sp.lambdify((a, b, d, g), resid, "math")
    fP0 = sp.lambdify((a, b, d, g), P.subs(y, 0), "math")
    for _ in range(200):
        av, bv, dv, gv = (rng.uniform(-0.2, 0.2) for _ in range(4))
        r1, q1 = lib.N0_resid_and_P0(av, bv, dv, gv)
        worst2 = max(worst2, abs(r1 - fN0(av, bv, dv, gv)),
                     abs(q1 - fP0(av, bv, dv, gv)))
    print(f"    lib.N0_resid_and_P0 vs sympy: max abs dev = {worst2:.2e}")
    ok &= worst2 < 1e-12

    # (6) L'''' identity + quotient-rule bound
    L4 = sp.diff(sp.log(P), y, 4)
    ident = (sp.diff(P, y, 4) / P - (4 * sp.diff(P, y, 3) * sp.diff(P, y)
             + 3 * sp.diff(P, y, 2) ** 2) / P**2
             + 12 * sp.diff(P, y, 2) * sp.diff(P, y) ** 2 / P**3
             - 6 * sp.diff(P, y) ** 4 / P**4)
    print("(6) L'''' quotient identity :", sp.simplify(sp.together(L4 - ident)) == 0)
    ok &= sp.simplify(sp.together(L4 - ident)) == 0
    fL4 = sp.lambdify((a, b, d, g, y), L4, "math")
    worst3 = 0.0
    for _ in range(300):
        av, bv, dv, gv = (rng.uniform(-0.15, 0.15) for _ in range(4))
        yv = rng.uniform(-0.1, 0.1)
        ps = [max(abs(lib.P_eval(av, bv, dv, gv, s * 0.1, r))
                  for s in (-1.0, -0.5, 0.0, 0.5, 1.0)) for r in range(5)]
        Pm = min(lib.P_eval(av, bv, dv, gv, s * 0.1)
                 for s in (-1.0, -0.5, 0.0, 0.5, 1.0))
        if Pm <= 0.4:
            continue
        bound = (ps[4] / Pm + 4 * ps[3] * ps[1] / Pm**2 + 3 * ps[2] ** 2 / Pm**2
                 + 12 * ps[2] * ps[1] ** 2 / Pm**3 + 6 * ps[1] ** 4 / Pm**4)
        val = abs(fL4(av, bv, dv, gv, yv))
        worst3 = max(worst3, val / bound)
    print(f"    |L''''| vs quotient-rule bound, 300 random pts: max ratio = {worst3:.3f}")
    ok &= worst3 <= 1.0

    print("\nNC-W1 VERDICT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
