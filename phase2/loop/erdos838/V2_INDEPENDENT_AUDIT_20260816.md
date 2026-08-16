# Independent audit V2: recursive separated-template half closure

**Date:** 2026-08-16.

## Verdict: PASS

Every construction in the stated recursive separated-template class expands
to one ordered binary strong-decomposition tree. The audited strong-tree
theorem therefore gives

\[
        \log_2V(P)\ge {1\over2}(\log_2|P|)^2
                       -O((\log|P|)^{3/2}).              \tag{1}
\]

The exact profile/rank recurrences, stationary coefficients, perfect-reset
ranks, and nonstationary finite ledgers are also correct. The verifier passes
all advertised exact tests.

This closes a construction class; it is not an unrestricted lower bound.
Any sub-half construction outside the known theorem must use genuinely
non-strong-decomposable children, rather than deeper or nonstationary
recursion among the separated modules audited here.

Audited sources:

- `agent_many_class_partner_reset/RECURSIVE_ES_RAMP_HALF_CLOSURE.md`;
- `agent_many_class_partner_reset/verify_recursive_es_ramp_half_barrier.py`;
- `agent_killsearch/STRONG_TREE_HALF_REFEREE.md` (previous independent
  audit of the load-bearing all-tree theorem).

## 1. Exact binary recurrences

For a rational high-left/low-right separated composition \(T=A\searrow B\),
let \(n,C,U,V\) denote size, nonempty cap count, nonempty cup count, and
ordinary-face count. The mixed orientation rule says that a spanning cap is
a cap of \(A\) followed by at most one label of \(B\), and a spanning cup
is the reflected object. A spanning ordinary face has a cap trace in \(A\)
and a cup trace in \(B\). Therefore

\[
\begin{aligned}
n(T)&=n(A)+n(B),\\
C(T)&=C(A)(1+n(B))+C(B),\\
U(T)&=U(A)+U(B)(1+n(A)),\\
V(T)&=V(A)+V(B)+C(A)U(B).                               \tag{2}
\end{aligned}
\]

All four are equalities: the block grounds are disjoint, so the trace
decompositions are recoverable and no load is hidden.

If \(a,b,v\) denote maximum cap, cup, and ordinary-face ranks, the same
classification gives

\[
\begin{aligned}
a(T)&=\max\{a(A)+1,a(B)\},\\
b(T)&=\max\{b(A),b(B)+1\},\\
v(T)&=\max\{v(A),v(B),a(A)+b(B)\}.                      \tag{3}
\end{aligned}
\]

For the recursively defined cup--cap module

\[
                     E(r,s)=E(r,s-1)\searrow E(r-1,s),  \tag{4}
\]

with the singleton boundary, induction in (3) yields

\[
 |E(r,s)|=\binom{r+s-4}{r-2},quad
 a=s-1,quad b=r-1,quad v=r+s-4.                       \tag{5}
\]

In particular, the \(h\)-fold \(E(7,7)\) reset has

\[
               |B^h|=252^h,qquad a=b=5h+1,qquad v=10h. \tag{6}
\]

The ranks are additive in \(h\); the earlier loose \(10^h\) rank estimate
is not used.

## 2. Macro substitution and stationary coefficient

Let a fixed \(m\)-label macro skeleton \(S\) receive the same \(N\)-point
child \(Q\) at every label. Classifying a spanning face by its first and
last occupied macro labels gives

\[
\begin{aligned}
C(S[Q])&=C(Q)A_S(N),\\
U(S[Q])&=U(Q)B_S(N),\\
V(S[Q])&=mV(Q)+C(Q)U(Q)F_S(N),                          \tag{7}
\end{aligned}
\]

where the nonnegative integer polynomials satisfy

\[
 \deg A_S=a(S)-1,qquad
 \deg B_S=b(S)-1,qquad
 \deg F_S=v(S)-2.                                      \tag{8}
\]

For example, every occupied macro label strictly between the first and last
contributes one arbitrary child singleton, giving the degree in \(F_S\).
An extremal macro face makes the leading coefficient positive.

Iterate \(S\) from a singleton. With \(\ell=\log_2m\) and
\(L_d=d\ell\), summing the endpoint degrees in (7) gives

\[
\begin{aligned}
\log C_d&={a-1\over2}\ell d^2+O_S(d),\\
\log U_d&={b-1\over2}\ell d^2+O_S(d),\\
\log V_d&={a+b-2\over2}\ell d^2+O_S(d).                \tag{9}
\end{aligned}
\]

The degree \(v-2\) contribution is only linear in the previous log-size at
one level and does not change this stationary quadratic fixed point.
Therefore

\[
 \lim_{d\to\infty}{\log V_d\over L_d^2}
        ={a+b-2\over2\log m}.                           \tag{10}
\]

