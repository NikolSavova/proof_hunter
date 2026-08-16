# A projectively universal central child defeats the two-sided product

**Date:** 2026-08-15.  All logarithms are base two.  This continues
`ALMOST_FULL_WORD_MIXED_BANK_BARRIER.md` on its two remaining proposed
escapes: multiply the left/right one-sided banks, or globally charge the
common central (1+3) circuits.

## Verdict

There is an exact scalable counter-regression in the same parabolic
two-arc model.  The central child (Y) may have an **arbitrary prescribed
rational order type**.  A projective tangent-coordinate embedding makes
all child labels a strict nesting chain relative to every left--right
outer pair while preserving the complete detached face complex of (Y).
Consequently:

* every partial base transversal is ordinary;
* the full detached child contributes all (H=V(Y)) faces;
* if both base arcs are occupied, an ordinary union contains at most one
  child label; and
* with only one base arc occupied, even granting every child face as a
  compatible profile gives only a one-sided bank.

Write (q=2k), let every base role have (D) labels, and put

[
              P=(D+1)^k-1,qquad M=D^{2k}.                        \tag{1}
]

Among faces which use at most one label from each base role, the complete
central/base face count satisfies the exact operation-level upper bound

[
 \boxed{
 V_{\rm tr}\le H(1+2P)+(|Y|+1)P^2.}                              \tag{2}
]

The four terms are respectively: child only, left only, right only, and
both arcs.  If

[
      \log M=(a+o(1))L^2,qquad \log H=(c+o(1))L^2,qquad
      \log|Y|=o(L^2),                                             \tag{3}
]

then

[
              {\log V_{\rm tr}\over L^2}le
                    \max\{c,a/2+c,a\}+o(1)
                  =\max\{a,a/2+c\}+o(1).                         \tag{4}
]

At (a=c=1/4), this is (3/8+o(1)), not (1/2).  Thus no one-face
inequality based only on the two one-sided unions and the central child
can recover the missing half base exponent.  The estimate is deliberately
optimistic: it counts **every** child face as compatible with either
one-sided base, although arbitrary children need not have this property.

The circuit charge has equally sharp congestion.  A polynomial-loss
pair-star

[
 \mathcal J=\{F\in\mathcal F(Y):\{o,p\}\subseteq F\},qquad
 |mathcal J|\ge {H-|Y|-1\over {|Y|\choose2}}                     \tag{5}
]

can be chosen with (p) nested inside
(operatorname{conv}{a,b,o}) for every left--right pair (a,b).
For the (M|mathcal J|) uniform records:

* the four-point circuit state ((o,p,a,b)) has exact load
  (D^{q-2}|mathcal J|) when (a,b) are the two canonical inner role
  labels;
* tagging by the actual old source (B_\omega) leaves load
  (|mathcal J|);
* tagging by (F) leaves load (D^{q-2}); and
* tagging by both ((B_\omega,F)) has load one but is a separated
  two-face state with (V^2) possible values.

Deleting central guards does not help.  Any ordinary output retaining the
whole base word can retain at most one child label, so some such output has
profile-history load at least

[
                       {|mathcal J|\over |Y|+1}.                  \tag{6}
]

Deleting a whole base side instead has at most

[
                |mathcal J|[2(D+1)^k-1]                           \tag{7}
]

possible face states and therefore loses half the base entropy, exactly
as in the preceding report.

This is not a global sub-half construction: faces using multiple labels
inside base-role cells, other directional child profiles, and other macro
masks remain available in the ambient point set.  It is a sharp kill of
the proposed local multiplication/central-circuit operation.  A positive
proof must use an ambient composition bank outside this trace complex, or
prove a new theorem coupling two arbitrary one-sided profile systems; an
ordinary circuit tag or a separated output pair is insufficient.

## 1. Arbitrary children can be totally nested

Normalize the limiting left and right roots as

[
                            u=(-1,0),\qquad v=(1,0).               \tag{8}
]

For a point (z=(x,y)) below (uv), use the positive tangent coordinates

