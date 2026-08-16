# Two-record/two-face uncrossing: a product-cell theorem and the remaining fan gate

**Date:** 2026-08-14.  All point sets are planar and in general position.
All logarithms are base two.

## 1. Verdict

The elementary proposed repair is false: if an exterior point `p` hides a
consecutive ear `I` of a convex polygon, `I union {p}` need not be in convex
position.  There is a nine-point rational parabola example in which the
middle of a three-vertex hidden ear lies strictly inside the triangle formed
by `p` and the two ear endpoints.

There is nevertheless an exact two-record theorem for the principal hard
equality case.  In a complete product repair cell with a linear hidden ear,
two endpoint microblocks can encode the two blocker labels.  One convex face
stores the first source word; a second, two-ended convex face stores the
second retained/hidden word and both blockers.  If the endpoint blocks and
the blocker cloud all have size `M`, the decoder fibre is at most four:

```text
|G|^2 <= 4 V(P)^2.                              (1)
```

The retained cores may vary arbitrarily.  For unequal endpoint block sizes
`q_1,q_b` and blocker-cloud size `y`, the exact loss is

```text
K = ceil(q_1 q_b y^2/(s(q_1)s(q_b))),
s(q)=1+q+binom(q,2),                              (2)
|G|^2 <= K V(P)^2.                               (3)
```

Thus the loss is `2^o(r)` whenever

```text
2 log y <= log q_1+log q_b+o(r).                 (4)
```

This proves the desired two-record scale for every full product grid whose
two active tangent endpoint cells have the face pool (9).  In particular it
applies to the fixed-outer-cell construction of ACP Proposition 26 after
choosing the first and last *internal* variable blocks and deleting the two
fixed outer guards from the coded face.  It does **not** say that an arbitrary
pair of hidden blocks automatically has (9).  It also identifies the exact
recursive alternative: if (4) fails, the blocker law has a linear entropy
surplus over the two endpoint reservoirs and must be retained as a child
rather than forgotten.

What remains unproved is the passage from a DRC complete fan of arbitrary
linear ears to such a two-ended product coordinate.  A fan gives many
interchangeable whole ears, but it does not canonically supply two endpoint
alphabets with the capacity in (4).  No realizable quadratic-entropy family
defeating all descendant endpoint coordinates was found.

## 2. Exact counterexample to `I+p` convex

Let

```text
A={(x,x^2):x=-4,-3,...,4},        p=(1/10,-3).    (5)
```

The nine points of `A` are in convex position.  Exact hull computation gives

```text
I={(-1,1),(0,0),(1,1)},
ext(A+p)=(A-I)+p.                                  (6)
```

The ten-point set is in general position: the line through
`(a,a^2),(b,b^2)` is

```text
y=(a+b)x-ab.
```

At `p`, collinearity would say

```text
-3=(a+b)/10-ab,
```

which fails for the finitely many distinct integers `a,b in [-4,4]`; the
verifier checks all triples exactly.

But `(0,0)` lies strictly inside

```text
conv{(-1,1),(1,1),(1/10,-3)}.                    (7)
```

For example, the two lower sides of this triangle meet the vertical line
`x=0` below zero, while its upper side has height one.  Hence
`I union {p}` has only three extreme points and is not a convex face.

The example scales.  Put `q_j=(j,j^2)`, take a deep point just off the
vertical axis, and fix two selected ear endpoints `q_-h,q_h`.  Every chosen
intermediate parabola point lies strictly inside the triangle cut out by
those endpoints and the deep point.  Replacing each intermediate
macrovertex by a small cluster produces linear-size, product-entropy ears
for which the blocker-plus-whole-ear shortcut still fails.  This is a
one-step decoder obstruction, not a counterexample to (3): the descendant
two-ended faces in those clusters are precisely the capacity used below.

There is a corrected local decomposition worth recording.

> **Lemma 1 (blocker--ear hull peel).**  For an exterior repair
> 
> ```text
> A=R union I,              ext(A+p)=R union {p},
> ```
> 
> put
> 
> ```text
> H=ext(I+p),               J=I-H.
> ```
> 
> Then `H` and `R union J` are disjoint convex faces, their ranks sum to
> `r+1`, `p in H`, and the marked pair `(H,R union J,p)` recovers the repair
> record.

**Proof.**  The set `H` is convex by definition.  The other set is a subset
of the convex source `A`, hence is convex.  Since `H-p subset I` and
`J=I-H`, the two faces are disjoint and their union is `A+p`, so their ranks
sum to `r+1`.  From their union and the marked point recover
`A=(H union R union J)-p`; taking `ext(A+p)` then recovers `R+p`, and hence
`R` and `I`.  `square`

Lemma 1 absorbs the blocker into an ordinary face without losing rank, but
still uses two faces for one record.  The theorem below is the nontrivial
tensorization that uses only two faces for two records.

## 3. The two-ended product-cell interface

Let `mathcal R` be any finite family of retained convex cores.  Let

