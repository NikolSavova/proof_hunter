# Endpoint-baseline scarcity: common-parent Boolean payment and the product barrier

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

A small same-rank endpoint bank is favorable, not an obstruction.  Fix a
raw cell `(j,e,r)`, let `N_(j,e,r)` be its selected canonical histories,
and let `C_(e,r)` be the number of all rank-`r` parent faces with endpoint
pair `e`.  Some actual parent `T` supports at least `N/C` histories.  If a
source is

\[
                         U=Q\mathbin{\dot\cup}T,
                         |Q|=2j,                          \tag{1}
\]

then every `Q union S`, `S subseteq T`, is ordinary.  Distinct sources have
distinct `Q`, so one parent gives the exact bank

\[
                         2^r{N\over C}.                   \tag{2}
\]

If the output is required to retain the parent endpoint pair, use
`e subseteq S`; the bank has `2^(r-2)N/C` faces, and canonical depth-`j`
peeling of the output recovers `e`.  Consequently scarce cells sum
globally with only rank/depth congestion:

\[
 \boxed{
   \sum_{j,e,r}2^{r-2}{N_{j,e,r}\over C_{e,r}}
       \le \mu JR\,V(P).}                                \tag{3}
\]

Here `mu` is the maximum upstream multiplicity of one geometric canonical
history, `J` is the number of depths, and `R` the number of parent ranks.
In particular, cells with `r>=r_0` and `C_(e,r)<=C_0` contain at most

\[
                      \mu JR C_0,2^{2-r_0}V(P)           \tag{4}
\]

raw histories.  The case `C=1` is the strongest instance of this payment.

Combining (2) with the exact same-rank identity from
`RAW_RANK_MATCHED_ENDPOINT_DICHOTOMY.md` gives, for one endpoint cell,

\[
 4^jh_{j,e}\le\mu V(P)
       \mathbb E_{p(\cdot\mid e)}2^{-r}\le {\mu V(P)\over4}.       \tag{5}
\]

Equivalently some contributing rank, of source rank `k=r+2j`, satisfies

\[
                              V(P)\ge {2^k h_{j,e}\over\mu}.       \tag{6}

\]

Thus endpoint-baseline scarcity cannot kill fixed-power multiplication at
one cell.  It does not, by itself, improve the leading coefficient of
`log V`: `k=O(log n)` contributes only `O(log n)` bits.

There is a scalable planar regression with all of the following at once:

* `C_(e,r)=n^{O(1)}` (and it can be `1` if the interval cage is omitted);
* `2^{Theta((log n)^2)}` distinct actual canonical sources over one parent;
* one fixed common interval face `W` with `W union e` nonconvex;
* one fixed insertion mark and tangent cell; and
* projectively arbitrary outer clusters.

It is not a counterexample.  The outer histories form a recoverable radial
product, so the detached one-gap profile theorem supplies a quadratic
extra bank.  Under a full `q=Theta(log n)` product extraction, this already
improves coefficient `1/4` to at least `3/8-o(1)` using the conservative
`1/8` local reservoir coefficient.  The exact remaining issue is therefore
not parent scarcity; it is extracting a recoverable positive-log-scale
outer product/module system from an arbitrary high-density cell.

## 1. One common parent has an exact Boolean source bank

Let `P` be strictly ordered by `x`.  A canonical depth-`j` history is an
ordinary source face

\[
 U=\{u_1<\cdots<u_{r+2j}\}                               \tag{7}
\]

whose remaining parent is

