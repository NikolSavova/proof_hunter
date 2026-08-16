# Joint detached-bank allocation: rank two fails, rank four passes

**Date:** 2026-08-15

## Verdict

The detached rank-one/two codes from
`LOCAL_TRACE_HALL_MATCHING_BARRIER.md` cannot be globally allocated across
the \(q^2\) matching star with subpolynomial load.  This is a full-set Hall
obstruction, independent of ownership or recovery ingenuity.

There is nevertheless an exact bounded-rank repair.  Pool all trace demands
*before* assigning outputs and promote the detached code from rank two to
rank four.  On the balanced matching star \(q=m\), the rank-four subsets of
the two homogeneous side clouds support one global decoder with output load
and recovery list at most \(14\).  Rank five improves this to load one and
recovery fibre one.  In both cases the output list recovers the side, both
trace endpoints, and the apex; no trace mark is external.

The same joint-allocation theorem passes the other primary regression.  If
\(q\le m\) coherent roots share the complement \(E(k,k)\), then for every
\(k\ge7\) its one top mixed bank supports **all roots at once** with load
and recovery fibre one.  In particular, every terminal maximal-cup history
is recovered.

Thus the exact lesson is:

\[
 \boxed{
 \text{independent rank-1/2 side codes fail globally, but a joint
 physical-bank code passes both kill tests (at rank 4 for the star).}} \tag{1}
\]

This is not yet a theorem for every reflection order: an arbitrary detached
side complex need not contain enough rank-four faces.  It gives an exact
sufficient condition, proves the low-rank barrier, and removes the
matching-star and \(E(k,k)\) families as obstructions to joint allocation.

## 1. Joint complete-bank theorem

Let \(\mathcal I\) be a family of cell-history records.  Record \(h\) has
demand \(d_h\), and every record is allowed to use every output in one
common ordinary-face bank \(\mathcal B\).  The record index includes all
cell data that must be recovered.

> **Theorem 1 (joint block allocation).** If, for an integer \(L\ge1\),
> \[
>  L|\mathcal B|\ge\sum_{h\in\mathcal I}\lceil d_h\rceil,      \tag{2}
> \]
> then there is a decoder of output load and recovery list size at most
> \(L\).  For \(L=1\), the recovery fibre is exactly one.

**Proof.**  Canonically order the records and \(L\) formal copies of the
bank, with all physical faces in one copy consecutive.  Give \(h\) the next
\(\lceil d_h\rceil\) unused slots and put equal flow
\(d_h/\lceil d_h\rceil\le1\) on them.  In the applications below each
record block is shorter than \(|\mathcal B|\), so it uses a physical face at
most once.  Forgetting the copy index leaves load at most \(L\).  From a
physical output, enumerate its at most \(L\) copy slots; their block indices
give a recovery list of at most \(L\) records.  For \(L=1\) the record is
unique. \(\square\)

The word “joint” is essential.  Constructing the same owned side block
independently in every trace gives quadratic reuse; ordering all
cell-history records first makes recovery part of the allocation.

## 2. Exact rank-one/two obstruction

Use the multi-trace matching-star construction with side clouds

\[
 |X|=|Y|=m,\qquad |J|=|L|=q=m.                           \tag{3}
\]

The ambient size is \(N=4m\).  For every trace
\((j_a,l_b)\), there are \(m\) left singleton side histories and \(m\)
right singleton side histories.  Hence there are

\[
 2m^3                                                     \tag{4}
\]

cell-history records.  Every record has rank three, half weight \(1/8\),
and desired demand \(N/8=m/2\).  Their total demand is exactly

\[
 \boxed{D_{\rm tot}=m^4.}                               \tag{5}
\]

The original detached bank consists of the nonempty rank-at-most-two faces
inside \(X\) or inside \(Y\).  Its size is

\[
 |\mathcal S_2(X,Y)|
 =2\left(m+\binom m2\right)=m(m+1).                    \tag{6}
\]

Therefore every fractional joint decoder into that bank has full-cut load

\[
 \boxed{
 \lambda\ge\frac{m^4}{m(m+1)}
 =\frac{m^3}{m+1}=\Theta(N^2).}                         \tag{7}
\]

Even allowing **every** ambient rank-one/two face gives at most

\[
 \binom N1+\binom N2=\frac{N(N+1)}2\le N^2             \tag{8}
\]

outputs, and hence

\[
 \lambda\ge\frac{m^4}{N^2}=\frac{N^2}{256}.            \tag{9}
\]

Allowing every face of rank at most three still cannot give
subpolynomial load.  Since

\[
 \sum_{r=1}^3\binom Nr\le N^3,
\]

the full cut forces

\[
 \lambda\ge\frac{m^4}{N^3}=\frac N{256}.               \tag{10}
\]

Thus endpoint marking by only one extra label, or any other rank-three
alphabet, does not close the matching star.  Some further rank promotion or
non-face telescope is necessary.

## 3. Constant-load rank-four repair

The exact realization in `LOCAL_TRACE_HALL_MATCHING_BARRIER.md` makes
\(X\) a strict cup and \(Y\) a strict cap.  Consequently every subset of
either cloud is an ordinary face.  First use the common rank-four bank

\[
 \mathcal B_4=\binom X4\mathbin{\dot\cup}\binom Y4,
 \qquad |\mathcal B_4|=2\binom m4.                      \tag{11}
\]

Ceiling the demand of each record separately requires

\[
 T_m=2m^3\left\lceil\frac m2\right\rceil.              \tag{12}
\]

For \(m\ge47\), direct expansion gives

\[
 T_m\le14|\mathcal B_4|=28\binom m4.                   \tag{13}
\]

Indeed \(T_m\le m^3(m+1)\), and (13) follows from