```text
Q_1,...,Q_b                    (b>=2)
```

be disjoint ordered hidden microblocks, with `q_i=|Q_i|`, and let `Y` be a
disjoint blocker cloud of size `y`.  Assume the following two planar facts.

1. For every `R in mathcal R` and every transversal
   `x_i in Q_i`, the source

   ```text
   R union {x_1,...,x_b}                              (8)
   ```

   is a convex face; every `p in Y` is an outward repair blocker for it.
2. For every `R in mathcal R`, every
   `E_1 subset Q_1,E_b subset Q_b` with
   `|E_1|,|E_b|<=2`, and every choice of one point from each middle block,

   ```text
   R union E_1 union {x_2,...,x_(b-1)} union E_b       (9)
   ```

   is a convex face.

Condition 2 is the full two-ended endpoint pool.  It is automatic in the
standard vertical lens product when `Q_1,Q_b` are the active boundary blocks
and the fixed guards outside them are omitted from the coded face.  This is
the descendant pool used by the internal first/last variable blocks in ACP
Proposition 26.  It is not automatic for two arbitrary internal blocks while
both of their neighbouring guards are retained.  Notice that `mathcal R`
need not be a product and need not have any decomposition, but its coexistence
with the endpoint pool remains an explicit hypothesis.

The full repair family is

```text
mathcal G=mathcal R times Q_1 times ... times Q_b times Y.      (10)
```

Write

```text
s(q)=sum_(j=0)^2 binom(q,j)=1+q+binom(q,2).        (11)
```

> **Theorem 2 (two-record/two-face product uncrossing).**  Under (8)--(10),
> 
> ```text
> |mathcal G|^2 <= K V(P)^2,
> K=ceil(q_1 q_b y^2/(s(q_1)s(q_b))).              (12)
> ```
> 
> In particular, if `q_1=q_b=y=M`, then `K<=4`.

**Proof.**  Let `mathcal A` be the source-face family (8), and let
`mathcal D` be the two-ended family (9).  Distinct block labels recover all
coordinates, so

```text
|mathcal A|=|mathcal R| product_i q_i,             (13)
|mathcal D|=|mathcal R|s(q_1)s(q_b)
                    product_(2<=i<=b-1)q_i.        (14)
```

Take two records

```text
g=(R,x_1,...,x_b,p),
h=(R',x'_1,...,x'_b,p').                           (15)
```

The first output face is simply the source of `g`; it records
`R,x_1,...,x_b` but deliberately forgets `p`.

For the second output, retain `R'` and the middle coordinates
`x'_2,...,x'_(b-1)`.  Encode the four remaining symbols

```text
(x'_1,x'_b,p,p') in
2^(Q_1)_(<=2) times 2^(Q_b)_(<=2).                (16)
```

The domain of this code has size `q_1 q_b y^2` and the codomain has size
`s(q_1)s(q_b)`.  Enumerating both finite sets gives a map of maximum fibre

```text
K=ceil(q_1 q_b y^2/(s(q_1)s(q_b))).               (17)
```

Use the two subsets supplied by the code as `E_1,E_b` in (9).  The result is
a convex face in `mathcal D`.  Given the two output faces, all coordinates
outside (16) are recovered uniquely, and (17) leaves at most `K` choices for
the four coded symbols.  Hence

```text
|mathcal G|^2 <= K |mathcal A||mathcal D|
              <= K V(P)^2.                        (18)
```

If all three relevant sizes equal `M`, then

```text
M^4/s(M)^2<4,
```

so `K<=4`.  `square`

The encoding is a genuine uncrossing: one record supplies the ordinary
source face, while the other record supplies the retained/middle word; the
two endpoint slots of the latter are doubled or deleted to store both
blocker identities.  The faces do not need to contain the blockers
themselves.  They are codewords in a fixed labelled endpoint reservoir,
which is sufficient for an injective counting argument.

There is a stronger symmetric form which is the correct interface for the
insertion-poset hierarchy.  It does not require the two endpoint reservoirs
to coexist in one face.

Choose two (not necessarily distinct) distinguished blocks `Q_j,Q_k` in
the product word.  Assume the following one-slot property separately for
each distinguished block: after omitting fixed cell guards, replacing the
one selected point in that block by an arbitrary subset of size at most two
always gives a convex face, while every other coordinate of the word is
retained.  No compatibility between `Q_j` and `Q_k` is assumed.

> **Theorem 2S (symmetric one-slot uncrossing).**  Under the preceding
> one-slot hypotheses,
>
> ```text
> |mathcal G|^2 <= K_(j,k) V(P)^2,
> K_(j,k)=ceil(q_j q_k y^2/(s(q_j)s(q_k))).          (18S)
> ```
>
> The formula remains valid for `j=k`.  In particular, one terminal block
> of size `M` in each output and a blocker cloud of size `M` give
> `K_(j,k)<=4`.

