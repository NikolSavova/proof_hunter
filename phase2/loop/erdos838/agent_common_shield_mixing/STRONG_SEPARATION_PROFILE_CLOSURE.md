# Strong separation does not supply endpoint profiles

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The proposed implication

\[
 \text{same cyclic transversal type}
   \Longrightarrow A_iR_i\ge H_i
   \text{ for the two rooted endpoint reservoirs}       \tag{1}
\]

is false, even for a complete product of redundancy zero and an
arbitrarily small convex child at one macro vertex.  Thus Proposition 3.3
of Barany--Pach cannot promote the live low-redundancy product to the
cyclic profile hypothesis.

For every `m>=14` there is an exact rational four-role product with one
`m`-point role `X_1` such that:

* every transversal is convex in the same cyclic role order, so the four
  supports are strongly separated;
* all `2^m-1` nonempty subsets of `X_1` are local ordinary faces; but
* after either role adjacent to `X_1` is omitted, every admissible trace in
  `X_1` has rank at most two.

Consequently each rooted profile family has size at most

\[
                   S_m=m+{m\choose2},                    \tag{2}
\]

and

\[
                   S_m^2<2^m-1=H_1.                     \tag{3}
\]

This kills not only the common-tangent proof but the abstract profile
capacity conclusion itself.  The cyclic multiplication formula remains
valid **conditionally** when compatible rooted profile families have
already been proved.  What fails is deriving those families from strong
separation, fixed transversal type, low redundancy, or small macro-cluster
diameter.

The counterexample is not an end-to-end low-face construction: its child
is convex and already contributes `2^m` local faces.  Its value is to
identify the exact missing operation.  A successful root-bad argument must
use the bad same-block four-circuits, for example by deleting a small set
of external roles that hits them, or by extracting a large matching of
external circuit traces.  It cannot quote same-type separation as a
multi-point substitution theorem.

## 1. Exact scalable product

Fix `m>=14`, put

\[
             \delta={1\over100m^2},\qquad
 P_t=(2-\delta t^2,-1/5+\delta t),\quad1\le t\le m,       \tag{4}
\]

and take the cyclic roles

\[
 X_1=\{P_1,\ldots,P_m\},\quad X_2=\{b=(4,0)\},\quad
 X_3=\{c=(0,4)\},\quad X_4=\{a=(0,0)\}.                 \tag{5}
\]

For `p=(x,y)`, direct determinants give

\[
\begin{aligned}
 \chi(P_t,b,c)&={44\over5}+4\delta(t^2-t)>0,\\
 \chi(P_t,b,a)&={4\over5}-4\delta t>0,\\
 \chi(P_t,c,a)&=8-4\delta t^2>0,\\
 \chi(b,c,a)&=16>0.                                    \tag{6}
\end{aligned}
\]

Thus every one of the `m` transversals has sign vector `(+,+,+,+)` on
the four role triples.  It is a convex quadrilateral in role order
`1,2,3,4`.  The transversals have one type, so Barany--Pach Proposition
3.3 makes the supports strongly separated.

The points `P_t` lie on the strictly concave parabola

\[
       x=2-{(y+1/5)^2\over\delta}.                       \tag{7}
\]

They are in convex position.  Every subset of `X_1` is therefore an
ordinary face, and its nonempty local face count is

\[
                              H_1=2^m-1.                 \tag{8}
\]

The diameter of `X_1` is `O(1/100)` uniformly in `m`: its horizontal
variation is less than `1/100` and its vertical variation is less than
`1/(100m)`.  More generally replace `delta` by `eta/m^2`.  All displayed
strict signs and the negative brackets in (9)--(10) persist for every
sufficiently small positive rational `eta`, while the diameter tends to
zero.  Hence
"infinitesimal child" is not a replacement for rooted profile
compatibility.

## 2. Every rank-three trace is blocked

Take `1<=i<j<k<=m`.  With

\[
 D_{ik}=\chi(P_i,P_k,c)
 =\delta(k-i)\left[2-{21\over5}(i+k)+\delta ik\right],   \tag{9}
\]

we have `D_ik<0`.  The three barycentric numerators of `P_j` in the
triangle `P_iP_kc` are

\[
\begin{aligned}
 \chi(P_j,P_k,c)
   &=\delta(k-j)\left[2-{21\over5}(j+k)+\delta jk\right]<0,\\
 \chi(P_i,P_j,c)
   &=\delta(j-i)\left[2-{21\over5}(i+j)+\delta ij\right]<0,\\
 \chi(P_i,P_k,P_j)
   &=\delta^2(k-i)(j-i)(j-k)<0.                          \tag{10}
\end{aligned}
\]

