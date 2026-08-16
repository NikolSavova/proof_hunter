# Post-collision remapping: an exact minimax barrier

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

No total remapping of the shelling/root-symbol ledger to ordinary faces can
have fibre $o(W)$, where $W$ is the total shelling weight. This remains
true if the remapping may inspect the whole future shelling, use any fixed
number of next-transition labels, replace cap endpoints, or choose auxiliary
cup data.

Let $P$ have $n$ points and $V=V(P)$ ordinary faces. The exact
shelling ledger has weighted mass $W(V-n)$, because every shelling contains
one symbol for every non-singleton face. Any mass-preserving remapping of
this ledger to the $V$ ordinary faces has an output of load at least

\[
 \boxed{W\frac{V-n}{V}.}                                 \tag{1}
\]

If outputs must remain non-singleton, the lower bound is exactly $W$, and
the canonical decoder attains it. Even when singleton outputs are allowed,
every generic planar point set satisfies

\[
 V\ge n+\binom n2+\binom n3=\frac{n(n^2+5)}6,            \tag{2}
\]

so (1) is at least

\[
 \boxed{W\left(1-\frac6{n^2+5}\right)=(1-O(n^{-2}))W.}  \tag{3}
\]

This is a sharp post-collision obstruction: the desired $o(W)$ fibre is
impossible for any decoder whose outputs are single ordinary faces.

The strongest one-next-transition menu was also tested exactly. For a tagged
face $F$, let $z$ be its first deleted member and $y$ the immediately
next shelling label. Allow every valid ordinary face among

\[
 F,\qquad F\cup\{y\},\qquad
 (F\setminus\{z\})\cup\{y\},\qquad F\mathbin\triangle\{y\}.             \tag{4}
\]

An exact integral max-flow assigns every tagged symbol to its best globally
balanced choice in (4). The optimal maximum fibres are:

\[
 \begin{array}{c|c|c|c}
 P & \text{absolute lower bound} & \text{menu optimum} & W\\ \hline
 \text{true }n=9\text{ minimizer} & 6610 & 6633 & 6984\\
 T_{4,2} & 296 & 298 & 336\\
 \text{convex }n=8 & 39056 & 39178 & 40320.
 \end{array}                                             \tag{5}
\]

Thus the one-label menu nearly attains the unrestricted counting lower bound,
but that bound itself is $(1-o(1))W$. The obstruction is output capacity,
not a poor local choice.

Exact verifier:

```text
python3 phase2/loop/erdos838/agent_post_collision_remapping/verify_post_collision_remapping.py
```

It exhausts all 6,984 shellings of the true nine-point minimizer, all 336
shellings of $T_{4,2}$, and all convex-polygon shellings through $n=8$.
It aggregates the local menus and proves the exact minimax loads by integer
max-flow. It also checks the unavoidable fractions for the nine-point and
36-point vertical Pascal squares.

## 1. The tagged ledger

Let $\mathcal S(P)$ be the extreme shellings of $P$. Assign arbitrary
weights $w_\sigma\ge0$ and put

\[
 W=\sum_{\sigma\in\mathcal S(P)}w_\sigma.               \tag{6}
\]

For a shelling $\sigma$, every transition $A\to A\setminus\{z\}$ exports
the nonempty caps of $A\setminus\{z\}$ in the radial $z$-chart. As proved
in the shelling-collision report, these local symbols are in bijection with
the non-singleton ordinary faces of $P$: a face is assigned when its first
member is deleted. Denote the resulting tagged ledger by $\mathcal D(P)$.
Its total weighted mass is exactly

\[
 \|\mathcal D(P)\|_w=W(V(P)-n).                          \tag{7}
\]

Each tag contains the complete shelling, transition, root, and cap subset.
Consequently, any rule based on finitely many future transitions is already a
function of a tag in $\mathcal D(P)$.

## 2. Arbitrary-remapping minimax theorem