**Proof.**  For records `g,h`, retain every coordinate of `g` except its
`Q_j` symbol, and every coordinate of `h` except its `Q_k` symbol.  Encode

```text
(x_j(g),x_k(h),p_g,p_h)
 in 2^(Q_j)_(<=2) times 2^(Q_k)_(<=2).              (18T)
```

As in (17), a balanced finite code has maximum fibre `K_(j,k)`.  Insert
the first code subset into the `Q_j` slot of `g` and the second into the
`Q_k` slot of `h`.  The two resulting sets are convex by the two separate
one-slot hypotheses.  They recover every uncoded coordinate of both
records; the code has at most `K_(j,k)` preimages for the four remaining
symbols.  This proves (18S).  The argument never puts a `Q_j` label and a
`Q_k` label in the same output face.  `square`

Theorem 2S removes an unnecessary geometric demand from Theorem 2.  For
the two-record square route, two nonadjacent active edges are not needed:
each record may use its own terminal tangent cell, and both cells may even
be the same cell.  The only local obstruction is now that the alternatives
inside one cell form a long nesting chain rather than a large antichain.

## 4. Entropy interpretation and sharpness

Equation (12) gives

```text
log K <= [2log y-log q_1-log q_b+2]_+ +O(1).       (19)
```

Thus a super-subexponential fibre can occur in this cell only when the
blocker alphabet has a linear entropy advantage over the geometric mean of
the two endpoint alphabets.  That is exactly a component-density surplus:
the blocker law must be kept as a recursive child.  In the entropy-balanced
product cell, `log K=o(r)` and the requested square inequality follows.

The estimate is capacity-sharp up to rounding for a code that uses only the
source pool (8) and the two-ended pool (9): their product has exactly the
right number of coordinate slots, and the ratio in (17) is the unavoidable
domain/codomain ratio.

It also explains why the fixed-outer-cell product is not a counterexample.
With `q_i=y=M`, the raw source and target projections each miss a factor
`M`.  Pairing two records, however, creates two endpoint slots, each having
`Theta(M^2)` subset capacity.  Those four symbol slots recover the two
missing blockers at constant fibre.  Equivalently, the familiar full-span
two-ended count

```text
|mathcal R| binom(M,2)^2 M^(b-2)                 (20)
```

is the geometric reservoir behind the second output face.

## 5. Why a complete DRC fan is not yet a product coordinate

ACP Theorem 25 produces either a fixed component with almost all record
entropy or `t=Theta(r)` distinct ears sharing a large common target
neighborhood.  In the latter case every selected target repairs with every
selected whole ear.  This is a complete fan, but the ears can have variable
cores, variable ranks, and unrelated internal label supports.

Theorem 2 applies once two ordered endpoint alphabets can be found with

```text
log s(q_1)+log s(q_b)
 >= log q_1+log q_b+2log y-o(r).                  (21)
```

For a product word this is automatic.  For arbitrary ears, two endpoint
labels carry only `O(log n)=O(r)` bits total, whereas the ear family can
carry `Theta(r^2)` bits in its interior.  The parabolic example in Section 2
shows that adjoining the blocker to the entire ear does not turn that
interior entropy into one face.  Therefore neither “complete fan” nor
“blocker plus ear” supplies (21) without a recursive internal-coordinate
theorem.

The exact remaining statement is:

> A quadratic-entropy complete fan of prefix-correlated linear ears either
> contains an entropy-balanced two-ended product coordinate to which
> Theorem 2 applies, or its interior ear law has a density-surplus child
> whose retained tangent description has only `2^o(r)` global reuse.

This is narrower than HTR: the blocker factor and the full product equality
case are now discharged by an explicit two-face code.  The unresolved part
is a planar factorization/stability theorem for an arbitrary complete fan.

### 5.1 Planarity supplies pair-compatible endpoint antichains

The `<=2` endpoint hypothesis has an intrinsic planar source.  Let `B` be a
convex face and let `X` be a set of points such that `B+x` is in convex
position for every `x in X`.  Each `x` is inserted across one unique edge
`e_x` of the boundary polygon `B`: all old support edges except `e_x` remain
support edges of `B+x`.

Fix one boundary edge `e` and put `X_e={x:e_x=e}`.  Define

```text
x <=_e y       iff       x in conv(B union {y}).
```

> **Lemma 3 (endpoint insertion poset).**  The relation `<=_e` is a partial
> order.  For distinct `x,y in X_e`,
> 
> ```text
> B union {x,y} is in convex position
>       iff x,y are incomparable under <=_e.       (E1)
> ```
> 
> Consequently, if every chain in `X_e` has at most `h` elements, then
> `X_e` is the union of at most `h` classes in each of which every subset of
> size at most two is compatible with `B`.

**Proof.**  If `x<=_e y`, then

```text
conv(B+x) subset conv(B+y).
```

This proves transitivity.  If both containments hold, the two hulls are
equal.  Their vertex sets are respectively `B+x` and `B+y`, so `x=y`; this
proves antisymmetry.

