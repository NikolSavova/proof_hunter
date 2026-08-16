# From weighted radial mass to raw completion density

**Date:** 2026-08-15  
**Verdict:** there is an unconditional raw dichotomy: low `N/C` radial
cells are paid directly by their endpoint completion banks, while every
unpaid cell already has high unweighted density.  The rank variables can be
aggregated exactly before this split, so guarded downshadows are unnecessary
at that interface.

A stronger fixed-power corollary holds for a weighted fibre of relative
mass `V/n^{o(1)}`: the established coefficient-`1/4` face bound pushes its
mass above source rank `(1/8)log n`, and the fibre then contains
`n^(1/8-o(1))V` raw occurrences, almost all in cells of density greater than
`n^(1/16)`.  Combined with the exact fixed-role ceiling
`M<=L_desc J V`, this means that under subpower description/depth load the
relative-heavy hypothesis is actually impossible: Theorem 3 below is an
**emptiness certificate**, not a surviving raw-mass branch.  **The current
marked KL/Hall localization does not in general
supply this relative-mass hypothesis.**  If its quadratic reservoir has
coefficient `a` while `log V` has coefficient `c>a`, the guaranteed fibre
is quadratically smaller than `V`, whereas rank conversion recovers only a
linear number of bits.  The exact threshold is recorded below.  No raw gate
is claimed closed across that coefficient gap.

All logarithms are base two.  Write `V` for the number of ordinary convex
faces and `L=log n`.

## 1. Exact aggregation over all rank pairs

Fix a radial cell `(j,e)`.  Let `N_(j,e,r)` be its number of histories with
parent rank `r`, and let `C_(e,s)` be the number of compatible endpoint
faces of rank `s`.  Put

\[
 N_{j,e}=\sum_rN_{j,e,r},\qquad C_e=\sum_sC_{e,s}.       \tag{1}
\]

Resolve `q_(j,e)` and `p_e` by rank as `q_(j,e,r)` and `p_(e,s)`.  Directly
from the half-weights,

\[
 N_{j,e}=F4^j\sum_rq_{j,e,r}2^r,\qquad
 C_e=F\sum_sp_{e,s}2^s.                                 \tag{2}
\]

> **Theorem 1 (aggregate raw-rank identity).**  With `h_(j,e)=q_(j,e)/p_e`,
> and with expectations taken under the conditional rank laws in the cell,
>
> \[
> \boxed{
> {N_{j,e}\over C_e}
> =h_{j,e}
> {\mathbb E_{q(\cdot\mid j,e)}2^{r+2j}
>  \over
>  \mathbb E_{p(\cdot\mid e)}2^s}.}                    \tag{3}
> \]

**Proof.**  Divide the two identities in (2), factor out `q_(j,e)` and
`p_e`, and use `4^j=2^(2j)`.  QED.

This identity aggregates the entire rank mismatch before any pair `(r,s)`
is selected.  In particular, downshadow allocation is unnecessary merely
to decide whether the cell already has high unweighted density.

## 2. The raw completion-bank dichotomy

Let cells `c` contain `N_c` raw history occurrences and have ordinary-face
completion banks `C_c`.  Repeated banks and overlapping banks are allowed;
assume only the global aggregate load bound

\[
                         \sum_c|C_c|\le\Lambda V.        \tag{4}
\]

> **Theorem 2 (raw density or direct completion payment).**  For every
> `rho>0`, if
>
> \[
> \mathcal L=\{c:N_c\le\rho|C_c|\},\qquad
> \mathcal H=\{c:N_c>\rho|C_c|\},                       \tag{5}
> \]
>
> then
>
> \[
> \boxed{\sum_{c\in\mathcal L}N_c\le\rho\Lambda V.}    \tag{6}
> \]
>
> Hence, if the total raw mass is `M`, either the low-density cells are
> paid directly by the completion banks at cost `rho Lambda V`, or
>
> \[
>              \sum_{c\in\mathcal H}N_c
>                 \ge M-\rho\Lambda V                  \tag{7}
> \]
>
> lies in cells of unweighted density greater than `rho`.

**Proof.**  Sum `N_c<=rho|C_c|` over the low cells and apply (4).  QED.

For the unmarked endpoint-rank cells `C_(e,s)`, the completion banks are
actually disjoint across endpoint pairs: a nontrivial face recovers its
first and last labels.  Since the same endpoint bank can occur at each of
`J` depths, cells `(j,e)` have `Lambda<=J`; grouping depths first gives
`Lambda=1`.  In a fixed marked/tangent fibre, the same proof
uses the genuine global decoder load.  For bounded-rank marks and a
polylogarithmic tangent alphabet this is `Lambda=n^{o(1)}`.  Crucially, one
must group all histories offered the same completion bank before applying
Theorem 2; spending that bank once per history would be invalid.

## 3. Exact radial history weights

