# Heavy common-base completions: the exact source-downset bank

**Date:** 2026-08-14.  All logarithms are base two.  This is the follow-up
to `CIRCUIT_TRANSVERSAL_OR_OUTER_TOGGLE.md`.

## Verdict

The heavy middle-toggle fibre has a full Boolean multiplier which survives
variable repair alphabets.  If a cell has common base `B`, uniform
completions `Q`, one source label `x`, and `D` repair labels over every
completion, then

\[
 \{S\cup Q\cup\{y\}:S\subseteq B,\ Q\in\mathcal Q,
                              y\in Y_Q\}                    \tag{1}
\]

is an ordinary-face bank of exact incidence size
`2^|B| D |mathcal Q|`.  Globally, if `L` is its maximum face overlap, the
selected records obey

\[
                         |E|\le L2^{-|B|}V(P).               \tag{2}
\]

Thus `L<=2^|B|D^(1-epsilon)` closes fixed-power EIC'.  This is a permissive
threshold: at the seam `2^|B|` is already almost one full power of `D`.

There is also a zero-overlap **two-face** version.  Complementary subsets
of `B` give

\[
 (B,Q,x,y,S)\longmapsto
       (S\cup Q\cup\{x\},\ (B-S)\cup Q\cup\{y\}),            \tag{3}
\]

and the pair recovers `B,Q,x,y,S` exactly.  Hence

\[
                         2^{|B|}|E|\le V(P)^2.               \tag{4}
\]

Equation (4) removes *all* cross-base ambiguity, but by itself is only a
pair-capacity bound and does not imply the linear estimate required by
EIC'.  A collision square or a one-face overlap theorem is still needed.

For recursion, the Boolean bank can retain the source label rather than the
repair label.  Its unavoidable multiplicity `D` is explicit, but a heavy
output then fixes `x` and the rank-half completion family inherits all `D`
repairs.  This is the square-preserving version of the descent.

For the one-face bank, a heavy middle-layer output has an exact structural
consequence.  After only
`binom(floor(|B|/2)+q,q)` split ambiguity and the actual source multiplicity
over one repaired carrier, it fixes the completion `Q`, the retained
half-base `S`, and the repair label `y`, and produces many distinct
rank-`ceil(|B|/2)` completions `I=B-S` over that common rooted base.  Thus
the unresolved atom descends by a factor two in the *variable base rank*.

This is genuine progress but not a closure.  The sparse guard construction
realizes the heavy alternative at every scale: its bases are subsets of a
large convex lower cloud.  The downset overlap is enormous, while the
unrestricted Boolean complex of that same cloud pays EIC' with
double-exponential room.  Therefore no bound on `L` using only the ranks
and cardinalities can be true.  The remaining theorem must charge a heavy
common-prefix completion family to its unrestricted outer shield complex,
or preserve a collision square through the rank-halving descent.

## 1. Setup

Let `P=O disjoint_union X` be a labelled planar general-position set.  A
cell `c` consists of

* an ordinary base `B_c subset O` of rank `b`;
* a family `Q_c` of `q`-sets, disjoint from `B_c`;
* a source label `x_c in X`; and
* for every `Q in Q_c`, a set `Y_(c,Q) subset X` of exactly `D` labels.

Assume

\[
 B_c\cup Q\cup\{x_c\},\quad B_c\cup Q\cup\{y\}
       \in F(P)\qquad(Q\in Q_c,\ y\in Y_{c,Q}).              \tag{5}
\]

The record set is

\[
 E_c=\{(c,Q,x_c,y):Q\in Q_c,\ y\in Y_{c,Q}\},
 \qquad |E_c|=D|Q_c|.                                      \tag{6}
\]

The alphabets `Y_(c,Q)` may vary arbitrarily.  Only actual labelled records
are counted; if the same source appears in several syntactic cells, retain
one canonical occurrence or include the established context multiplicity
in the final overlap parameter.

For the heavy-fibre statement put

\[
 \Delta=\max_{B,Q,y}|\{c:B_c=B,\ Q\in Q_c,
                                  y\in Y_{c,Q}\}|.            \tag{6a}
\]

