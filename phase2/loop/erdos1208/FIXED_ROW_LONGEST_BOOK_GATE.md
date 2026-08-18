# The fixed-row variable-longest `C_4` book gate: falsification

## 0. Status

This note records a natural sufficient fixed-row estimate, the two finite
stress tests that initially supported it, and the scalable six-biclique
construction that **disproves it**.  The conditional implication is correct;
the proposed moment hypothesis is false by a full power of `k`.

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

Together with (0.2), this proves `r(d)<=k^(3/2+o(1))`.  The tempting
sufficient hypothesis was

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

The line-rich/transverse splice would still be missing even if (1.4) were
true.  The next section shows that it is not.

## 2. Six simultaneous bicliques disprove (1.4)

Identify the plane with the complex numbers and put

\[
 (\gamma_0,\gamma_1,\gamma_2,\gamma_3)=(1,-1,i,-i).
\]

The fixed-row equation is

\[
 \sum_{a=0}^3\gamma_a z_a=d.                    \tag{2.1}
\]

Fix an integer `s`.  For each of the six role pairs `{p,q}`, independently
choose `s` labels `a_i` in role `p`, `s` labels `b_j` in role `q`, and one
fresh label `w_ij` in a third role `r` for every cell `(i,j)`.  If `t` is the
fourth role, define one more label by

\[
 z_{ij}=\gamma_t^{-1}
 \bigl(d-\gamma_p a_i-\gamma_q b_j-\gamma_r w_{ij}\bigr). \tag{2.2}
\]

Adjoin two fixed points whose oriented difference is `d`.  Use disjoint
labels for the six gadgets.  The total number of points is

\[
 k=6(2s^2+2s)+2=12s^2+12s+2.                    \tag{2.3}
\]

Every cell in the `{p,q}` gadget is a relation in (2.1), so projection
`pq` contains a `K_{s,s}`.  Therefore all six projections simultaneously
have at least

\[
 Q_s={s\choose2}^2=\Theta(s^4)=\Theta(k^2)       \tag{2.4}
\]

four-cycles.  This is a sharpness construction for the fixed-row `C_4` gate,
not a counterexample to it.

The coordinates can be chosen in the Gaussian integers so that the union is
distance-Sidon and every intended relation is transverse.  Here is an exact
genericity certificate.  Treat all free coordinates and `d` as independent
complex variables.  Every constructed point is a Gaussian-linear form in
those variables.  Two edge norms are identically equal exactly when their
coefficient vectors differ by a scalar of modulus one.  Any candidate
identity uses four endpoints and hence, after relabelling, at most four row
and column indices in each gadget.  The symbolic side-four checker enumerates
all 29,161 edges of the resulting 242-point template and finds distinct norm
signatures for every edge.  Consequently no unwanted equality is a polynomial
identity for arbitrary `s`.  Avoiding the finitely many nonzero distance and
transversality polynomials gives rational, and after scaling integral,
choices.

Now restrict attention in projection `pq` to its `K_{s,s}` cycles.  Whatever
their variable-longest charges are, the charge can only be one of

* the `2 binom(s,2)` selected side edges, or
* the at most `2s^2` distinguished relation edges.

Thus at most `3s^2-s` actual edges receive all `Q_s` charges.  Cauchy gives

\[
 \sum_g c_{d,pq}(g)^2
 \ge {Q_s^2\over 3s^2-s}
 =\Omega(s^6)=\Omega(k^3).                       \tag{2.5}
\]

There is one gadget for every projection, so (2.5) holds simultaneously in
all six projections.  Hence

\[
 \min_{pq}\sum_g c_{d,pq}(g)^2=\Omega(k^3),       \tag{2.6}
\]

which decisively falsifies (1.4).

The same example kills the proposed matching of rectangles to their
algebraically adjacent actual edges.  A single `K_{s,s}` has `Theta(s^4)`
rectangles but only `O(s^3)` such adjacent edges.  At `s=10`, the intended
projection has 2,025 rectangles and only 1,890 adjacent actual edges.

## 3. Why the first two finite tests were misleading

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

## 4. The misleading single-book picture

The largest heavy charge class has 44 cycles.  All but one contain the same
relation edge in the projection graph.  The largest strict-diameter class
has 34 cycles, all containing the same relation edge.  Thus the large values
of `c(g)` found by the search are ordinary `C_4` books centered on a relation,
with the additional constraint that the charged actual edge `g` is longer
than every other variable edge appearing in each page.

Before the six-biclique construction, this suggested the following target:

> Bound the total number of ordered pairs of fixed-row projection rectangles
> that share a charged variable-longest edge by `k^(2+o(1))`.

Such an injection cannot exist uniformly: the six-biclique family has
`Omega(k^3)` rectangle pairs sharing a variable-longest charge.  The apparent
quadratic scale in the two closure families came from testing dense endpoint
reuse without also testing the complementary sparse/fresh-endpoint branch.

## 5. Four other shortcuts that the exact witnesses kill

### 5.1 Affine quarter-turn orbits

For fixed `d`, the edge-vector map

\[
 T_d(e)=d-Je                                             \tag{4.1}
\]

has order four.  A relation is an occupied directed step from `e` to
`T_d(e)`.  In the 120-point witness there are ten completely occupied
four-orbits, so full orbit occupancy is compatible with distance-Sidonicity.
Orbit exclusion cannot prove the row bound.

### 5.2 Simultaneous cycles in several projections

Among the 11,852 distinct projection cycles of the 120-point row, 11,850
occur in exactly one projection and only two occur in three projections.
Pair-linearity explains why a four-relation set cannot be a cycle in
complementary projections, but this near-disjointness supplies no useful
global saving.

### 5.3 Linear rigidity

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

### 5.4 A three-factor parabola sieve

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

## 6. Verification and bottom line

`verify_fixed_row_longest_book_gate.py` checks the two original charge
profiles, the rigidity ranks, the affine-orbit occupancy, and the finite
parabola collision test.  `verify_fixed_row_six_biclique.py` checks the exact
side-four genericity template and a concrete 866-point, side-eight instance
with 784 four-cycles in every projection.  The exploratory scripts contain
the full intermediate profiles and the two largest book cores.

The honest endpoint is:

* the conditional Cauchy reduction in Section 1 is valid;
* its moment hypothesis (1.4) is false with cubic rather than quadratic mass;
* the underlying fixed-row `C_4<=k^(2+o(1))` conjecture survives and is
  exponent-sharp on the six-biclique family; and
* the proof must split sparse/fresh-endpoint bicliques from dense endpoint
  reuse instead of controlling all rectangle books by one moment.
