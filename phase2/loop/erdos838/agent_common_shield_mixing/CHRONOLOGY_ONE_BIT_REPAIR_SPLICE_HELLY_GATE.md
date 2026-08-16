# Cross-circuit chronology versus the one-bit repair alphabet

## Verdict

The one-bit relocation theorem closes a long cross-circuit chronology once
the chronology has already been promoted to a bounded-menu, fixed-edge
certificate.  The distinct physical completion labels on a retained path
then cost only one bit each, so `k=O(log n)`, and a polylogarithmic edge menu
costs only `G=O(log n log log n)`.

It does **not** splice for free into the surviving near-uniform role forest.
There is an exact selection-versus-relocation inequality.  At a role with
alphabet size `d` and maximum conditional label mass at most `K/d`, retaining
`s` label classes and relocating those `s` physical labels costs

\[
             g+s\ge \log(d/K)+1                            \tag{1}
\]

whenever `d/K>=2`; here `g` is the logarithmic retained-mass loss.  Hence
`Theta(L)` roles with `d_i>=n^gamma` and `K_i=poly(L)` force

\[
                G+k\ge \Theta(L^2)-O(L\log L),             \tag{2}
\]

exactly exhausting the fixed-gap budget.  Choosing one chronology path has
`k=Theta(L)` but quadratic `G`; keeping the whole forest avoids `G` only by
making the physical repair alphabet enormous.  Any successful splice must
sum different branches through recoverable ordinary/profile outputs.  That
summation is already the missing cycle/profile bank, not a consequence of
the one-bit theorem.

Fixed actual circuits also do not automatically provide fixed boundary
edges.  A rational stretchable family below has arbitrarily many distinct
completion labels and, at every chronology level, the same fixed inner
`1+3` circuit across three literal released faces.  Nevertheless no position
of the repair label makes all three released unions ordinary.  Every pair is
simultaneously repairable, so this is a genuine three-ear Helly obstruction.
It is a promotion barrier, not a live sub-half construction: the obstruction
itself supplies only `2^{O(L)}` internal completion faces when its length is
`O(L)`.

## 1. Exact alphabet-selection tradeoff

At one role let the conditional label masses be `p_z`, with

\[
                       \max_z p_z\le {K\over d}.          \tag{3}
\]

Suppose a proposed repaired subcertificate retains a set `S` of `s`
physical labels.  Its retained conditional mass `alpha` obeys

\[
               \alpha\le \min\{1,Ks/d\}.                 \tag{4}
\]

The selection loss is `g=-log alpha`, while the multi-label relocation
theorem charges `s` bits.  Put `D=d/K`.  If `s<=D`, then

\[
 g+s\ge\log(D/s)+s=\log D+(s-\log s)\ge\log D+1.         \tag{5}
\]

For integral `s>=1`, the last inequality is exactly `2^{s-1}>=s`.  If
`s>=D>=2`, then `g+s>=s>=log D+1`.  This proves (1).

The same calculation is valid conditionally at every node of a retained
role-forest branch.  Role supports are disjoint, so selected physical labels
at different roles are distinct and their relocation costs add.  Therefore

\[
       \boxed{\quad G+k\ge
           \sum_{j=1}^q\bigl(\log(d_j/K_j)+1\bigr).\quad} \tag{6}
\]

Here `G` includes only actual retained-mass/decoder loss which is not
recovered by disjoint ordinary outputs.  If different branches already have
recoverable output identifiers, they should be summed rather than charged
in `G`; doing so is precisely the desired bank alternative.

On the low-`Q_eff` role-forest branch,

\[
 K_j=L^{O(1)},\qquad d_j\ge n^\gamma
\]

at all but `o(L)` of `q=theta L` deleted roles.  Equation (6) then gives

\[
                  G+k\ge\theta\gamma L^2-O(L\log L).     \tag{7}
\]

Thus the new relocation theorem removes wall-crossing cost, but not the
entropy cost of identifying which physical labels are to be relocated.

Two endpoint choices calibrate (6):

* one selected label per role has `k=q` and
  `G>=sum_j log(d_j/K_j)`;
* retaining every label class has negligible selection loss but
  `k>=sum_j d_j`.

Intermediate subsets cannot improve their sum below (6).

## 2. Exact positive splice after edge localization

Consider a chronology with distinct repair labels

\[
                         z_1,\ldots,z_q.                 \tag{8}
\]

At turn `j`, suppose the only missing recurrence bank has the literal form

\[
          \{R\cup\{z_j\}:R\in\mathcal H_j\},            \tag{9}
\]

where every `R` is an ordinary face containing the same exposed edge `e_j`,
and all vertices of all such `R` lie on the same side of `e_j`.  Assume:

