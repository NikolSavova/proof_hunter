# Excess-rank sources: four-local completion or one-gap/blocker entropy

**Date:** 2026-08-15.  All logarithms and entropies are base two.

## Verdict

The excess-rank residue from
`HIGH_REDUNDANCY_RELEASE_HALL_BARRIER.md` has an exact planar
coordinatization dichotomy.  The physical point set is in general
position, as in the ambient problem.  Fix a root face `T` of rank
`t<=3`.  Let

\[
              E\subseteq X_1\times\cdots\times X_s       \tag{1}
\]

be selected words for which `T union A` is an ordinary convex face.  The
role supports are pairwise disjoint and disjoint from `T`.  Give the words
weights `0<w_A<=1`, put `W=sum_A w_A`, let `P` be the distribution
`P(A)=w_A/W`, write `m_i=|X_i|`, and set

\[
 P_0=\prod_i m_i,\qquad R_w=\log P_0-H(P).             \tag{2}
\]

The unweighted case has `w_A=1`, `W=M=|E|`, and
`R_w=log(P_0/M)`.  The weighted statement is important in the live
rank-safe slice: no conversion from history weight to raw source count is
being hidden.

There are two complementary exact theorems.

1. **Four-local completion.**  Either at least `P_0/2` rooted ambient
   words are ordinary, or at most four physical roles, together with a
   fixed subset of `T`, contain a polynomial-density complete box of
   bad four-circuits of one fixed `1+3` type.
2. **Projection entropy.**  For every coordinate, compare the number of
   selected extensions of a projected source with the number of all
   ordinary extensions.  Total redundancy splits as

   \[
                       R_w\le G+B,                       \tag{3}
   \]

   where `G` is recoverable one-gap entropy and `B` is rooted blocker
   entropy.  The ordinary one-gap bank satisfies

   \[
                    {V(P)\over W}\ge2^{G/s}.             \tag{4}
   \]

   If `B>=R_w/2`, one physical coordinate has a positive-mass family of
   projected sources each admitting only an exponentially small fraction
   of its role alphabet; a canonical source triple blocks
   `m_i/poly(s)` actual labels.

Thus a quadratic high-redundancy source family cannot remain an
unstructured sparse code.  It either completes to an ambient transversal
bank, emits a fixed-power one-gap bank, or returns a polynomial-loss
physical rooted-fan/core incidence.

At the live normalization

\[
                 W\ge V(P)2^{-\tau}.                     \tag{5}
\]

the first alternative rules out quadratic `R_w` whenever
`tau=o((log n)^2)`.  The second
alternative gives a genuine `n^{Omega(1)}` projection gain when
`G=Omega((log n)^2)`.  For the present four-local argument, injective role
colouring costs only `2^{O(s)}`, not the earlier positional
`2^{O(s log s)}` loss; fixing a physical root separately can still cost a
polynomial factor.  The third alternative is the exact
physical label core needed by the subsequent blocker/Hall machinery.

This does not yet prove the half coefficient.  A scalable cyclic Ferrers
or diagonal constraint can put its redundancy into local blocker entropy;
deleting a role breaks the constraint and exposes the known one-gap bank.
The missing global step is to multiply/sum those rolewise banks with
subquadratic decoder load.  The theorem below proves the local dichotomy
and eliminates the central-layer and MDS anti-module regressions.

## 1. Unordered injective role colouring costs only exponentially

The four-local and projection arguments do not need the cyclic position of
each source label to be fixed.

> **Lemma 1 (weighted injective colouring).**  Suppose every source is
> `T union A`, where `|A|=s`, and give the sources weights at most one.
> There is a colouring of all non-root physical labels by `[s]` for which
> the total weight of sources whose `s` labels receive all distinct
> colours is at least
>
> \[
>              {s!\over s^s}\,W_0\ge e^{-s}W_0.          \tag{5a}
> \]

**Proof.**  Under an independent uniform random colouring, the probability
for each fixed source is `s!/s^s`.  Average its weight.  The last
inequality is the standard bound `s!>=(s/e)^s`.  QED.

For a retained source, colour is now its coordinate.  The colour classes
are pairwise disjoint physical supports, but their cyclic order is allowed
to vary from word to word.  Nothing below uses a common cyclic order.
Thus at `s=O(log n)` the role cost is only `2^{O(s)}`.  The
`2^{O(s log s)}` positional colouring remains necessary for later
oriented seam operations, not for this dichotomy.

## 2. Dense uniform layers force a convex support shield

The basic planar certificate is especially rigid.

