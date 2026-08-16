# Dense Hall rectangles are paid by the internal triangle bank

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

Anti-aligned child profiles do not defeat a global internal-bank Cauchy
argument.  In fact, no unrestricted child-face theorem is needed: every
one-, two-, and three-point subset is ordinary.  Pair the five decoded Hall
targets with the rank-three banks inside the two physical clouds.

For a context `c`, let its active row and column clouds have sizes `a_c,b_c`
and let `e_c<=a_cb_c` be the number of canonical records in its simple
bipartite core.  Give every record in the context common weight `w_c`.
Let

\[
 h_c=2a_c+2b_c+1                                         \tag{1}
\]

be the number of actual `W,Q,C,A,E` targets and, when
`a_c,b_c>=6`, let

\[
 i_c={a_c\choose3}+{b_c\choose3}                         \tag{2}
\]

be the number of internal cloud triangles.  If `Lambda_H` and `Lambda_3`
are the actual maximum weighted overlaps of these two banks, then

\[
 \boxed{
 \sum_c w_ce_c\le
 {5\over2}\Lambda_HV(P)
 +\sqrt{27\over20}\,
       \sqrt{\Lambda_H\Lambda_3}\,V(P).}                \tag{3}
\]

The first term contains contexts with one side of size at most five; the
second contains the remaining contexts.  Thus a dense Hall core closes at
constant loss whenever the Hall-target and physical-triangle overlaps have
controlled geometric mean.  Independent reflections, arbitrary child
order types, and complete cap/cup anti-alignment do not affect (3).

This identifies the exact global residue.  Failure requires high reuse of
an actual cloud triangle together with high reuse of the decoded Hall
targets.  After a bounded triangle-to-child support decoder, this fixes one
physical child queried in many Hall contexts.  Only there do coherent
multi-direction `PGL_2` itineraries or a cyclic third-role profile identity
become relevant.

## 1. Setup and decoder bank

Context `c` has a simple bipartite record graph

\[
                            E_c\subseteq Y_c\times Z_c,   \tag{4}
\]

with no isolated active labels.  Global role coloring distinguishes the
row and column supports.  For every active row `y` there are two ordinary
targets `A_y,E_y`; for every active column `z` there are two ordinary
targets `W_z,C_z`; and the context has one ordinary common target `Q_c`.
They are actual, distinct faces inside the context, so their union
`mathcal H_c` has size (1).  This is precisely the five-target system in
`DENSE_HALL_TWO_CLOUD_PROFILE_BARRIER.md`.

Define

\[
 \Lambda_H=\max_R\sum_{c:R\in\mathcal H_c}w_c.           \tag{5}
\]

For a thick context (`a_c,b_c>=6`) put

\[
 \mathcal T_c={Y_c\choose3}\cup{Z_c\choose3}.           \tag{6}
\]

Every member of (6) is an ordinary triangle, independently of the order
type of the rest of its cloud.  Global role coloring makes the two parts
disjoint and `|mathcal T_c|=i_c`.  Define the actual overlap

\[
 \Lambda_3=\max_T\sum_{c:T\in\mathcal T_c}w_c.           \tag{7}
\]

No context or cloud name is treated as an output tag in (5) or (7).  All
reuse of the same ordinary face is included.

## 2. Exact local inequalities

If `s=min(a_c,b_c)<=5` and `t=max(a_c,b_c)`, then

\[
                 e_c\le st\le {s\over2}h_c
                              \le {5\over2}h_c.          \tag{8}
\]

This is the thin branch and uses only Hall targets.

Now suppose `a=a_c,b=b_c>=6`.  For every integer `t>=6`,

\[
 {t\choose3}={t(t-1)(t-2)\over6}\ge {5\over54}t^3.     \tag{9}
\]

Also

\[
 (a+b)(a^3+b^3)=(a+b)^2(a^2-ab+b^2)
                         \ge4a^2b^2.                    \tag{10}
\]

Since `h_c>=2(a+b)`, equations (2), (9), and (10) give

\[
 h_ci_c\ge {5\over27}(a+b)(a^3+b^3)
                  \ge {20\over27}a^2b^2
                  \ge {20\over27}e_c^2.                \tag{11}
\]

Equivalently,

\[
                       e_c\le\sqrt{27\over20}\sqrt{h_ci_c}.       \tag{12}
\]

The constant is uniform for unbalanced rectangles and arbitrary subgraphs.
At equal large sides the sharper limiting constant in (11) is `4/3`, but
the exact `20/27` is convenient down to size six.

## 3. Global weighted Cauchy theorem

For the thin contexts, sum (8) and use

\[
             \sum_cw_ch_c\le\Lambda_HV(P).              \tag{13}
\]

