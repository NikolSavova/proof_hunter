# Linking matrices after bounded inertia: weighted GS audit

## 1. Verdict

The proposed higher-order mechanism is mathematically real: after imposing
inertia-square caps, the quadratic parts of the old tame local relators are
controlled by the Legendre linking matrix.  A linear dependency among the
complete collection of quadratic initial forms promotes a corresponding
relation to Zassenhaus degree at least three and makes it cheaper in the
weighted Golod--Shafarevich polynomial.

For the actual rank-221 prefix construction, however, the mechanism gives
**no saving at all**.  An exact row reduction of

* all 221 retained inertia-square forms;
* the square of the eliminated inertia generator;
* all 221 capped Koch local relators; and
* all 11,767 useful Frobenius-square forms

has rank

\[
 12210,                                           \tag{1.1}
\]

exactly the full relation count.  No linear combination moves from degree
two to degree three.  The verifier is
`verify_bounded_inertia_quadratic_initial_rank.py`.

Engineered low-linking sets remain a logically valid different family, but
the explicit stress in Section 6 shows their prime-size cost is severe.  No
competitive sparse-linking certificate was found.  This last statement is
a search verdict, not a universal number-theoretic impossibility theorem.

## 2. Koch's quadratic initial forms

Let

\[
 T=\{p_0,\ldots,p_d\}
\]

contain a prime congruent to 3 modulo 4.  Put `a_i=1` for
`p_i=3 mod 4` and zero otherwise, and define the directed linking numbers

\[
 \ell_{ij}=1
 \quad\Longleftrightarrow\quad
 \left(\frac{p_i}{p_j}\right)=-1.                \tag{2.1}
\]

The standard Shafarevich--Koch presentation used by the tower has inertia
generators `x_i`, one global linear relation, and local relators whose
quadratic initial forms are

\[
 x_i^{2a_i}\prod_j[x_i,x_j]^{\ell_{ij}}pmod {F_{(3)}}. \tag{2.2}
\]

This is the explicit presentation recorded, for example, in Labute--Minac,
*Mild pro-2-groups and 2-extensions of Q with restricted ramification*,
Theorem 1.2's proof (citing Koch, Theorem 11.10 and Example 11.12).  It is
the missing interface between the safe relation-rank estimate and the
Legendre matrix.

Choose an index `e` with `a_e=1`.  The global relation eliminates `x_e` in
degree one:

\[
 X_e=\sum_{j\ne e}a_jX_j.                         \tag{2.3}
\]

One may omit the `e`th local relator.  Thus the `d` retained degree-one
inertia classes are a minimal generating basis.

## 3. What the inertia caps do

For each retained generator, adjoining `x_i^2=1` supplies the pure-square
initial form `X_i^[2]`.  These give a direct `d`-dimensional summand in
degree two.  Row-reducing (2.2) against them deletes its `X_i^[2]` term.

After substituting (2.3), the remaining commutator part of the `i`th old
local relator is

\[
 \rho_i=
 \sum_{j\ne i,e}
 \bigl(\ell_{ij}+\ell_{ie}a_j\bigr)[X_i,X_j].     \tag{3.1}
\]

The cap on the eliminated inertia generator must not be forgotten.  Its
Frattini vector is

\[
 v_e=\sum_{j\ne e}a_jX_j,                         \tag{3.2}
\]

so its restricted square has, modulo the retained pure squares, the clique
form

\[
 Q(v_e)=\sum_{i<j}(v_e)_i(v_e)_j[X_i,X_j].        \tag{3.3}
\]

This explains two potential bookkeeping errors.  It is wrong either to
leave the old `X_i^[2]` terms in (3.1), or to count the eliminated inertia
cap as another independent pure square without checking (3.3).

## 4. Frobenius-square initial forms

For a vector

\[
 v=\sum_i v_iX_i\in F/F_{(2)},
\]

the degree-two initial form of the square of any lift is the restricted
square

\[
 v^{[2]}=
 \sum_i v_iX_i^{[2]}+\sum_{i<j}v_iv_j[X_i,X_j].   \tag{4.1}
\]

It is independent of the chosen lift: changing a lift by an element of
`F_(2)` changes its square only in degree at least three.

