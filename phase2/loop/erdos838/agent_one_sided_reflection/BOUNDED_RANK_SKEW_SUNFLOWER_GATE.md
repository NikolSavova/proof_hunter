# Bounded-rank anti-alignment: a recoverable sunflower gate

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

Quadratic cap/cup anti-alignment cannot live inside one rank-
`O(log D)` sunflower petal.  If a petal has rank `p`, its directional
skew lies in an interval of length less than `p`.  Unit-width bucketing
therefore retains a `1/(p+1)` fraction of any petal family and loses at
most a factor two in every forward cap--cup product.  This is polynomial
regularization, not a `2^{o((log D)^2)}` thinning.

There are also two exact global consequences.  A quadratic-entropy,
rank-`q` family whose compatibility graph has fixed-power maximum degree
can be partitioned, apart from a quadratically negligible remainder,
into power-size pairwise-incompatible sunflowers.  First try extending one
whole completion by one label of another petal.  Such mixed faces have an
automatic `(q+1)`-decoder.  Hence either they give a fixed-power bank, or a
power-size set of petal labels shares one fixed planar four-circuit carrier
triple.

If the petals in the resulting rooted containers admit a **recoverable
two-ended gluing**, then their cap--cup
banks have aggregate size

\[
       \left|\mathcal B\right|
       \ge {M h\over 8(q+1)^2\Lambda},                    \tag{1}
\]

where `M` is the covered completion mass, `h` is the sunflower size, and
`Lambda` is the global representation multiplicity of the glued faces.
For `h=D^rho`, this is a fixed-power expansion whenever
`Lambda<=D^(rho-epsilon)`.  The geometric hypothesis is deliberately
weaker than a full substitution-module theorem: only the indicated
two-petal endpoint traces must glue, and only their aggregate decoder is
used.

Thus cap/cup skew is not the final anti-alignment obstruction in the
bounded-rank branch.  The remaining issue is to obtain the two-ended
gluing with subpower global reuse inside the all-bad rooted containers.  A
scalable exact ACP construction
shows that such reuse does not follow from rank, quadratic core entropy,
the three projection minimum degrees, or the rooted `1+3` circuit alone.
All sunflower groups can reuse the same untagged two-petal faces with
quadratic multiplicity.  In that construction the core labels form one
convex outer shield, whose Boolean complex pays enormously; hence it is
not a Hall-dense regression and does not contradict the desired theorem.

For coefficient scale, ordinary skew and size bucketing are likewise
only polynomial losses once a genuine positive-log-scale block system is
available.  Disjoint layers of a laminar reset chain automatically have a
scale-covering dyadic class.  What is not automatic is that those layers
are geometric substitution modules, or that the induced macro core has
the required high mean rank.  This isolates the exact structural target.

Exact verifier:

```bash
python3 phase2/loop/erdos838/agent_one_sided_reflection/verify_bounded_rank_skew_sunflower.py
```

## 1. A bounded-rank petal has only linear skew

Let `Q` be a `p`-point set in convex position.  Fix a generic direction,
and let `C(Q),U(Q)` be its nonempty cap and cup counts in that direction.
Write `W(Q)` for its nonempty ordinary-face count and

\[
                 \sigma(Q)={1\over2}\log{U(Q)\over C(Q)}. \tag{2}
\]

The upper/lower boundary-chain encoding of an ordinary face is injective,
so

\[
                         C(Q)U(Q)\ge W(Q).                 \tag{3}
\]

Since `Q` itself is in convex position,

\[
 W(Q)=2^p-1,qquad p\le C(Q),U(Q)\le2^p-1.                \tag{4}
\]

Consequently

\[
             |\sigma(Q)|\le {p-\log p\over2},             \tag{5}
\]

so all possible skews occupy an interval of length less than `p`.

