# Affine double-endpoint barrier for the pencil orientation gate

## 1. Outcome

The two canonical endpoint colourings of the block-intersection graph do
not, by themselves, imply the pencil-orientation estimate in
`ROTATED_TRANSLATE_SELF_REPRODUCTION_GATE.md`.

For every prime power `q`, there is a linear uniform block system with

\[
 k=q-1,
 \qquad |\mathcal B|=k(k-1)+1,
 \qquad |U|=k^2+2k-1,
\]

having all of the following properties.

1.  Its block-intersection graph has two orthogonal proper `k`-colourings.
    A nonzero block is labelled by one cell `(i,j) in (F_q^*)^2` with
    `i!=j`; equal first labels and
    equal second labels are both independent sets.
2.  There are exactly `k(k-1)` such nonzero blocks and one isolated zero
    block, just as for the complete difference set of a vector-Sidon
    `k`-point set.  Every block has size `k`.
3.  Every point pencil is a clique of size at most `k`, meeting every first- and second-colour
    class at most once.  Thus every pencil is a perfect matching between
    its two endpoint-label sets, exactly as in the Erdős 1208 block graph.
4.  The incidence graph even has a proper `k`-edge-colouring: every block
    sees all `k` labels and every pencil sees distinct labels.  This is the
    abstract analogue of the third endpoint in `x=p+J(r-q)`.
5.  Every two blocks meet in at most one point, and every edge of the
    block-intersection graph lies in exactly one pencil.
6.  Nevertheless, for **every** orientation, the pencil cost is larger
    than the target scale by a factor of order `k`.

Consequently an orientation based only on the two endpoint partitions, or
on the abstract matching shape of the pencils, cannot prove the cubic
support theorem.  The next argument must retain the characteristic-zero
translate identity

\[
 B_d=A+Jd
\]

and the fact that every nonzero `d` is the canonical difference of one
ordered pair of the same Euclidean distance-Sidon set `A`.

## 2. The affine construction

Work over `F_q`.  The points of the incidence system are the nonhorizontal
affine lines

\[
 U=\{(a,b):a\in F_q^*,\ b\in F_q\},
\]

where `(a,b)` denotes the line `y=ax+b`.  For every punctured cell
`(i,j) in (F_q^*)^2` with `i!=j`, take the block

\[
 B_{i,j}=\{(a,j-ai):a\in F_q^*\}.               \tag{2.1}
\]

Thus `B_(i,j)` is the set of allowed affine lines through `(i,j)` and has
size `k=q-1`.  Adjoin one further isolated block on `k` private points;
this is the analogue of the zero difference.

Two distinct cells `(i,j)` and `(i',j')` lie on one allowed line precisely
when

\[
 i\ne i',\qquad j\ne j'.                        \tag{2.2}
\]

In that case the slope and intercept are uniquely determined.  Therefore
the block-intersection graph is the complement of the rook graph on the
off-diagonal part of the `k` by `k` punctured cell array.  Its row classes and column classes give the two
orthogonal proper colourings.

For a point `(a,b) in U`, its pencil is

\[
 S_{a,b}=\{(i,ai+b):i,ai+b\in F_q^*\}.          \tag{2.3}
\]

After deleting diagonal cells, every nonempty pencil has size `k`, `k-1`,
or `k-2`, with at most one cell in every row and column, and is a clique.
Every edge satisfying (2.2) determines its unique line `(a,b)`, so it is
internal to exactly one pencil.

There is also an explicit third matching label.  Give the incidence of the
cell `(i,j)` with the line of slope `a` the label

\[
 \lambda=ia\in F_q^*.                           \tag{2.4}
\]

At a fixed cell, varying the `k` slopes gives all `k` labels.  Along a fixed
line, distinct cells have distinct first coordinates and hence distinct
labels.  Thus even the full three-coordinate-matching abstraction survives
in the countermodel.

## 3. Failure of every orientation

