# Full-solution attack on Erdős #669 (2026-08-13)

## Executive verdict

This attack did **not** fully solve Erdős #669.  For every fixed \(k\geq4\),
the existence and values of

\[
 \lim_{n\to\infty}\frac{f_k(n)}{n^2},\qquad
 \lim_{n\to\infty}\frac{F_k(n)}{n^2}
\]

remain open.  The standard routes through superadditivity, random sampling,
point cloning, and abstract design theory all have explicit gaps documented
below.

The attack did produce a proof-grade partial result.  Let \(A(r)\) be the
minimum area of a convex lattice \(r\)-gon.  A lattice-zonotope construction
gives, for every fixed \(k\geq3\),

\[
 \boxed{\quad f_k(n),F_k(n)\geq
 \frac{n^2}{4A(2k)}-O_k(n).\quad}
\tag{A}
\]

The construction is exact, has an independent incidence enumerator, and is
optimal within the whole lattice multigrid/parallel-strip scheme.  For
\(k=5,6,7,8,11\), its coefficients exceed those printed by Palásti in 1986.
Direct searches did not find the orchard application or those constants, but
novelty is **not cleared**: the determinant optimization is classical, and the
\(k=4\) instance was already described on a 2019 Chinese webpage.

## 1. Current numerical window

The known cases are \(k=2\), with constant \(1/2\), and \(k=3\), with constant
\(1/6\).  For the first open values, the strongest lower bound located in this
attack and the upper-bound envelope derived in Section 5 give:

| \(k\) | certified lower coefficient for both \(f_k,F_k\) | upper coefficient for \(F_k\) | lower-bound source |
|---:|---:|---:|:---|
| 4 | \(1/28\approx0.0357143\) | \(1/14\approx0.0714286\) | 2019 octagonal construction |
| 5 | \(1/56\approx0.0178571\) | \(1/25=0.04\) | zonotope theorem |
| 6 | \(1/96\approx0.0104167\) | \(1/39\approx0.0256410\) | zonotope theorem |
| 7 | \(1/160=0.00625\) | \(1/55\approx0.0181818\) | zonotope theorem |
| 8 | \(1/236\approx0.00423729\) | \(1/73\approx0.0136986\) | zonotope theorem |
| 9 | \(3/1000=0.003\) | \(2/189\approx0.0105820\) | Palásti |
| 10 | \(1/480\approx0.00208333\) | \(1/120\approx0.00833333\) | Palásti |
| 11 | \(1/656\approx0.00152439\) | \(2/297\approx0.00673401\) | zonotope theorem |

Every statement in this table is about a liminf or limsup.  It must not be
rewritten using a limit until existence is proved.

There is nevertheless a sharp order-of-magnitude estimate when the dependence
on \(k\) is retained.  Szemerédi--Trotter gives

\[
 F_k(n)=O\!\left(\frac{n^2}{k^3}+\frac nk\right),
\]

while (A), together with \(A(2k)=\Theta(k^3)\), gives normalized liminf
at least \(1/[4A(2k)]=\Theta(k^{-3})\).  Thus the extremal functions have
quadratic coefficients of order \(k^{-3}\), up to absolute factors, despite
the unknown fixed-\(k\) limits.

## 2. Three structural lemmas for the limit problem

Throughout, (a_k) denotes either (f_k) or (F_k), and (k\geq3) is
fixed.

### Lemma 1: generic union is superadditive

For all (m,n),

\[
 a_k(m+n)\geq a_k(m)+a_k(n).
\tag{1}
\]

Take extremal projective point sets (P,Q).  Choose a projective
transformation (T) so that no line containing at least three points of
(P\cup TQ) is mixed.  The forbidden transformations satisfy one of finitely
many conditions

\[
 Tq\in\overline{p_1p_2}
 \quad\hbox{or}\quad
 p\in T\overline{q_1q_2},
\]

together with collision conditions.  Each is a proper algebraic subset of
\(\mathrm{PGL}(3,\mathbb R)\), so their finite union can be avoided.  Internal
exact- and at-least-(k) lines are preserved and no mixed rich line is
created.

This is not quadratic superadditivity.  Fekete's lemma applied to (1) controls
(a_k(n)/n), not (a_k(n)/n^2).

### Lemma 2: sampling downward

For (N\geq n\geq k),

\[
 a_k(n)\geq \frac{(n)_k}{(N)_k}\,a_k(N).
\tag{2}
\]

For (f_k), sample a uniformly random (n)-subset of an extremal
(N)-point set.  An exact-(k) line survives whenever all its points are
sampled.  For (F_k), mark one fixed (k)-subset on each rich line; inclusion
of that subset guarantees survival.  Taking expectations proves (2).

