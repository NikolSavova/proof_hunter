# Erdos #1208 research log — 2026-08-17

## Current rigorous frontier

Write \(F_2(n)\) for the minimum, over all planar \(n\)-point sets \(P\), of the
largest subset of \(P\) whose unordered pairwise distances are all distinct.
The current published/preprint window is

\[
  n^{1/3} \ll F_2(n) \ll n^{1/2-\varepsilon}
\]

for an unspecified absolute \(\varepsilon>0\).  The lower bound is due to
Clemen--Fuehrer--Roche-Newton (arXiv:2606.05841); the polynomial upper saving is
due to Lee--Pohoata--Zhu (arXiv:2607.05374).  The local project has a
prime-power refinement and a rank-17 certificate proving the explicit partial
result \(F_2(n)\ll n^{0.49815}\), subject to the declared number-field tower
and master-inequality inputs.  The placewise refinement first improved this to
\(F_2(n)\ll n^{0.498}\).  The quadratic-Frobenius construction below first
gave \(F_2(n)\ll n^{0.4947}\).  Optimizing its presentation rank and globally
interleaving the first three local depths now gives the stronger certified
theorem

\[
  F_2(n)\ll n^{0.494586}.
\]

The natural full-resolution target remains

\[
  F_2(n)=n^{1/3+o(1)},
\]

but there is currently no proof that the square grid, or any other explicit
host, has distance-Sidon independence number \(n^{1/3+o(1)}\).

## Correction concerning the square grid

For an \(m\times m\) grid (host size \(n=m^2\)), the best known asymptotic
lower construction has size \(\Omega(m^{2/3})=\Omega(n^{1/3})\), while the
new combinatorial large sieve gives only

\[
  g(m) \ll m\exp(-c\log m/\log\log m).
\]

Finite Golomb-square records look much closer to linear for small \(m\), but
they do not give a larger asymptotic lower bound.  Thus the grid is still a
possible cube-root extremizer, although proving the matching upper bound would
also settle a long-standing Erdos--Guy grid problem.

## New lead: fractional activation of split prime places

This is an interpolation of the squarefree local sieve.  Let a rational prime
\(q\equiv1\pmod4\) split completely in a degree-\(d\) field.  At each prime
ideal above \(q\), independently:

* leave the place inactive with probability \(1-\theta\); or
* activate it with probability \(\theta\), choosing either isotropic line with
  probability \(1/2\).

For the resulting random congruence partition, Cauchy--Schwarz gives the
expected lower pair count

\[
  |A|^2 a_q(\theta)^d-|A|,
  \qquad
  a_q(\theta)=1-\theta+\theta/q.
\]

For a difference whose split coordinates have valuations \(\alpha,\beta\),
the probability that it survives one place is

\[
  1-\theta \quad(\alpha=\beta=0),\qquad
  1-\theta/2 \quad(\text{exactly one is positive}),\qquad
  1 \quad(\alpha,\beta>0).
\]

Consequently the usual ideal-divisor expansion is governed locally by

\[
  b_q(\theta)
   =(1-\theta)+\frac{\theta}{2q}+\frac{\theta}{2q^2}.
\]

At \(\theta=1\),

\[
  \frac{a_q(1)}{b_q(1)}=\frac{2q}{q+1},
\]

which recovers the Lee--Pohoata--Zhu squarefree gain.  For several primes the
factors multiply.  Ignoring the already-understood archimedean constants, the
interpolated master inequality should have the schematic form

\[
  |A|\lesssim
  \max\left\{
    \prod_q a_q(\theta_q)^{-d},
    X^d\left(\prod_q\frac{b_q(\theta_q)}{a_q(\theta_q)}\right)^{d/2}
  \right\}.
\]

This does not defeat the binary local entropy barrier: as \(\theta\to0\),

\[
 \frac{\log(a_q/b_q)}{\log(1/a_q)}\to\frac1{2q},
\]

