# Large Gaussian cells in the zero-sum endpoint hypergraph

## 1. Verdict

Let (A\subset[0,m]^2) be distance-Sidon and let (mathcal H_A) be the
linear three-uniform hypergraph of six-endpoint zero-sum directed-edge
matchings from `AMBIENT_CENTROID_ENDPOINT_DIFFERENCE_HYPERGRAPH_GATE.md`.
For a hyperedge with displacement vectors (u_1+u_2+u_3=0), decorate
every ordered pair (i\ne j) by

\[
 r=|u_i|^2-|u_j|^2,
 \qquad d=2\det(u_i,u_j).                              \tag{1.1}
\]

Write (ν_A(r,d)) for the number of decorated ordered pairs.  Then

\[
 \sum_{r,d}ν_A(r,d)=6|\mathcal H_A|.                \tag{1.2}
\]

The kill-search has a sharp answer.

1. Every individual cell is divisor-small:

   \[
    \boxed{ν_A(r,d)\le m^{o(1)}.}                    \tag{1.3}
   \]

2. There are rigorous reciprocal-coordinate tails

   \[
   \boxed{
   \sum_{r,d}{ν_A(r,d)\over |r|}
       \ll k^2\log(2m),\qquad
   \sum_{r,d}{ν_A(r,d)\over |d|}
       \ll (k^2+mk)\log(2m).}                         \tag{1.4}
   \]

3. No polynomial decay in a large norm-gap or determinant cutoff is
   possible.  For every odd prime (p), the explicit set

   \[
    A_p=\{(x+p[x^2]_p,[x^2]_p):0\le x<p\}             \tag{1.5}
   \]

   is genuinely Euclidean distance-Sidon, has (k=p), (m=O(p^2)), and
   has (Omega(p^4)=Omega(m^2)) clean zero-sum hyperedges.  For every
   fixed (epsilon>0),

   \[
   \boxed{
   \sum_{\substack{|r|>p^{2-\epsilon}\\
                   |d|>p^{1-\epsilon}}}
        ν_{A_p}(r,d)=\Omega(p^4).}                 \tag{1.6}
   \]

   These records occupy (p^{4-o(1)}=m^{2-o(1)}) different joint cells.

Thus large determinant is not a sparse tail: the ambient (m^2) equality
model lives almost entirely in simultaneously large norm-gap and
large-determinant cells.  Any conjecture gaining a factor (D^{-c}),
(R^{-c}), or ((RD)^{-c}) from the cutoffs is false.

The strongest natural statement left is the flat support bound

\[
 \boxed{
 |\operatorname{supp}ν_A|
 \le m^{o(1)}(k^3+m^2).}                              \tag{1.7}
\]

It is sharp on (1.5), but (1.3) makes it exponent-equivalent to the
original endpoint-hypergraph gate.  It is a clean reformulation, not a
proved simplification.  The only available tail savings are reciprocal
weights such as (1.4); removing those weights is exactly the unresolved
problem.

## 2. Pointwise cells and small-coordinate tails

For directed displacement vectors (u,v\in\mathbb Z[i]), put

\[
 \alpha=u-v,\qquad\beta=u+v.
\]

Then

\[
 \boxed{\alpha\overline\beta=r-id,}                  \tag{2.1}
\]

and the factors recover

\[
 u={\alpha+\beta\over2},\qquad
 v={\beta-\alpha\over2}.                             \tag{2.2}
\]

Distance-Sidonicity makes a directed displacement recover its endpoint
edge.  Two hypergraph vertices determine at most one third vertex, so an
ordered edge pair occurs in at most one hyperedge.  The Gaussian divisor
count consequently gives

\[
 ν_A(r,d)\le4\tau(r^2+d^2)^2=m^{o(1)},             \tag{2.3}
\]

proving (1.3).

There are two cumulative bounds.  First,

