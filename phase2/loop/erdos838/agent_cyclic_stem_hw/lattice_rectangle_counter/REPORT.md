# Comparable rectangles do not imply lattice product expansion

**Date:** 2026-08-14  
**Verdict:** two natural post--Theorem 23 product inferences are false, even
for exact rational planar point sets.  The fixed-directed-chord theorem is
not affected: when the two varying factors lie on opposite sides of one
fixed chord, cross-union is an injection and gives the full product of
ordinary convex faces.  What fails is the attempt to obtain that conclusion
from closure comparability, dense `C_4` support, or near-product entropy
alone, without retaining the chord/tangent signature.

No counterexample to ACP, Theorem 23, or the fixed-chord rectangle theorem is
claimed here.

## 1. Exact conjectures tested

Let `P` be a finite general-position planar point set and

\[
 \mathcal C(P)=\{P\cap\operatorname{conv}(S):S\subseteq P\}
\]

be its closure lattice.  Include the empty hull.  For
`K in mathcal C(P)`, write

\[
 D(K)=|\{L\in\mathcal C(P):L\subseteq K\}|,
 \qquad
 U(K)=|\{T\in\mathcal C(P):K\subseteq T\}|.
\]

The first tempting conjecture was the constant-one lattice rectangle bound

\[
 \boxed{D(K)U(K)\le |\mathcal C(P)|.}\tag{LR}
\]

This is exactly a comparable-rectangle-to-intermediate-hulls statement.
Every pair `(L,T)` in `down K times up K` is comparable.  Moreover every
closed hull `C` is intermediate for at least one such pair: take

\[
 L=C\cap K,\qquad T=\operatorname{cl}(C\cup K).
\]

Thus the union of all relevant intervals is the entire lattice, and `(LR)`
is necessary for an injective assignment of one distinct intermediate hull
to every comparable pair.  In general position, closure gives a bijection
between ordinary convex subsets and closed hulls: a convex subset maps to
its hull closure, and a closed hull maps back to its unique extreme-point
basis.  Hence the same counts apply to hulls and ordinary convex faces.

The second conjecture is the ACP-localized strengthening suggested by the
near-equality case of Theorem 23:

> **Localized product conjecture `(LTP)`.**  If a repair support graph
> `G subseteq T times I` is a full rectangle and satisfies Theorem 23 with
> `epsilon=0`, then there are at least `|G|` distinct intermediate closed
> hulls or convex faces retaining the common rooted core/tangent state.

This also fails.  The counterexample in Section 4 has exact independence,
support probability one, and weighted `C_4` probability one.

The positive control, which survives all tests, is deliberately stronger in
its geometry:

> **Fixed-chord control.**  Fix a directed chord `uv`.  If every lower
> factor is a rooted convex chain in one open half-plane, every upper factor
> is a rooted convex chain in the other, and the endpoint tangent ranks are
> dominance-compatible, then every cross-union is a distinct convex face.

The two open half-planes recover the two factors, so this last assertion is
an actual injection.  None of the counterexamples below has the two varying
factors on opposite sides of a common directed chord.

## 2. Minimal planar failure and fixed-`x` census

Take

\[
 a=(0,0),\quad b=(1,4),\quad p=(2,1),\quad c=(4,0).
\]

The point `p` lies strictly inside `abc`.  Every subset is closed except
`{a,b,c}`, whose closure also contains `p`.  Therefore

\[
 |\mathcal C(P)|=15.
\]

For `K={p}`, `D(K)=2`, while all eight subsets containing `p` are closed, so

\[
                  D(K)U(K)=2\cdot8=16>15.\tag{1}
\]

This is minimal: a general-position set of at most three points has Boolean
closure lattice, where `(LR)` holds with equality.

The verifier also enumerates the concrete stretchable fixed-`x` class

\[
                 P_\pi=\{(i,\pi(i)):0\le i<n\}
\]

for every permutation `pi`, discards collinear instances, and deduplicates
by the full labeled chirotope.  This is a census of this realized subclass,
not a claim to enumerate every planar order type.

