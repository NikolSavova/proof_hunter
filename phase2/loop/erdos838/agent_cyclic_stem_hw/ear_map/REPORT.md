# Erdős 838: cumulative block growth and the constant-two ear map

**Date:** 2026-08-14  
**Verdict:** the exterior-ear encoding can be sharpened substantially: after
the hidden interval and repaired hull are retained, its inverse multiplicity
is at most **two**, independently of rank.  This removes the previous factor
`r` from the ear-pair bound.  It still does not prove the required block
growth, because the encoding lands in a compatible **pair** of convex faces,
not one face.  Exact common-ear families show that this distinction is real.

For the weaker cumulative profile

\[
 F_k=\sum_{j=0}^k v_j,
\]

the block target

\[
 F_{k+b}\ge2F_k\qquad(0\le k\le\ell-2b),
 \quad \ell=\lceil\log_2 n\rceil,                 \tag{CB}_b
\]

is rigorously true in the initial range

\[
 k+b\le(1-o(1))\sqrt{b\log_2 n}.                  \tag{1}
\]

A first-failure reduction proves that the uncovered middle range is exactly
the low-addable exterior-ear Hall problem already isolated by the main
attack.  No solution of Erdős 838 is claimed here.

## 1. Why even cumulative block growth is a major theorem

Iterating `(CB)_b` at `k=0,b,2b,...` shows that every successive block of
ranks contains a face.  In particular the maximum convex rank is at least

\[
 \ell-3b+1.                                       \tag{2}
\]

Consequently, a universal `b=O(log ell)` would imply

\[
 ES(t)\le2^{t+O(\log t)},                         \tag{3}
\]

which is a near-conjectural Erdős--Szekeres bound.  Thus neither the
coefficientwise nor cumulative block statement should be expected from a
routine ear count.

The cumulative statement is nevertheless exactly strong enough for the
mean route.  The inequalities make the lower-tail masses decay geometrically
in steps of `b`; summing the tail gives

\[
 \mu(P)\ge\ell-3b.                                \tag{4}
\]

Hence `b=O(log log n)` would give the desired
`mu>=log n-O(log log n)`.

## 2. An unconditional initial window

There is a clean range in which `(CB)_b` follows just from supersaturation
of the Erdős--Szekeres theorem.

> **Proposition 1 (coarse cumulative block growth).**  Put `t=k+b`, let
> `m=ES(t)`, and suppose `n>=m` and `k<=(n-1)/3`.  If
> \[
>  \binom{n-k}{b}
>  \ge2\binom{t}{b}\binom mt,                     \tag{5}
> \]
> then `F_t>=2F_k`.

**Proof.**  Every `m`-subset contains a convex `t`-subset.  Counting pairs
consisting of such a witness and an `m`-set containing it gives

\[
 v_t\binom{n-t}{m-t}\ge\binom nm,
 \qquad
 v_t\ge{\binom nt\over\binom mt}.                \tag{6}
\]

Since successive lower binomial coefficients shrink by a factor at most
`k/(n-k)<=1/2`,

\[
 F_k\le\sum_{j=0}^k\binom nj\le2\binom nk.        \tag{7}
\]

Finally

\[
 {\binom nt\over\binom nk}
 ={\binom{n-k}{b}\over\binom tb}.                 \tag{8}
\]

Condition (5) therefore gives `v_t>=F_k`, and
`F_t>=F_k+v_t>=2F_k`.  QED.

Using the current estimate

\[
 \log_2 ES(t)\le t+O(\sqrt{t\log t}),             \tag{9}
\]

the logarithm of the right side of (5) is

\[
 t^2+O(t^{3/2}\sqrt{\log t}+b\log t),             \tag{10}
\]

whereas the left side has logarithm
`b log_2 n-O(b log b)`.  This proves (1), for example uniformly with a
fixed margin `t<=(1-epsilon)sqrt(b log_2 n)`.  For
`b=Theta(log log n)` this reaches

\[
 k=\Theta(\sqrt{\log n\log\log n}),               \tag{11}
\]

but not the critical ranks of order `log n`.

## 3. The exact exterior-ear decomposition

Let `A` be a convex rank-`r` face, `r>=4`, and let `p` be exterior to
`conv(A)` but blocked for `A`.  Put

\[
 B=\operatorname{ext}(A\cup\{p\}),\qquad
 I=A\setminus B.                                  \tag{12}
\]

The standard tangent geometry gives:

* `I` is a nonempty cyclic interval of `A`;
* `B=(A-I)+p` is convex;
* `I` is convex, being a subset of `A`;
* `I` and `B` are disjoint and
  `|I|+|B|=r+1`; and
* `conv(A)` is strictly contained in `conv(B)`.

Write `E_(r,i)` for the number of these incidences with `|I|=i`.

