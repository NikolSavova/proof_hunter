# Stationary all-delete seams: weighted child minimality and the high-wall residue

**Date:** 2026-08-15. All face and endpoint counts are nonempty. All
logarithms are base two.

## Verdict

Global \(V\)-minimality supplies a new exact constraint in a literal
two-block all-delete state. If

\[
                              P=A\prec B                         \tag{1}
\]

is a strong glue, put

\[
\begin{aligned}
 W_A&=V(A),& C_A&=C(A),& U_A&=U(A),& a&=|A|,\\
 W_B&=V(B),& C_B&=C(B),& U_B&=U(B),& b&=|B|.
\end{aligned}
\]

The parent count is

\[
                         V(P)=W_A+W_B+C_AU_B.                   \tag{2}
\]

If \(P\) is globally \(V\)-minimal among \((a+b)\)-point
configurations, then \(A\) is not merely a face-minimal child. It minimizes
the weighted functional

\[
                         \mathcal J_A(Q)=V(Q)+U_BC(Q),          \tag{3}
\]

and \(B\) minimizes

\[
                         \mathcal J_B(R)=V(R)+C_AU(R).          \tag{4}
\]

Singleton replacement inside these two functionals gives exact
coefficient-summed inequalities retaining the child face-rank and endpoint-
rank moments. In particular, writing

\[
 \mu_AW_A=\sum_{F\in\mathcal F(A)}|F|,
 \qquad M_C(A)=\sum_{F\in\mathcal C(A)}|F|,
 \qquad M_U(A)=\sum_{F\in\mathcal U(A)}|F|,                     \tag{5}
\]

and symmetrically for \(B\), every minimal seam satisfies

\[
\begin{aligned}
 \mu_AW_A+U_BM_C(A)
   &\le (1+U_B)\{a+aC_A-M_C(A)\},\\
 \mu_AW_A+U_BM_C(A)
   &\le a+aU_A-M_U(A)+U_Ba^2,                                 \tag{6}\\
 \mu_BW_B+C_AM_U(B)
   &\le (1+C_A)\{b+bU_B-M_U(B)\},\\
 \mu_BW_B+C_AM_U(B)
   &\le b+bC_B-M_C(B)+C_Ab^2.
\end{aligned}
\]

This has two concrete consequences.

1. It eliminates the exact scalar equality family previously used to show
   sharpness of the parent endpoint-reset inequality. For every
   \(m\ge3\) and its allowed parameter
   \(t\ge m+\binom m2\), that family violates the second line of (6), even
   using only the universal bound \(\mu_A\ge1\). Hence it cannot be the
   profile of a globally minimal planar seam.
2. The exact rational central Pascal seam \(T(6,3)\) also violates (6):
   replacing one point inside either child decreases the parent face count
   by between \(1041\) and \(1818\), depending on the point.

Thus global minimality genuinely removes the two currently stored scalar
and finite planar stationary calibrations.

The general survivor is still not closed. The coarse consequences of (6)
are

\[
\begin{aligned}
 U_A&\ge {\mu_AW_A-a-U_Ba^2\over a},\\
 C_B&\ge {\mu_BW_B-b-C_Ab^2\over b}.                            \tag{7}
\end{aligned}
\]

When both facing profiles \(C_A,U_B\) are small, (7) forces enormous
opposite profiles. Double reflection exposes the ordinary mixed bank

\[
                              U_AC_B,                            \tag{8}
\]

but in another configuration. Its exact wall cost is

\[
                   \Delta_{\rm wall}=U_AC_B-C_AU_B\ge0.         \tag{9}
\]

If the fixed-gap slack

\[
                        S_{\rm par}=F(n)-V(P)                   \tag{10}
\]

obeys \(\Delta_{\rm wall}<S_{\rm par}\), the double-reflected
configuration is still a counterexample and has the large mixed bank (8);
the proof may restart there. This is a rigorous conditional mutation
closure.

But the parent upper bound supplies no positive lower bound on
\(S_{\rm par}\). At the live child scale, (7) can make
\(U_AC_B\asymp W_AW_B/(ab)\), quadratically larger than the parent target.
The wall is then unaffordable, not decreasing. The surviving state is
therefore an exact trichotomy:

1. a weighted singleton child mutation decreases \(V\);
2. a near wall exposes a polylog-density mixed bank inside another
   counterexample; or
3. one has a high-wall/one-sided endpoint-skew state.

No current theorem excludes the third branch. In particular, order-one
minimality does not pull the opposite mixed bank back through the wall.
Order-two and order-three minimizer inequalities may constrain that wall,
but the known exact \(n=5,n=9\) audits show that their interaction Hessians
have both signs. No half-coefficient closure is claimed.

## 1. Weighted child functionals

The strong-glue recurrence is (2). Replace \(A\) by any \(a\)-point
configuration \(Q\), embedded in the same left chart while keeping \(B\)
fixed. The new parent count is

\[
                         V(Q)+W_B+C(Q)U_B.                      \tag{11}
\]

