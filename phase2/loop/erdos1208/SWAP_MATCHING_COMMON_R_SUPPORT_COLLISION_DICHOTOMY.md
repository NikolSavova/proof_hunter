# The matching common-`r` support/collision dichotomy

## 1. Outcome

The matching swap-cell four-cycle gate has an exact second localization.
Fix two opposite cells and one common matching neighbour.  After choosing
one parallel copy on each of the two incident edges, the extension carries a
single difference `r`.  That `r` simultaneously gives three correlated
members of `D-D`:

\[
 \boxed{r,\qquad r+d,\qquad J(r+Ld)\in D-D,}       \tag{1.1}
\]

where `d` is the displacement between the two opposite cells and
`L=I+J`.  If two common neighbours carry the same `r`, their four selected
edge copies give a five-direction affine collision with every popularity
condition and every endpoint cell retained.

This gives a lossless fork for the common-neighbour factor:

* many distinct `r` labels force a large set of correlated triples (1.1);
* repeated `r` labels force many decorated matching four-cycles of one
  exact affine type.

It is a direct narrowing of the cube-root problem, not yet its proof.  The
remaining theorem must globally pack these two outputs at the `K=|D-D|/|D|`
scale.  A pointwise fixed-cell divisor bound is already too optimistic:
genuine Costas stresses have five common neighbours in one fixed
opposite-pair/`r` cell and sixteen centres after only `(z,d,r)` is fixed.

## 2. One common-neighbour extension

Write a cell in component `z` as

\[
 C_z(b)=(b,z+Lb),\qquad b,z+Lb\in D.              \tag{2.1}
\]

Fix opposite cells `B=C_z(b)` and `C=C_z(c)`, and put

\[
 d=c-b.                                           \tag{2.2}
\]

Let `U=C_z(u)` be a common matching neighbour.  Choose an ordinary sum
`s_B` on the edge `BU` and an ordinary sum `s_C` on the edge `CU`.  The
corresponding bases are

\[
 a_B=J(s_B-z-Lb-Lu),\qquad
 a_C=J(s_C-z-Lc-Lu).                              \tag{2.3}
\]

Put `r=s_B-s_C`.  The exact seven-role edge normal form shows that all six
vectors in the following three pairs lie in `D`:

\[
 (s_B-u,s_C-u),\quad
 (s_B-b,s_C-c),\quad
 (a_B,a_C).                                       \tag{2.4}
\]

Their differences are precisely

\[
\begin{aligned}
 (s_B-u)-(s_C-u)&=r,\\
 (s_B-b)-(s_C-c)&=r+d,\\
 a_B-a_C&=J(r+Ld).
\end{aligned}                                    \tag{2.5}
\]

This proves (1.1).  Notice what has not been discarded: both selected edge
copies still carry their two adaptive-popular shifts and all seven `D`
members.  Formula (2.5) is therefore stronger than merely asking that three
unlabelled vectors belong to `D-D`.

For a fixed centre `U`, let `R_U` be the set of all `r` obtained by varying
the two selected parallel copies.  It is nonempty and satisfies

\[
 1\le |R_U|\le m(B,U)m(C,U)\le \mu_z^2.           \tag{2.6}
\]

## 3. Exact support-versus-collision inequality

For every common centre choose one `r_U in R_U`; the selector may be
arbitrary.  Let

\[
 n=|N(B)\cap N(C)|,\qquad
 X=|\{r_U:U\in N(B)\cap N(C)\}|,                 \tag{3.1}
\]

and let

\[
 Q=\#\{\{U,V\}:U\ne V,\ r_U=r_V\}.              \tag{3.2}
\]

If `n_r` is the selected load of `r`, then

\[
 \sum_r n_r=n,\qquad
 \sum_r n_r^2=n+2Q.                              \tag{3.3}
\]

Cauchy gives the exact dichotomy inequality

\[
 \boxed{n^2\le X(n+2Q).}                         \tag{3.4}
\]

In particular either `n<=2X`, or

\[
 Q\ge {n^2\over4X}.                              \tag{3.5}
\]

Thus large common-neighbour codegree cannot remain an unstructured graph
parameter.  It must appear either as distinct correlated triples (2.5), or
as a large repeated-`r` four-cycle family.

Using all sets `R_U` instead of a selector gives the related lossless
identity

