# Nested triangles: aggregate potential forces a restart, not the multiplier

**Date:** 2026-08-15.  All logarithms are base two.  This continues
`NESTED_TRIANGLE_PARTIAL_TRACE_TELESCOPE.md` and incorporates the three
macroscopic vertex clouds from
`../agent_shield_circuit_cover/NESTED_TRIANGLE_VERTEX_CLOUD_FIXED_GAP_GATE.md`.

## Verdict

The desired estimate

\[
 \sum_t\log(1+\rho_t)\ge (1-o(1))L\log\log L                 \tag{1}
\]

does **not** follow from the exact trace recurrence, cap/cup endpoint
factorization, the directional-activity inequality, least-counterexample
deletion minimality, and induction on every proper prefix.  Here
`L=log N`, the number of partner roles is `k asymp log L`, and
`log log L=log k+O(1)`.

There is a useful exact positive dichotomy.  If `Z_0` is within `2^A` of
the induction scale of the central child of size

\[
             m={N\over1+3k},
\]

then the three vertex clouds force

\[
 \sum_t\log(1+\rho_t)
       \ge (1-o(1))L\log k-A.                              \tag{2}
\]

Consequently any failure of (1) makes the central face bank itself inflate
to essentially the induction scale of a macroscopic `N/3`-point cloud.
This is a genuine **restart** of the child, not a mixed multiplier.

The restart can absorb the entire `L log k` deficit at the level of all
presently exact marginals.  I give a scalable formal profile sequence in
which

* all proper prefixes meet the fixed-gap induction target;
* the final state is a formal deletion-minimal counterexample marginal and
  its deletion identity has mean rank `(1/2+o(1))L`;
* all six outer-trace counts obey their exact floors and capacities;
* each of the three cloud banks occurs in the singleton profiles with
  load one;
* every directional endpoint profile obeys the exact common-endpoint
  identity, profile complement, and the `TV <= 2 mu V` activity bound; but
* nevertheless

\[
             \sum_t\log(1+\rho_t)
                 =(\log 3+o(1))L=o(L\log\log L).          \tag{3}
\]

This is not asserted to be a stretchable order type or even a planar
four-local face complex.  Its precise consequence is that an aggregate
proof must use a simultaneous planar coupling between the restarted
central bank and a cloud/partial trace, or a minimizer mutation excluding
that coupling pattern.  Endpoint counts, mean rank, and late-prefix
induction alone are sharp.

## 1. Exact cloud/restart dichotomy

Let

\[
 P_0=Y,\qquad P_t=P_{t-1}\mathbin{\dot\cup}T_t,
 \qquad P_{t-1}\subset\operatorname{int}\operatorname{conv}T_t, \tag{4}
\]

where the `T_t` are disjoint triangles.  Write `Z_t=V(P_t)`, including
the empty face, and

\[
 \rho_t={1+\sum_{\substack{G\subset T_t\\|G|=1,2}}
                 |\mathcal A_t(G)|\over Z_{t-1}}.          \tag{5}
\]

The outermost-trace theorem gives the exact identity

\[
       S:=\sum_{t=1}^s\log(1+\rho_t)
          =\log{Z_s\over Z_0}.                             \tag{6}
\]

Color the three vertices in every triangle arbitrarily and let `X_c` be
the three vertex clouds.  Let `H_c` be the number of **nonempty** ordinary
faces of `X_c`.  The maximum-layer cloud injection gives

\[
 \sum_t|\mathcal A_t(\{x_{t,c}\})|\ge H_c.                \tag{7}
\]

The central bank and the three cloud banks are disjoint labelled families,
so (equivalently, by summing (7) inside (6))

\[
                  Z_s\ge Z_0+H_1+H_2+H_3.                 \tag{8}
\]

Suppose the array has `s=km` triangles, so

\[
 N=m(1+3k),\qquad R=|X_c|=km={N\over3+1/k}.                \tag{9}
\]