which is worse than full activation.  Its possible value is quantitative:
it provides continuous phase tuning and could improve the adaptive explicit
exponent.  It still needs a line-by-line derivation with the exact box and
divisor constants before it can be claimed as a theorem.

### Stronger form: placewise prime-power depths

There is a cleaner deterministic interpolation which appears strictly more
efficient.  If

\[
 (q)=\mathfrak p_1\cdots\mathfrak p_d
\]

splits completely, nothing in the local-to-global proof requires the same
prime-power depth at every \(\mathfrak p_j\).  Choose depths
\(K_j\geq0\) separately and put

\[
 \mathfrak M=\prod_{j=1}^d\mathfrak p_j^{K_j},\qquad
 H=\prod_{j=1}^d(K_j+1),\qquad
 \Lambda=\prod_{j=1}^d\sum_{e=0}^{K_j}q^{-e}.
\]

The CRT index is \(N(\mathfrak M)=q^{\sum_jK_j}\), the valuation-pattern
count is \(H\), and the same ideal-divisor switch produces \(\Lambda\).
Thus the master bound should depend only on the per-degree averages

\[
 \ell_q=\frac1d\sum_jK_j\log q,
 \qquad
 g_q=\frac1d\sum_j
   \log\left(\frac{K_j+1}{\sum_{e=0}^{K_j}q^{-e}}\right).
\]

For large \(d\), arbitrary convex combinations of the integer-depth
cost/gain points are attainable with error \(O(1/d)\).  This removes the
quantization caused by forcing one depth for all \(d\) places.  It does not
break the local entropy barrier, but it may lower the explicit exponent and
replace the 27-row adaptive certificate by a convex optimization plus a
rounding lemma.

These audit points have now been resolved in
`proof_placewise_depths.md`.  With

\[
 L=d^{-1}\log N(\mathfrak M),\qquad
 G=d^{-1}\log(H/\Lambda),\qquad
 w=\frac{\log n}{2d},
\]

the exact master exponents are

\[
 E_1=\frac{L}{2w},\qquad
 E_2=\frac12+
 \frac{\log D-G+\log(4+e^{2(L-w)}/D)}{4w}.
\]

Let \(F(L)\) be the maximum placewise gain at cost \(L\), obtained by sorting
the depth increments by marginal gain-to-cost ratio.  The key simplification
is that

\[
 F(2\alpha w)-\log(4D)-(2-4\alpha)w
 -\log\left(1+\frac{e^{2(2\alpha-1)w}}{4D}\right)
\]

is concave in \(w\).  Hence an entire dyadic phase interval
\([w_0,2w_0]\) is certified by its two endpoints.  Rounding down the one
fractional layer preserves \(E_1\leq\alpha\) and loses only \(O(1/d)\) in
the gain, which is absorbed by any fixed endpoint margin as \(d\to\infty\).

The rank-20 exact data are:

* generator rank 20, relation-rank bound \(20+79=99<100\);
* 21 ramified primes through 79, root-discriminant bound
  \(D=1608822383670336453949542277065\);
* 79 certified split primes and 1580 exact Legendre-symbol checks;
* \(\alpha=0.49806\), \(w_0=5815.2\), endpoint log-margins exceeding
  \(0.24\) and \(0.48\), with the finite-packing correction included.

`verify_placewise_rank20.py` and `rank20_split_primes.txt` reproduce all of
these checks.  `verify_placewise_rank20_intervals.py` additionally certifies
the 534 used frontier slopes and both endpoint margins using exact rational
upper and lower bounds for every logarithm; no floating-point sign decision
remains.  The previous rank-17 and other repository verifiers still pass.
The relaxed optima found while increasing the tower rank are

\[
\begin{array}{c|c}
\text{rank}&\text{relaxed worst exponent}\\ \hline
17&0.4981387831\\
18&0.4981397970\\
19&0.4980699059\\
20&0.4980495747\\
21&0.4980116989\\
22&0.4979949635.
\end{array}
\]

