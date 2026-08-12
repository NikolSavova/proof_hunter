# wp4_sl_SL2 — Tilt–variance product floor: `A = lam^2 s2 >= c_A(w) m` (SL2, PROVED)

*Wave-3 prover deliverable, F2 campaign (Mahonian log-concavity, Theorem A),
2026-08-12. Assignment: sub-lemma SL2 of `wp4_plan_20260811.md`, verbatim
scope; no other sub-lemma touched. Status: **PROVED** — all three parts (i),
(ii), (iii), with part (i) strengthened to strict inequality and part (ii)
proved with **zero discreteness loss** (the plan's `O(lam)` discreteness
budget and the W7 anchor route turn out to be unnecessary; see §7).
Self-contained: consumes only the standing frame of `wp4_plan_20260811.md`
§0 (`s2 = sum_j Var(U_j^lam)`, independence — merged-draft Lemma 3.1 frame)
plus elementary analysis; the M2 rescue lemma is NOT needed. Scripts (all
SAVED and RUN, outputs archived beside them) in
`g2_scripts/campaign_20260811/wp4_SL2/`:
`sl2_e1_identity_monotone.py` (`out_sl2_e1.txt`),
`sl2_e2_band_certificate.py` (`out_sl2_e2.txt`),
`sl2_e3_truth_m401.py` (`out_sl2_e3.txt`). House rules: exact
`Fraction` arithmetic for every certified constant; safe-direction rounding
only (floor-prints for lower bounds, ceil-prints for upper bounds); no
existing file modified.*

## 0. Statement

Standing notation (plan §0): `U_j^lam` (`j = 1..m`) independent with
`P(U_j^lam = i) = e^{-lam i}/z_j(lam)` on `{0,...,j-1}`;
`s2 = sigma_lam^2 = Var(sum_j U_j^lam) = sum_{j=1}^m Var(U_j^lam)`;
`w := m lam`; `A := lam^2 s2`; residual band
`B(m) = { lam : 4/m < lam <= 0.89 }`; `w`-bands
`W1 = (4,5], W2 = (5,6], W3 = (6,8], W4 = (8,10], W5 = (10,20],
W6b = (20,40], W7 = (40, infty)` (each intersected with `lam <= 0.89`;
they partition `{w > 4}`).

**SL2 (proved below).**
**(i)** For every real `lam` and every `j >= 1`:
`Var(U_{j+1}^lam) > Var(U_j^lam)` (strict; the plan asked `>=`).
**(ii)** For every `m >= 401` and `lam in B(m)` (WLOG `lam > 0`; both signs
covered by evenness, see §5.3):

```
lam^2 s2 >= c_A(w) m ,
band:  W1    W2    W3    W4    W5    W6b   W7
c_A:   0.28  0.35  0.42  0.52  0.60  0.70  0.80
```

