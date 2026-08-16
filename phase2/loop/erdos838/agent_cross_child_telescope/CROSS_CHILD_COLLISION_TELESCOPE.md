# Cross-child collision telescope: the exact fixed-power threshold

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

The reuse left by the heavy-prefix and common-blocker descents has an exact
second-moment formulation.  A local bank need not have bounded overlap.
It is enough that **pairs of histories which collide at one bank face**
create a single ordinary mixed/shield face with fixed-power-better
aggregate multiplicity.

More precisely, let every source have `q` bank choices and let `d(F)` be
the number of sources whose bank contains the ordinary face `F`.  If the
off-diagonal collision events can be paid by ordinary faces with total load
at most `L`, then

\[
 q|S|\le {1+\sqrt{1+4L}\over2}\,V(P).                 \tag{1}
\]

For the central toggle bank, `q=2^s`.  Therefore, if every source carries
`D` selected records,

\[
 |E|\le {D\over2^s}{1+\sqrt{1+4L}\over2}\,V(P).       \tag{2}
\]

At `r=(alpha+o(1))log n`, `s=ceil(r/2)`, and
`D=n^(1-alpha+o(1))`, one has

\[
 2^s=D^{\alpha/(2(1-\alpha))+o(1)}.                   \tag{3}
\]

Consequently an aggregate collision load

\[
 L\le n^{o(1)}D^{2\lambda}                            \tag{4}
\]

gives the fixed saving

\[
 |E|\le n^{o(1)}D^{1-\varepsilon}V(P),\qquad
 \varepsilon={\alpha\over2(1-\alpha)}-\lambda.       \tag{5}
\]

In particular, at the seam `alpha=1/2`, **any**
`L<=D^(1-eta)n^o(1)` gives `epsilon=eta/2`.  This is the
precise meaning of the requested `d^epsilon` two-ended/shield gain.

The same theorem applies verbatim to the marked target downsets in the
common-blocker rotation child.  It removes the maximum-occurrence parameter
from that descent whenever collisions of two marked histories admit a
one-face mixed bank.

There is a second, more flexible certificate.  For every common-base cell
one may carry an outer/context face bank and an erased/internal face bank.
If their local product pays the square of the cell mass and their two
global overlaps have a fixed-power-better product, the recoverable-cell
Cauchy telescope gives exactly the same saving.  At the seam its sharp
condition is

\[
                         K L_A L_B\le D^{1-\eta}n^{o(1)}.     \tag{6a}
\]

This is weaker than forcing every collision into one face and is the
appropriate formulation for the retained-outer/erased-pocket recursion.

This report does not prove that geometric collision bank in the remaining
three-pocket/nested case.  It does prove three useful boundary facts.

1. A **pair** of recoverable output faces does not suffice; the collision
   square has to buy one ordinary face.
2. The canonical outputs `ext(M union M')` and `ext(A union A')` fail at
   the required power even on the complete quadratic shield.  Their fibres
   are of order `D^2` at the seam.
3. Pure fixed-edge chain geometry cannot prove the missing estimate: the
   tangent-coordinate map is projective, and one strict dominance chain
   can carry an arbitrary planar order type.  The remaining positive lemma
   must use the simultaneous hidden-child/source law, or descend with a
   protected tangent context.  It cannot use only the blocker chain.

Thus the exact live target is now the one-face inequality

\[
 \boxed{\sum_F d(F)(d(F)-1)\le n^{o(1)}D^{1-\eta}V(P)}       \tag{6}
\]

at `alpha=1/2` (with the exponent adjusted by (5) away from the seam),
or a contextual descent which preserves (6) across rank-halving children.

## 1. The collision-bank theorem

Let `X` be a finite set of histories and let `Y` be a set of ordinary
faces.  Let `G subset X times Y` be a bipartite incidence graph in which
every history has degree exactly `q`.  Put

\[
 N=q|X|,\qquad d(y)=|N_G(y)|,qquad R=|Y|\le V(P).             \tag{7}
\]

An off-diagonal collision is a triple `(y,x,x')` with distinct histories
`x,x'` both adjacent to `y`.  Ordered collisions are used, so their number
is

\[
 C=\sum_{y\in Y}d(y)(d(y)-1).                               \tag{8}
\]

> **Theorem 1 (one-face cross-child collision telescope).**  If the
> ordered collision multiset has a map to ordinary faces with maximum fibre
> `L`, then (1) holds.  More generally it is enough to know directly that
> `C<=LV(P)`.

**Proof.**  Cauchy--Schwarz and `R<=V(P)` give

\[
 C=\sum_y d(y)^2-N\ge {N^2\over V(P)}-N.                    \tag{9}
\]

