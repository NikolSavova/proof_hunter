# Unit reflection orders: an exponential Frobenius-alignment barrier

## Verdict

There is a scalable, stretchable, once-per-root type-\(A\) reflection order
on which the separate forward and reverse path matrices grow much faster
between activities \(1/2\) and \(1\) than the paired partition function.
The discrepancy is an exponentially worsening Frobenius angle:

\[
\frac{\kappa_n(1)}{\kappa_n(1/2)}
  =\Theta\!\left((3/4)^{n/2}\right),
\]

where

\[
\kappa_n(z)=
\frac{\langle A_n(z),B_n(z)\rangle_F-n}
{\sqrt{(\|A_n(z)\|_F^2-n)(\|B_n(z)\|_F^2-n)}}.
\]

Thus a proof of half weight cannot first compare the Frobenius pairing with
the product of the two marginal Frobenius norms up to polynomial, or even
\(n^{o(1)}\), loss.  Unit normalization, root completeness, reflection
betweenness, and straight-line stretchability do not repair that comparison.

This is **not** a counterexample to half weight.  On the same family

\[
H_n=\frac{nF_n(1/2)}{F_n(1)}
  =\Theta\!\left(n(3/4)^{n/2}\right)\longrightarrow0.
\]

The family therefore gives a useful proof dichotomy: exponential
anti-alignment is possible, but here it is paid by exponentially abundant
one-sided path mass.  A successful matrix proof has to retain that payment
instead of replacing the two arrays by marginal norms.

## 1. Matrix notation

For a type-\(A_{n-1}\) reflection order \(R\), put

\[
B_R(z)=\prod_R(I+zE_{ji}),\qquad
A_R(z)=\prod_{R^{\rm rev}}(I+zE_{ji}).
\]

The off-diagonal pairing and energies are

\[
\begin{aligned}
Q_R^\circ(z)&=\langle A_R(z),B_R(z)\rangle_F-n,\\
E_A(z)&=\|A_R(z)\|_F^2-n,\qquad
E_B(z)=\|B_R(z)\|_F^2-n.
\end{aligned}
\]

The convex-face polynomial, including the empty face, is

\[
F_R(z)=1+nz+Q_R^\circ(z).
\]

The quotient \(\kappa_R(z)=Q_R^\circ(z)/\sqrt{E_A(z)E_B(z)}\)
is the cosine between the off-diagonal forward and reverse endpoint arrays.

## 2. A stretchable alternating reflection order

Fix \(M=4n+1\) and take

\[
p_i=(i,(-1)^iM^{n-i})\quad(0\le i\le n-3),\qquad
p_{n-2}=(n-2,0),\quad p_{n-1}=(n-1,0).
\]

For \(i<j<k\),

\[
\det(p_j-p_i,p_k-p_i)
=(k-j)y_i-(k-i)y_j+(j-i)y_k.
\]

The first term dominates the other two because \(M>2n\).  Hence

\[
\operatorname{sign}\det(p_j-p_i,p_k-p_i)=(-1)^i. \tag{1}
\]

In particular the points are in general position.  Sorting all slopes gives
a stretchable reflection order in which every positive root occurs exactly
once.  Equation (1) gives the reflection packet axiom:

\[
(ij)<(ik)<(jk)\quad\text{if \(i\) is even},
\]

and the reverse order if \(i\) is odd.

## 3. Exact temporal-path classification

Consider an increasing-vertex path

\[
i=v_0<v_1<\cdots<v_r=j.
\]

The comparison between the consecutive root times
\((v_t,v_{t+1})\) and \((v_{t+1},v_{t+2})\) has sign determined by
the parity of \(v_t\).  Consequently:

- a forward-time path of at least two edges must have
  \(v_0,\ldots,v_{r-2}\) all even;
- a reverse-time path of at least two edges must have
  \(v_0,\ldots,v_{r-2}\) all odd.

Thus, for every endpoint pair \(i<j\), one of the two path entries is exactly
\(z\), while the other is a polynomial depending only on \(d=j-i\):

\[
\boxed{
R_d(z)=z+z^2\sum_{s=1}^{d-1}(1+z)^{\lfloor(s-1)/2\rfloor}.
} \tag{2}
\]

If \(i\) is even, \(B_{ji}(z)=R_d(z)\) and \(A_{ji}(z)=z\);
if \(i\) is odd, the two are interchanged.

This uses the complete unit factorization, not merely
\(A(z)=B(-z)^{-1}\).  It immediately gives the exact partition polynomial

\[
\boxed{
F_n(z)=1+nz+\sum_{d=1}^{n-1}(n-d)zR_d(z).
} \tag{3}
\]

It also gives the exact marginal energies

\[
\begin{aligned}
E_B(z)
 &=\sum_{\substack{i<j\\i\ {\rm even}}}R_{j-i}(z)^2
   +\sum_{\substack{i<j\\i\ {\rm odd}}}z^2,\\
E_A(z)
 &=\sum_{\substack{i<j\\i\ {\rm odd}}}R_{j-i}(z)^2
   +\sum_{\substack{i<j\\i\ {\rm even}}}z^2.       \tag{4}
\end{aligned}
\]

