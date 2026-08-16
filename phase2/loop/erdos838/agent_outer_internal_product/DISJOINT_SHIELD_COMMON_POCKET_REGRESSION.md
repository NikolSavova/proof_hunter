# Disjoint outer shields can reuse one common repair alphabet

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

A matching of disjoint outer traces, even attached to exponentially many
canonical source faces and to the actual rooted pocket `X_T`, does **not**
force independent internal face banks.  There is a scalable planar family in
which every one of `q` disjoint shields forms a bad circuit with every label
of the same `m`-point pocket.  All shield rows in the circuit-incidence matrix
are identical.

More precisely, for every positive `q,r,m` there is a planar general-position
configuration `P`, a convex `m`-point pocket `X`, a root triple `T`, a family
`mathscr A` of `2^r` convex source faces, and pairwise disjoint triples
`S_1,...,S_q` such that:

1. `T in mathcal T(A)` for every `A in mathscr A`;
2. the entire circuit neighborhood of `T` is `X`, in the single role where
   `x` is interior to `T`, so the deterministic role-pocket is exactly
   `X_T=X` and `d(T)=m`;
3. for every `i` and `x in X`, `S_i union {x}` is a bad circuit with `x`
   interior;
4. every `S_i` is an outer trace in every source, and the `S_i` form a
   matching of size `q`;
5. no guard of size less than `q` releases even one fixed singleton `{x_0}`
   from any source;
6. retaining the marked root `T` prevents adjoining every nonempty pocket
   face;
7. among the `3^q` natural guards which delete one vertex from each matched
   shield, every nonconstant choice still fails against `{x_0}`.  Only the
   three choices which delete an entire arc can even be candidates.

Thus one may take `q=Theta(log n)` and `m=Theta(n)` while retaining `2^r`
source attachments.  The exact matched-shield residual from
`GLOBAL_MARKED_POCKET_RELEASE.md` is realizable at arbitrary scale.

There is also an exact collision calculation.  Since `X` is convex, its
unrestricted face bank is `2^X`.  If two shields independently select
`F_1,F_2 subseteq X` and the construction only records their internal union,
then

\[
 (F_1,F_2)\longmapsto F_1\cup F_2                         \tag{1}
\]

has `4^m` input records but only `2^m` outputs.  The fibre over `U` has size

\[
                              3^{|U|},                      \tag{2}
\]

because each label of `U` may belong to the first face, the second, or both.
For `q` independently selected faces, the fibre over `U` is
`(2^q-1)^|U|`.  Hence the apparent `H^q` product, where `H=2^m`, can collapse
back to the single bank `H`.

This is not a counterexample to global EIC'.  It kills the stronger claim
that a disjoint matching of outer circuit traces automatically yields a
two-shield or multi-shield ordinary-face product.  A successful theorem must
extract **internal diversity**--for example disjoint or recoverably marked
subpockets--rather than outer-trace disjointness alone.

## 1. Construction

Start with three tiny, pairwise separated arcs `U,V,W` of a circle, centered
near the three vertices of an equilateral triangle.  Choose the arcs so small
that there is an open disk `D` contained in every transversal triangle

\[
                          \operatorname{conv}\{u,v,w\},
 \qquad u\in U, v\in V, w\in W.                           \tag{3}
\]

Choose `q` core points on each arc:

\[
 U_0=\{u_1,\ldots,u_q\},\quad
 V_0=\{v_1,\ldots,v_q\},\quad
 W_0=\{w_1,\ldots,w_q\}.                                  \tag{4}
\]

Choose another `r` optional points on the interior of the `W` arc.  All
these outer points form a convex set `R`.  Choose the endpoint `u_1` of the
`U` arc and the endpoint `v_1` of the `V` arc facing the empty gap between
the arcs.  They are adjacent in the cyclic order of `R`.  Relabel one core
point of `W` so that

                            T=\{u_1,v_1,w_1\}.               \tag{5}

