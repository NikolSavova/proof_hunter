# Integer-trace product compression and the parabolic aggregate gate

## Status

Let $A\subset [m]^2$ be distance-Sidon, and let

\[
 g(x)=Mx+t,\qquad M\in \operatorname{SL}_2(\mathbb Q),
 \qquad T=\operatorname{tr}M\in\mathbb Z
\]

carry one ordered triangle of $A$ to another.  Put

\[
 Q_M(v)=\det(v,Mv).
\]

This note records three exact conclusions.

1.  If $T\ne\pm2$, then for fixed $M$ and fixed nonzero product
    $P=Q_M(e_1)Q_M(e_3)$, **all translations together** support only
    $m^{o(1)}$ fully transverse ordered triangle records.  Thus the two
    invariant-form values can be compressed to their product.
2.  If $T=\pm2$, then $Q_M$ is a scaled square of one linear form.  The
    three side values lie in one signed squareclass, and the leading
    cross-determinant minor is a perfect square:
    \[
      K_{11}K_{22}=(K_{12}\mp d)^2.
    \]
3.  Reorganizing all equal-area records by a corresponding base-edge pair
    gives the exact size-biased envelope
    \[
      E_{\rm ft}\le
      \left(\sum_u 2e_u\sqrt{k+2e_u}\right)^2
      \ll k^5+m^4.                                    \tag{0.1}
    \]
    Here $e_u$ is the number of unordered edges of $A$ parallel to the
    primitive direction $u$.

The first two statements are genuine new fibre structure, but they do not
close the corrected target $m^{o(1)}(k^3+m^2)$.  The product has an
$O(m^4)$ rather than an $O(m^2)$ a priori range, while the universal
line-correlation envelope (0.1) is much too large.  Consequently this is a
precise gate, not a solution of the fully transverse equal-area problem.

## 1. Product-fibre compression away from trace $\boldsymbol{\pm2}$

Recall the compatibility lattice

\[
 \Lambda_M=\{v\in\mathbb Z^2:Mv\in\mathbb Z^2\}.
\]

For integer $T\ne\pm2$, `INTEGER_TRACE_INVARIANT_FORM_PELL_GATE.md`
proves uniformly, for every nonzero polynomial-size $q$,

\[
 \#\{v\in\Lambda_M\cap[-m,m]^2:Q_M(v)=q\}=m^{o(1)}.   \tag{1.1}
\]

### Theorem 1.1 (fixed-product fibre)

Fix $M\in\operatorname{SL}_2(\mathbb Q)$ with
$T\in\mathbb Z\setminus\{\pm2\}$, and fix $P\ne0$.  Among all translations
$t$, the number of fully transverse ordered source triangles
$(a,b,c)\in A^3$ for which $g(a),g(b),g(c)\in A$ and

\[
 Q_M(b-a)Q_M(a-c)=P                              \tag{1.2}
\]

is $m^{o(1)}$.

### Proof

Write $q_1=Q_M(b-a)$ and $q_3=Q_M(a-c)$.  Full transversality makes both
nonzero.  Since both the source and image vectors are differences of points
of $[m]^2$,

\[
 |q_i|=|\det(e_i,Me_i)|\le 2m^2.                       \tag{1.3}
\]

There are at most $2\tau(|P|)$ signed factor pairs $q_1q_3=P$.  For each
pair, (1.1) supplies $m^{o(1)}$ choices for each of the two directed edge
vectors.

A directed vector has at most one realization as a difference of two
points of $A$: two realizations would give two unordered pairs at the same
Euclidean distance.  Hence the two vectors determine at most one source
triangle.  The directed image of either vector likewise has at most one
realization in $A$, so it also determines at most one target anchoring and
one translation $t$.  Summing over the divisor-many factor pairs proves the
claim. $\square$

This improves the fixed-$(q_1,q_3)$ fibre theorem to a fixed-$P$ theorem.
It does **not** provide ambient compression, because (1.3) only yields

\[
 0<|P|\le4m^4.                                         \tag{1.4}
\]

The Pell--Heron identity

\[
 (q_1+q_3-q_2)^2+(4-T^2)d^2=4P                        \tag{1.5}
\]

does not by itself reduce this range: its remaining integer parameters can
still vary on the $m^2$ scale.

## 2. Exact parabolic normal form

Write $\varepsilon=T/2\in\{1,-1\}$.  If $M=\varepsilon I$, every
corresponding side pair is parallel, so there is no fully transverse
record.  Otherwise

\[
 N=M-\varepsilon I
\]

is a nonzero rank-one nilpotent matrix.  Its image equals its kernel.  Thus
there are a rational vector $w$ and a rational linear form $L$, with
$L(w)=0$, such that $Nv=L(v)w$.  Because every linear form vanishing on
$w$ is proportional to $v\mapsto\det(v,w)$, there is a fixed
$c\in\mathbb Q^*$ such that

\[
 \boxed{Q_M(v)=\det(v,Nv)=cL(v)^2.}                    \tag{2.1}
\]

