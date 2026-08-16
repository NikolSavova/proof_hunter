# Dynamic two-record spend/reset: an exact counterexample and a neutral potential

**Date:** 2026-08-14  
**Verdict:** a natural untagged Kraft recursion is false on the realizable
fixed-outer long-ear product of ACP Proposition 26.  If the outer apex label
is forgotten at descent, the squared load `E^2/V^2` grows like `M^2`, and
even a full child source face is reused by all `M` apex choices.  Taking
`M=2^r` gives exponential, not `2^o(r)`, child reuse.

This is not a counterexample to the fully tagged hierarchical tangent-reset
gate.  When every entropy-bearing coordinate is retained until it either
spends in a compatible cross-union or is exposed as a child coordinate, all
three equality families have a sharp neutral quadratic potential.  The
potential is ordered-pair collision mass

\[
                         \mathscr E(\Pi)=\sum_{C\in\Pi}|C|^2, \tag{1}
\]

where `Pi` is the current partition of records by the complete tangent,
prefix, and child signature.  Refinement cannot increase (1), and a coherent
spend/reset step satisfies an exact conservation identity.  What remains
open is geometric: prove an `L^2` Carleson bound on reuse of the ordinary
face banks attached to those tagged cells.

No counterexample to ACP, Proposition 26, or the full hierarchical
tangent-reset statement is claimed.

## 1. Exact dynamic gate tested

At an active tagged cell `C`, take two ordered repair records.  If their two
rooted arcs satisfy the fixed-chord tangent criterion, spend the pair to the
injective cross-union face.  Otherwise retain the failed tangent comparison
and descend both records to the corresponding prefix/child cell.  A scalar
Kraft version would like to forget the old outer labels and charge the
descending records to ordinary faces in the child.

There are two different claims here.

1. **Untagged child claim (false).**  Erasing an outer label before descent
   creates only `2^o(r)` cumulative reuse of child faces.
2. **Tagged pair claim (not falsified).**  Keep every varying coordinate in
   the state until two records separate there.  Compatible separation spends;
   equal-coordinate pairs descend.  The total normalized collision mass is
   bounded.

The distinction is essential.  Ordinary Shannon entropy detects the lost
coordinate, but after it is erased it does not remember which child-face
charges came from its different values.  The quadratic potential (1) does.

## 2. Proposition 26 kills untagged descent

Use the realizable fixed-outer-cell long-ear product in ACP Proposition 26.
There are `a` retained microblocks, `b` hidden microblocks, and an `M`-point
outer apex cluster.  Put

\[
                         s=a+b.
\]

The record family is the full product

\[
                       E=M^{s+1}.                 \tag{2}
\]

Suppose the same-side reset deletes the apex coordinate and descends to the
internal retained/hidden product.  Even granting **every** partial
transversal as a child face, the distinct child bank has only

\[
                       V=(M+1)^s                  \tag{3}
\]

members.  Therefore

\[
 \boxed{
 {E^2\over V^2}
 =M^2\left({M\over M+1}\right)^{2s}.}             \tag{4}
\]

If `2s<=M+1`, Bernoulli gives

\[
                  {E^2\over V^2}\ge {M^2\over4}. \tag{5}
\]

Thus `M=2^r` produces squared overload `2^(2r-O(1))`.  This is already a
counterexample after crediting the whole Boolean child complex, not merely
one chosen child face.

The exact reuse distribution is worse than its minimum.  A partial
transversal occupying `t` of the `s` internal blocks is contained in

\[
                         M^{s-t+1}                 \tag{6}
\]

outer records: `M^(s-t)` completions of its missing internal coordinates
and `M` apex choices.  Hence

\[
 \begin{array}{c|c}
 \text{child face}&\text{reuse}\\ \hline
 \text{full internal transversal}&M\\
 \text{empty child face}&M^{s+1}=E.
 \end{array}                                      \tag{7}
\]

Counting all partial transversals, the mean squared reuse is exactly

\[
 {1\over(M+1)^s}
 \sum_{t=0}^s\binom st M^t M^{2(s-t+1)}
 =M^{s+2}.                                        \tag{8}
\]

The verifier checks the following scalable instances.

