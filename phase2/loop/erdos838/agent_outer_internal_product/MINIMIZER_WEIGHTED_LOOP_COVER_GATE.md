# Rank-safe minimizer marking and the loop-cover entropy gate

**Date:** 2026-08-15.  All logarithms are base two and the empty face is
counted.

## Verdict

There is a useful correction to the minimizer-to-pocket splice.  Raw
canonical incidences `(A,T)` are biased by as much as `|A|^2`, so the
uniform mean rank does not by itself justify an `O(log n)` cutoff for that
raw incidence measure.  Assigning each blocked point to one canonical
tangent witness and giving the resulting record weight `1/n` removes the
bias exactly.

Let `V` be the number of ordinary faces, `mu` their uniform mean rank, `R`
their maximum rank, and

\[
 D_0={n-2\mu\over(R-2)\mu}.
\]

There is a weighted family of actual rooted marked incidences `(A,T)` of
total weight at least

\[
 \boxed{\displaystyle {n-2\mu\over2n}V}                 \tag{1}
\]

such that every source `A` carries weight at most one and every root has a
deterministic role-pocket of size at least `D_0/8`.  Hence, for every
`K>0`, the part with

\[
                         |A|\le K\mu                    \tag{2}
\]

has weight at least

\[
 \boxed{\displaystyle
 \left({n-2\mu\over2n}-{1\over K}\right)V.}             \tag{3}
\]

For a low-mean minimizer, `mu=O(log n)=o(n)`, so `K=4` already leaves
positive `Theta(V)` weighted mass at source rank `O(log n)`.  The global
marked-pocket release decoder remains valid for these fractional weights.

Combining this corrected slice with the exact average blocker-cover bank
gives a sharp conditional theorem.  If rooted complete-product charts of
total source mass `M>=eta V` and pocket face count at least `H` have
aggregate released-output load `Lambda`, then their product-weighted mean
deleted alphabet entropy satisfies

\[
 \boxed{\displaystyle
       \overline\sigma\ge\log {\eta H\over\Lambda}.}     \tag{4}
\]

Thus `log H>=(1/4-o(1))(log n)^2`, `eta=2^{-o((log n)^2)}`, and
`Lambda=2^{o((log n)^2)}` force

\[
                  \overline\sigma\ge
                    (1/4-o(1))(\log n)^2.               \tag{5}
\]

Weighted vertex-cover duality then forces either mean mandatory `3+1` loop
entropy at least `(1/8-o(1))(log n)^2`, or mean fractional `2+2` packing at
least `(1/16-o(1))(log n)^2`.

The low-source-rank conclusion supplied by the uniform mean does **not**
rule out the loop alternative.  It bounds the number of occupied roles by
`O(log n)`, but each role label still costs `Theta(log n)` bits.  An exact
rooted planar cap construction realizes
`q=Theta(log n)` mandatory loop roles, `A^q` canonical rank-`O(log n)`
sources, and deleted entropy

\[
                  q\log A=Theta((\log n)^2).             \tag{6}
\]

The easy realization exposes a common convex outer shield and therefore
does not carry `Theta(V)` marked mass under the low-mean minimizer law.
Suppressing that shield while keeping the complete source product is
exactly the unresolved projective-child/common-guard cap--cup alignment
gate.  No bounded-rank planar `Theta(V)` regression is claimed here, and
there is no EIC' closure.

The rigorous advance is therefore twofold: the live minimizer mass really
does survive an `O(log n)` rank cutoff, and the remaining high-loop escape
is not excluded by that cutoff.  It is a genuine quadratic alphabet-entropy
problem with the precise decoder/coexistence hypothesis displayed in (4).

## 1. Rank-safe blocked-point marking

For a face `A`, let `b(A)` be the number of labels `p` for which
`A union {p}` is nonconvex.  Cover balance gives

\[
                         \mathbb E b(A)=n-2\mu.          \tag{7}
\]

Let `mathcal T(A)` be the canonical tangent-triple cover from
`WEIGHTED_ROOT_STAR_MINIMIZER_OBSTRUCTION.md`.  It satisfies

