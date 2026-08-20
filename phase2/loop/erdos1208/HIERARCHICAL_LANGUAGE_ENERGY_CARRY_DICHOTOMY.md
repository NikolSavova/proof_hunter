# Hierarchical digit languages: energy extraction and the carry dichotomy

## 1. Outcome

The square-root extraction theorem in
`GAUSSIAN_POLYNOMIAL_NORM_FIBRE_SQRT_EXTRACTION.md` was stated for a fixed
Cartesian power `P^r` with `E+(P)<|P|^(5/2)`.  Neither fixedness nor the
Cartesian product is essential.

This note proves three extensions.

1. **Arbitrary non-product languages.**  If `C_r` is any set of digit words
   and its additive energy is at most `|C_r|^(5/2-eta)`, then a carry-free
   consecutive-scale embedding contains a distance-Sidon subset of size
   `|C_r|^(1/2-o(1))`.
2. **Slowly growing alphabets.**  The Gaussian polynomial norm fibres remain
   subexponential when the coefficient height grows as

   \[
   \log H_r=o\!\left(
      \frac{r(\log\log r)^3}{(\log r)^4}
   \right).                                         \tag{1.1}
   \]

3. **Structured carries.**  The same conclusion survives whenever the
   number of norm polynomials collapsed onto one evaluated distance by the
   carry mechanism is subexponential.  Thus a successful carry construction
   needs exponentially many genuine carry alternatives.  The canonical
   complete Gaussian digit system has that kind of high-energy behavior, but
   its image is exactly the ordinary square grid; it is not a new hierarchical
   construction.

This is a broad no-go theorem, not a construction resolving Erdos #1208.
It leaves a sharply delimited survivor: a language with near-`5/2` additive
energy together with exponential carry entropy (or coefficient height beyond
(1.1)).

## 2. Setup

Let `P_r` be a finite subset of the Gaussian integers contained in the disk
`|z|<=H_r`, and let

\[
 C_r\subseteq P_r^r,
 \qquad n_r=|C_r|.
\]

For a word `x=(x_0,...,x_(r-1))`, put

\[
 \Phi_r(x)=\sum_{j<r}B_r^jx_j.                     \tag{2.1}
\]

First suppose

\[
 B_r>16rH_r^2+2.                                   \tag{2.2}
\]

For an ordered edge `(x,y)`, its difference word is `d=x-y`, and

\[
 F_d(z)=\sum_{j<r}d_jz^j.
\]

Every coefficient of `F_d bar(F_d)` has absolute value at most `4rH_r^2`.
The leading-coefficient argument in the earlier note therefore gives

\[
 \|\Phi_r(x)-\Phi_r(y)\|^2
 =\|\Phi_r(x')-\Phi_r(y')\|^2
 \iff
 F_{x-y}\overline{F_{x-y}}
 =F_{x'-y'}\overline{F_{x'-y'}}.                   \tag{2.3}
\]

No product structure is used in (2.3).

Define the directed difference multiplicity and additive energy of the
language by

\[
 \rho_C(d)=|\{(x,y)\in C_r^2:x-y=d\}|,
 \qquad
 E^+(C_r)=\sum_d\rho_C(d)^2.                       \tag{2.4}
\]

## 3. Growing-height Gaussian norm fibres

### Theorem 3.1

Let `Delta_r` be contained in the Gaussian disk of radius `2H_r`.  Uniformly
over every nonzero polynomial

\[
 F(z)=\sum_{j<r}d_jz^j,qquad d_j\in\Delta_r,
\]

the number `R_r` of Gaussian polynomials `G` of degree below `r` satisfying

\[
 G\bar G=F\bar F
\]

obeys

\[
\begin{split}
 \log R_r\ll{}&r^{2/3}\log r+\log H_r\\
 &+\log(H_r\sqrt r)
   \left(\frac{\log r}{\log\log r}\right)^3\log r. \tag{3.1}
\end{split}
\]

In particular, (1.1) implies `R_r=exp(o(r))`.

### Proof

