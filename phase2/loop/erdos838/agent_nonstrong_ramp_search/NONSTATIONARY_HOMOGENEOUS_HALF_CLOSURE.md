# Nonstationary homogeneous vertical grammars: an exact half closure

**Date:** 2026-08-15. All logarithms are base two. This note concerns
vertical substitutions with a common child at each level. It does not claim
a theorem for heterogeneous child states.

## Verdict

Stationarity and a finite transition-state set are unnecessary for a
homogeneous vertical substitution. At level \(k\), allow an arbitrary
chart set \(\Theta_k\), whose cardinality may grow with \(k\). For every
\(\theta\in\Theta_k\), let the macro \(S_{k,\theta}\) have the same arity
\(m_k\). Its position \(i\) calls one chart
\(\tau_{k,\theta}(i)\in\Theta_{k-1}\). All child configurations at level
\(k-1\) have the same size \(N_{k-1}\), although their endpoint banks may
differ. Thus

\[
 N_k=m_kN_{k-1},\qquad q_k=\log m_k,\qquad
 L_k=\log N_k=\sum_{j\leq k}q_j.                            \tag{1}
\]

The two endpoint recurrences at a hinged position must call the *same*
target chart \(\tau_{k,\theta}(i)\). At the last level, assume that the
ordinary-face recurrence contains a two-position splice whose left cap
bank and right cup bank call one common chart at level \(d-1\). Under these
explicit compatibility hypotheses, the macros, order types, chart menus,
and transition maps may otherwise change arbitrarily, and

\[
 \boxed{
 \log V_d\geq
 {1\over2}\left(L_{d-1}^2-\sum_{k<d}q_k^2\right).}          \tag{2}
\]

Consequently, if \(q_*=\max_{k\leq d}q_k\), then

\[
 \log V_d
 \geq {1\over2}L_d^2-{3\over2}q_*L_d+q_*^2.                \tag{3}
\]

In particular, bounded arity \(m_k\leq B\) gives

\[
 \log V_d\geq {1\over2}L_d^2-O_B(L_d),                     \tag{4}
\]

and the weaker mesh condition \(q_*=o(L_d)\) gives coefficient at least
\(1/2-o(1)\). Thus growing chart complexity by itself cannot realize a
sub-half ramp while common child sizes and the same-chart final splice are
retained.

The homogeneous-size and common-target hypotheses are doing real work. Row
Kraft plus the chain rule does not by itself replace them: for unequal
children, a profile length counts support positions, whereas the endpoint
recurrence is weighted by the sizes of the *other* support blocks. A
two-position skew example below shows that replacing the latter by profile
length times anchor log-size can overestimate the actual multiplier by an
arbitrarily large factor. The unclosed residue is therefore heterogeneous
endpoint-bank alignment, not nonstationarity by itself.

## 1. Exact endpoint recurrence

For the \(x\)-ordered macro \(S_{k,\theta}\), let
\(\alpha_{k,\theta}(i)\) be the maximum cap reward with macro minimum
\(i\), and let \(\beta_{k,\theta}(i)\) be the maximum cup reward with macro
maximum \(i\). The universal hinged Kraft theorem gives, in every row,

\[
 \sum_{i=1}^{m_k}
 2^{-\alpha_{k,\theta}(i)-\beta_{k,\theta}(i)}\leq1.        \tag{5}
\]

Hence some position \(i_{k,\theta}\) obeys

\[
 \alpha_{k,\theta}(i_{k,\theta})
 +\beta_{k,\theta}(i_{k,\theta})\geq q_k.                  \tag{6}
\]

Write \(C_{k,\theta},U_{k,\theta}\) for the two endpoint banks in chart
\(\theta\), and put \(c_{k,\theta}=\log C_{k,\theta}\) and
\(u_{k,\theta}=\log U_{k,\theta}\). The homogeneous-size substitution
gives, for \(t=\tau_{k,\theta}(i)\),

\[
 \begin{aligned}
 c_{k,\theta}&\geq
 c_{k-1,t}+\alpha_{k,\theta}(i)L_{k-1},\\
 u_{k,\theta}&\geq
 u_{k-1,t}+\beta_{k,\theta}(i)L_{k-1}.
 \end{aligned}                                             \tag{7}
\]

Indeed, use an endpoint object in the distinguished child and choose one
arbitrary point independently in each of the other positions of the macro
cap or cup support. If the exact enumerator supplies factors
\(1+N_{k-1}\), (7) only discards a positive lower-order gain.

Define the universal-in-chart potential

\[
 E_k=\min_{\theta\in\Theta_k}
       \{c_{k,\theta}+u_{k,\theta}\}.                       \tag{8}
\]

Add (7) for the *same* position \(i_{k,\theta}\). Both terms use its same
target chart \(t\), so (6) and (8) give, for every parent chart,

\[
 c_{k,\theta}+u_{k,\theta}
 \geq E_{k-1}+q_kL_{k-1}.
\]

Taking the minimum over \(\theta\) yields

\[
                 E_k\geq E_{k-1}+q_kL_{k-1}.               \tag{9}
\]

No state is followed, no cycle is selected, and no limiting frequency is
used. The minimum makes chart inheritance explicit and remains valid for a
different, arbitrarily large chart menu at every level.

## 2. Telescoping and the final splice

Iteration of (9) gives

