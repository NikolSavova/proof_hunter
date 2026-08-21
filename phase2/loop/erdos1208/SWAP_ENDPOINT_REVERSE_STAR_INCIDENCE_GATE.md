# The reverse endpoint-star incidence gate

## 1. Outcome

This note rewrites the second-generation endpoint pencil in the variables
that retain both its physical endpoint and its orthogonal self-switch.  It
also proves a support-growth theorem for every fixed base-overlap start.

Let `A` be a planar lattice distance-Sidon set, put

\[
 D=A-A,\qquad S=|D+D|,
\]

and let `J(x,y)=(-y,x)` and `L=I+J`.  Fix a centre cell

\[
 C=(c,\ell),\qquad H=\ell+Jc,
\]

a physical endpoint `x in A`, and a nonzero switch `u`.  For a neighbour
displacement `t`, recall

\[
 Q_{C,t}=\{q:q,q+t\in\mathcal P_K,
 c-q,\ \ell+Jq+Jt,\ \ell+Jq+Lt\in D\}.
\]

Write `a_t(u)=R_{Q_{C,t}}(u)`.  The exact reverse records counted by
`a_t(u)` are pairs `(t,X)` satisfying six translated `D` memberships, four
popular-corner memberships, and one physical endpoint-star condition.  In
these variables the neighbour label, rather than the centre, is the only
free geometric direction.

The main positive theorem is the following.  Fix `X` and one of the four
oriented endpoint roles.  If `T_X` is the set of neighbour displacements
supporting reverse records in that role, then

\[
 \boxed{S\ge { |T_X|^4\over 2|T_X|^2-|T_X|}
        \ge {|T_X|^2\over2}.}                    \tag{1.1}
\]

Thus every fixed-`X`, fixed-role reverse star has size at most
`sqrt(2S)`.  The proof uses the physical fact that one oriented endpoint
star is a vector-Sidon set; it is false for an arbitrary index set.

This does not yet close the aggregate collision theorem.  It identifies
the exact missing step: globally pack the support footprints (1.1), or the
popular vertices they create, across different centres and base starts
without paying their full reverse multiplicity.

## 2. Exact reverse normal form

For an ordered pair `q,q-u in Q_{C,t}`, define

\[
 X=c-q,\qquad
 Y=H-JX+Jt,\qquad
 Z=H-JX+Lt.                                      \tag{2.1}
\]

Then the defining conditions are exactly

\[
\boxed{
\begin{gathered}
 X,X+u\in D,\\
 Y,Y-Ju\in D,\\
 Z,Z-Ju\in D,                                    \tag{2.2}\\
 c-X,c-X-u,c-X+t,c-X-u+t\in\mathcal P_K,
\end{gathered}}
\]

together with

\[
 x\in\partial(c+t)\cup\partial(\ell+Lt),        \tag{2.3}
\]

where `partial(v)` is the two-element endpoint set of the uniquely
represented nonzero directed difference `v`.  Conversely (2.1)--(2.3)
recover `q=c-X` and hence the ordered internal pair.  Therefore

\[
 \boxed{a_t(u)=|\{X:(t,X)\text{ satisfies (2.1)--(2.3)}\}|.} \tag{2.4}
\]

The three moving vectors obey

\[
 Z-Y=t,
 \qquad LY-JZ+JX=H.                              \tag{2.5}
\]

In particular any two of `X,Y,Z` recover the third.  The map

\[
 (t,X)\longmapsto((X,X+u),(Y,Y-Ju))              \tag{2.6}
\]

is injective for fixed `C`, giving again

\[
 \sum_ta_t(u)\le R_D(u)R_D(Ju).                 \tag{2.7}
\]

Unlike the bare product bound, (2.1)--(2.3) retain the endpoint star and
the third `Ju` overlap `(Z,Z-Ju)`.

### 2.1 Four popular-completion vertices

For a shift `r`, define its perpendicular completion set

\[
 \mathcal C(r)=\{(A,B):A,A+r,B,B+Jr\in D\}.     \tag{2.8}
\]

Thus `|mathcal C(r)|=R_D(r)R_D(Jr)`.  For one reverse record, put

