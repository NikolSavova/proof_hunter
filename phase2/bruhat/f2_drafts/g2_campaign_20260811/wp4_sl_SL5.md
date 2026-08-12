# wp4_sl_SL5 — Band arithmetic: the ledger closes; CL(79, 20, 0.89) lands

*Wave-3 prover deliverable for sub-lemma SL5 of `wp4_plan_20260811.md`.
Scope: exactly SL5(i)+(ii) of the plan — exact-rational certification of the
ledger table, the entries' monotonicity, and the assembly of the crude law
`CL(C_0* = 79, C* = 20, Lambda* = 0.89)` from SL1–SL4. SL1–SL4 are consumed
as HYPOTHESES (statements quoted verbatim from the plan; the assembler
resolves the dependency graph). One deviation from the architect's suggested
route is required and is documented honestly in §1.1: the far-entry
fallback certification via B.0(i)'s crude cap is arithmetically insufficient
at `m = 401`; it is replaced by a new one-line lemma (SL5.0, `A <= m`,
proved from the M2 rescue lemma) under which the architected conclusion —
every table row, every budget — survives unchanged. No existing file
modified. Scripts in `g2_scripts/campaign_20260811/wp4_SL5/` (both SAVED
and RUN 2026-08-11/12; outputs archived beside them and quoted verbatim
in §5).*

## 0. Standing notation, hypotheses, and citable inventory

Notation is `wp4_plan_20260811.md` §0 verbatim: `U_j^lam` (`j = 1..m`)
independent truncated-geometric factors, `P(U_j = i) = e^{-lam i}/z_j` on
`{0,...,j-1}`; `S_lam = sum_j U_j^lam`; `s2 = sigma_lam^2 = Var S_lam`;
`q := e^{-lam}`; `w := m lam`; `A := lam^2 s2`; `u := 1/A`; the mean-matched
tilt frame `mu(lam(k)) = k` (merged draft Lemma 3.1, cited-PROVED), mirror
symmetry `r(N-k) = r(k)`, `lam(N-k) = -lam(k)`, WLOG `lam > 0`; the residual
band `B(m) = { lam : 4/m < lam <= 0.89 }`, `m >= 401`; the `w`-bands
`W1 = (4,5]`, `W2 = (5,6]`, `W3 = (6,8]`, `W4 = (8,10]`, `W5 = (10,20]`,
`W6b = (20,40]`, `W7 = (40, infty)`, each intersected with `lam <= 0.89`
(they partition `w in (4, 0.89 m]` gap-free, so every interior `k` with
`lam(k) in B(m)` lies in exactly one band).

**Hypotheses (resolved by the assembler; statements = `wp4_plan_20260811.md`
verbatim).**

- **(H1) = SL1(i)+(ii)**: the banded cumulant scales
  `|kappa_3| <= R31*(W) s2/lam`, `|kappa_4| <= R42*(W) s2/lam^2` with
  ```
  band:    W1    W2    W3    W4    W5    W6b   W7
  R31*:    1.0   1.2   1.5   1.7   2.0   2.1   2.2
  R42*:    0.8   1.4   2.6   3.5   5.2   6.0   6.6
  ```
  and the core model with remainder `|R5(t)| <= C5 s2 t^5/lam^3` on
  `0 <= t <= lam/2`, `C5 = 3` for `lam <= 1/2` (all of W1..W6b at
  `m >= 401`, since there `lam <= 40/401 < 1/2`), `C5 = 8` for
  `1/2 < lam <= 0.89` (so `C5 = 8` is a valid worst case on all of W7).
- **(H2) = SL2(ii)+(iii)**: the banded floor `A = lam^2 s2 >= c_A(W) m` with
  ```
  band:  W1    W2    W3    W4    W5    W6b   W7
  c_A:   0.28  0.35  0.42  0.52  0.60  0.70  0.80
  ```
  together with SL2(iii)'s corollaries: `A/min(m, s2) >= c_A(W)` and
  `s2 >= c_A(W) m/lam^2`.
- **(H3) = SL3(ii)**: the tail ledger entries — mid piece
  `3.19 sqrt(A) e^{-A/32}`, W.6 piece `<= 0.2`, far piece
  `0.36 sqrt(A) A e^{-0.0373 m}` (all in `u`-units).
