# Low-band scalar tail: localization to one physical endpoint wedge

> **Status update.**  The localization identity in this note is correct,
> but its proposed pointwise gate is false.  The polynomial-height
> rich-pencil construction in
> `LOW_BAND_FIXED_WEDGE_RICH_PENCIL_COUNTEREXAMPLE.md` has
> `F_(N,k)(w)=Omega(k^2)` while every planted shift satisfies `U_N(r)>=k`.

## 1. Outcome

For a nonnegative determinant cutoff `L`, the joint endpoint-wedge moment

\[
 J_L=\sum_{r\ne0}R_D(-18r)W_{r,L}                        \tag{1.1}
\]

admits an exact localization over the `O(k^3)` *physical* endpoint wedges
of the complete graph on `A`.  For a physical wedge

\[
 w=(x;\{x,a_1\},\{x,a_2\}),                              \tag{1.2}
\]

define an explicit scalar weight `F_L(w)` in Section 2.  Then

\[
 \boxed{J_L=\sum_wF_L(w).}                                \tag{1.3}
\]

There are exactly

\[
 k{k-1\choose2}={k(k-1)(k-2)\over2}                      \tag{1.4}
\]

physical wedges.  Consequently the pointwise theorem

\[
 \boxed{F_L(w)\le m^{o(1)}k\quad\hbox{for every }w}       \tag{1.5}
\]

would imply

\[
 J_L\le m^{o(1)}Nk^2,                                    \tag{1.6}
\]

and therefore finish the entire low-codegree band.  It is enough, and
possibly more natural, to prove (1.5) after retaining only shifts with
`U_L(r)>=T`; this restricted pointwise form proves the dyadic tail directly.

The initially found stress family showed that the linear scale could not be
improved: there are genuine polynomial-height integral distance-Sidon sets
and physical wedges with

\[
 \boxed{F_N(w)\ge k-O(1),}                                \tag{1.7}
\]

where every retained target determinant exceeds `N`.  The later
perpendicular rich-pencil construction strengthens this decisively to

\[
 \boxed{F_{N,k}(w)=\Omega(k^2)}                           \tag{1.8}
\]

at polynomial height and with `U_N(r)>=k` for every planted shift.  Hence
(1.5), including its rich-restricted version, is false.  The contribution
of this note that survives is the exact identity (1.3) and its scalar
bookkeeping; it is a localization formula, not a pointwise proof route.

## 2. Exact fixed-wedge formula

Let the two first edges of (1.2) have squared-distance labels

\[
 A_1=\delta(xa_1),\qquad A_2=\delta(xa_2),\qquad
 g=A_1-A_2.                                               \tag{2.1}
\]

Let `v_1,v_2` be canonical displacement vectors of these first edges.
For an ordered partner-edge pair `(f_1,f_2)`, write `u_i` for the canonical
displacement of `f_i`.  Define

\[
 \mathcal P_L(w)=
 \left\{(f_1,f_2):
 \begin{array}{l}
 \delta(f_1)-\delta(f_2)=g,\\
 |2\det(v_1,u_1)|>L,\\
 |2\det(v_2,u_2)|>L
 \end{array}\right\}.                                    \tag{2.2}
\]

For every member of (2.2), put

\[
 r=A_1-\delta(f_1).                                       \tag{2.3}
\]

The gap equation in (2.2) also gives

\[
 r=A_2-\delta(f_2).                                       \tag{2.4}
\]

The fixed-wedge weight is

\[
 \boxed{
 F_L(w)=\sum_{(f_1,f_2)\in\mathcal P_L(w)}
 R_D\bigl(-18(A_1-\delta(f_1))\bigr).}                   \tag{2.5}
\]

This formula retains three pieces which were collapsed by the ordinary
line-incidence rewrite:

1. the physical first-edge wedge `w`;
2. the absolute partner label `delta(f_1)`, not merely the partner gap `g`;
3. the opposite source scale `-18r`.

## 3. Proof of the localization identity

Fix `r`.  An endpoint wedge counted by `W_(r,L)` consists of two records

\[
 (\{x,a_1\},f_1),\qquad(\{x,a_2\},f_2)                    \tag{3.1}
\]

with

\[
 A_1-\delta(f_1)=A_2-\delta(f_2)=r.                      \tag{3.2}
\]

