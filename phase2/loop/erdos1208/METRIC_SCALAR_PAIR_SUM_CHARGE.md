# A metric scalar charge for the clean pair-sum fibre

## 1. Exact reduction

Let `A subset Z^2` be distance-Sidon, let `|A|=k`, and suppose that both
coordinate widths of `A` are at most `m`.  Write

\[
 \Sigma=A\mathbin\oplus A,
 \qquad N=|\Sigma|=\binom k2,
\]

and let `H_q subset Sigma` be the clean start set for a realized directed
difference `q`, as in `DILATED_INTERNAL_PAIR_SUM_CHARGE.md`.  Every
`s in Sigma` has a unique unordered representation `s=a+b`.  Define its
canonical metric label

\[
 \delta(s)=|a-b|^2.                              \tag{1.1}
\]

Distance-Sidonicity makes `delta` injective on `Sigma`.  Fix a positive
integer `C`; the useful numerical choice below is `C=18`.  Consider

\[
 \Phi_{q,C}:H_q\times\Sigma\longrightarrow\mathbb Z,
 \qquad
 \Phi_{q,C}(s,t)=\delta(s)+C\delta(t).           \tag{1.2}
\]

This charge has `hN` records, where `h=|H_q|`, and only `O_C(m^2)` possible
integer values.  If

\[
 B_q=\delta(H_q),\qquad D=\delta(\Sigma),
\]

and `r_(X-X)(z)=|{(x,x') in X^2:x-x'=z}|`, its collision energy is exactly

\[
 \boxed{
 \mathcal M_{q,C}
 =\sum_{r\in\mathbb Z}
   r_{B_q-B_q}(Cr)r_{D-D}(-r).}                 \tag{1.3}
\]

The `r=0` contribution is exactly `hN`, because both metric-label maps are
injective.  Consequently the estimate

\[
 \boxed{\mathcal M_{q,C}\le m^{o(1)}hN}          \tag{1.4}
\]

for every clean fibre would prove

\[
 h\le {m^{2+o(1)}\over k^2}.                   \tag{1.5}
\]

Summing (1.5) over the `k(k-1)` realized directed differences and using the
exact identity

\[
 C_6(A)=4\sum_q |H_q|
\]

gives the ambient equal-centroid bound and hence

\[
 |A|\le m^{2/3+o(1)}.
\]

Thus (1.4) would resolve the square-grid order and Erdős problem 1208.  It
is currently unproved.

### Status after the resonant two-arm test

The construction in `GAUSSIAN_EDGE_VECTOR_TWO_ARM_BARRIER.md` disproves the
adjacent pair-sum and Gaussian vector charges, but it does **not** disprove
this scalar charge.  On its compressed two-arm subsystem, (1.2) becomes

\[
 2a^2+18b^2=2(a^2+9b^2).
\]

For a fixed value this positive-definite binary quadratic form has only
divisor-many integral representations.  Thus the exact resonance that makes
the vector charges polynomially large is near-diagonal for the scalar
charge.  This is evidence, not a proof: an actual counterexample to (1.4)
could use more complicated four-distance additive structure.

For the global problem, the sharp local target can be weakened to

\[
 \boxed{
 \mathcal M_{q,C}
 \le m^{o(1)}N\bigl(|H_q|+k\bigr).}             \tag{1.6}
\]

Indeed, fibres with `|H_q|<=k` contribute at most `O(k^3)` clean starts in
total and need no amplification.  On every remaining fibre, (1.6) is (1.4)
up to a factor two.  This `+k` correction is important when testing small
or deliberately planted clean gadgets.

### Latest proved reductions of the scalar gate

Two later notes now remove substantial parts of the four-label core.
`METRIC_SCALAR_SQUARECLASS_TRANSVERSE_GATE.md` proves that collisions which
stay in one squarefree norm class on each side contribute only
`m^(o(1))hN`; after the three-label cleanup, only four-distinct-edge
squareclass-transverse collisions remain.  This contains every
parallel--parallel collision.