For the fixed-gap target

\[
 \Phi_C(x)={x^2\over2}-Cx\log x,\qquad
 F_C(q)=2^{\Phi_C(\log q)},                                \tag{10}
\]

least-counterexample induction on each cloud gives
`H_c >= F_C(R)-1` if `F_C` includes the empty face.
Combining this with (6)--(8) proves

\[
 \boxed{\quad
 S\ge\log\!\left(1+{3(F_C(R)-1)\over Z_0}\right).
 \quad}                                                    \tag{11}
\]

If `Z_0 <= 2^A F_C(m)`, the exponent in the fraction is

\[
 \begin{aligned}
 \Phi_C(\log R)-\Phi_C(\log m)-A
   &=(1-o(1))L\log k-A,                                   \tag{12}
 \end{aligned}
\]

which proves (2).  Conversely, (11) gives the exact localization

\[
              Z_0\ge {3(F_C(R)-1)\over 2^S-1}.            \tag{13}
\]

Thus `S=o(L log k)` forces

\[
             \log Z_0\ge\Phi_C(\log R)-o(L\log k).        \tag{14}
\]

This is the aggregate conclusion actually supplied by the vertex clouds:
the central child has restarted at the macroscopic-cloud scale.

There is a second exact lower bound.  Every proper prefix is an induced
proper subset of a least counterexample.  Hence, for `t<s`,

\[
               Z_t\ge F_C(m+3t),\qquad
 S\ge\Phi_C(\log(N-3))-\log Z_0.                           \tag{15}
\]

When (14) is tight, (15) is only

\[
 \Phi_C(L)-\Phi_C(L-\log(3+o(1)))+o(L)
                    =(\log3+o(1))L.                       \tag{16}
\]

So late-prefix induction also stops at a fixed-power gap after the restart.

## 2. Formal profile countermodel

The following construction shows that (16) is compatible with every
scalar/marginal identity currently available.  It is useful to state it
first for `F_C`, ignoring integer rounding; the verifier uses an exact
integer discrete analogue.

Set `Z_0=F_C(R)`.  At an intermediate prefix of size `q=m+3t`, put

\[
 Z_t=\max\{F_C(q),\ Z_{t-1}+d(q-3)\}\quad(t<s),            \tag{17}
\]

where

\[
 K_q=q+\binom q2,\qquad d(q)=6(1+K_q)+1.                  \tag{18}
\]

At the last layer take

\[
             Z_s={F_C(N)+F_C(N-1)\over2}.                 \tag{19}
\]

For large `N`, rounding all quantities to integers is harmless.  Uniformly
for `q >= m=N/Theta(k)`,

\[
 {F_C(q+3)-F_C(q)\over F_C(q)}=O\!\left({kL\over N}\right)=o(1),
 \qquad d(q)=q^{O(1)}=o(F_C(R)).                           \tag{20}
\]

It follows that every increment

\[
                   \Delta_t=Z_t-Z_{t-1}                  \tag{21}
\]

lies between `d(q)` and `3Z_{t-1}`.  Therefore one may choose six integers
`a_{t,G}` with

\[
 \begin{gathered}
 1+K_q\le a_{t,G}\le Z_{t-1},\qquad
 \sum_{|G|=1,2}a_{t,G}+1=\Delta_t.                        \tag{22}
 \end{gathered}
\]

The lower bound in (22) is stronger than the universal edge floor and is
exactly the universal singleton floor.  Put all surplus above the six
floors into the three singleton profiles, as evenly as possible.  Since

\[
 Z_s-Z_0\gg F_C(R),                                      \tag{23}
\]

each singleton color receives total mass at least `F_C(R)`.  It can
therefore contain a maximum-layer cloud subprofile of that size, verifying
(7) for all three induced cloud targets with load one.

Equations (17), (19), and (22) give the exact outer-trace recurrence and
all proper-prefix induction inequalities.  Yet

