# Support redundancy in the varying-interval `1+3` fibre

**Date:** 2026-08-15.  All logarithms are base two, all point sets are in
general position, and the empty face is counted.

## Verdict

The high-support-redundancy branch of the varying-interval fibre has an
exact discharge, including endpoint multiplicity.  The low-redundancy
branch has an exact homogeneous-product and partial-transversal bank, but a
fixed rooted `1+3` trace does **not** promote that bank to a mixed
endpoint--interval product.

More precisely, let `Rcal` be a family of records `(e,W)`, where `W` is an
ordinary rank-`r` interval face and `e` is its endpoint pair.  After fixing
the circuit trace and circuit role, a random exact role-colouring followed
by cyclic-start/orientation and chain-mask pigeonholing retains a
`Gamma^{-1}` fraction of the records with

\[
          \Gamma\le 2^{r+1}r^{r+1}=2^{O(r\log r)}.        \tag{1}
\]

Let `E` be the distinct retained interval faces, written as words in
disjoint coordinate supports `X_1,...,X_r`, and put

\[
 M=|E|,\qquad P_0=\prod_i|X_i|,\qquad
 R=\log(P_0/M),\qquad N=\left|\bigcup_iX_i\right|.       \tag{2}
\]

If no interval face has more than `Delta` retained endpoint records, then
the induced support bank gives

\[
 \boxed{
 {V(P)\over |\mathcal R|}\ge {1\over\Gamma\Delta}
 \max\left\{1,{f(N)2^R\over P_0}\right\}.}              \tag{3}
\]

Since the supports are disjoint,

\[
 \boxed{
 \log{V(P)\over|\mathcal R|}
 \ge R+\log f(N)-r\log(N/r)-\log(\Gamma\Delta).}        \tag{4}
\]

The right side may of course be negative, in which case the first term in
the maximum in (3) remains the valid statement.  At the critical support
rank

\[
                  r=(1/4+o(1))\log N,                  \tag{5}
\]

quadratic redundancy `R>=rho r^2` pays the complete record family with
gain `2^{(1-o(1))R}`, provided `Delta` is polynomial in the ambient size
and `r=Theta(log n)`.  The endpoint and role taxes are then only
`O(r log r)=o(r^2)`.  Thus endpoint-pair reuse does not reopen the
high-redundancy branch.

In the complementary branch, the consecutive-sign retention theorem can
be applied **once an ordered/simple-chain certificate has been fixed**.
It retains

\[
                 M'\ge M2^{-A(r+R)}                    \tag{6}
\]

selected faces inside a product `Y_1 times ... times Y_r` every transversal
of which is ordinary.  Writing `y_i=|Y_i|`, this product supplies not just
the full transversals but the exact partial-transversal bank

\[
 \mathcal B(Y)=\{S:S\cap Y_i\text{ has size at most one for every }i\},
                                                                  \tag{7}
\]

with

\[
 |\mathcal B(Y)|=\prod_i(1+y_i),\qquad
 \sum_{S\in\mathcal B(Y)}2^{-|S|}=\prod_i(1+y_i/2).    \tag{8}
\]

Every member of (7) is ordinary by heredity.  The bank has a perfect
coordinate decoder.  If

