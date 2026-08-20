# A polynomial-height counterexample to the synchronized fixed-wedge dyadic gate

## 1. Verdict

The proposed geometric reciprocal-tail estimate

\[
 \boxed{\mathcal R_K(w)\le m^{o(1)}{k^4\over K^2}}     \tag{1.1}
\]

is false, even with every clean affine equation, the literal extension
indicator `Xi_K`, the rigid good-start pencil, the exact scalar selector,
and determinant cutoff `L=N` retained.

There are polynomial-height integral distance-Sidon sets with one physical
metric wedge `w` and one dyadic band `K` for which

\[
 K=\Theta(k^2),\qquad
 \boxed{\mathcal R_K(w)=\Omega(k^3).}                  \tag{1.2}
\]

The construction starts from a polynomial-span collinear Golomb ruler.
Triple-sum collisions force an ordered source pair with quadratic common
clean codegree.  The general endpoint-wedge inequality then forces cubic
one-role mass, and the codegree is so large that the exact `Xi_K`
transversality requirement deletes only a lower-order part.  A seven-point
off-line gadget makes this same source pair visible to one
determinant-qualified physical wedge without changing the asymptotics.

This counterexample does **not** refute the aggregate synchronized-pair
target.  Dyadic reversibility gives at the selected wedge

\[
 \Phi_{2,L,K}(w)\asymp K^2\mathcal R_K(w)=\Omega(k^7), \tag{1.3}
\]

while the global allowance is

\[
 Nk^5=\Theta(k^7).                                      \tag{1.4}
\]

Thus one collinear clean core can concentrate essentially the entire
global budget at a single physical wedge.  What is killed is precisely the
pointwise fixed-wedge theorem and every local `K^(-2)` reciprocal tail.
The aggregate theorem remains possible but must explicitly permit such
single-wedge concentration.

## 2. Dense Golomb rulers have fourth-power clean mass

For every large `n`, take an integer Golomb ruler

\[
 B=\{b_1,\ldots,b_n\}\subset[0,Cn^2]                  \tag{2.1}
\]

with absolute `C`.  The standard finite-field construction used by
`dense_ruler` gives one explicitly: if `p` is the first prime at least
`n`, the marks

\[
 b_j=2pj+(j^2\bmod p),\qquad 0\le j<n,                 \tag{2.2}
\]

have distinct positive differences and span `O(n^2)`.

Put the points `(b,0)` on the horizontal axis.  They form a
distance-Sidon set.  Golomb uniqueness also gives unique unordered pair
sums: an equality `a+b=c+d` would give the repeated directed difference
`a-c=d-b` unless the pairs were identical.

There are

\[
 M={n\choose3}=\Theta(n^3)                              \tag{2.3}
\]

unordered triples, while their integer sums occupy only `O(n^2)` values.
If `r_x` is the number of triples of sum `x`, Cauchy--Schwarz gives

\[
 \sum_x{r_x\choose2}
 \ge {M^2\over O(n^2)}-{M\over2}
 =\Omega(n^4).                                         \tag{2.4}
\]

Two distinct triples of equal sum are disjoint: after deleting a shared
point they would give two equal pair sums.  Hence every collision in (2.4)
is six-distinct.  Choosing one distinguished endpoint in each triple and
both orientations produces eighteen clean starts.  Therefore

\[
 \boxed{H:=\sum_qh_q=\Omega(n^4).}                     \tag{2.5}
\]

All these are literal clean fibres in the sense used by the synchronized
gate, not unrestricted triple-sum energy.

## 3. A quadratic common-clean codegree

Let `Sigma` be the `N=binom(n,2)` source pair sums and define

\[
 c(s,t)=|\{q:s,t\in H_q\}|.                             \tag{3.1}
\]

There is an exact second-moment switch

\[
 \sum_{s,t\in\Sigma}c(s,t)=\sum_qh_q^2.                \tag{3.2}
\]

There are at most `n(n-1)<n^2` active nonzero translations.  Equations
(2.5) and Cauchy give

