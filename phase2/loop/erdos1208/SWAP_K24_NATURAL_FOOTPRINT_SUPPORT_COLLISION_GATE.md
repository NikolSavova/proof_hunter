# Natural-level K2,4 footprints admit an exact support/collision restart

## 1. Outcome

The footprint-density fork leaves maximum footprint depth as an unnecessarily
strong statistic.  It can be replaced losslessly by ordinary incidence
support and pair-collision mass.

Fix a dyadic owner-load band

\[
 R\le r_C<2R
\]

and a footprint-compression level `L`.  For every expansive cell put

\[
 \Phi_C=z_C+(JS_C-S_C)\subset D+D,
 \qquad
 M_C=3{r_C\choose3}.
\]

Let

\[
 I=\sum_C|\Phi_C|,
 \quad
 X=\left|\bigcup_C\Phi_C\right|,
 \quad
 Q=\sum_z{d(z)\choose2},
 \quad
 d(z)=|\{C:z\in\Phi_C\}|.
\]

Then

\[
 \boxed{I^2\le X(I+2Q)}                         \tag{1.1}
\]

and hence

\[
 \boxed{
 \sum_CM_C
 <8LR\left(X+\sqrt{2XQ}\right).}               \tag{1.2}
\]

Thus the expansive branch is paid either by its actual footprint union or
by a literal pair of distinct owner cells sharing one footprint value.  No
maximum-depth hypothesis remains.

Every collision has a rigid endpoint-labelled normal form.  After choosing
one representation canonically in each cell, it exposes

* two physical K2,4 owners, each with three cells in
  `U_floor(2R/3)`;
* two differences `A,B` of adaptive-popular parameters;
* four literal directions in `D-D`; and
* one quarter-turn equation coupling all of them.

This is the correct recursive survivor.  The low-collision population is
already support-paid; a threatening high-collision population is no longer
an anonymous overlap of subsets of `D+D`.

## 2. Incidence identity

Since

\[
 \sum_zd(z)=I,
 \qquad
 \sum_zd(z)^2=I+2Q,
\]

Cauchy gives (1.1).  Solving the quadratic inequality yields

\[
 I\le{X+\sqrt{X^2+8XQ}\over2}
 \le X+\sqrt{2XQ}.                              \tag{2.1}
\]

An expansive cell satisfies

\[
 |\Phi_C|>{r_C^2\over8L},
\]

so

\[
 {M_C\over|\Phi_C|}<4Lr_C<8LR.                 \tag{2.2}
\]

Summing (2.2) and then applying (2.1) proves (1.2).

Two useful regimes are immediate.

* If `Q<=I`, then `I<=3X`, so the mass is `<24LRX`.
* If `I` is polynomially larger than `X`, then (1.1) forces
  `Q` to be polynomially large.  The proof may pass to actual colliding
  owner pairs without a maximum-depth or dyadic-popularity loss.

Using the actual union `X`, rather than the whole ambient box, keeps the
`k^3` allowance for isolated large cells.  One isolated cell has
`X=Theta(R^2)` and mass `Theta(R^3)`, exactly as (1.2) predicts.

## 3. Collision normal form

For one owner write its centre as `(c,ell)` and let

\[
 z_1=\ell+J(c+a)
\]

be the first K2,4 colour.  The footprint offset used in the exact analyzer
is

\[
 c+\ell+Ja=z_1+(I-J)c.                          \tag{3.1}
\]

Thus a footprint representation by parameters `f,g in S` is

\[
 \zeta=z_1+(I-J)c+Jg-f.                         \tag{3.2}
\]

This is already a literal sum in `D+D`.  Namely, with

\[
 X=F_0(f)=c-f,
 \qquad T=F_1(g)=z_1-J(c-g),
\]

one has

\[
 \boxed{\zeta=X+T.}                              \tag{3.2a}
\]

Hence a footprint collision is a decorated additive quadruple

\[
 X+T=X'+T'
\]

in the complete difference set.  The decoration cannot be discarded:
distinct physical owner pairs can induce the same canonical quadruple.

Take a second owner with primed variables and suppose the same `zeta` lies
in both footprints.  Choose the lexicographically first representation in
each cell and put

\[
 \Delta c=c-c',\quad
 \Delta z=z_1-z_1',\quad
 A=f-f',\quad B=g-g'.
\]

