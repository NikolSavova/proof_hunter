# Fixed squared-distance gaps: adaptive tail reduction and sharp high-fibre barrier

## 1. Outcome

Let `D` be the set of the `N=binom(k,2)` distinct squared-distance labels
of a distance-Sidon set, and put

\[
 R_D(r)=\#\{(e,e'): \delta(e)-\delta(e')=r\}.              \tag{1.1}
\]

For one clean fibre `H_q`, let `B_q=delta(H_q)` and `h_q=|H_q|`.  The scalar
energy has the exact difference expansion

\[
 \mathcal M_{q,18}
 =\sum_{r\in\mathbb Z}R_{B_q}(-18r)R_D(r).                 \tag{1.2}
\]

This gives a new adaptive branch which is independent of the determinant
branch:

\[
 \boxed{
 \sum_{0< R_D(r)\le N/h_q}
 R_{B_q}(-18r)R_D(r)\le Nh_q.}                            \tag{1.3}
\]

Thus, in a high fibre, the only remaining scalar collisions use a target
squared-distance gap having more than `N/h_q` representations.

There is an equally exact aggregate form.  Put

\[
 C(r)=\sum_qR_{B_q}(-18r),\qquad
 S_2=\sum_qh_q(h_q-1),qquad
 L_*={Nk^3\over S_2}.                                     \tag{1.4}
\]

When `S_2>0`, all nonzero gaps with `R_D(r)<=L_*` contribute at most
`Nk^3`.  Consequently the aggregate scalar conjecture is reduced to the
weighted popular-gap tail

\[
 \boxed{
 \sum_{r:R_D(r)>L_*} C(r)R_D(r)
 \le m^{o(1)}Nk^3.}                                      \tag{1.5}
\]

This is a genuine narrowing: it asks for anti-correlation between two
specific objects, not a marginal bound for either one.

The tempting marginal conjecture `R_D(r)<=k^(1+o(1))` is both sharp and of
full problem strength.  Such a bound alone would already prove
`k<=m^(2/3+o(1))` by a range count.  Moreover, there are genuine
polynomial-height distance-Sidon families with

\[
 h_q=\Omega(k^2)
 \quad\hbox{and}\quad
 \max_{r\ne0}R_D(r)\ge k^{1-o(1)}.                       \tag{1.6}
\]

Therefore high clean-fibre density does not improve the nearly linear
fixed-gap scale.  It is the weighted overlap `C(r)R_D(r)`, not the maximum
of `R_D`, which remains live.

## 2. Pointwise adaptive fixed-gap branch

Distance-Sidonicity makes both `delta:H_q -> B_q` and the full distance map
injective.  Expanding equality of two scalar charges gives (1.2).  Its
`r=0` term is exactly

\[
 R_{B_q}(0)R_D(0)=h_qN.                                  \tag{2.1}
\]

For the off-diagonal terms,

\[
 \sum_{r\ne0}R_{B_q}(-18r)\le h_q(h_q-1),                \tag{2.2}
\]

because the left side retains only those ordered pairs in `B_q^2` whose
difference is divisible by 18.  Hence, with `L_q=N/h_q`,

\[
\begin{aligned}
 \sum_{0<R_D(r)\le L_q}R_{B_q}(-18r)R_D(r)
 &\le L_q\sum_{r\ne0}R_{B_q}(-18r)\\
 &\le {N\over h_q}h_q(h_q-1)<Nh_q,
\end{aligned}                                             \tag{2.3}
\]

which proves (1.3).  No divisor estimate, endpoint pruning, or unspecified
constant is used.

The surviving pointwise target is now precisely

\[
 \sum_{r:R_D(r)>N/h_q}R_{B_q}(-18r)R_D(r)
 \le m^{o(1)}N(h_q+k).                                   \tag{2.4}
\]

The threshold agrees with the adaptive area threshold in the Gaussian
factorization, but it measures a different phenomenon.  Since fixing both
`r` and the signed doubled area gives only `m^(o(1))` target pairs, a gap
with `R_D(r)>L` must occupy at least `L/m^(o(1))` different signed areas.
Thus the old large-area core and the new popular-gap core are compatible,
not redundant.

## 3. Aggregate layer-cake formulation

Summing (1.2) over `q` gives

\[
 \sum_q(\mathcal M_{q,18}-Nh_q)
 =\sum_{r\ne0}C(r)R_D(r).                               \tag{3.1}
\]

Also

\[
 \sum_{r\ne0}C(r)\le S_2.                              \tag{3.2}
\]

Equations (1.4) and (3.2) immediately pay for the portion with
`R_D(r)<=L_*`.  A useful non-tautological sufficient version of (1.5) is
the following dyadic tail estimate: for every dyadic `lambda>L_*`,

\[
 \boxed{
 \sum_{r:\lambda<R_D(r)\le2\lambda}C(r)
 \le m^{o(1)}{Nk^3\over\lambda}.}                       \tag{3.3}
\]

There are only `O(log m)=m^(o(1))` nonempty levels, so multiplying (3.3)
by `2lambda` and summing proves (1.5).  This is the exact weighted-tail
theorem a future inverse argument has to establish.

Marginal estimates do not substitute for (3.3).  For example, even
`R_D(r)<=k` gives only

\[
 \sum_{r\ne0}C(r)R_D(r)\le kS_2,                         \tag{3.4}
\]

and genuine parabola fibres have `S_2` much larger than `k^4`.  Their
scalar energy stays small because most of this codegree mass lies on gaps
which are absent from the full distance-difference set.

