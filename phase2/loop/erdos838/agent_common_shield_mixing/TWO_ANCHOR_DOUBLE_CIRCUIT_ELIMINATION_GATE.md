# Two bad anchors: exact circuit elimination and decoder barrier

## Verdict

In a genuine two-block strong-glue chart, the two nonaddable endpoint
incidences produce two bad `1+3` circuits

\[
 C_L=\{a_0,a_1,y,z\},\qquad
 C_R=\{y,z,b_0,b_1\},                                  \tag{1}
\]

sharing the two physical anchors `y,z`.  Their signed elimination has four
and only four coarse types.  After orienting the circuits oppositely at `y`,
their signs at `z` are opposite in the two diagonal types and equal in the
two mixed types.  Opposite signs at **both** anchors are not sufficient for
a detached convex eliminant: when `y` and `z` are both inner points, every
sign-compatible single-anchor eliminant remains a rooted `1+3` circuit.

There is nevertheless an unconditional geometric rank-four face

\[
                         \{a,y,z,b\}                    \tag{2}
\]

for every `a` on the left and `b` on the right.  It retains both anchors but
not the full endpoint faces.  Dually, the detached face `A union B` retains
the full cap/cup endpoints but erases both anchors.  The ordered **pair**

\[
                  \bigl(A\cup B,\ \{a,y,z,b\}\bigr)    \tag{3}
\]

decodes `(A,B,y,z)` with load one, whereas neither component is a one-face
decoder.  On the exact twelve-point Pascal wrapper, the canonical rank-four
map has maximum load `108`; (3) has load one on all `3600` double-bad
records.

The circuit pair also does not force a decreasing physical bipartition.
The induced six-label carrier has `V=50` and a singleton strong-glue mutation
of size `48`, but two additional rational points produce an eight-point
configuration with `V=121` for which **all 256 physical bipartition
mutations have value at least 121**, while the same two rooted circuits and
their convex seams remain induced.  Thus any minimizer contradiction must
use global extension-cell/tangent data, not rank-three circuit elimination
alone.

This closes the requested classification but not the converter: the exact
survivor is a two-face tensor whose missing operation is to merge (3) while
preserving all four physical coordinates.

## 1. Strong-glue setup

Let `L,R` be the two fixed role grounds in one genuine strong-glue chart.
Let

\[
 A\in\mathcal C(L),\quad B\in\mathcal U(R),\quad
 y\in L\setminus A,\quad z\in R\setminus B,             \tag{4}
\]

and suppose

\[
                 A+y\notin\mathcal C(L),\qquad
                 B+z\notin\mathcal U(R).                \tag{5}
\]

Choose canonical witness pairs `a_0,a_1 in A` and `b_0,b_1 in B` for which
(1) are bad four-sets.  This witness existence is an additional
common-neighbourhood hypothesis if one is not already in a literal
strong-glue chart; a wrong internal triple alone does not name the physical
opposite-anchor circuit.

Every bad planar four-set has a unique inner point.  In `C_L`, the right
anchor `z` is never inner, so

\[
                         I_L\in\{a_0,a_1,y\}.            \tag{6}
\]

Similarly the left anchor `y` is never inner in `C_R`, and

\[
                         I_R\in\{z,b_0,b_1\}.            \tag{7}
\]

Only whether `I_L` lies in `A` or equals `y`, and whether `I_R` lies in `B`
or equals `z`, matters for signed elimination.

## 2. Exact signed-elimination table

Give an inner point the circuit sign opposite the three outer points.  Flip
the global sign of each circuit so that

\[
                         C_L(y)=+,qquad C_R(y)=-.        \tag{8}
\]

Then

\[
 {C_L(z)\over C_L(y)}=
   \begin{cases}+1&I_L\in A,\\-1&I_L=y,\end{cases}
 \qquad
 {C_R(z)\over C_R(y)}=
   \begin{cases}+1&I_R\in B,\\-1&I_R=z.\end{cases}      \tag{9}
\]

Remembering the sign reversal in (8) gives the following exact table.  A
`2+2` entry is an ordinary convex quadrilateral; `rooted` means a bad
`1+3` circuit.

| `I_L` | `I_R` | signs at `z` after (8) | best sign-compatible eliminant |
|---|---|---|---|
| in `A` | in `B` | opposite | detached `a_0a_1b_0b_1` (`2+2`) |
| in `A` | `z` | equal | `a_0a_1 z b_j` (`2+2`), losing `y` and one `B` label |
| `y` | in `B` | equal | `a_i y b_0b_1` (`2+2`), losing `z` and one `A` label |
| `y` | `z` | opposite | only rooted `1+3` eliminants |

The table follows by writing the four signed circuits on the six-label
ground and applying the circuit-elimination sign containment rule.  The
verifier constructs a rational representative of every row and exhausts
every four-subset of `(C_L union C_R)-y` and
`(C_L union C_R)-z`.

Two cautions are essential.

1. Circuit signs are defined only up to global reversal, so one can always
   make them opposite at **one** shared anchor.  What is invariant is whether
   they are then equal or opposite at the other anchor.
