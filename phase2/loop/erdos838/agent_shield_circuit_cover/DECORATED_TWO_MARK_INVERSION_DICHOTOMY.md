# Decorated two-mark strong seams: exact inversion-or-release dichotomy

**Date:** 2026-08-15.  This is a local structural theorem.  It does not by
itself supply the global Hall/context charge.

## Verdict

A chosen assembly direction and one chosen reset direction can be
synchronized inside a strong-comb role with exact rational coordinates.
This does **not** make the parent's reset profile a recurrence of the child
reset profiles.  The obstruction is completely visible: every inversion
between the child's assembly and reset orders flips all cross triples using
that pair.

For a block of size `n`, let `I` be the inversion count of the reset
permutation relative to assembly and put

\[
                    k=\min\left(I,{n\choose2}-I\right).       \tag{1}
\]

If the reset keeps macro blocks as intervals, then for **each** external
point the two cross-seam signs occur `I` and `binom(n,2)-I` times.  Hence a
block with `E` external points contributes exactly

\[
                              E k                            \tag{2}
\]

minority-sign mixed seams.  Conversely, deleting at most `k` block points
makes the remaining reset order agree with assembly or with its reversal.

Thus every block-separated reset has an exact dichotomy:

1. a small discarded set releases a monotone/reverse separated skeleton;
   or
2. there is a quantitatively equal supply of mixed cross seams.

If macro blocks interleave under the reset, one is already in the
cross-block interval-mixing branch.  This gives the requested local
``separated profile or dense mixed seam'' classification.  The remaining
global problem is to turn the mixed seams into **coexisting actual**
rooted-circuit/shield banks, or to charge the released deletion sets with
bounded context overlap.  Counting the absolute seams is not yet that
charge.

## 1. Exact sign identity

Let disjoint ordered blocks `B_1<...<B_q` form a strong cap comb in an
assembly functional `f`.  Thus for `i<j`, assembly-ordered pairs satisfy

\[
\begin{aligned}
 \chi(p,p',z)&<0 &&(p<_f p'\in B_i,\ z\in B_j),\\
 \chi(z,p,p')&>0 &&(z\in B_i,\ p<_f p'\in B_j).       \tag{3}
\end{aligned}
\]

Take another generic functional `h` and first suppose every `B_i` is an
interval of the `h`-order.  For a pair `p,p'` in one block define