\[
 T_j(U)=\{u_{j+1},\ldots,u_{j+r}\},\qquad
 e_j(U)=\{u_{j+1},u_{j+r}\}.                            \tag{8}

The peeled petal `Q=U-T_j(U)` has exactly `j` labels on each side of `e`.

Allow a selected occurrence family in which one geometric pair `(U,j)`
is represented at most `mu` times.  Put

\[
 d(T)=|\{\omega:T_j(U_\omega)=T\}|,qquad
 N=\sum_{T\in\mathcal B_{e,r}}d(T),\qquad
 C=|\mathcal B_{e,r}|.                                  \tag{9}
\]

> **Theorem 1 (scarce-parent Boolean payment).**  A parent `T` exists for
> which the selected family contains at least `N/(mu C)` distinct sources.
> The ordinary faces
> 
> \[
>      Q_U\cup S,\qquad S\subseteq T,                    \tag{10}
> \]
> 
> over those sources are all distinct, so
> 
> \[
>                         V(P)\ge {2^rN\over\mu C}.       \tag{11}
> \]
> 
> Restricting to `e subseteq S` gives `2^(r-2)N/(mu C)`
> distinct outputs which canonically recover `e` after depth-`j` peeling.

**Proof.**  Averaging gives a parent with occurrence degree at least `N/C`;
the multiplicity cap leaves at least `N/(mu C)` distinct sources.  Every
set (10) is a subset of its ordinary source `U`.  For the fixed `T`, the
output recovers `S` by intersection with `T` and recovers `Q_U` by
subtraction, so all pairs `(U,S)` are distinct.  If `S` contains both
points of `e`, then `Q_U` remains the set of the `j` leftmost and `j`
rightmost output labels.  Peeling those labels recovers `S` and hence its
extreme pair `e`.  QED.

The same proof retains any fixed guard `G subseteq T` at the exact cost
`2^|G|`, by requiring `G subseteq S`.  In particular a fixed repair mark or
circuit trace already contained in the parent is harmless.  A common
interval face `W` which is not contained in `T` cannot be adjoined to (10):
the hypothesis often says precisely that `W union e` has a bad circuit.
Equation (11) is therefore a global ordinary-face charge, not a false
coexistence assertion.

## 2. Global summation of the scarce cells

For every active cell `(j,e,r)`, choose one maximum-degree parent and form
the endpoint-retaining bank from Theorem 1.  Fix one depth `j`.  From an
output `F=Q union S`, canonical depth-`j` peeling recovers both `Q` and the
endpoint pair `e` of `S`.  Thus banks belonging to different endpoints do
not collide.  The parent rank `r` is not necessarily recovered, so there
are at most `R` representations at this fixed depth.  Summing over at most
`J` depths gives total output overlap at most `JR`.

> **Theorem 2 (global scarce-baseline inequality).**  With the notation
> above,
> 
> \[
>   \sum_{j,e,r}2^{r-2}{N_{j,e,r}\over\mu C_{e,r}}
>       \le JR,V(P).                                    \tag{12}
> \]
> 
> Therefore, for every subfamily satisfying `r>=r_0` and
> `C_(e,r)<=C_0`, equation (4) holds.

**Proof.**  Theorem 1 supplies the left side of (12) as bank incidence
mass.  The decoder just described bounds the incidence load of one actual
ordinary face by `JR`.  Double count.  On the stated subfamily,

\[
 2^{r-2}{N\over\mu C}\ge
             2^{r_0-2}{N\over\mu C_0}.                  \tag{13}
\]

Sum (13) and apply (12), proving (4).  QED.

For bounded ranks, `JR=(log n)^O(1)`.  Thus any endpoint baseline of
subquadratic entropy loses no leading `L^2` coefficient in this global
charge.  For fixed-power EIC the exact threshold is stronger: the scarce
part is paid at target `D_0^(1-epsilon)V` whenever

\[
                C_0\le {2^{r_0-2}D_0^{1-\epsilon}
                                \over\mu JR}.             \tag{14}
\]

## 3. Combination with the same-rank likelihood identity

For one endpoint and depth, put

\[
 d_r={N_{j,e,r}\over C_{e,r}}.                           \tag{15}
\]

The exact identity already proved in the common-shield report is

\[
 4^jh_{j,e}=\sum_r{p_{e,r}\over p_e}d_r.                \tag{16}
\]

Theorem 1 gives `d_r<=mu 2^(-r)V(P)` for every rank.  Substitution proves
the first inequality in (5); parent ranks are at least two, proving the
second.  Alternatively, some `r` has `d_r>=4^jh_(j,e)`, and Theorem 1 at
that rank gives

\[
 V(P)\ge {2^rd_r\over\mu}
       \ge {2^{r+2j}h_{j,e}\over\mu},                   \tag{17}
\]

which is (6).

This closes the proposed `C_(e,r)=1` failure mode exactly.  With one parent,
every bit of source multiplicity is an omitted-petal bit, and the parent's
Boolean downset multiplies it.  A large `C_(e,r)` is the branch requiring
cross-parent Hall/circuit analysis.

## 4. Coefficient audit: what (11) cannot do

Let `L=log n`, suppose a cell has

\[
 \log N=(a+o(1))L^2,quad
 \log C=(c+o(1))L^2,quad r=O(L),\quad\log\mu=o(L^2).    \tag{18}
\]

Equation (11) gives only

\[
                    \log V\ge(a-c-o(1))L^2+O(L).         \tag{19}
\]

Thus `c=0` preserves coefficient `a` but does not improve it.  In
particular a coefficient-`1/4` history family plus a parent Boolean factor
cannot alone prove `1/4+delta` for fixed `delta>0`.

This is an exact limitation of the inequality, not a planar equality
construction.  The abstract incidence model with one parent, `N=M`
distinct petals, and exactly the `M2^r` formal faces (10) attains equality
in (11).  Real planar radial products have additional one-gap faces, as the
next section shows.  Therefore no planar no-epsilon counterexample is
claimed.

## 5. Scalable planar scarcity regression

The same-rank endpoint count can genuinely be tiny while the source entropy
is quadratic.  Start with a strict concave high arc and choose a fixed
rank-`r` consecutive face

\[
                       T=\{t_0<\cdots<t_{r-1}\},
                       e=\{t_0,t_{r-1}\}.                \tag{20}
\]

Take `j` tiny outer cluster neighbourhoods strictly to the left of `e` and
`j` to the right, centered at further vertices of the same strict macro
cap.  Put `ell` points in every cluster.  The neighbourhoods may be chosen
successively small and rational so that every transversal, together with
all of `T`, is ordinary.  The source family has

\[
                         M=\ell^{2j}                      \tag{21}
\]

distinct members, every one canonically peeling at depth `j` to the same
parent `T`.

Inside the open interval of `e`, put a low strict concave arc `Z` far below
the chord of `e`.  As in the nested-cap construction, every trace compatible
with `e` contains at most two points of `Z`.  If `m=|Z|` and the only other
interior labels are the `r-2` internal points of `T`, then

\[
 C_{e,r}\le
 \sum_{a=0}^2\binom ma\binom{r-2}{r-2-a}
 =1+m(r-2)+\binom m2\binom{r-2}{2}.                    \tag{22}
\]

This is polynomial in `m,r`.  If the low cage is omitted, then literally
`C_(e,r)=1`.

Choose any fixed three-or-more point face `W subseteq Z`.  It is an actual
interval face, while `W union e` is nonconvex; a fixed bad four-circuit is
therefore shared by every history.  Choose an internal vertex `p` of `T`.
Deleting it from a source and reinserting it realizes every source as a
repaired star with the same mark `p`; choosing `p` away from the ends of
`T` fixes its two tangent neighbours and their outer neighbours.  Hence the
family also has a common marked tangent cell.  This refutes any assertion
that common `W`, a fixed circuit, and a fixed local mark force many
same-rank baseline parents.

The construction is robust under projectively universal replacements of
the outer clusters.  A sufficiently small replacement preserves every
transversal and the fixed tangent cell.  Thus no cap/cup regularity of an
individual cluster is implied.

The regression pays.  It has a recoverable cyclic/radial list of outer
clusters, so `DETACHED_RADIAL_LEXICOGRAPHIC_PROFILE.md` applies.  If `H_i`
is the nonempty face count of cluster `i`, its one-gap theorem gives an
ordinary bank at least

\[
 M\left(\prod_{i=1}^{q}{H_i\over\ell_i^3}\right)^{1/q},
 \qquad q=2j.                                            \tag{23}
\]

## 6. Conditional coefficient jump under the weakest known product gate

Equation (23) gives a complete coefficient calculation once a full radial
product has been extracted.  Suppose

\[
 q\le\kappa L,qquad M=\prod_i\ell_i\ge2^{aL^2},qquad
 \log H_i\ge(c_0-o(1))(\log\ell_i)^2,                   \tag{24}
\]

where the available conservative universal constant is `c_0=1/8`.
Writing `s_i=log ell_i`, Jensen gives

\[
 {1\over q}\sum_i\log{H_i\over\ell_i^3}
 \ge(c_0-o(1))\left({a\over\kappa}\right)^2L^2-O(L).   \tag{25}
\]

Therefore

\[
 \boxed{
 \log V(P)\ge
 \left[a+c_0(a/\kappa)^2-o(1)\right]L^2.}               \tag{26}
\]

For the balanced regression `ell_i=ell`, `q=(1/4)log ell`, and
`L=(1+o(1))log ell`, one has `a=kappa=1/4`; equation (26) yields

\[
                         \log V(P)\ge(3/8-o(1))L^2.       \tag{27}

\]

Thus the full-product scarcity regime is strictly beyond coefficient
`1/4`.  This is a conditional upper jump with an exact realizable gate.
What is not proved is that an arbitrary Hall-dense same-parent source
family contains such a recoverable positive-log-scale module product.  A
sparse anti-aligned subfamily can destroy the Cartesian product even though
all individual sources remain ordinary.

## 7. Remaining atom

The endpoint-baseline alternatives are now exact.

1. `C_(e,r)` below (14) is globally paid by the guarded common-parent bank.
2. A fixed high likelihood endpoint cell is paid by (5)--(6), independently
   of whether `C_(e,r)=1`.
3. Quadratic entropy can coexist with polynomial `C_(e,r)`, common `W`, a
   fixed bad circuit, and a fixed tangent mark.  Therefore scarcity does
   not force baseline multiplication.
4. Every recoverable full radial product pays a positive quadratic
   coefficient by (26).  The live residue is precisely the extraction of
   such modules, or a substitute circuit/anchor bank, from an arbitrary
   sparse same-parent completion family.

No coefficient closure is claimed without that extraction.

## 8. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_endpoint_baseline_scarcity.py
```

The checker verifies Theorems 1--2 on exact finite incidence systems,
checks the same-rank likelihood inequality with rational weights, and
enumerates a rational small instance of the planar regression.  In that
instance there are `81` distinct canonical sources over one rank-five
parent, a polynomial rank-five endpoint bank, an exact `2592`-face local
Boolean bank, one fixed nonconvex common interval trace, and one fixed
marked tangent cell.
