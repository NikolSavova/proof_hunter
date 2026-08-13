# Erdős 838: full-solution attack

> Status, 2026-08-13. The new upper theorem is proved in
> proof_central.md. The original limit problem is **not** proved here.
> This note reduces the missing lower bound to an exact weighted
> cap/cup-multiplicity statement, records the \(1/4\) barrier for all
> black-box Erdős--Szekeres double counts, and gives falsification data for
> the most obvious extremal conjectures.

All logarithms are base \(2\), except \(\ln\).

## 1. What a full solution would now look like

Write

\[
 \kappa=1-\frac1{4\ln2}=0.639326239777\ldots .
\]

The central Pascal-cell construction proves unconditionally that

\[
 \limsup_{N\to\infty}
 \frac{\log f(N)}{(\log N)^2}\leq\kappa.             \tag{1}
\]

The cleanest possible completion is therefore the following multiplicity
theorem.

> **Endpoint multiplicity conjecture.** Every \(N\)-point set \(P\) in
> general position satisfies
> \[
>  V(P)\geq
>  2^{\,(\kappa-o(1))(\log N)^2},                   \tag{EM}
> \]
> uniformly over \(P\).

Here \(V(P)\) counts all convex-position subsets; including or excluding
sets of size at most two has no effect on the displayed exponent. Equation
(EM), together with (1), would prove that the limit in Erdős 838 exists and
equals \(\kappa\).

This is a target, not yet a theorem. It may be false if a better construction
exists. Two independent searches are therefore needed in parallel:

1. prove (EM), or a weaker improvement over \(1/4\);
2. optimize the upper construction beyond Pascal cells.

The exact reformulation below makes the first lane finite and algebraic.

## 2. Exact endpoint factorization

After a small rotation, label the points
\(p_1,\ldots,p_N\) by increasing \(x\)-coordinate. For \(s<t\), let

* \(c(s,t)\) be the number of caps whose leftmost and rightmost points are
  \(p_s,p_t\);
* \(u(s,t)\) be the analogous number of cups.

The two-point set \(\{p_s,p_t\}\) is counted once in each number.

### Proposition 1 (exact identity)

\[
 \boxed{\quad
 V(P)=1+N+\sum_{1\leq s<t\leq N}c(s,t)u(s,t).
 \quad}                                             \tag{2}
\]

**Proof.** A convex subset of size at least two has unique leftmost and
rightmost points. Its upper hull is a cap and its lower hull is a cup with
those same endpoints. Conversely, take any cap and cup with common
endpoints. Every interior point of the cap is strictly on one side of the
endpoint line, and every interior point of the cup is strictly on the other,
so their interiors are disjoint. The monotone-chain hull algorithm retains
all their points, and their union is in convex position. These maps are
inverse. The terms \(1+N\) account for the empty set and the singletons.
\(\square\)

