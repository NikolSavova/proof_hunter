# Linear-codimension capped Hall: a selected same-edge chain is harmless

**Date:** 2026-08-14.  All logarithms are base two.  The empty convex
subset is counted.

## Verdict

The universal-chain obstruction disappears after the quantifiers are put
in the order required by capped Hall.  At rank

\[
                 r=(\alpha+o(1))\log n,\qquad 0<\alpha<1,
\]

the cap is polynomial, `d=n^(1-alpha+o(1))`, but a selector chooses at most
`d` **actual repair incidences above each actual source**.  It does not get
to regard all complete paths through those incidences as new records.

For one fixed-edge insertion chain, an incidence

\[
                 B+x_i\longrightarrow B+x_j\qquad(i<j)
\]

is injectively encoded by the ordinary two-point face `{x_i,x_j}`.  More
strongly, the whole first-divergence mass whose two records have the same
outer core `B` has constant-congestion encoding into an ordered pair of
ordinary faces.  One coordinate records `B`; the other is an arbitrary
convex face of the chain pocket used as a codeword.  The universal
Erdos--Szekeres lower bound makes that pocket codebook larger than all
ordered pairs of chain incidences.

Thus a selected same-edge chain is not a scalable obstruction, at linear
codimension or at any other cap.  The only part not discharged here is the
cross-core term: ordered records based at two genuinely different outer
cores.  A counterexample there would need quadratic outer-core entropy and
would have to prevent any product-like coexistence between core and pocket
face reservoirs.  That is the already-isolated crossing-pocket/OAI gate,
not the universal-chain example.

## 1. Setup and the quantifier correction

Let `X={x_1,...,x_N}` be in strict insertion-chain order behind a chord
`uv`, so

\[
 x_i\in\operatorname{int}\operatorname{conv}\{u,v,x_j\}
                    \quad(i<j).                         \tag{1}
\]

Let `B` be a convex outer core containing the chord and suppose every
`B+x_i` is convex.  Then (1) gives the repair relation

\[
 \operatorname{ext}(B\cup\{x_i,x_j\})=B\cup\{x_j\}.
                                                               \tag{2}
\]

A unit-weight capped selection is a simple set

\[
 E_B\subseteq\{(i,j):1\le i<j\le N\},\qquad
 \deg^+_{E_B}(i)\le d.                                  \tag{3}
\]

The word *simple* is important.  If many complete histories traverse the
same arrow `(i,j)`, they are not many actual incidences.  They must be
collapsed before (3) is applied.  Retaining their path multiplicity changes
the statement back into the uncapped full-history problem and is not a
capped-Hall selector.

Of course

\[
                       |E_B|\le\min\{dN,{N\choose2}\}.      \tag{4}
\]

## 2. An immediate incidence route

> **Theorem 1 (two-point route).**  For a fixed outer core `B`, the map
> \[
>                   (i,j)\longmapsto\{x_i,x_j\}             \tag{5}
> \]
> is an injection from `E_B` to the ordinary convex faces of the ambient
> point set.  Consequently `|E_B|<=V(P)` with congestion one, independently
> of `d`.

**Proof.**  Every two distinct points form a convex set, and the labelled
pair recovers `i,j`; the chain order recovers their direction.  QED.

This already kills the fixed-core immediate-chain obstruction.  It also
explains why the old count `binom(N,h)` was misleading at the capped scale:
the same `O(N^2)` arrows occur in exponentially many paths.

For a family `C` of distinct outer cores which all use the same pocket
`X`, there is an equally exact two-face code for a single incidence:

\[
                  (B,i,j)\longmapsto (B,\{x_i,x_j\}).       \tag{6}
\]

Both coordinates are ordinary convex faces and the code is injective.
Thus repeated cores create no issue until a proof asks two output faces to
encode an **ordered pair** of records.

## 3. Exact same-source first divergence

At one actual source `B+x_i`, two distinct selected successors `x_j,x_k`
give an ordered first-divergence pair.  Send it to

\[
       ((i,j),(i,k))\longmapsto(B,\{x_i,x_j,x_k\}).          \tag{7}
\]

> **Theorem 2 (explicit triple telescope).**  Across any family of outer
> cores, the map (7) has congestion at most two.

**Proof.**  Three points in general position form an ordinary convex face.
The first coordinate recovers `B`.  Within the second coordinate the chain
minimum is `i`, since both repairs point forward.  The other two labels are
`j,k`; only their order is forgotten.  QED.

In particular, writing `q_(B,i)=deg^+_E(B,i)`,

\[
 \sum_{B\in C}\sum_iq_{B,i}(q_{B,i}-1)
       \le2|C|{N\choose3}\le2V(P)^2.                        \tag{8}
\]

The first inequality is also visible directly: a triple can occur only
with its smallest chain label as the source and in the two successor
orders.  Fractional selected weights `0<=a_(i,j)<=1` obey the same bound,
because each of those two contributions has weight at most one.

## 4. All within-core record pairs, not only a common source

The preceding triple code is constructive but only treats two records
with the same current tip.  At the global first-divergence scale one may
want all ordered distinct pairs in `E_B`.  They are still harmless.

