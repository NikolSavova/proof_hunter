# Synchronized clique mass: exact localization at one physical metric wedge

## 1. Outcome

The `ell=2` synchronized four-sum mass from
`HIGHER_POOLING_FOUR_SUM_PARALLELOGRAM_GATE.md` has an exact localization
which keeps **all four clean translations**, the ordered source pair, and
the determinant-qualified scalar wedge.

For an ordered source pair `p=(s,t)`, let `B_2(p)` be its unweighted
transverse-rich synchronized-pair load (defined precisely in Section 2),
and put

\[
 K_2(r)=\sum_{\substack{p:\ c(p)\ge k\\ r(p)=r}}B_2(p),
 \qquad
 r(p)=-{\delta(s)-\delta(t)\over18}.                    \tag{1.1}
\]

Then the live weighted pooled mass is exactly

\[
 \boxed{\mathfrak P_2(V)=\sum_rK_2(r)W_{r,L}.}          \tag{1.2}
\]

More importantly, if `w` ranges over the

\[
 k{k-1\choose2}=N(k-2)                                 \tag{1.3}
\]

physical endpoint wedges of the complete graph on `A`, there is an
explicit local charge `Phi_(2,L)(w)` such that

\[
 \boxed{\mathfrak P_2(V)=\sum_w\Phi_{2,L}(w).}          \tag{1.4}
\]

Consequently the following single-wedge theorem is sufficient for the
entire transverse-rich branch:

\[
 \boxed{\Phi_{2,L}(w)\le m^{o(1)}k^4\quad\hbox{for every }w.} \tag{1.5}
\]

Indeed (1.3)--(1.5) give
`mathfrak P_2(V)<=m^(o(1))N k^5`, exactly the target required by the
binomial amplification.  This is one power of `k` more permissive than the
failed low-band fixed-wedge gate, because a source synchronized pair itself
has four-translation complexity.

There is also an exact four-fibre switch for `K_2(r)`: every summand lies in
one ordered source pair inside a common intersection of four clean fibres.
Thus (1.4) is not a relaxation to distance-label energy; it is a literal
physical-wedge/four-clean-fibre incidence count.

No counterexample to (1.5) was found.  The polynomial-height 43-point
transformed parabola gives a serious finite stress: at determinant cutoff
`L=20`,

\[
 \max_w\Phi_{2,20}(w)=736977
   =9.269\ldots\,k^3=0.2155\ldots\,k^4.                \tag{1.6}
\]

Thus the unit-normalized cubic estimate is already false on the main
stress, while the quartic scale survives with limited room.  This finite
example does **not** refute an asymptotic $m^{o(1)}k^3$ theorem.  The
literal `c(p)=49>=48`, scalar-weighted rank-flat certificate has local
charge `27140=0.00511... k^4`, so it also does not refute (1.5).

## 2. The source synchronized-pair profile

For `p=(s,t)` write

\[
 Q_p=\{q:s,t\in H_q\},\qquad c(p)=|Q_p|.                \tag{2.1}
\]

For an unordered base pair `b={q_1,q_2} subset Q_p`, say that `b` is
**one-role** when the two target edges meet in exactly one of the two
source roles:

\[
 \begin{aligned}
 &E(s+q_1)\cap E(s+q_2)\ne\varnothing,\qquad
 E(t+q_1)\cap E(t+q_2)=\varnothing,                    \tag{2.2}
 \end{aligned}
\]

or with `s,t` exchanged.  Relative to this base, let `T_p(b)` be the
number of translations `q_0 in Q_p` whose anchor edge is disjoint from
both base anchor edges and whose two target edges are disjoint from the
corresponding unions of base target endpoints.  This is exactly the
fully transverse definition in the amplified local dichotomy.

Define

\[
 \boxed{
 B_2(p)=\sum_{\substack{b\in {Q_p\choose2}\ \operatorname{one-role}\\
                   T_p(b)\ge c(p)/2}}
             {T_p(b)\choose2}.}                         \tag{2.3}
\]

Swapping `s,t` merely swaps the good and bad target roles, so

\[
 B_2(s,t)=B_2(t,s).                                     \tag{2.4}
\]

The pooled mass as defined with the symmetric weight
`V(p)+V(p^op)` is therefore equivalently

\[
 \mathfrak P_2(V)
 =\sum_{p\ \operatorname{ordered}}B_2(p)V(p).          \tag{2.5}
\]

For the scalar specialization `V(p)=W_(r(p),L)`, grouping (2.5) by
`r(p)` proves (1.2).  This elementary grouping is useful because `K_2`
still contains the whole synchronized clean system, instead of replacing
it by the much larger raw squared-distance-gap multiplicity.

