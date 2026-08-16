# Recoverable carrier coarsening: rooted gaps or one near-ambient run

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

The mask/run split gives an exact positive theorem on the many-gap side.
After trace-dependent carrier labels are deleted, let \(g\) compressed
gaps survive as actual boundary gaps. At least \(g/3\) of them are
pairwise nonadjacent. If gap \(i\) carries \(b_i\) triangular ears sharing
a retained hidden root \(x_i\), then the ordinary rooted-module bank has
size

\[
                       \prod_{i\in I}b_i^2,\qquad |I|\ge g/3.      \tag{1}
\]

The output retains the coarsened carrier, every root, and both endpoint
labels in each selected gap. Empty completion roles recover the monotone
forest path; any additional carrier-coarsening ambiguity is charged by one
explicit load \(\lambda\). Thus \(g=\Omega(\log\log n)\) polynomial-size
gap alphabets recover the full \(n^{\Theta(\log\log n)}\) scale loss.

On the few-run side, a deleted run has

\[
                 k=\Omega\!\left({\log n\over\log\log n}\right)   \tag{2}
\]

roles. With role size \(\Theta(n/\log n)\), its physical support has size

\[
                         m=\Omega\!\left({n\over\log\log n}\right).\tag{3}
\]

This is closer to \(n\) than a single \(n/\log n\) role. For the
coefficient-half target, the exact remaining finite-scale deficit from
an induced \(m\)-point child is at most

\[
              \Theta\!\bigl((\log n)\log\log\log n\bigr),          \tag{4}
\]

and is of that order when \(m=\Theta(n/\log\log n)\). Thus the worst
minimal-run scale needs
\(n^{\Theta(\log\log\log n)}\). The Boolean run bank
\(2^k\) is still much too small at that extremal scale.

No unconditional arbitrary-child two-ended splice follows. The parabolic
central-pair construction from
`ALMOST_FULL_WORD_MIXED_BANK_BARRIER.md` extends to unequal arcs and shows
that every nonempty trace from the long run can be incompatible with every
retained point on the opposite arc while a quadratic-coefficient arbitrary
central child is retained. Hence a cyclic endpoint factorization remains
false. The exact residual is a one-sided directional/reset composition at
the smaller scale (4), or a globally charged common \(1+3\) circuit bank.

## 1. Rooted-module product on surviving compressed gaps

Let \(K\) be the retained convex carrier after a deletion mask is applied
and the released pocket trace is fixed. Suppose
\(e_1,\ldots,e_g\) are distinct mask-created edges which remain actual
boundary edges of \(K\). Their edge-intersection graph is a subgraph of a
cycle and has maximum degree at most two. Greedy selection therefore gives
a set \(I\) of pairwise vertex-disjoint edges with

\[
                              |I|\ge\lceil g/3\rceil.              \tag{5}
\]

For \(i\in I\), let

\[
 T_{i,a}=(\ell_{i,a},z_{i,a},r_{i,a}),\qquad a\in[b_i],            \tag{6}
\]

be triangular ears in the exterior pocket of \(e_i\), and suppose one
retained physical point \(x_i\) lies strictly inside every \(T_{i,a}\).
The tangent lemma in
`HIGH_TRANSVERSAL_COMMON_POCKET_ENDPOINT_PRODUCT.md` gives

\[
                 K\cup\{\ell_{i,a},x_i,r_{i,c}\}
                         \in\mathcal F(P)                         \tag{7}
\]

for all \(a,c\in[b_i]\). Ears on the vertex-disjoint edges \(e_i\) commute,
so every union

\[
            K\cup\bigcup_{i\in I}
                    \{\ell_{i,a_i},x_i,r_{i,c_i}\}                 \tag{8}
\]

is ordinary. Its disjoint role supports recover \(K\), all \(x_i\), and
all \(a_i,c_i\), proving (1).

For a weighted family of coarsened states \(c\), write \(B_c\) for the
product in (1), \(w_c\) for its state weight, and define the literal output
load

