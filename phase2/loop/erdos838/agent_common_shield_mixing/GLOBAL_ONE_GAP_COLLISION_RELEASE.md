# Global one-gap collisions: a weighted splice theorem and the connected-child barrier

**Date:** 2026-08-14.  All logarithms are base two and every convex-position
complex contains the empty face.

## Verdict

There is one more genuine fixed-power exit before the detached one-gap
overlap problem.  If a rank-`q` face `Q` has `D` one-point extensions, one
edge pocket contains `m>=D/q` extension labels.  Dominance in that pocket is
a two-dimensional poset.  A width at least `m^(2/3)` gives
`Omega(m^(4/3))` distinct two-label extensions of `Q`; these outputs retain
`Q` with load at most `binom(q+2,2)`.  Otherwise there is a nested chain of
at least `m^(1/3)` labels, whose ordinary face reservoir is superpolynomial
in `m`.  Consequently, if the width branch occurs for a positive fraction
of `M` sources, then

\[
 V(P)\ \ge\ {M\over 8\binom{q+2}{2}}
                 \left({D\over q}\right)^{4/3}.             \tag{1}
\]

For `q=O(log D)`, (1) is the desired free `DM` count times
`D^(1/3-o(1))`.  The strict residue is therefore exactly the chain/shield
branch already isolated by the radial one-gap theorem.

For that residue there is an exact global collision statement.  Release a
base `B_c` by deleting a transversal `G_(c,U)` of all bad-circuit traces
against a detached face `U`, and write `R_(c,U)=B_c-G_(c,U)`.  Then
`U union R_(c,U)` is an ordinary face.  For two occurrences of the same
`U`, either

