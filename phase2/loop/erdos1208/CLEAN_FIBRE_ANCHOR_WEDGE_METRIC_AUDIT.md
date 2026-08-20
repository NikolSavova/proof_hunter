# Anchor-wedge closure versus the weighted scalar gate

## 1. Outcome

The anchor-wedge closure theorem and its exact exceptional identity are
correct.  They give two durable consequences for the weighted
common-translation dichotomy:

1. the exceptional bijection preserves the source start, hence it has an
   exact weighted form for **every** weight depending on that start; and
2. the replacement-pencil sizes `rho(p)` satisfy the new second-moment
   estimate

\[
 \boxed{
 \sum_p\rho(p)^2
 \le2k\left(k+\left\lfloor{k-3\over2}\right\rfloor-3\right)H.}
                                                               \tag{1.1}
\]

for `k>=6`, with ordered source pairs `p`.

On the rigid branch `c(p)<=sqrt(k)rho(p)`, this gives

\[
 \boxed{
 \sum_{p\ \mathrm{rigid}}c(p)^2
 \le2k^2\left(k+\left\lfloor{k-3\over2}\right\rfloor-3\right)H.}
                                                               \tag{1.2}
\]

This improves the generic clean-codegree fourth moment by a factor of about
`k` on that branch.

It does **not** close the weighted scalar tail.  The exact exceptional mass
controls only fibre pairs whose directed anchors have a common head.  The
mixed charge also has cross-head and disjoint-anchor pieces, and shared-head
closure is false there.  Even on the shared-head piece, inserting the metric
weight loses exactly the factors which prevented the previous endpoint
argument from reaching the dense reciprocal tail.

Thus the closure theorem gives a real structural and moment improvement,
but not the missing aggregate estimate.

## 2. Exact weighted exceptional identity

Use the notation of `SHARED_HEAD_FIBRE_INTERSECTION_SWITCH.md`.  For

\[
 q_1=a-b,\qquad q_2=a-c,                                 \tag{2.1}
\]

let `E(a;b,c)` be the exceptional starts in
`H_(q_1) cap H_(q_2)`.  The existing identity is

\[
 \sum_{a,\{b,c\}}|E(a;b,c)|=H.                           \tag{2.2}
\]

The bijection proving (2.2) preserves the start.  Indeed, if `s` is
exceptional and the retained target endpoint is `e`, then

\[
 E(s+q_1)=\{c,e\},\qquad E(s+q_2)=\{b,e\}.               \tag{2.3}
\]

Writing `S=E(s)`, clean membership gives

\[
 a+\sum S=b+c+e.                                         \tag{2.4}
\]

Consequently `s in H_(a-e)`, with target edge `{b,c}`.  Conversely, every
membership `s in H_(a-e)` reconstructs the unique exceptional wedge by
taking `{b,c}` to be its target edge.  The same `s` occurs on both sides.

Therefore, for every function `F:Sigma -> R`, not merely `F=1`,

\[
 \boxed{
 \sum_{a,\{b,c\}}\ \sum_{s\in E(a;b,c)}F(s)
 =\sum_q\sum_{s\in H_q}F(s).}                            \tag{2.5}
\]

This is the strongest direct metric-compatible form of the exceptional
identity.

## 3. Intersection with the mixed two-fibre charge

For an unordered pair `{q,q'}`, recall

