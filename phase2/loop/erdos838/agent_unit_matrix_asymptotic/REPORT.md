# Unit type-A matrices: Renyi alignment and endpoint-span localization

**Date:** 2026-08-14
**Verdict:** no proof or counterexample to the asymptotic target

\[
 H(R)=\frac{nF_R(1/2)}{F_R(1)}=n^{o(1)}
\]

is claimed.  The finite strengthening `H<=2` is already false, including in
the complete unit reflection-order class; none of the statements below uses
it.  This pass gives four exact pieces of structure:

1. the forward/reverse Frobenius angle is precisely a Hellinger affinity, so
   its cross-activity loss is a Renyi-divergence drift; and
2. a fixed-power counterexample to `H=n^{o(1)}` would have essentially all of
   its excess half-activity mass on super-polylogarithmic endpoint intervals,
   with a quantitative incidence-scale polynomial lower bound;
3. every endpoint cell satisfies an explicit trace-entropy Bellman
   inequality against the face polynomial of its open interior interval; and
4. every cell either has a genuine two-non-direct product face before
   descent or is quantitatively close to one-sided.  Exactly one-sided cells
   are simultaneous endpoint-root records.

These are theorems, but the n58, central-Pascal, and scalable alternating
audits expose the remaining overlap obstruction.  They rule out local or
bounded-span matrix blocks as the source of an asymptotic counterexample and
leave a genuinely long-range signed-record/trace-reuse problem.

All logarithms below are base two.

## 1. Exact matrix normalization

For a type-`A_(n-1)` reflection order `R`, put

\[
 B_R(t)=\prod_R(I+tE_{ji}),\qquad
 A_R(t)=\prod_{R^{\rm rev}}(I+tE_{ji})=B_R(-t)^{-1}.
\]

Every positive root occurs once and has unit weight.  On the strict lower
triangle write

\[
 a_{ij}(t)=A_R(t)_{j,i},\qquad b_{ij}(t)=B_R(t)_{j,i},
 \qquad i<j.
\]

The off-diagonal cross mass is

\[
 Q_R(t)=\sum_{i<j}a_{ij}(t)b_{ij}(t),
\]

and the empty-inclusive convex-face polynomial is exactly

\[
 F_R(t)=1+nt+Q_R(t).                                      \tag{1}
\]

Root completeness gives `a_ij(t),b_ij(t)>=t`, and hence
`Q_R(t)>=binom(n,2)t^2`.  Therefore, at `t=1/2,1`,

\[
 F_R(t)=Q_R(t)(1+O(1/n)).                                 \tag{2}
\]

In particular the asymptotic half-weight target is equivalent to

\[
 \log\frac{Q_R(1)}{Q_R(1/2)}\ge(1-o(1))\log n.             \tag{3}
\]

This removes the distracting diagonal/singleton correction without making
any false finite claim.

## 2. The Frobenius angle is a Renyi divergence

Define the separate endpoint energies

\[
 E_A(t)=\sum_{i<j}a_{ij}(t)^2,\qquad
 E_B(t)=\sum_{i<j}b_{ij}(t)^2
\]

and probability laws on the positive roots

\[
 p_t(i,j)=\frac{a_{ij}(t)^2}{E_A(t)},\qquad
 q_t(i,j)=\frac{b_{ij}(t)^2}{E_B(t)}.
\]

The normalized Frobenius angle is exactly their Hellinger affinity:

\[
 \kappa(t):=\frac{Q_R(t)}{\sqrt{E_A(t)E_B(t)}}
   =\sum_{i<j}\sqrt{p_t(i,j)q_t(i,j)}.                     \tag{4}
\]

Consequently, if `D_t=D_(1/2)(p_t||q_t)` is order-one-half Renyi divergence,

\[
 \boxed{D_t=-2\log\kappa(t).}                              \tag{5}
\]

This gives the exact cross-activity decomposition

\[
 \boxed{
 \log\frac{Q_R(1)}{Q_R(1/2)}
 =\frac12\log\frac{E_A(1)E_B(1)}{E_A(1/2)E_B(1/2)}
  -\frac12(D_1-D_{1/2}).}                                  \tag{6}
\]

Thus separate singular-value/Frobenius growth supplies the first term, but
forward/reverse endpoint segregation charges back the second.  Equation (6)
is the entropy form of the relative-alignment obstruction.  The exact
operator barriers already banked in
`../agent_cyclic_stem_hw/coxeter_matrix/REPORT.md` show why determinant-one,
PSD, or separate-Schatten interpolation cannot control this drift: the cross
operator can have nonreal spectrum, its symmetric part can be indefinite,
and separate endpoint norms can collide while the cross trace changes.

