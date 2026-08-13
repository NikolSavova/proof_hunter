# A counting refinement for Erdős problem 838

> Status (2026-08-12): candidate proof, not yet a public claim.  The
> asymptotic/combinatorial spine is complete.  The gluing lemmas are classical
> or classical-adjacent, but their exact orientation and the cap recurrence
> are being independently refereed.  Novelty sweep is in flight.

All logarithms in the theorem and proof are base \(2\).  Write

\[
H(t)=-t\log_2t-(1-t)\log_2(1-t)
\]

for binary entropy, with \(H(0)=H(1)=0\).

## Candidate theorem

Let \(Q_m=T_{m,\lfloor m/2\rfloor}\) be the central cell of the standard
Pascal construction, and let \(V(Q_m)\) be its number of convex-position
subsets.  Then

\[
\log_2 V(Q_m)\leq
\left(1-\frac1{4\ln2}+o(1)\right)m^2.             \tag{T1}
\]

Consequently, if \(f(N)\) is the largest integer such that every \(N\)-point
set in general position in the plane determines at least \(f(N)\) such
subsets, then

\[
\limsup_{N\to\infty}
\frac{\log_2 f(N)}{(\log_2N)^2}
\leq 1-\frac1{4\ln2}=0.6393262398\ldots .
\]

Thus the presently recorded base-2 window
\(1/4\leq\liminf\leq\limsup\leq1\)
would improve to

\[
\frac14\leq\liminf\leq\limsup\leq
1-\frac1{4\ln2}=0.6393262398\ldots .
\]

## 1. The Pascal cells

Use the standard Pascal-triangle construction.  Its cell \(T_{m,i}\), for
\(0\leq i\leq m\), has

\[
|T_{m,i}|={m\choose i}.
\]

The boundary cells are singletons.  Use the orientation in the proof of
Morris--Soltan Theorem 2.5: an interior cell is the separated union of a left
copy \(A=T_{m-1,i}\) and a right copy \(B=T_{m-1,i-1}\), with every cross
slope larger than every slope internal to either child.  A cap meeting both
children has at most one point in \(A\); its points in \(B\) form a cap.
(Reflecting the construction interchanges caps and cups.)

Let \(C_{m,i}\) be the number of **nonempty** cap subsets of \(T_{m,i}\), with
subsets of size one or two counted as caps.  The separation gives the exact
recurrence

\[
C_{m,i}= C_{m-1,i}
 +(1+{m-1\choose i})C_{m-1,i-1}.                 \tag{1}
\]

Indeed, a cap is either contained in \(A\), or its intersection with \(B\) is
a cap and it chooses at most one of the \({m-1\choose i}\) points of \(A\).
Boundary values are \(C_{m,0}=C_{m,m}=1\).

Let \(U_{m,i}\) count cups.  By reflection symmetry,

\[
U_{m,i}=C_{m,m-i}.                               \tag{2}
\]

## 2. Exponential rate of the cap recurrence

Expanding (1) along lattice paths, a diagonal step entering state \((r,j)\)
has weight

\[
q_{r,j}=1+{r-1\choose j},
\]

whereas a horizontal step has weight \(1\).  For fixed \(j\), \(q_{r,j}\) is
nondecreasing in \(r\).  Among paths ending at \((m,i)\), the product of
diagonal weights is therefore largest when all diagonal steps are taken as
late as possible, at \(r=m-i+j\).  There are at most \(2^m\) paths, so

\[
C_{m,i}\leq 2^{O(m)}
 \prod_{j=1}^{i}
 \left(1+{m-i+j-1\choose j}\right).              \tag{3}
\]

If \(i/m\to x\), the entropy estimate for binomial coefficients and a Riemann
sum give, uniformly in \(0\leq i\leq m\),

\[
\log_2 C_{m,i}\leq m^2 A(x)+o(m^2),              \tag{4}
\]

where

\[
A(x)=\int_0^x(1-x+s)
H\!\left(\frac{s}{1-x+s}\right)\,ds.             \tag{5}
\]

## 3. The central cell gives the stronger bound

Put \(i=\lfloor m/2\rfloor\) and \(Q_m=T_{m,i}\).  Stirling's formula gives

\[
|Q_m|={m\choose\lfloor m/2\rfloor}
=2^{m-O(\log m)}.                                 \tag{6}
\]

Every convex-position subset of an \(x\)-generic point set is the union of
its upper hull chain, which is a cap, and its lower hull chain, which is a
cup.  The ordered pair of hull chains determines the subset.  Thus, using
(2),

\[
V(Q_m)\leq 1+C_{m,i}U_{m,i}
=1+C_{m,i}C_{m,m-i}.                              \tag{7}
\]

Equations (4)--(5), with \(i/m\to1/2\), imply

\[
\log_2V(Q_m)\leq 2A(1/2)m^2+o(m^2).              \tag{8}
\]

The integral is elementary.  At \(x=1/2\),

