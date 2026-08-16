# A third cyclic merged downface: corrected history-faithful shadow theorem

## Correction and verdict

The earlier version of this report incorrectly promoted a large-load result
for the **prefix-only** output alphabet to a barrier for all one-face
routings. That promotion was false. The rational cyclic blocker constructed
below already has a cubic, constant-load, one-face bank: retain each complete
selected source word except for one role on each of the three sides.

For three binary (q)-role word families this codimension-three source
shadow has

\[
 \begin{aligned}
 M&=2^{3q},\\
 I_{\rm sh}&=Mq^3,\\
 |\mathcal G_{\rm sh}|&={Mq^3\over8},\\
 \max_G d(G)&=8.                                      \tag{1}
 \end{aligned}
\]

Thus the full-compatible-cube geometry supplies exactly the missing
(q^3/8) one-face multiplier. For (q=3), exact rational enumeration gives
(13{,}824) incidences, (1{,}728) ordinary outputs, and uniform load eight.

Two scope statements remain exact.

1. A third **linear** strong-composition block cannot be a third independent
   non-singleton profile: every intermediate occupied block has rank at most
   one.
2. The old prefix-only calculation is correct for that restricted alphabet,
   but it is not an intrinsic history obstruction. The unresolved live branch
   is precisely where the compatible rooted downsets do not contain
   almost-full selected source words.

This report therefore proves a positive conditional cubic theorem and
isolates a source-thin/high-codegree fork. It is not an unconditional
half-coefficient closure.

## 1. The linear two-profile ceiling

Consider a vertical lexicographic composition with occupied blocks

\[
                 Q_{i_0},Q_{i_1},\ldots,Q_{i_s},
                 \qquad i_0<\cdots<i_s.                 \tag{2}
\]

The strong-composition face theorem says that the first trace is a cap, the
last trace is a cup, and every intermediate occupied block contains exactly
one selected point. Consequently a proposed third prefix cloud is either
intermediate and has rank at most one, belongs to an existing endpoint
profile, or becomes a new endpoint and demotes an old endpoint.

> **Theorem 1 (linear two-profile ceiling).** A one-face merged downface in
> a linear strong composition has at most two independent non-singleton
> rooted profile factors.

At binary maximum-child depth (j), an intermediate rank-one alphabet has
at most (j+1) downfaces while the surviving mass fraction is (2^{-j}).
Hence its entire aggregate contribution is only

\[
                         \sum_{j\ge0}(j+1)2^{-j}=4.      \tag{3}
\]

The verifier exhausts the middle-block assertion in a rational nine-point,
three-block lexicographic composition: all 196 subsets meeting the first and
last blocks and using at least two middle-block labels are nonordinary.

## 2. A genuine cyclic common-ear operation

The two-sided blocker construction in
`TWO_SIDED_MERGED_DOWNFACE_MAXIMUM_CHILD_GATE.md` has merged faces

\[
                         G_{12}(S,T)=Y\cup S\cup T       \tag{4}
\]

sharing one exposed seam edge. Insert a sufficiently small strict rational
convex chain (E) in the open outer-ear chamber beyond this edge and inside
all other supporting halfplanes. Openness and finiteness give

\[
                  G_{12}(S,T)\cup U\in\mathcal F(P\cup E)
                         \qquad(U\subseteq E).           \tag{5}
\]

Partition (E) into a third role product. In the full-cube model, every
subset of every selected left, right, and third-ear word merges with the
seam. This is a genuine third physical multiplication, not a third-target
Hall restatement.

## 3. History-faithful codimension-three source shadow

Let the physical ground be split into three disjoint, role-coloured systems

\[
 \mathcal X^a=(X^a_1,\ldots,X^a_{q_a}),\qquad a=1,2,3.   \tag{6}
\]

A record (r) carries a transversal word
(w^a_r=\{x^a_{r,i}:1\le i\le q_a\}) in each system and a visible seam
(Y_r). Choose role sets (I_a\subseteq[q_a]). Assume that for every record
and every ((i,j,k)\in I_1\times I_2\times I_3),

\[
 O(r;i,j,k)=Y_r
 \cup\bigl(w^1_r\setminus\{x^1_{r,i}\}\bigr)
 \cup\bigl(w^2_r\setminus\{x^2_{r,j}\}\bigr)
 \cup\bigl(w^3_r\setminus\{x^3_{r,k}\}\bigr)           \tag{7}
\]

is an ordinary face. Let (W) be the weighted record mass and let
(\Delta_3) be the actual weighted load of these outputs, including physical
completions and external-history collisions.

> **Theorem 2 (codimension-three source shadow).** Under (7),
> \[
>             W|I_1||I_2||I_3|\le \Delta_3 V(P).        \tag{8}
> \]

The proof is exact incidence counting. The output occupancy mask reveals the
three omitted roles. Every retained physical label is still visible, so the
only local ambiguity is in the three omitted labels. If the retained words
and seam have residual history load at most (\Lambda), then

\[
 \Delta_3\le\Lambda
 \max_{(i,j,k)\in I_1\times I_2\times I_3}
        |X^1_i||X^2_j||X^3_k|.                         \tag{9}
\]

In particular, binary roles and literal histories give

