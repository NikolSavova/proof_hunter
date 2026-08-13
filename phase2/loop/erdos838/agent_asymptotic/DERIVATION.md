# Erdős 838: independent asymptotic audit of the Pascal-row count

## Bottom line

Assume the two geometric facts about the standard strongly glued Pascal row:

1. the cap recurrence and its reflected cup recurrence; and
2. the first-cap / last-cup / at-most-one-intermediate decomposition.

Then the proposed count is correct, with the following sharp conclusion for
this particular construction.  If `P_m` is the row of `2^m` points and `V_m`
is its number of convex-position subsets, then

\[
 \log_2 V_m=\left(\frac1{2\ln2}+o(1)\right)m^2.       \tag{A}
\]

Thus the construction proves

\[
 \limsup_{N\to\infty}
 \frac{\log_2 f(N)}{(\log_2N)^2}
 \leq \frac1{2\ln2}=0.721347520444\ldots .           \tag{B}
\]

The word **sharp** in (A) matters.  The same strong row-orientation law makes
every transversal (one point from every block) a cap.  There are
`prod_i binom(m,i)` such transversals, and that product already has the rate
in (A).  No refinement of the cap recurrence can lower the leading constant
for this construction.

## 1. Solve the cap recurrence

Use nonempty cap counts, so the boundary values are `C[m,0]=C[m,m]=1`.
This convention is the one for which the finite recurrence in the geometry
verifier is exact.  Adding the empty set once at the end is immaterial.

The recurrence to audit is

\[
 C_{m,i}\leq C_{m-1,i}+
 \left(1+{m-1\choose i}\right)C_{m-1,i-1}.           \tag{1}
\]

Let `D[m,i]` be the array obtained by replacing (1) with equality.  Expand
`D[m,i]` as a sum over lattice paths.  A horizontal step has weight one.  If
the `j`-th diagonal step is made at time `t_j`, its weight is

\[
 q(t_j,j)=1+{t_j-1\choose j}.
\]

There must remain room for the other `i-j` diagonal steps, hence
`t_j <= m-i+j`.  For fixed `j`, `q(t,j)` is nondecreasing in `t`.  Therefore
the largest path weight is attained by taking all diagonal steps last:

\[
 \prod_{j=1}^i\left(1+{m-i+j-1\choose j}\right).
\]

There are at most `2^m` paths, so

\[
 C_{m,i}\leq D_{m,i}\leq
 2^m\prod_{j=1}^i\left(1+{m-i+j-1\choose j}\right). \tag{2}
\]

Put `i/m -> x`.  The entropy bound for binomial coefficients, summed over
the `i` factors in (2), gives uniformly in `i`

\[
 \log_2 C_{m,i}\leq m^2A(x)+O(m\log m),              \tag{3}
\]

where

\[
 A(x)=\int_0^x(1-x+s)
 H_2\!\left(\frac{s}{1-x+s}\right)\,ds,             \tag{4}
\]

and `H_2(t)=-t log_2 t-(1-t)log_2(1-t)`.  One explicit
form, useful for numerical checks, is

\[
 A(x)=\frac{-x(1-x)-x^2\ln x-(1-x)(1+x)\ln(1-x)}
              {2\ln2}.                              \tag{5}
\]

The limiting middle-cell rate is, for example,
`A(1/2)=0.319663119889...`.

The `O(m log m)` in (3) is more than enough.  It follows directly by using
`log_2 binom(a,b) <= a H_2(b/a)`, paying `O(1)` for each `1+binom`, and using
a uniform Riemann-sum estimate (or crude endpoint truncation followed by
uniform continuity).  No delicate Stirling expansion is needed.

## 2. Optimize the row bound

The geometric decomposition gives

\[
 V_m\leq
 \sum_{0\leq k\leq \ell\leq m}
 C_{m,k}C_{m,m-\ell}
 \prod_{r=k+1}^{\ell-1}\left(1+{m\choose r}\right), \tag{6}
\]

up to a harmless additive term for the empty set.  If `k/m -> x` and
`ell/m -> y`, a summand has base-2 logarithmic rate at most

\[
 \Phi(x,y)=A(x)+A(1-y)+\int_x^yH_2(t)\,dt.           \tag{7}
\]

There is an especially clean pointwise proof of the maximum.  For fixed
`s`, define

\[
 g_s(v)=vH_2(s/v),\qquad v\geq s.
\]

Then

\[
 g_s'(v)=-\log_2(1-s/v)\geq0.                       \tag{8}
\]

In (4), `v=1-x+s <= 1`, so

\[
 (1-x+s)H_2\!\left(\frac{s}{1-x+s}\right)
 \leq H_2(s).
\]

Consequently

\[
 A(x)\leq\int_0^xH_2(t)\,dt,
 \qquad
 A(1-y)\leq\int_y^1H_2(t)\,dt.                    \tag{9}
\]

Substitution in (7) yields

\[
 \Phi(x,y)\leq\int_0^1H_2(t)\,dt
 =\frac1{2\ln2}.                                   \tag{10}
\]

Equality occurs at `(x,y)=(0,1)`; it is the unique continuum maximizer.
Since (6) has only `O(m^2)` terms, (10) proves the upper half of (A).