All three have the sign of `D_ik`, so

\[
                       P_j\in\operatorname{int}
                         \operatorname{conv}\{P_i,P_k,c\}. \tag{11}
\]

Both adjacent omissions retain role `X_3={c}`:

* omitting `X_2` leaves an endpoint trace in `X_1` together with `c,a`;
* omitting `X_4` leaves it together with `b,c`.

If the trace contains any three indices `i<j<k`, (11) makes the resulting
set nonconvex, independently of the additional singleton.  Every trace
which is uniformly admissible at either adjacent cut therefore has rank at
most two.  This proves (2).

At `m=14`,

\[
 S_{14}=105,\qquad S_{14}^2=11025<16383=2^{14}-1.        \tag{12}
\]

Moreover `S_(m+1)/S_m=(m+2)/m`, whose square is less than two for
`m>=14`, whereas `2^m` doubles.  Inequality (3) follows for every
`m>=14`.

No choice of canonical chains can evade this count: every member of either
actual endpoint family is one of the rank-at-most-two traces already
counted by `S_m`.

## 3. What survives from the cyclic product

Suppose, as an additional geometric hypothesis, role `i` has genuinely
compatible left and right rooted families of sizes `A_i,R_i`, and every
gap union is ordinary.  Then the exact gap bank and cyclic identity remain

\[
 B_j=R_{j-1}A_{j+1}
       \prod_{i\notin\{j-1,j,j+1\}}L_i,\qquad
 \prod_j{B_j\over P_0}
   =\prod_i{A_iR_i\over L_i^3}.                          \tag{13}
\]

Thus the familiar coefficient calculation

\[
              a+c_0(a/\kappa)^2-o(1)                    \tag{14}
\]

is correct **after** `A_iR_i>=H_i` has been established for the actual
rooted families.  At `a=kappa=c_0=1/4` it equals `1/2`.

The counterexample shows that the premise of (14) is not implied by:

1. a complete ambient product;
2. redundancy `R=0`;
3. one fixed convex cyclic transversal type;
4. Barany--Pach strong separation; or
5. an arbitrarily small child around its macro vertex.

Accordingly any use of the profile step in
`CENTRAL_SHELL_PROFILE_RECURRENCE.md`,
`DETACHED_RADIAL_LEXICOGRAPHIC_PROFILE.md`, or a root-bad integration must
retain its explicit rooted/cyclic compatibility hypothesis.  Ordinary
macro convexity and scale separation alone do not prove it.

## 4. Exact circuit-release replacement

There is a rigorous weaker branch which explains the right next target.
Let `F` be any family of local faces in a rich role, and let `J` be the
external roles retained by a proposed bank.  For every choice of one label
from each role in `J`, consider all planar bad four-circuits in its union
with a member of `F`.

> **Circuit hitting-set release.**  If a role set `T subseteq J` meets
> every such bad four-circuit, then deleting the roles in `T` makes every
> resulting union convex.  Hence the released bank has the exact size
>
> \[
>       |F|\prod_{j\in J\setminus T}|X_j|,               \tag{15}
> \]
>
> with load one inside the fixed role container.

Indeed, a nonconvex finite planar set in general position contains a
four-point circuit consisting of one point in the triangle of three
others.  If a union after deleting `T` were nonconvex, that circuit would
be one of the original bad circuits disjoint from `T`, contradicting the
hitting assumption.

Thus the honest dichotomy is now combinatorial: either the same-block bad
circuits have a small external-role transversal, yielding (15), or their
external traces have a large matching/codegree structure from which a
two-ended or crossing bank must be extracted.  Proposition 3.3 supplies
neither branch.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_strong_separation_profile_closure.py
```

The checker uses exact rational arithmetic.  It verifies all transversal
signs for `m=14`, convexity of `X_1`, every barycentric containment in
(11), the two rank-at-most-two endpoint bounds, the strict capacity
failure (12), persistence through `m=80`, and the conditional cyclic and
coefficient identities.

## Primary source

I. Barany and J. Pach, *Homogeneous selections from hyperplanes*, Journal
of Combinatorial Theory, Series B 104 (2014), 81--87, Proposition 3.3,
DOI `10.1016/j.jctb.2013.10.001`, author-hosted PDF:
`https://real.mtak.hu/21926/1/129.pdf`.
