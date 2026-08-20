# The trace--area bi-matching block gate

## 1. Outcome

Fix a clean fibre `H_q` of size `h`, and write

\[
 N=\binom{k}{2}.
\]

Every clean start has a source edge and a translated clean-target edge.
Partition `H_q` into blocks in which both sets of edges are matchings.  If
there are `B` blocks, put the block index into the adaptive trace--area
charge from `ADAPTIVE_TRACE_AREA_ENDPOINT_CHARGE.md`.

The resulting exact reduction is:

> **Bi-matching block gate.**  If `h>k`, the blocks can be chosen with
> \(B=O(h/k)\), and their blockwise adaptive envelopes satisfy
> \[
>  \sum_{i=1}^B\mathcal B_{q,i}
>  \le m^{o(1)}N(h+k),                                    \tag{1.1}
> \]
> then
> \[
>  kN\le m^{2+o(1)},
> \]
> and hence \(k\le m^{2/3+o(1)}\).

This is a real improvement over asking for (1.1) on the whole fibre.  In
all five genuine stress tests below, blockwise selected energy is within
`1.3%` of the diagonal mass `hN`.

There is, however, an exact division of labour:

* if the maximum source-or-target endpoint degree is `O(h/k)`, the needed
  number of blocks follows by a greedy theorem;
* no such block count holds universally.  An infinite genuine
  distance-Sidon star family has `h=L`, `k=3L+3`, but needs `B=L` blocks;
* even restricting to heavy fibres does not repair the statement from the
  star-to-matching axioms alone.  An explicit abstract heavy family has
  \(B/(h/k)\to\infty\).

Thus a successful continuation must either control blockwise envelopes on
larger star/forest pieces, or use the endpoint translation equation to
exclude the abstract heavy imbalance.  Merely coloring the role-conflict
graph is not a complete proof.

## 2. Exact block-indexed charge

Let `U` be the canonically oriented vector of every edge, and let `U_i` be
the source vectors in block `i`.  For a record `(u,v) in U_i times U`, put

\[
 T(u,v)=|u|^2+18|v|^2,\qquad A(u,v)=\det(u,v).             \tag{2.1}
\]

Compute the trace and area loads **inside this block**, and route each
record through its less loaded marginal.  Let `B_{q,i}` be the sum of that
minimum load over all records in `U_i times U`.  The selected charge uses
keys

\[
 (i,0,T)\quad\hbox{or}\quad(i,1,A).
\]

Exactly as in the unblocked construction, its energy `E_i` obeys

\[
 E_i\le \mathcal B_{q,i}.                                 \tag{2.2}
\]

The scalar ranges give at most `42m^2+2` keys per block.  Since the total
mass is `hN`, Cauchy--Schwarz gives

\[
 (hN)^2
 \le B(42m^2+2)\sum_iE_i
 \le B(42m^2+2)\sum_i\mathcal B_{q,i}.                   \tag{2.3}
\]

Under (1.1), and using `h+k<=2h`, this implies

\[
 hN\le Bm^{2+o(1)}.                                      \tag{2.4}
\]

If `B=O(h/k)`, cancellation of `h` gives `kN<=m^(2+o(1))`.
This is why the apparently innocuous factor `h/k` is the exact target:
`B=O(k)` would return only the square-root scale.

## 3. The balanced-degree regime is rigorous

For every start `s`, write

\[
 \sigma(s)=\{c,d\},\qquad \tau(s)=\{e,f\},\qquad
 e+f=c+d+q.                                               \tag{3.1}
\]

Let `Delta` be the maximum endpoint degree among the source graph
`{sigma(s)}` and target graph `{tau(s)}`.  Make the role-conflict graph on
`H_q`, joining two starts if their source edges meet or their target edges
meet.  Its independent sets are precisely source-and-target bi-matchings.

The star-to-matching theorem says that the two conflict types cannot occur
for the same pair of records.  In particular, each record has at most

\[
 4(\Delta-1)                                               \tag{3.2}
\]

conflict neighbours.  Greedy coloring proves

\[
 \boxed{B\le4\Delta-3.}                                   \tag{3.3}
\]