\[
 6m^2(m+1)\le7(m-1)(m-2)(m-3),                         \tag{14}
\]

which holds at \(m=47\) and whose right-minus-left polynomial is increasing
thereafter.  Theorem 1 with \(L=14\) gives global load and an exact recovery
list of size at most \(14\).  Since every record block has length
\(\lceil m/2\rceil<|\mathcal B_4|\), the slot construction never assigns
one record twice to the same physical face.

This is optimal in rank up to the gap between load one and constant load:
(10) rules out every rank-at-most-three alphabet with subpolynomial load,
while rank four succeeds with a universal constant.

## 4. Fibre-one rank-five repair

For unique rather than constant-list recovery, use

\[
 \mathcal B_5=\binom X5\mathbin{\dot\cup}\binom Y5,
 \qquad |\mathcal B_5|=2\binom m5.                     \tag{15}
\]

outputs.  For \(m=70\), direct integer evaluation gives

\[
 2\binom{70}{5}=24{,}206{,}028
 >24{,}010{,}000=T_{70}.                               \tag{16}
\]

For \(m\ge71\),

\[
\begin{aligned}
 2\binom m5
 &=\frac{m(m-1)(m-2)(m-3)(m-4)}{60}\\
 &\ge m^3(m+1)
 \ge2m^3\left\lceil\frac m2\right\rceil.             \tag{17}
\end{aligned}
\]

The first inequality in (17) is equivalent to

\[
 m^4-70m^3-25m^2-50m+24\ge0;                           \tag{18}
\]

it is positive at \(m=71\) and increasing thereafter.  Thus (2) applies
for every \(m\ge70\).

Order records by

\[
 (\text{side},a,b,i),                                   \tag{19}
\]

and order the five-subsets of \(X\), followed by those of \(Y\),
lexicographically.  The output's combinatorial rank identifies its block,
which recovers all four entries in (19).  Flow per output is

\[
 \frac{m/2}{\lceil m/2\rceil}\le1.                     \tag{20}
\]

This proves load and fibre one.  It is a genuine global recovery code, not
a family of marked local copies.  Rank five has a full factor
\(\Theta(m)\) of slack beyond the rank-four constant-list code.

## 5. Joint coherent-root code on \(E(k,k)\)

Let the complement be \(P=E(k,k)\), with

\[
 m=|P|=\binom{2k-4}{k-2},                               \tag{21}
\]

and add \(q\le m\) coherent positive roots.  Each root has all nonempty cup
histories \(S\subseteq P\).  The ambient amplification is
\(N=m+q\le2m\), so the joint ceiling demand is at most

\[
 T_{q,k}
 \le q\left(\frac N2U_{k,k}(1/2)+U_{k,k}(1)\right).    \tag{22}
\]

Let

\[
 W_k=U_{k-1,k}(1).                                      \tag{23}
\]

The top mixed bank of \(P\) has size \(W_k^2\).  Exact recurrence verifies

\[
 \boxed{W_k^2\ge T_{q,k}\qquad(k\ge7,\ q\le m).}       \tag{24}
\]

Here is a uniform proof for \(k\ge20\).  The path bounds from
`LABEL_REPLACING_ES_MIXED_CODE.md` give

\[
 U_{k,k}(1)\le4^k mW_k,
 \qquad
 W_k\ge2^{(k-3)(k-2)/2},
 \qquad
 m\le2^{2k-4}.                                         \tag{25}
\]

Since \(U(1/2)\le U(1)\), \(q\le m\), and \(N\le2m\),

\[
 T_{q,k}\le2m^2U_{k,k}(1)
 \le2\cdot4^k m^3W_k.                                 \tag{26}
\]

For \(k\ge20\),

\[
 \frac{(k-3)(k-2)}2\ge8k-11,
\]

so (25) yields

\[
 W_k\ge2^{8k-11}
 \ge2\cdot4^k m^3.                                    \tag{27}
\]

Equations (26)--(27) prove (24).  Exact integer/rational recurrence checks
the finite rows \(7\le k\le19\).  Applying Theorem 1 to the joint record
order \((\text{root},S)\) gives load and fibre one.  The output block
recovers both the root and the original cup history, including the terminal
\(E(k,3)\) cup.

The small rows \(k=5,6\) fail this particular one-bank capacity test when
\(q=m\); this is finite-scale behavior and is recorded rather than hidden.

## 6. Exact scope and next interface

Theorem 1 reduces joint detached allocation to one measurable quantity:

\[
 \boxed{
 \text{Does a group of trace cells sharing a side complex have at least
 the ceiling demand in ordinary faces of rank }n^{o(1)}?}             \tag{28}
\]

The matching star answers yes at rank four; \(E(k,k)\) answers yes in its
top mixed bank.  An arbitrary side complex can have far fewer rank-four
faces, so (25) is not automatic.  Failure of (25) is now a concrete
low-rank face-deficit alternative which must be charged recursively to a
larger ancestor or another side.

Independent local ownership is unnecessary and, by (7), impossible to
globalize on its original alphabet.  The correct unit is the entire group
of cells sharing a physical bank, allocated by one Hall/block instance.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_coxeter_global_half/verify_joint_detached_bank_rank_promotion.py
```

The checker constructs exact multi-trace matching stars, verifies the
\(q^2\) compatibility regression, and checks (5)--(18) through \(m=200\).
At \(m=70\) it implements combinatorial ranking/unranking of both the
14-copy rank-four code and the fibre-one rank-five code, auditing
boundary/sample recovery and load without materializing either bank.  It
also computes the exact cup
coefficient vectors and joint top-bank demands for \(5\le k\le30\), checks
the failures at \(k=5,6\), (24) from \(k=7\), and the uniform estimates
(25)--(27).
