# Disjoint source traces: exact global charge, four-cover lift, and the live-scale barrier

**Date:** 2026-08-15. All logarithms are base two. The empty face is
included. This continues
HIGH_RANK_FIXED_EDGE_CIRCUIT_DELETION_MATCHING_GATE.md.

## Verdict

The new low-cover versus matching theorem has an exact global
source-history charge, but the charge is only absolute. Let a weighted
record \(\omega\) have an ordinary source \(A_\omega\) and \(s\)
pairwise disjoint nonempty source traces

\[
                  T_{\omega,1},\ldots,T_{\omega,s},
                  \qquad |T_{\omega,i}|\le3.                    \tag{1}
\]

Every union-of-traces deletion is an ordinary source downface. If the total
weight of records over any one actual source is at most \(\rho\), then

\[
 \boxed{\displaystyle
 2^s\sum_\omega w_\omega
       \le \rho\,S_{3s}(n)\,V(P),\qquad
 S_j(n)=\sum_{i=0}^j\binom ni.}                                \tag{2}
\]

The decoder is literal: from the output, guess the at most \(3s\) deleted
physical labels and recover the source. This is the strongest universal
middle-shadow statement available from the matching alone.

It does not multiply the pocket alphabet. In a complete source by pocket
rectangle, \(\rho\) is the whole pocket degree, which cancels that factor
from (2). Even before the decoder, one matching uses at most \(3s\)
physical labels, so every bank which changes only matched labels has at
most

\[
                                  2^{3s}                         \tag{3}
\]

states per retained source word. At the live scale
\(s=\Theta(\Delta)\), \(\Delta=\Theta(\log\log n)\), this is only
\((\log n)^{O(1)}\); the required source--pocket multiplier has logarithm
\(\Theta(L\Delta)\), where \(L=\log n\). The missing factor \(L\) cannot
come from a more careful enumeration of the same trace support.

There is one exact positive support branch. If many completion traces over
a common retained face \(B\) **four-cover** their union support \(Q\), then
planar four-locality makes \(B\cup Q\) ordinary and exposes the full
Boolean rooted bank \(2^{|Q|}\). Its global weighted output load is
explicit below. Quantitatively, this branch reaches
\(2^{\Theta(L\Delta)}\) only when the recoverably common support has
\(|Q|=\Theta(L\Delta)\). The matching itself supplies only
\(|Q|\le3s=O(\Delta)\).

The failure is geometrically real. In the exact central Pascal strong-glue
cell, both source and pocket alphabets have size
\(V(P)n^{-O(1)}\), every singleton source label is a circuit trace, and a
polynomial-loss subfamily shares one physical exposed edge. Nevertheless
every nonempty source downface is incompatible with every pocket face in
the selected nonprofile family. All toggle/downshadow outputs lie in the
one left-child face bank and are reused across the entire right-child
alphabet; only deleting the full source releases the pocket, with terminal
load equal to the source mass.

This Pascal regression is stretchable, rank \(O(L)\), canonically weighted,
and live-normalized in both alphabets. It has coefficient
\(1-1/(4\ln2)>1/2\), so it is not a low-\(V\) parent and does not refute a
minimizer-specific theorem. It proves that the parent fixed-gap upper bound
must enter through a new mutation/profile inequality. Matching,
common-edge deletion, middle shadows, and deletion-child lower bounds do
not themselves supply that inequality.

No half-coefficient closure is claimed.

## 1. Weighted matched-trace downshadow

Let \(\Omega\) be a multiset of weighted records. Record \(\omega\)
contains an ordinary face \(A_\omega\) and a canonical ordered family (1).
The family may depend on the pocket partner and history. Define the row
weight

\[
                \rho=\max_A\sum_{\omega:A_\omega=A}w_\omega.    \tag{4}
\]

For \(I\subseteq[s]\), output

\[
             W_{\omega,I}
                 =A_\omega\setminus\bigcup_{i\in I}T_{\omega,i}. \tag{5}
\]

Every output is ordinary by heredity. Disjoint nonempty traces make the
\(2^s\) outputs of one record distinct.

