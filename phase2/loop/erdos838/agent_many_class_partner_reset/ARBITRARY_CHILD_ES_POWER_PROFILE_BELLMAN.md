# Arbitrary children in the perfect reset: exact endpoint Bellman and the surviving ramp

**Date:** 2026-08-15. All logarithms are base two. A cap or cup of size at
most two is counted in both families; all face counts are nonempty. This
note strengthens the representative-rank audit in
`PERFECT_RESET_LEXICOGRAPHIC_ES_COUNTERREGRESSION.md`. It does not claim a
construction beating the conjectured lower bound.

## Verdict

Every final macro point of the rational perfect-reset power can be replaced
by an independently chosen arbitrary rational (D)-point planar order
type. All perfect class-pair matchings, fresh physical pairs, label load
(t-1), and bad `2+2` circuit signs survive. There is no extra
non-(x)-projection chamber: the complete ordinary-face recurrence is the
same recursively coherent left-cap/right-cup rule at every node.

For the (h)-fold (E(7,7)) macro power, with

\[
       t=14^h,\qquad M=252^h,\qquad |Y_i|=18^hD,
\]

the exact macro ranks are

\[
 \boxed{R_C=R_U=5h+1,\qquad R_W=10h.}                \tag{1}
\]

Thus the earlier (10^h) bound is valid but extremely loose. A face
spanning multiple child cells has at most two non-singleton traces: a cap
in its left endpoint cell and a cup in its right endpoint cell. Every
other trace is a singleton.

Flattening the recursion gives exact nonnegative polynomials

\[
\begin{aligned}
 C(P)&=\sum_i A_i(D)C_i,\\
 U(P)&=\sum_j B_j(D)U_j,\\
 W(P)&=\sum_iW_i+\sum_{i<j}K_{ij}(D)C_iU_j,           \tag{2}
\end{aligned}
\]

with

\[
 \max_i\deg A_i=\max_j\deg B_j=5h,\qquad
 \max_{i<j}\deg K_{ij}=10h-2.                       \tag{3}
\]

Consequently identical low-endpoint-product children pay the stationary
factor (D^{10h-2}). Heterogeneous children can reduce this payment only
by forming a single globally coherent cap-richness ramp in macro
(x)-order. The sharp scalar degree relaxation is a four-entry max-plus
Bellman recurrence. At the live normalization (D=2^L), (L=14^h), and
local log-face budget (w=L^2/2), its forced extra parent log-count is

\[
                  \Theta_h L,\qquad
             \Theta_h=(4.7\ldots)h                    \tag{4}
\]

for the exact finite depths audited below. This is
(\Theta(L\log L)=o(L^2)): it does **not** raise the leading coefficient
above (1/2). It is, however, precisely on the fixed-gap scale, so it
cannot be discarded in a second-order proof.

The result is therefore a sharp barrier rather than a global
counterexample. The reset geometry permits arbitrary child order types
and imposes only (2). To turn the scalar ramp into an actual low-face
construction, one would still have to realize the required continuum of
cap/cup profiles by planar (D)-point children. Conversely, a positive
proof must rule out that realizability or charge the Bellman ramp; circuit
signs and alternative projections do not do it automatically.

## 1. Exact separated-composition recurrence

Write (T=A\searrow B) for a high-left copy of (A) and a low-right copy
of (B), separated so that every cross slope is below every internal
slope. For ordered triples, two points in (A) followed by one in (B)
have negative sign, while one in (A) followed by two in (B) have
positive sign.

If (Q) has profile

\[
                  (n(Q),C(Q),U(Q),W(Q)),
\]

then the sign rules classify every face and give the exact recurrence

\[
\boxed{
\begin{aligned}
n(T)&=n(A)+n(B),\\
C(T)&=C(A)(1+n(B))+C(B),\\
U(T)&=U(A)+U(B)(1+n(A)),\\
W(T)&=W(A)+W(B)+C(A)U(B).
\end{aligned}}                                        \tag{5}
\]

Indeed, a spanning cap has a cap trace in (A) and one point in (B); a
spanning cup has one point in (A) and a cup trace in (B); and a
spanning ordinary face has a cap trace in (A) and a cup trace in (B).
All choices are recovered from their two traces, so (5) is an equality.

The cup--cap construction is

\[
 E(r,s)=E(r,s-1)\searrow E(r-1,s),
 \qquad E(2,s)=E(r,2)=\{\ast\}.                       \tag{6}
\]

For arbitrary leaf profiles, apply (5) on this fixed binary recursion
tree. Applying the (E(7,7)) operator (h) times is the exact
multi-point child recurrence for the perfect-reset power.

There is no missing projection branch in (5). Ordinary convexity is
affine invariant, and the mixed triple signs prove both necessity and
sufficiency. Any ordinary face spanning at least two final leaves has a
unique first and last non-singleton candidate; recursive application of
(5) shows that these are respectively a cap and a cup and that every
other active final leaf is a singleton.

