# Fixed-alphabet local collision gadgets have zero norm-channel entropy

## Outcome

Consider the surviving carry-free consecutive-scale model

\[
 \Phi_r(x)=\sum_{j<r}B_r^jx_j,
 \qquad x_j\in P\subset\mathbb Z[i],               \tag{1.1}
\]

with `P` fixed and `B_r` above the coefficient-carry threshold.  Equal
Euclidean distances are then exactly equal Gaussian polynomial norms

\[
 F\bar F=G\bar G,
 \qquad F,G\in(P-P)[z].                            \tag{1.2}
\]

This note closes one proposed recursive lane: a finite local
distance-collision gadget cannot be repeated independently with positive
Shannon entropy.

There are three exact statements.

1. A nontrivial equal-norm block collision does not survive an arbitrary
   common suffix.  Universal suffix composition forces the two block
   displacements to be identical.  If the suffix is allowed to change, the
   only universal alternatives are applying one common planar isometry to
   both the block and the suffix.
2. More generally, every fixed-alphabet finite-state family of distinct
   difference words in one norm fibre has zero topological entropy.  A
   positive-entropy local rewrite system would contradict the established
   subexponential Gaussian norm-fibre theorem.
3. High additive energy survives only as endpoint translation multiplicity.
   Every distance-colour graph is the union of subexponentially many
   translation path forests, and every path has bounded length depending
   only on `P`.  A colour may nevertheless contain exponentially many
   disjoint short components.  That global component-packing problem is not
   closed by this note.

Thus a SAT search over a small planar gadget cannot justify a recursive
upper exponent by multiplying its local equal-distance alternatives.  A
successful high-energy construction must coordinate endpoint translations
globally across blocks, use positive-entropy carries, or let the alphabet
grow.  This is a rigorous barrier, not a new construction and not a full
no-go for all fixed high-energy languages.

## 1. Exact suffix expansion

For a Gaussian polynomial `F`, write

\[
 N(F)=F\bar F,
\]

where conjugation acts on coefficients and fixes `z`.  If `L` exceeds the
degrees of `F` and `H`, then

\[
 N(F+z^LH)
 =N(F)+z^L(F\bar H+\bar F H)+z^{2L}N(H).           \tag{2.1}
\]

The middle term is the planar cross term that a local distance-colour
gadget does not record.

### Theorem 1 (common-suffix rigidity)

Suppose `N(F)=N(G)`.  If

\[
 N(F+z^LH)=N(G+z^LH)                               \tag{2.2}
\]

holds for both constant suffixes `H=1` and `H=i`, then `F=G`.

### Proof

Put `D=F-G`.  Cancelling the equal block norms and the common suffix norm in
(2.1), equation (2.2) becomes

\[
 D\bar H+\bar D H=0.                               \tag{2.3}
\]

Write `D=A+iC` with `A,C in Z[z]`.  For `H=1`, (2.3) gives `2A=0`.  For
`H=i`, it gives `2C=0`.  Hence `A=C=0`.  `QED`

The same argument works with any two constant suffix directions which span
the real plane.  Therefore a noncollinear digit language need not literally
contain the digits `1` and `i`; two independent realized suffix differences
are enough after an invertible real change of the two equations.

### Theorem 2 (isometry-twisted suffix rigidity)

Let `epsilon` be a Gaussian unit.

* The identity

  \[
   N(F+z^LH)=N(G+z^L\epsilon H)                    \tag{2.4}
  \]

  holds for every `H` if and only if `G=epsilon F`.
* The identity

  \[
   N(F+z^LH)=N(G+z^L\epsilon\bar H)                \tag{2.5}
  \]

  holds for every `H` if and only if
  `G=epsilon bar(F)`.

### Proof

In (2.4), compare the coefficients of `H` and `bar(H)` in the middle term
of (2.1).  They give

\[
 G\bar\epsilon=F,
 \qquad \bar G\epsilon=\bar F,
\]

equivalent to `G=epsilon F`.  The norm terms then agree automatically.  In
(2.5), the same comparison gives

\[
 G\bar\epsilon=\bar F,
 \qquad \bar G\epsilon=F,
\]

equivalent to `G=epsilon bar(F)`.  The converse directions are ordinary
rotation/reflection invariance of the Euclidean norm.  `QED`

Theorems 1--2 isolate the only genuinely context-free composition rule:
one global orthogonal map must act on the entire displacement polynomial.
Independent local choices of different orthogonal maps reintroduce the
cross terms in (2.1).

## 2. Positive-entropy collision rewrites are impossible

Let `Delta=P-P`.  The fixed-alphabet norm-fibre theorem in
`GAUSSIAN_POLYNOMIAL_NORM_FIBRE_SQRT_EXTRACTION.md` says that, uniformly in
nonzero `F in Delta[z]` of degree below `r`,

\[
 \#\{G\in\Delta^r:N(G)=N(F)\}
 \le R_r
 =\exp\bigl(O_P(r^{2/3}\log r)\bigr)
 =\exp(o(r)).                                       \tag{3.1}
\]

This immediately has a Shannon-capacity consequence which is useful when
designing finite gadgets.

### Theorem 3 (zero norm-channel entropy)

Let `W_r(F)` be any family of distinct length-`r` difference words produced
from a seed `F` by a block rewrite system, a finite-state transducer, an SFT,
or any other rule whatsoever, provided every output satisfies
`N(G)=N(F)`.  Then

\[
 \limsup_{r\to\infty}
 \frac1r\log|W_r(F)|=0.                            \tag{3.2}
\]

In particular, there cannot be a fixed block length `ell` and `b>=2`
independent norm-preserving choices in each block: those would give

\[
 |W_r(F)|\ge b^{\lfloor r/\ell\rfloor},             \tag{3.3}
\]