\[
\begin{aligned}
A(1/2)
&=\int_0^{1/2}\left[
(s+\tfrac12)\log_2(s+\tfrac12)-s\log_2s+\tfrac12
\right]\,ds\\
&=\frac12-\frac1{8\ln2}.
\end{aligned}                                     \tag{9}
\]

Therefore

\[
\log_2V(Q_m)\leq
\left(1-\frac1{4\ln2}+o(1)\right)m^2.             \tag{10}
\]

For arbitrary \(N\), take the least \(m\) for which
\({m\choose\lfloor m/2\rfloor}\geq N\), and retain any \(N\) points of
\(Q_m\).  Deleting points cannot create new subsets of the remaining point
set, while (6) gives
\(m=\log_2N+O(\log\log N)\).  This proves (T1) and the claimed full limsup
bound.

## 4. Secondary result: count the convex subsets of one row

Glue the cells

\[
T_{m,0},T_{m,1},\ldots,T_{m,m}
\]

in the standard row arrangement.  The resulting set (P_m) has (2^m)
points.  The classical decomposition used to prove that (P_m) has no
convex ((m+2))-gon says more: if a convex-position subset has first and last
occupied blocks (k\leq l), then its intersection with (T_{m,k}) is a cap,
its intersection with (T_{m,l}) is a cup, and it uses at most one point from
every strictly intermediate block.

When (k=l), every convex-position subset of an (x)-generic point set is
the union of its upper cap chain and lower cup chain.  The ordered pair of
chains determines the subset, so the number contained in (T_{m,k}) is at
most (C_{m,k}U_{m,k}).  Hence the total number (V(P_m)) of convex-position
subsets satisfies

\[
V(P_m)\leq
\sum_{0\leq k\leq l\leq m}
C_{m,k}U_{m,l}
\prod_{r=k+1}^{l-1}\left(1+{m\choose r}\right).   \tag{6}
\]

The empty set contributes one additional subset to the right-hand side of
(6).  Harmless conventions for subsets of size at most two do not affect its
exponential rate.

For (k/m\to x) and (l/m\to y), (2), (4), and the entropy estimate yield

\[
\frac1{m^2}\log_2(\text{the }k,l\text{ summand})
\leq
\Phi(x,y)+o(1),                                   \tag{7}
\]

uniformly on (0\leq x\leq y\leq1), where

\[
\Phi(x,y)=A(x)+A(1-y)+\int_x^y H(t)\,dt.          \tag{8}
\]

## 4. The variational bound collapses pointwise

For (0\leq s\leq x\leq1), put (v=1-x+s\).  Then (s\leq v\leq1), and

\[
vH(s/v)\leq H(s).                                 \tag{9}
\]

One proof is to differentiate (vH(s/v)) with respect to (v): its derivative
is (-\log_2(1-s/v)\geq0).  Since (v\leq1), (9) follows.  Integrating gives

\[
A(x)\leq\int_0^xH(s)\,ds.                         \tag{10}
\]

By symmetry,

\[
A(1-y)\leq\int_y^1H(s)\,ds.                       \tag{11}
\]

Therefore every (0\leq x\leq y\leq1) satisfies

\[
\Phi(x,y)\leq\int_0^1H(s)\,ds
=\frac1{2\ln2}.                                   \tag{12}
\]

There are only (O(m^2)) summands in (6), so (7)--(12) imply

\[
V(P_m)\leq
2^{(1/(2\ln2)+o(1))m^2}.                          \tag{13}
\]

Because (|P_m|=2^m), this proves the claimed bound along powers of two.
For arbitrary (N), take an (N)-point subset of (P_m), where
(2^{m-1}<N\leq2^m).  Deleting points cannot create new convex subsets, and
(m=\log_2N+O(1)), so (13) gives the same limsup bound for all (N).

## 5. Sharpness for this construction

The strong row orientation law says that every transversal containing one
point from each block is a cap, hence is in convex position.
There are

\[
\prod_{i=0}^m {m\choose i}
\]

transversals.  Stirling's formula and a Riemann sum give

\[
\log_2\prod_{i=0}^m {m\choose i}
=m^2\int_0^1H(t)\,dt+o(m^2)
=\left(\frac1{2\ln2}+o(1)\right)m^2.             \tag{14}
\]

Together with (13), this proves (T1).  In particular, the constant cannot be
improved merely by counting the convex subsets of this same row construction
more sharply; a better upper constant would need a different configuration.

## 6. What remains before this is citable

1. State the separated-union construction with quantified coordinates or a
   clean order-type lemma, then prove recurrence (1) in that exact orientation.
2. Quote and re-prove the row decomposition carefully.  Morris--Soltan's proof
   of Theorem 2.6 states precisely the cap/first-block, cup/last-block, and
   one-point/intermediate-block conclusions, but their indexing and the
   (k=l) sentence should be normalized.
3. Write the uniform (o(m^2)) estimates in (4) and (7) explicitly (an
   (O(m\log m)) remainder is ample).
4. Finish the indexed and unindexed novelty sweep.
5. Cross-examine the final proof independently and attach an exact-coordinate
   small-(m) certificate.
