# Quadratic crossing cores: a linear shield barrier to local mixed faces

**Date:** 2026-08-14.  All logarithms are base two.  The empty face is
counted.

## Verdict

The most direct crossing-core completion of
`../agent_linear_codim_capped/LINEAR_CODIM_CAPPED_CHAIN.md` is false at
exactly the required scale.  There are planar families with

* `2^{Theta(r^2)}` distinct rank-`r` outer cores;
* one common strict insertion-chain pocket;
* a genuine simple selector of `d` distinct successors above every actual
  source; and
* the following shield property: every ordinary face which contains the
  two labels of a selected chain incidence and is local to its source core
  must erase an entire `Theta(r)`-point side of that core.

Consequently a coordinatewise mixed-face map has
`2^{Theta(r^2)}` inverse fibres, even for an ordered pair of records based
at two different cores.  Deleting the common chord, a bounded set of
guards, or even `o(r)` core labels cannot fix the problem.

This is a barrier to the **record-local guard-release route**, not a
counterexample to the unrestricted global EIC.  The construction pays for
the missing information in a huge ordinary-face cloud on the shield
labels.  Thus a successful global crossing-core theorem must be allowed to
route a record to nonlocal ordinary faces (or use a Cauchy/telescope which
charges that cloud); it cannot insist that the output remain a mixed
downface of the record's own core.

## 1. A uniform planar shield

Fix integers `M>=s>=1` and `N>=2`.  Put

\[
 u=(-1,0),\qquad v=(1,0).
\]

Choose two `M`-point clouds `L,R` on the lower arc of a strictly convex
oval, with `L` in a sufficiently small neighbourhood of `u` and `R` in a
sufficiently small neighbourhood of `v`.  Above `uv`, choose points
`X={x_1,...,x_N}` satisfying

\[
 x_i\in\operatorname{int}\operatorname{conv}\{u,v,x_j\}
                         \qquad(i<j).                 \tag{1}
\]

The clouds can be chosen sufficiently close to the endpoints that,
simultaneously for every `l in L`, `q in R`, and `i<j`,

\[
 x_i\in\operatorname{int}\operatorname{conv}\{l,q,x_j\}.   \tag{2}
\]

They can also be chosen so every member of
`Y={u,v} union L union R` remains extreme after any one `x_j` is adjoined.
All conditions are strict and finite, so rational general-position choices
exist.

For an explicit realization, use the rational lower semicircle

\[
 c(t)=\left({2t\over1+t^2},{t^2-1\over1+t^2}\right),
\]

take `u=c(-1),v=c(1)`, put the left and right parameters arbitrarily close
to `-1` and `1`, and take

\[
                         x_i=(\delta i^2,i)          \tag{3}
\]

with positive rational `delta` sufficiently small.  First choose `delta`
so (1) is strict, and then move the lower clouds close enough to the
endpoints that (2) and all tangent inequalities persist.  Avoiding the
finitely many collinearity equations gives general position.

For `S in binom(L,s)` and `T in binom(R,s)`, define the outer core

\[
                         B_{S,T}=\{u,v\}\cup S\cup T.          \tag{4}
\]

Every `B_{S,T}` and every `B_{S,T}+x_j` is an ordinary convex face, by
deletion from `Y+x_j`.  Equation (1) gives the repair relation

\[
 \operatorname{ext}(B_{S,T}\cup\{x_i,x_j\})
                         =B_{S,T}\cup\{x_j\}\qquad(i<j).     \tag{5}
\]

There are

