# Low-mean minimizers force a weighted family of rooted circuit stars

**Date:** 2026-08-14.  All logarithms are base two and the empty face is
included.

## Verdict

The unweighted conclusion in
`MINIMIZER_CIRCUIT_CODEGREE_DICHOTOMY.md` is not yet sharp enough: the
certified nine-point global minimizer already has a triple of the maximum
possible circuit degree `n-3`.  It is its outer-hull triangle.  Thus a dense
triple star does **not** force a `V`-decreasing mutation.

This note proves the correct weighted refinement.  Let `R` be maximum face
rank, `mu` the uniform mean rank, and use the canonical `O(h^2)` tangent
triple family `mathcal T(A)` for every face `A`.  Define

\[
 d(T)=|\{p:T\cup\{p\}\text{ is nonconvex}\}|,
 \qquad
 w(T)=|\{A:T\in\mathcal T(A)\}|.                   \tag{1}
\]

If `mu<n/2`, put

\[
 D_0={n-2\mu\over(R-2)\mu},
 \qquad
 \mathcal H=\{T:d(T)\ge D_0/2\}.                   \tag{2}
\]

Then

\[
 \boxed{\sum_{T\in\mathcal H}w(T)
       \ge {V(n-2\mu)\over2(n-3)}}                 \tag{3}
\]

and at least

\[
 \boxed{{V(n-2\mu)\over2(n-3)R(R-2)}}             \tag{4}
\]

distinct faces contain a canonical triple in `mathcal H`.

For a low-mean minimizer, `R<=(1/2+o(1))(log n)^2`.  Thus (4) gives a
`1/O((log n)^4)` fraction of **all** faces, and every selected face contains
a canonical triple with

\[
 d(T)\ge\left({1\over1-\epsilon}-o(1)\right)
                 {n\over(\log n)^3}                \tag{5}
\]

when `mu<=(1-epsilon)log n`.  Pigeonholing the interior role gives a rooted
pocket of at least one quarter this size, disjoint from the face.

This is strictly sharper than extracting one arbitrary dense triangle.  An
exceptional triangle occurring in only `o(V)` canonical face contexts cannot
by itself supply the linear weighted demand in (3).  The remaining obstruction
is a polylogarithmically dense **family of face-attached pockets**, possibly
spread across many roots.  Converting its unrestricted pocket faces into a
global product bank is still open.

## 1. Weighted tangent incidence

For completeness, recall the two exact facts used here.  For a uniformly
random convex face `A`, let `H=|A|`, let `u(A)` be its number of one-point
extensions, and put

\[
                         b(A)=n-H-u(A).                    \tag{6}
\]

Cover balance gives `E u=mu`, hence

\[
                         \mathbb E b(A)=n-2\mu.            \tag{7}
\]

If the vertices of an `h`-face are `v_0,...,v_(h-1)` in cyclic order, take

\[
 \mathcal T(A)=
 \{\{v_i,v_{i+1},v_j\}:j\notin\{i,i+1\}\}.        \tag{8}
\]

After repeated unordered triples are removed,

\[
                         |\mathcal T(A)|\le h(h-2).         \tag{9}
\]

Every non-addable interior label is witnessed by a fan triangle in (8).
Every blocked exterior label is witnessed by the tangent endpoint, its
first hidden neighbor, and the opposite tangent endpoint.  Consequently

\[
                b(A)\le\sum_{T\in\mathcal T(A)}d(T).       \tag{10}
\]

Summing (9)--(10) over all `V` faces gives

\[
 \sum_Td(T)w(T)\ge V(n-2\mu),
 \qquad
 \sum_Tw(T)\le V(R-2)\mu.                          \tag{11}
\]

## 2. Proof of the weighted theorem

> **Theorem 1 (weighted rooted-star extraction).**  Equations (3)--(4)
> hold for every planar general-position set with `R>=3` and `mu<n/2`.

**Proof.**  The contribution to the first sum in (11) from triples outside
`mathcal H` is at most

