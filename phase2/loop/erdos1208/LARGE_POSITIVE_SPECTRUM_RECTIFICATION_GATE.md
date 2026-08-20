# Large positive spectrum and the limit of additive Sidon rectification

## 1. Outcome

Let

\[
 A\subset [0,m]^2\cap\mathbb Z^2,\qquad |A|=k,
\]

be distance-Sidon.  Write

\[
 F(\theta)=\sum_{a\in A}e(a\cdot\theta),\qquad
 P(\theta)=|F(\theta)|^2
\]

on `T^2`, and put

\[
 D^*=(A-A)\setminus\{0\},\qquad
 S(\theta)=\widehat{1_{D^*}}(\theta).
\]

Distance-Sidonicity implies vector-Sidonicity, so every nonzero oriented
difference has multiplicity one and

\[
 \boxed{P=k+S.}                                  \tag{1.1}
\]

The useful new point is that the entire sixth-moment problem lives on the
**large positive spectrum**:

\[
 \boxed{
 \left|
   T(D^*)-\int_{\{S>k\}}S(\theta)^3\,d\theta
 \right|<k^3,}                                  \tag{1.2}
\]

where

\[
 T(D^*)=\#\{(d_1,d_2,d_3)\in(D^*)^3:
                       d_1+d_2+d_3=0\}.
\]

Thus neither the negative spectrum nor the medium positive spectrum needs
any geometry.  Up to the already acceptable `O(k^3)` term, the desired
ambient third-energy estimate is exactly

\[
 \int_{\{S>k\}}S^3
 \le m^{o(1)}(k^3+m^2).                         \tag{1.3}
\]

Equivalently, it is a size-biased large-spectrum theorem above
`|F|^2>2k`.  Section 3 gives the exact finite-torus/dyadic version.

This is a rigorous reduction, not a proof of (1.3).  Section 5 proves a
sharp barrier: after ordinary Freiman rectification, the set is merely a
sparse one-dimensional Sidon set, and such sets can have third energy
`Omega(k^4)` even inside an interval of length `O(k^2)`.  Therefore known
Fourier-uniformity theorems for *extremal* interval Sidon sets, or an
abstract higher-energy theorem for Sidon sets, cannot close (1.3).  A proof
must retain the Euclidean norm injectivity together with the height `m`.

## 2. Exact positive-tail theorem

Because `D^*` is symmetric, `S` is real.  Equation (1.1) and positivity of
`P` give

\[
 -k\le S\le k(k-1).                             \tag{2.1}
\]

Fourier orthogonality and `|D^*|=k(k-1)` give

\[
 \int S=0,\qquad
 \int S^2=k(k-1),\qquad
 \int S^3=T(D^*).                               \tag{2.2}
\]

On the complement of `{S>k}`, (2.1) says `|S|<=k`.  Hence

\[
 \left|\int_{\{S\le k\}}S^3\right|
 \le k\int S^2
 =k^2(k-1)<k^3,                                 \tag{2.3}
\]

which proves (1.2).

Expanding `P^3` also gives the exact identity

\[
 \boxed{
 E_3^+(A):=\int P^3
 =4k^3-3k^2+T(D^*).}                            \tag{2.4}
\]

Consequently (1.3) is equivalent, up to an additive `O(k^3)`, to

\[
 E_3^+(A)\le m^{o(1)}(k^3+m^2),                \tag{2.5}
\]

the ambient equal-centroid gate in
`AMBIENT_THIRD_ENERGY_CENTROID_GATE.md`.

The threshold in (1.2) is forced naturally by positivity: below it the
lower bound `S>=-k` makes the cubic absolutely controlled by the known
quadratic moment.  Any positive trigonometric-polynomial argument that uses
only `P>=0`, `int S^2=k(k-1)`, and the support size has no leverage left
beyond (1.2).

## 3. Exact finite-torus rectification and dyadic gate

Translate `A` into `[0,m]^2`.  Let `Q>3m` be an integer and regard `A` as a
subset of

\[
 G=(\mathbb Z/Q\mathbb Z)^2.
\]

One may take `Q=3m+1`, so the finite ambient group has order `Theta(m^2)`;
no prime modulus is needed.

No equality of two threefold sums wraps modulo `Q`: the difference in each
coordinate lies in `[-3m,3m]`.  Therefore, with the unnormalised finite
Fourier transform,

\[
 \boxed{
 E_3^+(A)=Q^{-2}\sum_{\xi\in\widehat G}
                  |\widehat{1_A}(\xi)|^6.}      \tag{3.1}
\]

The same no-wrap observation applies to triples of differences.  Put

\[
 S_Q(\xi)=|\widehat{1_A}(\xi)|^2-k.
\]

Then all identities in (2.2)--(2.4), and the positive-tail theorem (1.2),
hold exactly with torus integrals replaced by `Q^(-2)` times finite sums.

For `j>=0`, define

\[
 \Omega_j=
 \{\xi:2^jk<S_Q(\xi)\le 2^{j+1}k\}.            \tag{3.2}
\]

Only `O(log k)` levels are nonempty, and

\[
 {k^3\over Q^2}\sum_j2^{3j}|\Omega_j|
 < {1\over Q^2}\sum_{S_Q>k}S_Q^3
 \le {8k^3\over Q^2}\sum_j2^{3j}|\Omega_j|.   \tag{3.3}
\]

Thus the exact missing theorem is

\[
 \boxed{
 \sum_j2^{3j}|\Omega_j|
 \le m^{o(1)}Q^2\left(1+{m^2\over k^3}\right).}       \tag{3.4}
\]

Equivalently up to logarithms, one needs the levelwise estimate

\[
 \boxed{
 |\Omega_j|
 \le m^{o(1)}{Q^2(k^3+m^2)\over 2^{3j}k^3}.}   \tag{3.5}
\]

