# Aggregate rooted circuits: exposed shields and the anti-aligned child

## Verdict

The rooted $1+3$ normal form and the three-arc carrier--root rectangle do
give a rigorous aggregate theorem, but only when the three-arc shield
actually carries the entropy of the cores.

Let $D=2^L$.  Suppose $M$ distinct rank-at-most-$q$ cores are
recoverable, with fibre at most $K$, from subsets of one ordinary convex
shield $O$ of size $s$.  Then

\[
 M\le K\sum_{i=0}^q {s\choose i}.                         \tag{1}
\]

If

\[
 \log M\ge aL^2,\qquad q\le\kappa L,\qquad
 \log K=o(L^2),                                           \tag{2}
\]

then

\[
 s\ge D^{a/\kappa-o(1)},\qquad
 V(P)\ge2^s\ge D^tM                                      \tag{3}
\]

for every fixed $t$ and all sufficiently large $D$.  Thus
$2^{o(L^2)}$ thinning does not defeat an exposed three-arc shield.  In
particular, quadratic core entropy cannot live only in the carrier and root
labels of Proposition 4 in `EXTERNAL_ALPHABET_ENERGY_TRICHOTOMY.md`.

The exact residual is therefore narrower: after the carrier/root trace is
fixed, a retained core child outside the convex outer shield still has
$2^{\Theta(L^2)}$ conditional states.  An absolute shield bank is then
indeed insufficient.

For that residual, separated composition does **not** automatically close
the coefficient-$1/2$ problem.  If a projectively arbitrary mark child
$Z$ is substituted between $k_-$ left and $k_+$ right singleton
vertices of a convex macro, the exact nonempty-face count is

\[
\begin{aligned}
 W(P)={}&2^{k_-+k_+}-1+W(Z)\\
 &+(2^{k_-}-1)U(Z)+(2^{k_+}-1)C(Z)\\
 &+|Z|(2^{k_-}-1)(2^{k_+}-1).                    \tag{4}
\end{aligned}
\]

Here $C,U$ are the two directed cap/cup profile counts.  The two genuine
mixed banks are $2^{k_-}U$ and $2^{k_+}C$.  Their product is at least
$2^{k_-+k_+}W(Z)$, by $C(Z)U(Z)\ge W(Z)$, but taking the larger bank
only gives the geometric mean.  Writing

\[
 \sigma(Z)=\tfrac12\log(U(Z)/C(Z)),                       \tag{5}
\]

Put $K_0=k_-+k_+$.  When it lies in the interval $[-K_0,K_0]$, the split

\[
 k_--k_+=\log C(Z)-\log U(Z)=-2\sigma(Z)                  \tag{6}
\]

equalizes the two mixed exponents at

\[
 \tfrac12\bigl(k_-+k_++\log C(Z)+\log U(Z)\bigr).         \tag{7}
\]

Integer rounding changes this by at most one; outside the interval the
best split is an endpoint.  When $CU$ is close to $W$, (7) is only the
average of the logarithmic
outer and child banks, never larger than their maximum.  A
$2^{o(L^2)}$ thinning leaves a $\Theta(L^2)$ skew unchanged.  This is the
exact anti-alignment not covered merely by recognizing a separated
composition.  The common-skew theorem in `agent_upper_jump/REPORT.md`
closes it only when a macroscopic family of comparable child blocks is
available.  After trace localization there can be just one hidden core
child and one mark child, so such a common-skew core is not automatic.

Finally, a scalable planar full-ACP tensor shows that no linear summation
of the local rooted half-plane shields can replace this missing profile
theorem.  It has both mark alphabets large, every common-core rectangle bad,
uniform cores, and selected mass $\Theta(V(P))$.  Its parameters are outside
the hard normalization $q=O(\log D)$, so it is a barrier to the proposed
charging interface, not an EIC' counterexample.

Exact verifier:

    python3 phase2/loop/erdos838/agent_one_sided_reflection/verify_aggregate_circuit_shield.py

## 1. Exposed-support theorem

> **Theorem 1 (quadratic entropy cannot hide in a low-rank convex
> shield).**  Let $\mathcal R$ be $M$ distinct sets of rank at most
> $q$.  Suppose every $R\in\mathcal R$ has a code
> $\phi(R)\subseteq O$, $|\phi(R)|\le q$, and every code has at most
> $K$ preimages.  If $O$ is in convex position, then (1) holds.  Under
> (2), (3) follows.

**Proof.**  There are only $\sum_{i\le q}{s\choose i}$ possible codes,
which proves (1).  If $s\ge q$, the standard binomial estimate gives

\[
 \sum_{i=0}^q{s\choose i}\le (es/q)^q.                    \tag{8}
\]

Equations (1)--(2) imply

\[
 \log(es/q)\ge (a/\kappa-o(1))L,                          \tag{9}
\]

and hence the first part of (3).  The case $s<q$ cannot occur
asymptotically, since then the right side of (1) has logarithm only
$O(L)+o(L^2)$.  Every subset of $O$ is an ordinary face, so
$\log V(P)\ge s$.  The right side of this inequality is exponential in
$L$, whereas $\log(D^tM)=O(L^2)$.  This proves the second part of (3).
QED.

