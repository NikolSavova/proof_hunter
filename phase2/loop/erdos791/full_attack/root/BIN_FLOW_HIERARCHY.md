# A carry-bin flow hierarchy for Erdős #791

Date: 2026-08-13

## Status

This note proves a universal hierarchy of finite quadratic-flow upper
relaxations for the normalized range constant.  Along nested refinements the
bounds are monotone, and their limit is exactly the weak convolution
relaxation.  This does **not** solve #791: pointwise lattice coverage is still
lost at the limiting step.  The numerical optimization recorded below is
heuristic and is not itself an upper-bound certificate.

## The finite relaxation

Let `m>=1` and let `p=(p_0,...,p_{m-1})` be nonnegative with sum one.  For
`0<=i<=j<m` and `i+j<m`, give the unordered pair cell `(i,j)` capacity

```text
w_ij(p) = p_i p_j       if i<j,
          p_i^2/2       if i=j.
```

Cell `(i,j)` may send flow only to target bins `i+j` and `i+j+1` (when the
latter is below `m`).  Define `U_m` to be the supremum of `c` for which there
are a probability vector `p` and nonnegative flows `x_ijs` satisfying

```text
sum_s x_ijs <= w_ij(p)                         for every pair cell,
sum_{ij} x_ijs >= c/m                          for every target bin s.
```

This is a finite max-min quadratic program.  For fixed `p`, feasibility is an
ordinary bipartite max-flow problem.  Globally optimizing over `p` is the hard
copositive/nonconvex part.

## Theorem 1: every level is a rigorous universal upper relaxation

If

```text
alpha_+ = limsup_k R(k)/k^2,
```

then

```text
alpha_+ <= U_m                                                (1)
```

for every fixed `m`.

### Proof

Take bases `A_k` of size `k`, ranges `N_k`, and a subsequence on which
`N_k/k^2 -> alpha_+`.  Put `M_k=N_k+1` and partition both the elements and the
covered targets by

```text
I_i = {a : floor(m a/M_k)=i},
Q_s = {q : floor(m q/M_k)=s}.
```

Let `a_i=|A_k intersect I_i|`.  Select one unordered representation of every
`q=0,...,N_k`.  A selected pair with endpoints in `I_i,I_j` can represent a
target only in `Q_{i+j}` or `Q_{i+j+1}`, because

```text
(i+j)/m <= (a+b)/M_k < (i+j+2)/m.
```

Different targets use different unordered pairs.  Hence cell `(i,j)` has
capacity `a_i a_j` for `i<j` and `a_i(a_i+1)/2` for `i=j`.  Each target bin
has `M_k/m+O(1)` selected pairs entering it.  Divide all flows by `k^2`, pass
to a subsequence with `a_i/k -> p_i`, and let `k->infinity`.  The diagonal
`a_i/(2k^2)` term vanishes, leaving exactly the constraints defining `U_m`
with `c=alpha_+`.  This proves (1).

The proof uses actual selected representations, so it does not assume that
different pair cells or target bins are independent.

## Theorem 2: nested levels are monotone

For positive integers `r,m`,

```text
U_(rm) <= U_m.                                                (2)
```

### Proof

Group every `r` consecutive fine element bins into one coarse bin and every
`r` consecutive fine target bins into one coarse target bin.  Fine demands
sum from `c/(rm)` to `c/m`.  The total fine unordered capacity inside two
distinct coarse element bins is `P_I P_J`; inside one coarse bin it is
`P_I^2/2`.  A fine pair eligible for a fine target can enter only one of the
two coarse target bins allowed by the corresponding coarse pair.  Aggregating
the fine flow therefore gives a feasible level-`m` flow at the same `c`.

In particular `U_1,U_2,U_4,...` is nonincreasing.

## Theorem 3: completeness for the continuous relaxation

Define

```text
C_conv = sup {c : some probability measure mu on [0,1] satisfies
                    mu*mu >= 2c Lebesgue measure on (0,1)}.
```

