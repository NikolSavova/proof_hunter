# Dynamic two-record Kraft routing

**Date:** 2026-08-14  
**Verdict:** the dynamic gate has an exact pairwise formulation.  Work with
ordered **pairs of repair records**.  At the first scale where their two
boundary states are opposite-side tangent-compatible, switch the two lower
arcs and output an ordered pair of cross-union faces.  If the records remain
in one same-side nested state, terminate against the Boolean face complex of
the discarded prefix.  A first-divergence recursion is automatically a
Kraft partition, so neither its depth nor the ramp--plateau alphabet sizes
cost entropy.

The resulting theorem is conditional only in one sharply isolated place:
the total reuse of terminal face pairs across different outer states.  If
that reuse, the within-state record multiplicity, and the width of the
discarded-prefix families are `2^{o(r)}`, then

\[
                         E^2\le 2^{o(r)}V(P)^2,              \tag{1}
\]

where `E` is the selected exterior-record count.  Consequently the desired
capped rankwise estimate follows.  This report proves the switch decoder,
the nested pair release, the Kraft algebra, and the implication (1).  It
does **not** prove the required global reuse bound for arbitrary planar
repair histories, so Erdős 838 remains open.

The three prescribed equality tests behave correctly:

* an arbitrarily deep parabolic chain costs at most `9/4` locally;
* the fixed-outer long-ear product has an exact first-divergence Kraft sum,
  and its convex-blocker specialization already satisfies `E=poly(r)V`;
* the ramp--plateau word has overwhelmingly many abstract forward pairs,
  despite defeating every one-target atomic interval count.  Thus its
  obstruction is target recovery across states, not pair-recursion mass.

All faces below are convex-position subsets.  Since the face family is
hereditary, every subset of a face is again a face.  `V=V(P)` includes the
empty face.

## 1. The exact opposite-side two-record switch

Fix a directed chord `uv`.  For `j=1,2`, let

\[
              g_j=(C_j^+,C_j^-),                          \tag{2}
\]

where `C_j^+` and `C_j^-` are positive and negative rooted convex arcs for
`uv`, as in `../lattice_rectangle_theorem/REPORT.md`.  Suppose the two
**crossed** pairs

\[
                  (C_1^+,C_2^-),\qquad(C_2^+,C_1^-)       \tag{3}
\]

satisfy both rank-three endpoint tangent signs.  Put

\[
 F_{12}=C_1^+\cup C_2^-,
 \qquad
 F_{21}=C_2^+\cup C_1^-.                                  \tag{4}
\]

> **Theorem 1 (two-record switch decoder).**  Both sets in (4) are convex
> faces.  For fixed `uv`, the ordered target pair `(F_12,F_21)` recovers the
> ordered record pair `(g_1,g_2)`.  If `uv` is forgotten and every target
> has rank at most `r`, the fibre is at most
> \[
>                              r(r-1).                       \tag{5}
> \]
> With a state tag from `Sigma`, it is at most
> `|Sigma|r(r-1)`.

**Proof.**  The planar rectangle theorem applied twice proves convexity.
For fixed `uv`, intersecting `F_12` and `F_21` with the two open half-planes
recovers respectively

\[
 (C_1^+,C_2^-),\qquad(C_2^+,C_1^-),                       \tag{6}
\]

and hence both records.  Without the chord, `u,v` must be an ordered pair
of distinct vertices common to the recovered extreme sets.  There are at
most `r(r-1)` guesses, after which (6) is deterministic.  The tag contributes
the final factor.  QED.

Using **two** crossed targets is important.  A single interval target can
forget an exponential outside signature in a vertical product.  The
ordered pair in (4) retains both positive arcs and both negative arcs, so
no outside word is discarded after the chord is known.  Theorem 1 is the
geometric spend at a terminal opposite-side node.

## 2. Same-side nested pairs are paid by one prefix complex

Let `D` be a convex face of size `m`, and let `mathcal D subseteq 2^D` be a
family of possible discarded prefixes.  Write `w` for its inclusion width.

> **Lemma 2 (nested pair release).**
> \[
> \boxed{
>        |\mathcal D|^2
>        \le w^2(m+1)^2
>        \le {9\over4}w^2 2^m.}                           \tag{7}
> \]
> Consequently, for a fixed outer context face `X`, all ordered pairs of
> discarded states can be routed to target pairs
> \[
>                         (X,J),\qquad J\subseteq D,        \tag{8}
> \]
> with congestion at most `ceil(9w^2/4)`.

**Proof.**  Dilworth partitions `mathcal D` into `w` inclusion chains.
Every strict chain in `2^D` has at most `m+1` members, proving the first
bound.  The elementary inequality

\[
                       (m+1)^2\le {9\over4}2^m              \tag{9}
\]

holds for every integer `m>=0`, with equality at `m=2`.  There are `2^m`
choices of `J`, and every `J` is a face.  Distribute the at most
`(9/4)w^2 2^m` ordered pairs among them.  QED.

For the parabolic nested-prefix family