Remove the Gaussian content of `F` and factor the primitive part in the UFD
`Z[i][z]`.  As before, a non-self-conjugate irreducible orbit of total
exponent `N` can be allocated between `G` and `bar G` in at most `N+1`
ways, while a self-conjugate exponent is forced.  The Gaussian content has
at most `O(H_r^2)` possible associates of the required norm, contributing
only `O(log H_r)` to the logarithm of the fibre size.

The Mahler measure satisfies

\[
 M(F)\le\|F\|_2\le 2H_r\sqrt r.                    \tag{3.2}
\]

Put `D=r^(1/3)`.  The number `K` of distinct non-self-conjugate factor
orbits is bounded as follows.

* Factors of degree greater than `D`: `O(r/D)=O(r^(2/3))`.
* Cyclotomic factors of degree at most `D`: `O(D^2)=O(r^(2/3))`, using
  `phi(m)>=c sqrt(m)` and the fact that a rational cyclotomic polynomial
  has at most two factors over `Q(i)`.
* Noncyclotomic factors of degree at most `D`: Dobrowolski's lower bound and
  multiplicativity of Mahler measure give

  \[
   O\!\left(\log(H_r\sqrt r)
       \left(\frac{\log r}{\log\log r}\right)^3\right). \tag{3.3}
  \]

Thus `K` is bounded by the sum of these quantities.  Since the total factor
exponent is at most `2r`, AM--GM gives

\[
 \prod_{\mathcal O}(N_{\mathcal O}+1)
 \le\left(1+\frac{2r}{K}\right)^K.                \tag{3.4}
\]

Using `log(1+2r/K)<=log(3r)` in (3.4), and restoring the content, proves
(3.1).  Under (1.1) every term on its right is `o(r)`.  QED

The only non-elementary input is the same Dobrowolski theorem cited in the
fixed-alphabet note.  The argument also shows that it is coefficient height,
not alphabet cardinality by itself, that controls the growing-alphabet
extension.

## 4. Arbitrary-language extraction

### Theorem 4.1

Assume (2.2), (1.1), and

\[
 \log n_r=\Omega(r),
 \qquad
 E^+(C_r)\le n_r^{5/2-\eta}                       \tag{4.1}
\]

for some fixed `eta>0`.  Then the planar set `Phi_r(C_r)` contains a
distance-Sidon subset of size

\[
 \boxed{n_r^{1/2-o(1)}}.                           \tag{4.2}
\]

### Proof

Let `D_c` be the set of nonzero difference words whose Gaussian norm
polynomial is the color `c`.  Theorem 3.1 gives `|D_c|<=R_r`.  If

\[
 m_c=\sum_{d\in D_c}\rho_C(d)
\]

is the ordered multiplicity of the distance color, Cauchy--Schwarz and the
partition of the difference words into norm fibres give the exact bound

\[
 \sum_cm_c^2
 \le R_r\sum_d\rho_C(d)^2
 =R_rE^+(C_r).                                     \tag{4.3}
\]

At a fixed vertex and color, every neighbor gives a different difference
word in `D_c`; hence every color-degree is at most `R_r`.  The number of
three-vertex isosceles obstructions is therefore at most

\[
 \frac12R_rn_r(n_r-1).                             \tag{4.4}
\]

Up to an absolute orientation constant, (4.3) bounds the number of
four-vertex equal-distance obstructions by `R_rE+(C_r)`.

Retain vertices independently with probability

\[
 p=\frac{\epsilon}{\sqrt{R_rn_r}}.
\]

The expected retained vertex count is `epsilon sqrt(n_r/R_r)`.  Relative
to it, the expected three- and four-vertex obstruction counts are at most

\[
 O(\epsilon^2),
 \qquad
 O\!\left(
   \epsilon^3\frac{E^+(C_r)}{\sqrt{R_r}n_r^{5/2}}
 \right).                                         \tag{4.5}
\]

The second expression tends to zero by (4.1), while `R_r=exp(o(r))` and
`log n_r=Omega(r)` imply `R_r=n_r^{o(1)}`.  Choose `epsilon` as a sufficiently
small fixed constant and delete one vertex from every surviving obstruction.
This leaves (4.2).  QED

