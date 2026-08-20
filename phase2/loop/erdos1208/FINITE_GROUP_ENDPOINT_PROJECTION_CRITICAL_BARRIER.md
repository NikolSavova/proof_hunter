# Critical distance-Sidon lifts can have full finite-group shadows

## 1. Outcome

Let

\[
 Q(x,y)=x^2+y^2.
\]

The most direct finite-field attack on the square-grid problem reduces a
distance-Sidon set modulo primes `q == 3 (mod 4)` and then uses the anisotropic
quadratic plane over `F_q`.  This note proves a sharp obstruction to every
version of that attack which only retains the finite-group point multiset and
its endpoint cocycle.

**Theorem 1 (balanced full-shadow lift).**  Let `M>=2` and let `K` be a
multiple of `M^2`.  There is an integer distance-Sidon set

\[
 A\subset[0,m]^2,\qquad |A|\ge {7K\over8},                 \tag{1.1}
\]

such that every residue of `(Z/MZ)^2` occurs under `A -> (Z/MZ)^2` with
exactly the same multiplicity.  One may take

\[
 m=M^2K^{3/2}
 \exp\!\left(O\!\left({\log(MK)\over\log\log(MK)}\right)\right). \tag{1.2}
\]

In particular, if `M=K^{o(1)}`, then

\[
 |A|=m^{2/3-o(1)}.                                      \tag{1.3}
\]

Here distance-Sidon means that the values `Q(a-b)` are distinct as
`{a,b}` ranges over the unordered pairs of distinct points of `A`.

If `M` is a product of primes `q == 3 (mod 4)`, the projection of `A` modulo
every one of those primes is therefore a perfectly balanced copy of the full
anisotropic plane.  Reduction preserves every common-endpoint identity

\[
 (a-b)+(b-c)=a-c.                                      \tag{1.4}
\]

Thus the obstruction does not discard the endpoint cocycle: every finite
triangle, parallelogram, association-scheme relation, and bounded-degree
polynomial relation in the full plane occurs in the shadow of an actual
critical-height distance-Sidon set.

This does **not** rule out a modular proof of the cube-root theorem.  It rules
out a proof whose contradiction is visible in one subpolynomial modulus, or
in the collection of its finite-field shadows considered independently.  A
successful modular proof must retain information coupling the integer lifts
across moduli: actual norm labels, height, carries/quotients, or a comparable
cross-prime invariant.

## 2. The alteration construction

Put `t=K/M^2`.  For each residue `rho in (Z/MZ)^2`, introduce exactly `t`
labelled variables.  Choose every variable independently and uniformly from

\[
 S_\rho=\{x\in[0,m]^2:x\equiv\rho\pmod M\}.              \tag{2.1}
\]

For `m>=2M`, every such set has size at least

\[
 |S_\rho|\ge {m^2\over4M^2}.                              \tag{2.2}
\]

Let

\[
 \Delta(m)=\max_{1\le n\le2m^2}r_2(n),                  \tag{2.3}
\]

where `r_2(n)` is the number of ordered integral representations of `n` as
a sum of two squares.

There are two kinds of bad configurations.

* A duplicate is a pair of labels whose chosen lattice points coincide.
* A metric collision is a pair of distinct unordered label-pairs
  `e != f` for which their squared distances are equal.

For any fixed metric-collision event, one of its labels occurs in exactly one
of `e,f`.  Expose every other variable.  The remaining variable is constrained
to an integral circle of a fixed center and squared radius at most `2m^2`.
That circle contains at most `Delta(m)` lattice points, and hence

\[
 \Pr(e\hbox{ and }f\hbox{ collide})
 \le {4M^2\Delta(m)\over m^2}.                    \tag{2.4}
\]

The same exposure gives duplicate probability at most `4M^2/m^2`.  Since
there are fewer than `K^4/8` unordered pairs of distinct edges and fewer than
`K^2/2` label-pairs, the expected total number `Z` of bad configurations is

\[
 \mathbb EZ
 \le {K^4M^2\Delta(m)\over2m^2}
       +{2K^2M^2\over m^2}.                       \tag{2.5}
\]

Choose `m` so that

\[
 m^2\ge 64M^4K^3\Delta(m).                       \tag{2.6}
\]

