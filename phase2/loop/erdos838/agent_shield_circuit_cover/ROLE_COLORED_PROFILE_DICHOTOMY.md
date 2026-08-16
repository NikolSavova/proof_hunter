# Role-coloured local profiles: admissible reservoir or homogeneous root circuit

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

Canonical role colouring and the support-redundancy split give an exact
local theorem, but they do not force a root-admissible jet class.

Let `H` be a family of `t`-point ordinary faces in one ordered/simple-chain
local support `Q`, `|Q|=N`.  Fix the external base, root edge, occupied
mask, and seam side.  Assume:

1. ordinary convexity of a word and its external root/seam state are
   certified by `m=O(t)` strict orientation predicates of arity at most
   three;
2. after ordering the variable roles, each role occurs as a nonfirst
   variable in at most `Delta=O(1)` predicates; and
3. `t=O(log N)`.

These are the actual hypotheses of a fixed-base ear or ordered simple
chain after the first-two/last-two boundary jet is tagged.

There is a family `E` with disjoint coordinate supports `X_1,...,X_t`, all
of whose words lie in `H`, and

\[
                         |E|\ge {|H|\over t^t}.          \tag{1}
\]

After the `N^4`, polynomial-in-`t` losses needed to fix the actual boundary
jet and, in the bad case, a four-circuit role pattern, one of the following
holds.

1. **Root-admissible profile.**  A fixed root-good jet class has

   \[
       |J|\ge {|H|\over 2(N+1)^4}.                      \tag{2}
   \]

   Hence every quadratic local face coefficient survives, and the
   fixed-base adaptive-omission theorem applies directly.

2. **High support redundancy.**  For the role-coloured bad class put

   \[
    M=|E|,\qquad R=\log {\prod_i|X_i|\over M},
    \qquad N_E=\left|\bigcup_iX_i\right|.               \tag{3}
   \]

   The induced ordinary face complex obeys

   \[
    \log {V(Q)\over M}
     \ge\left[R+\log f(N_E)-t\log(N_E/t)\right]_+.      \tag{4}
   \]

   In particular, at `t=(1/4+o(1))log N_E`, quadratic `R` gives
   `V(Q)>=M2^{(1-o(1))R}`.  At arbitrary rank,
   `R>=rho t^2` gives the absolute bank

   \[
                         V(Q)\ge2^{(\rho^2/4-o(1))t^2}. \tag{5}
   \]

3. **Low-redundancy fixed circuit.**  There are subsets
   `Y_i subseteq X_i` such that every transversal is an ordinary local
   face with the same root-bad four-circuit and

   \[
    \left|E\cap\prod_iY_i\right|
        \ge M,2^{-A(m+\Delta R)}.                      \tag{6}
   \]

   Thus if `R=o((log N)^2)` and `log|H|=Theta((log N)^2)`, the full
   quadratic coefficient of the bad reservoir survives in a homogeneous
   root-circuit product.

The third alternative is a genuine barrier, not a disguised good class.
There is a scalable rational construction with `R=0`, an exact fixed
first-two/last-two jet, a fixed `1+3` circuit, and projectively arbitrary
children in `t-O(1)` roles.  Every transversal is an ordinary convex face,
but none is root-admissible.  Deleting the root maps this entire class to
its detached face with load one; if the same local class is reused by many
external contexts, the load is exactly the context multiplicity.  The
canonical load-one object is the **two-output** bank `(external context,
detached face)`, not a mixed one-face bank.

Therefore role colouring closes the compatible-profile gate only when a
quadratic root-good portion exists or when (4) pays.  In the surviving
low-`R` bad branch it performs the desired localization—down to one actual
circuit role pattern—but a summable one-face shield still needs an
independent guard-release, occupied-mask, or Hall decoder.  Projective
universality prevents deriving that release from the transcript alone.

## 1. Role colouring

Order each `F in H` as

\[
                         F=(x_1(F),\ldots,x_t(F)).       \tag{7}
\]

