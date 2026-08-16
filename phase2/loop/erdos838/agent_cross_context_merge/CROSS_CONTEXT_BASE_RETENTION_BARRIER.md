# Cross-context square descent: retaining the ancestor base is impossible

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

The common-base pocket split cannot be globalized by requiring both eventual
face banks to keep the common ancestor base.  There is an exact capped,
rank-seam, zero-addable-degree construction in which every occurrence lies in
one fixed pocket and every atom is heavy, but a face containing the ancestor
base carries at most one pocket label.  The parent square is then larger than
the complete two-bank base-retaining range by a factor `D^(2-o(1))`.

More precisely, for every sufficiently large rank `r` there is a rational
general-position set with

\[
 n=2^{2r},\qquad D=2^r={n\over2^r},                         \tag{1}
\]

and `D` rank-`r` low-addable sources, each with `D` selected exterior
repairs.  Relative to one common `(r-1)`-face `B`, the resulting atom weights
are

\[
                 \beta_1=\cdots=\beta_D=D,
 \qquad W=\sum_i\beta_i=D^2.                               \tag{2}
\]

Nevertheless the entire ordinary-face bank which contains `B` has only
`2D+1` members.  Consequently:

* the heavy-atom descent retains linear mass `W`, but its child-square sum is
  only `D^3=W^2/D`;
* any map of the ordered **cross-atom** record pairs to two ordinary faces
  both containing `B` has a fibre at least `D^2/18`;
* any recoverable-cell Cauchy certificate confined to two such banks must
  have
  \[
                       K L_A L_B\ge D^2/9.                  \tag{3}
  \]

The desired seam threshold is `D^(1-eta)n^o(1)`, so (3) misses it by more
than a full fixed power for every absolute `eta>0`.

This is **not** a counterexample to fixed-power EIC'.  The source family in
this construction has only `D=2^r` members, hence only linear-in-`r`
entropy, and the interior padding has a large unrestricted face bank by
Erdos--Szekeres.  It is a counterexample to the precise proposed interface
in which the intersection/common ancestor base is kept in both outputs.
A valid global proof has to release that base (in at least one output) and
recover it from a first-divergence code, or spend the branch through an
unguarded global face bank.

## 1. The nested one-pocket construction

Let `B` be a rational convex `(r-1)`-gon with a distinguished edge `uv`.
Choose rational points

\[
                         x_1,\ldots,x_{2D}                    \tag{4}
\]

in the exterior insertion pocket of `uv` so that

\[
 x_i\in\operatorname{int}\operatorname{conv}\{u,v,x_j\}
                         \qquad(i<j).                        \tag{5}
\]

All points can be chosen in general position.  One construction starts with
`u=(-1,0),v=(1,0)`, chooses successive apexes in the open wedge above `uv`
so that the preceding finite set lies strictly inside the new triangle,
and at every step avoids the finitely many forbidden secant lines.  The
rationals are dense, so all choices may be rational.  Choose `B-\{u,v\}`
generically below `uv`.

For `1<=i<=D`, put

\[
                         A_i=B\cup\{x_i\}.                   \tag{6}
\]

For every `D<j<=2D`, (5) gives the exterior rotation

\[
 \operatorname{ext}(A_i\cup\{x_j\})=B\cup\{x_j\}.          \tag{7}
\]

Select all `D^2` records `(A_i,x_j)`.  Thus each actual source has exactly
the cap `D` selected blockers.

Finally add

