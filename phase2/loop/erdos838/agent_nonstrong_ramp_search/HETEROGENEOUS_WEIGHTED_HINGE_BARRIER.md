# Heterogeneous children: the exact weighted-hinge residue

**Date:** 2026-08-15. All logarithms are base two. This note does not edit
the master attack.

## Verdict

There is an exact martingale reduction for unequal child sizes, but row
Kraft alone does not supply its local hypothesis.

At a node \(v\), let its child sizes be \(n_i\), put

\[
 N_v=\sum_i n_i,\qquad L_v=\log N_v,\qquad
 p_i={n_i\over N_v},\qquad
 \Delta_i=\log{N_v\over n_i},\qquad \ell_i=\log n_i.       \tag{1}
\]

Let \(A_i\) be the maximum weighted cap reward starting at position \(i\),
and let \(B_i\) be the maximum weighted cup reward ending at \(i\), where
using a sibling \(j\) contributes

\[
                         b_j=\log(1+n_j).                  \tag{2}
\]

Write \(R_i=A_i+B_i\). The exact local defect is

\[
 d_v=\left[\sum_i p_i\ell_i\Delta_i-\sum_i p_iR_i\right]_+,
 \qquad
 J_v=\sum_i p_i\Delta_i^2.                                \tag{3}
\]

For a uniform random leaf \(X\), let \(v\prec X\) mean that \(v\) lies on
its root-to-leaf address. Under the same-target chart recurrence,

\[
 \boxed{
 \log C_{\rm root}+\log U_{\rm root}
 \geq {1\over2}(\log N)^2
      -{1\over2}\mathbb E\sum_{v\prec X}J_v
      -\mathbb E\sum_{v\prec X}d_v.}                       \tag{4}
\]

Consequently, a same-chart final cap/cup splice gives the half coefficient
whenever

\[
 \mathbb E\sum_{v\prec X}J_v=o((\log N)^2),
 \qquad
 \mathbb E\sum_{v\prec X}d_v=o((\log N)^2).                \tag{5}
\]

In particular, a one-node inequality

\[
 \sum_i p_iR_i\geq\sum_i p_i\ell_i\Delta_i-c_BH(p)         \tag{6}
\]

with a constant depending only on the arity bound would close the defect
term with only \(c_B\log N\) loss. A uniform bound
\(\Delta_i\leq r=o(\log N)\) on active transitions closes the square-jump
term because

\[
 \mathbb E\sum_{v\prec X}J_v
 \leq r\,\mathbb E\sum_{v\prec X}H(p_v)
 =r\log N=o((\log N)^2).                                  \tag{7}
\]

Thus the exact surviving escape is not a growing chart set. It is a
macroscopic child-information jump or a positive quadratic sum of weighted
hinge defects.

One tempting way to bypass the exact second moment in (6) is the
entropy-only surrogate

\[
             \mathbb E R\geq H(p)(L-H(p)-c_B).             \tag{8}
\]

That surrogate with \(c_B=2\) is false even for an integral, stretchable,
genuinely non-strong eight-point macro. The exact certificate below
requires

\[
                         c_B>3.283858\ldots.               \tag{9}
\]

This is beyond the earlier binary skew warning: all eight macro positions
are present, the order type is non-strong after exhaustive decomposition
search, and its weighted cap/cup paths are computed in a genuine projection
chart.

A stronger zero-defect conjecture survived all searches:

\[
 \boxed{\sum_i p_iR_i\geq\sum_i p_i\ell_i\Delta_i.}         \tag{WH}
\]

The averaged inequality (WH) implies that some position obeys

\[
                         R_i\geq\ell_i\Delta_i.            \tag{10}
\]

Condition (10) alone is also sufficient for a deterministic Bellman-path
telescope, although it does not imply the averaged statement (WH). If (WH)
is true, (4) has no defect loss at all. This report treats both the new
weighted assertion and its pointwise consequence as experimentally strong
conjectures, not theorems. Ordinary hinged Kraft does not imply either one
formally: it records only the number of support positions and forgets which
sibling sizes occur on the maximizing weighted paths.

## 1. Weighted endpoint recurrence

Fix a projection chart and order the macro positions from left to right.
If edge slopes are processed increasingly, the exact tropical endpoint
updates are

\[
 \begin{aligned}
 A_i&\leftarrow\max\{A_i,A_j+b_j\},\\
 B_j&\leftarrow\max\{B_j,B_i+b_i\}
 \end{aligned}
 \qquad(i<j).                                             \tag{11}
\]

Equivalently, \(A_i\) is the largest sum of \(b_j\)'s on a decreasing-slope
path starting at \(i\), excluding the anchor, and \(B_i\) is the analogous
increasing-slope path ending at \(i\).

Suppose the cap and cup recurrences at position \(i\) call the same child
chart. If \(E_v=\log C_v+\log U_v\), then

\[
                         E_v\geq E_{vi}+R_i.               \tag{12}
\]

This is the exact weighted version of the homogeneous recurrence. The
quantity \(R_i\), not
\((\alpha_i+\beta_i)\log n_i\), is the geometric sibling multiplier.

## 2. Martingale telescope

Choose a uniform random leaf. Conditional on visiting \(v\), its next child
is \(i\) with probability \(p_i\). Hence

\[
 \mathbb E(\Delta_i\mid v)=H(p_v),\qquad
 \sum_{v\prec X}\Delta_v=\log N                           \tag{13}
\]

on every leaf address. The second identity follows because the product of
the conditional probabilities along any leaf is \(1/N\).

Iterating (11) down a random address and using that a maximum is at least
an average gives

