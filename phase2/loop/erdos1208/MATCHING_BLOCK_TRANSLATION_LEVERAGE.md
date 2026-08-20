# Matching-block translation leverage: exact identities and a sharp barrier

## 1. Verdict

The common translation does yield two exact positive mechanisms:

1. endpoint imbalance is measured exactly by target wedges plus endpoint
   escape; and
2. target wedges either expose many realized differences, or create many
   target `C_4`'s, each of which induces an eight-distinct-endpoint
   parallelogram among source pair sums.

But target wedges cannot be forced, even for a linear-sized clean block in a
genuine integral distance-Sidon set.  For every `L` there is an explicit
integral distance-Sidon set of size `4L+2` with one clean fibre containing a
source matching `F` of size `L` for which `tau_q(F)` is also a matching.
Thus

\[
 W(\tau_q(F))=0                                             \tag{1.1}
\]

and the number of wedge-induced realized shifts is zero.  The raw conjecture
that a matching channel must expose `Omega(L^2)` cross-edge shifts through
target endpoint reuse is false.  Any surviving channel-overlap theorem must
add scalar-energy concentration, count all cross pairs rather than wedges,
or exploit the eight-endpoint `C_4` branch described below.

## 2. Endpoint discrepancy identity

Let `F subset H_q` be a source matching of size `L`.  Write `T=tau_q(F)`,
let `f(x)` be the source endpoint indicator, and let `d(x)` be the target
degree.  Put

\[
 u(x)=d(x)-f(x),\qquad
 W(T)=\sum_x {d(x)\choose2},\qquad
 E(T,F)=\sum_{x\notin V(F)}d(x).                            \tag{2.1}
\]

Summing `e+f-c-d=q` over the block gives

\[
 \sum_xu(x)=0,\qquad \sum_xu(x)x=Lq.                       \tag{2.2}
\]

Since `F` is a matching, `sum f(x)=sum f(x)^2=2L`.  Therefore

\[
\begin{aligned}
 \sum_xu(x)^2
 &=\sum_xd(x)^2+2L-2\sum_{x\in V(F)}d(x)\\
 &=\boxed{2\bigl(W(T)+E(T,F)\bigr)}.                       \tag{2.3}
\end{aligned}
\]

For every origin `z`, Cauchy--Schwarz gives the exact quantitative
consequence

\[
 \boxed{
 W(T)+E(T,F)\ge
 {L^2|q|^2\over2\sum_{x\in A}|x-z|^2}.}                   \tag{2.4}
\]

Thus translation forces either endpoint reuse or endpoint escape, but not
reuse alone.  The counterfamily below pays (2.3) entirely through escape.

## 3. Wedges expose shifts, with `C_4` as the exact obstruction

For an ordered target wedge `(x,y,z)`, with target edges `xy` and `xz`, let
their source pair sums be `s_xy` and `s_xz`.  Translation gives

\[
 s_{xy}-s_{xz}=y-z.                                        \tag{3.1}
\]

Hence every wedge exposes a realized nonzero difference of `A`.  Because
distance-Sidonicity makes an oriented difference determine its ordered
endpoint pair, the multiplicity of the shift `y-z` is exactly

\[
 \mu(y-z)=|N_T(y)\cap N_T(z)|.                             \tag{3.2}
\]

Let `R` be the number of oriented shifts exposed, and let `C_4(T)` count
unoriented four-cycles.  Direct double counting gives

\[
 \sum_r\mu(r)=2W(T),\qquad
 \boxed{\sum_r\mu(r)^2=2W(T)+8C_4(T)}.                    \tag{3.3}
\]

Consequently

\[
 \boxed{R\ge {4W(T)^2\over2W(T)+8C_4(T)}}.                \tag{3.4}
\]

A star has `W=Theta(L^2)`, no four-cycles, and exposes `Theta(L^2)` distinct
oriented shifts.  If (3.4) is weak, many target four-cycles are present.
For a cycle with target edges `xy,xz,x'y,x'z`, translation yields

\[
 s_{xy}+s_{x'z}=s_{xz}+s_{x'y}.                            \tag{3.5}
\]

