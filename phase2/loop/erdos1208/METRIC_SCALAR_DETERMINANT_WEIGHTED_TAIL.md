# Determinant-decorated weighted tail: theorem and aligned obstruction

## 1. Outcome

Determinant decoration gives a rigorous nontrivial theorem:

* every fixed squared-distance-gap / doubled-area cell has Gaussian-divisor
  multiplicity `m^(o(1))`;
* the entire fibre-adaptive low-determinant part of the aggregate scalar
  excess is `m^(o(1))NH`; and
* a `T`-rich raw norm gap must be supported on `Omega(T/m^(o(1)))`
  distinct determinant values, with almost all its mass at high determinant
  once `T` exceeds the low-area capacity.

This does not prove the reciprocal weighted tail.  There is a genuine
aligned obstruction: in the 43-point transformed parabola, one fixed
**source** Gaussian cell contains only seven ordered edge pairs but has
clean-fibre codegree weight 219.  It aligns with a realized target norm gap
of multiplicity four.  Thus Gaussian factorization controls the number of
source edge pairs in a cell, but not the number of clean translations shared
by those pairs.

The full weighted-tail theorem is therefore reduced to the high-determinant
branch with anchor-codegree weights retained.  Dropping those weights after
Gaussian factorization is invalid.

## 2. Exact Gaussian factorization

Canonically orient each unordered edge and write its displacement as a
Gaussian integer `u`.  For an ordered edge pair `(u,v)` put

\[
 r=|u|^2-|v|^2,
 \qquad d=2\det(u,v),
 \qquad \alpha=u-v,
 \qquad \beta=u+v.                                        \tag{2.1}
\]

Then

\[
 \boxed{\alpha\overline\beta=r-id.}                       \tag{2.2}
\]

Indeed its real part is `(u-v) dot (u+v)=r`, while its
imaginary part is `-det(u-v,u+v)=-2det(u,v)`.

Conversely, `alpha,beta` determine

\[
 u={\alpha+\beta\over2},\qquad
 v={\beta-\alpha\over2}.                                  \tag{2.3}
\]

Distance-Sidonicity makes an oriented displacement determine its endpoint
edge.  Hence different edge-pair records in one nonzero `(r,d)` cell give
different Gaussian factorizations of `r-id`.

Let