The surviving matrix target is now precise: prove that the energy dilation
minus half the Renyi drift in (6) is `(1-o(1))log n`.  Bounding either term
alone is insufficient; the scalable alternating family in the cited report
has exponential terms which cancel at leading order.

### The actual face-endpoint law is the Hellinger midpoint

There is a stronger common-endpoint interpretation.  Let

\[
 r_t(i,j)=\frac{a_{ij}(t)b_{ij}(t)}{Q_R(t)}.                 \tag{6a}
\]

This is exactly the endpoint marginal of the activity-`t` convex-face law
(after omitting the asymptotically negligible empty faces and singletons).
Equations (4) and (6a) give the pointwise identity

\[
 \boxed{r_t(i,j)^2=\frac{p_t(i,j)q_t(i,j)}{\kappa(t)^2}.}   \tag{6b}
\]

Thus `r_t` is the normalized geometric, or Hellinger-midpoint, law between
the squared forward and reverse endpoint histories.  Taking logarithms in
(6b) yields

\[
 \boxed{
 D_{1/2}(p_t\Vert q_t)
 =D(r_t\Vert p_t)+D(r_t\Vert q_t).}                         \tag{6c}
\]

This is useful because the two divergences on the right have the ordinary
KL chain rule.  For any hierarchical partition `mathcal C` of endpoint
intervals---in particular a dyadic interval tree---write `p^C,q^C,r^C` for
the cell marginals.  Then exactly

\[
\begin{aligned}
 D_{1/2}(p_t\Vert q_t)
={}&D(r_t^{\mathcal C}\Vert p_t^{\mathcal C})
   +D(r_t^{\mathcal C}\Vert q_t^{\mathcal C})\\
 &+\sum_{C\in\mathcal C}r_t(C)
 \left[D(r_t(\cdot\mid C)\Vert p_t(\cdot\mid C))
      +D(r_t(\cdot\mid C)\Vert q_t(\cdot\mid C))\right]. \tag{6d}
\end{aligned}
\]

So interval nesting does not make the alignment loss mysterious: it splits
exactly into a between-cell mismatch and conditional within-cell mismatches.
The unresolved issue is cross-activity charging.  Individual terms in (6d)
can grow from `t=1/2` to `t=1`, and their drift must be paired with the energy
dilation created by the same endpoint histories.

## 3. Endpoint-cell cap

For `i<j`, put

\[
 G_{ij}(t)=a_{ij}(t)b_{ij}(t).
\]

In a reflection order, `G_ij` is the generating polynomial of convex faces
whose leftmost and rightmost vertices are `i,j`.  Such a face is determined
by a subset of the `j-i-1` intervening vertices.  Hence there is the
coefficientwise inequality

\[
 \boxed{G_{ij}(t)\preceq t^2(1+t)^{j-i-1}.}                \tag{7}
\]

This uses reflection betweenness (equivalently, the face/path-pair
bijection), not merely a complete list of root factors.  It is false as a
squarefree interpretation for arbitrary root orders.

Let `F_<=D(1/2)` be the half-activity mass of the empty face, all singletons,
and faces whose endpoint span is at most `D`.  Summing (7) gives

\[
\begin{aligned}
 F_{\le D}(1/2)
 &\le 1+\frac n2+\frac14\sum_{d=1}^D(n-d)(3/2)^{d-1}\\
 &\le \boxed{1+\frac n2(3/2)^D}.                           \tag{8}
\end{aligned}
\]

This is the promised local-matrix cap.

## 4. Quadratic-logarithmic span theorem for any power-law obstruction

> **Theorem (endpoint-span localization).**  Suppose along a sequence of
> complete unit reflection orders there is a fixed `epsilon>0` such that
> `H(R_n)>=n^epsilon`.  Put `alpha=log_2(3/2)`.  For every fixed
>
> \[
> c<\frac{1+\epsilon}{\alpha}
> \]
>
> and `D=floor(c log_2 n)`, the fraction of the `t=1/2` face mass carried by
> endpoint spans at most `D` tends to zero.

**Proof.**  Every zero-, one-, two-, and three-point subset is convex, so

\[
 F_R(1)\ge\binom n3.
\]

The assumed power-law violation gives

\[
 F_R(1/2)=\frac{H(R)}nF_R(1)
 \ge n^{\epsilon-1}\binom n3=\Omega(n^{2+\epsilon}).       \tag{9}
\]

On the other hand, (8) is

\[
 F_{\le D}(1/2)=O(n^{1+c\alpha}).                          \tag{10}
\]

The exponent in (10) is strictly smaller than `2+epsilon`, proving the
claim.  \(\square\)

This elementary version uses only the universal three-point coefficient.
The already banked lower bound for Erdős 838 sharpens it by a full logarithmic
factor.  Put `L=log_2 n` and

\[
 \alpha=\log_2(3/2),\qquad
 c_*={1\over4\alpha}=0.4273\ldots .                         \tag{10a}
\]

