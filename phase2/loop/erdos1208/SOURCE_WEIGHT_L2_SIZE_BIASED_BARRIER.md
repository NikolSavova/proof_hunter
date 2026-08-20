# Source-weight moments: an exact tilted identity and an L2 barrier

## 1. Outcome

Fix a dyadic group of clean fibres

\[
 \mathcal Q_h=\{q:h\le h_q<2h\},\qquad
 H_*=\sum_{q\in\mathcal Q_h}h_q,                          \tag{1.1}
\]

and retain the common translation in

\[
 C_*(r)=\sum_{q\in\mathcal Q_h}R_{B_q}(-18r).             \tag{1.2}
\]

There is an exact source-codegree-weighted second-moment inequality:

\[
 \boxed{
 \sum_{r\ne0}{C_*(r)^2\over R_D(-18r)}
 \le \sum_{q,q'\in\mathcal Q_h}|H_q\cap H_{q'}|^2
 \le \min\{2H_*^2,4hNH_*\}.}                            \tag{1.3}
\]

This is the sharpest universal size-biased statement obtained from the
source incidence alone.  Unfortunately, its bias is the source-side gap
`R_D(-18r)`, whereas endpoint amplification controls target richness at
`r`.  There is no known relation between those two gap cells.

The unweighted estimate that would combine perfectly with the new target
support tail is false.  Cauchy--Schwarz and

\[
 |\{r:U_L(r)\ge T\}|\ll {Nk^4\over T^2}                  \tag{1.4}
\]

would finish the reciprocal tail if

\[
 \boxed{
 \|C_*\|_2^2
 \le m^{o(1)}{N(H_*+k^3)^2\over k^4}.}                  \tag{1.5}
\]

But genuine polynomial-height scaled-parabola fibres violate (1.5) by
`k^(2-o(1))`.  Thus a marginal source moment cannot close the dense,
non-ultra-rich band.  The surviving possibility must restrict the moment
to target-rich `r`, or prove anti-correlation among target richness at `r`,
source-gap richness at `-18r`, and the common-`q` codegrees.

## 2. The exact common-translation expansion

Let `Sigma=A oplus A` be the set of unordered endpoint pair sums.  For
source edges `s,s' in Sigma`, define the dyadic clean codegree

