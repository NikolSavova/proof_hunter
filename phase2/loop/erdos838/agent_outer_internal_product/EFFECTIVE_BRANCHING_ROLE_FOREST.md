# Effective branching in the role forest

**Date:** 2026-08-15.  All logarithms are base two.  This sharpens
`ROLE_FOREST_TERMINAL_ENTROPY_SPLIT.md` and corrects the interpretation of
its low-\(Q\) branch.

## Verdict

The terminal forest should be charged by **mass branching**, not support
branching.  At a node \(v\), after the bad records have been partitioned by
their canonical eligible role \(i\), let their actual-label class masses be
\(b_z\), put \(b=\sum_zb_z\), retain a largest class of mass \(b_*\), and set

\[
                         r(v,i)={b\over b_*}.             \tag{1}
\]

Then \(1\le r(v,i)\le a(v,i)\le d_i\).  For a terminal output \(O\), define

\[
 C_{\rm eff}(O)=\prod_{(v,i)\in[\varnothing,O]}r(v,i),
 \qquad Q_{\rm eff}(O)={P_0\over C_{\rm eff}(O)},
 \qquad P_0=\prod_i d_i.                                \tag{2}
\]

The exact weighted forest inequality is

\[
 \boxed{
       \sum_O\mu(O)C_{\rm eff}(O)\ge M,
       \qquad \mu(O)\le\delta .}                        \tag{3}
\]

Consequently, for every \(Q_0\ge1\),

\[
 \boxed{
 \sum_{O:Q_{\rm eff}(O)\ge Q_0}
       \mu(O)C_{\rm eff}(O)
       \le {\delta V(P)P_0\over Q_0}.}                 \tag{4}
\]

The exact factorization is

\[
 Q_{\rm eff}(O)=
   \prod_{i\text{ undeleted}}d_i
   \prod_{(v,i)\text{ deleted}}{d_i\over r(v,i)}.      \tag{5}
\]

Thus the surviving low-\(Q\) branch has nearly uniform **mass**, not merely
nearly full label support.  At all but a small fraction of its deleted
levels,

\[
 {b_*\over b}={1\over r(v,i)}
       \le {L^K\over d_i},                              \tag{6}
\]

for the appropriate constant \(K\).  This is a conditional min-entropy
bound on the next actual label.

The **unit-weight** prefix-star family in
`EXCESS_RANK_PREFIX_STAR_COHERENCE_GATE.md` is therefore **not** in the true
survivor.  With unit record weights its edge ratios telescope to

\[
                  C_{\rm eff}=|\mathcal E_{s,k,d}|,
 \qquad Q_{\rm eff}={d^s\over|\mathcal E_{s,k,d}|}
                   =d^{s-k-o(s-k)},                    \tag{7}
\]

so its whole excess tail is exposed as unused capacity and is paid by (4)
once it exceeds the required quasipolynomial threshold.

This is a genuine narrowing, not a half-coefficient closure.  Very small
record weights can make the same sparse prefix-star support have **exactly**
uniform mass branching through \(\Theta(L)\) roles.  The weighted calibration
in `EXCESS_RANK_PREFIX_STAR_COHERENCE_GATE.md`, equations (11)--(17), has
total row-normalized mass \(d^k\), effective ratio \(r=d\) at every core and
tail role, \(Q_{\rm eff}=1\), and still zero co-occurrence between distinct
nondefault tail siblings.

Thus effective branching removes the support-count artefact but does not by
itself prove sibling intersection.  A lower cutoff on individual history
weights, a mass-to-source-count comparison, or new planar/minimizer geometry
is still required.

## 1. Proof of the effective forest inequality

For a node \(v\), let

\[
 \Phi(v)=\sum_{O\text{ below }v}\mu(O)
        \prod_{e\in[v,O]}r(e).                         \tag{8}
\]

We prove \(\Phi(v)\ge m(v)\), the record mass at \(v\).  The good mass
\(g(v)\) terminates at cost one.  For each eligible role \(i\), its bad mass
is \(b_i\), and the selected heaviest actual-label child has mass
\(b_{i,*}\).  Induction below that child and (1) give contribution at least

