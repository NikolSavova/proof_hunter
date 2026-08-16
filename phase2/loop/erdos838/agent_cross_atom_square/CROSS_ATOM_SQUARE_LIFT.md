# Cross-atom square lift in a protected three-pocket window

**Date:** 2026-08-14.  All masses below may be read either as numbers of
labelled occurrences or as nonnegative integer weights.

## Verdict

The apparent loss from sending many heavy hidden atoms to different bases
is not intrinsic.  There is an exact square-preserving version of the
pocket split.

First, the ordered collision square localizes without loss: either a fixed
fraction is already on separated pockets, one atom carries a fixed fraction
of the square, or a fixed fraction consists of pairs of distinct atoms in
one protected three-pocket window.  Second, inside such a window a face of
rank `s` has at most `3s^4` rooted-atom descriptions.  There is an even
more flexible decoder when an output keeps its contextual core up to at
most `b` open slots: its context overlap is at most
`sum_(t<=b) binom(s,t)` times the number of canonical tangent types.
Consequently the recoverable-cell Cauchy telescope sums paired child
decoders over arbitrarily many heavy atoms with only a polynomial factor:

\[
 \boxed{\sum_c |\mathcal G_c|
       \le 3s^4\sqrt K\,V(P).}                       \tag{1}
\]

Here `c` ranges over all contextual bases, and each child only has to prove

\[
 |\mathcal G_c|^2\le K|\mathcal A_c||\mathcal B_c|   \tag{2}
\]

using two ordinary-face banks which keep either the three-pocket cut or the
open-slot core recoverable.
There is no factor equal to the number of atoms or bases.

There is also an exact blocker-preserving realization of (2).  If two
recoverable one-slot endpoint reservoirs have sizes `q_-` and `q_+`, and
the blocker cloud has size `y`, the two blocker identities are
encoded--not discarded--with

\[
 K=\left\lceil {q_-q_+y^2\over s(q_-)s(q_+)}\right\rceil,
 \qquad s(q)=1+q+{q\choose2}.                       \tag{3}
\]

Thus `q_-=q_+=y` gives `K<=4`, uniformly across all heavy atoms.  Refining
the atoms by their arbitrary retained inner core does not lose their cross
square: deleting at most three output slots recovers that core, and Cauchy
then resums all cores.  This is a genuine one-/three-pocket shield square
theorem and closes the **spread among heavy atoms** gap whenever two
one-slot reservoirs are exposed.

It does not prove that every protected one-pocket child exposes those
reservoirs.  In a single fixed insertion edge the internal order type is
projectively universal.  Therefore the remaining branch is exactly the
one-pocket blocker/shield-progress theorem, not an accounting loss from
having many contextual bases.

## 1. Weighted square localization

Let the atoms in pocket `i` have weights `beta_(i,a)`, put

\[
 p_i=\sum_a\beta_{i,a},\qquad H=\sum_i p_i,           \tag{4}
\]

and call two cyclic pockets separated when they are neither equal nor
adjacent.  The ordered separated mass is

\[
 S=\sum_{i,j\ \text{ separated}}p_ip_j.              \tag{5}
\]

For the three-window mass `M_i=p_(i-1)+p_i+p_(i+1)`, direct expansion gives

\[
 S=H^2-\sum_i p_iM_i
   \ge H(H-\max_iM_i).                                \tag{6}
\]

> **Theorem 1 (square pocket trichotomy).**  Fix `0<eta,delta<1`.  At
> least one of the following holds.
>
> 1. separated ordered atom pairs have mass at least `eta H^2`;
> 2. one atom has weight at least `delta(1-eta)H`, and its diagonal child
>    therefore retains at least `delta^2(1-eta)^2H^2` collision mass;
> 3. a three-pocket window has mass `M>(1-eta)H`, and ordered pairs of
>    distinct atoms inside it have mass greater than
>    `(1-delta)M^2`.

**Proof.**  If (1) fails, (6) gives a window of mass
`M>(1-eta)H`.  Let `m` be its largest atom weight.  If `m>=delta M`, (2)
holds.  Otherwise

