# Fixed-edge circuit stars: a detached-shield telescope with exact carrier load

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

The fixed-edge tensor left by
*MASS_UNIFORM_SIBLING_EAR_OR_CIRCUIT_GATE.md* has more structure than a
generic labelled four-circuit box. Let \(B\) be convex, let \(e=uv\) be an
actual boundary edge, and let \(x,y\) be singleton ears which both replace
\(e\). If \(B\cup\{x,y\}\) is not convex, then one sibling is strictly
inside the triangle formed by the other sibling and \(u,v\). Thus:

* the bad circuit is exactly \(\{u,v,x,y\}\), with no
  \(\binom{|B|}{2}\) root-pigeonhole loss;
* neither base endpoint can be hidden;
* orienting the circuit from the outer sibling to the hidden sibling gives
  a strict triangle-containment DAG.

For an outer sibling \(x\), let \(N_g\) be the physical labels hidden by it
in a marked context \(g\), let \(d_g=|N_g|\), and put

\[
       h_g=V(P|N_g)-1.                                      \tag{1}
\]

The two ordinary banks attached to the star are

\[
 \mathcal A_g=\{B_g\cup\{x_g\}\},\qquad
 \mathcal H_g=\mathcal F(P|N_g)\setminus\{\varnothing\}.     \tag{2}
\]

For arbitrary nonnegative star weights \(a_g\), define

\[
\begin{aligned}
 T&=\sum_g a_gd_g,\\
 \kappa_A&=\max_A\sum_{g:\mathcal A_g=\{A\}}a_g,\\
 \lambda_H&=\max_F\sum_{g:F\in\mathcal H_g}a_g,\\
 Q^2&=\max_g{d_g^2\over h_g}.
\end{aligned}                                               \tag{3}
\]

Then

\[
             \boxed{T\le Q\sqrt{\kappa_A\lambda_H}\,V(P).}  \tag{4}
\]

This uses no mixed union, pairwise-to-global promotion, or arbitrary-child
endpoint factorization. The child bank is detached, and every
cross-context collision is recorded by the two displayed loads.

There is an exact high-load alternative. Define

\[
 \mu=\max_{A,F}\sum_{g:\mathcal A_g=\{A\},\ F\in\mathcal H_g}a_g. \tag{5}
\]

A shield face of load \(\lambda_H\) is paired with at least
\(\lambda_H/\mu\) distinct actual carrier faces. For every threshold \(R\),
either one fixed shield exposes a context-retaining outer-carrier bank of
size at least \(R\), or

\[
             \boxed{T\le Q\sqrt{\kappa_A\mu R}\,V(P).}      \tag{6}
\]

If all stars have \(d_g\ge d\) and use at most \(N\) physical labels, then

\[
           Q\le {N\over\sqrt{f(d)-1}},                      \tag{7}
\]

where \(f(d)\) is the minimum number of convex subsets of a planar
general-position \(d\)-set. At the live scale
\(d\ge n^\gamma/(\log n)^K\), the established safe estimate

\[
          \log f(d)\ge(1/8-o(1))(\log d)^2                 \tag{8}
\]

makes (7) at most
\(2^{-(\gamma^2/16-o(1))(\log n)^2}\). It absorbs
\(R=n^{\sigma\log\log n}\) and polynomial carrier/pair loads. Hence live
dense fixed-edge circuit mass forces either the desired quasipolynomial
outer-carrier bank or a genuinely superpolynomial literal carrier/pair
load. Sharing \(u,v\) alone does not preserve the tensor.

The remaining high load is exactly the source/carrier-mask atom isolated
by *DETACHED_PAIR_SOURCE_MASK_HALL.md* and
*RECOVERABLE_CARRIER_COARSENING_MASK_RUN_GATE.md*. After fixing
\((A,F)\), distinct full sources give an injective carrier bank, a
canonical longest deleted run gives the exact one-face Boolean bank, and
surviving compressed gaps give the rooted-module product. Copies of one
actual source/history remain an explicit load rather than geometric
entropy.

The theorem is sharp in arbitrary-child scope. Any planar order type can
be affinely shrunk into the common interior of many nested ear triangles
\(\triangle uvx\). Every nonempty child face is then incompatible with
every rooted carrier \(B\cup\{x\}\). Repeating the shield across distinct
contexts is possible, but the distinct full outer carriers give exactly
the high-load bank in (5)--(6).

## 1. Same-edge circuits are strict containment

Write the cyclic polygon as \(B=(\ldots,w,u,v,z,\ldots)\). A singleton ear
replacing \(uv\) lies outside the supporting halfplane of \(uv\) and
strictly inside the supporting halfplane of every other old edge. The old
support lines through \(wu\) and \(vz\) therefore still expose \(u,v\)
after any number of such singleton ears is inserted. Every other old
vertex also retains an old supporting line.

