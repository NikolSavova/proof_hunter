# Minimal rooted defects and their exact rank expansion

**Date:** 2026-08-14  
**Verdict:** the factorial-toggle defect has a sharper positive cover by
inclusion-minimal rooted nonfaces.  Except at the empty closed state, every
such nonface has at most three exterior labels; the only four-label case is
a whole planar circuit over the empty state.  The cover is exactly a positive
`2^{-rank}` sum.  The defect itself also has an exact signed `2^{-rank}`
Möbius expansion over unions of those boundaries.

This does not yet imply an asymptotic bound for `H` or for the half-activity
mean.  A realizable nested-fan family has only two-label minimal roots, but
its local defect tends to its maximum and its exact rank expansion has
exponentially large cancellation.  Consequently bounded root size is not a
bounded-reuse theorem; a useful inequality still has to charge roots across
different closed states to ordinary faces.

All probabilities below are at Bernoulli parameter `1/2`.  The point set is
in planar general position, and the empty convex face is included.

## 1. Closed states and the defect

For a convex face `A`, write

\[
 C_A=P\cap\operatorname{conv}(A),\qquad
 E_A=P\setminus C_A,\qquad q_A=|E_A|.
\]

For `X subseteq E_A`, call `X` **good over `A`** when every label of `X` is
extreme in `C_A union X`.  Otherwise call it bad.  The good sets form a
down-set and the bad sets form an up-set.  Let

\[
 \mathcal M_A=\{M\subseteq E_A:M\text{ is inclusion-minimal bad over }A\}.
\]

Grouping half-samples by their closed hull gives the exact local form of the
factorial-toggle defect:

\[
 \boxed{
 \Delta(P):=\mathbb E2^O-\mathbb E2^H
 =\sum_{A\in\mathcal F(P)}2^{-|A|-q_A}
   |\{X\subseteq E_A:X\text{ bad over }A\}|.}       \tag{1}
\]

Indeed, the samples with closed hull `C_A` are precisely `A union I` with
`I subseteq C_A-A`, hence have total probability
`2^{|C_A|-|A|-n}=2^{-|A|-q_A}`.  The good occurrences are exactly the
occurrences paired by factorial toggling, so their complement gives (1).

## 2. First repair removes the generic four-label term

> **Theorem 1 (minimal-root trichotomy).**  If `C_A` is nonempty, then every
> `M in mathcal M_A` has
> \[
> 2\le |M|\le3.                                      \tag{2}
> \]
> If `C_A` is empty, a minimal bad set has size at most four.  In general
> position the only possibility is `|M|=4`, with one point strictly inside
> the triangle of the other three.

**Proof.**  Let `x in M` be nonextreme in `C_A union M`.  Planar
Caratheodory gives a witness of at most three labels from
`C_A union (M-x)`.  Keeping `x` and just the exterior labels in this witness
produces a bad subset of `M`.  Minimality therefore gives `|M|<=4`.

Suppose equality holds and choose `c in C_A`.  The Caratheodory witness must
then be three labels `u,v,w` of `M-x`, with `x in conv{u,v,w}`.  Extend the
ray from `c` through `x` until it leaves the triangle `uvw`.  Its exit point
lies on an edge, say `uv`, and `x` lies in `conv{c,u,v}`.  Thus
`{x,u,v}` is already bad over `A`, contradicting minimality.  Hence a
four-label minimal root forces `C_A=emptyset`.  At the empty state, general
position makes every set of at most three points convex, and a minimal
four-point nonface is exactly a point-in-triangle circuit.  QED.

Thus the size-four term in the earlier Caratheodory cover is not a generic
relative tangent obstruction.  It occurs only once at the total empty
closed state (although that state can contain many four-circuits).

## 3. The exact positive `2^{-rank}` cover

Every bad `X` contains at least one member of `mathcal M_A`.  A union bound
over its minimal roots yields

\[
 |\{X\subseteq E_A:X\text{ bad}\}|
 \le \sum_{M\in\mathcal M_A}2^{q_A-|M|}.            \tag{3}
\]

Substitution in (1) proves

\[
 \boxed{
 \Delta(P)\le \mathfrak W(P):=
 \sum_{A\in\mathcal F(P)}\sum_{M\in\mathcal M_A}
 2^{-(|A|+|M|)}.}                                  \tag{4}
\]

This is an equality defining the weighted minimal-root cover: if the rank of
a rooted boundary is

\[
 r(A,M)=|A|+|M|,
\]

then `mathfrak W` is exactly the positive sum of `2^{-r(A,M)}` over all
repairable nonfaces `(A,M)`.  They are repairable in the literal sense that
every proper exterior subset of `M` is jointly toggleable over `A`.

The empty-state contribution consists only of four-circuits and equals

