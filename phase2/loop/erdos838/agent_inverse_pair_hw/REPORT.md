# Inverse-pair, graded-ratio, and antimatroid-Tutte audit for HW2

**Date:** 2026-08-14  
**Verdict:** the type-A reflection-order inequalities remain open, but the
algebraic boundary is now exact.  Coefficientwise positivity and
`A(z)=B(-z)^{-1}` do not imply HW2.  They still do not imply the proposed
rank-extension inequality after imposing the correct complete first-order
type-A datum `A_1=B_1=sum_(i<j) E_(j,i)`.  Complete root support in a genuine
reflection order is also insufficient if the root weights are allowed to
vary.  Thus unit normalization and the actual reflection-factorization data
are load-bearing, not cosmetic.

The new graded target

\[
 p_r=\frac{(r+1)v_{r+1}}{(n-r)v_r}\ge 2^{-r-o(r)}              \tag{GR}
\]

survives every tested unit reflection order in its relevant range and has the
right exponent on balanced Pascal towers.  The antimatroid identity

\[
 Z(s)=f(s,s^{-1}-1)                                             \tag{AT}
\]

is exact, but a naive deletion-contraction induction is impossible: an actual
nine-point planar configuration has hull-vertex deletion minors with
`H=56/27>2`.

## 1. Matrix normalization and path meaning

For a listed positive root `(i,j)`, `i<j`, let

\[
 T_{ij}(z)=I+zE_{j,i}.
\]

In the row-update convention, processing roots in the order `R` forms

\[
 B_R(z)=\prod_R T_{ij}(z),\qquad
 A_R(z)=\prod_{R^{\rm rev}}T_{ij}(z)=B_R(-z)^{-1}.              \tag{1}
\]

Every entry of both matrices has nonnegative coefficients.  The partition
polynomial including the empty set is

\[
 F_R(z)=1+nz+\langle A_R(z),B_R(z)\rangle_F-n.                 \tag{2}
\]

An entry of `B` counts vertex-increasing paths whose edge times increase in
`R`; the corresponding entry of `A` counts those whose edge times decrease.
The Frobenius product pairs two such paths with common endpoints.

If every positive root occurs once with unit weight, in **any** order, then

\[
 [z^2]F_R={n\choose2},\qquad [z^3]F_R={n\choose3}.              \tag{3}
\]

Indeed, degree two pairs the same direct edge in `A` and `B`.  For each triple
`i<j<k`, exactly one of the two-edge path `(i,j),(j,k)` and its reversal is
time-monotone; pairing it with the direct `(i,k)` edge contributes exactly one
degree-three object.

The reflection-order betweenness axiom is

\[
 (ij)<(ik)<(jk)\quad\hbox{or}\quad(jk)<(ik)<(ij)               \tag{4}
\]

for every `i<j<k`.  It is what turns the path pairs into a squarefree convex
subset system.  Without (4), degree can exceed `n`: the unit order

```text
01,12,24,34,23,02,03,04,13,14
```

has

\[
 F(z)=1+5z+10z^2+10z^3+7z^4+4z^5+z^6.                        \tag{5}
\]

Thus an arbitrary root order is not merely a nonstretchable point order; it
can lose the convex-set interpretation altogether.

## 2. Exact hierarchy of inverse-pair counterexamples

Write `H=nF(1/2)/F(1)`.  The following are exact.

### 2.1 Bare positive inverse pairs

Take `A=B=I`.  Then

\[
 F(z)=1+nz,\qquad H=\frac{n(n+2)}{2(n+1)}>2\quad(n\ge4).        \tag{6}
\]

This already has determinant one and coefficientwise-positive inverse
matrices.

### 2.2 Distinct unit type-A root factors

Use the `n-1` star roots `(0,j)`, each once with unit weight.  Their products
vanish pairwise, so

\[
 F(z)=1+nz+(n-1)z^2,qquad H=\frac{3(n+1)}8.                    \tag{7}
\]

Hence HW2 fails for every `n>=5`.  Root completeness is necessary.

### 2.3 Every root, in a genuine reflection order, with positive weights

At `n=5`, take the lexicographic reflection order and put weight one on
`(0,j)` and weight `epsilon` on the other six roots.  Direct multiplication
gives

\[
\begin{aligned}
F_\epsilon(z)={}&1+5z+(4+6\epsilon^2)z^2
 +(6\epsilon+4\epsilon^3)z^3\\
&+(4\epsilon^2+\epsilon^4)z^4+\epsilon^3z^5.                 \tag{8}
\end{aligned}
\]

