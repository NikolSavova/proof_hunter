# A cellwise saturation--bank dichotomy

**Date:** 2026-08-15
**Verdict:** Boolean-downset interpolation has an exact structural companion
for genuine type-A reflection orders.  In every endpoint cell, a longest
forward path and a longest reverse path generate a Boolean bank of ordinary
faces.  If its size is denoted by \(B_{uv}\), then

\[
 \boxed{4G_{uv}(1/2)B_{uv}\ge X_{uv}},                 \tag{1}
\]

where \(X_{uv}=G_{uv}(1)\).  More precisely, if

\[
 \Delta_{uv}:=\log_2\!\frac{4G_{uv}(1/2)}
                         {X_{uv}^{\alpha}},\qquad
 \alpha=\log_2(3/2),                                  \tag{2}
\]

is the sharp interpolation defect, then

\[
 \boxed{B_{uv}\ge X_{uv}^{1-\alpha}2^{-\Delta_{uv}}.} \tag{3}
\]

The banks from different endpoint cells are disjoint.  Thus (3) really does
inject ordinary faces rather than count them with an uncontrolled overlap.
At zero defect the conclusion is much stronger: the cell contains **every**
subset of its open endpoint interval, so \(B_{uv}=X_{uv}=2^{v-u-1}\).

There is also a sharp limitation.  Interpolation defect cannot control the
number of failed Boolean coordinates, even up to a constant factor.  The
stretchable alternating family has linear shortcut codimension but defect
tending to only \(0.395\) or \(0.415\) bits.  Its longest-path bank still
contains a constant fraction of all ordinary faces in the cell.  A second
stretchable family has a constant bank and realizes the opposite branch of
(1) up to a factor tending to one.  Hence the product tradeoff is the
scope-safe conclusion; a defect bound proportional to shortcut codimension
is false on genuine reduced words.

This theorem does not prove \(H(R)=n^{o(1)}\).  It exposes the next overlap
gate precisely: the ordinary banks are globally disjoint, but (3) supplies
only the exponent \(1-\alpha\), while the high-defect branch increases the
half-activity side.  A closing argument would have to recycle that branch
through additional geometric structure.

## 1. Temporal support downsets and complementary coordinates

Fix endpoints \(u<v\).  Write the forward and reverse temporal path
polynomials as

\[
 R_{uv}(t)=t\sum_{S\in\mathcal L^+_{uv}}t^{|S|},
 \qquad
 B_{uv}(t)=t\sum_{T\in\mathcal L^-_{uv}}t^{|T|}.       \tag{4}
\]

Both support families are Boolean downsets: shortcutting an internal vertex
replaces two consecutive roots by the root lying between them in their
reflection packet and preserves the temporal direction.

The active coordinates of the two downsets are complementary.  For every
\(u<w<v\), the two-edge path \(u,w,v\) is temporal in exactly one direction,
because its two root times are distinct.  Conversely, if \(w\) occurs in a
longer path, shortcut closure puts the singleton \(\{w\}\) in the same
family.  Consequently no internal label occurs in both \(\mathcal L^+\)
and \(\mathcal L^-\), and every internal label occurs in one of them.

Put

\[
 x=|\mathcal L^+|=R_{uv}(1),\quad
 y=|\mathcal L^-|=B_{uv}(1),\quad X=xy,               \tag{5}
\]

and let \(r,s\) be their respective maximum support sizes.  Choose maximum
supports \(S_*,T_*\).  They are disjoint, and the downset property gives
\(2^{S_*}\subseteq\mathcal L^+\) and
\(2^{T_*}\subseteq\mathcal L^-\).  The path-pair/face bijection therefore
maps

\[
 (A,C)\longmapsto \{u,v\}\cup A\cup C,\qquad
 A\subseteq S_*,\ C\subseteq T_*                     \tag{6}
\]

injectively to ordinary faces in the \((u,v)\) cell.  Define

\[
 B_{uv}:=2^{r+s}.                                      \tag{7}
\]

This is a literal Boolean face bank.  Banks belonging to different endpoint
pairs are disjoint because a face uniquely determines its minimum and
maximum labels.

## 2. Exact rank-refined half-activity inequality

The following elementary strengthening of downset interpolation records the
bank dimension.

