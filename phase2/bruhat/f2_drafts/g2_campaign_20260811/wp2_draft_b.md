# wp2-b — T.9's Taylor-remainder bucket, the w^2-envelope audit, and the assembled C_R(K) table

*Work package wp2-b (T2 Section-8 item 4, bucket 2 of 2 + assembly), 2026-08-11.
Blind protocol: this draft was written from `F2_PROOF_DRAFT.md` (merged draft),
`g1_draft_b.md` (refereed SURVIVES — B.0–B.9 citable), `g2_draft_t2_20260803.md`
(finalized T2 draft — T.1–T.10 citable at the statuses its §8 assigns),
`g2_item1_deep_tilt_notes_20260805.md`, `g2_item4_bucket_notes_20260805.md`, and
the scripts under `g2_scripts/t2/` and `g2_scripts/t2_item4/` (read + re-run
allowed). Nothing under `g2_campaign_undefined/` or
`g2_scripts/campaign_undefined/` other than this file and my own script
directory was read; `g2_draft_t1_20260803.md` was not read. No existing file
was modified.*

*Scripts (all saved and run 2026-08-11, CPython 3.12.2, sympy 1.14.0 /
mpmath 1.3.0 / numpy 1.26.4, macOS):
`g2_scripts/campaign_undefined/wp2_b/wp2b_lib.py` (shared helpers),
`wp2b_nc1_model_poly.py` (NC-W1), `wp2b_nc2_dictionary.py` (NC-W2),
`wp2b_nc3_taylor.py` (NC-W3), `wp2b_nc4_assembly.py` (NC-W4), plus the
generated `wp2b_n0_resid_table.py`. Every number quoted below is from a real
run of one of these; the verbatim output blocks are in §7.*

---

## 0. What this work package delivers, and its honest status

Theorem T.9 (= Prop 3.5(ii), the refined small-tilt law) was left PARTIAL in
`g2_draft_t2` §8 item 4 with three missing mechanical pieces: (1) the
box/tail/out kernel-transfer bucket (B.6-analogue), (2) the Taylor-remainder
bucket (B.7'-analogue), (3) assembly into an explicit `C_R(K)`. The pointwise
bucket (`N_lam(0)` residual) was already grid-certified in
`g2_item4_bucket_notes_20260805.md`. Piece (1) is the parallel work package
wp2-a (blind to me). This draft:

1. **Builds and certifies piece (2)** — Lemma W.4, the Taylor bucket — with a
   fully displayed proof and explicit constants:
   `T(K) = 0.00035 / 0.00100 / 0.01402` for `K = 1 / 2 / 4` at `m >= 180`
   (already `0.02034 / 0.06117 / 1.65299` at `m >= 30`). PROVED (given the
   W.1–W.3 inputs below, one of which is a grid certificate).
2. **Adds the linearization bucket** (`s2(r-1)` vs `s2 log r`) — Lemma W.5:
   `Lin(K) = 0.231 / 0.258 / 0.372` at `m >= 180`. PROVED (conditional, see §4).
3. **Upgrades the pointwise bucket** from grid-only to a closed-form all-`m`
   bound (§6, from the NC-W1 monomial table + NC-W2 boxes):
   `PW_closed(K) = 10.28 / 21.07 / 187.5` at `m >= 180` — alongside the sharper
   grid certificate `PW_grid(K) = 1.5491 / 4.0889 / 4.9126` (independently
   re-run here, reproducing the item-4 notes to 4 digits).
4. **Audits the `w^2`-envelope** (Prop W.6): the proved envelope coefficient is
   `c_w(1) = 0.407`, `c_w(2) = 0.466`, `c_w(4) = 0.951`. **T.9's stated
   `c_w = 1/2` is therefore PROVED for `K = 1, 2` and FALSE-as-proved for
   `K = 4`** (statement-level correction: use `c_w(4) = 1`). A true (not
   bound-artifact) mechanism is identified: `kappa_4(lam)` crosses zero near
   `w ~ 3.3` (measured `kappa_4(lam)/kappa_4(0) = -0.1417` at `m = 60, w = 4`).
5. **Assembles the table** (Theorem W.7): the exact decomposition
   `s2 log r(k) = [my chain] + Delta_ker` with every bucket of mine explicit
   and `Delta_ker` (kernel transfer + denominators) left as the single
   pending, exactly-defined leftover for wp2-a — whose TRUE size I measure
   against the exact harness: `~1.39 / 4.07 / 5.04` in `C_R` units,
   essentially `m`-independent on `m = 30..140`.

**Status of item 4 after this draft: my two buckets + assembly are done;
item 4 closes when wp2-a's kernel bucket lands and is merged into Theorem
W.7's table. Nothing here touches item 5 (the far-region thresholds
`m_2(K)`), which remains the binding constraint of T.9 exactly as stated in
`g2_draft_t2` §8.**

---

## 1. Notation and the tilted 6-term model polynomial

All notation from the merged draft and `g2_draft_t2`: `lambda = sigma^2 =
m(m-1)(2m+5)/72`, `S_r = sum_{j=1}^m j^r`, `B_m = (S_4 - m)/(240 lambda^2)`,
tilt `lam`, `w = lam m`, `lam(k)` the tilted-mean solution, `s2 =
sigma_{lam(k)}^2`, `kappa_r(lam)` the tilted cumulants (closed forms (2.2)–(2.5)
of T.2, extended to `r = 5, 6` by two more derivatives of
`g(u) = 1/u - 1/(e^u - 1)`, as in `t2i4_nc1_model.py`). WLOG `lam >= 0`
(symmetry `a_k = a_{N-k}`). Model coefficients and their scaled versions:

```
alpha = kappa_3/6,  beta = -kappa_4/24,  delta = kappa_5/120,  gamma = kappa_6/720 ,
a = alpha/s2^{3/2},  b = beta/s2^2,  d = delta/s2^{5/2},  g = gamma/s2^3 ,
h = s2^{-1/2},  J = [-h, h] .
```

### Lemma W.0 (model polynomial; sympy-verified, NC-W1).
Truncating `exp(-i alpha t^3 - beta t^4 + i delta t^5 - gamma t^6)` to `O(t^8)`
and Fourier-transforming against `e^{-s2 t^2/2}` via
`(1/2pi) int t^n e^{-s2 t^2/2} e^{-itx} dt = (-i)^n s2^{-n/2} Z(y) He_n(y)`
gives `phat_lam(x) = Z(y) P(y)` with the REAL polynomial

```
P(y) = 1 + a He_3(y) - b He_4(y) + d He_5(y) + (g + a^2/2) He_6(y)
         - a b He_7(y) + (b^2/2 + a d) He_8(y) ,
```

free of `s2` in scaled variables; the untilted limit `a = d = 0` reproduces
`g1_draft_b`'s `P = 1 - b He_4 + g He_6 + (b^2/2) He_8` exactly. With
`B_lam := 12 b` and `N(y) := -P''P + P'^2 - 12 b He_2(y) P^2` (the same
defining relation as B.7 / the item-4 notes),

```
-(log P)''(y) = 12 b He_2(y) + N(y)/P(y)^2 ,     and at y = 0:
N(0) = -36 a^2 + N0_resid ,
N0_resid = -90 g + 384 b^2 + 750 a d - 585 a^2 b + (675/2) a^4      [weight 4]
         + 225 d^2 + 90 b g - 522 b^3 + 1890 a b d + 1350 a^2 g
           + (12105/2) a^2 b^2 - 11025 a^3 d + 675 a^4 b             [weight 6]
         + (13 monomials of weight 8 and 10, table in
           wp2b_n0_resid_table.py) ,
```

where the weight of a monomial counts half-powers of `1/m` (`a ~ m^{-1/2}`,
`b ~ m^{-1}`, `d ~ m^{-3/2}`, `g ~ m^{-2}`): **every residual monomial has
weight >= 4, i.e. `N0_resid = O(1/m^2)`** — sympy-verified, and the bare
`-36 a^2` (weight 2, the `kappa_3^2` term that T.9's Step 2 folds into the
`w^2` bucket) is exactly the item-4 notes' finding. NC-W1 output (§7):
`Im P == 0` symbolically; untilted `N(0)` matches `-90g + 384b^2` plus
weight->=6 terms; the lib's numeric evaluators match sympy to `1e-13`.
**Status: PROVED (finite exact computation, sympy; hand-checkable via
`He_n' = n He_{n-1}`).**

---

## 2. Dictionary lemmas (inputs to every bucket)

Standing hypotheses for the rest of the draft: `m >= 30`, `0 <= w <= K`,
`K in {1, 2, 4}`.

### Lemma W.1 (variance floor up to |w| <= 4).
(i) *(quadratic clause, closed form)* For all real `w` and `m >= 30`:
`1 - s2/lambda <= S_4/(240 m^2 lambda) * w^2 <= 0.0330 w^2`.
(ii) *(floor at K = 4)* For `|w| <= 4`, `m >= 30`: `1 - s2/lambda <= 0.40`.
Consequently `s2 >= c_K lambda` with

```
c_1 = 0.967 ,   c_2 = 0.868 ,   c_4 = 0.60 .
```

*Proof.* From (2.3), `lambda - s2 = lam^2 sum_j [ j^4 E(lam j) - E(lam) ]`
with `E(u) := (1/12 - q(u))/u^2`, `q = -g'` — the kernel of (T.4), for which
the T2 draft's (T.4a'')-block PROVES `0 <= E(u) <= E(0) = 1/240` and `E`
decreasing in `|u|` (partial-fraction summands decrease in `u^2`). Dropping
the positive `+ lam^2 m E(lam)` term:
(i) `lambda - s2 <= lam^2 (1/240) S_4 = (w^2/m^2)(S_4/240)`; divide by
`lambda`; the rational number `coef(m) := S_4/(240 m^2 lambda)` is `0.031088`
at `m = 30` and decreasing (exact Fractions, NC-W2(e)); `0.0330` is a safe
uniform bound for `m >= 30`.
(ii) Four-band refinement: with `n_1 = floor(m/4), n_2 = floor(m/2),
n_3 = floor(3m/4)` and `Q(n) = sum_{j<=n} j^4` (exact),

```
lambda - s2 <= lam^2 [ Q(n_1)/240 + (Q(n_2)-Q(n_1)) E(w/4)
                       + (Q(n_3)-Q(n_2)) E(w/2) + (Q(m)-Q(n_3)) E(3w/4) ] ,
```

using `E` decreasing and `lam j > w/4, w/2, 3w/4` on the respective bands.
NC-W2(e) evaluates this bound with exact `Q`-sums and 40-digit `E`-values on
the grid `m in {30, 40, 50, 60, 80, 100, 150, 200, 300, 500, 1000, 3000}` x
80-point `w`-grid on `(0, 4]`: **max over the grid = 0.3789, attained at
(m, w) = (30, 4.0)**, decreasing toward the continuum limit `0.367`; the true
deficit never exceeds the bound (max violation `0.00e+00`). Certified
`E`-decimals: `E(1) <= 0.00400694`, `E(2) <= 0.00358720`,
`E(3) <= 0.00304100`. **Status: (i) PROVED; (ii) grid-certified with exact
band sums (same status class as (T.7b-cert)/(T.7c-cert): Sturm-able on
demand). True floor measured: `min s2/lambda = 0.6629` at `K = 4` —
slack 0.06 over `c_4`.**

