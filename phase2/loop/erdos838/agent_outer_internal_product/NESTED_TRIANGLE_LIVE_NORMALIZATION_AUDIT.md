# Nested all-loop arrays at the least-counterexample scale

**Date:** 2026-08-15. All logarithms are base two. This audits
`FIRST_INCOHERENT_SIBLING_NESTED_TRIANGLE_BARRIER.md` after restoring the
three macroscopic vertex clouds and the live source normalization.

## Verdict

The three vertex clouds are a real global payment, but they do not close the
fixed-gap lower bound. If the array has (m) central labels and (k) partner
classes, then its ground size and the size of each vertex cloud are

\[
        N=m(1+3k),\qquad R=km={N\over 3+1/k}.                    \tag{1}
\]

In a least counterexample for

\[
 \Phi_C(L)={L^2\over2}-CL\log L,\qquad F_C(n)=2^{\Phi_C(\log n)}, \tag{2}
\]

each cloud is an induced proper configuration, and hence contributes
(F_C(R)) ordinary faces. Thus the old central-child deficit
(2^{(1+o(1))L\log k}), with (k\asymp\log\log N), is reduced to

\[
 {F_C(N)\over F_C(R)}
       =N^{\log 3-o(1)}.                                      \tag{3}
\]

This is only a fixed polynomial gap, but it is still a genuine fixed-power
gap. The three cloud banks add; no union of two arbitrary cloud faces is
known to be ordinary.

There is also an exact load-one five-point bank. Every circuit record
(E_j(a)=\{y_a\}\cup T_j(a)) and every second central label (y_b),
(b\ne a), canonically give an ordinary four-face containing two central
labels and two vertices of (T_j(a)). These faces are injectively indexed
by ((j,a,b)), so their number is

\[
                         km(m-1)=\Theta(N^2/k).          \tag{4}
\]

This is additive and has logarithm only (2L-O(\log k)); it is negligible
beside the coefficient-half cloud bank. It does not multiply (F_C(R)).

Finally, source normalization does not create such a multiplication. If
weighted source histories of total mass (W) project to the (R=km)
geometric records and (Lambda_{\rm rec}) is the largest record fibre,
then exactly

\[
                         W\le R\Lambda_{\rm rec}.        \tag{5}
\]

On a live slice (W\ge V(P)/Q), (Q=2^{O(L\log L)}), induction on one
macroscopic cloud forces

\[
 \log\Lambda_{\rm rec}\ge {1\over2}L^2-O(L\log L).      \tag{6}
\]

So bounded-load projection is ruled out, but the conclusion is enormous
coalescence over one/few records, not a new ordinary-face bank. Even if one
optimistically grants a separated two-output source--cloud decoder,
Cauchy reduces to (V(P)\ge F_C(R)/(Q\Lambda)), weaker than the induced
cloud bank itself.

The scalar endpoint recurrence has an exact coherent-ramp witness. Even if
the (k) partner classes are additionally granted one genuine linear
strong-glue chart, its exact recurrence can remain only (O(k)) times one
partner-child bank. Taking the maximum with the three-cloud induction bank
leaves precisely (3). Therefore the nested array is not a live sub-half
construction, but neither macroscopic induction, the five-point extension,
nor source projection closes it. The remaining theorem must linearly mix a
macroscopic cloud face with a recoverable external profile, or use a
minimizer mutation excluding the coherent all-loop order.

## 1. Exact macroscopic-cloud and five-point bank

For every record triangle (T_j(a)), label its three vertices arbitrarily
as (t^0_j(a),t^1_j(a),t^2_j(a)), and put

\[
          Z^r=\{t^r_j(a):j\in[k],a\in[m]\},\qquad r=0,1,2. \tag{7}
\]

The sets (Y,Z^0,Z^1,Z^2) are pairwise disjoint, and every (Z^r) has
exactly (R=km) labels. No geometric coherence of the arbitrary vertex
labelling is being assumed. Since an ordinary face of an induced subset is
the identical ordinary subset in the ambient point set,

\[
 V(P)\ge V(Y)+\sum_{r=0}^2V(Z^r).                       \tag{8}
\]

Now fix (j,a) and (b\ne a). The five-set

