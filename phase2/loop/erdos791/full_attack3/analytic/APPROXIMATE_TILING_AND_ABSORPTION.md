# Approximate microtiles and aligned mesoscopic absorption

Date: 2026-08-13

## Verdict

This lane does **not** prove `alpha_-=alpha_+`.  It proves two results that
sharpen the remaining bridge.

1. A compactness/Fourier stability theorem: three `q+o(q)` integer tiles
   cannot have all three pair-sums cover all but `o(q^2)` points of intervals
   of length `q^2`.  Thus the exact matching theorem is unstable as a
   uniqueness statement, but its triangle-free consequence is stable.  Any
   near-full **one-pair-per-block** interaction architecture is still subject
   to the weighted `1/4` barrier.
2. A sparse-residue (rank-one) absorber: holes may occur in every mesoscopic
   block and still be repaired at `o(k)` cost, provided the residual pattern is
   shared across blocks.  This removes the incompatible requirements
   `q<<sqrt(k)` and `q>>sqrt(k)` created by the earlier full-block absorber.

An adversarial candidate family exposed the precise escape hatch.  It does
not contradict the stability theorem: its third raw pair misses a positive
fraction of every block-length interval.  But that pair is a perfect cyclic
tile, and two consecutive carry states exactly fill a block.  Together with
two direct interactions this gives an exact, asymptotically no-slack carry
triangle.  Consequently, an approximate-factorization route to closure must
use carry patches of this kind, rather than a triangle of pairwise near-full
raw intervals, and must align any residual holes into a small additive
rectangle.

## 1. Pair accounting turns near coverage into near-uniform convolution

For finite integer sets `X,Y`, write

```text
r(s) = #{(x,y) in X times Y : x+y=s},
P    = |X||Y|.
```

### Lemma 1 (exact accounting)

Let `I` be an interval of `Q` integers, let

```text
h = |I \ (X+Y)|,          K=Q-h,
```

and suppose `K>0`.  Let `nu` be the law of `x+y` for independent uniform
`x in X,y in Y`, and let `u_I` be uniform on `I`.  Then `P>=K` and

```text
||nu-u_I||_1
 <= (P-K)/P + h/Q + |P-Q|/P.                         (1)
```

In particular, if

```text
P=Q+o(Q),                 h=o(Q),                    (2)
```

then `nu` is `o(1)`-close in total variation to `u_I`.

### Proof

Let `W` be the number of ordered pairs whose sum is outside `I`, and let

```text
C=sum_{s in I, r(s)>0}(r(s)-1)
```

be the collision excess inside `I`.  Since precisely `K` values in `I` are
occupied,

```text
W+C=P-K.                                                (3)
```

The outside contribution to the `L1` distance is `W/P`; the `h` holes
contribute `h/Q`.  On an occupied value, compare first `r(s)/P` with `1/P`
and then `1/P` with `1/Q`.  Summing gives at most

```text
C/P + K |P-Q|/(PQ) <= C/P+|P-Q|/P.
```

Together with (3), this is (1).

This elementary point is important: near coverage plus near-minimal pair
budget is much stronger than a statement about the support of `X+Y`.  The
entire pair-sum distribution approaches the uniform law on the target
interval.

## 2. Established stability/no-go: approximate interactions are triangle-free

### Theorem 2 (no asymptotically efficient pair triangle)

Let `Q_n -> infinity`, and for `i=1,2,3` let `X_{i,n}` be finite integer
sets with

```text
|X_{i,n}|/sqrt(Q_n) -> 1.                               (4)
```

It is impossible that, for every pair `i<j`, there are intervals `I_{ij,n}`
of `Q_n` consecutive integers satisfying

```text
|I_{ij,n} \ (X_{i,n}+X_{j,n})|=o(Q_n).                  (5)
```

The intervals may have different translations for the three pairs.

### Proof

For each tile put the uniform empirical probability measure on its elements.
By Lemma 1, after scaling the integer line by `Q_n`, the convolution for pair
`ij` is `o(1)`-close in total variation to the uniform measure on the scaled
target interval.