Suppose \(B\cup\{x\}\) and \(B\cup\{y\}\) are ordinary but
\(B\cup\{x,y\}\) is not. No old point can be hidden, so one of \(x,y\) is
hidden; say \(y\). The stellar subdivision identity gives

\[
 \operatorname{conv}(B\cup\{x\})\setminus\operatorname{conv}(B)
       \subseteq\triangle uvx.                              \tag{9}
\]

Since \(y\notin\operatorname{conv}(B)\) but
\(y\in\operatorname{int}\operatorname{conv}(B\cup\{x\})\),

\[
                         y\in\operatorname{int}\triangle uvx. \tag{10}
\]

Conversely, (10) makes the union nonconvex. Define

\[
 x\succ_e y\quad\Longleftrightarrow\quad
 y\in\operatorname{int}\triangle uvx.                       \tag{11}
\]

This relation is transitive because
\(z\in\triangle uvy\) and \(y\in\triangle uvx\) imply
\(\triangle uvy\subset\triangle uvx\). It is irreflexive, hence a strict
partial order.

In the strip chart \(u=(-1,0),v=(1,0)\), put

\[
        L(p)={p_y\over1+p_x},\qquad
        R(p)={p_y\over1-p_x}.                               \tag{12}
\]

Barycentric arithmetic gives

\[
 x\succ_e y\quad\Longleftrightarrow\quad L(x)>L(y),\ R(x)>R(y). \tag{13}
\]

Thus the circuit signature is ordinary two-coordinate dominance. This
strengthening applies when \(u,v\) are the actual common insertion edge.
For an arbitrary circuit-root pair merely lying in \(B\), the generic
four signed types remain necessary.

## 2. Dense tensors contain high-degree stars

Let \(Z\) be the union of rich role clouds in one marked fixed-edge cell,
\(N=|Z|\), and orient every incompatible pair by (11). If the directed
graph has \(E\) edges, discard outer vertices of outdegree less than
\(E/(2N)\). Fewer than \(E/2\) edges are discarded, so retained stars carry
at least \(E/2\) circuit edges and each satisfies

\[
                              d_g\ge {E\over2N}.            \tag{14}
\]

Thus \(E\ge\rho N^2\) gives \(d_g\ge\rho N/2\). A single dense
\(D\)-by-\(D\) role pair already gives \(d_g=\Omega(D)\). If every pair
among \(s\) clouds of size \(D\) is dense, then \(d_g=\Omega(sD)\).
Dyadic bins for \(N,E,d_g\) cost only polynomially many marked cells.

The weighted application needs one additional, explicit uniformization.
Equations (3)--(4) assign one weight \(a_g\) to every retained edge of a
star. For arbitrary edge weights, first dyadically bin the sibling-label
classes and then replace every retained edge weight by the lower endpoint
of its bin. On the minimizer slice, positive normalized weights lie between
the \(1/n\) atom floor and one, so there are \(O(\log n)\) bins. A bin
carrying mass \(b\) and having maximum label mass at most \(b/r\) contains
at least \(r/O(\log n)\) physical labels after a further mass-pigeonhole.
Thus the mass-uniform role-forest hypothesis loses only polynomial factors
and still gives \(d=n^\gamma/\operatorname{polylog}n\). Without this
uniformization, large unweighted support alone is not asserted to carry
large weighted circuit mass.

## 3. Proof of the telescope and carrier alternative

Every \(A_g=B_g\cup\{x_g\}\) is ordinary. Every member of
\(\mathcal H_g\) is an ordinary ambient face by heredity. Grouping weighted
incidences by actual outputs gives

\[
 \sum_ga_g\le\kappa_AV(P),\qquad
 \sum_ga_gh_g\le\lambda_HV(P).                            \tag{15}
\]

Since \(d_g\le Q\sqrt{h_g}\), weighted Cauchy yields

\[
\begin{aligned}
 T&\le Q\sum_ga_g\sqrt{h_g}\\
  &\le Q\sqrt{\left(\sum_ga_g\right)
                   \left(\sum_ga_gh_g\right)}
  \le Q\sqrt{\kappa_A\lambda_H}\,V(P).
\end{aligned}                                               \tag{16}
\]

This proves (4). If \(F\) realizes \(\lambda_H\), partition its incident
stars by the actual carrier \(A_g\). Each part weighs at most \(\mu\), so
there are at least \(\lambda_H/\mu\) distinct carrier faces. If this is
less than \(R\), then \(\lambda_H<\mu R\), proving (6).

Finally, \(h_g\ge f(d_g)-1\ge f(d)-1\) and \(d_g\le N\), proving (7).
Equivalently, if \(T\ge\tau V(P)\) and no fixed shield sees \(R\) distinct
carriers, then

