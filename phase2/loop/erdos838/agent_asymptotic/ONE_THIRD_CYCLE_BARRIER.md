# The proposed `1/3` anti-alignment cycle and a depth-capacity barrier

All logarithms are base two. This note asks whether the max-plus recurrence
can realize the suggested cycle

\[
 (x,y,m)=\left({1\over3},{1\over6},{1\over3}\right)L^2
 \quad\longleftrightarrow\quad
 (x,y,m)=\left({1\over3},{1\over3},{1\over3}\right)L^2.       \tag{1}
\]

The anti-alignment half of the cycle is formally consistent: glue a
cup-heavy state on the left to its cap-heavy mirror on the right. The
forward term has exponent `1/3`, and the parent becomes balanced with all
three displayed rates `1/3`. The hard part is regenerating the imbalanced
state at a larger logarithmic scale. A natural size-doubling regeneration is
ruled out by an ordered-tree depth-capacity bound.

## 1. Tropical depth parameters

For a finite ordered full binary macro tree `S`, define

* `p(S)`: maximum number of left edges on a root-to-leaf path;
* `q(S)`: maximum number of right edges;
* `w(S)`: maximum one-turn degree, recursively

\[
 w(S)=\max\{w(A),w(B),p(A)+q(B)\}                 \tag{2}
\]

at `S=A prec B`, with all three parameters zero at a leaf. Thus `w+2` is
the largest leaf number of a left-comb/right-comb pattern in `S` (up to the
base convention).

When every macro leaf is replaced by the same `N`-leaf micro tree, these
parameters are the coefficients of `log N` in the tropical recurrences:

\[
 x'\ge x+p\log N,\qquad y'\ge y+q\log N,\qquad
 m'\ge x+y+w\log N.                               \tag{3}
\]

The last term is the obstruction: a macro tree which efficiently creates
both directional depths necessarily creates a long one-turn pattern too.

## 2. Exact finite capacity recurrence

Let `F(p,q,w)` be the maximum possible number of leaves of an ordered full
binary tree satisfying the three depth bounds. Splitting at the root gives
the exact dynamic program

\[
 F(p,q,w)=
 \max_{\substack{0\le i<p, 0\le j<q\\i+j\le w}}
 \{F(i,q,w)+F(p,j,w)\},                            \tag{4}
\]

with `F(0,q,w)=F(p,0,w)=1`. A simultaneous binomial induction applied to
(4) gives the capacity bound

\[
 F(p,q,w)\le 1+\max_{0\le h\le w}
 \sum_{j=\max(0,h+1-q)}^{\min(p,h+1)}
 \binom{h+1}{j}.                                  \tag{5}
\]

The additive one handles the degenerate leaf convention. To check the
induction, view the summation interval as binary words of length `h+1` with
at most `p` symbols of one kind and at most `q` of the other. In a root split
with `i+j<=h`, the two intervals are disjoint: one ends at `i`, while the
other starts at `h+1-j>=i+1`. Pascal's identity pads shorter words to a
common length. Equivalently, the right side is a super-solution of (4).

In particular, up to an irrelevant additive constant, (5) implies

\[
 F(p,q,w)\le
 \min\left\{
 \sum_{j=0}^{p}\binom{w+1}{j},
 \sum_{j=0}^{q}\binom{w+1}{j}
 \right\}.                                        \tag{5a}
\]

Asymptotically, if `q<=w/2`, (5) gives

\[
 \log F(p,q,w)\le
 (w+1)h_2\!\left({q\over w+1}\right)+O(\log w).   \tag{6}
\]

If `q>=w/2`, the cruder consequence is `log F<=w+1`.

## 3. Obstruction to depth-driven scale-doubling regeneration

Suppose a balanced state at log-size `L` is expanded by a macro tree also
having log-size `L`, so the new log-size is `2L`. To change

\[
 (x,y)=\left({1\over3},{1\over3}\right)L^2
\]

into the imbalanced target at scale `2L`, namely

\[
 (x',y')=\left({4\over3},{2\over3}\right)L^2,     \tag{7}
\]

If the quadratic increment is carried by the substitution-degree terms in
(3), rather than by a separate `Theta(L^2)` macro coefficient, the required
leading depths are

\[
 p=L,\qquad q={L\over3}.                           \tag{8}
\]

To keep `m'` at its target `4L^2/3`, (3) would require

\[
 {2\over3}L^2+wL\le {4\over3}L^2,
 \qquad\text{i.e.}\qquad w\le {2L\over3}.         \tag{9}
\]

But (5) then gives

\[
 \log |S|\le
 \log\sum_{j\le L/3}\binom{2L/3+1}{j}
 ={2L\over3}+o(L),                                \tag{10}
\]

contradicting the required `log|S|=L`.

In fact the entropy form (6) is stronger. A macro tree with `q=L/3` and
`2^L` leaves must have

\[
 w\ge(c_*+o(1))L,
 \qquad c_*h_2\!\left({1\over3c_*}\right)=1,      \tag{11}
\]

where

\[
 c_*=1.1524045938\ldots.                           \tag{12}
\]

Thus its forced cross term in (3) has rate at least
`(2/3+c_*)L^2`; after normalizing by the new squared log-size `4L^2`, this
is about `0.4543`, not `1/3`.

## 4. Broader construction consequences

A fixed stationary substitution template cannot attain `1/3` either. If
its log-size is `ell`, then the ordinary cap/cup depth bound gives
`p+q>=ell`; repeated substitution makes

\[
 {m\over L^2}\longrightarrow {p+q\over2\ell}\ge{1\over2}.    \tag{13}
\]

The same argument applies to nonstationary homogeneous substitutions whose
largest scale increment is `o(L)`. Therefore any genuine `1/3` construction
would need all of the following simultaneously:

1. infinitely many macroscopic scale jumps;
2. nonhomogeneous microstates across the macro leaves;
3. a regeneration mechanism not representable by one uniform macro depth
   triple `(p,q,w)`.

The depth-driven balanced/imbalanced size-squaring cycle is rigorously
blocked by (5). This does not exclude a uniform macro whose own endpoint
coefficient is already `Theta(L^2)` and supplies part of (7); that case must
charge the macro's intrinsic `M` simultaneously and is not captured by the
three depth increments (3). Nor does it prove a universal constant above
`1/3`: a more elaborate nonuniform multiscale tree can distribute different
microstates among macro leaves. The result does show that the most direct
degree-only regeneration cannot work, and quantifies the missing one-turn
mass rather than merely failing to find a template computationally.
