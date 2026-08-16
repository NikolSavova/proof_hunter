# Entropy-rich spread branch: an exact planar product obstruction

**Date:** 2026-08-14  
**Verdict:** quadratic polynomial-frame cover number, strong set-system
spread, near-maximality, and polynomially many exterior blockers do **not**
by themselves close the half-face Hall map.  There is a scalable stretchable
family satisfying all four properties in which:

* the visible-large replacements are merely coordinate moves in a product
  grid and produce no multiplicative target expansion;
* every half-core has codegree about the square root of the source count;
* its geometric extension frame is exponentially large, not polynomial;
* a common apex cloud supplies arbitrarily many hidden-large labels, but all
  of their Boolean hidden-face pools have only the original product-grid
  capacity.

Thus the proposed dichotomy

> low half-core codegree routes through `p`-containing half-faces, while high
> half-core codegree gives a subquadratic cover by polynomial frames

is false, even for rational planar order types and even after removing a
two-point common core.  This does **not** refute RNP: the configurations have
additional convex faces inside and between their large microblocks.  It
shows that the entropy-rich branch needs a recursive charge to those
microblock/pocket faces.  Ordinary sunflower or spread approximation stops
exactly one square root short.

All logarithms are base two.

## 1. Exact half-face routing lemma

First isolate what the spread route can prove.  Let `S` be an `r`-uniform
family of convex sources.  Suppose an incidence `(A,p)` has a canonical set
`J(A,p) subset A`, `|J|=s`, such that

\[
 T(A,p)=J(A,p)\cup\{p\}
\]

is convex.  This covers an interior blocker by the semicircle lemma and an
exterior blocker whose visible side has size at least `s`; take a canonical
`s`-subset of that side.  Put

\[
 d(J)=|\{A\in S:J\subseteq A\}|,
 \qquad \Delta_s=\max_{|J|=s}d(J).                 \tag{1}
\]

> **Lemma 1 (exact visible target multiplicity).**  For every incidence
> subfamily `I`,
> \[
> \boxed{|\{T(A,p):(A,p)\in I\}|
>       \ge {|I|\over(s+1)\Delta_s}.}              \tag{2}
> \]

**Proof.**  A fixed unmarked target `T` has at most `s+1` choices for which
of its points was `p`.  Once `p` is chosen, `J=T-p` is fixed and there are at
most `d(J)<=Delta_s` sources containing it.  QED.

If every source supplies `q` such incidences, (2) gives

\[
 V(P)\ge {q|S|\over(s+1)\Delta_s}.                 \tag{3}
\]

For the rankwise Hall target `V>=q|S|/poly(r)`, this needs
`Delta_s=poly(r)`.  In spread notation
`d(J)<=|S|/K^s`, it needs `K^s>=|S|/poly(r)`.  With
`s~r/2`, ordinary full spread has only `K^r<=|S|` and therefore supplies at
most the square-root scale `K^s<=sqrt(|S|)`.  The construction below attains
that obstruction exactly.

## 2. The product-block construction

Fix `r>=6` and `M>=2`.  Start with a strictly concave `r`-point chain

\[
 q_i=(i,i(r-1-i)),\qquad 0\le i<r.                \tag{4}
\]

Replace the two endpoint macro points `q_0,q_(r-1)` by singletons and every
internal macro point by an `M`-point almost-vertical block.  Use the standard
vertical lexicographic rule:

* triples in three blocks have the macro sign;
* triples in one block have the micro sign;
* the first two points in one block have negative sign;
* the last two points in one block have positive sign.

As usual this is rationally realizable: shear the macro and micro sets so
both coordinates increase and use

\[
 (X_i,Y_i)[Q_i]=
 \{(X_i+\epsilon^2x,Y_i+\epsilon y):(x,y)\in Q_i\}             \tag{5}
\]

for a sufficiently small rational `epsilon`.

Finally choose an `M`-point rational cloud `X` in a sufficiently small open
neighbourhood of the point `p=(-1,r^2)`.  The neighbourhood is chosen so
that every point of every internal block lies strictly inside
`conv{x,q_0,q_(r-1)}` for every `x in X`.  These are finitely many strict
conditions, so the cloud can be in general position and may have arbitrary
internal order type.

Let `b=r-2`.  For each word

\[
 \mathbf a=(a_1,\ldots,a_b)\in[M]^b
\]

take the two singleton endpoints and point `a_i` from internal block `i`.
Call the resulting rank-`r` face `A_a`, and let

\[
 \mathcal S_{r,M}=\{A_{\mathbf a}:\mathbf a\in[M]^b\}.          \tag{6}
\]

