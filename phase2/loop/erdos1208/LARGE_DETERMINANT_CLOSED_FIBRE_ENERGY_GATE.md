# Large determinant with the third vector retained: closed fibre energy

## Status

Let (A\subset[0,m]^2\cap\mathbb Z^2) be distance-Sidon, put

\[
 \mathscr D=(A-A)\setminus\{0\},\qquad N=k(k-1),
\]

and let \(\mathcal H_A[D,2D)\) be the six-endpoint matching hyperedges
whose nonzero absolute determinant lies in \([D,2D)\).

The projection argument in
LARGE_DETERMINANT_PROJECTION_DYADIC_GATE.md discarded both
\(-q_1-q_2\in\mathscr D\) and endpoint cleanliness.  This note retains
the first condition exactly and identifies the precise cost of the
second.

For every primitive active direction (w), choose
(v_w\in\mathbb Z^2) with \(\det(w,v_w)=1\), and define the longitudinal
fibre

\[
 S_{w,r}=\{n\in\mathbb Z:nw+rv_w\in\mathscr D\}.       \tag{0.1}
\]

Let

\[
 T_w=\{g>0:gw\in\mathscr D\},\qquad
 G_{w,r}(D)=\{g\in T_w:D\le g|r|<2D\}.                \tag{0.2}
\]

Then the exact third-vector condition is simply

\[
 nw+rv_w,\;-(n+g)w-rv_w\in\mathscr D
 \quad\Longleftrightarrow\quad
 n,n+g\in S_{w,r}.                                    \tag{0.3}
\]

Moreover, the determinant is exactly (gr).  If
(C^{\rm mat}_{w,r}(g)) counts the (n) in (0.3) for which the three
directed vectors have six distinct endpoint realizations, then

\[
 \boxed{
  3|\mathcal H_A[D,2D)|
  =\sum_{w,r}\sum_{g\in G_{w,r}(D)}
       C^{\rm mat}_{w,r}(g).}                          \tag{0.4}
\]

Thus (0.4) is a complete band-restricted, endpoint-sensitive replacement
for the old projection functional.

Writing

\[
 B_w(r)=|S_{w,r}|,
 \qquad
 \alpha_{w,D}(r)=|G_{w,r}(D)|,                        \tag{0.5}
\]

one rigorous relaxation is

\[
\begin{aligned}
 3|\mathcal H_A[D,2D)|
 &\le \mathcal K_D(A)\\
 &:=\sum_{w,r}\sum_{g\in G_{w,r}(D)}
       |S_{w,r}\cap(S_{w,r}-g)|\\
 &\le \mathcal Q_D(A)\\
 &:=\sum_{w,r}
   \min\left\{\binom{B_w(r)}2,
                    \alpha_{w,D}(r)B_w(r)\right\}.    \tag{0.6}
\end{aligned}
\]

The first inequality discards only six-endpoint cleanliness; it does not
discard the closing vector.  The second is a sharp one-dimensional
positive-gap estimate.

This gives a new sufficient theorem:

\[
 \boxed{
  \sum_D\mathcal Q_D(A)
  \le m^{o(1)}(k^3+m^2)}                              \tag{0.7}
\]

for dyadic (D) would close the entire nonzero-determinant endpoint
hypergraph.  It is strictly more structured than the old
\(\mathcal Z(A)\) target: it asks for selected positive gaps inside the
same determinant lattice fibre.

There are two firm limitations.

1. Abstract interpolation of (0.6) gives only

   \[
    |\mathcal H_A[D,2D)|
    \le {1\over3}\min\left\{\binom N2,
                     \sqrt{6D}\,N^{3/2}\right\}.       \tag{0.8}
   \]

   Thus retaining closure automatically adds a high-band (O(k^4))
   cap, but no power saving in the hard range.

2. This is a genuine barrier, not just weak algebra.  Euclideanized
   modular parabolas have one dyadic band with
   \(\Omega(k^4/\log k)\) clean matching hyperedges.  Consequently the
   exact clean functional in (0.4), the unrestricted closed functional
   \(\mathcal K_D\), and its relaxation \(\mathcal Q_D\) can all have
   fourth-order band mass.  A proof of (0.7) must use ambient height; the
   closure equation and endpoint matching alone cannot supply the gain.

The explicit (p=43) Euclidean lift makes the endpoint loss quantitative.
Across its mass-bearing bands,
\(\mathcal K_D/(3|\mathcal H_D|)\) lies between (1.19) and (1.39).
The closing-vector condition is therefore already almost exact on the
principal stress.  On the other hand,

\[
 \sum_{D\ge1}\mathcal Q_D=988320<1175^2,               \tag{0.9}
\]

