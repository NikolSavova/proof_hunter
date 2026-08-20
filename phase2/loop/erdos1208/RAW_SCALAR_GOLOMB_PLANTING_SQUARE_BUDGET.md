# The raw scalar Golomb-planting square budget

> **Status: one-channel theorem valid, global conclusion superseded.**
> `RAW_SCALAR_DILATED_SWAP_GOLOMB_COUNTEREXAMPLE.md` subsequently kills the
> original aggregate by using one diagonal copy to realize all core scalar
> channels simultaneously.  The square-budget theorem below still explains
> exactly why every earlier one-designated-channel gadget fell short.

## 1. Verdict

Return to the exact off-diagonal scalar aggregate

\[
 \mathfrak X(A)
 :=\sum_q\mathcal X_q
 =\sum_{r\ne0}C_A(r)R_A(r),                    \tag{1.1}
\]

where

\[
 C_A(r)=\sum_qR_{B_q}(-18r),\qquad
 R_A(r)=\#\{(e,e'): \delta(e)-\delta(e')=r\}. \tag{1.2}
\]

The earlier Golomb-plus-metric-gadget counterexamples to the endpoint and
synchronized-pooling gates do **not by themselves** threaten

\[
 \boxed{\mathfrak X(A)\le m^{o(1)}Nk^3.}        \tag{1.3}
\]

There is an exact reason.  A fixed nonzero squared-length gap in a
collinear Golomb core has only divisor-many physical source pairs.  Even
if every one of them has maximal quadratic clean codegree, a collection
of one-channel planted gadgets with total size `L` adds at most

\[
 \boxed{m^{o(1)}n^2L^2\le m^{o(1)}k^4}          \tag{1.4}
\]

to (1.1).  This is one full power below `Nk^3=Theta(k^5)`.  The theorem
pays both the earlier Golomb wedge gadgets and the new parabolic rectangle
without replacing raw records by endpoint wedges.

This isolates why a counterexample has to couple many scalar channels with
the same planted points.  The follow-up dilated-copy construction does
exactly that and disproves the global aggregate.

## 2. Fixed-gap source-weight theorem

Let

\[
 A_0=\{(b,0):b\in B\},\qquad |B|=n,             \tag{2.1}
\]

where `B` is an integer Golomb ruler.  For a nonzero scalar `r`, let

