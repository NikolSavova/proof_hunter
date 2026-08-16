# Global support-union Hall consolidation: exact codegree theorem and the synchronized-support regression

**Date:** 2026-08-15.  All logarithms are base two.  Half-weight is
unnormalized in this report:

\[
                         w(F)=2^{-|F|}.                 \tag{1}
\]

The common global factor `1/F(P)` can be restored everywhere and cancels
from every normalized load.

## Verdict

There is an exact global Hall/codegree theorem.  Remove the empty face from
every support bank.  For contexts `c` with demand `d_c`, hereditary
ordinary-face bank `B_c`, and nonempty half-capacity

\[
                  z_c=\sum_{F\in B_c}2^{-|F|},          \tag{2}
\]

the optimal fractional congestion is at most

\[
 \boxed{
 \max_x\sum_{c:\{x\}\in B_c}{d_c\over z_c}.}          \tag{3}
\]

Thus a support-union family has low global load unless one actual point is
contained in a high weighted codegree of banks.  No empty-face localization
is involved.  The theorem applies to full induced face banks, Boolean
support cubes, and coordinate partial-transversal cubes.

There is also an exact rank-`t` strengthening.  If every bank in a weighted
family has at least `b_t` ordinary rank-`t` faces, one nonempty ordinary
face `I` satisfies

\[
 \boxed{
 \sum_{c:I\in B_c}a_c
   \ge {b_t\over\binom nt}\sum_ca_c}                   \tag{4}
\]

for arbitrary nonnegative context weights `a_c`.  For Boolean `q`-cubes,
`b_t=binom(q,t)`.  For a partial cube on `r` global role classes of sizes
`y_(c,i)`,

\[
 b_t(c)=e_t(y_{c,1},\ldots,y_{c,r}),                   \tag{5}
\]

the elementary symmetric polynomial.  In particular `b_t(c)>=binom(r,t)`
when every active role is nonempty.

If `n=2^L`, `q=Theta(L)`, `t=tau L`, and the original weighted context
mass is `2^{(a+o(1))L^2}`, (4) retains

\[
                  2^{(a-\tau+o(1))L^2}                 \tag{6}
\]

mass on one common `t`-face.  This is linear mass preservation, not a
Cauchy square: no `M^2` record supply is silently converted to `M`.

The proposed completion recursion is exact for two classes of bank:

1. **Boolean support:** if `I subset Q_c`, then all
   `I union S`, `S subset Q_c-I`, are ordinary;
2. **one-per-role partial cube:** after deleting the roles occupied by
   `I`, every remaining partial transversal may be adjoined to `I`.

Their prefixed half-capacities are respectively

\[
 2^{-|I|}(3/2)^{|Q_c|-|I|},\qquad
 2^{-|I|}\prod_{i\notin\operatorname{roles}(I)}(1+y_{c,i}/2).
                                                               \tag{7}
\]

Inside one common-prefix fibre, distinct completion supports can therefore
be role-coloured and passed through the existing high-redundancy/retention
split.  The exact tax is the role-state loss times the maximum multiplicity
of one completion support.  In the low-redundancy branch the retained
ordered certificate must include compatibility with the fixed prefix `I`.

This does **not** finish global consolidation.  Two sharp obstructions
remain.

* For an arbitrary induced face bank, a common face need not coexist with
  faces of the deleted support.  A four-point `1+3` circuit already kills
  that recursion.
* Even for Boolean banks, all contexts may have the identical completion
  support.  Then every nonempty face is common to all contexts, repeated
  prefix extraction reaches the whole support, and the Hall load is
  unchanged.  No support-only theorem can recover the erased outer context.

