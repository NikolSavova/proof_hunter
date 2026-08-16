# A fibre-one label-replacing mixed code for the Erdős--Szekeres fan

**Date:** 2026-08-15

## Verdict

The maximal-cup obstruction disappears completely on its primary test
family once label replacement is allowed with an explicit recovery code.
For every \(k\ge5\), the **top** mixed bank of \(E(k,k)\) alone supports a
fractional decoder for all coherent-root cup histories with output load at
most one and recovery fibre exactly one.

Put

\[
 P=E(k,k)=A\prec B,
 \quad A=E(k,k-1),\quad B=E(k-1,k),
 \quad m=|P|=\binom{2k-4}{k-2},\quad n=m+1.             \tag{1}
\]

Let \(\mathcal U(P)\) be the nonempty cups in \(P\).  After adding a
coherent positive root \(p\), the history indexed by \(S\in\mathcal U(P)\)
has half-activity weight \(2^{-(|S|+1)}\).  Assign it demand

\[
 d(S)=\frac{n}{2^{|S|+1}},
 \qquad q(S)=\lceil d(S)\rceil.                         \tag{2}
\]

The top mixed bank is

\[
 \mathcal M=
 \{C\cup U:\varnothing\ne C\subseteq A\text{ a cap},
              \ \varnothing\ne U\subseteq B\text{ a cup}\}.       \tag{3}
\]

Its split is unique.  The exact capacity theorem is

\[
 \boxed{|\mathcal M|\ge\sum_{S\in\mathcal U(P)}q(S)
        \qquad(k\ge5).}                                 \tag{4}
\]

Order the histories and mixed pairs lexicographically.  Give history \(S\)
the next block of \(q(S)\) unused pairs and send \(d(S)/q(S)\le1\) units to
each.  From an output face, the top split recovers its pair, its
lexicographic index recovers the unique block, and that block recovers
\(S\).  Therefore

\[
 \boxed{\text{output load}\le1,
        \qquad\text{recovery fibre}=1.}                 \tag{5}
\]

In particular, the terminal maximal cup \(S_k=E(k,3)\) from
`MAXIMAL_CUP_HISTORY_MIXED_BARRIER.md` receives
\(\lceil n/2^k\rceil\) distinct mixed codewords.  None need contain
\(S_k\); the block decoder recovers it exactly.  Thus \(E(k,k)\) is a sharp
barrier to label retention but **not** to label replacement.

This theorem solves the local coherent-root interface only for the
recursive Erdős--Szekeres family.  It does not supply a canonical code for
an arbitrary reflection order, nor does it bound reuse if independently
chosen endpoint codes share the same global mixed bank.  Those are the
remaining global issues.

## 1. Exact mixed capacity

Write \(U_{r,s}(t)\) and \(C_{r,s}(t)\) for the nonempty cup and cap
polynomials of \(E(r,s)\), and

\[
 N_{r,s}=|E(r,s)|=\binom{r+s-4}{r-2}.                  \tag{6}
\]

The separated recursion gives

\[
 U_{r,s}(t)=U_{r,s-1}(t)
       +(1+N_{r,s-1}t)U_{r-1,s}(t),                    \tag{7}
\]

with boundary value \(U_{2,s}(t)=U_{r,2}(t)=t\), and
\(C_{r,s}=U_{s,r}\) by reflection.  Hence, if

\[
 W_k=C_{k,k-1}(1)=U_{k-1,k}(1),                        \tag{8}
\]

then the two factors in (3) both have size \(W_k\), so

\[
 |\mathcal M|=W_k^2.                                   \tag{9}
\]

Ceiling each history demand separately.  Equations (2) and the exact
rooted-fan identity \(Q_p(t)=tU_{k,k}(t)\) give

\[
 \begin{aligned}
 T_k:=\sum_Sq(S)
 &\le \sum_S(d(S)+1)\\
 &=\frac{m+1}{2}U_{k,k}(1/2)+U_{k,k}(1).               \tag{10}
 \end{aligned}
\]

Thus (4) follows from

\[
 W_k^2\ge
 \frac{m+1}{2}U_{k,k}(1/2)+U_{k,k}(1).                 \tag{11}
\]

The exact recurrence (7) verifies (11) for \(5\le k\le15\).  The margin
quickly becomes enormous:

