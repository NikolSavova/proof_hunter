# Self-reproduction in the rotated-translate incidence graph

## 1. Outcome

Let `A subset Z^2` be distance-Sidon, let `k=|A|`, and put

\[
 D=A-A,\qquad J(x,y)=(-y,x),\qquad U=A+JD.
\]

For `d in D`, write

\[
 B_d=A+Jd\subset U.
\]

The sets `B_d` are the blocks in the rotated-triple support formulation.
They have an exact endpoint-sensitive property not visible in a general
linear hypergraph.

For `x in U`, let

\[
 \mathcal R_x=\{(a,d)\in A\times D:x=a+Jd\},
 \qquad r_x=|\mathcal R_x|,
\]

and let `A_x` be the set of first coordinates occurring in `R_x`.  Then

\[
 \boxed{
 \bigcup_{(a,d)\in\mathcal R_x}B_d
   =x+(A-A_x),
 \qquad
 \left|x+(A-A_x)\right|=1+(k-1)r_x.}           \tag{1.1}
\]

Thus a fibre of multiplicity `h` automatically reproduces `h` translated
stars of the original endpoint set, with no collisions except their common
centre.  This is an exact local form of heavy-fibre compensation.

Equivalently, form a graph `G_A` on `U` by joining two outputs when they lie
in a common block `B_d`.  The blocks are edge-disjoint copies of `K_k`, and

\[
 \boxed{\deg_{G_A}(x)=(k-1)r_x.}                \tag{1.2}
\]

The full cube-root theorem would follow from proving that these expanding
closed neighborhoods cannot overlap with projective-plane efficiency once
their canonical endpoint decorations and the quarter-turn are retained.
The theorem below does not prove that global overlap estimate.  It replaces
the vague phrase “a heavy fibre must expand elsewhere” by one explicit
self-reproducing graph on the actual support.

## 2. Linear block structure

Distance-Sidonicity implies oriented-difference uniqueness and

\[
 (A-A)\cap J(A-A)=\{0\}.                        \tag{2.1}
\]

Every block has `k` elements.  Two distinct blocks meet in at most one
point.  Indeed, suppose `B_d` and `B_e` contain two common points:

\[
 a+Jd=a'+Je,\qquad b+Jd=b'+Je.
\]

Then

\[
 a-a'=J(e-d)=b-b'.
\]

If this vector is nonzero, oriented-difference uniqueness forces the two
ordered endpoint pairs to be identical, hence the two common points are the
same.  If it is zero, (2.1) gives `d=e`.  Thus the block family is linear.

Consequently the cliques induced by the blocks are edge-disjoint and

\[
 e(G_A)=|D|{k\choose2}.                          \tag{2.2}
\]

This is the familiar translate-union incidence structure.  Formula (1.1)
adds the exact endpoint shape of every closed neighborhood.

## 3. Proof of self-reproduction

Fix `x in U`.  For a representation `(a_i,d_i) in R_x`,

\[
 x=a_i+Jd_i,
\]

so

\[
 B_{d_i}=A+Jd_i=x+(A-a_i).                       \tag{3.1}
\]

Taking the union over the representations gives the set identity in
(1.1).

It remains to count the union.  If

\[
 a-a_i=b-a_j
\]

is nonzero, oriented-difference uniqueness gives `a=b` and `a_i=a_j`.
Thus two different translated stars `A-a_i` and `A-a_j` meet only at zero;
zero occurs once in each star.  Since the first-coordinate projection of a
fibre is injective, `|A_x|=r_x`, and hence

\[
 \left|\bigcup_{a_i\in A_x}(A-a_i)\right|
 =1+r_x(k-1).                                    \tag{3.2}
\]

This proves (1.1).  The union in (1.1) is precisely the closed neighborhood
of `x` in `G_A`, so (1.2) follows as well.

There is a useful dual reading.  Starting from a representation
`x=a+Jd`, replace `a` by every endpoint `b in A`.  The `k` resulting
outputs `b+Jd` are exactly one block through `x`.  If two such endpoint
switches coming from different representations of `x` collide away from
`x`, oriented-difference uniqueness identifies both switched endpoint
pairs and hence the original representation.  Endpoint switching is
therefore fully injective off the centre.

## 4. Exact global identities

Let `C` be the incidence matrix of outputs versus blocks.  Its column sums
are `k`, its row sums are `r_x`, and linearity gives

\[
 \sum_{x\in U}r_x=k|D|,                          \tag{4.1}
\]

\[
 C^{\mathsf T}C(d,e)=
 \begin{cases}
 k,&d=e,\\
 0\text{ or }1,&d\ne e.
 \end{cases}                                     \tag{4.2}
\]

Equations (1.2), (2.2), and (4.1) are consistent:

\[
 \sum_{x\in U}\deg(x)
 =(k-1)\sum_xr_x
 =k(k-1)|D|=2e(G_A).                             \tag{4.3}
\]

The desired support bound is `|U|>=k^(3-o(1))`.  Since the total incidence
mass in (4.1) is `k^(3+o(1))`, this asks for subpolynomial average row sum.
A general linear `k`-uniform hypergraph can instead have projective-plane
parameters and average row sum of order `k`.  Therefore (1.1) is not alone
enough: the remaining theorem must show that projective-plane-style overlap
is incompatible with the simultaneous facts that

1. every block is the translate `A+Jd`;
2. every nonzero `d` has one ordered endpoint pair in `A`; and
3. the closed neighborhood at `x` is the literal difference star
   `x+(A-A_x)`.

This graph is a compact alternative interface for the seven-incidence and
opposite-endpoint charges.  A size-biased bound on intersections of the
sets in (1.1), after deleting the common block contribution, would close the
same adaptive tail.

## 5. Verification

`verify_rotated_translate_self_reproduction.py` checks (1.1)--(4.3)
exactly on the determinant-prime affine Costas distance-Sidon families for
primes 11, 17, and 23.  It constructs every block, fibre, closed
neighborhood, and shadow edge using integer arithmetic.