1. the edge and the turn are recovered from the literal source/history;
2. every already certified output omits the full repair alphabet (the
   chronology labels are reattached only in the decoder);
3. all repaired cap, cup, and ordinary recurrences form one approximate
   strong tree in one fixed generic chart; and
4. its other decoder loss is `G_0`.

The common-star ear lemma supplies one open chamber for (9).  The labels in
(8) are distinct, so their positions can be chosen independently; generic
rational choices avoid every old pair line and every common-chart vertical
tie.  The resulting certificate is single-ear deficient with

\[
                         k=q,qquad G=G_0.               \tag{10}
\]

If `e_j` must be chosen from a recoverable menu of `t_j` edge classes, retain
a heaviest class at each turn.  Then

\[
                   k=q,qquad G\le G_0+\sum_j\log t_j.   \tag{11}
\]

Thus `q=O(L)`, `t_j=poly(L)`, and `G_0=O(L log L)` give
`G+k=o(L^2)` and the fixed-gap repair theorem applies.

### Fixed circuit versus fixed edge

Suppose a fixed bad circuit at turn `j` is

\[
                         \{z_j,a_j,b_j,c_j\},            \tag{12}
\]

with `z_j` the inner point.  If every reduced source in (9) contains the
outer triple and exposes at least one of the three edges
`a_jb_j,b_jc_j,c_ja_j`, then a three-class partition supplies (11) with
`t_j<=3`.  Once an edge is fixed, the third outer vertex fixes the common
side.  Hence this boundary-incidence hypothesis costs only `q log 3=O(L)`.

Neither part is automatic:

* the deleted completion label can be an **outer** circuit point;
* the three outer labels can be nonconsecutive vertices of every full
  source, so none of their three edges is exposed; and
* even with an inner deleted point, different full sources can demand
  incompatible non-circuit ear cells.

Moreover, the only unconditional guarantee obtained by fresh pigeonholing
among all actual circuits costs

\[
                  q\log\bigl(2{n\choose4}\bigr)
                         =\Theta(qL).                   \tag{13}
\]

For `q=Theta(L)` this guaranteed bound is quadratic; the chronology theorem
alone supplies no smaller one.  Fixed-circuit localization is useful
only when the circuit/edge is already recovered from retained physical data,
or its menu is `2^{o(L)}` per turn.  The variable-witness fixed-label
chronology does not supply this for free.

## 3. Literal released-face stability

The deletion chronology proves that the reduced completion and the released
endpoint remain ordinary after deleting `z_j`.  This is exactly the heredity
needed for (9), but it is weaker than single-ear deficiency.  Relocating
`z_j` may change every certified face that contains it.  Therefore the splice
requires the following literal separation:

\[
 \begin{array}{c|c}
 \text{missing bank}&R+z_j\text{ with }R\text{ literally recoverable},\\
 \text{certified banks}&\text{omit every repair label},\\
 \text{decoder only}&\text{reattach the side-coloured chronology}.
 \end{array}                                             \tag{14}
\]

The ordinary face `R` itself, its released component, and its carrier mark
are unchanged by relocation.  What remains a separate hypothesis is that
the repaired banks in (14) satisfy all recurrences in one common chart; a
collection of individually repaired ordinary unions is not automatically an
ordered strong tree.

## 4. A scalable fixed-circuit three-ear obstruction

Start in rational coordinates with

\[
 \begin{array}{lll}
 a=(0,0),&b=(6,0),&c=(0,6),\\
 d=(3,-10),&e=(13,3),&f=(-10,13).
 \end{array}                                             \tag{15}
\]

Put

\[
 R_0=\{a,b,c,d\},\quad R_1=\{a,b,c,e\},\quad
 R_2=\{a,b,c,f\}.                                      \tag{16}
\]

All three are convex quadrilaterals.  They are cyclic images under the
order-three affine map `(x,y) -> (6-x-y,x)`.

For arbitrary `q`, let

\[
 \epsilon={1\over100000q^2},\qquad
 z_t=(1+\epsilon t,\ 2+\epsilon t^2),\quad1\le t\le q. \tag{17}
\]

The `z_t` lie strictly inside `abc`, form a convex parabolic chain, and the
whole displayed configuration is in general position.  To see the last
claim uniformly in `q`, note first that the six outer points are in general
position and `(1,2)` lies on none of their pair lines.  An outer pair-line
evaluation at `z_t` is therefore a nonzero integer plus a perturbation of
absolute value less than one.  A line through `z_s,z_t` has integral slope
`s+t`; evaluating an integer outer point gives a nonzero integer equal, if
collinearity held, to the nonzero quantity `-epsilon*s*t` of absolute value
less than one.  Three parabolic points are never collinear.  For every `i,t`,

