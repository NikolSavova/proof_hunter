# wp3-a2 — Region-2 handoff: pentagonal region extended to k = Theta(m), the deficit floor, the tilt cap, and a gap-free stitching table (T2 §8 item 2)

*Work package wp3-a2 (wave 2, campaign 2026-08-11), T2 §8 item 2 — the
region-2 handoff, UNTOUCHED in wave 1 (STATUS §2 item 2). Written from:
`STATUS.md`, `F2_PROOF_DRAFT.md` (merged draft; "Lemma 1.x/3.x" cite it),
`g1_draft_b.md` (refereed; B.0–B.9 citable), `g2_draft_t2_20260803.md` ("T.x";
single-referee status at STATUS time — its MATHS referee pass
`referee_t2_maths.md` has since landed, MINOR_REPAIRS; every T.x used here is
flagged with its per-item status from that report), `wp1_draft_c.md` ("W.x
far bounds"; both referees MINOR_REPAIRS, repairs discharged in
`repairs_20260811.md`), `wp2_draft_b.md` (both referees MINOR_REPAIRS; its
lemmas cited as "W2b-"), the referee reports for all of the above, and
`harness_m200_20260811.md` (exact harness now to m = 400). NOT read:
`g2_draft_t1_20260803.md` (kept blind), anything under
`g2_scripts/campaign_20260811/wp2_a2/` (parallel wave-2 package). No existing
file modified. Scripts:
`g2_scripts/campaign_20260811/wp3_a2/wp3a2_nc1_pentagon.py`,
`wp3a2_nc2_constants.py`, `wp3a2_nc3_handoff.py`, `wp3a2_nc4_stitch.py` —
each SAVED and RUN 2026-08-11; every number quoted below is from a real
run; verbatim excerpts in §7.*

## Contents

- §0 The problem, the route taken, and the results with status markers.
- §1 The extended pentagonal toolkit (Lemmas P.1–P.3).
- §2 First/second-difference bounds on the pentagonal correction (Lemma P.4).
- §3 Theorem P.5: region 1 extended to k <= c·m, with the (c, m_p(c)) table.
- §4 Handoff lemmas: variance floor on the residual band (P.6), the
  all-w deficit floor (P.7), the tilt cap (P.8).
- §5 Theorem S: the stitching table (T.10-style), gap-free coverage, and
  exactly what is conditional on what.
- §6 The wp4 / wp2-a requirement specs (quantified).
- §7 Numeric checks NC-P1..NC-P4 (scripts, real quoted output).
- §8 What remains / honest markers.

## 0. The problem, the route, the results

**The gap (T2 §8 item 2, STATUS §2 item 2).** Theorem A's region 2 needs the
crude law (Prop 3.5(i)) at every interior `k >= sqrt(m)/4` with
`sigma_lam^2 <= rho lambda`; the crude law's hypothesis is
`s2 := sigma_{lam(k)}^2 >= C_0 = 2000`. T.5-final (PROVED; confirmed fully
correct by the T2 maths referee §2.6) gives only `s2 >= (k/6)(1+k/m)`, which
at the region-1 edge `k ~ sqrt(m)/4` is `sqrt(m)/24`: the hypothesis is
reachable only for `m >= (24 C_0)^2 = 2.3e9`. Wave 1 left this untouched.

**Route taken (route 3 of the assignment: a provable combination).** Three
observations, each delivered below:

1. *Region 1 does not stop at `sqrt(m)/4`.* The pentagonal mechanism behind
   Lemma 3.6 — exact alternating expansion of `I_m(k)` in negative-binomial
   blocks `T(k - g_n)` — is valid on ALL of `0 <= k <= m`, and the reason
   Lemma 3.6's chain died at `sqrt(m)/4` is only that it bounded the
   correction factor to zeroth order (`T(k)(1-2k/m) <= I(k) <= T(k)`). Taking
   the correction's SECOND DIFFERENCE instead (the same move Lemma 1.5 makes
   for the Fourier main term) costs `O(1/m^2)`, while the pentagonal signal
   `r_T(k) - 1 = (m-1)/(k(m+k))` is still `Theta(1/m)` at `k = Theta(m)`.
   Result (Theorem P.5): `r(k) - 1 >= (m-1)/(2k(m+k))` out to `k = c m`,
   `c` up to 1, with explicit thresholds — region 1 now ends at `k = Theta(m)`,
   where T.5-final gives `s2 >= c(1+c) m/6 = Theta(m)`, not `Theta(sqrt m)`.
2. *The `C_0`-arithmetic then closes linearly instead of quadratically*:
   `s2 >= C_0` on all of the residual band as soon as `m >= 6 C_0/(c(1+c))`.
   With `C_0 = 2000` intact: `m >= 6000` (was `2.3e9`, a `3.8e5`x reduction).
   With the exact harness now at `m <= 400` (`harness_m200_20260811.md`), a
   gap-free stitch for ALL m needs only `C_0* <= 79` — and the measured truth
   is that NO variance threshold is needed at all (`|s2(r-1) - 1| <= 0.0385`
   over every interior `k` at `m = 30`, falling like `~1.2/m`; NC-P3d).