The same proof permits a trace of rank $cq$, or a polynomial number of
trace colours: these only change $\kappa$ or contribute to $K$.  It also
survives discarding a $2^{o(L^2)}$ fraction of the cores.

In the three-arc carrier--root model, $O=L\cup R\cup\bigcup W$ is exactly
such a convex shield.  Therefore the model is fully discharged whenever a
core is decoded, up to subquadratic multiplicity, from its carrier/root
trace in $O$.  Any genuine residue must have quadratic conditional
entropy after that trace has been revealed.  Calling the same outer shield
once per hidden state is not a valid charge.

## 2. Exact one-child composition formula

Take a convex macro in increasing horizontal order.  Replace one macro
vertex by an arbitrary general-position child $Z$, leaving $k_-$
singleton positions to its left and $k_+$ to its right.  Make the
substitution sufficiently separated.

Faces fall into five disjoint classes.

1. No point of $Z$: $2^{k_-+k_+}-1$ choices.
2. No singleton position: $W(Z)$ choices.
3. Singleton positions only on the left: the trace in $Z$ is a cup,
   giving $(2^{k_-}-1)U(Z)$.
4. Singleton positions only on the right: the trace in $Z$ is a cap,
   giving $(2^{k_+}-1)C(Z)$.
5. Nonempty singleton traces on both sides: $Z$ is an internal macro
   block, so exactly one of its $|Z|$ labels is used.  This gives
   $|Z|(2^{k_-}-1)(2^{k_+}-1)$.

This proves (4).  It is the one-child specialization of the exact coloured
recurrence in `agent_upper_jump/REPORT.md`, but here no asymptotics or
homogeneity assumption is needed.

The full all-bad mark tensor is realized inside this model.  Use macro
points on a parabola with the substituted vertex between adjacent roots
$u,v$.  Theorem 1 of `DETACHED_RADIAL_LEXICOGRAPHIC_PROFILE.md` puts any
prescribed order type $Z$ in an arbitrarily small neighbourhood of that
vertex while making it totally nested behind $uv$.  Partition the nested
order into an inner alphabet $X$ followed by an outer alphabet $Y$.
For every subset $S$ of the other macro labels,

\[
 R_S=\{u,v\}\cup S,qquad
 \operatorname{ext}(R_S\cup\{x,p\})=R_S\cup\{p\}
 \quad(x\in X,p\in Y).                                  \tag{10}
\]

Thus all records and all bad rooted circuits persist, but their global
face count is governed by (4).  Recognizing the construction as separated
does not remove the profile skew in (5)--(7).

## 3. Scalable linear-mass regression

The preceding geometry also kills a stronger but tempting statement:

\[
 \sum_{\text{records }g}|\mathcal H_g|
       \le \operatorname{poly}(q)V(P),                    \tag{11}
\]

where $\mathcal H_g$ is the marked half-plane bank emitted by the rooted
circuit of $g$.

First take a fixed nested pair $x\prec p$, $K=2h$ outer macro
singletons, and the two roots nearest the missing macro position.  Every
subset of the remaining $K-2$ labels is a different core, so there are
$2^{K-2}$ actual records.  Formula (4), with a fixed two-point child,
gives $V(P)=\Theta(2^K)$; hence the selected mass is $\Theta(V(P))$.

The line $xp$ splits the free outer labels into two groups of size
$h-1$.  For a core choosing $\ell,r$ labels in the two groups, the
marked half-plane lemma emits at least

\[
                       2^{1+\max\{\ell,r\}}               \tag{12}
\]

faces.  Summing over all cores and using
$\max\{\ell,r\}\ge(\ell+r)/2$ gives

\[
 \sum_g|\mathcal H_g|
 \ge2(1+\sqrt2)^{K-2}.                                   \tag{13}
\]

The ratio of (13) to $V(P)$ grows like
$((1+\sqrt2)/2)^K$.  The same actual half-plane faces are reused by
exponentially many core states.  Pairing the shield output with the source
face still has the valid polynomial decoder, but that is a $V(P)^2$
bank, not the linear charge (11).

Both mark alphabets can be made large without changing the conclusion.
Take an even $m$, split a totally nested $m$-point child into
$|X|=|Y|=m/2$, and put $K=16m$ singleton macro positions around it.
Choose

\[
 M=\left\lfloor{2^{K-3}\over m}\right\rfloor             \tag{14}
\]

cores from the middle layer of the $K-2$ free outer labels.  This is
possible for all sufficiently large $m$.  All cores have one rank, every
pair $(x,p)$ has core degree $M$, and

\[
 |\mathcal E|=M{|X||Y|}=\Theta(m2^K).                     \tag{15}
\]

Since $C(Z),U(Z),W(Z)\le2^m$, formula (4) and $K=16m$ give

\[
                         V(P)=\Theta(m2^K).                \tag{16}
\]

Thus (15) is $\Theta(V(P))$, even though every common-core rectangle is
on the rooted-circuit branch and both mark alphabets grow.  Here the source
rank is $\Theta(K)=\Theta(m)$, not $O(\log m)$.  This last fact is
essential: the construction refutes a geometry-only rectangle-or-shield
inequality, but does not refute the rank-normalized EIC' statement.

