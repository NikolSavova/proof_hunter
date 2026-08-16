# A fixed-power saving: exact reduction and the complete shield-bank branch

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

A uniform fixed power saving over source projection would be enough for the
mean-size route.  The exact target is: for a unit-weight selected family of
rank-`r=ell-g` exterior repairs, with at most `d=2^g` selected blockers over
each actual source,

\[
             |E|\le r^{O(1)}d^{1-\epsilon}V(P)              \tag{1}
\]

for one absolute `epsilon>0`.

The quadratic shield family in `QUADRATIC_CROSS_CORE_SHIELD.md` does **not**
refute (1).  Its local mixed faces have quadratic congestion, but the very
same two shield clouds form one complete convex-position bank.  That bank
pays all selected records with enormous room.

More generally, the complete two-sided core-product branch satisfies (1)
with congestion one.  This is a rigorous global
“mixed product or shield bank” theorem in the first nontrivial model.  What
remains is a stability/container extension: a merely quadratic-entropy
subfamily of the core product need not contain every choice, so a single
bad quadruple is not ruled out by entropy alone.

No general proof of (1) is claimed here.

## 1. Why a fixed power is sufficient

Put `ell=ceil(log n)`.  Here is the exact conditional implication using the
already-banked rank-width and optimized-hull reductions.

> **Theorem 1 (fixed saving implies asymptotic peak mean).**  Suppose there
> is an absolute `epsilon>0` such that every selected exterior-repair family
> of cap `h` at ranks `Theta(log n)` satisfies
> \[
>                  |E|\le n^{o(1)}h^{1-\epsilon}V(P),        \tag{2}
> \]
> uniformly in the rank.  Then every positive-growth peak obeys
> \[
>                         \mu_1=(1-o(1))\log_2n.              \tag{3}
> \]
> Consequently the ACP/KL reduction closes the leading coefficient `1/2`.

**Proof.**  Suppose instead that along a subsequence
`mu_1<=(1-delta)ell` for some fixed `delta>0`.  The established
`Delta<1` rank-width theorem and low-addable reduction give a rank

\[
                         r=\mu_1+O(1)                         \tag{4}
\]

containing at least `cV(P)` hard low-addable sources, for an absolute
`c>0`.  Put `g=ell-r`; then

\[
                         g\ge\delta\ell+O(1).                 \tag{5}
\]

The optimized-hull tail removes only `K V(P)/2^g=o(V(P))`
sources, where `K=n^{o(1)}` is the established recovery factor.  Every
remaining source has at least

\[
                         h={2^g\over K}=n^{\delta+o(1)}       \tag{6}
\]

distinct exterior blockers.  Select exactly `h` over each remaining actual
source.  This is a simple capped selector and gives

\[
                         |E|\ge(c-o(1))hV(P).                 \tag{7}
\]

On the other hand (2) gives

\[
                         |E|\le n^{o(1)}h^{1-\epsilon}V(P).  \tag{8}
\]

After division, (7)--(8) say
`h^epsilon<=n^{o(1)}`, contradicting (6).  Hence no fixed `delta` exists,
which proves (3).  The last assertion is the established ACP/KL
implication.  QED.

There is also a sharper rankwise version when the tail/recovery factor is
polynomial.  If one can select `d=2^g` repairs above each of
`N_(ell-g)` sources and (1) has prefactor at most `ell^C`, then

\[
 {N_{\ell-g}\over V(P)}
       \le \ell^C2^{-\epsilon g}.                           \tag{9}
\]

Taking `G=((C+3)/epsilon)log_2 ell` makes the sum over `g>=G`
`O(ell^-3)`.  In the quantitative form of the deletion reduction this is
the advertised route to an `O((log log n)^2)` mean deficit.  Theorem 1 is
the unconditional asymptotic consequence needed for the leading
coefficient; it does not assume that the current `n^{o(1)}` recovery factor
is already polynomial.

Thus (1) is stronger than needed for the leading coefficient but strictly
weaker than an injective global EIC map.

## 2. Complete two-sided core products force a full face bank

The key planar fact is four-local.

> **Lemma 1 (four-point certificate).**  A finite planar general-position
> set `Q` is in convex position if and only if every four-point subset of
> `Q` is in convex position.

**Proof.**  One direction follows by deletion.  Conversely, if `Q` is not
in convex position, some `x in Q` lies in `conv(Q-x)`.  By planar
Caratheodory, `x` lies in the triangle of three other points, giving a
nonconvex four-subset.  QED.

Now let `L,R` be disjoint point clouds of size `M`, let `D` be any fixed
face disjoint from them, and fix `s>=4`.  Assume

