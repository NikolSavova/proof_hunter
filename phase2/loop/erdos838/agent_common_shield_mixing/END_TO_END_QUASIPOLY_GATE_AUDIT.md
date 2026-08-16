# End-to-end audit: the triangle tag closes the last dense context, not the half theorem

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

`QUASIPOLY_SOURCE_TRIANGLE_TAG_CLOSURE.md` genuinely closes the final
source-compressed dense rectangle at the
`n^(Theta(log log n))` scale.  It does **not** yet prove

\[
                         \log f(n)\ge(1/2-o(1))(\log n)^2.         \tag{1}
\]

The fixed-gap implication is conditional on an upstream promotion which
has not been proved for an arbitrary minimizer.  In its shortest honest
form, the new theorem says:

> **Closed terminal implication.**  Suppose a weighted hard family has
> already been partitioned into canonical dyadic simple bipartite label
> contexts with ordinary old-source targets, common layer weights, total
> demand
> 
> \[
>                              M\ge n^{\sigma\log\log n}V(P),       \tag{2}
> \]
> 
> and compressed actual source load `kappa_A=n^O(1)`.  Then the family is
> impossible for all sufficiently large `n`.

Indeed the source--triangle tag theorem gives

\[
 M\le \kappa_A\left(5+{3\over\sqrt5}n^{3/2}\right)V(P),           \tag{3}
\]

contradicting (2).  This remains true after fixing any one-direction
triangle star, signed `2+2`/`3+1` class, base type, physical child, or
chronology mark.

What is still open is the derivation of the hypotheses in the boxed
terminal implication from the rank-safe minimizer slice.  There are two
principal missing promotions and one load audit:

1. extract a quadratic-mass complete same-type/product chart from the
   weighted source--pocket incidences, or pay its failure by an already
   decoded one-face bank;
2. in the rooted bad-pair/endpoint branch, prove that all high-load mass
   either exits through an attached/detached/source-mask bank or becomes a
   coalesced label-by-label dense rectangle; and
3. prove that the actual noncoalescible description load `L` at that
   rectangle is polynomial, so that `kappa_A<2L=n^O(1)`.

Each is explicitly conditional or open in the banked reports.  Therefore
the present result closes equation `(3az30t6c)` and its fixed-triangle
continuation, but the unrestricted Erdős 838 lower coefficient remains
`1/4`, not `1/2`.

## 1. The fixed-gap minimizer start is rigorous

Fix `delta>0`, put

\[
                         c={1\over2}-\delta,\qquad L=\log n,       \tag{4}

\]

and suppose `n` is the least counterexample to
`f(n)>=2^{c(log n)^2}`.  Let `P` attain `f(n)`, let `V=V(P)`, let `mu` be
the mean rank of its ordinary faces, and let `R` be their maximum rank.

Every deletion `P-p` has at least `2^{c(log(n-1))^2}` faces.  Since

\[
 \sum_{p\in P}V(P-p)=\sum_{F\in\mathcal F(P)}(n-|F|)=V(n-\mu),    \tag{5}

\]

minimality gives

\[
 \mu\le n\left(1-2^{-c(L^2-(\log(n-1))^2)}\right)=O(L).          \tag{6}

\]

Also one maximum face contributes all its subfaces, so

\[
                              2^R\le V<2^{cL^2},\qquad R<cL^2.    \tag{7}

\]

Thus the low-mean/max-rank assumptions in
`MINIMIZER_WEIGHTED_LOOP_COVER_GATE.md` are consequences of fixed-gap
minimality, not extra conjectures.

That report then proves a rank-`O(L)` weighted family of canonical marked
sources of mass `Omega(V)`, with weight at most one over each actual
source, and a deterministic rooted pocket of size

\[
                         m\ge {n-2\mu\over8(R-2)\mu}
                             ={n\over\operatorname{polylog}n}.     \tag{8}
\]

Strong induction inside the pocket supplies

\[
 V(P|X_T)\ge f(m)ge
     2^{c(L-O(\log L))^2}=2^{cL^2-O(L\log L)}.                    \tag{9}

\]

Finally `GLOBAL_MARKED_POCKET_RELEASE.md` is exact: a source guard of
size `g` has decoder load

\[
                         {n\choose3}\sum_{i=0}^g{n\choose i},      \tag{10}

\]

