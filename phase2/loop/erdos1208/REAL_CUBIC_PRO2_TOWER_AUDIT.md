# Totally real base fields do not amplify the prime-ideal depth frontier

## 1. Verdict

Replacing `Q` by a totally real field does **not** multiply the useful-prime
frontier by the degree of the base field.  If `E` has degree `s` and
`q` is a prime ideal of norm `Q`, then one Frobenius-square cap and one
local depth increment have normalized cost and guaranteed gain

\[
 c_{\mathfrak q,k}=\frac{\log Q}{s},\qquad
 g_{\mathfrak q,k}=\frac1{2s}\log A_k(Q^{-2}),
 \tag{1}
\]

where

\[
 A_k(t)=\frac{k+1}{k}\frac{1-t^k}{1-t^{k+1}}.
\]

Thus their ratio is independent of `s`.  Moreover the prime-ideal theorem
is

\[
 \pi_E(X)\sim \operatorname{Li}(X),                 \tag{2}
\]

not `s Li(X)`.  The prime ideals whose residue fields already contain
`sqrt(-1)` are the primes split in `E(i)/E`, and have density `1/2`.
Frobenius-square caps at the complementary primes can at best restore
density one.  They cannot create a degree-`s` density gain.

There is an exact fixed-base obstruction.  In the natural family in which
the first `t` prime ideals by norm are ramified, every remaining local
increment has slope at most

\[
 c_t=\frac{\log 2}{2\log N\mathfrak p_{t+1}}.
 \tag{3}
\]

Consequently any exponent delivered by the present prime-power/Minkowski
master inequality satisfies

\[
 \alpha\ge
 \frac{2}{4+\log 2/\log N\mathfrak p_{t+1}}
 \longrightarrow\frac12.                           \tag{4}
\]

Units, the class group, and the Shafarevich relation excess change the
rank by constants when `E` is fixed, so they do not evade (4).

The most favorable simple test field, the real cubic field

\[
 E=\mathbb Q(\zeta_7)^+,
\]

does give a completely explicit infinite pro-2 tower and a certified
construction

\[
 F_2(n)\ll n^{0.49489}.                             \tag{5}
\]

This is viable but is **worse** than the current rational-base record
`0.49458525`.  Therefore the cubic-base idea does not improve the headline
bound.  This audit does not prove that every possible finite base field is
worse: a field with exceptional finite small-prime splitting or exceptional
2-class rank is not excluded.  What it proves is that degree scaling and
prime-ideal density themselves provide no asymptotic amplification.

## 2. Exact normalization over an arbitrary totally real base

Let `E` be totally real of degree `s`, and let `L/E` be a finite Galois
layer of degree `m` in a totally real pro-2 tower.  Put `K=L(i)`.  Let
`mathfrak q` be an odd prime ideal of `E`, of norm `Q`, whose Frobenius in
the chosen quotient has order at most two.  Every prime of `L` above
`mathfrak q` then has relative residue degree `f=1` or `2`.

At a prime of relative residue degree `f`, the placewise depth-`k`
increment from `proof_placewise_depths.md` has cost and gain

\[
 \frac{kf\log Q}{sm},\qquad
 \frac1{sm}\log\!\left(
 \frac{k+1}{\sum_{e=0}^kQ^{-fe}}
 \right).
\]

Summing over the primes above `mathfrak q` uses

\[
 \sum_{\mathfrak Q\mid\mathfrak q} f_{\mathfrak Q}=m.
\]

The all-depth comparison in `proof_frobenius_all_depth_rank713.md` says
that residue degree two gives a lower bound for residue degree one.  Taking
the difference between depths `k-1` and `k` gives exactly (1).  Both cost
and gain are divided by `s`; the local slope is

\[
 \frac{g_{\mathfrak q,k}}{c_{\mathfrak q,k}}
 =\frac{\log A_k(Q^{-2})}{2\log Q}.                 \tag{6}
\]

No rational splitting hypothesis was used.  Prime ideals of norm `p^f`
work verbatim.  The condition needed by the sum-of-two-squares factorization
is that `-1` be a square in the final residue field.  This holds immediately
if `Q=1 mod 4`; if `Q=3 mod 4`, it holds when the retained Frobenius has
order exactly two.