\[
          2^{2r}-(r-1)-2D                                   \tag{8}

rational points in the interior of `conv(B)`, choosing them successively
off all existing secant lines.  They calibrate the ambient size without
changing any statement involving a face which contains `B`.  Equation (1)
is now exact, and every source in (6) has rank `r`.

Every point outside `A_i` fails to be addable.  An interior padding point is
already in `conv(B)`.  If `k<i`, then `x_k` lies inside
`conv{u,v,x_i}`; if `k>i`, adding `x_k` makes `x_i` non-extreme.  Hence

\[
                         a(A_i)=0.                            \tag{9}
\]

This places the example inside the strongest low-addable slice, not merely
inside an abstract weighted recursion.

## 2. Exact pocket weights and square loss

Use `B` as the common base in the weighted pocket theorem.  The canonical
atom of every record over source `A_i` is

\[
                       \alpha_i=(B,uv,\{x_i\}).              \tag{10}
\]

The blocker `x_j` is completion data.  All `D` blockers occur over every
atom, so (2) follows.  All atoms lie in the same edge pocket.  In
particular, for every polynomial threshold `T=r^C`, all mass is in the
heavy branch once `r` is large, and the same mass is also contained in one
three-pocket window.

If the heavy branch is split into its atom children, the square retained by
independent child accounting is

\[
              \sum_{i=1}^D\beta_i^2=D^3={W^2\over D}.       \tag{11}
\]

The off-diagonal first-divergence mass is exactly

\[
 \Delta=W^2-\sum_i\beta_i^2
       =D^4-D^3=D^3(D-1).                                  \tag{12}
\]

Thus the warning that linear mass retention need not preserve the parent
collision square is sharp by a full factor `D` even in one genuine planar
pocket.

## 3. Faces containing the common ancestor cannot pay

There is first a positive recovery fact which removes one possible source of
confusion.

> **Lemma 1 (rooted atom faces have polynomial contextual overlap).**  Let
> `U=F union Q` be an ordinary face, where `Q` is a nonempty chain in the
> exterior pocket of a directed edge `uv` of `F`, all vertices of `F` lie
> in the retained closed half-plane, and all vertices of `Q` lie in the
> opposite open half-plane.  Among atoms satisfying these conditions, a
> fixed labelled face `U` has at most
> \[
>                         |U|(|U|-1)                         \tag{13}
> \]
> preimages `(F,uv,Q)`.

**Proof.**  Guess the ordered pair `(u,v)` in `U`.  The support line then
forces `Q`: it is exactly the set of vertices of `U` in the open pocket
half-plane.  It also forces `F=U-Q`.  There are fewer than
`|U|(|U|-1)` ordered pairs, and invalid guesses only lower the count.  QED.

Thus different descendant bases do **not** create a large first-bank
overlap once the rooted atom face itself is kept: over rank at most `r`,

\[
              \sum_c|\mathcal A_c|\le r^2V(P).              \tag{14}
\]

The obstruction below proves that this polynomial recovery does not supply
the second/internal bank.

Let

\[
 \mathcal F_B=\{F\subseteq P:F\text{ is in convex position and }B\subseteq F\}.
                                                                    \tag{15}
\]

By (5), a set containing `u,v` and two chain points is not in convex
position: the earlier chain point is strictly inside the triangle formed by
`u,v` and the later one.  An interior padding point is non-extreme in every
set containing `B`.  Conversely, `B` and every `B+x_i` are ordinary faces.
Therefore

\[
                         |\mathcal F_B|=2D+1.                \tag{16}
\]

Consider ordered pairs of selected records whose source atoms are distinct.
There are `Delta` of them, by (12).  Their two source faces intersect in
exactly `B`, so this is precisely the cross-atom square whose context one
might try to retain.  Every map into `mathcal F_B^2` has maximum fibre at
least

\[
 \left\lceil {D^3(D-1)\over(2D+1)^2}\right\rceil
       \ge {D^2\over18}\qquad(D\ge2).                       \tag{17}
\]

The same obstruction applies to the recoverable-cell formulation.  Suppose
the record family is partitioned into cells `G_c`, and both face families
`A_c,B_c` are subsets of `mathcal F_B`, with

\[
 |G_c|^2\le K|\mathcal A_c||\mathcal B_c|,\qquad
 \sum_c|\mathcal A_c|\le L_A|\mathcal F_B|,\qquad
 \sum_c|\mathcal B_c|\le L_B|\mathcal F_B|.                \tag{18}
\]

The exact Cauchy telescope gives

\[
 D^2=W\le\sqrt{K L_A L_B}\,(2D+1).
\]

Hence

\[
 K L_A L_B\ge {D^4\over(2D+1)^2}\ge {D^2\over9},           \tag{19}
\]

which is (3).  This conclusion is independent of the cell partition,
first-divergence chronology, fractional weights, or whether the decoder
recovers `B` explicitly: containment of `B` in both output banks alone
causes the deficit.

Lemma 1 and (19) together locate the failure.  Variation of the descendant
base has polynomial one-bank overlap.  What fails is the second/internal
bank: in the strict chain, keeping the same base prevents two completion
labels from coexisting.  The obstruction is geometric capacity, not
ambiguity in naming the base.

## 4. What one released bank proves exactly

Releasing one output from the ancestor base is not merely necessary; it
gives an exact positive Cauchy theorem until a sharply measured reservoir
overload occurs.

Let `mathcal C` be a set of contextual one-pocket cells.  In each cell `c`,
suppose there are `D^2` occurrences as above and a `2D`-point internal
label set `X_c`.  Let

\[
 \mathcal A_c=\{B_c\cup\{x\}:x\in X_c\},\qquad
                         |\mathcal A_c|=2D.                  \tag{20}
\]

Assume that a fixed ordinary face belongs to at most `Lambda` of the
families `mathcal A_c`.  Lemma 1 gives `Lambda<=r^2` when the rooted edge is
the only unmarked context.  Let `mathcal H` be any ordinary-face reservoir
available after dropping the ancestor base; for one shared chain it may be
the complete face complex of `X`.  Put

\[
 H=|\mathcal H|,\qquad b=\left\lceil{D^3\over2}\right\rceil,
 \qquad C=|\mathcal C|.                                    \tag{21}
\]

> **Theorem 2 (released-reservoir square allocation).**  Suppose `H>=b` and
> every cell may use every member of `mathcal H`.  There are subsets
> `mathcal B_c subseteq mathcal H`, each of size `b`, such that
> \[
>  D^4\le|\mathcal A_c||\mathcal B_c|,
>  \qquad
>  \max_{F\in\mathcal H}|\{c:F\in\mathcal B_c\}|
>       \le\left\lceil{Cb\over H}\right\rceil.              \tag{22}
> \]
> Consequently the recoverable-cell Cauchy telescope gives
> \[
>       C D^2\le
>       \sqrt{\Lambda\left\lceil Cb/H\right\rceil}\,V(P).   \tag{23}
> \]

**Proof.**  Enumerate `mathcal H` cyclically and give cell `c` the `b`
consecutive positions starting after the preceding cell's block.  Since
`b<=H`, every `mathcal B_c` is a set, and all `Cb` incidences are distributed
over `H` positions with loads differing by at most one.  This proves the
overlap assertion.  Equation (21) gives
`|mathcal A_c||mathcal B_c|=2Db>=D^4`.  Apply the two-bank Cauchy theorem
with `K=1`, first-bank overlap `Lambda`, and the overlap in (22).  QED.

For the strict chain, the unrestricted internal reservoir is
`mathcal H=mathcal F(X)`.  The established universal convex-subset lower
bound gives

\[
 \log |\mathcal F(X)|\ge(1/4-o(1))(\log |X|)^2,             \tag{24}
\]

so `H>D^A` for every fixed `A` once `D` is large.  Thus one isolated
context, or even any fixed-polynomial number of contexts, is discharged
with overlap one after one bank releases `B`.  This explains exactly why
the construction in Sections 1--3 is not an EIC' counterexample.

For the record family as stated, (23) directly implies fixed-power EIC'
whenever `Lambda ceil(Cb/H)<=D^(2-2epsilon)n^o(1)`.  In the actual
toggle/cross-child interface, where this product is inserted before the
central `q=sqrt(D)` bank factor, the sharper threshold already isolated in
the cross-child report is reached whenever, for some absolute `eta>0`,

\[
       \Lambda\left\lceil {C D^3\over2H}\right\rceil
                   \le D^{1-\eta}n^{o(1)}.                  \tag{25}
\]

If (25) fails, the obstruction is no longer descendant-base ambiguity:
it is the exact overload `C D^3/H` of the released internal reservoir by
quadratically many outer contexts.  A complete proof must then create
context-dependent mixed faces, or prove that the outer contexts and the
released reservoir multiply inside `F(P)`.

There is also a global entropy cutoff which should be applied before this
overload is studied.  If the entire active source family `S` has

\[
                         \log|S|=o((\log n)^2),              \tag{26}
\]

then a cap of at most `n` gives `|E|<=n|S|=2^{o((log n)^2)}`,
whereas the universal lower bound gives
`V(P)>=2^{(1/4-o(1))(log n)^2}`.  Hence `|E|<=V(P)` for all
sufficiently large `n`.  The genuinely live case of (25) therefore has
both quadratic source entropy and a released reservoir reused beyond its
own quadratic capacity.

## 5. Consequence for the live cross-child lemma

The common-base pocket theorem remains correct and useful.  Its separated
light-atom branch emits a one-face mixed bank and never enters this example.
The no-go concerns its heavy and three-pocket descendants.

The exact surviving interface is therefore narrower than “control merging
of descendant bases.”  Even with one fixed base and zero merging, the
collision square cannot be carried by two base-retaining banks.  A positive
first-divergence telescope must do one of the following:

1. release the ancestor tangent guards in at least one eventual face and
   encode the erased context jointly with the internal history;
2. charge the cross-atom divergence to an unguarded ordinary face before
   descending; or
3. invoke a global entropy cutoff which shows that the entire concentrated
   branch is too small to matter.

Option 3 disposes of the construction above, whose source entropy is only
`O(r)`.  Theorem 2 proves option 1 up to the explicit overload (25).  What
remains open is precisely the quadratic-entropy regime in which many outer
contexts reuse the same released internal reservoir with load greater than
`D^(1-eta)`.  The strict-chain construction proves that neither
first-divergence weights nor recoverability of the common intersection,
without such a guard-release allocation or a new mixed bank, supplies that
missing geometry.

## 6. Exact verification

Run

```bash
python3 phase2/loop/erdos838/agent_cross_context_merge/verify_cross_context_base_retention.py
```

The checker uses an exact rational projective insertion chain with twenty
tips.  It verifies all source/target hull identities, zero addability,
the exact full-base face count, the weighted heavy-atom and first-divergence
identities, and the finite fibre lower bounds.  On the transferred exact
20-point record, the released internal reservoir has `4,775` faces; the
checker constructs the balanced allocation in Theorem 2 and verifies that
nine contexts have overlap one while ten contexts have the sharp overlap
two.  It also audits the symbolic rank-seam padding, cap, and inequalities
(17)--(19) for ranks through 64.