It also does not refute the new shared-reservoir Hall formulation.  The
fifth term of (4) is an explicit common forward/two-ended bank: choose one
mark label and nonempty outer traces on both sides.  Its union has

\[
                  m(2^{K/2}-1)^2=\Theta(m2^K)             \tag{16a}
\]

distinct faces.  Once this already-proved bank is included in every
relevant $\mathcal B_g$, the all-record Hall ratio is $O(1)$.  Thus the
regression sharply kills summing the *occurrences* of local half-plane
banks, while shared-union charging handles it exactly as intended.

## 4. Exact remaining target

The combination of Theorem 1 and (4) leaves only the following aggregate
case.

* The carrier/root trace in every exposed three-arc shield has only
  $2^{o(L^2)}$ effective states, or else Theorem 1 pays.
* Conditioned on that trace, retained core labels outside the shield have
  $2^{\Theta(L^2)}$ states of rank $O(L)$.
* The hidden-core and mark directional profiles are anti-aligned by
  $\Theta(L^2)$, or their mixed bank gives the missing gain.

A theorem about the absolute outer shield, or a repeated local half-plane
bank, cannot close this case.  One must either bound the quadratic
directional skew using the actual source/repair histories, or prove the
hereditary high-mean statement required by the common-skew composition
theorem.  Without one of those inputs, the desired assertion is
coefficient-equivalent to the remaining cap/cup mean gate.

## 5. Hall-dense subfamilies have a hereditary three-projection core

The global Hall formulation gives one further exact reduction on this mark
branch.  Let $\mathcal A$ be any nonempty subfamily of distinct singleton
records and let

\[
 U_{\mathcal A}=\left|\bigcup_{g\in\mathcal A}\mathcal B_g\right|,
 \qquad \lambda_{\mathcal A}={|\mathcal A|\over U_{\mathcal A}},    \tag{17}
\]

where $\mathcal B_g$ contains, among all the other established banks, the
source anchor $R\cup\{x\}$, target anchor $R\cup\{p\}$, and marked
half-plane face $\{x,p\}$.  Assume source and target rank at most $q$.

> **Theorem 2 (three-projection Hall core).**  There is a subfamily
> $\mathcal A'\subseteq\mathcal A$,
> $|\mathcal A'|\ge|\mathcal A|/2$, such that every nonempty fibre of
> each of the three projections
> 
> \[
> (R,x,p)\mapsto(R,x),\qquad(R,p),\qquad(x,p)              \tag{18}
> \]
> 
> has degree at least
> 
> \[
>                         d={\lambda_{\mathcal A}\over4(q+1)}.       \tag{19}
> \]

**Proof.**  Let $S,T,M$ be the numbers of projection vertices in the
three parts.  A source face has at most $q$ representations $(R,x)$,
and the same is true for a target face.  A two-point face has at most two
ordered $X,Y$ roles.  Since all three kinds of faces belong to the Hall
union,

\[
                         S+T+M\le(2q+2)U_{\mathcal A}.     \tag{20}
\]

View the records as a three-partite, three-uniform hypergraph on these
projection vertices.  Repeatedly delete a projection vertex of current
degree less than $d$, together with its incident records.  Charge every
deleted record to the first vertex which deletes it.  The total number of
deleted records is less than

\[
 d(S+T+M)\le {\lambda_{\mathcal A}\over2}U_{\mathcal A}
             ={|\mathcal A|\over2}.                       \tag{21}
\]

The remaining hypergraph proves the theorem.  QED.

This reset is hereditary: it applies to the actual Hall-maximizing
subfamily, not only to the original selected system.  If
$\lambda_{\mathcal A}>D^{1-\epsilon}$, it simultaneously produces,
up to the polynomial rank loss,

* at least $d$ blockers for every retained source $(R,x)$;
* at least $d$ ears for every retained target $(R,p)$; and
* at least $d$ distinct retained cores for every mark pair $(x,p)$.

For a fixed core $R$, the active bipartite mark graph is a disjoint union
over insertion edges of $R$: an edge $xp$ can occur only when
$e_R(x)=e_R(p)$.  Hence every nonempty rooted component left by Theorem 2
has minimum degree at least $d$ on both sides, at least $d$ ear labels,
at least $d$ blocker labels, and at least $d^2$ records.  Every edge is
the exact dominance relation
$x\in\operatorname{int}\operatorname{conv}\{u,v,p\}$.

Thus a Hall counterexample cannot be a pointwise radial or sparse-star
failure.  It must be a dense family of minimum-degree dominance components
whose source, target, pair, outer, Ferrers, half-plane, and one-gap face
unions are all simultaneously reused.  Theorem 1 then forces any
quadratic context entropy not already paid by a common convex trace shield
into the hidden retained-core child.  Equations (4)--(7) identify the only
presently realizable way that hidden child can avoid a mixed product:
quadratic directional anti-alignment.  No bounded-rank planar regression
with $\lambda_{\mathcal A}>D^{1-\epsilon}$ is supplied here.
