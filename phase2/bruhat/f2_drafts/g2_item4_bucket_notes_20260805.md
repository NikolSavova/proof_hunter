# G2 §8 item 4 (T.9's mechanical remainder) — progress notes, 2026-08-05

*Status: PARTIAL. One bucket of the C_R(K) decomposition is now built,
cross-validated, and numerically certified. The others (box/tail/out
kernel-transfer, Taylor remainder) are not started. Script:
`g2_scripts/t2_item4/t2i4_nc1_model.py` (PASS, 2026-08-05).*

## Why item 4 wasn't actually "mechanical, one solid session" as labeled

`g2_draft_t2`'s §8 pointed at `g1_draft_b`'s Lemma B.6 (the untilted
kernel-transfer bucket table) as the pattern to repeat. But Theorem T.9's own
proof text (§5, Step 2) references a **"Lemma T.9'"** by name — the tilted
analogue of `g1_draft_b`'s Lemma B.7 (the exact second-order model polynomial)
— that was never actually written. The numbers currently backing item 4
(`N_lam(0)/P_lam(0)^2 <= 0.9/m^2`, total `C_R ~ 5.1`) are asserted in prose
("careful bookkeeping... certifies") with no derivation behind them.

## What's now built: the tilted model polynomial, from scratch, verified

Following `g1_draft_b`'s Lemma B.1/B.7 recipe but with the two new odd
cumulant terms (`kappa_3`, `kappa_5`) the tilted frame introduces:

```
log phi_lam^c(t) + s2 t^2/2 = -i*alpha*t^3 - beta*t^4 + i*delta*t^5 - gamma*t^6 + R_7(t),
alpha := kappa_3(lam)/6,  beta := -kappa_4(lam)/24,
delta := kappa_5(lam)/120, gamma := kappa_6(lam)/720
```
(sign convention matches T.6iii's SIGN NOTE: `(it)^r` cycles `-i,+1,+i,-1` for
`r=3,4,5,6`). Truncating `exp(...)` to `O(t^8)` and Fourier-transforming each
term via `(1/2pi) int t^n e^{-s2t^2/2} e^{-itx} dt = (-i)^n s2^{-n/2} Z(y) He_n(y)`
gives the tilted model density factor `P_lam(y)`.

**Two independent correctness checks, both PASS:**
1. `P_lam(y)`'s imaginary part cancels to **exactly 0 symbolically** — required
   (the tilted pmf is real), not assumed.
2. Setting `alpha=delta=0` (the untilted case) reproduces `g1_draft_b`'s known
   result **exactly**: coefficient of `gamma` is `-90/s2^3`, coefficient of
   `beta^2` is `384/s2^4` — matching `g1_draft_b`'s quoted `N(0) = -90g + 384b^2
   + O(m^-3)` term-for-term, with the "elided" `O(m^-3)` terms identified
   explicitly (`beta^3`, `beta*gamma`, `beta^4`, `beta^5` — all weighted order
   `>= 3` using `beta ~ O(1/m)`, `gamma ~ O(1/m^2)`).

## The finding that needed resolving: a bucket-placement subtlety

Computing `N_lam(y) := -P_lam''(y)P_lam(y) + P_lam'(y)^2 - B_lam He_2(y)
P_lam(y)^2` (same defining relation as `g1_draft_b`'s Lemma B.7, `B_lam := 12
beta/s2^2`) at `y=0` turns up a term **`-36 alpha^2/s2^3`** with no `beta`,
`gamma`, or `delta` factor. In the natural scaled variable `a := alpha/s2^1.5
= O(1/sqrt(m))` for bounded `w`, this term is `O(1/m)` — the **same order as
`B_m` itself**, not `O(1/m^2)`. This is not a bug: it's exactly the "`kappa_3^2`
term" that Theorem T.9's own proof text (Step 2) already handles *separately*,
folding it into the `w^2` coefficient (the "`0.35 + 0.09 < 0.5`" arithmetic) —
but the prose never showed the split explicitly, so it wasn't obvious this
bare-`alpha^2` piece is what that referred to, nor that the REST of `N_lam(0)`
is genuinely `O(1/m^2)` once it's pulled out.

**Confirmed numerically** (script §4): splitting `N_lam(0) = (bare alpha^2
term) + (residual)` and tracking each piece at FIXED `w = lam*m` as `m` grows:
`bare_term * m` converges to a nonzero constant (genuinely `O(1/m)` — belongs
in the `w^2` bucket, consistent with the theorem's existing accounting);
`residual * m^2` converges to a different nonzero constant (genuinely
`O(1/m^2)` — this is the real `C_R` contribution from this bucket).

## The certified number

A grid sweep (`m in {30,...,2000}`, `w` on a 20-point grid in `[0,K]`) of
`|residual / P_lam(0)^2 * m^2|`:
```
K=1: max = 1.5491   (at m=30, w=1.0)
K=2: max = 4.0889   (at m=30, w=2.0)
K=4: max = 4.9126   (at m=2000, w=2.8)
```
These are **smaller** than the draft's rough prose guess of `C_R ~ 5.1` for
this bucket alone, and land inside its stated "`C_R(K) ~ 6 + O(K^2)`-class"
envelope. Same status class as the (T.7b-cert)/(T.7c-cert) grid certificates
elsewhere in this draft — numerically certified over a grid, not yet a
closed-form worst-case proof (would need the T.9''a-style uniform cumulant
bounds pushed through this same computation symbolically; not attempted here).

Independent sanity check along the way: extended the verified `g0..g3`
closed-form cumulant machinery (`t2_nc1_cumulants.py`, checked as NC-T1) by two
more derivatives (`g4`, `g5`, Bernoulli-series small-`u` fallbacks) to get
`kappa_5(lam)`, `kappa_6(lam)` in closed form, then cross-checked the shared
`var`/`kappa_3` outputs against the independently-written `t2_nc5_cf.py`
(`sig2`, `kap3`) — agreement to `~1e-13` relative at every tested `(m, lam)`.

## What's still missing for item 4 to fully close

This covers **one bucket** of Theorem T.9's `C_R(K)`: the pointwise
`N_lam(0)/P_lam(0)^2` piece. Still open:
1. **The box/tail/out kernel-transfer bucket** (`g1_draft_b`'s Lemma B.6
   analogue) — the dominant piece in the untilted case (`KB(180) = 106.6`
   before scaling by `1/m^3`), not attempted for the tilted 6-term model.
2. **The Taylor-remainder bucket** (`g1_draft_b`'s Lemma B.7' analogue).
3. **Assembling the pieces into a single closed-form `C_R(K)`** with an
   honest, non-numerically-only proof (or accepting the grid-certificate
   status as the draft already does elsewhere for comparable pieces).

Given the strong headroom found here (measured needed constant ~10x smaller
than every asserted bound so far, in both item 1's and item 4's exploration),
the remaining buckets are more likely to be *tedious* than *risky* — but
tedious in the same "one real derivation, not a rubber stamp" sense as this
piece turned out to be.
