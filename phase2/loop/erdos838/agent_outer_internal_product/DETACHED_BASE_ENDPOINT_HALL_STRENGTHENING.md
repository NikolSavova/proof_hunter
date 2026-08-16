# The detached branch has an unconditional base-endpoint Hall target

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

The pair-ear hypothesis in `DETACHED_LOAD_SOURCE_EAR_HALL.md` is not
needed for the live detached endpoint branch.  That branch already assumes

\[
 B\cup F\text{ convex},\qquad B\cup\{v\}\text{ convex},
 \qquad F\cup\{v\}\text{ convex}.                       \tag{1}
\]

The second condition is equation (3) of
`ENDPOINT_POCKET_CODEGREE_DICHOTOMY.md`; it is also used there to prove
that every bad attached four-circuit meets `F`.  Therefore every detached
record has three unconditional ordinary targets

\[
        W=F\cup\{v\},\qquad Q=B\cup\{v\},
        \qquad C=B\cup F.                               \tag{2}
\]

After endpoint/base/pocket role coloring, `(W,Q)` already recovers

\[
 v,\qquad e=e(v),\qquad F=W\setminus\{v\},\qquad
 B=Q\setminus\{v\}.                                    \tag{3}
\]

Thus exact fractional Hall routing between `W` and `Q` applies to **all**
detached records, whether or not `A\cup e` is convex.  Adding the released
target `C` gives the exact three-target strengthening.  The old source
`A=B\cup G` is itself an unconditional fourth target.  Low Hall density
pays linearly.  In a high-density pruned core, bounded ordered-pair load
gives a genuine source-base `B` by pocket-face `F` incidence core.  High
ordered-pair load instead fixes `(B,F,v)` and is precisely a multiplicity
of source/guard histories; the source-mask downshadow is then the next
bank.

This removes a geometric hypothesis but does not solve the last global
overlap problem.  A scalable planar guard-by-pocket rectangle has
`m^2` record histories, exact two-target load `m^2/(m+1)`, exact
three-target load `m^2/(2m+1)`, exact four-target load `m^2/(3m+1)`, and
ordered-pair load `Delta=m`.  One explicit realization has convex guard
and pocket clouds and is paid by `2^m`-sized shields.  More sharply, the two
clouds can be replaced independently by arbitrarily prescribed rational
order types inside the same open cage regions.  Thus density does not
force either local support to be Boolean.  The remaining operation is a
genuinely global two-cloud composition/profile theorem.

## 1. Exact unconditional routing

Let `mathcal R` be a weighted family of detached records satisfying (1).
The matching/endpoint state includes a canonical map `v -> e(v)`.
Define

