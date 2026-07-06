# Theorem F2 — merged proof draft (post-referee synthesis)

*Merge editor pass, 2026-07-06. Sources: four blind drafts (`draft_clt.md`,
`draft_elementary.md`, `draft_saddle.md`, `draft_pro.md`) and their four adversarial
referee reports. This document takes the best-surviving path per proof obligation,
repairs every referee-caught flaw that is repairable without new mathematics, and
discards (with reasons, §6) everything that is false or broken. Every NUMERIC CHECK
below was **re-run by the merge editor** against the exact harness `mahonian.py`
(extended to `m = 150` in exact rational arithmetic); merge-editor scripts:
`merge_checks.py`, `r2_series.py`, `extend150.py` (session scratchpad).*

Notation (fixed throughout): `I_m(k)`, `N = m(m-1)/2`, `p(k) = I_m(k)/m!`,
`sigma^2 = m(m-1)(2m+5)/72`, `r(k) = I(k)^2/(I(k-1)I(k+1))`, `r_m = min_k r(k)`,
`x = k - N/2`, `y = x/sigma`. `S_r = sum_{j=1}^m j^r`. Central index `k_c = floor(N/2)`.

```
B_m := -kappa_4 / (2 sigma^4) = (S_4 - m)/(240 sigma^4) = (27/25) m^{-1} (1 + O(m^{-1})) > 0 .
```

(All four drafts' fourth-cumulant constants — `B_m`, `12 beta`, `|kappa_4|/2sigma^4`,
the elementary draft's `m^4/240` one-step excess — are algebraically the SAME quantity;
verified, no disagreement.)

---

## GAP LEDGER

Every remaining gap, ranked. "Blocks" = which frozen obligations do not close without it.

| # | Gap | Severity | Blocks | Most promising repair route |
|---|-----|----------|--------|------------------------------|
| **G1** | **Window Edgeworth bookkeeping** (Prop 2.1 / Prop 2.2): the pointwise expansion's constant `C_1` and, more importantly, the transfer of the Lemma 1.3/1.4 remainders through the second-difference kernel to the window law `|E_1| <= C_2/m^2` — structure asserted and numerically calibrated (`|E_1(0)| <= 0.19/m^2`; on `\|y\|<=3` the needed shape-constant is `C_2 ≈ 0.70` against `(1+y^6)/m^2` — NOT 0.4 as one blind draft claimed, NOT 0.2 as another's differently-shaped bound suggested; resolved numerically, see NC-6), not derived line by line. | moderate (standard machinery; every analytic ingredient is now fully proved — Lemmas 1.3, 1.4) | sharp-rate constants in (a); the constant in (b)'s `O(m)` localization; (c) | Petrov Ch. VII bookkeeping using Lemma 1.3's proved remainder + Lemma 1.4's proved far bound, pushed through Lemma 1.5's kernel (errors stay *relative* inside the kernel). Mechanical, long. |
| **G2** | **Tilted-frame uniformity** (Prop 3.5, both parts): (i) the crude uniform tilted ratio law over all interior `k` with `sigma_lam^2 >= C_0`; (ii) the refined small-tilt law `sigma_lam^2 (r(k)-1) = 1 - B_m(1+O(w^2)) + O(m^{-2})` for `\|lam\| <= K/m`. Proof exists at detailed-sketch level (odd-cumulant cancellation at the tilted mean + the same kernel); uniform-in-`lam` constants not written. Part (ii) was used *silently* by draft C (referee flaw) and left a coverage hole in draft S (referee flaw); here it is stated explicitly as the single load-bearing gapped proposition. | **major-technical** (this is the spec's "genuinely new part", obligation 3; the structural ideas — tilt invariance, variance domination, deficit monotonicity — ARE fully proved, only the LCLT bookkeeping in the tilted frame is missing) | rigor of (a)'s lower bound; (b)'s `O(m)` localization; (c) | Repeat §1–§2 for the tilted factors (truncated geometrics): all cumulants closed-form (Lemma 3.2-clt), exact tilted-cf identity `\|1-e^{it-lam}\|^2 = (1-e^{-lam})^2 + 2e^{-lam}(1-cos t)` gives the cf decay; state for `\|lam\| <= K/m` with K fixed (kills draft-S's `[1/m, 3.7/m]` hole) and for `sigma_lam^2 >= C_0` (crude). Numerically the claim is superbly supported (NC-9). |
| **G3** | **Part (b) fine scale**: from `\|argmin - N/2\| <= Cm` down to `<= 1`. No draft has a working route; genuinely open. | **major / open** (the only obligation with no complete plan) | (b) as frozen, for `m > 150` | Two routes. **R1 (preferred):** prove `k -> r_m(k)` is nonincreasing on `[1, floor(N/2)]` (⇔ `I(k)^3 I(k+2) >= I(k+1)^3 I(k-1)` on the half-line, a third-difference/PF_3 statement); verified exactly, ZERO violations for `5 <= m <= 56` (NC-11); natural attack: 3x3-minor Cauchy–Binet version of the elementary draft's §2 toolkit. **R2:** even-order Edgeworth pushed to relative error `O(m^{-4})` (the microscopic gain between `\|x\|=1` and `\|x\|=2` is `~ B_m/sigma^6 = Theta(m^{-7})` vs `D ~ m^{-3}`); heavy but finite, all cumulants explicit from Lemma 1.3. |
| **G4** | **Part (c) explicit constants + threshold**: needs G1+G2 with named constants, then `sigma^2(r_m-1) >= 1 - 1.08/m - C'/m^2 - (far-region additive error)` for `m >= m_1`, plus the exact finite check below `m_1`. The binding constraint is NOT the center (`1-1.08/m - C'/m^2 >= 187/216` already for `m >= 9..17` even with `C'` up to 20, NC-13) but the **far-region bound**: the proved `2e^{-0.1931m}` (Lemma 1.4) beats 10% of the signal `sigma^{-4} ~ 1296/m^6` only from `m_0 = 130` (NC-13). Harness is now exact to `m = 150 >= m_0` (NC-1), so the finite check is **already done** for the projected threshold. | major but mechanical-in-principle | (c) | Chase G1+G2 constants; if any constant lands large, either sharpen Lemma 1.4 (true decay is `e^{-c m log m}`-type: measured `\|phi\| <= 1.1e-16` at `m=40` vs bound `8.8e-4`) or extend the harness (exact run to `m=200` is minutes). |
| **G5** | Minor/cosmetic: lattice `±1` slops in continuous-style estimates; `N`-odd forced central tie (`r(floor(N/2)) = r(ceil(N/2))` exactly — the profile is *non-decreasing* away from the center, with exactly one flat step when `N` is odd, not "strictly increasing"); Lemma 3.6's edge chain has zero slack at its threshold (`m = 16k^2` is exact equality). | minor | nothing structural | note-level fixes, done in the statements below. |