\[
                  K={M\choose s}^2                            \tag{6}

distinct cores, all of rank `r=2s+2`; their chain sources have rank
`rho=r+1`.  Taking `M=2^{lambda rho+O(1)}` with fixed `lambda>1` and
`s=(rho-3)/2` gives

\[
                  \log K=(\lambda+o(1))\rho^2.               \tag{7}

Thus the family has the quadratic core entropy required by the residual
case.

## 2. The shield lemma

> **Lemma 1 (one whole side must be erased).**  Fix `B=B_(S,T)` and
> `i<j`.  If an ordinary face `F` obeys
> \[
>        \{x_i,x_j\}\subseteq F\subseteq B\cup\{x_i,x_j\},  \tag{8}
> \]
> then `F cap S=emptyset` or `F cap T=emptyset`.

**Proof.**  Otherwise choose `l in F cap S` and `q in F cap T`.
By (2), `x_i` lies strictly inside the triangle `l q x_j`, which is
contained in `conv(F-{x_i})`.  Hence `x_i` is not extreme in `F`, contrary
to `F` being a face.  QED.

In particular, every output of the form (8) deletes at least `s=(r-2)/2`
labels.  The conclusion still holds if `u,v` and any further `o(r)` labels
are deleted first.  It is not a failure caused by the two tangent guards:
the two side clouds themselves shield every nested pocket point.

The lemma also identifies the information loss.  A local output may retain
the chosen left `s`-set or the chosen right `s`-set, but never both.  The
forgotten choice has `log binom(M,s)=Theta(r^2)` bits.

## 3. Exact capped selector and local congestion

For clarity take `N=2d`.  Above every actual source `B+x_i`, `1<=i<=d`,
select the `d` distinct successors

\[
                            x_j,\qquad d<j<=2d.               \tag{9}

This is a simple selector: it contains no path multiplicities and its
outdegree is exactly the cap `d`.  Each core carries

\[
                            e=d^2=N^2/4                       \tag{10}

actual repair incidences, and the total record demand is `D=Ke`.

This can be put at the natural linear-codimension cap.  With the parameters
following (7), choose

\[
 d=2^{(\lambda-1)\rho+O(1)},\qquad N=2d.                    \tag{10a}
\]

The ambient cardinality is
`n=2M+N+2=2^{lambda rho+O(1)}`, so
`rho=(1/lambda+o(1))log n` and
`d<=n/2^rho` after changing only the harmless absolute factor in (10a).
Thus these are actual selected incidences at fixed linear codimension, not
complete-history multiplicities.

Call an ordinary face *record-local* if it satisfies (8) for at least one
selected record.  Put

\[
                  A(M,s)=\sum_{a=0}^s{M\choose a}.            \tag{11}

Lemma 1 gives the crude but useful global range bound

\[
 |U|\le 8{N\choose2}A(M,s).                                  \tag{12}

Indeed choose the two pocket labels, the subset of `{u,v}`, which one of
the two side clouds survives, and a subset of that cloud of size at most
`s`.  Therefore every map from the selected records to record-local faces
has maximum fibre at least

\[
 {D\over |U|}
 \ge { {M\choose s}^2 d^2
       \over 8{2d\choose2}A(M,s)}
 \ge { {M\choose s}^2\over 32 A(M,s)}.                       \tag{13}

When `M/s tends to infinity`,
`A(M,s)=(1+o(1))binom(M,s)`, so (13) is

\[
                    2^{(\lambda/2+o(1))\rho^2}              \tag{14}

under the normalization (7).  The precise coefficient is unimportant;
the loss is quadratic rather than the required `2^{o(r)}`.

For ordered pairs based at different cores, the demand is

\[
                       K(K-1)e^2.                            \tag{15}

If each output coordinate is required to be record-local to its
corresponding record, its range is contained in `U^2`.  Hence the maximum
fibre is at least

\[
 {K(K-1)e^2\over |U|^2}
       =2^{(\lambda+o(1))\rho^2}.                            \tag{16}

This is the exact crossing-core term, with the same-core diagonal removed.

## 4. Why this does not refute global EIC

The union `L union R` is itself in convex position.  It therefore supplies
`2^{2M}` unrestricted ordinary faces, vastly more than (15).  A global EIC
map may use those faces as an arbitrary codebook and need not satisfy (8).
The construction consequently cannot be promoted to a numerical
counterexample by counting only mixed core-pocket faces.

This distinction is the useful conclusion.  Quadratic core entropy does
not force a *local* compatible product: it can be protected behind a
linear shield.  But in this explicit shield, the labels responsible for
the protection create the nonlocal face reservoir which pays globally.
The remaining positive theorem must capture precisely that alternative:

\[
 \boxed{\text{mixed core--pocket product, or a charge to the shield's
 unrestricted ordinary-face complex.}}                       \tag{17}
\]

A bounded-codimension guard release, a fixed endpoint deletion, or a
coordinatewise local Hall neighbourhood cannot establish (17).  A global
Cauchy/telescope is essential.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_quadratic_cross_core/verify_quadratic_cross_core.py
```

The checker uses exact rational coordinates, verifies general position,
all strict nesting and shield triangles, all core/tip faces and repair
hulls, and exhausts the record-local face universe for a finite capped
instance.  It also audits the symbolic demand/range inequalities and the
quadratic entropy scaling.