Thus rank 18 loses, but the additional split-prime budget at ranks 19--22
more than compensates for the larger discriminant.  At rank 22 the exact
target \(\alpha=0.498\), \(w_0=6826.7\) is certified with rational endpoint
margin lower bounds \(0.138\) and \(0.275\).  The rank-22 verifier checks 98
split primes, 2156 Legendre symbols, generator/relation ranks \(22,120\), and
the root-discriminant bound
\(11884370948172775385325268800679155\).

## Quadratic-Frobenius upgrade: a certified 0.4947 exponent

Complete splitting is much stronger than the local sieve needs.  Start with
the maximal totally real pro-2 extension of \(\mathbb Q\) unramified outside
the first 401 odd primes.  Its tame Shafarevich presentation has generator
rank 400 and relation rank at most 400.  For each of 39,599 explicitly
selected unramified primes \(q\), impose only

\[
  \operatorname{Frob}_q^2=1.
\]

These square relators lie in the Frattini subgroup, so the generator rank is
unchanged.  The new relation bound is

\[
  400+39599=39999<400^2/4=40000,
\]

and Golod--Shafarevich still gives an infinite tower.  Every unramified prime
\(q\equiv1\pmod4\) is eligible.  A prime \(q\equiv3\pmod4\) is also eligible
when its Frattini Frobenius class is nonzero: the square relator then makes it
an actual involution, so it has residue degree exactly two in finite Galois
layers retaining the Frattini quotient.  All of the first 39,599 unramified
odd primes pass this criterion; the last is 479,939.  At a
residue-degree-two place, the first two guaranteed per-degree gains are

\[
 h_{q,1}=\frac12\log\frac2{1+q^{-2}},\qquad
 h_{q,2}=\frac12\log
 \frac{3(1+q^{-2})}{2(1+q^{-2}+q^{-4})},
\]

each at per-degree cost \(\log q\) when applied at all places above \(q\).
Residue-degree-one places are strictly better.  A two-stage path first gives
depth one to the useful primes in increasing order and then gives depth two
in the same order.  Each stage is concave.

With \(\alpha=0.4947\) and \(w_0=345000\), the three endpoint checks at
\(w_0\), the stage transition, and \(2w_0\) have log-margins exceeding
76.38, 804.49, and 106.25.  The exact construction and proof are in
`proof_frobenius_order_two.md`; `verify_frobenius_order_two_rank400.py`
generates the 401 ramified and 39,599 useful primes, checks the strict
Golod--Shafarevich inequality, and reproduces the 80-digit phase margins.

Higher Frobenius orders were also tested with the weighted
Golod--Shafarevich polynomial.  Imposing \(\operatorname{Frob}_q^4=1\)
allows many more rational primes, but divides the worst local gain by four;
the best pure order-four relaxation found was about 0.4961.  Mixtures of
order-two and order-four relators gave only small improvements at fixed rank
and did not beat the rank-400 order-two certificate.

## Kill: four-variable isotropic-plane amplification

The equal-distance congruence

\[
  Q(a-b)-Q(c-d)=0
\]

is a split quadratic form in four variables modulo a split prime.  It has
about \(2q\) maximal totally isotropic two-planes, each of index \(q^2\).
For a graph plane \(u=Rv\), Cauchy--Schwarz gives roughly
\(|A|^4/q^2\) modular quadruples.  At first sight, the local entropy
\((\log q)/(2\log q)=1/2\) looks much stronger than the two-line binary sieve.

This does **not** currently improve the distance-Sidon threshold.  For every
plane, the \(|A|^2\) zero-difference solutions

\[
  a=b,\qquad c=d
\]

