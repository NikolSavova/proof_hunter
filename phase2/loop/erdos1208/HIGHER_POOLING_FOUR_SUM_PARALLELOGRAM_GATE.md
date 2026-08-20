# Higher pooling: synchronized four-sum cliques, not area supersaturation

## 1. Outcome

The fully transverse high-codegree mass has an exact higher-pooling
reduction.  If a transverse-rich base record `C` has `T(C)>=k/2` third
translations, then for every fixed `ell>=2` and `k>=4ell`,

\[
 T(C)\le \ell!\left({4\over k}\right)^{\ell-1}
                 {T(C)\choose\ell}.                    \tag{1.1}
\]

Every `ell`-subset counted on the right is a clique in three synchronized,
endpoint-realized four-sum relations.  This gives a rigorous new sufficient
target at the `ell`-pool level, with the scalar weight and all base and
third translations retained.

The hoped-for bridge from those pools to equal-area/special-affine energy
is false even for surprisingly large pools.  The literal high-codegree,
scalar-weighted rank-flat certificate in
`HIGH_CODEGREE_TRANSVERSE_EQUAL_AREA_RANK_FLAT_BARRIER.md` has a set of
16 fully transverse translations such that the union of

* all source endpoints;
* all base anchor and target endpoints;
* all anchor and target endpoints of the 16 translations; and
* all determinant-qualified metric-wedge endpoints

contains **no** six-distinct equal-area triangle pair.  By monotonicity the
same is true for every subset of this pool, so every direct pooling
implication of orders `2<=ell<=16` fails on a certificate with

\[
 k=48,\qquad c(p)=49\ge k,qquad
 V(p)=V(p^{\rm op})=1.                                  \tag{1.2}
\]

Thus higher pooling produces a real structure, but that structure is the
synchronized four-sum clique itself.  A continuation must bound its
scalar-weighted aggregate directly; bounded-order pooling does not turn it
into the existing determinant-one energy.

## 2. Exact synchronized clique identities

Fix a source pair `p=(s,t)` and `q in Q_p`.  Write

\[
 q=A_q-B_q,qquad
 G_q=E(s+q),\qquad H_q=E(t+q),                           \tag{2.1}
\]

where `G_q,H_q` also denote their pair sums.  The two clean rows give

\[
 G_q=s+q,qquad H_q=t+q.                                \tag{2.2}
\]

For every two translations `q,r in Q_p`, one therefore has

\[
\boxed{
\begin{aligned}
 G_q+H_r&=G_r+H_q,                                      \tag{2.3a}\\
 G_q+B_q+A_r&=G_r+A_q+B_r,                             \tag{2.3b}\\
 H_q+B_q+A_r&=H_r+A_q+B_r.                             \tag{2.3c}
\end{aligned}}
\]

All entries in (2.3) are endpoints of `A`, grouped into four-point sums.
The first relation is target--target; the second and third synchronize the
good and bad target roles with the anchors.  An `ell`-pool is a complete
graph on `ell` translations in each of these three relations, with the
same vertex labels in all three graphs.

The full role-labelled endpoint system recovers the decorations exactly.
From an anchor and its good target edge one recovers

\[
 q=A_q-B_q,qquad s=G_q-q,                              \tag{2.4}
\]

and the bad edge similarly recovers `t=H_q-q`.  Thus keeping all three
roles makes `(p,q)` injective.  What cannot be discarded is the
synchronization: (2.3a) alone remembers only `s-t`, while an anchor--target
relation alone forgets the other source start and hence its scalar label.

## 3. Binomial amplification with the scalar weight

Let `C_tr` be the transverse-rich base records in the high-codegree band,
so

\[
 T(C)\ge{c(p_C)\over2}\ge{k\over2}.                    \tag{3.1}
\]

Put

\[
 w(C)=V(p_C)+V(p_C^{\rm op})                            \tag{3.2}

\]

and define the exact `ell`-pool mass

\[
 \mathfrak P_\ell(V)=
 \sum_{C\in\mathcal C_{\rm tr}}{T(C)\choose\ell}w(C). \tag{3.3}
\]

This retains the base translations, every selected third translation,
the ordered source pair, and the physical scalar wedge inside `V`.

