# Erdős 838: the exact Boolean collision kernel for pair descent

**Date:** 2026-08-14  
**Verdict:** the correct quadratic potential for a nested Boolean reset has
an exact closed form.  Its comparable/nested contribution is universally
bounded, without an inclusion-width hypothesis.  Every large collision
comes from incomparable carriers, precisely the pairs which must eventually
spend through an opposite-side tangent switch or recurse into a tagged
internal coordinate.

This sharpens the dynamic two-record gate but does not prove its remaining
global geometric reuse statement.

## 1. Boolean thinning as a fractional decoder

Let `D` be any finite family of faces.  A carrier `A in D` distributes one
unit of mass uniformly over its Boolean subfaces.  Thus the load at a face
`J` is

\[
 L(J)=\sum_{A\in\mathcal D:J\subseteq A}2^{-|A|}.           \tag{1}
\]

The total load is `sum_J L(J)=|D|`.  Its squared collision norm has the
following exact form.

> **Lemma 1 (Boolean collision identity).**
> \[
> \boxed{
> \sum_J L(J)^2
>   =\sum_{A,B\in\mathcal D}2^{-|A\cup B|}.}                \tag{2}
> \]

**Proof.**  Expand the square.  A face `J` contributes to the ordered pair
`(A,B)` exactly when `J subset A intersection B`.  Therefore its total
contribution is

\[
 2^{|A\cap B|}2^{-|A|}2^{-|B|}=2^{-|A\cup B|}.
\]

Summing proves (2).  QED.

Equation (2) is the `L^2` analogue of the one-record Boolean reset.  It
measures actual average reuse rather than the worst fibre of the empty face.

## 2. Nested collisions are automatically cheap

Call `(A,B)` comparable when one contains the other.

> **Theorem 2 (comparable-kernel bound).**
> For every family `D`,
> \[
> \boxed{
> \sum_{\substack{A,B\in\mathcal D\\A\subseteq B\text{ or }B\subseteq A}}
>       2^{-|A\cup B|}
> \le2|\mathcal D|.}                                      \tag{3}
> \]

**Proof.**  For one orientation,

\[
 \sum_{B\in\mathcal D}2^{-|B|}
       |\{A\in\mathcal D:A\subseteq B\}|
 \le\sum_{B\in\mathcal D}2^{-|B|}2^{|B|}
 =|\mathcal D|.                                           \tag{4}
\]

Reflect the containment direction.  The diagonal is counted twice, which
only strengthens the displayed upper bound.  QED.

Thus width is needed for a **maximum-fibre** Boolean decoder, but not for
the quadratic collision potential.  Once full outer tags are retained,
any superlinear term in (2) is carried by incomparable faces.

For the parabolic chain `D_t={1,...,t}`, `0<=t<=s`, every pair is
comparable and (2) is exactly

\[
 \sum_{t,u=0}^s2^{-\max(t,u)}
 =\sum_{k=0}^s(2k+1)2^{-k}<6.                             \tag{5}
\]

This is independent of the nesting depth.  It is the fractional version of
the constant `9/4` integral pair release in the dynamic Kraft report.

## 3. Product antichains put all excess in the forward branch

Let `D` be all transversals of `b` disjoint blocks of size `M`.  Distinct
carriers have the same size and are therefore incomparable.  Coordinatewise
factorization of (2) gives

\[
 \boxed{
 \sum_JL(J)^2
   =\left({M\over2}+{M(M-1)\over4}\right)^b
   =\left({M(M+1)\over4}\right)^b.}                        \tag{6}
\]

The comparable part is only the diagonal

\[
                         (M/2)^b.                           \tag{7}
\]

Hence the excess-to-comparable ratio is

\[
             \left({M+1\over2}\right)^b-1.                \tag{8}
\]

This is exactly the product-grid obstruction to a Boolean-only reset.  The
kernel does not pretend that the antichain is cheap: it directs essentially
all pair mass to the forward/two-ended branch.

## 4. Why complete tags are mandatory

Suppose every internal carrier occurs under `M` apex labels, as in ACP
Proposition 26.  If the apex is erased, every Boolean load in (1) is
multiplied by `M`, and its collision energy is multiplied by `M^2`.  If the
apex labels remain as separate tagged cells, the energies of the `M` cells
add and the multiplier is only `M`.  Thus

\[
 {\mathcal C_{\rm untagged}\over\mathcal C_{\rm tagged}}=M. \tag{9}
\]

This is the collision-kernel form of the exact `M^2/4` squared-overload
counterexample in `lattice_rectangle_counter/DYNAMIC_TWO_RECORD_GATE.md`.
An entropy-bearing coordinate cannot be erased until differing record pairs
have spent there or its own face complex has been entered.

For a product with alphabet sizes `m_1,...,m_q`, the probability that two
records remain together after the first `i` exposed coordinates is

\[
                         (m_1\cdots m_i)^{-1}.               \tag{10}
\]

Consequently the prefix collision Kraft sum is

\[
                  \sum_{i=0}^q(m_1\cdots m_i)^{-1}.          \tag{11}
\]

It is below two whenever every alphabet has size at least two.  The
ramp--plateau profile satisfies (11) with enormous slack; its exponential
atomic overload is caused by erasing the internal block tags, not by the
pair recursion.

## 5. Corrected dynamic gate

The exact collision potential at an active tagged cell of size `e`, split
into child cells of sizes `e_j`, is

\[
 e^2=\left(e^2-\sum_je_j^2\right)+\sum_je_j^2.              \tag{12}
\]

The first term is record-pair mass released at the first divergence; the
second is descending collision mass.  Equations (2)--(3) show that a nested
Boolean terminal adds no hidden depth or width loss in `L^2`.  Equations
(6)--(8) show that a product antichain must not terminate there: its
incomparable pair mass must be switched or recursively exposed.

This gives a sharper form of the remaining conjecture:

> **Tagged incomparable-pair gate.**  Preserve every entropy-bearing outer
> coordinate in the state.  For every hereditary subfamily, expose record
> pairs until either their discarded carriers are comparable, or they reach
> a common directed chord where both crossed tangent signs hold.  Comparable
> Boolean collision is charged by (3); switched pairs use the injective
> two-face decoder.  The total reuse of the resulting tagged face-pair banks
> must be `2^{o(r)}`.

Together with the dynamic pair-certificate theorem, this gate implies

\[
                         E^2\le2^{o(r)}V(P)^2
\]

and hence capped RNP.  The remaining unproved statement is no longer a
Kraft, depth, or inclusion-width inequality.  It is the planar assertion
that incomparable tagged carriers cannot repeatedly evade both tangent
switches while reusing the same ordinary face pair exponentially often.

## 6. Exact verification

Run

```bash
python3 phase2/loop/erdos838/agent_cyclic_stem_hw/verify_dynamic_collision_kernel.py
```

The verifier exhausts the comparable bound over every set family on up to
four labels, checks the parabolic identity through depth 128, independently
enumerates the product kernel in small cases, and checks the exact tag and
ramp--plateau Kraft factors.