The second obstruction has a scalable planar realization with rank
`O(log n)` source contexts and quadratic logarithmic context entropy.
Take one convex cap `Q`, and a large convex endpoint cloud `L` in a small
neighbourhood of a nested left endpoint.  Every `z in L` together with any
three cap points is a rooted `1+3` circuit, while every subset of `L` and
every subset of `Q` is ordinary.  Index contexts by the rank-`k` faces of
`L`, mark one canonical `z`, and give every context the identical Boolean
support bank `2^Q-{emptyset}`.  Then

\[
 M=\binom hk,\qquad z_Q=(3/2)^q-1,qquad
 \Lambda^*={M2^{-k}\over z_Q}.                         \tag{8}
\]

Every prefix `I subset Q` occurs in all `M` contexts and all completion
supports are identical.  The outer shield is nevertheless exact:

\[
             M2^{-k}\le\sum_{A\subseteq L}2^{-|A|}
                         =(3/2)^h.                     \tag{9}
\]

For `h=Theta(n)` and `k=kappa log n`,

\[
             \log M=(\kappa+o(1))(\log n)^2,           \tag{10}
\]

so this regression carries the requested quadratic context entropy on the
bounded-rank slice.  It is not an EIC' counterexample: the synchronized
support failure canonically exposes the large convex outer shield `L`.

The remaining theorem is now precise:

> when a common-prefix fibre has high multiplicity of one completion
> support, recover from the actual source/chronology data either a common
> convex outer shield like `L`, or a bounded-overlap partition of the outer
> contexts.  The support banks themselves contain no such decoder.

## 1. Exact Hall min-load and removal of the empty face

Let `C` be a finite set of contexts and `O` a finite set of ordinary
outputs.  Context `c` may route only to `B_c subseteq O`, and output `F`
has capacity `w(F)`.  The minimum possible normalized maximum load is

\[
 \Lambda^*=\min_a\max_F{\sum_ca(c,F)\over w(F)},       \tag{11}
\]

where `a(c,F)>=0`, is supported on `F in B_c`, and
`sum_Fa(c,F)=d_c`.  Fractional Hall/max-flow gives the exact dual formula

\[
 \boxed{
 \Lambda^*=\max_{\varnothing\ne A\subseteq C}
 {\sum_{c\in A}d_c\over
   \sum_{F\in\bigcup_{c\in A}B_c}w(F)}.}              \tag{12}
\]

The denominator is the capacity of a union, so no bank is spent once per
context.

The empty face belongs to every hereditary face bank and carries capacity
one.  It contains no support information.  Define throughout

\[
                  B_c=\mathcal F(Q_c)-\{\varnothing\}. \tag{13}
\]

Every nonempty support has `z_c>0`.  Excluding the empty output only makes
the routing problem harder and therefore gives a valid upper-bound target
for the original problem.  For a Boolean `q`-cube the lost capacity is
exactly one out of `(3/2)^q`; for `q=Theta(log n)` it is a fixed-power
negligible fraction, but no asymptotic approximation is used below.

Route proportionally inside each bank:

\[
             a(c,F)=d_c{2^{-|F|}\over z_c}.            \tag{14}
\]

Its normalized output load is

\[
             \ell(F)=\sum_{c:F\in B_c}{d_c\over z_c}. \tag{15}
\]

If the banks are hereditary and `x in F`, then

\[
       \{c:F\in B_c\}\subseteq\{c:\{x\}\in B_c\}.
\]

Consequently `ell(F)<=ell({x})`.  The maximum load in (14) is attained at
a singleton, proving (3).  Combining (3) with (12) gives the exact global
dichotomy

\[
 \boxed{
 \Lambda^*\le
 \max_x\sum_{c:x\in Q_c}{d_c\over z_c}.}              \tag{16}
\]

For a bucket with `d<=d_c<2d` and `z<=z_c<2z`, a load greater than
`lambda` forces one point into more than `lambda z/(2d)` contexts.  Thus a
quadratic weighted load produces a quadratic raw support codegree after
only the explicit demand/capacity bucketing loss.

## 2. Common-prefix extraction without square loss