> **Lemma 1 (maximum-rank refinement).**  If \(\mathcal L\) is a nonempty
> Boolean downset of size \(m\) and maximum rank \(r\), then
> \[
>  \sum_{S\in\mathcal L}2^{-|S|}
>  \ge \Phi(m,r):=m2^{-r}-1+(3/2)^r.                    \tag{8}
> \]

**Proof.**  A maximum member contains a full \(r\)-cube, whose exact weight
is \((3/2)^r\).  Each of the other \(m-2^r\) members has rank at most \(r\)
and hence weight at least \(2^{-r}\).  Adding the two contributions gives
(8).  \(\square\)

Applying the lemma to both path families gives the stronger exact cell
bound

\[
 \boxed{
  4G_{uv}(1/2)\ge \Phi(x,r)\Phi(y,s).
 }                                                       \tag{9}
\]

Dropping the positive cube corrections in (8) gives

\[
 4G_{uv}(1/2)\ge xy,2^{-(r+s)}=X/B_{uv},              \tag{10}
\]

which is (1).

For the defect form, sharp downset interpolation gives \(\Delta_{uv}\ge0\)
and (10) gives

\[
 \Delta_{uv}
 \ge (1-\alpha)\log_2X-(r+s).                          \tag{11}
\]

Exponentiating the rearrangement of (11) proves (3).  Equivalently, for
every threshold \(D\ge0\), each cell obeys the exact alternative

\[
 \boxed{
 \Delta_{uv}\ge D
 \quad\text{or}\quad
 B_{uv}\ge 2^{-D}X_{uv}^{1-\alpha}.}                  \tag{12}
\]

The first branch says that half activity beats the sharp baseline by the
factor \(2^D\); the second supplies the displayed ordinary Boolean bank.

For a collection \(\mathcal C\) of endpoint cells, disjointness gives

\[
 F_R(1)\ge\sum_{e\in\mathcal C}B_e.                    \tag{13}
\]

Splitting at defect \(D\) therefore yields the genuinely cross-cell pair

\[
\begin{aligned}
 F_R(1)&\ge 2^{-D}\sum_{e\in\mathcal C:\,\Delta_e<D}
                         X_e^{1-\alpha},\\
 F_R(1/2)&\ge \frac{2^D}{4}
             \sum_{e\in\mathcal C:\,\Delta_e\ge D}X_e^\alpha.
                                                               \tag{14}
\end{aligned}
\]

There is no multiplicity loss in the first line.

## 3. Exact zero-defect rigidity

The interpolation theorem has a rigid equality case.

> **Lemma 2.**  For \(0<h<1\), a nonempty Boolean downset satisfies
> \[
>  \sum_{S\in\mathcal L}h^{|S|}=|\mathcal L|^{\log_2(1+h)}
> \]
> if and only if \(\mathcal L=2^A\) for some coordinate set \(A\).

**Proof.**  In the section induction, write
\(\mathcal L_1\subseteq\mathcal L_0\) and
\(a=|\mathcal L_0|,b=|\mathcal L_1|\).  Strict concavity in the scalar step
shows that equality is possible only when \(b=0\) or \(b=a\).  In the first
case the coordinate is absent; in the second the two sections coincide and
the coordinate is freely present.  Induction gives a full cube on exactly
the free coordinates.  The converse is immediate.  \(\square\)

If \(\Delta_{uv}=0\), both path families are therefore full cubes on their
active coordinates.  Those coordinate sets partition all
\(d=v-u-1\) internal labels, so every internal subset is a face with
endpoints \(u,v\).  Hence

\[
 \boxed{X_{uv}=B_{uv}=2^d.}                             \tag{15}
\]

This is the exact saturation--unweighted-bank statement suggested by the
strict cup, and it holds in every reflection order.

## 4. Why defect cannot measure shortcut codimension

The quantitative strengthening

\[
 \Delta_{uv}\gtrsim d-(r+s)                             \tag{16}
\]

is false, even for stretchable reflection orders.  The sign families used
below have a uniform exact realization.  Given signs
\(\epsilon_i\in\{-1,+1\}\), take \(M=4n+1\) and

\[
 p_i=(i,\epsilon_iM^{n-i})\quad(0\le i\le n-3),
 \qquad p_{n-2}=(n-2,0),\quad p_{n-1}=(n-1,0).
\]