This identity matters more than the coarser inequality
\(V(P)\leq\#\mathrm{caps}\,\#\mathrm{cups}\) used for the upper construction:
the full lower problem is precisely an **endpoint alignment** problem.

### A finite dynamic program

Let \(\chi(i,j,k)\in\{-,+\}\) be the orientation of
\((p_i,p_j,p_k)\), for \(i<j<k\). Fix \(s\). Let \(C_s(i,j)\) count cap
paths starting at \(s\) whose last two vertices are \(i,j\), and define
\(U_s(i,j)\) similarly. Then

\[
\begin{aligned}
C_s(s,j)&=U_s(s,j)=1,\\
C_s(i,j)&=\sum_{\substack{s\leq h<i\\\chi(h,i,j)=-}}C_s(h,i),\\
U_s(i,j)&=\sum_{\substack{s\leq h<i\\\chi(h,i,j)=+}}U_s(h,i)
                                                        \tag{3}
\end{aligned}
\]

for \(s<i<j\), and

\[
c(s,t)=\sum_{i=s}^{t-1}C_s(i,t),\qquad
u(s,t)=\sum_{i=s}^{t-1}U_s(i,t).                    \tag{4}
\]

To justify the local recurrence, a cap is exactly an \(x\)-ordered chain
whose consecutive slopes strictly decrease; a cup has consecutive slopes
strictly increase. Thus (2)--(4) compute \(V(P)\) from the orientation signs
alone in \(O(N^4)\) elementary integer operations. The script
order_type_audit.py independently verifies (2) against the published
convex-\(k\)-gon profiles for the extremal order types through \(N=9\), after
enumerating every realizable order type at each of those sizes.

## 3. Why the known lower bound stops at \(1/4\)

Suk's theorem, sharpened in its error term by Holmsen--Mojarrad--Pach--Tardos,
states

\[
 ES(k)=2^{k+o(k)}.                                  \tag{5}
\]

Choose \(t=ES(k)\). Every \(t\)-subset of an \(N\)-point set contains a
convex \(k\)-subset. Counting pairs \((T,K)\), where \(K\subseteq T\),
gives

\[
 \#\{\text{convex }k\text{-subsets}\}
 \geq\frac{\binom Nt}{\binom{N-k}{t-k}}
 =\frac{\binom Nk}{\binom tk}.                      \tag{6}
\]

Put \(t=N^{\alpha+o(1)}\). Equation (5) permits
\(k=(\alpha+o(1))\log N\), and (6) gives

\[
 \log f(N)\geq
 \bigl(\alpha(1-\alpha)-o(1)\bigr)(\log N)^2.
\]

The maximum is \(1/4\), at \(\alpha=1/2\).

This is not merely a poor choice of scale. Any argument that treats (5) as
a black-box statement saying only “each \(t\)-set contains one witness” has
the same variational term \(\alpha(1-\alpha)\). Even recursively inserting
a lower bound \(f(t)\geq2^{(c-o(1))(\log t)^2}\) does not amplify \(c\).
After discarding subset sizes below
\((c\alpha-o(1))\log N\) and double-counting the rest, the best exponent
obtainable is

\[
 c\alpha^2+c\alpha(1-\alpha)=c\alpha\leq c.         \tag{7}
\]

Thus matching (1) requires a multiplicity or stability input that remembers
how cap and cup paths share endpoints. More averaging cannot do it.

## 4. The precise missing lemma

The orientations of a planar point set form a rank-three realizable
signotope: for every \(a<b<c<d\), the sequence

\[
 \chi(a,b,c),\ \chi(a,b,d),\ \chi(a,c,d),\ \chi(b,c,d)
\]

has at most one sign change. Baek and Balko use exactly this language in
their 2025 work on split polygons. Their key distinction is also exactly
ours: a split polygon has cap and cup chains sharing one endpoint, whereas a
convex polygon has chains sharing both endpoints.

In terms of (3)--(4), the desired theorem is the weighted signotope
inequality

\[
 \sum_{s<t}c(s,t)u(s,t)
 \geq
 2^{\,(\kappa-o(1))(\log N)^2}.                    \tag{8}
\]

The most promising proof architecture is:

1. **Weighted down-set labels.** Replace the longest-path pair used in the
   cap--cup and split-polygon theorems by the full path-count vectors in
   (3). The one-change axiom should impose nesting or majorization on these
   vectors.
2. **Endpoint-alignment lemma.** Prove that cap mass and cup mass cannot be
   asymptotically disjoint over their left endpoints. A loss
   \(2^{O(\log N\log\log N)}\) is harmless; a loss
   \(2^{\Theta((\log N)^2)}\) is not.
3. **Entropy optimization.** Once alignment is available, the same
   binomial entropy integral as in the Pascal-cell upper bound should yield
   \(A(1/2)+A(1/2)=\kappa\).

This is the point at which a proof currently stops. One cannot expect an
argument using only unconstrained two-colorings: Baek--Balko exhibit abstract
colorings where even the corresponding sharp weak-polygon existence
statement fails. The one-change/signotope constraint, or still more of
realizability, must be used essentially.

## 5. Construction-side control experiment

For a strongly decomposable set \(P=A\prec B\), let \(C,U,W\) count its
nonempty caps, cups, and convex subsets. The exact recurrences are

\[
\begin{aligned}
C(P)&=C(B)+(1+|B|)C(A),\\
U(P)&=U(A)+(1+|A|)U(B),\\
W(P)&=W(A)+W(B)+C(A)U(B).                          \tag{9}
\end{aligned}
\]

The last identity follows because every spanning convex subset is uniquely a
nonempty cap in \(A\) united with a nonempty cup in \(B\). It reduces
optimization over every binary decomposable construction to a Pareto dynamic
program in the state \((C,U,W)\).

The exact minima of \(W+1\) found by decomposable_dp.py are:

| \(N\) | 6 | 7 | 8 | 9 | 12 | 16 | 20 | 21 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| decomposable minimum | 46 | 76 | 121 | 185 | 543 | 1758 | 4821 | 6092 |
| normalized rate | .827 | .793 | .769 | .750 | .707 | .674 | .655 | .652 |

The displayed rate drifts toward \(\kappa\), and iterating every fixed
template tested through size \(21\) is worse than the nonstationary central
Pascal cell. This is only weak evidence: at these sizes compulsory triples
still dominate, and an untested nonstationary tree could behave differently.
The controlled target is therefore:

> **Decomposable extremality conjecture.**
> \(W(P)\geq
> 2^{(\kappa-o(1))(\log |P|)^2}\) for every decomposable \(P\).

A proof would establish that the central Pascal cell is asymptotically
optimal among the decomposable class, which contains the classical
Erdős--Szekeres and Horton-type constructions. It would not by itself prove
(EM), because
general point sets need not be decomposable.

## 6. Complete small-order-type falsification

Using Aichholzer's complete database of realizable order types and its
convex-\(k\)-gon profiles gives:

| \(N\) | exact minimum \(V(P)\), empty included | decomposable minimum |
|---:|---:|---:|
| 6 | 45 | 46 |
| 7 | 73 | 76 |
| 8 | 114 | 121 |
| 9 | 169 | 185 |

Therefore the tempting finite claim “a Pascal/decomposable set minimizes
the number of convex subsets” is already false at \(N=6\). The order types
minimizing total cap/cup mass are also different from those minimizing
\(V(P)\). This is why (8), not a separate lower bound on the total number of
caps and cups, is the correct invariant.

The database is not copied into this repository. To reproduce the census,
download matching otypesNN and kgonsNN files from the Point Set Order Type
Database and run, for example,

    python3 order_type_audit.py 9 --data-dir /path/to/database

## 7. Concrete next attacks

In order of expected information gain:

1. Encode rank-three signotopes and (3)--(4) in SAT/CP-SAT for
   \(N=10,\ldots,14\). Optimize (2), inspect minimizers, and test whether
   realizability appears to matter.
2. Extract a weighted analogue of the down-set injection in Baek--Balko
   Lemma 10. The first target should be any universal coefficient strictly
   greater than \(1/4\), not immediately \(\kappa\).
3. Prove or kill the decomposable extremality conjecture by finding an
   inductive potential for (9). This is the cleanest controlled model for
   the entropy calculation.
4. Run the generalized blow-up constructions of Baek--Balko through the
   endpoint DP. They generalize the classical extremal examples and are the
   most credible place for an upper coefficient below \(\kappa\).

## 8. Honest conclusion

We now have a complete proof of the strict upper improvement (1), an exact
algebraic identity for the full problem, and a sharply identified missing
lemma. We do **not** yet have a proof of the Erdős--Hammer limit conjecture.
The next genuine mathematical step is a weighted endpoint-alignment theorem
for realizable signotopes; without it, claiming the value \(\kappa\) would be
premature.

## References

- A. Suk, *On the Erdős--Szekeres convex polygon problem*,
  <https://arxiv.org/abs/1604.08657>.
- A. F. Holmsen, H. N. Mojarrad, J. Pach, G. Tardos,
  *Two extensions of the Erdős--Szekeres problem*,
  <https://arxiv.org/abs/1710.11415>.
- J. Baek, M. Balko, *The Erdős--Szekeres Conjecture Revisited*,
  <https://doi.org/10.4230/LIPIcs.SoCG.2025.13>.
- Point Set Order Type Database,
  <https://mathbases.org/d/order-types>.