\[
 \boxed{
 \sum_{0<|r|\le R}ν_A(r,d)\le4k^2R.}              \tag{2.4}
\]

Indeed the (\(\binom{k}{2}\)) squared edge lengths are distinct integers.  Once
the first directed edge is fixed, an integer interval of radius (R)
contains at most (2R) other norm labels, each with two orientations.

Second, the low-determinant lattice-coset theorem gives

\[
 \boxed{
 \sum_{0<|d|\le D}ν_A(r,d)
 \ll D(k^2+mk).}                                      \tag{2.5}
\]

Each hyperedge supplies six ordered pairs with
(|d|=2|\det(u_1,u_2)|), so this is precisely the earlier low-determinant
theorem with harmless constant changes.  Dyadic summation of (2.4)--(2.5),
using (|r|,|d|=O(m^2)), proves (1.4).  The same statements hold for
occupied-cell indicators because every occupied cell has load at least
one.

## 3. The explicit height-(O(p^2)) finite-field lift

The older generic shear guaranteed only (O(p^5)) height.  The particular
shear (t=p) is always distance-Sidon.

Put (y_x=[x^2]_p\in\{0,\ldots,p-1\}).  Orient an edge by the original
labels so that (x>x'), and write

\[
 h=x-x'\in\{1,\ldots,p-1\},\qquad z=y_x-y_{x'}.
\]

Its post-shear squared length is

\[
 Q_p(h,z)=(h+pz)^2+z^2.                               \tag{3.1}
\]

**Lemma.**  The values (Q_p(h,z)) are distinct for (1\le h<p) and
(|z|<p).

For fixed (z=s\ge0), (3.1) increases with (h), and consecutive
(s)-intervals are disjoint because

\[
 (p(s+1)+1)^2+(s+1)^2>(p(s+1)-1)^2+s^2.             \tag{3.2}
\]

For (z=-t\le-1), write (Q_p(h,-t)=(pt-h)^2+t^2).  It decreases with
(h), and consecutive (t)-intervals are disjoint because

\[
 (pt+1)^2+(t+1)^2>(pt-1)^2+t^2.                     \tag{3.3}
\]

For opposite signs, suppose

