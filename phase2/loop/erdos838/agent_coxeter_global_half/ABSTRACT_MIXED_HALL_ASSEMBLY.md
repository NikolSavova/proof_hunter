# Weighted Hall assembly for mixed trace banks

**Date:** 2026-08-15

## Verdict

There is an exact abstract globalization theorem for label-replacing mixed
codes.  It separates the remaining problem into a local weighted Hall
condition and a completely solved global overlap audit.

For each rooted endpoint/trace cell \(a\), let \(\mathcal H_a\) be its
weighted temporal histories and let \(\mathcal B_a\) be a mixed ordinary
face reservoir.  If every cell has a local decoder of output load at most
\(\lambda\) and recovery fibre at most \(\rho\), then superposing the
decoders gives, at an output face \(F\),

\[
 \boxed{
 \operatorname{load}(F)\le\lambda\delta(F),
 \qquad
 \operatorname{fibre}(F)\le\rho\delta(F),}             \tag{1}
\]

where \(\delta(F)\) is the number of local reservoirs containing \(F\).

For the genuine two-sided trace reservoirs of rooted diagonal
amalgamation, an ordinary rank-\(r\) face belongs to at most

\[
 \boxed{\delta(F)\le r-3.}                              \tag{2}
\]

The bound improves the previously recorded \(r-1\) and is sharp: an exact
rational alternating convex \(r\)-gon belongs to all \(r-3\) possible
interior consecutive-trace banks.

Consequently, on ranks at most \(R\), any local
\(n^{o(1)}\)-load, \(n^{o(1)}\)-fibre decoder globalizes with load and list
fibre at most

\[
 \lambda(R-3),\qquad \rho(R-3).                        \tag{3}
\]

In particular, this is \(n^{o(1)}\) at the live ranks
\(R=n^{o(1)}\), including \(R=O(\log n)\).

The exact local existence criterion is weighted Hall:

\[
 D\sum_{H\in X}w(H)
 \le\lambda\left|\bigcup_{H\in X}\Gamma_a(H)\right|
 \quad\text{for every }X\subseteq\mathcal H_a.         \tag{4}
\]

Here \(D\) is the desired amplification (in the half-weight application,
\(D=n\)) and \(\Gamma_a(H)\) is the set of compatible mixed outputs for
history \(H\).  Thus global mixed-face reuse is no longer an open-ended
loss: once (4) and local recovery are proved, the only global factor is the
sharp output rank.

There is also a necessary scope warning.  Root-indexed codes which all use
the same **unmarked complementary bank** need not obey (2).  A stretchable
configuration can have \(q\) coherent roots over one complement, so the
same mixed face belongs to all \(q\) root banks.  Independent local codes
can then incur load and recovery fibre \(q\).  Trace ownership, a global
partition of the shared bank, or a second Hall problem across roots is
essential.

This report gives the requested abstract theorem and the sharp overlap
audit.  It does not prove (4) for every reflection-order cell; that local
profile-contraction inequality is now the sole substantive hypothesis.

## 1. The exact local weighted Hall theorem

Fix a cell \(a\).  Give history \(H\in\mathcal H_a\) demand

\[
 d(H)=Dw(H).                                             \tag{5}
\]

A fractional local decoder is a nonnegative matrix
\(x_a(H,F)\), supported on \(F\in\Gamma_a(H)\), such that

\[
 \sum_Fx_a(H,F)=d(H),
 \qquad
 \sum_Hx_a(H,F)\le\lambda.                             \tag{6}
\]

> **Theorem 1 (weighted Hall).** A matrix satisfying (6) exists if and only
> if (4) holds for every history subfamily \(X\).

**Proof.**  Build the standard flow network: the source-to-history arc for
\(H\) has capacity \(d(H)\); every compatible history-to-output arc has
infinite capacity; and every output-to-sink arc has capacity \(\lambda\).
A finite cut is specified by a history set \(X\) and must retain every
output in \(\Gamma_a(X)\) on the source side.  Its deficit is exactly the
failure of (4).  Max-flow/min-cut proves the equivalence.  \(\square\)

Hall feasibility alone does not control recovery fibre: many histories can
send tiny amounts to the same output.  One must supply a local recovery
relation as a separate datum.  Define

\[
 \operatorname{fib}_a(F)
 =|\{H:x_a(H,F)>0\}|.                                   \tag{7}
\]

The most useful label-replacing special case has fibre one.

> **Corollary 2 (complete-reservoir block code).** Suppose
> \(\Gamma_a(H)=\mathcal B_a\) for every history and
>
> \[
>  |\mathcal B_a|\ge\sum_{H\in\mathcal H_a}\lceil d(H)\rceil. \tag{8}
> \]
>
> Then there is a decoder with \(\lambda=\rho=1\), and the output face
> exactly recovers its input history relative to the known cell.

**Proof.**  Order histories and outputs canonically.  Reserve a disjoint
block of \(\lceil d(H)\rceil\) outputs for \(H\), and put equal flow
\(d(H)/\lceil d(H)\rceil\le1\) on its block.  The block containing an
output recovers \(H\).  \(\square\)

`LABEL_REPLACING_ES_MIXED_CODE.md` verifies (8) for the top mixed bank of
every \(E(k,k)\), \(k\ge5\).  The point of Theorem 1 is that a general
reflection-order cell can use a restricted compatibility graph; then the
full family of inequalities (4), not just total scalar capacity, is the
exact missing condition.

## 2. Global assembly

Let \(\mathcal A\) be any family of cells and superpose their local flows.
For an ordinary face \(F\), put

\[
 \mathcal A(F)=\{a:F\in\mathcal B_a\},
 \qquad \delta(F)=|\mathcal A(F)|.                      \tag{9}
\]

