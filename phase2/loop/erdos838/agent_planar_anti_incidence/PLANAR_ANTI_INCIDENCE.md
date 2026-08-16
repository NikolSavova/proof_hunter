# Erdős 838: a planar anti-incidence theorem, and the exact history-reuse gate

**Verdict.**  A finite-projective-plane support cannot occur inside an
actual exterior-repair pocket without producing almost one ordinary convex
face per repair record.  The reason is genuinely planar: after a retained
core and its two root tangents are fixed, blocker--hidden-ear incidence is a
two-dimensional orthant relation.  A bounded-codegree orthant graph has only
near-linear edge mass.

This does **not** by itself close the component-surplus branch.  Immediate
repair records already satisfy the much weaker trivial bound `m <= n V`,
and the projective-plane obstruction in
`COMPONENT_SURPLUS_PAIR_TELESCOPE_BARRIER.md` concerns a composite history.
The theorem below identifies exactly what a stretchable tensor simulation
would have to do: it must reuse the same completed ordinary face under
`q^h = 2^{Theta(r^2)}` different outer-prefix/reservoir descriptions.
Ruling out that quadratic reuse is precisely the still-missing stacked-
reservoir/tag-absorption lemma.  Merely recovering the tangent-cell
identifier is not enough; Section 4 gives an exact star-partition audit.

## 1. Hidden ears are orthants

Put

\[
                  u=(-1,0),\qquad v=(1,0)
\]

and, for a point `z=(x,y)` in the upper wedge, put

\[
       \ell(z)={x+1\over y},\qquad r(z)={1-x\over y}.       \tag{1}
\]

The dominance calculation in `INSERTION_CHAIN_UNIVERSALITY.md` says

\[
 z\in\operatorname{conv}\{u,v,p\}
 \quad\Longleftrightarrow\quad
 \ell(z)\ge\ell(p),\quad r(z)\ge r(p).                    \tag{2}
\]

Now fix a lower rooted convex chain `R` with root chord `uv`.  Let `I` be
an upper rooted chain and let `p` be an upper point such that `R+p` is in
convex position and its upper boundary is `u,p,v`.  Then

\[
 \operatorname{ext}(R\cup I\cup\{p\})=R\cup\{p\}
\]

if and only if every point of `I` lies in the triangle `uvp`.  Indeed, the
intersection of `conv(R+p)` with the upper closed half-plane of `uv` is
exactly that triangle.  By (2), if

\[
       L(I)=\min_{z\in I}\ell(z),\qquad
       Q(I)=\min_{z\in I}r(z),                               \tag{3}
\]

then the repair relation is exactly

\[
             p\sim I
 \quad\Longleftrightarrow\quad
       \ell(p)\le L(I),\qquad r(p)\le Q(I).                 \tag{4}
\]

Thus a blocker is a point in a two-dimensional order and an ear is a
southwest-orthant threshold.  This remains true for an arbitrary selected
subfamily of the repairs.

## 2. A bounded-codegree orthant theorem

> **Theorem 1 (orthant anti-incidence).**  Let `X` be `a` points with
> distinct first coordinates and let `Q` be `b` northeast orthants.  Join a
> point to an orthant when the point lies in it.  Suppose every two distinct
> orthants have at most `lambda` common point-neighbours, where
> `lambda >= 1`.  If `e` is the number of incidences, then
> \[
>   \boxed{
>   e\le (a+\lambda b)
>          \{\lceil\log_2 a\rceil+1\}.}                    \tag{5}
> \]

**Proof.**  Recursively split the points by their first-coordinate median.
At one node write `X=X_0 dotcup X_1`, with `X_1` the upper half in the first
coordinate.  An orthant whose first threshold lies at or before the cut is
called crossing.  Its neighbours in `X_1` form a suffix of the single order
of `X_1` by second coordinate.  At most one crossing orthant has more than
`lambda` such neighbours: two suffixes of size at least `lambda+1` share
their top `lambda+1` points.  Hence all incidences from crossing orthants to
`X_1` number at most

