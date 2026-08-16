# Detached-load two-bank recovery and a scalable released-gap regression

**Date:** 2026-08-15.  This audits the last hypotheses in
`MULTIROLE_ENDPOINT_POCKET_TRANSFER.md`.

## Verdict

The marginal detached decoder load `Lambda_det` can be exponentially large,
even for distinct actual convex source/release contexts.  It should not be
bounded directly.  There is instead an exact two-face recovery:

\[
 \boxed{
   \text{released base }C_{c,F}=B_c\cup F,qquad
   \text{detached face }D_{e,F,v}=F\cup\{v\}.}               \tag{1}
\]

Both coordinates are ordinary faces.  Their intersection recovers `F`,
their differences recover `B_c` and `v`, and `v` recovers its matching edge
`e`.  If `mu_det` is the actual residual multiplicity after this decoding,
then for any weighted detached record family of total weight `H`,

\[
                         \boxed{H\le\mu_{\rm det}V(P)^2}.     \tag{2}
\]

Thus

\[
                              V(P)\ge\sqrt{H/\mu_{\rm det}}. \tag{3}
\]

This is the correct Hall/Cauchy response to high detached load.  It is a
two-bank coefficient-half bound, not a one-face multiplier.

The consecutive-gap qualification in the multirole theorem is also sharp.
There is a scalable rational family with `q` pairwise nonadjacent old source
gaps such that:

* every endpoint and every endpoint pair is a valid convex ear over the old
  source base;
* one common convex pocket trace destroys **all q** old gaps in the released
  hull and hides both endpoints in every role; and
* every detached set `F union {v}` remains convex.

Consequently old gap names, even a complete nonadjacent matching of them,
cannot be fed into the multirole product after release.  Actual consecutive
edges of `C_(c,F)` must be recomputed.

The same construction has `2^M` distinct released contexts sharing each
detached output, so `Lambda_det=2^M`.  Their released bases form an explicit
`2^M`-face bank, and the pair decoder in (1) has load one.  This exactly
exhibits what (2) records.

## 1. Weighted two-bank theorem

Let a detached compatible record be

\[
                         r=(c,e,F,v),                         \tag{4}
\]

with weight `w_r`, where `v` is an endpoint of the marked matching edge
`e`.  Assume

\[
 C_r=B_c\cup F\in\mathcal F(P),\qquad
 D_r=F\cup\{v\}\in\mathcal F(P),\qquad
 v\notin C_r.                                               \tag{5}
\]

Define the true pair load

\[
 \mu_{\rm det}=max_{C,D}
   \sum_{r:(C_r,D_r)=(C,D)}w_r.                              \tag{6}
\]

> **Theorem 1 (detached two-bank recovery).**  If
> `H=sum_r w_r`, then (2)--(3) hold.

**Proof.**  Group the record weight by the ordered pair `(C_r,D_r)`.  Each
pair carries weight at most (6), and there are at most `V(P)^2` ordered
pairs of ordinary faces.  This proves (2).

The decoder is concrete.  From (5),

\[
 F=C_r\cap D_r,\qquad v\in D_r\setminus C_r,qquad
 B_c=C_r\setminus F.                                        \tag{7}
\]

The endpoint label `v` identifies its disjoint matching edge.  Hence (6)
contains only context data not determined by the actual released base,
pocket trace, endpoint, and edge--for example an omitted carrier or guard
history.  QED.

The theorem is valid verbatim with arbitrary nonnegative weights and
cross-context collisions.  It also applies role by role or after summing
all detached-compatible cells in the multirole theorem.

This does not automatically restore the `n^{Theta(log log n)}` positive
multirole multiplier: (3) is a square-root bank.  Its value is at the
coefficient-half scale.  Any stronger use must combine it with the
independent pocket/source mass without counting the same face coordinate
twice.

## 2. Scalable rational gap-reset family

Fix integers `q>=1` and `M>=0`.  Put

\[
                         P_i=(i,i^2).                         \tag{8}
\]

Use the core base

\[
 A_0=\{P_0,\ldots,P_{2q+1}\}                                \tag{9}
\]

and optional tail

\[
 T=\{P_{2q+2},\ldots,P_{2q+M+1}\}.                          \tag{10}
\]

For role `j=0,...,q-1`, set `r=2j`.  Relative to the edge
`P_rP_(r+1)`, whose affine line at parameter `t` is

\[
 L_r(t)=\bigl(r+t, r^2+(2r+1)t\bigr),                       \tag{11}
\]

define

\[
\begin{aligned}
 x_j&=L_r(1/2)-(0,1/10),\\
 a_j&=L_r(1/4)-(0,3/100),\\
 b_j&=L_r(3/4)-(0,3/100).                         \tag{12}
\end{aligned}
\]

Let

                             F=\{x_0,\ldots,x_{q-1}\}.       \tag{13}

The selected old edges are pairwise nonadjacent: the unselected edge
`P_(2j+1)P_(2j+2)` separates successive roles.

