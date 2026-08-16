# Square-to-linear barrier: the carrier--root rectangle

**Date:** 2026-08-15.  All logarithms are base two.  This is a counting
barrier, not a planar realization.

## Verdict

The complete middle layer, the full released cube, the entire completion
bank, and the marked half-plane bank do **not** by themselves convert the
two-face estimate `(3z)` into a linear fixed-power EIC charge.  There is an
explicit scalable four-local face complex with

\[
 |U_c|=2r,\quad k={2r\choose r},\quad m=\Theta(n),\quad
 b=2,\quad q=2r+3=\Theta(\log n),                         \tag{1}
\]

whose canonical cells have marked mass `M`, while the number `V` of
ordinary faces satisfies

\[
                         V=(1+o(1))M.                      \tag{2}
\]

For every cell and every one of its `m` completion labels, the construction
has a collision-free `h=2^r` subbank of the at least `2^(r+1)` marked
half-plane outputs.  Nevertheless completion outputs
are reused along a root axis and half-plane outputs along an independent
carrier axis.  The pair `(completion,half-plane output)` has multiplicity
**one**.  Thus the example satisfies a stronger decoder than `(3z)` and
still has no linear saving.

Every root block has exactly the full-cube incidence table of the
small-carrier parabola regression.  The construction also satisfies the
formal planar four-local rule

\[
 S\text{ is a face}\quad\Longleftrightarrow\quad
 \text{every four-subset of }S\text{ is a face}            \tag{3}
\]

(with every set of rank at most three a face).  What is **not** proved is
realizability by one planar order type.  Consequently this is not a
counterexample to EIC'.  It proves that the missing theorem must use a
geometric compatibility between the carrier and root axes, beyond bank
sizes, exact pair decoding, complete layers, and four-locality.

## 1. Parameters and the two axes

Fix `r` tending to infinity and put

\[
 p=2r+1,\qquad a=4^r,\qquad t=pa,\qquad
 k={2r\choose r},\qquad h=2^r.                             \tag{4}
\]

Take four disjoint label classes, each of size `t`:

* carrier labels `A`;
* root labels `Z`, partitioned into `g=t/p=a` blocks `W` of size `p`;
* pocket labels `X`;
* background labels `G`.

Every carrier edge is used: the carrier family is the whole set
`{A choose 2}`.  For every pair `(e,z)` with `e in {A choose 2}` and
`z in Z`, make one central cell.  Thus

\[
 C={t\choose2},\qquad N=Ct,qquad M=Nk.                    \tag{5}
\]

If `z in W`, set `U_z=W setminus {z}`.  Then `|U_z|=2r`, and
the cell has the complete middle guard layer `{U_z choose r}` of weight
`k`.  Formally, its marked source occurrences are the labelled tuples
`(e,z,D)`, `D in {U_z choose r}`.  Distinct tuples are distinct marked
occurrences even if their underlying unmarked source sets coincide.  This
is exactly the weighted-incidence convention in the live gate; it is not a
claim that a planar canonical selector must retain all such tuples.

The source multiplicity is also controlled exactly.  For fixed `(e,W)`, an
underlying source `e union R`, `R in {W choose r+1}`, is represented by the
`r+1` tuples `(e,z,R setminus {z})`, `z in R`, and no others.  Equivalently,

\[
                 p{2r\choose r}=(r+1){2r+1\choose r+1}.   \tag{5a}
\]

Thus `M` is a genuine weighted marked-incidence mass with logarithmic
unmarked load, exactly on the allowed `O(log n)` bounded-rank scale.  Its
full released cube is

\[
 \mathcal A_{e,z}=
 \{e\cup\{z\}\cup D:D\subseteq U_z\},\qquad
 |\mathcal A_{e,z}|=a.                                    \tag{6}
\]

For fixed `(e,W)`, the `p` cells have common top face `e union W`.  An
output `e union S`, `emptyset ne S subseteq W`, lies in exactly `|S|` of
their cubes.  Hence

\[
 \left|\bigcup_{z\in W}\mathcal A_{e,z}\right|=2^p-1=2a-1,
 \qquad
 \sum_{z\in W}|\mathcal A_{e,z}|=pa.                      \tag{7}
\]

This is precisely the root/cube table of the `2r+1`-root parabola cage.
In particular its mean cube degree is `pa/(2a-1)=Theta(r)`, and more than
half of every cube has degree greater than `r^(1/3)` for all large `r`.
The construction is therefore in the genuine heavy-cube branch, not the
already discharged low-overlap branch.

## 2. Completion and half-plane banks form a rectangle

For every cell `(e,z)` use all `m=t` completion faces

\[
                         Y_{e,x}=e\cup\{x\},\qquad x\in X. \tag{8}
\]

The output `Y_(e,x)` is shared by all `t` roots.  In terms of top groups, it
is shared by the `g=t/p` distinct groups `(e,W)`.

Give every root block the cyclic regular tournament orientation, and let
`H_z` be the out-neighbourhood of `z`.  Thus

\[
 H_z\subseteq W(z)\setminus\{z\},\qquad |H_z|=r.          \tag{9}
\]

For every cell `(e,z)` and every `x in X`, use the marked half-plane bank

\[
 \mathcal H_{e,z,x}=
 \{F_{z,x,S}:=\{x,z\}\cup S:S\subseteq H_z\},
 \qquad |\mathcal H_{e,z,x}|=h.                           \tag{10}
\]

