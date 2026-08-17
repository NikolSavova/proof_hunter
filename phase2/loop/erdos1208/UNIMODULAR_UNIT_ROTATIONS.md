# Exact rotations from unimodular algebraic units

This note records a possible upper-construction mechanism for Erdős 1208
which is genuinely different from the split-prime congruence sieve.  The
mechanism is rigorous; the missing arithmetic input is the construction of a
field family with enough *small* independent unimodular units.

## 1. The disjoint-rotation lemma

Let `K` be a number field embedded in `C`, closed under complex conjugation,
and let

\[
  V_K=\{u\in\mathcal O_K^\times:|u|=1\}
\]

be its group of unimodular units at the chosen embedding.  Multiplication by
`u` is an exact Euclidean rotation of the chosen complex plane.

Let `B` be a finite Minkowski box in `O_K`, let `P` be its image in the chosen
complex embedding, and let `A` be a distance-Sidon subset of `P`.  Lift `A`
back to a set `S` in `B`, and put

\[
  E=(S-S)\setminus\{0\}.
\]

Every oriented nonzero difference has a unique representation, so

\[
  |E|=|A|(|A|-1).
\]

If `U` is any finite subset of `V_K` containing no two elements which differ
by a sign, then the sets

\[
  uE,\qquad u\in U,
\]

are pairwise disjoint.  Indeed, if `ue=ve'`, then the chosen embedding gives
`|e|=|e'|`.  Distance uniqueness implies `e'=+e` or `e'=-e`, and the integral
domain property then gives `u=+v` or `u=-v`.

This is exact symmetry amplification: unlike a rational Pythagorean
rotation, it introduces no denominator at the planar embedding.

## 2. The archimedean-window cost

Write the other archimedean embeddings as `tau`, with the usual real/complex
weights.  If `B` has side radii `R_tau`, then every point of `uE` satisfies

\[
  |\tau(ue)|\le 2R_\tau\max_{v\in U}|\tau(v)|.
\]

Standard lattice-point bounds in the full Minkowski embedding therefore give
schematically

\[
  |U|\,|A|(|A|-1)
  \ \ll_K\
  |B|\prod_\tau
  \left(\max_{u\in U}|\tau(u)|\right)^{w_\tau}.    \tag{2.1}
\]

The field-dependent constant can be made uniform in a bounded-root-
discriminant family by using the same box-packing estimates as in
`proof_prime_power.md`.

For multiplicatively independent units `epsilon_1,...,epsilon_r`, take the
subset-product family

\[
  U=\{\epsilon_1^{e_1}\cdots\epsilon_r^{e_r}:
      e_j\in\{0,1\}\}.
\]

After removing a harmless factor for signs, `|U|=2^r`, while

\[
  \prod_\tau\max_{u\in U}|\tau(u)|^{w_\tau}
  \le \prod_{j=1}^r M_K(\epsilon_j),              \tag{2.2}
\]

where

\[
  M_K(\epsilon)=
  \prod_\tau\max(1,|\tau(\epsilon)|)^{w_\tau}
\]

is the Mahler expansion counted with all embeddings of `K`.

Thus (2.1) has a genuine exponential gain whenever

\[
  \sum_{j=1}^r\big(\log2-\log M_K(\epsilon_j)\big)
  \ge \gamma [K:\mathbb Q]                       \tag{2.3}
\]

for some fixed `gamma>0`.  In a tower where `log |B|` is also linear in the
degree, (2.3) converts directly into a fixed power saving from the square-root
bound.

## 3. Why positive unit rank is not the issue

Daileda's rank formula gives, for a number field closed under conjugation,

\[
  \operatorname{rank}V_K+
  \operatorname{rank}(\mathcal O_K^\times\cap\mathbb R)
  =\operatorname{rank}\mathcal O_K^\times.
\]

Consequently non-real, non-CM fields can have many non-torsion unimodular
units.  In suitable Galois families the rank of `V_K` can be proportional to
the degree.  The obstruction is therefore not the supply of abstract exact
rotations.

The load-bearing missing input is **height**.  A basis of `V_K` supplied by
Dirichlet's theorem may have very large regulator.  Formula (2.2) shows that
large Mahler measures consume the entire `2^r` symmetry gain.  Units imported
from a fixed subfield are also ineffective: their Mahler measure is repeated
once for every embedding of `K` over that subfield.

