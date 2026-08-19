# The joint positive-spectrum gate for the remaining mixed energy

## 1. Outcome

Let `A subset Z^2` be distance-Sidon, put

\[
 k=|A|,\qquad D=A-A,\qquad N=|D|=k(k-1)+1,
\]

and let `J` be rotation by 90 degrees.  Define the real Fourier polynomial

\[
 \lambda(\theta)=\widehat{1_D}(\theta),\qquad
 \mu(\theta)=\lambda(J\theta).
\]

The complete-difference identity gives

\[
 \lambda(\theta)=|\widehat{1_A}(\theta)|^2-(k-1),
 \qquad \lambda,\mu\ge -(k-1).                 \tag{1.1}
\]

The orthogonal difference energy is

\[
 E_\perp(D)=\int_{\mathbb T^2}\lambda(\theta)^2
                         \mu(\theta)^2\,d\theta. \tag{1.2}
\]

Put

\[
 \mathcal H_*=
 \{\theta:\lambda(\theta)>N^{3/4},\quad
             \mu(\theta)>N^{3/4}\}.             \tag{1.3}
\]

Then the whole complement of this simultaneous large positive spectrum is
already at the critical fifth-power scale:

\[
 \boxed{
 E_\perp(D)
 \le 2N^{5/2}+\int_{\mathcal H_*}\lambda^2\mu^2.} \tag{1.4}
\]

Thus the ambient-energy theorem needed for Erdős 1208 is reduced to

\[
 \boxed{
 \int_{\mathcal H_*}\lambda^2\mu^2
 \le N^{5/2+o(1)}+m^{2+o(1)}N.}                \tag{1.5}
\]

This is a reduction, not a proof of (1.5).  Its value is that the remaining
mass is now localized simultaneously in sign, size, and two perpendicular
frequencies.  Generic high additive energy, negative spectrum, every
one-sided-large layer, and even the unbalanced positive layers are no longer
part of the problem.  In terms of the original exponential sum, (1.3) says
that both `|hat 1_A(theta)|` and `|hat 1_A(J theta)|` are larger than
`N^(3/8)=k^(3/4+o(1))`.

## 2. Exact proof

Parseval gives

\[
 \int\lambda^2=|D|=N,
 \qquad \int\mu^2=N.                            \tag{2.1}
\]

There are two useful truncations.  First, Cauchy--Schwarz gives the exact
`L^1` product estimate

\[
 \int|\lambda\mu|
 \le\left(\int\lambda^2\right)^{1/2}
      \left(\int\mu^2\right)^{1/2}=N.          \tag{2.2}
\]

On the set where `|lambda mu|<=N^(3/2)`,

\[
 \lambda^2\mu^2
 \le N^{3/2}|\lambda\mu|.
\]

Integration and (2.2) show that this set contributes at most `N^(5/2)`.

It remains only to identify the complementary set.  Since

\[
 (k-1)^2\le k(k-1)+1=N,                        \tag{2.3}
\]

equation (1.1) gives `lambda,mu>=-sqrt(N)`.  Also

\[
 \lambda,\mu\le k^2-(k-1)=N.                  \tag{2.4}
\]

If either factor is nonpositive, then

\[
 |\lambda\mu|\le\sqrt N\,N=N^{3/2}.
\]

The same upper bound holds if either positive factor is at most `sqrt(N)`.
Consequently `|lambda mu|>N^(3/2)` can occur only when both factors are
positive and larger than `sqrt(N)`.  This already removes the wrong-sign
and low-product regimes.

The balanced truncation is stronger.  Put `T=N^(3/4)`.  On the set
`|lambda|<=T`,

\[
 \lambda^2\mu^2\le T^2\mu^2.
\]

By (2.1), its integral is at most

\[
 T^2N=N^{5/2}.                                  \tag{2.5}
\]

The symmetric set `|mu|<=T` has the same bound.  Outside their union both
absolute values exceed `T`.  Since `T>sqrt(N)` and the negative floor is
`-sqrt(N)`, both factors must then be positive.  The remaining set is
exactly `mathcal H_*`, proving (1.4).

There is also the orthogonality identity

\[
 \int\lambda\mu=|D\cap JD|=1,                 \tag{2.6}
\]

because radial uniqueness gives `D cap JD={0}`.  It is not needed for
(1.4), but it shows that large positive joint spectrum must be compensated
by opposite-sign spectrum elsewhere.  This is the precise interface with
`ENDPOINT_FOURIER_COMPENSATION_LEMMA.md`.

## 3. Dyadic form

For dyadic `L,M>N^(3/4)`, put

\[
 \mathcal H_{L,M}
 =\{\theta:L<\lambda\le2L,\ M<\mu\le2M\}.
\]

Equation (2.2) immediately gives

\[
 |\mathcal H_{L,M}|\,LM\le N,                 \tag{3.1}
\]

and hence

\[
 \int_{\mathcal H_{L,M}}\lambda^2\mu^2
 \le16NLM.                                     \tag{3.2}
\]

The new information is not merely `LM>N^(3/2)`: each factor separately
exceeds `N^(3/4)`.  This deletes the highly unbalanced layers that survived
the first product truncation.

In terms of the original exponential sum, these layers satisfy

\[
 |\widehat{1_A}(\theta)|^2=L+O(\sqrt N),\qquad
 |\widehat{1_A}(J\theta)|^2=M+O(\sqrt N).       \tag{3.3}
\]

Thus a counterexample forces genuinely simultaneous large spectrum of `A`
at a frequency and its quarter-turn.  A one-frequency BSG statement or an
ordinary higher-energy inverse theorem discards precisely this correlation.

## 4. The remaining density-increment theorem

The most direct next statement is now the following.

> **Perpendicular large-spectrum theorem.**  For a distance-Sidon
> `A subset [0,m]^2`, the dyadic layers with `L,M>N^(3/4)` satisfy
> \[
> \sum_{L,M}\int_{\mathcal H_{L,M}}\lambda^2\mu^2
> \le N^{5/2+o(1)}+m^{2+o(1)}N.
> \]

The endpoint Fourier floor in (1.1) must remain load-bearing.  The sparse
oblique radial transversals from `SPARSE_OBLIQUE_MIDPOINT_BARRIER.md` can
have large mixed energy but do not satisfy this floor.  Conversely, a large
joint positive layer must create enough opposite-sign compensation through
(2.6).  The missing step is to localize that compensation to a structured
piece of `D`; once such a piece is found,
`ENDPOINT_FOURIER_COMPENSATION_LEMMA.md` quantifies the required complement.

This formulation is preferable to trying to bound the whole mixed fourth
moment at once: the low product, wrong-sign, one-sided-large, and unbalanced
positive regimes have now been removed with the sharp critical exponent.

Run

```text
python3 phase2/loop/erdos1208/verify_joint_positive_spectrum_gate.py
```

for exact coefficient-side checks of `D cap JD={0}`, the two Parseval inputs,
the orthogonal-energy identity, and the integer-squared endpoint comparisons
used in the threshold argument.  The analytic inequality itself is the
two-line Cauchy--Schwarz proof in Section 2; the computation is a regression
artifact, not a substitute for that proof.
