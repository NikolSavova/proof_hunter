# Three incompatible ears in an exact minimizer, and the order-three gate

**Date:** 2026-08-15. The face count \(V\) is nonempty.

## Verdict

The proposed three-ear dichotomy is false on the exact nine-point global
minimizer.

In the stored rational minimizer, label \(x=2\) is hidden inside each of the
three ordinary source triangles

\[
 R_1=\{0,1,6\},\qquad R_2=\{0,1,7\},\qquad R_3=\{1,3,8\}.          \tag{1}
\]

Use the exposed repair edges

\[
                       e_1=61,\qquad e_2=71,\qquad e_3=38.        \tag{2}
\]

Let \(C_i\) be the open ear chamber across \(e_i\): a replacement position
\(x'\in C_i\) makes \(R_i\cup\{x'\}\) an ordinary quadrilateral while
retaining every source vertex. Exact rational Fourier--Motzkin elimination
gives

\[
        C_1\cap C_2\ne\varnothing,\qquad
        C_1\cap C_3\ne\varnothing,\qquad
        C_2\cap C_3\ne\varnothing,\qquad
        C_1\cap C_2\cap C_3=\varnothing.                          \tag{3}
\]

Nevertheless every two-source union and the full source union are
nonordinary:

\[
             R_i\cup R_j\notin\mathcal F(P)\quad(i\ne j),\qquad
             R_1\cup R_2\cup R_3\notin\mathcal F(P).              \tag{4}
\]

The order type has \(V=168\) nonempty faces and is the unique global
minimizer in the documented exhaustive realizable-order-type database.
Therefore no relocation of two or three physical labels decreases \(V\).
Equations (1)--(4) simultaneously refute both proposed conclusions:

1. pairwise repairability of three same-label ear contexts does not force an
   already-ordinary union of their base supports; and
2. triple incompatibility does not force a two-/three-label relocation whose
   mixed Hessian beats the separate costs.

The barrier is finite rather than scalable, but it is genuinely
minimizer-safe and stretchable, which the earlier Pascal regressions were
not.

There is an exact rank-three classification. Write each ear chamber as a
finite system

\[
                              a\cdot p+c>0.                        \tag{5}
\]

If three chambers are pairwise feasible and jointly infeasible, planar
Helly and strict Farkas give one boundary inequality from each chamber and
positive coefficients \(\lambda_1,\lambda_2,\lambda_3\) such that

\[
       \lambda_1a_1+\lambda_2a_2+\lambda_3a_3=0,\qquad
       \lambda_1c_1+\lambda_2c_2+\lambda_3c_3\le0.                \tag{6}
\]

Thus the residue is exactly a dual three-line cage. The minimizer example
shows that this rank-three cage does not imply a primal ordinary union or a
decreasing mutation.

An order-three canonical strong-glue comparison is also exact. For
\(Q=P-X\), \(|X|=3\), \(N=n-3\), every global minimizer satisfies

\[
\boxed{
 V(P)-V(Q)\le7+\min\{
 6C(Q),\,6U(Q),\,3C(Q)+U(Q)+3N,\,
 C(Q)+3U(Q)+3N\}.}                                                \tag{7}
\]

Summing (7) yields third-rank-moment endpoint inequalities. They retain new
scalar moment data, but their low-rank leading constants are weaker than the
singleton and order-two bounds. The highest third Möbius interaction is
again nonnegative and bounded by \(V(Q)+1\), so it supplies no new
correlation. At \(n=9\), (7) has slack 19 to 34 faces. The balanced Pascal
wrapper violates it by 305 to 434 faces and is again rejected as nonminimal.

The exact surviving target must use additional marked history beyond the
three ear chambers: the Helly/Farkas cage and all order-\(\le3\) scalar
minimality inequalities coexist in a true minimizer.

## 1. Ear chambers and Fourier--Motzkin classification

Let \(R=(r_1,\ldots,r_s)\) be the counterclockwise boundary of an ordinary
face, and let \(e=r_kr_{k+1}\). Define its open ear chamber by

\[
 C(R,e)=
 \left\{p:
 \begin{array}{ll}
 \chi(r_k,r_{k+1},p)<0,&\\
 \chi(r_j,r_{j+1},p)>0,&j\ne k
 \end{array}\right\}.                                             \tag{8}
\]

Indices are cyclic. Every point of (8) lies outside precisely across \(e\)
and inside every other supporting halfplane. Hence the edge \(e\) is
replaced by the two edges through \(p\), and

\[
                              R\cup\{p\}\text{ is ordinary}.      \tag{9}
\]

