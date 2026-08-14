# Erdős 838: deletion variance and the cyclic-minimizer fork

**Date:** 2026-08-13
**Status:** exact identities and finite certificates; no unrestricted asymptotic
proof is claimed.

All logarithms are base two unless stated otherwise.  In Sections 1--3,
`V(P)` counts **all** convex subsets, including the empty set.  The first
moment is unaffected by the empty set.  Some reflection-order programs in the
repository report the nonempty count `V_+(P)=V(P)-1`; this convention change
must be made explicitly when comparing tables.

## 1. An exact second-order deletion identity

Let `K` be a uniformly random convex subset of an `n`-point set `P`, and write

\[
 V=V(P),\qquad M=\sum_K |K|,\qquad
 \mu=\frac MV,\qquad \sigma^2=\operatorname{Var}|K|.
\]

For `p\in P`, put `V_p=V(P-p)` and let `\mu_p` be the corresponding mean.
Double-counting a convex set against the points it omits gives

\[
 \sum_pV_p=(n-\mu)V.                                      \tag{1}
\]

Weighting the same incidences by the size of the convex set gives

\[
 \sum_pV_p\mu_p
 =\sum_K |K|(n-|K|)
 =\bigl(n\mu-\mathbb E|K|^2\bigr)V.                       \tag{2}
\]

Consequently, if a deletion is sampled with probability proportional to
`V_p`, then its expected convex-set mean is

\[
 \overline\mu_-=
 \frac{n\mu-\mathbb E|K|^2}{n-\mu}
 =\mu-\frac{\sigma^2}{n-\mu}.                             \tag{3}
\]

This identity is exact.  In particular, at least one deletion satisfies

\[
 \mu(P-p)\leq \mu(P)-\frac{\sigma^2(P)}{n-\mu(P)}.         \tag{4}
\]

Iterating the size-biased deletion kernel down to a singleton gives an exact
variance ladder:

\[
 \mu(P)=\mu(P_1)+
 \mathbb E\sum_{m=2}^n
 \frac{\sigma^2(P_m)}{m-\mu(P_m)},                         \tag{5}
\]

where `P_n=P` and each `P_{m-1}` is sampled from the deletions of `P_m` with
weight `V(P_m-p)`.

There is an equivalent activity form.  For
`Z_P(\lambda)=\sum_K\lambda^{|K|}` and
`\mu_\lambda=\lambda Z'_P(\lambda)/Z_P(\lambda)`,

\[
 \lambda\frac{d}{d\lambda}\mu_\lambda
 =\operatorname{Var}_\lambda |K|.                         \tag{6}
\]

## 2. What (3) would have to prove

The previously isolated mean-size criterion says that the unrestricted upper
coefficient `1/2` would follow if every minimum-count configuration satisfied

\[
 \mu(P)\geq \log_2 n-O(1).                                \tag{MS}
\]

Equation (5) shows that the naive sufficient pointwise variance bound would be
`\sigma^2\geq1/\ln2-o(1)`: since
`\sum_{m\le n}1/m=\ln n+O(1)`, this would yield
`\mu\geq(1/\ln2)\ln n-O(1)=\log_2n-O(1)`.

That pointwise route is false at the exact small minimizers.  The variances
through `n=9` are roughly `0.22,0.49,0.57,0.66,0.66,0.68,0.68,0.71`, far below
`1/\ln2=1.44269...`.  Thus a successful use of (5) must be amortized across
the deletion chain, must exploit the fact that the parent is a global
minimum, or must obtain the missing drift from a statistic richer than the
variance.

For a minimum configuration `P_n`, (1) also gives the exact deletion excess

\[
 E_n:=\sum_pV(P_n-p)-n f(n-1)
 =(n-\mu(P_n))f(n)-n f(n-1)\geq0.                          \tag{7}
\]

At the exact nine-point minimizer, the nine deletions have all-subset counts
`114` six times and `115` three times.  Hence `E_9=3`, exceptionally close to
the formal minimum zero.  At eight points the corresponding excess is `12`.
This near-tightness is a concrete stability signal, but no general upper bound
on `E_n` is currently known.

### 2.1 A sharper one-parameter target

Jensen gives a particularly clean sufficient condition for (MS).  Under the
uniform measure on convex subsets,

\[
 \frac{Z_P(1/2)}{Z_P(1)}=\mathbb E\,2^{-|K|}
 \geq 2^{-\mu(P)}.                                        \tag{8}
\]

It would therefore suffice to prove

\[
 \boxed{\quad nZ_P(1/2)\leq C Z_P(1)\quad}                \tag{HW}
\]

with an absolute `C`, either universally or just for minimum-count
configurations.  Even the weaker right-hand side `n^{o(1)}Z_P(1)` would give
`\mu(P)\geq(1-o(1))\log_2n` and close the normalized coefficient.  In
probabilistic language, `Z_P(1/2)` is the expected number of convex subsets in
a Bernoulli-`1/2` thinning of `P`.