## 3. A matching lower bound inside the construction

Sequential strong gluing has the row-orientation law: if three points in
increasing x-order lie in three distinct increasing blocks, their
orientation has the same sign (the sign called a cap by the current exact
geometry verifier).  Hence every choice of one point from each block
`T[m,0],...,T[m,m]` is a cap, and in particular is in convex position.
Therefore

\[
 V_m\geq \prod_{i=0}^m{m\choose i}.                 \tag{11}
\]

Using `log_2 binom(m,i)=mH_2(i/m)+O(log m)` and summing,

\[
 \log_2\prod_{i=0}^m{m\choose i}
 =m^2\int_0^1H_2(t)\,dt+o(m^2)
 =\left(\frac1{2\ln2}+o(1)\right)m^2.             \tag{12}
\]

Equations (10)--(12) prove (A), not merely its upper bound.  The endpoint
summand `(k,ell)=(0,m)` in (6), with optional singleton choices in the
intermediate blocks, visibly has the same rate.

## 4. Log bases and conversion from `m` to `N`

For `N=2^m`, put `L=log_2 N=m` and
`kappa=1/(2 ln 2)`.  The equivalent forms are

\[
 \log_2V_m=(\kappa+o(1))L^2,
 \qquad
 V_m=N^{(\kappa+o(1))\log_2N}.                     \tag{13}
\]

With natural logarithms, the coefficient is **not** `kappa`:

\[
 \frac{\ln V_m}{(\ln N)^2}
 \longrightarrow \frac{\kappa}{\ln2}
 =\frac1{2(\ln2)^2}=1.040684490503\ldots .          \tag{14}
\]

For arbitrary `N`, choose `m=ceil(log_2 N)` and delete `2^m-N` points from
`P_m`.  Deletion cannot create additional subsets of the remaining point
set, and `m=log_2N+O(1)`, so (B) holds for the full limsup, not just along
powers of two.

## 5. Exact finite-DP evidence

`dp_audit.py` uses Python integers for (1) and (6).  The displayed row bound
excludes the empty set; adding one does not change the printed digits.

| m | log2 row bound / m^2 | largest summand / m^2 | endpoint summand / m^2 | transversal lower bound / m^2 | maximizing (k,ell) | log2 C[m,floor(m/2)] / m^2 |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 0.743189012 | 0.619274539 | 0.465700694 | 0.411560156 | (2,2) | 0.309637269 |
| 8 | 0.641675765 | 0.598689437 | 0.529239674 | 0.521229730 | (2,6) | 0.281811774 |
| 16 | 0.645925624 | 0.633628174 | 0.596383092 | 0.595574542 | (3,13) | 0.286902338 |
| 32 | 0.665959966 | 0.662240705 | 0.644627744 | 0.644534697 | (5,27) | 0.296094070 |
| 48 | 0.677310708 | 0.675555179 | 0.664509072 | 0.664482061 | (6,42) | 0.300886446 |
| 64 | 0.684486651 | 0.683434153 | 0.675644579 | 0.675633290 | (7,57) | 0.303880938 |
| 96 | 0.693150822 | 0.692647110 | 0.687955030 | 0.687951714 | (9,87) | 0.307498762 |
| 128 | 0.698271657 | 0.697977280 | 0.694731892 | 0.694730499 | (11,117) | 0.309649521 |

The target is `0.721347520444...`; the midpoint cap target is
`A(1/2)=0.319663119889...`.  The finite maximizing pair lies in a shrinking
boundary layer rather than exactly at `(0,m)`, which is compatible with the
unique scaled maximizer `(0,1)`.

Reproduce, for example, with

```sh
python3 phase2/loop/erdos838/agent_asymptotic/dp_audit.py \
  --max-m 128 --show 4,8,16,32,48,64,96,128
```

## 6. Audit findings and stronger-route assessment

1. **Count convention:** the shared draft currently says cap counts include
   the empty set and therefore gives boundary value two.  The exact recurrence
   and the geometry verifier use nonempty counts with boundary value one.
   Normalize the proof to the latter convention and add the empty subset once.
   This is a finite bookkeeping issue, not an asymptotic failure.
2. **The constant survives:** `1/(2 ln 2)` is the correct base-2 coefficient.
   The short inequality (8)--(10) is rigorous and avoids a fragile
   two-variable derivative calculation.
3. **The same construction cannot beat it:** transversal caps give the
   matching lower bound (11)--(12).  Sharpening cap/cup counts, or improving
   the treatment of the `k=ell` case, cannot affect the leading term because
   the leading term comes from the intermediate singleton product.
4. **What a stronger upper bound would require:** either a different bad point
   construction whose block sizes have a smaller entropy integral, or a row
   geometry in which exponentially many transversals fail to be convex while
   the Erdős--Szekeres obstruction is retained.  Merely strengthening (1) is
   asymptotically powerless.
5. **Geometric dependency:** the asymptotic argument is complete conditional
   on the exact strong-gluing orientation and decomposition.  Those are the
   only genuinely geometric inputs; `dp_audit.py` intentionally does not
   certify them.
