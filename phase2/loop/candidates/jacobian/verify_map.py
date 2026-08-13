#!/usr/bin/env python3
"""Independent verification of the Jacobian conjecture counterexample.

Everything we might build downstream depends on this map being transcribed correctly. It reached
us through a `pdftotext`-style extraction of a blog post, and the project has already been bitten
once by trusting a paraphrase of a source instead of the source (the Part II novelty collapse on
2026-08-13). So it gets checked in exact rational arithmetic before anything is built on it.

Source: Levent Alpoge, announced 2026-07-20, found with Fable 5; digested by Terence Tao,
"A digestion of the Jacobian conjecture counterexample", 2026-07-21.

The two claims that matter:
  (1) det DF is the nonzero CONSTANT -2, so F satisfies the hypothesis of the Jacobian conjecture;
  (2) F is not injective -- three distinct points share an image -- so it violates the conclusion.

Usage: ./verify_map.py
"""
import sympy as S

x, y, z = S.symbols("x y z")

F = [
    (1 + x * y) ** 3 * z + y ** 2 * (1 + x * y) * (4 + 3 * x * y),
    y + 3 * x * (1 + x * y) ** 2 * z + 3 * x * y ** 2 * (4 + 3 * x * y),
    2 * x - 3 * x ** 2 * y - x ** 3 * z,
]
VARS = [x, y, z]
COLLIDING = [
    (S.Integer(0), S.Integer(0), S.Rational(-1, 4)),
    (S.Integer(1), S.Rational(-3, 2), S.Rational(13, 2)),
    (S.Integer(-1), S.Rational(3, 2), S.Rational(13, 2)),
]


def main():
    lines = []

    def log_(s):
        print(s, flush=True)
        lines.append(s)

    log_("Jacobian conjecture counterexample — independent verification (exact arithmetic)")

    J = S.Matrix(3, 3, lambda i, j: S.diff(F[i], VARS[j]))
    det = S.simplify(S.expand(J.det()))
    ok_det = det == -2
    log_(f"\n[1] det DF = {det}   (constant and nonzero: {ok_det})")
    log_(f"    component total degrees: {[S.Poly(f, x, y, z).total_degree() for f in F]}")

    log_("\n[2] collision:")
    images = []
    for p in COLLIDING:
        val = tuple(S.nsimplify(S.simplify(f.subs(dict(zip(VARS, p))))) for f in F)
        images.append(val)
        log_(f"    F{tuple(str(c) for c in p)} = {tuple(str(c) for c in val)}")
    ok_same = len(set(images)) == 1
    ok_distinct = len(set(COLLIDING)) == 3
    log_(f"    three DISTINCT points: {ok_distinct}; identical images: {ok_same}")

    # A constant Jacobian determinant makes F a local diffeomorphism everywhere, so the failure is
    # genuinely global injectivity, which is what the conjecture asserts.
    log_("\n[3] consequence: det DF is a nonzero constant, so F is everywhere locally invertible;")
    log_("    injectivity fails globally. Hence the Jacobian conjecture is FALSE in dimension 3,")
    log_("    and in every higher dimension by appending identity coordinates. The PLANE case")
    log_("    (n = 2) is untouched by this and remains open.")

    allok = ok_det and ok_same and ok_distinct
    log_(f"\n# OVERALL: {'MAP VERIFIED AS TRANSCRIBED' if allok else 'TRANSCRIPTION IS WRONG'}")
    import pathlib
    (pathlib.Path(__file__).resolve().parent / "out_verify_map.txt").write_text("\n".join(lines) + "\n")
    if not allok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