are present.  After summing over all planes, the same multiplicity multiplies
both the Cauchy lower bound and this diagonal.  The off-diagonal count is only
forced once \(|A|^4/q^{2d}>|A|^2\), i.e. \(|A|>q^d\), so the apparent branch
gain cancels.

Any resurrection of this idea requires a genuinely new off-diagonal mixing
estimate (or a four-partite count with a valid lower bound); merely listing
the isotropic planes is insufficient.

## Structural bottleneck

For \(A\subset[m]^2\), distance-Sidon means the nonzero difference set
\(A-A\) contains exactly one oriented pair \(\pm v\) on every integer circle.
The difference set also carries \(\Theta(|A|^3)\) triangle relations and
\(\Theta(|A|^4)\) parallelogram relations.  All currently used arguments see
either the radial uniqueness or the additive relations, but not both sharply
enough.  A plausible grid-closing lemma would bound the number of additive
triangles in a symmetric lattice set that meets each norm fibre in at most two
points.  No such bound strong enough for \(|A|\ll m^{2/3+o(1)}\) is presently
known.

### Additional structural routes checked

* **Low-rank distance matrix.**  The squared Euclidean distance matrix has
  rank at most four, so the problem is a rainbow-principal-submatrix problem
  for a highly special conditionally negative matrix.  Rank two already
  contains the additive Sidon example \(M_{ij}=x_i+x_j\), whose worst rainbow
  subset is only of square-root size.  No theorem was found that improves the
  cube-root guarantee for rank-four Euclidean matrices.
* **Semi-algebraic hypergraphs.**  The four-conflict relation is quadratic and
  semi-algebraic, but current Ramsey bounds for low-degree semi-algebraic
  hypergraphs are far too weak in the sparse off-diagonal regime.  The
  Clemen--Fuehrer--Roche-Newton argument already exploits substantially more
  geometry than a generic semi-algebraic independence theorem.
* **High-dimensional digit embeddings into the plane.**  Mapping a vector of
  labels to a complex polynomial evaluated at a transcendental scale does not
  emulate orthogonal tensor factors.  Equality of squared norms records the
  full autocorrelation polynomial; generically its fibres are finite, so the
  construction falls back to a square-root Sidon constraint rather than a
  cube-root one.
* **Four-variable local planes.**  Removing the literal zero edge by counting
  disjoint color classes would help, but Cauchy gives no lower cross-correlation
  between two prescribed classes.  A random vertex partition cannot repair a
  lower bound that may be entirely supported on the universal diagonal.

## Next concrete work

1. Obtain an independent audit of the order-two Frobenius quotient and its
   residue-degree-two placewise rounding argument.
2. Search for an off-diagonal finite-field energy inequality for the graph
   planes \(u=Rv\) that survives removal of the universal diagonal.
3. Formulate and test the grid difference-set lemma:
   if \(D=A-A\subset[-m,m]^2\) and \(Q\) is two-to-one on \(D\setminus\{0\}\),
   exploit the forced triangle relations in \(D\) to prove \(|A|\ll
   m^{2/3+o(1)}\), or find a construction falsifying that target.

## Rotated triple-sum reduction

The grid bottleneck now has a sharper exact form; see
`ROTATED_TRIPLE_ENERGY.md`.  If `J` is quarter-turn and `A` is a
distance-Sidon subset of `[m]^2`, then

\[
  |A+JA|=|A|^2.
\]

For the cubic map

\[
  \Phi(a,b,c)=a+J(b-c),\qquad b\ne c,
\]

all images lie in fewer than `9m^2` lattice positions.  Its collision energy
therefore satisfies

\[
  \mathcal T_J(A)\ge \frac{|A|^4(|A|-1)^2}{9m^2}.
\]

The estimate `T_J(A) <= |A|^{3+o(1)}`, or alternatively the triple-sum
expansion `|A+JA-JA| >= |A|^{3-o(1)}`, would prove the conjectural grid bound
`|A| <= m^{2/3+o(1)}` and hence close the power-law gap in problem 1208.

