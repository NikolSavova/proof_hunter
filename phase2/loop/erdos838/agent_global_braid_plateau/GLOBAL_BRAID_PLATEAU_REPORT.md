# Global braid plateaus and the mean-size route

**Date:** 2026-08-13
**Verdict:** exact finite theorems and two rigorous obstructions; no
asymptotic proof of Erdős 838.

Throughout this report `Z(z)` counts nonempty convex subsets, `V=Z(1)`, and
`M=Z'(1)`.  The closure-lattice calculation separately includes the empty
set, as it must.

## 1. Exact plateau theorem through seven points

Contract every long-braid edge joining commutation classes with the same
reverse-product trace.  Call a contracted component a **trace plateau**, and
call it a weak sink if every edge leaving it has larger trace.

The deterministic exhaustive census gives:

| `n` | classes | braid edges | trace plateaus | weak-sink plateaus |
|---:|---:|---:|---:|---:|
| 6 | 908 | 2,144 | 908 | 70 |
| 7 | 24,698 | 80,360 | 14,826 | 280 |

At `n=6` the 70 sink states have traces `44,45,48`, with multiplicities
`12,52,6`.  At `n=7` the sink plateaus have traces `72,74,78`, with plateau
counts `104,156,20`; together they contain the 982 weak-sink classes found in
the earlier local census.

Every one of these sinks has degree-four profile.  Consequently its profile
is forced by its trace:

\[
 Z(z)=nz+\binom n2z^2+\binom n3z^3+
 \left(V-n-\binom n2-\binom n3\right)z^4.
\]

Thus on all weak sinks through `n=7`, the mean is an increasing function of
the trace.  The smallest sink means occur at the global trace minima:
`M/V=108/44=27/11` for `n=6` and `190/72=95/36` for `n=7`.  Their nonempty
mean deficits are respectively `-0.130417...` and `-0.168466...`.

This is an exact computational theorem, not evidence sampled from reduced
words.  `plateau_census.py` reconstructs the full graph from Coxeter heaps.

## 2. Sink-plateau graded rigidity fails at eight points

The encouraging degree-four phenomenon ends immediately.  Starting from the
saved `n=8`, `V=113` record and exhausting its entire equal-trace component
gives a seven-class plateau.  All 30 distinct boundary classes have trace
strictly larger than 113 (six at 114, two at 115, sixteen at 116, six at 117),
so this plateau is a rigorously certified weak trace sink.

Its graded profiles and first moments are

\[
\begin{array}{c|c}
 (8,28,56,21)&M=316,\\
 (8,28,56,20,1)&M=317,\\
 (8,28,56,19,2)&M=318.
\end{array}
\]

Therefore even after contracting every trace tie, a weak trace-sink plateau
does **not** have a fixed rank generating polynomial or fixed mean.  The
minimum nonempty mean on this plateau has deficit
`316/113-log2(8)=-0.203539823...`.

This kills the simplest global repair of local braid descent: “descend trace,
then the terminal plateau has a canonical graded profile.”  Selecting the
minimum first moment *within* a plateau remains possible, but needs an
additional argument.

## 3. Larger certified local sinks: evidence only

`greedy_sink_search.py` starts from seeded random reflection orders, contracts
the full equal-trace plateau at every step, and descends to a smaller-trace
boundary component.  Coverage is heuristic, but each reported terminal
plateau is locally certified by exhaustive checking of its boundary.

Ten starts at `n=8` ended at traces `113,114,116,117`; all deficits were at
least `-0.203540`.  Twelve starts at `n=9` ended at traces from 169 to 183.
The best terminal record has

\[
 Z(z)=9z+36z^2+84z^3+38z^4+2z^5,
 \qquad (V,M)=(169,495),
\]

and deficit `-0.240930919...`.  This particular reflection-order certificate
was not certified by the fixed-`x` realization routine, so it is not asserted
here as a point-set record.  The finite deficits continue moving downward;
they give no basis for replacing `O(1)` in the mean-size conjecture by zero.

