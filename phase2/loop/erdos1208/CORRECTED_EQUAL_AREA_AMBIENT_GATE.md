# Corrected equal-area ambient gate: the parallel-side branch closes

## Status

The equal-area route remains live after correcting its target.  The earlier
$\Omega(k^4)$ polynomial-height examples do not refute the estimate that is
actually sufficient:

\[
 \mathcal E^{(6)}_{\Delta,\ne0}(A)
 \le m^{o(1)}(k^3+m^2).                                \tag{1.1}
\]

Their height is so large that the $m^2$ term dominates.

This note proves (1.1), with an extra harmless $\log m$, for every
equal-area pair having a pair of **corresponding parallel sides**.  The
initial direction-occupancy count by itself leaves an apparent longitudinal
line multiplicity.  Reorganizing first by the nonzero area and then using
integer divisor bounds removes that multiplicity exactly.

The remaining problem is now sharply isolated: bound the six-distinct
equal-area pairs for which all three pairs of corresponding sides are
nonparallel.  Equivalently, in the special-affine formulation below, every
side of the contributing source triangle avoids the real eigendirections of
the linear part.

## 1. Why the corrected estimate is sufficient

Let $A\subseteq\{0,\ldots,m\}^2$, $|A|=k$, be distance-Sidon.  For ordered
triples of distinct points write

\[
 \Delta(a,b,c)=\det(b-a,c-a).
\]

There are $R=k(k-1)(k-2)$ ordered triples, and at most $4m^2+1$ possible
signed doubled areas.  The zero-area triples must be handled separately.
If the six-distinct nonzero equal-area energy satisfies (1.1), while all
overlap and collinear terms are bounded at the same scale, Cauchy--Schwarz
gives

\[
 \frac{R^2}{4m^2+1}\le m^{o(1)}(k^3+m^2).
\]

In either range $k^3\le m^2$ or $k^3\ge m^2$, this yields
$k^3\le m^{2+o(1)}$.  Therefore the allowance $m^2$ is essential; the
stronger $m^{o(1)}k^3$ moment proposed in the earlier barrier note was not
necessary.

## 2. Special-affine identity

Every pair of ordered noncollinear triangles