Subtracting (3.2) gives (2.2), and the determinant qualifications in
`W_(r,L)` give the last two conditions there.  Thus (3.1) contributes
`R_D(-18r)` to exactly one summand of (2.5).

Conversely every partner pair in (2.2) defines the common shift (2.3)--
(2.4), so it gives one determinant-qualified target wedge at `r`, weighted
by `R_D(-18r)`.  Two distinct first edges have at most one common endpoint,
so there is no double counting.  Summing over all physical wedges proves
(1.3).

If (1.5) holds, (1.3)--(1.4) give

\[
 J_L
 \le m^{o(1)}{k^2(k-1)(k-2)\over2}
 <m^{o(1)}Nk^2,                                            \tag{3.3}
\]

which is (1.6).  The previous endpoint theorem then gives, for `T>=k`,

\[
 \sum_{r:U_L(r)\ge T}R_D(-18r)
 \le {kJ_L\over T^2}
 \le {m^{o(1)}Nk^3\over T^2}
 \le {m^{o(1)}Nk^2\over T}.                              \tag{3.4}
\]

Since `H_*+k^3>=k^3`, the last expression is at most the required
`m^(o(1))N(H_*+k^3)/(kT)` scale.

For the exact dyadic restriction, define

\[
 F_{L,T}(w)=
 \sum_{\substack{(f_1,f_2)\in\mathcal P_L(w)\\
                   U_L(A_1-\delta(f_1))\ge T}}
 R_D\bigl(-18(A_1-\delta(f_1))\bigr).                    \tag{3.5}
\]

The same proof gives

\[
 \sum_{r:U_L(r)\ge T}R_D(-18r)W_{r,L}
 =\sum_wF_{L,T}(w).                                       \tag{3.6}
\]

Thus the weaker uniform estimate `F_(L,T)(w)<=m^(o(1))k` is already
sufficient.

## 4. What the local gate still contains

The partner pairs in (2.2) form the complete distance-gap cell at the
single gap `g=A_1-A_2`.  If their first labels are denoted by

\[
 C_g=\{\delta(f_1):(f_1,f_2)\in\mathcal P_L(w)\},         \tag{4.1}
\]

then (2.5) is the restricted affine correlation

\[
 F_L(w)=\sum_{c\in C_g}R_D(-18(A_1-c)).                   \tag{4.2}
\]

The values `c` are distinct because one edge norm determines the other in
a fixed nonzero gap.  Formula (4.2) shows the precise remaining difficulty:
a fixed distance-gap representation set must not align too strongly, after
an affine dilation by `-18`, with another distance-gap population.

Neither uniqueness of directed edge vectors nor fixed-`(g,d)` Gaussian
factorization bounds (4.2).  The latter bounds the number of partner pairs
after their mutual determinant is fixed; (2.2) instead imposes two cross
determinants against the fixed wedge vectors and then sums over all absolute
partner norms.  A proof of (1.5) needs a genuinely local radial-difference
theorem, not another count of the supporting line from the previous audit.

## 5. First polynomial-height linear stress family

Fix a parameter `s` and put

\[
 C=s^3+10,qquad
 a=18(C+1)+1,qquad b=18(C+1)-1.                          \tag{5.1}
\]

Then

\[
 z=a^2-b^2=72(C+1),qquad r=-4(C+1),qquad z=-18r.       \tag{5.2}
\]

Take the two horizontal points

\[
 A_0=(a,0),\qquad A_1=(b,0),                              \tag{5.3}
\]

and `s` vertical points

\[
 Y_i=(0,Q+t_i),                                           \tag{5.4}
\]

where the `t_i` form a polynomial-span Golomb ruler.  For every `i`,

\[
 |A_0-Y_i|^2-|A_1-Y_i|^2=a^2-b^2=z.                     \tag{5.5}
\]

Hence `R_D(z)>=s`.

The offset `Q` can be chosen with polynomial size so that (5.3)--(5.4) are
distance-Sidon.  Internal distances are already different after a fixed
scale of the ruler.  Two different cross-distance polynomials in `Q` have
different linear coefficients unless they use the same `Y_i`; in that case
their constant terms distinguish `a` and `b`.  Cross/internal equalities
are also nonzero quadratic polynomials.  There are polynomially many bad
values, so a polynomial grid contains an admissible `Q`.

