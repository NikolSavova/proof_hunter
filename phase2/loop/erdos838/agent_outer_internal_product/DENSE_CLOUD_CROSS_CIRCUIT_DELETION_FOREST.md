# Dense cloud cross-circuits: the exact deletion-mask forest

**Date:** 2026-08-15. All logarithms are base two. This continues
'NESTED_TRIANGLE_LIVE_NORMALIZATION_AUDIT.md' and the shield vertex-cloud
fixed-gap gate.

## Verdict

An almost-complete bad rectangle between two induced cloud face complexes
has an exact one-face decision-forest decoder. Fix one cloud \(X\). For
each bad residual pair, choose a canonical cross-circuit, choose one
canonical \(X\)-label in that circuit, and delete it. Eventually the
residual \(X\)-trace is empty, so the union is ordinary.

The chronology itself need not be encoded. If two terminal paths delete
the same **unordered physical mask** \(D\subset X\), the ordinary residual
union together with fixed \(D\) recovers the original two faces.
Consequently, for a rank-at-most-\(q\) row family \(\mathcal A\) and any
column family \(\mathcal B\),

\[
 V(P)\ge {|\mathcal A||\mathcal B|\over
                  \sum_{t=0}^q { |X|\choose t}}.                 \tag{1}
\]

There is a sharper depth form. If \(E_{\ge s}\) pairs terminate while at
least \(s\) row labels survive, then

\[
 V(P)\ge {E_{\ge s}\over
                  \sum_{t=0}^{q-s}{|X|\choose t}}.                \tag{2}
\]

This is a genuine load-one mixed-face bank. At the nested-cloud scale,
\(|X|=R=(1-o(1))N/3\), (2) closes the remaining
\(N^{\log_2 3-o(1)}\) gap whenever a sufficiently dense active rank layer
releases with at least two labels surviving. For a rank-\(q\) layer of
density

\[
       \delta={|\mathcal A|\over {R\choose q}},                   \tag{3}
\]

and an opposite cloud bank of size \(H\), the two-label branch gives, up
to subpower factors,

\[
                  V(P)\gtrsim \delta H\,{R^2\over q^2}.           \tag{4}
\]

Thus \(\delta\ge N^{-(2-\log_2 3)+\varepsilon}\) is enough for the fixed
gap. The exact remaining branch is narrow:

* useful rank layers are support-sparse past the threshold in (3), or
* almost all bad pairs survive until the row trace has rank zero or one.

The second alternative is real and planar. Two oppositely oriented
parabolic clouds have facing profiles consisting only of ranks at most
two. If both selected alphabets are complete rank-\(q\) layers,
\(q\ge3\), every cross union is bad and deleting any proper subset of the
row still leaves a bad union. The forest deletes the entire row. There
are exactly \(\binom Rq\) terminal masks, each supplying only
\(\binom Rq\) column outputs, so (1) is sharp.

That regression is not a live low-face construction: each parabolic cloud
has a Boolean \(2^R\) shield. It proves that dense face cross-circuits and
deletion alone cannot close the live gate. One must rule out the
singleton-terminal anti-alignment in a least counterexample, exploit
support redundancy, or charge its \(1+3\) seam to an ambient
shield/profile bank.

## 1. The deletion-mask theorem

Let \(X,Y\) be disjoint subsets of a planar general-position set \(P\).
Let

\[
 \mathcal A\subseteq\mathcal F(X),\qquad
 \mathcal B\subseteq\mathcal F(Y),\qquad
                  \max_{A\in\mathcal A}|A|\le q.                  \tag{5}
\]

No density or uniform-rank assumption is needed.

### Theorem 1 (cross-circuit deletion forest)

There is a partition

\[
              \mathcal A\times\mathcal B
                    =\mathop{\dot\bigcup}_{D\subseteq X}\mathcal E_D
                                                                    \tag{6}
\]

such that:

1. \(\mathcal E_D=\varnothing\) unless \(|D|\le q\);
2. every \((A,B)\in\mathcal E_D\) has \(D\subseteq A\) and
   \((A\setminus D)\cup B\in\mathcal F(P)\);
