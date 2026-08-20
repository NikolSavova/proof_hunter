# A shared-head clean-fibre intersection switch

## 1. Outcome

Let `A` be a `k`-point distance-Sidon set.  For a pair sum `s`, write
`E(s)` for its unique endpoint edge.  Let

\[
 q_1=a-b,\qquad q_2=a-c,\qquad g=c-b,                    \tag{1.1}
\]

where `a,b,c` are distinct points of `A`.  Put

\[
 J(a;b,c)=|H_{a-b}\cap H_{a-c}|.                         \tag{1.2}
\]

The proposed intersection lemma is valid, with a better error term:

\[
 \boxed{
 J(a;b,c)\le h_{c-b}+\left\lfloor{k-3\over2}\right\rfloor.}
                                                                  \tag{1.3}
\]

More precisely, for `s` in the intersection and `t=s+q_2`, exactly one of
the following holds.

1. `t in H_g`.
2. For one point `e`,
   \[
    E(t)=\{e,b\},\qquad E(t+g)=\{e,c\}.                  \tag{1.4}
   \]

The exceptional source edges `E(s)` form a matching outside `{a,b,c}`,
which proves (1.3).  In particular the requested weaker estimate
`J<=h_g+k` follows.

There is also a global switch with no polynomial error.  Let

\[
 H=\sum_qh_q.                                             \tag{1.5}
\]

Then

\[
 \boxed{
 \sum_{\substack{a,b,c\in A\\\text{distinct}}}J(a;b,c)
 \le(k-4)H.}                                             \tag{1.6}
\]

The exceptional part of the left side is **exactly** `2H`; the
nonexceptional switch is at most `(k-6)`-to-one.  If

\[
 d_a(s)=|\{b\ne a:s\in H_{a-b}\}|,                       \tag{1.7}
\]

then (1.6) is equivalently the useful shared-head incidence bound

\[
 \boxed{
 \sum_{a,s}d_a(s)^2\le(k-3)H.}                           \tag{1.8}
\]

This is sharp in its endpoint count: a clean record uses six points, its
two target endpoints give the two unavoidable exceptional switches, and a
nonexceptional output leaves only `k-6` possible new heads.

The strongest immediate reciprocal consequence is

\[
 \boxed{
 \sum_{\substack{a,b,c\in A\\\mathrm{distinct}}}
 {J(a;b,c)^2\over
  h_{c-b}+\lfloor(k-3)/2\rfloor}
 \le(k-4)H.}                                             \tag{1.9}
\]

It yields a rigorous `1/T` tail for high common-translation source
codegrees in Section 5.  This is genuine progress toward the weighted
reciprocal tail, but it does not by itself control pairs whose anchor graph
is matching-like or the raw target squared-distance richness.

## 2. Proof of the local switch

Take

\[
 s\in H_{q_1}\cap H_{q_2},\qquad t=s+q_2.                \tag{2.1}
\]

Both pair sums

\[
 t=s+a-c,qquad t+g=s+a-b                               \tag{2.2}
\]

are realized.  Membership in `H_{a-c}` says that `E(t)` is disjoint from
`a,c` and from `E(s)`.  Membership in `H_{a-b}` says that `E(t+g)` is
disjoint from `a,b` and from `E(s)`.

To have `t in H_g`, the two edges in (2.2) must additionally be disjoint
from the anchors `c,b` and from one another.  Suppose one of these
conditions fails.

* If `b in E(t)`, write `E(t)={e,b}`.  Then
  \[
   t+g=e+b+c-b=e+c.
  \]
  Pair-sum injectivity gives `E(t+g)={e,c}`.
* The case `c in E(t+g)` is symmetric.
* Otherwise the two edges meet, say
  \[
   E(t)=\{e,x\},\qquad E(t+g)=\{e,y\}.
  \]
  Their pair-sum difference gives
  \[
   y-x=c-b.                                               \tag{2.3}
  \]
  A distance-Sidon set is vector-Sidon, so a nonzero directed difference
  has a unique ordered endpoint representation.  Equation (2.3) forces
  `(y,x)=(c,b)`.

Every possible cleanliness failure therefore has exactly the form (1.4).
Conversely, (1.4) plainly prevents membership in `H_g`.  This proves the
dichotomy, including all orientations.

