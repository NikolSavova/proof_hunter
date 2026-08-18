# The two-sided rotated-support audit

## Status

The identity

\[
 J\bigl(A+JA-JA\bigr)=JA+A-A
\]

makes the two natural third sumsets have the same size.  It is tempting to
seek a product lower bound for them and then take a square root.  This note
shows exactly what the abstract direct-sum information gives and why it is
one full power short.

For arbitrary finite sets `X,Y` in a torsion-free abelian group, assume that
the map

\[
 X\times Y\longrightarrow X+Y
\]

is injective.  Put

\[
 S=X+Y-Y,\qquad T=Y+X-X.
\]

Then

\[
 \boxed{|S||T|\ge |X|^2|Y|^2.}                 \tag{0.1}
\]

The exponent in (0.1) is sharp.  There are arbitrarily large equal-sized
co-Sidon pairs `X,Y subset Z` for which both third sumsets have only
`O(|X|^2)` elements.  Consequently, for `X=A` and `Y=JA`, (0.1) gives only
`|A+JA-JA|>=|A|^2`.  Any stronger estimate must use the same-set rotation
`Y=JX` together with Euclidean radial uniqueness; directness, individual
Sidonicity, planarity, and two-sided symmetry are not enough.

The verifier checks the injection on exact finite examples, constructs the
sharp Erdos--Turan Golomb-ruler model, and checks the centered collision
identity in Section 3.

## 1. Exact four-variable injection

For `(x_1,x_2,y_1,y_2) in X^2 x Y^2`, define

\[
 s=x_1+y_1-y_2\in S,
 \qquad
 t=y_2+x_2-x_1\in T.                            \tag{1.1}
\]

This map into `S x T` is injective.  Indeed,

\[
 s+t=y_1+x_2.                                   \tag{1.2}
\]

The directness of `X+Y` recovers `(y_1,x_2)` from (1.2).  It then recovers
`(y_2,x_1)` from

\[
 t-x_2=y_2-x_1.                                 \tag{1.3}
\]

For the second assertion, if `y-x=y'-x'`, then
`x'-x=y'-y` belongs to both `(X-X)` and `(Y-Y)`.  Directness says that this
intersection is `{0}`, so both pairs agree.  Counting the domain of (1.1)
proves (0.1).

For a distance-Sidon set `A`, the sums `A+JA` and `A-JA` are direct.  Taking
`X=A,Y=JA` and using `T=JS` therefore yields only

\[
 |A+JA-JA|\ge |A|^2.                            \tag{1.4}
\]

This is the same quadratic floor already supplied by the direct sum
`|A+JA|=|A|^2`; the product symmetry does not amplify it.

## 2. Sharp co-Sidon model

For a prime `p`, the classical Erdos--Turan sequence

\[
 R_p=\{2pi+(i^2\bmod p):0\le i<p\}
       \subset[0,2p^2)                           \tag{2.1}
\]

is a Sidon set.  To see this, suppose

\[
 r_i+r_j=r_a+r_b.
\]

The residue terms in (2.1) have sums strictly between `0` and `2p`, so the
equality first gives `i+j=a+b`.  Reducing modulo `p` then gives
`i^2+j^2=a^2+b^2`, and hence `ij=ab (mod p)`.  The two unordered pairs are
the same pair of roots modulo `p`, and all indices lie in `[0,p)`.  Thus
`{i,j}={a,b}`.

Given `k`, choose a prime `p` between `2k` and `4k` and split any `2k`
members of `R_p` into disjoint `k`-sets `X,Y`.  Since `X union Y` is Sidon,
`X+Y` is direct and both sets are individually Sidon.  On the other hand all
their elements lie in an interval of length `O(k^2)`, so

\[
 |X+Y-Y|=O(k^2),\qquad |Y+X-X|=O(k^2).           \tag{2.2}
\]

This proves sharpness of (0.1) at the exponent level.  Embedding the same
sets on a line in the plane shows that merely restating the argument in
planar language does not help.

The model is deliberately not of the form `Y=JX`.  That missing condition,
and the fact that the norm map is injective on the complete difference set
of `A`, are precisely the information a successful proof still has to use.

## 3. The exact centered Fourier residual

There is a useful positive identity explaining what remains after all
direct-sum information has been used.  Work in a finite abelian group large
enough to avoid wraparound, let `J` be an order-four automorphism, and use
the unnormalised Fourier transform.  Put

\[
 X(\chi)=|\widehat{1_A}(\chi)|^2,
 \qquad Y(\chi)=X(J^*\chi),
\]

and write `E_chi` for the average over characters.  If `A` is vector-Sidon
and `(A-A) intersect J(A-A)={0}`, then

\[
 \mathbb E X=\mathbb E Y=k,
 \quad
 \mathbb E X^2=\mathbb E Y^2=2k^2-k,
 \quad
 \mathbb E XY=k^2.                              \tag{3.1}
\]

The last equality is exactly the directness of `A+JA`.  The full rotated
triple energy is

\[
 \mathcal E_J(A)
 =\sum_z r_{A+JA-JA}(z)^2
 =\mathbb E_\chi X(\chi)Y(\chi)^2.              \tag{3.2}
\]

Set `F=X-k` and `G=Y-k`.  Expanding (3.2) and using (3.1) gives

\[
 \boxed{
 \mathcal E_J(A)=2k^3-k^2+\mathbb E_\chi F(\chi)G(\chi)^2.}       \tag{3.3}
\]

The residual is not a signed mystery.  If

\[
 D^*=(A-A)\setminus\{0\},
\]

then Fourier orthogonality gives

\[
 \mathbb E_\chi F G^2
 =\#\{(d,u,v)\in(D^*)^3:u+v=Jd\}.               \tag{3.4}
\]

It is therefore a nonnegative integer: the exact excess collision count
above the unavoidable `2k^3-k^2` baseline.  Rotation symmetry also gives

\[
 \mathbb E F G^2=\mathbb E G F^2
 =\frac12\mathbb E\bigl[FG(F+G)\bigr].          \tag{3.5}
\]

Equations (3.3)--(3.5) sharpen the restart point.  Ordinary second moments
and the covariance of `X,Y` are already completely exhausted by directness:
`F` and `G` are orthogonal.  The full problem is the centered cubic
correlation, with the parallel two-ruler contribution removed or handled by
the line-support lemma.  A Shannon/Ruzsa/product argument that sees only the
three numbers in (3.1) cannot control (3.4).

## 4. Consequence for the full attack

The two-sided-product lane is closed at the abstract level.  Do not seek a
`k^6` product bound from co-Sidonicity or from the equality `|S|=|T|`; the
Golomb model disproves it by a full factor `k^2`.

The live theorem remains a specifically Euclidean estimate for the positive
residual (3.4), equivalently the transverse row/decorated-parallelogram
moment in `TRANSVERSE_SECOND_MOMENT_GATE.md`.  A successful inequality must
use at least one of:

1. `Y` is the quarter-turn of the *same* set, not an unrelated co-Sidon set;
2. every nonzero element of `A-A` has a globally unique Euclidean norm; or
3. `A-A` is the complete directed difference set of one point set, not an
   arbitrary radial transversal.

This audit is a rigorous route elimination and a cleaner algebraic target,
not a solution of Erdős 1208.
