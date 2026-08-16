# Gap-budgeted mutation by a repair alphabet

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

The fixed-gap route removes both the least-counterexample slack problem and
the apparent cost of crossing many arrangement walls. Put

\[
                         \overline V(P)=V(P)+1,
\]

so that the empty face is included. Relocating one labelled point, with every
other point fixed, changes \(\overline V\) by a factor of at most two. More
strongly, if

\[
 \Phi_P(z)=\sum_{\substack{F\text{ ordinary in }P\\
                           \text{including }F=\varnothing}}z^{|F|},
\]

then for two positions \(x,y\) over the same deletion base \(Q\),

\[
                 \Phi_{Q+y}(z)\le (1+z)\Phi_{Q+x}(z)              \tag{1}
\]

coefficientwise. Consequently an arbitrary re-embedding of a repair alphabet
\(X\) of \(k\) physical labels costs at most \(k\) bits:

\[
       \overline V(Q\cup X')\le2^k\overline V(Q\cup X).          \tag{2}
\]

This is an endpoint comparison. An adjacent mutation path may cross
quadratically many pair lines, but all of its rooted edge-star derivatives
reuse the same face bank of \(Q\) and telescope to (1). Intermediate
configurations need not remain below the fixed-gap threshold.

Combining (2) with the loss-stable strong-tree theorem gives the following
exact conditional closure. Suppose \(P\) has

\[
                \log V(P)\le\left({1\over2}-\delta\right)L^2,
                \qquad L=\log n,                                 \tag{3}
\]

and an induced \(m\)-label set can be turned into a same-chart approximate
strong tree by relocating \(k\) labels, with one-turn decoder loss \(G\).
Then, exactly,

\[
 \log\{V(P)+1\}
 \ge {1\over2}(\log m)^2-O((\log m)^{3/2})-G-k.                   \tag{4}
\]

The assumption (3) makes the left side at most
\((1/2-\delta)L^2+o(1)\). Thus, when \(m=n^{1-o(1)}\), every repair with
\(G+k=o(L^2)\) contradicts (3). In particular, \(O(L)\) marked turns can
be repaired at negligible cost if each uses an exclusive blocked singleton
and the repaired seam banks really form one same-chart approximate strong
tree.

The last qualification is the surviving gate. The current marked all-delete
forest does not prove that its turn labels are exclusive, that one physical
position can satisfy every seam assigned to a reused label, or that repairing
the singleton also repairs the full released face/profile recurrence. These
are promotion failures, not mutation-budget failures.

There is an exact geometric formulation. Every common exposed-edge source
star has a nonempty open **ear chamber** in which its blocked singleton may be
placed so that every source-retaining union becomes ordinary. Distinct repair
labels may be placed independently. If one physical label is assigned several
turns, it works precisely when the corresponding ear chambers have a common
point. Empty intersection already has a witness of at most three chambers by
planar Helly. No current theorem turns such a two- or three-seam incompatibility
into the required cyclic/profile bank.

## 1. The deletion-base comparison

Let \(Q\) be any planar general-position configuration, and let \(x\) be a
new labelled point. Define

\[
 \mathcal L_x(Q)=
   \{R\subseteq Q:R\cup\{x\}\text{ is ordinary in }Q\cup\{x\}\}.
                                                                    \tag{5}
\]

Heredity gives

\[
                         \mathcal L_x(Q)\subseteq\mathcal F(Q),    \tag{6}
\]

where \(\mathcal F(Q)\) is the ordinary-face complex of \(Q\). Splitting
faces according to whether they contain \(x\) gives the exact identity

\[
       \Phi_{Q+x}(z)=\Phi_Q(z)+z
               \sum_{R\in\mathcal L_x(Q)}z^{|R|}.                 \tag{7}
\]

> **Theorem 1 (one-bit relocation).** For arbitrary general-position
> positions \(x,y\), equations (1) and
> \[
>       \overline V(Q+y)\le2\overline V(Q)
>                       \le2\overline V(Q+x)                      \tag{8}
> \]
> hold. For \(k\) relocated labels, (2) holds.

**Proof.** By (6)--(7),

\[
 \Phi_{Q+y}(z)\le(1+z)\Phi_Q(z)
                 \le(1+z)\Phi_{Q+x}(z)
\]

coefficientwise. Setting \(z=1\) proves (8).

For the multi-label statement, delete all of \(X\) and use the same base
\(Q\). Every ordinary face of \(Q\cup X'\) maps to an ordinary face of
\(Q\), and every output has at most \(2^k\) choices for its intersection
with \(X'\). Equivalently,

\[
       \Phi_{Q\cup X'}(z)\le(1+z)^k\Phi_Q(z)
                    \le(1+z)^k\Phi_{Q\cup X}(z).                  \tag{8a}
\]

Setting \(z=1\) proves (2) without requiring any sequence of
general-position hybrid embeddings. \(\square\)

No convexity of \(Q\) is used. The argument also preserves arbitrary fixed
metadata which can be decoded after deleting the relocated label.

## 2. Adjacent flips and the fan paid once

Fix positions \(x,y\), and consider the arrangement of the
\({|Q|\choose2}\) pair lines of \(Q\). A generic straight path from \(x\)
to \(y\), perturbed away from line intersections, crosses exactly the pair
lines which separate the two chambers. Each crossing is one adjacent
rank-three mutation. The coefficientwise derivative at a wall \(ab\) is
the exposed-edge-star formula

\[
       \Delta\Phi(z)=z\bigl(\Phi^+_{ab}(z)-
                                  \Phi^-_{ab}(z)\bigr).            \tag{9}
\]

Summing (9) along the path gives

\[
 \sum_i\Delta_i\Phi(z)
   =z\left(\sum_{R\in\mathcal L_y(Q)}z^{|R|}
                  -\sum_{R\in\mathcal L_x(Q)}z^{|R|}\right).     \tag{10}
\]

Thus the relevant cost is not the number of crossed walls or the sum of
their positive derivatives. The whole intervening fan is paid once by the
literal deletion map

\[
                          R\cup\{y\}\longmapsto R.                \tag{11}
\]

This map has load one into \(\mathcal F(Q)\). It is the global cancellation
which is invisible if every adjacent flip is charged a separate factor two.

The wall count itself can be quadratic. Let

\[
 Q_r=\{(i,i^2):-r\le i\le r\},\qquad
 x=\left(0,{r^2\over4}+{1\over3}\right),                          \tag{12}
\]

and move \(x\) to a small inside neighborhood of the boundary edge joining
\((0,0)\) and \((1,1)\). For every \(1\le u,j\le\lfloor r/3\rfloor\),
the line joining \((-u,u^2)\) and \((j,j^2)\) separates the two chambers.
Hence every adjacent path crosses at least

\[
                            \lfloor r/3\rfloor^2                  \tag{13}
\]

walls. Nevertheless Theorem 1 charges the complete relocation only one bit.
This is the requested adjacency-or-fan audit: adjacency can be expensive in
flip count, but the fan has an exact common-base decoder.

## 3. The fixed-gap budget

Let \(S\subseteq P\) have \(m\) physical labels and write \(S=Q\cup X\),
where \(|X|=k\). Suppose new rational general-position positions \(X'\)
exist such that \(S'=Q\cup X'\) carries a same-chart approximate ordered
strong tree. Let its certified ordinary banks have one-turn decoder loss
\(G\), in the notation of
`ROBUST_WEIGHTED_APPROXIMATE_STRONG_TREE_GATE.md`.

> **Theorem 2 (gap-budgeted repair).** One has
> \[
>  \log\{V(P)+1\}
>   \ge {1\over2}(\log m)^2-O((\log m)^{3/2})-G-k.                \tag{14}
> \]

**Proof.** Heredity and Theorem 1 give

\[
      \overline V(S')\le2^k\overline V(S)
                             \le2^k\overline V(P).                \tag{15}
\]

The robust strong-tree comparison gives

\[
             \log V(S')\ge {1\over2}(\log m)^2
                              -O((\log m)^{3/2})-G.               \tag{16}
\]

Since \(\overline V(S')\ge V(S')\), combine (15)--(16). \(\square\)

If \(m=n^\alpha\), the usable repair budget against (3) is

\[
 B_{\delta,\alpha}
   =\left[{\alpha^2\over2}-\left({1\over2}-\delta\right)\right]L^2
       -O(L^{3/2}).                                                \tag{17}
\]

The closure condition is \(G+k<B_{\delta,\alpha}\). For
\(\alpha=1-o(1)\), this is \(G+k<\delta L^2-o(L^2)\). Notice that
the budget is in the number of **relocated physical labels**, not in the
number of adjacent walls crossed by them.

## 4. Exact ear repair at one marked seam

Let \(\mathcal H\) be a finite family of ordinary sources \(R\subseteq Q\).
Suppose every \(R\in\mathcal H\) contains the same exposed edge \(ab\), and
all vertices of \(R\setminus\{a,b\}\) lie in the same open halfplane of
\(ab\). Choose a point \(t\) in the open segment \(ab\), avoiding all other
pair lines.

For each \(R\), every point in a sufficiently small one-sided neighborhood
of \(t\), on the side opposite \(R\), is an exterior ear of \(R\). Since
\(\mathcal H\) is finite, the intersection of these neighborhoods contains
a common nonempty open disk sector \(C(\mathcal H,ab,t)\).

> **Lemma 3 (common-star ear repair).** If \(x'\) is a generic rational
> point of \(C(\mathcal H,ab,t)\), then
> \[
>                    R\cup\{x'\}\text{ is ordinary}
>                    \qquad(R\in\mathcal H),                      \tag{18}
> \]
> and the outputs in (18) injectively recover the literal source by deleting
> \(x'\).

The proof is the exposed-edge argument in the single-flip derivative: the
edge \(ab\) is replaced by \(ax'\) and \(x'b\), while every old vertex
remains exposed.

For several marked turns, assign each turn \(v\) such an ear chamber
\(C_v\). If each turn has its own physical blocked label, choose the repaired
positions independently. If turns in \(I_x\) reuse one label \(x\), a single
repair is possible whenever

\[
                              \bigcap_{v\in I_x}C_v\ne\varnothing. \tag{19}
\]

The chambers are open convex sets after choosing their small disk sectors.
By planar Helly, failure of (19) is witnessed by at most three turns. This
is an exact finite obstruction, but it is not yet a bank: arbitrary
two-/three-chamber incompatibility does not prove a convex cyclic union.

## 5. Conditional marked-tree corollary

Call a marked approximate strong-tree certificate **single-ear deficient**
if:

1. every uncertified recurrence term is a family
   \(\{R\cup\{x_v\}:R\in\mathcal H_v\}\) satisfying Lemma 3;
2. every other certified output omits all repair labels;
3. for each physical repair label, its assigned ear chambers have nonempty
   intersection; and
4. after adding the repaired terms, all recurrence banks use one fixed
   ordered chart and have decoder loss \(G\).

> **Corollary 4.** A single-ear-deficient certificate on \(m\) labels with
> \(k\) distinct repair labels obeys (14). In particular, if
> \(m=n^{1-o(1)}\), \(k=O(L)\), and \(G=o(L^2)\), it excludes every fixed
> sub-half gap.

Condition 2 makes re-embedding harmless to the already certified banks;
Lemma 3 certifies the missing ones; Theorem 2 then applies.

## 6. Scope against the live marked forest

The theorem settles the **budget** part of the proposed route:

* no least-counterexample slack is needed;
* adjacency to the desired wall is unnecessary;
* an arbitrary number of intervening walls is charged once per physical
  repair label; and
* \(O(L)\) exclusive singleton repairs cost only \(O(L)\) bits, far below
  the \(\delta L^2\) fixed-gap budget.

It does not yet promote the live deletion forest. Three literal questions
remain.

1. **Alphabet size.** A marked turn currently deletes a singleton witness,
   but its desired released object can be a rank-\(\Theta(L)\) face. If that
   whole face must be re-embedded, \(O(L)\) turns can use \(\Theta(L^2)\)
   physical labels and consume the entire fixed-gap budget.
2. **Reuse.** The same actual witness label may carry several turns with
   incompatible ear chambers. The first obstruction has size at most three,
   but no ordinary cyclic/profile bank has been extracted from it.
3. **Same-chart promotion.** Current one-turn source retags do not by
   themselves prove the cap, cup, and ordinary recurrences of a single
   approximate strong tree. The repair theorem cannot manufacture those
   recurrences from selected-family products.

The strongest accurate endpoint is therefore: a fixed-gap proof may spend a
subquadratic **physical repair alphabet**, not a subquadratic number of
adjacent flips. The remaining theorem must convert the marked forest to a
single-ear-deficient same-chart certificate or charge a two-/three-ear reuse
obstruction.

## 7. Verification

The verifier `verify_gap_budgeted_repair_alphabet_mutation_gate.py` uses
exact rational arithmetic. It exhausts all labelled subsets in several
small relocation examples, checks (1) coefficient by coefficient, checks
the \(2^k\) two-label bound, and verifies a common exposed-edge ear star.
It also constructs (12) with \(r=12\) and confirms that the initial and
target chambers are separated by 91 pair lines, despite the one-bit
endpoint bound.