> **Lemma 1 (polynomial skew binning).**  Among any `h` convex petals of
> common rank `p`, there is a subfamily `I` of size
> \[
>                         |I|\ge {h\over p+1}              \tag{6}
> \]
> whose skews lie in one half-open interval of width one.  For every
> ordered $i,j\in I$,
> \[
>             C(Q_i)U(Q_j)\ge {1\over2}
>                    \sqrt{W(Q_i)W(Q_j)}
>                 ={2^p-1\over2}.                         \tag{7}
> \]

**Proof.**  Partition the interval in (5) into at most `p+1` unit
intervals and pigeonhole.  The exact identity

\[
 \log(C_iU_j)=\tfrac12\log(C_iU_i)
              +\tfrac12\log(C_jU_j)+\sigma_j-\sigma_i   \tag{8}
\]

together with (3) and `sigma_j-sigma_i>-1` proves (7).  QED.

In particular, if `p<=q<=kappa log D`, a petal skew is only
`O(log D)`.  A `Theta((log D)^2)` skew can occur only after many petals or
core histories have already been aggregated into a larger child.  It
cannot be attributed to an individual bounded-rank completion.

## 2. Almost all completions split into power-size sunflowers

The following covering form is slightly stronger than extracting one
sunflower.  It is useful because a global Hall bank must account for most
of the record mass.

> **Lemma 2 (independent sunflower decomposition).**  Let $\mathcal C$ be
> a family of `M` sets of rank at most `q`, and join two members when they
> are compatible.  If the compatibility graph has maximum degree `Delta`,
> then for every integer `h>=2`, all but at most
> \[
>       (q+1)(\Delta+1)q!(h-1)^q                            \tag{9}
> \]
> members of $\mathcal C$ can be partitioned into `h`-member sunflowers,
> each of which is pairwise incompatible.  Within a sunflower
> \[
>                    C_i=K\mathbin{\dot\cup}Q_i,           \tag{10}
> \]
> where the nonempty petals `Q_i` are pairwise disjoint and have one
> common rank `p`.

**Proof.**  Partition first by rank, and properly color every resulting
compatibility graph with at most `Delta+1` colors.  Every color class is
independent.  In each class, repeatedly remove an `h`-sunflower while its
size exceeds `s!(h-1)^s`, where `s` is the common rank.  The
Erdos--Rado sunflower bound guarantees the next removal.  At termination
each of the at most `(q+1)(Delta+1)` classes leaves at most
`q!(h-1)^q` members.  Distinct sunflower members have nonempty petals;
uniformity makes their petal ranks equal.  QED.

Put `D=2^L`.  If

\[
 M\ge2^{aL^2},\qquad q\le\kappa L,qquad
 \Delta\le D^c,                                          \tag{11}
\]

then for every fixed `rho<a/kappa`, choosing `h=floor(D^rho)` makes the
logarithm of (9) at most

\[
                         \kappa\rho L^2+o(L^2).            \tag{12}
\]

Thus the decomposition covers `(1-o(1))M` members.  The fixed-power
compatible-degree deletion and the rank partition cost only `O(L log L)`
bits, not quadratic entropy.

## 3. A globally decodable mixed-extension dichotomy

Before using endpoint profiles, there is a cheaper mixed extension with an
automatic global decoder.  For one sunflower write its completions as

\[
                         C_i=K\mathbin{\dot\cup}Q_i
                         \qquad(1\le i\le h).               \tag{13a}
\]

For every ordered $i\ne j$ and every $b\in Q_j$, test whether
$C_i\cup\{b\}$ is ordinary.  Call such a tuple a **good extension**.

> **Theorem 3 (mixed extension or a common rooted circuit).**  Let a
> collection of `h`-sunflowers cover `M_0` distinct completions of rank at
> most `q`, and assume `h>=4`.  Then one of the following holds.
>
> 1. The ordinary mixed extensions contain a bank of at least
>    \[
>             {M_0(h-1)\over4(q+1)}                       \tag{13b}
>    \]
>    distinct faces.
> 2. Sunflowers covering at least `M_0/2` completions each contain a fixed
>    completion $C_i$, a fixed triple $T\subseteq C_i$, and a set $B$ of
>    labels from the other disjoint petals, of size
>    \[
>             |B|\ge {h-1\over8{q\choose3}},              \tag{13c}
>    \]
>    such that every $T\cup\{b\}$, $b\in B$, is a bad four-circuit with
>    the same hidden role.  Thus either every $b$ is inside
>    $\operatorname{conv}T$, or one fixed $t\in T$ is inside
>    $\operatorname{conv}((T\setminus\{t\})\cup\{b\})$ for every $b\in B$.

