# Strong-tree amortization audit

All logarithms are base two.  This note proves a coefficient-`1/3` lower
bound for every strong-decomposition tree, audits the endpoint-max
reduction, and isolates the obstruction to coefficient `1/2`.

## 1. The endpoint enumerator lies below `CU`

At a strong glue `T=A prec B`, with sizes `a,b`, write `C,U,W` for the
nonempty cap, cup, and convex counts and `E` for endpoint-rooted
caterpillars.  The recurrences are

```
C_T=C_B+(b+1)C_A,       U_T=U_A+(a+1)U_B,
W_T=W_A+W_B+C_AU_B,
E_T=(b+1)E_A+(a+1)E_B-ab.
```

Then universally

```
E_T <= C_T U_T <= W_T^2.                          (1)
```

For the first inequality, induct on the tree.  Substituting
`E_A<=C_AU_A` and `E_B<=C_BU_B`, the difference between `C_TU_T` and the
resulting upper bound for `E_T` is

```
C_B U_A +(a+1)(b+1)C_A U_B +ab >=0.
```

The second inequality is combinatorial: every cap and every cup is a convex
set, so `C_T<=W_T` and `U_T<=W_T`.  Together with the sharp endpoint
caterpillar lemma, (1) recovers coefficient `1/4`, but not more.

## 2. The local imbalance game

Put

```
r_X=(log C_X+log U_X)/2,
d_X=(log C_X-log U_X)/2.
```

At one glue, the available terms imply

```
log W_T >= max(r_A+|d_A|, r_B+|d_B|,
              r_A+r_B+d_A-d_B).                  (2)
```

For arbitrary real `d_A,d_B`, the right side of (2) is at least

```
max(r_A,r_B, 2(r_A+r_B)/3).                       (3)
```

Indeed, if all three entries in (2) are at most `M`, then
`d_A>=-(M-r_A)` and `d_B<=M-r_B`; the cross entry is consequently at least
`2(r_A+r_B)-2M`, forcing `M>=2(r_A+r_B)/3`.

The proved product theorem gives

```
r_X >= (1/4)(log |X|)^2-(1/2)log |X|.             (4)
```

Thus a balanced glue already gives coefficient `1/3` from (2)--(4), with
no directional assumption.  This is a genuine improvement over taking
`sqrt(CU)` at that node.

## 3. A stopping-time theorem: coefficient `1/3`

The unbalanced-node gap can in fact be removed by stopping only after a
polynomial scale drop.

> **Theorem.** Every ordered full binary strong-decomposition tree with `n`
> leaves satisfies
>
> ```
> log W(T) >= (1/3)(log n)^2-O(log n log log n).    (5)
> ```

Here is a proof with explicit slack.  Put `L=log n` and `lambda=log L`, and
assume `L` is larger than an absolute constant.  Starting at the root,
repeatedly follow a larger child.  Write `m_i` for the current subtree size,
`m_{i+1}` for the followed-child size, and `s_i=m_i-m_{i+1}` for its sibling.
Stop at the first `t` for which

```
m_t < n/L^4.                                      (6)
```

Such a time exists because the path ends at a leaf.  There are two cases.

### Case 1: a logarithmically large sibling

Suppose that before the stopping time some

```
s_i >= m_i/L^2.                                  (7)
```

At that node both children are large.  Since the followed child is a larger
child,

```
log m_{i+1} >= L-4 lambda-1,
log s_i     >= L-6 lambda.                       (8)
```

Apply (3) at this node and (4) to its two children.  For `L` sufficiently
large,

```
log W(T)
 >= (2/3)(r_{m_{i+1}}+r_{s_i})
 >= (1/3)L^2-5L lambda.                           (9)
```

For completeness, substituting (8) in (4) gives the sharper intermediate
lower bound

```
(1/6)((L-4lambda-1)^2+(L-6lambda)^2)-2L/3,
```

which implies (9).

### Case 2: every sibling is tiny

Otherwise `s_i/m_i<1/L^2` for every `i<t`.  Since

```
log(m_i/m_{i+1})=-log(1-s_i/m_i) < 2/L^2         (10)
```

for `L>=2` (use `-log_2(1-z)<=2z` for `0<=z<=1/4`), while
(6) gives

```
sum_{i<t} log(m_i/m_{i+1}) > 4 lambda,
```

we have

```
t > 2L^2 lambda.                                  (11)
```

Fix one leaf in every discarded sibling and one terminal leaf below the
stopping point.  Color a level according to whether its sibling is the left
or the right child of the path node.  At least `t/2` levels have one color.
For every subset of those levels, take their fixed sibling leaves together
with the terminal leaf.  After unary suppression the selected set is a pure
left comb or a pure right comb, according to the common color.  All these
sets are distinct and are counted by `W`.  Consequently

```
log W(T) >= t/2 > L^2 lambda,                     (12)
```

which is stronger than (5).

