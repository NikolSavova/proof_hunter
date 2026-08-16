# Cubic `C_4` supersaturation in a two-dimensional dominance cell

**Date:** 2026-08-14.  This is a proved local theorem, not a proof of
Erdos 838.  Its relevance is that a fixed-root planar repair cell has the
form below: the two rooted boundary chains are compatible exactly when two
opposite tangent inequalities hold.

Let `X,Y` be finite labelled point sets in the plane and let `G` be the
strict dominance graph

\[
             xy\in E(G)\quad\Longleftrightarrow\quad
             y_1<x_1\quad\hbox{and}\quad y_2<x_2 .          \tag{1}
\]

Write `a=|X|`, `b=|Y|`, `m=|E(G)|`, and
`s=ceil(log_2(a+b))+1`.

> **Theorem.**  The ordered homomorphic four-cycle count satisfies
> \[
> \boxed{
>  \operatorname{hom}(C_4,G)
>       \ge {m^3\over 2ab s^3}.}                            \tag{2}
> \]
> Repeated vertices on either side are allowed.

The logarithmic power is deliberately inessential.  At coefficient scale,
(2) says that a dominance repair support cannot exhibit the projective-plane
`2/3` obstruction: if both vertex supports and the decoded face-pair pool
are bounded by `V(P)2^{o(r^2)}`, then

\[
                         m\le V(P)^{4/3}2^{o(r^2)},          \tag{3}
\]

or `log V(P)>=(3/4-o(1))log m`.

## 1. Ferrers cells

First suppose the first-coordinate inequality in (1) is automatic: every
point of `Y` lies to the left of every point of `X`.  Sorting `Y` by its
second coordinate makes every neighborhood an initial segment.  If the
left degrees are `d_1,...,d_a`, then

\[
 C:=\operatorname{hom}(C_4,G)
   =\sum_{i,j}\min(d_i,d_j)^2 .                              \tag{4}
\]

Put `D=d_I/b` for uniform `I in [a]`, `mu=E D=m/(ab)`, and
`F(t)=Pr(D>=t)`.  The layer-cake identity gives

\[
 {C\over a^2b^2}=E\min(D,D')^2
                 =\int_0^1 2tF(t)^2\,dt .                  \tag{5}
\]

Since `F<=1`,

\[
 \int_{\mu/2}^1F(t)dt\ge\mu/2.
\]

Cauchy--Schwarz on this interval yields

\[
 \int_0^1 2tF(t)^2dt
 \ge {\mu^2\over2\log(2/\mu)}
 \ge {\mu^3\over2},                                      \tag{6}
\]

where the last step uses `mu log(2/mu)<=1` for `0<mu<=1`.
Consequently every Ferrers cell satisfies

\[
                         C\ge {m^3\over2ab}.                 \tag{7}
\]

## 2. Dyadic first-coordinate decomposition

Sort `X union Y` by first coordinate (break ties consistently) and build a
balanced binary interval tree.  Assign an edge `xy` to the unique lowest
tree node whose left child contains `y` and whose right child contains `x`.
At a fixed node the first-coordinate inequality is automatic, so its edge
set is a Ferrers cell after sorting by second coordinate.

There are at most `s` depths.  At one fixed depth the node vertex sets are
pairwise disjoint.  Choose a depth carrying at least `m/s` edges, and write
the cell parameters there as `m_j,a_j,b_j`.  Equation (7) and Holder give

\[
\begin{split}
 \operatorname{hom}(C_4,G)
 &\ge\sum_j {m_j^3\over2a_jb_j},\\
 \left(\sum_jm_j\right)^3
 &\le\left(\sum_j{m_j^3\over a_jb_j}\right)
       \left(\sum_ja_j\right)\left(\sum_jb_j\right)
 \le ab\sum_j{m_j^3\over a_jb_j}.
\end{split}                                                \tag{8}
\]

Since `sum_jm_j>=m/s`, (8) proves (2).

## 3. Exact scope

For a fixed directed root chord, an upper rooted convex chain and a lower
rooted convex chain glue precisely when their two endpoint tangent ranks
satisfy a southeast-dominance relation.  Hence (2) applies inside every
fixed recoverable tangent cell.

It does **not** yet prove the unrestricted theorem.  A multilevel repair
history can switch its root edge and erase the cell identifier from one
of the two eventual output faces.  Summing (2) over cells is harmless only
when both output-face families recover their cells with subquadratic
overlap (the recoverable-cell Cauchy telescope in `agent_acp_proof`).  That
global label-faithful statement remains the exact gap.

## 4. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_root_followup/verify_dominance_c4.py
```

The checker exhausts all two-dimensional dominance graphs with up to three
vertices on each side obtained from distinct integer coordinates, checks
the Ferrers inequality for every degree sequence through size eight, and
stress-tests (2) on random labelled point sets.
