# Heavy middle toggles: first divergence and completion shields

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

A heavy middle-toggle fibre has substantially more structure than a generic
high-overlap bank.  Its common output turns every colliding contextual top
into a **uniform-rank convex completion over one common base**.  Repeating
the full Boolean toggle on that base is exact even when the `D` extension
labels vary with the completion.

There are two rigorous positive endpoints.

1. If a fixed extension label works for a complete `q`-layer on a support
   `W` (`q>=4`), planar four-locality forces the whole joined shield
   `B union W union {y}` to be convex.  Thus the apparent middle-layer
   overlap releases the full Boolean shield.
2. For an arbitrary completion family, all incompatibility with the common
   base is encoded by a rank-at-most-four trace clutter on its support.
   A matching of `s` disjoint traces suppresses the total number of
   compatible completions by `(15/16)^s`; the union of a maximal matching
   is a guard set of at most `4s` labels whose deletion releases a complete
   convex shield.

There is also an exact first-divergence alternative between two
completions: their union is an ordinary face, or a four-circuit uses a
label from each symmetric difference.  A dense compatible-pair graph gives
a global union bank with explicit load at most `3^(2q)`.

These statements do not yet close the global problem.  Across many common
bases, released shields can be reused, while the bad-pair circuit matchings
can live on different supports.  The missing theorem is now a summed
version of the trace-matching shield: its guard-released Boolean banks must
have fixed-power aggregate gain, or their first cross-base divergence must
produce a larger common shield.  A local common-`Y` assumption is not
needed for any of the localization below.

## 1. The exact variable-extension toggle bank

Let `P` be a planar general-position set with the contextual decoder
partition `P=O disjoint_union X`.  Fix a convex base `B subset O`.  Let
`mathcal Q` be a family of distinct `q`-sets in `O-B`.  For every
`Q in mathcal Q`, let `Y_Q` be a set of `D` labels in `X`,
such that

\[
                       B\cup Q\cup\{y\}\in F(P)
                 \qquad(y\in Y_Q).                          \tag{1}
\]

No equality or overlap condition on the sets `Y_Q` is assumed.

> **Theorem 1 (variable-`Y` local bank).**  The faces
> \[
>       B'\cup Q\cup\{y\},\qquad
>       B'\subseteq B,quad Q\in\mathcal Q,quad y\in Y_Q, \tag{2}
> \]
> are all ordinary and are pairwise distinct as indexed by `(B',Q,y)`.
> Consequently the bank has exactly
> \[
>                           2^{|B|}D|\mathcal Q|             \tag{3}
> \]
> members.

**Proof.**  Every set in (2) is a subset of the face in (1).  Its trace on
`X` recovers `y`, its trace on `B` recovers `B'`, and the remaining outer
labels recover `Q`.  QED.

The decoder statement uses the contextual partition into base, completion,
and extension labels.  Globally those roles can change from one fibre to
another; precisely that change creates overlap between banks (2).

## 2. A common output is another completion fibre

The preceding observation has a label-free formulation.  Consider any
family of Boolean intervals

\[
                       [A_i,T_i]=\{U:A_i\subseteq U\subseteq T_i\}
                                                               \tag{4}
\]

inside `F(P)`, with `|T_i-A_i|=b`.  In (2), take
`T_i=B union Q union {y}` and `A_i=Q union {y}`.

> **Theorem 2 (middle-overlap localization).**  If one ordinary face `U`
> lies in `L` indexed intervals (4), put
> \[
>                             P_i=T_i-U.                     \tag{5}
> \]
> Then
> \[
>                             T_i=U\cup P_i\in F(P).         \tag{6}
> \]
> Among the incidences there is a rank `p in {0,...,b}` carried by at least
> `L/(b+1)` of them.  If a fixed top face occurs with multiplicity at most
> `Sigma`, this gives at least
> \[
>                         {L\over(b+1)\Sigma}                \tag{7}
> \]
> distinct rank-`p` completions over the common base `U`.

**Proof.**  Since `U subset T_i`, (5)--(6) are immediate and `P_i` is
disjoint from `U`.  Pigeonhole its rank.  For fixed `U`, the set `P_i`
determines the top `T_i=U union P_i`; the multiplicity hypothesis gives
(7).  QED.

This is the exact first descent forced by heavy middle-toggle overlap.  It
does not guess the old contextual decomposition: the new state consists
only of an actual common face and actual completion sets.

## 3. Full layers release the whole shield

The strongest local completion statement is elementary but useful.

> **Theorem 3 (complete-layer closure).**  Let `W` be disjoint from a face
> `B`, let `4<=q<=|W|`, and fix a label `y` outside `B union W`.  If
> \[
>                   B\cup Q\cup\{y\}\in F(P)
>                        \qquad\left(Q\in{W\choose q}\right), \tag{8}
> \]
> then
> \[
>                         B\cup W\cup\{y\}\in F(P).         \tag{9}
> \]

**Proof.**  If (9) failed, planar Caratheodory would give a nonconvex
four-subset `C`.  Its trace `C cap W` has size at most four and therefore
extends to some `q`-set `Q subset W`.  Then `C` is a subset of the face in
(8), a contradiction.  QED.

If (8) holds for every `y` in a common `D`-set `Y`, the faces containing
exactly one marked `y` supply the distinct bank

\[
                         D,2^{|B|+|W|}.                    \tag{10}
\]

