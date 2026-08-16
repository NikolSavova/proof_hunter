# Global marked-pocket release: root entropy is only polynomial

**Date:** 2026-08-14.  All logarithms are base two and the empty convex
subset is counted.

## Verdict

The common-root versus diffuse-root split does not create a serious global
overlap.  If a source-attached circuit pocket can be released after deleting
at most `g` source vertices, then the output face, together with a guessed
root and guard, recovers the entire source record.  The exact multiplicity is

\[
 L_g={n\choose3}\sum_{i=0}^g{n\choose i}.                 \tag{1}
\]

Applied to the weighted high-root incidences from
`WEIGHTED_ROOT_STAR_MINIMIZER_OBSTRUCTION.md`, this proves the following
unconditional alternative.  Write

\[
 \alpha={n-2\mu\over2(n-3)},\qquad
 \mathscr I=\{(A,T):T\in\mathcal T(A),\ d(T)\ge D_0/2\}.
                                                               \tag{2}
\]

Then `|mathscr I|>=alpha V`.  Choose deterministically a largest one of the
four rooted-role classes in the circuit neighborhood of each marked triple
`T`, call it `X_T`, and put

\[
 H=\min_{T\text{ marked}}V(P|X_T).                           \tag{3}
\]

For an incidence `(A,T)`, let `tau(A,T)` be the minimum number of source
vertices meeting the outer trace of every bad split four-circuit between
`A` and `X_T`.  Then

\[
 \boxed{
 { |\{(A,T)\in\mathscr I:\tau(A,T)\le g\}|\over|\mathscr I|}
 \le {L_g\over\alpha H}.}                                   \tag{4}
\]

More strongly, if `b_g(A,T)` counts every pair `(G,F)` with
`G subseteq A`, `|G|<=g`, `F` a convex face of `X_T`, and
`(A setminus G) union F` convex, then

\[
 \boxed{\sum_{(A,T)\in\mathscr I}b_g(A,T)\le L_gV.}          \tag{5}
\]

Thus the weighted source multiplicity cannot disappear in a common root,
and diffuse roots cost only `3 log n` recovery bits.  The exact surviving
obstruction is geometric: for almost every weighted source, the cross-circuit
outer-trace hypergraph has large transversal number.

Conditionally on any universal reservoir estimate

\[
                  f(m)\ge2^{(c-o(1))(\log m)^2},             \tag{6}
\]

a low-mean minimizer with `mu<=(1-epsilon)log n` satisfies, for every fixed
`gamma<c`,

\[
 \tau(A,T)>\gamma\log n                                     \tag{7}
\]

for a `1-o(1)` fraction of its weighted incidences.  Consequently their
rank-three outer-trace hypergraphs contain matchings of size at least
`(gamma/3-o(1))log n`.  Taking the established `c=1/4` reservoir gives every
fixed `gamma<1/4`.

This does **not** close the half-coefficient theorem.  It removes the global
marked-overlap concern and identifies a new, exact local target: exploit
`Theta(log n)` disjoint source traces, while retaining the common repair
alphabet supplied by the pocket.

## 1. The marked pockets

For a triple `T`, let

\[
 N(T)=\{x\notin T:T\cup\{x\}\text{ is a bad four-circuit}\}.
                                                               \tag{8}
\]

Every bad four-circuit has a unique interior point.  Partition `N(T)` into
four classes according to which of the four labels is interior and choose a
largest class `X_T` using a fixed tie-breaking rule.  Hence

\[
 |X_T|\ge d(T)/4\ge D_0/8.                                  \tag{9}
\]

If `(A,T)` is a marked incidence, then

\[
                         A\cap X_T=\varnothing.              \tag{10}
\]

Indeed, if `x` belonged to `A`, the bad circuit `T union {x}` would be a
subset of the convex face `A`.

For `mu<=(1-epsilon)L` and
`R<=(1/2+o(1))L^2`, equation (9) gives

\[
 |X_T|\ge\left({1\over4(1-\epsilon)}-o(1)\right)
                    {n\over L^3}.                            \tag{11}
\]

Thus `log |X_T|=L-o(L)`, and (6) gives
`log H>=(c-o(1))L^2`.

## 2. Exact guard--circuit equivalence

Fix `(A,T)` and abbreviate `X=X_T`.  Define a hypergraph `K(A,T)` on vertex
set `A`.  For every bad four-circuit `Q subseteq A union X` which meets both
sides, insert its nonempty outer trace

\[
                              Q\cap A.                       \tag{12}
\]

Every edge has size one, two, or three.

> **Lemma 1 (exact release criterion).**  For `G subseteq A`, the following
> are equivalent:
>
> 1. `(A setminus G) union F` is convex for every convex face `F` of `X`;
> 2. `G` is a vertex cover of `K(A,T)`.

