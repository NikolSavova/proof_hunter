# A polynomial-height counterexample to the original raw scalar aggregate

## 1. Verdict

The original surviving scalar target

\[
 \boxed{
 \sum_q\mathcal X_q\le m^{o(1)}Nk^3,
 \qquad
 \mathcal X_q=\mathcal M_{q,18}-N|H_q|}          \tag{1.1}
\]

is false by a full polynomial factor.  There are integral distance-Sidon
sets of polynomial height for which

\[
 \boxed{\sum_q\mathcal X_q=\Omega(k^6),}         \tag{1.2}
\]

whereas `Nk^3=Theta(k^5)`.

The construction is a norm-dilated swap.  Take a dense collinear Golomb
clean core whose edge labels are `36 ell^2`, and adjoin a translated
diagonal copy of the same ruler whose corresponding edge labels are
`2 ell^2`.  The coefficient 18 in the scalar charge makes

\[
 36x^2+18(2y^2)=36y^2+18(2x^2).                 \tag{1.3}
\]

Thus every ordered pair of distinct starts in every old clean fibre gives
a literal off-diagonal scalar collision.  Dense Golomb rulers have
`sum_q |H_q|^2=Omega(k^6)`, so (1.2) follows.

This is a counterexample to the scalar proof architecture, **not** to
Erdos Problem 1208.  Its polynomial-height exponent is not the conjectural
one.  The conclusion is that the proof must abandon the positive scalar
charge (and every tail or endpoint reduction derived solely from it).

## 2. Construction

Let

\[
 B_n\subset[0,Cn^2]\cap\mathbb Z,
 \qquad |B_n|=n,                                  \tag{2.1}
\]

be a dense Golomb ruler; the standard Ruzsa construction supplies such a
family explicitly.  Put

\[
 A_H=\{(6b,0):b\in B_n\}.                         \tag{2.2}
\]

For a translation `T=(T_1,T_2)`, put

\[
 A_D=T+\{(b,b):b\in B_n\},
 \qquad A=A_H\cup A_D.                            \tag{2.3}
\]

If an underlying ruler edge has positive length `ell=|b_i-b_j|`, its two
copies have squared lengths

\[
 \delta_H(\ell)=36\ell^2,
 \qquad
 \delta_D(\ell)=2\ell^2,
 \qquad
 \delta_H(\ell)=18\delta_D(\ell).                \tag{2.4}
\]

## 3. Polynomial-height distance-Sidon specialization

The translation `T` can be chosen integrally at polynomial height so that
the union (2.3) is distance-Sidon.

First, each internal copy is distance-Sidon because `B_n` is Golomb.  The
two internal spectra are disjoint: an equality between them would give

\[
 36x^2=2y^2,qquad y^2=18x^2,                    \tag{3.1}
\]

which has no nonzero integral solution.

A cross edge from `(6b_i,0)` to `T+(b_j,b_j)` has displacement

\[
 T+v_{ij},qquad v_{ij}=(b_j-6b_i,b_j).          \tag{3.2}
\]

The map `(i,j) -> v_(ij)` is injective: equality of the second coordinates
gives `b_j=b_l`, and then equality of the first gives `b_i=b_k`.
Consequently an equality between two distinct cross-edge lengths is a
nonzero affine polynomial in `T`, whose linear coefficient is
`2(v_(ij)-v_(kl))`.  Equality of a cross length with an internal length is
a nonzero quadratic polynomial `|T+v_(ij)|^2-c`.  Point coincidences are
also nonzero polynomial conditions.

There are only `n^(O(1))` such degree-at-most-two bad polynomials.  Their
product is nonzero and has polynomial total degree.  The elementary grid
nonvanishing lemma therefore supplies an integral `T` of size `n^(O(1))`
outside their union.  Hence

\[
 |A|=2n,qquad m=n^{O(1)},                       \tag{3.3}
\]

and every squared distance in `A` is distinct.  Distance-Sidonicity also
implies unordered pair-sum uniqueness: two different equal pair sums would
form a parallelogram with two different equal-length opposite sides.

## 4. Dense clean mass in the horizontal core

The `Theta(n^3)` unordered triples of `B_n` have only `O(n^2)` possible
integer sums.  Cauchy--Schwarz gives `Omega(n^4)` pairs of equal-sum
triples.  Two distinct equal-sum triples are disjoint: after cancelling a
shared mark, the remaining two unordered pairs would have the same sum,
contradicting the Golomb property.

