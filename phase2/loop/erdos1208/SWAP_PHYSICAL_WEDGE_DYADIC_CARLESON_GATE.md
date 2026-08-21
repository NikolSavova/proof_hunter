# Physical-wedge dyadic Carleson gate

## 1. Purpose

The repeated mixed same-centre term is already a sum of triangle loads of
four-line completion blocks.  This note adds the physical endpoint that was
implicit in that formulation and separates, with no loss, the part paid by
the `k^3` allowance from the part that must use height.

The result is a sharper restart for the direct `1/3` attack.  It is not a
proof of Erdős 1208: one endpoint-sensitive high-wedge estimate remains.

Throughout, `A` is a `k`-point distance-Sidon set.  The notation for the
same-centre fibres and their cross-translate cells is that of
`SWAP_MIXED_SAME_CENTRE_TRIPLE_INTERSECTION_GATE.md` and
`SWAP_COMPLETION_DIAGONAL_FOUR_LINE_GATE.md`.

## 2. The physical-wedge partition

Every mixed `V`--`W` pair used in the same-centre sum has a unique common
physical endpoint `x`.  Retain

1. `x`;
2. the incident directed `V`-edge label;
3. the incident directed `W`-edge label; and
4. the two endpoint roles, one in `{0,1}` and one in `{2,3}`.

Call this five-tuple an oriented physical wedge `w`.  For each translate
cell `S` over `w`, put `r(S)=|S|` and define

\[
 M(w)=3\sum_{S\mapsto w}{r(S)\choose3},\qquad
 Q(w)=\sum_{S\mapsto w}{r(S)\choose2}.             \tag{2.1}
\]

The assignment is lossless:

\[
 \boxed{\displaystyle
 C_{\rm center}=\sum_w M(w).}                      \tag{2.2}
\]

For fixed `x` and fixed endpoint roles, each other endpoint determines the
directed incident edge uniquely.  Hence

\[
 \#\{w\}\le 4k(k-1)^2.                             \tag{2.3}
\]

The same-edge subfamily has at most `4k(k-1)` wedges; the genuine
one-common-endpoint subfamily has at most `4k(k-1)(k-2)`.

## 3. Exact two-threshold decomposition

Fix a wedge threshold `P>=0` and an integer cell threshold `R>=3`.  Put

\[
 M_R(w)=\sum_{\substack{S\mapsto w\\r(S)\ge R}}
 3{r(S)\choose3},
 \qquad
 H_{P,R}=\sum_{w:M_R(w)>P}M_R(w).                 \tag{3.1}
\]

Since

\[
 3{r\choose3}=(r-2){r\choose2},                    \tag{3.2}
\]

every cell with `r<R` has third mass at most
`(R-3) binom(r,2)`.  Moreover, every wedge with `M_R(w)>0` contains a
cell of load at least `R`, so it consumes at least `binom(R,2)` units of
`Q_phys`.  Splitting first by cell load and then by the *rich-cell mass* of
its wedge gives

\[
 \boxed{\displaystyle
 C_{\rm center}
 \le \left(R-3+{P\over {R\choose2}}\right)
       Q_{\rm phys}+H_{P,R}.}                       \tag{3.3}
\]

where `Q_phys=sum_w Q(w)` is precisely the same-centre part of the existing
second-generation parallel pencil, and in particular is bounded by the
full `W_parallel` reservoir.  This removes the ambient wedge-count loss
altogether and is stronger than thresholding the total `M(w)`: already-paid
low-load cells cannot falsely promote a wedge into `H_{P,R}`.

Independently, if `low` means the older total-mass condition `M(w)<=P`,
there are classwise bounds

\[
 C_{\rm same\ edge}^{\rm low}\le4Pk(k-1),\qquad
 C_{\rm one\ endpoint}^{\rm low}\le4Pk(k-1)(k-2). \tag{3.4}
\]

The classwise form is retained because its different `k^2`/`k^3`
capacities may still help in a refined argument.  But for
`P,R=N^{o(1)}`, (3.3) already pays *all* non-heavy mass directly by
`N^{o(1)}W_parallel`.  Only `H_{P,R}` remains.

## 4. The direct high-wedge theorem

The clean theorem to attack is