Let a depth-`j` history have parent `T`, endpoint pair `e=e(T)`, and source
rank

\[
                             k=|T|+2j.                  \tag{8}
\]

In the common-face/radial Hall normalization its weight is

\[
                 \omega(T,j)={2^{-|T|}\over4^jG_e}
                             ={2^{-k}\over G_e}.         \tag{9}
\]

The endpoint pair itself is always a compatible parent, so `G_e>=1/4`.
Therefore

\[
                         \boxed{\omega(T,j)\le4\,2^{-k}.}\tag{10}
\]

This is pointwise.  If a weighted occurrence family of source ranks at
least `K` has weight `W_K` and raw size `M_K`, then

\[
                         \boxed{M_K\ge2^{K-2}W_K.}       \tag{11}
\]

No likelihood-ratio or baseline-rank matching is used in (11).

There is also a ceiling which must be applied before interpreting a large
raw conclusion.  In one genuinely fixed role fibre, a geometric source
face has one canonical cell at each depth.  If the upstream description
map represents one source at most `L_desc` times and at most `J` depths are
active, then

\[
                         \boxed{M\le L_{\rm desc}JV.}    \tag{11c}
\]

Indeed, charge each raw occurrence to its ordinary source face and depth.
Equation (11c) follows immediately.  Hence a conclusion
`M>=n^alpha V` with fixed `alpha>0` contradicts a subpower
`L_desc J`; it cannot be carried forward as a new high-density branch.

Combining (11) with Theorem 2 gives the sharp relative form.  If the
rank-at-least-`K` portion has weight `W_K`, set

\[
                 \rho_*={2^{K-3}W_K\over\Lambda V}.     \tag{11a}
\]

Then cells of raw density greater than `rho_*` carry raw mass at least

\[
                              2^{K-3}W_K.               \tag{11b}
\]

Indeed (11) gives total raw mass at least `2^(K-2)W_K`, while Theorem 2
bounds the complementary cells by `rho_* Lambda V=2^(K-3)W_K`.  Thus the
largest density forced by this argument has logarithm

\[
       \log\rho_*=K-\log(V/W_K)-\log\Lambda-O(1).       \tag{11c}
\]

This is fixed-power precisely when the rank gain exceeds the relative-mass
deficit and decoder loss by `Omega(log n)`.

## 4. A heavy weighted fibre is automatically high-rank

Assume each source-depth occurrence carries at most `A(n)=n^{o(1)}` marked
or tangent roles.  The total weight of all occurrences whose source rank is
less than `K` is at most their raw count, hence at most

\[
 A(n)K\sum_{i<K}\binom ni
 \le A(n)K^2n^K.                                      \tag{12}
\]

Use the already established universal bound

\[
                    V\ge2^{(1/4-o(1))L^2}.             \tag{13}
\]

Set `K=floor(L/8)`.  Equations (12)--(13) imply

\[
 {A(n)K^2n^K\over V}=2^{-(1/8-o(1))L^2}.               \tag{14}
\]

> **Theorem 3 (weighted-to-raw density bridge).**  Suppose an actual
> localized occurrence fibre has total weight
>
> \[
>                             W\ge V/n^{o(1)},           \tag{15}
> \]
>
> role multiplicity `A(n)=n^{o(1)}`, and completion-bank load
> `Lambda=n^{o(1)}`.  Then its source-rank-at-least-`L/8` part has weight
> `(1-o(1))W` and raw mass
>
> \[
>                             M_K\ge n^{1/8-o(1)}V.      \tag{16}
> \]
>
> Taking `rho=n^(1/16)` in Theorem 2, the raw mass in cells satisfying
>
> \[
>                              {N_c\over|C_c|}>n^{1/16}  \tag{17}
> \]
>
> is `n^(1/8-o(1))V`.  In particular at least one genuine cell has
> fixed-power unweighted completion density.

**Proof.**  The low-rank weight is bounded by (12), which is negligible
relative to (15) by (14).  Apply (11) to the remaining weight to get (16).
Theorem 2 bounds all cells failing (17) by
`n^(1/16)Lambda V=n^(1/16+o(1))V`, negligible compared with (16).  QED.

The constants are deliberately wasteful.  If (13) is available with any
coefficient `c>0`, one may use every fixed `K=(c-delta)L`; the raw gain is
`n^(c-delta-o(1))`, and any smaller fixed-power density threshold survives
subpower decoder load.

## 5. Coefficient audit of the current marked localization

The marked Hall step presently guarantees a fixed fibre of weight at least

\[
                  W_*\ge {K_{\rm res}D_0^{1-\epsilon}\over bT},
 \qquad K_{\rm res}=2^{(a-o(1))(\log D_0)^2}.           \tag{18}
\]

Here `D_0=n^{1-o(1)}` in the low-mean minimizer branch and `b,T` are
subpower on the bounded-rank slice.  Consequently the guaranteed scale is

