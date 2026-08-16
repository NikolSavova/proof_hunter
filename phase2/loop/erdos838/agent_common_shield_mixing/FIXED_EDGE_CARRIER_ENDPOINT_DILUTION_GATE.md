# Fixed-edge carrier alphabets: endpoint surplus or critical dilution

**Date:** 2026-08-15. All logarithms are base two. Put

\[
 a=\log_2 3,
 \qquad \vartheta=2-a=0.415037499\ldots .                       \tag{1}
\]

This continues
`PLANAR_SINGLETON_TERMINAL_TWO_CELL_UNIVERSAL_CAGE.md` and addresses its
precise low-endpoint-surplus survivor.

## Verdict

A genuinely common physical carrier edge closes at exactly the polynomial
density appearing in the two-label survival gate. Suppose a carrier on
`p` physical labels has `V` ordinary faces and a family `H` of faces all
using the same exposed edge `uv` on the same side. There is one projective
chart, depending only on the physical support and `uv`, in which every one
of those `H` faces is a cap. Since every pair is a cup,

\[
 \boxed{\qquad
   {CU\over V}\ \ge\ {H\over V}\binom p2 .
 \qquad}                                                        \tag{2}
\]

Consequently

\[
 {H\over V}\ge p^{-\vartheta+\varepsilon}
 \quad\Longrightarrow\quad
 {CU\over V}\ge \tfrac13p^{a+\varepsilon}                     \tag{3}
\]

for large `p`. Equivalently, endpoint surplus below
`p^{a-o(1)}` forces the common-edge alphabet to have density at most

\[
                         {H\over V}\le p^{-\vartheta+o(1)}.      \tag{4}
\]

This is rank-free, so in particular there is no rank-`O(log p)` carrier
with low endpoint surplus and a common-edge alphabet denser than (4).
The exponent is exactly the required good-fraction threshold in the
three-cloud/two-label gate, not merely a numerically convenient bound.

The theorem does **not** close a face-dependent-edge alphabet. Paying for
one edge among `Theta(p^2)` physical possibilities destroys (3). Nor does
the bare least-counterexample comparison between a `p`-point child and a
`3p`-point parent suffice: it permits `H/V` as small as `p^{-a+o(1)}`,
where (2) gives only `p^{2-a+o(1)}` surplus. Thus the remaining operation
is sharply identified: retain a common physical edge at density above
`p^{-\vartheta}`, or route the dispersed-edge mass to the two-label/mixed
bank.

There is also an exact adjacent-edge release. Ears at `uz` and `zv`
always coexist after deleting the shared carrier vertex `z`. In a fixed
`z` fibre this turns the cross part of the two-cell bad-pair shadow into a
load-one mixed bank. Across varying carriers, however, erasing `z` incurs
the actual missing-vertex load (at most `p` without another mark). Hence
the only load-free universal cage is the same-edge branch.

## 1. Simultaneous projective normalization

> **Lemma 1 (one chart for a common exposed edge).** Let `u,v` be two
> labels and let `R` be a finite set lying strictly in one open halfplane
> bounded by `uv`. There is an orientation-preserving projective map,
> defined on `R union {u,v}`, which fixes `u,v` and has the following
> property. Every ordinary subset of `R union {u,v}` containing `u,v`
> with exposed edge `uv` is a cap in one fixed affine direction.

**Proof.** Affinely put

\[
 u=(-1,0),\qquad v=(1,0),\qquad R\subset\{y<0\}.                 \tag{5}
\]

For $\lambda>0$ use the projective map

\[
 \phi_\lambda(x,y)
   =\left({x\over1-\lambda y},{y\over1-\lambda y}\right).       \tag{6}
\]

The denominator is positive on the whole finite configuration, and the
homogeneous matrix of (6) has positive determinant. Thus all orientation
signs, and hence all ordinary subsets, are preserved. The map fixes the
line `y=0` pointwise. Choose $\lambda$ so large that

\[
                \left|{x\over1-\lambda y}\right|<1
                        \quad((x,y)\in R).                        \tag{7}
\]

Now `u` and `v` are respectively the unique leftmost and rightmost labels.
If `B` is ordinary and has exposed upper edge `uv`, its other boundary arc
from `u` to `v` is the lower `x`-monotone convex chain. Thus the labels of
`B`, in increasing `x` order, have one constant triple sign: `B` is a cap
(or a cup under the opposite sign convention). The chart is independent
of `B`. QED.

The same proof works for any selected family whose union support lies on
the fixed side. This side condition is automatic in the universal
common-edge cage: carrier faces lie on one side of `uv`, while the nested
ears lie on the other.

## 2. Endpoint dilution theorem

> **Theorem 2 (fixed-edge density versus endpoint surplus).** Let `P` be
> the `p`-label union support of a family $\mathcal H$ of `H` ordinary
> faces containing a common exposed physical edge `uv`, all on its same
> side. Write `V=V(P)`. In the chart from Lemma 1, its nonempty
> cap and cup counts satisfy (2).

**Proof.** Lemma 1 injects $\mathcal H$ into one endpoint family, so
`C>=H`. Every singleton and every pair is both a cap and a cup, hence

