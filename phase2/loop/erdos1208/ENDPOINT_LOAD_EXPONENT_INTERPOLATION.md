# Endpoint-load interpolation toward the cube-root bound

## 1. Outcome

Keep the notation of
`ENDPOINT_CROSS_SWITCHED_COLLISION_CHARGE.md`.  Thus

\[
 D=A-A,\qquad N=|D|,\qquad S=|D+D|,
\]

the adaptive rich-fibre off-diagonal mass is \(\mathcal O_K\), the first
\(D^2\)-charge has collision moment \(M_K\), and the refined endpoint
charge has load \(\mu\) on a universe of size at most \(6NS\).

The ideal remaining theorem is the size-biased estimate

\[
 \sum\mu^2\le N^{o(1)}M_K.
\]

There is a useful weaker hierarchy.  Suppose only that

\[
 \boxed{\max\mu\le N^{\rho+o(1)}}                 \tag{1.1}
\]

for some fixed \(\rho\ge0\).  Then the orthogonal energy obeys

\[
 \boxed{
 \mathcal E_\perp(D)
 \le N^{1+\rho/4+o(1)}S.}                       \tag{1.2}
\]

Consequently, if \(A\subseteq[m]^2\), then

\[
 \boxed{
 |A|\le m^{\,2/(3-\rho/4)+o(1)}.}               \tag{1.3}
\]

Equivalently, inside the \(n=m^2\) point square grid,

\[
 |A|\le n^{\,1/(3-\rho/4)+o(1)}.                \tag{1.4}
\]

Two cases calibrate the hierarchy:

* \(\rho=0\) recovers the desired cube-root exponent \(1/3\);
* the much weaker pointwise conjecture
  \(\max\mu\le |A|^{1+o(1)}=N^{1/2+o(1)}\) gives

  \[
  |A|\le n^{8/23+o(1)},\qquad {8\over23}=0.347826\ldots. \tag{1.5}
  \]

Thus a linear-in-endpoints load theorem would already be a substantial
intermediate result.  It is still unproved.  The exact stresses are
consistent with it: after the zero-midpoint refinement the largest loads
on the displayed Costas families are of the same order as \(|A|\), not
bounded constants.

## 2. Proof of the interpolation

The first charge gives

\[
 \mathcal O_K^2\le N^2M_K.                       \tag{2.1}
\]

The endpoint charge has total mass

\[
 \sum_\eta\mu(\eta)=M_K.                        \tag{2.2}
\]

Under (1.1),

\[
 \sum_\eta\mu(\eta)^2
 \le(\max\mu)M_K
 \le N^{\rho+o(1)}M_K.                         \tag{2.3}
\]

Cauchy--Schwarz on the endpoint target of size at most \(6NS\) yields

\[
 M_K^2\le6NS\sum\mu^2
 \le N^{1+\rho+o(1)}S M_K.
\]

After cancelling \(M_K\), and then applying (2.1),

\[
 M_K\le N^{1+\rho+o(1)}S,
 \qquad
 \mathcal O_K
 \le N^{(3+\rho)/2+o(1)}S^{1/2}.
\]

Since \(S\ge N\), this becomes

\[
 \boxed{\mathcal O_K\le N^{1+\rho/2+o(1)}S.}    \tag{2.4}
\]

Let

\[
 T_K=\sum_{u,s}g_K(u,s)
\]

be the adaptive rich-fibre mass.  Its second moment is exactly

\[
 \sum_{u,s}g_K(u,s)^2=T_K+\mathcal O_K.
\]

There are at most \(NS\) fibre labels, so another Cauchy--Schwarz
inequality and (2.4) give

\[
 T_K^2
 \le NS(T_K+\mathcal O_K).
\]

Solving this quadratic inequality, or using
\(x^2\le ax+b\Rightarrow x\le a+\sqrt b\), gives

\[
 T_K
 \le NS+\sqrt{NS\mathcal O_K}
 \le N^{1+\rho/4+o(1)}S.                       \tag{2.5}
\]

The zero shift and the two non-adaptive low parts of the orthogonal energy
contribute only \(O(NS)\).  Equation (2.5) therefore proves (1.2).

Let \(T=|D+JD|\).  The standard energy--support inequality is

\[
 T\ge {N^4\over\mathcal E_\perp(D)}.
\]

Combining this with (1.2) gives

\[
 ST\ge N^{3-\rho/4-o(1)}.                       \tag{2.6}
\]

For \(A\subseteq[m]^2\), both \(D+D\) and \(D+JD\) lie in fixed
integer boxes of area \(O(m^2)\).  Hence \(S,T=O(m^2)\), and (2.6) gives

\[
 N\le m^{4/(3-\rho/4)+o(1)}.
\]

Finally \(N=|A|(|A|-1)+1=|A|^{2+o(1)}\), proving (1.3)--(1.4).

## 3. Why the simplest injectivity proof fails

The endpoint key already recovers two heads \(\alpha,\beta\in A\).  It is
natural to hope that recording one or both corresponding tails makes the
charge injective.  This is false even on small genuine distance-Sidon
sets.

For the transformed Welch--Costas families, condition the refined charge
simultaneously on

\[
 y_{R_4(\gamma)},\qquad y_{R_2(\gamma')}.
\]

The maximum remaining multiplicities for sizes \(13,17,19\) are

\[
 3,\quad5,\quad8,                                \tag{3.1}
\]

respectively.  Thus even two additional literal endpoints do not make the
map bounded-to-one in the tested family.  These finite values do not
disprove an \(N^{o(1)}\) conditional multiplicity, but they rule out the
most direct exact inversion.

The practical restart point is therefore one of the following:

1. prove the full size-biased moment theorem;
2. prove the weaker linear pointwise bound in (1.5); or
3. condition on endpoint tails and prove that the residual multiplicity in
   (3.1) is subpolynomial, then sum over the \(|A|^2=N^{1+o(1)}\) tail
   pairs with a sharper aggregate charge.

Run

    python3 phase2/loop/erdos1208/verify_endpoint_load_exponent_interpolation.py

for the exact rational exponent calculation and the conditioned-load
profiles in (3.1).