Independently, at one point `Z`, plant two first-edge vectors

\[
 v_i=(C,T_i),\qquad i=1,2,                                \tag{5.6}
\]

and, at free centres, their partner vectors

\[
 u_i=(C+2,T_i).                                           \tag{5.7}
\]

Then

\[
 |v_i|^2-|u_i|^2=r,qquad |2\det(v_i,u_i)|=4|T_i|.       \tag{5.8}
\]

Choose polynomial-size `T_i>N/4` and use finite avoidance for every
unintended distance equality between the source and target gadgets.  The
resulting integral set is distance-Sidon and has polynomial height.  Its
point count is

\[
 k=(s+2)+(1+2+4)=s+9.                                    \tag{5.9}
\]

Let `w` be the physical wedge formed by the two first edges at `Z`.  Its
two partner edges give one member of `P_N(w)` at shift `r`.  Equations
(5.2), (5.5), and (2.5) yield

\[
 \boxed{F_N(w)\ge R_D(z)\ge s=k-9.}                      \tag{5.10}
\]

Thus the first construction already ruled out a sublinear estimate, even
with determinant cutoff `N` and polynomial height.

This construction stresses only the all-gap pointwise gate: its planted
target cell has two records.  The later rich-pencil construction closes the
former loophole by giving `U_N(r)>=k` and quadratic fixed-wedge weight.

## 6. Exponential-height quadratic stress

The sharp target-pencil family from
`LOW_BAND_TWO_SCALE_ENDPOINT_INCIDENCE_AUDIT.md` takes a quadratic-gap
source ruler with

\[
 R_D(-18r)=\Theta(k^2)                                    \tag{6.1}
\]

and an independent determinant-qualified target star at `r`.  Every
physical wedge in that star has only its planted partner pair, so (2.5)
gives

\[
 F_N(w)=\Theta(k^2).                                      \tag{6.2}
\]

That ruler has height exponential in `k`: producing linearly many
difference-of-squares factorizations of one fixed integer requires a
divisor-rich integer.  Thus (6.2) rules out a height-free `O(k)` theorem but
is compatible with (1.5).  It also explains why the `m^(o(1))` cannot be
deleted casually.

## 7. Exact finite audit

For cutoff `L=N`, the verifier reports

\[
 (\#\{w:F_N(w)>0\},\ J_N,\ \max_wF_N(w))                 \tag{7.1}
\]

as

\[
\begin{array}{c|rrr}
\text{family}&\#w&J_N&\max F_N\\ \hline
\text{closure }20&1911&37904&173\\
\text{Costas }22&1893&9839&34\\
\text{parabola }43&184&276&5\\
\text{perpendicular ruler }40&894&1012&21
\end{array}                                               \tag{7.2}
\]

After restricting to gaps with `U_N(r)>=k`, only closure 20 is nonempty;
its restricted `(number of wedges, mass, maximum weight)` is

\[
 (811,10542,76).                                          \tag{7.3}
\]

The polynomial-height sharp certificate has `k=17,N=136` and

\[
 (z,r,R_D(z),U_N(r),\max_wF_N(w))
 =(37656,-2092,8,2,8).                                   \tag{7.4}
\]

All 136 squared distances and pair sums are distinct.  Only one physical
wedge has positive scalar weight, so `J_N=8` exactly.

Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_low_band_fixed_wedge_weight.py
```

## 8. The pointwise route is closed

The rich-pencil counterexample gives, at polynomial height,

\[
 F_{N,k}(w)=\Omega(k^2)                                  \tag{8.1}
\]

and therefore disproves the proposed rich-restricted fixed-wedge bound.
It also gives `Omega(k^2)` horizontal wedges at one endpoint, each of
weight `Omega(k^2)`, so the global scale `J_N=Omega(Nk^2)` is sharp.

The remaining target is necessarily averaged: prove

\[
 \sum_wF_{L,T}(w)\le m^{o(1)}Nk^2,                       \tag{8.2}
\]

while explicitly allowing quadratic exceptional perpendicular pencils, or
classify and charge those pencils globally.  See
`LOW_BAND_FIXED_WEDGE_RICH_PENCIL_COUNTEREXAMPLE.md` for the construction
and verifier-backed certificate.
