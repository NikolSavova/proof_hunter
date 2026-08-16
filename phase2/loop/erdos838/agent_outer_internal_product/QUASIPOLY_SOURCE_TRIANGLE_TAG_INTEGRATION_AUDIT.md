# Source--triangle tags are a complete terminal gate, not an upstream ramp closure

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

The weighted source--triangle tag theorem in
`agent_common_shield_mixing/QUASIPOLY_SOURCE_TRIANGLE_TAG_CLOSURE.md` is
correct.  Its local inequality, tagged-mass count, Cauchy step, and
`n^(3/2)` decoder loss all check exactly.  Under its stated terminal
hypotheses it eliminates every family of demand

\[
                  M\ge n^{\sigma\log\log n}V(P)        \tag{1}
\]

whose compressed actual source load is polynomial.

It is **not** an end-to-end closure of the stationary common-triangle or
finite-gap strong-comb branch.  Three distinctions are load-bearing.

1. The estimate `kappa_A<2L` survives multiple contexts for one actual
   source only after all records with the same source, actual description,
   and dyadic layer have been regrouped into one simple source-row star, or
   after every noncoalescible copy has been charged to `L`.  Individual
   context simplicity does not prove global simplicity, and the current
   minimizer chain has not proved that this actual description/duplicate
   load is polynomial.
2. A finite-gap strong-comb profile ramp is not automatically one of the
   theorem's `a by b` record families.  Its endpoint quantities `C_i,U_i`
   count local faces, not active label vertices, and the recurrence does
   not supply a terminal demand satisfying (1).  The complete-product and
   dense-context promotions remain upstream open steps.
3. A polynomial loss really is negligible **if** (1) is already known:
   `kappa_A<=n^C` turns the theorem into
   `M<=O(n^(C+3/2))V`.  But in the exact half-scale ramp with
   `D=2^d`, `q=d/4`, the source-word bank is only
   `D^q=2^(d^2/4)`, whereas one inherited child already has
   `2^(d^2/2+o(d^2))` faces.  No `n^(sigma loglog n)V` demand is present.
   The decoder theorem cannot manufacture the missing demand.

Thus the correct status is:

> **Full proof:** the abstract tagged terminal theorem, and its application
> to any already coalesced dense family with polynomial source-description
> load and quasipolynomial excess demand.
>
> **Local gate only:** its claimed implication for the unrestricted live
> minimizer/global chain, including the finite-gap strong-comb ramp.

This agrees with the scope warning in
`agent_common_shield_mixing/END_TO_END_QUASIPOLY_GATE_AUDIT.md`.  It closes
the last profile issue *after* the two missing promotions in that report;
it does not close those promotions.

## 1. The tagged Cauchy theorem is exact

For context `c`, let `a_c>=1` be the number of actual source targets,
`b_c` the other active side, `e_c<=a_cb_c`, and
`t_c=max(a_c,b_c)`.  For `t_c>=6`, put

\[
                         i_c={t_c\choose3}.             \tag{2}
\]

Since `a_ct_c^3>=a_c^2b_c^2>=e_c^2` and
`{t choose3}>=5t^3/54` for `t>=6`, one has

\[
                         e_c^2\le{54\over5}a_ci_c.      \tag{3}
\]

Let every context carry weight `w_c` and define

\[
 \kappa_A=\max_A\sum_{c:A\in\mathcal A_c}w_c.          \tag{4}
\]

Choose one canonical `A_c` in `mathcal A_c` and tag each selected triangle
incidence by `(A_c,T)`.  A fixed tag has load at most `kappa_A`, so

\[
 \sum_cw_ci_c\le\kappa_AV(P){n\choose3},\qquad
 \sum_cw_ca_c\le\kappa_AV(P).                          \tag{5}
\]

Cauchy applied to (3), with `e_c<=5a_c` in the thin branch, yields

\[
 \sum_cw_ce_c\le
 \kappa_A\left(5+\sqrt{{54\over5}{n\choose3}}\right)V(P).       \tag{6}
\]

No union `A_c union T` is asserted ordinary.  The triangle is a decoder
tag from a universe of size at most `{n choose3}`.  That is legitimate:
(5) is a finite incidence count, not an ordinary-face bank.  The release
edge is unnecessary in the proof of (6).

Deleting contexts, or fixing one circuit signature, direction, child, or
triangle, preserves (4)--(6).  Hence there is no flaw in the terminal
Cauchy theorem itself.

## 2. Exact condition for the dyadic source cap

Let an actual canonical source occurrence have upstream weight `alpha`,
and let every descendant record weight satisfy `beta<=alpha`.  In layer
`k`, round

