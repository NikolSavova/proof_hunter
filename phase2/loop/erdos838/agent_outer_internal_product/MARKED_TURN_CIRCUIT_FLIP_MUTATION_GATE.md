# A circuit-flip formula for a heavy marked turn

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

There is an exact local mutation which creates the desired source-retaining
one-face retags. Its sign, however, goes the wrong way for a minimizing
configuration.

Let a blocked singleton \(x\) lie just inside a common exposed source edge
\(ab\). Move \(x\) through the open segment \(ab\) into the adjacent
arrangement chamber, changing only the orientation of \(\{a,b,x\}\). Write
\(E^+_{ab}\) and \(E^-_{ab}\) for the numbers of ordinary faces on the two
sides which contain \(ab\) as an exposed edge. Then

\[
                 \boxed{\quad
                 V(P^-)-V(P^+)=E^+_{ab}-E^-_{ab}.
                 \quad}                                           \tag{1}
\]

Every face counted by \(E^+_{ab}\) is blocked by \(x\) in \(P^+\), while
its union with \(x\) is an ordinary, full-source-retaining face in \(P^-\).
Thus the flip gives an exact load-one composable retag in the **mutated**
configuration.

If \(P^+\) minimizes \(V\) among all \(n\)-point configurations, (1) only
implies

\[
                              E^+_{ab}\ge E^-_{ab}.                 \tag{2}
\]

The minimizer places \(x\) on the side of the **larger** rooted edge star
and hides that star. It need not expose a comparable opposite-side bank in
the original configuration.

This obstruction is sharp and stretchable. For every \(m\ge3\) there is a
rational \(m\)-point cap \(Q_m\), a boundary edge \(ab\), and two adjacent
positions \(x^+,x^-\) such that

\[
 E^+_{ab}=2^{m-2}-1,\qquad E^-_{ab}=0,\qquad
 V(Q_m\cup\{x^-\})-V(Q_m\cup\{x^+\})=2^{m-2}-1.                   \tag{3}
\]

Hence neither local circuit-flip minimality nor endpoint-star counting
converts a heavy marked turn into current ordinary retags.

There is a precise conditional escape. Put

\[
                         S_{\rm mut}=F_c(n)-V(P^+),                \tag{4}
\]

where \(F_c(n)=2^{c(\log n)^2}\) is the forbidden parent threshold. If the
flip preserves the rest of the marked construction and

\[
                  0\le E^+_{ab}-E^-_{ab}<S_{\rm mut},             \tag{5}
\]

then \(P^-\) is still a least-size counterexample and contains the
load-one retags. The entire marked argument may be restarted in \(P^-\).
The current theory gives no positive lower bound on \(S_{\rm mut}\) and no
upper bound on the flip increase. The exact missing mutation parameter is
therefore the ratio of rooted edge-star imbalance to parent counterexample
slack.

For a general canonical marked source, another hypothesis is also missing:
the common tangent edge must be an **adjacent mutation wall** for the
blocked label. A fixed tangent root does not imply that the blocked point
can reach that wall without crossing other pair lines.

The scalable example (3) is not a strict sub-half parent construction; its
cap reservoir is exponentially large in its number of points. Producing a
scalable stretchable barrier satisfying the strict parent upper would
itself require a sub-half construction, which is not claimed.

## 1. Exact adjacent-wall formula

Let \(Q\) be a planar general-position set and let \(a,b\in Q\). Choose a
point \(t\) in the open segment \(ab\) which lies on no other line through
two labels of \(Q\). Let \(D_t\) be a sufficiently small disk about \(t\)
meeting no such line except \(ab\). Choose

\[
                         x^+\in D_t\cap H^+,\qquad
                         x^-\in D_t\cap H^-,                       \tag{6}
\]

where \(H^+,H^-\) are the two open halfplanes bounded by \(ab\). Put
\(P^\pm=Q\cup\{x^\pm\}\). These two configurations differ by one realizable
rank-three mutation.

For a sign \(\epsilon\in\{+,-\}\), let \(\mathcal E^\epsilon_{ab}\) be the
family of ordinary faces \(R\subseteq Q\) such that:

1. \(|R|\ge3\) and \(a,b\in R\);
2. \(ab\) is an exposed edge of \(\operatorname{conv}R\); and
3. \(R\setminus\{a,b\}\subset H^\epsilon\).

Write \(E^\epsilon_{ab}=|\mathcal E^\epsilon_{ab}|\).
Also write

\[
 \Phi_P(z)=\sum_{S\text{ ordinary in }P}z^{|S|},\qquad
 \Phi^\epsilon_{ab}(z)
   =\sum_{R\in\mathcal E^\epsilon_{ab}}z^{|R|}.                  \tag{7}
\]

> **Theorem 1 (single-flip face derivative).** One has the stronger
> rank-profile identity
> \[
>       \Phi_{P^-}(z)-\Phi_{P^+}(z)
>          =z\bigl(\Phi^+_{ab}(z)-\Phi^-_{ab}(z)\bigr).           \tag{8}
> \]
> In particular, (1) follows on setting \(z=1\). Moreover,
> \[
> \begin{array}{c|cc}
>  &P^+&P^-\\ \hline
> R\in\mathcal E^+_{ab}
>     &R\cup\{x\}\text{ nonordinary}
>     &R\cup\{x\}\text{ ordinary}\\
> R\in\mathcal E^-_{ab}
>     &R\cup\{x\}\text{ ordinary}
>     &R\cup\{x\}\text{ nonordinary}
> \end{array}                                                       \tag{9}
> \]
> hold. Every other labelled subset has the same status in \(P^+\) and
> \(P^-\).

**Proof.** A subset not containing all three labels \(a,b,x\) has the same
restricted chirotope in the two configurations. Consider
\(R\cup\{x\}\) with \(a,b\in R\).

If \(R\) is not ordinary, neither union is ordinary by heredity. Suppose
\(R\) is ordinary. If \(ab\) is not an exposed edge of
\(\operatorname{conv}R\), the open segment \(ab\) is locally inside that
convex polygon; both sufficiently close choices \(x^\pm\) are hidden.
If \(ab\) is exposed, all remaining vertices of \(R\) lie strictly in one
halfplane. On that same side, the nearby \(x\) lies inside
\(\operatorname{conv}R\). On the opposite side it replaces \(ab\) by the
two boundary edges \(ax,xb\), and every vertex of \(R\) remains extreme.
This proves (9). The rank-two set \(\{a,b,x\}\) is a convex triple on both
sides and is correctly excluded by \(|R|\ge3\). Summing the two changed
families rank by rank proves (8), hence (1). \(\square\)

The proof also shows that the map

\[
          R\longmapsto R\cup\{x^-\}
               \qquad(R\in\mathcal E^+_{ab})                      \tag{10}
\]

is an injective ordinary one-face retag in \(P^-\). It retains the literal
source \(R\), the marked singleton \(x\), and the exposed endpoint edge
\(ab\), so it is composable with an endpoint recurrence.

## 2. What minimality says

If \(P^+\) is an \(n\)-point minimizer, the adjacent configuration \(P^-\)
has at least as many faces:

\[
                         V(P^+)\le V(P^-).                         \tag{11}
\]

Equations (1) and (11) give (2). Thus a minimizing flip chooses the chamber
in which the larger of the two edge-star families is hidden. If a marked
fiber of weight \(W\) is supported on
\(\mathcal E^+_{ab}\), the source weight cap gives only

\[
                         W\le E^+_{ab}.                            \tag{12}
\]

Neither (2) nor (12) lower-bounds \(E^-_{ab}\). The ordinary
\(x\)-retaining faces already present in \(P^+\) are precisely the
opposite-star family in (9), which may be empty.

This is the local circuit-flip analogue of reflection-minimal
anti-alignment at a full strong seam: the mutation orients toward the bad
profiles rather than releasing them.

## 3. Conditional counterexample-preserving mutation

Assume \(P^+\) is a least-size counterexample to the \(c\)-target, and that
the marked rank, root, support, and approximate-tree data not involving
\(\chi(a,b,x)\) survive the adjacent flip. Equation (1) gives

\[
             V(P^-)=V(P^+)+E^+_{ab}-E^-_{ab}.                     \tag{13}
\]