\[
 P_Y=\prod_i y_i,\qquad R_Y=\log(P_Y/M'),              \tag{9}
\]

then its exact raw multiplier over the retained selected family is

\[
 { |\mathcal B(Y)|\over M'}
       =2^{R_Y}\prod_i(1+1/y_i),                       \tag{10}
\]

and, for equal rank-`r` literal depth-zero records, its half-Gibbs capacity
relative to `Delta M'` endpoint records is

\[
 {\pi(\mathcal B(Y))\over
       \Delta M'2^{-r}/(4F)}
       ={4\,2^{R_Y}\over\Delta}\prod_i(1+2/y_i).       \tag{11}
\]

Here `F` is the global face half-weight and cancels exactly.  Equations
(10)--(11) are the strongest automatic one-face payment furnished by the
retained singleton product.  In particular, when the coordinate supports
are large, both products can be subpower even though `r=Theta(log n)`.

The rooted `1+3` trace adds only a negative assertion: one endpoint cannot
coexist with one particular triple.  It does not imply any larger positive
mixed bank.  Universally one has the rank-at-most-three bank

\[
 \{e:e\in G\}\ \cup\
 \{e\cup\{x\}:e\in G,\ x\in Q\},                     \tag{12}
\]

of size `|G|(1+|Q|)`, because all sets of rank at most three are ordinary;
the endpoint pair is recovered from every output.  But (12) is additive in
the interval support and does not multiply a quadratic-entropy family of
`W`'s.  The conic `1+3` rectangle shows that no promotion based only on the
fixed trace and record subfaces is possible.

The conic regression itself is nevertheless **paid globally** after the
support union is audited.  Restrict each of its `2s` optional rank layers
to one choice from a three-point block.  Then

\[
 R=0,\qquad M=3^{2s}=9^s,\qquad
 \Delta=|L||R|=4^s,\qquad |\mathcal R|=36^s.           \tag{13}
\]

The partial-transversal bank (7) has only

\[
                       2^7 4^{2s}=128\,16^s            \tag{14}
\]

faces and does not pay (13).  However all `6s+7` interval-support labels
lie on one convex conic.  Their complete Boolean downset is ordinary and
has

\[
        2^{6s+7}=128\,64^s
          =128(16/9)^s|\mathcal R|                    \tag{15}
\]

faces.  At the literal depth-zero weights, the record demand without the
common factor `1/F` is

\[
       |\mathcal R|,2^{-(2s+9)}={9^s\over512},         \tag{16}
\]

whereas the Boolean support bank has half-weight

\[
       (3/2)^{6s+7}
       =512(3/2)^7(81/64)^s\,{9^s\over512}.             \tag{17}
\]

The original complete-middle-layer conic caused `Omega(n/log n)`
congestion for every record-subface decoder.  In each `s`-of-`3s` layer,
the `j`th order-statistic coordinate has `2s+1` possible labels.  Hence its
natural two-layer ordered-word encoding has

\[
 R_{\rm mid}=2s\log(2s+1)-2\log\binom{3s}{s}
             =\Theta(s\log s)=\Theta(r\log r),          \tag{17a}
\]

not zero.  Restricting it to the block product (13) makes `R=0`.  A
symmetric two-arc audit shows that the record-local obstruction does
survive this restriction.  Arrange the left endpoint so that it is
incompatible with every three lower-arc labels, and the right endpoint so
that it is incompatible with every three upper-arc labels.  Put

\[
                   P_2(m)=\sum_{i=0}^2\binom mi2^{-i}. \tag{17b}
\]

Every ordinary output contained in some record belongs to one of four
endpoint-presence classes.  Their total half-weight is at most

\[
\begin{aligned}
 Z_{\rm sub}\le{}&
 (3/2)^7(5/2)^{2s}\\
 &+{2^s\over2}(3/2)^2(5/2)^sP_2(3s+5)\\
 &+{2^s\over2}(3/2)^7(5/2)^sP_2(3s)\\
 &+{4^s\over4}(3/2)^2P_2(3s+5)P_2(3s).
                                                               \tag{17c}
\end{aligned}
\]

Indeed an endpoint-free record subface takes at most one label from every
three-point block.  A left-retaining face takes at most two labels from
the whole lower cloud; a right-retaining face takes at most two labels
from the upper cloud; and a two-endpoint face satisfies both restrictions.
The displayed expression deliberately overcounts all remaining choices.
Consequently

\[
 {9^s/512\over Z_{\rm sub}}
     =\Omega\left(s^{-4}(36/25)^s\right).              \tag{17d}
\]

Thus even arbitrary fractional routing to all ordinary record subfaces
has fixed-power normalized congestion.  Since
`n=2^{s+1}+O(s)`, its exponent is
`log_2(36/25)=0.526068...`, up to a polylogarithmic loss.  Nevertheless the `R=0`
restriction is not a counterexample to the support-union route: faces
using two or three labels from the same role block are external to every
selected record and supply the payment in (15)--(17).

This payment has no low-overlap decoder across the varying `W`'s.  A
partial transversal occupying `k` optional role blocks is contained in

\[
                         3^{2s-k}                      \tag{18}
\]

different interval faces and hence in `4^s3^{2s-k}` records.  The empty
face has load `36^s`.  The full Boolean bank in (15) succeeds precisely by
being charged **once to the merged support union**, not by assigning a
private copy to each interval face.  Across many different support unions,
or after summing many role/root fibres, a global Hall consolidation is
still required.

Accordingly this report closes the high-redundancy support branch and
removes the conic as a local low-redundancy counterexample.  It does not
close EIC'.  The exact surviving gate is:

> in a low-redundancy homogeneous interval product whose individual role
> supports do not themselves form a rich jointly ordinary downset, either
> produce a recoverable endpoint--support shield bank, or globally charge
> the family of support unions without spending `V(P)` once per union.

Projective singleton-reset universality shows why the phrase “role
supports form a rich jointly ordinary downset” cannot be inferred from
the singleton product alone.

## 1. Exact role-colouring and endpoint-degree reduction

Give each point of the interval support an independent uniform colour in
`[r]`.  Anchor the cyclic order using the already fixed circuit trace and
role.  A rank-`r` face receives the exact colour word `1,...,r` with
probability `r^{-r}`.  Therefore some colouring retains at least an
`r^{-r}` fraction of any nonnegative record weight.  If the start and
orientation have not already been anchored, pigeonholing them costs at
most `2r`, proving (1).  Fixing the upper/lower chain mask costs at most
`2^r`.  Together these losses give the explicit bound in (1).

Let `d(W)` be the number of retained endpoint records above `W`.  If
`d(W)<=Delta`, then the number `M` of distinct retained words obeys

\[
                M\ge {|\mathcal R|\over\Gamma\Delta}.  \tag{19}
\]

The same statement holds for nonnegative activity weights after dividing
all record weights by their maximum atom weight and defining `Delta` as
the largest normalized total weight above one `W`.  This is the exact
concentration alternative: a large `Delta` is a common-`W` fibre, while a
small `Delta` leaves many distinct interval faces.

Every `W in E` is an ordinary face contained in
`Q=union_i X_i`.  Hence

\[
                         V(P)\ge\max\{M,f(N)\}.          \tag{20}
\]

Since `M=P_0 2^{-R}`, division by (19) proves (3).  Disjointness of the
colour supports and AM--GM give `P_0<=(N/r)^r`, proving (4).

The role tax in (1) is harmless only on the coefficient scale:

\[
                   \log\Gamma=O(r\log r)=o(r^2).       \tag{21}
\]

For a fixed-power EIC estimate with `r=Theta(log n)`, it is generally
superpolynomial in `n`; one cannot call it `n^{o(1)}`.  A sharper canonical
role encoder would be needed for a fixed-power conclusion from the
low-redundancy branch.

## 2. Scope of semialgebraic retention

The retention theorem applies when ordinary source words in the fixed
role state are certified by `O(r)` fixed-arity predicates of bounded
dependency: adjacent label order, consecutive chain turns, endpoint seam
turns, and the closing state.  Its total-correlation telescope then costs
`O(r+R)` and gives (6).

Random role-colouring by itself does not prove this ordered/simple-chain
implication for arbitrary interlaced supports.  If certifying convexity
requires all `Theta(r^3)` orientation triples, the consecutive-sign
retention theorem cannot be quoted with the loss in (6).  In the live
radial or interval-chain slice the ordered certificate must therefore be
retained as an explicit hypothesis/state.  This is the same qualification
already present in `HIGH_REDUNDANCY_SUPPORT_BANK.md`.

Once every full transversal of `prod_iY_i` is ordinary, (7)--(8) need no
further geometry.  Every partial transversal extends to a full one, and
is ordinary by heredity.  Intersections with the disjoint `Y_i` recover
the partial word, proving the perfect decoder.  Equations (10) and (11)
follow by factoring the count and half-weight polynomials coordinatewise.

## 3. Why the fixed `1+3` trace is not a positive product theorem

For one fixed trace `A={a,b,c}` and left role, the geometric content is
that one point of `A` lies inside the triangle formed by the endpoint and
the other two.  This statement remains true after arbitrary changes to
all coordinates outside `A`.  Hence it places no positive compatibility
condition between the endpoint and those other coordinate supports.

The visible/hidden conic construction makes the independence literal.
The left endpoint plus any three lower-arc labels is bad, and symmetrically
the right endpoint plus any three upper-arc labels is bad, while all
optional upper and lower choices form ordinary interval faces.  For the
complete middle layers, the earlier exact capacity audit rules out all
one-face outputs contained in a record.  In the natural order-statistic
word encoding those middle layers have `R=Theta(r log r)`.  Restricting
them to one point in each three-point block makes a genuine `R=0` product
without changing either endpoint obstruction.  The four-case count
(17c)--(17d) proves the corresponding all-record-subface congestion
directly.

The symmetric construction scales.  Choose two disjoint compact rational
parameter intervals on a nondegenerate conic.  Put the left endpoint in a
region where its secant slope along the lower interval is strictly
monotone, and the right endpoint in the reflected region for the upper
interval.  The ray-and-chord argument then puts the middle of every ordered
arc triple strictly inside the triangle formed by the endpoint and the two
outer labels.  All inequalities are open, so arbitrarily many rational
arc labels and rational general-position endpoint clusters may be chosen.
This is the same strict nesting argument used in the scalable parabola
`1+3` regression, applied independently at the two ends.

What changes is the global support audit.  The conic makes every subset
of the support ordinary, including subsets taking several points from one
role block.  Those are the external outputs absent from every selected
record.  Equations (15)--(17) show that they pay both raw record count and
literal half-Gibbs demand.

This distinction is load-bearing:

* **complete-middle-layer record-local routing:** has fixed-power
  congestion;
* **the explicit `R=0` restriction:** also has fixed-power record-local
  congestion by (17d), but is globally paid by the external support bank;
* **one merged support union:** has enough total ordinary faces;
* **many support unions:** unresolved unless their banks have bounded
  aggregate overlap or a canonical global charge.

Thus the conic is simultaneously a sharp kill of a local decoder and a
positive example for the support-union bank.

## 4. Coefficient audit

Assume `r=Theta(log n)`, `Delta<=n^C`, and the retained record family has
quadratic logarithmic mass.  Then `log Delta=O(r)` and (21) is
`o(r^2)`.

* If `R>=rho r^2` and (5) holds, (4) gives a relative gain
  `(rho-o(1))r^2`.
* If `R=o(r^2)` and the ordered certificate is available, (6) preserves
  the leading quadratic coefficient.  Equations (10)--(11) may add a
  genuine gain when many `y_i` are small, but give no uniform fixed
  coefficient when the `y_i` are large.
* The universal endpoint bank (12) contributes only `O(log n)` bits over
  the endpoint graph and cannot by itself improve a quadratic coefficient.

Therefore the redundancy split is complete as a **retention/support
reduction**, not as a coefficient jump.  The missing low-redundancy
geometry is exactly a multi-label role-support bank or a globally
recoverable endpoint shield.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_support_redundancy_one_three_fibre.py
```

The verifier checks the role-colouring expectation, endpoint-degree form
of the support inequality, the raw and half-weight partial-transversal
identities, and the exact `R=0` three-label-block conic arithmetic,
including its exponentially large varying-`W` overlap.