Comparable points cannot both be extreme after they are adjoined, proving
one direction of (E1).  Conversely, every point of `X_e` satisfies the
inner support half-planes of all boundary edges of `B` other than `e`.
Those edges, and hence every old vertex of `B`, remain exposed after both
points are adjoined.  If `x,y` are incomparable, each lies outside the hull
of the other together with `B`, so both are exposed as well.  Thus all
points of `B+x+y` are extreme.  The last assertion is Mirsky's theorem: a
poset of height `h` is partitionable into `h` antichains.  `square`

There are at most `|B|` insertion edges.  Therefore, if no insertion cell
contains a nesting chain longer than `h`, the whole endpoint alphabet is a
union of at most

```text
|B|h <= rh                                           (E2)
```

pair-compatible classes.

Two insertion cells at nonadjacent boundary edges do not interact.  If
`X_e,X_f` are antichains and `e,f` have no common endpoint, then every set

```text
B union E union F,       E subset X_e, F subset X_f,
                         |E|,|F|<=2               (E3)
```

is convex: every old vertex remains incident with an unchanged support
edge, while the two local antichain hull replacements occur on disjoint
boundary intervals.  Thus
two antichains supplied by Lemma 3 give exactly the geometric pool (9).

> **Corollary 4 (endpoint antichain or nested-chain dichotomy).**  Suppose
> a tangent-factorized repair cell has two nonadjacent active endpoint edges,
> and the maximum nesting-chain lengths in their alternative sets are
> `h_L,h_R`.  The record family is covered by at most
> 
> ```text
> r^2h_Lh_R                                      (E4)
> ```
> 
> subcells satisfying the two-ended hypothesis (9).  Hence if
> `h_L,h_R=2^o(r)`, passing to a largest such subcell costs only `2^o(r)`;
> Theorem 2 gives the desired two-record inequality whenever its endpoint
> capacity is balanced.  Otherwise one endpoint contains a
> `2^Omega(r)` nested insertion chain, which is precisely the rooted
> one-cell recursion rather than an uncrossing spend.

This is a genuine planar regularization, not a scalar entropy assertion.
It rules out arbitrary pair-incompatibility at a variable endpoint: the
only obstruction is a long chain of nested hulls.  It does not manufacture
two nonadjacent endpoint edges when all variable ear entropy is trapped in
one cell (or in two adjacent cells); that is the nested/short-span branch
retained in HTR.

For the square route, Theorem 2S sharpens the last sentence: nonadjacency is
unnecessary because the two antichain reservoirs live in different output
faces.  Adjacent cells genuinely do *not* always coexist after deleting
their common guard.  Here is an exact counterexample to that tempting
shortcut.  In cyclic order put

```text
B={(-821887,-595397),(-738882,-762305),(365937,-1123009),
   (1057493,-478100),(1071435,-332802),(1105222,54013),
   (267072,1065040)}.
```

On the adjacent edges ending and starting at `v=(267072,1065040)`, put

```text
E={(913819,1914436),(1117441,1400409)},
F={(-2318987,3222280),(-1770368,2922150)}.           (E5)
```

The sets `B`, `B union E`, and `B union F` are convex, so each pair is an
endpoint antichain in its own cell.  All eleven points are in general
position.  Nevertheless

```text
(B-{v}) union E union F                              (E6)
```

is not convex: `(-1770368,2922150)` is nonextreme.  Thus a one-face
adjacent-cell concatenation is false even with the shared vertex deleted;
the symmetric two-face code is essential.

## 6. An exact dominance/reset dichotomy for a tangent-factorized fan

There is a clean recursive statement which explains how the first and last
variable ear coordinates should be selected.  It applies after the DRC fan
has been regularized into actual tangent-coordinate products.

Keep the product cell (10), suppose every source has rank `r`, and put

```text
rho=log|mathcal G|/(r+1).                         (22)
```

An active ear interval consists of consecutive blocks
`Q_j,...,Q_k`.  Deleting an endpoint coordinate means fixing one value in
that block and then suppressing it from the recursive record.  Because the
support is a full product, a value can be fixed at an exact cost `log q_j`
or `log q_k` bits.

> **Theorem 5 (balanced endpoints or density reset).**  Fix `eta>0`.  Starting
> from any active interval with at least two blocks, one of the following
> occurs after repeatedly inspecting its first and last blocks.
>
> 1. **Component surplus.**  An exposed endpoint block, or the blocker
>    cloud, has
>    
>    ```text
>    log q_i>rho+eta       or       log y>rho+eta. (23)
>    ```
>    
>    Its singleton faces have entropy density greater than `rho+eta`.
> 2. **Nested reset.**  An exposed endpoint satisfies
>    
>    ```text
>    log q_i<rho-eta.                              (24)
>    ```
>    
>    Fixing that coordinate and deleting its rank produces a child family
>    of density at least `rho+eta/r`.
> 3. **Two-face spend.**  The active interval has two endpoints satisfying
>    
>    ```text
>    rho-eta<=log q_j,log q_k<=rho+eta,
>    log y<=rho+eta,                               (25)
>    ```
>    
>    and, provided their two-ended pool has the convexity property (9),
>    
>    ```text
>    |mathcal G|^2 <= 2^(4eta+3)V(P)^2.            (26)
>    ```
> 4. The interval reaches one block, which is the already separated
>    singleton/short-ear child.

