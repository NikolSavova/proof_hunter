# A critical planted parabola kills the colored parent-energy gate

## 1. Outcome

The support-restricted colored parent-energy estimate proposed in
`COLORED_DERIVATIVE_L2_CORRELATION_GATE.md` is false by a polynomial
factor, even for genuine integral distance-Sidon sets at the cube-root
critical exponent.

More precisely, there is a sequence of graph-like distance-Sidon sets

\[
 A\subset [0,m]^2,\qquad |A|=k=m^{2/3-o(1)},                 \tag{1.1}
\]

and dyadic parent and child richness (L=J=m^{1/2+o(1)}), for which

\[
 \boxed{
 \mathfrak A_{L,J}
 =\sum_{h,\theta,B:J\le K_h(\theta,B)<2J}
       C_h(\theta,B)^2
 =\Theta(m^{3/2}).}                                  \tag{1.2}
\]

On these parameters, the full proposed right side

\[
 m^{o(1)}
 {S^4\over k^6(k^3J^3+k^2J^5)},
 \qquad S=k^3+m^2,                                   \tag{1.3}
\]

is only (m^{1/6+o(1)}).  Thus (1.2) violates (1.3) by

\[
 \boxed{m^{4/3-o(1)}.}                               \tag{1.4}
\]

The construction is elementary.  Plant the exact integer parabola

\[
 S_L=\{(r,r^2):0\le r<2L\}                           \tag{1.5}
\]

in a square of side (M=64L^2).  A random-alteration extension lemma
adds (M^{2/3-o(1)}) points in a high strip while preserving
distance-Sidonicity, distinct horizontal levels, and every planted
derivative support.  The planted arc then supplies the energy (1.2).

This does **not** disprove the ambient equal-centroid/equal-area target or
Erdős 1208.  The unweighted derivative-triple count of the planted arc is

\[
 \sum_{q=1}^L {2L-q\choose3}=\Theta(L^4)=\Theta(m^2), \tag{1.6}
\]

so ambient height pays it exactly.  What fails is charging that same
geometric core once for each of its (Theta(L)) coherent parent reverse
representations.  Indeed the weighted mass is (Theta(L^5)), a factor
(m^{1/2-o(1)}) above its proposed global scale.

Consequently all master gates obtained by applying colorwise
Cauchy--Schwarz and then bounding (mathfrak A_{L,J}) separately must be
retired.  A viable proof has to keep the parent-child dot product itself,
or charge each coherent child core before reverse-multiplicity
amplification.

## 2. The planted seed and a safe reservoir

Fix (L\ge2), put

\[
 M=64L^2,
 \qquad
 S_L=\{s_i=(i,i^2):0\le i<2L\},                     \tag{2.1}
\]

and take as the candidate reservoir

\[
 U=\{(X,Y)\in\mathbb Z^2:
       2L\le X\le M,
       16L^2\le Y\le32L^2\}.                        \tag{2.2}
\]

Thus (|U|=\Theta(M^2)), all candidate horizontal coordinates are
different from the seed coordinates, and the whole construction lies in
([0,M]^2).

The seed is distance-Sidon.  For an edge (i<j), put

\[
 a=j-i,\qquad s=i+j.
\]

Its squared length is (a^2(1+s^2)), with (1\le a\le s).  The standard
negative-Pell gap argument shows that two such values are equal only when
both (a) and (s) agree; it is reproduced in
`SUPPORT_WEIGHTED_HEISENBERG_PARABOLA_BARRIER.md`, Section 4.

The high strip has a useful stronger property:

\[
 \boxed{
 \text{no equal-distance relation on }S_L\cup U
 \text{ uses exactly one vertex of }U.}              \tag{2.3}
\]

There are only two cases.  First, every candidate-seed distance is larger
than every seed-seed distance.  Indeed

\[
 \min_{u\in U,s\in S_L}|u-s|^2>(12L^2)^2=144L^4,
\]

whereas

\[
 \max_{s,t\in S_L}|s-t|^2<4L^2+16L^4<20L^4.
\]

Second, a candidate (u=(X,Y)) cannot be equidistant from two seed points
(s_i,s_j), (i<j).  On writing (s=i+j\ge1), equality of the two
squared distances reduces exactly to

\[
 2X+2sY=s(1+i^2+j^2).                                \tag{2.4}
\]

The left side is at least (32sL^2), while the right side is less than
(s(1+8L^2)<9sL^2).  This proves (2.3).

## 3. A seeded distance-Sidon extension lemma

Let

\[
 \Delta_M=\max_{1\le n\le2M^2}r_2(n),               \tag{3.1}
\]

