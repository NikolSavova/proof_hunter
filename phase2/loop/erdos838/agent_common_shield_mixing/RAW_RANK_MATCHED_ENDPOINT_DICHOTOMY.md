# Raw rank matching at the endpoint: an exact low/high dichotomy

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The raw rank/history mismatch is not an obstruction inside the already
fixed `(W,A,p,F,tau)` fibre.  For a cell `(j,e,r)`, compare its rank-`r`
parents with the rank-`r` baseline endpoint faces.  This bucket is never
empty when the history cell is nonempty, and the exact identity is

\[
 \boxed{
 {N_{j,e,r}\over C_{e,r}}
   =4^j{q_{j,e,r}\over p_{e,r}}.}                       \tag{1}
\]

Thus depth supplies a favorable factor `4^j`; no adverse
`2^(r+2j-s)` mismatch remains.  More strongly,

\[
 \boxed{
 4^jh_{j,e}
 =\sum_r{p_{e,r}\over p_e}
             {N_{j,e,r}\over C_{e,r}}.}                \tag{2}
\]

Consequently every endpoint cell contains a same-parent-rank raw cell of
density at least `4^j h_(j,e)`.

There is an exact global low/high theorem.  At threshold `rho`, the raw
mass in low cells is at most

\[
                  \rho J V(P),                          \tag{3}
\]

where `J` is the number of peeling depths.  Their total genuine likelihood
mass is bounded more sharply by

\[
                  {4\rho\over3}V(P).                    \tag{4}
\]

Every remaining cell is a literal Hall-dense atom against its actual
rank-`r` endpoint-face bank.  Since `W,A,p,F,tau` are common fixed data in
the live residue, the interval tag is retained without an additional
decoder loss.

This settles density but not baseline **size**.  Neither a common blocked
`W` nor an exponentially large interval reservoir forces `C_(e,r)` to be
large.  An exact nested-cap/root-star family has `C_(e,2)=1`, interval
half-weight `(3/2)^m`, a fixed rank-three blocked `W`, and arbitrarily large
same-rank density supplied by one-sided inverse histories.  Thus (1) can
give `N>=rho` with no additional parent-bank multiplier.  Any later product
gain must use the inverse-history support, the blocker shield, or another
bank; it is not contained in rank matching itself.

This last qualification is necessary.  Across **varying** interval tags,
the endpoint/rank bank does not recover `W`.  A scalable planar construction
has central-binomially many ordinary interval faces `W` sharing one bad
trace `A`, one endpoint pair `e`, and the same rank-`r` endpoint bank; every
attempted union `W union R` with a bank face `R` is nonconvex.  Hence the
fixed-tag theorem cannot be summed over tags using the endpoint decoder
alone.  One must first localize a common `W`, retain `W` in a second bank,
or invoke additional planar shield structure.

## 1. Rank-resolved selected histories

Let `Omega` be any selected subfamily of canonical histories.  It may be
selected by a common interval face, bad-circuit profile, mark, shield, and
tangent state.  Let

* `N_(j,e,r)` be the number of selected depth-`j` histories whose remaining
  parent has rank `r` and endpoint pair `e`; and
* `C_(e,s)` be the number of **all** ordinary rank-`s` faces whose first and
  last labels are `e`.

Resolve the half-Gibbs laws by

\[
 q_{j,e,r}={N_{j,e,r}2^{-r}\over F4^j},\qquad
 p_{e,s}={C_{e,s}2^{-s}\over F}.                         \tag{5}
\]

If `N_(j,e,r)>0`, one of its parents is itself counted by `C_(e,r)`, so
`C_(e,r)>0`.  Setting `s=r` in the general rank identity proves (1).

Put

\[
 p_e=\sum_rp_{e,r},\qquad
 h_{j,e}={\sum_rq_{j,e,r}\over p_e}.                    \tag{6}
\]

Using (1),

\[
 4^jh_{j,e}
 =\sum_r {p_{e,r}\over p_e}
      \left(4^j{q_{j,e,r}\over p_{e,r}}\right)
 =\sum_r {p_{e,r}\over p_e}{N_{j,e,r}\over C_{e,r}},   \tag{7}
\]

where ranks with no selected histories contribute zero.  The coefficients
sum to one, proving (2) and the maximum-density conclusion.

This is the direct bucket comparison sought in the question.  Comparing
to source rank `r+2j` is unnecessary: the natural completion object is the
actual rank-`r` parent left after peeling.

