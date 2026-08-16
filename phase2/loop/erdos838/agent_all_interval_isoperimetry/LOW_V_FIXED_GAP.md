# Fixed-gap low-count regularization: exact threshold, prime reduction, and a scalar obstruction

**Date:** 2026-08-14.  All logarithms are base two.  Write `V(P)` for the
number of nonempty convex-position subsets of a planar point set `P`, and
write `d(P)` for the largest cardinality of a mirror-decomposable subset of
`P`.

## 1. Verdict

The fixed gap below one half is genuinely useful, but it does not by itself
produce a structural decomposition.  Its exact use is the following.

> **Fixed-gap extraction threshold.**  If
> 
> ```text
> log V(P) <= (1/2-delta)(log n)^2,
> ```
> 
> then a mirror-decomposable subset of size `n^(alpha+o(1))` is already a
> contradiction as soon as
> 
> ```text
> alpha > sqrt(1-2 delta).                         (1)
> ```

Thus the useful target is not literally near-spanning: for fixed `delta`, a
fixed polynomial exponent below one suffices.  Conversely, every putative
sub-half family must satisfy the quantitative inverse bound

```text
d(P) <= n^(sqrt(1-2 delta)+o(1)).                 (2)
```

The known guarded towers do not challenge (1).  Their convex-count
coefficient is above `1/2`, while every fixed or vanishing-mesh vertical
tower has coefficient at least `1/2`.  In fact a homogeneous vertical tower
under the displayed sub-half cap must contain a macro template occupying a
fixed positive fraction of the total logarithmic scale.

There are also two sharp limitations.

1. Adding a generic outer triangle changes `log V` by at most three bits,
   changes `d(P)` by at most three points, and makes the canonical module
   tree a single indecomposable node.  Therefore low count plus the fixed gap
   does not make canonical decompositions nontrivial; any structural theorem
   for prime triangular-hull configurations is already the full theorem.
2. A scalable abstract hereditary complex below one half can satisfy the
   scalar relations `CU >= V`, the cup--cap size constraint, and the sharp
   theorem on every declared decomposable subconfiguration, while having no
   decomposable set larger than `O(log n)`.  It is not a planar order type,
   but it proves that scalar count data cannot establish (1); the missing
   input must use oriented planar compatibility.

So this lane gives an exact reduction rather than a proof of Erdős 838: a
successful low-`V` stability lemma must be an oriented geometric theorem
strong enough to cross the exponent in (1).

## 2. The fixed-gap threshold

The audited strong-tree theorem gives an absolute constant `K` such that
every mirror-decomposable `m`-point set `D` satisfies

```text
log V(D) >= (1/2)(log m)^2-K(log m)^(3/2).        (3)
```

> **Theorem 1 (quantitative transfer and inverse constraint).**  Fix
> `0<delta<1/2`.  Let `P_j` be point sets with `n_j -> infinity` and
> 
> ```text
> log V(P_j) <= (1/2-delta)(log n_j)^2.           (4)
> ```
> 
> Then
> 
> ```text
> limsup_j log d(P_j)/log n_j <= sqrt(1-2 delta). (5)
> ```

**Proof.**  Choose a largest mirror-decomposable `D_j subset P_j` and put
`L_j=log n_j`, `s_j=log |D_j|`.  Heredity of convex position and (3) give

```text
(1/2-delta)L_j^2
 >= log V(P_j)
 >= log V(D_j)
 >= (1/2)s_j^2-Ks_j^(3/2).                       (6)
```

If `s_j/L_j` has a positive limit point `alpha`, divide (6) by `L_j^2`.
The error is `O(L_j^(-1/2))`, and hence

```text
1/2-delta >= alpha^2/2.
```

The same conclusion is automatic when the limit point is zero.  Taking the
largest limit point proves (5).  In particular, an extraction with exponent
strictly larger than the right side contradicts (4).  `square`

The threshold is exactly the quadratic extraction loss.  It also shows why
the fixed gap is essential.  As `delta -> 0`, the required exponent tends to
one, and the guarded-template obstruction in `../agent_low_v_structure/`
rules out such an unconditional near-spanning conclusion even at coefficient
`1/2+epsilon`.

There is a useful logical warning.

> **Corollary 2 (fixed-gap regularization is equivalent in strength to the
> missing lower bound).**  Suppose that for every fixed `delta>0` there is
> an `alpha_delta>sqrt(1-2delta)` such that every sufficiently large `P`
> satisfying (4) has `d(P)>=n^(alpha_delta-o(1))`.  Then
> 
> ```text
> log V(P) >= (1/2-o(1))(log |P|)^2
> ```
> 
> for all planar point sets.  Conversely, that lower bound makes each fixed
> gap hypothesis (4) empty for sufficiently large `n`.

