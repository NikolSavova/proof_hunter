# A resonant two-arm barrier to the Gaussian edge-vector charge

## 1. Verdict

The Gaussian edge-vector estimate in `GAUSSIAN_EDGE_VECTOR_CHARGE.md` is
false by a quadratic factor, even for genuine integral distance-Sidon sets
of polynomial height and quadratically large clean fibres.

Let

\[
 \lambda=3(I+J),\qquad J(x,y)=(-y,x).
\]

There are integral distance-Sidon sets `A_s` with `k=2s` points, a realized
directed difference `q`, and a clean fibre `H_q` of size `h=Omega(s^2)` such
that

\[
 \boxed{\mathcal G_q\gg s^6.}                   \tag{1.1}
\]

Since

\[
 N=\binom{k}{2}=\Theta(s^2),\qquad
 N(h+k)=\Theta(s^4),                            \tag{1.2}
\]

this contradicts

\[
 \mathcal G_q\le m^{o(1)}N(h+k)                \tag{1.3}
\]

by a factor `s^(2-o(1))`.  The construction has `m=s^{O(1)}`, so the
subpolynomial ambient factor cannot absorb the failure.

The same family also kills the dilated pair-sum vector charge

\[
 (s,t)\longmapsto s+\lambda t
\]

from `DILATED_INTERNAL_PAIR_SUM_CHARGE.md`, and it kills the compound scalar
charge `|u(s)+lambda u(t)|^2`.  It does not by itself kill the separate
distance-label charge `|u(s)|^2+18|u(t)|^2`.

## 2. A dense Golomb ruler split between resonant arms

For every `s`, take a `2s`-mark integer Golomb ruler

\[
 R=\{r_1,\ldots,r_{2s}\}\subset[0,L],
 \qquad L=O(s^2).                               \tag{2.1}
\]

For example, choose a prime `2s<=p<4s` and take the first `2s` marks of

\[
r_j=2pj+(j^2\bmod p),\qquad 0\le j<p.         \tag{2.2}
\]

For completeness, these marks are Sidon.  Write
`epsilon_j=j^2 mod p` in `[0,p-1]`.  If
`r_i+r_j=r_k+r_l`, reduction modulo `2p` shows
`epsilon_i+epsilon_j=epsilon_k+epsilon_l` as an equality of integers
(both sides lie in `[0,2p-2]`), and then the original equality gives
`i+j=k+l`.  Reduction modulo `p` also gives
`i^2+j^2 congruent k^2+l^2 (mod p)`, hence `ij congruent kl (mod p)`.
Thus the two index pairs are the same unordered pair of roots of
`X^2-(i+j)X+ij` over `F_p`.  Since all indices lie in `[0,p-1]`, the two
unordered integer pairs are equal.  In particular all positive differences
are distinct, so this is a Golomb ruler.  Bertrand's postulate and `j<2s`
give

\[
 \max R-\min R<4ps+p=O(s^2).                  \tag{2.2a}
\]

Split `R=R_X disjoint_union R_Y`, with `|R_X|=|R_Y|=s`.  Put

\[
 e=(1,0),\qquad d=(-1,-1),                     \tag{2.3}
\]

so that

\[
 \lambda e=(3,3)=-3d.                          \tag{2.4}
\]

For an integral translation `T`, define two arms

\[
 X=\{re:r\in R_X\},\qquad
 Y=\{T+rd:r\in R_Y\},\qquad A=X\cup Y.         \tag{2.5}
\]

Thus the two arm directions are not perpendicular: they have been chosen
to resonate exactly under the Gaussian dilation.

## 3. Polynomial-height distance-Sidon realization

There is an integral `T` of polynomial size for which `A` is distance-Sidon.
Here is a direct finite-avoidance proof.

Write

\[
 T=(Z,Z^2).                                     \tag{3.1}
\]

Internal `X` distances have squared lengths `a^2`, and internal `Y`
distances have squared lengths `2b^2`, where `a,b` are nonzero differences
of ruler marks.  The Golomb property separates lengths within each arm,
and `a^2=2b^2` has no nonzero integral solution, so the two internal spectra
are disjoint.

The squared cross distance between `r_i e` and `T+r_jd` is

\[
 F_{ij}(Z)=(Z-r_i-r_j)^2+(Z^2-r_j)^2.           \tag{3.2}
\]

If `(i,j)!=(i',j')`, then `F_ij-F_i'j'` is a nonzero polynomial.  Indeed,
its quadratic coefficient recovers `r_j-r_j'`; if that vanishes, its linear
coefficient recovers `r_i-r_i'`.  A cross distance equalling a fixed
internal distance is also a nonzero polynomial condition, now with degree
four.  There are only `O(s^4)` forbidden equalities, each excluding at most
four integer values of `Z`.  Choose `Z>2L` as well, which makes the two
arms disjoint.  Among the next `O(s^4)` integers there is therefore some

\[
 2L<Z\ll s^4                                   \tag{3.3}
\]

which avoids all of them.  The resulting coordinate width satisfies

\[
 m\ll Z^2+L\ll s^8.                             \tag{3.4}
\]

This proves integral distance-Sidonicity at polynomial height.

