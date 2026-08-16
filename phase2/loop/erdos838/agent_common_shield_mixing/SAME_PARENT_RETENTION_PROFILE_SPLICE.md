# Same-parent retention to radial profiles: exact splice and the compatible-jet gate

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The new redundancy-charged semialgebraic theorem removes the selected-word
container obstruction, but it does not by itself manufacture the local
directional faces needed by the one-gap bank.

Fix one parent, root/tangent state, cyclic macro order, and repair state.
Let `E` be a family of `M` selected singleton petal words on `q` coordinate
supports `X_i`, put

\[
 L_i=|X_i|,\quad s_i=\log L_i,\quad
 P_0=\prod_iL_i,\quad R=\log(P_0/M),                    \tag{1}
\]

and assume `L_i<=D`, `q<=kappa log D`.  The live entropy dichotomy is:

1. If the fixed atom already has the established detached one-gap/profile
   geometry, its ambient bank satisfies
   
   \[
    \log{\max_jB_j\over M}
      \ge R+{1\over q}\sum_i(\log H_i-3s_i).            \tag{2}
   \]
   
   In particular
   
   \[
            \log(\max_jB_j/M)\ge R-2\log D.             \tag{3}
   \]
   
   Thus `R>=eta(log D)^2` is already paid by a one-face ambient bank with
   coefficient gain `eta-o(1)`.  In a fixed two-sided seam state, the
   complete-profile bank of `PARENT_SEAM_JET_COMPLETION.md` analogously
   charges the exact left--right projection redundancy
   `log(|A||B|/M)`.

2. If `R=o(q^2)`, the theorem in
   `REDUNDANCY_CHARGED_SEMIALGEBRAIC_RETENTION.md` retains
   
   \[
          M'\ge M\,2^{-O(q+R)}=M\,2^{-o(q^2)}            \tag{4}
   \]
   
   words in a coordinate product on which every required consecutive
   orientation sign is homogeneous.  Including the fixed parent endpoints
   as singleton coordinates makes the closing and seam signs part of the
   same finite local certificate.  Hence, in the standard fixed-order
   radial model, every singleton transversal of the retained product is an
   ordinary carrier.  Fixed-parent seam-jet localization costs only
   `O(log D)` further bits and removes every remaining **singleton**
   left--right coupling.

The second conclusion is not yet a coefficient gain.  A one-gap output
replaces a singleton by a multi-point local directional face.  Its actual
entry/exit seam jet need not equal the jet seen by the selected singleton.
The rational `1+3` circuit in
`DOMINANCE_CELL_SEPARATED_ONE_GAP.md` has `R=0`, a complete homogeneous
singleton product, and a nonconvex formal one-gap output.  Thus neither the
retention theorem nor fixed-parent seam classification supplies a rich
**compatible** local reservoir.

There is an exact conditional coefficient theorem.  If each retained
coordinate support has enough two-ended profiles with the actual compatible
seam jets, so that the established radial one-gap multiplication is valid
and its compatible local reservoirs have coefficient `c_0`, then

\[
 {\log V(P)\over(\log D)^2}
       \ge a+c_0(a/\kappa)^2-o(1),                      \tag{5}
\]

where `log M=(a+o(1))(log D)^2`.  With the established asymptotic local
face coefficient `c_0=1/8` and `a=kappa=1/4`, this is

\[
                              3/8-o(1).                  \tag{6}

\]

The precise next operation is therefore a **compatible-jet reservoir
lemma**, not another selected-family product extraction:

> from a homogeneous singleton container, either find a mask-aware local
> face reservoir of quadratic entropy whose actual two-ended jets are
> compatible with the neighboring retained cells, or inject the
> incompatible reservoir mass into a circuit/shield bank.

The MDS and radial-transversal regressions both pass this audit.  MDS has
subquadratic redundancy and no selected Cartesian modules, but its genuine
small-cluster radial geometry has the compatible ambient reservoirs and
therefore pays `3/8`.  The full radial-transversal regression has `R=0` and
is already a homogeneous product; it is paid by its mask-aware
first-divergence/one-gap profiles, not by Boolean shadows or pairwise source
unions.  Neither is contradicted by (4).

## 1. Exact large-redundancy exit

Inside a fixed-tangent detached radial container, let `H_i` be the number
of nonempty ordinary local faces and let `A_i,R_i` be the two directional
profile counts, with