> **Theorem 2 (constant-two ear encoding).**  For every `r>=4` and
> `1<=i<=r-2`,
> \[
>  \boxed{E_{r,i}\le2v_i v_{r-i+1}.}              \tag{13}
> \]

**Proof.**  Map `(A,p)` to `(I,B)`.  This pair determines

\[
 S=I\mathbin{\dot\cup}B=A\cup\{p\}.              \tag{14}
\]

Every possible root `p` in the fibre belongs to the hull `B` and satisfies
that `S-p=A` is convex.  Thus the roots are hull members of the repair set

\[
 D(S)=\{x\in S:S-x\text{ is convex}\}.            \tag{15}
\]

If `|B|>=4`, the radial-gap proof of the planar repair theorem gives at most
two hull repairs.  If `|I|=1`, deleting its unique member also repairs `S`,
so the general bound `|D(S)|<=3` again leaves at most two hull roots.

It remains to rule out three roots when `B` is a triangle and `|I|>=2`.
Choose distinct `x,y in I`, and write their positive barycentric coordinates
relative to `B={a,b,c}` as `(x_a,x_b,x_c)` and `(y_a,y_b,y_c)`.  The three
ratios

\[
 \rho_a=x_a/y_a,\quad\rho_b=x_b/y_b,\quad
 \rho_c=x_c/y_c                                  \tag{16}
\]

are distinct by general position.  Their `y`-weighted average is one, so
one is the strict middle ratio.  The four-set `{b,c,x,y}` is convex exactly
when `rho_a` is this middle ratio: if it is the minimum then `x` lies in
`conv{b,c,y}`, and if it is the maximum then `y` lies in `conv{b,c,x}`;
the converse follows from the same barycentric calculation.  Hence exactly
one triangle-vertex deletion can leave even the four-point restriction
convex.  Three roots are impossible.

Thus every pair `(I,B)` has at most two preimages.  There are at most
`v_i v_(r-i+1)` possible pairs, proving (13).  QED.

Summing gives the improved convolution bound

\[
 \boxed{
 E_r\le2\sum_{i=1}^{r-2}v_i v_{r-i+1}.}           \tag{17}
\]

The previous direct estimate had coefficient `r-i+1`; (13) removes that
loss completely.  What remains is not root multiplicity but the fact that
`(I,B)` is a pair.  Its union is nonconvex, so in general it cannot be used
as one target face.

For singleton ears there is a second useful exact fact.  The switch
`A -> B=A-a+p` strictly enlarges the convex hull, hence these rank-preserving
switches form a directed acyclic graph.  A fixed target `B` has at most

\[
 2\,|\operatorname{cl}(B)-B|                     \tag{18}
\]

incoming singleton switches, by (13) applied separately to each hidden
singleton.  The ambient factor in (18) can be large, so acyclicity alone
does not yield the required Hall expansion.

There is also a positive fact that is lost by the coarse convolution (17).