\[
                         \log W_*\ge(a-o(1))L^2+O(L).   \tag{19}
\]

Write

\[
                         \log V=(c+o(1))L^2.            \tag{20}
\]

The present chain supplies `W_*>=V/n^{o(1)}` only if it supplies much more
than equality of the leading coefficients: by (11c) one needs

\[
                \log V-\log W_*=o(L)                   \tag{21}
\]

for the stated subpower-relative hypothesis, or at worst `O(L)` with a
small enough constant for some fixed-power raw conclusion.

The three coefficient regimes are therefore exact.

1. If `a>c` by a fixed constant, (18) contradicts genuine-history packing
   `W_*<=n^{o(1)}V`; this branch already forces the face coefficient up to
   at least `a`.
2. If `a=c+o(1)`, leading coefficients alone do not imply (21), because the
   uncontrolled `o(L^2)` error can dominate every rank gain `O(L)`.
3. If `c>a` by a fixed constant, the guaranteed relative mass is only
   `2^{-(c-a+o(1))L^2}`.  Even taking source rank `K=Theta(L)`, (11c) stays
   negative by `Theta(L^2)`, so no fixed-power raw density follows.

This is not merely a loose choice of `L/8`.  From a guaranteed fibre of
coefficient `a`, ranks below `(a-delta)L` have only
`2^{(a-delta)L^2+o(L^2)}` possible decorated occurrences and are negligible.
The best ensuing rank conversion is still only

\[
        \log M\ge aL^2+(a-\delta)L-o(L^2),              \tag{22}
\]

which cannot catch `cL^2` when `c>a`.  For the currently available
universal reservoir coefficient `a=1/4`, a hypothetical configuration with
face coefficient near `1/2` has a quadratic gap of about `L^2/4`; raw rank
conversion restores at most about `L/4` bits.

An exact abstract scale model saturates this limitation.  Take
`V_L=2^(cL^2)`, `W_L=2^(aL^2)`, histories of rank `floor(aL)` and weight
`2^(-floor(aL))`, and hence raw count

\[
              M_L=2^{aL^2+aL+O(1)}.                    \tag{23}
\]

For `c>a`, `M_L/V_L=2^{-(c-a)L^2+O(L)}`.  Assigning all these histories to
one completion bank of size `V_L` gives raw density tending to zero while
respecting the pointwise weight bound.  This is an arithmetic/interface
regression, not a claimed planar order-type construction; it proves that
the current numerical hypotheses alone cannot imply relative heaviness.

## 6. Relation to the rank-mismatch identity

For rank-resolved histories and completion faces,

\[
 {N_{j,e,r}\over C_{e,s}}
 ={q_{j,e,r}\over p_{e,s}}\,2^{r+2j-s}.                \tag{24}
\]

When `s>r+2j`, a large likelihood ratio need not give large raw density in
that particular rank pair.  Theorems 1--3 do not contradict (24).  They say
that a globally heavy fibre cannot put **all** of its raw mass into such
low-density pairs: if it did, the corresponding ordinary completion banks,
summed once with their true global load, would already pay the mass by (6).

This also explains why a guarded downshadow is secondary in this branch.
For a rank-`s` completion face, the number of endpoint-retaining rank-`k`
downfaces is

\[
                              \binom{s-2}{k-2}.          \tag{25}
\]

Those downfaces can improve a particular cell, but their codegrees may be
large.  The direct completion bank already yields the exact global
low-density payment (6), without trying to allocate (25).  Downshadows are
needed only after (17), inside the surviving genuinely high raw-density
cell, where they can be used for further geometric descent.

## 7. Exact remaining assumptions

Theorem 3 applies to the final profile bin only after checking two facts in
that bin:

1. the localized weighted mass is `V/n^{o(1)}`, rather than merely a fixed
   absolute power of `n`; and
2. the actual marked completion banks satisfy (4) with
   `Lambda=n^{o(1)}` after all root, mark, and tangent roles are included.

The weighted-history collapse `sum_j omega(U,j)<=1` prevents manufacturing
the first fact by recounting one source at many depths.  Conversely, once
the two facts hold, rank mismatch is rigorously eliminated by Theorem 3;
no assumption about the completion rank `s` remains.

## 8. Verification

Run

```bash
python3 \
  phase2/loop/erdos838/agent_outer_internal_product/verify_raw_completion_density_bridge.py
```

The verifier enumerates the exact rational nine-point planar configuration
used in the two-reference Hall audit.  It reconstructs every radial history,
checks (3) and (9)--(11) exactly, groups histories by genuine endpoint
completion banks, checks that those banks partition the nontrivial faces,
and verifies Theorem 2 for every distinct raw-density threshold occurring
in the instance.  It also audits the abstract high-rank estimate with exact
rational arithmetic and writes `raw_completion_density_bridge_certificate.json`.