## 4. Why a uniform linear fixed-gap theorem is already #1208

All labels in `D` are different integers in an interval of length at most
`2m^2`.  Therefore

\[
 N(N-1)=\sum_{r\ne0}R_D(r)
 \le 4m^2\max_{r\ne0}R_D(r).                             \tag{4.1}
\]

If `max R_D(r)<=m^(o(1))k`, then, since `N=Theta(k^2)`,

\[
 m^2\ge k^{3-o(1)},\qquad k\le m^{2/3+o(1)}.             \tag{4.2}
\]

Likewise the apparently softer second-moment estimate

\[
 \sum_{r\ne0}R_D(r)^2\le m^{o(1)}kN^2                  \tag{4.3}
\]

already implies (4.2) by Cauchy--Schwarz and the same support bound.  Thus
neither a uniform maximum theorem nor a global unweighted tail theorem is
an intermediate lemma; each would solve the expected exponent directly.

## 5. A sharp genuine high-fibre contamination theorem

**Theorem 5.1.**  There are arbitrarily large integral distance-Sidon sets
of polynomial height satisfying (1.6).

**Proof.**  Let

\[
 \mathcal D_X=\{n\le X:n=x^2+y^2\text{ for integers }x,y\},
 \qquad R=|\mathcal D_X|.                                  \tag{5.1}
\]

Landau--Ramanujan gives `R=X(log X)^(-1/2+o(1))`.  Since

\[
 \sum_{r\ne0}R_{\mathcal D_X}(r)=R(R-1)                  \tag{5.2}
\]

and there are at most `2X` nonzero gaps, some `r_X` obeys

\[
 R_{\mathcal D_X}(r_X)
 \ge {R(R-1)\over2X}=R^{1-o(1)}.                         \tag{5.3}
\]

Take the genuine two-arm distance-Sidon family from
`GAUSSIAN_EDGE_VECTOR_TWO_ARM_BARRIER.md` with arm parameter `R`.  It has
`2R` points, polynomial height, and some clean fibre of size `Omega(R^2)`.
For each \(n\in\mathcal D_X\), choose one integer vector `w_n` of squared norm
`n`.  Adjoin a controlled edge

\[
 \{P_n,\ P_n+S w_n\}.                                      \tag{5.4}
\]

Choose the polynomial integer scale `S` so that the prescribed squared
lengths `S^2n` avoid the old distance spectrum.  The centers `P_n` are free.
Every unintended equality between two squared distances is a nonzero
polynomial of degree at most two in their coordinates.  The only
center-independent equalities compare two prescribed edges or old edges;
these were already separated by the choice of `S` and by distinctness of
the `n`'s.  Hence the product of all forbidden polynomials is nonzero.
The elementary grid nonvanishing lemma supplies integral centers of
polynomial size avoiding their union.

The resulting union is distance-Sidon, and adjoining points cannot destroy
the old clean incidences.  It has

\[
 k=4R,\qquad h_q=\Omega(R^2)=\Omega(k^2).                 \tag{5.5}
\]

Its controlled edge labels satisfy

\[
 R_D(S^2r_X)\ge R_{\mathcal D_X}(r_X)=k^{1-o(1)}.         \tag{5.6}
\]

All input coordinates are polynomial in `R` because `X=R^{1+o(1)}` and
the finite-avoidance grid has polynomially many bounded-degree factors.
This proves the theorem.  \(\square\)

The construction is a contamination barrier, not a scalar counterexample:
it places a popular distance gap beside a quadratic clean fibre, but does
not force the clean-label gap distribution `C` to align with that target
gap.  Precisely this missing alignment is what (3.3) measures.

## 6. Exact stress data

The verifier records the nonzero fixed-gap maxima

\[
\begin{array}{c|rrrrr}
\text{closure size}&20&40&60&80&100\\ \hline
\max_{r\ne0}R_D(r)&35&100&164&215&275
\end{array}                                               \tag{6.1}
\]

and for the transformed parabola at `p=17,31,43,61` the maxima are
`3,6,8,9`.  No tested family exceeds a constant multiple of `k`, but
Section 4 explains why promoting this observation to a theorem is the full
problem.

The joint profiles expose the actual anti-correlation.  On the `p=43`
parabola, the divisible nonzero codegree mass is `2,792,682`; of this,
`2,559,820` lies on gaps with `R_D(r)=0`, and only `29,128` lies on gaps with
`R_D(r)>1`.  The weighted overlap is just `269,490`.  By contrast the
closure-40 stress has no zero-gap escape and weighted overlap `347,362`.

Finally, the verifier builds a 147-point genuine finite union: a 61-point
parabola core with a clean fibre of size 336, plus 43 prescribed
sum-of-two-squares edges.  It checks all 10,731 distances and pair sums.
The controlled nonzero gap has multiplicity 25.

Run

```text
python3 phase2/loop/erdos1208/verify_fixed_distance_gap_weighted_tail.py
```

## 7. Verdict

The fixed-gap idea gives a useful new deletion: target gaps of multiplicity
at most `N/h_q` are harmless pointwise, and gaps below `Nk^3/S_2` are
harmless in aggregate.  What survives is the dyadic weighted tail (3.3).

A nearly linear marginal gap bound is sharp even when `h_q=Omega(k^2)`,
and proving it uniformly would itself settle #1208.  The viable next move is
therefore not to bound `R_D` in isolation, but to prove that popular target
gaps have little clean-fibre codegree mass `C(r)`, using the common
translation and large-area constraints simultaneously.
