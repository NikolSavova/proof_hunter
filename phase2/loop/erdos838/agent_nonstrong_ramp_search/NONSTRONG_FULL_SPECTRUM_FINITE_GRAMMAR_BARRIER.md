# A nonstrong full-spectrum grammar: exact optimum \(2/3\), not \(1/2\)

**Date:** 2026-08-15. All logarithms are base two. Counts are for
nonempty caps, cups, and ordinary convex-position subsets.

## Verdict

An exact search over small rational order types found a genuinely
non-strong-decomposable eight-point macro whose projection spectrum supports
a nontrivial cap/cup reset. Two opposite projection charts reduce the
stationary endpoint payment from coefficient \(1\) to coefficient \(2/3\).
This is a real stretchable recursive construction, not merely a scalar LP.

It still does **not** realize the perfect-reset Bellman half ramp. In fact,
the complete 56-chamber spectrum of this macro has the exact optimum

\[
 \boxed{
  \inf_{\text{all finite chart/label grammars}}
  \liminf_{d\to\infty}
  {\log V(Q_d)\over(\log |Q_d|)^2}={2\over3}. }       \tag{1}
\]

The lower bound permits arbitrarily many states, an arbitrary projection
chart in every state, and an arbitrary child-state label at every one of the
eight macro positions. A two-state grammar attains it. Thus adding more
states from this full projection menu cannot approach \(1/2\).

If depth-\(d\) members of this grammar are substituted as the arbitrary
children of the 252-point perfect reset, the parent already contains every
local child face bank. Multiplication of size by 252 is constant, so its
leading coefficient remains at least \(2/3\). This exact small library
therefore cannot populate the missing Bellman ramp.

## 1. The integral nonstrong macro

Take the eight points \(p_i=(i,y_i)\), \(0\le i<8\), with

~~~text
y = (-4375003, -2375766, -3908671, -5825945,
      7932585,  7351545, -2562156, -3105652).
~~~

The smallest absolute determinant among the 56 triples is \(384369\), so
general position is exact. Direct hull enumeration gives

\[
             (v_1,v_2,v_3,v_4,v_5)=(8,28,56,43,10),
             \qquad V=145.                              \tag{2}
\]

This order type is not an opaque strong tree. The verifier exhausts all
\(8!=40320\) leaf orders. At every proposed internal cut it permits both
mixed-sign orientations

\[
 (A,A,B;A,B,B)=(-,+)\quad\hbox{or}\quad (+,-),           \tag{3}
\]

and recursively tests both children. No order decomposes. The second sign
choice includes reflections at arbitrary internal nodes, not merely one
fixed high-left/low-right convention.

This check matters: several other low-rank charts found by the search did
expand to strong trees after a non-obvious permutation of their leaves.
They were rejected.

## 2. The complete projection spectrum

For an oriented generic projection chart \(\xi\), write its increasing macro
order as \(z_1<\cdots<z_8\). Define endpoint rank rewards

\[
\begin{aligned}
 \alpha_\xi(i)&=\max\{|B|-1:B\text{ is a cap and }\min_\xi B=z_i\},\\
 \beta_\xi(i)&=\max\{|B|-1:B\text{ is a cup and }\max_\xi B=z_i\}.
                                                               \tag{4}
\end{aligned}
\]

All 28 pair directions are distinct. Crossing them around the oriented
direction circle gives exactly 56 chambers and 47 distinct numerical
\((C_\xi,U_\xi)\) profiles. The cap/cup rank histogram is

\[
\begin{array}{c|rrrrrrr}
(r_C,r_U)&(3,4)&(3,5)&(4,3)&(4,4)&(4,5)&(5,3)&(5,4)\\ \hline
\#\text{ chambers}&3&1&3&36&6&1&6.
\end{array}                                                   \tag{5}
\]

The decisive statistic is the **diagonal endpoint reward**

\[
                 h(\xi)=\max_i\{\alpha_\xi(i)+\beta_\xi(i)\}. \tag{6}
\]