\[
 \Lambda=\max_F
   \sum_{\substack{c,\text{ module choice}\\
                    \text{output }F}}w_c.                        \tag{9}
\]

Double counting actual ordinary outputs gives

\[
                 \boxed{\displaystyle
                 \sum_c w_c B_c\le\Lambda V(P).}                  \tag{10}
\]

There is no hidden history factor. The output shows which completion roles
are empty. Their increasing order is the unique role-forest path, whose
stored child labels reconstruct the deleted completion word. If the
coarsening removed further carrier labels, their true ambiguity is exactly
part of \(\Lambda\); it may not be called one without a decoder.

Suppose every usable gap has

\[
                    \log b_i\ge\beta\log n-K\log\log n.           \tag{11}
\]

Then (1) and (5) give

\[
 \log B_c\ge {2g\over3}
      \bigl(\beta\log n-K\log\log n\bigr).                        \tag{12}
\]

Consequently

\[
 g\ge\left({3\sigma\over2\beta}+o(1)\right)\log\log n             \tag{13}
\]

produces \(B_c\ge n^{\sigma\log\log n}\). This is the rooted-module
counterpart of the endpoint entropy threshold in
`../agent_common_shield_mixing/MULTIROLE_ENDPOINT_POCKET_TRANSFER.md`,
with the carrier/root decoder retained explicitly.

If many mask-created gaps are destroyed by the pocket trace, (12) does not
apply. One is in the low endpoint-entropy/double-circuit branch of that
report, not automatically in the long-run branch.

## 2. Exact size and deficit of the long run

Put

\[
 L_1=\log n,\qquad L_2=\log L_1,\qquad L_3=\log L_2.              \tag{14}
\]

Assume \(q=\Theta(L_1)\) role cells, each of size
\(D=\Theta(n/L_1)\). If the mask deletes \(t\ge\tau L_1\) roles in fewer
than \(\rho L_2\) runs, the mask/run lemma gives one run of length

\[
                         k\ge{\tau\over\rho}{L_1\over L_2}.       \tag{15}
\]

Its induced physical support \(X_R\) therefore has

\[
                   m=|X_R|\ge c\,{n\over L_2},\qquad
                   a:=\log{n\over m}\le L_3+O(1).                 \tag{16}
\]

For the pure half target \(\Phi(L)=L^2/2\),

\[
 \Phi(L_1)-\Phi(L_1-a)
                   =L_1a-\frac{a^2}{2}
                   =\Theta(L_1L_3).                              \tag{17}
\]

For the usual corrected target

\[
                       \Phi(L)=\frac12L^2-C L\log L,              \tag{18}
\]

the exact difference is

\[
\begin{aligned}
 \Phi(L_1)-\Phi(L_1-a)
   &=L_1a-\frac{a^2}{2}\\
   &\quad-C\{L_1\log L_1-(L_1-a)\log(L_1-a)\}\\
   &=L_1a-O(aL_2+a^2).                                           \tag{19}
\end{aligned}
\]

At the worst scale \(a=L_3+O(1)\), this is again
\(\Theta(L_1L_3)\). Thus an induced child meeting the target at size \(m\)
still needs a multiplier

\[
                         2^{\Theta(L_1L_3)}
                              =n^{\Theta(L_3)}.                   \tag{20}
\]

By comparison, the longest-run downshadow has only

\[
             2^k=\exp_2\!\left(\Theta(L_1/L_2)\right),
 \qquad {L_1\over L_2}=o(L_1L_3).                                \tag{21}
\]

So the exact Boolean run theorem is necessary for load control but cannot
close the fixed-gap deficit.

## 3. The surviving two-ended gate

Every induced child \(X_R\) has the exact endpoint decomposition

\[
                    V(X_R)-m=\sum_e C_eU_e,                       \tag{22}
\]

and hence some physical endpoint pair \(e\) has

\[
                         C_eU_e>{V(X_R)\over2m^2}.                 \tag{23}
\]

