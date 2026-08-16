# Coherent ramp: surplus telescope and rooted endpoint modules

**Date:** 2026-08-15. All logarithms are base two. This continues
FIXED_GAP_LINEAR_PROFILE_POTENTIAL.md and uses only genuine **linear
strong glue**. No cyclic omitted-gap profile factorization is used.

## Verdict

The formal constant-\(y_i\) ramp cannot also carry large
upper/lower-hull encoding surplus on many roles.

Let \(X_0,\ldots,X_{q-1}\) be planar children of common size \(D\ge3\)
in one recoverable first-cap/last-cup strong-glue chart. Write
\(C_i,U_i,H_i\) for the nonempty cap, cup, and ordinary-face counts of
\(X_i\), and put

\[
 A_i=\log_D C_i,\quad B_i=\log_D U_i,\quad
 h_i=\log_D H_i,\quad y_i=A_i-i,\quad
 s_i=A_i+B_i-h_i=\log_D\frac{C_iU_i}{H_i}.                       \tag{1}
\]

The hull encoding gives \(s_i\ge0\). Suppose the child induction gives
\(H_i\ge D^h\), the desired parent threshold is \(D^P\), and set

\[
                         T=P-h+1.                                 \tag{2}
\]

If neither a child nor any first-cap/last-cup cross-bank reaches
\(D^P\), then

\[
                    s_j+y_i-y_j<T\qquad(0\le i<j<q),              \tag{3}
\]

and the positive surplus above \(T\) telescopes:

\[
              \boxed{\displaystyle
              \sum_{j=1}^{q-1}(s_j-T)_+<P-1.}                    \tag{4}
\]

Consequently

\[
 \#\{j\ge1:s_j\ge2T\}<\frac{P-1}{T}.                             \tag{5}
\]

At the fixed gap \(q=\Theta(d)\), \(P=\Theta(d)\), and
\(T=\Theta(\log q)\), only \(O(d/\log q)=o(q)\) roles can have
\(s_j>2T\). Thus almost every role satisfies

\[
                         \frac{C_jU_j}{H_j}\le D^{2T}.             \tag{6}
\]

This scalar near-surjectivity has an exact planar consequence. For each
role satisfying (6), there is one actual left/right endpoint pair
\(e_j\) such that, among all nonsingleton cap and cup chains,

\[
 \frac{C_{j,e_j}}{C_j-D}\ge D^{-(2T+3)},\qquad
 \frac{U_{j,e_j}}{U_j-D}\ge D^{-(2T+3)}.                          \tag{7}
\]

Moreover every pair consisting of one such cap and one such cup has
ordinary union, and this union map is injective. Hence (7) is a genuine
rooted two-ended product module, not a formal profile statistic.

For the coefficient-half fixed gap, \(T=(1+o(1))\log q+1\). The loss in
(7) is therefore \(D^{O(\log q)}=n^{O(\log\log n)}\), exactly at the
scale of the missing multiplier.

This is positive structural progress, not yet closure. The selected
endpoint pair may depend arbitrarily on the role, and the module faces
are already counted inside \(H_j\). A final theorem must align these
rooted modules across roles or show that their failure to align creates
additional ordinary cross-role faces.

## 1. Exact surplus in the linear bank

For \(i<j\), the strong-glue recurrence contains

\[
                         C_iU_jD^{j-i-1}                           \tag{8}
\]

ordinary faces, using one label in every intermediate role. Its
base-\(D\) exponent is exactly

\[
\begin{aligned}
 A_i+B_j+j-i-1
 &=h_j+s_j+A_i-A_j+j-i-1\\
 &=h_j+s_j+y_i-y_j-1.                                            \tag{9}
\end{aligned}
\]

Since \(h_j\ge h\), condition

\[
                         s_j+y_i-y_j\ge T                         \tag{10}
\]

makes (9) at least

\[
                         h+T-1=P.                                \tag{11}
\]

Thus one actual ordered role pair closes the parent target, with decoder
load one. Its contrapositive is (3).

This strengthens the earlier drop theorem: a right-child surplus \(s_j\)
is interchangeable with a downward cap-potential drop. In particular,
the exact constant-\(y\) scalar ramp can remain unpaid only if every
usable right child has \(s_j<T\).

## 2. Prefix-maximum telescope

Let

\[
                       M_j=\max_{0\le i\le j}y_i.                 \tag{12}
\]

Taking the maximum over \(i<j\) in (3) gives

\[
                       y_j>M_{j-1}+s_j-T.                         \tag{13}
\]

Whenever \(s_j>T\), role \(j\) sets a new prefix maximum and

\[
                       M_j-M_{j-1}>s_j-T.                         \tag{14}
\]

These increments are disjoint, so

\[
 \sum_{j=1}^{q-1}(s_j-T)_+<M_{q-1}-M_0.                          \tag{15}
\]

Every cap is itself an ordinary face, hence \(C_i\le H_i\). Since no
local child closes the target, \(h_i<P\), so \(A_i<P\). Also every
singleton is a cap, so \(A_0\ge1\). Therefore

\[
                       M_{q-1}<P,\qquad M_0\ge1.                  \tag{16}
\]

