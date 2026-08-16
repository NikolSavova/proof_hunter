# Circuit transversals or an outer toggle shield

**Date:** 2026-08-14.  All logarithms are base two.  This note starts from
the outer--internal mixed-bank setup in
`../agent_outer_internal_product/OUTER_INTERNAL_MIXED_BANK.md`.

## Verdict

The concentrated four-circuit branch has an exact additional dichotomy.
If the outer traces of all bad `2+2` and `1+3` circuits in a context have a
small transversal, deleting it releases the *entire* common internal
reservoir.  The released mixed banks have global overlap at most

\[
                    L_t=\sum_{i=0}^t {n\choose i}.             \tag{1}
\]

Consequently, for cells of size `D^2`, a first bank of size at least `2D`
and overlap `Lambda`, and an internal reservoir of size `H`, the
small-transversal contexts satisfy

\[
 |G_{\rm tr}|\le
 D^{3/2}\sqrt{{\Lambda L_t\over2H}}\,V(P).                    \tag{2}
\]

Thus the branch closes fixed-power EIC' whenever
`H/(Lambda L_t)>=D^(1+2 epsilon)`.  In the quadratic reservoir regime
`log H=a(log D)^2+o((log D)^2)`, any
`t<=gamma log D` with

\[
 \gamma\,{\log n\over\log D}<a-o(1)                          \tag{3}
\]

gives much more than a fixed-power saving (and permits the harmless linear
term in the exponent required by (2)).  This rigorously closes every
concentrated-circuit cell whose defect is controlled by a sufficiently
small outer guard set.

If there is no such transversal, the residual is not an amorphous circuit
concentration.  The outer traces contain more than `t/2` pairwise disjoint
singletons/pairs.  Their union is a convex outer shield, and the `D`
one-point source extensions turn its Boolean complex into a source-tagged
toggle bank.  Either that bank already closes EIC', or one ordinary face
has a large fibre which canonically produces a family of distinct
rank-`<=2m` outer completions over one common retained base.  This is a
strictly narrower common-base shield child.

This does **not** finish the matching child.  The sparse guard-pair model
from the outer--internal report can have transversal number equal to the
entire carrier rank because of `1+3` circuits.  In that model the resulting
outer completion family lies in a complete convex cloud and pays globally.
The still-missing theorem must obtain the analogous released shield payment
for an arbitrary quadratic-entropy carrier family.

## 1. Circuit traces and guard release

Let `P=O disjoint_union X`, and let `R_c subset O` be distinct ordinary
outer carriers.  Let `H subset F(P)` be a common family of ordinary faces
contained in `X`.  Assume the one-point compatibility condition

\[
 R_c\cup\{x\}\in F(P)
 \quad(c\in[C],\ x\in\bigcup H).                              \tag{4}
\]

For every bad split circuit `T union S`, where

\[
 T\subseteq R_c,\quad S\subseteq X,\quad
 (|T|,|S|)\in\{(2,2),(1,3)\},\quad
 S\subseteq F\text{ for some }F\in H,                        \tag{5}
\]

call `T` its **outer trace**, and let `B_c` be the family of all such
traces.  A transversal is a set `G_c subset R_c` meeting every member of
`B_c`.

> **Theorem 1 (outer circuit-transversal release).**  If `G_c` is a
> transversal, then
> \[
>                 (R_c-G_c)\cup F\in F(P)\qquad(F\in H).      \tag{6}
> \]
> If `|G_c|<=t` for every context in a family `C_tr`, the mixed banks
> \[
> M_c=\{(R_c-G_c)\cup F:F\in H\}                              \tag{7}
> \]
> have size `H` and global overlap at most `L_t` from (1).

**Proof.**  If a union in (6) were nonconvex, planar Caratheodory would
give a nonconvex four-subset.  It cannot lie wholly in either factor.  It
cannot use three outer points and one internal point by (4) and deletion.
Its split is therefore `2+2` or `1+3`.  Its outer trace is disjoint from
`G_c`, contradicting the transversal property.  This proves (6).

The label partition recovers `F=U cap X` and
`B=U cap O=R_c-G_c` from a mixed face `U`.  Since the carriers are
distinct, a context containing `U` is determined by a set
`G subset O-B` of size at most `t`; there are at most `L_t` such sets.
This proves the overlap claim.  QED.

The use of *all* bad traces in (5) is essential.  Choosing one convenient
witness for each failed union does not imply (6), because another circuit
can survive the proposed guard deletion.

## 2. Exact fixed-power estimate

Suppose each context has `|G_c|=D^2` records and a first ordinary-face bank
`A_c` with `|A_c|>=2D`.  Suppose a fixed ordinary face belongs to at most
`Lambda` first banks.  The notation `G_c` for records in this paragraph is
unrelated to the guard set of Theorem 1.