If the second branch occurs then necessarily `q>=3`; for `q<3` every
one-label extension of an ordinary completion is ordinary.

**Proof.**  A face $F=C_i\cup\{b\}$ has at most $|F|\le q+1$
representations: choose $b\in F$, after which $C_i=F\setminus\{b\}$ is
determined.  Since the completions were globally partitioned into
sunflowers, $C_i$ also determines its sunflower and its petal.  This proves
the `(q+1)` decoder.

A sunflower of petal rank `p>=1` has exactly `h(h-1)p` tested ordered
extensions.  Call it good if at least half are ordinary.  If good
sunflowers cover at least `M_0/2` completions, their good-extension
representations number at least

\[
       {M_0\over2h}\,{h(h-1)p\over2}
             \ge {M_0(h-1)\over4}.                        \tag{13d}
\]

Divide by `q+1` to obtain (13b).

Otherwise bad sunflowers cover at least `M_0/2` completions.  In one of
them, some $C_i$ has at least $(h-1)p/2$ failed extension labels.  For each
failure, planar Caratheodory gives a bad four-subset of $C_i\cup\{b\}$.
It must contain $b$, since $C_i$ is ordinary.  Choose one canonically.
There are at most $\binom q3$ carrier triples in $C_i$, so one triple $T$
occurs for at least $(h-1)p/[2\binom q3]$ distinct labels $b$.  In a
general-position planar four-circuit exactly one of its four labels is
hidden.  Pigeonholing the four possible hidden roles and using `p>=1`
gives (13c).  The two displayed geometric forms are exactly the cases in
which the hidden label is $b$ or a fixed member of $T$.  QED.

For `h=D^rho` and `q=O(log D)`, branch 1 is already a
`D^{rho-o(1)}` expansion.  Branch 2 gives a positive-power rooted circuit
container of size `D^{rho-o(1)}` in every bad sunflower.  No cap/cup skew
has entered.  The remaining problem is to charge those containers across
sunflowers without erasing their carrier/core histories.

### 3.1 Exact interface with cap-weighted Jensen demand

The same argument has a weighted form, but it exposes one unavoidable
multiplicity.  Restrict to sunflowers of one petal rank $p$; partitioning
by petal rank costs at most a factor `q`.  Give completion $C_i$ a
positive demand weight $w_i$, and
suppose first that all weights lie in one dyadic band

\[
                              w\le w_i<2w.                 \tag{13e}
\]

Let $d_i$ be the number of labels in other petals which extend $C_i$ to an
ordinary face, and let $W_0=\sum_i w_i$ over all covered completions.

> **Theorem 3W (weighted extension/circuit gate).**  Under (13e), either
> \[
>       |\mathcal B|\ge
>          {W_0(h-1)p\over8w(q+1)},                       \tag{13f}
> \]
> or carrier completions of total weight at least $W_0/6$ each have a
> common-role circuit container of size at least
> \[
>                    { (h-1)p\over16\binom q3}.            \tag{13g}
> \]

**Proof.**  Call a sunflower weighted-good when

\[
                 \sum_i w_i d_i\ge{(h-1)p\over2}\sum_i w_i. \tag{13h}
\]

If weighted-good sunflowers carry at least half of $W_0$, the total
weighted number of good representations is at least
$W_0(h-1)p/4$.  A fixed output face has at most `q+1`
representations, and every representing completion has weight less than
`2w`.  Its total representation weight is therefore less than
`2w(q+1)`.  Division proves (13f).