Let a remapping distribute the mass of every tag among one or more ordinary
faces, with total outgoing mass equal to the tag weight. This includes
deterministic, randomized, globally optimized, and shelling-dependent rules.
Write $L(G)$ for the resulting load on the ordinary face $G$. Conservation
of mass gives

\[
 \sum_{G\in\mathcal F(P)}L(G)=W(V(P)-n).                 \tag{8}
\]

There are $V(P)$ outputs, so averaging proves

\[
 \max_G L(G)\ge W\frac{V(P)-n}{V(P)},                   \tag{9}
\]

which is (1). If only non-singleton outputs are legal, there are $V(P)-n$
of them and

\[
 \max_G L(G)\ge W.                                      \tag{10}
\]

The canonical decoder has load exactly $W$ on every non-singleton face, so
(10) is sharp.

All one-, two-, and three-point subsets are ordinary faces. This proves (2),
and hence (3). The conclusion is uniform over all planar order types; no
geometric regularity or minimizer hypothesis enters.

There is also an exact retention tradeoff. If a proposed decoder keeps only a
fraction $\rho$ of the total tagged mass, then

\[
 \max_G L(G)\ge
 \rho W\frac{V(P)-n}{V(P)}.                              \tag{11}
\]

Therefore an $o(W)$-fibre decoder must discard a $1-o(1)$ fraction of the
local cap ledger. A bounded-multiplicity selection cannot retain a positive
fraction of the recurrence mass.

## 3. Why extra transition labels do not evade the theorem

Suppose a rule reads the next $q=O(1)$ roots of the shelling. If those
labels are absorbed into a subset that is required to be an ordinary face,
the output space is still $\mathcal F(P)$, so (9) is unchanged. This covers
adding, deleting, toggling, or replacing $O(1)$ points.

If the output is instead a pair

\[
 (\text{ordinary face},\text{marked transition labels}),               \tag{12}
\]

then the larger codomain can reduce fibres, but (12) is not an ordinary face
and cannot be charged to $V(P)$. Forgetting the marks returns to (9).

A mixed cap-cup augmentation is even less favorable. If every cap tag is
paired with several cup choices, the tagged input mass increases while the
ordinary-face codomain remains $V(P)$. If one cup is selected
deterministically, the construction is simply another arbitrary remapping
covered by (9). Thus a cap-cup product helps only if a separate theorem turns
the marked pair into genuinely distinct countable ordinary faces.

## 4. The one-next-transition menu

For a non-singleton face $F$ and shelling $\sigma$, let
$z=z_\sigma(F)$ be the first member of $F$ deleted. Let $y$ be the
immediately following label in the full deletion permutation, including the
eventual survivor as its final label.

The four candidates in (4) have the following interpretations:

- $F$ is the canonical root-cap output;
- $F\cup\{y\}$ adds the next root when convexity survives;
- $(F\setminus\{z\})\cup\{y\}$ moves the rooted cap across the next seam;
- $F\mathbin\triangle\{y\}$ toggles the next label, using heredity when
  $y\in F$.

Invalid or empty candidates are removed. Tags with identical candidate sets
are aggregated. For a proposed load bound $M$, construct a flow network:

\[
 \text{source}\longrightarrow
 \text{menu types}\longrightarrow
 \text{ordinary faces}\longrightarrow\text{sink}.       \tag{13}
\]

The first capacities are menu multiplicities, menu-to-face edges permit the
valid candidates, and every face-to-sink edge has capacity $M$. Integral
max-flow decides whether load $M$ is feasible. Binary search gives the exact
minimum.

This optimization is deliberately stronger than a local deterministic rule:
it may coordinate all tags globally and split identical-menu multiplicities
among their outputs. Hence its failure to reach $o(W)$ is not an artifact of
greedy tie-breaking.

## 5. True nine-point minimizer

Here

\[
 (n,V,V-n,W)=(9,168,159,6984),                           \tag{14}
\]

so the domain has

\[
 W(V-n)=1{,}110{,}456                                   \tag{15}
\]

tagged symbols. The unrestricted all-face lower bound is