Thus the requested stability statement is a valid attack on the whole
problem, but not a formally weaker cleanup lemma.

## 3. Prime triangular-hull reduction preserves both low count and extraction

The canonical module tree is not rescued by imposing (4).

> **Theorem 3 (outer-triangle preservation).**  Let `P` be any `n`-point
> planar set.  Choose three generic points `O={o_1,o_2,o_3}` whose triangle
> strictly contains `P`, and put `Q=P union O`.  Then `Q` is in general
> position, has triangular convex hull, and its canonical module tree is a
> single indecomposable node.  Moreover, with the empty set included,
> 
> ```text
> Vhat(P) <= Vhat(Q) <= 8 Vhat(P),                 (7)
> d(P) <= d(Q) <= d(P)+3.                         (8)
> ```

**Proof.**  The geometric assertions follow after a generic perturbation of
the outer triangle.  A nontrivial canonical bowtie decomposition has at
least four hull vertices, so a nonconvex triangular-hull set has a one-node
indecomposable tree.

For every convex-position `A subset Q`, the intersection `A intersect P` is
convex-position in `P`.  Once this intersection is fixed there are at most
`2^3` choices for `A intersect O`, proving the upper bound in (7); the lower
bound follows from `P subset Q`.

If `D subset Q` is mirror-decomposable, then `D intersect P` is
mirror-decomposable because that class is hereditary.  Hence

```text
|D| <= d(P)+|O|=d(P)+3.
```

The other inequality in (8) again follows from inclusion.  `square`

The same deletion observation preserves any hereditary mutually-avoiding or
strong-pair witness up to three points.  Consequently, if a sub-half family
exists, it can be made module-indecomposable with the same quadratic
coefficient and the same decomposable-extraction exponent.  A proof based on
the canonical module tree must therefore solve its prime node directly.

## 4. Fixed gap forces a macroscopic primitive scale in vertical towers

The fixed gap does have an exact structural consequence inside the full
homogeneous vertical-composition universe.  Let

```text
Q_0 = one point,             Q_j=S_j[Q_(j-1)],
l_j=log |S_j|,               L_d=sum_(j<=d)l_j=log |Q_d|,
eta_d=max_(j<=d) l_j/L_d.
```

The growing-macro theorem in `../agent_growing_state_upper/` proves

```text
log V(Q_d) >= (1/2)(1-3 eta_d+eta_d^2)L_d^2.      (9)
```

> **Theorem 4 (macroscopic-jump localization).**  If
> 
> ```text
> log V(Q_d) <= (1/2-delta)L_d^2,
> ```
> 
> then
> 
> ```text
> eta_d >= eta(delta):=(3-sqrt(9-8delta))/2.       (10)
> ```

**Proof.**  Combine the assumed upper bound with (9).  This gives

```text
eta_d^2-3eta_d+2delta <= 0.
```

The second root is greater than one, whereas `0<=eta_d<=1`; hence `eta_d`
is at least the first root, which is (10).  `square`

For example, `eta(delta)=2delta/3+O(delta^2)`.  Thus a fixed sub-half gap
cannot be assembled from a vanishing mesh of guarded, Pascal, or arbitrary
new indecomposable templates.  Some template has

```text
|S_j| >= |Q_d|^eta(delta).                       (11)
```

In particular, the guarded fixed-template tower has `eta_d=1/d`.  For every
fixed `delta>0`, (10) would bound its depth by `1/eta(delta)`.  Hence no
arbitrarily deep guarded family can satisfy the sub-half hypothesis; this
is the exact point at which the fixed gap removes the near-half guarded
obstruction.

This is the precise vertical analogue of a macroscopic primitive node.  It
does not say that this node is mirror-decomposable.  At a genuinely
macroscopic heterogeneous jump, the common-skew theorem in
`../agent_upper_jump/REPORT.md` gives the sharper remaining alternative:
for a coefficient-minimizing hypothetical family with
`c_*=1/2-delta`, every automatic scale-covering core with
`ell,t=Theta(L)` must have

```text
mu_2(S[I]) <= (2c_*+o(1))ell
            = (1-2delta+o(1))ell.                (12)
```

Indeed, otherwise the exact endpoint product contributes

```text
c_*(ell^2+t^2)+ell t
 = c_*L^2+(1-2c_*)ell t > c_*L^2,                (13)
```