The full census gives

\[
 h(\xi)=4\quad(48\text{ chambers}),\qquad
 h(\xi)=5\quad(8\text{ chambers}).                         \tag{7}
\]

Thus \(h(\xi)\ge4\) in every exported chart. This is stronger than a
separate cap-rank and cup-rank statement: the two rewards in (6) occur at
the **same macro position**, so they survive arbitrary child relabelling.

## 3. Exact finite-state recurrence

Let \(\mathcal T\) be any finite state set. State \(p\) chooses any one of
the 56 charts \(\xi_p\) and any label map
\(\ell_p:\{1,\ldots,8\}\to\mathcal T\). Starting from singletons, form
\(Q_p(d)\) by sufficiently thin vertical substitution. Every state has
size \(8^d\).

For \(n=8^{d-1}\), the exact heterogeneous recurrences are

\[
\begin{aligned}
C_p(d)&=\sum_{B\ {\rm cap\ in}\ \xi_p}
 C_{\ell_p(\min B)}(d-1)n^{|B|-1},\\
U_p(d)&=\sum_{B\ {\rm cup\ in}\ \xi_p}
 U_{\ell_p(\max B)}(d-1)n^{|B|-1},\\
V_p(d)&=\sum_{i=1}^8V_{\ell_p(i)}(d-1)
 +\sum_{\substack{B\ {\rm convex\ in}\ \xi_p\\|B|\ge2}}
 C_{\ell_p(\min B)}(d-1)
 U_{\ell_p(\max B)}(d-1)n^{|B|-2}.               \tag{8}
\end{aligned}
\]

The first two equations are fixed positive-polynomial max-plus systems.
Give the edge \(p\to\ell_p(i)\) weights
\(\alpha_{\xi_p}(i)\) and \(\beta_{\xi_p}(i)\). In a strongly connected
component let \(\rho_C,\rho_U\) be their maximum cycle means. Expanding (8)
gives, uniformly in the component,

\[
 \log C_p(d)={3\rho_C\over2}d^2+O(d),\qquad
 \log U_p(d)={3\rho_U\over2}d^2+O(d).              \tag{9}
\]

### The diagonal-cycle lemma

Take a reachable sink component \(K\). For every state \(p\in K\), choose a
position attaining (6). Its labelled child also lies in \(K\). The chosen
out-edges form a finite functional graph and contain a directed cycle
\(\gamma\). By (7),

\[
 {1\over|\gamma|}\sum_{e\in\gamma}\alpha(e)
 +{1\over|\gamma|}\sum_{e\in\gamma}\beta(e)\ge4.
\]

Each summand is at most the corresponding maximum cycle mean, hence

\[
                         \boxed{\rho_C+\rho_U\ge4.}           \tag{10}
\]

Every two macro positions form a convex support. Because \(K\) is a sink,
choose any two positions of a state in \(K\) in the last line of (8).
Equations (9)--(10) give

\[
       \log V_p(d)\ge {3(\rho_C+\rho_U)\over2}d^2+O(d)
                     \ge6d^2+O(d).                           \tag{11}
\]

Since \(\log|Q_p(d)|=3d\), this is the \(2/3\) lower bound in (1).
An arbitrary initial state reaches a sink after a bounded path, and the
corresponding descendant block transfers the bound upward.

This proof optimizes over **every finite grammar**, not only the two-state
search performed by the verifier.

## 4. A sharp two-state grammar

Use states \(A,B\) with macro orders and child labels

~~~text
A: (0,1,2,4,5,3,6,7),    labels (B,B,B,A,A,A,A,A),
B: (7,6,3,5,4,2,1,0),    labels (B,B,B,B,B,A,A,A).
~~~

Their scalar assembly profiles are

\[
                  (C_A,U_A)=(82,57),\qquad
                  (C_B,U_B)=(57,82).                        \tag{12}
\]

After parallel edges with the same source and target are maximized, the cap
and cup reward matrices (rows are sources, columns are targets \(A,B\)) are