\[
 \mathcal I_{q,q'}=H_q\cap H_{q'},\qquad
 \mathcal G_{q,q'}=
 \{s\in\mathcal I_{q,q'}:
 E(s+q)\cap E(s+q')\ne\varnothing\}.                    \tag{3.1}
\]

If `q=a-b` and `q'=a-c` have a common head, the closure theorem says
exactly

\[
 \mathcal G_{q,q'}=E(a;b,c).                             \tag{3.2}
\]

Its nonexceptional injection gives

\[
 |\mathcal I_{q,q'}\setminus\mathcal G_{q,q'}|
 \le h_{c-b}.                                            \tag{3.3}
\]

In particular,

\[
\boxed{
 \sum_{\substack{q<q'\\\text{common head}}}
 |\mathcal G_{q,q'}|=H,
 \qquad
 2\sum_{\substack{q<q'\\\text{common head}}}
 |\mathcal G_{q,q'}|
 |\mathcal I_{q,q'}\setminus\mathcal G_{q,q'}|
 \le2NH.}                                                \tag{3.4}
\]

If `q,q'` have a common tail, their good set is empty.  A meeting pair of
targets would necessarily contain the two anchor heads, contradicting the
two clean conditions.

Now let `V(s,t)>=0` be any ordered source-pair weight and put

\[
 M_V(s)=\sum_{t\ne s}\bigl(V(s,t)+V(t,s)\bigr).          \tag{3.5}
\]

The shared-head part of the mixed weighted mass is

\[
 D_{\rm head}(V)=
 \sum_{\substack{q<q'\\\text{common head}}}
 \sum_{\substack{s\in\mathcal G_{q,q'}\\
                  t\in\mathcal I_{q,q'}\setminus
                        \mathcal G_{q,q'}}}
 \bigl(V(s,t)+V(t,s)\bigr).                              \tag{3.6}
\]

Equations (2.5) and (3.3) give the two rigorous bounds

\[
\boxed{
 D_{\rm head}(V)
 \le\sum_q\sum_{s\in H_q}M_V(s)}                        \tag{3.7}
\]

and

\[
\boxed{
 D_{\rm head}(V)
 \le2\|V\|_\infty
 \sum_{a,\{b,c\}}|E(a;b,c)|h_{c-b}
 \le2N H\|V\|_\infty.}                                \tag{3.8}
\]

Both retain the exact metric weight as far as the closure bijection allows.

## 4. New replacement-pencil second moment

For an ordered source pair `p=(s,s')`, let `R_p` be the set of translations
`q` for which `s,s' in H_q` and their two clean target edges meet.  Thus

\[
 \rho(p)=|R_p|.                                          \tag{4.1}
\]

Regard `R_p` as directed anchor edges on `A`, and let `d_p^+(a)` be its
outdegree at `a`.  Put

\[
 X(p)=\sum_a{d_p^+(a)\choose2}.                          \tag{4.2}
\]

Switching over common-head anchor pairs gives the exact identity

\[
\boxed{
 \sum_pX(p)
 =\sum_{a,\{b,c\}}e(a;b,c)(e(a;b,c)-1).}                 \tag{4.3}
\]

The right side counts ordered pairs of exceptional starts, exactly the
ordered source pairs whose two translations are both in their replacement
pencil.  Put

\[
 r_0=\left\lfloor{k-3\over2}\right\rfloor.              \tag{4.4}
\]

The exceptional matching theorem gives `e(a;b,c)<=r_0`, while `sum e=H`.
Therefore

\[
 \sum_pX(p)\le(r_0-1)H.                                 \tag{4.5}
\]

Cauchy--Schwarz on the `k` possible heads gives

\[
 X(p)\ge{\rho(p)^2\over2k}-{\rho(p)\over2}.             \tag{4.6}
\]

The first-moment replacement bound from the common-translation dichotomy is

\[
 \sum_p\rho(p)\le2(k-2)H.                               \tag{4.7}
\]

Combining (4.5)--(4.7) proves (1.1):

\[
\begin{aligned}
 \sum_p\rho(p)^2
 &\le2k\sum_pX(p)+k\sum_p\rho(p)\\
 &\le2k(r_0-1)H+2k(k-2)H\\
 &=2k(k+r_0-3)H.
\end{aligned}                                             \tag{4.8}
\]

On the rigid branch `rho(p)>=c(p)/sqrt(k)`, (1.2) follows.  A useful dyadic
corollary is

\[
 \boxed{
 \sum_{\substack{p\ \mathrm{rigid}\\c(p)\ge K}}c(p)
 \le {2k^2(k+r_0-3)H\over K}.}                          \tag{4.9}
\]

## 5. Scalar-weighted exponent audit

Take

\[
 V(s,t)=W_{r(s,t),L},\qquad
 r(s,t)=-{\delta(s)-\delta(t)\over18},                   \tag{5.1}
\]

with zero weight when the quotient or target gap is invalid.  For fixed
`s`, distinct `t` give distinct `r` because all source distances are
distinct.  The global target-wedge identity and the per-gap endpoint-degree
bound therefore give

\[
 M_V(s)\le2\sum_{r\ne0}W_{r,L}<Nk^3,
 \qquad
 \|V\|_\infty\le(k-2)N.                                 \tag{5.2}
\]

Thus (3.7)--(3.8) yield only

\[
 D_{\rm head}(V)
 \ll NHk^3\asymp N^2kH.                                 \tag{5.3}
\]

This is the same exponent as the previous crude endpoint charge.

The failure is particularly transparent on joint dyadic cells.  Suppose
`K<=c(p)<2K`, `K>=k`, and the target gap has
`T<=U_L(r)<2T`, `T>=k`.  Then

\[
 {T^2\over k}\le W_{r,L}\le2(k-2)T.                    \tag{5.4}
\]

The nonrigid dichotomy charges `c(p)` by `(k/K)O(p)`.  From (3.4), the
shared-head portion of this charge is at most

\[
 {2NkH\over K}.                                          \tag{5.5}
\]

Passing through the metric weight instead gives a reciprocal-looking but
weaker estimate

\[
 \ll {NHk^3\over KT}.                                    \tag{5.6}
\]

Indeed, throughout the possible range `T<=N asymp k^2`, (5.6) is no better
than (5.5).  In the dense regime `H>>k^3`, the desired bound is `NH/T`.
Equation (5.5) reaches it only when `T<<K/k`; equation (5.6) would require
`K>>k^3`, impossible since `c(p)<=k(k-1)`.  The rigid estimate (4.9) has
the same threshold `T<<K/k` after comparison with the desired dense tail.

Therefore the exact exceptional identity does not repair the reciprocal
tail exponent.  A proof still needs a metric antialignment beyond the fact
that there are exactly `H` exceptions.

## 6. Why the closure cannot be applied to the whole mixed mass

For non-common-head anchor pairs, a good target wedge still makes
`q-q'` a realized point difference, but the original clean conditions do
not exclude the two "wrong-side" anchor collisions needed to put every bad
start into `H_(q-q')`.

There is an exact scalar-weighted Costas witness.  In the 22-point stress,

\[
\begin{aligned}
 q&=(-20,-27),&\quad q'&=(24,37),&\quad g&=(-44,-64),\\
 s_{\rm good}&=(-167,-153),&&
 s_{\rm bad}=(-182,-156).
\end{aligned}                                             \tag{6.1}
\]

The anchors of `q` and `q'` are disjoint.  Both starts lie in
`H_q cap H_(q')`.  The two targets of `s_good` meet, while those of `s_bad`
do not; nevertheless

\[
 s_{\rm bad}+q'\notin H_g.                               \tag{6.2}
\]

The scalar endpoint-wedge weights are nonzero in both orientations:

\[
 V(s_{\rm good},s_{\rm bad})=3,qquad
 V(s_{\rm bad},s_{\rm good})=4.                          \tag{6.3}
\]

So this is a barrier inside the actual metric mixed mass, not merely an
unweighted abstract configuration.

The aggregate stresses show the scope problem quantitatively.  On
Costas-22,

\[
\begin{array}{c|r|r}
 &\text{shared head}&\text{all anchor geometries}\\ \hline
 \sum A&9342&47370\\
 2\sum A(J-A)&36910&177154\\
 \text{scalar-weighted mixed mass}&7715&35482.
\end{array}                                               \tag{6.4}
\]

Thus shared-head closure sees only about 22 percent of the actual weighted
mixed mass in this genuine stress.  There are 5652 nonhead failed images of
the form (6.2), carrying scalar-weighted mass 4405.

Even within the shared-head sector, the complementary-fibre weight need not
stay near its unweighted total.  The exact quantity

\[
 \sum_{a,\{b,c\}}e(a;b,c)h_{c-b}                         \tag{6.5}
\]

equals `19181793` on the full 43-point transformed parabola, while
`H=190278`; its ratio is about `100.81`.  The identity `sum e=H` alone
therefore supplies no metric or fibre-size antialignment.

## 7. Verification

`verify_clean_fibre_anchor_wedge_metric_audit.py` checks:

* the start-preserving weighted exceptional identity (2.5), using the full
  scalar row mass as `F`;
* the common-head and common-tail classifications;
* the exact switched identity (4.3) and bounds (1.1)--(1.2);
* the geometry split and actual scalar mixed weights on closure, Costas,
  parabola, and ruler stresses;
* the explicit weighted nonhead witness (6.1)--(6.3); and
* the full parabola complementary mass in (6.5).

No issue was found in the statement, proof, or verifier of
`SHARED_HEAD_FIBRE_INTERSECTION_SWITCH.md`.
