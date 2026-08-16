# Common-base completions: central shadows, hybrid overlap, and the exact residue

**Date:** 2026-08-14.  All logarithms are base two.  This note continues
`CIRCUIT_TRANSVERSAL_GUARD_RELEASE.md` at its high-toggle-overlap child.

## Verdict

There is an exact rank-halving theorem for the remaining common-base
completion family.  It is important to use a fixed central layer, rather
than the full Boolean downset: the empty toggle has automatic maximal
overlap and contains no information.

For an atomic cell `(B,Q,Y_Q)`, put `|B|=b`, `|Y_Q|=D`, and assume

\[
                 B\cup Q\cup\{y\}\in\mathcal F(P)
                         \qquad(y\in Y_Q).                    \tag{1}
\]

If `s=floor(b/2)`, deletion gives the central source-downshadow bank

\[
 \mathcal A_{B,Q}=\{S\cup Q\cup\{y\}:
                S\in{B\choose s},\ y\in Y_Q\},\qquad
 |\mathcal A_{B,Q}|=D{b\choose s}.                           \tag{2}
\]

Together with an `H`-face internal reservoir `\mathcal J_Q`, the exact
recoverable-cell estimate is

\[
 |E|\le D^{3/2}
       \sqrt{\frac{\Lambda_A\Lambda_J}{{b\choose s}H}}\,V(P).
                                                                    \tag{3}
\]

Here every atomic cell carries `D^2` records, and `Lambda_A,Lambda_J` are
the global overlaps of the two banks.  Thus this branch has a
`D^epsilon` saving whenever

\[
       {b\choose s}H\ge
       \Lambda_A\Lambda_J D^{1+2\epsilon}.                  \tag{4}
\]

Heavy overlap in (2) has a canonical geometric meaning.  A common output
fixes an ordinary outer prefix `P_0` and one label `y`; the erased
complements have uniform rank `ceil(b/2)`.  More importantly, **all `D`
one-point extensions survive**, even when the sets `Y_Q` vary with `Q`.
So the heavy child is another instance of the same problem at half the
free rank, over a larger common prefix.  This is a genuine first-divergence
descent, not merely a cardinality reduction.

Two terminal branches can now be closed.

* A completion family of size at most `H_D/D^(1+epsilon)` is absorbed at
  the desired fixed-power scale by the universal `D`-point face reservoir
  `H_D` (and `H_D/D^2` gives the stronger congestion-one bound).
* If a rank-`q` completion family is complete, or misses fewer than a
  `((q-3)/m)^4` fraction of all `q`-sets on an `m`-point ground cloud, the
  cloud is convex by the planar four-point certificate.  For
  `4<=q<=(1/2)log D`, that outer Boolean shield together with `H_D`
  pays `D^2` records per completion, with congestion one for all large
  `D`.
* More generally, compatible *pairs* of completions have a union-face bank
  of load at most `3^(2q)`.  Hence failure of the fixed-power estimate lets
  us retain half of a hard family so that every completion is compatible
  with only `D^(O(1))` others.  Almost every surviving pair must have a
  cross four-circuit.

This does **not** close the arbitrary-family child.  The exact residue is a
quadratic-entropy, far-from-complete, rank-`O(log D)` completion family
whose central-shadow banks have high contextual overlap at every
rank-halving scale.  Kruskal--Katona cardinalities alone do not settle it,
and separate large maxima `Lambda_A,Lambda_J` do not force an aligned
common prefix and common internal shield.  Both overstrong inferences have
explicit set-system counterexamples below.  No scalable planar
counterexample to the desired fixed-power theorem is obtained.

## 1. Atomic central-shadow bank

Write the ambient labels as `O disjoint_union X`.  In an atomic cell let

\[
 B,Q\subseteq O,\quad B\cap Q=\varnothing,\qquad
 Y_Q\subseteq X,\quad |Y_Q|=D,                              \tag{5}
\]

and assume (1).  The cell represents `D^2` selected records.  The precise
origin of the second `D` is irrelevant for this lemma.

> **Theorem 1 (central source-downshadow bank).**  For every
> `0<=s<=b`, all members of `\mathcal A_{B,Q}` in (2) are ordinary faces,
> and
> \[
>                   |\mathcal A_{B,Q}|=D{b\choose s}.        \tag{6}
> \]
> For any family `I` of atomic cells, if one ordinary face lies in at most
> `Lambda_A` central banks, then
> \[
>       |I|D^2\le {D\Lambda_A\over {b\choose s}}V(P).        \tag{7}
> \]

