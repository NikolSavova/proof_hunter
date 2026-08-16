# Coherent ramps require a two-chart Bellman reset

**Date:** 2026-08-15. All logarithms are base two unless a base is
displayed. This continues *ITERATED_FEW_RUN_LOAD_PROFILE_GATE* and
cross-audits *LINEAR_ENDPOINT_MODULE_ALIGNMENT_BARRIER* and the sampled
404-point menu.

## Verdict

The constant-potential ramp is not recursively closed in its own linear
assembly chart. There is an exact large obstruction which is invisible in
the ordinary-face recurrence.

Let \(q\) equal-sized \(D\)-point children be put in the right-associated
linear comb

\[
             X_0\prec(X_1\prec(\cdots\prec X_{q-1})).
\]

This is also the direct macro-parabola law with all distinct-role triples
positive. Besides the ordinary-face recurrence, the parent cap and cup
counts in that same chart satisfy

\[
\begin{aligned}
 C^+&=\sum_{i=0}^{q-1}C_i\{1+(q-1-i)D\},\\
 U^+&=\sum_{j=0}^{q-1}U_j(1+D)^j.                       \tag{1}
\end{aligned}
\]

For a perfect ramp

\[
 H_i=D^h,\qquad C_i=D^{a+i},\qquad U_i=D^{h-a-i},       \tag{2}
\]

put

\[
\begin{aligned}
 S_{q,D}&=\sum_{j=0}^{q-1}\left(D^{-j}+jD^{1-j}\right),\\
 T_{q,D}&=\sum_{j=0}^{q-1}(1+D^{-1})^j.                 \tag{3}
\end{aligned}
\]

Then, for every shift \(a\),

\[
\begin{aligned}
 W^+&=qD^h+{D^h\over D}
       \sum_{k=1}^{q-1}(q-k)(1+D^{-1})^{k-1},\\
 C^+&=D^{a+q-1}S_{q,D},\\
 U^+&=D^{h-a}T_{q,D}.                                   \tag{4}
\end{aligned}
\]

If \(D\ge q^2\) and \(q\ge2\), then

\[
 qD^h\le W^+\le2qD^h,\qquad
 2\le S_{q,D}<4,\qquad q\le T_{q,D}<2q.                 \tag{5}
\]

Consequently the assembly-chart endpoint surplus is

\[
 s_{\rm asm}:=\log_D{C^+U^+\over W^+}
                 =q-1+O(1/\log D).                     \tag{6}
\]

At the next unpaid coherent-ramp level, the surplus telescope says that
almost every child must instead have

\[
                    s\le2T=O(\log q).                   \tag{7}
\]

Thus a recursively surviving parent must be recharted to a direction
\(\beta\) for which

\[
\boxed{\quad
 \log_D{C_\beta U_\beta\over W^+}\le O(\log q),\qquad
 \log_D{C^+U^+\over C_\beta U_\beta}
                  \ge q-O(\log q).
\quad}                                                  \tag{8}
\]

This is a drop by \(D^{q-O(\log q)}\), much larger than the
\(D^{\Theta(\log q)}=n^{\Theta(\log\log\log n)}\) multiplier still needed
by the parent target. Changing the shift \(a\) changes the imbalance but
does not change this tax.

Therefore a valid recursive state is not \((W,C,U)\), nor a rooted
endpoint module in one chart. The smallest exact state established here is
a **two-chart seam-jet Bellman state**

\[
 \mathcal B(P;\alpha,\beta)=
 (W(P),\mathcal J_\alpha(P),\mathcal J_\beta(P),
       \omega_{\alpha\beta}),                           \tag{9}
\]

where \(\alpha\) is the construction chart, \(\beta\) is the exported
reset chart, and \(\omega_{\alpha\beta}\) records the macro projection
chamber (block order and seam signs) seen at \(\beta\).
\(\mathcal J_\theta\) is the finite table of cap/cup traces by their first
two and last two physical labels in \(\theta\)-order, with sentinels for
ranks zero and one. Its scalar marginals include

