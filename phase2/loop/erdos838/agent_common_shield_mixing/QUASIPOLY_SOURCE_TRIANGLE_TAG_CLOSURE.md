# A source face plus one triangle tag closes the quasipolynomial Hall deficit

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The fixed-triangle one-direction star, including arbitrary low-face/product
bases, is already closed at the live
`K=n^(Theta(log log n))` recovery scale.  No Boolean-base theorem, cyclic
profile identity, or base--triangle union is required.

Use the source-compressed form of the internal-bank Cauchy theorem.  In
each nonempty context choose one canonical actual old-source target `A_c`.
For every selected internal triangle `T`, tag the incidence by the pair

\[
                              (A_c,T).                   \tag{1}
\]

The first coordinate has at most `V(P)` possibilities and the second has
at most `{n choose3}` possibilities.  If `kappa_A` is the actual maximum
dyadically compressed source-target load, then every pair in (1) has load
at most `kappa_A`.  Hence the *total* weighted triangle-bank mass, not just
its maximum fibre, obeys

\[
            \boxed{\displaystyle
             \sum_c w_ci_c\le
                 \kappa_A V(P){n\choose3}.}             \tag{2}
\]

Together with `sum_c w_ca_c<=kappa_A V(P)` and the exact local inequality
from `HIGH_TRIANGLE_QUERY_LOCALIZATION_GATE.md`, this gives

\[
 \boxed{\displaystyle
  M\le\kappa_A\left(5+
      \sqrt{{54\over5}{n\choose3}}\right)V(P)
   \le\kappa_A\left(5+{3\over\sqrt5}n^{3/2}\right)V(P).}          \tag{3}
\]

The genuine minimizer/source-history domination and dyadic compression
give `kappa_A<2L`, where `L` is the actual canonical description load.
Thus `L=n^O(1)` makes the right side of (3) only `n^O(1)V(P)`.  For every
fixed `sigma>0`,

\[
                     n^{O(1)}=o(n^{\sigma\log\log n}),             \tag{4}

\]

so the full `n^(Theta(log log n))` deficit closes.

This is a scale-sensitive theorem.  The triangle tag costs `n^(3/2)`
after Cauchy and therefore does **not** settle an EIC target requiring a
loss `D^(1-epsilon)` with `D` comparable to `n`.  It exactly settles the
later scale-recovery gate, where every fixed polynomial is free.

The previous sixteen fixed-`T` `2+2`/`3+1` signatures and the one-direction
star remain correct, but they no longer form a residue at this scale:
restricting to any signature, direction, SCC, base type, or arbitrary
child order type only deletes contexts and preserves (2)--(3).

This terminal statement is not an end-to-end half-coefficient proof.
`END_TO_END_QUASIPOLY_GATE_AUDIT.md` records the still-open upstream
complete-product/context-coexistence promotions and the polynomial
description-load hypothesis needed before Theorem 1 applies.

## 1. Exact tagged-mass theorem

Let `P` be an `n`-point planar general-position set and let `V=V(P)`.
Consider weighted simple bipartite product contexts `c`.  The active
old-source side consists of `a_c>=1` actual ordinary targets
`mathcal A_c`; the other side has size `b_c`; and the context record graph
has `e_c<=a_cb_c` edges.  All records in the dyadic layer have common
upper weight `w_c`.

Put

\[
 \kappa_A=\max_A\sum_{c:A\in\mathcal A_c}w_c.           \tag{5}
\]

For a thick context, `t_c=max(a_c,b_c)>=6`, select all triples in its
larger role-colored label cloud and put

\[
                         i_c={t_c\choose3}.              \tag{6}
\]

> **Theorem 1 (source--triangle tag closure).**  Equations (2)--(3) hold.
> They remain true for every weighted subfamily obtained by fixing a
> triangle, signed circuit class, direction, physical child, SCC state,
> base profile, or chronology mark.

**Proof.**  For every context choose `A_c` to be the least member of
`mathcal A_c` in one fixed global order.  Send every incidence `(c,T)`,
with `T` one of the `i_c` selected triangles, to `(A_c,T)`.  The load of a
fixed pair is

\[
 \sum_{c:A_c=A,\ T\in\mathcal I_c}w_c
 \le\sum_{c:A\in\mathcal A_c}w_c
 \le\kappa_A.                                          \tag{7}
\]

There are at most `V` choices for the ordinary first coordinate and at
most `{n choose3}` choices for the unordered second coordinate.  Summing
(7) proves (2).  Notice that the union `A_c union T` need not be ordinary;
`T` is a polynomial decoder tag, not a claimed output face.