## 4. The toggle-CDE shortcut is rigorously unavailable

The exact fixed-`x` rational realization of the `n=7`, `V=72` trace minimizer
has 73 closed sets when the empty set is included, down-degree profile

\[
 (1,7,21,35,9),\qquad \sum_K d_\downarrow(K)=190.
\]

For each ground element `p`, let `T_p(K)` be `+1` if `p` can be toggled into
the closed set `K`, `-1` if it can be toggled out, and zero otherwise.  A
finite poset is toggle-CDE exactly when its down-degree vector lies in the
linear span of the constant vector and the signed toggle vectors: this is the
linear-algebra dual of constancy on all toggle-symmetric measures.

Over the rationals, the design matrix `[1,T_1,...,T_7]` has rank 8, while
adjoining down-degree raises the rank to 9.  More concretely, the following
signed weights on subset bitmasks have total weight zero and zero pairing with
every toggle vector, but pairing one with down-degree:

```text
0:+1, 1:+2, 3:-2, 4:-4, 6:+2, 8:-2, 12:+2, 16:+1.
```

Perturbing the positive uniform law by a sufficiently small positive or
negative multiple of this vector gives two toggle-symmetric probability laws
with different expected down-degree.  Hence this closure lattice is not
toggle-CDE.  A CDE proof of the desired mean estimate would require a new
minimizer-specific distribution or extra statistic; general tCDE machinery
cannot simply be invoked.

## 5. What global minimality really supplies

The earlier rank-one switch theorem writes a braid pair as

\[
 Z_+(z)=Z_0(z)+z^2\Phi(z),\qquad
 Z_-(z)=Z_0(z)+z^2\Psi(z),
\]

with nonnegative boundary polynomials depending on the full prefix and
suffix.  Choose, among global trace minimizers, one with minimum first moment.
At every exposed packet it obeys the exact lexicographic condition

\[
 (\Phi(1),\Phi'(1))\le_{\rm lex}(\Psi(1),\Psi'(1))
\]

in its current orientation.  Equivalently it is locally minimal over the
ordered dual-number objective `Z(1+epsilon)`.  This is stronger than weak
trace minimality and handles the eight-point plateau, but it is only a local
necessary condition.  The boundary vectors vary with the whole context, and
only a small fraction of triples are exposed at any one class.

The precise surviving target is therefore:

> **Global lex-minimum conjecture.**  If a realizable reflection order
> minimizes `(V,M)` lexicographically among `n`-point orders (it is enough to
> assume the underlying point set minimizes `V`), then
> `M/V >= log2(n)-O(1)`.

By the deletion lemma already recorded in `MEAN_SIZE_ATTACK.md`, this solves
Erdős 838 with coefficient `1/2`.  The best braid-specific route I can now
state is to amortize the dual-number switch inequalities over paths that
expose nonflippable triples.  A valid certificate must retain the four
prefix/suffix boundary vectors; scalar packet orientations, scalar braid
potentials, fixed graded profiles, and generic tCDE are all ruled out.

## 6. Reproduction and claim boundary

```bash
python3 phase2/loop/erdos838/agent_global_braid_plateau/plateau_census.py --selftest
python3 phase2/loop/erdos838/agent_global_braid_plateau/plateau_census.py 7
python3 phase2/loop/erdos838/agent_global_braid_plateau/plateau_census.py 8 \
  --seed-word-json phase2/loop/erdos838/agent_global_braid_plateau/n8_seed_word.json
python3 phase2/loop/erdos838/agent_global_braid_plateau/toggle_cde_test.py \
  phase2/loop/erdos838/agent_reflection_gate/classes_n7.json --key certificate
```

The `n<=7` graph statements, the complete `n=8` seeded plateau, and the
non-tCDE witness are exact.  The list of larger sinks is heuristic coverage
with exact local certification.  No statement here proves the asymptotic
mean bound, RPR, or Erdős 838.
