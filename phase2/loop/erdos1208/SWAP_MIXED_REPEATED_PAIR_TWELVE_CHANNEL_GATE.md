# Twelve-channel normal form for a repeated mixed projected-key pair

## 1. Outcome

The exact mixed group-overlap stress shows that the two projected-key roles
cannot be separated.  This note retains them jointly and passes from one
common group to a pair of distinct common groups.

Fix a moving-`W` projected key `eta_W=(r,B)` and a moving-`V` projected key
`eta_V=(rho,A)`.  Use the constants

\[
 C=A+\rho,\quad K_0=B+Jr,
\]

and `alpha,delta,chi,gamma,phi` from
`SWAP_PROJECTED_KEY_MIXED_CODEGREE_MIN_GATE.md`.  One common endpoint group
is uniquely represented by `(e,z,c)`, with

\[
 t=L^{-1}(B-e),                                    \tag{1.1}
\]

and the following twelve vectors in `D`:

\[
\begin{array}{lll}
 e,&z,&K_0-t,\\
 z-t,&Jz+\alpha,&e+z+\delta,\\
 c,&c+Jz+\chi,&c+t,\\
 e-c+\gamma,&e+z-c+\phi,&e+LC-Lc.
\end{array}                                        \tag{1.2}
\]

Take two distinct common groups `(e_i,z_i,c_i)`.  Put

\[
 h=e_1-e_2,\qquad s=z_1-z_2,\qquad a=c_1-c_2,
 \qquad \lambda=L^{-1}h.                           \tag{1.3}
\]

Integrality of both values in (1.1) makes `lambda` integral.  The twelve
paired differences in (1.2) are exactly

\[
\boxed{
 h,\ s,\ \lambda,\ s+\lambda,\ Js,\ h+s,\
 a,\ a+Js,\ a-\lambda,\ h-a,\ h+s-a,\ h-La.}      \tag{1.4}
\]

This is the correct joint repeated-edge cell.  In particular, marginalizing
the `V` or `W` role destroys six coupled translated pairs and creates the
huge false physical-bundle energies measured in the companion barrier.

## 2. Eight injective recovery triples

Write

\[
 R(v)=|D\cap(D-v)|.                                 \tag{2.1}
\]

For a fixed admissible nonzero triple `(h,s,a)`, put `lambda=L^{-1}h` and
define

\[
\begin{aligned}
 \Upsilon(h,s,a)=\min\{\;&R(h)R(s)R(a),
 R(\lambda)R(s)R(a),\\
 &R(h)R(Js)R(a+Js),
 R(h)R(s)R(h-a),\\
 &R(h)R(s)R(h-La),
 R(a)R(a+Js)R(a-\lambda),\\
 &R(h-a)R(h+s-a)R(a),\\
 &R(h-a)R(h+s-a)R(h-La)\}.                       \tag{2.2}
\end{aligned}
\]

Each product comes from an injective projection of a group `(e,z,c)` onto
three of the vectors in (1.2):

\[
\begin{array}{c|ccc}
1&e&z&c\\
2&K_0-t&z&c\\
3&e&Jz+\alpha&c+Jz+\chi\\
4&e&z&e-c+\gamma\\
5&e&z&e+LC-Lc\\
6&c&c+Jz+\chi&c+t\\
7&e-c+\gamma&e+z-c+\phi&c\\
8&e-c+\gamma&e+z-c+\phi&e+LC-Lc.
\end{array}                                        \tag{2.3}
\]

For example, row 6 first recovers `c`, then `z`, then `t`, and finally
`e=B-Lt`.  In row 8 put `U=e-c`; the first two entries recover `U,z`, while
the last gives

\[
 Jc=U+LC-(e+LC-Lc),                                \tag{2.4}
\]

and hence recovers `c,e`.

Let `n_eta(h,s,a)` be the number of canonically ordered pairs of distinct
common groups for the fixed mixed key pair `eta=(eta_W,eta_V)` having
difference triple `(h,s,a)`.  Counting the three translated pairs in any
row of (2.3) gives