**Statement corrections to the frozen spec (exact, verified — propagate upstream):**

1. Part (c)'s suggested `c = 7/8` is **FALSE at m = 6**: exactly
   `sigma_6^2 (r_6 - 1) = (85/12)(11/90) = 187/216 = 0.8657407... < 7/8`
   (`I_6(6) = 90`, `I_6(7) = I_6(8) = 101`, `r_6 = 101/90`). The sequence
   `sigma^2(r_m-1)` is NOT increasing at `m = 5 -> 6` (`7/8 -> 187/216`); it is strictly
   increasing on `6 <= m <= 150`. Corrected sharp target: **`c = 187/216`, attained at
   `m = 6`** (equivalently `c = 7/8` for `m in {5} ∪ {7, 8, ...}`). All four blind drafts
   found this independently; all four referees verified it.
2. Part (b)'s parenthetical "argmin = floor(N/2) for all 4 <= m <= 40" is false at
   `m = 4`: the ratio row is `9/5, 25/18, 36/25, 25/18, 9/5`, argmin is `k = 2` (tied
   with `k = 4`), not `floor(N/2) = 3`. Correct: argmin `= floor(N/2)` for
   `5 <= m <= 150`; at `m = 4`, `|argmin - N/2| = 1`, so the frozen inequality
   `|k - N/2| <= 1` itself is fine for all `m >= 4`.

**Status by obligation:**

| Spec obligation | Status |
|---|---|
| 1. Local expansion, explicit error | Prop 2.1 — structure complete, all analytic ingredients fully proved (L1.3 repaired, L1.4 replaced); constants = G1 |
| 2. Central ratio (CJZ transfer) | Prop 2.2/Cor 2.3 — done modulo G1; sharp form `sigma^2(r_c-1) = 1 - (27/25)/m + O(m^{-2})`, verified to 6 digits |
| 3. Global tail argument | §3 tilting: structural lemmas FULLY PROVED (3.2, 3.3, 3.6); LCLT bookkeeping = G2. Assembly (Thm A) repaired to a constant-`y_0` handoff |
| 4. (b) argmin centrality | exact for `4 <= m <= 150`; `O(m)` localization modulo G1+G2(ii); scale-1 statement = G3 (open) |
| 5. (c) explicit constant | corrected target `187/216`; reduced to G1+G2 constant chase + finite check (finite check done to 150); = G4 |

**Overall verdict: MAJOR GAPS** — (a) is proved modulo two standard-machinery gaps
(G1, G2) with every structural ingredient fully proved and referee-verified; (b) beyond
`m = 150` and (c) are honestly open (G3, G4).

---

## 0. Ground truth

NUMERIC CHECK (NC-1): `python3 mahonian.py --mmax 40` — argmin central for all
`4 <= m <= 40`; min ratio = central ratio for `m >= 5`; `varfit = sigma^2(r_m-1)`
runs `0.8426 (m=4), 0.8750 (5), 0.8657 (6), 0.8766 (7), ..., 0.9734 (40)`.
Merge-editor extension (exact rationals, `extend150.py`): for all `5 <= m <= 150`,
argmin `= floor(N/2)`, `varfit >= 187/216` with equality only at `m = 6`, and `varfit`
strictly increasing on `6 <= m <= 150` (`varfit(150) = 0.99282`). **Re-run: PASS.**

---

## 1. Exact structure (everything in this section is fully proved)

### Lemma 1.1 (factorization and inversion).
For `t in (-pi, pi]`, with `phi(t) := E e^{it(inv - N/2)}`:

```
phi(t) = prod_{j=2}^{m} sin(jt/2) / (j sin(t/2)),      p(k) = (1/2pi) ∫_{-pi}^{pi} phi(t) e^{-itx} dt,
```