\[
                              A_iR_i\ge H_i.              \tag{7}

\]

The existing one-gap bank omitting macro cell `j` has

\[
 B_j=R_{j-1}A_{j+1}
           \prod_{i\notin\{j-1,j,j+1\}}L_i.             \tag{8}

Multiplying cyclically and taking a geometric mean gives

\[
 \max_jB_j\ge P_0
       \left(\prod_i{H_i\over L_i^3}\right)^{1/q}.       \tag{9}

Divide by `M=P_0 2^{-R}` to obtain (2).  Every singleton is an ordinary
local face, so `H_i>=L_i`.  Since `sum_i s_i<=q log D`, equation (3)
follows.  No selected rectangle or
independence hypothesis is used: large support correlation is favorable
because the missing selected words remain available in the ambient
one-gap alphabet.

For a fixed parent split into a left ear and a right ear, Theorem 4 of
`PARENT_SEAM_JET_COMPLETION.md` partitions by the at-most-four-label seam
jet and gives all ambient cross-completions.  In one active fixed state,
if the selected family has left and right projection sizes `A,B`, its
ordinary completion bank has size `AB 2^{|T|}` and gains exactly

\[
                              \log{AB\over M}.            \tag{10}

\]

This charges the part of `R` visible at that seam split.  Equation (9),
when its radial hypotheses hold, charges the full coordinate-support `R`.
If only the separated two-face omit-one-cell bank is available, its output
lives in `mathcal F(P)^2` and incurs the known square loss; it cannot be
substituted for (9).

## 2. Low redundancy retains the quadratic source coefficient

Assume source convexity in the fixed macro order is certified by a fixed
list of strict orientation predicates on consecutive varying coordinates
and the fixed parent endpoints.  Add each fixed endpoint as a singleton
coordinate.  This changes the rank by `O(1)` and the support redundancy by
zero.

Apply the consecutive-sign retention theorem.  It gives coordinate subsets
`Y_i subseteq X_i` and a retained selected family

\[
 E'=E\cap\prod_iY_i,qquad |E'|\ge M2^{-A(q+R)}.         \tag{11}

\]

If `log M=(a+o(1))d^2`, `d=log D`, then necessarily
`q>= (a-o(1))d`, since `M<=D^q`.  Thus `q=Theta(d)` on the quadratic source
scale.  The condition `R=o(q^2)` implies

\[
                         \log|E'|=(a+o(1))d^2.           \tag{12}

\]

Every transversal of `prod_iY_i` has the same complete local sign
certificate as a member of `E'`, hence is an ordinary singleton carrier.
The fixed-parent edge-splice and four-label seam-jet theorems may now be
applied without a quadratic loss: their state description has only
`O(log D)` bits.  This proves complete ambient cross-completion at the
singleton level.

Notice what (11) does not say.  It gives no pair of points in a local
support `Y_i`, because every selected word uses only one point there.
Consequently it contains no information about the seam jet of a local
multi-point face.

## 3. Conditional one-gap coefficient

Write

\[
                 \ell_i=\log|Y_i|,qquad S=\sum_i\ell_i. \tag{13}

\]

Since `E' subseteq prod_iY_i`,

\[
                              S\ge\log|E'|.              \tag{14}

\]

Assume the following additional geometric hypothesis.

> **Compatible-profile hypothesis.**  In each retained cell there are
> two directional profile families with the actual entry/exit seam jets
> required by the neighboring retained cells.  Their cyclic products give
> the ordinary one-gap banks (8), and their compatible reservoir sizes
> `H_i^star` satisfy, in aggregate,
> 
> \[
> {1\over q}\sum_i\log H_i^\star
>   \ge {c_0-o(1)\over q}\sum_i\ell_i^2.                \tag{15}
> \]

The cyclic identity then yields

\[
 \begin{aligned}
 \log\max_jB_j
 &\ge S+{1\over q}\sum_i(\log H_i^\star-3\ell_i)\\
 &\ge S+{c_0-o(1)\over q}\sum_i\ell_i^2-{3S\over q}\\
 &\ge S+(c_0-o(1)){S^2\over q^2}-{3S\over q}.           \tag{16}
 \end{aligned}

\]

Here the last line is Cauchy--Schwarz.  Since `S>=log|E'|`, `S/q<=d`,
and the right side is increasing throughout the quadratic regime, (12)
and `q<=kappa d` give (5).  The term `3S/q` is only `O(d)`.

The established asymptotic planar face reservoir supplies `c_0=1/8` for
genuine strongly separated/projective radial clusters.  Substitution of
`a=kappa=1/4` in (5) gives

\[
 {1\over4}+{1\over8}\left({1/4\over1/4}\right)^2
                              ={3\over8}.                \tag{17}

\]

This is the exact scope of the often-quoted conditional `3/8` jump.

## 4. The compatible-jet implication is false without new input

Normalize the root edge to

\[
 u=(-1,0),\qquad v=(1,0),                               \tag{18}

\]

and take

\[
 \begin{aligned}
 q&=(-19/20,1/20),&x&=(-3/40,7/8),\\
 w&=(0,10/11),&z&=(3/40,7/8),&y&=(2/15,8/9).
 \end{aligned}                                         \tag{19}

\]

Use four cells

\[
 X_1=\{q\},\quad X_2=\{x\},\quad X_3=\{w\},
                         \quad X_4=\{z,y\}.             \tag{20}

\]

Both full singleton transversals

\[
 \{u,v,q,x,w,z\},\qquad \{u,v,q,x,w,y\}                \tag{21}

\]

are convex.  Thus the selected family is the complete product, `M=P_0=2`
and `R=0`; no semialgebraic retention is lost.  All singleton seam data are
compatible.

Omit the third cell and use the perfectly ordinary two-point local face
`{z,y}` from the fourth.  The formal one-gap output is

\[
                              \{q,x,z,y\}.               \tag{22}

\]

It is nonconvex because

\[
 z={3\over230}q+{122\over575}x+{891\over1150}y,         \tag{23}

\]

with positive coefficients summing to one.  The multi-point face changes
the actual seam jet and creates a `1+3` circuit.  This is an exact
counterexample to the implication

\[
 \text{homogeneous singleton product}
   \Longrightarrow\text{arbitrary compatible local-reservoir product}. \tag{24}

\]

The fixed-parent seam theorem detects the failure once the new face's
actual jet is supplied; it does not prove that a quadratic fraction of the
local reservoir has the desired jet.

Accordingly the next lemma must retain or create **face-valued** history:

* either a common compatible two-ended jet carries the quadratic local
  face entropy needed in (15);
* or every large incompatible jet class releases a recoverable bad circuit,
  outer shield, or detached one-gap face.

Tagging all four jet labels costs only `O(log D)` bits, but choosing the
largest jet class is invalid: the largest class can be incompatible with
the neighboring retained container.  Compatibility and reservoir size
must be proved simultaneously.

## 5. Regression audit

### MDS anti-module family

For the Reed--Solomon construction in
`MDS_MODULE_EXTRACTION_BARRIER.md`, with `d=log p`,

\[
 q=(1/4+o(1))d,\quad
 M=p^{q-c},\quad P_0=p^q,\quad R=c\log p=o(d^2).         \tag{25}

\]

It is in the low-redundancy branch.  The retention conclusion does not
claim a Cartesian subcode and therefore respects the MDS distance
obstruction.  The planar realization uses genuine small separated radial
clusters, so its mask-aware compatible profiles satisfy the radial
one-gap theorem.  Equation (17) reproduces its certified `3/8-o(1)` bank.

### Full radial transversal family

For `r` blocks of size `L`,

\[
 M=L^r=P_0,\qquad R=0.                                  \tag{26}

\]

The retention theorem can keep the full product.  Pairwise unions of
distinct transversals may still be nonconvex, and proper Boolean shadows
may contract; neither fact conflicts with singleton cross-completion.
The existing first-divergence radial theorem pays through occupied-mask
directional profiles.  The four-block universal-wrapper audit shows why
these profiles cannot be assigned independently of the omitted mask.

Thus both sharp regressions point to the same missing coordinate: the
actual mask-dependent entry/exit jet of the **replacement face**, not a
source-word module, marginal support, or another consecutive singleton
sign.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_same_parent_retention_profile_splice.py
```

The checker verifies the exact entropy algebra and coefficient `3/8`, the
large-redundancy bound at several scales, the low-redundancy MDS scaling,
the full-tensor `R=0` audit, and the rational compatible-jet circuit
obstruction using exact hull and barycentric arithmetic.