Let `c_{ij,n}` be the midpoint of that scaled interval.  Choose real centers

```text
a_1=(c_12+c_13-c_23)/2,
a_2=(c_12+c_23-c_13)/2,
a_3=(c_13+c_23-c_12)/2.                                 (6)
```

After translating empirical measure `i` by `-a_i`, all three pair
convolutions converge to the same law

```text
lambda = uniform[-1/2,1/2].                              (7)
```

The three centered marginal sequences are tight.  Indeed, put all three
independent empirical variables on one probability space and denote their
pair sums by `S_12,S_13,S_23`.  Each pair-sum family is tight, and

```text
2X_1=S_12+S_13-S_23                                    (8)
```

with the analogous identities for `X_2,X_3`.  A union bound in (8) proves
tightness of every marginal.

Pass to a jointly weakly convergent subsequence, with limits
`mu_1,mu_2,mu_3`.  Convolution is continuous under weak convergence, hence

```text
mu_1*mu_2 = mu_1*mu_3 = mu_2*mu_3 = lambda.             (9)
```

The limiting measures are compactly supported.  To see this without any
moment assumption, realize three independent variables having these laws.
All three pair sums lie in `[-1/2,1/2]` almost surely; (8) then puts each
variable in `[-3/4,3/4]` almost surely.

Their characteristic functions `f_i(z)` are therefore entire.  The
characteristic function of `lambda` is

```text
L(z)=2 sin(z/2)/z.                                      (10)
```

Equation (9) gives `f_1 f_2=f_1 f_3=f_2 f_3=L`.  All functions are nonzero in
a neighborhood of zero.  Dividing there gives `f_1=f_2=f_3` and hence
`f_1^2=L`.  The identity theorem extends this equality to the complex plane.
But every zero of a square of an entire function has even multiplicity,
whereas `L` has simple zeros at every nonzero `2 pi m`.  Contradiction.

### Corollary 3 (uniform qualitative gap)

There are absolute constants `eta>0` and `q_0` such that, for `q>=q_0`, the
following is impossible: three integer sets each of size at most
`(1+eta)q`, with every pair covering at least `(1-eta)q^2` points of some
interval of length `q^2`.

If no such constants existed, choose a counterexample with `eta=1/n` and
strictly increasing `q`.  Pair coverage and the upper size bounds force all
three cardinalities to be `(1+o(1))q`, contradicting Theorem 2.

No effective value of `eta` is obtained.  The conclusion is nevertheless
strong enough for asymptotic architecture: if a family of `q+o(q)` role tiles
declares an edge whenever one pair alone misses only `o(q^2)` points of a
`q^2` block (uniformly over declared edges), then its interaction graph is
eventually triangle-free.  For nonnegative role masses `w_i`, weighted
Mantel gives

```text
sum_{ij edge} w_i w_j <= (sum_i w_i)^2/4.                (11)
```

Thus one-pair near-full blocks cannot by themselves pass density `1/4`.
This theorem does **not** apply when a target block is assembled from several
partial pair-sum footprints in adjacent carry states.  The carry triangle in
`full_attack2` escapes for exactly that reason: none of its three pair types
individually supplies almost the whole block.

**Adversarial status.**  The family in Section 3 does not require a downgrade
of Theorem 2.  The apparent contradiction conflates exact coverage modulo
`B` (implemented by two adjacent carry states) with near coverage of one raw
integer interval.  The theorem and the `1/4` corollary must, however, remain
scoped to a *single pair footprint in a single raw block*; neither is a
barrier to carry-split interactions.

## 3. Established: an exact no-slack carry triangle

The following family was proposed as a possible counterexample to Theorem 2.
It is not one, but its carry behavior is substantially more useful.

For `q>=2`, put `d=q-1`, `B=q^2-q+1=d^2+d+1`, and

```text
X=d[0,d],
Y=[0,d],
Z={0} union {1+qj:0<=j<d}.                              (CT1)
```

All three tiles have `q` elements.  Two pairings are direct exact tiles:

```text
X+Y=Y+Z=[0,B-1].                                       (CT2)
```

