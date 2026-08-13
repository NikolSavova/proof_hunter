# Erdős 791: growing-scale rounding, absorption, and exact micro-tiling barriers

Date: 2026-08-13

## Verdict

No rounding theorem strong enough to close the normalized-limit problem was
proved.  The attack does establish:

* a quantitative theorem showing that diffuse independent rounding, even with
  an `o(k)` deterministic core, leaves a positive density of holes and with
  constant probability requires `Omega(k)` repair elements;
* an exact alteration theorem under logarithmic representation intensity,
  together with a pair-budget proof that its hypothesis is impossible at
  positive quadratic density;
* a deterministic mesoscopic block-absorption lemma that repairs clustered
  holes at `o(k)` cost;
* a factorization theorem showing that exact no-slack `q`-element micro-tile
  types have a unique complementary type for every `q`; for prime `q` these
  are forced to be the standard fine/coarse digit pair.  Thus finite-field
  “many line directions” cannot provide a no-overhead integer lift; genuine
  carry slack is essential.

The remaining bridge is a correlated, growing-scale design theorem producing
zero-density, sufficiently clustered holes, or an approximate factorization
theorem that organizes the necessary carry slack.  Neither is supplied here.

## 1. Model

Write `M=N+1` for the number of targets and suppose `M~c k^2`.  A target `n`
is covered by selecting both endpoints of at least one edge in the matching

\[
 \mathcal P_n=\{\{a,b\}:0\leq a<b\leq N,\ a+b=n\},
\]

or by selecting the diagonal point `n/2` when it is integral.  Matchings for
different targets overlap heavily in their vertices.  This is an induced
edge-cover problem: one chooses vertices, while all pairs between the chosen
vertices become available.

## 2. Established: diffuse independent rounding leaves quadratically many holes

### Theorem 2.1

Let `D_k subset [0,N_k]` be a deterministic core with `d_k=|D_k|=o(k)`.
Independently select every `x notin D_k` with probability `p_x`, where

```text
sum_x p_x = k,              max_x p_x = eta_k -> 0,
M_k/k^2 -> c > 0.
```

Let `H_k` be the number of targets missed by `D_k union R_k`.  Then

\[
 \boxed{\liminf_{k\to\infty}\frac{\mathbb E H_k}{M_k}
        \geq \exp\!\left(-\frac1{2c}\right)>0.}             \tag{2.1}
\]

This includes a forced zero or any other sublinear deterministic absorber in
the core.

### Proof

Discard the `o(M_k)` targets already in `D_k+D_k`.  For each remaining target
`n`, put

\[
 \theta_n=\sum_{d\in D_k:\,n-d\notin D_k}p_{n-d},\qquad
 \lambda_n=\sum_{\{a,b\}\in\mathcal P_n\atop a,b\notin D_k}p_ap_b,
\]

with out-of-range terms omitted.  The event that no core--random pair covers
`n` and the event that no random--random pair covers it are decreasing events
of independent Bernoulli variables.  Harris--FKG therefore lower-bounds the
probability of their intersection by the product of their probabilities.
Within one target, the non-diagonal representation pairs are disjoint, so

\[
 \Pr(n\text{ is missed})
 \geq(1-\eta_k)
 \exp\!\left(-\frac{\theta_n}{1-\eta_k}
              -\frac{\lambda_n}{1-\eta_k^2}\right).        \tag{2.2}
\]

Here `log(1-u)>=-u/(1-u)` is used for both the single-vertex and pair factors;
`1-eta_k` accounts for a possible diagonal representation.

Every core--random ordered choice contributes to at most one target, and every
unordered random pair also contributes to at most one.  Hence

\[
 \sum_n\theta_n\leq d_k k=o(k^2),\qquad
 \sum_n\lambda_n\leq k^2/2.                               \tag{2.3}
\]

Average (2.2) over the remaining targets and apply convexity of the
exponential.  Equations (2.3), `eta_k->0`, and `M_k/k^2->c` give (2.1).

### Corollary 2.2 (linear alteration is frequently necessary)

