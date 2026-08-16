# Coherent middle overlap: the strong-tree closure and its sharp half barrier

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

There is an exact minimizer-specific exit, but exponential middle-shadow
overlap does **not** by itself give a coefficient strictly larger than one
half.

If the high-overlap deletion hierarchy can be promoted to an actual ordered
strong-decomposition tree on an induced set of \(m\) physical labels, then

\[
 \log V(P)\ge {1\over2}(\log m)^2-O((\log m)^{3/2}).              \tag{1}
\]

Consequently a least fixed-gap counterexample with target

\[
                 \log V(P)<\left({1\over2}-\delta\right)(\log n)^2
                                                                        \tag{2}
\]

cannot contain such a tree on

\[
       m\ge n^{\sqrt{1-2\delta}+\varepsilon}                         \tag{3}
\]

for any fixed \(\varepsilon>0\) and all sufficiently large \(n\). In
particular, promotion on \(n^{1-o(1)}\) labels closes every fixed gap.

This is essentially sharp. For every fixed \(\eta>0\) there is a rational
stretchable planar homogeneous strong-glue hierarchy \(Q_d\) such that

\[
 {\log V(Q_d)\over(\log |Q_d|)^2}\le {1\over2}+\eta+o_d(1),           \tag{4}
\]

while one rank-\(q_d=\Theta(\log |Q_d|)\) layer comprises a constant
fraction of all faces and both its carrier middle shadows and its terminal
Boolean leaf banks have

\[
                         \Lambda_{\rm mid}
                       \ge 2^{q_d-o(q_d)}.                            \tag{5}
\]

Thus even exponentially coherent overlap occurs arbitrarily close to the
coefficient-half equality regime. No argument depending only on carrier
convexity, rank, middle-shadow codegree, and the existence of a recursive
strong-glue hierarchy can furnish a uniform super-half margin. The live
missing theorem is the **promotion** of the overlap forest to a large actual
strong tree (or an equality-case rigidity theorem using the retained
root/endpoint history), not a stronger local overlap count.

## 1. Conditional minimizer closure

The weighted one-turn alignment theorem in
agent_asymptotic/NEXT_ENDPOINT_ATTACK.md says that every ordered full
binary strong-decomposition tree \(T\) on \(m\) leaves has

\[
                 \log V(T)\ge {1\over2}(\log m)^2
                                  -O((\log m)^{3/2}).                 \tag{6}
\]

Suppose an overlap/deletion hierarchy produces an induced subset
\(S\subseteq P\) whose physical order type is represented by such a tree.
Every ordinary face of \(S\) is an ordinary face of \(P\), so (6) gives
(1) with no decoder or output-load loss.

Write \(L=\log n\) and suppose (3). Then

\[
 {1\over2}(\log m)^2
 \ge {1\over2}(\sqrt{1-2\delta}+\varepsilon)^2L^2
 =\left({1\over2}-\delta+c_{\delta,\varepsilon}\right)L^2,          \tag{7}
\]

where

\[
 c_{\delta,\varepsilon}
   =\varepsilon\sqrt{1-2\delta}+{\varepsilon^2\over2}>0.            \tag{8}
\]

The error in (6) is \(o(L^2)\), so (7) contradicts (2). Notice the exact
scale: a merely logarithmic-rank carrier is not enough. The hierarchy must
retain a polynomially large set of **physical labels** with exponent above
\(\sqrt{1-2\delta}\).

This implication is fully global once the induced strong tree is present.
It does not spend \(V(P)\) once per carrier, root, or leaf.

## 2. Fixed-template hierarchies and the half coefficient

Let \(S\) be a fixed rational planar template with

\[
 |S|=r,\qquad a=\text{maximum cap rank},\qquad
 b=\text{maximum cup rank}.                                      \tag{9}
\]

Starting with one point, form the vertical lexicographic iterates

\[
                         Q_d=S[Q_{d-1}],\qquad |Q_d|=r^d.           \tag{10}
\]

The exact substitution formulas from proof_blowup_half.md give

\[
 \lim_{d\to\infty}{\log V(Q_d)\over(\log |Q_d|)^2}
                   ={a+b-2\over2\log r}=:\rho(S).                   \tag{11}
\]

The cap--cup theorem gives