\[
 (ps+h)^2+s^2=(pt-h')^2+t^2,\qquad s\ge0, t\ge1.  \tag{3.4}
\]

Put (A=ps+h), (B=pt-h').  If (t\le s), then (A>B) while
(t^2-s^2\le0), impossible.  Hence (t>s).  Equality forces (A>B), so
(h+h'>p(t-s)).  Since (h+h'\le2p-2), necessarily (t=s+1).  But then

\[
 (A-B)(A+B)=2s+1,
 \qquad A+B\ge2ps+2>2s+1,                            \tag{3.5}
\]

again impossible.  This proves the lemma.

Equal edge lengths therefore give the same ((h,z)).  Modulo (p), the
parabola identity (z\equiv h(x+x')) recovers both endpoints because
(h\ne0).  Thus (1.5) is distance-Sidon, and its coordinate width is less
than (p^2).

## 4. The doubly large tail has fourth-order support

The shear preserves exact triple sums.  Before shearing, all
(\(\binom{p}{3}\)) unordered triple sums lie in fewer than (\(9p^2\)) integer
cells.  If (t_s) is their load, then

\[
 \sum_st_s(t_s-1)
 \ge {\binom p3^2\over9p^2}-{p\choose3}
 =\Omega(p^4).                                       \tag{4.1}
\]

Distinct triples in one cell are disjoint: cancelling a common endpoint
would contradict the finite-field parabola's pair-sum uniqueness.  Each
ordered pair of triples has six endpoint matchings, so

\[
 |\mathcal H_{A_p}|=6\sum_st_s(t_s-1)=\Omega(p^4).   \tag{4.2}
\]

Apply (2.4) with (R=p^{2-\epsilon}) and (2.5) with
(D=p^{1-\epsilon}).  Since (k=p,m=O(p^2)), the discarded masses are
both (O(p^{4-\epsilon})).  This proves (1.6).  Dividing the remaining
mass by the pointwise cap (2.3) proves the support lower bound.

At (p=43), the exact profile is

\[
 (m,|\mathcal H|,|\operatorname{supp}_{d\ne0}|,
   \text{nonzero mass},\maxν)
 =(1790,126852,374288,758772,8).                     \tag{4.3}
\]

Even after imposing (|r|>43^2) and (|d|>43), there are (341244)
occupied cells carrying (690220) records, with maximum load eight.

## 5. Other requested stresses

### Critical planted integer parabola

For ({(j,j^2):0\le j<n\}), fixing a triple's sum (s) and square sum
(t) fixes

\[
 3t-s^2=(a-b)^2+(b-c)^2+(c-a)^2
       =2(x^2+xy+y^2).                               \tag{5.1}
\]

The Eisenstein divisor bound gives only (n^{o(1)}) triples per cell.
Hence the deliberate parabola core has at most (n^{3+o(1)}) hyperedges
and Gaussian cells.  In the critical planted extension, (n=\Theta(m^{1/2})),
so this is (m^{3/2+o(1)}\ll m^2).  The construction which killed the
colored derivative energy does not kill the ambient support gate.

### Multi-arcs

The same argument gives (L^{3+o(1)}) internal centroid matchings per
arc.  Generic linear and constant parameters avoid cross-arc triple-sum
coincidences, leaving at most

\[
 bL^{3+o(1)}\le(bL)^{3+o(1)}=k^{3+o(1)}.             \tag{5.2}
\]

The stored four-arc certificate has no equal-centroid pair at all.

### Golomb hybrids

A pure Golomb ruler has (d=0) in every hyperedge.  If a fixed or
subpolynomial-size off-line gadget (G) is attached, every noncollinear
record uses a gadget endpoint.  Fixing its role and value and three more
endpoints determines the final pair by additive Sidonicity, giving

\[
 O(|G|k^3)=m^{o(1)}k^3.                               \tag{5.3}
\]

### Singer endpoint-product constructions

For any additive Sidon set, fixing four endpoints in an equal-triple-sum
pair determines the remaining unordered pair, so
(|\mathcal H_A|=O(k^4)).  Singer has (k\asymp q,m=O(q^2)), hence
(k^4=O(m^2)).  Its selected fourth-order records are equal-area rather
than equal-centroid; the stored eight-point certificate has
(mathcal H_A=\varnothing).

## 6. Exact surviving conjecture

For polylogarithmic (R_0,D_0\ge1), set

\[
 \mathcal C_A(R_0,D_0)
 =\{(r,d):ν_A(r,d)>0, |r|>R_0, |d|>D_0\}.        \tag{6.1}
\]

The precise survivor is:

> **Flat large-Gaussian-support gate.**
> 
> \[
> |\mathcal C_A(R_0,D_0)|
> \le m^{o(1)}(k^3+m^2).                              \tag{6.2}
> \]

The discarded small-coordinate mass is already controlled by
(2.4)--(2.5).  Conversely, (2.3) turns (6.2) into the desired hypergraph
bound, while the hypergraph bound trivially implies (6.2).  The statements
are exponent-equivalent.

The explicit lift proves (6.2) is sharp at (m^2) and permits no cutoff
decay.  What remains is to explain why a critical-height distance-Sidon set
cannot occupy (k^{4-o(1)}) jointly large cells.

## 7. Verification

Run

```text
python3 phase2/loop/erdos1208/verify_large_gaussian_cell_support_tail_audit.py
```

The verifier checks the (Q_p) injectivity, distance-Sidonicity of the
explicit lifts, exact Gaussian profiles through (p=43), the finite
doubly-large core, integer parabola profiles, and the stored multi-arc and
Singer certificates.