\[
 D\cup S\cup T\quad\hbox{is a face for every}
 \quad S\in{L\choose s},\ T\in{R\choose s}.                 \tag{7}

> **Theorem 2 (complete shield-bank theorem).**  Under (7), `L union R` is
> in convex position.  Consequently
> \[
>                         V(P)\ge2^{2M}.                     \tag{8}
> \]

**Proof.**  Take any four-point subset `Q` of `L union R`.  Since `s>=4`,
extend `Q cap L` to an `s`-set `S subset L` and `Q cap R` to an `s`-set
`T subset R`.  Equation (7) and deletion imply that `Q` is convex.  Lemma 1
now proves that `L union R` is convex, and all of its subsets are ordinary
faces.  QED.

The statement is global: the paying faces need not coexist with `D` or
with a pocket incidence.

There is a quantitative, albeit very-high-density, stability extension.
Let `C` be only a subfamily of the pairs in (7), and write

\[
 \eta=1-{|C|\over\binom Ms^2}.                                \tag{8a}
\]

> **Corollary 3 (exponentially thin completeness threshold).**  If
> \[
>                  \eta<\left({s-3\over M}\right)^4,         \tag{8b}
> \]
> then `L union R` is still in convex position and (8) holds.

**Proof.**  If a four-set `Q subset L union R` is nonconvex and
`a=|Q cap L|`, every core pair containing `Q` is absent from `C`.  Its
fraction in the complete product is

\[
 { (s)_a\over(M)_a}{(s)_{4-a}\over(M)_{4-a}}
 \ge\left({s-3\over M}\right)^4,                            \tag{8c}
\]

since every one of the four successive numerator factors is at least
`s-3` and every denominator factor is at most `M`.  This contradicts
(8b).  Hence every four-set is convex, and Lemma 1 applies.  QED.

At `M=2^{Theta(rho)}`, the threshold in (8b) is
`2^{-Theta(rho)}`.  Thus it is relevant to a fixed-power saving, whose
desired gain also has a linear exponent, but it does not cover a general
quadratic-entropy subfamily of constant or exponentially small density.

## 3. The complete product satisfies the power saving injectively

There are

\[
                         K={M\choose s}^2                     \tag{9}

cores in (7).  Suppose each core supports at most `q` actual source faces,
and each source selects at most `d` repairs.  Then

\[
                         |E|\le Kqd.                          \tag{10}

The face bank in Theorem 2 pays every record injectively whenever

\[
                         Kqd\le2^{2M}.                        \tag{11}

In the linear-codimension shield scaling, source rank
`rho=2s+|D|+1=Theta(s)`,

\[
 M=2^{\lambda\rho+O(1)},\qquad
 q\le n=2^{O(\rho)},\qquad d\le n=2^{O(\rho)}.               \tag{12}

But

\[
 \log(Kqd)\le2s\log(eM/s)+O(\rho)=O(\rho^2),                \tag{13}
\]

whereas `log 2^(2M)=2M=2^{Theta(rho)}`.  Therefore (11) holds
with double-exponential room.  In fact this branch has

\[
                         |E|\le V(P),                          \tag{14}

which is stronger than (1) for every `epsilon<=1`.

For the exact shield construction, `q=d` (the first `d` chain tips are
sources and the last `d` are successors), so (10) is precisely
`|E|=Kd^2`.  The record-local universe has quadratic overload, as proved in
the companion note, while the unrestricted bank (8) gives an injection.
This is an exact demonstration that local congestion is the wrong statistic
for (1).

## 4. Why quadratic entropy alone does not trigger Theorem 2

Completeness in (7) is load-bearing beyond the narrow range of Corollary 3.
If one prescribed four-set `Q` is
nonconvex, the forbidden core pairs are only those containing `Q`.  If
`a=|Q cap L|`, their fraction in the complete product is exactly

\[
 { (s)_a\over(M)_a}{(s)_{4-a}\over(M)_{4-a}}
       \le\left({s\over M-s+1}\right)^4.                     \tag{15}

For `M=2^{Theta(rho)}` and `s=Theta(rho)`, (15) is
`2^{-Theta(rho)}`.  Removing all those core pairs leaves

\[
 (1-2^{-Theta(rho)}){M\choose s}^2
       =2^{Theta(rho^2)}                                     \tag{16}

cores.  Thus the assertion “quadratic source entropy forces every shield
quadruple to be convex” is false even as a set-system inference.

A proof of (1) needs an aggregate statement: either sufficiently many core
pairs coexist to generate many convex shield subsets, or the missing core
pairs/repair incidences themselves admit a power-saving charge.  Checking
one quadruple, one fixed codimension, or one local Hall neighbourhood cannot
give that aggregate conclusion.

This isolates a concrete sufficient extension of Theorem 2.

> **Open shield stability target.**  Let `C` be a rank-`rho` family of
> convex cores, with `d` selected exterior repairs per source.  Prove that
> either the union of all core-compatible shield complexes contains at
> least `d^epsilon|C|` ordinary faces, or the mixed repair faces themselves
> contain that many, for one universal `epsilon>0`.

Unlike a two-face coefficient decoder, this is a one-record global count.
It is exactly strong enough for (1) and does not demand an injective or
record-local assignment.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_quadratic_cross_core/verify_fixed_power_shield_bank.py
```

The checker exhausts the four-point implication for small abstract bad-quad
systems, verifies the exact forbidden fraction (15), audits the complete
product counts, and checks the linear-codimension asymptotic inequalities
with exact integers.
