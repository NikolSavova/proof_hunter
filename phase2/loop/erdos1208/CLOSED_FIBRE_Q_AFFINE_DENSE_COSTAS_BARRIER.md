# The closed-fibre `Q` relaxation is affine-rigid and fourth-order on dense Sidon arrays

## 1. Outcome

For a vector-Sidon set `A`, let

\[
 \mathcal Q_\Sigma(A)=\sum_{D=1,2,4,\ldots}\mathcal Q_D(A)
\]

be the dyadic sum of the closed-fibre relaxation from
`LARGE_DETERMINANT_CLOSED_FIBRE_ENERGY_GATE.md`:

\[
 \mathcal Q_D(A)=
 \sum_{w,r}
 \min\left\{\binom{B_w(r)}2,
                   \alpha_{w,D}(r)B_w(r)\right\}.     \tag{1.1}
\]

This note proves two structural facts that sharply limit (1.1).

### Theorem A (affine quasi-invariance)

If `T` is a nonsingular integral linear map, then

\[
 \boxed{
 {1\over2}\mathcal Q_\Sigma(A)
 \le \mathcal Q_\Sigma(TA)
 \le2\mathcal Q_\Sigma(A).}                         \tag{1.2}
\]

If `|det T|` is a power of two, equality holds.  Thus the aggregate `Q`
functional is essentially blind to an affine map that changes the Euclidean
height by a large factor.

### Theorem B (dense vector-Sidon arrays have fourth-order `Q`)

For every fixed `C>=1`, there is `c_C>0` such that every sufficiently large
vector-Sidon set

\[
 A\subset[0,m]^2,\qquad |A|=k,\qquad m\le Ck
\]

satisfies

\[
 \boxed{\mathcal Q_\Sigma(A)\ge c_C k^4.}            \tag{1.3}
\]

The proof is elementary and quantitative.  It uses many short realized
directions, the bounded range of determinant projections, and the fact that
the local minimum in (1.1) already charges half the mass in every
non-singleton nonzero fibre.

### Theorem C (the clean centroid count is fourth-order too)

With the notation of
`DIRECTIONAL_MIDPOINT_POINTWISE_NO_GO_GLOBAL_GATE.md`, every such dense
vector-Sidon array also satisfies