\[
\boxed{n_\eta(h,s,a)\le\Upsilon(h,s,a).}            \tag{2.5}
\]

Therefore

\[
 {c(\eta_W,\eta_V)\choose2}
 \le\sum_{\substack{(h,s,a)\ne(0,0,0)\\h\in L\mathbb Z^2}}
 \Upsilon(h,s,a),                                  \tag{2.6}
\]

with all key-specific support and adaptive-popular conditions available for
retention inside the sum.

## 3. Group-pair disintegration

The displacement triple is intrinsic to the two endpoint groups, not to
the chosen projected keys.  Indeed a group is `(c,e,u)` and, for fixed
keys, `z=K_0+Ju`.  Hence

\[
 h=e_1-e_2,\qquad s=J(u_1-u_2),\qquad a=c_1-c_2. \tag{3.1}
\]

In particular, every common mixed key pair of the same two groups lies in
the same `(h,s,a)` cell.  If

\[
 a_{GH}=|V_G\cap V_H|,\qquad b_{GH}=|W_G\cap W_H|,
\]

then the repeated mixed-pair energy has the simultaneous exact forms

\[
 \boxed{
 C_{VW}=\sum_{G<H}a_{GH}b_{GH}
       =\sum_{\eta_W,\eta_V}{c(\eta_W,\eta_V)\choose2}.} \tag{3.2}
\]

Thus (2.5) may be summed by displacement cells without duplicating a
group pair across different cells.  This is the useful localization.
It does not by itself justify replacing the occupied key support by the
full ambient set of keys.

## 4. Why this is stronger than the one-group minimum

The five-channel one-group theorem bounds the number of choices of `c`
after `(e,z)` are fixed.  Formula (1.4) instead controls simultaneous reuse
of the *same* mixed key pair by two groups.  It adds the group displacement
`(h,s,a)` and couples both projected roles through `lambda=L^{-1}h`, `Js`,
and `La`.

The target repeated mixed-pair energy is exactly

\[
 C_{VW}=\sum_{\eta_W,\eta_V}{c(\eta_W,\eta_V)\choose2}. \tag{4.1}
\]

The remaining theorem is a support-sensitive summation of (2.5) over
occupied projected-key pairs.  A uniform summation of (2.6) for every key
pair would repeat its ambient boundary term and is not proposed.  The
required Carleson step must retain at least one of the twelve affine starts,
the physical endpoint orientation, and the four adaptive-popular corners.

The decisive gain is conceptual and exact: the false separate-side energies
have been removed, and no local group multiplicity remains after the
difference triple and one recovery row are fixed.

## 5. Exact stress and the summation barrier

On transformed Costas sizes `29,31,37`, respectively, the exact rows are

\[
\begin{array}{c|r|r|r|r|r}
k&C_{VW}&\#(G,H)&\#(h,s,a)&
 \max n_\eta(h,s,a)&\sum_{\rm occupied}\Upsilon\\ \hline
29&7724&7108&466&4&290091145355\\
31&10658&7932&467&5&395266391216\\
37&8014&7742&588&2&1027343639776
\end{array}                                               \tag{5.1}
\]

Here `#(G,H)` counts group pairs carrying at least one common mixed key
pair.  The true cell loads are almost simple, while the sum of the local
overlap-product envelope is larger by seven to eight orders.  Therefore
the uniform sum of (2.6) is decisively dead.  The remaining estimate must
retain the occupied key support or the group-pair endpoint realization.

There is also a large coordinate diagonal.  At sizes `29,31`, the branch
`h=a=0` carries `4857/7724` and `5058/10658` of the collision.  It has the
exact third-order parallel-fibre formula proved in
`SWAP_MIXED_SAME_CENTRE_TRIPLE_INTERSECTION_GATE.md`.  The remaining
non-axis cells are the genuine three-parameter Carleson survivor.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_mixed_repeated_pair_twelve_channel.py
```

The verifier checks the twelve differences and all eight inverses on
50,000 random integral configurations.  It also exhausts finite `D`-boxes,
enumerates every valid common group for random fixed keys, and checks all
eight overlap-product bounds (2.5) cell by cell.
