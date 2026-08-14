# Erdős 838: plan of attack after the lower-bound campaign

> **Date:** 2026-08-13
>
> **Status:** research plan, not a claimed proof
>
> **Current rigorous window (base two):**
> \[
> \frac14\le \liminf \frac{\log f(N)}{(\log N)^2}
> \le \limsup \frac{\log f(N)}{(\log N)^2}\le\frac12.
> \]

This plan incorporates the seven new Sol reports in
`campaign_lower_*_20260813.md`, the corrected synthesis in
`CAMPAIGN_SYNTHESIS_20260813.md`, and the earlier unrestricted dossiers.  Its
purpose is to concentrate the next campaign on one exact object that has not
already been eliminated.

All logarithms below are base two.

---

## 1. What the new notes changed

The round-one campaign established four facts that must constrain all future
work.

1. The global cap--cup product is the wrong target.  A lower bound
   `log C+log U >= (1/2-o(1))log^2 N` implies only the existing coefficient
   `1/4` for the convex count, because cap and cup mass can be exponentially
   anti-aligned across endpoint pairs.
2. Every argument using only asymmetric cup--cap thresholds and hereditary
   size-by-size double counting is capped at `1/4`.  Its sharp normalized
   consequence is
   \[
     (c+u)H\!\left(\frac{c}{c+u}\right)\ge\frac14.
   \]
   A successful proof must retain extension or overlap information.
3. The canonical module tree does not reduce arbitrary order types to the
   decomposable class: triangular-hull configurations can be arbitrarily large
   indecomposable one-node instances.  The unrestricted problem must therefore
   be handled directly.
4. The multiscale reset proof for decomposable sets has now been independently
   audited and is valid.  Its endpoint alignment, rather than its radial
   cap--cup product alone, is the part that must be reproduced.

The exact unrestricted statistic remains
\[
 V(P)=N+\sum_{s<t}c(s,t)u(s,t),                 \tag{1}
\]
where `c(s,t)` and `u(s,t)` count caps and cups with the same left and right
endpoints.  Bounding either the sum in (1), or its largest term (the two differ
by at most `N^2`), at coefficient `1/2` resolves the problem.

---

## 2. Primary reformulation: a reverse-product trace inequality

After a generic perturbation inside the order type, assume all chord slopes
are distinct.  List the edges
\[
 e_1,e_2,\ldots,e_M,\qquad M=\binom N2,
\]
in increasing slope order.  For `e=(i,j)`, `i<j`, put
\[
 T_e(z)=I+zE_{ji}.
\]
Define the opposite products
\[
 A(z)=T_{e_M}(z)\cdots T_{e_1}(z),\qquad
 B(z)=T_{e_1}(z)\cdots T_{e_M}(z).              \tag{2}
\]

### Exact matrix lemma

For `s<t`,

- `A(z)_{t,s}` is the generating polynomial of cups with endpoints `s,t`,
  with a chain on `r+1` vertices weighted by `z^r`;
- `B(z)_{t,s}` is the analogous polynomial for caps.

This follows by processing an edge `i j` as the update
`row_j <- row_j+z row_i`.  A contributing matrix monomial is exactly a path
whose consecutive slopes occur in increasing order; reversing the processing
order counts decreasing-slope paths.

A cap and a cup with the same endpoints have disjoint interiors and their union
is a unique convex subset.  Hence the full convex-set partition function is
\[
 Z_P(z):=\sum_{\varnothing\ne K\text{ convex}}z^{|K|}
 =Nz+\langle A(z),B(z)\rangle_F-N.              \tag{3}
\]
In particular,
\[
 \boxed{V(P)=\langle A(1),B(1)\rangle_F
       =\operatorname{tr}(A(1)^\mathsf T B(1)).} \tag{4}
\]

For every `i<j<k`, the slope of `ik` is a strict weighted average of the
slopes of `ij` and `jk`.  Thus the edge order is a **stretchable reflection
order** on the positive roots of type `A_(N-1)`.  Reflection orders are the
root sequences of reduced words for the longest permutation; stretchability
is the additional geometric restriction.

The full lower bound is therefore equivalent to the following theorem.

> **Reverse-product reflection-order target (RPR).**  For every stretchable
> type-`A_(N-1)` reflection order,
> \[
> \log\langle A(1),B(1)\rangle_F
> \ge \frac12(\log N)^2-o((\log N)^2).          \tag{RPR}
> \]

This is the primary target.  It retains both hull endpoints, applies directly
to indecomposable order types, and has an exact finite interface through
reduced words and braid moves.  A theorem for all reflection orders would be
stronger and is worth testing first, but it must not be assumed: nonstretchable
pseudoline orders may be genuine counterexamples.