Otherwise weighted-bad sunflowers carry at least half of $W_0$.  In one
such sunflower put $f_i=(h-1)p-d_i$.  Equation (13h) fails, so
$\sum_i w_i f_i>(h-1)p\sum_i w_i/2$.  The indices with
$f_i\ge(h-1)p/4$ carry at least one third of the sunflower weight: otherwise
the weighted average of $f_i$ is at most
$(2/3)((h-1)p/4)+(1/3)(h-1)p=(h-1)p/2$.
For every retained $i$, repeat the carrier-triple and hidden-role
pigeonholes in Theorem 3.  They leave at least
$f_i/[4\binom q3]$, proving (13g).  Summing the retained carrier weights
over weighted-bad sunflowers gives at least $W_0/6$.  QED.

The denominator $w$ in (13f) is real.  The face $C_i\cup\{b\}$ records a
completion once, not $w_i$ times.  Dyadic weight bucketing can make the
weights comparable, but it cannot turn one face into multiple units of
capacity.  For unrestricted weights, a level carrying a fraction
`1/B_w` of $W_0$ can be selected if there are $B_w$ occupied dyadic
levels; both the factor $B_w$ and the band maximum $w$ remain.

There is a second, independent support loss.  If a dyadic band has support
size $M_b$ and total weight $W_b$, the remainder (9) has weight at most

\[
 2w(q+1)(\Delta+1)q!(h-1)^q.                            \tag{13h1}
\]

Thus Lemma 2 preserves `(1-o(1))W_b` precisely when its cardinal remainder
is `o(M_b)`.  A large Jensen sum by itself does not imply this: one atom of
weight $W_0$ has arbitrarily large weighted demand and no sunflower at all.
The three-projection minimum degree controls unweighted incidence support,
but an additional cap on reciprocal capture, or a proof that the Jensen
mass is spread over a quadratic-entropy dyadic band, is needed to enter
Theorem 3W.

For the radial Jensen sum the distinction is exact.  The quantities
$q_{j,e}$ already aggregate all actual parents and histories having endpoint
state $(j,e)$.  To invoke Lemma 2 one must disaggregate them into **distinct
completion sets**.  Repeated histories of the same completion become its
weight $w_i$; they do not become new sunflower vertices.  If they are
instead treated as labelled copies, the mixed-face decoder acquires their
maximum history multiplicity $H$ and (13f) has the additional denominator
$H$.  Thus the entropy needed by the sunflower lemma is entropy of distinct
parent cores, not entropy of radial histories.  This is the same
history-erasure loss seen in the reset-chain regressions, now at the exact
weighted interface.

There is exactly one way to remove this loss.  Suppose completion $C_i$
has a family $\mathcal T_i$ of at least $w_i$ cap/interval-cage tags, every
tag coexists with every good extension label, and the resulting tagged
face has global decoder multiplicity at most $\Lambda$.  Then the same
count gives

\[
             |\mathcal B_{\rm tagged}|
                 \ge {W_0(h-1)p\over4\Lambda}             \tag{13i}
\]

on the weighted-good half, with no dyadic maximum.  Thus a Jensen lower
bound such as $\sum q_{j,e}/\lambda_e$ can be consumed by the sunflower
gate only if the reciprocal-capture/cap weight is realized by a
**coexisting recoverable tag reservoir**.  Treating $1/\lambda_e$ as a
scalar weight gives (13f), not (13i).  Shared interval cages reappear
precisely as the decoder multiplicity $\Lambda$.

### 3.2 Conditioning on the common interval face

The global Jensen demand has a stronger localization than arbitrary weight
binning.  For an interval face $W$, put

\[
 \eta_e=\sum_{j:W\subseteq I_e}h_{j,e},\qquad
 H_W=\sum_e\eta_e,qquad \eta_*=\max_e\eta_e.             \tag{13j}
\]

The exact common-target load identity from
`agent_outer_internal_product/TWO_REFERENCE_HALL_DEMAND_GATE.md` is