\[
                         \lambda |Q_{\rm cross}|+|X_1|.      \tag{6}
\]

Charge those incidences at the current node.  Pass a crossing orthant to
the `X_0` child and every other orthant to the `X_1` child.  Thus every
orthant follows one path, so at each depth the total orthant charge is at
most `lambda b`.  The point sets at one depth are disjoint, so the total
exceptional point charge is at most `a`.  There are at most
`ceil(log_2 a)` internal depths; the extra `+1` pays the leaves.  Summing
proves (5).  QED.

The `lambda=1` case forbids a projective plane at its natural density.  If
`N=q^2+q+1` points and `N` orthants had the point--line incidence relation
of `PG(2,q)`, then (5) would give

\[
 N(q+1)\le2N\{\lceil\log_2N\rceil+1\},                     \tag{7}
\]

which is false for all sufficiently large `q` (already for `q=31`).

## 3. The completed-face form

Use the tangent cells of ACP Theorem 13.  For a cell `c`, let

* `mathcal R_c` be its retained lower cores;
* `mathcal I_c` be its hidden upper chains;
* `P_c` be its singleton blockers; and
* `E_c subseteq mathcal R_c times P_c times mathcal I_c` be any selected
  exterior-repair triples.

For fixed `R`, let `G_(c,R)` be the blocker--ear graph cut out by `E_c`.
Suppose every two ears in this graph have at most `lambda` common blockers.
Equation (4) and Theorem 1 give, with
`D=ceil(log_2 n)+1`,

\[
 |E_{c,R}|\le\lambda D
       (|P_{c,R}|+|\mathcal I_{c,R}|).                       \tag{8}
\]

The tangent-rectangle theorem supplies every completion

\[
 \mathcal F_c=
 \{R\cup X:R\in\mathcal R_c,\ 
       X\in\mathcal I_c\cup\{\{p\}:p\in P_c\}\}.           \tag{9}
\]

These are ordinary convex faces.  Inside a directed root cell the union
recovers its lower and upper pieces.  The blocker singleton pool and the
ear pool can overlap only as sets of upper chains, so

\[
 |\mathcal R_c|(|P_c|+|\mathcal I_c|)\le2|\mathcal F_c|.    \tag{10}
\]

After summing (8) over `R` and then over cells, Theorem 13 says that a
convex face of rank at most `K` is counted by (9) at most `K(K-1)` times.
We obtain the planar anti-incidence bound

> **Theorem 2 (bounded-codegree repair supports).**
> If every selected repair has completed rank at most `K`, and every
> fixed-core blocker--ear graph has pair codegree at most `lambda`, then
> \[
> \boxed{
> |E|\le
> 2\lambda\{\lceil\log_2 n\rceil+1\}K(K-1)V(P).}            \tag{11}
> \]

In particular, if the target--ear repair support is injective-`C_4`-free,
then the hypothesis holds with `lambda=1`: for fixed `R`, two ears and two
common blockers would be exactly an injective repair rectangle.  Therefore
an actual `PG(2,q)` repair support with `m=N(q+1)` records exposes at least

\[
             {N(q+1)\over
              2(\lceil\log_2n\rceil+1)K(K-1)}               \tag{12}
\]

ordinary convex faces.  The abstract endpoint count `2N=m^{2/3+o(1)}` is
not geometrically attainable inside a genuine repair layer when `q` is
superpolynomial in `K log n`.

## 4. What happens under tensoring

The local theorem has a precise composite version, but its extra hypothesis
is load-bearing.  Let `mathscr S` be a collection of history slices.  In
slice `s`, suppose the first-divergence choices are represented by genuine
repair triples and satisfy the codegree hypothesis above.  Let
`mathcal F_(s,c)` be their completed face pools (9).  If every ordinary face
occurs in at most `B` of these *tagged completed-reservoir* pools, then the
same proof gives

