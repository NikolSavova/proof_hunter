# Marked halfplane bank for a root--shield star

## Verdict

The proposed marked bank is valid, including the exponent and the retained
mark.  Moreover, it globalizes with a polynomial decoder: pairing a marked
halfplane output with its completion face has multiplicity at most

\[
             \left\lfloor{q^2\over4}\right\rfloor {b\choose2},       \tag{1}
\]

where the top shields have rank at most `q` and the carriers have rank at
most `b`.  Thus the high `(x,z)`-profile fibre is not a new obstruction: it
releases distinct completion faces after only a `binom(b,2)` edge loss.

This is a genuine second ordinary-face bank.  It retains the repair mark
`{x,z}` and does not require recovering that mark intrinsically from the
unlabelled output alone.

## 1. Local geometry

> **Lemma 1 (marked halfplane bank).**  Let `Q` be a finite planar set in
> convex position, let `z,u,v in Q`, and let
> \[
>                         x\in\operatorname{int}\triangle(u,v,z).     \tag{2}
> \]
> Assume the ambient point set is in general position.  Partition
> `Q setminus {z}` by the two open halfplanes of the line `xz`, and let
> `H` be a larger part.  Then
> \[
> |H|\ge\left\lceil{|Q|-1\over2}\right\rceil,             \tag{3}
> \]
> and every set
> \[
>                         \{x,z\}\cup S,\qquad S\subseteq H,          \tag{4}
> \]
> is in convex position.  Consequently (4) gives at least
> \[
>                         2^{\lceil(|Q|-1)/2\rceil}                    \tag{5}
> \]
> distinct ordinary faces, all retaining the labelled pair `{x,z}`.

**Proof.**  Condition (2) puts `x` in the interior of `conv(Q)`.  General
position implies that no point of `Q setminus {z}` lies on `xz`; hence the
two open halfplanes partition `Q setminus {z}` and (3) follows.

Fix `S subseteq H`.  Every point of `S union {z}` remains exposed after
`x` is added.  Indeed, a vertex `w` of the convex polygon `Q` has a linear
functional uniquely maximized at `w` on `Q`.  Since `x` is in the interior
of `conv(Q)`, the same functional is strictly smaller at `x`.  It therefore
still exposes `w` in `{x,z} union S`.

The line `xz` supports `{x,z} union S`, since all points of `S` lie in one
of its open halfplanes.  Its intersection with the new convex hull is the
segment `[x,z]`; thus both endpoints `x,z` are extreme.  All points in (4)
are therefore vertices.  There are `2^|H|` choices of `S`, proving (5).
QED.

Because `x` is an interior point, every line through `x` meets the interior
on both sides.  In particular both halfplane parts are nonempty.  If
`|Q|<=q`, every output in (4) consequently has rank at most `q` (not
`q+1`).

## 2. Canonical root--shield incidences

Use the exact first-divergence data from
`CROSS_ANCHOR_COMPLETION_TELESCOPE.md`.  A canonical incidence consists of

\[
 (Y,Q,x,z,e),\qquad Y=B\cup\{x\},\quad e=\{u,v\}\subseteq B,         \tag{6}
\]

where `Q` is an ordinary convex top face containing `B union {z}` and
`x in int triangle(u,v,z)`.  The missing root satisfies `z notin Y`.
The central cell is determined by

\[
                         B=Y\setminus\{x\},\qquad T=e\cup\{z\}.      \tag{7}
\]

For every incidence, choose the richer halfplane `H` canonically (breaking
a tie by the ambient label order) and emit all faces

\[
                         F=\{x,z\}\cup S,\qquad S\subseteq H.        \tag{8}
\]

Let `mathcal I` denote the resulting set of marked occurrences `(c,S)`.
By Lemma 1,

\[
 |\mathcal I|
 \ge\sum_c2^{\lceil(|Q_c|-1)/2\rceil}.                    \tag{9}
\]

## 3. Global bounded-overlap theorem

