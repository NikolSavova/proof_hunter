# An adaptive trace--area endpoint charge

## 1. Outcome

Fix a clean fibre `H_q` of size `h`, and let `U_q` and `U` be its
canonically oriented source edge vectors and the full oriented edge-vector
set.  Thus

\[
 |U_q|=h,\qquad |U|=N=\binom k2.
\]

For a record `(u,v) in U_q times U`, retain both

\[
 T(u,v)=|u|^2+18|v|^2,
 \qquad A(u,v)=\det(u,v).                                  \tag{1.1}
\]

Each coordinate has only `O(m^2)` possible integer values.  Instead of
requiring one marginal to have small energy, send every record through the
less loaded of its two marginal cells.  This gives an exact adaptive charge
whose energy is bounded by

\[
 \boxed{
 \mathcal B_q=
 \sum_{(u,v)\in U_q\times U}
 \min\{L_T(T(u,v)),L_A(A(u,v))\}.}                         \tag{1.2}
\]

Here `L_T,L_A` are the full marginal loads.  The pointwise estimate

\[
 \boxed{\mathcal B_q\le m^{o(1)}N(h+k)}                    \tag{1.3}
\]

would prove the cube-root upper bound.  It is strictly weaker than either
trace- or area-energy control and survives every genuine stress presently
available, including the sums-of-two-squares planting, the resonant
two-arm family, and the champion affine parabola.

This note does not prove (1.3).  Its durable new result is a sharp inverse:
because a joint `(T,A)` cell is divisor-small, a polynomial failure of
(1.3) forces a polynomial-minimum-degree bipartite graph of trace and area
values.  Thus the remaining theorem is no longer a marginal-energy
dichotomy; it is an endpoint-realized dense-support exclusion.

## 2. The selected charge and its energy

Let

\[
 L_T(t)=|\{(u,v):T(u,v)=t\}|,
 \qquad
 L_A(a)=|\{(u,v):A(u,v)=a\}|.                              \tag{2.1}
\]

For each record choose route `0` if `L_T(T)<=L_A(A)`, and route `1`
otherwise.  Its key is respectively `(0,T)` or `(1,A)`.  The two route
universes are disjoint.  If `nu` denotes selected-key load, then record by
record

\[
 \nu(\text{selected key})
 \le\min\{L_T(T),L_A(A)\}.
\]

Summing over records proves

\[
 \boxed{\mathcal E_q^{\rm sel}:=\sum_z\nu(z)^2
 \le\mathcal B_q.}                                        \tag{2.2}
\]

The trace lies in an interval of at most `38m^2+1` integers, and signed
area has at most `4m^2+1` values.  Hence the selected charge uses at most
`42m^2+2` keys.  Cauchy--Schwarz gives