> **Lemma 2 (four-cover shield).**  Let `Z` be a set of physical labels and
> let `mathcal E` be ordinary faces contained in `Z`.  If every four-set of
> `Z` is contained in some member of `mathcal E`, then `Z` is in convex
> position.  Consequently all `2^{|Z|}` subsets of `Z` are ordinary.

**Proof.**  Every four-set is a subset of an ordinary face and is therefore
ordinary.  A finite planar point set is in convex position iff each of its
four-subsets is in convex position.  QED.

For an `r`-uniform family `mathcal E subseteq {Z choose r}`, `r>=4`, write

\[
                       \eta=1-{|\mathcal E|\over {|Z|\choose r}}.     \tag{6}
\]

If a four-set is uncovered, all its `{|Z|-4 choose r-4}` extensions are
missing.  Hence

\[
 \eta\ge{{|Z|-4\choose r-4}\over{|Z|\choose r}}
       ={(r)_4\over(|Z|)_4}
       \ge\left({r-3\over|Z|}\right)^4.                \tag{7}
\]

Thus the strict reverse inequality in (7) forces the Boolean shield of
Lemma 2.  This is the exact dense-layer exit; no stability theorem is
needed in the exponentially-near-complete regime.

The central-layer stress family `mathcal E={Z choose r}` is therefore not
a residue: it releases the complete support shield.  Kruskal--Katona
cardinality without the four-cover conclusion would miss this payment.

## 3. Rooted four-local completion of a role box

Let \(\mathcal I\) consist of pairs \((J,K)\), where
\(J\subseteq[s]\), \(K\subseteq T\), and \(|J|+|K|=4\).  For
\((J,K)\in\mathcal I\), let `Bad_{J,K}` be the tuples in
`prod_(i in J) X_i` for which the tuple together with `K` is a
nonconvex four-set, and put

\[
             \beta_{J,K}={|Bad_{J,K}|\over\prod_{i\in J}m_i}.        \tag{8}
\]

Every relevant projection of a selected word lies outside
`Bad_{J,K}`.  More importantly, a rooted ambient completion
`T union A` is nonconvex iff at least one of these four-subsets is bad.
There are at most \({s+t\choose4}\) patterns.

> **Theorem 2 (rooted ambient completion or physical circuit core).**  The
> number `C_0` of ambient words for which `T union A` is ordinary
> satisfies
> 
> \[
>       C_0\ge P_0\left(1-\sum_{(J,K)\in\mathcal I}\beta_{J,K}\right).
>                                                               \tag{9}
> \]
> 
> Consequently either `C_0>=P_0/2`, or some pattern obeys
> 
> \[
>            \beta_{J,K}>{1\over2{s+t\choose4}}.        \tag{10}
> \]

**Proof.**  A bad `(J,K)`-tuple extends to exactly
`P_0/prod_(i in J)m_i` ambient words.  Union-bound these extensions.
Every nonconvex finite planar set has a nonconvex four-subset (Caratheodory,
or the usual planar circuit certificate), so every rooted word outside the
union is ordinary.  This proves (9); (10) is pigeonhole.  QED.

The second branch contains a complete physical bad box after a
polynomial-loss refinement.  Split `Bad_{J,K}` by which of its four
points is interior and retain a signed `1+3` relation of density at least
`beta_{J,K}/4`.  This is a fixed-complexity semialgebraic
`|J|`-partite relation, with the points of `K` as fixed parameters.
Apply the fixed-arity semialgebraic regularity atom with error
`beta_{J,K}/8`.  If its number of parts per variable role is at most

\[
                         Q\le(8/\beta_{J,K})^{C},         \tag{11}
\]

where `C` is an absolute constant uniform over arities one through four,
the homogeneous bad cells have total product mass at least
`beta_{J,K}/8`.  One cell has product mass at least

\[
          {\beta_{J,K}\over8Q^{|J|}}
             \ge(\beta_{J,K}/8)^{4C+1}.                \tag{12}
\]

Hence there are subsets `Y_i subseteq X_i`, `i in J`, for which
every transversal together with `K` is the same signed `1+3` circuit
and

\[
                 \prod_{i\in J}{|Y_i|\over|X_i|}
                    \ge(\beta_{J,K}/8)^{4C+1}.         \tag{13}
\]

The regularity atom used here is exactly the fixed-arity,
fixed-description-complexity consequence of Fox--Pach--Suk Theorem 4.1
(the section form corresponding to their introductory Theorem 1.3)
recorded and audited in
`REDUNDANCY_CHARGED_SEMIALGEBRAIC_RETENTION.md`.