\[
             \varnothing\subset D_1\subset\cdots\subset D_s,
 \qquad |D_j|=j,                                           \tag{10}
\]

one has `w=1`.  Arbitrary exposure depth therefore costs a constant in the
**pair** problem, just as the one-record Boolean demand costs less than one
doubling bit.  The only possible large loss is reuse of the same pair
`(X,J)` under many different outer contexts.

There is a useful multiplicity version.  If at most `eta` active records
share one discarded state in one context, (7) acquires the factor `eta^2`.
If every target pair `(X,J)` is used by at most `rho` release contexts, then
all nested terminal states together cost at most

\[
                   {9\over4}\eta^2w^2\rho V^2.             \tag{11}
\]

Indeed the occurrences of the Boolean pools in (8) sum to at most
`rho V^2`.

## 3. The dynamic pair-certificate theorem

Let `Omega` be a selected family of `E>=2` repair records.  Run any recursive
comparison of ordered distinct pairs in `Omega^2`.  A pair may descend
through equality or same-cell children several times, but it is counted
only at its **first terminal node**.  There are two allowed terminal types.

* A **switch terminal** satisfies Theorem 1 and maps to an ordered face pair.
  Across all switch terminals, suppose the global inverse multiplicity is
  at most `kappa`.
* A **nested terminal** has the data of Lemma 2.  Suppose the uniform bounds
  on record multiplicity, inclusion width, and cross-context target reuse
  are `eta,w,rho`.

Allow an uncovered fraction `theta<1` of the ordered off-diagonal pairs.

> **Theorem 3 (dynamic pair Kraft bound).**  Under the preceding
> hypotheses,
> \[
> \boxed{
> E^2\le {2\over1-\theta}
>       \left(\kappa+{9\over4}\eta^2w^2\rho\right)V^2.}     \tag{12}
> \]

**Proof.**  First-terminal nodes partition the covered ordered pairs, so
there is no depth factor.  The switch decoder bounds all switch pairs by
`kappa V^2`.  Equation (11) bounds all nested pairs.  Therefore

\[
 (1-\theta)E(E-1)
 \le\left(\kappa+{9\over4}\eta^2w^2\rho\right)V^2.          \tag{13}
\]

Since `E>=2` gives `E(E-1)>=E^2/2`, rearrangement proves (12).  QED.

Thus (1) follows whenever

\[
 {1\over1-\theta},\quad\kappa,\quad\eta,\quad w,\quad\rho
                         =2^{o(r)}.                         \tag{14}
\]

The theorem deliberately puts the unresolved geometry into `rho` and
`kappa`, rather than hiding it in an interval decoder.  Fixed-chord switch
states contribute only `r(r-1)` to `kappa`; dyadic tangent localization and
`2^{o(r)}` prefix tags remain harmless.  What is not proved is that arbitrary
same-side histories can be organized so that their face-pair reuse `rho`
is subexponential.

### Corrected capped-RNP implication

Suppose a rank-`r` hard family `S` has at least