**(iii)** Corollaries: `s2 >= 1122800/7921 = 141.749... >= 141 > 79` on the
whole band (CL's `s2 >= 79` hypothesis is implied, never binding); and
`A/min(m, s2) >= c_A(w)`. Bonus (recorded for SL5): `s2 > m` on all of
`B(m)`, `m >= 401`, so `min(m, s2) = m` there (§5.2).

## 1. The exact variance identity

Throughout, define

```
h(x) := x^2 e^x / (e^x - 1)^2  =  ( x / (2 sinh(x/2)) )^2      (x != 0),
h(0) := 1  (the limit),        v(x) := 1 - h(x).
```

The second form follows from `e^x - 1 = e^{x/2}(e^{x/2} - e^{-x/2}) =
2 e^{x/2} sinh(x/2)`, so `x^2 e^x/(e^x-1)^2 = x^2/(2 sinh(x/2))^2`. In
particular `h` is **even**. `v` is exactly the plan's continuum profile:
`1 - a^2 e^{-a}/(1 - e^{-a})^2 = 1 - a^2 e^a/(e^a - 1)^2` (multiply
numerator and denominator by `e^{2a}`).

**Lemma SL2.0 (closed form).** For every real `lam != 0` and `j >= 1`,

```
Var(U_j^lam) = e^{lam}/(e^{lam}-1)^2 - j^2 e^{j lam}/(e^{j lam}-1)^2 ,
equivalently    lam^2 Var(U_j^lam) = h(lam) - h(j lam) = v(j lam) - v(lam) ;
```

and for `lam = 0`, `Var(U_j^0) = (j^2-1)/12` (uniform), which is the
`lam -> 0` limit of the display.

*Proof.* `U_j^lam` is the exponential-family tilt of the uniform on
`{0,...,j-1}`: with `Z_j(lam) := sum_{i=0}^{j-1} e^{-lam i} =
(1 - e^{-lam j})/(1 - e^{-lam})` (`lam != 0`), we have
`Z_j' = - sum_i i e^{-lam i}`, hence `(log Z_j)'(lam) = -E U_j^lam` and
`(log Z_j)''(lam) = Z_j''/Z_j - (Z_j'/Z_j)^2 = E (U_j^lam)^2 -
(E U_j^lam)^2 = Var(U_j^lam)` — the standard cgf identity, valid for all
real `lam` since `Z_j` is a finite sum of exponentials, positive and smooth.
Set `psi(x) := log|1 - e^{-x}| = log|e^x - 1| - x` for `x != 0`. For
`lam > 0` both `1 - e^{-j lam}` and `1 - e^{-lam}` are positive; for
`lam < 0` both are negative; in both cases the signs cancel in the quotient,
so `log Z_j(lam) = psi(j lam) - psi(lam)` up to the (lam-independent)
branch constant — hence with the same second derivative. Now

```
psi'(x) = e^x/(e^x - 1) - 1 = 1/(e^x - 1) ,
psi''(x) = - e^x/(e^x - 1)^2 ,
```

so `Var(U_j^lam) = (log Z_j)''(lam) = j^2 psi''(j lam) - psi''(lam) =
e^{lam}/(e^{lam}-1)^2 - j^2 e^{j lam}/(e^{j lam}-1)^2`. Multiplying by
`lam^2` and using `x^2 e^x/(e^x-1)^2 = h(x)` with `x = lam` and `x = j lam`
gives the `h`-form; the `v`-form is the same identity since `v = 1 - h`.
At `lam = 0` the uniform variance is classical, and
`h(x) = 1 - x^2/12 + O(x^4)` gives `[h(lam) - h(j lam)]/lam^2 ->
(j^2 - 1)/12`. ∎

**Script check (E1.1, exact).** The identity was verified in exact
`Fraction` arithmetic, parametrized by rational `q = e^{-lam}` (formula side
in `E = 1/q`), over an 11-point `q`-grid covering `lam > 0`, `lam = 0`, and
`lam < 0`, for all `j <= 60`:

```
E1.1 identity: 660 (q, j) pairs compared in exact Fractions; mismatches = 0
```

*Remark.* The identity shows the plan's continuum profile is not an
approximation but an exact shift: `lam^2 Var(U_j^lam) = v(j lam) - v(lam)`.
This single fact is what makes parts (i) and (ii) elementary.

## 2. Monotonicity of `h`, and part (i)

**Lemma SL2.1.** `h` is even, `h(0) = 1`, and `h` is strictly decreasing on
`(0, infty)` with `h(x) -> 0` as `x -> infty`. Equivalently `v = 1 - h` is
strictly increasing on `[0, infty)`, `v(0) = 0`, `v -> 1`.

*Proof.* `h(x) = phi(x/2)^{-2}` where `phi(y) := sinh(y)/y =
sum_{n>=0} y^{2n}/(2n+1)!` (`phi(0) := 1`). The series has strictly
positive coefficients at every even power, so for `0 <= y_1 < y_2` every
`n >= 1` term is strictly larger at `y_2`: `phi` is strictly increasing on
`[0, infty)`, `phi(0) = 1`, `phi -> infty`. Hence `h = phi(./2)^{-2}` is
strictly decreasing from `1` to `0` on `[0, infty)`, and even because `phi`
is even. ∎

**Corollary SL2.2 (= SL2(i), strict).** For every real `lam` and `j >= 1`:
`Var(U_{j+1}^lam) > Var(U_j^lam)`.

*Proof.* `lam = 0`: `((j+1)^2 - 1)/12 > (j^2 - 1)/12`. `lam != 0`: by
Lemma SL2.0,

```
Var(U_{j+1}^lam) - Var(U_j^lam) = [ h(j lam) - h((j+1) lam) ] / lam^2
                                = [ h(|j lam|) - h(|(j+1) lam|) ] / lam^2 > 0
```

since `h` is even (second equality) and strictly decreasing on `(0, infty)`
(Lemma SL2.1) with `|j lam| < |(j+1) lam|`. ∎

**Script check (E1.2, confirmation only — the proof is above).** The plan's
NC-PL1 grid re-run: `lam in {0.01, ..., 0.89} x j <= 60`:

```
E1.2 variance-monotone-in-j violations, lam in {0.01..0.89} x j <= 60: 0
```

## 3. The master inequality (discreteness-free block bound)

**Lemma SL2.3.** For every `m >= 1` and `lam > 0`, with `w = m lam` and
`V(w) := (1/w) int_0^w v(x) dx`:

```
(a)  A := lam^2 s2 = sum_{j=1}^m [ v(j lam) - v(lam) ]        (exact) ;
(b)  A / m >= V(w) - v(lam) ;
(c)  V is strictly increasing on (0, infty), with V(w) -> 1 as w -> infty.
```

*Proof.* (a) Sum Lemma SL2.0's `v`-form over `j = 1..m` (independence gives
`s2 = sum_j Var(U_j^lam)`, the plan-§0 frame; the `j = 1` term is `0`, as
`U_1 = 0` a.s.).