In every triple the term containing the least-index height dominates the
other two, so \(\chi(i,j,k)=\epsilon_i\).  The same leading-power argument
shows that no two pair slopes coincide.  Sorting the slopes therefore gives
a generic stretchable reflection order and an adjacent-swap reduced word for
\(w_0\).

First use the alternating choice

\[
 \chi(i,j,k)=(-1)^i\qquad(i<j<k).                       \tag{17}
\]

One path direction is direct-only.  At endpoint distance \(d\), the other
has

\[
 R_d(t)=t+t^2\sum_{q=1}^{d-1}(1+t)^{\lfloor(q-1)/2\rfloor},
 \qquad r=\lfloor d/2\rfloor.                           \tag{18}
\]

For \(d=2m\), exact evaluation gives

\[
 R_d(1)=3\,2^{m-1}-1,\qquad
 2R_d(1/2)=\frac52(3/2)^{m-1}-1,                       \tag{19}
\]

and for \(d=2m+1\),

\[
 R_d(1)=2^{m+1}-1,\qquad
 2R_d(1/2)=2(3/2)^m-1.                                 \tag{20}
\]

Thus \(d-r=\lceil d/2\rceil\) is linear, whereas the cell defect tends to

\[
 \begin{cases}
 \log_2(5/2)-\alpha\log_2 3=0.394784\ldots,&d\text{ even},\\
 1-\alpha=0.415037\ldots,&d\text{ odd}.
 \end{cases}                                           \tag{21}
\]

The Boolean bank is nevertheless large:

\[
 B_{uv}=2^{\lfloor d/2\rfloor}=\Theta(X_{uv}).          \tag{22}
\]

So a constant defect is compatible with linearly many failed Boolean
coordinates, but in this family the longest path itself retains a constant
fraction of the unweighted cell.

## 5. The opposite branch is also sharp

The same geometric construction realizes any prescribed signs depending
only on the least triple index.  Take

\[
 \chi(0,j,k)=+1,\qquad \chi(i,j,k)=-1\quad(i>0).         \tag{23}
\]

For the extreme cell \((0,n-1)\), put \(d=n-2\).  The rich path family is
exactly the empty support and all \(d\) singleton supports.  Hence

\[
 R(t)=t+dt^2,\qquad B(t)=t,\qquad X=d+1,               \tag{24}
\]

\[
 4G(1/2)=1+d/2,\qquad B_{0,n-1}=2.                     \tag{25}
\]

Lemma 1 is equality here, and

\[
 \frac{4G(1/2)B_{0,n-1}}{X}=\frac{d+2}{d+1}\to1.      \tag{26}
\]

Thus a constant ordinary bank can coexist with only a logarithmic
interpolation defect,

\[
 \Delta=(1-\alpha)\log_2d-1+o(1),                      \tag{27}
\]

and the basic product tradeoff (1) is asymptotically sharp on genuine
reduced words.

## 6. Regression on the saved 58-wire adversary

The certified finite word which falsifies \(H\le2\) also shows the scale
still missing from (14).  Exact longest-temporal-path dynamic programming
gives

\[
 \sum_{u<v}B_{uv}=55{,}221,\qquad
 F_R(1)-1-n=1{,}059{,}609.                              \tag{28}
\]

The largest bank dimension in any cell is only eight.  In the extreme cell
\((0,57)\), the forward and reverse maximum ranks are \(3,1\), while

\[
 X_{0,57}=1950,\qquad 4G_{0,57}(1/2)=1431/4.            \tag{29}
\]

Thus (1) holds there with ratio \(2.935\ldots\), but the chosen Boolean
banks account for only about five percent of the full nontrivial face count
after summing all endpoint cells.  This is not a counterexample to the
dichotomy--the inequalities pass exactly--but it certifies that the bank
needs another amplification or recycling step before it can address the
live asymptotic target.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_coxeter_global_half/verify_saturation_bank_dichotomy.py
```

The dependency-free checker exhausts all Boolean downsets through four
coordinates, including the equality classification and rank refinement.  It
then constructs exact integer coordinates for both sign families, sorts
their rational slopes, verifies that every crossing is an adjacent swap in
a reduced word for \(w_0\), checks the temporal-path classification by
explicit support enumeration at small sizes, and replays (18)--(27) using
exact transvection products through 48 wires.  Finally it replays the saved
58-wire reduced word, computes every maximum temporal rank, and checks
(1), (3), (8), and (28)--(29) cell by cell.