If `T` is the set of tame ramified prime ideals of `E`, every layer has
root discriminant bounded by

\[
 D_E=\operatorname{rd}(E)
     \prod_{\mathfrak p\in T}(N\mathfrak p)^{1/s}. \tag{7}
\]

Thus the apparent saving `1/s` in the ramification logarithm is the same
`1/s` already present in every local gain and cost.  If `F_E` is the
fractional depth frontier, the master inequality is

\[
 F_E(2\alpha w)\ge
 \log(4D_E)+(2-4\alpha)w+
 \log\!\left(1+
 \frac{e^{2(2\alpha-1)w}}{4D_E}\right).             \tag{8}
\]

After putting `W=sw` and multiplying by `s`, the frontier costs, gains, and
linear term are all on the same unnormalized ideal scale.  The base-field
constant becomes

\[
 s\log(4D_E)=s\log4+\log|\operatorname{Disc}E|
              +\sum_{\mathfrak p\in T}\log N\mathfrak p, \tag{9}
\]

which is a penalty, not a hidden gain.

## 3. Fixed-base no-amplification theorem

Order the odd prime ideals of a fixed `E` by nondecreasing norm,
`mathfrak p_1, mathfrak p_2, ...`, with multiplicity.  Ramify at the first
`t` of them and use disjoint prime ideals for the Frobenius caps.  This is
the norm-minimizing ramification prefix.

For every `0<u<1` and `k>=1`,

\[
 A_k(u)\le \frac{k+1}{k}\le2.
\]

Since every useful prime has norm at least `N mathfrak p_{t+1}`, (6) gives
(3), and hence

\[
 F_E(L)\le c_tL.                                   \tag{10}
\]

If (8) holds at a positive scale, discard its positive constant and
correction terms and substitute `L=2 alpha w`.  Necessarily

\[
 2\alpha c_t\ge2-4\alpha,
\]

which is exactly (4).  There are only finitely many ideals of bounded norm,
so `N mathfrak p_{t+1}` tends to infinity.  The prime-ideal theorem sharpens
this to

\[
 N\mathfrak p_{t+1}\sim t\log t.                  \tag{11}
\]

For a fixed base field, Kummer theory gives generator rank
`t+O_E(1)` and the tame Shafarevich theorem gives relation excess
`O_E(1)`.  The unit rank and 2-class rank are included in these constants.
Therefore increasing the generator rank over a fixed higher-degree base
eventually drives this construction back to exponent `1/2`, just as it
does over `Q`.

The restriction to a ramification prefix in this theorem is deliberate.
It is the exact family suggested by generator-rank per root-discriminant.
The theorem is not advertised as an absolute optimization over all finite
sets, nor over a varying sequence of base fields.  Uniformly controlling
exceptional initial splitting in varying fields would require additional
discriminant-versus-splitting input.

## 4. The real cubic arithmetic input

Let `theta=2 cos(2 pi/7)`.  Its minimal polynomial is

\[
 x^3+x^2-2x-1,                                    \tag{12}
\]

whose discriminant is `49`.  The Minkowski bound for ideal classes is

\[
 \frac{3!}{3^3}\sqrt{49}=\frac{14}{9}<2,
\]

so `E` has class number one.  The roots of (12) lie in
`(-2,-1)`, `(-1,0)`, and `(1,2)`.  The units

\[
 -1,\qquad \theta,\qquad \theta+1
\]

therefore have independent signature vectors.  The unit signature map has
full rank three.  Finally (12) reduces to `x^3+x^2+1` modulo two, which has
no root; hence the unique dyadic prime is unramified of residue degree
three.

Let `T` contain all three prime ideals above each of the first 269 rational
primes `p=+/-1 mod 7`.  These rational primes split completely in `E`, so
`|T|=807`.  The last is `6287`.

Here is a conservative Kummer rank count.  Since the class number is one,
the odd `T`-unit squareclass space has dimension `|T|+3`.  Full unit
signatures leave a totally positive subspace of dimension `|T|`.  At the
unique dyadic completion, the unit squareclasses modulo the unramified
line have dimension three.  Imposing the unramified-at-two condition
therefore costs at most three dimensions.  Thus the Frattini quotient of
the maximal totally real pro-2 extension unramified outside `T` has