For `epsilon=1/5`,

\[
 F=(1,5,106/25,154/125,101/625,1/125),
 \qquad H=\frac{472435}{232832}>2.                             \tag{9}
\]

More explicitly,

\[
 5F(1/2)-2F(1)=\frac{6771}{20000}>0.                           \tag{10}
\]

All ten positive roots occur with weights in `[1/5,1]`, and the order obeys
(4).  Unit normalization is therefore essential even after completeness and
reflection betweenness are imposed.

### 2.4 Even the correct complete linear term does not imply (GR)

Let `S` be the strictly lower-triangular all-ones `6x6` matrix.  There are
nonnegative integer matrices `A_2,B_2,A_3` such that

\[
 A=I+zS+z^2A_2+z^3A_3,\qquad B=I+zS+z^2B_2,
 \qquad B(-z)A=AB(-z)=I,                                     \tag{11}
\]

but

\[
 F(z)=1+6z+15z^2+20z^3+z^4.                                  \tag{12}
\]

In zero-based matrix coordinates, the nonzero entries are

```text
A2: (3,1)=1, (4,0)=3, (4,1)=2, (4,2)=1, (5,1)=3
B2: (2,0)=1, (3,0)=2, (5,0)=4, (5,2)=2, (5,3)=1
A3: (4,1)=1.
```

The checker multiplies both sides of (11) as polynomial matrices.  This pair
has the exact complete type-A first coefficient and consequently the correct
`v_2=15,v_3=20`, but

\[
 p_3=\frac{4v_4}{3v_3}=\frac1{15}<\frac18.                    \tag{13}
\]

It need not admit a once-per-root transvection factorization.  That is exactly
the point: inverse coefficient identities, even with their correct linear
boundary condition, do not contain the required rank-extension theorem.

## 3. What remains live for unit root factorizations

The broad class in which every positive root occurs exactly once with unit
weight, but in an arbitrary order, has not produced an HW2 counterexample.

* All `10! = 3,628,800` arbitrary orders at `n=5` were exhausted.  The maximum
  was `H=65/48`, attained for example by

  ```text
  01,02,03,04,14,23,24,12,34,13,
  ```

  with profile `(1,5,10,10,1)`.  This order violates (4) on triples `123`,
  `124`, and `134`.
* Arbitrary-transposition annealing seeded from the best reflection records
  found no improvement at `n=20,24,30`; the seed values remained
  `1.5975068,1.6909900,1.7349749`.

This is evidence, not a theorem.  In particular, reflection betweenness is
provably necessary for the geometric interpretation, but it is not known to
be necessary for the scalar inequality itself.

The axiom boundary is therefore:

| Class | Status |
|---|---|
| positive inverse pair | false, (6) |
| distinct unit root factors, incomplete support | false, (7) |
| all roots, reflection order, arbitrary positive weights | false, (9) |
| positive inverse pair with `A_1=B_1=S` | exact (GR) bound false, (13) |
| every root once, unit weight, arbitrary order | HW2 open; tests pass |
| every root once, unit weight, reflection order | original HW2/(GR), open |

## 4. The normalized graded target

Put

\[
 a_r=\frac{v_r}{\binom nr}.
\]

Then the proposed ratio is simply

\[
 p_r=\frac{a_{r+1}}{a_r}.                                     \tag{14}
\]

Thus (GR), multiplied from the universal `a_3=1`, gives

\[
 \log_2a_k\ge-\frac12k^2+o(k^2),                              \tag{15}
\]

which is the desired coefficient-one-half lower mechanism.

### Exact finite data

A complete commutation-class scan through `n=6` gives the following smallest
`p_3` values: `0,1/5,1/5` at `n=4,5,6`.  The zero occurs only where
`r=3>log_2n` and a convex quadrilateral need not exist.  At `n=5,6`,
`2^3p_3=8/5`.

For the saved exact adversarial unit reflection orders, all ranks
`3<=r<=floor(log_2 n)` have:

| `n` | `r` | exact `p_r` | `2^r p_r` | `-log_2(p_r)/r` |
|---:|---:|---:|---:|---:|
| 20 | 3 | `2401/4845` | 3.9645 | 0.337620 |
| 20 | 4 | `4265/38416` | 1.77634 | 0.792772 |
| 24 | 3 | `894/1771` | 4.03840 | 0.328739 |
| 24 | 4 | `291/2384` | 1.95302 | 0.758573 |
| 30 | 3 | `13973/27405` | 4.07896 | 0.323932 |
| 30 | 4 | `2005/13973` | 2.29586 | 0.700242 |