\[
 c_*(s,s')
 =|\{q\in\mathcal Q_h:s,s'\in H_q\}|.                    \tag{2.1}
\]

The common `q` has not been discarded: expanding (1.2) gives

\[
 \boxed{
 C_*(r)=
 \sum_{\substack{s,s'\in\Sigma\\
       \delta(s)-\delta(s')=-18r}}c_*(s,s').}             \tag{2.2}
\]

Put

\[
 A_*(r)=
 \sum_{\substack{s,s'\in\Sigma\\
       \delta(s)-\delta(s')=-18r}}c_*(s,s')^2.            \tag{2.3}
\]

There are exactly `R_D(-18r)` ordered full-set edge pairs in the cell of
(2.2).  Cauchy--Schwarz inside this one scalar cell gives

\[
 \boxed{C_*(r)^2\le R_D(-18r)A_*(r).}                    \tag{2.4}
\]

Summing (2.3) over `r` retains only the norm gaps divisible by 18 and hence

\[
 \sum_rA_*(r)
 \le \sum_{s,s'}c_*(s,s')^2
 =\sum_{q,q'\in\mathcal Q_h}|H_q\cap H_{q'}|^2
 =:M_4.                                                   \tag{2.5}
\]

The middle equality is the exact Frobenius identity
`||I^T I||_F^2=||I I^T||_F^2` for the clean incidence matrix.  Equations
(2.4)--(2.5) prove the first inequality in (1.3).

There are also clean universal bounds on `M_4`.  Write
`d(s)=|{q in Q_h:s in H_q}|` and `Q=|Q_h|`.  Since
`|H_q cap H_q'|<2h`,

\[
\begin{aligned}
 M_4
 &<2h\sum_{q,q'}|H_q\cap H_{q'}|\\
 &=2h\sum_sd(s)^2\\
 &\le2hQ\sum_sd(s)
 =2hQH_*.
                                                               \tag{2.6}
\end{aligned}
\]

Every fibre has size at least `h`, so `Q<=H_*/h`; and every `q` is a
nonzero ordered point difference, so `Q<=k(k-1)=2N`.  Substitution in
(2.6) gives

\[
 M_4\le\min\{2H_*^2,4hNH_*\},                            \tag{2.7}
\]

as claimed.

## 3. What the universal moment bounds actually buy

For every nonzero gap, `R_(B_q)(-18r)<=h_q`, since a fixed difference is
a matching on the injectively labelled set `B_q`.  Also

\[
 \sum_{r\ne0}C_*(r)
 \le\sum_{q\in\mathcal Q_h}h_q(h_q-1)<2hH_*.
                                                               \tag{3.1}
\]

Consequently

\[
 \boxed{\|C_*\|_2^2<2hH_*^2.}                            \tag{3.2}
\]

Combining (3.2) with (1.4) gives

\[
 \sum_{r:U_L(r)\ge T}C_*(r)
 \ll {H_*k^2\sqrt{hN}\over T}.                           \tag{3.3}
\]

This reaches the desired scale `N(H_*+k^3)/T` only if

\[
 H_*k^2\sqrt{hN}\ll N(H_*+k^3),                          \tag{3.4}
\]

or, using `N asymp k^2`, roughly

\[
 H_*k\sqrt h\ll H_*+k^3.                                 \tag{3.5}
\]

This creates no genuinely new range.  Since `h<=N<k^2`, condition (3.5)
is at least as strong, up to constants, as the condition under which the
plain `L1` bound (3.1) already pays for every feasible `T<=N`.

The tilted estimate (1.3) does not recover the missing `1/T`.  For any set
`S` of gaps,

\[
\begin{aligned}
 \sum_{r\in S}C_*(r)
 &\le
 \left(\sum_{r\in S}R_D(-18r)\right)^{1/2}M_4^{1/2}\\
 &\le N M_4^{1/2}.                                        \tag{3.6}
\end{aligned}
\]

The global identity `sum_z R_D(z)=N^2` gives the last line.  In the whole
feasible range `T<=N`, inserting only the support estimate (1.4) cannot
improve that first factor: the bound `|S|N` is no smaller than `N^2` at
the relevant scale.  Thus (1.3) identifies the right common-translation
moment but also the exact sign/scale mismatch blocking it.

## 4. Why the sufficient unweighted L2 estimate is necessary

Let

\[
 S_T=\{r:U_L(r)\ge T\}.
\]

By (1.4),

\[
 \sum_{r\in S_T}C_*(r)
 \le |S_T|^{1/2}\|C_*\|_2
 \ll {\sqrt N,k^2\over T}\|C_*\|_2.                    \tag{4.1}
\]

For the right side to be bounded by the desired
`N(H_*+k^3)/T`, it is precisely sufficient to have (1.5).  The powers of
`T` cancel.  This explains why a source `L2` theorem looked attractive:
it would fill the entire interval between the elementary low-richness and
endpoint ultra-richness bounds in one step.

The next theorem shows that this route is unavailable without placing the
target-rich restriction inside the moment itself.

## 5. A genuine endpoint-realized counterexample

### Theorem 5.1

There are arbitrarily large integral distance-Sidon sets of polynomial
height and dyadic clean-fibre groups for which

\[
 \|C_*\|_2^2
 \ge {k^{8-o(1)}},                                        \tag{5.1}
\]

whereas the right side of (1.5), without its `m^(o(1))` factor, is
`O(k^6)`.  Hence (1.5) fails by `k^(2-o(1))`.

### Proof

For a prime `p`, take the integer finite-field parabola lift

\[
 P_p=\{(x,x^2\bmod p):0\le x<p\}\subset[0,p)^2.          \tag{5.2}
\]

It is vector-Sidon.  Its `p^3` ordered triple sums occupy at most `9p^2`
integer bins, so Cauchy--Schwarz gives triple energy at least `p^4/9`.
Collisions involving a shared point or an internally repeated point total
only `O(p^3)`: after cancellation, vector-Sidonicity fixes the remaining
unordered pair.  Thus there are `Omega(p^4)` disjoint equal-sum triple
pairs.

Choosing one distinguished anchor in each triple and an orientation gives
18 clean records per collision.  A record determines the collision, so

\[
 H:=\sum_qh_q=\Omega(p^4).                                \tag{5.3}
\]

A generic nonsingular integer linear map separates all squared edge
lengths while preserving these additive relations.  Polynomial finite
avoidance chooses the map with `p^O(1)` entries.  Finally multiply every
point by six.  The resulting set is still integral distance-Sidon, has
polynomial height, and has the same clean fibres.

There are `O(log p)` dyadic groups and at most `p(p-1)<p^2` nonempty
fibres.  Some group therefore satisfies

\[
 H_*\gg {p^4\over\log p}.                                 \tag{5.4}
\]

For this group put

\[
 S_2^*=\sum_{q\in\mathcal Q_h}h_q(h_q-1).
\]

Cauchy--Schwarz over its at most `p^2` fibres yields

\[
 S_2^*\gg {H_*^2\over p^2}-H_*
 \gg {p^6\over(\log p)^2}.                               \tag{5.5}
\]

Scaling by six multiplies every squared distance by 36.  Every nonzero
source norm gap is therefore divisible by 18, and (1.2) captures every
ordered unequal pair within every fibre.  Hence

\[
 \|C_*\|_1=S_2^*.                                         \tag{5.6}
\]

The support of `C_*` has size at most `N(N-1)<p^4`, because every source
gap is a difference of two of the `N` global distance labels.  Another
Cauchy--Schwarz application gives

\[
 \|C_*\|_2^2
 \ge{(S_2^*)^2\over N(N-1)}
 \gg {p^8\over(\log p)^4}.                               \tag{5.7}
\]

On the other hand, universally `H_*<=2N^2=O(p^4)`, so

\[
 {N(H_*+p^3)^2\over p^4}=O(p^6).                         \tag{5.8}
\]

Because the height is polynomial in `p`, an `m^(o(1))=p^(o(1))` factor
cannot absorb the ratio `p^2/(log p)^4`.  This proves the theorem.  QED.

This is an endpoint-realized obstruction: all `H_q` come from genuine
six-distinct common-translation rows.  It is not a counterexample to the
desired reciprocal target tail.  Indeed, the scaling deliberately exposes
the remaining issue: large source moment may sit on `r` for which the
target gap at `r` is absent or unrich.

## 6. Exact stress profiles

For each family below, choose the displayed heaviest dyadic group and
scale conceptually by six.  The scaling only relabels the full source-gap
counter, so all values are computed exactly before scaling.  Write

\[
 \Lambda={k^4\|C_*\|_2^2\over N(H_*+k^3)^2};             \tag{6.1}
\]

thus (1.5) would assert `Lambda=m^(o(1))`.

\[
\begin{array}{c|r|r|r|r|r|r}
\text{family}&h&H_*&S_2^*&|\operatorname{supp}C_*|&
 \|C_*\|_2^2&\Lambda\\ \hline
\text{closure }20&4&152&496&454&588&0.00745\\
\text{closure }40&8&7500&77136&31254&337112&0.21643\\
\text{closure }60&16&29344&626368&162152&5417424&0.65898\\
\text{parabola }17&8&1420&12488&7522&28104&0.43033\\
\text{parabola }31&64&18484&1291164&187010&13860724&11.8123\\
\text{parabola }43&128&84220&11823100&755526&287882776&40.6594\\
\text{parabola }61&256&358704&102855868&3138070&5126443444&113.0723
\end{array}                                               \tag{6.2}
\]

The closure profiles remain diffuse, while the parabola sequence visibly
crosses and then rapidly exceeds the sufficient `L2` scale.  The verifier
also checks (1.3) exactly on closure 40 and parabolas 31 and 43.  For
parabola 43 the selected group has

\[
 M_4=286617058,qquad
 \sum_r{C_*(r)^2\over R_D(-18r)}
 ={481959577\over14}.                                    \tag{6.3}
\]

Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_source_weight_l2_barrier.py
```

## 7. Exact remaining gate

The source moment has to know that `r` is target-rich.  In the notation
above, any successful refinement must control on

\[
 S_T=\{r:U_L(r)\ge T\}
\]

one of the genuinely joint quantities

\[
 \sum_{r\in S_T}C_*(r)^2,
 \qquad
 \sum_{r\in S_T}R_D(-18r)A_*(r),
 \qquad\text{or}\qquad
 \left(\sum_{r\in S_T}R_D(-18r)\right)
 \left(\sum_{r\in S_T}A_*(r)\right).                    \tag{7.1}
\]

The three factors that can no longer be separated are:

1. determinant-qualified target richness `U_L(r)`;
2. the population of the opposite-scale source gap cell `R_D(-18r)`; and
3. the common-translation fourth weight `A_*(r)`.

The endpoint tail controls the first marginal, and (1.3) controls the last
two after summing over every `r`.  The scaled-parabola theorem proves that
this loss of alignment is polynomially fatal.  A restricted, genuinely
three-way anti-correlation theorem is the remaining middle-band problem.
