# Referee-style audit of `proof_blowup_half.md`

## Recommendation and mathematical verdict

The main theorem is mathematically sound:

\[
 \limsup_{N\to\infty}\frac{\log_2 f(N)}{(\log_2N)^2}\leq\frac12.
\]

I found no counterexample to the mixed-triple realization, the cap/cup and
convex-set classification, the exact substitution formulas, the fixed
template exponent, or the passage from powers to arbitrary `N`.  Both exact
verification programs pass.

The draft is not yet referee-ready as written.  There are three required
repairs, none of which changes the construction or coefficient:

1. the rational-realization assertion needs rational input coordinates;
2. the Pascal template invokes an undefined strong-glue construction;
3. the `W_d` asymptotics should display the unrolled recurrence, and the
   lower bound should use an explicit constant instead of `+O_S(d)`.

Several additional presentational/citation repairs are listed below.  I do
not recommend altering the core file until the authors choose whether the
paper will cite the classical cups--caps construction or prove its recursive
realization.

## 1. Line-by-line audit

Line numbers refer to the 2026-08-13 version.

### Lines 13--25: theorem and counting convention

**Correct.**  Counting nonempty convex subsets rather than all subsets adds
or removes only one.  Removing all subsets of size at most two changes the
count by `O(N^2)`, whose logarithm is `O(log N)`, negligible on the
`(log N)^2` scale.

**Proposed repair.**  Define one convention once.  For example, let `w(P)`
count nonempty convex-position subsets throughout, and mention in one
sentence after the theorem that adding the empty set does not alter it.
The phrase "including or excluding ... sets of size at most two" is true but
unnecessarily invites a question about whether `f` changes definition later.

### Lines 27--40: provenance

**No proof issue.**  This belongs in the introduction, but repository paths
and a report that a targeted search found nothing do not belong in a final
paper.  Replace the abbreviated references by full bibliography entries and
state only the precise relation to prior art: generic blow-ups prescribe
within-block and transversal triples, whereas this realization additionally
fixes the two mixed triple signs used in Lemma 1.

### Lines 44--49: coordinate normalization

**Minor omitted hypothesis.**  A general-position set need not initially
have distinct `x`-coordinates.  A generic orientation-preserving linear map
first makes all `x`-coordinates distinct.  The stated shear then makes `y`
increase in the induced `x`-order and preserves orientations.

For rational input, choose the generic linear map and the shear with rational
coefficients outside finitely many forbidden values.  This preserves
rationality.

### Lines 51--78: mixed-sign realization

**The determinant argument is correct.**  If two points in block `i` have
micro-coordinate difference `(Delta x,Delta y)`, then against a later block
the determinant has leading term

\[
 -\varepsilon\,\Delta y\,(X_k-X_i)<0,
\]

and against an earlier block the corresponding leading term is positive.
One-block determinants are `epsilon^3` times the determinant in `Q`, and
three-block determinants tend to those in `S`.  Finiteness supplies a common
positive threshold for all determinants and all coordinate inequalities.

**Required repair R1.**  The sentence at lines 75--76 is false for arbitrary
irrational `S,Q`: rational `epsilon` does not make irrational input
coordinates rational.  Use either of the following exact formulations.

> If `S,Q` have rational coordinates, choose rational
> `0<epsilon<epsilon_0`; then `S[Q]` is rational.  For arbitrary real
> `S,Q`, the same construction gives a real realization.

All templates actually needed later may be chosen rational, so this is only
a quantifier repair.

Also say explicitly that `epsilon` may be chosen afresh at every finite
iteration.  No uniform threshold or limiting configuration is required.

### Lines 82--123: cap and cup formulas

**Correct, including `j=1`.**  A spanning cap has an arbitrary nonempty cap
in its first occupied block and exactly one point in every later block.  A
macro-cap of size `j` therefore contributes `C(Q)n^{j-1}`.  For `j=1`, the
term is `c_1(S)C(Q)=rC(Q)`, exactly the caps lying in one block.  The cup
statement is the reflected classification.

For readability, state this as a bijection, not only a summation argument.

### Lines 125--152: necessity for convex subsets

**Correct.**

* The lower hull reaches the last occupied block, so it cannot contain two
  points of the first occupied block; together those three points would have
  negative orientation.  Since every selected point of a convex-position
  set lies on one of its two boundary chains, the first-block intersection
  is a cap.  Reflection gives a cup in the last block.
* If an intermediate block contains `b_1<b_2`, representatives `a,c` from
  earlier and later blocks put `b_1,b_2` on the same side of `ac`, because
  both transversal triples inherit the same macro sign.  The two mixed signs
  then rule out either possible side.  The four-set is nonconvex, contradicting
  heredity of convex position.