\[
 q=c-X,\qquad p=q+t,\qquad W=\ell+Lt.           \tag{2.9}
\]

Then (2.2) is equivalently the four simultaneous completion memberships

\[
\boxed{
\begin{array}{ll}
 (X,\ell)\in\mathcal C(p),
   &(X+u,\ell)\in\mathcal C(p-u),\\
 (X,W)\in\mathcal C(q),
   &(X+u,W)\in\mathcal C(q-u),
\end{array}}                                      \tag{2.10}
\]

together with

\[
 W-\ell=L(p-q)                                    \tag{2.11}
\]

and the endpoint condition that `x` lies on `X+p` or `W`.  Conversely
(2.10)--(2.11) recover

\[
 c=X+q,\qquad t=p-q,\qquad C=(c,\ell),           \tag{2.12}
\]

and all six vectors in (2.2).  Hence the popular self-switch is literally
a square of four vertices in the completion space, with aligned first
coordinates `X,X+u` and aligned second coordinates `ell,W`.

The total number of available popular-completion vertices is exactly

\[
 \sum_{r\in\mathcal P_K}|\mathcal C(r)|
 =\sum_{r\in\mathcal P_K}R_D(r)R_D(Jr),          \tag{2.13}
\]

the original adaptive perpendicular tail.  This is the correct global
reservoir for a density-increment proof.  A black-box additive-energy bound
for `mathcal P_K` loses the aligned completion coordinates in (2.10) and is
therefore strictly weaker.

### 2.2 Global diagonal reconstruction

Let

\[
 \mathcal V_K=\{(r,A,B):r\in\mathcal P_K,
                         (A,B)\in\mathcal C(r)\}.     \tag{2.14}
\]

The centre factor in the crude product estimate (2.7) disappears if one
keeps a crossed diagonal of the square.  Take