\[
                    E_j(a)\cup\{y_b\}                  \tag{9}
\]

contains an ordinary four-subset. It cannot be (E_j(a)), which is a bad
(1+3) circuit. It also cannot be (T_j(a)\cup\{y_b\}), because every
central label lies strictly inside every record triangle. Hence an ordinary
four-subset of (9) deletes one triangle vertex and has the form

\[
          \{y_a,y_b\}\cup\bigl(T_j(a)\setminus\{t\}\bigr). \tag{10}
\]

Choose the first such (t) in the fixed physical label order. The two
retained triangle labels determine the unique disjoint record triangle,
hence recover ((j,a)); the other central label then recovers (b).
Therefore (10) has decoder load one.

The outputs in (10) contain central and triangle labels, whereas the four
banks in (8) are supported in one of the four disjoint ground classes.
They are disjoint as families of labelled subsets. We have proved the exact
positive theorem

\[
 \boxed{\quad
 V(P)\ge V(Y)+V(Z^0)+V(Z^1)+V(Z^2)+km(m-1).
 \quad}                                                  \tag{11}
\]

The proof uses only the signed (1+3) type, strict central containment,
and disjoint record triangles. Total nesting is not needed for (11); it is
what destroys complete-triangle mixing.

## 2. Least-counterexample coefficient audit

Assume the whole array has (N=m(1+3k)=\Theta(n)) labels inside an
induction-minimal ambient configuration, so constant changes between
(N) and (n) only change the fixed-power ledger. Put

\[
 L=\log N,\quad
 \beta=\log{N\over R}=\log(3+1/k),\quad
 \alpha=\log{N\over m}=\log(1+3k).                    \tag{12}
\]

For arbitrary (a<L), direct subtraction in (2) gives

\[
 \Phi_C(L)-\Phi_C(L-a)
 =aL-{a^2\over2}
  -C\{L\log L-(L-a)\log(L-a)\}.                       \tag{13}
\]

Applying induction to (11),

\[
 V(P)\ge F_C(m)+3F_C(R)+km(m-1).                       \tag{14}
\]

If (k\asymp\log\log N), then

\[
 \begin{aligned}
 \Phi_C(L)-\Phi_C(L-\alpha)&=(1+o(1))L\log k,\\
 \Phi_C(L)-\Phi_C(L-\beta)&=(\log3)L-O_C(\log L).
 \end{aligned}                                        \tag{15}
\]

Thus the central and individual partner-class induction banks miss the
target by (2^{(1+o(1))L\log k}), while a macroscopic vertex cloud misses
by only (N^{\log3}/(\log N)^{O_C(1)}). The extension term (4) is
(2^{O(L)}), whereas

\[
              \log F_C(R)={1\over2}L^2-O(L\log L).     \tag{16}
\]

Consequently the maximum term in (14) is a cloud bank, and the exact
remaining scale is the fixed power (3). Three copies contribute only the
constant factor three.

This conclusion is robust if the array occupies any fixed positive
fraction of the ambient ground: (R=\Theta(n)) and the exponent in (3)
changes only by another fixed constant. It is not robust if the array is
submacroscopic; the present audit is specifically the live central
(m\asymp n/\log\log n) branch.

## 3. Source projection and the square-root non-payment

Let (mathcal H) be any weighted collection of actual source histories
attached to the array, and let

\[
 \pi:\mathcal H\longrightarrow[k]\times[m]             \tag{17}
\]

be the geometric record remaining after the outside source word is erased.
With total mass (W) and maximum fibre mass

\[
 \Lambda_{\rm rec}=\max_{j,a}\sum_{h:\pi(h)=(j,a)}w(h), \tag{18}
\]

grouping by (17) proves (5). If the preceding live normalization gives
(W\ge V(P)/Q), then (11) gives

\[
 \Lambda_{\rm rec}\ge {F_C(R)\over QR}.                \tag{19}
\]

For (Q=2^{O(L\log L)}), equation (16) proves (6). Hence the geometric
record alphabet has only polynomial size and cannot itself carry the live
mass with quasipolynomial load.

This observation must not be converted into a false product. Suppose,
more strongly than is presently known, that every source occurrence and
every face in one cloud produce an ordered pair of ordinary outputs, with
decoder load at most (Lambda). Writing (H=V(Z^r)), the exact count is