> **Theorem 2 (stretchable entropy-rich product obstruction).**  The family
> in (6) has the following exact properties.
>
> 1. `|S_(r,M)|=M^(r-2)`, and every source is convex and maximal:
>    `u(A)=0`.
> 2. If the chosen micro index in block `i` is `a_i`, then the alternatives
>    on one side of it are exterior singleton-ear replacements and the
>    alternatives on the other side are interior blockers.  Consequently,
>    \[
>    \mathbb E_A e_{\rm visible}(A)={b(M-1)\over2}.             \tag{7}
>    \]
> 3. Every `x in X` is an exterior hidden-large blocker, with
>    \[
>    \operatorname{ext}(A+x)=\{q_0,x,q_{r-1}\},\qquad
>    I(A,x)=A\setminus\{q_0,q_{r-1}\}.                         \tag{8}
>    \]
>    Hence each source has exactly `M` such labels and
>    \[
>    \mathbb E_Ae(A)\ge M+{b(M-1)\over2}.                      \tag{9}
>    \]
> 4. After deleting the two fixed endpoints, the source family is exactly
>    `M`-spread: a valid `k`-point partial transversal has codegree
>    \[
>    d(J)=M^{b-k}={|S|\over M^k},                              \tag{10}
>    \]
>    and every invalid `J` has codegree zero.

**Proof.**  A set meeting each occupied macro block in at most one point has
the induced macro order type, so every transversal in (6) is convex.
Adding another point to an internal block creates two selected points in an
intermediate occupied block.  The exact vertical-composition
classification forbids this in a convex spanning set.  There are no other
ordinary points, and every cloud point hides the internal chain, so `u=0`.

For two micro points in one intermediate block, the mixed-triple signs show
that the point on one side replaces the selected point on the hull, whereas
the point on the other side lies inside the old hull.  There are respectively
`a_i` and `M-1-a_i` choices, up to reversing the micro indexing.  Averaging
over the uniform word gives (7).  The strict triangle choice of `X` proves
(8), hence (9).  Finally, a partial transversal fixes exactly one coordinate
per represented internal block, leaving `M` independent choices in every
other block.  This proves (10).  QED.

## 3. Quadratic frame entropy and the failure of high-core discharge

Let a source frame have ground-set size at most `F`.  It contains at most
`binom(F,r)` rank-`r` subsets, so every frame cover of (6) has size

\[
 \boxed{T\ge {M^{r-2}\over\binom Fr}.}             \tag{11}
\]

Take `M=2^r` and `F=r^C` for fixed `C`.  Then