The two cases prove (5).  Notice that no induction on `W`, no scalar
Bellman inequality, and no comparison of `E/W` is used.  The only global
input is the already proved product estimate (4); the directional loss is
handled either by the exact minimax (3) or by the long-spine majority
argument.

The constant `1/3` is the limit of this information set.  At a balanced
node with `r_A=r_B=r`, taking `d_A=-r/3` and `d_B=r/3` makes all three terms
in (2) equal `4r/3`.  Since (4) supplies `r` with coefficient `1/4`, a
strict improvement beyond `1/3` needs structural information excluding or
charging this anti-aligned state inside the two children.

## 4. Exact endpoint-max reduction

For an ordered point/tree set, let `x(s)` be the number of caps whose
leftmost point is `s`, including the singleton, and let `y(t)` be the number
of cups whose rightmost point is `t`.  Put

```
X=max_s x(s),   Y=max_t y(t),
M=max_{s<t} c(s,t)u(s,t).
```

At `T=A prec B`, the exact max-product recurrences are

```
X_T=max((b+1)X_A,X_B),
Y_T=max(Y_A,(a+1)Y_B),
M_T=max(M_A,M_B,X_A Y_B),                         (13)
```

with leaf state `(X,Y,M)=(1,1,0)`.  To verify the crossing term, for
`s in A,t in B` one has exactly

```
c_T(s,t)=x_A(s),   u_T(s,t)=y_B(t).
```

The endpoint identity gives

```
W(T)=n+sum_{s<t}c(s,t)u(s,t),
```

and hence, for `n>=2`,

```
M <= W <= n+binom(n,2)M <= n^2 M.                (14)
```

Thus total convex count and the single best endpoint product differ by at
most `2 log n` logarithmically.  Also `C<=nX` and `U<=nY`; combining this
with the product theorem yields

```
log(XY) >= (1/2)(log n)^2-3log n.                (15)
```

Equations (13)--(15) turn the matching `1/2` problem into a particularly
clean weighted one-turn path theorem.

There is a useful quantitative form of the remaining obstruction.  Write
`x=log X,y=log Y` and fix a threshold `H`.  If two children satisfy

```
x_A+y_A >= H+epsilon,
x_B+y_B >= H+epsilon,
```

but their forward cross is unpaid, `x_A+y_B<H`, then

```
y_A-y_B>epsilon,   x_B-x_A>epsilon.              (16)
```

Moreover the reverse maximum inherited by the parent satisfies

```
x_T+y_T >= x_B+y_A
          >= x_A+y_A+x_B+y_B-(x_A+y_B)
          > H+2epsilon.                          (17)
```

So every failed forward alignment creates an endpoint-product surplus and
forces the maxima to come from opposite children.  A proof at coefficient
`1/2` should amortize the surplus in (17) across a stopping tree.  The point
still needing care is an unbalanced chain: the same high `x` can persist
down a right spine while successive left siblings independently carry the
high `y`, so (16) does not telescope along a single coordinate without also
using the long-spine pure-comb count.

## 5. Can the `1/3` minimax state recur?

Equality in the one-node game suggests a cup-heavy child with normalized
rates

```
(log X,log Y,log M)/(log n)^2 = (1/6,1/3,1/3)
```

and its mirror.  Putting the cup-heavy child on the left and the cap-heavy
child on the right makes the forward cross have rate `1/3`, and the parent
has `(1/3,1/3,1/3)`.  This is a valid tropical one-node state, but the
imbalanced children themselves must be realized recursively.

They cannot come from a stationary Pascal template.  For the full Pascal
tree `T(m,i)`, with `r=binom(m,i)` leaves and `h=log r`, iterating leaf
substitution gives the limiting endpoint rates

```
log X/(log n)^2 -> i/(2h),
log Y/(log n)^2 -> (m-i)/(2h),
log M/(log n)^2 -> m/(2h).                        (18)
```

The first two statements follow directly from the max recurrences: one
substitution level adds respectively `i log n` and `(m-i)log n`, up to
lower-order terms.  The crossing recurrence then gives the sum rate for
`M`.  In particular

```
m/(2 log binom(m,i)) >= 1/2,                      (19)
```

with a strict constant gap for a fixed noncentral bias.  Alternating a
biased template with its mirror balances `X,Y` but leaves the same `M` rate.

More generally, a fixed strong template with endpoint-degree increments
`p,q` has stationary `X,Y` rates `p/(2log r),q/(2log r)` and its crossing
terms force `M` rate at least `(p+q)/(2log r)`.  The cap--cup extremal bound
gives `log r<=p+q+O(1)`, so this route cannot realize a rate below `1/2`.
For a fixed proportional imbalance the sharper binomial/entropy form gives
a strict surplus over `1/2`.

Thus the putative sharp `1/3` children are not self-similar constructions;
realizing them would require genuinely nonstationary templates or
macroscopic scale jumps.  Proving that such repeated jumps also spend the
entropy surplus is essentially the remaining route from (5) to `1/2`.
