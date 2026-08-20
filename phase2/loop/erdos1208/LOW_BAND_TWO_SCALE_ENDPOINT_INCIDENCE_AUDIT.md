# Low-band two-scale sum: endpoint incidence identities and a sharp pencil barrier

## 1. Outcome

Let

\[
 S_T=\{r\ne0:U_L(r)\ge T\},\qquad T\ge k,                \tag{1.1}
\]

and recall that the low-codegree reduction leaves

\[
 \sum_{r\in S_T}R_D(-18r).                               \tag{1.2}
\]

There are two exact sufficient global quantities.  Put

\[
 \begin{aligned}
 B_L&=\sum_{r\ne0}R_D(-18r)U_L(r),\\
 J_L&=\sum_{r\ne0}R_D(-18r)W_{r,L},                      \tag{1.3}
 \end{aligned}
\]

where `W_(r,L)` is the endpoint-wedge count of the first edges in the
determinant-qualified target cell.  Then

\[
 \boxed{
 \sum_{r\in S_T}R_D(-18r)
 \le \min\left\{{B_L\over T},{kJ_L\over T^2}\right\}.}  \tag{1.4}
\]

Consequently either estimate

\[
 \boxed{B_L\le m^{o(1)}Nk^2}                             \tag{1.5}
\]

or

\[
 \boxed{J_L\le m^{o(1)}Nk^2}                             \tag{1.6}
\]

would prove the required low-band two-scale tail

\[
 \sum_{r\in S_T}R_D(-18r)
 \le {m^{o(1)}N(H_*+k^3)\over kT}.                       \tag{1.7}
\]

For (1.6), use `T>=k` after (1.4).  Thus the two-sided endpoint-wedge idea
does reach the exact required exponents if its natural global moment can be
proved.

The standard point-circle or point-line incidence route does not prove
(1.5) or (1.6).  Distance-Sidonicity makes the *unweighted* incidence
support almost trivial: every relevant circle has at most one other point
of `A`, and each target wedge is one incidence on an explicitly determined
line.  The scalar source multiplicity is then placed as a weight on these
already-supported incidences.  The resulting weighted circle count is
exactly `2B_L`, and the weighted line count is exactly `J_L`.  Applying an
unweighted incidence theorem therefore returns the original unknown
moment, not a bound for it.

This failure is sharp.  There are arbitrarily large genuine integral
distance-Sidon sets with determinant cutoff `L=N` for which

\[
 R_D(-18r)=\Theta(k^2),\qquad
 U_N(r)=\Theta(k),\qquad W_{r,N}=\Theta(k^2),             \tag{1.8}
\]

at one gap.  Hence

\[
 \boxed{J_N=\Omega(k^4)=\Omega(Nk^2).}                   \tag{1.9}
\]

All target wedge lines in this subsystem form a pencil through one endpoint,
while every target determinant exceeds `N`.  Thus no estimate
`J_L=o(Nk^2)` follows from determinant transversality or ordinary line
incidence.  The scale (1.6), if true up to `m^(o(1))`, is best possible.

The sharp family has exponential height, inherited from the quadratic-gap
source ruler.  It does not refute (1.6) with its allowed `m^(o(1))` factor,
and it does not refute (1.7).  It is a decisive barrier to obtaining a
power saving beyond the exact required scale.

## 2. Simultaneous endpoint equations

Write the ordered source edges as

\[
 u=c-d,\qquad u'=c'-d',                                  \tag{2.1}
\]

and a determinant-qualified target record as

\[
 v=x-a,\qquad v'=y-b.                                    \tag{2.2}
\]

The simultaneous source/target scalar system is

\[
 \boxed{
 |c-d|^2-|c'-d'|^2
 +18\bigl(|x-a|^2-|y-b|^2\bigr)=0,}                     \tag{2.3}
\]

with

\[
 |2\det(x-a,y-b)|>L.                                     \tag{2.4}
\]

For a fixed source pair, put

\[
 r=-{|c-d|^2-|c'-d'|^2\over18}.                          \tag{2.5}
\]

There are `U_L(r)` target completions.  Summing first over the source pair
therefore proves the exact scalar-record identity