This is a genuine rooted two-ended module **inside** the child. It does not
by itself multiply \(V(X_R)\): the rectangles in (22) partition faces
already counted by \(V(X_R)\). To recover (20), one must attach a
near-full child coface family to at least
\(n^{\Theta(L_3)}\) recoverable one-sided outside contexts, or use a
separate reset/shield bank. Merely taking the larger of \(C_e,U_e\) loses
half of the child's quadratic logarithmic exponent and is unusable.

The exact pair-star pigeonhole retains almost the whole child coefficient:
some physical pair belongs to at least

\[
                    {V(X_R)-m-1\over\binom m2}                     \tag{24}
\]

ordinary child faces. But ambient attachment of that family is an
additional root/tangent predicate. It is not implied by (24), strong
separation, or a cyclic omitted gap.

There is nevertheless an exact one-sided sufficient condition. Let
\(\mathcal J_R\) be the pair-star family in (24), let \(\mathcal P\) be
any family of ordinary outside contexts on a disjoint marked ground, and
let

\[
 E=\{(F,S)\in\mathcal J_R\times\mathcal P:
                                  F\cup S\in\mathcal F(P)\}.       \tag{24a}
\]

The union itself recovers \(F\) and \(S\), so

\[
                              V(P)\ge |E|                           \tag{24b}
\]

with load one. No complete rectangle or semialgebraic thinning is needed.
If \(H_R=V(X_R)\ge2^{\Phi(L_1-a)}\), this closes the target whenever

\[
 |E|\ge2^{\Phi(L_1)},\quad\text{in particular whenever}\quad
 { |E|\over|\mathcal J_R||\mathcal P|}\,|\mathcal P|
       \ge \binom m2\,2^{\Phi(L_1)-\Phi(L_1-a)+O(1)}.              \tag{24c}
\]

At the extremal run scale, the right side is
\(n^{\Theta(L_3)}\); the factor \(m^2\) only adds \(O(L_1)\) to its
logarithm. Thus the long-run problem is an incidence lower bound, not a
biclique problem. The obstruction below shows that one directional
incidence graph can still be empty.

## 4. Sharp planar attachment barrier

The construction in `ALMOST_FULL_WORD_MIXED_BANK_BARRIER.md` uses two
parabolic macro arcs and a central arbitrary child coface family
\(\mathcal J\) containing a fixed pair \(o,p\). Coordinates can be chosen
so that

\[
                 p\in\operatorname{int}\triangle(o,a,b)           \tag{25}
\]

for every macro label \(a\) on the left arc and \(b\) on the right arc.
The two arcs need not have equal length. Take the left arc to have
\(\Theta(L_1/L_2)\) roles and the right arc to contain the remaining
\(\Theta(L_1)\) roles.

Then every union of \(F\in\mathcal J\), one nonempty left-run trace, and
one retained right label is nonconvex by the same fixed \(1+3\) circuit
(25). The left run has the exact physical size (16), yet no nonempty face
from it can be spliced through the central child to the opposite side.
All inequalities are open and rationally realizable, and the order type of
the central child is arbitrary.

This kills the statement

\[
 \text{long induced run + arbitrary child faces}
       \Longrightarrow\text{two-ended ambient product}.           \tag{26}
\]

It does not give a sub-half construction. Deleting the whole left arc
exposes a one-sided composition bank, and other directional child profiles
may pay. The positive residual is therefore exact: prove a one-sided
profile/reset bank of size (20), or globally charge the repeated circuit
(25). No arbitrary-child cyclic endpoint factorization may be used.

## 5. Verification

Run

~~~text
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_recoverable_carrier_coarsening_mask_run_gate.py
~~~

The verifier exhausts cyclic masks through length twelve, checks the
run/gap identity, the \(g/3\) vertex-disjoint gap extraction, and the
longest-run bound. It checks the three-log scale arithmetic and rooted
module threshold numerically, then invokes the exact rational rooted-ear
audit and the finite central-pair attachment obstruction. The unequal-arc
extension uses the same open containment inequalities proved in Section 4.
