# Marked one-turn load: the exact minimizer scale gate

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

The parent upper bound and deletion minimality do not, by themselves, make
a marked one-turn decoder subquadratic. A polynomially small fiber
\(V(P)/n^A\) still has the same quadratic logarithmic coefficient as
\(V(P)\). The uniform mean-rank bound and the per-source weight cap do not
change this fact.

There is one exact conditional exit. If all sources in a turn fiber live
on \(s\) physical labels and have rank at most \(r\), then

\[
 \boxed{\quad
 \Lambda_{\rm turn}
   \le\sum_{i\le r}{s\choose i}
   \le\left({es\over r}\right)^r.
 \quad}                                                            \tag{1}
\]

Thus, if \(s\le n^{\sigma+o(1)}\) and
\(r\le(\kappa+o(1))\log n\),

\[
                         \log\Lambda_{\rm turn}
                    \le(\kappa\sigma+o(1))(\log n)^2.               \tag{2}
\]

Combine this with the robust approximate-tree theorem. If the approximate
tree retains \(m=n^{\alpha+o(1)}\) physical labels and all other one-turn
losses total \((g+o(1))(\log n)^2\), then a
\((1/2-\delta)\)-counterexample is impossible whenever

\[
            \boxed{\quad
              g+\kappa\sigma
               <{1\over2}\alpha^2-\left({1\over2}-\delta\right).
            \quad}                                                 \tag{3}
\]

The live marked slice does not satisfy this inequality: it gives only
\(r=O(\log n)\) on a near-ambient support, with no sufficiently small
constant \(\kappa\).

The canonical Pascal family is the sharp planar nonminimal regression. Its
marked source fiber has rank \(O(\log N)\), polynomial entrance loss, and
terminal turn load

\[
               \Lambda(U)\ge {V(P)\over4N^{14}}
                   =2^{(\beta+o(1))(\log N)^2},
 \qquad \beta=1-{1\over4\ln2}>{1\over2}.                            \tag{4}
\]

Every nonempty source trace remains incompatible with \(U\), so no natural
source-retaining single-face retag exists. Pascal fails the least
sub-half parent upper bound, and therefore does not refute a genuinely
minimizer-specific geometric theorem. It does prove that such a theorem
must use more than deletion minimality, low mean rank, canonical weights,
polynomial state loss, and all-order deletion children.

The exact missing positive statement is now narrow: either compress every
heavy turn to parameters satisfying (3), or replace its loaded output by a
**single ordinary composable retag** with subquadratic load. A pair of
ordinary faces does not suffice.

## 1. What least-counterexample minimality actually says

Fix \(c=1/2-\delta>0\), put \(L=\log n\), and write

\[
                         F_c(n)=2^{c(\log n)^2}.                    \tag{5}
\]

If \(n\) is the least counterexample and \(P\) is minimizing, then every
one-point deletion gives

\[
                         F_c(n-1)\le V(P)<F_c(n).                   \tag{6}
\]

The window is extremely narrow:

\[
 \log {F_c(n)\over F_c(n-1)}
   =c\bigl(L^2-\log^2(n-1)\bigr)
   =O\!\left({L\over n}\right),                                   \tag{7}
\]

and hence \(F_c(n)/F_c(n-1)=1+O(L/n)\).

But (6) controls only the total number of ordinary outputs. It gives no
upper bound smaller than \(V(P)\) on the multiplicity of one marked
projection. For every fixed \(A>0\), the scalar load

\[
                         \Lambda_A={F_c(n-1)\over n^A}              \tag{8}
\]

is compatible with (6) and satisfies

\[
               \log\Lambda_A=cL^2-AL+o(L).                         \tag{9}
\]

Thus polynomial normalization changes only the linear term. In particular,
for every \(\zeta<c\), (9) eventually exceeds
\(\zeta L^2\).

This remains compatible with the two live weighted constraints. Give the
fiber distinct source atoms, each of weight at most one, all at rank
\(r=(c+\varepsilon)L\). There are enough possible sources because

