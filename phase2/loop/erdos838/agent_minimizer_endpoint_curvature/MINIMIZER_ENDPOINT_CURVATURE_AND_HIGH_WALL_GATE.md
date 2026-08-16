# Minimizer endpoint curvature and the high-wall gate

**Date:** 2026-08-15.  Face and endpoint counts are nonempty, and all
logarithms are base two.

## Verdict

There is a sharp exact lower bound on the directional endpoint parameter
which uses all the scalar information in singleton minimality.  For an
$a$-point ordinary-face minimizer $Q$, let

\[
 f(a)=V(Q),\qquad
 p(a)=\min_{Q,\theta}\,C_\theta(Q),                         \tag{1}
\]

where the minimum is over ordinary-face minimizers and generic projection
charts.  If $m_a(N)$ denotes the least possible sum of cardinalities of
$N$ distinct nonempty subsets of an $a$-set, then

\[
 \boxed{m_a(f(a))+m_a(p(a))\le a\{1+p(a)\}.}              \tag{2}
\]

Equivalently, $p(a)$ is at least the first integer
$c\ge a+\binom a2$ for which

\[
                  a(1+c)-m_a(c)\ge m_a(f(a)).             \tag{3}
\]

This is stronger than the earlier bound using only the mean face rank,
because it also retains the least possible cap-rank moment.  It is the
strongest consequence of the summed singleton inequality which uses only
$\bigl(a,f(a),p(a)\bigr)$, and it is sharp at $a=5$.

If $f(a)=2^{c(\log a)^2+o((\log a)^2)}$, let $r$ be the first rank for
which $\sum_{j\le r}\binom aj\ge f(a)$.  Then

\[
 r=(c+o(1))\log a,
 \qquad
 \boxed{p(a)\ge(1-o(1)){r f(a)\over a}.}                 \tag{4}
\]

Thus, conditionally on the inductive half-coefficient lower bound, the
ordinary-minimizer endpoint product is much larger than the fixed-gap
target.  The value of $p(a)$ is not the high-wall obstruction.

The obstruction is **Pareto curvature**.  Define the endpoint deficit cost

\[
 \Phi_a(c)=\min_{Q,\theta:C_\theta(Q)\le c}
                       \{V(Q)-f(a)\},\qquad \ell_a\le c\le p(a),
 \quad \ell_a=a+\binom a2.                                \tag{5}
\]

For a literal seam with child sizes $a,b$, the exact profile inequality
needed to close a target $F(a+b)$ is

\[
 \boxed{
 \min_{\substack{\ell_a\le c\le p(a)\\
                  \ell_b\le u\le p(b)}}
 \{\Phi_a(c)+\Phi_b(u)+cu\}
 \ \ge\ F(a+b)-f(a)-f(b).
 }                                                          \tag{6}
\]

This is the precise high-wall gate.  A convenient sufficient, but much
stronger, tangent condition is

\[
 \Phi_a(c)\ge p(b)\{p(a)-c\},\qquad
 \Phi_b(u)\ge p(a)\{p(b)-u\}.                              \tag{7}
\]

It is false already on stretchable finite minimizers.  Exact exhaustive
reflection-order scans give

\[
\begin{array}{c|c|c|c}
 a&f(a)&p(a)&
 \lambda(a):=\min_{C<p(a)}{V-f(a)\over p(a)-C}\\ \hline
 5&26&17&2\\
 8&113&55&1/2.
\end{array}                                                  \tag{8}
\]

For the unique stored nine-point minimizer, all 72 projection chambers have
minimum cap count $82$, while a stretchable $V=169$ configuration has a
chamber with $C=76$.  Hence its exposed ordinary-profile slope is at most
$1/6$.  At every nonempty literal seam the facing penalty is at least one,
so

\[
 (114+53t)-(113+55t)=1-2t<0,\qquad t\ge1,                 \tag{9}
\]

and, for the stored nine-point profile,

\[
 (169+76t)-(168+82t)=1-6t<0.                              \tag{10}
\]

Therefore an ordinary minimizer is not even a weighted child minimizer at
these sizes.  The exact comparison $C_A\le p(a)$ is normally strict in a
literal seam.  No argument based only on the value of $p(a)$, or on
deletion moments of the ordinary minimizer, can close the wall.  One needs
the integrated two-child curvature (6), or a physical mutation outside the
fixed seam chart.  Nor can the flat competitors be diverted to the
strong-tree recursion: exhaustive audits prove that the eight- and
nine-point witnesses are both non-strong-decomposable.  No half-coefficient
closure is claimed.

