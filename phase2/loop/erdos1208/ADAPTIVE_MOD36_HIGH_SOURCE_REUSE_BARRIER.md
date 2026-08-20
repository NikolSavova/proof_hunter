# Adaptive mod-36 packing: high same-source reuse

## Status

The disjoint-union theorem gives

\[
X_{36}\le 153G(m)m^2\mu_{\max}\Delta,
\tag{0.1}
\]

where \(\mu(p)\) is the number of tail translations containing one fixed
source pair \(p\), and \(\Delta\) is the depth of the full residual
supports across distinct source pairs.

This note resolves the first structural question about the factor
\(\mu_{\max}\).

**Exact capacity theorem.** If the two source edges of a selected pair
\(p\) use four distinct points, and \(I_p\) is its set of isolated
directed anchors, then

\[
\boxed{
\mu(p)\le |I_p|\le k-4.
}
\tag{0.2}
\]

Indeed, the heads of the isolated directed anchors are distinct, and every
head avoids the four source endpoints. The same holds for their tails.
Oppositely oriented incidences can meet in directed paths or cycles, so
\((k-4)/2\) is valid only in the literal underlying-matching subcase.

The linear size of (0.2) is genuinely attainable at polynomial height,
even in the fully metric adaptive setting. There are integral
distance-Sidon families with two selected source pairs
\(p_0,p_1\) and \(J=\Theta(k)\) distinct translations such that

\[
\begin{aligned}
H_{q_j}&=\{s_0,t_0,s_1,t_1\},\\
h_{q_j}&=4,\qquad e_{q_j}=2,\qquad b_{q_j}=1,\\
U_N(r)&=k
\end{aligned}
\tag{0.3}
\]

for every \(j\). Both source pairs have all \(J\) anchors as their exact
common-translation matching. Their source areas lie in one mod-36 class,
but their normalized residual supports are disjoint.

Every tie ordering leaves one of the two records in the tail of each
translation. Therefore

\[
\boxed{
X_{36}=Jk=\Theta(k^2)=\Theta(H_Q),
\qquad
\mu_{\max}\Delta\ge \frac{J}{2}=\Theta(k),
\qquad
\Delta=1.
}
\tag{0.4}
\]

With a consistent tie ordering, one fixed source pair is tail in all
\(J\) translations, so \(\mu_{\max}=J\).

This is not a counterexample to \(X_{36}\le m^{o(1)}H_Q\); it saturates
that estimate. It is a genuine counterexample to any proposed
subpolynomial bound on \(\mu_{\max}\Delta\), even under global
distinct-source support disjointness, unit signed-area cell multiplicity,
the same metric gap, exact centroid companion sets, and the actual
adaptive quota.

The high-reuse branch must therefore be charged, not eliminated. For one
fixed source pair the exact endpoint charge is

\[
\sum_{q:(p,q)\ {\rm tail}}U_L(r(p))
=\mu(p)U_L(r(p))
\le (k-4)U_L(r(p)).
\tag{0.5}
\]

This is enough at the \(k^2\) scale when \(U_L(r(p))\le m^{o(1)}k\), and
the construction shows that scale is sharp. The unresolved issue is the
aggregate over many high-reuse source pairs, especially when their anchor
matchings and clean starts are reused.

## 1. The anchor capacity theorem

Let

\[
p=(s,t)
\tag{1.1}
\]

be an isolated selected source pair. Write \(E(s)\) and \(E(t)\) for its
two source endpoint edges, and assume

\[
|E(s)\cup E(t)|=4.
\tag{1.2}
\]

For every isolated common translation \(q\in I_p\subseteq Q_p\), let
\((a_q,b_q)\) be its unique directed anchor, so

\[
q=a_q-b_q.
\tag{1.3}
\]

