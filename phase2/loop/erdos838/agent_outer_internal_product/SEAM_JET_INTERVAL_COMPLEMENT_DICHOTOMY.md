# Literal interval circuits: exact complement repair for 2+2 traces and the 1+3 seam barrier

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The four-label seam theorem gives an exact positive branch for the literal
common-interval residual, but it does not repair the whole residual.

Fix an ordinary interval face `W`, an endpoint pair `e={ell,r}` straddling
it in the `x`-order, and a bad circuit trace `A subset W`.  Put `C=W-A`.
If the bad circuit is of type `2+2`, and therefore both one-ended sets

\[
                       W\cup\{\ell\},\qquad W\cup\{r\}             \tag{1}
\]

are ordinary, then

\[
                         \boxed{C\cup e\text{ is ordinary}.}       \tag{2}
\]

The reason is exact: the two singleton ears can fail only at one common
parent vertex `z`; every `2+2` witness contains `z`, while deleting `z`
turns the ears into automatically compatible singleton insertions on the
same new edge.  Thus (2) retains both endpoints and the entire discarded
complement.  Since `A` is fixed in the localized fibre, the output itself
recovers `W=A union C` and has decoder load one even if `W` is allowed to
vary across records.

This is already the desired activity-weighted Hall payment for the `2+2`
atom.  If a record `(W,e)` has aggregate radial tilt `eta_(W,e)`, put
`H=sum_(W,e) eta_(W,e)` and `eta_*=max_(W,e) eta_(W,e)`.  For one fixed
trace `A`, the distinct ordinary outputs `(W-A) union e` give

\[
             |\mathcal O|\ge {H\over\eta_*},\qquad
             H\le\eta_*|\mathcal O|\le\eta_*V(P).                  \tag{3}
\]

Consequently either one endpoint fibre has the prescribed heavy tilt, or
the full common-`W` weighted load is paid by tagged ordinary faces.  No
pointwise RMC estimate and no seam-state pigeonhole is used.

The `1+3` branch is genuinely different.  One endpoint is already
incompatible with `W`, so the seam theorem's individual-ear hypothesis is
false.  There is a scalable rational general-position regression in which
one fixed left-role trace `A={w_0,w_1,w_2}` is canonical for every one of
`N^2` endpoint pairs, yet `C union e` is nonconvex for every pair.  More
strongly, either endpoint is incompatible with every retained subset of
`W` of rank at least three.  Making a seam theorem applicable requires
deleting at least `|W|-2` interval labels, not four labels or a bounded
number of circuit traces.

Thus the exact live interface is:

* the common-trace `2+2` fibre is closed by the one-face complement bank;
* the `1+3` fibre is not repaired by four-label seam localization;
* genuine weighted histories in that remaining fibre are still subject to
  the independent packing bound `sum w_(U,j)<=V(P)`, but any raw or tagged
  continuation must use a one-sided blocker/repair bank rather than claim
  that `C` reattaches.

The verifier is

```text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_seam_jet_interval_complement.py
```

It checks a rational `2+2` complete endpoint rectangle with 64 varying
`(W,e)` records, literal radial tilts, exact tag recovery, and the load
inequality (3).  It then checks the scalable `1+3` regression and its
linear deletion requirement.

## 1. Setup and canonical hierarchy

Let `W` be a strictly convex planar set whose point abscissae are distinct.
Let

\[
         \ell_x<\min_{w\in W}w_x,
         \qquad r_x>\max_{w\in W}w_x.                              \tag{4}
\]

Thus every point of `W` lies in the open label interval of
`e={ell,r}`.  Suppose `W union e` is nonconvex.

It is useful to choose the circuit type hierarchically:

1. if `W union {ell}` is nonconvex, choose a canonical `1+3` circuit with
   left endpoint role;
2. otherwise, if `W union {r}` is nonconvex, choose a canonical `1+3`
   circuit with right endpoint role;
3. otherwise both one-ended unions are ordinary, and every bad circuit has
   type `2+2`.

