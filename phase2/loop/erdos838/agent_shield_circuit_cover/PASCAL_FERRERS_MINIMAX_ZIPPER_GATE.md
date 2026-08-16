# Pascal cross walls: exact minimax and the rooted weighted zipper

**Date:** 2026-08-15. All chain and face counts are nonempty, and all
logarithms are base two unless a base is displayed. This continues
`PASCAL_STRONG_GLUE_PROJECTION_SPECTRUM_GATE.md` and
`PASCAL_WEIGHTED_INVERSION_LEX_SEAM_GATE.md`.

## Verdict

The correct cross-wall object is a bottleneck path in the Young lattice,
not the minimum over isolated shuffles. For

\[
 A=T(4,3),\qquad B=T(8,2),
\]

there are \({32\choose4}=35960\) reverse-internal shuffles. The cheapest
single shuffle has

\[
 (C,U)=(83100,2835),\qquad
 \log_{32}\frac{CU}{V}=1.5419638968\ldots<\log_2 3.       \tag{1}
\]

Nevertheless, every monotone adjacent-swap path from $B^{\rm rev}A^{\rm
rev}$ to $A^{\rm rev}B^{\rm rev}$ has a chamber with

\[
 CU\ge491676585,
 \qquad
 \log_{32}\frac{CU}{V}=1.7542520037\ldots .             \tag{2}
\]

The bound is sharp: an exact $112$-swap path never exceeds the two endpoint
profiles $(297445,1653)$ and $(1653,297445)$. Thus the finite Pascal pair
really does have a positive minimax reset, even though pointwise shuffle
uniformity is false.

There is also an exact asymptotic obstruction to the most obvious proof of
such a reset. A high-density Pascal cap family has a strongly rooted
minimum-endpoint distribution. Its sharp Ferrers/Young rectangle
potential is

\[
 \log Z_d=\frac{d}{4\ln2}+o(d),                       \tag{3}
\]

where $Z_d$ is the maximum of $q$ times the lower-convex suffix mass of
the minimum endpoint. This is a genuine fixed power, but it is too small
by itself. In the live pair $s=(11/20)t$, the resulting one-rectangle bank has
normalized exponent only

\[
 1+\frac{11}{80\ln2\,H_2(1/4)}
      =1.2445161063\ldots,                             \tag{3a}
\]

while the two corner chambers give $1+11/20=1.55$. Both are below
$\log_2 3$. Thus a weighted Menger argument applied to one middle
rectangle cannot close. It loses exactly at the common-root Pascal ramp.

The second incomparable middle rectangle supplies the missing factor. Its
two complementary transforms have a direction-uniform floor
$|A_R|^{1-o(1)}$. Therefore the peak above cannot be synchronized with a
collapse of the other rectangle. The resulting pathwise exponent is

\[
 1+\frac{11}{20}
   +\frac{11}{80\ln2\,H_2(1/4)}
       =1.7945161063\ldots>\log_2 3.                  \tag{3b}
\]

This proves a positive minimax theorem for the reverse-internal Pascal
cross-wall interval, independent of the realizable wall schedule. At the
top Pascal split, the four cross rectangles are partially ordered as

\[
 (B_L,A_R)\quad<\quad
 \{(B_R,A_R),(B_L,A_L)\}\quad<\quad(B_R,A_L).          \tag{4}
\]

The proof couples the two incomparable middle rectangles in (4); it does
not require completing either block or fixing the varying opposite
endpoint. A single fixed-edge theorem would still lose that entire
macroscopic endpoint role.

This closes the adversarial cross-wall scheduling escape for this exact
opposite-density Pascal regression. It is not a coefficient-half closure
for the full planar problem: a reduction still has to produce these two
dominant Pascal endpoint modules in one actual reverse-internal interval,
and chambers outside that interval remain governed by the first-jump and
separated-profile branches.

## 1. The exact Young-lattice bottleneck

Keep the internal orders of $A$ and $B$ reversed. A shuffle is determined
by the $a$ occupied positions of the $A$ labels in a word of length
$a+b$. Moving from $B^{\rm rev}A^{\rm rev}$ to
$A^{\rm rev}B^{\rm rev}$ swaps one adjacent $BA$ pair at a time. The
shuffle states are therefore the vertices of the distributive lattice of
order ideals of $[a]\times[b]$.

For a natural $B$-cup $S$, let