Then

```text
inf_r U_(2^r) = C_conv.                                      (3)
```

### Proof

If `mu*mu >= 2c lambda`, partition `mu` into `m` bins.  The half-product
measure `(mu times mu)/2` gives exactly capacities `p_i p_j` off the diagonal
(after combining the two orientations) and `p_i^2/2` on it.  If `T(u,v)=u+v`
and `rho=T#((mu times mu)/2)>=c lambda`, let
`f=d(c lambda)/d rho<=1` and put
`nu=f(T(u,v))(mu times mu)/2`.  Then `T#nu=c lambda`.  Aggregate this symmetric
submeasure by unordered pair and target bins to obtain a feasible flow.  Thus
`C_conv<=U_m`.

Conversely, suppose `c<U_(2^r)` for every `r`.  Trim the incoming flow in each
target bin to exactly `c/m`.  Choose any point `(u,v)` in a fine pair cell
whose sum lies in its eligible target bin.  Such a point exists by the
eligibility definition.  For an off-diagonal flow atom put half its mass at
`(u,v)` and half at `(v,u)`; for a diagonal atom choose `(u,u)`.  This defines
a symmetric measure `nu_m` whose addition pushforward has exactly `c/m` mass
in every target bin.  Let `mu_m` put mass `p_i` anywhere in element bin `i`.

Although `nu_m` need not be pointwise dominated by
`(mu_m times mu_m)/2` inside each fine rectangle, put each `p_i` at its bin
center.  Fix an ordered coarse dyadic rectangle at level `l` and take only
levels `m=2^r` refining it.  After the off-diagonal symmetrization above, the
summed full-fine-cell inequalities give the required domination for this
coarse rectangle, with only boundary cells of diameter `O(1/m)` undecided.

Compactness gives subsequential weak limits `mu` and `nu`.  Apply Portmanteau
to closed dyadic rectangles enlarged by one fine boundary layer and then let
the enlargement shrink.  Thus

```text
nu <= (mu times mu)/2.
```

first on the dyadic rectangle pi-system and hence, by the monotone-class
theorem, on all Borel sets.  The addition pushforwards converge to `c lambda`:
they and `c lambda` put the same mass in every target bin, so their
Wasserstein-1 distance is at most `1/m`.  Therefore

```text
(mu*mu)/2 >= c lambda.
```

Letting `c` increase to the infimum proves the reverse inequality in (3).

The rectangle-capacity/Portmanteau passage is the key reason nested partitions
are used; an arbitrary nonnested sequence would not by itself identify the
limiting dominating measure.

## Exploratory numerics

`bin_flow_relax.cpp` evaluates the exact inner max flow and heuristically
optimizes the outer masses.  A heuristic value is a **lower bound on `U_m`**,
not a certified universal upper bound.  Initial runs gave:

```text
m=4:   0.5000000
m=8:   0.4877478
m=12:  0.4695453
m=16:  0.4672328
m=20:  0.4559668
```

The decrease is evidence that multi-bin carry constraints see information
absent from one-weight counting.  These values cannot be compared as certified
bounds until the nonconvex outer problem has an exact rational dual
certificate.

## Why this still does not close #791

Equation (3) completes the hierarchy only for the continuous convolution
relaxation.  A measure inequality controls aggregate mass in intervals, while
an additive basis must cover every individual lattice point with only
`Theta(1)` available pairs per point.  Random discretization at constant mean
representation multiplicity leaves a positive density of holes.  No proved
rounding/design theorem currently turns every feasible limiting flow into a
discrete basis with `o(k)` extra elements.

There are two ways this hierarchy could nevertheless close the problem:

1. an exact finite-level dual certificate could match a scalable discrete
   construction; or
2. a new lattice refinement (tracking collisions/differences in addition to
   carry bins) could be proved asymptotically complete for actual bases.

The second item is now the sharply isolated missing bridge.
