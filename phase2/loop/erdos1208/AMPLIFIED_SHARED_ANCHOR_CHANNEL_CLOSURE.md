# Amplified shared-anchor channels: head closure and a tail barrier

## 1. Outcome

The two shared-head anchor channels in the amplified local/transverse
dichotomy can be converted rigorously into a common clean fibre for
**both** source starts.

* A shared-head third translation has exactly two exceptional choices for
  each source start.  Outside their union, both shifted starts lie in one
  new clean fibre.
* A shared-tail third translation always gives a disjoint shifted-edge
  transition, but it need not be clean relative to the new anchors.  It
  lands in `B_h=H_h \dot\cup \partial B_h`, and the wrong-side boundary is
  genuinely nonempty.

Consequently a selected shared-head channel of load at least `k/30`
contains at least half its load in double-closure records (for `k>=300`,
after deleting the one diagonal third translation).  Its contribution to
the high one-role mass is therefore at most `60/k` times an exact
closure-lift mass.

This closes the two shared-head channels as independent cases.
It does not yet bound the scalar closure-lift mass: the original weight

\[
 V(s,t)=W_{-(\delta(s)-\delta(t))/18,L}                 \tag{1.1}
\]

becomes a backward metric correlation after the shift.  The exact
remaining local channels are the two boundary-decorated shared-tail
channels, four cross-orientation anchor chains, and seven target-endpoint
stars.

## 2. Shared-head double closure

Let

\[
 q_1=a-b,\qquad q_0=a-c,\qquad h=q_1-q_0=c-b.           \tag{2.1}
\]

For `u in H_(q_1) intersect H_(q_0)`, the shared-head closure theorem says
exactly one of the following holds:

\[
 u+q_0\in H_h,                                         \tag{2.2}
\]

or, for one point `e`,

\[
 E(u+q_0)=\{e,b\},\qquad E(u+q_1)=\{e,c\}.             \tag{2.3}
\]

Fix `(q_1,u)` and vary `q_0` with the same head `a`.  The exceptional
choices are exactly

\[
 q_0=a-c,qquad c\in E(u+q_1).                          \tag{2.4}
\]

Thus there are exactly two.  Now fix a source pair `p=(s,t)` common to
`q_1,q_0`.  At most four distinct `q_0` are exceptional for at least one
of `s,t`.  Every other shared-head third translation gives

\[
 \boxed{s+q_0, t+q_0\in H_{q_1-q_0}.}                 \tag{2.5}
\]

All orientations and the original translations remain recoverable.

## 3. Shared-tail lift and the wrong-side barrier

Let instead

\[
 q_1=a-b,\qquad q_0=c-b,\qquad h=q_1-q_0=a-c.           \tag{3.1}
\]

Take `u in H_(q_1) intersect H_(q_0)` and put `r=u+q_0`.  The two edges

\[
 E(r)=E(u+q_0),\qquad E(r+h)=E(u+q_1)                  \tag{3.2}
\]

are disjoint.  Indeed, if they met, their outer-endpoint difference would
be `a-c`; vector-Sidonicity would force the outer endpoints `a,c`,
contradicting the original clean rows, because `E(u+q_1)` avoids `a` and
`E(u+q_0)` avoids `c`.

Therefore `r` lies in the disjoint-transition family from the target-star
switch:

\[
 \boxed{u+q_0\in B_{q_1-q_0}.}                          \tag{3.3}
\]

It lies in `H_(q_1-q_0)` exactly when the two wrong-side anchor collisions
are absent.  Here these are

\[
 a\in E(u+q_0)
 \quad\hbox{or}\quad
 c\in E(u+q_1).                                        \tag{3.4}
\]

Neither is forbidden by the original two clean rows.  The 16-point closure
stress gives the exact witness (indices below are zero-based, as in the
verifier)

\[
\begin{aligned}
 q_1&=(-33,11)=A_3-A_{14},\\
 q_0&=(-7,8)=A_{11}-A_{14},\\
 u&=(70,29),\\
 E(u+q_0)&=\{A_3,A_{15}\},\\
 E(u+q_1)&=\{A_2,A_8\}.
\end{aligned}                                           \tag{3.5}
\]