## 3. Exact fixed-wedge formula

Fix a physical wedge

\[
 w=(x;\{x,a_1\},\{x,a_2\}).                             \tag{3.1}
\]

Canonically order its two first edges, write their squared norms as
`A_1,A_2`, and their canonical displacement vectors as `v_1,v_2`.  Let
`P_L(w)` be the set of ordered partner pairs `(f_1,f_2)`, ordered according
to the first edges, for which

\[
 \begin{aligned}
 A_1-\delta(f_1)&=A_2-\delta(f_2)=:r,\\
 |2\det(v_1,u_1)|&>L,\qquad |2\det(v_2,u_2)|>L,         \tag{3.2}
 \end{aligned}
\]

where `u_i` is the canonical displacement of `f_i`.  Put

\[
 \boxed{
 \Phi_{2,L}(w)=
   \sum_{(f_1,f_2)\in\mathcal P_L(w)}
       K_2\bigl(A_1-\delta(f_1)\bigr).}                 \tag{3.3}
\]

For a fixed `w`, the map `(f_1,f_2)->r` is injective: the value of `r`
fixes both partner norms, and distinct-distance Sidonicity fixes each
partner edge.  Thus (3.3) is a restriction sum of `K_2`, with no hidden
partner multiplicity.

Equivalently, if `g=A_1-A_2` and `D_g` is the set of first distance labels
`C` in determinant-qualified representations `(C,C-g)`, then

\[
 S_L(w)\subseteq A_1-D_g,
 \qquad
 \Phi_{2,L}(w)=\sum_{r\in S_L(w)}K_2(r).                \tag{3.4}
\]

The containment rather than equality only records the two cross-
determinant tests against the fixed first-edge vectors.

To prove (1.4), fix `r`.  The first edges of the determinant-qualified
records at scalar shift `r` form a simple graph on `A`; its endpoint
wedges are counted by `W_(r,L)`.  Each such graph wedge is one physical
`w` and its two unique partner edges satisfy (3.2).  Conversely (3.2)
gives exactly one graph wedge at `r`.  Hence

\[
 W_{r,L}=\#\{w:r\in S_L(w)\},                           \tag{3.5}
\]

where `S_L(w)` is the set of shifts occurring in (3.2).  Multiplying by
`K_2(r)` and switching the two finite sums proves

\[
 \sum_rK_2(r)W_{r,L}
 =\sum_w\sum_{r\in S_L(w)}K_2(r)
 =\sum_w\Phi_{2,L}(w).                                 \tag{3.6}
\]

## 4. Four-clean-fibre switch

Expanding the binomial coefficient in (2.3) gives an endpoint-preserving
description of `K_2`.  For a base `b={q_1,q_2}` and a pool
`a={q_0,q'_0}`, let `X_p(b,a)` be the indicator that

1. `q_1,q_2` are one-role for `(s,t)`;
2. `T_p(b)>=c(p)/2`; and
3. both `q_0,q'_0` are transverse to the base.

Then