For `X+Y`, the intervals `[di,di+d]` overlap successively at their endpoints.
For `Y+Z`, start with `[0,d]`; the remaining intervals are
`[1+qj,q(j+1)]`, which form the rest of the consecutive interval.

The third pair is not close to a raw interval.  Define its low and high carry
footprints

```text
L=(X+Z) intersect [0,B-1],
H=((X+Z) intersect [B,infinity))-B.                     (CT3)
```

Then

```text
L union H=[0,B-1].                                      (CT4)
```

Here is an exact description.  Write a residue below `B` in base `d` as
`r=da+c`, `0<=c<d`; the allowed digit pairs are

```text
0<=a<=d, 0<=c<d, together with (a,c)=(d+1,0).
```

Then

```text
L: c=0 and 0<=a<=d+1,
   or 1<=c<=d-1 and c-1<=a<=d;

H: 1<=c<=d-1 and 0<=a<=c-1.                            (CT5)
```

Indeed a nonzero-`Z` sum is

```text
di+1+(d+1)j=d(i+j)+(j+1).
```

For `0<=j<=d-2`, this has canonical digits `(i+j,j+1)`.  It is low exactly
when `i+j<=d`; when it is high, subtracting `B=d(d+1)+1` gives digits
`(i+j-d-1,j)`.  For `j=d-1`, first normalize `j+1=d`: the raw digits are
`(i+d,0)`.  The cases `i=0,1` are low and the remaining cases, after
subtracting `B`, have digits `(i-2,d-1)`.  This proves (CT5).  The only low
holes have

```text
1<=c<=d-1, 0<=a<=c-2,
```

and are contained in `H`, proving (CT4).  In particular the lower raw window
misses

```text
binom(d-1,2)=binom(q-2,2)=Theta(q^2)                    (CT6)
```

points, not `O(q)`.

In fact no translated raw interval saves the proposed counterexample.  The
best interval of `B` consecutive integers contains exactly

```text
B-floor((q-2)^2/4)                                     (CT7)
```

distinct values of `X+Z`.  To verify (CT7), let `A=[0,B-1] \ L` and
`D=H \ A`.  For a window starting at `ell`, its number of holes is

```text
ell+|A|-2|A intersect [0,ell-1]|-|D intersect [0,ell-1]|. (CT8)
```

Within each base-`d` digit block this quantity rises, is possibly flat once,
and then falls, so a minimum occurs at `ell=dm`.  Direct summation gives

```text
h(dm)=binom(d-1,2)-m(d-2-m).
```

Optimizing over `m` yields (CT7).  Thus the hypotheses of Theorem 2 fail by a
fixed asymptotic fraction.

For completeness, an extremizing window may be assumed to have
`0<=ell<=max(X+Z)-B+1=d(d-1)`: moving a window that starts to the left of the
sumset rightward, or one that ends to its right leftward, cannot decrease its
intersection.  Thus the endpoint calculation above covers all translated
integer intervals, not just the lower ones.  Notice that `q=5` is misleadingly
small: the lower window has only three holes and the best window only two,
but these counts grow respectively as `q^2/2` and `q^2/4` to leading order.

Nevertheless (CT4) gives an exact carry transition.  For macro role sets
`P_X,P_Y,P_Z`, define

```text
A=(X+B P_X) union (Y+B P_Y) union (Z+B P_Z).
```

Macro block `r` is fully covered whenever

```text
r in P_X+P_Y,
or r in P_Y+P_Z,
or {r-1,r} subset P_X+P_Z.                              (CT9)
```

The last clause takes `L` from an `X+Z` macro sum at `r` and `B+H` from one
at `r-1`.  Thus (CT9) is a genuine triangle of role interactions: two direct
edges and one consecutive-carry edge.  It has no leading local loss:

```text
|L|=B-binom(d-1,2),  |H|=binom(d,2),  |L intersect H|=d-1=q-2. (CT10)
```