- **(H4) = SL4**: for `m >= 401`, `lam = lam(k) in B(m)`, `k` interior:
  `s2 (r(k) - 1) = 1 + theta L(W, A, m) u`, `|theta| <= 1`, with the ledger
  ```
  L(W, A, m) := R42*/2 + 0.3 (R31*)^2 + 6.4 C5/sqrt(A)
                + 3.19 sqrt(A) e^{-A/32} + 0.2 + 1.0
                + 0.36 sqrt(A) A e^{-0.0373 m} .
  ```

**Citable (established) inventory actually consumed here**: the M2 rescue
lemma (`Var(truncated geometric) <= Var(geometric)`, memorylessness mixture
— `referee_t2_maths.md` M2; STATUS_wave2 §1 lists it citable), the plan-§0
frame conventions (merged draft Lemma 3.1 + mirror), and elementary calculus.
**B.0(i) is NOT consumed** — see the deviation note §1.1. No use of
T.10(2)/T.8'' anywhere. All new numeric claims are from the two saved+run
scripts of §5; the proof-bearing arithmetic (NC-SL5-1) is exact
`fractions.Fraction` end-to-end, with every transcendental replaced by a
certified one-sided rational bound (`e^x >= P_N(x)` partial sums;
`sqrt(a) <= s` iff `s^2 >= a`).

---

## 1. Lemma SL5.0 (tilt–variance product cap `A <= m`) — PROVED, unconditional

**Lemma SL5.0.** For every `lam > 0` and every `m >= 1`,

```
A  =  lam^2 sigma_lam^2  <=  m h(lam) ,      h(lam) := (lam/2)^2 / sinh^2(lam/2) ,
```

and `h(lam) < 1` strictly; in particular `A < m` — uniformly in `lam`, with
no band hypothesis.

*Proof.* By independence `s2 = sum_{j=1}^m Var(U_j^lam)`. Fix `j` and let
`X ~ Geom(q)` on `{0, 1, 2, ...}`, `P(X = i) = (1-q) q^i`, `q = e^{-lam}`.
Conditioning on the event `{X < j}` (probability `1 - q^j`) gives exactly
`U_j^lam` (the weights `q^i` restricted to `{0,...,j-1}`), and by
memorylessness `(X | X >= j) =d j + X'` with `X' =d X`. The law of total
variance then gives

```
Var(X) = E[Var(X | 1_{X>=j})] + Var(E[X | 1_{X>=j}])
       >= (1 - q^j) Var(U_j^lam) + q^j Var(X) ,
```

whence `Var(U_j^lam) <= Var(X)` (divide by `1 - q^j > 0`; for `j = 1`,
`Var(U_1) = 0` trivially). This is precisely the M2 rescue lemma
(`referee_t2_maths.md` M2), reproved here in three lines for
self-containment. Now `Var(X) = q/(1-q)^2` (standard geometric variance),
and the exact identity

```
(1-q)^2/q = e^{lam} (1 - e^{-lam})^2 = (e^{lam/2} - e^{-lam/2})^2 = 4 sinh^2(lam/2)
```

gives `Var(X) = 1/(4 sinh^2(lam/2))`. Summing over `j`:
`s2 <= m/(4 sinh^2(lam/2))`, so `A = lam^2 s2 <= m (lam/2)^2/sinh^2(lam/2)
= m h(lam)`. Finally `sinh x > x` for `x > 0` (Taylor series, positive
terms), so `h(lam) < 1`. ∎

*Numeric consistency (measurement only, NC-SL5-2(a)):* over a 720-point
dense grid of `B(m) x {m = 401, 1000, 1581}`, `A/m <= h(lam)` holds at every
point, with `max A/(m h(lam)) = 0.9978` — the cap is used at essentially
full sharpness on the deep end of the band — and `max A/m = 0.9869 < 1`.
The closed-form `Var(U_j^lam) = q/(1-q)^2 - j^2 q^j/(1-q^j)^2` used by the
measurement script agrees with direct summation to `9.2e-26` (relative).

### 1.1 Deviation note (honest record): why SL5.0 replaces the architect's far-entry fallback

