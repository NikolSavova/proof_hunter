# Loop-heavy blockers: the exact endpoint-reset gate and a seam counterexample

**Date:** 2026-08-15.  All logarithms are base two.  Face counts are
nonempty.

## Corrected verdict

The first version of this note incorrectly applied the half-quadratic
endpoint estimate from `agent_asymptotic/NEXT_ENDPOINT_ATTACK.md` to an
arbitrary planar atom.  That estimate was proved for an ordered
strong-decomposition tree in its compatible chart, not for an arbitrary
order type in an arbitrary projection chamber.  The unrestricted estimate

\[
       \log X(Q)+\log Y(Q)
          \ge \left({1\over2}-o(1)\right)(\log |Q|)^2                 \tag{1}
\]

is itself one of the campaign's open endpoint targets.  Therefore a
logarithmic outer strong-glue chain of arbitrary low-face/projectively
recharted children is **not** closed by the existing theorem.

What is valid is an exact conditional reset lemma.  If the children have
endpoint sum at least `F` in the actual chart used by the outer glue, then a
one-direction logarithmic chain promotes the root fixed-endpoint product to
`F-o(F)`.  It does not manufacture the missing factor two: the only
unconditional input from ordinary child faces is roughly
`F>=log V(Q)-2log|Q|`, which is only quarter-quadratic at the live lower
scale.

There is also a scalable exact obstruction to deriving the hypothesis from
the current low-mean loop data.  A `3+1` loop sees one label from a blocker
cluster.  Independent infinitesimal affine rotations of the blocker
children preserve every loop and every singleton macro transversal, while
making the `2+1` signs across adjacent seams mixed.  The verifier gives a
rational example with five local parabola points and three three-point
blocker clusters.

Thus the exact live gate is:

> prove half-quadratic endpoint energy for the arbitrary atoms in the
> projection charts selected by the loop-heavy wrapper, or extract a
> mixed-seam circuit/profile bank when that endpoint energy or strong-glue
> compatibility fails.

Neither low mean, common `3+1` loops, nor a singleton same-type product
currently supplies that input.

## 1. Endpoint states and their exact domain

For a point set `S` in a generic ordered chart, let `x_S(a)` count caps
whose left endpoint is `a`, including the singleton, and define the
right-endpoint cup count `y_S(b)` symmetrically.  Put

\[
 X(S)=\max_a x_S(a),\qquad Y(S)=\max_b y_S(b),            \tag{2}
\]

and

\[
 M(S)=\max\left(1,\max_{a<b}c_S(a,b)u_S(a,b)\right).     \tag{3}
\]

At a vertical strong glue `A\prec B`, with `a=|A|,b=|B|`, the exact
recurrences are

\[
\begin{aligned}
 X(A\prec B)&=\max\{(b+1)X(A),X(B)\},\\
 Y(A\prec B)&=\max\{Y(A),(a+1)Y(B)\},\\
 M(A\prec B)&=\max\{M(A),M(B),X(A)Y(B)\}.              \tag{4}
\end{aligned}
\]

They require the mixed `2+1` strong-glue signs.  The elementary endpoint
partition also gives

\[
                         X(S),Y(S)\le |S|M(S).           \tag{5}
\]

The half-quadratic estimate used by `NEXT_ENDPOINT_ATTACK` is valid at
nodes of the ordered strong-decomposition tree treated there.  It must not
be silently substituted into (4) for an arbitrary child.

There is a weaker universal bridge.  Let `C(S),U(S)` be total cap and cup
counts in the current chart.  Every ordinary face has a unique upper/lower
decomposition, while endpoint partitioning gives

\[
             V(S)\le C(S)U(S)\le |S|^2X(S)Y(S).          \tag{6}
\]

Consequently

\[
       \log X(S)+\log Y(S)\ge\log V(S)-2\log|S|.         \tag{7}
\]

At a child with only a quarter-quadratic ordinary-face guarantee, (7) is
only quarter-quadratic.  This is why the correction changes the coefficient
conclusion rather than merely an error term.

