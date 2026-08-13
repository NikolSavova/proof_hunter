# Erdős 838: the convex-quadruple clique route and its barriers

## Verdict

A point subset is in convex position if and only if each of its four-point
subsets is in convex position.  Thus convex `k`-sets are `k`-cliques in the
4-uniform hypergraph `H(P)` whose edges are the convex quadruples of `P`.

This reformulation is exact, but fixed-order density information does not
currently yield the desired growing-`k` supersaturation gain.

1. Any argument using only lower densities of convex `j`-sets for fixed
   `j` (including the exact `c_4` or `c_5`) has a sharp abstract obstruction:
   a random 4-graph has every fixed induced density bounded away from zero,
   yet has clique number only `Theta((log n)^(1/3))`, far below
   `k=Theta(log n)`.
2. The first universal flag-complex inequality, obtained by counting
   nonedges, gives existence only for `k=O(1)` because the convex-quadruple
   nonedge density is a positive constant.
3. A genuinely geometric stress test---the limiting fixed-`k` densities of
   infinitely iterated balanced Pascal templates---does not refute the target
   `c_k >= 2^{-(1-eta)k^2+o(k^2)}`.  Exact fixed-point computation instead
   gives an apparent exponent rising slowly from `0.168` at `k=10` to `0.390`
   at `k=120`.  This is evidence that a large gain may be true, but not a
   proof and not yet an asymptotic formula.

The missing ingredient is a *growing-order planar flag theorem*: an inequality
coupling the common-endpoint cap/cup path counts, not just fixed induced
densities or the usual one-endpoint downsets.

All logarithms are base two.

## 1. Convex sets are cliques of convex quadruples

### Lemma 1 (four-point flag property)

For a finite planar point set `X` in general position, `X` is in convex
position if and only if every four-point subset of `X` is in convex position.

#### Proof

The forward implication is hereditary.  Conversely, if `X` is not in convex
position, choose a nonvertex `x in X`.  Then `x` lies in the convex hull of
`X\{x}`.  By Carathéodory's theorem in the plane, `x` lies in the convex hull
of three points `a,b,c in X\{x}`.  General position makes the containment
strict, so `{x,a,b,c}` is not in convex position. `square`

Let `H(P)` be the 4-graph on `P` whose edges are its convex quadruples.
Lemma 1 says exactly

```
v_k(P) = number of copies of K_k^(4) in H(P).       (1)
```

The complementary 4-graph records quadruples with one point inside the
triangle of the other three.

## 2. The strongest elementary density consequence

Let `q(P)` be the fraction of nonconvex quadruples.  For a uniformly random
`k`-subset `X`, let `B(X)` be its number of nonconvex quadruples.  Then

```
E B(X)=q(P) binom(k,4).                             (2)
```

Since `1_{B=0} >= 1-B`,

```
v_k(P)/binom(n,k) >= 1-q(P)binom(k,4).             (3)
```

More generally, if an `m`-point induced subset has nonedge density at most
`q`, averaging (3) and lifting gives nothing beyond the same bound, because
each nonedge is seen in exactly `binom(n-4,m-4)` restrictions.

The minimum asymptotic density of convex quadrilaterals is a positive
constant strictly below one; equivalently, `q(P)` can be bounded away from
zero in extremal configurations.  Therefore (3) becomes vacuous once `k`
exceeds an absolute constant.  Exact knowledge of `c_4` cannot by itself
reach `k=Theta(log n)`.

The same issue affects any finite Bonferroni expansion: it requires joint
density information for growing systems of overlapping nonconvex quadruples,
not merely the one-edge density.

## 3. Fixed-order densities have an abstract quasirandom barrier

The obstruction persists if one knows the density of every convex
`j`-configuration for all `j<=L`, with `L` fixed.

### Proposition 2 (finite-density information does not force logarithmic
cliques)

Fix `0<p<1`, a positive integer `L`, and `epsilon>0`.  For all sufficiently
large `n`, there is a 4-graph `G` such that

1. every vertex subset `U` of size at least `n^epsilon` has 4-edge density
   `p+o(1)`;
2. for every fixed `j<=L`, its induced `K_j^(4)` density is
   `p^{binom(j,4)}+o(1)`; but
3. its clique number is `O((log n)^(1/3))`.

#### Proof

Take the binomial random 4-graph `G^(4)(n,p)`.  Chernoff's inequality and a
union bound over all `U` of size at least `n^epsilon` give (1): for a fixed
`m`, the failure probability for one `U` is `exp(-Omega(m^4))`, while there
are at most `binom(n,m)<=exp(m log(en/m))` such sets.  The former exponent
dominates uniformly for every `m>=n^epsilon`; summing over the at most `n`
possible sizes is harmless.  The same bounded-pattern concentration gives
(2).

For a fixed `t`, the expected number of `t`-cliques is

```
binom(n,t) p^{binom(t,4)}
 <= 2^{t log n-c_p t^4+O(t^3)},                   (4)
```

where `c_p=-log p/24>0`.  Taking `t=C_p(log n)^(1/3)` with a sufficiently
large constant makes (4) tend to zero.  With positive probability all three
properties hold. `square`

This does not construct a point order type: random 4-graphs violate many
oriented-matroid constraints.  Its conclusion is methodological.  No theorem
whose hypotheses are only finitely many fixed-order densities, even
hereditarily across all polynomial-size subsets, can prove logarithmic
cliques.  A successful use of the planar equations must retain constraints
of order growing with `k`.

## 4. Low-order planar equations do not close the gap

