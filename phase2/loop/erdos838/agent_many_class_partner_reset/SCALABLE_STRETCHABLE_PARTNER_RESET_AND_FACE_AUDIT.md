# A scalable stretchable many-class partner reset

**Date:** 2026-08-15.  This addresses the exact remaining \(2+2\)
partner-itinerary gate after
`THREE_CLASS_PAIR_CIRCUIT_TRIANGLE_GATE.md`.  All face counts are for
nonempty ordinary convex subsets, and all logarithms are base two.

## Verdict

Arbitrarily many fresh-partner resets are stretchable, even with one
label-disjoint bad-\(2+2\) matching on **every** class pair, a uniform
signed hidden-point rule, and a common-\(uv\) pocket.

For every

\[
                         t\ge2,\qquad m\ge t-1,        \tag{1}
\]

there is an exact rational general-position configuration with \(t\)
classes \(Y_0,\ldots,Y_{t-1}\), each of size \(g=2m\), and selected
matchings \(\mathcal M_{ij}\) of size \(m=g/2\), such that

* every selected edge is a nonconvex \(2+2\) four-set;
* every physical label occurs once against each of the other \(t-1\)
  classes;
* different neighbouring classes use different physical partners;
* every physical pair node has degree one, so there are no pair-node
  triangles; and
* for \(i<j\), the hidden point in every edge of \(\mathcal M_{ij}\) is
  the designated left label of \(Y_j\).

Thus signed circuit type, radial/circular order, high label reuse, and the
common carrier do not by themselves force physical-pair reuse.  The
construction is a genuine planar realization of the scalable incidence
reset that was previously only abstract.

The ambient-face audit is equally important.  The explicit rational
representative used here is **far too rich to be a least counterexample**:
each class is in convex position and already contributes \(2^g-1\)
faces.  It also has exactly

\[
 \binom t2 m^2(m-1)(2m-1)                              \tag{2}
\]

convex \(2+2\) quadrilaterals between class pairs, in addition to the
canonical ES5 release bank.  At \(t=\Theta(\log N)\), \(g=N/t\), the
internal payment alone has logarithm \(\Omega(N/\log N)\), vastly above
the live \(O((\log N)^2)\) target.  Therefore this is a **stretchability
barrier**, not a low-face counterexample and not a proof that a
coefficient-scale face/profile theorem is impossible.

## 1. Tangent-line skeleton and its exact orders

For \(0\le i<t\), let

\[
                 \ell_i:\quad y=2ix-i^2              \tag{3}
\]

be the tangent at \(x=i\) to \(y=x^2\).  Parameterize \(\ell_i\) by

\[
                 p_i(s)=(i+s,\ i^2+2is).              \tag{4}
\]

The intersection of \(\ell_i\) and \(\ell_j\), in the \(s\)-coordinate
on \(\ell_i\), is

\[
                         s_{ij}={j-i\over2}.           \tag{5}
\]

Put \(D=8(m+1)\),

\[
              \alpha_a={a+1\over D}\quad(0\le a<m),
              \qquad B=t+1,                           \tag{6}
\]

and initially place

\[
       L_{i,a}=p_i(\alpha_a),\qquad
       R_{i,a}=p_i(B+\alpha_a).                        \tag{7}
\]

All \(x\)-coordinates in (7) are distinct.  More significantly, the
order on \(\ell_i\) is exact:

\[
 \{\ell_i\cap\ell_j:j<i\}
   \;<\;p_i(0)\;<\;L_i
   \;<\;\{\ell_i\cap\ell_j:j>i\}\;<\;R_i.            \tag{8}
\]

The intersections in the left and right braces occur in increasing
class-index order.  Hence a segment \(L_{i,a}R_{i,b}\) crosses every
later-class line \(\ell_j\), \(j>i\), at \(\ell_i\cap\ell_j\), but lies
entirely on one side of every earlier-class intersection.

This line order is the geometric resource that implements the itinerary.
It is not an abstract graph construction.

## 2. Cyclic factors and fresh partner itineraries

For \(i\ne j\), let

\[
 r_i(j)=\begin{cases}j,&j<i,\\j-1,&j>i.\end{cases}    \tag{9}
\]

The values \(r_i(j)\), as \(j\) ranges over the neighbours of \(i\), are
the distinct residues \(0,\ldots,t-2\), which exist modulo \(m\) by (1).
Assign to neighbour \(j\) the cyclic perfect matching

\[
 \mathcal P_i(j)=
 \bigl\{\{L_{i,a},R_{i,a+r_i(j)\pmod m}\}:0\le a<m\bigr\}.  \tag{10}
\]

These are distinct factors of the standard one-factorization of
\(K_{m,m}\).  For \(i<j\), match the \(a\)-th pair of
\(\mathcal P_i(j)\) to the \(a\)-th pair of \(\mathcal P_j(i)\); call the
resulting family \(\mathcal M_{ij}\).

Every label occurs in one pair of each of the \(t-1\) factors.  A fixed
left label sees the right-partner itinerary

