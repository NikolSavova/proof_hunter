# The exact endpoint potential left by a live all-loop rectangle

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The live Pascal barrier does not become contradictory merely by declaring
the ambient configuration \(V\)-minimal.  At a genuine replaceable
strong-glue seam \(P=Y\prec Z\), reflection minimality forces the two
**facing** profiles to be the smaller endpoint profiles:

\[
                 C(Y)\le U(Y),\qquad U(Z)\le C(Z).       \tag{1}
\]

Thus minimization creates exactly the anti-alignment needed by the
all-loop rectangle.  This is consistent with, and in fact is the two-block
version of, the coherent quarter ramp.

There is nevertheless a useful exact invariant.  Every ordinary face has
a canonical upper-cap/lower-cup decomposition, so

\[
                         V(Q)\le C(Q)U(Q).               \tag{2}
\]

Writing endpoint energy and imbalance as

\[
 e(Q)={\log C(Q)+\log U(Q)\over2},\qquad
 \rho(Q)={\log U(Q)-\log C(Q)\over2},                   \tag{3}
\]

the actual mixed seam has logarithmic size

\[
 \log(C(Y)U(Z))
   =e(Y)+e(Z)-\rho(Y)+\rho(Z).                          \tag{4}
\]

The only way a live all-loop seam avoids the endpoint energy furnished by
(2) is therefore a directed drop of the potential \(\rho\).  Along an
actual directed cycle of seams the potential differences telescope, so
one edge recovers the average endpoint energy.  Along a path, the coherent
quarter ramp stores the entire loss in the endpoint potential difference.

This identifies the precise extra planar/history hypothesis beyond
two-family badness:

> one must produce, in the **same configuration**, either a directed
> profile cycle/reset, or two actual direction queries of the same physical
> child whose endpoint potential cannot keep dropping.

Reflecting a child only constructs a different configuration and does not
provide such a bank inside the minimizer.  A dense \(D\times U\) Hall
rectangle likewise supplies no cycle by itself.

For the Pascal regression the imbalance is \(o(L^2)\), and the seam already
has the full coefficient
\(\beta=1-1/(4\ln2)>1/2\).  Its coefficient-level exclusion already comes
from comparison with the known global coefficient-half construction, not
from a hidden leading-order seam deficit.  For the formal
quarter ramp, the potential drops exactly cancel every intermediate-span
gain, so no stronger conclusion follows.  Hence (1)--(4) are a sharp
minimizer/profile-balance gate, not a proof of the half lower bound.

## 1. Reflection-minimal strong seams select the small profiles

Let \(Y^\ast\) denote a reflected copy of \(Y\), so

\[
 V(Y^\ast)=V(Y),\qquad C(Y^\ast)=U(Y),\qquad
 U(Y^\ast)=C(Y).                                      \tag{5}
\]

All four configurations

\[
           Y^{\epsilon}\prec Z^{\eta},
           \qquad \epsilon,\eta\in\{1,\ast\},           \tag{6}
\]

have the same number of points and are rationally realizable strong glues.
Their exact face counts are

\[
 V(Y)+V(Z)+a b,\qquad
 a\in\{C(Y),U(Y)\},\quad b\in\{U(Z),C(Z)\}.             \tag{7}
\]

If the displayed \(P=Y\prec Z\) is minimal even within this four-element
mutation class, its cross term is the least of the four products.  Since
all counts are positive, this is equivalent to (1), and

\[
 C(Y)U(Z)
   =\min\{C(Y),U(Y)\}\min\{C(Z),U(Z)\}.                 \tag{8}
\]

Conversely (1) makes every reflection mutation nonimproving.  Swapping the
two children adds no new scalar inequality: after independent reflections,
all four endpoint products in (7) have already occurred.

This theorem applies only when the selected clouds are actual replaceable
strong-glue children.  A Hall core or a semialgebraic product chart does not
automatically supply that macro mutation.  In the Pascal counterexample it
does, because the live rectangle is the top split itself.

## 2. Universal endpoint decomposition

Fix a generic horizontal direction on a planar general-position set \(Q\).
For an ordinary face \(F\), let \(A(F)\) be its upper hull chain and
\(B(F)\) its lower hull chain, assigning the left and right endpoints to a
fixed side convention.  Then \(A(F)\) is a cap, \(B(F)\) is a cup, and the
ordered pair \((A(F),B(F))\) recovers \(F\).  This proves the injection

\[
       \mathcal F(Q)\hookrightarrow
       \mathcal C(Q)\times\mathcal U(Q)                 \tag{9}
\]