For all sufficiently large `K`, (2.5) is then less than `K/(16M^2)`.
Markov's inequality supplies an outcome with

\[
 Z<{K\over8M^2}={t\over8}.                       \tag{2.7}
\]

Remove one participating label from each surviving bad configuration.
At most `Z` labels are removed.  The remaining lattice points are distinct
and distance-Sidon, and every residue class retains at least `t-Z>7t/8`
points.  Finally, delete additional points within the larger residue classes
until all `M^2` classes have the same size.  Deletion preserves
distance-Sidonicity.  The final set has at least

\[
 M^2(t-Z)>7K/8                                      \tag{2.8}
\]

points and has a perfectly balanced full shadow, proving the structural part
of Theorem 1.

## 3. Height bookkeeping

The classical divisor estimate gives

\[
 r_2(n)\le4\tau(n)
 \le \exp\!\left(O\!\left({\log n\over\log\log n}\right)\right). \tag{3.1}
\]

Consequently one may satisfy (2.6) with

\[
 m=M^2K^{3/2}L(MK),\qquad
 L(X)=\exp\!\left(C{\log X\over\log\log X}\right)       \tag{3.2}
\]

for a sufficiently large absolute constant `C`; increasing `m` to the next
integer changes nothing.  This proves (1.2).  If `M=K^{o(1)}`, both `M^2`
and `L(MK)` are `K^{o(1)}`, so `m=K^{3/2+o(1)}`.  Since the alteration loses
only a fixed factor, (1.3) follows.

The factor `M^2` in (1.2) is the cost of demanding that **every** one of the
`M^2` residue cells survive.  It is harmless for any subpolynomial modulus,
which is exactly the range in which a bounded- or slowly-growing-modulus
polynomial method would hope to accumulate only `m^{o(1)}` losses.

## 4. What the finite shadows contain

Suppose now that `q|M` and `q == 3 (mod 4)`.  Since `-1` is not a square in
`F_q`,

\[
 x^2+y^2=0\pmod q\quad\Longrightarrow\quad x=y=0\pmod q. \tag{4.1}
\]

Thus `Q` is anisotropic on `F_q^2`.  Nevertheless Theorem 1 makes the reduced
point multiset exactly `s` copies of all of `F_q^2`, for some `s`.  In
particular:

* the reduced squared-distance matrix still has rank at most four;
* every nonzero difference vector occurs exactly `s^2q^2` times;
* every nonzero norm class contains all `q+1` vectors on its anisotropic
  circle, with the full-plane multiplicity;
* every endpoint-compatible triangle `u+v=w` occurs with full support.

These are precisely the extremal statistics seen by the translation
association scheme and by fixed-degree polynomial/rank tests on the endpoint
labels.  The integer set above is distance-Sidon only because its different
lifts in a residue class have different **integer** norm values.  Reduction
forgets that load-bearing separation.

The barrier remains valid simultaneously for any family of primes whose
product is `K^{o(1)}`: take their product as `M`.  Merely summing a one-prime
Delsarte inequality, even while writing all triangle endpoints explicitly,
therefore cannot force a power saving.  Some term comparing the quotients or
actual norm labels at different primes is indispensable.

## 5. Exact finite certificate

The companion verifier constructs a balanced full-shadow example for
`q=3`, checks all Euclidean squared distances exactly, checks directed-vector
uniqueness and radial uniqueness, and then verifies the complete finite-field
difference and norm-class statistics together with the endpoint cocycle.

Run

```text
python3 phase2/loop/erdos1208/verify_finite_group_endpoint_projection_critical_barrier.py
```

The finite example is only a regression certificate.  The asymptotic theorem
is the alteration argument in Sections 2--3.

## 6. Restart target

The natural surviving modular object is not the reduced point set by itself
but the decorated edge

\[
 \left(a\bmod q,\ b\bmod q,\
 {Q(a-b)-Q(a-b)\bmod q\over q}\right).            \tag{6.1}
\]

For several primes, the quotient decorations are coupled by one integer norm
in `[1,2m^2]`.  A viable polynomial method must exploit that coupling while
keeping the common endpoints in (1.4).  The full-shadow lift proves that
anisotropy, rank four, and endpoint closure without these quotient labels are
insufficient even at the conjectured exponent.