The plan's SL5(i) instructs: "the far entry needs the crude cap
`A <= 0.024 m^3` (B.0(i)) ... at `m = 401`,
`0.36 sqrt(A) A e^{-15.0} <= 0.36 * 62 * 3850 * 3.2e-7 = 0.028`". This
arithmetic does not correspond to the stated cap: `sqrt(A) = 62`,
`A = 3850` is `A <= 0.024 m^2` at `m = 401`, not `0.024 m^3`. With the cap
as stated, `A = 0.024 * 401^3 = 1547549` and the far entry evaluates to
**`221.3`** at `m = 401` (NC-SL5-2(c), verbatim in §5) — it fails the
tabulated `0.01` (and the relaxed `0.05`) by four orders; along the crude
cap the far entry first drops below `0.05` only at `m = 692`, leaving
`[401, 691]` uncovered by that route. The plan's own primary phrasing
("`<= 0.01` for `m >= 401` **given `A <= m`**") is the correct route, and
Lemma SL5.0 supplies exactly the missing `A <= m` — unconditionally, from
the M2 lemma alone. Under SL5.0 the far entry is `<= 9.23e-4` at `m = 401`
(Lemma SL5.1(iii), exact certificate), decreasing in `m`; the tabulated
entry `0.01` and every row total of the architect's table survive unchanged.
Consequence: **B.0(i) is dropped from SL5's dependency list** and the
statement of SL5(i) is corrected to quantify over `A in [c_A(W) m, m]`
(the upper end supplied by SL5.0 for every actual `(k, m)`); as literally
written ("for all `A >= c_A * m`", far entry included) the plan's clause is
false, since the far entry is increasing in `A`.

---

## 2. Lemma SL5.1 (entry monotonicity + the far-entry certificate) — PROVED, unconditional

**Lemma SL5.1.** (i) `A |-> 6.4 C5/sqrt(A)` is strictly decreasing on
`A > 0`. (ii) `A |-> 3.19 sqrt(A) e^{-A/32}` is strictly decreasing on
`A > 16`. (iii) For every `m >= 401` and every `lam in B(m)` (so
`A <= m` by Lemma SL5.0),

```
0.36 sqrt(A) A e^{-0.0373 m}  <=  F(m) := 0.36 m^{3/2} e^{-0.0373 m}
                              <=  F(401) <= 9.229e-4  <  1/100 ,
```

and `F` is strictly decreasing on `m >= 41`.

*Proof.* (i) is trivial. (ii): `d/dA log(3.19 sqrt(A) e^{-A/32})
= 1/(2A) - 1/32 < 0` iff `A > 16`. (iii): `sqrt(A) A` is increasing in `A`
and `A <= m` (SL5.0), giving the first inequality. Monotonicity of `F`:
`d/dm log F(m) = 3/(2m) - 0.0373 < 0` iff `m > 3/(2*0.0373) = 40.21...`;
the discrete ratio test is also certified exactly (NC-SL5-1 [2]):
`(F(m+1)/F(m))^2 = (1 + 1/m)^3 e^{-0.0746} <= (402/401)^3 e^{-0.0746}` for
`m >= 401`, and `(402/401)^3 = 1.007500... < 1 + 746/10000 <= e^{0.0746}`
(exact rational comparison; the last step is the two-term Taylor lower
bound `e^x >= 1 + x`). The endpoint value: `0.0373 * 401 = 149573/10000`
exactly; `e^{-149573/10000} <= 1/P_120(149573/10000) = 3.1925e-7`
(certified partial-sum bound), `sqrt(401^3) <= 8030.02` (certified:
`8030.02^2 >= 401^3 = 64481201`), so
`F(401) <= (9/25) * 8030.02 * 3.1925e-7 <= 9.229e-4` — all four numbers
from NC-SL5-1 [2], exact `Fraction` arithmetic end-to-end. ∎

*Remark (worst-case location).* By (i)+(ii), on any band `W` the `A`-dependent
entries of `L` other than the far entry are maximized over
`A in [c_A(W) m, m]` at the left endpoint `A = c_A(W) m`, and (since
`c_A(W) m` is increasing in `m` and `c_A(W)*401 > 32` for every band —
exact check NC-SL5-1 [5]) are further maximized at `m = 401`, i.e. at
`A = c_A(W)*401`. The far entry is handled separately by (iii), uniformly
by `1/100`. This is exactly the "worst case `m = 401`, `A = c_A*401`"
reduction the plan asserts, now with the far entry repaired.

---

## 3. Theorem SL5.2 (= SL5(i), corrected form: the ledger closes) — PROVED modulo (H1)–(H3)

**Theorem SL5.2.** Assume (H1), (H2), (H3) (which fix the constants
`R31*(W), R42*(W), C5, c_A(W)` and the form of `L` in (H4)). Then for every
band `W`, every `m >= 401`, and every `A in [c_A(W) m, m]`,