and hence (2).  The harmless endpoint convention also handles faces of
rank at most two.

In the notation (3),

\[
 \log C(Q)=e(Q)-\rho(Q),\qquad
 \log U(Q)=e(Q)+\rho(Q),\qquad
 e(Q)\ge {1\over2}\log V(Q).                           \tag{10}
\]

For a forward strong-glue bank from \(Q_i\) to \(Q_j\), with a decoded
intermediate singleton reservoir of logarithmic size \(s_{ij}\), the exact
profile term has logarithm

\[
 e(Q_i)+e(Q_j)+\rho(Q_j)-\rho(Q_i)+s_{ij}.              \tag{11}
\]

Equation (4) is the case \(s_{ij}=0\).

## 3. Exact cycle/reset payment

Let \(Q_0,\ldots,Q_{k-1}\) be physical child occurrences and suppose the
same configuration contains decoded forward banks on a directed cycle
\(Q_i\to Q_{i+1}\), with indices modulo \(k\).  Let \(s_i\ge0\) be their
decoded intermediate-reservoir logarithms.  Summing (11) gives

\[
 \sum_{i=0}^{k-1}\log B_i
   =2\sum_{i=0}^{k-1}e(Q_i)+\sum_{i=0}^{k-1}s_i.        \tag{12}
\]

Therefore some actual bank satisfies

\[
 \boxed{\quad
 \log B_i\ge {2\over k}\sum_j e(Q_j)
                  +{1\over k}\sum_j s_j.
 \quad}                                                \tag{13}
\]

By (10), the right side is at least the average child log-face count plus
the average span.  No bound on individual imbalances is required.

On a path \(Q_0\to\cdots\to Q_t\), the same sum has the uncancelled boundary
term

\[
                    \rho(Q_t)-\rho(Q_0).                \tag{14}
\]

The common-guard scalar ramp makes (14) as negative as the accumulated
span is positive.  Thus replacing “cycle” by “many seams” is invalid.
One needs either an actual reset/return edge or a same-physical-child
multi-direction theorem bounding the available potential range.

## 4. Calibration against Pascal and the quarter ramp

For the central Pascal split

\[
 T(n,n/2)=T(n-1,n/2-1)\prec T(n-1,n/2),
\]

the two child profiles are mirror-adjacent.  The uniform cap asymptotic
gives

\[
 e(Y)=\left({\beta\over2}+o(1)\right)n^2,\qquad
 \rho(Y)=o(n^2),
\]

and the symmetric statements for \(Z\).  Hence (4) has exponent
\((\beta+o(1))n^2\), exactly the parent coefficient.  The live all-loop
rectangle is locally seam-saturated; the global benchmark rules it out
because \(\beta>1/2\).

For the integral quarter ramp, in base-\(D\) logarithms,

\[
 \log_D C_i=i+2,\qquad
 \log_D U_i=q+1-i.                                    \tag{15}
\]

For every \(i<j\), the intermediate span has exponent \(j-i-1\), and

\[
 \log_D\!\left(C_iU_jD^{j-i-1}\right)=q+2.             \tag{16}
\]

The endpoint-potential drop cancels the entire span.  Equations
(15)--(16) show why any proposed minimizer inequality must retain the
cycle/reset hypothesis: the coherent ramp is an exact equality obstruction
to a path theorem.

## 5. Consequence for the live branch

The Pascal report proves that live sides, excess rank, a fixed rooted
blocker, and fixed-label chronology do not couple the two banks.  The
present note adds the sharp minimizer audit:

* local reflection mutations orient a live all-loop seam toward the bad
  profiles rather than away from them;
* universal endpoint energy exists, but can be hidden in the unused
  profiles as a one-dimensional potential;
* an actual cycle or coherent multiquery reset makes that potential
  telescope and is sufficient for a profile payment; and
* the current dense Hall rectangle supplies neither feature.

Thus the next genuinely geometric target is not another two-family
retention lemma.  It is a promotion from the fixed-label chronology to an
actual directed profile cycle, or a theorem that one physical child queried
in several realized directions has insufficient endpoint-potential range
to support the required \(\Theta(L)\)-step drop.  This is exactly the
additional hypothesis absent from the quarter scalar model.

## 6. Verification

**verify_minimizer_all_loop_endpoint_potential.py** exhausts all positive
integer endpoint profiles through six, verifying the reflection-minimum
criterion (8).  It checks the endpoint injection inequality on every Pascal
cell through the exact independent dynamic programs, verifies the cycle
telescope on exhaustive small integer exponent words, checks the exact
quarter-ramp cancellation, and records the Pascal imbalance through
\(n=96\).