\[
 E_{\rm root}
 \geq\mathbb E\sum_{v\prec X}R_v
 \geq\mathbb E\sum_{v\prec X}
       \{\ell_{\rm child}\Delta_v-d_v\}.                   \tag{14}
\]

But \(L_v=\ell_{\rm child}+\Delta_v\), so pathwise

\[
 \ell_{\rm child}\Delta_v
 ={1\over2}\{L_v^2-\ell_{\rm child}^2-\Delta_v^2\}.        \tag{15}
\]

The first two squares telescope from \(L_{\rm root}^2\) to zero. Taking
expectations proves (4). Also,

\[
 \mathbb E\sum_{v\prec X}H(p_v)=\log N,                   \tag{16}
\]

so (6) contributes at most \(c_B\log N\). Equations (7) and (16) give the
announced sharp interface: conditional entropy controls the defect sum,
whereas the conditional information *second moment* controls scale jumps.
Bounded arity alone does not bound that second moment, because a bounded row
may contain a child of arbitrarily small relative size.

## 3. Exact non-strong countercertificate to entropy-only \(c_B=2\)

Take the eight integral points

~~~text
(0,  611223)
(1, -321380)
(2, -883444)
(3, -152693)
(4, -406855)
(5, -230093)
(6, -115174)
(7,  791471).
~~~

The minimum absolute triple determinant is \(1430\). In the displayed
\(x\)-order, the increasing slope order is

~~~text
01 02 12 03 04 34 05 06 35 14 36 15 07 16
13 56 46 45 17 26 25 37 24 27 47 57 23 67.
~~~

Exhausting all \(8!\) leaf orders, every split, and both mirror signs finds
no strong-decomposition tree.

Give position zero \(128\) child points and every other position one point.
Thus \(N=135\). Put \(b=\log129\). Exact symbolic execution of (10) gives

\[
 \begin{aligned}
 A&=(1,2,3,1,2,1,1,0),\\
 B&=(0,b,b+1,b+2,b+2,b+2,b+2,b+3).                       \tag{17}
 \end{aligned}
\]

Therefore

\[
 \begin{aligned}
 L&=\log135,\\
 H(p)&=\log135-{896\over135},\\
 \mathbb E R&={150+7\log129\over135}.                     \tag{18}
 \end{aligned}
\]

The least constant making the entropy-only surrogate

\[
             \mathbb E R\geq H(p)(L-H(p)-c)               \tag{19}
\]

true at this node is

\[
 c_*={896\over135}
      -{\mathbb E R\over H(p)}
 \in(3.283,3.284).                                        \tag{20}
\]

The verifier proves the interval in (20) with rational upper and lower
bounds for the logarithms; it does not rely on floating-point comparison.
Thus \(c=2\), and even \(c=3\), are rigorously false.

This does not refute (6), because replacing
\(\mathbb E\Delta^2\) by \(H(p)^2\) made the surrogate artificially
strong. In fact the example does not refute (WH). At position zero,

\[
 R_0=1>
 7\log{135\over128}=\ell_0\Delta_0,                        \tag{21}
\]

so its large child itself pays the exact Bellman increment. It instead
shows why an entropy-only theorem loses the relevant state: averaging hides
the location of the large child and the actual siblings on its cap/cup
witnesses.

## 4. What is proved, conjectured, and missing

**Proved.**

1. The exact heterogeneous telescope (4), including the sharp defect and
   second-moment terms.
2. The sufficient conditions (5)--(7).
3. The stretchable non-strong counterexample (17)--(20) to every universal
   entropy-surrogate constant \(c\leq3.283\).

**Exhaustive evidence, not a theorem.**

The verifier checks (WH), hence also its pointwise consequence (10), for:

1. all \(720\) total orders of the six edges at arity four and all
   \(5^4\) child vectors from \(\{1,2,4,16,1024\}\);
2. every one of the 62 reflection-order commutation classes at arity five
   and all \(7^5\) power-of-two child vectors with exponents \(0,\ldots,6\);
3. all 56 projection chambers of the non-strong certificate, every choice
   of one distinguished child, and sizes \(2^t\) for \(1\leq t\leq20\).

The same audit checks the square-mesh inequality

\[
 \max_i\left\{{1\over2}\ell_i^2+R_i\right\}
 \geq {1\over2}L^2-{1\over2}(\log m)^2,                   \tag{22}
\]

which is implied by (10) whenever the selected
\(\Delta_i\leq\log m\), but is recorded separately because that implication
is not automatic.

**Missing state.**

The merged threshold word proves an unweighted prefix code. The
heterogeneous recurrence additionally needs the identities and sizes of
the vertices used by every cap and cup path. Threshold lengths alone permit
witness switching across size scales. A proof of (WH), or a counterexample
to it, must therefore retain a weighted predecessor forest (equivalently,
the sibling-incidence profile of the two endpoint dynamic programs).

This is the exact residue left after removing stationarity and finite chart
menus: not the number of states, but multiscale alignment between endpoint
paths and child masses.

## 5. Verification

Run

~~~bash
python3 phase2/loop/erdos838/agent_nonstrong_ramp_search/verify_heterogeneous_weighted_hinge.py
~~~

The current output is

~~~text
PASS: heterogeneous weighted-hinge barrier; c_interval=(3.2838580461996249505,3.2838580461996249505); decomposition_states=40335; martingale_trees=10; arbitrary_n4=450000; reflection_n5=1042034; nonstrong_weight_vectors=8960
~~~

The determinant, reflection-order realization, strong-decomposition
exhaustion, symbolic weighted profiles, and interval in (20) are exact.
The last three weighted-search counts are finite floating-point regressions
with a \(10^{-10}\) comparison tolerance; they are evidence for (WH) and
(22), not proof.
