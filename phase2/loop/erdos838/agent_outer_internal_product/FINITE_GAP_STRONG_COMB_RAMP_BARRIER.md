# Finite-gap induction stalls on a growing strong-comb profile ramp

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

Even after granting the stationary common-triangle fibre a fixed linear
strong-comb chart, the finite-gap induction does **not** recover the missing
`n^{Theta(loglog n)}` factor from scalar child face counts.  The exact
heterogeneous recurrence has a finite pair-safe max-plus optimization whose
value in the live range `2<=q<=h-2` is

\[
                              \boxed{h}.                 \tag{1}
\]

Here `q` is the number of role blocks and `R^h` is the common child face
scale, with `R=1+D` for `D` labels per role.  The profile baseline is
quadratic because every pair is both a cap and a cup.  The integral
pair-safe ramp

\[
                 x=(2,2,3,\ldots,q)                    \tag{2}
\]

makes every forward cap--cup term at most `R^h`.  The sum over all terms
costs only `O(q^2)`.  This remains true while each formal child satisfies
all scalar constraints

\[
 C_i,U_i\ge D+{D\choose2},\qquad C_i,U_i\le W_i,
                    \qquad C_iU_i=W_i=R^h.                       \tag{3}
\]

Consequently, when `D=2^d`, `q=rho d` and an induced `D`-point child has the
half-scale bank `R^h=2^{(1/2+o(1))d^2}`, the recurrence may remain at that
child scale.  Re-expressing the desired half bound at
`N=(q+O(1))D` needs an additional

\[
              2^{(1-o(1))d\log q}=N^{(1-o(1))\log q},           \tag{4}
\]

which is exactly the missing quasipolynomial factor.  The rank-at-most-two
cloud traces allowed by the stationary `1+3` obstruction contribute only a
polynomial factor and do not change (4).

There is also an exact weak-baseline optimization over
`1<=x_i<=h-1`, valid for all `h,q`, whose value is `max(h,q)`; the
pair-safe form (1)--(3) is the one used in the geometric scale audit.

This is an exact **recurrence barrier**, not a planar upper construction.
To turn (2) into a construction one must recursively realize a growing menu
of marked child order types whose assembly profiles cover
`Omega(q/log q)` distinct cap/cup levels and whose completed parents export
the marked chart needed at the next scale.  No such recursive state is
known.  Treating the numbers in (2) as primitive children would be circular:
at half scale their required low face counts and broad directional menu are
the unresolved heterogeneous cap--cup problem itself.

There is a sharp positive remnant.  If the profile sequence has a forward
defect

\[
       \Delta=\max\!\left\{0,
          \max_{i<j}\bigl((j-i)-(x_j-x_i)\bigr)\right\},        \tag{5}
\]

then one ordinary forward bank has size `R^h R^(Delta-1)`.  In particular,
if only `K` integral profile levels occur, then

\[
       \Delta\ge\lceil q/K\rceil-1,
       \qquad W(P)\ge R^hR^{\lceil q/K\rceil-2}.                 \tag{6}
\]

Thus a fixed or `o(q/log q)`-width menu *does* pay the required factor.  The
only scalar survivor is a genuinely growing, nearly unit-slope profile
ramp.

## 1. What the stationary triangle sign leaves

In `FULL_WORD_TRIANGLE_REUSE_SCALE_BARRIER.md`, a variable base-role label
`z` and every three-set `T` in either physical cloud satisfy

\[
                              z\cup T\text{ is bad}.              \tag{7}
\]

By heredity, a face retaining any variable word label has trace rank at most
two in each cloud.  Put

\[
                         K_2(m)=1+m+{m\choose2}.                   \tag{8}
\]

For `M=D^q` full words, all rank-at-most-two traces in two `m`-point clouds
therefore give at most `M K_2(m)^2` different word-retaining candidates.
Even if every candidate is ordinary and load one, its gain over the source
bank is at most `m^4`, not `n^{Theta(loglog n)}`.

There is a more precise fixed-chart description.  Suppose the cloud and the
base-role cells lie in an exact linear strong composition.  A multi-block
face is classified by its first and last occupied blocks:

* its first trace is a cap in the assembly direction;
* its last trace is a cup;
* every strictly intermediate occupied block contributes exactly one
  label.

Every zero-, one-, or two-point cloud trace is both a cap and a cup (the
monotonicity condition is vacuous below rank three).  Hence a two-point
cloud trace may coexist with an arbitrary singleton **prefix** when the
cloud is the last occupied block, or with an arbitrary singleton
**suffix** when it is first.  It cannot be placed between nonempty prefix
and suffix in this exact composition.  A singleton cloud trace can be
intermediate.  Thus a cloud at an outer end supplies at most
`K_2(m)D^q`, while a cloud at an internal cut supplies the corresponding
one-sided prefix and suffix banks.  These are again only polynomial
multipliers over `M`.