## 1. The exact rank-moment bound

For $0<N\le2^a-1$, choose $k$ so that

\[
 B_{k-1}<N\le B_k,
 \qquad B_k=\sum_{j=1}^k\binom aj.
\]

Then

\[
 m_a(N)=\sum_{j<k}j\binom aj+k\{N-B_{k-1}\}.             \tag{11}
\]

This is simply the minimum total rank of $N$ distinct nonempty subsets:
fill the Boolean lattice from the bottom.

Fix an ordinary-face minimizer $Q$ and a chart attaining $p(a)$.  Write

\[
 M_F=\sum_{F\in\mathcal F(Q)}|F|,
 \qquad M_C=\sum_{A\in\mathcal C_\theta(Q)}|A|.
\]

The exact singleton comparison, summed over the deleted label, is

\[
                         M_F+M_C\le a\{1+C(Q)\}.          \tag{12}
\]

Every face and every cap is a distinct nonempty subset, so

\[
                         M_F\ge m_a(f(a)),\qquad
                         M_C\ge m_a(p(a)).                \tag{13}
\]

Equations (12)--(13) prove (2).

For the asymptotic form, the first $f(a)$ Boolean sets have typical rank
$r+O(1)$.  Also every cap is an ordinary face, so
$p(a)\le f(a)=2^{o(a)}$; hence the first $p(a)$ sets have rank $o(a)$.
Consequently

\[
 m_a(f(a))=(r+O(1))f(a),\qquad
 a p(a)-m_a(p(a))=(a-o(a))p(a),                           \tag{14}
\]

which gives (4).  The verifier evaluates (3) at
$a=2^L,\ f=2^{0.49L^2+O(1)}$; the ratio of its exact lower bound to
$rf/a$ is between $0.9985$ and $1.0022$ for $8\le L\le14$.

### Why the endpoint value would be enough if curvature were available

For balanced near-ambient children $a,b\asymp n$, induction at coefficient
one half and (4) give

\[
 \log\{p(a)p(b)\}
 \ge \log f(a)+\log f(b)-\log(ab)+O(\log\log n)
 =(\log n)^2-O(\log n).                                  \tag{15}
\]

This is far above a target
$2^{(1/2-\varepsilon)(\log n)^2}$.  The high wall occurs because a weighted
child is permitted to move far to the left of $p(a)$ on the Pareto
frontier, not because (2) leaves $p(a)$ too small.

## 2. All-order deletion/Möbius inequalities

The singleton bound has an exact order-$d$ extension.  Put

\[
 N_d=\binom ad,
 \quad
 S_F(d)=\sum_{F\in\mathcal F(Q)}\binom{a-|F|}{d},
 \quad
 S_C(d)=\sum_{A\in\mathcal C(Q)}\binom{a-|A|}{d}.        \tag{16}
\]

For each $d$-set $X$, compare $Q$ with $Q-X$ followed by a
strongly-separated $d$-point convex chain whose facing endpoint count is

\[
                         \ell_d=d+\binom d2.               \tag{17}
\]

Global minimality gives pointwise

\[
 V(Q)-V(Q-X)\le(2^d-1)+\ell_d C(Q-X).                    \tag{18}
\]

Summing (18) proves the exact Möbius inequality

\[
 \boxed{N_df(a)-S_F(d)
       \le N_d(2^d-1)+\ell_d S_C(d).}                    \tag{19}
\]

Let

\[
 H_{a,d}(c)=\max_{|\mathcal A|=c}
       \sum_{A\in\mathcal A}\binom{a-|A|}{d}.            \tag{20}
\]

As in (11), $H_{a,d}$ is explicit: fill the lowest ranks first.  Since
$S_C(d)\le H_{a,d}(p(a))$, (19) gives

\[
 H_{a,d}(p(a))\ge
 {N_df(a)-S_F(d)-N_d(2^d-1)\over\ell_d}.                 \tag{21}
\]

At $d=1$, (21) is exactly (12).  On a low-rank face scale $r=o(a)$,
the left loss in (19) is approximately $N_ddr/a$, while
$\ell_d\asymp d^2$.  Thus order $d$ yields only about
$rf(a)/(ad)$; the singleton case is the strongest leading scalar bound.
Higher orders retain useful curvature information, but do not improve the
leading asymptotic endpoint value without rank correlation.