Equations (15)--(16) prove (4), and (5) follows because every term with
\(s_j\ge2T\) contributes at least \(T\).

The asymmetry at \(j=0\) is real: the first role is never the right
endpoint of (8). Losing one role is harmless at fixed-gap scale.

## 3. Exact endpoint factorization inside one planar child

Fix a planar general-position set \(X\) of size \(D\) and a generic
horizontal direction. A cap or cup of rank at least two has a unique
ordered pair \(e=(a,b)\) of leftmost and rightmost endpoints. Let
\(C_e,U_e\) count cap and cup chains with exact endpoints \(e\), and put

\[
 \bar C=C-D=\sum_e C_e,\qquad
 \bar U=U-D=\sum_e U_e,\qquad
 \bar H=H-D.                                                       \tag{17}
\]

Every ordinary face of rank at least two has a unique upper cap and
lower cup with the same endpoint pair. Conversely, the union of any cap
and cup with the same endpoints is ordinary. Therefore

\[
                         \boxed{\bar H=\sum_e C_eU_e}.             \tag{18}
\]

The map from the disjoint union of rectangles
\(\bigsqcup_e(\mathcal C_e\times\mathcal U_e)\) to nonsingleton ordinary
faces is a bijection.

Normalize

\[
 p_e=\frac{C_e}{\bar C},\qquad q_e=\frac{U_e}{\bar U},\qquad
 \bar s=\log_D\frac{\bar C\bar U}{\bar H}.                         \tag{19}
\]

Equation (18) becomes

\[
                         \sum_e p_e q_e=D^{-\bar s}.              \tag{20}
\]

There are fewer than \(D^2\) endpoint pairs. Hence some \(e\) obeys

\[
 p_e q_e\ge D^{-(\bar s+2)}.                                    \tag{21}
\]

Since \(p_e,q_e\le1\), each factor is at least the product.
The same endpoint pair also carries a polynomial fraction of all child
faces:

\[
 C_eU_e\ge\frac{\bar H}{\binom D2}>
            \frac{H}{2D^2}.                                     \tag{21a}
\]

Thus the extracted object is simultaneously large as an ordinary-face
module and, when \(s\) is small, large in both directional projections.

For \(D\ge3\), all singletons and pairs are faces, caps, and cups, so
\(H,C,U\ge D(D+1)/2\ge2D\). Consequently

\[
 \bar H=H-D\ge H/2,\qquad
 \bar C\le C,\qquad \bar U\le U,
\]

and

\[
                         \bar s\le s+\log_D2\le s+1.              \tag{22}
\]

Combining \(s\le2T\), (21), and (22) proves (7).

This is the strongest unconditional interpretation of small
\(C U/H\) available from planar hull factorization: it produces a
physical common-endpoint rectangular module. It does **not** by itself
produce extra faces beyond \(H\), because (18) is already an exact
partition of the existing faces.

## 4. Coefficient accounting

Take the live half target

\[
 \Phi(L)=\frac12L^2-O(L\log L),\qquad
 h=\frac{\Phi(d)}d,\qquad
 P=\frac{\Phi(d+\log q)}d.                                       \tag{23}
\]

Then

\[
 T=P-h+1=(1+o(1))\log q+1.                                      \tag{24}
\]

For \(q=\Theta(d)\), (5) leaves at most

\[
             O\!\left(\frac d{\log q}\right)=o(q)                \tag{25}
\]

high-surplus roles. Every other role admits the rooted product module
(7) with exponent loss

\[
                         2T+3=(2+o(1))\log q.                     \tag{26}
\]

Thus a planar realization of the formal coherent ramp would have to
contain \((1-o(1))q\) independently rooted cap/cup rectangles, each
retaining quasipolynomial fractions of both directional alphabets.
Arbitrary scalar menus no longer describe the survivor.

The remaining obstruction is **cross-role root anti-alignment**:
different roles can choose unrelated endpoint pairs and unrelated
projective gauges. The false cyclic endpoint-profile theorem cannot be
used to align them. Any next step must work in the actual linear chart,
for example by:

* extracting many roles whose rooted endpoint modules have one compatible
  tangent state;
* using a failed tangent alignment to create a new seam/circuit bank; or
* proving that an induction-minimal child cannot devote
  \(D^{-O(\log q)}\) fractions of both directional banks to one endpoint
  without an internal face surplus.

## 5. Verification

Run

    python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_coherent_ramp_endpoint_module_localization.py

The verifier uses exact integer/Fraction arithmetic. It:

1. exhausts every subset of three rational seven-point order types;
2. checks the cap/cup endpoint bijection (18), including every product
   union and uniqueness;
3. checks the \(D^2\) endpoint localization; and
4. exhausts 152 rational potential/surplus arrays satisfying the unpaid
   inequalities and verifies the telescope (4).

Expected output:

    PASS: exact endpoint cap/cup bijections, D^2 localization, and prefix-surplus telescope; arrays=152, summaries=[(7, 112, 47, 42, 105, (0, 6)), (7, 100, 43, 41, 93, (0, 6)), (7, 112, 55, 36, 105, (0, 6))]