**Proof.**  If (23) occurs, the indicated labels are distinct singleton
faces, so their log-count per unit rank is greater than `rho+eta`.

If (24) occurs, fix any coordinate value (all fibres have equal size in the
full product) and delete that coordinate.  The new log-count and rank are

```text
log|mathcal G'|=rho(r+1)-log q_i,
rank parameter=r.
```

Therefore its density is at least

```text
{rho(r+1)-(rho-eta)}/r=rho+eta/r.                 (27)
```

This is the nested reset.  Continue until a surplus occurs, two balanced
endpoints remain, or only one block remains.

In the balanced case, Theorem 2 and `s(q)>=q^2/2` give

```text
log K
 <= [2log y-log q_j-log q_k+2]_+ +1
 <=4eta+3,                                        (28)
```

which is (26).  `square`

Taking `eta=o(r)` makes the spend loss `2^o(r)`.  The theorem uses the fixed
gap between coordinate entropy and rank density exactly: low boundary
coordinates are removed with a density gain, high ones are marginal
surpluses, and only balanced boundary coordinates survive to be used as the
two blocker-code reservoirs.

### Interface with the actual weighted DRC fan

For a prefix-correlated ear, the intrinsic coordinates are the successive
tangent-child choices encountered from the first hidden vertex to the last.
The “first and last variable coordinates” are the first and last nodes of
this word trie having more than one live successor.  If, after conditioning
on the intervening tangent state, the live support is Cartesian and the
endpoint double-occupancy faces are convex, Theorem 5 applies verbatim.

More generally the actual fan has nonuniform weights and its word support
need not be Cartesian.  The entropy chain rule still gives the same formal
trichotomy:

* conditional boundary entropy below `rho-eta` is fixed and deleted, giving
  the reset (27);
* conditional boundary entropy above `rho+eta` is the component-surplus
  branch of ACP Theorem 23--24;
* two balanced boundary laws have enough *information* to encode the two
  blockers.

The last bullet needs a planar support theorem, not another Shannon
inequality: it must turn the two balanced weighted laws into the
`<=2`-subset face pool (9) with only `2^o(r)` smoothing loss.  DRC Theorem 25
gives a complete fan of whole ears but does not prove this Cartesian tangent
factorization.  Thus Theorem 5 is an exact sufficient dominance/reset
theorem for the actual successor family once that single support property
is supplied; proving the support property is the remaining arbitrary-fan
gate.

## 7. Full-hierarchy audit: the local reset does not yet telescope

The endpoint-poset dichotomy is local.  It is important not to infer a
global `2^o(r)` theorem merely by repeating its nested branch.

Suppose a rank parameter `k+1` node has record density `rho_k` and an
endpoint coordinate of log-size `a_k<rho_k`.  Fixing that coordinate and
dropping one unit of rank gives exactly

```text
rho_(k-1)={rho_k(k+1)-a_k}/k
          =rho_k+(rho_k-a_k)/k.                 (H1)
```

This gain is real, but it does not bound the number of resets by `o(r)`.
For example, take initial `rho_r=r`, put

```text
a_k=r-sqrt(r)
```

for `r/2` consecutive product coordinates, and store the remaining entropy
in the retained core.  Formula (H1) permits all `r/2` deletions: the density
only rises from about `r` to about `r+sqrt(r)`.  This is well below the
ambient ceiling `log n=Theta(r)`.  Thus a hard quadratic-entropy node can
traverse `Theta(r)` low-endpoint levels.

Selecting one branch at every such level would lose

```text
sum_k a_k=Theta(r^2)                              (H2)
```

bits.  Even a binary nested choice at every level loses `Theta(r)` bits,
which is not `o(r)`.  The density increase in (H1) therefore controls the
leading quadratic coefficient but is insufficient for the requested
subexponential-in-r fibre.

The downclosure of one nesting cell does not repair this by itself.  A
chain of `q` insertion alternatives supplies its `q` singleton faces and
`binom(q,2)` two-label faces, but those faces are not automatically
compatible with the variable retained/hidden data at the other nesting
levels.  Summing `O(q^2)` new-tip faces level by level is additive, whereas
the record histories multiply.  This is the same exact phenomenon as the
planar thin closure rectangle in
`../agent_cyclic_stem_hw/LATTICE_RECTANGLE_BARRIER.md`.

There is, however, an exact weighted Kraft invariant for a *single
monotone nesting history*.  It shows that the number of levels is not the
obstruction.