**Proof.**  Every set in (2) is obtained from a source face in (1) by
deletion.  The partition `O disjoint_union X` recovers `y`, while the
disjoint decomposition `B disjoint_union Q` inside one cell makes the
choices of `S` distinct.  This proves (6).  Double-counting bank
incidences gives

\[
       |I|D{b\choose s}\le\Lambda_A V(P),                   \tag{8}
\]

which is (7).  QED.

Taking a central layer prevents the vacuous collision shared by every
full downset bank at `S=emptyset`.  It also loses only a polynomial factor:

\[
            {b\choose\lfloor b/2\rfloor}\ge {2^b\over b+1}. \tag{9}
\]

## 2. Hybrid with the internal reservoir

For every atomic cell choose a family `\mathcal J_Q` of exactly `H`
ordinary faces contained in its selected `D`-label cloud.  Such a family
is supplied by the established universal blocker-neighbourhood reservoir;
the theorem below only uses its cardinality.  Let

\[
 \Lambda_J=\max_F|\{(B,Q):F\in\mathcal J_Q\}|.              \tag{10}
\]

> **Theorem 2 (central-shadow/internal-reservoir Cauchy).**  For atomic
> cells of common base rank `b`, with `s=floor(b/2)`,
> \[
> |E|\le D^{3/2}
>       \sqrt{\frac{\Lambda_A\Lambda_J}{{b\choose s}H}}\,V(P).
>                                                                    \tag{11}
> \]
> In particular (4) implies `|E|<=D^(1-epsilon)V(P)`.

**Proof.**  In one cell, with `a={b\choose s}`,

\[
 D^4={D^3\over aH}\,(Da)H
     ={D^3\over aH}|\mathcal A_{B,Q}||\mathcal J_Q|.        \tag{12}
\]

Sum square roots, apply Cauchy--Schwarz, and use

\[
 \sum|\mathcal A_{B,Q}|\le\Lambda_A V(P),\qquad
 \sum|\mathcal J_Q|\le\Lambda_J V(P).                     \tag{13}
\]

This proves (11); (4) is immediate.  QED.

The banks in Theorem 2 are deliberately separate.  It is not asserted
that a central outer face coexists with an arbitrary internal reservoir
face.  That stronger mixed-face statement is exactly the geometric issue
in the residual branch.

## 3. What a heavy central collision retains

The high-overlap alternative has more structure than an unspecified large
fibre.