so the proposed ambient estimate (0.7) survives this stress.  The result
is a real localization of the missing theorem, not a completed proof.

## 1. Unimodular determinant fibres

Distance-Sidonicity makes the directed endpoint map injective: every
(q\in\mathscr D) has one directed endpoint edge.  Let
(\mathcal W(A)) be the primitive unoriented directions of the
unordered edges of (A).  Orient every (w\in\mathcal W(A)) by the
lexicographically positive convention.

Since (w) is primitive, Bezout gives (v_w\in\mathbb Z^2) satisfying
\(\det(w,v_w)=1\).  Every lattice vector has a unique expansion

\[
 q=nw+rv_w,
 \qquad
 r=\det(w,q),\quad n=\det(q,v_w).                     \tag{1.1}
\]

This proves that (0.1) is exactly the intersection of \(\mathscr D\)
with one affine coset of the rank-one lattice \(\mathbb Zw\).  Symmetry
of the complete difference set gives

\[
 S_{w,-r}=-S_{w,r},
 \qquad
 S_{w,0}=\{\pm g:g\in T_w\}.                          \tag{1.2}
\]

Fix (g\in T_w) and take

\[
 q_1=gw,\qquad q_2=nw+rv_w.
\]

The forced third vector is

\[
 q_3=-q_1-q_2=-(n+g)w-rv_w.                           \tag{1.3}
\]

By (1.2), (q_3\in\mathscr D) if and only if
((n+g)w+rv_w\in\mathscr D), which is exactly
(n+g\in S_{w,r}).  Also

\[
 \det(q_1,q_2)=gr.                                    \tag{1.4}
\]

Equations (1.3)--(1.4) prove the closed-fibre identity (0.3).

## 2. Exact six-endpoint factor

For (g>0), define (C^{\rm mat}_{w,r}(g)) to be the number of
(n\in S_{w,r}) such that (n+g\in S_{w,r}) and the unique directed
endpoint edges representing

\[
 gw,\qquad nw+rv_w,\qquad -(n+g)w-rv_w                \tag{2.1}
\]

are pairwise endpoint-disjoint.

If both signs of the distinguished first vector are retained, every
hyperedge supplies six ordered choices of its first two vertices.  The
reversal involution on hyperedges exchanges the two signs and has no
fixed point.  Consequently the positive first-vector orientation supplies
exactly half the total after summing over all hyperedges.  Hence

\[
 \sum_{w,r}\sum_{g\in G_{w,r}(D)}
 C^{\rm mat}_{w,r}(g)
 ={1\over2}\,6|\mathcal H_A[D,2D)|,
\]

which proves (0.4).  No endpoint or multiplicity factor is hidden here.

Dropping endpoint cleanliness replaces (C^{\rm mat}) by

\[
 C_{w,r}(g)
 =|\{n\in S_{w,r}:n+g\in S_{w,r}\}|
 =|S_{w,r}\cap(S_{w,r}-g)|.                           \tag{2.2}
\]

This proves the first inequality in (0.6).

## 3. The sharp local positive-gap envelope

Let (S\subset\mathbb Z) have size (B), and let
(G\subset\mathbb Z_{>0}) have size \(\alpha\).  Then

\[
 \boxed{
  \sum_{g\in G}|S\cap(S-g)|
  \le\min\left\{\binom B2,\alpha B\right\}.}          \tag{3.1}
\]

Indeed every summand is at most (B).  On the other hand, every ordered
occurrence (n,n+g\in S), with (g>0), is one unordered pair of
distinct elements of (S), and its positive gap determines (g)
uniquely.  Thus all (g\in G) together use at most \(\binom B2\) pairs.

Applying (3.1) to (S_{w,r}) and (G_{w,r}(D)) proves the second
inequality in (0.6).  This estimate can be attained to constant order by
interval-like fibres and initial positive-gap sets, so a further gain
must couple different fibres or directions.

## 4. What abstract summation can and cannot prove

First sum the pair side of (3.1).  An unordered pair of distinct vectors
of \(\mathscr D\) has exactly one primitive difference direction.  It
is counted for at most that one (w\in\mathcal W(A)).  Therefore

\[
 \sum_{w,r}\binom{B_w(r)}2\le\binom N2.               \tag{4.1}
\]

For the other side, the multiplicative interval lemma from the projection
note gives

\[
 \sum_r\alpha_{w,D}(r)^2\le8De_w,                     \tag{4.2}
\]

where (e_w=|T_w|).  With

\[
 E_w=\sum_rB_w(r)^2,
 \qquad
 \mathcal Z(A)=\sum_w\sqrt{e_wE_w},                  \tag{4.3}
\]

Cauchy--Schwarz yields