Colour every point of `Q` independently and uniformly with the colours
`1,...,t`.  Call `F` aligned when `x_i(F)` has colour `i` for every `i`.
For each fixed face,

\[
                         Pr(F\text{ aligned})=t^{-t}.   \tag{8}

\]

The expectation of the number of aligned faces is `|H|/t^t`, so one
colouring retains at least this many.  Let `E` be the retained ordered
words and let `X_i` be its used labels of colour `i`.  The `X_i` are
pairwise disjoint and (1) holds.  The colouring is not required to be
canonical for existence; choosing the lexicographically first maximizing
colouring makes it canonical whenever the point labels are fixed.

The loss is

\[
                         t\log t=o((\log N)^2)           \tag{9}
\]

under `t=O(log N)`.  Hence it never changes a quadratic coefficient.

For a fixed-base ear, record the first two and last two actual boundary
labels, padding ranks below four.  There are at most `(N+1)^4` such jets.
Root admissibility is constant on a fixed jet: internal turns are already
certified by ordinary convexity, and only the two endpoint turns into the
fixed base remain.  If at least half of `H` is root-good, pigeonholing its
jet proves (2).

Suppose instead that at least half is root-bad.  Every `B union F` contains
a strict planar four-circuit.  Choose the lexicographically first circuit.
Its intersection with the variable word is specified by at most four role
positions, and its intersection with the fixed external tuple is specified
by at most four external positions.  There are only

\[
                         O((t+|B|)^4)                    \tag{10}
\]

role patterns and constantly many oriented circuit types.  Pigeonholing
therefore fixes one actual `1+3` or `2+2` circuit pattern at only
`O(log(t+|B|))` bits of cost.  Apply role colouring after this thinning.

## 2. Bounded-degree sign transcripts

The consecutive-triple transcript extends verbatim to any bounded-degree
list of local orientation predicates.

> **Lemma 1 (bounded-degree local-sign retention).**  Let `E` be uniform
> on a family of words in `X_1 times ... times X_t`.  Suppose every word
> has the same prescribed outcome on `m` orientation predicates, each
> involving at most three variable coordinates and any number of fixed
> singleton parameters.  Order the variable coordinates.  If each
> coordinate occurs as a nonfirst variable in at most `Delta` predicates,
> then there is a coordinate product `prod_iY_i` homogeneous for every
> predicate and
> 
> \[
>  |E\cap\prod_iY_i|
>      \ge |E|,2^{-A_0(m+\Delta R)},                   \tag{11}
> \]
> 
> where `R=log(prod_i|pi_iE|/|E|)` and `A_0` is absolute.

**Proof.**  Write

\[
 a_i=I(X_i;X_1,\ldots,X_{i-1}),\qquad
 T_*=\sum_i a_i\le R.                                  \tag{12}
\]

For a predicate on variable coordinates `i<j<k`, its local total
correlation is at most `a_j+a_k`, exactly as for a consecutive triple.
For two variable coordinates it is at most the `a`-term of the later one;
fixed singleton parameters contribute zero entropy.  Hence the sum of
local total correlations is at most `Delta T_*<=Delta R`.

Apply the entropy-sensitive positive/negative orientation transcript to
each predicate.  Its transcript entropy is `O(1+TC)`.  Entropy
subadditivity gives joint transcript entropy

\[
                         O(m+\Delta R).                 \tag{13}

\]

Some transcript atom has the mass in (11).  Intersecting all coordinate
parts assigned by that atom gives one genuine product, homogeneous for
all predicates.  QED.

Apply Lemma 1 after the circuit role pattern is fixed, including the four
orientation signs of that circuit among the predicates.  In the
ordered/simple-chain setting the internal and closing turns certify that
every transversal is an ordinary face.  The circuit signs certify that
the same external root circuit survives for every transversal.  This is
(6).

The high-redundancy alternative is exactly
`HIGH_REDUNDANCY_SUPPORT_BANK.md` applied to the disjoint role supports,
giving (4)--(5).

## 3. Exact projective-universal bad product

The low-redundancy alternative cannot be promoted to root-goodness.
Choose a strictly convex rational `t`-gon