Conversely, the records incident with a maximum-degree endpoint form a
clique, so

\[
 \boxed{B\ge\Delta.}                                      \tag{3.4}
\]

Also a source matching has at most `floor(k/2)` edges, whence

\[
 B\ge\left\lceil{h\over\lfloor k/2\rfloor}\right\rceil. \tag{3.5}
\]

Consequently

\[
 \Delta=O(h/k)                                            \tag{3.6}
\]

is a sufficient, and up to constants necessary, degree regime for the
block count.  In this regime the only remaining statement is the
blockwise envelope estimate (1.1).

## 4. A genuine infinite star obstruction

The restriction (3.6) is not automatic even in a genuine distance-Sidon
configuration.  Work first in the free abelian group with basis

\[
 Q,C,D_0,E_0,\ldots,D_{L-1},E_{L-1}
\]

and take

\[
 \mathcal P_L=\{0,Q,C\}\cup
 \{D_i,E_i,F_i:0\le i<L\},\qquad
 F_i=Q+C+D_i-E_i.                                        \tag{4.1}
\]

This is a difference-Sidon set: if one examines the private `(D_i,E_i)`
coordinates of a difference, two different occupied blocks identify both
endpoints immediately.  With one occupied block, the private signatures

\[
 (1,0),\ (0,1),\ (1,-1),\ (1,-1),\ (0,1),\ (-1,2)        \tag{4.2}
\]

coming from a block element or a same-block difference have only the two
displayed repetitions.  In those two cases the `(Q,C)` coordinates are,
respectively, different.  Differences among `0,Q,C` are also distinct.
Hence equality up to sign identifies the unordered endpoint pair.

Map the displayed basis, in order, to successive powers of an integer
`M>=10`.  Any alleged new equality of differences would give

\[
 \sum_j a_jM^j=0,\qquad |a_j|\le4,                        \tag{4.3}
\]

which is impossible by the leading digit.  Translating the resulting
integers to be nonnegative embeds `P_L` on a horizontal line in a lattice
box and preserves all distances.

Use anchors `a=Q,b=0`, so `q=Q`.  For every `i`,

\[
 E_i+F_i=C+D_i+q.                                        \tag{4.4}
\]

A direct private-coordinate check shows these are the only clean starts
in `H_q`.  Therefore

\[
 k=3L+3,\qquad h=L,                                      \tag{4.5}
\]

all source edges share `C`, and all clean-target edges form a matching.
Every bi-matching block contains at most one start, so

\[
 B=L,qquad {B\over h/k}=3L+3\longrightarrow\infty.       \tag{4.6}
\]

This obstruction is light (`h<k`), so it does not disprove the desired
cube-root theorem.  It does rigorously rule out silently assuming the
optimal block count for every fibre.

### A heavy role-combinatorial obstruction

The lightness is not removable using only the known role-conflict axioms.
Let `p` be an odd prime.  On four disjoint `p`-sets, index records by
`(i,j) in F_p^2` and put

\[
 \sigma(i,j)=\{R_i,C_j\},\qquad
 \tau(i,j)=\{U_{i+j},V_{i+2j}\}.                         \tag{4.7}
\]

If two source edges meet, their target edges are disjoint, and conversely.
Adjoin, on disjoint labels, a source star of degree

\[
 d=p\lfloor\sqrt p\rfloor                               \tag{4.8}
\]

whose target edges are a matching.  The combined abstract system has

\[
 k=4p+3d+1,\quad h=p^2+d,\quad \Delta=d.                 \tag{4.9}
\]

For all sufficiently large `p`, `h>k`, while

\[
 {B\over h/k}\ge {dk\over h}=\Theta(p).                 \tag{4.10}
\]

This is not asserted to obey the endpoint translation equation in the
integer plane.  Its point is exact: injectivity, source-star-to-target-
matching, the target-side dual, and heaviness do not imply the desired
block count.  Any proof of that count must use more geometry or arithmetic.

## 5. Fixed support patches and DRC do not close the gate