A narrow initial prior-art search found the standard reflection-order/reduced-
word correspondence and extensive PBW/Lusztig literature, but no reverse-
product Frobenius inequality or this path-count statistic.  A proper database
and expert search is required before any novelty claim.

---

## 3. Stage I: exact discovery engine (first gate)

### 3.1 Build the evaluator

Extend the initial `reflection_trace.py` checker and add a search driver with
four independent modes.

1. Read rational coordinates, sort all slopes, and compute (2)--(4) exactly.
2. Read a reduced word for `w_0`, construct its root sequence, and compute the
   same matrices without coordinates.
3. Compute the graded polynomial (3), so that `[z^k]Z_P(z)` is the exact number
   of convex `k`-sets.
4. Report the full endpoint arrays, their largest coordinate product, row and
   column masses, and the trace.

Required cross-checks:

- the six-point `T_(4,2)` cell: `(C,U,V)=(31,31,50)`;
- the audited 36-point composition: `(14136,14136,441399)`;
- every available complete order type through `N=9` against
  `order_type_audit.py`;
- deep `T_(4,2)` iterates, Horton sets, and the alternating least-index
  obstruction.

### 3.2 Search the right state space

For small `N`, enumerate reflection orders through reduced words, quotienting
commuting disjoint roots.  For larger `N`, use beam search and braid-move
annealing on
\[
 \log\langle A,B\rangle_F,
\]
not on `C U`.  Store exact integer certificates for every record.

For a promising root order, test a sufficient stretchability model by fixing
`x_i=i`.  Every proposed slope comparison is then a strict linear inequality
in the `y_i`; linear programming can find a rational realization or certify
infeasibility in this model.  Infeasibility with fixed `x` is not a proof of
nonstretchability, so unresolved candidates must be passed to an oriented-
matroid/stretchability checker.

### 3.3 Gate A

There are three possible outcomes.

1. **All reflection orders remain at or above `1/2`.**  Pursue the stronger
   all-reflection-order theorem; Coxeter moves are then legitimate proof tools.
2. **Only nonstretchable orders fall below `1/2`.**  Identify the first rank-3
   stretchability circuit that excludes them and make that circuit explicit in
   the proof state.
3. **A stretchable family falls below `1/2`.**  Stop trying to prove (RPR).
   Turn the family into an exact rational upper construction and determine its
   asymptotic coefficient.  This would improve our paper, although a matching
   lower bound would still be needed to solve #838 completely.

This gate prevents another campaign from spending proof effort on a false
scalar inequality.

---

## 4. Stage II: the proof attack on (RPR)

The proof should be developed in the following order.

### 4.1 Derive an exact contiguous-cut formula

Split the horizontal order into consecutive sets `L<R`.  Any increasing-
`x` path from `L` to `R` uses exactly one cross edge.  For a cross edge
`e=(i,j)`, define:

- prefix path vectors in `L` whose last slope is below (or above) `slope(e)`;
- suffix path vectors in `R` whose first slope is above (or below)
  `slope(e)`.

Then every cross entry of `A(z)` and `B(z)` is an exact sum, over cross edges,
of a prefix weight times `z` times a suffix weight.  Write this formula before
proposing an inequality.  It is the arbitrary-order-type replacement for the
single product `X(A)Y(B)` at a strong glue.

The minimum viable state is therefore a pair of **slope-filtered boundary
vectors**.  The already-refuted scalar states `C,U`, a one-endpoint history,
or a fixed finite list of flag densities are not sufficient.

### 4.2 Search for the cut anti-avoidance lemma

On exact small reflection orders and recursive adversarial families, test
inequalities with this form:

> If the forward cap/cup contribution across a balanced cut is deficient by
> `D` bits, the reflection-order betweenness constraints force at least `D`
> bits of persistent mass into an opposite slope-filtered boundary coordinate.

This is the precise analogue of the decomposable reset.  The desired loss per
cut is `O(log N)` or another amount summing to `o(log^2 N)`.  Any candidate
must be tested under all `A_2` braid moves and against:

- cap-heavy/cup-heavy endpoint anti-alignment;
- the six-point cell and its iterates;
- the exact Horton recursion;
- nonstretchable reflection orders found by Stage I.

Do not patch a failed scalar inequality with a constant.  Record the smallest
counterexample and enlarge the hereditary boundary state only if the failure
identifies information that is both exact and reusable at the next scale.

### 4.3 Multiscale assembly

Once the one-cut lemma is proved, select nested contiguous intervals by
following a larger side through a `Theta(sqrt(log N))`-bit window.  The target
assembly is the already-audited reset proof:

- many small compatible events directly create enough path choices;
- otherwise `Theta(sqrt(log N))` macroscopic cuts each have nearly full radial
  boundary mass;
- a small trace forces a reset at the deepest cut;
- repeated same-direction attachments accumulate the deficit in a persistent
  coordinate;
