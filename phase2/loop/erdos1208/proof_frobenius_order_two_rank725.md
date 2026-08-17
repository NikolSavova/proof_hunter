# Rank-725 optimization of the quadratic-Frobenius construction

## Result

The proof in `proof_frobenius_order_two.md` remains unchanged after replacing
the rank-400 presentation and its two-stage numerical data by the parameters
below.  They give the strengthened explicit partial result

\[
  \boxed{F_2(n)\ll n^{0.49459}.}
\]

The complete finite computation is in
`verify_frobenius_order_two_rank725.py`.

## 1. Presentation data

Let (T) be the first 726 odd rational primes.  The positive odd quadratic
discriminants supported on (T) form a 725-dimensional vector space over
\(\mathbb F_2\).  A basis consists of every singleton
\(p\equiv1\pmod4\) in (T), together with (3p) for every
\(p\equiv3\pmod4\), (p\ne3).  Thus the tame totally-real Shafarevich
presentation has

\[
  d=725,\qquad r_0\le725.
\]

Take the first

\[
  N=130681
\]

unramified odd primes satisfying the useful-prime condition from
`proof_frobenius_order_two.md`: either (q\equiv1\pmod4), or
\(q\equiv3\pmod4\) and its Frobenius class is nonzero in the displayed
Frattini quotient.  The verifier finds that the last such prime is
1,747,247.  Quotienting by the (N) Frobenius-square relators preserves the
generator rank and gives

\[
  r\le725+130681=131406
     <\frac{725^2}{4}=131406.25.
\]

The Golod--Shafarevich inequality therefore supplies the infinite pro-2
tower, with root-discriminant bound

\[
  D=\prod_{p\in T}p,
  \qquad
  \log D
  =5407.904825022434791701075426363109763141425685688\ldots .
\]

The verifier checks the prime lists, the 725-dimensional square-class rank,
the useful-prime criterion, and the strict integer inequality
\(4r<d^2\).  In fact no (3\pmod4) prime is rejected before the useful-prime
cutoff, but the proof uses the criterion rather than assuming this pattern.

## 2. Local path and endpoint certificate

Use the same worst-residue-degree-two local increments as in the rank-400
proof:

\[
 h_{q,1}=\frac12\log\frac{2}{1+q^{-2}},\qquad
 h_{q,2}=\frac12\log
 \frac{3(1+q^{-2})}{2(1+q^{-2}+q^{-4})}.
\]

Give all useful primes their first increment in increasing order, followed
by second increments in increasing order.  Fractional use of the last prime
is implemented by the residue-degree-two placewise rounding lemma.

Set

\[
  \alpha=0.49459,\qquad w_0=1069500.
\]

If (F(L)) is the guaranteed gain on this path, the master inequality is
valid at scale (w) once

\[
 F(2\alpha w)\ge
 \log(4D)+(2-4\alpha)w+
 \log\!\left(1+\frac{e^{2(2\alpha-1)w}}{4D}\right).       \tag{1}
\]

The transition between the two stages is

\[
 w_*=1759107.5828599767385044417384446090113179327105\ldots,
\]

which lies strictly inside ([w_0,2w_0]).  Concavity reduces (1) to the
three endpoints (w_0,w_*,2w_0).  After subtracting a numerical allowance
of (10^{-29}), the certified margins are respectively

\[
  23.2840128368\ldots,qquad
  1814.2041294306\ldots,qquad
  23.9472153445\ldots .
\]

For every sufficiently large (n), choose a degree-(2^j) layer so that

\[
  w=\frac{\log n}{2[K:\mathbb Q]}\in[w_0,2w_0).
\]

Use the first or second stage according as (w\le w_*) or (w>w_*).
The fixed endpoint margins absorb the (O(1/[K:\mathbb Q])) placewise
rounding error.  The master inequality then gives

\[
  |A|\le(1+\sqrt2)n^{0.49459}
\]

for every distance-Sidon subset (A) of the constructed planar point set.
The finite initial range is absorbed into the implied constant.

## 3. Scope and verification

This is a strict improvement of the explicit upper exponent, not a resolution
of Erdős problem #1208.  It uses the same two declared external inputs as the
rank-400 proof: the tame totally-real Shafarevich presentation theorem and the
prime-power master inequality proved in the accompanying notes.

The verifier uses exact integer arithmetic for the prime, square-class, and
Golod--Shafarevich checks.  Its transcendental endpoint calculations use
80-digit `Decimal` arithmetic rather than directed interval arithmetic; the
smallest displayed margin exceeds 23, so the numerical slack is far larger
than any rounding uncertainty at that precision.
