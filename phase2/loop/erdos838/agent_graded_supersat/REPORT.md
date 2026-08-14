# Erdős 838: graded supersaturation and mean-size lane

**Date:** 2026-08-13
**Verdict:** one exact obstruction, one sharpened live target, and one new
full-strength reformulation.  No unrestricted lower-bound improvement is
claimed.

All logarithms are base two.  Write `v_k(P)` for the number of convex
`k`-subsets and `Z_P(z)=sum_k v_k(P)z^k`.

## 1. The graded reverse-product identity is exact

Put the points in increasing horizontal order.  If the chord `(i,j)` is the
root `e`, set

\[
T_e(z)=I+zE_{ji}.
\]

Order the roots by increasing slope and define

\[
A(z)=T_{e_M}(z)\cdots T_{e_1}(z),\qquad
B(z)=T_{e_1}(z)\cdots T_{e_M}(z).
\]

The row update is `row_j <- row_j + z row_i`.  Consequently, `A(z)_{t,s}`
is the generating polynomial for increasing-slope paths from `s` to `t`,
with one factor of `z` per edge; `B` counts decreasing-slope paths.  These
are the cups and caps with those two endpoints.  A cap and cup with common
endpoints have disjoint interiors and form one convex polygon.  Their total
edge count is the polygon's vertex count.  The identity paths on the matrix
diagonal have weight one and must be replaced by the `n` singletons of
weight `z`.  Thus

\[
\boxed{Z_P(z)=nz+\langle A(z),B(z)\rangle_F-n.}       \tag{1}
\]

`graded_trace.py` implements (1) over the integers.  Its independent
`T_(4,2)` check returns

```
(v_1,v_2,v_3,v_4)=(6,15,20,9),   sum v_k=50.
```

## 2. Exact graded recurrence for a vertical blow-up

For a template `S` of size `r`, define

\[
\begin{aligned}
A_S(x)&=\sum_{j\ge1}c_j(S)x^{j-1},\\
B_S(x)&=\sum_{j\ge1}u_j(S)x^{j-1},\\
D_S(x)&=\sum_{j\ge2}v_j(S)x^{j-2}.
\end{aligned}
\]

If `|Q|=n`, the vertex-graded version of the exact composition lemma is

\[
\begin{aligned}
C_{S[Q]}(z)&=C_Q(z)A_S(nz),\\
U_{S[Q]}(z)&=U_Q(z)B_S(nz),                         \tag{2}\\
Z_{S[Q]}(z)&=rZ_Q(z)+C_Q(z)U_Q(z)D_S(nz).
\end{aligned}
\]

The scripts `graded_balanced.py` and `graded_trace.py` independently verify
these formulas: one uses the recursive strong-glue classification and the
other uses the reverse matrix products.

## 3. The diagonal target has an exact fixed-template exponent

Fix `S`.  Let

\[
p=\max\{|K|-1:K\text{ is a cap of }S\},\qquad
q=\max\{|K|-1:K\text{ is a cup of }S\},
\]

and put `L=log r`.  Iterate `Q_0` a singleton and `Q_d=S[Q_(d-1)]`.
Let

\[
k_d=\left\lfloor\frac{Ld}{2}\right\rceil,
\]

so `|Q_d|=2^(2k_d+O(1))`.

### Theorem (fixed-template diagonal coefficient)

For every fixed template with `p,q>0`,

\[
\boxed{
\log v_{k_d}(Q_d)
=\left(2-\frac{L}{2(p+q)}+o(1)\right)k_d^2.}       \tag{3}
\]

### Proof

Iteration of the first formula in (2) gives

\[
C_{Q_d}(z)=z\prod_{s=0}^{d-1}A_S(r^sz).            \tag{4}
\]

Every size from one through the largest cap size occurs, by taking subsets
of a largest cap.  Therefore, for `0<=t<=pd`,

\[
\log c_{t+1}(Q_d)=L M_{p,d}(t)+O_S(d),             \tag{5}
\]

where

\[
M_{p,d}(t)=\max\left\{\sum_{s=0}^{d-1}sx_s:
0\le x_s\le p,\ \sum_sx_s=t\right\}.              \tag{6}
\]