Subtracting (3.2) gives the exact collision equation

\[
 \boxed{
 \Delta z+(I-J)\Delta c=A-JB.}                 \tag{3.3}
\]

The first two synchronized K2,4 tracks associated to a parameter `f` are

\[
 F_0(f)=c-f,qquad F_1(f)=z_1-JF_0(f).
\]

They and their primed versions are literal members of `D`.  Consequently
the collision exposes the four represented directions

\[
\boxed{\begin{aligned}
 U_A&=\Delta c-A, &V_A&=\Delta z-J\Delta c+JA,\\
 U_B&=\Delta c-B, &V_B&=\Delta z-J\Delta c+JB
\end{aligned}}                                  \tag{3.4}
\]

in `D-D`.  Moreover `A,B` are differences of actual adaptive-popular
parameters.  Equation (3.3) is equivalent to either pair of track
reconstructions and prevents the four directions from being separated into
independent ambient overlaps.

There is a further exact compression.  Put

\[
 u=\Delta c-A,
 \qquad H=A-B.
\]

Then the four directions in (3.4) are

\[
 \boxed{u,\quad u+H,\quad -u,\quad JH-u.}       \tag{3.5}
\]

Thus a footprint collision is a rotated three-direction closure, not four
independent `D-D` memberships.  The parameter `H` is the difference between
the two within-cell shifts `f-g` and `f'-g'`.  In particular, after reversal
symmetry is removed, the recursive core has only the two vector parameters
`(u,H)` and satisfies

\[
 (u+H)-u=H,
 \qquad u+(JH-u)=JH.                             \tag{3.6}
\]

This perpendicular pair of Schur closures is the preferred form for the
next endpoint-sensitive packing theorem.

The collision retains both physical endpoints and endpoint roles through
the two anchored K2,4 owner keys.  By the core-saturation theorem, all six
owner vertices lie in `U_floor(2R/3)`.  Therefore `Q` counts an exact
two-owner, four-direction, deep-core configuration.  It is the next object
for a density increment or determinant/height packing theorem.

## 4. Relation to the compressed branch

Combining this note with
`SWAP_K24_NATURAL_LEVEL_FOOTPRINT_DENSITY_FORK.md` gives a complete
three-way decomposition of one dyadic load band.

1. **Large support, few collisions:** paid by the first term of (1.2).
2. **Large support, many collisions:** gives the two-owner core
   (3.3)--(3.4).
3. **Compressed footprint:** gives at least `5L` perpendicular popular
   directions attached to one owner in `U_floor(2R/3)`.

The remaining theorem is consequently an aggregate packing statement for
two explicit density-increment objects.  A proof no longer needs to guess a
pointwise footprint bound.  Conversely, a counterexample must realize many
deep physical K2,4 owners while concentrating either the collision system
(3.3) or the perpendicular-popular incidences from the compressed branch.

This still does not close #1208.  It removes the overstrong maximum-depth
gate and identifies exactly what a failure of support packing contains.

## 5. Genuine stress

The analyzer now records cellwise footprints, energies, off-diagonal
supports, owner natural levels and footprint-pair codegrees.  The load-three
Costas-31 population has maximum footprint-pair codegree `140`, decisively
killing a bare `C4`-free hypothesis.  At the top genuine bands the maxima
fall to `2--3`, but the theorem above does not assume this finite behavior:
all excess is retained in `Q` and converted to (3.3)--(3.4).

Likewise, mapping a collision to its canonical additive quadruple (3.2a)
is not injective.  The maximum reuse is `4,210,810` on the full load-three
populations at Costas `23,29,31`.  It drops to `1` on the Costas-29
load-five band and `3` on the Costas-31 load-six band.  This is useful
high-level evidence, but the exact collision theorem must retain the two
anchored owner keys rather than assume bounded quadruple reuse.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_k24_natural_footprint_collision.py
python3 phase2/loop/erdos1208/verify_swap_k24_natural_level_footprint_fork.py
```

The first verifier checks the exact incidence identity and radical bound,
constructs nontrivial colliding footprints, verifies (3.3)--(3.4) on their
literal tracks, and checks the weighted expansive-cell inequality.  The
second verifier supplies the compressed perpendicular-popularity theorem
and the natural owner-level calculation.
