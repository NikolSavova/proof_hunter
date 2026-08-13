# Erdős 838: independent asymptotic audit of the Pascal-row count

## Bottom line

Assume the two geometric facts about the standard strongly glued Pascal row:

1. the cap recurrence and its reflected cup recurrence; and
2. the first-cap / last-cup / at-most-one-intermediate decomposition.

Then the proposed row count is correct, but it is not the strongest immediate
consequence of the Pascal construction.  There are two sharp conclusions.

If `P_m` is the full row of `2^m` points and `V(P_m)` is its number of
convex-position subsets, then

\[
 \log_2 V(P_m)=\left(\frac1{2\ln2}+o(1)\right)m^2.    \tag{A}
\]

However, the single central cell

\[
 Q_m=T_{m,\lfloor m/2\rfloor},\qquad
 |Q_m|={m\choose\lfloor m/2\rfloor}=2^{m-o(m)},
\]

has the strictly smaller sharp rate

\[
 \log_2V(Q_m)=
 \left(1-\frac1{4\ln2}+o(1)\right)m^2.             \tag{B}
\]

It therefore gives the stronger Erdős-838 bound

\[
 \limsup_{N\to\infty}
 \frac{\log_2 f(N)}{(\log_2N)^2}
 \leq 1-\frac1{4\ln2}
 =0.639326239778\ldots .                             \tag{C}
\]

The word **sharp** in (A) matters.  The strong row-orientation law makes
every transversal (one point from every block) a cap.  There are
`prod_i binom(m,i)` such transversals, and that product already has the rate
in (A).  Likewise, the top strong-glue split of the central cell realizes all
cap/cup cross-pairs and supplies a matching lower bound in (B).  Better
bookkeeping alone cannot improve either construction's leading constant.

## 1. Solve the cap recurrence

Use nonempty cap counts, so the boundary values are `C[m,0]=C[m,m]=1`.
This convention is the one for which the finite recurrence in the geometry
verifier is exact.  Adding the empty set once at the end is immaterial.

For the standard strong glue, the recurrence is in fact exact:

\[
 C_{m,i}= C_{m-1,i}+
 \left(1+{m-1\choose i}\right)C_{m-1,i-1}.           \tag{1}
\]

Expand `C[m,i]` as a sum over lattice paths.  A horizontal step has weight one.  If
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

The latest-step path occurs as one summand and there are exactly `binom(m,i)`
paths, so, writing `M[m,i]` for its product,

\[
 M_{m,i}\leq C_{m,i}\leq{m\choose i}M_{m,i},\qquad
 M_{m,i}=\prod_{j=1}^i
 \left(1+{m-i+j-1\choose j}\right).                \tag{2}
\]

Put `i/m -> x`.  The entropy bound for binomial coefficients, summed over
the `i` factors in (2), gives uniformly in `i`

