# The balanced-anchor arboricity gate

## 1. Outcome

Keep the endpoint graphs `G_omega` and the balanced moment

\[
 \mathcal B_N=
 \sum_\omega\sum_{e=(\ell,z)\in G_\omega}
 \min\{d_L(\ell),d_R(z)\}                     \tag{1.1}
\]

from `HYBRID_ENDPOINT_OPPOSITE_CHARGE_GATE.md`.  Edges and degrees in this
note count multiplicity.  The new exact reduction is

\[
 \boxed{
 \mathcal B_N\le
 2\sum_\omega a(G_\omega)|E(G_\omega)|,}       \tag{1.2}
\]

where `a(G)` is the multigraph arboricity.  Consequently the normal route
is finished by the single size-biased statement

\[
 \sum_\omega a(G_\omega)|E(G_\omega)|
 \le N^{o(1)}|C_N|.                            \tag{1.3}
\]

This is not yet proved.  It sharpens the missing theorem: every failure has
a genuinely dense two-sided endpoint-realizable subgraph, not merely a
large star or a bundle of charge collisions.

## 2. Forest-orientation proof

The arboricity `a(G)` is the minimum number of forests whose edge multisets
partition `E(G)`.  In a multigraph, two parallel copies cannot lie in the
same forest.  Orient every forest toward an arbitrary root in each
component.  Every vertex then has outdegree at most one in each forest and
therefore at most `a(G)` in total.

For any such orientation,

\[
 \begin{aligned}
 \sum_{uv\in E(G)}\min\{d(u),d(v)\}
 &\le \sum_{u\to v}d(u)\\
 &=\sum_u d(u)d^+(u)\\
 &\le a(G)\sum_u d(u)
 =2a(G)|E(G)|.                                  \tag{2.1}
 \end{aligned}
\]

Applying (2.1) to each `G_omega` proves (1.2).  This is the standard
arboricity estimate behind the Chiba--Nishizeki subgraph-listing method;
the proof above includes the multigraph extension needed here.  See
Chiba--Nishizeki, *Arboricity and Subgraph Listing Algorithms*,
SIAM J. Comput. 14 (1985),
<https://doi.org/10.1137/0214017>.

By Nash--Williams, high arboricity is equivalent to a dense subgraph:

\[
 a(G)=\left\lceil
 \max_{H\subseteq G,\ |V(H)|\ge2}
 {|E(H)|\over |V(H)|-1}\right\rceil.           \tag{2.2}
\]

Thus (1.3) is exactly a weighted prohibition on dense anchor cores.

## 3. Parallel bundles and a matched three-edge path

Let `r_{ell,z}` be the multiplicity of one anchor pair inside a fixed
`G_omega`, and put

\[
 \mathcal P_2=\sum_{\omega,\ell,z}r_{\ell,z}^2. \tag{3.1}
\]

There is an exact decomposition

\[
 \boxed{
 \mathcal B_N=\mathcal P_2+\mathcal M_3,}       \tag{3.2}
\]

where `M_3` is the size of a canonically selectable family of genuine
three-edge paths.

Indeed, fix a cell `(ell,z)` of multiplicity `r`.  Besides its `r` parallel
edge occurrences, the left endpoint has `d_L(ell)-r` other incident edge
occurrences and the right endpoint has `d_R(z)-r`.  Match the smaller of
these two multisets injectively into the larger.  For every one of the `r`
central copies this gives

\[
 r\min\{d_L(\ell),d_R(z)\}
 =r^2+r\min\{d_L(\ell)-r,d_R(z)-r\}.            \tag{3.3}
\]

The second term counts a central edge together with one nonparallel edge at
each endpoint.  Summing (3.3) proves (3.2).  In particular, parallel-edge
multiplicity and the genuine two-sided core can be attacked separately.

If the maximum parallel multiplicity is `mu` and the underlying simple
graph has arboricity at most `alpha`, then

\[
 a(G_\omega)\le\mu\alpha.                      \tag{3.4}
\]

This follows by decomposing the simple graph into `alpha` forests and
placing the at most `mu` copies of each edge in separate copies of those
forests.  Hence subpolynomial `mu` and `alpha`, even in a size-biased
aggregate form, suffice for (1.3).

## 4. Exact geometry of one matched path