\[
 \boxed{\kappa_A\mu\ge{\tau^2(f(d)-1)\over N^2R}.}          \tag{17}
\]

Thus an unpaid live tensor forces an enormous literal carrier or
carrier--shield pair load, not an unnamed context multiplicity.

The outer-ear role identifies \(x\in A\), hence \(B=A-\{x\}\). A nonempty
\(F\subseteq N_g\) identifies a canonical hidden sibling, for example its
first label. Since \(uv\) is fixed, \((A,F)\) retains the literal circuit.
Thus \(\mu\) is precisely the residual source/guard/reset multiplicity
after geometric marks are fixed. If role supports or the actual edge were
forgotten, their true description factors must instead be included in
\(\mu\).

## 4. Exact carrier-mask and run splice

Fix an actual pair \((A,F)\) of total weight \(H\). Suppose occurrence
\(\omega\) came from the ordinary full source

\[
                         S_\omega=A\cup G_\omega.           \tag{18}
\]

With

\[
 \kappa_{\rm src}=\max_S\sum_{\omega:S_\omega=S}a_\omega,  \tag{19}
\]

grouping by the actual source gives

\[
                         H\le\kappa_{\rm src}V(P).         \tag{20}
\]

For each nonempty mask choose its first longest cyclic run
\(R(G_\omega)\). Every

\[
 A\cup J,\qquad\varnothing\ne J\subseteq R(G_\omega)       \tag{21}
\]

is an ordinary downface of \(S_\omega\). Define its actual output load
\(\Lambda_{\rm run}\) in the evident way. Exact incidence counting gives

\[
 \boxed{\sum_\omega a_\omega
       \left(2^{|R(G_\omega)|}-1\right)
        \le\Lambda_{\rm run}V(P).}                         \tag{22}
\]

A rank-\(t\) mask with at most \(r\) cyclic runs has a chosen run of rank
at least \(\lceil t/r\rceil\). If many compressed gaps instead survive as
actual released boundary gaps, the rooted-module theorem in
*RECOVERABLE_CARRIER_COARSENING_MASK_RUN_GATE.md* applies with its literal
carrier/root/endpoint decoder. Fixing \((A,F)\) adds no new ambiguity.

Equations (20)--(22) are the honest endpoint. Repeating one actual source
under noncanonical history names raises both loads without creating a
face. Canonical radial depth is already decoded by the source and endpoint
mark, as proved in *DETACHED_PAIR_SOURCE_MASK_HALL.md*. The remaining
multiplicity must be an actual guard/tuple degree or explicit metadata;
the \(1/n\) atom floor alone does not bound it.

## 5. Sharp arbitrary-child and context-reuse barrier

Take a convex quadrilateral \(B\) with top edge \(uv\). Choose outer ears
\(X\) whose triangles \(\triangle uvx\) have a common open intersection
\(\Omega\) outside \(\operatorname{conv}(B)\). Any finite planar order
type \(Y\) can be sent by an orientation-preserving affine contraction
into \(\Omega\). Then for every \(x\in X,y\in Y\),

\[
 B\cup\{x\},\ B\cup\{y\}\in\mathcal F(P),\qquad
 y\in\operatorname{int}\triangle uvx.                     \tag{23}
\]

Therefore every pair is a fixed-edge circuit, and for every nonempty
\(F\in\mathcal F(P|Y)\),

\[
                         B\cup\{x\}\cup F\notin\mathcal F(P). \tag{24}
\]

The detached child can have arbitrary order type, and none of its nonempty
faces has a rooted mixed splice.

Put context ears \(z_1,\ldots,z_H\) on a boundary edge nonadjacent to
\(uv\). The carriers

\[
                         B\cup\{x,z_h\}                    \tag{25}
\]

are ordinary and distinct while reusing the same child bank. The shield
load and outer-carrier bank are both exactly \(H\). This attains the
high-load alternative without a mixed face.

It is not a live low-face regression. Scaling \(H\) to quadratic context
entropy requires a large actual context-face family, which is itself the
outer bank in (25). The example proves that this bank must be charged and
that no arbitrary-child rooted splice can replace it.

## 6. Verification

Run:

    python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_fixed_edge_circuit_star_shield_telescope.py

The exact rational checker verifies a four-role dominance tensor, all 96
labelled circuits and hidden siblings, three opposite-edge contexts, the
weighted telescope and its nontrivial carrier/shield/pair loads, dense
outdegree pruning, and the fixed-shield carrier count. It exhausts cyclic
masks through rank eight for (22) and checks a finite arbitrary-child
instance in which all 31 nonempty child faces fail the rooted splice.