## 2. Low cells sum globally after the tag is fixed

Fix the external state `(W,A,p,F,tau)`.  The selected raw histories are now
partitioned by cells `(j,e,r)`.  For `rho>0`, write

\[
 \mathcal L=\{(j,e,r):N_{j,e,r}\le\rho C_{e,r}\},\qquad
 \mathcal H=\{(j,e,r):N_{j,e,r}>\rho C_{e,r}\}.         \tag{8}
\]

> **Theorem 1 (rank-matched endpoint dichotomy).**  If at most `J` depths
> occur, then
> 
> \[
> \boxed{\sum_{c\in\mathcal L}N_c\le\rho J V(P).}       \tag{9}
> \]
> 
> If `M=sum_cN_c`, the high cells contain raw mass at least
> 
> \[
> \boxed{\sum_{c\in\mathcal H}N_c\ge M-\rho JV(P).}    \tag{10}
> \]

**Proof.**  Sum the defining low-cell inequality.  For a fixed endpoint
and rank, the same bank can occur at no more than `J` depths, so

\[
 \sum_{c\in\mathcal L}N_c
 \le\rho J\sum_{e,r}C_{e,r}.                            \tag{11}
\]

Every nontrivial ordinary face has one unique pair of extreme labels and
one rank.  Hence the endpoint/rank buckets partition the nontrivial faces,
`sum_(e,r)C_(e,r)<=V(P)`, proving (9); (10) follows by subtraction.  QED.

The overlap parameter is exactly `J`, not the number of ranks and not an
ambient power of `n`.  Grouping all depths before the split can reduce it
further, but (9) is already subpower on the bounded-rank slice.

There is also a hard ceiling on the total raw mass in a genuinely fixed
role fibre:

\[
                         \boxed{M\le J V(P).}            \tag{11a}
\]

At one depth a source face has one canonical parent, endpoint pair, and
rank, so it contributes to exactly one cell; across all active depths it
contributes at most `J` times.  With an upstream description load `L`, the
right side is `LJV(P)`.  Therefore a claimed fixed-role raw mass
`n^alpha V(P)` with `alpha>0` is not a new high-density conclusion: for
subpower `LJ` that branch is empty.  External blocker or source-mark
multiplicity must be kept explicit if it is intended to exceed this ceiling.

There is a likelihood-weight version which removes even `J`.

> **Theorem 2 (low raw density pays low likelihood mass).**  The contribution
> of the low cells to the selected likelihood tilt satisfies
> 
> \[
> \boxed{
> \sum_{j,e}\sum_{r:(j,e,r)\in\mathcal L}
>             {q_{j,e,r}\over p_e}
> \le {4\rho\over3}\binom n2
> \le {4\rho\over3}V(P).}                              \tag{12}
> \]

**Proof.**  By (1), a low cell obeys

\[
 {q_{j,e,r}\over p_e}
 ={p_{e,r}\over p_e}{1\over4^j}
                  {N_{j,e,r}\over C_{e,r}}
 \le {\rho\over4^j}{p_{e,r}\over p_e}.                \tag{13}
\]

Sum first over the low ranks.  Their `p_(e,r)/p_e` mass is at most one.
There are at most `binom(n,2)` endpoint pairs, and
`sum_(j>=0)4^(-j)=4/3`.  Finally every two-point set is an ordinary face,
so `binom(n,2)<=V(P)`.  QED.

Thus a fixed fibre whose selected likelihood mass exceeds `(4/3)rho V`
must put the excess in genuinely high raw-density cells.  This statement
uses the original `q/G` normalization exactly; it never replaces weights
by counts before the low/high split.

## 3. The high cells are literal Hall atoms

For `c=(j,e,r)`, let

\[
 \mathcal B_c=\{R\in\mathcal F(P):|R|=r,
                    (\min R,\max R)=e\}.                \tag{14}
\]

Then `|mathcal B_c|=C_(e,r)`.  Give every selected raw history in `c` the
same actual ordinary-face bank `mathcal B_c`.  The full cell has Hall
density