A second obstruction concerns the polynomial-minimum-degree support patch
from `ADAPTIVE_TRACE_AREA_ENDPOINT_CHARGE.md`.  There is a genuine
38-point distance-Sidon configuration with `h_q=9` whose trace--area
support contains an exact `K_{3,3}`.  After a common scale, its nine
selected vector records are

\[
\begin{array}{c|ccc}
 &A=4&A=204&A=444\\ \hline
T=7489 &(1;20,4)&(17;16,12)&(37;14,12)\\
T=11326&(2;25,2)&(34;23,6)&(74;17,6)\\
T=22084&(4;35,1)&(68;31,3)&(148;1,3),
\end{array}                                               \tag{5.1}
\]

where `(x;y,z)` means `u=(x,0),v=(y,z)`.  Thus

\[
 T=x^2+18(y^2+z^2),\qquad A=xz.                          \tag{5.2}
\]

All nine source norms are distinct, all nine target norms are distinct,
and the two norm sets are disjoint.  The verifier plants every record as a
clean translated edge pair with generic integer centers and checks the
entire 38-point set, not merely the nine-vector template.  Therefore no
universal forest, two-degeneracy, or fixed-`K_{3,3}` exclusion for genuine
trace--area support can be true.

Nor does dependent random choice alone convert polynomial minimum degree
into a forbidden fixed patch in the needed parameter range.  The incidence
graph of the projective plane over `F_p` is `(p+1)`-regular, has
`2(p^2+p+1)` vertices, and is `C_4`-free.  Hence purely graph-theoretic
minimum degree can grow as the square root of the support size without
even producing a rectangle.  These incidence graphs are not claimed to be
endpoint-realizable; they show exactly where an arithmetic classification
would have to enter.

The standard Elekes--Ronyai setup does not directly supply that
classification.  Here an edge of the support is the joint image

\[
 (u,v)\mapsto
 \bigl(|u|^2+18|v|^2,\det(u,v)\bigr)                     \tag{5.3}
\]

of two two-dimensional vector sets, with one set carrying a separate
four-endpoint translation decoration.  It is not a dense level set of one
bivariate polynomial on two scalar sets.  Reducing (5.3) to an applicable
polynomial-expansion theorem remains a substantive missing lemma.

## 6. Blockwise stress audit

The block charge itself survives all current genuine stresses.  The table
uses a deterministic DSATUR coloring of the role-conflict graph.

\[
\begin{array}{l|r|r|r|r|c}
\text{instance}&k&h&B&\Delta&\sum_i\mathcal B_{q,i}/(hN)\\ \hline
\text{closure-40}&40&23&4&4&1.016945\\
\text{closure-120}&120&127&6&6&1.012419\\
\text{Costas-22}&22&34&7&7&1.005602\\
\text{parabola-image-43}&43&171&14&14&1.001049\\
\text{two-arm-50}&100&114&10&9&1.000062
\end{array}                                               \tag{6.1}
\]

The corresponding selected energies are no larger.  These computations
are evidence for (1.1), not a proof.  They also show the precise tension:
the scalar energy becomes essentially diagonal after splitting, while the
number of colors is the delicate endpoint quantity.

## 7. Status and next theorem

The durable positive result is the balanced-degree reduction

\[
 \Delta=O(h/k)quad+\quad\text{blockwise (1.1)}
 \quad\Longrightarrow\quad k\le m^{2/3+o(1)}.            \tag{7.1}
\]

The durable negative results are:

1. the optimal block count fails on an infinite genuine star family;
2. role-conflict combinatorics alone fails even in a heavy abstract family;
3. genuine support can contain `K_{3,3}`;
4. polynomial minimum degree alone has high-girth graph models.

The sharp surviving target is therefore a star-sensitive endpoint theorem:
either decompose a heavy clean fibre into `O(h/k)` pieces larger than
bi-matchings on which the adaptive envelope is still near diagonal, or
prove that endpoint translation forbids the heavy abstract imbalance.

Run

```text
python3 phase2/loop/erdos1208/verify_trace_area_bimatching_block_gate.py
```

for the exact star family, abstract heavy role system, genuine `K_{3,3}`
certificate, projective-plane high-girth audit, block coloring, and all
profiles in (6.1).
