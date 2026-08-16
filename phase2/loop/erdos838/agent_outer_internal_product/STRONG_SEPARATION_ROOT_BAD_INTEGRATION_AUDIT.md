# Root-bad products: strong separation, endpoint profiles, and the global load gate

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The current low-redundancy retention argument reaches a complete product
of ordinary singleton transversals only under its stated
**ordered/simple-chain certificate**.  If that certificate says that the
role word is the boundary order, then every transversal has one fixed
cyclic order.  This is exactly a same-type product, and hence is strongly
separated by Barany--Pach, Proposition 3.3.

Two stronger inferences do not follow.

1. Merely knowing that every transversal is convex does not fix its type.
   Section 2 gives a rational four-role counterexample with two convex
   transversals whose role-triple sign flips.
2. Strong separation fixes orientations involving one point from each of
   three distinct roles.  A multi-point endpoint profile also uses signs
   with two points from one role.  Section 3 gives a scalable strongly
   separated rational product in which both directional endpoint families
   have only polynomial size while the local face reservoir is
   exponential.  Thus the desired profile factorization is false under
   strong separation alone.

The proposed local interface

> **Strong-separation endpoint-profile lemma.**  For strongly separated
> cyclic supports, directional local profile families satisfy
> `A_i R_i >= H_i`, and the two profiles exposed at any omitted role,
> together with singleton choices in the other roles, form an ordinary
> face.

is false.  What can still suffice is the same statement under a stronger
**lexicographic exposure** hypothesis, such as infinitesimal radial
clusters or fixed oriented ear containers.  Conditional on that stronger
hypothesis, the cyclic product identity gives

\[
 \log V(P)\ge
 \left[a+c_0(a/\kappa)^2-o(1)\right](\log D)^2.       \tag{1}
\]

Thus the universal local coefficient `c_0=1/4`, at
`a=\kappa=1/4`, gives coefficient `1/2` exactly.  With only
`c_0=1/8`, the same calculation gives `3/8`.

There is no cross-base load in (1) when one fixed product already has
`log P_0 >= (a-o(1))(log D)^2`: its profile bank is one family of distinct
ordinary faces and is counted once.  If only a sum of many smaller
base-specific products carries the quadratic mass, local banks cannot be
summed.  The exact aggregate conclusion loses their output overlap
`Lambda`; identical products reused by `K` bases have `Lambda=K` and gain
nothing from summation.  This is the remaining global decoder/container
promotion gate.

Accordingly this report is a **conditional coefficient-half theorem and
an unconditional scalable regression against the strong-separation
bridge**, not an end-to-end proof of EIC'.

## 1. What low-redundancy retention actually produces

Let

\[
                 E\subseteq X_1\times\cdots\times X_q,
 \qquad M=|E|,\qquad
 R=\log {\prod_i|\pi_iE|\over M}.                     \tag{2}
\]

The role-colouring step makes the coordinate supports disjoint at cost
`q log q`.  Fixing the actual boundary jet and a root-bad four-circuit
role pattern costs only `O(log D+log q)` bits.  In the high-`R` branch,
the support-union bank pays as recorded in
`HIGH_REDUNDANCY_SUPPORT_BANK.md`.

In the low-`R` branch, the bounded-degree sign transcript gives subsets

\[
                         Y_i\subseteq\pi_iE             \tag{3}
\]

such that every ambient transversal in

\[
                         \mathcal P=\prod_iY_i          \tag{4}
\]

has the fixed predicate transcript, while

\[
 |E\cap\mathcal P|\ge M2^{-O(q+R)}.                    \tag{5}
\]

The distinction between (4) and (5) is useful.  The retained selected
family may be sparse, but the ambient rectangle is complete.  If the
certificate has the implication

\[
 \boxed{\text{fixed transcript}\Longrightarrow
        (y_1,\ldots,y_q)\text{ is the cyclic hull order}},             \tag{CYC}
\]

then every member of (4) is an ordinary face in that fixed cyclic order.
The phrase `ordered/simple-chain certificate` in
`ROLE_COLORED_PROFILE_DICHOTOMY.md` is precisely where (CYC) must enter.
The semialgebraic retention theorem alone only preserves the supplied
sign predicates; it does not manufacture simplicity or the hull order.

This makes the present integration status exact:

* after (CYC) is supplied, the low-`R` branch is a complete same-type
  product;
* random role colouring plus the unordered assertion “every transversal
  is convex” is insufficient for (CYC); and
* any occurrence of the branch before an ordered/simple-chain slicing is
  completed remains conditional on that slicing.

## 2. Fixed cyclic order is exactly the strong-separation bridge