\[
\begin{array}{c|r|r}
k&m&W_k^2/\bigl((m+1)U(1/2)/2+U(1)\bigr)\\ \hline
5&20&3.44436\\
6&70&58.8298\\
8&924&1.31046\cdot10^6\\
10&12870&1.65686\cdot10^{13}\\
12&184756&1.57382\cdot10^{23}\\
15&10400600&4.82931\cdot10^{43}
\end{array}                                             \tag{12}
\]

Here the displayed decimals are informational; the verifier compares the
integers and rationals in (11) exactly.

## 2. A uniform proof from \(k=16\) onward

At activity one, expand (7) down its recursion tree.  There are fewer than
\(4^k\) root-to-boundary paths.  Along any path, the factor associated with
decreasing the first parameter from \(r\) is at most
\(1+N_{r,k-1}\).  On the other hand, one particular path in
\(U_{k-1,k}(1)\) decreases the first parameter at every step.  Therefore

\[
 \begin{aligned}
 U_{k,k}(1)
 &\le4^k\prod_{r=3}^{k}(1+N_{r,k-1})\\
 &\le4^k W_k(1+m/2)
 \le4^k mW_k.                                          \tag{13}
 \end{aligned}
\]

The middle inequality uses
\(W_k\ge\prod_{r=3}^{k-1}(1+N_{r,k-1})\) and
\(N_{k,k-1}=m/2\).

Since \(U(1/2)\le U(1)\) and \(m\ge6\), (10) and (13) imply

\[
 T_k\le3\cdot4^{k-1}m^2W_k.                            \tag{14}
\]

For \(3\le r\le k-1\),

\[
 N_{r,k-1}=\binom{r+k-5}{r-2}
 \ge\binom{2r-4}{r-2}\ge2^{r-2}.                      \tag{15}
\]

Taking the same single path as above gives

\[
 W_k\ge2^{(k-3)(k-2)/2}.                               \tag{16}
\]

Also \(m\le2^{2k-4}\).  For \(k\ge16\),

\[
 \frac{(k-3)(k-2)}2\ge6k-8,
\]

and hence

\[
 W_k\ge2^{6k-8}
 \ge3\cdot4^{k-1}m^2.                                 \tag{17}
\]

Equations (14) and (17) prove \(T_k\le W_k^2\), completing
the proof of (4) for every \(k\ge5\).

## 3. Exact recovery, including the terminal history

Fix the inherited label order.  Lexicographically order:

1. all nonempty cups \(S\subseteq P\);
2. all nonempty caps \(C\subseteq A\); and
3. all nonempty cups \(U\subseteq B\).

Order \(\mathcal M\) by the product order on \((C,U)\).  Equation (4)
allows consecutive, pairwise-disjoint blocks

\[
 I_S\subseteq\mathcal M,
 \qquad |I_S|=q(S).                                    \tag{18}
\]

For every \(F=C\cup U\in I_S\), put flow \(d(S)/q(S)\) on \(S\to F\).
Every history emits exactly its demand, and every output receives flow from
exactly one history and load at most one.

Recovery uses no per-output auxiliary mark.  The known top division
\(P=A\prec B\) gives

\[
 C=F\cap A,
 \qquad U=F\cap B.                                     \tag{19}
\]

The pair's product-order index determines its unique interval in (18), and
therefore determines \(S\).  The fixed root \(p\) then reconstructs the
original temporal history \(\{p\}\cup S\).  This is an exact fibre-one
label-replacing decoder.

For \(S=S_k\), equation (2) says \(q(S_k)=\lceil n/2^k\rceil\).  Although
no proper ordinary face contains \(S_k\), (18)--(19) give that many distinct
recoverable mixed outputs.  This explicitly passes the maximal-cup kill
test.

## 4. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_coxeter_global_half/verify_label_replacing_es_mixed_code.py
```

The checker computes the full cup coefficient vectors and all scalar
profiles by exact integer/rational recurrence through \(k=40\), verifies
(4), (10)--(17), and checks the table.  At \(k=5\) it constructs the exact
rational point set, enumerates all 1,281 rooted cup histories and all 10,201
top mixed faces, verifies convexity and the unique top split, assigns the
2,331 codewords in disjoint blocks, and checks emission, load, and fibre one
exactly.