\[
 s_\theta=\log_D{C_\theta U_\theta\over W(P)},\qquad
 \rho_\theta={1\over2}\log_D{U_\theta\over C_\theta}.    \tag{10}
\]

The coherent ramp requires both the large surplus reset (8) and graded
values of \(\rho_\beta\), up to the known \(O(\log q)\) slack.

This is alternative (iii), not a coefficient-half proof. The exact missing
theorem is:

> Show that no induction-minimal planar child produced by an unpaid
> \(q\)-role ramp has an exported chamber with the reset (8) and the needed
> imbalance, or show that those chambers carry a second ordinary-face bank.

The same-chart alignment barrier does not address this question: metric
endpoint slopes can vary without changing the chirotope, whereas (8)
compares two projection chambers of the same child.

There is an important association correction. For the left-associated
comb \(((X_0\prec X_1)\prec\cdots)\prec X_{q-1}\), the simultaneous
formulas are

\[
 C^{\rm L}=\sum_i(1+D)^{q-1-i}C_i,\qquad
 U^{\rm L}=\sum_i\{1+iD\}U_i.                           \tag{11}
\]

Thus the product-weighted cap formula and product-weighted cup formula
belong to opposite associations. No one actual chart has both of them.
For the ramp (2), the left comb merely swaps \(S_{q,D}\) and \(T_{q,D}\)
in (4), so (6)--(8) are unchanged. Both comb associations have the same
ordinary-face recurrence (15).

The exact \(q=3,D=4\) verifier uses local profiles
\((13,11,14),(11,13,14),(12,12,15)\). It finds

\[
\begin{array}{c|c}
\text{actual association}&(C,U,W)\\ \hline
X_0\prec(X_1\prec X_2)&(184,376,1124)\\
(X_0\prec X_1)\prec X_2&(392,184,1124).
\end{array}
\]

The simultaneously product-weighted prediction \((392,376,1124)\) is
therefore not the profile of either actual chart.

## 1. Exact recurrences

Use the oriented linear block law

\[
 \chi(i,j,k)=+\quad(i<j<k),\qquad
 \chi(i,i,k)=-,\qquad \chi(i,j,j)=+.                    \tag{12}
\]

A cap meeting at least two roles cannot meet three. If its first and last
roles are \(i<j\), the last role is a singleton. Conversely any cap in
\(X_i\), together with one point of \(X_j\), is a cap. Therefore

\[
             C^+=\sum_iC_i+\sum_{i<j}C_iD_j.            \tag{13}
\]

A cup may meet any number of roles, but every occupied role except the
last is a singleton; the trace in the last role is a cup. Hence

\[
             U^+=\sum_jU_j\prod_{i<j}(1+D_i).           \tag{14}
\]

These are exact chain classifications, not arbitrary endpoint
factorization. The ordinary-face recurrence is

\[
 W^+=\sum_iH_i+\sum_{i<j}C_iU_j(1+D)^{j-i-1}.           \tag{15}
\]

Substitution of (2) gives (4). In particular

\[
 {C^+\over U^+}
    =D^{2a+q-1-h}{S_{q,D}\over T_{q,D}},\qquad
 C^+U^+=D^{h+q-1}S_{q,D}T_{q,D}.                        \tag{16}
\]

Thus \(a\) moves the imbalance but not the surplus tax. For \(D\ge q^2\),
the cross part of \(W^+\) is at most \(D^h\). Also

\[
 2\le S_{q,D}
 <\sum_{j\ge0}D^{-j}+\sum_{j\ge0}jD^{1-j}<4,            \tag{17}
\]

and every summand of \(T_{q,D}\) lies in
\([1,(1+D^{-1})^{q-1})\subset[1,2)\). Therefore

\[
                  q-1\le s_{\rm asm}
                     <q-1+\log_D8.                     \tag{18}
\]

which proves (6).

## 2. Why two charts and seam jets are necessary

A one-level face proof queries only the construction direction \(\alpha\),
so \((W,C_\alpha,U_\alpha)\) suffices for (15). Recursion queries the
completed parent again in a possibly different direction \(\beta\).
Ordinary-face count \(W\) is chart-invariant, but \(C\) and \(U\) are not.

