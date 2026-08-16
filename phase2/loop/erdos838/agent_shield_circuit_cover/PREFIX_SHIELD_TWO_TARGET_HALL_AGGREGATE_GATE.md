# Prefix shields: exact two-target Hall aggregate and half-scale barrier

**Date:** 2026-08-15. All logarithms are base two. This continues
`FIXED_ENDPOINT_PREFIX_PEELING_COMPANION_OR_SHIELD.md` and keeps
every conditional-mass and decoder-load factor.

## Verdict

The erased cap tail has an exact weighted two-target routing. At a trie node
of depth \(j\), expand each actual record by every subset of its common cap
prefix. If the node has total record weight \(W_j\), the expanded weight is

\[
                              E_j=2^jW_j.                          \tag{1}
\]

Every expanded record has the two actual ordinary targets

\[
                       A=C,\qquad F=B\cup U\cup S,\quad S\subseteq K_j.
                                                                    \tag{2}
\]

Let \(\eta_j\) be the exact fractional two-target Hall density, let
\(\lambda_j\) be the maximum weighted load of one shield target \(F\), and
let \(\delta_j\) be the maximum weighted load of one ordered pair \((A,F)\).
Then

\[
 \boxed{\displaystyle
 2^jW_j\le
   \min\{\eta_jV(P),\ \lambda_jV(P),\ \delta_jV(P)^2\}.}           \tag{3}
\]

There is also the ordinary-source marginal

\[
                              W_j\le\kappa_jV(P),                  \tag{4}
\]

where \(\kappa_j\) is the maximum record weight over one actual cap source.

Summing along one nested maximum-child path is equally exact. Put

\[
 E_\Sigma=\sum_{j<s}2^jW_j,\qquad
 \alpha_j=W_j/W_0,\qquad
 \mathfrak B=\sum_{j<s}2^j\alpha_j.                               \tag{5}
\]

Using aggregate target and pair loads \(\eta_\Sigma,\lambda_\Sigma,
\delta_\Sigma\),

\[
 \boxed{\displaystyle
 W_0\mathfrak B\le
 \min\{\eta_\Sigma V,\lambda_\Sigma V,\delta_\Sigma V^2\}.}       \tag{6}
\]

If the parent normalization gives \(W_0\ge\rho V^2\), then necessarily

\[
 \eta_\Sigma,\lambda_\Sigma\ge\rho V\mathfrak B,\qquad
 \delta_\Sigma\ge\rho\mathfrak B.                                \tag{7}
\]

Thus prefix shields close only if \(\mathfrak B\) beats the actual
description/pair load. The minimizer upper bound by itself does not force
this.

There is a sharp rank-\(O(\log n)\), coefficient-half source regression.
Take \(a=\lfloor\log n\rfloor\) ordered cap roles of size \(2\), followed
by \(b=\lfloor(\log n)/2\rfloor\) roles of common size
\(D=(1+o(1))n/b\), and choose one label per role. Then

\[
\begin{aligned}
 H&=2^aD^b
   =2^{\frac12(\log n)^2-\frac12(\log n)\log\log n+O(\log n)},\\
 R&=a+b+2=(3/2+o(1))\log n.                                     \tag{8}
\end{aligned}
\]

For uniform context degree, the maximum-child path has

\[
 \alpha_j=
 \begin{cases}
 2^{-j},&0\le j\le a,\\
 2^{-a}D^{-k},&j=a+k,
 \end{cases}
\qquad
 h_j=
 \begin{cases}
 2,&j<a,\\
 D,&j\ge a.
 \end{cases}                                                     \tag{9}
\]

Consequently

\[
 \boxed{\displaystyle
 \max_j\alpha_jh_j\le2,\qquad
 \mathfrak B
 =a+\sum_{k=0}^{b-1}(2/D)^k=O(\log n).}                          \tag{10}
\]

So neither the conditioned endpoint branching nor the aggregate rooted
shield supplies a quasipolynomial multiplier, despite half-scale source
entropy and rank \(O(\log n)\). This role product is rationally stretchable:
use strongly separated infinitesimal children on a concave macro chain.
Every transversal is a fixed-endpoint cap and every prefix subset is an
ordinary rooted shield.

This is an exact **source-mass/interface barrier**, not a completed
sub-half construction. Convex large role clouds pay by Boolean shields;
arbitrary low-face role children bring back precisely the coherent-ramp
profile-composition problem. What (10) proves is that parent minimality,
rank, trie entropy, and near-uniform conditional record mass cannot alone
make (6) large. A closure must bound \(\delta_\Sigma\) below the desired
scale, or turn a high pair/Hall load into a new mixed-profile bank.

## 1. Weighted two-target theorem

Fix a node with common prefix \(K_j\). Let \(\Omega_j\) be its weighted
actual records

\[
                         \omega=(B_\omega,C_\omega,U_\omega),
 \qquad \sum_{\omega\in\Omega_j}w_\omega=W_j.                    \tag{11}
\]