3. *What genuinely cannot be closed here* is the deep-tilt crude law itself
   (the core model, wp4's job — STATUS §2 item 1): on the residual band the
   tilt is a CONSTANT (`lam(k) <= log(1+1/c) <= 1.1`, Lemma P.8 — a new
   one-line cap that pins wp4's needed scope, all of it inside wp1-c's
   far-bound coverage `|lam| <= 1.7627`). The stitching theorem (§5) is
   therefore stated with the future crude law as a PARAMETER, and §6 turns
   the stitch into a quantified requirement spec: `(C_0*, C*, Lambda*) =
   (79, 20, 0.89)` suffices for every `m >= 401`.

**Results, with status:**

> **Theorem P.5 (region-1 extension) — PROVED.** For `2 <= k <= min(c m, m-1)`
> and `m >= m_p(c)`: `r(k) - 1 >= (m-1)/(2k(m+k))`, with
> `(c, m_p(c)) = (1/4, 30), (1/2, 83), (7/10, 300), (1, 1581)`
> (Lemmas P.1–P.4; certified constant chain, NC-P2; exact-harness truth check:
> zero violations over all `2 <= k <= m-1`, `8 <= m <= 200`, global min slack
> factor 2.0002, NC-P1).

> **Lemma P.6 (variance handoff) — PROVED** (corollary of T.5-final + P.5):
> on the residual band `k >= c m`, `s2 >= c(1+c)m/6`; hence `s2 >= C_0` for
> all `m >= 6C_0/(c(1+c))` — the item-2 mismatch reduced from quadratic to
> linear in `C_0`.

> **Lemma P.7 (all-`w` deficit floor) — PROVED.** For `m >= 30` and every real
> `w`: `1 - s2/lambda >= 6.85 w^2 E(w)` with `E` the (T.4a'')-kernel and
> certified decimals `E(4) >= 0.00248992` etc. (NC-P3b). This replaces the
> `(1 - w^2/19)`-degraded (T.4)-lower bound beyond `w ~ 3` and gives
> `s2 <= 0.7271 lambda` on `|w| >= 4` — the `rho`-side input the stitch needs
> at its `w_0 = 4` operating point (and it repairs the scope hole T2's (T.4)
> left at `|w| > pi` for this purpose).

> **Lemma P.8 (tilt cap) — PROVED.** For `k >= c m`:
> `lam(k) <= log(1 + 1/c)`. In particular wp4's deep-tilt core lemma is only
> ever needed for `|lam| <= 1.0987` (c = 1/2), `0.8874` (c = 7/10), `0.6932`
> (c = 1) — strictly inside wp1-c Corollary W.5's proved far-bound range
> `|lam| <= 1.7627`.

> **Theorem S (stitching; T.10-style table) — PROVED AS A REDUCTION.** For
> `m <= 400` Theorem A's parts (a-finite)/(b)/(c-finite) are exact (harness).
> For `m >= 401` the four regions R1a/R1b/R2/R3 of §5 PARTITION the interior
> `k`-range with every boundary explicit; R1a/R1b and the partition geometry
> are unconditional; R2 is conditional on exactly the wp4 core lemma at
> `(C_0*, C*, Lambda*) = (79, 20, 0.89)`; R3 is conditional on exactly
> wp2-a's `Delta_ker` (T2 §8 item 4's last bucket) at `K = 4`, whose
> far-region viability threshold `m_2(4) = 379 <= 400` is already inside the
> harness. **No band of `m` or `k` is uncovered, and no condition other than
> those two named open packages remains.**

Notation as in the merged draft and T2: `N = m(m-1)/2`,
`lambda = sigma^2 = m(m-1)(2m+5)/72`, `r(k) = a_k^2/(a_{k-1}a_{k+1})`,
`lam(k)` the tilted-mean parameter (`mu(lam(k)) = k`), `s2 = sigma_{lam(k)}^2`,
`w = lam m`, `B_m = (S_4 - m)/(240 lambda^2)`. WLOG `k <= N/2` (`a_k = a_{N-k}`).
Citation statuses used throughout: B.x = g1_draft_b (double-refereed,
citable); T.x = T2 draft (numerics referee MINOR_REPAIRS + maths referee
MINOR_REPAIRS `referee_t2_maths.md` — each T.x used here carries its per-item
verdict inline); W.x = wp1-c, W2b-x = wp2-b (each double-refereed
MINOR_REPAIRS, repair lists discharged in `repairs_20260811.md`).

## 1. The extended pentagonal toolkit

Throughout §1–§3: `T(j) := C(m-1+j, m-1)` for `j >= 0`, `T(j) := 0` for
`j < 0`; pentagonal numbers `g_n = n(3n-1)/2` for `n in Z` (`g_0 = 0`,
`g_1 = 1, g_{-1} = 2, g_2 = 5, g_{-2} = 7, g_3 = 12, g_{-3} = 15, ...`);
`G^+ := {g_n : n != 0} = {1, 2, 5, 7, 12, 15, 22, 26, ...}` (in each pair
`(g_n, g_{-n})` both members carry the sign `(-1)^n`).

### Lemma P.1 (pentagonal expansion, full range `k <= m`) — PROVED.
For every `m >= 1` and every `0 <= k <= m`:

```
I_m(k) = sum_{n in Z} (-1)^n T(k - g_n) .
```

*Proof.* `sum_k I_m(k) q^k = prod_{j=1}^m (1+q+...+q^{j-1})
= [prod_{j=1}^m (1 - q^j)] (1-q)^{-m}`. The first factor agrees with
`prod_{j=1}^infty (1 - q^j)` in every degree `<= m` (the quotient
`prod_{j>m}(1-q^j)` is `1 + O(q^{m+1})`), and Euler's pentagonal number
theorem gives `[q^g] prod_{j>=1}(1-q^j) = (-1)^n` if `g = g_n`, else 0.
The second factor contributes `[q^j](1-q)^{-m} = T(j)`. Convolve. ∎
(The merged draft's Lemma 3.6 used this identity only on `k <= sqrt(m)/4`;
its validity to `k = m` is the point here. NC-P1(a): exact-integer match with
the Mahonian rows for all `0 <= k <= m`, `m in {4, 8, 12, 20, 30, 40, 60}`,
zero mismatches.)

### Lemma P.2 (the correction factor and its building blocks) — PROVED.
For `1 <= k <= m` define

```
x_g(k) := T(k-g)/T(k) = prod_{i=0}^{g-1} (k-i)/(m+k-1-i)     (x_0 = 1; x_g(k) = 0 for g > k),
x(k)   := x_1(k) = k/(m+k-1),
Phi(k) := I_m(k)/T(k) = 1 + sum_{g in G^+, g <= k} eps(g) x_g(k) ,
```

`eps(g) = (-1)^n` for `g in {g_n, g_{-n}}`. Then:

(i) *(geometric envelope)* `0 <= x_g(k) <= x(k)^g`. Each factor
`(k-i)/(m+k-1-i) <= k/(m+k-1)`, since the difference of cross-products is
`i(m-1) >= 0`.

(ii) *(monotonicity in `k`)* Each `x_g` is nondecreasing in `k`:
`(d/dk)[(k-i)/(m+k-1-i)] = (m-1)/(m+k-1-i)^2 > 0` factorwise (and the
discrete statement follows from the exact ratio in (iii)).

(iii) *(exact shift ratios; the engine of §2)* For `1 <= g <= k`:

```
x_g(k+1)/x_g(k) = (k+1)(m+k-g) / [ (k+1-g)(m+k) ]         (k+1-g >= 1),
x_g(k)/x_g(k-1) = k(m+k-1-g) / [ (k-g)(m+k-1) ]           (k-g >= 1; x_g(k-1) = 0 if g = k),
```

both by telescoping the defining product. Equivalently

```
x_g(k+1) - x_g(k) = x_g(k+1) * g(m-1) / [ (k+1)(m+k-g) ]   >= 0 ,
x_g(k)  - x_g(k-1) = x_g(k)  * g(m-1) / [ k(m+k-1-g) ]      >= 0 .
```

*Proof of the difference forms.* `1 - x_g(k)/x_g(k+1) =
1 - (k+1-g)(m+k)/[(k+1)(m+k-g)]`, and `(k+1)(m+k-g) - (k+1-g)(m+k) =
g(m-1)` by expansion; same computation one step down. ∎

### Lemma P.3 (bracketing and the positivity floor) — PROVED.
For `2 <= k <= m`:

(i) *(pair bracketing)* Grouping `G^+` into the sign pairs
`P_1 = x_1 + x_2`, `P_2 = x_5 + x_7`, `P_3 = x_12 + x_15`, ...
(each `P_{j+1} <= P_j` termwise, since `x_g` is nonincreasing in `g` by
P.2(i)-factor count), the alternating pair series brackets `Phi`:

```
1 - x_1(k) - x_2(k)  <=  Phi(k)  <=  1 - x_1(k) - x_2(k) + x_5(k) + x_7(k) .
```

(ii) *(floor)* `Phi(k) >= 1 - x(k) - x(k)^2 > 0` whenever `x(k) < 0.618`;
in particular for `k <= m`, `x(k) <= m/(2m-1) <= 0.5085` (`m >= 30`) and
`Phi(k) >= 811/3481 >= 0.2329`.

*Proof.* (i) is the standard alternating-series bracket applied to
`Phi = 1 - P_1 + P_2 - P_3 + ...` with `P_1 >= P_2 >= ... >= 0`. (ii): from
(i) and P.2(i), `Phi >= 1 - x - x^2`, positive below the golden-ratio root. ∎
(NC-P1(b): brackets and floor verified in exact `Fraction`s at
`m in {12, 30, 60}`, all `2 <= k <= m-1`, zero violations; the floor's
minimum margin over the tested grid is `+0.00053` at `(m, k) = (60, 2)` —
i.e. at small `k` the floor is nearly exact, as `Phi = 1 - x_1 - x_2 + O(x^5)`
there.)

**Why this is the right normalization.** `log r(k) = Delta^2(-log I)(k) =
log r_T(k) + D_Phi(k)`, where

```
r_T(k) := T(k)^2/(T(k-1)T(k+1)) = 1 + (m-1)/(k(m+k))            (exact; merged draft NC-10),
D_Phi(k) := 2 log Phi(k) - log Phi(k-1) - log Phi(k+1) .
```

The pentagonal SIGNAL `(m-1)/(k(m+k))` is `Theta(1/m)` throughout
`k = Theta(m)`; §2 shows the CORRECTION `D_Phi` is `O(1/m^2)` there — this
size separation, invisible to the zeroth-order bracketing that Lemma 3.6
used, is what extends region 1 from `sqrt(m)/4` to `Theta(m)`.

## 2. Difference bounds on the pentagonal correction

Standing hypotheses for §2: `m >= 30`, `2 <= k <= min(c m, m-1)` for a fixed
`c in (0, 1]`, and

```
x+ := (k+1)/(m+k)  <=  xc(c) := (30c+1)/(30(1+c))     [c < 1; worst m = 30]
                      ,  xc(1) := 30/59                [c = 1, i.e. k <= m-1]
```

(`x+` is increasing in `k` and, at fixed `c`, decreasing in `m`; every `x(j)`,
`j in {k-1, k, k+1}`, is `<= x+`). Write `Psi := 1 - Phi`,
`d_+ := Psi(k+1) - Psi(k)`, `d_- := Psi(k-1) - Psi(k)`,
`A := d_+ + d_- = Delta^2 Psi`. The pentagonal sums used (all with positive
coefficients, hence increasing in `x`; exact `Fraction` evaluations at the
`xc(c)` values, with an explicit all-integer tail bound added, in NC-P2):

```
sigma_1'(x) := sum_{g in G^+} g x^g ,        sigma_2^-(x) := sum_{g in G^+, g >= 5} g^2 x^{g-2} .
```

### Lemma P.4 (first and second differences of `Psi`) — PROVED.
Under the standing hypotheses:

```
(i)  max(|d_+|, |d_-|) <= C_d(c)/m ,      C_d(c) := sigma_1'(xc)/xc ;
(ii) |A| <= C_A(c)/m^2 ,                  C_A(c) := 4 + 6 sigma_2^-(xc) ;
(iii) D_Phi(k) >= - C_P(c)/m^2 ,          C_P(c) := C_A(c)/Phimin(c) + C_d(c)^2/Phimin(c)^2 ,
      Phimin(c) := 1 - xc - xc^2 .
```

*Proof.* **(i).** By P.2(ii) all shift differences of `x_g` are `>= 0`, so
`|d_+| <= sum_{g >= 1} [x_g(k+1) - x_g(k)]` (the signs `eps(g)` can only
help). By P.2(iii), and `m+k-g >= m-1` for `g <= k+1`:

```
x_g(k+1) - x_g(k) = x_g(k+1) g(m-1)/[(k+1)(m+k-g)] <= g x_g(k+1)/(k+1) <= g (x+)^g/(k+1) .
```

Since `x+/(k+1) = 1/(m+k) <= 1/m`, summing gives
`|d_+| <= sigma_1'(x+)/(x+ (m+k)) <= sigma_1'(xc)/(xc m)` (using that
`sigma_1'(x)/x` is increasing in `x`). For `d_-` the same chain one step down
(`x_g(k) - x_g(k-1) <= g x(k)^g/k`, and `x(k)/k = 1/(m+k-1) <= 1/m`) gives
the same bound with `x(k) <= x+`.

**(ii).** `|A| <= sum_{g in G^+} |Delta^2 x_g|`, bounded per `g`:

*`g = 1`.* Exactly `Delta^2 x_1 = -2(m-1)/[(m+k-1)(m+k)(m+k-2)]`
(one-line computation from `x_1 = k/(m+k-1)`), and the denominator is
`>= m(m+1)(m+2) >= m^3` for `k >= 2`: `|Delta^2 x_1| <= 2/m^2`.

*`g = 2`.* Combining the two P.2(iii) ratios,

```
Delta^2 x_2 = 2(m-1)(m-2k) / [ (m+k)(m+k-1)(m+k-2)(m+k-3) ] ,
```

(direct expansion; at `k = 2` this reads `2(m-4)/[m(m+1)(m+2)]` after the
`(k-1)`-cancellation, consistent with `x_2(1) = 0`). Since `|m - 2k| <= m`
for `2 <= k <= m-1` and the denominator is `>= m^4` for `k >= 3` (for
`k = 2` the displayed exact form gives `<= 2/m^2` directly):
`|Delta^2 x_2| <= 2/m^2`.

*`g >= 5`, case `g <= (k+1)/2`.* From the two ratios,

```
Delta^2 x_g = x_g(k) g(m-1) [ (g-1)(m+k) - (g+1)k ] / [ (k+1-g) k (m+k)(m+k-1-g) ] ,
```

with `|(g-1)(m+k) - (g+1)k| <= 2g(m+k)`, `k+1-g >= (k+1)/2`,
`m+k-1-g >= m-1`:

```
|Delta^2 x_g| <= 4 g^2 (x+)^g / [k(k+1)]  =  4 g^2 (x+)^{g-2} (k+1)/[k(m+k)^2]  <=  6 g^2 (x+)^{g-2}/m^2
```

(`(k+1)/k <= 3/2` for `k >= 2`).

*`g >= 5`, case `g > (k+1)/2`* (so `k+1 <= 2g`): bound the two shift
differences separately. `x_g(k+1) - x_g(k) <= g(x+)^g/(k+1)
= g (x+)^{g-2} (k+1)/(m+k)^2 <= 2g^2 (x+)^{g-2}/m^2`; similarly
`x_g(k) - x_g(k-1) <= g (x+)^g / k <= (3/2) g (x+)^{g-2}(k+1)/(m+k)^2
<= 3 g^2 (x+)^{g-2}/m^2`; total `<= 5 g^2 (x+)^{g-2}/m^2 <= 6 g^2 (x+)^{g-2}/m^2`.

Summing: `|A| <= [2 + 2 + 6 sigma_2^-(x+)]/m^2 <= C_A(c)/m^2`.

**(iii).** With `Phi_j = 1 - Psi_j`:

```
Phi(k-1)Phi(k+1) = (1-Psi_k-d_-)(1-Psi_k-d_+) = Phi(k)^2 [ 1 - A/Phi(k) + d_- d_+ / Phi(k)^2 ] ,
```

so `D_Phi = -log[1 - A/Phi(k) + d_- d_+/Phi(k)^2]
>= -log[1 + |A|/Phimin + C_d^2/(m^2 Phimin^2)] >= -C_P(c)/m^2`
(`-log(1+u) >= -u`; `Phi(j) >= Phimin(c)` for all three `j` by P.3(ii) with
`x(j) <= xc`). ∎

**Certified values (NC-P2, exact `Fraction` chain, tail `< 1e-100` added):**

| `c` | `xc` | `Phimin` | `C_d` | `C_A` | `C_P` |
|---|---|---|---|---|---|
| 1/4 | 0.2267 | 0.7220 | 1.4675 | 5.923 | **12.34** |
| 1/2 | 0.3556 | 0.5180 | 1.8053 | 12.443 | **36.17** |
| 7/10 | 0.4314 | 0.3825 | 2.0823 | 20.649 | **83.61** |
| 1 | 0.5085 | 0.2329 | 2.4804 | 34.920 | **263.23** |

**Measured truth (NC-P2, exact binomial `Phi`, `2 <= k <= m-1`):**
`max m^2|A| = 0.75` (essentially `m`-independent), `max m|d_pm| = 1.00`
(at `k = 2`), `max m^2 |D_Phi| = 0.95..1.00` (at `k = 2`, drifting to 1 from
below). So the proved `C_P` carries a factor 12 (`c = 1/4`) to 260 (`c = 1`)
of triangle-inequality slack over truth — honest, and irrelevant downstream:
§3's thresholds all land at or below the harness range except `c = 1`.

## 3. Theorem P.5: region 1 extended to k = Theta(m)

### Theorem P.5 — PROVED.
Let `c in {1/4, 1/2, 7/10, 1}`, `m >= m_p(c)` as tabulated below, and
`2 <= k <= min(c m, m-1)`. Then

```
r(k) - 1  >=  (m-1) / (2 k (m+k))          ( >= (m-1)/(2c(1+c) m^2) ) ,
```

and more precisely `r(k) - 1 >= (m-1)/(k(m+k)) - 1.5 C_P(c)/m^2` on the same
range for every `m >= 30`.

| `c` | `C_P(c)` | `m_p(c)` (`= max(30, ceil(3 C_P c(1+c) + 1))`) |
|---|---|---|
| 1/4 | 12.34 | **30** |
| 1/2 | 36.17 | **83** |
| 7/10 | 83.61 | **300** |
| 1 | 263.23 | **1581** |

*Proof.* By P.1–P.3, `log r(k) = log r_T(k) + D_Phi(k)` with
`r_T(k) - 1 = (m-1)/(k(m+k)) =: s` (exact), and by P.4(iii)
`D_Phi >= -u`, `u := C_P(c)/m^2`. Hence
`r(k) >= r_T(k) e^{-u} >= (1+s)(1-u)`, so

```
r(k) - 1 >= s - u(1+s) >= s - 1.5 u
```

(`s <= (m-1)/(2(m+2)) < 1/2` at `k = 2`, and `s` is decreasing in `k`).
This is the "more precisely" clause. For the main clause, `s - 1.5u >= s/2`
iff `s >= 3u` iff `k(m+k) <= m^2(m-1)/(3 C_P(c))`; since `k(m+k)` is
increasing in `k`, it suffices at `k = c m`: `c(1+c) <= (m-1)/(3 C_P(c))`,
i.e. `m >= 3 C_P(c) c(1+c) + 1`, which is the table's `m_p(c)`. ∎

**Ground truth (NC-P1(c), exact integer cross-multiplication, no floats in
the verdict):** `r(k) - 1 >= (m-1)/(2k(m+k))` holds with ZERO violations for
every `8 <= m <= 200` and every `2 <= k <= m-1` — i.e. even at `c = 1` the
inequality is TRUE far below the proved threshold 1581. Global minimum of
`(r-1)/[(m-1)/(2k(m+k))]` = `2.0002` at `(m, k) = (200, 2)`: the true
correction at small `k` is `O(x^5)`-tiny and the factor-2 safety margin of
the statement is intact everywhere on the tested grid. (The four range rows
in NC-P1's output all report the same min — the bound is uniformly slack by
`>= 2x` on `m <= 200`.)

**Remarks.**
1. *Region-1 conclusion strength.* On `k <= c m` the bound beats the
   Theorem-A comparison scale `sigma^{-2} = 1/lambda` by a factor
   `(m-1)^2(2m+5)/(144 c(1+c) m)`: at `(m, c) = (401, 7/10)` this is
   `1879x`; at `(1581, 1)` it is `17364x` (NC-P4). Nothing downstream is
   tight against region 1.