The stationary sign (7) alone does not imply this strong-comb
classification.  We deliberately grant the stronger fixed-chart hypothesis
in the next sections.  Since even that stronger reduction stalls, no claim
that (7) by itself closes the branch is being made.

## 2. Exact heterogeneous recurrence

Let `X_1 prec ... prec X_q` be a linear strong composition.  Write
`n_i=|X_i|`, and let `W_i,C_i,U_i` be respectively its nonempty ordinary,
cap, and cup counts in the actual assembly chart.  First/last occupied
block classification gives the exact recurrence

\[
 W(P)=\sum_{i=1}^qW_i+
       \sum_{1\le i<j\le q}C_iU_j
          \prod_{i<k<j}(1+n_k).                         \tag{9}
\]

If singleton endpoint guards are added on both sides, (9) additionally has

\[
 \sum_{j=1}^qU_j\prod_{k<j}(1+n_k)
 +\sum_{i=1}^qC_i\prod_{k>i}(1+n_k)
 +\prod_{k=1}^q(1+n_k)+2.                              \tag{10}
\]

Equations (9)--(10) are equalities: the first and last traces and the
intermediate empty/singleton choices recover every output.

For completeness, every local ordinary face injects into its lower and
upper hull chains, so `C_iU_i>=W_i`.  Every singleton and pair belongs to
both directional classes, giving

\[
 C_i,U_i\ge n_i+{n_i\choose2}.                          \tag{11}
\]

The minimax calculation below is therefore compatible with, and slightly
stronger than, the universal scalar data used by finite-gap induction.

## 3. Exact finite max-plus theorem

Set all `n_i=D`, put `R=D+1`, and fix integers `h>=2`, `q>=2`.  Consider the
formal scalar children

\[
 W_i=R^h,\qquad C_i=R^{x_i},\qquad U_i=R^{h-x_i},qquad
                         1\le x_i\le h-1.               \tag{12}
\]

Substituting (12) into the guarded recurrence gives

\[
\begin{aligned}
 \mathcal R_R(x)={}&2+qR^h+R^q
  +\sum_{j=1}^qR^{h-x_j+j-1}
  +\sum_{i=1}^qR^{x_i+q-i}\\
 &+\sum_{1\le i<j\le q}
               R^{h+x_i-x_j+j-i-1}.                   \tag{13}
\end{aligned}
\]

Let `E(h,q;x)` be the largest exponent appearing in (13).

> **Theorem 1 (weak-baseline integral ramp minimax).**
>
> \[
>             \min_{x\in\{1,\ldots,h-1\}^q}E(h,q;x)
>                              =\max\{h,q\}.            \tag{14}
> \]
>
> Moreover
>
> \[
> R^{\max\{h,q\}}\le\min_x\mathcal R_R(x)
>       \le(q+3)^2R^{\max\{h,q\}}.                    \tag{15}
> \]

**Proof.**  The local term `R^h` and the guard-to-guard term `R^q` prove
the lower bound.

If `q<=h`, choose

\[
               x_1=1,\qquad x_i=i-1\quad(2\le i\le q). \tag{16}
\]

The left-guard exponents are at most `h`, the right-guard exponents are at
most `q`, and an internal forward exponent is `h` when `i=1` and at most
`h-1` otherwise.

If `q>h`, put `p=q-h+2`, set `x_i=1` for `i<=p`, and set
`x_i=i-p+1` for `i>p`.  A direct substitution shows that all left-guard,
right-guard, and internal exponents are at most `q`.  The largest exponent
is therefore `max(h,q)` in both cases.  Finally (13) has fewer than
`(q+3)^2` positive monomials, proving (15).  QED.

Writing `y_i=x_i-i`, the internal exponent has the transparent form

\[
            h+x_i-x_j+j-i-1=h-1+y_i-y_j.               \tag{17}
\]

This proves (5): any positive drop of `y` by `Delta` produces the factor
`R^(Delta-1)` over the child bank (and when `Delta=0` the local child bank
is stronger than this vacuous bound).  If only `K` values of `x_i` occur,
one value occurs at least `ceil(q/K)` times; when there are at least two
occurrences, the first and last are separated by at least
`ceil(q/K)-1`.  The case of one occurrence is already trivial from the
local bank.  This proves (6) in all cases.

Equivalently, avoiding an `R^s` gain forces

\[
                  x_j-x_i\ge j-i-s-1\qquad(i<j),       \tag{18}
\]

and every exact profile level appears only `O(s)` times.  At the live
target `s=Theta(log q)`, the surviving menu has width
`Omega(q/log q)`.

The actual directional profiles have the stronger pair baseline.  The
following shifted form is the live theorem.

