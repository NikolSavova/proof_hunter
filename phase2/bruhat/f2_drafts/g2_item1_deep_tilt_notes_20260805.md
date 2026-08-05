# G2 §8 item 1 (T.7 far region / deep tilt) — diagnostic notes, 2026-08-05

*Status: EXPLORATION ONLY. No new lemma is proved here. This documents (a) why
the two existing far-region mechanisms (T.7b-final, T.7c) provably cannot be
patched to cover `lam in (pi/m, 1/2]`, and (b) a repair route that looks right
but has an unresolved constant-chasing gap at one boundary. Written so the next
pass doesn't re-discover (a) from scratch and knows exactly where (b) stalled.
Diagnostic script: `g2_scripts/t2_item1/diag1_deep_tilt.py` (numbers below are
its output, reproduced 2026-08-05, CPython stdlib, double precision).*

## The gap, restated precisely

`g2_draft_t2_20260803.md` §3 proves the far-region decay `|phi_lam(t)| <=
exp(-m_*/4730)` on `pi/m <= |t| <= pi` **only for `0 <= lam <= pi/m`** (T.7b-
final), and a second bound `exp(-0.06 e^{-2K} m)` **only for `|lam| m <= K`**
fixed (T.7c). Both are "small tilt": `lam = O(1/m)`. Missing: any far-region
bound at all for `lam` ranging up through a genuine constant, e.g. `lam in
(pi/m, 1/2]` — item 1 of §8.

## Why neither existing mechanism extends (three findings)

**(1) The near/far split point `t = pi/m` is itself wrong for deep tilt.**
For `lam` FIXED (not shrinking with `m`), `|phi_lam(pi/m)| -> 1` as `m -> oo`:
```
lam=0.1: |phi_lam(pi/m)| at m=30,100,300,1000 = 0.0347, 0.0388, 0.2325, 0.6207
lam=0.3: |phi_lam(pi/m)| at m=30,100,300,1000 = 0.3183, 0.6160, 0.8395, 0.9476
lam=0.5: |phi_lam(pi/m)| at m=30,100,300,1000 = 0.6048, 0.8344, 0.9389, 0.9810
```
So **no bound of the form `exp(-c(lam) m)` can hold on the closed interval
`[pi/m, pi]`** for any lam bounded away from 0 — the true decay right at
`t = pi/m` is not exponential-in-`m` at all (this is expected: `sigma_lam^2 =
Theta(m)` for fixed lam, so the genuine CLT radius is `t ~ 1/sqrt(m)`, which is
*wider* than `pi/m`; the point `t=pi/m` sits deep inside the near-Gaussian
ball, not in a genuine far zone). Any correct deep-tilt far lemma needs a
`lam`-dependent (or at least a fixed, non-`pi/m`) starting point for `t`, not
`pi/m` verbatim.

**(2) The Gaussian bound (T.6ii) itself does not extend past `pi/m`.**
`exp(-sigma_lam^2 t^2/5)` is proved (unconditionally in `lam`) only for `|t|
<= pi/m`. Checking whether it happens to remain valid further out:
```
lam=0.3 m=100: worst finite |phi|/exp(-s2 t^2/5) = 1.9e+228 at t=1.87 (pi/m=0.031)
lam=0.5 m=300: worst finite |phi|/exp(-s2 t^2/5) = 1.1e+150 at t=1.73 (pi/m=0.010)
```
Astronomically violated. "Just reuse the near bound further out" is not a
repair route — the quadratic approximation genuinely breaks down once `t`
leaves a shrinking neighborhood of 0, as it must.

**(3) T.7c's pairwise-tilt-comparison technique is small-tilt by construction,
not merely by an unproved wider claim.** Its bound `E_lam sin^2(...) >=
e^{-2 lam(j-1)} E_0 sin^2(...)` carries a prefactor `e^{-2 lam(j-1)}`, and at
`j=m` this is `e^{-2w}`, `w = lam m`:
```
lam=0.1 m=30:  w=3    e^{-2w}=2.5e-3
lam=0.3 m=100: w=30   e^{-2w}=8.8e-27
lam=0.5 m=300: w=150  e^{-2w}=5.1e-131
```
For deep tilt `w = Theta(m)`, this prefactor is `e^{-Theta(m)}` — it destroys
the very bound it's being used to prove. T.7c's hypothesis `|w| <= K` isn't a
missed generalization; the technique is structurally incapable of deep tilt.

## The repair route that looks right (per the draft's own §8 item-1 note)

