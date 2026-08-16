# A live Pascal common-guard barrier to source--pocket multiplication

**Date:** 2026-08-15.  All logarithms are base two.  Counts below exclude
the empty face; this changes nothing asymptotically.

## Verdict

There is no unconditional two-family retention theorem at the interface left
open by `EXCESS_RANK_FOUR_LOCAL_PROJECTION_DICHOTOMY.md` and
`LIVE_DENSE_COMPLETION_PROFILE_GATE.md`.  A central Pascal cell gives an exact,
scalable, live-normalized obstruction.

In its top strong-glue split

\[
             P=Y\prec Z,
\]

take on the left a fixed-rank fibre of ordinary faces which are not caps, and
on the right all ordinary faces which are not cups.  After fixing one actual
noncap triple \(T\subset Y\), the records form a complete rectangle

\[
                    \mathcal D_{T,r}\times\mathcal H_Z.       \tag{1}
\]

Every \(D\in\mathcal D_{T,r}\) contains the same physical label
\(x\in T\).  Every \(z\in Z\) is blocked by the same rooted \(3+1\) witness
\(T\cup\{z\}\).  More strongly, for every record \((D,U)\), the whole set
\(D\) is the unique inclusion-minimal guard which releases \(U\): as long as
one label of \(D\) remains, its union with \(U\) is nonconvex.

For the central Pascal family both sides of (1) have size

\[
             V(P)\,2^{-O(L\log L)},\qquad L=\log |P|,          \tag{2}
\]

the left rank is \(O(L)\), and in fact it has linear excess above every
threshold \(cL\) with

\[
              c<\beta:=1-{1\over4\ln2}=0.639326\ldots .       \tag{3}
\]

Thus this is live at precisely the normalization of the dense completion
core.  It is not the earlier bounded-rank parabolic toy obstruction.

The obstruction also defeats the strengthened fixed-label chronology.
Deleting any fixed sequence of source labels preserves incompatibility until
the source trace becomes empty.  Every source-side one-gap face, ambient
completion, or four-local alternative which remains nonempty is still
incompatible with every \(U\in\mathcal H_Z\).  Consequently entropy-sensitive
semialgebraic retention cannot help: the entire rectangle is already one
homogeneous bad product cell.

This does **not** construct a sub-half point set and does not refute a
minimizer-specific theorem.  The central Pascal cell has coefficient
\(\beta>1/2\).  It proves the narrower and important negative result that
live normalization, excess rank, a fixed root, deterministic blocker support,
exact pair decoding, and a length-\(\Theta(L)\) label chronology do not by
themselves multiply the source and pocket banks.  Any closure must use an
additional minimizer/profile-balance input, a third cyclic role, or a bank
which charges the all-loop guard chronology globally.

## 1. Exact strong-glue rectangle

Use the following standard strong-glue identity.  If \(P=Y\prec Z\), a
nonempty subset meeting both children is an ordinary face exactly when its
\(Y\)-trace is a cap and its \(Z\)-trace is a cup.  In particular, writing
\(\mathcal F(X)\), \(\mathcal C(X)\), and \(\mathcal U(X)\) for the nonempty
ordinary, cap, and cup families,

\[
 V(P)=V(Y)+V(Z)+C(Y)U(Z).                              \tag{4}
\]

Set

\[
 \mathcal S_Y=\mathcal F(Y)\setminus\mathcal C(Y),
 \qquad
 \mathcal H_Z=\mathcal F(Z)\setminus\mathcal U(Z).    \tag{5}
\]

Every \(D\in\mathcal S_Y\) contains a noncap triple: being a cap is exactly
the condition that every increasing triple has cap orientation.  Choose the
lexicographically first such triple \(T(D)\), and partition \(\mathcal S_Y\)
by the pair \((T(D),|D|)\).  There is a triple \(T\) and a rank \(r\) for
which