The collision map gives `C<=LV(P)`.  Hence

\[
 N^2-NV(P)-LV(P)^2\le0.
\]

Solving this quadratic inequality gives (1).  QED.

The theorem is deliberately aggregate.  No child identifier is selected
or paid for.  Exponentially many cells are harmless if their collision
events share one global face bank with load `L`.

There is a robust fractional version.  Suppose a designated set of good
collision events has size at least `theta C-BN` and maps to ordinary faces
with load `L`.  Then

\[
 C\le {LV(P)+BN\over\theta}.                                \tag{10}
\]

Substituting (10) into (9) gives the corresponding quadratic bound.  Thus
constant-density nonadjacent-pocket splices are enough; the unmatched
events may cost only `o(1)` times the first moment.  What is not enough is
to identify a good pair of output faces for each collision: that only
bounds `C` by `O(V(P)^2)` and returns no one-face saving.

## 2. Toggle banks and exact constants

Use the notation of
`../agent_heavy_prefix_rotation/HEAVY_PREFIX_ROTATION_DESCENT.md`.  Every
rank-`r` source has a central decomposition

\[
 A=Q_A\mathbin{\dot\cup}R_A,\qquad |Q_A|=s,
\]

and its toggle bank is

\[
 \mathcal B(A)=\{R_A\cup B:B\subseteq Q_A\}.                \tag{11}
\]

This is precisely a left-regular incidence graph of degree `q=2^s` on the
ordinary face complex.  Applying Theorem 1 and multiplying the source count
by the selected degree `D` proves (2).

Write

\[
 \gamma={\log_D 2^s}={\alpha\over2(1-\alpha)}+o(1).          \tag{12}
\]

For `L>=1`,

\[
 {1+\sqrt{1+4L}\over2}\le1+\sqrt L.                        \tag{13}
\]

Equations (2), (4), and (12)--(13) give

\[
 |E|\le n^{o(1)}D^{1-\gamma+\lambda}V(P),                  \tag{14}
\]

which is (5).  At `alpha=1/2`, `gamma=1/2`.  Thus collision
load `D^(1-eta)` contributes only `D^((1-eta)/2)` after Cauchy and leaves
the saving `eta/2`.  This square-root loss is sharp for the abstract
incidence data.

When `alpha>2/3`, `gamma>1`; even collision load of order `D` leaves a
fixed saving.  The genuinely tight constant is at the seam.

## 3. Marked common-blocker downsets

The same accounting strengthens the marked-target theorem.  Let `Omega`
be any multiset of common-blocker histories.  If every history has a
rank-`k` repaired target containing its marked blocker `p`, join it to all
marked downfaces of that target.  Its bank degree is

\[
                         q=2^{k-1}.                           \tag{15}
\]

Repeated histories and identical repaired targets cause no problem: they
are distinct left vertices, and their reuse appears exactly in `d(F)`.
If two histories colliding at a marked downface generate a one-face mixed
bank with load `L`, Theorem 1 gives

\[
 |\Omega|\le2^{1-k}{1+\sqrt{1+4L}\over2}V(P).               \tag{16}
\]

This is the aggregate replacement for the pointwise maximum weight `M` in
the earlier inequality
`|Omega|<=k M 2^(1-k)V(P)`.  It shows exactly what the cross-child
geometry has to supply: not a bound on the heaviest blocker or target, but
a second-moment bank for histories which collide after the mark is kept.

## 4. Size-biased/KL form

Choose a uniformly random bank incidence and let `Y_*` be its face.  Then

\[
 \Pr(Y_*=y)={d(y)\over N}.                                  \tag{17}
\]

The collision moment is the chi-square numerator

\[
 \sum_y\Pr(Y_*=y)^2={N+C\over N^2}.                         \tag{18}
\]

Under the hypothesis `C<=LV`, the Renyi divergence from the uniform law
on the full face bank obeys

\[
 D_2(Y_*\|\operatorname{Unif}(\mathcal F(P)))
 \le\log\!\left({V(P)(N+LV(P))\over N^2}\right).           \tag{19}
\]

There is also an exact high-degree tail bound:

\[
 \Pr\{d(Y_*)\ge T\}
 \le {LV(P)\over N(T-1)}\qquad(T>1).                        \tag{20}
\]

Indeed `d<=d(d-1)/(T-1)` on `d>=T`, and then sum (8).
This is the bank analogue of the radial size-biased-core law

\[
 \mathbb E_\pi d_j=4^j\Pr_\pi\{|U|\ge2j\}.
\]