where (r_2(n)) is the number of ordered integral representations of
(n) as a sum of two squares.  The divisor bound gives

\[
 \Delta_M\le4\max_{n\le2M^2}\tau(n)=M^{o(1)}.       \tag{3.2}
\]

We prove that (S_L) extends inside (S_L\cup U) to a distance-Sidon set
of size

\[
 \boxed{k\gg M^{2/3}/\Delta_M.}                     \tag{3.3}
\]

We impose two harmless additional requirements on the extension:

1. no two chosen candidates have the same first coordinate;
2. no new pair lies on any of the planted derivative relations
   
   \[
    v_x-u_x=q,\qquad v_y-u_y=2qu_x+q^2,
    \qquad1\le q\le L.                              \tag{3.4}
   \]

First remove from (U) every candidate which forms (3.4) with a seed
point.  There are only (O(L|S_L|)=O(M)) such candidates, so the remaining
reservoir (U_0) still has size (Theta(M^2)).

Choose every point of (U_0) independently with probability

\[
 p=\varepsilon\Delta_M^{-1}M^{-4/3},                \tag{3.5}
\]

where (\varepsilon>0) is a sufficiently small absolute constant.
An equal-distance relation is a pair of distinct unordered edges with the
same squared length.  If it uses exactly (q\in\{2,3,4\}) candidate
vertices, the number (H_q) of such relations obeys

\[
 \boxed{
 H_q\ll \Delta_M M^{2(q-1)}|S_L|^{4-q}.}            \tag{3.6}
\]

To see this, fix the endpoint-role pattern, choose (q-1) candidate
vertices and at most (4-q) seed vertices, and leave a candidate endpoint
of one edge last.  Its mate and the squared length are then fixed, so the
last endpoint lies on an integral circle with at most (Delta_M) points.
If the two edges share a vertex, choose a leaf endpoint last.  There are
only constantly many role patterns.  Repeated seed slots only decrease the
count.  Since (|S_L|=2L=O(M^{1/2})), (3.6) gives

\[
 H_2\ll\Delta_MM^3,qquad
 H_3\ll\Delta_MM^{9/2},qquad
 H_4\ll\Delta_MM^6.                                 \tag{3.7}
\]

The same-first-coordinate pairs number (O(M^3)).  The candidate pairs
satisfying one of (3.4) number (O(LM^2)=O(M^{5/2})), because (q) and
the first endpoint determine the second endpoint.

The expected selected size is

\[
 \mathbb E|X|=p|U_0|\gg
 \varepsilon\Delta_M^{-1}M^{2/3}.                  \tag{3.8}
\]

The expected numbers of selected forbidden objects are, respectively,

\[
\begin{array}{c|c}
\text{object}&\text{expectation}\
\hline
q=2\text{ distance relation}
 &O(\varepsilon^2\Delta_M^{-1}M^{1/3})\\
q=3\text{ distance relation}
 &O(\varepsilon^3\Delta_M^{-2}M^{1/2})\\
q=4\text{ distance relation}
 &O(\varepsilon^4\Delta_M^{-3}M^{2/3})\\
\text{same first coordinate}
 &O(\varepsilon^2\Delta_M^{-2}M^{1/3})\\
\text{new planted-line incidence}
 &O(\varepsilon^2\Delta_M^{-2}M^{-1/6}).
\end{array}                                         \tag{3.9}
\]

The first, second, fourth, and fifth lines are (o(\mathbb E|X|)).  The
third is at most a small fixed fraction of (mathbb E|X|) after choosing
(\varepsilon) small.  Hence some outcome has selected size minus the
number of forbidden objects (gg M^{2/3}/\Delta_M).  Delete one candidate
point from each remaining forbidden object.  Property (2.3) ensures that
every equal-distance collision has at least one deletable candidate, and
deletion creates no new collision.  This proves (3.3), including both
additional requirements.

Finally trim the extension, if necessary, so that

\[
 k=\Theta(M^{2/3}/\Delta_M).                         \tag{3.10}
\]

Since (Delta_M=M^{o(1)}), the result is exponent-critical:

\[
 m=M+1,qquad k=m^{2/3-o(1)},qquad
 {m^2\over k^3}=m^{o(1)}.                           \tag{3.11}
\]

## 4. The planted colored profile is unchanged

Distinct first coordinates make the final set graph-like in the horizontal
direction.  Requirement (3.4) says that for every (1\le q\le L), the
derivative line

\[
 d_q(r)=2qr+q^2                                      \tag{4.1}
\]

has exactly its planted support

