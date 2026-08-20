# The lossless actual-codegree normalized three-translation switch

## 1. Outcome

The failed synchronized-pooling route used the ambient lower cutoff `k`
to pay for a source pair which could have actual common-clean codegree
`c(p)>>k`.  There is a lossless replacement: average the third translation
with weight `1/c(p)`.

For every nonnegative scalar weight `V`, the high-codegree one-role mass
has an exact decomposition

\[
 \boxed{
 D_{\rm one}^{\ge k}(V)
 =\mathfrak N_{\rm tr}(V)+
   \sum_{j=1}^{15}\mathfrak N_j(V).}                  \tag{1.1}
\]

Here every term retains the ordered source pair, the one-role base, and a
literal third clean translation.  `mathfrak N_tr` is fully transverse;
the other fifteen terms use a **disjoint canonical assignment** to the
first local endpoint channel which occurs.  No factor `c(p)/k` is lost.

On the transverse-rich branch,

\[
 \boxed{D_{\rm one,tr}^{\ge k}(V)
        \le2\mathfrak N_{\rm tr}(V).}                 \tag{1.2}
\]

There are two different actual-codegree normalizations for higher pools,
and they must not be conflated.  The coefficient `c(p)^(1-ell)` normalizes
an `ell`-pool only back to the **pre-normalized, once-amplified** mass
`sum_C T(C)w(C)`.  The lossless outer `1/c(p)` in (1.1) requires one
additional reciprocal factor.  The terminal fixed-`ell` mass is

\[
 \boxed{
 \mathfrak P_\ell^{\rm out}(V)
 =\sum_C c(p_C)^{-\ell}{T(C)\choose\ell}w(C).}        \tag{1.3}
\]

On `T(C)>=c(p_C)/2`, (1.3) is within constants depending only on `ell` of
the outer-normalized mass `sum_C(T(C)/c(p_C))w(C)`.  Its live global scale
is `Nk^3`.  The large-star construction in
`ACTUAL_CODEGREE_NORMALIZED_LARGE_STAR_BARRIER.md` proves that the
pre-normalized `c^(1-ell)` mass can be `Theta(k^7)>Nk^4`, while (1.3)
remains sharply `Theta(Nk^3)`.

## 2. Canonical local-channel partition

Let `C` be a one-role base record with ordered source pair
`p_C=(s,t)`, base translations `q_1,q_2`, common-translation set

\[
 Q_p=\{q:s,t\in H_q\},\qquad c(p)=|Q_p|,              \tag{2.1}
\]

and symmetric scalar weight

\[
 w(C)=V(p_C)+V(p_C^{\rm op}).                         \tag{2.2}
\]

Orient the target roles so that the `s`-edges of `q_1,q_2` meet and the
`t`-edges are disjoint.  Write the ordered anchor of `q_i` as `(a_i,b_i)`.
For a third translation `q_0`, with anchor `(a_0,b_0)`, use the following
fixed priority list of fifteen predicates:

1. `a_0=a_1`, `a_0=a_2`, `b_0=b_1`, `b_0=b_2`;
2. `a_0=b_1`, `a_0=b_2`, `b_0=a_1`, `b_0=a_2`;
3. the three predicates that its good target edge contains a specified
   endpoint of the three-point good base union; and
4. the four analogous predicates for the four-point bad base union.

Let `chi_j(C,q_0)` be one precisely when predicate `j` holds and every
earlier predicate fails.  Let `tau(C,q_0)` be one when none holds.  Then
the partition is pointwise:

\[
 \boxed{
 \tau(C,q_0)+\sum_{j=1}^{15}\chi_j(C,q_0)=1.}         \tag{2.3}
\]

In particular, unlike the raw channel loads, the canonical local loads do
not overlap.

Define

\[
\begin{aligned}
 \mathfrak N_{\rm tr}(V)
 &=\sum_{C:c(p_C)\ge k}{w(C)\over c(p_C)}
       \sum_{q_0\in Q_{p_C}}\tau(C,q_0),\\
 \mathfrak N_j(V)
 &=\sum_{C:c(p_C)\ge k}{w(C)\over c(p_C)}
       \sum_{q_0\in Q_{p_C}}\chi_j(C,q_0).
                                                               \tag{2.4}
\end{aligned}
\]

Summing (2.3) over `q_0 in Q_p` gives one exactly, after division by
`c(p)`.  Summing over bases proves (1.1).

This also gives a literal third-translation switch.  For example,

\[
 \boxed{
 \mathfrak N_{\rm tr}(V)
 =\sum_{q_0}
   \sum_{\substack{C:\ q_0\in Q_{p_C}\\c(p_C)\ge k}}
   {\tau(C,q_0)\over c(p_C)}w(C),}                    \tag{2.5}
\]

and the identical formula with `chi_j` holds for each local channel.  The
third translation is now outermost, but the common source pair and the
two base translations remain literal.  The reciprocal factor obeys the
fractional partition of unity

\[
 \sum_{q_0\in Q_p}{1\over c(p)}=1.                    \tag{2.6}
\]

Thus a source pair can be charged through many fibres without being paid
many times.

## 3. Exact rich-branch comparison

Write

\[
 T(C)=\sum_{q_0\in Q_{p_C}}\tau(C,q_0).               \tag{3.1}
\]

If `T(C)>=c(p_C)/2`, then

\[
 w(C)\le {2T(C)\over c(p_C)}w(C).                     \tag{3.2}
\]

Summing (3.2) proves (1.2).  Notice that this is stronger and more
faithful than inserting `T(C)>=k/2`: an ultra-high-codegree pair with
`c(p)=Theta(k^2)` still has normalized cost at most `w(C)`, not an
artificial extra factor `k`.