\[
 \boxed{\displaystyle
 H_{P,R}\le N^{o(1)}m^2}                            \tag{4.1}
\]

for some subpolynomial thresholds `P,R`.  Thus every surviving wedge carries
more than `P` mass *from cells of load at least `R`*.  The statement is
substantially narrower than a pointwise bound on every wedge or every
four-line cell.  It allows the lifted modular-parabola equality model to
spend the entire ambient `m^2` allowance.

Each cell in (4.1) is simultaneously:

- a four-line intersection in the diagonal completion reservoir;
- a clique of synchronized two-completion squares;
- a set whose translates `-S` and `JS` lie in the directed-difference set;
  and
- a block with perpendicular footprint `JS-S`.

The existing footprint dichotomy says that such a cell either has large
metric support, or it contains many differences popular in both directions
`u` and `Ju`.  Consequently a proof of (4.1) must do one of two genuinely
endpoint-sensitive things:

1. Carleson-pack the large footprints into determinant/height cells; or
2. turn perpendicular popularity into a reusable completion core and run a
   density increment with a decreasing endpoint resource.

Ambient representation depth alone cannot prove (4.1): the separated
parabola model in the same-centre note has a factor-`|S|` pointwise depth
loss.  The common physical endpoint and the four completion lines are
load-bearing.

## 5. Finite stress

The augmented optimal-core analyzer gives:

\[
\begin{array}{c|r|r|r|r|r}
\text{family}&C_{\rm center}&\#w&\max M(w)&
 C_{\rm same\ edge}&C_{\rm one\ endpoint}\\ \hline
\text{Costas }23&204&68&3&24&180\\
\text{Costas }29&4857&945&48&774&4083\\
\text{Costas }31&5058&418&123&1992&3066
\end{array}
\]

At `p=31`, the top same-edge wedge has mass `123`, and the top genuine
one-endpoint wedge has mass `108`.  In both cases a single load-six cell
contributes `60`; the remaining mass comes from only a handful of load-three
and load-four cells.  This supports the two-threshold formulation: high
wedge mass is already concentrated into genuinely rich four-line cells.

The same two wedges have resonant/transverse splits `93+30` and `87+21`.
The resonant branch is therefore a worthwhile first subproblem, but it does
not exhaust the obstruction.

There is one further lossless inverse audit.  For an unordered parameter
triple `T`, let `mu(w,T)` be the number of four-line cells over `w` which
contain `T`.  Then

\[
 \boxed{\displaystyle
 C_{\rm center}=3\sum_{w,T}\mu(w,T).}             \tag{5.1}
\]

The tempting claim `mu<=1` is false.  Exact profiles are

\[
\begin{array}{c|r|r|r|r}
\text{family}&\#\{(w,T):\mu>0\}&\max_w\#\{T:\mu(w,T)>0\}
 &\max\mu&
 \sum_{w,T}{\mu\choose2}\\ \hline
\text{Costas }23&68&1&1&0\\
\text{Costas }29&1583&15&2&36\\
\text{Costas }31&1386&32&4&366\\
\text{Costas }37&1604&15&2&28
\end{array}
\]

At the multiplicity-four rows the owners form small two-by-two translation
rectangles: two centre choices combine with two cross shifts.  Thus a
physical wedge plus three parameters does not determine the cell.  Any
inverse theorem must either retain one completion corner or control these
translation rectangles in aggregate; literal triple rigidity is closed as
a shortcut.

The replacement is an exact support--collision fork.  Put

\[
 I=\sum_{w,T}\mu(w,T)={C_{\rm center}\over3},\qquad
 X=|\{(w,T):\mu(w,T)>0\}|,
 \qquad Q=\sum_{w,T}{\mu(w,T)\choose2}.           \tag{5.2}
\]

Cauchy gives

\[
 \boxed{I^2\le X(I+2Q).}                          \tag{5.3}
\]

Put `B_0=k^3+m^2`.  The two aggregate estimates

\[
 \boxed{X\le N^{o(1)}B_0,\qquad Q\le N^{o(1)}B_0} \tag{5.4}
\]

are jointly sufficient for the same-centre term.  Indeed, with one common
subpolynomial factor `L`, (5.3) gives