\[
 L_A(S)=\#\{x\in A:x\text{ lies before }\max S\},
 \qquad
 R_A(S)=\#\{x\in A:x\text{ lies after }\min S\}.       \tag{5}
\]

The exact diagonal formula from the preceding report can be compressed to

\[
 \begin{aligned}
 C(W)&=U(A)+\sum_{S\in\mathcal U(B)}(1+L_A(S))(1+R_A(S)),\\
 U(W)&=C(B)+\sum_{T\in\mathcal C(A)}(1+L_B(T))(1+R_B(T)).
                                                               \tag{6}
 \end{aligned}
\]

Thus every Young-lattice vertex has an exact integer cost
$\omega(W)=C(W)U(W)$.

> **Theorem 1 (exact finite minimax).** For $A=T(4,3)$ and $B=T(8,2)$,
> 
> \[
> \min_{\Pi}\max_{W\in\Pi}\omega(W)=491676585,          \tag{7}
> \]
> 
> where $\Pi$ ranges over all monotone paths between the two corners.

**Proof.** Dynamic programming on the Young lattice gives

\[
 D(W)=\max\!\left(\omega(W),
              \min_{W'\lessdot W}D(W')\right),        \tag{8}
\]

starting at the first corner. Formula (6) evaluates every vertex with
integer arithmetic. There are only $35960$ states. The verifier checks
every cover relation, obtains (7), and reconstructs a path of $ab=112$
swaps attaining it. Since each corner already has cost

\[
             297445\cdot1653=491676585,                \tag{9}
\]

the certificate is both a lower and an upper bound. $\square$

This computation also independently corrects the tempting all-shuffle
claim: the minimum vertex cost is $235588500$, attained at (1), well below
the bottleneck.

## 2. The exact weighted Ferrers potential

Let $z_1,\ldots,z_n$ be rows, let $x_1,\ldots,x_m$ be columns, and give
the rows probability weights $w_i\ge0$, $\sum_iw_i=1$. The cross events
of any reverse-internal wall sweep form a Young ideal. For a state $I$,
let $q_j$ be the number of rows not yet crossed by column $x_j$. Thus

\[
 \overline q=\frac1m\sum_{j=1}^m q_j                 \tag{10}
\]

is the mean un-crossed row count. Put

\[
 W(q)=\sum_{i=q}^{n-1}w_i                             \tag{11}
\]

for integer $q$, linearly interpolate, and let $\underline W$ be the
lower-convex envelope of these $n+1$ points.

> **Lemma 2 (Ferrers convexification).** At every state,
> 
> \[
> \frac1m\sum_{j=1}^m W(q_j)
>             \ge \underline W(\overline q).          \tag{12}
> \]
> 
> Consequently every full wall sweep has a state whose two complementary
> rectangle factors have product at least
> 
> \[
> m Z(w)-O(m+n),\qquad
> Z(w)=\max_{0\le q\le n}q\,\underline W(q).          \tag{13}
> \]

**Proof.** In one column the crossed rows form a suffix, so its weighted
crossed mass is exactly $W(q_j)$. Since $\underline W\le W$ and
$\underline W$ is convex, Jensen gives (12). During a full sweep,
$\overline q$ decreases from $n$ to $0$ in steps $1/m$. At a state nearest
a maximizer $q_*$ of (13), one complementary factor is at least
$1+\overline q$, while the other is at least
$1+m\underline W(\overline q)$. Multiplication and the one-step rounding
loss prove (13). $\square$

This statement already includes arbitrary interleaving of rows and
columns; it is not a row-major assumption. It is also sharp up to the
rounding term for the abstract weighted rectangle: a boundary path which
follows supporting chords of $\underline W$ realizes the corresponding
convex mixtures.

The cruder maximum-atom estimate is recovered by putting
$K=n\max_iw_i$: at weighted mass $1/2$, at least $n/(2K)$ rows remain, so
$Z(w)\ge n/(4K)-1$. For Pascal this loses the true exponent because the
ordered tail, not the largest atom alone, controls the bottleneck.

## 3. Pascal endpoint tails

Let $C(d,k)$ be the natural cap count of $T(d,k)$ in lexicographic order,
and let $m_{d,k}(z)$ count caps whose minimum endpoint is label $z$. At the
top split $T(d,k)=L\prec R$,

\[
 \begin{aligned}
 C(d,k)&=C(d-1,k)+(1+|R|)C(d-1,k-1),\\
 m_{d,k}|_L&=(1+|R|)m_{d-1,k-1},\\
 m_{d,k}|_R&=m_{d-1,k}.                                \tag{13a}
 \end{aligned}
\]