The exact factor identity (T.6i), already proved, is tilt-lossless:
```
|nu_j(t)|^2 = (1 + A_j) / (1 + a),
A_j := 4 e^{-lam j} sin^2(jt/2) / (1 - e^{-lam j})^2 >= 0,
a   := 4 e^{-lam}   sin^2(t/2)  / (1 - e^{-lam})^2   >= 0.
```
For `j >= j_1 := ceil(C/lam)` (`C` an absolute constant, e.g. `C=10`),
`e^{-lam j} <= e^{-C}` is tiny, so `A_j <= eps(C) := 4 e^{-C}/(1-e^{-C})^2`
(e.g. `eps(10) ~ 1.8e-4`) uniformly in `j, t`. Separately, for `lam <= 1/2`
and `t` bounded away from 0 (say `|t| >= t_0`), `(1-e^{-lam})^2 <= lam^2` gives
`a >= 4 e^{-1/2} sin^2(t_0/2) / lam^2`, bounded below by a positive constant
whenever `lam` is bounded above. So for `j >= j_1`, `|nu_j(t)|^2 <= (1+eps)/
(1+a) =: rho < 1`, a per-factor bound bounded away from 1 — and multiplying
over the `m - j_1` such factors gives genuine `exp(-c(lam,t_0) (m - j_1))`
decay. This is the mechanism the draft's item 1 gestures at, and the numerics
above (§ finding at fixed `t`, converging `-log|phi|/m` rates for `t = O(1)`)
confirm the TRUE behavior really is exponential-in-`m` once `t` is bounded
away from 0 — so this route is aimed at the right target.

## Where it stalls — the unresolved handoff

The count of "good" factors is `m - j_1 = m - ceil(C/lam)`. Two problems, not
yet resolved:

1. **Near the `lam ~ pi/m` boundary** (where T.7b-final already applies),
   `j_1 = C/lam` can be `>= m` (e.g. `lam = pi/m`, `C=10` gives `j_1 ~ 3.2m`),
   leaving *zero* usable "deep" factors — this mechanism is vacuous exactly
   where it needs to hand off to T.7b-final. Shrinking `C` to fix the handoff
   (e.g. `C ~ pi/2` so `j_1 <= m/2` at `lam = pi/m`) makes `eps(C)` no longer
   negligible, which weakens the `A_j <= eps` step and propagates into a worse
   constant in `rho`.
2. **The `t_0` used to lower-bound `a` is a free choice that interacts with
   the near-region boundary from finding (1) above**: finding (1) says the
   argument can't start at `t = pi/m` for fixed lam near `1/2`, but doesn't
   yet pin down how large `t_0(lam)` needs to be, nor what covers `t in
   [pi/m, t_0(lam)]` for lam away from the `pi/m` boundary (this is the
   "crossover" zone; empirically the true decay there tracks something close
   to `exp(-sigma_lam^2 t^2 / const)` with a SMALLER effective `sigma_lam^2`
   than the full one — i.e. a genuine local-CLT statement restricted to the
   "near-uniform" factors only — but this hasn't been turned into a clean
   inequality with an explicit constant).

Neither of these is a dead end — both look like ordinary (if fiddly) constant-
chasing, same flavor as what T.7b-final and T.7c already did twice in this
draft — but closing them is a genuine additional piece of work, not a
one-line patch. Estimate: comparable effort to T.7c's own derivation (a
"solid session"), not a quick fix.

## Checked: is the crossover slice actually load-bearing, or does it drop out?

Two things worth ruling in/out before investing more analysis effort:

**(a) Does Theorem A even invoke T.8 in the large-`w` regime?** Yes — checked
against Corollary T.10's own regime split (§ above, already in the draft):
"(ii) on `{|w| <= w_0}` and (i) on `{sigma_lam^2 <= rho lambda}`", and `(T.4)`
shows `sigma_lam^2 <= rho lambda` FORCES `w^2` large. So T.8 (= item 1's
lemma) is specifically the regime the refined law (ii) does *not* cover —
deep tilt is exactly its job, not an edge case. Item 1 is load-bearing.

**(b) Does the `sigma_lam^2 >= C_0` hypothesis at least confine `lam` to a
narrow, shrinking range, cutting the deep-tilt burden down?** Checked
numerically (`C_0 = 2000`, the ledger's constant): solved for `lam*(m)` where
`sigma_lam^2(m, lam*) = C_0`:
```
m=150:  lam* = 0.262   (w* = 39)
m=500:  lam* = 0.492   (w* = 246)
m=1000: lam* = 0.692   (w* = 692)
m>=3000: lam* essentially -> 1  (search saturates at the 0.9999 cap)
```
**`lam*` GROWS toward 1 as `m` grows — it does not shrink.** So for the
`m >= 180` regime this whole campaign targets (matching G1's threshold),
`sigma_lam^2 >= C_0` stays satisfied across essentially the *entire* `lam in
(0, 1)` range, not just up to `1/2`. The "up to `1/2`" scoping in the current
draft is not a corner that vanishes for large `m` — the deep-tilt lemma is
needed across close to the full domain, and possibly needs to reach beyond
`1/2` too (the draft's own `1/2` cutoff was inherited from the `k <~ 1.6m`
Step-0 boundary, not from a `sigma_lam^2` argument — worth re-checking that
cutoff is actually the right one once the lemma is being built for real).

## Recommendation

Item 1 does not drop out — treat it as open and necessary. If resumed: fix
`C` and `t_0` as explicit functions of `lam` (not universal constants) chosen
so mechanism-2's factor count `m - j_1(lam)` and mechanism-1's (`T.7b-final`)
domain `lam <= pi/m` overlap with no gap — mirroring how (T.10) already
stitched together the *hypothesis* ranges for (i)/(ii). The crossover slice
(point 2 in the section above) is the harder half and is now confirmed
necessary, not optional; budget it as its own sub-lemma rather than hoping it
folds into mechanism 2 for free.
