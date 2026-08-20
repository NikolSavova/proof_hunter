# Adversarial stress of the surviving metric scalar gate

## 1. Verdict

No genuine integral distance-Sidon counterexample to the metric scalar gate
was found.  The strongest tested pointwise ratio is

\[
 \boxed{
 \max_q{\mathcal M_{q,18}\over N(|H_q|+k)}
 =0.8220314424\ldots}                                      \tag{1.1}
\]

on an integral affine deformation of the 43-point parabola image.  Its
maximum charge load is only three.  Almost all of its off-diagonal excess is
in the exact core left by the proved reductions: four distinct edges,
squareclass-transverse, and large target determinant.  Even there the
excess remains a small fraction of the allowed pointwise budget.

The search therefore gives no evidence that the pointwise scalar gate is
false.  It gives stronger evidence for an aggregate version which would be
enough for Erdős problem 1208 even if rare pointwise fibres eventually
fail.

## 2. The exact aggregate conjecture

Put

\[
 h_q=|H_q|,\qquad S=\sum_qh_q,qquad
 \mathcal X_q=\mathcal M_{q,18}-Nh_q.                       \tag{2.1}
\]

The computationally suggested target is

\[
 \boxed{
 \sum_q\mathcal X_q\le m^{o(1)}Nk^3.}                      \tag{2.2}
\]

Equivalently,

\[
 \sum_q\mathcal M_{q,18}
 \le m^{o(1)}N(S+k^3).                                     \tag{2.3}
\]

This is weaker than summing the pointwise estimate only in how it allows
different fibres to compensate: a rare bad fibre is permitted provided its
excess is paid for by the global `Nk^3` endpoint budget.

### Why (2.2) resolves #1208

The scalar charge has `O(m^2)` values.  Cauchy--Schwarz on each fibre gives

\[
 h_q^2N^2\ll m^2\mathcal M_{q,18}.                          \tag{2.4}
\]

Sum (2.4), use (2.3), and then use Cauchy over the at most `k(k-1)` realized
differences:

\[
 \sum_qh_q^2\le {m^{2+o(1)}\over N}(S+k^3),
 \qquad
 S^2\le k^2\sum_qh_q^2
 \le m^{2+o(1)}(S+k^3).                                    \tag{2.5}
\]

Solving the quadratic inequality and using
`m k^(3/2)<=(m^2+k^3)/2` yields

\[
 S\le m^{2+o(1)}+k^{3+o(1)}.                               \tag{2.6}
\]

Since `C_6(A)=4S`, this is the required ambient equal-centroid estimate and
gives the cube-root bound.

## 3. Affine metric search

An invertible integral linear map preserves every pair-sum relation and
every clean fibre while changing squared distances from `|v|^2` to a
positive definite integral binary quadratic form.  This makes affine
deformation a clean adversarial test: it searches metric resonance without
changing the additive closure.

The verifier generates 300 seeded integral matrices in addition to the
identity on `transformed_parabola_43()`.  After quotienting common scalar
factors, it finds 295 distinct positive forms; 291 remain distance-Sidon.
The strongest form is

\[
 Q(x,y)=x^2-2xy+17y^2,                                     \tag{3.1}
\]

realized up to the harmless factor ten by

\[
 M=\begin{pmatrix}-3&-1\\-1&13\end{pmatrix},qquad
 M^TM=10\begin{pmatrix}1&-1\\-1&17\end{pmatrix}.          \tag{3.2}
\]

On the initially selected largest fibre this form has energy `158371` and
maximum load three.  Searching all fibres of the champion gives energy
`158851` at `h=171`, producing (1.1).

For that worst fibre,

\[
\begin{array}{c|r}
\text{mass }hN&154413\\
\text{off-diagonal excess}&4438\\
\text{four-distinct-edge collisions}&4416\\
\text{squareclass-transverse}&4416\\
\text{large target area }|2\det|>N/h&4370\\
\text{low area}&46
\end{array}                                                 \tag{3.3}
\]