For a cut after the first $q$ labels, write

\[
 S_{d,k}(q)=\sum_{z\ge q}m_{d,k}(z).                  \tag{14}
\]

This is also the number of caps wholly contained in the suffix beginning
at $q$.

> **Theorem 3 (Pascal convex-tail exponent).** Let $k=3d/4+O(1)$, normalize
> $w_z=m_{d,k}(z)/C(d,k)$, and form $Z(w)$ as in (13). Then
> 
> \[
>                  \log Z(w)=\frac{d}{4\ln2}+o(d).    \tag{15}
> \]
> 
> Put $\rho=(11/20)H_2(1/4)$ and let
> $M_d=2^{\rho d+o(d)}$. The complementary transform also has the
> direction-uniform floor
> 
> \[
> \min_{0\le q\le {d\choose k}}
> (1+q)\{1+M_d\underline W(q)\}
>                =M_d\,2^{o(d)}.                     \tag{15a}
> \]
> 
> The reflected statement holds for the maximum endpoint of the natural
> cups of $T(d,d-k)$.

**Proof.** Expand (13a) over Pascal lattice paths, as in the dominant-path
lemma of `PASCAL_WEIGHTED_INVERSION_LEX_SEAM_GATE.md`. Follow the initial
left spine for $h$ steps. The remaining cell has

\[
 D=d-h,\qquad K=k-h,\qquad
 1-\frac KD=\frac{d-k}{D}.                             \tag{16}
\]

At the boundary between its left and right children, the prefix scale is
$2^{H_2(K/D)D+o(d)}$. The normalized suffix mass pays the first right
delay

\[
 2^{-K_0(K/D)D+o(d)},\qquad
 K_0(y)=\frac{-\ln(1-y)-y}{\ln2}.                     \tag{17}
\]

All outer weighted-left factors cancel. This boundary therefore has
logarithmic potential

\[
 D\{H_2(y)-K_0(y)\}+o(d),\qquad y=K/D.                \tag{18}
\]

Since $D=(d-k)/(1-y)$, the largest exponent is

\[
 (d-k)\max_{0<y\le3/4}
       \frac{H_2(y)-K_0(y)}{1-y}+o(d).                \tag{19}
\]

Elementary differentiation gives the unique maximum at $y=1/2$. There
$H_2(1/2)=1$ and
$K_0(1/2)=1-1/(2\ln2)$, so (19) is $d/(4\ln2)+o(d)$.

For the upper bound, assign every suffix cut to the first Pascal node at
which it meets a right child. The same binomial comparison gives (18) for
that node. Summing delay partitions and the final $O(\sqrt d)$ boundary
levels costs $(d+1)^{O(\sqrt d)}=2^{o(d)}$. Passing to the lower-convex
envelope can only decrease this upper bound.

For the matching lower bound after convexification, take the node with
$D=2(d-k)+O(1)$, so $K/D=1/2+o(1)$, and denote its raw tail point by
$(q_0,W_0)$. Since every tail curve is decreasing, the function

\[
 h(q)=W_0\max\{0,1-q/q_0\}
\]

is convex and lies below the whole raw tail curve. Hence
$\underline W\ge h$ and

\[
 Z(w)\ge (q_0/2)h(q_0/2)=q_0W_0/4.                  \tag{19a}
\]

The raw upper bound already proved gives the reverse inequality at
exponential scale. Equation (18) at $y=1/2$ now proves (15).

For (15a), use the same node parameter $y$ and put

\[
 a(y)=\frac{1}{4}\frac{H_2(y)}{1-y},\qquad
 b(y)=\frac{1}{4}\frac{K_0(y)}{1-y}.                 \tag{19b}
\]

The raw-tail product has exponent

\[
             a(y)+\max\{0,\rho-b(y)\}.                \tag{19c}
\]

For a cut inside rather than at a Pascal child boundary, take the first
right child met by the suffix recursion (19e). It contains a neighboring
complete child suffix; the binomial comparison and terminal partition
bound change (19c) by only $o(d)$. Thus (19c) is a uniform lower bound for
all raw-tail points, not only for the displayed lattice-path boundaries.

Elementary calculus gives (19b) at least $\rho$: if $a(y)<\rho$, then
$H_2(y)>K_0(y)$ and hence $a(y)>b(y)$; if $a(y)\ge\rho$, the conclusion is
immediate. Therefore the raw tail lies above

