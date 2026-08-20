# Radial Schur triples: endpoint cleanliness is not the missing property

## 1. Outcome

Let \(A\subset[0,m]^2\) be distance-Sidon and put

\[
 D=(A-A)\setminus\{0\}.
\]

Distance-Sidonicity makes every directed vector in \(D\) recover its unique
ordered endpoint pair.  Write

\[
 T(D)=|\{(x,y,z)\in D^3:x+y+z=0\}|.                 \tag{1.1}
\]

There are two sharply different conclusions.

**For genuine complete difference sets**, removing six-endpoint
cleanliness costs only the automatic cubic term:

\[
 \boxed{T(D)=C_6(A)+O(k^3),\qquad k=|A|.}            \tag{1.2}
\]

Thus

\[
 T(D)\le m^{o(1)}(k^3+m^2)                           \tag{1.3}
\]

is exponent-equivalent to the ambient six-endpoint conjecture.  Since
\(|D|=N=k(k-1)\), the variant \(T(D)\ll N^{3/2}+m^2\) is the same target.
Endpoint cleanliness itself is not an additional obstruction.

**For radial transversals**, the analogous statement is false by a full
power.  There are centrally symmetric sets

\[
 \mathcal D\subset[-m,m]^2,
 \qquad |\mathcal D|=k(k-1)=m^{4/3-o(1)},             \tag{1.4}
\]

with exactly one antipodal pair \(\{v,-v\}\) at every occupied squared
radius, but

\[
 \boxed{T(\mathcal D)=m^{8/3-o(1)}.}                  \tag{1.5}
\]

Hence

\[
 T(\mathcal D)\gg m^{2/3-o(1)}
       \bigl(|\mathcal D|^{3/2}+m^2\bigr).            \tag{1.6}
\]

The model can even be labelled bijectively by all ordered endpoint pairs
of a formal \(k\)-point set, respecting reversal, so that
\(m^{8/3-o(1)}\) of its Schur triples have six formally distinct endpoints.
What it cannot satisfy is the global difference cocycle

\[
 \boxed{\delta(a,b)+\delta(b,c)=\delta(a,c)}          \tag{1.7}
\]

for every endpoint triple.  This common-realization, or coboundary,
property is the load-bearing distinction between a genuine (A-A) and an
abstract radially unique vector system.

## 2. Why cleanliness is automatic up to \(O(k^3)\)

For a genuine \(D\), let the unique endpoint representation of
\(x_i\in D\) be

\[
 x_i=b_i-a_i.
\]

Then \(x_1+x_2+x_3=0\) is exactly

\[
 a_1+a_2+a_3=b_1+b_2+b_3.                            \tag{2.1}
\]

If the six endpoint roles are distinct, this is one of the ordered clean
centroid records counted by \(C_6(A)\), and the correspondence is
bijectional.

If the roles are not distinct, choose one of the at most fifteen equal
role pairs.  Each fixed equality leaves at most \(k^3\) solutions.  For
example, if \(a_1=a_2\), choose \(a_1,b_1,b_2\); then
\(x_3=-x_1-x_2\), and directed-vector uniqueness gives at most one ordered
endpoint realization \((a_3,b_3)\).  If \(a_1=b_2\), choose the common
endpoint, \(b_1\), and \(a_2\).  Then
\(x_1+x_2=b_1-a_2\), so uniqueness forces
\((a_3,b_3)=(b_1,a_2)\).  The other same-side and opposite-side equalities
are identical after permuting roles; \(a_i=b_i\) is forbidden because
\(x_i\ne0\).  Thus a union bound gives the sharper estimate

\[
 0\le T(D)-C_6(A)\le15k^3.                            \tag{2.2}
\]

This proves (1.2).  In particular, a counterexample obtained merely by
allowing repeated endpoints cannot exist in the genuine setting.

## 3. A dense centrally symmetric radial transversal

Let

\[
 B_L=\{v\in\mathbb Z^2:0<\|v\|_\infty\le L\}.
\]

For every represented squared radius \(n\), partition the vectors of norm
\(n\) into antipodal pairs and choose one such pair uniformly and
independently.  Let \(\mathcal D_L\) be the union of the chosen pairs.

Put

\[
 \Delta_L=\max_{1\le n\le2L^2}r_2(n)=L^{o(1)}.       \tag{3.1}
\]

Since \(B_L\) has \(\Theta(L^2)\) vectors and every radius contains at
most \(\Delta_L\) of them, the number \(R_L\) of occupied radii obeys

\[
 R_L=L^{2-o(1)},qquad |\mathcal D_L|=2R_L.           \tag{3.2}
\]

There are \(\Theta(L^4)\) full-box Schur triples with three distinct
radii.  Indeed, choose

\[
 x,y\in[1,\lfloor L/4\rfloor]^2,qquad z=-x-y.        \tag{3.3}
\]

