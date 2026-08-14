# Erdős 838: tangent-pruning and collision audit

> **Post-audit correction (2026-08-13).**  Section 5's counterfactual `1/3`
> arithmetic additionally uses
> `log C(I)+log U(I)>=(1/2-o(1))log^2|I|` for arbitrary point sets.
> That product inequality is not currently proved; it is a central missing
> directional-mass statement.  Hypothetical polynomial `(C)` and `(T)` alone
> would therefore not establish `1/3`.  The exact counterfamily and kernel
> computations are unchanged.

**Date:** 2026-08-13
**Verdict:** the polynomial collision lemma **(C) is false**, by an exact
rational stretchable family with an exponentially small normalized collision
ratio.  The polynomial tangent lemma **(T) remains open**; its lossless form is
already false on seven integral points.  Therefore this lane yields **no new
unconditional coefficient**: the rigorous lower coefficient remains `1/4`.
If both polynomial statements and the additional product input used in
Section 5 had been true, the arithmetic would have given exactly `1/3`, not
anything stronger.

The independent evaluator and searches are in `attack_search.py`.  The exact
certificate checker is `verify_certificates.py`, which writes
`verified_certificates.json`.

## 1. Independent reconstruction of the cut kernel

Let the points be indexed in increasing horizontal order, and cut at

\[
L=\{0,\ldots,m-1\},\qquad R=\{m,\ldots,n-1\}.
\]

For a cross edge `e=(i,j)` of slope `q_e`, define the four boundary vectors

\[
\begin{array}{ll}
 a_e(s)=\#\{\hbox{cup paths }s\leadsto i\hbox{ in }L:
                    \hbox{ all slopes}<q_e\},&
 r_e(t)=\#\{\hbox{cup paths }j\leadsto t\hbox{ in }R:
                    \hbox{ all slopes}>q_e\},\\
 b_e(s)=\#\{\hbox{cap paths }s\leadsto i\hbox{ in }L:
                    \hbox{ all slopes}>q_e\},&
 d_e(t)=\#\{\hbox{cap paths }j\leadsto t\hbox{ in }R:
                    \hbox{ all slopes}<q_e\}.
\end{array}
\]

An increasing-horizontal path from `L` to `R` has a unique cross edge.
Splitting there gives, independently of any decomposition hypothesis,

\[
 U_{t,s}=\sum_e a_e(s)r_e(t),\qquad
 C_{t,s}=\sum_f b_f(s)d_f(t).
\]

Thus, with

\[
 K_L(e,f)=\sum_s a_e(s)b_f(s),\qquad
 K_R(e,f)=\sum_t r_e(t)d_f(t),
\]

the crossing trace is exactly

\[
 \boxed{X_{L\mid R}=\sum_{e,f}K_L(e,f)K_R(e,f).}       \tag{1}
\]

This also reconstructs why the same-bridge diagonal is trivial: a nonidentity
cup prefix below `q_e` and cap prefix above `q_e` with the same endpoints
would force their common chord slope to lie both below and above `q_e`.
Hence `K_L(e,e)=K_R(e,e)=1`.

There is a useful aggregate form not used by the original checker.  Delete
all internal-`R` edges and let `u^-_s,c^-_s` be the total cup and cap path
counts from `s` in `L` to `R` in the remaining graph.  Such a path has its
cross edge last, so

\[
 u^-_s=\sum_ea_e(s),\qquad c^-_s=\sum_fb_f(s),\qquad
 \boxed{S_L=\sum_{s\in L}u^-_sc^-_s.}              \tag{2}
\]

Deleting internal-`L` edges gives the reflected identity for `S_R`.  This
computes `X,S_L,S_R` in `O(n^3)` arithmetic operations without forming the
`|L|^2|R|^2` table.  `verify_certificates.py` cross-checks (2) against the
entrywise two-bridge kernel through `n=16`.

## 2. An exponential stretchable counterexample to (C)

Take `n=2m`, choose an integer `M>2n`, and put

\[
 p_i=(i,(-1)^iM^{n-i})\quad(0\le i\le n-3),\qquad
 p_{n-2}=(n-2,0),\quad p_{n-1}=(n-1,0).             \tag{3}
\]

These are exact integral coordinates.  For `i<j<k`,

\[
 \det(p_j-p_i,p_k-p_i)
 =(k-j)y_i-(k-i)y_j+(j-i)y_k.
\]

The first term has magnitude at least `M^(n-i)`, while the two later terms
have total magnitude less than `2n M^(n-i-1)`.  Therefore

\[
 \chi(i,j,k)=(-1)^i.                                \tag{4}
\]

In particular, a path is a cup exactly when every selected vertex except its
last two has even index; it is a cap exactly when all those vertices have odd
index.

Let the cut be the balanced cut after `m`.  If a cross path starts at an even
index, its cap count is exactly one (the direct edge); if it starts at an odd
index, its cup count is exactly one.  Every crossing endpoint product is
therefore just one oriented path count.  Encoding a cup by its last two
vertices and the subset of earlier even vertices, and similarly for caps,
gives the crude but sufficient bound

\[
 X_{L\mid R}\le 2n^2 2^m.                           \tag{5}
\]

The boundary masses are much larger.

* For `S_L`, fix start `0`, left penultimate vertex `m-1`, and an arbitrary
  cross endpoint.  Every subset of the even vertices in
  `\{1,\ldots,m-2\}` gives a cup, while every direct cross edge gives a cap.
  Hence

  \[
  S_L\ge m^2 2^{\lfloor(m-2)/2\rfloor}
      \ge m^2 2^{m/2-2}.                           \tag{6}
  \]

