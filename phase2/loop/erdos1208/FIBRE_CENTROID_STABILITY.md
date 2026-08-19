# Centroid stability of almost-full rotated-difference fibres

## 1. Exact identity

Let `A subset Z^2` be distance-Sidon, `|A|=k`, and let

\[
 \mathcal F_x=
 \{(p,r,q)\in A^3:r\ne q,\ x=p+J(r-q)\}
\]

be a nonzero fibre of size `h`.  Its three coordinate projections are
sets `P,R,Q subset A`, each of cardinality `h`.  Put

\[
 \Sigma=\sum_{a\in A}a,
 \qquad
 P^c=A\setminus P,
 \quad R^c=A\setminus R,
 \quad Q^c=A\setminus Q.
\]

Summing the defining equation over the fibre gives the exact identity

\[
 \boxed{
 h x=\Sigma-\sum_{p\in P^c}p
       +J\left(\sum_{q\in Q^c}q-
                \sum_{r\in R^c}r\right).}       \tag{1.1}
\]

Let `mu=Sigma/k` and put `t=k-h`.  Subtracting `h mu` yields the centered
form

\[
 \boxed{
 h(x-\mu)=
 -\sum_{p\in P^c}(p-\mu)
 +J\left(
    \sum_{q\in Q^c}(q-\mu)-
    \sum_{r\in R^c}(r-\mu)
 \right).}                                      \tag{1.2}
\]

Thus the output of an almost-full fibre is controlled entirely by the
three small coordinate complements.

## 2. Quantitative lattice consequence

Assume that `A` lies in an axis-parallel square of side `m`.  Then every
point of `A` is within distance `sqrt(2)m` of its centroid.  Equation (1.2)
therefore gives

\[
 \boxed{
 |x-\mu|\le {3\sqrt2\,m t\over k-t}.}            \tag{2.1}
\]

Let `N_t` be the number of integer outputs whose fibre size is at least
`k-t`.  All of them lie in the disk from (2.1), and hence in a square of
the same radius.  Consequently

\[
 \boxed{
 N_t\le
 \left({6\sqrt2\,m t\over k-t}+2\right)^2.}      \tag{2.2}
\]

In particular, a full fibre has

\[
 x=\mu,                                          \tag{2.3}
\]

so there is at most one full output, and it exists only if the centroid is
an integer point.

This is exactly the kind of constraint absent from the finite-field models
in `AFFINE_DOUBLE_ENDPOINT_ORIENTATION_BARRIER.md` and
`THREE_PROJECTION_FIBRE_BARRIER.md`: those models support quadratically many
full or almost-full fibres, whereas all real almost-full outputs are forced
into one small centroid neighborhood.

## 3. Scope

The lemma is a genuine characteristic-zero stability estimate, but it does
not by itself prove cubic support.  At the critical scale `k about m^(2/3)`,
it becomes restrictive only when `t` is substantially below `sqrt(k)`.
The closure stresses have maximum fibre only `O(sqrt(k))`, far from this
almost-full regime.  A completion of the proof therefore needs either

1. a multiscale extension of (1.1) to medium-rich fibres; or
2. a density increment showing that a counterexample at medium scale
   creates an almost-full fibre in a smaller characteristic-zero model.

The identity rules out the extreme affine-plane tail exactly and supplies
the correct localization target for such an increment.

## 4. Verification

`verify_fibre_centroid_stability.py` constructs every nonzero fibre of the
stored integral 20-point closure set.  It checks coordinate matching,
(1.1), the centered integer form of (1.2), and the lattice count (2.2) for
every threshold `0<=t<k`.
