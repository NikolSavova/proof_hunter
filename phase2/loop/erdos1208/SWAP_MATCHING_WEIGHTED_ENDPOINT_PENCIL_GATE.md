# The weighted endpoint-pencil gate

## 1. Outcome

The endpoint-contact branch of the matching wedge problem has a sharper
exact reduction than the maximum-product estimate
`mu_z^2 kappa_z h_z`.  Work in one matching component and write `m(C,B)`
for the multiplicity of the edge between two cells.  A matching cell `B`
has a set `E(B)` of at most four physical endpoints; a zero directed label
contributes none.

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

Every neighbour cell has at most four physical endpoints.  Summing (1.1)
first over `x` and then over the two ends of every matching edge gives

\[
 \sum_{C,x}\lambda(C,x)
 \le4\sum_Cd_{\rm wt}(C)=8M.                            \tag{2.2}
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

## 5. Role-refined key rigidity

There is an additional exact compression after retaining the oriented
endpoint roles and their raw physical difference.
Write

\[
 t=p-q=b-c.                                             \tag{5.1}
\]

For fixed centre `(c,ell)` and fixed neighbour displacement `t`, the
parallel-copy fibre is exactly

\[
\boxed{
 Q_{C,t}=\{q:\ q,q+t\in\mathcal P_K,\quad
 c-q,\quad \ell+Jq+Jt,\quad \ell+Jq+Lt\in D\}.}         \tag{5.2}
\]

The two cell labels `c+t` and `ell+Lt` are fixed separately.  In particular
`m(C,C_z(c+t))=|Q_{C,t}|` after the matching endpoint filter.

Associate to a copy the four-dimensional parameter point

\[
 g(p,q)=(p-q,Jp)=(t,Jp).                                \tag{5.3}
\]

For two copies, the difference of their parameter points is precisely
`(delta,rho)` from (4.2).  Fix `C`, `x`, and the ordered pair of their four
oriented endpoint roles.  Augment this parameter difference by the raw
endpoint difference

\[
 \sigma=y_2-y_1\in D.                                  \tag{5.4}
\]

If two ordered copy pairs have the same
`(roles,sigma,delta,rho)`, then they have the same ordered pair of neighbour
cells.  Indeed, vector-Sidonicity of `A` makes `sigma` recover the ordered
pair `(y_2,y_1)`.  With `x`, `C`, and the two roles fixed, both directed
neighbour labels and hence both cells are forced.  In equal first-label
roles `sigma=+/-delta`; in equal second-label roles
`sigma=+/-Ldelta`, so the augmentation is redundant there but essential
for cross-role contacts.

Consequently repeated decorated keys cannot mix different neighbour pairs.
For one fixed ordered pair `(t_1,t_2)`, their multiplicity is
exactly a cross-difference multiplicity between the two fibres in (5.2):

\[
 q_1-q_2=-(\delta+J\rho),\qquad
 q_i\in Q_{C,t_i}.                                      \tag{5.5}
\]

Thus the remaining obstruction in (1.6) is no longer an arbitrary contact
graph.  It is the size-biased cross-energy of the explicit three-`D` fibres
`Q_{C,t}`, indexed by a Sidon family of neighbour displacements.  Large
support in (5.5) pays the distinct-key branch; repeated keys are confined
to additive rectangles between the same two parallel-copy fibres.

## 6. Exact support-versus-collision fork

Fix `(C,x)` and one ordered endpoint-role pair.  Let `Omega` be the set of
copy pairs on two distinct neighbour fibres in that pencil, canonically
ordered by the neighbour cells, and map each member of `Omega` to its
decorated key

\[
 (\text{roles},\sigma,\delta,\rho).                    \tag{6.1}
\]

Write `n=|Omega|`, let `X` be the number of keys used, and let `Q` count
unordered pairs of distinct members of `Omega` with the same key.  If the
key loads are `n_k`, then

\[
 \sum_kn_k=n,\qquad \sum_kn_k^2=n+2Q.
\]

Cauchy gives the lossless local fork

\[
 \boxed{n^2\le X(n+2Q).}                              \tag{6.2}
\]

Now sum over all centres, endpoints, and role pairs.  Denote the three
global sums by `P_end`, `X_end`, and `Q_end`; the first is exactly the pencil
upper mass in (1.3).  A second Cauchy inequality gives

\[
 \boxed{P_{\rm end}^2\le
 X_{\rm end}(P_{\rm end}+2Q_{\rm end}).}              \tag{6.3}
\]

Hence either `P_end<=2X_end`, or

\[
 Q_{\rm end}\ge {P_{\rm end}^2\over4X_{\rm end}}.     \tag{6.4}
\]

By Section 5, two occurrences counted by `Q_end` use the same ordered pair
of neighbour fibres and satisfy

\[
 q_1-q_2=q'_1-q'_2,\qquad
 q_1+q'_2=q'_1+q_2.                                   \tag{6.5}
\]

No edge copy can be shared by the two occurrences: within a fixed fibre,
`q` determines the copy.  Thus every collision in (6.5) is a genuine
four-copy additive rectangle, with all six memberships defining the two
`Q_{C,t}` fibres, both endpoint roles, and the raw difference `sigma`
retained.

There is also an exact orthogonal switch back to the original rich-tail
energy.  Write the two occurrences as `(q_1,q_2)` and `(q'_1,q'_2)` and put

\[
 u=q_1-q'_1=q_2-q'_2\ne0.                             \tag{6.6}
\]

For `i=1,2`, define

\[
\begin{aligned}
 X_i&=c-q_i,&X'_i&=c-q'_i,\\
 Y_i&=\ell+Jq_i+Jt_i,&Y'_i&=\ell+Jq'_i+Jt_i,\\
 Z_i&=\ell+Jq_i+Lt_i,&Z'_i&=\ell+Jq'_i+Lt_i.
\end{aligned}                                         \tag{6.7}
\]

All twelve displayed vectors lie in `D`, and

\[
 X_i-X'_i=-u,\qquad
 Y_i-Y'_i=Z_i-Z'_i=Ju.                                \tag{6.8}
\]

Thus every repeated endpoint key canonically creates two labelled
representations of `-u` and four of `Ju`, while retaining the eight popular
corners `q_i,q_i+t_i,q'_i,q'_i+t_i`.  The collision branch is therefore a
self-switch into the perpendicular overlap energy, not an unrelated fourth
moment.  A proof may split the new shift `u` at the adaptive cutoff: the
nonpopular part belongs to the already-paid low tail, while the popular
part is a genuinely recursive rich rectangle.  What is still missing is a
reverse-multiplicity or density-increment theorem that retains the centre,
fibre, and endpoint decorations in this switch.

The whole collision mass is itself an exact second-generation endpoint
pencil.  For fixed `(C,x,u)`, put

\[
 a_t(u)=R_{Q_{C,t}}(u),\qquad
 \Lambda_2(C,x,u)=\sum_ta_t(u),\qquad
 P_2(C,x,u)=\sum_{t<t'}a_t(u)a_{t'}(u),                \tag{6.9}
\]

where `t` ranges over neighbour fibres whose cell contains `x`.  The usual
cross-energy identity gives

\[
 \boxed{2Q_{\rm end}=\sum_{C,x,u\ne0}P_2(C,x,u).}     \tag{6.10}
\]

Let `W_parallel` be the centred parallel-wedge mass
`sum_{C,t} binom(|Q_{C,t}|,2)` and define

\[
 \Theta_2=
 \max_{\Lambda_2>0}{P_2(C,x,u)\over\Lambda_2(C,x,u)}.
\]

Since each neighbour cell has at most four physical endpoints,

\[
 \sum_{C,x,u\ne0}\Lambda_2(C,x,u)
 \le 8W_{\rm parallel}.
\]

Consequently

\[
 \boxed{Q_{\rm end}\le4\Theta_2W_{\rm parallel}.}     \tag{6.11}
\]

If `a_{t_*}` is the largest weight in one second-generation pencil and
`B=Lambda_2-a_{t_*}`, then

\[
 P_2=a_{t_*}B+\sum_{t<t',\ t,t'\ne t_*}a_ta_{t'}
 \le B\Lambda_2.
\]

Therefore

\[
 \boxed{\Theta_2\le
 \max_{C,x,u}\left(\Lambda_2(C,x,u)-\max_ta_t(u)\right).} \tag{6.12}
\]

This is another load-bearing cancellation: one arbitrarily heavy parallel
fibre costs nothing.  The sharp local inverse target is to bound the
off-largest-fibre internal-difference load, not the full `Lambda_2`.

The preferred form is aggregate rather than pointwise.  Define

\[
 \mathcal G_2=
 \sum_{C,x,u\ne0}
 \left(\Lambda_2(C,x,u)-\max_ta_t(u)\right)
 \Lambda_2(C,x,u).                                    \tag{6.13}
\]

Equations (6.10) and (6.12) give the exact sufficient bound

\[
 \boxed{2Q_{\rm end}\le\mathcal G_2.}                 \tag{6.14}
\]

Thus the sharp collision theorem is

\[
 \boxed{\mathcal G_2\le N^{o(1)}W_{\rm parallel}.}
\]

It is weaker and safer than a uniform subpolynomial bound on `Theta_2` and
preserves the size bias needed by the nested-core argument.

This couples the collision branch to the already-separated parallel-reuse
branch.  Moreover (6.7)--(6.8) give the pointwise cutoff

\[
 a_t(u)\le\min\{R_D(u),R_D(Ju)\}.                     \tag{6.15}
\]

There is also a product injection.  Each summand of `a_t(u)` is an ordered
pair `q,q-u in Q_{C,t}`.  Map it to the two labelled `D`-overlap
representations

\[
 (c-q,c-q+u),\qquad
 (\ell+Jq+Jt,\ell+Jq+Jt-Ju).                         \tag{6.16}
\]

For fixed `C`, the first pair recovers `q` and the second recovers
`p=q+t`, so the map is injective even after summing over all neighbour
fibres.  Hence

\[
 \boxed{\Lambda_2(C,x,u)\le R_D(u)R_D(Ju).}           \tag{6.17}
\]

This identifies the recursive pencil as an endpoint-decorated subpopulation
of the original perpendicular overlap energy.  Summing (6.17) naively over
centres would reintroduce the fatal core-size factor; the required argument
must use the nested-core mass or reverse endpoint rigidity before that sum.

That reverse rigidity now has an exact incidence form.  Put `H=ell+Jc`
and `X=c-q`.  An internal pair `q,q-u in Q_{C,t}` is equivalently

\[
\begin{gathered}
 X,X+u,\quad H-JX+Jt,H-JX+Jt-Ju,\\
 H-JX+Lt,H-JX+Lt-Ju\in D,                       \tag{6.17a}
\end{gathered}
\]

with the four popular corners and the condition that `x` is an endpoint of
`c+t` or `ell+Lt`.  After fixing one of the four oriented endpoint roles,
the possible `t` form an affine image of a subset of `A`, hence a vector-
Sidon set.  For fixed `X`, if `T_X` is the set of surviving `t`, then

\[
 D+D\supseteq \text{a translate of }JT_X+LT_X,
 \qquad |D+D|\ge {|T_X|^2\over2}.               \tag{6.17b}
\]

Indeed the energy equation `Jt_1+Lt_2=Jt_3+Lt_4` reduces to
`t_1-t_3=(I-J)(t_4-t_2)` and has at most `2|T_X|^2-|T_X|` solutions by
vector-Sidonicity.  Thus a high reverse degree creates a literal quadratic
support footprint.  It also exposes `|T_X|` distinct popular shifts
`p=c-X+t`, contributing more than `|T_X|K^2` to the original perpendicular
tail.  The still-missing step is to pack these footprints or popular
vertices across different `(C,x,u,X)` anchors.  See
`SWAP_ENDPOINT_REVERSE_STAR_INCIDENCE_GATE.md`.

Thus a subpolynomial bound for `Theta_2`, together with the linear parallel
wedge estimate, would close `Q_end`.  More generally, (6.10)--(6.17) are
the correct place to run a popular/nonpopular density increment; treating
`Q_end` as a free fourth moment loses both the same-neighbour cancellation
and the adaptive cutoff.

In particular, the two linear estimates

\[
 X_{\rm end},Q_{\rm end}\le K N^{o(1)}M              \tag{6.18}
\]

would imply `P_end<=2KN^{o(1)}M`.  This is the precise support/collision
replacement for the original endpoint-pencil gate.

## 7. Exact unification with the common-`r` triple

The cross-energy cell in Section 5 is exactly the correlated triple from
`SWAP_MATCHING_COMMON_R_SUPPORT_COLLISION_DICHOTOMY.md`, not merely an
analogy.  Take

\[
 q_1\in Q_{C,t_1},\qquad q_2\in Q_{C,t_2},\qquad
 d=t_1-t_2,\qquad \eta=q_1-q_2.                        \tag{7.1}
\]

The three moving `D` pairs in (5.2) have differences

\[
 -\eta,qquad
 v:=J(\eta+d),qquad
 v+d=J\eta+Ld.                                         \tag{7.2}
\]

Set

\[
 R=v+d,\qquad \Delta=-d.                              \tag{7.3}
\]

Then a direct calculation gives

\[
\boxed{
 R,\qquad R+\Delta,
 \qquad J(R+L\Delta)=-\eta\in D-D.}                   \tag{7.4}
\]

Thus every weighted endpoint-pencil copy pair is a fully represented
common-`r` triple.  Endpoint contact adds the raw signed difference (4.6),
while the clean codegree branch adds sixteen distinct cell endpoints; the
underlying affine support/collision key is the same `(R,Delta)`.

Equivalently, put `X=R` and `Y=R+Delta`.  Since `L=I+J`,

\[
 J(R+L\Delta)=X+(J-I)Y.                               \tag{7.5}
\]

Thus the shared unlabelled support is the fixed-coefficient Schur form

\[
 X,\qquad Y,\qquad X+(J-I)Y\in D-D,                   \tag{7.6}
\]

where `det(J-I)=2`.  This gives a clean Fourier/incidence normalization, but
the unlabelled count is deliberately not the target: the centre, endpoint,
popular-corner, and clean-label decorations are what distinguish the live
population from the affine countermodels.

For a fixed fibre pair, if

\[
 r_{t_1,t_2}(\eta)=
 |\{(q_1,q_2)\in Q_{C,t_1}\times Q_{C,t_2}:
 q_1-q_2=\eta\}|,
\]

then the three explicit representations in (7.2) give the cellwise cap

\[
\boxed{
 r_{t_1,t_2}(\eta)
 \le\min\{R_D(\eta),R_D(J(\eta+d)),R_D(J\eta+Ld)\}.}   \tag{7.7}
\]

The preferred remaining theorem is therefore one global, endpoint-decorated
packing estimate for (7.4).  It must combine distinct triple support with
repeated-key energy.  Treating endpoint contact and clean codegree by two
independent unlabelled `D-D` estimates would discard the strongest common
structure now available.

## 8. Exact stress

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

The exact copy-level profiles `(load, neighbour fibres, largest fibre,
distinct q, max q reuse, distinct p, max p reuse, difference-key support,
max key load)` for the largest pencils are

| family | profile |
|---|---:|
| Costas 23 | `(12,4,4,10,3,9,3,50,2)` |
| Costas 29 | `(22,4,6,12,4,12,3,121,4)` |
| Costas 31 | `(17,3,7,9,3,8,3,47,5)` |

Here the difference key includes the ordered endpoint-role pair and the raw
nonshared-endpoint difference `sigma`.  The support is already a substantial
fraction of the total pair mass, while
the remaining collision load is small and, by Section 5, lies entirely
inside fixed parallel-fibre pairs.

Globally, the exact `(P_end,X_end,Q_end)` support/collision rows are

| family | `P_end` | `X_end` | `Q_end` |
|---|---:|---:|---:|
| Costas 17 | 202 | 200 | 2 |
| Costas 23 | 70,261 | 67,245 | 3,140 |
| Costas 29 | 328,426 | 295,731 | 35,743 |
| Costas 31 | 118,933 | 106,127 | 14,952 |
| Costas 37 | 713,968 | 672,204 | 44,110 |

The second-generation switch rows `(sum P_2,sum Lambda_2,Theta_2,
W_parallel)` are

| family | row |
|---|---:|
| Costas 17 | `(4,3,320,1/2,428)` |
| Costas 23 | `(6,280,542,212,5/4,67,882)` |
| Costas 29 | `(71,486,2,012,372,23/8,251,614)` |
| Costas 31 | `(29,904,957,776,26/9,119,724)` |
| Costas 37 | `(88,220,5,293,108,11/6,661,754)` |
| closure 40 | `(212,72,056,2/3,9,184)` |
| closure 50 | `(12,7,232,1/2,932)` |

Here `sum P_2=2Q_end` exactly and `sum Lambda_2<=8W_parallel` is nearly
tight, while the load-bearing cancellation is the small local ratio
`Theta_2<3`.  This confirms that (6.11), rather than a raw internal-energy
sum, is the correctly normalized recursive quantity.  The maximum
off-largest-fibre loads in (6.12) are only `1,2,5,5` on Costas
`17,23,29,31`, respectively.

The sharper aggregate values are

| family | `G_2` | `G_2/W_parallel` |
|---|---:|---:|
| Costas 17 | 8 | 0.019 |
| Costas 23 | 11,748 | 0.173 |
| Costas 29 | 130,082 | 0.517 |
| Costas 31 | 53,196 | 0.444 |
| Costas 37 | 163,592 | 0.247 |

Thus the exact sufficient gate following (6.14) has constant-scale margin
on every current hard row, even though the cruder total-load estimate is
nearly saturated.

Splitting `sum P_2` by the adaptive status of the new shift `u` gives

| family | nonpopular `P_2` | popular `P_2` |
|---|---:|---:|
| Costas 17 | 0 | 4 |
| Costas 23 | 0 | 6,280 |
| Costas 29 | 24 | 71,462 |
| Costas 31 | 36 | 29,868 |
| Costas 37 | 72 | 88,148 |

Thus the low-tail part is already absent or negligible on the hard exact
rows.  The genuine survivor is the popular self-switch, precisely the
branch in which (6.13)--(6.15) retain both large orthogonal overlap factors.

The lifted modular-parabola equality model at prime 43 has

\[
 (P_{\rm end},X_{\rm end},Q_{\rm end})=(87,87,0),
 \qquad \Theta_2=0.
\]

So the ambient `m^2`-sharp construction lies entirely in distinct decorated
support and creates no recursive collision at all.  This is strong evidence
that the popular self-switch is a genuine obstruction branch rather than a
repackaging of the equality model that must survive the final theorem.

A small hostile affine-neighbourhood audit also separates the phenomenon
from accidental norm collisions.  Four additional genuine distance-Sidon
Welch images near the stored prime-11/17 transforms have exact
`(G_2,W_parallel,max residual)` rows

\[
 (0,20,0),\quad(0,0,0),\quad(0,476,0),\quad(0,84,0).
\]

This is only a finite kill-search, not asymptotic evidence, but it confirms
that Euclidean distance separation usually destroys the recursive
collision rather than inflating it.

Thus 89--99% of the exact pencil upper mass is already supported on
distinct decorated keys in these rows.  The collision term is not zero,
but it is much smaller and consists only of the four-copy rectangles
(6.5).  This is the first stress split that mirrors the common-`r`
support/collision dichotomy on the endpoint side without discarding copy
multiplicity.

## 9. Verification and next theorem

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_matching_weighted_endpoint_pencil.py
python3 phase2/loop/erdos1208/verify_swap_matching_weighted_endpoint_pencil.py --larger
python3 phase2/loop/erdos1208/verify_swap_endpoint_reverse_star_incidence.py
```

The verifier checks (1.3)--(2.2) on finite weighted endpoint systems,
proves (3.3)--(3.4) and (4.2)--(4.4) symbolically, checks (6.2)--(6.4)
exhaustively on small key-load systems, verifies the recursive-pencil and
product-injection identities, and reproduces the stored Costas and lifted-
parabola profiles.  The optional run checks Costas 37 and the two closure
rows.

The direct endpoint-contact theorem is now exactly (1.6).  A proof should
dyadically regularize the fibres `Q_{C,t}` in (5.2), use the Sidon rigidity
of their `t` indices, and split into large key support versus excessive
cross-energy within one fixed fibre pair.  In the latter branch it must
retain the two popular differences in (4.4) and the physical raw difference
from (4.6), then force two distinct complete-difference vectors of equal
Euclidean norm.  By Section 7 this should be combined with the clean
common-`r` population before any global support bound is applied.  The two
populations retain different endpoint decorations, but are governed by one
shared support/collision theorem rather than two unrelated `D-D` estimates.