Let `ell=ceil(log n)` and put `d_k=2^(ell-k)`.  A marked rank-`k` rotation
step is a convex target `T_e` of size `k` together with the fresh label
`a_e` inserted at that step.  Give it the marked downclosure

```text
D_e={F:F subset T_e, a_e in F},       |D_e|=2^(k-1). (H3)
```

All members of `D_e` are ordinary convex faces.

> **Lemma 6 (marked-downclosure Kraft bound).**  Let `mathcal E` be any
> weighted family of marked rotation steps of ranks
> `k>=ceil(ell/2)`, with nonnegative occurrence weights `w_e`.  If
>
> ```text
> max_F sum_(e:F in D_e) w_e <= mu,                 (H4)
> ```
>
> then
>
> ```text
> sum_e w_e d_(k(e)) <= 2 mu V(P).                  (H5)
> ```
>
> Along one monotone rotation chain whose inserted label at each step is
> absent from every earlier target, unit weights satisfy `mu=1`; hence a
> chain of arbitrary length costs only the constant factor two in (H5).

**Proof.**  Double-count the pairs `(e,F)` with `F in D_e`, using weights:

```text
sum_e w_e 2^(k(e)-1)
 =sum_F sum_(e:F in D_e)w_e <=mu V(P).              (H6)
```

For `k>=ceil(ell/2)`,

```text
d_k=2^(ell-k)<=2^k=2*2^(k-1),                      (H7)
```

so (H5) follows.  If `e<f` lie on one chain, the later fresh mark `a_f`
does not belong to `T_e`.  Every member of `D_f` contains `a_f`, so
`D_e` and `D_f` are disjoint.  Thus `mu=1`.  `square`

An often convenient recoverable version marks the inserted label only
implicitly.  If a fixed pair `(F,a)` with `a in F` arises below at most
`M` recursion histories, then an unmarked face `F` has multiplicity at most
`|F|M<=rM`; Lemma 6 gives total loss at most `2rM`.  This is the exact
`rM` decoder factor: `r` guesses the mark in the output face, and `M` is
the genuine history reuse.

The max-overlap hypothesis can be regularized without losing the tangent
edge.  This is the exact crossing/laminarity statement for variable bases.
Let a history `omega` carry a convex `k`-set `B_omega`, an addable point
`x_omega`, and its insertion edge `u_omega v_omega` on `B_omega`.  Fix
`0<=t<=k-2`.  Delete only sets

```text
D subset B_omega-{u_omega,v_omega},       |D|=t,   (H8)
```

and output `(B_omega-D)+x_omega`.  For a marked output `F` the two cyclic
neighbours of `x_omega` in `F` are exactly `u_omega,v_omega`; hence the
insertion edge is recovered even though the base varies.

For a weighted multiset of histories define

```text
lambda(x,S)=sum{w_omega:
  S=B_omega-D for some D satisfying (H8)},
Lambda=max_(x,S) lambda(x,S).                       (H9)
```

> **Theorem 7 (guard-retaining weighted shadow).**  The histories route
> integrally to the faces `(B_omega-D)+x_omega` with maximum fibre
>
> ```text
> K_t^guard=
> ceil((k-t+1)Lambda/binom(k-2,t)).                 (H10)
> ```
>
> If the mark is supplied separately, the factor `k-t+1` is omitted.
> Every heavy collision in (H10) fixes a common retained prefix `S`, a
> common inserted label `x`, and the same insertion edge, not merely an
> unstructured family of variable cores.

**Proof.**  Every history has exactly `binom(k-2,t)` allowed outputs.  From
an unmarked output, guess `x` in at most `k-t+1` ways; then `S=F-x`, and
the two neighbours of `x` recover the guarded edge.  The total compatible
history weight is at most `Lambda`.  The usual duplicated-Hall argument
gives (H10).  `square`

For `t=ceil(sqrt(k))`, retaining the two guards is asymptotically free:

```text
binom(k,t)/binom(k-2,t)
 =k(k-1)/((k-t)(k-t-1))=2^o(1).                   (H11)
```

With heavy threshold `2^(-k^(2/3))`, the number of possible heavy atoms is
at most

```text
2^(k^(2/3)+O(sqrt(k)log k))=2^o(k).                (H12)
```

Thus high inter-chain reuse is not arbitrary: after a subexponential state
split it is a same-edge, common-prefix recursion of residual rank
`ceil(sqrt(k))`.  Whenever the light branch means
`K_t^guard=2^o(r)`, (H10) is already the required face map.  Applying it
independently to the two records gives a map to `F(P)^2` of fibre
`(K_t^guard)^2=2^o(r)`.  Equivalently, Theorem 2S couples two separately
regularized terminal slots; no adjacent-cell face is needed.

There is one genuine geometric caveat in the heavy branch.  A later
rotation at a different edge can erase a vertex of the fixed prefix `S`,
so the Boolean prefix tensor is not automatically preserved.  Nonadjacent
edge changes are the two-ended spend of Lemma 3.  An adjacent change erodes
a boundary end of the protected prefix.  Such erosions have an exact root-
walk bound.

