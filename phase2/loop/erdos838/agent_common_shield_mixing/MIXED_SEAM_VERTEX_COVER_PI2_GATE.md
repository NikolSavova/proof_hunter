# Mixed seams reduce exactly to a bad-pair vertex-cover state

**Date:** 2026-08-15.  All logarithms are base two.  Write
`Z=V+1`, `C_hat=C+1`, and `U_hat=U+1` for counts including the empty set.

## Verdict

Qualitative nonhomogeneity of many adjacent `2+1` seams does not force a
quadratic ordinary-face bank.  There is an exact scalable planar wrapper in
which every seam is nonhomogeneous but one marked label per role repairs all
seams simultaneously.  If there are `q=Theta(log n)` roles, the repair tag
has only `2^q=2^{O(log n)}` values and is invisible at the quadratic
coefficient scale.

The correct quantitative state is a vertex cover of the **bad repeated-pair
graphs**.  If deleting a fixed set `H` of `T` labels makes all cross-role
`2+1` signs homogeneous, then for every projection direction `xi`,

\[
\begin{aligned}
 Z(P)&\le2^T Z(P-H),\\
 \widehat C_\xi(P)&\le2^T\widehat C_\xi(P-H),\\
 \widehat U_\xi(P)&\le2^T\widehat U_\xi(P-H).       \tag{1}
\end{aligned}
\]

The reverse inequalities hold because `P-H` is induced.  Hence the whole
two-direction state `Pi_2`, not only ordinary faces in the assembly chart,
changes by at most `T` bits per coordinate.  The decoder is exact:

\[
                       F\longmapsto(F-H,F\cap H).       \tag{2}
\]

Subsets of a convex face remain convex, and subsets of a cap or cup remain
the same kind of chain.  No distinct-coordinate regularity or product-cell
claim is used.

Thus the mixed-seam alternative has a sharp further dichotomy.

* If the total bad-pair cover is `o((log n)^2)`, mixed seams are
  coefficient-equivalent to the repaired wrapper and cannot themselves pay
  a fixed quadratic gain.
* A positive argument must first force cover entropy
  `Omega((log n)^2)` (equivalently a large bad-pair matching up to factor
  two), then turn those many disjoint repeated-coordinate defects into
  ordinary faces.

The second conversion remains open.  The construction here proves that
merely counting nonhomogeneous seams cannot replace it.

## 1. Bad-pair graphs

Let `X_1,...,X_q` be disjoint roles.  Assume their singleton transversals
have one fixed convex cyclic type.  Fix the desired vertical strong-glue
sign convention between every ordered pair of roles.

For role `X_i`, define a graph `G_i` on its labels.  A pair `{x,x'}` is an
edge if for some other role `X_j` and some `y in X_j`, the repeated-role
triple `(x,x',y)` has the wrong strong-glue sign (with the arguments put in
the order prescribed by `i<j`).  These are genuine repeated-coordinate
predicates; the singleton same-type hypothesis says nothing about them.
This is deliberately the **global** bad graph, not merely the predicate at
one adjacent seam.  Covers for adjacent graphs alone do not make a chain
after intermediate roles are discarded.

Choose a vertex cover `H_i` of `G_i` and put

\[
                         H=\bigcup_iH_i,qquad T=|H|.    \tag{3}
\]

Every pair remaining inside `X_i-H_i` has the homogeneous mixed sign toward
every other surviving role.  Thus `P-H`, in the assembly chart, is the
vertical strong composition of the induced role configurations.  Internal
order types remain arbitrary.

The elementary cover--matching relation gives

\[
                   \tau(G_i)\le2\nu(G_i),qquad
                   \sum_i\tau(G_i)\le2\sum_i\nu(G_i),   \tag{4}
\]

where a maximal matching supplies the factor-two cover.  Consequently a
large cover state really does contain many vertex-disjoint bad repeated
pairs.  What (4) does not provide is compatibility among their prospective
face outputs.

## 2. Exact all-direction repair

> **Theorem 1 (seam-cover decoder).**  Let `P` be any planar point set and
> `H subset P` have size `T`.  Put `v_0(P)=1`.  For every rank `r`,
>
> \[
> v_r(P)\le\sum_{j=0}^{\min(T,r)}{T\choose j}v_{r-j}(P-H).           \tag{5}
> \]
>
> For every generic projection direction `xi`, equation (1) holds.
> Therefore, for two generic directions `xi,eta`, every coordinate of
> `Pi_2(P)` lies between the corresponding coordinate of `Pi_2(P-H)` and
> `2^T` times it.

**Proof.**  If `F` is an ordinary face (possibly empty) of rank `r`, then `F-H` is an
ordinary face of `P-H`.  Record also the set `F cap H`, of size `j`.  The
pair in (2) recovers `F`, proving (5).  Summing over `r` proves the first
line of (1).

