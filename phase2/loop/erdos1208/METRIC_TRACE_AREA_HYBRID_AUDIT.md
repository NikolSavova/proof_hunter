# Trace--area hybrid audit for the metric scalar charge

## 1. Verdict

Let `U` be the canonically oriented edge-vector set of a distance-Sidon
configuration, and let `U_q subset U` be the vectors belonging to a clean
fibre.  Write

\[
 |U|=N=\binom k2,\qquad |U_q|=h.
\]

For a record `(u,v) in U_q times U`, define

\[
 T(u,v)=|u|^2+18|v|^2,
 \qquad \Omega(u,v)=\det(u,v).                 \tag{1.1}
\]

The joint key is arithmetically almost injective:

\[
 \boxed{
 \max_{t,a}|\{(u,v):T(u,v)=t,\ \Omega(u,v)=a\}|
 \le m^{o(1)}.}                                \tag{1.2}
\]

More precisely, if `R=t^2-72a^2>0`, the load is at most `2 tau(R)`; if
`R=0`, it is at most one.  Consequently the joint collision energy is

\[
 \boxed{\mathcal E_{T,\Omega}\le m^{o(1)}hN.}  \tag{1.3}
\]

This is an exact theorem, but it does **not** imply that either marginal
energy is near diagonal.  There are abstract radial-transversal products
`U_q=U` for which

\[
 \mathcal E_{T,\Omega}\le m^{o(1)}|U|^2
\]

while simultaneously

\[
 \boxed{
 \min(\mathcal E_T,\mathcal E_\Omega)
 \ge m^{2-o(1)}|U|^2.}                         \tag{1.4}
\]

Thus joint divisor multiplicity, Cartesian-product structure, integrality,
the support box, and one vector per squared radius are insufficient by a
full power-scale factor.  A hybrid proof remains possible only if actual
endpoint factorization and the clean pair-sum translate force a projection
dichotomy which the radial model lacks.

The exact genuine profiles are highly asymmetric: trace energy stays close
to diagonal while area energy can be enormous, and the joint map is almost
injective.  This supports the still-live trace charge but supplies no new
proof of it.

## 2. Why a marginal minimum theorem would solve the problem

Let

\[
 \mathcal E_T=\sum_t L_T(t)^2,
 \qquad
 \mathcal E_\Omega=\sum_a L_\Omega(a)^2,       \tag{2.1}
\]

where `L_T,L_Omega` are the two marginal loads of the `hN` records.
The trace energy `E_T` is exactly the metric scalar energy
`M_(q,18)` from `METRIC_SCALAR_PAIR_SUM_CHARGE.md`.

Both keys have only `O(m^2)` possible values: `1<=T<=38m^2`, while
`|Omega|<=2m^2`.  Hence either estimate

\[
 \mathcal E_T\le m^{o(1)}N(h+k)
 \quad\hbox{or}\quad
 \mathcal E_\Omega\le m^{o(1)}N(h+k)           \tag{2.2}
\]

gives the usual charge amplification.  When `h>k`, Cauchy--Schwarz gives

\[
 (hN)^2\le O(m^2)m^{o(1)}hN,
 \qquad h\le {m^{2+o(1)}\over N}.              \tag{2.3}
\]

Fibres with `h<=k` are covered by the standard `+k` correction.  Therefore
the single dichotomy

\[
 \boxed{
 \min(\mathcal E_T,\mathcal E_\Omega)
 \le m^{o(1)}N(h+k)}                           \tag{2.4}
\]

would imply the cube-root upper bound in Erdos problem 1208.

Section 4 proves that (2.4) cannot follow from the joint theorem and radial
uniqueness alone.

## 3. Exact joint multiplicity

### Theorem 3.1

Let `V,W subset Z^2` be finite sets such that squared norm is injective on
each set.  For fixed integers `t,a`, put

\[
 \nu(t,a)=|\{(u,v)\in V\times W:
 |u|^2+18|v|^2=t,\ \det(u,v)=a\}|.             \tag{3.1}
\]

If `R=t^2-72a^2>0`, then

\[
 \boxed{\nu(t,a)\le2\tau(R).}                 \tag{3.2}
\]

If `R=0`, then `nu(t,a)<=1`.

### Proof

For a record counted by (3.1), set

\[
 x=|u|^2,\qquad y=|v|^2,\qquad z=u\cdot v,
 \qquad p=x-18y.                               \tag{3.3}
\]

The Gram identity `xy-z^2=det(u,v)^2` gives

\[
 \boxed{
 t^2-72a^2=p^2+72z^2.}                        \tag{3.4}
\]

Conversely, `t,p` recover the two norm labels:

\[
 x={t+p\over2},\qquad y={t-p\over36}.         \tag{3.5}
\]

Norm injectivity then recovers `u` from `x` and `v` from `y`.  Thus distinct
records in one joint cell inject into the integer representations

\[
 p^2+72z^2=R.                                  \tag{3.6}
\]

These form a subset of the representations

\[
 p^2+2w^2=R                                    \tag{3.7}
\]

obtained by putting `w=6z`.  The classical exact formula is