\[
 I^2\le |\cup_U R_U|\left(I+2\sum_{U<V}|R_U\cap R_V|\right),
 \qquad I=\sum_U|R_U|.                            \tag{3.6}
\]

The selector form (3.4) is cleaner because it introduces no parallel-copy
loss.

## 4. The repeated-`r` five-direction collision

Let `U=C_z(u)` and `V=C_z(v)` be two common neighbours of `B,C`.  Suppose
the selected sums satisfy

\[
 s_{BU}-s_{CU}=s_{BV}-s_{CV}=r.                  \tag{4.1}
\]

Put

\[
 \delta=v-u,\qquad h=s_{BV}-s_{BU}.
\]

Equation (4.1) also gives `h=s_CV-s_CU`.  Comparing the four complete edge
records produces the five displacements

\[
 \boxed{
 \delta,\quad L\delta,\quad h,\quad h-\delta,
 \quad \eta:=J(h-L\delta).}                     \tag{4.2}
\]

More precisely:

* `delta` occurs between the two centre first-coordinates;
* `L delta` occurs between their second cell coordinates;
* `h` occurs on both opposite-cell target roles;
* `h-delta` occurs on both centre target roles; and
* `eta` occurs on both base roles.

All source and target labels in these comparisons lie in `D`.  Hence the
last three displacements in (4.2) have two labelled `D-D` representations,
while the first two retain the affine component relation.  In the
sixteen-physical-endpoint branch, the cell representations of `delta` and
`L delta` use disjoint endpoints.  This is the exact collision system to
attack; deleting its duplicated roles or the four popularity pairs returns
to generic affine plantings.

## 5. Stress and equality-model separation

The fixed-cell profiles in the exact optimal matching cores are:

| family | max opposite/`r` centre load | max `(z,d,r)` centre load | max opposite `r` support |
|---|---:|---:|---:|
| Costas 17 | 1 | 1 | 6 |
| Costas 23 | 4 | 6 | 25 |
| Costas 29 | 5 | 10 | 30 |
| Costas 31 | 5 | 11 | 23 |
| Costas 37 | 5 | 16 | 27 |

On Costas 23, 828 of 1492 matching four-cycles admit no common `r` on
either diagonal.  Among the 76 fully sixteen-endpoint cycles, 50 have no
common `r`.  On Costas 37 the corresponding figures are

\[
 {29811\over63119}=47.23\%\quad\text{and}\quad
 {8004\over16786}=47.68\%.                        \tag{5.1}
\]

So neither side of the dichotomy is negligible: a proof must pay both.

The important positive separation is the lifted modular parabola, the
known `m^2`-sharp ambient equality model.  For primes `17,23,31,43`, the
adaptive popular set has exactly eight shifts.  The largest rich-fibre
sizes are `2,3,3,3`; the largest matching component sizes are `0,2,3,3`;
and there are no matching four-cycles.  This does not prove an asymptotic
theorem for the family, but it shows that the present matching gate is not
merely repackaging the dominant ambient countermodel that killed several
earlier energy estimates.

## 6. The next direct theorem

The matching branch still follows from

\[
 \mu_z^2r_zh_z\le K^2N^{o(1)}.                   \tag{6.1}
\]

Equations (2.5)--(4.2) identify the two concrete estimates that should now
replace a raw graph-codegree attack:

1. **Distinct-support packing.**  Bound, globally and with component size
   retained, selected triples
   `(r,r+d,J(r+Ld))` coming from the complete extensions (2.3)--(2.6).
2. **Repeated-`r` packing.**  Bound the fully decorated five-direction
   collisions (4.2), routing endpoint-contact cycles separately and keeping
   the four adaptive-popular shift pairs in the clean branch.

A useful theorem must combine these two counts before dropping endpoint
labels.  Independent pointwise bounds on component size, parallel
multiplicity, fixed-`r` load, or raw `D-D` representation count are not
supported by the current barriers.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_matching_common_r_support_collision.py
python3 phase2/loop/erdos1208/verify_swap_matching_common_r_support_collision.py --larger
```

The default verifier proves the identities in Sections 2 and 4, exhausts
(3.4) for every assignment through six centres and four labels, reproduces
the Costas-17/23 common-extension data, and checks the lifted-parabola rows
through prime 43.  The optional larger run reproduces all Costas-37 numbers
in (5.1).  The optimal-core analyzer independently checks (2.5) on every
common-neighbour extension it enumerates.
