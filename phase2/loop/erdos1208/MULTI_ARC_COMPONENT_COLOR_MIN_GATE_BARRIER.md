# Multi-arc component color: a polynomial barrier to the uncolored minimum gate

## 1. Outcome

The one-dimensional minimum-weight envelope

\[
 \mathcal G_L
 :=
 \sum_{h\ne0}
 \min\left\{
 M_L(h),{Q_R(h)\over(L-1)^2}
 \right\}T(h)                                         \tag{1.1}
\]

can exceed the true support-weighted Heisenberg mass \(W_L\) by a
polynomial factor on integral distance-Sidon sets of polynomial height.

For arbitrary \(b,L\), there are graph-like distance-Sidon sets with
\(k=2bL\) points and a selected dyadic family such that

\[
 \boxed{
 \mathcal G_L=\Theta(b^3L^5),\qquad
 W_L=\Theta(bL^5),\qquad
 {\mathcal G_L\over W_L}=\Theta(b^2).}                \tag{1.2}
\]

The construction consists of \(b\) disjoint quadratic arcs of length
\(2L\), with a generic choice of their linear and constant terms.
Every parent shift cell has \(b\) rich lines.  Hence \(M_L(h)\) counts
\(b^2\) possible pairs.  The child cell also has \(b\) rich internal
lines.  But genericity makes every cross-arc quotient have occupancy at
most two, so only the \(b\) matching arc colors contribute to \(W_L\).
Formula (1.1) multiplies unrelated parent and child colors and loses
\(b^2\).

This is not a counterexample to the corrected global target: the generic
integral realization below has polynomial, but not critical, height.
It is a sharp barrier to proving that target through (1.1).  The scalar
shift \(h\) is no longer sufficient.  A successful summation must retain
at least the normalized parameter difference
\((h,A_c-A_d)\), or an equivalent component color, until it is matched
to the child line.

The two-layer affine-block theorem does retain this information and does
not suffer the loss in (1.2).  The remaining global problem is therefore
to combine that blockwise additive-energy bound across affine projection
lines, using the endpoint injection only for genuinely isolated blocks.

## 2. The multi-arc model

Let

\[
 R=\{0,\ldots,2bL-1\}
\]

and split it into consecutive blocks

\[
 I_i=\{2Li+s:0\le s<2L\},\qquad 0\le i<b.
                                                               \tag{2.1}
\]

Choose integer parameters \(\gamma_i,C_i\), and define

\[
 f(2Li+s)=s^2+\gamma_i s+C_i.                        \tag{2.2}
\]

For \(1\le q\le L\), the \(2L-q\) internal tails in block \(i\)
satisfy

\[
\begin{aligned}
 f(r+q)-f(r)
 &=2qr+\alpha_{i,q},\\
 \alpha_{i,q}
 &=q^2+\gamma_iq-4iLq.                               \tag{2.3}
\end{aligned}
\]

Thus the selected patch

\[
 p_{i,q}=(q,2q,\alpha_{i,q})                         \tag{2.4}
\]

has richness between \(L\) and \(2L-1\).  For a generic choice of the
parameters, (2.3) has no additional tails outside \(I_i\).

All selected projections lie on the same affine line

\[
 \lambda=2q.
\]

After the quadratic normalization \(F(r)=f(r)-r^2\), the parameter is

\[
 (q,A_{i,q}),\qquad
 A_{i,q}=\alpha_{i,q}-q^2
 =q(\gamma_i-4iL).                                   \tag{2.5}
\]

This last coordinate is the component color discarded by (1.1).

## 3. Exact true weighted mass

Fix one block \(i\), and take \(c>d\).  Its two parent patches have
quotient

\[
\begin{aligned}
 h&=c-d,\\
 \mu&=2h,\\
 \beta&=h^2+h(\gamma_i-4iL).                         \tag{3.1}
\end{aligned}
\]

This is exactly the internal derivative line in block \(i\) at shift
\(h\), and it has \(2L-h\) tails.  There are \(L-h\) parent pairs at
difference \(h\).

Choose the parameters generically so that a pair of parent patches from
distinct blocks has child occupancy at most two.  Such pairs have zero
triple weight.  It follows exactly that

\[
 \boxed{
 W_L
 =b\sum_{h=1}^{L-1}(L-h){2L-h\choose3}
 =\Theta(bL^5).}                                     \tag{3.2}
\]

The construction is a disjoint union only at the level of the selected
supports.  The full point set is globally distance-Sidon.

## 4. The uncolored gate loses \(b^2\)

For every selected parent shift \(q\),

\[
 N_L(q)=b.
\]

Therefore

\[
 M_L(h)=b^2(L-h)\qquad(1\le h<L).                    \tag{4.1}
\]

The derivative cell at shift \(h\) contains the \(b\) internal child
lines from (3.1), each with \(2L-h\) tails.  Hence

\[
 T(h)\ge b{2L-h\choose3}.                            \tag{4.2}
\]

Since \(R\) is an interval of length \(k=2bL\),

\[
 Q_R(h)=\Theta(k^3)
\]

uniformly for \(1\le h<L\).  Consequently

\[
 {Q_R(h)\over(L-1)^2}
 =\Theta(b^3L)
 \ge M_L(h)
\]

apart from harmless absolute constants.  The minimum in (1.1) therefore
chooses \(M_L(h)\), and