\[
 M_C=\begin{pmatrix}2&3\\1&2\end{pmatrix},\qquad
 M_U=\begin{pmatrix}2&1\\3&2\end{pmatrix}.                 \tag{13}
\]

For each matrix the loops have mean \(2\), and the cross two-cycle has mean
\((3+1)/2=2\). Thus

\[
                         \rho_C=\rho_U=2.                    \tag{14}
\]

Equations (8)--(9) now give

\[
 \log C_A(d)=3d^2+O(d),\quad
 \log U_A(d)=3d^2+O(d),\quad
 \log V_A(d)=6d^2+O(d),                                    \tag{15}
\]

and the same with \(A,B\) exchanged. Therefore the limit is exactly
\(2/3\).

The verifier also evaluates the integer recurrence. The finite face ratios
at depths \(1,4,8,12\) are

\[
 0.7977676767,\quad0.6678130440,\quad
 0.6656408421,\quad0.6656301484,                            \tag{16}
\]

consistent with convergence to \(2/3\) with a signed lower-order term. It
also exhausts every pair of charts and all strongly connected binary
labellings after lossless edge-maxima compression; the exact two-state
optimum is \(\rho_C+\rho_U=4\), attained by (13). Reducible binary grammars
end in a one-state sink, and the separately exhausted one-state optimum is
\(5\).

## 5. Perfect-reset consequence and the missing state

Let \(R_d\) be a 252-leaf perfect-reset parent whose leaves receive
independently chosen depth-\(d\) children from any finite grammar using this
spectrum. Then

\[
 |R_d|=252\cdot8^d,\qquad
 V(R_d)\ge\max_iV(Q_i(d)).                                  \tag{17}
\]

The bounded factor 252 does not change the log-squared normalization, so

\[
             \liminf {\log V(R_d)\over(\log|R_d|)^2}\ge{2\over3}. \tag{18}
\]

Outer mixed terms can only increase the count. The Bellman ramp therefore
cannot be populated by this nonstrong full-spectrum menu.

The obstruction identifies what a larger construction state must change:

1. More copies of the same finite spectrum do not help; the diagonal-cycle
   proof already allows arbitrarily many finite states.
2. Within vertical substitution, a candidate approaching \(1/2\) needs a
   depth-growing macro library whose diagonal reward density approaches
   \(h(\xi)/\log|S|=1\), together with a compatible nonperiodic ramp. Here
   the ratio is \(4/3\).
3. A single-chart scalar spectrum is not a closed geometric state when both
   an assembly and a later reset direction must be retained. Such a search
   needs the decorated two-mark insertion gauge and the placement of
   cross-child pair directions.
4. Alternatively, a successful construction must change the standard
   vertical mixed-triple rule, so that the two-block term in (8) no longer
   couples the endpoint cycle means.

One tempting generalization is **not** currently valid: the published
Baek--Balko split-polygon threshold supplies a cap and cup sharing their
rightmost point. The rewards in (4) require a cap whose **minimum** and a cup
whose **maximum** are the same macro position. Thus that theorem does not
imply a universal analogue of (7). A general diagonal theorem would be a new
hinged cap-to-the-right/cup-from-the-left threshold.

This is an exact finite/menu obstruction, not a lower bound for arbitrary
planar order types.

## 6. Verification

Run

~~~bash
python3 phase2/loop/erdos838/agent_nonstrong_ramp_search/verify_nonstrong_full_spectrum_grammar.py
~~~

Expected output begins

~~~text
PASS: nonstrong integral n=8 macro; leaf_orders=40320;
ordered_subproblems=40339;
chambers=56; profiles=47; ... diagonal_floor=4;
exact finite-grammar optimum=4; sharp cycle means=(2,2); coefficient=2/3
~~~

All geometric predicates, the all-permutations strong-decomposition test,
the full chamber spectrum, compressed grammar search, and recursive counts
use exact integer or rational arithmetic.
