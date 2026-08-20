# Synchronized clique quartic gate: dyadic reversibility and the graph-only barrier

## 1. Outcome

The fixed-metric-wedge localization can be sharpened on every dyadic
source-codegree band, but the sharpening reveals a structural no-go.  Let

\[
 K\le c(p)<2K,\qquad K\ge k,                              \tag{1.1}
\]

and let \(R(p)\) be the number of one-role bases for \(p\) which are
transverse-rich, meaning \(T_p(b)\ge c(p)/2\).  For a fixed physical metric
wedge \(w\), put

\[
 \mathcal R_K(w)=
 \sum_{\substack{p:\ K\le c(p)<2K}}R(p)V_w(p),           \tag{1.2}
\]

where \(V_w(p)\) is the exact zero-one scalar/determinant selector from the
fixed-wedge localization.  If \(\Phi_{2,L,K}(w)\) is the contribution of
this band to the synchronized pair mass, then

\[
\boxed{
 {K^2\over16}\mathcal R_K(w)
 \le \Phi_{2,L,K}(w)
 <2K^2\mathcal R_K(w).}                                 \tag{1.3}
\]

Thus the local quartic target is quantitatively equivalent to

\[
 \boxed{
 \mathcal R_K(w)\le
 m^{o(1)}{k^4\over K^2}.}                               \tag{1.4}
\]

At the literal threshold \(K=k\), this is the fixed-wedge
transverse-rich one-role-base bound \(m^{o(1)}k^2\).

Equation (1.3) is a positive exact reduction, but also a reversibility
barrier: binomial pooling supplies two powers of \(K\), and removing those
pool choices costs exactly the same two powers.  Hence no proof can
amplify to pairs of third translations and then forget their endpoint
data; that returns to (1.4), the localized form of the original weighted
one-role gate.

Anchor isolation does not repair this at the indexed-graph level.  There
is an explicit family on \(k=M+3\) endpoint labels with

\[
 c=3M\asymp3k,\qquad
 R=\Theta(k^2),\qquad
 T(b)\ge c/2,\qquad
 B_2=\Theta(k^4),                                       \tag{1.5}
\]

in which a \(1-O(1/k)\) fraction of the rich bases have disjoint anchor
edges.  The three indexed edge maps (anchor, good target, bad target) are
all simple and injective.  This is **not** claimed to be a realizable
integral distance-Sidon construction, because it does not impose the
clean-row affine equations.  It rigorously kills any quartic proof using
only anchor/target degree counts or adaptive quotas after those equations
have been discarded.

Gaussian determinant cells give a second exact reduction but no saving at
the threshold.  In a fixed source cell \((r,d)\) and band (1.1),

\[
 \boxed{
 K_{2,K}(r,d)\le 8G(m)kK^3,\qquad G(m)=m^{o(1)},}        \tag{1.6}
\]

so at \(K=k\) even one cell is allowed \(m^{o(1)}k^4\).
The missing theorem must therefore couple either the retained pool
endpoints or multiple determinant cells to the clean affine equations.

## 2. Proof of dyadic reversibility

For an ordered source pair \(p\), recall

\[
 B_2(p)=
 \sum_{\substack{b\ \operatorname{one-role}\\T_p(b)\ge c(p)/2}}
 {T_p(b)\choose2}.                                      \tag{2.1}
\]

If \(c=c(p)\ge4\), then every retained base has

\[
 {T_p(b)\choose2}
 \ge {\lceil c/2\rceil\choose2}
 \ge {c^2\over16},                                      \tag{2.2}
\]

while trivially

\[
 {T_p(b)\choose2}\le {c\choose2}<{c^2\over2}.           \tag{2.3}
\]

Summing over the \(R(p)\) rich bases gives

\[
 {c(p)^2\over16}R(p)
 \le B_2(p)<{c(p)^2\over2}R(p).                         \tag{2.4}
\]

On (1.1), this implies

\[
 {K^2\over16}R(p)
 \le B_2(p)<2K^2R(p).                                   \tag{2.5}
\]

The fixed physical wedge selects an ordered source pair at most once for
its scalar shift, by distinct-distance Sidonicity.  Therefore

\[
 \Phi_{2,L,K}(w)
 =\sum_{\substack{p:\ K\le c(p)<2K}}B_2(p)V_w(p).       \tag{2.6}
\]

Multiplying (2.5) by \(V_w(p)\) and summing proves (1.3).
This proof retains the scalar sign, determinant cutoff, ordered source
pair, and the full definition of transverse-richness.

There is a useful exact switch for the base mass.  If
\(\mathcal G_{q,q'}\) and \(\mathcal I_{q,q'}\) are the good-start pencil
and common clean-fibre intersection from the one-role switch, then