> **Theorem 2 (small-transversal discharge).**  For the contexts admitting
> guards of size at most `t`,
> \[
> |G_{\rm tr}|\le
> D^{3/2}\sqrt{{\Lambda L_t\over2H}}\,V(P).                   \tag{8}
> \]
> In particular, if
> \[
>                    H\ge {1\over2}\Lambda L_t
>                              D^{1+2\epsilon},               \tag{9}
> \]
> then `|G_tr|<=D^(1-epsilon)V(P)`.

**Proof.**  In each cell,

\[
 |G_c|^2=D^4\le {D^3\over2H}|A_c||M_c|.                     \tag{10}
\]

The recoverable-cell Cauchy telescope and the overlap bounds `Lambda,L_t`
give (8).  Substitution of (9) gives the last assertion.  QED.

For (3), use

\[
 \log L_t\le t\log(en/t)
       =\left(\gamma{\log n\over\log D}+o(1)\right)(\log D)^2. \tag{11}
\]

Thus the coefficient gap in (3) dominates every fixed linear power of
`D`, including (9).

## 3. The complementary matching is an outer shield

The trace family `B_c` is a hypergraph of rank at most two.  Let `tau_c`
be its transversal number and `nu_c` its maximum matching number.

> **Lemma 3 (trace matching).**
> \[
>                         \tau_c\le2\nu_c.                   \tag{12}
> \]
> Consequently `tau_c>t` gives more than `t/2` pairwise disjoint bad outer
> traces.

**Proof.**  The union of the members of a maximal matching meets every
trace; otherwise the disjoint trace could be appended.  The union has at
most twice the matching size.  QED.

Fix a matching `T_1,...,T_m`, put `W_c=union_i T_i`, and assume as in the
one-pocket application that there are `D` distinct internal labels `x`
for which `R_c+x` is a source face.  Since `W_c subset R_c`, every set

\[
       (R_c-W_c)\cup Z\cup\{x\},
       \qquad Z\in{W_c\choose\lfloor|W_c|/2\rfloor},         \tag{13}
\]

is an ordinary face.  There are at least
`D2^|W_c|/(|W_c|+1)` of them in the context, with
`m<=|W_c|<=2m`.

> **Theorem 4 (matching-toggle dichotomy).**  Let `Omega` be the maximum
> number of banks (13) containing one ordinary face, over a family of `C_m`
> matching contexts with `|W_c|>=m`.  Their `C_mD^2` selected records obey
> \[
>             C_mD^2\le(2m+1)D\Omega2^{-m}V(P).              \tag{14}
> \]
> Hence `Omega<=2^mD^{-epsilon}/(2m+1)` closes this branch with saving
> `D^epsilon`.  Otherwise a single ordinary face `U` yields more than
> `2^mD^{-epsilon}/(2m+1)` distinct completion faces
> \[
>                 Q_c=R_c-(U\cap O),\qquad
>              m/2\le |Q_c|\le m,                            \tag{15}
> \]
> of one common rank over the common base `U cap O`; every
> `(U cap O) union Q_c=R_c` and its one-point source extension are ordinary
> faces.

**Proof.**  The largest binomial layer of a `w`-set has size at least
`2^w/(w+1)`.  Double-counting (13) therefore gives
`C_mD2^m/(2m+1)<=Omega V`, which is (14).  In a common output `U`, the unique
internal source label is `U cap X`, so it is fixed across the fibre.  Also
`U cap O=R_c-Q_c`.  Distinct carriers give distinct `Q_c`, and (15) and
the common-base assertion follow.  Finally all carriers have the same rank,
so

\[
 |Q_c|=|R_c|-|U\cap O|
 \]

is constant across the fibre.  Since
`|Q_c|=ceil(|W_c|/2)` and `m<=|W_c|<=2m`, it lies between `m/2` and `m`.
QED.

Theorem 4 is useful because the matching alternative is now a
rank-`O(log D)` common-base completion family, not the original arbitrary
outer--internal incidence layer.  Closing that heavy completion family is
the remaining matching-shield theorem.

## 4. Sparse-model cross-audit

In the exact 26-point carrier/20-point internal-chain instance used by the
outer--internal verifier, every one of the six carrier labels occurs as the
singleton outer trace of a bad `1+3` circuit.  Hence

\[
                         \tau=\nu=6.                         \tag{16}
\]

This kills any claim that the canonical insertion edge alone is always a
transversal of *all* split circuits.  The model nevertheless has 56
carriers cut from one convex lower cloud.  Its matching-toggle completion
family is therefore contained in the Boolean complex of that cloud, the
released shield which makes it harmless for EIC'.  The audit is exactly
consistent with Theorems 1--4: it lands in the heavy completion alternative,
not in the small-transversal branch.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_circuit_transversal_toggle.py
```

The checker exhausts rank-two trace hypergraphs, checks (12), audits the
integer Cauchy and toggle inequalities, and reconstructs the rational sparse
guard-pair model to verify (16) and the complete bad-trace list.