\[
 \sum_qh_q^2\ge {H^2\over n^2}=\Omega(n^6).           \tag{3.3}
\]

The diagonal contribution to (3.2) is exactly

\[
 \sum_s c(s,s)=H=O(n^4),                               \tag{3.4}
\]

because `h_q<=N`.  Since there are fewer than `N^2=O(n^4)` ordered
off-diagonal pairs, (3.2)--(3.4) force distinct starts `s,t` with

\[
 \boxed{c(p)=c(s,t)\ge\alpha n^2}                      \tag{3.5}
\]

for an absolute `alpha>0` depending only on the span constant in (2.1).

This is the key geometric fact missed by graph-only stresses: a dense
torsion-free Golomb ruler has enough exact equal-triple closure to create a
quadratic literal common-translation codegree.

## 4. Cubic `Xi_K`-qualified one-role mass

For `q in Q_p`, form the two simple target-edge graphs

\[
 e_0(q)=E(s+q),\qquad e_1(q)=E(t+q).                    \tag{4.1}
\]

Let `O(p)` count unordered translation pairs which are endpoint wedges in
exactly one role.  The simultaneous-overlap classification gives one
replacement pencil of size `rho(p)<=n-2`, and the exact endpoint-degree
inequality is

\[
 O(p)\ge {4c(p)^2\over n}-2c(p)-\rho(p)(\rho(p)-1).    \tag{4.2}
\]

Inserting (3.5) and `rho<=n-2` yields

\[
 \boxed{O(p)=\Omega(n^3).}                             \tag{4.3}
\]

Now retain the full transverse-extension predicate.  Relative to any
one-role base, at most `15n-36` translations have an anchor endpoint in
the four base-anchor points, a good target endpoint in the three-point
good union, or a bad target endpoint in the four-point bad union.  Hence

\[
 T_p(b)\ge c(p)-(15n-36).                               \tag{4.4}
\]

For large `n`, (3.5) makes the right side at least `c(p)/2`.  Every
one-role base in (4.3) is therefore transverse-rich, with the literal
indicator `Xi_K=1`.  Thus

\[
 R(p)=O(p)=\Omega(n^3).                                 \tag{4.5}
\]

This step is genuinely geometric: `c(p)` comes from the exact clean
fibres of the Golomb ruler, and (4.4) uses the actual anchor and target
endpoint roles.  No indexed-graph relaxation is inserted.

## 5. The seven-point metric-wedge gadget

It remains to make `p` visible to one noncollinear physical wedge.  Scale
the Golomb core by `6z`, where `z` is an integer polynomial in `n`.  If

\[
 \Delta_0=\delta(s)-\delta(t)\ne0                       \tag{5.1}
\]

before scaling, then afterward

\[
 r=-{36z^2\Delta_0\over18}=-2z^2\Delta_0              \tag{5.2}
\]

is a nonzero even integer.

For `v in {1,3}`, put

\[
 X_v={r+v^2+1\over2},\qquad
 u_v={r+v^2-1\over2}.                                  \tag{5.3}
\]

These are integers and obey

\[
 X_v^2-(u_v^2+v^2)=r.                                  \tag{5.4}
\]

Take one point `O`, the two first edges with vectors `(X_1,0)` and
`(X_3,0)`, and two independently translated partner edges with vectors
`(u_1,1)` and `(u_3,3)`.  This uses seven points.  Both first edges share
`O`, and (5.4) gives the common shift `r`.  Moreover

\[
 X_1^2-X_3^2
 =(u_1^2+1)-(u_3^2+9),                                 \tag{5.5}
\]

so the two partners form exactly the partner pair required by the fixed
wedge.  Their doubled cross determinants are

\[
 2X_1,qquad6X_3.                                       \tag{5.6}
\]

Choosing `z` polynomially large makes both exceed the final
`N'=binom(n+7,2)`.  The fixed-wedge scalar selector then satisfies

\[
 V_w(p)=1                                               \tag{5.7}
\]

at cutoff `L=N'`.

