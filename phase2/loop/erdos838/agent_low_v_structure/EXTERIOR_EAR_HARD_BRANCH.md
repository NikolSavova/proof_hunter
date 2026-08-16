# Exterior-ear hard branch: a two-face injection and a crossing obstruction

**Date:** 2026-08-14.  All point sets are planar and in general position.

## 1. Verdict

No rankwise Hall bound with congestion `2^(alpha r+o(r))`, `alpha<1`, is
proved here.  Two rigorous facts substantially narrow that target:

1. every exterior blocked incidence has an injective **two-convex-face**
   encoding whose ranks sum to `r+1`; but
2. the `Omega(r^2)` exterior labels supplied by the ACP hard-family lemma do
   not force crossing, distinct, or even differently-ended hidden
   intervals.  A planar configuration can put all `r^2` labels in the same
   ear cell.

Thus an interval-graph or laminar-decomposition proof cannot start from
Lemma 5's scalar exterior mass alone.  It must either exploit the global
constant-density source hypothesis or recurse inside a multiply occupied
replacement cone.

## 2. Exact two-face encoding

Let `A` be a convex `r`-face and let `p` be exterior to `conv(A)` but bad
for `A`.  Define

\[
 I= A\setminus\operatorname{ext}(A+p),\qquad
 B= \operatorname{ext}(A+p).                                    \tag{1}
\]

The cyclic repair theorem gives:

* `I` is a nonempty consecutive interval of `A`;
* `B=(A-I) union {p}` is convex;
* `I` is convex by heredity;
* `I cap B` is empty; and
* `|I|+|B|=r+1`.

> **Lemma 1 (exterior incidence injection).**  The map
> 
> \[
>  (A,p)\longmapsto(I,B,p)                                      \tag{2}
> \]
> 
> is injective into triples in which `I,B` are disjoint convex faces,
> `p in B`, and `|I|+|B|=r+1`.

**Proof.**  Given `(I,B,p)`, recover

\[
 A=I\cup(B-p).
\]

Hence two incidences with the same image are equal. `square`

For a family `S` of convex rank-`r` sources, let

\[
 E(S)=\sum_{A\in S}e(A)
\]

be its exterior blocked-incidence mass.  If `v_j` denotes the total number
of convex `j`-faces, Lemma 1 immediately gives

\[
 \boxed{
 E(S)\le
 \sum_{i=1}^{r-2}(r-i+1)v_i v_{r-i+1}.}                         \tag{3}
\]

The factor `r-i+1` marks `p in B`; dropping disjointness, nesting, and the
interval condition only enlarges the codomain.  Combining (3) with the ACP
hard-family estimate `E(S)>=c r^2|S|` yields the rigorous product-Hall
reduction

\[
 \boxed{
 |S|\le {1\over c r^2}
 \sum_{i=1}^{r-2}(r-i+1)v_i v_{r-i+1}.}                         \tag{4}
\]

This is genuinely stronger structural information than a raw endpoint
tag, but it is not yet the desired Hall map: its target is an ordered pair
of faces rather than one face.  Bounding one factor in (4) by `V(P)` loses
an entire factor `V(P)`, far more than `2^{alpha r}` in the hard regime.

## 3. Quadratic exterior mass need not create crossings

The following construction shows why an interval-overlap theorem cannot be
deduced just from `e(A)=Omega(r^2)`.

Fix `r>=5`, put `M=5r`, `L=M-1`, and take the strictly concave chain

\[
 q_j=(j,j(L-j)),\qquad 0\le j\le L.                              \tag{5}
\]

Let `p=(-1,M^2)`.  Choose a set `X` of `t=r^2` points in a sufficiently
small open neighbourhood of `p`, maintaining general position.  Fix
`0<c<L`.  For every `(r-3)`-subset

\[
 T\subseteq\{q_1,\ldots,q_{L-1}\}\setminus\{q_c\},
\]

put

\[
 A_T=\{q_0,q_c,q_L\}\cup T.                                    \tag{6}
\]

> **Lemma 2 (common-interval quadratic label family).**  There is a choice
> of the neighbourhood of `p` such that all
> 
> \[
>  {5r-3\choose r-3}
> \]
> 
> sets `A_T` are convex rank-`r` faces and satisfy
> 
> \[
> u(A_T)=4r,qquad e(A_T)=r^2.                                  \tag{7}
> \]
> 
> For every `x in X`,
> 
> \[
> \operatorname{ext}(A_T+x)=\{q_0,x,q_L\},
> \qquad I(A_T,x)=A_T\setminus\{q_0,q_L\}.                     \tag{8}
> \]
> 
> In particular, for each source all `r^2` exterior labels induce the
> identical hidden interval and the identical tangent endpoints.  Its
> interval crossing graph has no edges.

**Proof.**  Every subset of the strict concave chain is convex, and every
omitted chain point is addable, giving `u=M-r=4r`.  The calculation from the
common-apex construction gives, for `0<j<L`,

\[
 q_j\in\operatorname{int}\operatorname{conv}\{p,q_0,q_L\};
\]

comparison with the line `pq_L` reduces to `j<M`.  All these containments
are strict and hence persist throughout a sufficiently small neighbourhood
of `p`.  Choose `X` there, avoiding finitely many forbidden lines.  Every
`x in X` then hides every selected chain point except `q_0,q_L`, proving
(8), so all `r^2` apex points are exterior and bad.  There are no other
ambient points, and every omitted chain point is addable, proving (7).
`square`

The same open-cell argument allows `X` to have an arbitrary internal order
type.  Therefore large multiplicity of one interval cannot be controlled
by a special geometric theorem about the fibre: the full planar problem
can recur inside it.

Lemma 2 does not reproduce the ACP hard branch's additional
`|S|=Omega(V(P))` hypothesis; its source family has only
`2^{Theta(r)}` members.  It proves the narrower and important logical
point that **Lemma 5 plus the cyclic interval classification alone cannot
force crossing intervals**.  Any use of constant density must enter as a
separate global ingredient.

## 4. Source-coding implication

For one source in Lemma 2, an interval/endpoint record and the choice of one
of the guaranteed exterior labels use only `O(log r)` bits, but do not
record which of the

\[
 {5r-3\choose r-3}=2^{Theta(r)}                                  \tag{9}
\]

sources was used.  The hidden interval itself contains that source
information; replacing it by its two endpoints discards a linear number of
bits.  This is the same source-code obstruction as the common-onion family,
now with the full `Omega(r^2)` exterior-label count.

The remaining viable dichotomy is consequently:

* use the actual selected vertices of the hidden interval as a target-face
  code; or
* if many labels occupy one ear cell, recurse into that cell while retaining
  the two tangencies.

Merely coloring the interval crossing graph, decomposing it into laminar
subfamilies, or selecting one of `r^2` labels cannot yield an exponent
`alpha<1`.

## 5. Verification

`exterior_ear_verify.py` checks Lemma 1 on complete exact subset censuses and
checks Lemma 2 at `r=5`, using 25 rational apex points and all 231 sources.
It verifies general position, every addable chain point, every blocked apex
point, and the common hidden interval.

```bash
python3 phase2/loop/erdos838/agent_low_v_structure/exterior_ear_verify.py
```
