# Terminal weight floor and the excess-rank Kraft gate

**Date:** 2026-08-15.  All logarithms are base two.  This is the exact
weighted endpoint after `EFFECTIVE_BRANCHING_ROLE_FOREST.md`.

## Verdict

Every low-\(Q_{\rm eff}\) terminal in the linear excess-rank regime has
quadratically tiny actual routed mass.  More precisely, if the root record
mass is \(M\), then each terminal output \(O\) satisfies the pathwise upper
bound

\[
                   \boxed{\ \mu(O)C_{\rm eff}(O)\le M.\ }       \tag{1}
\]

Since \(C_{\rm eff}=P_0/Q_{\rm eff}\), a terminal with
\(Q_{\rm eff}<Q_0\) obeys

\[
                   \boxed{\ \mu(O)<{M Q_0\over P_0}.\ }         \tag{2}
\]

Suppose, on a balanced rank slice,

\[
 {P_0\over M}
   \ge2^{\varepsilon L^2-KL\log L},
 \qquad Q_0=2^{BL\log L}.                              \tag{3}
\]

Then every low-\(Q_{\rm eff}\) terminal has

\[
 -\log\mu(O)
   \ge\varepsilon L^2-(K+B)L\log L.                   \tag{4}
\]

Consequently a quasipolynomial lower cutoff
\(\mu(O)\ge2^{-O(L\log L)}\) closes the branch **provided the excess in
(3) is measured relative to the root record mass \(M\)**.
Without such a cutoff it does not close: the weighted prefix-star
construction has

\[
 \mu=d^{-(s-k)},\qquad C_{\rm eff}=d^s,qquad
 M=d^k,qquad Q_{\rm eff}=1,                           \tag{5}
\]

and attains equality in (1)--(2).  Its weights are exactly a \(d\)-ary Kraft
distribution over first-divergence depth.

Thus the surviving live object is not merely a near-uniform branch tree.  It
is a **quadratic-depth chronology tail** whose selected leaf has probability
\(2^{-\Theta(L^2)}\), while discarded first-divergence siblings carry the
source mass.  Any positive planar theorem must charge that Kraft alphabet to
ordinary faces or prove that the canonical history weights in the minimizer
slice have a stronger floor.  No such charge is proved here.

The qualification above is load-bearing in the live source--release
rectangle.  There the known excess is \(P_0/M_D\), relative to the selected
completion family, while the forest root mass is approximately \(M_DH\).
The pocket factor \(H\) can make (3) false.  The canonical \(1/n\) atom floor
then cancels completion redundancy but returns only the already known
released bank; see `LIVE_ATOM_FLOOR_ROLE_FOREST_AUDIT.md`.  Thus this theorem
is a conditional weight-floor discharge, not an unconditional closure of the
live rectangle.

## 1. Proof of the pathwise upper bound

Let a terminal path be

\[
                        v_0,v_1,\ldots,v_t.             \tag{6}
\]

Write \(m_j\) for the whole record mass at \(v_j\).  At the edge
\(v_jv_{j+1}\), let \(b_j\le m_j\) be the mass in the chosen canonical-role
class before splitting by its actual label.  The selected heaviest-label
child has mass \(m_{j+1}\), so

\[
            r_j={b_j\over m_{j+1}}le{m_j\over m_{j+1}}.          \tag{7}
\]

Multiplying (7) telescopes:

\[
 C_{\rm eff}(O)=\prod_{j=0}^{t-1}r_j
       \le {m_0\over m_t}={M\over m_t}.               \tag{8}
\]

The decoder coalesces all formal copies at the same terminal literal pair;
after that coalescing \(m_t=\mu(O)\).  This proves (1).  Substituting
\(C_{\rm eff}=P_0/Q_{\rm eff}>P_0/Q_0\) proves (2), and (3) gives (4).

This upper inequality complements the global lower potential inequality

\[
                  \sum_O\mu(O)C_{\rm eff}(O)\ge M.     \tag{9}
\]

There is no contradiction: a single terminal can have the product in (1)
equal to \(M\), as in the prefix-star example.

## 2. Exact Kraft equality in the weighted prefix star

Put \(h=s-k\).  For each fixed core word, the tail code consists of the zero
word of weight \(d^{-h}\) and, for every depth \(j\), \(d-1\) first-divergence
words of weight \(d^{-j}\).  Its normalization is

\[
                    d^{-h}+(d-1)\sum_{j=1}^h d^{-j}=1. \tag{10}
\]

At each depth the \(d-1\) divergence classes and the continuing zero class
all have equal mass \(d^{-j}\).  Hence \(r_j=d\) at every core and tail role.
The selected terminal mass is \(d^{-h}\), proving (5) and

\[
                  \mu C_{\rm eff}=d^{-h}d^s=d^k=M.     \tag{11}
\]

This is precisely Kraft equality for a \(d\)-ary prefix code whose leaves are
the first divergence label/depth and the terminal zero word.  It shows why
mass-uniformity and row normalization alone cannot give a weight floor.

## 3. Coefficient interpretation

Take total role support \(N=sd\), \(L=\log N\),
\(s=\alpha L+O(1)\), and \(k=cL+O(1)\).  Then

\[
 \log M=cL^2-cL\log L+O(L),                            \tag{12}
\]

while

\[
 -\log\mu=(s-k)\log d
   = (\alpha-c)L^2-(\alpha-c)L\log L+O(L).             \tag{13}
\]

Thus the exact weight deficit is the excess role entropy.  At the critical
rank \(\alpha=c\), it is only lower order and the earlier terminal-capacity
bound pays.  For \(\alpha>c\), it is quadratic and can absorb every
quasipolynomial decoder threshold.

The next proof obligation is therefore sharply coefficient-sensitive:
convert a first-divergence Kraft code of quadratic depth entropy into a
planar prefix/cup/cap bank, or show that a minimizer cannot support it.  The
central Pascal prefix DAG is the mandatory live calibration; its coefficient
above one half explains why it does not settle the minimizer branch.

## 4. Verification

Run

```text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_terminal_weight_floor_excess_rank_gate.py
```

The script checks (1)--(2) on the exact rational weighted geometric role
forest and verifies Kraft equality (5), (10)--(11), and the pathwise
telescoping ratios on several weighted prefix-star instances.