\[
                         d=2^{\ell-r-o(r)}                  \tag{15}

selected exterior records per source.  Then `E>=d|S|`.  If it admits a
dynamic certificate satisfying (14), (12) gives

\[
 \boxed{
 |S|\le 2^{r-\ell+o(r)}V.}                                 \tag{16}
\]

This is the capped rankwise inequality required by the cumulative-envelope
and low-addable reductions.  Hence Theorem 3 is a corrected sufficient
condition for capped RNP.  It is stronger and more precise than asking one
record to remember every outside interval signature.

## 4. Why recursion depth has zero Kraft cost

The exact algebra is clearest for a full word cell

\[
                 \mathcal W=Q_1\times\cdots\times Q_q,
 \qquad |Q_i|=m_i,qquad N=\prod_i m_i.                    \tag{17}

For two independent uniform words, the probability that their first
difference occurs at coordinate `j` is

\[
 p_j=\left(\prod_{i<j}{1\over m_i}\right)
                     \left(1-{1\over m_j}\right),          \tag{18}
\]

and the probability they agree everywhere is `1/N`.  Telescoping gives the
exact Kraft identity

\[
                         \sum_{j=1}^q p_j+{1\over N}=1.      \tag{19}
\]

Thus descending through a fixed outer tangent cell and exposing arbitrarily
many internal coordinates does not multiply losses.  A pair is charged
once, at its first divergence or at the diagonal leaf.

There is also an exact forward/nonforward split.  Put the same total order
on each alphabet, lexicographically order the words, and call a distinct
pair forward when a later coordinate reverses the first strict comparison.
The ordered nonforward count, including the diagonal, is

\[
 N_{\rm nf}=2\prod_{i=1}^q{m_i(m_i+1)\over2}-N.             \tag{20}

Indeed a lexicographically increasing pair is nonforward exactly when it is
coordinatewise increasing.  Since `m_i>=2`,

\[
 {N_{\rm nf}\over N^2}
 \le2\prod_i{m_i+1\over2m_i}
 \le2(3/4)^q.                                               \tag{21}

Large-dimensional full products therefore have abundant abstract forward
pair mass.  Equation (21) does not prove that all these pairs share the
planar chord/signature required by Theorem 1; that is precisely the
geometric localization issue represented by `kappa`.

## 5. Equality-test audits

### 5.1 ACP Proposition 26: fixed outer cell, long ears

In Proposition 26, put `q=a+b`.  The repair records form the full word cell

\[
                  \mathcal G=[M]^{q+1},qquad E=M^{q+1},     \tag{22}

where the last coordinate is the apex blocker.  All outer tangent data are
fixed.  Equations (18)--(19) show that recursive entry into the `q+1`
internal coordinates is exactly Kraft-normalized; there is no
`Theta(q log M)` decoder loss.  Equations (20)--(21) show that, once many
coordinates remain, most record pairs contain a forward inversion.  Pairs
with only one active coordinate must recurse into that microblock's order
type, as Proposition 26 requires.

There is a completely unconditional check on the specialization in which
the `M` apex blockers are chosen in convex position.  The source faces give
`M^q` distinct faces and the blocker cloud gives `2^M` faces, so

\[
                 V\ge\max\{M^q,2^M\}.                       \tag{23}
\]

Put `s=q+1` and

\[
                 B_s=\left\lceil2s\log_2(2s)\right\rceil.   \tag{24}
\]

If `M<=B_s`, (23) gives `E/V<=M<=B_s`.  If `M>B_s`, monotonicity of
`x/log_2x` and the definition of `B_s` give `2^M>=M^s=E`.
Therefore

\[
                         \boxed{E\le B_sV}.                  \tag{25}
\]

Since `B_s=O(r log r)=2^{o(r)}`, this full fixed-outer-cell family already
satisfies (1).  For a difficult blocker order type, (25) is replaced by the
recursive pair certificate inside that order type; the outer full product
itself creates no Kraft loss.

### 5.2 The parabolic nested chain

For prefixes of sizes `0,1,...,s`, there are `(s+1)^2` ordered record pairs
and `2^s` Boolean prefix faces.  The exact worst ratio is

\[
                    \max_{s\ge0}{(s+1)^2\over2^s}={9\over4}, \tag{26}

attained at `s=2`.  Thus arbitrarily long same-side nesting passes Lemma 2
with an absolute constant and does not consume a bit per descent.

### 5.3 The ramp--plateau word

For the exponent word

\[
 (1,2,4,\ldots,L/2,
   \underbrace{L,\ldots,L}_{L/2\text{ times}},
   L/2,\ldots,4,2,1),                                    \tag{27}

put `m_i=2^{a_i}`.  The atomic all-interval report proves that all one-target
partial-word and two-endpoint pools have only polynomial excess over the
source count, below capped demand.  Nevertheless (19) holds exactly for
these wildly nonuniform alphabets, and (21) gives

\[
             {N_{\rm forward}\over N^2}
                       \ge1-2(3/4)^{L/2+2\log_2L}.           \tag{28}

So the ramp--plateau is not a counterexample to pair mass or to Kraft
descent.  It remains a sharp test for `kappa`: a valid geometric switch must
retain both complete outside arcs, as (4) does, and the same target pair
must not be repaid under exponentially many outer signatures.

## 6. Exact residual

The dynamic attack reduces the gate to the following concrete planar
statement.

> **Dynamic face-pair reuse conjecture.**  Apply the outward-successor entry
> theorem and Theorem 23, and recursively expose the internal tangent
> coordinates of every entropy-balanced fixed cell.  Stop an ordered record
> pair at its first opposite-side compatible state, or at the first
> same-side state whose discarded prefixes lie in a common Boolean carrier.
> The resulting switch and release terminals cover a constant fraction of
> all off-diagonal pairs and have
> \[
>       \kappa,\eta,w,\rho=2^{o(r)}.                        \tag{29}
> \]

Theorems 1--3 prove that (29) implies capped RNP.  Proposition 26, the
parabolic chain, and the ramp--plateau all pass the **algebraic** pair-Kraft
part.  What remains is geometric: prove subexponential global reuse of the
ordered face pairs after tangent markers and outer signatures change.

## 7. Verification

Run

```bash
python3 \
  phase2/loop/erdos838/agent_cyclic_stem_hw/dynamic_pair_kraft/verify_dynamic_pair_kraft.py
```

The checker uses exact integers and rational comparisons.  It verifies:

* the sharp nested-pair inequality (9) through rank 512;
* the first-divergence Kraft identity for 180 heterogeneous product cells,
  with independent brute-force word enumeration in the small cases;
* the exact forward/nonforward formula (20);
* the fixed-outer bound (25) for `2<=q<=80` and all `2<=M<=4096`, including
  both branches around `B_s`; and
* the complete ramp--plateau profiles for `3<=h<=7`, using the enormous
  integer alphabet sizes directly rather than floating approximations.

The finite audits test the algebra.  The switch and dynamic-certificate
theorems are symbolic and are proved above.
