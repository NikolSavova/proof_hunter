# What exact regularization would be enough for Erdős 838, and what the
# known extraction tools lose

All logarithms are base two.  Write `V(P)` for the number of convex-position
subsets of a planar point set `P`, including or excluding the empty set (the
difference is irrelevant below).  This note records one new structural
dichotomy and two exact exponent-transfer calculations.

The conclusion is negative but sharp: the newly proved `1/2` theorem for
strong-decomposition trees cannot be transferred by a black-box
same-type/mutually-avoiding extraction of the currently known strength.
A successful full-problem proof must retain almost all logarithmic scale, or
use multiplicity across many extracted pieces rather than pass to one exact
structured subset.

## 1. Quadratic exponents square the extraction loss

The elementary transfer rule is worth stating explicitly.

> **Extraction transfer.**  Suppose every `n`-point set in a class contains
> a subset `Q` of size
> \[
> |Q|\ge n^{\alpha-o(1)}                         \tag{1}
> \]
> belonging to a structured class for which
> \[
> \log V(Q)\ge(c-o(1))(\log |Q|)^2.              \tag{2}
> \]
> Then this route proves only
> \[
> \log V(P)\ge(c\alpha^2-o(1))(\log n)^2.        \tag{3}
> \]

This is just substitution of (1) into (2), but it is a severe constraint
for a quadratic-scale problem.  With the new strong-tree constant `c=1/2`,
a polynomial-size extraction beats the existing general coefficient `1/4`
only if

\[
 \alpha>{1\over\sqrt2},                          \tag{4}
\]

and it preserves the conjectural coefficient `1/2` only if `alpha=1-o(1)`.
The classical mutually-avoiding-pair theorem gives two sets of order
`sqrt(n)`; even if their union were optimistically granted the full
strong-tree theorem, (3) would give only `1/8`.

## 2. A strong-subtree / balanced-pair dichotomy

The preceding square-law might conceivably be evaded by extracting a very
large but extremely unbalanced strong tree.  The following lemma shows that
such imbalance itself creates convex multiplicity.

> **Lemma (comb-or-balanced-strong-pair).**  Let `Q` be a strongly
> decomposable `q`-point subset of an arbitrary ambient point set `P`.  For
> every integer `h>=1`, at least one of the following holds:
>
> 1. `V(P)>=2^h`;
> 2. `P` contains a strong pair `A prec B` with
>    \[
>      |A|,|B|\ge {q\over4h}.                    \tag{5}
>    \]
>
> In particular `A,B` are mutually avoiding.

### Proof

Follow a larger child in the strong-decomposition tree of `Q`, stopping
when the current subtree first has fewer than `q/2` leaves.  Let `t` be the
number of discarded siblings and let their sizes be `s_1,...,s_t`.

If `t>=2h`, at least `h` of these siblings are attached on the same side of
the followed path.  Fix one point in each of those siblings and one terminal
point below the stopping node.  Every subset of the fixed sibling points,
together with the terminal point, is a pure cap or a pure cup.  These `2^h`
sets are distinct and convex, proving alternative 1.

Otherwise `t<2h`.  Since the stopping subtree has fewer than `q/2` leaves,

\[
 \sum_{i=1}^t s_i>q/2.                           \tag{6}
\]

Hence some discarded sibling has size greater than `q/(2t)>q/(4h)`.
Immediately before it was discarded the current subtree still had at least
`q/2` leaves, and the followed child was larger, so that child has at least
`q/4>=q/(4h)` leaves.  The two children at this node form a strong pair,
which proves (5).

Finally, a strong pair is mutually avoiding: every line through two points
of either child places the entire other child in one strict open half-plane,
and therefore misses its convex hull.  This completes the proof. `square`

The useful conditional form is obtained by taking
`h=floor(log V(P))+1`: any `q`-point strong subset inside a point set with
only quasipolynomially many convex subsets forces a mutually avoiding pair
of size

\[
 \Omega\left({q\over\log V(P)}\right)
 =\Omega\left({q\over(\log n)^2}\right)          \tag{7}
\]

in the regime relevant to Problem 838.