(b) `v` is increasing (Lemma SL2.1), so for `x in [(j-1) lam, j lam]` we
have `v(x) <= v(j lam)`, whence `lam v(j lam) >= int_{(j-1)lam}^{j lam} v`.
Summing over `j = 1..m`: `lam sum_{j=1}^m v(j lam) >= int_0^{m lam} v =
w V(w)`, i.e. `sum_j v(j lam) >= m V(w)`. Insert into (a):
`A >= m V(w) - m v(lam)`.

(c) For `0 < w < w'`: `V(w') = (1/w')[ w V(w) + int_w^{w'} v ] >=
(1/w')[ w V(w) + (w' - w) v(w) ] >= V(w)`, using `v(w) >= V(w)` (an
increasing function dominates its own average over `[0, w]`); strictness
from strict monotonicity of `v`. `V -> 1` since `v -> 1`. ∎

**Remark (why there is no discreteness correction).** The plan budgeted an
`O(lam)` discreteness loss for the block route and an anchor workaround on
W7 (`lam` up to `0.89`). Neither is needed: in (b) the Riemann comparison
runs the *favorable* way because `j lam` is the RIGHT endpoint of its block
and `v` is increasing — the discrete sum dominates the integral exactly.
The only `lam`-dependent loss in the whole proof is the single subtracted
term `v(lam)`, which is capped per band in §4. In particular W7 is handled
uniformly, with no anchors; the plan's anchor
`Var(U_3^{0.89}) * 0.89^2 = 0.3666` is reproduced as a consistency check
only (E1.3: `0.3666`).

## 4. Rational certificates and part (ii)

**Proposition SL2.4 (certificates; exact rationals, script E2).** Define,
for the seven bands, the left endpoints `w0 in {4, 5, 6, 8, 10, 20, 40}`
and the tilt caps

```
cap(W1..W6b) = w1(band)/401 ,  i.e.  5/401, 6/401, 8/401, 10/401, 20/401, 40/401 ;
cap(W7) = 89/100 .
```

Then there are exact rationals `LBV(w0) <= V(w0)` and
`UBv(cap) >= v(cap)` with (prints floor-rounded for lower bounds,
ceil-rounded for upper bounds; exact `Fraction`s in the script):

```
band        w0  LBV(w0)   cap     UBv(cap)    floor:=LBV-UBv  c_A   margin
W1  (4,5]     4  0.287512  5/401   0.00001296  0.287499        0.28  0.007499
W2  (5,6]     5  0.381827  6/401   0.00001866  0.381808        0.35  0.031808
W3  (6,8]     6  0.462919  8/401   0.00003317  0.462885        0.42  0.042885
W4  (8,10]    8  0.584563  10/401  0.00005183  0.584512        0.52  0.064512
W5  (10,20]  10  0.665345  20/401  0.00020727  0.665138        0.60  0.065138
W6b (20,40]  20  0.832381  40/401  0.00082877  0.831552        0.70  0.131552
W7  (40,oo)  40  0.916190  89/100  0.06347403  0.852716        0.80  0.052716
```

