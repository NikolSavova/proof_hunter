# Exact counterexample to hull-rooted and onion-rooted amortization

**Date:** 2026-08-14

**Verdict:** both proposed induction lemmas are false, even for an explicit
mirror-decomposable planar configuration.  There is a 131-point rational
configuration with triangular outer hull for which every hull vertex fails

\[
 2Z_{P-e}(1/2)+|P|R_e(1/2)\leq4R_e(1),                    \tag{RA}
\]

and the whole outer layer fails

\[
 hZ_I(1/2)+|P|\bigl(Z_P(1/2)-Z_I(1/2)\bigr)
 \leq2\bigl(Z_P(1)-Z_I(1)\bigr).                          \tag{ORA}
\]

Here `I=P-hull(P)` and `h=|hull(P)|`.  Thus neither existential
hull-vertex induction nor onion-layer induction can prove HW2.

## 1. The recursively glued core

Let `Q_0` be a singleton and recursively set

\[
 Q_d=Q_{d-1}\prec Q_{d-1},\qquad N_d=|Q_d|=2^d,
\]

using the rational strong glue already verified in
`agent_geometry/audit_geometry.py`.  The coordinates are strictly increasing
in both coordinates.  Let `C_d(z),U_d(z),W_d(z)` count nonempty caps, cups,
and convex subsets, with weight `z` per selected point.  The strong-glue
classification gives the exact recurrences

\[
\begin{aligned}
 C_d(z)&=C_{d-1}(z)(2+N_{d-1}z),\\
 U_d(z)&=U_{d-1}(z)(2+N_{d-1}z),\\
 W_d(z)&=2W_{d-1}(z)+C_{d-1}(z)U_{d-1}(z),                 \tag{1}
\end{aligned}
\]

starting from `C_0=U_0=W_0=z`.  The last identity is exact: a crossing
convex face is uniquely a nonempty cap in the left child together with a
nonempty cup in the right child.

Consequently `log C_d(1)=d^2/2+O(d)`, while
`log(1+W_d(1/2))=d^2+O(d)`.  The half-weight mass of the core is the square,
at leading exponential order, of either one-sided chain count.

## 2. A skinny triangular wrapper

Normalize `Q_d` into `[0,1]^2`, and let `mu>0` be its least pair slope.
For a sufficiently large rational `L`, add

\[
 \ell_+=(-L-1,2),\qquad \ell_-=(-L,-1),\qquad r=(L,1/2).
                                                                  \tag{2}
\]

The triangle contains the unit square strictly.  Taking, for example,
`L>4/mu+10`, all slopes from an outer point to a core point have absolute
value less than `mu`.  Hence for core points `q_i<q_j`,

\[
 \chi(\ell_+,q_i,q_j)=\chi(\ell_-,q_i,q_j)=+,
 \qquad \chi(q_i,q_j,r)=-.                                  \tag{3}
\]

The displayed rational choice is in general position; the verifier checks
every determinant exactly for `d=7`.

The signs (3) have a decisive hereditary consequence.

* If a convex face contains either left hull point, its core intersection
  is a cup.
* If it contains the right hull point, its core intersection is a cap.
* If it contains hull points of both types, its core intersection is both a
  cap and a cup, hence has at most two points.

For the first claim, if `a<b<c` in the core intersection had
`chi(a,b,c)=-`, then the four signs in (3) put `b` strictly inside
`conv{ell,a,c}`.  The right-hand claim is the reflected argument.  Deleting
the other selected outer points justifies applying these one-root statements.

Write

\[
 X_N=1+N+\binom N2,
\]

the number of core subsets of size at most two.  If `L` denotes the family
of convex faces meeting the outer triangle, the seven possible nonempty
outer subsets now give

\[
 |L|\leq 3(1+U_d(1))+(1+C_d(1))+3X_{N_d}.                   \tag{4}
\]

For a left root and for the right root, respectively,

\[
 R_{\ell}(1)\leq2(1+U_d(1))+2X_{N_d},\qquad
 R_r(1)\leq1+C_d(1)+3X_{N_d}.                              \tag{5}
\]

## 3. The exact 131-point failure

At `d=7`, the core has `N=128` points and the parent has 131 points.  The
recurrences give

```text
C_7(1)=U_7(1)               = 29,082,240
Z_Q7(1/2)=1+W_7(1/2)        = 264,094,556
X_128                         = 8,257
outer-layer upper bound (4)  = 116,353,735
largest rooted upper bound   = 58,180,996
```

Therefore

\[
 2|L|\leq232707470<792283668=3Z_{Q_7}(1/2),                \tag{6}
\]

which already contradicts ORA before its additional positive
`131 Z_L(1/2)` term is included.  Also, for every one of the three hull
vertices,

\[
 4R_e(1)\leq232723984<528189112=2Z_{Q_7}(1/2).             \tag{7}
\]

Since `Z_{P-e}(1/2)>=Z_Q7(1/2)`, (7) contradicts RA even before its
additional positive rooted half-weight term is included.

This counterexample is structurally important: averaging over the whole
outer hull does not repair bad roots.  A skinny wrapper can force every
outer-rooted face to retain only one one-sided chain, while the unrooted
interior retains the product of two independent chains.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_extreme_ra/verify_wrapper_counterexample.py
```

The checker builds the 128-point core by exact rational strong gluing,
constructs (2), verifies all determinants, checks that the outer hull is
exactly the triangle, checks every sign in (3), evaluates (1) over the
integers and dyadic rationals, and confirms the strict numerical failures
(6)--(7).