`phi` real, even (`inv = sum U_j`, `U_j ~ Unif{0..j-1}` independent, via the inversion
table; each centered factor is `sin(jt/2)/(j sin(t/2))`; lattice Fourier inversion).

NUMERIC CHECK (NC-2): midpoint quadrature reproduces `p(k)` to `<= 7e-18` at `m=10`
(referee-clt re-run confirmed; not re-run by merge editor — exactness is structural).

### Lemma 1.2 (cumulants).
Odd cumulants vanish. `sigma^2 = (S_2 - m)/12`; `kappa_4 = -(S_4 - m)/120 < 0`
(per factor: `Unif{0..j-1}` has `kappa_4 = -(j^4-1)/120`); hence `B_m` as displayed
above, `B_m -> 27/(25m)`.

NUMERIC CHECK (NC-3): `m (1 - sigma^2(r_c - 1))` = `0.953 (m=10), 1.038 (20),
1.065 (40), 1.071 (60), 1.075 (100), 1.076 (120)` -> `27/25 = 1.08` with `O(1/m)`
drift. **Re-run: PASS.**

### Lemma 1.3 (log-series, Gaussian domination, remainder — REPAIRED, now fully proved).
For `0 < |t| < 2pi/m` every factor of `phi` is positive and, with
`a_r = zeta(2r)/(r pi^{2r}) > 0` (`a_1 = 1/6, a_2 = 1/180, a_3 = 1/2835`) and
`S*_{2r} := S_{2r} - m = sum_{j=2}^m (j^{2r} - 1)`:

```
-log phi(t) = sum_{r>=1} a_r (t/2)^{2r} S*_{2r}   (all terms positive),
r=1 term = sigma^2 t^2/2,   r=2 term = -kappa_4 t^4/24 .
```

(i) **(Gaussian domination)** `0 < phi(t) <= e^{-sigma^2 t^2/2}` on `|t| <= 2pi/m`.

(ii) **(remainder)** Let `R(t) := -log phi(t) - sigma^2 t^2/2 + kappa_4 t^4/24 >= 0`
(the `r >= 3` tail). Then for `m >= 3`:

```
R(t) <= (m+1)^7 t^6 / 635040      for |t| <= sqrt(2) pi / m,
R(t) <= (m+1)^7 t^6 / 952560      for |t| <= pi / m.
```

*Proof of (ii) — this repairs the broken steps in BOTH Fourier drafts.* The ratio of
consecutive series terms is `(a_{r+1}/a_r) (t/2)^2 (S*_{2r+2}/S*_{2r})`. First,
`a_{r+1}/a_r = zeta(2r+2) r / (zeta(2r)(r+1) pi^2) < 1/pi^2`. Second, the **summed**
inequality `S*_{2r+2} <= m^2 S*_{2r}` holds for `m >= 3, r >= 1`: termwise,
`m^2(j^{2r}-1) - (j^{2r+2}-1) = j^{2r}(m^2 - j^2) - (m^2-1)`, which is `>= 0` for
`2 <= j <= m-1` (at `j=2`: `4^r(m^2-4) >= 4m^2-16 >= m^2-1` for `m >= 3`; at `j=m-1`:
`(m-1)^{2r}(2m-1) >= (m-1)^2(2m-1) >= m^2-1` for `m >= 2`; the interior is larger),
and the single negative `j=m` term, `-(m^2-1)`, is covered by the `j=2` surplus
`>= 3m^2 - 15 >= m^2 - 1` (`m >= 3`). Hence the term ratio is `<= (mt/2)^2/pi^2`,
which is `<= 1/2` for `|t| <= sqrt2 pi/m` and `<= 1/4` for `|t| <= pi/m`; the tail is
at most `2×` (resp. `4/3 ×`) its first term, and the first term is
`a_3 (t/2)^6 S*_6 <= (t^6/64)((m+1)^7 - 128)/(7·2835)` by `sum_{j=2}^m j^6 <=
∫_2^{m+1} x^6 dx`. Multiplying: `2/(2835·64·7) = 1/635040`, `(4/3)/(2835·64·7) =
1/952560`. ∎

NUMERIC CHECK (NC-4), exact positive series via mpmath (`r2_series.py`, no float
cancellation): `max R/((m+1)^7 t^6/952560)` on `(0, pi/m]`, `4 <= m <= 40`: **0.810**
(at m=40); on the wider range `max R/((m+1)^7 t^6/635040) <= max R·317520/(m^7t^6)
= 0.818` (at m=4); asymptotic check at `m = 60..400`: ratio drifts to `~0.887 < 1`
from both sides. Also confirmed: the ORIGINAL saddle-draft constant `m^7/952560` is
**false** for `m <= 29` (ratio 1.90 at m=4), and the original clt-draft proof step
`S_{2K}-m <= 2m^{2K+1}/(2K+1)` is false (m=4, K=3) though its stated bound
`m^7 t^6/317520` happens to hold numerically — the proved bound above implies it for
`m >= 10` (`((m+1)/m)^7 <= 2`). **Re-run: PASS.**

### Lemma 1.4 (far-region decay — draft-S version; the clt draft's version is discarded).
For `t in [2pi/m, pi]`:

```
|phi(t)| <= prod_{j=2}^m min(1, pi/(jt))   and   |phi(t)| <= 2 exp(-(log 2 - 1/2) m) = 2 e^{-0.19314 m}.
```

*Proof.* `|sin(jt/2)| <= 1`, `sin(t/2) >= t/pi` on `[0, pi]`; at `t = 2pi/m` the
factors `j > m/2` give `log prod <= -∫_{m/2}^m log(2x/m) dx + log 2`; the product bound
is nonincreasing in `t`. ∎ (Referee-verified sound. The clt draft's stronger-looking
clause "`|phi| <= e^{-m/6}` for `m >= 25`" did NOT follow from its own bound — the
inequality first holds near `m ≈ 280` — and is discarded.)

NUMERIC CHECK (NC-5): `max_{[2pi/m, pi]} |phi|` = `3.3e-5 (m=10), 3.9e-9 (20),
6.2e-13 (30), 1.1e-16 (40), 3.3e-24 (60)`; bound = `2.9e-1, 4.2e-2, 6.1e-3, 8.8e-4,
1.9e-5`. Holds everywhere with enormous slack — the slack is exactly what G4 would
harvest if the constant chase needs it. **Re-run: PASS.**

### Lemma 1.5 (second-difference kernel — exact; the honest CJZ transfer device).
For `D(k) := p(k)^2 - p(k-1)p(k+1)`:

```
D(k) = (1/4pi^2) ∫∫_{[-pi,pi]^2} phi(s) phi(t) cos((s+t)x) (1 - cos(s-t)) ds dt .
```

*Proof.* Expand each `p` by Lemma 1.1 and symmetrize `1 - e^{i(s-t)}` in `(s,t)`. ∎

**Why this is load-bearing:** the additive error of any pointwise expansion is
`Theta(sigma^{-1} m^{-2})`, LARGER than the signal `D(k) ~ sigma^{-4}`; second
differences must be taken *inside* the integral, where the kernel
`1 - cos(s-t) <= (s-t)^2/2` supplies the `sigma^{-2}` for main and error terms alike.
This kernel — not any theorem quoted from CJZ (their Thm 4.6/eq. (4.11) is for the
central Gaussian binomial ONLY and is nowhere invoked as a citation doing work) — is
the legitimate q-factorial transfer. The pro draft's alternative (second-differencing
its pointwise expansion (3.1)) is arithmetically impossible (`Theta(m^{-2})` error vs
an `O(m^{-5})` target) and is discarded; see §6.

NUMERIC CHECK (NC-2b): identity verified to 12 significant digits at `m=8, k=14,18`
(two independent referees; exact algebra also checked by hand).

---

## 2. Central window (obligations 1 and 2)

### Proposition 2.1 (pointwise local expansion; constants = G1).
With `He_4(y) = y^4 - 6y^2 + 3`, for every `k`:

```
p(k) = (sigma sqrt(2pi))^{-1} e^{-y^2/2} [1 - (B_m/12) He_4(y)] + E(k),   |E(k)| <= C_1/(sigma m^2).
```

*Proof scheme (complete; the constant `C_1` is G1).* Split the inversion integral at
`t_2 = m^{-5/4}`, `sqrt2 pi/m`, `2pi/m`, `pi`; on `[0, t_2]` use Lemma 1.3(ii) (now
fully proved) and Gaussian–Hermite moment integrals; `[t_2, 2pi/m]`: Lemma 1.3(i),
super-polynomially small; `[2pi/m, pi]`: Lemma 1.4 — `2e^{-0.193m}` is
super-polynomially small, uniformly, with a fully proved constant (this replaces the
clt draft's broken `m >= 25` invocation, so the scheme now has no unproved analytic
input). ∎

NUMERIC CHECK (NC-6a): `sup_{|y|<=3} (rel. error) · m^2 = 6.96, 6.30, 6.09, 6.01` at
`m = 20, 30, 40, 60` (referee-verified; consistent with the omitted `He_6`/`He_4^2`
next-order terms).

### Proposition 2.2 (window law — stated at CONSTANT `y_0`; the sqrt(log m)-window
version of draft C is discarded as false).
Fix any constant `y_0 >= 1`. For `|y| <= y_0` and `m >= m_1(y_0)`:

```
sigma^2 log r(k) = 1 + B_m (y^2 - 1) + E_1(k),      |E_1(k)| <= C_2(y_0)/m^2 .
```

*Proof scheme.* Insert `phi_model = e^{-sigma^2 t^2/2}(1 + kappa_4 t^4/24)` into
Lemma 1.5, rotate `u = s+t, v = s-t` (1-D Gaussian moments; the pure Gaussian part
gives `D/p^2 = 1 - e^{-1/sigma^2}`, whence the leading `1`; the `kappa_4` part gives
exactly `B_m(y^2-1)` at first order), and transfer the Lemma 1.3(ii)/1.4 remainders
through the kernel (relative errors stay relative). Full bookkeeping = **G1**. ∎