* One representative per occupied block is a convex subset and has the
  corresponding macro order type, so the occupied macro-set is convex.

**Suggested clarification.**  At line 129 insert "every selected point is a
vertex of the selected set's convex hull" before concluding that all other
first-block points are on the upper chain.  At line 135 explicitly identify
the equal signs as `chi(a,b_1,c)=chi(a,b_2,c)`.

### Lines 154--166: converse classification

**Correct; this is the most important geometric lemma.**  Let `E` be the
chosen first-block cap and `F` the last-block cup.  The upper macro-chain,
with `E` inserted at its left endpoint and the rightmost point of `F` at its
right endpoint, is a cap: its triples are either internal to `E`, contain
two points of `E` followed by a later point, or inherit an upper macro-chain
sign.  The dual construction is a cup.  They share the leftmost point of
`E` and rightmost point of `F` as endpoints and together contain every
selected point.  The cap is strictly above the common endpoint chord and the
cup strictly below it, so they cannot cross.

This covers singleton endpoint intersections and the `j=2` case.  The data
`(B,E,F, intermediate points)` are recovered uniquely from the selected
set, so the factor `C(Q)U(Q)n^{j-2}` has neither omission nor overcount.

**Proposed repair.**  Promote the classification itself to a named lemma:

> A subset meeting at least two blocks is convex if and only if its occupied
> macro-blocks are convex, its first-block intersection is a nonempty cap,
> its last-block intersection is a nonempty cup, and every intermediate
> block contributes one point.

Then derive all three equations as a corollary.  This separates geometry
from enumeration and makes the converse quantifier unmistakable.

### Lines 170--190: cap/cup iteration

**Correct but should be written as an equality.**  Put

\[
 F_C(x)=\sum_{j\ge1}c_j(S)x^{j-1},\qquad
 F_U(x)=\sum_{j\ge1}u_j(S)x^{j-1}.
\]

Then

\[
 C_d=C_{d-1}F_C(r^{d-1}),\qquad
 U_d=U_{d-1}F_U(r^{d-1}).                         \tag{A}
\]

Because these positive polynomials have degrees `a-1,b-1`, respectively,

\[
\begin{aligned}
 \log C_d&={a-1\over2}(\log r)d^2+O_S(d),\\
 \log U_d&={b-1\over2}(\log r)d^2+O_S(d).
\end{aligned}                                    \tag{B}
\]

The difference between `d(d-1)/2` and `d^2/2` is absorbed by `O_S(d)`.

### Lines 193--227: the `W_d` recurrence

**The conclusion is correct, but the proof is too compressed for a paper.**
This is required repair R2.  Define

\[
 G(x)=\sum_{j\ge2}v_j(S)x^{j-2}.
\]

The exact recurrence and its unrolling are

\[
\begin{aligned}
 W_d&=rW_{d-1}+C_{d-1}U_{d-1}G(r^{d-1}),\\
 W_d&=r^dW_0+\sum_{s=1}^d r^{d-s}C_{s-1}U_{s-1}G(r^{s-1}).   \tag{C}
\end{aligned}
\]

Since `deg G<=r-2` is fixed, (B) shows uniformly in `1<=s<=d` that the
logarithm of the `s`-th summand is at most

\[
 {a+b-2\over2}(\log r)(s-1)^2+O_S(d).
\]

Taking the maximum and paying `log(d+1)` for the sum proves (5).  Conversely,
`v_2(S)=binom(r,2)>0`, so the `s=d` term gives the unambiguous bound

\[
 W_d\ge v_2(S)C_{d-1}U_{d-1}.                    \tag{D}
\]

Together with (B), this proves equality (7).  Replace line 218's
`>= ... +O_S(d)` by (D): a lower inequality containing an unsigned `O` term
is formally ambiguous.

### Lines 231--244: Pascal template

**The numerical indices are correct.**  In a strong glue `A prec B`, a cap
meeting both children consists of a cap in `A` and one point in `B`; a cup is
the reflection.  Thus the central cell `T_{2k-4,k-2}` has
`binom(2k-4,k-2)` points and maximum cap/cup sizes `k-1`.

**Required repair R3.**  The operation `prec`, its realizability, and the
boundary conditions for `T_{m,i}` have not been defined in this draft.
Calling the paragraph "for completeness" therefore overstates what was
proved.  Choose one of two repairs:

1. cite the classical cups--caps lower construction in its exact form and
   use only what the theorem needs: a rational set of
   `binom(2k-4,k-2)` points with maximum cap and cup at most `k-1`; or
2. add a short lemma defining `A prec B`, proving its rational separated
   realization, setting `T_{m,0}=T_{m,m}` to a singleton, and inducting on
   its size and maximum cap/cup values.