If (n/N\to\alpha), normalizing by (n^2) loses the factor
(\alpha^{k-2}).  This is the precise obstruction to the usual hereditary
sampling proof of convergence.

### Lemma 3: padding and one-step increments

\[
 0\leq a_k(n+1)-a_k(n)\leq
 \left\lfloor\frac{n}{k-1}\right\rfloor.
\tag{3}
\]

The lower bound follows by adding a point outside all determined lines.  For
the upper bound, delete a point (p) from an extremal ((n+1))-point set.  The
only counted lines that can disappear are exact-(k) lines through (p).
Their other (k-1) points are disjoint from line to line.  In the exact case,
lines formerly containing (k+1) points may become exact after deletion, but
that only helps the remaining configuration.

### These properties still do not force a limit

Choose very lacunary integers (M_j) and put

\[
 H_M(x)=
 \begin{cases}
 x^k/M^{k-2},&x\leq M,\\
 Mx,&x\geq M,
 \end{cases}
 \qquad
 B(x)=\varepsilon\sum_j H_{M_j}(x).
\]

Each (H_M) is increasing and superadditive, and (H_M(x)/x^k) is
nonincreasing.  With sufficiently lacunary (M_j) and small
(\varepsilon), (B) is (O(x^2)), satisfies the analogues of (2) and (3),
but (B(x)/x^2) has positive limsup and zero liminf.  Thus monotonicity,
superadditivity, exact sampling, linear increments, and a pair budget do not
jointly imply convergence.  A successful proof needs additional geometry.

## 3. Why the obvious quadratic amplifiers fail

A natural strategy replaces every point by (q) nearby points and hopes that
each original (k)-point line produces (q^2) new ones.  The simplest
transverse blow-up loses a fixed factor.

Put the (k) centers at ((i,0)), (0\leq i<k), and replace center (i) by

\[
 C_i=\{(i,\varepsilon s):0\leq s<q\}.
\]

The line joining endpoint labels (a,b) has label

\[
 \frac{(k-1-i)a+ib}{k-1}
\]

over fiber (i).  It meets all fibers at labeled points exactly when
(a\equiv b\pmod{k-1}).  One base line therefore produces only

\[
 \frac{q^2}{k-1}+O(q)
\]

exact-(k) lines, not (q^2).  Small disjoint neighborhoods prevent
off-line clusters from creating contaminating incidences, so the loss is
genuine arithmetic rather than a generic-position oversight.

A generic overlay of (q) projective copies is worse: it gives only
(q a_k(n)) internal rich lines on (qn) points.  Abstract Steiner systems
do achieve the pair-counting density, but for (k\geq3) their absence of
ordinary lines conflicts with Sylvester--Gallai and Melchior; real rank-three
representability is not preserved by design blow-ups.

A universal quadratic amplifier would settle the limit question: it would
replace every (n)-point configuration by ((1+o(1))qn) points with
((1-o(1))q^2a_k(n)) corresponding rich lines.  No such operation is known,
and the calculations above rule out the two immediate candidates.

## 4. The lattice-zonotope lower theorem

Let (v_1,\ldots,v_k\in\mathbb Z^2) be primitive, pairwise nonparallel
vectors spanning the lattice, let (R) be a (90^\circ) lattice rotation,
and define

\[
 Z=\sum_{i=1}^k[0,Rv_i],\qquad
 D=\sum_{i<j}|\det(v_i,v_j)|.
\tag{4}
\]

For every (q\geq1), take every integer-level line

\[
 v_i\mathbin\cdot x=t
\]

that meets (qZ).  If
(w_i=\sum_j|\det(v_i,v_j)|), family (i) has exactly (qw_i+1)
members, so the total line count is

\[
 n_q=\sum_i(qw_i+1)=2Dq+k.
\tag{5}
\]

A finite point has multiplicity (k) precisely when it lies on one member of
every family.  The spanning hypothesis makes its coordinates integral, and
the level bounds are exactly the supporting-strip description of (qZ).
Thus all finite exact-(k) vertices are precisely (qZ\cap\mathbb Z^2).
Since (Z) has area (D) and (2k) primitive boundary edges, Pick's theorem
gives the exact count

\[
 t_k^{\rm fin}=Dq^2+kq+1.
\tag{6}
\]

For (q\geq2), every parallel-family point at infinity has multiplicity
(qw_i+1>k); hence (6) is also the projective exact-(k) count.  Projective
duality and generic padding yield