**Merge resolution of a constants disagreement.** Draft C claimed effective error
constant `~0.2` (against shape `(1+y^6)e^{y^2}/m^2`); draft S claimed `0.4` against
`(1+y^6)/m^2`; referee-S measured `~0.69`. Merge-editor re-run (NC-6): against
`(1+y^6)/m^2` on `|y| <= 3`, the needed constant is `0.65 (m=6), 0.71 (10), 0.69 (20),
0.686 (30), 0.686 (40)` (worst near `|y| ≈ 0.8`, where the true next-order term is
`y^2`-dominated). **Use `C_2 = 0.75` for `|y| <= 3` as the calibrated target; at
`y = 0` the needed constant is `0.19`.** Draft S's `0.4` is wrong; draft C's `0.2`
referred to a different (exponentially inflated) shape and is misleading — both
superseded by this line.

NUMERIC CHECK (NC-6): as just stated; command pattern:
```
python3 - <<'EOF'
import math; from mahonian import mahonian
for m in (10,20,30,40):
    a=mahonian(m); N=m*(m-1)//2; s2=m*(m-1)*(2*m+5)/72; s=math.sqrt(s2)
    c4=sum(j**4-1 for j in range(2,m+1))/2880; B=12*c4/s2**2
    la=[math.log(x) for x in a]
    print(m, max(abs(s2*(2*la[k]-la[k-1]-la[k+1])-(1+B*(((k-N/2)/s)**2-1)))/((1+((k-N/2)/s)**6)/m**2)
                 for k in range(1,N) if abs((k-N/2)/s)<=3))   # -> 0.71, 0.69, 0.686, 0.686
EOF
```
**Re-run: PASS (with the corrected constant).**

**Why constant `y_0` and not `sqrt(log m)`:** at `y^2 = log m` the error term
`C_2(1+y^6)e^{y^2}/m^2 ~ C_2 log^3 m / m` EXCEEDS the growth `B_m y^2 ~ 1.08 log m/m`
by `~ log^2 m` — for every `m` (referee-verified at `m = 30 .. 10^6`). Draft C's
Corollary 2.4(ii)/(iii) passed through this hole; the constant-`y_0` split (with the
tilt taking over at `|y| >= y_0`, §4) is the repair.

### Corollary 2.3 (central ratio, sharp form).
`sigma^2 (r_m(k_c) - 1) = 1 - B_m + O(m^{-2}) = 1 - (27/25) m^{-1} + O(m^{-2})`
(at `k_c`, `|y| <= 1/(2sigma)`, so `B_m y^2` is negligible; `e^{D} - 1` vs `D`
contributes `+D^2/2 = O(sigma^{-2})` relative, absorbed).

NUMERIC CHECK (NC-7): `sigma^2 log r(k_c)` vs `1 - B_m`, residual `× m^2`:
`-0.05 (m=6), -0.10 (10), -0.17 (20), -0.19 (30), -0.19 (40)` — the `O(m^{-2})` shape
is exact; predicted varfit at `m=40`: `0.973381` = harness value to 6 digits.
**Re-run: PASS.**

---

## 3. Global mechanism: tilting (obligation 3)

### Lemma 3.1 (tilt invariance).
For `theta = e^{-lam} > 0`, `I_lam(k) := I_m(k) theta^k` has the same ratios
`r(k)`; normalized, it is the Mallows/q-Mahonian law, a sum of independent truncated
geometrics on `{0,...,j-1}`. The tilted mean `mu(lam)` satisfies
`mu'(lam) = -sigma_lam^2 < 0`, so for every interior `k` there is a unique `lam(k)`
with `mu(lam(k)) = k`: **the ratio at `k` is the central ratio of a tilted measure
sitting at its own mean.** (Trivial + standard; verified.)

### Lemma 3.2 (tilted variance domination — FULLY PROVED).
For every `j >= 2` and `lam != 0`: `Var_lam(U_j) < (j^2-1)/12`; hence
`sigma_lam^2 < sigma^2`.

*Proof (draft-pro version — shortest of the three independent full proofs, referee
verdict "publishable as-is").* `v_j(t) = (1/4)[csch^2(t/2) - j^2 csch^2(jt/2)]`;
it suffices that `h(u) = u^3 coth(u) csch^2(u)` is strictly decreasing on `(0,∞)`,
since then `j^3 coth(js)csch^2(js) < coth(s)csch^2(s)` (`s = t/2`, `j >= 2`).
`h'/h = 3/u + tanh u - 3 coth u`, and `h' < 0 ⟺ F(u) := 3u + 2u sinh^2 u
- 3 sinh u cosh u > 0`: `F(0) = 0` and `F'(u) = 4 sinh u (u cosh u - sinh u) > 0`. ∎

### Lemma 3.3 (deficit monotonicity — FULLY PROVED; sign wording corrected).
`lam -> sigma_lam^2` is even and nonincreasing in `|lam|`; the deficit
`sigma^2 - sigma_lam^2` is **nondecreasing** in `|lam|`. *Proof:* reduces to
`u(x) = x^3 cosh x / sinh^3 x` **nonincreasing** (note: the per-factor quantity
`g = -2u` is then nondecreasing — draft S had the two words swapped, conclusion
unaffected), i.e. `3 sinh y <= y cosh y + 2y` (`y = 2x`), which holds termwise in the
power series (`3/(2n+1)! <= 1/(2n)!` for `n >= 1`; `n = 0` covered by `2y`). ∎

