# Exact two-level rechart exploration

**Date:** 2026-08-15.  This is a finite exact stress test, not an
asymptotic theorem.  Counts below are nonempty.

## Verdict

The 14-point mutation-minimal common-guard wrapper can be recursively
recharted, but its second-level profile spectrum does not reproduce the
atomic scalar menu.  Start with the exact wrapper of face count

\[
                         W_1=1561,
\]

enumerate its 174 projection chambers, and choose three chamber profiles
which minimize a fresh three-child common-guard wrapper.  The exact optimum
is

\[
 (C,U)=(209,1071),(414,342),(1071,209),
\]

and the proved block recurrence gives

\[
                         n_2=44,qquad W_2=928811.       \tag{1}
\]

Re-embed those three copies by rational orientation-preserving affine maps
and the exact strong-comb map.  Exhausting all 1860 projection chambers
of the resulting 44-point order type gives

\[
 \min_\xi C_\xi U_\xi
   =14391\cdot61321=882470511,
 \qquad
 \min_\xi\max(C_\xi,U_\xi)=42362.                     \tag{2}
\]

Thus the reset spectrum retains very large product energy, while still
containing highly skewed profiles.  Optimizing three copies of this exact
second-level spectrum gives

\[
 (13263,121607),(49248,20379),(121607,13263)
\]

and a realizable third wrapper with

\[
                         n_3=134,qquad W_3=8899254645. \tag{3}
\]

Including the empty set, the finite normalized coefficients
`log_2(W+1)/(log_2 n)^2` at the first three levels are approximately

\[
                         0.73181,quad0.66515,quad0.66195. \tag{4}
\]

This is consistent with convergence toward the known coefficient-half
barrier, but three finite levels do not prove a limit.  It also shows why
the reset gate must retain the full skew spectrum rather than only
`min C U`: the large product in (2) does not prevent the asymmetric entries
used in (3).

## Global first-reset menu audit

The mutation-minimal word above is not the globally best first reset.  A
second exact audit exhausts the complete rooted four-point menu together
with its generic reset chambers.  In the fixed rational gauge used by the
checker, the three witnesses have assembly/reset data

\[
 \begin{array}{c|c|c}
   \text{rooted word}&\text{reset profile}&W\\ \hline
   (7,0,0)&(183,1975)&1992\\
   (0,1,7)&(342,414)&1986\\
   (7,0,0)&(1975,183)&1992.
 \end{array}
\]

Their exact strong-comb assembly has

\[
             n_2=44,\qquad W_2=747670,                 \tag{5}
\]

and 1884 generic projection chambers.  Its least endpoint product in this
gauge is

\[
              18275\cdot49645=907262375,               \tag{6}
\]

while `min max(C,U)=39777`.  Optimizing the next three-child wrapper over
this entire spectrum chooses

\[
 (15121,102449),(44728,21566),(102449,15121)
\]

and gives

\[
             n_3=134,\qquad W_3=11358202734.           \tag{7}
\]

The normalized coefficients at these two levels are `0.65465` and
`0.66900`.  Thus the globally better level-two menu actually rebounds at
level three.  This is useful negative evidence against treating a single
low finite reset as a recursive fixed point.

The exact endpoint minimum in (6) is gauge-sensitive: independently
mirroring or projectively recharting the children changes the numerical
spectrum while preserving the displayed assembly count.  Accordingly a
recursive audit must retain the realized child embeddings and cross-child
pair-direction arrangement, then recompute the completed parent's reset
spectrum; the particular pair in (6) is not a recursive invariant.  A
branching wrapper uses independent child copies, so this statement does not
impose a same-generation multi-direction `Pi_q` constraint.  A node may be
promoted as a new atom, export its construction-to-one-reset pair, and
forget older target charts because its ordinary face count is chart
invariant.  Pathwise multi-direction coherence is required only if one
explicitly retains several ancestor profiles at once; it is not an
unconditional recursive constraint.

## Exactness and scope

The level-one and level-two chamber lists use exact `Fraction` arithmetic.
Every triple in the 44-point configuration is checked nonzero.  Cap and cup
counts are computed by the last-two-points chain recurrence after one exact
orientation-table computation.  Face counts (1) and (3) use the already
proved exact five-block strong-comb recurrence; enumerating `2^44` subsets
is neither needed nor attempted.  The affine chamber rechart and exact
strong-glue construction preserve every child order type and displayed
assembly chart, so (3) is an
existence statement even though the 134-point chamber spectrum is not
enumerated.

Run

```bash
cd phase2/loop/erdos838/agent_root_followup
python3 explore_two_level_rechart.py
```

The script is deliberately named `explore`: it certifies the displayed
finite values but makes no all-scale inequality or sub-half construction
claim.

The global-menu variant is checked independently by

```bash
python3 phase2/loop/erdos838/agent_root_followup/verify_global_menu_two_level.py
```