For thick contexts, multiply (12) by `w_c`, sum, and apply Cauchy:

\[
\begin{aligned}
 \sum_cw_ce_c
 &\le\sqrt{27\over20}
      \sum_c\sqrt{(w_ch_c)(w_ci_c)}\\
 &\le\sqrt{27\over20}
      \sqrt{\sum_cw_ch_c}\sqrt{\sum_cw_ci_c}\\
 &\le\sqrt{27\over20}\sqrt{\Lambda_H\Lambda_3}\,V(P). \tag{14}
\end{aligned}
\]

Adding the thin bound proves (3).

Arbitrary edge weights cause no conceptual change.  Split each context
into dyadic edge-weight layers and regard every nonempty layer as a context
with its active row/column sets.  Replacing a layer's weights by its upper
endpoint loses a factor below two.  The loads (5),(7) are then computed on
the actual layers, so no number-of-buckets factor is hidden.

## 4. Scale consequence

For any desired coefficient saving, (3) reduces the thick core to the
single explicit condition

\[
              \sqrt{\Lambda_H\Lambda_3}\le D^{1-\epsilon},        \tag{15}
\]

with the analogous direct condition on `Lambda_H` for thin contexts.
This is stronger than a cross-profile theorem: it survives the exact
`S_m^2` anti-aligned regression, because the two parabolic clouds contain
`2{m\choose3}` distinct triangle outputs.

In one complete `m` by `m` regression,

\[
 h=4m+1,\qquad i=2{m\choose3},\qquad e=m^2,              \tag{16}
\]

and (11) holds with room.  The internal profiles may be polynomial or
exponential; the triangle bank is unchanged.

## 5. What high triangle overlap means

Equation (7) is label-level, not a formal context statistic.  A high value
fixes an actual triangle `T` reused by many contexts.  If an actual
triangle belongs to at most `Delta_child` canonical physical child
supports, then one child is incident with weight at least

\[
                           \Lambda_3/\Delta_{\rm child}.             \tag{17}
\]

This is the correct entrance to the coherent-direction argument.  Form a
directed query multigraph whose vertices are physical labelled children
and whose edge `Y -> Z` is a two-cloud Hall context, tagged by its actual
projective direction and `W,Q,C,A,E` state.

There is an exact combinatorial split:

1. edges internal to nontrivial strongly connected components lie on
   directed cycles;
2. edges between components form a DAG; and
3. a high-degree vertex is one physical child queried many times.

The first branch can use the cyclic endpoint-product identity only if the
cycle's profile unions are jointly ordinary and recoverable; separate Hall
contexts do not automatically supply that geometry.  In the third branch,
four genuinely distinct direction queries to the **same completed child**
are precisely the scope where the coherent `PGL_2` itinerary bound applies.
If there are at most three directions, all the weight may occupy a
one-direction star or reset hierarchy; the universal cage regression
realizes this and shows that no contradiction follows from graph theory.

Thus (3) closes low triangle reuse and localizes every failure to the exact
multiquery/chronology state where earlier `PGL_2` bounds are legitimate.
It does not incorrectly apply those bounds to independent siblings.

`HIGH_TRIANGLE_QUERY_LOCALIZATION_GATE.md` sharpens this residue.  It
replaces the full Hall overlap by the dyadically compressed old-source
load, retains the `n^(Theta(log log n))` scale, and proves the exact next
split: a decoded base--triangle mixed face or one of sixteen signed
`2+2`/`3+1` circuit classes.  Its one-direction Boolean-star construction
also shows why SCC and projective coherence alone cannot finish the latter
branch.

At the `n^(Theta(log log n))` scale, the continuation is complete:
`QUASIPOLY_SOURCE_TRIANGLE_TAG_CLOSURE.md` tags every triangle incidence
by one canonical source face and the ambient triangle.  The resulting
`O(kappa_A n^(3/2))` loss is polynomial and hence negligible at that
scale.  This last step is deliberately not asserted for the fixed-power
EIC gate.

## 6. Sharp abstract history barrier

Neither overlap in (3) is bounded by planarity alone.  Duplicate one fixed
geometric rectangle with `r` different unrecorded chronology descriptions.
The demand and both loads are multiplied by `r`, while the ordinary face
set is unchanged.  Equation (3) remains an equality-scale statement and
cannot remove `r`.  Canonicalization, an actual history mark, or a source
downshadow is necessary.

This is the only abstract obstruction left by the internal triangle bank:
the anti-aligned child order types themselves are fully paid.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_dense_hall_internal_triangle_cauchy.py
```

The checker exhausts all side sizes through 100, every bipartite graph
through `4` by `4`, exact rational weighted overlap systems, and the
strongly-connected-component cycle/DAG split.  It verifies (8)--(14) by
integer cross multiplication.