Each condition in (8) has the affine form

\[
                              ax+by+c>0.                          \tag{10}
\]

Fourier--Motzkin eliminates \(y\) exactly. Conditions with \(b>0\) give
lower affine bounds on \(y\), those with \(b<0\) give upper bounds, and each
lower--upper pair gives one strict linear inequality in \(x\). Feasibility
then reduces to a strict interval for \(x\). This is the exact algorithm in
the verifier.

For the abstract classification, apply planar Helly to all halfplanes
appearing in three ear systems. A minimally infeasible subsystem has at
most three inequalities. Pairwise feasibility of the chamber systems means
that it must use at least one inequality from every chamber, hence exactly
one from each. Strict Farkas gives (6). Conversely (6) makes simultaneous
satisfaction impossible after taking the positive weighted sum.

The certificate is a directional cage only. The source labels need not lie
in convex position when the three contexts are united.

## 2. Exact nine-point minimizer barrier

The rational coordinates, in physical-label order, are

\[
\begin{array}{c|rrrrrrrrr}
i&0&1&2&3&4&5&6&7&8\\ \hline
x_i&62614&2922&10209&20660&33336&30137&15334&14934&10934\\
y_i&7322&4014&14386&24299&29017&33324&45211&55621&61521.
\end{array}                                                       \tag{11}
\]

The three source hull orders are

\[
                  (1,0,6),\qquad(1,0,7),\qquad(1,3,8),           \tag{12}
\]

so the directed edges in (2) occur on their boundaries. Direct determinant
checks show

\[
             2\in\operatorname{int}\operatorname{conv}R_i
                        \qquad(i=1,2,3).                          \tag{13}
\]

Thus the actual singleton \(x=2\) is blocked in every context.

The exact systems (8) for (12) have feasible pair intersections. The
verifier returns rational interior witnesses, perturbs them within their
positive margins to avoid every ambient pair line, and checks both repaired
quadrilaterals directly. The combined nine inequalities are infeasible by
exact Fraction arithmetic. An explicit three-row subsystem is

\[
 \begin{array}{rrr}
 -37889&-47280&2718566006\\
 -51607& 12012& 102579486\\
  37222&  9726&-1005338594
 \end{array}                                                       \tag{13a}
\]

with rows interpreted as \(ax+by+c>0\), one from each ear chamber. The
positive Farkas multipliers

\[
                    (158173391,\ 231891291,\ 482516938)           \tag{13b}
\]

annihilate the first two columns, while their weighted constant sum is

\[
                           -31300806765102400<0.                   \tag{13c}
\]

This is a literal exact certificate of the last assertion in (3). Direct
hull enumeration proves (4).

The stored nonempty face profile is

\[
                         (v_1,v_2,v_3,v_4,v_5)
                              =(9,36,84,36,3).                    \tag{14}
\]

The database certificate establishes global minimality at \(V=168\).
Consequently every realizable same-size re-embedding, including any move of
two or three labels designed from the cage certificate, has at least 168
faces. This is exactly the minimizer-safe failure requested.

## 3. The order-three Möbius interaction

For anchors \(u,v,w\), define

\[
 J_Q(u,v,w)=
  |\{R\subseteq Q:R\cup\{u,v,w\}\text{ is ordinary}\}|.           \tag{15}
\]

The eight anchor masks give a coefficientwise expansion analogous to the
order-two identity. Its highest alternating difference is

\[
\begin{aligned}
 &V(Q+u+v+w)-V(Q+u+v)-V(Q+u+w)-V(Q+v+w)\\
 &\quad+V(Q+u)+V(Q+v)+V(Q+w)-V(Q)
       =J_Q(u,v,w)\ge0.                                           \tag{16}
\end{aligned}
\]

Deleting the three anchors injects this family into the augmented base-face
complex, so

\[
                              J_Q(u,v,w)\le V(Q)+1.               \tag{17}
\]

If an output in (16) retains the union of several variable base supports,
that union was already ordinary by heredity. Thus the positive third
interaction has the same anchor-erasure cancellation as orders one and two.

Mixed relocation Hessians obtained by comparing actual and new anchors can
have either sign; global minimality only says their total, after all lower
order relocation costs, is nonnegative. The nine-point barrier makes clear
that the Farkas cage does not force the negative total needed for a
decreasing move.

## 4. Four canonical three-anchor mutations

Let \(E_3\) be a three-point order type. Its face count is seven, while its
two endpoint profiles are six and seven. Reflecting it puts the smaller
profile toward \(Q\). Therefore