\[
                    r\le {a+b-2\choose a-1}\le2^{a+b-2},          \tag{12}
\]

and hence \(\rho(S)\ge1/2\). This is the stationary version of the
strong-tree closure. It also shows why a genuine strong-glue promotion is
enough for the least-fixed-gap argument.

For a sharp family, take the balanced Erdős--Szekeres cell

\[
 S_k=T(2k-4,k-2),\qquad
 r_k={2k-4\choose k-2},\qquad a_k=b_k=k-1.                         \tag{13}
\]

It is rational and stretchable. Equations (11)--(13) give

\[
                    \rho_k={k-2\over\log {2k-4\choose k-2}}
                            \downarrow {1\over2}.                  \tag{14}
\]

Thus for each \(\eta>0\), fixing a sufficiently large \(k\) and then
letting \(d\to\infty\) proves (4).

Write \(Q_{k,d}\) for the \(d\)-fold iterate of \(S_k\). There is also one
diagonal scalable sequence at the exact boundary. Choose
\(k_j\to\infty\), and for each \(k_j\) choose \(d_j\) sufficiently large
that the \(o_{d_j}(1)\) error in (11) is at most \(1/j\). Then

\[
 P_j=Q_{k_j,d_j},\qquad
 { \log V(P_j)\over(\log |P_j|)^2}\longrightarrow {1\over2}.       \tag{14a}
\]

All \(P_j\) are rational stretchable configurations. Thus “strictly above
one half” is false even as a qualitative asymptotic conclusion from the
existence of a recursively strong-decomposable overlap hierarchy.

## 3. The top rank layer has constant density

The same family also calibrates the exact middle-overlap residual. The
point is stronger than a pigeonhole over \(O(d)\) ranks: for every fixed
balanced template in (13), the top rank layer is a constant fraction of
all faces.

Write the three template polynomials

\[
 \begin{aligned}
 G_C(x)&=\sum_{j\ge1}c_j(S)x^{j-1},\\
 G_U(x)&=\sum_{j\ge1}u_j(S)x^{j-1},\\
 G_V(x)&=\sum_{j\ge2}v_j(S)x^{j-2}.
 \end{aligned}                                                     \tag{15}
\]

Let \(h\) be the maximum ordinary-face rank in \(S\). For the balanced
cell (13), upper/lower hull decomposition and the top strong-glue split
give

\[
                              h=a+b-2=2k-4.                        \tag{16}
\]

The graded form of the exact substitution formulas is

\[
 \begin{aligned}
 C_d(z)&=C_{d-1}(z)G_C(r^{d-1}z),\\
 U_d(z)&=U_{d-1}(z)G_U(r^{d-1}z),\\
 V_d(z)&=rV_{d-1}(z)
       +C_{d-1}(z)U_{d-1}(z)G_V(r^{d-1}z).
                                                                    \tag{17}
 \end{aligned}
\]

Therefore

\[
 \deg C_d=1+d(a-1),\quad
 \deg U_d=1+d(b-1),\quad
 \deg V_d=dh.                                                       \tag{18}
\]

Let \(A_d,B_d,T_d\) be the leading coefficients of these three
polynomials. Since every polynomial in (15) is fixed and has a positive
leading coefficient,

\[
 {C_d(1)\over A_d}
  =\prod_{t<d}{G_C(r^t)\over c_a r^{t(a-1)}}=O_S(1),
 \qquad
 {U_d(1)\over B_d}=O_S(1).                                      \tag{19}
\]

Indeed each factor after the first is \(1+O_S(r^{-t})\). The cross term
of degree \(dh\) in (17) has coefficient

\[
              T_d=A_{d-1}B_{d-1}v_h r^{(d-1)(h-2)}.               \tag{20}
\]

Equations (19)--(20) show that the current cross term is \(O_S(T_d)\).
The inherited term \(rV_{d-1}(1)\) is smaller than \(T_d\) by a geometric
factor \(O_S(r^{3-(d-1)h})\). Induction gives a finite constant \(K_S\)
such that

\[
                         V(Q_d)\le K_S T_d                         \tag{21}
\]

for every \(d\). Thus the family of top faces

\[
             \mathcal Q_d=\{Q\subseteq Q_d:|Q|=q_d=dh,
                                       \ Q\text{ ordinary}\}       \tag{22}
\]