The pointwise version is false: one external image can have linearly many
generic representations.  What remains plausible, and is supported by
greedy experiments, is a *total* mixed-energy bound.  Fourier analysis turns
the full energy into

\[
  |G|^{-1}\sum_\chi |\widehat{1_A}(\chi)|^2
  |\widehat{1_A}(J^*\chi)|^4.
\]

This exposes the exact missing inverse theorem: a large mixed sixth moment
must force perpendicular additive structure in `A-A`, and that structure
must then be contradicted by the fact that `(A-A) intersect J(A-A)={0}`.
Generic BSG loses the rotation and returns only a rank-two progression, so it
does not suffice.

The pinned-distance/Tardos entropy idea was also audited.  Two pinned rows do
indeed share exactly one entry, but there are only `|A|` rows and Tardos's
row-sum exponent tends to `1/e`; this cannot reach the required cubic count.

## Kill: direct pro-3 Frobenius-cube amplification

A pro-`3` analogue of the order-two construction initially looks stronger.
With generator rank `d` and initial relation rank at most `d`, adding `N`
Frobenius-cube relators is certified by

\[
  1-dt+dt^2+Nt^3<0.
\]

Optimizing `t` permits `N` of order `d^3`, rather than the order `d^2`
quadratic-relator budget in a pro-`2` group.  However, the guaranteed residue
degree is now three.  A depth-one useful prime contributes at worst

\[
  \frac13\log\frac{2}{1+q^{-3}}
\]

per absolute degree, while still costing `log q`.  Ramification also has to
use primes congruent to `1 mod 3`, and useful primes were conservatively
restricted to `1 mod 4` so that `-1` already splits in the residue field.

A direct sweep using the exact cubic GS capacity and the smallest eligible
primes gave the following *continuous-degree, no-phase-loss* exponents:

| `d` | cube relators | relaxed exponent |
|---:|---:|---:|
| 20 | 923 | 0.49602 |
| 30 | 3407 | 0.49533 |
| 40 | 8424 | 0.49535 |
| 50 | 16864 | 0.49548 |

The best point in this sweep is already worse than the rigorous pro-`2`
exponent `0.4947`, before accounting for the much coarser degree sequence
`3^j`.  Higher odd primes have an even worse gain-to-log-cost ratio.  Thus
Frobenius-cube amplification is not a competitive route with the current
local norm sieve.

## Exact-rotation lane from unimodular units

`UNIMODULAR_UNIT_ROTATIONS.md` records a new construction mechanism.  In an
imaginary non-CM field closed under conjugation, the subgroup

\[
  V_K=\{u\in\mathcal O_K^\times:|u|=1\}
\]

can have rank proportional to the degree.  Every such unit acts as an exact
rotation at the chosen planar embedding.  For a distance-Sidon set with
nonzero lifted difference set `E`, the sets `uE` are disjoint as `u` ranges
over units modulo sign.

For a subset-product family generated by independent units `epsilon_j`, the
symmetry gain is `2^r`, while the full Minkowski-window expansion is at most
the product of their full-field Mahler measures.  Thus a tower with linearly
many independent units satisfying average

\[
  \log M_K(\epsilon_j)<\log2-c
\]

would give an immediate polynomial improvement through a direct lattice
packing argument, with no split-prime sieve.

The current blocker is arithmetic rather than geometric: Dirichlet's rank
formula supplies the units abstractly, but no bounded-root-discriminant tower
with the required small relative regulator/Mahler basis was located.  CM
fields have rank zero here, a single Salem unit loses to expansion at the
other embeddings, and `S`-units reintroduce the rational-rotation denominator
cost.  This lane remains open pending either a small-unit construction or a
regulator obstruction.

Akhtari--Vaaler's relative-height inequality now makes the obstruction
numerical.  If `r=rank V_K` and `R_{K/F}` is the relative regulator for
`F=K intersect R`, every full-rank independent rotation family satisfies