## 3. The exceptional set is a matching

Fix `(a,b,c)`, and let exceptional starts `s_i` have outer endpoints `e_i`
as in (1.4).  From `s_i+a-b=e_i+c`,

\[
 s_i=e_i+b+c-a.                                           \tag{3.1}
\]

The `e_i` are distinct because pair sums are unique.  Suppose two source
edges `E(s_i),E(s_j)` meet at `x`; write their other endpoints as `y,z`.
Subtracting their pair sums in (3.1) gives

\[
 y-z=e_i-e_j.                                             \tag{3.2}
\]

Vector-Sidonicity forces `(y,z)=(e_i,e_j)`.  But `E(s_i)` is disjoint from
its `H_{a-b}` target edge `{e_i,c}`, a contradiction.  Thus the source
edges belonging to distinct exceptions are pairwise disjoint.

Every such source edge avoids `a,b,c` by the two original clean
conditions.  Hence there are at most

\[
 \left\lfloor{k-3\over2}\right\rfloor                  \tag{3.3}
\]

exceptions.  The nonexceptional map `s -> t=s+a-c` is injective into
`H_{c-b}`, proving (1.3).

## 4. Exact global switching

Let `X` be the set of ordered quadruples `(a,b,c,s)` with distinct
`a,b,c`, with `s in H_(a-b) intersect H_(a-c)`, which are exceptional.
There is an exact bijection

\[
 \boxed{
 X\longleftrightarrow
 \{(a,b,s,x):s\in H_{a-b},\ x\in E(s+a-b)\}.}            \tag{4.1}
\]

Indeed, if `E(s+a-b)={c,e}`, choosing `c` gives

\[
 s+a-c=e+b,                                              \tag{4.2}
\]

so `s in H_(a-c)` and the switch is exceptional.  Choosing `e` gives the
second exception.  All six endpoints are distinct by the original clean
record.  Conversely (1.4) recovers exactly such a target endpoint choice.
Therefore

\[
 \boxed{|X|=2H.}                                         \tag{4.3}
\]

For a nonexceptional quadruple, map

\[
 (a,b,c,s)\longmapsto(c,b,t),\qquad t=s+a-c\in H_{c-b}.  \tag{4.4}
\]

Fix an output `(c,b,t)`.  Since `t in H_(c-b)`, the two edges
`E(t),E(t+c-b)` and the anchors `c,b` are six distinct points.  Any
preimage head `a` must avoid all six: it is distinct from `b,c`, it is
disjoint from `E(t)` by cleanliness in `H_(a-c)`, and disjoint from
`E(t+c-b)` by cleanliness in `H_(a-b)`.  Once `a` is chosen,
`s=t-a+c` is fixed.  Thus (4.4) is at most `(k-6)`-to-one.

The nonexceptional mass is at most `(k-6)H`; adding (4.3) proves (1.6).

There is a weighted form.  For any nonnegative weights `w_(c,b,t)`,

\[
 \sum_{\rm nonexceptional}w_{c,b,t}
 \le(k-6)\sum_{c\ne b}\sum_{t\in H_{c-b}}w_{c,b,t}.      \tag{4.5}
\]

For arbitrary weights `W(a,b,c,s)`, the exceptional term has the exact
endpoint expansion

\[
 \sum_{\rm exceptional}W(a,b,c,s)
 =\sum_{a\ne b}\sum_{s\in H_{a-b}}
   \sum_{c\in E(s+a-b)}W(a,b,c,s).                       \tag{4.6}
\]

Equations (4.5)--(4.6), rather than a maximum-fibre estimate, are the
strongest weighted form of the switch.

Finally, summing (1.7) over all incidences gives

\[
 \sum_{a,s}d_a(s)=H,qquad
 \sum_{a,s}d_a(s)(d_a(s)-1)=\sum_{a,b,c}J(a;b,c).        \tag{4.7}
\]

Equations (1.6) and (4.7) prove (1.8).  The pointwise estimate (1.3),
followed by (1.6), proves (1.9).

## 5. A reciprocal source-codegree tail

For an ordered pair `p=(s,s')` of distinct source pair sums, put

