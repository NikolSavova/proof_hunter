# Commutator stability for eight corner matchings

## 1. Outcome

The exhaustive translation audit applies when the eight corner matchings
commute.  This note gives an exact stability reduction from arbitrary
edge-disjoint perfect matchings to that abelian branch.

Let `X` be a finite set of relation records and let

\[
 \tau_0,\ldots,\tau_7:X\to X
\]

be fixed-point-free involutions.  In the corner application, `tau_epsilon`
pairs two records having the same `epsilon`-corner key.  Distance-Sidon
linearity makes the eight matching edge sets disjoint.

Define the commutator-defect set

\[
 B=\{x\in X:\tau_i\tau_jx\ne\tau_j\tau_ix
        \text{ for some }i<j\}.                 \tag{1.1}
\]

**Theorem 1.1 (exact eight-involution stability).**  There is an invariant
set `G subseteq X` such that

\[
 |X\setminus G|\le256|B|,                       \tag{1.2}
\]

and `G` is a disjoint union of orbits on which all eight involutions
commute.  Every such orbit is an elementary abelian translation system
`F_2^m`, `m<=8`.  If the matchings are fixed-point-free and edge-disjoint,
their eight shifts on every orbit are distinct and nonzero.

Thus a full corner core has the exact structural alternative

\[
 \boxed{|X|\le256|B|+|G|,}                     \tag{1.3}
\]

where every record counted by `G` lies in a bounded abelian orbit.

The exact partition closure in
`NONGENERIC_TRANSLATION_CORE_OBSTRUCTION.md` now rules out every stable
orbit in a distance-Sidon realization, including arbitrary additional
endpoint identifications.  Consequently the alternative sharpens to

\[
 \boxed{|X|\le256|B|}                           \tag{1.4}
\]

whenever the eight involutions are fixed-point-free, edge-disjoint corner
matchings on genuine distinct transverse relations.

This does not yet bound `B` by the required cubic size-biased budget.  It
does remove the second, nongeneric stable-orbit charge entirely: the
remaining full-core problem is to charge commutator defects alone.

## 2. Proof of the stability theorem

For `epsilon in F_2^8`, apply the selected generators in increasing order
and write the resulting canonical word as

\[
 w_\epsilon=\tau_7^{\epsilon_7}\circ\cdots\circ
              \tau_1^{\epsilon_1}\circ\tau_0^{\epsilon_0}. \tag{2.1}
\]

Put

\[
 C=\bigcup_{\epsilon\in\mathbb F_2^8}w_\epsilon^{-1}(B).
                                                               \tag{2.2}
\]

Every canonical word is a bijection, so

\[
 |C|\le2^8|B|=256|B|.                           \tag{2.3}
\]

Take `x notin C`.  Every canonical point `w_epsilon x` lies outside `B`.
At those points adjacent generators commute.  Moving one generator through
a canonical word, one adjacent swap at a time, therefore gives

\[
 \tau_iw_\epsilon x=w_{\epsilon+e_i}x.          \tag{2.4}
\]

It follows that

\[
 O_x=\{w_\epsilon x:\epsilon\in\mathbb F_2^8\} \tag{2.5}
\]

is invariant under every generator.  Equation (2.4) also shows that every
canonical word based at any member of `O_x` remains in `O_x` and avoids
`B`; hence `O_x subseteq X\setminus C`.  The sets (2.5) partition
`G=X\setminus C`.

The map `epsilon -> w_epsilon x` factors through a linear stabilizer in
`F_2^8`, so `O_x` is a quotient `F_2^m`.  The generator `e_i` is zero in
the quotient exactly when `tau_i` has a fixed point on the orbit.  Two
generator images agree exactly when `tau_i x=tau_j x`, meaning the two
matching colours use the same edge.  The fixed-point-free and edge-disjoint
hypotheses therefore give eight distinct nonzero translation shifts.  This
proves the theorem.

## 3. Exact controls

`verify_corner_matching_commutator_stability.py` checks the construction on
three deterministic 64-record systems.

| system | `|B|` | `|C|` | stable orbit sizes |
|---|---:|---:|---:|
| commuting translation core | 0 | 0 | 64 |
| one admissible two-edge switch | 32 | 64 | none |
| fixed-seed random matchings | 64 | 64 | none |

The first row checks recovery of the full elementary-abelian orbit.  The
single local switch already contaminates the whole 64-record system, which
explains why the factor 256 cannot by itself provide a useful numerical
gain: the next theorem must charge the defect set rather than merely delete
its canonical-word neighbourhood.

Run

```bash
python3 phase2/loop/erdos1208/verify_corner_matching_commutator_stability.py
```

## 4. Connection to the size-biased tail

For a dyadic rich relation layer, every corner fibre has degree at least
`t`.  If all relevant fibre sizes are even, choose a perfect matching inside
each fibre for every corner colour.  The distance-Sidon linearity lemma makes
the eight matching edge sets disjoint, so Theorem 1.1 applies.

Odd fibres can be paired with at most one fixed record per fibre.  The
simultaneous bookkeeping is now supplied in Section 4.1 below for an
internally rich layer; the distinction between internal richness and
popularity measured in the ambient relation set remains essential.

For even regularized layers, a sufficient continuation is now simply

\[
 |B|\ll k^{3+o(1)}/t.                           \tag{4.1}
\]

Equation (4.1), together with (1.4), is exactly the size-biased
eight-corner bound for that layer.

The advantage of (4.1) over the original core statement is that its only
witness is explicit: a failed commutator square.  The next attack should
seek a size-biased charge of those witnesses into `A^3`, `D x (D+D)`, or
the opposite-endpoint cells already isolated in the seven-incidence route.

The first unfiltered pointwise relaxation has already been ruled out
sharply.  For two adjacent corner colours, fixing their two common selected
endpoints leaves an intersection of `A-A` with a translate of `A+JA`; the
perpendicular-ruler construction makes one such ambient intersection
`Omega(|A|^2)`, although that large cell is non-transverse.  The independent
45-point source certificate has genuine transverse load `250`.  Thus the
safe continuation is an aggregate defect/support charge, not the
unfiltered maximum; see `ADJACENT_CORNER_FIBRE_BARRIER.md`.

### 4.1 Near-perfect matchings in internally rich cores

There is now an exact cleanup for odd fibre sizes.  Suppose every internal
corner fibre on `X` has size at least `t`.  Pair each fibre arbitrarily and
fix its possible leftover record.  If `F` is the union of all fixed records,
then

\[
 |F|\le 8|X|/t.
\]

Run the canonical-word proof with `B union F` in place of `B`.  Outside its
256 word-preimages, all generators commute and are fixed-point-free, so the
new complete abelian-core obstruction rules out every remaining orbit.
Therefore

\[
 \boxed{|X|\le256|B|+{2048\over t}|X|.}         \tag{4.2}
\]

For `t>=4096` this gives `|B|>=|X|/512`.  What remains is to extract an
internally rich core from the externally popular tail without losing the
critical power, or to charge boundary expansion directly.