*Construction (all safe-direction, all in `Fraction`).*
(1) *Exponential brackets.* For rational `t in (0, 1]`,
`S_N(t) := sum_{n<=N} t^n/n!` with `N = 18` satisfies
`0 < e^t - S_N(t) <= t^{N+1}/(N+1)! * 1/(1 - t/(N+2))` (geometric
domination of the Taylor tail), giving rational `lo <= e^t <= hi`
(bracket width `<= 5.74e-35` at `t = 1/8`, E2.0). Powers:
`lo^k <= e^{k/8}` for `t = 1/8`.
(2) *Node bounds.* `g(E) := E/(E-1)^2` has
`g'(E) = -(E+1)/(E-1)^3 < 0` for `E > 1`, so `g` is strictly decreasing
there. Hence at a node `a = k/8` (`k >= 1`):
`h(a) = a^2 g(e^a) <= a^2 g(lo^k)` (an over-estimate of `h`), which is then
rounded UP at 12 decimals — still an upper bound on `h(a)`, so
`v_lo(a) := 1 - (rounded bound) <= v(a)`.
(3) *Riemann sums.* Since `v` is increasing, the left-endpoint sum
lower-bounds the integral: `int_0^{w0} v >= (1/8) sum_{k=0}^{8 w0 - 1}
v(k/8) >= (1/8) sum_k v_lo(k/8) =: w0 * LBV(w0)`.
(4) *Caps.* `h(cap) >= cap^2 g(hi)` with `hi >= e^{cap}` (same
monotonicity, other direction), rounded DOWN; `UBv(cap) := 1 - (rounded
bound) >= v(cap)`.
(5) The table's `floor - c_A = margin > 0` checks are exact `Fraction`
comparisons; script E2 prints `E2.2 all seven bands PASS: True`. ∎

**Theorem SL2.5 (= SL2(ii)).** For every `m >= 401` and every
`lam in B(m)` (`0 < lam <= 0.89`, `w = m lam > 4`), with `w` in band `Wi`:

```
A = lam^2 s2 >= c_A(Wi) m ,     c_A = 0.28 / 0.35 / 0.42 / 0.52 / 0.60 / 0.70 / 0.80 .
```

*Proof.* Fix the band `Wi` containing `w`, with left endpoint `w0(i)`.
*(Step 1: profile floor.)* `w > w0(i)`, so by Lemma SL2.3(c) and
Proposition SL2.4: `V(w) >= V(w0(i)) >= LBV(w0(i))`.
*(Step 2: tilt cap.)* If `Wi` is a finite band `(w0, w1]`, then
`lam = w/m <= w1/m <= w1/401 = cap(Wi)` using `m >= 401`; if `Wi = W7`,
then `lam <= 0.89 = cap(W7)` by the definition of `B(m)`. In both cases
`v(lam) <= v(cap(Wi)) <= UBv(cap(Wi))` (`v` increasing, Proposition SL2.4).
*(Step 3: assemble.)* By Lemma SL2.3(b),

```
A/m >= V(w) - v(lam) >= LBV(w0(i)) - UBv(cap(Wi)) >= c_A(Wi) ,
```

the last inequality being Proposition SL2.4's exact-rational margin column
(all seven strictly positive). The chain is uniform in `m >= 401`: the only
`m`-dependence is Step 2's `w1/m <= w1/401`, which is monotone in the safe
direction. ∎

## 5. Part (iii): corollaries

**5.1 Corollary (variance floor; SL2(iii) first clause).** On all of
`B(m)`, `m >= 401`: since `c_A(w) >= 0.28` in every band and
`lam^2 <= 0.89^2 = 0.7921`,

```
s2 = A/lam^2 >= 0.28 m / 0.7921 >= (28/100) * 401 / (7921/10000)
   = 1122800/7921 = 141.7497... >= 141 > 79 .
```

(Exact fraction from E2.3; print floor-rounded.) So CL's hypothesis
`s2 >= C_0* = 79` is implied on the whole residual band and is never
binding, as the plan asserts (its chain `141 > 126 > 79` a fortiori).

**5.2 Corollary (`A/min(m, s2)` floor; SL2(iii) second clause).** For all
`m >= 401`, `lam in B(m)`: since `min(m, s2) <= m` always,

```
A / min(m, s2) >= A / m >= c_A(w) .
```