### Lemma W.2 (global per-factor derivative bounds — new; these extend the
dictionary from |w| <= pi to |w| <= 4).
With `v_n := 2 pi n` and the cotangent partial fractions
`g(u) = 1/2 - sum_{n>=1} [ (u - i v_n)^{-1} + (u + i v_n)^{-1} ]`
(the mechanism of T.9'' Step 1):

(a) `|g''(u)| <= |u|/120` for all `|u| <= 2 pi sqrt(3) = 10.88...`

(b) `|g'''(u) - 1/120| <= u^2/273` for `|u| <= 4`.

*Proof.* (a) `g''(u) = -2 sum_n [ (u-iv_n)^{-3} + (u+iv_n)^{-3} ]
= 4u sum_n (3v_n^2 - u^2)/(u^2+v_n^2)^3`. For `u^2 <= 3 v_1^2 = 12 pi^2`
every summand is nonnegative, and `(3v_n^2 - u^2)/(u^2+v_n^2)^3 <= 3v_n^2/v_n^6
= 3/v_n^4`; summing, `|g''(u)|/|u| <= 12 sum v_n^{-4} = 12 zeta(4)/(2pi)^4
= 12/1440 = 1/120` (exact: `zeta(4) = pi^4/90`).
(b) `g'''(u) = 12 sum_n phi_n(u)`, `phi_n(u) = (u^4 - 6u^2v_n^2 + v_n^4)/
(u^2+v_n^2)^4`, `g'''(0) = 12 zeta(4)/(2pi)^4 = 1/120`. In `s := u^2`,
`d phi/d s = (-2s^2 + 20 s v^2 - 10 v^4)/(s+v^2)^5`, so for `0 <= s <= 16`,
`v^2 >= 4pi^2 = 39.478`: `|d phi/d s| <= (2*16^2 + 20*16*v^2 + 10 v^4)/v^{10}
<= (10 + 320/39.478 + 512/39.478^2) v^4 / v^{10} <= 18.44/v^6`. Hence
`|g'''(u) - 1/120| <= 12 * 18.44 u^2 sum v_n^{-6} = 221.3 u^2 zeta(6)/(2pi)^6
= 221.3 u^2/60480 <= u^2/273` (`zeta(6)/(2pi)^6 = 1/60480` exact). QED

NC-W2(b,c): 400-point 40-digit grids on `(0, 4]`: max ratios `0.99999206`
(the `|u|/120` bound is asymptotically sharp as `u -> 0`) and `0.54166`.
**Status: PROVED.**

### Lemma W.3 (cumulant boxes, uniform in |w| <= 4, m >= 30).

```
|kappa_3(lam)|              <= lam (S_4+m)/120  <= |w| m^4/545
|kappa_4(lam)|              <= (S_4+m)/120                    [T.9''a, r=4: 2*3!*zeta(4)/(2pi)^4 = 1/120, sharp]
|kappa_4(lam)-kappa_4(0)|   <= lam^2 (S_6+m)/273 <= w^2 m^5/1500
|kappa_5(lam)|              <= C5 (S_5+m),   C5 = 48 zeta(5)/(2pi)^5  <= 5.08266e-3
|kappa_6(lam)|              <= C6 (S_6+m),   C6 = 240 zeta(6)/(2pi)^6 <= 3.96835e-3
```

*Proof.* First line: `kappa_3 = sum_j [ j^3 g''(lam j) - g''(lam) ]`, W.2(a)
termwise (`lam j <= w <= 4 < 2 pi sqrt 3`), then `(S_4+m)*545 <= 120 m^5` for
`m >= 30` (exact Fraction check, NC-W2(f); leading coefficient `6/30 = 1/5 <
120/545` makes it eventually true, roots below 30). Third line: W.2(b)
termwise plus `(S_6+m)*1500 <= 273 m^7` (same certificate). Lines 2, 4, 5 are
T.9''(a) instances (`|g^{(r)}(u)| <= 2 r! zeta(r+1)/(2pi)^{r+1}` for all real
`u`), with the zeta-constants certified as upper decimals (NC-W2). QED