\[
 g(q)=\max\!\left\{0,\frac{2^{-o(d)}}{1+q}
                           -\frac1{M_d}\right\}.       \tag{19d}
\]

The function $g$ is convex. Since $\underline W$ is the greatest convex
minorant of the raw tail, $\underline W\ge g$, which proves the lower
bound in (15a). At $q=0$, $\underline W(0)=1$, giving the matching upper
bound $1+M_d$. This proves (15a). $\square$

The suffix recurrence behind the proof is exact. Put
$\ell={d-1\choose k-1}$ and $r={d-1\choose k}$. If $q<\ell$, then

\[
 S_{d,k}(q)=C(d-1,k)+(1+r)S_{d-1,k-1}(q),             \tag{19e}
\]

whereas for $q\ge\ell$,
$S_{d,k}(q)=S_{d-1,k}(q-\ell)$. The verifier constructs the endpoint
distribution from these recurrences and takes its exact rational lower
convex hull.

The first endpoint atom is the all-left path

\[
 D(d,k)=\prod_{h=0}^{k-1}
          \left(1+{d-1-h\choose k-h}\right),          \tag{19f}
\]

so its normalized density is $D(d,k)/C(d,k)=2^{-o(d)}$. Equivalently, the
maximum-atom parameter is ${d\choose k}^{1-o(1)}$. The atom bound therefore
misses (15); the positive exponent comes from an exponentially wider
nested suffix at local density $1/2$.

## 4. The stretchable zipper

Pass the rows $z_n,z_{n-1},\ldots,z_1$ through all $m$ columns, completing
one row before starting the next. At a row boundary with $q$ rows still
unmoved, the two complementary factors are bounded by

\[
       1+q,
       \qquad
       1+m\frac{S_{d,k}(q)}{C(d,k)}.                  \tag{20}
\]

During the active row one adds at most its endpoint atom. Applying (15) at
$q$ and $q-1$ gives

\[
 \max_{\text{zipper states}}
 (1+\text{unmoved rows})
 (1+\text{weighted crossed columns})
       \le m\,2^{d/(4\ln2)+o(d)}+O(m+n).              \tag{21}
\]

The raw suffix curve has the same leading exponent as its lower-convex
envelope: this is the upper-bound part of the lattice-path argument in
Theorem 3. Hence Lemma 2 and (21) match at exponential scale. The rooted
zipper is the sharp one-rectangle regression, not merely a convenient
schedule.

The passage is stretchable. Start with two rational strong-glue clusters
near distinct macro points. Preserve each child order type by a positive
affine contraction. Make the row displacement scale $\varepsilon$ and the
total column displacement scale $\varepsilon^2$. Every cross-segment wall
then has the expansion

\[
        s_{ij}=s_0+\varepsilon\alpha_i
                     +\varepsilon^2\beta_j+O(\varepsilon^3),    \tag{22}
\]

with strict rational gaps. For sufficiently small rational
$\varepsilon$, walls are ordered first by the prescribed row and then by
the column. Strong-glue signs are open strict inequalities, so they remain
unchanged. Hence the upper side (21) is geometric, not merely pseudoline.

## 5. The two middle rectangles force the reset

Write the reverse top orders as

\[
              B_R,B_L,A_R,A_L.                         \tag{23}
\]

Theorem 3 first quantifies the sharp charge from the
$(B_L,A_L)$ middle rectangle. In the live scaling,
$m=|B_L|=2^{H_2(1/4)t+o(t)}$ and the row depth is
$s=(11/20)t+O(1)$, so Lemma 2 gives

\[
 \log\{mZ(w)\}
   =\left(H_2(1/4)+\frac{11}{80\ln2}\right)t+o(t).    \tag{23a}
\]

After division by $\log N=H_2(1/4)t+o(t)$ this is (3a), below even the
corner exponent $1.55$. Thus an unweighted area cut is wasteful, but even
the sharp weighted one-rectangle cut is quantitatively insufficient.

Here is the exact geometric contraction behind that calculation. The
dominant top modules are

\[
 \{S_L\cup\{p\}:S_L\in\mathcal C(A_L),\ p\in A_R\},
 \qquad
 \{\{x\}\cup T_R:x\in B_L,\ T_R\in\mathcal U(B_R)\}.   \tag{23b}
\]

They occupy a $2^{-o(t)}$ fraction of $C(A)$ and $U(B)$ respectively.
During the $(B_L,A_L)$ passage, summing over $p$ and $T_R$ cancels those
module sizes. Formula (6) leaves precisely