(No case split on `s2 vs m` is needed; the plan's two-case argument is
subsumed.) **Bonus, recorded for SL5:** in fact `min(m, s2) = m` on all of
`B(m)`, `m >= 401`. Indeed on a finite band, `lam <= w1/m` gives
`s2 >= c_A m (m/w1)^2 >= 0.28 * (401/40)^2 * m = 0.28 * 100.50 * m >
28 m`; on W7, `s2 >= 0.80 m/0.7921 = (8000/7921) m = 1.009973... m > m`
(exact fraction, E2.4). Band-wise chain values at `m = 401` are quoted in
E2.5 (minimum `404.99`, attained on W7). *Caution for consumers:* the W7
margin over `m` is only `1.0%`; SL5 should rely on the displayed
`A/min(m, s2) >= c_A(w)` (robust) and may use `min(m, s2) = m` only as a
simplification, not as a load-bearing margin.

**5.3 Both tilt signs.** `h` is even, so by Lemma SL2.0
`Var(U_j^{-lam}) = Var(U_j^{lam})` for every `j` (equivalently: reflection
`i -> j-1-i` maps the `-lam`-tilted law to the `lam`-tilted one and
preserves variance). Hence `s2`, `A`, and every bound above are invariant
under `lam -> -lam`, and Theorem SL2.5 + §5.1–5.2 hold verbatim for
`|lam| in (4/m, 0.89]` — consistent with the plan's WLOG-mirror convention.

## 6. Numerical verification (scripts, outputs archived)

| # | script (`g2_scripts/campaign_20260811/wp4_SL2/`) | validates | key output (verbatim) |
|---|---|---|---|
| E1 | `sl2_e1_identity_monotone.py` | Lemma SL2.0 (exact), Cor SL2.2 grid re-check, plan anchor | `E1.1 identity: 660 (q, j) pairs compared in exact Fractions; mismatches = 0`; `E1.2 variance-monotone-in-j violations, lam in {0.01..0.89} x j <= 60: 0`; `E1.3 anchor Var(U_3^{0.89}) * 0.89^2 = 0.3666 [NC-PL1 quotes 0.3666]` |
| E2 | `sl2_e2_band_certificate.py` | Prop SL2.4 certificates (exact `Fraction`s, safe rounding), §5 arithmetic | table of §4 verbatim; `E2.2 all seven bands PASS: True`; `E2.3 crude global chain 0.28*401/0.89^2 = 1122800/7921 = 141.7497 >= 141: True`; `E2.4 W7 chain c_A(W7)/0.89^2 = 8000/7921 = 1.009973 > 1: True` |
| E3 | `sl2_e3_truth_m401.py` | truth `>=` certified floor `>=` `c_A`, per band, `m = 401` and `802`; pointwise Lemma SL2.3(b) | all 14 band rows `PASS`; spot check diffs all `>= +0.0009` |

E3's truth table at `m = 401` (float, display-grade; band grids of 201
points plus the edge `w0 + 1e-6`):

```
    band   min A/m   at w      cert.floor  c_A   truth>=floor>=c_A
    W1    0.2992   4.0000    0.287499    0.28  PASS
    W2    0.3932   5.0000    0.381808    0.35  PASS
    W3    0.4735   6.0000    0.462885    0.42  PASS
    W4    0.5934   8.0000    0.584512    0.52  PASS
    W5    0.6728   10.0000   0.665138    0.60  PASS
    W6b   0.8365   20.0000   0.831552    0.70  PASS
    W7    0.9182   40.0000   0.852716    0.80  PASS
```

and identically-shaped `PASS` rows at `m = 802` (minima `0.2988 / 0.3927 /
0.4730 / 0.5928 / 0.6722 / 0.8361 / 0.9182`).

**Two honest observations (nothing moves, both recorded for the referees):**

1. *The truth decreases in `m`.* Band infima at `m = 802` are slightly
   BELOW those at `m = 401` (e.g. W1: `0.2988 < 0.2992`), decreasing toward
   the continuum limit `V(w0)`. A pointwise measurement at `m = 401` alone
   therefore could NOT certify all `m >= 401`; the proof above is
   `m`-uniform by construction (its only `m`-dependence, the tilt cap
   `w1/m <= w1/401`, is safe-direction), and its floors `LBV - UBv` sit
   below the `m -> infty` limits by design.
