# Metric transversality inside one decorated endpoint key

## 1. Outcome

The proper collision colouring in
`SWAP_COMPLETION_BOX_DYADIC_DENSITY_GATE.md` still permits an abstract
one-factorization.  This note retains the squared Euclidean lengths of all
six directed-difference roles and proves that such a colour can never be
metrically one-dimensional.

Fix a centre `C=(c,ell)`, two distinct neighbour displacements `t_1,t_2`,
and one decorated endpoint key.  Put

\[
 d=t_1-t_2\ne0,\qquad s=q_1-q_2.                 \tag{1.1}
\]

The occurrences of this key are parameterized by one set `S`.  For
`q in S`, define

\[
\begin{aligned}
 A&=c-q,\\
 B&=\ell+Jq+Jt_1,\\
 C_1&=\ell+Jq+Lt_1=B+t_1,
\end{aligned}                                      \tag{1.2}
\]

where `L=I+J`.  Then the exact six-difference cell is

\[
\boxed{
 A,A+s,\quad B,B-J(s+d),\quad
 C_1,C_1-Js-Ld\in D.}                              \tag{1.3}
\]

The four adaptive-popular corners are

\[
 q,q+t_1,q-s,q-s+t_2\in\mathcal P_K.              \tag{1.4}
\]

Conversely, (1.3)--(1.4), the fixed endpoint role, and the physical
endpoint condition recover one occurrence of the decorated key.  Thus a
key load is the size of one explicit triple overlap, not an arbitrary
edge-colour class.

Let `delta(v)=|v|^2` and attach the three metric gaps

\[
\begin{aligned}
 g_0(A)&=\delta(A+s)-\delta(A),\\
 g_1(A)&=\delta(B-J(s+d))-\delta(B),\\
 g_2(A)&=\delta(C_1-Js-Ld)-\delta(C_1).
\end{aligned}                                      \tag{1.5}
\]

Their linear parts as functions of `A` are respectively

\[
 2A\mathbin\cdot v_0,\quad2A\mathbin\cdot v_1,
 \quad2A\mathbin\cdot v_2,                         \tag{1.6}
\]

where

\[
 v_0=s,\qquad v_1=s+d,\qquad v_2=s+d-Jd.            \tag{1.7}
\]

These three vectors always span the plane.  More sharply,

\[
\boxed{
 \max_{0\le i<j\le2}|\det(v_i,v_j)|
 \ge {|d|^2\over3}.}                               \tag{1.8}
\]

Choose the lexicographically first maximizing pair `(i,j)`.  The refined
metric key

\[
 (\text{decorated key},g_i,g_j)                     \tag{1.9}
\]

has load at most one.  Its affine Jacobian in the integer variable `A`
has absolute determinant at least

\[
 \boxed{{4\over3}|d|^2.}                            \tag{1.10}
\]

Therefore the matching-heavy survivor has no genuine rank-one metric
branch.  It is a packing problem for occupied points in rank-two affine
lattices whose covolume grows quadratically with the physical neighbour
separation `|d|`.  This does **not** yet prove the desired aggregate bound:
discarding the endpoint and popularity labels and counting all lattice
points in the ambient metric box loses the cube-root scale.

## 2. Exact occurrence set

For fixed `(C,t_1,t_2,s)`, write

\[
 \mathscr S_{C,t_1,t_2,s}
 =\{q:q\in Q_{C,t_1},\ q-s\in Q_{C,t_2}\}.          \tag{2.1}
\]

This is precisely the cross-difference fibre in equation (5.5) of the
weighted endpoint-pencil note.  Expanding the definition of `Q_{C,t}`
gives (1.3)--(1.4).  In detail, the second occurrence has starts

\[
 A+s,\qquad B-J(s+d),\qquad C_1-Js-Ld.              \tag{2.2}
\]

The first start `A=c-q` recovers `q`, so no multiplicity is lost in this
normal form.

For later use, put

\[
 K_0=\ell+Jc+Jt_1.
\]

Then

\[
 B=K_0-JA,\qquad C_1=K_0+t_1-JA.                   \tag{2.3}
\]

Equations (2.2)--(2.3) show that one occurrence is three synchronized
translated pairs in `D`, all driven by the same two-dimensional variable
`A`.

## 3. Proof of metric transversality

The first gap in (1.5) plainly has linear part `2 A dot s`.  Put
`beta=-J(s+d)` and `gamma=-Js-Ld`.  Since

\[
 J\beta=s+d,\qquad J\gamma=s+d-Jd,                  \tag{3.1}
\]

and `B,C_1` have linear part `-JA`, expanding the other two squared norms
gives exactly (1.6)--(1.7).

Let

\[
 a=\det(s,d),\qquad b=s\mathbin\cdot d,
 \qquad D_0=|d|^2.
\]

The three pair determinants are

\[
 \det(v_0,v_1)=a,\qquad
 \det(v_0,v_2)=a-b,\qquad
 \det(v_1,v_2)=-(b+D_0).                            \tag{3.2}
\]

If all three absolute values were below `D_0/3`, the first two would give
`|b|<2D_0/3`, while the third would force
`b in (-4D_0/3,-2D_0/3)`, a contradiction.  This proves (1.8).
The constant is sharp at the real-vector level: for `d=(3,0)` and
`s=(-2,1)`, all three determinants have absolute value three, equal to
`|d|^2/3`.

For a selected pair `(i,j)`, equality of `(g_i,g_j)` for two occurrences
`A,A'` implies

\[
 (A-A')\mathbin\cdot v_i=(A-A')\mathbin\cdot v_j=0.
\]

The two directions are independent, so `A=A'`, and then `q=q'`.  The
linear coefficient matrix has rows `2v_i,2v_j`; its determinant is
`4 det(v_i,v_j)`, proving (1.9)--(1.10).

## 4. The exact remaining packing gate

Let

\[
 \Lambda=\{|e|^2:e\in D\}
\]

be the set of nonzero squared-distance labels.  Distance-Sidonicity gives
`|Lambda|=binom(k,2)`, and every coordinate in (1.5) lies in
`Lambda-Lambda`.  For a fixed decorated cell, the selected metric pairs
lie in one coset of a rank-two integer lattice of covolume at least
`4|d|^2/3`.

The desired repeated-key estimate is now equivalent to a labelled packing
bound for

\[
 \sum_{C,x,\mathrm{roles},t_1\ne t_2,s}
 { |\mathscr S_{C,t_1,t_2,s}|\choose2},             \tag{4.1}
\]

where every occupied metric point must retain (1.3), (1.4), and the fixed
physical endpoint role.  A viable proof can dyadically split `|d|` and
apply a determinant-sensitive large sieve or incidence bound to these
metric lattices.  The theorem must be endpoint weighted: the unlabelled
ambient lattice count has an `O(m^2)` boundary term per cell and is far too
large after summing cells.

The useful conclusion is a clean strategic exclusion.  There is no
separate parabolic or rank-one metric case to classify.  Any remaining
counterexample must reuse many genuinely two-dimensional metric lattice
points across many endpoint-decorated cells while simultaneously keeping
all four adaptive-popular corners.  That is the direct height-sensitive
packing statement required for the `1/3` exponent.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_decorated_key_metric_transversal.py
```

The verifier checks the six-vector normal form and all three gap formulas
on exhaustive small integer parameters, proves the determinant inequality
and its sharp example, checks canonical-pair injectivity on random cells,
and verifies the theorem on the genuine two-occurrence transformed
Costas-23 collision from the completion-box note.