There are constants `delta,gamma>0`, depending only on `c`, such that with
probability at least `delta`, the sampled set has at most `2k` elements, has
at least `delta M_k` holes, and every complete repair requires at least
`gamma k` new elements.

Indeed, Chernoff bounds make `|D_k union R_k|>2k` exponentially unlikely.
The expectation lower bound and `0<=H_k<=M_k` then give a constant-probability
event with a positive density of holes.  If `A` has `s` elements and `r` new
elements repair all its old holes, then

\[
 \boxed{H(A)\leq sr+\frac{r(r+1)}2.}                        \tag{2.4}
\]

The right side counts all possible new sums in `A+X` and the unordered sums
in `X+X`.  With `s<=2k`, a positive multiple of `k^2` on the left forces
`r>=gamma k`.

This theorem does not say that an exponentially rare independent sample can
never be a basis.  It says the usual “sample, bound the expected holes, then
alter” method has linear leading cost in this regime.

### Theorem 2.3 (even a growing aggregate modulus is relaxation-neutral)

For an integer `q>=1`, let `u_q` be uniform measure on `Z/qZ` and define

\[
 C_q=\sup\{c:\exists\mu\in\mathcal P([0,1]\times\mathbb Z/q\mathbb Z),
 \ \mu*\mu\geq2c(\lambda|_{(0,1)}\times u_q)\}.
\]

Then for every `q`, including a choice `q=q(k)` tending to infinity,

\[
 \boxed{C_q=C_{\rm conv}.}                                 \tag{2.5}
\]

Projection onto `[0,1]` proves `C_q<=C_conv`; tensoring a continuously
feasible measure with `u_q` proves the reverse inequality because
`u_q*u_q=u_q`.

This equality is relevant to actual growing scales, not only fixed-modulus
compactness.  If `q_k=o(M_k)`, then in every fixed macro interval `I` and
residue `r mod q_k`,

\[
 \#\{0\leq n<M_k:n/M_k\in I,\ n\equiv r\pmod {q_k}\}
 =\frac{M_k|I|}{q_k}+O(1).                                 \tag{2.6}
\]

Across a fixed number of macro bins the total normalized discrepancy is
`O(q_k/M_k)=o(1)`.  Thus merely appending aggregate residues modulo a
mesoscopic modulus—even `q_k` of order `k`—feeds the same false product-uniform
points into the relaxation.  A useful growing-scale hierarchy must couple
residues to lattice-scale differences/collisions or retain carry position at
resolution `q_k/M_k`; aggregate modular mass alone is not enough.

### Numerical scale

The limiting lower fractions in (2.1) are

```text
c=1/4:       exp(-2)             = 0.135335...
c=85/294:    exp(-147/85)        = 0.177389...
c=2/5:       exp(-5/4)           = 0.286505...
c=9/20:      exp(-10/9)          = 0.329193...
```

Thus the obstruction is not a small boundary loss.

## 3. Established: the independent alteration threshold and its budget barrier

### Proposition 3.1 (a sufficient but unusable logarithmic hypothesis)

Independently choose elements with probabilities `p_x`, with `p_0=1` and
total expected size `k`, and let

\[
 \lambda_n=\sum_{a<b,\ a+b=n}p_ap_b.
\]

If for some fixed `epsilon>0`

\[
 \lambda_n\geq(1/2+\epsilon)\log M                       \tag{3.1}
\]

for every nonzero target, then there is a deterministic set of size `k+o(k)`
whose sumset covers `[0,N]`, provided `M=Theta(k^2)`.

**Proof.** A target-hole probability is at most `exp(-lambda_n)`, so the
expected number of holes is at most
`M^{1/2-epsilon}=o(k)`.  With positive probability the selected cardinality
is `k+o(k)` and the hole count is `o(k)`.  Add each remaining hole; then every
patched target is `0+h`.

But (3.1) is impossible at positive quadratic density, since

\[
 \sum_{n=0}^N\lambda_n\leq\frac{k^2}{2}.                   \tag{3.2}
\]