What is needed is a bounded-root-discriminant family `K_j`, together with
linearly many independent `epsilon` in `V_{K_j}`, for which the *average*
full-field log Mahler expansion is strictly below `log 2` (or, more generally,
below the entropy obtained by a better finite exponent set than `{0,1}`).
No theorem or explicit tower supplying this was located.

## 4. Relation to existing dead ends

* In a CM field, the relative norm-one unit group has rank zero, so the usual
  totally-real tower followed by adjoining `i` has only roots of unity.  This
  explains why the existing norm sieve sees only the four Gaussian rotations.
* Allowing `S`-units recovers rational Pythagorean rotations, but clearing
  denominators creates exactly the lattice-window cost that previously killed
  the many-rational-rotations argument.
* A single Salem-type unit supplies infinitely many planar rotations, but its
  powers expand the other embeddings exponentially.  One needs rank linear in
  the field degree, not a single cyclic rotation group.

## 5. Precise research target

Either construct a family satisfying (2.3), or prove a regulator/Mahler
inequality showing that (2.3) is impossible.  A positive construction would
immediately feed into (2.1) and give a new polynomial upper bound for problem
1208; a negative theorem would close a conceptually distinct route and explain
why all known successful constructions must use local congruence branching.

Reference for the rank calculation: Ryan C. Daileda,
“Algebraic Integers on the Unit Circle” (2005),
https://ramanujan.math.trinity.edu/rdaileda/research/papers/p1.pdf .

## 6. An exact relative-regulator obstruction

There is a useful quantitative sharpening of the height bottleneck.  Put

\[
  F=K\cap\mathbb R,
\]

where the real structure is the fixed complex conjugation used at the planar
embedding.  Then (K/F) is quadratic and, modulo torsion, (V_K) is exactly
the relative unit group (E_{K/F}).  Indeed, at the chosen embedding the
relative norm is (u\bar u=|u|^2), so a relative unit has norm one rather
than the other possible real root of unity.

Let

\[
  d=[K:\mathbb Q],\qquad r=\operatorname{rank}V_K,
  \qquad R_{K/F}=\operatorname{Reg}(E_{K/F}).
\]

Akhtari--Vaaler's relative-height inequality says that every full-rank
independent collection \(\epsilon_1,\ldots,\epsilon_r\) in (V_K) satisfies

\[
  R_{K/F}\leq\prod_{j=1}^r d\,h(\epsilon_j).       \tag{6.1}
\]

For a unit, the quantity in each factor is precisely

\[
  d\,h(\epsilon)=\log M_K(\epsilon).
\]

The arithmetic--geometric mean inequality therefore gives the rigorous
lower bound

\[
  \sum_{j=1}^r\log M_K(\epsilon_j)
  \geq r R_{K/F}^{1/r}.                            \tag{6.2}
\]

Consequently a full-rank subset-product construction can have positive
entropy only if

\[
  R_{K/F}^{1/r}<\log 2.                            \tag{6.3}
\]

More strongly, (2.3) requires

\[
  R_{K/F}^{1/r}
  \leq \log2-\frac{\gamma d}{r}.                  \tag{6.4}
\]

This is an unusually sharp numerical target: the relevant threshold is
`log 2 = 0.693...`, not merely an unspecified bounded regulator per degree.

The converse does not follow from the regulator alone.  Akhtari--Vaaler also
construct a basis whose *product* of log heights is at most `r! R_{K/F}`;
that factorial loss and the absence of coordinatewise control do not imply
that the *sum* in (2.3) is small.  If one uses only a positive-rank subfamily
of (V_K), the right invariant is the corresponding collection of
successive minima of the relative logarithmic lattice, not its full
determinant.

Known unconditional lower bounds for relative regulators do not appear to
settle (6.3).  Friedman--Skoruppa give exponential lower bounds for regulator
ratios, but in the quadratic extension (K/F) the published absolute
constants are far too weak to force the normalized relative regulator above
`log 2`.  Thus the unit-rotation lane is narrowed to a concrete arithmetic
question rather than closed:

> Can a bounded-root-discriminant family of non-CM quadratic extensions
> (K/F) have linearly growing relative-unit rank and a positive proportion
> of relative logarithmic successive minima below `log 2`?

Primary references:

* Shabnam Akhtari and Jeffrey D. Vaaler, “Independent relative units of low
  height,” Acta Arith. 202 (2022), 389--401,
  https://arxiv.org/abs/2008.06124 .
* Eduardo Friedman and Nils-Peter Skoruppa, “Relative regulators of number
  fields,” Invent. Math. 135 (1999), 115--144,
  https://doi.org/10.1007/s002220050281 .
