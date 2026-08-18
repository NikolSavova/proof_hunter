# The transverse row--source four-cycle gate

## Summary

The surviving fourth-moment problem has a second exact graph formulation.
Put

\[
 D=A-A,\qquad B=A+JA.
\]

Distance-Sidonicity makes the coordinate map `A x A -> B` injective, so
`|B|=k^2`.  Form a bipartite graph `K_A` whose left vertices are the realized
differences `d in D` and whose right vertices are the uniquely decorated
sources `p in B`.  Join `d` to `p` when both `p` and `p+d` belong to `B` and
the corresponding relation is transverse.  Its left degrees are exactly the
row degrees `r(d)` from `TRANSVERSE_SECOND_MOMENT_GATE.md`.

If the number of four-cycles of `K_A` is at most `k^(4+o(1))`, then the
desired transverse bound follows.  This is a rigorous sufficient condition,
not a proof of it.  Exact closure data remain on the predicted fourth-power
scale.  A separate targeted construction shows why no maximum-degree version
of the statement is safe: one source already has degree
`250 = 0.828... k^(3/2)` at `k=45`.

## 1. Definition and exact edge count

Write every point of `B` uniquely as

\[
 p=v+Jy,\qquad v,y\in A.
\]

For `d in D`, join `d` to `p` if there are `u,x in A` with

\[
 p+d=u+Jx\in B,
\]

and, on putting `e=x-y`, one has

\[
 e\ne0,\qquad d\cdot e\ne0.
\]

The coordinate uniqueness of `B` makes `(u,x)` unique.  Subtracting gives

\[
 d=(u-v)+J(x-y),
\]

so the degree of the left vertex `d` is exactly

\[
 \deg_{K_A}(d)=r(d).
\]

Consequently, if

\[
 T=\sum_{d\in D}r(d),\qquad
 W=\sum_{d\in D}\binom{r(d)}2,
\]

then

\[
 e(K_A)=T,\qquad
 W=\sum_{d\in D}\binom{\deg(d)}2.                 \tag{1.1}
\]

## 2. The four-cycle implication

Let `L=|D|<k^2`, `R=|B|=k^2`, and let `Q_A` be the number of unlabelled
copies of `C_4` in `K_A`.  For two right vertices `p,q`, write `c(p,q)` for
their number of common left neighbours.  Double counting gives

\[
 W=\sum_{p<q}c(p,q),\qquad
 Q_A=\sum_{p<q}\binom{c(p,q)}2.                   \tag{2.1}
\]

Hence Cauchy--Schwarz yields

\[
 W^2
 \le \binom R2\sum_{p<q}c(p,q)^2
 =\binom R2\bigl(W+2Q_A\bigr).                  \tag{2.2}
\]

If

\[
 \boxed{Q_A\le k^{4+o(1)}},                     \tag{2.3}
\]

then (2.2), with `R=k^2`, implies `W<=k^(4+o(1))`.  By convexity on the
left degrees,

\[
 W\ge L\binom{T/L}{2}
    =\frac{T^2}{2L}-\frac T2.                    \tag{2.4}
\]

Since `L<k^2`, equations (2.3)--(2.4) give

\[
 T\le k^{3+o(1)}.
\]

Thus (2.3) is a sufficient averaged theorem for the wide branch of the
rotated-support argument.  It is stronger than merely bounding `W`, but it
has the advantage that it is a standard supersaturation target on a graph
whose two vertex classes both have exactly the critical `Theta(k^2)` size.

## 3. Exact stress data

For prefixes of the certified heavy-row closure, the exact row--source
four-cycle counts are

| `k` | `Q_A` | `Q_A/k^4` |
|---:|---:|---:|
| 16 | 3,349 | 0.0511 |
| 20 | 33,067 | 0.2067 |
| 30 | 716,180 | 0.8842 |
| 40 | 4,284,047 | 1.6735 |
| 50 | 12,210,794 | 1.9537 |
| 60 | 29,370,111 | 2.2662 |

At `k=60`, about `89.4%` of these four-cycles use two row edges whose
underlying edges of `A` are endpoint-disjoint.  The hard term is therefore
not an endpoint-overlap degeneracy.

The same warning appears on the right degrees.  Starting from the common
16-point seed and fixing

\[
 p=(46,1)+J(24,29),
\]

a deterministic relation-closure search produces an exact 45-point
distance-Sidon set with

\[
 \deg_{K_A}(p)=250=0.82817\ldots k^{3/2}.         \tag{3.1}
\]

Thus a pointwise `k^(1+o(1))` source-degree theorem is unsafe, just like the
previous row and colour maximum theorems.  The four-cycle total, rather than
a maximum codegree or maximum degree, is the correct formulation.

## 4. Translation-slice form of the same obstruction

There is a useful exact disintegration of `W`.  For a row pair write

\[
 e_1=e+q,\qquad e_2=e,
\]

and hence

\[
 f_1=f-Jq,\qquad f_2=f,
\]

where the common row is `d=f+Je`.  Choosing one representative from every
pair `{q,-q}`, one obtains

\[
 W=\sum_{q/\{\pm1\}} W_q,                        \tag{4.1}
\]

where `W_q` counts the triples `(q,e,f)` satisfying

\[
 e,e+q,f,f-Jq,f+Je\in D                         \tag{4.2}
\]

together with the two transverse indicators.  Dropping the fifth incidence
in (4.2) gives

\[
 W_q\le R_D(q)R_D(Jq),                           \tag{4.3}
\]

and summing (4.3) is exactly the unrestricted mixed energy already known to
have size `k^5`.  The fifth incidence is therefore still load-bearing.

At `k=60`, there are `187,055` active sign-classes of `q`, the largest slice
has size `3,322`, and their total is

\[
 W=12,442,796.
\]

Thus there are `Theta(k^3)` active translations with only `Theta(k)` mass on
average.  A viable proof may establish (2.3) by a switching or charging map
across these translation slices.  Pointwise bounds on a single slice are not
supported by the data.

## 5. Extension of the strongest adversary

Two further deterministic closure steps preserve exact distance-Sidonicity.
Appending

```text
(799,435), (472,-756)
```

to the certified 120-point chain gives, at `k=122`,

\[
\begin{aligned}
 |D|&=14763,\\
 T&=2925748,\\
 \max r&=971,\\
 \sum_d r(d)^2&=770269576,\\
 W&=383671914.
\end{aligned}
\]

The normalized global ratio is

\[
 \frac{W}{kT}=1.074888\ldots,
\]

slightly below its value at `k=120`.  Meanwhile the fixed heavy row continues
on the square-root-heavy scale.  This is finite evidence only, but it sharply
separates the surviving global conjecture `W=O(kT)` from every failed local
strengthening.

`verify_transverse_row_source_c4.py` checks the 45-point source certificate,
the row--source four-cycle table through `k=40`, and, with `--extended`, the
122-point global profile.  All checks use exact integer arithmetic.

## 6. Remaining theorem

Either of the estimates

\[
 W\le k^{4+o(1)},\qquad Q_A\le k^{4+o(1)}
\]

closes the transverse collision gate.  The second is a clean graph
supersaturation formulation; neither is proved.  The exact data now rule out
proofs based on bounded endpoint overlap, bounded source degree, bounded row
degree, or a pointwise translation slice.  A proof has to charge the generic,
endpoint-disjoint four-cycles globally.
