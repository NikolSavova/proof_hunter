# Planar rank layers need not have square-root anticoncentration

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

The proposed global shortcut

\[
                         V(P)\ge c\sqrt r\,v_r(P)        \tag{1}
\]

is false for every absolute \(c>0\), even for rational stretchable planar
configurations built from one fixed six-point seed.

Let \(T=T(4,2)\) be the central six-point Pascal cell and let \(P_d\) be
its depth-\(d\) almost-vertical self-substitution. Then

\[
 |P_d|=6^d,\qquad v_{4d}(P_d)>0,\qquad
                         V(P_d)\le40\,v_{4d}(P_d).       \tag{2}
\]

Consequently

\[
 {V(P_d)\over\sqrt{4d}\,v_{4d}(P_d)}
       \le {20\over\sqrt d}\longrightarrow0.            \tag{3}
\]

Thus fixed-rank Boolean-source capacity cannot be globalized merely by a
universal planar \(f\)-vector inequality. The middle-shadow theorem still
needs its explicit carrier-codegree descent. This counterexample does not
invalidate that theorem: its dominant top layer is spread through a
recursive strong-glue hierarchy, exactly the high-overlap profile state
isolated there.

## 1. The fixed rational seed and exact graded recurrence

The nonempty cap, cup, and ordinary-face polynomials of the six-point
Pascal cell are

\[
 c(z)=u(z)=6z+15z^2+10z^3,\qquad
 f(z)=6z+15z^2+20z^3+9z^4.                              \tag{4}
\]

Take \(P_0\) to be one point. At every step substitute a sufficiently
small rational affine copy of \(P_{d-1}\) into each of the six seed
positions. The vertical strong-glue classification is open in the
orientation signs, so successively small rational scales give an actual
rational general-position realization at every finite depth.

Write \(C_d(z)\) for the cap polynomial and \(F_d(z)\) for the ordinary
face polynomial of \(P_d\), and put \(n=6^{d-1}\). The exact substitution
recurrence is

\[
 \begin{aligned}
 C_d(z)&=C_{d-1}(z)\bigl(6+15nz+10n^2z^2\bigr),\\
 F_d(z)&=6F_{d-1}(z)
       +C_{d-1}(z)^2\bigl(15+20nz+9n^2z^2\bigr).
 \end{aligned}                                         \tag{5}
\]

The first line chooses a seed cap and identifies its first child label;
the second says that a face is either internal to one seed block or is a
cap-by-cup spanning face. These are equalities, not asymptotic estimates.
Here \(F_d\) counts nonempty faces. If the ambient convention includes the
empty face, add one at the end; since \(T_d\ge9\), the slack in (14) keeps
the same constant 40.

Let

\[
 A_d=[z^{2d+1}]C_d(z),\qquad
 T_d=[z^{4d}]F_d(z),\qquad
 R_d={C_d(1)\over A_d},\qquad S_d={F_d(1)\over T_d}.     \tag{6}
\]

The top coefficients in (5) give

\[
 A_d=10n^2A_{d-1},\qquad T_d=9n^2A_{d-1}^2.             \tag{7}
\]

In particular, \(T_d=v_{4d}(P_d)>0\).

## 2. A uniform constant bound for the whole face polynomial

Evaluating the cap recurrence at one and dividing by (7) gives

\[
 R_d=R_{d-1}\left(1+{3\over2\,6^{d-1}}
                         +{3\over5\,6^{2d-2}}\right).   \tag{8}
\]

The first factor, at \(d=1\), is \(31/10\). The sum of all increments in
the remaining factors is

\[
 \sum_{t\ge1}\left({3\over2\,6^t}+{3\over5\,6^{2t}}\right)
       ={3\over10}+{3\over175}={111\over350}.           \tag{9}
\]

For nonnegative \(x_i\) with \(\sum x_i<1\), expansion into elementary
symmetric functions gives

\[
                         \prod_i(1+x_i)
              \le {1\over1-\sum_i x_i}.                 \tag{10}
\]

Therefore

\[
                  R_d\le {31\over10}{350\over239}<5.    \tag{11}
\]

It remains to bound the internal term in the second recurrence. For
\(d\ge2\), put \(n_0=6^{d-2}\), so \(n=6n_0\). Equation (7) one level
earlier gives

\[
                         {T_{d-1}\over A_{d-1}^2}
                              ={9\over100n_0^2}.         \tag{12}
\]

Divide the face recurrence in (5) by \(T_d\). Using (11)--(12),

\[
 \begin{aligned}
 S_d
 &={6F_{d-1}(1)\over9n^2A_{d-1}^2}
   +R_{d-1}^2\left(1+{20\over9n}+{5\over3n^2}\right)\\
 &\le {3S_{d-1}\over50n_0^2n^2}
       +25\left(1+{20\over54}+{5\over108}\right).       \tag{13}
 \end{aligned}
\]

Now \(S_1=50/9<40\). If \(S_{d-1}\le40\), the first term in (13) is at
most \(1/15\), while the second is \(425/12<35.42\). Induction proves

\[
                               S_d<40                    \tag{14}
\]

for every \(d\), which is exactly (2). No limiting estimate or numerical
fit is used.

## 3. Scope for the live proof

The counterfamily has maximum face rank \(4d=\Theta(\log |P_d|)\), so it
lies in the live minimizer rank scale. Its top-rank faces comprise a
constant fraction of all ordinary faces, disproving even the weaker claim
that every rank layer is at most \(O(V/\sqrt r)\).

What survives is the carrier-aware statement. In the self-substitution,
top faces retain a long hierarchical profile word; treating them as one
unstructured rank layer erases exactly the branch information needed for
the return bank. Thus a successful high-\(\Lambda_{\rm mid}\) argument
must exploit completion first divergence, a private petal, or the rooted
strong-glue chronology. It cannot be replaced by an \(f\)-vector bound.

There is also a direct calibration against the weighted middle-shadow
gate. Take every top face \(Q\) of \(P_d\) as one carrier and take its
actual source to be \(A=Q\), with weight one. These sources are distinct,
so the rank-safe normalization is exact. Put \(q=4d\) and
\(K=v_q(P_d)\). Then

\[
                         W=K\ge V(P_d)/40.               \tag{15}
\]

Let \(B_q\) be the number of subsets of a \(q\)-set whose ranks lie between
\(q/3\) and \(2q/3\). Counting carrier--middle-face incidences gives

\[
 \Lambda_{\rm mid}
    \ge {K B_q\over V(P_d)}
    \ge {B_q\over40}
    =2^{q-o(q)}.                                         \tag{16}
\]

Thus the high-\(\Lambda_{\rm mid}\) branch is not a small polynomial
artifact: a genuine planar rank-safe family can have exponentially
coherent middle-shadow reuse. Likewise, applying the
private-petal/four-cover forest theorem to these carriers shows that its
terminal Boolean-bank overlap must satisfy

\[
                         \Lambda_{\rm leaf}
                              \ge {\sqrt{\pi q/2}\over40}.             \tag{17}
\]

Otherwise that theorem would contradict (15). The Pascal hierarchy is
therefore a sharp scalable regression for any completion argument using
only source ranks, carrier convexity, private labels, and four-local union
lifts. The external root/endpoint history must enter before a full return
can be proved.

## 4. Verification

**verify_planar_rank_layer_sqrt_counterexample.py** evaluates the exact
integer recurrences through depth 14, checks (4)--(8) coefficient by
coefficient, verifies \(V_d<40v_{4d}\), and checks the rational constants
used in the induction.
