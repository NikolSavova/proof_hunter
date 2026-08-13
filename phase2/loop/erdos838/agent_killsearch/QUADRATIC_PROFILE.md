# Erdős 838: quadratic-profile attack and comparison counterexample

**Date:** 2026-08-13. All logarithms in this note are base \(2\). The
nonempty cap, cup, and convex-subset counts are denoted by \(C,U,W\). This
note concerns the exact strong-glue recurrences

\[
\begin{aligned}
C(A\prec B)&=C(B)+(|B|+1)C(A),\\
U(A\prec B)&=U(A)+(|A|+1)U(B),\\
W(A\prec B)&=W(A)+W(B)+C(A)U(B).
\end{aligned}                                                    \tag{1}
\]

The reproducible artifact is
[quadratic_profile_attack.py](/Users/sihaohuang/Desktop/Coding/proof_hunter/phase2/loop/erdos838/agent_killsearch/quadratic_profile_attack.py).
Run it from the repository root with

```bash
python3 phase2/loop/erdos838/agent_killsearch/quadratic_profile_attack.py
```

Every displayed state is generated using exact Python-integer evaluations of
(1). Floating point is used only to rank search states; the reported local
witness is reevaluated with 80-digit `Decimal` arithmetic.

## Bottom line

The candidate profile

\[
\Psi(T)=\log W(T)-\kappa
 \frac{(\log C(T)-\log U(T))^2}{\log C(T)+\log U(T)},
\qquad \kappa=\frac1{2\ln 2},                         \tag{2}
\]

has **not** been disproved. Exhaustive enumeration of every distinct exact
\((C,U,W)\) state through 13 leaves, a deterministic exact-integer recursive
beam through 1000 leaves, and homogeneous/nonstationary Pascal-template
analysis all survive

\[
\Psi(T)\stackrel{?}{\ge}\frac12(\log |T|)^2.          \tag{3}
\]

However, two natural routes to (3) are decisively false:

1. There is no universal polynomial, \(n^{O(\log\log n)}\), or even
   \(n^{o(\log n)}\) upper bound on \(CU/W\). An explicit family has
   \(\log(CU/W)=(13/70+o(1))(\log n)^2\).
2. The scalar inherited-margin induction
   \(F(A\prec B)\ge\min(F(A),F(B))\), where
   \(F(T)=\Psi(T)-\tfrac12(\log|T|)^2\), fails by more than 5.46 bits on an
   exact valid 893-leaf tree.

Thus (3), if true, needs a genuinely amortized/profile argument rather than
either a global \(CU/W\) comparison or monotonicity of one scalar margin.

## 1. A quadratic lower bound on \(\log(CU/W)\)

Let \(S\) be the first \(2^{35}\) leaves, in leaf order, of the Pascal cell
\(T_{41,27}\), with the unused suffix deleted and unary nodes suppressed.
Its cap and cup substitution degrees are exactly

\[
(p,q)=(27,14).                                      \tag{4}
\]

The artifact certifies (4) with the compressed exact prefix recursion. Let
\(X_t\) be the \(t\)-fold homogeneous leaf substitution of \(S\), starting
from a singleton, and write \(N=|X_t|=2^{35t}\). Standard leading-degree
unrolling of (1) gives

\[
\begin{aligned}
\log C(X_t)&=\frac{27}{70}(\log N)^2+O(\log N),\\
\log U(X_t)&=\frac{14}{70}(\log N)^2+O(\log N),\\
\log W(X_t)&=\frac{41}{70}(\log N)^2+O(\log N).
\end{aligned}                                      \tag{5}
\]

Let \(\overline{X_t}\) be the mirror tree, interchanging caps and cups, and
put

\[
Y_t=\overline{X_t}\prec X_t,qquad n=|Y_t|=2N.       \tag{6}
\]

Equation (1) gives the exact identities

\[
C(Y_t)=U(Y_t)=C(X_t)+(N+1)U(X_t),
\qquad W(Y_t)=2W(X_t)+U(X_t)^2.                      \tag{7}
\]

Using (5) in (7), the linear factor \(N+1\) is lower order on the quadratic
scale, so

\[
\begin{aligned}
\log C(Y_t)=\log U(Y_t)
  &=\left(\frac{27}{70}+o(1)\right)(\log n)^2,\\
\log W(Y_t)&=\left(\frac{41}{70}+o(1)\right)(\log n)^2.
\end{aligned}
\]

Consequently

\[
\boxed{
\log\frac{C(Y_t)U(Y_t)}{W(Y_t)}
=\left(\frac{13}{70}+o(1)\right)(\log n)^2.}         \tag{8}
\]

The script evaluates (7) exactly through \(t=20\). At \(t=20\), where
\(\log n=701\), the normalized ratio in (8) is \(0.190972\ldots\), tending
to \(13/70=0.185714\ldots\). This refutes all proposed comparisons
\(CU/W\le n^{O(1)}\), \(CU/W\le n^{O(\log\log n)}\), and
\(CU/W\le n^{o(\log n)}\).

This example does **not** refute (3): because \(C(Y_t)=U(Y_t)\), its penalty
vanishes and \(\log W(Y_t)/(\log n)^2\to41/70>1/2\).

## 2. Why \(\kappa=1/(2\ln2)\) is forced

For homogeneous iteration of a full Pascal cell \(T_{m,i}\), put
\(x=i/m\) and let \(m\to\infty\). Binary entropy \(h_2\) gives

\[
\frac{\Psi_\kappa}{(\log n)^2}
=\frac{1-\kappa(2x-1)^2}{2h_2(x)}.                  \tag{9}
\]

For (9) to be at least \(1/2\) for every bias \(x\), necessarily