\[
 d\ge |T|-3=804.                                   \tag{13}
\]

The tame totally-real Shafarevich presentation bound gives

\[
 r\le d+(r_1+r_2-1)=d+2.                          \tag{14}
\]

This is the only standard presentation theorem used here, and is the
number-field version of the same Koch--Shafarevich input already audited
for the rational rank-713 construction.

Now select the first 53,599 unramified rational primes

\[
 q\equiv1,13\pmod {28};                            \tag{15}
\]

the last is `4,603,241`.  Such a `q` splits into three ideals of norm `q`
in `E`, and `q=1 mod 4`, so `-1` is already a square in every base residue
field.  Add one Frobenius-square relation at each of the three prime ideals.
There are `160,797` added relations.  If the actual generator rank is
`d>=804`, then

\[
 r'\le d+2+160797<\frac{d^2}{4};                  \tag{16}
\]

indeed at the worst endpoint `d=804`,

\[
 4(804+2+160797)=646412<646416=804^2.
\]

The quotient is infinite by Golod--Shafarevich.  Every selected prime ideal
has relative residue degree at most two in every Galois layer.  As in
`RANK715_ARITHMETIC_INPUT_AUDIT.md`, an infinite finitely generated pro-2
group supplies normal layers of every sufficiently large dyadic degree.
The absolute degrees here are `3*2^j`.

Because all three primes above each ramified rational `p` are used, (7)
becomes

\[
 D_E=49^{1/3}\prod_{p\in T_{\mathbb Q}}p.          \tag{17}
\]

Likewise, grouping the three useful prime ideals above one `q` turns their
three copies of (1) into exactly one rational-scale item

\[
 (\log q,\;\tfrac12\log A_k(q^{-2})).              \tag{18}
\]

This equality is the clearest finite manifestation of the degree
cancellation.

## 5. Numerical certificate and consequence

The all-depth verifier takes

\[
 \alpha=0.49489,\qquad w_0=461600.                 \tag{19}
\]

It checks all prime lists, (16), the logarithm of (17), every first through
third local increment, global slope order, exclusion of all fourth and
later increments, and both endpoints of `[w_0,2w_0]`.  The two margins are

\[
 17.2775\ldots,\qquad33.9787\ldots .               \tag{20}
\]

Run

```bash
python3 phase2/loop/erdos1208/verify_real_cubic_pro2_tower_audit.py
```

It prints

```text
literal cubic family F_2(n) << n^0.49489: CERTIFIED
```

The construction is rigorous, but `0.49489 > 0.49458525`.  The rational
rank-713 construction remains the record.  The useful conclusion is a
no-amplification theorem and a clean boundary for future searches:

* arbitrary prime ideals are already covered by (1);
* degree does not change local slopes;
* useful-prime-ideal density is one, or one half without the order-two
  Frobenius repair;
* fixed-field units and class groups contribute only bounded rank shifts;
* a future improvement from a different base field must exploit an
  exceptional **finite** arithmetic configuration, not asymptotic degree
  multiplication.

## 6. References and verification scope

Primary sources for the tower input are:

* N. Alon, T. Bloom, W. T. Gowers, D. Litt, W. Sawin, A. Shankar,
  J. Tsimerman, V. Wang, and M. Matchett Wood, *Remarks on the disproof of
  the unit distance conjecture*, arXiv:2605.20695, especially the tame
  pro-2 presentation in Section 2 and its references to Koch, Theorems
  11.5 and 11.8;
* F. Hajir, C. Maire, and R. Ramakrishna, *Cutting towers of number
  fields*, arXiv:1901.04354, for Frobenius cutting in infinite
  Golod--Shafarevich towers.

The verifier certifies the elementary cubic arithmetic and the complete
finite prime/envelope calculation.  The Shafarevich relation theorem,
Golod--Shafarevich theorem, prime-ideal theorem, and Chebotarev theorem are
declared mathematical inputs rather than re-proved computationally.