\[
 {\#\{\text{rooted four-circuits of }P\}\over16}.   \tag{5}
\]

All remaining terms have two or three exterior labels.

## 4. Exact signed expansion of the defect itself

The union bound in (3) is not exact because a bad set can contain many
minimal roots.  There are two equivalent exact rank expansions.  Direct
inclusion-exclusion gives

\[
 \boxed{
 \Delta(P)=
 \sum_A\sum_{\emptyset\ne J\subseteq\mathcal M_A}
 (-1)^{|J|+1}2^{-(|A|+|\bigcup_{M\in J}M|)}.}       \tag{6}
\]

For a collected version, let `f_A(X)` be the bad-set indicator and define
its Boolean Möbius transform

\[
 \beta_A(Y)=\sum_{X\subseteq Y}(-1)^{|Y|-|X|}f_A(X).
\]

Then

\[
 \beta_A(Y)=
 \sum_{\substack{\emptyset\ne J\subseteq\mathcal M_A\\
                   \bigcup_{M\in J}M=Y}}
 (-1)^{|J|+1},                                     \tag{7}
\]

so a nonzero coefficient is supported on a union of minimal rooted
boundaries.  Averaging `f_A(X)=sum_{Y subseteq X} beta_A(Y)` over a uniform
`X subseteq E_A` gives

\[
 \boxed{
 \Delta(P)=\sum_A\sum_{Y\subseteq E_A}
 \beta_A(Y)2^{-(|A|+|Y|)}.}                        \tag{8}
\]

Equations (4) and (8) separate the issue cleanly.  Root rank is bounded in
the positive cover, but unions in the exact expansion can have every rank,
and their coefficients have signs.

## 5. A planar nested-fan barrier

For `q>=2`, put `B=4q` and take

\[
 a=(-B,0),\quad b=(B,0),\quad y_i=(i,2^i)
 \quad(1\le i\le q).                               \tag{9}
\]

These points are in general position.  Let `A={a,b}`.  Its closure is just
`A`.  If `i<j`, then `y_i` is strictly inside the triangle `aby_j`: at
height `2^i`, writing `t=2^{i-j}<=1/2`, that triangle has horizontal centre
`tj` and half-width `B(1-t)`, while

\[
 |i-tj|\le q+q/2 < B(1-t).
\]

Consequently every exterior singleton is good, every exterior pair is bad,
and

\[
 \mathcal M_A={E_A\choose2}.                       \tag{10}
\]

The local positive cover and the actual local defect are therefore

\[
 \mathfrak W_A={\binom q2\over16},\qquad
 \Delta_A={1\over4}\left(1-{q+1\over2^q}\right). \tag{11}
\]

Thus even two-label roots can make the normalized bad probability tend to
one.  The root union bound is worse than the true defect by `Theta(q^2)`.
More decisively, the exact Möbius coefficient of an `s`-set is

\[
 \beta_s=(-1)^s(s-1)\qquad(s\ge2),                 \tag{12}
\]

and hence

\[
 \Delta_A={1\over4}\sum_{s=2}^q
 \binom qs(-1)^s(s-1)2^{-s}.                       \tag{13}
\]

The absolute mass of the same expansion is

\[
 {1\over4}\left[1+\left({q\over3}-1\right)
                    \left({3\over2}\right)^q\right]. \tag{14}
\]

An order-one answer is therefore obtained through exponential
cancellation among arbitrarily high-rank unions of rank-two boundaries.

This also rules out a statewise comparison with the toggleable hull term.
For this same `A`, the term in `sum_A 2^{-q_A}` is `2^{-q}`, whereas
`Delta_A` tends to `1/4`; their ratio is exponential.

## 6. Why no asymptotic `H` or mean inequality follows yet

The new reduction is structurally sharp but not an asymptotic estimate.

1. The empty state already contains the original counting problem.  Good
   exterior subsets over `A=emptyset` are exactly the convex subsets of
   `P`, so its normalized bad mass is
   \[
   1-{V(P)\over2^n}.                                \tag{15}
   \]
   Estimating the complementary mass of the four-circuit boundary complex
   is precisely estimating `V(P)`.
2. The nested fan proves that small minimal roots do not control their
   reuse.  Neither truncating (8) to low ranks nor taking absolute values is
   viable: the former is false and the latter can be exponentially larger
   than the defect.
3. The positive cover (4) has no closed-state-local charge.  A single state
   can contribute order one to the defect while its hull term is
   exponentially small.  Any useful inequality must send a rooted boundary
   to other ordinary faces and bound the total cross-state congestion.

The only automatic estimate from root size is the circular one

\[
 \mathfrak W(P)\le
 \left({n\choose2}+{n\choose3}\right)Z_P(1/2)
 +{n\choose4\over16},                              \tag{16}
\]

up to harmlessly overcounting the unique empty-state term.  Since the
quantity to be bounded appears on the right, (16) yields no new bound on
`H=nZ_P(1/2)/V(P)` and no lower bound on the half-activity mean.

The exact remaining target is therefore a **cross-state bounded-reuse
theorem** for the rank-two/rank-three rooted boundaries in (4), not another
local Caratheodory reduction.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_rooted_cluster_weight/verify_rooted_cluster_weight.py
```

The verifier uses exact integer and rational arithmetic.  It exhausts every
closed face state of the four-point circuit and the exact nine-point
minimizer; verifies the minimal-root trichotomy; reconstructs both the
positive cover and the signed Möbius rank identity; and checks the nested
fans through twelve exterior labels, including (10)--(14) and exact general
position.