\[
 \{0,\ldots,2L-q-1\},qquad |S_q|=2L-q.             \tag{4.2}
\]

Select these (L) parent patches.  They all lie in the dyadic parent band
([L,2L)), with

\[
 \lambda_q=2q,qquad \alpha_q=q^2,qquad
 A_q=\alpha_q-q^2=0.                                \tag{4.3}
\]

For (c>d), put (h=c-d).  The unique normalized active color is

\[
 (\theta,B)=(2,0),\qquad
 C_h(2,0)=L-h,qquad K_h(2,0)=2L-h.                 \tag{4.4}
\]

Thus all (1\le h<L) lie in the child band (J=L), and

\[
 \boxed{
 \mathfrak A_{L,L}
 =\sum_{h=1}^{L-1}(L-h)^2
 ={(L-1)L(2L-1)\over6}
 =\Theta(L^3)=\Theta(M^{3/2}).}                     \tag{4.5}
\]

## 5. Exact exponent comparison

Write (Delta=Delta_M=M^{o(1)}).  From (3.10),

\[
 k=\Theta(M^{2/3}/\Delta),qquad
 J=L=\Theta(M^{1/2}),qquad
 S=k^3+m^2=\Theta(M^2).                             \tag{5.1}
\]

Moreover

\[
 {k^2J^5\over k^3J^3}={J^2\over k}
 =M^{1/3+o(1)}\longrightarrow\infty.                \tag{5.2}
\]

Therefore the proposed bound (1.3) is at most

\[
 m^{o(1)}{M^8\over k^8J^5}
 =m^{o(1)}\Delta^8M^{1/6}
 =M^{1/6+o(1)}.                                     \tag{5.3}
\]

Comparison with (4.5) proves the factor (M^{4/3-o(1)}) in (1.4).

The same family also kills the proposed weighted master estimate.  Its
planted weighted mass is

\[
 W_L=\sum_{h=1}^{L-1}(L-h){2L-h\choose3}
 =\Theta(L^5)=\Theta(M^{5/2}),                      \tag{5.4}
\]

whereas

\[
 m^{o(1)}{S^2\over k^3}=M^{2+o(1)}.                \tag{5.5}
\]

The polynomial excess in (5.4) is an amplification artifact.  Before
reverse parent multiplicity is inserted, the actual derivative triples in
the planted lines total

\[
 T_L=\sum_{q=1}^{L}{2L-q\choose3}
 ={2L\choose4}-{L\choose4}
 =\Theta(L^4)=\Theta(M^2)=\Theta(m^2).              \tag{5.6}
\]

This is precisely the ambient square budget.  A direct proof should pay
(5.6) once; the colored (L^2) route pays it (L) times.

## 6. Stress-family verdicts

The single planted parabola is already stronger than the requested
multi-arc, modular-parabola, matching-line, and Golomb hybrid stresses.
For completeness:

* **Disjoint quadratic arcs.**  Their internal colored energy is
  (Theta(bL^3)), but a generic finite-avoidance realization has only a
  polynomial, not critical, height guarantee.  The seeded extension above
  removes that ambiguity with (b=1) and gives an exponent-critical
  realization.
* **Modular parabola Euclideanizations.**  An affine metric separation can
  make a fixed modular parabola distance-Sidon, but its anisotropy changes
  the derivative colors and its known realizations do not improve on the
  exact integral planted arc.  No modular input is needed for the kill.
* **Pure matching-rich lines.**  One rich matching line has large child
  occupancy but does not by itself create the coherent reverse color
  multiplicity (C_h=L-h).  Polynomial-height finite avoidance therefore
  does not reach the present target without an additional parent gadget.
* **Golomb hybrids.**  A collinear Golomb component has normalized
  curvature (	heta=0).  Fixed-shift vector injectivity gives child
  occupancy at most one, so it is inactive in (mathfrak A_{L,J}).
  Its quadratic span also supplies only (O(M^{1/2})) points at height
  (M), not the needed critical filler.

The durable conclusion is not merely that the known examples happen to be
paid by (m^2).  It is that an actual exponent-critical distance-Sidon set
can contain the sharp (m^2)-paid parabola core, and separate parent-energy
control then amplifies that legal core by a polynomial factor.

## 7. Verification

Run

```text
python3 phase2/loop/erdos1208/verify_critical_planted_parabola_colored_energy_counterexample.py
```

The verifier checks the seed distance-Sidon lemma through (L=64), the
safe-strip inequalities, the exact planted parent/child profile, the
alteration exponent ledger, the target exponent gap, and a deterministic
finite greedy extension retaining exact planted supports.