If `F` is a cap in direction `xi` (with the empty chain allowed), every subset of `F` is again a cap in
the induced `xi`-order; the same decoder proves the cap line of (1).
Likewise for cups.  Every face or chain of `P-H` is also one of `P`, which
gives the reverse inequalities.  Applying the one-direction inequalities
in `xi` and `eta` proves the `Pi_2` statement.  QED.

The load `2^T` is exact in the abstract: without geometric information on
the deleted labels, all subsets of `H` may occur over the same repaired
face.  In the marked construction below, (2) is the literal first-divergence
decoder and not merely a union bound.

## 3. A scalable one-defect-per-role realization

> **Theorem 2 (sparse mixed-seam wrapper).**  For all `q>=3` and `A>=4`
> there is a rational general-position configuration with roles
> `X_1,...,X_q`, `|X_i|=A`, such that:
>
> 1. every singleton transversal is convex in one fixed role order;
> 2. every ordered role pair has a nonhomogeneous `2+1` predicate;
> 3. in each `X_i` there is one marked pair `{p_i,z_i}` and it is the only
>    bad repeated pair; and
> 4. deleting `H={z_1,...,z_q}` leaves an exact vertical strong
>    composition.

**Construction.**  Put macro centers on a sufficiently shallow rational
parabola

\[
                         c_i=(i,\delta i^2),             \tag{6}
\]

with `delta>0` so small that every forward macro secant has slope less than
`1/10`.  At `c_i`, start with an arbitrary `(A-2)`-point rational core
`R_i`.  An invertible affine shear can make both coordinates strictly
increasing in one common label order.  A further positive diagonal scaling
puts the core in `[0,1]^2` with every secant slope positive and bounded away
from zero.

Add two markers, in local coordinates,

\[
                         p_i=(2,3),\qquad z_i=(3,2).      \tag{7}
\]

All core--core and core--marker secants have positive slope, while the one
marker secant `p_i z_i` has slope `-1`.  Replace each local configuration by

\[
                         c_i+\varepsilon X_i             \tag{8}
\]

for a sufficiently small positive rational `epsilon`.  Relative to every
later macro role, all positive-slope pairs have one strong-glue sign and
`p_i z_i` has the opposite sign.  The reflected statement holds toward
earlier roles.  All inequalities are strict, so one rational `epsilon` and
an arbitrarily smaller generic perturbation give general position without
changing a sign.

The macro parabola and smallness of (8) make every singleton transversal a
strict convex cup.  This proves 1--4.  Notice also

\[
                         Z(X_i)\le4Z(R_i),               \tag{9}
\]

because intersection with `R_i` is an ordinary face and the two marker
choices give at most four preimages.  Thus the sparse-defect gadget is
compatible with arbitrary low-face cores; it does not force a locally
Boolean child.

For this family `T=q`.  Equations (1),(5) become

\[
 \log Z(P)=\log Z(P-H)+O(q),
 \quad
 \log \widehat C_\xi(P)=\log \widehat C_\xi(P-H)+O(q),
 \quad
 \log \widehat U_\xi(P)=\log \widehat U_\xi(P-H)+O(q) \tag{10}
\]

uniformly over **all** directions.  If `q=Theta(log n)`, every error in
(10) is `O(log n)=o((log n)^2)`.  Hence every seam may be nonhomogeneous
without changing any quadratic `Pi_2` exponent.

## 4. Relation to the formal ramp

The repaired point set `P-H` has the exact strong-composition recurrence in
the assembly chart.  The sparse-defect wrapper has at most the
coefficient-free factor `2^q` more ordinary faces, and its endpoint counts
in every possible reset chart have the same factor bound.

This gives a scalable **two-direction state obstruction** to the proposed
mixed-seam proof: qualitative seam failure does not imply that either entry
of `Pi_2` is large.  If a low one-chart ramp could be realized by the
arbitrary cores, adding one defect per seam would make all seams
nonhomogeneous while preserving that ramp and its reset spectrum to
`2^{o((log n)^2)}` precision.

This is not an unconditional sub-half construction.  Realizing the repaired
strong wrapper with genuinely low arbitrary cores and a recursively low
second-direction profile is exactly the open `Pi_2` problem.  The theorem
shows only that sparse nonhomogeneity does not solve it.

## 5. Fixed-gap induction sharpens the survivor threshold

The minimizer bootstrap suggested by the high-root branch does give a
stronger, rigorous localization.  It does not by itself finish the mixed
branch.