\[
 \log T\ge r(r-2)-O_C(r\log r)=\Omega(r^2).       \tag{12}

Thus this lies exactly in the entropy-rich branch left by the
polynomial-frame theorem.

Now take a half-core containing the fixed endpoints and `k` internal
coordinates, where `k=floor(b/2)`.  Its source codegree is

\[
 d(J)=M^{b-k}=|S|^{1/2+o(1)}.                     \tag{13}

It does not define a polynomial frame.  Every point in every unrepresented
internal block is individually addable to `J`, because it simply occupies a
new macro block.  Therefore

\[
 \boxed{|J\cup U(J)|\ge(b-k)M=2^{\Omega(r)}.}      \tag{14}

Equations (13)--(14) rigorously kill the hoped-for high-core implication.
High half-codegree can coexist with both quadratic frame-cover entropy and
an exponential geometric extension frame.  Abstract spread approximation
does not control `U(J)`.

The visible replacement map is equally sharp.  Each exterior microblock
label replaces one coordinate of the word `a`; its full `p`-containing
QuickHull target is another member of the same product grid.  Hence

\[
 |\mathcal I_{\rm visible}|
 ={b(M-1)\over2}|S|,
 \qquad
 |\{B(A,p):(A,p)\in\mathcal I_{\rm visible}\}|=|S|-1.          \tag{15}
\]

The missing word is the unique coordinatewise extreme word with no incoming
replacement.  Thus even using the entire visible face, rather than a
truncated half, gives average inverse load asymptotic to `b(M-1)/2`,
exponential in `r`.

## 4. The hidden-large branch is also sharp

For a fixed source, every apex label in `X` has the same hidden face

\[
 I_{\mathbf a}=A_{\mathbf a}\setminus\{q_0,q_{r-1}\}.          \tag{16}
\]

The repaired `p`-containing face is only the triangle
`{q_0,p,q_(r-1)}`.  Across all `M|S|` hidden incidences there are only `M`
such rooted triangles and only `|S|` full hidden faces.  Even allowing every
Boolean subset of every hidden face gives exactly the partial-transversal
family (including the empty face)

\[
 \boxed{|\bigcup_{\mathbf a}2^{I_{\mathbf a}}|=(M+1)^b.}       \tag{17}
\]

With the nonempty convention the right side is `(M+1)^b-1`; this changes
none of the estimates.

For `M=2^r`,

\[
 {(M+1)^b\over|S|}=(1+1/M)^b=1+o(1).             \tag{18}

Thus `M` hidden-large labels per source create essentially no new global
Boolean capacity.  The selected vertices of `I` store the source word, but
they do not store the apex-label demand.  A successful proof must recurse
into, or charge faces of, the apex cloud.

This construction also shows exactly where the missing capacity can live.
Omit the two global singleton endpoints, choose two arbitrary points in the
first internal block, two in the last internal block, and one in every
intermediate block.  The vertical classification makes every such set
convex: the first pair is a cap, the last pair a cup, and all other occupied
blocks are singletons.  Hence

\[
 \boxed{V(P)\ge {M\choose2}^2M^{b-2}
       ={(M-1)^2\over4}|S|.}                       \tag{18a}
\]

This dwarfs both the RNP demand `D|S|` and the total visible/hidden incidence
mass when `M=2^r`.  So the example is deliberately not an RNP
counterexample: it proves that a correct argument must discover
**two-ended microblock/pocket faces**, not that the needed capacity is
absent.

The target pool generated by all partial transversals is itself sharply
rank-concentrated.  Including optional use of the two endpoints, its rank
polynomial is

\[
 (1+z)^2(1+Mz)^b.                                  \tag{19}

Under its uniform face law,

\[
 \mathbb E K=1+{bM\over M+1},\qquad
 \operatorname{Var}K={1\over2}+{bM\over(M+1)^2}.  \tag{20}

For `M=2^r`, the variance tends to `1/2`.  Hence product spread does not
broaden the source-generated face ranks; it produces an asymptotically
constant-width grid.  Any broadening sufficient for Erdős 838 must come
from the extra within-block or pocket faces, precisely the recursive mass
ignored by a black-box spread theorem.

## 5. Exact scale match

For `M=2^r`, the ambient size is

\[
 n=(r-1)2^r+2,qquad
 \ell=\lceil\log n\rceil,qquad g=\ell-r=\Theta(\log r).       \tag{21}
\]

Thus the RNP demand scale is

\[
 D=2^g=\Theta(r),                                  \tag{22}

\]

whereas every source has `M=2^r` hidden-large exterior blockers and average
total exterior degree `Theta(r2^r)=Theta(n)`.  The construction therefore
has far more than the optimized-hull lower bound `D`, not merely a marginal
number of labels.  Its source entropy is

\[
 \log|S|=r(r-2),                                   \tag{23}
\]

and (12) certifies quadratic polynomial-frame cover number.

Again, this is not an RNP counterexample: `V(P)` can and does charge the
microblocks/cloud by faces outside the product target pool.  It is a
counterexample to closing RNP from spreadness plus half-face targets without
that recursive charge.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_entropy_spread/verify_product_blocker.py
```

The verifier builds a 22-point exact rational instance with `r=6,M=4`.
It checks every orientation determinant, exhaustively enumerates all 256
sources, and classifies all 4,096 source/nonmember incidences by exact convex
hulls.  It verifies `u=0`, the visible-replacement rule, all hidden-large
apex repairs, (7)--(10), the exact target unions, and all 576 two-ended
faces in (18a).  It also writes
`certificate.json` with exact scalable arithmetic for `M=2^r` at
`r=16,24,32,48,64`.

## 7. Surviving theorem target

The two branches now have a clean status.

* **Visible-large:** Lemma 1 closes the genuinely low half-codegree part.
  Intermediate/high codegrees do not imply polynomial frames; the product
  construction is a stretchable counterexample.  They must be charged to
  faces inside the exponential extension frames `J union U(J)`.
* **Hidden-large:** the hidden face carries source entropy but can be shared
  by exponentially many blocker labels.  Its Boolean cube alone is sharp on
  the product construction.  One must recurse into the replacement cone or
  blocker cloud while preserving the root demand.

So the entropy-rich gate is not a generic sunflower theorem.  The missing
statement is a **recursive spread-or-pocket theorem**: an exponential
extension frame or a multiply used hidden pocket must contribute ordinary
convex faces at the same `D|S|` scale.  The product obstruction identifies
exactly where those faces have to be found and prevents silently treating a
large core as a polynomial frame.
