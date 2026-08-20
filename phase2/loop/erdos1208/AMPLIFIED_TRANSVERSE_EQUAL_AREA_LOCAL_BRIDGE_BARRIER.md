# The amplified transverse system has only an equal-centroid local lift

## 1. Outcome

Fix one fully transverse third-translation record from
`AMPLIFIED_THIRD_TRANSLATION_LOCAL_TRANSVERSE_DICHOTOMY.md`.  Its complete
endpoint equations have a simple exact normal form.  They force two
equal-centroid identities,

\[
 x+c+d=y+a+b,                                           \tag{1.1}
\]

and

\[
 e+f+a+b=x+z+h+i.                                      \tag{1.2}
\]

They do **not** force an equal-area pair.  This distinction cannot be
repaired by retaining the scalar weight, the adaptive determinant cutoff,
all three anchors, or all target endpoints: the verifier contains a
28-point integral distance-Sidon certificate having one fully transverse
three-translation record of positive determinant-qualified scalar weight,
but having no six-distinct equal-area triangle pair anywhere in the set.

Thus there is no record-by-record charge from the transverse scalar system
to the existing six-distinct special-affine energy.  The certificate has
source codegree three, rather than the live codegree at least `k`.  It does
not disprove an aggregate high-codegree bridge.  It proves that such a
bridge must use the coexistence of many third translations; none of the
local coordinate identities supplies the missing determinant-one equation.

## 2. Exact coordinates of a transverse record

Let the ordered source pair be `p=(s,t)`.  Orient a one-role base
`q_1,q_2 in Q_p` by writing

\[
\begin{array}{lll}
 E(s+q_1)=\{x,z\},&E(s+q_2)=\{y,z\},&g=q_2-q_1=y-x,\\
 E(t+q_1)=\{a,b\},&E(t+q_2)=\{c,d\},&
        c+d-a-b=g.
\end{array}                                             \tag{2.1}
\]

For a fully transverse third translation `q_0`, write

\[
 E(s+q_0)=\{e,f\},\qquad E(t+q_0)=\{h,i\}.             \tag{2.2}
\]

Put `r_0=q_0-q_1`.  The complete pair-sum equations are

\[
\begin{aligned}
 y-x&=c+d-a-b,\\
 e+f-x-z&=h+i-a-b=r_0,\\
 s-t&=x+z-a-b=e+f-h-i.
\end{aligned}                                           \tag{2.3}
\]

Equations (1.1) and (1.2) follow by rearrangement.  They retain `q_1`,
`q_2`, and `q_0`: explicitly

\[
 q_1=x+z-s=a+b-t,quad
 q_2=y+z-s=c+d-t,quad
 q_0=e+f-s=h+i-t.                                      \tag{2.4}
\]

The anchor equations are independently retained as

\[
 q_j=A_j-B_j\qquad(j=0,1,2),                            \tag{2.5}
\]

with `\{A_0,B_0\}` disjoint from both base anchor edges.  Full
transversality further says

\[
 \{e,f\}\cap\{x,y,z\}=\varnothing,qquad
 \{h,i\}\cap\{a,b,c,d\}=\varnothing.                 \tag{2.6}
\]

These are all affine-linear consequences of the three-translation system.
In particular, (1.1) says that the triangles `(x,c,d)` and `(y,a,b)` have
the same centroid; it does not say that they have the same area.

There is an analogous canonical equal-centroid lift for every single clean
incidence.  If

\[
 q=A-B,quad E(S)=\{C,D\},\quad E(S+q)=\{E,F\},          \tag{2.7}
\]

then

\[
 A+C+D=B+E+F.                                          \tag{2.8}
\]

Writing `u=C-D`, `v=E-F`, its signed doubled-area defect is exactly

\[
\begin{aligned}
 2\Omega(q;S)
 &=2\bigl(\Delta(A,C,D)-\Delta(B,E,F)\bigr)\\
 &=\det(u,S-2A)-\det(v,S+q-2B).                         \tag{2.9}
\end{aligned}
\]

Neither cleanliness nor (2.3) makes (2.9) vanish.  Vanishing is precisely
the additional determinant-one condition needed to enter the
special-affine framework.