> **Theorem 3 (fixed-gap survivor reset).**  Put `L=log n`.  Suppose
> `q=Theta(L)` roles have common size `A=n^{1-o(1)}` (in the balanced
> application `A=Theta(n/q)`).  Assume the strong induction input
>
> \[
>              \log f(t)\ge c(\log t)^2                 \tag{11}
> \]
>
> for all relevant `t<n`, where `c>0` is fixed.  Let
> `s=A/(log n)^B`.  If at least `rho L` bad-pair graphs have vertex covers
> leaving at least `s` labels, then
>
> \[
>                       \log V(P)\ge cL^2-O(L\log L).   \tag{12}
> \]
>
> The constant in the error depends only on `B,rho,c`.

**Proof.**  In every retained role delete a cover and choose exactly `s`
surviving labels.  The survivors in different roles have all vertical
strong-glue signs, so they form a chain of `r>=rho L` arbitrary atoms.
Every atom `Y` has, in the actual assembly chart, the universal bridge

\[
 \log X(Y)+\log Y(Y)
       \ge\log V(Y)-2\log|Y|
       \ge c(\log s)^2-2\log s.                         \tag{13}
\]

Apply the **conditional** reset theorem from
`LOOP_HEAVY_STRONG_GLUE_RESET_AUDIT.md` with the right side of (13) as
`F`.  Since `log s=L-O(log L)` and `r=Theta(L)`, its loss is
`O(L log L)`, proving (12).  No arbitrary-atom version of the
`NEXT_ENDPOINT_ATTACK` lemma is used.  QED.

At coefficient scale, (12) preserves the induction coefficient.  In
particular, if the induction input is `c=1/2-delta` and the parent is being
tested against a fixed lower threshold `(c-epsilon)L^2`, the survivor branch
contradicts that threshold for large `n`.

The contrapositive is much stronger than the earlier
`Omega(L^2)`-cover heuristic.  If fewer than `rho L` roles survive, then a
linear number of roles obey

\[
                  \tau(G_i)>A-s.                        \tag{14}
\]

By the factor-two cover--matching relation, each such role contains
`Omega(A)` vertex-disjoint bad pairs.  Across the disjoint roles this is

\[
                  \boxed{\Omega(qA)}                    \tag{15}
\]

pairwise label-disjoint repeated-coordinate defects; this is `Omega(n)` in
the balanced high-root application `qA=Theta(n)`.  Therefore the only
mixed-seam obstruction to the fixed-gap bootstrap is a **linear planar
bad-pair matching**, not merely one defect per seam or quadratic entropy in
the role names.

This also audits the proposed half-scale loop-cover bootstrap.  If the
pocket has size `n/polylog(n)`, induction at coefficient
`1/2-delta` makes its ordinary-face entropy
`(1/2-delta-o(1))L^2`; the global average-cover gate then forces cover
entropy at that same scale, assuming its aggregate load hypothesis.  But
large mandatory `3+1` loop entropy does not force large **bad-pair** cover:
Theorem 2 has `Theta(L^2)` role-alphabet entropy and only `T=q=Theta(L)`
seam-cover bits.  Thus the bootstrap closes the many-survivor branch and
localizes the residue to (15), but still needs a matching-to-face theorem.

The `O(L log L)` term in (12) is harmless for a fixed coefficient gap.  It
does mean that (12), by itself, is coefficient-preserving rather than a
strict coefficient improvement at an equality threshold.

## 6. What a positive mixed-seam theorem must assume

The natural quantitative replacement is:

\[
               \sum_i\tau(G_i)=\Omega((\log n)^2).      \tag{16}
\]

Even (16) is only the start.  By (4) it yields quadratically many disjoint
bad repeated-pair labels, but a planar charging argument must still convert
them into a bounded-overlap `2+2`, one-gap, or detached-face bank.  The
outputs must retain the role and pair marks; erasing them recreates the
`2^T` ambiguity in Theorem 1.

This cover threshold is the exact analogue of the blocker-role cover state
in the high-loop analysis.  It respects repeated-coordinate predicates and
does not infer them from distinct-coordinate semialgebraic homogeneity.

For the fixed-gap high-root application, Theorem 3 shows that the relevant
hard threshold is actually the linear matching (15), unless the desired
regularization is required to retain substantially fewer than `Theta(L)`
roles.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_mixed_seam_vertex_cover_pi2.py
```

The exact checker builds the `q=4,A=4` rational instance, verifies general
position, all 256 singleton transversals, and that each bad-pair graph is the
single marked edge.  It exhausts all subsets to check (5), recovers the
strong-composition recurrence after deleting the three marked labels, and
enumerates every projection chamber to verify the cap/cup inequalities in
(1).  It also checks the coefficient arithmetic and the linear-matching
contrapositive in Theorem 3 over a range of exact integer parameters.
