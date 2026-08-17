# Strict-subhalf linear pockets force a common linear circuit core

**Date:** 2026-08-17. All logarithms are base two. This note generalizes
`INDUCED_SUBSET_HIGH_RANK_POCKET_LIFT_GATE.md` from a
near-ambient pocket to a fixed-power pocket. It uses only the established
quarter-coefficient lower bound, not a coefficient-one-half inductive
hypothesis.

## Verdict

Fix \(0<\delta<1/2\). Suppose that an \(n\)-point planar configuration
\(P\), \(L=\log n\), satisfies

\[
                 \log V(P)\le (1/2-\delta+o(1))L^2.       \tag{1}
\]

Put

\[
 a=1-\delta^2,\qquad |X|=n^{a+o(1)},\qquad Y=P\setminus X. \tag{2}
\]

The ordinary faces inside the pocket \(X\) and the rank
\((1/2-o(1))L\) Erdős--Szekeres bank inside \(Y\) form a Cartesian record
rectangle of logarithmic size

\[
 \left({1\over4}+{a^2\over4}-o(1)\right)L^2
 =\left({1\over2}-{\delta^2\over2}+{\delta^4\over4}
          -o(1)\right)L^2.                              \tag{3}
\]

Relative to (1), this has the fixed quadratic surplus

\[
             \boxed{\eta_\delta=\delta-{\delta^2\over2}
                              +{\delta^4\over4}>0.}       \tag{4}
\]

After fixing a literal exposed source edge and its side, all but an
\(2^{-(\eta_\delta-o(1))L^2}\) fraction of the rectangle is cross-bad.
The exact circuit-deletion theorem then has the following consequence.
There are two face families \(\mathcal A_*\subseteq\mathcal F(P[Y])\)
and \(\mathcal H_*\subseteq\mathcal F(P[X])\), and

\[
 s\ge {\eta_\delta\over65}L,                            \tag{5}
\]

fixed pairwise vertex-disjoint nonordinary crossing four-sets
\(C_1,\ldots,C_s\), such that

\[
 |\mathcal A_*||\mathcal H_*|
       \ge V(P)\,2^{(\eta_\delta/2-o(1))L^2},            \tag{6}
\]

every \(A\in\mathcal A_*\) contains \(C_i\cap Y\), every
\(F\in\mathcal H_*\) contains \(C_i\cap X\), and every union
\(A\cup F\) is nonordinary. Thus **every fixed strict gap below one half
forces a literal linear common-circuit core with quadratic continuation
mass**.

This is a stronger and cleaner strict-deficit residue than the earlier
\(n/\operatorname{polylog}n\) pocket, where only
\(\Theta(\log\log n)\) circuits were forced. It is not a closure. The
fixed circuits need not hit all the other bad circuits of a record. Deleting
one label from each common circuit therefore does not necessarily make
\(A\cup F\) ordinary. Their own support has only \(O(L)\) labels, so its
entire Boolean face bank has size only \(2^{O(L)}\), far below the
quadratic continuation mass in (6).

The exact remaining theorem can now be phrased without a
quasipolynomial-scale ambiguity:

> **Common-core conversion target.** Exclude (6) in a strict-subhalf
> minimizer by either finding a common transversal of all crossing
> circuits on a positive-mass subrectangle, or charging the varying
> residual transversals to a physical ordinary support/profile bank of
> size \(V(P)2^{\Omega(L^2)}\).

The anti-aligned two-parabola construction shows that local planarity,
rank, a common exposed edge, and a linear circuit matching do not imply
this conversion. Its internal convex clouds are Boolean and hence violate
(1); the missing input is genuinely the global strict-subhalf/minimizer
condition.

## 1. The linear-scale pocket ledger

The known unrestricted lower bound gives, for every fixed \(a>0\),

\[
 V(P[X])\ge
 2^{(a^2/4-o(1))L^2}.                                  \tag{7}
\]

Take \(t=n^{1/2+o(1)}\). The best asymptotic Erdős--Szekeres theorem
provides

