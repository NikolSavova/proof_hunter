# Nearby-anchor tangent intervals: exact reduction and anti-alignment gate

**Date:** 2026-08-15. All faces below are ordinary (convex-position)
subsets. Empty bases are allowed in extension counts.

## Verdict

Moving a second anchor infinitesimally close to a fixed anchor really does
reduce its pair interaction to a weighted interval-depth problem on the
projective line. The resulting interval dichotomy is exact:

\[
 J_Q(u,u+\epsilon d)=A_Q(u)-H_u([d]),
 \qquad
 \Pr(I_R\cap I_S\ne\varnothing)\le 2h .                 \tag{1}
\]

Here $I_R$ is the projectivized inward tangent cone at $u$ of the face
$R\cup\{u\}$, $H_u(\theta)$ is its weighted depth, and $h$ is the maximum
normalized depth. Thus low depth produces quadratically many pairs of
base faces whose cones are disjoint.

However, **disjoint tangent cones do not imply an ordinary union, even
with exponential local face entropy**. There is a scalable rational
configuration with one convex $m$-point child, one fixed two-point shield,
and disjoint root cones for every child face of rank at least two, yet only
the $m$ singleton child faces coexist with the shield. Hence the interval
dichotomy alone does not give the missing two-ended cap--cup converter. It
must be supplemented by a cross-support condition: lexicographic
separation, an already-ordinary detached union, or a recoverable
circuit/shield output.

## 1. Exact infinitesimal interval formula

Fix a finite general-position set $Q\subset\mathbb R^2$, a point
$u\notin Q$, and put

\[
 \mathcal R_u=\{R\subseteq Q:R\cup\{u\}\text{ is ordinary}\},
 \qquad A_Q(u)=|\mathcal R_u|.                            \tag{2}
\]

For $|R|\ge2$, let $p_R,q_R$ be the two neighbours of $u$ on the boundary
of $\operatorname{conv}(R\cup\{u\})$. The inward cone at $u$ is the open
cone between the rays $up_R,uq_R$ containing the rest of the polygon.
Since its angle is strictly less than $\pi$, its image in
$\mathbb {RP}^1$ is a proper interval $I_R$. Set
$I_R=\varnothing$ when $|R|\le1$.

> **Theorem 1 (nearby-anchor formula).** Fix a projective direction
> $\theta=[d]$ which is not an endpoint of any $I_R$. For all sufficiently
> small $\epsilon>0$, with $v=u+\epsilon d$,
>
> \[
> R\cup\{u,v\}\text{ is ordinary}
>       \quad\Longleftrightarrow\quad
> R\in\mathcal R_u\text{ and }\theta\notin I_R.           \tag{3}
> \]
>
> Consequently,
>
> \[
> J_Q(u,v)=A_Q(u)-H_u(\theta),\qquad
> H_u(\theta)=|\{R\in\mathcal R_u:\theta\in I_R\}|.       \tag{4}
> \]

**Proof.** Heredity gives
$R\cup\{u,v\}$ ordinary $\Rightarrow R\cup\{u\}$ ordinary. Suppose
$R\cup\{u\}$ is ordinary. If the oriented ray $d$ lies in the inward cone,
then $v$ is locally hidden by the two incident edges. If $-d$ lies there,
then $u$ is locally hidden after $v$ is inserted. These are the same
condition $[d]\in I_R$ on the projective line. Outside that projective
interval, $u,v$ replace $u$ by two consecutive boundary vertices. All
inequalities are strict, and there are finitely many $R$, so one common
$\epsilon_0>0$ works. The cases $|R|\le1$ are immediate. Summing (3)
proves (4). $\square$

The theorem does not use minimality. If $u$ lies in a minimum
one-point-extension cell of $Q$, it says only that the baseline $A_Q(u)$
is minimum; it does not constrain the relative positions of the intervals
$I_R$.

The same proof is coefficientwise and weighted. For weights $w_R\ge0$,
replace $A,H,J$ by the corresponding weighted sums.

## 2. Weighted interval dichotomy

Let $\mathcal I$ be any finite weighted family of proper intervals on an
oriented circle (in particular on $\mathbb {RP}^1$). Put

\[
 W=\sum_{I\in\mathcal I}w_I,
 \qquad h=\max_\theta\sum_{I\ni\theta}w_I.                \tag{5}
\]

> **Theorem 2 (two-endpoint charging).**
>
> \[
> \sum_{I,J}w_Iw_J\,1_{I\cap J\ne\varnothing}\le2Wh.     \tag{6}
> \]
>
> In particular, the ordered weight of disjoint pairs is at least
> $W^2-2Wh$.

