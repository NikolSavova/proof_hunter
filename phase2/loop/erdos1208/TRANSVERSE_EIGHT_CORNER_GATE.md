# Adaptive eight-corner gate for the transverse theorem

## 1. Status

The compact-anchor construction kills every global non-collinear
third-moment estimate, but it remains exactly on the conjectured cubic scale
for the transverse second moment.  This note gives a new sufficient
formulation of that surviving theorem.

Every transverse relation has three uniquely oriented edges of `A`.  Choosing
one endpoint from each edge gives eight three-coordinate projections.  A
relation need not be light in any fixed projection, but it is enough that
each relation be light in **one projection chosen adaptively**.  All exact
stress families tested satisfy this with adaptive degree at most eight.

This is an exact reduction and falsification target, not a proof.  The missing
lemma is that simultaneous richness in all eight corners forces a repeated
Euclidean distance.

## 2. The relation hypergraph

Let `A` be distance-Sidon, `|A|=k`, put `D=A-A`, and let `J` be quarter turn.
Write an oriented transverse relation as

\[
 d=f+Je,\qquad d,e,f\in D,\quad e\ne0,\quad d\cdot e\ne0. \tag{2.1}
\]

Every nonzero vector in `D` has a unique ordered endpoint pair.  Write

\[
 d=a_0-a_1,\qquad f=b_0-b_1,\qquad e=c_0-c_1.   \tag{2.2}
\]

Thus the relation set `R(A)` is a six-partite, six-uniform hypergraph on six
role copies of `A`.  Its size is the oriented transverse count

\[
 |R(A)|=2E_{\rm trans}(A).                       \tag{2.3}
\]

For a corner `epsilon=(epsilon_1,epsilon_2,epsilon_3) in {0,1}^3`, define

\[
 \pi_\epsilon(\rho)
 =(a_{\epsilon_1},b_{\epsilon_2},c_{\epsilon_3})\in A^3. \tag{2.4}
\]

Let

\[
 \deg_\epsilon(v)=|\{\rho\in R(A):\pi_\epsilon(\rho)=v\}|,
\]

and define the adaptive degree of a relation by

\[
 \delta(\rho)=
 \min_{\epsilon\in\{0,1\}^3}
 \deg_\epsilon(\pi_\epsilon(\rho)).             \tag{2.5}
\]

The eight projections are genuinely different.  A fixed corner degree is a
fibre of one of the signed triple maps `+/- A +/- A +/- JA`; the known
square-root-heavy fibres show that no single projection should be expected
to have a pointwise subpolynomial bound.

## 3. Exact sufficient lemma

**Adaptive-corner lemma.**  If

\[
 K(A):=\max_{\rho\in R(A)}\delta(\rho)\le k^{o(1)}, \tag{3.1}
\]

then

\[
 E_{\rm trans}(A)\le k^{3+o(1)}.                 \tag{3.2}
\]

Indeed, assign every relation to a corner attaining the minimum in (2.5),
breaking ties deterministically.  There are eight choices of corner and at
most `k^3` projected triples for each corner.  If a bucket `(epsilon,v)`
receives any relation, then its full projection degree is at most `K(A)`, so
the bucket receives at most `K(A)` relations.  Therefore

\[
 |R(A)|\le8K(A)k^3.                              \tag{3.3}
\]

Equations (2.3) and (3.1) prove (3.2).

This would close the wide branch of #1208 after Elekes's trapezoid theorem,
exactly as the previous transverse moment gate does.  It is stronger than the
global `k^(4+o(1))` row-moment statement, but it has a new advantage: all
known heavy rows, heavy colours, and compact-anchor fibres can change to a
different light projection relation by relation.

## 4. Exact stress data

`verify_transverse_eight_corner_gate.py` enumerates the complete relation
sets and all eight projection degrees.  The results are

| witness | `k` | `|R(A)|` | `K(A)` | mean `delta(rho)` |
|---|---:|---:|---:|---:|
| heavy closure | 30 | 26,428 | 5 | 1.57772 |
| heavy closure | 45 | 107,720 | 6 | 1.77564 |
| heavy closure | 60 | 259,516 | 8 | 1.84137 |
| compact-anchor lift | 117 | 159,888 | 6 | 2.00443 |

The maximum degrees in the eight fixed projections are respectively

\[
\begin{array}{c|c}
k& (\max\deg_\epsilon)_{\epsilon}\cr
30&(9,10,10,9,9,10,10,9)\cr
45&(13,12,12,13,13,12,12,13)\cr
60&(14,14,14,14,14,14,14,14)\cr
117&(6,12,12,6,6,12,12,6).
\end{array}
\]

The last row is important: it is the exact general-position family that
forces the non-collinear third moment above `k^3`.  Its adaptive corner
profile is nevertheless lighter than the closure examples.  Thus the new
gate survives the strongest known obstruction to the discarded route.

Run

```text
python3 phase2/loop/erdos1208/verify_transverse_eight_corner_gate.py
```

## 5. Structural interpretation and next proof target

For the all-head corner, a completion is a triple `(a_1,b_1,c_1)` in a fibre
of

\[
 \Phi(a,b,c)=a-b-Jc.                             \tag{5.1}
\]

The other seven corners give the seven remaining sign patterns.  Directness
of `A+JA` and `A-JA` implies that fixing either of the first two coordinates
determines the other two.  Fixing the third reduces to a prescribed directed
difference and is also unique unless that difference is zero; the zero branch
is the familiar diagonal family.  In particular every fibre has size at most
`k`.  This explains the universal bound `deg_epsilon<=k`, but not the
required subpolynomial adaptive minimum.

The exact missing statement is an eight-sign inverse theorem:

> If one relation lies in polynomially large fibres for every one of the
> eight signed triple maps, then two non-antipodal differences of `A` have
> the same Euclidean norm.

This statement is now the most local surviving route to the transverse
theorem.  It retains every metric constraint, permits a square-root-heavy
fibre in any fixed sign pattern, and asks only that one of eight complementary
views be sparse.  A kill family would be distance-Sidon sets `A_k` and
relations `rho_k` for which `delta(rho_k)>=k^epsilon` for some fixed
`epsilon>0`; none is currently known.
