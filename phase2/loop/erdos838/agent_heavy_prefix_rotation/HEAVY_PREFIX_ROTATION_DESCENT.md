# Heavy-prefix toggle banks and the exact weighted rotation child

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

The two residuals in `FIXED_POWER_EIC_SPLIT.md` admit a common exact
form: either a Boolean downset already gives a fixed power of the cap, or
many histories merge into one genuine common child.

For the high-rank branch, fix a central split `A=Q_A disjoint_union R_A`.
Toggling the prefix `Q_A` gives `2^|Q_A|` ordinary faces per source.  This
proves the desired fixed-power estimate globally whenever the overlap of
these toggle banks is a subpower of the cap.  If the overlap is heavy, it
does not produce an unstructured collision: one ordinary face `F` is
contained in all the colliding sources, every source differs from `F` in
at most half the rank, and the complementary Boolean bank over `F` is an
injective full released-core bank.  At `alpha>=1/2`, each such child has a
local square-root saving over the cap.

For the low-rank rotation branch, the codegree-square mass has an exact
marked-target expansion.  Unless it is paid by the downsets of the repaired
targets, it fixes one blocker label carrying a large fraction of the entire
weighted incompatible mass.  Thus the remaining rotation atom is not just
"many nested rotations": it is a **common-blocker, variable-base child**.

These statements do not finish EIC'.  Different common children can still
reuse each other's complementary banks.  The all-middle-layer set system
shows that this cross-child reuse cannot be bounded combinatorially; a
planar two-ended/shield theorem is still required.  No scalable planar
counterexample to EIC' was found.

## 1. Central toggle-bank descent

Let `S` be a family of distinct rank-`r` ordinary faces.  For every
`A in S`, choose a decomposition

\[
                  A=Q_A\mathbin{\dot\cup}R_A,
          \qquad |Q_A|=s,\quad |R_A|=t=r-s.          \tag{1}
\]

The intended choice is `s=ceil(r/2)` and `t=floor(r/2)`.  Define the
toggle bank of `A` by

\[
             \mathcal B(A)=\{R_A\cup B:B\subseteq Q_A\}.     \tag{2}
\]

Every member of (2) is an ordinary face, by deletion from `A`.  For an
ordinary face `F`, put

\[
 m(F)=|\{A\in S:R_A\subseteq F\subseteq A\}|,
 \qquad \kappa=\max_F m(F).                                \tag{3}
\]

> **Theorem 1 (toggle bank or common child).**  With the notation above,
> \[
>                  2^s|S|\le\kappa V(P).                    \tag{4}
> \]
> If every source carries exactly `D` selected records, then
> \[
>                  |E|=D|S|\le\kappa D2^{-s}V(P).           \tag{5}
> \]
> Moreover, if `m(F)=m`, then the `m` sources counted by `m(F)` have the
> form
> \[
>                         A=F\mathbin{\dot\cup}M_A,
>                         \qquad |M_A|\le s,                 \tag{6}
> \]
> with distinct residual sets `M_A`, and they generate the injective
> complementary bank
> \[
>       \mathcal C(F)=\{B\cup M_A:B\subseteq F,\ A\text{ counted by }m(F)\},
> \qquad |\mathcal C(F)|=2^{|F|}m\ge2^tm.                   \tag{7}
> \]

**Proof.**  The left side of (4) counts the pairs `(A,F)` with
`F in B(A)`.  Every output is an ordinary face and occurs at most `kappa`
times, which proves (4); multiplying by `D/2^s` proves (5).

If `A` is counted by `m(F)`, then `R_A subseteq F subseteq A`, so
`M_A=A-F subseteq Q_A` and (6) follows.  Distinct sources give distinct
`M_A`.  Since `F` and `M_A` are disjoint, the union in (7) uniquely
recovers the pair `(B,M_A)`.  It is a subset of the face `A`, hence is a
face.  Finally `|F|>=|R_A|=t`.  This proves (7).  QED.

The theorem gives a clean fixed-power alternative.  Suppose

\[
 r=(\alpha+o(1))\log n,\qquad
 D=n^{1-\alpha+o(1)},\qquad \alpha\ge\tfrac12,              \tag{8}
\]

and use the central split.  Then

\[
             2^s\ge n^{\alpha/2-o(1)}
                   \ge D^{1/2-o(1)}.                        \tag{9}
\]

Consequently, for every fixed `delta<1/2`, either

\[
 \kappa\le D^\delta n^{o(1)}
 \quad\Longrightarrow\quad
 |E|\le n^{o(1)}D^{1-(1/2-\delta)}V(P),                     \tag{10}
\]

or one explicit face `F` is shared by more than `D^delta n^{-o(1)}`
sources, all their residual ranks are at most `ceil(r/2)`, and their local
complementary bank has record-to-face ratio at most

\[
                         {D\over2^t}\le D^{1/2+o(1)}.        \tag{11}
\]

Thus `delta=1/4`, for example, gives a quarter-power global saving in the
light-overlap branch and a square-root local saving in every heavy child.
The only missing operation is to sum the child banks without paying their
cross-child overlap.

This is stronger than merely naming a heavy central prefix.  A bank
collision itself supplies the next common prefix `F`, proves a factor-two
rank descent in its variable part, and exhibits the exact full Boolean
reservoir which must be preserved by the recursion.

## 2. Why a set-system proof cannot remove cross-child reuse

The obstruction is already present without geometry.  Let `S` be the
complete middle layer `binom([2r],r)`, and choose any deterministic central
split of each source.  Its downclosure has only `2^(2r)` sets, while

