# The fixed-row variable-longest `C_4` book gate

## 0. Status

This note records a new **sufficient** fixed-row estimate and the exact
stress tests that currently support it.  The estimate is not proved, so it
does not improve the unconditional exponent by itself.

Let `A` be a distance-Sidon set of `k` planar points, put `D=A-A`, and let
`J(a,b)=(-b,a)`.  For a fixed realized row `d in D`, write the transverse
relations as

\[
 \mathcal R_d=\{(u,v,x,y)\in A^4:
 d=(u-v)+J(x-y),\ x\ne y,\ d\mathbin\cdot(x-y)\ne0\}.
 \tag{0.1}
\]

Every two roles determine the whole relation, so each of the six projections
`uv, ux, uy, vx, vy, xy` is a simple bipartite graph with
`r(d)=|R_d|` edges.  The preceding note
`TRANSVERSE_FIXED_ROW_C4_GATE.md` shows that

\[
 C_4(G_d^{ij})\le k^{2+o(1)}
 \quad\Longrightarrow\quad r(d)\le k^{3/2+o(1)}. \tag{0.2}
\]

The present reduction isolates a still more geometric sufficient input: a
second moment for `C_4` books charged to their longest *variable* edge.

## 1. Variable-longest charge

Fix one projection `ij` and a four-cycle `C` in `G_d^{ij}`.  It consists of
four relations from (0.1).  Form the set `E(C)` of actual unordered edges of
`A` appearing as

1. the two side edges in each of the two selected projection roles; or
2. one of the distinguished edges `(u,v)` and `(x,y)` in the four
   relations.

Repeated occurrences of the same unordered edge are collapsed.  Delete from
`E(C)` the fixed unordered edge realizing `d`.  Because `A` is
distance-Sidon, the remaining distinct edges have distinct lengths.  Hence
there is a unique longest member `g(C)`.  Define

\[
 c_{d,ij}(g)=\#\{C\subset G_d^{ij}:g(C)=g\}.       \tag{1.1}
\]

The deletion of the fixed row is essential: in the strict-diameter stress
family, `d` is the unique global diameter and would otherwise receive every
charge.

Since the `c(g)` partition the four-cycles,

\[
 Q_{d,ij}:=C_4(G_d^{ij})=\sum_g c_{d,ij}(g).       \tag{1.2}
\]

There are fewer than `k^2/2` unordered edges.  Cauchy therefore gives the
exact implication

\[
 \sum_g c_{d,ij}(g)^2\le k^{2+o(1)}
 \quad\Longrightarrow\quad
 Q_{d,ij}\le k^{2+o(1)}.                          \tag{1.3}
\]

Together with (0.2), this proves `r(d)<=k^(3/2+o(1))`.  Thus a sufficient
local theorem is

\[
 \boxed{\min_{ij}\sum_g c_{d,ij}(g)^2\le k^{2+o(1)}
        \quad\hbox{for every }d\in D.}             \tag{1.4}
\]

Uniformly in `d`, (1.4) gives the same conditional wide-branch consequence
as the fixed-row gate:

\[
 T\le k^{7/2+o(1)},\qquad
 |A+J(A-A)|\ge k^{5/2-o(1)},\qquad
 k\le m^{4/5+o(1)}\quad(A\subset[m]^2).           \tag{1.5}
\]

The line-rich/transverse splice is still missing, so even a proof of (1.4)
would not yet be a full proof of #1208.

## 2. Exact stress data

For each row below, the six entries are

\[
 (Q_{d,ij},\ \max_g c_{d,ij}(g),\ \sum_g c_{d,ij}(g)^2)
\]

in projection order `uv, ux, uy, vx, vy, xy`.

For the 120-point square-root-heavy closure witness with `d=(0,-1)`:

| projection | `Q` | maximum book | charge moment |
|:--|--:|--:|--:|
| `uv` | 1,869 | 14 | 7,595 |
| `ux` | 1,922 | 29 | 12,838 |
| `uy` | 1,923 | 29 | 13,991 |
| `vx` | 2,008 | 44 | 15,126 |
| `vy` | 2,063 | 38 | 15,117 |
| `xy` | 2,071 | 26 | 9,419 |

