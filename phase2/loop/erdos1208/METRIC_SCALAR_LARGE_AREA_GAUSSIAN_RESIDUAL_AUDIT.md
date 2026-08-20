# Large-area scalar core: Gaussian residual branch and sharpness barrier

## 1. Verdict

Keep the four-distinct-edge scalar collision notation

\[
 |u|^2-|u'|^2+18(|v|^2-|v'|^2)=0,             \tag{1.1}
\]

with `u,u'` from one clean fibre of size `h` and `v,v'` from the full edge
set of size `N`.  Put

\[
 r_s=|u|^2-|u'|^2,\quad d_s=2\det(u,u'),
 \qquad
 r_t=|v|^2-|v'|^2,\quad d_t=2\det(v,v').       \tag{1.2}
\]

The Gaussian products from
`METRIC_SCALAR_CROSS_EDGE_DETERMINANT_BRANCH.md` are

\[
 Z_s=(u-u')\overline{(u+u')}=r_s-id_s,
 \qquad
 Z_t=(v-v')\overline{(v+v')}=r_t-id_t.         \tag{1.3}
\]

Equation (1.1) gives the exact residual identity

\[
 \boxed{Z_s+18Z_t=-i(d_s+18d_t).}              \tag{1.4}
\]

This yields a new rigorous branch.  In fact, for any fixed integers `A,B`
with `B!=0` and any finite `E subset Z`, the number of four-edge collisions
satisfying

\[
 A d_s+B d_t\in E
\]

is at most

\[
 \boxed{|E|m^{o(1)}h^2.}                      \tag{1.5}
\]

Taking `A=1,B=18` and `E=[-N/h,N/h]` proves

\[
 \boxed{
 T_q^{(4)}\bigl(|d_s+18d_t|\le N/h\bigr)
 \le m^{o(1)}hN.}                             \tag{1.6}
\]

Thus even collisions with two individually large signed areas are harmless
when their Gaussian residual nearly cancels.  The earlier low-target-area
theorem is the case `A=0,B=1`.

The branch is exponent-sharp.  There are genuine polynomial-height
distance-Sidon sets with a clean fibre `h=Theta(k)` for which

\[
 \boxed{
 T_{q,\mathrm{large}}^{(4),\mathrm{transverse}}
 \ge k^{3-o(1)},}                             \tag{1.7}
\]

where every counted collision has

\[
 |d_t|>N/h,qquad |d_s+18d_t|>N/h.             \tag{1.8}
\]

More strongly, the construction survives the low-diversity branch (1.5)
for any fixed finite menu of area projections.  Its parameters satisfy

\[
 N(h+k)=\Theta(k^3),                           \tag{1.9}
\]

so it matches the required weak scalar bound up to a subpolynomial factor;
it does not disprove that bound.

This closes the hoped-for shortcut.  Gaussian products and determinant
incidence can delete low-diversity area projections, but the surviving
large-area core is genuinely allowed to have the full target exponent.
Any proof must use the sharp `m^(o(1))` constant-scale endpoint theorem, not
a polynomial saving from area largeness itself.

## 2. The projected-area completion theorem

### Theorem 2.1

Let `C` be the set of ordered four-distinct-edge collisions in one scalar
charge fibre problem.  For fixed integers `A,B` with `B!=0`, define

\[
 \ell(c)=A d_s(c)+B d_t(c).
\]

Then for every finite integer set `E`,

\[
 |\{c\in C:\ell(c)\in E\}|
 \le |E|m^{o(1)}h(h-1).                       \tag{2.1}
\]

### Proof

Fix the ordered source pair `(u,u')`.  It fixes `r_s,d_s`, while the scalar
equation fixes

\[
 r_t=-r_s/18.                                  \tag{2.2}
\]

If this is not integral there is no completion.  For a fixed `e in E`, the
area projection also fixes

\[
 d_t={e-A d_s\over B}.                         \tag{2.3}
\]