> **Theorem (quadratic-span localization).**  For every fixed `eta>0`, under
> the same power-law obstruction `H(R_n)>=n^epsilon`, the fraction of the
> half-activity mass carried by spans at most
>
> \[
> D_n=\left\lfloor(c_*-\eta)L^2\right\rfloor               \tag{10b}
> \]
>
> tends to zero.

**Proof.**  The coefficient-`1/4` lower bound gives

\[
 \log F_R(1)\ge(1/4-o(1))L^2.                               \tag{10c}
\]

Since `F_R(1/2)=H(R)F_R(1)/n` and `log H(R)>=epsilon L`, the
linear terms do not affect the quadratic coefficient:

\[
 \log F_R(1/2)\ge(1/4-o(1))L^2.                             \tag{10d}
\]

But (8), with (10b), gives

\[
 \log F_{\le D_n}(1/2)
 \le L+\alpha D_n+O(1)
 \le(1/4-\alpha\eta)L^2+O(L).                               \tag{10e}
\]

The ratio of (10e) to (10d) is `2^{-Omega_eta(L^2)}`.  \(\square\)

The coefficient-`1/4` theorem is currently banked for actual planar point
sets, so this sharpened conclusion is asserted at least for the stretchable
reflection orders needed by Erdős 838.  The first, logarithmic theorem used
only the matrix face coefficients and applies to any reflection-order class
where those coefficients have the squarefree face interpretation.

Since failure of `H=n^{o(1)}` produces a fixed `epsilon>0` on a subsequence,
the quadratic theorem applies to every genuine planar asymptotic
counterexample.  No bounded-size gadget, no `o(log n)` endpoint window, and
indeed no window below
`(1/(4log_2(3/2))-o(1))(log_2n)^2` can carry its bad mass.

The limitation is important.  Long endpoint span does not force large face
rank.  A direct edge already spans an arbitrary interval, and benign Pascal
families also put most of their half mass on long intervals.  A proof still
needs a history-sensitive statement converting long-range endpoint energy
into radial dilation without paying it back as Renyi drift.

### Entropy bootstraps the span to every subpolynomial scale

The mean constraint on a hypothetical counterexample pushes the localization
much farther.  Let `mu_(1/2)` be the activity-half mean face size.  Monotonicity
of the activity mean gives

\[
 \mu_{1/2}\le\log\frac{F(1)}{F(1/2)}
 =\log\frac nH\le(1-\epsilon)L.                            \tag{10f}
\]

For `S>=2`, let `M_S` be the half-weighted mass of nontrivial faces with
endpoint span at most `S`, put `rho_S=M_S/F(1/2)`, and let `kbar_S` be their
conditional mean size.  Under this conditional law a face can be encoded by
one of at most `nS` endpoint pairs and a subset of at most `S` intervening
labels.  Its Shannon entropy is also exactly `log M_S+kbar_S`.  The elementary
subset-entropy bound therefore gives

\[
 \log M_S+\bar k_S
 \le\log(nS)+\bar k_S\log(eS).                            \tag{10g}
\]

On the other hand, positivity and (10f) give

\[
 \rho_S\bar k_S\le\mu_{1/2}\le(1-\epsilon)L.              \tag{10h}
\]

Combining (10d), (10g), and (10h) proves two further conclusions.

> **Theorem (subpolynomial-span exclusion).**  If `S=S_n` satisfies
> `log S=o(L)`, then under a fixed-power obstruction `H>=n^epsilon`,
>
> \[
> \boxed{\rho_{S_n}=o(1).}                                 \tag{10i}
> \]

Indeed, if `rho_S` stayed bounded below, then
`log M_S>=(1/4-o(1))L^2`, while (10g) would force
`kbar_S=Omega(L^2/log S)=omega(L)`, contradicting (10h).

More quantitatively, for fixed `gamma>0` and `S=n^gamma`, every positive
subsequential limit of `rho_S` obeys

\[
 \boxed{\limsup\rho_{n^\gamma}\le4\gamma(1-\epsilon).}     \tag{10j}
\]

To see this, (10g) forces
`kbar_S>=(1/(4gamma)-o(1))L`, and then use (10h).  Thus one may take, for
example,

\[
 S_n=2^{L/\log L}=n^{1/\log L}
\]

in (10i): asymptotically all bad half mass must span more than this
super-polylogarithmic but subpolynomial number of consecutive labels.  This
strictly strengthens the explicit `c_*L^2` cutoff.  It also identifies the
remaining recursive interval problem: any bad state must repeatedly retain
endpoint histories across genuinely growing, rather than local, intervals.

There is also a useful incidence-weighted form which does not choose a
cutoff.  Under the nontrivial half-face law let `K` be face size and `D` its
endpoint span.  Encoding the endpoint pair and then the interior subset gives