\[
 f_k(n),F_k(n)\geq\frac{n^2}{4D}-O_k(n).
\tag{7}
\]

There is a necessary sublattice correction.  If the (v_i) span a sublattice
of index (h), the common-level points lie in the dual lattice and the
coefficient is (h/(4D)=1/[4(D/h)]), not (1/(4D)).  A basis change turns
(D/h) into the area of a convex lattice (2k)-gon.

Simpson proved that a minimum-area convex lattice (2k)-gon may be taken
centrally symmetric, and its (k) primitive edge directions generate exactly
the zonotope above.  Consequently the best possible coefficient in this whole
scheme is

\[
 c_k^{\rm zono}=\frac1{4A(2k)},
\]

which proves (A).  Mixed-area inequality also shows that (Z) is the optimal
convex strip window for any fixed directions.

Simpson's tabulated values give

\[
 A(8),A(10),\ldots,A(22)=7,14,24,40,59,87,121,164.
\]

For example, the (k=5) construction has

\[
 n_q=28q+5,\qquad t_5=14q^2+5q+1\quad(q\geq2),
\]

and the (k=6) construction has

\[
 n_q=48q+6,\qquad t_6=24q^2+6q+1.
\]

Bárány and Tokushige proved that
(A(r)/r^3\to\gamma), with their computations suggesting
(\gamma\approx0.0185067).  Hence this construction has asymptotic
coefficient

\[
 c_k^{\rm zono}\sim\frac1{32\gamma}\frac1{k^3}
 \approx\frac{1.68858}{k^3}.
\]

The full proof, direction sets, sublattice audit, and comparisons are in
[`ZONOTOPE_CONSTRUCTION.md`](ZONOTOPE_CONSTRUCTION.md).  Exact projective
enumeration passes for every (4\leq k\leq11), (q=1,2), in
[`verify_zonotope_construction.py`](verify_zonotope_construction.py).

## 5. Audited upper-bound envelope

Let (t_r) count (r)-fold vertices of a real projective line arrangement.
Pair counting and Melchior give

\[
 \binom n2=\sum_{r\geq2}\binom r2t_r,
 \qquad
 t_2\geq3+\sum_{r\geq4}(r-3)t_r.
\]

Therefore

\[
 \limsup_{n\to\infty}\frac{F_k(n)}{n^2}
 \leq\frac1{(k-2)(k+3)}.
\tag{8}
\]

For (k\geq5), Shnurnikov's inequality improves this to

\[
 \limsup_{n\to\infty}\frac{F_k(n)}{n^2}
 \leq\frac1{k^2+3k-15}.
\tag{9}
\]

Bojanowski--Langer gives, when the maximum multiplicity is at most (2n/3),

\[
 \limsup_{n\to\infty}\frac{F_k(n)}{n^2}
 \leq\frac{2}{3k(k-2)}.
\tag{10}
\]

This is asymptotically global.  If a vertex has multiplicity (M>2n/3), put
(B=n-M<n/3).  Every other (k)-fold vertex uses at least (k-1) of the
(B) lines outside the large pencil, and distinct such vertices use distinct
pairs.  Hence

\[
 F_k(n)\leq1+\frac{\binom B2}{\binom{k-1}2},
\]

whose quadratic coefficient is smaller than (10).  The strongest audited
envelope is therefore

\[
 \limsup_{n\to\infty}\frac{F_k(n)}{n^2}\leq
 \begin{cases}
 1/14,&k=4,\\[1mm]
 1/(k^2+3k-15),&5\leq k\leq8,\\[1mm]
 2/[3k(k-2)],&k\geq9.
 \end{cases}
\tag{11}
\]

The same bounds hold for \(f_k\).  Formula (11) is a deduction from published
arrangement inequalities, not a claimed new inequality.

For sufficiently large \(k\), the non-explicit absolute constant in the
Szemerédi--Trotter rich-line bound \(O(n^2/k^3+n/k)\) is asymptotically
stronger than the explicit \(O(n^2/k^2)\) envelope (11).  The point of (11) is
its concrete small-\(k\) coefficients.

## 6. The (k=4) upper-bound bottleneck

For a projective arrangement let

\[
 T=\sum_{r\geq4}t_r,qquad
 \Delta=\sum_{j\geq4}(j-3)f_j,qquad N=\binom n2,
\]

where (f_j) counts (j)-gonal faces.  Euler's formula gives the exact defect
identity

\[
 N-7T
 =3+\Delta+3t_3+
 \sum_{r\geq5}\frac{(r+5)(r-4)}2t_r.
\tag{12}
\]