On a local-rich base, (1.1) keeps the entire mass with total normalized
local coefficient

\[
 {1\over c(p_C)}\sum_{j,q_0}\chi_j(C,q_0)\le1.       \tag{3.3}
\]

One may now attack each chosen endpoint channel after the outer switch
(2.5).  The former factor `30/k` is unnecessary at this stage; it arose
only from choosing one possibly overlapping heavy channel before
normalizing.

## 4. Pre-normalized versus outer-normalized synchronized pools

For a fixed `ell>=2`, first define the pre-normalized mass

\[
 \mathfrak P_\ell^{\rm pre}(V)
 =\sum_Cc(p_C)^{1-\ell}{T(C)\choose\ell}w(C).         \tag{4.1}
\]

Since
`T(C)<=c(p_C)`, one always has

\[
 c(p_C)^{1-\ell}{T(C)\choose\ell}
 \le {T(C)\over\ell!}.                                \tag{4.2}
\]

Conversely, if `c(p_C)>=4ell` and `T(C)>=c(p_C)/2`, then
`T(C)-ell+1>=c(p_C)/4`, so

\[
\begin{aligned}
 {T(C)\choose\ell}
 &\ge {T(C)\over\ell!}
       \left({c(p_C)\over4}\right)^{\ell-1},\\
 T(C)&\le \ell!4^{\ell-1}
 c(p_C)^{1-\ell}{T(C)\choose\ell}.                   \tag{4.3}
\end{aligned}
\]

Therefore

\[
 \ell!\,\mathfrak P_\ell^{\rm pre}(V)
 \le\sum_CT(C)w(C)
 \le\ell!4^{\ell-1}\mathfrak P_\ell^{\rm pre}(V).  \tag{4.4}
\]

Dividing the pointwise inequalities by `c(p_C)` gives the lossless outer
version (1.3):

\[
 \ell!\,\mathfrak P_\ell^{\rm out}(V)
 \le\sum_C{T(C)\over c(p_C)}w(C)
 \le\ell!4^{\ell-1}\mathfrak P_\ell^{\rm out}(V).  \tag{4.5}
\]

For `ell=2`, the sharper exact comparison is

\[
 {T(C)\over c(p_C)}
 \le {4c(p_C)\over c(p_C)-2}
 {1\over c(p_C)^2}{T(C)\choose2}.                    \tag{4.6}
\]

Thus outer-normalized pooling retains the synchronized four-sum identities
without increasing the analytic target.  The live sufficient estimate is

\[
 \mathfrak P_\ell^{\rm out}(W_{\cdot,L})
 \le m^{o(1)}Nk^3.                                    \tag{4.7}
\]

The analogous `Nk^4` estimate for `mathfrak P_ell^pre` is false.

## 5. Equality-model audit and exact remaining barrier

In the sharpened Golomb large-star construction,

\[
 c(p)=\Theta(n^2),\quad O(p)=\Theta(n^3),\quad
 T(C)=\Theta(n^2),\quad W_{r,N}=\Theta(n^2).          \tag{5.1}
\]

Consequently the three relevant selected-p masses are

\[
\begin{aligned}
 \mathfrak N_{\rm tr}(W)
  &\asymp n^3{n^2\over n^2}n^2=\Theta(n^5),\\
 \mathfrak P_\ell^{\rm pre}(W)
  &\asymp n^3(n^2)^{1-\ell}(n^2)^\ell n^2
    =\Theta(n^7),\\
 \mathfrak P_\ell^{\rm out}(W)
  &\asymp n^3(n^2)^{-\ell}(n^2)^\ell n^2
    =\Theta(n^5).                                     \tag{5.2}
\end{aligned}
\]

for every fixed `ell`.  The first and third exactly match
`Nk^3=Theta(n^5)`, while the second exceeds `Nk^4=Theta(n^6)` by a factor
`n`.  This is why the outer reciprocal factor cannot be postponed until
after a pre-normalized pool.

Normalization alone does not prove (4.7).  After the switch (2.5), a
crude estimate inside each `q_0` can still discard the common source pair
and the scalar weight, while a crude sum over source pairs simply uses
(2.6) and returns the original unpooled problem.  The exact survivor is:

> Bound the outer-`q_0` endpoint system in (2.5), retaining the reciprocal
> source-pair codegree, the one-role base, and `W_(r(p),L)` simultaneously.

A useful theorem must make the reciprocal factor interact with endpoint
reuse or with the fixed scalar; treating `1/c(p)` only as a number cannot
improve the equality model.  This is the sharp restart after the pooled
no-go.

## 6. Exact certificate

On the 102-point, six-wedge certificate, for the stored source pair and
test scalar weight `w=6`, the verifier obtains

\[
\begin{array}{c|r}
\text{quantity}&\text{value}\\ \hline
c(p),\ \#\text{ one-role bases}&320,\ 6,169\\
\sum_CT(C)&1,313,335\\
\sum_C(c(p)-T(C))&660,745\\
D_{\rm one}(w)&37,014\\
\mathfrak N_{\rm tr}(w)&788,001/32\\
\sum_j\mathfrak N_j(w)&396,447/32\\
\sum_C{T(C)\choose2}&139,373,896\\
\sum_CT(C)w(C)&7,880,010\\
\mathfrak P_2^{\rm pre}(w)&52,265,211/20.
\end{array}                                            \tag{6.1}
\]

The two normalized terms add exactly to `37,014`; all 660,745 local
records are assigned once among the fifteen channels.  The verifier also
checks the rich comparison (3.2), the pre-normalized pair comparison, and the
global distance/pair-sum-Sidon construction inherited from the multi-wedge
certificate.

Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_actual_codegree_normalized_three_translation_switch.py
```
