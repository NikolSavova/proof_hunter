# Fixed-power saving from bounded planar circuit codegrees

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

The fixed-power target is true whenever the nonconvex-quadruple hypergraph
has bounded triple codegree.  More precisely, let `C` be any family of
rank-`r` convex cores on an `m`-point planar ground set.  If no triangle is
contained in more than `Lambda` nonconvex quadruples, then every core has at
least

\[
                 u=m-r-\Lambda{r\choose3}                    \tag{1}

convex one-point extensions.  Consequently

\[
                 V(P)\ge {|C|u\over r+1}.                    \tag{2}

If each core carries at most `d` selected repairs and
`u/(r+1)>=d^epsilon`, this gives

\[
                 |E|\le d^{1-\epsilon}V(P).                  \tag{3}

At the quadratic source scale, `|C|>=d^(beta r)` already forces the ground
support to have `m>=Omega(r d^beta)` points.  Thus the bounded-codegree
condition `Lambda binom(r,3)<=m/3` yields (3) for every fixed
`epsilon<beta`; in the coefficient-`1/4` hard slice one has `beta>=1-o(1)`,
so for example `epsilon=1/3` works uniformly.

Failure gives an exact container seed: one triangle participates in at
least `Omega(m/r^3)` bad quadruples, and one of its four rooted circuit
types contains a quarter of those labels.  The unresolved branch is
therefore not an arbitrary incomplete product.  It is a quadratic-entropy
source family concentrated over a macroscopic common rooted triangle cell.

This is a genuine partial theorem, not the full fixed-power inequality.

## 1. The planar circuit hypergraph

For a planar general-position set `Q`, let `H_Q` be the 4-uniform
hypergraph whose edges are the nonconvex four-subsets.  A subset `A subset Q`
is an independent set of `H_Q` exactly when it is in convex position.

Indeed, if `A` is not convex, one point lies in the hull of the others, and
planar Caratheodory places it in a triangle of three other points.  Thus `A`
contains a bad quadruple.  The converse follows by deletion.

For a triple `T`, put

\[
  \deg_H(T)=|\{x\in Q-T:T\cup\{x\}\in H_Q\}|,
  \qquad \Lambda=\max_T\deg_H(T).                            \tag{4}
\]

The argument below actually holds for every 4-uniform hypergraph; planarity
identifies its independent sets with the ordinary face bank.

## 2. Bounded codegree forces upward face expansion

> **Theorem 1 (triple-codegree extension theorem).**  Let `H` be a
> 4-uniform hypergraph on `m` vertices, and let `C` be any family of
> independent `r`-sets.  If the maximum triple codegree is `Lambda`, put
> \[
>                         u=m-r-\Lambda{r\choose3}.            \tag{5}
> \]
> Then the independent-set complex of `H` contains at least
> \[
>                    {|C|\max(u,0)\over r+1}                 \tag{6}
> \]
> distinct `(r+1)`-sets.

**Proof.**  Fix `A in C`.  A label `x notin A` fails to extend `A` exactly
when `A+x` contains a hyperedge.  Since `A` itself is independent, such an
edge is `T+x` for some `T in binom(A,3)`.  The union bound and (4) show that
at most `Lambda binom(r,3)` outside labels fail.  Hence `A` has at least
`max(u,0)` independent one-point extensions.

Count pairs `(A,B)` with `A in C`, `B` an independent `(r+1)`-set, and
`A subset B`.  The preceding paragraph gives at least
`|C|max(u,0)` pairs, while any `B` contains at most `r+1` members of `C`.
Division proves (6).  QED.

For the planar circuit hypergraph, all sets in (6) are ordinary convex
faces.  This gives (2) without requiring the extension to coexist with any
pocket blocker.

> **Corollary 2 (fixed-power selected-repair bound).**  In the planar
> setting, suppose every `A in C` carries at most `d` selected repair
> records.  If
> \[
>                 {m-r-\Lambda\binom r3\over r+1}
>                            \ge d^\epsilon,                  \tag{7}
> \]
> then
> \[
>                            |E|\le d^{1-\epsilon}V(P).       \tag{8}
> \]

**Proof.**  The cap gives `|E|<=d|C|`.  Theorem 1 and (7) give
`V(P)>=d^epsilon|C|`.  Combine them.  QED.

This is a global count, not a record-local map.  Its paying `(r+1)`-faces
may be unrelated to the selected blockers.

## 3. Quadratic entropy supplies the power

The codegree premise is useful because quadratic source entropy forces an
exponential ground support.  The elementary estimate

\[
             |C|\le{m\choose r}\le\left({em\over r}\right)^r \tag{9}

gives

\[
                         m\ge {r\over e}|C|^{1/r}.            \tag{10}

> **Corollary 3 (entropy--codegree regime).**  Suppose
> \[
>                         |C|\ge d^{\beta r}                  \tag{11}
> \]
> for fixed `beta>0`, `d tends to infinity`, and
> \[
>             r+\Lambda{r\choose3}\le {m\over3}.             \tag{12}
> \]
> Then, for every fixed `epsilon<beta` and all sufficiently large
> parameters,
> \[
>                         |E|\le d^{1-\epsilon}V(P).          \tag{13}
> \]

**Proof.**  Equations (10)--(11) give
`m>=r d^beta/e`.  From (12), the numerator in (7) is at least `2m/3`, so

\[
 {m-r-\Lambda\binom r3\over r+1}
       \ge {2r\over3e(r+1)}d^\beta\ge d^\epsilon             \tag{14}
\]

for large `d`.  Corollary 2 applies.  QED.

At a hard coefficient-scale slice, write

\[
 r=(\alpha+o(1))L,\quad d=2^{(1-\alpha+o(1))L},\quad
 \log|C|\ge(c-o(1))L^2.                                     \tag{15}
\]

Then (11) holds with

\[
 \beta={c\over\alpha(1-\alpha)}-o(1).                       \tag{16}
\]

Since `alpha(1-alpha)<=1/4`, the established `c>=1/4` gives
`beta>=1-o(1)`.  Thus under (12), any universal
`epsilon<1` is asymptotically available; choosing `epsilon=1/3` leaves
ample room for all lower-order factors.

## 4. Exterior blockers give a common rooted-triangle container

The global codegree `Lambda` in Theorem 1 also sees points lying inside a
source hull.  Those points are irrelevant to exterior repair.  The exterior
part has a sharper sourcewise localization with no bounded-codegree
assumption.

For a convex source `A`, let

\[
 q(A)=|Q\setminus\operatorname{conv}(A)|,\qquad
 u(A)=|\{x:A+x\text{ is convex}\}|,\qquad
 e(A)=q(A)-u(A).                                               \tag{15a}
\]

Thus `e(A)` is exactly its number of exterior blocked labels.

> **Theorem 4 (rooted-circuit container).**  Every convex rank-`r` source
> `A` has an ordered rooted triple `(a;b,c)` of distinct labels in `A` such
> that at least
> \[
>                         {e(A)\over3\binom r3}                \tag{15b}
> \]
> exterior blockers `x` satisfy
> \[
>                  a\in\operatorname{int}\operatorname{conv}\{b,c,x\}.
>                                                                    \tag{15c}
> \]
> Consequently, if a source family `C` has `e(A)>=h` for every member,
> one fixed ambient rooted triple is assigned to at least
> \[
>                         {|C|\over3\binom m3}                 \tag{15d}
> \]
> sources, and every assigned source has at least
> `h/(3 binom(r,3))` blockers in that rooted cell.
> The same assertions hold with `e(A)` replaced by the size of any
> preselected subfamily of exterior blocked labels over `A`.

**Proof.**  Let `x` be exterior to `conv(A)` but suppose `A+x` is not
convex.  Some `a in A` is not extreme in `A+x`.  Planar Caratheodory puts
`a` in the triangle of three points of `(A-a)+x`.  The triangle must use
`x`, since `a` is extreme in `A`; hence it is `{b,c,x}` for two labels
`b,c in A-a`.  General position makes the containment strict and the
interior point unique.  Assign `x` to one such rooted triple.  There are
`3 binom(r,3)` rooted triples in `A`, proving (15b).

The proof never used unselected blocked labels, so it applies verbatim to
any preselected subfamily.  For the family statement, assign each source one rooted triple attaining
(15b).  There are at most `3 binom(m,3)` ambient tags.  Pigeonhole proves
(15d), and the blocker lower bound is retained by the chosen tag.  QED.

At `m=2^{Theta(r)}`, fixing the tag costs only `O(r)` bits.  Therefore a
quadratic-entropy hard source family remains quadratic after this
localization.  **This is only a coefficient-scale statement.**  There are
`3 binom(m,3)=2^{Theta(r)}` ambient rooted tags.  That multiplicity can be
larger than the desired `d^epsilon=2^{epsilon(ell-r)}` gain.  Hence one
cannot pigeonhole a single ambient rooted triangle inside the fixed-power
EIC contradiction and then discard the tag cost.  The sourcewise choice
costs only `3 binom(r,3)`, which is harmless; the subsequent global
identification of the chosen triples is the load-bearing step.

The blocker cloud itself can be made common by the exact DRC count.  Let
`C_0` be the cell in (15d), let every source have at least `D` blockers in
the fixed rooted region, and fix `1<=t<=D`.  Double counting pairs
`(A,Z)`, `Z subset N(A)`, `|Z|=t`, gives a `t`-set of blockers common to at
least

\[
                  |C_0|{\binom Dt\over\binom mt}              \tag{15e}
\]

sources.  When `D=d/r^O(1)`, `m<=n=2^{Theta(r)}`, and
`t=floor(sqrt(r))`, the logarithmic loss in (15e) is only
`O(r^(3/2))=o(r^2)`.  Thus the unbounded-codegree branch reduces to a
quadratic source family with a common rooted triangle and a growing common
blocker fan **at quadratic-entropy resolution**.  It does not yet reduce
the fixed-power EIC problem: (15d) has already paid an ambient
`2^{Theta(r)}` tag factor.  To preserve a `d^epsilon` gain one needs either
a gain exceeding that factor, or a summed-over-triangles/Cauchy bank whose
ordinary faces carry only `r^O(1)` total tag load.

## 5. Exact heavy-circuit localization from global codegree

The contrapositive is structurally useful.

> **Corollary 5 (macroscopic rooted triangle).**  If (12) fails and
> `m>=6r`, then some triple `T` has
> \[
>                    \deg_H(T)>{m/3-r\over\binom r3}
>                              \ge {m\over6\binom r3}.        \tag{17}
> \]
> Moreover, at least one of four rooted circuit types occurs for at least
> `deg_H(T)/4` of these fourth labels.

**Proof.**  Failure of (12) gives the first inequality.  The assumption
`m>=6r` gives the second.  Every planar bad quadruple has a unique point in
the triangle of the other three.  For a fixed triple `T={a,b,c}` and a
fourth point `x`, the interior point is exactly one of `x,a,b,c`.
Pigeonhole proves the final assertion.  QED.

Thus the heavy branch canonically fixes:

* one triangle `T`;
* which of its three labels, or the varying fourth label, is the circuit's
  interior point; and
* a cloud of `Omega(m/r^3)` fourth labels in that one rooted cell.

There are `4 binom(m,3)=2^{Theta(r)}` possible tagged cells.  Their
logarithm is only `O(r)`, so selecting one costs no *quadratic* entropy, but
the multiplicity is not negligible compared with `d^epsilon`.  What is
still missing is a theorem coupling all tagged source cells, without this
ambient pigeonhole loss, to the ordinary face complex of their
fourth-label clouds.  An absolute cloud count alone is not multiplicative
enough.

## 6. Container interpretation and remaining boundary

Theorem 1 is the first step of the elementary hypergraph-container
algorithm.  An independent `r`-set with many available labels expands
upward and pays.  Failure means its triples cover nearly the whole ground
set through circuit neighborhoods, and (17) supplies a high-codegree
fingerprint.

Iterating fingerprints without retaining the source partition is unsafe:
different cores may use different high-codegree triples and later merge
into the same rooted cloud.  A full container proof would need an
amortized statement of the following form:

\[
 \boxed{\begin{array}{c}
 \text{upward expansion by }d^\epsilon,\text{ or}\
 \text{a summed rooted-triangle bank with polynomial face overlap whose}\
 \text{released fourth-label complexes supply }d^\epsilon\text{ globally.}
 \end{array}}                                                \tag{18}
\]

The first line is proved here.  Theorem 4 and Corollary 5 give the exact
sourcewise fingerprint for the second.  Proving that all fingerprints can
be summed with only polynomial ordinary-face overlap--without paying the
ambient `m^3` tag count--is the remaining crossing-core stability problem.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_quadratic_cross_core/verify_circuit_codegree_power.py
```

The checker exhausts all 4-uniform hypergraphs through six vertices,
audits every full independent rank family and thousands of deterministic
subfamilies, verifies the extension double count and codegree bound, checks
the entropy-to-power arithmetic, and audits the four rooted planar circuit
types on exact rational point sets.