Indeed, (4)'s coefficient is a sum over precisely these integer vectors;
all template coefficients and the number of vectors contribute only
`2^(O_S(d))`.  The maximizer fills the latest levels first.  Uniformly for
`t=theta*p*d+O(1)`,

\[
M_{p,d}(t)=pd^2\left(\theta-\frac{\theta^2}{2}\right)+O_S(d). \tag{7}
\]

The same statement holds for cups with `q` in place of `p`.

Unroll the last recurrence in (2).  A convex `k_d`-set created at level `s`
is a cap and cup in `Q_(s-1)`, plus a bounded number of macro vertices.
The `r^(d-s)` choice of the final containing block and all template
coefficients cost only `2^(O_S(d))`.  For fixed required cap/cup sizes the
weighted sums in (6) strictly improve as `s` increases, so the leading term
is created at `s=d`.  Concavity of (7) makes the optimal split proportional
to the capacities `p:q`.  With

\[
\theta=\frac{L}{2(p+q)},                            \tag{8}
\]

the two sides use respectively `theta*p*d+O(1)` and
`theta*q*d+O(1)` interior vertices.  The cup--cap theorem gives
`r<=binom(p+q,p)<=2^(p+q)`, so `theta<=1/2` and this split is feasible.
Equations (5)--(8) now give

\[
\log v_{k_d}(Q_d)
=L(p+q)d^2\left(\theta-\frac{\theta^2}{2}\right)+O_S(d).
\]

Dividing by `k_d^2=L^2d^2/4+O(d)` proves (3).  The same estimates are both
upper and lower bounds because all admissible sizes occur and the final
level supplies an explicit summand.  `square`

## 4. Consequence: the proposed `rho=2` target cannot solve #838

For the balanced Pascal template

\[
S_h=T_{2h-4,h-2},\quad
r_h={2h-4\choose h-2},\quad p=q=h-2.
\]

Stirling gives `log r_h=2(h-2)-O(log h)`.  Letting first the iteration depth
and then `h` tend to infinity in (3) yields

\[
\boxed{v_{k_d}(Q_d)=2^{(3/2+o(1))k_d^2},\qquad
|Q_d|=2^{2k_d+O(1)}.}                             \tag{9}
\]

Hence

\[
\mu_k(2^{2k+o(k)})\ge2^{(1+\eta-o(1))k^2}
\]

is **false for every `eta>1/2`**.  In particular the `eta=1` version that
would have yielded the full coefficient `1/2` is decisively killed by the
paper's actual upper construction.  At this scale the best possible fixed
gain is at most `eta=1/2`, which would improve the total lower coefficient
only to `3/8`.

This does **not** kill a smaller fixed gain.  No proof or counterexample was
found for `0<eta<=1/2`.  Formula (3) also shows that every fixed vertical
template has diagonal exponent at least `3/2`, since `L<=p+q`.  Balanced
Pascal templates attain the infimum.  Thus the construction evidence points
to the sharper incremental conjecture

\[
\mu_k(2^{2k+o(k)})\ge2^{(3/2-o(1))k^2},           \tag{10}
\]

but there is currently no unrestricted proof of (10).

Exact finite calculations from `graded_balanced.py` converge toward (3).
For example, the predicted fixed-template exponents for `h=6,8,10` are
`1.6169,1.5895,1.5734`; the exact small-depth coefficients fluctuate around
these values because `k_d` is rounded and the error is `O_h(d)`.

## 5. A stronger route: mean convex-subset size

Define