For a trace in a generic direction, being a cap or cup is equivalent to
the corresponding sign condition on every consecutive turn. When
separated blocks are concatenated, all turns internal to a block are
certified by its local chain type. At each occupied-block seam, only the
last two labels on the left and first two labels on the right occur in the
new turns. Therefore the finite contraction of the child jet tables
\(\mathcal J_\theta\), using the signs in \(\omega\), computes the exact
parent cap/cup counts in that chamber. There are only \(O(|P|^4)\) possible
four-label jets per chain type. This proves that (9) is an exact
finite-dimensional Bellman state for two prescribed, block-separated
query directions. Total \(C\) and \(U\) alone are insufficient outside
the uniform linear law because they forget these seam compatibilities.

An orientation-preserving projective map is transitive on ordered pairs of
distinct directions. Hence a copy can calibrate its construction and one
future reset direction independently. This kills a false many-direction
coherence argument, but does not erase (9): the second jet table depends
on the actual macro chamber and the child reset profiles.

If \(\beta\) sees the same linear block law and its child profiles again
form an unpaid ramp, (4) reproduces the tax (18). A successful reset must
therefore use a genuinely different macro chamber, or child reset profiles
outside the constant-potential regime.

Along a construction branch, the exported \(\beta\) becomes the
construction chart at the next level. Thus two marked jet tables compose
by identifying the second mark of a child with the first mark of its
parent. No older chart need be retained. Two marks suffice for one path
and are necessary for the reset; a claimed \(q\)-mark PGL constraint would
overstate the recursion.

## 3. Sampled 404-point calibration

The current exact 512-direction audit of the 134-point \(W_3\) child gives

\[
 W_3=11358202734,\qquad
 \min_{\rm sample}CU=2562123\cdot33305052
                   =85331639745396.                     \tag{19}
\]

Using child size \(134\), the minimum sampled surplus is

\[
 \log_{134}(85331639745396/W_3)=1.8221013266\ldots.      \tag{20}
\]

The sampled extreme profiles

\[
 (1118689,355504811),\qquad(355504811,1118689)           \tag{21}
\]

have \(\log_{134}(C/U)\) values \(-1.1763106907\ldots\) and
\(+1.1763106907\ldots\). The exact 404-point recurrence uses these extrema
and \((3842402,27715665)\), giving

\[
 W_{4,\rm sample}=204331272672794,\qquad
 {\log W_{4,\rm sample}\over(\log404)^2}
                   =0.634137803895\ldots.               \tag{22}
\]

Thus the finite menu genuinely contains useful reset directions; one-chart
data misses the improvement. But \(q=3\), the sampled surplus stays of
constant order, and the imbalance width is only \(2.35262\ldots\). It
neither proves nor refutes the asymptotic reset (8).

These figures supersede the older 128-direction sample: the current
verifier uses 512 proposed directions and 894 certified profiles.

## 4. Exact remaining alternatives

Any one of the following would finish this branch.

1. **Reset-surplus rigidity:** every exported chamber of a live ramp has
   \(s_\beta>2T\), except for a family with a bounded-load ordinary bank.
2. **Reset-width payment:** chambers satisfying (8) with the required
   graded imbalances generate \(D^{\Omega(\log q)}\) additional faces.
3. **Decorated construction:** a rational recursive family realizes the
   seam-jet states (9), with (8) at every level and a closed full-face
   recurrence.

The universal inequality \(CU\ge W\), same-chart metric alignment, and
arbitrary endpoint factorization prove none of these. The 404-point sample
also shows that a valid rigidity theorem must be asymptotic or charge the
whole chamber menu rather than forbid one reset.

## 5. Verification

Run

~~~text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_coherent_ramp_two_chart_bellman_gate.py
~~~

The verifier exhausts the cap/cup classification for a rational 12-point
right comb and an independently nested left comb, checks (1), (11), and
(15), verifies (3)--(6) for integral formal ramps, and checks the current
894-profile numerical calibration.
