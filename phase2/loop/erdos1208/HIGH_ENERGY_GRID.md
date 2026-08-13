# The high-energy branch on the square grid

Let (P=[m]^2), put (N=m^2), and let (r_s) be the number of unordered
pairs of points of (P) whose squared distance is (s).  This note isolates
what the usual energy, codegree, dependent-random-choice, and additive-energy
inputs can and cannot see.  The conclusion is negative but useful: all of
those statistics stop exactly at the cube-root scale on the grid.

## 1. The conflict-hypergraph profile

Let (R_2(s)) be the number of integer vectors ((u,v)) satisfying
(u^2+v^2=s).  The divisor bound gives, uniformly for (s=O(N)),

\[
 R_2(s)=N^{o(1)}.
\]

There are (O(N)) possible squared distances, while

\[
 \sum_s r_s=\binom N2,
 \qquad r_s\le \frac N2R_2(s)=N^{1+o(1)}.
\]

Cauchy--Schwarz and the last bound therefore give

\[
 \sum_s r_s^2=N^{3+o(1)}.                         \tag{1.1}
\]

Let (mathcal H_4) be the 4-uniform hypergraph whose edges are 4-sets that
admit a partition into two equal-length pairs.  Pair-pair coincidences that
share an endpoint are isosceles triples.  At a fixed apex and radius there
are at most (R_2(s)=N^{o(1)}) grid points, so the total number of such
triples is (N^{2+o(1)}).  Removing these and the identical-pair terms from
(1.1), and observing that a 4-set supports at most three pairings, proves

\[
 |\mathcal H_4|=N^{3+o(1)}.                       \tag{1.2}
\]

The same circle-counting argument gives the ordinary codegrees

\[
 \Delta_1(\mathcal H_4)\le N^{2+o(1)},\qquad
 \Delta_2(\mathcal H_4)\le N^{1+o(1)},\qquad
 \Delta_3(\mathcal H_4)\le N^{o(1)}.              \tag{1.3}
\]

Indeed, after fixing three vertices, the fourth lies on one of three fixed
lattice circles.  After fixing two, either they form one of the equal edges,
leaving at most (r_s) choices, or one may choose a third vertex and place
the fourth on a fixed circle.  The one-vertex bound follows similarly by
choosing two further vertices before placing the last one.  The 3-uniform
isosceles-conflict hypergraph has only (N^{2+o(1)}) edges.

This profile alone cannot force an independent set larger by any fixed power
than (N^{1/3}).  For comparison, the random hypergraph
(G=H^{(4)}(N,c/N)) has, with high probability, the same bounds

\[
 |G|=\Theta(N^3),\quad
 \Delta_1=O(N^2),\quad \Delta_2=O(N),\quad
 \Delta_3=O(\log N/\log\log N),
\]

but

\[
 \alpha(G)=O((N\log N)^{1/3}).                    \tag{1.4}
\]

For (1.4), the expected number of independent (s)-sets is at most

\[
 \binom Ns(1-c/N)^{\binom s4}
 \le (eN/s)^s\exp(-c\binom s4/N),
\]

which tends to zero for (s=A(N\log N)^{1/3}) and sufficiently large fixed
(A).  Standard Chernoff bounds give the displayed codegrees.  Consequently,
no container, nibble, local-lemma, or abstract hypergraph theorem whose
hypotheses use only (1.2)--(1.3) can beat the cube-root power on the grid.
It must exploit an additional arithmetic or Euclidean forbidden pattern.

## 2. The exact multiplicity-scale inverse statement

Suppose more generally that

\[
 \sum_s r_s^2\ge N^{3-o(1)},\qquad
 \sum_s r_s=\Theta(N^2),\qquad
 r_s\le N^{1+o(1)}.
\]

Some dyadic level (R\le r_s<2R), containing (D_R) distance values,
satisfies (D_RR^2\ge N^{3-o(1)}).  Since (D_RR\le N^2), this forces

\[
 R=N^{1+o(1)},\qquad D_R=N^{1+o(1)}.               \tag{2.1}
\]

Thus near-cubic grid energy is carried by roughly (N) colours, each on
roughly (N) edges.  At every vertex the degree in one colour is only
(N^{o(1)}).  This is the one-factorization scale at which generic proper or
locally bounded colourings have rainbow cliques of only
(N^{1/3+o(1)}).  The inverse statement (2.1) therefore locates the hard
case but does not solve it: the missing datum is the compatibility among the
matchings arising from lattice translations and rotations.