\[
       a,\ a+1,\ldots,a+t-2\pmod m,                   \tag{11}
\]

in neighbour-rank order.  No physical pair is repeated, because the
factor shifts are distinct.  Consequently every pair node in the
auxiliary graph has degree one and the graph is a disjoint union of
\(m\binom t2\) edges.

## 3. Signed circuit proof

Two lines meeting at \(O\) may be sent affinely to the coordinate axes.
Suppose two points on the first line have coordinates

\[
                         (a,0),(A,0),\qquad a<0<A,
\]

and two points on the second have coordinates

\[
                         (0,b),(0,B),\qquad 0<b<B.
\]

Then \((0,b)\) lies strictly inside the triangle with other vertices
\((a,0),(A,0),(0,B)\).  Indeed,

\[
 (0,b)=
 (1-b/B){A\over A-a}(a,0)
 +(1-b/B){-a\over A-a}(A,0)
 +{b\over B}(0,B),                                   \tag{12}
\]

and all three coefficients are positive and sum to one.

For \(i<j\), (8) says that the pair in \(Y_i\) straddles
\(\ell_i\cap\ell_j\), while both labels of the pair in \(Y_j\) lie on
the same ray from the intersection.  Its \(L_{j,a}\) label is the nearer
one.  Equation (12) therefore proves that every selected four-set is a
strict nonconvex circuit with hidden point \(L_{j,a}\).  The sign is the
same on the whole \(ij\) matching, and the hidden class follows the
transitive class order.

This also gives the full two-class \(2+2\) table.  For \(i<j\), a pair in
\(Y_i\) straddles the intersection exactly when it chooses one \(L\) and
one \(R\), whereas no pair in \(Y_j\) straddles.  Four points on two
lines are nonconvex exactly when precisely one of their two within-line
pairs straddles the intersection: (12) proves the one-straddling case;
if both pairs straddle, the four points occupy the four rays and form a
quadrilateral; if neither straddles, each within-line pair is a supporting
edge because the other pair lies strictly on one side of its line.  Thus,
before perturbation,

\[
\begin{aligned}
 N^{\rm bad}_{ij}&=m^2\binom{2m}{2},\\
 N^{\rm cvx}_{ij}
  &=\left(\binom{2m}{2}-m^2\right)\binom{2m}{2}
    =m^2(m-1)(2m-1).                                  \tag{13}
\end{aligned}
\]

## 4. Exact rational general-position lift

The skeleton has deliberate collinearities within the classes.  They are
removed without changing any two-class circuit sign by the rational lift

\[
                 (x,y)\longmapsto(x,y+\delta x^2).    \tag{14}
\]

For a labeled triple \(A,B,C\), its orientation after (14) is

\[
 \operatorname{or}_\delta(A,B,C)
 =\operatorname{or}_0(A,B,C)
  +\delta(x_B-x_A)(x_C-x_A)(x_C-x_B).                 \tag{15}
\]

All \(x\)-coordinates are distinct.  For every triple using two labels
of one class and one of another, the first term in (15) is nonzero.
Define the positive rational number

\[
 \rho={1\over4}\min
 { |\operatorname{or}_0(A,B,C)|\over
   |(x_B-x_A)(x_C-x_A)(x_C-x_B)|},                    \tag{16}
\]

where the minimum is over those two-class triples.  Start with
\(\delta=\rho\), and repeatedly halve it until every triple is
noncollinear.

This exact search terminates.  Equation (16) preserves the sign of every
two-class triple.  A triple contained in one class has orientation equal
to the nonzero second term of (15).  A triple meeting three classes
excludes at most one positive value of \(\delta\), so only finitely many
members of the infinite halving sequence are forbidden.  All coordinates
remain rational.

It follows that every selected circuit, its hidden label, and the complete
count (13) survive in a rational uniform rank-three order type.  Within
class \(i\), the lifted points lie on the strictly convex parabola

\[
                      y=\delta x^2+2ix-i^2,           \tag{17}
\]

so all \(2m\) are hull vertices.

## 5. Exact ambient-face audit

The chosen lift makes every nonempty subset of every \(Y_i\) convex.
The internal banks are disjoint and contribute exactly

\[
                         t(2^{2m}-1).                 \tag{18}
\]

The convex two-class quadrilaterals in (13) are distinct from those
banks and contribute exactly (2).

There is also the existing five-point canonical-release bank.  Each of
the \(m\binom t2\) selected bad circuits may be extended by any of the
\(2m(t-2)\) labels in a third class.  Deleting the first successful
circuit label gives

\[
                 R_{\rm ES5}=2m^2(t-2)\binom t2       \tag{19}
\]

records.  The general decoder in
`THREE_CLASS_CIRCUIT_MATCHING_EXTENSION_AND_ANTI_ALIGNMENT.md` has load
at most three, so at least \(R_{\rm ES5}/3\) further three-class
quadrilateral faces exist.  These are disjoint from (18) and (2) by
their class occupancies.  Hence this representative satisfies the
fully physical lower bound

