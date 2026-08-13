# Emergency audit of the nested epsilon failure

**Date:** 2026-08-13
**Verdict:** **NOT A PROOF FAILURE.** The original independent test reused
\(\varepsilon=1/97\) at two geometrically different scales. That value is
valid for every internal glue used to construct the six-point
\(T_{4,2}\), but is not below the threshold for the outer 36-point
composition. Choosing the outer parameter afresh, as the paper's lemma
requires, realizes every prescribed orientation and gives exactly
\[
(C,U,W)=(14136,14136,441399).
\]

## Exact findings

The strengthened independent checker uses exact rational arithmetic and
audits coordinate order, zero determinants, and every one of the four
composition orientation rules.

For the recursive template, internal \(\varepsilon=1/97\) passes at every
nontrivial glue:

| Cell | Child sizes | coordinate order | zero determinants | mixed-sign mismatches |
|---|---:|---:|---:|---:|
| \(T_{2,1}\) | \(1+1\) | yes | 0 | 0 |
| \(T_{3,1}\) | \(1+2\) | yes | 0 | 0 |
| \(T_{3,2}\) | \(2+1\) | yes | 0 | 0 |
| \(T_{4,2}\) | \(3+3\) | yes | 0 | 0 |

Thus the six-point template itself is a valid strong Pascal cell. Its direct
statistics remain
\[
C=U=31,\qquad W=50,
\]
with cap and cup size vectors \(6,15,10\), as required.

For the outer composition \(T_{4,2}[T_{4,2}]\), the exact search gives:

| Outer epsilon | coordinate order | zero determinants | orientation-rule mismatches |
|---|---:|---:|---:|
| \(1/97\) | no | 412 | 1491 |
| \(1/1000\) | no | 0 | 684 |
| \(1/5000\) | no | 0 | 684 |
| \(1/9000\) | no | 0 | 684 |
| \(1/9500\) | no | 0 | 152 |
| \(1/9750\) | yes | 0 | 0 |
| \(1/10000\) | yes | 0 | 0 |
| \(1/16384\) | yes | 0 | 0 |

This also exposes why checking only general position is inadequate:
\(\varepsilon=1/1000\), for example, has no zero determinant but does not
have separated block order and has 684 wrong limiting signs.

At the first successful tested value, outer \(\varepsilon=1/9750\), the
direct endpoint dynamic program returns
\[
(C,U,W)=(14136,14136,441399),
\]
exactly matching all three substitution formulas.

## Why the paper's reasoning remains valid

Lemma 2.1 says “for all sufficiently small positive \(\varepsilon\),” not
that one numerical epsilon works at every recursive depth.

For fixed finite \(S,Q\):

1. A within-block determinant is multiplied by the positive factor
   \(\varepsilon^3\), so its sign is preserved for every positive
   \(\varepsilon\).
2. A three-block determinant converges to the corresponding nonzero
   determinant of \(S\); finitely many such signs therefore stabilize below
   a positive threshold.
3. For two points in one block, the leading mixed determinant term is
   \(-\varepsilon\Delta y\,\Delta X\) when the third point is later, and its
   reflection is positive when the first point is earlier. The shear makes
   \(\Delta y,\Delta X>0\), so these signs stabilize.
4. The finitely many positive coordinate gaps of the macro configuration
   also persist below a positive threshold.

Taking the minimum of these finitely many thresholds produces a nonempty
interval \(0<\varepsilon<\varepsilon_0(S,Q)\). At the next recursive level,
the input coordinates have much smaller feature gaps, so
\(\varepsilon_0\) can be much smaller. The construction explicitly permits
choosing a new rational epsilon at every level. The enumeration depends only
on the stabilized orientation rules, not on a uniform numeric parameter.

Therefore the failed reuse of \(1/97\) tests a claim the paper does not make.

## Artifact change

The file independent_check.py now:

- audits every internal Pascal glue at the template scale;
- searches several exact rational outer scales;
- rejects a scale unless both coordinate orders are strict, all determinants
  are nonzero, and every labelled triple has its prescribed orientation;
- uses the first successful tested scale for the independent direct count.

This is stronger than merely changing the outer epsilon to a smaller hard
coded value: it certifies the actual hypothesis needed by the substitution
formulas.