\[
                       V(P)\ge {Wq_1q_2q_3\over8}.      \tag{10}
\]

For one unweighted complete role product with a fixed seam and no duplicate
external histories, let (W) denote its number of words. Outputs belonging
to different omitted-role triples have different occupancy masks. Therefore
the exact number of distinct outputs is

\[
 W\left(\sum_{i\in I_1}{1\over|X^1_i|}\right)
  \left(\sum_{j\in I_2}{1\over|X^2_j|}\right)
  \left(\sum_{k\in I_3}{1\over|X^3_k|}\right).          \tag{11}
\]

This also identifies the useful arbitrary-alphabet strategy: omit roles
with small physical completion alphabet, rather than necessarily the first
or last roles.

## 4. Exact rational realization

Start with the rational full-prefix-compatible blocker gadget

\[
 \begin{aligned}
 y&=(-1,2),&a&=(0,0),&c&=(1,-1),&p(x)&=(x,-x^2),\\
 z&=(-1,-2),&b&=(0,0),&d&=(1,1),&q(x)&=(x,x^2),
                                                               \tag{12}
 \end{aligned}
\]

with all variable labels at (x>2), followed by rational strong glue. The
merged faces share the exposed edge between the physical images of (y,z).
For edge endpoints (p_0,p_1), use third-ear points

\[
 p(t)=p_0+t(p_1-p_0)
       +\varepsilon t(1-t)R_{\rm out}(p_1-p_0),
       \qquad0<t<1,                                      \tag{13}
\]

where (\varepsilon>0) is sufficiently small and rational. These points
form a strict outer chain replacing the seam edge. Every third source word
and every third-word subset is compatible with every two-sided merged face.

For three binary roles per side, exact enumeration gives

\[
 \begin{array}{c|r}
 \text{complete source triples}&512\\
 \text{codimension-three incidences}&13{,}824\\
 \text{distinct ordinary outputs}&1{,}728\\
 \text{minimum/maximum output load}&8/8.
 \end{array}                                             \tag{14}
\]

The output itself retains six of the nine selected source labels. The only
ambiguity is the omitted binary label in each of the three revealed roles,
so load eight is both an upper bound and sharp.

## 5. What the prefix-only calculation actually proves

If one artificially restricts outputs to marked subsets of the three fixed
all-zero prefixes, then

\[
 \begin{aligned}
 E_{\rm pre}&=2^{3q-3}(q-1)^3,\\
 |\mathcal G_{\rm pre}|&=(2^{q-1}-1)^3,\\
 {E_{\rm pre}\over|\mathcal G_{\rm pre}|}&\ge(q-1)^3.   \tag{15}
 \end{aligned}
\]

One such prefix face has load (2^{3q-3}=M/8). These formulas are correct,
but they apply only to enumerating the restricted prefix-output incidences.
They do not rule out the almost-full outputs (7), which retain the variable
source tails and have constant load.

## 6. Fixed-gap half-scale ledger

Retain the two (K=3) double-bad sides from the preceding gate:

\[
 a=L,\qquad b=\lfloor L/4\rfloor,\qquad
 D=\lfloor2^L/L^6\rfloor.                              \tag{16}
\]

Add a third independent physical history word with (L) binary roles. The
complete-source record mass satisfies

\[
 \log_2M={1\over2}L^2-3L\log_2L+3L+O(1),               \tag{17}
\]

while the support is (O(2^L/L^5)) and source rank is (O(L)). Retain every
selected large-role label and omit one binary role on each side. Theorem 2
then gives the exact bank

\[
                            V(P)\ge {ML^3\over8}.        \tag{18}
\]

Thus the displayed full-compatible-word construction is a positive equality
model for the missing (K=3) multiplier, not a barrier.

## 7. Exact remaining scope

The maximum-child theorem available in the general live branch guarantees
compatible fixed prefixes, not (7). The corrected trichotomy is therefore:

1. **Almost-full branch.** Condition (7) holds for three
   (\Theta(L))-sized role reservoirs and
   (\Delta_3=L^{o(1)}); (8) supplies the cubic one-face bank.
2. **Source-thin branch.** In at least one component, almost every selected
   word loses compatibility after any single low-completion omission. A
   first missing physical label is then a continuation-bearing
   blocker/profile record, but its global decoder still requires proof.
3. **High-codegree branch.** Many physical completions or external histories
   share the same almost-full output. This is a literal dense
   face--face/history core and must be handled by the existing Hall/Renyi
   machinery rather than by the prefix load calculation.

The unresolved promotion is from prefix compatibility to an almost-full
source shadow, or an exact payment of the source-thin/high-codegree
alternatives.

## 8. Verification

Run

```bash
python3 agent_outer_internal_product/verify_third_cyclic_merged_downface_history_load_gate.py
```

The verifier:

1. exhausts the linear middle-block rank-one obstruction;
2. builds the rational double-bad strong glue and common outer ear;
3. checks all source faces and subset mergers;
4. exhausts the codimension-three shadow, obtaining
   (13{,}824) incidences, (1{,}728) outputs, and load (8);
5. retains the prefix-only load calculation as a restricted-alphabet audit;
6. checks (11) for unequal role alphabets; and
7. verifies the fixed-gap (ML^3/8) ledger for (32\le L\le128).

It prints `PASS`.