The known second moment gives only

\[
 |\Omega_j|< {Q^2\over2^{2j}}.                 \tag{3.6}
\]

It does prove (3.5) in the low part

\[
 2^j\lesssim1+{m^2\over k^3},                  \tag{3.7}
\]

but loses the factor `2^j/(1+m^2/k^3)` above that.  In the critical regime
`k asymp m^(2/3)`, every genuinely high dyadic band remains.  Formula (3.4)
is therefore a precise harmonic restatement of the outstanding geometric
problem, not a consequence of the fourth moment.

## 4. What Euclidean structure is still visible in frequency space

Distance-Sidonicity says more than additive Sidonicity:

\[
 d,d'\in D^*,\quad |d|^2=|d'|^2
 \quad\Longrightarrow\quad d'=\pm d.           \tag{4.1}
\]

In particular, `D^*` is a symmetric radial transversal and is the complete
difference set of one endpoint set.  The first property alone is
insufficient by `RADIAL_ADDITIVE_TRIPLE_AUDIT.md`; the completeness alone is
insufficient by Section 5 below.  A proof of (3.4) has to use both at once.

One useful way to phrase the remaining input is:

> If a complete difference polynomial `S=|F|^2-k` of a height-`m`
> distance-Sidon set is unusually positive on many finite frequencies, then
> radial injectivity must force a size-biased loss in the count of those
> frequencies.

This is strictly narrower than uniform Fourier decay.  Low frequencies near
zero necessarily have `|F|` close to `k`; only their total measure, together
with all other large-spectrum components, needs the weighted bound (3.4).

## 5. Sparse interval Sidon sets are a sharp barrier

Ordinary Freiman rectification preserves exactly the additive quantity in
(2.5), but loses (4.1).  The loss is fatal.

### Proposition 5.1 (exact base encoding)

Let `X subset [0,m]^2` and take an integer `B>3m`.  The map

\[
 \phi_B(x,y)=x+By                              \tag{5.1}
\]

preserves all equalities between sums of at most three points.  Indeed, an
equality after applying `phi_B` has the form

\[
 \Delta_x+B\Delta_y=0,qquad |\Delta_x|\le3m.
\]

Since `B>3m`, this forces `Delta_x=Delta_y=0`.  In particular, vector-Sidon
sets map to one-dimensional Sidon sets and

\[
 E_3^+(\phi_B(X))=E_3^+(X).                    \tag{5.2}
\]

Choosing `B=3m+1`, the image lies in an interval of length `O(m^2)`.

### Proposition 5.2 (the interval theorem one would need is false)

For every odd prime `p`, take least residues

\[
 P_p=\{(x,[x^2]_p):0\le x<p\}\subset[0,p-1]^2. \tag{5.3}
\]

This is vector-Sidon.  Its `p^3` ordered triples have at most
`(3p-2)^2<9p^2` exact sums, so Cauchy--Schwarz gives

\[
 E_3^+(P_p)>{p^4\over9}.                       \tag{5.4}
\]

For completeness, equality of two nonzero oriented differences, reduced
modulo `p`, gives

\[
 x-y=u-v\ne0,qquad
 (x-y)(x+y)=(u-v)(u+v).
\]

Thus `x+y=u+v`; since `p` is odd, the two ordered endpoint pairs agree
modulo `p`, and hence as least residues.  This proves the asserted
vector-Sidonicity.

Take `B=3p` in (5.1).  Then

\[
 S_p=\phi_B(P_p)\subset[0,(3p+1)(p-1)]
\]

is a one-dimensional Sidon set with `|S_p|=p` and

\[
 E_3^+(S_p)>{p^4\over9}.                       \tag{5.5}
\]

Thus a universal estimate

\[
 E_3^+(S)\lesssim |S|^{3+o(1)}+N^{1+o(1)}
 \quad(S\subset[N]\text{ Sidon})               \tag{5.6}
\]

is false by a polynomial factor: here `N=O(p^2)`, while the left side is
`Omega(p^4)`.

This also explains why the standard interval-Sidon literature does not
close the live problem.  Ortega--Prendiville's Fourier-uniformity theorem
([arXiv:2110.13447](https://arxiv.org/abs/2110.13447), Theorem 6.3) is
effective for extremal Sidon sets of size close to `N^(1/2)`.  In the live
range, base encoding has `N=Theta(m^2)` and
`k around m^(2/3)=N^(1/3)`, far from extremality.  The parabola family above
shows this is a real obstruction, not just a mismatch in stated
hypotheses.  Shkredov's general higher-energy inverse theory
([arXiv:2103.14670](https://arxiv.org/abs/2103.14670)) likewise does not
retain radial norm injectivity or supply (3.4).

The generic integral shear in `THIRD_ADDITIVE_ENERGY_BARRIER.md` can make
the parabola distance-Sidon while preserving its large third energy, but it
also increases the containing height; the `m^2` term then pays.  This is
exactly the tradeoff that a successful proof of (3.4) must quantify.

## 6. Verified claims and next gate

Run

```text
python3 phase2/loop/erdos1208/verify_large_positive_spectrum_rectification_gate.py
```

The verifier uses exact integer arithmetic for:

1. vector- and distance-Sidon examples;
2. the complete-difference identities (1.1), (2.2), and (2.4), interpreted
   by convolution counts;
3. exact finite-torus rectification for `Q>3m`;
4. the base-encoding preservation of two- and three-sum fibres;
5. the finite-field parabola's `Omega(k^4)` third energy inside an interval
   of length `O(k^2)`.

It also samples the real torus to adversarially check the pointwise bounds
used in (1.2) and the dyadic inequalities (3.3).  The exact remaining gate
is (3.4), with (4.1) and complete endpoint realization retained.