The fixed-rank first-moment identity alone is tautological.  Equations
(18)--(20) say precisely what additional geometric input is needed: a
one-face pair bank controls the size-biased tilt.  A recoverable
**two-output** cell controls only an `O(V^2)` pair pool and does not bound
the radial high tail at fixed-power scale.

## 5. The two-bank recoverable-cell threshold

The last warning does not rule out a structured two-bank telescope.  Let
the bank faces be grouped into common-base cells `c`, and write `w_c` for
the history mass in cell `c`.  Suppose there are two ordinary-face families
`A_c,B_c` such that

\[
                  w_c^2\le K|A_c||B_c|                       \tag{21}
\]

and

\[
 \sum_c|A_c|\le L_A V(P),\qquad
 \sum_c|B_c|\le L_B V(P).                                   \tag{22}
\]

> **Theorem 2 (fixed-power recoverable-cell Cauchy threshold).**  Under
> (21)--(22),
> \[
>                  \sum_cw_c\le\sqrt{K L_A L_B}\,V(P).       \tag{23}
> \]

**Proof.**  Sum the square roots in (21), apply Cauchy--Schwarz, and then
use (22):

\[
 \sum_cw_c\le\sqrt K\sum_c\sqrt{|A_c||B_c|}
 \le\sqrt{K\sum_c|A_c|\sum_c|B_c|}
 \le\sqrt{K L_A L_B}\,V(P).                                 \tag{24}
\]

QED.

For toggle banks, `sum_c w_c=q|S|` after assigning each bank incidence to
its output cell.  Put

\[
                    K L_A L_B\le n^{o(1)}D^{2\lambda}.       \tag{25}
\]

Then (23) gives

\[
 |E|=D|S|\le n^{o(1)}D^{1-\gamma+\lambda}V(P),              \tag{26}
\]

with the same `gamma` as (12).  At `alpha=1/2`, condition
`K L_A L_B<=D^(1-eta)n^o(1)` again gives saving `eta/2`.

This formulation shows exactly how much separate cell recoverability is
needed.  Taking the first bank to be the original source faces costs
`L_A<=q`, since one source occurs in its `q` toggle cells.  At the seam this
uses only `D^(1/2+o(1))` of the allowed product.  It would therefore suffice
to construct an erased/internal bank with

\[
                         K L_B\le D^{1/2-\eta}n^{o(1)}.       \tag{27}
\]

The quadratic shield does this through its unrestricted shield complex.
The stacked-pocket obstruction explains the difficulty in general: if the
internal output is forced to retain the outer tangent guards, coexistence
fails; if it erases them, many ancestor cells can reuse the same internal
face.  The desired recursion must make the other output recover the erased
context while still satisfying the separate sums (22), or prove a weighted
variant of (22) along first-divergence cells.

## 6. Geometry of one collision and the surviving contextual child

Suppose one toggle face `F_0` is shared by sources `A,A'`.  Replacing it by

\[
                         F=A\cap A'                            \tag{28}
\]

only increases the common face and remains legitimate: the original
collision implies `R_A union R_A' subseteq F_0 subseteq A cap A'`, so
`F` belongs to both toggle banks.  Put

\[
                         M=A\setminus F,qquad
                         M'=A'\setminus F.                    \tag{29}
\]

Then `M,M'` are disjoint and each has size at most `s`.  Every point of
either residual is individually addable to the convex polygon `F`, hence
lies in one of its cyclic edge pockets.

The nonadjacent-pocket theorem gives a real positive operation.  Components
inserted across nonadjacent edges coexist, and whole convex replacement
chains across such edges commute.  Therefore dispersed residual variation
creates mixed faces.  If the collision entropy remains confined to one
edge and its two neighbours, however, one obtains exactly the protected
three-pocket/two-orientation contextual child already isolated by the
circuit hard-core theorem.  Fixed-edge nesting inside that child is
projectively universal, so no theorem based only on its dominance-chain
order can finish (6).

This explains why a successful recursion must preserve the active tangent
frame while it descends.  At a later dispersed level it must charge a
single mixed face to the original collision square; it may not emit a new
independent face at every level.  Equivalently, its invariant must prove
(6) after summing all first-divergence weights.

There is now an exact local version of this split in
`../agent_quadratic_cross_core/BALANCED_HIDDEN_ATOM_POCKET_SPLIT.md`.
For a fixed common base `F`, aggregate every canonical rooted pocket atom
`Q` with its full completion weight `beta_Q`.  Given `T>=1` and
`0<eta<1`, it proves one of:

* atoms of weight greater than `T` retain at least half the occurrence
  mass and descend with their exact completion laws;
