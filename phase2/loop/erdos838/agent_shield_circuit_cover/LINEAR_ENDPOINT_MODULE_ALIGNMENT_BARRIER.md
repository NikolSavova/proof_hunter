# Linear endpoint modules: exact cross-role alignment barrier

**Date:** 2026-08-15. This continues
COHERENT_RAMP_ENDPOINT_MODULE_LOCALIZATION.md. The setting is genuine
linear strong glue only.

## Verdict

Cross-role endpoint alignment cannot close the coherent-ramp residue.
This is not merely a failure of one proposed proof: in the pure linear
model the first-cap/last-cup recurrence is the **entire** ordinary-face
set.

More strongly, one may prescribe arbitrary rational metric slopes for
the selected rooted endpoint chords in all roles, including making them
perfectly equal, without changing the labeled parent chirotope. Hence:

* perfect metric alignment creates no additional multi-role faces;
* complete metric anti-alignment creates no new circuit or seam class;
* every chirotope-defined tangent state is already fixed by the linear
  block orientation law; and
* a short coherent-ramp recurrence cannot recover its
  \(D^{\Theta(\log q)}\) deficit by rerouting or reclassifying endpoint
  modules across macro roles.

The live gate is therefore internal to a child:

> Can a low-face planar child have a
> \(D^{-O(\log q)}\)-dense common-endpoint cap/cup product in both
> projections without either an internal face surplus or a structured
> reset in another projection chamber?

The earlier endpoint-module theorem makes this internal alternative
unavoidable on \((1-o(1))q\) roles. The present report proves that the
macro linear seams add nothing further.

This is a sharp barrier, not a scalable sub-half construction. It does
not realize the formal constant-\(y_i\) child profiles; it proves that
**if** those profiles are realizable, cross-role endpoint geometry in the
same linear chart cannot rule them out.

## 1. The exact oriented linear model

Let \(X_0,\ldots,X_{q-1}\) be planar general-position blocks, each in an
increasing \(x\)-chart. A direct rational realization of their linear
strong glue is obtained as follows.

First apply an orientation-preserving vertical shear to role \(i\),

\[
                         (x,y)\longmapsto(x,y+t_i x),              \tag{1}
\]

and then place it near the \(i\)-th point of a macro parabola:

\[
 (x,y)\in X_i\longmapsto
 \bigl(i+\varepsilon^2x,\ i^2+\varepsilon(y+t_i x)\bigr).         \tag{2}
\]

For every finite rational list \(t_0,\ldots,t_{q-1}\), a sufficiently
small rational \(\varepsilon>0\) gives the oriented block law

\[
\begin{array}{c|c}
\text{roles of an increasing triple}&\text{orientation}\\ \hline
i<j<k&+\\
i=i<k&-\\
i<j=j&+
\end{array}                                                       \tag{3}
\]

while triples internal to \(X_i\) retain their original orientation.

Indeed, three distinct roles converge after rescaling to three points of
the parabola, so their determinant is positive. A pair internal to one
role has \(x\)-difference of order \(\varepsilon^2\) and
\(y\)-difference of order \(\varepsilon\); its slope is of order
\(\varepsilon^{-1}\), while every macro seam has bounded slope. This
gives the last two signs in (3). All inequalities are strict, so a
rational \(\varepsilon\) exists.

The distinguished endpoint chord \(e_i=(a_i,b_i)\) has parent slope

\[
 \frac{(b_i)_y-(a_i)_y+t_i((b_i)_x-(a_i)_x)}
      {\varepsilon((b_i)_x-(a_i)_x)}.                             \tag{4}
\]

Thus its slope can be prescribed arbitrarily above the finite internal
slope threshold by choosing \(t_i\), and then choosing
\(\varepsilon\) smaller. In particular all \(q\) slopes may be exactly
equal, or may follow any strict rational order.

The shears (1) preserve every local orientation, cap, cup, ordinary
face, and fixed-endpoint module. Formula (3) shows that the full labeled
parent chirotope is independent of the chosen slope itinerary.

## 2. Exact face classification

For a nonempty subset \(F\) meeting at least two roles, let \(i\) and
\(j\) be its first and last occupied roles. The oriented law (3) gives
the exact equivalence

\[
\begin{split}
 F\text{ is ordinary}\quad\Longleftrightarrow\quad&
 F\cap X_i\text{ is a cap},\\
 &F\cap X_j\text{ is a cup},\\
 &|F\cap X_r|\le1\quad(i<r<j).
\end{split}                                                       \tag{5}
\]

If \(F\) meets only \(X_i\), it is ordinary precisely when it is an
ordinary face of \(X_i\). Therefore, writing
\(D_r=|X_r|\) and \(C_i,U_i,H_i\) for the local counts,

