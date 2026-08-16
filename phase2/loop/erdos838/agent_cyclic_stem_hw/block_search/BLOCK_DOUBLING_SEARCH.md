# Block-doubling obstruction search

**Date:** 2026-08-14  
**Verdict:** adjacent doubling is decisively false at consecutive dyadic
boundaries, including for cumulative prefixes.  The first surviving block,
`b=2`, was not killed.  More importantly, every natural attempt to scale the
finite failures by homogeneous vertical substitution repairs adjacent
doubling after at most two further levels.  Thus this search found a genuine
finite obstruction and a precise nonstationary danger, but no scalable
counterexample to the `b=O(log log n)` target.

Write

\[
 v_k(P)=\#\{A\subseteq P:|A|=k,\ A\text{ is in convex position}\},
 \qquad \ell=\lceil\log_2|P|\rceil.
\]

The block condition under attack is

\[
 (\mathrm{BD})_b:\qquad v_{k+b}\ge 2v_k
 \quad(0\le k\le \ell-2b).
\]

## 1. Exact stretchable failures at `n=65` and `n=129`

The verifier constructs two integral general-position point sets.  Both use
the saved 58-point onion configuration as a macro, followed by very small
integral clusters.  The first replaces its deepest point by an eight-point
cluster.  Its exact profile through the needed rank is

\[
 (v_0,\ldots,v_6)
 =(1,65,2080,43680,353852,863119,788398).
\]

Here `ell=7`, and at the final adjacent test

\[
 {v_6\over2v_5}={394199\over863119}=0.4567145\ldots.       \tag{1}
\]

Thus `(BD)_1` fails by more than a factor two.

For the second example, 45 of the 58 macro points are replaced by
two-point vertical clusters and thirteen by three-point clusters.  This gives
129 integral points and

\[
 (v_0,\ldots,v_7)=
 (1,129,8256,349504,5832916,30290697,65584381,72859822).
\]

Now `ell=8`, and

\[
 {v_7\over2v_6}={36429911\over65584381}=0.5554662\ldots.   \tag{2}
\]

The mechanism is a **dyadic-boundary resonance**.  The low-mean onion macro
has a descending upper tail.  Tiny heterogeneous clusters increase `n` just
past a power of two while moving the required adjacent test into that tail.
This is why the failure becomes substantially stronger than the earlier
17-, 44-, and 58-point examples.

These are exact stretchable examples, not allowable-sequence artifacts.  The
certificate uses integer slope comparisons, audits every tied slope to rule
out a shared endpoint (hence every collinear triple), and evaluates the
truncated rank polynomial by the exact endpoint-chain transvection identity.

## 2. Cumulative doubling also fails

Let `F_k=sum_(j<=k) v_j`.  Smoothing by prefix sums does not rescue adjacent
doubling.  The same examples give

\[
 {F_6\over2F_5}={2051195\over2525594}=0.812158\ldots
 \quad(n=65),                                      \tag{3}
\]

and

\[
 {F_7\over2F_6}={174925706\over204131768}=0.856907\ldots
 \quad(n=129).                                     \tag{4}
\]

So even the candidate cumulative inequality `F_(k+1)>=2F_k` fails at two
successive dyadic boundaries.

## 3. Block two survives with substantial slack

For the 65-point example the tightest `(BD)_2` test is

\[
 {v_5\over2v_3}={863119\over87360}=9.880025\ldots,          \tag{5}
\]

and for the 129-point example it is

\[
 {v_6\over2v_4}={65584381\over11665832}=5.621920\ldots.    \tag{6}
\]

Thus these examples have minimal block exactly two, but they are not close
to killing block two in the literal inequality.  A fixed-`x` integral
annealer was also written specifically to minimize the worst block-two
ratio.  A 20,000-candidate `n=65` run reached `9.626...` and no failure; a
separate corrected 4,000-candidate run, retaining every rank needed to audit
the reported minimal block, again found no near failure.  These are heuristic
negative results, not a proof of `(BD)_2`.

The prior exact census contains 59 distinct saved profiles.  None needs a
block larger than two.  The new examples therefore enlarge and sharpen the
`b=2` class but do not increase the record.

## 4. The resonance does not survive ordinary scaling

The main scalable test starts from the exact 129-point example and replaces
every point homogeneously by a sufficiently thin pair.  Cap, cup, and convex
profiles are propagated by the exact vertical-composition recurrence.  The
result is:

| pair depth | `n` | `ell` | minimal block | worst adjacent ratio to doubling |
|---:|---:|---:|---:|---:|
| 0 | 129 | 8 | 2 | 0.555466 |
| 1 | 258 | 9 | 2 | 0.837569 |
| 2 | 516 | 10 | 1 | 1.297191 |
| 3 | 1032 | 11 | 1 | 2.050753 |
| 4 | 2064 | 12 | 1 | 3.279197 |
| 5 | 4128 | 13 | 1 | 5.221392 |
| 6 | 8256 | 14 | 1 | 8.151613 |

The same self-healing occurs even faster for homogeneous iterations of the
44- and 58-point saved hard macros: depth one can fail adjacent doubling,
while depth two already passes.  Central Pascal towers and the three guarded
fixed-template towers pass adjacent doubling throughout every tested depth.

This is strong evidence that **repeating a bounded macro is the wrong way to
kill block doubling**.  Vertical substitution introduces powers of the old
population into successive coefficients; after a few levels these overwhelm
the finite upper-tail collapse.

## 5. What a genuine obstruction would have to do

The only live computational obstruction suggested by this lane is a
nonstationary one:

> At every new dyadic scale, construct a fresh low-mean macro whose rank
> profile begins descending exactly at `ell-O(b)`, then cross the boundary
> using heterogeneous clusters without allowing earlier levels to smooth the
> tail.

The `n=65` and `n=129` examples demonstrate the first two finite stages of
that phenomenon.  They do **not** give compatible nested stages, and the
homogeneous continuation provably fails in the exact recurrence.  Finding a
sequence with minimal block tending to infinity would amount to producing
increasingly sharp low-rank tails at fresh scales—essentially the same missing
nonstationary geometry that separates unrestricted Erdős 838 from all known
fixed-template constructions.

The most useful next computation is therefore not another fixed-template
iteration.  It is a direct search at `n=257` or `n=513` minimizing

\[
 \min_{k\le\ell-4}{v_{k+2}\over2v_k},
\]

seeded by genuinely new onion/order-type macros rather than by a blow-up of
the 129-point record.  A block-two failure would be the first evidence that
the required block can grow; another large safety margin would materially
strengthen the case for a universal constant-block theorem.

## 6. Artifacts

Run

```bash
python3 phase2/loop/erdos838/agent_cyclic_stem_hw/block_search/verify_block_resonance.py
```

It writes `block_resonance_certificate.json`, containing all coordinates,
profiles, raw block tests, prefix tests, and the exact homogeneous pair-tower
audit.

`block_profile_search.cpp` is the exact-integer fixed-`x` annealer.  Its
slope ordering uses `__int128`, and its truncated endpoint matrices use
unsigned 128-bit coefficients.

