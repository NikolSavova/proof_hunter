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

## 5. Exact transverse common-neighborhood normal form

The overlap between two self-reproducing neighborhoods splits exactly into
the unavoidable common block and one shifted endpoint-difference count.

Take distinct `x,y in U`, put `delta=y-x`, and retain the endpoint sets
`A_x,A_y` from Section 1.  For `p in A_x` and `q in A_y`, set

\[
 w=\delta+p-q.                                   \tag{5.1}
\]

If `w in D minus {0}`, let `(a_w,b_w)` be its unique ordered endpoint pair:

\[
 w=a_w-b_w.
\]

Define `T_(x,y)` to be the set of pairs `(p,q) in A_x times A_y` for which

\[
 w\in D\setminus\{0\},\qquad a_w\ne p,\qquad b_w\ne q.       \tag{5.2}
\]

Let `x sim y` mean adjacency in `G_A`, equivalently that `x,y` lie in one
common block.  Then

\[
 \boxed{
 |N[x]\cap N[y]|=k\,1_{x\sim y}+|\mathcal T_{x,y}|.}          \tag{5.3}
\]

The two terms in (5.3) have disjoint geometric meanings.  The first is the
entire unique common `K_k`; the second counts common neighbors obtained from
two different blocks.

### Proof

First suppose `w=0`.  Since `p in A_x` and `q in A_y`, there are blocks
`B_d,B_e` such that

\[
 x=p+Jd,\qquad y=q+Je.
\]

The equality `delta=q-p` is then equivalent to `J(e-d)=0`, so `d=e`.
Thus a zero value in (5.1) exists exactly when `x sim y`; by block
linearity it comes from the unique common block.  That block contributes
all `k` of its vertices to `N[x] cap N[y]`.

Now take a pair in `T_(x,y)` and define

\[
 z=x+a_w-p.                                      \tag{5.4}
\]

Equation (5.1) rearranges to

\[
 a_w-p-\delta=b_w-q,
\]

so also

\[
 z=y+b_w-q.                                      \tag{5.5}
\]

The difference `a_w-p` shows that `z in N[x]`, and `b_w-q` shows that
`z in N[y]`.  The last two conditions in (5.2) ensure `z notin {x,y}`.
Moreover `z` cannot be another point of a common block: uniqueness of the
two nonzero endpoint differences in (5.4)--(5.5) would then force the
canonical common-block endpoints and hence `w=0`.

The map `(p,q) -> z` is injective.  If two pairs give the same `z`, then

\[
 a_w-p=a_{w'}-p'.
\]

This is nonzero, so oriented-difference uniqueness recovers both `a_w` and
`p`.  Applying the same argument to (5.5) recovers `b_w` and `q`.

Conversely, let `z` be a common neighbor outside the common block.  Choose
the block through `x,z` and the different block through `y,z`, and write

\[
 x=p+Jd,\quad z=a+Jd,
 \qquad y=q+Je,\quad z=b+Je.
\]

Then

\[
 \delta+p-q=a-b\in D\setminus\{0\},
\]

and `z notin {x,y}` gives the two inequalities in (5.2).  This reverses
(5.4)--(5.5) and proves (5.3).

Formula (5.3) is the local overlap gate in its smallest endpoint form.  A
general projective plane pays only the first term.  Any excess must now be
realized by the concrete six-endpoint condition

\[
 p\in A_x,\quad q\in A_y,quad
 (y-x)+p-q=a-b\in A-A.                           \tag{5.6}
\]

A size-biased aggregate bound for (5.6), after the common-block term is
removed, is equivalent to the transverse part of the existing
seven-incidence charge.

## 6. Exact self-duality of the aggregate transverse overlap

The local normal form does not, by itself, improve the global second
moment.  Its unweighted aggregate is exactly the old collision count at the
dual scale:

\[
 \boxed{
 \sum_{\{x,y\}\in\binom U2}|\mathcal T_{x,y}|
 =(k-1)^2\sum_{z\in U}{r_z\choose2}.}            \tag{6.1}
\]

To prove (6.1), fix a point `z` and two distinct representations

\[
 z=a+Jd=b+Je.
\]

The blocks `B_d,B_e` meet only at `z`.  Choose independently

\[
 p\in A\setminus\{a\},\qquad q\in A\setminus\{b\},
\]

and put

\[
 x=p+Jd,qquad y=q+Je.                            \tag{6.2}
\]

Then `x!=y`, while `z` is a transverse common neighbor of `x,y`.  The
unique blocks through `x,z` and through `y,z` recover `d,e`; their endpoint
decorations recover `p,q`.  Thus different choices in (6.2), and different
unordered pairs of representations of `z`, give different transverse
wedges `({x,y},z)`.  Conversely every member counted by some
`T_(x,y)` recovers exactly this data through the proof of (5.3).

There are `(k-1)^2` endpoint switches for every unordered pair of
representations at `z`, proving (6.1).

Equation (6.1) is a useful no-go theorem.  Summing the exact neighborhood
expansion (1.1) and controlling overlaps only by their total multiplicity
is circular: it reproduces `sum binom(r_z,2)` multiplied by the same
endpoint-switch factor that created the expansion.  A successful use of
self-reproduction must therefore do at least one of the following:

1. orient the transverse wedges and control a convex size-biased load;
2. discard a structured family and charge it to a genuinely new support;
   or
3. use the Gaussian-core scale/index to make repeated switching shrink the
   ambient lattice.

This explains, in the simpler block graph, why the preferred swap gate is
the oriented energy `2 sum_v d^+(v)^2` rather than an unweighted common-
neighborhood total.

## 7. Verification

`verify_rotated_translate_self_reproduction.py` checks (1.1)--(6.1)
exactly on the determinant-prime affine Costas distance-Sidon families for
primes 11, 17, and 23.  It constructs every block, fibre, closed
neighborhood, and shadow edge using integer arithmetic.