2. *Relation to Lemma 3.6.* Lemma 3.6 (merged draft, PROVED) is retained for
   `k = 1` (P.5 needs `k >= 2`) and for `m < 30`. On `sqrt(m)/4 <= k <= cm`,
   P.5 replaces the zero-slack chain of 3.6 entirely; on `k <= sqrt(m)/4`
   both hold (P.5's bound is then `~1/(2k) * (m-1)/(m+k)`, within a factor
   ~2 of 3.6's `(m-1)/(2k(m+k))` — identical form).
3. *Why not `k > m`.* Lemma P.1 fails for `k > m` (the coefficients of
   `prod_{j<=m}(1-q^j)` are no longer `0, ±1` there); an extension to
   `k <= 2m` via `prod_{j>m}(1-q^j)^{-1} = 1 + q^{m+1} + ...` is mechanical
   but buys only a constant in the §4 arithmetic (the floor `s2 >= Theta(m)`
   is already reached at `k = c m`) — not pursued.

## 4. Handoff lemmas P.6–P.8

### Lemma P.6 (variance floor on the residual band) — PROVED.
For every interior `k` with `c m <= k <= N/2`:

```
s2 = sigma_{lam(k)}^2 >= (k/6)(1 + k/m) >= v(c) m ,      v(c) := c(1+c)/6 ,
```

i.e. `v(1/2) = 1/8`, `v(7/10) = 0.1983`, `v(1) = 1/3`. Consequently
`s2 >= C_0` on the whole band as soon as `m >= C_0/v(c)`.

*Proof.* T.5-final (T2 §2; PROVED there, and verified "CORRECT, fully" by the
T2 maths referee §2.6) plus monotonicity of `(k/6)(1+k/m)` in `k`. ∎

This is the item-2 repair in one line ONCE region 1 reaches `k = c m`
(Theorem P.5): the old inner edge `k ~ sqrt(m)/4` gave only
`s2 >= sqrt(m)/24`, hence `m >= (24 C_0)^2`; the new edge gives a LINEAR
law `m >= C_0/v(c)`. With `C_0 = 2000` intact: `m >= 6000` (`c = 1` clause,
`m >= 1581` satisfied) — down from `2.3e9` by a factor `3.8e5` (NC-P4).

### Lemma P.7 (all-`w` deficit floor) — PROVED.
Let `m >= 30`, `lam` real, `w = lam m`. With the (T.4a'')-kernel
`E(u) := (1/12 - q(u))/u^2 = sum_{n >= 1} 2(3 v_n^2 + u^2) / (v_n^2 (v_n^2 + u^2)^2)`,
`v_n = 2 pi n` (T2 §2; partial-fraction block verified by the T2 maths
referee; `E` positive, decreasing in `|u|`, `E(0) = 1/240`):

```
1 - s2/lambda  >=  6.85 w^2 E(w) ;    and for |w| >= w0:   1 - s2/lambda >= 6.85 w0^2 E(w0)
```

(the second clause by Lemma 3.3's deficit monotonicity applied at
`|lam| >= w0/m`).

In particular (certified lower decimals for `E`, NC-P3b: 50000-term positive
partial sums, truncation `< 2e-21`):

| `w0` | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| `E(w0) >=` | .00400693 | .00358719 | .00304036 | .00248992 | .00200652 | .00161241 |
| deficit `>=` | 0.0274 | 0.0983 | 0.1874 | **0.2729** | 0.3436 | 0.3976 |
| `rho(w0) :=` `s2/lambda <=` | 0.9726 | 0.9017 | 0.8126 | **0.7271** | 0.6564 | 0.6024 |

and by deficit monotonicity in `|lam|` (merged draft Lemma 3.3, FULLY
PROVED), `s2 <= rho(w0) lambda` holds for ALL `|w| >= w0`.

*Proof.* From T2's (T.4) Step-2 display (proved there; maths referee §2:
T.4 correct): `lambda - s2 = lam^2 sum_{j=1}^m [ j^4 E(lam j) - E(lam) ]`.
Since `E` is decreasing and `lam j <= w` for `j <= m`:
`lambda - s2 >= lam^2 [ E(w) S_4 - m/240 ]`. Divide by
`lambda <= 1.05 m^3/36` (B.0(i), `m >= 30`) and use `S_4 >= m^5/5`
(`m >= 8`; certified exactly in T2's NC-T2 bracket):

```
1 - s2/lambda >= (w^2/m^2) (36/(1.05 m^3)) [ E(w) m^5/5 - m/240 ]
             = 6.857 w^2 E(w) [ 1 - 1/(48 E(w) m^4) ]  >=  6.85 w^2 E(w)
```

(the bracket is `>= 0.9996` for `m >= 30` and `|w| <= 8`, where
`E(w) >= 0.001`; for `|w| > 8` the clause used downstream is the monotone
one at `w0 <= 6`). ∎ (Consistency, NC-P3c: the TRUE deficit at `|w| = w0`
exceeds the floor at every tested `(m, w0)`, capturing 82–90% of truth at
`w0 <= 4` — e.g. `m = 60, w0 = 4`: true 0.3327 vs floor 0.2729.)

**Why P.7 is needed at all:** T2's (T.4)-lower carries the factor
`(1 - w^2/19)`, useless beyond `|w| ~ 3` and scoped to `|w| <= pi`; the
stitch's region-3/region-2 boundary sits at `w0 = 4` (to reuse wp2-b's
`K = 4` dictionary), where only the `E(w)`-form above gives a nontrivial
`rho`. It also repairs, at `w0 <= 1`, the same constant the T2 maths referee
repaired in T.10(2) (`rho = 1 - 0.022 w_0^2`; P.7 gives the stronger
`1 - 0.0274 w_0^2` at `w_0 = 1` — consistent, since `6.85 E(1) = 0.02745 >
0.022`).

### Lemma P.8 (tilt cap on the residual band) — PROVED.
For every interior `k >= c m` (`c in (0, 1]`, any `m >= 2`):

```
lam(k) <= log(1 + 1/c) ;
```

in particular `lam(k) <= 1.0987` for `k >= m/2`, `<= 0.8874` for
`k >= 0.7 m`, `<= 0.6932` for `k >= m` (all rounded up, safe direction for a
cap).

*Proof.* For `lam > 0`, each tilted factor satisfies
`E U_j^{lam} <= 1/(e^lam - 1)`: `U_j^{lam}` is the untruncated geometric
`G ~ Geom(e^{-lam})` conditioned on `{G < j}`, and conditioning on a lower
set can only lower the mean (`E[G | G < j] <= E[G | G >= j]` trivially,
hence `E[G | G < j] <= E G = 1/(e^lam - 1)`). Summing, `mu(lam) <=
m/(e^lam - 1)`. At `lam_c := log(1 + 1/c)`, `e^{lam_c} - 1 = 1/c`, so
`mu(lam_c) <= c m <= k`; since `mu` is strictly decreasing (Lemma 3.1),
`lam(k) <= lam_c`. ∎ (NC-P3a: measured `lam(cm)` rises to the cap from
below — e.g. `c = 0.7`: 0.8403 (m=30) -> 0.8869 (m=3000) vs cap 0.8873.)

**Consequence for wp4's scope.** The deep-tilt core lemma is needed ONLY for
`lam in (w0/m, log(1+1/c)]` — a range on which wp1-c's far bounds are
already PROVED: Corollary W.5(ii) covers `pi/m <= |lam| <= 1.7627 >
1.0987` on `t in [t_0(lam), pi]` with exponent floor `0.0373 m`, and Clause
W.6 covers the crossover `[pi/m, t_0(lam)]`. wp4 owes only the core
`|t| <= pi/m`-scale model (STATUS §2 item 1's identified strip-analyticity
route), not any new decay bound.