[
             L(z)={1+x\over-y},\qquad R(z)={1-x\over-y}.           \tag{9}
]

Their inverse is

[
             (L,R)\longmapsto
             \left({L-R\over L+R},-{2\over L+R}\right),          \tag{10}
]

and direct barycentric calculation gives

[
 z\in\operatorname{int}\operatorname{conv}\{u,v,z'\}
       \quad\Longleftrightarrow\quad
       L(z)>L(z'),\ R(z)>R(z').                                  \tag{11}
]

Let (Y_0) be any finite rational general-position realization.  Choose
independent affine coordinates (f,g), with all (f)-values distinct and
indexed increasingly.  For sufficiently small rational
(arepsilon>0), put

[
 \begin{aligned}
 L_i&=L_0+\varepsilon f_i+\varepsilon^2g_i,\\
 R_i&=R_0+\varepsilon f_i-\varepsilon^2g_i,
 \end{aligned}                                                    \tag{12}
]

where (L_0=R_0>0).  Both sequences are strictly increasing.  The map
from ((f,g)) to ((L,R)) is invertible affine, and (10) is projective
with one positive denominator on the whole child.  Hence it preserves the
labelled order type and every ordinary subset of (Y_0).  Equations
(11)--(12) make the image one strict nesting chain.  Increasing (L_0)
and decreasing (arepsilon) place it in an arbitrarily small prescribed
pocket.

Now choose (k) macro base roles on each of two short arcs of the rational
parabola (y=x^2-1), the left arc close to (u) and the right arc close
to (v).  All macro points and all their subsets are in convex position.
Put an arbitrary (D)-point rational order type in a sufficiently small
cell at every macro role.  Every partial transversal remains ordinary.
Because all containments (11) are strict, the cells and child can be
shrunk so that for every left label (a), right label (b), and nested
pair (y_i\prec y_j),

[
                   y_i\in\operatorname{int}
                         \operatorname{conv}\{a,b,y_j\}.          \tag{13}
]

All conditions are finitely many open rational orientation inequalities,
so a generic rational realization in ambient general position exists.
This proves the arbitrary-child construction without imposing convexity,
strong separation, or a directional spectrum on (Y).

## 2. Exact restricted-face trichotomy

Consider ordinary subsets of the assembled configuration which meet every
base-role cell in at most one label.  The occupied state of one side has
((D+1)^k) possibilities, of which (P) are nonempty.

Classify a face by whether its base support meets the left and right arcs.

1. **Neither side:** its central trace is any ordinary child face, giving
   at most (H) states.
2. **Left only:** there are (P) partial base transversals and at most
   (H) possible child traces, giving at most (PH) states.
3. **Right only:** symmetrically at most (PH).
4. **Both sides:** if the child trace contained two labels, (13) would
   hide the inner one.  Hence it is empty or a singleton, giving at most
   ((|Y|+1)P^2) states.

The supports are disjoint, so these four classes are disjoint and their
states have no decoder overlap.  Summing proves (2).  Taking logarithms
gives (4), because

[
                         \log P={1\over2}\log M+o(L^2).            \tag{14}
]

This is a genuine geometric obstruction rather than an abstract
incompatibility graph: every child order type is realizable inside it.
It also explains why the earlier strong-separation endpoint-profile
factorization failed.  Same-type singleton transversals control no signs
with two labels in the central role; here all those signs are chosen to be
the strict nesting orientation.

## 3. Pair-star circuits and release congestion

The pair-star estimate (5) is the double count

[
 \sum_{\{o,p\}\in{Y\choose2}}
    |\{F:\{o,p\}\subseteq F\}|
      =\sum_{F\in\mathcal F(Y)}{|F|\choose2}
      \ge H-|Y|-1.                                             \tag{15}
]

Choose a maximizing pair and name the outer member in the nesting order
(o), the inner member (p).  Equation (13) gives the common strict
circuit

[
                        p\in\operatorname{int}
                              \operatorname{conv}\{a,b,o\}.       \tag{16}
]

Every (Fin\mathcal J) contains this same child pair.

For every full word (B_\omega), select the labels (a_\omega,b_\omega)
in the two roles closest to the central gap.  In the complete product,
the circuit state has only (D^2) values.  Each fixed value extends over
the other (q-2) base coordinates and every (Fin\mathcal J), so its
load is exactly

[
                          D^{q-2}|\mathcal J|.                     \tag{17}
]

The actual source (B_\omega) recovers all word coordinates but none of
the profile choice, leaving exact load (|\mathcal J|).  Conversely the
face (F) and circuit state recover only the two inner base coordinates,
leaving exact load (D^{q-2}).  The full pair ((B_\omega,F)) is
injective, but both entries are already ordinary faces; counting it gives
only the separated bound (V^2\ge M|\mathcal J|).

Suppose a guard-release rule maps every record
((B_\omega,F)) to an ordinary union which retains all of
(B_\omega) and a subset of (F).  By (13), that retained subset has rank
at most one.  There are at most (M(|Y|+1)) possible outputs for
(M|\mathcal J|) uniform records.  Pigeonhole proves (6).  Allowing the
rule to choose the retained singleton adaptively does not improve the
bound.

If instead the rule deletes all roles on at least one base side, the total
candidate state count is bounded by (7), even if every such union is
ordinary.  The corresponding uniform-record congestion is at least

[
                 {M\over2(D+1)^k-1}
                    =D^{k-o(k)}.                                  \tag{18}
]

Thus guard deletion spends the child entropy, while side deletion spends
half the base entropy.  There is no third bounded-release state in the
trace model.

## 4. Weighted global-load form

Let (w_{\omega,F}\ge0) be arbitrary weights on a selected record family
and put

[
                              W=\sum_{\omega,F}w_{\omega,F}.       \tag{19}
]

Pure averaging gives the following unavoidable loads for any routing into
the indicated state spaces:

[
\begin{array}{c|c}
\text{state space}&\text{some weighted load is at least}\\ \hline
\text{raw canonical circuit }(o,p,a,b)&W/D^2\\
\text{actual source }B_\omega\text{ plus circuit}&W/M\\
\text{profile }F\text{ plus circuit}&W/(|\mathcal J|D^2)\\
\text{full-word rank-}\le1\text{ release}&W/[M(|Y|+1)]\\
\text{one-sided release}&W/[|\mathcal J|(2(D+1)^k-1)].
\end{array}                                                       \tag{20}
]

For uniform weights these specialize to (6), (17), and (18).  In
particular the source occurrence cap in a triangle-tag Cauchy theorem is
(|\mathcal J|), not polynomial.  Normalizing weights can reduce that
cap only by reducing the selected record mass by the same factor.

Equation (20) is the precise global obstruction.  A low-rank circuit tag
has too few states; a source tag forgets the child face; a shield tag
forgets the outer word; and the joint source--shield tag is a (V^2)
object.  Any successful global charge must construct a new ordinary face
coexisting with information from both coordinates.

## 5. Scope

The construction and (2) are exact for the one-label-per-base-role trace
complex which carries the quadratic selected source entropy.  They allow
arbitrary low-face children both centrally and inside base roles.

They do **not** upper-bound the complete ambient face complex.  In
particular:

* a face may use several labels from one base-role child;
* other occupied macro masks may expose a detached one-gap profile bank;
* a special central child may have unusually rich directional profiles;
  and
* recursion across those ambient profiles may improve the coefficient.

Accordingly this is a scalable exact counter-regression to the proposed
left/right one-face multiplication and common-circuit Hall charge, not an
Erdős-838 counterexample.  The sole positive escape is now an ambient
composition theorem which genuinely uses multi-label role faces or
couples the two arbitrary one-sided directional spectra.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_central_nested_child_two_sided_product_barrier.py
```

Expected output:

```text
PASS: arbitrary child H=55 pair-star=13, words=16, all cross-rooted child pairs nested, restricted faces=1039<=1383, circuit load=52
```
