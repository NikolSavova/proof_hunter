# Cubic dilated pair-sum support in the high-resonance-index branch

## 1. Outcome

Let

\[
 L=I+J,\qquad J(x,y)=(-y,x).
\]

The support target

\[
 |2A-LA|\ge |A|^{3-o(1)}                       \tag{1.1}
\]

would give the cube-root grid upper bound in Erdős problem 1208.  The
preceding heavy-fibre note shows that (1.1) cannot be proved by bounding
every dilation overlap.  This note proves (1.1) for a broad and important
branch instead: distance-separating affine images whose quarter-turn
resonance lattice has sufficiently large index.

In particular, it proves a uniform constant-times-cubic bound for every
determinant-prime affine Welch--Costas stress in
`DETERMINANT_PRIME_COSTAS_RESONANCE.md`.  Those examples were the main
low-doubling affine adversaries for the adaptive tail.

## 2. Exact collision theorem

Call `A_0 subset Z^2` **vector-Sidon** if every nonzero element of
`A_0-A_0` has a unique ordered representation as a difference of two
members of `A_0`.  Put `k=|A_0|`, let `T` be a nonsingular integral
two-by-two matrix, and define

\[
 A=TA_0,\qquad R=T^{-1}JT,
\]

\[
 \Gamma_T=\{z\in\mathbb Z^2:Rz\in\mathbb Z^2\},
 \qquad
 H=|((A_0-A_0)\setminus\{0\})\cap\Gamma_T|.       \tag{2.1}
\]

**Theorem 2.1 (exact resonance collision bound).** One has

\[
 \boxed{
 |2A-LA|\ge
 {k^6\over 2k^3-k^2+H(k^2+k-1)}.}                \tag{2.2}
\]

Consequently, `H<=k^(1+o(1))` implies (1.1).

**Proof.** For ordered triples in `A_0^3`, write

\[
 F(a,b,c)=Ta+Tb-LTc
          =T\bigl(a+b-(I+R)c\bigr).              \tag{2.3}
\]

Let

\[
 r(x)=|\{(a,a')\in A_0^2:a-a'=x\}|.
\]

Vector-Sidonicity says

\[
 r(0)=k,qquad r(x)=1
 \quad(x\in(A_0-A_0)\setminus\{0\}).             \tag{2.4}
\]

A collision between `(a,b,c)` and `(a',b',c')` gives

\[
 x+y=(I+R)z,\qquad
 x=a-a',\ y=b-b',\ z=c-c'.                       \tag{2.5}
\]

The left side and `z` are integral, so (2.5) forces `Rz` to be integral;
hence `z in Gamma_T`.  Conversely, every weighted solution of (2.5) is a
collision.

The contribution from `z=0` is exactly

\[
 r(0)\sum_xr(x)r(-x)
 =k\bigl(k^2+k(k-1)\bigr)=2k^3-k^2.              \tag{2.6}
\]

Now take a nonzero `z`.  Since `R^2=-I`, the map `I+R` is nonsingular, so
`w=(I+R)z` is nonzero.  There are at most

\[
 |A_0-A_0|=k(k-1)+1
\]

possible values of `x` in the inner convolution.  Every product
`r(x)r(w-x)` is one, except that `x=0` or `x=w` can increase it by at most
`k-1` each.  Therefore

\[
 \sum_xr(x)r(w-x)\le k^2+k-1.                    \tag{2.7}
\]

There are exactly `H` eligible nonzero values of `z`, and each has
`r(z)=1`.  Equations (2.6)--(2.7) bound the collision energy of `F` by the
denominator in (2.2).  The domain of `F` has size `k^3`, so
Cauchy--Schwarz proves (2.2).  This completes the proof.

Notice that the theorem uses only vector-Sidonicity of `A_0`.  The
additional assertion that `TA_0` is Euclidean distance-Sidon is needed only
when applying the result to #1208.

## 3. Resonance-index consequence

Write

\[
 T=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
 T^{\mathsf T}T=\begin{pmatrix}\alpha&\beta\\\beta&\gamma\end{pmatrix}.
\]

The Smith-normal-form calculation in
`DETERMINANT_PRIME_COSTAS_RESONANCE.md` gives

\[
 [\mathbb Z^2:\Gamma_T]
 ={|\det T|\over\gcd(\alpha,\beta,\gamma)}=:I_T. \tag{3.1}
\]

If `A_0 subset [0,M]^2`, the elementary Hermite-normal-form lattice count
therefore yields

\[
 H\ll {M^2\over I_T}+M+1.                        \tag{3.2}
\]

Combining (2.2) and (3.2) proves cubic support whenever

\[
 {M^2\over I_T}+M\le k^{1+o(1)}.                 \tag{3.3}
\]

This is the exact high-resonance-index branch of the proposed affine
dichotomy.  The unresolved regime is small `I_T`, where the lattice is
nearly quarter-turn stable and collision differences are not confined to a
thin congruence lattice.

## 4. Determinant-prime Costas corollary

Let `p` be prime, let `A_0 subset [0,p)^2` be a `k=p-1` Welch--Costas
array, and suppose

\[
 \det T=p,
\]

with the Gram matrix of `T` nonzero modulo `p`.  Then `Gamma_T mod p` is a
line with `p` residue vectors.  Every residue vector has at most four lifts
in `A_0-A_0 subset (-p,p)^2`, so

\[
 H\le4p-1=4k+3.                                  \tag{4.1}
\]

For `p>=7`, (2.2) and (4.1) give the explicit uniform estimate

\[
 \boxed{|2TA_0-(I+J)TA_0|\ge {k^3\over7}.}        \tag{4.2}
\]

Thus every determinant-prime affine image which also separates all
Euclidean distances satisfies the full cubic-support target.  The exact
finite profiles are substantially stronger: on the stored primes 11
through 43, the support lies between `0.506` and `0.542` times `k^3`, and
the collision-energy lower bound is within a few percent of the actual
support.

The companion verifier checks the resonance restriction, exact collision
identity, Cauchy bound, distance-Sidonicity, and stored profiles for all ten
determinant-prime matrices.

## 5. Strategic consequence

This closes the generic/high-index affine branch without invoking the
seven-incidence charge.  It also explains why exhaustive affine searches
found almost-injective cubic support even when the adaptive swap graph was
nonempty.

The live full problem is now more localized: a counterexample to (1.1)
must have a dense, low-index quarter-turn resonance model.  That is exactly
the regime where the sharp oblique-lattice height theorem applies to a
complete patch, and where the remaining difficulty is upgrading sparse
endpoint-realizable structure to sufficient aggregate support.
