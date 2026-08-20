# Single-fibre replacement wedges: nested transition switch and a planted barrier

## 1. Outcome

Consider the surviving single-fibre term

\[
 \mathcal R_L=
 \sum_q\sum_{\substack{s,s'\in H_q, s\ne s'\\
 E(s+q)\cap E(s'+q)\ne\varnothing}}
 W_{r(s,s'),L},
 \qquad
 r(s,s')=-{\delta(s)-\delta(s')\over18},                 \tag{1.1}
\]

with zero weight when the quotient is not integral.  This is the quantity
which appears, multiplied by `sqrt(k)`, in the replacement branch of the
weighted common-translation dichotomy.

There is a further exact switch.  Except for two explicitly enumerable
cross-endpoint degeneracies, every replacement pair `(s,s')` is itself one
clean source-to-target transition in the fibre

\[
 g=s'-s=y-x,                                               \tag{1.2}
\]

where `(x,y)` is the rigid replacement-centre pair.  Thus the nondegenerate
part of (1.1) is exactly a transition-gap weighted clean-incidence sum,
not an arbitrary pair-codegree sum.

This does not finish the term.  A genuine polynomial-height planted family
has

\[
 H=\Theta(k^2),\qquad
 \mathcal R_L=\Omega(k^4),                                \tag{1.3}
\]

with every counted target record determinant-qualified.  It saturates the
replacement first moment, the nested-fibre reduction, and the target-star
wedge count simultaneously.  Hence no bound `R_L<=m^(o(1))k^(4-epsilon)`
can hold from these decorations alone.

The construction does not refute the scale sufficient for #1208.  When
`H=Theta(k^2)`, that scale is

\[
 {N(H+k^3)\over\sqrt k}=\Theta(k^{9/2}),                  \tag{1.4}
\]

leaving a precise square-root gap.  Moreover, the elementary planted
pencils have codegree a fixed fraction below the `c(p)>=k` cutoff of the
current dichotomy.  Closing the actual high-codegree branch therefore
requires using the additional, nonreplacement common translations which
make `c(p)` large; the single-fibre star and nested transition alone do not
contain that information.

## 2. Exact nested-transition switch

Fix an ordered source pair `p=(s,s')` with replacement-pencil size
`rho(p)>0`.  Its rigid centres `(x,y)` are characterized by

\[
 E(s+q)=\{x,u_q\},\qquad
 E(s'+q)=\{y,u_q\},qquad y-x=s'-s                         \tag{2.1}
\]

for each pencil record `q`.  Put `g=y-x`.

Let `E(s)={c,d}` and `E(s')={e,f}`.  Equation (2.1) implies

\[
 s+y=s'+x.                                                \tag{2.2}
\]

If

\[
 y\notin E(s),\qquad x\notin E(s'),                       \tag{2.3}
\]

then the six points `y,x,c,d,e,f` are distinct: the two source edges are
disjoint by the fixed-fibre star-to-matching theorem, and (2.3) removes the
only remaining cross coincidences.  Consequently

\[
 \boxed{s\in H_g,qquad s+g=s'.}                          \tag{2.4}
\]

Define the extension multiplicity of such a transition by

\[
 e(g,s)=\#\{q:s,s+g\in H_q,
 E(s+q)=\{x,u\},E(s+g+q)=\{y,u\}	ext{ for some }u\},     \tag{2.5}
\]

where `(x,y)` is the unique ordered endpoint pair realizing `g`.
Uniqueness of directed point differences makes this definition
unambiguous, and `e(g,s)=rho(s,s+g)`.

Therefore the nondegenerate part of (1.1) has the exact form

\[
 \boxed{
 \mathcal R_L^{\rm nd}
 =\sum_{g}\sum_{\substack{s\in H_g\\s+g\in\Sigma}}
 e(g,s)
 W_{-(\delta(s)-\delta(s+g))/18,L}.}                     \tag{2.6}
\]

This preserves both translations: `g` is the nested clean translation and
the multiplicity (2.5) still counts every original `q`.

The two degenerate types are small in support, although their scalar weight
is not automatically small.  For the type `y in E(s)`, choose the ordered
centre pair `(x,y)` and the other endpoint `d` of `E(s)`.  These determine
`s=y+d`, then `s'=s+y-x`, and pair-sum uniqueness determines `E(s')` if it
exists.  Hence there are fewer than `k^3` such ordered pairs `p`.  The type
`x in E(s')` has the same bound.  Thus

\[
 \#\{p:\rho(p)>0\text{ and (2.3) fails}\}<2k^3.           \tag{2.7}
\]

Since `rho(p)<=k-2`, their unweighted replacement-record count is less
than `2k^4`.  A weighted proof must still control which scalar gaps these
records occupy.

## 3. An anchor-overlap restriction inside one pencil

Write the oriented anchor edge of record `i` as `(a_i,b_i)`, and its outer
endpoint as `u_i`.  From (2.1),

\[
 a_i-b_i=u_i+(x-s).                                       \tag{3.1}
\]

If two records have `a_i=a_j`, subtraction gives

\[
 b_j-b_i=u_i-u_j.                                        \tag{3.2}
\]

Distance-Sidonicity forces the unordered edges `{b_i,b_j}` and
`{u_i,u_j}` to coincide.  The direct identification
`b_i=u_i,b_j=u_j` violates cleanliness, so necessarily

\[
 b_i=u_j,qquad b_j=u_i.                                  \tag{3.3}
\]

In particular, no point is the first anchor endpoint of three pencil
records.  The symmetric statement holds for the second anchor endpoint.
Thus the directed anchor graph of a replacement pencil has outdegree and
indegree at most two.  This is stronger than arbitrary anchor reuse, but it
still permits linear pencils and supplies no polynomial saving beyond the
known `rho<=k-2` scale.

## 4. A planted common-source/star system

The following formal construction shows that (2.6) can be dense.  Choose
`h` source edge vectors `v_i`, free centres `P_i`, a free shift `R`, and put

\[
 C_i=P_i,\qquad D_i=P_i+v_i,\qquad
 s_i=C_i+D_i,qquad U_i=s_i-R.                            \tag{4.1}
\]

Choose `Q` free ordered anchor pairs `(A_j,B_j)`, set

\[
 q_j=A_j-B_j,qquad X_j=q_j+R.                            \tag{4.2}
\]

Then, for every `i,j`,

\[
 s_i+q_j=X_j+U_i.                                        \tag{4.3}
\]

After generic specialization, (4.3) is a clean row.  Thus all `Q` fibres
contain the same `h` source starts, and the target graph in fibre `q_j` is
the star

\[
 \{\{X_j,U_i\}:1\le i\le h\}.                            \tag{4.4}
\]

For every ordered pair `(s_i,s_l)`, all `Q` records are one replacement
pencil with centres `(U_i,U_l)`.  Moreover

\[
 U_l-U_i=s_l-s_i,                                        \tag{4.5}
\]

so `(s_i,s_l)` is exactly the nested clean transition in (2.4).  Therefore

\[
 \sum_p\rho(p)=Qh(h-1)=\Theta(kH)                        \tag{4.6}
\]

when `h,Q=Theta(k)`.  This makes the general first-moment bound sharp in
order of magnitude and shows that passing to the nested fibre does not by
itself reduce extension multiplicity.

The affine point forms in (4.1)--(4.2) have distinct unordered pair sums.
One quick verification is to compare their coefficients in the independent
variables `P_i,A_j,B_j,R`: the possible coefficients of each `P_i` are
`0,1,2`, and after those are fixed the anchor and `R` coefficients separate
all remaining types.  Hence two different formal edge vectors are never
equal up to sign.  All unintended squared-distance equalities are nonzero
quadratic polynomials in the free coordinates.

## 5. Installing one determinant-qualified scalar wedge

Take `h=2n`.  Fix an integer `C>0` and put

\[
 r=-4(C+1),\qquad K=36(C+1).                              \tag{5.1}
\]

For `1<=i<=n`, choose distinct small integers `t_i` and assign two source
edge vectors

\[
 v_i^+=(K-t_i,t_i+1),\qquad
 v_i^-=(K-t_i-1,t_i).                                    \tag{5.2}
\]

They obey

\[
 |v_i^+|^2-|v_i^-|^2=2K=-18r.                            \tag{5.3}
\]

Choose the `t_i` in a short interval so that all `2n` controlled norms are
different.

Independently introduce a point `Z` and `t` first target edges with vectors

\[
 a_j=(C,T_j),                                             \tag{5.4}
\]

all incident to `Z`.  Give each one a partner edge, at a free centre, with
vector

\[
 b_j=(C+2,T_j).                                           \tag{5.5}
\]

Then

\[
 |a_j|^2-|b_j|^2=r,qquad
 |2\det(a_j,b_j)|=4|T_j|.                                \tag{5.6}
\]

Take a polynomial-height Golomb ruler for the `T_j`, translate and scale it
so that all fixed internal distances are different, and make
`4|T_j|>N/h`.  The determinant-qualified first-edge graph is a `t`-edge
star, so

\[
 W_{r,N/h}={t\choose2}.                                   \tag{5.7}
\]

Every aligned pair `(v_i^+,v_i^-)` has replacement multiplicity `Q` in
(4.3).  Consequently the controlled part of (1.1) is

\[
 \boxed{
 \mathcal R_{N/h}
 \ge nQ{t\choose2}.}                                     \tag{5.8}
\]

Take `n,Q,t` proportional to a parameter `M`.  The construction uses
`O(M)` points, has controlled clean mass `2nQ=Theta(M^2)`, and (5.8) is
`Theta(M^4)`.  The fixed vectors have polynomial size.  After excluding
the finitely many controlled internal collisions, all remaining unwanted
distance equalities and pair-sum collisions are nonzero bounded-degree
polynomials in the free centres.  The grid nonvanishing lemma gives an
integral distance-Sidon specialization of polynomial height in which every
controlled row is six-distinct.  Extra clean rows, if present, only increase
the ambient clean mass.  This proves (1.3).

The example is deliberately honest about its limitation.  Its planted
common codegree is `Q=Theta(k)` but, in this direct realization, a fixed
constant below the total point count.  It therefore kills purely
single-fibre/nested-transition estimates below `k^4`, but it does not kill
an estimate using the extra hypothesis `c(p)>=k` quantitatively.

## 6. Exact finite certificate

The verifier constructs a deterministic 64-point specialization with six
common source starts, seven translations, three aligned replacement pairs,
and eight determinant-qualified target records.  It checks:

* all 2,016 unordered squared distances and pair sums are distinct;
* all 42 prescribed common-translation rows are clean;
* the 21 aligned records are full replacement pencils;
* every aligned pair is a clean nested transition;
* the target gap is `-4004`, every target determinant exceeds the adaptive
  cutoff, and its wedge weight is 28; and
* the controlled weighted replacement mass is `21*28=588`.

Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_single_fibre_replacement_transition_barrier.py
```

## 7. Remaining high-codegree gate

Equation (2.6) is the strongest exact replacement reformulation found in
this attack.  A sufficient theorem must use that the pairs entering the
actual dichotomy have

\[
 c(p)\ge k,qquad \rho(p)\ge {c(p)\over\sqrt k},           \tag{7.1}
\]

not merely that `rho(p)` extensions exist.  The planted theorem saturates
everything visible after deleting `c(p)-rho(p)`, so those nonreplacement
common translations are the only unused resource.

Equivalently, the missing estimate must couple three objects:

1. the nested transition `(g,s)` in (2.4);
2. its replacement extension set of size `rho(p)`; and
3. the at least `c(p)-rho(p)` further fibres containing both starts but not
   using the same retained target endpoint.

The target determinant cells and wedge weight alone do not see item 3.
This explains the remaining square-root gap and gives a concrete criterion
for the next inverse step.
