# Full-word masks do not discharge a stationary common triangle

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

Splitting the Hall-target overlap from the internal-triangle overlap gives
a sharper exact weighted Cauchy theorem, but it does **not** close the
quadratic base-word fibre.  If `M` distinct base words use the same two
physical `m`-point clouds, then base-decoding `A,C` targets have load one
while every physical cloud triangle has load `M`.  The resulting bound is

\[
                         V(P)\ge\sqrt{10/27}\,M^{1/2}m^2,          \tag{1}
\]

whereas the source/base bank already gives `V(P)>=M`.  At
`log M=kappa(log n)^2` and `log m=O(log n)`, (1) has quadratic coefficient
`kappa/2` and is asymptotically weaker than the source bank.  It does not
supply `M n^{Theta(loglog n)}` or the required linear EIC multiplier.

The high triangle overlap is geometrically realizable without producing
four distinct projective-direction queries.  Put all `q` base-word role
cells in one small stationary circuit chamber.  There are rational
adjacent-gap clouds `G,X` such that, for every base-role label `z` and
every three-set `T` contained in either cloud,

\[
                              \{z\}\cup T\text{ is nonconvex}.     \tag{2}
\]

All source--release targets `W,Q,C,A,E`, cross singleton faces, and actual
gap states remain valid.  Equation (2) has an exact full-word consequence:

* an ordinary output retaining even one variable base-role label has rank
  at most two in each physical cloud;
* any output containing a cloud triangle must omit **all** `q` variable
  roles; and
* after those omissions its base-word load is `M=D^q`.

Thus massive omission does not automatically create a cyclic third-role
bank.  The `q` incidences are repeated queries in one circuit chamber, not
genuinely distinct directions of the completed cloud, so the coherent
four-direction `PGL_2` theorem is inapplicable.  This is a sharp stationary
hierarchy barrier.  It is not a global low-face construction: the explicit
clouds are convex chains with large detached banks.  Charging those banks
still requires almost-full base history, exactly as in
`QUADRATIC_BASE_WORD_DETACHED_REUSE_BARRIER.md`.

## 1. Split-overlap internal-triangle Cauchy

Let context `c` have a simple bipartite record graph on active clouds of
sizes `a_c,b_c`, with `e_c<=a_cb_c` records of common weight `w_c`.
Choose one actual base-decoding target for every active row and column;
write

\[
                         h_c=a_c+b_c.                    \tag{3}
\]

For example, in the five-target rectangle take all `A_y` and `C_z`.
Let their actual weighted overlap be

\[
 \Lambda_B=\max_R\sum_{c:R\in\mathcal H_c^B}w_c.        \tag{4}
\]

When `a_c,b_c>=6`, take the internal triangle bank

\[
 i_c={a_c\choose3}+{b_c\choose3},\qquad
 \Lambda_3=\max_T\sum_{c:T\in\mathcal T_c}w_c.          \tag{5}
\]

> **Theorem 1 (heterogeneous-overlap triangle Cauchy).**
>
> \[
> \boxed{\displaystyle
>  \sum_cw_ce_c\le
>       5\Lambda_BV(P)+\sqrt{27/10}\,
>       \sqrt{\Lambda_B\Lambda_3}\,V(P).}              \tag{6}
> \]

**Proof.**  If `s=min(a,b)<=5` and `t=max(a,b)`, then
`e<=st<=5(a+b)=5h`.  For `a,b>=6`,

\[
 {t\choose3}\ge{5\over54}t^3,
 \qquad (a+b)(a^3+b^3)\ge4a^2b^2.                       \tag{7}
\]

Consequently

\[
                       h_ci_c\ge{10\over27}a_c^2b_c^2
                                  \ge{10\over27}e_c^2.  \tag{8}
\]

Multiply the square-root form of (8) by `w_c`, sum, and apply Cauchy.
The two occurrence sums are at most `Lambda_B V(P)` and
`Lambda_3 V(P)`.  Add the thin bound.  QED.

This refines `DENSE_HALL_INTERNAL_TRIANGLE_CAUCHY.md` when the high-overlap
targets form only a small part of the Hall bank.  It also makes the
remaining obstruction more explicit: the geometric mean in (6), not
either overlap separately, is the exact scale.

## 2. Honest scale audit on quadratic base words

In the tensor of `QUADRATIC_BASE_WORD_DETACHED_REUSE_BARRIER.md`, use one
context per word, unit weights, and complete `m by m` record graphs.  The
targets `A_(omega,i),C_(omega,j)` recover the word and active label, so

\[
 h=2m,\qquad \Lambda_B=1.                               \tag{9}
\]

The physical clouds are common to every word, hence every internal
triangle is reused in all contexts:

\[
 i=2{m\choose3},\qquad \Lambda_3=M.                    \tag{10}
\]

Substitution into (6) gives (1), up to the irrelevant thin term.  The
desired gain over the source bank `M` would be

\[
                    {M^{1/2}m^2\over M}={m^2\over M^{1/2}}.        \tag{11}
\]

Its logarithm is `2 log m-(1/2)log M`, which tends to negative quadratic
order when `log M=kappa(log n)^2`.  Therefore neither (1) nor its maximum
with the source bound improves the coefficient `kappa`.

For nonnegative context weights put

\[
                         W=\sum_\omega w_\omega,
 \qquad w_*=\max_\omega w_\omega.                       \tag{12}
\]

