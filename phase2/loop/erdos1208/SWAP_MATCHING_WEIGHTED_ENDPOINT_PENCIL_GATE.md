# The weighted endpoint-pencil gate

## 1. Outcome

The endpoint-contact branch of the matching wedge problem has a sharper
exact reduction than the maximum-product estimate
`mu_z^2 kappa_z h_z`.  Work in one matching component and write `m(C,B)`
for the multiplicity of the edge between two cells.  Every matching cell
`B` has a four-element set `E(B)` of physical endpoints.

For a centre cell `C` and a physical point `x`, put

\[
 \lambda(C,x)=
 \sum_{B\sim C:\ x\in E(B)}m(C,B)                         \tag{1.1}
\]

and

\[
 P(C,x)=
 \sum_{\substack{B<B'\sim C\\x\in E(B)\cap E(B')}}
 m(C,B)m(C,B').                                           \tag{1.2}
\]

Let `M` be the total matching edge-copy mass.  Then the complete
endpoint-contact wedge mass satisfies

\[
 \boxed{W_{\rm contact}\le \mathcal P_{\rm end}:=
 \sum_{C,x}P(C,x).}                                      \tag{1.3}
\]

Moreover, if

\[
 \Theta=
 \max_{C,x:\lambda(C,x)>0}{P(C,x)\over\lambda(C,x)},     \tag{1.4}
\]

then

\[
 \boxed{\mathcal P_{\rm end}\le8\Theta M.}              \tag{1.5}
\]

Consequently the endpoint-contact branch closes from either the aggregate
estimate

\[
 \boxed{\mathcal P_{\rm end}\le K N^{o(1)}M}             \tag{1.6}
\]

or the stronger local estimate `Theta<=K N^{o(1)}`.  This is strictly
better targeted than `mu^2 kappa h`: it couples multiplicity to the actual
endpoint pencil where it occurs, discounts a large isolated parallel
fibre, and removes the component-size factor `h` entirely.

This note proves (1.3)--(1.5) and gives the complete two-copy normal form
for (1.6).  It does not yet prove (1.6).

## 2. The weighted-pencil identity

For fixed `(C,x)`, write the nonzero incident weights in the `x`-pencil as
`w_1,...,w_s`.  Then

\[
 \lambda(C,x)=\sum_iw_i,
 \qquad
 P(C,x)={1\over2}\left(
     \lambda(C,x)^2-\sum_iw_i^2
 \right).                                                \tag{2.1}
\]

Every contact wedge has two distinct neighbouring cells sharing at least
one endpoint, so it is counted at least once on the right of (1.3).  It
can be counted more than once only if the two neighbouring cells share
more than one physical endpoint; this harmless overcount is why (1.3) is
an inequality.

Every neighbour cell has exactly four physical endpoints.  Summing (1.1)
first over `x` and then over the two ends of every matching edge gives

\[
 \sum_{C,x}\lambda(C,x)
 =4\sum_Cd_{\rm wt}(C)=8M.                              \tag{2.2}
\]

Now `P(C,x)<=Theta lambda(C,x)` and (1.5) follows.  Notice that a pencil
supported on only one neighbour has `P(C,x)=0`, regardless of the parallel
multiplicity.  This is the cancellation lost by the old product of
separate maxima.

## 3. One edge copy relative to its centre

Put `L=I+J`.  Fix a centre cell

\[
 C=C_z(c)=(c,\ell),\qquad \ell=z+Lc.                    \tag{3.1}
\]

For an edge copy from `C` to `B=C_z(b)`, let `a` be its base and define the
two adaptive-popular shifts

\[
 q=c-a,\qquad p=b-a.                                    \tag{3.2}
\]

Then

\[
 a=c-q,\qquad b=c+p-q,
 \qquad r=z+J(c+p),                                     \tag{3.3}
\]

and the seven complete-difference roles are exactly

\[
\boxed{
\begin{gathered}
 c-q,\quad c+p-q,\quad c,\\
 \ell+Lp-q,\quad \ell+Jp,\\
 \ell+L(p-q),\quad \ell\in D,
 \qquad p,q\in\mathcal P_K.
\end{gathered}}                                         \tag{3.4}
\]

Conversely (3.2)--(3.4) reconstruct the edge copy.  Thus a fixed endpoint
pencil is a two-variable, five-moving-projection system, not an arbitrary
weighted star.