\[
 |\mathcal T(A)|\le |A|(|A|-2),                         \tag{8}
\]

and every blocked label has a witnessing triple in `mathcal T(A)`.  Fix a
global order of triples.  For every blocked pair `(A,p)`, assign `p` to the
first witness and denote it by `T_A(p)`.

Call this record heavy when

\[
                         d(T_A(p))\ge D_0/2.             \tag{9}
\]

For a fixed face and fixed triple, at most `d(T)` labels can be assigned to
that triple.  Therefore the number `b_L(A)` of light assigned records obeys

\[
 b_L(A)
 \le \sum_{\substack{T\in\mathcal T(A)\\d(T)<D_0/2}}d(T)
 \le {D_0\over2}|A|(|A|-2).                            \tag{10}
\]

Averaging and using `|A|<=R` gives

\[
 \begin{aligned}
 \sum_A b_L(A)
 &\le {D_0\over2}V\,\mathbb E[|A|(|A|-2)_+]\\
 &\le {D_0\over2}V(R-2)\mu
  ={V(n-2\mu)\over2}.                                  \tag{11}
 \end{aligned}
\]

Together with (7), at least `V(n-2mu)/2` blocked records are heavy.
Aggregate them by `(A,T)` and put

\[
 \omega(A,T)={1\over n}
   |\{p:T_A(p)=T\text{ and the record is heavy}\}|.     \tag{12}
\]

This proves (1).  More importantly,

\[
                  \sum_T\omega(A,T)\le {b(A)\over n}\le1
                                                                  \tag{13}
\]

for every source face separately.  Markov under the **uniform face law**
now gives

\[
 \sum_{\substack{A,T\\|A|>K\mu}}\omega(A,T)
 \le |\{A:|A|>K\mu\}|\le {V\over K},                  \tag{14}
\]

which proves (3).  This is the step that is unavailable for raw `(A,T)`
counts.

For every heavy `T`, choose its deterministic largest rooted circuit class
`X_T`.  Then

\[
                         |X_T|\ge d(T)/4\ge D_0/8,       \tag{15}
\]

and `A cap X_T` is empty whenever `omega(A,T)>0`, since `T subset A` and a
bad four-circuit cannot be a subset of the convex face `A`.

## 2. Weighted global release survives unchanged

For `(A,T)`, let `tau(A,T)` and `b_g(A,T)` be the exact guard number and
partial release count from `GLOBAL_MARKED_POCKET_RELEASE.md`.  Put

\[
              L_g={n\choose3}\sum_{i=0}^g{n\choose i}. \tag{16}
\]

> **Theorem 1 (rank-safe weighted marked release).**
>
> \[
> \boxed{\displaystyle
>   \sum_{A,T}\omega(A,T)b_g(A,T)\le L_gV.}             \tag{17}
> \]
>
> Consequently, if `H=min_T V(P|X_T)`, then
>
> \[
> \boxed{\displaystyle
>   \sum_{\tau(A,T)\le g}\omega(A,T)\le {L_gV\over H}.}\tag{18}
> \]

**Proof.**  Output `(A setminus G) union F`.  Given the output and the
guessed `(T,G)`, the deterministic pocket gives

\[
        F=C\cap X_T,\qquad A=(C\setminus F)\cup G.      \tag{19}
\]

Thus an output has at most `L_g` possible records.  Each has weight at most
one by (13), proving (17).  If `tau<=g`, one guard releases all `H` pocket
faces, so `b_g>=H`; (18) follows.  QED.

In particular, (3), (16), and (18) put the already proved
`Theta(log n)` guard lower bound on a genuine `Theta(V)`, rank-`O(log n)`
weighted slice.  No raw-incidence cutoff is needed.

## 3. Global average-cover theorem with the exact missing decoder

A **rooted release chart** `c` consists of a fixed retained root edge, a
local ordinary-face family `mathcal H_c`, and disjoint external role
supports of sizes

\[
                         L_{c,1},\ldots,L_{c,q_c}.       \tag{20}
\]