Isolation says that the head \(a_q\) has directed outdegree one and the
tail \(b_q\) has directed indegree one in the full anchor graph of
\(Q_p\). Consequently two isolated edges cannot share their heads, and
they cannot share their tails. However, the head of one may be the tail of
another. Thus the isolated directed edges can form paths and cycles; their
underlying edges need not form a matching.

Cleanliness gives

\[
\{a_q,b_q\}\cap(E(s)\cup E(t))=\varnothing.
\tag{1.4}
\]

The map from an isolated directed edge to its head is therefore an
injection into the \(k-4\) points outside the source endpoints. Hence

\[
\boxed{|I_p|\le k-4.}
\tag{1.5}
\]

This proves (0.2). If the isolated anchors additionally form a literal
underlying matching, then both endpoints can be charged and

\[
\boxed{|I_p|\le
\left\lfloor\frac{k-4}{2}\right\rfloor.}
\tag{1.6}
\]

More generally, if \(v(p)=|E(s)\cup E(t)|\), the same proof gives

\[
|I_p|\le k-v(p),
\tag{1.7}
\]

with the stronger half-bound in the literal underlying-matching subcase.
Equation (1.7) uses the full centroid/common-translation structure, but it
cannot be improved to \(m^{o(1)}\): the next construction has
\(|I_p|=|Q_p|\ge ck\).

## 2. A linearly reused pair

Fix \(J\), choose a prime \(P\) with \(J\le P\le2J\), and use the area
scale

\[
S=5,
\qquad
r=-100S^2.
\tag{2.1}
\]

Construct the scaled perpendicular target pencil with

\[
H=10J+P+12
\tag{2.2}
\]

horizontal points and the four vertical marks

\[
0,\ 10S,\ 24S,\ 26S.
\tag{2.3}
\]

There are exactly two determinant-qualified target records of gap \(r\)
per horizontal point. The final point count below is \(k=2H\), so

\[
U_N(r)=2H=k.
\tag{2.4}
\]

Every normalized target area belongs to \(S^2\mathbf Z=25\mathbf Z\), and
finite avoidance makes all \(k\) target area cells distinct.

Now create two source records using

\[
\begin{aligned}
z_0&=17,&
u_0&=(900S^2-z_0,z_0+1),&
u'_0&=(900S^2-z_0-1,z_0),\\
z_1&=26,&
u_1&=(900S^2-z_1,z_1+1),&
u'_1&=(900S^2-z_1-1,z_1).
\end{aligned}
\tag{2.5}
\]

For \(i=0,1\),

\[
|u_i|^2-|u'_i|^2=1800S^2=-18r,
\tag{2.6}
\]

while