3. for fixed \(D\), the map
   \[
       (A,B)\longmapsto(A\setminus D)\cup B                         \tag{7}
   \]
   is injective; and
4. pairs with \(|A\setminus D|\ge s\) use only masks
   \(|D|\le q-s\).

Consequently,

\[
\begin{aligned}
 V(P)&\ge {|\mathcal A||\mathcal B|\over
                 \sum_{t=0}^q {|X|\choose t}},\\
 V(P)&\ge {E_{\ge s}\over
                 \sum_{t=0}^{q-s}{|X|\choose t}},
 \qquad
 E_{\ge s}:=\sum_D|\{(A,B)\in\mathcal E_D:
                              |A\setminus D|\ge s\}|.     \tag{8}
\end{aligned}
\]

#### Proof

Start from \((A,B)\) and put \(A_0=A\). If \(A_i\cup B\) is ordinary,
stop and put \(D=A\setminus A_i\).

Otherwise planar four-locality supplies a bad four-subset
\(Q_i\subseteq A_i\cup B\). Since \(A_i\) and \(B\) are separately
ordinary, \(Q_i\) meets both sides. Choose the first such \(Q_i\) in a
fixed physical order, choose the first
\(x_i\in Q_i\cap A_i\), and put

\[
                            A_{i+1}=A_i\setminus\{x_i\}.            \tag{9}
\]

At most \(|A|\le q\) deletions occur. When \(A_i=\varnothing\), the
residual union is \(B\), which is ordinary. This assigns every pair to one
mask \(D\).

For fixed \(D\), an output \(U\) in (7) recovers

\[
              A\setminus D=U\cap X,\qquad B=U\cap Y,
              \qquad A=(U\cap X)\cup D.                            \tag{10}
\]

Thus (7) has physical decoder load one. Different deletion orders with
the same mask may be merged because (10) does not use chronology. Counting
the possible masks proves (8). \(\square\)

Only the deleted physical label is fixed at each nonterminal node; the
other three circuit labels may vary. This is the face-rectangle analogue
of variable-witness fixed-label chronology.

### Corollary 2 (rank-\(q\), \(s\)-survival)

If \(\mathcal A\subseteq\binom Xq\) and an \(\eta\)-fraction of
\(\mathcal A\times\mathcal B\) terminates with \(s\) row labels surviving,
then

\[
 V(P)\ge {\eta|\mathcal A||\mathcal B|\over
                  \sum_{t=0}^{q-s}{R\choose t}},
             \qquad R=|X|.                                      \tag{11}
\]

For \(q=o(R)\) and fixed \(s\le q\),

\[
 { {R\choose q}\over\sum_{t=0}^{q-s}{R\choose t}}
 \ge {1\over q+1}
       \prod_{i=0}^{s-1}{R-q+i+1\over q-i}.                      \tag{12}
\]

Indeed the layers increase through \(q\), so
\(\sum_{t\le q-s}\binom Rt\le(q+1)\binom R{q-s}\), and the remaining
ratio is exact. For \(s=2\), (12) is \(R^{2-o(1)}/q^{2+o(1)}\).
If \(|\mathcal A|=\delta\binom Rq\), this proves (4), with the explicit
factor \(\eta/(q+1)\).

## 2. Fixed-gap splice

Let

\[
 K=F_C(N),\qquad H=F_C(R),\qquad
                 R={N\over3+o(1)}.                               \tag{13}
\]

The cloud audit gives

\[
                         {K\over H}=N^{\log_2 3-o(1)}.             \tag{14}
\]

Take a rank-\(q\) row subfamily \(\mathcal A\), an opposite cloud family
\(\mathcal B\) of size at least \(H/N^{o(1)}\), and suppose

\[
 |\mathcal A|\ge\delta{R\choose q},\qquad
 \delta\ge N^{-(2-\log_2 3)+\varepsilon}.                        \tag{15}
\]

If an \(N^{-o(1)}\)-fraction of its cross pairs terminates with at least
two row labels, then (11)--(12) imply

