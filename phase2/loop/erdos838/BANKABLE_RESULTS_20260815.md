# Erdős 838: short bankable-results note

This note extracts a small number of reusable statements from the full
campaign.  It is not a claim that the unrestricted problem is solved.  The
recent statements are candidates for a standalone barrier/construction note
only after the independent audits in `VERIFICATION_QUEUE_20260815.md`.

All logarithms are base two.  Write `V(P)` for the number of convex subsets,
including the empty set; changing the empty-set convention changes none of
the asymptotics.

## 1. Exact extraction threshold from the strong-tree theorem

**Proposition 1.**  Suppose that every `n`-point set `P` satisfying

\[
     \log V(P)\le (1/2-\delta)(\log n)^2
\]

contains a mirror-decomposable subset `Q` of size
`n^{\alpha+o(1)}`.  If

\[
                         \alpha>\sqrt{1-2\delta},
\]

then no such `P` exists for all sufficiently large `n`.

**Proof.**  The audited strong-tree theorem gives

\[
 \log V(Q)\ge \frac12(\log |Q|)^2-O((\log |Q|)^{3/2})
              =\left(\frac{\alpha^2}{2}-o(1)\right)(\log n)^2.
\]

Every convex subset of `Q` is a convex subset of `P`, so `V(P)>=V(Q)`.
The strict inequality `alpha^2/2>1/2-delta` contradicts the assumed upper
bound.  \(\square\)

This is an exact regularization threshold, not an extraction theorem.  Known
general extraction results do not reach it.

Source: `agent_all_interval_isoperimetry/LOW_V_FIXED_GAP.md` and the audited
strong-tree theorem in `paper/main.tex`.

## 2. A universal hinged endpoint Kraft inequality

Let the points be ordered by increasing `x` coordinate.  For a point `i`, let
`beta_i` be the largest cup length ending at `i` minus one and `alpha_i` the
largest cap length starting at `i` minus one.  Define:

- `U_i(r)`: the minimum possible last slope of an `r`-edge cup ending at `i`;
- `D_i(s)`: the minimum possible first slope of an `s`-edge cap starting at
  `i`.

Merge the two increasing lists, writing `0` for a `U` entry and `1` for a `D`
entry.  Call the resulting binary word `w_i`; its length is
`alpha_i+beta_i`.

**Theorem 2 (hinged Kraft).**  The words `w_i` are prefix-free.  Consequently

\[
       \sum_i2^{-(\alpha_i+\beta_i)}\le1,
       \qquad
       \max_i(\alpha_i+\beta_i)\ge\lceil\log n\rceil.
\]

**Proof skeleton.**  For `i<j`, put `t=slope(ij)`.  Let `x` be the first index
with `U_i(x)>t` and `y` the first with `D_j(y)>t`, with the standard sentinel
at the end of each list.  Appending `ij` to a cup gives `U_j(x)<=t`; prepending
`ij` to a cap gives `D_i(y)<=t`.  Therefore the first `x+y-1` entries of
`w_i` contain at most `x-1` zeros, whereas the same prefix of `w_j` contains
at least `x` zeros.  The two words differ before either ends.  Kraft's
inequality and the maximum-length bound follow.  \(\square\)

The theorem is geometric but uses only the ordered edge slopes.  Its exact
variable-arity grammar consequence closes a large class of homogeneous
finite-menu recursive constructions at coefficient `1/2`; that consequence
is V1 in the independent audit queue.

Source: `agent_nonstrong_ramp_search/HINGED_DIAGONAL_FLOOR_LOG.md`.

## 3. Macroscopic regeneration penalty

**Proposition 3 (conditional support calculus).**  Consider a heterogeneous
vertical composition satisfying the hypotheses recorded in
`agent_upper_jump/REPORT.md`: a macro-large induced core, child coefficient
`c`, logarithmic macro/child proportions `alpha,beta`, balanced directional
endpoints, and no macro-count or mean loss.  Then

\[
                   c_{out}\ge c+(1-2c)\alpha\beta.
\]

In particular, if `c<1/2` and `alpha beta>0`, comparable macroscopic
regeneration strictly raises the coefficient.  A sub-half construction in
this framework must therefore lose one of the stated hypotheses: it needs
directional skew, low local convex mass, support avoiding same-skew induced
cores, or a genuine macro-mean deficit.

This proposition is useful as a construction barrier, not as an unrestricted
lower bound.  Its hypotheses must remain attached to every citation.

## 4. Exact weighted Hall and global assembly

Let histories `H` have weights `w(H)` and let `Gamma(H)` be their compatible
ordinary outputs.  Suppose each history requires demand multiplier `D`.

**Theorem 4 (local allocation).**  A fractional decoder of output load at
most `lambda` exists if and only if, for every history subfamily `X`,

\[
             D\sum_{H\in X}w(H)\le\lambda|\Gamma(X)|.
\]

This is the weighted Hall/max-flow min-cut theorem.  Recovery fibre is an
independent requirement and cannot be inferred from the load inequality.

**Theorem 5 (assembly).**  If local codes are superposed over eligible traces
and a physical output belongs to at most `delta(F)` trace banks, then global
load is at most `lambda delta(F)` and global recovery-list size is at most
`rho delta(F)`, where `rho` is the local recovery fibre.  For genuine
two-sided consecutive traces inside a rank-`r` face,

\[
                         \delta(F)\le r-3,
\]

and this rank factor is sharp.

**Proof.**  Sum the local load (respectively recovery-list) bound over the
trace banks containing the output.  For the rank refinement, an eligible
two-sided trace needs one label on each side, leaving exactly the `r-3`
interior consecutive positions; alternating convex polygons attain them all.
\(\square\)

This theorem makes precise why a local load-one code is not automatically a
global decoder: bank incidence and recovery must both be charged.

Source: `agent_coxeter_global_half/ABSTRACT_MIXED_HALL_ASSEMBLY.md`.

## 5. Sharp scope and publication package

The preceding statements support a short paper section containing:

1. the already-audited `1/2` construction and strong-tree characterization;
2. Proposition 1 as the exact regularization threshold;
3. Theorem 2 and its independently checked grammar corollary;
4. Proposition 3 as a conditional construction barrier;
5. Theorems 4--5 as a reusable decoder framework;
6. a selected, small set of exact stretchable counterexamples showing why
   local history-preserving allocation is insufficient.

No item in this note improves the unrestricted lower coefficient beyond
`1/4`.  That gain is the separate target in
`PROVED_GAIN_STRATEGY_20260815.md`.