> **Theorem 3 (common-prefix rank-halving child).**  Suppose one face `F`
> belongs to the central banks of `k` atomic cells.  For each incidence
> write
> \[
> F=P_0\cup\{y\},\qquad P_0=S\cup Q,\qquad
> C=B-S.                                                     \tag{14}
> \]
> Then `P_0` and `y` are common throughout the fibre,
> `|C|=b-s`, and
> \[
>             P_0\cup C\cup\{y'\}\in\mathcal F(P)
>                        \qquad(y'\in Y_Q).                  \tag{15}
> \]
> If an ordinary source face is represented in at most `mu` atomic cells,
> the fibre contains at least `k/mu` distinct completions `C`.

**Proof.**  The `X`-part of `F` is the singleton `y`, and its `O`-part is
the common set `P_0`.  Since `S subseteq B` and `B cap Q=emptyset`, the
erased complement has size `b-s`.  Finally

\[
 P_0\cup C\cup\{y'\}
   =S\cup Q\cup(B-S)\cup\{y'\}
   =B\cup Q\cup\{y'\},                                    \tag{16}
\]

which is a source face by (1).  For fixed `F`, equal completions give equal
source faces, so quotienting by source multiplicity proves the last claim.
QED.

Thus `P_0` is a released common outer shield (all of its subsets are
ordinary), while the `C`'s are a uniform completion fan over it.  The
critical point in (15) is that the collision selected only one `y`, but
did not destroy the other labels in `Y_Q`.  Treating each `C` as the new
free base and `P_0` as the retained part repeats Theorem 3 with free rank
`ceil(b/2)`.  Any global use of this recursion must carry normalized
first-divergence weights; selecting one heavy child at every level would
lose its mass.

## 4. Source-cloud cutoff and a complete-family terminal theorem

Let `H_D` be a number such that every `D`-point planar set has at least
`H_D` ordinary convex subsets.  The established reservoir estimate permits

\[
                    H_D\ge2^{(\log D)^2/8}                  \tag{17}
\]

for all sufficiently large `D` (the available asymptotic coefficient is
larger than `1/8`).  Choosing any one `Y_Q` gives `V(P)>=H_D`.

> **Lemma 4 (source-cloud cutoff).**  A completion family of size `M`
> carrying `D^2` records per completion satisfies the desired
> `D^epsilon` saving whenever
> \[
>                            M\le H_D/D^{1+\epsilon}.         \tag{18}
> \]
> If `M<=H_D/D^2`, the stronger bound `D^2M<=V(P)` holds.

Indeed (18) gives `D^2M<=D^(1-epsilon)H_D<=D^(1-epsilon)V(P)`;
the second assertion is immediate as well.  Hence only a genuinely
quadratic-entropy completion family survives.

There is also a geometric terminal branch.  Let `Z` be an `m`-point outer
cloud disjoint from `P_0`, let `\mathcal Q subseteq {Z\choose q}`, `q>=4`,
and suppose

\[
       P_0\cup Q\cup\{y\}\in\mathcal F(P)
          \qquad(Q\in\mathcal Q,\ y\in Y_Q),                \tag{19}
\]

where every `Y_Q` has size `D`.

> **Theorem 5 (dense completion family releases the full outer shield).**
> Put
> \[
>       \eta=1-{|\mathcal Q|\over {m\choose q}}.
> \]
> If
> \[
>                    \eta<\left({q-3\over m}\right)^4,      \tag{20}
> \]
> then `Z` is in convex position.  Consequently
> `V(P)>=max(2^m,H_D)`.
>
> If in addition `d=log D`, `4<=q<=d/2`, (17) holds, and `d` is
> sufficiently large, then
> \[
>             D^2|\mathcal Q|\le V(P).                      \tag{21}
> \]
> One explicit sufficient asymptotic range for the elementary estimates
> below is `d>=404`.

**Proof.**  If a four-set `T subseteq Z` were not contained in any member
of `\mathcal Q`, all of its
`{m-4\choose q-4}` extensions would be missing.  Their fraction is

\[
 { {m-4\choose q-4}\over {m\choose q}}
   ={(q)_4\over(m)_4}
   \ge\left({q-3\over m}\right)^4,                          \tag{22}
\]

contrary to (20).  Thus every four-set lies in some `Q`; deletion in
(19) makes it convex.  The planar four-point certificate makes all of `Z`
convex, proving the first assertion.

It remains to check that the two unrestricted banks pay the formal record
count.  Put `M_0={m\choose q}`.  We claim

\[
                       \max(2^m,H_D)\ge D^2M_0.              \tag{23}
\]

Suppose first that `2^m<D^2M_0`.  Using
`M_0<=(em/q)^q` and `q<=d/2` gives

\[
             m<2d+{d\over2}\log(em).                        \tag{24}
\]

With `L=log(4ed)`, the right side of (24) is already below `m`
at `m=4dL`, and its derivative is below one thereafter.  Hence

\[
                         m<4d\log(4ed).                      \tag{25}
\]

For `d` satisfying

\[
              {d\over8}\ge2+4\log(4ed),                    \tag{26}
\]

which holds for `d>=404`, equations (17) and (25) give
`H_D>=D^2M_0`.  This proves (23).  Since
`|\mathcal Q|<=M_0`, (21) follows.  QED.

The numerical constant `404` is immaterial; Theorem 5 is an asymptotic
statement.  Its point is that there is no intermediate gap.  If the outer
cloud is small, the family has only `2^{o((log D)^2)}` members and the
`D`-point reservoir pays.  If the cloud is large, its Boolean shield pays.

## 5. Compatible-pair multiplication leaves an almost-antichain

The dense-layer hypothesis can be replaced by a direct geometric pair
test.  Let `\mathcal C` be `M` distinct rank-`q` completions over one
common face `P_0`, so `P_0 union C` is ordinary for every
`C in \mathcal C`.  Call an ordered distinct pair `(C,C')` compatible if

\[
                         P_0\cup C\cup C'\in\mathcal F(P),  \tag{27}
\]

and let `E_+` be the number of compatible ordered pairs.

> **Theorem 6 (compatible-pair union bank).**
> \[
>              V(P)\ge {E_+\over3^{2q}}.                   \tag{28}
> \]
> Consequently, for a family carrying `D^2M` records,
> \[
>       E_+\ge3^{2q}D^{1+\epsilon}M                         \tag{29}
> \]
> implies `D^2M<=D^(1-epsilon)V(P)`.
>
> If (29) fails, a subfamily of size at least `M/2` has maximum
> compatible degree less than
> \[
>                         2\,3^{2q}D^{1+\epsilon}.           \tag{30}
> \]

**Proof.**  Map a compatible pair to the face in (27).  For a fixed output
face, every label outside `P_0` is in the first completion only, the second
only, or both.  There are at most `3^(2q)` ordered descriptions, proving
(28).  Equation (29) then gives the desired estimate.  If (29) fails, the
average compatible degree is below the right side of (29) divided by `M`,
namely `3^(2q)D^(1+epsilon)`.  At least half the vertices have degree below
twice that quantity, and their induced subgraph has no larger degrees.
QED.

In the hard branch `M>H_D/D^(1+epsilon)=2^{Omega((log D)^2)}` while
`q=O(log D)`.  The bound (30) is only a fixed power of `D`.  Thus after a
constant thinning, almost every ordered pair is incompatible.  For any
such pair, a bad four-circuit in its union must meet both
`C-C'` and `C'-C`; otherwise it would lie in one of the two source faces.
This is the exact cross-circuit input still available in the residual.

## 6. Why Kruskal--Katona alone does not finish the descent

Kruskal--Katona says that if
`|\mathcal Q|={x\choose q}` in generalized-binomial notation, then

\[
                    |\partial_s\mathcal Q|\ge{x\choose s}.  \tag{31}
\]

This correctly estimates the number of *distinct* central outputs.  It
does not provide a fixed-power multiplier for an arbitrary family.  Take

\[
                 \mathcal Q={ [2q]\choose q}.               \tag{32}
\]

Its full downclosure satisfies

\[
 { |\Delta\mathcal Q|\over|\mathcal Q|}
   ={\sum_{i=0}^q{2q\choose i}\over{2q\choose q}}
   \le q+1.                                                  \tag{33}
\]

At `D=2^q`, this is smaller than `D^epsilon` for every fixed positive
`epsilon` and all large `q`.  Thus “the Boolean completion bank always
expands by a fixed power” is false even for the KK extremizer.

This example is not a geometric counterexample.  It has only
`|\mathcal Q|<=D^2`, so the source-cloud cutoff absorbs it; and when all
members in (28) occur geometrically, Theorem 5 releases the entire
`2q`-point outer shield.

## 7. Separate heavy overlaps need not align

There is a second tempting but false inference from Theorem 2:

> large `Lambda_A` and large `Lambda_J` force many cells sharing both one
> central prefix and one internal shield.

As an abstract incidence statement this fails maximally.  Take a central
cell `0`, `k` A-leaves, and `k` J-leaves.  Let cell `0` use `(a_*,j_*)`.
Every A-leaf uses `a_*` and a private `j_i`; every J-leaf uses a private
`a_i` and `j_*`.  Then

\[
                      \Lambda_A=\Lambda_J=k+1,               \tag{34}
\]

but every pair `(a,j)` has common-cell multiplicity one.  Tensoring with
private dummy outputs equalizes bank sizes without changing this fact.

Therefore the product of the two **maximum** overlaps is a valid numerical
upper bound in (11), but failure of (4) does not by itself extract an
aligned common-prefix/common-shield subfamily.  A positive global theorem
must use one of:

1. a one-face geometric splice of the two outputs;
2. a codegree or dependent-overlap estimate inside each heavy central
   fibre; or
3. normalized first-divergence weights which sum the rank-halving tree
   without selecting unrelated maximum fibres.

The sparse guard-pair construction from
`OUTER_INTERNAL_MIXED_BANK.md` is consistent with this boundary: its
central overlap is maximal, but its full outer cloud is convex, so it exits
through Theorem 5 rather than refuting the desired theorem.

## 8. Exact remaining theorem

After the proved reductions, the unresolved statement can be isolated as
follows.

> **Completion-bank overlap target.**  In the weighted rank-halving tree
> generated by Theorem 3, for a quadratic-entropy family of distinct
> rank-`O(log D)` completions, either the central source-downshadow and
> internal-reservoir banks satisfy (4) in aggregate, or a heavy aligned
> fibre releases `D^epsilon` ordinary mixed/outer-shield faces per unit
> source mass.

Theorem 5 proves this target for complete and exponentially-near-complete
uniform families.  Theorem 6 reduces the other hard families to an
almost-pairwise-incompatible cross-circuit system.  Equations (33)--(34)
show why neither shadow cardinality nor unrelated overlap maxima prove it
in general.  Thus the present report is a rigorous conditional advance,
not a complete proof of EIC'.

The follow-up `PAIRWISE_INCOMPATIBLE_COMPLETION_REGRESSION.md` pursues this
last system.  It extracts a fixed-power bad-pair sunflower, and gives a
scalable planar nested-ear product showing that the sunflower/circuit
container can still be quadratic-entropy.  Its payment comes from detached
outer chain shields, not from the common-base joined complex.

## 9. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_common_base_completion_shadow.py
```

The checker exhausts small uniform families for the central-shadow
incidence identity and rank-halving fibres, audits the exact integer form
of (11), checks the dense four-cover threshold, verifies the explicit
outer-shield/source-cloud dichotomy, and constructs both obstruction
set-systems (29)--(30).