\[
 (hN)^2\le(42m^2+2)\mathcal E_q^{\rm sel}
 \le(42m^2+2)\mathcal B_q.                                \tag{2.3}

For `h>k`, (1.3) therefore gives `hN<=m^(2+o(1))`.
Fibres with `h<=k` contribute at most `k^3` clean starts in total.  Summing
the heavy-fibre conclusion over the at most `k(k-1)` realized differences
gives the ambient equal-centroid bound and hence `k<=m^(2/3+o(1))`.

There is also an aggregate version.  If `Q={q:h_q>k}` and

\[
 \sum_{q\in Q}\mathcal B_q
 \le m^{o(1)}N\sum_{q\in Q}h_q,                            \tag{2.4}
\]

then summing (2.3), followed by Cauchy over `|Q|<=k^2`, gives

\[
 \sum_{q\in Q}h_q\le m^{2+o(1)}.                          \tag{2.5}

Together with the light fibres this again proves the required bound.

## 3. Joint cells are divisor-small

Put

\[
 \mu(t,a)=|\{(u,v):T(u,v)=t,A(u,v)=a\}|,
 \qquad D_q=\max_{t,a}\mu(t,a).                            \tag{3.1}
\]

The trace--area theorem in `METRIC_TRACE_AREA_HYBRID_AUDIT.md` proves

\[
 \boxed{D_q\le m^{o(1)}.}                                  \tag{3.2}
\]

For completeness, put

\[
 x=|u|^2,\quad y=|v|^2,\quad z=u\cdot v,\quad p=x-18y.
\]

Then

\[
 t^2-72a^2=p^2+72z^2.                                     \tag{3.3}

Fixing `(t,a)` leaves divisor-many `(p,z)`.  The value `p` recovers
`x=(t+p)/2` and `y=(t-p)/36`; distance-Sidonicity makes each norm recover
its unique edge.  More precisely `D_q<=2 tau(t^2-72a^2)` away from the
zero-discriminant case, where the load is at most one.

The joint theorem alone did not control either marginal.  The adaptive
charge uses it differently: it shows that large load on both available
routes must come from a dense *support graph* rather than parallel records
inside a few joint cells.

## 4. The dense-support inverse

Form a simple bipartite graph `G_q`.  Its left vertices are occupied trace
values, its right vertices are occupied area values, and `(t,a)` is an edge
when `mu(t,a)>0`.  Write `d_T(t),d_A(a)` for its simple degrees, `M` for its
number of edges, and

\[
 W(G_q)=\sum_{(t,a)\in E(G_q)}\min\{d_T(t),d_A(a)\}.        \tag{4.1}
\]

Since every joint multiplicity is at most `D_q`, weighted marginal loads
are at most `D_q` times simple degrees.  Therefore

\[
 \boxed{
 \mathcal B_q\le D_q^2 W(G_q).}                            \tag{4.2}
\]

The following elementary lemma turns (4.2) into a quantitative inverse.

### Lemma 4.1 (minimum-degree extraction)

Every finite graph `G` with `M>=1` edges contains a nonempty subgraph of
minimum degree at least

\[
 {W(G)\over4M(1+\lceil\log_2M\rceil)}.                    \tag{4.3}
\]

### Proof

Partition edges dyadically according to
`2^j<=min(d(x),d(y))<2^(j+1)`.  For some `j`,

\[
 2^j|E_j|\ge {W(G)\over2(1+\lceil\log_2M\rceil)}.          \tag{4.4}
\]

There are at most `2M/2^j` vertices of global degree at least `2^j`.
The subgraph induced by those vertices contains `E_j`, so its average
degree is at least the right side of (4.3) multiplied by two.  Iteratively
delete vertices below half this average degree.  Not all vertices can be
deleted, and the surviving subgraph has the claimed minimum degree.  QED.

Let `Q_q=hN` be the number of records.  Since `M<=Q_q`, (4.2)--(4.3) imply:

\[
 \boxed{
 \mathcal B_q\ge KQ_q
 \Longrightarrow
 G_q\text{ contains a subgraph of minimum degree }
 \ge {K\over4D_q^2(1+\lceil\log_2Q_q\rceil)}.}             \tag{4.5}

Thus a `k^epsilon` violation of the adaptive gate forces a
`k^(epsilon-o(1))`-minimum-degree patch of trace and signed-area values.
Every support edge in this patch still carries a record `(u,v)`, with `u`
an edge of one clean common-translation fibre.  Abstract radial
transversals have such dense patches.  On the tested genuine systems the
joint multiplicity is at most two, and even the largest minimum of the two
support degrees at an occupied cell is only six.  The missing theorem is to
exclude a polynomial dense patch using the clean partner equation

\[
 e+f-c-d=q.                                                \tag{4.6}

One support rectangle is not itself a contradiction.  The 43-point
parabola support has exactly eight `4`-cycles.  Four use eight different
source/ordinary edge labels, and two of those use fourteen different point
endpoints among the eight edges.  Thus even an almost completely
endpoint-disjoint trace--area rectangle is genuinely realizable.  The
future endpoint theorem must use polynomial minimum degree, many coupled
rectangles, or a higher-girth dense patch; it cannot stop at one local
cycle.

## 5. Why the known counterfamilies do not kill the charge

### Local sums-of-two-squares planting

The planted construction controls only `h=Theta(k)` clean edges and an
`O(k)` ordinary-edge subsystem.  Its deliberate trace collisions cost at
most `h^(3+o(1))=Theta(Nh)`.  The free centers can be chosen, by the same
polynomial-avoidance argument used to make the ambient set distance-Sidon,
to avoid every other nonidentical trace equality outside the controlled
labels.  (The forced determinant-zero records are harmless because their
trace labels are distinct.)  Hence already the trace route, and therefore
the adaptive charge, has

\[
 \mathcal B_q=m^{o(1)}Nh.                                  \tag{5.1}

The deterministic 98-point certificate is even closer to diagonal:
`Q_q=114072`, `B_q=114231`, and selected energy `114230`.

### Ruler arms and the two-arm vector barrier

On collinear or parallel-line blocks, signed area can collapse completely,
but trace is a positive binary quadratic form and has divisor-scale load.
The resonant two-arm family which disproves the Gaussian vector charge has,
at side 50,

\[
 {\mathcal B_q\over N(h+k)}=0.53317\ldots.                 \tag{5.2}

Thus the adaptive rule automatically takes the trace route on the area-zero
resonance.

### Parabola stresses

On the transformed 43-point parabola, `h=171`, `N=903`.  The original
metric has selected energy `157131`; the champion affine metric has
`158367`.  Their respective weak budgets are `193242` and the same
`193242`.  The support-cell multiplicity is at most two.

## 6. Endpoint-free barrier

The endpoint clause in (4.6) is indispensable.  Take one lattice vector of
every occupied squared radius in an `m`-box and use the same radial
transversal for `U_q` and `U`.  This has norm injectivity and the joint
divisor bound, but need not be a complete edge set or clean fibre.

For transversal sides `8,20,40,80`, the normalized adaptive envelopes
`B_q/(|U_q||U|)` are

\[
 1.6305\ldots,\quad5.0011\ldots,\quad
 14.4949\ldots,\quad46.1324\ldots.                         \tag{6.1}

At side 80 the minimum of the two simple support degrees reaches 105.
The growth is forced asymptotically by the `O(m^2)` marginal ranges.
Therefore (1.3) cannot follow from radial uniqueness, joint multiplicity,
integrality, or Cartesian-product structure alone.

## 7. Status

The adaptive trace--area charge is a strictly smaller and more
endpoint-compatible target than the scalar large-area excess.  It absorbs
exactly the two complementary pathologies seen so far: trace handles ruler
and parallel resonance, while area can separate deliberately planted trace
classes.  Its failure has the concrete inverse certificate (4.5).

What remains unproved is the endpoint theorem:

> a polynomial-minimum-degree trace--area support patch cannot be realized
> by `U_q times U` when `U` is the complete edge-vector set of one
> distance-Sidon configuration and `U_q` carries the clean translation
> decoration (4.6).

This is narrower than the previous request to bound all large signed areas,
but it is still a genuine new theorem, not a consequence of the present
divisor estimates.

Run

```text
python3 phase2/loop/erdos1208/verify_adaptive_trace_area_endpoint_charge.py
```

for the exact selected-energy inequality, support bounds, genuine stress
profiles, the 98-point planting, and the endpoint-free radial barrier.