The first route is shorter.  Exact equality of the maximum sizes is not
needed for the upper bound; `a,b<=k-1` suffices.

### Lines 246--271: arbitrary `N` and order of limits

**Correct.**  The clean finite statement for fixed `k` should nevertheless
be displayed.  Let

\[
 A_k={k-2\over\log r_k}.
\]

Equations (5)--(6) give

\[
 \log W(Q_d)\le A_k(\log |Q_d|)^2+O_k(\log |Q_d|).             \tag{E}
\]

For arbitrary `N`, take `d=ceil(log_{r_k}N)` and any `N`-point subset
`P_N` of `Q_d`.  Convex position is intrinsic to a subset, so every convex
subset of `P_N` was already counted in `Q_d`; hence

\[
 \log f(N)\le\log W(P_N)\le\log W(Q_d)
 \le A_k(\log N)^2+O_k(\log N).                  \tag{F}
\]

This proves (9).  The quantifier order is legitimate: the same limsup is at
most `A_k` for every fixed `k`, and only then is `k` sent to infinity.  No
choice `k=k(N)` is being smuggled into an `O_k` term.

Stirling gives the slightly clearer

\[
 \log_2\binom{2k-4}{k-2}=2k-\tfrac12\log_2 k+O(1),
\]

which implies `A_k->1/2`.

### Lines 273--282: fixed-template optimality

**Correct indexing.**  The classical cups--caps theorem says that a set
with no `(a+1)`-cap and no `(b+1)`-cup has at most

\[
 \binom{a+b-2}{a-1}
\]

points.  Therefore `log r<=a+b-2`, and (7) is at least `1/2`.

This theorem needs a formal citation, and its hypotheses should state
`a,b>=2`, automatic when `r>=2`.  Phrase the conclusion as optimality among
iterations of a single fixed template under this directional composition;
it does not address nonstationary or heterogeneous blow-ups.

### Lines 284--299: verification artifact

**Verified.**  Running the script reproduces

```
(C,U,W)=(14136,14136,441399)
```

for the 36-point composition, and the separate exact 16-point census in
`agent_geometry/audit_blowup_classification.py` passes all `2^16` subsets.
For publication, put scripts and a README in a versioned supplement and give
a commit/archive identifier.  Computational verification supports but is
not used by the proof.

### Lines 301--323: open window

The endpoint identity is correct, subject to consistent conventions:
`V(P)=1+W(P)` if `W` counts nonempty subsets.  Define `c(s,t),u(s,t)` before
using them.  The lower coefficient `1/4` is not proved or cited in this
draft.  Either cite the modern `ES(k)=2^{k+o(k)}` theorem and include the
short witness double count, or omit the lower-window discussion from the
proof paper.  It is logically independent of the upper theorem.

## 2. Recommended theorem and lemma organization

A concise paper structure would be:

1. **Theorem 1 (main upper bound).**  State both the limsup result and its
   equivalent `for every delta>0` finite formulation.
2. **Definition 2 (vertical composition).**  Normalize coordinates and
   define `S[Q]`.
3. **Lemma 3 (mixed-triple realization).**  State all four signs and the
   rational-input conclusion.
4. **Lemma 4 (spanning-set classification).**  Give the iff description for
   caps, cups, and convex subsets meeting multiple blocks.
5. **Corollary 5 (substitution enumerators).**  Display (2).
6. **Proposition 6 (fixed-template exponent).**  Prove the exact limit (7)
   from the explicit unrolling (C).
7. **Lemma 7 (balanced cups--caps template).**  Cite or construct `S_k`.
8. **Proof of Theorem 1.**  Apply Proposition 6, use (F), then let `k` tend
   to infinity.
9. **Corollary 8 (fixed-template optimality).**  Apply the cups--caps theorem.
10. Put prior-art comparison, verification artifacts, and the lower-bound
    discussion in separate introduction/appendix sections.

This order makes every quantifier local: realization before counting,
classification before formulas, a finite recurrence before its asymptotic
limit, and fixed `k` before arbitrary `N` and then `k->infinity`.

## 3. Minimal proposed correction set

Before external circulation, the minimum safe edits are:

* add rational hypotheses to the rational-realization sentence;
* mention a generic orientation-preserving coordinate change before the
  shear;
* name the spanning convex-set iff classification;
* replace lines 193--219 by the explicit recurrence (C) and lower bound (D);
* define/cite the Pascal construction instead of invoking undefined `prec`;
* display the finite arbitrary-`N` inequality (F);
* give exact citations for the cups--caps theorem and any claimed lower
  coefficient;
* remove internal repository/prior-art-search language from the paper body.

With these repairs, I would regard the proof itself as ready for external
mathematical review.