Write `P_c=prod_r L_(c,r)` and `H_c=|mathcal H_c|`.  Assume the chart has
the exact four-local blocker graph described in
`BLOCKER_ROLE_COVER_RELEASE_DICHOTOMY.md`.  For `F in mathcal H_c`, let
`J_c(F)` be its canonical minimum-cost circuit cover and put

\[
             \sigma_c(F)=\sum_{r\in J_c(F)}\log L_{c,r}.\tag{21}
\]

The output occupies every role outside `J_c(F)`.  Its occupancy mask
recovers the cover, so the chart contributes exactly

\[
                 P_c\sum_{F\in\mathcal H_c}2^{-\sigma_c(F)}
                                                                  \tag{22}
\]

ordinary output records.  Let `Lambda` be the **actual aggregate maximum
multiplicity** of one ordinary output across all charts, including roots,
bases, carriers, and role descriptions.

> **Theorem 2 (global marked average-cover gate).**  Put
>
> \[
> N=\sum_cP_cH_c,
> \qquad
> \overline\sigma={1\over N}
>       \sum_cP_c\sum_{F\in\mathcal H_c}\sigma_c(F).    \tag{23}
> \]
>
> Then
>
> \[
> \boxed{\displaystyle
>                N2^{-\overline\sigma}\le\Lambda V.}   \tag{24}
> \]
>
> If `sum_cP_c>=M>=eta V` and `H_c>=H`, then (4) follows.

**Proof.**  Sum (22) over charts.  Jensen for `2^{-x}`, with each local
face repeated with weight `P_c`, gives at least
`N2^{-overline sigma}` records.  By the definition of `Lambda`, their sum
is at most `Lambda V`, proving (24).  Since `N>=HM>=eta HV`, cancellation
of `V` proves (4).  QED.

This theorem does not hide a copy of `V` per root or per carrier.  It also
states exactly what the present minimizer reductions do **not** yet supply:
a complete-product extraction whose released occupancy masks have
`Lambda=2^{o((log n)^2)}` across all marked bases.

Let `ell_c(F)` be the cost of mandatory loop roles and let
`nu_c^*(F)` be the capacitated fractional matching value of the remaining
`2+2` graph.  Pointwise weighted vertex-cover duality gives

\[
                 \sigma_c(F)\le\ell_c(F)+2\nu_c^*(F). \tag{25}
\]

Averaging with the weights in (23), (5) and (25) imply

\[
 \boxed{
 \overline\ell\ge(1/8-o(1))(\log n)^2
 \quad\hbox{or}\quad
 \overline\nu^*\ge(1/16-o(1))(\log n)^2.}             \tag{26}
\]

Equation (26) is the exact high-loop/high-crossing interface on the
rank-safe minimizer slice.

### 3.1 A common outer shield cannot carry the hard mass

There is one unconditional concentration consequence.  Suppose all
rank-at-most-`h` marked sources in a fibre are subsets of one convex outer
carrier `Q`.  Since `Q` is itself a face, `|Q|<=R`, and (13) gives

\[
 \boxed{\displaystyle
   \sum_{\substack{A\subseteq Q,\ |A|\le h\\
                    T:\omega(A,T)>0}}
       \omega(A,T)
   \le\sum_{j=0}^h {R\choose j}.}                       \tag{26a}
\]

On the minimizer slice `h=O(log n)` and
`R=O((log n)^2)`, so

\[
                  \log\sum_{j=0}^h{R\choose j}
                        =O((\log n)\log\log n).          \tag{26b}
\]

Thus one common convex cage or outer shield carries only
`2^{o((log n)^2)}` of the `Theta(V)` weighted mass.  When
`log V=Theta((log n)^2)` and occurrences are assigned to canonical carrier
fibres, a live high-loop branch must use
`2^{Theta((log n)^2)-o((log n)^2)}` distinct carriers.  Those carriers are
distinct ordinary faces and hence give a correct linear bank, but (26a)
alone does not multiply that bank by the pocket reservoir.  The aggregate
decoder `Lambda` in Theorem 2 is exactly the missing global consolidation
variable.

## 4. Why low mean does not make loop entropy subquadratic