so for every fixed `gamma<c`, almost every marked source has guard
transversal number greater than `gamma L`, and hence a matching of
`Omega(L)` disjoint outer circuit traces.  Equations (5)--(10), including
the genuine weighted source cap, are a proved fixed-gap entrance.

## 2. First open promotion: incidences to a complete product chart

The matching in Section 1 lives inside each source/root incidence.  The
later blocker-cover and seam theorems instead assume disjoint coordinate
roles `X_1,...,X_q` and a complete same-type singleton product, with a
quadratic weighted family of selected words and a recoverable pocket/base
state.

No banked theorem derives this object from all rank-safe marked
incidences.  The exact partial results are:

* `REDUNDANCY_CHARGED_SEMIALGEBRAIC_RETENTION.md` retains
  `2^{-O(q+R_supp)}` selected mass **after** a word family and its
  coordinate supports have been supplied.  It does not create the
  coordinatization.
* In low support redundancy it gives a homogeneous singleton container,
  but `SAME_PARENT_RETENTION_PROFILE_SPLICE.md` proves that this does not
  manufacture compatible multi-point seam jets.  Its rational `R=0`
  example kills that inference.
* In high support redundancy, the proposed payment uses an already valid
  detached one-gap/profile bank.  Arbitrary nonseparated children need not
  have that bank; the m=14 strong-separation counterexample rules out the
  naïve replacement.
* `MINIMIZER_WEIGHTED_LOOP_COVER_GATE.md`, Theorem 2, is explicitly
  conditional on rooted complete-product charts of total mass
  `M>=eta V` and aggregate released-output load `Lambda`.  The report says
  that the current minimizer reductions do not supply a complete-product
  extraction with `Lambda=2^{o(L^2)}`.

This is the earliest decisive gap.  The triangle-tag theorem begins much
later and does not address it.

## 3. Exact branches inside a supplied complete product

Assume temporarily that the missing chart and its actual global decoder
have been supplied.  The following local branch tree is rigorous.

### 3.1 Blocker cover

For a local pocket face `F`, `BLOCKER_ROLE_COVER_RELEASE_DICHOTOMY.md`
constructs the looped blocker graph on external roles.

* A low-cost vertex cover deletes roles and releases the whole `F`; its
  occupancy mask gives the exact local bank.
* High mean cover cost becomes either mandatory `3+1` loop entropy or a
  fractional packing of `2+2` traces.

The local dichotomy is exact.  Its **global** use still assumes the
aggregate output load in the preceding section.  The all-loop parabola
regression shows that high cover cost need not produce any `2+2` matching.

### 3.2 Strong reset or a linear bad-pair matching

`MIXED_SEAM_VERTEX_COVER_PI2_GATE.md` is exact under its balance
hypotheses: `q=Theta(L)` macroscopic roles of size `n^{1-o(1)}`.

* If a linear number of role graphs have small bad-pair covers, deletion
  gives a strong chain.  The fixed-gap induction input and the conditional
  strong-chain reset preserve coefficient `c` with only `O(L log L)`
  loss.
* Otherwise a linear number of roles each contain `Omega(n/q)` disjoint
  bad repeated pairs.

What has not been proved upstream is that every high-cover chart can be
balanced into these macroscopic role hypotheses while retaining the
required weighted context mass and decoder.  The theorem itself is sound.

### 3.3 Rank-four classification

`BAD_PAIR_RANK4_PIQ_CLASSIFICATION.md` loses only a constant: every marked
pair with two canonical neighbors is convex or lies in one of four rooted
`1+3` classes.  `CONVEX_BAD_PAIR_EAR_PROMOTION.md` proves that the convex
class is a genuine commuting pair-ear class.

The warning is essential.  Its
`(log n)^{Theta(log n)}=n^{Theta(log log n)}` faces are an **absolute**
singleton/ear bank.  They are the needed relative multiplier only when a
separate released base/pocket context coexists and the output has controlled
global load.  This coexistence is not supplied by the rank-four theorem.

## 4. Second open promotion: endpoint circuits to the dense rectangle

`ENDPOINT_POCKET_CODEGREE_DICHOTOMY.md` gives the exact next split for a
released base `B union F` and a marked pair.

1. Attached-compatible endpoints give ordinary `B union F union {v}`
   outputs, conditional on their actual aggregate load.