\[
 \lambda _2=\max_{\varnothing\ne\mathcal R'\subseteq\mathcal R}
 {\sum_{r\in\mathcal R'}w_r\over
  |\bigcup_{r\in\mathcal R'}\{W_r,Q_r\}|},              \tag{4}
\]

and

\[
 \lambda _3=\max_{\varnothing\ne\mathcal R'\subseteq\mathcal R}
 {\sum_{r\in\mathcal R'}w_r\over
  |\bigcup_{r\in\mathcal R'}\{W_r,Q_r,C_r\}|}.         \tag{5}
\]

Finally define

\[
 \lambda _4=\max_{\varnothing\ne\mathcal R'\subseteq\mathcal R}
 {\sum_{r\in\mathcal R'}w_r\over
  |\bigcup_{r\in\mathcal R'}\{W_r,Q_r,C_r,A_r\}|}.     \tag{5a}
\]

> **Theorem 1 (unconditional detached/base Hall).**  The minimum maximum
> load of a fractional routing from each record to `\{W_r,Q_r\}` is
> exactly `lambda_2`, and the corresponding value for
> `\{W_r,Q_r,C_r\}` is exactly `lambda_3`.  Since every old source `A_r`
> is an ordinary face, the four-target value is exactly `lambda_4`.
> Consequently
>
> \[
>           \sum_rw_r\le\lambda _2V(P),\qquad
>           \sum_rw_r\le\lambda _3V(P),\qquad
>           \sum_rw_r\le\lambda _4V(P).                 \tag{6}
> \]

**Proof.**  Use the record-to-target max-flow network.  A cut indexed by a
record subfamily has finite capacity precisely equal to its target-union
capacity, so max-flow/min-cut gives (4), (5), and (5a).  Summing the routed load
over actual ordinary faces gives (6).  QED.

Coincident targets cause no problem: (4)--(5) use actual set unions, not
typed copies.  In the live disjoint role buckets, `W,Q,C` have different
support traces unless a degenerate empty role is admitted; retaining the
actual union formulation is safer.

## 2. Decoder, dense core, and the real residual load

The endpoint trace of either target in (2) recovers `v`; the matching state
then recovers `e(v)`.  The fixed support roles give (3).  Hence define

\[
 \Delta_{BQ}=\max_{W,Q}
       \sum_{r:(W_r,Q_r)=(W,Q)}w_r.                     \tag{7}
\]

This is not a mysterious face collision: it is exactly the total weight
of canonical source/root/guard histories having the same recovered
`(B,F,v)`.

There are two additional exact decoders.  Since base and pocket roles are
globally colored,

\[
                    B=C\cap X_{\rm base},\qquad
                    F=C\cap X_{\rm pocket}.              \tag{7a}
\]

Thus low load on released faces `C` alone closes linearly, while a high-`C`
fibre fixes `(B,F)`.  Within that fibre the unconditional source target
`A` varies, and the pair `(A,C)` also recovers

\[
                              G=A\setminus B.             \tag{7b}
\]

Accordingly, after fixed endpoint localization the final geometric Hall
residue may be viewed as a dense old-source `A` by released-face `C`
rectangle.  Multiplicity of one ordered pair `(A,C)` is only the remaining
root/chronology description load; it no longer contains an erased guard.

If `lambda_2>K`, choose a family violating the Hall inequality at load
`K` and repeatedly delete any target of current incident weight at most
`K`, together with its incident records.  A nonempty bipartite core
remains with weighted minimum degree greater than `K`; otherwise charging
each record when its first target is deleted contradicts the violation.
By (7), each surviving target has more than `K/Delta_BQ` distinct
neighbors.  Since a `Q` target determines `B` and a `W` target determines
`F`, this is literally a dense base-by-pocket incidence graph, not merely
a graph of erased formal contexts.

The same pruning works for (5).  With

\[
 \Delta_{BQC}=\max_{W,Q,C}
       \sum_{r:(W_r,Q_r,C_r)=(W,Q,C)}w_r,                \tag{8}
\]

every target in the three-sided core is incident with more than
`K/Delta_BQC` distinct ordered pairs of other targets.  Since
`C=B\cup F` is a deterministic function of the decoded geometric record,
the third target improves capacity but does not reduce the residual
history multiplicity in (7).

## 3. Fixed-record history load descends to source masks

Write the old convex source as

\[
                              A=B\cup G.                 \tag{9}
\]

No pair-ear compatibility is required here.  Because `A` is an ordinary
face, heredity supplies

\[
                  \mathcal S(B;\mathcal G)
                    =\{B\cup S:S\subseteq G
                       \text{ for some }G\in\mathcal G\}           \tag{10}
\]

for every fixed-`(B,F,v)` history fibre, where `mathcal G` is its guard
completion family.  If completion `G` carries history weight `beta_G`,
generating all its submasks gives the exact global accounting

\[
 \sum_G\beta_G2^{|G|}\le
 \Lambda_{\rm mask}V(P),
 \qquad
 \Lambda_{\rm mask}=max_S\sum_{G\supseteq S}\beta_G,              \tag{11}
\]

with additional fixed-fibre overlap included if different `B` produce the
same actual output.  Formula (11) is the source-mask bank referred to in
the marked-shield descent.  The empty mask can have full fibre load, so a
global completion/downshadow or first-divergence theorem is still needed
to turn (11) into a fixed-power gain in every case.

If the stronger source ear `A\cup e` is known convex, the bank upgrades to
`B\cup S\cup e`; this is exactly the conditional theorem in
`DETACHED_LOAD_SOURCE_EAR_HALL.md`.  The unconditional result above stops
at (10), but its Hall targets (2) exist before that upgrade.

## 4. Sharp planar history rectangle

Use the common cage

\[
 B=\{(-3,0),(3,0),(0,5)\},\qquad
 v=(-2,-1),\quad u=(2,-1),                              \tag{12}
\]

and the rational guard and pocket clouds

\[
 g_i=(z_i,5+z_i-z_i^2),\quad z_i={i\over100m},
 \qquad
 x_j=(s_j,-4+s_j^2),\quad s_j={2j-m-1\over200m}.         \tag{13}
\]

As in `THREE_TARGET_ENDPOINT_HALL_COMPLETION_DESCENT.md`, arbitrarily
small rational general-position perturbations preserve all strict
properties.  Put

\[
 A_i=B\cup\{g_i\},\quad G_i=\{g_i\},\quad F_j=\{x_j\}.  \tag{14}
\]

For every `(i,j)`, all three unconditional outputs are ordinary:

\[
 W_j=\{x_j,v\},\qquad Q=B\cup\{v\},
 \qquad C_j=B\cup\{x_j\}.                              \tag{15}
\]

The attached union `B\cup\{g_i,x_j,v\}` is nonconvex because `v` lies
strictly inside `triangle((-3,0),x_j,(3,0))`.  Thus the records genuinely
belong to the detached, not attached, branch.

There are `m^2` histories, one common `Q`, and `m` distinct `W` targets.
Any record subfamily meeting `j` columns has at most `mj` records and at
least `j+1` pair targets.  Hence

\[
                       \lambda _2={m^2\over m+1}.        \tag{16}
\]

Adding the `m` distinct released targets `C_j` gives

\[
                       \lambda _3={m^2\over2m+1}.        \tag{17}
\]

The old-source targets `A_i` are also distinct.  For a subfamily meeting
`i` rows and `j` columns there are at most `ij` records and at least
`i+2j+1` four-bank targets.  This ratio is increasing in both variables,
so

\[
                       \lambda _4={m^2\over3m+1}.        \tag{18}
\]

Every pair `(A_i,C_j)` now recovers `(G_i,B,F_j)` and has unit
multiplicity.  The large four-target Hall load is therefore a genuine
complete source-by-release rectangle, not duplicate descriptions.

For each column `(W_j,Q)`, exactly `m` guard histories collide, so
`Delta_BQ=m`.  This meets the dense-core bound at the correct scale.
Finally, `B\cup\{g_1,\ldots,g_m\}` is convex.  Its guard support supplies
a Boolean bank of `2^m` ordinary faces, overwhelmingly larger than the
`m^2` record rectangle.  The regression therefore identifies, rather than
defeats, the completion-mask alternative.

### 4.1 Arbitrary-order-type refinement: the Boolean shield is not forced

The convex clouds in (13) are a convenient positive realization, not a
consequence of the record axioms.  Let

\[
           g_0=(1/100,50099/10000),\qquad x_0=(0,-4).    \tag{19}
\]

There are open disks `U_g` about `g_0` and `U_x` about `x_0` such that for
every `g in U_g` and `x in U_x`,

\[
 B\cup\{g\},\quad B\cup\{g,v,u\},\quad
 B\cup\{x\},\quad B\cup\{v\},
 \quad\{x,v\}\text{ are convex},\qquad
 B\cup\{g,x,v\}\text{ is nonconvex}.                   \tag{20}
\]

Indeed all assertions hold strictly at `(g_0,x_0)`: the last one follows
from `v` lying in the interior of `triangle((-3,0),x_0,(3,0))`.  Strict orientation signs are
constant in sufficiently small disks.

Now take any two rational general-position configurations `Y,Z` of `m`
points.  Independent positive homotheties place order-type-preserving
copies of `Y` in `U_g` and `Z` in `U_x`.  A further arbitrarily small
generic rational perturbation, still within the same order-type cells,
avoids every cross-cloud/base collinearity.  Use those copies as
`\{g_i\}` and `\{x_j\}`.  Equations (14)--(17) and the four-target value
(18) remain valid; so do the old pair-ear targets
`E_i=B\cup\{g_i,v,u\}` from the conditional theorem.

> **Proposition 2 (universal common-cage rectangle).**  The complete
> source-by-release Hall rectangle is compatible with independently
> prescribed rational order types on its guard and pocket supports.

In particular, if `Y` has an interior point then the full guard cloud is
not a convex face; similarly for `Z`.  More generally, the ordinary faces
contained wholly in either cloud are exactly the convex subsets of the
prescribed child order type.  For singleton completions
`G_i=\{g_i\}`, the formal source-mask downshadow (10) has only `m+1`
members (the empty set and the singletons), not `2^m`.

This gives the sharp common-cage regression.  It kills the purely local
claim that a dense `A by C` rectangle forces a Boolean guard or pocket
shield.  It does **not** give a low-face global counterexample: the two
small clouds occupy separated macro regions, and their cross-profile face
bank may still pay through a strong-composition theorem.  Establishing
that bank with globally controlled overlap is exactly the remaining gate.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_detached_base_endpoint_hall.py
```

Expected output:

```text
PASS: unconditional W/Q/C/A Hall, exact history rectangle loads, and guard-mask shield
```