```
L(W, A, m)  <=  T(W)  <=  20 c_A(W)  <=  20 A / min(m, s2) ,
```

where `T(W)` is the certified row total of the table below, and the last
inequality is (H2)'s `A/min(m, s2) >= c_A(W)`. Moreover, for every actual
interior `k` with `lam(k) in B(m)` the pair `(A, m)` does lie in the stated
range: `A >= c_A(W) m` by (H2) and `A <= m` by Lemma SL5.0
(unconditionally). The certified table (every entry a rational upper bound;
every comparison exact — NC-SL5-1 [1], verbatim output in §5):

```
band      c_A   A=cA*401  k4/2  0.3R31^2  R5<=    I1u<=   I2u  slop  far<=  total<=  20c_A  margin>=
(4,5]     0.28   112.28   0.400   0.300   1.8120  1.0118  0.2  1.0   0.01   4.7338    5.6   0.8662   PASS
(5,6]     0.35   140.35   0.700   0.432   1.6207  0.4706  0.2  1.0   0.01   4.4333    7.0   2.5667   PASS
(6,8]     0.42   168.42   1.300   0.675   1.4795  0.2144  0.2  1.0   0.01   4.8789    8.4   3.5211   PASS
(8,10]    0.52   208.52   1.750   0.867   1.3297  0.0681  0.2  1.0   0.01   5.2248   10.4   5.1752   PASS
(10,20]   0.60   240.60   2.600   1.200   1.2379  0.0269  0.2  1.0   0.01   6.2748   12.0   5.7252   PASS
(20,40]   0.70   280.70   3.000   1.323   1.1460  0.0083  0.2  1.0   0.01   6.6873   14.0   7.3127   PASS
(40,inf)  0.80   320.80   3.300   1.452   2.8586  0.0025  0.2  1.0   0.01   8.8231   16.0   7.1769   PASS
```

(The architect's NC-PL4(iv) totals `4.73/4.43/4.88/5.22/6.27/6.69/8.82` are
reproduced by these certified upper bounds to display rounding; the
certification direction is one-sided everywhere.)

*Proof.* Fix `W` and `m >= 401`, and let `A in [c_A(W) m, m]`. Decompose
`L(W, A, m)` per (H4):

1. `R42*/2` and `0.3 (R31*)^2` are band constants; their exact rational
   values are columns 4–5 (e.g. `0.3 * (17/10)^2 = 867/1000` on W4).
2. `6.4 C5/sqrt(A) <= 6.4 C5/sqrt(c_A(W)*401)` by SL5.1(i) and the Remark
   (with `C5 = 3` on W1..W6b, valid there for ALL `m >= 401` since
   `lam <= 40/m <= 40/401 < 1/2`; `C5 = 8` on W7 — worst case of (H1)).
   Column `R5<=` is the certified rational bound: the least 4-decimal `r`
   with `r^2 * (c_A*401) >= (32 C5/5)^2`, an exact integer comparison.
3. `3.19 sqrt(A) e^{-A/32} <= 3.19 sqrt(c_A*401) e^{-c_A*401/32}` by
   SL5.1(ii) (applicable: `c_A*401 >= 0.28*401 = 112.28 > 32`, exact check
   NC-SL5-1 [5]). Column `I1u<=` is the certified bound
   `3.19 * sqrt_upper(c_A*401) / P_120(c_A*401/32)`, exact rationals, both
   factors one-sided in the safe direction.
4. The W.6 entry is `<= 0.2` by (H3) and the slop entry is `1.0` by (H4),
   both `m`- and `A`-free.
5. The far entry is `<= 1/100` by Lemma SL5.1(iii) (this is where
   `A <= m` enters; no other entry uses it).

Summing the five groups gives `L <= T(W)`; `T(W) <= 20 c_A(W)` is the exact
`Fraction` comparison of NC-SL5-1 [1] — all seven rows PASS, minimal margin
`0.8662` (band W1). The final inequality `20 c_A(W) <= 20 A/min(m, s2)` is
(H2)/SL2(iii) verbatim. ∎

*Consistency (measurement, not proof-bearing — NC-SL5-2(b)):* the TRUE
budget `20 A/min(m, s2)` at `m = 401`, minimized over a 160-point grid per
band, is `5.996 / 7.875 / 9.488 / 11.880 / 13.495 / 16.751 / 18.439` —
uniformly above the stated `20 c_A = 5.6 / 7.0 / 8.4 / 10.4 / 12.0 / 14.0 /
16.0`, matching the plan's NC-PL1 column (`6.378 .. 19.36` on its coarser
grid; the band-infimum refinement here is sharper and still clears).

