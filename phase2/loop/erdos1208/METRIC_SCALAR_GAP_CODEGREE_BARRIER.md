# Scalar gap multiplicity versus clean-fibre codegree

## 1. Outcome

The proposed pointwise estimate

\[
 R_D(r)\le k^{1+o(1)}\qquad(r\ne0)                         \tag{1.1}
\]

is false in the strongest possible exponent.  There are genuine integral
distance-Sidon sets with

\[
 \boxed{R_D(r)=\Omega(k^2)=\Omega(N)}                     \tag{1.2}
\]

at one nonzero squared-distance gap.  Since the universal bound is
`R_D(r)<=N`, this is sharp.

However, the construction can simultaneously have no equal disjoint triple
sums, hence no clean fibres and no fibre codegrees.  Its quadratic gap is
completely invisible in the exact weighted identity.  This shows that raw
distance-gap tails are the wrong object, while a genuinely weighted
gap--codegree tail remains viable.

The exact sufficient target is now particularly clean.  Put

\[
 S(z)=\sum_q\#\{(s,s')\in H_q^2:
                      \delta(s)-\delta(s')=z\}.            \tag{1.3}
\]

If, uniformly for `1<=T<=N`,

\[
 \boxed{
 \sum_{\substack{r\ne0\\R_D(r)\ge T}}S(-18r)
 \le {m^{o(1)}N(H+k^3)\over T},}                          \tag{1.4}
\]

then the aggregate scalar theorem follows by dyadic summation.  No proof of
(1.4) is supplied here; the contribution of this note is to kill (1.1),
prove the exact weighted reduction, and give reproducible alignment data.

## 2. Exact weighted identity and elementary limits

Let `D=delta(Sigma)`, `N=|D|`, and

\[
 R_D(r)=|D\cap(D+r)|.                                     \tag{2.1}
\]

The aggregate identity is

\[
 \sum_q\mathcal M_{q,18}
 =\sum_rS(-18r)R_D(r).                                    \tag{2.2}
\]

Because squared distances are distinct,

\[
 R_D(0)=N,\qquad R_D(r)\le N.                             \tag{2.3}
\]

Likewise, injectivity of `delta` on each `H_q` gives

\[
 S(0)=H,qquad
 \sum_rS(r)=\sum_qh_q^2\le NH,qquad
 S(r)\le H.                                               \tag{2.4}
\]

Thus the diagonal in (2.2) is exactly `NH`, and every *single* nonzero gap
contributes at most `NH`.  The only possible failure is simultaneous
alignment over many gaps:

\[
 \sum_q\mathcal M_{q,18}-NH
 =\sum_{r\ne0}S(-18r)R_D(r).                              \tag{2.5}
\]

Define the weighted cumulative tail

\[
 \mathfrak S(T)=
 \sum_{\substack{r\ne0\\R_D(r)\ge T}}S(-18r).            \tag{2.6}
\]

Layer-cake summation gives the exact relation

\[
 \sum_{r\ne0}S(-18r)R_D(r)
 =\sum_{T=1}^N\mathfrak S(T).                              \tag{2.7}
\]

Consequently (1.4) gives `m^(o(1))N(H+k^3) log N`, and the logarithm is
absorbed into `m^(o(1))`.  Equivalently it is enough to prove the analogous
bound on each dyadic shell `T<=R_D(r)<2T`.

This formulation distinguishes the real issue from a pointwise gap bound.
At `T=1`, (1.4) follows already from (2.4); only the rich-gap tail is new.

## 3. Infinite quadratic-gap construction

Fix an odd base `B>=11` and an integer `L`.  Put

\[
 M=2L+1,\qquad r=B^M,                                     \tag{3.1}
\]

and take the `2L` horizontal marks

\[
 a_i={B^{M-i}+B^i\over2},\qquad
 b_i={B^{M-i}-B^i\over2},\qquad 0\le i<L.                \tag{3.2}
\]

They satisfy

\[
 a_i^2-b_i^2=(a_i-b_i)(a_i+b_i)=B^iB^{M-i}=r.             \tag{3.3}
\]

The horizontal marks form a Golomb ruler.  Formally replace `B^j` by a
basis vector `e_j`.  The two marks in block `i` become

\[
 e_{M-i}+e_i,qquad e_{M-i}-e_i.                           \tag{3.4}
\]

In a difference of two distinct marks, the high coordinates identify the
ordered block pair; if both marks come from one block, the difference is
`+-2e_i`.  Hence all oriented formal differences are distinct.  Evaluating
at powers of `B` preserves this: an alleged equality leaves a base-`B`
relation with coefficients in `[-4,4]`, whose highest nonzero digit
dominates all lower digits when `B>=11`.

Take `2L` vertical Golomb marks `Y`, scale them so that their positive
difference spectrum is disjoint from the horizontal spectrum, and put

\[
 A_C=\{(x,0):x\in\{a_i,b_i\}\}
     \cup\{(0,C+y):y\in Y\}.                              \tag{3.5}
\]

There is an integral `C` for which this is distance-Sidon.  Internal
distances are already distinct.  A cross squared distance is

\[
 x^2+(C+y)^2=C^2+2yC+(x^2+y^2).                           \tag{3.6}
\]

Different cross edges give different polynomials in `C`: the linear
coefficient identifies `y`, then the constant identifies the positive mark
`x`.  Only finitely many integers `C` cause a cross/cross or cross/internal
collision, so a generic large integer works.

For every `i` and every vertical point `(0,C+y)`, the two cross edges from
`(a_i,0)` and `(b_i,0)` have squared-distance gap `r`.  Therefore

\[
 R_D(r)\ge L|Y|=2L^2.                                     \tag{3.7}
\]

Here `k=4L` and `N=binom(4L,2)=8L^2-2L`, so

\[
 R_D(r)\ge {k^2\over8}=(1/4+o(1))N.                       \tag{3.8}
\]

This proves (1.2).

The construction may also be chosen triple-sum-Sidon.  The formal high
coordinates in (3.4) identify every subset of at most three horizontal
marks, while distinct powers of two identify every subset of at most three
vertical marks.  Taking `C` larger than the vertical offset range separates
triples containing different numbers of vertical points.  Thus no two
distinct triples have equal sums and

\[
 H=0,qquad S(r)=0\quad\hbox{for all }r.                   \tag{3.9}
\]

The verifier uses vertical powers of two, scale two, and exact admissible
offsets for `L=2,4,8,16`.  It obtains

\[
\begin{array}{c|r|r|r}
L&k&N&R_D(B^{2L+1})\\ \hline
2&8&28&8\\
4&16&120&32\\
8&32&496&128\\
16&64&2016&512
\end{array}                                                \tag{3.10}
\]

and checks `H=0` exactly in every row.

This family has exponentially large height.  It rules out a bound purely in
`k`, but does not rule out a height-sensitive estimate whose `m^(o(1))`
factor absorbs sparse constructions.  Such a pointwise estimate would still
have to be strong enough to avoid losing an extra factor `k` in (2.5).

## 4. Exact weighted stress profiles

For each stored family the verifier computes all squared-distance gaps, all
clean-fibre source gaps, and their exact aligned product in (2.5).

\[
\begin{array}{c|r|r|r|r|r|r}
\text{family}&N&H&\max_{r\ne0}R_D(r)&
\#\{r:S(-18r)R_D(r)>0\}&\text{offdiag}&\max_r SR\\ \hline
\text{closure }40&780&12420&100&2300&347362&1988\\
\text{Costas }22&231&9342&19&1296&72622&686\\
\text{parabola }43&903&190278&11&27218&2143322&2637\\
\text{perpendicular ruler }40&780&4914&24&980&2188&25\\
\text{scalar-channel barrier }74&2701&252&2&114&172&4
\end{array}                                                \tag{4.1}
\]

The factors in the largest aligned product `(R_D,S)` are respectively

\[
 (71,28),\ (14,49),\ (9,293),\ (5,5),\ (2,2).             \tag{4.2}
\]

In the Costas and perpendicular-ruler families, the maximally popular raw
gap has zero clean-fibre weight.  The deliberately engineered 74-point
large-area scalar channel aligns twelve records, but its raw distance-gap
multiplicities never exceed two.  The quadratic-gap construction has no
clean weight at all.

These computations do not prove (1.4), but they survive adversarial tests
from both directions: high raw gap multiplicity without codegree, and exact
scalar codegree alignment without a rich raw gap.

## 5. Restart target

The pointwise route `R_D(r)<=k^(1+o(1))` is closed.  The surviving direct
route is the reciprocal weighted tail (1.4), or a stronger determinant-
decorated version.  Any proof must show that many clean source pairs cannot
align with many rich squared-distance gaps at once.  Bounding the two
marginals separately cannot do this: (3.8)--(3.9) exhibit their complete
decoupling.

Run `verify_metric_scalar_gap_codegree_barrier.py` for the exact
certificates and profiles.