\[
                 {N_c\over|\mathcal B_c|}>\rho          \tag{15}

precisely when it lies in `mathcal H`.  The endpoint and rank are decoded
from every bank face.  In the live residue, the state `(W,A,p,F,tau)` was
fixed before this comparison, so it remains common side information and
is not guessed or erased.

If one starts directly from likelihood mass, (12) localizes every excess
above `D^(alpha/2)V(P)` to density-`D^(alpha/2)` cells.  By contrast, a
preceding claim of raw mass `M>=D^alpha V(P)` inside a fixed-role fibre must
first be reconciled with (11a); it is impossible for fixed-power `D^alpha`
and subpower description/depth load.

This does not by itself discharge a high atom.  It removes the proposed
rank/history ambiguity and hands the geometric descent an exact endpoint,
parent rank, depth, common interval trace, repair mark, shield, and tangent
state.

## 4. Baseline scarcity is a genuine planar branch

The identity (1) and the size of its denominator are logically separate.
There is no inequality of the form

\[
 C_{e,r}\ge F_e^delta,
 \quad C_{e,r}\ge h_{j,e}^delta,
 \quad\hbox{or}\quad
 C_{e,r}\ge2^{delta|W|}                                \tag{16}
\]

for any universal `delta>0`, even with one fixed blocked common face `W`.

Here is an exact scalable obstruction.  Put

\[
 e=\{(-2,0),(2,0)\},\qquad
 w_i=(x_i,-100-x_i^2),\quad
 x_i=-1+{2i\over m+1}.                                  \tag{17}
\]

All `w_i` lie in the open endpoint interval and form a convex cap.  Every
subset is ordinary.  As in the nested-cap lemma, `e union T` is ordinary
for `|T|<=2` and is nonconvex for `|T|>=3`.  Therefore

\[
 F_e=(3/2)^m,\qquad
 G_e={1\over4}\left(1+{m\over2}+{\binom m2\over4}\right),
 \qquad C_{e,2}=1.                                      \tag{18}
\]

Fix any three low-cap points as the common ordinary interval face `W`.
Then `e union W` is nonconvex, with a trace wholly contained in this fixed
rank-three `W`.

Place `a` points in a sufficiently small rational disk around `(-4,-4)`
and `b` points in a sufficiently small rational disk around `(4,-4)`, in
general position.  The disks can be chosen so that every four-set

\[
                  \{\ell,(-2,0),(2,0),r\},
                  \qquad \ell\in L,\ r\in R,            \tag{19}
\]

is convex.  Its depth-one parent is exactly `e`.  Hence the selected
rank-two parent cell has

\[
 N_{1,e,2}=ab,qquad
 {q_{1,e,2}\over p_{e,2}}={ab\over4},qquad
 {N_{1,e,2}\over C_{e,2}}=ab.                           \tag{20}
\]

Relative to the full endpoint law, its likelihood tilt is

\[
 h_{1,e}={ab\over
 4\left(1+m/2+\binom m2/4\right)}.                      \tag{21}
\]

Taking `a=1` and sending `b` to infinity gives a genuinely one-sided star:
the density and `h` are arbitrarily large, while the baseline bank remains
the singleton edge and the common blocked tag remains fixed.  Taking both
`a,b` large gives the familiar carrier-by-root rectangle, but that product
comes from the inverse histories in (19), not from `F_e` or `C_(e,2)`.

This family is not an EIC' counterexample.  The source faces (19), the root
support, and the Boolean low cap create other banks.  It is an exact kill of
the proposed inference “large interval reservoir or common `W` forces a
large same-rank baseline.”

## 5. Why varying interval tags cannot be silently summed

If a tag `theta` is allowed to vary, cells are
`(theta,j,e,r)`.  The exact completion-bank load becomes

\[
 \Lambda=\max_{e,r}
 |\{(\theta,j):(\theta,j,e,r)\text{ is active}\}|,       \tag{22}
\]

and the proof of Theorem 1 gives only

\[
                  \sum_{c\in\mathcal L}N_c
                         \le\rho\Lambda V(P).           \tag{23}
\]

Endpoint/rank decoding controls the depths but says nothing about
`theta=W`.  The following planar construction makes this failure exact.

Take two extreme endpoints `e={L,R}`.  Put a lower convex chain `S` between
them, so every `e union X`, `X subset S`, is ordinary.  Above the segment
`LR`, put a convex polygon `Q` with two distinguished adjacent vertices
`A={a,b}` such that `a` lies strictly inside `triangle(L,R,b)`.  This is an
open order-type condition and has rational realizations in general
position.  For a central family

\[
 \mathcal W=\{A\cup J:J\subset Q-A,
                  |J|=\lfloor(|Q|-2)/2\rfloor\},         \tag{24}
\]

every `W` is an ordinary interval face, while `e union W` is nonconvex with
the same retained witness trace `A`.  There are

\[
                    |\mathcal W|=\binom{|Q|-2}
                       {\lfloor(|Q|-2)/2\rfloor}
                       =2^{|Q|-o(|Q|)}                  \tag{25}
\]

such tags.

Fix a rank `r` and let `mathcal B_(e,r)` be the full rank-`r` endpoint bank.
For each `W in mathcal W`, use those very bank faces as the depth-zero raw
histories.  Then

\[
 N_{W,0,e,r}=C_{e,r},\qquad
 {q_{W,0,e,r}\over p_{e,r}}=1.                          \tag{26}
\]

Every tag cell has density one, but the same bank is reused
`|mathcal W|` times.  Moreover every proposed tagged union
`W union R`, `R in mathcal B_(e,r)`, contains the bad four-set
`e union A` and is therefore nonconvex.  The endpoint output cannot encode
the interval tag as one ordinary face.

This is a scalable planar obstruction to a **global varying-tag decoder**,
not an EIC' counterexample: the tag faces themselves and other shield banks
remain available.  It proves exactly why the common-`W` localization must
precede Theorems 1--2.

## 6. Coefficient audit: no unconditional gain above `1/4`

The same-rank theorem by itself gives no positive improvement in the
quadratic coefficient of `log V(P)`.  Write `L=log n`.  If a high cell has

\[
 {N_c\over C_c}=2^{(\beta+o(1))L^2},\qquad
 C_c=2^{(\gamma+o(1))L^2},                              \tag{27}
\]

then the distinct source histories only give

\[
             V(P)\ge N_c
                    =2^{(\beta+\gamma+o(1))L^2}.        \tag{28}

An improvement over the established coefficient `1/4` follows exactly
when `beta+gamma>1/4`.  Baseline scarcity shows that no positive `gamma`
is automatic.  A merely fixed-power density `D^alpha<=n^alpha` has
`beta=0` on the `L^2` scale, so it cannot change the coefficient.

In particular the previously suggested threshold `rho=n^(1/16)` changes
`log V` by only `L/16=o(L^2)`.  Moreover, summing the corresponding raw
histories over one fixed `(W,A,p,F,tau)` fibre is subject to (11a), so it
cannot produce `n^(1/8-o(1))V(P)` unless an omitted external role has been
counted with fixed-power multiplicity.

Kruskal--Katona downshadows do not alter this conclusion without an
additional structural input: the original histories are already ordinary
faces, and a uniform-rank family can have a downshadow of the same leading
logarithmic size.  Erdos--Szekeres applied only to the support of one cell
likewise supplies at most a fixed-power or `2^{o(L^2)}` factor unless it
produces a new independent convex shield.  The radial transversal examples
in the existing bank show that a large uniform-rank face family can realize
this leading-order sharpness while its one-gap bank, not its raw downshadow,
does the additional work.

Therefore the honest unconditional coefficient gain from (1)--(15) is
**zero**.  A publishable epsilon would require one of the following extra
quantitative inputs:

1. density coefficient `beta>1/4` in one cell;
2. a baseline/shield coefficient `gamma>1/4-beta`; or
3. a recoverable product bank multiplying the high cell by
   `2^{(epsilon+o(1))L^2}` with subquadratic overlap.

The common `W` and the interval reservoir alone provide none of these, by
(17)--(21).

## 7. Exact verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_raw_rank_matched_endpoint.py
```

The checker uses exact rational arithmetic.  On the nine-point two-reference
configuration it enumerates every ordinary face and canonical history,
checks (1)--(2) cell by cell, and audits both low bounds for every distinct
raw-density threshold.  It then verifies a twelve-point rational instance
of the planar tag obstruction: all triples are noncollinear, all six
uniform-rank tags are ordinary and contain the same bad trace, the common
rank-four endpoint bank has 34 faces, all six density-one cells reuse that
bank, and all `6*34=204` attempted tagged unions are nonconvex.

Finally it audits the scarcity construction with six low-cap points and
three roots on each side: the endpoint interval has exact half-weight
`(3/2)^6`, the compatible endpoint half-weight is the quadratic expression
in (18), `C_(e,2)=1`, all nine inverse rank-four histories are convex, and
the rank-resolved and aggregate tilts in (20)--(21) hold exactly.