\[
 \ell(W)={1\over4}H_W,qquad
 \sum_jS_j=\mathbb E_{W\sim\pi}\ell(W).                  \tag{13k}
\]

Thus a large Jensen demand can fix one actual $W$ without a dyadic loss.
The following is what the sunflower gate gives after that conditioning.

> **Theorem 3C (common-target mixed face or rank-two circuit
> sunflower).**  Let $W$ be an ordinary face of rank $w$, and let
> $e=(a,b)$ range over distinct endpoint pairs whose open intervals contain
> $W$, with loads $\eta_e>0$.  If $H_W>0$, then either
>
> 1. the ordinary faces $W\cup e$ form a bank of size at least
>    \[
>                          {H_W\over2\eta_*},              \tag{13l}
>    \]
>    or
> 2. there is a circuit cell of load at least
>    \[
>          {H_W\over16(\binom w2+\binom w3)}              \tag{13m}
>    \]
>    and distinct endpoint-pair support at least
>    \[
>          m_W:={H_W\over
>             16\eta_*(\binom w2+\binom w3)}.             \tag{13n}
>    \]
>    Every pair in the cell has a bad four-circuit with one fixed trace
>    $A\subseteq W$, $|A|\in\{2,3\}$, one fixed hidden role, and, when
>    $|A|=3$, one fixed choice of the left or right endpoint.  The endpoint
>    pairs in this cell contain either a star or a matching of size at
>    least $\sqrt{m_W/2}$.  Equivalently, they contain a rank-two
>    sunflower of that size, with common core respectively one endpoint or
>    the empty set.

For `w<=1` the second branch is empty, since every set of at most three
points is ordinary.

**Proof.**  Split the load according to whether $W\cup e$ is ordinary.  If
the ordinary side has load at least $H_W/2$, it uses at least
`H_W/(2 eta_*)` distinct pairs.  The faces are distinct, because $W$ is
fixed and $e=(W\cup e)\setminus W$.  This proves (13l).

Otherwise the bad side has load at least $H_W/2$.  For every bad pair,
choose a canonical bad four-subset of $W\cup e$.  It meets both $W$ and
$e$, since each is ordinary separately.  As $|e|=2$, its trace on $W$ has
rank two or three.  There are at most

\[
                     8\left(\binom w2+\binom w3\right)    \tag{13o}
\]

choices of the trace, hidden role, and endpoint side.  One cell therefore
has the load in (13m), and division by $\eta_*$ gives (13n).

The endpoint pairs form a simple bipartite graph between labels to the
left and right of $W$.  If its maximum degree is at least
$\sqrt{m_W/2}$, there is the asserted star.  Otherwise a maximal matching
has size at least `m_W/(2 Delta)>sqrt(m_W/2)`, because the endpoints of a
maximal matching cover every edge.  This proves the final assertion.  QED.

There is one apparent degeneracy in the final rank-two sunflower, but it
also has an exact resolution.  If $|A|=3$, only one endpoint of $e$ occurs
in the fixed circuit.  A star could be centered at this active endpoint,
so initially only the unused endpoints vary.  Let the star have size $t$
and call its unused endpoints $c_1,\ldots,c_t$.  Test the one-ended sets
$W\cup\{c_i\}$.  Either at least `t/2` are ordinary, giving that many
distinct $W$-retaining faces, or at least `t/2` are bad.  In the latter
case every canonical bad circuit has three labels in $W$ and the label
$c_i$; pigeonholing its trace and hidden role leaves at least

\[
                         {t\over8\binom w3}               \tag{13p}
\]

distinct $c_i$ in one common rooted interior/exterior circuit.  In all
other matching/star cases, a circuit endpoint already varies on all
$t$ members.  Thus a rank-two circuit sunflower always yields either a
further $W$-retaining face bank or, at polynomial loss, a genuinely varying
rooted circuit alphabet.

