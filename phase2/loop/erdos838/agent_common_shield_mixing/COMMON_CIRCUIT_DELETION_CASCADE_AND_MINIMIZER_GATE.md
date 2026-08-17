# Common-circuit deletion: exact cascade and a true-minimizer gate

**Date:** 2026-08-17. The empty face is allowed as an output. All point
labels below refer to the stored exact nine-point minimizer.

## Verdict

The strongest naive completion of
`STRICT_SUBHALF_LINEAR_POCKET_CIRCUIT_CORE_GATE.md` is false, even in a
genuine global minimizer. A complete bad face rectangle may share a literal
bad four-circuit $C$, while **no subset of the common labels** releases
every record after deletion. New bad circuits can appear entirely in the
private continuations once $C$ is removed.

There is nevertheless an exact positive replacement. Deleting the current
common core either sends a positive fraction of the rectangle injectively
to ordinary faces, or one can fix a new residual bad four-circuit at a cost
of at most $\binom n4$ and continue. Thus the sole surviving common-core
route is a **residual circuit cascade**. For row rank at most $r$, column
rank at most $h$, and a common core using $c_Y,c_X$ labels on the two
sides, the cascade gives

\[
 |\mathcal A||\mathcal H|
 \le 2V(P)\left(2\binom n4\right)^q,
 \qquad q=\min\{r-c_Y,h-c_X\}.                         \tag{1}
\]

The factor in (1) is exponentially sharp at the level relevant here: for
$q=\Theta(\log n)$ it costs $2^{\Theta((\log n)^2)}$. Consequently the
linear common-circuit theorem has not closed the strict-subhalf route. What
it has done is isolate the missing statement exactly: a minimizer-specific
positive-mass release, or a sub-$n^4$ amortized charge for successive
residual circuits.

## 1. The cascade theorem

Let $P=Y\sqcup X$, let
$\mathcal A\subseteq\mathcal F(P[Y])$ and
$\mathcal H\subseteq\mathcal F(P[X])$, and suppose fixed sets
$C_Y\subseteq Y,C_X\subseteq X$ occur in every row and column. Put
$C=C_Y\cup C_X$ and $M=|\mathcal A||\mathcal H|$.

Call a record $(A,F)$ **released** if

\[
                       (A\cup F)\setminus C              \tag{2}
\]

is ordinary. The map (2) is injective on released records: intersecting the
output with $Y,X$ and then reattaching the fixed sets $C_Y,C_X$
recovers $A,F$. Hence the number of released records is at most $V(P)$.

If more than $V(P)$ records remain bad, choose canonically one bad
four-subset of each residual union. Some fixed four-set $D$ occurs on at
least

\[
                         {M-V(P)\over\binom n4}           \tag{3}
\]

records. Let $\mathcal A',\mathcal H'$ be the row and column projections
of those records. Every member of $\mathcal A'$ contains $D\cap Y$,
every member of $\mathcal H'$ contains $D\cap X$, and the complete
rectangle $\mathcal A'\times\mathcal H'$ contains $D$. Moreover,

\[
 |\mathcal A'||\mathcal H'|
 \ge {M-V(P)\over\binom n4}.                             \tag{4}
\]

Because $D$ lies in the residual union, it is disjoint from $C$. Replace
$C$ by $C\cup D$ and iterate. While the current rectangle has size at
least $2V(P)$, (4) loses at most the factor
$2\binom n4$. Every new crossing circuit consumes at least one new row
label and one new column label. Therefore there can be at most
$q=\min(r-c_Y,h-c_X)$ iterations, which proves (1).

This proof has no hidden history load: completing the selected edges to
their row and column projections only enlarges the record family, and the
new fixed circuit makes every completed pair bad by heredity.

## 2. Exact obstruction inside the nine-point minimizer

Use the rational coordinates

\[
\begin{array}{c|rrrrrrrrr}
i&0&1&2&3&4&5&6&7&8\\ \hline
x_i&62614&2922&10209&20660&33336&30137&15334&14934&10934\\
y_i& 7322&4014&14386&24299&29017&33324&45211&55621&61521.
\end{array}                                               \tag{5}
\]

This is the unique minimum trace in the exhaustive realizable order-type
database at $n=9$. It has

\[
 (v_1,v_2,v_3,v_4,v_5)=(9,36,84,36,3),\qquad V=168.      \tag{6}
\]

Take

\[
 X=\{0,1,2,3\},\quad Y=\{4,5,6,7,8\},\quad
 C=\{1,4,5,7\}.                                         \tag{7}
\]

The set $C$ is nonordinary. Let

\[
 \mathcal A=\bigl\{\{4,5,7\},\{4,5,7,8\}\bigr\}        \tag{8}
\]

and let $\mathcal H$ be the eight subsets of $X$ which contain label
$1$. All ten side sets are ordinary, while every one of the sixteen
unions in $\mathcal A\times\mathcal H$ contains $C$ and is bad.

An exhaustive check of the sixteen subsets $G\subseteq C$ gives

\[
 \forall G\subseteq C\quad
 \exists(A,F)\in\mathcal A\times\mathcal H:
                  (A\cup F)\setminus G\text{ is bad}.   \tag{9}
\]

In particular, deleting the entire fixed circuit does not release the last
record:

\[
 (\{4,5,7,8\}\cup\{0,1,2,3\})\setminus C
                         =\{0,2,3,8\},                  \tag{10}
\]

which is nonordinary. This is the smallest rectangle found by the exhaustive
audit with no common-label deletion.

The obstruction is sharp but not pessimistic about **mass**: deleting all
of $C$ releases the other fifteen records. Across every four/five
partition and every crossing bad four-set in (5), there are $10{,}800$
induced fixed-circuit rectangles. Exactly $1{,}569$ admit no deletion
$G\subseteq C$ which releases every record, but deleting all of $C$
releases at least $25/28$ of every rectangle. The last statement is finite
evidence, not an asymptotic theorem.

## 3. Strategic consequence

The finite minimizer rules out the literal target "fixed common circuits
imply a common deletion set." It does **not** rule out the quantitatively
weaker statement needed by the strict-subhalf proof: deleting a linear
common core might release an inverse-subexponential fraction in every
strict-subhalf minimizer. If that fraction is bounded below by
$2^{-o((\log n)^2)}$, the rectangle from the linear-pocket theorem closes
immediately.

If such release fails, Theorem 1 forces a long sequence of fresh residual
circuits. The optimal next theorem is therefore one of the following, and
not another static common-core lemma:

1. **positive-mass release:** a minimizer-specific lower bound for the
   released density after deleting a common circuit matching; or
2. **amortized cascade charge:** successive residual circuits cost less than
   four fresh physical labels each because their ordinary side faces or
   endpoint histories overlap in a recoverable way.

The anti-aligned Boolean-cloud examples show that neither conclusion follows
from four-locality alone. The strict parent upper bound or a decreasing
mutation must enter essentially.

## 4. Verification

Run

```text
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_common_circuit_deletion_cascade.py
```

The verifier uses exact integer orientation predicates. It checks general
position, the complete face vector (6), all $10{,}800$ fixed-circuit
rectangles, every common-label deletion, the exact witness (7)--(10), and
the minimum full-core release ratio $25/28$.
