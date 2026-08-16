# MDS anti-modules: the same-parent extraction barrier and its one-gap payment

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

An arbitrary quadratic-entropy same-parent petal family need not contain a
positive-linear collection of recoverable modules, even after
`2^{o((log n)^2)}` thinning.  A high-rate Reed--Solomon code gives an exact
counterfamily.

Take `q=Theta(log n)` disjoint outer macroblocks, each with alphabet
`mathbb F_p`, and represent a word by its transversal.  Let `mathcal C` be
the length-`q`, dimension-`k=q-c` Reed--Solomon code.  Then

\[
                 |\mathcal C|=p^{q-c},\qquad
                 d_{\min}=c+1.                            \tag{1}
\]

Any nontrivial recoverable module has coordinate support at least `c+1`.
Therefore a Cartesian product contained in `mathcal C` can have at most

\[
                              \left\lfloor{q\over c+1}\right\rfloor       \tag{2}
\]

disjoint variable modules.  Choose

\[
 q=\left({1\over4}+o(1)\right)L,qquad
 c=\left({1\over4}+o(1)\right){L\over\log L},qquad
 \log p=L.                                                \tag{3}
\]

Then `log|mathcal C|=(1/4-o(1))L^2`, but (2) is only
`O(log L)=o(L)`.  No subfamily can contain a product absent from the whole
code.

This remains a counterexample after the exact two-tangent state is fixed.
Split the coordinates into equal left/right halves.  Both projections are
full, so the tangent rectangle has `p^q` ordinary cross-combinations, but