The old-source bank itself gives

\[
                         \sum_cw_ca_c\le\kappa_AV.      \tag{8}

For thick contexts, equation (1) of
`HIGH_TRIANGLE_QUERY_LOCALIZATION_GATE.md` says

\[
                         e_c\le\sqrt{54\over5}\sqrt{a_ci_c}.       \tag{9}

Multiply by `w_c`, sum, and apply Cauchy with (2),(8):

\[
 \begin{aligned}
 \sum_{t_c\ge6}w_ce_c
 &\le\sqrt{54\over5}
   \sqrt{\sum_cw_ca_c}\sqrt{\sum_cw_ci_c}\\
 &\le\kappa_A\sqrt{{54\over5}{n\choose3}}\,V.          \tag{10}
 \end{aligned}

For `t_c<=5`, `e_c<=5a_c`, contributing at most
`5 kappa_A V`.  This proves the first inequality in (3).  Finally
`{n choose3}<=n^3/6`, and

\[
                     \sqrt{{54\over5}\,{1\over6}}={3\over\sqrt5}, \tag{11}

\]

which proves the second.  Deleting contexts cannot increase (5), so every
listed localization inherits the theorem.  QED.

## 2. Why the source tag is legitimate under reservoir replication

The theorem does not route each of the `e_c` records separately to one
source face.  Such routing would give a row of degree `d` and weight
`alpha` load `d alpha`, losing the release multiplier.

Instead, a product context/layer enters each source target once.  For an
upstream source mark of weight `alpha`, bucket descendant record weights
as

\[
                  2^{-k-1}\alpha<\beta\le2^{-k}\alpha. \tag{12}

\]

Entering the source once at the upper weight `2^{-k}alpha` in every
nonempty layer costs at most

\[
                         \sum_{k\ge0}2^{-k}\alpha=2\alpha.          \tag{13}

\]

Every original edge is rounded upward by less than two.  Therefore the
per-source canonical mark cap from
`MINIMIZER_WEIGHTED_LOOP_COVER_GATE.md`, together with actual description
load `L`, gives `kappa_A<2L`.  Genuine release neighbors remain as distinct
edges inside the context and still contribute to `e_c`; they are not
divided away.

Canonical coalescing is part of the statement.  Records with the same
fixed geometric/history state and dyadic weight layer must be treated as
one product context with their full active column set.  If two records
cannot be coalesced because they have different actual tangent, root, or
chronology states, that state contributes to the certified description
load `L`.  Artificially splitting one product into one-column contexts
and then claiming `kappa_A<2L` would be the same forbidden release-degree
overcount as direct routing.

## 3. Consequence for the fixed-triangle star

The exact planar family in
`HIGH_TRIANGLE_QUERY_LOCALIZATION_GATE.md` has `2^r` distinct bases `B_R`,
one fixed triangle `T`, one query direction, and unit source weights.
It satisfies (2) trivially with `kappa_A=1`: choosing one canonical
ordinary source `B_R union {P_1}` per context makes all pairs

\[
                       (B_R\cup\{P_1\},T)               \tag{14}

\]

distinct.  Replacing the Boolean top-ear bases by arbitrary low-face or
product bases cannot defeat Theorem 1.  Either their canonical source
targets remain distinct, consuming the `V` factor in (2), or repeated
targets consume `kappa_A` and are charged to the actual description load.
No property of the internal base face complex is used.

Likewise, fixing any one of the sixteen bad fixed-`T` circuit signatures
does not change the proof.  The tag `T` retains the root/cage side, and the
canonical `A_c` retains the source side.  A long mask run or cyclic third
role would give additional ordinary faces, but neither is needed for the
quasipolynomial estimate.

The theorem pinpoints why the earlier high-overlap formulation looked
harder than the live scale requires.  Bounding only
`Lambda_triangle=max_T sum_{c:T in I_c}w_c` insists on a one-face triangle
bank and exposes the fixed-`T` star.  Bounding the **total** triangle mass
with one ambient rank-three tag spends `n^3` decoder states instead.  That
is too costly for a fixed-power theorem but free against
`n^(Theta(log log n))`.

## 4. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_quasipoly_source_triangle_tag_closure.py
```

The checker verifies the local inequality through side size 100, exhausts
all bipartite subgraphs through `4` by `4`, constructs overlapping exact
rational source--triangle incidence systems and checks (2),(8),(10) by
cross multiplication, audits the dyadic source cap, and reruns the exact
one-direction planar star through Boolean rank eight.
