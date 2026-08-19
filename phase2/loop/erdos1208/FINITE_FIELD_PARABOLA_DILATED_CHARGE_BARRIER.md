# The finite-field parabola kills a metric-free dilated charge theorem

## 1. Outcome

The dilated internal pair-sum estimate is a genuinely Euclidean statement.
It cannot be proved from vector-Sidonicity, unique pair sums, or the clean
six-endpoint condition alone.

For every odd prime `p`, put

\[
 A_p=\{(x,x^2\bmod p):0\le x<p\}\subset\{0,\ldots,p-1\}^2. \tag{1.1}
\]

Regard the residues in the second coordinate as their standard integer
representatives.  Then `A_p` is vector-Sidon over the integers.  Let
`Sigma_p=A_p oplus A_p`, let `H_q` be the clean internal-shift set, and put

\[
 \Lambda=3(I+J),\qquad
 \Psi_q(s,t)=s+\Lambda t.
\]

**Theorem 1.1.**  For all sufficiently large odd primes, some realized
difference `q` satisfies

\[
 |H_q|\gg p^2                                      \tag{1.2}
\]

and

\[
 \boxed{
 {\sum_z|\Psi_q^{-1}(z)|^2\over
      |H_q|\binom p2}\gg p^2.}                    \tag{1.3}
\]

Thus the desired near-diagonal energy bound fails by a fixed power even
though every nonzero vector difference and every unordered pair sum has a
unique endpoint representation.

The sets `A_p` are not Euclidean distance-Sidon: different difference
vectors can have the same squared norm.  This is the precise missing input.
Any proof of the live charge estimate must use radial uniqueness in an
essential way; a Freiman model, ordinary design rank, or pair-sum endpoint
decoration that remembers only vector addition cannot suffice.

## 2. Vector-Sidonicity

Suppose two nonzero ordered differences in `A_p` agree as integer vectors.
They then agree modulo `p`.  Writing the first coordinates as `x-y=h`, the
second-coordinate difference satisfies

\[
 x^2-y^2=h(x+y)\pmod p.                          \tag{2.1}
\]

Since `h` is nonzero, the two coordinates of the difference recover both
`x-y` and `x+y` modulo `p`, and hence recover the ordered pair `(x,y)`.
The standard representatives are unique, so the original ordered pairs
are equal.  Therefore `A_p` is vector-Sidon.  In particular,

\[
 |\Sigma_p|=\binom p2.                           \tag{2.2}
\]

The same argument allows repeated summands: every two-element multiset in
`A_p` has a unique sum.

## 3. Quadratically large clean fibres

There are `p^3` ordered triples from `A_p`.  Their integer coordinate sums
lie in a box with fewer than `9p^2` points.  If `r(u)` is the ordered
triple-sum representation function, Cauchy--Schwarz gives

\[
 \sum_u r(u)^2\ge {p^6\over9p^2}={p^4\over9}.   \tag{3.1}
\]

Only `O(p^3)` of this energy comes from repeated labels or from two
orderings of the same three-element multiset.  Here is a self-contained
reason.  If two distinct triple multisets of a Sidon set have the same sum
and share an element, cancel that element.  Uniqueness of two-element
multiset sums then makes the triples equal, a contradiction.  Hence the
supports of distinct representations of one triple sum are disjoint, and
there are only `O(p)` ordered representations of any fixed sum.  There are
`O(p^2)` ordered triples with a repeated label, so all energy involving one
is `O(p^3)`; the reorderings of identical multisets also contribute only
`O(p^3)`.

It follows that there are `Omega(p^4)` ordered pairs of disjoint
three-element sets with the same sum.  Given such a pair `T,U`, choose
`a in T` and `b in U`, and put

\[
 q=a-b,\qquad s=\sum_{x\in T\setminus\{a\}}x.
\]

The common-sum identity gives

\[
 s+q=\sum_{y\in U\setminus\{b\}}y,              \tag{3.2}
\]

so `s in H_q`.  Vector-Sidonicity and pair-sum uniqueness recover all six
endpoints from `(q,s)`, so this map has only an absolute ordering
multiplicity.  Consequently

\[
 \sum_{q\in(A_p-A_p)^*}|H_q|\gg p^4.            \tag{3.3}
\]

There are `p(p-1)` realized directed differences, and (1.2) follows.

## 4. The forced charge energy

Fix the `q` from (1.2) and put `N=binom(p,2)`, `h=|H_q|`.  The charge has
`Nh=Omega(p^4)` records.  Both `s` and `t` have coordinates between zero
and `2p-2`; therefore `s+Lambda t` lies in an axis-parallel box with
`O(p^2)` integer points.  Cauchy--Schwarz gives

\[
 \sum_z|\Psi_q^{-1}(z)|^2
 \gg {N^2h^2\over p^2}.                         \tag{4.1}
\]

Dividing by `Nh` and using `N,h=Omega(p^2)` proves (1.3).

This is an asymptotic obstruction to a metric-free proof, not a
counterexample to the live Euclidean estimate.  An integral affine
transformation can separate all Euclidean distances of a fixed `A_p`, but
the required anisotropy conjugates the quarter-turn dilation into a thin
high-index resonance lattice.  That is why the transformed parabola stress
has nearly diagonal charge energy while (1.1) does not.

## 5. Exact finite calibration

The companion verifier checks vector-Sidonicity, pair-sum uniqueness,
Euclidean distance collisions, the largest clean fibre, and the complete
charge profile for `p=17,31,43,61`.  The normalized energies are

\[
 1.23109\ldots,quad2.07416\ldots,quad
 3.04065\ldots,quad4.76184\ldots,               \tag{5.1}
\]

respectively.  These small cases are far below the asymptotic lower bound's
eventual scale because the explicit charge box has a large absolute
constant.  They are regression data, not the proof of Theorem 1.1.

Run

```text
python3 phase2/loop/erdos1208/verify_finite_field_parabola_dilated_charge_barrier.py
```

## 6. Restart target

The surviving theorem must convert a polynomial excess in the dilated
charge into two *different* endpoint differences of equal Euclidean norm.
The present barrier shows why this cannot be done collision by collision:
the additive parabola has abundant clean charge collisions.  The conversion
must be a supersaturation statement in which many compatible charge
collisions force a norm collision.  For an actual distance-Sidon set that
norm-collision count is zero.