For every \(S\subseteq K_j\), make one expanded record
\(e=(\omega,S)\) of weight \(w_\omega\), and give it the targets (2).
The source \(A_e=C_\omega\) is ordinary. The shield target is ordinary
because

\[
 B_\omega\cup U_\omega\cup S
 \subseteq B_\omega\cup U_\omega\cup C_\omega,                   \tag{12}
\]

and the right side is the certified parent face for the record.

Define, with duplicate actual targets identified,

\[
 \eta_j=
 \max_{\varnothing\ne\mathcal E'\subseteq\mathcal E_j}
 \frac{\sum_{e\in\mathcal E'}w_e}
 {|\bigcup_{e\in\mathcal E'}\{A_e,F_e\}|}.                       \tag{13}
\]

The record-to-target max-flow/min-cut theorem routes all expanded weight
with maximum face load exactly \(\eta_j\). Summing the load over at most
\(V(P)\) actual faces gives the first term in (3).

The other terms are direct. Define

\[
\begin{aligned}
 \lambda_j&=\max_F\sum_{e:F_e=F}w_e,\\
 \delta_j&=\max_{A,F}\sum_{e:(A_e,F_e)=(A,F)}w_e,\\
 \kappa_j&=\max_A\sum_{\omega:C_\omega=A}w_\omega.                \tag{14}
\end{aligned}
\]

Grouping expanded records by \(F\) gives \(E_j\le\lambda_jV\).
Grouping by ordered target pairs gives at most \(V^2\) groups and proves
\(E_j\le\delta_jV^2\). Grouping the unexpanded records by their actual
source proves (4). This proves (3)--(4).

For all depths at once, take the disjoint formal union of the expanded
record sets but the **actual union** of their target faces. Define
\(\eta_\Sigma,\lambda_\Sigma,\delta_\Sigma\) by (13)--(14) on this
aggregate. The same proof gives (6).

If child, context, and prefix supports are role-separated, the pair
\((A,F)\) recovers

\[
 C=A,\qquad S=(A\cap F)\setminus e,\qquad
 B\cup U=F\setminus S,                                           \tag{15}
\]

where the fixed endpoint pair \(e=C\cap U\) is already part of the node
state. When the fixed roles split \(B\) from \(U\), only the
chronology/history mark remains. A pair can occur at several depths because the same
\(S\) may be contained in several nested prefixes, but at most \(R\)
depths are possible. Hence, if the residual actual-history load is
\(\delta_{\rm hist}\),

\[
                         \delta_\Sigma\le R\delta_{\rm hist}.     \tag{16}
\]

Equation (16) is the desired positive decoder. It is useful only when
\(\mathfrak B\) in (5) exceeds this true history load after the parent
normalization. The product regression below shows that trie entropy does
not force such an excess.

## 2. Dense-core alternative

If \(\eta_\Sigma>K\), weighted pruning leaves a nonempty two-target core in
which every actual source or shield target has incident expanded weight
greater than \(K\). This is the standard exact Hall-core conclusion.

If additionally every ordered pair has weight at most \(\delta_\Sigma\),
each target in the core has more than \(K/\delta_\Sigma\) distinct opposite
face neighbors. Thus the high branch is a dense graph of **actual cap
sources** \(C\) and **actual rooted shield faces** \(B\cup U\cup S\).
It is not a graph of chronology names.

This is the strongest unconditional promotion of high aggregate load. A
dense face-by-face graph does not automatically provide a physical point
alphabet; the anti-aligned face-core regression in
`agent_outer_internal_product/RELEASED_FACE_HALL_LABEL_PRIMITIVE_GATE.md`
applies verbatim.

## 3. Relation to trie branching

Let \(m_j\) be the number of distinct cap tails at node \(j\), and
\(h_j=m_j/m_{j+1}\) the unweighted maximum-child ratio. Let \(d(C)\) be
the total context/history weight of one cap source. Then

\[
                         W_j=\sum_{C\in\mathcal A_j}d(C).          \tag{17}
\]

If degrees are \(\Theta\)-near-uniform on the root trie,

\[
 \Theta^{-1}\frac{m_j}{m_0}
 \le\alpha_j
 \le\Theta\frac{m_j}{m_0}.                                      \tag{18}
\]

Thus the true mass-adjusted endpoint gain is

\[
                         \alpha_j\min\{M,h_j\},                   \tag{19}
\]

not merely \(h_j\), and the true shield expansion is \(2^j\alpha_j\).
The factors in (19) and (5) are exactly those lost by conditioning.

Without near-uniform degrees, one must run the maximum-child descent using
the record masses \(W_j\). Its ratios telescope \(W_0/W_s\), but they do
not count distinct endpoint faces. Converting weighted branching to
physical endpoints costs the maximum cap load \(\kappa_j\). This is another
actual decoder load, not free entropy.

## 4. Half-scale ordered-role regression

Let \(N=2^L\), put

\[
 a=L,\qquad b=\lfloor L/2\rfloor,\qquad
 D=\left\lfloor\frac{N-2a-2}{b}\right\rfloor.                    \tag{20}
\]

For large \(L\), \(D\ge3\). Take \(a+b\) ordered internal roles:

\[
 |X_i|=2\quad(i<a),\qquad |X_i|=D\quad(a\le i<a+b).               \tag{21}
\]

Add fixed endpoints \(u,v\), and let \(\mathcal C\) contain every cap word
\[
                         \{u,v\}\cup\{x_i:x_i\in X_i\}.            \tag{22}
\]

Then (8) follows directly from

\[
 \log H=a+b\log D,\qquad
 \log D=L-\log b+O(1).                                           \tag{23}
\]

The maximum child in every role has exactly the reciprocal fraction of the
role size, proving (9). At a binary depth,

\[
                         2^j\alpha_j=1,\qquad
                         \alpha_jh_j=2^{1-j}\le2.                 \tag{24}
\]

At large-role depth \(j=a+k\),

\[
 2^j\alpha_j=(2/D)^k,\qquad
 \alpha_jh_j=2^{-a}D^{1-k}\le1.                                  \tag{25}
\]

Summing (24)--(25) proves (10).

For a rational planar realization, put \(a+b+2\) macro points on a strict
concave parabola and replace each internal macro point by a sufficiently
small rational child in its own disjoint neighborhood. Standard
lexicographic composition makes every one-point-per-role transversal have
the macro cap order type. The construction is open, so the children may
have arbitrary prescribed rational order types. The prefixes in (22) are
literal cap chains, and (12)--(14) are genuine planar hereditary outputs
whenever the stated external contexts are present.

The regression has the exact rank and selected-source entropy of a live
half-scale slice. It deliberately does not assert an upper bound on the
full ambient \(V(P)\). If a large child is convex, its Boolean complex pays;
if arbitrary induction-minimal children are inserted, controlling their
cross-role cap/cup profiles is the original coherent-ramp gate. Therefore
this construction is a sharp no-go for a **pure aggregate-Hall/trie**
closure, not a counterexample to the target theorem.

The endpoint-surplus upper does not remove the scalar regression. Use the
single opposite cup \(U=\{u,v\}\). Every selected cap word in (22) is its
own ordinary cap--cup union, so the selected fixed-pair module has

\[
                         C_e=H,\qquad U_e=1,\qquad H_e=H.          \tag{25a}
\]

Its module surplus is exactly one (and allowing all universal pairs changes
this only polynomially). Thus a low \(C_eU_e/H_e\) hypothesis is compatible
with (9)--(10); the missing information is still the external-context/pair
load.

## 5. What parent minimality does and does not give

Assume the live record entrance has

\[
                         W_0\ge\rho V(P)^2.                       \tag{26}
\]

Equations (6)--(7) show exactly what follows:

* if \(\delta_\Sigma=o(\rho\mathfrak B)\), the ordered-pair bank
  contradicts (26);
* if \(\eta_\Sigma=o(\rho V\mathfrak B)\), fractional Hall contradicts
  (26); and
* otherwise a dense actual source-by-shield-face core remains.

There is no further conclusion from \(V(P)\) being minimal or from the
endpoint surplus bound alone. In the role regression,
\(\mathfrak B=O(\log n)\), so even a polynomial history load can absorb the
whole aggregate. At the coefficient target, the known description losses
are \(2^{O((\log n)\log\log n)}\), much larger still.

The endpoint branch (19) also stays constant in the regression. Hence
combining the maximum-child path, the source target, and all rooted prefix
shields does not recover the missing quasipolynomial multiplier.

The exact residual is now one of the following genuinely geometric inputs:

1. prove \(\delta_\Sigma\) is much smaller than its current description
   bound by decoding the parent/context from \((C,F)\);
2. turn the dense source--shield core into a mixed-profile/circuit bank; or
3. exploit the internal face complexes of the \(D\)-point large roles.

Option 3 is the strictly internal coherent-ramp child gate already isolated
before this prefix descent.

## 6. Verification

Run

    python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_prefix_shield_two_target_hall_aggregate_gate.py

The exact verifier:

1. exhausts a small weighted two-target system and checks the Hall,
   marginal, pair, and source inequalities;
2. checks the aggregate depth decoder and its at-most-\(R\) collision;
3. verifies (9)--(10) for finite product-role systems; and
4. checks exact half-scale entropy/rank/support inequalities through
   \(L=18\), plus a rational cap-role realization.

Expected output:

    PASS: prefix-shield Hall aggregate; hall=(8, 6, 4/3, 4, 2, 1), depth=(24, 72, 3), role=(6, 3, 16, 457/64, 2), geometry=(3, 2, 5, 200)
