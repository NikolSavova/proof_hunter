# High-determinant reciprocal tail: endpoint wedge amplification

## 1. Outcome

There is a rigorous endpoint-aware quadratic tail in the surviving
high-determinant regime.  If a norm gap has `T` determinant-qualified target
representations, then their first target edges span at least

\[
 {2T^2\over k}-T                                           \tag{1.1}
\]

endpoint wedges.  Summed over all gaps, these wedges have an exact global
lift bounded by `O(Nk^3)`.  Consequently, for any dyadic group of clean
fibres of total mass `H_*`,

\[
 \boxed{
 \sum_{r:U_L(r)\ge T} C_*(r)
 \ll {H_*Nk^4\over T^2}\qquad(T\ge k),}                   \tag{1.2}
\]

where `U_L(r)` counts target representations with doubled determinant
larger than `L`, and `C_*(r)` retains the full common-translation `q` weight.

This proves the desired reciprocal tail in the ultra-rich range

\[
 T\gg \max\left\{k,{H_*k^4\over H_*+k^3}\right\}.         \tag{1.3}
\]

The range is genuine but not sufficient for #1208: in dense clean-fibre
groups the second threshold can exceed the universal `T<=N`.  The exact
remaining obstruction is now visible.  Endpoint amplification supplies a
quadratic `T^2/k`, but the crude bound `C_*(r)<=H_*` loses the entire clean
mass on every rich gap.  A full proof needs a weighted version of the wedge
identity, not merely the unweighted target endpoint graph.

## 2. Full common-translation form of the source weight

Let

\[
 C(r)=\sum_qR_{B_q}(-18r),                                  \tag{2.1}
\]

where `B_q=delta(H_q)`.  Because every realized difference and every pair
sum has a unique endpoint representation, `C(r)` is exactly the number of
ordered endpoint systems

\[
 (a,b,c,d,c',d',e,f,e',f')                                \tag{2.2}
\]

satisfying

\[
\begin{aligned}
 q&=a-b,\\
 e+f&=c+d+q,\\
 e'+f'&=c'+d'+q,\\
 |c-d|^2-|c'-d'|^2&=-18r.                                 \tag{2.3}
\end{aligned}
\]

Each of `(a,c,d,b,e,f)` and `(a,c',d',b,e',f')` obeys the
six-distinct clean condition.  Possible overlaps between the two rows are
retained.  Thus (2.1) has not forgotten the common anchor difference `q` or
either clean translate.

The determinant-decorated refinement also records

\[
 e_s=2\det(c-d,c'-d').                                    \tag{2.4}
\]

The target side consists of ordered scalar-target edges with displacements
`u,v` satisfying

\[
 |u|^2-|v|^2=r,qquad d_t=2\det(u,v).                       \tag{2.5}
\]

The previous Gaussian theorem bounds every fixed `(r,d_t)` cell by
`m^(o(1))`; the adaptive low-`|d_t|` contribution is already
`m^(o(1))NH`.  Everything below applies after retaining only
`|d_t|>L`.

## 3. Endpoint graph of one rich target gap

Let `D=delta(Sigma)`.  For fixed `r!=0` and determinant cutoff `L`, define