This removes an artefact of lexicographically choosing a `2+2` circuit even
when a separate one-ended obstruction is present.  The positive theorem
below applies exactly to the third branch.

## 2. An adjacent seam is the only 2+2 obstruction

> **Theorem 1 (2+2 complement reattachment).**  Assume (1), while
> `W union e` is nonconvex.  Let `A subset W`, `|A|=2`, be the internal
> trace of any bad `2+2` circuit in `W union e`, and put `C=W-A`.  Then
> (2) holds.

**Proof.**  Apply endpoint-ear localization to the two ordinary one-ended
unions in (1).  The singleton `ell` replaces an edge `g_ell` incident with
the leftmost vertex of `W`, and `r` replaces an edge `g_r` incident with
the rightmost vertex.

If the two insertion edges are disjoint, the edge-splice lemma says that
the ears commute, contradicting the nonconvexity of `W union e`.

They cannot be equal either.  Equality forces the common edge to be the
empty side joining the leftmost and rightmost parent vertices.  Normalize
that edge to `(0,0)(1,0)` and put both ears below it.  Write

\[
             \ell=(s,t),\quad s<0,t<0,
             \qquad r=(u,v),\quad u>1,v<0.                         \tag{5}
\]

The two seam turns are

\[
 \chi((0,0),\ell,r)=sv-tu>0,
 \qquad
 \chi(\ell,r,(1,0))=t(1-u)-v(1-s)>0.                              \tag{6}
\]

Hence the same-edge seam criterion makes the joint union ordinary, again
a contradiction.

The insertion edges are therefore distinct and adjacent.  Write them as
`pz` and `zq`, where `z` is their common parent vertex.  The distinct-edge
splice lemma says that the only possibly bad turn of the joint boundary is
the turn at `z`.

Delete `z`.  By heredity, `W-z+ell` and `W-z+r` are ordinary.  Both
singletons now replace the same new parent edge `pq`, so (6), after an
affine normalization, shows that

\[
                         (W-\{z\})\cup e                              \tag{7}
\]

is ordinary.  Every bad four-circuit in `W union e` must consequently
contain `z`.  In particular `z in A`.  Therefore

\[
                    C\cup e\subseteq(W-\{z\})\cup e,
\]

and heredity proves (2).  QED.

The theorem is stronger than a finite-state partition.  It gives an actual
one-face repair for every pair in the fibre; no labels are guessed.
It is deliberately a **singleton-endpoint** theorem.  For multi-vertex
petal profiles, deleting the old seam vertex can expose a new bad turn
inside a petal, so (7) is false without fixing the new seam jet.  Literal
interval endpoint pairs have exactly the singleton form used here.

## 3. Exact decoder and activity-weighted Hall bound

Fix one trace/role state `(A,2+2 role)`.  Let `mathcal R` be any set of
records `(W,e)` satisfying Theorem 1 with that same `A`; the interval face
`W` may vary.  Put `C_W=W-A` and define

\[
       \mathcal O=\{C_W\cup e:(W,e)\in\mathcal R\}.                 \tag{8}
\]

Every output is ordinary.  Its two labels outside the open interval of `C`
recover `e`, while its internal trace recovers `C_W`; the fixed trace `A`
then recovers `W=A union C_W`.  Hence the record map is injective:

\[
                         |\mathcal O|=|\mathcal R|.                  \tag{9}
\]

Now give record `(W,e)` any nonnegative aggregate activity `eta_(W,e)`.
In the literal KL application this is

\[
          \eta_{W,e}=\sum_{j:\,W\subseteq I_e}h_{j,e}               \tag{10}
\]

restricted to the fixed circuit fibre.  Division by
`eta_*=max_(W,e) eta_(W,e)` and (9) prove (3), with `H` summed over
records.  In particular there is no residual varying-`W` collision inside
one fixed `2+2` trace state.

If different traces `A` or upstream descriptions are summed, let `Lambda`
be their maximum decoder load on one output.  The exact global version is

