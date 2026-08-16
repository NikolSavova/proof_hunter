# Same-type and positive-fraction extraction: ample absolute bank, exact pocket barrier

## Verdict

The quantitative extraction route is strong enough for the missing
lower-order scale. For every fixed \(\alpha>0\), putting

\[
                   k=\lfloor\alpha\log_2\log_2 n\rfloor          \tag{1}
\]

in the current planar same-type plus Erdős--Szekeres pipeline gives \(k\)
disjoint blocks of size

\[
                   s\ge {n\over(\log n)^{5\alpha+o(1)}}          \tag{2}
\]

such that every transversal is convex in one fixed type. Consequently

\[
                   V(P)\ge(1+s)^k-1
                       =n^{\alpha\log_2\log_2 n-o(\log\log n)}.  \tag{3}
\]

Thus same-type loss is not the obstruction to an
\(n^{\Theta(\log\log n)}\) **absolute** bank.

The bank does not automatically multiply an inherited pocket or source
face. Same-type controls determinants with one label from each of three
distinct blocks. Coexistence with a pocket face uses determinants with two
pocket labels and one external label. A scalable rational example has

* a \(14\)-point convex pocket with \(2^{14}-1\) nonempty faces;
* three three-point external blocks whose \(378\) one-from-each singleton
  transversals, including one pocket representative, all have one convex
  type; but
* every pocket trace of rank at least three is nonordinary with every
  choice from one guard block.

Only \(1+14+\binom{14}{2}=106\) pocket traces can possibly coexist with a
full external transversal. The formal product has \(442{,}341\) incidences,
while at most \(2{,}862\) mixed outputs survive. This is a geometric
failure before any decoder or load issue.

Mirzaei--Suk's polynomial-fraction mutually avoiding theorem is even
stronger in block size, but weaker in high-rank convexity. It immediately
guarantees every \(2+2\) choice across the two sides is a convex
quadrilateral, giving a rank-four bank

\[
                       \binom{k}{2}^{\!2}s^4.                    \tag{4}
\]

It does not make a \(2k\)-point transversal convex. An exact six-point pair
of mutually avoiding triples has only five hull vertices, while all nine
\(2+2\) subsets are convex. Applying same-type and Erdős--Szekeres inside
one side recovers (3), but does not repair pocket coexistence.

The exact positive interface is therefore an **anchored same-type**
hypothesis: the inherited face must coexist with every external
transversal. Under that extra hypothesis the desired multiplier is
load-one locally and has only the stated global context overlap. No
unconditional half-coefficient closure is claimed.

## 1. Strongest clean unconditional convex-transversal bank

Let \(P\) have \(n\) points and let \(m=ES(k)\). Partition \(P\) into
\(m\) parts as equally as possible. Bukh--Vasileuski's planar same-type
theorem gives subsets of all \(m\) parts of size at least

\[
                 s\ge 2^{-400}m^{-4}\lfloor n/m\rfloor          \tag{5}
\]

whose full product has one order type. Choose one representative from each
block. The representatives contain a convex \(k\)-subset by the definition
of \(ES(k)\). Restricting to those \(k\) block indices, every transversal
has the same type as this convex representative set and is therefore
ordinary.

Every subtransversal is also ordinary by heredity. Since the role supports
are disjoint, all choices are distinct, proving

\[
                            V(P)\ge(1+s)^k-1.                    \tag{6}
\]

Suk's sharp bound \(ES(k)=2^{k+o(k)}\) and (5) give

\[
                         \log_2s
                   \ge L-5k-o(k)-400,\qquad L=\log_2n.          \tag{7}
\]

Substituting (1) into (6)--(7) proves (2)--(3):

\[
 \log_2\bigl((1+s)^k-1\bigr)
      \ge\alpha L\log_2L-5\alpha^2(\log_2L)^2
             -o((\log L)^2)-O(\log L).                          \tag{8}
\]

The older Fox--Pach--Suk same-type fraction
\(2^{-O(m\log m)}\) also proves the same leading term when
\(k=\alpha\log L\) with any fixed \(\alpha<1\): then
\(m=L^{\alpha+o(1)}\) and the per-block loss is \(2^{-o(L)}\).
The polynomial Bukh--Vasileuski fraction removes this restriction and
gives the explicit five powers of \(m\) in (5).

The primary quantitative sources are:

* Bukh--Vasileuski,
  [New bounds for the same-type lemma](https://arxiv.org/abs/2309.10731);
* Fox--Pach--Suk,
  [Density and regularity theorems for semi-algebraic hypergraphs](https://homepages.math.uic.edu/~suk/regularity031014.pdf);
* Suk's \(ES(k)=2^{k+o(k)}\) theorem as cited in the main project notes.

The exact verifier uses the conservative classical bound \(ES(k)\le4^k\).
Even this gives

\[
                \log V(P)\ge kL-O(k^2)-O(k),                    \tag{9}
\]

which is already \(\Theta(L\log L)\) at \(k=\Theta(\log L)\).

## 2. Why the absolute bank does not repair the live gap

Suppose an independent inherited pocket has \(H\) ordinary faces. The two
separate statements

\[
                         V(P)\ge H,\qquad V(P)\ge(1+s)^k         \tag{10}
\]

imply only their maximum, not their product. In the fixed-gap regime,
\(\log H=\Theta(L^2)\) while \(\log(1+s)^k=\Theta(L\log L)\), so the
absolute extraction bank is swallowed by the already known pocket bank.

To supply the missing multiplier, one needs ordinary unions retaining both
choices. This introduces orientation signs absent from the same-type
transcript. A singleton transversal uses signs

\[
                  \chi(z_i,z_j,z_\ell)
       \quad\text{for three distinct role blocks}.              \tag{11}
\]

If a pocket face \(F\) contributes two labels \(u,v\), convexity of
\(F\cup T\) also uses

\[
                         \chi(u,v,z_i),\qquad u,v\in F.           \tag{12}
\]

Neither (11) nor strong separation determines (12).

## 3. Exact anchored splice

Let \(Q_c\) be a pocket support, let
\(\mathcal F_c\subseteq\mathcal F(Q_c)\), and let
\(Z_{c,1},\ldots,Z_{c,k_c}\) be disjoint external role blocks, also
disjoint from \(Q_c\). Assume

\[
 F\cup\{z_i:i\in I\}\in\mathcal F(P)                            \tag{13}
\]

for every \(F\in\mathcal F_c\), every \(I\subseteq[k_c]\), and every
choice \(z_i\in Z_{c,i}\). It is enough to assume (13) for full
transversals; heredity gives all \(I\).

For one fixed context, disjoint support colours recover \(F\), the occupied
roles, and every external label. Hence the mixed bank has exactly

\[
                   |\mathcal F_c|\prod_{i=1}^{k_c}
                                      (1+|Z_{c,i}|)              \tag{14}
\]

distinct ordinary outputs.

For several contexts, define the actual output load

\[
 \Lambda=\max_G
   \#\{(c,F,I,(z_i)):G=F\cup\{z_i:i\in I\}\}.                    \tag{15}
\]

Double counting gives the exact global theorem

\[
 \boxed{\displaystyle
 V(P)\ge {1\over\Lambda}
       \sum_c|\mathcal F_c|\prod_i(1+|Z_{c,i}|).}                \tag{16}
\]

Combining (2)--(3) with (16) supplies the required
\(n^{\Theta(\log\log n)}\) multiplier whenever
\(\Lambda=n^{o(\log\log n)}\). This is the clean conditional splice. Its
load-bearing hypothesis is (13), not same-type singleton convexity.

## 4. Scalable repeated-block barrier

Fix \(m\ge14\), put \(\delta=1/(100m^2)\), and define

\[
 P_t=\left(2-\delta t^2,-{1\over5}+\delta t\right),
 \qquad1\le t\le m.                                            \tag{17}
\]

Let \(Q_m=\{P_1,\ldots,P_m\}\). These points lie on a strict concave
parabola, so every nonempty subset is ordinary and

\[
                         V(Q_m)-1=2^m-1.                         \tag{18}
\]

Use the three macro anchors

\[
                         b=(4,0),\qquad c=(0,4),\qquad a=(0,0).  \tag{19}
\]

Replace each by an arbitrarily small rational role cloud. Openness of the
strict orientation conditions makes every transversal

\[
                         (P_t,b',c',a')                          \tag{20}
\]

a convex quadrilateral in the same cyclic role order. Thus
\((Q_m,B,C,A)\) is a complete same-type product.

Nevertheless, for \(i<j<k\), the point \(P_j\) lies strictly inside

\[
                         \operatorname{tri}(P_i,P_k,c).          \tag{21}
\]

The barycentric inequalities are strict, so (21) persists for every
\(c'\) in a sufficiently small guard cloud \(C\). Consequently

\[
 |F|\ge3,\ c'\in C
       \quad\Longrightarrow\quad F\cup\{c'\}\text{ is nonordinary}. \tag{22}
\]

Every full external transversal contains one \(c'\). Therefore at most

\[
                              1+m+\binom m2                         \tag{23}
\]

pocket traces can coexist with it, instead of \(2^m\). The same
construction supports any number of additional same-type macro roles and
arbitrarily large rational role clouds: insert further vertices in the
strict macro polygon and shrink all clouds. Equation (22) is unchanged.

At \(m=14\) and cloud size three, the verifier uses the explicit rational
offsets

\[
\begin{aligned}
B-b&=10^{-7}\{(2,7),(-10,7),(15,22)\},\\
C-c&=10^{-7}\{(25,-12),(-26,2),(-2,28)\},\\
A-a&=10^{-7}\{(6,15),(-5,9),(-13,-13)\}.
\end{aligned}                                                  \tag{24}
\]

It obtains

\[
\begin{array}{c|r}
\text{same-type singleton transversals}&14\cdot3^3=378\\
\text{strict pocket-middle containments}&\binom{14}{3}\cdot3=1092\\
\text{formal nonempty-pocket/full-external product}&442{,}341\\
\text{upper bound after the guard obstruction}&2{,}862.
\end{array}                                                     \tag{25}
\]

This is a pure geometric failure. All supports and choices are literal, so
there is no hidden context overlap to blame. The bad determinant in (21)
contains two labels from \(Q_m\), exactly the sign omitted by same-type.

## 5. Mirzaei--Suk: what polynomial-fraction mutual avoidance gives

Mirzaei--Suk prove that there are \(2k\) blocks

\[
                    A_1,\ldots,A_k,B_1,\ldots,B_k
\]

of common size \(s=\Omega(n/k^4)\) such that every \(A\)-transversal and
every \(B\)-transversal form mutually avoiding sets. See
[A positive fraction mutually avoiding sets theorem](https://arxiv.org/abs/1802.06484).

For two chosen \(A\)-roles and two chosen \(B\)-roles, mutual avoidance
implies that every \(2+2\) choice is a convex quadrilateral. Role colours
make the choices distinct, proving the unconditional bank (4). Since
\(s=\Omega(n/k^4)\),

\[
             \log_2\!\left(\binom{k}{2}^{2}s^4\right)
                        =4L-O(\log k).                           \tag{26}
\]

Indeed, extend the four selected points to full (A)- and
(B)-transversals and use heredity of mutual avoidance. If the four points
were not convex, one would lie inside the triangle of the other three. The
line joining that hidden point to the other point of its own colour meets
the segment joining the two opposite-colour points, contradicting mutual
avoidance.

This is a strong polynomial absolute bank, but its rank remains four. The
theorem does not make the union of full \(A\)- and \(B\)-transversals
ordinary. The verifier gives the exact mutually avoiding triples

\[
\begin{aligned}
A&=\{(3,2),(4,1),(1,1)\},\\
B&=\{(2,-6),(-5,-6),(-1,-5)\}.
\end{aligned}                                                  \tag{27}
\]

All nine \(2+2\) subsets are convex, while \(A\cup B\) has only five hull
vertices.

One can recover a high-rank bank from one side by applying the planar
same-type theorem to \(A_1,\ldots,A_k\), then taking a convex
\((1-o(1))\log_2 k\)-subset of representatives. The retained blocks have
size \(\Omega(n/k^8)\). Taking \(k=\Theta(L)\) gives

\[
       \log V(P)\ge(1-o(1))L\log_2L-O((\log L)^2),                \tag{28}
\]

again the absolute scale (3). Mutual avoidance does not add the missing
anchored signs (12), so it does not improve (16).

## 6. Exact endpoint

The positive-fraction route settles the numerical question:
\(n^{\Theta(\log\log n)}\) convex-transversal banks exist unconditionally.
What remains is not extraction but one of:

1. an anchored same-type theorem proving (13) for the inherited live
   pocket/source face;
2. a circuit-release operation paying every failure of (12); or
3. a global decoder showing that the absolute transversal bank is new for
   each inherited context.

The rational construction (17)--(25) rules out deriving the first item from
same-type or mutual avoidance alone. It also rules out a claim that triples
with two labels from one block are a lower-order technicality: they erase
an exponential pocket reservoir.

## 7. Verification

Run:

    python3 agent_outer_internal_product/verify_same_type_positive_fraction_pocket_coexistence_gate.py

The verifier:

1. checks the conservative same-type/ES extraction arithmetic at
   \(1024\le L\le4096\);
2. verifies the conditional mixed-bank decoder;
3. exhausts the rational same-type pocket/guard construction in (24);
4. checks all \(1092\) strict hidden-point witnesses and the count (25);
5. verifies mutual avoidance and all nine \(2+2\) faces in (27); and
6. checks the Mirzaei--Suk rank-four capacity scale.

It prints PASS.