2. *One plan headroom figure was a grid artifact.* NC-PL1's quoted band
   minima at `m = 401` (`0.3189/0.3932/0.4735/0.5934/0.6728/0.8365/0.9182`)
   match E3 in every band EXCEPT W1: `0.3189` is the value at the plan
   grid's first in-band point `w = 4.2` (E3 reproduces `A/m = 0.318922`
   there), while the true band-W1 infimum is the edge limit `~= 0.2992` as
   `w -> 4+` (consistent with the plan's own note `0.2992 at w = 4.0, just
   outside the open band`). So W1's true headroom over `c_A = 0.28` is
   `6.4%`, not `~14%`. The stated `c_A = 0.28` is still comfortably TRUE —
   certified floor `0.287499`, margin `0.0075` — and no other band is
   affected; but the plan's "10–14% headroom on every stated `c_A`" should
   read "6.4% on W1, 10–14% elsewhere".

## 7. Deviations from the suggested route; interface notes

**Deviations (all in the direction of a shorter, stronger proof):**

- *Part (i)*: proved via the exact closed form (Lemma SL2.0 + evenness and
  strict monotonicity of `h`), not via the memorylessness mixture or
  log-concave weight comparison. Strict inequality obtained for free; valid
  for ALL real `lam` including `lam = 0` and `lam < 0`.
- *Part (ii)*: the plan's block decomposition with left-endpoint evaluation
  and an `O(lam)` discreteness budget is replaced by the exact identity
  `lam^2 Var(U_j^lam) = v(j lam) - v(lam)` plus a right-endpoint Riemann
  comparison, which carries **no discreteness error at all** (Lemma SL2.3
  and its Remark). W7 needs no exact anchors; the anchor value `0.3666` is
  reproduced only as a consistency check (E1.3).
- The M2 rescue lemma (`Var(truncated geometric) <= Var(geometric)`) is NOT
  consumed. (It is, incidentally, an immediate corollary of Lemma SL2.0:
  for `lam > 0`, `h(lam)/lam^2 = e^{lam}/(e^{lam}-1)^2 = q/(1-q)^2 =
  Var(Geom(q))` with `q = e^{-lam}`, so `Var(U_j^lam) = Var(Geom(q)) -
  h(j lam)/lam^2 < Var(Geom(q))`, strict for every finite `j`; recorded in
  case SL1/SL3 want it from a single source.)

**Dependencies consumed:** the plan-§0 frame only (`U_j` independent,
`s2 = sum_j Var(U_j^lam)` — merged-draft Lemma 3.1 frame / tilt
convention). No other sub-lemma, no T2/g1/wp1/wp2 statement, no grid
certificate. SL2 is therefore a leaf of the wp4 dependency graph, as the
architect intended.

**For SL3 (form-level dependency `A >= c_A(w) m`):** use Theorem SL2.5
exactly as stated; the per-band worst case at `m = 401` is
`A >= c_A(band) * 401`, exactly `112.28 / 140.35 / 168.42 / 208.52 /
240.60 / 280.70 / 320.80` (the plan's SL5 `A` column is these values
nearest-rounded to one decimal; the safe-direction floors are `112.28`
etc. as listed).

**For SL5:** the three inputs it names are delivered as:
`A/min(m, s2) >= c_A(w)` (§5.2, robust form); `s2 >= 141 > 79` (§5.1);
`u := 1/A <= 1/(c_A(band) * 401)` per band (immediate from Theorem SL2.5
at `m >= 401`). Optional simplification `min(m, s2) = m` on `B(m)`
(§5.2 bonus) — flagged as thin-margin (`1.0%`) on W7; do not spend it as
headroom.

**Sharpness note:** the certificates lose `~0.010–0.011` to the step-`1/8`
left Riemann sum (e.g. `LBV(4) = 0.2875` vs `V(4) ~= 0.2977`); a finer
step would push every floor to within `~0.001` of `V(w0)`, but the stated
`c_A` values clear already and SL5's ledger consumes `c_A` as fixed
constants — nothing downstream wants tighter floors.

## 8. Status

**SL2: PROVED** (parts (i), (ii), (iii); part (i) strict; part (ii)
`m`-uniform for all `m >= 401` with exact-rational certificates;
part (iii) with the case-split-free `min(m, s2) <= m` argument and the
recorded `min(m, s2) = m` bonus). Every constant explicit; every numeric
claim from the saved, run scripts E1–E3 with outputs archived. Awaiting
the house-rule two referees.

*End of wp4_sl_SL2.md.*