At `s=O(log n)`, (10) makes (13) only a polylogarithmic support loss.
This is an actual label tensor with a fixed physical root subset, not a
formal triple of face alphabets.

If the first branch holds, its `C_0` rooted words are distinct ordinary
faces.  Since `w_A<=1`,
\(H(P)=\log W-W^{-1}\sum_Aw_A\log w_A\ge\log W\).  Therefore

\[
                       {V(P)\over W}\ge2^{R_w-1}.       \tag{14}
\]

Under (5), (14) forces `R_w<=tau+1`.  Thus every live
quadratic-redundancy family lies in the signed physical circuit-core branch.

An MDS/orthogonal-array code of strength at least four exits through the
other branch.  Every assignment on at most four variable roles extends to
a selected rooted word, so every `Bad_{J,K}` is empty and **all**
`P_0` rooted ambient words are ordinary.  Minimum distance can destroy
selected Cartesian modules but cannot evade planar four-local completion.

## 4. Exact weighted missing-coordinate entropy split

Let `X=(X_1,...,X_s)` have the weighted law `P`.  For a projected word

\[
                         v\in\pi_{-i}E,                  \tag{15}
\]

define

\[
\begin{aligned}
 a_i(v)&=\sum_{\{x:(v,x)\in E\}}w_{(v,x)},\\
 d_i(v)&=|\{x\in X_i:T\cup v\cup\{x\}\text{ is ordinary}\}|,\\
h_i(v)&=H(X_i\mid X_{-i}=v).
\end{aligned}                                                       \tag{16}
\]

The projection law is `P_i(v)=a_i(v)/W`.  Since every individual
weight is at most one, the conditional probabilities are at most
`1/a_i(v)`; hence
\(h_i(v)\ge\log a_i(v)\).  Also
\(h_i(v)\le\log d_i(v)\).  Put

\[
\begin{aligned}
 \rho_i&=\log m_i-\mathbb E h_i(v),\\
 g_i&=\mathbb E\bigl(\log d_i(v)-h_i(v)\bigr),\\
 b_i&=\mathbb E\log{m_i\over d_i(v)}.                  \tag{17}
\end{aligned}
\]

Thus `rho_i=g_i+b_i`, and both summands are nonnegative.

> **Theorem 3 (one-gap or blocker entropy).**  Put
> `G=sum_i g_i`, `B=sum_i b_i`.  Then
> 
> \[
>                         R_w\le G+B,                    \tag{18}
> \]
> 
> and the union of the ordinary one-coordinate extension banks gives
> 
> \[
>                         {V(P)\over W}
>                           \ge {1\over s}\sum_i2^{g_i}
>                           \ge2^{G/s}.                  \tag{19}
> \]

**Proof.**  The dual-total-correlation inequality

\[
                 \sum_iH(X_i\mid X_{-i})\le H(X)       \tag{21}
\]

follows from Shearer's inequality
`sum_iH(X_-i)>=(s-1)H(X)`.  Therefore

\[
 \sum_i\rho_i
   \ge\sum_i\log m_i-H(X)=R_w,
\]

which proves (18).

For coordinate `i`, the number of ordinary extensions of selected
projections is

\[
 D_i=\sum_vd_i(v)
    =W\mathbb E{d_i(v)\over a_i(v)}
    \ge W2^{\,\mathbb E(\log d_i-\log a_i)}
    \ge W2^{g_i}.                                       \tag{22}
\]

The first inequality is Jensen, and the second uses
`h_i(v)>=log a_i(v)`.  Every output is a rooted full transversal and
can occur in at most the `s` coordinate banks.  Thus
`sum_iD_i<=sV(P)`.  This proves the first inequality in (19); the
second is again Jensen.  QED.

If `G>=R_w/2`, (19) gives the recoverable projection gain

\[
                         {V(P)\over W}\ge2^{R_w/(2s)}.  \tag{23}
\]

For `R_w=Omega(L^2)` and `s=O(L)`, this is a fixed power of `n`.

## 5. Blocker entropy produces a physical root star

Suppose instead `B>=R_w/2`.  Some coordinate satisfies

\[
                         b_i\ge {R_w\over2s}.            \tag{24}
\]

Put `b=b_i` and

\[
                   Z(v)=\log{m_i\over d_i(v)}\in[0,\log m_i].         \tag{25}
\]

Since `E Z=b`,

\[
              \Pr\{Z\ge b/2\}\ge {b\over2\log m_i}.  \tag{26}
\]

Indeed `E Z<=b/2+(log m_i)Pr{Z>=b/2}`.  For every projected source in
this positive-mass class,

