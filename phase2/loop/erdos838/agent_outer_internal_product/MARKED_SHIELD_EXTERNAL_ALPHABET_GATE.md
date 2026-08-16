# The 1+3 external-alphabet gate: exact product threshold and chronology audit

**Date:** 2026-08-15.  All logarithms are base two.  Put

\[
                         \alpha=\log_2(3/2)=0.5849625007\ldots .   \tag{1}
\]

## Verdict

The live marked-shield descent does retain the identity of an actual
ordinary face `F` and its mark `p`; it does **not** retain a geometric
product between the downset of `F` and the varying common-interval record.
This distinction is exact.

There is a clean conditional closure theorem.  If a base one-face routing
has normalized load `R`, every record has a disjoint `c`-label ordinary
repair face `C`, every base output coexists with every subset of `C`, and a
product output has global decoder load at most `L`, then the product routing
has normalized load at most

\[
                         \boxed{LR(3/2)^{-c}.}             \tag{2}
\]

Thus if

\[
 R=n^{\beta+o(1)},\qquad L=n^{\lambda+o(1)},\qquad
 c=(\gamma+o(1))\log n,                                  \tag{3}
\]

the precise exponent after repair is

\[
                         \beta+\lambda-\alpha\gamma.      \tag{4}
\]

Subpower congestion follows when `gamma>=(beta+lambda)/alpha`.

For the sharp conic `1+3` rectangle, every subset-valued routing has load
at least `n^(1-o(1))`.  Hence, even granting a fictitious full product and
subpower decoder, a necessary threshold is

\[
 c\ge\left({1\over\alpha}-o(1)\right)\log n
       = (1.709511\ldots-o(1))\log n.                    \tag{5}
\]

There is also a completely explicit sufficient branch.  Route first to the
full interval `W`; its load in the rectangle is `Theta(n^2)`.  If `W union C`
is convex and the product decoder has subpower load, then

\[
 c\ge\left({2\over\alpha}+o(1)\right)\log n
       =(3.419023\ldots+o(1))\log n                     \tag{6}
\]

closes that fibre.

Neither hypothesis is supplied by the present marked shield.  The best
currently established pocket reservoir coefficient `a=1/4` guarantees a
rank only `(a-o(1))log n`, far below (5).  More decisively, the hard branch
has no coexistence: the common marked-alphabet regression has

\[
                  (Q\cup\{p\})\cup F\quad\hbox{nonconvex}
                  \qquad(F\ne\{p\}).                    \tag{7}
\]

Using the downset of `F` as a separate additive bank does not fix this.  In
the conic rectangle it would need

\[
 c\ge\left(6+{2\over\alpha}-o(1)\right)\log n
       =(9.419023\ldots-o(1))\log n                     \tag{8}
\]

to carry the whole record demand by itself.  Moreover a proper subface of
`F` erases `F`, and the marked Carleson theorem gives no bound on how many
different shields contain that subface.

Accordingly this report does **not** close EIC'.  It identifies the exact
missing statement:

> **Shield-faithful coexistence/decoder.**  From a common-`W`, fixed
> `1+3`-trace occurrence with marked state `(p,F,tau)`, construct ordinary
> faces `Phi(O,S)` for enough base outputs `O` and `S subset F-{p}` such
> that `Phi` has the product half-weight, remains convex, and recovers
> `(F,O,S)` with `n^{o(1)}` aggregate load.

The current descent retains `(p,F,tau)` only as named state.  It supplies
neither `Phi` nor an equivalent globally recoverable alphabet.

The exact verifier is

```text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_marked_shield_external_alphabet_gate.py
```

It checks the product-routing identity, all numerical thresholds, the
rank-extraction scale, a rational conic common-cage regression, and the
actual marked common-alphabet noncoexistence construction.

## 1. Exact external-product routing theorem

Give every ordinary face `O` half-Gibbs capacity

\[
                             \pi(O)={2^{-|O|}\over F(P)}.           \tag{9}
\]

Let weighted records first be fractionally routed to ordinary base outputs.
Write `a_(sigma,O)` for the total mass sent to `O` by records in state
`sigma`, and suppose

\[
                    \sum_\sigma a_{\sigma,O}\le R\pi(O)           \tag{10}
\]

for every `O`.  State `sigma` has a disjoint ordinary face `C_sigma` of
rank at least `c`.  Fix a `c`-subset if it is larger.  Assume that

\[
                         \Phi(\sigma,O,S)=O\cup S                 \tag{11}
\]

is ordinary for every `S subset C_sigma`, and every ordinary output has at
most `L` preimages `(sigma,O,S)`.

> **Theorem 1 (external alphabet multiplication).**  Under (9)--(11), the
> records have a fractional one-face routing of normalized load at most
> (2).

**Proof.**  Put `E=(3/2)^c`.  Split the mass `a_(sigma,O)` among all
`S subset C_sigma` in proportions

\[
                              {2^{-|S|}\over E}.                    \tag{12}
\]

The proportions sum to one.  Disjointness gives

\[
                \pi(O\cup S)=\pi(O)2^{-|S|}.                       \tag{13}
\]

For one decoded triple, its contribution divided by (13) is
`a_(sigma,O)/(E pi(O))<=R/E`.  At most `L` triples produce the same
ordinary output, proving (2).  QED.

The theorem remains true with `c` replaced by

\[
               c_{\rm free}=\min_{\sigma,O}|C_\sigma-O|,          \tag{14}
\]

provided those free labels give the same coexistence and decoder.  This is
the relevant parameter for a marked shield because `p` is already present
in the repaired star.

Equations (3)--(4) follow immediately from (2).  Notice that rank
`Theta(log n)` by itself says nothing: its constant relative to `log n`
and the decoder exponent are load-bearing.