The five-point relation is illustrative.  A general-position five-set has
one of three hull sizes.  If `q_4(X)` denotes the number of its convex
quadruples, then

```
hull size 3: q_4=1,
hull size 4: q_4=3,
hull size 5: q_4=5.                               (5)
```

Thus the mean `q_4` determines one linear combination of the three five-point
order-type densities, while the convex-five density is only one of the three
unknowns.  Nonnegativity gives some linear bounds, but no recursive control
at growing order.  Higher fixed-order flag equations have the same basic
limitation highlighted by Proposition 2 unless one proves a specifically
planar inequality uniform in their order.

There is an exact endpoint decomposition for planar order types,

```
V(P)=|P|+sum_{s<t} c(s,t)u(s,t),                  (6)
```

where `c(s,t)` and `u(s,t)` count caps and cups with the **same left and
right endpoints**.  This endpoint matching is indispensable.  Multiplying
path counts that retain only their final edge counts split objects rather
than convex polygons: on the six-point cell `T_{4,2}`, that incorrect sum is
`44`, while the true nonempty convex-subset count is `50`.  In particular,
the usual maximum-red/blue-path downsets, which discard the left endpoint,
cannot simply be weighted and inserted into (6).

## 5. Exact limiting density in iterated Pascal templates

The local target from the hereditary analysis is

```
c_k >= 2^{-(1-eta+o(1))k^2}                       (7)
```

for some fixed `eta>0`, with a uniform finite version.  To test whether (7)
is already false geometrically, consider infinite iteration of a fixed
vertical template `S` of size `r`.

Let `c_j(S),u_j(S),v_j(S)` be its graded profiles.  For its depth-`d`
iterate of size `N_d=r^d`, put

```
A_h(d)=c_h(Q_d)/binom(N_d,h),
B_h(d)=u_h(Q_d)/binom(N_d,h),
D_h(d)=v_h(Q_d)/binom(N_d,h).
```

For each fixed `h`, the exact graded composition recurrence and
`binom(N,h)~N^h/h!` give triangular limits `A_h,B_h,D_h`.  With `A_1=B_1=D_1=1`,

```
A_h = [h!/r^h]/[1-r^{1-h}]
      sum_{j=2}^h c_j(S) A_{h-j+1}/(h-j+1)!,      (8)

B_h = [h!/r^h]/[1-r^{1-h}]
      sum_{j=2}^h u_j(S) B_{h-j+1}/(h-j+1)!,      (9)

D_h = [h!/r^h]/[1-r^{1-h}]
      sum_{j=2}^h v_j(S)
      sum_{a+b=h-j+2} A_aB_b/(a!b!).             (10)
```

Equation (10) includes the within-block term through the denominator.  These
are exact fixed-point identities for the limiting density; no depth fitting
or floating-point subset enumeration is involved.

The script `fixed_k_density.py` evaluates (8)--(10) with arbitrary-precision
decimal arithmetic for balanced central Pascal templates.  Optimizing the
template row over the searched range gives

| `k` | best `-log_2 D_k/k^2` | template row `m` | `r=binom(m,floor(m/2))` |
|---:|---:|---:|---:|
| 10 | 0.167935 | 8 | 70 |
| 20 | 0.247243 | 14 | 3432 |
| 30 | 0.286060 | 14 | 3432 |
| 40 | 0.312947 | 18 | 48620 |
| 50 | 0.331496 | 22 | 705432 |
| 60 | 0.345237 | 24 | 2704156 |
| 70 | 0.355793 | 28 | 40116600 |
| 80 | 0.365158 | 24 | 2704156 |
| 100 | 0.379427 | 30 | 155117520 |
| 120 | 0.389656 | 36 | 9075135300 |

The maximizing row is shallow relative to `k` (roughly `0.3k` in this
range), and the exponent is still increasing.  These data do **not** identify
its limit.  In particular they neither prove a fixed `eta` in (7) nor show
that the exponent tends to one.  What they do establish is that this natural
geometric extremal family does not currently falsify the target: through
`k=120` its exponent is below `0.39`, leaving a very large numerical margin.

The finite-depth script `pascal_vk_probe.py` independently implements the
graded integer recurrence.  For fixed `k` and growing depth its density
converges to (8)--(10), providing a separate check of the normalization.

## 6. What theorem would actually suffice

The desired gain cannot be extracted from `c_4`, `c_5`, or any other fixed
list of densities.  A useful theorem must be uniform at order
`k=Theta(log n)` and exploit one of the following genuinely planar objects:

1. the joint distribution of the **two-endpoint** cap/cup counts
   `c(s,t),u(s,t)` in (6);
2. growing families of forbidden nonconvex quadruples together with the
   rank-3 oriented-matroid elimination constraints; or
3. a planar flag-algebra inequality whose flag size grows with `k` and whose
   error remains uniform for `n>=2^{rho k}`.

A particularly clean target remains

```
mu_k(2^{2k+o(k)}) >= 2^{(1+eta-o(1))k^2}.         (11)
```

The random-hypergraph barrier says that the proof of (11), if true, cannot be
a density-only clique argument.  The fixed-point experiment says that
balanced recursive order types are compatible with a much stronger result;
the unknown step is turning their endpoint structure into a universal
inequality.

## 7. Verification

From this directory:

```
python3 -m py_compile pascal_vk_probe.py fixed_k_density.py
python3 fixed_k_density.py --k 10 20 30 40 50 60 --max-template 45
python3 pascal_vk_probe.py --k 10 20 30 40
```

Both scripts use exact integer template profiles.  The limiting-density
script uses only the closed triangular equations (8)--(10); its decimal
precision is configurable.