### 2.1 Old ears are genuine

The successive slopes of the parabola chain are `2i+1`.  At role `j`,
write `s=2r+1`.  Inserting `a_j,b_j` replaces the old slope `s` by

\[
                         s-0.12,quad s,quad s+0.12,          \tag{14}
\]

strictly between the neighboring base slopes `s-2` and `s+2`.  Therefore

\[
 A\cup\{a_j\},\quad A\cup\{b_j\},\quad
 A\cup\{a_j,b_j\}                                           \tag{15}
\]

are convex for every `A=A_0 union S`, `S subseteq T`.  Thus `{a_j,b_j}`
is a genuine old-base convex ear.

Likewise `x_j` replaces `s` by `s-0.2,s+0.2`.  All these replacements and
the untouched separating slopes remain increasing, so

\[
                            C_S=A_0\cup S\cup F               \tag{16}
\]

is convex for every tail mask `S`.

### 2.2 Release destroys every gap and endpoint

In local coordinates with `P_r=(0,0)`, `P_(r+1)=(1,0)`, the three new
labels are

\[
               x=(1/2,-1/10),\quad
               a=(1/4,-3/100),\quad b=(3/4,-3/100).           \tag{17}
\]

At horizontal coordinate `1/4`, the lower side of the triangle
`P_r x P_(r+1)` has height `-1/20`, while `a` has height `-3/100`.
Thus `a` is strictly inside that triangle; the symmetric statement holds
for `b`.  Consequently

\[
 C_S\cup\{a_j\},\quad C_S\cup\{b_j\}                        \tag{18}
\]

are nonconvex.  The old edge `P_rP_(r+1)` has been replaced by the two
edges through `x_j`, so it is not a boundary edge of `C_S`.  The endpoints
are interior, hence they are not ears at either new consecutive edge.

This happens simultaneously in all `q` roles.  Therefore the candidate
gap list inherited from `A` has zero valid roles after release, despite
being a nonadjacent list before release.

### 2.3 Detached branch and exponential load

The pocket points lie on the translated parabola

\[
                           y=x^2+3/20,                        \tag{19}
\]

while `a_j,b_j` lie on `y=x^2+63/400`.  Direct slope comparison shows

\[
                         F\cup\{a_j\},\quad F\cup\{b_j\}     \tag{20}
\]

are convex.  Hence every one of the `2q` endpoints lies in the perfect
detached branch.

As `S` ranges over the `2^M` tail masks, the detached output (20) is
unchanged.  Thus each has marginal detached load exactly

\[
                           \Lambda_{\rm det}=2^M.             \tag{21}
\]

The released coordinate `C_S`, however, distinguishes all masks.  The
ordered pairs `(C_S,F union {v})` are all distinct, so
`mu_det=1`.  The erased tail is itself a convex-position shield with `2^M`
faces.  This family therefore demonstrates both the failure of a marginal
load bound and the exact payment exposed by Theorem 1.

The displayed formulas are strict for every fixed `q,M`.  If an accidental
collinearity occurs at a larger parameter, an arbitrarily small rational
perturbation preserves every hull/containment assertion and gives general
position.  The exact verifier needs no perturbation at `q=M=3`.

## 3. Consequence for multirole transfer

The positive theorem in `MULTIROLE_ENDPOINT_POCKET_TRANSFER.md` remains
correct when its candidate gaps are actual boundary edges of each released
base `C_(c,F)`.  The family above proves that none of the following weaker
inputs is sufficient:

* the gaps were consecutive in the old source face;
* the roles were pairwise nonadjacent before release;
* every endpoint pair was a commuting convex ear over that source; or
* the released pocket face itself is convex.

A mask/pocket hull can destroy every role at once.  The released cyclic
word, tangent neighbors, and active-gap mask must therefore be retained in
the context before applying the multirole product.

When detached compatibility is high but its marginal outputs collide, use
Theorem 1.  The remaining hard branch is now one of:

1. the pair load `mu_det` in (6) is still large because omitted
   carrier/guard histories survive even after `(C,D)` is fixed; or
2. detached compatibility is low, leaving the multirole tensor of double
   circuits wholly inside `F union {v}`.

The regression shows that large `Lambda_det` by itself is not evidence for
branch 2; it may simply be erased convex-base entropy.

## 4. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_detached_load_gap_reset.py
```

Expected output:

```text
PASS: gap-reset universe=20 contexts=8 records=48 detached=6 load=8 pair_outputs=48; weighted total=313/21 banks=6x12 pair_load=1
```

The verifier uses exact `Fraction` arithmetic.  At `q=M=3` it checks general
position of all 20 labels, every source ear and pair ear in all eight tail
contexts, convexity of every released base, destruction of all three old
boundary gaps, both endpoint failures, all detached faces, marginal load
eight, and pair load one.  A separate weighted collision table verifies
(2) with nonintegral weights and nontrivial pair reuse.