\[
 \log_2 C_{m,i}=m^2A(x)+O(m\log m),                  \tag{3}
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

The `O(m log m)` in (3) is more than enough.  It follows from the standard
two-sided entropy estimate for binomial coefficients, paying `O(1)` for each
`1+binom`, and a uniform Riemann-sum estimate (or crude endpoint truncation
followed by uniform continuity).  No delicate Stirling expansion is needed.

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

## 4. A stronger construction: use one central cell

Take `i=floor(m/2)` and `Q_m=T[m,i]`.  Every convex-position subset is
uniquely determined by its upper and lower hull chains.  The upper chain is a
cap and the lower chain a cup.  Reflection of the recurrence gives
`U[m,i]=C[m,m-i]`, and hence

\[
 V(Q_m)\leq C_{m,i}C_{m,m-i}.                       \tag{13}
\]

Since `i/m -> 1/2`, (3) yields

\[
 \log_2V(Q_m)\leq
 \bigl(2A(1/2)+o(1)\bigr)m^2.                       \tag{14}
\]

Formula (5) gives

\[
 A(1/2)=\frac12-\frac1{8\ln2},\qquad
 2A(1/2)=1-\frac1{4\ln2}=0.639326239778\ldots .     \tag{15}
\]

This upper rate is attained inside the cell.  In the top split
`T[m,i]=A prec B`, the union of any cap in the left child with any cup in the
right child is in convex position.  More explicitly, its upper hull is the
left cap together with the rightmost point of the right cup, while its lower
hull is the leftmost point of the left cap together with the right cup; their
union contains every selected point.
The product of the two relevant child counts has rate `2A(1/2)m^2`.
Equivalently, if `W[m,i]` counts nonempty convex subsets, strong gluing gives
the exact recurrence

\[
 W_{m,i}=W_{m-1,i-1}+W_{m-1,i}
          +C_{m-1,i-1}U_{m-1,i}.                   \tag{16}
\]

Thus (B) is an equality for the actual count of the central cell, not just
the rate of a convenient upper bound.

The center is also optimal among all fixed-density single cells under this
analysis.  For `i/m -> x`, the number of points has rate `H_2(x)m`, while a
short simplification of (5) gives

\[
 A(x)+A(1-x)=H_2(x)-\frac{x(1-x)}{\ln2}.            \tag{17}
\]

The coefficient relative to `(log_2 |T[m,i]|)^2` is therefore

\[
 K(x)=\frac{H_2(x)-x(1-x)/\ln2}{H_2(x)^2}.          \tag{18}
\]

To see rigorously that its minimum is at `x=1/2`, write
`h=-x ln x-(1-x)ln(1-x)` and `q=x(1-x)`.  Then
`K=ln(2)(h-q)/h^2`.  On `0<x<1/2`,

\[
 h'=\ln\frac{1-x}{x}>0,\qquad q'=1-2x>0,
 \qquad h\geq2q,
\]

where the last inequality follows by applying `-ln u >= 1-u` to `u=x`
and `u=1-x`.  Hence

\[
 K'(x)=\ln2\,\frac{h'(2q-h)-hq'}{h^3}<0.           \tag{19}
\]

Symmetry finishes the minimization.

## 5. Log bases and conversion from `m` to `N`

For the full row `N=2^m`, put `L=log_2 N=m` and
`kappa_row=1/(2 ln 2)`.  The equivalent forms are

\[
 \log_2V(P_m)=(\kappa_{\rm row}+o(1))L^2,
 \qquad
 V(P_m)=N^{(\kappa_{\rm row}+o(1))\log_2N}.        \tag{20}
\]

With natural logarithms, the coefficient is **not** `kappa_row`:

\[
 \frac{\ln V(P_m)}{(\ln N)^2}
 \longrightarrow \frac{\kappa_{\rm row}}{\ln2}
 =\frac1{2(\ln2)^2}=1.040684490503\ldots .          \tag{21}
\]

For the stronger central-cell bound, let
`kappa_cell=1-1/(4 ln 2)`.  Since

\[
 \log_2{m\choose\lfloor m/2\rfloor}
 =m-\tfrac12\log_2m+O(1),                           \tag{22}
\]

the same coefficient `kappa_cell` appears when (14) is normalized by the
square of the log of the actual number of points.  Given arbitrary `N`, take
the least `m` for which the central binomial coefficient is at least `N` and
delete excess points.  Here `m=log_2N+O(log log N)`.  Deletion cannot create
additional subsets of the remaining point set, proving (C) for the full
limsup.  In natural logarithms the improved coefficient is

\[
 \frac{\kappa_{\rm cell}}{\ln2}
 =\frac1{\ln2}-\frac1{4(\ln2)^2}
 =0.922352795638\ldots .                            \tag{23}
\]

## 6. Exact finite-DP evidence

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

The same integer run also evaluates the exact strong-glue recurrence (16)
for the central cell.  These rates are normalized by the square of the log
of the **actual** cell size, not by `m^2`.

| m | log2 central-cell size | exact cell recurrence / (log2 size)^2 | Cap*Cup upper bound / (log2 size)^2 |
|---:|---:|---:|---:|
| 4 | 2.58496 | 0.844631831 | 1.482841434 |
| 8 | 6.12928 | 0.679099040 | 0.960173583 |
| 16 | 13.65172 | 0.652167052 | 0.788186554 |
| 32 | 29.16298 | 0.646779160 | 0.713010264 |
| 64 | 60.66862 | 0.643917627 | 0.676340224 |
| 96 | 92.37801 | 0.642753181 | 0.664168989 |
| 128 | 124.17143 | 0.642100314 | 0.658077364 |
| 192 | 187.87989 | 0.641378104 | 0.651966544 |
| 256 | 251.67284 | 0.640979821 | 0.648895070 |

Both columns converge to the sharp central-cell target
`0.639326239778...`.  The exact recurrence converges much faster than the
coarse `Cap*Cup` product, but the two have the same quadratic rate.

Reproduce, for example, with

```sh
python3 phase2/loop/erdos838/agent_asymptotic/dp_audit.py \
  --max-m 128 --show 4,8,16,32,48,64,96,128
```

## 7. Audit findings and stronger-route assessment

1. **Count convention:** the shared draft currently says cap counts include
   the empty set and therefore gives boundary value two.  The exact recurrence
   and the geometry verifier use nonempty counts with boundary value one.
   Normalize the proof to the latter convention and add the empty subset once.
   This is a finite bookkeeping issue, not an asymptotic failure.
2. **The row constant survives:** `1/(2 ln 2)` is the correct base-2
   coefficient for the `2^m`-point full row.  The short inequality (8)--(10)
   is rigorous and avoids a fragile two-variable derivative calculation.
3. **But the row is not the best construction:** one central Pascal cell
   immediately improves the upper coefficient to
   `1-1/(4 ln 2)=0.639326...`, using only the already-audited cap recurrence
   and upper/lower-hull injection.
4. **Neither count can be sharpened at quadratic scale:** transversal caps give the
   matching lower bound (11)--(12).  Sharpening cap/cup counts, or improving
   the treatment of the `k=ell` case, cannot affect the leading term because
   the full-row leading term comes from the intermediate singleton product.
   For the cell, the cross-child cap/cup family attains (15).
5. **What a still stronger upper bound would require:** a different recursive
   order type or a nontrivial thinning in which the large cross-product
   families disappear while the point count retains exponent one.  Merely
   strengthening (1) is asymptotically powerless.
6. **Geometric dependency:** the asymptotic argument is complete conditional
   on the exact strong-gluing orientation and decomposition.  Those are the
   only genuinely geometric inputs; `dp_audit.py` intentionally does not
   certify them.
