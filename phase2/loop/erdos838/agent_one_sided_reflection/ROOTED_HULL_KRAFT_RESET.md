# Rooted-hull Kraft reset for two-tangent trace profiles

## Verdict

There is an exact local reset behind the remaining tangent-profile
inequality. For one side cloud of a trace, partition every label subset by
the vertices visible from the two roots. If \(H\) is that rooted visible
hull and \(I(H)\) is its hidden pocket, then

\[
 (1+z)^m=\sum_H z^{|H|}(1+z)^{|I(H)|}.                 \tag{1}
\]

This is both a weighted Kraft equality and an exact entropy/KL identity. It
proves a sharp dichotomy: either the rooted-side face polynomial is large,
or one convex rooted hull hides all but logarithmically many labels of the
side cloud. Rooted-side faces have global trace load one, and choosing one
hidden pocket per trace state gives ordinary-face load at most \(O(n^2)\).
Thus both the spend and the reset can be summed globally with only
polynomial loss.

Applied to the two-tangent contraction, fix thresholds \(L,K\). Each active
orientation state has one of:

1. genuine rank-above-four compatible mass at least \(L\), paid with rank
   load by the preceding report;
2. at least \(K\) half-weighted left or right rooted histories, paid
   globally with load one; or
3. a hidden pocket on each side retaining all but \(\log_{3/2}K\) labels.

Taking \(L\) and \(K\) of order \(d^{1+\epsilon}\), where \(d\) is the
singleton mixed-extension degree, makes either of the first two branches a
fixed-power gain over rank-four mass. The only unspent state localizes to
two pockets of codimension \(O((1+\epsilon)\log d)\).

This does not yet close the coefficient-half bound. The remaining issue is
coexistence through a sequence of deep pockets: a face of the child pocket
need not coexist with its rooted hull. The perfect-matching star realizes
exactly this obstruction, while central Pascal cells exhibit the expected
balanced visible/reset behavior. No closure claim is made.

Exact verifier:

    python3 phase2/loop/erdos838/agent_one_sided_reflection/verify_rooted_hull_kraft_reset.py

## 1. Relative rooted hulls

Fix distinct roots \(u,v\) and a finite set \(Q\) of \(m\) points lying
strictly in one open halfplane of the line \(uv\). General position is
assumed. For \(A\subseteq Q\), let

\[
 h(A)=\operatorname{vert}\operatorname{conv}(A\cup\{u,v\})
                                      \setminus\{u,v\}.  \tag{2}
\]

The roots are vertices and \(uv\) is a hull edge. Hence
\(h(A)\cup\{u,v\}\) is convex. Let \(\mathcal R\) be the family of all such
rooted visible sets. For \(H\in\mathcal R\), define its open hidden pocket

\[
 I(H)=Q\cap\operatorname{int}
               \operatorname{conv}(H\cup\{u,v\}).        \tag{3}
\]

> **Theorem 1 (rooted-hull fibre partition).** For every
> \(H\in\mathcal R\),
> \[
> h^{-1}(H)=\{H\cup Z:Z\subseteq I(H)\}.                 \tag{4}
> \]
> Consequently, coefficientwise in \(z\),
> \[
> \boxed{(1+z)^m
>   =\sum_{H\in\mathcal R}z^{|H|}(1+z)^{|I(H)|}.}        \tag{5}
> \]

**Proof.** If \(h(A)=H\), every point of \(A-H\) is a nonvertex of the
strictly convex polygon with vertex set \(H\cup\{u,v\}\). General position
puts it strictly inside that polygon, so \(A=H\cup Z\) with
\(Z\subseteq I(H)\). Conversely, adding any subset of strictly interior
points changes no hull vertex. This proves (4). Summing \(z^{|A|}\) over
its disjoint fibres gives (5). QED.

The empty visible set is allowed and is the hull of the empty subset.

## 2. Exact KL form

Put

\[
 R_Q(z)=\sum_{H\in\mathcal R}z^{|H|},\qquad
 c(H)=m-|I(H)|.                                         \tag{6}
\]

There are two natural laws on rooted hulls:

\[
 \pi_z(H)={z^{|H|}(1+z)^{|I(H)|}\over(1+z)^m},\qquad
 \rho_z(H)={z^{|H|}\over R_Q(z)}.                        \tag{7}
\]

The first is the hull induced by a Bernoulli-\(z/(1+z)\) subset of \(Q\);
the second is the ordinary rooted-face Gibbs law. Direct cancellation gives,
in bits,

\[
\boxed{
 \log_2R_Q(z)
 =\log_2(1+z)\,\mathbb E_{\pi_z}c(H)
   +D_2(\pi_z\Vert\rho_z).}                              \tag{8}
\]