An `X+Z` macro edge supplies `L` to its own block and `H` to the next block.
Along a consecutive run the interior edges are reused on both sides, so two
states in the clause of (CT9) do not impose a factor-two asymptotic cost;
there is only the `O(q)` overlap in (CT10) and an endpoint loss.

A fixed finite macro certificate of role cost `ell` covering the consecutive
blocks `0,...,m-1` gives

```text
|A|<=q ell,       range >=mB-1,
liminf R(k)/k^2 >= m/ell^2.                             (CT11)
```

Indeed for arbitrary `k`, take `q=floor(k/ell)` and pad the resulting set if
the convention requires exactly `k` marks.  Then `q ell<=k`, `q->infinity`,
and `B/q^2->1`.

This is not yet full closure.  The current-pair compatibility graph is `K3`,
so the unique-sum/Turan argument from `full_attack2` says a near-lossless
sequence in this three-role language can exist only when
`alpha_+<=1/2-1/12=5/12`.  A macro certificate or structured typing theorem
is still missing.  But the family is an exact realization of the
carry-splitting mechanism that Theorem 2 deliberately leaves open.

## 4. Established counterexample: approximate mates are not unique

The stronger exact conclusion “each tile has one mate” has no edit-distance
stability, even with far fewer than `o(q^2)` holes.

For integers `q>=2` and `0<=a<q`, set

```text
X_q=[0,q-1],
Y_{q,a}={0} union {jq+a:1<=j<q}.                         (12)
```

Then the `q^2` cross-sums are all distinct and

```text
X_q+Y_{q,a}
 = [0,q-1] union [q+a,q^2+a-1].                         (13)
```

Thus only the `a` points `[q,q+a-1]` are missing from `[0,q^2-1]`.
For distinct `a,b`, the normalized tiles `Y_{q,a},Y_{q,b}` intersect only at
zero, so their symmetric difference has size `2(q-1)`.

Taking `h_q -> infinity` with `h_q=o(q)` gives one normalized tile with
`h_q` mutually far, `o(q)`-hole partners.  Approximate factorization cannot
be reduced to perturbing the unique exact polynomial quotient.  The stable
object in Theorem 2 is triangle-freeness, not mate uniqueness.

## 5. Established positive tool: rank-one hole absorption

### Lemma 4 (additive-rectangle absorber)

Let `B,U,V` be finite sets of nonnegative integers and let `H` be the targets
in a target set `T` not covered by `B+B`.  If

```text
H subset U+V,                                            (14)
```

then `B union U union V` covers `T` and has size at most

```text
|B|+|U|+|V|.                                             (15)
```

This is immediate: old targets stay covered and every `h in H` is a sum of
one newly available element of `U` and one of `V`.

The earlier full-block absorber is the special case
`U={bad block starts}`, `V=[0,L-1]`.  Its cost `L+N/L` cannot be `o(k)` when
`N=Theta(k^2)`, by AM--GM.  The following sparse-residue specialization
evades that obstruction.

### Corollary 5 (same residual pattern in every block)

Fix a block length `Q`.  If all holes have the form

```text
H subset {Qj+r : j in S, r in R},                        (16)
```

then they can be repaired with at most `|S|+|R|` new elements, by adding
`Q S` and `R`.

Suppose `N=Theta(k^2)`, take `Q=q^2`, and choose

```text
sqrt(k) << q << k.                                       (17)
```

Even if every one of the `O(N/Q)=O(k^2/q^2)=o(k)` blocks is bad, the repair
is `o(k)` whenever the common residual set has `|R|=o(k)`.  In particular,
an `o(q)` residual from a tile such as (12) is harmless.  The crucial resource
is not a vanishing *density* of holes but low additive rank of their global
placement.

### Conditional full-closure theorem

Let `R(k)` be the maximal interval range with at most `k` nonnegative
elements and let
`alpha_+ = limsup R(k)/k^2`.  Suppose that for every sufficiently large `k`
there are a preliminary set `B_k`, a target endpoint `N_k`, and sets `U_k,V_k`
such that

```text
|B_k|<=k,
N_k/k^2 -> alpha_+,
[0,N_k] \ (B_k+B_k) subset U_k+V_k,
|U_k|+|V_k|=o(k).                                        (18)
```