\[
 \boxed{
 \sum_{s\in\mathscr S}|E_s|
 \le2\lambda D K(K-1)B V(P).}                               \tag{13}
\]

For `G_q^{tensor h}`, a coordinate-by-coordinate projective-plane
simulation has `h(Nd)^h` local edge occurrences, while its advertised face
pool has only `N^h` objects.  With `lambda=1`, (13) forces

\[
 B\ge {h d^h\over2DK(K-1)}
      ={q^h\over2^{O(h\log h)}}.                            \tag{14}
\]

At the critical scaling `log_2q=Theta(h)` and `r=Theta(h)`, this is

\[
                         B=2^{Theta(r^2)}.                   \tag{15}
\]

So a tensor simulation cannot hide inside the local geometry.  It must
reuse the same hybrid ordinary face under quadratically many outer-prefix
and local-reservoir states.  Conversely, (11) gives no bound on that reuse:
a recursive projection may forget an outer frame before reaching its hidden
component.
Theorem 20 recovers the current outward-successor prefix from the repaired
target, but a proof that every later hidden-ear completion still recovers
all earlier prefixes with `B=2^{o(r^2)}` is not presently available.

This is why (13), although exact, is not yet a proof of Erdős 838.  It turns
the vague request for a “planar property absent from projective planes”
into one sharp remaining assertion:

\[
 \boxed{\text{stacked prefix/reservoir reuse }B=2^{o(r^2)}.}\tag{16}
\]

The abstract tensor barrier proves that some assertion of this strength is
necessary.  The planar orthant theorem proves that it is sufficient to
eliminate projective-plane incidence at every genuine repair layer.

### Cell-ID recovery alone is exactly insufficient

Partition the edges of `PG(2,q)` into its `N` point-stars.  Every star is a
dominance graph (one left vertex and `d=q+1` right vertices), and its cell
identifier is exactly the retained point.  Thus the whole cell-ID sequence
in the tensor power is already recovered by the retained point word.
Nevertheless, conditional on that word there remain

\[
                              d^h=q^{h+o(h)}                 \tag{17}
\]

line words.  For an ordered pair of histories the missing factor is
`d^(2h)`.  The local tangent completion exposes the `d` right-reservoir
faces in each star, but a full proof must show that one choice from each of
the `h` reservoirs coexists in, and is recoverable from, the final two
ordinary faces.

Therefore a theorem saying only “the final face recovers every tangent-cell
ID” cannot close the proof: the star partition satisfies it and leaves the
full projective-plane deficit.  The correct hypothesis is the **stacked
compatibility** of Theorem 4 in `TAGGED_FULL_HISTORY_CARLESON.md`, or an
equivalent amortized theorem charging every reservoir word before its outer
frame is erased.

For comparison, `agent_root_followup/DOMINANCE_C4_SUPERSATURATION.md` proves
the stronger local analytic inequality

\[
 \operatorname{hom}(C_4,G)
 \ge {m^3\over2|L||R|(\lceil\log_2(|L|+|R|)\rceil+1)^3}.    \tag{18}
\]

Its Ferrers layer-cake and dyadic-tree proof was independently
cross-checked, and its exact verifier passes.  It gives the local `3/4`
conversion without a bounded-codegree assumption.  The star audit shows
why neither (18) nor recoverable cell IDs automatically tensor: the
unresolved object is the product of the completed reservoirs, not the local
rectangle count.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_planar_anti_incidence/verify_planar_anti_incidence.py
```

The verifier uses exact rational arithmetic to check (2), exhaustively
enumerates small orthant families and checks (5), audits projective-plane
parameters for prime orders, evaluates the exact tensor reuse lower bound
(14), and checks that the point-star cell IDs leave exactly `d^h`
conditional neighbor words.