Thus visible rooted mass pays for the mean number of labels outside the
selected child pocket, with a nonnegative KL surplus. This is an identity.

## 3. The shallow/deep reset

Let \(i_*=\max_H|I(H)|\) and \(\delta=m-i_*\). From (5),

\[
 (1+z)^m\le (1+z)^{i_*}R_Q(z),
\]

so

\[
 \boxed{R_Q(z)\ge(1+z)^\delta.}                          \tag{9}
\]

Equivalently, for every \(K>1\), either

\[
 R_Q(z)\ge K,                                            \tag{10}
\]

or there is a canonically tie-broken maximally deep rooted hull \(H_*\)
with

\[
 |I(H_*)|>m-\log_{1+z}K.                                \tag{11}
\]

At half weight \(z=1/2\), the reset loses at most

\[
 \log_{3/2}K={\log_2K\over\log_2(3/2)}.                 \tag{12}
\]

For \(K=d^{1+\epsilon}\), this is
\((1+\epsilon)\log_2(d)/\log_2(3/2)\). Thus the matching-star state, which
can have only singleton compatible pairs, cannot disappear into an
unspecified side cloud: on each unpaid side almost the entire cloud lies in
one explicitly recoverable convex pocket.

## 4. Compatible parents expose a complete hidden grid

The reset retains exactly the tangent datum needed at its first divergence.
Let \(H\) and \(K\) be nonempty rooted visible hulls on opposite sides of
\(uv\).

> **Theorem 2 (hidden-pocket grid).** If
> \[
> H\cup K\cup\{u,v\}\quad\hbox{is convex},               \tag{13}
> \]
> then every pair \(x\in I(H),y\in I(K)\) is singleton-compatible:
> \[
> \{x,u,v,y\}\quad\hbox{is a mixed convex quadrilateral}.\tag{14}
> \]
> In particular, if the singleton compatibility graph has \(d\) edges,
> \[
>                         |I(H)|\,|I(K)|\le d.            \tag{15}
> \]

**Proof.** The two rooted polygons lie in opposite halfplanes and their
compatible union is a strictly convex polygon \(C\). Both hidden pockets
are contained in \(C\). For \(x,y\) on opposite sides, the segment \(xy\)
lies in \(C\) and crosses the line \(uv\). Strict convexity implies
\(C\cap\operatorname{line}(uv)=[u,v]\): a continuation past either root
would make that root non-extreme. Hence \(xy\) crosses the open segment
\(uv\), which is precisely (14). QED.

This makes the double reset quantitative. If the two side-cloud sizes are
\(a,b\), (11) chooses pockets of sizes greater than \(a-s,b-s\), where
\(s=\log_{1+z}K\). If

\[
                         (a-s)(b-s)>d,                   \tag{16}
\]

their two selected visible hulls cannot glue. The two-tangent amalgamation
theorem then identifies a specific failed left or right tangent guard. That
failed guard, together with the two pockets, is an exact first-divergence
child state.

For the perfect-matching regression \(a=b=m,d=m\). With
\(s=O(\log m)\), (16) holds strongly, so the two near-full pockets are
forced into an incompatible tangent rectangle. For a complete grid
\(d=ab\), (15) allows compatible parents; this is the universality barrier
and correctly sends the argument into the two arbitrary hidden order types.

There is also strict progress inside a failed rectangle. Normalize
\(u=(0,0),v=(1,0)\), and use the dominance coordinates from the preceding
report. If \(p_u,p_v\) are the endpoint tangents of an upper rooted hull,
then every \(x\in I(H)\) satisfies

\[
 \alpha_x<\alpha_{p_u},\qquad \beta_x>\beta_{p_v}.       \tag{17}
\]

For a lower rooted hull with tangents \(q_u,q_v\), every \(y\in I(K)\)
satisfies

\[
 A_y>A_{q_u},\qquad B_y<B_{q_v}.                        \tag{18}
\]

Indeed, an interior point lies strictly inside the tangent cone at each
root. Intersecting its ray with a transverse affine coordinate line gives
exactly these four inequalities. General position makes them strict.
Therefore a pocket reset moves both endpoint coordinates monotonically
toward compatibility. It cannot remain in the same tangent equality cell.
This is a genuine ranked first-divergence recursion, although its worst-case
depth is still linear in the cloud size.

## 5. Exact global accounting of rooted sides

Return to the original x-ordered point set. For a trace \(j<l\) and sign
\(\sigma\), let \(Q^L_{jl,\sigma}\) consist of labels \(x<j\) on side
\(\sigma\) of \(jl\). Define \(Q^R_{jl,-\sigma}\) using labels \(y>l\) on
the other side.

Let \(M^L_{jl,\sigma}(z)=R_Q(z)-1\), excluding the empty rooted hull. Every
term \(H\) produces the ordinary convex face