When `M~c k^2`, the average intensity is at most `1/(2c)`, a constant.  The
logarithmic alteration threshold therefore loses at least a logarithmic factor
in range.  No tuning of independent probabilities changes this pair budget.

## 4. Established: a mesoscopic block absorber

### Lemma 4.1

Let `B subset [0,N]`, choose a block length `L`, and put
`P=[0,L-1]`.  Partition `[0,N]` into the aligned intervals

\[
 Q_j=[jL,\min((j+1)L-1,N)].
\]

Let `b` be the number of these blocks containing a target not covered by
`(B union P)+(B union P)`.  Then one can obtain a full interval basis by
adding at most `b` further elements.  The final size is at most

\[
 |B|+L+b.                                                    \tag{4.1}
\]

**Proof.** For every bad block add its left endpoint `jL`.  Then
`jL+P` covers the entire block.

### Conditional two-scale rounding theorem

If `N_k=Theta(k^2)` and a correlated mesoscopic procedure produces sets
`B_k` for which some `L_k=o(k)` has

```text
|B_k| <= k+o(k),
only o(k) aligned L_k-blocks contain holes after adding [0,L_k-1],
```

then Lemma 4.1 deterministically rounds them to interval bases of size
`k+o(k)`.  Consequently, if the preliminary ranges approach `alpha_+ k^2`,
this hypothesis forces `alpha_-=alpha_+`.

This is a genuine `o(k)` absorption statement: it can repair far more than
`o(k)` individual holes when they cluster.  It is also explicit about the
missing input.  Theorem 2.1 shows diffuse independent rounding does not supply
it by the usual expectation/alteration argument: on the constant-probability
failure event from Corollary 2.2, positive-density holes meet at least `H/L`,
hence `Omega(k^2/L)>>k`, bad blocks whenever `L=o(k)`.

## 5. Established: exact micro-tiles have only complementary roles

A tempting growing-scale idea is to use the `q+1` line directions of
`F_q^2`, assigning many micro-role colors so that differently colored macro
elements generate a full `q^2` block.  Integer carries destroy this proposal.
The obstruction already appears in an exact classification.

### Theorem 5.1 (exact interval factorization)

Let `q>=2` and let `X,Y` be `q`-element sets of nonnegative integers.  If

\[
 [t,t+q^2-1]\subseteq X+Y,
\]

then after translating both minima to zero their set-polynomials factor

\[
 P_X(z)P_Y(z)=G_q(z):=1+z+\cdots+z^{q^2-1}.                \tag{5.1}
\]

Consequently a fixed normalized tile `X` has at most one normalized partner
`Y`.  There is no self-partner.  If `q` is prime, the only possibilities are

\[
 X=[0,q-1],\quad Y=q[0,q-1],                               \tag{5.2}
\]

or the two roles are exchanged.  In particular every target has a unique
representation and there are no sums outside the displayed interval.

### Proof

There are exactly `q^2` ordered cross-pairs and already `q^2` required target
values.  Thus the sum map is bijective and `X+Y` is exactly the interval.
Subtract the minima so that the interval starts at zero.  With

\[
 P_X(z)=\sum_{x\in X}z^x,\qquad P_Y(z)=\sum_{y\in Y}z^y,
\]

unique representation gives (5.1).  The polynomial `G_q` is squarefree over
`Q`: it is the product of the distinct cyclotomic polynomials `Phi_d` with
`d|q^2`, `d>1`.  Hence `G_q/P_X` uniquely determines any normalized partner,
and `P_X^2=G_q` is impossible.  This proves the general claims.

When `q` is prime, unique factorization specializes to

\[
 P_X(z)P_Y(z)=\Phi_q(z)\Phi_{q^2}(z).                      \tag{5.3}
\]

Both cyclotomic polynomials are irreducible in `Z[z]`.  Unique factorization,
the constant terms one, and the fact that both set-polynomials are nonconstant
force them to be the two factors in (5.3).  These are precisely

\[
 \Phi_q(z)=1+z+\cdots+z^{q-1},\qquad
 \Phi_{q^2}(z)=1+z^q+\cdots+z^{(q-1)q}.
\]