\[
                 \sum_c H_c\le
                   \left(\max_c\eta_{*,c}\right)\Lambda V(P).       \tag{11}
\]

For the live common-`W`, common-`A` fibre, `Lambda=1`.  Equation (11) does
not silently solve varying-tag overlap.

## 4. A scalable 1+3 regression

Fix `m>=6` and take the convex parabola chain

\[
                         w_i=(i,i^2),\qquad0\le i<m.                \tag{12}
\]

Let

\[
                \ell_0=(-1,-m^2),\qquad r_0=(m,-m^2).              \tag{13}
\]

For the ray from `ell_0` to `w_i`, the slope is

\[
             s_i={i^2+m^2\over i+1},\qquad
             s_{i+1}-s_i
                =1-{m^2+1\over(i+1)(i+2)}<0.                       \tag{14}
\]

The last inequality holds for every `i<=m-2`.  Consequently, for every
`i<j<k`, the point `w_j` lies strictly inside

\[
                         \operatorname{conv}\{\ell_0,w_i,w_k\}.     \tag{15}
\]

Indeed (14) puts `w_j` between the two rays from `ell_0`, while strict
convexity of the parabola puts it below the chord `w_iw_k`, on the same
side as `ell_0`.  At the right endpoint use the positive slope magnitude

\[
                 t_i={i^2+m^2\over m-i}.
\]

It is strictly increasing, since the numerator of `t_(i+1)-t_i` after
clearing its positive denominator is

\[
                   (2i+1)(m-i)+i^2+m^2>0.
\]

The identical ray-and-chord argument gives the analogue of (15) for
`r_0`.

All inequalities are strict.  Therefore, for every `N`, one may choose
`N` distinct rational points `L` in a sufficiently small neighbourhood of
`ell_0` and `N` distinct rational points `R` near `r_0`, avoiding the
finitely many forbidden lines, so that the whole configuration is in
general position and (15) holds for every endpoint in `L union R`.

Order all of `L` before `W` and all of `R` after `W`.  For every
`e={ell,r} in L times R`, the lexicographically first four-subset of
`e union W` is

\[
                         \{\ell,w_0,w_1,w_2\},                       \tag{16}
\]

and it is nonconvex.  Thus all `N^2` pairs share the fixed trace

\[
                    A=\{w_0,w_1,w_2\}                              \tag{17}
\]

and the left endpoint role.  Yet with `C=W-A`, `|C|=m-3>=3`, (15) gives

\[
                         C\cup e\text{ nonconvex}                   \tag{18}
\]

for every endpoint pair.

More strongly, if `K subset W` and `|K|>=3`, then both
`K union {ell}` and `K union {r}` are nonconvex.  Thus an endpoint becomes
an admissible singleton ear only after all but at most two interval labels
have been deleted.  At least `m-2` deletions are necessary.

This is an exact failure of the seam-jet proposal, not of its proof.  The
four-label theorem assumes that the parent plus each ear is already
ordinary.  In (18) that hypothesis remains false after deleting the fixed
three-label trace, or after any bounded number of trace deletions as
`m` grows.  Partitioning endpoint pairs into states cannot change this
geometric fact.

The construction is not asserted to be a counterexample to the global KL
bound.  Each pair is a legitimate blocked literal record and the endpoint
graph has `N^2` edges, but its actual likelihood weights may be discharged
by genuine-history packing, a heavy endpoint fibre, or a separate
one-sided blocker bank.  What it rules out is precisely the proposed
one-face reattachment of `C` via the four-label seam theorem.

## 5. Consequence for the live residual

The circuit hierarchy should be changed before continuing the Hall
descent:

1. prioritize one-ended `1+3` circuits;
2. send the remaining `2+2` cells through Theorem 1 and the weighted bank
   (3);
3. retain only the genuine one-sided `1+3` atom.

This strictly shrinks `(23r10j-k)`: `2+2` trace erasure is no longer a
residual.  The four-label seam theorem does not close the last `1+3` atom,
and the parabola regression shows that iterating bounded trace deletion is
not a substitute.