## 4. A quadratically large clean fibre on the diagonal arm

Regard `R_Y` as a scalar Sidon set.  There are

\[
 M=\binom{s}{3}=\Theta(s^3)                    \tag{4.1}
\]

unordered three-element subsets, and their sums occupy only `O(L)=O(s^2)`
integer values.  If `rho(z)` counts these triple sums, Cauchy gives

\[
 \sum_z\binom{\rho(z)}2\gg s^4.                \tag{4.2}
\]

Distinct triples of a Sidon set with the same sum are disjoint: after
cancelling a common mark, equality of the remaining two-element sums would
make the triples equal.

Take two disjoint equal-sum triples `C,E`, choose `a in C` and `b in E`,
and put

\[
 q=(a-b)d,
 \qquad s_{C,a}=2T+\left(\sum_{c\in C\setminus\{a\}}c\right)d.
                                                            \tag{4.3}
\]

The equal-sum identity gives

\[
 s_{C,a}+q
 =2T+\left(\sum_{e\in E\setminus\{b\}}e\right)d,          \tag{4.4}
\]

so `s_C,a` is a clean member of `H_q`; its six endpoints are distinct.
Let `H_q^(Y)` denote the subfibre of clean starts for which both the source
and target pairs lie on `Y`.
Moreover `(q,s_C,a)` recovers `a,b` by unique ordered differences and then
recovers both remaining endpoint pairs by unique pair sums.  Consequently

\[
 \sum_{q\in(Y-Y)^*}|H_q^{(Y)}|\gg s^4.         \tag{4.5}
\]

There are at most `s(s-1)` realized nonzero directed differences in `Y`, so
some `q` satisfies

\[
 \boxed{h_Y=|H_q^{(Y)}|\gg s^2.}               \tag{4.6}
\]

Adding the `X` arm cannot delete any of these clean starts, so the full
fibre has `h=|H_q|>=h_Y` and also `h<=N=O(s^2)`.  In particular both
`h_Y` and `h` have order `s^2`.

## 5. Cubic charge energy

Fix the following reading of the canonical orientation: the edge vector is
the lexicographically smaller endpoint minus the larger endpoint.  (If the
opposite convention was intended, every vector below is globally negated
and the conclusion is unchanged.)  Write the ruler marks increasingly.
For every source sum in the clean subfibre furnished by Section 4, the two
endpoints lie on `Y`; if their scalar gap is `a_s>0`, then

\[
 u(s)=a_s d,\qquad 1\le a_s\le L.              \tag{5.1}
\]

Indeed, increasing the ruler parameter moves a `Y` point in the
lexicographically decreasing direction `d`.  Every internal `X` pair sum
`t`, with positive scalar gap `b_t`, has instead

\[
 u(t)=-b_t e,\qquad 1\le b_t\le L.             \tag{5.2}
\]

Thus the orientation signs are compatible, not cancelling.  By (2.4),

\[
 \Gamma_q(s,t)=u(s)+\lambda u(t)
 =(a_s+3b_t)d.                                  \tag{5.3}
\]

Thus the restriction of `Gamma_q` to

\[
 H_q^{(Y)}\times\binom X2
\]

has

\[
 h_Y\binom{s}{2}=\Omega(s^4)                   \tag{5.4}
\]

records but at most `4L+1=O(s^2)` vector keys.  Cauchy--Schwarz gives

\[
 \mathcal G_q
 \ge {\left(h_Y\binom{s}{2}\right)^2\over4L+1}
 \gg s^6,                                      \tag{5.5}
\]

which proves (1.1).

For the older pair-sum charge, internal `Y` sums have the form
`2T+ad`, while internal `X` sums have the form `be`; equation (2.4) again
puts all restricted keys on `2T+Z d` with only `O(s^2)` possibilities.
For the compound norm charge, the vectors in (5.3) are collinear, and
taking squared norms cannot increase the number of keys.  The same lower
bound therefore applies to both charges.

By contrast, on this restriction the *separate positive scalar* label is

\[
 |u(s)|^2+18|u(t)|^2=2a_s^2+18b_t^2.           \tag{5.6}
\]

It can have `O(L^2)=O(s^4)` values, the same order as the number of
records.  Collinearity supplies no compression for (5.6).  Thus this
construction decisively kills `Psi`, `Gamma`, and the compound norm
`|Gamma|^2`, but it does **not** kill the positive distance-label charge.

## 6. Consequence

The Gaussian edge-vector gate and the dilated pair-sum gate are closed.
Their excellent finite profiles missed a resonant direction: a ruler arm in
direction `e` is sent by `3(I+J)` onto a second ruler arm in direction
`(-1,-1)`.  A fixed planted clean gadget is harmless because it supplies
only one source vector, but the diagonal ruler arm has `Omega(s^2)` clean
sources by triple-sum pigeonholing, producing a genuinely cubic energy.

Any replacement must prevent a whole clean fibre and a quadratic family of
ordinary edges from occupying two dilation-related one-dimensional arms, or
must pay directly for that parallel-cover structure.  A stand-alone
near-diagonal Gaussian charge cannot do so.

Run `verify_gaussian_edge_vector_two_arm_barrier.py` for exact finite
certificates.