This proves (5.2).

### Corollary 5.2 (exact efficient interaction graphs are bipartite)

Consider any family of `q`-element integer micro-tiles, identify translates,
and join two normalized tile types when their cross-sum contains `q^2`
consecutive values.  Theorem 5.1 says every nonisolated type has a unique
complementary type and none complements itself.  Hence the interaction graph
is a matching, in particular bipartite and triangle-free.  For prime `q` its
only nonisolated types are the fine interval and coarse `q`-progression.

Combined with the weighted Mantel/current-sum count, a no-slack architecture
of these exact tiles has density at most `1/4`.  This algebraically rules out
importing the many pairwise-complementary line directions of `F_q^2` into the
integer interval problem at zero leading overhead.

The theorem does **not** cover:

* tiles of size `q+o(q)` with `o(q^2)` collisions or omissions;
* phased pairs whose sums split one block across two adjacent carry states;
* parallelogram patches combining several component pairs.

Kohonen-type constructions exploit exactly this sort of carry slack, so no
contradiction with the `85/294>1/4` construction arises.

## 6. Why standard LLL and nibble machinery does not immediately apply

These are method audits, not impossibility theorems.

### Lovasz local lemma

Under full-support elementwise rounding, the hole event for target `n` depends
on essentially every selection variable in `[0,n]`.  The natural dependency
graph is therefore dense (the top target is adjacent to all others), while
Theorem 2.1 gives constant-order bad-event probabilities.  The symmetric LLL
condition `e p(d+1)<=1` fails by a factor of order `N`.  Reducing each hole
probability to `O(1/N)` requires logarithmic representation intensity, which
is excluded by (3.2).  Moreover hole events are decreasing and positively
correlated under product measure, so the usual lopsided negative-dependence
shortcut is absent.

### Rodl nibble

The natural 3-uniform incidence edges are `{a,b,n}` with `a+b=n`.  A nibble
selects nearly disjoint hyperedges; the postage-stamp objective instead needs
`Theta(k^2)` target edges supported on only `k` element vertices, so each
chosen element must be reused `Theta(k)` times.  Selecting representation
edges independently destroys this endpoint reuse, while selecting element
vertices returns to the nonlinear induced-cover problem.  A specialized
high-reuse nibble could still exist, but standard matching/packing theorems do
not provide it directly.

## 7. Exact missing lemmas

Two explicit bridges remain.

### Design/absorption bridge

Construct, from a growing-scale feasible flow, a correlated preliminary set
with holes contained in `o(k)` blocks of length `o(k)`.  Lemma 4.1 would then
close the normalized limit without leading loss.  Merely proving bounded
expected representation multiplicity or matching fixed-bin flows is
insufficient by Theorem 2.1.  Aggregate residues at any `q=o(N)` are also
insufficient by Theorem 2.3.

### Approximate factorization/carry bridge

Classify pairs of `q+o(q)` integer micro-tiles which cover almost all of a
`q^2` block, including which omissions can be transferred consistently to an
adjacent carry state.  The exact theorem forces two roles, but no stability
theorem was proved.  A useful positive result would exhibit a multi-role
family with total tile cost `q+o(q)` and a carry automaton covering all but
`o(q^2)` residues in only `o(k)` repairable macro blocks.

These hypotheses are substantially stronger than continuous or fixed-modulus
flow feasibility and are the weakest explicit sufficient conditions isolated
in this lane.

## 8. Verification artifact

Run

```bash
python3 phase2/loop/erdos791/full_attack2/analytic/growing_scale_checks.py
```

It produces `GROWING_SCALE_CHECKS.json` and checks:

* all normalized `q=2,3,4` interval-factor pairs (two canonical orientations
  for the primes, six complementary orientations at composite `q=4`);
* the canonical factorization through prime `q=19`;
* the alteration capacity inequality on 65,536 small set pairs;
* 3,321 block-absorber instances;
* finite diffuse-rounding lower bounds at four quadratic coefficients.

These computations sanity-check the exact finite statements.  They are not
evidence for either missing asymptotic lemma.