---

## 4. Theorem SL5.3 (= SL5(ii): the crude law CL(79, 20, 0.89)) — PROVED modulo (H1)–(H4)

**Theorem SL5.3.** Assume (H1)–(H4). Then for every `m >= 401` and every
interior `k` whose mean-matching tilt satisfies `|lam(k)| in (4/m, 0.89]`:

```
s2 (r(k) - 1) = 1 + theta' * 20 / min(m, s2) ,     |theta'| <= 1 ,
```

and in particular the lower-bound form
`r(k) - 1 >= (1 - 20/min(m, s2)) / s2`. Moreover `s2 >= 1122800/7921
= 141.75 > 79` for every such `k`, so the hypothesis set of the spec
`CL(C_0* = 79, C* = 20, Lambda* = 0.89)` of `wp3_draft_a2.md` §6.1 —
`|lam| in (4/m, 0.89]` AND `s2 >= 79` — is contained in the set covered
here, and the `s2 >= 79` clause never binds. **This is CL(79, 20, 0.89)
verbatim, with `C* = 20`, for all `m >= 401`.**

*Proof.* WLOG `lam = lam(k) > 0`: for `lam(k) in [-0.89, -4/m)` apply the
result to `k' = N - k`, using `r(N-k) = r(k)`, `lam(N-k) = -lam(k)`, and the
equality of the mean-matched tilted variances at `k` and `N-k` (the plan-§0
mirror frame, merged draft Lemma 3.1's convention: tilting `S` by `-lam` is
tilting `N' - S` by `+lam` for the reflected coordinate, so `s2` is
unchanged). So let `lam in B(m)` and let `W` be the unique `w`-band
containing `w = m lam` (§0: the bands partition `(4, 0.89 m]`).

By (H4), `s2 (r(k) - 1) = 1 + theta L(W, A, m) u` with `|theta| <= 1` and
`u = 1/A`. By (H2), `A >= c_A(W) m`; by Lemma SL5.0, `A <= m`; hence
Theorem SL5.2 applies and gives `L(W, A, m) <= 20 c_A(W)`. By (H2)/SL2(iii),
`A >= c_A(W) min(m, s2)`. Chaining:

```
|theta| L u  <=  20 c_A(W) / A  <=  20 c_A(W) / (c_A(W) min(m, s2))  =  20 / min(m, s2) ,
```

so `theta' := theta L u * min(m, s2)/20` has `|theta'| <= 1` and
`s2 (r(k) - 1) = 1 + theta' * 20/min(m, s2)`. The variance floor: by
(H2)/SL2(iii), `s2 >= c_A(W) m / lam^2 >= (7/25) * 401 / (89/100)^2
= 1122800/7921 = 141.7498... > 141 > 79` (exact rational chain, NC-SL5-1
[3]; `c_A >= 0.28` is the minimum over bands, `lam <= 0.89`, `m >= 401`).
The lower-bound form follows by taking `theta' = -1` as the worst case:
`s2 (r(k)-1) >= 1 - 20/min(m, s2)`, i.e.
`r(k) - 1 >= (1 - 20/min(m, s2))/s2`. ∎

**Remark SL5.4 (refinement, recorded but not needed downstream).** Under
(H2) alone, `min(m, s2) = m` for EVERY `k` in the band and `m >= 401`: on
band `Wi` with upper edge `w_hi <= 40` (i.e. W1..W6b), `lam <= w_hi/m`, so
`s2 >= c_A(Wi) m/lam^2 >= c_A(Wi) m^3/w_hi^2 >= (c_A(Wi)/w_hi^2) 401^2 m`;
the worst ratio `c_A/w_hi^2` over W1..W6b is W6b's `0.7/1600`, giving
`s2 >= 0.7 * 401^2 m/1600 = 70.35 m > m`; on W7,
`s2 >= 0.80 m/lam^2 >= 0.80 m/0.7921 = 1.0099 m > m`. So on the residual band the error term is exactly `20/m`,
and CL could be stated with `min(m, s2) = m`; we keep the `min(m, s2)` form
because that is the spec verbatim (safe direction: the two agree here).