\[
                         U\ge p+\binom p2\ge\binom p2.            \tag{8}
\]

Multiplication and division by `V` prove (2). If
$H/V\ge p^{-\vartheta+\varepsilon}$, then for `p>=3`,

\[
 {CU\over V}
   \ge p^{-\vartheta+\varepsilon}{p(p-1)\over2}
   \ge {1\over3}p^{2-\vartheta+\varepsilon}
   ={1\over3}p^{a+\varepsilon},                                 \tag{9}
\]

which is (3); (4) is its contrapositive at exponent scale. QED.

### Live normalization

Equation (2) should be used with the *actual carrier face count* `V`, not
with the selected history mass and not automatically with the global
ambient count. If the rank-safe reductions supply

\[
                         H\ge Vp^{-\vartheta+\varepsilon},       \tag{10}
\]

the endpoint branch is finished. If they supply only the inductive bank
`H>=F_C(p)` while allowing `V` up to `F_C(3p)`, then

\[
              {H\over V}\ge p^{-a-o(1)}                         \tag{11}
\]

is the honest comparison, and (2) yields only `p^{2-a-o(1)}`. There is no
hidden fixed-power closure in (11).

This also explains the scope of the balanced-shell endpoint barrier. Its
full ordinary alphabet is Boolean, but no `V/p^{o(1)}` portion of that
alphabet shares one physical exposed edge. A truly dense common-edge fibre
would be caught by (2).

## 3. Adjacent cells release after deleting the common vertex

> **Lemma 3 (adjacent singleton release).** Let `B` be a strictly convex
> polygon with consecutive vertices `u,z,v`. Let `x` be an individually
> compatible ear at `uz`, and `y` an individually compatible ear at `zv`.
> Then
>
> \[
>                         (B\setminus\{z\})\cup\{x,y\}           \tag{12}
> \]
>
> is ordinary.

**Proof.** In the oriented boundary of `B+x`, the local edge `uz` is
replaced by the strictly convex chain `u,x,z`; in `B+y`, `zv` is replaced
by `z,y,v`. Delete `z`. The four local tangent inequalities at the two
ears say exactly that `u,x,y,v` is the exposed replacement chain for the
old arc `u,z,v`. All unchanged vertices retain their strict supporting
lines. Hence the resulting boundary is strictly convex. Equivalently, an
orientation check on the four local triples proves (12). QED.

For a fixed carrier `B`, let `E_cross(B)` be any collection of bad pairs
with one endpoint in each adjacent cell. The map

\[
       \{x,y\}\longmapsto(B\setminus\{z\})\cup\{x,y\}            \tag{13}
\]

is injective after physical role colouring. For a family $\mathcal H$ of
carriers sharing the same physical `z`, the map `(B,{x,y}) -> (13)` is
also injective: intersect the output with the carrier colour and add the
fixed `z` to recover `B`. Thus this branch gives exactly

\[
                       \sum_{B\in\mathcal H}|E_cross(B)|         \tag{14}
\]

ordinary outputs with load one.

If `z` is not fixed, the output omits it. Its decoder load is at most the
number of possible physical missing vertices, at most `p`; this loss is
real, not metadata. Therefore the `N^{2-o(1)}` two-shadow from the earlier
two-cell theorem closes the adjacent branch only after a common-`z`
localization (or an independent bank retaining that mark). The surviving
load-free branch is a common-edge dominance cage, exactly the setting of
Theorem 2.

## 4. Stress tests and remaining scope

* **Nested `1+3` cage.** The affine universal dominance construction is
  untouched: its arbitrary child order type remains hidden. Theorem 2
  charges the *carrier alphabet* once that alphabet is dense on the same
  physical edge. It does not pretend to release two child labels.
* **Three-cloud partner barrier.** Its rich faces have face-dependent
  extreme edges. A separate common-edge localization would cost up to
  `p^2`, so Theorem 2 cannot simply be applied. This is precisely the
  dispersed-edge escape stated after (4).
* **Rank.** No rank hypothesis was used. Rank `O(log p)` therefore cannot
  produce a counterexample to (3). It may still realize the critical or
  subcritical density `H/V<=p^{-vartheta+o(1)}`; excluding that regime
  needs the survival/mixed-bank half of the trichotomy.
* **Chart scope.** The theorem produces one projective chart fixed by the
  common physical edge and side. This is legitimate for an order-type
  invariant argument and for a tangent state which is recharted together
  with its outside roles. It is not automatically a lower bound in an
  independently prescribed affine projection chamber. If chronology has
  frozen such a chamber, compatibility with (6) must be retained as an
  explicit state coordinate.

## 5. Verification

Run

```text
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_fixed_edge_carrier_endpoint_dilution_gate.py
```

The verifier uses exact rational arithmetic. It projectively normalizes a
generic carrier whose original labels extend far beyond both endpoints of
`uv`; checks every orientation sign; exhausts every ordinary fixed-edge
face and verifies it becomes a directional cap; enumerates `V,C,U` and
checks (2). It also exhausts integer-grid ears at every adjacent edge pair
of a rational pentagon, verifying (12), injectivity in a fixed carrier,
and the exact exponent identity `2-(2-log2(3))=log2(3)`.