## 3. The scalar decoration is orthogonal to the area defect

The weight on the source pair is

\[
 V(p)=W_{r,L},\qquad
 r=-\frac{\delta(s)-\delta(t)}{18}.                    \tag{3.1}
\]

It supplies physical target edge pairs `(U,U')` satisfying

\[
 |U|^2-|U'|^2=r,qquad |2\det(U,U')|>L,                 \tag{3.2}
\]

and an endpoint wedge among their first edges.  This is a norm-difference
and high-area condition on a second endpoint system.  It does not set any
of the clean-incidence defects (2.9) to zero.  Formally one may rewrite a
norm gap as

\[
 |U|^2-|U'|^2=\det(U-U',J(U+U')),                       \tag{3.3}
\]

but `J(U+U')` need not be a realized difference of two points of `A`.
Deleting that endpoint-realizability requirement would therefore be an
invalid passage to equal-area triangles in `A`.

## 4. A verified local obstruction

The stored certificate has `k=28`, `N=binom(k,2)=378`, and lies in
`[0,m]^2` with `m=452256448`.  It has globally unique pair sums and globally
unique nonzero squared distances.  For its displayed source pair,

\[
 Q_p=\{q_1,q_2,q_0\},qquad
 (|H_{q_1}|,|H_{q_2}|,|H_{q_0}|)=(3,3,2).              \tag{4.1}
\]

The first two translations form a one-role base and the third is fully
transverse.  The source norm gap is `7272`, so `r=-404`.  At the adaptive
cutoff

\[
 L=N/|H_{q_1}|=126,                                    \tag{4.2}
\]

there are exactly two target representations of the gap `-404`.  Their
first edges share one endpoint, their doubled determinants are `-1604` and
`-2428`, and hence

\[
 V(p)=W_{-404,126}=1.                                  \tag{4.3}
\]

In the exact reverse-switch notation, putting

\[
 v=s+q_1=x+z,qquad w=t+q_1=a+b
\]

gives `v in P_g`, `w in H_g subset B_g`, and
`v,w in X_(q_1,g)`.  Thus this is not merely an abstract one-role pattern:
it is a literal endpoint record of the amplified mass before imposing its
high-codegree cutoff.

Nevertheless every one of the `binom(28,3)=3276` geometric triangles is
noncollinear and

\[
 \boxed{\mathcal E_{\Delta,\ne0}^{(6)}(A)=0.}          \tag{4.4}
\]

In particular, even the two same-centroid triangle pairs canonically
visible in (1.1) and (2.8) have unequal areas.

This certificate is below the high-codegree threshold: `c(p)=3<28`.
That limitation is substantive.  It leaves exactly one possible bridge:
for `c(p)>=k`, use relations **between distinct third translations** to
force many equal-area/special-affine records, with bounded reverse
multiplicity and the common scalar weight still attached to `p`.  A local
map depending on only `(p,q_1,q_2,q_0)` is impossible by (4.4).

One precise sufficient next lemma is therefore a high-codegree collective
extraction statement.  For every weighted base record `C`, it would have
to assign a family of pairs `(q_0,q_0')` from its transverse extension set
to six-distinct determinant-one affine maps, in such a way that

1. a positive proportion of the `T(C)` choices is covered after the
   necessary size bias;
2. the reverse multiplicity is `m^{o(1)}` after retaining `p,q_1,q_2` and
   the scalar gap; and
3. the resulting maps lie in an aggregate-controlled low-denominator
   trace class.

No such collective extraction is presently proved.  The certificate shows
why the word “collective” cannot be dropped.

## 5. Verification

Run

```bash
python phase2/loop/erdos1208/verify_amplified_transverse_equal_area_local_bridge_barrier.py
```

The verifier checks all endpoint equations (2.1)--(2.6), all six clean
rows, the exact codegree and fibre sizes (4.1), full transversality, the
scalar gap and determinant-qualified wedge (4.3), global distance and
pair-sum Sidonicity, the area-defect formula (2.9), and the exhaustive
zero-energy statement (4.4).
