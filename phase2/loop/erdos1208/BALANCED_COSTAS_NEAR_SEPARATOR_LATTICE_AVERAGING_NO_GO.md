# Balanced Costas near-separators by index-\(p\) lattice averaging

## Status and consequence

Let

\[
 W_p=\{(i,g^i\bmod p):0\le i<p-1\}
\]

be a Welch--Costas array.  The exact full-array question

\[
 \exists T,\quad \det T=p,\quad
 \|T\|_\infty=p^{1/2+o(1)},\quad
 TW_p\text{ distance-Sidon}                         \tag{0.1}
\]

remains open.  The exact \(p=263\) cutoff in
BALANCED_COSTAS_SEPARATOR_EXACT_CUTOFF.md neither proves nor refutes
(0.1).

For the ambient centroid obstruction, however, full separation is
unnecessary.  This note proves the following unconditional substitute.

### Theorem A (balanced near-separator)

For every odd prime \(p\), there are an integral matrix \(T_p\) and a
subset \(B_p\subset W_p\) such that

\[
 \boxed{
 \det T_p=p,\qquad
 \|T_p\|_\infty=p^{1/2+o(1)},\qquad
 |B_p|=p^{1-o(1)},}                                  \tag{0.2}
\]

and \(T_pB_p\) is Euclidean distance-Sidon.

More quantitatively, let \(F=F(p)\to\infty\) with \(F=p^{o(1)}\).
One may choose

\[
 \|T_p\|_\infty\ll F\sqrt p                         \tag{0.3}
\]

so that the complete edge set \(T_pW_p\) has at most

\[
 F^2p^{1+o(1)}                                      \tag{0.4}
\]

unordered pairs of distinct edges with the same norm.  Deleting points
from the resulting collision hypergraph leaves

\[
 |B_p|\ge {p\over Fp^{o(1)}}=p^{1-o(1)}.             \tag{0.5}
\]

The proof does not use a special property of Welch arrays until the last
line: it works for every \(p\)-point vector-Sidon set in a \(p\)-box.

### Corollary B (the ambient clean-centroid gate is false)

The sets

\[
 A_p=T_pB_p
\]

have

\[
 |A_p|=p^{1-o(1)},\qquad
 m(A_p)=p^{3/2+o(1)},                                \tag{0.6}
\]

but their six-distinct-label centroid mass is

\[
 \boxed{\mathcal H(A_p)=p^{4-o(1)}.}                 \tag{0.7}
\]

Consequently

\[
 \mathcal H(A)\stackrel?{\le}
 m^{o(1)}\bigl(|A|^3+m^2\bigr)                       \tag{0.8}
\]

is false by a factor \(p^{1-o(1)}\).  Thus the balanced Welch equality
model is now resolved for the purpose for which it arose: the global
ambient centroid/grid upper gate cannot be used to prove Erdős 1208.

This does not disprove Erdős 1208.  The construction lies at the expected
critical scale \(|A_p|=m^{2/3-o(1)}\).

## 1. Exact Gram and congruence formulation

Write

\[
 T=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
 G=T^{\mathsf T}T=
 \begin{pmatrix}A&B\\B&C\end{pmatrix},\qquad
 \det T=p.                                           \tag{1.1}
\]

Then

\[
 AC-B^2=p^2.                                         \tag{1.2}
\]

For two canonical edge vectors \(u,v\), put

\[
 r=u-v,\qquad s=u+v.
\]

The exact collision equation is

\[
 |Tu|^2=|Tv|^2
 \quad\Longleftrightarrow\quad
 \boxed{r^{\mathsf T}Gs=0.}                         \tag{1.3}
\]

If \(r=d r_0\) with \(r_0\) primitive and

\[
 c_G(r_0)=\gcd\bigl((Gr_0)_1,(Gr_0)_2\bigr),
\]

then all integral solutions of (1.3) have

\[
 s=n\,{JGr_0\over c_G(r_0)},\qquad n\in\mathbb Z.    \tag{1.4}
\]

Moreover

\[
 \boxed{c_G(r_0)\mid p^2.}                           \tag{1.5}
\]

Indeed, \(\operatorname{adj}(G)Gr_0=p^2r_0\), so
\(c_G(r_0)\) divides both coordinates of \(p^2r_0\); primitivity finishes
the proof.

There is also a useful modulo-\(p\) form.  The matrix \(T\bmod p\) has
rank one.  If its image line is nonisotropic for the ordinary dot
product over \(\mathbb F_p\), then (1.3) implies

\[
 \boxed{T(u-v)\equiv0\pmod p
 \quad\text{or}\quad
 T(u+v)\equiv0\pmod p.}                              \tag{1.6}
\]

This is the exact two-sign kernel congruence behind the finite separator
search.  Isotropic image lines, possible when \(p\equiv1\pmod4\), are a
real exception.  The averaging proof below handles both cases and does
not discard this exception.

For a Gram triple, the two exact factorizations