\[
 \log {n\choose r}
    \ge r\log(n/r)
    =(c+\varepsilon)L^2-O(L\log L)
    >\log\Lambda_A.                                                \tag{10}
\]

If the fiber is only an \(n^{-A}\) fraction of the face law, its
contribution to the uniform mean rank is
\(O(Ln^{-A})\). Hence a low mean \(O(L)\), or even \(O(1)\) from this
fiber, does not rule it out.

Equations (8)--(10) are a scalar capacity barrier, not a claimed planar
configuration. The point is logical: no inequality using only (6), source
weight at most one, rank \(O(L)\), and mean rank \(O(L)\) can prove
\(\log\Lambda=o(L^2)\).

The constant in the mean-rank bound can be audited exactly. The deletion
identity gives

\[
 V(P)(n-\mu)=\sum_{p\in P}V(P-p)\ge nF_c(n-1).
\]

Using \(V(P)<F_c(n)\) and (7),

\[
 \mu<n\left(1-{F_c(n-1)\over F_c(n)}\right)
                         =(2c+o(1))L.                            \tag{10a}
\]

The rank-safe marked-source theorem retains positive asymptotic mass after
the cutoff \(|D|\le K\mu\) exactly when \(K>2\). Hence the best rank
constant supplied by uniform mean alone is

\[
                       \kappa\downarrow4c
                       \qquad(K\downarrow2).                     \tag{10b}
\]

On a near-ambient source support and a near-ambient approximate tree,
(3) would require \(\kappa<\delta\). In the live interval
\(c=1/2-\delta\ge1/4\), one has

\[
                          4c\ge1>\delta.                         \tag{10c}
\]

Thus even the sharp constant from deletion minimality misses the marked-turn
budget by a fixed factor. A better rank constant cannot be obtained merely
by optimizing the Markov cutoff.

## 2. The support--rank cap

Let \(\mathcal D\) be the actual source faces contributing to one turn
fiber. Suppose every source is contained in one support \(S\), \(|S|=s\),
and has rank at most \(r\le s/2\). If its marked weight is at most one,

\[
 \Lambda_{\rm turn}
       =\sum_{D\in\mathcal D}w_D
       \le|\mathcal D|
       \le\sum_{i=0}^r{s\choose i}.                                \tag{11}
\]

The standard binomial estimate gives the second inequality in (1).
Substitute

\[
                \log s\le(\sigma+o(1))L,\qquad
                r\le(\kappa+o(1))L                                \tag{12}
\]

to obtain (2); the \(r\log(er)\) correction is only \(O(L\log L)\).

Now apply
ROBUST_WEIGHTED_APPROXIMATE_STRONG_TREE_GATE.md. Its one-turn loss is at
most

\[
             G_M\le(g+\kappa\sigma+o(1))L^2.                       \tag{13}
\]

The retained tree contributes

\[
                    {1\over2}\alpha^2L^2-o(L^2).                   \tag{14}
\]

Comparison with the forbidden parent exponent
\((1/2-\delta)L^2\) proves (3).

There is a useful alternative formulation. If the induced source support
has a separately proved upper face count

\[
                         V(P[S])\le2^{(\theta+o(1))L^2},            \tag{15}
\]

then \(\log\Lambda_{\rm turn}\le(\theta+o(1))L^2\), and \(\theta\)
may replace \(\kappa\sigma\) in (3). Least-counterexample induction gives
a **lower** bound on \(V(P[S])\), not (15), so (15) is genuine extra input.

## 3. What a valid heavy-turn conversion must produce

Consider the raw forward records at one approximate seam. The ordinary
output map may have maximum load \(\Lambda_{\rm turn}\). A valid
source/profile conversion is a map from those same records to ordinary
faces \(\Psi(R)\) satisfying:

1. \(\Psi(R)\) retains or decodes the selected cap endpoint, cup endpoint,
   and branch state needed by the later approximate-tree recurrence;
2. the maximum weighted load of one \(\Psi\)-output is \(K_{\rm turn}\);
3. the output is one ordinary face of \(P\).