> **Theorem 3 (fixed-frame rectangle completion).**  Fix an exterior root
> `p`, its two tangent vertices `x,y`, the source rank `r`, and hidden size
> `i`.  Let `S_f` be any family of incidences having this fixed frame.  Let
> `X_f` be its family of hidden intervals `I`, and let `Y_f` be its family
> of retained faces `R=B-p`.  Then every cross-union
> \[
>  I\cup R,\qquad I\in X_f,\ R\in Y_f,             \tag{RC}
> \]
> is a distinct convex rank-`r` face.  In particular,
> \[
>  \boxed{v_r\ge |X_f||Y_f|\ge |S_f|.}            \tag{RC'}
> \]

**Proof.**  The repair geometry puts every `I` in the open ear triangle
`pxy`; `I+{x,y}` is a convex polygon having `xy` as an edge.  Every
`R in Y_f` lies on the opposite side of the line `xy`, and is another
convex polygon having `xy` as an edge.  Gluing the two polygons along this
common edge leaves every vertex extreme, proving convexity.  The two open
half-planes recover `I` and `R` from their union, so the cross-unions are
distinct.  QED.

Thus a sparse incidence relation inside one frame automatically completes
to a much larger rectangle of genuine source-rank faces.  Quantitatively,
if `|S_f|/(|X_f||Y_f|)<=1/D`, this one rectangle already supplies a factor
`D` of capacity.  The hard fixed-frame case is a nearly complete rectangle.
Across many fixed blockers, such dense rectangles may reuse the same source
coordinates; controlling that reuse is the forward two-ended alignment
problem.  This theorem makes the dichotomy exact but does not by itself
amortize it across crossing frames.

## 4. Exact local obstructions

Two integral configurations isolate the remaining losses.

### 4.1 An arbitrarily large common ear need not give a long extension

Take the convex diamond

\[
 x=(-20,0),\quad a=(2,-10),\quad y=(20,0),\quad z=(1,100)
\]

and points

\[
 p_t=(t,-1000-3t^2),\qquad
 t\in\{-8,-6,-4,-2,1,3,5,7\}.                    \tag{19}
\]

Every `p_t` is exterior blocked for `A={x,a,y,z}` and hides exactly the same
singleton `a`.  Every pair of blockers can replace `a`, so there are 28
rank-five faces of the form `{x,y,z,p_s,p_t}`.  But no three blockers can
replace it while `{x,y,z}` is retained: the blockers form a strict concave
cap and any middle selected blocker lies inside the hull of the two extreme
ones and `z`.

This construction admits arbitrarily many generic rational parameters in a
small interval.  Hence no lemma of the form

> many blockers in one singleton ear force an arbitrarily long convex
> extension retaining the other source vertices

can be true.  The missing capacity is nevertheless visible: the blocker
cloud itself is in convex position.  A successful cumulative proof must be
allowed to restart into that detached face pool.

### 4.2 Dropping the hidden face has unbounded congestion

Conversely, fix one deep hull vertex `p` and put arbitrarily many generic
points `q` in its open ear triangle.  Every

\[
 A_q=(B-p)+q
\]

is convex, `p` is exterior blocked for `A_q`, and

\[
 \operatorname{ext}(A_q+p)=B.                    \tag{20}
\]

The certificate gives an eight-source integral instance.  Thus the raw
map `(A,p)->B` has unbounded inverse multiplicity.  Retaining `I={q}` is
exactly what repairs this collapse and leads to the constant-two theorem.

These examples point in opposite directions: keeping only `B` loses the
source, while insisting on a coface of `A-I` misses the detached cloud.
The pair `(I,B)` is therefore not an artefact of the proof.

## 5. What a first cumulative failure supplies

The cumulative formulation interfaces cleanly with the existing low-degree
reduction.

> **Proposition 3 (first-failure slice).**  Suppose `k>=2b` is the first
> failure of `(CB)_b`, so
> \[
> F_{k+b}<2F_k,
> \]
> while the block inequalities at `k-b` and `k-2b` hold.  Then at least
> `F_k/2` faces have ranks in `(k-2b,k]` and addable degree at most
> `8(k+1)`.  Consequently one rank in this interval contains at least
> `F_k/(4b)` such faces.

**Proof.**  The two preceding block inequalities give

\[
 F_{k-2b}\le F_k/4.                              \tag{21}
\]

On the other hand, double-counting covers and using the failure gives

\[
 \begin{aligned}
 \sum_{r=0}^k\sum_{|A|=r}u(A)
 &=\sum_{s=1}^{k+1}s v_s\\
 &\le(k+1)F_{k+1}
 \le(k+1)F_{k+b}<2(k+1)F_k.                      \tag{22}
 \end{aligned}
\]

At most `F_k/4` faces can therefore have `u(A)>8(k+1)`.  At least
`3F_k/4` faces lie above rank `k-2b` by (21); removing the high-degree
ones leaves `F_k/2`.  Pigeonhole over `2b` ranks.  QED.

Thus failure in the middle range creates precisely a large near-top,
low-addable slice.  The optimized hull-activity theorem then removes its
low-exterior-label part.  Every unresolved source has the required capped
number of exterior ears.  Theorem 2 says that fixing the hidden and outer
faces costs only a factor two, but turning those compatible pairs into
distinct single-face capacity is still the crossing-pocket Hall gate.

In particular, simply inserting (17) into (22) does not close the argument:
bounding the convolution by `V^2` loses a full factor `V`, far more than the
allowed `n^o(1)`.  Rank concentration or cumulative growth at earlier ranks
does not remove that square.  One must either

1. glue a controlled fraction of the compatible pairs into genuine convex
   targets;
2. route balanced pairs recursively while proving that unbalanced ear chains
   spend detached pocket capacity; or
3. prove capped Hall directly for the bipartite compatible-pair graph.

## 6. Verification

Run

```bash
python3 \
  phase2/loop/erdos838/agent_cyclic_stem_hw/ear_map/verify_ear_map.py
```

The checker writes `ear_map_certificate.json`.  It uses only integer
orientation predicates and verifies:

* all 6,439 exterior blocked incidences of the exact 14-point LC
  counterexample;
* 4,320 distinct `(I,B)` pairs and maximum fibre two;
* all 971 fixed root/tangent frames in that configuration and every
  hidden-by-retained cross-union in their rectangle completions;
* the eight-blocker common-ear family, including exactly 28 two-blocker
  replacements and no replacement using three or more blockers; and
* the eight-source common-target star.

The proof of Theorem 2 is symbolic; the census is an independent regression,
not the basis for the theorem.