\[
 I\le {LB_0+\sqrt{L^2B_0^2+8L^2B_0^2}\over2}
   =2LB_0,qquad C_{\rm center}=3I\le6LB_0.       \tag{5.5}
\]

These are the **twin physical-wedge Carleson gates**.  The first is an
occupied-support packing theorem; the second is an owner-reuse theorem.
The finite maximum number of supported triples over one wedge is already
`32`, so the support gate cannot be replaced by a constant pointwise
fibre bound.

The support gate has a further exact normalization.  Choose one owner of
an occupied key `(w,T)`, and let `G_0(q),...,G_5(q)` be its six actual
`D`-valued tracks.  If the two directed physical edges of `w` are `V,W`,
put

\[
 R=JV+W.                                           \tag{5.5a}
\]

As `q` runs through `T`, the tracks `G_0,G_3` are translates of `-T`,
whereas `G_1,G_2,G_4,G_5` are translates of `JT`.  Moreover, for every
`q` they obey

\[
\begin{aligned}
 JG_0+G_1-LG_4+LG_5&=R,\\
 JG_0+G_2+G_3-LG_4+G_5&=(I-J)R.
\end{aligned}                                      \tag{5.5b}
\]

Thus `X` is not an arbitrary wedge--triple incidence count.  Every key
contains two synchronized copies of its parameter triangle in one
orientation, four in the quarter-turned orientation, and a common
two-dimensional invariant `R` determined by its physical wedge.  If
`W_R` is the number of physical wedges with invariant `R`, then

\[
 \sum_R W_R\le4k(k-1)^2.                          \tag{5.5c}
\]

After fixing the two endpoint roles, the corresponding three physical
points `(P,U,Z)` satisfy

\[
 \epsilon_1 JU+\epsilon_2 Z
 - (\epsilon_1J+\epsilon_2I)P=R,
 \qquad \epsilon_1,\epsilon_2\in\{-1,1\}.        \tag{5.5d}
\]

The `R` fibre is not pointwise bounded.  For every `n`, fix a nonzero
integer vector `R` and choose independent formal points `P_i,U_i`.  Set

\[
 Z_i=P_i-J(U_i-P_i)+R,qquad 1\le i\le n.          \tag{5.5e}
\]

Then the `n` wedges `(P_i,U_i,Z_i)` all have the same invariant `R`.
For nonzero `R`, the squared-distance polynomials of the `3n` formal
points are pairwise different.  This reduces to a finite four-block
coefficient audit, since two candidate edges involve at most four block
indices.  There are `O(n^4)` bad equal-distance polynomials, each nonzero
of degree at most two.  Schwartz--Zippel specialization in a box of side
`O(n^4)` therefore gives integral distance-Sidon examples of polynomial
height with

\[
 \max_R W_R\ge n=k/3.                             \tag{5.5f}
\]

So even the physical half of the invariant must be summed globally.  In
the finite Costas stresses the exact profiles are

\[
\begin{array}{c|r|r|r|r|r|r|r|r|r}
\text{family}&\#R&\max W_R&\max X_R&\max\nu&Q_{\rm inv}
 &X_{\nu=1}&X_{\mu=\nu=1}&X_{\rm col}&X_{\rm nc}\\ \hline
29&816&4&23&3&143&1321&1295&115&1180\\
31&332&4&68&2&254&878&770&60&710\\
37&960&4&30&2&152&1300&1280&120&1160
\end{array}                                        \tag{5.5g}
\]

where `X_R` is the number of occupied `(w,T)` keys in the fibre.  The small
observed value `4` is therefore not a viable theorem; the invariant is a
Carleson summation coordinate, not a rigidity key.  Moreover the singleton
mass `X_{nu=1}` is respectively `83.4%`, `63.3%`, and `81.0%` of `X`.
The matching-like terminal branch is therefore the dominant finite core,
not a lower-order cleanup.  After imposing both uniqueness conditions,
the noncollinear fractions are `91.1%`, `92.2%`, and `90.6%`.  Directional
line energy can at best pay a small subsidiary branch; the principal height
theorem must use the full two-dimensional parameter triangle.

There is nevertheless an exact reuse switch inside each `R` fibre.  Let

\[
 \nu(R,T)=\#\{w:(w,T)\text{ is occupied and }JV(w)+W(w)=R\},
 \qquad
 Q_{\rm inv}=\sum_{R,T}{\nu(R,T)\choose2}.        \tag{5.5h}
\]