NC-W2(d) ratios against the closed-form cumulants on `m in {30, 60, 120,
300}` x 40-point `w`-grid to 4: `0.9994 / 0.9851 / 0.9983 / 0.5413 / 0.4761 /
0.7861 / 0.9959` — all `<= 1`; the `kappa_3` and `kappa_4` bounds are
essentially sharp. **Status: PROVED.** *(Note: `|kappa_3| <= |w| m^4/545`
supersedes T.4's `/284` — sharper constant AND wider scope; and T.9''a's
`|kappa_4| <= (S_4+m)/120 ~ m^5/545` supersedes the `m^5/155` clause of
(T.4') — both usable wherever T.4' was.)*

**Scaled boxes.** With `s2 >= s2min := c_K lambda(m)` (W.1) and exact `S_r(m)`:

```
|a| <= amax(K, m) := (K/m)(S_4+m) / (720 s2min^{3/2}) ,   per-w: |a| <= w * amax/K ,
|b| <= bmax(m)    := (S_4+m) / (2880 s2min^2) ,
|d| <= dmax(m)    := C5 (S_5+m) / (120 s2min^{5/2}) ,
|g| <= gmax(m)    := C6 (S_6+m) / (720 s2min^3) ,
h   <= hmax(m)    := s2min^{-1/2}   ( <= 0.0461 for m >= 30, all K ) .
```

---

## 3. Lemma W.4: the Taylor-remainder bucket (the wp2-b deliverable)

### Statement.
Let `m >= 30`, `0 <= w <= K`, `L := log P` with `P` from Lemma W.0 at the true
scaled coefficients, and `F(0) := e^{1/s2} P(0)^2/(P(-h)P(h))`. Then `P > 0`
on `J` and

```
s2 log F(0) = 1 - B_lam + N(0)/P(0)^2 + theta_T * T(K, m) ,   |theta_T| <= 1 ,
T(K, m) := m^{-2} * [ m^2 sup_J |L''''| / (12 s2min) ]   (the bracket is the C_R entry),
```

with the explicit, decreasing-in-`m` values (NC-W3; full table §7):

| `m >=` | `K=1` | `K=2` | `K=4` |
|---|---|---|---|
| 30  | 0.02034 | 0.06117 | 1.65299 |
| 60  | 0.00388 | 0.01118 | 0.19700 |
| 180 | 0.00035 | 0.00100 | 0.01402 |
| 500 | 0.00004 | 0.00012 | 0.00158 |

*(entries are `m^2 T`, i.e. the contribution to `C_R(K)`; `P_min` at the
worst case `(K, m) = (4, 30)` is `0.8710 > 0`.)*

### Proof.
**Step 1 (exact ratio).** `phat(x) = Z(y) P(y)` (W.0) gives
`phat(0)^2/(phat(1) phat(-1)) = [Z(0)^2/(Z(h)Z(-h))] * P(0)^2/(P(h)P(-h))
= e^{h^2} P(0)^2/(P(h)P(-h)) = F(0)` exactly (`Z(h)Z(-h) = (2 pi s2)^{-1}
e^{-h^2}`). NC-W3(4) confirms the whole model pipeline by independent
`mpmath` quadrature at `(m, w) = (30, 1)`: `phat` vs `Z P` and the ratio
identity agree to `1.2e-16` / `3.1e-17` (float precision).

**Step 2 (fourth-order symmetric Taylor).** `log F(0) = h^2 + 2L(0) - L(h)
- L(-h)`, and with the integral remainder
`L(h) + L(-h) - 2L(0) = h^2 L''(0) + (h^4/6) int_0^1 (1-tau)^3 [L''''(tau h)
+ L''''(-tau h)] d tau`, whose modulus is `<= (h^4/12) sup_J |L''''|`
(`int_0^1 (1-tau)^3 = 1/4`; odd orders cancel in the symmetric difference —
this is where the tilted frame's `kappa_3, kappa_5` model terms drop out of
the Taylor step entirely, entering only through `sup|L''''|`). Multiply by
`s2` and use `s2 h^2 = 1` and `-L''(0) = -B_lam + N(0)/P(0)^2` (W.0, `He_2(0)
= -1`): the displayed identity, with `|s2 * remainder| <= sup_J |L''''|/(12
s2) <= sup_J |L''''|/(12 s2min)`.

**Step 3 (Hermite sups).** For `|y| <= 1/2` (our `h <= 0.0461`):
`|He_1| <= |y|`, `|He_2| = |y^2-1| <= 1`, `|He_3| = |y||y^2-3| <= 3|y|`,
`|He_4| = |3-6y^2+y^4| <= 3`, `|He_5| = |y||15-10y^2+y^4| <= 15|y|`,
`|He_6| = |{-15}+45y^2-15y^4+y^6| <= 15`, `|He_7| <= 105|y|`, `|He_8| <= 105`
— each a one-line polynomial inequality on `y^2 <= 1/4` (e.g. He_6: `45y^2 -
15y^4 + y^6 <= 30` there); grid-certified in NC-W3(1), max ratio `1.0000`
(attained, at `He_1`).

**Step 4 (derivative sups and the quotient rule).** With `P = sum c_n He_n`
(`c_3 = a, c_4 = -b, c_5 = d, c_6 = g + a^2/2, c_7 = -ab, c_8 = b^2/2 + ad`)
and `P^{(r)} = sum c_n (n)_r He_{n-r}` (NC-W1(5), sympy-verified), Step 3 and
the W.3 boxes give, on `J` (writing `a, b, d, g, h` for the box values,
`ga := g + a^2/2`, `e8 := b^2/2 + ad`):

```
p_1 <= 3a + 12bh + 15d + 90 ga h + 105 ab + 840 e8 h
p_2 <= 6ah + 12b + 60dh + 90 ga + 630 ab h + 840 e8
p_3 <= 6a + 24bh + 60d + 360 ga h + 630 ab + 5040 e8 h
p_4 <= 24b + 120dh + 360 ga + 2520 ab h + 5040 e8
P_min >= 1 - [ 3ah + 3b + 15dh + 15 ga + 105 ab h + 105 e8 ]
```

and the quotient-rule identity (NC-W1(6), sympy-verified)
`L'''' = P''''/P - (4P'''P' + 3P''^2)/P^2 + 12 P''P'^2/P^3 - 6P'^4/P^4`
yields `sup_J |L''''| <= p_4/P_min + 4p_3p_1/P_min^2 + 3p_2^2/P_min^2
+ 12 p_2 p_1^2/P_min^3 + 6 p_1^4/P_min^4` (numerically re-checked at 300
random points, max ratio `0.810`). Evaluating at `s2min = c_K lambda(m)`
(every factor decreasing in `m`; monotonicity re-verified on `m = 30..3000`
step 10, NC-W3(2)) gives the table. QED

**Truth check (NC-W3(3)).** At `(m, w)` samples the measured
`s2 |log F(0) - (1 - B_lam + N(0)/P(0)^2)| m^2` is below the bucket bound with
ratio `0.008 – 0.60` (worst `0.60` at `m = 120, K = 1, w = 1` — the bound is
within a factor 1.7 of truth where it matters most, and within ~100x at
`K = 4` where the crude boxes pay for the sign-flip regime, §5), and the
remainder always obeys the direct `(h^4/12) sup_J |L''''|` form. **Status:
PROVED (modulo W.1(ii)'s grid-certificate status for `c_4`; for `K <= 2` the
only inputs are the fully proved W.1(i), W.2, W.3).**

---

## 4. Lemma W.5: the linearization bucket

### Statement.
If `|s2 log r(k) - 1| <= 1/2` (which the assembled theorem provides at its
own thresholds once the wp2-a bucket lands; see §6), then

```
s2 (r(k) - 1) = s2 log r(k) + theta_L * Lin(K, m) ,  |theta_L| <= 1 ,
Lin(K, m) := (9/8) e^{1.5/s2min} / s2min ,      s2min := c_K lambda(m) ,
```

with the `C_R` entries `m^2 Lin = 0.2308 / 0.2571 / 0.3719` (`K = 1/2/4`) at
`m = 180`, decreasing in `m`.

*Proof.* `rho := log r(k) >= 0` (log-concavity, Bona — the ambient fact of the
ledger); the hypothesis gives `rho <= 1.5/s2 <= 1.5/s2min`. Then
`s2 (e^rho - 1 - rho) <= s2 rho^2 e^rho / 2 <= (1.5^2/2) e^{1.5/s2min}/s2min`.
QED  *(`e^{1.5/s2min} <= 1.00001` at `m >= 180`; the bucket is really
`9/(8 s2min) ~ 40.5/(c_K m^3)`, an `O(1/m^3)` object — its `C_R` entry decays
like `1/m`.)*

---

## 5. Proposition W.6: the proved w^2-envelope — audit of T.9's `c_w = 1/2`

The main chain (W.4) produces `1 - B_lam + N(0)/P(0)^2`; T.9's statement wants
`1 - B_m (1 + theta_1 c_w w^2)` plus an `O(m^{-2})` bucket. The `w^2`-envelope
must therefore absorb (I) `B_m - B_lam` and (II) the bare `-36 a^2/P(0)^2`
(Lemma W.0). Both are genuinely `O(w^2/m)`.

### Statement.
For `m >= 180` and `0 <= w <= K`:

```
| (B_lam - B_m) + 36 a^2/P(0)^2 |  <=  B_m * c_w(K) * w^2 ,
c_w(1) = 0.407 ,   c_w(2) = 0.466 ,   c_w(4) = 0.951
```

(NC-W4(3); worst `m` among `{180, 500, 2000, 10^4}` is 180; the `B`-part /
bare-part splits are `0.273 + 0.134`, `0.280 + 0.186`, `0.373 + 0.577`).
**Hence T.9's `c_w = 1/2` is PROVED for `K = 1` and `K = 2`, and must be
weakened to `c_w(4) = 1` (or 0.96) at `K = 4`.**

### Proof sketch (all pieces displayed; the max is a 400-point `w`-grid of
explicit monotone formulas, NC-W4).
`B_lam/B_m = [kappa_4(lam)/kappa_4(0)] * (lambda/s2)^2 =: ratio * R`, with:
`|ratio - 1| <= q(w) := (600/2200) w^2` for `w <= pi` (T.4', scope-valid) and
`(600/1500) w^2` for `pi < w <= 4` (W.3 recentred; both use `S_4 - m >= m^5/5`,
exact); `ratio` also obeys the DIRECT two-sided `|ratio| <= (S_4+m)/(S_4-m)`
(W.3 line 2); `1 <= R <= 1 + devB(w)`, `devB = def(2-def)/(1-def)^2`,
`def(w) = min(0.0330 w^2, 0.40)` (W.1). Upper side:
`B_lam/B_m - 1 <= min( q(1+devB) + devB, (S_4+m)/(S_4-m) (1+devB) - 1 )` — the
direct clause is what keeps `c_w(1), c_w(2)` under `1/2` (the `kappa_4`-shrink
can only push `B_lam` DOWN, so the upper side is essentially `devB` alone).
Lower side: `1 - B_lam/B_m <= min( lower_q, 1 + (S_4+m)/(S_4-m)(1+devB) )`
where `lower_q = q` if `q <= 1` and `1 + (q-1)(1+devB)` if `q > 1` (the
`q > 1` case is where `kappa_4(lam)` may cross zero — see the finding below).
Part (II): `|a| <= w * amax/K` (W.3), so `36 a^2/P(0)^2 <= [36 (amax/K)^2 /
(B_m P0_min^2)] * B_m w^2` with exact `B_m(m)` and
`P0_min = 1 - 3b - 15(g + a^2/2) - 105(b^2/2 + ad) - (odd, O(h))` terms.
Sum the two coefficients, maximize over the `w`-grid and over
`m in {180, 500, 2000, 10^4}`. QED

### Finding (true mechanism, not bound slack): `kappa_4(lam)` changes sign.
NC-W2(d) measures `kappa_4(lam)/kappa_4(0) = 0.4670 / 0.0982 / -0.1417` at
`m = 60`, `w = 2 / 3 / 4`. So at `K = 4` the model's `B_lam` genuinely crosses
zero and turns negative (`B_lam/B_m ~ -0.32` at `w = 4`), i.e.
`|B_lam - B_m| ~ 1.3 B_m` — an honest `c_w`-floor of `~0.083` from part (I)
alone at `w = 4`, and no chase through `B_lam` separately can reach the TRUE
total envelope (`~0.01 B_m w^2`, NC-T8): the truth is a cancellation between
(I) and (II) and the kernel bucket (the flatness NC-9/NC-T7 survives at
`w = 4` even though `kappa_4` has flipped). Proving `c_w(4) = 1/2` would need
a cancellation lemma coupling the buckets — noted in §9; NOT attempted here.

---

## 6. Theorem W.7: the assembled table

### Statement (assembly; kernel bucket pending).
Fix `K in {1, 2, 4}`. For `m >= 180` and interior `k` with
`0 < lam(k) <= K/m` (and symmetrically), with `u := r(k) - 1`,
`v := F(0) - 1 > 0`, define the EXACT leftover

```
Delta_ker(k) := s2 [ log(1+u) - log(1+v) ]
```

(the kernel-transfer + denominator defect: everything that changes when the
true tilted pmf values `P_0, P_{+-1}` are replaced by the 6-term-model values
`phat(0), phat(+-1)` — the object wp2-a is bounding). Then, exactly,

```
s2 log r(k) = 1 - B_m (1 + theta_1 c_w(K) w^2) + theta_2 * [PW + T] / m^2 + Delta_ker(k) ,
s2 (r(k)-1) = the same + theta_3 * Lin(K, m)   [conditional, Lemma W.5] ,
```

`|theta_i| <= 1`, with the buckets (each certified decreasing in `m`;
`m >= 180` column; kernel column = the pending wp2-a deliverable, its TRUE
size measured in NC-W4(6)):

| K | PW (grid cert., m<=2000) | PW (closed form, all m) | Taylor `T` | Lin | **C_R^PT = PW+T+Lin (grid)** | **C_R^PT (closed)** | kernel (pending; truth) |
|---|---|---|---|---|---|---|---|
| 1 | 1.5491 | 10.278 | 0.00035 | 0.2308 | **1.7803** | **10.509** | pending (~1.39) |
| 2 | 4.0889 | 21.063 | 0.00100 | 0.2571 | **4.3470** | **21.321** | pending (~4.07) |
| 4 | 4.9126 | 187.41 | 0.01402 | 0.3719 | **5.2985** | **187.80** | pending (~5.04) |

*Proof.* Chain W.4 (Taylor) + W.0 (`N(0)` split) + W.6 (envelope) + the
`N0_resid/P(0)^2` bucket + the identity `s2 log(1+u) = s2 log(1+v) +
Delta_ker`. The pointwise bucket in the grid flavor is the item-4 notes'
certificate, independently re-run here (NC-W4(1), reproduced to 4 digits:
`1.5491 (m=30, w=1.0) / 4.0889 (30, 2.0) / 4.9126 (2000, 2.8)`); in the
closed-form flavor it is `sum |coeff| * amax^i bmax^j dmax^k gmax^l * m^2 /
P0_min^2` over the NC-W1 monomial table with the W.3 boxes — valid for ALL
`m >= 180` (decrease in `m` verified 180..2000 step 60, and the `m = 10^4`
values continue down: `10.268 / 20.942 / 178.69`). QED

**Remarks.**
1. *Two flavors, honestly labeled.* The grid flavor is sharp but certified
   only on the sampled `m <= 2000` (same status class as (T.7b-cert)); the
   closed-form flavor is a theorem for all `m >= 180` given W.1–W.3 but pays
   the triangle inequality on the `N0_resid` monomials — the `-90g + 384b^2`
   and `750ad - 585a^2b` cancellations are discarded, hence `10.3` vs `1.55`
   at `K = 1` and `187` vs `4.9` at `K = 4` (the `a`-heavy monomials dominate
   there). A corner-rectangle refinement in the style of Cor B.9 (two-sided
   boxes for `a, b, d, g`) would recover most of the gap; not done here (§9).
2. *Thresholds.* `m >= 180` matches the G1 campaign target; `m <= 150` is
   covered by the exact harness (NC-1/NC-T8); the band `150 < m < 180` needs
   the planned harness extension (same note as g1_draft_b §8 item 2).
   The Lin bucket's hypothesis `|s2 log r - 1| <= 1/2` is discharged once the
   merged bound (with wp2-a's kernel constant `C_ker`) satisfies
   `B_m(1 + c_w K^2) + (C_R^PT + C_ker)/m^2 <= 1/2` — at `m >= 180` this
   holds for any `C_ker <= 10^4`-scale, so the conditionality is cosmetic.
3. *What the far region still costs.* Nothing here changes T.9's `m_2(K)`
   thresholds: the far bucket (inside wp2-a's `Delta_ker` chase) is still
   governed by (T.7c)'s `exp(-0.06 e^{-2K} m)`, the single binding exponent
   (T2 §8 item 5). My table is the `O(m^{-2})`-bucket half of item 4 only.

---

## 7. Numeric checks (all run 2026-08-11; scripts in
`g2_scripts/campaign_undefined/wp2_b/`)

| # | script | validates | verdict |
|---|---|---|---|
| NC-W1 | `wp2b_nc1_model_poly.py` | Lemma W.0: model polynomial, `-36a^2` split, monomial weights, derivative + quotient-rule formulas | **PASS** |
| NC-W2 | `wp2b_nc2_dictionary.py` | W.1 (floor, bands, `E`-decimals), W.2 (global `g''`, `g'''`), W.3 (boxes vs closed forms), zeta-constants, exact polynomial certificates | **PASS** |
| NC-W3 | `wp2b_nc3_taylor.py` | Lemma W.4: Hermite sups, bucket table, monotonicity, truth ratios, quadrature check of the Fourier rule | **PASS** |
| NC-W4 | `wp2b_nc4_assembly.py` | PW grid re-run, PW closed form, Prop W.6 `c_w`, Lemma W.5 values, Theorem W.7 table, harness truth (`needed`, `Delta_ker`) | **PASS** |

Key verbatim output (NC-W1):

```
(1) Im P == 0 : True
(2) P free of s2 : True
(2) P == 1 + a He3 - b He4 + d He5 + (g+a^2/2) He6 - ab He7 + (b^2/2+ad) He8 : True
(3) untilted limit == g1_draft_b P : True
(4) coefficient of bare a^2 in N(0): -36  (must be -36)
    min weight = 4 (need >= 4, i.e. O(1/m^2)) : True
    untilted residual = -90 g + 384 b^2 + (weight>=6 terms) : True
(5) He-shift derivative formulas r=1..4 : True
    lib.P_eval vs sympy, r=0..4, 200 random pts: max rel dev = 1.07e-14
(6) L'''' quotient identity : True
    |L''''| vs quotient-rule bound, 300 random pts: max ratio = 0.810
NC-W1 VERDICT: PASS
```

NC-W2 (trimmed):

```
(a) E decreasing on (0,4] (400-pt grid): True
    E(1) = 0.004006927541  (<= 0.00400694: True)
    E(2) = 0.003587187144  (<= 0.00358720: True)
    E(3) = 0.003040358636  (<= 0.00304100: True)
(b) max |g''(u)|/(|u|/120) on (0,4]: 0.99999206  (<= 1: True)
(c) max |g'''(u)-1/120|/(u^2/273) on (0,4]: 0.54166193  (<= 1: True)
    C5 = 48 zeta(5)/(2pi)^5 = 0.005082652228 (<= 0.00508266: True)
    C6 = 240 zeta(6)/(2pi)^6 = 0.003968253968 (<= 0.00396835: True)
(d) |kappa_3| / [lam(S_4+m)/120]      max ratio = 0.9994
    |kappa_3| / [w m^4/545]           max ratio = 0.9851
    |kappa_4| / [(S_4+m)/120]         max ratio = 0.9983
    |kappa_4-kappa_4(0)| / [lam^2(S_6+m)/273] max ratio = 0.5413
    |kappa_4-kappa_4(0)| / [w^2 m^5/1500]     max ratio = 0.4761
    |kappa_5| / [C5 (S_5+m)]          max ratio = 0.7861
    |kappa_6| / [C6 (S_6+m)]          max ratio = 0.9959
    [info] m=60 w=2.0: kappa_4(lam)/kappa_4(0) = 0.4670
    [info] m=60 w=3.0: kappa_4(lam)/kappa_4(0) = 0.0982
    [info] m=60 w=4.0: kappa_4(lam)/kappa_4(0) = -0.1417
(e) max PROVED deficit bound over grid = 0.3789 at (m,w)=(30, 4.0)  (<= 0.40, giving c_4 = 0.60: True)
    max (true deficit - bound) = 0.00e+00  (must be <= 0)
    coef(30) = S_4/(240 m^2 lambda) = 0.031088 (<= 0.0330: True), decreasing on 30..300 step 10: True
    floors: K=1: true min s2/lambda = 0.9698 (>= 0.967: True)
            K=2: 0.8887 (>= 0.868: True)   K=4: 0.6629 (>= 0.6: True)
(f) (S_4+m)*545 <= 120 m^5 (m=30..2000 sample): True;  (S_6+m)*1500 <= 273 m^7: True
NC-W2 VERDICT: PASS
```

NC-W3 (trimmed):

```
(1) Hermite sup certificates on |y|<=0.05: max ratio = 1.0000 (<= 1: True)
(2) Taylor bucket T(K, m) = m^2 sup|L''''|/(12 s2min)  [C_R contribution]:
        m         K=1        K=2        K=4   (Pmin at K=4)
       30     0.02034    0.06117    1.65299   (0.8710)
       60     0.00388    0.01118    0.19700   (0.9455)
      120     0.00084    0.00238    0.03517   (0.9750)
      180     0.00035    0.00100    0.01402   (0.9838)
      500     0.00004    0.00012    0.00158   (0.9944)
     2000     0.00000    0.00001    0.00009   (0.9986)
    decreasing in m on 30..3000 (step 10), all K: True
(3) truth ratios (s2*R_T*m^2)/(bucket): 0.008 .. 0.60, all True on RT<=h4/12*supL4
(4) quadrature check (m=30, w=1): max rel dev phat vs Z*P = 1.19e-16; ratio identity rel dev = 3.08e-17
NC-W3 VERDICT: PASS
```

NC-W4 (trimmed; the full assembly and truth tables):

```
(1) K=1: max |N0_resid/P0^2 m^2| = 1.5491 at (m,w)=(30, 1.0)
    K=2: 4.0889 at (30, 2.0)   K=4: 4.9126 at (2000, 2.8)
    reproduces item-4 notes (1.5491/4.0889/4.9126 within 0.02): True
(2) PW_closed:  m=180: 10.278 / 21.063 / 187.414   (m=10^4: 10.268 / 20.942 / 178.694)
    decreasing in m (180..2000 step 60): True
(3) c_w(K), max over m in {180, 500, 2000, 10000}:
    K=1: c_w = 0.4067 (B-part 0.2727 + bare-alpha^2 0.1340) -> c_w <= 1/2: True
    K=2: c_w = 0.4658 (B-part 0.2802 + bare-alpha^2 0.1857) -> c_w <= 1/2: True
    K=4: c_w = 0.9506 (B-part 0.3734 + bare-alpha^2 0.5772) -> c_w <= 1/2: False
(4) Lin(K, 180): 0.2308 / 0.2571 / 0.3719
(5)  K   PW_grid  PW_closed    Taylor     Lin  C_R^PT grid  C_R^PT closed
     1    1.5491     10.278   0.00035  0.2308       1.7803         10.509
     2    4.0889     21.063   0.00100  0.2571       4.3470         21.321
     4    4.9126    187.414   0.01402  0.3719       5.2985        187.800
(6)    m  K   needed0 needed_env  ker_truth
      30  1     0.349      0.344      1.374
      30  2     0.783      0.343      4.031
      30  4     2.410      0.338      5.031
      60  1     0.543      0.089      1.386
      60  2     2.146      0.089      4.070
      60  4     5.233      0.089      5.022
     100  1     1.068      0.022      1.391
     100  2     3.689      0.022      4.061
     100  4     8.781      0.022      5.031
     140  1     1.523      0.070      1.386
     140  2     5.175      0.070      4.059
     140  4    12.280      0.070      5.038
NC-W4 VERDICT: PASS
```

(`needed0 := max |s2(r-1) - (1-B_m)| m^2` over `|w| <= K` — grows with `m`
because it contains the TRUE `w^2`-envelope, measured at `~0.01 B_m w^2`;
`needed_env` subtracts `B_m c_w(K) w^2` with MY proved `c_w` and reproduces
NC-T8's `0.343 / 0.089 / 0.022 / 0.070` — near-identical across `K`, i.e. the
envelope soaks up all `w`-dependence; `ker_truth := max |Delta_ker| m^2`.)

---

## 8. Comparison with NC-T8's headroom — how much slack remains, honestly

NC-T8's calibration: the constant the refined law actually NEEDS is
`<= 0.35` for `m <= 140` (and falling: `0.070` at `m = 140`). Against that:

1. **My assembled `C_R^PT(K)` (pointwise + Taylor + Lin, kernel excluded):**
   grid flavor `1.78 / 4.35 / 5.30`, closed flavor `10.5 / 21.3 / 187.8`.
   The grid flavor is `5.1x` (K=1) above the worst measured need `0.35`, and
   `25x` above the `m = 140` need `0.070`. The closed flavor is `30x` /
   `150x` at `K = 1`.
2. **The pending kernel bucket cannot be small:** its TRUE size is
   `1.39 / 4.07 / 5.04` (NC-W4(6), stable in `m`) — comparable to the whole
   pointwise bucket. So the final merged `C_R(K)` is at best
   `~3.2 / ~8.4 / ~10.3` (grid flavor + kernel truth), i.e. **>= 9x the
   measured need at `K = 1`** even if wp2-a's bound were exactly tight.
3. **Where the 9x lives — a cancellation the bucket route discards:** the
   individual buckets are large (`PW ~ 1.55`, `ker ~ 1.39` at `K = 1`) while
   their SIGNED SUM is the total residual (`needed_env ~ 0.07-0.34`): the
   pointwise model error and the kernel-transfer error cancel against each
   other in truth. The same phenomenon in the `w^2` envelope: `kappa_4`'s
   sign-flip (§5) is compensated by the bare `alpha^2` and kernel terms, so
   the true envelope is `~0.01 B_m w^2` while the proved one is
   `0.41–0.95 B_m w^2`. Triangle-inequality assembly can never see this; a
   sharper result would need the buckets bounded jointly, not separately.
4. **Does the slack endanger anything downstream?** No, at the current
   targets: Theorem A's region-3 handoff and G4's center-margin chase use
   small `K` (`w <= w_0 ~ 1`), where even the all-`m` closed flavor
   (`10.5 + kernel`) sits inside G4's tested tolerance `C' <= 20` (NC-13,
   center margin holds for `m >= 17` at `C' = 20`). The binding constraint of
   T.9 remains the far-region exponent (thresholds `m_2(K)`, T2 §8 item 5),
   NOT these constants — exactly as the T2 draft predicted ("the constant
   chase is not the risk; the far exponent is").

---

## 9. What remains

1. **The kernel-transfer + denominator bucket (`Delta_ker`)** — wp2-a's
   package, the one remaining piece of T2 §8 item 4. Exactly defined here
   (Theorem W.7); its true size is measured (`~1.4 / 4.1 / 5.0` in `C_R`
   units); once an explicit bound lands, item 4's row flips to closed
   (modulo referee) by adding one column to the W.7 table. Until then
   Theorem W.7 is an exact decomposition, not a closed bound: **T.9 remains
   PARTIAL.**
2. **`c_w(4)`: statement-level correction to T.9.** With the proved
   constants, `c_w = 1/2` holds for `K = 1, 2` but not `K = 4`
   (`c_w(4) = 0.951`; use 1). The obstruction is true, not slack:
   `kappa_4(lam)` crosses zero near `w ~ 3.3` (§5). Either T.9's statement
   carries `c_w(K) = max(1/2, ...)` per K, or a bucket-coupling cancellation
   lemma is proved — the latter is genuinely new work, and the NC-T7/NC-9
   flatness (band `~3/m^2` out to `|w| = 4`) says the cancellation is real
   and strong. My envelope is also only stated for `m >= 180` (evaluated on
   `{180, 500, 2000, 10^4}`, worst at 180, all pieces monotone or constant
   in `m`); `30 <= m < 180` values would be larger and were not chased.
3. **Grid-certificate statuses** (Sturm-able, same class as
   (T.7b-cert)/(T.7c-cert), g1_draft_b §8 item 1): W.1(ii)'s band bound
   (exact band sums, certified `E`-decimals, 12x80 grid + continuum limit);
   the PW grid flavor (`m <= 2000` sample grid); the Hermite sup certificates
   (also proved by displayed one-line inequalities). Everything else in
   W.0–W.5 is closed-form given those.
4. **The closed-form PW flavor is crude at `K = 4`** (`187` vs truth `4.9`):
   the triangle inequality discards the `-90g + 384b^2` and `750ad - 585a^2b`
   cancellations. A Cor-B.9-style corner-rectangle version (needs TWO-SIDED
   boxes for `a, d`, i.e. signed lower bounds on `kappa_3, kappa_5` along the
   tilt — not currently in any draft) would recover most of it. Not needed
   at the current targets (§8 item 4 note).
5. **Conditionality of Lin** (Lemma W.5): discharged only jointly with
   wp2-a's constant; cosmetic at `m >= 180` (§6 remark 2).
6. **The band `150 < m < 180`** between the harness range and my thresholds:
   inherited from g1_draft_b §8 item 2; the planned harness extension
   (minutes of compute, per G4) covers it.
7. **Untouched: T2 §8 items 1, 5** (deep tilt; the far exponent and the
   `m_2(K)` thresholds). My buckets feed the `O(m^{-2})` side of item 4 only;
   the far-region viability condition inside wp2-a's bucket will still be
   governed by (T.7c) and will still set `m_2(K)`.

*End of wp2_draft_b. Blind protocol maintained throughout.*