\[
 V(P)\ge
 t(2^{2m}-1)
 +\binom t2m^2(m-1)(2m-1)
 +{2\over3}m^2(t-2)\binom t2.                         \tag{20}
\]

The verifier records the actual canonical outputs rather than only the
load-three bound.  At the default \(t=m=6\), it finds 4,320 records,
4,320 distinct faces, and decoder load one.  It certifies the disjoint
bank

\[
       24{,}570+29{,}700+4{,}320=58{,}590.            \tag{21}
\]

For the exhaustively enumerable regression \(t=3,m=2\), the whole
12-point configuration has exactly 861 nonempty convex subsets.  The
three displayed bank types account for only 105 of them.  Thus (20) is
an audit lower bound, not an exact total-profile formula.

Most decisively, if \(N=2mt\), \(t=\Theta(\log N)\), then (18) alone
gives

\[
                         \log V(P)\ge2m=N/t
                            =\Omega(N/\log N).         \tag{22}
\]

This witness cannot inhabit the fixed-gap least-counterexample regime.
No claim is made that the Boolean payment is forced by the reset
constraints; finding a low-face perturbation of the same line skeleton,
or proving none exists, remains open.

## 6. Common-\(uv\) pocket compatibility

The entire rational order type can additionally be nested behind one
fixed carrier.  First scale the raw coordinates to \(p=(f,h)\) in a
bounded box, and for sufficiently small positive rational
\(\varepsilon\) apply

\[
 T_\varepsilon(f,h)=
 \left({\varepsilon^2h\over2+\varepsilon f},
       {-1\over2+\varepsilon f}\right).               \tag{23}
\]

This is the projective transformation

\[
             [f:h:1]\longmapsto
             [\varepsilon^2h:-1:2+\varepsilon f],     \tag{24}
\]

so it preserves the complete order type when the denominators are
positive.  With

\[
              u=(-1,0),\qquad v=(1,0),                \tag{25}
\]

the left and right tangent coordinates of an image point are

\[
 {1+X\over-Y}=2+\varepsilon f+\varepsilon^2h,
 \qquad
 {1-X\over-Y}=2+\varepsilon f-\varepsilon^2h.         \tag{26}
\]

Because all raw \(f\)-coordinates are distinct, both quantities have the
same strict order for sufficiently small \(\varepsilon\).  For two points
below \(uv\), the point with both larger quantities in (26) lies strictly
inside the triangle formed by \(u,v\) and the other point; this follows
directly by intersecting that triangle with the horizontal line through
the first point.  The child
points are therefore totally nested: for every two child labels \(y,z\),
\(\{u,v,y,z\}\) is nonconvex.  Meanwhile (23) tends to \((0,-1/2)\), so
the fixed opposite-side point \(x=(1/7,1)\) makes every
\(\{u,v,x,y\}\) convex once \(\varepsilon\) is small.  Avoiding the
finitely many remaining collinearities gives global general position.

The verifier finds such an \(\varepsilon\) by exact halving, checks all
carrier-child pairs and carrier-singleton faces, and rechecks the full
selected signed circuit system and the face counts after nesting.  Thus
the scalable reset survives the common side covector and the endpoint-XOR
setup, just as the earlier twelve-point reset did.

## 7. Consequence for the remaining gate

The previous abstract one-factorization escape is now planar and
stretchable.  A continuation cannot infer a repeated physical pair from
any combination of:

1. one matching of size \(g/2\) on every class pair;
2. label load \(t-1\);
3. a fixed signed hidden-point rule;
4. coherent intersection/radial orders; or
5. a common-\(uv\) pocket with all endpoint colors defined.

What this note does **not** decide is the face-budget-sensitive statement:
whether every realization of the same itinerary under
\(V(P)<2^{\Phi_3(\log n)}\) must release a recoverable quasipolynomial
profile bank.  The exact new fork is narrower:

* construct a low-face perturbation/order type with the same tangent-line
  itinerary; or
* exploit the low-face hypothesis to prove that the Boolean-style payment
  seen here cannot be suppressed without creating a recoverable
  chronology/profile seam.

The present result closes only the pure stretchability question.  It does
not close Erdős 838 or the unrestricted coefficient gap.

## 8. Verification

Run

```text
python3 phase2/loop/erdos838/agent_many_class_partner_reset/verify_scalable_partner_reset.py
```

The default exact run uses \(t=m=6\), \(N=72\), and checks all triple
orientations, all selected hidden points, factor disjointness, label and
pair-node loads, all 65,340 cross-class \(2+2\) quadrilaterals, every ES5
canonical release, the three bank disjointness audit, the common-\(uv\)
projective nesting, and the exhaustive \(t=3,m=2\) total face count.  It
prints `PASS`.

The script is parameterized.  For example,

```text
python3 phase2/loop/erdos838/agent_many_class_partner_reset/verify_scalable_partner_reset.py --t 8 --m 8 --no-small-regression
```

checks a 128-point, 224-circuit realization.  Larger values are exact but
the all-triples and all-\(2+2\)-quad audits are polynomially expensive.
