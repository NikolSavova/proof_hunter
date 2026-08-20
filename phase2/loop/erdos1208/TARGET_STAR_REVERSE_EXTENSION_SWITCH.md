# Target-star reverse extension switch

## 1. Outcome

The two masses left by `HIGH_CODEGREE_REPLACEMENT_COMPLETION.md` admit a
common endpoint normal form.  For every realized directed difference

\[
 g=y-x,
\]

there are two canonical families of pair sums:

\[
 \begin{aligned}
 P_g&=\{x+z:z\in A\setminus\{x,y\}\},\\
 B_g&=\{w\in\Sigma:w+g\in\Sigma,
              E(w)\cap E(w+g)=\varnothing\}.
 \end{aligned}                                           \tag{1.1}
\]

The first family is the complete `(k-2)`-edge **star defect**: for
`v=x+z in P_g`,

\[
 E(v)=\{x,z\},\qquad E(v+g)=\{y,z\}.                    \tag{1.2}
\]

The second family splits as

\[
 \boxed{B_g=H_g\mathbin{\dot\cup}\partial B_g,
        \qquad |\partial B_g|\le2(k-2).}                 \tag{1.3}
\]

Thus a pair of edges whose sums differ by `g` is either the forced
meeting star `P_g`, a genuine clean transition `H_g`, or one of only
`2(k-2)` wrong-side boundary transitions.

Both residual weighted masses switch exactly into interactions between
these families.  No maximum fibre, scalar-gap maximum, or determinant
condition is discarded.  In particular, the formerly arbitrary mixed
two-fibre mass is now a star-to-clean reverse-extension mass plus a
linearly supported boundary mass.

This does not yet prove the required `m^(o(1)) N k^3` estimate.  The exact
remaining obstruction is the metric weight on the common backward
translation `q`: even after the target pair sums are pinned, the source
gap

\[
 \delta(v-q)-\delta(w-q)                                \tag{1.4}
\]

varies with `q`.  A successful final lemma must bound this reverse-extension
metric correlation.  The switch below is strictly more endpoint-rigid than
`D_rep+D_one`, and identifies precisely where that lemma has to act.

## 2. The three-way endpoint partition

Pair-sum injectivity and vector-Sidonicity imply the following.

**Lemma 2.1.**  If `E(v)` and `E(v+g)` meet, then `v in P_g`.  Conversely
every `v in P_g` has the form (1.2).  Hence `|P_g|=k-2`.

**Proof.**  Write the meeting edges as `{z,u}` and `{z,u'}`.  Their
pair-sum difference is `u'-u=g=y-x`.  Uniqueness of a nonzero directed
point difference gives `(u',u)=(y,x)`.  The converse is immediate.  QED.

Now take `w in B_g`.  Since the two edges are disjoint, `x` cannot belong
to `E(w)`: otherwise `E(w)={x,u}` and pair-sum uniqueness would give
`E(w+g)={y,u}`, a meeting pair.  Symmetrically `y` cannot belong to
`E(w+g)`.  Therefore the only ways the clean six-distinct condition for
`H_g` can fail are

\[
 y\in E(w)\quad\hbox{or}\quad x\in E(w+g).              \tag{2.1}
\]

There are at most `k-2` pair sums of the first kind and at most `k-2` of
the second kind.  This proves (1.3), including possible overlap between
the two boundary types.

## 3. Exact reverse target fibres

For a clean translation `q`, put

\[
 T_q=\{s+q:s\in H_q\}.                                  \tag{3.1}
\]

For an oriented pair `(q,q+g)` define its common reverse target fibre

\[
 X_{q,g}=T_q\cap(T_{q+g}-g)
 =\{u:u-q\in H_q\cap H_{q+g}\}.                         \tag{3.2}
\]

The second equality is literal: `u` is the target pair sum in the `q`
row, while `u+g` is the target pair sum in the `q+g` row.

Let `V(s,t)>=0` be any weight on ordered distinct source pair sums.  The
replacement mass has the exact form

\[
\boxed{
 D_{\rm rep}(V)=
 \sum_g\sum_{q}
 \sum_{\substack{b\in B_g:\ b,b+g\in H_q\\b+q\in P_g}}
 V(b,b+g).}                                             \tag{3.3}
\]

Indeed, if the two targets of `b,b+g in H_q` meet, their first pair sum
`b+q` lies in `P_g` by Lemma 2.1.  The fixed-fibre
star-to-matching theorem says the two source edges are disjoint, so
`b in B_g`.  Conversely these conditions give exactly one replacement
record.  Splitting `B_g` in (1.3) recovers the nested clean transition of
`SINGLE_FIBRE_REPLACEMENT_TRANSITION_BARRIER.md`, and makes its two
wrong-side degeneracies explicit.