\[
 \begin{aligned}
 S&=\log Z_s-\log Z_0\\
  &=\Phi_C(L)-\Phi_C(L-\log(3+1/k))+o(1)\\
  &=(\log3+o(1))L,                                       \tag{24}
 \end{aligned}
\]

which proves (3).

## 3. Least-counterexample deletion and rank marginals

The formal final state is consistent with deletion minimality.  Give each
of its `N` one-point deletions the value `D=F_C(N-1)`.  Define the total
rank incidence and mean rank by

\[
 M=N(Z_s-D),\qquad \mu={M\over Z_s}
            =N\left(1-{F_C(N-1)\over Z_s}\right).         \tag{25}
\]

Then the exact deletion identity holds:

\[
             \sum_{p}V(P-p)=ND=NZ_s-M=Z_s(N-\mu).        \tag{26}
\]

Moreover, a one-step expansion of (10) and (19) gives

\[
 \mu={1\over2}\Phi_C'(L)+o(1)
      ={L\over2}-{C\over2}\log L+O_C(1)=O(L).            \tag{27}
\]

Thus the formal state lies strictly inside the usual least-counterexample
mean-rank bound `mu <= Phi_C'(L)+o(1)`.  For `C>=1`, ordinary subset
scarcity does not contradict (27): the lowest rank at which there are
`F_C(N)` available subsets is

\[
 {L\over2}-(C-1/2)\log L+O_C(1)\le\mu+O_C(1).            \tag{28}
\]

The exact checker verifies the finite analogue of (28) by summing binomial
layers.  This is only a rank-marginal consistency check; it does not
manufacture a planar face complex.

## 4. Endpoint identity and profile complement are also compatible

Fix a prefix with `q` labels and let `H=Z-1` be its nonempty face count.
There are `E=binom(q,2)` physical endpoint pairs.  For one generic
direction assign exact endpoint counts

\[
 C_e=1\quad\hbox{for every }e,\qquad
 U_e=\begin{cases}
       1+H-q-E,&e=e_0,\\
       1,&e\ne e_0.
      \end{cases}                                      \tag{29}
\]

Then

\[
 \boxed{\quad H-q=\sum_e C_eU_e,\quad}                   \tag{30}
\]

which is the exact common-endpoint cap/cup factorization.  The total
directional profiles are

\[
                 C=q+\sum_eC_e=K_q,qquad
                 U=q+\sum_eU_e=H.                        \tag{31}
\]

Thus `CU >= H`, with all endpoint energy stored in the profile opposite
the small facing profile.  Repeat (31) in the three side directions of a
homothetic nested triangle family and swap `C,U` at the three antipodes.
Every edge trace in (22) is even granted the whole small profile
`1+C=1+K_q`.

The resulting cyclic cap-count step function has total variation

\[
                         6(H-K_q).                        \tag{32}
\]

This obeys the genuine planar activity marginal

\[
                         \operatorname{TV}C\le2\mu H      \tag{33}
\]

as soon as `mu >= 3`; (27) has much more room.  Hence endpoint complement
does not force a partial-trace gain.  It can be anti-aligned coherently at
all repeated triangle directions, exactly as in the endpoint-potential
ramp.

The important limitation is simultaneous realizability.  Equations
(29)--(33) are exact marginals, but they do not assert that one
downward-closed rank-three oriented matroid realizes them together with
(17)--(22).  Proving that this simultaneous realization is impossible
would be precisely the new planar theorem needed here.  It cannot be
replaced by endpoint factorization, activity, or deletion algebra, because
the model satisfies each of those separately and with slack.

## 5. What the all-triangle clouds really force

The aggregate branch is now localized without overclaim:

1. If the central bank is near its own `m=N/Theta(log L)` induction
   minimum, (11)--(12) prove the full `L log log L` potential.
2. If that potential is absent, (13)--(14) promote the central bank to the
   macroscopic `N/3` scale.
