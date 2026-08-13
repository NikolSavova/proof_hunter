# Adversarial audit of the unequal-branching finite-state barrier

All logarithms are base two.  This note audits Theorem 3 of
`agent_upper_multitype/FINITE_STATE_BARRIER.md`.  It does not modify that
artifact.

## Verdict

I did not find a counterexample.  The theorem is correct, but the displayed
proof compresses six points that should be made explicit:

1. the Perron component must be chosen from the matrix restricted to states
   reachable from the initial state;
2. `Lambda >= 2` follows for that full reachable matrix, not from the row
   sums of the chosen diagonal block;
3. a maximal Perron component need not be a sink, but deleting its outgoing
   children leaves its diagonal block and therefore preserves `Lambda`;
4. irreducible periodic blocks still satisfy two-sided bounds at **every**
   depth, not just on a subsequence;
5. `Lambda > 1` forces some row of the diagonal block to have at least two
   internal occurrences; and
6. the state with two internal positions need not be the initial state, so a
   fixed transition path must be used to transfer its lower bound back.

The corrected proof below supplies these details.  The two most plausible
counterexamples---an imprimitive component such as
`[[0,2],[3,0]]`, and a chain of distinct components with the same spectral
radius---do not break the result.  The former has bounded periodic Perron
factors at all depths, while the latter creates only a polynomial factor in
the initial size.

## Corrected theorem

> **Theorem (finite-state unequal-branching barrier).**  Let `T` be finite.
> For every state `p`, fix an integer `r_p >= 2`, an `r_p`-point macro order
> type in increasing horizontal order, and labels
> `ell_p(1),...,ell_p(r_p)` in `T`.  Starting from one point in every state,
> recursively replace macro-position `i` by the depth-`d-1` construction in
> state `ell_p(i)`, using the vertical mixed-triple convention.  If `Q_p(d)`
> is the resulting point set and `W_p(d)` its number of nonempty convex
> subsets, then for every initial state `p`,
> \[
>  \liminf_{d\to\infty}
>  {\log W_p(d)\over(\log |Q_p(d)|)^2}\ge {1\over2}.
> \]

## 1. Dominant component and initial-state size

Fix the initial state `p_0`, discard states not reachable from it, and let
`M` be the resulting substitution matrix,
\[
 M_{pq}=|\{i:\ell_p(i)=q\}|.
\]
Every row sum is `r_p >= 2`, hence
\[
 M\mathbf 1\ge2\mathbf 1,
 \qquad M^d\mathbf1\ge2^d\mathbf1.
\]
It follows that the spectral radius `Lambda=rho(M)` is at least two.  In
Frobenius normal form, `Lambda` is the maximum spectral radius of a diagonal
strongly connected block.  Choose such a block `K`.  This is the precise
meaning of a maximal Perron component.  Notice that `K` need not be a sink.

The size vector is exactly
\[
 N(d)=M^d\mathbf1.
\]
Finite nonnegative-matrix growth gives
\[
 N_{p_0}(d)=\Lambda^d d^{O(1)},
 \qquad
 \log N_{p_0}(d)=d\log\Lambda+O(\log d).          \tag{1}
\]
For completeness, the lower bound follows by taking a fixed path from
`p_0` to `K` and then remaining in `K`; the upper bound follows from
Frobenius normal form, where a path through several diagonal blocks of
spectral radius `Lambda` contributes at most a fixed power of `d`.

## 2. Pruning and the periodicity issue

For `q in K`, let
\[
 I_q=\{i:\ell_q(i)\in K\}.
\]
Strong connectivity implies `I_q` is nonempty.  Define `R_q(0)` to be one
point and define `R_q(d)` by retaining in the macro for `q` exactly the
positions in `I_q`, placing `R_{\ell_q(i)}(d-1)` in them.  This is an induced
subset of `Q_q(d)`.  Its size vector is
\[
 m(d)=M_K^d\mathbf1,                              \tag{2}
\]
where `M_K` is the irreducible diagonal block indexed by `K`.  Outgoing
children have disappeared, but the diagonal block itself has not changed;
therefore `rho(M_K)=Lambda`.

Periodicity causes no exceptional depths in (2).  Let `v>0` be a right
Perron vector of `M_K`.  There are constants `a,b>0` with
`a v <= 1 <= b v` coordinatewise.  Positivity preserves these inequalities,
so for every `d>=0`,
\[
 a\Lambda^d v\le M_K^d\mathbf1\le b\Lambda^d v. \tag{3}
\]
Consequently, uniformly in `q in K` and at every depth,
\[
 \log |R_q(d)|=d\log\Lambda+O(1).                \tag{4}
\]
This direct Perron-vector comparison is stronger and cleaner than an appeal
to eventual positivity, which would be false for an imprimitive block.

## 3. Cap and cup rates after pruning

For `q in K` and `i in I_q`, define
\[
 \alpha(q,i)=\max\{|B|-1:B\subseteq I_q\text{ is a cap in the
 restricted macro and }\min B=i\},
\]
and define `beta(q,i)` analogously using cups and `max B=i`.  Give the
internal edge `q -> ell_q(i)` these two weights.  Let `rho_C,rho_U` be the
respective maximum cycle means on this strongly connected multigraph.

