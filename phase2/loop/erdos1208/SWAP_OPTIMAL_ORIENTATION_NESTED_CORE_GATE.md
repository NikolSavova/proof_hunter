# Optimal swap orientations and the nested-core gate

## 1. Outcome

This note replaces the opaque quadratic orientation cost in
`SWAP_CELL_DEGENERACY_CHARGE.md` by an exact nested family of mutually rich
endpoint cells.  It is a graph-theoretic reduction, not the final geometric
estimate.

Let `G=(V,E)` be a finite loopless multigraph; parallel edges are allowed.
Orient its edge copies, write `x_v=d^+(v)`, and choose an orientation
minimizing

\[
 \mathcal E_2(G)=\sum_{v\in V}x_v^2.                         \tag{1.1}
\]

For `t>=1`, put

\[
 U_t=\{v:x_v\ge t\},\qquad e_t=|E(G[U_t])|,                 \tag{1.2}
\]

where edge copies are counted with multiplicity.  Then

\[
 \boxed{
  \sum_{t\ge1}e_t\le \mathcal E_2(G)
  \le |E|+\sum_{t\ge1}e_t.}                                \tag{1.3}
\]

More precisely,

\[
 \mathcal E_2(G)=\sum_{t\ge1}e_t+B,                        \tag{1.4}
\]

where `B` is the number of oriented edge copies `u->v` for which
`x_u=x_v+1`.  Thus `0<=B<=|E|`.

Applied to the swap multigraph, (1.3) makes the preferred size-biased
orientation theorem equivalent, up to the harmless diagonal mass, to a
single nested-core packing estimate.  It also explains exactly why stars
are cheap: in an optimal orientation their high-load leaves have no edges
among themselves, so they contribute nothing to `sum_t e_t`.

## 2. Proof of the exact identity

Fix an optimal orientation.  If one edge copy is oriented `u->v`, reversing
only that copy changes the energy by

\[
 (x_u-1)^2+(x_v+1)^2-x_u^2-x_v^2
 =2(x_v-x_u+1).                                             \tag{2.1}
\]

Optimality therefore implies

\[
 x_u\le x_v+1                                               \tag{2.2}
\]

on every oriented edge.  Consequently

\[
 \min(x_u,x_v)\le x_u\le \min(x_u,x_v)+1,                  \tag{2.3}
\]

and the upper inequality is strict exactly when `x_u=x_v+1`.

Every edge oriented out of `u` contributes `x_u` once to the following
sum, hence

\[
 \sum_{u\to v}x_u=\sum_u x_u d^+(u)=\sum_u x_u^2.           \tag{2.4}
\]

Summing (2.3) over edge copies proves

\[
 \mathcal E_2(G)
 =\sum_{\{u,v\}\in E}\min(x_u,x_v)+B.                     \tag{2.5}
\]

Finally, layer cake gives

\[
 \min(x_u,x_v)
 =\sum_{t\ge1}{\bf1}_{u,v\in U_t}.                         \tag{2.6}
\]

Summing (2.6) over `E` proves (1.4), and hence (1.3).

## 3. A mass-bearing core from any failure

Let `Delta=max_v x_v` and

\[
 J=\lceil\log_2(\Delta+1)\rceil.
\]

Partition the positive levels into dyadic blocks.  Since `e_t` decreases
with `t`,

\[
 \sum_{t\ge1}e_t
 \le\sum_{0\le j<J}2^j e_{2^j}.                             \tag{3.1}
\]

Therefore some dyadic `t=2^j` satisfies

\[
 \boxed{t e_t\ge {1\over J}\sum_{s\ge1}e_s.}               \tag{3.2}
\]

Moreover `t|U_t|<=sum_v x_v=|E|`, so this same level obeys

\[
 {e_t\over |U_t|}
 \ge {t e_t\over |E|}
 \ge {\sum_s e_s\over J|E|}.                               \tag{3.3}
\]

Thus excessive quadratic orientation energy does not merely expose one
arbitrarily small maximum-degeneracy witness.  It exposes a dyadic induced
core that is simultaneously dense and mass-bearing through the product
`t e_t`.  This is the correct inverse object for a size-biased theorem.

## 4. Application to the adaptive swap graph

Use the notation of `ADAPTIVE_CROSS_PAIR_D2_CHARGE_GATE.md`.  Thus

\[
 D=A-A,\quad N=|D|,\quad S=|D+D|,\quad K=S/N,
\]

and the adaptive off-diagonal mass is `O_K`.  The swap multigraph has

\[
 |E(G_{\rm sw})|={1\over2}\mathcal O_K.                     \tag{4.1}
\]

An orientation gives the exact charge moment

\[
 \mathcal Q_{\rm or}=2\sum_v(d^+(v))^2.                    \tag{4.2}
\]

Choose a quadratic-optimal orientation and its level sets `U_t`.  Equations
(1.3), (4.1), and (4.2) give

\[
 \boxed{
  2\sum_{t\ge1}|E(G_{\rm sw}[U_t])|
  \le \mathcal Q_{\rm or}
  \le \mathcal O_K+
       2\sum_{t\ge1}|E(G_{\rm sw}[U_t])|.}                 \tag{4.3}
\]

Hence the geometric estimate

\[
 \boxed{
  \sum_{t\ge1}|E(G_{\rm sw}[U_t])|
  \le K N^{o(1)}|E(G_{\rm sw})|}                           \tag{4.4}
\]

is exponent-equivalent to the preferred orientation gate

\[
 \mathcal Q_{\rm or}\le K N^{o(1)}\mathcal O_K.            \tag{4.5}
\]

The established adaptive-tail reduction then gives

\[
 k\le m^{2/3+o(1)},
\]

and therefore `F_2(n)<=n^(1/3+o(1))` for the square grid.

## 5. The exact geometric survivor

A swap edge arising from a fibre joins

\[
 C(q,p)=(b,\ell),\qquad
 C(p,q)=(b+t,\ell+(I+J)t),\qquad t=p-q.                     \tag{5.1}
\]

Both endpoints have the component invariant

\[
 z=\ell-(I+J)b.                                             \tag{5.2}
\]

Thus `E(G_sw[U_t])` counts records for which **both** swapped `D^2` cells
are popular in the globally optimal charge.  One-sided stars have vanished.
What remains is a nested collection of mutually rich, endpoint-realizable
affine shifts inside the invariant components (5.2).

For a fixed `epsilon>0`, a polynomial failure of (4.4) yields through
(3.2)--(3.3) a dyadic level satisfying

\[
 t e_t\gg {K N^\epsilon |E|\over\log N},
 \qquad
 {e_t\over|U_t|}\gg {K N^\epsilon\over\log N}.             \tag{5.3}
\]

The remaining endpoint-rich core theorem can now be stated without an
overstrong maximum-load hypothesis:

> A genuine complete-difference swap graph of a distance-Sidon point set
> has no dyadic optimal-load core satisfying (5.3).

A proof must use the canonical endpoint lift of every nonzero member of
`D=A-A`.  Abstract radial transversals satisfy the affine identities but
violate the desired estimate, so radial uniqueness and graph density alone
cannot prove it.  The intended dichotomy is that a core satisfying (5.3)
either concentrates in an already-paid one-dimensional/low-index lattice
branch, or forces two distinct endpoint differences to have equal Euclidean
norm.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_optimal_orientation_nested_core.py
```

The verifier exhausts every orientation of several loopless multigraphs,
including stars and parallel bundles, recomputes the exact optimum, checks
(2.2), (1.4), and the dyadic extraction, and then repeats the audit on
seeded random multigraphs.  The proof above is exact and independent of the
finite checks.

