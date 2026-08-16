# Fixed detached-pair load: source masks and deleted-run Hall banks

**Date:** 2026-08-15.  This continues
`DETACHED_LOAD_TWO_BANK_AND_GAP_RESET.md` at the residual pair load
`mu_det`, and uses the mask-run lemma in
`../agent_common_shield_mixing/MULTIROLE_ENDPOINT_POCKET_TRANSFER.md`.

## Verdict

Before fixing the pair, there is an unconditional Hall strengthening of
the earlier `C,D` square bound.  Every detached record has the two ordinary
faces

\[
                         W=F\cup\{v\},\qquad Q=B\cup\{v\}. \tag{0}
\]

The second is part of the source-side endpoint compatibility hypothesis.
Fractional Hall routing to `{W,Q}` gives `H<=eta_*V(P)`, where `eta_*` is
the maximum weighted edge density of a subfamily (Theorem 0 below).  The
pair `(W,Q)` recovers exactly the same data as `(C,D)`, so this improves
the global routing but does not alter the fixed-pair residue.

After the two ordinary outputs

\[
                  C=B\cup F,\qquad D=F\cup\{v\}              \tag{1}
\]

are fixed, they recover `B,F,v` and the matching mark `e`.  If a remaining
record came from the ordinary source

\[
                         A=B\cup G,                            \tag{2}
\]

then the omitted carrier mask `G` is recovered by the source face `A`.
Consequently, if `kappa_src` is the total weight of the heaviest fibre over
one actual source, a fixed detached-pair fibre of weight `H` satisfies

\[
                     \boxed{H\le \kappa_{\rm src}V(P).}       \tag{3}
\]

Whenever the old endpoint extension `A union {v}` or the full old pair-ear
face `A union e` is ordinary, it gives the same one-face decoder: since
`v,e` are already fixed by `D`, deleting the fixed endpoint mark(s) recovers
`A`.  It does not give an independent second coordinate.  This is the
fixed-`(C,D)` specialization of the source-ear routing theorem in
`../agent_outer_internal_product/DETACHED_LOAD_SOURCE_EAR_HALL.md`.

There is also an exact one-face Hall bank from every deleted mask.  Choose
one longest cyclic run `R(G)` canonically.  Every nontrivial set

\[
              B\cup J,\qquad \varnothing\ne J\subseteq R(G), \tag{4}
\]

is an ordinary face.  If `Lambda_run` is the maximum weighted incidence
load of one output in (4), then

\[
 \boxed{
   \sum_\omega w_\omega (2^{|R(G_\omega)|}-1)
                       \le \Lambda_{\rm run}V(P).}            \tag{5}
\]

Thus masks of size at least `t` and at most `s` cyclic runs give

\[
             \boxed{V(P)\ge
               {H(2^{\lceil t/s\rceil}-1)\over\Lambda_{\rm run}}.} \tag{6}
\]

Equations (3) and (6) are genuine ordinary **one-face** banks.  They leave
one sharply identified residue: several omitted guard or noncanonical
reset descriptions may have the same actual source `A`.  Neither `A` nor
`A union {v}` decodes such descriptions.  Canonical radial reset depth and
carrier are in fact decoded by `(A,e)` (Lemma 2 below).  For genuine
likelihood-weighted radial histories the more general residue is already
bounded by `WEIGHTED_HISTORY_DOMINATION_AND_COMPLEMENT_NO_GO.md`; for other
raw histories an explicit actual-mark/source-history multiplicity bound is
still necessary.

A scalable rational example realizes `mu_det=2^M` for one fixed pair
`(C,D)` with `2^M` distinct actual sources.  Its source bank, old
source-endpoint bank, and one long-run Boolean bank all have exactly `2^M`
members.  Hence large pair load is possible, but source variation is paid
losslessly.  Artificially copying every record `h` times multiplies the
pair load by `h` without changing any face; this is the exact reason that
chronology multiplicity cannot be inferred from planarity alone.

## 0. Unconditional detached/base-endpoint Hall routing

For a detached record `omega`, let `W_omega,Q_omega` be (0).  The endpoint--
pocket hypotheses give both as ordinary faces: `W` is the definition of
detached compatibility, while `Q=B union {v}` is the old source-side
compatibility required before the pocket is retained.  Give the record
weight `w_omega`, and define