Under (5), \(V(P^-)<F_c(n)\). Every proper induced subset of \(P^-\) has at
least the inductive target because \(n\) was the least bad size; it need
not itself be minimizing. Thus all least-size deletion inequalities remain
available. At the same time, (10) supplies the one-face source-retaining
retags.

This is a valid mutation closure, but its hypotheses are not currently
proved:

* the parent slack \(S_{\rm mut}\) may be less than one;
* a heavy star may make the increase in (13) quadratic-exponential; and
* reaching the desired tangent edge may require a path through many
  arrangement chambers rather than one adjacent flip.

Along a longer allowable mutation path, (1) telescopes exactly, but
intermediate positive and negative edge-star derivatives need not preserve
the parent upper bound or the canonical marked state.

## 4. Scalable rational one-sided barrier

Fix rational numbers

\[
             -10=x_1<x_2<\cdots<x_{m-1}<x_m=10
\]

and put

\[
                         q_i=(x_i,100-x_i^2).                      \tag{14}
\]

Choose the interior \(x_i\)'s so that every chord other than
\(q_1q_m\) meets the vertical line through the origin at height greater
than one. Set

\[
                  a=q_1=(-10,0),\quad b=q_m=(10,0),\quad
                  x^+=(0,1),\quad x^-=(0,-1).                     \tag{15}
\]

The points \(Q_m=\{q_1,\ldots,q_m\}\) form a strict cap, and \(ab\) is its
lower exposed edge. The two positions in (15) are in adjacent arrangement
chambers; only \(\chi(a,b,x)\) changes.

Every subset \(R\subseteq Q_m\) containing \(a,b\) and at least one other
label is ordinary, has exposed edge \(ab\), and lies on the plus side.
Therefore

\[
                    E^+_{ab}=2^{m-2}-1,\qquad E^-_{ab}=0.          \tag{16}
\]

Equation (3) follows from Theorem 1. In \(P^+\), the singleton \(x^+\) is
hidden in every one of these source faces; in \(P^-\), all their unions
with \(x^-\) are ordinary and injectively retain the source.

This family proves that the opposite-star term in (1) cannot be recovered
from planarity, stretchability, rank-three mutation, or local minimality.
The obstruction is already present before the multi-face noncup release
problem: a single hidden marked label suffices.

## 5. Audit against the canonical Pascal turn

The canonical Pascal source fiber has a fixed tangent triple and a fixed
hidden-point circuit class. After fixing which pair of the triple is the
boundary edge, only a constant factor is lost, and every source contains a
common exposed edge. This resembles the plus-star side of Theorem 1.

Two gaps prevent direct application:

1. the hidden pocket label is not known to lie in the arrangement chamber
   adjacent to that edge; and
2. a complete released noncup face \(U\) contains more information than
   the singleton \(x\). Flipping one circuit label need not make
   \(D\cup U\) ordinary.

The exact Pascal strong-glue identity is the macroscopic analogue. Its
current orientation uses the minimum of the four reflection products, and
fixed-label deletion remains bad until the whole source is removed.
Therefore neither a single circuit flip nor a whole-child reflection
produces a current composable retag.

## 6. Exact remaining mutation parameter

A successful minimizer-specific mutation theorem must supply all three:

1. **adjacency:** a positive-mass marked fiber has one common exposed edge
   whose blocked label is in the adjacent arrangement chamber;
2. **slack control:** its edge-star derivative obeys (5), or a sequence of
   flips has every prefix below the parent threshold; and
3. **full-release stability:** the retag after mutation retains enough of
   the released endpoint/profile state to replace the marked turn in the
   approximate-tree recurrence.

The first and third are geometric. The second is the exact place where the
strict parent upper must enter. Current deletion minimality gives none of
them.

## 7. Verification

The verifier
verify_marked_turn_circuit_flip_mutation_gate.py constructs the rational
eight-point cap

\[
 x_i\in\{-10,-8,-5,-2,1,4,7,10\}
\]

and the two positions (15). It exhausts every labelled subset, checks
general position, verifies that exactly one triple orientation changes,
checks the complete classification (9), verifies (8) coefficient by
coefficient, and confirms

\[
              E^+_{ab}=63,\qquad E^-_{ab}=0,\qquad
              V(P^-)-V(P^+)=63.
\]