\[
 Q_p=\{q:s,s'\in H_q\},\qquad c(p)=|Q_p|.                \tag{5.1}
\]

Represent every `q in Q_p` by its unique ordered anchor edge `a -> b`.
Let `d_a(p)` be the outdegree of `a` in this anchor graph and put

\[
 W_{\rm head}(p)=\sum_a\binom{d_a(p)}2.                  \tag{5.2}
\]

Switching the order of summation gives the exact identity

\[
 \boxed{
 \sum_pW_{\rm head}(p)
 =\frac12\sum_{\substack{a,b,c\in A\\\mathrm{distinct}}}
       J(a;b,c)(J(a;b,c)-1).}                            \tag{5.3}
\]

Write

\[
 H_2=\sum_gh_g^2,qquad r_0=\left\lfloor{k-3\over2}\right\rfloor.
                                                                    \tag{5.4}
\]

The nonexceptional switch (4.4), the exact exceptional mass `2H`, and
`h_g<=N=binom(k,2)` imply

\[
\begin{aligned}
 R_{\rm head}
 &:=(k-6)(H_2+r_0H)+2(N+r_0)H,\tag{5.5}\\
 \sum_{a,b,c}J(a;b,c)^2&\le R_{\rm head},\tag{5.6}\\
 \sum_pW_{\rm head}(p)&\le {R_{\rm head}\over2}.        \tag{5.7}
\end{aligned}

For completeness, (5.6) follows by multiplying every `J` by its
pointwise upper bound `h_g+r_0`.  Nonexceptional records of tail `g` have
total multiplicity at most `(k-6)h_g`, while all exceptional records have
total multiplicity `2H` and weight at most `N+r_0`.

Cauchy--Schwarz on the anchor outdegrees gives

\[
 W_{\rm head}(p)
 \ge {c(p)(c(p)-k)\over2k}.                               \tag{5.8}
\]

Thus, for every `T>=2k` and even after imposing any additional predicate
on `p`,

\[
 \boxed{
 \sum_{p:c(p)\ge T}c(p)
 \le {2kR_{\rm head}\over T}.}                           \tag{5.9}
\]

This is a genuine reciprocal `1/T` tail for the clean source codegree.
Using `H_2<=NH`, its crude form is

\[
 \sum_{p:c(p)\ge T}c(p)\ll {k^2NH\over T}.               \tag{5.10}
\]

The estimate applies in particular after selecting scalar-aligned source
pairs.  It does not yet prove the desired scalar reciprocal tail: (5.10)
is too large in the middle range, and it says nothing about large raw
target gap multiplicity attached to low-codegree `p`.  Its value is that
the formerly unstructured shared-head part of the high-codegree source
weight now has an exact endpoint switch and reciprocal moment.

## 6. Stress audit

The exact profiles below are

\[
 (k,H,\sum J,\text{nonexceptional},\text{exceptional},
   \max J,\sum d_a(s)^2,\sum J(J-1),\max_gE_g),           \tag{6.1}
\]

where `E_g` is the exceptional mass with tail difference `g`.

\[
\begin{array}{l|rrrrrrrrr}
\text{instance}&k&H&\sum J&\rm nonex&\rm ex&\max J&\sum d^2&\sum J(J-1)&\max E_g\\ \hline
\text{closure-20}&20&648&1296&0&1296&2&1944&240&15\\
\text{closure-40}&40&12420&32616&7776&24840&7&45036&24844&54\\
\text{Costas-22}&22&9342&36180&17496&18684&12&45522&145820&75\\
\text{parabola-43}&43&190278&1507104&1126548&380556&49&1697382&34799420&348\\
\text{ruler-40}&40&4914&11286&1458&9828&5&16200&7776&33
\end{array}                                               \tag{6.2}
\]

In every row the exceptional count is exactly `2H`; all local
orientations and both exceptional edge identities are checked directly.
The parabola has intersections of size 49, so this is not merely a
small-codegree phenomenon.

Run

```text
python3 phase2/loop/erdos1208/verify_shared_head_fibre_intersection.py
```

for the local dichotomy, exceptional matching, exact global bijection,
weighted multiplicities, reciprocal moment, head-degree identities, and
all profiles in (6.2).
