# Consecutive-scale Gaussian norm fibres force square-root extraction

## 1. Outcome

Let `P` be a fixed finite subset of the Gaussian integers and, for every
`r`, embed the product `P^r` in the integer plane by

\[
 \Phi_r(x_0,\ldots,x_{r-1})=\sum_{j=0}^{r-1}B_r^j x_j,
 \qquad B_r>4r\max_{u,v\in P}|u-v|^2+2.             \tag{1.1}
\]

The consecutive exponents deliberately merge all Gram coefficients on the
same anti-diagonal.  This is the sole scale-collision lane left open by
`HIERARCHICAL_PLANAR_GRAM_RANK_NO_GO.md`.  It still does **not** give a
sub-square-root construction for a large and natural class of alphabets.

### Theorem A (subexponential Gaussian norm fibres)

Fix a finite `Delta subset Z[i]`.  If

\[
 F(z)=\sum_{j<r}d_jz^j,\qquad d_j\in\Delta,         \tag{1.2}
\]

is nonzero, then the number of coefficient words `e in Delta^r` satisfying

\[
 F_e(z)\overline{F_e}(z)=F(z)\overline F(z)         \tag{1.3}
\]

is at most

\[
 R_r=\exp\!\bigl(O_\Delta(r^{2/3}\log r)\bigr)
     =\exp(o(r)).                                   \tag{1.4}
\]

Here the bar conjugates coefficients and fixes `z`.  In fact (1.4) bounds
all Gaussian polynomials `G` of degree below `r` with `G bar(G)=F bar(F)`,
apart from a constant depending only on the possible Gaussian contents.

### Theorem B (energy criterion for square-root extraction)

Write `q=|P|` and

\[
 \rho_P(d)=|\{(a,b)\in P^2:a-b=d\}|,\qquad
 E^+(P)=\sum_d\rho_P(d)^2.                          \tag{1.5}
\]

If

\[
 E^+(P)<q^{5/2},                                    \tag{1.6}
\]

then the `n=q^r` points in (1.1) contain a subset of size

\[
 \boxed{n^{1/2-o(1)}}                               \tag{1.7}
\]

whose pairwise Euclidean distances are all distinct.

In particular the genuinely noncollinear alphabet

\[
 P=\{0,1,i\}                                        \tag{1.8}
\]

has `q=3` and

\[
 E^+(P)=3^2+6=15<3^{5/2}.                           \tag{1.9}
\]

Thus the most economical noncollinear consecutive-scale product contains
a distance-Sidon set of size `n^(1/2-o(1))`.  It cannot furnish the hoped-for
`n^(1/3+o(1))` upper construction for Erdos #1208.

This is a theorem about this hierarchical product lane, not a proof of
#1208.  It does not cover alphabets with `E^+(P)>=q^(5/2)`, alphabets growing
with `r`, or non-product/carrying encodings.

## 2. Exact reduction to a Gaussian polynomial norm

For an edge `x-y`, put

\[
 d_j=x_j-y_j,\qquad F_d(z)=\sum_{j<r}d_jz^j.        \tag{2.1}
\]

Then

\[
 \|\Phi_r(x)-\Phi_r(y)\|^2
   =F_d(B_r)\overline{F_d}(B_r).                    \tag{2.2}
\]

Every coefficient of `F_d bar(F_d)` is a rational integer of absolute
value at most

\[
 r\max_{u,v\in P}|u-v|^2.                          \tag{2.3}
\]

The difference of two such coefficient vectors is therefore strictly
smaller than `B_r` coefficientwise.  Reducing an equality at `B_r` modulo
`B_r`, and then dividing by `B_r`, proves successively that every
coefficient agrees.  Consequently

\[
 \boxed{\|\Phi_r(x)-\Phi_r(y)\|^2
 =\|\Phi_r(x')-\Phi_r(y')\|^2
 \iff F_{x-y}\bar F_{x-y}=F_{x'-y'}\bar F_{x'-y'}.} \tag{2.4}
\]

There is no hidden carry assumption beyond the explicit choice (1.1).

## 3. Proof of the norm-fibre theorem

Factor a nonzero `F` in the UFD `Z[i][z]`, first removing its Gaussian
content.  Conjugation acts on irreducibles.  For a non-self-conjugate orbit
`{pi,bar(pi)}`, suppose `pi` and `bar(pi)` occur in `F bar(F)` with their
common total exponent `N_pi`.  A solution `G bar(G)=F bar(F)` may put
`0,1,...,N_pi` copies on the `pi` side; its conjugate exponent is then
forced.  A self-conjugate irreducible has a forced exponent.  Hence

\[
 |\{G:G\bar G=F\bar F\}|
 \le C_\Delta\prod_{\mathcal O}(N_{\mathcal O}+1), \tag{3.1}
\]

where the product runs over the distinct non-self-conjugate irreducible
orbits occurring in `F bar(F)`.  The content contributes only `C_Delta`,
because a nonzero coefficient of `F` lies in the fixed finite set `Delta`.

It remains to show that the number `K` of orbits is `o(r)`.  The standard
Mahler-measure inequality gives

\[
 M(F)\le \|F\|_2\le C_\Delta\sqrt r.               \tag{3.2}
\]

We bound the distinct irreducible factors of `F` over `Q(i)` and then
double the answer.  Put `D=r^(1/3)`.

