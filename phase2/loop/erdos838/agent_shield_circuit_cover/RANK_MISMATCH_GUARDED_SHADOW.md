# Rank mismatch: endpoint Hall split and the sharp guarded-shadow gate

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

There is a simpler raw-count dichotomy before any rank transfer is used.
For an endpoint pair `e=(x,y)`, let

\[
 \mathcal B_e=\{U\in\mathcal F(P):\min U=x,\ \max U=y\}.
                                                               \tag{1}
\]

The nontrivial face families `\mathcal B_e` are disjoint as `e` varies.
If raw history cells over one endpoint have at most `J` possible auxiliary
states, then, for every `rho>0`, the cells of density at most `rho` contain
at most

\[
                         \rho J V(P)                         \tag{2}
\]

histories.  Every remaining cell has literal raw density greater than
`rho` against its actual endpoint-face bank.  Thus, whenever arbitrary
ordinary endpoint faces are legitimate global EIC payment, choosing
`rho=D_0^(1-epsilon)/J` removes the rank-mismatch gate with only the
subpower state loss `J`.  Any already fixed common interval face, repair
mark, or circuit role remains fixed on the surviving histories.

This statement does **not** say that the bank faces retain those marks, or
coexist with the common interval face.  It is a global ordinary-face
charge.  If the local architecture requires a mark-retaining output, the
guarded-shadow theorem below is the exact substitute.

For rank transfer itself, put `b=s-k`, let `G` be a protected guard of rank
`g` (the endpoint-only case has `g=2`), and define

\[
 R_{s,k,g}=\binom{s-g}{k-g}=\binom{k+b-g}{b},\qquad
 \beta=2^b.                                                \tag{3}
\]

Every rank-`s` endpoint face supplies exactly `R_(s,k,g)` guarded
rank-`k` downfaces.  If `Delta` is the largest number of baseline faces
containing one guarded output, then `beta` clones of every baseline face
route to ordinary guarded downfaces with maximum congestion

\[
                  K\le\left\lceil{\beta\Delta\over
                                      R_{s,k,g}}\right\rceil .       \tag{4}
\]

This is sharp.  Failure at target congestion `L` fixes a genuine common
rank-`k` endpoint prefix `T` lying in more than `R L/beta` rank-`s`
faces.  If these faces are distinct, writing them as `T union D`, the
fixed fibre has the exact local Boolean bank

\[
 \{G\cup A\cup D:A\subseteq T-G\},
 \qquad\text{of size }2^{k-g}|\mathcal D|.                \tag{5}
\]

Hence the heavy prefix itself recovers the desired factor whenever
`k-g>=b`.  In the mismatch-poor regime `k-g<b`, neither (3) nor (5) must
contain `2^b` symbols.  There one genuinely needs the variable-petal
shield.  Compatible petal pairs give an exact mixed bank, while every bad
pair has a planar four-circuit crossing both petal differences.

The complete convex endpoint layer is a scalable, bounded-rank regression
showing that no rank-only subpower bound on `Delta` is possible.  Its
guarded-shadow congestion is exactly (4), and can be a fixed power or much
larger.  This is not an EIC counterexample: the common petal support is in
convex position and its full Boolean shield pays overwhelmingly.

## 1. The endpoint partition removes raw rank mismatch globally

Give the ambient point set a strict `x`-order.  Every ordinary face of
rank at least two has a unique ordered pair `(min U,max U)`.  Therefore

\[
       \mathcal B_e\cap\mathcal B_f=\varnothing\quad(e\ne f),
       \qquad \sum_e|\mathcal B_e|\le V(P).                \tag{6}
\]

Let `Omega` be a raw multiset of histories.  It is partitioned into cells
`Omega_(e,a)`, where `e` is the endpoint state and `a` is any remaining
rank/depth state.  Assume at most `J` values of `a` occur over one `e`.
Previously fixed data such as `W`, `(p,F,tau)`, or a circuit role are held
fixed outside this notation and do not contribute to `J`.  Put

\[
              N_{e,a}=|\Omega_{e,a}|,
              C_e=|\mathcal B_e|.                         \tag{7}
\]

