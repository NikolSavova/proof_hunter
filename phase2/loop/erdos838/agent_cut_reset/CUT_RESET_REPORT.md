# Erdős 838: exact contiguous-cut transfer and the reset obstruction

> **Post-audit correction (2026-08-13).**  The conditional `1/3`
> calculation below also assumes
> `log C(I)+log U(I)>=(1/2-o(1))log^2|I|` for arbitrary point sets.
> That product estimate is not a standard known theorem; it is itself an open
> directional-mass target.  Thus `(C)+(T)` alone does not establish `1/3`.
> The exact kernel factorization and finite certificates are unaffected.

**Date:** 2026-08-13
**Verdict:** exact cut theorem proved; the proposed single-bridge reset is
false in the strongest possible way.  No unrestricted coefficient above
`1/4` is claimed here.  The first still-plausible quantified replacement is
isolated in (C) and (T) below.  With the additional unproved cap--cup product
input stated in Section 5 they would give coefficient `1/3`; a multiscale
persistence strengthening would still be needed for `1/2`.

All calculations are exact.  The checker is `cut_kernel.py` in this
directory.

## 1. Notation

Write the points as `p_1,...,p_n` in increasing horizontal order and assume,
after a harmless perturbation, that incident chord slopes are distinct.  For
an edge `e=(i,j)` put `q_e=slope(p_i p_j)` and

\[
 T_e(z)=I+zE_{ji}.
\]

The increasing-slope product `A(z)` counts cups by their two endpoints and
the decreasing-slope product `B(z)` counts caps.  Fix a contiguous cut

\[
 L=\{1,\ldots,m\},\qquad R=\{m+1,\ldots,n\},
\]

and let `E(L,R)` be its cross edges.

For a threshold `q`, define four filtered path matrices.

* `U_L^{<q}` is the increasing-slope product of internal `L` edges of slope
  below `q`.
* `U_R^{>q}` is the increasing-slope product of internal `R` edges of slope
  above `q`.
* `C_L^{>q}` is the decreasing-slope product of internal `L` edges of slope
  above `q`.
* `C_R^{<q}` is the decreasing-slope product of internal `R` edges of slope
  below `q`.

For a cross edge `e=(i,j)` put

\[
\begin{array}{ll}
 a_e(s)=(U_L^{<q_e})_{i,s},& r_e(t)=(U_R^{>q_e})_{t,j},\\
 b_e(s)=(C_L^{>q_e})_{i,s},& d_e(t)=(C_R^{<q_e})_{t,j}.
\end{array}                                                    \tag{1}
\]

Every entry here is a polynomial in `z`; the notation suppresses `z`.

## 2. Exact contiguous-cut theorem

> **Theorem 1 (slope-filtered cut factorization).**  For `s in L,t in R`,
> \[
> A_{t,s}(z)=z\sum_{e\in E(L,R)}a_e(s)r_e(t),\qquad
> B_{t,s}(z)=z\sum_{f\in E(L,R)}b_f(s)d_f(t).                 \tag{2}
> \]
> Consequently, if
> \[
> K_L(e,f)=\sum_{s\in L}a_e(s)b_f(s),\qquad
> K_R(e,f)=\sum_{t\in R}r_e(t)d_f(t),                       \tag{3}
> \]
> then the cross-block contribution to the convex-set partition function is
> \[
> \boxed{X_{L|R}(z)=z^2\sum_{e,f\in E(L,R)}K_L(e,f)K_R(e,f).} \tag{4}
> \]

**Proof.**  An increasing-horizontal path from `L` to `R` has exactly one
cross edge `e=(i,j)`.  It is a cup precisely when its prefix slopes are below
`q_e` and its suffix slopes are above `q_e`.  This gives the first identity
in (2), including the factor `z` for `e`.  Reversing all inequalities proves
the cap identity.  Multiply the two expressions, sum over their common
global endpoints `s,t`, and separate the `s` and `t` sums.  This is (4).
No inequality or decomposability hypothesis is used.  The same proof works
for a type-A reflection order, with slope comparisons replaced by root
order comparisons.  QED.