> **Theorem 1 (weighted matched-trace shadow).** Equation (2) holds.

**Proof.** Fix an output \(W\). If \(W=W_{\omega,I}\), then

\[
       A_\omega=W\cup G,\qquad
       G=A_\omega\setminus W,\qquad |G|\le3s.                   \tag{6}
\]

There are at most \(S_{3s}(n)\) choices for \(G\). Once \(A_\omega\) is
fixed, the total weight of all records over that source is at most
\(\rho\), and a fixed record produces \(W\) for at most one \(I\).
Therefore the weighted load of \(W\) is at most
\(\rho S_{3s}(n)\). The total output-incidence weight is
\(2^s\sum_\omega w_\omega\). Summing over ordinary outputs proves (2).
\(\square\)

There is an exact rank-refined middle-shadow form. If every source has
rank \(r\), write \(v_q(P)\) for the number of ordinary rank-\(q\) faces.
An output of rank \(q\) is extended back to a source by exactly
\(r-q\) labels outside it, so the preceding proof gives

\[
 \boxed{\displaystyle
 2^s\sum_\omega w_\omega
 \le \rho\sum_{q=r-3s}^{r}
              \binom{n-q}{r-q}v_q(P).}                         \tag{2a}
\]

Equation (2) follows by bounding every binomial coefficient by
\(S_{3s}(n)\) and the sum of the \(v_q\)'s by \(V(P)\). Thus no rank
averaging or middle-shadow mass is being discarded implicitly. At
\(r=O(L)\), \(s=\Theta(\Delta)\), the largest coefficient in (2a) still
has logarithm \(\Theta(L\Delta)\); improving the decoder requires an
actual restriction on source extension codegree.

If every source contains a common exposed edge \(e\), discard the at most
two matched traces meeting its endpoints. The same proof, with
\(s\) replaced by \(s-2\), gives outputs which all retain \(e\) and its
side. Thus the common edge preserves a chart but changes no scale in (2).

### Complete rectangles cancel the pocket degree

Let \(\mathcal A\times\mathcal H\) be a literal unweighted rectangle and
give every pair weight one. Then \(\rho=|\mathcal H|\), so (2) becomes

\[
             2^s|\mathcal A|
                   \le S_{3s}(n)V(P).                           \tag{7}
\]

The factor \(|\mathcal H|\) has cancelled exactly. Equivalently, normalize
every pair to weight \(1/|\mathcal H|\). Every source row then has weight
one, the total mass is \(|\mathcal A|\), and (7) is unchanged.

This is not an artifact of the coarse decoder. The output (5) contains no
pocket label, so all partners of one source may literally produce the same
downface.

## 2. A sharp information ceiling

Put

\[
                         U_\omega=\bigcup_{i=1}^sT_{\omega,i}.   \tag{8}
\]

Then \(|U_\omega|\le3s\). If an output is required to retain the source
outside \(U_\omega\) and may change only membership on \(U_\omega\), its
entire local state space is a subfamily of

\[
       \{(A_\omega\setminus U_\omega)\cup R:R\subseteq U_\omega\}.
                                                                    \tag{9}
\]

Hence (3) is an absolute upper bound, independent of planarity or the
choice of decoder. In particular, any product interpretation with local
alphabets \(d_1,\ldots,d_s\) satisfies

\[
             \prod_i(1+d_i)\le2^{3s}                            \tag{10}
\]

unless it imports labels outside the matched traces.

Suppose a live rectangle needs a multiplier \(2^{\sigma L\Delta}\) and
the matching theorem supplies \(s\le C\Delta\). Then

\[
       \log_2(2^{3s})\le3C\Delta=o(L\Delta).                    \tag{11}
\]

Thus a successful promotion must use cross-history variation to create
large trace alphabets. More precisely, if \(s\) recovered slots form a
complete product with alphabet sizes \(d_i\), reaching the target requires

\[
       {1\over s}\sum_i\log_2(1+d_i)
                    \ge {\sigma L\Delta\over s}
                    \ge {\sigma\over C}L.                       \tag{12}
\]