\[
 \log Q(1/2)+\mathbb E K
 \le 2L+\mathbb E[K\log(eD)]+O(1).                         \tag{10k}
\]

Together with `log Q(1/2)>=(1/4-o(1))L^2` and (10f), this implies

\[
 \mathbb E[K\log D]\ge(1/4-o(1))L^2.                      \tag{10l}
\]

Equivalently, if an incidence is sampled by size-biasing the half-face law,

\[
 \boxed{
 \mathbb E_{\rm incidence}\log D
 \ge\left({1\over4(1-\epsilon)}-o(1)\right)L.}             \tag{10m}
\]

Thus the geometric mean endpoint span seen by a random selected-vertex
incidence is at least
`n^(1/(4(1-epsilon))-o(1))`.  Reflection betweenness now acts across a
macroscopic hidden interval: every boundary path from the two endpoints
must cross that interval through temporally nested roots.  What remains
unproved is a no-reuse theorem which turns those nested roots into new rank
instead of repeatedly charging the same direct boundary edge.

### Exact one-sided-history dichotomy

Reflection betweenness gives one further exact reduction.  Write

\[
 a_{ij}(t)=t+r_{ij}t^2+\cdots,\qquad
 b_{ij}(t)=t+s_{ij}t^2+\cdots .                            \tag{10n}
\]

Every intermediate label `k` gives a two-edge path `i-k-j` in exactly one
temporal direction, so

\[
 r_{ij}+s_{ij}=j-i-1.                                      \tag{10o}
\]

Moreover,

\[
 \boxed{r_{ij}=0\Longrightarrow a_{ij}(t)=t,qquad
        s_{ij}=0\Longrightarrow b_{ij}(t)=t.}              \tag{10p}
\]

For stretchable orders this is immediate from slopes: every subsequence of
a strict cup or cap chain is again a cup or cap chain.  Hence any temporal
path with at least two edges would retain a two-edge path after deleting all
but one interior vertex, contradicting the missing quadratic coefficient.
The same statement follows from the packet betweenness axiom by shortcutting
the path.

Thus a macroscopic endpoint cell has only two possibilities:

1. both temporal directions already have nontrivial rank-two histories; or
2. one direction is **exactly the same direct root at every nesting scale**,
   and all entropy lies in the opposite path polynomial.

The verifier finds `299` forward-direct and `258` backward-direct cells in
the 58-wire record, and `96` of each in the 36-point Pascal composition.
The alternating family takes the second branch at every endpoint pair.  This
formally identifies why a naive dyadic ancestor telescope fails: it may
charge one direct root at every ancestor without creating a new selected
vertex.  A valid recursion must instead prove dilation from the rich
one-sided polynomial, or use the two-sided branch to create a genuinely new
cup--cap product before descending.

### The exact coupled cell Bellman inequality

The preceding last sentence can be made quantitative.  Fix a cell `(i,j)`,
put `I={i+1,...,j-1}`, `m=|I|`, and write

\[
 a(t)=t+A(t),\qquad b(t)=t+B(t).                           \tag{10q}
\]

Both remainders have nonnegative coefficients and start in degree two.  The
cell polynomial splits into four disjoint path-pair types:

\[
 \boxed{G_{ij}(t)=t^2+tA(t)+tB(t)+A(t)B(t).}              \tag{10r}
\]

The final summand is not just an algebraic error term.  It is exactly the
subfamily whose two boundary histories are both non-direct.  Deleting the
two endpoints is injective on this family and leaves a convex face of the
open interval.  Therefore, coefficientwise,

\[
 \boxed{\frac{A(t)B(t)}{t^2}\preceq F_I(t).}              \tag{10s}
\]

At `h=1/2`, set

\[
 u={A(h)\over h},\quad v={B(h)\over h},\quad
 \theta={A(h)B(h)\over a(h)b(h)}
       ={uv\over(1+u)(1+v)}.                              \tag{10t}
\]

For every `0<delta<1` there is the exact alternative

\[
 \boxed{\theta\ge\delta\quad\hbox{or}\quad
 \min(u,v)\le {\sqrt\delta\over1-\sqrt\delta}.}          \tag{10u}
\]

Indeed, if both normalized remainders exceed the displayed threshold, then
both `u/(1+u)` and `v/(1+v)` exceed `sqrt(delta)`.  Thus a cell either creates
a positive product face **before** recursive descent, or one of its two
histories has half-value within the factor `1/(1-sqrt(delta))` of the direct
root.  Notice that this is stronger than the rank-two dichotomy: it remains
quantitative when both quadratic coefficients are nonzero.

There is also a sharp one-cell radial inequality in the exactly one-sided
case.  Suppose, after possibly exchanging the directions, that