For the one-role term, fix once and for all a total order on directed
translations and orient every unordered pair as `q<q+g`.  Then

\[
\boxed{
\begin{aligned}
 D_{\rm one}(V)
  =\sum_{q<q+g}
    \sum_{v\in X_{q,g}\cap P_g}
    \sum_{w\in X_{q,g}\cap B_g}
    \bigl(V(v-q,w-q)+V(w-q,v-q)\bigr).
\end{aligned}}                                         \tag{3.4}
\]

To prove (3.4), take a one-role record in the old switch.  If `s` is its
good start and `t` its bad start, put

\[
 v=s+q,\qquad w=t+q.                                    \tag{3.5}
\]

The good target edges `E(v),E(v+g)` meet, so `v in P_g`.  The bad target
edges are disjoint, so `w in B_g`.  The four original clean memberships
are exactly `v,w in X_(q,g)`.  Conversely (3.5) recovers `s,t` and all
four memberships, so the correspondence is bijective.  The two terms in
(3.4) retain both source orientations.

The switch also gives an unconditional unweighted budget.  Since an edge
of the complete graph on `A` meets at most `2(k-2)` ordered other edges,

\[
 D_{\rm rep}(1)\le2(k-2)H.                              \tag{3.5}
\]

For fixed `q,v,w`, membership `v in P_g` leaves at most `2(k-2)` choices
of `g`: choose which endpoint of `E(v)` is `x`, then choose `y`.  Dropping
the second reverse-fibre membership in (3.4) therefore gives

\[
 \boxed{D_{\rm one}(1)
 \le4(k-2)\sum_qh_q(h_q-1)
 \le4(k-2)(N-1)H.}                                     \tag{3.6}
\]

This is not the desired weighted estimate, but it verifies that the new
parameterization introduces no hidden multiplicity beyond the explicit
star choice.

## 4. Scalar specialization and exact remaining gate

Take

\[
 V(s,t)=W_{-(\delta(s)-\delta(t))/18,L},                 \tag{4.1}
\]

with zero weight unless the quotient is integral and the determinant-
qualified target wedge exists.  Equations (1.3), (3.3), and (3.4) split
the high-codegree residual into four endpoint-rigid pieces:

\[
 D_{\rm rep}^{\rm clean}+D_{\rm rep}^{\partial}
 +D_{\rm one}^{\rm clean}+D_{\rm one}^{\partial}.       \tag{4.2}
\]

In the replacement-clean piece, `b in H_g`; this is precisely the nested
transition, now also decorated by the target-star condition `b+q in P_g`.
In the one-role-clean piece, `v` is in the complete star `P_g`, `w` is in
the actual clean fibre `H_g`, and both are pulled backward through the
same two clean translations `q,q+g`.  In both boundary pieces the
nonclean side has support at most `2(k-2)` for each `g`.

Consequently a sufficient endpoint theorem is

\[
 \boxed{
 D_{\rm rep}^{\rm clean}+D_{\rm rep}^{\partial}
 +D_{\rm one}^{\rm clean}+D_{\rm one}^{\partial}
 \le m^{o(1)}Nk^3.}                                    \tag{4.3}
\]

Unlike a restatement in source-codegree notation, every summand in (4.3)
has one target member in `P_g`; the other is either in `H_g` or in a
linear-size, explicitly parameterized boundary.  The only uncompressed
quantity is the backward metric correlation (1.4), together with the four
clean memberships encoded by `X_(q,g)`.

## 5. Barrier to deleting the boundary or the backward translation

The boundary is genuine.  On the 19-point transformed-parabola stress,
the verifier finds 1,522 ordered one-role records.  Of these, 1,366 have
the clean lift `w in H_g`, while 156 lie in `partial B_g`.  Thus the
wrong-side terms cannot simply be declared impossible.

Nor may `q` be forgotten after fixing `(g,v,w)`: equation (1.4) contains
the squared distances of the two backward-shifted pair sums, not those of
`v,w`.  Global distance injectivity makes the label at each fixed source
sum unique, but gives no invariance under translating a pair sum.  Any
argument replacing (1.4) by `delta(v)-delta(w)` is invalid.

## 6. Verification

`verify_target_star_reverse_extension_switch.py` checks, on closure,
Costas, parabola, and ruler distance-Sidon families:

* the exact characterization and size of `P_g`;
* `B_g=H_g dotcup partial B_g` and the `2(k-2)` boundary bound;
* the local bijections (3.3) and (3.4), including every orientation;
* the equality between clean membership and absence of the two wrong-side
  endpoint collisions; and
* the unweighted budgets (3.5)--(3.6); and
* the nonzero boundary stress quoted above.