The geometric mean alphabet must be \(n^{\Omega(1)}\). A matching of
actual rank-three traces has alphabet at most eight per slot. A
first-divergence or semialgebraic theorem must prove that alternatives from
different source histories are mutually composable; the matching theorem
does not.

## 3. Exact four-cover union lift

There is a clean positive branch when high overlap really does organize a
common support.

> **Theorem 2 (rooted four-cover lift).** Let \(B\) be ordinary, let
> \(\mathcal U\) be a family of subsets of a disjoint ground \(Q\), and
> assume
> \[
>                         B\cup U\in\mathcal F(P)
>                         \quad(U\in\mathcal U).                 \tag{13}
> \]
> If every subset \(S\subseteq Q\) of rank at most four is contained in
> some \(U\in\mathcal U\), then \(B\cup Q\) is ordinary. Therefore
> \[
>                         B\cup R\in\mathcal F(P)
>                         \quad(R\subseteq Q),                  \tag{14}
> \]
> giving exactly \(2^{|Q|}\) rooted outputs.

**Proof.** If \(B\cup Q\) were bad, planar four-locality would give a bad
four-subset \(C\). It is not contained in \(B\). Put
\(S=C\cap Q\), so \(1\le|S|\le4\). Choose \(U\in\mathcal U\) containing
\(S\). Then \(C\subseteq B\cup U\), contradicting (13). This proves the
first assertion; (14) follows by heredity. \(\square\)

For weighted contexts \(c=(B_c,Q_c,\mathcal U_c)\) satisfying the theorem,
output all \(B_c\cup R\), \(R\subseteq Q_c\). If

\[
 \Lambda_4=\max_G
     \sum_{c,R:\,G=B_c\cup R}w_c,                               \tag{15}
\]

then exact double counting gives

\[
 \boxed{\displaystyle
       \sum_cw_c2^{|Q_c|}\le\Lambda_4V(P).}                     \tag{16}
\]

This is the desired global support charge whenever
\(|Q_c|\ge\sigma L\Delta+\log_2\Lambda_4+O(1)\). But applying Theorem 2
only to the union of one matching gives \(|Q_c|\le3s=O(\Delta)\), and
(16) reduces to the local ceiling (3).

If the four-cover condition fails, choose the first uncovered
\(S\subseteq Q\), \(1\le|S|\le4\). There are only \(S_4(n)\) physical
choices. Fixing \(S\) is therefore polynomial-loss localization, but it
does not make alternatives from different contexts composable. This is the
exact support-container residue.

## 4. An exact low-\(V\) scalar capacity model

The scalar parent bound alone does not contradict the two separate target
alphabets. Fix \(0<c<1/2\), \(0<\sigma<1\), let
\(\Delta=o(L)\), and define

\[
\begin{aligned}
 V_0&=2^{\lfloor cL^2\rfloor},\\
 H&=2^{\lfloor cL^2\rfloor-1},\\
 K&=2^{\lfloor\sigma L\Delta\rfloor},\qquad
 s=\lceil C\Delta\rceil.                                      \tag{17}
\end{aligned}
\]

For all sufficiently large \(L\),

\[
       H+K2^{3s}\le V_0,\qquad KH\ge V_0\,2^{\sigma L\Delta-2}. \tag{18}
\]

Thus a pocket alphabet of size \(H\), a source family with all trace-local
states \(K2^{3s}\), and a rectangle exceeding \(V_0\) by the required
quasipolynomial factor are numerically consistent with the same low-\(V\)
budget. Route every record to its pocket target with load \(K\), or to its
source target with load \(H\); both large loads are genuine.

This is an exact capacity obstruction, not a claim of planar
realizability. Producing a planar instance satisfying (17)--(18) with
\(c<1/2\) would itself amount to a sub-half construction. Its purpose is to
show that the scalar upper bound cannot close the Hall rectangle without a
new geometric relation between the two alphabets.

## 5. Stretchable Pascal calibration

The central Pascal strong-glue cell supplies that obstruction with full
planar geometry at the local live normalization. Write

\[
                         P=Y\prec Z.                            \tag{19}
\]

Let \(\mathcal D\) be the fixed-root, fixed-rank noncap source fibre and
let