\[
             R_i\cup\{z_t\}\text{ is nonordinary through the same
             fixed circuit }\{a,b,c,z_t\}.              \tag{18}
\]

Every suffix of the completion chain is ordinary.  Hence the three records
with completion endpoint `{z_j,...,z_q}` and released endpoints `R_i` admit
a literal fixed-circuit chronology: delete `z_j`; both endpoints remain the
same ordinary faces, the released endpoint is untouched, and the original
pair is recovered by reattaching the labelled prefix.  If physical labels
are ordered `a,b,c,z_1,...,z_q,d,e,f`, then `abc z_j` is also the
lexicographically first bad four-set at level `j`: a competing circuit either
is `abc z_k` with `k>=j`, or has its third label after `c`; `abc` and each
released quadruple are ordinary.

Nevertheless,

\[
 \boxed{\quad\nexists x\in\mathbb R^2\text{ such that all three }
                    R_i\cup\{x\}\text{ are ordinary}.\quad}      \tag{19}
\]

For a convex quadrilateral with cyclic vertices `p_0,...,p_3`, a new point
can be added while retaining every old vertex iff it lies in one of the four
open ear cells.  The cell replacing edge `p_ip_{i+1}` is given by the three
strict linear inequalities

\[
 \chi(p_{i-1},p_i,x)>0,quad
 \chi(p_i,x,p_{i+1})>0,quad
 \chi(x,p_{i+1},p_{i+2})>0.                            \tag{20}
\]

There are `4^3=64` choices of one ear cell for each quadrilateral in (16).
Exact rational Fourier--Motzkin elimination makes every one infeasible.
For each of the three pairs of quadrilaterals, at least one of the `4^2`
cell intersections is feasible.  Thus (19) is a minimal three-ear, not a
pairwise, obstruction.

The verifier also applies the orientation-preserving shear

\[
                         (x,y)\mapsto(x+y/997,y),        \tag{21}
\]

under which all labels have distinct first coordinates.  Thus the entire
chronology and obstruction live in one explicit generic chart.

This family is scalable in chronology length and uses distinct physical
repair labels.  It disproves the promotion claim

> fixed actual `1+3` circuits plus literal deletion stability imply a
> simultaneous ear repair.

It does not disprove a quantitative cycle theorem with additional live
mass hypotheses.  The parabolic completion chain itself has `2^q` faces,
which is only `2^{O(L)}` for `q=O(L)`, and the three released contexts are
constant.  Indeed one may retain a pair (or one) of those contexts at only
constant loss, so this gadget does not defeat bounded-menu promotion.  A
theorem extracting the missing `n^{Theta(log log n)}` bank must use
cross-role mass/branching or physical circuit elimination beyond this local
fixed-circuit data.

### 4.1 Weighted fractional-Helly localization

There is nevertheless a sharp abstract dichotomy at one fixed physical
repair label.  Give its convex ear chambers their conditional record-mass
law `nu`, and put

\[
             h=\sup_x\nu\{C:x\in C\}.                         \tag{22}
\]

The weighted planar fractional Helly theorem (obtained from the finite
theorem by rational cloning and a limit) gives

\[
 \Pr_{C_1,C_2,C_3\sim\nu}
       [C_1\cap C_2\cap C_3\ne\varnothing]
       \le 1-(1-h)^3\le3h.                              \tag{23}
\]

Thus at each localized turn either:

* one position repairs at least an `eta` fraction of the record mass, costing
  at most `log(1/eta)` bits; or
* at least `1-3eta` of the weighted chamber triples have empty intersection.

Taking `eta=L^{-B}` over `q=O(L)` turns costs only `O(L log L)` in the first
branch.  Hence a survivor to bounded-menu repair contains a dense family of
literal, same-label two-/three-ear Helly witnesses.  Equation (23) is not a
face bank: mapping those triples to a cyclic/profile output while retaining
the released carrier and role history is exactly the missing planar step.

## 5. Exact remaining gate

The chronology-to-repair route is now reduced to one of two genuinely new
inputs.

1. **Bounded-menu promotion:** recover from each live turn an actual exposed
   edge menu with
   `sum_j log t_j=O(L log L)`, while preserving (14) and one chart.
2. **Branch-summing geometry:** when (6) forces quadratic selection/repair
   cost, turn the many incompatible two-/three-ear records into recoverable
   same-configuration cyclic/profile faces.  Abstract Helly obstruction is
   insufficient; the output must retain the released carrier/history and
   distinguish physical role branches.

No half-coefficient closure is claimed.
