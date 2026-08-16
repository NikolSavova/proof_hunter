# Minimizer mutations favor, rather than forbid, the common-guard ramp

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

For the exact common-guard recurrence, global `V`-minimality gives clean
reflection, replacement, and adjacent-swap inequalities.  They do not force
balanced child profiles.  Their sign is the opposite: a minimizer sorts
cup-heavy children to the left and cap-heavy children to the right.  The
quarter cap/cup ramp satisfies every reflection and adjacent-permutation
inequality strictly.

There is also a fully realizable finite certificate.  With three
four-point children behind the common guard, the profile word

\[
 (W,C,U)=\boxed{(15,10,15)},\quad
              (14,11,13),\quad
              \boxed{(15,15,10)}                         \tag{1}
\]

has exactly `V=1561` faces.  Exhaustion of **every** rooted profile of every
four-point planar general-position order type and all `5^3=125` profile
words proves that 1561 is the global minimum inside this mutation class.
Thus every single-child replacement, reflection, and permutation mutation
is nonimproving.  The exact rational realization has all guard-retaining
transversals convex and every same-child pair blocked by the guards.

This does not produce an asymptotic sub-half order type: the finite children
are convex/codimension-one toys, and a planar realization of the quadratic
quarter ramp remains the missing heterogeneous-child problem.  It does
prove that minimizer first-order conditions alone cannot kill that ramp.
Any positive theorem needs a nonlocal profile-reset or a comparison outside
the common-guard wrapper class.

## 1. Exact Euler inequalities for a minimizer

Use the common-guard block order

\[
                       u,Q_0,Q_1,\ldots,Q_{q-1},v.        \tag{2}
\]

Let block `i` have size `n_i` and nonempty profile `(W_i,C_i,U_i)`.
The guards have size and all three counts equal to one.  The exact face
recurrence is

\[
 V=\sum_iW_i+
   \sum_{h<j}C_hU_j\prod_{h<k<j}(1+n_k).                 \tag{3}
\]

For a child position `i`, define its prefix and suffix weights

\[
\begin{aligned}
 L_i&=\sum_{h<i}C_h\prod_{h<k<i}(1+n_k),\\
 R_i&=\sum_{j>i}U_j\prod_{i<k<j}(1+n_k),                 \tag{4}
\end{aligned}
\]

including the two guard blocks in the sums.  Holding every other child
fixed, (3) is

\[
                V=\text{constant}+W_i+R_iC_i+L_iU_i.     \tag{5}
\]

Consequently a global minimizer among permissible same-size replacements
must satisfy, for every replacement profile `(W',C',U')`,

