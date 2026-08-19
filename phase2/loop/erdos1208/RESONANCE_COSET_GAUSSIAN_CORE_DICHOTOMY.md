# Resonance-coset decomposition and the Gaussian hard core

## 1. Outcome

Let

\[
 J(x,y)=(-y,x),\qquad L=I+J,
\]

let `A_0 subset Z^2` be vector-Sidon, let `T` be a nonsingular integral
two-by-two matrix, and put

\[
 A=TA_0,\qquad R=T^{-1}JT,
\]

\[
 \Gamma=\{z\in\mathbb Z^2:Rz\in\mathbb Z^2\},
 \qquad \Lambda=T\Gamma.
\]

The collision theorem in `DILATED_PAIR_SUM_RESONANCE_BRANCH.md` proves
cubic support when only few differences of `A_0` lie in `Gamma`.  This
note identifies the complementary branch exactly.

Partition `A_0` into its cosets modulo `Gamma`, with occupancies `k_C`, and
write `k=|A_0|`.  Then:

1. the resonance count is exactly

   \[
   H=\sum_C k_C(k_C-1);
   \]

2. if `h=max_C k_C`, then

   \[
   \boxed{|2A-LA|\ge {k^3\over2h}};
   \]

3. `Lambda` is invariant under the quarter-turn `J`, hence is a scaled and
   rotated copy of the Gaussian lattice `Z[i]`; and
4. the internal triple supports of distinct coset pieces lie in disjoint
   lattice cosets:

   \[
   \boxed{|2A-LA|\ge
          \sum_C |2A_C-LA_C|},
   \qquad A_C=T(A_0\cap C).
   \]

Thus a failure of cubic support cannot hide in a generic low-index affine
model.  It must concentrate polynomially many points in a translate of a
quarter-turn-stable lattice, where—after a similarity and translation—it
is literally a smaller instance of the original square-lattice problem.
This is an exact spread-versus-Gaussian-core dichotomy.  It is not yet a
solution: the concentrated branch recursively returns to the hard problem.

## 2. Exact resonance occupancy identity

The resonance lattice is stable under `R`:

\[
 z\in\Gamma
 \Longrightarrow Rz\in\mathbb Z^2,
 \qquad R(Rz)=-z\in\mathbb Z^2,
\]

so `Rz in Gamma`.  Applying the same argument to `-R` gives

\[
 R\Gamma=\Gamma.                                      \tag{2.1}
\]

Recall that

\[
 H=|((A_0-A_0)\setminus\{0\})\cap\Gamma|.
\]

Vector-Sidonicity says that every nonzero difference of `A_0` has one
ordered representation.  A difference belongs to `Gamma` exactly when its
two endpoints lie in the same `Gamma`-coset.  Therefore

\[
 \boxed{H=\sum_C k_C(k_C-1).}                    \tag{2.2}
\]

In particular, for `h=max_C k_C`,

\[
 H\le k(h-1).                                    \tag{2.3}
\]

Insert (2.3) into the exact collision estimate

\[
 |2A-LA|\ge
 {k^6\over 2k^3-k^2+H(k^2+k-1)}.
\]

Since `k^2+k-1<=2k^2`, its denominator is at most

\[
 2k^3+2k^3(h-1)=2hk^3.
\]

This proves

\[
 \boxed{|2A-LA|\ge {k^3\over2h}.}               \tag{2.4}
\]

Consequently `h=k^(o(1))` already gives `|2A-LA|=k^(3-o(1))`.
Conversely, any power-scale failure of cubic support forces a
polynomially large resonance coset.

## 3. Every concentrated coset is a Gaussian-lattice core

Equation (2.1) gives

\[
 J\Lambda=JT\Gamma=TR\Gamma=T\Gamma=\Lambda.    \tag{3.1}
\]

Identify the Euclidean plane with `C`, so that `J` is multiplication by
`i`.  Then `Lambda` is a rank-two discrete `Z[i]`-submodule of `C`, hence a
fractional Gaussian ideal.  Since `Z[i]` is a principal ideal domain,

\[
 \Lambda=\alpha\mathbb Z[i]                     \tag{3.2}
\]

for some nonzero complex `alpha`.  Multiplication by `alpha` is a rotation
and dilation.  It preserves all distance equalities.

It follows that any piece `A_C` contained in a translate of `Lambda`
becomes, after translation and similarity, an ordinary distance-Sidon
subset of `Z^2`.  The low-index concentrated branch is therefore not a new
approximate-group geometry; it is the original Gaussian-lattice hard core.

## 4. Internal supports of distinct cosets are disjoint

Choose a representative `x_C in Z^2` for a nonempty coset `C`.  If
`a,b,c in x_C+Gamma`, then

\[
 a+b-(I+R)c\in (I-R)x_C+\Gamma,                 \tag{4.1}
\]

using `R Gamma=Gamma`.  Hence the internal physical support

\[
 S_C:=2A_C-LA_C
\]

lies in the single `Lambda`-coset

\[
 T(I-R)x_C+\Lambda.                             \tag{4.2}
\]

Suppose the output cosets belonging to `C` and `C'` agree.  Then

\[
 (I-R)(x_C-x_{C'})\in\Gamma.                    \tag{4.3}
\]

In particular the left side is integral.  Since `x_C-x_C'` is integral as
well,

\[
 R(x_C-x_{C'})
 =(x_C-x_{C'})-(I-R)(x_C-x_{C'})\in\mathbb Z^2.
\]

Thus `x_C-x_C' in Gamma`, so `C=C'`.  The map from input resonance
cosets to output `Lambda`-cosets is injective.

Different `Lambda`-cosets are disjoint, so every point of the union of the
internal supports belongs to exactly one `S_C`.  Since that union is a
subset of the full support,

\[
 \boxed{|2A-LA|\ge\left|\bigcup_CS_C\right|
       =\sum_C|S_C|.}                            \tag{4.4}
\]

No incidence estimate or multiplicity loss is hidden in this aggregation.

## 5. Strategic meaning and remaining gap

The affine support attack now has a clean exact dichotomy.

- **Spread branch.**  If every resonance coset has subpolynomial
  occupancy, (2.4) proves cubic support.
- **Concentrated branch.**  A polynomially large piece lies in a translate
  of a Gaussian lattice.  Equation (4.4) allows the internal supports of
  all such pieces to be aggregated with no loss.

What is still missing is a density increment that wins when one or more
Gaussian cores are large.  Applying only a hypothetical quadratic bound
inside each core and summing (4.4) reproduces a quadratic bound, not a
cubic one.  A successful induction must gain from the interaction between
the core size, its lattice scale/index, and the ambient endpoint set.  The
adaptive seven-incidence charge and the complete-difference Fourier lower
bound are the two current mechanisms that retain this missing ambient
information.