The proof is completely insensitive to how `C_r` is defined.  It covers
finite-state restrictions, forbidden-block languages, constant-composition
codes, and globally coupled algebraic codes whenever their actual additive
energy satisfies (4.1).

For the full product `C_r=P^r`, identity

\[
 E^+(P^r)=E^+(P)^r
\]

recovers the earlier threshold.  For a high-energy fixed alphabet, a
non-product restriction only remains a candidate if it retains energy
`n_r^(5/2-o(1))`; merely abandoning the Cartesian product is not enough.

## 5. Carries

For a base below the separation threshold, define its norm-polynomial carry
ambiguity by

\[
 \kappa_r=max_s
 \left|\left\{Q=F_d\bar F_d:
      d\in C_r-C_r,\ Q(B_r)=s\right\}\right|.      \tag{5.1}
\]

The set counts **distinct norm polynomials**, not endpoint pairs.  A scalar
distance fibre is a union of at most `kappa_r` polynomial norm fibres, so
every use of `R_r` in Section 4 may be replaced by

\[
 \widetilde R_r=\kappa_rR_r.                       \tag{5.2}
\]

### Corollary 5.1

Under (1.1) and (4.1), and assuming that `Phi_r` is injective on `C_r`,
Theorem 4.1 remains valid for a carrying evaluation whenever

\[
 \kappa_r=\exp(o(r)).                              \tag{5.3}
\]

Thus boundedly many global carry choices, polynomially many choices, and
any zero-entropy carry automaton do not evade square-root extraction.  A
successful structured-carry construction must create exponentially many
norm-polynomial alternatives for some scalar distances while simultaneously
maintaining endpoint energy near the `5/2` threshold.

For a coefficient-difference polynomial `h(z)=sum h_jz^j`, equality
`h(B)=0` is equivalent to the carry recurrence

\[
 c_0=0,\qquad h_j+c_j=Bc_{j+1}\quad(0\leq j<L),
 \qquad h_L+c_L=0.                                  \tag{5.4}
\]

where `L=deg h`.  Consequently (5.3) can be checked by counting admissible
paths in a finite carry graph.  Positive topological entropy is necessary
for escape.

## 6. The complete-digit carry model is exactly the square grid

Let

\[
 P_B=\{a+ib:0\le a,b<B\}.
\]

Ordinary base-`B` uniqueness gives the exact identity

\[
 \left\{\sum_{j<r}B^jx_j:x_j\in P_B\right\}
 =\{0,1,\ldots,B^r-1\}^2.                         \tag{6.1}
\]

Thus the most natural growing/high-energy alphabet with structured carries
does not define a new point set at all: it is the `B^r by B^r` square grid.
Moreover the digit map is bijective, so an arbitrary non-product restriction
`C_r subset P_B^r` is simply an arbitrary subset of that grid written in
base `B`.

This explains why complete digits evade the low-energy theorem without
already solving the problem.  Their survivor is exactly the known square-grid
core of Erdos #1208.  Proving that their largest distance-Sidon subset has
order `n^(1/3+o(1))` would be the desired grid theorem itself, not a free
hierarchical amplification.

## 7. Exact survivor and verification

The hierarchical construction program is now reduced to at least one of:

1. `E+(C_r)>=n_r^(5/2-o(1))` for the actual non-product endpoint language;
2. coefficient height violating (1.1); or
3. exponentially many norm-polynomial carry alternatives `kappa_r`.

The standard complete-digit example satisfies the hard alternatives by
collapsing to the square grid.  Any proposed new construction should report
all three quantities `(E+(C_r), H_r, kappa_r)`; base-alphabet collision
counts alone do not test the theorem.

Run

```bash
python3 phase2/loop/erdos1208/verify_hierarchical_language_energy_carry_dichotomy.py
```

The verifier checks the exact arbitrary-language energy identity and local
fibre bound on several non-product languages, coefficient separation at a
large base, scalar carry ambiguity at a small base, the carry recurrence,
and the complete-digit square-grid identity.
