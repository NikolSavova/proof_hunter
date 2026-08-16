# Strict parent upper bounds do not buy a wall crossing

**Date:** 2026-08-15. All face and endpoint counts are nonempty. All
logarithms are base two.

## Verdict

The proposed strict-parent/equality-stability splice is only partly true.
The exact Pascal live-rectangle obstruction is eliminated, with a very large
margin, by weighted child minimality. But the stronger conclusion needed for
the proof does not follow from the four currently available inputs.

More precisely:

1. In the finite Pascal ledger used in
   `PASCAL_TOP_LAYER_LIVE_FIXED_EDGE_STABILITY_BARRIER.md`, the left child
   violates the necessary weighted singleton inequality

   \[
        W_A\le a+aU_A+U_Ba^2                                      \tag{1}
   \]

   by a factor exceeding \(2^{716}\). Hence some literal one-point child
   replacement decreases the whole parent. The top-layer record surplus is
   real, but this parent is on the mutation branch, not the stationary branch.
   The same conclusion holds asymptotically for every fixed-depth Pascal
   self-substitution with a \(2^{O(L\log L)}\)-face pocket.

2. Strictness of the parent upper bound supplies **zero uniform positive
   mutation budget**. If the integer forbidden threshold is \(T\), the boundary
   counterexample \(V=T-1\) is strict, but a mutation of cost one reaches
   \(T\) and leaves the counterexample class. Thus only a nonincreasing
   mutation is universally safe. In particular, the high reflection wall
   cannot be paid merely because the parent inequality is strict.

3. If all weighted singleton mutations are nondecreasing, the rank-moment
   inequalities do force a same-chart facing bank, but the exact scale is

   \[
    C_AU_B\ge {1\over4}\max\left\{{\mu_AW_A\over a},
                                  {\mu_BW_B\over b}\right\}.   \tag{1a}
   \]

   At the coefficient-half fixed-gap scale this is only the parent target
   times \(L^K/n^2\), even when both child banks are inductively live. It misses
   a useful polylog-density bank by a polynomial factor. The scalar survivor
   below attains this bound within a constant factor.

4. The all-delete history loss is exact and is not repaired by the strict
   upper. For a Cartesian record family \(\mathcal A\times\mathcal H\), routing
   a record to its released pocket face has decoder load exactly
   \(|\mathcal A|\). Division by this load leaves exactly \(|\mathcal H|\), no
   matter how large the record rectangle is. In the finite Pascal ledger the
   record surplus over the whole parent is at least \(2^{325}\), but the natural
   history load has 886 bits and exceeds the useful load threshold by more than
   \(2^{559}\). Disjoint physical circuits do not change this identity.

5. There is an exact integral scalar family satisfying the parent upper,
   reflection minimality, endpoint factorization, both weighted rank-moment
   inequalities for both children, and the new envelope comparison. It has a
   small facing bank, an unaffordable opposite wall, and an exponentially bad
   endpoint-pair decoder load. This is not asserted to be a planar profile; it
   sharply proves that the current scalar/envelope/history interface cannot
   force the desired usable same-chart bank.

6. The true nine-point minimizer does not refute a genuinely geometric
   theorem, because it has no literal strong-glue seam in any of its 72 generic
   projection chambers. In fact weighted minimality excludes it even more
   directly as a child next to any sibling of size at least four: replacing it
   by the nine-point all-cup chain decreases the weighted child objective by at
   least 27. The finite minimizer therefore lives on the **nonliteral promotion**
   side of the gate.

The exact remaining theorem is consequently narrower than the proposed
stability statement:

> A genuine least counterexample with a promoted literal seam, after every
> nonincreasing weighted child mutation has been exhausted, must admit a
> source-history-preserving conversion of part of the opposite endpoint bank
> with polylogarithmic load.

Nothing in the strict parent upper, the weighted envelope, or the fixed-edge
matching currently supplies that history-preserving conversion. The live
Pascal example is not a survivor, but it measures the missing load exactly.