The exact `n=8,9` minimizers have

\[
 nZ_P(1/2)/Z_P(1)=1.42544\ldots,\quad1.456\ldots,
\]

respectively.  Balanced Pascal cells make this ratio decrease, for example
from `1.2721` at `T_{4,2}` to `0.8104,0.3659,0.1974` at the central cells in
rows `8,16,32`.  Thus (HW) passes the principal exact stress families currently
available.  It is strictly stronger than (MS), and at present remains a
conjectural target.

The tempting sufficient strengthening
`\mu_{1/2}\geq\log_2n-1` is false.  Exact rational planar records at `n=24`
and `30` have half-activity means `3.5623676<\log_2(24)-1` and
`3.8243197<\log_2(30)-1`.  Their actual half-weight ratios remain only
`1.68614` and `1.73021`.  Thus the partition-function ratio is the robust
target; that pointwise tilted-mean surrogate is not.

The ordinary long-braid descent does not prove (HW): there is an exact
ten-wire packet for which the lexicographically better side at `z=1` has a
larger value at `z=1/2`.  Any proof must therefore be global or amortized, not
packetwise monotone.

## 3. Exact small minima and convention correction

The exhaustive reflection-order and realizable-order-type searches give:

\[
 f(8)=114,\qquad f(9)=169,                                \tag{9}
\]

when the empty set is counted, as in the official problem.  The matrix traces
are the nonempty values `113` and `168`.  Direct hull enumeration independently
certifies the profiles

\[
\begin{aligned}
n=8:&\quad 1+8z+28z^2+56z^3+21z^4,\\
n=9:&\quad 1+9z+36z^2+84z^3+36z^4+3z^5.
\end{aligned}                                             \tag{10}
\]

For `n=9`, (9) gives

\[
 \mu=\frac{492}{169},\qquad
 \sigma^2=\frac{21576}{28561}.                            \tag{11}
\]

These exact values are discovery data, not asymptotic evidence by themselves.

## 4. The cyclic three-cluster lead is rigorously excluded

The unique realizable nine-point lexicographic minimum is 3-decomposable.  In
the sorted-coordinate labels used by the certificate, its three clusters are

\[
 \{0,1,5\},\qquad\{2,3,4\},\qquad\{6,7,8\}.                \tag{12}
\]

Exact projection orders put each of these clusters between the other two in
one of three directions.  The eight-point minimum has the analogous unique
`3,3,2` partition.  This is notable because cyclic three-direction geometry is
not covered by the proved barrier for vertical prescribed-mixed-triple
blow-ups.

Fitting a three-map rational self-affine system to (11) reproduces the
nine-point order type at depth two.  Exact reverse-product evaluation of the
best of the `6^3` vertex identifications gives nonempty counts

\[
 7,\ 168,\ 22862,\ 54472059,\ 24596520332047
\]

at sizes `3,9,27,81,243`.  Their normalized logarithms are approximately

\[
 1.118,\ 0.736,\ 0.640,\ 0.639,\ 0.708.                  \tag{13}
\]

The apparent dip at depths three and four is therefore not stable even at the
next computed depth.  More decisively, an exact max-plus version of the same
opposite-product evaluator gives maximum convex-subset sizes

\[
 3,\ 5,\ 9,\ 16,\ 28,\ 50                                 \tag{14}
\]

through depth six.  The whole point set has only three hull vertices at every
one of these depths, so (13) is a genuinely internal phenomenon.  The
obstruction is now rigorous.  For two certified child blocks
`T_0=F_0\circ F_0` and `T_1=F_0\circ F_1`, every one of the `2^r` points
`T_{\epsilon_1}\cdots T_{\epsilon_r}(q)` forms a single strict convex chain
at IFS depth `2r+1`.  Consequently, when `N=3^{2r+1}`,

\[
 V(P_{2r+1})\geq 2^{2^r}=2^{(N/3)^{\log_9 2}}.          \tag{15}
\]

This is stretched-exponential, far above the quasipolynomial regime.  The
all-depth rational slope-cone proof and exact checker are in
`agent_cyclic_ifs_kill/`.

## 5. Current attack decision

The attack should proceed on two tracks.

1. **Lower/identity track.**  Prove (MS) for global minimum configurations by
   amortizing the full reflection-order boundary vector.  Equation (3) says
   exactly how much drift a second-moment argument must recover, and (7)
   supplies a possible stability charge.
2. **Construction track.**  The fitted three-cluster minimizer is closed by
   (15).  More generally, a recurrent finite cone state with two independent
   descendants produces stretched-exponential mass.  A quasipolynomial cyclic
   construction must therefore have an eventually nonbranching cone automaton;
   combined with complementary endpoint capacity, this points back toward the
   already sharp `1/2` one-multi-occupancy mechanism.  Any genuine upper escape
   needs growing state complexity or a different mixed-triple geometry.

The first track remains the primary route.  The second is now a sharply posed
escape search rather than a vague appeal to triangular symmetry.