> **Theorem 2 (completion--halfplane pair decoder).**  Suppose
> `|Y|<=b+1` and `|Q|<=q` for every canonical incidence.  The map
> \[
>                         (c,S)\longmapsto(Y,F)                         \tag{10}
> \]
> has multiplicity at most
> \[
>                         D=\left\lfloor{q^2\over4}\right\rfloor
>                            {b\choose2}.                              \tag{11}
> \]
> Hence, writing `V(P)` for the number of ordinary convex subsets of the
> ambient point set,
> \[
> \boxed{
> \sum_c2^{\lceil(|Q_c|-1)/2\rceil}
>       \le D\,V(P)^2.}                                      \tag{12}
> \]

**Proof.**  Fix the two labelled output faces `(Y,F)`.  To recover a
preimage, guess

\[
 x\in Y\cap F,\qquad z\in F\setminus Y,\qquad
 e\in{Y\setminus\{x\}\choose2}.                            \tag{13}
\]

The first two roles are forced in every genuine preimage because `x in Y`,
`z notin Y`, and both marks are retained in `F`.  Equation (7) then
recovers the canonical cell and its top face `Q`; finally
`S=F setminus {x,z}` is forced.

There are at most `binom(b,2)` choices for `e`.  If
`a=|Y cap F|`, then the number of choices for `(x,z)` is at most

\[
                         a(|F|-a)\le\left\lfloor{|F|^2\over4}\right\rfloor
                         \le\left\lfloor{q^2\over4}\right\rfloor.    \tag{14}
\]

This proves (11).  Both coordinates in (10) are ordinary faces, so their
range has size at most `V(P)^2`; (9) now gives (12).  QED.

If every live shield has rank at least `s`, and `N` is the number of
canonical incidences, (12) yields the explicit corollary

\[
 N\,2^{\lceil(s-1)/2\rceil}
 \le\left\lfloor{q^2\over4}\right\rfloor{b\choose2}V(P)^2.           \tag{15}
\]

Thus logarithmic-rank shields produce a genuine fixed-power factor before
the polynomial decoder loss.

## 4. The requested low/high profile split

The same result can be seen as an exact codegree dichotomy.  Let `theta`
be the largest number of marked occurrences having one fixed triple
`(x,z,F)`.

* A face `F` of rank at most `q` supports at most `q(q-1)` ordered mark
  profiles.  Hence the unpaired halfplane bank has size at least
  \[
                  {|\mathcal I|\over q(q-1)\theta}.                    \tag{16}
  \]

* In a fibre with fixed `(x,z,F)`, one completion face `Y` supports at most
  `binom(b,2)` occurrences: after `Y` is fixed, only `e` remains to be
  guessed, and (7) recovers the cell.  Therefore that high fibre contains
  at least
  \[
                         {\theta\over\binom(b,2)}                       \tag{17}
  \]
  distinct ordinary completion faces.

Thus low profile overlap pays directly through (16), while high overlap
fixes the retained repair mark and releases the varying carriers through
their completion faces.  Multiplying (16) and (17) already gives the
slightly weaker but still polynomial global estimate

\[
             |\mathcal I|\le q(q-1){b\choose2}V(P)^2.                 \tag{18}
\]

The direct pair decoder sharpens `q(q-1)` to `floor(q^2/4)`.

## 5. Scope

The theorem resolves the overlap question for canonical root--shield
incidences: no additional history coordinate is required once the common
completion `Y` is retained as the first output face.  It does not assert
that the halfplane face `F` alone identifies `(x,z)`; indeed it generally
does not.  The bounded ambiguity is exactly why the pair decoder uses the
set differences `Y cap F` and `F setminus Y`.

Whether (15) closes a particular ACP slice is then a quantitative question
about how many marked records are represented by each canonical incidence
and the lower ranks of its shields, not a remaining planar-overlap problem.

## 6. Verification artifact

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_root_shield_marked_halfplane.py
```

The verifier uses exact rational orientation arithmetic.  It checks every
subset in both halfplane banks of an eleven-vertex parabola polygon with an
interior marked point, and exhausts an abstract canonical-cell family to
verify the pair-decoder and high-profile multiplicity caps.