\[
 \begin{aligned}
 E_{d-1}
 &\geq\sum_{k<d}q_kL_{k-1}\\
 &=\sum_{k<d}\sum_{j<k}q_jq_k\\
 &={1\over2}\left(L_{d-1}^2-\sum_{k<d}q_k^2\right).
 \end{aligned}                                             \tag{10}
\]

By the stated final-splice hypothesis, the left cap bank and right cup bank
call one common chart \(\phi\in\Theta_{d-1}\). They form a convex spanning
bank, so

\[
 V_d\geq C_{d-1,\phi}U_{d-1,\phi}\geq2^{E_{d-1}}.           \tag{11}
\]

Equations (10)--(11) prove (2). Since \(q_d\leq q_*\),
\(L_{d-1}\geq L_d-q_*\), and

\[
                  \sum_{k<d}q_k^2\leq q_*L_{d-1},          \tag{12}
\]

we obtain

\[
 \begin{aligned}
 \log V_d
 &\geq {1\over2}(L_d-q_*)^2
       -{1\over2}q_*(L_d-q_*)\\
 &= {1\over2}L_d^2-{3\over2}q_*L_d+q_*^2,
 \end{aligned}                                             \tag{13}
\]

which is (3). If \(m_k\leq B\), then \(q_*\leq\log B\), proving
(4). More generally, \(q_*=o(L_d)\) and (12) make both losses in (2)
subquadratic.

The square-mesh term in (2) is exact for this ledger:

\[
 \sum_{k<d}q_kL_{k-1}
 ={1\over2}L_{d-1}^2-{1\over2}\sum_{k<d}q_k^2.             \tag{14}
\]

Thus a macroscopic entropy jump is the only way the homogeneous ledger can
lose a positive quadratic fraction.

## 3. Entropy wording

For a common \(m_k\)-ary layer, a uniform random leaf chooses each macro
position with probability \(1/m_k\). Its conditional entropy is exactly
\(h_k=q_k\). Row Kraft (5), equivalently rowwise cross-entropy, says

\[
 h_k\leq {1\over m_k}\sum_i
       (\alpha_{k,\theta}(i)+\beta_{k,\theta}(i)).           \tag{15}
\]

The max-plus proof above is stronger than averaging (15): it chooses one
hinged position satisfying (6), so cap and cup rewards use the same child
scale \(L_{k-1}\). The chain-rule identity \(\sum h_k=L_d\) then becomes
exactly the quadratic telescope (14).

For a genuinely heterogeneous node, a uniform random leaf instead chooses
position \(i\) with probability proportional to the number \(n_i\) of
leaves below that position. Row Kraft still gives

\[
 H((n_i/\sum_jn_j)_i)
 \leq\sum_i {n_i\over\sum_jn_j}
          (\alpha(i)+\beta(i)),                            \tag{16}
\]

but (16) is not the endpoint multiplier. A cap or cup supported at \(i\)
chooses points in specified *sibling* blocks, so its logarithmic reward is
a sum of terms \(\log(1+n_j)\), not
\((\alpha(i)+\beta(i))\log n_i\). This covariance and incidence information
is absent from row Kraft.

## 4. Exact skew-child obstruction to the naive martingale

Take the genuine two-position macro. Its two hinged lengths are both one,
so its Kraft row is exact:

\[
                         2^{-1}+2^{-1}=1.                  \tag{17}
\]

Give the left child \(M=2^t\) points and the right child one point. For the
left anchor, the cap recurrence has the exact outer multiplier

\[
                         1+n_{\rm right}=2.                \tag{18}
\]

The tempting replacement of this multiplier by
\(n_{\rm left}^{\ell}=M\) is already false for every \(t>1\), and its
logarithmic error is \(t-1\), arbitrarily large despite arity two and exact
Kraft equality. For the right anchor the cup multiplier is \(1+M\).
Thus the support weight follows the sibling selected by the geometric
profile, not the anchor sampled by the leaf law.

This example is not a sub-half geometric construction: binary strong trees
have a separate all-tree payment. It is an exact obstruction to the
proposed inference from row Kraft and chain rule alone. Any extension of
(2) to heterogeneous nonstrong grammars must retain at least one of:

1. the weighted identities of the sibling blocks in the cap and cup
   witnesses;
2. a compatible one-turn/Ferrers splice coupling cap-rich left children to
   cup-rich right children; or
3. a global all-tree theorem in the relevant changing projection charts.

The finite Perron proof supplied this alignment through a recurrent
critical component with comparable child growth. The homogeneous theorem
supplies it through common sizes, a common target at each hinge, and a
same-chart final splice. Neither mechanism is present in (16) alone.

## 5. Verified scope

The companion verifier performs the following checks.

1. It exhausts every sequence \(q_k\in\{1,2,3\}\) through eight levels and
   every split \(q_k=\alpha_k+\beta_k\), checking (7)--(14) with integer
   arithmetic.
2. It exhausts all arity sequences \(m_k\in\{2,3,4,5\}\) through seven
   levels using high-precision logarithms and the sharp integer reward
   \(\lceil\log m_k\rceil\).
3. It checks the bounded-arity corollary and the exact skew-child
   obstruction (17)--(18) for \(2\leq t\leq80\).
4. It propagates 40 nonstationary complete-prefix layers through a chart
   menu growing from one to 41 charts, with changing transition maps, and
   checks the universal-in-chart minimum after every row.

The report therefore closes arbitrary depth-dependent homogeneous sizes,
growing chart menus, and changing transitions under the same-target and
final-splice hypotheses. Heterogeneous child sizes or a noncommon final
chart remain the next construction-side residue.