When $w=O(\log n)$, the trace denominator in (13m)--(13p) is polynomial.
Hence fixed-power common-target load has only two escapes: one endpoint
cell has fixed-power radial history multiplicity $\eta_*$, or a
fixed-power rooted circuit alphabet survives.  In the three-point trace
case it is a common rooted interior/exterior alphabet after the preceding
star refinement.  In the two-point trace case it is a fixed-root `2+2`
endpoint circuit family.

Theorem 3C does **not** yet make the resulting shield faces retain the full
$W$.  Indeed its bad branch starts from the fact that $W\cup e$ is not
ordinary.  Only the carrier trace $A\subseteq W$ is guaranteed to coexist
in the bad circuit.  Reattaching $W\setminus A$ may recreate other
circuits.  Thus conditioning on $W$ eliminates weight bucketing and fixes
the target, but the precise remaining decoder loss is erasure of
$W\setminus A$ during the rooted shield release.  A proof must either keep
that discarded trace in a second recoverable face or charge its face
complex before descending.

There is nevertheless an unconditional detached shield at this point,
independent of compatibility.

> **Corollary 3D (cubic endpoint shield versus one heavy cell).**  With
> the notation of Theorem 3C, the union of the endpoint labels contains a
> subset $X$ of size
> \[
>                         |X|\ge\sqrt{H_W/(2\eta_*)}.       \tag{13q}
> \]
> Every subset of $X$ of rank at most three is ordinary, and hence, for
> $|X|\ge3$,
> \[
> F_X(1/2)\ge{\binom{|X|}{3}\over8}
>             \ge {|X|^3\over288}.                        \tag{13r}
> \]
> In particular this detached half-Gibbs reservoir is at least the full
> normalized demand contributed by the common target $W$ whenever
> $H_W/(2\eta_*)\ge9$ and
> \[
> \eta_*\le
> {H_W^{1/3}2^{2(w+2)/3}\over2\,288^{2/3}}.               \tag{13s}
> \]

**Proof.**  The endpoint graph has at least $H_W/\eta_*$ distinct edges.
Apply the star/matching argument in Theorem 3C to the whole graph.  The
varying leaves of a star, or one side of a matching, give (13q).  General
position makes every triple ordinary, and
`(s-1)(s-2)>=s^2/6` for `s>=3`, proving (13r).

The common target contributes

\[
 \pi(W)\ell(W)={H_W2^{-(w+2)}\over F(P;1/2)}              \tag{13t}
\]

to the Jensen Hall demand, whereas the detached shield has normalized
capacity $F_X(1/2)/F(P;1/2)$.  Substitute (13q) into (13r); inequality
(13s) is exactly the condition that the latter capacity is at least
(13t).  QED.

Thus after fixing $W$, diffuse endpoint load already creates a detached
rank-three shield; failure of that shield inequality forces one endpoint
pair to carry at least the right side of (13s) in cumulative radial tilt.
The circuit localization in Theorem 3C remains useful because the same
detached $X$ may be reused by many different common targets in a global
Hall family.  It retains a fixed trace of $W$ and identifies the precise
rooted fibre in which such cross-target reuse must be resolved.

## 4. The weakest two-ended extraction that gives a fixed-power bank

Consider any collection $\Gamma$ of the sunflowers produced by Lemma 2.
For $g\in\Gamma$, let its petals be $Q_{g,1},\ldots,Q_{g,h}$, in a specified
geometric order, and let `p_g` be their common rank.  Each petal is a
subset of an ordinary completion and hence is itself in convex position.

We say that $\Gamma$ has a **two-ended gluing of multiplicity $\Lambda$** if
for every $g$ and every ordered pair $i<j$ in the skew bin supplied by
Lemma 1, every union of

* a cap in $Q_{g,i}$,
* a cup in $Q_{g,j}$, and
* the prescribed fixed tag for cell $g$

is an ordinary face, and every ordinary face is obtained from at most
$\Lambda$ such tuples $(g,i,j,\mathrm{cap},\mathrm{cup})$.  The tag may be empty.  No union of
whole petals, no product coordinate system, and no compatibility between
three petals is assumed.

