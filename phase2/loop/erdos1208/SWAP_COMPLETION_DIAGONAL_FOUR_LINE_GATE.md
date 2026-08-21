# Diagonal completion lines and the four-line rich cell

## 1. Outcome

The completion-square formulation still indexes records by a centre and a
neighbour displacement.  There is a lossless global normalization which
removes both from the individual fibre.  Put

\[
 \mathcal L_{U,B}=
 \{r\in\mathcal P_K:U-r,\ B+Jr\in D\},
 \qquad U,B\in D.                                  \tag{1.1}
\]

This is the diagonal line in the completion reservoir whose first terminal
is `U` and whose perpendicular start is `B`: every member is the vertex

\[
 (r,U-r,B)\in\mathcal V_K.                         \tag{1.2}
\]

The lines partition the completion reservoir with multiplicity one:

\[
 \boxed{
 \sum_{U,B\in D}|\mathcal L_{U,B}|
 =|\mathcal V_K|
 =\sum_{r\in\mathcal P_K}R_D(r)R_D(Jr).}          \tag{1.3}
\]

For a centre `C=(c,ell)` and neighbour displacement `t`, put

\[
 V=c+t,\qquad W=\ell+Lt.                           \tag{1.4}
\]

Then the parallel-copy fibre has the exact two-line form

\[
 \boxed{
 Q_{C,t}=\mathcal L_{c,W}
       \cap(\mathcal L_{V,\ell}-t).}               \tag{1.5}
\]

Thus a cross-difference cell between two fibres is a four-line
intersection.  If `q in Q_{C,t_1}` and `q-s in Q_{C,t_2}`, write
`V_i=c+t_i`, `W_i=ell+Lt_i`.  Its occurrence set is exactly

\[
\boxed{
 \mathscr S_{C,t_1,t_2,s}
 =\mathcal L_{c,W_1}
  \cap(\mathcal L_{V_1,\ell}-t_1)
  \cap(s+\mathcal L_{c,W_2})
  \cap(s-t_2+\mathcal L_{V_2,\ell}).}             \tag{1.6}
\]

The physical endpoint and its oriented roles select a subfamily of these
four-line cells; no endpoint information is used or lost in (1.5)--(1.6).
The size-biased mixed obstruction is therefore a four-line intersection
moment inside one global line reservoir of total mass `|V_K|`.

## 2. Proof of the two-line factorization

Recall

\[
 Q_{C,t}=\{q:q,q+t\in\mathcal P_K,\quad
 c-q,\ \ell+Jq+Jt,\ \ell+Jq+Lt\in D\}.           \tag{2.1}
\]

Membership `q in L_{c,W}` says

\[
 q\in\mathcal P_K,\qquad c-q\in D,\qquad
 W+Jq=\ell+Lt+Jq\in D.                            \tag{2.2}
\]

Membership `q+t in L_{V,ell}` says

\[
 q+t\in\mathcal P_K,\qquad
 V-(q+t)=c-q\in D,\qquad
 \ell+J(q+t)\in D.                                \tag{2.3}
\]

Together (2.2)--(2.3) are precisely (2.1), proving (1.5).  Applying
(1.5) to `q` and to `q-s`, then translating the latter two sets back to
the `q` coordinate, proves (1.6).

For (1.3), a vertex `(r,A,B)` determines and is determined by

\[
 U=A+r,\qquad r\in\mathcal L_{U,B}.                \tag{2.4}
\]

Alternatively, for fixed `r`, the `U` and `B` choices are independently
the `R_D(r)` and `R_D(Jr)` translated-pair starts.

## 3. Exact line degrees and pair codegrees

For one popular shift `r`, its line degree is

\[
 \boxed{
 |\{(U,B):r\in\mathcal L_{U,B}\}|
 =R_D(r)R_D(Jr)>K^2.}                              \tag{3.1}
\]

Thus popularity is exactly high incidence degree in the diagonal-line
system.

For two shifts `r_1,r_2`, define the signed triple loads

\[
\begin{aligned}
 T_D^-(r_1,r_2)
  &=|\{U\in D:U-r_1,U-r_2\in D\}|,\\
 T_D^+(Jr_1,Jr_2)
  &=|\{B\in D:B+Jr_1,B+Jr_2\in D\}|.
\end{aligned}                                      \tag{3.2}
\]

The two coordinates of a line are independent, so

\[
 \boxed{
 |\{(U,B):r_1,r_2\in\mathcal L_{U,B}\}|
 =T_D^-(r_1,r_2)T_D^+(Jr_1,Jr_2).}                \tag{3.3}
\]

This is the exact dual of the triple-intersection energy in
`SWAP_MIXED_SAME_CENTRE_TRIPLE_INTERSECTION_GATE.md`: a dense point block
forces high pair codegree in two perpendicular `D`-triple systems.

## 4. The direct Carleson theorem in line language

Let `mathfrak F` be the endpoint-compatible coupled line pairs arising
from active matching cells.  For each ordered pair of distinct members and
each displacement `s`, let `S` be the four-line intersection (1.6).  The
same-centre repeated mixed mass is

\[
 3\sum_{S\in\mathfrak F}{|S|\choose3}.            \tag{4.1}
\]

The exact remaining estimate is

\[
 \boxed{
 3\sum_{S\in\mathfrak F}{|S|\choose3}
 \le N^{o(1)}W_\parallel.}                        \tag{4.2}
\]

Low four-line load is already reduced to the second-generation pencil.
For high load, (3.3) and the perpendicular footprint fork give the only
two viable outcomes:

1. many point pairs have high codegree in perpendicular diagonal lines,
   producing a genuine high-reuse completion core; or
2. the four-line block has large metric/`D+D` support and must be paid by
   determinant and height.

An arbitrary set-system theorem cannot prove (4.2): popular points have
degree greater than `K^2`, and four sets may share a large block.  What is
new is that the line family is not abstract—its degrees and codegrees are
the explicit orthogonal `D` overlaps (3.1)--(3.3), while the coupled line
pairs retain a common physical endpoint.  This is the preferred form for
the next density-increment or determinant-sensitive incidence argument.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_completion_diagonal_four_line.py
```

The verifier exhausts random finite `D,P` systems.  It checks the reservoir
mass identity, the exact two-line representation of every active parallel
fibre, the four-line cross-cell formula, and the line degree/codegree
identities.