\[
 V(P)\ge H\,N^{\log_2 3+\varepsilon-o(1)}\ge K.                   \tag{16}
\]

This is conditional on layer density and terminal survival; neither
follows from \(V(X)\ge H\) alone. Failure gives an exact alternative:
after discarding subpower mass, the chronology leaves at most one row
label. Its last nonterminal residue is a literal singleton-versus-face
bad pair and hence a \(1+3\) cross-circuit. This is the correct interface
with fixed-root cage, sibling-ear, and shield/profile gates.

## 3. Sharp planar saturation

Take the two infinitesimal parabolic clouds from
'DENSE_HALL_TWO_CLOUD_PROFILE_BARRIER.md', oriented so that the facing
right profiles of \(X\) and facing left profiles of \(Y\) consist exactly
of subsets of ranks one and two. Their exact recurrence says

\[
 U\cup W\in\mathcal F(P)
 \quad\Longleftrightarrow\quad
 U\in\mathcal R(X),\ W\in\mathcal L(Y)                 \tag{17}
\]

when both traces are nonempty.

Fix \(q\ge3\) and take

\[
             \mathcal A={X\choose q},\qquad
             \mathcal B={Y\choose q}.                              \tag{18}
\]

Every row and column is ordinary, but for every nonempty
\(A'\subseteq A\),

\[
                              A'\cup B\notin\mathcal F(P),          \tag{19}
\]

because \(B\) is not a facing left profile. Every \(X\)-side deletion
process must therefore delete all of \(A\), independently of its circuit
and label choices.

The terminal mask is \(D=A\). There are exactly \(\binom Rq\) masks, and
for each fixed mask the residual bank is exactly the \(\binom Rq\)
columns. Theorem 1 is attained with equality:

\[
 {|\mathcal A||\mathcal B|\over |\{D\}|}
                  ={ \binom Rq^2\over\binom Rq}
                  =\binom Rq.                                      \tag{20}
\]

At the calibration rank

\[
 q={1\over2}\log R-\left(C-{1\over2}+o(1)\right)\log\log R,         \tag{21}
\]

Stirling gives

\[
                         \log {R\choose q}
                     =\Phi_C(\log R)+o((\log R)\log\log R).         \tag{22}
\]

Thus the selected alphabets can sit at the live cloud-bank scale. The
full parabolic clouds still have \(2^R\) faces and globally pay; (21)--(22)
are a scale calibration, not a live counterexample.

## 4. Global decoder and scope

For one fixed physical cloud pair, (7) has load one. The mask \(D\) is
fixed after pigeonholing and is not per-output metadata. The output
recovers both residual traces by intersection with the two physical color
classes; adjoining fixed \(D\) recovers the row.

If summed over multiple arrays or source contexts, the physical cloud pair
and mask must also be recoverable. A context load \(\Lambda_{\rm ctx}\)
changes (8) to

\[
 V(P)\ge {E_{\ge s}\over
     \Lambda_{\rm ctx}\sum_{t=0}^{q-s}{R\choose t}}.                \tag{23}
\]

The fixed-gap splice tolerates \(\Lambda_{\rm ctx}=N^{o(1)}\), but not an
untracked coefficient-half projection load. The nested-triangle gate has
one fixed array and three colored cloud pairs, so this extra load is
constant.

No coefficient-half closure is claimed. The exact survivor is

\[
\boxed{\begin{array}{c}
\text{a support-sparse active layer, or an almost-complete bad rectangle}\\
\text{whose fixed-label chronology reaches rank }0\text{ or }1.
\end{array}}                                                    \tag{24}
\]

The parabolic regression proves that planarity alone permits the second
line. A live proof must use the low-face/minimizer normalization which its
Boolean clouds violate.

## 5. Verification

Run

~~~text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_dense_cloud_cross_circuit_deletion_forest.py
~~~

The checker exhausts the deterministic circuit-deletion forest on exact
rational point sets, verifies the fixed-mask decoder, checks (8), (11),
and (12), and proves exact saturation on the anti-aligned parabolic
rank-three rectangle.