The four source edges lie in the matching `F`, so they have eight distinct
endpoints.  Thus the only multiplicity obstruction to wedge exposure comes
with a concrete higher additive relation, rather than disappearing.

## 4. A universal bi-matching extraction

Let `Delta=floor((k-3)/2)`.  The star-to-matching theorem and its target-side
dual give maximum degree at most `Delta` in both the source graph of `H_q`
and its target image.

Make a conflict graph on the `h_q` clean records, joining two records when
their source edges meet or their target edges meet.  The two conflict types
are disjoint by star-to-matching.  A record has at most

\[
 4(\Delta-1)                                               \tag{4.1}
\]

neighbours.  Greedy independence therefore proves

\[
 \boxed{|F|\ge\left\lceil{h_q\over4\Delta-3}\right\rceil} \tag{4.2}
\]

for some `F` such that both `F` and `tau_q(F)` are matchings.  In particular,
a fibre of order `k^2` always contains a linear-sized block with no target
wedges.  This is useful extraction information, but it runs opposite to a
wedge-forcing proof.

## 5. Explicit infinite integral counterfamily

Fix `B>=10`.  On the integer line take anchors

\[
 b=0,\qquad a=1,
\]

and, for `0<=i<L`, take

\[
\begin{aligned}
 c_i&=B^{3i+1},&d_i&=B^{3i+2},&e_i&=B^{3i+3},\\
 f_i&=1+c_i+d_i-e_i.
\end{aligned}                                               \tag{5.1}
\]

Translate the whole set if nonnegative coordinates are desired.  Put
`q=a-b=1`.  Then all six points in each row are distinct and

\[
 e_i+f_i=c_i+d_i+q.                                       \tag{5.2}
\]

Thus `s_i=c_i+d_i` belongs to `H_q`.  The `L` source edges `c_i d_i` are a
matching, and their target edges `e_i f_i` are another matching, disjoint
from the source endpoint set.

It remains to check that this is genuinely distance-Sidon.  Before applying
the powers of `B`, regard `1,c_i,d_i,e_i` as independent basis vectors
`Q,C_i,D_i,E_i`, and regard

\[
 f_i=Q+C_i+D_i-E_i.                                       \tag{5.3}
\]

The set

\[
 \{0,Q,C_i,D_i,E_i,Q+C_i+D_i-E_i:0\le i<L\}              \tag{5.4}
\]

is Sidon in the free abelian group.  Indeed, private block coordinates
identify the two summands unless both lie in one block; the finite one-block
table is injective once the `Q` coordinate is retained (in particular it
separates `C_i+D_i` from `E_i+(Q+C_i+D_i-E_i)`).

Every coefficient in a difference of two points lies in `[-2,2]`.  If two
integer differences obtained from (5.1) were equal up to sign, subtracting
their coefficient vectors would give a base-`B` relation with digits in
`[-4,4]`.  The highest nonzero digit dominates all lower digits when
`B>=10`, so no such relation exists.  Hence unordered absolute differences,
and therefore squared Euclidean distances after embedding on the x-axis,
are all distinct.

This proves an infinite genuine counterfamily with

\[
 k=4L+2,\qquad |F|=L,\qquad W(\tau_q(F))=0.                \tag{5.5}
\]

## 6. Finite geometric stress and status

The 43-point transformed parabola also contains an exact clean double
matching of size 18 in its fibre `q=(396,-38)`.  Its source and target
matchings share 31 of their 36 endpoint vertices, so only five target
incidences escape; nevertheless the target wedge count is still zero.
Here (2.3) reads `sum u(x)^2=10=2(0+5)`.

The companion verifier checks the infinite construction for
`L=1,2,4,8,16`, every distance, all clean translations, (2.2)--(2.4), the
star and four-cycle instances of (3.3), and the exact parabola certificate.

The durable restart target is therefore not “force wedges from a matching
block.”  It is one of:

* show that a **scalar-energy-concentrated** bi-matching block exposes its
  quadratic cross pairs by another complete-difference map;
* charge the escape term in (2.3) across many fibres; or
* exploit the eight-distinct source parallelograms forced by the `C_4`
  obstruction in (3.5).