On the compatibility lattice one may normalize $L$ to be primitive
integral and retain a fixed rational scale $c$.  In particular, all nonzero
values of $Q_M$ have the same signed rational squareclass.

For cyclic triangle sides $e_1+e_2+e_3=0$, let $r_i=L(e_i)$.  Then

\[
 r_1+r_2+r_3=0,\qquad q_i=cr_i^2.                      \tag{2.2}

The Pell--Heron identity degenerates exactly to

\[
 (q_1+q_3-q_2)^2=4q_1q_3.                             \tag{2.3}

This explains why fixed-value Pell counting fails here: a nonzero value
fibre is a union of parallel lines.

There is also a useful coordinate-free statement in the $3\times3$
cross-determinant matrix.  Let $f_i=Me_i$,
$K_{ij}=\det(e_i,f_j)$, and $d=\det(e_1,e_2)$.  The two exact identities

\[
 K_{11}K_{22}-K_{12}K_{21}=d^2,
 \qquad K_{12}-K_{21}=Td                              \tag{2.4}
\]

give

\[
 \boxed{K_{11}K_{22}=(K_{12}-\varepsilon d)^2.}        \tag{2.5}
\]

Thus trace $2$ uses $(K_{12}-d)^2$ and trace $-2$ uses
$(K_{12}+d)^2$.

## 3. The exact base-edge line-correlation envelope

For a primitive unoriented direction $u$, let $e_u$ be the number of
unordered edges of $A$ parallel to $u$.  If $n_u(s)$ are the occupancies of
the lines parallel to $u$, indexed by $s=\det(u,x)$, then

\[
 \sum_s n_u(s)^2=k+2e_u.                               \tag{3.1}
\]

Fix ordered source and target base edges $(a,b)$ and $(a',b')$, and write
$v=b-a$, $v'=b'-a'$.  A pair of third vertices $c,c'$ gives equal signed
area precisely when

\[
 \det(v,c-a)=\det(v',c'-a'),
\]

or equivalently

\[
 \det(v',c')=\det(v,c)+\det(v',a')-\det(v,a).          \tag{3.2}
\]

Therefore the number of compatible third-vertex pairs is one shifted
correlation of the two parallel-line occupancy sequences.  Cauchy--Schwarz
and (3.1) give

\[
 C((a,b),(a',b'))
 \le\sqrt{(k+2e_u)(k+2e_{u'})}.                        \tag{3.3}
\]

Every fully transverse ordered equal-area pair has a designated first
base-edge pair and is included in this count.  There are $2e_u$ ordered
base edges in direction $u$.  Summing (3.3) proves the first inequality in
(0.1).

To estimate it, put $N=\binom{k}{2}=\sum_u e_u$.  Then

\[
 \sum_u2e_u\sqrt{k+2e_u}
 \le 2N\sqrt{k}+2\sqrt2\sum_u e_u^{3/2}.               \tag{3.4}
\]

If $\|u\|_\infty=q$, distance-Sidonicity gives $e_u\le m/q$: for each
integer multiple $ru$, at most one edge can have that vector length.  There
are $O(q)$ primitive directions of sup-norm $q$, whence

\[
 \sum_u e_u^{3/2}
 \ll\sum_{q\le m}q(m/q)^{3/2}\ll m^2.                 \tag{3.5}
\]

Equations (3.4)--(3.5) establish (0.1).  Notice that this calculation
already retains the size bias of rich directions.  What it loses is the
simultaneous compatibility of the other two side correspondences and the
arithmetic restriction on the affine trace.

## 4. Parabolic stress is material

The verifier enumerates fully transverse, six-distinct, equal-signed
ordered triangle pairs in transformed Costas certificates:

| prime $p$ | $k$ | all fully transverse | trace $+2$ | trace $-2$ |
|---:|---:|---:|---:|---:|
| 11 | 10 | 1,260 | 0 | 48 |
| 13 | 12 | 6,876 | 156 | 108 |
| 17 | 16 | 32,292 | 444 | 624 |

Thus the parabolic exception is not empty or numerically negligible.  Each
of these records satisfies (2.3) and (2.5) exactly.

## 5. Remaining gate

The nonparabolic theorem reduces a fixed affine linear part to the product
key $P$, but that key has $m^4$ ambient range.  The parabolic theorem reduces
the form to one longitudinal coordinate, but its fibres may contain whole
parallel-line slices.  Finally, the strongest universal aggregation of
those slices obtainable from one corresponding base-edge pair is only
$O(k^5+m^4)$.

A successful continuation must therefore use at least one genuinely
three-side constraint.  Concretely, it must either

* compress the occupied products $P$ across endpoint-realized maps to
  $m^{2+o(1)}$ effective mass,
* obtain a rich-map tail coupling $P$ to the translation/overlap size, or
* in the parabolic case, combine the three relations $r_1+r_2+r_3=0$ with
  global distance-label injectivity more strongly than separate line
  correlations.

The one-base-edge size-biased energy method alone does not deliver the
corrected ambient bound.

## 6. Verification

Run:

```bash
python phase2/loop/erdos1208/verify_integer_trace_product_parabolic_aggregate_gate.py
```