\[
               2^{-k-1}\alpha<\beta\le2^{-k}\alpha     \tag{7}
\]

up to `2^{-k}alpha`.  If, for each triple

\[
          (\hbox{actual source},\hbox{actual description},k),   \tag{8}
\]

all distinct release labels are regrouped into one simple row star, the
source is entered only once in that layer.  Its total source load for one
description is then

\[
                         \sum_{k\ge0}2^{-k}\alpha<2\alpha.       \tag{9}
\]

If every actual source has total canonical occurrence weight at most one
and at most `L` descriptions, summation proves `kappa_A<2L`.

This argument is robust to originally overlapping product rectangles:
assign every record edge to its actual source row and regroup the distinct
column labels.  The local theorem still applies to the resulting one-row
stars (`a=1`).  It is not robust to uncharged duplicate records with the
same actual source and the same actual column.  `J` unit copies of one
geometric edge have demand `J`; a simple row star contains that edge only
once.  Preserving demand either gives it weight `J`, violating the
one-layer source cap, or assigns `J` noncoalescible descriptions.  Thus one
needs one of the following proved facts:

* canonicalization removes all such duplicates;
* their total descendant weight is already bounded by the source weight;
  or
* their actual multiplicity is included in `L`.

The abstract statement of the tag theorem assumes `kappa_A`; it does not
prove any of these three facts.  The currently banked global chain also
does not prove `L=n^O(1)` after base, root, tangent, cover, mask, and
chronology data are consolidated.  Calling different states
"descriptions" is a correct conditional accounting convention, not yet a
bound on their number.

## 3. Why the strong-comb ramp is upstream of the theorem

The exact guarded strong-comb recurrence from
`FINITE_GAP_STRONG_COMB_RAMP_BARRIER.md` is

\[
 W(P)=\sum_iW_i+
 \sum_{i<j}C_iU_j\prod_{i<k<j}(1+n_k)+\text{endpoint terms}.     \tag{10}
\]

Its scalar obstruction uses `q` children with

\[
 W_i=R^h,qquad C_i=R^{x_i},\qquad U_i=R^{h-x_i},       \tag{11}
\]

and a unit-slope profile ramp.  The quantities `C_i,U_i` are numbers of
possibly high-rank local faces.  They are not the side cardinalities
`a_c,b_c` of a simple label graph.  Equation (10) alone provides neither:

* a partition into actual source-by-label records;
* a triangle support of size `max(a_c,b_c)` attached to each record
  context;
* polynomial actual description load; nor
* total record demand `n^(sigma loglog n)V(P)`.

Indeed take `D=2^d`, `q=d/4` and `h=d/2`.  The source transversals number

\[
                         M_{src}=D^q=2^{d^2/4},         \tag{12}
\]

while the inherited local child bank in (11) is already

\[
                         H=R^h=2^{d^2/2+o(d^2)}.        \tag{13}
\]

Even adjoining two rank-at-most-two cloud alphabets of size at most `D`
only changes (12) by `2^{O(d)}`.  Therefore

\[
                         M_{src}D^{O(1)}=o(H),          \tag{14}
\]

much less than the terminal hypothesis `M>=n^(sigma loglog n)H`.
The missing factor is the difference between evaluating the inherited
bank at scale `D` and at scale `qD`; it is not an already-counted family of
record incidences.

Thus not every finite-gap ramp branch is represented by Theorem 1.  A
separate product/context extraction would have to turn the ramp failure
into the demand in (1).  This is exactly the first open promotion in the
end-to-end audit.

## 4. The polynomial loss closes precisely the terminal scale

If the terminal demand (1) and `kappa_A<=n^C` hold for a fixed `C`, (6)
gives

\[
 M\le O(n^{C+3/2})V(P).                                \tag{15}
\]

For fixed `sigma>0`,

\[
 {n^{\sigma\log\log n}\over n^{C+3/2}}
      =n^{\sigma\log\log n-C-3/2}\longrightarrow\infty.         \tag{16}
\]

So the `n^(3/2)` loss really is free at that scale.  It remains free for
the more specific deficit in (4) of the finite-gap report, which is
`N^{(1-o(1))log q}`, **provided that deficit has first been realized as
record demand relative to `V(P)`**.  No such realization follows from the
strong-comb recurrence.

The tag theorem therefore removes the final fixed-triangle/profile
obstruction in a supplied dense terminal context.  It does not eliminate
the quadratic-mass complete-product extraction, dense-context promotion,
or polynomial-description-load gates.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_quasipoly_source_triangle_tag_integration.py
```

Expected output:

```text
PASS: tagged Cauchy, dyadic coalescing condition, ramp scale, and polynomial threshold
```
