# Perfect fresh-partner resets without a tangent cup

**Date:** 2026-08-15. All constructions are rational, stretchable, and in
general position. A physical pair node means an actual two-label subset of
one class.

> **Rank strengthening.** The later exact profile audit
> ARBITRARY_CHILD_ES_POWER_PROFILE_BELLMAN.md proves
> \(r_C=r_U=5h+1\) and \(r_W=10h\). The \(10^h\) estimates below remain
> valid upper bounds, but are deliberately superseded and must not be used
> for second-order accounting.

## Verdict

Perfect common-support reset matchings do **not** force a tangent-like
global cup or cap. There is an exact 252-point base with

\[
        t_0=14,\qquad |Y_i|=18,\qquad m_0=9,           \tag{1}
\]

such that every class pair has a perfect matching of nine bad `2+2`
circuits, every physical label has load 13, every physical pair node has
degree one, and there are no pair-node triangles. Nevertheless the whole
base has maximum ordinary convex rank at most 10, strictly less than the
number of classes.

Lexicographic powers give, for every `h>=1`, a rational perfect reset with

\[
 \boxed{
 t=14^h,quad |Y_i|=18^h=2m,quad
 d(x)=t-1,quad \Delta_{\rm pair}=1,quad
 \operatorname{rank}_{\rm conv}\le10^h.}              \tag{2}
\]

Thus

\[
 \operatorname{rank}_{\rm conv}
       \le t^\rho,qquad
 \rho=\log_{14}10=0.87250\ldots<1.                    \tag{3}
\]

Every cup, cap, colorful endpoint word, and one-point-per-cell source word
is an ordinary set, so all such global banks are limited by (2). This is a
scalable counter-regression in the exact full-support/high-reuse residue,
not merely the source-inflated twelve-point branch.

The conclusion is stable under near-perfect padding. If each class has

\[
             |Y_i'|=(1+\varepsilon)2m                \tag{4}
\]

and the perfect reset is retained on its common `2m`-label core, distribute
the extra labels among infinitesimal cells around the core labels. Then