\[
\kappa\le
\frac{1-h_2(x)}{(2x-1)^2}.                         \tag{10}
\]

The infimum of the right-hand side is

\[
\kappa_* =\frac1{2\ln2}=0.721347520444\ldots,       \tag{11}
\]

approached as \(x\to1/2\). Conversely, the binary-entropy form of Pinsker's
inequality

\[
h_2(x)\le1-\frac{(2x-1)^2}{2\ln2}                  \tag{12}
\]

shows that \(\kappa_*\) makes (9) at least \(1/2\) for every \(x\). Hence
(11) is the **largest possible universal penalty coefficient even within
homogeneous Pascal templates**, while the critical coefficient survives all
of them at leading order.

There is also a leading-scale extension to nonstationary homogeneous
template schedules with no macroscopic one-level jump. At level \(j\), let
\(\ell_j\) be the log-size increment, \(L_{j-1}\) the accumulated log-size,
\(s_j=p_j+q_j\), and \(d_j=p_j-q_j\). Entropy/Pinsker yields

\[
s_j-\kappa_*\frac{d_j^2}{s_j}\ge \ell_j-o(\ell_j),  \tag{13}
\]

and weighted Cauchy gives

\[
\frac{\left(\sum_j d_jL_{j-1}\right)^2}
     {\sum_j s_jL_{j-1}}
\le \sum_j\frac{d_j^2}{s_j}L_{j-1}.                \tag{14}
\]

Combining (13)--(14) leaves
\(\sum_j\ell_jL_{j-1}=\tfrac12L^2-o(L^2)\). This is not an exact proof of
(3): macroscopic jumps and lower-order terms are precisely where a local or
finite-scale argument is still needed.

## 3. Exact finite search

Exhaustively enumerating all distinct exact triples through 13 leaves found
no violation of (3). The minimum values of
\(F=\Psi-\tfrac12(\log n)^2\) were

\[
F_{\min}(2)=1.084962501\ldots,qquad
F_{\min}(13)=2.699448715\ldots,                    \tag{15}
\]

with positive values at every intermediate size. There are 202,969 distinct
states at 13 leaves.

A deterministic beam retaining low-margin states and coarse imbalance bins
also found no violation through 1000 leaves. The smallest retained margin at
1000 leaves was \(15.993875300\ldots\). This second result is heuristic only:
beam retention does not certify all states.

For a generalized coefficient \(\kappa\), exhaustive small states impose
only weak ceilings: the running ceiling through 13 leaves is
\(2.848027164\ldots\), far above (11). Thus the sharp obstruction to a larger
coefficient is asymptotic and near-central, not a small tree.

## 4. The natural scalar induction fails exactly

Set

\[
F(T)=\Psi(T)-\frac12(\log|T|)^2.                   \tag{16}
\]

The tempting Bellman lemma

\[
F(A\prec B)\stackrel{?}{\ge}\min\{F(A),F(B)\}       \tag{17}
\]

holds exhaustively through 13 leaves but is false. A deterministic recursive
beam produces valid exact subtrees of sizes \(a=515\) and \(b=378\) with

```text
A: C=278088873137502
   U=88272696090590218
   W=369399013621622451658622880

B: C=3360930061559256384
   U=1224756619015
   W=114026966966178909384382679
```

Applying (1) gives the 893-leaf parent exactly:

```text
A≺B: C=3466325744478369642
     U=88904670506001958
     W=824017168637379565765806089
```

At 80-decimal precision,

\[
\begin{aligned}
F(A)&=47.201674829942387879187867466\ldots,\\
F(B)&=46.658881560321568032887810129\ldots,\\
F(A\prec B)&=41.197236719941631485214552161\ldots.
\end{aligned}
\]

Therefore

\[
F(A\prec B)-\min(F(A),F(B))
=-5.461644840379936547673257968\ldots.              \tag{18}
\]

The artifact regenerates the exact triples from leaves and asserts them, so
this is a certificate inside the valid recursive class rather than an
arbitrary numerical state.

An even more direct scalar recurrence also fails. If \(E(T)=2^{\Psi(T)}\),
one might hope for

\[
E(A\prec B)\ge (b+1)E(A)+(a+1)E(B).                \tag{19}
\]

At \(a=2,b=11\), take

\[
(C,U,W)_A=(3,3,3),\quad
(C,U,W)_B=(393,238,2047),\quad
(C,U,W)_{A\prec B}=(429,717,2764).
\]

Then the ratio of the left side of (19) to the right side is
\(0.4477798630\ldots\). Even the one-sided term
\(E(A\prec B)\ge(a+1)E(B)\) fails, with ratio
\(0.4504467991\ldots\).

## 5. What state an induction appears to need

The scalar \(F\) suppresses exactly the cap/cup information that a later
anti-aligned merge can spend. The smallest natural Markovian lift retains

\[
S=\log(CU),\qquad \Delta=\log(C/U)                  \tag{20}
\]

along with \(W\) (or \(\Psi\)). Equivalently, retain the separate coordinates
\((\log C,\log U,\log W)\). Here \(S\) records radial cap/cup mass and the
signed \(\Delta\) records which orientation can participate in the cross term
\(C(A)U(B)\). Size must of course also be retained for the multiplicative
factors in (1).

This is a statement about the minimal **natural continuous/algebraic** state,
not a set-theoretic impossibility theorem about encoding several reals into
one. The exact 893-leaf witness proves that the one-dimensional margin alone
does not have the needed Bellman property. A plausible next proof route is a
two-dimensional attainable-region/profile induction in \((S,\Delta)\), with
the loss in (18) charged against stored radial mass, rather than another
scalar local inequality.
