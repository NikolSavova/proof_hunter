# Mass-uniform sibling roles: a diffuse ear bank or a fixed-edge circuit tensor

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The correction in
`agent_outer_internal_product/EFFECTIVE_BRANCHING_ROLE_FOREST.md` has an
exact geometric consequence, but it does not by itself close the live
rectangle.

Follow one low-`Q_eff` role-forest path.  At a deleted role `i`, let `b_i`
be the mass before splitting by its actual label, let `b_(i,z)` be the
label-class masses, and put

\[
 r_i={b_i\over\max_z b_{i,z}}.                         \tag{1}
\]

If `S_i={z:b_(i,z)>0}`, then the elementary inequality

\[
                         |S_i|\ge r_i                 \tag{2}
\]

turns effective mass branching into actual physical sibling labels.  On
the true low-`Q_eff` branch, all but `o(L)` deleted roles have

\[
                 r_i\ge {d_i\over L^K}.               \tag{3}
\]

Suppose a fixed chamber/carrier cell has a common stripped convex base `B`
such that `B union {z}` is an ordinary face for every sibling label
`z in S_i`.  Every sibling is then a singleton ear at a unique actual
boundary edge of `B`.  Choosing a heaviest insertion edge `g_i` leaves

\[
              |Y_i|\ge {r_i\over |B|}.                \tag{4}
\]

There is an exact dichotomy.  For every integer `t>=1`, either:

1. `t` roles have pairwise nonadjacent heavy insertion edges, and the
   ambient ordinary-face bank has size

   \[
        \boxed{\quad
        \left|\left\{B\cup\{z_i:i\in I\}:z_i\in Y_i\right\}\right|
                  =\prod_{i\in I}|Y_i|
                  \ge\prod_{i\in I}{r_i\over |B|};
        \quad}                                         \tag{5}
   \]

2. fewer than `3t` heavy boundary edges occur, and one fixed actual edge
   `g` carries at least `s/(3t)` rich role clouds `Y_i`, each satisfying
   (4).

If `d_i>=n^gamma`, `|B|=O(L)`, and `t=A log L`, the first branch has

\[
           \log |\mathcal B|
            \ge (gamma A-o(1))L\log L,                \tag{6}
\]

which is exactly an `n^{Theta(log log n)}` ambient bank.  No selected-word
codegree is used: missing selected double toggles are manufactured by
planar commutation of nonadjacent ears.

The second branch is also sharply classified at the first pair of rich
role clouds.  For `i != j` on the same edge, either many pairs `(x,y)` make
`B union {x,y}` ordinary, giving a decoded two-label bank, or a fixed pair
`{u,v} subset B` supports a dense labelled `2+2` circuit box

\[
                        \{u,v,x,y\}.                   \tag{7}
\]

The circuit orientation may be `1+3`; “`2+2`” in (7) refers to the two
sibling and two base labels.  This is precisely the concentrated
common-edge carrier handed to the shield/fan analysis.

There are two indispensable scope qualifications.

* The base in (5) must retain the actual chamber/carrier/context mark, or
  its cross-cell output load must be charged explicitly.  A source-only
  common base can be reused by arbitrarily many released contexts.
* The original `1/n` minimizer weight floor eliminates a quadratically tiny
  weighted-prefix leaf, but supplies no extra factor in a complete
  `M_D by H` rectangle.  Per released column it merely recovers the usual
  redundancy ratio `P_0/M_D`.  Thus it kills the weighted prefix-star
  artefact, not the low-redundancy complete-product survivor.

Accordingly, (5)--(7) close the **diffuse stripped-core** branch.  The exact
remaining alternatives are: a fixed-edge mass-uniform circuit tensor, or a
large cross-context load because the stripped base omits the released
carrier.  No minimizer-decreasing mutation is proved here.

## 1. Effective branching really gives physical siblings

At a forest node, the nonempty label classes partition mass `b_i`.  Since
each class has mass at most `b_i^*=max_z b_(i,z)`,

\[
                 b_i=\sum_{z\in S_i}b_{i,z}
                      \le |S_i|b_i^*.
\]

This proves (2).  Notice that no lower cutoff on the individual record
weights is needed.

The low-`Q_eff` factorization is

\[
 Q_{\rm eff}=\prod_{i\ {\rm undeleted}}d_i
        \prod_{i\ {\rm deleted}}{d_i\over r_i}.       \tag{8}
\]