\[
 \sum_{\alpha\ \text{ in window}}\beta_\alpha^2
 \le m\sum_\alpha\beta_\alpha=mM<\delta M^2.        \tag{7}
\]

Subtract (7) from `M^2`.  This proves (3).  QED.

Inside the selected window, pairs using its first and third pockets return
to alternative 1.  Hence the genuinely unspent part of alternative 3 is in
one pocket or two adjacent pockets.  The theorem is an exact correction to
a linear-mass descent: a family of many equally heavy atoms is sent to the
cross-atom branch rather than losing its square.

## 2. Recovering a protected window from one face

Let `F` be a counterclockwise convex polygon and let

\[
 e_0=a_0a_1,\quad e_1=a_1a_2,\quad e_2=a_2a_3       \tag{8}
\]

be three consecutive directed edges.  A set `D_j` lies in pocket `j` when
its points violate precisely the support inequality of `e_j`.  Call

\[
 U=F\cup D_0\cup D_1\cup D_2                         \tag{9}
\]

a **protected window face** when it is in convex position.  Choose an
active index `j` and require `D_j=Q` to be the fixed rooted atom.  Completion
data--the opposite half, blocker, selector mark, and outer history--remain
in the conditional law; they are not included in the definition of `Q`.

> **Lemma 2 (four-root decoder).**  A protected window face `U` of rank at
> most `s` has at most `3s^4` descriptions `(F,e_0,e_1,e_2,j,Q)` of the
> preceding form.

**Proof.**  Guess the ordered four roots `(a_0,a_1,a_2,a_3)` from `U`, in
at most `s^4` ways.  The three pocket components are then forced:

\[
 D_i=\{x\in U:\operatorname{orient}(a_i,a_{i+1},x)<0\}. \tag{10}
\]

Validity requires these sets to be disjoint and every remaining point to
obey all three retained support inequalities.  If valid,

\[
 F=U-(D_0\cup D_1\cup D_2)                         \tag{11}
\]

is forced.  Finally choose the active index in three ways and put `Q=D_j`.
Invalid guesses are discarded.  QED.

This is where the three-pocket protection is load-bearing.  For additions
in arbitrarily many pockets, recovering `F` may require an arbitrary subset
of the output boundary.  For a single unmarked fixed-edge chain, such a
recovery statement would contain an arbitrary planar order type.

The conditional repair law survives the change of base exactly.  If an
occurrence has source `F union C`, atom `Q=C cap R_j(F)`, and new base
`F union Q`, then the residual source is

\[
 (F\cup Q)\cup(C-Q)=F\cup C.                         \tag{12}
\]

Any exterior blocker, repaired hull, selector mark, and shield relation are
therefore literally the same labelled objects.  Lemma 2 is not permission
to project them away.

There is a second recovery mechanism which does not require all retained
coordinates to lie in the three pockets.

> **Lemma 3 (open-slot core decoder).**  Suppose every contextual type `c`
> has a canonical ordinary core `R_c`, and an output in its bank has the
> form
> \[
>                         U=R_c\cup E,\qquad |E|\le b. \tag{12a}
> \]
> Once `R_c` and one of `Z` tangent/transition types are known, the cell and
> its state-dependent codebook are forced.  Then a face of rank at most
> `s` occurs in at most
> \[
>                  Z S_b(s),\qquad
>                  S_b(s)=\sum_{t=0}^b {s\choose t}          \tag{12b}
> \]
> such contextual banks.

**Proof.**  Guess `E subset U` with `|E|<=b`, put `R_c=U-E`, and guess the
canonical type.  These data force `c`; invalid guesses are discarded.  QED.

The core may contain an arbitrary inner order type and arbitrary earlier
pocket history.  Only the number of genuinely open output slots is paid.
This is why refining a heavy atom by all of its retained completion
coordinates does not reintroduce the number of refined cells.

## 3. The two-bank square lift