> **Theorem 1 (raw endpoint Hall dichotomy).**  For every `rho>0`, let
> `L` be the union of cells satisfying `N_(e,a)<=rho C_e` and let `H` be
> the remaining histories.  Then
> 
> \[
>                       |L|\le\rho J V(P).                 \tag{8}
> \]
> 
> Moreover the complete bipartite bank from one low cell to `\mathcal B_e`
> routes its histories with congestion at most `ceil(rho)`.  Superposing
> all low cells gives congestion at most `J ceil(rho)`.  If `H` is
> nonempty, its endpoint banks have union `\mathcal B_(E_H)` and
> 
> \[
>                |H|>\rho|\mathcal B_{E_H}|,               \tag{9}
> \]
> 
> so `H` is already a literal raw Hall-dense family.

**Proof.**  For a fixed endpoint, at most `J` low cells each contain at
most `rho C_e` histories.  Sum this and use (6), proving (8).  A complete
bipartite graph with `N_(e,a)` left vertices and `C_e` right vertices has
an equitable assignment of load `ceil(N_(e,a)/C_e)<=ceil(rho)`; summing
over at most `J` states proves the routing claim.  Finally, if `E_H` is the
set of endpoints supporting high cells, then

\[
 |H|=\sum_{e,a:\,\mathrm{high}}N_{e,a}
   >\rho\sum_{e,a:\,\mathrm{high}}C_e
   \ge\rho\sum_{e\in E_H}C_e,                              \tag{10}
\]

which is (9) because the endpoint banks are disjoint.  QED.

At the low-rank cutoff `R=O(log n)`, taking `a=(j,k)` costs at most
`J=O(R^2)=n^o(1)`.  With

\[
                         \rho={D_0^{1-\epsilon}\over J},    \tag{11}
\]

the low part is bounded by `D_0^(1-epsilon)V(P)`, while the high part has
raw Hall density `D_0^(1-epsilon-o(1))`.  No comparison between a
half-Gibbs likelihood ratio and a raw count has been made.

The interface qualification is exact.  Theorem 1 is available for global
EIC because every member of `\mathcal B_e` is an actual ordinary face and
the endpoint is decoded from it.  It is unavailable if a narrower local
lemma insists that the output contain a fixed `W` or a fixed repair mark.

## 2. What weighted localization does and does not imply

For a fixed history rank `k=r+2j`, the genuine history weight from the
radial bridge is

\[
                         w_{U,j}={2^{-k}\over G_e}.         \tag{12}
\]

Since the endpoint pair itself contributes `1/4` to `G_e`,

\[
                         w_{U,j}\le2^{2-k}.                \tag{13}
\]

Thus a fixed-rank fibre of total likelihood weight `H` contains at least

\[
                              H2^{k-2}                     \tag{14}
\]

raw histories.  This only forces a high cell in Theorem 1 under the honest
relative hypothesis

\[
                         H2^{k-2}>\rho J V(P).              \tag{15}
\]

An absolute bound `H>=D_0^c` is not enough when `V(P)` is unrestricted.

Rank resolution gives the sharper local audit.  If `C_(e,s)` is the
number of rank-`s` baseline faces and `b=s-k>0`, then

\[
 G_e\ge C_{e,s}2^{-s},\qquad
 {N_{j,e,k}\over C_{e,s}}
       ={H_{j,e,k}G_e2^k\over C_{e,s}}
       \ge {H_{j,e,k}\over2^b}.                            \tag{16}
\]

Consequently `H_(j,e,k)>rho 2^b` forces literal raw density `rho`, but a
tilt of size only `2^b` may correspond to raw density one.  This is the
precise sense in which weighted localization alone does not close the raw
gate.  Theorem 1 instead says: if that raw family is light, charge it; if
it is not light, retain it as a raw Hall atom.

## 3. Exact endpoint-guarded shadow routing

Fix a guard `G` of rank `g`, containing the two endpoints, and integers
`g<=k<s`.  Let `\mathcal U` be a family of distinct ordinary rank-`s`
faces containing `G`.  Define

\[
 \partial^G_k(U)=\{T\subseteq U:|T|=k,\ G\subseteq T\},
 \qquad d(T)=|\{U\in\mathcal U:T\subseteq U\}|,
 \qquad\Delta=\max_Td(T).                                 \tag{17}
\]