Then `alpha_-=alpha_+`.

Indeed Lemma 4 produces a basis of size `k+o(k)` and range `N_k`.  Given an
arbitrary larger cardinality budget `K`, choose `k=(1-o(1))K` so that the
repair fits inside `K`; the `o(k)` bound is uniform on a tail.  This proves
`R(K)/K^2>=alpha_+-o(1)`, and the reverse liminf/limsup inequality is
automatic.

This conditional theorem is stronger than the earlier “holes in `o(k)` full
blocks” criterion: (16)--(17) permit holes in every block.

## 6. What this does and does not close

Theorem 2 kills the simplest hoped-for stability statement:

```text
many q+o(q) roles, each useful role pair almost filling one q^2 block.
```

Its interaction graph remains triangle-free and hence cannot exploit more
than `1/4` of the pair mass.  Section 4 also kills a different tempting claim:
an approximate mate need not be close in edit distance to the unique exact
mate.

Theorem 2 does not rule out (CT9), because its `X+Z` footprint is split between
adjacent blocks.  The viable bridge is now the following explicit, strictly
weaker target.

> **Missing carry-rectangle lemma.**  Starting from bases approaching
> `alpha_+`, construct a near-lossless multi-pair carry placement at a scale
> `sqrt(k)<<q<<k` whose uncovered targets lie in `U_k+V_k` with
> `|U_k|+|V_k|=o(k)`.

It is enough that all macro blocks share an `o(k)` residual alphabet; they do
not have to be individually exact, nor may their number of bad blocks need to
be `o(k)`.  On the negative side, Theorem 2 says the local patch must combine
several partial footprints or adjacent carries.  This is exactly the geometry
left open by the `H-S-T0` carry triangle.

No theorem here constructs such a placement from an arbitrary limsup basis,
so the normalized-limit problem remains open.

### Proof-dependency audit

The negative theorem uses only four inputs: exact pair accounting, tightness of
probability laws on the real line, continuity of convolution under weak
convergence, and the elementary zero-multiplicity fact for entire squares.
It does not assume Freiman structure, bounded tile diameter, moment bounds, a
common translation of the three target intervals, or prime `q`.

The positive theorem is deliberately conditional.  Neither small total hole
count nor `o(1)` hole density implies (14); the missing content is the global
additive-rectangle organization.  Also, adding `U union V` is legal only when
these are nonnegative integer coordinates, which is included explicitly in
Lemma 4 and condition (18).

## 7. Prior-art scope

The exact tiling literature studies direct factorizations
`A direct-sum B=Z_M` and cyclotomic allocation; see Laba--Londner,
*Combinatorial and harmonic-analytic methods for integer tilings*,
<https://arxiv.org/abs/2106.14042>.  Kreher--Martin--Stinson,
*Uniqueness and explicit computation of mates in near-factorizations*,
<https://arxiv.org/abs/2411.15890>, uses “near-factorization” for the exact
group identity `A+B=G\{0}` with `|A||B|=|G|-1`, not for an asymptotically
small uncovered fraction.

The modulus `B=d^2+d+1` is also the classical Singer/projective-plane
parameter when `d` is a prime power.  The footprint calculation (CT1)--(CT10)
is an elementary interval/carry identity valid for every integer `d`; it
does not assert a perfect difference set.  A targeted search did not locate
this precise three-tile carry predicate, but that search is not sufficient to
claim the construction as new.

Targeted searches did not locate the three-measure approximate-triangle
statement above.  That is not a novelty certification; an additive-tiling or
probability expert should still check the characteristic-function argument
against the broader convolution-root literature before external use.

## 8. Verification artifact

Run

```text
python3 phase2/loop/erdos791/full_attack3/analytic/approximate_checks.py
```

It checks the exact accounting inequality on exhaustive small pairs, the
jitter-family identities, all carry-triangle identities and the best-window
formula through `q=100`, and the rank-one/block-residue absorber on exhaustive
and randomized finite instances.  The compactness/Fourier step is a proof,
not a finite computation.