As in the standard dense-Golomb clean-core argument, distinguishing one
endpoint in each of two disjoint equal-sum triples produces literal
six-distinct clean starts.  Therefore, for the horizontal core fibres,

\[
 H_0:=\sum_q h_q=\Omega(n^4).                    \tag{4.1}
\]

There are at most `n(n-1)` directed horizontal anchor differences.  Thus

\[
 \sum_qh_q^2
 \ge {H_0^2\over n(n-1)}
 =\Omega(n^6).                                    \tag{4.2}
\]

All these old clean records survive in `A`.  Indeed their six points are
unchanged, and global pair-sum uniqueness prevents a new pair from
altering their canonical representations.

## 5. Exact raw scalar swap

For every horizontal source start `s`, let `s^D` denote the corresponding
diagonal-copy edge using the same two ruler marks.  Equation (2.4) says

\[
 \delta_H(s)=18\delta_D(s^D).                   \tag{5.1}
\]

Fix `q` and two distinct old starts `s,s' in H_q`.  The two records

\[
 (s,(s')^D),qquad (s',s^D)                     \tag{5.2}

\]

belong to `H_q times Sigma(A)`, are different, and have equal scalar
charge:

\[
\begin{aligned}
 \delta_H(s)+18\delta_D((s')^D)
 &=\delta_H(s)+\delta_H(s')\\
 &=\delta_H(s')+18\delta_D(s^D).                \tag{5.3}
\end{aligned}

Therefore the off-diagonal energy obeys the literal lower bound

\[
\begin{aligned}
 \sum_q\mathcal X_q
 &\ge\sum_qh_q(h_q-1)\\
 &=\sum_qh_q^2-H_0
 =\boxed{\Omega(n^6)}.                           \tag{5.4}
\end{aligned}

The final set has `k=2n` and `N=binom(2n,2)=Theta(n^2)`, so

\[
 Nk^3=\Theta(n^5).                               \tag{5.5}
\]

Since `m=n^(O(1))`, the allowed factor `m^(o(1))=n^(o(1))` cannot absorb
the factor `n` between (5.4) and (5.5).  This proves the counterexample to
(1.1).

In the exact gap-codegree identity, the same mechanism reads

\[
 {\delta_H(s')-\delta_H(s)\over18}
 =\delta_D((s')^D)-\delta_D(s^D).                \tag{5.6}
\]

Thus every old ordered source pair is aligned with a raw target-gap record.
This is why the earlier one-channel planting square budget does not apply:
the diagonal copy simultaneously realizes all `Theta(n^4)` source-gap
channels with the same `n` points.

## 6. Exact finite certificate

The verifier takes the 30-mark Ruzsa ruler from `p=31`, uses the horizontal
scale 6, and translates its diagonal copy by

\[
 T=(1,121,776,528,\ 8,095,936,488).              \tag{6.1}
\]

The 60-point union has all 1,770 squared distances and pair sums distinct.
Every horizontal clean start remains in the corresponding full-set fibre.
Its exact old-core and swap profile is

\[
\begin{array}{c|r}
\text{quantity}&\text{value}\\ \hline
n,k,N&30,60,1,770\\
\#\text{ old active fibres}&870\\
H_0&82,746\\
\sum_qh_q^2&8,233,370\\
\sum_qh_q(h_q-1)&8,150,624\\
Nk^3&382,320,000\\
\max|\text{coordinate}|&8,095,937,388.
\end{array}                                             \tag{6.2}
\]

The finite ratio is small because the asymptotic lower-bound constants in
the dense triple-sum argument are not optimized.  The verifier checks all
8,150,624 displayed ordered swaps exactly; the theorem uses their
`Omega(n^6)` asymptotic order.

Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_raw_scalar_dilated_swap_golomb_counterexample.py
```

## 7. Consequence for the proof architecture

The failure occurs before determinant truncation, endpoint wedges,
common-`q` switching, dyadic tails, or actual-codegree normalization.  It
is already a complete four-edge scalar swap inside the original charge.
Accordingly, none of those downstream refinements can repair (1.1) while
retaining the same positive scalar projection.

The still-valid information is the exact clean common-translation
incidence itself and the earlier vector/matrix identities before scalar
projection.  A renewed route must keep enough orientation, matrix, or
endpoint data to distinguish the two swapped norm-dilated copies.