\[
 R_D(r,d)=\#\{(t,t'):\delta(t)-\delta(t')=r,
                         2\det(v_t,v_{t'})=d\}.            \tag{2.4}
\]

The number of Gaussian divisors of a nonzero integer `w` is at most
`4 tau(|w|^2)^2` (a deliberately safe rational-divisor bound).
Equations (2.2)--(2.3) therefore prove the quantitative
bound

\[
 \boxed{
 R_D(r,d)\le4\tau(r^2+d^2)^2=m^{o(1)}
 \qquad((r,d)\ne(0,0)).}                                  \tag{2.5}
\]

Parity and endpoint-realizability only reduce the count.  Since all
coordinates lie at height `O(m)`, both `r` and `d` are `O(m^2)`, so the
standard divisor bound is uniform.

## 3. A proved determinant range

Put

\[
 G(m)=\max_{(r,d)\ne(0,0)}R_D(r,d)=m^{o(1)}.               \tag{3.1}
\]

For one fibre `H_q` of size `h_q`, set

\[
 L_q=\left\lfloor{N\over h_q}\right\rfloor.              \tag{3.2}
\]

Fix an ordered off-diagonal source pair.  Its scalar radius difference fixes
`r`; among target pairs with `|d|<=L_q`, (2.5) gives at most

\[
 G(m)(2L_q+1)                                             \tag{3.3}
\]

choices.  Summing the `h_q^2` source pairs yields

\[
\begin{aligned}
 \mathcal X_q^{\rm low}
 &\le G(m)(2L_q+1)h_q^2\\
 &\le3G(m)Nh_q.
\end{aligned}                                             \tag{3.4}
\]

Therefore

\[
 \boxed{
 \sum_q\mathcal X_q^{\rm low}\le m^{o(1)}NH.}            \tag{3.5}
\]

This is a complete theorem, not a conjectural tail estimate.  Combined with
the repeated-edge and squareclass-resonant reductions, it leaves exactly the
four-edge, squareclass-transverse, adaptive high-determinant core.

There is also a useful classification of raw rich gaps.  From (2.5), for a
fixed `r` and any `L`,

\[
 \sum_{|d|\le L}R_D(r,d)\le G(m)(2L+1).                   \tag{3.6}
\]

Consequently, if `R_D(r)>=T`, then

\[
 \sum_{|d|>L}R_D(r,d)
 \ge T-G(m)(2L+1).                                        \tag{3.7}
\]

In particular, when `T>=2G(m)(2L+1)`, at least half of the rich-gap mass is
at determinant greater than `L`.  Also

\[
 |\{d:R_D(r,d)>0\}|\ge {R_D(r)\over G(m)}.                \tag{3.8}
\]

Thus every genuinely rich norm gap is determinant-rich; the obstruction is
not hidden multiplicity inside one hyperbola cell.

## 4. Why the same factorization does not bound clean weights

Define the determinant-decorated source weight

\[
 S(z,e)=
 \sum_q\#\{(s,s')\in H_q^2:
 \delta(s)-\delta(s')=z,
 2\det(u_s,u_{s'})=e\}.                                   \tag{4.1}
\]

For a fixed `(z,e)`, the Gaussian argument shows that only `m^(o(1))`
ordered source edge pairs can occur.  But (4.1) counts each such pair with
its clean-fibre codegree

\[
 c(s,s')=|\{q:s,s'\in H_q\}|.                             \tag{4.2}
\]

Precisely,

\[
 S(z,e)=
 \sum_{\substack{(s,s'):\text{cell }(z,e)}}c(s,s').       \tag{4.3}
\]

The divisor theorem bounds the number of summands, not their weights.

The transformed parabola gives an exact aligned certificate.  In its source
cell

\[
 (z,e)=(189216,-288),                                     \tag{4.4}
\]

there are only seven ordered edge pairs, but their codegrees are

\[
 60,38,37,29,25,20,10,                                   \tag{4.5}
\]

so

\[
 \boxed{S(189216,-288)=219.}                              \tag{4.6}
\]

This cell is relevant to the scalar identity because

\[
 -{189216\over18}=-10512                                  \tag{4.7}
\]

is a realized target norm gap.  Its total multiplicity is four, distributed
over target determinant cells as

\[
 R_D(-10512,-716)=1,\quad
 R_D(-10512,16)=2,\quad
 R_D(-10512,1020)=1.                                      \tag{4.8}
\]

Thus this one source Gaussian cell contributes

\[
 219\cdot4=876                                            \tag{4.9}
\]

to the aggregate scalar expansion.  The example does not threaten the
desired global bound, but it is a genuine aligned counterexample to the
step “fixed Gaussian cell implies subpolynomial clean weight.”

## 5. Computational determinant profiles

The verifier checks (2.2) for every ordered edge pair and reports the exact
nonzero target-cell multiplicities:

\[
\begin{array}{c|r|r|r|r|r}
\text{family}&\max R_D(r,d)&\#(=2)&\#(=3)&\#(=4)&\#(\ge5)\\ \hline
\text{closure }20&3&176&2&0&0\\
\text{closure }40&3&1620&8&0&0\\
\text{Costas }22&5&666&28&8&2\\
\text{parabola }43&8&7120&328&58&16\\
\text{perpendicular ruler }40&6&3706&382&48&10
\end{array}                                               \tag{5.1}
\]

The small decorated multiplicities contrast sharply with raw gap
multiplicities as large as 100 in the same stored families.  This confirms
the Gaussian theorem numerically, while (4.4)--(4.9) isolate the separate
anchor-codegree obstruction.

## 6. Status of the reciprocal weighted tail

Determinant decoration rigorously removes the adaptive low-area branch and
forces every remaining `T`-rich gap to occupy many high-area cells.  It does
not, by itself, prove

\[
 \sum_{\substack{r\ne0\\R_D(r)\ge T}}S(-18r)
 \le {m^{o(1)}N(H+k^3)\over T}.                           \tag{6.1}
\]

The exact missing input is now narrower:

> Control the clean codegrees `c(s,s')` collectively across the many source
> determinant cells whose real Gaussian parts are `-18` times determinant-
> rich target real parts.

A proof may use the common-translation endpoint equations or a joint
incidence theorem in the two Gaussian products.  It cannot discard `q`
after applying the divisor bound, because (4.5) shows that the lost weight
is already linear-sized in a genuine geometric family.

Run `verify_metric_scalar_determinant_weighted_tail.py` for the exact
Gaussian identities, cell profiles, and aligned obstruction.
