# Weighted splice from inversion seams to endpoint--pocket codegree

**Date:** 2026-08-15.  This note connects
`DECORATED_TWO_MARK_INVERSION_DICHOTOMY.md` to
`ENDPOINT_POCKET_CODEGREE_DICHOTOMY.md` without dropping the actual pocket
trace or hiding a per-context copy of the face bank.

## Verdict

When the external label of a minority repeated-block seam lies in the
actual pocket trace `F`, the seam-weighted endpoint-codegree dichotomy loses
only the rank of `F`.  More precisely, use every pocket seam label as a
separate weighted record.  If endpoint compatibility is large, the attached
endpoint--pocket face bank pays with its actual global decoder load.  If it
is small, almost all record weight lies in cells carrying the two canonical
endpoint circuits which meet `F`.  Forgetting which seam label in `F` was
used costs at most `|F|=O(r)`.

There is an essential caveat: a pocket-labelled orientation seam does not
itself imply endpoint incompatibility.  It can occur with endpoint
codegree `g=2`.  Thus the explicit high/low codegree split cannot be
skipped.

In the clean strong-comb setting, a minority pair is defective against every
point outside its repeated block.  Hence any trace meeting another block
admits a canonical witness in `F` and no such loss occurs.  The honest
support residue is `F` lying wholly inside the repeated block.  In looser
applications where only a preselected external defect ledger is known, an
outside-`F` mark still needs an actual decoder.

## 1. Seam-labelled weighted records

Let `rho=(c,e,F,z)` range over minority seams supplied by the inversion
dichotomy, where `c` is the complete source/release context, `e={a_e,b_e}`
is the matching mark, `F` is its actual retained pocket trace, and

\[
                              z\in F.                         \tag{1}
\]

Give `rho` weight `w_rho`.  Put

\[
 D=\sum_\rho w_\rho,
 \qquad
 G=\sum_\rho w_\rho g_c(e,F),                              \tag{2}
\]

where `g` is the attached endpoint codegree from
`ENDPOINT_POCKET_CODEGREE_DICHOTOMY.md`.  Notice that `g` depends on the
cell `(c,e,F)`, not on the particular exposing label `z`.

For every compatible endpoint output

\[
                         B_c\cup F\cup\{v\}.                 \tag{3}
\]

Define the **seam-labelled** decoder load

\[
 \Lambda_{\rm seam}=\max_W
   \sum_{(\rho,v):(3)=W}w_\rho.                             \tag{4}
\]

Grouping records by their actual ordinary output gives the exact high
branch

\[
                     V(P)\ge {G\over\Lambda_{\rm seam}}.     \tag{5}
\]

There is no context count multiplying the right side: all collisions of
bases, roots, carriers, and seam labels are already in (4).

### 1.1 Canonical pocket witness in a strong comb

The full rank factor in (8) is unnecessary in the clean strong-comb
application.  Let `B_i` be the repeated block, and let `E_i^-` be the
minority relation class: inversion pairs if inversions are fewer, and
noninversion pairs otherwise.  The exact sign identity from
`DECORATED_TWO_MARK_INVERSION_DICHOTOMY.md` holds for **every** point outside
`B_i`.  Therefore, whenever

\[
                              F\setminus B_i\ne\varnothing,  \tag{4a}
\]

fix the first label

\[
                         z_i(F)=\min(F\setminus B_i)          \tag{4b}
\]

in a global order.  For every `e in E_i^-`, the triple `(e,z_i(F))` is a
minority repeated-block seam.  The choice is a deterministic function of
the retained trace `F`, so it creates **no** extra decoder multiplicity.

Consequently, if the local bad-pair matching is contained in `E_i^-` and
every live pocket trace satisfies (4a), the endpoint--pocket theorem applies
directly to the full matching-by-pocket rectangle `(e,F)`.  Its high branch
is the attached bank, and its low branch is the double canonical circuit
rectangle meeting the actual trace.  No probabilistic selection of an
external seam label is required.

For a general pocket family split

\[
 \mathcal H_i^{\rm ext}=\{F:F\setminus B_i\ne\varnothing\},\qquad
 \mathcal H_i^{\rm int}=\{F:F\subseteq B_i\}.                 \tag{4c}
\]

The first family has the exact rectangle above.  The second is the genuine
same-block child residue: the external-point sign law says nothing about
triples wholly inside `B_i`, and one must descend to that child's own
profile/circuit structure.  This is a support localization, not a decoder
loss.

## 2. Exact low branch

For one record let `Z=1_{g=0}`.  Since `g` lies in `{0,1,2}`,

\[
                              Z\ge1-g.                       \tag{6}
\]

Consequently, if `G<=theta D` for `theta<1`, the total weight of records
whose cell has `g=0` is at least