> **Theorem 3 (incidence assembly).** If every local decoder has load at
> most \(\lambda\) and fibre at most \(\rho\), their superposition satisfies
> (1).  In particular, all cell-history demand is paid by ordinary faces
> with global capacity \(\lambda\max_F\delta(F)\), and an unmarked output
> has a recovery list of at most \(\rho\max_F\delta(F)\) cell-history pairs.

**Proof.**  At \(F\), sum the local output loads over
\(a\in\mathcal A(F)\); each summand is at most \(\lambda\).  Similarly, the
recovery list is the union of at most \(\delta(F)\) local lists, each of
size at most \(\rho\).  \(\square\)

The list is explicit, not existential: enumerate the cells whose reservoir
contains \(F\), then apply their local block/Hall decoders.  If the trace
mark is retained externally, recovery stays at the local fibre \(\rho\);
without a mark, (1) is the exact list bound.

## 3. Exact overlap of mixed trace banks

Index a two-sided mixed trace cell by an ordered label pair \(j<l\) and the
side sign \(\sigma\).  Its output face has nonempty selected histories on
both sides of the trace.  As in rooted diagonal amalgamation, \(j,l\) must
be consecutive in the output's inherited label order and \(jl\) must be a
diagonal.  Conversely such a consecutive diagonal determines the two side
histories and the sign.

Let \(F=\{v_1<\cdots<v_r\}\).  Nonempty histories on both sides force an
eligible trace to be

\[
 v_i v_{i+1}\qquad(2\le i\le r-2).                     \tag{10}
\]

There are only \(r-3\) pairs in (10); the diagonal and compatibility tests
can only remove pairs.  The sign is then forced by which side contains the
earlier vertices.  This proves (2).  The argument depends only on the
inherited order and the unique side split, so it applies equally to a
stretchable point configuration and to the rank-three allowable-sequence
version of a type-A reflection order.

Rankwise, if \(V_r\) is the number of ordinary rank-\(r\) faces and
\(L_{a,r}\) is the total local flow sent to rank \(r\), Theorem 3 gives

\[
 \boxed{
 \sum_{a\in\mathcal A}L_{a,r}
 \le\lambda(r-3)V_r.}                                  \tag{11}
\]

This is the exact global face-bank inequality needed after a local Hall
decoder has been built.

## 4. Sharp stretchable trace-overlap regression

For \(r\ge4\), take the rational x-ordered points

\[
 z_i=
 \begin{cases}
 (i,K-i^2),&i\text{ even},\\
 (i,-K+i^2),&i\text{ odd},
 \end{cases}
 \qquad 0\le i<r,\qquad K=10r^2.                       \tag{12}
\]

The even points form a strict upper cap and the odd points a strict lower
cup.  The large vertical separation makes their union a convex \(r\)-gon.
For every interior consecutive pair \(z_i,z_{i+1}\),
\(1\le i\le r-3\), all earlier points lie strictly on one side of its line
and all later points on the other.  Hence the segment is a diagonal and the
whole polygon occurs in that mixed trace bank.  The two extreme consecutive
pairs are hull edges.  Therefore

\[
 \delta(\{z_0,\ldots,z_{r-1}\})=r-3.                  \tag{13}
\]

Assigning one unit local history to this same face in each eligible trace
cell gives local load/fibre one and global load/fibre \(r-3\).  Thus no
rank-independent assembly theorem is possible.

## 5. Sharp root-bank warning

The trace proof does not cover a bank indexed only by a coherent root.
Let \(W\) be any separated configuration with a nonempty mixed bank and add
\(q\) successively farther-left coherent positive roots
\(p_1,\ldots,p_q\).  Each root has

\[
 \chi(p_a,x,y)=+\qquad(x<y\text{ in }W).                \tag{14}
\]

If every root code declares the same complementary mixed reservoir
\(\mathcal B(W)\), then every \(F\in\mathcal B(W)\) has

\[
 \delta(F)=q.                                           \tag{15}
\]

Singleton local codes which all choose one fixed \(F\) attain global
load/fibre \(q\).  This does not rule out a **joint** Hall allocation: the
large \(E(k,k)\) bank, for example, may be partitioned among several roots.
It proves that independently constructing fibre-one root codes and then
invoking the trace rank bound is invalid.  Root codes must first be assigned
to trace-owned subbanks, or all roots sharing a complement must enter one
global Hall instance.

## 6. What remains

The global route can now be stated exactly.  On a rank window \(r\le R\):

1. assign each rooted history cell to genuine two-sided trace reservoirs;
2. prove its weighted Hall inequalities (4) with
   \(\lambda=n^{o(1)}\);
3. give a local recovery relation with \(\rho=n^{o(1)}\); and
4. apply (11), losing only \(R-3=n^{o(1)}\).

For root-indexed complementary codes, replace step 1 by a joint Hall
allocation across all roots using that bank.  Total capacity alone is
insufficient; all subfamily cuts in (4) are necessary.

Accordingly the unsolved mathematical content is local profile contraction
or joint-root Hall expansion.  Global mixed-face overlap itself is exactly
controlled.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_coxeter_global_half/verify_abstract_mixed_hall_assembly.py
```

The checker exhausts small bipartite compatibility graphs and verifies the
weighted Hall/max-flow equivalence with exact integer capacities.  It
constructs block decoders and audits their assembled load and recovery
lists.  For \(4\le r\le30\), it checks the rational configuration (12) is
in general position and convex, and that exactly \(r-3\) consecutive pairs
give mixed trace representations.  Finally it builds repeated coherent
roots over an exact rational separated configuration and verifies the
root-bank overlap (15).
