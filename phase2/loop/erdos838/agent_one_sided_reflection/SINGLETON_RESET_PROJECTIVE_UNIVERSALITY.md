# Singleton reset chains are projectively universal

## Verdict

The proposed cross-level discarded-layer theorem is false already for
singleton layers, in the strongest possible sense. A strict codimension-one
reset chain with the full-pocket containment

\[
 Q_{t-1}\subset\operatorname{int}\operatorname{conv}\{u,v,z_t\} \tag{1}
\]

can have an arbitrary prescribed rational planar order type on its discarded
tips \(z_0,\ldots,z_{L-1}\). The fixed-edge tangent-coordinate map is one
projective collineation, and (1) is exactly a two-coordinate dominance
relation. Hence the detached discarded-tip face complex can be no better
than the original unrestricted problem.

The chronology is also exact. A detached face whose largest tip index is
\(m\) is offered by exactly \(L-m\) prefix states, so face-only recovery has
worst load \(L\). Strict tangent progress does give one positive theorem:
for a fixed root edge, the left and right compatibility margins are
monotone under any interleaving of upper and lower pocket resets. A guard
can change only from failure to success and can never fail again; alternating
left/right failures along one fixed-root chain are impossible. This
monotonicity does not create faces because one guard may remain failed for
all \(L\) universal levels.

Thus the missing cross-level bank isolated in
TANGENT_RESET_CHAIN_BARRIER.md is coefficient-equivalent to Erdős 838
itself. Any successful global use must correlate many reset chains, exploit
the terminal/source law, or obtain a chronology-weighted improvement; no
standalone discarded-layer theorem can give a stronger coefficient.

Exact verifier:

    python3 phase2/loop/erdos838/agent_one_sided_reflection/verify_singleton_reset_universality.py

## 1. Tangent coordinates are projective

Normalize

\[
                         u=(0,0),\qquad v=(1,0).          \tag{2}
\]

For a point \(z=(x,-h)\), \(h>0\), below the root line, put

\[
 A(z)={x\over h},\qquad B(z)={x-1\over h}.              \tag{3}
\]

Then \(A-B=1/h>0\), and the inverse is

\[
 z(A,B)=\left({A\over A-B},-{1\over A-B}\right).        \tag{4}
\]

In homogeneous coordinates, (3) is induced by the invertible linear map

\[
 (x,y,1)\longmapsto (x,x-1,-y).                         \tag{5}
\]

All denominators \(-y\) are positive on the lower halfplane. Therefore this
single projective map preserves the oriented matroid up to one global sign,
and in particular preserves exactly which subsets are in convex position.

The stronger full-pocket condition has a particularly simple form:

> **Lemma 1 (dominance equals triangle containment).**
> For two lower points \(z_i,z_j\),
> \[
> z_i\in\operatorname{int}\operatorname{conv}\{u,v,z_j\}
> \quad\Longleftrightarrow\quad
> A_i>A_j,\quad B_i<B_j.                                \tag{6}
> \]

**Proof.** The line \(uz_j\) has endpoint coordinate \(A_j\), while
\(vz_j\) has endpoint coordinate \(B_j\). The open triangle below \(uv\)
is the intersection of the two strict inward halfplanes, which are exactly
the inequalities in (6). Equivalently, substituting (4) gives positive
barycentric coordinates. QED.

## 2. Universality construction

Let \(P=\{p_0,\ldots,p_{L-1}\}\) be any rational general-position point set,
indexed by increasing first coordinate \(x_i\). Choose a rational \(M\)
large enough that

\[
                         y_i+Mx_i
\]

is strictly increasing. Apply the invertible affine map

\[
 p_i\longmapsto
 (A_i,B_i)=(C-x_i,\ y_i+Mx_i),                           \tag{7}
\]

where \(C\) is then chosen so large that \(A_i>B_i\) for every \(i\).
This affine image has the same convex-subset complex as \(P\), while

\[
 A_0>A_1>\cdots>A_{L-1},\qquad
 B_0<B_1<\cdots<B_{L-1}.                                \tag{8}
\]

Apply the inverse projective map (4), obtaining lower points \(z_i\).
Equations (6) and (8) give

\[
 \{z_0,\ldots,z_{t-1}\}
 \subset\operatorname{int}\operatorname{conv}\{u,v,z_t\}
 \quad(1\le t<L).                                       \tag{9}
\]

A final affine shear parallel to \(uv\) moves every \(z_i\) to the left of
\(u\), fixes both roots, and preserves all containments and convexity.
Thus the points form a legitimate one-side x-ordered trace cloud.