\[
                U\cup R_(c,U)\cup R_(c',U)                 \tag{2}
\]

is one ordinary splice face, or a bad four-circuit meets both symmetric
differences `R_c-R_c'` and `R_c'-R_c`.  If a fixed positive share of the
same-`U` collision energy takes the first branch, a one-face Cauchy count
bounds the total incidence overlap sharply.  With unit occurrences, splice
load `L`, good fraction `theta`, and additive exceptional budget `beta N`,

\[
 {N\over V(P)}\le {a+\sqrt{a^2+8L/\theta}\over2},
 \qquad a=1+{2\beta\over\theta}.                            \tag{3}
\]

A completely explicit recoverability bound is

\[
 L\le 4^{h+2b}\,\mu^2
        \left(\sum_{i=0}^t\binom ni\right)^2,               \tag{4}
\]

where `|U|<=h`, `|B_c|<=b`, `|G_(c,U)|<=t`, and at most `mu`
histories have the same actual base.  Formula (3) also has a weighted
version below.

If (3) does not pay, the collision energy is carried by pairs with a
four-circuit crossing the two released base petals.  Combining these
witnesses with the circuit-component join identity localizes the failure to
one bad-circuit-connected child; independent children multiply exactly.

This last connected child cannot be discharged from the shared face and
the bases alone.  For **every** planar order type `X`, surround it by a
generic triangle `U`.  Every maximum-rank face of `X` is a valid base, all
distinct bases have detached-incompatible unions, the circuit graph is
connected through `U`, every base requires total deletion before it joins
`U`, and nevertheless

\[
                         V(X\cup U)\le 8V(X).               \tag{5}
\]

Thus a generic theorem for the connected child after the already-free
extension factor `D` has been spent would imply the corresponding
top-layer-versus-total-face theorem for arbitrary `X`: it is an E838-level
restatement.  The remaining proof must retain extra repair/history
structure of the extension labels through the descent.  The triangle
wrapper is a barrier to the proposed mixing interface, not an EIC'
counterexample, because it does not itself realize the full `D`-star
hypothesis.

## 1. The pocket width-or-shield theorem

Let `Q` be a convex `q`-set in general position and let `Y` be a set of `D`
points outside `Q` such that

\[
                         Q\cup\{y\}\in\mathcal F(P)
                         \quad(y\in Y).                    \tag{6}
\]

Every `y` lies in the open insertion cell of a unique edge of `Q`: the two
tangencies from `y` to `Q` must be adjacent, since no vertex of `Q` is lost
in (6).  Fix an edge `uv` whose cell contains a subset `Z` of size

\[
                               m\ge D/q.                    \tag{7}
\]

After mapping `u=(-1,0),v=(1,0)`, use the tangent coordinates

\[
 L(z)={1+x(z)\over-y(z)},\qquad
 R(z)={1-x(z)\over-y(z)}.                                  \tag{8}
\]

For labels in this cell define

\[
 z\prec z'\quad\Longleftrightarrow\quad
 L(z)>L(z'),\ R(z)>R(z').                                  \tag{9}
\]

Equivalently, `z` is strictly inside the triangle `uvz'`.

> **Lemma 1 (same-pocket pair test).**  For distinct `z,z' in Z`,
> \[
> Q\cup\{z,z'\}\notin\mathcal F(P)
> \quad\Longleftrightarrow\quad z,z'\text{ are comparable in (9)}.
>                                                                    \tag{10}
> \]

**Proof.**  The insertion cell is bounded by the continuations of the two
edges of `Q` adjacent to `uv`.  Hence adding any collection of points in the
cell cannot remove a vertex of `Q`; only a newly added point can fail to be
extreme.  Relative to one other label, the part of
`conv(Q union {z'})` outside `conv(Q)` is exactly the triangle `uvz'`.
Thus `z` is lost exactly when it lies in that triangle.  The tangent-ratio
calculation gives (9), and exchanging `z,z'` proves (10).  QED.

Let `a` and `w` be the height and width of this poset.  Dilworth gives
`aw>=m`.  If `a<m^(1/3)`, then `w>m^(2/3)`, and an antichain gives at least

\[
                  \binom w2\ge {1\over4}m^{4/3}            \tag{11}

two-label faces for all sufficiently large `m`.  If `a>=m^(1/3)`, a chain
of that length is a detached point set in `P`.  The universal planar face
reservoir

\[
       V(S)\ge 2^{(1/8-o(1))(\log |S|)^2}                  \tag{12}

is eventually larger than `m^A` for every fixed `A`; in particular it is
larger than `m^(4/3)`.  Notice that total nesting relative to `uv` does not
restrict the internal order type of the chain: the projective-universality
theorem in `DETACHED_RADIAL_LEXICOGRAPHIC_PROFILE.md` is exact here.

Now take `M` distinct uniform rank-`q` source faces.  If at least `M/2` of
them take the width branch, sum (11).  A fixed rank-`q+2` output has at most
`binom(q+2,2)` possible source faces, obtained by deleting the guessed two
extension labels.  This proves (1).  Hence only the shield branch requires
global work.

## 2. Circuit transversals release the base

Let `U` and `B` be disjoint ordinary faces.  Define the trace clutter

\[
 \mathcal T(U,B)=\{C\cap B:C\subseteq U\cup B,
            |C|=4,\ C\notin\mathcal F(P),\ C\cap B\ne\varnothing\}.
                                                                    \tag{13}
\]

> **Lemma 2 (exact release).**  If `G subseteq B` hits every member of
> `mathcal T(U,B)`, then
> \[
>                         U\cup(B-G)\in\mathcal F(P).       \tag{14}
> \]

**Proof.**  Otherwise planar Caratheodory supplies a bad four-set `C` in
the left side.  It is not contained in `U`, so `C cap B` is a nonempty
member of (13) disjoint from `G`, a contradiction.  QED.

This is the correct repair split: the whole base need not be kept.  It is
also sharp; Section 5 has examples in which `G=B` is forced.

## 3. Same-face collision and first cross-circuit

For every occurrence `(c,U)`, apply Lemma 2 and abbreviate
`R_c=B_c-G_(c,U)`.  Thus `U union R_c` is a face.

> **Lemma 3 (splice or cross-circuit).**  For two occurrences of the same
> `U`, either (2) is a face, or it contains a bad four-circuit `C` such that
> \[
> C\cap(R_c-R_{c'})\ne\varnothing,
> \qquad C\cap(R_{c'}-R_c)\ne\varnothing.                  \tag{15}
> \]

**Proof.**  Choose a bad four-circuit in (2).  It cannot be contained in
either face `U union R_c` or `U union R_c'`.  Therefore it has a point in
each of the two displayed differences.  QED.

Thus the first failure of a splice is already a named edge of the
bad-circuit graph on the released base petals.  If the support is partitioned
into containers, the component-join identity from
`agent_detached_pair_union/DETACHED_CIRCUIT_COMPONENT_FACTORING.md` says
that distinct circuit components multiply their full face complexes
exactly.  There is no overlap loss between them.  The only unpaid object is
one component connected by witnesses (15).

## 4. Weighted one-face collision inequality

The cleanest statement allows fractional weights.  Let `Omega` be the
occurrences and give occurrence `i` weight `w_i>=0`.  For a face `U`, put

\[
 s_U=\sum_{i:\,U_i=U}w_i,\qquad
 W=\sum_iw_i,\qquad \Delta=\sum_iw_i^2.                   \tag{16}
\]

There are at most `V=V(P)` distinct values of `U`, so Cauchy gives

\[
 {1\over2}\sum_U\left(s_U^2-
              \sum_{i:\,U_i=U}w_i^2\right)
       \ge {1\over2}\left({W^2\over V}-\Delta\right).     \tag{17}

Suppose the total weight `G` of splice-good unordered pairs satisfies

\[
 G\ge {\theta\over2}\left(\sum_Us_U^2-\Delta\right)-\beta W,
 \qquad 0<\theta\le1,                                     \tag{18}

and the total good-pair weight mapped to any one output (2) is at most `L`.
Then `G<=LV`.  If `Delta<=alpha W`, (17)--(18) give, for `x=W/V`,

\[
 x^2-\left(\alpha+{2\beta\over\theta}\right)x
       -{2L\over\theta}\le0.                             \tag{19}

Therefore

\[
 \boxed{\ {W\over V}\le
 {a+\sqrt{a^2+8L/\theta}\over2},\qquad
 a=\alpha+{2\beta\over\theta}.\ }                       \tag{20}

For unit occurrences, `alpha=1`, yielding (3).  With every collision good,
the factor is `(1+sqrt(1+8L))/2`.

Here is a crude but completely general combinatorial load.  Assume
`|U|<=h`, `|B_c|<=b`, guards have size at most `t`, and an actual base has
at most `mu` admissible histories.  From a fixed output `W_0` in (2), assign
each point one of the four membership states

\[
     U,\quad R_c-R_{c'},\quad R_{c'}-R_c,
                \quad R_c\cap R_{c'}.                     \tag{21}

There are at most `4^(h+2b)` assignments.  Guess the two guards in at most
`(sum_(i<=t) binom(n,i))^2` ways, and then the two histories in at most
`mu^2` ways.  This proves (4).  Any rooted gap, known support edge, or
canonical guard only improves this load.

If (18) fails for every useful `theta,beta`, most same-`U` collision energy
lies on the cross-circuit branch (15).  Independent-set thinning either
recovers many splice pairs, or the witness circuits link almost all of the
weight into one circuit-connected support child.  This is precisely the
child on which the component-factor theorem says one must use the extension
history rather than another detached product.

## 5. A scalable realizable barrier for the connected child

> **Theorem 4 (outer-triangle wrapper).**  Let `X` be any finite planar
> general-position set.  Choose a generic triangle
> `U={u_1,u_2,u_3}` whose interior contains `X`, and put `P=X union U`.
> Let `q` be the maximum rank of a face of `X` and let `mathcal B` be the
> rank-`q` layer.  Then:
>
> 1. `U` and every `B in mathcal B` are ordinary faces;
> 2. `U union B` is nonconvex for every nonempty `B`;
> 3. distinct `B,B' in mathcal B` have nonconvex detached union;
> 4. every circuit-transversal release of `U` against `B` deletes all of
>    `B`;
> 5. the circuit graph on the containers `U` and `X` is connected; and
> 6. `V(P)<=8V(X)`.

**Proof.**  Every `x in X` lies strictly inside the triangle `U`, so
`U union {x}` is a bad `3+1` circuit.  This proves (2), connects the two
containers, and puts the singleton trace `{x}` in (13).  Hence every
transversal contains every `x in B`, proving (4).  If distinct maximum-rank
faces had convex union, its rank would exceed `q`, proving (3).  Finally,
restriction sends a face `F of P` injectively to

\[
                         (F\cap X,F\cap U).                \tag{22}

The first coordinate is a face of `X` and the second has at most eight
values, proving (6).  QED.

The construction is rational and scalable: after an affine normalization
of rational `X`, choose any sufficiently large rational triangle off the
finitely many forbidden secant lines.  In the exact verifier, the five-point
set

\[
 X=\{(-4,-4),(4,-4),(4,4),(-4,4),(0,1)\}                  \tag{23}

has three maximum rank-four faces and `V(X)=29`.  The triangle

\[
 U=\{(-23,-19),(21,-17),(2,31)\}                           \tag{24}

contains `X` strictly, is jointly in general position with it, and the
eight-point wrapper has `V(P)=126<=232=8V(X)`.  All three bases require
four deletions.

Theorem 4 explains the precise limit of the global collision route.  A
shared detached face, pairwise detached-incompatible bases, a dense supply
of `3+1` or `2+2` witnesses, and even bad-circuit connectedness do not force
a new power.  Those hypotheses can wrap an arbitrary order type at constant
face cost.  What is not present in the wrapper is the live `D`-extension
alphabet.  The pocket theorem proves that this alphabet either pays before
localization or creates the shield incidences.  To close the remaining
case, one must show that the repair/source histories constrain the wrapped
base family more strongly than an arbitrary maximum layer; deleting that
history makes the desired conclusion circular.

## 6. Exact remaining atom

After the tagged width branch (1), circuit release, one-face collision
bound (20), and exact component factoring, the only unpaid atom has all of
the following properties:

1. a positive fraction of sources entered a large same-pocket nested-label
   shield rather than the tagged two-extension branch;
2. the same untagged one-gap faces have high weighted reuse across distinct
   source/common-base histories;
3. no `O(log D)` circuit-trace transversal releases enough of those bases;
   or, after release, almost every energetic pair fails the splice (2);
4. the first failed splices generate one bad-four-circuit-connected child;
5. the already-counted `DM` star faces retain exactly one extension factor
   `D`, but the second factor is invisible after forgetting the histories.

Theorem 4 shows that item 4 alone is irreducible.  A final theorem must use
item 1 or 5 quantitatively inside that connected child -- for example a
bounded-history tangent profile, an opposite pocket forced by the source
edge, or a circuit container in which the extension label remains a marked
vertex.  No theorem about the unrestricted face complex of the child can
avoid the outer-triangle reduction.