\[
                             (1-\theta)D.                    \tag{7}
\]

Every such cell has two canonical `1+3` circuits, one through each endpoint
of `e`, and both circuits meet the named trace `F`.  This conclusion uses
the convexity of `B_c union F` and of `B_c union {v}` exactly as in the
endpoint--pocket theorem.  The inversion seam supplies the weighted cell
selection; endpoint codegree supplies the circuits.

Suppose the unlabelled endpoint or circuit decoder has load `Lambda_0` when
records are indexed only by `(c,e,F)`.  If every pocket trace has rank at
most `r`, then

\[
                    \boxed{\Lambda_{\rm seam}\le r\Lambda_0}. \tag{8}
\]

Indeed a fixed cell has at most `|F|<=r` possible exposing labels `z`, and
the output retains the whole named trace but not which one was selected.
The same proof applies to the canonical circuit outputs, which may be
independent of `z`.  Thus pocket membership creates only a linear-rank
description loss, `2^{O(log r)}`, not a quadratic entropy loss.

Combining (5)--(8), a pocket-labelled minority-seam mass `D` has the exact
trichotomy:

1. attached faces of weighted size at least `theta D/Lambda_seam`;
2. a `(1-theta)D`-weight double endpoint--pocket circuit rectangle, with
   circuit decoder load at most `r` times its cell load; or
3. the detached endpoint branch of the endpoint--pocket theorem, if one
   chooses to split once more using detached codegree `h`.

This is the desired splice whenever a fixed-power share of the inversion
mass has its external label in the actual pocket trace.

## 3. Why the codegree split is necessary

Take

\[
 a=(0,0),\quad b=(1,0),\quad z=(0,1),\quad w=(2,3),           \tag{9}
\]

with base `B={w}` and pocket trace `F={z}`.  Every triple is noncollinear.
Both `B union F union {a}` and `B union F union {b}` have rank three and
are convex, so

\[
                              g(\{a,b\},F)=2.                \tag{10}
\]

Nevertheless the orientation of `(a,b,z)` is positive, and reversing the
pair in a reset chart flips that repeated-block seam exactly as in the
inversion identity.  Hence a mixed seam whose external label is literally
`z in F` can lie in the **high** endpoint-codegree branch.  Orientation
alone cannot manufacture the two circuits in (7).

This example is deliberately rank-minimal.  It shows a logical implication
is false; it does not obstruct (5), which pays perfectly in this cell.

## 4. The outside-pocket ledger in a looser application

For all minority seam records, split the exact weighted mass as

\[
 D=D_{\rm in}+D_{\rm out},\qquad
 D_{\rm in}=\sum_{z\in F}w_\rho.                            \tag{11}
\]

At least one side has half the mass.  If `D_in>=D/2`, Sections 1--2 apply
with only the factor `r` in (8).  Under the full strong-comb sign law,
Section 1.1 supersedes this mass split: reselect the deterministic
`z_i(F)` for every trace in `H_i^ext`.

If `D_out>=D/2`, the seam label need not be present as a distinguished mark
in either an endpoint output or a canonical pocket circuit.  Many different
outside labels can therefore collapse to the same output.  Let

\[
 \Delta_{\rm out}=\max_W
   \sum_{\rho:\,z\notin F,\ \Phi(\rho)=W}w_\rho             \tag{12}
\]

be the actual load of the proposed separated/context output `Phi`.  A bank
exists exactly at scale `D_out/Delta_out`; without a bound on (12), the
words "outside the pocket" imply no gain.  Recoverability can come from a
retained role label, a carrier/anchor tag, or a Hall union over contexts,
but it must be proved in the ambient application.

Thus outside the full strong-comb hypothesis the remaining target is
narrow:

* show that a large share of minority seams use actual pocket labels; or
* give an output which retains an outside seam mark with subpower weighted
  load.

Inside a strong comb, replace the first bullet by the exact support split
`H_i^ext union H_i^int` in (4c); only `H_i^int` descends.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_inversion_endpoint_pocket_splice.py
```

The checker verifies the rational barrier (9)--(10), exhausts (6) for every
`g in {0,1,2}` pattern through eight cells, and checks (5),(7),(8) on exact
rational weighted tables with deliberate cross-context collisions.  Both
the endpoint and canonical-circuit tables attain nontrivial seam-label
multiplicity, so the rank-load check is not vacuous.

## Scope

This note is an exact weighted bookkeeping theorem conditional only on the
already proved endpoint--pocket circuit extraction.  It does not claim that
a general inversion seam chooses a pocket point, nor that an outside seam
label is recoverable.  Those are precisely the two geometric/Hall questions
left exposed by (11)--(12).