Thus the exact boundary state exposed by a cut is not a scalar cap/cup pair.
It is the two-bridge kernel `(K_L(e,f))`: `e` is the lower-hull/cup bridge and
`f` the upper-hull/cap bridge.

## 3. Two structural facts

> **Lemma 2 (the equal-bridge diagonal is trivial).**  For every cross edge
> `e`,
> \[
> K_L(e,e)=K_R(e,e)=1.                                      \tag{5}
> \]

For example, if a nonidentity term contributed to `K_L(e,e)`, there would be
a cup from `s` to `i` all of whose slopes are below `q_e`, and a cap with the
same endpoints all of whose slopes are above `q_e`.  The chord slope `q_{si}`
is a positive weighted average of the consecutive slopes of either path, so
it would be both below and above `q_e`, a contradiction.  Only the two
identity paths at `i` remain.  The right-hand statement is reflected.  The
reflection-order proof uses convexity of the root order.

This kills a natural version of the hoped-for reset: **failure at a bridge
cannot put mass into the opposite statistic at the same bridge.**  Every
nontrivial crossing convex set is necessarily an off-diagonal transfer
`e != f`.

> **Lemma 3 (ordered support).**  In a geometric realization, draw a vertical
> separator inside the cut strip.  If `e != f` and
> `K_L(e,f)K_R(e,f)>0`, then `e` meets the separator strictly below `f`.

Indeed a contributing cup and cap have the same extreme endpoints.  They
are the lower and upper hull chains of their union, so their respective cut
bridges occur in this vertical order.  This was also checked exactly on every
coordinate family below.

Lemmas 2--3 show the correct persistent object: an **ordered pair of exposed
bridges**, not one slope threshold or one endpoint coordinate.  A future
reset proof has to move mass from one off-diagonal pair to another while
remembering this order.

## 4. Quantified anti-avoidance attempts

Put

\[
 S_L=\sum_{e,f}K_L(e,f),\quad S_R=\sum_{e,f}K_R(e,f),\quad
 E=|L||R|.                                                    \tag{6}
\]

The clean average-collision guess

\[
 X_{L|R}\ \ge\ \frac{S_LS_R}{E^2}                            \tag{7}
\]

is false even for exact rational point sets.  On the 16-point dyadic Horton
set,

\[
 (E,S_L,S_R,X)=(64,7940,7940,5329),
\]

and

\[
 \frac{XE^2}{S_LS_R}=\frac{1364224}{3940225}=0.34622\ldots.
\]

The explicit 12-point integral configuration

```text
(i,y_i),  y = [-677058,-3660524,535511,4765981,-4127906,8538748,
                4609976,4593410,5357026,5928495,7488423,9074704]
```

is a stronger stretchable anti-alignment certificate:

\[
 (E,S_L,S_R,X)=(36,1512,2421,693),\qquad
 \frac{XE^2}{S_LS_R}=\frac{66}{269}.                         \tag{8}
\]

The polynomial-loss version remains live:

\[
 \boxed{X_{L|R}\ge n^{-O(1)}\frac{S_LS_R}{E^2}.}             \tag{C}
\]

It held in the checker on the six-point cell, its audited 36-point iterate,
the Horton family, the certificate (8), and random reflection orders through
`n=13`.  This is evidence, not a proof; the tested ratio decreased with `n`
and a superpolynomial decay has not been excluded.

Aggregate boundary masses also do not determine the crossing trace.  The
following two six-point integral configurations, cut after point 3, have
identical child data

\[
 (C_L,U_L,V_L)=(C_R,U_R,V_R)=(6,7,7)
\]

and identical `(S_L,S_R)=(59,62)`, but crossing traces `36` and `35`:

```text
y = [47732327,-47889601,8927488,65242589,-36349432,94616416]
y = [96932891,-82941997,-39598354,7172190,-79138602,-20420550]
```

Thus even the oriented child cap/cup totals plus both scalar boundary masses
are not an exact hereditary state.  Their different entrywise kernel
alignment is essential.

## 5. The first plausible incremental theorem

