# V5 independent audit: mixed Hall assembly and low-rank replacement

**Date:** 2026-08-15. **Verdict:** **PASS**. All logarithms are base two.

## 1. Package reconstructed

This audit independently read and reconstructed:

- **agent_coxeter_global_half/ABSTRACT_MIXED_HALL_ASSEMBLY.md**;
- **agent_coxeter_global_half/JOINT_DETACHED_BANK_RANK_PROMOTION.md**;
- **agent_coxeter_global_half/GLOBAL_RANK_THREE_ES4_REPLACEMENT_CODE.md**;
- the supporting **agent_coxeter_global_half/LABEL_REPLACING_ES_MIXED_CODE.md**.

The package separates three issues which must not be conflated:

1. enough compatible outputs for every weighted history subfamily;
2. recovery of the history from an unmarked output; and
3. reuse of one physical output by several local banks.

Each theorem controls exactly the issue it claims to control.

## 2. Weighted Hall and recovery

For a local history family with demand \(d(H)=Dw(H)\), a fractional decoder
of output capacity \(\lambda\) is a flow in the bipartite
history--compatible-output graph. Max-flow/min-cut gives the exact condition

\[
 D\sum_{H\in X}w(H)
 \le \lambda\left|\bigcup_{H\in X}\Gamma(H)\right|
 \quad\text{for every history subfamily }X.             \tag{1}
\]

This condition controls load but not recovery: arbitrarily many histories
could send tiny flow to one output. The report therefore records recovery
fibre separately. When every history can use a common bank \(\mathcal B\)
and

\[
 |\mathcal B|\ge\sum_H\lceil d(H)\rceil,                \tag{2}
\]

consecutive disjoint blocks give load one and fibre one. With \(L\) formal
copies of the bank, (2) with \(L|\mathcal B|\) gives physical load and
recovery list at most \(L\).

The block construction is exact: a physical output identifies at most one
slot in each formal copy, and the slot's block index identifies its source
record. No geometric mark is being silently retained.

## 3. Global trace-bank overlap

If local decoders are superposed, an output \(F\) has load and recovery list
at most the local bounds times

\[
 \delta(F)=|\{a:F\in\mathcal B_a\}|.                    \tag{3}
\]

For the stated genuine two-sided trace banks, a rank-\(r\) output can use
only an interior consecutive pair \(v_iv_{i+1}\), with
\(2\le i\le r-2\). The inherited order determines the side sign, so

\[
                         \delta(F)\le r-3.               \tag{4}
\]

This is sharp on the saved alternating convex polygon. The argument does
not apply to unmarked banks indexed only by a coherent root; the saved
coherent-root example has overlap equal to the number of roots. Such roots
must be pooled into one Hall instance or assigned trace-owned outputs.

## 4. Matching-star rank promotion

In the balanced matching star, there are \(2m^3\) rank-three records, each
with demand \(m/2\), so total demand is \(m^4\). The detached rank-at-most-two
side bank has \(m(m+1)\) faces and therefore forces load

\[
                         {m^3\over m+1}=\Theta(N^2).      \tag{5}
\]

Even every ambient rank-at-most-three set has only \(O(N^3)\) possible
outputs, forcing polynomial load. This is a full-cut obstruction and cannot
be repaired by a different ownership rule.

On the exact construction, however, each side cloud is homogeneous and all
its four- and five-subsets are ordinary. For \(m\ge47\), fourteen formal
copies of the two rank-four banks contain all ceiling-demand slots. For
\(m\ge70\), the two rank-five banks contain them with one copy. The block
allocation therefore gives, respectively, load/list at most \(14\), and
load/fibre exactly one. The inequalities are elementary polynomial
comparisons and were rerun exactly.

This is a theorem for that pooled physical bank, not a claim that every side
complex has enough rank-four faces.

## 5. Literal rank-three and growing-rank replacement

Every five planar points contain a convex quadrilateral. Double counting
five-sets gives

\[
                         v_4(P)\ge {1\over5}\binom n4.    \tag{6}
\]

There are at most \(\binom n3\) literal rank-three histories, each demanding
\(n/8\). Reserving \(q=\lceil n/8\rceil\) slots per history needs at most ten
formal copies of the bank in (6), because

\[
 {5\binom n3q\over\binom n4}={20q\over n-3}\le10.       \tag{7}
\]

Thus all literal rank-three histories admit one pooled code of load and
recovery list at most ten. Ranks one through three together need at most
eighty copies.

For literal rank \(r\), classical Erdős--Szekeres with
\(t_r\le4^r+1\) gives

\[
 v_{r+1}(P)\ge
 {\binom n{r+1}\over\binom{t_r}{r+1}}.                  \tag{8}
\]

The same block count yields load/list \(2^{O(r^2)}\). Pooling all
\(r\le R=o(\sqrt{\log n})\) therefore costs \(n^{o(1)}\). At
\(r\ge\log n\), retaining the history itself has amplified load at most one.
The direct method leaves exactly the intermediate literal range

\[
              \Omega(\sqrt{\log n})\le r<\log n.         \tag{9}
\]

## 6. Coherent-root \(E(k,k)\) regression

For \(q\le m=|E(k,k)|\) coherent roots, the reports pool every pair
\((\text{root},S)\) before allocation. The top mixed bank has size \(W_k^2\).
The exact cup recurrence proves its capacity for \(7\le k\le19\); for
\(k\ge20\), the path estimates

\[
 U_{k,k}(1)\le4^k mW_k,\qquad
 W_k\ge2^{(k-3)(k-2)/2},\qquad m\le2^{2k-4}             \tag{10}
\]

give \(W_k^2\) at least the total ceiling demand. Hence one joint block code
has load and fibre one, including the terminal maximal-cup histories. The
finite failures at \(k=5,6\) are explicitly retained.

## 7. Numerical reruns

All four relevant programs passed. The principal outputs were:

~~~text
abstract mixed Hall assembly: PASS; weighted Hall graphs checked=8232;
exact trace overlap r=30 -> 27; coherent-root overlap=12

joint detached-bank rank promotion: PASS;
rank4 m=70 load/list=14; rank5 m=70 load/fibre=1;
E(k,k) joint margin positive from k=7

PASS: global rank-three ES4 replacement code;
worst3=10; worst<=3=45; generalized rows through r=18

label-replacing ES mixed code: PASS;
E(5,5): histories=1281, mixed=10201, used=2331, max_load=7/8;
symbolic rows through k=40
~~~

## 8. Dependency and scope audit

The unconditional inputs are max-flow/min-cut, elementary slot allocation,
rank incidence, the five-point \(ES(4)\) theorem, and the classical
Erdős--Szekeres upper bound. The matching-star and \(E(k,k)\) statements
also use their explicitly verified ordinary-face recurrences. No step invokes
the desired unrestricted Erdős 838 lower bound.

The package does **not** prove local Hall expansion for arbitrary temporal
cells, does not make root-indexed bank reuse disappear, and does not solve
the intermediate range (9). Its valid use in the fixed-size attack is:
low literal ranks can be pooled globally; any remaining proof must address
intermediate ranks, nonliteral multiplicity, or a bank-incidence constraint
outside the trace-owned setting.