## 2. The valid q-ary reset lemma

> **Theorem 1 (conditional strong-chain atom reset).**  Let
>
> \[
>                         P=Q_1\prec\cdots\prec Q_q      \tag{8}
> \]
>
> be a vertical strong-glue chain of `q>=3` arbitrary planar atoms in one
> ordered chart.  Put `N=|P|`, `L=log N`, and assume in this chart that
>
> \[
>              \log X(Q_i)+\log Y(Q_i)\ge F             \tag{9}
> \]
>
> for every `i`.  Then
>
> \[
> \boxed{\quad
> \log V(P)\ge\log M(P)\ge
>   \min\left\{F-L,{q\over q+1}F-{2L\over q+1}\right\}.
> \quad}                                                \tag{10}
>

**Proof.**  Associate (8) as the right comb
`S_i=Q_i\prec S_(i+1)` and write `mu=log M(P)`.  Every atom and suffix is a
node of the comb, so (4) bounds its `M` by `M(P)`.  Equations (5) and
`|S_i|<=N` give

\[
                  \log X(T),\log Y(T)\le\mu+L           \tag{11}
\]

for every atom and suffix.  Each atom has endpoint sum at least `F`; every
suffix does too because both endpoint maxima are monotone under (4).

If `mu>=F-L`, the first term of (10) holds.  Otherwise put

\[
                  D=F-\mu>L,\qquad \ell=D-L>0.           \tag{12}
\]

Equations (9),(11) make every endpoint coordinate at least `ell`.  At the
deepest glue `Q_(q-1)\prec Q_q`, the forward term in (4) is at most
`2^mu`.  Writing lower-case letters for logarithms,

\[
             x_{q-1}+y_q\le\mu,
             \qquad y_{q-1},x_q\ge2D-L.                 \tag{13}
\]

Thus `S_(q-1)` has both coordinates at least `2D-L`.

At every later glue `Q_i\prec S_(i+1)`, the paid forward term says

\[
                   x_i+y(S_{i+1})\le\mu.                \tag{14}
\]

Together with `x_i+y_i>=F`, this gives

\[
                   y_i\ge D+y(S_{i+1}).                 \tag{15}
\]

Hence each of the `q-2` later attachments increases the inherited
`y`-coordinate by at least `D`.  The final paid cross yields

\[
                         \mu\ge qD-2L.                   \tag{16}
\]

Substitute `D=F-mu` to obtain the second term of (10).  Finally, for fixed
endpoints the union of a cap and cup is an ordinary face and uniquely
recovers the pair, so `V(P)>=M(P)`.  QED.

The theorem is useful but coefficient-neutral.  If `q=Theta(L)`, then

\[
                       \log V(P)\ge F-O(L).              \tag{17}
\]

Thus `F=(1/2-o(1))L^2` closes the chain, whereas
`F=(1/4-o(1))L^2` stays at one quarter.  The reset preserves a rich
endpoint exponent; it does not double it.

## 3. Consequences that are actually justified

There are three distinct atom regimes.

1. **Compatible strong-tree atom.**  If the atom is a node of an ordered
   strong-decomposition tree in the same chart, the endpoint theorem from
   `NEXT_ENDPOINT_ATTACK` supplies the half-quadratic `F`, and (17) closes.

2. **Already half-rich ambient atom.**  If
   `log V(Q_i)>=(1/2-o(1))(log|Q_i|)^2` and
   `|Q_i|=N/polylog(N)`, then the atom's ambient faces alone close, without
   Theorem 1 and in every rechart.

3. **Arbitrary low-face/recharted atom.**  Only (7) is presently automatic.
   At the live quarter scale this supplies `F=1/4 L^2-o(L^2)`, so (17)
   does not improve the coefficient.  This is the surviving common-guard
   ramp branch.

In particular, an arbitrary projection chamber can destroy the compatible
strong-tree order used in regime 1.  Ordinary face count survives the
projective move, but the directional endpoint state does not.  The exact
finite chamber computations in
`agent_root_followup/COMMON_GUARD_ALL_DIRECTION_AUDIT.md` are encouraging,
not an asymptotic theorem.

## 4. Loops are blind to the missing seams

> **Lemma 2 (one-label blindness).**  Let `X` be finite and let distinct
> macro blockers `c_1,...,c_q` satisfy finitely many strict conditions of
> the form
>
> \[
>                 p\in\operatorname{int}\operatorname{conv}\{a,b,c_i\},
>                                                               \tag{18}
> \]
>
> together with strict singleton-transversal orientation conditions.  For
> arbitrary finite planar children `R_i`, maps
>
> \[
>                   z\longmapsto c_i+\varepsilon A_i z             \tag{19}
> \]
>
> preserve all those conditions for sufficiently small positive
> `epsilon`, independently for every invertible `A_i`.

**Proof.**  There are finitely many strict determinant inequalities.
Every determinant in (18) or a singleton transversal converges to its
nonzero macro determinant as `epsilon` tends to zero.  One positive
epsilon preserves all signs.  QED.

The `2+1` signs required by (4) behave differently.  For two labels
`z,z'` in `R_i` and an external macro point `c_j`,

\[
 \operatorname{orient}(c_i+\varepsilon A_i z,
                        c_i+\varepsilon A_i z',c_j)
 =\varepsilon\det(A_i(z'-z),c_j-c_i)+O(\varepsilon^2). \tag{20}
\]

Choosing `A_i` so that `c_j-c_i` lies between two child secant directions
makes the signs in (20) both positive and negative.  This breaks the seam
without changing any loop or singleton transversal.

The verifier realizes this over the rationals.  Five parabola points have
the middle point of every triple hidden by every label in three three-point
blocker clusters.  All one-label-per-cluster macro transversals are convex
and the full configuration is in general position, yet both adjacent
natural seams have mixed `2+1` signs.

There is a useful mutation stress test on exactly the same macro.  Replace
the three rotated triangles by coherent near-parallel triangles so that both
adjacent seams (indeed, all three block pairs) have the uniform vertical
strong-glue signs.  Both placements
still have the same three-point child order types, all 90 loops, and all 135
singleton transversals.  Exact subset exhaustion gives

\[
\begin{array}{c|cc}
 &\text{mixed seams}&\text{coherent seams}\\ \hline
 V(\text{nine blocker labels})&273&274\\
 V(\text{full sixteen-point macro})&5833&6508.
\end{array}                                             \tag{21}
\]

Thus the most literal seam-regularizing mutation increases the full face
count by 675 in this regression.  This is not a certified global minimizer
and not an asymptotic construction, but it rules out a monotonicity claim
that minimization automatically prefers the coherent reset.

This is scalable: replace each blocker by an arbitrarily large child in
(19).  It is not a sub-half construction, because the resulting
nonhomogeneous cross-cluster face recurrence is uncontrolled.  It proves
only that the loop/low-mean extraction has not yet forced the hypothesis of
Theorem 1.

## 5. Precise remaining operation

The loop-heavy branch now requires one of the following genuinely new
steps.

* A direction-uniform endpoint theorem proving (1) for the relevant
  arbitrary atoms; this would feed Theorem 1 directly.
* A semialgebraic/entropy extraction which retains a macroscopic strong
  chain **and** half-quadratic endpoint energy in the induced child charts.
* A bank charged to the mixed `2+1` seam circuits created by Lemma 2.

Extracting only singleton same-type products or common `3+1` loop roles is
insufficient.  Minimizer status has not yet been used in a way that controls
these seam signs, so no minimizer-specific closure is claimed.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_loop_heavy_strong_glue_reset.py
```

The checker exhausts the conditional max-plus reset implication on 20,939
integer states.  Its asymptotic arithmetic checks are explicitly
conditional on a half-quadratic input `F`; they do not assert that input for
arbitrary atoms.  It also verifies the rational regression: general
position, 90 loop containments, 135 convex singleton macro transversals, and
both signs at both adjacent `2+1` seams.  It exhausts all subsets of both the
mixed and coherent placements to verify (21).