* separated light atoms create more than `eta W^2/4` one-face collision
  mass, with global load less than `s^4T^2`; or
* one cyclic three-pocket window retains more than
  `(1-eta)W/2` occurrence mass.

With `T=r^C`, the separated branch has `n^o(1)` load and plugs directly
into Theorem 1.  The caveat is load-bearing: the other two branches preserve
linear occurrence mass, not automatically its square.  If the heavy mass
splits among many atoms `Q`, cross-atom pairs have different descendant
bases `F union Q`; similarly a three-window family can contain many
different rooted chains.  The sum of the child squares may then be much
smaller than the parent square.  This is precisely where Theorem 2, rather
than an independent one-child descent, is needed.

Inside one fixed edge, those different rooted chains can realize an
arbitrary planar order type by projective universality.  Hence no
source-only rule which simply picks a largest contextual child can repair
the square loss.  The selected blocker/shield law or a two-bank
first-divergence invariant must remain in the state.

## 7. Entropy threshold and source-only regressions

The universal lower bound

\[
                 \log V(P)\ge(1/4-o(1))(\log n)^2            \tag{30}
\]

discharges an entire selected source subfamily `X` whenever
`log|X|=o((log n)^2)`: multiplying by the cap changes its logarithm by only
`O(log n)`.  More generally any total subfamily below the `1/4` coefficient
by a fixed margin is harmless.  This observation may be applied to a total
branch of the recursion, but not separately to exponentially many cells.

It also explains the elementary complete-convex regression.  On `2r`
points in convex position, the complete middle layer has
`|S|=binom(2r,r)` and only `2^(2r)` downfaces, so any source-only collision
map has load at least `2^(r-o(r))`.  This is not a hard EIC slice when
`r=Theta(log n)`, because its total entropy is only linear in `r` and the
global planar bank (28) swamps it.  A quadratic-entropy hard branch cannot
be dismissed this way.  There the extra repair/blocker geometry is
essential; a universal local toggle theorem with no entropy hypothesis
would be false.

## 8. Kill-search: the canonical hull outputs are quantitatively false

The quadratic shield gives an exact regression.  Ignore its common roots
and take residual source choices

\[
                  M_{S,T}=S\cup T,qquad
 S\in{L\choose s},\quad T\in{R\choose s},                   \tag{31}
\]

where `L union R` is in convex position.  Consider ordered source pairs
with `S,S'` disjoint and `T,T'` disjoint.  The canonical residual-union
output is the ordinary face

\[
                   M_{S,T}\cup M_{S',T'}.                    \tag{32}
\]

For a fixed output having `2s` labels on each side, the number of ordered
preimages is

\[
                         {2s\choose s}^2.                    \tag{33}
\]

With shield parameter `r=2s+O(1)`, (25) is

\[
                         2^{2r-o(r)}.                         \tag{34}
\]

At the seam the cap is `D=2^{r+O(1)}`, so this is `D^(2-o(1))`, much
larger than the required `D^(1-eta)`.  The same partition fibre occurs for
`ext(A union A')` when the relevant union is convex.  Taking only a first
onion remainder loses still more information and is invalid in general:
the remainder need not be a face.

This does not obstruct (6).  The complete shield has the enormous global
bank `2^(|L|+|R|)`, which pays the collision events nonlocally.  It proves
that the remaining theorem must count the whole released shield complex or
recurse contextually; no canonical one-output hull map can have the needed
load.

## 9. Exact remaining lemma

The preceding reductions leave the following statement, with no hidden
ambient-cell factor.

> **Cross-child bank lemma (open).**  In the central toggle-bank or marked
> common-blocker incidence graph, either the ordered collision count
> satisfies (6) for some absolute `eta>0`, or its protected three-pocket
> descendants admit two eventual banks satisfying
> `K L_A L_B<=n^o(1)D^(1-eta)`.  The statement must preserve the parent
> collision square across different descendant bases; preservation of only
> their total linear mass is insufficient.

The nonadjacent-pocket theorem proves the dispersed step.  Projective
universality proves that the concentrated child cannot be closed locally.
The unresolved content is exactly preservation/recovery of the tangent
context across edge switches.  Proving this lemma and substituting it into
(2) closes the high-rank half of fixed-power EIC; (16) gives the analogous
closure for the low-rank common-blocker half.

## 10. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_cross_child_telescope/verify_cross_child_collision.py
```

The verifier exhausts all small left-regular bipartite bank graphs, checks
the collision identity and the sharp quadratic root in (1), audits the
fractional and high-tail variants, checks the exponent arithmetic in
(3)--(5), and verifies the exact shield-union fibre (25).