> **Corollary 2 (pair-safe ramp).**  If `h>=4` and
> `2<=q<=h-2`, then
>
> \[
> \min_{x\in\{2,\ldots,h-2\}^q}E(h,q;x)=h.             \tag{18a}
> \]
>
> It is attained by `x_1=2` and `x_i=i` for `2<=i<=q`.
> Every formal child then has
> `C_i,U_i>=R^2>=D+{D choose2}` and `C_iU_i=W_i=R^h`.

Indeed the local term gives the lower bound.  Substitution of the shifted
ramp gives left-guard exponents at most `h-1`, right-guard exponents at
most `q+1<=h-1`, and internal exponents at most `h`.  Thus the stronger
unavoidable rank-two baseline does not change the obstruction whenever
`q<=h-2`, which includes the fixed-gap range below.

## 4. Half-scale coefficient audit

Take `D=2^d`, `q=floor(rho d)` with fixed `0<rho<1/2`, and
`h=floor(d/2)`.  Since `log R=d+o(1)`, the formal child scale is

\[
                           R^h=2^{(1/2+o(1))d^2}.       \tag{19}
\]

For every fixed `rho<1/2`, Corollary 2 applies for large `d` and permits
the entire guarded recurrence to be only
`q^{O(1)}R^h`.  But a parent has

\[
                       N=(q+O(1))D,qquad
                       \log N=d+\log q+O(1/q),          \tag{20}
\]

and the half-scale target is

\[
 2^{\frac12(\log N)^2}
 =R^h\,2^{(1-o(1))d\log q}.                            \tag{21}
\]

The polynomial number of recurrence terms and the rank-two factors in
(8) contribute only `2^{O(d+log q)}`.  They are negligible compared with
the `Theta(d log q)` exponent in (21).

More generally, if a finite-gap induction supplies child scale
`2^{(a+o(1))d^2}` and `q=(rho+o(1))d` with `rho<a`, the same pair-safe ramp stalls
at coefficient `a` on the child logarithmic scale.  Passing from `D` to
`qD` still asks for `2^{(2a-o(1))d log q}` additional faces.  Thus the
argument is not special to the exact coefficient one half.

## 5. The explicit recursive state still missing

The scalar ramp is not a construction primitive.  A noncircular recursive
realization would have to provide, at each scale `d`, a growing collection
of **marked two-chart states**

\[
                \mathfrak P_{d,k}=(P_{d,k};\alpha_{d,k},\beta_{d,k}),
                \qquad k\in\mathcal K_d,               \tag{22}
\]

with all of the following properties.

1. `|P_(d,k)|=2^{d+o(d)}` and
   `W(P_(d,k))<=2^{(a+o(1))d^2}` uniformly in `k`.
2. In the construction chart `alpha_(d,k)`, its endpoint counts realize a
   prescribed level `x=k+o(d)` with
   `log_R C=x+o(d)` and `log_R U=h-x+o(d)`.
3. The level set has width `|K_d|=Omega(d/log d)` and contains a sequence
   satisfying the ramp inequalities (18) for `q=Theta(d)` independently
   recharted child copies.
4. After those copies are assembled, the **completed** parent exports the
   marked chart `beta` required for its occurrence at the next scale, while
   keeping the same face-count bound.  The output state and all input marks
   must be verified in one rational order type; they cannot be assigned as
   independent scalar numbers after assembly.
5. The transition from the states at scale `d` to every state needed at
   the next scale is recursive from a fixed finite seed.  Importing a fresh
   low-face child for each ramp level is not allowed.

Independent child copies need only service their current construction
chart and one future reset chart, so a false `q`-direction query of one
copy is not being imposed here.  Conversely, merely knowing that `PGL_2`
is transitive on an ordered pair of directions does not prove item 4: the
completed parent's endpoint spectrum is a geometric output of the whole
assembly.  Existing exact menu searches show favorable one-level resets
but no self-reproducing transition of the form (22).

This is the precise surviving construction problem.  The scalar recurrence
and finite-gap induction cannot rule it out, while no actual recursive
state satisfying (22) has been built.

## 6. Scope and adjacent false exits

Theorems (9)--(18) are exact.  The coefficient audit is an obstruction to
proofs using only the child face scale, endpoint product, and linear
strong-comb recurrence.  It neither constructs a planar sub-half family nor
shows that every stationary common-triangle fibre admits such a recurrence.

No cyclic omitted-gap shell theorem for arbitrary children is used here.
Pairwise strong separation or a directed context cycle does not imply that
arbitrary child endpoint traces glue around the cycle; the scalable
parabola endpoint-profile counterexample already kills that step unless an
additional joint shell/seam hypothesis is proved.  Thus the cycle/DAG
proposal does not bypass the ramp barrier.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_finite_gap_strong_comb_ramp.py
```

Expected output:

```text
PASS: strong-comb minimax, profile defect/menu bound, and half-scale loss
```
