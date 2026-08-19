# A size-biased eight-corner gate for the transverse theorem

## 1. Outcome

Let `A` be a planar distance-Sidon set of size `k`, put `D=A-A`, and let
`J` be quarter-turn.  Write an oriented transverse relation as

\[
 d=f+Je,
 \qquad d,e,f\in D,
 \qquad e\ne0,
 \qquad d\mathbin\cdot e\ne0.                  \tag{1.1}
\]

Give the three directed edges their unique endpoint pairs

\[
 d=a_0-a_1,
 \qquad f=b_0-b_1,
 \qquad e=c_0-c_1.                              \tag{1.2}
\]

For every corner `epsilon in {0,1}^3`, let

\[
 \pi_\epsilon(\rho)
 =(a_{\epsilon_0},b_{\epsilon_1},c_{\epsilon_2})
 \in A^3,                                       \tag{1.3}
\]

and let `deg_epsilon(v)` be the number of transverse relations having
corner key `v`.  Define

\[
 \delta(\rho)=
 \min_{\epsilon\in\{0,1\}^3}
 \deg_\epsilon(\pi_\epsilon(\rho)),
 \qquad
 \mathcal C(A)=\sum_{\rho}\delta(\rho).        \tag{1.4}
\]

The pointwise conjecture `max delta(rho)=k^(o(1))` is false by the product
construction in `TRANSVERSE_EIGHT_CORNER_PRODUCT_BARRIER.md`.  The proof
only needs the strictly weaker size-biased statement

\[
 \boxed{\mathcal C(A)\le k^{3+o(1)}.}           \tag{1.5}
\]

Indeed every relation has `delta(rho)>=1`, so (1.5) gives

\[
 2E_{\rm trans}(A)=|\mathcal R(A)|
 \le \mathcal C(A)\le k^{3+o(1)}.              \tag{1.6}
\]

Together with Elekes's trapezoid estimate, this closes the wide regime
`max_line(A)<=sqrt(k) log k` of the rotated triple support theorem.  The
polynomially line-rich regime still requires coupling this transverse bound
to `PARALLEL_LINE_SUPPORT_LEMMA.md`; (1.5) is therefore a major direct gate,
not by itself a full resolution of Erdos 1208.

Estimate (1.5) is **not proved**.  Its value is that the mechanism which
refutes the pointwise statement does not refute the aggregate one: its one
planted relation of adaptive degree `Theta(k)` contributes only `Theta(k)`,
not a power-scale fraction of the allowed cubic budget.  The total aggregate
of that generic product family has not been classified here.

## 2. Equivalent rich-core tail

For an integer `t>=1`, put

\[
 \mathcal R_{\ge t}
 =\{\rho:\deg_\epsilon(\pi_\epsilon(\rho))\ge t
          \text{ for every }\epsilon\}.        \tag{2.1}
\]

The layer-cake identity is exact:

\[
 \boxed{
 \mathcal C(A)=\sum_{t=1}^k|\mathcal R_{\ge t}|.}             \tag{2.2}
\]

Consequently the uniform dense-core estimate

\[
 \boxed{
 |\mathcal R_{\ge t}|
 \le {k^{3+o(1)}\over t}}
 \qquad(1\le t\le k)                           \tag{2.3}
\]

implies (1.5), with only a logarithmic loss.  This is the honest inverse
formulation.  A counterexample must contain polynomially many relations
which remain simultaneously popular in all eight mixed endpoint
projections; making one relation popular in eight independent completion
families is no longer enough.

## 3. Exact calibration

The exact profiles below are

\[
 (k,|\mathcal R|,\max\delta,\mathcal C,
       \mathcal C/k^3,\mathcal C/|\mathcal R|).
\]

\[
\begin{array}{c|r|r|r|c|c}
k&|\mathcal R|&\max\delta&\mathcal C&
 \mathcal C/k^3&\mathcal C/|\mathcal R|\\ \hline
30&26{,}428&5&41{,}696&1.54430&1.57772\\
45&107{,}720&6&191{,}272&2.09901&1.77564\\
60&259{,}516&8&477{,}864&2.21233&1.84137\\
90&1{,}009{,}116&9&2{,}018{,}332&2.76863&2.00010\\
120&2{,}798{,}384&12&6{,}182{,}704&3.57795&2.20938
\end{array}                                                    \tag{3.1}
\]

The 117-point compact-anchor obstruction has

\[
 (|\mathcal R|,\max\delta,\mathcal C)
 =(159{,}888,6,320{,}484).                       \tag{3.2}
\]

Thus the size-biased quantity stays on the `k^3` scale while the local
maximum grows.  The slow increase in `C/k^3` is compatible with a logarithm
and should not be interpreted as evidence for a constant bound.

## 4. Why the path-boundary shortcut fails

A corner fibre is a three-coordinate matching.  After multiplying by a
sign and by `J`, its complementary triples have the canonical form

\[
 x=p+J(r-q).                                      \tag{4.1}
\]

When the first two corner bits agree, `q` and `r` lie in the same signed
copy of `A`; the directed edges `q->r` therefore have the translation-
invariant path/cycle structure of `FIBRE_PATH_CIRCULATION.md`.

The stored relation closures suggested the attractive assertion that every
transverse relation is a path endpoint in at least one of the four
same-sign corner fibres.  That assertion is false.

There is an explicit 22-point integer distance-Sidon set containing the
base relation

\[
 (0,1),\quad(2,3),\quad(4,5),                  \tag{4.2}
\]

in the three endpoint roles of (1.2), together with the following eight
relations:

\[
\begin{array}{c|c|c}
\text{corner}&\text{side}&(d,f,e)\\ \hline
0&\text{predecessor}&((0,3),(2,6),(4,7))\\
0&\text{successor}&((0,8),(2,1),(4,9))\\
3&\text{predecessor}&((2,1),(10,3),(4,11))\\
3&\text{successor}&((12,1),(0,3),(4,13))\\
4&\text{predecessor}&((0,3),(2,14),(15,5))\\
4&\text{successor}&((0,16),(2,1),(17,5))\\
7&\text{predecessor}&((2,1),(18,3),(19,5))\\
7&\text{successor}&((20,1),(0,3),(21,5)).
\end{array}                                                     \tag{4.3}
\]

For each of the four same-sign corners `0,3,4,7`, the corresponding two
rows in (4.3) make the base edge have both a predecessor and a successor.
It is therefore internal in all four translation-invariant fibres.

All 231 positive squared distances among the 22 points are distinct.  The
coordinates are stored in the verifier rather than repeated here.  The
construction arose from a rank-nine Gaussian-linear system on 22 point
variables; a generic integral specialization avoids every distance
equality.  The explicit certificate is enough for the barrier theorem.

This kills only the proposed boundary shortcut.  It does not falsify the
size-biased estimate (1.5): the construction spends sixteen fresh points to
make one base relation internal, exactly the endpoint cost that an aggregate
theorem is allowed to charge.

## 5. Verification and next theorem

`verify_size_biased_eight_corner_gate.py` checks the profiles in (3.1), the
layer-cake identity, the 22-point distance certificate, every relation in
(4.2)--(4.3), and the four internal path positions using exact integer
arithmetic.

The next proof target is (2.3), not a pointwise corner bound and not a
claim that every relation exposes a path endpoint.  A viable argument must
prune a large `R_(>=t)` to a core with reuse in all eight projections and
then use the literal characteristic-zero equation or complete-difference
endpoint realization to show that the core either spends `Omega(t)` new
points per relation family or forces a repeated Euclidean distance.