Then the forward factor
\(\lambda^M_{v,\times}=\Lambda_{\rm turn}\) in the robust theorem is
replaced by \(K_{\rm turn}\). If the resulting one-turn Carleson sum
satisfies (3), the fixed gap closes.

The third condition is essential. Mapping a record to the ordered pair
\((D,U)\) of its ordinary source and released face has load one, but it
lives in \(\mathcal F(P)^2\). It yields only a two-output square bound and
does not replace the one-face recurrence for \(M\).

Likewise, merely choosing a cap or cup subtrace of \(D\) does not work
unless that trace coexists with the released endpoint data in one ordinary
face. This is exactly the compatibility statement which the Pascal
regression denies.

## 4. Canonical Pascal saturates every arithmetic input

Use the central cell

\[
                         P=T(2h,h)=Y\prec Z,\qquad
                         N=|P|={2h\choose h}.                       \tag{16}
\]

The exact canonical marking and unordered coloring in
CANONICAL_SOURCE_ROLE_DELETION_PASCAL_DENSITY_BARRIER.md produce:

* a fixed root and rank-\(O(\log N)\) noncap source fiber
  \(\mathcal E\subseteq\mathcal F(Y)\);
* total marked weight
  \[
                  W_{\mathcal E}\ge {V(P)\over4N^{14}};            \tag{17}
  \]
* a noncup released family
  \(\mathcal H\subseteq\mathcal F(Z)\); and
* for every \(D\in\mathcal E\), \(U\in\mathcal H\), and \(G\subseteq D\),
  \[
      (D\setminus G)\cup U\text{ is ordinary}
                    \quad\Longleftrightarrow\quad G=D.             \tag{18}
  \]

Thus every fixed \(U\in\mathcal H\) has literal terminal load
\(\Lambda(U)=W_{\mathcal E}\), proving (4). Equation (18) says that every
natural source-retaining union is nonordinary. The pair \((D,U)\) still
decodes the record, demonstrating precisely why pair decoding is
insufficient.

The same example has all of the following:

* actual canonical weights, not artificial row normalization;
* uniform mean and maximum rank \(O(\log N)\);
* polynomial parent/child, root, rank, and coloring losses;
* every role-deletion child retaining a large induced \(Z\)-bank;
* the reflection-minimal orientation among all four child reflections; and
* a genuine lossless **unmarked** ambient strong tree.

Yet the marked turn load has coefficient \(\beta\) in (4). The only live
hypothesis it violates is the least sub-half parent upper bound. Therefore
that upper bound must interact with a new geometric mutation, support
compression, or composable retag; it cannot merely be appended to the
arithmetic inputs above.

## 5. Exact remaining gate

For a least fixed-gap counterexample, one of the following is sufficient:

1. **support--rank compression:** prove (12) with constants satisfying (3);
2. **source-complex compression:** prove (15) with
   \(g+\theta<\alpha^2/2-(1/2-\delta)\);
3. **single-face retagging:** construct \(\Psi\) with a one-turn Carleson
   load satisfying (3); or
4. **unmarking promotion:** show that a heavy marked turn lies inside a
   large same-chart unmarked strong tree, so the mark may be discarded and
   the lossless ambient theorem applies.

Current minimizer theory gives only a near-ambient pocket/support and, by
(10a)--(10b), the inadequate constant \(\kappa\ge4c-o(1)\) from the
uniform-mean cutoff. Canonical Pascal shows that these inputs are not
enough. The missing number is the
quadratic coefficient of the actual **marked turn load after the best
composable one-face retag**.

## 6. Verification

The verifier
verify_marked_turn_minimality_load_scale_gate.py checks the minimality-window
expansion, the polynomial-fiber coefficient barrier, the exact
support--rank binomial bound, and the constants in (3) on a range of scales.
It also imports the independent canonical-Pascal verifier and rechecks its
exact finite geometry: canonical source weights, rank-safe fiber, complete
all-delete incompatibility, and equality of the retained source weight with
the terminal output load.