\[
                    {b_i\over b_{i,*}}b_{i,*}=b_i.      \tag{9}
\]

Therefore

\[
                 \Phi(v)\ge g(v)+\sum_i b_i=m(v).      \tag{10}
\]

At the root this is (3).  The empty-role decoder from
`ROLE_MONOTONE_MIXED_FACE_FOREST.md` recovers the literal endpoint pair, so
each ordinary terminal output has routed mass at most the pair load
\(\delta\).

For \(Q_{\rm eff}(O)\ge Q_0\),

\[
 \mu(O)C_{\rm eff}(O)
   =\mu(O){P_0\over Q_{\rm eff}(O)}
   \le {\delta P_0\over Q_0}.                          \tag{11}
\]

There are at most \(V(P)\) terminal faces, proving (4).  Since every role is
deleted at most once, separating the deleted and undeleted factors in
\(P_0/C_{\rm eff}\) proves (5).

## 2. Quantitative low-\(Q\) consequence

Suppose \(Q_{\rm eff}(O)<2^{BL\log L}\).  Taking logarithms in (5) gives

\[
 \sum_{i\text{ undeleted}}\log d_i
 +\sum_{(v,i)\text{ deleted}}\log{d_i\over r(v,i)}
                         <BL\log L.                    \tag{12}
\]

If every \(d_i\ge n^\gamma\), at most \((B/\gamma)\log L\) roles remain.
If \(s=\Theta(L)\), Markov applied to the second sum says that outside an
\(\varepsilon s\)-set of deleted levels,

\[
             \log{d_i\over r(v,i)}=O_\varepsilon(\log L).
                                                               \tag{13}
\]

Equations (1) and (13) yield (6).  In information language, conditional on
the node and eligible role, the most likely actual label has probability at
most \(L^K/d_i\).  This is the exact min-entropy input available to a future
tree/geometry splice.

## 3. Prefix-star telescope

Give every word of \(\mathcal E_{s,k,d}\) unit mass and follow the zero path.
Let \(m_i\) be the number of surviving words immediately before role \(i\).
The zero class is heaviest at every level and has size \(m_{i+1}\).  Hence

\[
                       r(v_i,i)={m_i\over m_{i+1}}.     \tag{14}
\]

Since \(m_1=|\mathcal E_{s,k,d}|\) and the terminal class consists only of
\(0^s\),

\[
                \prod_{i=1}^s r(v_i,i)
                  ={m_1\over m_{s+1}}
                  =|\mathcal E_{s,k,d}|.               \tag{15}
\]

This proves (7).  The earlier support cost \(\prod_i a(v_i,i)=d^s\) counted
each thin tail sibling as if it carried the mass of the zero class; (15)
removes exactly that overcount.

## 4. Exact remaining interface

On the live low-\(Q_{\rm eff}\) branch with
\(s=(c+\varepsilon)L+o(L)\), the data now include:

1. all but \(O(\log L)\) completion roles are deleted;
2. all but \(o(L)\) deleted roles have conditional min-entropy
   \(\log d_i-O(\log L)\); and
3. the physical four-local theorem supplies a polynomial-density signed bad
   box on at most four role supports, but not necessarily on one common tree
   node or through one common released context.

What is still missing is a weighted sibling-intersection theorem which
places a positive fraction of the near-uniform branch mass inside a common
physical box, or a first-divergence output which remembers the released
context with load \(2^{O(L\log L)}\).  The planar Pascal common-guard
regression continues to rule out a theorem using only live normalization and
all-loop deletion.  The unit-weight prefix-star no longer rules out the
strengthened formulation, but its depth-weighted version does so abstractly.
It is not yet a stretchable live/minimizer counterexample.

## 5. Verification

Run

```text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_effective_branching_role_forest.py
```

The verifier recomputes the rational anti-aligned geometric forest using
exact fractional record weights, checks (3) and (5) on every terminal, and
checks the threshold inequality (4).  It then verifies the prefix-star
telescope (14)--(15) for several parameter triples and confirms that its
effective \(Q\) is exactly \(d^s/|\mathcal E|\).
