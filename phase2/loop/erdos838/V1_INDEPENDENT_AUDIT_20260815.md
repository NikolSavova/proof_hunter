# V1 independent audit: hinged Kraft and grammar half-closure

**Date:** 2026-08-15. **Verdict:** `MINOR_REPAIR`, repaired in the source
artifact and reverified. All logarithms are base two.

## 1. Claims audited

This audit independently reconstructed the proofs in

- **agent_nonstrong_ramp_search/HINGED_DIAGONAL_FLOOR_LOG.md**, and
- **agent_nonstrong_ramp_search/NONSTATIONARY_HOMOGENEOUS_HALF_CLOSURE.md**.

The claims are:

1. the mixed cap/cup profile words form a prefix-free code;
2. the resulting hinged Kraft inequality is exact;
3. a finite variable-arity transition grammar has cap-plus-cup cycle reward
   at least its logarithmic growth rate;
4. the corresponding vertical construction has face coefficient at least
   one half;
5. stationarity is unnecessary when every level has a common child size,
   provided both endpoint recurrences use the same target chart and the
   final cap/cup product is an actual face bank.

## 2. Prefix-code reconstruction

For a point or ordered-graph vertex \(i\), let \(u_i(r)\) be the minimum
last edge label among \(r\)-edge increasing paths ending at \(i\), and let
\(d_i(s)\) be the minimum first edge label among \(s\)-edge decreasing paths
starting at \(i\). Both lists are nondecreasing. Merge them, writing zero
for a \(u\)-entry and one for a \(d\)-entry. The resulting word \(w_i\) has
length

\[
             |w_i|=\alpha(i)+\beta(i),
\]

where \(\alpha(i)\) is the largest cap reward with left endpoint \(i\), and
\(\beta(i)\) is the largest cup reward with right endpoint \(i\).

For \(i<j\), put \(t=\lambda(i,j)\) and define

\[
 x=\min\{r:u_i(r)>t\},\qquad
 y=\min\{s:d_j(s)>t\}.
\]

Appending \(ij\) to the path realizing \(u_i(x-1)\) gives
\(u_j(x)\le t\); prepending it to the path realizing \(d_j(y-1)\) gives
\(d_i(y)\le t\). Thus, in the first \(x+y-1\) positions, \(w_i\) has at
most \(x-1\) zeroes while \(w_j\) has at least \(x\) zeroes. This prefix
exists in both words, so the words differ before either ends. The family is
prefix-free and Kraft gives

\[
             \sum_i2^{-\alpha(i)-\beta(i)}\le1.           \tag{1}
\]

No geometric statement beyond the ordered distinct edge labels is used in
this step.

## 3. Finite-grammar reconstruction

Restrict the transition multigraph to a reachable critical strongly
connected component \(K\), retaining the induced macro positions and
recomputing their endpoint rewards. If \(M\) is its transition-count matrix,
\(\Lambda=\rho(M)\), and \(r\) is a positive right Perron vector, give an
individual edge \(e:s\to t\) probability

\[
                    p_e={r_t\over\Lambda r_s}.
\]

Under the stationary vertex law, these probabilities have entropy rate
\(\log\Lambda\): the Perron-potential terms telescope. Row Kraft and relative
entropy give

\[
                    \log\Lambda\le \mathbb E(c_e+u_e).
\]

The stationary edge law is a circulation, hence a convex combination of
cycle flows. Some cycle has mean \(c+u\) at least \(\log\Lambda\). Therefore

\[
                    \rho_C+\rho_U\ge\log\Lambda.          \tag{2}
\]

Repeating a cap-maximizing cycle for depth \(d\) contributes
\((\rho_C\log\Lambda/2)d^2+O(d\log d)\), and similarly for cups. The original
write-up then jumped directly to their product. The missing justification
was small but real: one must put both banks beneath two positions of one
actual parent row. Because \(\Lambda>1\), some row of \(K\) has two retained
positions. Strong connectivity sends their two child states to the two
maximizing cycles in bounded depth; cycle-period adjustments also cost only
bounded depth. The ordered two-position macro support then supplies the
actual cap-times-cup face bank. This paragraph is now present in the source
report. It changes only the lower-order error and yields

\[
 {\rho_C+\rho_U\over2\log\Lambda}\ge {1\over2}.           \tag{3}
\]

## 4. Nonstationary homogeneous reconstruction

At level \(k\), let every child have common log-size \(L_{k-1}\), let the
macro arity have log \(q_k\), and require that the cap and cup recurrences at
a hinged position call the same child chart. Row Kraft supplies one position
with \(\alpha+\beta\ge q_k\). For

\[
 E_k=\min_\theta(\log C_{k,\theta}+\log U_{k,\theta}),
\]

the exact endpoint recurrences give

\[
                    E_k\ge E_{k-1}+q_kL_{k-1}.            \tag{4}
\]

Hence

\[
 E_{d-1}\ge {1\over2}
 \left(L_{d-1}^2-\sum_{k<d}q_k^2\right).                 \tag{5}
\]

If the final parent contains an actual same-chart cap/cup splice, then
\(V_d\ge2^{E_{d-1}}\). Bounded arity gives

\[
                    \log V_d\ge {1\over2}L_d^2-O(L_d).   \tag{6}
\]

The common-size, same-target, and final-splice assumptions are used exactly
where stated. For unequal children, profile length is not the multiplier in
the endpoint recurrence, so this proof does not extend by averaging.

## 5. Numerical reruns

The repaired finite-grammar artifact returned:

~~~text
PASS: universal hinged Kraft regression; arbitrary_n4_edge_orders=720;
variable_arity=(rho,entropy,length_cycle,cap_cycle,cup_cycle)=(4,2,2,2,2);
n8_stretchable_h=3; n8_min_determinant=2000; n8_kraft_sum=1
~~~

The nonstationary homogeneous artifact returned:

~~~text
PASS: nonstationary homogeneous half closure;
exact_ledgers=16142517; arbitrary_arity_ledgers=21840;
skew_binary_instances=79; chart_rows=860; final_charts=41
~~~

## 6. Dependency and scope audit

The proof depends only on the exact endpoint recurrences for ordered vertical
substitution, prefix-free Kraft, Perron--Frobenius on a finite nonnegative
matrix, circulation decomposition, and an actual final cap/cup face product.
It does **not** invoke the desired unrestricted Erdős 838 lower bound, a
least-counterexample hypothesis, or any unproved face-number inequality.

It also does **not** prove the unrestricted theorem. The finite-grammar result
does not cover a genuinely growing state space, and the nonstationary result
does not cover heterogeneous child sizes or loss of the same-target/final
splice. Those are precisely the remaining construction-side escape routes.