There is no finite counterevidence here; the relevant ratios have constant
slack over `2^{-r}`.

### Balanced towers are asymptotically sharp

For a fixed vertical template of size `R`, let `P=p+q` be the sum of its cap
and cup capacities and `L=log_2R`.  The fixed-template saddle calculation at
depth `d` and rank `k=Theta(d)` gives

\[
 \log_2 v_k=Ldk-\frac{L}{2P}k^2+O_R(d),                        \tag{16}
\]

while

\[
 \log_2\binom{R^d}{k}=Ldk-k\log_2k+O(k).                      \tag{17}

At the local-ratio level this predicts

\[
 p_k=2^{-(L/P)k+O_R(\log k)}.                                 \tag{18}

For central Pascal templates, `L/P -> 1`, so the exponent in (GR) is sharp.
Exact tower computations at `r=floor(log_2 n)` give exponents

```text
h=6:  0.608416
h=10: 0.742267
h=16: 0.807332,
```

moving toward one as the balanced template grows.  Equation (18) is the
local saddle prediction; a publishable proof should establish the adjacent
coefficient ratio directly rather than subtract the `O(d)` errors in (16).

## 5. Why Newton and ordinary total positivity do not close (GR)

The valid `n=5` reflection profile

\[
 1+5z+10z^2+10z^3+z^4                                      \tag{19}
\]

is not real-rooted.  Indeed, Newton's necessary log-concavity after
normalizing by the degree-four binomial coefficients already fails at rank
one:

\[
 (5/4)^2=25/16<10/6.                                        \tag{20}
\]

So real-rootedness, stability, and the standard Newton inequalities are not
available.  Even if normalized log-concavity held in a restricted range, it
would upper-bound later `p_r`; (GR) needs lower bounds.

Nor are the endpoint matrices totally nonnegative.  For the valid
lexicographic `A_2` reflection order `01,02,12`,

\[
 B(1)=\begin{pmatrix}1&0&0\\1&1&0\\2&1&1\end{pmatrix},
\]

whose minor on rows `(1,2)` and columns `(0,1)` is `-1`.  Any successful
canonical-basis or positivity argument must therefore use a subtler object
than ordinary total positivity of `A` or `B`.

## 6. Exact antimatroid-Tutte formulation

Let `G` be the shelling antimatroid dual to a finite convex geometry.  Its
feasible sets are complements of closed sets.  If `F=E-C`, then a continuation
of `F` is exactly an extreme point of `C`:

\[
 \Gamma(F)=\operatorname{ext}(C).                             \tag{21}
\]

Define the shifted greedoid Tutte polynomial by its antimatroid feasible-set
expansion

\[
 f_G(t,z)=\sum_{F\text{ feasible}}
 t^{n-|F|}(z+1)^{n-|F|-|\Gamma(F)|}.                          \tag{22}

Equivalently, summing over closed `C`,

\[
 f_G(t,z)=\sum_C t^{|C|}(z+1)^{|\operatorname{int}(C)|}.       \tag{23}

Every convexly independent set `A` is the extreme set of the unique closed
set `cl(A)`.  Therefore

\[
 \boxed{Z_G(s)=\sum_Cs^{|\operatorname{ext}(C)|}
       =f_G(s,s^{-1}-1).}                                     \tag{24}

In particular,

\[
 \boxed{\text{HW2}\iff n f_G(1/2,1)\le2 f_G(1,0).}            \tag{25}

For a planar point configuration, (24) is exactly the same polynomial as the
matrix expression (2): both enumerate the convex subset `ext(C)`.  The same
identification holds for the generalized rank-three convex geometry attached
to a valid type-A reflection order.  It fails for arbitrary root orders such
as (5), which have no squarefree convex interpretation.

The ordinary corank-nullity expansion also gives

\[
 f_G(1/2,1)=\sum_{X\subseteq E}2^{-(n-r_G(X))},\qquad
 f_G(1,0)=|\mathcal F|.                                       \tag{26}

This is a clean expected-rank formulation, but it does not by itself add a
planar inequality.

## 7. Deletion-contraction: exact recurrence and exact obstruction

For an atomistic point convexity and a hull point `e`, the singleton `{e}` is
feasible and both greedoid minors have ground size and rank `n-1`.  The
standard recurrence becomes

\[
 f_G(t,z)=f_{G/e}(t,z)+t f_{G-e}(t,z).                         \tag{27}

On the curve (24),

\[
 Z_G(s)=Z_{G/e}(s)+sZ_{G-e}(s).                               \tag{28}

Here `G/e` is the ordinary point-deletion convex geometry on `P-e`, while
`G-e` is a rooted/relative convexity: its closed sets are the original closed
sets containing `e`, with `e` removed.

If both minors satisfied HW2 and

\[
 D=f_{G-e}(1,0),\qquad C=f_{G/e}(1,0),
\]

then (28) would induct provided

\[
 C\le\left(\frac n2-1\right)D.                               \tag{29}

But the premise is false even for a planar parent.  The exact nine-point
integer configuration in `agent_lex_minimizer_search` has parent profile

\[
 (1,9,36,84,36,3),\qquad H=7875/5408<2.                       \tag{30}

For **each** of its three hull vertices, the greedoid deletion minor has

\[
 (1,8,28,15,2),\qquad H=\frac{56}{27}>2,                      \tag{31}

whereas the contraction/point-deletion minor has

\[
 (1,8,28,56,21,1),\qquad H=\frac{651}{460}.                   \tag{32}

The verifier reconstructs every closed set directly from the integer
coordinates and checks (24), `f(1,1)=2^n`, and (28) at three rational
specializations.  Thus HW2 is not minor-closed even along minors of actual
planar shelling antimatroids.

Universal antimatroid identities cannot fix this.  The simple
Caratheodory-three convex geometry already recorded in
`agent_root_followup/ABSTRACT_LATTICE_BARRIER.md` has

\[
 Z(z)=1+nz+\binom n2z^2+\binom n3z^3,                         \tag{33}

so it violates HW2 and has `p_3=0`.  It satisfies all general antimatroid
Tutte relations.  Planar rank-three/oriented-matroid input is indispensable.

The viable remnant of this route is a **bivariate amortized induction** which
keeps the closed-set size/interior variable through rooted minors.  A scalar
induction on (25), or any argument using only universal Tutte identities,
cannot work.

## 8. Recommended next proof target

The best surviving matrix/antimatroid statement is still (GR), but it must be
proved from unit reflection factorization or rank-three oriented-matroid
elimination—not from inverse positivity.  Three equivalent readings are:

1. `p_r=a_(r+1)/a_r` for normalized convex-set densities;
2. `p_r` is the mean fraction of missing points which extend a uniform convex
   `r`-set;
3. in the matrix model it is the adjacent-degree growth of common-endpoint
   increasing/decreasing temporal path pairs.

Balanced towers say the exponent one is sharp.  The concrete missing lemma is
a rank-three extension theorem of the form

\[
 \mathbb E_{|A|=r,\ A\text{ convex}}u(A)
 \ge(n-r)2^{-(1+o(1))r},\qquad r\le(1-o(1))\log_2n.            \tag{34}

The exact barriers above specify what (34) must use: unit once-per-root
factorization, reflection betweenness, and history/endpoint alignment.

## 9. Reproduction

From the repository root:

```bash
python3 phase2/loop/erdos838/agent_inverse_pair_hw/verify_inverse_pair_barrier.py
python3 phase2/loop/erdos838/agent_inverse_pair_hw/verify_antimatroid_bridge.py
python3 phase2/loop/erdos838/agent_inverse_pair_hw/graded_ratio_audit.py
python3 phase2/loop/erdos838/agent_inverse_pair_hw/graded_ratio_audit.py --exhaustive-small

c++ -O3 -std=c++17 \
  phase2/loop/erdos838/agent_inverse_pair_hw/arbitrary_root_order.cpp \
  -o /tmp/arbitrary_root_order
/tmp/arbitrary_root_order 5 exhaustive
```

All claimed counterexamples and finite profiles are checked with exact integer
or rational arithmetic.  The C++ arbitrary-order annealer is exploratory; its
saved winners are replayed exactly by the Python verifier.

## Sources for the antimatroid formulas

* G. Gordon and E. McMahon, “A greedoid polynomial,” *Proc. AMS* 107 (1989),
  287–298.  This gives the corank-nullity polynomial and greedoid
  deletion-contraction recurrence.
* G. Gordon, “Linear relations for a generalized Tutte polynomial,” *EJC* 22
  (2015), P1.79, especially Theorem 4.1 for the closed-set/interior expansion
  of an antimatroid Tutte polynomial.