The core and gadget can be joined at polynomial height.  First choose `z`
outside the polynomially many roots which identify two forced internal
distance labels.  Then choose the relative core translation and the two
partner-edge centres outside the polynomially many nonzero linear or
quadratic equations which create a point collision, repeated distance, or
unintended pair sum.  The grid nonvanishing lemma gives integer choices of
size `n^(O(1))`.  Thus the union is a genuine integral distance-Sidon set
with `m=n^(O(1))`.

All old clean rows remain clean.  Adding seven points creates only

\[
 {n+7\choose2}-{n\choose2}=7n+21                       \tag{5.8}
\]

new pair sums.  A translation newly entering `Q_p` must use a new target
pair sum in at least one of the two source roles; each new pair sum fixes
that translation in each role.  Thus the final codegree `c'(p)` exceeds
the core codegree by at most `2(7n+21)=O(n)`.  The old transverse pools in
(4.4) still have size at least `c'(p)/2` for large `n`.  Hence all
`Omega(n^3)` old bases remain counted after the union.

Choose the dyadic band start `K` with

\[
 K\le c'(p)<2K.                                        \tag{5.9}
\]

Then `K=Theta(n^2)`, while the final point count is `k=n+7`.  Equations
(4.5), (5.7), and (5.9) give

\[
 \mathcal R_K(w)\ge R(p)=\Omega(k^3),
 \qquad {k^4\over K^2}=O(1).                           \tag{5.10}
\]

Since `m^(o(1))=k^(o(1))` at polynomial height, (5.10) disproves (1.1).

Finally, dyadic reversibility shows why the aggregate theorem survives:

\[
 \Phi_{2,N',K}(w)
 \ge {K^2\over16}\mathcal R_K(w)
 =\Omega(k^7)=\Theta(N'k^5).                           \tag{5.11}
\]

The example is a sharp concentration model, not an aggregate excess.

## 6. Exact certificate

The verifier uses the 60-mark Ruzsa Golomb ruler obtained from `p=61` and
primitive root `2`, scales it by six, and installs the seven-point gadget.
The resulting 67-point set has all 2,211 squared distances and pair sums
distinct.  Its exact profile is

\[
\begin{array}{c|r}
\text{quantity}&\text{value}\\ \hline
k,N&67,\ 2,211\\
H&1,322,406\\
\sum_qh_q^2&516,142,658\\
\sum_{s\ne t}c(s,t)&514,820,252\\
c(p)&320\\
O(p),R(p)&6,169,\ 6,169\\
\min T_p(b),\max T_p(b)&182,\ 245\\
B_2(p)&139,373,896\\
K&268\\
r&-2,673,600\\
\text{two doubled determinants}&2,673,598,\ 8,020,770
\end{array}                                             \tag{6.1}
\]

In particular

\[
 {R(p)K^2\over k^4}=21.987\ldots,qquad
 {B_2(p)\over k^4}=6.91\ldots.                         \tag{6.2}
\]

These constant finite ratios are only a certificate shadow; the proof
above gives the polynomial asymptotic separation.  The verifier checks the
Ruzsa modular Sidon property, integer Golomb property, global distance and
pair-sum uniqueness, every clean fibre, the maximum codegree, every
one-role and `Xi_K` condition, the exact synchronized mass, the scalar
orientation, both determinant tests, and the physical partner-gap identity.

Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_synchronized_fixed_wedge_dyadic_golomb_counterexample.py
```

## 7. Consequence for the proof architecture

The synchronized higher-pooling identity remains valid, but it cannot be
localized by a uniform `k^4` bound at each physical wedge, even after
dyadic codegree decomposition.  Dense collinear Golomb cores are the exact
obstruction: their `Omega(k^4)` clean mass produces a quadratic common
codegree, and one off-line wedge can expose its whole cubic one-role base
population.

The live replacement for (1.1) must be global.  It should either charge a
high fixed-wedge value against a correspondingly small family of physical
wedges, or classify and pay the dense-Golomb/collinear clean core directly.
The correct scale must allow one wedge of size `Theta(Nk^5)`; any theorem
which spreads that budget uniformly over the `Theta(Nk)` physical wedges
is false.