This is only one factor two smaller than the guaranteed richer-side bank
for `q=2r+3`, and has the exact root-only profile of such a subbank.  The
four-local construction does not assert that all these cyclic sides are
simultaneously realizable by one planar order type.

These outputs are independent of `e`.  Thus a half-plane face is shared by
all `C=binom(t,2)` carriers.  On the other hand

\[
       (Y_{e,x},F_{z,x,S})\quad\text{determines}\quad(e,z,x,S).       \tag{11}
\]

Indeed, if one root set could be emitted with two distinct marks `z,z'`,
then both tournament arcs `z -> z'` and `z' -> z` would be required.  Hence
the root mark is intrinsic to the output, and the completion--half-plane
pair multiplicity is exactly one.  The exact
bank statistics are

\[
\begin{array}{c|c|c}
\text{bank}&\text{distinct outputs}&\text{record load}\\
\hline
\text{completion}&Ct&t\text{ roots per output}\\
\text{half-plane}&t^2h&C\text{ carriers per output}\\
\text{ordered pair}&Ct^2h&1.
\end{array}                                                \tag{12}
\]

The pair graph is the disjoint union over `x in X` of complete bipartite
graphs

\[
                   K_{C,\,th}.                            \tag{13}
\]

This is the exact square obstruction.  Low completion overlap and low
half-plane overlap cannot be forced simultaneously: their high-degree
directions are perpendicular, while retaining both outputs decodes the
record perfectly.

## 3. A four-local ordinary-face complex

It remains to show that the preceding banks can coexist with
`Theta(V)` marked mass, rather than merely fitting in a formal `V^2`
output square.

Define the good four-subsets on `A union Z union X` to contain every
four-subset of

\[
                         e\cup W                           \tag{14}
\]

for every carrier edge `e` and root block `W`, and every four-subset of

\[
                         \{x,z\}\cup H_z                  \tag{15}
\]

for every `(x,z)`.  This makes all outputs in (6), (8), and (10) faces.

Partition `G` into four equal parts.  The complete four-partite
four-graph on `G` has `(t/4)^4` edges and contains no complete
five-vertex four-graph.  For all sufficiently large `r`,

\[
 M={t\choose2}tk\le (t/4)^4,                              \tag{16}
\]

because the ratio of the two sides is

\[
 {M\over(t/4)^4}=128(1-1/t){k\over t}=O(r^{-3/2}).        \tag{17}
\]

Choose exactly `M` of these background four-edges and add them to the good
four-subsets.  There are no other good four-subsets.

Finally declare every set of rank at most three to be a face, and a larger
set to be a face exactly when all its four-subsets are good.  This is an
exact hereditary four-local face complex.  A face of rank at least four
cannot mix `G` with the other classes.  Inside `G`, the four-partite
construction has no face of rank at least five, so it contributes exactly
`M` high-rank faces.

For completeness, all high-rank gadget faces admit the following crude but
sufficient classification.  Their root labels lie in one block.  A face
without a pocket label uses at most two carrier labels; a face with a
pocket label uses no carrier label and at most one pocket label.  Therefore
their number is at most

\[
 V_{\rm gad}
 \le g\,2^p\left(1+2t+{t\choose2}\right).                \tag{18}
\]

There are at most `sum_(i=0)^3 binom(4t,i)` low-rank faces.  If `V` denotes
the total number of faces, (16)--(18) give

\[
\begin{aligned}
 M\le V
 &\le M+\sum_{i=0}^3{4t\choose i}
       +g\,2^p\left(1+2t+{t\choose2}\right),\\
 {V-M\over M}
 &=O(r^{-1/2})+O(r^{3/2}/t)=o(1).                         \tag{19}
\end{aligned}
\]

This proves (2).  Notice also that `n=4t`, `m=t=Theta(n)`, and
`r=(1/2+o(1))log n`, so the example lies in the central logarithmic,
small-carrier scale.

## 4. Exact consequence for the proof route

Suppose a proposed square-to-linear lemma uses only the following data:

1. complete middle weight `k=binom(2r,r)` per cell;
2. the full cube (6) and its actual aggregate degrees;
3. all `m` completion faces;
4. all `mh` marked half-plane records;
5. a polynomial, or even injective, decoder for the ordered output pair;
6. heredity and planar four-locality of the face family.

Then the lemma cannot conclude `M<=n^(-epsilon)V` for any fixed positive
`epsilon`: the system above has `M/V -> 1`.  In particular Cauchy applied
to the two output coordinates cannot bridge `(3z)` by itself.

The regression does **not** say that the rectangular pattern is realizable
by a planar point set.  That is now the exact positive target: show that a
large family of root blocks and carrier edges cannot simultaneously realize
the two perpendicular reuse relations (8) and (10).  Equivalently, planar
circuit interactions between two carriers and two roots must create a new
ordinary-face bank, or must force one axis of the rectangle to have
fixed-power smaller degree.  Any proof of this statement would use geometry
strictly beyond the current four-local bank accounting.

There is a second, logically separate escape: prove that the live canonical
marking cannot retain all labelled occurrences `(e,z,D)` in this rectangle.
The construction counts exactly the weighted marked occurrences used in
`M`, with the explicit logarithmic source load in (5a).  If the actual
selector is injective on underlying source faces, or has a substantially
smaller root multiplicity for geometric reasons, that is additional
structure not represented by the four-local model and could also break the
regression.

## 5. Verification artifact

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_square_to_linear_rectangle_barrier.py
```

The verifier checks the exact parameter identities, background capacity,
cube degrees, pair injectivity on a finite rectangle, and the asymptotic
face-count ratios in (19).