## 3. Why standard inverse tools return the grid itself

On pair-vertices, the graph joining two pairs of equal length is exactly

\[
 \bigsqcup_s K_{r_s}.
\]

Dependent random choice can only return one monochromatic clique and gives
no simultaneous control of the other (N^{1+o(1)}) energetic colours.

Additive-energy increment also stops immediately.  For an oriented grid
displacement (u=(u_1,u_2)),

\[
 r_P(u)=(m-|u_1|)(m-|u_2|),
\]

and hence

\[
 \sum_u r_P(u)^2
 =\left(m^2+2\sum_{j=1}^{m-1}j^2\right)^2
 =\Theta(m^6)=\Theta(N^3).                        \tag{3.1}
\]

Balog--Szemerédi--Gowers or a Freiman-type inverse theorem applied to this
subenergy merely recovers a rank-two generalized arithmetic progression:
the square grid.  Any inverse theorem terminating at a bounded-rank
progression still has to solve the norm-Sidon extraction problem inside that
progression.

The same issue appears in the rigid-motion/Elekes--Sharir encoding.  A large
second moment of motion incidences need not, from the incidence bound alone,
force a rich motion or an approximate group.  What would be useful is a
near-extremal stability theorem for the Guth--Katz line configuration that
either produces a tractable one-dimensional component or exposes extra
arithmetic constraints among the rank-two translation component.

## 4. Two concrete algebraic handles

For arbitrary planar points (p_i=(x_i,y_i)), the squared-distance matrix is

\[
 D_{ij}=u_i+u_j-2x_ix_j-2y_iy_j,qquad
 u_i=x_i^2+y_i^2.                                  \tag{4.1}
\]

Thus (operatorname{rank}D\le4), and (D) is conditionally negative
semidefinite.  Erdős 1208 can be viewed as finding a large principal
submatrix whose off-diagonal entries are all different in this special
rank-four matrix class.  Generic semialgebraic Ramsey bounds for the
four-variable equality relation are weaker than the Guth--Katz energy input,
but (4.1) suggests a different target: a rainbow-principal-submatrix theorem
that uses low rank together with conditional negative definiteness.  The
rank-two additive model (D_{ij}=a_i+a_j) has square-root Sidon extraction,
so low rank can matter; the quadratic coupling in (4.1) is the essential
planar difficulty.

The two credible lower-bound routes are therefore:

1. a stability/inverse theorem for near-extremal Elekes--Sharir line
   intersections, with a conclusion stronger than “bounded-rank GAP”; or
2. a rainbow principal-submatrix theorem specialized to Euclidean distance
   matrices of rank at most four.

Neither statement is presently available.  They identify information that
the sharp grid profile (1.2)--(1.3) does not already rule out.

## 5. Computational sanity check and prior art

An exact CP-SAT model with one binary variable per grid point and at most one
selected pair in every squared-distance class reproduces

\[
 1,2,3,4,5,6,7,7
\]

for grids of side (1,ldots,8).  These values are validation rather than a
new computation: [OEIS A271490](https://oeis.org/A271490) records the exact
sequence through side 17 as

\[
 1,2,3,4,5,6,7,7,8,9,10,10,11,11,12,13,13.
\]

Direct energy computations for sides
(8,16,32,64,100,200,500,1000) give respectively

\[
 \frac{E(P)}{N^3}=2.802,3.577,4.357,5.140,5.644,6.426,7.460,8.242,
\]

and (E(P)/(N^3\log N)) decreases from (0.674) to (0.597).  This is
consistent with the sharp (N^3\log N) order and confirms that the grid is
not a cosmetic edge case.  Random-greedy witnesses empirically track the
(N^{1/3}=m^{2/3}) scale, but do not improve the published constructions and
carry no evidentiary weight toward an asymptotic theorem.

Simple structural guesses also fail.  Exact 11-by-11 solutions can put four
chosen points in one row, and one-dimensional Golomb rulers permit unbounded
row occupancy.  The always-valid row and column inequalities are only

\[
 \sum_i\binom{r_i}{2}\le m-1,
 \qquad
 \sum_j\binom{c_j}{2}\le m-1,
\]

because every horizontal or vertical squared distance is globally unique.
They imply only the square-root-scale upper bound (O(m)), not the desired
(O(m^{2/3+o(1)})).