contradicting (3.1).

### Proof

Every output belongs to the norm fibre in (3.1), so
`|W_r(F)|<=R_r`; divide its logarithm by `r`.  `QED`

The theorem permits polynomially or subexponentially many global Gaussian
factor reallocations.  It rules out precisely the exponential multiplication
needed for a fixed local collision gadget to improve an exponent through a
naive Shannon-capacity product.

## 3. Exact endpoint-translation residual

Theorem 3 counts distinct displacement words.  High additive energy instead
creates many endpoint pairs with the **same** displacement.  The following
decomposition shows exactly what remains.

For a language `C_r subset P^r` and a directed difference word `d`, let
`T_d` be the undirected graph on `C_r` whose edges have displacement `d` or
`-d`.  Define

\[
 \ell(P)=\max\{t+1:
   a,a+v,\ldots,a+tv\in P,
   \ a,v\in\mathbb Z[i],\ v\ne0\}.               \tag{4.1}
\]

Since `P` is fixed, `ell(P)` is a constant.

### Theorem 4 (short translation-path decomposition)

Every component of `T_d` is a path on at most `ell(P)` vertices.  If `c` is
a nonzero Euclidean distance colour, its colour graph is the union of at
most `R_r` such translation path forests:

\[
 G_c=\bigcup_{d:N(d)=c}T_d.                        \tag{4.2}
\]

### Proof

Translation by a nonzero vector in the torsion-free group
`Z[i]^r` has no cycles, and every vertex has at most one predecessor and one
successor.  Thus `T_d` is a path forest.  On a component

\[
 x,x+d,\ldots,x+td,
\]

choose a coordinate `j` with `d_j != 0`.  Then

\[
 x_j,x_j+d_j,\ldots,x_j+td_j
\]

is an arithmetic progression in `P`, so `t+1<=ell(P)`.  Equation (4.2) is
the definition of a colour fibre, and (3.1) bounds the number of its
distinct difference words.  `QED`

The number of components of one `T_d` can still be exponential in `r`.
For the full product it is essentially the endpoint multiplicity

\[
 \rho_r(d)=\prod_j\rho_P(d_j),                     \tag{4.3}
\]

which is exactly where high additive energy enters.  Therefore bounded
path length and subexponential channel count do not themselves prove a
square-root extraction theorem.  The surviving problem is to coordinate
the exponentially many short translation components across different
`d` and different norm colours.

## 4. Exact high-energy stress: the binary square

Take

\[
 P_\square=\{0,1,i,1+i\}.                          \tag{5.1}
\]

Its additive energy is

\[
 E^+(P_\square)=36>4^{5/2}=32,                    \tag{5.2}
\]

so it is the smallest natural noncollinear alphabet lying beyond the
low-energy extraction theorem.  It also demonstrates why a local rainbow
number cannot simply be exponentiated.

Let `M_r` be the maximum size of a distance-Sidon subset of
`P_square^r` under the coefficient-separated Gaussian norm colouring.  An
exact exhaustive calculation gives

\[
 M_1=2,
 \qquad M_2=5>2^2.                                 \tag{5.3}
\]

Thus even at two blocks, the local obstruction is supermultiplicative.  A
one-block SAT gadget with rainbow number two does not certify a capacity
base of two.  The five-word witness is

\[
\begin{split}
 &(1+i,1+i),\ (1+i,i),\ (i,1),\\
 &(1,0),\ (0,1).
\end{split}                                        \tag{5.4}
\]

The verifier checks all ten polynomial squared distances in (5.4) and
exhaustively rules out a six-word subset of the sixteen two-block words.
For this alphabet `ell(P_square)=2`; the high-energy multiplicity is entirely
in the number of disjoint translation edges, not in long components.

As a second stress, the cross alphabet

\[
 P_+=\{0,1,-1,i,-i\}                               \tag{5.5}
\]

has `ell(P_+)=3`.  Exhaustive translation-graph checks through three product
levels attain neither cycles nor a component longer than three, exactly as
Theorem 4 predicts.

## 5. A concrete non-isometric factor reallocation

To distinguish Theorem 1 from a claim that all equal norms are global
isometries, take

\[
 A=1+iz,
 \qquad B=1+(1+i)z,
\]

and put

\[
 U=AB,
 \qquad V=A\bar B.                                 \tag{6.1}
\]

Then

\[
 N(U)=N(A)N(B)=N(V),                               \tag{6.2}
\]

but `V` is neither a unit multiple of `U` nor a unit multiple of `bar(U)`.
Direct expansion gives

\[
 U=1+(1+2i)z+(-1+i)z^2,
 \qquad
 V=1+z+(1+i)z^2.                                   \tag{6.3}
\]

Appending the same constant suffix `1` or `i` beyond this block breaks the
norm equality in both cases.  This is the simplest explicit regression test
for the cross term that a local colour-only tensor model misses.

## 6. Verification and research consequence

Run

```bash
python3 phase2/loop/erdos1208/verify_fixed_alphabet_local_collision_capacity_no_go.py
```

The verifier checks Gaussian polynomial multiplication and conjugation,
(6.2)--(6.3), exclusion of all eight global unit/conjugate isometries,
failure under the two common suffixes, successful composition under a
single global rotation or reflection, (5.2), the exact rainbow maxima in
(5.3), the witness (5.4), and every translation component for the square
and cross alphabets through three product levels.

This changes the recommended search target.  Do not score a finite gadget by
its one-block distance-colour classes or multiply its local rainbow number.
For every candidate, retain the full displacement polynomial and test its
cross term against all reachable suffix states.  A finite-state search is
potentially meaningful only if it controls endpoint translation components
globally; a positive-entropy norm-preserving displacement automaton is
impossible by Theorem 3.