\[
 (a,b,c),\qquad (a',b',c')
\]

with the same signed area determines a unique affine map
$g(x)=M_gx+t_g$ satisfying

\[
 g(a)=a',\quad g(b)=b',\quad g(c)=c',\qquad \det M_g=1.
\]

Conversely, any ordered **noncollinear** triple of distinct points in

\[
 B_g=A\cap g^{-1}A
\]

produces such a pair.  If $\mathcal G(A)$ is the finite set of maps arising
from at least one triangle pair, and if $T_{\rm nc}(B)$ denotes the number
of ordered noncollinear triples in $B$, then the exact nonzero signed-area
energy is

\[
 \boxed{
 \mathcal E_{\Delta,\ne0}(A)
 =\sum_{g\in\mathcal G(A)}T_{\rm nc}(B_g)
 \le\sum_{g\in\mathcal G(A)}(|B_g|)_3.}               \tag{2.1}
\]

Thus the often-written identity with $(|B_g|)_3$ is exact only when $A$ has
no collinear triple.  This qualification matters for a general
distance-Sidon set, although the falling-factorial sum is still a valid
upper envelope for the nonzero energy.

The six-distinct energy is obtained by retaining only noncollinear triples
$(a,b,c)\in B_g^3$ for which
$\{a,b,c\}\cap\{g(a),g(b),g(c)\}=\varnothing$.

A corresponding side is parallel precisely when, for one of
$v=b-a,c-b,a-c$,

\[
 M_gv\parallel v.                                      \tag{2.2}
\]

Thus $v$ is a real eigenvector of $M_g$.  The theorem below disposes of all
terms in (2.1) possessing such an eigen-edge, without needing to analyze the
maps individually.

## 3. Direction and line notation

Let $\mathcal U$ be the primitive integer directions modulo sign.  Choose
one representative $u=(u_1,u_2)$ from each class.  Let $e_u$ be the number
of unordered edges of $A$ parallel to $u$.  Then

\[
 \sum_{u\in\mathcal U}e_u={k\choose2}=:N.              \tag{3.1}
\]

Put $q(u)=\lVert u\rVert_\infty$.  An edge parallel to $u$ has vector
$tu$ with $1\le |t|\le m/q(u)$.  Distance-Sidonicity implies that two
different unordered edges in this direction cannot have the same $|t|$,
since both would have squared length $t^2\lVert u\rVert^2$.  Hence

\[
 e_u\le\left\lfloor\frac{m}{q(u)}\right\rfloor.        \tag{3.2}
\]

There are at most $4q$ primitive unoriented directions with
$\lVert u\rVert_\infty=q$.  Therefore

\[
 \boxed{
 \sum_ue_u^2
 \le4m^2\sum_{q=1}^m\frac1q
 \ll m^2\log(2m).}                                     \tag{3.3}
\]

For a fixed $u$, partition $A$ into the lines parallel to $u$.  The integer
line coordinate

\[
 \lambda_u(x)=\det(u,x)
\]

labels these lines.  Write
$n_u(s)=|\{x\in A:\lambda_u(x)=s\}|$.  Every pair on the same such line is
an edge of direction $u$, so

\[
 \boxed{
 \sum_sn_u(s)^2=k+2e_u.}                               \tag{3.4}
\]

## 4. Parallel corresponding sides

For a nonzero integer $z$, let $r_u(z)$ be the number of ordered triangles
$(a,b,c)$ with

\[
 \Delta(a,b,c)=z,qquad b-a\parallel u.                \tag{4.1}
\]

### Theorem 4.1

Let

\[
 \tau_m=\max_{1\le n\le2m^2}\tau(n),
\]

where $\tau$ is the ordinary positive divisor function.  Then

\[
 \boxed{
 \sum_{u\in\mathcal U}\sum_{z\ne0}r_u(z)^2
 \le4\tau_m\left(kN+2\sum_ue_u^2\right)
 \ll m^{o(1)}\bigl(k^3+m^2\log(2m)\bigr).}             \tag{4.2}
\]

Consequently the number of equal-area ordered triangle pairs for which at
least one of the three pairs of corresponding sides is parallel is at most

\[
 \boxed{
 12\tau_m\left(kN+2\sum_ue_u^2\right)
 \ll m^{o(1)}\bigl(k^3+m^2\log(2m)\bigr).}             \tag{4.3}
\]

This includes intersecting triangles.  It therefore also bounds the desired
six-distinct subfamily.

### Proof

Fix $u$.  Orient every edge parallel to $u$ both ways.  Its vector is
$tu$ for a signed nonzero integer $t$.  By distance-Sidonicity, every signed
$t$ occurs for at most one oriented edge.  Let $T_u$ be the resulting set of
signed coefficients, so $|T_u|=2e_u$.  If the edge belonging to $t$ starts
at $a_t$, set

\[
 \sigma_t=\lambda_u(a_t).
\]

Both endpoints have line coordinate $\sigma_t$.  For a third point $c$,

\[
 \Delta(a_t,a_t+tu,c)
 =\det(tu,c-a_t)
 =t\bigl(\lambda_u(c)-\sigma_t\bigr).                  \tag{4.4}
\]

It follows that

\[
 \boxed{
 r_u(z)=
 \sum_{\substack{t\in T_u\\t\mid z}}
 n_u\!\left(\sigma_t+\frac zt\right).}                \tag{4.5}
\]

The sum in (4.5) has at most $2\tau(|z|)\le2\tau_m$ terms.  Cauchy gives

\[
 r_u(z)^2
 \le2\tau_m
 \sum_{\substack{t\in T_u\\t\mid z}}
 n_u\!\left(\sigma_t+\frac zt\right)^2.               \tag{4.6}
\]

Sum (4.6) over $z\ne0$ and reverse the two sums.  For fixed $t$, the values
$\sigma_t+z/t$ visit each integer line coordinate at most once.  Using
(3.4),

\[
 \sum_{z\ne0}r_u(z)^2
 \le2\tau_m|T_u|(k+2e_u)
 =4\tau_m e_u(k+2e_u).                                 \tag{4.7}
\]

Summing (4.7), then using (3.1) and (3.3), proves (4.2).  Rotating the roles
of $(a,b,c)$ shows that the same estimate applies to the other two
corresponding sides.  The union bound proves (4.3).  Finally,
$\tau_m=m^{o(1)}$ by the standard divisor bound.  QED.

## 5. Why the divisor reorganization is necessary

If one first fixes two parallel base edges, the equal-area condition leaves
the sixth vertex on an entire line parallel to those bases.  Cauchy on line
occupancies then gives only

\[
 O\!\left(\sum_ue_u^2(k+e_u)\right),                  \tag{5.1}
\]

which is far too large.  Formula (4.5) changes the order of summation.  A
fixed nonzero area $z$ permits only divisor-many signed base lengths $t$;
after Cauchy in this divisor set, the longitudinal points are absorbed by
the exact second moment (3.4).  This is the step that produces one $e_u$
rather than $e_u^2$.

## 6. Exact remaining gate

Let $\mathcal E_{\mathrm{np}}^{(6)}(A)$ count equal nonzero signed-area
pairs of ordered triangles with six distinct vertices and

\[
 b-a\not\parallel b'-a',\qquad
 c-b\not\parallel c'-b',\qquad
 a-c\not\parallel a'-c'.                              \tag{6.1}
\]

The parallel theorem reduces the corrected ambient route to

\[
 \boxed{
 \mathcal E_{\mathrm{np}}^{(6)}(A)
 \stackrel{?}{\le}m^{o(1)}(k^3+m^2).}                 \tag{6.2}
\]

In special-affine language, (6.2) is the part of (2.1) in which the three
edges of the source triangle all avoid the real eigendirections of $M_g$.
This formulation makes the surviving difficulty explicit:

* elliptic $M_g$ have no real eigendirection, so the parallel argument says
  nothing about them;
* hyperbolic or parabolic $M_g$ have at most two eigendirections, but a large
  overlap $B_g$ need not contain an edge in either direction;
* the old modular-parabola examples have corrected energy at most the
  permitted $m^2$ scale after Euclideanization and hence are not a no-go.

No counterexample to (6.2) is currently known.  Nor does the theorem above
claim control of it.  The equal-area route should therefore remain active,
with (6.2) as its precise arithmetic/incidence target.

## 7. Verification

The verifier checks:

1. distinct signed direction coefficients;
2. the exact line identity (3.4);
3. the exact divisor formula (4.5);
4. the bounds (3.3), (4.2), and (4.3);
5. exact profiles on closure, Costas, modular-parabola, and ruler
   distance-Sidon certificates.

Run:

```bash
python phase2/loop/erdos1208/verify_corrected_equal_area_ambient_gate.py
```