\[
\begin{aligned}
 \mathcal G_L
 &\ge
 b^3\sum_{h=1}^{L-1}(L-h){2L-h\choose3}\\
 &=\Theta(b^3L^5).                                   \tag{4.3}
\end{aligned}
\]

Comparison with (3.2) proves (1.2).  Notice that retaining the actual
parent-shift load \(M_L\), while necessary for the single-parabola
barrier, is still insufficient: \(M_L\) knows the shifts but not which
of the \(b\) normalized center coordinates match a child line.

## 5. Polynomial-height distance-Sidon realization

The parameters in (2.2) can be specialized integrally at polynomial
height while imposing all the generic conditions above.

Treat

\[
 \gamma_0,\ldots,\gamma_{b-1},C_0,\ldots,C_{b-1}
\]

as independent variables.  Add the following forbidden equations:

1. every unintended equality between two squared Euclidean distances;
2. every additional incidence of a point of a derivative cell on one of
   the selected internal lines (2.3);
3. for every pair of selected patches from distinct blocks and every
   triple of possible child tails, the simultaneous equations saying
   that all three tails lie on its quotient line.

Each forbidden condition is the zero set of a nonzero polynomial of
bounded degree.

For item 1, orient a cross-block edge by increasing block index.  Its
vertical difference contains \(C_j-C_i\).  Equality for two distinct
edges cannot be an identity: comparison of the independent \(C\)
coefficients first recovers the ordered block pair, and comparison of
the \(\gamma_i,\gamma_j\) coefficients then recovers both local
endpoints.  The same-block case is even simpler.

For item 2, an unintended tail either lies in a different block, when an
independent \(\gamma_j\) or \(C_j\) remains, or crosses a block boundary.
In neither case is (2.3) an identity.

For item 3, two incidence equations may be combined as the sum of their
squares.  They cannot both vanish identically.  If the three child edges
lie internally in one block \(u\), coefficient comparison in
\(\gamma_i,\gamma_j,\gamma_u\) would force the two parent block colors
to agree, contrary to their selection.  A cross-block child edge retains
an independent constant difference.

There are \(O(k^4)\) distance equations, \(O(k^2)\) extra-incidence
equations, and \(O(k^5)\) quotient-triple equations.  The product of all
forbidden polynomials is nonzero and has degree \(k^{O(1)}\).  The grid
nonvanishing lemma therefore supplies integer parameters of size
\(k^{O(1)}\) outside their union.  After a vertical translation, (2.2)
is an integral distance-Sidon set in a square of polynomial side length.

Thus the \(b^2\) loss in (1.2) is a genuine polynomial-height phenomenon,
not a formal parameter configuration.

## 6. Exact finite certificate

The verifier stores the case

\[
 b=4,\qquad L=3,\qquad k=24,
\]

with

\[
\begin{aligned}
 \gamma&=(90762,27201,-10283,-91079),\\
 C&=(-351997,-573877,-50618,-650066).                \tag{6.1}
\end{aligned}
\]

The resulting values \(f(0),\ldots,f(23)\) are

\[
\begin{split}
(&-351997,-261234,-170469,-79702,11067,101838,\\
 &-573877,-546675,-519471,-492265,-465057,-437847,\\
 &-50618,-60900,-71180,-81458,-91734,-102008,\\
 &-650066,-741144,-832220,-923294,-1014366,-1105436).
                                                               \tag{6.2}
\end{split}
\]

All \({24\choose2}=276\) squared distances are distinct.  The twelve
selected patches have exactly their intended supports.  Every cross-arc
parent quotient has occupancy at most two, and

\[
 W_L=96.
\]

On the other hand,

\[
\begin{array}{c|c|c|c}
h&M_L(h)&T(h)&
\min\{M_L(h),Q_R(h)/(L-1)^2\}\\ \hline
1&32&40&32\\
2&16&16&16
\end{array}
\]

so

\[
 \boxed{\mathcal G_L=1536=16W_L=b^2W_L.}             \tag{6.3}
\]

## 7. Consequence for the route

The hierarchy of surviving quantities is now:

\[
\text{raw }Q_RT
\quad\longrightarrow\quad
\text{uncolored minimum gate (1.1)}
\quad\longrightarrow\quad
\text{normalized-parameter colored mass }W_L.
\]

The first arrow loses polynomially on one parabola at intermediate
richness.  The second loses polynomially on the multi-arc family.
Therefore the next viable proof must work with the blockwise correlation

\[
 \sum_x
 r^+_{P_{\theta,\eta}-P_{\theta,\eta}}(x)
 {r_{B_\theta-B_\theta}(x)\choose3},                 \tag{7.1}
\]

and sum (7.1) across \((\theta,\eta)\) without first forgetting \(x\).
Large affine blocks are controlled by the two-layer popular-difference
theorem.  The exact remaining issue is to charge the numerous small
affine blocks without multiplying them by all child lines in the same
shift cell.

## 8. Verification

Run

    python phase2/loop/erdos1208/verify_multi_arc_component_color_min_gate_barrier.py

The verifier checks the polynomial formulae (2.2)--(3.1), all squared
distances, exact intended supports, all parent quotients and child
occupancies, \(W_L=96\), every rich nonhorizontal child line in the two
relevant cells, the interval correlations \(Q_R(h)\), and the exact
factor-16 gap (6.3).