### Lemma 3.4 (quantitative deficit; mean–tilt dictionary).
With `w := lam m`: `1 - sigma_lam^2/sigma^2 = (3/100) w^2 (1 + O(w^2) + O(1/m))`
(coefficient `= |kappa_4|/(2 sigma^2 m^2) -> 3/100`, i.e. `= B_m sigma^2/m^2`), and
`|x(lam)| = |mu(lam) - N/2| <= lam sigma^2`, so `y ≈ w sqrt(m)/6`. For every
`w_0 > 0` there is `rho(w_0) < 1` with `sigma_lam^2 <= rho sigma^2` for
`|w| >= w_0` (Lemma 3.3 + continuity). (Small-`w` part verified to 3% at `m = 40`;
consistency: `(3/100)w^2 = B_m y^2` exactly at leading order — the tilt-deficit and
the window's `y^2`-growth are the SAME `kappa_4` phenomenon, a strong internal
cross-check, and identical to the elementary draft's `m^4/240` one-step excess.)

### Proposition 3.5 (tilted window law — the single gapped global engine; = G2).
There are absolute `C_0, K, C` such that for all interior `k`:

(i) *(crude, uniform)* if `sigma_lam^2 >= C_0` (`lam = lam(k)`):
    `r(k) - 1 = sigma_lam^{-2} (1 + theta C / min(m, sigma_lam^2))`, `|theta| <= 1`;

(ii) *(refined, small tilt)* if `|lam| <= K/m`:
    `sigma_lam^2 (r(k) - 1) = 1 - B_m (1 + O(w^2)) + O(m^{-2})`.

*Proof status:* detailed sketch — repeat §1–§2 for the tilted factors: all tilted
cumulants closed-form; cf decay from `|1 - e^{it-lam}|^2 = (1-e^{-lam})^2 +
2e^{-lam}(1-cos t)`; at the tilted mean all odd Edgeworth terms cancel in the
symmetric second difference, and the kernel (Lemma 1.5, verbatim in the tilted frame)
keeps errors relative. **GAP G2** (uniform constants not written). Statement (ii) is
what draft C used without stating and what closes draft S's `lam ∈ [1/m, 3.7/m]`
coverage hole (state (i) for ALL `sigma_lam^2 >= C_0` and (ii) on the full `K/m`
range with `K` free — the two ranges then overlap for any `K >= 1`).

NUMERIC CHECK (NC-9, merge re-run, m=30): `sigma_lam^2 (r(k)-1)` at
`k = 216, 210, 200, 160, 120, 40, 5`: `0.9648, 0.9647, 0.9646, 0.9631, 0.9615,
0.9669, 0.9677` — uniformly `≈ 1 - 1.08/30 = 0.964` across the entire bulk while
`sigma_lam^2` falls from `785` to `5.8`. **Re-run: PASS** (this is the strongest
empirical fact in the whole problem: the tilted profile is FLAT at `1 - B_m`).

### Lemma 3.6 (extreme edge — pentagonal; FULLY PROVED).
For `0 <= k <= m`, exactly `I_m(k) = sum_n (-1)^n T(k - g_n)`,
`T(j) = C(m-1+j, m-1)`, `g_n = n(3n-1)/2`; and `T(k)^2/(T(k-1)T(k+1)) =
1 + (m-1)/(k(m+k))` exactly. Consequently, for `1 <= k <= sqrt(m)/4`, `m >= 16`:

```
r(k) - 1 >= (m-1)/(2k(m+k)) >= 1/(6k)  >>  1/sigma^2 .
```

(Bracketed-pairs comparison `T(k)(1 - 2k/m) <= I(k) <= T(k)`; the chain has zero
slack at `k = sqrt m/4` exactly — G5 note.) NUMERIC CHECK (NC-10):
`min_{1<=k<=m} (r(k)-1) k(m+k)/(m-1) = 1.0025 (m=30), 1.0013 (m=40)`; pentagonal
identity exact at `m=20`, all `k <= m`. **Re-run: PASS.**

---

## 4. Synthesis

Throughout `k <= N/2` WLOG (`r(N-k) = r(k)`).

### Theorem A (= F2(a), sharp form; modulo G1 + G2).

```
sigma^2 (r_m - 1) = 1 - (27/25) m^{-1} + O(m^{-2});   in particular  r_m = 1 + sigma^{-2}(1 + o(1)),
equivalently r_m - 1 ~ 36/m^3 .
```

*Proof (repaired assembly; the regime handoff is at a CONSTANT `y_0`).* Fix the G2
constants `C_0 > C`, `K`; choose the constant `y_0^2 := max(1, (25/27)(C_G - 1.08))`
where `C_G` is the combined G1/G2 error constant (this is the constant-aware handoff
that repairs the referee-flagged "factor-m gap" fallacy — at the inner edge the
comparison is between CONSTANTS, `≈ 0.90` available vs `1.08` needed empirically,
with ~20% headroom, not a factor of `m`).

1. `1 <= k <= sqrt(m)/4`: Lemma 3.6 — `r(k)-1 >= (2/3)m^{-1/2} >> sigma^{-2}`.
   (Fully proved, no gaps.)
2. `sqrt(m)/4 <= k`, `sigma_lam^2 <= rho sigma^2` (`rho < 1` from Lemma 3.4 at
   `w_0 = w(y_0)`): Prop 3.5(i) + Lemma 3.2:
   `r(k)-1 >= (1 - C/min(m, sigma_lam^2)) sigma_lam^{-2} >= (1+delta) sigma^{-2}`
   once `min(m, sigma_lam^2) >= C_0` large; for bounded `sigma_lam^2 in [C_0, K']`
   the middle expression is `>= (1-C/C_0)/K' >> sigma^{-2}`. (Needs
   `sigma_lam^2 >= C_0` for `k >= sqrt m/4` — order-plausible `sigma_lam^2 ≍ k(1+k/m)`,
   filed inside G2.)
3. `sigma_lam^2 >= rho sigma^2` (equivalently `|y| <= O(y_0)`, small tilt): Prop
   3.5(ii) + Lemmas 3.3/3.4:
   `sigma^2(r(k)-1) >= (1 + (3/100)w^2(1-o(1)))(1 - B_m(1+O(w^2)) - O(m^{-2}))
   >= 1 - B_m - O(m^{-2}) + w^2[(3/100) - o(1) - O(B_m)] >= 1 - B_m - O(m^{-2})`,
   with equality-shape attained at `w = 0`, i.e. at the center, where Cor 2.3 gives
   the value `1 - B_m + O(m^{-2})`.

Min over all three regions = central value. ∎ **Status: complete modulo G1
(region-3 constants) and G2 (regions 2–3 machinery).** The weak form
`1 + sigma^{-2}(1+o(1))` needs the same two gaps — there is no gap-free route to (a)
in any of the four drafts; the alternative saddlepoint mechanism (pro Lemma 6,
`Phi'' = -1/B` + Lemma 3.2 here) gives an independent second path to region 2, but
carries its own tail split (its log-B second difference is `-3759 sigma^{-2}` at
`k=1, m=20` — referee measurement — so `k = O(1)` must be handled by Lemma 3.6
regardless; kept as a backup route inside G2).

NUMERIC CHECK (NC-1, NC-3, NC-7, NC-9) jointly instantiate every regime of this
proof. **All re-run: PASS.**

### Theorem B (= F2(b); partial — localization `O(m)`, fine scale open).

(i) *(exact, finite)* For `4 <= m <= 150`: `|argmin - N/2| <= 1`, indeed argmin
`= floor(N/2)` for `5 <= m <= 150` (and the min ratio EQUALS the central ratio for
`m >= 5`); at `m = 4` the argmin is `k = 2` (tied with 4), `|k - N/2| = 1`. (NC-1.)

(ii) *(asymptotic, modulo G1 + G2)* `|argmin - N/2| <= C' m` for `m >= m_1`:
by Theorem A's region 3, a minimizer must satisfy
`(3/100) w^2 (1 - o(1)) <= O(B_m w^2) + C_G/m^2`, forcing `w <= c/m`, i.e.
`|x| <= (c/m)·sigma^2/m ≍ m/36 · c`. Note `O(m) = o(sigma)`: argmin`/N -> 1/2`.
(Without Prop 3.5(ii) — i.e. with only the crude (i) — one gets `O(sigma)`; the
refined form is exactly what buys `O(m)`. This dependence was hidden in draft C and
is now explicit.)

(iii) *(fine scale, `Cm -> 1`)* **OPEN = G3.** Preferred route R1 (unimodality of
`k -> r_m(k)` on the half-line): NUMERIC CHECK (NC-11, merge re-run, exact integers):
`I(k)^3 I(k+2) >= I(k+1)^3 I(k-1)` for all `1 <= k < floor(N/2)`, all `5 <= m <= 56`,
ZERO violations (`m = 4` has exactly one, at `k = 2`); for `N` odd there is exactly
one forced flat step at the center. **Re-run: PASS.** This single inequality implies
(b) in full for all `m` at once and is a clean, self-contained combinatorial target
(third-difference of `log I_m` single-signed on each half; PF_3 / 3x3 Cauchy–Binet
via the elementary draft's boundary identities is the suggested attack). Route R2
(microscopic Edgeworth to relative `O(m^{-4})`) is available in principle from Lemma
1.3's exact series but heavy.

### Theorem C (= F2(c); corrected target; reduction only — OPEN = G4).

The spec's `c = 7/8` is FALSE (correction 1 above). Corrected statement to prove:

```
r_m >= 1 + (187/216)/sigma_m^2   for all m >= 5, with equality iff m = 6 .
```

*Reduction.* Exact for `5 <= m <= 150` (NC-1, rational arithmetic — a legitimate
proof step). For `m > 150`: Theorem A's chain with explicit G1+G2 constants gives
`sigma^2(r_m-1) >= 1 - 1.08/m - C'/m^2 - (additive far-region term)`. Center margin
is cheap: `1 - 1.08/m - C'/m^2 >= 187/216` for `m >= 9 / 12 / 17` at
`C' = 1 / 5 / 20` (NC-13). The binding constraint is the far region: the PROVED
Lemma 1.4 bound `2e^{-0.1931m}` is `<= 0.1 × 1296/m^6` (10% of the signal) only for
`m >= 130` (NC-13) — hence the harness extension to 150. So (c) closes if and only
if the G1+G2 constant chase lands `m_1 <= 150` (projected: `m_1 ≈ 130–140` from the
far region; extendable — exact harness to `m = 200` costs minutes). **Not closed
here; no false conditionality is claimed** (the elementary draft's induction route to
(c) is discarded — its one-step lemma is false as stated, §6).

---

## 5. Numeric-check index (merge-editor re-runs, 2026-07-06)

| # | Claim | Result |
|---|---|---|
| NC-1 | harness exact to m=150: argmin=floor(N/2) (m>=5), varfit >= 187/216 (eq. iff m=6), strictly incr. 6..150; m=4: argmin=2, ratio 25/18 | **PASS** |
| NC-3 | `m(1-varfit_c) -> 27/25`: 0.953 → 1.076 (m=10→120) | **PASS** |
| NC-4 | repaired remainder: max ratio 0.81 vs `(m+1)^7/952560` (exact series, m<=40; drift to 0.887 at m<=400); original `m^7/952560` FALSE m<=29 | **PASS** |
| NC-5 | far region: max\|phi\| ≤ 2e^{-0.1931m}, m=10..60 (slack 4–8 orders) | **PASS** |
| NC-6 | window-law error constant vs `(1+y^6)/m^2`, \|y\|<=3: needed 0.65–0.71 (use 0.75); at y=0: 0.19 | **PASS (resolves 0.2/0.4/0.69 dispute)** |
| NC-7 | center residual `× m^2` in [-0.19, -0.05], m=6..40 | **PASS** |
| NC-9 | tilted flatness: `sigma_lam^2 (r(k)-1)` ∈ [0.9615, 0.9677] across k=5..216 at m=30 | **PASS** |
| NC-10 | pentagonal identity (m=20, exact); edge bound min 1.0013 (m=40) | **PASS** |
| NC-11 | unimodality of r_m(k): zero violations 5<=m<=56; m=4: one (k=2) | **PASS** |
| NC-13 | (c) feasibility: far-bound crossover m=130; center margin m0 = 9/12/17 at C'=1/5/20 | **PASS** |

(NC-2/2b, NC-6a, NC-8: exact-representation and Edgeworth-accuracy checks re-run by
the four referees and accepted; not repeated by the merge editor.)

---

## 6. Discarded paths (do not resurrect without the stated repair)

1. **Elementary draft, Theorem 4.2 (one-step convolution lemma): FALSE as stated.**
   Exact counterexample (referee): `b = I_6` (log-concave, support width 16),
   `a = b * u_18` has `a(15..17) = 720, 720, 720`, so `r_a(16) = 1` exactly, `c' = 0`
   — defeats every choice of absolute constants; smooth peaked variants show no
   absolute constants can exist. Any revival needs an anti-concentration/width
   hypothesis carried THROUGH the §5 induction (nontrivial). Its §2 exact identities
   (boundary formula, Cauchy–Binet positivity) are correct, referee-verified, and
   retained as the toolkit for G3-R1. Its `m^4/240` excess law is the same `kappa_4`
   mechanism as `B_m` (cross-check, §3.4).
2. **Pro draft, Lemma 3 eq. (3.2):** second-differencing a pointwise expansion with
   `Theta(m^{-2})` error cannot bound a `Theta(m^{-3})` quantity to `O(m^{-5})`;
   replaced by the kernel (Lemma 1.5). Pro Lemma 6's "log B second difference is
   `o(sigma^{-2})` uniformly" is false in the tail (measured `-3759 sigma^{-2}` at
   `k=1, m=20`); the `Phi''`-mechanism survives only with a `k = O(1)` split
   (Lemma 3.6 covers it).
3. **Clt draft, Lemma 1.4 "in particular" clause and Cor 2.4(ii)/(iii)
   sqrt(log m)-window comparison:** both false as written (referee-verified, the
   latter for every `m` up to `10^6`); replaced by Lemma 1.4 (draft-S bound) and the
   constant-`y_0` handoff of Theorem A.
4. **Saddle draft, Lemma 4.5(i)/(ii) synthesis:** the stated ranges left
   `lam ∈ [1/m, ~3.7/m]` (61 values of k at m=30) covered by neither; fixed by
   stating Prop 3.5(i) uniformly in `sigma_lam^2 >= C_0` and (ii) on `|lam| <= K/m`.
5. **Both Fourier drafts' remainder-constant proofs** (`2m^{2K+1}/(2K+1)` step;
   `m^7/7` for `sum j^6`): false; replaced by the fully proved Lemma 1.3(ii) above.

## 7. Citations

- Bóna, Electron. J. Combin. 11(2) (2004/05) #N2 (log-concavity, direct); Hoggar,
  JCTB 16 (1974) / Kook (2006) (product closure). Used only as the ambient fact
  `r(k) >= 1`; every quantitative statement here is self-contained.
- Canfield–Janson–Zeilberger, Adv. Appl. Math. 46 (2011), arXiv:0908.2089, Thm 4.6 /
  eq. (4.11): method precedent for Lemma 1.5's kernel; their theorem (central
  Gaussian binomial) is NOT invoked as a citation carrying weight — all four
  referees confirm no illegal transfer in the retained material.
- Petrov, *Sums of Independent Random Variables*, Ch. VII: the G1/G2 bookkeeping
  framework.
- The hyperbolic inequalities of §3.2–3.3 ("among all exponential tilts of a discrete
  uniform, the untilted one has maximal variance, monotonically in the tilt") appear
  to be new as stated and independently useful.

*End of merged draft.*