## 1. Why the Pascal live rectangle is nonstationary

Use the finite instance from the Pascal barrier with

\[
 k=12,\qquad D=3,\qquad Z=T(44,22).                         \tag{2}
\]

Let \(A=Q_{12,3}\) be the threefold central Pascal substitution and let
\(P=A\prec Z\). Exact graded recurrences give the bit lengths

\[
\begin{array}{c|rrrrr}
 & |A|&C_A&U_A&W_A&U_Z\\ \hline
 \text{bit length}&53&872&872&1641&581.
\end{array}                                                  \tag{3}
\]

Weighted singleton minimality of the left child implies (1). In this
instance

\[
 {W_A\over a+aU_A+U_Za^2}>2^{716}.                            \tag{4}
\]

Therefore (1) fails, so the summed pointwise inequalities force at least one
actual singleton replacement of \(A\) to decrease \(V(P)\). This conclusion
does not rely on a scalar profile mutation: it is the contrapositive of the
physical reembedding inequality in
`STATIONARY_ALL_DELETE_WEIGHTED_PROFILE_MUTATION_GATE.md`.

The same failure is asymptotic. For fixed \(D\), write \(L=\log|A|\). The
Pascal coefficient calculation gives

\[
\begin{aligned}
 \log W_A&=\left({1\over2}+{\beta-1/2\over D}\right)L^2
                   +O_D(L\log L),\\
 \log U_A&={1\over2}\log W_A+O_D(L\log L),\qquad
 \log U_Z=O(L\log L),                                      \tag{5}
\end{aligned}
\]

where \(\beta=1-1/(4\ln2)>1/2\). Hence

\[
 \log(a+aU_A+U_Za^2)\le {1\over2}\log W_A+O_D(L\log L)
                         <\log W_A                            \tag{6}
\]

for large \(L\). Every fixed-depth Pascal realization of the top-layer
barrier is therefore rejected by weighted child minimality before the strict
parent upper is invoked.

This is the positive part of the splice: the two reports are compatible.
The local stability obstruction is real, but it is not stationary in the
global minimizer class.

## 2. The strongest same-chart bank forced by the moment inequalities

Assume no weighted singleton child mutation decreases the parent. The first
summed moment inequality gives

\[
\begin{aligned}
 \mu_AW_A
 &\le \mu_AW_A+U_BM_C(A)\\
 &\le(1+U_B)\{a+aC_A-M_C(A)\}\\
 &\le a(1+C_A)(1+U_B).                                      \tag{6a}
\end{aligned}
\]

The symmetric inequality for \(B\) gives

\[
 (1+C_A)(1+U_B)\ge
 \max\left\{{\mu_AW_A\over a},{\mu_BW_B\over b}\right\}.   \tag{6b}
\]

Since \(C_A,U_B\ge1\), one has
\((1+C_A)(1+U_B)\le4C_AU_B\), proving (1a). Thus weighted
minimality does force an actual ordinary mixed bank in the current chart.
The issue is its exact size.

For the balanced child scale \(a=b=2^{L-1}\), suppose only the inductive
lower bound

\[
 W_A,W_B\ge2^{\Phi_{1/2,K}(L-1)}.
\]

Using \(\mu_A,\mu_B\ge1\), (1a) gives

\[
 \log(C_AU_B)-\Phi_{1/2,K}(L)
 \ge -2L-{1\over2}
      +K\{L\log L-(L-1)\log(L-1)\}.                         \tag{6c}
\]

Consequently the forced bank is only
\(2^{-2L+O(\log L)}\) of the parent target, namely
\(L^{K+O(1)}/n^2\) times that target. Retaining a mean rank
\(\mu=O(L)\) improves this by another polylogarithm, not by the missing
factor \(n^2\).

This is the sharp positive equality-stability statement available from the
current moment data. It is far weaker than the desired polylog-density bank.

## 3. Exact history load in the all-delete rectangle

Let each record be \((A,H)\in\mathcal A\times\mathcal H\), and suppose the
all-delete rule releases \(H\). Then