\[
                         c_1,\ldots,c_t                 \tag{14}

\]

around a root point `z`.  Choose three well-spaced roles `a,b,c` such that

\[
                         z\in\operatorname{int}
                              \operatorname{conv}\{c_a,c_b,c_c\}.       \tag{15}
\]

Make the four boundary-jet roles and the three circuit roles singleton
supports.  At each of the remaining `t-O(1)` roles, shrink an arbitrary
rational planar order type of `D` points into a sufficiently small
neighbourhood of `c_i`.  By openness of all finitely many strict
orientation and containment inequalities:

* every one-point-per-role transversal is a strictly convex `t`-gon;
* the first-two/last-two boundary jet is fixed;
* every transversal contains the same three fixed circuit anchors; and
* `z` lies strictly inside their triangle.

Thus

\[
 M=D^{t-O(1)},\qquad P_0=M,qquad R=0,                  \tag{16}

\]

and every word has the fixed strict circuit

\[
                         \{z,c_a,c_b,c_c\}.             \tag{17}

\]

The children in the variable roles are projectively universal: shrinking
is an affine realization preserving each prescribed internal order type.
For `t=alpha log D`, (16) has

\[
                         \log M=(\alpha-o(1))(\log D)^2.\tag{18}

\]

There is no root-admissible member at all, despite zero redundancy, a
complete homogeneous product, a fixed actual boundary jet, and a fixed
circuit.

This construction does have a detached shield: the `M` transversals are
distinct ordinary faces.  In a separated radial wrapper its ambient
one-gap/profile complexes may provide still more faces.  Accordingly it
is not a low-face counterexample and makes no sub-half construction claim.
It is sharp for the proposed inference

\[
 \text{low redundancy + transcript + fixed jet}
       \Longrightarrow\text{rich root-admissible class}.               \tag{19}

\]

## 4. Summability barrier

Let `C` be any family of distinct external contexts, all lying in the
common interior region in (15), and use the same detached product `E` for
each context.  The selected bad incidence set has `|C|M` records.  The
guard-deletion map

\[
                         (c,F)\longmapsto F             \tag{20}

\]

has image size exactly `M` and load exactly `|C|`.  The circuit itself
does not reduce this load: its three outer roles are already fixed.  The
pair map

\[
                         (c,F)\longmapsto(c,F)           \tag{21}

\]

is a load-one **two-face** bank, since a singleton context and detached
face are both ordinary.  Turning (21) into one ordinary mixed face is
precisely what the root circuit forbids.

Therefore a global circuit charge must retain a recoverable context tag,
use two output slots, or find an independent released shield.  Counting
the detached local face once per context is invalid.  This is the exact
summability obstruction left by alternative 3.

## 5. Consequence for the local profile programme

For a quadratic fixed-rank local reservoir, the safe workflow is now:

1. fix rank and actual boundary jet (`2^{O(log N)}` loss);
2. if a quadratic root-good class remains, apply fixed-base adaptive
   omission and obtain the rich compatible profile;
3. otherwise role-colour the root-bad class (`2^{O(t log t)}` loss) and
   fix a circuit-role pattern;
4. if its support redundancy crosses the rank tax, charge the induced
   ambient face bank by (4);
5. if redundancy is subquadratic, use Lemma 1 to obtain a homogeneous
   fixed-circuit product.

Step 5 is a localization, not a closure.  The exact next input must be a
mask-aware guard-release theorem or a Hall decoder which preserves the
external context.  The projective-universal construction proves that no
argument using only role supports, local sign transcripts, and the fixed
circuit can manufacture a root-admissible jet class.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_role_colored_profile_dichotomy.py
```

The verifier exhausts the role-colouring expectation, checks the
bounded-degree total-correlation inequality on finite word laws, and
audits an exact 17-point rational bad product: four nonconvex
projectively-universal child order types, all 256 convex transversals,
one fixed positive consecutive-sign pattern, and one strict `1+3` circuit
through the common root for every transversal.