\[
 \eta_*=max_{\varnothing\ne\Omega'\subseteq\Omega}
   {\sum_{\omega\in\Omega'}w_\omega
    \over |\bigcup_{\omega\in\Omega'}\{W_\omega,Q_\omega\}|}. \tag{0a}
\]

> **Theorem 0 (base--pocket two-target Hall).**  The records admit a
> fractional routing to ordinary faces in which every face receives load
> at most `eta_*`.  In particular,
> 
> \[
>                              H\le\eta_*V(P).             \tag{0b}
> \]

**Proof.**  Make a flow network with capacity `w_omega` into each record,
infinite arcs from the record to its one or two targets, and capacity
`eta` from every ordinary target to the sink.  The max-flow/min-cut
condition is exactly the family of inequalities in (0a).  At
`eta=eta_*` all weight routes.  Summing the at-most-`eta_*` loads over at
most `V(P)` ordinary faces proves (0b).  QED.

This route is unconditional within the endpoint--pocket setup and can be
far stronger than either marginal decoder.  If `m` records share one `W`
and have distinct `Q` targets, then `eta_*=m/(m+1)<1`.

Assume the base, pocket, and endpoint role supports are disjoint.  Then

\[
 v=W\cap Q,\qquad F=W-\{v\},\qquad B=Q-\{v\}.             \tag{0c}
\]

The endpoint label recovers its matching edge `e`.  Conversely,

\[
 F=C\cap D,\quad v=D-C,\quad B=C-F,
 \qquad W=D,\quad Q=B\cup\{v\}.                          \tag{0d}
\]

Thus `(W,Q)` and `(C,D)` are bijective encodings of `B,F,v,e`; their true
parallel-edge residual multiplicity is identical.  In one fixed pair
fibre all records have the same `W,Q`, so Theorem 0 deliberately has no
further leverage.  The source-mask results below begin exactly there.

## 1. The fixed-pair source decoder

Let `Omega_(C,D)` be a weighted family of detached records producing the
fixed ordered pair (1).  Assume `v notin C` and that `D-C={v}`.  Then

\[
 F=C\cap D,\qquad v\in D\setminus C,\qquad B=C\setminus F.    \tag{7}
\]

Each record `omega` has an ordinary original source `A_omega` containing
`B`; put `G_omega=A_omega-B`.  Define

\[
 H=\sum_\omega w_\omega,\qquad
 \kappa_{\rm src}=
   \max_A\sum_{\omega:A_\omega=A}w_\omega.                  \tag{8}
\]

> **Theorem 1 (source completion bank).**  Equation (3) holds.  If every
> old endpoint extension
> 
> \[
>                         Q_\omega=A_\omega\cup\{v\}         \tag{9}
> \]
> 
> is ordinary and `v notin A_omega`, then the same bound holds using only
> the output family `{Q_omega}`.  Likewise, if the old pair ear
> `E_omega=A_omega union e` is ordinary and disjointly role-coloured, the
> family `{E_omega}` gives the same bound.

**Proof.**  Group the record weight by the ordinary source `A_omega`.
Each group has weight at most `kappa_src`, and there are at most `V(P)`
distinct sources.  For the second assertion, `v` is fixed and
`A_omega=Q_omega-{v}`, so `A -> Q` is injective.  For a pair ear,
`A_omega=E_omega-e` after the fixed endpoint role is read.  QED.

The word *actual* in (8) matters.  A list of several chronological routes
to the same selected source is not several source faces.  Conversely, if
the upstream record is a set-valued source incidence and fixes all its
other actual marks, then `kappa_src=1`; if it has a certified description
load `L`, then `kappa_src<=L`.

### 1.1 Canonical radial depth is already decoded

There is no residual reset-depth multiplicity in the canonical radial
peeling used by the Hall bridge.  Write an ordered rank-`k` source as

\[
                        A=\{u_1<\cdots<u_k\}.             \tag{9a}
\]

At depth `j` its retained carrier and endpoint pair are

\[
 T_j(A)=\{u_{j+1},\ldots,u_{k-j}\},\qquad
 e_j(A)=\{u_{j+1},u_{k-j}\}.                             \tag{9b}
\]

> **Lemma 2 (source--endpoint depth decoder).**  For fixed `(A,e)`, there
> is at most one canonical depth `j` with `e_j(A)=e`; when it exists,
> `T_j(A)` is determined as well.

**Proof.**  The left endpoint `u_(j+1)` has a different rank in `A` for
every `j`.  Hence the unordered pairs `e_j(A)` are distinct.  Formula
(9b) then determines the carrier.  QED.

Consequently, if the fixed detached pair supplies the same endpoint mark
`e` as the radial history, raw canonical peeling contributes no factor to
`kappa_src`.  If the only remaining actual choice is a guard/source mark
of maximum degree `d` over `(A,e)`, then

\[
                         \kappa_{\rm src}\le d,
                 \qquad H\le dV(P).                       \tag{9c}
\]

This statement is deliberately scoped to canonical symmetric peeling.
An arbitrary reset tree, or a construction exporting several noncanonical
charts, needs its own description bound.

### 1.2 Actual exterior guards give a target bank

Suppose the remaining mark is an actual exterior guard `y notin A`, and
its ordinary repaired target is

\[
                         T(A,y)=\operatorname{ext}(A\cup\{y\}). \tag{9d}
\]

Because `y` is exterior, `y in T(A,y)`, while every other target label lies
in `A`.  Hence for one fixed source

\[
                           T(A,y)-A=\{y\},                \tag{9e}
\]

so distinct guards give distinct ordinary target faces.  Let `s` be the
number of actual sources in a fixed detached-pair fibre, let `d` be its
maximum number of distinct guards above one source, and let `h` bound the
residual multiplicity of one actual tuple `(A,y)`.  The source bank has
size `s`, while the repaired targets above a source of degree `d` give a
bank of size `d`.  Since `H<=hsd`,

\[
                         \boxed{V(P)\ge\sqrt{H/h}.}       \tag{9f}
\]

For set-valued canonical radial records, Lemma 2 gives `h=1` after all
other actual marks are fixed.  Thus simultaneous carrier and actual-guard
variation in one fixed `(C,D)` fibre already has a coefficient-half
one-face payment.  What (9f) does not handle is a dense global family in
which target faces are reused across different sources, or noncanonical
metadata copies of the same `(A,y)` tuple.  The former calls for the full
source--target Hall graph; the latter is not geometric incidence entropy.

There is a useful marked variant.  Suppose a history has an actual guard
`y_omega`, the union `A_omega union {y_omega}` is ordinary, has rank at
most `q+1`, and the actual tuple `(A_omega,y_omega)` has history load at
most `h`.  From the unmarked union there are at most `q+1` choices for
which label is `y`.  Hence its output load is at most `(q+1)h`, giving

\[
                         H\le(q+1)hV(P).                    \tag{10}
\]

This conditional observation must not be applied to a hiding repair:
when `y` hides part of `A`, the full union need not itself be an ordinary
face.

## 2. Full-mask and longest-run downshadows

For every record, heredity of convex position gives the full Boolean
reservoir

\[
       {\cal D}^+(\omega)=
                \{B\cup J:\varnothing\ne J\subseteq G_\omega\}. \tag{11}
\]

Define its maximum weighted output load by

\[
 \Lambda_{\rm all}=\max_W
       \sum_{\omega:W\in{\cal D}^+(\omega)}w_\omega.         \tag{12}
\]

Double-counting the incidences `(omega,W)` gives

\[
       \boxed{\sum_\omega w_\omega(2^{|G_\omega|}-1)
                         \le\Lambda_{\rm all}V(P).}          \tag{13}
\]

For the form which interfaces directly with the cyclic reset analysis,
let `r(G)` be the number of maximal cyclic runs of deleted labels in the
source word `A`, and choose the first longest run `R(G)` in a fixed
orientation and label order.  Restrict (11) to nonempty `J subseteq R(G)` and call
the corresponding maximum load `Lambda_run`.  The same incidence count
proves (5).  Lemma 4 of `MULTIROLE_ENDPOINT_POCKET_TRANSFER.md` gives

\[
                         |R(G)|\ge\lceil |G|/r(G)\rceil,      \tag{14}
\]

which proves (6).

Equivalently, after duplicating an ordinary output according to its
weighted capacity, (5) is a Hall routing with congestion
`Lambda_run/(2^ell-1)` when all canonical runs have length at least `ell`.
No released gap is used: (4) consists only of downfaces of the original
source.

Omitting `J=emptyset` is essential for the Hall formulation: the common
base `B` would otherwise occur in every reservoir and force
`Lambda_run>=H`.  For a single source one may restore `B`, obtaining the
absolute Boolean bank of exactly `2^|R|` faces.

### 2.1 Exact splice with the mask-run corollary

Fix a run threshold `s`.  A mask of rank at least `t` has exactly one of
the following forms.

1. `r(G)<s`.  Then (14) supplies a run of length at least
   `ceil(t/(s-1))` (or the slightly weaker `ceil(t/s)`), and the one-face
   bank (5) applies.
2. `r(G)>=s`.  Before the pocket is inserted there are exactly `r(G)`
   compressed source gaps.  If enough remain actual consecutive gaps of
   the released hull, the multirole endpoint transfer applies.  If the
   pocket destroys them, one is in its low endpoint-entropy/double-circuit
   branch; destruction does **not** imply a long run.

This is precisely the caveat in Section 5.1 of the multirole report.  The
present theorem adds the missing payment on the genuinely few-run side,
but does not relabel destroyed released gaps as mask runs.

## 3. What the source and pair faces do not decode

For fixed `(C,D)`, the source output `A`, the old endpoint output
`A union {v}`, and the old pair-ear output `A union e` carry exactly the
same information because `v,e` are fixed.
Therefore two records with the same actual source and different omitted
guard/reset histories collide in both banks.  The run bank (4) also
depends only on `A` after the canonical run is chosen.

This is an information-theoretic obstruction, not a missing planar lemma.
If one replaces every geometric record by `h` differently named copies,
then `H`, `kappa_src`, `Lambda_all`, and `Lambda_run` all scale by `h`,
while the point configuration and every ordinary face bank are unchanged.
Such copies are not automatically distinct selected incidences.  They are
legitimate only when the upstream construction supplies `h` actual marks;
then one must retain one of those marks in an ordinary output or prove a
separate decoder bound.

For canonical radial histories, Lemma 2 additionally removes reset depth
and carrier once `(A,e)` is known.  The surviving raw load is therefore an
actual guard/mark degree, not the number of paths reaching that state.

In the genuine radial likelihood normalization, Theorem 1 of
`WEIGHTED_HISTORY_DOMINATION_AND_COMPLEMENT_NO_GO.md` gives total history
weight at most `L V(P)` for description load `L`, so this last residue is
already harmless.  In a raw-count application, canonical peeling gives
only whatever explicit depth/guard multiplicity has actually been proved;
it cannot be replaced by the number of names in a chronology tree.

## 4. A fixed-pair scalable rational regression

Use the coordinates of Section 2 in
`DETACHED_LOAD_TWO_BANK_AND_GAP_RESET.md`.  Fix `q>=1` and `M>=0`, the
parabola core

\[
                         B=\{P_0,\ldots,P_{2q+1}\},         \tag{15}
\]

the consecutive tail `T={P_(2q+2),...,P_(2q+M+1)}`, and the pocket face
`F={x_0,...,x_(q-1)}`.  Fix one role `j`, its pair `e={a_j,b_j}`, and one
endpoint `v=a_j`.  For every `S subseteq T`, take the original source

\[
                         A_S=B\cup S.                       \tag{16}
\]

Release **all** of `S` and retain `F`.  Every record now has the same

\[
                         C=B\cup F,\qquad D=F\cup\{v\}.      \tag{17}
\]

The exact slope calculations from the earlier report show simultaneously
that

* `A_S`, `A_S union {v}`, and `A_S union e` are ordinary;
* `C` and `D` are ordinary; and
* `C union {v}` is nonconvex, so this is a genuine detached cell.

Thus one fixed pair (17) has

\[
                          \mu_{\rm det}=2^M.                 \tag{18}

\]

The `2^M` sources (16) and old endpoint faces `A_S union {v}` are all
distinct.  For the top source `A_T`, the deleted tail is one consecutive
cyclic run of length `M`; its downshadow (4) is exactly the entire source
bank (16).  Hence (3), the endpoint version of (3), and the absolute
long-run bank are simultaneously tight in their exponential parameter.

This corrects the contextual interpretation of the earlier scalable
example: retaining the tail in `C_S` gives marginal detached load `2^M`
but pair load one; deleting the selected tail gives the fixed pair (17)
and true residual pair load `2^M`, paid by the original source masks.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_detached_pair_source_mask_hall.py
```

Expected output:

```text
PASS: fixed-pair universe=21 sources=16 pair_load=16 source_bank=16 endpoint_bank=16 long_run_bank=16; abstract Hall histories=20 full_inc=111 run_inc=81 Lambda_all=9 Lambda_run=9 hall_star=5/6
```

The checker uses exact `Fraction` arithmetic.  It verifies general
position, all sixteen original source/source-endpoint/source-pair faces,
the common released and detached faces, endpoint hiding, exact fixed-pair
load, and the full length-four Boolean run bank.  It also exhausts a
weighted abstract mask table to check (3), (5), (13), the cyclic longest-
run inequality, the source--endpoint depth decoder, and the exact
fixed-fibre guard Cauchy bound (9f), and the exact invariance under history
duplication.  A brute-force weighted target-graph
enumeration verifies (0a)--(0b), including the exact star value `5/6`.