* Factors of degree greater than `D`: at most `r/D=O(r^(2/3))`.
* Cyclotomic factors of degree at most `D`: a cyclotomic polynomial over
  `Q` splits into at most two factors over `Q(i)`.  Such a factor coming
  from `Phi_m` has degree at least `phi(m)/2`.  The elementary lower bound
  `phi(m) >= c sqrt(m)` gives `m=O(D^2)`, hence `O(D^2)=O(r^(2/3))`
  possibilities.
* Noncyclotomic factors of degree at most `D`: a factor with nonunit leading
  coefficient has Mahler measure at least `sqrt(2)`.  For a monic factor,
  choose a root `alpha`.  Its minimal polynomial over `Q` has degree at most
  `2D` and Mahler measure at most the square of the factor's measure.
  Dobrowolski's theorem therefore gives

  \[
   \log M(f)\gg
   \left({\log\log(2D)\over\log(2D)}\right)^3       \tag{3.3}
  \]

  unless `alpha` is a root of unity.  Multiplicativity of Mahler measure
  and (3.2) bound the number of these factors by
  `O(log r (log D/log log D)^3)`.

Thus

\[
 K=O_\Delta\!\left(r^{2/3}
       +\log r\left({\log r\over\log\log r}\right)^3\right)
   =O_\Delta(r^{2/3}+\operatorname{polylog}r).       \tag{3.4}
\]

Also `sum_O N_O<=2r`.  Arithmetic-geometric mean in (3.1) now yields

\[
 \prod_{\mathcal O}(N_{\mathcal O}+1)
 \le \left(1+{2r\over K}\right)^K
 \le \exp(O_\Delta(r^{2/3}\log r)),                \tag{3.5}
\]

which proves Theorem A.

The only non-elementary input is Dobrowolski's lower bound.  The original
source is E. Dobrowolski, *On a question of Lehmer and the number of
irreducible factors of a polynomial*, Acta Arith. 34 (1979), 391--401,
DOI `10.4064/aa-34-4-391-401`.

## 4. From fibres and additive energy to a rainbow subset

For a difference word `d=(d_0,...,d_(r-1))`, the number of ordered ambient
edges with that difference is

\[
 \rho_r(d)=\prod_j\rho_P(d_j).                     \tag{4.1}
\]

If `c` is a nonzero norm-polynomial colour, let `D_c` be its difference
fibre and let

\[
 m_c=\sum_{d\in D_c}\rho_r(d)                      \tag{4.2}
\]

be its ordered edge multiplicity.  By Theorem A and Cauchy,

\[
 \sum_c m_c^2
 \le R_r\sum_d\rho_r(d)^2
 =R_r E^+(P)^r.                                    \tag{4.3}
\]

This bounds, up to an absolute constant, the number of pairs of disjoint
edges having the same distance.

For pairs of equal-coloured edges sharing a vertex, fix the vertex `x` and
colour `c`.  Every neighbour determines a distinct word `x-y in D_c`, so
the colour-degree at `x` is at most `R_r`.  Therefore the total number of
three-vertex isosceles obstructions is at most

\[
 {1\over2}R_r n(n-1).                              \tag{4.4}
\]

Retain each vertex independently with probability

\[
 p={\varepsilon\over\sqrt{R_rn}}.                  \tag{4.5}
\]

The expected numbers of retained vertices, three-vertex obstructions, and
four-vertex obstructions are at most

\[
 pn,qquad {1\over2}p^3R_rn^2,qquad
 C p^4R_rE^+(P)^r.                                 \tag{4.6}
\]

Relative to `pn`, the last two quantities are at most

\[
 {\varepsilon^2\over2},\qquad
 {C\varepsilon^3\over\sqrt{R_r}}
 \left({E^+(P)\over q^{5/2}}\right)^r.             \tag{4.7}
\]

Choose a fixed sufficiently small `epsilon`.  Under (1.6), the second
ratio tends exponentially to zero.  Some sample therefore has positive
`(#vertices - #bad triples - #bad quadruples)` of order `pn`; delete one
vertex from every remaining obstruction.  The result has all distances
distinct and size

\[
 \Omega(\sqrt{n/R_r})=n^{1/2-o(1)},                \tag{4.8}
\]

as claimed.

## 5. Exact finite certificate and scope

The verifier checks all finite algebra used above.  It also supplies a
nontrivial exact certificate at `r=6`: using

\[
 \mathbb F_{27}=\mathbb F_3[t]/(t^3+2t+1),
 \qquad \mathcal C=\{(x,x^2):x\in\mathbb F_{27}\}, \tag{5.1}
\]

and reading the six ternary coordinates as digits of `{0,1,i}`, all 351
pairwise polynomial norms on the resulting 27 words are distinct.  Thus
the 729-point triangle product already contains an exact square-root
distance-Sidon subset.

The durable conclusion is narrow but decisive for this construction
program:

1. Fully separated scales fail by global Gram rigidity.
2. Consecutive scales fail for every fixed alphabet satisfying the explicit
   energy condition (1.6), including the smallest noncollinear alphabet.
3. A surviving hierarchical upper construction must violate at least one
   theorem hypothesis: it needs a high-energy or growing alphabet, a
   non-product digit restriction, or arithmetic carries used as structure
   rather than avoided.