\[
\begin{aligned}
 \sum_{w,r}\alpha_{w,D}(r)B_w(r)
 &\le\sqrt{8D}\,\mathcal Z(A)\\
 &<\sqrt{6D}\,N^{3/2}.                               \tag{4.4}
\end{aligned}
\]

The last inequality uses the exact global budgets

\[
 \sum_we_w={N\over2},
 \qquad
 \sum_wE_w<{3N^2\over2}.                             \tag{4.5}
\]

Since the sum of minima in (0.6) is bounded by either complete sum,
(4.1) and (4.4) prove (0.8).

More generally, geometric interpolation between (4.1) and (4.4) gives,
for every (0\le\theta\le1),

\[
 |\mathcal H_A[D,2D)|
 \le {1\over3}
 \left(\binom N2\right)^{1-\theta}
 \bigl(\sqrt{6D}\,N^{3/2}\bigr)^\theta.              \tag{4.6}
\]

This has the phase transition (D\asymp N\): below it the old projection
side is stronger, while above it closure supplies only the fourth-order
pair cap.  No choice of \(\theta\) reaches (k^3+m^2) in the conjecturally
hard range (k^3>m^2).

## 5. A genuine high-band obstruction

For an odd prime (p), let

\[
 P_p=\{(x,[x^2]_p):0\le x<p\}\subset[0,p-1]^2.
\]

This is integer vector-Sidon.  There are \(\binom p3\) unordered triples
and fewer than (9p^2) exact integer sum cells.  Cauchy--Schwarz gives
\(\Omega(p^4)\) ordered pairs of distinct triples with the same sum, and
vector-Sidonicity makes their endpoint sets disjoint.  Hence

\[
 |\mathcal H_{P_p}|=\Omega(p^4).                       \tag{5.1}
\]

Only (O(p^2\log p)) hyperedges are collinear, while every nonzero
determinant is at most (2(p-1)^2).  Pigeonholing the (O(\log p))
dyadic bands gives a (D\le2p^2) with

\[
 |\mathcal H_{P_p}[D,2D)|
 =\Omega(p^4/\log p).                                 \tag{5.2}
\]

Apply a determinant-one integral shear avoiding the finitely many
quadratic distance-collision equations.  The resulting set is genuinely
Euclidean distance-Sidon at polynomial height, while every centroid
record and determinant is unchanged.  Equations (0.4) and (0.6) then
force

\[
 \mathcal K_D(A),\mathcal Q_D(A)
 =\Omega(k^4/\log k).                                 \tag{5.3}
\]

Thus closure, lattice index, vector injectivity, and endpoint matching do
not imply a near-cubic estimate without using the size of the Euclidean
realization.  This is the exact no-go boundary of the closed-fibre method.

## 6. The (p=43) endpoint audit

Take the least-residue (p=43) parabola and shear by (28).  It is a
genuine distance-Sidon set with (k=43), (m=1175), and (N=1806).
The following table records the clean hyperedge load, the unrestricted
closed-fibre functional, and the local-minimum relaxation.

\[
\begin{array}{r|r|r|r}
D&|\mathcal H_D|&\mathcal K_D&\mathcal Q_D\\ \hline
1&446&1590&2468\\
2&1006&4008&6848\\
4&2034&8028&14526\\
8&4258&16236&29534\\
16&8648&32826&58962\\
32&15514&59628&110770\\
64&25066&97872&189372\\
128&31370&121980&250432\\
256&27520&107742&222504\\
512&10236&42708&94340\\
1024&364&2796&8564
\end{array}                                           \tag{6.1}
\]

The clean quantity in (0.4) is (3|\mathcal H_D|).  In the bands
(1\le D\le512), the cost of discarding cleanliness after retaining
closure is only a factor (1.19) to (1.39).  Summed over all nonzero
bands,

\[
 \sum_D|\mathcal H_D|=126462,
 \quad
 \sum_D\mathcal K_D=495414,
 \quad
 \sum_D\mathcal Q_D=988320.                           \tag{6.2}
\]

The last number is below (m^2=1380625).  Therefore the finite-field
stress does not disprove (0.7), but it demonstrates that the third-vector
closure itself has already spent essentially all available combinatorial
gain.  The missing step must be a global, height-sensitive packing of the
positive-gap fibres in (0.6).

## 7. Verification

Run

    python3 phase2/loop/erdos1208/verify_large_determinant_closed_fibre_energy_gate.py

The verifier checks the unimodular coordinates, fibre symmetry, the exact
third-vector closure, the factor (3) in (0.4), both local envelopes in
(0.6), the universal band estimates, a complete (p=7) certificate, and
every entry of the (p=43) table.