## 2. Sharp thresholds on the conic rectangle

Use the notation of `VISIBLE_HIDDEN_INTERVAL_KRAFT_BARRIER.md`: two
optional conic clouds have size `3s`, their selected layers have rank `s`,
and `l=r=2^s`.  Then

\[
 n=2^{s+1}+O(s).                                         \tag{15}
\]

That report proves that every routing to an arbitrary ordinary subface of
the record has load

\[
                             \Omega(2^s/s)=n^{1-o(1)}.    \tag{16}
\]

Allowing all subsets of `c` new labels can multiply total half-weight by at
most `(3/2)^c`.  Therefore (16) implies (5), even if every formally possible
union is declared ordinary and its decomposition is free.  This is a
necessary information/capacity threshold, independent of the particular
four projection banks.

For a positive conditional branch, output the full `W`.  Every record has
demand `pi(W)/4`, and one `W` is shared by exactly `lr` endpoint pairs, so
its normalized load is exactly

\[
                              R_W={lr\over4}=\Theta(n^2).            \tag{17}
\]

If `W` has a product with a disjoint external alphabet and the product
decoder has load `L=n^{o(1)}`, Theorem 1 and (17) prove (6).

Without coexistence, the downset of one common external face is only an
additive capacity `(3/2)^c/F(P)`.  The rectangle's total record demand,
with the common factor `1/F(P)` removed, is

\[
 \Theta\left({lr(3/2)^{6s}\over s}\right)
       =2^{(6\alpha+2+o(1))s}.                           \tag{18}
\]

For this independent downset alone to absorb (18) with subpower load one
needs `alpha c>=(6alpha+2-o(1))s`, which is exactly (8).  Adding it to the
record-subface capacity does not change the conclusion unless it reaches
this scale: the latter is smaller than (18) by `Theta(2^s/s)`.

## 3. What the live marked shield actually retains

The three relevant theorems fit together without a bookkeeping loss, but
they do not imply Theorem 1's geometric hypotheses.

1. `GLOBAL_MARKED_POCKET_RELEASE.md` proves that a guard `G` releases the
   whole pocket bank exactly when it hits every split circuit.  Its output
   `(A-G) union F` really coexists and recovers `F`.  But the live hard
   branch is the complementary one: for almost every weighted source,
   every such guard has `Omega(log n)` vertices.  The small-guard release
   product has already exited before the residual `1+3` fibre.

2. `RADIAL_KL_TO_HALL_BRIDGE.md` expands the common-`W` load into genuine
   histories and then localizes a dense family to one actual state
   `(p,F,tau)`.  Thus the identity of `F` is not forgotten.  Fixing the bin,
   however, turns `F` into side information; none of its labels is asserted
   to lie in the tangent-guarded output or to coexist with `W`.

3. `MARKED_NESTED_SHIELD_CARLESON.md` and
   `TANGENT_MARKED_SHIELD_DESCENT.md` show that this is a real distinction.
   Their common-alphabet construction has exact overlap `M` for every
   marked face `(p,F)`, while every nontrivial star--shield union is
   nonconvex.  The tangent output recovers `p`, the insertion edge, and the
   local cell, but not the labels of `F`; `F` remains a fixed bin name.

Consequently the marked shield survives **combinatorially** but is erased
**geometrically** from the one-face output.  Calling its `c` labels an
external alphabet silently assumes precisely the missing coexistence map
(11).

## 4. The guaranteed alphabet is below the necessary scale

There is a general rank extraction, but its coefficient is too small here.
Let a shield ground set have `d` labels and at least

\[
                       H\ge2^{(a-o(1))(\log d)^2}          \tag{19}
\]

ordinary faces.  For every fixed `gamma<a`,

\[
 \sum_{i\le\gamma\log d}{d\choose i}
       \le d^{\gamma\log d+1}
       =2^{(\gamma+o(1))(\log d)^2}=o(H).                \tag{20}
\]

So the reservoir may be restricted, without losing its quadratic
coefficient, to faces of rank at least `(gamma-o(1))log d`.  Applying the
established `a=1/4` pocket bound and `d=n/polylog(n)` gives only

\[
                         c\ge(1/4-o(1))\log n.            \tag{21}
\]

Even under fictitious perfect coexistence this reduces load by only

\[
                         (3/2)^c\le n^{\alpha/4+o(1)}
                                  =n^{0.14624\ldots+o(1)},          \tag{22}
\]

whereas the conic barrier needs `n^{1-o(1)}`.  Rank binning therefore does
not bridge the gap.

More importantly, marked localization can concentrate on low-rank faces
unless (20) is imposed before the incidence pigeonhole.  The statement
`|F|<=b=Theta(log n)` used in the current descent is an upper bound, not a
lower bound, and supplies no external capacity at all by itself.

## 5. Common-cage and common-alphabet regressions

The obstruction survives both mandatory tests.

* **Conic common cage.**  Put an arbitrary rational convex `c`-gon strictly
  inside the triangle of three labels forced into every conic interval
  `W`.  It is an ordinary common marked face `F`, with a full downset of
  weight `(3/2)^c`, but `W union S` is nonconvex for every nonempty
  `S subset F`.  Thus arbitrary logarithmic rank does not imply one bit of
  coexistence.

* **Actual repair alphabet.**  The projectively universal radial repair
  construction has an actual common marked shield `(p,F)`, exact occurrence
  overlap equal to the number `M` of completions, and nonconvex
  `(Q union {p}) union F` for every `F ne {p}`.  This preserves the repair
  chronology and kills the inference from a named shield to a product
  alphabet.

Neither construction is an EIC' counterexample: both expose other ordinary
banks.  They prove only that the missing shield-faithful coexistence/decoder
cannot be obtained from rank, marked incidence, or common-state localization
alone.