\[
 \left\lceil\frac{1{,}110{,}456}{168}\right\rceil=6610
 =0.94645\,W.                                            \tag{16}
\]

The one-label menus have 1,038 distinct types. Exact max-flow gives optimum

\[
 M_\star=6633=\frac{737}{776}W\approx0.94974W.           \tag{17}
\]

Thus this quite flexible noncanonical decoder comes within 23 of the absolute
counting lower bound, but cannot approach $o(W)$.

For comparison, choosing each mutation without global balancing gives:

| rule | changed tags | output faces used | maximum fibre |
|:---|---:|---:|---:|
| canonical | 0 | 159 | 6,984 |
| add next label | 330,120 | 159 | 11,712 |
| replace root by next | 1,007,514 | 167 | 13,968 |
| toggle next label | 716,112 | 168 | 6,984 |

Mutation frequency is not the issue: root replacement changes more than 90%
of all tags, yet worsens maximum congestion.

## 6. Pascal and vertical towers

For the six-point Pascal cell $T_{4,2}$,

\[
 (V,V-n,W)=(50,44,336).                                  \tag{18}
\]

The absolute all-face lower bound is 296. The one-label menu has 191 types
and exact optimum 298, compared with the canonical load 336. The four direct
map maxima are respectively

\[
 336,\qquad600,\qquad672,\qquad336.                      \tag{19}
\]

Again, global mutation nearly saturates the counting obstruction but leaves
fibre $298=(149/168)W$, not $o(W)$.

For the nine-point homogeneous square $T_{3,1}[T_{3,1}]$,

\[
 (V,W)=(273,64{,}560).                                   \tag{20}
\]

Before imposing any local-menu restriction, (1) already forces maximum fibre

\[
 \left\lceil64{,}560\frac{264}{273}\right\rceil
 =62{,}432=0.96704\,W.                                   \tag{21}
\]

The canonical 36-point square $T_{4,2}[T_{4,2}]$ has $V=441{,}399$.
For any shelling weight $W$, every total ordinary-face remapping has a fibre
of weight at least

\[
 \frac{441{,}399-36}{441{,}399}W
 =\frac{147121}{147133}W
 >0.999918W.                                             \tag{22}
\]

Thus the obstruction becomes stronger, rather than weaker, in the vertical
tower regime.

## 7. Convex polygons: scalable exact calibration

For a convex $n$-gon, every nonempty subset is an ordinary face and every
permutation is an extreme shelling:

\[
 V=2^n-1,\qquad W=n!.                                    \tag{23}
\]

The exact one-label max-flow results are:

| $n$ | tagged symbols | absolute lower bound | menu optimum | $W=n!$ |
|---:|---:|---:|---:|---:|
| 4 | 264 | 18 | 18 | 24 |
| 5 | 3,120 | 101 | 102 | 120 |
| 6 | 41,040 | 652 | 657 | 720 |
| 7 | 604,800 | 4,763 | 4,788 | 5,040 |
| 8 | 9,959,040 | 39,056 | 39,178 | 40,320 |

The unrestricted ratio is

\[
 \frac{V-n}{V}=1-\frac{n}{2^n-1}\longrightarrow1.       \tag{24}
\]

The menu optimum follows the same trend. Convex polygons therefore give a
fully stretchable, arbitrarily large barrier to any claim that finitely many
future root labels can spread the full ledger over ordinary faces with
sub-shelling fibre.

## 8. Exact remaining option

The counting theorem leaves only two routes:

1. retain $o(1)$ of the tagged cap mass and prove that this sparse selection
   still carries the full $K_{n,1}$ curvature; or
2. construct a genuinely larger family of independently countable geometric
   objects, together with an injection back into ordinary faces that does not
   forget the extra labels.

The first route requires a new concentration theorem. The second cannot use
marked faces or cap-cup pairs merely as formal metadata, because forgetting
those marks restores the minimax bound (1). Adding or replacing $O(1)$
shelling labels inside a single ordinary output is now ruled out sharply.