**Proof.** Give each proper interval its initial endpoint in the fixed
cyclic orientation. If two circular intervals meet, then the initial
endpoint of one lies in the other. Therefore

\[
 1_{I\cap J\ne\varnothing}
 \le 1_{\ell(I)\in J}+1_{\ell(J)\in I}.
\]

For fixed $I$, the $J$-weight of the first event is at most $h$; the other
term is symmetric. $\square$

Thus $h\le W/4$ gives at least $W^2/2$ disjoint ordered pairs. This is the
strongest conclusion available from interval depth alone.

## 3. Scalable stretchable anti-alignment

For $m\ge3$, let

\[
 \epsilon={1\over100m},\quad u=(0,0),\quad
 r_i=\left(i,{i\over10}+\epsilon i(m-i)\right)
       \quad(1\le i\le m),                               \tag{7}
\]

and

\[
 s_1=(0,m^2),\qquad s_2=(-1,1),\qquad
 R_m=\{r_1,\ldots,r_m\},\quad S=\{s_1,s_2\}.             \tag{8}
\]

All displayed coordinates are rational. The child $R_m\cup\{u\}$ is in
general position. If one of the finitely many cross triples is
accidentally collinear for a particular $m$, perturb $s_2$ by an
arbitrarily small rational amount; every inequality below is strict, so
this preserves all claims and gives a rational general-position
realization. No perturbation is needed for the verified instance $m=14$.

The points $u,r_1,\ldots,r_m$ lie on a strictly concave quadratic graph,
above the chord $ur_m$, so they are in convex position. Hence all $2^m-1$
nonempty subsets $F\subseteq R_m$ give ordinary faces
$F\cup\{u\}$. Also $S\cup\{u\}$ is a triangle.

Every ray $ur_i$ has slope

\[
 {1\over10}+\epsilon(m-i)\in[1/10,11/100),               \tag{9}
\]

whereas the cone of $S\cup\{u\}$ is the projective interval between the
vertical ray and slope $-1$. Thus for every $|F|\ge2$,

\[
                         I_F\cap I_S=\varnothing.         \tag{10}
\]

Nevertheless, if $r_i,r_k\in F$ with $i<k$, then

\[
 r_i={i\over k}r_k+
       {\epsilon i(k-i)\over m^2}s_1+
       \left(1-{i\over k}-{\epsilon i(k-i)\over m^2}\right)u .
                                                               \tag{11}
\]

All three coefficients are strictly positive: the last one is positive
because $i/k\le1-1/k$ and
$\epsilon i(k-i)/m^2<1/(100m)<1/k$. Thus $r_i$ is strictly inside
$\operatorname{tri}(u,r_k,s_1)$, and

\[
 F\cup S\cup\{u\}\text{ is ordinary}
                   \quad\Longleftrightarrow\quad |F|\le1.       \tag{12}
\]

So an exponential $2^m-1$ root-face bank with completely disjoint cone
profiles has only $m$ nonempty traces compatible with the opposite shield.
The loss is exponential, not a decoder artifact.

## 4. Consequence for the live gate

The minimum-cell/nearby-anchor proposal supplies a useful exact statistic:
high interval depth makes $J_Q(u,v)$ small in a chosen direction, while
low depth produces many disjoint cone pairs. But (7)--(12) show that the
second branch is not yet a two-ended ordinary-face bank. Tangent cones
record only the two edges incident to the common root; they do not stop a
far point of one support from hiding almost the entire other support.

Therefore a valid converter must retain at least one further coordinate:

1. a detached-union certificate $R\cup S$ (or a face containing it);
2. a lexicographic/strong-seam condition controlling every cross-support
   four-set; or
3. a marked hiding circuit whose output is itself banked with bounded
   physical-history load.

This is consistent with the exact two-anchor sign classification in
TWO_ANCHOR_DOUBLE_CIRCUIT_ELIMINATION_GATE.md: local root signs and local
tangent intervals both miss the same far-support hiding operation.

## 5. Verification

The verifier verify_nearby_anchor_tangent_interval_antialignment_gate.py
checks the circle-interval charging implication exhaustively on all binary
weighted families of the twelve proper discrete intervals on a
four-cycle. It then uses exact rational arithmetic for $m=14$ to verify
general position, the convex $2^{14}-1$ child bank, cone separation, the
barycentric identities (11), and the exact compatibility count $14$.