\[
 \boxed{
 W_{\rm lin}=\sum_iH_i+
 \sum_{0\le i<j<q}C_iU_j
       \prod_{i<r<j}(1+D_r).}                                    \tag{6}
\]

This is equality, not a lower bound.

One can prove (5) directly from (3). On the upper and lower hull walks,
the first occupied role can contribute only a negative-turn chain, the
last only a positive-turn chain, and two points in an intermediate role
force one of them behind the macro hull. Conversely the three displayed
conditions concatenate the two boundary chains with the intervening
singletons, and every chosen point is exposed. This is the standard
first-cap/last-cup characterization.

Now take in every role the common-endpoint module
\(\mathcal C_{i,e_i}\times\mathcal U_{i,e_i}\) supplied by
COHERENT_RAMP_ENDPOINT_MODULE_LOCALIZATION.md. Even when all endpoint
chords in (4) are exactly aligned, (5) forbids:

* a full module face in an intermediate role;
* a cup part in the first occupied role; and
* a cap part in the last occupied role.

The only admissible cross-role use is already the term
\(C_iU_j\prod_r(1+D_r)\) in (6). Restricting to the rooted modules only
shrinks that term.

## 3. Why a seam/circuit split also cannot help here

The aligned and anti-aligned realizations above have identical labeled
chirotopes. Consequently they have exactly the same:

* ordinary faces and nonfaces;
* \(1+3\) and \(2+2\) circuit supports and signs;
* tangent-neighbor states defined by orientation predicates; and
* source/target decoders based on physical labels.

Thus changing or binning the metric endpoint slopes cannot expose a
new bounded-load circuit bank. Any such bank present after
anti-alignment is already present, with the same labels and load, after
perfect alignment.

There can still be a useful seam/circuit theorem if it uses additional
geometry **inside** a child or compares a second projection chamber.
What is ruled out is a theorem whose input consists only of:

1. the actual linear block law (3);
2. the role profiles \(C_i,U_i,H_i\);
3. one large rooted endpoint product per role; and
4. tangent data in the same construction chart.

For those data, (6) is an exact cardinality certificate.

## 4. Coefficient consequence

In the coherent-ramp scalar regression, equal role size \(D=2^d\) and
\(q=\Theta(d)\) give

\[
                         W_{\rm lin}\le2qD^{d/2},                 \tag{7}
\]

whereas the coefficient-half parent threshold exceeds this by

\[
                         D^{(1-o(1))\log q}.                      \tag{8}
\]

The endpoint localization theorem loses only
\(D^{O(\log q)}\), so it is quantitatively meaningful, but (6) proves
that no same-chart cross-role composition can turn that localization
into the missing factor. A successful continuation must contradict the
local profile menu itself.

A precise surviving internal problem is:

* \(X\) has \(D\) points and fewer than the desired surplus number of
  ordinary faces;
* \(C U/H\le D^{O(\log q)}\);
* one endpoint \(e\) supports
  \(D^{-O(\log q)}\) fractions of both cap and cup alphabets and at least
  \(H/(2D^2)\) ordinary product faces;
* decide whether another projection direction has a larger
  cap/cup/face bank, or whether the two hereditary side complexes around
  \(e\) force an internal detached bank.

That statement is genuinely about planar child structure. It does not
reinvoke the retracted cyclic endpoint factorization.

## 5. Scalable status

Construction (2) works for arbitrary \(q\), arbitrary finite planar
children, and arbitrary finite rational slope itineraries. It is
therefore a scalable exact regression against macro tangent alignment.

It is not a sub-half family because the children were left arbitrary.
To turn it into one would require choosing children that realize the
constant-\(y_i\), low-\(H_i\) menu at every recursive scale, which is
exactly the unresolved internal problem rather than a consequence of
the glue.

## 6. Verification

Run

    python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_linear_endpoint_module_alignment_barrier.py

The exact rational verifier uses three nonisomorphic four-point child
profiles. It checks all \(2^{12}-1\) nonempty parent subsets against
(5), checks (6), checks each rooted cap/cup product, and constructs:

1. a realization in which all three endpoint slopes are exactly equal;
2. a realization in which all three slopes are distinct; and
3. an exact equality of the two labeled chirotopes.

Expected output:

    PASS: exact linear recurrence and trace classification, aligned and free endpoint-slope itineraries have identical chirotope; profiles=[(13, 11, 14), (11, 13, 14), (12, 12, 15)], modules=[(3, 1), (1, 3), (2, 2)], faces=1124, aligned_slope=20000000, free_slopes=[Fraction(93000000, 7), Fraction(267000000, 7), Fraction(162000000, 7)]
