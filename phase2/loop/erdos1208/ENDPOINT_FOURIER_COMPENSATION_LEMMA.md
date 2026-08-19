# Endpoint Fourier compensation for structured pieces of \(A-A\)

## 1. Outcome

Let \(A\subset\mathbb Z^2\) be vector-Sidon, put \(k=|A|\), and let

\[
D=A-A,\qquad f=1_D.
\]

Distance-Sidonicity implies vector-Sidonicity, so this applies throughout
the direct attack on Erdős 1208. The familiar endpoint identity is

\[
\widehat f(\theta)=|\widehat {1_A}(\theta)|^2-(k-1)
\ge -(k-1).                                      \tag{1.1}
\]

This note gives a quantitative version for a structured piece
\(0\le g\le1_D\). If \(g\) has Fourier mass below the floor in (1.1), the
complement \(1_D-g\) must supply the entire deficit, both pointwise and in
\(L^2\). For an indicator \(g=1_E\), \(E\subseteq D\), this gives

\[
\boxed{
\int_{\mathbb T^2}
  \bigl(-(k-1)-\operatorname {Re}\widehat {1_E}(\theta)\bigr)_+^2
  \,d\theta
\le |D\setminus E|.}                           \tag{1.2}
\]

If \(E\) lies in a box of height \(M\) and has one linearly negative
Fourier coefficient, (1.2) automatically spreads that deficit over a
frequency square. The resulting explicit consequence is

\[
\boxed{
|D\setminus E|
\ge {\eta^2\over16\pi^2M^2}
      \left({\eta|E|\over2}-(k-1)\right)_+^2} \tag{1.3}
\]

whenever

\[
\operatorname {Re}\widehat {1_E}(\theta_0)
\le-\eta|E|,\qquad 0<\eta\le1.               \tag{1.4}
\]

In particular, if \(\eta|E|\ge4(k-1)\), then

\[
\boxed{
|D\setminus E|
\ge {\eta^4|E|^2\over256\pi^2M^2}.}          \tag{1.5}
\]

This does not yet produce the structured set \(E\) from excessive
cross-fibre load. It supplies the rigorous compensation half of that
program: once a dense Gaussian/shear core with a negative mode is
extracted, its missing endpoint support is no longer heuristic.

## 2. The endpoint identity

Use the unnormalised Fourier transform

\[
\widehat h(\theta)=
\sum_{x\in\mathbb Z^2}h(x)e^{-2\pi i\theta\cdot x}.
\]

The autocorrelation

\[
c_A(x)=|\{(a,b)\in A^2:a-b=x\}|
\]

has Fourier transform \(|\widehat {1_A}|^2\). Vector-Sidonicity gives

\[
c_A=k\delta_0+1_{D\setminus\{0\}}
   =1_D+(k-1)\delta_0.                          \tag{2.1}
\]

Taking Fourier transforms proves (1.1).

The identity is stronger than radial uniqueness. An abstract set may have
one representative from every nonzero norm and nevertheless have a Fourier
coefficient of order \(-|D|\). A complete difference set can go only down
to \(-(k-1)\), which is of order \(-\sqrt{|D|}\).

## 3. The compensation theorem

### Theorem 3.1

Let \(g:\mathbb Z^2\to[0,1]\) satisfy \(g\le1_D\), and put

\[
r=1_D-g,\qquad
\Delta_g(\theta)=
\bigl(-(k-1)-\operatorname {Re}\widehat g(\theta)\bigr)_+.
\]

Then

\[
\boxed{\Delta_g(\theta)\le|\widehat r(\theta)|}          \tag{3.1}
\]

for every \(\theta\), and

\[
\boxed{
\int_{\mathbb T^2}\Delta_g(\theta)^2\,d\theta
\le\sum_x r(x)^2
\le |D|-\sum_xg(x).}                           \tag{3.2}
\]

### Proof

If \(\Delta_g(\theta)>0\), then (1.1) gives

\[
\operatorname {Re}\widehat r(\theta)
=\widehat {1_D}(\theta)
  -\operatorname {Re}\widehat g(\theta)
\ge -(k-1)-\operatorname {Re}\widehat g(\theta)
=\Delta_g(\theta).
\]

This proves (3.1); the case \(\Delta_g=0\) is immediate. Parseval gives the
first inequality in (3.2). Since \(0\le r\le1\), one has \(r^2\le r\),
which gives the second. QED.

Taking \(g=1_E\) proves (1.2). There is also the useful pointwise version

\[
\bigl(-(k-1)-\operatorname {Re}\widehat {1_E}(\theta)\bigr)_+
\le |D\setminus E|.                            \tag{3.3}
\]

Unlike (1.2), (3.3) does not exploit the geometric width of a Fourier peak.

## 4. Height-localised compensation

Assume \(E\subseteq[-M,M]^2\), with \(M\ge1\), and write \(W=|E|\).
For either coordinate,

\[
\left|\partial_j\operatorname {Re}\widehat {1_E}(\theta)\right|
\le2\pi MW.                                    \tag{4.1}
\]

If (1.4) holds, put

\[
\rho={\eta\over8\pi M}.
\]

For every \(\theta\) in the \(L^\infty\)-square of radius \(\rho\) around
\(\theta_0\), the two-coordinate mean-value bound (4.1) gives

\[
\operatorname {Re}\widehat {1_E}(\theta)
\le-{\eta W\over2}.                           \tag{4.2}
\]

The square has Haar measure

\[
4\rho^2={\eta^2\over16\pi^2M^2}.
\]

Insert the lower bound

\[
\Delta_{1_E}(\theta)
\ge\left({\eta W\over2}-(k-1)\right)_+
\]

on this square into (1.2). This proves (1.3). Under
\(\eta W\ge4(k-1)\), the last display is at least \(\eta W/4\), which
proves (1.5).

The scale is important. A structured piece of size \(W\asymp r^2\) and
height \(M=r^{3/2}\) pays only order \(r\) missing differences, matching
the codimension-one modular-midpoint stability scale. At smaller height the
forced complement grows. This is consistent with, and explains
spectrally, why arbitrary dense oblique subsets survive far below the
complete-patch threshold while exact endpoint realization remains
potentially stronger.

## 5. Interface with the live cross-fibre theorem

The current \(D^2\) and opposite-endpoint charges reduce the missing
adaptive tail to a dense core containing several coupled affine copies
inside \(D\). The abstract radial shear models show that these copies and
adaptive popularity alone do not bound the core. Their failure to be a
complete difference is visible through a Fourier coefficient of order
\(-|D|\).

Theorem 3.1 gives a precise two-step target.

1. From a dyadic cross-fibre core with excessive size-biased load, extract a
   weight \(0\le g\le1_D\) whose negative spectral deficit is comparable to
   the core mass.
2. Apply (3.2), or the height-sensitive form (1.3), and charge the required
   complement to unused ordinary sums or to the boundary of the core.

Step 2 is now a theorem. Step 1 remains the genuinely new density-increment
problem. The lemma does not revive the scalar balanced-Fourier route killed
by perpendicular rulers: it is applied to a selected endpoint-decorated
piece \(g\), not to the full mixed Fourier moment.

Run

    python3 phase2/loop/erdos1208/verify_endpoint_fourier_compensation.py

for exact autocorrelation and parity-character checks, plus finite-torus
Parseval tests of (3.2).