**Proof.**  If `G` misses the outer trace of a split circuit `Q`, put
`F=Q cap X`.  This has at most three points, hence is a convex face of `X`,
and the unreleased union contains the bad circuit `Q`.

Conversely, suppose a released union is nonconvex.  In planar general
position it contains a bad four-subset: choose a nonextreme point and a
Caratheodory triangle containing it.  The four-subset cannot lie entirely in
`A setminus G`, because `A` is convex, or entirely in `F`, because `F` is
convex.  It is therefore a split circuit whose outer trace avoids `G`, a
contradiction.  QED.

In particular, `tau(A,T)` is exactly the smallest guard which releases the
**entire unrestricted pocket face bank**, not merely a sufficient proxy.

## 3. Recoverable-cell theorem

> **Theorem 2 (global marked release).**  Equations (4)--(5) hold.

**Proof.**  For every record counted by `b_g(A,T)`, output the ordinary face

\[
                         C=(A\setminus G)\cup F.             \tag{13}
\]

Fix an output `C`.  Guess `T` and `G`; there are at most `L_g` choices.
The deterministic rooted class `X_T` is then known.  By (10),

\[
              F=C\cap X_T,\qquad A=(C\setminus F)\cup G.    \tag{14}
\]

So at most one source record corresponds to each guess `(T,G)`.  Every
ordinary face has multiplicity at most `L_g`, proving (5).

If `tau(A,T)<=g`, Lemma 1 supplies one guard which works for all `H` pocket
faces, so `b_g(A,T)>=H`.  Let `mathscr I_g` be this set of incidences.  Then

\[
       |\mathscr I_g|H\le L_gV,
       \qquad |\mathscr I|\ge\alpha V,                      \tag{15}
\]

and division proves (4).  QED.

This proof treats both proposed global branches uniformly:

* if many sources share one root, (14) recovers the source after the common
  root and guard are guessed;
* if roots are diffuse, enumerating all of them costs only `{n choose 3}`.

No factor involving `w(T)` is lost.

## 4. Quantitative minimizer corollary

Let `g=floor(gamma L)`.  The standard binomial estimate gives

\[
 \log L_g
 \le3L+g\log(en/g)+O(\log g)
 =(\gamma+o(1))L^2.                                        \tag{16}
\]

Since `mu=O(L)`, equation (2) has `alpha=1/2-o(1)`.  Equations (4),
(6), (11), and (16) show that the fraction of incidences with
`tau(A,T)<=g` is at most

\[
                         2^{-(c-\gamma-o(1))L^2}.            \tag{17}
\]

Finally, the endpoints of a maximal matching in a rank-three hypergraph form
a vertex cover.  Therefore `tau<=3 nu`, where `nu` is matching number, and
(7) implies the asserted disjoint-trace matching.

Equation (5) also gives a useful partial-release statement.  For every
`delta>0`, at least a `1-delta` fraction of marked incidences obey

\[
 b_g(A,T)\le {L_g\over\alpha\delta}.                         \tag{18}
\]

Thus, in the hard branch, even allowing the guard to vary with the pocket
face releases only `2^{(gamma+o(1))L^2}` marked pairs for almost every source,
against a pocket reservoir of `2^{(c-o(1))L^2}`.

## 5. Why common-root mass alone is insufficient

There is a scalable weighted version of the familiar triangle-pocket
obstruction.  Take a convex set `R`, choose adjacent vertices `u,v` and a
third vertex `w`, and put an arbitrary general-position set `X` strictly
inside the triangle `T={u,v,w}`.  In the full configuration `R union X`, all

\[
                         A=T\cup S,\qquad S\subseteq R\setminus T,
                                                               \tag{19}
\]

are convex source faces, `T in mathcal T(A)`, and every `x in X` is in the
same rooted role of the bad circuit `T union {x}`.  Hence

\[
                  w(T)\ge2^{|R|-3},\qquad d(T)\ge|X|.       \tag{20}
\]

Nevertheless no nonempty pocket face can be adjoined while retaining `T`,
because its points lie inside `conv(T)`.  Thus even exponentially many
canonical source attachments at one root do not themselves make a product.
Theorem 2 pinpoints what is additionally needed: a small cross-circuit
transversal which releases the root shield.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_global_marked_release.py
```

The checker recomputes the exact nine-point minimizer, its marked incidence
family, deterministic rooted pockets, all induced pocket faces, and every
guard of size at most two.  It verifies the guard--circuit equivalence record
by record, constructs all release-bank outputs, and audits both the decoder
and the multiplicity bound (1).