The experiments suggest separating anti-avoidance into collision (C) and a
tangent-mass statement.  A useful quantified tangent target is

\[
\begin{aligned}
 S_L&\ge n^{-O(1)}|R|^2\min\{C(L),U(L)\},\\
 S_R&\ge n^{-O(1)}|L|^2\min\{C(R),U(R)\}.                    \tag{T}
\end{aligned}
\]

The same assertions with no polynomial loss are false (random reflection
orders already give ratios below one), but (T) survived thousands of random
reflection orders and random rational point sets through `n=13`, with the
smallest observed constant ratios around `0.83`.  Again this is not a proof.

There is a concrete reason to attack exactly (C)+(T).  Let `L,R` be balanced,
let `mu=log V(P)`, and put

\[
 F=\tfrac12(\log(n/2))^2-O(\log n).
\]

The standard cap--cup product bound gives
`log C(I)+log U(I)>=F` for each child `I`.  Since `C(I),U(I)<=V(P)<=2^mu`,

\[
 \log\min(C(I),U(I))\ge F-\mu.
\]

If (C) and (T) hold with polynomial loss, (4) gives

\[
 \mu\ge\log X_{L|R}\ge2(F-\mu)-O(\log n),
\]

and hence

\[
 \boxed{\log V(P)\ge\tfrac13(\log n)^2-O(\log n).}          \tag{9}
\]

This would be the first universal improvement over `1/4`.  Reaching `1/2`
would then require the strong-tree idea: repeated tangent failures must
preserve *which off-diagonal bridge coordinate* received the mass, so later
cuts can charge it rather than paying the `2/3` one-shot reset loss.

## 6. Why tangent history appears unavoidable

Appending a right point to a cap/cup path is decided by its final slope.  If
the append fails, the external point has a unique tangent contact farther
back on the chain; a suffix is discarded.  Iterating this operation records
a sequence of tangent contacts, not a fixed endpoint or a binary orientation.
Lemma 2 explains why collapsing that sequence to one threshold loses all
nontrivial mass.  A proof of (T) would need a bounded-fibre tangent-pruning
map, with a dichotomy of the following kind:

* either pruning fibres are polynomial, yielding (T); or
* a large fibre contains enough independently selectable discarded cap/cup
  vertices to give the desired convex-subset lower bound directly.

This is the minimal concrete reset subproblem left by the cut calculation.

## 7. Exact verification

Run

```bash
python3 phase2/loop/erdos838/agent_cut_reset/cut_kernel.py --selftest
```

The script independently verifies (4) against the full matrix cross block,
asserts (5), checks the bridge-height support on realizable examples, and
prints the following key cases.

| family | `E` | `S_L` | `S_R` | `X_{L|R}` | max kernel term |
|---|---:|---:|---:|---:|---:|
| `T_(4,2)` | 9 | 54 | 54 | 36 | 1 |
| audited `T_(4,2)[T_(4,2)]` | 324 | 210924 | 210924 | 423801 | 144 |
| dyadic Horton, `n=16` | 64 | 7940 | 7940 | 5329 | 100 |
| stretchable anti-alignment (8) | 36 | 1512 | 2421 | 693 | 14 |

At a strong glue, the formulas reduce exactly to

\[
 S_L=|R|^2C(L),\qquad S_R=|L|^2U(R),\qquad
 X_{L|R}=C(L)U(R),
\]

so the normalized collision ratio in (7) is exactly one.  This confirms that
Theorem 1 genuinely extends the strong-tree crossing term, while the Horton
and anti-alignment examples identify the new loss outside that class.

## 8. Bottom line

The contiguous-cut formula is now exact and executable.  It rules out a
same-bridge reset universally and shows that the first nontrivial hereditary
state is an off-diagonal two-bridge kernel.  I did not prove (C), (T), or the
full RPR inequality.  The sharpest next attack is a bounded-fibre
tangent-pruning proof of (T), followed by a planar-network/correlation proof
of (C).  Proving both would already move the universal coefficient from
`1/4` to `1/3`; retaining the resulting bridge coordinate over nested cuts is
the remaining route to `1/2`.