> **Lemma 8 (adjacent root walk).**  Let
> `P_i=ext(P_(i-1)+a_i)` be a monotone exterior-rotation history, and let
> `J_0` be a protected ordered boundary interval of `P_0`.  Suppose every
> step which changes the active insertion edge adjacently and damages the
> protected interval deletes a nonempty prefix or suffix of the current
> interval `J_(i-1)`; let `J_i` be what remains.  Then:
>
> 1. the deleted pieces are disjoint and there are at most `|J_0|` damaging
>    adjacent switches;
> 2. the complete sequence of left/right deletions and their positive
>    lengths has at most `3^|J_0|` possibilities;
> 3. no erased guard or exact used boundary edge can recur.

**Proof.**  Convex hulls increase by inclusion.  A point which ceases to be
extreme is interior to the new hull and remains interior forever.  Thus the
deleted intervals are disjoint and a used edge, which becomes an interior
chord, never returns.  Exterior visibility on a convex polygon is a
consecutive boundary interval; for an adjacent edge change its intersection
with the protected interval touches the corresponding end.  Hence the
current intervals are nested and each damaging step removes at least one
new label.  A transcript with `s` steps is a choice of `s` left/right bits
and a composition of total length at most `|J_0|` into `s` positive parts.
Summing gives

```text
sum_(s=0)^|J_0| 2^s binom(|J_0|,s)=3^|J_0|.        (H13)
```

This proves all assertions.  `square`

Lemma 8 closes the **transcript** cost for the weaker quadratic-coefficient
target: `3^r=2^O(r)=2^o(r^2)`.  The bound is global across a multirank path,
not `3^r` per level, because all deleted protected pieces are disjoint
subsets of the original rank-`r` boundary.  It does not by itself close the
global two-face charge: different outer cores can still reach the same
terminal pair of faces after carrying identical root-walk transcripts.
Theorem 7 reduces that remaining collision precisely to heavy common-prefix
atoms.  Proving that the two terminal faces recover the variable outer core,
or producing a quadratic-entropy family where they do not, is the residual
global step.

For the full-coefficient target, the outer-core collision can in fact be
removed by stopping at the first heavy guarded shadow.  The point is to use
the two **cross-sources** of a repair `C_4`, rather than a small terminal
component, as the bases to which Theorem 7 is applied.

Consider two retained components `T_i=(R_i,p_i)` and two ears `I_i`
forming a complete repair rectangle.  Its diagonal record pair is encoded
by the two convex cross-sources

```text
A_12=R_1 union I_2,       A_21=R_2 union I_1.       (H14)
```

Both have the full source rank, and together with `p_1,p_2` and the two
canonical split positions they recover the diagonal records.  The split
positions cost only `r^O(1)` possibilities.

> **Theorem 9 (heavy-prefix terminal-pair reuse, coefficient scale).**
> Let `Pi` be a family of ordered repair rectangles of source rank at most
> `r`.  Suppose that after one of `Z` canonical state tags, each rectangle
> supplies cross-sources `A_12,A_21` as in (H14) and convex prefixes
> `S_12 subset A_12,S_21 subset A_21` such that
>
> ```text
> |A_12-S_12|,|A_21-S_21|<=t.                       (H15)
> ```
>
> Then
>
> ```text
> |Pi| <= Z r^O(1) n^(2t+2) V(P)^2.                 (H16)
> ```
>
> Consequently, if `ell=ceil(log n)=Theta(r)`, `t=ceil(sqrt(r))`, and
> `log Z=o(r^2)`, then `|Pi|<=2^o(r^2)V(P)^2`.

**Proof.**  Map a rectangle to the two ordinary faces `(S_12,S_21)` and
its implicit canonical state tag.  Given these data, guess the at most `t`
missing labels of each cross-source in at most `n^(2t)` ways and guess the
two blockers in at most `n^2` ways.  The two boundary cut positions (and
orientations, if not fixed by the tag) have `r^O(1)` possibilities.  Now
(H14) recovers `R_1,I_2,R_2,I_1`, hence the diagonal records.  This proves
(H16).  Its logarithmic loss is

```text
log Z+O(log r)+(2t+2)ell=o(r^2).                    (H17)
```

`square`

Theorem 9 is the exact first-divergence bound across different outer cores:
if the output prefixes coincide, only the two `t`-label residuals and the
blockers can differ.  There is no additional multiplication by the number
of recursion levels or outer-core histories.  Combining it with the
component-surplus/typical-slice alternative and the `2^o(r^2)` weighted-
rectangle extraction of ACP Theorems 23--25 proves

```text
|mathcal G|^2 <= 2^o(r^2) V(P)^2                  (H18)
```

