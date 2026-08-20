# Weighted common-translation wedges: switching theorem and replacement branch

## 1. Outcome

The weighted target-wedge mass from the endpoint-rich reduction admits a
rigorous source-codegree dichotomy.  Write

\[
 c(p)=|Q_p|,\qquad
 Q_p=\{q:s,s'\in H_q\},\qquad p=(s,s'),                 \tag{1.1}
\]

for an ordered pair of distinct source pair sums.  Associated to `p` are
two graphs, formed by the clean target edges `E(s+q)` and `E(s'+q)` as
`q` runs through `Q_p`.  If `W_0(p),W_1(p)` are their endpoint-wedge
counts and `I(p)` counts pairs of translations which are wedges in both
roles, then

\[
 \boxed{I(p)={\rho(p)\choose2}}                           \tag{1.2}
\]

for one rigid endpoint-replacement pencil of size `rho(p)<=k-2`.  Moreover,

\[
 \boxed{
 O(p):=W_0(p)+W_1(p)-2I(p)
 \ge {4c(p)^2\over k}-2c(p)-\rho(p)(\rho(p)-1).}          \tag{1.3}
\]

Thus, whenever `c(p)>=k`, either

\[
 \rho(p)\ge {c(p)\over\sqrt{k}}                          \tag{1.4}
\]

or

\[
 \boxed{O(p)\ge {c(p)^2\over k}.}                        \tag{1.5}
\]

The first case is completely classified: all its simultaneous overlaps
replace the same endpoint `x` by the same endpoint `y`, retaining a varying
outer endpoint `u`, and `y-x=s'-s`.  It can occur only for
`c(p)<=(k-2)sqrt(k)`.  The second case gives the requested endpoint-wedge
amplification for every source pair outside that rigid branch.

There is also an exact global switch which retains both clean translations.
For `q!=q'`, put

\[
 J(q,q')=|H_q\cap H_{q'}|                                \tag{1.6}
\]

and let `A(q,q')` count starts `s` in this intersection for which the two
target edges `E(s+q),E(s+q')` meet.  Then