\[
                       r=(1/2-o(1))L                    \tag{8}
\]

such that every \(t\)-set contains an ordinary rank-\(r\) face. The
induced-subset double count gives a family \(\mathcal A\) of ordinary
rank-\(r\) faces in \(Y\) satisfying

\[
 |\mathcal A|
 \ge {\binom{|Y|}{r}\over\binom tr}
 \ge (|Y|/t)^r
 =2^{(1/4-o(1))L^2}.                                    \tag{9}
\]

Here \(|Y|=n(1-o(1))\), because \(a<1\). Let
\(\mathcal H=\mathcal F(P[X])\setminus\{\varnothing\}\). Combining
(7) and (9) proves (3). The identity

\[
 {1\over4}+{(1-\delta^2)^2\over4}
       -\left({1\over2}-\delta\right)
 =\delta-{\delta^2\over2}+{\delta^4\over4}             \tag{10}
\]

is (4).

Every source in \(\mathcal A\) has \(r\) exposed directed boundary
edges. There are fewer than \(n^2\) physical edge-and-side states, so one
state is shared by a subfamily \(\mathcal A_e\) with

\[
                    |\mathcal A_e|\ge r|\mathcal A|/n^2. \tag{11}
\]

The loss in (11) is \(O(L)=o(L^2)\). On the good pairs, union is an
injective map from \(\mathcal A_e\times\mathcal H\) into
\(\mathcal F(P)\), since the physical grounds are disjoint. Hence (1),
(3), and (11) show that the good density is at most

\[
                         2^{-(\eta_\delta-o(1))L^2}.     \tag{12}
\]

## 2. Linear circuit matching and literal localization

For a bad pair \((A,F)\), let \(\tau_\times(A,F)\) be the minimum number
of labels meeting every nonordinary crossing four-subset of \(A\cup F\).
The exact deletion decoder gives

\[
 |\{(A,F):\tau_\times(A,F)\le d\}|
       \le S_d(n)V(P),
 \qquad S_d(n)=\sum_{j\le d}\binom nj.                  \tag{13}
\]

Put

\[
 s=\left\lfloor{\eta_\delta L\over64}\right\rfloor,
 \qquad d=8s.                                           \tag{14}
\]

Since \(d=O(L)\),

\[
 \log S_d(n)\le d\log(en/d)
             \le(\eta_\delta/8+o(1))L^2.               \tag{15}
\]

Equations (3), (11)--(13), and (15) imply that asymptotically almost all
records have \(\tau_\times>d\). A maximum matching in a rank-four
hypergraph has size greater than \(d/4=2s\). Choose the first \(s\)
circuits of one such matching. They are fully vertex-disjoint.

There are at most \(n^{4s}\) ordered literal descriptions of these
circuits, and

\[
                 \log n^{4s}\le(\eta_\delta/16+o(1))L^2. \tag{16}
\]

Pigeonholing therefore leaves a record subfamily \(\mathcal R_*\) of
size at least

\[
 |\mathcal R_*|
 \ge V(P)2^{(15\eta_\delta/16-o(1))L^2}.                \tag{17}
\]

The weaker exponent \(\eta_\delta/2\) in (6) leaves ample room for all
integer, empty-face, edge-localization, and bad-density losses.

Let \(\mathcal A_*\) and \(\mathcal H_*\) be the row and column
projections of \(\mathcal R_*\). Every row contains every
\(C_i\cap Y\), and every column contains every \(C_i\cap X\). Therefore
the complete product \(\mathcal A_*\times\mathcal H_*\) still contains
all \(C_i\) and is cross-bad. Also

\[
             |\mathcal A_*||\mathcal H_*|
                    \ge|\mathcal R_*|,                  \tag{18}
\]

which proves (5)--(6). Notice that passing to the complete product loses
no record mass and restores a literal rectangle.

## 3. What the common core gives, and what it does not

Put

\[
 Y_0=\bigcup_i(C_i\cap Y),\qquad
 X_0=\bigcup_i(C_i\cap X).                               \tag{19}
\]