Fix arbitrary nonnegative weights `a_c`.  Count pairs `(c,I)` with
`I in B_c` and `|I|=t`, weighted by `a_c`.  Their total is at least

\[
                         b_t\sum_ca_c.                 \tag{17}
\]

There are at most `binom(n,t)` possible `I`, so one receives at least the
average, proving (4).  Notice that (17) is a first moment.  It neither
creates nor consumes a pair of contexts.

For Boolean `q`-cubes, every `t`-subset of `Q_c` is present.  For a partial
cube, a rank-`t` face chooses `t` roles and one label from each, giving
(5).

Let `n=2^L`, `q=kappa L+O(1)`, and `t=tau L+O(1)`, with
`0<tau<kappa`.  Then

\[
 \log{\binom qt\over\binom nt}
       =-\tau L^2+O(L\log L).                          \tag{18}
\]

Substitution in (4) proves (6).  Thus `Theta(log n)` successive common
labels can be retained while losing a controlled amount of the quadratic
coefficient.

This statement must be applied to the literal linear Hall weights, for
example `a_c=d_c/z_c` from (15).  If a previous argument supplies a
two-record count, its diagonal/source multiplicity must be removed before
(4); otherwise one would reintroduce the known square-to-linear error.

## 3. Exact prefix factoring and completion multiplicity

Suppose first that `Q_c` is itself in convex position, so its bank is the
Boolean cube.  For `I subset Q_c`, define

\[
 \mathcal B_c[I]=\{I\cup S:S\subseteq Q_c-I\}.         \tag{19}
\]

This is an ordinary bank, all outputs contain the fixed recoverable prefix,
and direct factorization gives the first formula in (7).

For a partial cube with global disjoint roles `Y_(c,1),...,Y_(c,r)`, let
`J(I)` be the roles occupied by `I`.  If `I` contains at most one point per
role, put

\[
 \mathcal B_c[I]=\left\{I\cup S:
       |S\cap Y_{c,i}|\le1\ (i\notin J(I)),\quad
       S\cap Y_{c,i}=\varnothing\ (i\in J(I))\right\}. \tag{20}
\]

Every output is again a partial transversal, and the second formula in
(7) follows coordinatewise.

Now fix one common `I` fibre and merge contexts having the same completion
support.  Let `Delta_I` be the maximum resulting multiplicity and let
`E_I` be the family of distinct completion supports.  When these
completions are ordinary rank-`r'` faces, exact role-colouring with state
loss `Gamma_I` gives disjoint coordinate supports, redundancy `R_I`, and
the existing support theorem yields

\[
 {V(P)\over |C_I|}\ge{1\over\Gamma_I\Delta_I}
 \max\left\{1,{f(N_I)2^{R_I}\over P_I}\right\}.       \tag{21}
\]

This is the high-redundancy exit with the correct global multiplicity.

In the low-redundancy branch, semialgebraic retention gives a product of
completion roles.  To use (19) rather than an unprefixed completion bank,
the retained sign certificate must include the fixed points of `I` and
certify that `I` plus every completion transversal is ordinary.  Under
that explicit hypothesis, the prefixed partial bank has the exact count
and half-weight products in (7).  Random role-colouring alone does not
supply this compatibility for arbitrary interlaced supports.

If `Delta_I` is comparable to `|C_I|`, (21) is empty: the support data have
forgotten essentially the whole context alphabet.  Repeating (4) cannot
repair this, because every further prefix sees the same completion.  This
is the synchronized-support residual.

For a general induced face bank, even (19) is false.  Let `a,b,c` be a
triangle and let `x` lie strictly inside it.  The singleton `I={a}` is
ordinary and `S={b,c,x}` is an ordinary face of `Q-I`, but

\[
                         I\cup S=\{a,b,c,x\}            \tag{22}
\]

is nonconvex.  Therefore common-face extraction may be followed by a
completion recursion only for a genuinely prefix-closed Boolean/partial
bank or after proving a separate guard-release lemma.