Every output is ordinary by heredity.  When `G` is just the endpoint pair,
the output has the same minimum and maximum, so the guard and endpoint
cell are decoded by the output itself.

> **Theorem 2 (beta-clone guarded-shadow routing).**  Put `R` and `beta`
> as in (3).  There is a map from `beta` labelled clones of every
> `U in \mathcal U` to its guarded rank-`k` downfaces such that every output
> receives at most
> 
> \[
>                         K=\left\lceil{\beta\Delta\over R}\right\rceil
>                                                                  \tag{18}
> \]
> 
> clones.  In particular, for a proposed subpower congestion `L`, either
> `K<=L+1`, or one actual guarded prefix `T` lies in more than
> 
> \[
>                              {RL\over\beta}               \tag{19}
> \]
> 
> baseline faces.

**Proof.**  In the incidence graph from `\mathcal U` to its shadows, every
left degree is `R` and every right degree is at most `Delta`.  Hence for
every left subfamily `A`,

\[
                       R|A|\le\Delta|N(A)|.                \tag{20}
\]

Replace every left vertex by `beta` clones and every right vertex by `K`
copies.  A set of clones is supported on at most the corresponding set of
original left vertices, so (20) and `K>=beta Delta/R` give Hall's
condition.  A matching proves (18).  If (19) fails, then
`Delta<=RL/beta`, so (18) gives `K<=L`.  QED.

The local feasibility factor is explicit:

\[
 {R\over\beta}={\binom{k+b-g}{b}\over2^b}.                \tag{21}
\]

If `k-g>=b`, every factor in

\[
 \binom{k+b-g}{b}=\prod_{i=1}^b\left(1+{k-g\over i}\right) \tag{22}
\]

is at least two, so `R>=beta`.  At the other extreme, if `k=g`, then
`R=1` while `beta=2^b`; exact rank-`k` guarded downfaces cannot even give
`beta` distinct local symbols.  Any theorem which omits the factor (21)
is false before planarity is used.

Across varying endpoints, the outputs are disjoint because they recover
their minimum and maximum.  Across varying `(j,s)` one may sum the
congestions, losing only the number of rank/depth states.  A fixed `W` or
fixed circuit mark can be included in `G` only when it is actually a
subset of every baseline face.  A merely compatible or external `W`
cannot be adjoined for free.

## 4. The heavy prefix has a Boolean bank and a circuit split

Fix a prefix `T` witnessing `d(T)=M`.  Every containing face has a unique
form

\[
                         U_D=T\mathbin{\dot\cup}D,
                         |D|=b.                            \tag{23}
\]

Distinct baseline faces give distinct petals `D`.  If baseline
occurrences have multiplicity at most `mu`, the fibre still contains at
least `M/mu` distinct petals; below we state the distinct-face form.

> **Theorem 3 (fixed-prefix Boolean completion bank).**  For every
> `D` in the fibre and every `A subseteq T-G`,
> 
> \[
>                           G\cup A\cup D                   \tag{24}
> \]
> 
> is an ordinary face.  These faces are all distinct as `(A,D)` varies.
> Hence the bank has exactly
> 
> \[
>                             M2^{k-g}                      \tag{25}
> \]
> 
> members.  The unguarded form has `M2^k` members.

**Proof.**  The output (24) is a subset of the ordinary carrier `T union D`.
Because `T` is fixed, intersecting the output with `T-G` recovers `A`, and
subtracting `T` recovers `D`.  QED.

Thus a heavy prefix is not an empty collision.  If `k-g>=b`, (25) gives
at least `M beta` ordinary faces while retaining all guards.  If a common
interval face `W` is contained in `T`, including it in `G` retains it at
the exact cost `2^|W-G_old|`; similarly for fixed circuit marks.  If `W`
is not contained in the carriers, no such conclusion is valid.

There is also an exact first-divergence alternative.  Call a pair
`D,D'` compatible if `T union D union D'` is ordinary, and let `E_+` and
`E_-` be the numbers of compatible and incompatible unordered pairs.

