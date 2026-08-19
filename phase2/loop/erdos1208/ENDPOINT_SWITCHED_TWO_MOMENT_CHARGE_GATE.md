# Endpoint-switched charges for the two popular-pair moments

## 1. Outcome

Keep the notation of `POPULAR_PAIR_RECTANGLE_MOMENT_GATE.md`.  Thus

\[
 D=A-A,\qquad N=|D|,\qquad S=|D+D|,
\]

`P` is the support-adaptive popular set, and for an ordered distinct pair
`z=(q,q') in P^2` we have

\[
 A_z=\{a:a,a+q,a+q'\in D\},\qquad
 B_z=\{d:d,d-Jq,d+q-q',d+q-q'-Jq'\in D\}.
\]

Write `alpha_z=|A_z|` and `beta_z=|B_z|`.  The remaining moment product is

\[
 \left(\sum_z\alpha_z^2\right)
 \left(\sum_z\beta_z^2\right)
 \le N^{2+o(1)}S^2.                              \tag{1.1}
\]

This note gives each factor a canonical charge whose target has exactly the
size required by (1.1): a constant number of labelled copies of
`D times (D+D)`.  Both charges combine one literal complete difference with
one endpoint-midpoint difference.  The beta charge routes its only
noninvertible common-endpoint stratum to `D^2`, which is no larger because
`N<=S`.  The resulting size-biased load product is a sufficient theorem for
the full cube-root order.

The load theorem is **not proved here**.  What is proved is the exact charge
factorization, its target size, its reconstruction formulas, and its formal
implication for (1.1).  Exact complete-difference stresses have near-unit
size-biased loads.  Abstract radial impostors do not possess the endpoint
decoration required to define either hybrid charge.

## 2. The endpoint midpoint decoration

Every nonzero `d in D` has a unique ordered representation

\[
 d=x_d-y_d,\qquad x_d,y_d\in A,                  \tag{2.1}
\]

because `A` is distance-Sidon.  Define

\[
 m(d)=x_d+y_d.                                   \tag{2.2}
\]

For zero, fix one `a_* in A` and put `m(0)=2a_*`.  In every case
`m(d) in A+A`.  Moreover

\[
 (A+A)-(A+A)=A+A-A-A=D+D.                       \tag{2.3}
\]

Thus every difference of two decorated midpoints belongs to the ordinary
support `D+D`.  Notice that the popular shifts `q,q'` need not themselves
belong to `D`; they are never decorated.  This avoids an invalid hidden
hypothesis in an earlier exploratory search.

There is an exact endpoint switch.  If `d=x_d-y_d` and `e=x_e-y_e`, put

\[
 \sigma_+(d,e)={m(d)-m(e)+d-e\over2}=x_d-x_e,
 \qquad
 \sigma_-(d,e)={m(d)-m(e)-d+e\over2}=y_d-y_e.   \tag{2.4}
\]

Both switched values belong to `D`, including when `d` or `e` is zero under
the fixed zero decoration.  Conversely, if both switched values are
nonzero, their unique ordered endpoint representations recover `d` and `e`.
The only failure is when one switch is zero, equivalently
`m(d)-m(e)=+(d-e)` or `m(d)-m(e)=-(d-e)`; geometrically the two decorated
edges share an endpoint.

There is a second small rigidity fact that will be useful in any load proof.
For nonzero `s,t in D`, write their endpoint decorations as
`s=x_s-y_s,t=x_t-y_t`.  If

\[
 C=s+t,\qquad V=x_s-x_t\ne0,                    \tag{2.5}
\]

then `(C,V)` determines `(s,t)` up to at most two ordered possibilities.
Indeed `V` recovers the ordered pair `(x_s,x_t)`.  The sum
`y_s+y_t=x_s+x_t-C` then recovers the unordered pair `{y_s,y_t}`, because a
distance-Sidon set is also additive Sidon; only its two assignments remain.
Thus a large hybrid load cannot come from repeatedly reusing the same
endpoint-head difference.

## 3. Alpha: a cyclic maximal midpoint charge

An ordered contribution to `alpha_z^2` is a pair `a,b in A_z`.  Arrange its
six differences as

\[
\begin{matrix}
 d_0=a&d_1=a+q&d_2=a+q'\\
 d_3=b&d_4=b+q&d_5=b+q'.
\end{matrix}                                     \tag{3.1}
\]

Define the three cyclic crossed differences

\[
 c_0=m(d_0)-m(d_4),\qquad
 c_1=m(d_1)-m(d_5),\qquad
 c_2=m(d_2)-m(d_3).                              \tag{3.2}
\]

Order their indices by decreasing squared norm, breaking ties by the smaller
index, and let `(i,j)` be the first two indices.  Associate the pairs

\[
 (e_0,f_0)=(d_0,d_4),\quad
 (e_1,f_1)=(d_1,d_5),\quad
 (e_2,f_2)=(d_2,d_3),
\]

For each `r in {i,j}`, let `ell_r in {+,-}` select the larger of
`sigma_+(e_r,f_r),sigma_-(e_r,f_r)`, breaking a tie by a fixed order.  If
all four switches belonging to the selected cyclic pairs are nonzero, put

\[
 \Theta_\alpha(z,a,b)=
 (0,i,j,\ell_i,\ell_j,c_i,\sigma_{\ell_j}(e_j,f_j))
 \in\{0,1,2\}^2\times\{+,-\}^2\times(D+D)\times D. \tag{3.3}
\]

If the unselected switch of pair `j` is zero, replace the last coordinate by
the larger literal member of `(e_j,f_j)`.  Otherwise, if pair `i` has a zero
switch, replace the last two coordinates by the selected switch of pair `j`
and the larger literal member of `(e_i,f_i)`.  Record the route and literal
role.  Both common-endpoint routes still lie in `(D+D) times D`, because
`D subset D+D`.  Only six ordered distinct `(i,j)` occur.  There are at most
24 normal labels and 48 on each exceptional route, so the target has at most
`120NS` elements.  Let `lambda_alpha` be its load.  Then, exactly,

\[
 A_2:=\sum_z\alpha_z^2
     =\sum\lambda_\alpha.                        \tag{3.4}
\]

The cyclic crossed choice is not cosmetic.  The same-column charges
`(m(d_0)-m(d_3),m(d_1)-m(d_4))` have polynomially larger loads on the
determinant-prime Costas stresses.  Keeping only the fixed pair `(c_0,c_1)`
also creates high-load strata when either coordinate vanishes.  The maximal
cyclic rule retains the two switchings needed to distinguish the rows while
moving away from those strata whenever another cyclic difference is
available.  The literal switched difference in `D` retains one complete
endpoint pair without paying for a second copy of `D+D`; the two separate
routes remove every zero switch.  Thus every normal key has four nonzero
switches, and both selected pairs are exactly recoverable from them.

Put

\[
 Q_\alpha=\sum\lambda_\alpha^2,
 \qquad L_\alpha=Q_\alpha/A_2.                   \tag{3.5}
\]

Since the combined target has at most `120NS` elements,
Cauchy--Schwarz gives

\[
 A_2^2\le120NSQ_\alpha,
 \qquad A_2\le120NSL_\alpha.                   \tag{3.6}
\]

Every two cyclic pairs retain a four-entry reconstruction.  For roles
`(0,1)`, the four values `(d_0,d_4,d_1,d_5)` determine

\[
 d_2=d_1+d_5-d_4,\qquad d_3=d_0+d_4-d_1.        \tag{3.7}
\]

For roles `(0,2)`, the values `(d_0,d_4,d_2,d_3)` determine

\[
 d_1=d_0+d_4-d_3,\qquad d_5=d_3+d_2-d_0,        \tag{3.8}
\]

and for roles `(1,2)`, the values `(d_1,d_5,d_2,d_3)` determine

\[
 d_0=d_2+d_3-d_5,\qquad d_4=d_1-d_2+d_5.        \tag{3.9}
\]

Thus a fixed alpha charge is a coupled pair of endpoint-midpoint fibres,
with the two cross-memberships in (3.7)--(3.9) retained.  Dropping those two
memberships returns to the previously disproved unrestricted midpoint
charge.

## 4. Beta: a diagonal-switched maximal-role charge

Put `L=I+J`.  For `d in B_z`, write

\[
 x_0=d,\quad x_1=d+q-q',\quad x_3=d-Jq,
 \quad x_2=x_3+L(x_1-x_0).                       \tag{4.1}
\]

All four values lie in `D`.  An ordered contribution to `beta_z^2` is a
pair `d,e in B_z`; if `h=e-d`, put

\[
 y_i=x_i+h\quad(0\le i<4).                       \tag{4.2}
\]

Again all eight values lie in `D`.

Every role has a canonical partner on one of the two guaranteed popular
edges:

\[
 \pi(0)=3,\quad\pi(3)=0,\quad
 \pi(1)=2,\quad\pi(2)=1.                         \tag{4.3}
\]

Indeed the corresponding displacement is one of `Jq,-Jq,Jq',-Jq'`, hence
lies in `P`.

Distance-Sidonicity makes the squared norms of the elements of `D` distinct
up to antipodes.  Break antipodal ties by the smaller role.  When `d!=e`,
let `i` and `j` be the maximal roles in the `x` and `y` rows and set

\[
 u=x_i,\qquad v=y_j,\qquad w=y_{\pi(j)}.          \tag{4.4}
\]

When `d=e`, the two rows coincide.  Charging the duplicated pair `(x_i,x_i)`
creates the whole high-load diagonal stratum.  Instead, let `i,j` be the
largest and second-largest roles in the single row and put

\[
 u=x_i,\qquad v=x_j,\qquad w=x_{\pi(j)}.          \tag{4.5}
\]

In either case define

\[
 c=m(v)-m(w)\in D+D,\qquad t=v-w\in P.           \tag{4.6}
\]

If `c` is different from both `t` and `-t`, charge the configuration to the
labelled pair `(u,c) in D times (D+D)`.  If `c=t` or `c=-t`, one endpoint
switch in (2.4) is zero; route exactly this common-endpoint stratum to the
labelled literal pair `(u,v) in D^2`.  The labels record whether the rows
coincide, which route was used, and `(i,j)`.

For a fixed `z` and fixed labels, this charge is injective in `(d,e)`.  The
value `u` recovers `d`.  On the literal route, `v` recovers `e`.  On the
midpoint route, the known `t` and charged `c` recover the two nonzero
switches `(c+t)/2,(c-t)/2`.  Their unique endpoint decorations recover
`v,w`, and hence `e`.  In the diagonal case `u` already recovers the one
row.  Thus every nontrivial load is purely cross-`z`.

Let `lambda_beta` be its load and put

\[
 B_2:=\sum_z\beta_z^2=\sum\lambda_\beta,
 \quad Q_\beta:=\sum\lambda_\beta^2,
 \quad L_\beta:=Q_\beta/B_2.                    \tag{4.7}
\]

There are at most 28 role labels on each route.  Since `N<=S`, the combined
target has size at most `28NS+28N^2<=56NS`.  Therefore

\[
 B_2^2\le56NSQ_\beta,
 \qquad B_2\le56NSL_\beta.                     \tag{4.8}
\]

### 4.1 Exact fixed-key form

Take an off-diagonal midpoint-route charge with roles `(i,j)=(0,2)`.  Its
fixed values are `u=x_0` and

\[
 c=m(y_2)-m(y_1).
\]

Put

\[
 r=q-q',\qquad p=q'.                             \tag{4.9}
\]

Here `t=y_2-y_1=-Jp`.  Therefore the two endpoint switches are

\[
 a_p={c-Jp\over2},\qquad b_p={c+Jp\over2}.       \tag{4.10}
\]

They are nonzero elements of `D`.  Write their unique endpoint decorations
as `a_p=x_{a_p}-y_{a_p}` and `b_p=x_{b_p}-y_{b_p}`.  Then the charged
midpoint difference and the known spoke recover

\[
 V_c(p)=x_{a_p}-x_{b_p}=y_2,
 \qquad W_c(p)=y_{a_p}-y_{b_p}=y_1.              \tag{4.11}
\]

With `v=V_c(p)`, the eight entries are exactly

\[
\begin{array}{llll}
 x_0=u,&x_1=u+r,&x_3=u-J(r+p),&x_2=u+r-Jp,\\
 y_0=v-r+Jp,&y_1=v+Jp,&y_2=v,&y_3=v-Lr.
\end{array}                                      \tag{4.12}
\]

The popularity restrictions are `p,r+p in P`.  For two preimages of the
same key put

\[
 \rho=r'-r,\qquad \pi=p'-p,
 \qquad \eta=V_c(p')-V_c(p).                    \tag{4.13}
\]

The seven uncharged form displacements are

\[
 \rho,\quad-J(\rho+\pi),\quad\rho-J\pi,
 \quad\eta-\rho+J\pi,\quad\eta+J\pi,
 \quad\eta,\quad\eta-L\rho.                     \tag{4.14}
\]

Unlike the old literal-pair charge, `eta` is not free: (4.10)--(4.11) force
it through four uniquely decorated complete differences.  This is the new
endpoint constraint retained by the hybrid charge.  The maximal-role rule
also retains the six rowwise norm inequalities.  On the common-endpoint
route, `u,v` are fixed instead and the earlier six linear displacements are
recovered by setting `eta=0` in the corresponding literal-key formulas.

## 5. A single sufficient load-product theorem

Combining (3.6) and (4.8) gives

\[
 A_2B_2\le6720N^2S^2L_\alpha L_\beta.           \tag{5.1}
\]

Consequently the following statement is sufficient for (1.1), and hence
for the cube-root order of Erdős problem 1208:

> **Endpoint-switched two-load theorem.**  For every planar lattice
> distance-Sidon set, with the support-adaptive popular set `P`,
> \[
> L_\alpha L_\beta=N^{o(1)}.                    \tag{5.2}
> \]

The stronger pair `L_alpha=N^{o(1)}` and `L_beta=N^{o(1)}` also suffices,
but (5.2) allows compensation between the midpoint and rotated sides.  This
is strictly more flexible than proving the two raw moment bounds separately.

## 6. Exact stress profiles

`verify_endpoint_switched_two_moment_charge.py` checks all identities above.
The key exact profiles are

\[
\begin{array}{c|r|r|r|r}
&\text{mass}&\text{charge image}&\text{charge second moment}&\max\lambda\\ \hline
\alpha,\ \text{closure }40&2,744,348&2,524,398&3,303,104&16\\
\alpha,\ \text{Costas }23&2,294,322&2,085,894&2,763,502&7\\
\beta,\ \text{closure }40&104,948&96,590&133,192&11\\
\beta,\ \text{Costas }23&250,722&225,272&310,190&7
\end{array}                                      \tag{6.1}
\]

Thus the four size-biased loads in (6.1) are respectively

\[
 1.2036\ldots,\quad1.2044\ldots,\quad
 1.2691\ldots,\quad1.2371\ldots.                \tag{6.2}
\]

The optional `--extended` verifier checks that the determinant-prime rows
through `p=41` remain at the same constant scale:
the two loads at `p=41` are `1.2076...` and `1.3215...`.  The old dense
Sidon-ruler midpoint obstruction has empty adaptive tail, so it contributes
no charge at all.  The abstract radial impostors cannot even be supplied to
these maps: both hybrid charges require the canonical complete-difference
endpoint decoration.  This is structural evidence, not a proof of (5.2).

## 7. Next proof target

The next useful theorem should not rely only on a maximum load: exceptional
keys still grow while the size-biased load stays bounded.  It should instead
charge ordered collisions of either map to lower-radius endpoint switchings,
or prove the product form (5.2) directly.  For beta, the endpoint-forced
system (4.9)--(4.14) and the maximal-radius inequalities must remain present.
For alpha, both the endpoint switch (2.4) and cross-memberships
(3.7)--(3.9) are load-bearing; deleting them is the known Sidon-ruler failure
mode.
