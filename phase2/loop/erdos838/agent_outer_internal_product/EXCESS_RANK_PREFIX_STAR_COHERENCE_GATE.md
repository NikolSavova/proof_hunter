# Excess rank after the terminal split: the prefix-star coherence gate

**Date:** 2026-08-15.  All logarithms are base two.  This continues
`ROLE_FOREST_TERMINAL_ENTROPY_SPLIT.md`.

## Verdict

The low-\(Q\), excess-rank terminal regime does **not** by itself contain a
Cartesian completion subfamily on the excess roles.  There is an exact
high-entropy prefix-star family for which

* the selected family has any prescribed quadratic logarithmic entropy below
  the full role-box entropy;
* along one terminal path every role has complete actual branching,
  \(a(v,i)=d_i\), so the path has \(Q=1\);
* in the all-loop chronology every role is deleted; but
* no selected word contains nondefault labels in two excess roles.

Thus neither the terminal entropy identity nor a four-local bad box on four
excess-role supports can be spliced to a selected-family product without a
new **sibling-coherence** theorem.  The four-local box may live entirely on
tuples which no selected source ever visits.

This is an exact hereditary set-system barrier, not a claimed planar
counterexample.  The genuinely planar central-Pascal common-guard example
independently shows that live normalization, linear excess rank, and complete
deletion also do not suffice, but it does not presently certify the
near-complete coloured-role branching required here.  Consequently the exact
remaining theorem is narrower than either ingredient separately:

> On a coefficient-below-one-half/minimizer slice, prove that a positive
> terminal-potential mass of near-complete coloured role paths is physically
> coherent across several excess roles, or charge the incoherent sibling
> stars to an ambient face/profile bank with global load
> \(2^{O(L\log L)}\).

No such planar/minimizer theorem is proved here, and no half-coefficient
closure is claimed.

There is a stronger weighted version.  It survives the effective mass
branching refinement of `EFFECTIVE_BRANCHING_ROLE_FOREST.md`: geometrically
decaying chronology weights make every conditional actual-label class have
exactly equal mass while different excess siblings still never coexist.

## 1. The exact prefix-star family

Fix integers

\[
                 s>k\ge1,\qquad d\ge2,
\]

and give every role the alphabet \(X_i=\{0,1,\ldots,d-1\}\).  Let
\(0^s\) be the default word.  Define

\[
\begin{split}
 \mathcal E_{s,k,d}
  ={}&\{(x_1,\ldots,x_k,0,\ldots,0):x_i\in[d]\}\\
   &\cup\{(0,\ldots,0,z,0,\ldots,0):
                     k<i\le s,\ 1\le z<d\}.
                                                               \tag{1}
\end{split}
\]

Hence

\[
                 |\mathcal E_{s,k,d}|
                    =d^k+(s-k)(d-1).                         \tag{2}
\]

The first term is a complete \(k\)-role core.  Every excess role contributes
only a star of one-coordinate deviations from the default word.

Consider an all-loop role chronology which asks the roles in order, uses the
usual heaviest actual-label class, and breaks ties in favour of label zero.
Follow the all-zero path.  (This is the branching datum seen by the role
forest whenever the current role remains the canonical eligible circuit
role; no planar realization of that eligibility predicate is asserted in
this section.)  Conditional on the zero prefix:

* for \(i\le k\), every label occurs and the zero class is heaviest (tied
  with the other labels before the last core coordinate); and
* for \(i>k\), every label occurs, while the zero class contains the default
  word and every later tail star, so it is heaviest.

Therefore

\[
                  a(v_i,i)=d\quad(1\le i\le s),
 \qquad C(0^s)=d^s=P_0,qquad Q(0^s)=1.              \tag{3}
\]

The terminal path is thus maximally branched according to the exact statistic
used in the capacity split.