| `(a,b,M)` | `log2(E^2/V^2)` | minimum full-face reuse |
|---|---:|---:|
| `(4,4,16)` | `6.600595` | 16 |
| `(8,8,256)` | `15.820014` | 256 |
| `(16,16,65536)` | `31.998591` | 65,536 |

This identifies the precise false move: **the apex cannot be deleted as
mere outer-frame syntax.**  It is an entropy-bearing product coordinate.
The recursion must retain it, spend pairs which differ there, or recurse
into the apex cluster's own face complex.

### Tagged repair of the calculation

Retain all `s+1` size-`M` coordinates.  After exposing `i` coordinates,
there are `M^i` tagged cells of equal size `E/M^i`, so their normalized
collision mass is

\[
 {M^i(E/M^i)^2\over E^2}=M^{-i}.                 \tag{9}
\]

The cumulative collision Kraft sum is

\[
             \sum_{i=0}^{s+1}M^{-i}< {M\over M-1}. \tag{10}
\]

Thus the very family giving unbounded untagged reuse is neutral after the
lost coordinate is restored to the recursion state.

## 3. Parabolic nested prefixes are quadratically neutral

Let the discarded faces be the full prefix chain

\[
 D_0\subset D_1\subset\cdots\subset D_d,
 \qquad |D_j|=j.
\]

Charging every Boolean subface with multiplicity gives demand

\[
 E=\sum_{j=0}^d2^j=2^{d+1}-1,\qquad V=2^d.       \tag{11}
\]

Consequently

\[
 \boxed{{E^2\over V^2}=(2-2^{-d})^2<4.}          \tag{12}
\]

Although the empty face is reused `d+1` times, this worst fibre is
misleading.  A nonempty subset whose largest label is `m` is reused
`d-m+1` times, and there are `2^(m-1)` such subsets.  Therefore

\[
 {1\over2^d}\sum_{J\subseteq D_d}\operatorname{reuse}(J)^2
 ={(d+1)^2\over2^d}+\sum_{h=1}^d{h^2\over2^h}<7, \tag{13}
\]

with limit `6`.  The square-capacity Kraft sum is even sharper:

\[
 {\sum_{j=0}^d|2^{D_j}|^2\over|2^{D_d}|^2}
 ={1+4+\cdots+4^d\over4^d}< {4\over3}.           \tag{14}
\]

So the arbitrarily deep parabolic chain is not a counterexample to either
the original one-bit `L^1` reset or the quadratic two-record recursion.

## 4. Ramp--plateau: raw reuse explodes, tagged collision does not

Use the realizable vertical product with exponent word

\[
 (1,2,4,\ldots,L/2,
   \underbrace{L,\ldots,L}_{L/2\text{ copies}},
   L/2,\ldots,4,2,1),                             \tag{15}
\]

where `L=2^h`, block `i` has `m_i=2^(a_i)` labels, and

\[
                         N=\prod_i m_i.
\]

Let `V_atom` be the maximally generous atomic bank consisting of every
partial transversal plus every unordered two-endpoint interval target.
The exact formulas are

\[
 D=\prod_i(m_i+1),\qquad
 T=\sum_{i<j}\binom{m_i}{2}\binom{m_j}{2}
                   \prod_{i<q<j}(m_q+1),
 \qquad V_{atom}=D+T.                              \tag{16}
\]

For capped multiplier `d_0=2^(ell-b)`, the demand is `E=d_0N`.  The ramp
identities give

\[
 V_{atom}<21\left(1+\binom b2\right)N,
\]

so

\[
 {E^2\over V_{atom}^2}
 >{d_0^2\over 21^2(1+\binom b2)^2}.               \tag{17}

\]

This grows exponentially: the exact verified logarithms are

| `h` | `L` | `b` | `log2(E^2/V_atom^2)` |
|---:|---:|---:|---:|
| 6 | 64 | 44 | `41.015627` |
| 7 | 128 | 78 | `102.243615` |

Thus the ramp--plateau family is a second realizable counterexample to a
recursion which treats large blocks as atomic and charges only source
subfaces plus rank-two interval endpoints.  It is not a counterexample once
the internal block complexes are recursively exposed.

Indeed, a particular letter in block `i` is reused by `N/m_i` source
words—astronomical on the plateau and still larger in the small ramp
blocks.  But summing squared loads over all `m_i` tagged letters gives