\[
             d_i(v)\le m_i2^{-b/2},
 \qquad m_i-d_i(v)\ge m_i(1-2^{-b/2}).                 \tag{27}
\]

Every bad extension label `x in X_i` makes
`T union v union {x}` nonordinary, while `T union v` is ordinary.
Its bad four-circuit therefore consists of `x` and a triple
`Q subseteq T union v`.  One canonical triple blocks at least

\[
       {m_i-d_i(v)\over {s+t-1\choose3}}
       \ge {m_i(1-2^{-b/2})\over {s+t-1\choose3}}       \tag{28}
\]

actual labels.  Give a projected source `v` its genuine weight
`a_i(v)`; (26) says the displayed class retains the stated fraction
of total source weight.  The root, role colour, and projected source recover
the incidence.  Thus (26)--(28) are a genuine weighted family of
source--root--blocker incidences with only polynomial decoder loss.

When `R_w=delta L^2` and `s<=rho L`, (24) has
`b>=delta L/(2rho)`.  Equations (26)--(28) retain a constant fraction
depending only on `delta,rho` and produce blocker alphabets of size
`m_i/poly(L)`.  This is the desired fixed physical label dense core.

The conclusion does not say that all projected sources share one actual
triple.  Fixing it globally would cost up to `n^3`; at coefficient scale
that is polynomial, while at the sharper scale it should be summed using
the source--triangle tag rather than pigeonholed.

## 6. Exact relation to the excess-rank gate

Let `N` be the number of physical non-root labels in the role supports.
Since \(\sum_i m_i\le N\), AM--GM and \(H(P)\ge\log W\) give

\[
 R_w\le s\log(N/s)-\log W.                              \tag{29}
\]

In the live least-counterexample normalization, suppose

\[
 \log W\ge c(\log N)^2-o(L^2),\qquad \log N=\Theta(L).  \tag{30}
\]

Then

\[
 R_w\le (s-c\log N)\log N-s\log s+o(L^2).              \tag{31}
\]

Consequently `R_w>=delta L^2` forces
`s-c log N=Omega_delta(L)`.  This proves that the excess-rank condition
isolated in the preceding report is **necessary** for the hard weighted
redundancy branch.

The converse is false as a statement about rank alone: a high-rank family
may have entropy close to the full role-box entropy and hence small
`R_w`.  In the live proof, quadratic `R_w` must still come from the
previous high-release-redundancy transfer.  The present theorem starts
after that localization; it does not manufacture redundancy from excess
rank.

## 7. Stress tests and exact remaining gate

1. **Complete/central layer.**  Lemma 2 makes its effective support convex,
   yielding the Boolean shield.
2. **MDS transversal code.**  Strength four makes all
   `beta_{J,K}=0`, so Theorem 2 recovers the entire rooted ambient role
   product.
3. **Diagonal family in a convex radial container.**  The selected
   missing-coordinate degree is one but the ambient degree is the full
   alphabet, so `G` carries the redundancy and the one-gap/ambient bank
   pays.
4. **Cyclic Ferrers constraints.**  They may put most entropy in `B`.
   Breaking one constraint exposes the familiar one-gap chain; large
   noncommutation gives the signed four-role core of Theorem 2.

Theorems 2--3 do not automatically multiply the rolewise projection gains.
At the live normalization (5), the fixed-power factor in (23) can be
smaller than the polynomial fixed-root/description loss and is much
smaller than an `n^{Theta(log log n)}` target multiplier.  Lemma 1
removes the earlier quasipolynomial positional-colouring loss for this
local dichotomy, but does not create the missing product.  Likewise, a
single rooted fan from (28) is a localization, not the pocket multiplier.

The exact remaining statement is therefore a global summation theorem:

> across the excess-rank source slice, either the `D_i` one-gap banks for
> many roles commute with recoverable occupancy masks, or the signed
> four-role/rooted-fan cores coalesce into the already isolated dense
> physical-label Hall context with subquadratic source-description load.

A purely Kruskal--Katona shadow count cannot replace this operation.  The
MDS and diagonal families show that selected downshadows may have huge
codegree even when the ambient completion bank pays; cyclic Ferrers
families show why the payment may occur only after a role is omitted.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_excess_rank_four_local_projection.py
```

The checker exhausts binary word families with both uniform and nonuniform
weights for the entropy/projection inequalities, exhausts a finite weighted
injective-colouring instance, audits every rooted four-local pattern with
one through four variable roles, verifies the exact dense-layer threshold,
and checks every projection of size at most four in a length-five
Reed--Solomon code and its full ambient completion bank.