\[
 \#\{\text{systems (2.1)--(2.4)}\}=B_L.                 \tag{2.6}
\]

In particular, on `S_T`, every source representation has at least `T`
completions, giving the first term in (1.4).

## 3. The two-target endpoint wedge

Take two target records with the same `r` and a common endpoint on their
first edges:

\[
 \{x,a_1\},\{y_1,b_1\},qquad
 \{x,a_2\},\{y_2,b_2\}.                                 \tag{3.1}
\]

Their equal-gap equations are

\[
 \begin{aligned}
 |x-a_1|^2-|y_1-b_1|^2&=r,\\
 |x-a_2|^2-|y_2-b_2|^2&=r.                               \tag{3.2}
 \end{aligned}
\]

Subtracting gives

\[
 |x-a_1|^2-|x-a_2|^2
 =|y_1-b_1|^2-|y_2-b_2|^2=:g.                            \tag{3.3}
\]

After expansion, the common endpoint lies on the exact line

\[
 \boxed{
 2x\mathbin\cdot(a_2-a_1)
 =g-|a_1|^2+|a_2|^2.}                                    \tag{3.4}
\]

For every source representation of `-18r`, the same target wedge is one
line-incidence lift.  Hence the number of simultaneous source-pair/target-
wedge systems is exactly

\[
 J_L=\sum_rR_D(-18r)W_{r,L}.                              \tag{3.5}
\]

The endpoint lower bound

\[
 W_{r,L}\ge {2U_L(r)^2\over k}-U_L(r)                   \tag{3.6}
\]

implies `W_(r,L)>=T^2/k` on `S_T`, proving the second term of
(1.4).

## 4. Why ordinary circle incidence is tautological

For `x in A` and a distance label `lambda in D`, let

\[
 \mathcal C(x,\lambda)=\{z:|z-x|^2=\lambda\}.            \tag{4.1}
\]

Distance-Sidonicity implies

\[
 |(A\setminus\{x\})\cap\mathcal C(x,\lambda)|\le1.       \tag{4.2}
\]

Indeed, two such points would give two different edges with the same
squared distance.  A target record whose first edge is `{x,a}` is exactly
the supported incidence

\[
 a\in\mathcal C(x,\delta(xa)).                            \tag{4.3}
\]

and also its reversal with centre `a`.  Give this incidence the weight