All 46 low-area rows have parallel target edges.  Among the 4,370 surviving
large-area rows, 428 have a source-edge endpoint overlap, 394 have a
target-edge endpoint overlap, only 30 have both, and 3,578 have neither.
Across all six pairs among the four edges, 2,232 rows are fully endpoint-
disjoint.  Thus neither parallel resonance nor shared endpoints explain the
champion: the fully disjoint large-area rows alone form the majority of its
modest excess.

## 4. All-fibre profiles

For each family define

\[
 R_\infty=\max_q{\mathcal M_q\over N(h_q+k)},\qquad
 R_{\rm agg}={\sum_q\mathcal M_q\over N(S+k^3)},\qquad
 R_{\rm off}={\sum_q(\mathcal M_q-Nh_q)\over Nk^3}.        \tag{4.1}
\]

The verifier evaluates every nonempty clean fibre using the exact
difference-correlation formula.

\[
\begin{array}{c|r|r|r|r|r}
\text{family}&\#q&S&R_\infty&R_{\rm agg}&R_{\rm off}\\ \hline
\text{closure }40&1518&12420&0.419048&0.168350&0.006958\\
\text{Costas }22&462&9342&0.647959&0.483061&0.029525\\
\text{parabola }43&1806&190278&0.814518&0.714093&0.029853\\
\text{champion deformation}&1806&190278&0.822031&0.717499&0.041410\\
\text{source closure }45&1920&12834&0.340902&0.125560&0.002405\\
\text{perpendicular ruler }40&774&4914&0.259687&0.071347&0.000044
\end{array}                                                 \tag{4.2}
\]

The champion increases transverse collisions, but its total off-diagonal
mass is still only `0.041411 Nk^3`.  The aggregate conjecture has much more
slack than the pointwise inequality on every tested family.

## 5. A genuine transverse multi-arm stress

To test whether many resonant channels cooperate, take a dense scalar Golomb
ruler on each of the primitive directions

\[
 (1,0),(1,1),(1,2),(1,3),(2,3),(1,4).                     \tag{5.1}
\]

Their primitive squared norms have distinct squareclasses.  Translate the
arms successively along `(Z,Z^2+j)`, choosing the first integral `Z` for
which all distances remain distinct.  The verifier checks the resulting
sets are genuine integral distance-Sidon sets before measuring all clean
fibres.

For the 20-mark arms:

\[
\begin{array}{c|r|r|r|r|r}
\text{arms}&k&S&R_\infty&R_{\rm agg}&R_{\rm off}\\ \hline
2&40&11520&0.406315&0.153039&0.000586\\
3&60&17856&0.319029&0.076498&0.000156
\end{array}                                                 \tag{5.2}
\]

The same monotone dilution occurs for 12- and 16-mark arms.  Adding a new
internal direction creates another possible scalar channel, but it also
creates cross-edges to every old arm.  The target population grows
quadratically in the number of arms while the structured internal-edge
population grows only linearly.  The possible linear load amplification is
therefore paid for by `N`.

This suggests the structural mechanism behind (2.2):

> **Parallel-cover compensation conjecture.**  Any collection of direction
> or squareclass channels which creates `L`-fold scalar-charge overlap must
> expose `Omega(L^2)` cross-edge endpoint pairs, and their contribution to
> `N` globally pays for the overlap.  After summing over `q`, the unpaid
> transverse excess is at most `m^(o(1))Nk^3`.

The first sentence is deliberately a structural conjecture rather than a
formal theorem; an eventual proof must formulate the relevant channel cover
so that shared endpoints and nonparallel equal-squareclass vectors are
included.  The exact proposed inequality is (2.2).

## 6. Status

The search does **not** support the scenario “pointwise false but aggregate
true”; it found no pointwise violation at all.  What it does show is that
the aggregate conjecture is more robust, has a direct proof implication for
#1208, and survives the strongest affine, large-area, parallel, shared-
endpoint, Costas, closure, and multi-arm stresses currently available.

Run `verify_metric_scalar_adversarial_stress.py` to reproduce the affine
scan, every all-fibre total in (4.2), the champion core decomposition, and
all eight multi-arm certificates.