Thus the common-`Y` complete-layer variant is closed outright.  With
variable `Y_Q`, Theorems 1--2 remain valid; only the promotion (8)--(10)
requires a label of high completion codegree.

## 4. Circuit traces: matching suppression or guard release

Theorem 3 has a robust version.  Fix a face `F` and a disjoint support
`W`.  Form the trace clutter

\[
 \mathcal T(F,W)=\{C\cap W:
      C\subseteq F\cup W,\ |C|=4,\ C\notin F(P)\}.          \tag{11}
\]

Empty traces do not occur because `F` is a face.  Every trace has rank at
most four.  A subset `Q subset W` is a compatible completion exactly when
it contains no member of `mathcal T(F,W)`.

> **Theorem 4 (completion trace matching).**  If the trace clutter has a
> matching of `s` pairwise disjoint members, the number `I(F,W)` of all
> compatible completion subsets obeys
> \[
>                I(F,W)\le 2^{|W|}(15/16)^s.                \tag{12}
> \]
> Conversely, if `T_1,...,T_s` is a maximal matching, then
> \[
>                 G=T_1\cup\cdots\cup T_s,\qquad |G|\le4s, \tag{13}
> \]
> meets every bad trace and
> \[
>                         F\cup(W-G)\in F(P).                \tag{14}
> \]

**Proof.**  A compatible subset must avoid containing each disjoint trace.
If their ranks are `a_1,...,a_s<=4`, the number of subsets of `W` avoiding
all of them is exactly

\[
       2^{|W|-\sum a_i}\prod_i(2^{a_i}-1)
       =2^{|W|}\prod_i(1-2^{-a_i})
       \le2^{|W|}(15/16)^s,                                \tag{15}
\]

which proves (12).  The union of a maximal matching meets every trace,
else a disjoint trace could be appended.  If (14) were nonconvex, one of
its four-circuits would have a trace disjoint from `G`, a contradiction.
QED.

Writing `c_4=log(16/15)`, (12) gives the useful density form

\[
       I(F,W)\ge2^{|W|-\rho}quad\Longrightarrow\quad
       \nu(\mathcal T(F,W))\le {\rho\over c_4}.             \tag{16}
\]

Hence an exponentially dense completion complex differs from a complete
joined shield by a quantitatively controlled guard set.  The theorem is
sharp in its qualitative dependence: disjoint four-circuits independently
forbid one of the sixteen local Boolean patterns.

## 5. First divergence of two completions

Let `mathcal P` be distinct rank-`p` completions over a common face `F`:

\[
                         F\cup P_i\in F(P).                 \tag{17}

> **Lemma 5 (cross-circuit first divergence).**  For distinct `P_i,P_j`,
> either `F union P_i union P_j` is a face, or it has a four-circuit `C`
> satisfying
> \[
>       C\cap(P_i-P_j)\ne\varnothing,
>       \qquad C\cap(P_j-P_i)\ne\varnothing.               \tag{18}
> \]

**Proof.**  Take any bad four-subset of the union.  If it missed
`P_i-P_j`, it would lie in the face `F union P_j`; symmetrically it cannot
miss `P_j-P_i`.  QED.

The compatible branch already has a quantitative global bank.  Let `E_+`
be the number of ordered distinct pairs whose union with `F` is convex.
A fixed union face has at most `3^(2p)` ordered descriptions: every label
outside `F` is assigned to the first completion only, the second only, or
both.  Therefore

> **Corollary 6 (compatible-pair union bank).**
> \[
>       \#\{F\cup P_i\cup P_j:(i,j)\text{ compatible}\}
>                          \ge {E_+\over3^{2p}}.              \tag{19}
> \]

If `E_+>=|mathcal P|^2/2` and
`|mathcal P|>=2D^epsilon3^(2p)`, (19) gives a fixed-power
`D^epsilon` expansion over the completion family.  Otherwise at least half
the ordered pairs carry the cross-divergence circuits (18).  Those circuits
are precisely the input to Theorem 4 after their supports are localized.

## 6. What remains globally

The results above rule out three tempting false endpoints.

* High toggle overlap is not merely a decoder failure: it produces actual
  common-base completion faces by Theorem 2.
* A complete middle layer cannot remain a sparse local obstruction:
  Theorem 3 promotes it to a full joined shield.
* A dense incompatible completion complex cannot have arbitrary defects:
  disjoint defects cost `(15/16)` each, while concentrated defects are
  removed by the explicit guard set (13).

What is not yet summed is variation of the common base `F`.  Applying
Theorem 4 independently can reuse the same released face `F union (W-G)`
in many fibres, and ambient-label guessing of `G` is too expensive at the
fixed-power seam.  The remaining target is therefore:

\[
 \boxed{\text{sum the guard-released completion shields across bases, or
 charge their first cross-base circuit divergence.}}       \tag{20}
\]

The convex-cloud regression realizes maximal overlap and lands in the
first alternative: take all bases and completions inside one ambient
convex set.  It is harmless because the unrestricted Boolean cloud is
already present.  Thus (20) must be a global surplus theorem, not a claim
that local overlap is bounded.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_middle_toggle_fibres/verify_middle_toggle_first_divergence.py
```

The checker exhausts finite Boolean interval collisions, verifies the
complete-layer closure on exact rational configurations, audits the trace
matching inequality and guard release, and checks every compatible/bad
completion pair in several finite planar models.