\[
                    {p^q\over|\mathcal C|}=p^c
                           =2^{O(L^2/\log L)}=2^{o(L^2)}.  \tag{4}

Thus diagonal amalgamation gains no fixed leading coefficient on this
family.  Balanced recursion merely exposes the same global MDS constraint;
it cannot manufacture `Theta(L)` independent modules.

The construction is exactly planar-realizable with one common parent,
common bad interval face `W`, fixed circuit, fixed insertion mark, and fixed
tangent cell.  Put each alphabet in a tiny outer macro-cap cluster and
select only the codeword transversals.  Every selected source is ordinary.
The same-rank endpoint bank is polynomial, as in
`ENDPOINT_BASELINE_SCARCITY.md`.

This is **not** a face-count counterexample.  The ambient clusters are a
recoverable radial container system, whether or not the selected records
form a product.  The detached one-gap theorem uses the whole cluster
complex and gives

\[
 \log V(P)\ge
       q\log p+c_0(\log p)^2-o(L^2)
       =\left({1\over4}+c_0-o(1)\right)L^2.               \tag{5}

With the conservative `c_0=1/8`, this is `3/8-o(1)`.  Hence the MDS family
is a sharp kill of **selected-family module extraction**, while explicitly
realizing the anchor/one-gap shield branch which pays.  A valid general
theorem must extract modules from ambient planar circuit containers, not
from the selected record support alone.

## 1. Recoverable modules and the minimum-distance obstruction

Let the outer label set be partitioned into disjoint coordinate blocks

\[
                     X_1\mathbin{\dot\cup}\cdots
                       \mathbin{\dot\cup}X_q,qquad |X_i|=p.       \tag{6}
\]

A transversal is identified with a word `x=(x_1,...,x_q) in mathbb F_p^q`.
For the obstruction it is enough to use the following permissive notion.
A **disjoint recoverable product** inside a word family `mathcal A` is a
set

\[
                  \{x(a_1,\ldots,a_t):a_i\in A_i\}
                         \subseteq\mathcal A,             \tag{7}

\]

where `|A_i|>=2`, and changing `a_i` can alter only coordinates in a set
`S_i subseteq[q]`, with the `S_i` pairwise disjoint.  This includes block
products, disjoint petals, and any module whose label support is recovered
independently of the other choices.

> **Theorem 1 (minimum distance bounds recoverable modules).**  If
> `mathcal A` is contained in a linear code of minimum Hamming distance
> `d`, then every product (7) has
> 
> \[
>                              t\le\lfloor q/d\rfloor.     \tag{8}
> \]

**Proof.**  Fix all choices except `a_i`, and take two different values of
that module.  The difference of the resulting codewords is a nonzero
codeword supported inside `S_i`.  Hence `|S_i|>=d`.  The supports are
disjoint, so `td<=sum_i|S_i|<=q`.  QED.

The conclusion is hereditary: a subfamily of `mathcal A` cannot acquire a
product which was absent from `mathcal A`.  Thus no amount of thinning,
subquadratic or otherwise, repairs (8).

## 2. The explicit MDS family

Let `p` be prime, let `q<p`, and choose distinct evaluation points
`alpha_1,...,alpha_q in mathbb F_p`.  Put

\[
 \mathcal C_{p,q,k}=
 \{(f(\alpha_1),\ldots,f(\alpha_q)):
                      f\in\mathbb F_p[z],\ \deg f<k\}.    \tag{9}

\]

The evaluation map is injective, so `|mathcal C|=p^k`.  A nonzero
polynomial of degree less than `k` has at most `k-1` roots, giving

\[
                         d_{\min}=q-k+1.                  \tag{10}

\]

Equality is attained by a polynomial with `k-1` selected evaluation roots.
Set `k=q-c`; Theorem 1 gives (2).

To scale, choose a prime `p_L` between `2^L` and `2^(L+1)`, put

\[
 q=\lfloor L/4\rfloor,qquad
 c=\left\lceil{q\over\log L}\right\rceil,qquad
 k=q-c.                                                    \tag{11}

\]

The label count of the outer blocks is `qp_L`, so its logarithm is
`L+o(L)`.  Equations (1), (10), and (11) give

\[
 \log|\mathcal C|
   =(q-c)\log p_L=(1/4-o(1))L^2,                         \tag{12}

\]

while every disjoint product has only `O(log L)` variable modules.

This is stronger than a sparse random-code obstruction: it is explicit,
linear, MDS, and its anti-module certificate is one line of exact distance
arithmetic.

## 3. Exact tangent-rectangle stress test

Assume `q` is even and split the coordinates into `q/2` left and `q/2`
right blocks.  Reed--Solomon is MDS, so the projection to any `t`
coordinates has size

\[
                              p^{\min(k,t)}.              \tag{13}

\]

For (11), `k>q/2`.  Hence both projection supports have size `p^(q/2)`.
In the planar realization below, the root and all four tangent neighbours
are fixed, and every cross-combination of a left projection word and a
right projection word is an ordinary source.  This is precisely the
complete rectangle supplied by two-tangent amalgamation.  Its size is
`p^q`, whereas the selected MDS graph has `p^(q-c)` edges.  Formula (4)
follows.

The surplus is subquadratic but not accidental.  Conditional on either
projection, the code has exactly `p^(k-q/2)` continuations.  At a balanced
binary split, puncturing and shortening an MDS code again gives an MDS
support.  The `c` global parity symbols can be revealed across levels, but
their entire entropy is only

\[
                              c\log p=O(L^2/\log L).       \tag{14}

\]

Therefore any recursion which counts only projection rectangles and
relative tangent states obtains at most a `2^{o(L^2)}` surplus on this
family.  To gain a fixed coefficient it must use faces outside the selected
code support.

## 4. Planar realization with the full fixed tuple

Use the rational open construction from
`ENDPOINT_BASELINE_SCARCITY.md`.  Take a fixed consecutive high-cap parent

\[
                         T=\{t_0<\cdots<t_{r-1}\},
                         e=\{t_0,t_{r-1}\}.              \tag{15}

\]

For the coefficient-scaled regression one may keep this core at five
vertices, so it contributes only `O(1)` fixed macro sites.  Allowing
`r=O(L)` changes none of the anti-module statements, but a literal cyclic
geometric-mean application must then retain the corresponding harmless
fixed-site dilution explicitly.

Place `q/2` macro cluster centres to the left of `e` and `q/2` to the
right, continuing the strict high cap.  Replace each centre by a sufficiently
small rational cluster `X_i` of size `p`.  Finitely many strict orientation
inequalities guarantee that every transversal together with `T` is
ordinary.  Select only the transversals whose coordinate word lies in
`mathcal C_(p,q,k)`.  They are distinct actual rank-`r+q` sources and
canonically peel at depth `q/2` to the same parent `T`.

Inside `e`, put the separated low cap `Z`.  Every compatible endpoint trace
uses at most two points of `Z`, so the same-rank baseline count remains

\[
 C_{e,r}\le1+|Z|(r-2)+\binom{|Z|}{2}\binom{r-2}{2}.       \tag{16}

\]

Fix a three-point face `W subseteq Z`; then `W union e` is nonconvex and
contains a fixed four-circuit.  Choose an internal `p_0 in T`.  In every
source, `p_0` is an exterior insertion into the carrier obtained by deleting
it, and its two tangent neighbours and their outer neighbours are the same
four points of `T`.  Thus the family retains exactly the common endpoint,
parent, interval face, bad trace, repair mark, and tangent state demanded by
the live atom.

The clusters may be projectively universal rather than convex.  Shrinking
an arbitrary rational order type into each macro neighbourhood preserves
all transversal sources and the common fixed tuple.  Hence the barrier does
not rely on cap/cup regularity inside a module.

## 5. Why the regression pays: the ambient one-gap bank

Let `H_i` be the nonempty ordinary face count of the induced order type on
`X_i`.  The selected MDS family is irrelevant to the ambient radial
container structure: all `p^q` transversals are geometrically available.
The detached radial one-gap theorem supplies an ordinary bank of size at
least

\[
 B\ge p^q\left(\prod_{i=1}^q{H_i\over p^3}\right)^{1/q}. \tag{17}

\]

Using

\[
                   \log H_i\ge(c_0-o(1))(\log p)^2,
                   \qquad c_0=1/8,                       \tag{18}

\]

gives

\[
 \log B\ge q\log p+c_0(\log p)^2-O(\log p)
          =(3/8-o(1))L^2.                                \tag{19}

\]

The bank is recoverable from the omitted macro gap and the two directional
cluster profiles.  It is an anchor/one-gap payment of the precise kind
allowed in the proposed rectangle-or-shield dichotomy.

Notice the distinction:

* the **selected** code family has no `Theta(L)` disjoint modules and its
  tangent rectangle gains only `2^{o(L^2)}`;
* the **ambient geometry** has `q` recoverable containers, whose local face
  complexes multiply through a one-gap bank and gain coefficient `1/8`.

Any general extraction theorem must use the latter information.  It cannot
be formulated solely in terms of the selected set family, its projection
entropies, or repeated tangent-state thinning.

## 6. Consequence for the proposed binary recursion

At one two-tangent split, let `A,B` be the left and right projection
supports of a selected family `E`.  After fixing the actual tangent state,
all `A times B` cross-combinations are ordinary, so

\[
                 V(P)\ge |A||B|,qquad
 \log{|A||B|\over|E|}\ge I_E(A;B).                       \tag{20}

\]

Equality in (20) holds when both projection laws are uniform, in particular
for the MDS family.  This exact rectangle is useful whenever its support
surplus has a fixed quadratic coefficient.  The MDS family has only the
subquadratic value (14), while its component correlations persist under
balanced restriction.
Therefore the binary entropy/product recursion has the honest dichotomy:

1. quadratic projection surplus gives an immediate coefficient jump by
   (20); or
2. high-rate anti-alignment may persist, and payment must come from ambient
   container/profile faces such as (17).

There is no third, purely combinatorial, conclusion extracting a linear
number of modules from the selected histories.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_mds_module_extraction_barrier.py
```

The checker constructs the exact `[6,4,3]` Reed--Solomon code over
`mathbb F_17`, verifies its size, minimum distance, all half-projection
sizes, rectangle surplus, and the module bound.  It also constructs a
small rational high-cap realization of an `[4,3,2]` code over
`mathbb F_5`, checks all `125` selected sources, the common parent,
nonconvex common `W`, and fixed tangent mark, and audits the coefficient
arithmetic in (11)--(19).