\[
 \epsilon_h(p,p')=
 \begin{cases}
 +1,&f\text{ and }h\text{ order the pair alike},\\
 -1,&f\text{ and }h\text{ order the pair oppositely}.
 \end{cases}                                                \tag{4}
\]

In the `h`-ordered cross triple, changing from `f` to `h` either retains or
swaps exactly the two same-block points.  Alternation of the determinant
therefore multiplies the relevant sign in (3) by
`epsilon_h(p,p')`.  The macro block order may itself reverse, which changes
which of the two formulas in (3) is displayed, but it does not change the
`I` versus `binom(n,2)-I` split.  This proves (2) exactly, not merely up to a
constant.

In particular, a reset seam is uniform on a block exactly when its
permutation is increasing or decreasing.  A child scalar pair `(C,U)` does
not retain this inversion pattern, which is why the formal reset recurrence
can fail even after both marked child profiles have been synchronized.

## 2. Exact release set

Assume first `I<=binom(n,2)-I`.  Form the inversion graph on the block
positions and, for every inversion edge, select one endpoint.  The union
`G` of the selected endpoints is a vertex cover, has size at most `I`, and
leaves no inversion.  Hence `h` and `f` agree on `B\G`.

If noninversions are fewer, do the same with the noninversion graph.  The
remaining order is decreasing.  In both cases

\[
                              |G|\le k.                       \tag{5}
\]

This intentionally elementary cover is enough for the dichotomy.  A
minimum vertex cover or longest-monotone-subsequence decoder can improve
`|G|`, but is not needed for (5).

For several blocks, write `n_i=|B_i|`, `N=sum n_i`, and `k_i` for (1).  No
cross triple is counted for two different doubled blocks, so the exact
minority mass is

\[
                    M=\sum_i (N-n_i)k_i.                     \tag{6}
\]

Deleting at most `sum k_i` points leaves every block monotone or reverse.
Equation (6) is the natural local potential for a pathwise reset chain:
either it is spent on discarded visible layers, or it records mixed seams
which must be carried into the rooted `1+3`/`2+2` circuit analysis.

## 3. Two marked directions really can be synchronized

The sign obstruction is not an inability to fit one selected reset into a
tangent cone.  Let `f,h` be independent generic functionals on one child.
For positive handedness `det(f,h)>0`, use local coordinates

\[
                    X=\delta f,\qquad
                    Y=S\delta f+\varepsilon h,                \tag{7}
\]

where `delta,epsilon>0` and `epsilon/delta` is sufficiently small.  This is
orientation preserving, the assembly order is the `f`-order, all pair
slopes lie in an arbitrarily small interval about `S`, and

\[
                             Y-SX=\varepsilon h.              \tag{8}
\]

Thus the one desired reset is exact.  For negative handedness use
`Y=S delta f-epsilon h` and reset `SX-Y`.

Place the role centers on the strict cap

\[
                         (i,Si-i^2).                          \tag{9}
\]

For sufficiently small clusters, every internal pair slope is larger than
every relevant cross slope, proving all strong-comb signs (3).  In the
positive-handed reset (8), the macro offsets are `-i^2`, so the blocks occur
in reverse order while each block has exactly its prescribed `h`-order.

This construction proves local two-mark synchronization.  It also exposes
the catch: if `h` has both inversions and noninversions relative to `f`, the
cross signs at reset are mixed by (4), so the reset is not a strong or
opposite comb of the child scalar profiles.

## 4. Exact 44-point stress test

Use the three assembly states realizing the exact scalar optimum
`W_2=747670`:

\[
                 (183,1975),\quad(342,414),\quad(1975,183).   \tag{10}
\]

On the positive-handed side choose reset profiles

\[
                 (193,1826),\quad(251,539),\quad(1826,193).   \tag{11}
\]

These are attained in chambers `45,29,44` of the same three child order
types.  The rational construction (7)--(9), with singleton endpoint roles,
has exact assembly profile

\[
                           (103311,16109).                    \tag{12}
\]

The three reset permutations have inversion counts

\[
                              (1,9,1).                        \tag{13}
\]

There are 30 external points for every size-14 child, so (6) gives exactly

\[
                         M=30(1+9+1)=330                     \tag{14}
\]

minority cross triples.  Exhausting the actual reset order gives

\[
                         (C,U)=(14537,106989).                \tag{15}
\]

By contrast, pretending the three child reset profiles form a clean
reverse/opposite comb gives `(13503,113423)`.  The discrepancy is not a
coordinate error; it is precisely the inversion seam in (4).  Even the
small value `sum k_i=11` already invalidates the scalar recurrence.

## 5. Pathwise consequence and honest remaining gate

At one wrapper generation, sibling copies choose their assembly/reset pairs
independently.  If a proof retains the profiles induced on the same
descendant by several ancestor resets, applying (4) at each retained level
produces a pathwise inversion potential

\[
                    \sum_{\text{levels }t}
                    \sum_{\text{blocks }i}(N_{t}-n_{t,i})k_{t,i}. \tag{16}
\]

A future proof using those simultaneous histories must telescope this
potential into actual coexisting context banks, or show that the union of
the release sets in (5) has small history multiplicity.  Neither follows
merely from (16): the same rooted `1+3` circuit or the same released face
may be reused by many source contexts and many ancestors.  This is exactly
where target/context labels and Hall load must be retained.  An existential
recursive construction may instead forget old descendant charts after
promoting a completed parent to a new atom; in that model only one decorated
assembly/reset edge is exported at a time, and no pathwise `Pi_d` condition
should be imposed.

Consequently this artifact closes the **local orientation classification**
but not the global coefficient-half theorem.  It provides the right input
to the rooted-circuit/convex-ear branch: block interleaving, a released
monotone/reverse skeleton, or an exact mass of mixed seams with their block
and external-point labels intact.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_decorated_two_mark_inversion.py
```

Expected output:

```text
PASS: permutation deletion exhaustive through n=7; exact 44-point bi-chart parent assembly=(103311,16109), reset=(14537,106989), inversion counts=(1,9,1), mixed cross triples=330
```

The verifier uses exact `Fraction` arithmetic.  It exhausts the deletion
claim for every permutation through size seven, constructs the rational
44-point bi-chart parent, checks every triple sign in the assembly strong
comb, verifies the two marked child profiles and reset block order, counts
all 330 minority cross triples directly, and computes (12) and (15) by the
independent chain DP.
