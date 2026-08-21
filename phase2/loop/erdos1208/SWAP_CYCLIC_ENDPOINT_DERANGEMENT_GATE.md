# Cyclic endpoint derangement removes the amplification square

## 1. Outcome

The endpoint-pencil envelope is

\[
 \mathcal P_\Lambda
 =3\sum_{o\ {\rm high}} w(o),
 \qquad
 w(o)={r_{C(o)}-1\choose2}.                       \tag{1.1}
\]

The previous two-track key paired every pointed record over `o` with every
other occurrence through its assigned endpoint.  That multiplication is
unnecessary: the key universe is already `O(k^3)`.  This note schedules
each pointed decoration against exactly one partner, cyclically and without
fixed points.

Let `M_cyc=sum_o w(o)=P_Lambda/3`, let `K_cyc` be the occupied key support,
and let

\[
 Q_{\rm cyc}=\sum_\kappa {M_{\rm cyc}(\kappa)\choose2}. \tag{1.2}
\]

Then

\[
 K_{\rm cyc}\le144k(k-1)^2<144k^3                  \tag{1.3}
\]

and

\[
 \boxed{M_{\rm cyc}^2
 \le K_{\rm cyc}(M_{\rm cyc}+2Q_{\rm cyc}).}       \tag{1.4}
\]

Consequently

\[
 \boxed{Q_{\rm cyc}\le N^{o(1)}(k^3+m^2)}          \tag{1.5}
\]

is sufficient for the full endpoint-pencil gate.  Unlike the old
all-neighbours collision, `Q_cyc` contains no Cartesian endpoint-degree
factor.

## 2. The cyclic schedule

For each endpoint `x`, order the occurrences whose six-track footprint
contains `x`:

\[
 O_x=(o_0,\ldots,o_{d(x)-1}).                       \tag{2.1}
\]

Every high occurrence `o_i` has already been assigned one endpoint
`x=chi(o_i)` with `d(x)>=Lambda>=2`.  Enumerate its `w(o_i)` pointed
decorations by `t=0,...,w(o_i)-1` and put

\[
 \phi_t(o_i)=o_{i+s_t},\qquad
 s_t=1+(t\bmod(d(x)-1)),                            \tag{2.2}
\]

with indices modulo `d(x)`.  Thus `phi_t(o_i)!=o_i`.  For each fixed
residue `t mod (d(x)-1)`, `phi_t` is a cyclic permutation and hence is
injective.

At `x`, take the first of the twelve directed-track endpoint slots of an
occurrence.  Its token consists of the slot and the opposite physical
endpoint.  If these tokens for `o_i` and `phi_t(o_i)` are `(sigma,y)` and
`(tau,z)`, define

\[
 \kappa(o_i,t)=(x,\sigma,y,\tau,z).                 \tag{2.3}
\]

There are at most `k` choices for `x`, twelve choices for each slot, and
`k-1` choices for each opposite endpoint.  This proves (1.3).  Every
pointed decoration is scheduled exactly once, so its total mass is exactly
`M_cyc`.  Equation (1.4) is Cauchy applied to the key loads.

Writing `B_0=k^3+m^2`, (1.3)--(1.5) give

\[
 M_{\rm cyc}
 \le K_{\rm cyc}+\sqrt{2K_{\rm cyc}Q_{\rm cyc}}
 \le N^{o(1)}B_0.                                  \tag{2.4}
\]

Together with the already-paid all-low occurrence branch, this proves the
desired cube-root support estimate.

## 3. Exact collision split

Take two distinct scheduled decorations with the same key.  If their first
occurrences differ, those occurrences reuse the first fixed physical
track.  If their partners differ, the partner occurrences reuse the second
fixed physical track.  Therefore every collision except one explicitly
quantified internal case feeds the rank-five anchored-track theorem.

The internal case has the same first occurrence `o` and the same partner.
By (2.2), this happens exactly when the two decoration indices are equal
modulo

\[
 D_o=d(\chi(o))-1.                                  \tag{3.1}
\]

Write `w(o)=q_oD_o+s_o`, with `0<=s_o<D_o`.  The exact internal collision
mass is

\[
 \boxed{
 Q_{\rm int}
 =\sum_{o\ {\rm high}}
 \left(D_o{q_o\choose2}+s_oq_o\right)
 \le\sum_{o\ {\rm high}}{w(o)^2\over2D_o}.}       \tag{3.2}
\]

Thus the direct geometric gate has become

\[
 Q_{\rm cyc}=Q_{\rm int}+Q_{\rm track},            \tag{3.3}
\]

where every record in `Q_track` contains a literal repeated
endpoint-labelled track and hence the rank-five transverse quotient plus
the one-dimensional gauge.  There is no remaining anonymous collision
class.

For later summation it is useful to keep the exact four-way split.  In a
collision compare the first occurrence identities and the partner
occurrence identities.  Write `Q_ab`, `a,b in {0,1}`, where `a=1` means
the first identities differ and `b=1` means the partner identities differ.
Then

\[
 \boxed{Q_{\rm cyc}=Q_{00}+Q_{10}+Q_{01}+Q_{11},}  \tag{3.3a}
\]

with `Q_00=Q_int`.  The `Q_10` and `Q_01` branches have one anchored
repeated track, while `Q_11` has two simultaneous anchored repeated tracks
through the same physical endpoint.  This double-track branch is the
genuinely transverse main term; it should be attacked before relaxing to
one unanchored six-direction energy.

