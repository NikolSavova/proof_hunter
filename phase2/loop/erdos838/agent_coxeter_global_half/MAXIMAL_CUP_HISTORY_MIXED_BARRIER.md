# A maximal weighted history blocks label-retaining mixed promotion

**Date:** 2026-08-15

## Verdict

There is an exact stretchable obstruction at the surviving local interface.
It applies to the full mixed \(C(A)\times U(B)\) banks, not only to the
homogeneous cup/cap banks of `WEIGHTED_ROOTED_HISTORY_HALL_BARRIER.md`.

Let

\[
 P_k=E(k,k),\qquad
 m=|P_k|=\binom{2k-4}{k-2},\qquad n=m+1.               \tag{1}
\]

The leftmost recursive subconfiguration \(E(k,3)\subset P_k\) is a strict
cup \(S_k\) of rank \(k-1\).  It is inclusion-maximal among **all** ordinary
convex faces of \(P_k\):

\[
 \boxed{F\in\mathcal V(P_k),\ S_k\subseteq F
        \quad\Longrightarrow\quad F=S_k.}              \tag{2}
\]

Add a coherent positive root \(p\).  Then

\[
 H_k=\{p\}\cup S_k                                     \tag{3}
\]

is a genuine temporal history of rank \(k\) and half-activity weight
\(2^{-k}\).  Consequently any fractional decoder which asks this history
to emit the required \(n2^{-k}\) units and preserves its original labels in
the ordinary output has only the single target \(S_k\).  Its load satisfies

\[
 \boxed{
 \Lambda\ge\frac{m+1}{2^k}
       \ge\frac{\sqrt m}{4\sqrt{2k-3}}
       =m^{1/2-o(1)}.}                                  \tag{4}
\]

This remains a fixed-power obstruction if an ordinary face is supplied
with \(k^{O(1)}\) trace or recursion marks: divide the right side of (4) by
the number of allowed marks.

Thus no local rule can force a compatible opposite-sign history while
retaining every label of an arbitrary coherent-root cup history.  On this
family one live history is already terminal.  Any successful global
argument must either

1. charge the terminal history directly to its unweighted face \(S_k\) by
   a mechanism that does not demand the factor \(n\) history-by-history;
2. pool or telescope demands before decoding; or
3. erase/replace labels while supplying an independently bounded recovery
   code.

The last alternative is outside label-retaining two-tangent amalgamation:
that theorem glues side histories and therefore preserves their vertices.

This is a barrier to a proposed decoder, not a counterexample to
\(H(P)=n^{o(1)}\).

## 1. The separated-composition rule

Use the classical strict high-left/low-right realization

\[
 E(r,s)=E(r,s-1)\prec E(r-1,s).                         \tag{5}
\]

Write the two children in (5) as \(A\prec B\).  Every convex face meeting
both children has the unique form

\[
 C\cup U,\qquad
 \varnothing\ne C\subseteq A\text{ a cap},\quad
 \varnothing\ne U\subseteq B\text{ a cup}.             \tag{6}
\]

Indeed, in a separated realization the selected vertices in the high-left
child must form the upper (cap) chain of the mixed polygon, while those in
the low-right child must form its lower (cup) chain.  Conversely those two
strict chains concatenate to a convex polygon.  The split recovers \(C,U\),
so (6) is both a characterization and a decoder.  It is the set-level
version of

\[
 V_{A\prec B}(t)=V_A(t)+V_B(t)+C_A(t)U_B(t).            \tag{7}
\]

## 2. The terminal cup

Inside \(E(k,k)\), follow the left child in (5) until reaching
\(E(k,3)\).  Since

\[
 |E(k,3)|=\binom{k-1}{k-2}=k-1,                        \tag{8}
\]

and this configuration has no \(k\)-cup but is built recursively as

\[
 E(k,3)=E(k,2)\prec E(k-1,3),                           \tag{9}
\]

all its points form a strict \((k-1)\)-cup.  Call this point set \(S_k\).

We prove (2) while climbing back up the left spine.  It is trivial inside
the base configuration \(E(k,3)=S_k\).  Suppose \(S_k\) is terminal in the
left child \(A=E(k,s-1)\) of \(E(k,s)=A\prec B\), where \(s\ge4\), and let
\(F\) be a convex face containing \(S_k\).  If \(F\) meets \(B\), (6) says
that \(F\cap A\) is a cap.  But \(F\cap A\) contains three points of the
strict cup \(S_k\), whose orientation is positive; no cap can contain that
triple.  Hence \(F\subseteq A\), and induction gives \(F=S_k\).

This proof uses every mixed bank at every separated-recursion node.  The
failure is not a shortage after scalar aggregation: the extension
neighbourhood of this particular history is exactly one face.

## 3. Temporal lift and load

Choose \(p\) to the left of \(P_k\) with

\[
 \chi(p,x,y)=+\qquad(x<y\text{ in }P_k).                \tag{10}
\]

The consecutive edges along \(p,S_k\) occur in increasing reflection time,
because the root comparisons have sign (10) and every consecutive triple
of \(S_k\) is positive.  Thus (3) is one of the rooted temporal histories
in the exact identity

\[
 Q_p(t)=tU_{k,k}(t).                                    \tag{11}
\]

A **label-retaining mixed decoder** sends flow from (3) only to ordinary
faces \(F\) with \(S_k\subseteq F\).  This is precisely the preservation
property of promotion by (6) or by two-tangent gluing.  By (2), all
\(n2^{-k}\) units emitted by (3) land on \(S_k\), proving the first bound in
(4).

Finally, the central-binomial average bound gives

\[
 m\ge\frac{2^{2k-4}}{2k-3},
 \qquad
 2^k\le4\sqrt{(2k-3)m}.                                \tag{12}
\]

Using \(m+1\ge m\) in (4) proves the second bound.

If outputs are pairs \((F,\tau)\) with at most \(M_k\) admissible marks for
one face, the same one-history Hall cut gives

\[
 \Lambda\ge\frac{m+1}{M_k2^k}.                         \tag{13}
\]

In particular, the at-most-rank trace multiplicity in rooted diagonal
amalgamation, or any polynomial number of recursive marks, leaves
\(m^{1/2-o(1)}\) load.

## 4. Exact scope

Equation (2) does **not** forbid an abstract label-erasing code which maps
\(H_k\) to unrelated faces and records enough information to reconstruct
\(S_k\).  Without a geometric compatibility condition, the enormous mixed
face alphabet of \(E(k,k)\) has ample scalar capacity.  Such a code would
need its own exact recovery relation and a global bound on how often that
relation reuses a face.  Merely invoking the mixed bank (6) does not provide
one.

The sharp surviving interface is therefore not “find more mixed faces.”
It is:

\[
 \boxed{\text{pool terminal-history demand, or construct a bounded-load
 label-replacing recovery code.}}                       \tag{14}
\]

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_coxeter_global_half/verify_maximal_cup_history_mixed_barrier.py
```

The checker constructs exact rational \(E(k,k)\) realizations for
\(4\le k\le6\), applies a sign-preserving generic perturbation, identifies
the leftmost \(E(k,3)\), and verifies that it is a strict cup and has no
one-point convex extension.  By deletion-heredity this proves exact
inclusion-maximality.  It then adds the coherent root, reconstructs the
adjacent-swap reduced word, checks the temporal path and rooted convex face,
and verifies (4), (8), and (12) symbolically through \(k=40\).
