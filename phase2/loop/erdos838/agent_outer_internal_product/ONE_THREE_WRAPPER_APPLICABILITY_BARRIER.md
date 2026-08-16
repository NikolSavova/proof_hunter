# A rooted 1+3 atom does not imply a lexicographic strong-glue wrapper

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The strengthened `1+3` interval obstruction does not, by itself, force the
sequential/lexicographic wrapper needed for a coefficient-one-half
fixed-point recurrence.

The distinction is exact.  A rooted `1+3` statement says that a proposed
mixed output is nonconvex because one label lies inside a triangle.  The
strong-glue recurrence needs a positive converse: after one macro cell is
omitted, every right profile at the preceding cell must splice with every
left profile at the following cell, together with all retained traces, to
one recoverable ordinary face.  The first property supplies none of the
second.

There is a seven-point rational counterexample.  Four cells are strictly
ordered in both fixed-edge tangent coordinates, in reverse directions; the
two complete singleton words are ordinary convex hexagons.  After the third
cell is omitted, however, the formal one-gap output is

\[
                            \{q,x,z,y\},                           \tag{1}
\]

where the interval trace `W={x,z,y}` is an ordinary triangle but

\[
 z={3\over230}q+{122\over575}x+{891\over1150}y.                   \tag{2}
\]

Thus `q union W` is exactly a rooted `1+3` circuit: the endpoint plus the
only three interval labels is bad.  This is simultaneously the claimed
one-gap cap/cup splice, and it is nonconvex even after the root edge is
deleted.  Hence the local `1+3` hypotheses are compatible with failure of
the first nontrivial strong-glue output.

There is a sharp conditional positive statement, already proved in
`ALTERNATING_FERRERS_PLANAR_WRAPPER.md`.  If one additionally assumes
lexicographic exposure, cyclic macro separation, and an exact decoder, then
one-gap profile multiplication gives the fixed-point constraint

\[
                         c\ge {1+\beta\over1+2\beta}>{1\over2}.    \tag{3}
\]

So a genuine lexicographic wrapper cannot stay below coefficient one half.
But (1)--(2) prove that this conclusion cannot be invoked for the residual
`1+3` fibre without first proving the missing exposure theorem.

Projective universality makes the gap structural.  Strict tangent and
circuit inequalities survive tiny substitution by arbitrary child order
types, while reflection swaps a child's cap and cup profiles without
changing its size, total face count, or the macro Ferrers incidences.
Consequently repeated atoms can be quadratically anti-aligned at their
directional seams.  Neither a common cage nor a local circuit trace selects
the aligned child orientations required by (3).

This is an applicability barrier, not a sub-half construction and not an
EIC' counterexample.  It leaves one precise positive target:

> show that a fixed-power share of live `1+3` atoms admits a separated
> omitted-cell seam whose two directional profiles and retained traces
> form a recoverable ordinary face, or charge the failed seam's `1+3`
> circuits to a globally recoverable external shield.

The exact verifier is

```text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_one_three_wrapper_applicability.py
```

It checks the rational rooted circuit, strict reverse dominance, both full
source words, failure of the one-gap splice with and without the root, the
conditional coefficient algebra, and an arbitrary-order-type projective
reset stress test.

## 1. What a strong-glue recurrence actually needs

Suppose cyclic macro cells `X_0,...,X_(q-1)` carry selected trace words.
For a gap `g`, write `R_(g-1)` for right exposed profiles in the preceding
cell and `A_(g+1)` for left exposed profiles in the following cell.  The
one-gap term used by the alternating wrapper is

\[
 (A/4)^{q-1}s^{q-3}R_{g-1}A_{g+1}.                              \tag{4}
\]

Its proof uses all of the following.

1. The surviving anchor word is valid after cell `g` is omitted.
2. Every chosen right profile and left profile splice across the new seam.
3. They remain compatible with every trace retained in the other cells.
4. The ordinary output recovers the partial word and both profiles.

The `1+3` obstruction is only the negation of one candidate output.  It
does not imply any of items 1--4.  In particular, deleting a blocker can
change both tangent neighbors of a local profile; broad dominance orders
do not control the resulting three-variable circuit.

