# The selected K2,4 support is an owner star, not a fourth colour

> **Continuation.**  `SWAP_K24_AMBIENT_OWNER_CORE_SATURATION.md` separates
> this support into literal ambient-owner geometry and dyadic-core
> membership.  Any ambient matching owner of load at least
> `ceil(3t/2)`, where `t` is the core level, automatically belongs to the
> core.  Thus the selected support may
> be removed losslessly on the high tail; only the low-load part retains a
> support discrepancy.

## 1. Outcome

The support indicator left in
`SWAP_K24_ADAPTIVE_POPULAR_THREE_FACTOR_GATE.md` has a simpler exact
description.  It does **not** depend on the cross-translation colour `e`.
It is the indicator of one physical two-neighbour star in the selected
swap core.

Write `J` for quarter-turn and `L=I+J`.  For a centre

\[
 C=(c,\ell)
\]

and two neighbour displacements `a,b`, put

\[
 C_a=(c+a,\ell+La),\qquad
 C_b=(c+b,\ell+Lb).                               \tag{1.1}
\]

The physical directed edges used by the mixed owner are

\[
 V=c+a,\qquad W=\ell+Lb.                          \tag{1.2}
\]

Fix the common endpoint and its two oriented roles.  Let
`G^epsilon_{a,b}` be the set of pairs `(z,c)` for which

\[
 \ell=z-J(c+a)                                    \tag{1.3}
\]

makes `(C,C_a,C_b)` an actual selected matching owner and the two edges
in (1.2) meet in the prescribed physical endpoint roles.  Then the support
set in the preceding note is exactly

\[
 \boxed{\mathcal G^\epsilon_{a,b,e}=\mathcal G^\epsilon_{a,b}}
                                                               \tag{1.4}
\]

for every occupied cross colour `e`.

This removes one false degree of freedom from the final gate.  The exact
remaining mass is a correlation between two parallel-copy fibres over the
same owner star, rather than a four-colour ambient tensor.

## 2. The two owner fibres

For any displacement `t`, define the selected parallel-copy fibre

\[
\begin{aligned}
 Q_{C,t}=\{q:\;&q,q+t\in\mathcal P,\quad c-q\in D,\\
             &\ell+Jq+Jt\in D,\quad
               \ell+Jq+Lt\in D\}.               \tag{2.1}
\end{aligned}
\]

This is the two-line fibre from
`SWAP_COMPLETION_DIAGONAL_FOUR_LINE_GATE.md`.  Put

\[
 X=Q_{C,a},\qquad Y=Q_{C,b}.                      \tag{2.2}
\]

For one cross colour `e`, the selected occurrence set is exactly

\[
 \boxed{S_{C,a,b}(e)=X\cap(e+Y).}                 \tag{2.3}
\]

Indeed an occurrence has first parameter `q` on the `a`-neighbour and
second parameter `q-e` on the `b`-neighbour.  Its six tracks are

\[
\begin{aligned}
 F_0&=c-q,&
 F_1&=\ell+Jq+Ja,&
 F_2&=\ell+Jq+La,\\
 F_3&=c-q+e,&
 F_4&=\ell+J(q-e)+Jb,&
 F_5&=\ell+J(q-e)+Lb.                            \tag{2.4}
\end{aligned}
\]

Thus `q in X` supplies the first three tracks and `q-e in Y` supplies the
last three.  Conversely (2.4), together with the four popular parameters,
recovers the two swap records.

The first-row K2,4 key has first coordinate

\[
 z=F_1+JF_0=\ell+J(c+a),                         \tag{2.5}
\]

which depends on `(C,a)` but not on `q` or `e`.  Equations (1.3) and
(2.5) are the same identity.  Hence the owner support depends on
`(a,b,z,c,epsilon)` and not on `e`, proving (1.4).

Writing

\[
 r_{C,a,b}(e)=|X\cap(e+Y)|,                      \tag{2.6}
\]

the whole selected same-centre mass is losslessly

\[
 \boxed{
 C_{\rm center}
 =3\sum_{\epsilon}\sum_{(a,b,z,c)\in\mathcal G^\epsilon}
       \sum_e {r_{C,a,b}(e)\choose3}.}           \tag{2.7}
\]

