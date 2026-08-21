# Support growth in a high-reuse completion link rectangle

## 1. Outcome

The local metric inversions reduce the repeated endpoint-key problem to
global reuse of completion corners.  This note gives the exact link-matrix
normal form at one corner and proves a target-scale theorem for all four
oriented physical endpoint roles.  The base corner is chosen opposite the
physical label, so that the moving popular coordinate is always an affine
copy of a subset of `A` and hence vector-Sidon.

Fix

\[
 v=(p,X,\ell)\in\mathcal V_K,qquad Z_0=\ell+Lp.   \tag{1.1}
\]

A reverse record through `v` is indexed by a horizontal move `u` and a
vertical popular coordinate `q`.  Put

\[
 W_q=\ell+L(p-q),\qquad Z_q=W_q+Jq=Z_0-q.          \tag{1.2}
\]

The other three completion vertices are

\[
 (p-u,X+u,\ell),\quad(q,X,W_q),\quad
 (q-u,X+u,W_q).                                   \tag{1.3}
\]

After the row-only and column-only conditions are removed, the two exact
cross conditions are

\[
 \boxed{q-u\in\mathcal P_K,qquad Z_0-q-Ju\in D.} \tag{1.4}
\]

The map

\[
 (u,q)\longmapsto(q-u,Z_0-q-Ju)                   \tag{1.5}
\]

is injective: its inverse satisfies

\[
 Lu=Z_0-(q-u)-(Z_0-q-Ju).                         \tag{1.6}
\]

Let `G subset U x Q` be any occupied subgraph and put `e=|E(G)|`.  If the
physical endpoint lies on the moving label `W_q`, then `Q` is vector-Sidon.
The cross vectors in (1.4) give the literal support

\[
 Z(G)=\{Z_0-q-Ju:(u,q)\in E(G)\}\subset D.        \tag{1.7}
\]

Writing `a=|Q|` and `b=|U|`, vector-Sidonicity gives the restricted energy
bound

\[
 \sum_z r_G(z)^2\le e+b(b-1)\le b(a+b),           \tag{1.8}
\]

where `r_G(z)` counts edges with `q+Ju=z`.  Consequently

\[
 \boxed{
 |Z(G)|\ge {e^2\over b(a+b)},
 \qquad e^2\le |D|\,b(a+b).}                     \tag{1.9}
\]

This is already a sparse theorem: no rectangle extraction or regularity
lemma is needed.  For the complete graph `G=U x Q`, it specializes to

\[
 |Q+JU|\ge{a^2b\over a+b},
 \qquad a\min\{a,b\}\le2|D|.                    \tag{1.10}
\]

Thus a balanced complete link rectangle has side at most
`sqrt(2|D|)`, while an arbitrary sparse link is controlled by the exact
row-size moment `b(a+b)`.

If instead the endpoint lies on the label `X+p`, pivot to the opposite
`q`-corner.  Section 4 proves the identical theorem with `p` as the moving
vector-Sidon coordinate.  Thus (1.9) applies to every oriented role.

The remaining obstruction is global rather than local: one must sum the
row-size moments `|U_v|(|Q_v|+|U_v|)` over reused completion corners without
paying an uncontrolled number of centres.

## 2. Exact link expansion

Membership of the four vertices in `mathcal V_K` expands as follows.  The
base corner gives

\[
 X,X+p,\ell,\ell+Jp\in D.                         \tag{2.1}
\]

The horizontal corner adds

\[
 X+u,\qquad\ell+Jp-Ju\in D,qquad p-u\in\mathcal P_K.
                                                               \tag{2.2}
\]

The vertical corner adds

\[
 X+q,W_q,Z_q\in D,qquad q\in\mathcal P_K.        \tag{2.3}
\]

The fourth corner shares the first three relevant starts and adds exactly

\[
 q-u\in\mathcal P_K,qquad Z_q-Ju\in D,           \tag{2.4}
\]

which is (1.4).  Formula (1.6) follows by adding the two output coordinates
in (1.5): if `r=q-u` and `z=Z_0-q-Ju`, then