\[
2\det(u_i,u'_i)=-1800S^2+70+36i.
\tag{2.7}
\]

Thus the two source areas are congruent modulo \(36\), and their normalized
source shifts differ by one. Since all normalized target areas are
multiples of \(25\), their two normalized residual supports are disjoint.

Choose \(J\) pairwise-disjoint anchor edges

\[
(a_j,b_j),
\qquad
q_j=a_j-b_j.
\tag{2.8}
\]

For each \(j\), and for each of the four fixed source starts
\(s_0,t_0,s_1,t_1\), add a fresh target edge having pair sum equal to the
source start plus \(q_j\). This forces

\[
H_{q_j}=\{s_0,t_0,s_1,t_1\}
\tag{2.9}
\]

after generic finite avoidance. Both pairs \(p_0=(s_0,t_0)\) and
\(p_1=(s_1,t_1)\) have exactly the anchor matching (2.8) as their common
translations, and every \(q_j\) is isolated.

At a fixed anchor head \(a_j\), the four relevant centroid companion sets
are

\[
\{b_j,\text{the two endpoints of the corresponding target edge}\}.
\tag{2.10}
\]

They form a singleton sunflower with core \(\{b_j\}\). Thus the linear
reuse does not come from weakening the centroid condition.

The planted point count before the filler is

\[
(H+4)+8+10J.
\tag{2.11}
\]

After adjoining the \(P\)-point filler and using (2.2), the total is

\[
k=(H+4)+8+10J+P=2H.
\tag{2.12}
\]

Because \(P\asymp J\), this gives \(J=\Theta(k)\).

## 3. The actual adaptive quota

Use the finite-field parabola filler and finite avoidance exactly as in
ADAPTIVE_MOD36_DISJOINT_UNION_PACKING.md. In addition to distance and
pair-sum uniqueness, require:

1. every planted fibre is exactly the four starts in (2.9);
2. the common anchors of each \(p_i\) are exactly (2.8);
3. the only global source edge-label pairs of gap \(-18r\) are
   \(p_0,p_1\);
4. the only determinant-qualified target records of gap \(r\) are the
   \(k\) prescribed pencil records; and
5. every displayed centroid class contains exactly its two intended
   triples.

All unwanted equalities are nonzero polynomials of degree at most two in
the free centres, target endpoints, filler scale, and relative
translation. The grid nonvanishing lemma gives an integral
distance-Sidon specialization of polynomial height.

Begin with all \(J\) planted translations and add filler translations
until the actual mass first reaches \(4k^2\). Since each fibre contains at
most \(N\) starts,

\[
4k^2\le H_Q<4k^2+N.
\tag{3.1}
\]

Every planted fibre has \(h_{q_j}=4\), and therefore

\[
b_{q_j}
=
\left\lceil\frac{4k^2}{H_Q}\right\rceil
=1.
\tag{3.2}
\]

The two loads in each fibre are tied at \(k\), so exactly one remains in
the residue-refined tail. The total tail mass is independent of all tie
choices:

\[
X_{36}=Jk.
\tag{3.3}
\]

Across \(J\) binary choices, one of the two source pairs is tail at least
\(\lceil J/2\rceil\) times. Since the two distinct-source supports are
disjoint,

\[
\mu_{\max}\Delta\ge \left\lceil\frac{J}{2}\right\rceil
=\Theta(k),
\qquad
\Delta=1.
\tag{3.4}
\]

Equations (3.1), (3.3), and \(J=\Theta(k)\) prove (0.4).

## 4. Exact finite certificate

The verifier uses

\[
J=4,
\qquad
P=47,
\qquad
S=5.
\tag{4.1}
\]

It constructs a 198-point integral distance-Sidon set with

\[
\begin{array}{c|r}
k&198\\
N&19{,}503\\
\text{planted translations}&4\\
h_{q_j}&4\\
\sum_jh_{q_j}&16\\
U_N(-2{,}500)&198\\
\text{filler clean-start mass}&300{,}798\\
H_Q&156{,}955\\
b_{q_j}&1\\
X_{36}&792.
\end{array}
\tag{4.2}
\]

Both source pairs have exactly the same four-edge anchor matching. The
two normalized supports are disjoint. For every one of the sixteen
possible tie orderings, total tail mass remains \(792\) and
\(\mu_{\max}\ge2\); a consistent ordering gives \(\mu_{\max}=4\).

Run:

    PYTHONPATH=phase2/loop/erdos1208 python3 \
      phase2/loop/erdos1208/verify_adaptive_mod36_high_source_reuse_barrier.py

## 5. Consequence

The strategy

\[
\text{globally disjoint supports}
\Longrightarrow
\mu_{\max}\Delta=m^{o(1)}
\tag{5.1}
\]

is false. Distinct-source support depth can be one while a single support
is repeated through linearly many genuine isolated translations.

The remaining high-reuse target is aggregate. A viable statement must
look like

\[
\sum_p\mu(p)U_L(r(p))
\le m^{o(1)}H_Q,
\tag{5.2}
\]

and must exploit either the competition between the common-anchor
matchings and the external target-load graphs, or the fact that many
different high-reuse pairs cannot all receive their adaptive top witnesses
economically. Bounding one \(\mu(p)\), one companion sunflower, or one
repeated residual support cannot close the branch.