- a later opposite product forces
  `log V >= (1/2)log^2 N-O(log^(3/2)N)`.

The assembly is not the risky step; the new mathematical content is the
contiguous-cut anti-avoidance lemma.  It should be stated and audited as a
standalone theorem before being inserted into the multiscale argument.

### 4.4 Gate B

- If a finite, scale-stable boundary state survives exhaustive and recursive
  tests, commit to the full (RPR) proof.
- If every exact state needs unbounded slope history, move to the graded
  supersaturation target below rather than disguising the history in a scalar
  potential.

---

## 5. Stage III fallback: graded supersaturation

Equation (3) packages every fixed-size count in the same endpoint-correct
object.  Let `mu_k(n)` be the minimum number of convex `k`-sets in an
`n`-point configuration.  The incremental target is
\[
 \mu_k(2^{2k+o(k)})
 \ge 2^{(1+\eta-o(1))k^2}                       \tag{5}
\]
for any fixed `eta>0`.  The standard argument is `eta=0`; (5) improves the
unrestricted lower coefficient to `(1+eta)/4`.  The full coefficient `1/2`
would correspond to `eta=1` at this scale.

Before attempting a proof, use the graded matrix recurrence to compute the
**diagonal regime** `k about (log n)/2` for:

1. balanced Pascal-template iterates;
2. canonical Baek--Balko `x`-blow-ups;
3. record-low reflection orders from Stage I;
4. small complete order-type data.

The existing fixed-`k`, infinite-depth calculations do not answer this
diagonal question.  If these tests drive `eta` to zero, discard (5).  If a
uniform positive margin survives, seek a growing-order planar inequality for
the coefficient of (3), not a fixed convex-quadruple density.  Candidate tools
include entropy on the two slope-filtered boundary vectors, containers with
rank-3 codegree constraints growing with `k`, or stability toward recursive
reflection orders.

This fallback is deliberately incremental: proving any explicit `eta>0`
would be a new lower bound even if (RPR) remains open.

---

## 6. Construction-side adversary

The search in Stage I doubles as a truth check.  Any route below `1/2` must
escape all proved construction barriers, so it should be required to exhibit
at least one of:

- state complexity growing with depth;
- a macroscopic nondecomposable template jump;
- noncanonical extremal Baek--Balko cells in the remaining parameter window;
- mixed-triple geometry outside the vertical endpoint-cluster rule.

The objective is always the exact trace (4), including every larger-support
term.  Separate cap/cup marginal optimization is rejected at the design stage.
Every coordinate candidate is checked in exact rational arithmetic and across
several perturbation scales.

---

## 7. Routes not to restart

Unless a new lemma explicitly repairs the recorded failure, do not spend time
on:

- global `C U` without common endpoints;
- repeated Erdős--Szekeres subset double counts or same-type transversals;
- a canonical decomposition bridge through indecomposable nodes;
- Székely graph transfer;
- hinged-history compression, even nonlocal with `2^{O(k log k)}` fibres;
- fixed lists of convex-quadruple/flag densities;
- finite-state reflected or anti-aligned vertical blow-ups;
- multiplying nested cages;
- local scalar Bellman potentials already killed by iterated Pascal examples.

---

## 8. One-week execution schedule and success criteria

### Days 1--2: exact gate

- finish the matrix/graded evaluator;
- prove and document (3)--(4);
- exhaust small reflection orders and run braid search;
- compute the diagonal supersaturation profile on the upper construction.

### Days 3--4: one-cut theorem

- derive the exact slope-filtered cut formula;
- enumerate candidate cut inequalities;
- kill them on the standard adversarial families;
- freeze the smallest state that survives.

### Days 5--6: proof or pivot

- assemble the multiscale reset if the cut lemma survives; or
- prove a concrete positive `eta` in (5); or
- certify a stretchable trace-minimizing family if the conjectured value is
  false.

### Day 7: verification and packaging

- independent reconstruction by another model and a human-readable audit;
- exact certificates and asymptotic checks;
- formalize the finite matrix/path bijection and any stable algebraic lemma in
  Lean where practical;
- repeat the prior-art search using the final theorem's exact language.

Success is, in descending order:

1. (RPR), which together with the proved upper bound solves #838 with limit
   `1/2`;
2. any universal coefficient `1/4+delta` from the trace or any `eta>0` in
   (5), which improves the lower bound;
3. an exact stretchable family below `1/2`, which improves the upper bound and
   changes the conjectured answer;
4. a clean theorem showing a precisely defined reflection-order method cannot
   exceed `1/4`, provided it is genuinely stronger than the barrier already
   banked.

The immediate next command-level task is to implement and exhaustively verify
the reverse-product trace evaluator.  No further high-level campaign should
launch until Gate A reports whether (RPR) survives the broader reflection-order
state space.
