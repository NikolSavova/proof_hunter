# Codimension-three source shadows in the tangent reset

**Date:** 2026-08-15. All faces are nonempty. This note audits the exact
tangent-line construction from
`SCALABLE_STRETCHABLE_PARTNER_RESET_AND_FACE_AUDIT.md`, including the
arbitrary-child substitution and endpoint-profile ramp from
`LOW_FACE_SUBSTITUTION_AND_STRONG_COMB_RAMP.md`.

## Verdict

The original three full class words do **not** feed the history-faithful
codimension-three source-shadow lemma. For `m>=2`, omitting one of the
`2m` macro roles in each of three classes leaves both an `L`-role and an
`R`-role in each lower class. The union already contains a strict bad
`2+2` circuit. Thus the number of ordinary almost-full outputs is exactly
zero, even with empty seam. A seam cannot repair this hereditary defect.

There is, however, a canonical and much larger recoverable bank. For any
three ordered classes `i<j<k`, retain

\[
              L_i,\qquad L_j,\qquad L_k\cup R_k.       \tag{1}
\]

These `m,m,2m` macro cells form a cup. After arbitrary `D`-point child
order types are substituted into the cells, every transversal choosing one
physical label from each cell in (1) is still a cup. Consequently there are

\[
                              D^{4m}                    \tag{2}
\]

distinct ordinary full-word faces for every class triple. The internal
children may simultaneously realize the sharp cap-to-cup endpoint ramp;
the bank uses only three-distinct-cell signs, so the ramp cannot erase it.
Banks from different class triples have different class supports, hence a
`t`-class reset contains the disjoint bank

\[
                         \binom t3D^{4m}.               \tag{2a}
\]

There is an even larger ambient bank: retain every `L`-cell in classes
`0,...,t-2` and every cell in the top class. These `m(t+1)` cells form one
cup, giving

\[
                              D^{m(t+1)}.               \tag{2b}
\]

The codimension-three splice becomes valid **after** this source thinning.
For complete equal alphabets its exact ledger is

\[
\begin{array}{c|c}
\text{thin records}&D^{4m}\\
\text{omission incidences}&2m^3D^{4m}\\
\text{distinct ordinary outputs}&2m^3D^{4m-3}\\
\text{decoder load}&D^3.
\end{array}                                             \tag{3}
\]

If the records retain the discarded halves of the two lower full class
words as hidden history, their exact load is instead

\[
                              D^{2m+3}.                 \tag{4}
\]

Thus three role colours are available, but not at constant completion cost:
the tangent circuit signs force a `2m`-role source-thinning payment before
the three omissions. At the live large-alphabet scale the base banks
(2a)--(2b), not the cubic multiplier in (3), are the decisive consequence. In
particular, any claimed low-face parent with

\[
 V(P)<\max\left\{\binom t3D^{4m},D^{m(t+1)}\right\}     \tag{5}
\]

cannot contain this separated tangent reset, regardless of the child order
types or endpoint ramp. This is a theorem about the exact tangent model,
not a proof that every planar fresh-partner itinerary has the same
cross-class cup.

## 1. The mixed-side circuit obstruction

Write the macro cells of class `i` as

\[
                  L_{i,0},\ldots,L_{i,m-1},
                  R_{i,0},\ldots,R_{i,m-1}.            \tag{6}
\]

The exact cross-quad classification in the tangent construction says that,
for every `i<j`,