has size \(T_d\ge V(Q_d)/K_S\). In particular

\[
             q_d={2k-4\over\log r_k}\log |Q_d|=\Theta(\log|Q_d|).
                                                                        \tag{23}
\]

## 4. Exponential common-middle overlap at the half barrier

Use every \(Q\in\mathcal Q_d\) as a carrier and use the literal source
\(A=Q\) with weight one. Sources are distinct, so the rank-safe
per-source normalization is exact. Let

\[
 B_q=\sum_{q/3\le t\le2q/3}{q\choose t}.                          \tag{24}
\]

Every carrier contributes \(B_q\) carrier--middle-face incidences. Every
middle face is an ordinary face of \(Q_d\). Hence, if

\[
       \Lambda_{\rm mid}
          =\max_F|\{Q\in\mathcal Q_d:F\subseteq Q\}|,             \tag{25}
\]

double counting and (21) give

\[
 \Lambda_{\rm mid}V(Q_d)
       \ge T_dB_{q_d}
       \ge {V(Q_d)\over K_S}B_{q_d},
 \qquad
 \boxed{\Lambda_{\rm mid}\ge {B_{q_d}\over K_S}
                    =2^{q_d-o(q_d)}.}                             \tag{26}
\]

The private-petal/four-cover forest has the same exponential obstruction.
Every \(Q\in\mathcal Q_d\) has maximum possible ordinary rank \(q_d\).
The union of two distinct carriers therefore has rank greater than \(q_d\)
and is not ordinary. But the union support of every terminal four-covered
leaf is ordinary. Hence every terminal leaf contains exactly one carrier,
and its Boolean bank is \(2^Q\). The middle face attaining (25) belongs to
all the corresponding terminal banks, so

\[
                    \boxed{\Lambda_{\rm leaf}
                       \ge\Lambda_{\rm mid}
                       \ge B_{q_d}/K_S
                       =2^{q_d-o(q_d)}.}                         \tag{26a}
\]

Thus the overlap is genuinely exponential at both gates and occurs in a
planar, rank-safe, recursively strong-decomposable family whose coefficient
can be arbitrarily close to \(1/2\).

For the diagonal sequence (14a), choose \(d_j\) still larger if necessary
so that \(\log K_{S_{k_j}}=o(q_{d_j})\). Then (23) gives
\(q_{d_j}=(1+o(1))\log |P_j|\), while (26)--(26a) give

\[
       \Lambda_{\rm mid},\Lambda_{\rm leaf}
                  =2^{q_{d_j}-o(q_{d_j})}.                        \tag{26b}
\]

Hence equality coefficient \(1/2\), logarithmic maximum rank, and
exponential coherent overlap coexist along one scalable planar sequence.

## 5. Exact remaining interface

The following implication is valid and sufficient:

\[
 \begin{array}{c}
 \text{high-overlap deletion forest}\\
 \text{on a support of size }m
 \end{array}
 \quad+\quad
 \begin{array}{c}
 \text{actual ordered strong-tree promotion}\\
 \text{on those same physical labels}
 \end{array}
 \Longrightarrow\quad (1).                                      \tag{27}
\]

What is false is the expectation that the **amount** of overlap supplies a
strict gain beyond (1). The near-extremal family (13)--(26) has as much
middle overlap as the counting argument can demand.

Accordingly a complete minimizer argument must prove one of two genuinely
new statements:

1. the canonical high-overlap forest retains a support satisfying (3) and
   promotes to an ordered strong tree in one common physical chart; or
2. equality-scale strong hierarchies are incompatible with the retained
   root/endpoint history of the marked minimizer records.

Carrier overlap alone, even with stretchability and logarithmic rank, does
not distinguish these alternatives.

## 6. Verification

The script
verify_minimizer_coherent_overlap_strong_tree_gate.py checks the exact
graded substitution recurrence for the six-point balanced seed through
depth \(14\), including \(\deg V_d=4d\), the constant top-layer ratio, and
the middle-incidence lower bound. It also checks the exact coefficients
\(\rho_k\) in (14), their monotone approach to \(1/2\) on a long dyadic
subsequence, and the fixed-gap support threshold (7)--(8).