## 4. Two copies sharing one oriented endpoint

Take two edge copies at the same centre, with parameters `(p_i,q_i)` and
neighbours

\[
 b_i=c+p_i-q_i=x-y_i\qquad(i=1,2),                       \tag{4.1}
\]

where the physical endpoint `x` occurs in the same oriented first-edge
role.  Put

\[
 \delta=b_1-b_2=y_2-y_1\in D,
 \qquad
 \rho=J(p_1-p_2).                                      \tag{4.2}
\]

Comparing the five moving roles in (3.4) gives the exact collision system

\[
\boxed{
 \delta,\quad L\delta,\quad \rho,
 \quad\delta+\rho,\quad\delta+J\rho\in D-D.}            \tag{4.3}
\]

More precisely these five differences occur respectively on the two
neighbour first-edge roles, neighbour second-edge roles, the `ell+Jp`
roles, the `ell+Lp-q` roles, and the base roles.  The popular-shift pairs
also retain

\[
 p_1-p_2=-J\rho,
 \qquad
 q_1-q_2=-(\delta+J\rho).                               \tag{4.4}
\]

If the shared oriented endpoint lies on the neighbour second-edge role,
the same calculation applies after interchanging `delta` with `L delta`.
Uniformly across all endpoint roles, contact gives the following extra raw
condition.  Choose

\[
 u_i\in\{b_i,\ell+L(p_i-q_i)\},\qquad
 \epsilon_i\in\{1,-1\}                                  \tag{4.5}
\]

so that `epsilon_i u_i=x-y_i` has common head `x`.  Then

\[
 \boxed{\epsilon_1u_1-\epsilon_2u_2=y_2-y_1\in D.}       \tag{4.6}
\]

Thus opposite orientations and cross-role contacts give signed midpoint
forms, but never lose the complete raw difference in (4.6).  There are
only sixteen `(u_1,u_2,epsilon_1,epsilon_2)` types, so they may be separated
before any analytic estimate.

Equations (4.1)--(4.4) are the correct object for a proof of (1.6).  In
particular, deleting the endpoint identity `delta=y_2-y_1`, or deleting
the two simultaneous popular-set differences (4.4), returns to the
generic affine countermodels which already defeat raw `D-D` energy bounds.

## 5. Exact stress

The exact optimal matching cores give the following profiles.  The last
two columns are the exact contact-pencil upper mass divided by `M`, and
the local ratio `Theta`.

| family | `K` | max `lambda` | `P_end/M` | max `Theta` |
|---|---:|---:|---:|---:|
| Costas 17 | 9.539 | 5 | 0.281 | 6/5 |
| Costas 23 | 9.747 | 12 | 1.431 | 53/12 |
| Costas 29 | 9.518 | 22 | 2.612 | 181/22 |
| Costas 31 | 10.901 | 17 | 1.469 | 97/16 |
| Costas 37 | 11.036 | 15 | 1.481 | 38/7 |
| closure 40 | 99.972 | 13 | 0.826 | 31/6 |
| closure 50 | 136.497 | 6 | 0.345 | 13/6 |

Thus the aggregate quantity in (1.6), unlike `mu^2 kappa h`, has a large
margin on every current genuine stress.  The pointwise load `lambda` can
exceed `K` (Costas 29), while `Theta` remains below `K`; this confirms that
subtracting the same-neighbour square term in (2.1) is load-bearing.

## 6. Verification and next theorem

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_matching_weighted_endpoint_pencil.py
python3 phase2/loop/erdos1208/verify_swap_matching_weighted_endpoint_pencil.py --larger
```

The verifier checks (1.3)--(2.2) on finite weighted endpoint systems,
proves (3.3)--(3.4) and (4.2)--(4.4) symbolically, and reproduces the stored
Costas profiles.  The optional run checks Costas 37.

The direct endpoint-contact theorem is now exactly (1.6).  A proof should
dyadically regularize the two popular differences in (4.4), retain the
physical edge `delta=y_2-y_1`, and show that polynomial excess in (1.6)
forces two distinct complete-difference vectors of equal Euclidean norm.
The clean sixteen-endpoint codegree branch remains separate and is governed
by the common-`r` support/collision dichotomy.
