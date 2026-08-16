# Layered insertion chains: exact quadratic label loss after rank collapse

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

The proposed mixed light/heavy shortcut is false without an additional
progress invariant.  A protected prefix can be fixed once, the residual
rank can collapse all the way to one, and nevertheless the same prefix can
support `Theta(L)` successive comparable replacement layers.  The layers
carry `Theta(L^2)` independent label bits, while two protected-prefix
shadow faces and the complete polynomial/factorial reverse transcript carry
only `O(L log L)` extra bits.

This is a stretchable planar obstruction, not merely an abstract support
graph.  It already occurs in one fixed insertion edge, so allowing adjacent
edge switches or recording their `3^r` root-walk transcript cannot repair
it.  What fails is repeated use of the **same** Boolean prefix bank: the
`2^k` downfaces of one prefix are a global pool, not a fresh factor at every
comparable descent.

The construction does not disprove Erdős 838.  In the explicit rational
audit the individual clouds were chosen on short convex arcs, so their
internal face complexes are in fact enormous.  More generally one may put
an arbitrary order type into a chain cell, but then using its additional
ordinary faces is exactly the original Erdős 838 problem recursively.  The
construction does rigorously kill the inference

```text
heavy atom -> rank k becomes sqrt(k) -> one-sided history is cheap,
```

and the stacked-compatibility/handoff argument when its final outputs are
the protected-prefix shadows certified by Theorem 31.

## 1. A complete layered replacement chain

Let `F={f_1,...,f_k}` be a convex `k`-gon with a distinguished upper edge
`uv`.  For example, take the rational points

\[
 f_i=(x_i,x_i^2-1),\qquad
 x_i=-1+{2(i-1)\over k-1}.                              \tag{1}
\]

Thus `u=(-1,0)`, `v=(1,0)`, and every other vertex lies strictly below
`uv`.  Above `uv`, choose disjoint rational clouds

\[
                         Q_0,Q_1,\ldots,Q_{h-1},
 \qquad |Q_j|=q,                                      \tag{2}
\]

with `Q_j` in a sufficiently small neighbourhood of `(0,2^j)`.  The
neighbourhoods may be chosen so that, for every `x in Q_j` and
`y in Q_{j+1}`,

\[
                         x\in\operatorname{int}\operatorname{conv}\{u,y,v\}.
                                                               \tag{3}
\]

Indeed the horizontal cross-section of the triangle
`conv{u,(b,H),v}` at height `s<H` has centre `bs/H` and half-width
`1-s/H`; for consecutive heights close to `2^j,2^(j+1)` this half-width is
close to `1/2`.  Small boxes about the displayed centres therefore satisfy
(3) uniformly.  All required inequalities are strict, so the points can
be chosen rationally and in general position.

Every set `F+x`, `x in Q_j`, is a convex face.  Equation (3) gives the
exact replacement relation

\[
 \operatorname{ext}(F\cup\{x,y\})=F\cup\{y\}
       \quad(x\in Q_j,\ y\in Q_{j+1}).              \tag{4}
\]

Consequently every word

\[
                         \omega=(x_0,\ldots,x_{h-1})
                   \in Q_0\times\cdots\times Q_{h-1}       \tag{5}
\]

is a valid monotone exterior-repair history

\[
 F+x_0\longrightarrow F+x_1\longrightarrow\cdots
        \longrightarrow F+x_{h-1}.                         \tag{6}
\]

The active insertion edge is always `uv`; the whole `k`-vertex prefix is
protected and every residual child has rank one.  There are exactly `q^h`
histories.

## 2. Protected shadows have a quadratic inverse fibre

Let `U` be the entire pool of faces obtainable by retaining an arbitrary
downface of the protected prefix and at most one currently visible chain
tip:

\[
 U=2^F\ \cup\
   \{D\cup\{x\}:D\subseteq F,\ x\in Q_j,\ 0\le j<h\}.       \tag{7}
\]

All members of `U` are ordinary convex faces by heredity of `F+x`, and

\[
                         |U|\le 2^k(1+hq).                   \tag{8}
\]

This pool generously contains every same-edge protected-prefix output of
the weighted-shadow recursion, at every codimension and every layer.

> **Theorem 1 (layered-chain label-loss bound).**  Every map from the
> histories (5) to an ordered pair of faces in `U^2` has maximum fibre at
> least
> \[
> \boxed{
> {q^h\over 2^{2k}(1+hq)^2}.}                               \tag{9}
> \]
> If the decoder is also given one of `T` transcript values, the lower
> bound is divided by at most `T`.

**Proof.**  There are `q^h` inputs and at most `|U|^2` output pairs.  Apply
the pigeonhole principle and (8).  Adding a transcript simply multiplies
the range by `T`.  QED.

Take

\[
                         k=h,\qquad q=2^h.                  \tag{10}
\]

The ambient size is `n=k+hq=2^{h+o(h)}`, so `L=log n=h+o(h)` and the active
rank is `k+1=Theta(L)`.  Even before transcript costs, (9) has logarithm

\[
 h^2-2h-2\log(1+h2^h)
                  \ge h^2-4h-2\log(h+1).                   \tag{11}
\]

Allow the complete reverse-transcript budget from the global decoder,

\[
 T_h=(h!)^2\{8(h+1)^4\}^h.                                  \tag{12}
\]

Then `log T_h=O(h log h)=o(h^2)`, so (9) remains

\[
                         2^{(1-o(1))h^2}.                    \tag{13}
\]