This is the number of actual source labels/histories which can sit over one
fixed repaired carrier `(B union Q,y)`.  It is one when the heavy layer has
already fixed the source label globally; otherwise it must be retained
explicitly (the simple cap gives only `Delta<=D`).

## 2. The one-face Boolean bank

> **Theorem 1 (source-downset bank).**  Define
> \[
> A_c=\{S\cup Q\cup\{y\}:S\subseteq B_c,
>                 Q\in Q_c,\ y\in Y_{c,Q}\}.                \tag{7}
> \]
> Then every member of `A_c` is an ordinary face, and the number of
> representations in (7) is exactly
> \[
>                         2^bD|Q_c|=2^b|E_c|.                \tag{8}
> \]
> If a fixed ordinary face has at most `L` representations across all
> cells, then (2) holds.

**Proof.**  Every set in (7) is a subset of the repair face
`B_c union Q union {y}` in (5).  Within a fixed representation the label
partition recovers `y`; the sets `S,Q` are disjoint, so varying `S` gives
exactly `2^b` occurrences per actual record.  Summing occurrences gives
(8).  At most `LV(P)` occurrences can land on ordinary faces, proving (2).
QED.

The word “representations” is deliberate.  Different base/completion
splits can give the same labelled face, and `L` measures exactly this
remaining ambiguity.

It is often useful to use only one layer.  Put `s=floor(b/2)` and

\[
 A_c^{(s)}=\{S\cup Q\cup\{y\}:S\in{B_c\choose s},
                    Q\in Q_c,\ y\in Y_{c,Q}\}.              \tag{9}
\]

If its maximum representation overlap is `L_s`, then

\[
                |E|\le {L_s\over {b\choose s}}V(P).         \tag{10}
\]

This form makes every heavy fibre uniform-rank.

## 3. Complementary halves give an exact global pair decoder

> **Theorem 2 (complementary-base pair injection).**  The map (3), over
> all cells, records, and subsets `S subseteq B_c`, is injective, after
> canonical deduplication of actual records.  Both coordinates are ordinary
> faces.  Consequently (4) holds.

**Proof.**  The first coordinate is a subset of the source face in (5), and
the second a subset of the repair face, so both are ordinary.  From the
ordered output pair `(F_0,F_1)`, the label partition gives `x` and `y`.
On outer labels,

\[
 Q=(F_0\cap F_1)\cap O,\qquad
 B=((F_0\cup F_1)\cap O)-Q,\qquad
 S=(F_0\cap O)-Q.                                           \tag{11}
\]

These recover the record and the Boolean codeword.  There are `2^b|E|`
inputs and at most `V(P)^2` ordered output pairs.  QED.

The theorem is the sharp cross-base Cauchy statement available from
heredity alone.  It cannot simply be converted from `V^2` to `V`: doing so
would require control of the two coordinate projections, precisely the
overlap problem in Theorem 1.

There are two useful coordinate projections of (3).  The repair projection
is (9).  The **source projection**, counted as an occurrence multiset, is

\[
 X_c^{(s)}=\{S\cup Q\cup\{x_c\}:S\in{B_c\choose s},
          Q\in Q_c,\ y\in Y_{c,Q}\}.                         \tag{11a}
\]

Each labelled source downface occurs once for every one of its `D` repair
labels.  Let `L_s^x` be the maximum occurrence load of one ordinary face in
these multisets.  The same double count gives

\[
                 |E|\le {L_s^x\over {b\choose s}}V(P).       \tag{11b}
\]

Unlike the repair projection, a heavy member of (11a) contains and hence
fixes the source label `x`.  This distinction is load-bearing in an
iteration.

## 4. Exact structure of a heavy middle-layer fibre

Assume all cells have the same `b,q`.  Let a face `U` have `L_U`
representations in (9).  Its internal label determines `y`.  Its outer part
has rank `s+q`.