\[
 a(t)=t,\qquad b(t)=tC(t).                                \tag{10v}
\]

The monomials underlying `C` are a family `mathcal T` of distinct subsets of
`I`: they are the interior traces left after deleting the two endpoints.
Every trace is itself convex, so

\[
 C(t)\preceq F_I(t).                                      \tag{10w}
\]

Put `Z=C(1/2)=2b(1/2)` and sample `S in mathcal T` with probability
`2^(-|S|)/Z`.  If `ubar=E|S|`, then

\[
 H(S)=\log Z+\bar u
 \le m h_2(\bar u/m),                                    \tag{10x}
\]

where the inequality is the standard marginal-entropy bound for a random
subset of an `m`-element set.  On the other hand Jensen gives

\[
 \boxed{
 {G_{ij}(1)\over G_{ij}(1/2)}
 =4{C(1)\over C(1/2)}
 =4\,\mathbb E 2^{|S|}
 \ge2^{2+\bar u}.}                                       \tag{10y}
\]

This is the requested radial-dilation Bellman bound.  To display explicitly
how it couples to the interior face mass, define

\[
 \lambda={C(1/2)\over F_I(1/2)},\qquad
 \psi_m(Z)=\inf\{x\in[0,m]:\log Z+x\le m h_2(x/m)\}.
\]

Then (10x)--(10y) say

\[
 \boxed{
 {G_{ij}(1)\over G_{ij}(1/2)}
 \ge2^{2+\psi_m(\lambda F_I(1/2))}.}                      \tag{10z}
\]

For example, if `m<=n`, `L=log n`, and
`log Z>=(beta-o(1))L^2`, the elementary bound
`m h_2(x/m)<=x log(e m/x)` forces
`ubar>=(beta-o(1))L`; the cell dilates by at least
`n^(beta-o(1))`.  This is rigorous, but it also exposes the coefficient
barrier: the universal `1/4` quadratic entropy by itself yields only a
quarter-power dilation at one level.  A complete proof must show that trace
capture `lambda` persists through enough nested intervals, or charge the
missing trace mass to product faces from (10s).  Summing (10w) naively over
all endpoint cells loses up to a quadratic endpoint multiplicity and does
not close such an induction.

In fact the entropy part has a stronger universal form which is worth
recording as the exact Bellman functional.  Every face in the whole endpoint
cell has a unique trace after deleting `i,j`, regardless of its boundary
type.  Hence

\[
 C_{ij}(t):={G_{ij}(t)\over t^2}\preceq F_I(t).            \tag{10za}
\]

Put `Z_ij=C_ij(1/2)=4G_ij(1/2)` and let `u_ij` be the mean trace size under
its half-weighted trace law.  Exactly as above,

\[
 \boxed{
 \log Z_{ij}+u_{ij}\le m h_2(u_{ij}/m),\qquad
 {G_{ij}(1)\over G_{ij}(1/2)}\ge2^{2+u_{ij}}.}            \tag{10zb}
\]

If `r_(1/2)` is the endpoint law (6a), summing cellwise yields the rigorous
global Bellman lower bound

\[
 \boxed{
 {Q(1)\over Q(1/2)}
 \ge\sum_{i<j}r_{1/2}(i,j)
 2^{\,2+\psi_{j-i-1}(4G_{ij}(1/2))}.}                    \tag{10zc}
\]

Equivalently one may replace the argument of `psi` by
`lambda_ij F_I(1/2)`, where
`lambda_ij=4G_ij(1/2)/F_I(1/2)`.  This is a completely explicit
conditional recursion target: prove that the endpoint-law average in
(10zc) is `n^(1-o(1))`, using the fact that small capture ratios leave most
of the interior face mass available for descent.  Without a bounded-overlap
or signed-record lemma, however, the same interior trace can be available to
many outer endpoint cells, which is the precise unresolved charging gap.

The capture ratio also has an exact information-theoretic meaning.  Let
`pi_I(S)=2^(-|S|)/F_I(1/2)` be the full half-Gibbs face law in the open
interval, and let `nu_ij` be the trace law of the endpoint cell.  Since the
trace family is an event of `pi_I` of probability `lambda_ij`, and the two
laws have identical relative weights on that event,

\[
 \boxed{D(\nu_{ij}\Vert\pi_I)=\log{1\over\lambda_{ij}}.}  \tag{10zd}
\]

Thus the only loss in descending through a cell is a literal conditioning
cost.  The desired multiscale proof would follow from a chain rule which
charges these costs without repeatedly paying for the same inner face; the
current interval state does not yet remember enough boundary data to make
that chain Markovian.

### Canonical endpoint peeling gives an exact KL chain rule

There is nevertheless a canonical reference process for which all capture
losses telescope exactly.  If a face is
`U={v_1<...<v_k}`, successively peel its endpoint pairs