The classical cup--cap bound

\[
                      m\le\binom{a+b-2}{a-1}
                        \le2^{a+b-2}                    \tag{11}
\]

makes (10) at least \(1/2\). For \(E(k,k)\), it is

\[
 {k-2\over\log\binom{2k-4}{k-2}}>1/2,
\]

and tends to \(1/2\). For every reset power it is

\[
                         {5\over\log252}=0.626780\ldots. \tag{12}
\]

Thus the lower coefficient is sharp for the class, while reset depth does
not evade it.

## 3. Grafting lemma

Expand every occurrence of \(E(r,s)\) using (4). Its realization is an
ordered full binary strong tree with rule \(\searrow\) at each internal
node. A reflected module remains such a tree: reverse the local horizontal
order and exchange its two children at every node. Replacing a macro label
by another expanded module grafts the second root at the corresponding leaf
of the first tree. Grafting ordered full binary trees again produces one
ordered full binary tree, and the sufficiently small rational insertion
preserves every ancestor's separated mixed signs.

Induction on the construction syntax therefore proves:

> Every finite configuration generated from singletons by separated binary
> composition, arbitrary \(E(r,s)\) modules, their reflections,
> \(E(7,7)\) reset powers, and arbitrary recursive substitutions among these
> modules is represented by one ordered strong-decomposition tree.

The reset matching/circuit annotations do not alter the ordinary-face
orientation signs and hence cannot delete any face counted by that tree.
Different modules may be used in every leaf; stationarity is not required.

## 4. Application of the audited all-tree theorem

The strong-tree theorem is uniform over every ordered full binary tree. Its
exact endpoint max-plus recurrences are

\[
\begin{aligned}
X_R&=\max\{(|B|+1)X_A,X_B\},\\
Y_R&=\max\{Y_A,(|A|+1)Y_B\},\\
M_R&=\max\{M_A,M_B,X_AY_B\}.                            \tag{13}
\end{aligned}
\]

The previous independent referee audit checks the heavy-path dichotomy:
many tiny same-side siblings inject a Boolean cap/cup comb, while many
macroscopic siblings force a persistent endpoint coordinate through
\(\Omega(\sqrt{\log n})\) reset opportunities. In either case

\[
               \log M_R\ge {1\over2}(\log n)^2
                              -O((\log n)^{3/2}).        \tag{14}
\]

The exact face/endpoint comparison

\[
                       M_R\le V(R)\le2n^2\max\{1,M_R\}  \tag{15}
\]

turns (14) into (1). The theorem does not require equal macro arity, a finite
profile menu, balance, or a stationary reflection schedule. Hence it applies
after the grafting lemma with no additional asymptotic assumption.

## 5. Nonstationary scalar ledger

For depth-dependent macros \(S_j\), put
\(\ell_j=\log|S_j|\), \(L_j=\sum_{q\le j}\ell_q\). The exact polynomial
corrections in (7) produce a finite ledger; summing its cap and cup lines and
using (11) at every depth gives

\[
 c_d+u_d\ge{1\over2}\left(L_d^2-sum_{j\le d}\ell_j^2\right). \tag{16}
\]

When the mesh is small, (16) already has coefficient \(1/2\). For
macroscopic or heterogeneous jumps, (16) alone does not align the endpoint
product appearing in \(V\); the all-tree theorem supplies exactly that
missing orientation-sensitive step. Thus the scalar ramp is a valid
relaxation but not a realizable sub-half construction in this class.

## 6. Exact replay

Command:

~~~text
python3 phase2/loop/erdos838/agent_many_class_partner_reset/verify_recursive_es_ramp_half_barrier.py
~~~

Fresh result: `PASS`. The suite checks:

- all \(E(r,s)\) ranks for \(3\le r,s\le12\);
- reset ranks through depth eight;
- stationary powers of \(E(k,k)\) for \(k=4,7,12,20\);
- four hostile nonstationary schedules;
- the exact nondominated \((C,U,V)\) census of every oriented binary strong
  tree through twelve leaves.

Selected output:

~~~text
E(7,7): size=252, fixed_point=0.626780061368,
depth12_V=0.625614078542
E(20,20): size=9075135300, fixed_point=0.544147404351,
depth12_V=0.552476199921
exact Pareto minimum V through n=12:
3,7,14,26,45,75,120,184,271,389,542
~~~

The finite census is regression evidence for (2)--(9); the asymptotic
closure rests on the analytic strong-tree theorem plus the grafting lemma.

## 7. Scope

The audit rules out sub-half constructions generated recursively from the
listed separated modules. It does not assert that every planar order type is
strong-decomposable or contains a near-spanning strong-decomposable subset.
That promotion/extraction statement is false without additional hypotheses
and remains outside V2.