If `Q_eff<2^{O(L log L)}` and `s=Theta(L)`, Markov applied to
`sum log(d_i/r_i)` gives (3) outside `o(L)` exceptional roles.  This is the
mass-uniform strengthening which the unit-weight prefix-star fails.

Now impose the geometric stripped-core hypothesis.  The role grounds are
disjoint, the non-role part `B` is fixed in the chamber cell, and for every
`z in S_i` some ordinary source endpoint contains `B union {z}`.  Heredity
therefore makes `B union {z}` ordinary.  If `B` has at least three points,
`z` has a unique insertion edge in the cyclic boundary of `B`; call it
`g(z)`.  Partition `S_i` by `g(z)` and choose a largest class `Y_i`, proving
(4).

This hypothesis is weaker than complete-product promotion.  It asks only
for a fixed stripped source base in one already localized chamber cell.
It is nevertheless not automatic if stripping the roles also erases the
released carrier or if different forest siblings have different non-role
source traces.  Those failures belong in the load parameter of Section 4.

## 2. Diffuse insertion edges give the missing-scale bank

The following standard planar fact is the whole geometric input.

> **Independent-ear lemma.**  Let `B` be a strictly convex polygon.  If
> `z_1,...,z_t` are singleton ears on pairwise nonadjacent boundary edges,
> then `B union {z_1,...,z_t}` is strictly convex.

One proof uses the supporting-halfplane arrangement.  An ear on edge `e`
lies outside the supporting halfplane of `e` and inside every other old
supporting halfplane.  Its two new supporting edges cut only the angular
ear cell at `e`.  The ear cells of nonincident edges lie strictly inside
both new halfplanes, so simultaneous stellar subdivisions of the selected
edges commute.

Let `G={g_i}` be the set of distinct selected heavy edges.  Any set of `R`
vertices in a cycle contains an independent set of size at least `R/3`.
Therefore, if `|G|>=3t`, choose one role on each of `t` pairwise
nonadjacent edges.  The independent-ear lemma makes every Cartesian choice
in (5) ordinary.  Disjoint physical role grounds make the map from choices
to output faces injective, proving (5).

If `|G|<3t`, pigeonhole gives one edge carrying at least `s/(3t)` roles.
This proves the second branch.  The loss in (4) is only `log |B|=O(log L)`
bits per selected role.  With (3), `d_i>=n^gamma`, and `t=A log L`,

\[
 \sum_{i\in I}\log {|Y_i|}
 \ge t\bigl(gamma L-O(log L)\bigr)
 =gamma A L\log L-O((\log L)^2),                      \tag{9}
\]

which is (6).

The theorem also has a word-dependent version.  If a positive-mass set of
words uses fewer than `3t` actual insertion edges, fixing that edge set
costs at most

\[
             \sum_{j<3t}{|B|\choose j}
              \le 2^{O(t\log L)}.                     \tag{10}
\]

For `t=Theta(log L)`, this is `2^{O((log L)^2)}`, negligible compared with
the `2^{Theta(L log L)}` target.  Thus adaptive edge sets do not hide a
quasipolynomial amount of mass.  What remains after (10) is still a
bounded-arc/common-edge carrier, not a diffuse chamber forest.

## 3. The first concentrated pair: ambient codegree or a rooted circuit box

Fix two rich role clouds `Y_i,Y_j` whose heavy insertion edge is the same
actual edge `g` of `B`.  Put

\[
 K_{ij}=\{(x,y)\in Y_i\times Y_j:
                       B\cup\{x,y\}\text{ is ordinary}\}.       \tag{11}
\]

If `|K_ij|>=theta|Y_i||Y_j|`, the faces `B union {x,y}` are all distinct
and give the exact ambient bank

\[
                      |\mathcal B_{ij}|=|K_{ij}|
                         \ge theta|Y_i||Y_j|.           \tag{12}
\]

This test must be made in the ambient order type.  Zero selected-word
codegree does not imply zero geometric codegree: an unselected double
toggle may still be the face in (12).

For every incompatible pair, `B union {x}` and `B union {y}` are ordinary
but `B union {x,y}` is not.  Planar Caratheodory gives a bad four-subset.
It must contain both `x` and `y`, because deleting either leaves an
ordinary set.  Hence it is

\[
                            \{u,v,x,y\}
\]