\[
\begin{aligned}
 V(Q\prec E_3)-V(Q)&=7+6C(Q),\\
 V(E_3\prec Q)-V(Q)&=7+6U(Q).                                    \tag{18}
\end{aligned}
\]

For a split of one anchor to the left and two to the right, strong-glue
associativity gives

\[
 V(\{u\}\prec Q\prec E_2)-V(Q)
                 =7+3C(Q)+U(Q)+3N,                               \tag{19}
\]

where \(V(E_2)=C(E_2)=U(E_2)=3\). Reflection gives

\[
 V(E_2\prec Q\prec\{u\})-V(Q)
                 =7+C(Q)+3U(Q)+3N.                               \tag{20}
\]

Global minimality and the least of (18)--(20) prove (7).

## 5. Third deletion moments

Put

\[
                   w_3(r)={n\choose3}-{n-r\choose3}.              \tag{21}
\]

The exact deletion identities are

\[
\begin{aligned}
 \sum_{|X|=3}\{V(P)-V(P-X)\}
    &=\sum_{F\in\mathcal F(P)}w_3(|F|),\\
 \sum_{|X|=3}C(P-X)
    &=\sum_{A\in\mathcal C(P)}{n-|A|\choose3},\\
 \sum_{|X|=3}U(P-X)
    &=\sum_{B\in\mathcal U(P)}{n-|B|\choose3}.                    \tag{22}
\end{aligned}
\]

Summing the four branches of (7) separately gives:

\[
\begin{aligned}
 \sum_Fw_3(|F|)
 &\le7{n\choose3}
       +6\sum_{A\in\mathcal C(P)}{n-|A|\choose3},\\
 \sum_Fw_3(|F|)
 &\le7{n\choose3}
       +6\sum_{B\in\mathcal U(P)}{n-|B|\choose3},                 \tag{23}\\
 \sum_Fw_3(|F|)
 &\le(3n-2){n\choose3}
       +3\sum_{A\in\mathcal C(P)}{n-|A|\choose3}
       +\sum_{B\in\mathcal U(P)}{n-|B|\choose3},\\
 \sum_Fw_3(|F|)
 &\le(3n-2){n\choose3}
       +\sum_{A\in\mathcal C(P)}{n-|A|\choose3}
       +3\sum_{B\in\mathcal U(P)}{n-|B|\choose3}.
\end{aligned}
\]

These are new exact third-moment constraints. On a rank
\(r=o(n)\) slice, however,

\[
                 w_3(r)=\left({r\over2}+o(r)\right)n^2.          \tag{24}
\]

The first branch of (23), after dropping rank correlations, yields only
approximately

\[
                              C(P)\gtrsim {rV(P)\over2n},         \tag{25}
\]

compared with \(rV(P)/n\) from the singleton first moment. The order-three
scalar inequality is weaker at the leading low-rank scale. Its value is the
retained third-moment correlation, for which no favorable minimizer theorem
is currently known.

## 6. Finite order-three audit

For the true five-point minimizer, the pointwise slack in (7) is exactly
two for every triple. For the nine-point minimizer it ranges from 19 to 34;
the mixed \(1+2\) branches are optimal for 84 of the 84 triples. Thus the
three-ear barrier is comfortably compatible with the canonical comparison.

For the balanced wrapper \(T(4,2)\prec T(4,2)\), all 220 triple deletions
violate (7), by 305 to 434 faces. The wrapper also violates the summed
third-moment inequalities. As at orders one and two, canonical Pascal is a
sharp local converter regression but not a minimizer-safe one.

## 7. Scope

Proved:

* a finite stretchable global-minimizer counterexample to the proposed
  three-ear dichotomy;
* exact Fourier--Motzkin and Farkas classification of the Helly residue;
* the third Möbius interaction and base-face capacity bound;
* the four-branch order-three canonical minimizer inequality;
* four exact third-rank-moment endpoint inequalities; and
* exact \(n=5,n=9,n=12\) verification.

Not proved:

* a scalable sequence of minimizers carrying the same cage;
* a marked-history condition which excludes the nine-point pattern; or
* any leading coefficient improvement from the third moments.

Any positive splice must retain data absent from the bare ear chambers,
their source supports, and order-\(\le3\) minimality.

## 8. Verification

The verifier verify_three_ear_minimizer_barrier_and_order_three_gate.py uses
only exact rational arithmetic. It verifies the ear systems and their
pair/triple intersections by Fourier--Motzkin elimination, checks source
hiddenness and all bad unions, checks the third Möbius decomposition, and
exhausts every triple deletion and moment inequality on the three finite
calibrations.