When actual `A,C` targets are unique to their source word,
`Lambda_B=w_*`, while a common physical triangle has `Lambda_3=W`.  The
thick bound becomes

\[
                         V(P)\ge\sqrt{10/27}\,m^2
                                  \sqrt{W/w_*}.          \tag{13}
\]

Canonical per-source mark weight at most one controls `w_*`; it does not
control `W`, because the triangle is shared by many distinct actual
sources.  Thus the effective context count in (13) is only square-rooted.
If actual `A,C` targets have duplicate degree `Delta_B`, replace `w_*` by
the actual load `Lambda_B`; this can only weaken the conclusion.  The
live obstruction is geometric common-child reuse, not merely duplicated
nongeometric chronology.

## 3. A stationary high-triangle-load realization

Use the fixed anchors

\[
 l=(-3,0),\qquad r=(3,0),\qquad t=(0,5),
 \qquad v=(-2,-1),\quad u=(2,-1).                       \tag{14}
\]

Let `G,X` be the rational adjacent double-dominance chains from
`DENSE_RECTANGLE_ACTUAL_GAP_FAN_GATE.md`.  For the `q` base-role macro
positions take

\[
 s_k={9\over10}+{k\over20(q+1)},\qquad
 z_k=(-3+3s_k-s_k(1-s_k),\ 5s_k+s_k(1-s_k)).             \tag{15}
\]

They occupy one short strictly convex subarc immediately before `t`.
Put an arbitrary `D`-point rational role cell in a sufficiently small disk
about every `z_k`.  Every transversal together with `l,r,t` is a convex
base word, giving `M=D^q` words.  Generic rational perturbation inside the
open cells removes cross collinearities.

The same strict checks as in the preceding tensor remain true for every
word `B_omega`:

\[
\begin{aligned}
 B_\omega,\ B_\omega\cup\{g\},\ B_\omega\cup\{x\},\
 B_\omega\cup\{g,x\}&\text{ are convex},\\
 B_\omega\cup\{v\},\ \{x,v\},\
 B_\omega\cup\{g,v,u\}&\text{ are convex},\\
 B_\omega\cup\{g,x,v\}&\text{ is nonconvex}.          \tag{16}
\end{aligned}
\]

The guard actual gap is always `rt` and the pocket actual gap is always
`lr`.

There is one additional stationary sign.  For every role point `z` in
every macro cell and every triple `T` contained wholly in `G` or wholly in
`X`, exact orientation gives (2).  All cells may be chosen uniformly small
because there are finitely many strict signs at each finite scale.  In the
explicit formulas the assertion holds throughout the rational interval
`9/10<=s<=19/20`; the verifier audits every triple exactly.

> **Proposition 2 (stationary triangle blocker).**  Any ordinary face
> containing at least one variable base-role label has at most two labels
> from `G` and at most two labels from `X`.

Indeed a larger trace contains a cloud triangle, and with the retained
role label it contains the nonconvex four-set (2), contradicting heredity.
The assertion is independent of which fixed anchors are deleted.  Thus no
mask of `l,r,t,u,v` releases a triangle while retaining even one variable
role.

## 4. Exact full-word/omission dichotomy

Put

\[
                              K_m=1+m+{m\choose2}.       \tag{17}
\]

If an output retains a nonempty subset of base roles, Proposition 2 gives
at most `K_m` possible traces in either physical cloud, or `K_m^2` for two
clouds.  These are polynomial baseline profiles and contain no
`n^{Theta(loglog n)}` child reservoir.

If an output uses a cloud triangle or any higher-rank detached face, it
must omit all `q` variable roles.  The output then contains no value of the
word `omega`; the same geometric face is generated by all `M=D^q` words.
Its exact base-word load is `M` unless some external chronology is attached.
The decoder bound from the preceding report says that attaching at most
`h` role labels would leave load at least
`D^(q-h)/((q+1)2^q)`, but here (2) is stronger: for triangle outputs one
must take `h=0`.

This also answers the direction-coherence proposal.  The physical cloud
has high incidence degree, but all `q` blockers lie in the same open
oriented-matroid chamber and impose the same `1+3` sign.  They do not query
four distinct projection chambers.  Contracting repeated stationary
queries leaves a one-direction star/reset hierarchy, which is explicitly
outside the scope of the coherent-itinerary theorem.  No directed cycle
of jointly ordinary profile unions is forced.

## 5. Scope

Theorem 1 is unconditional.  Proposition 2 is a scalable exact planar
barrier preserving the complete marked target system and actual gaps.  It
shows that the high-`Lambda_3` residue in (6) can carry quadratic base
entropy and survive every bounded fixed-anchor mask.

The construction is not a coefficient-scale upper bound for the full face
count.  Its explicit clouds are convex chains, so after erasing the word
they have large detached reservoirs.  Projective-universal low-face
replacement preserves fixed-root nesting but need not preserve the
all-triples stationary sign (2).  A genuine subhalf construction would
still require an exact full recurrence controlling those detached and
base-role child faces.  What is proved here is the sharp failure of the
current full-word mask, triangle-Cauchy, and multi-direction-query exits.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_full_word_triangle_reuse.py
```

Expected output:

```text
PASS: split Cauchy constants, stationary triangle blockers, targets/gaps, and scale audit
```

