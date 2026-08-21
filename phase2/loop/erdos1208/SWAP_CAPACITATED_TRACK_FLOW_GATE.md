# Capacitated track flow isolates the exact Hall-deficiency core

## 1. Outcome

The balanced-row theorem assigned all pointed decorations of one occurrence
to a single endpoint-track row.  The endpoint-pencil union bound does not
require that restriction: each pointed decoration may independently choose
any high endpoint and any one of the six physical tracks of its occurrence
incident there.

This freedom has an exact max-flow formulation.  Let `O_hi` be the high
occurrences and retain the weight

\[
 w(o)={r_{C(o)}-1\choose2}.                         \tag{1.1}
\]

A row is an endpoint-labelled directed-track token

\[
 \rho=(x,\text{track slot},\text{opposite endpoint}). \tag{1.2}
\]

Let `R(o)` be all rows belonging to `o` at high endpoints.  For a high
endpoint `x`, let `T_x` be the full token support, `s_x=|T_x|`, and let
`a_x(u)` count occurrences using token `u`.  Give row `(x,u)` base capacity

\[
 b_x(u)=s_x-\mathbf1_{a_x(u)=1}.                  \tag{1.3}
\]

This is exactly the number of partner tokens available to that row.  For an
integer `L>=1`, define the Hall deficiency

\[
 \boxed{
 D_L=\max_{X\subseteq O_{hi}}
 \left(
   \sum_{o\in X}w(o)
   -L\sum_{\rho\in R(X)}b(\rho)
 \right)_+.}                                      \tag{1.4}
\]

Then all but exactly `D_L` pointed decorations can be assigned to incident
rows so that row `rho` receives at most `Lb(rho)` decorations.  Balancing
each row over its partner tokens and using

\[
 \sum_\rho b(\rho)\le144k(k-1)^2                 \tag{1.5}
\]

gives

\[
 \boxed{
 {\mathcal P_\Lambda\over3}
 \le144Lk(k-1)^2+D_L.}                            \tag{1.6}
\]

Consequently the whole endpoint-pencil branch follows from the one exact
target

\[
 \boxed{D_L\le N^{o(1)}m^2}                       \tag{1.7}
\]

for a subpolynomial `L=N^{o(1)}`.  This is stronger than bounding heavy rows
after an arbitrary occurrence-level assignment.  A survivor is a set of
owner occurrences whose *entire union of actual endpoint-labelled tracks*
has insufficient partner capacity.

## 2. Exact max-flow/min-cut proof

Replace each occurrence `o` by a left vertex of supply `w(o)` and every row
`rho` by a right vertex of capacity `Lb(rho)`.  Connect `o` to all
`rho in R(o)` with infinite capacity.  Integrality gives an assignment of
individual decorations.

For a finite cut, if a set `X` of occurrence vertices lies on the source
side, every row in `R(X)` must also lie there.  The cut capacity is

\[
 \sum_{o\notin X}w(o)+L\sum_{\rho\in R(X)}b(\rho). \tag{2.1}
\]

Subtracting its minimum from `sum_o w(o)` proves (1.4) and the exact
unmatched-mass statement.

At endpoint `x`, every row has at most `s_x` partner tokens and there are
`s_x` rows.  A token has one of twelve directed roles and one of `k-1`
opposite endpoints.  Hence

\[
 \sum_\rho b(\rho)
 \le\sum_xs_x^2
 \le144k(k-1)^2,                                  \tag{2.2}
\]

which proves (1.5)--(1.6) using the balanced-row theorem.

## 3. What a deficient cut means geometrically

Every occurrence contributes its actual six `D` tracks, with both physical
endpoints and roles retained.  Thus a maximizing set `X` in (1.4) has

\[
 \sum_{o\in X}{r_{C(o)}-1\choose2}
 >L\sum_{(x,u)\in R(X)}
 \bigl(s_x-\mathbf1_{a_x(u)=1}\bigr).             \tag{3.1}
\]

This rules out all assignment artefacts.  Such an `X` must concentrate
quadratic rich-cell weight on a small collection of repeatedly used physical
tracks, simultaneously at every endpoint/role available to its occurrences.
Two repeated rows feed the exact rank-five relative-owner map; a repeated
single row is the corresponding anchored pencil.  The missing theorem is
therefore a geometric expansion statement for the six-track incidence
hypergraph:

> every Hall-deficient occurrence core has total deficiency at most
> `N^{o(1)}m^2`.

It is essential to retain the six tracks.  Dropping them to anonymous
`D-D` directions recreates the already-false ambient energy gates.

There is an unconditional low-weight/low-repetition theorem.  Fix `W,A>=1`
and retain occurrences satisfying

\[
 w(o)\le W,qquad
 a(\rho)\le A\quad\hbox{for every }\rho\in R(o).  \tag{3.2}
\]

For every subset `X` of these occurrences, write
`I_X=sum_{o in X}|R(o)|`.  Since each occurrence has a row,

\[
 |X|\le I_X
 =\sum_{\rho\in R(X)}\deg_X(\rho)
 \le A|R(X)|
 \le A\sum_{\rho\in R(X)}b(\rho).                \tag{3.3}
\]

Therefore

\[
 \sum_{o\in X}w(o)
 \le WA\sum_{\rho\in R(X)}b(\rho),               \tag{3.4}
\]

and the Hall deficiency is zero at `L=WA`.  With subpolynomial `W,A`, this
pays the entire doubly-low branch directly from `k^3`.  Every genuine
survivor contains either

1. an occurrence with `w(o)>W`, equivalently a very rich owner cell; or
2. an endpoint-labelled physical track used by more than `A` occurrences.

This improves the earlier cyclic `R Delta^2` cutoff to one factor of track
multiplicity and removes its dependence on an arbitrary cyclic ordering.

The deficiency need not vanish pointwise.  Independent low-load owner
blocks may share one physical edge while all their other endpoints are
fresh; this creates linear deficiency but is harmless relative to `k^3`
and the ambient `m^2` budget.  The target is (1.7), not `D_L=0`.

## 4. Genuine stress audit

The optimal-core analyzer solves the integral flow exactly.  At
`Lambda=16`, every pointed record is matched already with `L=1` for each of

\[
 \text{Costas }23, 29, 31, 37.
\]

Their canonical balanced-row collision masses were respectively
`0,212,1308,0`; the flexible flow removes even the two nonzero finite rows.
The available base-capacity totals are `72860,588248,137080,734524`, so the
stress is not near a Hall cut.  The stored Golomb, lifted-parabola, and
rank-flat barriers have zero selected same-centre third mass and remain
irrelevant to this gate.

## 5. Status and next attack

The flow theorem and (1.6) are unconditional.  Bound (1.7) is open.  It is
now the smallest direct support gate: proving it closes the endpoint-pencil
branch, while a counterexample must be a genuine polynomial-height
distance-Sidon family with a dense six-track Hall core.

The next useful decomposition is not another arbitrary dyadic moment.  The
doubly-low portion is already closed by (3.4).  One should take a minimal
maximizing cut `X`, separate its very-rich occurrences, and apply the
two-zero-coordinate specialization of the rank-five relation to its
high-multiplicity physical tracks together with the metric height budget.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_capacitated_track_flow.py
```

The verifier compares integral max flow with the exact subset formula
(1.4) on exhaustive small incidence systems and checks the row-capacity and
support bounds on deterministic and seeded random six-track systems.  The
optimal-core analyzer independently computes the four Costas flow profiles.