for two labels `u,v in B`.  Choose one circuit canonically.  Among the at
most `{|B| choose 2}` base pairs, one fixed pair supports at least

\[
 { (1-theta)|Y_i||Y_j|\over {|B|\choose2}}            \tag{13}
\]

incompatible sibling pairs.  Equations (4), (3), and (13) show that this
is a polynomial-density physical circuit box, with only `O(log L)` root
localization bits.  It retains the fixed boundary edge, chamber cell, role
pair, and base-root signature.

Pair compatibility is not promoted to a many-label rooted face theorem.
The known six-point rooted gadget has all relevant singleton/pair
insertions but a bad three-label union.  Thus (12)--(13), rather than a
false pairwise-to-global clique inference, is the exact first-pair endpoint.

## 4. Global decoder/load statement

For a collection of chamber cells `c`, let `\mathcal B_c` be the bank from
(5) or (12), and give the cell a nonnegative bookkeeping weight `a_c`.
Define the literal output load

\[
 \Lambda_{\rm ear}=\max_{W\in\mathcal F(P)}
          \sum_{c:\,W\in\mathcal B_c}a_c.             \tag{14}
\]

Grouping the actual ordinary outputs gives the exact inequality

\[
              \boxed{\qquad
                \sum_c a_c|\mathcal B_c|
                     \le \Lambda_{\rm ear} V(P).
              \qquad}                                 \tag{15}
\]

If the output retains a recoverable carrier/context mark inside `B_c`,
then (14) is only the already certified description multiplicity.  If it
does not, (14) can be arbitrarily large.  There is no hidden assertion that
a source-only ear bank multiplies every released context.

An exact planar collision illustrates the point at the full diffuse scale.
Take a convex `2t`-gon `B`, put rich ear clouds on `t` pairwise
nonadjacent edges, and take `H` generic points `u_h` in the interior of
`B`.  Every Cartesian ear choice is an ordinary face by Section 2 and is
independent of `h`, whereas adjoining any `u_h` makes it nonordinary
because `u_h` remains inside `conv(B)`.  Thus every output in the entire
diffuse bank is reused by all `H` released contexts.  This is an
interface/load barrier, not a low-face construction: the convex ear and
interior-point banks can themselves pay in larger compositions.

## 5. Exact weight-floor audit

The original minimizer mark has weight

\[
        \omega(A,T)={1\over n}
        |\{p:T_A(p)=T\text{ and }p\text{ is heavy}\}|,           \tag{16}
\]

so every nonzero mark is at least `1/n`.  Deterministic restriction,
copying it over released faces, induced dense-core pruning, chamber
localization, and the role forest do not split a record and preserve this
floor.  Fractional Hall allocation, Gibbs/radial `q/G` weights, and a
descendant dyadic replacement `beta<<omega` do not preserve it.

For any unsplit forest terminal, the pathwise Kraft bound is

\[
                  \mu(O)C_{\rm eff}(O)\le M.          \tag{17}
\]

Together with `mu(O)>=1/n`, it rules out a terminal for which
`C_eff>nM`.  This is useful only after the root mass has been normalized to
one genuine source fibre.

It gives no missing-scale multiplier in the complete rectangle.  If one
released column has `M_D` completion sources, each of atom weight `1/n`,
then

\[
                  M_U={M_D\over n},\qquad
                  C_{\rm eff}\le {M_U\over1/n}=M_D,
                  \qquad Q_{\rm eff}\ge {P_0\over M_D}. \tag{18}
\]

Thus the floor recovers exactly the ordinary completion redundancy and
nothing more.  When `M_D` is comparable with `P_0`, (18) is constant.  In an
`M_D by H` rectangle the terminal released bank has only `H` outputs, and
the forest inequality reduces, up to the certified pair load, to that
already-known `H` bank.  There is no extra `n^{Theta(log log n)}` factor.

This is why the correct surviving theorem is (5)--(15), with the
carrier/context load visible, rather than a claimed floor closure.

## 6. Verification

Run

```text
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_mass_uniform_sibling_ear_gate.py
```

The verifier uses exact rational orientation arithmetic.  It checks
independent-ear commutation on a rational convex octagon, exhausts the
cycle independent-set/product inequality, verifies (2), (4), (5), and the
fixed-root circuit pigeonhole on finite weighted systems, checks the
complete-rectangle cancellation (18), and constructs the general-position
interior-context collision from Section 4.