If `k>=4ell`, then `T>=k/2` gives `T-ell+1>=k/4`, and hence

\[
\begin{aligned}
 {T\choose\ell}
 &= {T\over\ell}{T-1\choose\ell-1}\\
 &\ge {T\over\ell!}(T-\ell+1)^{\ell-1}
 \ge {T\over\ell!}\left({k\over4}\right)^{\ell-1}.
\end{aligned}                                          \tag{3.4}
\]

This proves (1.1) and the weight-preserving aggregate reduction

\[
 \boxed{
 \mathfrak T_{\rm rich}(V)
 \le \ell!\left({4\over k}\right)^{\ell-1}
       \mathfrak P_\ell(V).}                            \tag{3.5}
\]

Consequently a sufficient endpoint theorem for the transverse-rich term is

\[
 \boxed{
 \mathfrak P_\ell(V)
 \le m^{o(1)}N k^{\ell+3}.}                             \tag{3.6}
\]

Indeed (3.5) then gives the required `m^(o(1)) N k^4` bound for fixed
`ell`.  For `ell=2`, one may use the sharper exact inequality

\[
 T\le {4\over k-2}{T\choose2}\qquad(T\ge k/2),          \tag{3.7}
\]

so the first pooled target is the scalar-weighted synchronized
parallelogram-pair mass at scale `m^(o(1))Nk^5`.

## 4. A 16-pool with no affine witness

In the 48-point rank-flat certificate, choose the stored one-role base and
the following 16 transverse translations, named by their original template
differences:

\[
\begin{split}
 &(942,-90),(726,-70),(445,-43),(-20,2),\\
 &(438,-42),(-111,11),(139,-13),(-178,18),\\
 &(117,-11),(-526,50),(-695,67),(-416,40),\\
 &(843,-81),(1340,-128),(555,-53),(-741,71).
\end{split}                                             \tag{4.1}

Their actual deformed anchor vectors are, as always, recovered from their
stored endpoint pairs; the labels in (4.1) only identify the incidence
roles unambiguously.

The verifier exhaustively checks all 24 global six-distinct geometric
equal-area pairs.  None is supported on the endpoint union of the base,
the metric wedge, and all 16 translations in (4.1).  Nevertheless every
one of the `binom(16,2)=120` translation pairs satisfies all three
relations (2.3).  Thus the four-sum clique is dense while the local
special-affine energy is zero.

There is substantial room below 16.  On all 36 transverse translations of
the same base, the exact number of zero-exposure pools is

\[
\begin{array}{c|rrrrrr}
 \ell&1&2&3&4&5&6\\ \hline
 \#\text{ pools exposing no area pair}
 &31&404&2466&8358&18486&29577.
\end{array}                                             \tag{4.2}

Equation (4.1), rather than the sampled counts in (4.2), is the decisive
barrier: it simultaneously kills every bounded pooling order through 16.

## 5. Exact remaining route

The equal-area framework can still be used only after an additional global
many-to-one theorem; no endpoint-local extraction is available.  The more
literal target is now (3.6), treating an `ell`-pool as a synchronized clique
of four-sum parallelograms.

A successful direct proof must exploit at least one of the following facts
without deleting the scalar weight:

1. all three clique relations (2.3) use the same translation vertices;
2. the full roles recover `(p,q)` injectively by (2.4);
3. the anchor and both target edges are clean six-endpoint rows; and
4. `V(p)` supplies an independent high-determinant physical endpoint wedge.

Bounding an unrestricted fourth additive energy, or retaining only
(2.3a), loses the source pair and is too coarse.  Conversely, the 16-pool
barrier shows that simply increasing a fixed pooling order and invoking
determinant-one energy cannot close the route.

## 6. Verification

Run

```bash
python phase2/loop/erdos1208/verify_higher_pooling_four_sum_parallelogram_gate.py
```

The verifier imports and rechecks the literal rank-flat certificate, checks
all 120 synchronized four-sum triples inside (4.1), verifies that its full
endpoint union has zero area exposure, reproduces the zero-pool counts in
(4.2), and exhaustively checks the finite binomial inequalities underlying
(3.5) and (3.7).