\[
 Z_0-r-z=u+Ju=Lu.                                 \tag{2.5}
\]

The integral inverse exists automatically for an occupied cell.

## 3. Why the moving-role column set is vector-Sidon

Suppose the fixed physical endpoint is `x`, and choose one orientation of
the label `W_q`.  Its other endpoint `y` satisfies one of

\[
 W_q=x-y\qquad\text{or}\qquad W_q=y-x.            \tag{3.1}
\]

Since `W_q=ell+L(p-q)`, the corresponding `q` lies in one of the affine
images

\[
 p-L^{-1}(x-A-\ell),qquad
 p-L^{-1}(A-x-\ell).                              \tag{3.2}
\]

Directed-vector Sidonicity of `A`, followed by the injective linear map
`L^{-1}`, shows that every nonzero directed difference of `Q` has at most
one ordered representation.  Hence `Q` is vector-Sidon.

The diagonal part of the restricted energy has `e` solutions.  For every
nonzero ordered difference in `Q-Q`, there is at most one ordered `Q` pair,
while the total number of ordered distinct `U` pairs is `b(b-1)`.  This
proves (1.8).  Cauchy--Schwarz gives (1.9).  For the complete graph it gives
the first part of (1.10); since `a+b<=2max(a,b)`, the second follows.

## 4. The dual pivot covers the fixed-label roles

Suppose the physical endpoint lies on

\[
 V_p=X+p.                                          \tag{4.1}
\]

At the `p`-corner this label is fixed and gives no information about the
`q` columns.  Instead base the same completion square at its opposite
corner

\[
 w=(q,X,W).                                        \tag{4.2}
\]

For a moving popular coordinate `p`, put

\[
 \ell_p=W-L(p-q),\qquad R_0=W+Lq.                 \tag{4.3}
\]

The square is

\[
 (q,X,W),\quad(q-u,X+u,W),\quad
 (p,X,\ell_p),\quad(p-u,X+u,\ell_p),              \tag{4.4}
\]

and its exact cross conditions are

\[
 \boxed{p-u\in\mathcal P_K,qquad R_0-p-Ju\in D.} \tag{4.5}
\]

Indeed

\[
 \ell_p+J(p-u)=W+Lq-p-Ju=R_0-p-Ju.               \tag{4.6}
\]

The map `(u,p)` to the two values in (4.5) has the same inverse (1.6).
After fixing the orientation at `x`, the condition `X+p=x-y` or `y-x`
makes the `p`-set a translate of `x-A-X` or `A-x-X`; it is vector-Sidon.
The proof of (1.9) applies verbatim with `P` in place of `Q`.

Thus every one of the four physical endpoint roles has a canonical base:

\[
\begin{array}{c|c|c}
\text{physical label}&\text{base corner}&\text{Sidon moving coordinate}\\\hline
W_q&(p,X,\ell)&q\\
X+p&(q,X,W)&p.
\end{array}                                        \tag{4.7}
\]

## 5. Relation to the global Carleson gate

Let a rich completion corner `v` have a role-adapted link graph
`G_v subset U_v x Q_v`, and write `d(v)=|E(G_v)|`.  The sparse theorem gives

\[
 d(v)^2\le |D|\,|U_v|\bigl(|Q_v|+|U_v|\bigr).    \tag{5.1}
\]

The dual pivot removes the former fixed-label asymmetry, so (5.1) is
available in all four endpoint roles.  The remaining theorem is therefore
a global moment packing statement: sum the quantities

\[
 |U_v|\bigl(|Q_v|+|U_v|\bigr)                    \tag{5.2}
\]

over the size-biased family of reused corners, retaining the endpoint and
metric-key weights, without paying the number of centres.  This is
strictly narrower than the previous rectangle-extraction problem: every
individual sparse link is already controlled optimally up to constants.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_completion_link_rectangle_support.py
```

The verifier checks both exact four-corner expansions and their inverse,
exhausts the energy estimate on random vector-Sidon column sets, arbitrary
row sets, and random sparse subgraphs, and verifies both the sparse and
complete support inequalities.