\[
 e_r=(v_{r+1},v_{k-r}),\qquad 0\le r<\lfloor k/2\rfloor.  \tag{10ze}
\]

On any current interval `J`, define a reference transition by taking the
endpoint marginal of the **unconditioned** half-Gibbs face law on `J`:

\[
 q_J(i,j)={G_{ij}(1/2)\over F_J(1/2)},\quad
 q_J(\varnothing)={1\over F_J(1/2)},\quad
 q_J(\{i\})={1/2\over F_J(1/2)}.                          \tag{10zf}
\]

After a pair `(i,j)` is chosen, this reference process forgets the outer
boundary and independently repeats in the open interval `(i,j)`.  It is a
probability law on syntactic nested endpoint chains, although it can produce
a chain whose union is not a convex face.  Let `mathsf P` be the true
half-Gibbs law on the canonical chains of convex faces and `mathsf Q` this
reference law.  Direct cancellation of the successive interval partition
functions gives, pointwise,

\[
 \boxed{
 {\mathsf Q(U)\over\mathsf P(U)}
 =\prod_{r<\lfloor |U|/2\rfloor}\lambda_{e_r}.}           \tag{10zg}
\]

Consequently the desired cumulative loss is already a single KL divergence:

\[
 \boxed{
 \mathbb E_{\mathsf P}\sum_r\log{1\over\lambda_{e_r}}
 =D(\mathsf P\Vert\mathsf Q).}                            \tag{10zh}
\]

This answers the telescope question affirmatively, but does not by itself
bound the answer.  The endpoint chain encodes the face bijectively, so its
entropy is

\[
 H(\mathsf P)=\log F(1/2)+\mu_{1/2}.                      \tag{10zi}
\]

A general KL divergence need not be bounded by the entropy of its first
argument.  What is still needed here is a geometric lower bound on the
reference probabilities of compatible chains (equivalently, an upper bound
on the incompatibility cost in (10zh)).  The exact audits do satisfy the
stronger pointwise inequality `sum log(1/lambda)<=-log mathsf P(U)`, but no
proof of that inequality is claimed.

That pointwise inequality is already false for abstract hereditary
set systems satisfying the universal triple condition.  Take `n=m+4`
ordered vertices, a middle block `W` of size `m`, and the nested four-set
`U={0,1,n-2,n-1}`.  Let the complex consist of every set of size at most
three, every subset of `W`, and `U` (with its subsets).  At `m=19`, exact
rational evaluation gives

\[
 \lambda_{0,n-1}\lambda_{1,n-2}<\Pr_\pi(U),              \tag{10zia}
\]

with `cost-surprisal=0.125504` bits.  The two large, nested interior Boolean
blocks are visible to the reference process but incompatible with the chosen
outer endpoints, so their partition functions are paid twice.  Thus any
pointwise or KL/entropy theorem must use planar reflection signs/product
faces, not only downward closure and the fact that all triples are faces.

For contrast, the verifier exhausts all packet-sign reflection classes
through `n=6` (respectively `2,8,62,908` classes for `n=3,4,5,6`) and checks
the pointwise inequality in every face.  It also checks 100 deterministic
random straight-line configurations at `n=14`.  No planar/reflection-order
violation was found.  Exhaustion at `n=7,8` was not attempted: enumerating all
reduced words already jumps from `292,864` at `n=6` to over a billion at
`n=7`.  The abstract counterexample therefore kills the entropy-only proof,
not the still-plausible planar signed-record inequality.

Even a hypothetical universal bound `D(mathsf P||mathsf Q)<=H(mathsf P)`
would not close 838 on its own.  The rank-truncated complex
`{S:|S|<=c log n}` has

\[
 \log F(1/2)=(c-o(1))(\log n)^2,qquad
 \log{F(1)\over F(1/2)}=(c+o(1))\log n,                  \tag{10zib}
\]

while its face-law entropy is still quadratic.  It therefore obeys the
right coarse entropy scale but has only `n^c` activity dilation.  A useful
geometric capture theorem must couple KL to radial rank with a near-unit
constant.  One sufficient form would be

\[
 \mu_{1/2}+{D(\mathsf P\Vert\mathsf Q)\over\log n}
 \ge(1-o(1))\log n                                      \tag{10zic}
\]

together with an independent planar bound
`D(mathsf P||mathsf Q)=o((log n)^2)`.  Neither inequality is presently proved;
(10zic) is recorded only to quantify the scale and constant a KL route must
deliver.  The much weaker `D<=H=Theta((log n)^2)` leaves the entire fixed-power
gap untouched.

There is an additional global bounded-overlap identity.  For a convex face
`S`, let `d_r(S)` be the number of convex faces `U` whose core after deleting
the `r` smallest and `r` largest labels is `S`.  Radial deletion is unique,
so under the full half-Gibbs face law `pi`,