## 4. A scalable planar synchronized-support regression

Fix `q>=3` and take the convex cap

\[
                         Q=\{(i,i^2):0\le i<q\}.        \tag{23}
\]

Put `ell_0=(-2,-100q^2)`.  For sufficiently small positive rational
`epsilon`, take

\[
 L=\left\{\left(-2-j\epsilon,
        -100q^2+(j\epsilon)^2+j\epsilon^3\right):1\le j\le h\right\}.
                                                               \tag{24}
\]

The cloud `L` is in convex position.  The secant slopes from `ell_0` to the
parabola cap are strictly decreasing; the perturbations in (24) preserve
all strict signs.  The usual ray-and-chord argument gives

\[
       \{z,w_i,w_j,w_k\}\text{ nonconvex}
       \quad(z\in L,\ i<j<k).                           \tag{25}
\]

All coordinates are rational and a sufficiently small `epsilon` avoids
every forbidden collinearity.  Thus the fixed first cap triple is one
canonical rooted `1+3` trace for every `z`.

Let contexts be all `k`-subsets `A subset L`, each an ordinary source face,
with its first label marked as the endpoint role.  Give every context the
same interval support `Q` and Boolean bank

\[
                         B_A=2^Q-\{\varnothing\}.       \tag{26}
\]

Assign the literal source weight `d_A=2^{-k}`.  Since all banks are
identical, the full context set is a Hall witness and proportional routing
is constant on every output.  Therefore (8) is exact.

For every `I subseteq Q`, all contexts contain `I`, and after factoring it
the completion support is always `Q-I`.  Hence

\[
                         \Delta_I=M.                   \tag{27}
\]

Neither codegree localization, rank-`t` prefix extraction, high-support
redundancy, nor low-redundancy retention distinguishes the contexts.

The erased alphabet is visible geometrically: it is the convex cloud `L`.
Every source context is one of its faces, and the complete downset gives
(9).  If `h=Theta(n)` and `k=floor(kappa log n)`, Stirling gives (10), while
the source rank remains `O(log n)`.  The regression therefore preserves
the bounded-rank and quadratic-mass hypotheses demanded by the live
profile slice.

This example is the exact reason a global completion theorem must retain
the actual source/chronology mark.  A statement formulated only in terms
of `(Q_c,B_c,d_c)` is false: arbitrary many distinct outer contexts may
reuse one identical internal cube.

## 5. What is closed and what remains

The following steps are rigorous and global.

1. Delete the empty output and use (12)--(16).
2. A high Hall load gives one high weighted singleton codegree.
3. Use (4) directly, rather than iterated pigeonholing, to retain a
   `Theta(log n)` common prefix with the exact coefficient loss (18).
4. Boolean and partial cubes factor over that prefix by (7).
5. Merge identical completion supports and pay their multiplicity exactly
   in (21).

The remaining branch is also exact: `Delta_I` is large.  The support union
has then erased a large external context alphabet.  The synchronized cap
construction shows that planarity allows this branch, but exposes a convex
outer shield which pays it.

What is not proved is the corresponding structural theorem for arbitrary
live marked histories:

\[
 \text{large completion multiplicity}
 \Longrightarrow
 \text{recoverable convex outer shield with bounded global overlap}. \tag{28}
\]

The context source faces themselves give only the baseline linear bank;
the desired fixed-power gain requires a downset, chronology alphabet, or
another completion family beyond that baseline.  Equation (28), with the
actual marked root retained, is the sole remaining global support-union
gate.  No EIC' closure is claimed here.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_global_support_union_hall.py
```

The verifier checks the exact fractional Hall formula by exhaustive
linear-program-free subset enumeration, proportional singleton domination,
the weighted rank-`t` double count, Boolean and partial prefix
factorizations, the four-point failure for arbitrary induced banks, and a
rational finite instance of the synchronized cap/outer-shield regression.