\[
 |\mathcal D_{T,r}|
 \ge { |\mathcal S_Y|\over { |Y|\choose3}(R_Y+1)},     \tag{6}
\]

where \(R_Y\) is the maximum face rank in \(Y\).  All members of this fibre
contain \(T\); fix any \(x\in T\).

Now take \(D\in\mathcal D_{T,r}\), \(U\in\mathcal H_Z\), and \(z\in Z\).
The strong-glue identity gives all of the following.

* \(T\cup\{z\}\) is nonconvex because its left trace is not a cap.
  Hence the pocket of labels blocked by the fixed physical root \(T\) is all
  of \(Z\).
* \(\{y\}\cup U\) is nonconvex for every \(y\in Y\), because \(U\) is not a
  cup.
* If \(G\subseteq D\), then

  \[
       (D\setminus G)\cup U\text{ is convex}
       \quad\Longleftrightarrow\quad G=D.             \tag{7}
  \]

  Indeed, the forward implication fails whenever \(D\setminus G\) is
  nonempty, while for \(G=D\) the output is the ordinary face \(U\).

Thus \(D\) is the unique inclusion-minimal guard.  The two ordinary targets
\((D,U)\) recover the literal record, so the pair decoder has load one.  The
rectangle (1) is therefore an exact complete source--release relation, not a
mere pair of unrelated large face families.  If the live incidence measure
requires source mass at most one, assign every pair weight
\(1/|\mathcal H_Z|\).  Then every source row has total weight one, the total
mass is \(|\mathcal D_{T,r}|\), and the pair decoder remains exact.  Thus the
example respects genuine-history/source domination.  It is not claimed to
reproduce any additional upstream weighted-degree statistic beyond the
two live target alphabets and complete compatibility relation.

There is also no hidden benefit from replacing \(D\) by another ordinary
left trace \(A\subseteq Y\).  For every nonempty \(A\in\mathcal F(Y)\) and
every \(U\in\mathcal H_Z\), the set \(A\cup U\) is nonconvex.  This covers
the ambient, one-gap, projection, and four-local source-side banks unless an
operation removes the left trace altogether.

## 2. Live normalization in a central Pascal cell

Let

\[
 P_n=T(n,h),\qquad n=2h,
\]

be the central cell in the standard strongly glued Pascal construction.  Its
top split has mirror children

\[
 Y=T(n-1,h-1),\qquad Z=T(n-1,h),                     \tag{8}
\]

of equal size and equal face count.  Put \(W=V(Y)=V(Z)\) and
\(C=C(Y)=U(Z)\).  Then (4) is the exact recurrence

\[
                         V(P_n)=2W+C^2.               \tag{9}
\]

The cap-path estimate already proved in `agent_asymptotic/DERIVATION.md` is
uniform in the cell index:

\[
 \log C(m,i)=m^2 A(i/m)+O(m\log m).                  \tag{10}
\]

Apply the lower mixed product in the top split of \(Y\):

\[
 W\ge C(n-2,h-2)\,U(n-2,h-1)
   = C(n-2,h-2)\,C(n-2,h-1).                         \tag{11}
\]

All three cap terms in (9)--(11) have index ratio
\(1/2+O(1/n)\).  The explicit smooth function \(A\) in the cited estimate
therefore gives

\[
 {C^2\over W}\le 2^{O(n\log n)},
 \qquad
 {V(P_n)\over W}\le 2^{O(n\log n)}.                 \tag{12}
\]

Moreover, a single cap count has only half the quadratic logarithmic rate of
the product in (11).  Hence

\[
 |\mathcal S_Y|=W-C=(1-o(1))W,
 \qquad
 |\mathcal H_Z|=W-C=(1-o(1))W.                       \tag{13}
\]

Since

\[
 |P_n|={n\choose n/2},\qquad L=\log|P_n|=n-O(\log n),\tag{14}
\]

(12)--(13) prove the two live bounds in (2).