## 5. Theorem S: the stitching table

**Operating point** (fixed for the rest of the draft): `w0 = 4` (so region 3
is exactly wp2-b's `K = 4` dictionary), `delta = 0.02`,
`rho := rho(4) <= 0.7271` (P.7), clause `c = c(m) := 7/10` for
`401 <= m < 1581` and `1` for `m >= 1581` (Theorem P.5's ladder).

**The future crude law, as a parameter.** Write `CL(C_0*, C*, Lambda*)` for
the statement: *for interior `k` with `s2 >= C_0*` and `|lam(k)| <= Lambda*`,
`r(k) - 1 = s2^{-1}(1 + theta C*/min(m, s2))`, `|theta| <= 1`.* This is Prop
3.5(i)'s shape; its proof for the deep-tilt range is wp4's package (the core
model is the one missing piece — the far/crossover decay it needs is already
PROVED in wp1-c W.5/W.6, see P.8's consequence). A lower-bound-only variant
(`r(k)-1 >= (1 - C*/min(m,s2))/s2`) suffices everywhere below.

### Theorem S (gap-free stitching; a reduction with two named conditions).
Let `m >= 401` and WLOG `1 <= k <= N/2` interior. Define the partition

```
K_c := min(c m, m-1) ;
R1a := {k = 1} ,   R1b := {2 <= k <= K_c} ,
R2   := {k > K_c , |w(k)| > 4} ,   R3 := {k > K_c , |w(k)| <= 4} ,
```

(`w(k) = m lam(k)`; for `c = 1`, `k > K_c` means `k >= m`, so P.6's floor
`(k/6)(1+k/m) >= m/3` still applies verbatim). Then, with every constant
explicit:

| region | facts (all PROVED here or cited-PROVED) | conclusion `lambda (r(k)-1) >=` | conditional on |
|---|---|---|---|
| R1a | Lemma 3.6 (merged draft): `r(1)-1 >= (m-1)/(2(m+1))` | `>= 10^5` (any `m >= 401`) | — |
| R1b | Theorem P.5 (`m >= m_p(c)` holds: `401 >= 300`, `1581` at the switch): `r-1 >= (m-1)/(2k(m+k))` | `>= (m-1)^2(2m+5)/(144 c(1+c) m)` `= 1879` at `m = 401` | — |
| R2 | P.6: `s2 >= v(c) m >= 79.5`; P.7+L3.3: `s2 <= 0.7271 lambda`; P.8: `lam(k) <= 0.8874` (`c = 7/10`) / `0.6932` (`c = 1`); so CL applies with `C_0* = 79 <= s2`, `Lambda* = 0.89`, and errs `C*/min(m, s2) <= 20/79.5 = 0.2516 <= eps* := 1 - 1.02 rho = 0.2584` | `>= (1 - 0.2516)/rho = 1.0294 >= 1.02` | **wp4**: `CL(79, 20, 0.89)` |
| R3 | wp2-b Theorem W.7 at `K = 4` (`m >= 180` ✓), `c_w(4) = 1` (repair B2), buckets `C_R^PT(4) = 5.30` (grid, `m <= 2000`; closed-form all-`m` flavor 187.8) + `Lin = 0.372`; far bucket viable: wp1-c W.4(i) `c_1(4) = 0.1019`, threshold `m_2(4) = 379 <= 400 < 401` (proxy criterion, flagged); core: T.9'' (T2; maths referee: fully verified); plus P.7's `w^2`-coefficient domination `6.85 E(4) = 0.01706 >= B_m (1 + 17 B_m + ...)`, valid `m >= 100` | `>= 1 - B_m - [C_R^PT(4) + C_ker + Lin]/m^2` | **wp2-a**: the `Delta_ker` bucket constant `C_ker` |

Since R1a/R1b/R2 all give `lambda(r-1) >= 1.02 > 1 - B_m`, the global
minimum lies in R3 and

```
sigma^2 (r_m - 1) >= 1 - B_m - [C_R^PT(4) + C_ker + Lin]/m^2      for all m >= 401 ,
```

while for `4 <= m <= 400` all of Theorem A parts (a-finite)/(b)/(c-finite)
hold EXACTLY (harness_m200 C1–C6). **Coverage is gap-free in both `m` and
`k`; the only conditions are the two named open packages (wp4's CL at
`(79, 20, 0.89)`; wp2-a's `C_ker`), plus the standing citation statuses
(§0).** ∎ (proof = the table rows, each verified in §1–§4 or cited)

**Derivation notes for the table (all one-line, recorded for the referee):**

1. *R2 partition membership.* `|w| > 4` and Lemma 3.3 (deficit nondecreasing
   in `|lam|`) + P.7 at `w0 = 4` give `s2 <= 0.7271 lambda`; `k > c m` and
   P.6 give `s2 >= v(c) m` (`v(7/10) 401 = 79.5`, `v(1) 1581 = 527`); P.8
   caps the tilt. CL's conclusion then yields `r - 1 >=
   (1 - 0.2516)/s2 >= 0.7484/(0.7271 lambda)`. The error budget is monotone
   in `m` along each clause and jumps favorably at the `c`-switch
   (`min(m, s2) >= 527` there).
2. *R3 chain.* `lambda(r-1) = (lambda/s2) * s2(r-1) >= (1 + D)(1 - B_m(1 +
   w^2) - C/m^2)` with `D = 1 - s2/lambda >= 6.85 E(4) w^2` (P.7, since `E`
   decreasing makes `E(w) >= E(4)` on `|w| <= 4`), `C := C_R^PT + C_ker +
   Lin`. Expanding: `>= 1 - B_m - C/m^2 + w^2 [ 6.85 E(4)(1 - 17 B_m -
   C/m^2) - B_m ]`, and the bracket is `>= 0.01628 - 0.00270 > 0` at
   `m = 401` (NC-P4 prints the crossover: `m >= 63.3` ignoring the
   `(1 - 17B_m)` factor, `m >= ~68` with it). The `w^2`-term is then
   discarded (nonnegative), leaving the displayed bound. The `Lin` bucket's
   hypothesis `|s2 log r - 1| <= 1/2` is discharged exactly as wp2-b §6
   remark 2 states (any `C_ker <= 10^4`).
3. *R1a value.* `lambda (r(1)-1) >= lambda (m-1)/(2(m+1)) ~ m^3(m-1)/(72 m)`
   — astronomically clear of 1.02.
4. *No use of T.8/T.8-final anywhere.* R2's tilts satisfy `|w| > 4 > pi`, so
   T.8-final's scope (`|lam| <= pi/m`) is disjoint from R2; the band it does
   cover lies inside R3, where the refined law is used instead. The old
   `C_0 = 2000` and `C = 600` therefore appear NOWHERE in this stitch: item
   2's mismatch is not "worked around" but replaced by the explicit CL spec.
   Similarly T.10(2)'s (repaired) overlap annulus is not needed — the
   partition is exact, not an overlap argument.

**Threshold table (NC-P4 output, verbatim basis for the claims above):**

```
m-range        clause c   s2 floor at range start   tilt cap   C_0* max   C* max
[401, 1581)      0.70     0.1983*m >=     79.5       0.8873        79       20
[1581, inf)      1.00     0.3333*m >=    527.0       0.6931       527      136
OLD (T2 item 2): floor sqrt(m)/24 >= 2000  <=>  m >= 2.3e+09
NEW, C_0* = 2000 intact: c=1 clause, m/3 >= 2000  <=>  m >= 6000   (3.8e5 x better)
```

If one insists on `C_0 = 2000` intact (the assignment's route 2 flavor): the
stitch above closes gap-free for all `m >= 6000` with `C*` still needing
`<= eps* * min(m, s2)|_{m=6000} = 0.2584 * 2000 = 516` — i.e. even the
UNCERTIFIED old `C = 600` would nearly suffice there; the honest statement
remains that CL itself (any constants) is open pending wp4's core model.

## 6. Requirement specs for the open packages

### 6.1 wp4 (deep-tilt core -> the crude law CL) — what is actually needed.

```
CL(C_0* = 79, C* = 20, Lambda* = 0.89)   for all m >= 401
```

(lower-bound form suffices). Support the spec gives wp4:

1. **Scope is bounded**: only `4/m < lam <= 0.89` ever arises (P.8 + R3
   taking `|w| <= 4`); for `m >= 1581` only `lam <= 0.70`. All of it sits
   inside wp1-c's PROVED far machinery: W.5(ii) on `[t_0(lam), pi]`
   (exponent `m q(m sinh(lam/2), 1) >= 0.0373 m`), W.6 on the crossover
   `[pi/m, t_0(lam)]`, and (T.6ii) Gaussian domination on `[0, pi/m]`
   (distribution-free, T2 — maths referee: correct). The ONLY missing
   ingredient is the two-sided core model on the `1/sqrt(s2)`-scale
   (STATUS §2 item 1; wp1-c §9 item 2's strip-analyticity route: `log
   phi_lam` is analytic in `|Im t| < lam`, and on the residual band `lam`
   is a CONSTANT `in [4/m, 0.89]` — precisely the regime where the
   cumulant-model radius `~ c lam` beats the Gaussian width
   `1/sqrt(s2) ~ 1/sqrt(v(c) m)`; the ratio is `lam sqrt(s2) >=
   (4/m) sqrt(79.5) ...` growing like `sqrt(m)` at fixed `lam`).
2. **The truth has 6x-plus margin** (NC-P3d, exact rows + closed-form `s2`):
   `eps(k) := |s2 (r(k)-1) - 1| <= 0.0385` over EVERY interior `k` at
   `m = 30` — with no variance threshold at all — falling to `0.0084` by
   `m = 140` (`~1.2/m`). The spec asks only `eps <= 0.2516` at `s2 >= 79`.
   Equivalently: the measured `C_0` at tolerance `eps = 0.25` is BELOW the
   smallest interior `s2` on the tested range (`trueC0 = 0` rows in
   NC-P3d) — "truth `C_0 ~ 10`" (STATUS) was already conservative.
3. **What would falsify the stitch**: only a core-model constant so weak
   that `C* > 20` at `s2 ~ 80`. Given 2., that would mean losing a factor
   ~6 at `m = 401` (and the requirement relaxes linearly in `m`; from
   `m >= 1581` the budget is `C* <= 136`).

### 6.2 wp2-a (`Delta_ker`) — unchanged, with one addition.
The stitch consumes `C_ker` exactly as wp2-b Theorem W.7 defines it, at
`K = 4` only. Measured target size `~5.04` in `C_R` units (wp2-b NC-W4(6),
numerics-referee-verified). Addition from this package: once `C_ker` lands,
Theorem S's R3 row plus the harness gives part (a)'s lower bound for ALL
`m` with explicit constants `[5.30 + C_ker + 0.38]/m^2` — no further
stitching work is needed; the reduction here is final modulo wp4.

### 6.3 The refined-law far bucket at `K = 4` (caveat carried).
`m_2(4) = 379` is the NC-T10d-criterion proxy (wp1-c §9 item 5 caveat,
STATUS §2 item 5): the eventual W.7+`Delta_ker` assembly must check its own
polynomial prefactor against `c_1(4) = 0.1019`. Because the harness now
reaches 400, ANY landing point `m_2'(4) <= 400` keeps Theorem S gap-free
as stated; if the true assembly threshold exceeded 400, the harness
extension (`~m^3` scaling, 321 s to 400 — `m = 600` is minutes) absorbs it.

## 7. Numeric checks (all scripts in `g2_scripts/campaign_20260811/wp3_a2/`, run 2026-08-11)

| # | script | validates | real result |
|---|---|---|---|
| NC-P1 | `wp3a2_nc1_pentagon.py` | P.1 identity (exact ints, 7 values of `m`, all `k <= m`); P.3 brackets+floor (exact Fractions); **P.5 truth: exact cross-multiplied check of `r(k)-1 >= (m-1)/(2k(m+k))`, ALL `2 <= k <= m-1`, ALL `8 <= m <= 200`** | **PASS** — 0 identity mismatches; 0 bracket violations; **0 inequality violations**; global min slack 2.0002 at (200, 2) |
| NC-P2 | `wp3a2_nc2_constants.py` | the P.4 constant chain in exact Fractions (tail bound added); the `(c, m_p)` table; measured truth of `m^2|A|`, `m|d|`, `m^2|D_Phi|` | **PASS** — table §2; truth: 0.75 / 1.00 / 0.95–1.00, i.e. proved constants have 12x–260x slack |
| NC-P3 | `wp3a2_nc3_handoff.py` | P.8 cap (measured `lam(cm)` vs `log(1+1/c)`, 15 rows); P.7 `E`-decimals (50000-term positive partial sums) + floor-vs-truth; deep-band truth `eps(k)` from exact rows | **PASS** — cap never violated, approached from below; floors hold with 82–90% capture; `max eps = 0.0385 (m=30) .. 0.0084 (m=140)` over ALL interior `k` |
| NC-P4 | `wp3a2_nc4_stitch.py` | the Theorem S threshold table; legacy-constant comparisons; R1 margins | **PASS** — table §5; OLD `2.3e9` reproduced from `(24*2000)^2`; NEW 6000 at `C_0 = 2000`; R1 margins 1879x / 17364x |

Key verbatim excerpts:

```
NC-P1: exact violations of  r(k)-1 >= (m-1)/(2k(m+k)):  0
       global min of (r-1)/[(m-1)/(2k(m+k))] = 2.0002 at (m,k)=(200,2)
NC-P2:  c      xc      Phi_min     C_d      C_A       C_P      m_p(c)
       0.25  0.2267   0.7220    1.4675    5.923     12.34       30
       0.50  0.3556   0.5180    1.8053   12.443     36.17       83
       0.70  0.4314   0.3825    2.0823   20.649     83.61      300
       1.00  0.5085   0.2330    2.4804   34.920    263.23     1581
       measured:  m=400:  max m^2|A| = 0.7409 (k=168),  max m*d = 1.0000 (k=2),
                  max m^2|D_Phi| = 0.9951 (k=2)
NC-P3(a): c=0.7 cap=0.8873: m=30:0.8403  m=100:0.8739  m=300:0.8829  m=1000:0.8860  m=3000:0.8869  (all <= cap)
NC-P3(b): E(4) >= 0.00248992  ->  deficit >= 0.2729,  rho(4) <= 0.7271
NC-P3(c): m=60:  w0=4: true 0.3327 >= floor 0.2729 ok   (all 10 rows ok)
NC-P3(d):   m   max_eps(band [0.7m, w=4 edge])   max_eps(s2 >= 50)
           30   0.0385 (k=114)                    0.0385
           60   0.0194 (k=476)                    0.0194
          100   0.0117 (k=1344)                   0.0117
          140   0.0084 (k=2652)                   0.0084
          (eps never exceeds 0.25 at ANY interior k on the tested range)
NC-P4:  [401, 1581)  c=0.70  floor 0.1983*m >= 79.5  cap 0.8873  C_0* <= 79  C* <= 20
        [1581, inf)  c=1.00  floor 0.3333*m >= 527   cap 0.6931  C_0* <= 527 C* <= 136
        OLD floor sqrt(m)/24 >= 2000 <=> m >= 2.3e+09 ;  NEW (C_0=2000): m >= 6000
```

(Precision notes: NC-P1 and NC-P2's chain are exact integer/`Fraction`
arithmetic end-to-end; NC-P2's measured block, NC-P3 and NC-P4 use floats as
measurement only — no proved constant depends on them except the `E(w0)`
lower decimals, which are partial sums of a positive series with the
truncation size printed (`< 2e-21`), and the `Phi_min` entry 0.2330 whose
safe-direction value 0.2329 = 811/3481 is used in the text.)

## 8. What remains / honest markers

**Status recap.** PROVED here, unconditionally: Lemmas P.1–P.4, Theorem P.5
(region 1 extended to `k = c m`, thresholds 30/83/300/1581), Lemma P.6 (the
linear `C_0` arithmetic), Lemma P.7 (all-`w` deficit floor), Lemma P.8 (tilt
cap). PROVED AS A REDUCTION: Theorem S — gap-free `(m, k)` coverage for
Theorem A's minimum bound, `m <= 400` exact, `m >= 401` conditional on
exactly wp4's `CL(79, 20, 0.89)` and wp2-a's `C_ker`. **T2 §8 item 2 in its
original form (the `C_0 = 2000` unreachability) is CLOSED**: the arithmetic
mismatch is gone (linear, not quadratic, in `C_0`; `m >= 6000` even at
`C_0 = 2000`; no use of `C_0 = 2000` or `C = 600` anywhere in the stitch).
What item 2 always concealed — that the band's tilts are CONSTANTS, so the
crude law there needs the deep-tilt core — is now isolated, capped
(`lam <= 0.89`), and spec'd (§6.1), not closed. Honest markers:

1. **The deep-tilt core (wp4) is the load-bearing condition of R2.** Nothing
   here touches it; the stitch quantifies exactly what it must deliver and
   proves everything around it. The measured margin on its target is 6x-plus
   (NC-P3d) and the scope is a compact `lam`-interval with all decay bounds
   already proved (wp1-c) — but it is genuinely open mathematics (STATUS §4
   item 4a) and this draft does NOT close it.
2. **R3 is conditional on wp2-a** (`C_ker`, T2 §8 item 4's last bucket), and
   carries wp2-b's own statuses: the `PW_grid`/`C_R^PT(4) = 5.30` flavor is
   grid-certified to `m <= 2000` (with the +0.22% caveat, wp2-b repair B3:
   carry `~5.31` beyond the grid or use the closed-form 187.8 all-`m`
   flavor — either fits Theorem S; the R3 conclusion line simply inherits
   whichever constant is quoted); `m_2(4) = 379` is proxy-criterion (§6.3).
3. **Citation statuses.** T2 items used (T.5-final, (T.4)-Step-2 display,
   (T.6ii), Lemma 3.1's `mu' < 0`, T.9'') now carry BOTH referee passes
   (numerics MINOR_REPAIRS + maths MINOR_REPAIRS, `referee_t2_maths.md`),
   with T.5 and the T.4 partial-fraction block explicitly verified there;
   none of the two items the maths referee found broken (T.10(2), T.8'') is
   used here. wp1-c and wp2-b are double-refereed MINOR_REPAIRS with repair
   lists discharged (`repairs_20260811.md`). Under the house rule this
   draft itself has ZERO referees until its own pass runs.
4. **Finite-computation steps (not gaps).** The `C_d, C_A, C_P` values are
   exact-`Fraction` evaluations of explicit pentagonal series (safe-side
   tail added); `E(w0)` lower decimals are positive partial sums (truncation
   `< 2e-21`, printed). Sturm-style certificates are not needed anywhere in
   §1–§4: every inequality in the P.4 chain is displayed algebra.
5. **Slack.** The proved `C_P(c)` exceed measured truth by 12x–260x
   (triangle inequality on the alternating pentagonal tail; NC-P2). If a
   future assembly needs `c = 1` below `m = 1581`, the two-sided pair
   bracketing (P.3(i) with one more pair) would tighten `C_A` by roughly
   the observed factor — mechanical, not done. Likewise `k <= 2m` via the
   corrected expansion (P.5 remark 3) is available but unneeded.
6. **What the next sessions should do, in order** (updating STATUS §5): (i)
   wp2-a / merge (closes Prop 3.5(ii) and fills Theorem S's R3 constant);
   (ii) wp4 core model against the §6.1 spec (closes R2 — and with it Prop
   3.5(i) in the only range Theorem A still needs, `lam <= 0.89`,
   `s2 >= 79`); (iii) referee this draft (house rule); (iv) then Theorem A
   assembly is literally Theorem S's table plus Corollary 2.3's central
   value — no further stitching session is required.

*End of wp3_draft_a2. Blind protocol maintained: `g2_draft_t1_20260803.md`
and the parallel `wp2_a2` package were not read; no existing file modified.*