For three planar points write

\[
 \chi(x,y,z)=\det(y-x,z-x).                             \tag{6}
\]

Assume the union of the pairwise disjoint supports `Y_i` is in general
position and `q>=3`.

> **Lemma 1 (cyclic type implies strong separation).**  If every
> transversal `(y_1,...,y_q)` is a strictly convex polygon whose
> counterclockwise boundary order is `(1,...,q)`, then the collection
> `Y_1,...,Y_q` is strongly separated.

**Proof.**  For every `i<j<k`, the three vertices occur in
counterclockwise order on the boundary of the transversal, so

\[
                         \chi(y_i,y_j,y_k)>0.           \tag{7}
\]

The sign is therefore independent of every coordinate choice.  All
transversals have the same type.  Proposition 3.3 of I. Barany and J.
Pach, [*Homogeneous selections from hyperplanes*, JCTB 104 (2014),
81--87](https://users.renyi.hu/~pach/publications/hyperplanes080411.pdf),
says that a finite collection in `R^d`, with at least `d+1` classes, is
strongly separated if and only if every pair of transversals has the same
type.  Apply it with `d=2`.  QED.

The converse useful here is immediate from the same proposition.  If the
supports are strongly separated and one reference transversal has cyclic
type `(1,...,q)`, every transversal has that type and hence is a convex
polygon in the same cyclic order.

Convexity without the fixed role order is weaker.  Put

\[
\begin{aligned}
 p&=(2,-2),&q&=(-3,2),\\
 a&=(0,0),&b&=(4,0),&c&=(0,4),
\end{aligned}                                          \tag{8}
\]

and take `X_1={p,q}`, `X_2={a}`, `X_3={b}`, `X_4={c}`.
Both four-point transversals are strictly convex, and all five points are
in general position.  But

\[
                 \chi(p,a,b)=-8,
 \qquad          \chi(q,a,b)= 8.                       \tag{9}
\]

They have different types, so the supports are not strongly separated.
This kills the shortcut

\[
 \text{complete product of convex sets}
       \Longrightarrow\text{strong separation}.       \tag{10}
\]

The fixed cyclic-order clause is essential.

## 3. Strong separation is not itself a multi-point profile theorem

Proposition 3.3 controls exactly the signs in (7): three labels drawn from
three distinct supports.  Endpoint profiles require additional signs such
as

\[
                         \chi(u,v,y_j),qquad u,v\in Y_i,               \tag{11}
\]

which are absent from the transversal type.

The following exact example shows why an arbitrary local face cannot be
used as a profile.  Put

\[
\begin{aligned}
 u&=(2,-2),&v&=(2,-1),\\
 b&=(4,0),&c&=(0,4),&a&=(0,0),
\end{aligned}                                          \tag{12}
\]

and assign the cyclic roles

\[
            Y_1=\{u,v\},\quad Y_2=\{b\},\quad
            Y_3=\{c\},\quad Y_4=\{a\}.               \tag{13}
\]

For either choice in `Y_1`, every role triple `i<j<k` has positive
orientation.  Both transversals are convex in the cyclic order
`(1,2,3,4)`.  Lemma 1 therefore makes the four supports strongly
separated.

The two-point set `F={u,v}` is an ordinary local face.  Omit the adjacent
role `4`.  The formal endpoint substitution is

\[
                         F\cup\{b,c\}.                  \tag{14}
\]

It is nonconvex, because

\[
                  v={3\over4}u+{1\over8}b+{1\over8}c. \tag{15}
\]

All coefficients are positive.  Thus strong separation does not justify
replacing a singleton by an arbitrary detached local face, even at a
genuine adjacent gap.

The two-point example by itself does not disprove a directional-profile
theorem: its local face can be encoded by two singleton chains.  The next
construction kills the factorization quantitatively.

### 3.1 A scalable fixed-type regression against both endpoint directions

Fix `m>=14`, put

\[
              \delta={1\over100m^2},\qquad
 P_t=\left(2-\delta t^2,-{1\over5}+\delta t\right)
             \quad(1\le t\le m),                       \tag{16}
\]

and take

\[
 X_1=\{P_1,\ldots,P_m\},\quad
 X_2=\{b=(4,0)\},\quad X_3=\{c=(0,4)\},\quad
 X_4=\{a=(0,0)\}.                                     \tag{17}
\]

Every `P_t` satisfies `x>0`, `y<0`, and `x+y<4`.  Therefore, in the role
order `(P_t,b,c,a)`,

\[
\begin{aligned}
 \chi(P_t,b,c)&=16-4x(P_t)-4y(P_t)>0,\\
 \chi(P_t,b,a)&=-4y(P_t)>0,\\
 \chi(P_t,c,a)&=4x(P_t)>0,\\
 \chi(b,c,a)&=16>0.                                   \tag{18}
\end{aligned}
\]

All transversals have the same convex cyclic type, so Lemma 1 makes the
four supports strongly separated.

The points `P_t` lie on the strictly concave parabola

\[
              x=2-{(y+1/5)^2\over\delta}.              \tag{19}
\]

They are in convex position.  Hence every nonempty subset of `X_1` is an
ordinary face and

\[
                              H_1=2^m-1.                \tag{20}
\]

But three labels from `X_1` never form an admissible endpoint trace while
the singleton `c` is retained.  Indeed, for `i<j<k`, put

\[
 D_{ik}=\chi(P_i,P_k,c)
 =\delta(k-i)\left[2-{21\over5}(i+k)+\delta ik\right]<0.\tag{21}
\]

Also

\[
 \chi(P_i,P_k,P_j)
   =\delta^2(k-i)(j-i)(j-k)<0,                          \tag{22}
\]

while

\[
 \chi(P_j,P_k,c)<0,\qquad \chi(P_i,P_j,c)<0            \tag{23}
\]

by the same formula as (21).  The three barycentric coordinates of
`P_j` relative to `(P_i,P_k,c)` are the three ratios in
(22)--(23) over `D_{ik}`.  They are strictly positive and sum to one.
Thus

\[
                         P_j\in\operatorname{int}
                                  \operatorname{conv}\{P_i,P_k,c\}.
                                                               \tag{24}
\]

Any trace `G subseteq X_1` of rank at least three contains such a triple,
so `G union {c}` is nonconvex.

Both omitted gaps adjacent to role `1` retain `c`: omitting role `2`
leaves `{c,a}`, while omitting role `4` leaves `{b,c}`.  Consequently
every admissible left or right endpoint profile in `X_1` has rank at most
two.  Each profile family has size at most

\[
                    S_m={m\choose1}+{m\choose2}
                       ={m(m+1)\over2}.                 \tag{25}
\]

At `m=14`,

\[
                  S_m^2=105^2=11025
                       <16383=2^{14}-1=H_1.             \tag{26}
\]

It is therefore impossible to have `A_1R_1>=H_1` with both profile
families admissible at their assigned omitted gaps.  This refutes the
strong-separation endpoint-profile lemma, including its weaker
`L_i^3` omitted-cell version.

The displayed configuration is already in general position.  For two
`P`-labels and `a`, the possible extra determinant is

\[
 \delta(k-i)\left[2-{i+k\over5}+\delta ik\right],       \tag{27}
\]

which is nonzero: when `i+k=10` its last term is positive, and otherwise
its first two terms have magnitude at least `1/5`, greater than
`delta ik<=1/100`.  The determinant with `b` is strictly negative;
(21) handles `c`; the parabola handles triples in `X_1`; and (18) handles
one `P`-label with two external labels.

## 4. Conditional lexicographic profile theorem and coefficient

Let `L_i=|Y_i|`, `P_0=prod_iL_i`, and let `H_i` be the nonempty ordinary
face count in the induced configuration on `Y_i`.  Assume, in addition
to strong separation, the following endpoint-profile property.

* There are left and right profile families of sizes `A_i,R_i` with

  \[
                             A_iR_i\ge H_i.             \tag{28}
  \]

* On omitting role `j`, every union of a right profile from role `j-1`, a
  left profile from role `j+1`, and one arbitrary point from every other
  retained role is an ordinary face.

The gap bank then has the exact size

\[
 B_j=R_{j-1}A_{j+1}
          \prod_{i\notin\{j-1,j,j+1\}}L_i.             \tag{29}
\]

Different choices give different subsets because the role supports are
disjoint.  Multiplying cyclically gives

\[
 \prod_j{B_j\over P_0}
   =\prod_i{A_iR_i\over L_i^3}
   \ge\prod_i{H_i\over L_i^3}.                         \tag{30}
\]

Therefore

\[
 \boxed{
 \max_jB_j\ge
 P_0\left(\prod_i{H_i\over L_i^3}\right)^{1/q}.}      \tag{31}
\]

This property holds in the previously verified infinitesimal radial and
fixed oriented-ear models, but Section 3.1 proves that it is not a
consequence of strong separation.  When it does hold, (31) is one
ordinary-face bank with decoder load one inside the fixed product: its
missing role and its intersections with all other disjoint supports
recover every choice.

For the coefficient calculation put `d=log D`, `s_i=log L_i`, and assume

\[
 \log P_0=\sum_i s_i\ge(a-o(1))d^2,
 \qquad q\le(\kappa+o(1))d,                            \tag{32}
\]

and the uniform local reservoir bound

\[
                    \log H_i\ge(c_0-o(1))s_i^2.        \tag{33}
\]

Taking logs in (31), then applying Cauchy, gives

\[
\begin{aligned}
 \log\max_jB_j
 &\ge \sum_i s_i+{c_0-o(1)\over q}\sum_i s_i^2
                   -{3\over q}\sum_i s_i\\
 &\ge \sum_i s_i+{c_0-o(1)\over q^2}
                    \left(\sum_i s_i\right)^2-O(d)\\
 &\ge\left[a+c_0(a/\kappa)^2-o(1)\right]d^2.          \tag{34}
\end{aligned}
\]

Equation (1) follows.  In particular,

\[
 (a,\kappa,c_0)=(1/4,1/4,1/4)
       \Longrightarrow a+c_0(a/\kappa)^2=1/2,          \tag{35}
\]

whereas `c_0=1/8` gives `3/8`.

The linear term in (34), including the exact `L_i^3` normalization, is
only `O(d)` because `q=Theta(d)` and `sum_i s_i=O(d^2)`.

## 5. The global context/base overlap audit

For each external context `c`, let `mathcal B_c` be the cyclic profile
bank produced from its retained product.  Define the aggregate overlap

\[
 \Lambda_B=\max_{F\in\mathcal F(P)}
                    |\{c:F\in\mathcal B_c\}|.          \tag{36}
\]

Double counting gives the exact and only automatic global inequality

\[
                         V(P)\ge {\sum_c|\mathcal B_c|\over\Lambda_B}.
                                                               \tag{37}
\]

There are two different regimes.

1. **One quadratic product.**  If one fixed context has (32), then (34)
   already lower-bounds `V(P)`.  No summation, base decoder, or context tag
   is used.  The root-bad circuit and the external base are omitted from
   every bank output.
2. **Distributed mass.**  If only `sum_c M_c` is large while every
   `P_{0,c}` is smaller than quadratic scale, (34) is merely local.  One
   needs an independent bound on `Lambda_B`, or a promotion which inserts
   the varying base blocks into a common recoverable cyclic container.

The second qualification is necessary.  Reuse the same separated supports
and hence the same bank `mathcal B` for `K` different root/base contexts
placed in a common root-bad pocket.  Then

\[
 |\mathcal B_c|=|\mathcal B|,qquad
 \sum_c|\mathcal B_c|=K|\mathcal B|,qquad
 \Lambda_B=K.                                         \tag{38}
\]

Equation (37) reduces to `V(P)>=|mathcal B|`.  The context multiplicity
can have quadratic entropy, so it cannot be discarded as a polynomial
decoder tax.  A two-output code `(context face,profile face)` has capacity
`V(P)^2` and does not repair this one-face summation loss.

This is exactly the cross-base regression already isolated in
`CROSS_BASE_ONE_GAP_REUSE_REGRESSION.md`.  Strong separation is a property
of the local supports; it does not encode an external context which is
absent from the output.

## 6. Exact remaining proof obligations

The root-bad branch would close at coefficient `1/2` after the following
three inputs are simultaneously verified.

1. **Ordered extraction.**  The live low-`R` fibre is sliced into an
   ordered/simple-chain certificate satisfying (CYC), with only
   `2^{o((log D)^2)}` loss.  The transcript theorem preserves such a
   certificate but does not create it.
2. **Lexicographic exposure.**  The retained product has a stronger
   common-tangent/ear state under which the conditional endpoint-profile
   property (28)--(29) holds.  It cannot be inferred from strong
   separation: (16)--(27) are a scalable counterexample.
3. **Global scale or decoder.**  Either one retained product itself obeys
   (32), or the aggregate banks have
   `Lambda_B=2^{o((log D)^2)}` (or are promoted into one common
   container).  Local banks cannot be charged once per base.

Inputs 1 and 2 are local geometry.  Input 3 is global bookkeeping.  The
Barany--Pach theorem settles only the singleton type between inputs 1 and
2.  Even a proof that the **live subclass** has the stronger exposure
state would close the root-bad branch only in the one-quadratic-product
regime; the distributed-context regime still needs a recoverable
base/container argument.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_strong_separation_root_bad_integration.py
```

The checker verifies the two small rational configurations, the scalable
`m=14` strongly separated regression, all `2^14-1` local faces, every
rank-three hidden-point witness, the endpoint-profile count failure, the
coefficient arithmetic, the finite cyclic product identity, and the sharp
identical-bank overlap calculation.
