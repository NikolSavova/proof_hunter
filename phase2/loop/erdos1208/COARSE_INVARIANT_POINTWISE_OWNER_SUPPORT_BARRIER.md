# A polynomial-height barrier to pointwise coarse-invariant support

## 1. Outcome

The canonical support gate in
`SWAP_PHYSICAL_WEDGE_DYADIC_CARLESON_GATE.md` counts coarse keys `(R,T)`,
where `R=JV+W` is the physical-wedge invariant and `T` is a three-point
parameter set.  It is tempting to prove the gate by showing that a fixed
`R` supports only `N^{o(1)}` parameter triangles.

That pointwise statement is false if one uses only the literal owner and
endpoint equations.  For every `n` there is a polynomial-height integral
distance-Sidon set with `39n` points containing `n` valid local owner
blocks, all with the same nonzero `R` and pairwise distinct noncollinear
parameter triangles.  Thus the local coarse support over one invariant can
be linear in the number of points.

This is not a counterexample to the selected optimal-core support gate:
the global energy-minimizing orientation and its dyadic core may discard
the planted blocks.  It is a sharp methodological barrier.  Any proof of
the coarse support theorem must use global orientation/core selection or
an aggregate budget across invariant fibres.  The fixed-`R` owner equations
alone cannot give a subpolynomial fibre bound.

## 2. One local block

Fix a nonzero integer vector `R`.  Choose vectors

\[
 P,V,a,b,e,q_0,q_1,q_2\in\mathbb Z^2
\]

and put

\[
 W=R-JV,qquad U=P+V,qquad Z=P+W.                 \tag{2.1}
\]

Then `(P,U,Z)` is a physical wedge with

\[
 J(U-P)+(Z-P)=JV+W=R.                             \tag{2.2}
\]

For `q` in `T={q_0,q_1,q_2}`, define the six tracks

\[
\begin{aligned}
G_0(q)&=V-a-q,\\
G_1(q)&=W-Lb+Jq+Ja,\\
G_2(q)&=W-Lb+Jq+La,\\
G_3(q)&=V-a-q+e,\\
G_4(q)&=W-b+Jq-Je,\\
G_5(q)&=W+Jq-Je.
\end{aligned}                                      \tag{2.3}
\]

For each of the eighteen vectors `G_j(q_i)`, choose a fresh base point
`B_{i,j}` and put both

\[
 B_{i,j},\qquad B_{i,j}+G_j(q_i)                 \tag{2.4}
\]

into the ambient point set.  Equations (2.1)--(2.4) put all six tracks in
the directed difference set and give exactly one literal local owner block
over the physical wedge.  One block uses three physical points and thirty-
six track-realization points.

## 3. No forced distance collision

Take `n` independent copies of the variables in Section 2, retaining the
same constant `R`.  Every constructed point is an affine-linear form in
the independent variables.  The squared distance between two constructed
points is therefore a polynomial of degree at most two.

No two unordered point pairs have the same squared-distance polynomial.
This is a finite type assertion: two candidate edges involve at most four
block indices, so it suffices to expand the construction on four formal
blocks.  There are `156` formal points and `12090` unordered edges; the
verifier checks that their `12090` quadratic coefficient dictionaries are
all different.  It also checks separately that the twenty prescribed
vectors `V,W,G_j(q_i)` in one block have distinct norm polynomials.

Consequently every forbidden equality of two distances is a nonzero
quadratic polynomial.  Add the nonzero polynomials forbidding coincident
points, degenerate parameter triangles, and equal parameter triangles
between blocks.  There are `O(n^4)` such conditions.  Choosing every scalar
variable independently from a set of size `Cn^4`, Schwartz--Zippel and the
union bound leave a specialization avoiding all of them.  All coordinates
then have size `O(n^4)`.

We obtain a distance-Sidon set `A_n` with

\[
 |A_n|=39n,qquad m=n^{O(1)},qquad
 \#\{T:\text{a local owner exists at the fixed }R\}\ge n. \tag{3.1}
\]

Since `n` is not `m^{o(1)}`, no pointwise subpolynomial theorem follows
from the local equations.

## 4. Finite certificate and scope

Run

```bash
python3 phase2/loop/erdos1208/verify_coarse_invariant_pointwise_owner_support_barrier.py
```

The verifier performs the four-block symbolic audit and constructs a
deterministic `156`-point certificate with four blocks at
`R=(17,11)`.  It checks all `12090` squared distances, all track equations,
the common invariant, and distinct noncollinear parameter triangles.

The conclusion is deliberately scoped.  It rules out pointwise/local
owner-equation proofs of the coarse support gate.  It does not show that
all four blocks survive the optimal orientation and nested-core selection,
and it does not challenge the aggregate target
`widehat X <= N^{o(1)}(k^3+m^2)`.
