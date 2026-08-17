# Rotated difference overlap: an intermediate exponent theorem

This note isolates a pointwise statement strictly weaker than the full
rotated-energy conjecture, but already strong enough to improve Erdős 1208 by
a large amount.  It also records two computational stress tests and the exact
places where the obvious graph and Costas-array arguments stop.

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

for some \(0\le\theta\le1\).  Since

\[
 \sum_t\rho_B(t)=|B|^2=k^4,
\]

(3)--(5) imply

\[
 E^+(B)=\sum_t\rho_B(t)^2
 \le k^4+k^{1+\theta+o(1)}k^4
 =k^{5+\theta+o(1)}.                             \tag{6}
\]

The cross-sum factorization gives

\[
 \mathcal E_J(A)
 \le\sqrt{E^+(B)E^+(A)}
 \le k^{7/2+\theta/2+o(1)},                      \tag{7}
\]

because \(E^+(A)=2k^2-k\).  On the other hand the image of the rotated
triple map lies in a box of \(O(m^2)\) lattice points, so

\[
 \mathcal E_J(A)\gg k^6/m^2.                    \tag{8}
\]

Comparing (7) and (8) yields

\[
 k\le m^{4/(5-\theta)+o(1)}.                    \tag{9}
\]

Applied to the \(m\) by \(m\) grid, (9) proves the conditional upper bound

\[
 \boxed{F_2(n)\le n^{2/(5-\theta)+o(1)}.}        \tag{10}
\]

In particular:

* \(M_A(t)\le k^{1+o(1)}\) gives \(F_2(n)\le n^{2/5+o(1)}\);
* \(M_A(t)\le k^{3/2+o(1)}\) gives
  \(F_2(n)\le n^{4/9+o(1)}\);
* any \(\theta<0.9562\) already improves the local unconditional exponent
  \(0.494586\).

This pointwise route cannot by itself reach the conjectural cube root.  The
baseline \(k\)-multiplicity terms in (2) make (6) naturally fifth-power.  A
cube-root proof still needs the stronger total-energy cancellation described
in `ROTATED_TRIPLE_ENERGY.md`.

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

Any \(\delta>0.0438\) improves the current best upper exponent through (10),
while \(\delta=1\) gives the fifth-power energy theorem and exponent \(2/5\).
The likely proof needs a stability theorem for a difference set with large
overlap under a quarter-turn about an external centre.  Standard BSG sees only
one difference set and loses the rotation; pair-codegree and generic Costas
cross-correlation statements see too little of the Euclidean norm condition.
