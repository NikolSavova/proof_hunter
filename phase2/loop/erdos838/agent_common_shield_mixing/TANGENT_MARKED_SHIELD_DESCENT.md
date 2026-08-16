# Tangent-marked shield descent: guarded Carleson and the omitted-petal barrier

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

The completion insertion edge and its full tangent cell can be retained at
no ambient `n^4` cost.  If

\[
                         S=Q\cup\{p\}                       \tag{1}
\]

is a repaired rank-`q+1` star, the cyclic order of `S` contains five
consecutive vertices

\[
                         \tau(S)=(a,u,p,v,b),               \tag{2}

where `uv` is the edge of `Q` replaced by `p`, and `a,b` are the other
neighbours of `u,v`.  Keep these five vertices and delete `t` of the other
`q-4` vertices.  Every star supplies

\[
                         B_t=\binom{q-4}{t}                 \tag{3}

ordinary marked downfaces.  From one output and the marked vertex `p`, its
cyclic neighbours recover `u,v`, and their other neighbours recover `a,b`.
Thus different insertion edges or tangent cells never collide in this
bank.

For a weighted family of stars inside one already-localized common marked
shield bin `(p,F)`, let `W` be its total weight and `Lambda_t` the maximum
weight of histories producing one guarded downface.  Then

\[
 \boxed{WB_t\le\Lambda_tV(P).}                             \tag{4}
\]

Across varying marks the right side is only multiplied by `q+1`, since the
mark has at most `q+1` choices in the output.  If the total history weight
in one tangent cell is at most `A`, then `Lambda_t<=A`; hence

\[
                         V(P)\ge {WB_t\over A}.             \tag{5}

This is the requested high-edge-diversity saving.  With central
`t=(q-4)/2`, `B_t=2^{q-o(q)}`.  Whenever
`A<=B_t/D^epsilon`, (5) gives a fixed `D^epsilon` gain over the injective
star count.

The corresponding Cauchy theorem is equally clean.  Put `N=WB_t` for unit
weights, or use the weighted incidence mass.  If a `theta` share of
same-output collisions splices to one ordinary face with load `L`, with
diagonal parameter `alpha` and exceptional budget `beta N`, then

\[
 {N\over V(P)}\le
 {c+\sqrt{c^2+8L/\theta}\over2},
 \qquad c=\alpha+{2\beta\over\theta}.                      \tag{6}

Thus edge diversity and every positive-density splice branch are paid.

The high-overlap fibre has an exact classification.  One guarded output
`T` fixes `(a,u,p,v,b)` and a common convex prefix

\[
                         B=T-\{p\}.                         \tag{7}

Every carrier is uniquely

\[
              S_D=T\cup D,\qquad Q_D=B\cup D,
              \qquad |D|=t.                               \tag{8}

For two distinct pairwise detached-incompatible completions, a first bad
four-circuit meets both `D-D'` and `D'-D`.  Therefore the next genuinely
missing history coordinate is the **omitted completion petal `D`**.  The
edge, both tangent neighbours, repair mark, shield face, and retained
prefix are all already fixed and recoverable.

This final atom is realizable at quadratic entropy.  In the radial repair-
star construction, fix the representatives in the four blocks
`X_(q-1),X_0,X_1,X_2` around the repair edge and vary the remaining
`q-4` blocks.  For a fixed `p` and a fixed internal shield face `F`
containing it, all `L^(q-4)` completions have the same
`(tau,p,F)`, injective maximal stars, and nonconvex star--shield unions.
The guarded downface overlap is exactly the number of choices in the
deleted active blocks.  Its radial cyclic one-gap banks pay globally, so
this is not an EIC' counterexample; it is a sharp barrier to any argument
using only the recovered tangent cell, mark, shield, and prefix.

## 1. Exact recovery of the tangent cell

Orient the cyclic boundary of the repaired star `S`.  Since `p` is an
exterior insertion into the edge `uv` of `Q`, the local cyclic order is

\[
                     \cdots,a,u,p,v,b,\cdots.              \tag{9}

The reverse orientation gives the same unoriented cell.  Define

\[
 \mathcal D_t(S,p)=\{S-D:D\subseteq S-\{a,u,p,v,b\},
                              |D|=t\}.                     \tag{10}

Every member is an ordinary face by heredity, and (3) is immediate.

> **Lemma 1 (guarded output decoder).**  From a marked output
> `(p,T)`, `T in mathcal D_t(S,p)`, one recovers the insertion edge `uv`
> and the tangent cell `tau(S)` up to reversal.

**Proof.**  In the convex polygon `T`, the two cyclic neighbours of `p`
are exactly `u,v`, because every vertex in (2) was protected.  The other
neighbour of `u` is `a`, and the other neighbour of `v` is `b`.  Deleting
vertices outside (2) cannot change these four local adjacencies.  QED.

The five-vertex protection costs only a constant shift in the Boolean
exponent.  At a central deletion level,

\[
 \binom{q-4}{\lfloor(q-4)/2\rfloor}
                      ={2^{q-4}\over\operatorname{poly}(q)}. \tag{11}

Most importantly, Lemma 1 replaces an `n^2` edge guess or `n^4` tangent-
cell guess by exact recovery from the ordinary output.

## 2. Guarded Carleson theorem

Let `Omega` be a weighted multiset of repaired stars, already lying in one
fixed marked-shield fibre `(p,F)`.  Stars may repeat as histories.  For an
ordinary marked output `T`, put

\[
 \lambda_t(T)=\sum_{\omega:T\in\mathcal D_t(S_\omega,p)}w_\omega,
 \qquad
 \Lambda_t=\max_T\lambda_t(T),
 \qquad W=\sum_\omega w_\omega.                            \tag{12}

> **Theorem 2 (tangent-guarded Carleson).**  Equation (4) holds.
> If `A` is the maximum total history weight in any one tangent cell, then
> `Lambda_t<=A`, giving (5).

**Proof.**  Double-count the incidences `(omega,T)`:

\[
 WB_t=\sum_T\lambda_t(T)\le\Lambda_tV(P).                  \tag{13}

By Lemma 1, all histories producing a fixed `T` have the same tangent
cell.  Their total weight is at most `A`, so `Lambda_t<=A`.  QED.

If the common mark has not yet been fixed, count outputs as marked pairs
`(p,T)`.  There are at most

\[
                         \sum_T|T|\le(q+1)V(P)             \tag{14}

such pairs, giving

\[
                 WB_t\le\Lambda_t(q+1)V(P).               \tag{15}

Thus mark diversity also costs only a rank factor.  The shield `F` need
not be encoded again at this stage: the preceding marked Carleson/collision
descent has already fixed the actual pair `(p,F)`.

## 3. Guarded collision Cauchy

Regard every incidence `(omega,T)` in (10) as an occurrence of weight
`w_omega`.  Let

\[
 N=WB_t,qquad
 \Delta=B_t\sum_\omega w_\omega^2\le\alpha N.             \tag{16}

Because the common mark is fixed, there are at most `V=V(P)` output bins.
Writing `s_T=lambda_t(T)`, Cauchy gives

\[
 \mathcal C={1\over2}\left(\sum_Ts_T^2-\Delta\right)
       \ge {1\over2}\left({N^2\over V}-\Delta\right).     \tag{17}

Suppose good collision weight `G` obeys

\[
                       G\ge\theta\mathcal C-\beta N       \tag{18}

and maps to ordinary splice faces with total weight at most `L` per face.
Then `G<=LV`.  Substitution in (17), division by `V`, and solution of the
resulting quadratic prove (6).  With unit incidences, `alpha=1`.

This theorem can use any geometric splice associated with two completions
which collide at the same guarded prefix.  If no such splice has positive
energy, the first bad circuit is already localized to the omitted petals,
as follows.

## 4. Exact high-fibre classification

Fix a marked output `T` with at least two preimages.  Lemma 1 fixes the
same cell `tau=(a,u,p,v,b)` for all of them.  Put `B=T-p`.  For history
`omega`, let

\[
                         D_\omega=S_\omega-T.              \tag{19}

Then `|D_omega|=t` and (8) holds.  The set `D_omega` uniquely recovers the
star, so distinct geometric completions give distinct petals.

> **Lemma 3 (first circuit is cross-petal).**  If
> `Q_D=B union D` and `Q_D'=B union D'` are individually ordinary but
> their detached union is not, then a bad four-circuit in their union meets
> both `D-D'` and `D'-D`.

**Proof.**  A bad circuit exists by planar Caratheodory.  It cannot be
contained in either ordinary face `B union D` or `B union D'`.  Hence it
contains a point absent from each carrier, which is precisely the stated
pair of symmetric differences.  QED.

The fixed data in the high fibre are now:

1. the actual repair label `p`;
2. the actual shield face `F` containing `p`;
3. the insertion edge `uv`;
4. both tangent neighbours `a,b`;
5. the common retained prefix `B`, including the four tangent guards; and
6. the uniform petal rank `t`.

The only variable is `D`.  Any further common-fibre theorem which does not
use `D` is false for the construction below.

## 5. Scalable cell-mark-shield barrier

Take the radial completion/repair construction with active blocks
`X_0,...,X_(q-1)` of size `L`, and a projectively universal repair block
`Y` beyond the edge between `X_0,X_1`.  Fix one representative in each of

\[
                         X_(q-1),X_0,X_1,X_2.              \tag{20}

Let the remaining `q-4` representatives vary freely.  There are

\[
                              M_0=L^{q-4}                  \tag{21}

pairwise detached-incompatible completions.  Fix `p in Y` and an internal
ordinary face `F subseteq Y` containing `p`.  Every completion has the same
tangent cell `(a,u,p,v,b)` from (20), the same marked shield `(p,F)`, and a
distinct maximal star.

Every attempted star--shield union with `F ne {p}` contains the bad repair
circuit on `u,v,p` and a second label of `F`.  Thus the shield does not
splice.  Pairwise completion incompatibility is witnessed in the first
active block where their words differ.  For

\[
             q=\Theta(\log D),\qquad L=D^\delta,           \tag{22}

equation (21) has `log M_0=Theta((log D)^2)`.  Hence fixing the complete
tangent cell costs only four `log L=O(log D)` bits and preserves the
quadratic entropy of the hard family.

For the complete product subfamily, delete `t` of the `q-4` variable
coordinates.  A guarded output records the other `q-4-t` coordinate values
and forgets exactly the deleted values.  Consequently

\[
 \begin{split}
 \#\text{incidences}&=L^{q-4}\binom{q-4}{t},\\
 \#\text{distinct guarded outputs}
      &=\binom{q-4}{t}L^{q-4-t},\\
 \text{load of every output}&=L^t.                        \tag{23}
 \end{split}

Thus the high-fibre multiplicity is exactly the number of omitted petals;
there is no hidden edge, mark, shield, or tangent ambiguity left.  The
radial one-gap theorem pays this construction through other cyclic banks,
so (23) is an interface barrier rather than an EIC' counterexample.

## 6. Exact rational audit

The verifier uses eight rational two-point radial blocks.  Their outer
points are

\[
 (-3,-1),(-2,-3),(1,-4),(3,-2),(4,1),(2,3),(-1,4),(-4,2), \tag{24}
\]

and their slightly perturbed inner points are listed in the verifier.  All
`2^8=256` transversals are convex and every pair of transversals is
detached-incompatible.

The four repair labels are

\[
 Y=\{(-177/70,-141/70),(-2983/1180,-1187/590),
       (-101/40,-121/60),(-1619/640,-641/320)\}.            \tag{25}

They have a nonconvex internal order type but are totally nested relative
all completion choices.  Hence all `1024` repair stars are ordinary and
every two-label repair extension is nonconvex.

Fix the outer representatives in blocks `7,0,1,2`, the first repair label
`p`, and a three-label internal shield face containing `p`.  The remaining
four binary blocks give `M_0=16` completions in one common
`(tau,p,F)` fibre.  At deletion depth `t`, exact enumeration gives

\[
 \#\text{outputs}=\binom4t2^{4-t},\qquad
 \text{load}=2^t                                      \tag{26}

for every `0<=t<=4`.  At `t=2` there are `96` incidences, `24` outputs,
and exact load four.  Every output recovers the same five-vertex tangent
cell by cyclic adjacency, verifying the decoder rather than merely the
counts.

## 7. Final boundary

The tangent refinement closes every branch with sufficiently diverse
cells or bounded guarded-prefix codegree.  Its failure is no longer a
vague “common repair blocker” case.  It is the following explicit atom:

> one fixed tangent-guarded convex prefix `B`, one fixed insertion edge,
> one fixed repair mark `p`, one fixed shield face `F`, and a large uniform
> family of omitted petals `D` whose pairwise unions create cross-petal
> four-circuits.

This is exactly the heavy common-base completion atom, now with all repair
geometry retained.  The next theorem must exploit the distribution of the
petals `D`--for example their own circuit components, a central shadow of
the deleted coordinates, or a cyclic container profile.  No further
tangent-cell refinement is available: the complete radial product realizes
the remaining fibre with the sharp load `L^t` in (23).