The two target edges are disjoint, but `A_3` is the head anchor of
`q_1-q_0=A_3-A_11`, so `u+q_0` lies in
`\partial B_(q_1-q_0)`, not in the clean fibre.  A shared-tail channel
therefore cannot be passed through shared-head closure by reversing
notation.

## 4. Weighted amplified consequence

Use the channel selection from
`AMPLIFIED_THIRD_TRANSLATION_LOCAL_TRANSVERSE_DICHOTOMY.md`.  Let
`\mathcal C_sh` be the selected local-rich base records whose chosen channel
is one of the two shared-head channels.  For a base
record `C`, let `D(C)` be that channel load.

Delete the diagonal choice `q_0=q_i` belonging to the selected base
anchor and the at most four choices exceptional for `s` or `t`.  If
`k>=300`, then

\[
 D(C)\ge{k\over30}\ge10
 \quad\Longrightarrow\quad
 D_{\rm cl}(C)\ge {D(C)\over2},                         \tag{4.1}

\]

where every retained choice satisfies the double closure (2.5).
Define the exact closure-lift mass

\[
 \mathfrak C(V)=
 \sum_{C\in\mathcal C_{\rm sh}}D_{\rm cl}(C)
   \bigl(V(p_C)+V(p_C^{\rm op})\bigr).                 \tag{4.2}
\]

Since the selected channel has `D(C)>=c(p_C)/30>=k/30`, (4.1) gives

\[
 \boxed{
 \sum_{C\in\mathcal C_{\rm sh}}
   \bigl(V(p_C)+V(p_C^{\rm op})\bigr)
 \le {60\over k}\mathfrak C(V).}                      \tag{4.3}
\]

The bounded range `k<300` is absorbed into the absolute constant in an
asymptotic `m^(o(1))` statement.

For a closure-lift record put

\[
 S=s+q_0,qquad T=t+q_0,qquad h=q_i-q_0.               \tag{4.4}
\]

Then

\[
 S,T\in H_h,qquad
 V(s,t)=W_{-(\delta(S-q_0)-\delta(T-q_0))/18,L}.        \tag{4.5}
\]

Thus the common fibre is genuine, but the metric weight is a backward
shift by the still-realized anchor difference `q_0`.  Replacing it by
`delta(S)-delta(T)` would be invalid.

## 5. Exact remaining thirteen-channel mass

Combining this theorem with the previous dichotomy gives

\[
 \boxed{
 D_{\rm one}^{\ge k}(V)
 \le {2\over k}\mathfrak T(V)
   +{60\over k}\mathfrak C(V)
   +{30\over k}\mathfrak R_{13}(V),}                  \tag{5.1}
\]


where `mathfrak R_13` is the selected channel-incidence mass in exactly:

1. two shared-tail channels, retaining the `B_h` lift (3.3);
2. four cross-orientation anchor chains; and
3. three good-role plus four bad-role target endpoint stars.

Every cross channel realizes a composable anchor chain such as

\[
 q_i=a-b,\quad q_0=b-c,\quad q_i+q_0=a-c\in A-A.        \tag{5.2}
\]

Every target channel supplies a set `U subset A`, `|U|>=k/30`, for which,
in the appropriate role,

\[
 q_0=z+u-s\in A-A,qquad z+u+(t-s)\in\Sigma
 \quad(u\in U).                                        \tag{5.3}
\]

These are the exact special-affine-looking endpoint systems still needing
a metric incidence theorem.  The scalar weight in (1.1) is constant on
the source pair but is not one of the physical target edges in (5.3), so
the known fixed-wedge theorem does not directly bound it.  Expanding
`W_(r,L)` adds a second, independent physical wedge; the remaining problem
is an incidence between that metric wedge and (5.2) or (5.3).

## 6. Verification

`verify_amplified_shared_anchor_channel_closure.py` checks on closure,
Costas, parabola, and ruler distance-Sidon families:

* exactly two shared-head exceptions for every clean record;
* the double-closure union bound of four exceptions;
* the exact shared-tail `B_h` lift and a genuine wrong-side witness; and
* the pairwise double-closure identities with all orientations retained.