\[
                         WH\le\Lambda V(P)^2.           \tag{20}
\]

Using (W\ge V(P)/Q) yields only

\[
                         V(P)\ge {H\over Q\Lambda},     \tag{21}
\]

which is weaker than (V(P)\ge H). A one-face output of size
(WH/\Lambda) would be decisive, but that is exactly the missing
source/cloud mixing theorem. The nested construction proves its failure
for the complete released triangle: every nonempty central face is
incompatible with it.

## 4. Exact max-plus coherent-ramp witness

The uncontrolled partial triangle traces might conceivably promote the
(k) partner classes into a linear strong-glue chart. Grant this extra
hypothesis. Let every partner child have (D=3m) labels, write (H_i,C_i,
U_i) for its face, cap, and cup counts in that chart, and put (B=D+1).
The exact linear recurrence is

\[
 W_{\rm lin}=\sum_{i=0}^{q-1}H_i+
   \sum_{0\le i<j<q}C_iU_jB^{j-i-1},\qquad q=k.         \tag{22}
\]

Universal cap/cup decomposition gives (H_i\le C_iU_i). These scalar
constraints and (22) still admit an exact coherent ramp. Choose integers
(h>3q) and (b=(h-q)/2) (adjust parity by one), and set

\[
 H_i=B^h,\qquad C_i=B^{b+i},\qquad U_i=B^{h-b-i}.       \tag{23}
\]

Then (C_iU_i=H_i), while every cross term is exactly

\[
                    C_iU_jB^{j-i-1}=B^{h-1}=H_i/B.     \tag{24}
\]

Therefore

\[
 W_{\rm lin}=qB^h+{q(q-1)\over2}B^{h-1}
          \le2qB^h\qquad(B\ge q^2).                   \tag{25}
\]

At (D\asymp N/k), (q\asymp\log\log N), choosing
(h=\Phi_C(\log D)/\log B+O(1)) makes the first term have the inductive
partner-child scale. Its target deficit is
((1+o(1))L\log k), just as in (15). The independent macroscopic cloud
floor (F_C(R)) is much larger and therefore dominates (25), but it has no
certified cross term with another cloud or with the source. In the formal
state (23), the combined scalar ledger is consequently

\[
 {\cal L}_{\rm scalar}:=
 \max\{\log F_C(R),\ \log W_{\rm lin},\ \log(km(m-1))\}
 =\Phi_C(L)-(\log3+o(1))L.                              \tag{26}
\]

Equation (23) is a formal endpoint menu, not a claim that the arbitrary
nested array realizes those profile counts or has no additional ambient
faces. Its role is exact and narrow: the universal scalar constraints plus
the strongest presently justified ordered recurrence admit (26), so those
constraints alone cannot force the missing fixed-power multiplier. A proof
must use more than the three induced face counts, five-point rank-four
faces, source projection, and scalar cap/cup energy.

## 5. Precise remaining interface

The audit separates the nested-array branch as follows.

* **Paid globally:** the three (N/(3+o(1)))-point induced clouds force the
  coefficient-half scale up to (N^{\log3-o(1)}).
* **Paid only additively:** the canonical five-point faces contribute
  (Theta(N^2/k)), far below a cloud bank.
* **Localized, not paid:** live source mass forces a coefficient-half
  record fibre by (19).
* **Still open:** turn that literal high-load fibre into a one-face output
  retaining a macroscopic cloud face and (N^{\log3+o(1)}) recoverable
  external states, or prove that a least-counterexample mutation forbids
  the coherent all-loop nesting.

There is no end-to-end coefficient-half closure here, and the nested array
is not asserted to be a globally low-face construction. The result is a
sharp normalization and max-plus barrier: all currently automatic global
banks stop a fixed power below the target.

## 6. Verification

Run

```text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_nested_triangle_live_normalization_audit.py
```

The checker constructs a rational/integer nested array, verifies the three
cloud sizes and every canonical five-point face with its load-one decoder,
checks the exact source-load and Cauchy algebra, audits (13)--(16) over a
growing asymptotic grid, and verifies the coherent-ramp recurrence (22)--
(25) with exact integers.