\[
                         \mathcal H=\mathcal F(Z)\setminus
                                      \mathcal U(Z)             \tag{20}
\]

be the noncup pocket family from
CANONICAL_SOURCE_ROLE_DELETION_PASCAL_DENSITY_BARRIER.md. The exact
estimates there give

\[
              |\mathcal D|,\ |\mathcal H|
                    \ge V(P)\,|P|^{-O(1)},\qquad
              r:=|D|=\Omega(\log|P|).                           \tag{21}
\]

For every \(D\in\mathcal D\), \(U\in\mathcal H\), and \(y\in D\), the
union \(\{y\}\cup U\) is nonordinary. Four-locality gives a bad circuit
consisting of \(y\) and three labels of \(U\). Therefore every singleton
\(\{y\}\) is a source trace:

\[
                      \nu_Y(D,U)=\tau_Y(D,U)=r.                 \tag{22}
\]

Every source face has \(r\) exposed boundary edges. Pigeonholing a physical
oriented edge costs at most \(|P|^2\), so a subfamily of size
\(|\mathcal D|r/|P|^2\) shares one literal edge and side. After discarding
its two endpoints, (22) still gives \(r-2\) disjoint singleton traces
which preserve that edge.

Nevertheless the strong-glue classification says

\[
            A\cup U\notin\mathcal F(P)
       \quad\text{for every nonempty }A\in\mathcal F(Y),
                         \ U\in\mathcal H.                       \tag{23}
\]

Hence:

* all toggle/downshadow outputs from every \(D\) lie in the single bank
  \(\mathcal F(Y)\), of size \(V(Y)\);
* that bank is reused for every \(U\in\mathcal H\);
* only deleting the whole source releases \(U\); and
* the terminal output \(U\) has load equal to the total source weight.

The exact canonical row weights are at least \(1/2\) before normalization,
and the unordered role-colouring retains polynomial total mass. Every
deletion child still contains all of \(Z\), so all inherited scalar
lower bounds hold. This is strictly stronger than an abstract trace
complex.

Its limitation is equally exact:

\[
          \log V(P)=
          \left(1-{1\over4\ln2}+o(1)\right)(\log|P|)^2
                    >{1\over2}(\log|P|)^2.                      \tag{24}
\]

Thus the example cannot satisfy the parent fixed-gap upper bound. It rules
out a local support-charge theorem; it does not rule out a theorem saying
that a global minimizer cannot contain this stationary all-delete profile.
That minimizer/profile mutation is the remaining input.

## 6. Consequence for the live proof

The high-rank pocket lift and the low-cover theorem rigorously reach a hard
rectangle with \(s=\Omega(\Delta)\) disjoint source traces. The present
audit proves:

1. the matching gives a globally valid weighted source downshadow (2);
2. its pocket degree cancels exactly in a dense rectangle;
3. its entire physical support has exponentially too little entropy;
4. a common edge preserves the chart but not the pocket; and
5. only a recoverable four-cover core of size \(\Omega(L\Delta)\), or an
   equivalent cross-history alphabet/product theorem, supplies the missing
   scale.

The next theorem cannot merely sharpen \(3s\) to \(2s\), improve a
binomial decoder, or invoke low \(V\) as a scalar inequality. It must show
that repeated circuit traces from different high-rank sources assemble
into the large common support of Theorem 2, or that their stationary
all-delete profile admits a \(V\)-decreasing minimizer mutation.

## 7. Verification

Run:

    python3 agent_outer_internal_product/verify_disjoint_trace_global_support_charge_gate.py

The verifier:

1. exhausts weighted matched-trace shadows and checks the exact load in
   Theorem 1;
2. exhausts random finite four-cover complexes and verifies Theorem 2;
3. checks the scalar capacity inequalities (18) at five large scales;
4. reconstructs the exact rational \(T(6,3)\) Pascal cell, verifies every
   singleton source trace, localizes a common exposed edge, and exhausts
   every nonempty source downface against every selected pocket; and
5. checks that the terminal pocket load and the reuse of the left-child
   downshadow are literal.

It prints PASS.
