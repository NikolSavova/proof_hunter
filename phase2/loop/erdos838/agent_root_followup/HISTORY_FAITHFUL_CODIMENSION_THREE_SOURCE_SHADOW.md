# History-faithful codimension-three source shadow

**Date:** 2026-08-15. All face counts are nonempty; record weights are
nonnegative.

## Verdict

The full-compatible-cube regression in
`THIRD_CYCLIC_MERGED_DOWNFACE_HISTORY_LOAD_GATE.md` contains the desired
one-face cubic bank. The prefix-only projection erases the source tails, but
there is no reason to project to prefixes: retain the full selected source
word on each of the three sides and omit one low-completion role per side.

For three binary `q`-role word families this gives exactly

\[
             2^{3q}q^3\quad\hbox{incidences},\qquad
             2^{3q-3}q^3\quad\hbox{ordinary outputs},
             \qquad\hbox{load }8.                       \tag{1}
\]

In the exact rational `q=3` cyclic blocker these are `13,824` incidences
and `1,728` distinct ordinary faces, every one of load eight. Thus the
claimed cubic one-face load cancellation is false for the complete
source-word geometry. The earlier prefix calculation remains correct only
for the artificially restricted prefix-output alphabet.

The general theorem is a conditional interface: it applies whenever the
merged rooted complexes contain the almost-full selected source words. A
live survivor must therefore be **source-thin** in at least one component,
have large physical completion codegree in the omitted roles, or have a
large residual seam/history load. No unrestricted half-coefficient closure
is claimed.

## 1. Exact role-coloured shadow lemma

Let the physical ground be split into three disjoint role systems

\[
             \mathcal X^a=(X^a_1,\ldots,X^a_{q_a}),
             \qquad a=1,2,3.                            \tag{2}
\]

A record `r` carries a transversal word
`w^a_r={x^a_{r,i}:1<=i<=q_a}` in each system and a fixed visible seam
`Y_r`. Choose role sets `I_a subset [q_a]`. Assume that for every record
and every `(i,j,k) in I_1 times I_2 times I_3`,

\[
 O(r;i,j,k)=Y_r\cup(w^1_r-\{x^1_{r,i}\})
                    \cup(w^2_r-\{x^2_{r,j}\})
                    \cup(w^3_r-\{x^3_{r,k}\})          \tag{3}
\]

is an ordinary face. Let `Delta_3` be the actual weighted load of (3),
including all physical completions and every external history collision.

> **Theorem 1 (codimension-three source shadow).** If the record mass is
> `W`, then
> \[
>                 W|I_1||I_2||I_3|\le\Delta_3 V(P).     \tag{4}
> \]

This is just incidence counting, but its decoder is exact: the output
occupancy reveals the three omitted roles, and the retained physical labels
reveal every other role choice. If the full words together with the seam
have residual history load at most `Lambda`, then

\[
       \Delta_3\le\Lambda
       \max_{(i,j,k)\in I_1\times I_2\times I_3}
                    |X^1_i||X^2_j||X^3_k|.              \tag{5}
\]

In particular, binary roles and simple literal histories give

\[
                       V(P)\ge {Wq_1q_2q_3\over8}.       \tag{6}
\]

For complete role products, the sharper exact output count is

\[
 W\left(\sum_{i\in I_1}{1\over |X^1_i|}\right)
  \left(\sum_{j\in I_2}{1\over |X^2_j|}\right)
  \left(\sum_{k\in I_3}{1\over |X^3_k|}\right),        \tag{7}
\]

because outputs with different omitted-role triples have different
occupancy masks and a fixed triple has exactly the product of the three
omitted alphabet sizes as completion load.

## 2. Application to the rational cyclic blocker

In the exact construction, the seam is

\[
                         Y=\{a,y,z,b\}.                 \tag{8}
\]

Every subset of each selected left, right, and third-ear word merges with
`Y`. Hence (3) is ordinary for all role triples. For `q=3`, direct exact
enumeration gives

\[
 \begin{array}{c|r}
 \text{complete source triples}&512\\
 \text{codimension-three incidences}&13824\\
 \text{distinct merged faces}&1728\\
 \text{minimum/maximum output load}&8/8.
 \end{array}                                           \tag{9}
\]

The output itself identifies the seam and every retained source label.
Only the three omitted binary labels remain, so the factor eight is sharp.

At the fixed-gap ledger, each of the two blocker sides has `L` binary
roles followed by `L/4` large roles, and the common ear has `L` binary
roles. Retain **all** selected large-role labels and omit one binary role
on each of the three sides. If `M` is the complete-source record count,
then

\[
                         V(P)\ge {ML^3\over8}.           \tag{10}
\]

This is exactly the missing `K=3` polylogarithmic multiplier. Therefore
the displayed full-compatible-word construction is a positive equality
model, not a barrier to the one-face operation.

## 3. Exact remaining scope

The theorem does not assert that a general live double-bad record has
property (3). In the adaptive-release language, (3) requires the rooted
cap/cup/common-ear complexes to contain the selected source words after
only one low-codegree omission per component. The previous maximum-child
prefix theorem guarantees only fixed prefixes, not the variable tails.

Accordingly the corrected fork is:

1. **almost-full branch:** (3) holds on three role reservoirs with
   `|I_a|=Theta(L)` and completion/history load `L^{o(1)}`; then (4)
   supplies the needed cubic one-face bank;
2. **source-thin branch:** at least one rooted compatibility complex rejects
   almost every almost-full selected word; its first missing physical label
   gives a continuation-bearing blocker/profile record; or
3. **high-codegree branch:** many completions or histories share the same
   almost-full merged output, producing the literal dense face--face core
   already isolated by the Renyi/Hall reductions.

The important correction is that erased maximum-child tails are not an
intrinsic obstruction when the full released words are geometrically
compatible. Almost-full role-coloured shadows retain those tails at constant
load.

## 4. Verification

Run

```text
python3 phase2/loop/erdos838/agent_root_followup/verify_history_faithful_codimension_three_source_shadow.py
```

The verifier reuses the exact rational cyclic blocker, exhausts all
codimension-three outputs, checks convexity and uniform load eight, verifies
the complete-product formulas for unequal alphabets, and checks the fixed-gap
`ML^3/8` ledger.