| `n` | distinct labeled chirotopes | violating `(LR)` | worst `|C|/(DU)` |
|---:|---:|---:|---:|
| 3 | 2 | 0 | `1` |
| 4 | 8 | 4 | `15/16` |
| 5 | 28 | 22 | `29/32` |
| 6 | 144 | 134 | `25/32` |
| 7 | 684 | 662 | `41/64` |

Thus failure is not a rare nonstretchable or coordinate-degeneracy effect.

## 3. Exponentially strong planar pocket family

There is a scalable two-layer pocket obstruction.  Put `2k` points `O` near
a regular `2k`-gon and `k` points `I` in convex position in a sufficiently
small disk around its centre.  Choose all coordinates by a generic rational
perturbation and apply a rational affine shear, so the point set is in
general position with distinct `x`-coordinates.  Let `K=I`.

Every subset of `I` is closed and every superset of `I` is closed.  Hence

\[
                D(K)=2^k,\qquad U(K)=2^{2k},
                \qquad D(K)U(K)=2^{3k}.             \tag{2}
\]

This product is exponentially larger than the closure lattice.  To see it,
choose the inner disk after the outer polygon.  Every outer subset whose
hull contains the origin in its interior then contains the entire inner
disk.  A subset which does not do so is contained in a closed semicircle.
For a regular `2k`-gon, at most `k+1` vertices lie in such a semicircle, so
the number of exceptional outer subsets is at most
`(2k)2^(k+1)`.  A nonexceptional outer subset permits only the full inner set
in a closed hull; an exceptional one permits at most `2^k` inner choices.
Consequently

\[
 |\mathcal C(P)|
 \le 2^{2k}+(2k)2^{k+1}2^k
 =(1+4k)4^k,                                      \tag{3}
\]

and therefore

\[
 { |\mathcal C(P)|\over D(K)U(K)}
 \le (1+4k)2^{-k}.                                \tag{4}
\]

All properties used here are open, so the rational generic perturbation
preserves them.  The certificate contains explicit integral realizations
for `k=3,4,5,6`.  Before the final affine shear, the outer coordinates have
scale about `10^4` and the inner coordinates have scale about `10^2`; the
shear `(x,y)->(100000x+y,y)` makes every `x` distinct and preserves every
orientation sign.

| inner `k` | outer `2k` | exact hull/face count | rectangle pairs `2^(3k)` | ratio |
|---:|---:|---:|---:|---:|
| 3 | 6 | 230 | 512 | `115/256` |
| 4 | 8 | 871 | 4,096 | `871/4096` |
| 5 | 10 | 2,990 | 32,768 | `1495/16384` |
| 6 | 12 | 9,841 | 262,144 | `9841/262144` |

The verifier enumerates all subsets, computes closure by exact planar
Caratheodory witnesses, independently tests convexity of every subset, and
gets the same count from both descriptions.

## 4. Exact Theorem-23 equality inside one nested ear cell

The preceding family kills the unrestricted lattice inequality.  The next
one directly targets the entropy-near-product residual.

Fix an integer `a>=2`, put

\[
 q=a+a^3,\qquad D=100q^2,
\]

and take the fixed core

\[
                         u=(0,0),\qquad v=(D,0).
\]

For `0<=j<q`, put

\[
              z_j=(D/2+j^2,-D\,2^{j+1}).          \tag{5}
\]

The stored cases `a=2,3` are in general position.  For arbitrary finite
`a`, an arbitrarily small rational perturbation of the first coordinates
avoids the finitely many possible collinearities while preserving every
strict containment below.

If `i<j`, the point `z_i` is strictly inside the triangle `uvz_j`.  Indeed,
at height `y(z_i)` the interpolation fraction toward `z_j` is
`2^(i-j)<=1/2`; the horizontal section of `uvz_j` contains
`[D/4,3D/4]`, while every `x(z_i)` lies in `[D/2,51D/100)`.  Conversely
`z_j` is exterior to `uvz_i`.  Hence

\[
 A_i=\{u,v,z_i\},\qquad p_j=z_j,
 \qquad T_j=\operatorname{ext}(A_i+p_j)=\{u,v,z_j\} \tag{6}
\]

is an exact exterior-ear repair for every `i<j`, hiding exactly
`I_i={z_i}`.

Use the first `a` labels as hidden ears and the remaining `a^3` labels as
blockers/targets.  All cross pairs occur, so