\[
 \left(1+\frac1{|B_L|}\sum_{x\in B_L}
                  \#\{A_L\text{ after }x\}\right)
 \left(1+\mathbb E_{S_L}
                  \#\{B_L\text{ after }\min S_L\}\right).       \tag{23c}
\]

The first factor is the uniform un-crossed-row count and the second is the
weighted crossed-column count in Lemma 2. Thus (23a) is an actual
directional cap/cup product inside the Pascal glue, with no abstract
profile substitution.

The other middle rectangle is $(B_R,A_R)$. For an arbitrary chamber $W$
define

\[
\begin{aligned}
 X_1(W)&=\mathbb E_{T_R\in\mathcal U(B_R)}
          \{1+\#(A_R\text{ before }\max T_R)\},\\
 X_2(W)&=\mathbb E_{p\in A_R}
          \{1+\#(B_R\text{ before }p)\},\\
 Y_1(W)&=\mathbb E_{x\in B_L}
          \{1+\#(A_L\text{ after }x)\},\\
 Y_2(W)&=\mathbb E_{S_L\in\mathcal C(A_L)}
          \{1+\#(B_L\text{ after }\min S_L)\}.
                                                               \tag{23d}
\end{aligned}
\]

The endpoint transform (6) and the two dominant modules (23b) factor
exactly:

\[
 \frac{C(W)U(W)}{C(A)U(B)}
 \ge 2^{-o(t)}
       \{X_1(W)X_2(W)\}\{Y_1(W)Y_2(W)\}.              \tag{23e}
\]

The reflected floor (15a), applied to the $(B_R,A_R)$ rectangle, gives in
**every** chamber

\[
                 X_1(W)X_2(W)
       \ge |A_R|\,2^{-o(t)}
       =2^{(11/20)H_2(1/4)t-o(t)}.                    \tag{23f}
\]

This bound is direction-uniform: it already uses the lower-convex envelope,
so arbitrary leakage through other rectangles cannot reduce it.

During a full cross-wall sweep every cell of $B_L\times A_L$ changes
order. Lemma 2 and Theorem 3 therefore give some chamber $W_*$ with

\[
 Y_1(W_*)Y_2(W_*)
  \ge2^{\{H_2(1/4)+11/(80\ln2)\}t-o(t)}.              \tag{23g}
\]

Combining (23e)--(23g), and using
$V(A\prec B)=C(A)U(B)2^{o(t)}$, proves:

> **Theorem 4 (Pascal cross-wall minimax).** Every monotone
> reverse-internal wall sweep of
> \[
> A=T((11/20)t,\,3(11/20)t/4),\qquad B=T(t,t/4)
> \]
> has a chamber satisfying
> \[
> \frac{C(W)U(W)}{V(A\prec B)}
> \ge N^{\,1.7945161063\ldots-o(1)}
> >N^{\log_2 3+\varepsilon}
> \]
> for an absolute $\varepsilon>0$.

No realizability assumption on the linear extension is used; the theorem
holds for every Young-lattice path and hence for every planar strong-glue
realization.

For calibration only, the verifier evaluates the five **completed
top-block** orders at $t=320$, $s=176$. Their normalized exponents relative
to $C(A)U(B)$ are

\[
 1.544139098,\quad1.885894890,\quad1.542513592,\quad
 1.990541438,\quad1.544139098.                         \tag{24}
\]

The finite rows (24) are only calibration; Theorem 4, not their sequential
completion, is the minimax argument.

The common-root alone is insufficient for fixed-edge dilution. A cap in
the dominant module has endpoints $(z,p)$ with common $z$ but variable
$p\in A_R$. Fixing $p$ loses $|A_R|$, precisely the factor retained by
(23f). The two-rectangle proof avoids this loss rather than silently
summing face-dependent edges.

## 6. Verification

Run

```text
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_pascal_ferrers_minimax_zipper_gate.py
```

The verifier uses exact integer endpoint matrices. It exhausts all $35960$
shuffles, solves (8), reconstructs the optimal $112$-swap path, checks the
Pascal minimum-endpoint recurrence and exact rational convex-tail statistic
through depth $24$, checks the companion-role convex floor at the same
depths, checks the local-density-one-half boundary through depth $640$,
verifies the exponent in Theorem 4, and evaluates the exact top-block rows
(24). Expected output begins

```text
PASS: Pascal Ferrers minimax/zipper gate
```