\[
 \boxed{
 \mathbb E_\pi d_r(S)
 =4^r\,\Pr_\pi\{|U|\ge2r\}\le4^r.}                       \tag{10zj}
\]

For `r=1` the mean number of two-endpoint extensions of a random face is
strictly less than four, not quadratic in `n`.  Moreover, the law of the
`r`-times-peeled core is exactly the `d_r`-size-biased tilt of `pi`.  Thus the
overlap gap has been reduced to controlling the high-degree tails of these
radial extension counts.  Reflection signs/product faces must enter there:
the first moment (10zj) alone allows a very small family of cores to carry
large degree and hence large KL cost.

### Homogeneous intervals are endpoint-root records, but abundance is not enough

The one-sided branch has a useful order-theoretic classification.  If one
direction is direct-only, then for every `i<k<j` the two other roots occur in
the same order.  Reflection betweenness consequently makes `(i,j)` a
simultaneous record among the two endpoint stars: in one orientation

\[
 \operatorname{pos}(k,j)<\operatorname{pos}(i,j)
 <\operatorname{pos}(i,k)\quad(i<k<j),                   \tag{10aa}
\]

and all inequalities reverse in the other orientation.  In a straight-line
realization this says that the slope of the chord `ij` is a record minimum or
maximum among the slopes from `i`; equivalently all intermediate points lie
strictly on the same side of `ij`.  Thus `ij` is a hull edge of the whole
interval `P[i..j]`.

This record formulation does **not** by itself give a density theorem.
Both a convex cup and the stretchable alternating family (11) have
`Theta(n^2)` homogeneous intervals, including quadratically many crossing
pairs; the latter is exactly one-sided in every endpoint cell.  Therefore
neither the count of long homogeneous intervals, laminarity versus crossing,
nor interval span alone can force the product branch.  Any successful
classification must retain the signs of the endpoint records, or an
equivalent coupling between adjacent/nested intervals.

## 5. A long-span Renyi-drift barrier

The preceding KL decomposition is exact, but a tempting conclusion from it
is false: after localizing to long intervals, the Renyi drift need not be
`o(log n)`.  It can remain linear in `n`, even for a straight-line,
once-per-root unit reflection order.

Use the stretchable alternating family from
`../agent_cyclic_stem_hw/REFLECTION_FROBENIUS_BARRIER.md`, whose chirotope is

\[
 \chi(i,j,k)=(-1)^i\qquad(i<j<k).
\]

For an endpoint distance `d`, one temporal direction has only the direct
path `t`, while the other has the exact nested-history polynomial

\[
 R_d(t)=t+t^2\sum_{s=1}^{d-1}(1+t)^{\lfloor(s-1)/2\rfloor}. \tag{11}
\]

The rich direction alternates with the parity of the left endpoint.  Thus
forward and reverse endpoint energies live on interlaced, fully nested
interval families; this is not an artifact of short spans.

For a cutoff `D`, restrict `Q,E_A,E_B,kappa,D_t` to pairs with `j-i>D` and
decorate them by `>D`.  If `D=O(log n)`, then (11) gives

\[
\begin{aligned}
 Q^{>D}_n(t)&=\Theta_t((1+t)^{n/2}),\\
 E^{>D}_{A,n}(t),E^{>D}_{B,n}(t)&=\Theta_t((1+t)^n),\\
 \kappa^{>D}_n(t)&=\Theta_t((1+t)^{-n/2}).                 \tag{12}
\end{aligned}
\]

Indeed the deleted short-span sums are only polynomial in `n`, whereas each
displayed full sum has an exponential long-span tail.  Therefore

\[
 \boxed{
 D^{>D}_1-D^{>D}_{1/2}
 =n\log_2(4/3)+O(1).}                                      \tag{13}
\]

This is a scalable barrier inside exactly the branch selected by the
endpoint-span theorem.  Neither long span, interval nesting, reflection
betweenness, nor straight-line stretchability bounds the Renyi drift by
`o(log n)`.

It is still not a counterexample to the half-weight target.  On the same
long intervals, the separate energy term in (6) is

\[
 n\log_2(4/3)+O(1),
\]

while half the drift in (13) costs only
`(n/2)log_2(4/3)+O(1)`.  The surviving net dilation is exponential.  This
proves that the long-span branch must be attacked by a **coupled** inequality
between energy creation and conditional KL drift at the same nesting nodes;
a stand-alone affinity or Renyi bound is impossible.

## 6. Exact stress tests

The verifier reconstructs two unit complete reflection orders and checks
all quantities with exact integers or rationals.

### The 58-wire finite counterexample to `H<=2`

For the saved record,