Under items 1--4, cyclic cancellation gives

\[
 \prod_g R_{g-1}A_{g+1}=\prod_iA_iR_i\ge\prod_iH_i,              \tag{5}
\]

and the calculation in the alternating wrapper yields (3).  Therefore the
coefficient conclusion is rigorous but explicitly conditional on the
positive splice, not on the existence of bad `1+3` witnesses.

## 2. Exact rooted-circuit counterexample

Normalize the root edge to

\[
                         u=(-1,0),\qquad v=(1,0).                  \tag{6}
\]

Take

\[
 \begin{aligned}
 q&=(-19/20,1/20),&x&=(-3/40,7/8),&w&=(0,10/11),\\
 z&=(3/40,7/8),&y&=(2/15,8/9).
 \end{aligned}                                                   \tag{7}
\]

Their positive tangent coordinates `(L,R)` satisfy

\[
 L_q<L_x<L_w<L_z<L_y,
 \qquad R_q>R_x>R_w>R_z>R_y.                                    \tag{8}
\]

Use cells

\[
                  X_1=\{q\},\quad X_2=\{x\},\quad
                  X_3=\{w\},\quad X_4=\{z,y\}.                  \tag{9}
\]

Both selected words

\[
 \{u,v,q,x,w,z\},\qquad \{u,v,q,x,w,y\}                         \tag{10}
\]

are ordinary convex hexagons.  Thus the occupancy-one trace choices
cross-complete in the strongest possible two-word sense.  The pair
`{z,y}` is a two-point left and right boundary profile of the final cell.

Omit `X_3`.  The formal directional gap output is (1), consisting of the
other trace `q`, the left adjacent profile `x`, and the right profile
`{z,y}`.  Equation (2) has positive coefficients summing to one, so `z` is
strictly inside `conv{q,x,y}`.  Therefore (1) is nonconvex.  The six-point
set obtained by adjoining `u,v` remains nonconvex.

This is exactly a local instance of the strengthened barrier:

\[
 W=\{x,z,y\}\text{ is ordinary},\qquad
 q\cup W\text{ is a bad }1+3\text{ circuit}.                      \tag{11}
\]

Since `W` has precisely three labels, the condition “the endpoint plus any
three interval labels is bad” holds literally.  Yet it kills, rather than
creates, the desired omitted-cell face.  No infinitesimal or degeneracy
issue is involved; all seven points are rational and in general position.

## 3. Why repetition and universality do not repair the implication

Strict macro orientation inequalities are open.  A sufficiently small
projective substitution inside a cell preserves the tangent order and the
bad circuit (2), while allowing arbitrary intrinsic child order type on
coordinates not used by the witness.  Reflection of a child exchanges its
left/right cap and cup enumerators.

Thus local data of the following form are invariant under child
anti-alignment:

* the rooted `1+3` witness;
* the macro tangent/Ferrers order;
* selected singleton-word validity; and
* child size and total ordinary-face count.

The directional products `R_(g-1)A_(g+1)` are not invariant.  They can be
moved to incompatible anchor halves around an alternating cycle, exactly
as in `CYCLIC_FERRERS_PROFILE_TRANSFER.md`.  Quadratic word entropy and
large unweighted local reservoirs then coexist with zero adjacent marked
profile bank.

The separated alternating construction has an additional property which
defeats this anti-alignment: after one cell is omitted, equal parities meet
and the microchildren are lexicographically exposed.  That is a feature of
its chosen realization, not a consequence of (11).  The rational example
above shows the exposure implication already fails at four cells.

## 4. Exact residual

The coefficient route can use (3) only after proving a prevalence theorem
for lexicographic seams.  A sufficient form is:

\[
 \sum_{\text{recoverable gaps }g}
 R_{g-1}A_{g+1}\prod_{i\notin\{g-1,g,g+1\}}m_i
 \ge n^{-o(1)}\times\text{the formal cyclic profile mass}.        \tag{12}
\]

Every term must be an actual one-face bank and its output must recover the
source context at subpower load.  Failed terms must instead be charged to
their canonical `1+3` circuit shields.  Neither the strengthened local
barrier, the common marked face, nor Ferrers incidence proves (12).
