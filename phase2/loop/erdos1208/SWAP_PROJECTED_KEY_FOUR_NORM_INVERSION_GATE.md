# Four-norm inversion over a projected completion key

## 1. Outcome

The role-projected completion key removes a factor `K` from the available
key space, but one projected key can still be reused through many full
completion vertices and many bases.  Four ordinary squared lengths remove
all of that local multiplicity.

Let `delta(v)=|v|^2`.  For either endpoint-role type, define a decorated
cell

\[
 (\text{type},\eta,n_1,n_2,n_3,n_4),              \tag{1.1}
\]

where `eta` is the role-projected key from
`SWAP_ROLE_PROJECTED_COMPLETION_RESERVOIR_GATE.md` and the four `n_i` are
the squared norms specified below.  Then

\[
 \boxed{\text{every decorated cell (1.1) has occurrence load at most }16.}
                                                               \tag{1.2}
\]

The bound is global: the base completion corner, centre, switch, moving
popular coordinate, neighbour displacement, and full fourth corner are all
recovered.  It uses only the distance-Sidon fact that a squared norm labels
at most the two directed vectors `v,-v` in `D`.

Moreover, in each role the four directed vectors obey one exact linear
identity.  Thus the remaining theorem is not a four-dimensional box count;
it is a support-sensitive packing problem for endpoint-realized solutions
of one four-vector equation, with two adaptive-popular pairs retained.

## 2. Moving-`W` role

Fix a projected key

\[
 \eta_\perp=(r,B),\qquad B,B+Jr\in D.             \tag{2.1}
\]

For an occurrence write `c=A+r` and use its variables `(q,t)`.  The six
variable directed vectors forced into `D` are

\[
\begin{aligned}
 X&=c-q,&Y&=B+Jq,\\
 V&=c+t,&E&=B-Lt,\\
 F&=B+Jq-t,&G&=B+Jr-t.
\end{aligned}                                     \tag{2.2}
\]

The four popular coordinates are

\[
 q,\quad q+t,\quad r,\quad r+t\in\mathcal P_K. \tag{2.3}
\]

Conversely, (2.1)--(2.3) reconstruct the completion square by

\[
 u=q-r,\quad p=q+t,\quad A=c-r,\quad
 \ell=B-Lt.                                       \tag{2.4}
\]

Decorate the projected key by

\[
 \mathbf n_\perp=(\delta(X),\delta(Y),
                   \delta(V),\delta(E)).          \tag{2.5}
\]

For each choice of the four oriented vectors compatible with these norm
labels, recover

\[
 q=-J(Y-B),\qquad c=X+q,qquad t=V-c,             \tag{2.6}
\]

and check `E=B-Lt`.  Hence there is at most one occurrence for each
oriented choice, and at most `2^4=16` in the norm cell.

The four vectors satisfy the exact centre-free identity

\[
 \boxed{E+LV-LX-(I-J)Y=JB.}                       \tag{2.7}
\]

Indeed substitute `X=c-q`, `Y=B+Jq`, `V=c+t`, and `E=B-Lt`.

## 3. Moving-`V` role

Now the projected key is

\[
 \eta_\parallel=(r,A),\qquad A,A+r\in D,qquad
 c=A+r.                                           \tag{3.1}
\]

Using the opposite-corner pivot, parameterize an occurrence by `(p,t)`.
Put

\[
\begin{aligned}
 X&=c-p,&Y&=B+Jp,\\
 C_0&=c-t,&W&=B+Lt,\\
 F&=B+Jp+t,&G&=B+Jr+t.
\end{aligned}                                     \tag{3.2}
\]

All six vectors lie in `D`, and

\[
 p,\quad p-t,\quad r,\quad r-t\in\mathcal P_K. \tag{3.3}
\]

The remaining variables are

\[
 u=p-r,\qquad q=p-t,\qquad B=Y-Jp.              \tag{3.4}
\]

Decorate the key by

\[
 \mathbf n_\parallel=(\delta(X),\delta(Y),
                       \delta(C_0),\delta(W)).    \tag{3.5}
\]

For each oriented choice compatible with the norm labels, recover

\[
 p=c-X,\qquad t=c-C_0,\qquad B=Y-Jp,            \tag{3.6}
\]

and check `W=B+Lt`.  This again gives load at most sixteen.  The exact
linear identity is

\[
 \boxed{W-Y-JX+LC_0=c.}                           \tag{3.7}
\]

## 4. Pair differences retained by a high cell

For two moving-`W` occurrences over the same projected key `(r,B)`, their
complementary completion starts need not agree.  Put

\[
 h=c_1-c_2=A_1-A_2,\qquad
 s=q_1-q_2,\qquad d=t_1-t_2.                      \tag{4.1}
\]

The six vector pairs in (2.2) have directed differences

\[
 \boxed{h-s,\quad Js,\quad h+d,\quad -Ld,
        \quad Js-d,\quad -d.}                    \tag{4.2}
\]

If the two occurrences also share the full completion corner, then `h=0`
and (4.2) reduces to the five-direction configuration from the repeated-`r`
matching branch.  For a merely projected-key collision, the additional
`h` is exactly the displacement along the complementary row of the
Cartesian completion fibre.

In the moving-`V` role, `c=A+r` is fixed while the perpendicular starts may
differ.  With `h=B_1-B_2`, `s=p_1-p_2`, and `d=t_1-t_2`, the corresponding
six differences are

\[
 \boxed{-s,\quad h+Js,\quad-d,\quad h+Ld,
        \quad h+Js+d,\quad h+d.}                 \tag{4.3}
\]

The final global gate can therefore be stated cleanly: bound the
size-biased pair energy of occupied cells (1.1), using (2.7)/(3.7), the
six pair directions (4.2)/(4.3), and the four adaptive-popular coordinates.
The only additional pair parameter is the explicit complementary-fibre
displacement `h`; no hidden completion-centre multiplicity remains.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_projected_key_four_norm_inversion.py
```

The verifier checks both six-vector normal forms, both centre-free linear
identities, exhaustive recovery from all compatible sign choices, and both
six-direction pair formulas on random integral occurrences.