> **Theorem 2 (projective universality of singleton resets).**
> The discarded-tip configuration \(Z=\{z_0,\ldots,z_{L-1}\}\) has exactly
> the same convex-subset complex as the arbitrary input \(P\), while its
> prefixes form the strict full-pocket reset chain (9).

This directly corrects the special cap wrapper from the preceding report:
that explicit wrapper had \(2^L\) detached faces, but Booleanity is not a
consequence of singleton nesting.

## 3. Exact rooted profile and zero coexistence

Put \(Q_t=\{z_0,\ldots,z_t\}\). Since every earlier tip is interior to
the triangle \(uvz_t\), the rooted-side polynomial is

\[
 \boxed{
 \sum_{\substack{S\subseteq Z\\S\cup\{u,v\}\ {\rm convex}}}
       s^{|S|}
       =1+Ls.}                                          \tag{10}
\]

At level \(t\), the visible hull \(\{z_t\}\) has full pocket \(Q_{t-1}\).
It is a deepest codimension-one reset. For every nonempty
\(S\subseteq Q_{t-1}\),

\[
 S\cup\{u,v,z_t\}\quad\hbox{is not convex}.              \tag{11}
\]

Thus strict rank progress, the Kraft identity, and even the strongest
possible pocket containment coexist with arbitrary detached face complexity
and zero parent-child product.

Singleton layers are a subcase of every bounded-rank-layer statement.
Consequently no theorem for layers of rank at most a fixed \(h\) can escape
this counterexample. If exact rank \(h>1\) is required, each \(z_t\) may be
replaced by a sufficiently small \(h\)-vertex rooted cap; the containments
are open and one representative from every cap still induces the arbitrary
order type \(P\).

## 4. Exact chronology multiplicity

Let \({\cal F}(Z)\) be the ordinary convex-subset complex of the discarded
tips. For nonempty \(S\in{\cal F}(Z)\), write

\[
                         m(S)=\max\{i:z_i\in S\}.         \tag{12}
\]

The prefix state \(Q_t\) contains \(S\) exactly when \(t\ge m(S)\). Hence

\[
 \boxed{
 \operatorname{mult}(S)=L-m(S),\qquad
 \sum_{t=0}^{L-1}V(Q_t)
 =L+\sum_{\varnothing\ne S\in{\cal F}(Z)}(L-m(S)).}      \tag{13}
\]

The empty face contributes \(L\). The worst nonempty load is exactly \(L\),
attained by the singleton \(\{z_0\}\). Therefore a face-only decoder cannot
recover the reset depth with sublinear worst-case ambiguity. A depth or
largest-tip tag is necessary.

In the special Boolean cap wrapper, the nonempty incidence sum is
\(2^{L+1}-L-2\), and including the empty face gives \(2^{L+1}-2\), so the
average history load is below two. Universality shows that this favorable
average is not an invariant of reset geometry; formula (13), rather than a
Boolean estimate, is the exact general chronology bank.

## 5. Fixed-root guard failures cannot alternate

For an upper rooted hull use coordinates
\(\alpha,\beta\), and for a lower rooted hull use \(A,B\), as in the
two-tangent report. Define the guard margins

\[
                         g_L=A-\alpha,\qquad
                         g_R=\beta-B.                    \tag{14}
\]

Compatibility is \(g_L>0\) and \(g_R>0\). An upper pocket reset makes

\[
                         \alpha\downarrow,\qquad\beta\uparrow,
\]

while a lower reset makes

\[
                         A\uparrow,\qquad B\downarrow.   \tag{15}
\]

All inequalities are strict in general position. Therefore:

> **Theorem 3 (monotone guard phases).** Under any interleaving of upper and
> lower pocket resets with the same roots, both \(g_L\) and \(g_R\) increase
> monotonically, strictly whenever either relevant side resets. Each guard
> can cross zero at most once, from failure to success. The set of failed
> guards is nested in time; left/right failure cannot alternate.

This removes guard oscillation as the source of linear depth. The
universality chain shows the real obstruction: one margin may make \(L\)
strict rank steps while remaining negative, and the detached tips seen
during those steps can encode an arbitrary order type.

## 6. Sharp scalable regression

Choose \(P\) to be a balanced central Pascal cell. The construction above
turns it into a singleton full-pocket reset chain without changing a single
convex subset. Hence the discarded-layer bank has the known sharp
coefficient-half Pascal profile, not a fixed-power surplus over it. Choosing
any other stretchable family transfers its exact face complex in the same
way.

The verifier performs this transfer for exact rational Pascal, random, and
alternating inputs. It checks all triple signs up to one global reversal,
all convex subsets, every full-pocket containment, the rooted polynomial
\(1+Ls\), zero parent-child coexistence, chronology identity (13), and
monotone guard phases.
