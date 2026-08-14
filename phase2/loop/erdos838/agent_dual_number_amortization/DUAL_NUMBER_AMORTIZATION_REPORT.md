# Dual-number braid amortization and the half-weight route

**Date:** 2026-08-13
**Verdict:** no proof of the unrestricted mean bound.  There is a rigorous
global exposure identity, but two exact *realizable* obstructions show that
the obvious amortizations of the local rank-one inequalities are invalid.
The attack nevertheless isolates a cleaner sufficient target,

\[
 H(P):=\frac{nZ_P(1/2)}{Z_P(1)}=O(1),                 \tag{HW}
\]

and gives an exact deletion interface for it.  Every exhaustive or geometric
test is compatible with (HW).  The largest planar value found was about
`1.7835` at 31 points.  This is evidence only: boundedness is not proved.

All partition functions in this report include the empty set unless a
display explicitly says “nonempty.”

## 1. Why (HW) would finish the mean-size route

Let `K` be the size of a uniformly selected convex subset.  Then

\[
 \frac{Z_P(1/2)}{Z_P(1)}=\mathbb E2^{-K}\ge 2^{-\mathbb EK}
\]

by Jensen.  Consequently (HW) gives

\[
 \mu(P)=\mathbb EK\ge \log_2 n-\log_2 O(1).           \tag{1}
\]

This is exactly the mean-size estimate which, through the already proved
deletion lemma, gives

\[
 \log_2 f(n)\ge \tfrac12(\log_2n)^2-O(\log n).
\]

The activity formulation is also useful.  Put

