# Rotated difference overlap: an intermediate exponent theorem

This note isolates a pointwise statement which, in its natural linear form,
settles the power-law order in Erdős 1208.  It also records two computational
stress tests and the exact places where the obvious graph and Costas-array
arguments stop.

Let

\[
 A\subset [m]^2,\qquad |A|=k,
\]

be distance-Sidon, let \(J(x,y)=(-y,x)\), and put

\[
 D=(A-A)\setminus\{0\},\qquad B=A+JA.
\]

As in `ROTATED_TRIPLE_ENERGY.md`, every nonzero oriented difference of \(A\)
has a unique representation and

\[
 |B|=k^2,\qquad D\cap JD=\varnothing.             \tag{1}
\]

## 1. Exact autocorrelation formula

Write

\[
 \rho_A(x)=|\{(a,b)\in A^2:a-b=x\}|.
\]

Then \(\rho_A(0)=k\), while \(\rho_A(x)=1_D(x)\) for \(x\ne0\).  Directness
of \(A+JA\) gives, for every translation \(t\),

\[
 \rho_B(t)
 =\sum_{x+Jy=t}\rho_A(x)\rho_A(y).               \tag{2}
\]

For \(t\ne0\), at most one summand in (2) has \(x=0\) or \(y=0\), by (1).
Consequently

\[
 \rho_B(t)\le k+M_A(t),                           \tag{3}
\]

where

\[
 M_A(t):=|D\cap(t-JD)|.                           \tag{4}
\]

Thus the new local target is an overlap between the complete directed
difference set and a translated quarter-turn of itself.

## 2. Conditional exponent theorem

Suppose that, uniformly for all distance-Sidon \(A\) and all \(t\ne0\),

\[
 M_A(t)\le k^{1+\theta+o(1)}                     \tag{5}
\]

for some \(0\le\theta\le1\).  Every representation counted by \(M_A(t)\)
has \(t\in D+JD\), which lies in a box of \(O(m^2)\) lattice positions, and

\[
 \sum_t M_A(t)=|D|^2=k^2(k-1)^2.                 \tag{6}
\]

Consequently

\[
 k^{4-o(1)}\ll m^2k^{1+\theta+o(1)},
\]

and hence

\[
 k\le m^{2/(3-\theta)+o(1)}.                    \tag{7}
\]

Applied to the \(m\) by \(m\) grid, (7) proves the conditional upper bound

\[
 \boxed{F_2(n)\le n^{1/(3-\theta)+o(1)}.}        \tag{8}
\]

In particular:

* \(M_A(t)\le k^{1+o(1)}\) proves
  \(F_2(n)\le n^{1/3+o(1)}\), matching the universal lower bound and
  resolving the power-law order;
* \(M_A(t)\le k^{3/2+o(1)}\) gives
  \(F_2(n)\le n^{2/5+o(1)}\);
* any \(\theta<0.9781\) already improves the local unconditional exponent
  \(0.494586\).

Equivalently, any fixed estimate

\[
 M_A(t)\le k^{2-\delta}
\]

with \(\delta>0.0219\) improves the current theorem, and \(\delta=1\) solves
the problem at the conjectured exponent.

### A weaker energy consequence

For completeness, (5) also feeds the cross-sum energy factorization.  Since

\[
 \sum_t\rho_B(t)=|B|^2=k^4,
\]

(3)--(5) imply

\[
 E^+(B)=\sum_t\rho_B(t)^2
 \le k^4+k^{1+\theta+o(1)}k^4
 =k^{5+\theta+o(1)}.                             \tag{9}
\]

The cross-sum factorization gives

\[
 \mathcal E_J(A)
 \le\sqrt{E^+(B)E^+(A)}
 \le k^{7/2+\theta/2+o(1)},                      \tag{10}
\]

because \(E^+(A)=2k^2-k\).  The rotated-triple lower bound is

\[
 \mathcal E_J(A)\gg k^6/m^2.                    \tag{11}
\]

Comparing (10) and (11) yields only

\[
 k\le m^{4/(5-\theta)+o(1)}.                    \tag{12}
\]

The direct support count (6)--(8) is strictly stronger for \(\theta<1\); the
energy estimate remains useful only as a connection with the earlier Fourier
formulation.

## 3. What pair-injectivity gives, and why it is insufficient

A representation counted by \(M_A(t)\) is a quadruple

\[
 a-b+J(c-d)=t.                                   \tag{11}
\]

Any two of the four coordinates, one from the first directed edge and one
from the second, determine the remaining solution uniquely.  For example,
two different solutions sharing \(a,c\) would give

\[
 b-b'=-J(d-d'),
\]

contradicting distance uniqueness.  The within-edge pairs \((a,b)\) and
\((c,d)\) are unique as well, by oriented-difference uniqueness.  Hence the
solutions form a four-partite linear hypergraph in which every two-coordinate
projection is injective.

This gives only \(M_A(t)\le k^2\).  Abstract linear four-partite hypergraphs
of size \(k^2\) exist (orthogonal Latin-square/MDS constructions), so a proof
must use the Euclidean equation in (11), not just pair codegrees.