\[
                         |S|=\binom{2r}{r}=2^{2r-o(r)}.       \tag{12}
\]

Thus no theorem about downsets alone can attach a fixed exponential bank
to every source with bounded global overlap.  In an actual planar point
set, completeness of all `r`-sets would force the whole ground set into
convex position by the four-point criterion, so (12) is not a planar
counterexample.  It pinpoints exactly where rank-three geometry must enter:
heavy overlap of many complementary banks must force either mixed faces or
a shield face cloud.

## 3. The weighted incompatible-rotation child

Use the singleton notation from `FIXED_POWER_EIC_SPLIT.md`.  The sources are

\[
                         A_a=R_a\cup\{x_a\},                 \tag{13}
\]

and `N(a)` is the selected blocker set.  Put

\[
 Q_{ab}=N(a)\cap N(b),\qquad q_{ab}=|Q_{ab}|.                \tag{14}
\]

Call `(a,b,p)` left-incompatible if `p in Q_ab` and

\[
              T_{a,p}=R_a\cup\{p\}\in\mathcal F(P),
              \qquad T_{a,p}\cup\{x_b\}\notin\mathcal F(P).\tag{15}
\]

The first assertion in (15) is precisely the singleton repair relation.
Form the integer multiset

\[
 \Omega=\{(a,b,p,q):a\ne b,\ p,q\in Q_{ab},
                         \ (a,b,p)\text{ is left-incompatible}\}. \tag{16}
\]

The extra coordinate `q` is the codegree-square weight.  For a blocker
label `p`, let

\[
                         M_p=|\{\omega\in\Omega:\omega
                                      \text{ has blocker }p\}|,
 \qquad M=\max_pM_p.                                  \tag{17}
\]

> **Theorem 2 (marked-target payment or common blocker).**  If every
> `T_(a,p)` in (15) has rank `r`, then
> \[
>                         |\Omega|\le rM2^{1-r}V(P).          \tag{18}
> \]
> More exactly, if
> \[
> c_{pq}=|\{a:p,q\in N(a)\}|,                               \tag{19}
> \]
> then the unrestricted weighted reuse of `p` is
> \[
> \widetilde M_p=
>   \sum_{a\ne b:\,p\in Q_{ab}}q_{ab}
>   =\sum_q c_{pq}(c_{pq}-1),                               \tag{20}
> \]
> and
> \[
>                  M_p\le\widetilde M_p,
>          \qquad \sum_p\widetilde M_p=\sum_{a\ne b}q_{ab}^2. \tag{21}
> \]
> For every `theta>0`, at most `1/theta` blocker labels satisfy
> `M_p>=theta|Omega|`.

**Proof.**  An occurrence `omega=(a,b,p,q)` supplies all `2^(r-1)`
downfaces of `T_(a,p)` which contain the marked label `p`.  Fix an output
face `F`.  Its occurrences have marks in `F`; for each `p in F` there are
at most `M_p<=M` of them.  Thus the output load is at most `|F|M<=rM`.
Double counting gives (18).

For fixed `p`, expand the left side of (20) and then choose the second
common blocker `q`.  The ordered source pairs adjacent to both `p,q` are
exactly `c_pq(c_pq-1)`.  Summing (20) over `p` counts every ordered source
pair `q_ab^2` times.  The last assertion follows from
`sum_p M_p=|Omega|`.  QED.

If the forward-codegree theorem fails with constant/subpolynomial
parameters, one of the two orientations contains a comparable fraction of
`Q_2=sum q_ab^2`; after swapping left and right, (16) therefore has

\[
                         |\Omega|\ge n^{-o(1)}Q_2.            \tag{22}
\]

Theorem 2 says that this mass is paid by marked target downsets unless
their occurrence overlap is large.  In the latter case one obtains a
specific blocker `p` and the exact weighted common-blocker child measured
by (20).  This child simultaneously includes exterior rotations and
interior-containment failures; no unjustified comparability claim is used.

The distinction between geometric targets and history occurrences is
load-bearing.  A single face `T_(a,p)` may carry many `(b,q)` coordinates.
The universal same-edge history construction shows that erased history
cannot be reconstructed from one terminal face.  Therefore the remaining
theorem must couple this common-blocker child to a second open face slot,
or charge a nonlocal shield complex; acyclicity of rotations alone is not
enough.

## 4. Failed counterexample route

A tempting way to refute EIC' is to put a coefficient-`1/2` face family in
one rooted pocket and add a common blocker cloud which hides the pocket.
If the source family retained the full quadratic face entropy while all
targets collapsed to one root, this would give `|E|` of order `D V`.

The direct wrapper does not achieve this.  Adding fixed outer vertices to
a small planar copy retains only the boundary chain visible from those
vertices; arbitrary convex faces of the copy need not remain convex after
the wrapper is added.  Conversely, if a blocker hides only a fixed root
singleton and retains the variable core, the repaired target recovers the
record, giving an injection in that common-root class.  A scalable
counterexample would therefore need both quadratic entropy in the
wrapper-compatible source faces and variable-ear erasure without creating
a two-sided shield bank.  No such realization is currently known.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_heavy_prefix_rotation/verify_heavy_prefix_rotation.py
```

The verifier exhausts small uniform set families and every central split,
checks (4) and the common-child injection (7), audits the exponent windows
(9)--(11), and exhausts small left-regular incidence graphs to verify the
weighted codegree identities (20)--(21) and the marked-downface count
(18) in the abstract face complex generated by the targets.