\[
 F(1)=1059668,\qquad F(1/2)=\frac{18736483}{512},\qquad
 H=\frac{543358007}{271275008}=2.002978\ldots .
\]

This is deliberately included so that no argument silently reinstates the
false constant-two claim.  In (6), the separate energy dilation is
`8.079337` bits, while the Renyi drift charges back `3.222400` bits, leaving
only `4.856937` bits of off-diagonal dilation.  The endpoint-span fractions
at `D=5,10` are respectively `0.005240` and `0.022286`.

At half activity, exactly one-sided cells carry `0.308204` of the
off-diagonal mass, and those of span at least ten still carry `0.304494`.
The genuinely two-rich product term `AB` carries `0.516659` of all cell
mass; cells in which it is at least one quarter of the cell carry `0.689457`
of the mass.  On the one-sided cells, the trace family captures a
cell-mass-weighted `0.050332` of its full interior face polynomial, a mean
loss of `4.772206` bits.  Across all cells, the universal trace capture from
(10za) is `0.097392` (weighted log-loss `4.163010` bits).  Thus this finite
adversary really does exercise both sides of (10u): it has a macroscopic long
homogeneous component, but also a larger product-face component available
for recursive charging.

Enumerating all `1,059,609` nontrivial faces verifies (10zg) exactly at every
face.  The expected cumulative canonical-peeling loss is `6.372305` bits,
versus endpoint-chain entropy `19.693268` bits; the worst pointwise value of
`cost-surprisal` is `-3.195996` bits.  The one-step mean radial extension
degree from (10zj) is `3.996721`.

### The depth-two central Pascal composition

For the exact rational realization `T_(4,2)[T_(4,2)]`,

\[
 F(1)=441400,\qquad F(1/2)=\frac{80351}{8},\qquad
 H=\frac{723159}{882800}=0.81916\ldots .
\]

Here the energy dilation is `5.887587` bits and the Renyi charge is only
`0.427277` bits, leaving `5.460310` bits, already larger than
`log_2 36=5.169925...`.  Nevertheless the short-span fractions at `D=5,10`
are still only `0.011258` and `0.043671`.  This is the exact warning that
span localization is necessary but far from sufficient.

The coupled split is much cleaner here: one-sided cells carry only
`0.018080` of the mass, while `AB` carries `0.794262`; product-dominant cells
carry `0.977225`.  The few one-sided trace families capture a weighted
`0.417736` of the corresponding interior face mass (mean loss `1.700008`
bits).  Across all cells, the universal weighted capture is `0.221832`
(weighted log-loss `2.414801` bits).  This sharply separates the Pascal
mechanism from the n58 finite adversary even though their raw long-span
statistics looked similar.

Here all `441,363` nontrivial faces give canonical-peeling loss `4.909362`
bits versus chain entropy `18.261981` bits; the worst pointwise
`cost-surprisal` margin is `-6.049298` bits, and the mean one-step extension
degree is `3.992433`.

The verifier additionally removes every span at most
`ceil(2 log_2 n)` from the alternating family through `n=160`.  It checks
exactly that

\[
 \frac{(\kappa^{>D}_n(1))^2}{(\kappa^{>D}_n(1/2))^2}
 (4/3)^n
\]

stays between fixed positive rational constants.  At `n=160` the measured
Renyi drift is `0.411774 n` bits, approaching
`log_2(4/3)n=0.415037...n`.

The verifier also enumerates the canonical chains in the stretchable
alternating family at `n=30`: cumulative capture KL is `3.560101` bits versus
face entropy `17.383095` bits.  Together with the separate scalable Renyi
calculation, this shows that the capture cost is nonzero in the one-sided
barrier, while at this audited size it remains well below endpoint-label
entropy.

## 7. Verification

From the repository root run

```bash
python3 \
  phase2/loop/erdos838/agent_unit_matrix_asymptotic/verify_endpoint_span_localization.py
```

Expected first line:

```text
endpoint-span localization audit: PASS
```

The script independently validates reducedness, once-per-root completeness,
reflection betweenness, exact dyadic products at `t=1/2`, the full values at
`t=1`, the Hellinger/Renyi identity in rational form, every span cap in the
two test instances, the simultaneous endpoint-root record property, the
exact product-face decomposition and interior injection at both activities,
the universal and one-sided trace entropy/Jensen inequalities, and the
rational Pascal coordinates/general-position conditions.  It additionally
enumerates every temporal path pair/convex face in n58, Pascal36, and the
alternating family at `n=30`, checking the pointwise canonical-peeling
identity (10zg), its expected KL cost, and the radial extension first moment.
It finally verifies the exact `n=23` hereditary counterexample (10zia), so
the report's distinction between planar theorems and abstract entropy
barriers is mechanically enforced, and exhausts the small reflection classes
and deterministic random planar sample described above.