\[
  \sum_{j=1}^r \log M_K(\epsilon_j)
  \ge r R_{K/F}^{1/r}.
\]

Thus the binary subset-product mechanism requires
`R_{K/F}^{1/r}<log 2`, and a polynomial gain requires a fixed gap below this
threshold.  Known general relative-regulator bounds do not settle that sharp
inequality.  The exact derivation and citations are in
`UNIMODULAR_UNIT_ROTATIONS.md`.

## Kill: odd-degree composita as dyadic phase fillers

Compositing the pro-2 tower with fixed cyclic totally real fields of degrees
`1,3,5,...,15` gives degree phases with maximum ratio `9/8`; the construction
is arithmetically valid and can use conductors already in the ramification
set.  However, requiring the useful primes to split in a degree-`s` field
thins them by `1/s`.  Exact prime enumeration plus a master-inequality sweep
shows that every auxiliary family has a worse best exponent than the base
family, even at a single favorable scale.  Varying the presentation rank does
not reverse this.  See `ODD_DEGREE_PHASE_AUDIT.md`.

## Kill: radial uniqueness without difference-set realizability

For `D=(A-A)\{0}`, every ordered point triple supplies an additive relation
`(a-b)+(b-c)=a-c`.  It was tempting to conjecture that any symmetric lattice
set with at most one antipodal pair on each circle has only `m^{2+o(1)}`
additive triples.  `RADIAL_ADDITIVE_TRIPLE_AUDIT.md` gives a decisive
counterexample: canonical representatives from every occupied lattice circle
have more than 20 billion additive triples already at `m=800`, over 32,000
times `m^2`.

The missing input is therefore not radial uniqueness itself but the fact that
`D` is the complete directed difference set of one set `A`.  Any additive
proof must retain that realizability constraint.

## Tri-coloured fibres and a second abstraction barrier

Every fibre of `Phi(a,b,c)=a+Jb-Jc` is tri-coloured sum-free, not merely a
matching.  If its representations are `(a_i,b_i,c_i)`, a mixed solution
`a_i+Jb_j-Jc_l=x` would imply
`b_j-b_i=c_l-c_i`; oriented-difference uniqueness then forces
`b_i=c_i`, a contradiction unless all three indices agree.  This is a
rigorous induced-matching structure and suggests arithmetic-removal methods.

However, direct-sum theory without the rotation cannot suffice.  Split a
`2k`-mark Golomb ruler of length `O(k^2)` into two `k`-sets `X,Y`.  They are
Sidon, `(X-X) intersect (Y-Y)={0}`, and `X+Y` is direct, yet
`|X+Y-Y|=O(k^2)`.  Therefore the identity `Y=JX` and radial uniqueness are
essential; any black-box theorem for two abstract direct Sidon summands is
false at exactly the desired cubic scale.

## Kill: Frobenius fourth powers

Imposing `g_q^4=1` in a pro-2 group gives degree-four GS relators and allows
`Theta(d^4)` useful primes, but their worst residue degree is four.  An exact
prime sweep has best dyadic exponent about `0.49576` near rank 15, worse than
`0.4947`.  At rank 400 the existing square presentation can surprisingly
absorb 39,999 extra fourth-power relators for free, but all of their local
increments occur below the part of the square-prime concave envelope used by
the tight dyadic interval.  The certified threshold is unchanged.  See
`FROBENIUS_FOURTH_POWER_AUDIT.md`.

## Rank-725 optimization of the quadratic-Frobenius tower

An exact rank sweep showed that the two-stage Frobenius-square construction
is strongest near presentation rank 725, rather than the previously used
rank 400.  Take the first 726 odd primes as the ramification set and impose
Frobenius-square relators at the first 130,681 useful unramified primes.  The
presentation has

\[
 d=725,\qquad r\le725+130681=131406<725^2/4.
\]