Both \(Y_0\) and \(X_0\) are ordinary: they are contained in every
member of \(\mathcal A_*\), respectively \(\mathcal H_*\). The circuits
are disjoint, so every transversal of the full crossing-circuit hypergraph
has size at least \(s\). But (19) has at most \(4s=O(L)\) labels. Even
granting every subset of both sides gives only

\[
                       2^{|Y_0|}+2^{|X_0|}=2^{O(L)}.      \tag{20}
\]

This cannot absorb (6). A common deletion set \(G\) *would* finish: if
\(|G|=O(L)\), \(G\) is fixed over the rectangle, and

\[
                    (A\cup F)\setminus G                 \tag{21}
\]

were ordinary for every record, then (21) would recover \((A,F)\) after
reattaching the fixed labels, contradicting (6). The present theorem does
not produce such a \(G\): the selected circuits are a matching, not a
maximal matching or a transversal of all residual circuits.

The all-delete two-parabola regression is exact. Take a rank-\(r\) face
on one convex parabola and a rank-at-least-three face on the anti-aligned
parabola. Every source singleton together with a pocket triple is a bad
four-set, so the minimum source deletion is all \(r\) labels. Since the
source surplus in (9) is \(b(1-b)L^2\) at rank \(bL\), while literalizing
or guessing all source labels costs \(bL^2\),

\[
                         b(1-b)<b\qquad(0<b<1).          \tag{22}
\]

Thus linear scaling does not make the naive all-delete decoder affordable.
The regression is not a strict-subhalf construction because each physical
parabola is convex and contributes a gigantic Boolean bank. Precisely that
global payment is absent from the current abstract rectangle theorem.

## 4. Strategic consequence and insertion-interval correction

From (6) and the trivial bounds
\(|\mathcal A_*|,|\mathcal H_*|\le V(P)\), one still has the useful exact
consequence

\[
 |\mathcal A_*|,|\mathcal H_*|
             \ge2^{(\eta_\delta/2-o(1))L^2}.             \tag{23}
\]

An earlier draft asserted more: it assigned every continuation label a
unique insertion edge of the common convex core and inferred a product of
independent ear-cell traces. That assertion is false. A point outside a
convex polygon has a **visible boundary interval**, which may contain
several consecutive edges. Even after pigeonholing the interval type, traces
belonging to different carriers need not be freely recombinable. The cyclic
independent-set averaging calculation in the verifier is correct as an
abstract calculation, but its geometric hypothesis was not established and
is not used here.

Thus (23) says that both continuation families are quadratically large, but
it does not factor either family into a large ordinary profile product. The
remaining loss is more basic: after the common bad circuits are deleted,
new bad circuits can use private continuation labels. Any closing theorem
must either release a positive fraction of the rectangle after deleting the
common core, control the resulting residual circuit cascade, or show that
the cascade admits a decreasing mutation.

The earlier pocket target asked for a
\(2^{\Theta(L\log L)}\) conversion from only
\(\Theta(\log L)\) circuits. Equations (5)--(6) replace it, under a fixed
strict-subhalf hypothesis, by a scale-matched statement:

* the continuation mass is \(2^{\Theta(L^2)}\);
* the common physical circuit core has \(\Theta(L)\) disjoint circuits;
* all description, edge, and fixed-circuit localization losses have been
  paid; and
* the only unpaid information is the residual crossing-circuit
  transversal/history outside that core.

This is a legitimate narrowing for the secondary strict-deficit mutation
route. It does not improve the unconditional coefficient, and it should
not be renamed into another decoder problem. The next attack must use
global low-\(V\) geometry to turn the common core into a common transversal,
a large convex support, or a decreasing physical mutation.

## 5. Verification

Run

```text
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_strict_subhalf_linear_pocket_circuit_core.py
```

The verifier checks the exact rational coefficient identity for a dense
grid of strict gaps, optimizes the source sampling exponent, checks the
deletion/localization budget with integer floors at large finite scales,
and verifies the all-delete cost inequality.