for the stable branch whenever the guarded shadow is taken on the two
full-rank cross-sources.  Light shadows close by Theorem 7; heavy shadows
close by Theorem 9; antichain/product cells close by Theorem 2S.  The
remaining interface to audit in the full ACP proof is geometric, not a
reuse count: the canonical tangent recursion must expose the guarded
shadow on (H14), rather than only on a lower-rank retained or hidden
component.

The distinction between goals is sharp.  The fibre in (H16) is
`2^Theta(r^(3/2))`, which is negligible relative to `r^2` but is not
`2^o(r)`.  Thus this closes global terminal-pair reuse for the coefficient
route, not the stronger capped Hall statement.

In fact there is an even simpler coefficient-scale decoder.  Once a repair
rectangle exists, its *full* cross-sources can be output directly; no
shadow or root-walk transcript is needed.

> **Theorem 10 (global cross-source rectangle decoder).**  Let `mathcal C_4`
> be any family of ordered repair rectangles
> `(T_1,T_2,I_1,I_2)`, where `T_i=(R_i,p_i)`, all four cross pairs are
> records of source rank at most `r`, and hence
>
> ```text
> A_12=R_1 union I_2,       A_21=R_2 union I_1       (H19)
> ```
>
> are convex faces.  Then
>
> ```text
> |mathcal C_4| <= n^2 2^(2r) V(P)^2.               (H20)
> ```

**Proof.**  Output `(A_12,A_21)`.  Given this pair, guess the two blockers
in at most `n^2` ways.  Guess the two set partitions

```text
A_12=R_1 disjoint_union I_2,
A_21=R_2 disjoint_union I_1                            (H21)
```

in at most `2^(|A_12|+|A_21|)<=2^(2r)` ways.  The four candidate records
are now forced, and checking the repair relations and the canonical order
discard invalid guesses.  Thus the map has the fibre in (H20).  `square`

When `log n=Theta(r)`, the loss in (H20) is `2^O(r)=2^o(r^2)`.
Consequently **different outer cores never cause a coefficient-scale
terminal-pair obstruction after a counted `C_4` has been extracted**.  The
guarded shadows, symmetric endpoint code, and root walk are required only
for the capped `2^o(r)` theorem or for producing the rectangle.  For the
coefficient route the sole remaining analytic conversion is to turn the
weighted `C_4` mass of ACP Theorem 23 (after its component-surplus and
typical/degree regularization) into at least
`|mathcal G|^2/2^o(r^2)` counted ordered rectangles.  The geometric decoder
and its global reuse are completely settled by (H20).

The same proof permits `Theta(r)` successive ranks and never multiplies
their local losses: it is a genuine telescope at the capped scale.  It
also pinpoints the only surviving failure.  In a recursion forest, the
same marked face can be reached through many different variable-core
histories.  Then the left side of (H4) counts those history occurrences,
not merely distinct geometric rotation edges, and `mu` can be exponential.
Neither the insertion-poset lemma nor (H1) bounds this **inter-chain reuse**.
The fixed-base chain has `mu=1`; any counterexample to the Kraft route must
therefore have exponentially many variable bases merging into common marked
downfaces.

Here is the precise sufficient invariant still missing.  A hierarchical
two-face decoder should carry two **open tangent slots**.  At a nested
endpoint step, two records in branches `x,y` place `x` into the first slot
and `y` into the second, so the branch labels are recorded in the eventual
faces rather than paid as a multiplicative code tag.  At an antichain step,
the two slots merge into the `<=2` endpoint reservoir of Theorem 2.  If the
two open faces remain convex through every ancestor and the terminal target
reuse is `2^o(r)`, then no product of the branch counts in (H2) is lost.

Neither Lemma 3 nor entropy-density conservation proves preservation of
those open slots: after a deep blocker code is inserted, an ancestor's
nested point can hide part of that code face.  The parabola example in
Section 2 is the four-point base case of this failure.  Consequently:

> **Hierarchy verdict.**  The product/antichain branch has the desired
> `2^o(r)` two-record decoder.  A chain may occupy `Theta(r)` successive
> ranks, but Lemma 6 pays every rank with constant marked loss (polynomial
> loss when the mark is implicit) as long as marked-face reuse across
> histories is subexponential.  A proof of the
> full square inequality still requires an open-slot tangent invariant (or
> a heavy-reuse recursion) which bounds that inter-chain multiplicity.
> Density gain alone does not do so; marked downclosures do telescope, and
> isolate the precise remaining obstruction.

This is not a counterexample to the numerical square inequality: known
multilevel product and ramp cells release cross-level two-ended faces.  It
is an exact audit of why the current local dichotomy cannot claim the full
hierarchical theorem.

## 8. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_all_interval_isoperimetry/verify_two_record_uncrossing.py
```

The script verifies the parabola counterexample with exact rational
determinants and convex hulls.  It also constructs balanced finite endpoint
codes, checks their exact maximum fibres against (17), audits (12) for
unequal and balanced product cells, and checks both the long-reset arithmetic
and the marked-downclosure Kraft inequality.