\[
 \mu_\lambda=\lambda\frac{Z'_P(\lambda)}{Z_P(\lambda)}.
\]

Then

\[
 \log\frac{Z_P(1)}{Z_P(1/2)}
 =\int_{1/2}^1\mu_\lambda\,d\log\lambda,
 \qquad
 \frac{d\mu_\lambda}{d\log\lambda}
 =\operatorname {Var}_\lambda K.                     \tag{2}
\]

Thus (HW) says that the activity-integrated mean is at least `log n-O(1)`.
It packages the variance ladder without demanding the false small-`n`
pointwise bound `Var K>=1/ln 2`.

## 2. Exact weighted up/down and deletion identities

For a convex face `A`, let `u(A)` be the number of points which can be added
while staying convex.  Under the probability law proportional to
`lambda^|A|`, double-counting cover relations gives

\[
 \mathbb E_\lambda d_\downarrow=\mu_\lambda,
 \qquad
 \mathbb E_\lambda d_\uparrow=\frac{\mu_\lambda}{\lambda}.              \tag{3}
\]

Indeed, every nonempty face `B` is reached from exactly `|B|` lower faces,
whose total weight is `|B|lambda^{|B|-1}`.

For `p in P`, write `Z_p(lambda)=Z_{P-p}(lambda)`.  The same omitted-point
double count gives, at every activity,

\[
 \sum_p Z_p(\lambda)=(n-\mu_\lambda)Z_P(\lambda).       \tag{4}
\]

Differentiating (4), or weighting by `|A|`, recovers

\[
 \sum_p Z_p(\lambda)\mu_{p,\lambda}
 =\bigl(n\mu_\lambda-\mathbb E_\lambda K^2\bigr)Z_P(\lambda).          \tag{5}
\]

At `lambda=1`, (5) is the deletion--variance identity

\[
 \mu(P)-\frac{\sum_pV_p\mu(P-p)}{\sum_pV_p}
 =\frac{\operatorname {Var}K}{n-\mu(P)}.               \tag{6}
\]

There is a particularly clean recursion for (HW).  Sample a deletion with
probability proportional to `V_p=Z_p(1)`.  From (4),

\[
 \boxed{
 \mathbb E_{p\propto V_p}H(P-p)
 =\frac{n-1}{n}\frac{n-\mu_{1/2}(P)}{n-\mu_1(P)}H(P).}  \tag{7}
\]

This is the best exact induction interface found here.  It would make `H`
nonincreasing along some deletion whenever

\[
 n\bigl(\mu_1-\mu_{1/2}\bigr)+\mu_{1/2}\ge n.          \tag{8}
\]

The exact small minima miss (8) modestly: their activity gaps are about
`0.59--0.60`, rather than nearly one.  So (7) does not by itself prove a
constant bound; it identifies the missing activity drift precisely.

## 3. What global lexicographic braid minimality really gives

For one exposed long braid, retain all four value/derivative boundary
vectors and the common matrices.  The exact formula is

\[
 Z_+(z)=Z_0(z)+z^2\Phi(z),\qquad
 Z_-(z)=Z_0(z)+z^2\Psi(z),                              \tag{9}
\]

where

\[
 \Phi=\beta^TB_0^T\alpha,
 \qquad
 \Psi=\gamma^TA_0\delta.                               \tag{10}
\]

At a global `(V,M)` lexicographic minimum, its current branch satisfies

\[
 \Phi(1)\le\Psi(1),
\]

and, only in case of equality, `Phi'(1)<=Psi'(1)`.

There is also a genuine global exposure statement.  Reverse the entire root
order.  Forward and reverse endpoint products swap, so the full polynomial
is unchanged:

\[
 Z_{R^{\rm rev}}(z)=Z_R(z).                             \tag{11}
\]

By Matsumoto connectivity there is a long-braid path, modulo short
commutations, from `R` to `R^rev`.  Every labeled triple is flipped an odd
number of times.  If `R` is globally lex-minimal and the switch differences
along the path are `D_j(z)`, then

\[
 \sum_{j\le t}D_j(1)=Z_{R_t}(1)-Z_R(1)\ge0,
 \qquad
 \sum_jD_j(z)=0.                                       \tag{12}
\]

When a partial count sum in (12) is zero, its first derivative is also
nonnegative by the second lexicographic coordinate.  This “dual-number
excursion” is rigorous and retains every changing boundary context.

It does **not** yet bound the base mean.  Differences alone are insensitive
to a polynomial common to every state.  A successful use of (12) needs an
absolute anchor relating the common matrices `A_0,B_0` to the switch mass;
telescoping rank-one differences cannot supply that anchor.

## 4. Realizable obstruction: packet preference cannot be transported

The full six-wire commutation graph has 908 classes.  The exact global
lexicographic objective is

```text
(nonempty V,M)=(44,108), profile=(0,6,15,20,3),
```

attained by 12 classes.  Across all twelve global minima, only 16 of the 20
labeled packets are exposed.  The missing packets are exactly

```text
(0,1,5), (0,2,5), (0,3,5), (0,4,5).
```

More decisively, start with the saved global minimum and change only the
packets

```text
(0,3,4), (0,3,5), (0,4,5), (0,2,5).
```

The nonempty objectives along this four-edge path are

```text
(44,108) -> (45,112) -> (48,124) -> (49,128) -> (48,124).
```

The target packet `(0,1,5)` has not moved, so its orientation is unchanged.
It is now exposed, but flipping it gives `(45,112)`: its preferred direction
has reversed.  Every one of the six states has an exact rational fixed-`x`
realization stored in `certificate.json`.

Therefore an exposure path cannot carry the inequality of a packet at the
global minimum to the context in which that packet becomes exposed.  The
four boundary vectors change essentially.  The complete telescoping count is

```text
+1 +3 +1 -1 -3 = +1;
```

global minimality controls this total, not the final `-3` switch.

## 5. Realizable obstruction: lex descent can increase the half weight

A second exact rational fixed-`x` certificate on ten points has one direct
braid on the labeled triple `(1,5,6)`.  Its two nonempty profiles are

\[
\begin{aligned}
Z_+(z)&=10z+45z^2+120z^3+147z^4+88z^5+24z^6+2z^7,\\
Z_-(z)&=10z+45z^2+120z^3+148z^4+87z^5+23z^6+2z^7.
\end{aligned}
\]

The minus branch is strictly better in both lex coordinates:

```text
(V_+,M_+)=(436,1646),   (V_-,M_-)=(435,1639).
```

Nevertheless

\[
 Z_-(1/2)-Z_+(1/2)
 =2^{-4}-2^{-5}-2^{-6}=\frac1{64}>0.                  \tag{13}
\]

The complete local state is

```text
(V0,M0)=(428,1610),
(Phi,Phi')=(8,20),       (Psi,Psi')=(7,15),

alpha  = ((0,0,0,0,0,0,1,1,1,2), (0,0,0,0,0,0,0,1,1,3)),
beta   = ((0,1,0,0,0,0,0,0,0,0), (0,0,0,0,0,0,0,0,0,0)),
gamma  = ((0,0,0,0,0,0,1,0,0,0), (0,0,0,0,0,0,0,0,0,0)),
delta  = ((1,1,0,0,0,0,0,0,0,0), (1,0,0,0,0,0,0,0,0,0)).
```

Each pair records value and derivative.  Thus (HW) cannot be proved by
showing that every `(V,M)`-descending braid also decreases `Z(1/2)`.

For second moments the limitation is even more explicit.  The bonus
`z^2Phi(z)` contributes

\[
 4\Phi(1)+5\Phi'(1)+\Phi''(1)                           \tag{14}
\]

to the raw second moment.  If `Phi(1)<Psi(1)`, lex minimality imposes no
condition at all on either derivative in (14).

## 6. Exact finite audit of the half-weight target

Exhausting **all** reflection-order commutation classes gives:

| `n` | classes | `max H` | number of maximizers |
|---:|---:|---:|---:|
| 3 | 2 | `81/64 = 1.265625` | 2 |
| 4 | 8 | `4/3 = 1.333333` | 4 |
| 5 | 62 | `65/48 = 1.354167` | 22 |
| 6 | 908 | `167/120 = 1.391667` | 12 |
| 7 | 24,698 | `1645/1168 = 1.408390` | 152 |

At every one of these sizes, the set of `H`-maximizers is **exactly** the set
of global trace minimizers.  The exact realizable minima at the next sizes
give

| `n` | empty-inclusive profile | `H` |
|---:|---|---:|
| 8 | `(1,8,28,56,21)` | `325/228 = 1.425439` |
| 9 | `(1,9,36,84,36,3)` | `7875/5408 = 1.456176` |

Further adversarial families do not currently threaten boundedness:

* dyadic Horton sets decrease from `H=1.06` at `n=8` to about `0.1063` at
  `n=128`;
* tested balanced Pascal towers decrease rapidly with depth (for instance the
  `h=4` central template has `H=0.8192,0.1413,0.00281` at depths `2,4,8`);
* the previous evolved planar macros through `n=20` lie between about `1.45`
  and `1.54`.

A coordinate anneal targeted directly at `H` did find slow finite growth:

```text
n       20       24       26       29       30       31       36
H    1.5965   1.6861   1.7190   1.7420   1.7302   1.7835   1.7489
```

The rows are separate heuristic records, not a nested construction, so they
do not demonstrate asymptotic growth.  No value reached `1.8` through the
search at 36 points.  It would be unsafe to infer a constant bound from this
range, but there is also no observed counterexample trend resembling a power
or logarithm.

## 7. A new exact twenty-point record

The half-weight search incidentally found the integer fixed-`x` configuration
stored in `half_weight_search_records.json`.  Its empty-inclusive profile is

\[
 (1,20,190,1140,2415,866,135,8),                       \tag{15}
\]

so

```text
V=4775,  M=18676,
mu=18676/4775=3.9112...,
mu-log2(20)=-0.4107...,
H=4879/3056=1.596531...
```

The previous saved planar `n=20` macro had nonempty count 5155, hence
empty-inclusive count 5156.  The new record improves that finite count by
381.  This is not an asymptotic construction and does not change either
proved coefficient.

The profile has two independent exact checks:

1. `dual_number_obstructions.py` reconstructs the slope order and evaluates
   the reverse products coefficient by coefficient;
2. `direct_hull_n20.cpp` ignores reflection orders and tests all `2^20`
   subsets with an exact-integer monotone convex hull.

Both also verify general position.  Exact replay records at `n=24` and `n=30`
have mean deficits `-0.4933` and `-0.4962`, respectively, still consistent
with a bounded loss in `mu>=log n-O(1)`.

## 8. Surviving proof target

The local braid-amortization plan has reached a clean fork.

* A differences-only argument is blocked by Sections 4--5.
* The viable strengthened target is the absolute matrix inequality

\[
 n\left(1+\frac n2+
   \langle A(1/2),B(1/2)\rangle_F-n\right)
 \le C\left(1+\langle A(1),B(1)\rangle_F\right)          \tag{16}
\]

for global minimum realizable reflection orders.

Equation (16) is just (HW) written with the endpoint matrices.  A braid proof
of it must charge the **absolute common bases** `A_0,B_0`, while using the
rank-one switch inequalities only to prevent repeated charging.  The
reversal excursion (12) is a plausible indexing device, but is not itself the
charge.

The deletion alternative is equally precise: use (7) and prove enough
amortized activity drift that, along a suitable deletion chain,

\[
 \sum_m\left[-\log\left(
 \frac{m-1}{m}\frac{m-\mu_{1/2}(P_m)}{m-\mu_1(P_m)}
 \right)\right]_+<\infty,                               \tag{17}
\]

or establish a compensating decrease of `H` on the steps where (8) fails.
Neither statement is proved here.

## 9. Verification

From the repository root:

```bash
python3 -m py_compile \
  phase2/loop/erdos838/agent_dual_number_amortization/dual_number_obstructions.py

python3 \
  phase2/loop/erdos838/agent_dual_number_amortization/dual_number_obstructions.py \
  --write-certificate \
  phase2/loop/erdos838/agent_dual_number_amortization/certificate.json

c++ -std=c++17 -O3 \
  phase2/loop/erdos838/agent_dual_number_amortization/direct_hull_n20.cpp \
  -o /tmp/direct_hull_n20
/tmp/direct_hull_n20
```

The Python check exhausts the 24,698 seven-wire classes, verifies all saved
fixed-`x` realizations and full dual boundary vectors, replays the exact
`n=20,24,30` coordinate records, and checks the deletion/variance identities.