\[
 \overline d={t-1\over1+\varepsilon},qquad
 \operatorname{rank}_{\rm conv}(P')
       \le\lceil1+\varepsilon\rceil10^h.              \tag{5}
\]

In particular the rank remains `o(t)` whenever
`1+epsilon=o(t^(1-rho))`; here `1-rho=0.12749...`. Exact perfection
(`epsilon=0`) is already a counterexample, so no positive theorem can be
recovered by taking `epsilon` smaller.

This does not construct a least-face counterexample to Erdos 838. Rich
multi-point traces placed inside one infinitesimal cell can still create
endpoint-profile payments. What (2) rules out is the proposed geometric
implication

```text
perfect fresh-partner reset + stretchability
    => tangent-like linear-rank global cup/cap/source bank.
```

The remaining possible positive operation must use multi-point endpoint
profiles or a weighted fan deletion, not a global representative
transversal.

## 1. The 252-point rational base

Use the classical cup--cap lower construction. Let `E(r,s)` be an
`x`-ordered rational set with no `r`-cup and no `s`-cap. Recursively put a
normalized copy of `E(r,s-1)` high and left of a normalized copy of
`E(r-1,s)`, with every cross slope below every internal slope. Then

\[
                 |E(r,s)|=\binom{r+s-4}{r-2}.         \tag{6}
\]

A crossing cup uses at most one point of the high-left block, while a
crossing cap uses at most one point of the low-right block. This proves the
claimed avoidance by induction. The verifier uses the explicit separation
height

\[
                  M=\lceil3S+5\rceil,                 \tag{7}
\]

where `S` bounds all internal absolute slopes.

Take `E(7,7)`, of size `binom(10,5)=252`. Its longest cup and cap both have
rank six. Every convex `x`-ordered set is the union of its lower cup and
upper cap, sharing its two endpoints, so

\[
                     \operatorname{rank}_{\rm conv}E(7,7)\le10. \tag{8}
\]

Partition these points into fourteen 18-label classes. The exact verifier
deterministically finds, and then independently recertifies, the following
data:

* for every `i<j`, partitions of `Y_i` and `Y_j` into nine physical pairs;
* a matching of those two nine-pair factors whose nine unions are all
  strict nonconvex `2+2` circuits; and
* across the thirteen neighbours of any fixed class, all 117 selected
  physical pairs are distinct.

Therefore every neighbour matching covers all 18 labels. Every label has
load 13, while the auxiliary pair graph is itself a matching with

\[
                     9\binom{14}{2}=819               \tag{9}
\]

edges. This proves all assertions in (1). The construction was found by an
exact fixed-seed search, but the verifier checks only literal rational
determinants and physical incidences when certifying the output.

## 2. Lexicographic power and perfect factors

Let `B` denote the base order type. Its `h`-fold lexicographic power is
obtained by replacing every point of `B` by a sufficiently small rational
affine copy of `B^(h-1)`. Finite strictness permits rational scales; generic
rational shears remove the remaining collinearities. A final point has:

* a class-colour word `c=(c_0,...,c_(h-1)) in [14]^h`; and
* a local-label word `a=(a_0,...,a_(h-1)) in [18]^h`.

Hence there are `14^h` classes of size `18^h`.

Fix two distinct class words `c,d`, and let `ell` be their first differing
coordinate. Use the base perfect factor between colours `c_ell,d_ell`.
For each common local prefix in `[18]^ell`, each of its nine base pairs,
and every suffix index in `Z/(18^(h-ell-1))`, pair the two suffixes with a
cyclic shift encoding the neighbour colour suffix
`(d_(ell+1),...,d_(h-1))` in base 14.

There are enough shifts because

\[
                    14^{h-\ell-1}\le18^{h-\ell-1}.    \tag{10}
\]

The resulting factor contains

\[
  9\cdot18^\ell\cdot18^{h-\ell-1}
        ={18^h\over2}                                 \tag{11}
\]

pairs and covers the class. Match it to the corresponding factor in class
`d` using the base circuit matching and identical local-prefix/suffix
indices. The four labels share every earlier lexicographic cell and occupy
the four cells of a bad base circuit at coordinate `ell`. Their union is
therefore a bad `2+2` circuit.

A physical pair decodes its neighbour exactly. Its first differing local
coordinate reveals `ell`; the base pair reveals `d_ell`, because the base
pair nodes have degree one; and the suffix shift reveals the base-14
neighbour suffix. Thus no physical pair is reused. Since every factor is
perfect, every label occurs once against each of the other `14^h-1`
classes. This proves the matching and load assertions in (2).

## 3. Rank bound and the missing tangent bank

Let `R_h` be the maximum convex rank of `B^h`. If `F` is convex, its active
first-level cells form a convex subset of `B`: selecting one label from
each active cell preserves the base chirotope. There are at most ten such
cells. The trace in each active cell has rank at most `R_(h-1)`. Therefore

\[
                  R_h\le10R_{h-1},\qquad R_1\le10,    \tag{12}
\]

which proves `R_h<=10^h`.

One may further replace each final macro label by a `D`-point child and
expand every circuit indexwise. The reset remains perfect, with pair-node
degree one. Any representative face using at most one physical label per
final macro cell still activates at most `10^h` cells. If `M=252^h` is the
number of macro cells, the entire representative bank is bounded above by

\[
             \sum_{q\le10^h}\binom MqD^q.             \tag{13}
\]

When `14^h=Theta(log n)` and `D=n/polylog(n)`, the base-two logarithm of
(13) is

\[
 O\bigl((\log n)^\rho\log n\bigr)
       =o((\log n)^2).                                \tag{14}
\]

Thus this exact perfect reset defeats the half-scale tangent mechanism
based on one choice per macro cell. Equation (13) does not bound faces
with multi-point child traces; those are the explicitly surviving profile
branch.

## 4. Stability and the common-label fan

For near-perfect padding, replace every macro point by a rational
infinitesimal cell containing either `floor(1+epsilon)` or
`ceil(1+epsilon)` labels, distributed to obtain the desired integer class
size. Retain one distinguished core label in every cell for the reset.
Every active cell contributes at most `ceil(1+epsilon)` labels to a convex
set, proving (5). The selected incidence sum in one class remains

\[
                         2m(t-1),                      \tag{15}
\]

so the average load in (5) is exact.

For a fixed core label `x`, its `t-1` partners are all distinct. Any radial
or cyclic ordering of them has the expected Erdos--Szekeres monotone
subsequence. The counterexample shows that this fact alone cannot yield a
linear-rank global fan bank: even the union of all classes has convex rank
at most `10^h`. A `sqrt(t)` fan is consistent with (3), since
`sqrt(t)<t^rho`. Circuit elimination must therefore retain a multi-point
endpoint profile or delete a visible branch; monotone partner order alone
does not contradict the construction.

## 5. Verification

Run

```text
python3 phase2/loop/erdos838/agent_many_class_partner_reset/verify_perfect_reset_lexicographic_counter.py
```

The exact verifier constructs all 252 rational coordinates, checks
2,635,500 ordered triple states in the cup/cap dynamic program, obtains
longest cup/cap ranks `(6,6)`, deterministically reconstructs all 819 bad
circuits, and checks label load 13, pair-node degree one, and zero
pair-node triangles. It exhausts the 31,590 physical pair nodes incident
with one class in the second lexicographic power and checks exact
fresh-partner decoding. Finally it checks powers `1<=h<=8` and the padded
rank/load ledger.

The scalable power theorem is proved symbolically in Sections 2--4; the
finite verifier certifies its complete rational base and the nontrivial
suffix-factor decoder.