Again, a nonintegral value gives no completion.  Otherwise the fixed
radius-difference/signed-area lemma gives only `m^(o(1))` ordered target
edge pairs with invariants `(r_t,d_t)`.  Here `r_t!=0`, because the two
target edge labels are distinct and all squared distances are globally
unique.  Summing over `E` and the at most `h(h-1)` source pairs proves
(2.1).  QED.

The result is translation invariant in the area coordinate: any set of at
most `N/h` residual values is harmless, not only a centered interval.
Consequently a polynomial failure of the scalar gate must occupy more than
`N/h` values of every fixed projected area used in this way.

For the Gaussian choice `(A,B)=(1,18)`, equation (1.4) says that the
projected area is precisely the remaining imaginary coordinate after the
real scalar coordinate has cancelled.

## 3. Why large area itself gives no saving

Fixing both `r_t` and `d_t` makes the Gaussian factorization divisor-rigid,
but fixing only `r_t` need not.  A simple radial-unique vector model already
shows the obstruction.

For positive integers `C,t`, put

\[
 v_t=(C,t),\qquad v'_t=(C+2,t).                \tag{3.1}
\]

Then

\[
 |v_t|^2-|v'_t|^2=-4(C+1),
 \qquad 2\det(v_t,v'_t)=-4t.                  \tag{3.2}
\]

Choose `t` in an interval whose successive square gaps exceed `4(C+1)`.
Then all the norms in the two families in (3.1) are distinct, yet one fixed
radius difference has arbitrarily many completions and every determinant
can be arbitrarily large.  The fixed-`(r,d)` divisor theorem is sharp about
which two coordinates must be retained; summing `d` cannot gain merely
from the condition `|d|>L`.

The next section strengthens this formal obstruction to a genuine clean
endpoint family at the exact weak-target scale.

## 4. Genuine clean-endpoint sharpness construction

Let

\[
 D_X=\{n\le X:n=x^2+y^2\text{ for some }x,y\in\mathbb Z\},
 \qquad R=|D_X|.                               \tag{4.1}
\]

The Landau--Ramanujan theorem gives

\[
 R=X(\log X)^{-1/2+o(1)}.                     \tag{4.2}
\]

Choose one integral vector `w_n` of norm `n` for every `n in D_X`.  The
scalar label energy satisfies the range lower bound

\[
 \begin{aligned}
 E(D_X,18D_X)
 &=\sum_z|\{(a,b)\in D_X^2:a+18b=z\}|^2\\
 &\ge {R^4\over19X+1}
 =R^{3-o(1)}.                                  \tag{4.3}
 \end{aligned}
\]

We now install these labels as genuine clean starts.  Fix anchors `a,b`
with an even difference `q=a-b`.  For each `n`, choose free integral
parameters `P_n,z_n` and introduce

\[
\begin{aligned}
 c_n&=P_n+S w_n,&d_n&=P_n-S w_n,\\
 e_n&=P_n+q/2+z_n,&f_n&=P_n+q/2-z_n.           \tag{4.4}
\end{aligned}
\]

Then

\[
 c_n+d_n+q=e_n+f_n,                            \tag{4.5}
\]

so every `c_n+d_n` is a clean `q`-start, and its source edge has squared
length `4S^2n`.  Use the same source edges as an `R`-edge subset of the
ordinary target set.  Multiplication of every controlled label by `4S^2`
does not change the energy in (4.3).

The free parameters can be chosen so that the full point set is
distance-Sidon and these are exactly the clean `q`-starts.  Indeed, every
unwanted equality of two squared distances is a nonzero polynomial in the
free coordinates, and every unwanted pair-sum translate is a nonzero
linear polynomial.  The intended source distances are already distinct.
The product of the finitely many forbidden polynomials is nonzero; evaluation
on an integer grid larger than its degree gives a nonvanishing integral
choice.  There are polynomially many conditions of bounded degree, so the
height remains polynomial in `R` and `X`.

The resulting set has

\[
 k=4R+2,qquad h=R,qquad N=\binom k2=\Theta(R^2).          \tag{4.6}
\]

It remains to locate the energy inside the exact surviving core.  The
following deletions cost only `R^(2+o(1))`:

1. collisions using fewer than four edge labels, by the repeated-label
   proposition;
2. collisions staying in one source squareclass and one target
   squareclass, by the squareclass-resonant theorem;
3. collisions with `d_t=0`, by Theorem 2.1 with `E={0}`; and
4. collisions with `A_jd_s+B_jd_t=0` for any fixed finite list of
   projections with `B_j!=0`, again by Theorem 2.1.

Subtracting these from (4.3) leaves `R^(3-o(1))` four-edge,
squareclass-transverse collisions with nonzero target determinant and with
every selected area projection nonzero.

Finally choose the common integer scale `S=R`.  Every doubled area and
every projected area in the controlled subsystem is multiplied by `S^2`.
Since

\[
 N/h=\Theta(R),                               \tag{4.7}
\]

every surviving nonzero value is larger than `N/h` for all sufficiently
large `R`.  This proves (1.7)--(1.8), and proves the stronger finite-menu
claim.  Polynomial scaling preserves polynomial height.

The construction is the cleanly dressed projection model from
`METRIC_MATRIX_PROJECTION_INVERSE_AUDIT.md`, with the determinant scale and
all previous core deletions now audited explicitly.

## 5. Exact stress profiles

For the stored genuine families, let `L=floor(N/h)`.  The verifier reports

\[
 (T^{(4)},\ |d_t|\le L,\ |d_s+18d_t|\le L,
   \text{union deleted},\ \text{survivors}).
\]

\[
\begin{array}{c|r|r|r|r|r}
\text{family}&T^{(4)}&\text{low target}&\text{low residual}
 &\text{union}&\text{survivors}\\ \hline
\text{closure }30&252&4&0&4&248\\
\text{closure }40&2648&82&4&86&2562\\
\text{closure }80&22474&190&8&198&22276\\
\text{closure }120&116938&448&10&458&116480\\
\text{source }45&830&22&0&22&808\\
\text{perpendicular ruler }40&18&10&10&10&8\\
\text{Costas }22&514&0&0&0&514\\
\text{parabola image }43&2708&50&44&90&2618\\
\text{two-arm }50\text{ restricted}&612&612&612&612&0
\end{array}                                                    \tag{5.1}
\]

The Gaussian residual branch is exact but deletes little of the generic
closure core.  It completely absorbs the one-dimensional two-arm subsystem,
where both area coordinates vanish.

The verifier also builds a deterministic 98-point genuine dressed example
from the 24 sums of two squares at most `50`.  It has exactly 24 clean
starts for the planted `q`, full edge count `N=4753`, and controlled energy

\[
 (h^2,\mathcal E,\mathcal E-h^2)=(576,736,160).             \tag{5.2}
\]

Of the 160 off-diagonal controlled collisions, 16 use three edge labels.
All remaining 144 are four-edge, squareclass-transverse, have
`|d_t|>floor(N/h)=198`, and have
`|d_s+18d_t|>198`.  This is a finite exact shadow of the asymptotic
sharpness construction.

Run

```text
python3 phase2/loop/erdos1208/verify_metric_scalar_large_area_gaussian_residual_audit.py
```

for the factor identities, genuine profiles, and dressed certificate.

## 6. Consequence

The determinant route now has a precise endpoint:

* low target area is divisor-small;
* low Gaussian residual, and more generally every low-diversity fixed area
  projection, is divisor-small;
* nevertheless the complementary large-area, residual-large core can have
  `k^(3-o(1))` genuine clean-endpoint collisions.

That last quantity is exactly the weak budget `N(h+k)` in the planted
`h=Theta(k)` regime.  Therefore area incidence alone cannot yield a power
saving.  A full proof must exploit the heavy-fibre regime `h>>k`, where the
planted construction is paid by the `+k` term and endpoint reuse becomes
unavoidable.