\[
 {D_0\over2}\sum_Tw(T)
 \le {D_0\over2}V(R-2)\mu
 ={V(n-2\mu)\over2}.                                \tag{12}
\]

Therefore

\[
             \sum_{T\in\mathcal H}d(T)w(T)
                    \ge {V(n-2\mu)\over2}.                 \tag{13}
\]

Since `d(T)<=n-3`, equation (13) proves (3).  A face contributes at most
`R(R-2)` members to the sum on the left of (3); dividing proves (4).  QED.

For any convex face `A` containing `T`, none of the `d(T)` circuit neighbors
belongs to `A`, since every subset of `A` is convex.  Hence the pocket in
(5) is automatically disjoint from its attached source face.  Splitting the
neighbors according to the unique interior point of the bad four-circuit
gives one of four rooted roles with at least `d(T)/4` labels.

## 3. Coefficient-scale minimizer consequence

Let `P_n` attain `f(n)`, put `L=log n`, and suppose

\[
                         \mu\le(1-\epsilon)L.               \tag{14}
\]

Every subset of a largest face is a face, while the known construction gives

\[
 R\le\log V(P_n)\le(1/2+o(1))L^2.                  \tag{15}
\]

Equations (2), (14), and (15) imply (5).  Moreover `mu=O(L)=o(n)`, so (4)
becomes

\[
             |\{A:\mathcal T(A)\cap\mathcal H\ne\varnothing\}|
                    \ge {V\over O(L^4)}.                   \tag{16}
\]

Choose one canonical high triple `T_A` for every face in (16), and choose
its majority rooted role.  The exact residual is therefore:

> **Weighted pocket obstruction.**  A `1/polylog(n)` fraction of every
> low-mean minimizer's faces carries a disjoint, canonically rooted
> `n/polylog(n)` circuit cloud.  Either many sources reuse one such pocket,
> or the roots themselves have large entropy.

The common-pocket branch should be multiplied by the unrestricted face
reservoir inside that cloud; the diffuse-root branch should be charged to
the root entropy.  Neither global overlap estimate is proved here.

## 4. Dense stars do not force a decreasing mutation

The exact nine-point minimizer has stored integral coordinates

\[
\begin{split}
 &(62614,7322),(2922,4014),(10209,14386),\\
 &(20660,24299),(33336,29017),(30137,33324),\\
 &(15334,45211),(14934,55621),(10934,61521).
\end{split}                                                \tag{17}
\]

Its outer hull is the triple with stored indices `{0,1,8}`.  Every other
six points lies strictly inside this triangle, so

\[
                         d(\{0,1,8\})=6=n-3.                \tag{18}
\]

The exhaustive realizable-order-type certificate records this configuration
as the unique global minimizer among all 158,817 database order types, with

\[
 (v_0,\ldots,v_9)=(1,9,36,84,36,3,0,\ldots,0),
 \qquad V=169.                                      \tag{19}
\]

Thus no point mutation can lower `V`.  There is also a fully internal local
test.  Convert the exact slope order of (17) into its reduced word and
enumerate every exposed long-braid neighbor modulo commutations.  There are
eleven.  Relative to the nonempty objective `(V-1,M)=(168,492)`, their
changes are

\[
                         (\Delta V,\Delta M)=
 \begin{cases}
 (2,8)&\text{for eight neighbors},\\
 (2,10)&\text{for three neighbors}.
 \end{cases}                                               \tag{20}
\]

Hence the minimizer is a strict local minimum under every currently exposed
allowable-sequence flip, despite the maximum possible interior triple star.
Any mutation theorem must use the weighted family (16), not the existence of
one dense root.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_weighted_root_star.py
```

The checker recomputes every face, circuit degree, canonical tangent weight,
and non-addable incidence of (17) using exact integers.  It verifies
(11)--(13), the outer-hull star (18), and the exact source-face count for
(4).  It then reconstructs the reduced word from rational slopes and audits
all eleven braid mutations in (20).  Finally it checks the stored exhaustive
database metadata used only for the global-minimum assertion.
