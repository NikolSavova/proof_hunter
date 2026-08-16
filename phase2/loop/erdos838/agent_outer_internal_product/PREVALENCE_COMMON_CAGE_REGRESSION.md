# Prevalence regression: a giant external component need not create repair entropy

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

The proposed prevalence step is false from the currently available data.
Disjoint outer traces need not yield many private cells, and the external
circuits which merge them need not yield many recoverable completion
profiles.  A scalable reinforced common cage has all of the following at
once:

* an actual canonical marked root `T` with role-pocket `X_T=X`;
* `2^r` weighted source contexts carrying that same root and pocket;
* any prescribed matching of `q` disjoint outer traces, with
  `q<=p` and `p` arbitrarily larger than `q`;
* one giant root-deleted external circuit component containing every pocket
  label and every surviving core shield label;
* singleton guard number exactly `p`;
* only two or three minimum completion profiles, shared by all labels of `X`.

Thus one may take `q=Theta(log n)` and `p=Theta(n)`.  No positive fraction of
the matched traces becomes a private/recoverably separable cell, while every
`q`-toggle is still far below the first possible completion size.  Even at
the minimum size `p`, the completion alphabet is constant rather than
exponential in `q`.

This is not a counterexample to EIC'.  It is an exact scalable regression to
the asserted structural dichotomy.  The missing hypothesis is a bound on
**external reinforcement/codegree**: outer matching alone records disjoint
witnesses, but does not control the many additional transversal circuits
which merge and reinforce them.

## 1. Reinforced common cage

Fix integers

\[
                         1\le q\le p,\qquad r,m\ge1.        \tag{1}
\]

Take three sufficiently short arcs `U,V,W` around the vertices of an
equilateral triangle on a circle.  Choose them so that an open disk `D` lies
strictly inside every transversal triangle

\[
             \operatorname{conv}\{u,v,w\},qquad
             u\in U,\ v\in V,\ w\in W.                     \tag{2}
\]

Put `p` core points on each arc, denoted

\[
 U_0=\{u_1,\ldots,u_p\},\quad
 V_0=\{v_1,\ldots,v_p\},\quad
 W_0=\{w_1,\ldots,w_p\}.                                  \tag{3}
\]

Put another `r` optional outer points in the interior of the `W` arc.  Let
`R` be the resulting convex outer set and `C=U_0 union V_0 union W_0`.  Choose
gap-facing endpoints `u_* in U_0` and `v_* in V_0`; they are adjacent in the
cyclic order of `R`.  With any `w_* in W_0`, put

                             T=\{u_*,v_*,w_*\}.              \tag{4}

Finally put an arbitrary `m`-point general-position child `X` inside `D`,
using a sufficiently small generic similarity.  Define the source family

\[
             \mathscr A=\{C\cup Y:Y\subseteq R\setminus C\}.
                                                               \tag{5}
\]

All `2^r` members of (5) are convex, and `T` is a canonical tangent triple in
each because `u_*v_*` remains an edge.  Every `x in X` lies inside `T`, while
every outer label together with `T` is a four-subset of the convex-position
set `R`.  Hence

\[
                             N(T)=X,\qquad X_T=X.             \tag{6}

This preserves the actual marked root, its role, its repair alphabet, and
its weighted canonical source occurrences.

## 2. Matching with complete reinforcement

Choose any `q` disjoint transversal triples

\[
                        S_i=\{u_i,v_i,w_i\},quad1\le i\le q.
                                                               \tag{7}
\]

They are disjoint outer traces.  But (2) gives much more than this matching:

\[
 \{u,v,w,x\}\text{ is a bad circuit for every }
 u\in U_0, v\in V_0, w\in W_0, x\in X.                  \tag{8}

Thus the circuit-incidence tensor is the complete `p by p by p by m`
rectangle.  The chosen matching is only a sparse diagonal of it.

Delete any one label of the root `T`.  For `p>=2`, every arc still has a
surviving core point.  Fixing one surviving point in two arcs and a child
label in (8) connects every point of the third arc into the same bad-circuit
co-occurrence component.  Varying the child label connects all of `X` as
well.  Therefore all surviving core labels and all pocket labels lie in one
root-deleted external component.

In particular, a private-cell profile of
`RECOVERABLE_COMPONENT_TOGGLE_BRANCH.md` can contain at most one nonempty
internal cell: any two proposed cells are joined through common outer
partners in (8).  Hence the `Omega(log n)` private-cell conclusion fails
maximally.

## 3. Exact singleton completion profile

Fix `x in X` and a source `A`.  If a guard `G subseteq A` has `|G|<p`, at
least one core point survives on each arc.  Their transversal triangle
contains `x`, so

\[
                         (A\setminus G)\cup\{x\}             \tag{9}
\]

is nonconvex.  Thus the singleton guard number is at least `p`.

Choose the three arcs sufficiently short that the union of the centre disk
`D` with any two complete arcs is in convex position whenever only one point
of `D` is selected.  This is an open condition and holds in the limiting
equilateral model.  Deleting all `p` points of `U_0` or all `p` points of
`V_0` therefore makes (9) convex.  Deleting all of `W_0` also works for the
source with no optional `W` labels.

Conversely, a size-`p` guard which does not exhaust a core arc leaves a point
on every arc and fails by (2).  If the source contains an optional `W` label,
deleting only `W_0` still leaves that third-arc point and also fails.  Hence
the minimum guards are exactly

\[
 \begin{cases}
 U_0,V_0,W_0,&A=C,\\
 U_0,V_0,&A\ne C.
 \end{cases}                                                \tag{10}
\]

They are independent of `x`.  Across the full repair alphabet, the number of
minimum singleton completion records per source is therefore only `3m` or
`2m`, not `3^q`, `m^q`, or `V(X)^q`.

If `q<p`, every guard obtained by choosing one vertex from each matched trace
has size `q` and fails immediately by (9).  If `q=p`, every nonconstant such
choice leaves one point on all three arcs, and only the three constant words
in (10) can work.  Thus matched-toggle entropy is absent at every scale.

## 4. Why the secondary bank still does not pay a fixed power

The guaranteed completion output associated with (10) is only

\[
                          C=(A\setminus G)\cup\{x\}.         \tag{11}
\]

It retains two labels of the marked root.  The standard source decoder
guesses the retained edge, the missing root label, and one of the constant
profiles in (10), for loss `O(nR^2)`.  The guaranteed local completion bank
has size at most `3m<=3n`.  Therefore its ratio to this decoder loss is at
most `O(1/R^2)`, not `n^epsilon`.

For a common root known in advance, (11) can of course be useful; the point
is that the marked-incidence theorem includes diffuse roots, and merging by
itself does not supply the extra root-recovery bits.  Larger pocket faces or
larger guards may create additional faces in particular realizations, but
they are not forced by the matching-plus-merger data.  The arbitrary-child
embedding in Section 1 prevents such a conclusion from being read off the
induced order type of `X`.

The exact remaining prevalence target must therefore use more than connected
versus disconnected external circuits.  Viable quantitative hypotheses
include bounded external codegree, many distinct minimum guard profiles, or
a geometric alternation which makes the missing root recoverable from the
completion itself.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_prevalence_common_cage.py
```

The exact rational checker uses `p=5`, `q=3`, `r=2`, and `m=4`.  It verifies
general position, all weighted canonical sources, `N(T)=X`, the complete
transversal circuit tensor, connectedness after deleting each root label,
failure of all `3^q` matched toggles, and exhaustive classification of every
minimum size-`p` singleton guard for every source and pocket label.