Let the central configuration have parameters `(a_0,p_0,q_0)` and anchors
`(ell,z)`.  Let a left-neighbour configuration share `ell`, and a
right-neighbour configuration share `z`.  Write their parameter changes as

\[
 (\eta_L,\pi_L,\rho_L)
 =(a_L-a_0,p_L-p_0,q_L-q_0)
\]

and

\[
 (\eta_R,\pi_R,\rho_R)
 =(a_R-a_0,p_R-p_0,q_R-q_0).                    \tag{4.1}
\]

The shared endpoint-midpoint label forces both `eta_L` and `eta_R` from
the corresponding `pi` variables.  The left collision supplies the seven
`D-D=D+D` displacements

\[
 \eta_L,\ \eta_L+\rho_L,\ \eta_L+\pi_L,\ 0,
 J\rho_L,\ (I+J)\rho_L-\pi_L,
 (I+J)(\rho_L-\pi_L),                           \tag{4.2}
\]

while the right collision supplies

\[
 \eta_R,\ \eta_R+\rho_R,\ \eta_R+\pi_R,\ 0,
 \rho_R-\pi_R,\ -J\rho_R,
 \rho_R-(I+J)\pi_R.                            \tag{4.3}
\]

All three configurations retain both adaptive-popular shifts and their
seven original members of `D`.  The fourth anchor pair completing the
three-edge path would have colour

\[
 q_*=q_0+\rho_L+\rho_R.                         \tag{4.4}
\]

There is no assertion that the fourth edge exists.  Equations
(4.1)--(4.4), plus the matching condition from Section 3, are the exact
restart point for an endpoint-sensitive incidence or Fourier estimate.

## 5. Proper edge colours are not enough

After parallel copies are collapsed, every edge has the colour

\[
 q=-J(z-\ell).                                  \tag{5.1}
\]

Each colour class is a matching, so the underlying graph is properly
edge-coloured.  This alone cannot prove (1.3): complete bipartite graphs
have proper one-factorizations and arbitrarily large arboricity.  Any proof
must use the endpoint label `omega`, the compatible second shift `p`, all
seven `D` memberships, and adaptive popularity.  Replacing the problem by
a generic properly coloured graph returns to the known anti-Ramsey
cube-root barrier.

## 6. Exact diagnostics

`analyze_balanced_anchor_parallel.py` recomputes the multigraphs and checks
the parallel square moment, (3.2), and exact core degeneracies.  Selected
profiles are

\[
\begin{array}{c|r|r|r|r|r}
\text{family}&|C_N|&\mathcal P_2&\max r&\mathcal B_N&
 \max\text{ weighted degeneracy}\\ \hline
\text{closure }40&301640&302152&2&313937&2\\
\text{closure }80&303490&303582&2&304560&2\\
\text{Costas }23&458872&465854&3&584338&3\\
\text{Costas }31&731126&742794&3&946578&3\\
\text{Costas }37&2853770&2912002&3&3808250&4\\
\text{Costas }41&4445470&4532186&4&6240597&5
\end{array}                                     \tag{6.1}
\]

For Costas `p=43`, without the slower core peeling, the exact values are

\[
 |C_N|=8250792,\quad \mathcal P_2=8410596,
 \quad\max r=4,\quad\mathcal B_N=11901168.      \tag{6.2}
\]

Thus parallel load remains between `1.0003` and `1.0205` in the stored
large families; most of `B_N-|C_N|` is the genuine path term `M_3`.
The slowly growing degeneracies are encouraging but are finite evidence,
not a proof of (1.3).

Run

```bash
python3 phase2/loop/erdos1208/analyze_balanced_anchor_parallel.py \
  --extended --cores
```

The default extended core pass skips the expensive Costas-43 peeling but
still checks its parallel and balanced moments.  Add `--p43-core` to force
that final core computation.

## 7. Current proof target

The next theorem should be stated directly in one of these equivalent
sufficient forms:

1. the size-biased arboricity estimate (1.3); or
2. a subpolynomial aggregate bound for both `P_2` and the selected matched
   path family `M_3` in (3.2).

A black-box BSG or DRC extraction is insufficient: sparse shear models
already satisfy the affine-copy and popularity data without producing a
complete patch.  The new input must retain complete-difference endpoint
realizability.  The most focused next subproblem is to bound parallel
multiplicity for a fixed `(omega,q,w)` and then prove that a high-arboricity
simple core forces either ordinary support growth or a forbidden radial
collision.