## 3. Restriction-defect curvature

There is a second exact multiscale inequality which directly couples
$p(a)$ to smaller endpoint minima.  Define the total restriction defect

\[
 D_{a,d}(Q)=S_F(d)-N_df(a-d)\ge0,
 \qquad e_{a,d}=\min\{D_{a,d}(Q),N_d\}.                   \tag{22}
\]

Every nonminimal restriction $Q-X$ contributes at least one to
$D_{a,d}$.  Therefore at least $N_d-e_{a,d}$ restrictions are ordinary
minimizers.  In the inherited chart each of those has cap count at least
$p(a-d)$; every other restriction has at least the singleton-pair baseline
$\ell_{a-d}$.  Hence

\[
 \boxed{
 S_C(d)\ge
 (N_d-e_{a,d})p(a-d)+e_{a,d}\ell_{a-d}.
 }                                                          \tag{23}
\]

Combining (20) and (23) gives the exact curvature recursion

\[
 H_{a,d}(p(a))\ge
 (N_d-e_{a,d})p(a-d)+e_{a,d}\ell_{a-d}.                  \tag{24}
\]

This is strong only when the ordinary-minimizer restriction defect is
small.  It is sharp at $a=5,d=1$, but already weak at $a=8,9$.  More
fundamentally, if the endpoint surplus in $H_{a,d}$ is allowed to occupy
rank three, even zero defect propagates it only by the cubic factor

\[
                       \left({a\over a-d}\right)^3.       \tag{25}
\]

Thus restriction curvature alone is polynomial.  It cannot prove the
integrated quasipolynomial deficit cost in (6).  The face moment (2) forces
the **value** of $p(a)$ to be large, but no deletion identity forces a
configuration with $C<p(a)$ to pay proportionally in $V-f(a)$.

## 4. Exact finite audit

The finite values and profiles used below are independently realized with
rational or integer coordinates.

| $a$ | ordinary profile $(v_1,v_2,\ldots)$ | $f(a)$ | cap-minimum profile | $p$ | scalar lower from (2) |
|---:|---|---:|---|---:|---:|
| 5 | $(5,10,10,1)$ | 26 | $(5,10,2)$ | 17 | 17 |
| 8 | $(8,28,56,21)$ | 113 | $(8,28,17,2)$ | 55 | 53 |
| 9 | $(9,36,84,36,3)$ | 168 | $(9,36,28,8,1)$ | 82 in the stored minimizer | 71; 72 using its actual face vector |

At five points, $M_F=59,M_C=31$, so (12) is equality:

\[
                         59+31=5(1+17).                  \tag{26}
\]

Also $D_{5,1}=1$, and (23) is equality:

\[
 S_C(1)=54=4p(4)+\ell_4=4\cdot11+10.                    \tag{27}
\]

At eight points, the selected cap moment is $123$, so
$S_C(1)=8\cdot55-123=317$.  The restriction defect is $12\ge8$, and
(23) asks only for $8\ell_7=224$.  At nine points the corresponding
figures are

\[
 M_C=202,\qquad S_C(1)=536,\qquad D_{9,1}=3,\qquad
 6p(8)+3\ell_8=438.                                      \tag{28}
\]

Thus all exact deletion-curvature inequalities have substantial slack at
the two sizes where the weighted frontier is already flat.

### Exact flat-frontier witnesses

The complete $B(5,2)$ scan has 62 commutation classes and begins

\[
                         (V,C)=(26,17),(28,16),(31,15).   \tag{29}
\]

The complete $B(8,2)$ scan has $1,232,944$ classes and begins

\[
                         (V,C)=(113,55),(114,53).         \tag{30}
\]

The second pair in (30) is a stretchable one-face/two-cap trade.  It proves
the exact slope $1/2$ in (8), and it makes the ordinary eight-point
minimizer lose every weighted child comparison with penalty $t>1/2$.

For nine points, the integer configuration

\[
\begin{array}{c|rrrrrrrrr}
i&0&1&2&3&4&5&6&7&8\\ \hline
x_i&11164&12508&15188&27928&17968&16188&28308&48288&60248\\
y_i&4101&65228&59208&45988&20888&13108&26528&28008&30768
\end{array}                                                 \tag{31}
\]