With \(\alpha=0.49459\) and phase interval
\(w\in[1069500,2139000]\), the three concavity endpoint margins in the
master inequality are \(23.28\), \(1814.20\), and \(23.95\).  Hence

\[
  F_2(n)\ll n^{0.49459}.
\]

The mathematical delta is recorded in
`proof_frobenius_order_two_rank725.md`; the exact arithmetic and 80-digit
endpoint certificate are in `verify_frobenius_order_two_rank725.py`.

## Global depth envelope at rank 715

The two-stage path is not quite the true concave local frontier: near its
large-scale endpoint, a third increment at a small prime has slightly larger
gain per cost than a second increment at a much larger prime.  Globally
sorting the first three increments and re-optimizing the presentation rank
gives the best sampled rank at 715.  With

\[
 \alpha=0.494586,\qquad w\in[1040100,2080200],
\]

the two concavity endpoint margins are (3.0585\) and (3.3207\).  The right
endpoint uses all 127,091 first increments, 30,938 second increments, and 396
third increments.  Therefore

\[
  F_2(n)\ll n^{0.494586}.
\]

The proof, including the new residue-degree-one identity for the third
increment, is in `proof_frobenius_all_depth_rank715.md`; the finite certificate
is `verify_frobenius_all_depth_rank715.py`.

## Local PSD optimality of the branch sum

At a split residue place the norm-zero relation is the union of the two axes
in \(\mathbb F_q^2\).  A symmetric translation-invariant kernel supported on
those axes, with weight (b\) on a nonzero axial difference and weight (a\)
at zero, has Fourier eigenvalues whose smallest type is (a-2b\).  Hence every
positive-semidefinite Cauchy kernel must have (a\ge2b\).  The existing sum of
the two branch-equivalence kernels has (a=2,b=1\), so it is optimal.

Thus the diagonal double count which produces the local divisor factor cannot
be removed by passing to the union relation, by nonnegative reweighting, or by
a thinned pattern code while retaining a universal pair-energy lower bound.
`LOCAL_PSD_BARRIER.md` gives the calculation and the coding interpretation.

## Cross-sum energy target

For (B=A+JA\), directness gives (|B|=|A|^2\) and
\(|\widehat{1_B}|^2=|\widehat{1_A}|^2
 |\widehat{1_A}\circ J^*|^2\).  Cauchy--Schwarz therefore turns the rotated
triple energy into

\[
 \mathcal E_J(A)\le\sqrt{E^+(A+JA)E^+(A)}.
\]

Since (E^+(A)=2|A|^2-|A|\), an upper bound
\(E^+(A+JA)\le |A|^{5+o(1)}\) would already yield the new grid bound
\(|A|\le m^{4/5+o(1)}\), hence (F_2(n)\le n^{2/5+o(1)}\).  The sharp
\(|A|^{4+o(1)}\) energy bound would solve the cube-root problem.  Experiments
put the cross-sum energy naturally on the fifth-power scale, while the Golomb
ruler counterexample shows that directness alone allows sixth-power energy.
Section 9 of `ROTATED_TRIPLE_ENERGY.md` records the exact reduction.

## Relative Minkowski-unit target

In an imaginary non-CM Galois field, every unit `beta` produces exact
rotations `sigma(beta)/c sigma(beta)`, all of height at most `2h(beta)`.  A
single relative Minkowski unit whose conjugate ratios have linear rank would
therefore suffice if its full-field log height were below `(log 2)/2`.
Amoroso--Masser rule out the naive case where `beta` itself is a primitive
generator of a growing Galois field: its Mahler measure must grow.  Their
theorem does not rule out an element lying in a much larger Galois tower whose
conjugate rank grows with the ambient degree.  This leaves a sharply stated
higher-dimensional Lehmer/regulator construction problem; Section 7 of
`UNIMODULAR_UNIT_ROTATIONS.md` records it.