\[
\begin{aligned}
 C\,Q_G(x,y)&=(Bx+Cy)^2+p^2x^2,\\
 A\,Q_G(x,y)&=(Ax+By)^2+p^2y^2
\end{aligned}                                       \tag{1.7}
\]

are often useful computationally.  For the exact \(p=263\) first
separator,

\[
 T=\begin{pmatrix}-67&-45\\52&31\end{pmatrix},
\qquad
 (A,B,C)=(7193,4627,2986),                           \tag{1.8}
\]

and (1.7) is the exact certificate checked by the verifier.

## 2. The \(p+1\) index-\(p\) lattices

Let \(\mathscr L_p\) be the family of index-\(p\) sublattices of
\(\mathbb Z^2\).  Reduction modulo \(p\) identifies them with the
\(p+1\) lines in \(\mathbb F_p^2\):

\[
 \Lambda_L=\{z\in\mathbb Z^2:z\bmod p\in L\}.
                                                               \tag{2.1}
\]

For \(R\ge1\), let \(\mathcal E_\Lambda(R)\) be the number of unordered
pairs

\[
 \{z,z'\}\subset\Lambda\cap\{0<|z|\le R\}
\]

such that

\[
 |z|=|z'|,\qquad z'\ne\pm z.                         \tag{2.2}
\]

The central estimate is

\[
 \boxed{
 \sum_{\Lambda\in\mathscr L_p}\mathcal E_\Lambda(R)
 \le {R^2\over p}\,(pR)^{o(1)}
 \quad(R\ge p).}                                     \tag{2.3}
\]

The \(o(1)\) is uniform for \(R\) polynomial or subpolynomially larger
than a power of \(p\).

### Proof of (2.3)

A pair \(z,z'\) lies in a common member of \(\mathscr L_p\) precisely
when

\[
 \det(z,z')\equiv0\pmod p.                           \tag{2.4}
\]

If their reductions span a nonzero line, that lattice is unique.  If
both vectors vanish modulo \(p\), all \(p+1\) lattices contain them.

First consider pairs with \(z,z'\in p\mathbb Z^2\).  After dividing by
\(p\), both vectors lie in the disk of radius \(R/p\).  The elementary
bound

\[
 r_2(n)\le4\tau(n)=(pR)^{o(1)}                       \tag{2.5}
\]

shows that the number of equal-norm pairs is at most

\[
 {R^2\over p^2}(pR)^{o(1)}.
\]

Their multiplicity \(p+1\) in the lattice sum costs at most the
right-hand side of (2.3).

If exactly one of \(z,z'\) lies in \(p\mathbb Z^2\), the pair belongs to
the unique lattice determined by the nonzero reduction of the other
vector.  There are \(O(R^2/p^2)\) choices for the divisible vector, and
(2.5) gives only \((pR)^{o(1)}\) equal-norm partners for each.  This is
again smaller than the right-hand side of (2.3).

For the remaining pairs, work modulo \(p\).  If \(z\) is nonzero and
nonisotropic and \(z'=\lambda z\), equality of norms forces
\(\lambda=\pm1\).  Thus

\[
 z'\equiv z\pmod p
\quad\text{or}\quad
 z'\equiv-z\pmod p.                                  \tag{2.6}
\]

For the plus sign write \(z'=z+pw\), \(w\ne0\).  Equality of norms is

\[
 2z\mathbin\cdot w+p|w|^2=0.                         \tag{2.7}
\]

Write \(w=d w_0\) with \(w_0\) primitive.  For fixed \(w_0,d\),
(2.7) places \(z\) on an integral line with step vector \(Jw_0\), hence
there are

\[
 O\left(1+{R\over|w_0|}\right)                       \tag{2.8}
\]

solutions in the disk.  Also

\[
 d\le {2R\over p|w_0|}.
\]

Summing first over \(d\), then over primitive \(w_0\) with
\(|w_0|\le2R/p\), gives

\[
 O\left({R^2\over p}\log(2R)+{R^2\over p^2}\right).
                                                               \tag{2.9}
\]

The minus sign is identical after writing \(z'=-z+pw\).

It remains to count isotropic reductions.  The congruence

\[
 z_1^2+z_2^2\equiv0\pmod p
\]

is either only the zero residue or the union of two lines.  Its integer
points in a disk of radius \(R\) number

\[
 O\left({R^2\over p}+R+1\right).                     \tag{2.10}
\]

For each such \(z\), (2.5) gives only \((pR)^{o(1)}\)
equal-norm partners.  Since \(R\ge p\), (2.9)--(2.10), together with
the all-zero case, prove (2.3).

## 3. Almost all index-\(p\) lattices have balanced bases

Fix \(F\to\infty\).  Call \(\Lambda\in\mathscr L_p\) bad if it has a
nonzero vector shorter than \(\sqrt p/F\).

Such a shortest vector yields a primitive vector of no greater length in
\(\Lambda\).  To see this, divide out its coordinate gcd \(d\).  The
shortness gives \(p\nmid d\), and the quotient
\(\mathbb Z^2/\Lambda\) has exponent \(p\), so multiplication by \(d\)
is invertible on the quotient.

Every primitive vector not divisible by \(p\) lies in exactly one member
of \(\mathscr L_p\).  Therefore

\[
 |\{\text{bad }\Lambda\}|
 \ll {p\over F^2}.                                   \tag{3.1}
\]

Every nonbad lattice has a basis \(b_1,b_2\) satisfying

\[
 |b_1|,|b_2|\ll F\sqrt p.                            \tag{3.2}
\]

Indeed choose \(b_1\) shortest and reduce \(b_2\) along \(b_1\).  The
parallel component of \(b_2\) is at most \(|b_1|/2\), while its
perpendicular component is \(p/|b_1|\).  Minkowski's elementary disk
argument gives \(|b_1|\ll\sqrt p\), and nonbadness gives
\(|b_1|\ge\sqrt p/F\), proving (3.2).

Choose

\[
 R=C Fp^{3/2}                                        \tag{3.3}
\]

with a sufficiently large absolute \(C\).  There are \(p-o(p)\) nonbad
lattices.  Averaging (2.3) over them gives one nonbad \(\Lambda\) with

\[
 \mathcal E_\Lambda(R)
 \le F^2p^{1+o(1)}.                                  \tag{3.4}
\]

Let the columns of \(T\) be the balanced basis in (3.2).  After changing
one sign,

\[
 \det T=p,\qquad \|T\|_\infty\ll F\sqrt p.           \tag{3.5}
\]

Every edge vector \(u\) of \(W_p\) has \(|u|\ll p\), hence
\(Tu\in\Lambda\) and \(|Tu|\le R\).  Distinct physical Welch edges never
map to opposite vectors, because Welch is vector-Sidon and \(T\) is
injective.  It follows from (3.4) that the number of edge-norm collisions
in \(TW_p\) is at most \(F^2p^{1+o(1)}\).

## 4. Sparse deletion retains \(p^{1-o(1)}\) points

Put a hyperedge on the \(p-1\) Welch points for every pair of distinct
physical edges with the same post-transform norm.  Its support has size
three or four, and the number \(M\) of hyperedges satisfies

\[
 M\le F^2p^{1+o(1)}.                                 \tag{4.1}
\]

Retain every point independently with probability

\[
 q=\min\left\{{1\over2},
 \sqrt{p\over 8M}\right\}.                           \tag{4.2}
\]

The expected number of retained points is \((p-1)q\), while the expected
number of surviving collision hyperedges is at most \(Mq^3\).  Delete
one point from each surviving hyperedge.  For some outcome this leaves

\[
 |B_p|\gg pq
 \ge {p\over Fp^{o(1)}}=p^{1-o(1)}                  \tag{4.3}
\]

points and no repeated distance.  This proves Theorem A.

## 5. Why this kills the ambient centroid gate

The set \(B_p\) remains vector-Sidon and lies in a \(p\)-box.  If
\(k=|B_p|=p^{1-o(1)}\), Cauchy--Schwarz on triple sums gives

\[
 E_3(B_p)
 =\sum_s r_{3B_p}(s)^2
 \ge {k^6\over |3B_p|}
 \gg {k^6\over p^2}
 =p^{4-o(1)}.                                        \tag{5.1}
\]

For a vector-Sidon set, sextuples in (5.1) with a repeated endpoint label
number only \(O(k^3)\): cancel an opposite-sign repetition and use unique
directed differences, or fix the common same-sign point and use the same
uniqueness.  Thus (5.1) leaves \(p^{4-o(1)}\) six-distinct-label centroid
collisions.

The invertible map \(T\) preserves all endpoint labels and exact centroid
equalities.  Meanwhile

\[
 m(TB_p)\ll p\|T\|_\infty=p^{3/2+o(1)}.              \tag{5.2}
\]

Hence

\[
 k^3+m^2=p^{3+o(1)},\qquad
 \mathcal H(TB_p)=p^{4-o(1)},                        \tag{5.3}
\]

which proves Corollary B.

## 6. Exact scope

The durable conclusions are:

1. balanced determinant-\(p\) transforms with only
   \(p^{1+o(1)}\) metric collisions exist unconditionally;
2. deleting only a subpolynomial fraction on the exponent scale gives a
   genuine distance-Sidon set of size \(p^{1-o(1)}\);
3. this is enough to disprove the ambient clean-centroid estimate;
4. the stronger statement that the complete \(W_p\) is separable remains
   open.

Thus no asymptotic extrapolation from the exact radius \(67\) at \(p=263\)
is needed for the #1208 strategy.  The full separator is an interesting
arithmetic refinement, but it is no longer a gate for the ambient route.

## 7. Verification

Run

    python3 phase2/loop/erdos1208/verify_balanced_costas_near_separator_lattice_averaging.py

The verifier checks the \(p+1\) lattice classification, exact common-lattice
multiplicities, the nonisotropic two-sign congruence, reduced balanced
bases, shell-energy averaging on small primes, collision-hypergraph
deletion, genuine distance-Sidonicity of the retained certificate, and
the exact \(p=263\) Gram/factorization witness.