Let `I` be the number of edges in the block-intersection graph.  There are
`k-1` pencils of size `k`, `k` pencils of size `k-1`, and `k(k-1)` pencils
of size `k-2`.  Counting inside them gives

\[
 I=(k-1){k\choose2}+k{k-1\choose2}
      +k(k-1){k-2\choose2}.                     \tag{3.1}
\]

Orient the graph arbitrarily.  Define `c_x` for a pencil exactly as in the
live gate: it is the number of oriented edges whose tail lies in the pencil
and whose head lies outside it.  Since every block has `k=q-1` points, the
orientation-independent mass identity remains

\[
 \sum_{x\in U}c_x=(k-1)I=(q-2)I.                \tag{3.2}
\]

Cauchy--Schwarz, including the `k` private zero-block points with load zero,
and `|U|=k^2+2k-1` now force

\[
 \sum_xc_x^2
 \ge{(k-1)^2I^2\over k^2+2k-1}.                \tag{3.3}
\]

Relative to the desired scale `I^2/k`, this says

\[
 {k\sum_xc_x^2\over I^2}
 \ge{k(k-1)^2\over k^2+2k-1}
 =\Theta(k).                                    \tag{3.4}
\]

The loss is a full power, not a logarithm or a defect of random
orientation.  No correlated orientation can repair it at this abstract
level.

The construction is not a counterexample to the Erdős 1208 theorem.  Its
blocks are affine-line pencils, not the simultaneous translates `A+Jd` of
one torsion-free complete difference set, and it has no Euclidean radial
uniqueness.  Its purpose is to isolate those properties as indispensable.

## 4. Exact characteristic-zero obstruction to the affine model

One feature of the finite-field model explains sharply why it cannot be the
real translate system.  For every nonidentity slope `a`, the pencil with
intercept zero has all `k` cells

\[
 (r,ar),\qquad r\in F_q^*,
\]

and the third incidence label from (2.4) is `p=ar`, equal to the second
endpoint label `q=ar` at every cell.

The corresponding full pencil is impossible over the reals.

### Contraction lemma

Let `A` be a nonempty finite subset of `R^2`.  If `sigma:A->A` is a
permutation and one point `x` satisfies

\[
 x=\sigma(r)+J(r-\sigma(r))                     \tag{4.1}
\]

for every `r in A`, then `A={x}`.

Indeed, (4.1) rearranges to

\[
 \boxed{
 \sigma(r)-x={I-J\over2}(r-x).}                 \tag{4.2}
\]

The linear map `(I-J)/2` is a similarity of ratio `1/sqrt(2)`.  Every orbit
of a permutation of a finite set is periodic.  Iterating (4.2) around such
an orbit multiplies the distance from `x` by a strict power of
`1/sqrt(2)`, so that distance must be zero.  This proves the lemma.

Thus the abstract design's full `p=q` pencils are killed by the literal
characteristic-zero equation `x=p+J(r-q)`, not by its three matching
labels.  A quantitative stability version is a concrete possible next
step: a nearly complete affine-like core would have to avoid these
contracting pencils, or else pay exponential coordinate height.

The lemma alone does not prove the cubic support theorem.  The hard fibres
need not contain a large `p=q` submatching; indeed all common-endpoint roles
together have only quadratic total mass.  Its value is to identify one
exact algebraic obstruction that the finite-field orientation barrier
cannot imitate.

## 5. Verification

`verify_affine_double_endpoint_orientation_barrier.py` checks (2.1)--(3.4)
by exact finite-field enumeration for `q=5,7,11,13`.  It also constructs a
lexicographic orientation, verifies the pencil mass identity directly, and
checks both endpoint colourings, the third incidence label, and the
unique-centre property.  It also verifies that the `k-1` nonidentity
zero-intercept pencils are full and have third label equal to their second
endpoint label, the hypothesis excluded by the contraction lemma.