\[
 \#\text{records}=|\mathcal A||\mathcal H|,qquad
 \operatorname{load}(H)=|\mathcal A|.                         \tag{7}
\]

Consequently

\[
 {\#\text{records}\over\text{decoder load}}=|\mathcal H|.     \tag{8}
\]

This is an equality, not a weakness of a pigeonhole estimate. Retaining a
common directed edge, every singleton trace, and many vertex-disjoint
circuits changes neither side of (7).

For the exact Pascal instance, the localized source family has 886 bits, the
pocket top layer has 1081 bits, and the parent has 1641 bits. Thus

\[
 \log { |\mathcal A||\mathcal H|\over V(P)}\ge325,             \tag{9}
\]

while release routing leaves only \(|\mathcal H|<V(P)/2^{559}\). Equivalently,
the natural source-history load exceeds the maximum useful average load by
more than \(2^{559}\). This is the exact amount of source information which a
successful converter must preserve rather than erase.

The strict parent upper only changes the comparison target from \(V(P)\) to
some \(F>V(P)\). It does not alter (7), and hence cannot reduce the history
load.

## 4. Strictness has no positive integer gap

Write the desired integer conclusion as

\[
                              V(P)\ge T(n),                    \tag{10}
\]

where \(T(n)=\lceil2^{\Phi(L)}\rceil\), if necessary. A strict
counterexample satisfies \(V(P)\le T(n)-1\). At the boundary value
\(V(P)=T(n)-1\), a mutation of cost one has value \(T(n)\), so it is no
longer a counterexample.

The same statement in the unrounded formulation is even sharper: the slack
\(2^{\Phi(L)}-V(P)\) can lie anywhere in \((0,1]\) at the last admissible
integer. Therefore the implication

\[
 \text{strict parent upper}\quad\Longrightarrow\quad
 \text{affordable positive reflection prefix}                 \tag{11}
\]

is false without a separate quantitative slack theorem. A near-wall restart
is rigorous only when its entire prefix cost is nonpositive, or when an
independently proved lower bound on the slack exceeds that cost.

## 5. A full scalar survivor of the current inequalities

The earlier scalar equality family was correctly killed by weighted child
minimality. The following family shows that this does not close the numerical
system.

Let \(d\) be a large power of two, put

\[
 m=2^d,\qquad r=d,qquad
 h={d^2\over2}-4d\log d+O(1),\qquad H=2^h,                     \tag{12}
\]

where the \(O(1)\) parity adjustment makes the next quantity integral. Set

\[
 x=2\sqrt{rH/m},\qquad y={4rH\over m},                         \tag{13}
\]

and give the two abstract children the reflected profiles

\[
\begin{array}{c|ccc}
 &W&C&U\\ \hline
 A&H&x&y\\
 B&H&y&x.
\end{array}                                                    \tag{14}
\]

Assign the rank moments

\[
 \mu_A=mu_B=r,quad
 M_C(A)=rx,quad M_U(A)=ry,quad
 M_C(B)=ry,quad M_U(B)=rx.                                   \tag{15}
\]

For \(d=64,128,256\), and in the asymptotic inequalities with room to spare,
the two distinct weighted moment conditions reduce to

\[
\begin{aligned}
 rH+rx^2&\le(1+x)\{m+mx-rx\},\\
 rH+rx^2&\le m+my-ry+xm^2.                                  \tag{16}
\end{aligned}
\]

Both hold. The other two child inequalities are identical by reflection.
Also

\[
 x\le y\le H,qquad H\le xy,                                 \tag{17}
\]

so reflection minimality, endpoint factorization, and the elementary count
bounds hold. Taking the abstract ordinary-minimizer data \(f(m)=H,p(m)=x\)
makes the weighted envelope comparison exact:

\[
 C_A=U_B=p(m),qquad W_A=W_B=f(m).                             \tag{18}
\]

The parent has

\[
 V(P)=2H+x^2=2H+{4rH\over m}.                                \tag{19}
\]

An exact discrete half-scale target with next-step exponent

\[
 h+d-8\log d                                                  \tag{20}
\]

strictly exceeds (19). Yet the opposite wall satisfies

\[
 y^2-x^2>2^{h+d-8\log d},                                    \tag{21}
\]

and the endpoint-pair load relative to ordinary faces is at least

\[
 {y^2\over V(P)}=2^{h-2d+O(\log d)},                          \tag{22}
\]

far larger than every polylogarithm. A formal all-delete rectangle of the
two dense nonfacing banks has quadratic record mass, but release routing
again has the complete source-bank load.

Moreover

\[
                     x^2={4rH\over m},                         \tag{22a}
\]

while (1a) only forces \(x^2\ge rH/(4m)\). Thus the survivor lies within a
factor 16 of the strongest facing-bank conclusion obtainable from the full
rank-moment inequality. The polynomial deficit in (6c) is not an artifact of
discarding moment information.

This family is deliberately labelled a **scalar survivor**, not a planar
construction. Realizing (12)--(15) by a stretchable minimizer would be as
hard as the original problem. Its role is exact logical separation: the
parent upper, the envelope bounds, all four rank-moment inequalities,
reflection minimality, and the history ledger have no numerical
contradiction. The missing input must be planar and history-sensitive.

## 6. The true nine-point minimizer sits outside the literal seam

The exact nine-point minimizer has

\[
 f(9)=168,qquad p(9)=82,qquad \ell_9=45.                     \tag{23}
\]

If it were the left child of a globally minimal literal seam, with facing
penalty \(t=U_B\), the all-cup nine-point chain would be a permissible child
replacement. Weighted optimality would require

\[
 168+82t\le511+45t,qquad\text{hence}\qquad t\le{343\over37}.  \tag{24}
\]

Every child of size at least four has \(U_B\ge4+\binom42=10\). Therefore
(24) fails, and at the smallest possible penalty the replacement decreases
the parent by

\[
 (168+82\cdot10)-(511+45\cdot10)=27.                          \tag{25}
\]

Using any other projection chamber only increases the cap count and makes
the decrease larger.

An independent exhaustive set-system check considers all 72 generic
projection orders and every one of their eight contiguous cuts. No cut
satisfies the exact strong-glue face classification. The closest cut still
misclassifies ten subsets. Thus the genuine minimizer neither supplies a
stationary child calibration nor a literal seam counterexample. It confirms
the scope boundary: promotion to a physical two-block chart remains a real
geometric theorem, not a bookkeeping step.

## 7. What would finish the splice

The surviving branch has all of the following properties simultaneously:

* every weighted child mutation is nondecreasing;
* the facing endpoint product is below the parent target;
* the opposite endpoint product is huge but lies behind an unaffordable wall;
* the parent endpoint reset has at least the fixed-gap polylogarithmic energy;
* all-delete records lose their source history at a load much larger than that
  polylogarithmic energy.

A valid closure must therefore prove one of two genuinely new statements.

1. **Planar Pareto curvature:** the scalar survivor (12)--(18) cannot be the
   directional weighted envelope of realizable minimizers; quantitatively,
   some child replacement is nonincreasing.
2. **History-preserving endpoint conversion:** a positive slice of the
   opposite cap--cup bank can be realized in the current chart with decoder
   load below the endpoint-reset surplus, without first paying the full
   reflection wall.

Neither follows from strictness alone. The first is a theorem about
directional profiles of ordinary minimizers; the second is precisely the
root/carrier-history statement absent from the local fixed-edge matching.

## 8. Verification

Run:

```bash
python3 phase2/loop/erdos838/agent_strict_parent_profile_rigidity/verify_strict_parent_profile_rigidity_gate.py
```

The checker uses exact integer and rational arithmetic. It reconstructs the
finite Pascal ledger and its weighted mutation failure, audits the exact
source-history load, verifies the full scalar survivor at three enormous
scales, enumerates every projection chamber and contiguous seam of the true
nine-point minimizer, and checks the all-cup weighted replacement decrease.