\[
 \boxed{\sum_w H_w\ge c'_Ck^4.}                    \tag{1.4}
\]

Moreover `sum_w H_w` is exactly affine invariant.  Consequently a genuinely
balanced asymptotic distance-separating map would kill the proposed ambient
centroid bound as well as the `Q` and `P` relaxations.

Together, (1.2)--(1.3) expose a serious obstruction to the proposed bound

\[
 \mathcal Q_\Sigma(A)
 \le m^{o(1)}(k^3+m^2).                              \tag{1.5}
\]

Any dense vector-Sidon array that can be made Euclidean distance-Sidon by a
balanced integral map of coefficient size `k^(1/2+o(1))` has final height
`k^(3/2+o(1))`, but retains `Q=k^(4-o(1))`; it would disprove (1.5) by a
full factor `k^(1-o(1))`.

This last balanced-separator assertion is **not proved asymptotically** here,
so (1.5) is not formally disproved.  It is, however, a genuine and extensive
distance-Sidon stress: exact determinant-prime transforms of Welch--Costas
arrays exist for every tested prime through `251`, with coefficient size at
most `4 sqrt(p)` in that range.  Their height is on the critical
`k^(3/2)` scale, while exact `Q` computations through `p=59` are about
`0.30 k^4`.  The obstruction grows rather than disappears.

The correct strategic conclusion is conditional but broader: a balanced
separator would refute all three ambient estimates `Q`, `P`, and `sum H_w`.
Until that separator is proved, `Q` and `P` are already structurally unsafe;
the clean centroid gate remains the best of the three only because its finite
Costas constants are smaller, not because affine invariance protects it.

## 2. Proof of affine quasi-invariance

Fix a primitive unoriented active direction `w_0` for `A`.  Write

\[
 T w_0=\epsilon c w,
 \qquad c=\gcd((Tw_0)_1,(Tw_0)_2),\quad
 \epsilon\in\{\pm1\},                              \tag{2.1}
\]

where `w` has the canonical primitive orientation.  If an edge parallel to
`w_0` has content `g`, its image has content `cg`.  If

\[
 r_0=\det(w_0,q_0),\qquad q=Tq_0,qquad \Delta=\det T,
\]

then

\[
 r=\det(w,q)={\epsilon\Delta\over c}r_0.             \tag{2.2}
\]

This is integral because it is a determinant of integral vectors.  More
importantly,

\[
 \boxed{(cg)|r|=|\Delta|g|r_0|.}                    \tag{2.3}
\]

The map `q_0 -> Tq_0` is a bijection between complete nonzero difference
sets.  Equation (2.2) therefore identifies the corresponding projection
fibres and preserves their loads:

\[
 B_w(r)=B_{w_0}(r_0).                               \tag{2.4}
\]

For one fixed fibre load `B`, let `X` be the multiset of positive numbers
`g|r_0|`, one for each `g in T_{w_0}`, and set

\[
 f_B(a)=\min\left\{\binom B2,aB\right\}.
\]

The contribution of this fibre to `Q_Sigma` is

\[
 \Phi_B(X)=\sum_{I\in\mathfrak D}f_B(|X\cap I|),     \tag{2.5}
\]

where `mathfrak D={[2^j,2^(j+1)):j in Z}`.  By (2.3), the image contribution
is `Phi_B(|Delta|X)`.

The dyadic partition and its translate by `log_2|Delta|` have the property
that every cell of either partition meets at most two cells of the other.
Also `f_B` is subadditive, and splitting one load into at most two pieces
increases its total `f_B` cost by at most a factor two.  Hence

\[
 {1\over2}\Phi_B(X)
 \le\Phi_B(|\Delta|X)\le2\Phi_B(X).                 \tag{2.6}
\]

Summing (2.6) over the bijected directions and fibres proves (1.2).  When
`|Delta|` is a power of two, the two dyadic partitions are identical after
reindexing, so equality holds.

Notice the contrast with height: a balanced determinant-`p` map can enlarge
an `O(p)` box to an `O(p^(3/2))` box, while (1.2) changes `Q_Sigma` by at
most a factor two.

## 3. A local lower bound from collided projection mass

For an active primitive direction `w`, write

\[
 N=k(k-1),\qquad q=\|w\|_\infty,
\]

and let

\[
 M_w=\sum_{\substack{r\ne0\\B_w(r)\ge2}}B_w(r)      \tag{3.1}
\]

be the mass in nonzero, non-singleton determinant fibres.

### Lemma 3.1

For every active `w`,

\[
 \boxed{
 \sum_D\sum_r
 \min\left\{\binom{B_w(r)}2,
                   \alpha_{w,D}(r)B_w(r)\right\}
 \ge {M_w\over2}.}                                  \tag{3.2}
\]

### Proof

Fix `r!=0` with `B=B_w(r)>=2`.  Since `w` is active, choose any
`g in T_w`.  The positive integer `g|r|` belongs to exactly one dyadic band,
so that band has `alpha>=1`.  Its local contribution is at least

\[
 \min\left\{\binom B2,B\right\}\ge {B\over2}.
\]

Sum over the fibres.  QED.

If `A subset [0,m]^2`, then every projection of a difference satisfies

\[
 |r|=|\det(w,a-b)|\le2qm.                            \tag{3.3}
\]

Thus at most `4qm` nonzero integers can support singleton fibres.  Moreover,

\[
 B_w(0)=2e_w\le {2m\over q},                         \tag{3.4}
\]

because vector-Sidonicity makes the positive contents in direction `w`
distinct.  Equations (3.3)--(3.4) give

\[
 \boxed{M_w\ge N-4qm-{2m\over q}.}                  \tag{3.5}

In particular, every sufficiently short active direction contributes
`Omega(N)` to `Q_Sigma`.

## 4. Proof of the dense fourth-order theorem

It remains to show that a dense vector-Sidon array has quadratically many
short active directions.

Fix `C` and put

\[
 t=\lceil128C^2\rceil.
\]

Partition `[0,m]^2` into `t^2` axis-parallel cells.  If their occupancies are
`n_i`, the number of within-cell unordered edges is at least

\[
 \sum_i\binom{n_i}2
 ={1\over2}\left(\sum_i n_i^2-k\right)
 \ge {1\over2}\left({k^2\over t^2}-k\right)
 \ge {k^2\over4t^2}                                 \tag{4.1}
\]

for sufficiently large `k`.  Every such edge has primitive direction
`w` with

\[
 q=\|w\|_\infty\le {m\over t}+1\le {k\over64C}.     \tag{4.2}
\]

Let `H` be the number of active primitive directions occurring among these
short edges.  There are at most `4q` canonically oriented primitive
directions of sup-norm exactly `q`.  Therefore, for every set of `H`
directions,

\[
 \sum_w{1\over\|w\|_\infty}\le6\sqrt H.             \tag{4.3}
\]

Since `e_w<=m/q`, (4.1) and (4.3) imply

\[
 {k^2\over4t^2}
 \le\sum_we_w
 \le6m\sqrt H
 \le6Ck\sqrt H.
\]

Consequently

\[
 H\ge {k^2\over576C^2t^4}.                          \tag{4.4}

For every direction in (4.2), (3.5) gives `M_w>=N/2` once `k` is large
enough in terms of `C`.  Lemma 3.1 and (4.4) now yield

\[
 \mathcal Q_\Sigma(A)
 \ge {HN\over4}
 \ge {k^4\over4608C^2t^4},                         \tag{4.5}
\]

after using `N>=k^2/2`.  This proves Theorem B with an explicit, deliberately
unoptimized constant.

The theorem is not a radial-only or abstract-Sidon obstruction.  It uses the
complete determinant fibres of the endpoint difference set, exactly the
objects in (1.1).  It says that fourth-order `Q` is the default at dense
vector-Sidon scale.

## 5. Exact determinant-prime Costas stress

Let

\[
 W_p=\{(i,g^i\bmod p):0\le i<p-1\},                  \tag{5.1}
\]

where `g` is the least primitive root modulo the prime `p`.  This is a
vector-Sidon set of `k=p-1` points in a `k` by `k` box, so Theorem B applies.

The following integral matrices have determinant `p`; exact enumeration
shows that `T_pW_p` is Euclidean distance-Sidon.

\[
\begin{array}{c|c|r|r|r|r}
p&T_p&m&\mathcal Q_\Sigma(W_p)&
 \mathcal Q_\Sigma(T_pW_p)&
 \mathcal Q_\Sigma(T_pW_p)/(k^3+m^2)\\ \hline
11&(-3,2;2,-5)&41&2190&2180&0.8131\\
23&(-5,-2;-1,-5)&131&61370&61406&2.2081\\
43&(-5,13;-1,-6)&612&874300&874292&1.9488\\
47&(-10,11;3,-8)&666&1289926&1290082&2.3851\\
59&(-10,-9;-9,-14)&1144&3348872&3349322&2.2272
\end{array}                                           \tag{5.2}
\]

The normalized base values in the last four rows range from
`0.2620 k^4` to `0.2959 k^4`; they are moving toward, not away from, a
fourth-order law.  The tiny changes under determinant-`p` maps illustrate
(1.2) much more sharply than its worst-case factor two.

The search was then continued without evaluating the expensive full `Q`
functional.  Exact distance separation holds for

\[
\begin{array}{c|c|r|c}
p&T_p&m&\max|T_{ij}|/\sqrt p\\ \hline
101&(-22,-23;-9,-14)&4029&2.29\\
139&(-39,-34;-20,-21)&9437&3.31\\
211&(-57,46;14,-15)&18498&3.92\\
251&(-53,59;-33,32)&26980&3.72
\end{array}                                           \tag{5.3}
\]

Every prime between `11` and `251` tested by the same exhaustive balanced
matrix search had a separator with maximum coefficient below `4 sqrt(p)`.
This is finite evidence only; no infinite balanced-separator theorem is
claimed.  But (1.2), Theorem B, and (5.2)--(5.3) together make a blind proof
of (1.5) implausible and identify exactly what it would have to rule out.

## 6. The global `P` energy has the same barrier

The sufficient global pair energy from
`CLOSED_FIBRE_Q_HEIGHT_LAYERED_BARRIER.md` is

\[
 \mathcal P(A)=\sum_{w,r\ne0}\binom{B_w(r)}2.        \tag{6.1}
\]

Unlike `Q_Sigma`, this functional is **exactly** affine invariant.  Equations
(2.1)--(2.4) biject its directions and projection loads, and preserve
`r=0`; hence

\[
 \boxed{\mathcal P(TA)=\mathcal P(A)}.               \tag{6.2}
\]

The proof of Theorem B also applies verbatim: for every short direction,

\[
 \sum_{r\ne0}\binom{B_w(r)}2\ge {M_w\over2},
\]

so dense vector-Sidon arrays satisfy

\[
 \boxed{\mathcal P(A)\ge c_Ck^4.}                   \tag{6.3}
\]

On the Costas rows `p=11,23,43,47,59`, the exact invariant values are

\[
 1764,\ 53442,\ 762092,\ 1127250,\ 2848616,          \tag{6.4}
\]

respectively; the last is `0.2517... k^4`.  Therefore replacing `Q` by the
flat sufficient estimate

\[
 \mathcal Q_\Sigma\le O(\log m)\mathcal P
\]

does not repair the issue.  It removes the harmless dyadic factor while
retaining the affine-rigid fourth-order population.

There is an exact line-restriction identity.  For

\[
 S(\theta)=|\widehat{1_A}(\theta)|^2-k,
\]

put `E_w=sum_r B_w(r)^2`.  Then

\[
 E_w=\int_0^1|S(tJw)|^2\,dt,
 \qquad
 \mathcal P(A)
 ={1\over2}\sum_w(E_w-N)
   -\sum_w\binom{2e_w}2.                            \tag{6.5}
\]

The correction subtracts the `r=0` fibres.  Formula (6.5) is the precise
harmonic interpretation of `P`: it is off-axis `L^2` energy of restrictions
of the positive-definite difference polynomial to rational frequency lines.

## 7. The clean centroid count: a third conditional casualty

The global clean midpoint quantity

\[
 \sum_wH_w=3|\mathcal H_A|
\]

is affine invariant, because an invertible affine map preserves zero-sum
difference triples and all endpoint labels.  It retains the actual closing
gap and six-endpoint cleanliness, but this does not remove the dense affine
obstruction.

Indeed let

\[
 E_3(A)=|\{(a,b,c,d,e,f)\in A^6:a+c+e=b+d+f\}|.
\]

Cauchy--Schwarz gives

\[
 E_3(A)\ge {k^6\over |3A|}\ge {k^6\over(3m+1)^2}.
                                                               \tag{7.1}
\]

Only `O(k^3)` of these sextuples repeat a label.  For an equality between a
positive and a negative position, cancel the common label and use
`E^+(A)=2k^2-k`, which follows from vector-Sidonicity.  For an equality
between two positions of the same sign, fix the common point and two
opposite-sign points; the remaining directed edge is unique.  The exceptional
zero edge would give a nontrivial three-term progression in `A`, impossible
by directed-difference uniqueness.  A union bound over the fifteen pairs of
positions proves the `O(k^3)` assertion.

Thus (7.1) leaves `Omega_C(k^4)` six-distinct-label zero-sum difference
triples.  Each unordered clean three-edge hyperedge has at most
`2^3 3!=48` ordered oriented endpoint labellings.  The exact clean-hyperedge
identity `sum_w H_w=3|\mathcal H_A|` then proves Theorem C.

On exactly the same transformed sets as (5.2), exact enumeration gives

\[
\begin{array}{c|r|c|c}
p&\sum_wH_w&(\sum_wH_w)/(k^3+m^2)&(\sum_wH_w)/k^4\\ \hline
11&216&0.0806&0.0216\\
23&18684&0.6719&0.0399\\
43&338904&0.7554&0.1089\\
47&517932&0.9576&0.1157\\
59&1365624&0.9081&0.1207
\end{array}                                             \tag{7.2}
\]

The last column, not the small-prime target ratio, reveals the asymptotic
warning: it stabilizes near a positive fourth-order constant.  The ratio to
`k^3+m^2` is still near one only because the displayed matrices have sizeable
absolute constants in their `sqrt(p)` coefficients.  If uniformly balanced
separators exist, that ratio grows by a full power of `k`.

This corrects the tempting but false conclusion that endpoint cleanliness
alone makes the global midpoint estimate safe.  Its status is now exactly
the same conditional one as `Q/P`: the missing issue is existence of an
asymptotically balanced Euclidean separator.

The classical Lefmann--Thiele theorem, [*Point sets with distinct
distances*](https://doi.org/10.1007/BF01299744), Combinatorica 15 (1995),
379--408, proves directly that an `m` by `m` grid
contains a distance-Sidon subset of size `Omega(m^(2/3))`.  It does **not**
supply the missing separator: its set is already sparse at critical scale,
and (7.1) then gives only the target-order `Omega(k^3)` lower bound.  Nothing
in that result identifies the set as a balanced affine image of a dense
`k`-point vector-Sidon array.  Thus the known optimal-order grid construction
neither proves nor refutes the affine Costas obstruction.

## 8. Fourier interpretation and the correct surviving target

Thus the pair cap in (1.1) is a truncated `L^2` energy of restrictions of
the positive-definite difference polynomial to rational frequency lines.
The affine law (1.2) shows why a bandwise large sieve based only on ambient
height cannot work: a determinant-`p` map makes the physical box
`p^(1/2)` times wider while merely rescaling all determinant frequencies by
`p`.  Dyadic line energy is unchanged up to constants.

The large-positive-spectrum gate in
`LARGE_POSITIVE_SPECTRUM_RECTIFICATION_GATE.md` remains valid because it
uses the full two-dimensional Haar measure.  What fails is replacing the
actual closed gap correlation by independent line energy.  A viable repair
is one of:

1. retain
   `sum_{g in G}|S_{w,r} cap (S_{w,r}-g)|` rather than the local minimum;
2. retain the lattice covolume and anisotropy of the affine realization in
   the line restriction; or
3. charge the line mass back to two-dimensional positive-spectrum measure
   with endpoint and actual-gap compatibility still present.

## 9. Verification

Run

```text
python3 phase2/loop/erdos1208/verify_closed_fibre_q_affine_dense_costas_barrier.py
```

The verifier checks, using exact integer arithmetic:

* the direction/content/residue transformation laws (2.1)--(2.4);
* affine quasi-invariance and exact equality for power-of-two determinant;
* the local collided-mass inequality (3.2)--(3.5);
* every full `Q` value in (5.2);
* every global `P` value in (6.4), the line-restriction identity (6.5), and
  every clean midpoint total in (7.2);
* distance-Sidonicity, determinant, height, and coefficient scale for all
  rows in (5.2)--(5.3).

The verifier does not extrapolate the finite Costas search into an infinite
family.  The durable theorem is (1.2)--(1.3); the durable warning is that the
proposed final `Q` bound is one balanced-separator theorem away from being
false by a full power.