Use the universal planar lower bound: for every fixed `c<1/4` and all
sufficiently large `N`, every `N`-point set satisfies

\[
                        V(X)\ge2^{c(\log N)^2}.              \tag{9}
\]

Hence, for all sufficiently large `N`,

\[
                        V(X)\ge N^4\ge |E_B|^2,              \tag{10}
\]

where the last inequality uses the simple-incidence bound
`|E_B|<=binom(N,2)`.  Choose any injection

\[
             \psi_B:E_B^{\ne2}\hookrightarrow\mathcal F(X).
                                                               \tag{11}
\]

> **Theorem 3 (same-core capped first-divergence theorem).**  Let `C` be
> any family of outer cores, all with the same strict insertion-chain
> pocket `X`.  For every core choose an arbitrary simple capped incidence
> set `E_B`.  The ordered pairs of distinct records which have a common
> core admit the congestion-one code
> \[
>         ((B,e),(B,f))\longmapsto(B,\psi_B(e,f))
>                    \in\mathcal F(P)^2.                    \tag{12}
> \]
> For the finitely many smaller values of `N`, source projection gives a
> uniform constant depending only on the threshold in (10).  Therefore
> the same-core first-divergence contribution has `O(1)`, hence
> `n^{o(1)}`, global reuse for every cap `d<=N`.

**Proof.**  Equation (10) gives (11).  In (12), the first face recovers the
core and the second recovers the ordered record pair using the codebook
chosen for that core.  Distinct cores cannot collide in the first
coordinate.  If `N` is below the fixed threshold, there are only `O(1)`
possible incidences, so the elementary source-pair route has `O(1)` load.
QED.

The same proof permits fractional selection weights in `[0,1]`: after the
support pairs are assigned distinct codewords, the weight on any codeword
is `a_e a_f<=1`.  It does not permit duplicating one geometric incidence
with an integer path multiplicity; that is exactly the quantifier error
excluded after (3).

This theorem permits arbitrary pocket order type.  A convex subset of `X`
remains a convex subset after the outer points are adjoined, so every
codeword in (11) is an ordinary ambient face.  No coexistence with the
tangent guards is asserted or needed: `B` and the pocket codeword occupy
the two different output slots.

The use of an arbitrary pocket face as a codeword is legitimate for the
global EIC and for a guard-release telescope whose right side consists of
ordinary face families.  If one imposes a narrower, record-local target
neighbourhood, Theorem 3 need not respect it; Theorem 2 is the constructive
local statement.

At linear codimension a source which attains the full cap has at least
`d=n^(1-alpha+o(1))` available successors, so its pocket size tends to
infinity polynomially and (10) holds with enormous room.  If the available
successor pool is only `n^o(1)`, plain source projection already has
`n^o(1)` congestion.  These two cases cover every same-core chain slice.

## 5. What remains: cross-core pairs

Let `e_B=|E_B|`.  The complete ordered-pair mass decomposes exactly as

\[
 \left(\sum_Be_B\right)^2-\sum_{B,e\in E_B}1
 =\underbrace{\sum_Be_B(e_B-1)}_{\text{same core}}
  +\underbrace{\sum_{B\ne C}e_Be_C}_{\text{cross core}}.    \tag{13}
\]

Theorem 3 discharges the first term.  It says nothing about the second.
For a cross-core pair, the two available output slots must jointly remember

\[
                  B,\quad C,\quad e\in E_B,\quad f\in E_C. \tag{14}
\]

Using `(B,C)` forgets the two incidence words and has possible load `d^2`;
using the two pocket codes forgets the two cores.  Four separate face slots
would make the problem trivial, but only two are available.  The missing
geometric assertion is precisely that enough ordinary faces combine some
core information with some released pocket information.

Existing source-cloud entropy already shows that a family with
`log|C|=o(r^2)` cannot obstruct the capped global bound.  Therefore a
surviving cross-core family must have

\[
                         \log|C|=\Omega(r^2),                \tag{15}
\]

as well as polynomially many selected successors per typical source.  A
scalable planar counterexample to the desired guard-release telescope would
have to realize (15), reuse essentially the same pocket codebooks across
those cores, and nevertheless avoid the mixed core--pocket face reservoir
which normally appears when guards are released.  The fixed-core universal
chain does none of these things.

This identifies the correct attack boundary:

\[
 \boxed{\text{capped same-edge histories are closed; only quadratic-entropy
 crossing cores remain.}}                                      \tag{16}
\]

Producing the required nonproduct planar family would be a genuine new
barrier to the OAI/guard-release route.  Proving that such a family cannot
exist is the remaining crossing-core theorem.  Neither conclusion follows
from the universal-chain construction alone.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_linear_codim_capped/verify_linear_codim_chain.py
```

The checker uses exact rational coordinates for a strict insertion chain,
verifies every repair hull, exhausts all small capped selections, checks
the two-point injection and the sharp two-to-one triple telescope, audits
fractional weights, and checks the `N^4` codebook comparison at the
universal-bound exponent scale.
