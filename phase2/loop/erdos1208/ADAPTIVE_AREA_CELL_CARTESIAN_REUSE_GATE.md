# Adaptive area cells: Cartesian reuse obstruction and the nonseparable gate

## Status

For a retained adaptive occurrence $\omega=(p,q)$, let $r_\omega$ be its
selected scalar gap and put

\[
 \mathcal A(r)=\{d:|d|>L,\ n_r(d)>0\},                 \tag{0.1}
\]

where

\[
 n_r(d)=\#\{(v,v'):\delta(v)-\delta(v')=r,
                         2\det(v,v')=d\}.              \tag{0.2}
\]

Gaussian factorization gives $n_r(d)\le G(m)=m^{o(1)}$.  Hence the adaptive
lift has the exact support reduction

\[
 X_{\rm ad}
 =\sum_{\omega}\sum_{d\in\mathcal A(r_\omega)}n_{r_\omega}(d)
 \le G(m)\sum_\omega|\mathcal A(r_\omega)|.             \tag{0.3}
\]

The problem is therefore reuse of signed-area supports by many surviving
common-$q$ occurrences.

This note establishes one positive endpoint theorem and one decisive
barrier.

**Exact size-biased pairing reduction.**  If the occurrence loads in one
translation are ordered $U_{q,1}\ge\cdots\ge U_{q,e_q}$, then

\[
 \sum_{i>b_q}U_{q,i}
 \le {1\over b_q}\sum_{i<j}\min(U_{q,i},U_{q,j}).        \tag{0.4}
\]

Consequently

\[
 \boxed{
 X_{\rm ad}\le {H_Q\over k^2}\mathcal P_{\rm ad},
 \qquad
 \mathcal P_{\rm ad}:=
 \sum_q{1\over h_q}\sum_{i<j}\min(U_{q,i},U_{q,j}).}   \tag{0.5}
\]

Thus the exact remaining positive target is
$\mathcal P_{\rm ad}\le m^{o(1)}k^2$.  Unlike a one-occurrence cell cap,
this is a genuinely paired common-$q$ endpoint quantity.

**Two-role Cartesian reuse obstruction.**  Suppose $P$ source pairs are
common to $Q\ge4$ distinct clean translations.  If the target edges in
each of the two roles admit the economical rank-one endpoint reuse

\[
 \tau_{q_j}(s_i)=\{X_i,Y_j\},\qquad
 \tau_{q_j}(t_i)=\{X'_i,Y'_j\},                         \tag{0.6}
\]

then the ambient set cannot be distance-Sidon.  Indeed, two different
unordered endpoint pairs have the same pair sum.  Thus the most efficient
$O(P+Q)$-endpoint realization of a $P\times Q$ occurrence grid is forbidden
by the simultaneous clean roles.

**Sharp abstract barrier.**  The adaptive quota, low source codegree,
isolated matching anchors, disjoint role targets, Gaussian cell multiplicity
one, and even injective joint residual cells are jointly insufficient.
There is an explicit finite model with nominal point count $k$ for which

\[
 H_Q=\Theta(k^2),\qquad X_{\rm ad}=\Theta(k^3).          \tag{0.7}
\]

The model is not economically endpoint-realizable by the pattern (0.6), and is not claimed to be a
geometric counterexample.  It proves that a successful global packing
theorem must use nonseparable endpoint realization of the common
translations; size bias and local area cells alone leave a full factor
$k$.

The exact residual is consequently a design problem: show that a large
adaptive-tail incidence matrix contains enough approximately separable
two-role endpoint reuse to invoke the obstruction, or charge the genuinely
nonseparable blocks directly.  This is a narrower gate than arbitrary area
cell reuse.

## 1. Exact occupied-cell and size-biased expansions

For each occurrence $\omega$, the affine residual from the clean rows is
constant over its target decorations, while the Gaussian residual is

\[
 G_{\omega,d}=a_\omega+18d.                            \tag{1.1}
\]

The map $d\mapsto G_{\omega,d}$ is injective.  Therefore the occupied joint
cells of one occurrence are exactly its occupied signed target areas, and
their multiplicities are the numbers $n_{r_\omega}(d)$.  Summing gives the
equality and inequality in (0.3).

This formulation also exposes why a bound on one fixed area cell cannot
finish the problem.  If $E(r)$ tail occurrences use the same scalar gap,
then every occupied target area at $r$ is reused $E(r)$ times:

\[
 X_{\rm ad}=\sum_r E(r)U_L(r).                          \tag{1.2}
\]

The vertical tensor is a genuine Cartesian product at the level of
residual labels.  The missing restriction is whether its occurrences can
be realized by the same $k$ physical endpoints.

There is a lossless way to expose the required occurrence pairing.  For a
fixed $q$, order its loads decreasingly and abbreviate $b=b_q$.  In the
pairwise-minimum sum, the term $U_{q,j}$ occurs as the minimum of
$(U_{q,i},U_{q,j})$ for every $i<j$.  Hence every $j>b$ occurs at least
$b$ times, proving (0.4).  Since

\[
 b_q\ge {k^2h_q\over H_Q},                              \tag{1.3}
\]

summing (0.4) proves (0.5).

The paired functional also has the exact layer-cake form

\[
 \mathcal P_{\rm ad}
 =\sum_{t\ge1}\sum_q{1\over h_q}
       \binom{E_q(t)}2,
 \qquad
 E_q(t)=|\{i:U_{q,i}\ge t\}|.                         \tag{1.4}
\]

Thus a proof can work dyadically: it must bound the normalized second
moment of target-rich isolated occurrences which share one literal
translation.  Formula (1.4) retains exactly the paired common-$q$ endpoint
structure absent from the vertical tensor theorem.

## 2. The two-role Cartesian obstruction

Let $s_i,t_i$ denote source pair sums and let $q_j$ be distinct literal
translations.  Assume the factorized target pattern (0.6).  The clean
pair-sum equations are

\[
 X_i+Y_j=s_i+q_j,
 \qquad
 X'_i+Y'_j=t_i+q_j.                                    \tag{2.1}
\]

Fixing any one $i$ shows that there are constants $C,C'$ such that

\[
 X_i=s_i+C,\quad Y_j=q_j-C,
 \qquad
 X'_i=t_i+C',\quad Y'_j=q_j-C'.                        \tag{2.2}
\]

For distinct $j,\ell$, (2.2) gives

\[
 \boxed{Y_j+Y'_\ell=Y'_j+Y_\ell.}                     \tag{2.3}
\]

Within each family the points are distinct, because the $q_j$ are
distinct.  Also $Y_j\ne Y'_j$: otherwise the two target role edges in the
occurrence $(p_i,q_j)$ meet, contradicting the exact target-disjointness of
an isolated anchor.

Cross-family coincidences form a partial matching: a fixed $Y_j$ can equal
at most one $Y'_\ell$, and conversely.  Among $Q\ge4$ indices one can choose
$j\ne\ell$ for which

\[
 Y_j\ne Y'_\ell,qquad Y'_j\ne Y_\ell.                 \tag{2.4}
\]

Indeed, for each $j$ at most two values of $\ell$ are forbidden by these
two equalities.  The two sides of (2.3) are then sums of distinct points,
and the unordered pairs

\[
 \{Y_j,Y'_\ell\},\qquad\{Y'_j,Y_\ell\}                 \tag{2.5}
\]

are different.  A distance-Sidon set has unique unordered pair sums:
equality of two pair sums rearranges to equality of two directed
differences and hence of the endpoint pairs.  Equation (2.3) is therefore
impossible.  This proves the theorem.

The use of both roles is essential.  One factorized target grid
$\{X_i,Y_j\}$ is compatible with pair-sum uniqueness.  The second grid,
carrying the same literal translations, creates the cross-role collision
(2.3).

## 3. A factor-$k$ abstract adaptive countermodel

Let $n\ge4$ and take nominal point count

\[
 k=10n.                                                  \tag{3.1}
\]

Use $n$ selected source pairs $p_1,\ldots,p_n$ and $n$ translations
$q_1,\ldots,q_n$.  Put two formal clean starts $s_i,t_i$ for each $p_i$
and declare

\[
 H_{q_j}=\{s_i,t_i:1\le i\le n\}.                      \tag{3.2}
\]

Thus each displayed fibre has $h_{q_j}=2n$, every $p_i$ has codegree
$n<k$, and every translation contributes $e_{q_j}=n$ isolated selected
occurrences.  Give the anchors of each $p_i$ pairwise disjoint heads and
tails, so its anchor graph is a literal matching.  Give each occurrence
four formal role-target endpoints, disjoint within that occurrence.

Adjoin unrelated filler clean fibres until

\[
 H_Q=4k^2.                                              \tag{3.3}
\]

This is within the elementary capacity of at most $k(k-1)$ translations,
each of size at most $N=\binom k2$.  The adaptive quota on every displayed
translation is

\[
 b_{q_j}
 =\left\lceil{k^2(2n)\over4k^2}\right\rceil
 =\lceil n/2\rceil.                                    \tag{3.4}
\]

Assign all selected source pairs one common target gap with exactly $k$
occupied signed-area cells, each of multiplicity one.  Thus even the same
area support may be reused by all displayed occurrences; use different
formal affine joint labels whenever desired.  After removing the largest
$b_{q_j}$ occurrences, all loads are tied and

\[
 \begin{aligned}
 E_{\rm ad}&=n\lfloor n/2\rfloor,\\
 X_{\rm ad}&=kn\lfloor n/2\rfloor
             =\Theta(k^3),\\
 {X_{\rm ad}\over H_Q}&=\Theta(k).
 \end{aligned}                                         \tag{3.5}
\]

Every numerical and local structural input listed in the status holds.
What fails is precisely global endpoint realization: the economical
factorized realization of (3.2) in both roles is forbidden by Section 2,
while assigning fresh target endpoints to every cell would require
$\Theta(n^2)$ points instead of $k=10n$.

The paired functional makes the same failure explicit.  In this model,

\[
 \mathcal P_{\rm ad}
 =n\,{1\over2n}\binom n2 k
 =\Theta(k^3),                                         \tag{3.6}
\]

a full factor $k$ above its required $k^2$ scale.  Therefore the
order-statistic reduction (0.5), while exact, cannot be completed by any
abstract second-moment estimate on the undecorated incidence graph.

Thus no inequality derived only from

* the quota values $b_q$;
* $h_q,e_q,c_Q(p)$;
* isolated matching anchors and within-occurrence role disjointness; or
* fixed signed-area/joint-cell multiplicity

can imply $X_{\rm ad}\le m^{o(1)}H_Q$.

## 4. Quantitative restart gate

Let the tail incidence graph have left vertices source pairs $p$, right
vertices translations $q$, and one edge for every surviving occurrence.
Each edge carries two clean target-role edges.  Section 2 forbids a
$K_{P,Q}$ block with $Q\ge4$ whenever both role-edge arrays reuse endpoints
in the rank-one pattern (0.6).

A viable theorem can therefore take either of two forms.

1. **Separable extraction.**  Prove that adaptive mass
   $X_{\rm ad}\gg m^{o(1)}H_Q$ forces a large incidence block on which both
   target-role arrays factor as in (0.6), perhaps after boundedly many
   endpoint classes.  Section 2 then gives a contradiction.
2. **Nonseparable charge.**  Prove directly that occurrence blocks avoiding
   (0.6) consume enough distinct target endpoints, pair sums, or design rank
   that their total signed-area support is $m^{o(1)}H_Q$.

Ordinary dependent random choice on the unlabelled incidence graph is not
enough: the abstract model in Section 3 contains the complete
$K_{n,n}$.  The extraction must retain the two endpoint decorations and
show their approximate separability.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_adaptive_area_cell_cartesian_reuse_gate.py
```

The verifier checks the exact quota, paired-minimum reduction, and factor-$k$
excess in Section 3, all matching/codegree/cell-cap conditions, and the symbolic pair-sum
collision (2.3) for Cartesian blocks.  It also exhausts the cross-family
coincidence patterns for $4\le Q\le8$ and confirms that a valid pair
$j,\ell$ satisfying (2.4) always exists.
