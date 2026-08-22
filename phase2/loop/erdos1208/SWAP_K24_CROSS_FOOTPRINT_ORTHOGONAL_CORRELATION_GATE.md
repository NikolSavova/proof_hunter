# Cross-footprint collisions are an exact orthogonal correlation

## 1. Outcome

The support-collision term in the natural-level K2,4 footprint gate now has
an exact weighted lift.  For two physical owners with parameter sets `S,T`
and footprint offsets `O,O'`, write

\[
 m_{O,S}(z)=|\{(f,g)\in S^2:O+Jg-f=z\}|,
 \qquad K=O-O'.
\]

If

\[
 R_{S,T}(v)=|\{(s,t)\in S\times T:s-t=v\}|,
\]

then

\[
 \boxed{
 \sum_zm_{O,S}(z)m_{O',T}(z)
 =\sum_v R_{S,T}(v)R_{S,T}(K+Jv).}               \tag{1.1}
\]

Thus a pair of colliding owner footprints is not an arbitrary additive
energy term: it correlates one cross-difference fibre with its translated
quarter-turn.  The offset `K` is the endpoint-labelled owner displacement
from the preceding normal form.

There is also a sharp limitation.  The unweighted support collision can be
large while (1.1) remains at its ordinary product baseline.  Consequently
it does **not** force two polynomially popular cross shifts.  The surviving
object is the decorated `L=1` rotated-Schur closure

\[
 u,\quad u+H,\quad -u,\quad JH-u,                \tag{1.2}
\]

unless a genuinely large weighted correlation is first established.  This
rules out one tempting but false shortcut: support collision cannot simply
be upgraded to a second rich-translation level.

## 2. Exact pair identity

An equality counted by the left side of (1.1) is

\[
 O+Jg-f=O'+Jg'-f'.                               \tag{2.1}
\]

Putting `A=f-f'` and `B=g-g'` gives

\[
 A=K+JB.                                         \tag{2.2}
\]

For fixed `B`, the choices of `(g,g')` and `(f,f')` are independent and
have respective multiplicities `R_{S,T}(B)` and
`R_{S,T}(K+JB)`.  Summing proves (1.1).

The affine map `v -> K+Jv` is a bijection of the integer lattice.  Hence
Cauchy gives the useful universal envelope

\[
 \boxed{
 E_{O,O'}(S,T)
 \le \sum_vR_{S,T}(v)^2.}                        \tag{2.3}
\]

The right side is the ordinary cross-additive energy of `S,T`.  It is only
an envelope: discarding `K`, the quarter-turn, or the two owner labels is
not justified in the final aggregate.

If `Phi_{O,S}=O+(JS-S)`, then every common support point has at least one
representation from each cell.  Therefore

\[
 \boxed{
 |\Phi_{O,S}\cap\Phi_{O',T}|\le E_{O,O'}(S,T).}  \tag{2.4}
\]

For a family of cells, put

\[
 M(z)=\sum_Cm_C(z),\qquad
 W=\sum_{C<C'}\sum_zm_C(z)m_{C'}(z).
\]

Then exactly

\[
 \boxed{
 W={1\over2}\left(\sum_zM(z)^2-
                    \sum_C\sum_zm_C(z)^2\right),
 \qquad Q\le W,}                                 \tag{2.5}
\]

where `Q=sum_z binom(d(z),2)` is the support-collision mass from the
preceding note.

## 3. Popular cross-shift fork

For an integer `L>=1`, define

\[
 \mathcal P_L(S,T;K)=
 \{v:R_{S,T}(v)\ge L,\ R_{S,T}(K+Jv)\ge L\}.
\]

Outside this set at least one factor in (1.1) is below `L`.  Splitting
according to which factor is small and using
`sum_v R_{S,T}(v)=|S||T|` gives

\[
 \boxed{
 E_{O,O'}(S,T)
 \le2L|S||T|+
 \sum_{v\in\mathcal P_L}
 R_{S,T}(v)R_{S,T}(K+Jv).}                       \tag{3.1}
\]

Since every cross-difference load is at most
`m_0=min(|S|,|T|)`, if `E>2L|S||T|` then

\[
 \boxed{
 |\mathcal P_L|
 \ge {E-2L|S||T|\over m_0^2}.}                  \tag{3.2}
\]

For the physical owners, every member of `P_L` retains both anchored owner
keys.  In the notation of the support/collision normal form it supplies
`A=K+JB`, hence `H=A-B` and the four literal `D-D` directions (1.2).
Thus (3.2), when active, is a genuine second density increment rather than
an anonymous popular-difference statement.

For a family, let `P` be the sum of `|S_C||S_C'|` over pairs with positive
cross energy, and let `J_L` be the sum of the popular terms in (3.1).  Then

\[
 \boxed{W\le2LP+J_L.}                             \tag{3.3}
\]

This is the exact aggregate fork.  It is useful only when the weighted
energy exceeds its product baseline by a real factor.

## 4. The diagonal-baseline barrier

Support collision alone cannot activate (3.2).  Let

\[
 S_r=\{(2^j,0):0\le j<r\}.
\]

The map `(f,g) -> Jg-f` is injective, so one footprint has `r^2` points and
all its representation multiplicities are one.  Give two formally
distinct cells the same set and offset.  They have

\[
 Q=r^2,\qquad W=r^2=|S_r|^2.                     \tag{4.1}
\]

The whole correlation is carried by the single cross difference `v=0`,
whose two loads are `r`.  For every `L>=1`, the hypothesis
`W>2L|S_r|^2` fails.  Hence even quadratic support overlap does not force a
population of popular nonzero cross shifts.

This is an abstract cell barrier, not a claimed physical #1208
counterexample.  Its role is precise: any proof using (1.1) must retain the
physical owner decoration to control baseline or diagonal reuse.  A generic
cross-energy theorem cannot replace the endpoint-sensitive packing lemma.

## 5. Canonical support collisions have a diffuse/dense dichotomy

Choose one representation

\[
 \rho_C(z)=(f_C(z),g_C(z))
\]

canonically for every footprint incidence.  For a collision between `C`
and `C'`, put

\[
 A=f_C-f_{C'},\qquad B=g_C-g_{C'},
 \qquad a=R_{S,T}(A),\quad b=R_{S,T}(B).          \tag{5.1}
\]

Every support collision belongs to exactly one of two classes.

* **Diffuse:** `min(a,b)=1`.  One of the two cross-parameter pairs is
  uniquely recovered from its difference and the two owner cells.
* **Dense:** `a,b>=2`.  Choose the first two representations
  `(f_1,f'_1),(f_2,f'_2)` of `A`.  Then

  \[
   \alpha=f_1-f_2=f'_1-f'_2\ne0.                 \tag{5.2}
  \]

  Doing the same for `B` gives a second nonzero common chord `beta`.
  Thus both owner parameter sets contain translated copies of each of two
  literal two-point patterns.

The dense conclusion is stronger than a high weighted energy label.  If
the original `B` pair is held fixed while the two `A` representations are
used, (2.1) produces two distinct footprint values common to the same two
cells.  Hence every dense collision lies on a cell pair with footprint
codegree at least two.  It is therefore a genuine K2,2 incidence between
two deep owners and two footprint values.

This gives an exact restart at the support level.  The diffuse population
must be charged through its uniquely oriented cross pair; the dense
population carries two common internal chords and a footprint K2,2.  No
weighted overcount is required to state either branch.

## 6. Genuine equality-model stress

The natural-core analyzer now records the exact quantities in (2.5), the
active-pair product baseline, and pairwise normalized cross energies.

* Costas 23, load three: `Q=209`, `W=304`, so `W/Q=16/11`.
* Costas 29, top load five: `Q=16`, `W=40`, so `W/Q=5/2`.
* Costas 31, top load six: `Q=82`, `W=520`, so `W/Q=260/41`.

For the last row there are six active cell pairs and
`P=6*6^2=540`, so `W<P`; even `L=1` does not enter the large-correlation
regime of (3.2).  The maximum individual normalized energy is `25/9`, and
the exact product excess is retained by the analyzer.  These data show that
the weighted lift is faithful but not, by itself, a power-saving bridge.

The canonical support dichotomy separates the two top equality models
almost perfectly.

* Costas 29, load five: all `16` collisions are diffuse; the two active
  cell pairs have the **same three owner vertices**.
* Costas 31, load six: `80/82` collisions are dense.  Of the six active
  cell pairs, two have the same three owner vertices and four have disjoint
  owner triples; the corresponding support masses are `34` and `48`.

So neither branch is a negligible exception.  The next aggregate theorem
must simultaneously pay a same-owner diffuse cross-colour correlation and
a disjoint-owner dense K2,2 population.  This is a materially sharper
target than an undifferentiated `(u,H)` collision sum.

There is one unconditional local packing gain.  Fix an **unordered** set of
three distinct owner vertices.  A resonant physical owner cell chooses one
of the three vertices as centre, an order on the other two, and one of the
three equations

\[
 e=0,\qquad e=b-a,\qquad e=L(a-b).                \tag{6.1}
\]

For fixed orientation and `e`, the centre, shifts and first K2,4 colour are
fixed.  The two physical directed edges are fixed vectors in `D`, so
distance-Sidonicity recovers their endpoint pairs and common endpoint.
Therefore

\[
 \boxed{\text{one owner triple supports at most }3\cdot2\cdot3=18
        \text{ resonant cells}.}                 \tag{6.2}
\]

In a dyadic band `R<=r_C<2R`, let `n_R` be the number of resonant cells and
let `Q_same,W_same` retain cell pairs with the identical unordered owner
triple.  A footprint has fewer than `4R^2` points.  Its representation
multiplicity is at most its cell load, so its internal energy is less than
`8R^3`; cross Cauchy gives the same bound for a pair.  Since
`binom(18,2)=153`,

\[
 \boxed{Q_{same}<612R^2n_R,
 \qquad W_{same}<1224R^3n_R.}                    \tag{6.3}
\]

Thus same-owner resonant reuse introduces no new power beyond the cell
cubic scale.  The unresolved power-saving issue is the disjoint-owner
population (plus nonresonant cells), exactly as the Costas-31 top row
indicates.

The next theorem must therefore pack the baseline `L=1` owner-labelled
closures (1.2), or prove that physical owner reuse makes their aggregate
strictly smaller than the abstract model.  This is narrower than the prior
two-branch statement: a second cross-popularity increment is now a bonus
branch, not the expected main mechanism.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_k24_cross_footprint_correlation.py
python3 phase2/loop/erdos1208/analyze_swap_optimal_nested_cores.py --k24-prime=31
```

The standalone verifier checks (1.1), (2.3)--(2.5), (3.1)--(3.3), the
sharp diagonal-baseline construction, the dense common-chord lift, and the
18-cell resonant capacity.  The analyzer independently rebuilds every
footprint representation from the literal six-track cells.