Thus any sequence approaching the Melchior coefficient (1/14) must be
asymptotically simplicial, have (t_2,t_4\sim n^2/14), and have only
(o(n^2)) triple, higher-multiplicity, and face-defect contributions.  Known
real-arrangement inequalities do not force any term on the right of (12) to
be (\Omega(n^2)).

In a non-near-pencil simplicial arrangement, local adjacency bounds imply
(t_3\geq4+\sum_{r\geq5}(r-4)t_r), but this improves Melchior only by an
additive constant.  It is even sharp at the 13-line (A(13,2)) arrangement,
with ((t_2,t_3,t_4)=(12,4,9)).  A genuine epsilon improvement requires a
new large-(n) realizability or stretchability theorem.

The lower side is

\[
 f_4(n)\geq n^2/28-O(n).
\]

Our exact four-direction model and verifier are useful, but the coefficient is
prior art: Zhao Hui Du's 2019 Chinese webpage gives the asymptotic counts
(14m+O(1)) lines and (7m^2+O(m)) quadruple points, although it mistakenly
prints (1/24) rather than the implied (1/28).

## 7. Classical square-grid baseline

For the square grid (G_m=\{0,\ldots,m-1\}^2), with (N=m^2), the formulas
of Haukkanen and Merikoski give

\[
 F_k(N)\geq
 \left(\frac{3(2k-1)}{\pi^2k^2(k-1)^2}+o(1)\right)N^2
\]

and

\[
 f_k(N)\geq
 \left(
 \frac{6(3k^2-1)}{
 \pi^2k^2(k-1)^2(k+1)^2}+o(1)
 \right)N^2.
\]

These are classical and weaker than the zonotope exact-(k) construction.

## 8. Prior-art and claim status

The source audit covered the original Erdős formulations, Palásti's 1986
paper and visible citations, Elkies's survey, arrangement-inequality surveys,
multigrid/zonotope terminology, exact constant and formula searches, and the
minimum-area lattice-polygon literature.

What is definitely prior art:

- the problem and the request to prove existence of the normalized limits;
- the determinant-area and Ehrhart formulas for lattice zonotopes;
- Simpson's minimizing direction sets and values (A(2k));
- the (k=4), (1/28) octagonal construction;
- all inequalities used in the upper envelope.

What was not located in the sources checked:

- the orchard-problem deduction (f_k(n)\geq n^2/[4A(2k)]-O_k(n));
- the exact (k=5) and (k=6) formulas above;
- the coefficients (1/56,1/96,1/160,1/236,1/656) as rich-line bounds.

The safe description is therefore **apparently unrecorded application and
lower coefficients, pending specialist citation clearance**.  It is not safe
to call them new or state of the art yet.

## 9. What would finish the problem

Any one of the following would be decisive:

1. a lossless asymptotic quadratic amplifier for real rank-three incidence
   structures, proving existence of both limits;
2. a stability theorem reducing quadratic extremizers to bounded rational
   parallel-family templates, where Ehrhart theory applies;
3. a new real-arrangement inequality with a positive sharp (t_4) weight;
4. a classification of asymptotically extremal arrangements for each fixed
   multiplicity.

None was proved here.  The lattice construction is a genuine
template-specific quadratic amplifier, but it cannot amplify an arbitrary
limsup witness, so it does not settle either requested limit.

## Primary sources

- [Erdős Problems #669](https://www.erdosproblems.com/669)
- [Erdős's 1992 formulation](https://lematematiche.dmi.unict.it/index.php/lematematiche/article/download/587/555/)
- [Palásti, *A construction for arrangements of lines with vertices of large multiplicity*](https://real-j.mtak.hu/5463/1/StudScientMath_21.pdf)
- [Simpson, *Convex lattice polygons of minimum area*](https://doi.org/10.1017/S0004972700028525)
- [Bárány--Tokushige, *The minimum area of convex lattice n-gons*](https://www.renyi.hu/~barany/cikkek/94.pdf)
- [Pokora, *Hirzebruch-type inequalities viewed as tools in combinatorics*](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v28i1p9/pdf/)
- [Shnurnikov, *On the number of regions and multiplicities of vertices in plane arrangements*](https://arxiv.org/abs/1203.1296)
- [Szemerédi--Trotter, *Extremal problems in discrete geometry*](https://trotter.math.gatech.edu/papers/38.pdf)
- [Haukkanen--Merikoski, square-grid line counts](https://arxiv.org/abs/1110.6864)
- [Zhao Hui Du's 2019 octagonal construction](https://emathgroup.github.io/blog/orchard-planting-problem/)