This is the physical-owner version of the cross-third-energy identity.
It is also exactly the support-restricted tensor from the preceding note
after summing the colour `e` last.

## 3. Literal endpoint parametrization

Let `x` be the common endpoint and let `v,w` be the other endpoints of
the two physical edges.  For fixed oriented roles choose signs
`sigma_V,sigma_W in {+1,-1}` so that

\[
 V=\sigma_V(v-x),\qquad W=\sigma_W(w-x).          \tag{3.1}
\]

Then every support point has

\[
\boxed{\begin{aligned}
 c&=\sigma_V(v-x)-a,\\
 \ell&=\sigma_W(w-x)-Lb,\\
 z&=\sigma_W(w-x)+J\sigma_V(v-x)-Lb.
\end{aligned}}                                   \tag{3.2}
\]

For a distance-Sidon set, a nonzero directed edge determines its ordered
endpoint pair.  Therefore, for fixed `(a,b,epsilon)`, the map from an
actual physical wedge to `(z,c)` is injective.  In particular

\[
 \boxed{|\mathcal G^\epsilon_{a,b}|\le k(k-1)^2.} \tag{3.3}
\]

There is a sharper endpoint-weighted cap.  Every support point also has

\[
 V,V-a\in D,\qquad W,W-Lb\in D.                  \tag{3.4}
\]

For fixed roles, a directed edge `V` fixes its common endpoint, after
which at most `k-1` directed `W` edges can use the prescribed role at that
point.  Interchanging `V,W` gives

\[
 \boxed{
 |\mathcal G^\epsilon_{a,b}|
 \le(k-1)\min\{R_D(a),R_D(Lb)\}.}                \tag{3.5}
\]

The crude (3.3) is a genuine `k^3` support bound **per displacement pair**.
Even (3.5) cannot be summed independently of the cell load: doing so would
still reintroduce the missing power.  The two colours, their overlap
weights, and selected-core membership must remain coupled.

## 4. Why four-norm inversion does not close this fibre

The four-norm theorem for a projected completion key is locally correct
but applies at a different level.  Here the K2,4 key and the first track
already determine all six tracks.  If one additionally fixes

\[
 n=|F_0|^2,                                       \tag{4.1}
\]

radial uniqueness leaves at most the two possibilities `F_0=f,-f`.
Consequently

\[
 \boxed{\text{a fixed K2,4 key and one norm label have load at most }2.}
                                                               \tag{4.2}
\]

This is stronger than the older four-norm local bound, but it supplies no
Carleson saving.  A fibre of load `r` occupies at least `r/2` distinct
norm cells, and its third mass counts triples of **different** norm cells.
Fragmenting the fibre into bounded norm cells therefore merely replaces
`binom(r,3)` by the number of occupied norm-cell triples.  The unresolved
quantity is global reuse of those triples across owner stars, not local
inversion inside one norm cell.

## 5. Sharpened remaining theorem

The direct target can now be stated without the artificial `e`-dependent
support notation:

\[
 \boxed{
 3\sum_{\epsilon}\sum_{(a,b,z,c)\in\mathcal G^\epsilon}
       \sum_{e:\ r_{C,a,b}(e)\ge R}
       {r_{C,a,b}(e)\choose3}
 \le N^{o(1)}(k^3+m^2)}                           \tag{5.1}
\]

for a subpolynomial threshold `R`.  Low `r` is already paid by the
parallel second-moment reservoir.  A threatening term in (5.1) is now an
explicit object:

* one actual physical endpoint wedge;
* one selected three-vertex star `(C,C_a,C_b)`;
* two parallel-copy fibres `Q_{C,a},Q_{C,b}`; and
* many translated copies of the same three-point parameter pattern.

The next density increment should be performed on these owner stars.
Neither the ambient three-factor tensor nor the four-norm local inversion
retains the information needed for (5.1).

## 6. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_k24_physical_owner_support.py
```

The verifier checks the fibre formulas, the six-track/K2,4 reconstruction,
the cross-correlation third moment, the endpoint parametrization and its
injectivity on a genuine distance-Sidon set, and the one-norm load-two
bound.