* For `S_R`, fix terminal vertices `n-2,n-1`.  Choose an even source in `L`
  and an arbitrary subset of the even signed vertices in `R` to get a cup;
  choose an odd source and an arbitrary subset of the odd signed vertices to
  get a cap.  If `p,q` are the counts of even and odd sources in `L`, then

  \[
  S_R\ge pq\,2^{m-2}\ge m^2 2^{m-5}.              \tag{7}
  \]

Since `E=|L||R|=m^2`, (5)--(7) imply

\[
 \boxed{
 \frac{X_{L\mid R}E^2}{S_LS_R}
 \le 1024m^2 2^{-m/2}.}                            \tag{8}
\]

The right side is smaller than `n^{-K}` for every fixed `K` once `n` is
large.  Thus there is no constant hidden in `n^{-O(1)}` for which

\[
 X_{L\mid R}\ge n^{-O(1)}\frac{S_LS_R}{E^2}
\]

holds universally.  This refutes (C), exponentially strongly, inside exact
rational realizable orders.

This failure does **not** refute RPR: (5) is only an upper bound, and the exact
crossing trace on this family is already exponential in `n`.  The bad
normalized collision occurs in a regime with vastly more convex subsets than
the quasipolynomial target needs.  A viable replacement would have to be a
capped dichotomy: either `X` already exceeds the target, or the normalized
collision is inverse-polynomial.

## 3. Status of tangent mass (T)

The polynomial-loss claim

\[
 S_L\ge n^{-O(1)}|R|^2\min\{C(L),U(L)\},\qquad
 S_R\ge n^{-O(1)}|L|^2\min\{C(R),U(R)\}             \tag{T}
\]

was not proved or refuted.  The alternating family above satisfies the left
inequality with normalized ratio exactly one in every tested even size and
has a growing right ratio, so it isolates collision rather than tangent loss.

The lossless strengthening is false.  On the seven integral points

```text
(i,y_i),  y = [3,2,5,4,6,1,0],   cut after i=2,
```

the right child has `(C_R,U_R)=(12,12)` and `S_R=98`, so

\[
 \frac{S_R}{|L|^2\min(C_R,U_R)}=\frac{98}{9\cdot12}=\frac{49}{54}<1. \tag{9}
\]

This is the smallest failure found in the exhaustive fixed-`x`, permutation-
height subfamily: the lossless tangent ratio stayed at least one through
`n=6` and first fell to `49/54` at `n=7`.

No decaying tangent family was found.  Two thousand random integral trials at
each size gave exact record left ratios `5/6,111/125,247/279` at
`n=8,10,12`; the corresponding right records were `5/6,451/500,17/18`.
These computations are evidence only.  The bounded-fibre tangent-pruning
problem therefore remains a meaningful lemma, but proving it cannot rescue
the proposed route without replacing (C).

## 4. Small stretchable-order search

`attack_search.py exhaustive-permutations n` exhausts all configurations
`x_i=i` with the `y_i` a permutation of `0,...,n-1`, rejecting collinear
instances.  This is a strict stretchable subfamily, not all order types.

| `n` | general-position instances | min collision ratio | min left T ratio | min right T ratio |
|---:|---:|---:|---:|---:|
| 4 | 18 | `32/39` | `1` | `1` |
| 5 | 56 | `24/31` | `1` | `1` |
| 6 | 272 | `945/1426` | `1` | `1` |
| 7 | 1000 | `92/149` | `1` | `49/54` |

The exact minimizers and all summary values are saved in
`permutation_exhaustive_n4.json` through `permutation_exhaustive_n7.json`.
The random rational certificates are the `random_tangent-*.json` files.

## 5. Exponent arithmetic

For completeness, suppose counterfactually that both (C) and (T) held with
fixed polynomial losses.  Let `h=n/2`, `mu=log_2 V(P)`, and use the standard
child product bound

\[
 \log C(I)+\log U(I)\ge
 F:=\tfrac12(\log h)^2-O(\log n).
\]

Since every cap and cup is a convex subset, `C(I),U(I)<=V(P)<=2^mu`, whence

\[
 \log\min(C(I),U(I))\ge F-\mu.
\]

The two tangent inequalities would give

\[
 \log S_L,\log S_R\ge 2\log h+F-\mu-O(\log n).
\]

As `E=h^2`, collision would then give

\[
 \mu\ge\log X
 \ge\log S_L+\log S_R-2\log E-O(\log n)
 \ge2F-2\mu-O(\log n).
\]

Therefore

\[
 3\mu\ge(\log n)^2-O(\log n),\qquad
 \mu\ge\tfrac13(\log n)^2-O(\log n).              \tag{10}
\]

The cancellation and factor of three are exact.  These two one-cut lemmas
could not yield a coefficient stronger than `1/3` without a stronger input.
Because (C) is false, (10) is conditional only.  The present rigorous
unrestricted coefficient is still `1/4`.

More generally, if collision loses `alpha (log n)^2+o(log^2 n)` bits, the
same calculation yields only `(1-alpha)/3`.  An inverse-polynomial collision
loss is precisely why the proposed proof needed `alpha=0`.

## 6. Reproduction and crisp verdict

Run

```bash
python3 phase2/loop/erdos838/agent_tangent_pruning/verify_certificates.py
python3 phase2/loop/erdos838/agent_tangent_pruning/attack_search.py \
  alternating --max-n 30
```

The verifier checks (3)--(8), recomputes the exact seven-point tangent
certificate, and cross-checks the fast aggregate kernel against the original
entrywise kernel.

**Final verdict:** discard standalone (C).  Keep (T) as an open auxiliary
lemma, but redirect collision work to a capped/small-`X` dichotomy.  No
coefficient above `1/4` follows from this lane as it stands; `1/3` was the
correct conditional coefficient and is invalidated by the counterexample to
(C).