\[
 \sum_{\substack{(v,v'):\ v=\{x,a\}\\
          |2\det(v,v')|>L}}
 R_D\bigl(-18(\delta(v)-\delta(v'))\bigr).                \tag{4.4}
\]

Then the exact weighted incidence identity is

\[
 \boxed{I_{\rm circle}^{\rm weighted}=2B_L.}             \tag{4.5}
\]

The distinct supported incidences in (4.3) number only `2N`.  Thus a
point-circle theorem has nothing left to save on the support; the whole
problem is the weight (4.4), which is precisely the scalar moment being
estimated.  The high determinant cutoff filters summands of (4.4) but does
not change (4.2).

## 5. Why ordinary line incidence is also tautological

For ordered `a_1!=a_2` and an integer `g`, denote the line in (3.4) by
`ell(a_1,a_2;g)`.  Uniqueness of directed differences means different
ordered neighbour pairs have different directed normals `a_2-a_1`.
Nevertheless two obstructions remain.

First, a fixed point `x` can support a quadratic pencil of these distinct
lines, one for every ordered pair of its other endpoints.  Second, every
ordered partner-edge pair with norm gap `g` produces the *same* line for
fixed `(a_1,a_2)`.  The different absolute partner norms give different
scalar shifts `r`, and hence different weights `R_D(-18r)`, without changing
the line.

Weight the incidence (3.4) by `R_D(-18r)` for every determinant-qualified
partner pair which produces it.  Then

\[
 \boxed{I_{\rm line}^{\rm weighted}=J_L.}                 \tag{5.1}
\]

A Szemeredi--Trotter bound for the distinct lines sees the endpoint triples
`(x,a_1,a_2)` but discards the partner-pair and source-pair weights.  A
weighted incidence theorem strong enough to prove (1.6) would have to
control exactly these scalar weights; it is not supplied by the distinct
slopes.

## 6. A sharp genuine target-pencil construction

Fix an odd `B>=11` and a parameter `M`.  The quadratic-gap ruler construction
provides `4M` integral distance-Sidon points and a gap

\[
 z_0=B^{2M+1}                                             \tag{6.1}
\]

with at least `2M^2` ordered edge-pair representations.  Scale every point
by `12`.  The resulting gap

\[
 z=144B^{2M+1}                                           \tag{6.2}
\]

still has

\[
 R_D(z)\ge2M^2.                                           \tag{6.3}
\]

Put

\[
 r=-{z\over18}=-8B^{2M+1},qquad
 C=2B^{2M+1}-1.                                          \tag{6.4}
\]

At one new point `Z`, plant `M` first-edge vectors

\[
 v_i=(C,T_i).                                             \tag{6.5}
\]

At independent free centres plant partner vectors

\[
 v_i'=(C+2,T_i).                                         \tag{6.6}
\]

They obey

\[
 |v_i|^2-|v_i'|^2=-4(C+1)=r,qquad
 |2\det(v_i,v_i')|=4|T_i|.                               \tag{6.7}
\]

Choose a scaled Golomb ruler for the `T_i`, translate it beyond `N/4`, and
exclude the finitely many controlled internal collisions.  Generic integral
choices of `Z` and of the partner centres then make the union
distance-Sidon and introduce no unwanted occurrence of the two planted
gaps.  As usual, all bad distance equalities are nonzero quadratic
polynomials and the grid nonvanishing lemma supplies an integral choice.

The construction has

\[
 k=4M+(1+3M)=7M+1,qquad N=\Theta(M^2).                   \tag{6.8}
\]

Every target record passes the cutoff `L=N`; its first edges form an
`M`-edge star.  Hence

\[
 U_N(r)\ge M,qquad W_{r,N}\ge {M\choose2}.               \tag{6.9}
\]

Combining (6.3) and (6.9),

\[
 J_N\ge2M^2{M\choose2}=\Theta(M^4)=\Theta(Nk^2).         \tag{6.10}
\]

The wedge lines (3.4) are a genuine high-determinant pencil through `Z`.
Thus the scale in (1.6) cannot be improved.  The base-power ruler makes the
height exponential in `M`; this is why (6.10) is compatible with an
`m^(o(1))` theorem.

## 7. Exact finite certificate

The verifier checks (2.3), (3.3), (3.4), (4.5), and (5.1) on the stored
closure, Costas, parabola, and perpendicular-ruler families.  With cutoff
`L=N`, their exact `(B_L,J_L)` values are

\[
\begin{array}{c|rr}
\text{family}&B_L&J_L\\ \hline
\text{closure }20&28994&37904\\
\text{Costas }22&18380&9839\\
\text{parabola }43&16194&276\\
\text{perpendicular ruler }40&8544&1012
\end{array}                                               \tag{7.1}
\]

It also constructs a 35-point sharp-pencil certificate.  All `N=595`
distances and pair sums are distinct.  At

\[
 (z,r)=(339544467504,-18863581528)                        \tag{7.2}
\]

it has

\[
 (R_D(z),U_N(r),W_{r,N})=(32,6,15),                      \tag{7.3}
\]

so the aligned scalar and wedge masses are `192` and `480`.  The full
determinant-qualified moments are `B_N=384,J_N=480`.

Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_low_band_two_scale_endpoint_incidence.py
```

## 8. Exact remaining gate

The endpoint attack reduces the low band to either of the sharp global
moments (1.5) or (1.6).  The joint-wedge formulation uses all the requested
decorations: the source gap remains `-18r`, the target determinant cutoff
remains inside `W_(r,L)`, and both target records retain their common
endpoint.

What fails is a black-box incidence proof.  The endpoint geometry determines
only the support circles and lines; the missing estimate is a weighted
anti-correlation between their scalar shifts and `R_D(-18r)`.  The sharp
pencil shows that this weighted theorem can hold only at the exact
`m^(o(1))Nk^2` scale, with no power saving.  Proving (1.6), or finding a
polynomial-height family exceeding it by a fixed power, is the remaining
two-scale problem.