Then \(z\in B_L\), and \(|z|>|x|,|y|\).  Only the pairs with
\(|x|=|y|\) must be discarded.  There are at most
\(O(L^2\Delta_L)=L^{2+o(1)}\) of those, leaving
\(\Theta(L^4)\) ordered triples with distinct radii.

For any one such triple, the probability that all three of its antipodal
pairs are selected is at least \(\Delta_L^{-3}=L^{-o(1)}\).  Therefore

\[
 \mathbb E T_{\rm distinct}(\mathcal D_L)
 \ge L^{4-o(1)}.                                     \tag{3.4}
\]

Some radial transversal realizes this lower bound.

## 4. Exact cardinality and formal clean endpoint labels

The size objection can be removed completely.  Let \(k\) be the largest
integer with

\[
 {k\choose2}\le R_L.
\]

Choose uniformly a subfamily of exactly \(\binom{k}{2}\) occupied radial
classes.  Since

\[
 0\le R_L-{k\choose2}<k=O(\sqrt{R_L}),               \tag{4.1}
\]

every distinct-radius Schur triple survives with probability (1-o(1)).
Thus one obtains a centrally symmetric set \(\mathcal D'_L\) with

\[
 |\mathcal D'_L|=k(k-1),qquad
 T_{\rm distinct}(\mathcal D'_L)=L^{4-o(1)}.         \tag{4.2}
\]

Now label the \(\binom{k}{2}\) antipodal classes uniformly by the unordered
edges of \(K_k\), assigning the two signs to the two orientations.  For
three distinct radial classes, the probability that their three labels
form a matching is

\[
 {15\binom k6\over\binom{\binom k2}3}=1-O(1/k).      \tag{4.3}
\]

Consequently some labelling makes \(L^{4-o(1)}\) Schur triples formally
six-endpoint clean.  This model has all of the following:

* central symmetry and the correct multiplicity two at each radius;
* exactly \(k(k-1)\) directed vectors;
* a bijection with every ordered endpoint pair;
* reversal compatibility \(\delta(b,a)=-\delta(a,b)\);
* radial uniqueness; and
* almost entirely six-distinct Schur triples.

Yet it is not a genuine difference set, because the labels do not satisfy
(1.7).  Point coordinates would force (1.7) simultaneously on all
\(k(k-1)(k-2)\) ordered endpoint triangles.

Finally place the construction in an ambient box of side

\[
 m=\lceil L^{3/2}\rceil.                              \tag{4.4}
\]

Since all vectors already lie in the \(L\)-box,

\[
 k=L^{1-o(1)}=m^{2/3-o(1)},quad
 |\mathcal D'_L|=m^{4/3-o(1)},quad
 T(\mathcal D'_L)=m^{8/3-o(1)}.                     \tag{4.5}
\]

Equations (1.5)--(1.6) follow.

## 5. What endpoint property is load-bearing?

The barrier separates three notions which should not be conflated.

1. **Radial uniqueness:** every norm identifies one antipodal vector pair.
2. **Formal endpoint completeness:** the vectors can be bijectively named
   by all ordered pairs of (k) abstract labels.
3. **Geometric endpoint realization:** there are common points
   \(P_1,\ldots,P_k\in\mathbb Z^2\) with
   \(\delta(a,b)=P_b-P_a\) for every ordered pair.

The first two permit the counterexample above, even with formal
six-endpoint cleanliness.  The third is equivalent to the complete family
of cocycle identities (1.7), after fixing one base point.  It is therefore
the exact load-bearing input in the radial Schur formulation.

This also explains why ordinary additive-combinatorial estimates on the
vector set stall.  A radial transversal can have almost quadratic Schur
mass.  A proof for (A-A) must use the compatibility of all those vectors
as one complete endpoint coboundary, not merely their distinct radii or
their individual endpoint names.

## 6. Finite certificate

For \(L=30\), a deterministic radial choice has 407 occupied classes and
83,604 ordered distinct-radius Schur triples.  Delete its least-used class,
leaving

\[
 k=29,qquad |\mathcal D|=812=k(k-1),qquad
 T_{\rm distinct}=83,496.                            \tag{6.1}
\]

A stored deterministic bijection to the edges of \(K_{29}\) leaves
54,720 formally six-endpoint clean triples.  With
\(m=\lceil30^{3/2}\rceil=165\),

\[
 54,720>29^3+165^2=51,614.                           \tag{6.2}
\]

Only six of the 21,924 ordered endpoint triangles happen to satisfy the
cocycle (1.7), illustrating the missing global realization.

## 7. Verification

Run

```text
python3 phase2/loop/erdos1208/verify_radial_schur_triple_endpoint_cocycle_barrier.py
```

The verifier checks genuine difference-set cleanliness decomposition,
radial uniqueness, critical scaling profiles, exact cardinality trimming,
the formal complete endpoint labelling, six-endpoint clean Schur counts,
and cocycle failure.