Global minimality of \(P\) makes (11) at least (2), proving (3). Replacing
\(B\) proves (4). This uses a physical reembedding, not a formal profile
comparison.

Fix \(x\in A\), put \(Q=A-x\), and abbreviate

\[
 d_x=\{W_A-V(Q)\}+U_B\{C_A-C(Q)\}.                              \tag{12}
\]

There are two canonical ways to restore one point.

First use \(Q\prec\{s\}\). The exact recurrences give

\[
\begin{aligned}
 V(Q\prec\{s\})-V(Q)&=1+C(Q),\\
 C(Q\prec\{s\})-C(Q)&=1+C(Q).
\end{aligned}
\]

Second use \(\{s\}\prec Q\):

\[
\begin{aligned}
 V(\{s\}\prec Q)-V(Q)&=1+U(Q),\\
 C(\{s\}\prec Q)-C(Q)&=a.
\end{aligned}
\]

Minimality of (3) therefore gives the pointwise inequality

\[
 d_x\le\min\bigl\{
       (1+U_B)(1+C(Q)),\,
       1+U(Q)+aU_B
                    \bigr\}.                                   \tag{13}
\]

The symmetric calculation for \(y\in B\), \(R=B-y\), and

\[
 e_y=\{W_B-V(R)\}+C_A\{U_B-U(R)\}                               \tag{14}
\]

is

\[
 e_y\le\min\bigl\{
       (1+C_A)(1+U(R)),\,
       1+C(R)+bC_A
                    \bigr\}.                                   \tag{15}
\]

If either inequality fails for one label, the displayed singleton
replacement of that child gives a literal \(V\)-decreasing reembedding of
the whole parent.

## 2. Summed rank-moment inequalities

The deletion identities inside \(A\) are

\[
\begin{aligned}
 \sum_x\{W_A-V(A-x)\}&=\mu_AW_A,\\
 \sum_x\{C_A-C(A-x)\}&=M_C(A),\\
 \sum_xC(A-x)&=aC_A-M_C(A),\\
 \sum_xU(A-x)&=aU_A-M_U(A).                                   \tag{16}
\end{aligned}
\]

Sum the two branches of (13) separately and apply (16). This proves the
first two lines of (6). The same calculation in \(B\) proves the last two.

Dropping the nonnegative endpoint moments from the second and fourth lines
gives (7). The weaker but sometimes convenient necessary conditions

\[
\boxed{
 W_A\le a+aU_A+U_Ba^2,\qquad
 W_B\le b+bC_B+C_Ab^2
}                                                              \tag{17}
\]

follow from \(\mu_A,\mu_B\ge1\). They already detect the scalar endpoint
equality obstruction.

### The previous scalar equality family is nonminimal

That family has \(a=b=m\) and

\[
\begin{array}{c|ccc}
 &W&C&U\\ \hline
 A&(m+1)t^2&t&(m+1)t\\
 B&(m+1)t^2&(m+1)t&t.
\end{array}                                                     \tag{18}
\]

The first condition in (17) would require

\[
             (m+1)t^2\le m+(2m^2+m)t.                           \tag{19}
\]

At \(t_0=m(m+1)/2=m+\binom m2\), four times the difference between the
left and right sides is

\[
              m^2(m+1)(m^2-2m-1)-4m>0\qquad(m\ge3).             \tag{20}
\]

The difference increases for \(t\ge t_0\). Hence (19) fails throughout
the advertised parameter range. If an actual child had the profiles (18),
some singleton child replacement would decrease its strong-glue parent.

This does not disprove the parent endpoint-reset theorem; it removes only
its abstract equality calibration after the additional global-minimizer
hypothesis is imposed.

## 3. Exact wall trichotomy

Reflecting a child interchanges its cap and cup profiles without changing
its ordinary-face count. The four reflection states of (1) have mixed
terms

\[
        C_AU_B,\qquad U_AU_B,\qquad C_AC_B,\qquad U_AC_B.        \tag{21}
\]

Global minimality implies that the current term is no larger than each of
the other three. In particular, (9) holds.

Let \(F(n)\) be the forbidden parent target and assume
\(V(P)<F(n)\). Double reflection gives a configuration \(P^\star\) with

\[
 V(P^\star)=W_A+W_B+U_AC_B
            =V(P)+\Delta_{\rm wall}.                            \tag{22}
\]

If (9)--(10) satisfy

\[
                       0\le\Delta_{\rm wall}<S_{\rm par},       \tag{23}
\]

then \(V(P^\star)<F(n)\). If \(n\) was the least bad size, every proper
restriction of \(P^\star\) still satisfies the inductive lower target.
Thus the full argument may restart in \(P^\star\), where the mixed term
\(U_AC_B\) is an actual injective ordinary-face bank.

There is a useful quantitative special case. Suppose

\[
\begin{gathered}
 U_B\le {W_A\over4a^2},\qquad
 C_A\le {W_B\over4b^2},\\
 W_A\ge4a,\qquad W_B\ge4b.                                     \tag{24}
\end{gathered}
\]