\[
 v=(p,X,\ell),\qquad w=(r,X',W)\in\mathcal V_K       \tag{2.15}
\]

and put

\[
 u=X'-X,\qquad q=r+u,\qquad t=p-q.                   \tag{2.16}
\]

Call `(v,w)` admissible when `u,t` are nonzero,

\[
 W-\ell=Lt,                                           \tag{2.17}
\]

and the two complementary vertices

\[
 (p-u,X',\ell),\qquad(q,X,W)                         \tag{2.18}
\]

also belong to `mathcal V_K`.  Then an admissible diagonal recovers

\[
 c=X+q,qquad C=(c,\ell),\qquad
 (V,W)=(X+p,W),                                      \tag{2.19}
\]

and hence the entire reverse record except for the choice of a physical
endpoint of the neighbour cell `(V,W)`.  Each nonzero label has its unique
two endpoints, so there are at most four such choices (and possibly none
for a purely algebraic admissible diagonal with zero labels).  Conversely
every genuine reverse endpoint record gives the admissible diagonal

\[
 ((p,X,\ell),(q-u,X+u,W)).                            \tag{2.20}
\]

Thus the reverse map is globally bounded-to-one after retaining completion
coordinates; no sum over centres is necessary.  The hard aggregate is now
the endpoint-labelled, within-`(C,u)` pair energy of admissible diagonals in
`mathcal V_K`.  A pair of diagonals in one such pencil creates a fully
labelled eight-vertex completion configuration.  This is the precise
higher-energy/density-increment formulation of the popular self-switch;
no unproved cube independence is asserted here.

## 3. The four endpoint roles are Sidon

The neighbour cell has directed labels

\[
 V_t=c+t,\qquad W_t=\ell+Lt.                    \tag{3.1}
\]

After fixing which label contains `x` and whether `x` is its head or tail,
the possible `t` lie in one of

\[
\begin{array}{ll}
 x-A-c,&A-x-c,\\
 L^{-1}(x-A-\ell),&L^{-1}(A-x-\ell),
\end{array}                                      \tag{3.2}
\]

with the zero edge removed and only integral preimages retained.  Each set
in (3.2) is vector-Sidon.  For the first two this is immediate from the
directed-difference uniqueness of `A`; for the last two, applying the
injective map `L` reduces equality of two differences to the same fact.

Consequently every nonzero vector has at most one ordered representation
as a difference of two members of a fixed role set.

## 4. A quadratic support footprint

Fix `X` and one role, and let `T=T_X`.  For every `t in T`, (2.2) places

\[
 Y_t=H-JX+Jt,qquad Z_t=H-JX+Lt                  \tag{4.1}
\]

in `D`.  Hence `D+D` contains a translate of

\[
 JT+LT.                                          \tag{4.2}
\]

Put `h=|T|`.  The additive energy of (4.2) counts

\[
 Jt_1+Lt_2=Jt_3+Lt_4.                           \tag{4.3}
\]

Writing `d=t_1-t_3` and `e=t_4-t_2`, (4.3) is

\[
 Jd=Le,qquad d=(I-J)e.                          \tag{4.4}
\]

There are `h^2` zero solutions.  For `e ne 0`, vector-Sidonicity gives at
most one ordered pair `(t_4,t_2)`, and then at most one ordered pair
`(t_1,t_3)` for the forced value `(I-J)e`.  There are only `h(h-1)`
possible nonzero ordered differences `e`.  Thus

\[
 E_+(JT,LT)\le h^2+h(h-1)=2h^2-h.               \tag{4.5}
\]

Cauchy--Schwarz applied to (4.2) proves (1.1).

Splitting into four endpoint roles gives the unconditional local degree
bound

\[
 \#\{t:(t,X)\text{ is a reverse record}\}
 \le4\sqrt{2S}.                                  \tag{4.6}
\]

Since the possible `X` lie in `D cap (D-u)`, (4.6) and (2.7) yield

\[
 \boxed{
 \Lambda_2(C,x,u)le
 \min\{4R_D(u)\sqrt{2S},\ R_D(u)R_D(Ju)\}.}     \tag{4.7}
\]

## 5. Popularity retained by a high-degree star

For fixed `X`, put `q=c-X`.  Distinct `t in T_X` give distinct
`p=q+t`, and (2.2) retains

\[
 q,q-u,p,p-u\in\mathcal P_K.                    \tag{5.1}
\]

Therefore a fixed-`X` star of size `h` exposes `h` distinct popular shifts
and literally contributes more than

\[
 hK^2                                             \tag{5.2}
\]

to `sum_{p in P_K}R_D(p)R_D(Jp)`.  Formula (5.2) is not yet globally
summable because the same popular `p` may be reused by many
`(C,x,u,X)` anchors.  Bounding precisely that reuse, or showing that high
reuse creates a larger support footprint, is the remaining density-
increment problem.

## 6. Aggregate collision target

Let

\[
 \mathcal R_{C,x,u}=\{(t,X):(2.1)--(2.3)\},
 \qquad \Lambda_2=|\mathcal R_{C,x,u}|.
\]

Its fibres over `t` have sizes `a_t(u)`.  If `a_*` is the largest fibre,
the exact size-biased envelope from the endpoint-pencil reduction is

\[
 \mathcal G_2=
 \sum_{C,x,u\ne0}(\Lambda_2-a_*)\Lambda_2,       \tag{6.1}
\]

and `2Q_end<=mathcal G_2`.  The desired theorem is

\[
 \boxed{\mathcal G_2\le N^{o(1)}W_{\rm parallel}.} \tag{6.2}
\]

Equations (4.7) and (5.2) rigorously close projection-sparse or
low-reuse subfamilies, but they do not by themselves sum (6.1).  A valid
completion must correlate the popular-vertex reuse in (5.2) with the
translated support footprints (4.2).  Replacing this correlation by a
maximum fibre or by the unlabelled product `R_D(u)R_D(Ju)` reintroduces the
known component-size loss.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_endpoint_reverse_star_incidence.py
```

The verifier checks the bijection (2.1)--(2.5), the completion square
(2.8)--(2.12), the global diagonal reconstruction (2.14)--(2.20), the
product injection, all four endpoint-role Sidon
statements, and the exact energy calculation (4.3)--(4.5) on finite
distance-Sidon samples.