\[
 r_{X^2+2Y^2}(R)
 =2\sum_{d\mid R}\chi_{-8}(d),                \tag{3.8}
\]

so its absolute value is at most `2 tau(R)`.  This proves (3.2).  If
`R=0`, (3.4) forces `p=z=0`; equations (3.5) and norm injectivity leave at
most one record.  QED.

For edge vectors in an `m` by `m` box, `t<=38m^2` and hence
`0<=R<=1444m^4`.  The uniform divisor bound gives (1.2), and summing
`load^2 <= (max load) load` gives (1.3).

The theorem uses signed determinant.  Replacing it by absolute determinant
changes the bound by at most a factor two.

## 4. A sharp radial-transversal no-go

Let

\[
 \mathcal R_m={|w|^2:
 w\in[-m,m]^2\cap\mathbb Z^2,\ w\ne0\}.
\]

The number of lattice vectors is `Theta(m^2)`, while every radius has at
most `m^(o(1))` representations by the two-squares divisor bound.  Hence

\[
 n:=|\mathcal R_m|=m^{2-o(1)}.                 \tag{4.1}
\]

Choose one vector of every squared radius and call the resulting set `U`.
Put `U_q=U`.  This formal model has exactly the radial uniqueness and
Cartesian-product inputs of Theorem 3.1.

There are `Q=n^2` records.  The trace has at most `38m^2+1` values, so
Cauchy--Schwarz gives

\[
 \mathcal E_T\ge {n^4\over38m^2+1}.           \tag{4.2}
\]

The determinant has at most `4m^2+1` values, and therefore

\[
 \mathcal E_\Omega\ge {n^4\over4m^2+1}.       \tag{4.3}
\]

Together with (4.1),

\[
 \min(\mathcal E_T,\mathcal E_\Omega)
 \ge m^{2-o(1)}Q,                              \tag{4.4}
\]

whereas Theorem 3.1 gives

\[
 \mathcal E_{T,\Omega}\le m^{o(1)}Q.          \tag{4.5}
\]

This proves (1.4).  If one wants the formal edge count to be exactly
`binom(k,2)`, retain any triangular number of radii below `n`; one can take
`k=m^{1-o(1)}`, so the same exponents hold.

The obstruction is not a genuine endpoint configuration, and `U_q=U`
need not be a clean fibre.  Those are precisely the two remaining sources
of possible leverage.  The conclusion is scoped but decisive: no matrix
inequality using only bounded joint cells and the two marginal ranges can
prove (2.4).

## 5. Exact profiles

For each genuine family, the verifier uses either its largest clean fibre
or the certified two-arm fibre.  It reports the three energies normalized
by the record count `Q=hN`:

\[
\begin{array}{c|c|c|c|c}
\text{family}&\mathcal E_T/Q&\mathcal E_\Omega/Q
 &\mathcal E_{T,\Omega}/Q&\max L_{T,\Omega}\\ \hline
\text{closure }30&1.04138&2.36552&1&1\\
\text{closure }120&1.12904&4.39652&1.000002&2\\
\text{perpendicular ruler }40&1.00165&802.532&1.000183&2\\
\text{Costas }22&1.06723&23.7731&1.000255&2\\
\text{parabola image }43&1.01762&113.888&1.000363&2\\
\text{integer parabola }50&1.01199&57.5108&1.000109&2\\
\text{two-arm }50&1.00203&34577.0&1.000578&2
\end{array}                                                    \tag{5.1}
\]

The area collapse is expected on one-dimensional pieces: many parallel
records have determinant zero.  Trace separates them through the positive
binary form in the squared lengths.  The joint key then separates almost
every remaining record.

For the formal radial transversal, the normalized exact profiles are

\[
\begin{array}{c|r|c|c|c|c}
m&n&\mathcal E_T/Q&\mathcal E_\Omega/Q
 &\mathcal E_{T,\Omega}/Q&\max L_{T,\Omega}\\ \hline
8&41&1.63058&46.9465&1.00833&2\\
20&197&5.00933&191.551&1.03035&4\\
40&686&14.5217&573.062&1.03542&5
\end{array}                                                    \tag{5.2}
\]

Thus the joint theorem is already nearly sharp on finite radial models,
while the smaller marginal excess grows steadily and is forced to be
polynomial asymptotically.

Run

```text
python3 phase2/loop/erdos1208/verify_metric_trace_area_hybrid_audit.py
```

for the exact identities, quadratic-form representation formula, genuine
profiles, and radial no-go certificates.

## 6. Research consequence

The hybrid invariant contributes one rigorous fact: simultaneous trace and
area determine a record up to divisor multiplicity.  It does not by itself
improve the scalar trace gate, because projection can create large energy
in both coordinates even when the joint map is injective.

A viable continuation would need an endpoint theorem of the following very
specific kind:

> If both marginal energies in (2.1) are polynomially above diagonal, then
> the induced trace--area incidence graph contains a structured rectangle
> whose four edge vectors cannot all arise from one distance-Sidon endpoint
> set with the first vectors in a single clean pair-sum fibre.

The radial transversal proves that the final endpoint clause is essential.
Without such a rectangle-to-endpoint contradiction, the hybrid is a useful
diagnostic coordinate system rather than a solution gate.
