# The role-projected completion reservoir

## 1. Outcome

The sparse completion-link theorem still records its cross support in a
copy of `D` attached to each base corner.  This note removes that base
coordinate.  Every role-adapted link cell injects, at its fixed base, into
one of two global projections of the fourth completion corner.  The
combined projected reservoir is smaller than the full completion reservoir
by the adaptive popularity factor `K`.

Write

\[
 \mathcal V_K=\{(r,A,B):r\in\mathcal P_K,
     A,A+r,B,B+Jr\in D\},
 \qquad W_\square=|\mathcal V_K|.                 \tag{1.1}
\]

Define its two coordinate projections

\[
\begin{aligned}
 \mathcal T_K^\parallel
   &=\{(r,A):r\in\mathcal P_K,\ A,A+r\in D\},\\
 \mathcal T_K^\perp
   &=\{(r,B):r\in\mathcal P_K,\ B,B+Jr\in D\}.
\end{aligned}                                     \tag{1.2}
\]

Since every `r in mathcal P_K` satisfies
`R_D(r)>K` and `R_D(Jr)>K`,

\[
\boxed{
 |\mathcal T_K^\parallel|
   =\sum_{r\in\mathcal P_K}R_D(r)\le {W_\square\over K},
 \qquad
 |\mathcal T_K^\perp|
   =\sum_{r\in\mathcal P_K}R_D(Jr)\le {W_\square\over K}.}   \tag{1.3}
\]

The role decides which projection retains the physical edge.

* If the physical label is the moving `W_q`, a cell `(u,q)` maps to

  \[
   \eta_\perp(u,q)=(r,B)=(q-u,W_q)\in\mathcal T_K^\perp.       \tag{1.4}
  \]

  Here `B=W_q` is the physical directed edge.

* If the physical label is the moving `V_p=X+p`, after the opposite-corner
  pivot a cell `(u,p)` maps to

  \[
   \eta_\parallel(u,p)=(r,A)=(p-u,X+u)
      \in\mathcal T_K^\parallel.                              \tag{1.5}
  \]

  Here `A+r=X+p=V_p` is the physical directed edge.

Both maps are injective at a fixed base.  Thus all four endpoint roles use
a global key space of size at most `2W_square/K`, with no completion-centre
coordinate left in the key.

This gives an exact low-reuse charge.  For any family `mathscr E` of
role-adapted link occurrences, let `mu(eta)` be the number of occurrences
having projected key `eta`.  For every `R>=1`,

\[
\boxed{
 |\{e\in\mathscr E:\mu(\eta(e))<R\}|
 < {2R\over K}W_\square.}                         \tag{1.6}
\]

If the group load of every occurrence is below `2L`, its size-biased
contribution is therefore below

\[
 \boxed{{4LR\over K}W_\square.}                   \tag{1.7}
\]

The only survivor is high reuse of a physical half-completion.  Section 3
shows that this is exactly a two-level grid: either many complementary
starts are used, or one full completion vertex is itself reused many times.

## 2. Exact role projections

Use the `W`-moving normal form at a base

\[
 v=(p,X,\ell),\qquad Z_0=\ell+Lp,qquad
 W_q=Z_0-Lq.                                      \tag{2.1}
\]

For a link cell put `r=q-u` and `B=W_q`.  The cross condition is

\[
 Z_0-q-Ju=B+Jr\in D,                              \tag{2.2}
\]

while `B in D`; hence `(r,B) in mathcal T_K^perp`.  At the fixed base,
`B=Z_0-Lq` recovers `q`, and then `u=q-r`.  This proves the injectivity of
(1.4).  The full fourth corner is

\[
 \kappa=(r,A,B)=(q-u,X+u,W_q)\in\mathcal V_K.     \tag{2.3}
\]

For the `V`-moving role, base at the opposite corner `(q,X,W)` and write

\[
 R_0=W+Lq,\qquad \ell_p=R_0-Lp.                  \tag{2.4}
\]

Put `r=p-u` and `A=X+u`.  Then

\[
 A+r=X+p=V_p\in D,                                \tag{2.5}
\]

so `(r,A) in mathcal T_K^parallel`.  At the fixed base, `A` recovers
`u=A-X` and then `p=r+u`, proving (1.5).  Its full fourth corner is

\[
 \kappa=(r,A,B)=(p-u,X+u,\ell_p)\in\mathcal V_K.  \tag{2.6}
\]

The head/tail orientation of the physical edge changes neither projection.
It only chooses one of its two endpoint labels, so (1.3)--(1.7) cover all
four oriented roles with the displayed factor two for the two projection
types.

## 3. The exact high-reuse grid

Let `nu(r,A,B)` count occurrences which lift to the full fourth corner
`(r,A,B)`.  The two projected multiplicities are exactly

\[
\begin{aligned}
 \mu_\perp(r,B)
   &=\sum_{A:\ A,A+r\in D}\nu(r,A,B),\\
 \mu_\parallel(r,A)
   &=\sum_{B:\ B,B+Jr\in D}\nu(r,A,B).
\end{aligned}                                     \tag{3.1}
\]

Consequently

\[
\boxed{
 \mu_\perp(r,B)<S R_D(r),\quad
 \mu_\parallel(r,A)<S R_D(Jr)}                  \tag{3.2}
\]

whenever every full corner above the given projected key has reuse below
`S`.  Equivalently, a projected key of load at least the corresponding
right-hand side forces a full completion vertex of reuse at least `S`.

Thus the remaining Carleson theorem has no hidden local branch.  Low
projected-key reuse receives the factor-`K` charge (1.7).  High projected
reuse is a literal row or column of the Cartesian completion fibre

\[
 (D\cap(D-r))\times(D\cap(D-Jr)),                 \tag{3.3}
\]

and excessive concentration inside that row or column forces high reuse of
one full vertex of `mathcal V_K`.  The unresolved input is now a weighted
packing theorem for these two-sided high-reuse grids, retaining the metric
key and the physical endpoint.

## 4. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_role_projected_completion_reservoir.py
```

The verifier checks both role inversions on random integral cells, verifies
the exact projection cardinalities on genuine distance-Sidon difference
sets, and exhausts the low-reuse and two-level grid inequalities on random
finite multiplicity tables.