This makes the regularization gap concrete.  Strong glues are not merely a
convenient sufficient condition: after excluding the already-favorable
pure-comb explosion, any large exact strong tree contains a nearly balanced
mutually avoiding pair.  Aronov--Erdős--Goddard--Kleitman--Klugerman--Pach--
Schulman guarantee pairs only of order `sqrt(n)`, and Valtr constructed
point sets in which this is tight up to constants.  Thus the unconditional
mutual-avoidance theorem is two polynomial exponents short of the
`n^(1-o(1))` scale required by (3).  The relevant primary statements are
summarized in Mirzaei--Suk's
[positive-fraction paper](https://arxiv.org/abs/1802.06484).

The lemma does not prove that low-`V` point sets realize Valtr's extremal
examples.  Rather, it is a precise obstruction to a black-box proof: an
improved strong-tree extractor in the only difficult (`V` quasipolynomial)
case would automatically be a major conditional improvement for mutually
avoiding pairs.

There is an equally stark recursion calculation.  Even if the
`Theta(sqrt(s))` mutually avoiding pair supplied by an `s`-point set were
optimistically assumed to be a correctly oriented strong pair, recursively
applying only the guaranteed-size conclusion in both children gives the
method recurrence

\[
 q(s)\ge 2q(c\sqrt{s}).                           \tag{7a}
\]

After `d` levels there are `2^d` pieces of size approximately
`n^(1/2^d)`.  Recursion reaches singleton leaves when `2^d=Theta(log n)`,
and hence this black-box recursion constructs only `Theta(log n)`
strong-tree leaves, up to
constant-factor distortions.  The sharp tree theorem on this extracted
object has logarithm only `Theta((log log n)^2)`.  Stopping sooner does not
fix the transfer: without additional lexicographic/multiple-occupancy
control, an unresolved leaf piece cannot be expanded to more than one point
while preserving the exact strong-tree order type.

## 3. Same-type regularization: an exact coefficient audit

There is a second common pipeline:

1. put `m=ES(k)=2^(k+o(k))`;
2. partition `P` into `m` input parts;
3. retain blocks having same-type transversals;
4. choose a convex `k`-set of representatives;
5. count all transversals of those `k` selected blocks.

Suppose the regularization retains a fraction `m^(-d+o(1))` from each input
part.  Since the initial partition costs another factor `m`, the selected
blocks have common size

\[
 s\ge n\,m^{-\gamma-o(1)},\qquad \gamma=d+1.     \tag{8}
\]

Every transversal of the selected `k` blocks is convex.  In fact, because
every subset of a convex set is convex, using *all* subtransversals from
these blocks gives exactly the product lower bound

\[
 (1+s)^k.                                        \tag{9}
\]

Put `k=beta log n`.  Equations (8)--(9) give

\[
 \log V(P)\ge
 \bigl(\beta-\gamma\beta^2-o(1)\bigr)(\log n)^2,
                                                        \tag{10}
\]

whose optimum is

\[
 \boxed{{1\over4\gamma}.}                       \tag{11}
\]

Bukh--Vasileuski's planar same-type theorem retains a fraction at least
`2^(-400)m^(-4)` from each of `m` disjoint input sets.  In this pipeline
`d=4`, `gamma=5`, and (11) is `1/20`, matching the direct structured
corollary already recorded in `agent_killsearch/MULTIPLICITY.md`.

More decisively, even a **perfect** same-type step (`d=0`) leaves the
unavoidable initial partition loss `gamma=1`.  Formula (11) then gives only
`1/4`.  Thus no improvement in the constant of the same-type lemma can make
this one-witness transversal pipeline approach `1/2`; its ideal limit is
exactly the existing uniform supersaturation coefficient.

This is a method ceiling, not an upper bound on what richer regularity
arguments might prove.  To escape (11), one must use many compatible convex
index sets simultaneously, permit controlled multiple occupancy of blocks,
or couple endpoint masses across different regularized pieces.  Merely
making the same-type blocks larger does not suffice.

## 4. Precise target for a useful full-problem regularization lemma

The calculations leave a narrow useful target.  Either one needs

* an exact strong-decomposable subset of size `n^(1-o(1))`; or
* a family of smaller strong pieces whose **weighted** one-turn counts add
  with only `2^o((log n)^2)` overlap; or
* an approximate-strong decomposition in which the exceptional triples can
  be charged to already numerous convex subsets, rather than deleted.

The first target cannot plausibly follow from the existing
`Theta(sqrt(n))` mutually-avoiding extraction, by (3) and the dichotomy
lemma.  The second and third are genuinely multiplicity statements and are
not consequences of standard same-type regularity.
