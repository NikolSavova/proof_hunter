# Spectral and unrestricted-energy audit of the transverse gate

## Summary

Let `A` be a distance-Sidon set of size `k`, put `D=A-A`, and let `J` be a
quarter-turn.  The transverse row--colour matrix is

\[
 \mathcal B(d,e)=
 1_D(d-Je)1_{e\ne0}1_{d\cdot e\ne0},\qquad d,e\in D.
\]

Two natural strengthenings of the fourth-moment gate were tested.  Neither is
a safe proof target.

1. The operator estimate `||B||<=k^(1+o(1))` would imply the desired row
   moment, but the finite data do not support a stable bounded normalization.
2. The stronger Schur estimate saying that every row has only
   `k^(2+o(1))` two-step mass is strongly threatened: on the certified
   heavy-row chain the fixed heavy row grows on the `k^(5/2)` scale.
3. Dropping the restriction that the common sum lies in `D` produces the
   familiar mixed energy `E^+(D,JD)`, but that relaxation grows on the
   `k^5` scale on the same chain.

The load-bearing object is therefore the *restricted* fourth moment already
recorded in `TRANSVERSE_SECOND_MOMENT_GATE.md`.  Spectral or Fourier language
does not remove its final `1_D` constraint.

These are exact reductions and exact finite falsification data, except for
the displayed singular values, which are numerical diagnostics.  They are
not an asymptotic counterexample to either spectral statement.

## 1. Spectral sufficient condition

Let `r=B1` be the row-degree vector.  Since `|D|<k^2`,

\[
 M_{\rm row}=\|\mathcal B\mathbf1\|_2^2
 \le \|\mathcal B\|_{\rm op}^2|D|.
\]

Hence

\[
 \|\mathcal B\|_{\rm op}\le k^{1+o(1)}
 \quad\Longrightarrow\quad
 M_{\rm row}\le k^{4+o(1)}.
\]

Power iteration on the exact matrices of the heavy-row prefixes gives the
following approximate singular values.

| `k` | `||B||_op` | `||B||_op/k` |
|---:|---:|---:|
| 60 | 101.339 | 1.689 |
| 80 | 148.318 | 1.854 |
| 100 | 208.473 | 2.085 |
| 120 | 272.147 | 2.268 |

The estimate may still hold with a subpolynomial factor, but these data do
not justify treating it as easier than the moment theorem itself.

## 2. The two-step Schur strengthening is unsafe

Schur's test gives

\[
 \|\mathcal B\|_{\rm op}^2
 \le \|\mathcal B\mathcal B^T\|_\infty
 =\max_d\sum_{e:\mathcal B(d,e)=1}c(e),
\]

where `c(e)` is the column degree.  Thus the pointwise estimate

\[
 \sum_{e:\mathcal B(d,e)=1}c(e)\le k^{2+o(1)}       \tag{2.1}
\]

would imply the spectral gate.  It is much too optimistic on the targeted
closure chain.  For its fixed heavy row `d=(0,-1)`, the exact values are:

| `k` | row degree | two-step mass | mass / `k^2` | mass / `k^(5/2)` |
|---:|---:|---:|---:|---:|
| 60 | 339 | 36,740 | 10.206 | 1.318 |
| 70 | 422 | 57,028 | 11.638 | 1.391 |
| 80 | 514 | 81,504 | 12.735 | 1.424 |
| 90 | 614 | 114,692 | 14.160 | 1.493 |
| 100 | 719 | 161,478 | 16.148 | 1.615 |
| 110 | 830 | 213,652 | 17.657 | 1.684 |
| 120 | 948 | 276,604 | 19.209 | 1.753 |

At `k=120` this is the maximum row two-step mass; the maximum column
two-step mass is `160,976=11.179...k^2`.  The normalization in the last
column is slowly increasing and is far more stable than the `k^2`
normalization.  This strongly threatens (2.1), although a finite chain is not
an asymptotic disproof.

The useful lesson is that heavy rows can preferentially meet heavy columns.
The fourth-power *average* moment survives, but no local two-step bound should
be assumed.

## 3. Exact restricted-energy identity

First remove only the transverse indicators and put

\[
 \mathcal B_0(d,e)=1_D(d-Je),\qquad d,e\in D.
\]

Writing `e_1=e+q`, `e_2=e`, `f_2=f`, and using

\[
 f_1+Je_1=f_2+Je_2
 \quad\Longleftrightarrow\quad
 f_1=f-Jq,
\]

gives the exact identity

\[
 \sum_{d\in D}\Big(\sum_{e\in D}1_D(d-Je)\Big)^2
 =\sum_{q,e,f}
 1_D(e)1_D(e+q)1_D(f)1_D(f-Jq)1_D(f+Je).       \tag{3.1}
\]

The transverse row moment is at most (3.1).  Formula (3.1) is the cleanest
algebraic form of the live gate: it is a perpendicular correlation of two
difference fibres, with the common sum forced back into the complete
difference set `D`.

## 4. Why ordinary mixed energy is too large

If the final factor `1_D(f+Je)` is deleted from (3.1), the remaining sum
factorizes.  With

\[
 R_D(q)=|\{(x,y)\in D^2:x-y=q\}|,
\]

the relaxation is

\[
 E^+(D,JD)=\sum_qR_D(q)R_D(Jq).                 \tag{4.1}
\]

It is an upper bound for (3.1), but it loses an entire power.  Exact values on
the heavy-row chain are:

| `k` | `E^+(D,JD)` | energy / `k^4` |
|---:|---:|---:|
| 20 | 1,735,609 | 10.848 |
| 30 | 16,135,769 | 19.921 |
| 40 | 76,060,041 | 29.711 |
| 50 | 231,533,961 | 37.045 |
| 60 | 581,578,857 | 44.875 |
| 70 | 1,344,282,105 | 55.988 |

The ratio is consistent with `Theta(k^5)`, not `k^(4+o(1))`.  Consequently
Fourier, BSG, or higher-energy arguments that first discard the last factor
in (3.1) cannot close the transverse gate.  Any proof has to exploit that the
common sum is itself the uniquely realized difference of two points of `A`.

`verify_transverse_spectral_audit.py` reproduces the exact two-step and mixed
energy tables.  The singular-value table is deliberately not part of the
exact certificate.

## 5. Surviving target

The current theorem to prove remains

\[
 \sum_{d\in D}r(d)^2\le k^{4+o(1)},
\]

equivalently the decorated-parallelogram estimate in
`TRANSVERSE_PARALLELOGRAM_GATE.md`.  The audit above narrows the acceptable
proof mechanisms:

* average/tail charging is still viable;
* a pointwise local maximum or pointwise two-step estimate is not;
* unrestricted additive energy is too coarse by one power;
* the fifth incidence in (3.1), or the unique `A x A` decoration of
  `A+JA`, must be used essentially.