\[
\boxed{
 K_2(r)=
 \sum_{\{q_1,q_2\}}
 \sum_{\{q_0,q'_0\}}
 \sum_{\substack{s\ne t\in
       H_{q_1}\cap H_{q_2}\cap H_{q_0}\cap H_{q'_0}\\
       c(s,t)\ge k,\ r(s,t)=r}}
 X_{(s,t)}(\{q_1,q_2\},\{q_0,q'_0\}).}               \tag{4.1}
\]

The two translation pairs in (4.1) are unordered, and transversality makes
them disjoint automatically.  Equation (4.1) is just a switch of the four
finite choices in (2.3), so it has no multiplicity loss.  Combining (4.1)
and (3.3) exhibits the local charge in (1.5) as one physical metric wedge
coupled to an ordered source pair in four simultaneous clean fibres.

This is the durable positive reduction: any closure, divisor, or endpoint
support argument can now be aimed at a fixed `w` while retaining four
clean translations.  A bound for raw distance gaps alone discards exactly
the information exposed by (4.1).

There is a sharp reciprocal-tail formulation.  For dyadic `Lambda>=1`, put

\[
 n_w(\Lambda)=
 \#\{r\in S_L(w):\Lambda\le K_2(r)<2\Lambda\}.          \tag{4.2}
\]

The local estimates

\[
 \boxed{
 n_w(\Lambda)\le {m^{o(1)}k^4\over\Lambda}
 \quad\hbox{for every }w,\Lambda}                      \tag{4.3}
\]

imply (1.5), up to the harmless `O(log m)=m^(o(1))` number of
dyadic levels.  Unlike a maximum bound for `K_2` or a support bound for
`S_L(w)`, (4.3) has exactly the reciprocal weighting needed by (3.3).

## 5. What elementary bounds lose

Let `O(p)` be the number of one-role base pairs.  Since a `c(p)`-edge
simple target graph has at most `(k-2)c(p)` endpoint wedges,

\[
 O(p)\le2(k-2)c(p).                                     \tag{5.1}
\]

Consequently

\[
 B_2(p)\le {c(p)\choose2}O(p)<(k-2)c(p)^3.             \tag{5.2}
\]

This does not prove (1.5): at the live threshold `c(p)\asymp k`, a single
source pair may already cost the full `k^4` local budget, while a fixed
metric wedge can support many distinct scalar shifts.  Likewise Cauchy on
(3.3) only gives

\[
 \Phi_{2,L}(w)
 \le |S_L(w)|^{1/2}
      \left(\sum_{r\in S_L(w)}K_2(r)^2\right)^{1/2},    \tag{5.3}
\]

and the low-band rich-pencil barrier shows that `|S_L(w)|` itself can be
quadratic.  Thus the missing estimate must couple the four-fibre profile
`K_2(r)` to the particular radial-difference set `S_L(w)`; separate
maxima reproduce the old scalar-correlation loss.

The exact one-role profile gives one further useful, but still insufficient,
upper switch.  If `O(p)` is the number in (5.1), then

\[
 K_2(r)
 \le\sum_{p:r(p)=r}{c(p)\choose2}O(p).                  \tag{5.4}
\]

On a dyadic source-codegree block `K<=c(p)<2K`, this becomes

\[
 K_{2,K}(r)<2K^2 O_K(r),
 \qquad
 O_K(r)=\sum_{\substack{p:r(p)=r\\K\le c(p)<2K}}O(p). \tag{5.5}
\]

Thus the threshold block `K\asymp k` would follow from the fixed-wedge
correlation
`\(\sum_{r\in S_L(w)}O_K(r)\le m^{o(1)}k^2\)`.
This is stronger than the known global switch for `sum_p O(p)V(p)` and is
not asserted here; (5.5) identifies exactly where the two extra pool
choices have gone.

## 6. Exact stresses and remaining gate

At `k=43`, the transformed-parabola verifier finds

\[
\begin{array}{c|r}
\text{ordered scalar-aligned pairs with }c(p)\ge k&7972\\
\text{one-role bases}&2053352\\
\text{transverse-rich bases}&1116236\\
|\operatorname{supp}K_2|&7270\\
\sum_rK_2(r)&547712688\\
\max_rK_2(r)&657408\\
\mathfrak P_2(W_{\cdot,20})&94435636\\
\max_w\Phi_{2,20}(w)&736977.
\end{array}                                             \tag{6.1}
\]

The exact identity (1.4) is checked independently by summing the 43-point
fixed-wedge charges.  The resulting total is only
`0.000711... N k^5`; the maximum local load is the more informative
stress and gives (1.6).

The maximizing physical wedge in fact sees only two scalar shifts, with
loads `149756` and `587221`.  Hence this stress is not caused by a broad
radial support: it shows that a **single fixed squared-distance gap can
already carry a substantial fraction of the quartic synchronized-clique
budget**.  In particular, any cubic intermediate theorem needs a constant
at least 8.26 on this finite family.  This is an adversarial warning, not
an asymptotic counterexample to $K_2(r)\le m^{o(1)}k^3$.

On the 48-point rank-flat certificate, the planted ordered pair has 183
one-role bases, 77 transverse-rich bases, and

\[
 B_2(p)=27140.                                          \tag{6.2}
\]

The two scalar orientations are supported on two determinant-qualified
physical wedges, one per orientation.  Hence the planted pooled mass is
`54280` and each fixed wedge has charge `27140`.

The precise surviving theorem is (1.5), or an aggregate substitute for it.
No bounded-pool equal-area extraction is used here.  A proof should exploit
the four-fibre intersection in (4.1) together with the fixed partner-label
correlation in (3.2); neither ingredient alone has the required exponent.

## 7. Verification

Run

```bash
python phase2/loop/erdos1208/verify_synchronized_clique_fixed_metric_wedge_localization.py
```

The verifier checks the source profile, determinant-qualified metric-wedge
localization, exact total equality, all stated 43-point values, the planted
rank-flat values, the injectivity in (3.3), and the elementary inequalities
(5.1)--(5.3).