has $V=169$ and a projection chamber with $C=76$.  The unique stored
nine-point minimizer has $V=168$ and minimum stored-chamber count $82$.
Equation (10) is therefore a literal physical weighted replacement, not a
scalar fake.  The database scan through $V=180$ is recorded in
`endpoint_curvature_certificate.json`.

Both flat-frontier competitors, $(V,C)=(114,53)$ at eight points and
$(V,C)=(169,76)$ at nine points, are genuinely **not strongly
decomposable**.  The verifier exhausts every leaf permutation, every split,
and both mirror signs at every recursive node.  No strong tree exists.  On a
failed search it evaluates every ordered nonempty subset, giving exactly
$109{,}600$ cache misses at $n=8$ and $986{,}409$ at $n=9$.  Consequently
the flat frontier cannot be dismissed as a hidden strong-tree child or
routed through the recursive strong-tree half theorem.  Any successful
Pareto-curvature theorem must control genuinely nonstrong children.

There is a minor scope distinction at $a=9$.  The exhaustive realizable
order-type database proves uniqueness of the ordinary minimizer and the
72-chamber audit proves $82$ for its stored realization.  The universal
moment argument proves $p(9)\ge72$ for every realization.  The present
artifacts do not enumerate the entire $B(9,2)$, so the conservative
realization-independent statement is

\[
                              72\le p(9)\le82.             \tag{32}
\]

Nothing in the high-wall barrier needs equality in (32): the exact
eight-point slope $1/2<1$ already refutes the tangent route (7), and the
nine-point pair is an additional stretchable calibration.

## 5. Derivation of the exact closure inequality

Let a globally minimal literal seam $P=A\prec B$ have

\[
 c=C(A)\le p(a),\qquad u=U(B)\le p(b).                    \tag{33}
\]

By the definition of $\Phi$,

\[
 V(A)\ge f(a)+\Phi_a(c),\qquad
 V(B)\ge f(b)+\Phi_b(u).                                  \tag{34}
\]

The strong-glue identity then gives

\[
 V(P)=V(A)+V(B)+cu
 \ge f(a)+f(b)+\Phi_a(c)+\Phi_b(u)+cu.                    \tag{35}
\]

Taking the minimum over the rectangle in (33) proves that (6) is sufficient
and is the strongest possible conclusion based only on the two directional
Pareto frontiers.

If (7) held, then

\[
\begin{aligned}
 &\Phi_a(c)+\Phi_b(u)+cu-p(a)p(b)\\
 &\quad\ge
 p(b)\{p(a)-c\}+p(a)\{p(b)-u\}+cu-p(a)p(b)\\
 &\quad=\{p(a)-c\}\{p(b)-u\}\ge0,                       \tag{36}
\end{aligned}
\]

so the large ordinary endpoint product (15) would close the seam.  But
(30) makes the left tangent at $a=8$ equal to $1/2$, whereas every
opposite endpoint penalty is at least one.  This is the exact point where
the $p(a)$-only plan fails.

The finite witness also gives a scalar impossibility statement.  All
deletion, moment, and Möbius inequalities of an ordinary minimizer constrain
only that minimizer's rank profiles.  A neighboring configuration
$(f+1,p-2)$ is compatible with all of them; (30) realizes it by actual
points.  Therefore no manipulation of those inequalities alone can prove a
lower tangent greater than one.  A positive proof of (6) must compare the
competitor's own marked geometry, or use a mutation which changes the seam.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_minimizer_endpoint_curvature/verify_minimizer_endpoint_curvature.py
```

The verifier uses exact integer/rational arithmetic.  It compiles and runs
the independent packet-state scanner `exact_endpoint_bruhat.cpp`, exhausting
all 62 classes of $B(5,2)$ and all $1,232,944$ classes of
$B(8,2)$.  It then:

1. verifies the three minimizer face and cap rank profiles;
2. verifies the $V=114,C=53$ and $V=169,C=76$ stretchable witnesses;
3. proves both witnesses non-strong-decomposable by exhaustive recursive
   leaf-order and mirror-sign search;
4. checks (2), (19), and (23) at every available deletion order;
5. checks the exact finite slopes and the weighted decreases (9)--(10); and
6. checks the asymptotic inversion of (3) on four quadratic-log scales.

`scan_endpoint_envelope.cpp` is an optional scanner for the external
Aichholzer--Aurenhammer--Krasser coordinate and k-gon files.  Their hashes
and provenance are already recorded in
`agent_lex_minimizer_search/DATABASE_PROVENANCE.md`.

The verifier prints PASS.
