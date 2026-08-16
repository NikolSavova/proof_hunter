# Low-count structural regularization: an almost-sharp obstruction

**Date:** 2026-08-14.  All logarithms are base two.  Write `W(P)` for the
number of nonempty convex-position subsets of a planar point set `P`.

## 1. Headline

Low convex-subset count, even with quadratic coefficient arbitrarily close
to the conjectural optimum `1/2`, does **not** force a near-spanning
decomposable subset.  In fact it does not force a decomposable subset left
after deleting `o(n)` points.

> **Theorem (guarded-template obstruction).**  For every `epsilon>0` there
> are a constant `alpha=alpha(epsilon)<1` and arbitrarily large stretchable
> planar point sets `Q` such that
> 
> \[
>  \log W(Q)\le (1/2+\epsilon)(\log |Q|)^2+O_\epsilon(\log |Q|),       \tag{1}
> \]
> 
> but every mirror-decomposable subset `D` of `Q` satisfies
> 
> \[
>  |D|\le |Q|^\alpha.                                                \tag{2}
> \]

Thus each such `Q` requires deletion of `|Q|-o(|Q|)` points before it
becomes mirror-decomposable.  This falsifies the first proposed
regularization target in `agent_asymptotic/FULL_REGULARIZATION_TRANSFER.md`,
even under an almost-best-possible low-count hypothesis.

The proof is elementary once one combines the paper's exact substitution
formula with a six-point indecomposable guard.

## 2. Two hereditary facts

Recall that `A \prec B` is the mirrored strong glue used in the paper.

> **Lemma 1.**  The class of mirror-decomposable point sets is hereditary.

**Proof.**  Restrict a decomposition tree to the chosen subset.  At a node
`A \prec B`, strong separation is inherited by `A' subset A` and
`B' subset B`.  Suppress an empty child, and proceed inductively in every
nonempty child. `square`

The following observation is the engine of the construction.

> **Lemma 2 (indecomposable template throttles extraction).**  Let `S` be
> an indecomposable `r`-point template, and form the homogeneous vertical
> iterates
> 
> \[
>  Q_0=\{q\},\qquad Q_d=S[Q_{d-1}].                                \tag{3}
> \]
> 
> Then every mirror-decomposable subset of `Q_d` has size at most
> `(r-1)^d`.

**Proof.**  Let `M_d` be the largest possible size of such a subset, and
let `D subset Q_d` be mirror-decomposable.  If `D` meets all `r` top-level
blocks, choose one point of `D` from each block.  This transversal has order
type `S`, while by Lemma 1 it is mirror-decomposable.  That contradicts the
choice of `S`.  Hence `D` meets at most `r-1` top blocks.  Its intersection
with each block is again mirror-decomposable by Lemma 1 and has at most
`M_{d-1}` points.  Therefore

\[
 M_d\le(r-1)M_{d-1},\qquad M_0=1,
\]

which proves `M_d<= (r-1)^d`. `square`

This argument needs no alignment between a decomposition of `D` and the
substitution blocks.  Heredity plus one transversal is enough.

## 3. An explicit six-point guard

Take the following six rational points in increasing `x`-order:

```text
(-10,-13), (-6,5), (-2,-13), (1,-10), (14,-10), (18,2).          (4)
```

Call this order type `G`.  It is indecomposable even if one allows an
arbitrary candidate leaf order rather than keeping the displayed
`x`-order.

> **Lemma 3 (six-point guard).**  `G` is not mirror-decomposable.

**Finite proof.**  A mirror decomposition determines a total leaf order.
For each of the `6!=720` orders, test its five possible root cuts.  At a cut
after position `j`, the `\prec` rule requires every triple with its first
two points on the left to have sign `-`, and every triple with its last two
points on the right to have sign `+`; then apply the same test recursively
to both intervals.  Exact integer determinants for (4) give the following
complete dynamic-programming census:

| subset size | ordered sequences | recursively decomposable sequences | decomposable subsets |
|---:|---:|---:|---:|
| 1 | 6 | 6 | 6 of 6 |
| 2 | 30 | 30 | 15 of 15 |
| 3 | 120 | 120 | 20 of 20 |
| 4 | 360 | 150 | 15 of 15 |
| 5 | 720 | 50 | 6 of 6 |
| 6 | 720 | **0** | **0 of 1** |

This exhausts all binary `\prec` trees and proves the lemma.  The verifier
implements precisely this recurrence. `square`

## 4. Guarding an almost-optimal Pascal template

Let

\[
 P_k=T_{2k-4,k-2},\qquad
 R_k=|P_k|={2k-4\choose k-2}.                                    \tag{5}
\]

The paper proves that the largest cap and cup in `P_k` both have size
`k-1`.  Inflate the first point of `G` by a sufficiently small vertical
copy of `P_k`, and inflate its other five points by singletons.  Denote the
resulting rational point set by

