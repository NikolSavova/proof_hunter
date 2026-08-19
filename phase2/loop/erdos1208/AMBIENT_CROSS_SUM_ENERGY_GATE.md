# An ambient-sensitive cross-sum energy gate for the cube-root exponent

## 1. Outcome

Let

\[
 A\subset[0,m]^2\cap\mathbb Z^2,
 \qquad |A|=k,
\]

be distance-Sidon, and let `J(x,y)=(-y,x)`.  Put

\[
 B=A+JA.
\]

Distance-Sidonicity makes the representation `a+Jb` unique, so
`|B|=k^2`.  The additive energy of this cross sum has the exact Fourier
form

\[
 E^+(B)=\int_{\mathbb T^2}
   |\widehat{1_A}(\theta)|^4
   |\widehat{1_A}(J\theta)|^4\,d\theta.        \tag{1.1}
\]

Band limitation at the origin gives the unconditional lower bound

\[
 \boxed{E^+(A+JA)\ge {k^8\over1024m^2}.}       \tag{1.2}
\]

Consequently the following ambient-sensitive estimate would resolve the
power-law order in Erdős 1208:

\[
 \boxed{
 E^+(A+JA)
 \le k^{5+o(1)}+m^{2+o(1)}k^2.}               \tag{1.3}
\]

Indeed (1.2)--(1.3), after splitting according to the larger term on the
right, give `k^3<=m^(2+o(1))` or `k^6<=m^(4+o(1))`; either conclusion is

\[
 k\le m^{2/3+o(1)}.                            \tag{1.4}
\]

Estimate (1.3) is not proved.  It is a sharp successor to the false
size-only bound `E^+(A+JA)<=k^(5+o(1))`: dense perpendicular Golomb-ruler
families have energy `Omega(k^6)` but can be placed at ambient scale
`m=k^(2+o(1))`, exactly the scale allowed by the second term of (1.3).

## 2. Directness of the cross sum

Suppose

\[
 a+Jb=c+Jd,
 \qquad a,b,c,d\in A.
\]

Then

\[
 a-c=J(d-b).                                   \tag{2.1}
\]

The two sides have the same Euclidean norm.  If they are nonzero,
distance-Sidonicity says that the two underlying unordered point-pairs are
equal.  Their directed vectors must therefore agree up to sign, whereas a
nonzero real vector cannot equal plus or minus its quarter-turn.  Hence both
sides of (2.1) vanish, and `a=c`, `b=d`.  Thus

\[
 |A+JA|=k^2.                                    \tag{2.2}
\]

Writing `H(theta)=|hat 1_A(theta)|^2`, directness also gives

\[
 \int H(\theta)H(J\theta)\,d\theta=k^2.        \tag{2.3}
\]

Equation (1.1) is Parseval applied to the indicator
`1_B=1_A*1_{JA}`.

## 3. Origin localization

Translate `A` so that its two coordinate ranges are at most `m`.  If

\[
 |\theta_1|,|\theta_2|\le {1\over16m},
\]

then the phases `2 pi theta dot a`, as `a` ranges over `A`, lie in an
interval of length at most `pi/4`.  After one common phase rotation, every
summand has real part at least `1/sqrt(2)`.  Therefore

\[
 H(\theta)\ge {k^2\over2},
 \qquad H(J\theta)\ge {k^2\over2}.             \tag{3.1}
\]

The frequency square has area `1/(64m^2)`.  Inserting (3.1) into (1.1)
proves (1.2).

This shows why the two terms in (1.3) meet at precisely the desired
exponent.  At `k=m^(2/3)`, the unavoidable origin peak already contributes
on the `k^5=m^2k^2` scale.

## 4. A stronger pointwise sufficient statement

For `t in Z^2`, let

\[
 r_B(t)=|B\cap(B+t)|.
\]

The identity

\[
 \sum_t r_B(t)=|B|^2=k^4                     \tag{4.1}
\]

and `r_B(0)=k^2` show that the pointwise estimate

\[
 \boxed{
 \max_{t\ne0}r_B(t)
 \le k^{o(1)}\left(k+{m^2\over k^2}\right)}  \tag{4.2}
\]

would imply (1.3):

\[
 E^+(B)=\sum_t r_B(t)^2
 \le k^4+k^{4+o(1)}
       \left(k+{m^2\over k^2}\right).
\]

In difference-vector language,

\[
 r_B(t)=
 |\{(x,y)\in(A-A)^2:x+Jy=t\}|,                \tag{4.3}
\]

where the zero differences retain their endpoint multiplicities.  A fixed
nonzero row is a partial affine quarter-turn matching

\[
 y=-Jx-Jt
\]

between directed edges of the complete geometric graph on `A`.

Estimate (4.2) is deliberately density-sensitive.  The known
perpendicular-ruler construction can have a row of order `k^2`, but only at
ambient scale `m=k^(2+o(1))`, where `m^2/k^2=k^(2+o(1))`.  Thus it does not
contradict (4.2).  The generic translated-segment row gadgets likewise pay
through their large coordinate height.

The pointwise statement may still be too strong; (1.3) is the preferred
aggregate theorem.  Its advantage over the support-adaptive endpoint gate is
that the ambient box directly pays for sparse line-like peaks, while the
`k^5` term is reserved for genuinely two-dimensional endpoint reuse.

## 5. Exact stress profiles

`verify_ambient_cross_sum_energy_gate.py` checks directness, (1.1) in
coefficient form, (1.2), and the following exact profiles.  Here `m` is the
larger coordinate range and the energy ratio is

\[
 {E^+(B)\over k^5+m^2k^2}.
\]

\[
\begin{array}{c|r|r|r|r|c}
\text{family}&k&m&E^+(B)&\max_{t\ne0}r_B(t)&\text{energy ratio}\\ \hline
\text{closure }30&30&150&21{,}580{,}780&152&0.484417\ldots\\
\text{closure }40&40&223&95{,}040{,}912&231&0.522299\ldots\\
\text{source }45&45&324&107{,}918{,}569&137&0.271763\ldots\\
\text{perpendicular ruler }40&40&3202&30{,}866{,}544&110&0.001869\ldots\\
\text{Costas }22&22&131&1{,}565{,}772&28&0.116331\ldots
\end{array}                                                        \tag{5.1}
\]

The stronger pointwise normalization in (4.2) requires an absolute constant
larger than one on the closure stresses: the maximum displayed ratio
`max r_B/(k+m^2/k^2)` is `3.2498...` at closure 40.  Thus neither live
statement should be formulated with a sharp constant one.

These finite rows are evidence and calibration only.  The new mathematical
target is the aggregate estimate (1.3), or a counterexample to it inside a
genuine bounded-height distance-Sidon set.

## 6. Relation to the endpoint programme

A collision in one row of (4.3) compares two directed edges and produces
the same quarter-turn displacement systems studied by the eight-corner and
opposite-endpoint charges.  The difference is the bookkeeping scale:

* the endpoint programme pays a heavy row through `|D+D|`; while
* (1.3) pays its line-like component directly through the ambient `m^2`
  term.

A proof of (1.3) can therefore use the existing commutator dichotomy.  The
abelian full-core branch is already impossible.  What remains is to show
that noncommuting endpoint reuse contributes `k^(5+o(1))`, while the
approximately one-dimensional/perpendicular-ruler part contributes at most
`m^(2+o(1))k^2`.