Let `c` range over any collection of contextual cells, possibly with
different bases and different active pockets.  Let `G_c` be the exact
conditional completion/blocker occurrences under `c`.  Suppose there are
ordinary-face families `A_c,B_c` such that

1. every member of both families recovers `c`, either as a protected window
   face by Lemma 2 or as an open-slot core by Lemma 3; and
2. a paired child decoder has maximum fibre `K_c`:

\[
                 |G_c|^2\le K_c|A_c||B_c|.          \tag{13}
\]

> **Theorem 4 (cross-atom recoverable-cell Cauchy telescope).**  Let `L_A`
> and `L_B` bound the number of `A_c`- and `B_c`-banks containing one
> ordinary face.  If `K=max_c K_c`, then
> \[
>             \sum_c|G_c|\le\sqrt{K L_A L_B}\,V(P).  \tag{13b}
> \]
> In the protected-window case Lemma 2 gives (1).  In the open-slot case,
> Lemma 3 gives the same statement with `3s^4` replaced by
> `sqrt(Z_A Z_B S_{b_A}(s)S_{b_B}(s))`.
> Equivalently, the complete collision square obeys
> \[
>       \left(\sum_c|G_c|\right)^2
>          \le K L_A L_B\,V(P)^2.                    \tag{13c}
> \]

**Proof.**  By the definitions of `L_A,L_B`,

\[
 \sum_c|A_c|\le L_AV(P),\qquad
 \sum_c|B_c|\le L_BV(P).                            \tag{14}
\]

Sum the square roots of (13) and apply Cauchy:

\[
\begin{aligned}
 \sum_c|G_c|
 &\le\sqrt K\sum_c\sqrt{|A_c||B_c|}\\
 &\le\sqrt{K\sum_c|A_c|\sum_c|B_c|}
 \le\sqrt{K L_A L_B}\,V(P).
\end{aligned}                                       \tag{15}
\]

QED.

The theorem is the requested square correction.  Applying a linear child
bound separately and then summing contextual weights is unsafe.  Applying
the paired bound (13) and only then Cauchy preserves all cross-atom mass.
The number of heavy atoms never enters (15).

## 4. A blocker-faithful flank/shield bank

Here is a concrete sufficient condition for (13).  Fix a context `c` and
let its records factor as

\[
 \mathcal G_c=\mathcal R_c\times X_-\times X_+\times Y,     \tag{16}
\]

where `Y` is the actual blocker alphabet.  Put
`q_-=|X_-|,q_+=|X_+|,y=|Y|`.  Assume the following two one-slot facts.
The four factors are labelled disjoint coordinate systems, and the
coordinates retained in an output determine its member of `R_c`; this is
the usual recoverable product-cell convention, not an unlabelled support
projection.

* In the first output, retain every record coordinate except its `X_-`
  symbol and replace that symbol by any subset of `X_-` of size at most two.
  The result is an ordinary face and either is a protected window face
  retaining `Q`, or recovers its canonical core after deletion of at most
  three open labels.
* The analogous assertion holds in the second output for `X_+`.

For the four-root decoder, the distinguished reservoirs are nonactive
pockets, so the component `Q` and all four window roots remain recoverable.
For the open-slot decoder they may instead lie in the active pocket,
provided deleting the at-most-two code labels and the one retained endpoint
symbol recovers a canonical core and hence the reservoir alphabet.  The two
reservoirs may be adjacent or identical in tangent type: they occur in
different output faces.

> **Theorem 5 (flank square code).**  Under (16) and the one-slot facts,
> (13) holds with `K` given by (3).

**Proof.**  For ordered records `g,h`, retain all coordinates of `g` except
`x_-(g)` in the first face and all coordinates of `h` except `x_+(h)` in
the second.  Enumerate the four-symbol tuples

\[
                  (x_-(g),x_+(h),p_g,p_h)           \tag{17}
\]

and distribute them as evenly as possible over

\[
 {X_-\choose\le2}\times {X_+\choose\le2}.          \tag{18}
\]