The largest moment is `15,126=1.0504... k^2`.

For the 90-point strict-global-diameter witness with `d=(10000,0)`:

| projection | `Q` | maximum book | charge moment |
|:--|--:|--:|--:|
| `uv` | 473 | 30 | 5,215 |
| `ux` | 243 | 15 | 1,407 |
| `uy` | 262 | 22 | 1,928 |
| `vx` | 312 | 14 | 2,058 |
| `vy` | 447 | 34 | 4,701 |
| `xy` | 230 | 16 | 1,162 |

Here the largest moment is `5,215<k^2`.  All calculations are exact; the
finite data are calibration, not asymptotic evidence strong enough to prove
(1.4).

## 3. The surviving inverse problem is a `C_4`-book problem

The largest heavy charge class has 44 cycles.  All but one contain the same
relation edge in the projection graph.  The largest strict-diameter class
has 34 cycles, all containing the same relation edge.  Thus the large values
of `c(g)` found by the search are ordinary `C_4` books centered on a relation,
with the additional constraint that the charged actual edge `g` is longer
than every other variable edge appearing in each page.

Consequently, the most concrete next theorem is:

> Bound the total number of ordered pairs of fixed-row projection rectangles
> that share a charged variable-longest edge by `k^(2+o(1))`.

An injection of such rectangle pairs into `A^2` with subpolynomial
multiplicity would prove (1.4).  No such injection is known.  The length
ordering is the only input in this formulation that is not present in a
generic bipartite graph.

## 4. Four shortcuts that the exact witnesses kill

### 4.1 Affine quarter-turn orbits

For fixed `d`, the edge-vector map

\[
 T_d(e)=d-Je                                             \tag{4.1}
\]

has order four.  A relation is an occupied directed step from `e` to
`T_d(e)`.  In the 120-point witness there are ten completely occupied
four-orbits, so full orbit occupancy is compatible with distance-Sidonicity.
Orbit exclusion cannot prove the row bound.

### 4.2 Simultaneous cycles in several projections

Among the 11,852 distinct projection cycles of the 120-point row, 11,850
occur in exactly one projection and only two occur in three projections.
Pair-linearity explains why a four-relation set cannot be a cycle in
complementary projections, but this near-disjointness supplies no useful
global saving.

### 4.3 Linear rigidity

Regard the row equations as Gaussian-linear relations

\[
 z_u-z_v+i(z_x-z_y)=z_p-z_q.                         \tag{4.2}
\]

Over the exact test field, the 948 equations of the 120-point heavy witness
have rank 118 and nullity two: they already determine the configuration up
to translation and complex scaling.  The diameter family has fixed nullity
five through 90 points.  Therefore a dichotomy saying that many relations
force rigidity is true on the adversary but useless: rigidity itself does
not force repeated distances.

### 4.4 A three-factor parabola sieve

For the integer parabola `(t,t^2)`,

\[
 \|(t,t^2)-(s,s^2)\|^2
 =(t-s)^2\bigl(1+(t+s)^2\bigr)
 =(t-s)^2(t+s-i)(t+s+i).                            \tag{4.3}
\]

The tempting three local factors do not produce a dense collision-rich
planar construction: the exact initial interval through 1,000 points has all
499,500 distances distinct.  Moreover the one-parameter ambient set has
quartic distance height, so the extra local branch is lost to the ambient
scaling in the direct number-field adaptation.  This is a killed route, not
a theorem that every finite subset of the parabola is distance-Sidon.

## 5. Verification and bottom line

`verify_fixed_row_longest_book_gate.py` checks the two exact charge profiles,
the rigidity ranks, the affine-orbit occupancy, and the finite parabola
collision test.  The exploratory scripts contain the full intermediate
profiles and the two largest book cores.

The honest endpoint is:

* the variable-longest charge gives a clean new second-moment gate;
* it survives the two purpose-built square-root-heavy rows sharply;
* several natural proof shortcuts are now decisively excluded; and
* (1.4), its global propagation, and the line-rich splice remain unproved.