\[
                         H\cup\{j,l\}.                   \tag{19}
\]

Conversely, in every convex face of rank at least three, its two largest
x-labels form its unique right hull edge; all other selected labels lie on
one side of that edge. Therefore

\[
\boxed{
 z^2\sum_{j<l,\sigma}M^L_{jl,\sigma}(z)
       =F_{\ge3}(P;z).}                                  \tag{20}
\]

The reflected identity holds for right rooted sides using the two smallest
selected labels. Summing both sides has decoder load exactly two.

For the reset branch choose at most one deepest pocket for every directed
side state. A convex face contained in such a pocket is an ordinary convex
face of \(P\), and there are fewer than \(4n^2\) directed side states.
Hence

\[
 \sum_{\text{selected states}}F(I(H_*);z)
                  \le 4n^2F(P;z).                        \tag{21}
\]

This crude load is polynomial in \(n\), so its logarithm is lower order
relative to the target \(\Theta((\log n)^2)\) exponent. Equations
(20)--(21) make the reset globally summable. They do not assert that parent
and child faces coexist.

## 6. Interface with the two-tangent contraction

For one orientation state at \(jl\), write \(R_L,R_R\) for the two
rooted-hull polynomials and \(H_{jl}\) for the compatible contraction from
the preceding report. If \(d=d_{jl}^\sigma\) is its singleton degree, define
the genuine higher-history mass

\[
 H_{jl}^{>4}(1/2)=H_{jl}(1/2)-{d\over16}.                \tag{22}
\]

The subtraction is exact because every compatible singleton pair contributes
one rank-four face of half weight \(2^{-4}\).

> **Corollary 2 (summable spend/double-reset).** Fix \(L,K>1\). If
> \(H_{jl}^{>4}(1/2)\) is at least \(L\), it sums with
> rank load at most \(k-1\). Otherwise, each state
> either has \(R_L(1/2)\ge K\) or a left pocket of codimension less than
> \(\log_{3/2}K\); independently it either has \(R_R(1/2)\ge K\) or such a
> right pocket. All high-rooted states sum through (20). If neither rooted
> side pays, the state localizes to two explicit deep pockets.

If \(d_{jl}^\sigma\) is the number of compatible singleton pairs and
\(L,K\) are constant multiples of
\((d_{jl}^\sigma)^{1+\epsilon}\), this is the requested fixed-power local
dichotomy. Moreover, with \(K=(d_{jl}^\sigma)^{1+\epsilon}\),

\[
 \sum_{\substack{\text{states with}\\R_L(1/2)\ge
                   (d_{jl}^\sigma)^{1+\epsilon}}}
       \bigl((d_{jl}^\sigma)^{1+\epsilon}-1\bigr)
 \le 4F_{\ge3}(P;1/2),                                  \tag{23}
\]

and likewise on the right. Thus the rooted spend has no hidden global
overlap.

The compatible alternative is equally summable. The rank-load theorem gives

\[
 \sum_{jl,\sigma}H_{jl}^{>4}(1/2)
 \le\sum_{k\ge5}(k-1)v_k(P)2^{-k}
 \le nF(P;1/2).                                         \tag{24}
\]

At the live ranks \(k=\Theta(\log n)\), the first loss is only
\(O(\log n)\). Hence states with
\(H_{jl}^{>4}(1/2)\ge c(d_{jl}^\sigma)^{1+\epsilon}\)
also have a rigorous fixed-power global charge.

What (23) does not prove is that sufficiently many states take the spend
branch. The \(q^2m\) matching-star regression may send every state into two
deep pockets while its outer compatibility graph remains a matching.
Iterating those pockets without losing tangent ancestry is the exact
residual. The KL term in (8) shows that no entropy is lost at one reset;
turning a sequence of such identities into convex faces still requires a
coexistence or first-divergence theorem.

## 7. Sharp stress tests

The verifier checks the full fibre partition (4), every coefficient of
(5), and the numerical KL identity (8) after exact rational auditing. It
also checks the hidden-pocket grid theorem, the exact left and right global
identities (20) on rational point sets, a twenty-point central Pascal cell
and its heaviest trace, and the repeated perfect-matching-star construction.

The matching star has \(q^2\) traces with the same \(m\) singleton edges and
no higher outer-cloud amalgamation. Depending on the tiny generic
perturbation, the rooted visible profile either pays directly or (9)
identifies a deep outer pocket. In neither case is scalar singleton mass
mistaken for a compatible higher product.

Central Pascal is the opposite sharp test: its profile is recursively
balanced and the visible hull distribution branches. Formula (8) records
the balance as visible cost plus KL surplus, while (20) prevents the same
rooted histories from being spent at multiple traces.