\[
\boxed{
\begin{aligned}
 \sum_p W_0(p)&=\sum_{q<q'}A(q,q')(J(q,q')-1),\\
 \sum_p I(p)&=\sum_{q<q'}A(q,q')(A(q,q')-1),\\
 \sum_p O(p)&=2\sum_{q<q'}A(q,q')(J(q,q')-A(q,q')).
\end{aligned}}                                           \tag{1.7}
\]

Every nonzero `A(q,q')` is itself a rigid pencil with fixed outer endpoints
and a moving common endpoint; in particular `A(q,q')<=k-2`.

Most importantly, (1.7) has an exact weighted version.  It converts the
surviving weighted scalar problem into a mixed double-wedge mass rather than
discarding `q`.  This is a genuine advance, but not yet the full reciprocal
tail theorem: the mixed mass and the replacement-pencil branch still need
global bounds.

## 2. Setup

Let `A` be a `k`-point integral distance-Sidon set.  Let `Sigma` be its
unordered pair-sum set and `E(s)` the unique endpoint edge represented by
`s in Sigma`.  Distinct distances imply both:

* pair sums in `Sigma` are unique; and
* every nonzero directed difference of points of `A` has a unique ordered
  endpoint representation.

For a clean fibre `H_q`, membership `s in H_q` supplies the target pair sum
`s+q in Sigma`.  Fix an ordered pair `p=(s,s')`, `s!=s'`, and define `Q_p`
and `c(p)` by (1.1).  For `q in Q_p`, write

\[
 e_0(q)=E(s+q),\qquad e_1(q)=E(s'+q).                    \tag{2.1}
\]

Both maps `q -> e_i(q)` are injective.  Define

\[
\begin{aligned}
 W_i(p)&=\#\{\{q,q'\}\subset Q_p:e_i(q)\cap e_i(q')
                 \ne\varnothing\},\\
 I(p)&=\#\{\{q,q'\}\subset Q_p:
      e_0(q)\cap e_0(q')\ne\varnothing,
      e_1(q)\cap e_1(q')\ne\varnothing\}.
                                                               \tag{2.2}
\end{aligned}
\]

Thus `O(p)=W_0+W_1-2I` counts translation pairs which overlap in exactly
one target-edge role.

## 3. Simultaneous-overlap classification

Suppose two records `q,q'` overlap in both roles.  Name their first-role
edges

\[
 e_0(q)=\{x,u\},\qquad e_0(q')=\{x,v\},                 \tag{3.1}
\]

and their second-role edges

\[
 e_1(q)=\{y,u'\},\qquad e_1(q')=\{y,v'\}.               \tag{3.2}
\]

Because the pair-sum shift from role zero to role one is the same in both
records,

\[
 (y+u')-(x+u)=(y+v')-(x+v)=s'-s.                         \tag{3.3}
\]

Subtracting gives `u'-v'=u-v`.  Uniqueness of directed differences forces

\[
 u'=u,\qquad v'=v.                                       \tag{3.4}
\]

Consequently

\[
 e_0(q)=\{x,u\}\longmapsto e_1(q)=\{y,u\},
 \qquad y-x=s'-s,                                        \tag{3.5}
\]

and similarly for `q'`.  The directed difference `s'-s` determines the
ordered centre pair `(x,y)` uniquely.  Therefore every simultaneous pair
for this fixed `p` belongs to one and the same replacement pencil.  Let
`rho(p)` be its number of records.  Any two pencil records overlap in both
roles, proving (1.2).  Their retained endpoints are distinct and avoid
`x,y`, so `rho(p)<=k-2`.

The clean fixed-fibre star-to-matching lemma adds useful source structure.
Every replacement record has meeting target edges, hence its source edges
`E(s),E(s')` are disjoint.  Writing the replacement centres as `(x,y)`, the
identity `s'-s=y-x` gives

\[
 s+y=s'+x.                                                \tag{3.6}
\]

If `y` is not an endpoint of `E(s)` and `x` is not an endpoint of `E(s')`,
then (3.6) is a six-distinct clean incidence, so

\[
 \boxed{s\in H_{s'-s}.}                                 \tag{3.7}
\]

Thus the rigid branch is either a nested clean fibre or one of the two
explicit cross-endpoint degeneracies.  It is not an unspecified high
codegree exception.

## 4. Proof of the fixed-pair dichotomy

For role `i`, let `d_x` be endpoint degrees in the `c(p)`-edge simple graph
formed by `e_i(q)`.  Since `sum_x d_x=2c(p)`, Cauchy--Schwarz gives

\[
 W_i(p)=\sum_x{d_x\choose2}
 \ge {2c(p)^2\over k}-c(p).                              \tag{4.1}
\]

Equations (1.2) and (4.1) imply (1.3).  If `c(p)>=k` and
`rho(p)<c(p)/sqrt(k)`, then

\[
\begin{aligned}
 O(p)
 &>{4c(p)^2\over k}-2c(p)-{c(p)^2\over k}\\
 &= {3c(p)^2\over k}-2c(p)
 \ge {c(p)^2\over k},
\end{aligned}                                             \tag{4.2}
\]

which proves (1.4)--(1.5).  Also `rho(p)<=k-2` shows that the replacement
alternative is impossible once `c(p)>(k-2)sqrt(k)`.

The replacement sizes also have a useful aggregate first moment.  A record
counted by `rho(p)` is exactly an ordered pair of starts in one `H_q` whose
two target edges meet.  If the target-edge graph of `H_q` has endpoint
degrees `d_x`, its number of ordered wedges is

\[
 \sum_xd_x(d_x-1)\le(k-2)\sum_xd_x=2(k-2)h_q.            \tag{4.3}
\]

Consequently

\[
 \boxed{\sum_p\rho(p)\le2(k-2)H.}                        \tag{4.4}
\]

For the replacement alternative in (1.4), this proves the aggregate bound

\[
 \boxed{
 \sum_{p:\rho(p)\ge c(p)/\sqrt{k}}c(p)
 \le2(k-2)\sqrt{k}\,H.}                                 \tag{4.5}
\]

This is not by itself strong enough for #1208, but it shows that the rigid
exception has only `O(k^(3/2)H)` total common-translation mass rather than
the unconstrained codegree second moment.

In particular, if a dyadic block contains `P` distinct pairs with
`K<=c(p)<2K`, `K>=k`, then outside the replacement branch those pairs
produce at least

\[
 {PK^2\over k}                                           \tag{4.6}
\]

one-role common-translation wedges.  This is the precise version of the
"many distinct pairs amplify; high overlap is structured" dichotomy.

## 5. Exact fibre-pair switch

Fix an unordered fibre pair `{q,q'}`.  Put

\[
 \mathcal I_{q,q'}=H_q\cap H_{q'},                       \tag{5.1}
\]

and

\[
 \mathcal G_{q,q'}=
 \{s\in\mathcal I_{q,q'}:
 E(s+q)\cap E(s+q')\ne\varnothing\}.                    \tag{5.2}
\]

Thus `J=|I|` and `A=|G|`.  To count `W_0`, choose its first source `s` in
`G` and its distinct second source `s'` arbitrarily in `I`; this gives
`A(J-1)`.  To count `I`, both ordered sources must lie in `G`; this gives
`A(A-1)`.  Summing over fibre pairs proves the first two identities in
(1.7), and the third follows by subtraction.

There is additional rigidity in `G`.  If

\[
 E(s+q)=\{x,a\},\qquad E(s+q')=\{x,b\},                  \tag{5.3}
\]

then

\[
 a-b=q-q'.                                                \tag{5.4}
\]

The ordered endpoints `(a,b)` are uniquely determined by `q-q'`, so every
good start for this fibre pair has the form

\[
 s=x+a-q=x+b-q'                                          \tag{5.5}
\]

with fixed `a,b` and varying `x`.  Hence `A(q,q')<=k-2`.

## 6. Weighted switch and the scalar specialization

Let `V(p)>=0` be any weight on ordered source pairs.  Expanding the left
side fibre pair by fibre pair shows the exact identity

\[
\boxed{
 \sum_p V(p)O(p)
 =\sum_{q<q'}
   \sum_{\substack{s\in\mathcal G_{q,q'}\\
                   t\in\mathcal I_{q,q'}\setminus
                         \mathcal G_{q,q'}}}
       \bigl(V(s,t)+V(t,s)\bigr).}                        \tag{6.1}
\]

No clean-translation weight has been replaced by a maximum in (6.1).

For the endpoint-rich scalar problem, take

\[
 V(s,s')=W_{r(s,s'),L},\qquad
 r(s,s')=-{\delta(s)-\delta(s')\over18},                 \tag{6.2}
\]

with weight zero unless the quotient is integral and the target gap is
realized.  Here `W_(r,L)` is the determinant-qualified target endpoint
wedge count from the previous endpoint-rich theorem.  The weighted mass in
question is

\[
 Z_L=\sum_p c(p)V(p)=\sum_r C_*(r)W_{r,L}.               \tag{6.3}
\]

For a dyadic source-codegree block `c(p)>=K>=k`, (1.5) and (6.1) prove

\[
\boxed{
 \sum_{\substack{p:c(p)\ge K\\
                  \rho(p)<c(p)/\sqrt{k}}}
 c(p)V(p)
 \le {k\over K}
 \sum_{\substack{p:c(p)\ge K\\
                  \rho(p)<c(p)/\sqrt{k}}}V(p)O(p).}      \tag{6.4}
\]

The right side is the mixed double-wedge count displayed explicitly by
(6.1).  Since `k/K<=1`, the common-translation weight has been eliminated
on this branch without losing a factor of `H_*`.

The replacement branch has a parallel exact weighted switch.  Since
`c(p)<=sqrt(k)rho(p)` there,

\[
\begin{aligned}
 \sum_{p\text{ replacement}}c(p)V(p)
 &\le\sqrt{k}\sum_p\rho(p)V(p)\\
 &=\sqrt{k}\sum_q
   \sum_{\substack{s,s'\in H_q,\ s\ne s'\\
          E(s+q)\cap E(s'+q)\ne\varnothing}}
       V(s,s').                                          \tag{6.5}
\end{aligned}
\]

Thus the high-codegree weighted wedge mass is reduced to exactly two
endpoint-decorated quantities: the mixed two-fibre mass in (6.1) and the
single-fibre replacement-wedge mass in (6.5).  Both preserve `q` and the
full scalar/determinant weight.

This is the strongest current reduction of the dense weighted wedge mass.
To finish it one must prove global bounds for the right sides of (6.1) and
(6.5), using their fixed-outer-edge and nested-fibre decorations.  The
low-codegree band `c(p)<k` also remains outside this dichotomy.

## 7. Exact stress and warning

The companion verifier checks (1.2), (1.3), (1.7), the pencil bound, the
nested-fibre/endpoint-degeneracy classification, and the fully weighted
identity (6.1) on closure, Costas, transformed-parabola, and ruler stresses.

On the full 43-point transformed parabola, restricted to scalar-aligned
source pairs, it finds

\[
\begin{array}{c|r}
\text{aligned source pairs}&39260\\
\text{pairs with }c(p)\ge43&7972\\
\text{replacement branch}&4192\\
\text{one-role wedge branch}&3780\\
\max c(p)&86\\
\max\rho(p)&26\\
\sum O(p)\text{ on the high block}&2053352.
\end{array}                                               \tag{7.1}
\]

For the untruncated scalar wedge weight, the high-codegree nonreplacement
mass is `36380`, while its mixed double-wedge charge is `193521`, exactly
consistent with (6.4).  The replacement branch still carries scalar mass
`41306`; its weighted replacement-record charge in (6.5) is `10798`, so
`41306<sqrt(43)*10798` as predicted.  It is quantitatively real and cannot
be omitted.

The warning is therefore sharp.  Endpoint switching has removed the crude
per-gap `C_*(r)<=H_*` loss on a large, explicitly characterized branch, but
it has not supplied a global estimate for the mixed double-wedge mass.
Treating (6.1) as automatically `O(Nk^3)` would simply rename the remaining
problem.