2. Even when they are opposite at both anchors, simultaneous cancellation
   of both affine coefficients is not automatic.  The both-inner row is the
   exact counterexample: its allowed eliminants retain one anchor and remain
   nonconvex.

Thus plain oriented-matroid elimination does not supply the desired ordinary
full-mark output.

## 3. What strong-glue geometry supplies beyond elimination

For arbitrary `a in A` and `b in B`, the two-label left trace `{a,y}` and
two-label right trace `{z,b}` are automatically compatible.  Hence (2) is
an ordinary `2+2` face in all four rows of the table.  Also

\[
                         A\cup B                          \tag{10}
\]

is an ordinary detached face because its traces are the original cap and
cup.  Conversely, the exact strong-glue face classification and (5) give

\[
 A\cup B\cup\{y\}\notin\mathcal F(P),\qquad
 A\cup B\cup\{z\}\notin\mathcal F(P).                  \tag{11}

Thus no literal-inclusion output can retain full `A,B` and even one bad
anchor.  This is stronger than failure of a particular elimination choice.

Choose `a=a_*(A,y)` and `b=b_*(B,z)` canonically from the two witness pairs.
The rank-four output (2) recovers only `(a,y,z,b)` and has exact load

\[
 \Lambda(a,y,z,b)=
   |\{A:a_*(A,y)=a\}|\,|\{B:b_*(B,z)=b\}|.              \tag{12}
\]

There is no circuit-theoretic bound on these two fibres.  In contrast, the
pair (3) has load one: intersect its first component with the fixed role
grounds to recover `A,B`; in its second component, the label outside `A` on
the left is `y`, and the label outside `B` on the right is `z`.

This is the sharp decoder statement:

> the double circuit gives a load-one **two-face** converter and a possibly
> high-load one-face anchor seam.

The two-anchor-avoidance theorem supplies large cap and cup reservoirs in
`P-{y,z}`, but those are further detached faces.  Without a composition
lemma, adding them only enlarges the same tensor rather than merging (3).

## 4. Exact Pascal stress

Let `Q=T(4,2)` be the rational six-point Pascal cell and
`P=Q prec Q` its exact twelve-point strong glue.  In the prescribed chart,

\[
                         (C(Q),U(Q),V(Q))=(31,31,50).    \tag{13}

Among the endpoint incidences there are `60` nonaddable cap-anchor records
and `60` nonaddable cup-anchor records.  Their Cartesian product gives
`3600` double-bad records.  All four rows of the sign table occur, with
counts

\[
             1444,\quad836,\quad836,\quad484.           \tag{14}

The canonical one-face seams (2) occupy only `121` distinct rank-four
faces and have maximum decoder load `108`.  The ordered pairs (3) are all
distinct and have load one.  Every detached `A union B` is ordinary, while
(11) holds record by record.

This finite rational instance proves that the anchor seam is not secretly a
bounded-load full-record decoder.

## 5. Physical bipartition mutation: local gain, global failure

The six witness labels alone have the order type represented by the four
rows above.  In the first row, and equivalently after the relevant
relabellings in the other rows, the induced carrier has

\[
                         (C,U,V)=(31,31,50).             \tag{15}

Moving the appropriate right singleton to the opposite strong-glue side
gives an exact physical bipartition mutation with `48` faces.  This is the
tempting local minimizer contradiction.

It is not stable under ambient labels.  Take the first-row rational carrier
inside `T(4,2) prec T(4,2)` and adjoin

\[
                         (89/11,-173/11),\qquad
                         (-116/11,49/11).                \tag{16}

The resulting eight-point configuration is in general position, still
contains both induced circuits (1), the detached seam, and all four-point
anchor seams.  Exact enumeration gives

\[
                         (C,U,V)=(77,71,121),             \tag{17}

and for every physical bipartition `S sqcup S^c`,

\[
 V(P[S])+V(P[S^c])+C(P[S])U(P[S^c])\ge121.              \tag{18}

All `256` choices are checked.  In particular the two far-cell singleton
mutations of the named anchor `z` have values `123` and `132`.

This is a stretchable, exact **partition-minimal** barrier, not a globally
`V`-minimal configuration.  It proves that no theorem using only the two
induced circuits can force a decreasing physical bipartition.  In a global
minimizer, the exact singleton condition is instead

\[
 \ell_z\le1+C(P-z),\qquad \ell_z\le1+U(P-z).             \tag{19}

To get a mutation contradiction one must show that the mass of double
circuits makes one inequality in (19) fail.  The rank-four seams have the
large fibre (12), so that injection is precisely what is missing.

## 6. Scope and next operation

Proved here:

- the complete shared-anchor circuit-sign classification;
- the exact convex eliminants and the both-inner failure;
- a universal ordinary rank-four anchor seam;
- a load-one two-face decoder and the exact one-face fibre;
- a rational high-load Pascal stress;
- a rational partition-minimal ambient barrier.

Not proved here:

- a one-face merger of (3);
- that the large deleted-anchor reservoirs coexist with the seam;
- a global minimizer contradiction;
- the half-coefficient theorem.

The proposed minimum-extension-cell tangent-interval route is genuinely
additional information: it can constrain the fibres in (12) or charge them
to directional profiles.  It is not a consequence of the two circuit sign
vectors.