\[
 |\mathcal I|=a,qquad |\mathcal T|=a^3,qquad
 |\mathcal G|=a^4.                                \tag{7}
\]

Under the uniform edge law the two variables are independent.  In the
notation of Theorem 23,

\[
 \kappa=1,\quad\tau=3,\quad R_0=4,\quad
 \rho={\log_2|\mathcal G|\over4}=\log_2a,          \tag{8}
\]

and both density hypotheses are equalities:

\[
 H_2(I)=\log_2a=\rho\kappa,qquad
 H_2(T)=3\log_2a=\rho\tau.                        \tag{9}
\]

Thus `epsilon=0`, `I(T;I)=0`, the independent support probability is one,
and the weighted `C_4` probability is one.  This is exact near-product
equality, not merely a dense approximation.

Nevertheless there are only `q+1=a+a^3+1` closed hulls containing the
fixed core `uv`: they are `uv` and the prefixes

\[
                 \{u,v,z_0,\ldots,z_j\},\quad0\le j<q. \tag{10}
\]

There are also only `q+1` ordinary convex faces containing `uv`: `uv` and
the triangles `uvz_j`.  Any selection of two `z`-points makes the shallower
one nonextreme.  Hence

\[
 { |\mathcal G|\over\#\{\text{core-preserving hulls/faces}\}}
 ={a^4\over a^3+a+1}=\Theta(a).                   \tag{11}
\]

For the two exact stored instances the counts are `16>11` and `81>31`.
The failure mechanism is a **same-side reset**: the hidden ear and blocker
both lie below `uv`.  Target variation replaces one nested point by another
and does not create a second opposite-side factor.  This is why (11) does
not contradict fixed-chord rectangle completion.

## 5. General meet-distributive comparison

The four-point interior-triangle example is the rooted-circuit convex
geometry on `{a,b,c,p}`:

\[
 \operatorname{cl}(S)=
 \begin{cases}
 S+p,&\{a,b,c\}\subseteq S,\\
 S,&\text{otherwise}.
 \end{cases}                                      \tag{12}
\]

It has 15 closed sets, while `K={p}` has `D=2,U=8`.  Direct products of
`m` copies are again convex geometries, hence their lattices are
meet-distributive.  They have

\[
 |\mathcal C|=15^m,qquad D(K)=2^m,qquad U(K)=8^m,\qquad
 {D(K)U(K)\over|\mathcal C|}=\left({16\over15}\right)^m. \tag{13}
\]

Thus meet-distributivity by itself not only fails `(LR)` but permits an
exponential tensor-power gap.  The planar concentric-pocket family shows
that planarity does not repair the implication; the geometric input must be
the ordered, opposite-side tangent structure used by the fixed-chord map.

## 6. Consequence for the ACP route

Theorem 23 is doing exactly what it claims: it gives a dense weighted
rectangle of repair records.  The false step is

\[
 \text{dense comparable support / many `C_4`s}
 \quad\Longrightarrow\quad
 \text{product-many intermediate hulls or faces}.             \tag{14}
\]

Any valid continuation must preserve enough signature to distinguish the
two half-plane factors.  At minimum it needs one of:

1. a common directed chord with dominance-compatible factors on opposite
   sides, where cross-union is injective;
2. cross-cell ordered variation which releases a genuine two-ended target;
3. a descent charge which pays same-side nested resets from the child/pocket
   complex, with a global reuse bound.

Closure-lattice cardinalities, meet-distributivity, mutual information,
support density, and weighted `C_4` count cannot replace that signature.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_cyclic_stem_hw/lattice_rectangle_counter/verify_lattice_rectangle_counter.py
```

The script uses integer determinants and exact rational counts.  It:

* verifies the minimal `15<16` planar obstruction;
* enumerates and deduplicates all fixed-`x` permutation chirotopes through
  `n=7`;
* enumerates all `2^18` subsets of the largest stored nested ring;
* checks all nested-ear containments and repairs in the `a=2,3`
  Theorem-23 equality examples;
* checks the entropy equalities after clearing logarithms by integer powers;
* checks a 4-by-5 opposite-side fixed-chord positive control; and
* writes the complete coordinates and counts to `certificate.json`.