> **Theorem 4 (mixed bank or cross-petal circuit).**  The compatible pairs
> produce at least
> 
> \[
>                  {2^{k-g}E_+\over3^{2b}}                 \tag{26}
> \]
> 
> distinct ordinary faces retaining `G`.  Every incompatible pair has a
> four-point circuit in `T union D union D'` which meets both
> `D-D'` and `D'-D`.  Moreover the incompatible-pair graph contains either
> a star or a matching of size at least `sqrt(E_-/2)`.

**Proof.**  A compatible pair supplies `G union A union D union D'` for
every `A subseteq T-G`.  For a fixed outside union `L=D union D'`, at most
`3^|L|<=3^(2b)` ordered membership patterns `(D,D')` have union `L`.
Different `(A,L)` give different faces, proving (26).

For a bad pair, planar Caratheodory gives a bad four-circuit in the union.
It cannot be contained in either individually ordinary carrier
`T union D` or `T union D'`; therefore it meets both exclusive petal
differences.  Finally, if maximum bad degree is at least `sqrt(E_-/2)`,
there is the claimed star.  Otherwise a greedy matching has size at least
`E_-/(2 Delta_bad)>sqrt(E_-/2)`.  QED.

Theorem 4 is a rigorous localization, not a claim that an arbitrary
cross-petal circuit family already has a globally reusable shield.  In the
mismatch-poor regime, discharging this circuit graph still needs the
established outer/one-gap/anchor banks or a new petal-shield theorem.

## 5. Sharp convex regression

Let `P={z_0,...,z_(m-1)}` be in strict convex position and increasing
`x`-order, fix `e={z_0,z_(m-1)}`, and take every rank-`s` face containing
`e`.  Then

\[
 |\mathcal U|=\binom{m-2}{s-2},\qquad
 |\partial^e_k\mathcal U|=\binom{m-2}{k-2},               \tag{27}
\]

and every output has degree

\[
                         \Delta=\binom{m-k}{s-k}.          \tag{28}
\]

The incidence identity

\[
 \binom{m-2}{s-2}\binom{s-2}{k-2}
 =\binom{m-2}{k-2}\binom{m-k}{s-k}                        \tag{29}
\]

shows that the average, hence minimum possible, congestion for `beta`
clones is exactly `beta Delta/R`; Theorem 2 attains its ceiling.

Take `k=4`, `b=s-k=c log D_0`, and `m` polynomial in `D_0`.  Then
`R=binom(b+2,2)` is only polynomial in `log D_0`, while
`beta=D_0^c` and `Delta=binom(m-4,b)`.  The guarded-shadow congestion is
far from subpower.  Thus bounded ranks and planarity alone do not control
the rank-transfer overlap.

This regression honestly pays: `P` itself is convex and contributes
`2^m` ordinary faces.  More locally, after fixing a prefix `T`, the petal
support is still a convex cloud.  Therefore it is a sharp kill of a
rank-only guarded-shadow assertion, not a counterexample to the desired
global EIC or to a rectangle-or-shield dichotomy.

## 6. What is closed and what remains

1. **Global raw EIC payment.**  If arbitrary endpoint faces are allowed,
   Theorem 1 gives an exact paid-or-raw-dense split with subpower state
   loss.  Rank mismatch is not an obstruction in this interface.
2. **Mark-retaining local transfer.**  Theorem 2 is the sharp Hall theorem.
   Its only obstruction is a heavy actual guarded prefix.
3. **Heavy prefix.**  Theorem 3 gives its exact Boolean capacity.  This
   closes the balanced range `k-g>=s-k`.
4. **Mismatch-poor residual.**  Compatible petals pay by Theorem 4;
   incompatible petals localize to a cross-petal four-circuit graph.  The
   complete convex regression proves that a petal-support shield, rather
   than a rank-only overlap estimate, is indispensable.
5. **Weighted-to-raw caution.**  An absolute Jensen/localization load does
   not by itself imply the relative hypothesis (15).  It either must be
   combined with a raw counterfamily of size `>rho J V`, or remain in the
   already closed weighted EIC branch.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_rank_mismatch_guarded_shadow.py
```

The checker verifies the endpoint partition and low/high inequalities,
constructs the beta-clone Hall flow and proves the stated congestion is
sharp on a complete convex layer, enumerates the fixed-prefix Boolean
bank, checks the mixed-union multiplicity bound, and verifies an exact
rational insertion-chain example whose bad union has a cross-petal
four-circuit.
