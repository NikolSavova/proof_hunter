# The projection-sparse branch of the dilated pair-sum gate

## 1. Outcome

Let `A subset R^2` be distance-Sidon, let

\[
 \Sigma=A\mathbin{\oplus}A,
 \qquad N=|\Sigma|=\binom{|A|}{2},
\]

and, for a realized difference `q`, let `H_q subset Sigma` be the clean
internal-shift set from `DILATED_INTERNAL_PAIR_SUM_CHARGE.md`.  Put

\[
 J(x,y)=(-y,x),\qquad \Lambda=3(I+J).
\]

For a nonzero real linear functional `pi`, write

\[
 R_\pi=|\pi(\Sigma)|.
\]

The following closes every projection-sparse branch of the live resonance
estimate.

**Theorem 1.1.**  For every `q`, the charge

\[
 \Psi_q(s,t)=s+\Lambda t,
 \qquad (s,t)\in H_q\times\Sigma,
\]

satisfies

\[
 \boxed{
 \sum_z |\Psi_q^{-1}(z)|^2
 \le R_\pi^2\,N|H_q|.}                         \tag{1.1}
\]

Consequently the off-diagonal resonance sum obeys

\[
 \sum_{w\ne0}r_{\Sigma-\Sigma}(w)
       r_{H_q-H_q}(-\Lambda w)
 \le (R_\pi^2-1)N|H_q|.                        \tag{1.2}
\]

In particular, if some projection of `Sigma` has `k^(o(1))` values, where
`k=|A|`, then the missing estimate in the dilated charge note holds and the
cube-root conclusion follows.

If `A` is covered by `r` parallel affine lines, choose `pi` constant on
those lines.  Then

\[
 R_\pi\le |\pi(A)+\pi(A)|\le {r(r+1)\over2},   \tag{1.3}
\]

so (1.1) has loss at most `r^2(r+1)^2/4`.  Hence the full target is proved
for every configuration covered by `k^(o(1))` parallel lines.

Keeping the loss gives the quantitative consequence

\[
 \boxed{k\ll m^{2/3}\bigl(1+R_\pi^{1/3}\bigr)
       \ll m^{2/3}(1+r^{2/3}).}                 \tag{1.4}
\]

Indeed, (1.1) and the ambient key bound give
`sum_q |H_q| << R_pi^2 m^2`.  The exact equal-centroid identity then gives
third additive energy `O(k^3+R_pi^2 m^2)`, while origin localization gives
`Omega(k^6/m^2)`.  Taking the two possible dominant terms proves (1.4).

This is a branch theorem, not a solution of Erdős problem 1208.  It shows
that any polynomial failure of the new resonance gate must have
polynomially many pair-sum levels in every direction.  Together with the
existing high-resonance-index affine theorem, it removes the rank-one end
of a prospective inverse argument; the unresolved model is genuinely
rank two.

## 2. Proof

The two linear functionals

\[
 \pi,\qquad \pi\circ\Lambda                 \tag{2.1}
\]

are linearly independent.  Otherwise `pi Lambda=c pi` for a real `c`, so
`pi` would be a real left eigenvector of `Lambda`.  But the eigenvalues of
`Lambda=3(I+J)` are `3+3i` and `3-3i`, and it has no real eigenvector.

Fix an output `z` of `Psi_q`.  Map a preimage `(s,t)` to

\[
 (\pi(s),\pi(t))\in\pi(\Sigma)^2.              \tag{2.2}
\]

This map is injective.  Indeed, once the two scalars in (2.2) and `z` are
known, the identity

\[
 \pi(z)=\pi(s)+(\pi\circ\Lambda)(t)            \tag{2.3}
\]

recovers `(pi o Lambda)(t)`.  The two independent functionals in (2.1)
then recover the point `t`; finally `s=z-Lambda t`.  Therefore every charge
fibre has size at most `R_pi^2`.

If `nu_q(z)=|Psi_q^(-1)(z)|`, then

\[
 \sum_z\nu_q(z)=N|H_q|.
\]

The maximum-fibre estimate just proved gives

\[
 \sum_z\nu_q(z)^2
 \le R_\pi^2\sum_z\nu_q(z)
 =R_\pi^2N|H_q|,
\]

which is (1.1).  The exact energy identity from the dilated charge note
says that the diagonal contribution is `N|H_q|`; subtracting it proves
(1.2).

For (1.3), the value of `pi` on a point of `A` is one of at most `r`
numbers.  Every element of `Sigma` is a sum of two distinct points, so its
projection belongs to the ordinary two-fold sumset of those `r` numbers.
That sumset has at most `r(r+1)/2` unordered values.  This completes the
proof of (1.1)--(1.3).  The deduction of (1.4) is the final paragraph of
Section 1.

## 3. Exact regression check

The companion verifier checks the fibre injection directly on:

* a 16-point collinear Erdős--Turán ruler, where every charge fibre has
  size one;
* the stored 30-point closure under several primitive projections.

It also verifies (1.1), including every realized `q`, rather than only the
largest clean fibre.  Run

```text
python3 phase2/loop/erdos1208/verify_dilated_internal_pair_sum_projection_branch.py
```

The computation is a regression artifact.  The proof of Theorem 1.1 is the
two-functional inversion in (2.3).

## 4. Restart target

The remaining case has no projection with subpolynomial pair-sum support.
An inverse theorem fed by a polynomial failure of the dilated energy must
therefore end in one of two places:

1. a rank-one/projection-sparse model, now closed by Theorem 1.1; or
2. a genuinely rank-two, low-index Gaussian model.

Only the second branch is live.  Ordinary Balog--Szemerédi--Gowers density
is not enough there: the sparse oblique-midpoint constructions already show
that a dense subset of a two-dimensional progression need not contain a
large complete patch.  The next argument must retain the complete pair-sum
endpoint representations of `Sigma` and the clean translate
`H_q subset Sigma intersect (Sigma-q)`.