Then the nonsingleton part of the support satisfies

\[
 \sum_{R,T:\nu(R,T)\ge2}\nu(R,T)\le2Q_{\rm inv}.\tag{5.5i}
\]

More importantly, take two wedges in the same `(R,T)` fibre and choose
one owner for each.  Write their owner variables as `(V,W,a,b,e)`, so
`W_beta-W_alpha=-J(V_beta-V_alpha)`.  Put

\[
 U=V_\beta-V_\alpha,\quad A=a_\beta-a_\alpha,\quad
 B=b_\beta-b_\alpha,\quad E=e_\beta-e_\alpha.
\]

The six track differences are

\[
\begin{aligned}
d_0&=U-A,&d_1&=-JU-LB+JA,&d_2&=-JU-LB+LA,\\
d_3&=U-A+E,&d_4&=-JU-B-JE,&d_5&=-JU-JE.
\end{aligned}                                      \tag{5.5j}
\]

Every `q in T` gives one labelled representation of every `d_j` in
`D-D`.  The six forms in `(U,A,B,E)` are exactly the forms in (5.9) after
the substitution `q=-U`.  Consequently the same thirteen invertible
four-track projections and the same fractional cover apply.  Reused
parameter triangles therefore create the same six-direction recursive
core as repeated owners; a full bipartite rectangle is not needed.

Hence, after paying the two collision quantities `Q` and `Q_inv`, the truly
new support theorem may assume simultaneously

\[
 \boxed{\mu(w,T)=1\quad\text{and}\quad\nu(R,T)=1.} \tag{5.5k}
\]

This is the terminal matching-like height branch: each surviving parameter
triangle has one physical wedge in its invariant fibre and that key has one
owner.  Any proof using a second completion before reaching this branch is
spending structure already available to the six-direction recursion.

This is the concrete input for attacking the first twin gate: a physical
three-point equation correlated with a synchronized six-copy triangle in
`D`.  Dropping either the physical equation or the synchronization returns
to ambient centroid/quarter-turn energies already known to be too large.

Thus excessive mass either exposes many distinct physical-wedge/parameter-
triple keys, or creates many pairs of owner cells sharing one such key.
The latter pairs have a rigid six-direction normal form.

Write one owner cell as `(c,ell,a,b,eta)`, where `a,b` are its first and
second fibre displacements and the second-fibre parameter paired with `q`
is `q-eta`.  Its fixed physical wedge contains

\[
 V=c+a,\qquad W=\ell+Lb.                           \tag{5.6}
\]

Suppose owners `alpha,beta` have the same `V,W` and contain the same
parameter set `T`.  Put

\[
 A=c_\beta-c_\alpha,qquad
 B=b_\beta-b_\alpha,qquad
 E=\eta_\beta-\eta_\alpha.                        \tag{5.7}
\]

Since the wedge is fixed,
`a_beta-a_alpha=-A` and
`ell_beta-ell_alpha=-LB`.  Comparing the three `D` tracks of the first
fibre and the three tracks of the second fibre gives

\[
 \boxed{
 A,\quad -LB-JA,\quad -L(A+B),\quad
 A+E,\quad -B-JE,\quad -JE\in D-D,}               \tag{5.8}
\]

 each with at least `|T|` labelled representations.  More precisely, for
every `q in T` the six representing pairs are the corresponding owner
tracks at `q`; no averaging is used.  Formula (5.8) explains the observed
two-by-two rectangles: `A` changes the centre owner while `E` changes the
cross shift.

There is also a sharp fixed-offset counting theorem.  Once the physical
wedge `(V,W)` is fixed, one owner and one common parameter `q` are determined
by four vector variables `(a,b,e,q)`, where `e=eta`.  After deleting the
fixed translations `V,W`, its six `D` tracks are

\[
\begin{aligned}
 F_0&=-a-q, & F_1&=-Lb+Jq+Ja, & F_2&=-Lb+Jq+La,\\
 F_3&=-a-q+e, & F_4&=-b+Jq-Je, & F_5&=Jq-Je.
\end{aligned}                                      \tag{5.9}
\]