\[
 S_k=G[P_k,1,1,1,1,1],\qquad r_k=|S_k|=R_k+5.                    \tag{6}
\]

Every transversal of these six guard blocks has order type `G`.  If `S_k`
were mirror-decomposable, Lemma 1 would make such a transversal
mirror-decomposable, contradiction.  Hence `S_k` is indecomposable.

Let `a_k,b_k` be its largest cap and cup sizes.  The exact composition
classification sharpens the crude additive-three bound.  Since the
`P_k` block is the first guard block, it may be multiply occupied by a cap
but not by a cross-block cup.  The largest guard cap through that block uses
two further guard points; that point is not the last point of any
nonsingleton guard cup.  Consequently, for `k>=5`,

\[
 a_k=k+1,\qquad b_k=k-1,
 \qquad a_k+b_k-2=2k-2.                                        \tag{7}
\]

Now iterate this fixed guarded template:

\[
 Q_{k,0}=\{q\},\qquad Q_{k,d}=S_k[Q_{k,d-1}].                    \tag{8}
\]

All finite iterates have rational realizations: choose each vertical scale
smaller than the finitely many strict determinant thresholds at that level.
The exact fixed-template proposition in the paper gives

\[
 \log W(Q_{k,d})
 = {a_k+b_k-2\over2\log r_k}(\log |Q_{k,d}|)^2+O_k(\log|Q_{k,d}|). \tag{9}
\]

By (6), its coefficient is exactly

\[
 c_k={k-1\over\log\left({2k-4\choose k-2}+5\right)}
     ={1\over2}+O\left({\log k\over k}\right).                 \tag{10}
\]

Choose `k=k(epsilon)` so that `c_k<=1/2+epsilon`.  This proves (1).
On the other hand Lemma 2 gives

\[
 |D|\le(r_k-1)^d
      =|Q_{k,d}|^{\alpha_k},\qquad
 \alpha_k={\log(r_k-1)\over\log r_k}<1,                         \tag{11}
\]

which proves (2).

Notice that the paper's cup--cap template barrier also gives a lower
coefficient `1/2` for every fixed template.  Thus the guarded towers really
sit in the window `[1/2,1/2+epsilon]`; (1) is not obtained by allowing a
wildly larger low-count constant.

## 5. Consequences for the live route

### 5.1 Exact or deletion-based regularization is closed

The following implication is false for every fixed `C>1/2`, even if `C` is
arbitrarily close to `1/2`:

```text
log W(P) <= C(log n)^2
    => P contains a decomposable n^(1-o(1))-point subset.
```

It also remains false if “contains” is replaced by “becomes decomposable
after deleting `o(n)` points.”  For a fixed guarded template, (11) is
`o(n)`.

### 5.2 A family-of-pieces theorem must have quadratic multiplicity

Suppose a proposed transfer merely sums the guaranteed internal mass of a
family of decomposable pieces of size at most `n^alpha`.  The sharp
decomposable theorem supplies at most the target scale

\[
 2^{(\alpha^2/2+o(1))(\log n)^2}
\]

per piece.  To reach coefficient `1/2` by addition alone, one therefore
needs at least

\[
 2^{((1-\alpha^2)/2-o(1))(\log n)^2}                            \tag{12}
\]

pieces with essentially disjoint charged outputs.  Polynomially or even
`2^{o((log n)^2)}` many extracted pieces cannot repair the loss for any
fixed `alpha<1`.

Equation (12) does not rule out a genuinely weighted family theorem, but it
sets its unavoidable scale.  Such a theorem must exploit cross-piece
convex subsets or quadratically many compatible histories; it cannot be a
cover by a modest number of exact strong pieces.

### 5.3 What survives

The obstruction points away from structural extraction and toward the two
currently sharp global formulations:

1. the half-weight/Tutte inequality
   `n Z_P(1/2) <= 2 Z_P(1)` (or its asymptotic version); and
2. the rank-extension estimate
   `p_r >= 2^{-r-o(r)}` for `r <= (1-o(1))log n`.

An “approximate decomposition” can still be useful only if its defects are
charged directly to new convex subsets.  Approximation measured by deleting
exceptional points is ruled out by the guarded towers.

## 6. Verification artifact

`guarded_template_verify.py` checks all `720` guard leaf orders and their
recursive cuts with exact integer determinants, constructs the Pascal signs
recursively, forms the guarded abstract composition, computes largest caps
and cups by dynamic programming, and reports the obstruction exponent
`log(r-1)/log(r)` and coefficient `(k-1)/log r`.

Run:

```bash
python3 phase2/loop/erdos838/agent_low_v_structure/guarded_template_verify.py
```

The program is a check of the finite combinatorics, not a premise of the
proof.