\[
 \mathcal P_{r,L}
 =\{(t,t')\in\Sigma^2:
     \delta(t)-\delta(t')=r,
     |2\det(v_t,v_{t'})|>L\},                              \tag{3.1}
\]

and put `U_L(r)=|P_(r,L)|`.

Both projections of `P_(r,L)` are injective.  Indeed, one edge norm
determines the other norm, and all edge norms are distinct.  Let `E_(r,L)`
be the simple graph on `A` formed by the first endpoint edges `t`.  It has
exactly `U_L(r)` edges.  If its endpoint degrees are `d_x`, then

\[
 W_{r,L}=\sum_x{d_x\choose2}.                              \tag{3.2}
\]

Cauchy--Schwarz and `sum_x d_x=2U_L(r)` give

\[
 \boxed{
 W_{r,L}\ge {2U_L(r)^2\over k}-U_L(r).}                   \tag{3.3}
\]

This retains the high determinant condition on every target record.  In
particular, if `U_L(r)>=T>=k`, then

\[
 W_{r,L}\ge {T^2\over k}.                                 \tag{3.4}
\]

There is also a simultaneous matching extraction.  Make a conflict graph
on `P_(r,L)`, joining two records if their first edges meet or their second
edges meet.  Projection injectivity gives maximum conflict degree at most
`4(k-2)`.  Greedy independence produces at least

\[
 \boxed{
 \left\lceil{U_L(r)\over4k-7}\right\rceil}                \tag{3.5}
\]

records whose first edges form a matching and whose second edges form a
matching.  Thus an ultra-rich high-area gap always contains a linear-sized
bi-endpoint-disjoint scalar channel after the inevitable factor `k` loss.

## 4. Exact global wedge lift

First take `L=-1`, so every representation is retained.  Write

\[
 \mathcal E_r=\{t\in\Sigma:\delta(t)-r\in D\}.             \tag{4.1}
\]

For an unordered endpoint wedge `{t_1,t_2}` in the complete graph on `A`,
put `g=delta(t_1)-delta(t_2)`.  The wedge belongs to `E_r` exactly when

\[
 \delta(t_1)-r,\ \delta(t_2)-r\in D.                      \tag{4.2}
\]

The number of such `r` is `R_D(g)`.  One of them is `r=0`, which is excluded
from the scalar off-diagonal tail.  Hence the exact identity is

\[
 \boxed{
 \sum_{r\ne0}W_r
 =\sum_{\{t_1,t_2\}\text{ endpoint wedge}}
    \bigl(R_D(\delta(t_1)-\delta(t_2))-1\bigr).}            \tag{4.3}
\]

There are exactly

\[
 k{k-1\choose2}                                           \tag{4.4}
\]

unordered endpoint wedges, and `R_D(g)<=N`.  Therefore

\[
 \boxed{
 \sum_{r\ne0}W_r
 \le (N-1)k{k-1\choose2}< {1\over2}Nk^3.}                 \tag{4.5}
\]

For determinant-truncated graphs, `E_(r,L)` is a subgraph of `E_r`, so its
wedge count is no larger.  Combining (3.4) and (4.5) yields

\[
 \boxed{
 |\{r:U_L(r)\ge T\}|
 \ll {Nk^4\over T^2}\qquad(T\ge k).}                     \tag{4.6}
\]

This is the promised quadratic rich-gap support tail.  Unlike Markov's
`N^2/T`, it is explicitly generated by endpoint reuse and continues to hold
after determinant truncation.

## 5. Retaining `q`: a dyadic clean-fibre tail

Group differences `q` by

\[
 h\le h_q<2h,
 \qquad
 H_*:=\sum_{q\text{ in the group}}h_q.                    \tag{5.1}
\]

Let `C_*(r)` be (2.1) restricted to this group.  For one `q`, a fixed
nonzero radius gap gives a matching inside the injectively labelled set
`B_q`, so it occurs at most `h_q` times.  Therefore

\[
 \boxed{C_*(r)\le H_*.}                                   \tag{5.2}
\]

Every scalar collision left after the adaptive determinant cut has

\[
 |d_t|>{N\over h_q}>{N\over2h}=:L_h.                      \tag{5.3}
\]

Thus the common high-determinant target graph for the group is controlled by
`U_(L_h)(r)`.  Equations (4.6) and (5.2) prove

\[
\begin{aligned}
 \sum_{r:U_{L_h}(r)\ge T}C_*(r)
 &\le H_*|\{r:U_{L_h}(r)\ge T\}|\\
 &\ll {H_*Nk^4\over T^2},
\end{aligned}                                             \tag{5.4}
\]

which is (1.2).  Comparing it with the desired dyadic reciprocal tail

\[
 {N(H_*+k^3)\over T}                                      \tag{5.5}
\]

shows that (5.5) is proved whenever (1.3) holds.  Summing the `O(log k)`
fibre-size groups costs only `m^(o(1))`.

This is a genuine endpoint-aware range theorem.  It preserves `q` through
`C_*`, preserves determinant qualification through `U_(L_h)`, and uses the
common-translation structure at least through the sharp per-gap matching
bound (5.2).  Its limitation is equally exact: (5.2) does not decrease with
target richness.

## 6. Exact stress profiles

The companion verifier checks (3.3), (3.5), and the exact identity (4.3) on
all ordered target pairs.  It reports

\[
\begin{array}{c|r|r|r|r|r}
\text{family}&k&\max_{r\ne0}R_D(r)&W_{r_{\max}}&
 \sum_{r\ne0}W_r&\text{double matching}\\ \hline
\text{closure }20&20&35&108&35495&6\\
\text{Costas }22&22&19&37&13808&5\\
\text{parabola }43&43&11&6&22946&4\\
\text{perpendicular ruler }40&40&24&234&161576&2\\
\text{quadratic-gap family }32&32&128&1408&86444&8
\end{array}                                               \tag{6.1}

The quadratic-gap family has the strongest possible raw richness and
substantial endpoint amplification, but no clean fibres.  This again shows
why the target endpoint theorem must ultimately be coupled more tightly to
the source common translations.

For the stored 40-point closure family, the exact raw-rich weighted tails
`(# rich gaps, sum C(r))` are

\[
\begin{array}{c|r|r}
T&\#\{r:R_D(r)\ge T\}&\sum C(r)\\ \hline
20&8958&7374\\
40&1612&4046\\
60&260&1454\\
80&30&240\\
90&10&70\\
100&2&12
\end{array}                                               \tag{6.2}

The size-biased decay is much stronger than the worst-case estimate (5.4),
but the proof does not yet recover it.

## 7. Exact remaining gate

The endpoint theorem supplies the correct quadratic amplification on the
target side.  To finish the reciprocal tail, one needs to replace the crude
product

\[
 H_*\cdot\sum_r1_{U_{L_h}(r)\ge T}                        \tag{7.1}
\]

by a weighted wedge identity in which `C_*(r)` is charged across the target
wedges themselves.  Expanded in endpoints, this means controlling systems
(2.2)--(2.5) in which two scalar-target records additionally share an
endpoint.  The common `q` must remain present; previous Gaussian-cell
profiles show that discarding it loses a linear codegree factor.

Run `verify_metric_scalar_endpoint_rich_tail.py` for all exact identities,
determinant truncations, matching extractions, and stress values.