\[
 \{L_{i,a},R_{i,b},Z_{j,c},Z'_{j,d}\}                 \tag{7}
\]

is nonconvex for every `a,b`, every two distinct higher cells, and every
choice `Z,Z' in {L,R}`. This is stronger than the selected one-factor
circuits: every mixed-side lower pair obstructs every higher pair. Strictness
makes (7) stable under substitution, so every physical transversal through
the four cells is nonconvex as well.

It follows immediately that an ordinary partial-transversal union meeting
at least two cells of a higher class can meet **at most one side** of the
lower class. For three ordered class traces of rank at least two, the first
two traces must therefore both be one-sided. Starting with three full
`2m`-role words, at least `m` roles must be discarded from each of the first
two words. Three single omissions cannot do this when `m>=2`.

More quantitatively, if each cell has `D` label choices, the compatible
maximal word patterns obtained by allowing either side in each lower class
number at most

\[
                         4D^{4m},                       \tag{8}
\]

versus `D^{6m}` original full histories. The factor four is only the two
side choices in each lower class. For the fixed canonical choice (1), the
erased-label completion multiplicity is exactly `D^{2m}`.

This identifies the exact source-thin branch of the general source-shadow
trichotomy: the missing source is not a prefix artifact and not an abstract
history collision. It is a visible signed-circuit obstruction.

## 2. The canonical cross-class cup

Before the small lift, a macro point of class `r` with local parameter `s`
has coordinates

\[
       p_r(s)=(r+s,r^2+2rs),\qquad
       s\in(0,1/8)\ \text{on }L,
       \quad s=B+(0,1/8)\ \text{on }R,                 \tag{9}
\]

where `B=t+1`. The construction adds `delta x^2` to the second coordinate
for a positive rational `delta`.

All ordered triples in (1) are positive:

* three cells in one class acquire the positive quantity
  `delta (x_2-x_1)(x_3-x_1)(x_3-x_2)`;
* for a same-class pair followed or preceded by another class, the
  unlifted sign is determined by which side of the relevant tangent line
  the third point lies. A lower `L`-point lies strictly above a higher
  tangent because `(j-i)^2-2(j-i)s>0`; the lift adds a positive
  Vandermonde term;
* for three distinct classes with all three points on `L`, use
  `y=x^2-s^2`. If `d_1=x_2-x_1` and `d_2=x_3-x_2`, the unlifted determinant
  is
  \[
   d_1d_2(d_1+d_2)+d_1(s_2^2-s_3^2)
                         +d_2(s_2^2-s_1^2)>0,          \tag{10}
  \]
  since distinct class gaps give `d_1,d_2>7/8` while `0<s_r<1/8`;
* moving the last point of (10) from its `L` parameter to its `R`
  parameter moves it along the same tangent. The determinant is affine in
  that parameter with derivative
  \[
        (x_2-x_1)\bigl(2k-\operatorname{slope}(p_i,p_j)\bigr)>0. \tag{11}
  \]
  The last inequality follows from `i<j<k` and `s_i,s_j<1/8`:
  the earlier secant slope is at most
  `x_1+x_2+1/56<2j<2k`.

The lift contributes a positive Vandermonde term whenever the three cells
belong to distinct macro points, so none of these signs can reverse.
Therefore the macro set (1) is a cup.

In the arbitrary-child construction, a triple using three distinct cells
has exactly the macro sign. A source word uses at most one physical point
from each cell. Every triple in every transversal of (1) is consequently
positive, proving (2). Notice that this argument never inspects a triple
inside a child. The children may be nonconvex, pairwise nonisomorphic, and
arranged in the endpoint-profile ramp.

The same proof gives (2b): any triple in all the lower `L`-blocks plus the
full highest class is one of the cases above. The three-class subbank is
recorded separately because it is exactly the interface needed for three
role colours. Both conclusions remain confined to the displayed tangent
order type.

## 3. Exact source-shadow and history ledger

Use the cells in (1) as three coloured role systems of lengths

\[
                         (q_1,q_2,q_3)=(m,m,2m).        \tag{12}
\]

Every complete source record has `D^(4m)` label choices. Omitting one role
of each colour preserves the cup. There are `m*m*(2m)=2m^3` occupancy
masks. For each mask, exactly `D^(4m-3)` retained-label assignments remain,
and each output has the `D^3` possible omitted labels as completions. This
proves (3), including exact decoder load.

If an input record is instead a full word on all `6m` cells of the three
classes, the same output forgets the `2m` labels on the discarded `R`
halves of the first two classes. Its load is

\[
                    D^{2m}\cdot D^3=D^{2m+3},          \tag{13}
\]

which proves (4). A fixed nonempty seam may be adjoined only when it is
compatible with every selected cup word; low parent count alone does not
guarantee that compatibility. The empty-seam bank already proves (2).

This also explains why the cubic splice by itself does not defeat the
large-alphabet completion barrier: relative to full histories, its cubic
role count is paid for by exponential source erasure. Conversely, whenever
either bank in (5) already exceeds the permitted parent face count, no
splice or seam is needed—the source-thin bank itself excludes the exact
reset. In the standard tangent-reset scaling `N=2mtD`,
`t~m~(log N)/6`, the three-class bank has base-two logarithm
`(2/3+o(1))(log N)^2`, while the all-lower bank has
`(1/36+o(1))(log N)^3`. Thus this exact reset is far outside a half-scale
parent budget. These numerical consequences use that parameterization
only; they are not asserted for arbitrary many-class planar itineraries.

## 4. Exact verification

Run

```text
python3 phase2/loop/erdos838/agent_many_class_partner_reset/verify_codimension_three_tangent_source_shadow.py
```

The verifier uses rational arithmetic throughout. It checks six exact macro
constructions (`3<=t<=8`), every mixed-side obstruction and every
codimension-`(1,1,1)` almost-full support in that sweep, and every triple of
the canonical cup banks, including each all-lower-plus-top bank. It then
substitutes alternating nonconvex
four-point children, exhausts all relevant physical child transversals,
rechecks the heterogeneous strong-comb profile and the exact max-plus ramp,
and exhaustively verifies the complete-product counts and loads in (3)--(4).

The finite sweep is a regression artifact; the all-parameter statement is
proved by the signed-coordinate argument in Section 2.