> **Theorem 4 (recoverable two-ended sunflower bank).**  Suppose every
> sunflower in $\Gamma$ has size `h>=4(q+1)`, and together they cover `M_0`
> completions.  A two-ended gluing of multiplicity `Lambda` produces an
> ordinary face bank satisfying
> \[
>        \boxed{|\mathcal B|\ge
>             {M_0h\over8(q+1)^2\Lambda}.}                \tag{13}
> \]

**Proof.**  In a sunflower of petal rank `p`, Lemma 1 gives
`s>=h/(p+1)>=h/(q+1)` petals in one skew bin.  Since `s>=4`,
`binom(s,2)>=s^2/4`.  Equation (7) gives at least `(2^p-1)/2>=1/2`
endpoint choices for every ordered petal pair.  Hence this sunflower has
at least

\[
                 {h^2\over8(q+1)^2}                       \tag{14}
\]

two-ended representations.  There are `M_0/h` sunflowers.  Sum (14) and
divide by the asserted maximum representation multiplicity `Lambda`.
QED.

Combining Lemma 2 and Theorem 4 gives the promised fixed-power gate.  Under
(11), choose any `rho<a/kappa`.  If the recovered two-ended bank has

\[
                        \Lambda\le D^{\rho-\epsilon},      \tag{15}
\]

then

\[
                        |\mathcal B|\ge
                  M D^{\epsilon-o(1)}.                    \tag{16}
\]

Thus, after the compatible-union branch has been deleted, the only way a
quadratic completion family can remain Hall-dense is for every power-size
sunflower decomposition to fail two-ended gluing or to reuse its glued
faces with essentially the whole `D^rho` multiplicity.  Quadratic
cap/cup skew is not a third possibility: Lemma 1 has already removed it at
polynomial cost.

The decoder in Theorem 4 is load-bearing.  Pairing the bank with one source
face and applying Cauchy would in general give only a `V(P)^2` statement,
not the linear Hall expansion (13).

## 5. Positive-log-scale modules: skew is again free

For completeness, here is the coefficient-scale version.  Suppose a
geometric extraction gives disjoint substitution modules `Q_1,...,Q_r`
inside an ordered macro `S`, with total size `N`, and suppose
`log W(P)<=C(log N)^2`.  Dyadically bin the module sizes.  In a fixed size
bin, every skew lies in an interval of length at most `C(log N)^2`.
Partition that interval into windows of width `log N`.  There are only
`O_C(log N)` skew windows.  Hence size and skew binning together cost a
polynomial factor and produce an induced core `I` with

\[
 \log|I|+\log n_I=\log N-o(\log N),\qquad
 D_I=O(\log N)=o((\log N)^2).                            \tag{17}
\]

If both terms on the left are positive fractions of `log N` and the
induced macro satisfies

\[
 \log V_2(S[I])\ge(c-o(1))(\log|I|)^2,quad
 \mu_2(S[I])\ge\log|I|-o(\log N),                        \tag{18}
\]

while the children satisfy the corresponding coefficient-`c` lower
bound, Theorem 4a of `agent_upper_jump/REPORT.md` gives

\[
 c_{\rm out}\ge c+(1-2c)
 {\log|I|\log n_I\over(\log N)^2}-o(1).                  \tag{19}
\]

This is a strict upper jump for `c<1/2`.  Notice that (17), including the
skew conclusion, is automatic **after** actual modules exist.

There is a useful laminar specialization.  If a strict reset chain has
pairwise-disjoint discarded layers `Q_i` whose union has size `N_0`, then
some dyadic size class satisfies

\[
             |I|\min_{i\in I}|Q_i|
                  \ge {N_0\over2(1+\log N_0)}.             \tag{20}
\]

Indeed the dyadic classes partition total layer mass.  A further skew bin
costs only `O(log N_0)`.  Therefore a laminar reset chain automatically
supplies the scale-covering arithmetic in (17).  The missing assertions
are geometric: its discarded layers need not be substitution modules, and
their induced macro need not obey (18).  If one logarithmic scale in (20)
is `o(log N_0)`, it is the already-known one-scale/fine-mesh boundary, not
a cap/cup anti-alignment failure.