> **Theorem 3 (heavy overlap descends the variable base).**  Some
> `q`-subset `Q subset U cap O` and its complement
> `S=(U cap O)-Q` occur in at least
> \[
>                    {L_U\over {s+q\choose q}}               \tag{12}
> \]
> representations.  For those representations, the missing sets
> \[
>                         I_c=B_c-S                           \tag{13}
> \]
> contain at least
> \[
>                 {L_U\over\Delta {s+q\choose q}}             \tag{13a}
> \]
> distinct members, all of the common rank `b-s=ceil(b/2)`, and satisfy
> \[
>              S\cup Q\cup I_c\cup\{y\}\in F(P).            \tag{14}
> \]
> Thus they are uniform completion faces over the common rooted base
> `S union Q union {y}`.

**Proof.**  There are at most `binom(s+q,q)` ways to identify the full
completion `Q` inside `U cap O`; this fixes `S`.  Pigeonhole gives (12).
Equation (14) is the repair face from (5).  For fixed `Q,S,y`, a fixed base
`B` can occur in at most `Delta` cells by (6a).  Dividing the representation
count by `Delta` therefore gives (13a) distinct missing completions.  Their
rank is fixed by `|B_c|=b`, proving the claim.  QED.

For the heavy matching atom of the preceding note, `q=O(gamma log D)` and
`b` is the remaining source rank.  The split cost in (12) is

\[
 \log {s+q\choose q}
      \le q\log\!\left({e(s+q)\over q}\right),               \tag{15}
\]

which is only `O(gamma log(1/gamma) log D)` bits when `q/b=O(gamma)`.
Thus a small matching coefficient makes the rank-halving child retain a
fixed-power fraction of the heavy overlap.  What is not yet proved is a
global square-preserving summation of these children.

There is an exact source-preserving counterpart.  Let

\[
 \Sigma_x=\max_{B,Q,x}|\{c:B_c=B,\ Q\in Q_c,\ x_c=x\}|       \tag{15a}
\]

be the syntactic context multiplicity of one actual source.  If an ordinary
face `U` has occurrence load `L_U^x` in (11a), then after fixing one of at
most `binom(s+q,q)` splits `U cap O=S disjoint_union Q`, it yields at least

\[
              {L_U^x\over D\Sigma_x {s+q\choose q}}          \tag{15b}
\]

distinct rank-`ceil(b/2)` sets `I=B-S` such that

\[
                 S\cup Q\cup I\cup\{x\}\in F(P),            \tag{15c}
\]

and every displayed source retains its original `D`-element repair alphabet.
The factor `D` in (15b) is exact: it is the deliberate repetition over
`y in Y_(c,Q)` in (11a), not an untracked congestion loss.  Thus
(15b)--(15c) is the correct rank-half child for a collision-preserving
telescope.

## 5. Why an overlap-only closure is false

Use the scalable sparse construction in
`../agent_outer_internal_product/OUTER_INTERNAL_MIXED_BANK.md`.  Its outer
labels `Z` are in convex position, its carriers are fixed-rank subsets of
`Z` containing the guard data, and its source/repair labels form a strict
insertion chain.  For a fixed small output `S union Q union {y}`, the number
of carrier bases extending `S` contains a binomial factor

\[
                         { |Z|-|S|-|Q| \choose b-|S|}.        \tag{16}
\]

This can be `D^(Theta(log D))`, far above the threshold in (2).  Hence
`L` is not bounded by a fixed power from ranks alone.

Nevertheless `Z` is convex, so all `2^|Z|` subsets are ordinary faces and
pay the selected records with enormous room.  The example is not an EIC'
counterexample.  It proves that the correct completion of Theorem 3 must be

\[
 \boxed{\text{light source-downset overlap, or charge the heavy
 common-prefix completion family to its unrestricted outer shield.}}    \tag{17}
\]

The first branch is (10); the exact rank-half child in the second branch is
(12)--(14).

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_heavy_common_base.py
```

The checker exhausts finite abstract cells to verify (8), (10)--(14),
constructs the complementary decoder and reverses every output pair, and
uses exact rational sparse-chain coordinates to verify every source and
repair face in a nontrivial common-base completion family.