\[
\bar s(P)=\frac{Z'_P(1)}{Z_P(1)}.
\]

The following statement would resolve the full problem:

> **Mean-size target.** There is an absolute constant `C` such that every
> `N`-point set satisfies `bar s(P)>=log N-C`.

To see this, take an extremal `P` with `Z_P(1)=f(N)`.  Double-counting
deletions gives

\[
\sum_{p\in P}Z_{P-p}(1)
=\sum_K(N-|K|)=\bigl(N-\bar s(P)\bigr)f(N).
\]

Every deletion has at least `f(N-1)` convex subsets, and hence

\[
\frac{f(N)}{f(N-1)}\ge\frac{N}{N-\bar s(P)}.       \tag{11}
\]

Using `-log_2(1-x)>=x/ln 2`, summing (11), and inserting the mean-size
target gives

\[
\log f(N)\ge\frac12(\log N)^2-O(\log N).
\]

Together with the proved upper bound this solves #838.

### Exact fixed-template evidence

Differentiate (2) at `z=1`.  If `m_C=C'_Q(1)/C_Q(1)` and

\[
\alpha_A(n)=\frac{\sum(j-1)c_j(S)n^{j-1}}
                  {\sum c_j(S)n^{j-1}},
\]

then

\[
m_C(S[Q])=m_C(Q)+\alpha_A(n),                     \tag{12}
\]

and analogously for cups.  Since `alpha_A(r^s)=p+O_S(r^{-s})`, cap and cup
means in `Q_d` are `pd+O_S(1)` and `qd+O_S(1)`.  The last cross term in the
convex recurrence exponentially dominates the earlier terms, so

\[
\boxed{\bar s(Q_d)=(p+q)d+O_S(1)
\ge d\log r-O_S(1)=\log|Q_d|-O_S(1).}             \tag{13}
\]

The inequality uses `log r<=p+q`.  It is asymptotically sharp on the
balanced Pascal templates.  `graded_balanced.py` evaluates (12) and the
full differentiated convex recurrence exactly with integer arithmetic.

### Small and adversarial tests

The exhaustive reflection-order search in `../agent_reflection_gate/`
found the following minimum values of `bar s-log n` over **all** reduced
words through `n=6`:

| n | minimum deficit |
|---:|---:|
| 2 | +0.333333 |
| 3 | +0.129323 |
| 4 | 0 |
| 5 | -0.052697 |
| 6 | -0.130417 |

For `n=6`, the exact minimizing profile is `(6,15,20,3)`, so
`bar s=108/44=2.454545...`.  A rational fixed-`x` seven-point certificate
has profile `(7,21,35,9)` and deficit `-0.168466`.  A separate mean-deficit
anneal in this directory found a rational fixed-`x` eight-point certificate
with profile `(8,28,56,21,1)`, `bar s=321/114`, and deficit `-0.184211`.
The deficit therefore cannot be replaced by zero, but no growing negative
deficit was found.

The exact dyadic Horton family gives positive and rapidly growing slack:

| n | `bar s-log n` |
|---:|---:|
| 8 | +0.4023 |
| 16 | +0.9664 |
| 32 | +1.8087 |
| 64 | +2.9010 |
| 128 | +4.2349 |

These data support the `O(1)`-loss target but are not a proof.  Proving it
is essentially a common-endpoint alignment theorem in differential form;
the ordinary size-by-size double counts do not control the denominator in
`bar s`.

## 6. Recommended next move

1. Promote the mean-size target to the primary graded target.  It has exactly
   the strength needed for `1/2` and is sharp on the known construction.
2. Search for a one-chord or contiguous-cut inequality for the logarithmic
   derivatives of the two reverse products, not merely their values.
3. Keep (10) as an incremental target.  Any exponent above one improves the
   published lower bound, but the balanced construction caps this particular
   `rho=2` strategy at `3/2`.
4. When searching computationally, minimize `Z'(1)/Z(1)-log n` directly and
   require stretchability certificates.  The current worst certified value
   is only about `-0.1842`.

## 7. Reproduction

From this directory:

```
python3 -m py_compile graded_trace.py graded_balanced.py mean_size_probe.py
python3 graded_trace.py
python3 graded_balanced.py --h 6 8 10 --depth 1 2 4 6
python3 mean_size_probe.py --horton-level 1 2 3 4 5 6 7
```

The JSON files `mean_heuristic_n8.json` and `mean_heuristic_n10.json` are
annealing outputs.  Only the `n=8` file currently includes a rational
fixed-`x` realization; the larger uncertified reflection-order samples are
evidence only.