`METRIC_SCALAR_CROSS_EDGE_DETERMINANT_BRANCH.md` then proves that the part
with target doubled area

\[
 |2\det(v,v')|\le\lfloor N/h\rfloor
\]

also contributes only `m^(o(1))hN`.  Hence the unresolved core is
four-edge, squareclass-transverse, and large-area, with the complete
endpoint-difference and clean-fibre constraints retained.  Neither result
proves (1.6), but together they sharply localize what a proof or genuine
counterexample must address.

### Proof of the implication

Equation (1.3) is obtained by expanding equality of two values in (1.2):

\[
 \delta(s)-\delta(s')
   =C\bigl(\delta(t')-\delta(t)\bigr).
\]

Both labels lie in `[1,2m^2]`, so (1.2) has at most
`2(C+1)m^2+1` values.  Cauchy--Schwarz and (1.4) give

\[
 (hN)^2
 \le (2(C+1)m^2+1)m^{o(1)}hN.
\]

Cancel `hN` and use `N asymp k^2` to obtain (1.5).  The standard origin
localization of third additive energy completes the displayed cube-root
deduction.

## 2. Repeated edge labels are already diagonal-scale

Write a collision as four canonical unordered edge labels

\[
 (E_1,F_1;E_2,F_2),
 \qquad E_1,E_2\in H_q,\quad F_1,F_2\in\Sigma,
\]

where the two records have equal charge.  Assume `C!=1`.

**Proposition 2.1.**  Apart from the identical-record diagonal, collisions
using at most three distinct edge labels contribute at most `4h^2`, and
hence at most `4hN`.

If `E_1=E_2`, injectivity of `delta` forces `F_1=F_2`, giving the diagonal;
the same holds if `F_1=F_2`.  If the two records swap their edge labels,
then

\[
 \delta(E_1)+C\delta(F_1)
 =\delta(F_1)+C\delta(E_1)
\]

forces the labels equal because `C!=1`, again giving the diagonal.  Thus an
off-diagonal collision with fewer than four edge labels has exactly three,
and its repeated edge is one of

\[
 E_1=F_1,\quad E_2=F_2,\quad
 E_1=F_2,\quad E_2=F_1.                         \tag{2.1}
\]

For each case, choose the ordered pair `(E_1,E_2)` in at most `h^2` ways.
The charge equation determines the metric label of the remaining edge, and
global distance uniqueness supplies at most one such edge.  Summing the
four cases proves the proposition.

Consequently the scalar theorem has no repeated-distance-label obstruction:
after an `O(hN)` term, all four edge distances in a collision are distinct.
Endpoint labels may still overlap between these four edges, and the
eight-distinct endpoint pattern dominates the finite closure data.

## 3. Why this retains information missing from the vector charge

The earlier charge `s+3(I+J)t` sees the endpoint sums but not their
Euclidean separation.  In contrast, (1.1) is precisely the globally unique
squared-distance label of the canonical edge represented by `s`.  The
finite-field parabola therefore does not automatically transfer as a
counterexample: an integral affine map which separates its Euclidean
distances also changes every label in (1.2).

The coefficient `18` is the norm multiplier of `3(I+J)`, but the reduction
works for every fixed positive integer `C`.  Larger fixed coefficients look
slightly more injective in finite data, but no asymptotic claim follows from
that observation.

## 4. A rigorous collinear branch

**Proposition 4.1.**  Estimate (1.4) holds when `A` is collinear.

After translation, write the points as `r v`, where `v` is a fixed primitive
integral vector and the integers `r` form a Golomb ruler.  Every metric label
is

\[
 \delta=|v|^2 d^2,
\]

where the positive ruler differences `d` are all distinct.  A fibre of
(1.2) is therefore contained in the set of positive integer solutions of

\[
 x^2+C y^2=n.                                    \tag{4.1}
\]

For fixed `C`, the representation number of the positive-definite binary
quadratic form in (3.1) is `n^{o(1)}`.  This follows, for example, from the
standard ideal-divisor bound in the fixed quadratic order of discriminant
`-4C`; the finitely many imprimitive factors only change the constant.
Since `n=O_C(m^2)`, every load of (1.2) is `m^{o(1)}`.  Hence its second
moment is at most `m^{o(1)}hN`, proving the proposition.

This branch is already covered by the stronger projection theorem, but it
is useful evidence that the scalar charge interacts correctly with the
classical Golomb-ruler obstruction.

## 5. A scalable exact stress: the integer parabola

The family

\[
 P_r=\{(j,j^2):0\le j<r\}                       \tag{5.1}
\]

is itself distance-Sidon.  Indeed, for `i>j` put

\[
 u=i-j,\qquad v=i+j.
\]

The squared distance is

\[
 d=u^2(1+v^2)=(uv)^2+u^2.                      \tag{5.2}
\]

Because `1<=u<=v`,

\[
 (uv)^2<d<(uv+1)^2.
\]

Thus `floor(sqrt(d))=uv`, after which (4.2) recovers
`u^2=d-(uv)^2`, then `u,v`, and finally the unordered pair `{i,j}`.

The exact verifier constructs the largest clean fibre for (4.1).  At
`r=10,15,20,25,30,40,50`, the normalized scalar-charge energies for `C=18`
are respectively

\[
 1, 1.00816\ldots, 1.00827\ldots, 1.01394\ldots,
 1.01275\ldots, 1.01144\ldots, 1.01199\ldots .
\]

The maximum loads are at most three.  This is a scalable falsification test,
not a proof of (1.4); the parabola lies in a box of side `Theta(r^2)` and is
well below the cube-root-critical density.

## 6. Exact finite profiles

For the largest clean fibre of each stored family, the verifier reports

\[
 (k,m,q,h,N,hN,|\operatorname{im}\Phi|,
   \mathcal M_{q,18},\max\Phi^{-1}).
\]

\[
\begin{array}{c|r|r|r|r}
\text{family}&hN&|\operatorname{im}\Phi|&\mathcal M_{q,18}&\max\Phi^{-1}\\ \hline
\text{closure }30&6090&5964&6342&2\\
\text{closure }40&17940&16732&20592&4\\
\text{closure }80&199080&188394&221584&4\\
\text{closure }120&906780&851608&1023788&6\\
\text{source }45&21780&21364&22612&2\\
\text{perpendicular ruler }40&10920&10911&10938&2\\
\text{Costas }22&7854&7601&8382&3\\
\text{parabola image }43&154413&153065&157133&3
\end{array}
\]

The largest normalized energy in the table is `1.147826...` on closure 40;
closure 120 is `1.129036...`.  These profiles are substantially less rigid
than the vector charge but remain at constant scale on every present stress.

The verifier also separates the off-diagonal patterns.  On closures
`30,40,80,120`, the numbers with exactly three distinct edge labels are
`0,4,30,70`, while the numbers whose four edges have eight distinct
endpoints are `70,1276,15930,91308`.  In particular, `91308` of the
`117008` off-diagonal closure-120 collisions already lie in the fully
eight-endpoint core.  Proposition 2.1 removes the repeated-edge cases, but
ordinary endpoint-overlap cleanup cannot by itself close the scalar gate.

Run

```text
python3 phase2/loop/erdos1208/verify_metric_scalar_pair_sum_charge.py
```

## 7. Exact remaining theorem

The live target is the weaker sharp form (1.6), or just its aggregate
consequence

\[
 \sum_q|H_q|\le m^{o(1)}(k^2+m^2).
\]

One cannot replace `B_q` by the whole squared-distance set and appeal only
to additive energy: the closure profiles have much larger global distance
energy, while the restricted clean fibres remain nearly diagonal.  A proof
must use simultaneously that

1. `B_q` consists of source-edge labels in one clean pair-sum translate;
2. every label in `D` has one endpoint edge; and
3. all labels are norms of integral planar differences.

The next inverse step is to show that polynomial cross-additive energy
between `B_q` and `C D` forces two distinct endpoint differences to have the
same norm.  That conclusion is forbidden by distance-Sidonicity.