If no singleton mutation decreases the parent, (7) and
\(\mu_A,\mu_B\ge1\) give

\[
               U_A\ge {W_A\over2a},\qquad
               C_B\ge {W_B\over2b},\qquad
               U_AC_B\ge {W_AW_B\over4ab}.                     \tag{25}
\]

If both induced banks are live in the sense that

\[
                 W_A,W_B\ge {V(P)\over(\log n)^D},              \tag{26}
\]

then

\[
 {U_AC_B\over V(P)}
 \ge {V(P)\over4n^2(\log n)^{2D}}.                              \tag{27}
\]

At any quadratic logarithmic face scale, (27) is much larger than every
fixed polylogarithm. Therefore the reflected state is dominated by its
ordinary mixed bank. The sole issue is the wall cost (23), not bank
capacity after reflection.

If either inequality in the first line of (24) fails, the state has a
large facing profile on one side. If their product already obeys

\[
                         C_AU_B\ge {V(P)\over(\log n)^K},        \tag{28}
\]

the original configuration itself has the desired polylog-density mixed
bank. Otherwise one obtains a quantitatively skew pair of facing profiles.
This is the one-sided endpoint-skew residue.

## 4. Why the parent fixed-gap upper does not pay the wall

The strict upper \(V(P)<F(n)\) controls only the nonnegative slack (10);
it gives no lower bound on it. Even a mutation increasing \(V\) by one can
leave the counterexample class.

More strongly, the live child lower bounds make the opposite wall
potentially much larger than the target. For a calibration take

\[
 a=b=2^{L-1},\qquad
 W_A=W_B=2^{c(L-1)^2},\qquad C_A=U_B=1,                         \tag{29}
\]

with \(0<c<1/2\). Equations (25) force an opposite product on the scale

\[
            {W_AW_B\over4ab}
              =2^{2c(L-1)^2-2L+O(1)},                           \tag{30}
\]

whereas the parent target has logarithm \(cL^2\). For large \(L\), (30)
exceeds the target by \(cL^2-O(L)\) bits. Hence the full opposite
reflection is not a gap-budgeted move, despite its excellent mixed bank.

The numbers in (29) are a scalar capacity calibration, not a planar
profile claim. They show that the fixed-gap upper and the child lower
bounds point in opposite directions for paying the wall.

## 5. Exact Pascal mutation audit

For the rational central split

\[
                         T(6,3)=T(5,2)\prec T(5,3),              \tag{31}
\]

the exact child profiles are

\[
\begin{array}{c|ccc}
 &W&C&U\\ \hline
 T(5,2)&375&101&170\\
 T(5,3)&375&170&101.
\end{array}                                                     \tag{32}
\]

The parent has

\[
 V=10951,\qquad
 (C_AU_B,U_AU_B,C_AC_B,U_AC_B)
       =(10201,17170,17170,28900).                              \tag{33}
\]

Thus the displayed all-delete orientation is already reflection-minimal.
Nevertheless it is not globally minimal. In the left child,
\(\mathcal J_A=W+101C\) has value \(10576\). For every label, the second
singleton replacement in (13) has value between \(8758\) and \(9535\).
It decreases the whole parent by \(1041\) to \(1818\). The right child is
symmetric.

This exact audit confirms that weighted child minimality is strictly
stronger than reflection minimality and removes the finite Pascal
stationary calibration. It does not prove the same decrease for every
large coherent all-delete wrapper.

## 6. Remaining theorem

For a globally minimal fixed-gap counterexample, a literal stationary
strong-glue all-delete seam must satisfy all of (6), reflection minimality
(21), and the parent upper. The exact unresolved states are:

1. a one-sided facing-profile skew in which (24) fails but (28) remains
   small; or
2. a balanced small-facing state satisfying (25) whose opposite mixed bank
   is trapped behind the high wall
   \(\Delta_{\rm wall}\ge S_{\rm par}\).

Closing either state requires a mutation path whose *maximum prefix cost*
is controlled, or a circuit converter which realizes a portion of the
opposite bank without crossing the whole reflection wall. Singleton
minimality, the scalar endpoint reset, and the current deletion forest do
not provide that path.

For a cage which is not already a literal strong glue, equations (3)--(6)
are conditional on first promoting it to a physical two-block replacement
chart. The common-edge trace matching alone does not prove that promotion.

## 7. Verification

Run:

    python3 agent_outer_internal_product/verify_stationary_all_delete_weighted_profile_mutation_gate.py

The verifier:

1. checks every strong-glue and weighted singleton formula symbolically on
   thousands of integer profile rows;
2. proves (20) exactly for \(3\le m\le200\) and checks monotonicity in
   \(t\);
3. reconstructs the rational \(T(6,3)\) cell, all child face/cap/cup
   profiles and rank moments, and every one-point weighted child mutation;
4. recovers the decreases \(1041,\ldots,1818\) and all four reflection
   products in (33); and
5. audits the conditional wall and fixed-gap scale inequalities through
   \(L=512\).

It prints PASS.
