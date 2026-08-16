# Strong trees at fixed rank: diffuse comb or near-full seam

**Date:** 2026-08-15. All logarithms are base two. This is a theorem about
ordered binary strong-decomposition trees; it is not yet an unrestricted
point-set theorem.

## Verdict

Let `T` be an ordered strong tree with `N` leaves, and fix `k>=2`. Follow a
larger child from the root to a leaf. The discarded sibling subtrees split
into two classes according to whether they lie to the right or left of the
path. Then one of the following holds.

1. `T` has at least

   \[
             \left({N-1\over2(k-1)}\right)^{k-1}             \tag{1}
   \]

   convex `k`-subsets, all lying in one literal cap or cup comb; or
2. some strong seam `A prec B` in `T` has

   \[
       |A|,|B|>{N-1\over2(k-1)}.                              \tag{2}
   \]

At the canonical fixed-size scale `N=4^k`, alternative 1 gives

\[
             \log v_k(T)\ge 2k^2-O(k\log k),                  \tag{3}
\]

which is stronger than the desired `3k^2/2-o(k^2)` diagonal bound.
Therefore every strong-tree survivor below that diagonal bound contains a
single near-full seam: both children and the seam itself have logarithmic
size `2k-O(log k)`.

This removes arbitrary diffuse/caterpillar structure from the strong-tree
fixed-rank problem. The remaining gate is genuinely the graded cap/cup
alignment across one near-full seam. The already-proved ungraded all-tree
theorem resolves its total mass but does not locate that mass at rank `k`.

## 1. Exact comb bank

At a strong seam `A prec B`, every cap in `A` remains a cap after adjoining
zero or one point of `B`. Dually, every cup in `B` remains a cup after
adjoining zero or one point of `A`.

Follow any root-to-leaf path ending at leaf `x`. Let

\[
       R_1,\ldots,R_p
\]

be the right siblings at nodes where the path enters the left child, and
let `r_i=|R_i|`. Choosing `t` of these sibling blocks, one label in each,
and the fixed terminal leaf `x` gives a cap of rank `t+1`. Every output
recovers the chosen blocks and labels. Hence

\[
       c_{t+1}(T)\ge e_t(r_1,\ldots,r_p),                    \tag{4}
\]

where `e_t` is the elementary symmetric polynomial. For the left siblings
at nodes where the path enters the right child, the reflected statement is

\[
       u_{t+1}(T)\ge e_t(l_1,\ldots,l_q).                    \tag{5}
\]

Both are literal load-one banks.

## 2. Diffuse elementary-symmetric lower bound

We use the following elementary lemma.

> **Lemma.** If `s_i>=0`, `S=sum_i s_i`, and
> `max_i s_i<=S/t`, then
> \[
>                         e_t(s_1,\ldots,s_q)\ge(S/t)^t.      \tag{6}
> \]

**Proof.** Draw `t` indices independently with probabilities `s_i/S`.
Conditioned on the first `j` indices being distinct, their total probability
mass is at most `j/t`. Thus the probability that all `t` draws are distinct
is at least

\[
       \prod_{j=0}^{t-1}(1-j/t)={t!\over t^t}.                \tag{7}
\]

On the other hand this probability is exactly `t! e_t/S^t`. Rearranging
proves (6). `square`

## 3. Heavy-path dichotomy

Now follow a larger child at every node. The discarded siblings partition
all leaves except the terminal leaf, so their sizes sum to `N-1`. Let `S_R`
and `S_L` be the sums in the two orientation classes. One satisfies

\[
                         S:=\max(S_R,S_L)\ge(N-1)/2.          \tag{8}
\]

Put `t=k-1`. If every sibling in this majority-mass class has size at most
`S/t`, apply (4) or (5) and Lemma (6):

\[
 v_k(T)\ge(S/t)^t
          \ge\left({N-1\over2(k-1)}\right)^{k-1}.             \tag{9}
\]

Otherwise one sibling in that class has size greater than `S/t`. At its
node, the path child is at least as large because the path follows a larger
child. Thus both children satisfy (2). This proves the dichotomy.

For `N=4^k`, taking logarithms in (9) gives

\[
 (k-1)\{\log(N-1)-1-\log(k-1)\}
 =2k^2-O(k\log k),                                          \tag{10}
\]

which proves (3).

## 4. Exact remaining strong-tree gate

It is now enough to treat a seam `P=A prec B` with

\[
 |P|\le4^k,qquad |A|,|B|\ge {4^k-1\over2(k-1)}.             \tag{11}
\]

The graded recurrence is exact:

\[
\begin{aligned}
 C_P(z)&=C_A(z)(1+|B|z)+C_B(z),\\
 U_P(z)&=U_A(z)+U_B(z)(1+|A|z),\\
 V_P(z)&=V_A(z)+V_B(z)+C_A(z)U_B(z).                         \tag{12}
\end{aligned}
\]

The children in (11) are both at the full logarithmic scale
`2k-O(log k)`. Standard Erdős--Szekeres supersaturation supplies the
baseline `2^{k^2-O(k log k)}` internal rank-`k` mass in each child. To gain
a fixed quadratic exponent one must now prove that the forward coefficient

\[
                    [z^k]C_A(z)U_B(z)                        \tag{13}
\]

is large, or charge its anti-alignment to an equally large inherited graded
profile. This is the first open lemma after the diffuse branch; it is not a
global decoder or arbitrary-child reformulation.

## 5. Verification

Run

```text
python3 phase2/loop/erdos838/verify_strong_tree_fixed_rank_comb_gate.py
```

The verifier checks (6) on all bounded integer vectors in its census,
enumerates every ordered binary tree through ten leaves, recomputes the
exact graded strong-glue recurrences, and verifies the literal comb banks
and the dichotomy on every heavy path.