\[
 C_0(r)=
 \sum_{\substack{s,s'\in\Sigma_0\\
       \delta(s)-\delta(s')=-18r}}c_0(s,s'),    \tag{2.2}
\]

where `c_0(s,s')` is the number of clean core translations common to the
two starts.

**Theorem 2.1 (one-channel source cap).**  Uniformly for `r!=0`,

\[
 \boxed{
 C_0(r)\le2\tau(18|r|)n(n-1)=m^{o(1)}n^2.}     \tag{2.3}
\]

**Proof.**  Every core edge has a positive integral length `x`, and the
Golomb property makes the map from physical edges to lengths injective.
An ordered pair counted in (2.2) therefore gives

\[
 x^2-y^2=(x-y)(x+y)=-18r.                       \tag{2.4}
\]

The two factors in (2.4) determine `(x,y)`.  Allowing signs and parity
only enlarges the count to at most `2 tau(18|r|)`.  For each physical
source pair there are at most `n(n-1)` possible nonzero directed anchor
differences `q`; distance-Sidonicity makes the directed difference identify
its anchor.  Clean restrictions can only decrease the count.  This proves
(2.3).  Since `|r|<=2m^2`, the classical divisor bound makes the last
factor `m^{o(1)}`.  QED.

This argument deliberately retains literal common `q`: the codegree is
bounded only after the number of physical source pairs at the fixed scalar
has been divisor-counted.

## 3. Square budget for planted metric channels

Adjoin disjoint metric components `G_j` of sizes `ell_j`.  Suppose the
engineered target records in `G_j` use one designated nonzero scalar
`r_j`; write

\[
 R_j=\#\{(e,e')\in E(G_j)^2:
                 \delta(e)-\delta(e')=r_j\}.    \tag{3.1}
\]

Because all distance labels are distinct, the first edge determines the
second at a fixed gap.  Hence

\[
 R_j\le {\ell_j\choose2}.                       \tag{3.2}
\]

Apply Theorem 2.1 to the core-source/component-target part of (1.1):

\[
\begin{aligned}
 \mathfrak X_{0\to G}
 &\le\sum_j C_0(r_j)R_j\\
 &\le m^{o(1)}n^2\sum_j{\ell_j\choose2}\\
 &\le m^{o(1)}n^2\left(\sum_j\ell_j\right)^2.
                                                        \tag{3.3}
\end{aligned}
\]

This remains true when some `r_j` agree: combine their `R_j` before using
the same bound (2.3).  Put `L=sum_j ell_j` and `k=n+L`.  Equation (3.3)
is at most `m^{o(1)}k^4`, proving (1.4).

The scope is exact.  It bounds the deliberately planted internal target
channels against old Golomb-core source pairs.  It does not automatically
bound unintended cross-component target gaps or new clean source pairs.
Those are finite-avoidance conditions in the counterexample constructions,
and the exact certificate below confirms that they contribute zero in the
stored parabolic instance.  A universal proof of (1.3) must, of course,
handle them without a genericity assumption.

### Parabolic rectangle

For the `4L`-point rectangle of
`OUTER_NORMALIZED_PARABOLIC_RECTANGLE_COUNTEREXAMPLE.md`,

\[
 R_G(r)=R_G(-r)=L^2,\qquad
 W_{r,N}=W_{-r,N}=L^2(L-1).                     \tag{3.4}
\]

Thus the genuine raw channel costs only

\[
 C_0(r)R_G(r)=m^{o(1)}n^2L^2,                  \tag{3.5}
\]

while an endpoint-wedge replacement inserts the false extra factor `L`.
This is precisely why the outer-normalized gate failed by a power and the
original aggregate did not.

### Earlier Golomb wedge gadgets

The same proof pays any collection of fixed-scalar arms or wedges.  Their
raw fixed-gap multiplicity is at most the number of internal gadget edges,
so the sum over all planted blocks obeys the same square budget (3.3).
Binomial translation pooling and endpoint-degree amplification count one
raw target record many times; (1.1) counts it once.

## 4. Exact 92-point decomposition

The verifier recomputes the original scalar aggregate on the stored
60-point Ruzsa core joined to the 32-point parabolic rectangle.  Its
off-diagonal mass splits into exactly two nonzero role channels:

\[
\begin{array}{c|r}
\text{source pair / target pair}&\text{raw mass}\\ \hline
\text{core--core / core--core}&172,851,320\\
\text{core--core / rectangle--rectangle}&71,680\\
\text{all other role combinations}&0.
\end{array}                                             \tag{4.1}
\]

At each of the two signs of the planted scalar, the core source weight is

\[
 C_0(\pm r)=320+240=560,                        \tag{4.2}
\]

coming from exactly two ordered core source pairs, while
`R_G(plus/minus r)=64`.  Therefore the entire rectangle increment is

\[
 2\cdot560\cdot64=71,680.                       \tag{4.3}
\]

The total is

\[
 \mathfrak X(A)=172,923,000
 <Nk^3=3,259,587,968,                            \tag{4.4}
\]

or `0.05305057... Nk^3`.  By comparison, the false endpoint statistic
has `W_(r,N)=448` at each sign instead of the raw `64`.

## 5. The intrinsic Golomb core points to the multi-channel survivor

The planting theorem does not make the core itself easy.  Exact Ruzsa
profiles are

\[
\begin{array}{c|r|r|r|r|c}
p&k&H&\max C_0(r)&\mathfrak X(A_0)&
 \mathfrak X(A_0)/(Nk^3)\\ \hline
17&16&3,888&35&11,302&0.022994\\
31&30&82,746&604&2,669,740&0.227309\\
43&42&336,114&1,858&24,551,018&0.384874\\
59&58&1,251,486&4,691&195,524,996&0.606241\\
61&60&1,322,406&3,951&172,851,320&0.452112.
\end{array}                                             \tag{5.1}
\]

The oscillation is arithmetical (not monotone in `p`), and larger profiles
continue to grow.  This led to the norm-dilated diagonal copy in
`RAW_SCALAR_DILATED_SWAP_GOLOMB_COUNTEREXAMPLE.md`, which aligns every core
source pair and gives `Omega(k^6)` raw mass.

For a collinear core, the target marginal also has
`R_A(r)<=2 tau(|r|)=m^{o(1)}`.  Consequently the remaining core theorem is
equivalent, up to a divisor factor, to the internally coupled incidence
bound

\[
 \boxed{
 \sum_{\substack{s\ne s'\\
  (\delta(s')-\delta(s))/18\in D-D}}
 c_0(s,s')\le m^{o(1)}Nk^3.}                    \tag{5.2}
\]

The trivial bound is `sum_q h_q^2`, of order `k^6` on dense rulers; (5.2)
would require a factor-`k` saving from the two-scale metric selector.  That
saving is false: the diagonal-copy swap makes every summand active.
Equation (5.2) is retained here as the exact gate killed by the follow-up.

## 6. Verification

The verifier uses bitsets for exact common-fibre codegrees.  It checks the
factorization/divisor cap on the 32 most occupied collinear source gaps in
each core, recomputes the five Ruzsa profiles in (5.1), and performs the
complete role-channel decomposition (4.1).

Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_raw_scalar_golomb_planting_square_budget.py
```