2. Detached-compatible endpoints have the unconditional Hall targets
   `F union {v}`, `B union {v}`, and `B union F` (plus the old source
   `A`).  Low Hall density closes linearly.
3. High ordered-pair load fixes `(B,F,v,e)` and descends to actual source
   masks/chronology.
4. Double detached incompatibility gives two pocket-only circuits.

This report explicitly calls the result a reduction, not a closure.
The fixed-pair source-mask and genuine-history theorems close canonical
weighted fibres, but raw/global base reuse may remain.  The double-circuit
branch has a polylogarithmic common-signature normalization in
`DOUBLE_ENDPOINT_POCKET_SIGNATURE.md`; that report explicitly says it is
not a release theorem.

The subsequent four/five-target Hall reports are exact **once** their
record family is present.  They show that a low-density source--release
graph closes, while a high-density core is a literal old-source by
released-face incidence graph.  What is not yet proved for every rooted
fan/cage branch is a lossless promotion to the special label-level object
needed below:

* simple bipartite contexts with one common layer weight;
* active sides represented by actual label clouds, so rank-three tags are
  available;
* total hard demand `>=n^(sigma log log n)V`; and
* polynomial actual description load after all base, root, tangent, cover,
  mask, and chronology states are coalesced.

The exact anti-aligned rectangles prove that Hall density and the five
targets alone do not supply a cross-profile product.  The new tag theorem
removes that **last** profile issue, but it does not create the rectangle
or prove the four bullets.

## 5. The terminal dense-context branch is now complete

Suppose the four bullets in Section 4 do hold.  Dyadically bucket each
source star, coalesce all release neighbors with the same actual state, and
enter the source target once per nonempty layer.  Genuine canonical source
weight gives

\[
                              \kappa_A<2L_{desc}.         \tag{11}

\]

Here `L_desc` must be the **proved actual** description load.  The fact
that canonical radial depth is decoded by `(A,e)` removes one possible
factor; it does not automatically bound all cover/mask/base histories.

For each context with `a` source rows, larger side `t`, and `e` records,

\[
                           a{t\choose3}\ge {5\over54}e^2.           \tag{12}

\]

Pair each triangle incidence with one canonical source face.  There are
at most `V(P){n choose3}` pairs and each has load at most `kappa_A`, giving
(3).  If `L_desc=n^O(1)`, then the entire terminal family has only
`n^O(1)V` weight, contradicting its required
`n^(sigma log log n)V` mass.

The fixed-`T` one-direction star, all sixteen circuit signatures, arbitrary
base order types, SCC cycles/DAGs, and coherent projective itineraries are
subfamilies of this estimate.  They require no further branch.

## 6. Scale bookkeeping and the exact conclusion

Passing from a pocket of size `n/polylog n` back to scale `n` loses
`O(L log L)` bits in (9).  A multiplier

\[
                         n^{\sigma\log\log n}
                         =2^{\sigma L\log L}             \tag{13}

\]

with a sufficiently large fixed `sigma` repairs that loss.  The
`n^(3/2)` tag cost in (3) is only `2^{O(L)}` and is therefore harmless.

If Sections 2 and 4 were proved with uniform constants and
`L_desc=n^O(1)`, the fixed-gap induction would establish
`f(n)>=2^{(1/2-delta)(log n)^2}` for every fixed `delta>0`; combined with
the known half-coefficient construction, this would solve the limit with
coefficient `1/2`.

They are not presently proved.  The honest status is therefore:

\[
 \boxed{
 \begin{array}{l}
 \text{rank-safe minimizer/pocket entrance: proved;}\\
 \text{complete-product and context-coexistence promotion: open;}\\
 \text{dense source--triangle terminal gate: proved at quasipolynomial scale;}\\
 \text{unrestricted lower coefficient }1/2:\text{ not proved.}
 \end{array}}                                            \tag{14}
\]

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_end_to_end_quasipoly_gate_audit.py
```

The checker audits the exact deletion identity, the fixed-gap mean-rank
bound, the maximum-rank/downset bound, the pocket scale, the
`O(L log L)` recovery exponent, and the polynomial-versus-quasipolynomial
terminal comparison.  It also checks the dependency ledger and refuses to
mark the half theorem closed while either promotion node remains open.