The maximum finite-code fibre is exactly the ceiling in (3).  The two
one-slot hypotheses make both codewords ordinary faces with a recoverable
window or open-slot core.  Their retained coordinates recover both inner
histories.  In particular the two bank sizes are exactly

\[
 |A_c|=|\mathcal R_c|q_+s(q_-),\qquad
 |B_c|=|\mathcal R_c|q_-s(q_+),                      \tag{18a}
\]

so the ratio `|G_c|^2/(|A_c||B_c|)` is the expression inside the ceiling
in (3).  The finite code recovers both blocker labels and both omitted endpoint labels with at
most `K` choices.  Thus no blocker or shield tag is forgotten.  QED.

Since `s(q)>=q^2/2`,

\[
 K\le\left\lceil{4y^2\over q_-q_+}\right\rceil.     \tag{19}
\]

In the balanced protected-window case Theorems 4--5 give

\[
                  \sum_c|G_c|\le6s^4V(P).           \tag{20}
\]

There is a form which is usually more useful for the heavy-atom descent.
Allow the factor `R_c` in (16) to range over arbitrary labelled inner
cores, and split the record family into cells indexed by `R`.  In the first
output the open set consists of the code subset `E_-` (at most two labels)
and the retained `X_+` symbol; deleting at most three labels therefore
recovers `R`.  The second output is symmetric.  If the two codebooks are
canonical from `R` up to `Z` tangent types, Lemma 3 and Theorems 4--5 give

\[
 \boxed{
 |\mathcal R\times X_-\times X_+\times Y|
   \le ZS_3(s)\sqrt K\,V(P).}                       \tag{20a}
\]

In particular the balanced loss is at most `2ZS_3(s)`.  Arbitrarily many
different inner cores, heavy atoms, and bases are already summed in (20a);
they are not pigeonholed.  The exact blocker labels are still the two
symbols `p_g,p_h` in (17), so this refinement does not weaken the shield
law.

More generally, `y^2<=n^o(1)q_-q_+` gives subpolynomial square loss.  This
is precisely the two-ended/shield payment expected in a three-pocket child.

## 5. Exact residual

Equations (1) and (20) remove two false obstructions:

* collision mass may be spread among exponentially many heavy atoms; and
* their bases may vary arbitrarily, provided the two output banks retain a
  recoverable protected window or open-slot core.

The remaining obstruction is geometric.  A child can have all of its
entropy in one active pocket, with no two recoverable one-slot reservoirs
satisfying (19), even after allowing the active-pocket/open-slot decoder.
The insertion order in that pocket is a two-dimensional dominance order,
and one strict chain in it can carry an arbitrary planar order type by a
projective transformation.  Consequently one cannot replace the one-slot
hypotheses by “all records use the same edge” or “the blockers are nested.”

There is also a precise interface warning.  Theorem 1 localizes the
**indices of the chosen atoms** to a three-window; it does not by itself say
that every opposite-half completion is supported in those three pockets.
Such a completion is covered by Theorem 5 only after its outside coordinates
are retained in the recoverable core `R`, as in (20a), or after a separate
protected-window reduction.  Dropping them would again erase the
completion/blocker law.

The live lemma after this report is therefore:

\[
 \boxed{\text{a blocker-bearing one-pocket child either exposes two
 recoverable one-slot/shield reservoirs, or makes quantified progress while
 preserving a recoverable core.}}                            \tag{21}
\]

The accounting, atom spread, base overlap, and blocker coding on the first
branch are settled above.  Proving (21) on the universal nested branch is
still required to close Erdős 838.

## 6. Exact verification

Run

```bash
python3 phase2/loop/erdos838/agent_cross_atom_square/verify_cross_atom_square_lift.py
```

The checker exhausts cyclic weight vectors for Theorem 1, audits the
four-root decoder on exact rational three-pocket configurations, exhausts
small flank-code parameters and their exact ceiling fibres, enumerates the
open-slot reverse descriptions through rank 32, and stress-tests the integer
recoverable-cell Cauchy inequality.