## 6. A bounded-rank ACP overlap regression, paid by an exposed shield

The global decoder cannot be inferred from the local rooted circuit.  Here
is an exact scalable construction which keeps the full singleton-ear ACP
tuple and rank `O(log D)`.

Let `u=(-1,0),v=(1,0)`.  Put `N` points `O` on the strictly concave arc
`y=1-x^2` between `u` and `v`; then `O union {u,v}` is in convex position.
Below `uv`, put a totally nested sequence `Z`, so that for its outer-to-
inner order

\[
             z_j\in\operatorname{int}\triangle uvz_i
                         \qquad(i<j).                      \tag{21}
\]

All inequalities are strict, so the points can be chosen rationally in
general position.  Partition an outer segment of `Z` as blockers `Y` and
a later inner segment as ears `X`.  For every $s$-subset $S\subseteq O$, put

\[
                         R_S=\{u,v\}\cup S.                \tag{22}
\]

Then, for every $x\in X,p\in Y$,

\[
 R_S\cup\{x\},\ R_S\cup\{p\}\text{ are ordinary},
 \qquad
 \operatorname{ext}(R_S\cup\{x,p\})=R_S\cup\{p\}.       \tag{23}
\]

Thus `(R_S,x,p)` is an actual singleton-ear source/blocker/repaired-target
record.  Its three projection degrees are exactly

\[
 |Y|,qquad |X|,qquad {N\choose s}.                       \tag{24}
\]

For fixed `R_S`, every pair of distinct completions using `Z` is
incompatible, with the same rooted `1+3` circuit on `u,v`.  Yet an untagged
two-singleton face `{z_i,z_j}` is independent of `S`.  Across all cores it
has representation multiplicity

\[
                              {N\choose s}.                \tag{25}
\]

Take `N=floor(D^delta)` and `s=floor(kappa log D)`.  Then

\[
 \log {N\choose s}=\kappa\delta(\log D)^2
                      -O((\log D)\log\log D),              \tag{26}
\]

while every source has rank `s+3=O(log D)`.  Both mark alphabets may have
fixed-power size.  Projective universality permits the nested child `Z` to
carry any prescribed internal order type, and reflection changes its
directional profile without changing (21)--(24).  Hence local ACP signs do
not control aggregate child skew or the decoder multiplicity.

This is **not** a Hall regression.  The outer set `O union {u,v}` is a
convex shield, so

\[
                         V(P)\ge2^{N+2}-1,                  \tag{27}
\]

which dwarfs the `2^{Theta((log D)^2)}` record mass.  It lies exactly in
the exposed-shield branch of `AGGREGATE_CIRCUIT_SHIELD_ANTI_ALIGNMENT.md`.
The example proves only that a bounded-overlap two-ended decoder needs the
Hall/exposed-shield hypothesis; it cannot be deduced pointwise from the
rooted circuit or from the three projection degrees.

## 7. Exact remaining statement

After the existing exposed-shield theorem and the results above, the final
anti-alignment target can be stated without cap/cup ambiguity:

> In a Hall-dense, three-projection-minimum-degree ACP family with
> rank `O(log D)` and quadratic conditional core entropy outside all
> exposed convex shields, extract a power-size sunflower decomposition for
> which either the compatible-union bank or the mixed whole-completion
> extension bank fires, or the resulting common-triple circuit containers
> have petal endpoint traces with two-ended gluing multiplicity
> `D^{rho-epsilon}` smaller than the sunflower size.

Theorem 4 would then give the fixed-power Hall expansion.  A positive-log-
scale module or laminar-layer extraction satisfying (18) would instead
give the coefficient-`1/2` upper jump.  The ACP regression in Section 5
shows why the phrase “outside all exposed shields” and the global decoder
bound are both essential.  No bounded-rank, Hall-dense planar regression
with quadratic hidden entropy is produced here.
