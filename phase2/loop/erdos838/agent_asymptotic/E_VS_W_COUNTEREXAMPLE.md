# The endpoint-caterpillar enumerator cannot be globally charged to `W`

All logarithms are base two.  The proposed comparison

\[
 \log E(T)\le \log W(T)+O(\log n\log\log n)       \tag{1}
\]

is false, even for an explicit alternating caterpillar tree.  In fact its
two sides can differ by `Theta(n)`.  This does not threaten the ordered-tree
alignment conjecture: in the example `W` is exponential in `n`, enormously
larger than the conjectured quasipolynomial lower bound.  It does rule out a
global `E/W` comparison as the bridge from the endpoint-caterpillar lemma.

## 1. Conventions and exact recurrence

Let `E(T)` be the number of nonempty leaf subsets whose reduced induced
rooted tree is an endpoint-rooted binary caterpillar, including singletons
and pairs.  At `T=A prec B`, with `a=|A|`, `b=|B|`, a crossing subset is an
endpoint-rooted caterpillar precisely when it consists of

* an `E`-set in `A` and at most one leaf in `B`, or
* an `E`-set in `B` and at most one leaf in `A`.

The choices with one leaf on each side are counted twice.  Therefore

\[
 \boxed{E(T)=(b+1)E(A)+(a+1)E(B)-ab.}             \tag{2}
\]

This verifies the proposed convention.  The comparison count satisfies

\[
 W(T)=W(A)+W(B)+C(A)U(B).                         \tag{3}
\]

## 2. An exact alternating-caterpillar family

Let `o` denote a single leaf and define

\[
 T_0=o,\qquad T_{j+1}=o\prec(T_j\prec o).         \tag{4}
\]

Thus `n_j=|T_j|=2j+1`.  Geometrically this is an endpoint-rooted
caterpillar whose attachment directions alternate at every step.

Write `(C_j,U_j,W_j,E_j)` for its four counts.  First glue `T_j` to the
right leaf and then glue the left leaf to the result.  Direct substitution
in the exact recurrences gives

\[
\begin{aligned}
 C_{j+1}&=2C_j+2j+4,\\
 U_{j+1}&=2U_j+4j+5,\\
 W_{j+1}&=W_j+C_j+U_j+2j+4,\\
 E_{j+1}&=4E_j+3,                                \tag{5}
\end{aligned}
\]

with all four initial values equal to one.

The last recurrence solves immediately:

\[
 E_j=2\cdot4^j-1=2^{n_j}-1.                      \tag{6}
\]

This also has a structural explanation: every nonempty restriction of an
endpoint-rooted caterpillar remains an endpoint-rooted caterpillar, so all
`2^{n_j}-1` nonempty subsets are counted.

The first two recurrences in (5) have the exact solutions

\[
 C_j=7\cdot2^j-2j-6,\qquad
 U_j=10\cdot2^j-4j-9.                             \tag{7}
\]

Substituting (7) into the recurrence for `W` and summing gives

\[
 W_j=17\cdot2^j-2j^2-9j-16.                      \tag{8}
\]

The formulas agree with the initial values and (5), so induction proves
them for every `j>=0`.

Consequently

\[
 \log E_j=n_j+o(1),\qquad
 \log W_j=j+\log24+o(1)={n_j\over2}+O(1),         \tag{9}
\]

and hence

\[
 \boxed{\log(E_j/W_j)={n_j\over2}-O(1).}          \tag{10}
\]

This contradicts (1) by an exponential margin.  For example, at `j=100`
(`n=201`), direct exact evaluation gives
`log(E/W)=96.9125...`, whereas `log n log log n` is only about `22.46`.

## 3. Why sibling-subtree compensation does not save the comparison

In this family the discarded sibling at every spine level is itself only a
leaf.  There are no large sibling subtrees in which hidden `W`-mass could
compensate the alternating orientations.  Nevertheless every subset is an
endpoint-rooted caterpillar, while only the much smaller left--right-comb
family is counted by `W`.

The polynomial form is equally decisive.  Since every subset is counted,

\[
 E_{T_j}(x)=(1+x)^{n_j}-1.                        \tag{11}
\]

Thus at any fixed sampling probability `p`, `E_{T_j}(p)` grows as
`(1+p)^{n_j}`.  No evaluation-at-one comparison, random-restriction
averaging, or coefficient pigeonhole can yield a subexponential loss to
`W(T_j)`.

## 4. What kind of comparison is still plausible

The counterexample has `W(T_j)=2^{Theta(n_j)}`, so it is already far above

\[
 2^{\frac12(\log n_j)^2-O(\log n_j\log\log n_j)}. \tag{12}
\]

It suggests that a useful dichotomy must truncate the endpoint count rather
than compare all of it:

* if `E(T)` is exponentially larger than the quasipolynomial scale, a
  separate density/comb argument may force `W(T)` above the target even
  though `E/W` is exponential;
* only in the near-extremal regime
  `log E(T)=O((\log n)^2)` could a comparison with subquadratic logarithmic
  loss reasonably hold.

A conceivable repaired statement is therefore conditional or capped, for
example

\[
 \min\{\log E(T),K(\log n)^2\}
 \le \log W(T)+O(\log n\log\log n),               \tag{13}
\]

with an appropriate fixed `K`, or a fixed-size comparison restricted to
`k=Theta(log n)` rather than the total values at `x=1`.  The present example
does not refute such a localized statement.  It does prove that the proposed
unconditional global comparison (1), even allowing sibling-subtree
compensation, is untenable.