**Remark SL5.5 (P.8-consistency note, as instructed by the plan).** The
scope `lam <= 0.89` covers everything Theorem S's R2 row can send: for the
`c = 7/10` clause the tilt cap is `lam <= log(1 + 1/c) = log(17/7)
<= 0.8874 <= 0.89`, and for `m >= 1581` the `c = 1` clause caps at
`log 2 <= 0.6932 <= 0.89` — a subset; nothing new is needed. Both
logarithm bounds are certified by exact partial-sum comparisons
(NC-SL5-1 [4]: `P_60(0.8874) = 2.4288065 >= 17/7 = 2.4285714`;
`P_60(0.6932) = 2.0001056 >= 2`), safe direction.

---

## 5. Numeric checks (scripts in `g2_scripts/campaign_20260811/wp4_SL5/`, run 2026-08-11/12; outputs archived beside them)

| # | script | validates | arithmetic | real result |
|---|---|---|---|---|
| NC-SL5-1 | `sl5_nc1_ledger_exact.py` (out: `out_sl5_nc1.txt`) | [1] the seven ledger rows of Theorem SL5.2 (certified rational upper bounds per entry, exact comparison to `20 c_A`); [2] far-entry certificate + ratio test (SL5.1(iii)); [3] the `s2 >= 141` chain (SL5.3); [4] the P.8-consistency logarithm bounds (SL5.5); [5] domain checks `c_A*401 > 32`, `c_A <= 1` | exact `fractions.Fraction` end-to-end; transcendentals replaced by one-sided certified bounds (partial sums `P_N(x) <= e^x`; `sqrt` via exact squaring) | **all 7 rows PASS**, margins `0.8662 / 2.5667 / 3.5211 / 5.1752 / 5.7252 / 7.3127 / 7.1769`; `far(401) <= 9.228821e-04 <= 1/100` TRUE; `(402/401)^3 = 1.0075 < 1.0746` TRUE; floor `= 1122800/7921 = 141.7498 >= 141` TRUE; all three log certificates TRUE; domain checks TRUE |
| NC-SL5-2 | `sl5_nc2_consistency.py` (out: `out_sl5_nc2.txt`) | (a) SL5.0 truth on a dense grid + closed-form-Var identity; (b) true budget column per band at `m = 401` vs `20 c_A`; (c) the deviation-note honesty record (fallback cap fails; slip identified; `A <= m` route value) | mpmath dps=30, measurement only (NOT proof-bearing) | (a) `0` violations of `A/m <= h(lam)` in 720 pts, `max A/(m h) = 0.9978`, `max A/m = 0.9869 < 1`, Var identity to `9.2e-26`; (b) band minima `5.996/7.875/9.488/11.880/13.495/16.751/18.439`, all above `20 c_A` — consistent with NC-PL1's `6.378..19.36`; (c) fallback value `221.3` at `m=401`, first `<= 0.05` at `m = 692`; slip value `0.0276`; SL5.0 route `9.229e-04` |

Key verbatim excerpts (`out_sl5_nc1.txt`):

```
band        c_A  A=cA*401   k4/2 0.3R31^2    R5<=   I1u<=  I2u slop far<=  total<=  20c_A margin>=  verdict
(4,5]      0.28    112.28  0.400    0.300  1.8120  1.0118  0.2  1.0  0.01   4.7338    5.6   0.8662  PASS
(5,6]      0.35    140.35  0.700    0.432  1.6207  0.4706  0.2  1.0  0.01   4.4333    7.0   2.5667  PASS
(6,8]      0.42    168.42  1.300    0.675  1.4795  0.2144  0.2  1.0  0.01   4.8789    8.4   3.5211  PASS
(8,10]     0.52    208.52  1.750    0.867  1.3297  0.0681  0.2  1.0  0.01   5.2248   10.4   5.1752  PASS
(10,20]    0.60    240.60  2.600    1.200  1.2379  0.0269  0.2  1.0  0.01   6.2748   12.0   5.7252  PASS
(20,40]    0.70    280.70  3.000    1.323  1.1460  0.0083  0.2  1.0  0.01   6.6873   14.0   7.3127  PASS
(40,inf)   0.80    320.80  3.300    1.452  2.8586  0.0025  0.2  1.0  0.01   8.8231   16.0   7.1769  PASS
all 7 rows PASS (exact Fraction comparison): True
  far(401) <= (9/25)*8030.02*e^-14.9573 <= 9.228821e-04  <= 1/100 : True
  ratio test: (402/401)^3 = 1.007500 < 1 + 746/10000 = 1.0746 : True
  = 1122800/7921 = 141.7498 ;  >= 141: True ;  > 126: True ;  > 79: True
  e^0.8874 >= 17/7 (i.e. log(17/7) <= 0.8874):  P_60 = 2.4288065 >= 2.4285714 : True
```