Finally choose `m` points `X` in convex position inside `D`, avoiding the
finitely many forbidden lines.  The whole configuration is in general
position.  Put

 C=U_0\cup V_0\cup W_0,qquad
 \mathscr A=\{C\cup Y:Y\subseteq R\setminus C\}.            \tag{6}

Every member of `mathscr A` is a subset of the convex outer set, hence is a
convex face.  There are exactly `2^r` of them.  The pair `u_1v_1` remains an
edge of every source, so (5) belongs to the canonical tangent-triple family
of every source.

## 2. Root and shield audit

Every `x in X` lies strictly inside `T`, so `T union {x}` is a bad circuit in
the same rooted role.  On the other hand, for every outer label `y notin T`,
the four labels `T union {y}` are a subset of the convex-position set `R`
and are therefore convex.  Consequently

\[
                         N(T)=X,\qquad X_T=X.                \tag{7}
\]

Define

                         S_i=\{u_i,v_i,w_i\}.                \tag{8}

The triples in (8) are pairwise disjoint.  Equation (3) says that every
`x in X` is interior to every `S_i`, proving the complete `q by m` circuit
rectangle

\[
                 \{(S_i,x):1\le i\le q,\ x\in X\}.         \tag{9}
\]

In particular, all `q` disjoint outer traces can use the same fixed label
`x_0`, or the same full repair alphabet `X`.

Fix a source `A` and a guard `G subseteq A` with `|G|<q`.  It cannot delete
all `q` core points in any of the three arcs.  Choose surviving
`u in U_0`, `v in V_0`, and `w in W_0`.  Their triangle contains `D`, hence
contains `x_0`.  Therefore

\[
                         (A\setminus G)\cup\{x_0\}          \tag{10}
\]

is nonconvex.  This proves the guard lower bound `tau(A,T)>=q`; equivalently,
the matching obstruction survives even when the guard may vary arbitrarily
across the source.

There are `3^q` natural matching-transversal guards obtained by deleting one
of `u_i,v_i,w_i` for each `i`.  Unless all choices are `u_i`, all choices are
`v_i`, or all choices are `w_i`, at least one core point survives on each of
the three arcs.  The same argument proves that the released union with
`{x_0}` is still nonconvex.  Thus the nominal `3^q` toggle alphabet collapses
to at most three candidates before any larger pocket face is considered.

Finally, if a nonempty `F subseteq X` is adjoined while retaining `T`, any
`x in F` remains inside `T`, so `T union {x}` witnesses nonconvexity.  Thus
the canonical source attachment and the full pocket reservoir coexist, but
they have no root-retaining mixed product.

## 3. Exact lesson for a toggle theorem

The circuit rectangle (9) has maximal outer matching and zero internal
matching: every outer trace sees the same label set.  A theorem based only on

* `q` disjoint outer traces,
* a common rooted alphabet of size `m`, and
* the unrestricted face count `H=V(X)`

cannot infer two independent copies of `H`.  The union collision (2) is not
a loose counting artefact; it is realized by a convex pocket, where every
subset is genuinely an ordinary face.

The next viable target must add one of the following hypotheses:

1. a matching or entropy condition on the **internal traces** of the split
   circuits;
2. shield-specific subpockets recoverable from the output face;
3. a geometric alternation condition forcing different shields to expose
   different arcs of the pocket hull.

Without such a condition, outer toggles merely encode different ways of
deleting the same cage around one internal face bank.

## 4. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_disjoint_shield_regression.py
```

The checker constructs an exact rational instance with `q=4`, `r=3`, and
`m=5`.  It verifies general position, convexity of all outer points, the eight
canonical source contexts, `N(T)=X`, all twenty shield--label circuits, the
four disjoint traces, failure of every guard smaller than four against a
fixed pocket label, failure of every nonconstant matched-toggle guard, failure
of all root-retaining mixed faces, and the exact two-bank collision histogram
(2).