For the second owner, these become `F_j+d_j`, where `(d_0,...,d_5)` is
the list in (5.8).  Of the fifteen four-subsets of the six forms, exactly
thirteen give invertible maps from `(a,b,e,q)` over the rationals.  The two
exceptions are

\[
 \{0,1,4,5\},\qquad \{1,2,3,5\}.                \tag{5.10}
\]

Let `G_w(A,B,E)` count ordered owner-pair/common-parameter witnesses at
these fixed offsets.  Projection to any valid four-form basis is injective,
so

\[
 G_w(A,B,E)\le\min_{\mathcal B\ {\mathrm{valid}}}
       \prod_{j\in\mathcal B}R_D(d_j).           \tag{5.11}
\]

Give weight `1/10` to

\[
 0125,\quad0135,\quad1245,\quad1345
\]

and weight `1/15` to the other nine valid bases.  The weights sum to one
and every form has total incident weight `2/3`.  Taking the weighted
geometric mean in (5.11) proves

\[
 \boxed{\displaystyle
 G_w(A,B,E)^3\le\prod_{j=0}^5R_D(d_j)^2.}         \tag{5.12}
\]

This controls the first moment of every owner intersection.  If two owners
have common-parameter load `h<H`, then

\[
 {h\choose3}\le{(H-1)(H-2)\over6}\,h.           \tag{5.13}
\]

Hence the low-`h` owner-collision branch is reduced, without a size bias, to
the explicit aggregate sum of the right side of (5.12) over the retained
physical wedges and offsets.  That six-overlap aggregate is not yet bounded
at target scale.  The other exact survivor consists of owner pairs sharing
at least `H` parameters; those pairs expose all six directions with at least
`H` representations.

The finite owner-collision population is entirely resonant.  Number the six
directions in (5.8) from zero to five and record the indices at which they
vanish.  The exact witness-mass profiles are

\[
\begin{array}{c|l}
\text{family}&\text{zero-mask masses}\\ \hline
\text{Costas }29&(012):28,\ (035):4,\ (25):4\\
\text{Costas }31&(0):14,\ (012):258,\ (035):20,\ (2):12,\
 (23):10,\ (24):4,\ (25):18,\ (4):2,\ (45):28\\
\text{Costas }37&(012):24,\ (035):2,\ (25):2.
\end{array}                                       \tag{5.14}
\]

In particular the fully transverse mask is absent.  The dominant `(012)`
case has `A=B=0` and varies only the cross shift `E`; `(035)` has `A=E=0`;
and `(25)` has `E=0,A+B=0`.  These are literal owner-rectangle axes, not
small numerical determinants.  They should be routed to the decorated
resonant completion graphs before applying (5.12).  A future proof must
still allow a fully transverse owner collision: (5.14) is finite evidence,
not a universal zero-direction theorem.

Consequently the remaining high-wedge proof has a sharp second fork:

1. charge the distinct `(w,T)` support in (5.3) to height; or
2. use the six represented directions (5.8) to build a recursive rich
   completion core.

This is stronger than merely recording owner codegree.  All six directions,
the common physical wedge, and the common parameter triple survive the
switch.

Three major barrier families are benign for this particular term.  Dense
one-dimensional Golomb rulers through `k=14`, the explicit lifted residue
parabolas through prime `43`, and the genuine `k=48`, codegree-`49`
rank-flat certificate all have `C_center=0` (some can have cross-cell load
one, but never load three).  Thus the four-line high-wedge gate is not
merely a restatement of the collinear-core, modular-parabola, or collective
high-codegree obstruction.  This is finite evidence, not an asymptotic
theorem, but it is an important kill-search result for choosing the next
lemma.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_physical_wedge_dyadic_carleson.py
```

The verifier exhausts the oriented-wedge counts, checks the lossless mass
partition and (3.3)--(3.4) on random cell systems, checks the stored Costas
stress and triple-owner rows, and reruns small genuine Golomb and
lifted-parabola controls.  It also checks the six owner-switch directions
(5.8), the complete four-form rank audit, the fractional weights in (5.12),
finite overlap-count instances, and the stored zero-mask profiles directly
from the track definitions.
It also reruns the rank-flat `k=48` certificate.  The main analyzer
independently asserts physical-wedge mass conservation whenever actual
endpoints are available.
