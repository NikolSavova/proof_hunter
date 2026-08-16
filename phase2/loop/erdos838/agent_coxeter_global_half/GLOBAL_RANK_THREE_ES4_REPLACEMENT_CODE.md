# Global rank-three replacement from the planar ES(4) bank

**Date:** 2026-08-15.  All point sets are in general position.

## Verdict

Every collection of literal rank-three temporal histories on an \(n\)-point
planar set can be pooled and label-replaced by ordinary convex
quadrilaterals with universal load and recovery list at most \(10\).
No local two-tangent compatibility is required.

More generally, all literal histories of ranks one, two, and three can be
pooled into the same rank-four bank with universal load/list at most \(80\).
At growing rank \(r\), the same argument with the classical
Erdős--Szekeres number gives a load/list \(2^{O(r^2)}\).  Hence every
literal rank \(r=o(\sqrt{\log n})\) has an \(n^{o(1)}\) global replacement
code.
Thus the matching-star obstruction to local Hall expansion is not a global
obstruction at constant history rank.  Any surviving Coxeter obstruction
must lie in the intermediate range
\(\Omega(\sqrt{\log n})\le r<\log n\), have additional multiplicity not
recovered by its literal support, or have a global bank-incidence constraint
not present in a single pooled allocation.

## 1. Universal convex-quadrilateral reservoir

Let \(v_4(P)\) be the number of four-point subsets of \(P\) in convex
position.  Every five-point set contains a convex quadrilateral.  Count
pairs \((Q,S)\) where \(Q\) is a convex four-set and \(Q\subset S\), with
\(|S|=5\).  Every five-set contributes at least one pair and every \(Q\)
occurs in exactly \(n-4\) five-sets.  Hence

\[
 \boxed{v_4(P)\ge {\binom n5\over n-4}={1\over5}\binom n4.} \tag{1}
\]

This is the only geometric input.

## 2. Rank-three code

Assume the histories are literal: their three physical labels recover the
history, so their number is at most \(\binom n3\).  At activity \(1/2\), the
amplified demand of one rank-three history is \(n/8\).  Give it
\[
                         q=\left\lceil {n\over8}\right\rceil \tag{2}
\]
unit-capacity code slots.  The total number of slots is at most
\[
                         T_3=\binom n3 q.                \tag{3}
\]

For \(n\ge5\), \(q\le(n-3)/2\).  Combining this with (1),
\[
 {T_3\over v_4(P)}
 \le {5\binom n3 q\over\binom n4}
 ={20q\over n-3}\le10.                                  \tag{4}
\]

Order all histories canonically and order the ordinary convex four-faces.
Use ten formal copies of the latter bank, and give each history the next
\(q\) unused slots.  Place weight \((n/8)/q\le1\) on each assigned slot.
After the copy index is forgotten, every physical face has load at most
ten.  Given a physical output, its ten possible copy slots identify a list
of at most ten history blocks.  Thus

\[
 \boxed{\text{output load}\le10,\qquad
        \text{history-recovery list}\le10.}             \tag{5}
\]

The code is global and label-replacing: the quadrilateral need not contain
any label of the history.  Its globally known combinatorial rank in the
ordinary-face bank is the recovery code.

If a literal support has at most \(c\) admissible temporal orientations,
the same proof gives load/list at most \(10c\).

## 3. Joint ranks one through three

For a rank-\(r\) literal history use
\(\lceil n/2^r\rceil\) slots.  The combined slot count is
\[
 T_{\le3}=\sum_{r=1}^3\binom nr
                \left\lceil{n\over2^r}\right\rceil.      \tag{6}
\]

Using \(\lceil x\rceil\le x+1\), direct comparison with \(\binom n4\)
gives, for \(n\ge5\),
\[
\begin{aligned}
 { \binom n1(n/2+1)\over\binom n4}&\le {7\over2},\\
 { \binom n2(n/4+1)\over\binom n4}&\le {9\over2},\\
 { \binom n3(n/8+1)\over\binom n4}&\le {13\over4}.
\end{aligned}                                           \tag{7}
\]
The three ratios decrease after \(n=5\), and their displayed sum is
\(45/4<16\).  Therefore
\[
                  T_{\le3}\le16\binom n4\le80v_4(P).     \tag{8}
\]
The same block allocation gives joint load/list at most \(80\).

## 4. General literal-rank replacement

Let \(r\ge3\) and put \(k=r+1\).  The classical cups--caps bound gives
\[
 t_r:=ES(r+1)\le\binom{2r-2}{r-1}+1\le4^r+1.            \tag{9}
\]
Every \(t_r\)-subset of \(P\) contains an ordinary convex \(k\)-subset.
Double counting pairs consisting of such a \(k\)-face and a containing
\(t_r\)-set gives
\[
 \boxed{v_{r+1}(P)\ge
 { \binom n{r+1}\over \binom{t_r}{r+1}}.}               \tag{10}
\]

There are at most \(\binom nr\) literal rank-\(r\) histories.  Giving each
\(\lceil n/2^r\rceil\) code slots and applying the same pooled block
allocation gives load and recovery list at most
\[
 L_r=
 \left\lceil
 \binom{t_r}{r+1}{r+1\over n-r}
 \left\lceil{n\over2^r}\right\rceil
 \right\rceil.                                         \tag{11}
\]
For \(r\le\log n\) and \(r\le n/2\),
\[
 L_r\le
 1+{4(r+1)\over2^r}\binom{4^r+1}{r+1}
 =2^{O(r^2)}.                                          \tag{12}
\]
Pooling all ranks \(r\le R\) adds only a factor \(R\).  Therefore
\[
 R=o(\sqrt{\log n})
 \quad\Longrightarrow\quad
 \sum_{r\le R}L_r=n^{o(1)}.                             \tag{13}
\]
At the other endpoint, mapping a history to itself has load
\(n2^{-r}\le1\) for \(r\ge\log n\).  The remaining literal-rank interval is
thus
\[
                 \Omega(\sqrt{\log n})\le r<\log n.     \tag{14}
\]

The asymptotic conclusion uses only the classical \(ES(k)\le4^{k+O(1)}\)
bound.  Sharper Erdős--Szekeres estimates improve the constant in
\(\log L_r\), but not the square-root threshold of this direct method.

## 5. Scope

This theorem does not solve the intermediate interval in (14).  Nor does
(5) allow independent modules to reuse the same global quadrilateral bank:
they must be pooled into one allocation, or their incidence must be
separately bounded.

The exact verifier is

~~~text
python3 phase2/loop/erdos838/agent_coxeter_global_half/verify_global_rank_three_es4_code.py
~~~

It checks the algebra for \(5\le n\le500\), the generalized load formula
through \(r=18\), exact convex-quadrilateral counts on rational test
configurations, and an explicit block allocation.
