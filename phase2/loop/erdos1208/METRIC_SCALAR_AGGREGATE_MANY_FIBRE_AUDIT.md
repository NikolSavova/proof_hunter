# Aggregate many-fibre audit for the large-area scalar core

## 1. Outcome

Summing over all clean fibres gives a useful exact incidence identity and a
clean aggregate reduction:

\[
 \boxed{
 \sum_q\mathcal M_{q,18}
 \le m^{o(1)}N\sum_q h_q+T_{\rm large}^{\rm agg}.}          \tag{1.1}
\]

Here `T_large^agg` is precisely the four-edge, squareclass-transverse part
with target doubled area

\[
 |2\det(v,v')|>{N\over h_q}.                    \tag{1.2}
\]

Thus the repeated-edge, squareclass-resonant, and adaptive low-area branches
all sum with no extra loss.

There is also a new endpoint theorem.  For one fixed clean fibre, the target
images of all source edges incident to one vertex are pairwise
vertex-disjoint.  Consequently

\[
 \boxed{
 \Delta(G_q)\le\left\lfloor{k-3\over2}\right\rfloor,
 \qquad
 h_q\le {k-2\over2}\left\lfloor{k-3\over2}\right\rfloor.} \tag{1.3}
\]

This is a real structural constraint, but it does not close (1.1).  An
explicit graph-and-label countermodel has a heavy `Theta(k^2)` source fibre,
injective disjoint clean partners satisfying the star-to-matching theorem,
and scalar energy a factor `Theta(k)` above the desired bound.  The model is
not a geometric counterexample: it deliberately omits the common vector
identity

\[
 e+f-c-d=q.                                      \tag{1.4}
\]

It proves that endpoint density, six-distinctness, injective partner edges,
ordinary BSG, and all graph-incidence moments are still insufficient.  The
remaining inverse must use the simultaneous linear equations (1.4), not
merely the fact that many endpoints are reused.

## 2. The clean incidence graph

Let `Sigma=A oplus A`, and identify a pair sum with its unique unordered
endpoint edge.  Define the incidence matrix

\[
 I(q,s)=1_{s\in H_q},
 \qquad q\in(A-A)^*,\ s\in\Sigma.               \tag{2.1}
\]

Write

\[
 h_q=\sum_s I(q,s),\qquad
 d(s)=\sum_q I(q,s),\qquad
 H=\sum_qh_q=\sum_sd(s).                        \tag{2.2}
\]

For two source edges put

\[
 c(s,s')=\sum_q I(q,s)I(q,s').                 \tag{2.3}
\]

Then

\[
 \sum_{s,s'}c(s,s')=\sum_qh_q^2,               \tag{2.4}
\]

and the exact fourth incidence moment is

\[
 \sum_{s,s'}c(s,s')^2
 =\sum_{q,q'}|H_q\cap H_{q'}|^2.               \tag{2.5}
\]

Equation (2.5) is just
`||I^T I||_F^2=||I I^T||_F^2`.  It is the natural place where a
many-fibre dependent-random-choice argument would have to enter.

The incidence has more structure than an arbitrary bipartite graph.  If
`I(q,s)=1`, then

\[
 s\in\Sigma,\qquad s+q\in\Sigma,
 \qquad q=a-b                                   \tag{2.6}
\]

for one ordered anchor edge `(a,b)`, and the source and target edges are
disjoint from each other and from the anchors.  For fixed `q`, the map

\[
 \tau_q:H_q\longrightarrow\Sigma,
 \qquad \tau_q(s)=s+q                          \tag{2.7}
\]

is injective.

## 3. Exact aggregate scalar-energy identity

Let

\[
 D=\delta(\Sigma),
 \qquad
 R_D(r)=\#\{(t,t')\in\Sigma^2:\delta(t)-\delta(t')=r\}.    \tag{3.1}
\]

Distance-Sidonicity makes `delta` injective, but its difference
representation function need not be small.  Expanding the scalar equation
and summing first over `q` gives the exact identity

\[
 \boxed{
 \sum_q\mathcal M_{q,18}
 =\sum_{s,s'\in\Sigma}
 c(s,s')
 R_D\left({\delta(s')-\delta(s)\over18}\right),}           \tag{3.2}
\]

where a nonintegral argument contributes zero.  Equivalently, if

\[
 S(z)=\sum_q
 \#\{(s,s')\in H_q^2:\delta(s)-\delta(s')=z\},            \tag{3.3}
\]

then

\[
 \sum_q\mathcal M_{q,18}
 =\sum_{r\in\mathbb Z}S(-18r)R_D(r).           \tag{3.4}
\]

The diagonal term is exactly `NH`.

To retain the large-area information, define

\[
 R_D(r,d)=\#\{(t,t'):\delta(t)-\delta(t')=r,
                    2\det(v_t,v_{t'})=d\}.     \tag{3.5}
\]

The Gaussian factorization in
`METRIC_SCALAR_CROSS_EDGE_DETERMINANT_BRANCH.md` gives, uniformly for
`(r,d)!=(0,0)`,

\[
 R_D(r,d)\le m^{o(1)}.                          \tag{3.6}
\]

Thus (3.2) has an exact refinement obtained by summing (3.5) over the
occupied signed areas.

## 4. Proof of the aggregate reduction

Put `H=sum_q h_q`.  The off-diagonal collisions with at most three distinct
edge labels contribute at most

\[
 4\sum_qh_q^2\le4NH,                            \tag{4.1}
\]

because `h_q<=N`.  The squareclass-resonant theorem contributes
`m^(o(1))NH` after summing over `q`.

For the transverse four-edge part with

\[
 |d|\le L_q:=\left\lfloor{N\over h_q}\right\rfloor,
\]

fix an ordered source pair.  Its radius difference fixes `r` in (3.5), and
there are at most `2L_q+1` signed areas.  Equation (3.6) gives

\[
\begin{aligned}
 T_{\rm low}^{\rm agg}
 &\le m^{o(1)}\sum_q(2L_q+1)h_q^2\\
 &\le3m^{o(1)}N\sum_qh_q
 =3m^{o(1)}NH.                                  \tag{4.2}
\end{aligned}

Everything not covered by (4.1), the resonant estimate, or (4.2) is exactly
`T_large^agg`.  This proves (1.1).

In particular, aggregation does not introduce a hidden factor equal to the
number of realized differences.  It also does not by itself gain anything:
if a heavy-fibre sum satisfies

\[
 \sum_{q:h_q>k}\mathcal M_{q,18}
 \ge K N\sum_{q:h_q>k}h_q,                     \tag{4.3}
\]

then weighted averaging gives one `q` with
`M_q>=KNh_q`.  A single bad fibre can dominate the aggregate.  Any genuine
many-fibre gain must use the intersections in (2.5), not just sum the local
inequalities.

## 5. Star-to-matching theorem

Fix `q=a-b` and let `G_q` be the graph on `A\setminus{a,b}` whose edges are
the source endpoint pairs represented by `H_q`.

**Theorem 5.1.**  If two different source edges of `G_q` share a vertex,
their target edges under `tau_q` are vertex-disjoint.

**Proof.**  Write the source edges as `{c,d_1}` and `{c,d_2}`.  Suppose their
targets share `x`, so they are `{x,y_1}` and `{x,y_2}`.  The common translate
identity gives

\[
 x+y_i-c-d_i=q\qquad(i=1,2).                   \tag{5.1}
\]

Subtracting yields

\[
 y_1-y_2=d_1-d_2.                               \tag{5.2}
\]

Vector-Sidonicity makes every nonzero ordered difference unique, hence
`(y_1,y_2)=(d_1,d_2)`.  Equation (5.1) now says `x-c=q=a-b`.
Uniqueness of the ordered difference `q` gives `(x,c)=(a,b)`, contradicting
the six-distinct clean condition.  \(\square\)

For a source star centered at `c`, all target edges are consequently
pairwise disjoint and avoid `a,b,c`.  They occupy `2deg_Gq(c)` different
vertices among only `k-3`, proving

\[
 \deg_{G_q}(c)\le\left\lfloor{k-3\over2}\right\rfloor.    \tag{5.3}
\]

Only `k-2` vertices can occur in the source graph, so summing degrees proves
(1.3).  Applying the same argument to `-q` gives the dual statement for
target stars.

This theorem is stronger than ordinary source density, but it points toward
a subtle obstruction: a source star is sent to a matching.  Endpoint reuse
on the source side is deliberately dispersed on the target side.

## 6. A graph countermodel surviving all immediate clean constraints

The following model shows that (2.2)--(2.7), injective labels, heavy endpoint
reuse, and Theorem 5.1 still do not imply the scalar bound.

Take an even `k_0` and a one-factorization

\[
 E(K_{k_0})=F_1\sqcup\cdots\sqcup F_{k_0-1},
 \qquad |F_i|=L=k_0/2.                          \tag{6.1}
\]

Use the first `r=floor(k_0/20)` factors as the abstract heavy source fibre

\[
 H=F_1\sqcup\cdots\sqcup F_r,
 \qquad h=rL=\Theta(k_0^2),                    \tag{6.2}
\]

and use all `N=binom(k_0,2)` edges as ordinary labels.

Choose integer block centers `M_i` such that all ordered weighted sums

\[
 M_i+18M_j                                      \tag{6.3}

are distinct.  Such centers of polynomial size exist by a greedy argument:
when adjoining the `j`-th center, only `O(j^3)` linear equalities are
forbidden.  Scale the centers by more than `19L`, and label the edges of
factor `F_i` by the interval

\[
 \{M_i,M_i+1,\ldots,M_i+L-1\}.                 \tag{6.4}

The labels are globally injective.  Distinct ordered block pairs have
disjoint charge ranges by (6.3).  Inside one block pair the energy is

\[
\begin{aligned}
 E_L
 &=\#\{x+18y=x'+18y':0\le x,x',y,y'<L\}\\
 &=\sum_{|j|\le(L-1)/18}(L-18|j|)(L-|j|)
 =\Theta(L^3).                                  \tag{6.5}
\end{aligned}

Therefore the full source/ordinary energy is

\[
 r(k_0-1)E_L
 =\Theta(hNL)
 =\Theta(k_0hN),                                \tag{6.6}

a linear-factor violation of the desired near-diagonal estimate.

One can also install an injective abstract clean partner map

\[
 \tau:H\longrightarrow E(K_{k_0})              \tag{6.7}

such that

1. `tau(e)` is disjoint from `e`; and
2. if two source edges share a vertex, their target edges are disjoint.

A greedy construction suffices.  When assigning one source edge, it has at
most `2r` previously assigned adjacent edges.  Their target edges forbid
fewer than `4rk_0` candidates; injectivity and disjointness from the source
forbid only another `O(rk_0+k_0)`.  For `r<=k_0/20`, this is smaller than
`binom(k_0,2)` for all sufficiently large `k_0`.

Thus the model has a `Theta(k^2)` source fibre, all endpoint labels, an
injective six-distinct partner decoration, and the exact star-to-matching
property.  Each additive block is nevertheless a perfect matching, so no
single structured block reuses an endpoint.

This is **not** a geometric counterexample.  Its arbitrary labels need not
be squared norms, and its partner map need not solve the common vector
system (1.4).  Its role is decisive but negative: no theorem about abstract
endpoint graphs or BSG blocks can close the scalar gate.

## 7. The common-translation equations are the remaining leverage

For a genuine matching block `F` inside one clean fibre, summing (1.4) over
its edges gives

\[
 \sum_{\{c,d\}\in F}(e_{cd}+f_{cd})
 -\sum_{\{c,d\}\in F}(c+d)
 =|F|q.                                         \tag{7.1}

If `F` is a perfect matching, the second sum is simply `sum_(x in A)x`.
For two large matching blocks, subtracting their versions of (7.1) produces
a nontrivial integer linear relation among target endpoint multiplicities.
The graph countermodel has no reason to satisfy any of these relations.

Equivalently, a proposed partner map `tau` gives a design matrix with rows

\[
 e_c+e_d-e_e-e_f,                              \tag{7.2}
\]

and a genuine realization requires both coordinate vectors of `A` to solve
the same inhomogeneous system with right side `-q`.  When `h>>k`, this is a
highly overdetermined rank condition.  The finite-field parabola and ruler
families show that low-rank exceptional systems do exist; what is missing is
a theorem that *simultaneous scalar-energy concentration* forces such a
system either into a proved ruler/module branch or into two equal endpoint
norms.

This is a substantially narrower restart target than generic endpoint DRC:

> extract many matching-like scalar blocks while retaining enough common
> translate equations (7.2) to obtain a low-rank endpoint module, then apply
> the sharp height or repeated-norm obstruction.

## 8. Exact verification

The companion verifier checks:

* the codegree identity (3.2) against direct aggregate scalar energy;
* the complete collision partition into diagonal, repeated, resonant,
  transverse-low-area, and transverse-large-area rows;
* Theorem 5.1 for every clean fibre tested;
* the one-factorization countermodel, its polynomial-size weighted-Sidon
  centers, its exact energy, and its greedy clean partner.

The exact aggregate profiles are

\[
\begin{array}{c|r|r|r|r|r|r}
\text{family}&H&NH&\sum_q\mathcal M_q&
\text{repeated}&T_{\rm low}&T_{\rm large}\\ \hline
\text{closure }20&648&123120&124562&22&190&1230\\
\text{parabola image }17&2088&283968&284024&0&0&56
\end{array}
\]

For the finite graph model with 64 non-anchor vertices,

\[
 (h,N,hN,\mathcal M,N(h+k),\max\Phi^{-1})
 =(288,2016,580608,1072764,713664,2).            \tag{8.1}
\]

Even maximum load two is enough to violate the weak target because the
off-diagonal collisions occur coherently across every ordered block pair.

Run

```text
python3 phase2/loop/erdos1208/verify_metric_scalar_aggregate_many_fibre_audit.py
```

## 9. Verdict

Aggregation cleanly preserves all proved scalar reductions, but it does not
automatically amplify a quotient-energy excess beyond the endpoint scale.
A single bad heavy fibre can dominate, and even a dense source graph may
decompose into additive perfect matchings.

The durable positive result is the star-to-matching theorem and the exact
incidence formula (3.2).  The durable barrier is the one-factorization model:
endpoint incidence plus abstract clean partners remains insufficient by a
linear factor.  The next proof attempt must retain the common vector
translation in many BSG blocks and exploit the rank of the design system
(7.2).  Without that linear structure, a many-fibre inverse is false.