## 2. Arbitrary substitution preserves the reset

The reset in the preceding report is a finite rational order type with
strict bad macro four-circuits. Around every final macro point (z), put
an independently chosen rational affine copy of an arbitrary child
(Q_z), using a sufficiently small rational scale. Finitely many strict
determinants imply simultaneously that

1. triples inside one cell have the child signs;
2. triples in distinct cells have the macro signs; and
3. every transversal through a designated bad macro four-circuit remains
   the same bad circuit.

Expand every macro factor edge indexwise through the (D) child labels.
A physical pair still decodes its unique macro pair and child index, so no
pair is reused. Every factor covers its class and every physical label has
load (t-1). Thus the arbitrary-child operation changes neither the
perfect matchings nor their pair-node degree-one certificate.

This is a genuine substitution theorem: the children need not be copies,
need not have the same cap/cup profile, and may be oriented independently
before insertion. The global separated chart used in (5) is retained.

## 3. Additive rank and flattened endpoint polynomials

The rank version of (5) is also exact:

\[
\begin{aligned}
r_C(T)&=\max\{r_C(A)+1,r_C(B)\},\\
r_U(T)&=\max\{r_U(A),r_U(B)+1\},\\
r_W(T)&=\max\{r_W(A),r_W(B),r_C(A)+r_U(B)\}.          \tag{7}
\end{aligned}

Starting from a singleton and iterating (E(7,7)), (7) gives

\[
 (r_C,r_U,r_W)=(5h+1,5h+1,10h),                      \tag{8}
\]

proving (1). In particular, a representative bank choosing at most one
point per final macro leaf has exponent (D^{10h}), not (D^{10^h}).

To flatten (5), mark the final leaves (1<\cdots<M). A global cap has at
most one non-singleton leaf trace, and a global cup has the analogous
property. An ordinary face has either one local trace, or a cap trace at
(i), a cup trace at (j>i), and a recursively compatible set of
singleton leaves between them. Summing these choices gives (2).

More explicitly, (K_{ij}(D)) is the sum of (D^{|S|}) over compatible
sets (S) of singleton leaves that complete endpoint leaves (i,j).
It has nonnegative integer coefficients and constant term one. If

\[
 c_i=\deg A_i,\quad u_i=\deg B_i,\quad
 d_{ij}=\deg K_{ij},                                  \tag{9}
\]

then a binary node (T=A\searrow B) transforms the degrees by

\[
\begin{array}{c|cc}
 &i\in A&i\in B\\ \hline
c_i(T)&c_i(A)+1&c_i(B)\\
u_i(T)&u_i(A)&u_i(B)+1,
\end{array}                                           \tag{10}
\]

retains internal (d_{ij}), and gives every cross edge

\[
                  d_{ij}=c_i(A)+u_j(B).               \tag{11}
\]

Equations (10)--(11) prove (3). They also show directly why no third
multi-point child profile can appear.

## 4. The exact two-boundary Bellman state

For a nonempty increasing leaf path
(\pi=(i_0<\cdots<i_k)), define

\[
 S(\pi)=\sum_{q<k}d_{i_qi_{q+1}}.                     \tag{12}
\]

For a penalty (x\ge0), retain the four boundary states

\[
 M_T^{\alpha\beta}(x)=
 \max_\pi\left[
   \alpha u_{i_0}+S(\pi)-kx+\beta c_{i_k}
 \right],\qquad \alpha,\beta\in\{0,1\}.             \tag{13}
\]

At a singleton all four entries are zero. Equations (10)--(11) give the
exact max-plus recurrence

\[
\boxed{
M_T^{\alpha\beta}=
\max\left\{
 M_A^{\alpha\beta}+\beta,
 M_B^{\alpha\beta}+\alpha,
 M_A^{\alpha1}+M_B^{1\beta}-x
\right\}.}                                           \tag{14}
\]

The third term is a path crossing once from (A) to (B); its two
boundary credits are exactly the cross degree in (11). This four-scalar
state is sufficient for the entire (252^h)-leaf tree.

At zero penalty it gives

\[
 M_h(0)=
 \begin{pmatrix}R_h&R_h+1\\R_h+1&R_h+2\end{pmatrix},
 \qquad R_h=182\,252^{h-1}-2.                         \tag{15}
\]

Thus an exactly stationary zero-slack ramp would need enormous total
width. That observation alone is misleading: a small payment per mixed
term is paid at every edge of a long path. The correct quantity is the
penalized state (14).

## 5. Sharp scalar profile payment

Suppose all (D)-point children obey (W_i\ge2^w), and put
(a_i=\log C_i), (b_i=\log U_i). The boundary-chain injection gives

\[
                       a_i+b_i\ge w.                  \tag{16}
\]

If (W(P)\le2^p), the leading monomial of every mixed term in (2) gives

\[
                  a_i+b_j+d_{ij}L\le p,\qquad L=\log D. \tag{17}
\]

Let $\delta=p-w$. In the scalar relaxation one may replace

\[
 a_i\mapsto\min\{a_i,w\},\qquad
 b_i\mapsto w-\min\{a_i,w\};                         \tag{18}
\]

this only decreases every left side in (17). Hence the relaxation is
feasible exactly when there are potentials (0\le a_i\le w) with

\[
                 a_j-a_i\ge d_{ij}L-\delta.           \tag{19}
\]

Because the leaf order is acyclic, difference constraints give the exact
criterion

\[
 \max_\pi\{LS(\pi)-k\delta\}\le w.                  \tag{20}
\]

Equivalently, with (B=w/L),

\[
 \boxed{
 p-w\ge L\Theta_h(B),\qquad
 \Theta_h(B)=
 \max_{\pi:k\ge1}{S(\pi)-B\over k}\vee0.}          \tag{21}
\]

The value in (21) is obtained exactly by walking the piecewise-linear
envelope (M_h^{00}(x)) from (14) until it first drops to (B). This is
the sharp optimum of the degree/profile scalar relaxation. The actual
integer polynomials (K_{ij}(D)) can only increase the face count.

For (L=14^h) and (w=L^2/2), the exact rational values are

\[
\begin{array}{c|c|c}
h&\Theta_h&\Theta_h/h\\ \hline
1&33/7&4.714285\\
2&174/17&5.117647\\
3&14740/1007&4.879179\\
4&248434/12601&4.928855\\
5&6081464/254015&4.788272\\
6&55420988/1905121&4.848422\\
7&1067503776/32006015&4.764746\\
8&18497721126/480090241&4.816209.
\end{array}                                           \tag{22}
\]

These finite values are verifier-certified, not asserted as a proved
limit. Uniformly, the trivial direct-edge bound and (3) give

\[
                  0\le\Theta_h(B)\le10h-2,            \tag{23}
\]

so for (h=\Theta(\log L)) every scalar payment remains
(O(L\log L)=o(L^2)). Therefore the leading coefficient can remain
(1/2) in the scalar recurrence. Claiming an actual planar family at that
coefficient would additionally require actual low-face children realizing
the potentials in (19); that is the unresolved ramp-realizability gate.

## 6. One, two, and many endpoint profiles

If every leaf uses one identical endpoint profile and
(C_iU_i\ge2^w), choose endpoints of a rank-(10h) macro face in (2):

\[
                    p\ge w+(10h-2)L.                 \tag{24}
\]

For at most (R) distinct numerical profiles, one profile occupies at
least (M/R) macro leaves. The elementary cup--cap upper bound

\[
                  ES(r)\le {2r-4\choose r-2}+1        \tag{25}
\]

finds within that same-profile set a macro convex support of rank (r),
where (r) is the largest integer satisfying

\[
             \lfloor M/R\rfloor\ge {2r-4\choose r-2}+1. \tag{26}
\]

Taking its first and last leaves in (2) gives

\[
                        p\ge w+(r-2)L.                \tag{27}
\]

For two profiles, (r=(\tfrac12\log 252+o(1))h=
3.9886\ldots h+o(h)). This is still a second-order payment, not a
leading-coefficient improvement. More importantly, a near-optimal
Bellman ramp cannot be modeled by merely one or two stationary child
types: it needs a growing ordered bank of genuinely different endpoint
potentials, unless some larger same-profile macro support is paid through
(27).

Equations (24)--(27) audit the one/two-profile coexistence requested in
the reset branch. They do not rule out a many-profile planar ramp.

## 7. Verification

Run

```text
python3 phase2/loop/erdos838/agent_many_class_partner_reset/verify_es_power_child_profile_bellman.py
```

The verifier:

* constructs the rational separated (E(r,s)) charts and brute-forces
  every subset for eight small cases, matching (5) exactly;
* checks a heterogeneous nonconvex-child composition by rational hull
  enumeration;
* certifies (8) for (1\le h\le8), the 252 flattened leaf coefficients,
  all 31,626 endpoint pairs, and maximum degrees `(5,5,8)`;
* independently enumerates every increasing path in the six-leaf
  (E(4,4)) tree and matches all four Bellman states at (x=3/2);
* checks the closed form (15), walks the exact rational parametric envelope
  for all values in (22), and prints the active `(degree,edge-count)`
  witness at every breakpoint; and
* checks the finite one/two-profile ES payments through depth eight.

The perfect reset itself and its 819 rational base circuits remain
certified by `verify_perfect_reset_lexicographic_counter.py`.