\[
\begin{aligned}
 \mathcal R_K(w)
 =\sum_{q<q'}\!
 \sum_{\substack{s\in\mathcal G_{q,q'}\\
                  t\in\mathcal I_{q,q'}\setminus
                       \mathcal G_{q,q'}}}
 &\bigl(V_w(s,t)\Xi_K(s,t;q,q')\\
 &+V_w(t,s)\Xi_K(t,s;q,q')\bigr),                       \tag{2.7}
\end{aligned}
\]

where \(\Xi_K\) is the indicator that \(K\le c(s,t)<2K\) and the
displayed one-role base has at least \(c(s,t)/2\) fully transverse
extensions.  Equation (2.7) is a restriction of the exact target-star
switch, not an unweighted relaxation.

It follows that a proof of (1.4) can still use the retained pool endpoints
through \(\Xi_K\).  Dropping \(\Xi_K\), or replacing it by one, returns to
the previous fixed-wedge weighted one-role correlation and gains nothing
from the higher pooling.

## 3. Determinant-cell consequence

Let the two canonically oriented source edges of \(p\) have displacement
vectors \(u,u'\), and define the signed doubled source area

\[
 d(p)=2\det(u,u').                                      \tag{3.1}
\]

For fixed scalar \(r\) and fixed \(d\), the Gaussian factorization

\[
 (u-u')\overline{(u+u')}=-18r-id                       \tag{3.2}
\]

shows that the number of ordered source pairs in this cell is at most

\[
 G(m)=4\max_{z\ne0}\tau(|z|^2)^2=m^{o(1)}.              \tag{3.3}
\]

This counts source pairs, not their synchronized-clique weights.  The
elementary endpoint-wedge bound gives

\[
 R(p)\le O(p)\le2(k-2)c(p).                             \tag{3.4}
\]

Combining (2.3), (3.4), and \(c(p)<2K\) gives

\[
 B_2(p)<(k-2)c(p)^3<8kK^3.                              \tag{3.5}
\]

Summing (3.5) over the at most \(G(m)\) source pairs in (3.2) proves
(1.6).  At \(K=k\), (1.6) has exactly quartic size.  Consequently
Gaussian factorization is useful only if the subsequent argument controls
the number or weighted arrangement of occupied cells; summing its
pointwise bound over signed areas is not a proof.

## 4. A literal indexed-graph quartic extremizer

Take an integer \(M\ge128\) and use

\[
 k=M+3,\qquad c=3M.                                     \tag{4.1}
\]

The endpoint labels are three centres \(0,1,2\) and \(M\) leaves
\(\ell_j\), with indices modulo \(M\).  The common translations are
indexed by

\[
 q=(i,j),\qquad i\in\{0,1,2\},\quad j\in\mathbb Z/M.    \tag{4.2}
\]

Define three injective edge maps on this common index set.  The good target
graph is the union of three stars:

\[
 G(i,j)=\{i,\ell_j\}.                                   \tag{4.3}
\]

The bad target graph is a union of three sparse circulants:

\[
 H(i,j)=\{\ell_j,\ell_{j+i+1}\}.                        \tag{4.4}
\]

Finally use the directed anchor

\[
 A(i,j)=(\ell_j,\ell_{j+i+4}).                          \tag{4.5}
\]

For \(M>12\), all three maps are injective.  Choose a base
\(\{(i,j),(i,j')\}\) in one good star whose two bad edges are disjoint.
It is one-role.  There are exactly

\[
 R=3\left({M\choose2}-M\right)                          \tag{4.6}
\]

such bases: in each bad circulant, exactly \(M\) unordered edge pairs
meet.

A candidate transverse translation must come from one of the other two
good stars and avoid the two base leaves.  This leaves \(2(M-2)\)
candidates.  The union of two base bad edges contains at most four leaves;
each leaf lies in at most six bad edges.  The union of two base anchors
also contains at most four leaves; each leaf lies in at most six directed
anchors when head and tail contacts are both counted.  Hence

\[
 T(b)\ge2(M-2)-24-24=2M-52.                             \tag{4.7}
\]

For \(M\ge104\),

\[
 2M-52\ge{3M\over2}={c\over2}.                         \tag{4.8}
\]

Thus every base in (4.6) is transverse-rich and

\[
 B_2\ge
 3\left({M\choose2}-M\right){2M-52\choose2}
 =\Theta(M^4)=\Theta(k^4).                              \tag{4.9}
\]

Only \(O(M)\) bases have two anchors which meet, because the anchor graph
in each colour has constant degree.  Hence
\(R-O(M)=\Theta(M^2)\) bases are anchor-disjoint.
Shared-head/shared-tail charging sees only a vanishing fraction of the
rich-base population.

The same example blocks an unbalanced translation quota.  Each translation
is transverse to \(\Theta(M^2)\) ordered choices of a rich base and a
second pool translation, so its pool-incidence load is \(\Theta(M^3)\),
while the total synchronized-pair mass is \(\Theta(M^4)\).  A quota whose
total is \(o(k^4)\) cannot absorb this model.

Again, (4.3)--(4.5) are an **indexed endpoint countermodel**, not a
geometric counterexample to #1208.  Its role is precise: after the affine
clean-row equations and scalar norm equations are removed, all remaining
degree, isolation, transversality, and quota data permit quartic mass.

## 5. Consequence for the live proof

The new exact local target may be written in either of two equivalent
forms:

\[
\begin{aligned}
 \Phi_{2,L,K}(w)&\le m^{o(1)}k^4,\\
 \mathcal R_K(w)&\le m^{o(1)}k^4/K^2.
\end{aligned}                                           \tag{5.1}
\]

The second form is smaller and should be the next attack surface, but only
if the extension indicator \(\Xi_K\) in (2.7) is retained.  The indexed
extremizer shows that anchor isolation or an adaptive quota on its own
cannot prove it.  The determinant-cell estimate (1.6) shows that a
fixed-cell divisor bound also stops exactly at the quartic threshold.

Therefore the genuinely new ingredient must couple at least one of:

1. the affine clean-row identities of a selected pool translation;
2. the scalar/determinant data of the fixed physical wedge; and
3. the rigid good-start pencil in the base switch.

Using only their separate marginal bounds reproduces (1.3), (1.6), or the
graph extremizer.

## 6. Verification

Run

    python phase2/loop/erdos1208/verify_synchronized_clique_dyadic_reversibility_barrier.py

The verifier exhausts the finite binomial inequalities behind (1.3),
constructs (4.3)--(4.5), checks injectivity and every one-role/transverse
condition exactly, reproduces (4.6), verifies (4.7) base by base, measures
the anchor-disjoint fraction and per-translation quota loads, and checks
the finite algebra behind (1.6).