contradicting coefficient minimality.  Therefore a vertical sub-half model
must expose either a near-total primitive macro or a macroscopic induced
macro with a linear two-ended mean-rank deficit.  Endpoint anti-alignment is
not a third escape, because dyadic size and skew bucketing automatically
produce the common-skew core.

## 5. A scalable scalar countermodel

The next construction is deliberately abstract.  It is a hereditary set
system, not a planar order type.  Its purpose is to identify what a proof of
Theorem 1 cannot use by itself.

Fix `0<delta<1/2`, put `c=1/2-delta`, let `n=2^L`, and set

```text
h=ceil((L+log L)/2)+3,           A=2^h,
M=floor(2^(cL^2)).                              (14)
```

Choose the least integer `R` satisfying

```text
R^2 >= (M+2R)A + sum_(j=0)^3 binom(n,j).         (15)
```

For all sufficiently large `L`, `M+2R <= binom(n,h)`.  Choose that many
distinct `h`-subsets of `[n]`; call the collection `G`, and distinguish two
disjoint subcollections `G_C,G_U`, each of size `R`.  Define

```text
K = {X:X subset G for some G in G} union binom([n],<=3),
C = {X:X subset G for some G in G_C} union binom([n],<=2),
U = {X:X subset G for some G in G_U} union binom([n],<=2).       (16)
```

Assign every triple not already covered to `C` as well.  This makes every
abstract triple an endpoint type without changing any quadratic
coefficient.  Making all uncovered triples caps is intentionally
nongeometric and is one transparent reason the model need not be
stretchable.

Finally declare the structured subconfigurations to be precisely the sets
in `K`.  This is harmless for the audit: if `D in K`, then every subset of
`D` lies in `K`, so its induced convex count is exactly `2^|D|` and is much
larger than the strong-tree lower bound.

> **Proposition 5 (scalar profile obstruction).**  The system (14)--(16)
> is hereditary and satisfies
> 
> ```text
> log |K| = (1/2-delta)L^2+O(L),                 (17)
> |C||U| >= |K|,                                 (18)
> max{|X|:X in K}=h=O(L).                        (19)
> ```
> 
> It also contains all triples, assigns every triple to an endpoint type,
> has cap and cup ranks `h`, and
> 
> ```text
> binom(2h-2,h-1) >= n                           (20)
> ```
> 
> for all sufficiently large `L`, so it respects the scalar cup--cap size
> constraint.

**Proof.**  Heredity is immediate.  Put
`T=sum_(j=0)^3 binom(n,j)`.  Every member of `K` is either one of the `T`
small sets or a subset of one of `M+2R` generators.  Hence

```text
M <= |K| <= (M+2R)2^h+T <= R^2,                 (21)
```

where the last inequality is (15).  On the other hand `|C|,|U|>=R`, so
(18) follows.  Solving the quadratic in (15) shows

```text
R=2^((c/2)L^2+O(L)),
```

and (17) follows from (21).  All members of `K` have size at most `h`, and
the chosen generators show equality.  Finally the central binomial lower
bound

```text
binom(2h-2,h-1) >= 2^(2h-2)/(2h-1)
```

and the definition of `h` prove (20).  `square`

This model simultaneously has sub-half total mass, the universal scalar
endpoint product, adequate cap--cup ranks, and perfect behavior on every
declared structured subset, but its largest structured subset is only
`O(log n)`.  It is nonrealizable -- planar orientation compatibility is
exactly what has been omitted.  Therefore a proof of fixed-gap
regularization must use circuits, tangencies, or another oriented
compatibility law; entropy of `V`, separate endpoint totals, heredity, and
the strong theorem on extracted pieces are insufficient.

## 6. What remains

The clean surviving target is now quantitative:

> Under (4), prove either `d(P)>=n^(alpha_delta-o(1))` for some
> `alpha_delta>sqrt(1-2delta)`, or produce a family of forward-compatible
> strong pieces whose injective endpoint mass is at least
> `2^((1/2-delta+Omega_delta(1)))(log n)^2`.

The outer-triangle theorem says this must work inside a one-node
triangular-hull order type.  The vertical localization theorem says that all
known recursive near-half obstructions are irrelevant below a fixed gap:
the only recursive escape is a macroscopic primitive macro with the rank
deficit (12).  Bridging that primitive macro to a large structured subset or
to compatible endpoint mass is the unresolved geometric stability lemma.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_all_interval_isoperimetry/verify_low_v_fixed_gap.py
```

The script checks the exact extraction thresholds, the quadratic root in
(10), and finite integer instances of the scalar countermodel, including
(15), generator availability, `CU>=V`, and the cup--cap rank constraint.
