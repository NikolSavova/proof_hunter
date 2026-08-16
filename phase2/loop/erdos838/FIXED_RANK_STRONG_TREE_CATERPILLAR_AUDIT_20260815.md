# Fixed-rank strong trees and plane caterpillars

**Date:** 2026-08-15.  This note preserves a useful prior-art connection and
records exactly why it does not, by itself, close the growing-rank theorem.
All logarithms are base two.

## Result of the audit

An ordered binary strong-decomposition tree has three exact rank
polynomials:

\[
\begin{aligned}
C_T(z)&=C_A(z)(1+|B|z)+C_B(z),\\
U_T(z)&=U_A(z)+U_B(z)(1+|A|z),\\
V_T(z)&=V_A(z)+V_B(z)+C_A(z)U_B(z)
\end{aligned}                                                     \tag{1}
\]

at a seam $T=A\prec B$.  Consequently:

* a cap or cup is a **plane rooted caterpillar with a prescribed monotone
  spine direction**;
* an ordinary crossing face consists of a left monotone rooted caterpillar
  and a right monotone rooted caterpillar;
* equivalently, its plane spine has at most one turn.

This is an exact reformulation, not a lower bound: its three recursive
counting equations are precisely (1).

There is a closely related published theorem for **unordered** rooted binary
caterpillars.  Dossou-Olory proves that if $R_k(T)$ counts $k$-leaf subsets
whose suppressed rooted tree is the binary caterpillar $F_k^2$, then, for
every binary tree with $n$ leaves,

\[
 R_k(T)\ge b_k n^k-{n^{k-1}\over(k-1)!},\qquad
 b_k={1\over2}\prod_{j=1}^{k-1}(2^j-1)^{-1}.                 \tag{2}
\]

For fixed $k$ this yields the sharp minimum asymptotic density

\[
 k!b_k={k!\over2}\prod_{j=1}^{k-1}(2^j-1)^{-1}.             \tag{3}
\]

Source: Audace A. V. Dossou-Olory,
[The minimum asymptotic density of binary caterpillars](https://arxiv.org/abs/1804.05731),
Theorem 2 and its proof.

If (2) were uniform with a relative error $2^{o(k^2)}$ at $n=4^k$, its main
term would have

\[
 \log(b_k n^k)={3\over2}k^2+O(k),                            \tag{4}
\]

exactly the desired strong-tree diagonal.  This explains why the constant
$3/2$ keeps appearing in the profile calculations.

## Why the published theorem does not close P1b

There are two independent losses.

### 1. The finite-size error is nonuniform

At $n=4^k$, the error term in (2) has logarithm

\[
 2k(k-1)-\log((k-1)!)=2k^2-k\log k+O(k),                    \tag{5}
\]

which is larger than the main exponent $3k^2/2+O(k)$.  The lower bound is
therefore vacuous in the canonical growing-rank window.  The paper's sharp
statement is an $n\to\infty$ theorem with $k$ fixed; the present problem has
$k=(1/2)\log n$.

The large additive error is not accidental in the proof.  A homogeneous
induction

\[
 R_k(T)\ge b_kn^k-e_kn^{k-1}                                \tag{6}
\]

through an arbitrarily unbalanced root split forces
$e_k/e_{k-1}\ge1/(k-1)$, yielding the coefficient
$e_k=1/(k-1)!$ in (2).  Unbalanced trees themselves have many caterpillars;
the loss comes from asking one scalar induction to handle balanced and comb
branches simultaneously.  The proved comb-or-seam theorem is exactly the
right preliminary split, but a uniform post-split estimate is still open.

### 2. Forgetting the plane order loses the geometric predicate

The recurrence for unordered rooted caterpillars is, for $k\ge3$,

\[
 R_k(T)=R_k(A)+R_k(B)+|A|R_{k-1}(B)+|B|R_{k-1}(A).           \tag{7}
\]

It accepts every left/right itinerary of the caterpillar spine because
children may be swapped under rooted-tree isomorphism.  A cap in the strong
geometry accepts only the monotone itinerary in (1), and an ordinary face
accepts only a one-turn itinerary.  The verifier finds strict finite trees
for which the number of unordered caterpillar leaf sets exceeds the number
of ordinary faces.  Thus (2) cannot simply be relabelled as a convex-face
bound.

## Exact surviving statement

The strong-tree subproblem P1b can now be stated without cap/cup
terminology:

> For every ordered full binary tree with $n=4^k$ leaves, prove that at
> least $2^{(3/2-o(1))k^2}$ of its $k$-leaf subsets induce a plane
> caterpillar whose spine has at most one turn.

The diffuse heavy-path theorem already proves this when one orientation has
no sibling larger than its average $1/(k-1)$ share.  The survivor has a
macroscopic seam and is exactly the orientation-sensitive, growing-rank
version absent from (2)--(3).

This is useful narrowing, but it is not claimed as a new coefficient gain.
It also supplies a stop rule: fixed-$k$ inducibility, unordered tree shape,
or an $O(n^{k-1})$ error without its $k$-dependence cannot close P1b.

## Verification

Run

```text
python3 phase2/loop/erdos838/verify_strong_tree_caterpillar_audit.py
```

The checker enumerates every ordered full binary tree through nine leaves,
verifies (1) and (7), checks the finite inequality (2) exactly, verifies that
strong faces inject into unrooted caterpillar copies, exhibits strict loss
from forgetting plane orientation, and confirms that the error exponent in
(2) dominates its main term at the canonical scales tested.