\[
 {m_i(N/m_i)^2\over N^2}={1\over m_i}.            \tag{18}

\]

For (15),

\[
                         \sum_i{1\over m_i}<2.     \tag{19}

\]

The prefix-partition collision Kraft sum is also below two:

\[
 \sum_{i=0}^b{1\over m_1\cdots m_i}<2.            \tag{20}

\]

For both verified sizes it is `1.632843...`.  The exponential raw fibre is
exactly cancelled by the tiny collision probability that two independent
records retain the same exposed coordinates.

## 5. The sharp neutral potential

Let a tagged active cell contain `e` records and let its same-side descent
partition it into children of sizes `e_1,...,e_k`.  In a coherent candidate
recursion, pairs in different children are released at this step (and must
then be proved geometrically compatible), while pairs in one child descend.
The underlying pair-count identity is

\[
 \boxed{
 e^2=\underbrace{\left(e^2-\sum_j e_j^2\right)}_{
             \text{released/spent ordered pairs}}
       +\underbrace{\sum_j e_j^2}_{
             \text{descending collision mass}}.}             \tag{21}

\]

Iterating on a coherent recursion tree gives

\[
 E_{root}^2
 =\sum_{v}\operatorname{Spend}(v)
  +\sum_{\lambda\text{ terminal}}E_\lambda^2.     \tag{22}


This is the dynamic two-record analogue of Kraft equality.  It is exactly
neutral on product coordinates, sees the one-cell collapse in Proposition
26, and treats a long nested chain by the bounded square sums (12)--(14).
The verifier checks (21) directly and, for every product model, partitions
all ordered word pairs by their first unequal coordinate:

\[
 N^2=N+\sum_i
 \left(\prod_{q<i}m_q\right)m_i(m_i-1)
 \left(\prod_{q>i}m_q\right)^2.                  \tag{23}

\]

Equation (22) alone is not the missing planar theorem.  It counts record
pairs, while ACP must route them to ordinary faces with low congestion.
For an active history `v`, let `B_v` be its prefix/child face bank and let
`lambda_v=E_v/|B_v|` be its average load.  A sufficient face-side companion
would be an `L^2` Carleson reuse estimate such as

\[
 \sup_{F\in\mathcal F(P)}
 \sum_{v:F\in B_v}\lambda_v^2\le2^{o(r)},         \tag{24}


or a comparably strong hereditary capped version.  Proposition 26 proves
that (24) is false if histories differing in the apex label are merged;
the three regression families are consistent with it when full tags and
internal block recursion are retained.

## 6. Outcome for the hierarchical gate

The countersearch gives a sharp design constraint rather than a full
counterexample.

1. **Killed:** any scalar recursion which deletes an entropy-bearing outer
   coordinate and charges all descendants to an untagged child bank.
   Proposition 26 gives squared overload at least `M^2/4`.
2. **Killed:** an atomic all-interval recursion for ramp--plateau blocks.
   Its capped squared overload is exponentially large.
3. **Survives all three tests:** the tagged collision potential (21), with
   recursive exposure of retained, hidden, and blocker block complexes.
4. **Still open:** convert released ordered-pair mass to compatible planar
   cross-union faces and prove the global face-bank reuse bound (24) across
   different outer histories.

The practical implication is that a proof should not seek a new scalar
entropy loss per depth.  It should build a coherent tagged pair tree and
prove a quadratic Carleson packing theorem for its face banks.  Any state
compression is allowed only after the erased coordinate's pair mass has
been spent or its internal face complex has been deposited.

## 7. Exact verification

Run

```bash
python3 phase2/loop/erdos838/agent_cyclic_stem_hw/lattice_rectangle_counter/verify_dynamic_two_record.py
```

The verifier uses exact integers and rational arithmetic.  It checks:

* equations (2)--(10) on three scalable Proposition-26 parameter sets;
* the full child-face reuse distribution and exact mean-square identity
  (8);
* parabolic depths through 128, including (12)--(14);
* exact ramp--plateau banks (16) for `h=6,7`;
* the capped squared overload, raw child fibres, coordinate collision sums,
  and prefix collision Kraft sums; and
* the ordered-pair identities (21) and (23).

It writes `dynamic_two_record_certificate.json`.