The cutoff (2) gives only `q_c<=Kmu=O(log n)` occupied roles.  Since a role
may have up to `n` labels,

\[
               \ell_c(F)\le q_c\log n=O((\log n)^2),   \tag{27}
\]

and this estimate is sharp in its exponent.

Here is an exact rooted planar realization.  Put

\[
 a=(0,-1),\quad b=(4,-1),\quad c_0=(0,4),              \tag{28}
\]

and, for `1<=t<=h`,

\[
 P_t=\left(2-\delta t^2,-{1\over5}+\delta t\right),
 \qquad \delta={1\over100h^2}.                         \tag{29}
\]

On a sufficiently short rational cap around `c_0`, put disjoint role
supports `Y_1,...,Y_q`, each of size `A`.  They may be chosen on
`y=4-x^2`.  The strict determinant audit from
`BLOCKER_ROLE_HITTING_SET_BARRIER.md` gives

\[
 P_j\in\operatorname{int}\operatorname{conv}\{P_i,P_k,y\}
 \quad(i<j<k,\ y\in Y_r).                              \tag{30}
\]

The root

\[
                              T=\{a,b,c_0\}             \tag{31}
\]

is canonical in every source

\[
                T\cup\{y_r:y_r\in Y_r, 1\le r\le q\};\tag{32}
\]

the edge `ab` stays exposed.  Every `P_t` is inside `T`, whereas every
upper-cap label is compatible with `T`; hence the deterministic rooted
pocket is precisely the local cap.  There are exactly `A^q` sources in
(32), all of rank `q+3`.  If `a,b,c_0` are the first three labels, `T` is
also the first canonical witness of every blocked local label.  Thus this
is an actual instance of the rank-safe marking in Section 1, not an
unmarked product model.  Every local face containing three `P` labels has a
mandatory loop at every role by (30), and therefore

\[
                         \sigma=q\log A.                \tag{33}
\]

For the quadratic version, replace each `P_t` by an `A`-label microblock in
a sufficiently small neighbourhood and retain the `A^h` local
transversals.  All strict containments persist.  Taking

\[
                    h=\lfloor\alpha\log A\rfloor,
 \qquad             q=\lfloor\gamma\log A\rfloor      \tag{34}
\]

gives a local pocket family and marked source family with

\[
 \log A^h=(\alpha+o(1))(\log D)^2,
 \qquad
 \log A^q=(\gamma+o(1))(\log D)^2,                    \tag{35}
\]

while both relevant ranks are `O(log D)` and all blocker entropy is in
`3+1` loops.  The blocked-point weight of each source is
`hA/D=Theta(1)`, so the marked weighted mass is `Theta(A^q)`.

In this elementary realization the entire upper cap is convex.  Its
Boolean outer shield is much larger than the selected product (32), and its
large ranks violate the live low-mean/minimizer regime.  Replacing every
macroscopic cap microblock by an arbitrary low-face projective child is
allowed locally, but controlling the full face count then becomes the
heterogeneous cap--cup recurrence of
`COMMON_GUARD_PROFILE_RAMP_BARRIER.md`.  A `Theta(V)` realization with
quadratic marked mass would therefore require precisely the unresolved
anti-alignment/substitution step.  The present data neither rule it out nor
construct it.

This separates the conclusions cleanly:

* low mean **does** give the rank-safe weighted slice (3);
* low rank **does not** imply `overline sigma=o((log n)^2)`;
* a low-overlap complete-product extraction closes by (4);
* the sole loop-heavy escape is suppression of the common outer shield
  without creating the cap--cup/profile bank.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_minimizer_weighted_loop_cover.py
```

The checker recomputes all 169 faces of the certified nine-point minimizer,
assigns every blocked point to its first canonical tangent witness, and
audits (10)--(14) with exact rational arithmetic.  It then constructs a
14-point rational instance of (28)--(32), verifies general position, the
canonical root, its exact role-pocket, all source transversals, every
mandatory loop, every circuit-cover/release equivalence, the disjoint
occupancy-mask bank, and the finite Jensen inequality behind (24).