The elementary Erdős--Szekeres induction gives, in \(T(m,i)\), maximum cap
rank \(i+1\), maximum cup rank \(m-i+1\), and maximum ordinary-face rank at
most \(m\).  Thus \(R_Y\le n-1\).  The denominator in (6) is at most
\(|Y|^3n\), only \(2^{O(L)}\).  Therefore the fixed-\((T,r)\) fibre itself
satisfies (2).

Finally, the central cell asymptotic is

\[
       \log V(P_n)=(\beta+o(1))n^2,\qquad
       \beta=1-{1\over4\ln2}.                        \tag{15}
\]

Equations (2), (6), and
\(\lvert\mathcal D_{T,r}\rvert\le {|Y|\choose r}\le|Y|^r\)
imply

\[
                         r\ge(\beta-o(1))L.           \tag{16}
\]

This proves the claimed excess-rank statement (3).

## 3. Why fixed-label peeling does not couple the banks

Suppose a bad-record peeling procedure fixes one physical source label and
deletes it, losing at most a factor \(2|P_n|\) per step.  In (1), after any
fixed deleted set \(K\subseteq Y\), restrict to records with \(K\subseteq D\).
The map \(D\mapsto D\setminus K\) is injective.  For every survivor with
\(D\setminus K\ne\varnothing\), (7) still says

\[
                         (D\setminus K)\cup U
                         \notin\mathcal F(P_n).        \tag{17}
\]

Thus the Pascal example realizes the full-loop alternative at every depth.
The strengthened \(2n\)-choice chronology can indeed peel a linear number of
labels; it does not manufacture a mixed face.  Its accumulated
\(2^{\Theta(L^2)}\) cost is exactly what the excess rank can support.

Likewise, a semialgebraic or entropy retention lemma for the two selected
families cannot distinguish a helpful subrectangle: the predicate

\[
             \mathbf 1[A\cup U\text{ is convex}]
\]

is identically zero on
\((\mathcal F(Y)\setminus\{\varnothing\})\times\mathcal H_Z\).
The missing input is therefore not better two-family regularization.  It is
an operation that charges the repeated all-loop guard state elsewhere in the
global minimizer, or an additional role/profile constraint which the Pascal
cell is not required to satisfy.

## 4. Scope and consequence for the live proof

This report closes the requested alternative by a scalable
**live-normalized regression**, not by a coefficient gain.  It shows that the
following data, even simultaneously, are insufficient:

1. two face alphabets of size \(V(P)2^{-O(L\log L)}\);
2. exact ordered-pair decoding;
3. rank \(O(L)\) with linear excess rank;
4. a fixed physical source label and a fixed rooted \(3+1\) circuit whose
   blocker support is the whole pocket;
5. a complete source--release rectangle, including row-normalized
   source-dominated weights; and
6. a length-\(\Theta(L)\) hereditary fixed-label chronology.

The example is not a candidate minimizer: its coefficient is
\(\beta>1/2\).  Therefore it does not kill a theorem which additionally uses
the fixed-gap minimizer inequality, endpoint/profile balance, or a global
third-role/cycle charge.  It does kill any proposed splice whose hypotheses
are only the current live two-sided transfer plus the local
four-local/one-gap alternatives.

## 5. Verification artifact

`verify_live_pascal_common_guard_barrier.py` performs two independent exact
checks.

* On the rational \(T(6,3)=T(5,2)\prec T(5,3)\) realization it enumerates
  all child faces, selects a canonical fixed-triple/fixed-rank fibre, checks
  the complete mixed-face classification, verifies the rooted blockers, and
  exhausts every guard subset in every record.
* Using the independent integer dynamic programs, it checks (9), positivity
  of both nonprofile banks, and the stated \(2^{O(n\log n)}\) normalization
  envelope for all even (6\le n\le96).

The finite computation is a regression check; the proof for all (n) is
the exact strong-glue argument plus the uniform estimate (10).