3. The three cloud banks and all late proper prefixes then guarantee only
   the fixed-power distance (16).
4. Endpoint identity and least-counterexample mean rank allow an exact
   coherent marginal state at that distance.

Therefore the next operation must be one of:

* a one-face product retaining a restarted central face and a cloud or
  partial trace;
* a cross-cloud circuit/shield theorem that supplies the remaining fixed
  power; or
* a genuine `V`-decreasing planar mutation excluding the restarted
  coherent profile.

The aggregate potential itself is not the missing inequality.

## 6. The `n^(3/2)` triangle tag does not yet close the fixed power

The polynomial endpoint makes the source--triangle tag look almost
decisive.  Put

\[
 a=\log_2 3=1.5849625\ldots,\qquad
 \delta=a-{3\over2}=0.0849625\ldots.                  \tag{34}
\]

If one had already promoted the residue to **label-primitive** product
contexts of selected mass at least

\[
                         n^{a-o(1)}V(P),                \tag{35}
\]

then the source--triangle theorem

\[
 M\le O(\kappa_A n^{3/2})V(P)                          \tag{36}
\]

would close whenever

\[
                         \kappa_A\le n^{\delta-o(1)}.  \tag{37}
\]

This conditional exponent calculation is correct.  The three cloud banks
do not supply its hypothesis.

Indeed, an unpaid mixed-cloud rectangle has rows and columns which are
ordinary **faces**, not physical labels.  If both face alphabets have size
`H`, the complete bad rectangle has

\[
                         e=H^2,\qquad a_c=H.             \tag{38}
\]

Even granting every ambient physical triangle as a tag gives only
`i_c <= binom(N,3)`.  The local Cauchy premise

\[
                         e^2\le\Gamma a_ci_c             \tag{39}
\]

would require

\[
                         H^3\le\Gamma\binom N3.          \tag{40}
\]

Here `log H=(1/2-o(1))L^2`, so (40) fails by a
quadratic-exponential factor.  A constant number of choices of the third
vertex cloud changes only `Gamma`.

Concentrating the canonical cross-cloud four-circuit does not improve
(40).  It fixes at most four physical trace labels.  The row and column
families containing those traces can still be exponentially large face
alphabets on the remaining cloud labels.  If the rectangle is split into
smaller contexts until (39) holds, the same source face occurs in all the
pieces; the number of pieces enters `kappa_A`, and the Cauchy gain cancels.

The obstruction is already stretchable at trace level.  On a convex
`p`-point cloud, the faces containing one fixed trace `S` number

\[
                         2^{p-|S|},                     \tag{41}
\]

while the full physical triangle alphabet has only `binom(p,3)` members.
Thus a fixed physical circuit trace can support an exponential residual
face alphabet with no metadata or chronology duplication.  This cloud has
a detached Boolean bank and is not a least-counterexample construction;
it proves precisely that circuit concentration alone is not the missing
label-primitive promotion.

Therefore the tempting comparison `3/2 < log_2 3` is a valid **conditional
margin**, but not a completed bridge.  To use it one still needs either a
physical-support projection satisfying (39), or a bounded-overlap charge
of the face alphabet to a mixed/detached shield bank.

## 7. Verification

Run

```text
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_nested_triangle_aggregate_potential_restart_barrier.py
```

The checker builds an exact integer target with logarithmic derivative
`floor(log q)-floor(log log q)`, the discrete analogue of
`Phi_1`.  On a 40,000-label formal array it verifies every prefix target,
every six-profile floor and capacity, the exact telescope, all three cloud
loads, the final deletion identity and mean rank, binomial rank scarcity,
the exact endpoint factorization, and the activity budget.  It separately
checks the asymptotic `O(L)` versus `L log log L` comparison from the exact
fixed-gap difference formula.  It also checks (34), the conditional
triangle-tag margin, and the exact failure of (39) for convex face
alphabets with a fixed trace.