and (`out_sl5_nc2.txt`):

```
    violations of A/m <= h(lam): 0 / 720 pts ; max A/(m h(lam)) = 0.9978 ; max A/m = 0.9869 < 1
    (4,5]     min 20A/min(m,s2) =   5.996  vs 20c_A =   5.6   consistent
    (40,inf)  min 20A/min(m,s2) =  18.439  vs 20c_A =  16.0   consistent
    with A = 0.024 m^3 (B.0(i) fallback): 0.36 sqrt(A) A e^-0.0373m = 221.3  (FAILS 0.05)
    fallback route first reaches <= 0.05 at m = 692 (gap [401, 691] uncovered by it)
    with A <= m (Lemma SL5.0):            value = 9.229e-04  (<= 0.01 with 10x room)
```

---

## 6. Status, dependencies, honest markers

**Status of the results in this file.**

- **Lemma SL5.0** (`A <= m h(lam) < m`): **PROVED, unconditional** (three-line
  self-contained proof; the mixture step is the citable M2 rescue lemma,
  reproved inline). New to the campaign; independently useful wherever a
  crude `A`-cap is needed (it retires B.0(i) from this package).
- **Lemma SL5.1** (entry monotonicity; far entry `<= 1/100` uniformly on
  `m >= 401`): **PROVED, unconditional** (elementary calculus + exact
  certificates NC-SL5-1 [2]).
- **Theorem SL5.2** (= SL5(i), corrected quantification `A in [c_A m, m]`):
  **PROVED modulo (H1)–(H3)** — given the constants of SL1(i)/(ii),
  SL2(ii)/(iii) and SL3(ii), the ledger inequality
  `L <= T(W) <= 20 c_A(W) <= 20 A/min(m, s2)` is certified in exact
  rationals, all seven bands, worst margin `0.8662` on W1.
- **Theorem SL5.3** (= SL5(ii)): **PROVED modulo (H1)–(H4)** — i.e. modulo
  SL1–SL4 exactly as the plan's dependency graph specifies. Conclusion:
  **`CL(79, 20, 0.89)` verbatim for all `m >= 401`**, two-sided form with
  `C* = 20`, plus the lower-bound form, plus `s2 >= 141.7498 > 79`
  (hypothesis clause never binds), mirror included.

**Corrections to the architected statement (both conclusion-preserving,
neither optional):**

1. The far-entry certification route "crude cap `A <= 0.024 m^3` from
   B.0(i)" is FALSE as arithmetic at `m = 401` (entry value `221.3`, not
   `0.028`; the printed numbers trace to `0.024 m^2`, a slip; that route
   certifies `<= 0.05` only from `m = 692`). Replaced by Lemma SL5.0
   (`A <= m`), which certifies the tabulated `0.01` for all `m >= 401`
   with 10x room. §1.1 has the full record.
2. SL5(i)'s clause "for all `A >= c_A * m` ... each `L`-entry is
   nonincreasing in `A`" is false for the far entry (increasing in `A`);
   the corrected statement quantifies over `A in [c_A(W) m, m]` and
   handles the far entry by the uniform SL5.1(iii) cap. Every actual
   `(k, m)` pair lies in the corrected range (lower end (H2), upper end
   SL5.0), so nothing downstream changes.

**What SL5 hands the assembler.** If SL1, SL2, SL3, SL4 land as stated in
`wp4_plan_20260811.md`, then by Theorem SL5.3 the single remaining open
condition of `wp3_draft_a2.md` Theorem S (its R2 row) is met, in the exact
form Theorem S names: `CL(79, 20, 0.89)`, lower-bound form included. The
only inputs of this file beyond (H1)–(H4) are: the M2 rescue lemma
(citable, and reproved inline), the plan-§0 frame (merged draft Lemma 3.1 +
mirror, cited-PROVED), and exact arithmetic (NC-SL5-1). No grid
certificates, no floats in the proof-bearing chain, no use of
T.10(2)/T.8'', no reading of any other prover's wp4 file.

*End of wp4_sl_SL5.md.*