## 4. Exact asymptotic consequence

Fix \(z>0\) and write \(q=1+z\).  The finite geometric sum in (2) gives,
with constants depending only on \(z\),

\[
R_d(z)=\Theta_z(q^{d/2}).                           \tag{5}
\]

Using \(s=n-d\) in (3),

\[
\sum_{d=1}^{n-1}(n-d)q^{d/2}
=q^{n/2}\sum_{s=1}^{n-1}s q^{-s/2}
=\Theta_z(q^{n/2}).
\]

Therefore

\[
Q_n^\circ(z)=\Theta_z(q^{n/2}),\qquad
F_n(z)=\Theta_z(q^{n/2}).                           \tag{6}
\]

For (4), one longest rich entry gives the lower bound, while summing the
two geometric tails over its start and end gives the upper bound.  Hence

\[
E_A(z)=\Theta_z(q^n),\qquad E_B(z)=\Theta_z(q^n).   \tag{7}
\]

Combining (6)--(7) proves

\[
\boxed{\kappa_n(z)=\Theta_z(q^{-n/2}).}             \tag{8}
\]

At the two half-weight activities this yields three sharply different
scales:

\[
\begin{aligned}
\frac{\sqrt{E_A(1)E_B(1)}}{\sqrt{E_A(1/2)E_B(1/2)}}
  &=\Theta((4/3)^n),\\
\frac{\kappa_n(1)}{\kappa_n(1/2)}
  &=\Theta((3/4)^{n/2}),\\
\frac{Q_n^\circ(1)}{Q_n^\circ(1/2)}
  &=\Theta((4/3)^{n/2}).                          \tag{9}
\end{aligned}
\]

The first line is an extremely strong marginal-norm dilation.  Half of its
exponent is canceled by the relative rotation of the endpoint arrays.  The
last line is still exponentially stronger than the \(n^{1-o(1)}\) dilation
needed for Erdős 838, which explains why the family itself is harmless:

\[
H_n=\Theta(n(3/4)^{n/2}).                           \tag{10}
\]

## 5. A finite marginal-data collision

There is a complementary exact obstruction already on six wires.  Consider
the two reduced words

\[
\begin{aligned}
w_1={}&(0,2,1,3,2,1,4,3,2,1,0,1,2,4,3),\\
w_2={}&(0,3,2,1,2,4,3,2,1,0,1,4,3,2,3).
\end{aligned}
\]

For \(w_1\), the multiset of all polynomial entries of \(A\) equals the
multiset of entries of \(B\) for \(w_2\), and conversely.  Thus the unordered
pair of complete entry-polynomial histograms is identical.  In particular,
every symmetric entrywise marginal statistic, including all entrywise
\(\ell_p\) sums at every activity, is identical.

Nevertheless the nonempty paired profiles are

\[
(6,15,20,8,1)\qquad\text{and}\qquad(6,15,20,8).
\]

After adding the empty face their half-weight ratios are respectively

\[
\frac{345}{272}\quad\text{and}\quad\frac{129}{100}.
\]

The missing information is exactly which forward entry is paired with which
reverse entry.  This finite collision does not by itself address asymptotic
half weight, but it confirms algebraically what the alternating family shows
at exponential scale.

The statement is about entrywise/Frobenius marginals.  It does not assert
that the two matrices have identical singular spectra, so it does not rule
out every possible Schatten argument.  It rules out a Schatten or Hölder
strategy only when that strategy first discards the relative endpoint
coupling.

## 6. What survives

The barrier suggests a precise matrix dichotomy rather than abandoning the
network route.

1. If the endpoint arrays remain sufficiently aligned across activities,
   a marginal energy-dilation estimate may prove half weight.
2. If alignment drops exponentially, the proof must charge the rich
   one-sided path complex responsible for (7), as (3) does explicitly in the
   alternating family.

The necessary inequality therefore has to be **total-count capped** or
history retaining.  A bare reverse Cauchy inequality of the form

\[
Q_R^\circ(z)\ge n^{-O(1)}\sqrt{E_A(z)E_B(z)}
\]

is false even for stretchable unit reflection orders.  So is the weaker
claim that the alignment quotient between activities one and one-half is
\(n^{-o(1)}\).  Any viable Frobenius proof must add the one-sided internal
mass as an explicit compensating term.

## 7. Verification

Run

    python3 phase2/loop/erdos838/agent_cyclic_stem_hw/reflection_frobenius_barrier.py

The verifier:

- constructs the integral point sets and checks every determinant;
- sorts slopes exactly and checks every reflection packet;
- multiplies all unit transvections as polynomial matrices;
- verifies (2) entry by entry through fourteen wires;
- evaluates (3)--(4) with exact rational arithmetic through \(n=240\);
- checks the six-wire entry-histogram collision; and
- writes reflection_frobenius_barrier_certificate.json.

No floating-point arithmetic is used for a claimed identity or inequality;
logarithms are used only for the displayed asymptotic diagnostics.