In particular, neither superfast residual-rank collapse, protected-frame
recovery, chronology guesses, nor the exact same-edge handoff
`Q_j -> Q_(j+1)` gives a coefficient-scale label-faithful decoder.

## 3. Exact gap in the mixed light/heavy proposal

Suppose the light side of a two-history pair is routed to and frozen in its
first output.  The heavy side fixes the prefix `F` and descends to the
rank-one chain (6).  It now has only the second output available.
Equation (7) is more generous than that one-output allowance because
Theorem 1 grants **two** protected-shadow outputs to the heavy history.  Yet
its inverse fibre is still (13).  Therefore freezing the light output and
recursing only the heavy side cannot be justified from Theorem 31 plus rank
collapse.

The failure is not the `Lambda` estimate and not root recovery.  At each
individual layer the endpoint and successor alphabets both have size `q`,
the handoff multiplicity is one, and the frame is fixed.  The failure is
stacked compatibility: for `x in Q_j,y in Q_(j+1)`, (4) says that no face
retaining `F` can retain both tips.  Hence the same `2^k` prefix downfaces
cannot be multiplied once per level.  Across the complete history they are
available only once, as counted in (8).

An edge switch can only make this worse.  If switches erode protected
labels, the `3^k` root-walk word records which ends and lengths were erased,
but not the identities of quadratically many intermediate tips.  Since
(13) already holds with zero switches, root-walk control is orthogonal to
the missing label capacity.

## 4. Consequence for the `3/4`-support bypass

The same example audits the proposed use of the universal
`log V >= (2/3)log m-O(log K)` repair-support theorem.  The `q^h` composite
histories are not edges of a simple repair graph whose two endpoints are
ordinary faces: projecting a history to any protected start/end shadow has
the quadratic multiplicity (13).  Treating the history word itself as an
endpoint violates the face hypothesis, while treating every transition as
a separate edge destroys the cumulative `h log q` entropy.  Thus baseline
face entropy plus the formal sum of per-level blocker entropies does **not**
canonically produce a `3L^2/4` simple face-to-face repair support.

Any successful `3/4` bypass must add a planar theorem that converts a
positive fraction of the intermediate comparable tips into ordinary faces
outside the repeated rooted-shadow pool (7), and must re-establish a
cross-source decoder for rectangles in that composite support.

## 5. The decisive two-output calculation is equivalent to Erdős 838

The failure above is genuinely one-slot/protected-shadow failure.  It
cannot be strengthened to a cardinality obstruction against **all** pairs
of ordinary faces without solving the original problem in the negative.

Use the projective insertion-chain universality theorem to put an arbitrary
`N`-point planar order type `Q` into one fixed insertion edge, and adjoin a
fixed outer base and a common final tip.  Every `h`-subset of the chain,
read in its forced order, is a valid same-edge repair history.  Thus the
history bank has size

\[
                              \binom Nh.                    \tag{14}
\]

The ambient face complex differs from that of `Q` by only a constant
factor:

\[
                         V(P)\le 2^{O(1)}V(Q).               \tag{15}
\]

This is proved in
`../agent_recursive_pocket_induction/LONG_CHAIN_MIXED_BRANCH_BARRIER.md`
and checked there with exact rational coordinates.

Suppose that the desired cross-level theorem routed all histories (14) to
two arbitrary ordinary faces with fibre `K=2^{o(L^2)}`, where
`L=log N`.  Then

\[
 \binom Nh\le K V(P)^2\le K2^{O(1)}V(Q)^2.                  \tag{16}
\]

Taking `h=floor(L)` gives

\[
 \log\binom Nh=L^2-O(L\log L),                              \tag{17}
\]

and hence

\[
                         \log V(Q)\ge(1/2-o(1))L^2.          \tag{18}

This is precisely the missing lower coefficient for arbitrary `Q`.
Conversely, (18) gives enough **cardinality** for an enumerative map of the
history bank into face pairs with subquadratic fibre.  Therefore the
unrestricted two-output capacity statement for a universal insertion chain
is coefficient-scale equivalent to Erdős 838; insertion-chain geometry has
not simplified it.

On the explicit sharp directional-blow-up configurations,

\[
 \log V(Q)=(1/2+o(1))L^2,\qquad
 \log\binom N{\lfloor L\rfloor}=(1-o(1))L^2,                \tag{19}
\]

so the two-face pool is exactly large enough in leading exponent.  This
answers the extra-face audit: one protected-shadow slot is deficient by
`(1/2-o(1))L^2` bits, while two unrestricted face slots saturate the
history chronology.  A successful proof must exploit those two slots
jointly; a stronger scalable obstruction would itself amount to a
sub-half construction.

There is likewise no automatic "large cloud" induction shortcut.  If a
chain uses at most `h=(alpha+o(1))L` tips from a union of
`n^(beta+o(1))` possible labels, its history entropy can be
`(alpha beta-o(1))L^2`.  Even granting coefficient one half inductively
inside that union supplies only `(beta^2/2-o(1))L^2` face bits per slot.
The deficit `alpha beta-beta^2/2` is positive throughout the critical
range `alpha=1,0<beta<=1`.  Thus a cloud need not be almost spanning for
the one-slot failure to remain quadratic.  The exact entropy law and its
sharp universal-chain realization are also banked in the referenced
mixed-branch barrier.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_label_faithful_decoder/verify_layered_chain_label_loss.py
```

The checker constructs rational general-position instances, verifies (3)
and (4) exactly for every adjacent cloud pair, and audits the integer fibre
bound (9), including the transcript factor (12), at growing symbolic
critical parameters.