On the other hand, if \(i,j>k\) are distinct and \(z,z'\ne0\), then

\[
      \{x\in\mathcal E_{s,k,d}:x_i=z, x_j=z'\}=\varnothing. \tag{4}
\]

So the excess roles contain no nontrivial two-dimensional Cartesian box,
let alone a four-role product.  Complete one-path branching records marginal
sibling availability; it records no compatibility between siblings born at
different depths.

## 2. The construction has the required entropy scale

Put \(N=sd\), let \(L=\log N\), and take

\[
                s=\lfloor\alpha L\rfloor,
       \qquad k=\lfloor cL\rfloor,qquad 0<c<\alpha.  \tag{5}
\]

Since \(d=N/s\), equations (2) and (5) give

\[
 \log|\mathcal E_{s,k,d}|
       =k\log d+O(1)
       =cL^2-cL\log L+O(L).                           \tag{6}
\]

Meanwhile the role-box rank is

\[
                         s=\alpha L+O(1),              \tag{7}
\]

so it has the exact linear excess \((\alpha-c)L+O(1)\) left by
`ROLE_FOREST_TERMINAL_ENTROPY_SPLIT.md`.  The failure in (4) is therefore
not a small-family or low-entropy artefact.

More generally, multiplying every word by the same released family
\(\mathcal U\) and giving each row total weight one preserves (2)--(4), the
source-weight normalization, and the full branching of the zero path.  It
does not create cross-role coherence.

## 3. Why a physical four-local box does not automatically help

Let \(i_1,i_2,i_3,i_4>k\).  Choose arbitrary nonempty supports
\(Y_{i_j}\subseteq X_{i_j}\setminus\{0\}\), and mark every transversal of

\[
                       \prod_{j=1}^4Y_{i_j}             \tag{8}
\]

as a bad four-circuit of one fixed signed type.  This is consistent with the
hereditary complex generated by the selected words: by (4), no selected word
contains even two vertices from different \(Y_{i_j}\), and hence none
contains a marked four-set.

Thus the conclusions of a four-local regularity lemma and of the terminal
path theorem can coexist abstractly while having zero incidence.  To combine
them one needs a statement about **co-occurrence across forest siblings**,
not merely density inside the physical support box.

The same point can be expressed through conditional codegrees.  For two
roles define

\[
 \Gamma_{ij}(z,z')=
   \#\{x\in\mathcal E:x_i=z, x_j=z'\}.                \tag{9}
\]

The forest statistic \(a(v,i)\) controls only which one-coordinate fibres
are nonempty at one chosen prefix.  In (1), it is maximal at every level,
while

\[
       \Gamma_{ij}(z,z')=0
       \quad(i,j>k, i\ne j, z,z'\ne0).              \tag{10}
\]

Any valid positive splice must therefore control a conditional codegree or
branch-energy quantity comparable to (9), or derive such control from planar
geometry/minimality.

## 3a. Exact weighted calibration of every branch

The support-only example above is sent to high \(Q_{\rm eff}\) by effective
mass branching if all words have unit weight.  That does not settle the live
weighted problem.  Put \(h=s-k\), and replace the tail in (1) by

\[
 \mathcal S_{h,d}=\{0^h\}\cup
 \{(0,\ldots,0,z,0,\ldots,0):1\le j\le h,\ 1\le z<d\}.
                                                               \tag{11}
\]

Use the selected source family

\[
                         [d]^k\times\mathcal S_{h,d}.   \tag{12}
\]

For a tail word, assign weight

\[
 w(0^h)=d^{-h},\qquad
 w(0^{j-1}z0^{h-j})=d^{-j}\quad(z\ne0).               \tag{13}
\]

Every full selected source gets the weight of its tail.  For each fixed core
word these weights sum to one, because

\[
 d^{-h}+(d-1)\sum_{j=1}^h d^{-j}=1.                  \tag{14}
\]

Thus all source weights are at most one and the total marked mass is

\[
                              M=d^k.                   \tag{15}
\]

Along the zero path, every core coordinate has \(d\) equal-mass classes.
Immediately before tail role \(j\), the surviving mass per fixed zero core is
\(d^{-(j-1)}\).  Each of its \(d-1\) nonzero classes has mass \(d^{-j}\),
and the zero class (all later deviations plus the terminal word) also has
mass \(d^{-j}\).  Hence

\[
                         r(v,i)=d\quad(1\le i\le s).    \tag{16}
\]

The selected terminal has weight \(d^{-h}\), and therefore

\[
 \mu(O)C_{\rm eff}(O)=d^{-h}d^s=d^k=M,
 \qquad Q_{\rm eff}(O)=1.                             \tag{17}
\]

This exactly saturates the effective forest potential on one path.  Yet no
word in (12) contains nonzero labels in two different tail roles.  Moreover,
there is only one released record per source, so (13) obeys the per-source
row-mass bound without metadata duplication.  With the scaling (5), (15) is
the required quadratic-logarithmic mass and \(h=(\alpha-c)L+O(1)\).

Thus near-uniform **conditional mass** also fails to force sibling
co-occurrence when individual chronology weights may decay exponentially in
depth.  A positive theorem needs one extra input, for example a
quasipolynomial lower cutoff on individual record weights, a bound on the
ratio between sibling source counts and sibling masses, or a genuinely
geometric bank which charges the first depth-skewed sibling.

## 4. What the planar Pascal regression proves, and what it does not

`LIVE_PASCAL_COMMON_GUARD_MULTIPLICATION_BARRIER.md` supplies an exact
stretchable family with all of the following simultaneously:

1. both endpoint banks have size \(V2^{-O(L\log L)}\);
2. the completion rank is at least \((\beta-o(1))L\),
   \(\beta=1-1/(4\ln2)>1/2\);
3. every nonempty completion trace remains incompatible with every released
   trace; and
4. the fixed-label chronology must delete the completion trace completely.

It therefore rules out a theorem based only on live normalization, excess
rank, four-locality, and terminal deletion.  However, its fixed-rank Pascal
families have not been shown to admit a single global injective role colouring
for which a positive terminal-potential mass also satisfies the low-\(Q\)
near-complete branching hypothesis (3).  Claiming that conjunction would be
an unsupported conversion from family entropy to one-path branching.

Conversely, (1) proves that even the strongest possible one-path branching
does not supply the missing product, but it is only a hereditary abstract
complex.  Projective universality cannot be invoked for free: simultaneously
realizing the marked circuits (8), all selected source faces, and the two live
ambient banks is precisely the missing geometry.

Hence the surviving gate is the intersection of these two barriers.  A proof
may close it by any one of the following genuinely new inputs:

* a planar sibling-codegree theorem forcing (9) on several excess roles;
* a globally bounded-load bank indexed by the first pair of incoherent
  siblings; or
* a minimizer mutation showing that a long prefix-star guard chronology
  decreases \(V\).

The present forest identities alone do none of these.  The weighted
calibration (11)--(17) is still an abstract hereditary construction; a
stretchable live/minimizer realization remains open.

## 5. Verification

Run

```text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_excess_rank_prefix_star_coherence_gate.py
```

The script exhausts several \((s,k,d)\), verifies (2), follows the exact
heaviest zero path, checks \(a(v_i,i)=d\) and \(Q=1\), and confirms the zero
two-role codegrees (4).  It also constructs the hereditary generated complex
and checks that an arbitrary four-role bad box on nondefault tail labels is
disjoint from every selected word.  Finally it verifies (11)--(17) with exact
rational weights, including row normalization, \(r(v,i)=d\), and exact
effective-potential equality.
