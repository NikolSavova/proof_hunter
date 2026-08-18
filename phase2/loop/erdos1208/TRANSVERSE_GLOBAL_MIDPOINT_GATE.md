# Global midpoint form of the transverse gate

## Plain-language summary

The 90-point closure witness makes the maximum local overlap look like
`Theta(k^(3/2))`, while its total transverse energy is still `Theta(k^3)`.
This note records the exact global object that remains: decorated pairs of
unique midpoints whose separation is perpendicular to, and half the length
of, an edge of `A`.  The reformulation is equivalent to the transverse
collision problem, not a proof of it.  It removes the misleading
`L^infinity` target and isolates the disjoint-six-point configurations that an
incidence theorem would actually have to count.

## 1. Exact identity

Let `A` be a distance-Sidon set of `k` planar points, put

\[
 D=A-A,
 \qquad J(x,y)=(-y,x),
\]

and let `E_trans(A)` count unordered pairs of distinct `d,d' in D` for which

\[
 J(d'-d)\in D,
 \qquad \det(d,d')\ne0.                         \tag{1.1}
\]

Every nonzero directed difference has a unique ordered endpoint pair.  Write

\[
 d=a-b,\qquad d'=c-e,\qquad J(d'-d)=x-y.        \tag{1.2}
\]

Then

\[
 d'-d=(b+c)-(a+e).                              \tag{1.3}
\]

If

\[
 m_L={a+e\over2},\qquad m_R={b+c\over2},
\]

the collision equation is exactly

\[
 \boxed{x-y=2J(m_R-m_L)}.                       \tag{1.4}
\]

Thus `2E_trans(A)` is exactly the number of ordered sextuples
`(a,b,c,e,x,y)` satisfying (1.4), with the nonzero, distinct, and determinant
conditions from (1.1)--(1.2).  There is no loss in this change of variables.

## 2. Why the midpoints are unique

Distance-Sidon implies vector-Sidon.  If

\[
 a+e=a'+e',
\]

then `a-a'=e'-e`; equality of the two lengths forces the same unordered edge,
and the vector orientation then forces `{a,e}={a',e'}`.  A nontrivial
three-term progression is excluded for the same reason.  Consequently the
unordered midpoint set

\[
 M(A)=\{(a+e)/2:\{a,e\}\subseteq A\}
\]

has exactly `k(k+1)/2` elements, and every midpoint remembers its unique
unordered endpoint pair.

Equation (1.4) therefore counts pairs of these unique midpoints together with
one of the at most four cross-orderings of their endpoint pairs.  The segment
between the midpoints is perpendicular to `xy` and has half its length.  The
cross-ordering is load-bearing because it determines
`d=a-b`, `d'=c-e`, and hence whether the collision is transverse.

## 3. The easy and hard endpoint patterns

If the directed edges underlying `d` and `d'` share an endpoint, there are
only `O(k^3)` ordered choices before imposing (1.1).  Hence all such midpoint
configurations already lie on the desired cubic scale.

The unresolved term begins with the disjoint four-endpoint case:

* the two edges `a-b` and `c-e` are disjoint;
* their decorated midpoints satisfy (1.4) for the third edge `x-y`;
* `a-b` and `c-e` are not parallel.

The endpoints `x,y` may still overlap the first four; those mixed role
patterns must be retained or separately charged.  No claim that all six
points are distinct is being used here.

The needed theorem is that these disjoint decorated midpoint configurations
number at most `k^(3+o(1))` (in the wide regime; the parallel term is already
controlled by the line/trapezoid argument).  This is precisely the global
transverse gate in incidence language.

## 4. Why two tempting shortcuts fail

1. **Unweighted midpoint incidences are too strong.**  Forgetting the endpoint
   decoration also forgets the transverse determinant.  The perpendicular
   two-ruler construction has a fourth-power parallel contribution, so one
   cannot simply bound every pair `m_L,m_R` satisfying (1.4).
2. **The deltoid theorem does not apply.**  A deltoid uses two pairs of equal
   adjacent side lengths in `A`, which a distance-Sidon set forbids outright.
   Relation (1.4) compares an edge of `A` with a segment between midpoints;
   it does not create a deltoid on four points of `A`.

The literature search located midpoint-set growth theorems and Elekes's
deltoid count, but no theorem for the decorated perpendicular midpoint
incidence in (1.4).

## 5. Calibrating data

For the exact 90-point closure witness:

\[
 \max_d m_{\rm tr}(d)=614=0.7191\ldots k^{3/2},
\]

while

\[
 2E_{\rm trans}=1,009,116,
 \qquad E_{\rm trans}=0.6921\ldots k^3.
\]

Its rotated support is `446,638=0.6127... k^3`.  Therefore any useful
midpoint theorem must permit square-root-heavy individual fibres and control
their aggregate.  `verify_transverse_closure_global.py` checks every number
above exactly.
