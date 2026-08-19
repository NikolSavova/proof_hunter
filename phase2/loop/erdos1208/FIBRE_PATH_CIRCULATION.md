# Path--cycle structure inside a rotated-difference fibre

## 1. Exact decomposition

Let `A subset Z^2` be distance-Sidon, let `|A|=k`, and put

\[
 \mathcal F_x=
 \{(p,r,q)\in A^3:r\ne q,\ x=p+J(r-q)\}.
\]

Write `h=|F_x|` and let `P,R,Q` be its three coordinate sets.  The
matching lemma says that all three coordinate projections are injective, so
`|P|=|R|=|Q|=h`.

Make a directed graph on `A` by giving every record `(p,r,q)` the edge

\[
 q\longrightarrow r
\]

labelled by `p`.  Every vertex has indegree and outdegree at most one.
Consequently its nontrivial components are directed paths and directed
cycles.  Put

\[
 S_x=Q\setminus R,\qquad E_x=R\setminus Q,
 \qquad s_x=|S_x|=|E_x|.
\]

The sets `S_x,E_x` are exactly the starts and ends of the path components;
`s_x` is the number of paths.  Summing the fibre equation and cancelling
the internal path and cycle vertices gives

\[
 \boxed{
 h x=\sum_{p\in P}p+
 J\left(\sum_{e\in E_x}e-\sum_{s\in S_x}s\right).}       \tag{1.1}
\]

This is a medium-fibre refinement of `FIBRE_CENTROID_STABILITY.md`.  It
depends on the circulation defect `s_x`, not on the much larger global
complement size `k-h`.

There is also a componentwise form.  If a path has `ell` edges, labels
`p_1,...,p_ell`, initial vertex `q_0`, and final vertex `q_ell`, then

\[
 \boxed{
 \ell x=\sum_{j=1}^{\ell}p_j+J(q_\ell-q_0).}             \tag{1.2}
\]

If the component is a cycle, then instead

\[
 \boxed{
 \ell x=\sum_{j=1}^{\ell}p_j.}                           \tag{1.3}
\]

Thus every cycle label set has centroid exactly `x`, while a long path
places `x` within one endpoint displacement divided by its length.

## 2. Quantitative localization

Assume `A` lies in an axis-parallel square of side `m`, and let

\[
 \mu_P={1\over h}\sum_{p\in P}p.
\]

Pair the `s_x` path starts arbitrarily with the `s_x` path ends.  Every
paired displacement has norm at most `sqrt(2)m`.  Equation (1.1) therefore
gives

\[
 \boxed{
 |x-\mu_P|\le {\sqrt2\,m s_x\over h}.}                    \tag{2.1}
\]

In particular, `Q=R` forces `x=mu_P` for a fibre of *any* size.  More
generally, a medium-rich fibre with small path boundary is localized just as
strongly as an almost-full fibre.

For an individual path, (1.2) similarly gives

\[
 \left|x-{1\over\ell}\sum_{j=1}^{\ell}p_j\right|
 \le {\sqrt2\,m\over\ell}.                              \tag{2.2}
\]

## 3. Global circulation budget

The total amount of internal circulation has a simple cubic bound:

\[
 \boxed{
 \sum_x |Q_x\cap R_x|
 =\sum_x(h_x-s_x)
 \le k(k-1)^2.}                                         \tag{3.1}

Indeed, a vertex in `Q_x cap R_x` gives two consecutive records

\[
 (p_0,v,u),\qquad(p_1,w,v)
\]

in the same fibre.  Choose the ordered triple `(u,v,w)`, with `u!=v` and
`w!=v`.  Equality of their outputs forces

\[
 p_0-p_1=J(w-2v+u).                                    \tag{3.2}

Vector-Sidonicity gives at most one ordered endpoint pair `(p_0,p_1)` for
the forced nonzero vector.  There are at most `k(k-1)^2` choices of
`(u,v,w)`, proving (3.1).

This budget is sharp only at the already natural cubic scale, so it does
not finish the energy estimate.  Its role is to split the remaining medium
fibres into two precise branches:

1. large circulation, which is globally chargeable by (3.1); and
2. large path boundary, where (1.2) exposes many endpoint displacements and
   the next density-increment argument must use their ambient height.

## 4. Verification

`verify_fibre_path_circulation.py` constructs every nonzero fibre of the
stored integral closure witness.  It checks the path--cycle decomposition,
the global and componentwise identities, the squared form of (2.1), and the
global circulation budget (3.1) using exact integer arithmetic.