The maximum cap and cup sizes `a_q(d),b_q(d)` in `R_q(d)` satisfy exactly
\[
\begin{aligned}
 a_q(d)&=\max_{i\in I_q}
  \bigl(a_{\ell_q(i)}(d-1)+\alpha(q,i)\bigr),\\
 b_q(d)&=\max_{i\in I_q}
  \bigl(b_{\ell_q(i)}(d-1)+\beta(q,i)\bigr).
\end{aligned}                                    \tag{5}
\]
Deleting cycles from a path and repeating a maximum-mean cycle gives,
uniformly in `q`,
\[
 a_q(d)=\rho_Cd+O(1),\qquad b_q(d)=\rho_Ud+O(1). \tag{6}
\]

The enumerative recurrence has the same leading weights.  By (3), the size
of each additional occupied retained block at depth `d-1` is between fixed
positive multiples of `Lambda^(d-1)`.  Grouping cap terms by their first
occupied block therefore gives
\[
 \log C_q(d)=\max_{i\in I_q}
 \left(\log C_{\ell_q(i)}(d-1)
       +\alpha(q,i)(d-1)\log\Lambda\right)+O(1), \tag{7}
\]
with a uniform error; the analogous formula holds for cups.

On expanding (7) along a path with edge weights `x_1,...,x_d`, its quadratic
part is
\[
 \log\Lambda\sum_{t=1}^d(d-t)x_t
 =\log\Lambda\sum_{s=1}^{d-1}(x_1+\cdots+x_s).  \tag{8}
\]
Every length-`s` prefix has weight at most `rho_C s+O(1)`, and a bounded
entrance followed by repetitions of a maximum-mean cycle attains this up to
`O(1)`.  The per-step log-sum error in (7) contributes only `O(d)`.  Hence
\[
\begin{aligned}
 \log C_q(d)&={\rho_C\log\Lambda\over2}d^2+O(d),\\
 \log U_q(d)&={\rho_U\log\Lambda\over2}d^2+O(d),
\end{aligned}                                    \tag{9}
\]
uniformly in `q in K`.

Apply the cup--cap theorem to `R_q(d)`.  In the convention where `a_q(d)`
and `b_q(d)` are the largest cap and cup sizes,
\[
 |R_q(d)|\le
 \binom{a_q(d)+b_q(d)-2}{a_q(d)-1}
 \le2^{a_q(d)+b_q(d)}.
\]
Equations (4) and (6) imply
\[
 \rho_C+\rho_U\ge\log\Lambda.                   \tag{10}
\]

## 4. The row with two internal positions

Some row of `M_K` has internal row sum at least two.  Otherwise every row
sum of `M_K` would equal one.  Since `M_K` is an irreducible nonnegative
integer matrix, it would then be the permutation matrix of one directed
cycle and would have spectral radius one, contradicting
`Lambda >= 2`.

Fix such a state `q_*` and two distinct retained macro-positions `i<j`.
They may carry the same state label; only the occurrences must be distinct.
The two-point macro-index set is convex.  The vertical composition rule thus
turns every cap of `R_{ell(i)}(d-1)` together with every cup of
`R_{ell(j)}(d-1)` into a distinct convex subset of `Q_{q_*}(d)`.  Therefore,
using (9)--(10),
\[
\begin{split}
 \log W_{q_*}(d)
 &\ge \log C_{\ell(i)}(d-1)+\log U_{\ell(j)}(d-1)\\
 &\ge { (\log\Lambda)^2\over2}d^2+O(d).          \tag{11}
\end{split}
\]
It is important that (9) is uniform over all states in `K`; the cap-rich and
cup-rich maximum cycles need not pass through the two chosen child states.
Strong connectivity supplies only bounded entrances to those cycles, which
is absorbed by `O(d)` in (9).

## 5. Transfer to the initial state

Because `K` is reachable from `p_0` and strongly connected, there is a fixed
transition path of some length `h` from `p_0` to `q_*`.  Following the
corresponding child occurrence at each of those `h` levels identifies a
descendant block in `Q_{p_0}(d)` that is a copy of `Q_{q_*}(d-h)`.  Hence
\[
 W_{p_0}(d)\ge W_{q_*}(d-h).                     \tag{12}
\]
Combining (1), (11), and (12) gives
\[
 {\log W_{p_0}(d)\over(\log |Q_{p_0}(d)|)^2}
 \ge
 {\frac12(\log\Lambda)^2(d-h)^2+O(d)
  \over(d\log\Lambda+O(\log d))^2}
 ={1\over2}-o(1).
\]
This proves the theorem.

## 6. Exact scope of the repair

No additional sink assumption is needed.  No primitivity assumption is
needed.  It is also unnecessary for every row of `M_K` to contain two
internal children: one such row suffices, because its state is reached at a
fixed depth from the initial state.

The proof does require all state rules to be fixed independently of depth
and every original macro size to be at least two.  If one allowed unary
states, the conclusion would still hold whenever the dominant reachable
Perron value is greater than one, but the blanket assertion
`Lambda >= 2` would no longer follow from row sums.  The theorem as stated
has `r_p >= 2`, so this is not a counterexample.