Equation (3.2) is also the correct diagnostic for the internal rich-cell
branch.  If `w(o)<d(chi(o))`, it vanishes exactly.  If it is large, the
obstruction is not endpoint amplification but a rich owner cell whose
pointed decorations revisit the same physical partner.

There is already a target-scale theorem for the low-weight part.  For a
dyadic `W`, retain the occurrences with

\[
 W\le w(o)<2W.                                    \tag{3.4}
\]

If `n_x` of them are assigned to `x`, then `n_x<=d(x)` and, since
`d(x)>=2`, one has `d(x)-1>=d(x)/2`.  Hence (3.2) gives

\[
 Q_{\rm int}(W)
 \le\sum_x {4W^2n_x\over d(x)}
 \le4kW^2.                                       \tag{3.5}
\]

Put `B_0=k^3+m^2` and

\[
 W_0=\sqrt{B_0/k}.                                \tag{3.6}
\]

Summing the geometric series of dyadic bounds proves

\[
 \boxed{Q_{\rm int}[w(o)\le W_0]=O(B_0).}         \tag{3.7}
\]

Since `w(o)=binom(r_C-1,2)`, the only internal survivor has

\[
 r_C\gg(B_0/k)^{1/4}.                             \tag{3.8}
\]

In the critical range `m^2\asymp k^3`, this means `r_C\gg sqrt(k)`.
Thus the internal branch has already become a genuinely very-rich-cell
problem; ordinary and moderately rich owner cells are free.

There is a complementary first-moment theorem for the off-diagonal branch.
For an endpoint `x` and a track token `u=(slot,opposite endpoint)`, put

\[
 a_x(u)=|\{o\in O_x:\operatorname{token}_x(o)=u\}|. \tag{3.9}
\]

For a scheduled first occurrence `o` assigned to `x`, define its cycle
repetition

\[
 \rho(o)=\left\lceil{w(o)\over d(x)-1}\right\rceil. \tag{3.10}
\]

Fix `R,Delta>=1`.  Retain only scheduled records for which

\[
 \rho(o)\le R,qquad a_x(u)\le\Delta,qquad a_x(v)\le\Delta, \tag{3.11}
\]

where `u,v` are the first and partner tokens of the key.  For a fixed first
occurrence, the cyclic schedule visits each partner identity at most `R`
times.  There are at most `a_x(v)` partners with token `v` and at most
`a_x(u)` possible first occurrences.  Hence every retained key has load at
most

\[
 R a_x(u)a_x(v)\le R\Delta^2.                     \tag{3.12}
\]

Using (1.3) gives the direct first-moment bound

\[
 \boxed{M_{\rm low}(R,\Delta)
 \le144R\Delta^2 k(k-1)^2.}                      \tag{3.13}
\]

Thus subpolynomial `R,Delta` pay this whole branch from `k^3`, without
forming `Q_cyc`.  Every surviving record has one of two concrete features:

1. **high cycle repetition**, `rho(o)>R`, which is the very-rich internal
   regime quantified by (3.2)--(3.8); or
2. **a high physical-track token**, `a_x(u)>Delta` or `a_x(v)>Delta`, which
   is exactly an endpoint-labelled repeated-track pencil and feeds the
   rank-five normal form.

This is the cleanest current direct dichotomy.  The hard off-diagonal
energy need only be studied inside polynomially rich physical-track
pencils; low track degree is already free.

## 4. Exact stresses

The improvement is already large on the first active rows.

* Transformed Costas `23`, at `Lambda=16`: the old all-neighbours profile
  was `(mass,support,max,Q)=(16244,5380,20,33564)`.  The cyclic profile is
  `(204,192,2,12)`.  Its internal mass is zero.  Seven of the twelve
  collisions are pure gauge on both occurrence pairs; the other five are
  transverse repeated-track pairs.  All twelve lie in `Q_11`.
* Transformed Costas `29`, at `Lambda=16`: the cyclic profile is
  `(4857,3095,35,8174)`.  Again `Q_int=0`; all collisions are honest
  repeated-track collisions, with
  `(Q_00,Q_10,Q_01,Q_11)=(0,83,146,7945)`.  Thus more than 97% of the
  collision mass already lies in the double-track branch.

The second row contains cells of load greater than three, so the vanishing
of the internal term is not merely the load-three tautology.

## 5. What remains

The next theorem should be stated for (3.3), not for the superseded
all-neighbours `Q_star`.

1. Bound the off-diagonal `Q_track` by summing the four-direction
   transverse quotient and its sharp linear gauge fibre across the two
   fixed physical tracks.  By (3.13), this is needed only when at least one
   of those tracks has polynomial occurrence degree.
2. Handle only the very-rich internal tail (3.8), preferably by charging
   its repeated parameter pairs directly to the metric determinant/height
   budget.  The complementary internal mass is already paid by (3.7).

The cyclic schedule removes the endpoint-degree square before either hard
problem is addressed.  It therefore exposes the smallest currently known
direct gate to the `1/3` exponent.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_cyclic_endpoint_derangement.py
```

The verifier checks the exact schedule, support bound, Cauchy inequality,
collision trichotomy, and the equality and upper bound in (3.2) on
exhaustive small and seeded random endpoint systems.  It also checks the
dyadic inequality (3.5), the per-key estimate (3.12), and its global
consequence (3.13).  The optimal-core
analyzer independently produces the two genuine Costas profiles above.