One tempting strengthening is also false.  Regard the domain cells
\((a,c)\) of (11) as a bipartite graph on two copies of \(A\).  Exact greedy
examples contain many four-cycles.  For sides 20, 40, 80, 120 the maximizing
nonzero translations had respectively

\[
 (k,\rho_B(t),C_4)=(12,29,11),(19,49,30),
 (31,78,45),(41,117,87).
\]

Thus a bare \(C_4\)-free/Kővári--Sós--Turán proof is unavailable, although
the observed four-cycle count remains sparse.

A larger fixed forbidden biclique does not rescue this route.  Exhaustive
translation scans of the small greedy examples suggested \(K_{4,4}\)-freeness,
but this was a sampling artefact.  For any prescribed \(s\), choose source
labels \(a_i,c_j\), target first labels \(b_{ij}\), and a translation \(t\)
generically, and define

\[
 d_{ij}=c_j-Ja_i+Jb_{ij}+Jt.
\]

Then

\[
 a_i+Jc_j-(b_{ij}+Jd_{ij})=t
\]

for all \(i,j\), so the translation graph contains \(K_{s,s}\).  The exact
script `search_biclique_realization.py` found rational/integral
distance-Sidon realizations for \(s=2,3,4\), using respectively 12, 24, and 40
points.  Thus neither \(K_{3,3}\) nor \(K_{4,4}\) is universally forbidden.

The generic construction spends new target endpoints for essentially every
biclique edge, so it produces only linear total overlap relative to the final
number of points.  This pinpoints the actual issue: a superlinear overlap must
reuse the same \(k\) endpoints across many such local grids.  A successful
extremal theorem has to exploit that global reuse; no bounded forbidden
configuration can prove the required power saving.

## 4. Costas and distinct-difference stress test

The set \(A\) is a distinct-difference configuration, but with the stronger
condition that the norms of all its nonzero differences are distinct as well.
The distinction is essential.  Blackburn--Etzion--Martin--Paterson construct
ordinary distinct-difference configurations with extremely rich two-hop
coverage; vector uniqueness alone therefore cannot control (4).  See
<https://arxiv.org/abs/0811.3896>.

Costas arrays provide a particularly dense stress test: they have \(k\)
points in a \(k\) by \(k\) box and \(k(k-1)\) distinct oriented vectors, but
their Euclidean lengths repeat.  The script
`analyze_affine_costas_energy.py` takes Welch Costas arrays, finds a small
integral shear/stretch which separates every squared Euclidean length, and
then computes \(E^+(A+JA)\) and the largest nonzero autocorrelation exactly.

For \(k=6,10,12,16,18,22,28,30,36,40,42\), the largest nonzero overlap
divided by \(k\) was between 1.02 and 1.33.  The ratio
\(E^+(A+JA)/k^5\) decreased from 0.73 to about 0.10 over the tested range.
Thus this natural high-density distinct-difference family does not falsify
(5) with \(\theta=0\); imposing radial uniqueness forces enough anisotropy to
collapse its rotated common energy.

These calculations are evidence only.  The relevant Costas literature studies
ordinary cross-correlation of two dot arrays, not the second-order overlap of
their complete difference sets in (4).  In particular, the known small
correlation of an array with some rotated/flipped images does not prove (5).

## 5. Live problem

The most useful next lemma is now explicit:

> Prove a fixed power saving
> \(\max_{t\ne0}|(A-A)\cap(t-J(A-A))|\le k^{2-\delta}\)
> for every planar distance-Sidon set \(A\).

Any \(\delta>0.0219\) improves the current best upper exponent through (8),
while \(\delta=1\) gives the full cube-root solution directly from (6).
The likely proof needs a stability theorem for a difference set with large
overlap under a quarter-turn about an external centre.  Standard BSG sees only
one difference set and loses the rotation; pair-codegree and generic Costas
cross-correlation statements see too little of the Euclidean norm condition.

### Failed digit-tensor counterexample

An exact search found a 13-point distance-Sidon seed with
\(M_A((-2,-1))=34\), which at first appears tensorizable.  The naive product

\[
 A^{(d)}=\left\{\sum_j\gamma_j a_j:a_j\in A\right\}
\]

does multiply the 34 overlap solutions coordinate by coordinate.  It does
**not** remain distance-Sidon, even for algebraically generic Gaussian scales
\(\gamma_j\).  If two endpoints agree in one digit, that digit is invisible
in their difference; changing the common digit produces a second edge with
the identical displacement and length.  In particular, every Cartesian digit
product has unavoidable cylinder collisions.  Restricting to a code with no
such repeated difference words returns the ordinary Sidon-code square-root
loss and no longer preserves enough tensor edges.  Thus this tempting
counterexample to the linear overlap target fails.

Affine images of one-dimensional parabola sets were also tested because their
chord vectors have the explicit form \((h,hs)\) and a generic anisotropic
metric separates all lengths.  Exact searches over small rational scalings
gave sublinear-to-linear maximum overlap, not a counterexample.  The two
coordinate equations determine both endpoint sums from the two gaps, leaving
a divisor-type rather than a product-sized family.