For the rank-221 construction take `e` to be the prime 3.  The squareclass
basis dual to the retained inertia generators consists of

* `p_i` when `p_i=1 mod 4`; and
* `3p_i` when `p_i=3 mod 4`, `p_i!=3`.

Therefore the Frattini vector `v(q)` of an unramified Frobenius is computed
exactly by the Legendre symbols of these radicands modulo `q`.  Modulo the
retained inertia-square span, its cap contributes the clique form

\[
 Q(v(q))=\sum_{i<j}v_i(q)v_j(q)[X_i,X_j].         \tag{4.2}
\]

The verifier finds no zero vector among the 11,767 selected useful primes.
Had a `q=1 mod 4` prime had zero Frattini vector, its square relation would
have degree at least four rather than two; this possible bonus simply does
not occur in the certified list.

## 5. Exact rank-221 computation

The commutator space on 221 generators has dimension

\[
 \binom{221}{2}=24310.                            \tag{5.1}
\]

Using (3.1)--(3.3), the eliminated inertia cap together with the 221 old
local relators has exact rank

\[
 222.                                             \tag{5.2}
\]

Adjoining the 11,767 clique rows (4.2) raises the commutator rank by exactly
11,767:

\[
 222+11767=11989.                                 \tag{5.3}
\]

There is no dependency at any stage.  Restoring the direct 221-dimensional
pure-square summand gives

\[
 221+11989=12210,                                 \tag{5.4}
\]

the same number as

\[
 221\text{ base relators}
 +222\text{ inertia caps}
 +11767\text{ Frobenius caps}.                    \tag{5.5}
\]

Consequently the safe polynomial with every relation charged at degree two
is not concealing any weighted-GS slack for this prefix set.

## 6. The genuine sparse-linking branch and its cost

The full-rank result does not make the mechanism vacuous.  Take one prime
`e=3 mod 4` and `d` primes `p_i=1 mod 4` that are pairwise quadratic
residues.  Eliminate `e`.  Then every coefficient in (3.1) vanishes, so the
`d` base relators have degree at least three.  Also `v_e=0`, so the
eliminated inertia-square cap has degree at least four.  With `N` useful
quadratic Frobenius caps, the safe weighted polynomial becomes

\[
 P(t)=1-dt+(d+N)t^2+dt^3+t^4.                    \tag{6.1}
\]

Thus sparse linking can genuinely restore almost `d` useful-prime caps.

The verifier contains an explicit pairwise-residue set of 19 primes,
beginning

\[
 5,29,109,281,349,1601,\ldots
\]

and ending at 9,594,709.  Together with the eliminated prime 3, (6.1) at
`d=19`, `N=69`, and `t=0.1044` is strictly negative.  The ordinary
all-quadratic budget at this rank permits only 51 useful caps.  Hence the
weighted gain is real—but obtaining even 19 zero-linked generators already
pushes the ramified support to nearly ten million.  A direct disk-envelope
test of this stress family was far worse than the rank-221 prefix (about
`0.4994`, used only as orientation).

More economical partial rank deficiencies are not ruled out by a theorem.
However, the exact prefix computation shows they must be deliberately
engineered: the natural small-prime set has maximal possible initial-form
rank.  Any claimed improvement must provide all of the following, not just
a sparse Legendre matrix:

1. an explicit ramified set and the eliminated global relation;
2. the rank of the **combined** base, inertia, and Frobenius initial forms;
3. a weighted GS value `P(t)<0`;
4. the changed useful-prime Legendre list; and
5. a disk-envelope gain exceeding the enlarged root discriminant.

No construction passing all five tests is currently known.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_bounded_inertia_quadratic_initial_rank.py
```

It reconstructs the Koch linking rows, the eliminated generator and cap,
all useful Frobenius vectors, every restricted-square clique, and the exact
`F_2` row rank.  It also checks primality, congruence, and all pairwise
Legendre symbols in the 19-prime zero-linking stress, plus the exact negative
rational sign of its weighted polynomial.

The output ends with

```text
total quadratic rank / relations: 12210 12210
bounded-inertia quadratic initial forms: FULL RANK
```