\[
 \boxed{W_i+R_iC_i+L_iU_i
       \le W'+R_iC'+L_iU'.}                              \tag{6}
\]

Reflection is always a permissible projective mutation and swaps `C,U`.
Equation (6) gives the necessary reflection inequality

\[
 \boxed{(R_i-L_i)(C_i-U_i)\le0.}                         \tag{7}
\]

Thus a suffix-heavy position (`R_i>L_i`) prefers `C_i<U_i`, i.e. a
cup-heavy child.  A prefix-heavy position prefers a cap-heavy child.  This
is exactly the ramp orientation.

Suppose adjacent children `i,i+1` have the same size `n`.  Let `L` be the
prefix weight just before `i` and `R` the suffix weight just after `i+1`.
Subtracting the value after swapping the two children from the current
value gives

\[
\boxed{
 \Delta_{i,i+1}=
 nL(U_{i+1}-U_i)+nR(C_i-C_{i+1})
 +C_iU_{i+1}-C_{i+1}U_i.}                               \tag{8}
\]

A minimizing order requires `Delta<=0`.  If `C_i<=C_(i+1)` and
`U_i>=U_(i+1)`, every term in (8) is nonpositive.  Adjacent-swap
minimality therefore **sorts** the anti-aligned ramp; it does not reset it.

## 2. The quadratic scalar ramp passes the tests

Put `n_i=D`, and use the exact integral profiles

\[
 C_i=D^{i+2},\qquad U_i=D^{q+1-i},\qquad W_i=C_i+U_i.    \tag{9}
\]

Then `C_i` strictly increases and `U_i` strictly decreases.  Formula (8)
is strictly negative at every adjacent pair.  The exact prefix and suffix
weights in (4) satisfy

\[
                 R_i>L_i\Longleftrightarrow C_i<U_i,     \tag{10}
\]

apart from a possible equality at the central index.  Hence (7) also holds
at every position.

With `D=2^d` and `q=floor(d/4)`, the recurrence has coefficient
`1/4+o(1)` as proved and verified in
`COMMON_GUARD_PROFILE_RAMP_BARRIER.md`.  Thus all local reflection and
permutation Euler inequalities are compatible with the formal quarter
fixed point.

Replacement inequalities (6) ask for the actual lower Pareto envelope of
planar child profiles under the varying weight ratio `R_i/L_i`.  Global
minimality may select a different exposed Pareto point at each position.
Without a theorem restricting that envelope, (6) is a mechanism for
creating the ramp, not a balance theorem.

## 3. Complete four-point mutation certificate

For four points in general position there are only two unlabelled order
types.  Exhausting all coordinate orders gives the complete rooted profile
menu

\[
\begin{array}{c|c|c}
\text{local type}&W&(C,U)\\ \hline
\text{convex}&15&(10,15),(12,12),(15,10),\\
\text{one interior point}&14&(11,13),(13,11).
\end{array}                                             \tag{11}
\]

The baseline ten singleton/pair traces are both caps and cups.  The four
triples contribute according to their signs; the full four-set contributes
to one side exactly in the all-cap/all-cup convex cases.  Direct
chirotope/permutation exhaustion proves that (11) is complete.

Take three size-four children.  Evaluating (3) on all 125 words from (11)
gives

\[
                 \min V=1561.                            \tag{12}
\]

The two minimizers have the convex cup profile `(15,10,15)` on the left,
the convex cap profile `(15,15,10)` on the right, and either interior-point
orientation in the middle.  Choose (1).

The exact one-coordinate replacement values are

\[
\begin{array}{c|ccccc}
\text{position}&\multicolumn{5}{c}{\text{sorted attainable values}}\\ \hline
0&1561&1646&1734&1820&1996\\
1&1561&1561&1562&1577&1577\\
2&1561&1644&1730&1814&1986.
\end{array}                                             \tag{13}
\]

The two adjacent swaps give `1664` and `1842`.  Thus every inequality
(6)--(8) holds, including all same-size planar replacements rather than
only reflection.

## 4. Exact planar realization

Normalize the guards to `u=(-1,0),v=(1,0)` and use pocket coordinates

\[
                 (L,R)\longmapsto
       \left({L-R\over L+R},-{2\over L+R}\right).        \tag{14}
\]

Choose macro parameters `t=4,1,1/4`, so their centers have
`(L_0,R_0)=(1/t,t)` on a convex antichain.  With
`epsilon=1/1000`, map seed coordinates `(f,g)` by

\[
 L=L_0+\varepsilon f+\varepsilon^2g,qquad
 R=R_0+\varepsilon f-\varepsilon^2g.                    \tag{15}
\]

Use the seeds

\[
 (f,-f^2)_{f=0}^3,\qquad
 (0,0),(1,4),(2,1),(4,0),\qquad
 (f,f^2)_{f=0}^3.                                       \tag{16}
\]

They realize respectively the three profiles in (1).  Formula (15)
preserves each child order type, gives the common-guard nesting order, and
has the vertical strong-glue mixed signs.  Exact rational brute force over
all `2^14` subsets gives 1561 nonempty ordinary faces, equal to (3).

## 5. Consequence

The minimizer-specific route has a sharp stopping point:

* reflections yield the anti-alignment sign (7);
* adjacent permutations sort profiles monotonically by (8);
* local replacements select the lower weighted Pareto envelope by (6); and
* a finite planar minimizer already realizes this cup-to-cap progression.

Therefore a proof of coefficient one half cannot come from these mutation
inequalities alone.  It must show that a long quadratic ramp cannot be a
planar Pareto envelope without some child paying locally, or use a mutation
which changes the macro/guard structure and creates a new ambient bank.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_minimizer_common_guard_mutations.py
```

The checker uses exact integers/rationals.  It derives the complete menu
(11) by chirotope permutation, exhausts all 125 wrapper words and all
mutations, checks (7)--(10) on scalar ramps through `q=40`, constructs
(14)--(16), verifies all guard circuits and transversals, and exhausts its
`2^14` subsets to recover `V=1561`.
