# wave4_sl3p_ROUTE — SL3' mid-exponent upgrade: route selection + validated lemma chain (Stage 1 of 2)

*Wave-4 ROUTE-FINDER deliverable, F2 campaign, 2026-08-12. Assignment: find
and numerically validate a route to the bridge piece SL3' of
`wp4_draft_composite.md` §5.3 — the banded mid-exponent upgrade
`gamma* = 0.42/0.42/0.40/0.40/0.38/0.34/0.32` (W1..W7) on the mid interval,
replacing Theorem A3(i)'s proven `c1 = 0.1317`. This file states the chosen
route, the full lemma chain (each statement explicit), the numeric evidence
per step, and the constants remaining for the Stage-2 prover. Scripts:
`g2_scripts/campaign_20260811/wave4_sl3p/sl3p_nc1_identity_master.py`,
`sl3p_nc2_continuum.py`, `sl3p_nc3_split.py` — all SAVED and RUN 2026-08-12,
outputs archived beside them (`out_sl3p_nc1/2/3.txt`), quoted verbatim in §5.
No existing file modified. Blind protocol: no other wave-4 bridge draft read.*

**Bottom line: ROUTE FOUND AND VALIDATED — the exact log-modulus product
identity (Lemma E.1), not a repair of the truncation route.** Along the
chain below, Lemmas E.1, E.2, E.3 are PROVED in this file (short, complete
proofs); E.4 is a standard bounded-variation discretization step with two
named constants to chase; E.5 and E.6 are finite certificates of the
SL3.A-class (CONJECTURED, numerics verified here at every band edge and
worst measured point, margins 5.9%–23%). SL3' itself therefore remains
CONJECTURED, but with a complete, explicitly constant-budgeted proof plan
whose every numeric gate PASSes with headroom, worst case `gamma_ach/gamma*
= 1.0592` (W5, `w = 20`, `m = 401`, `tau = 0.8`).

## 1. Route decision (including a decisive negative)

**1.1 The ledger's candidate (i) — "keep the sin^2 mass beyond the first
truncation point" — is structurally DEAD and must not be pursued.** The
A3 route bounds `E sin^2(tD/2) >= (t^2/pi^2) E[D^2; |D| <= pi/t]` via the
chord bound `sin u >= (2/pi) u` on `|u| <= pi/2`. That linearization caps
the extractable Gaussian constant at

```
c <= (2/pi^2) * (1 - eps) <= 2/pi^2 = 0.202642    even at eps = 0 ,
```

which is below EVERY SL3' target (min `gamma* = 0.32`, max `0.42`). So no
improvement of the per-factor tail loss `eps: 0.35 -> 0.10` inside that
route can reach any band target: the loss that must go is the
`(2/pi)`-chord itself, not the truncation mass. (Verbatim: NC2 §D
`dead-route cap: 2/pi^2 = 0.202642 < 0.32 = min gamma*`.)

**1.2 The chosen route (realizing candidate (ii) exactly).** The factor
product need not be estimated at all: the truncated-geometric cf has a
closed form, and taking `-2 log| . |` of the product gives an EXACT
identity (Lemma E.1) expressing `-2 log|phi|` as a main term minus an
explicit, nonnegative, exponentially decaying correction sum — the
cf-level lift of SL2's exact variance identity
`lam^2 Var(U_j) = h(lam) - h(j lam)` (Theorem A2's mechanism, two-referee
citable via the composite). The "per-factor loss" of the old route
disappears; what remains is a clean comparison between two explicit sums,
which reduces (Lemma E.2) to a one-dimensional master inequality for the
function `F(x) = g_tau(x) - 2 gamma tau^2 h(x)`. All analysis then lives
on explicit elementary functions; no characteristic-function estimate of
any kind survives into Stage 2.

## 2. Lemma E.1 (exact log-modulus identity) — PROVED

Notation as composite §0: `q = e^{-lam}`, `U_j` truncated geometric on
`{0..j-1}`, `phi(t) = prod_{j=1}^m nu_j(t)`, `h(x) = (x/2)^2/sinh^2(x/2)`.
Define, for `x != 0`, real `y`:

```
g(x, y) := log( 1 + sin^2(y/2) / sinh^2(x/2) ) .
```

**Lemma E.1.** For every `m >= 1`, real `lam != 0` and real `t`:

```
-2 log|phi_lam(t)| = sum_{j=1}^m [ g(lam, t) - g(j lam, j t) ]
                   = m g(lam, t) - sum_{j=1}^m g(j lam, j t) .
```

*Proof.* `nu_j(t) = c_j sum_{i=0}^{j-1} (q e^{it})^i
= [(1-q)/(1-q^j)] (1 - (q e^{it})^j)/(1 - q e^{it})` (finite geometric
series; `q e^{it} != 1` since `0 < q < 1`). For any `r in (0,1)`:
`|1 - r e^{is}|^2 = (1-r)^2 + 4 r sin^2(s/2)`, and
`4r/(1-r)^2 = 1/sinh^2((log(1/r))/2)`. Applying this with `r = q^j,
s = jt` (numerator) and `r = q, s = t` (denominator):

```
|nu_j(t)|^2 = [1 + sin^2(jt/2)/sinh^2(j lam/2)] / [1 + sin^2(t/2)/sinh^2(lam/2)] ,
```

so `-2 log|nu_j(t)| = g(lam, t) - g(j lam, j t)`; sum over `j` (the `j = 1`
term is identically 0). For `lam < 0` both `g`-arguments are even in the
first slot. ∎

*Consistency checks (both PROVED elsewhere, both reproduced by E.1):* the
`t^2`-coefficient of E.1 at `t -> 0` is `sum_j [1/(4 sinh^2(lam/2)) -
j^2/(4 sinh^2(j lam/2))] = s2`, i.e. SL2's exact identity; dropping the
(nonnegative) correction sum gives `-2 log|phi| <= m g(lam,t)`, whose
`t^2`-shadow is Lemma C.1's `s2 <= m/(4 sinh^2(lam/2))`. *Numeric check
(NC1 §a, independent O(m^2) termwise summation of every factor's series,
dps 25): rel. err `<= 1.1e-23` at all four probe points, e.g. `m=401
w=4.05 tau=0.8: -2log|phi| = 76.8524292638 identity = 76.8524292638`.*

## 3. Lemma E.2 (reduction to the master inequality) — PROVED

Fix a band `W` with target `gamma* = gamma*(W)`, and `tau := t/lam in
(0, 4/5]`. Define

```
F(x) = F_{tau,gamma*}(x) := g(x, tau x) - 2 gamma* tau^2 h(x)  (x > 0) ,
F(0) := F(0+) = log(1 + tau^2) - 2 gamma* tau^2 .
```

**Lemma E.2.** For `m >= 1`, `lam != 0`, `t = tau lam`:

```
-2 log|phi_lam(t)| - 2 gamma* s2 t^2 = sum_{j=1}^m [ F(lam) - F(j lam) ] .
```

Hence the SL3' band statement `|phi_lam(t)| <= exp(-gamma*(W) s2 t^2)` for
all `t in (0, 0.8 lam]` is EQUIVALENT to the

**Master inequality M(W):** `sum_{j=1}^m [ F(lam) - F(j lam) ] >= 0`
for all `m >= 401`, `lam = w/m` with `w in W`, `lam <= 0.89`,
`tau in (0, 4/5]`.

*Proof.* `s2 t^2 = tau^2 lam^2 s2 = tau^2 sum_j [h(lam) - h(j lam)]`
(SL2's identity, cited via the composite; equivalently E.1's own
`t^2`-coefficient), and E.1 gives the `g`-part; subtract term by term. ∎

*(Scope notes: the SL4'-consumer needs only `t in [lam/2, 0.8 lam]`; the
route delivers all of `(0, 0.8 lam]` — the small-`tau` end is the easy
direction, see E.5/E.6 numerics. The `j = 1` summand vanishes.)*

## 4. The remaining chain: E.3–E.7 (statements, status, evidence)

**Lemma E.3 (arch monotonicity) — PROVED.** For `tau in (0, 1)`, the
function `psi_tau(x) := sin^2(tau x/2)/sinh^2(x/2)` is strictly decreasing
on `(0, 2 pi/tau)`; hence so is `g(x, tau x) = log(1 + psi_tau(x))`.

*Proof.* On `(0, 2pi/tau)`, `tau x/2 in (0, pi)` so `sin(tau x/2) > 0` and
`(log psi)'(x) = tau cot(tau x/2) - coth(x/2)`. If `tau x/2 >= pi/2` then
`cot <= 0 < coth`, done. If `tau x/2 < pi/2`, multiply by `x/2 > 0`: the
claim is `(tau x/2) cot(tau x/2) < (x/2) coth(x/2)`, and `u cot u <= 1`
on `(0, pi/2)` (from `tan u >= u`) while `v coth v >= 1` (from
`tanh v <= v`), with joint equality only in the limit `x -> 0`. ∎

*(Beyond `2 pi/tau`, `g` oscillates in arches under the strictly
decreasing envelope `genv(x) = log(1 + 1/sinh^2(x/2))`; NC2 §C confirms
the first-arch monotonicity on grids: max consecutive increment
`<= -3.1e-8`, all `tau`.)*

**Step E.4 (discretization, small-lam regime) — STANDARD, two constants to
chase.** For `F` of bounded variation on `[0, w]` (guaranteed by E.3 +
envelope + `h` monotone):

```
(a)  sum_{j=1}^m F(j lam) <= (1/lam) Int_0^w F(x) dx + V_[0,w](F)      [right-Riemann/BV]
(b)  F(lam) >= F(0+) - K1' tau^2 lam^2       for 0 < lam <= 0.3 ,
```

with `V_[0,w](F) <= V' tau^2` and `K1'` `tau`-uniform. Measured at
`tau = 0.8` (NC2 §D): `V_[0,60](F) <= 0.1901` (i.e. `V'/tau^2`-normalized
`0.297`) worst band `gamma = 0.32`; `K1 = 0.01920 = tau^2(1-2 gamma)/12`
exactly to leading order (`gamma = 0.32`), `0.00853` at `gamma = 0.42`.
*Proposed Stage-2 constants: `V' = 0.5`, `K1' = 0.05` (2x-safe over
measured; both provable in closed form — `V(2 gamma* tau^2 h) =
2 gamma* tau^2` exactly, `V(g)` = first-arch drop + geometric arch-sum
via `genv`).*

**Certificate E.5 (continuum band functional) — CONJECTURED, numerics
verified.** Define, for `w > 4`, `tau in (0, 4/5]`:

```
G(w, tau) := [ log(1+tau^2) - (1/w) Int_0^w g(x, tau x) dx ]
             / ( 2 tau^2 [ 1 - (1/w) Int_0^w h(x) dx ] ) .
```

*Claim:* `min over (w in W, tau in (0, 4/5]) of G(w, tau) >= gamma*(W) +
margin(W)`, with the per-band minima (all attained at the TOP `w`-edge and
`tau = 0.8`; NC2 §A, dps 20, quad cross-checked by
`Int_0^inf h = pi^2/3` to `2.1e-21`):

```
band  gamma*  G_min      at (w, tau)    ratio    delta* (F-units, tau=0.8)
W1    0.42    0.479524   (5, 0.8)       1.1417   +0.02988
W2    0.42    0.464896   (6, 0.8)       1.1069   +0.02715
W3    0.40    0.440953   (8, 0.8)       1.1024   +0.03104
W4    0.40    0.426155   (10, 0.8)      1.0654   +0.02248
W5    0.38    0.402547   (20, 0.8)      1.0593   +0.02411
W6b   0.34    0.393795   (40, 0.8)      1.1582   +0.06319
W7    0.32    0.386535   (5000, 0.8)    1.2079   +0.08511   [w->inf limit 0.38648144]
```

`delta*(W) = 2 tau^2 (1 - avg_h)(G - gamma*)` is exactly the
per-`(1/m)`-share the master inequality needs. Stage-2 certification plan
(SL3.A-class, no continuum grid-sampling): 2-D monotone-cell partition in
`(w, tau)` using (i) `avg_g(w)` and `avg_h(w)` decreasing in `w` for
`w >= 4` (provable: `d/dw avg_f = (f(w) - avg_f)/w < 0` once `f(w)` is
below its running average — exponential decay), so cell-wise
`G >= [log(1+tau_1^2) - avg_g(w_1, tau_2-bound)] / (2 tau_2^2 (1 -
avg_h(w_2)))`; (ii) `tau`-cell bounds on `avg_g` via `g <= g(., tau_2 .)`
on `x <= pi/tau_2` plus the `genv` envelope beyond; (iii) W7's unbounded
`w`-tail by the same avg-monotonicity (both averages `-> 0`, `G ->
log(1+tau^2)/(2 tau^2) >= 0.38648 at tau = 0.8`). Two structural facts to
exploit, both observed on every scanned cell: `G` decreasing in `tau` and
decreasing in `w` inside each band (argmin always top edge, `tau = 0.8`).

**Certificate E.6 (large-lam per-j domination; W7 only) — CONJECTURED,
numerics verified.** For `gamma = 0.32`, `lam in [0.30, 0.89]`,
`tau in (0, 4/5]`: `F(x) <= F(lam)` for ALL `x >= 2 lam`. Then `M(W7)`
holds term by term — no discretization, any `m`. Numerics (NC2 §B + NC3):
grid min of `[F(lam) - F(x)]` is `+0.001387` (at `lam = 0.25`; the split
point is `0.30` where the min is larger), high-precision recheck
`+0.00138689418`; the correct `tau`-uniform invariant
`[F(lam) - F(x)]/tau^2` has grid min `+0.007921` (`lam >= 0.30`, `tau
in {0.10..0.80}`, at `lam = 0.30, tau = 0.10, x = 0.60`), matching the
analytic small-`tau` limit `(1 - 2 gamma)[h(lam) - h(2 lam)] = +0.007920`
— so the small-`tau` end reduces analytically to `h` strictly decreasing,
and only `tau in [tau_low, 0.8]` needs a finite certificate. The `x > 60`
tail needs one throwaway constant (`|F(x)| <= (1 + x^2) e^{-x}`-class vs
`F(lam) >= tau^2 (1-2 gamma) h(0.89) (1 - corr) > 0`).

**Assembly E.7 (Theorem SL3', conditional proof) — arithmetic validated.**
Given E.3–E.6, `M(W)` holds for every band: *small-lam regime* (all of
W1–W6b, where `lam <= 40/401 < 0.0998`; and W7 with `lam <= lam_split =
0.30`): by E.4(a,b) + E.5,

```
sum_j [F(lam) - F(j lam)] >= m [ delta(w,tau) - K1' tau^2 lam^2 ] - V' tau^2 ,
```

which is positive since `delta/tau^2 >= delta*/(tau^2) >= 0.0351` (W4,
the band minimum in normalized units) vs `K1' lam^2 + V'/m <= 0.05 *
0.0998^2 + 0.5/401 = 0.00175` — 20x headroom at the proposed (2x-safe)
Stage-2 constants; the measured-constant version is 33–99x (NC3: W7 split
budget `0.08511 vs 0.00220`, headroom 39x). *Large-lam regime* (W7,
`lam in [0.30, 0.89]`): E.6 termwise. Then Lemma E.2 converts `M(W)` to:

**Theorem SL3' (target statement).** *For `m >= 401`, `|lam| in B(m)`,
`w = m|lam| in W`, and all `0 < t <= 0.8 |lam|`:*

```
|phi_lam(t)| <= exp( - gamma*(W) s2 t^2 ) ,
gamma* = 0.42/0.42/0.40/0.40/0.38/0.34/0.32   (W1..W7) .
```

*Consumer impact (why this closes the §5.2 refutation's mid gap; NC3,
verbatim): the honest kernel-weighted mid' slot at W1 (`A0 = 112.28`,
`mid' = sqrt(2/pi) A^{3/2} e^{-gamma A/4}(1 + 2/(gamma A))/(2 gamma)`) is
`W1 ... gamma=0.1317: exp(...)=e^-3.70 ... mid' = 101.5` (the referee's
REF-C C7 figure `101.41`; `129.86` at the orphan's `gamma = 1/8`) versus
`gamma=0.4200: exp(...)=e^-11.79=7.585e-06  mid' = 0.008935` — four
orders under the W1 budget; higher bands land `2.7e-6` (W4) down to
`5.2e-8` (W7). The crossover tier (`c2`, to `1.074 lam`) is NOT touched
by SL3'; A3's Theorem SL3.1 remains the citation for it.*

## 5. Numeric evidence (scripts SAVED+RUN; key output verbatim)

All in `g2_scripts/campaign_20260811/wave4_sl3p/`; outputs archived as
`out_sl3p_nc1.txt`, `out_sl3p_nc2.txt`, `out_sl3p_nc3.txt`.

**NC1 = `sl3p_nc1_identity_master.py` (mpmath dps 25).** (a) E.1 vs an
independent O(m^2) computational path (termwise summation of every
factor's finite series): rel. err `5.4e-24 / 1.1e-23 / 0.0 / 3.9e-25` at
the four probes. (b) finite-m `gamma_ach(m, w, tau) = sum DG_j / (2 tau^2
sum DH_j)` — the exact achieved mid-exponent, `min over tau in {0.3, 0.5,
0.65, 0.75, 0.8}` — at every band edge, the worst measured points of the
prior campaign, and `m in {401, 2000, 20000}` (28 points, ALL PASS):

```
401    4.05     W1    0.42 | 0.492265   0.8  | 1.1721 | +1.73778  PASS
401    5.0      W1    0.42 | 0.479432   0.8  | 1.1415 | +2.19920  PASS
401    10.0     W4     0.4 | 0.426079   0.8  | 1.0652 | +4.28886  PASS
401    20.0     W5    0.38 | 0.402499   0.8  | 1.0592 | +6.20135  PASS
401    40.0     W6b   0.34 | 0.393689   0.8  | 1.1579 | +9.31421  PASS
401    356.89   W7    0.32 | 0.379407   0.8  | 1.1856 | +10.55580  PASS
20000  20.0     W5    0.38 | 0.402547   0.8  | 1.0593 | +308.94921  PASS
worst ratio gamma_min/gamma* over all points: 1.0592 at m=401 w=20.0 (W5)
```

Cross-validation: the `m = 401` values reproduce NC-SL3-2's measured tier-1
truths exactly (`0.4923` at `w = 4.05`, `0.3794` at `w = 356.89`) — an
independent confirmation of E.1 against the prior campaign's direct-cf
measurements. Slack column = master-inequality LHS at `gamma*` (nats,
worst `tau`); positivity is exactly `M(W)` at that point.

**NC2 = `sl3p_nc2_continuum.py` (dps 20 + labeled float scans).** §A: the
E.5 table of §4 (`check: Int_0^inf h = 3.289868134 vs pi^2/3 ... rel err
2.1e-21`). §B: E.6 grid `min [F(lam)-F(x)] = +0.001387 ... PASS`,
recheck dps 30 `+0.00138689418`. §C: E.3 grids PASS. §D: `V_[0,60](F)`
`0.1450–0.1901`; `K1` `0.00853 / 0.01920` = leading order exactly;
`dead-route cap: 2/pi^2 = 0.202642 < 0.32`.

**NC3 = `sl3p_nc3_split.py` (floats, labeled).** Normalized E.6 slack
`+0.007921` (`lam >= 0.30`) vs analytic small-`tau` limit `+0.007920`;
W7 split budget `delta* = 0.08511 vs K1*lam_split^2 + V/401 = 0.00220`
(headroom 39x) at `lam_split = 0.30`; the consumer-impact mid' table of
§4 (E.7), incl. the `101.5`-vs-`0.008935` W1 comparison.

## 6. Exactly what remains to be chased (Stage-2 prover's list)

1. **`V'` and `K1'`** (E.4): closed-form, `tau`-uniform certified values;
   proposed `V' = 0.5`, `K1' = 0.05` (measured `0.297`, `0.030` in
   normalized units at the worst band). Route: `V(2 gamma tau^2 h) =
   2 gamma tau^2` exact; `V(g)` = `g(0+) `-drop on the first arch (E.3)
   plus a geometric arch-sum under `genv(x) = log(1 + 1/sinh^2(x/2))`;
   `K1'` by one Taylor-with-remainder estimate of `F` at `0` valid on
   `lam <= 0.3`.
2. **E.5 certificate**: the two avg-monotonicity lemmas (`d/dw avg_f < 0`
   for `w >= 4`), the `tau`-cell bound for `avg_g`, and the finite
   monotone-cell table certifying `G >= gamma* + margin` per band
   (measured margins: 6.5% W4, 5.9% W5 — the two thin bands — 10-23%
   elsewhere; cells must be fine enough near the top edges of W4/W5).
   W7 `w`-tail via the same monotonicity; `tau`-edge at exactly `4/5`.
3. **E.6 certificate**: finite cell table on `(lam, tau, x) in [0.30,
   0.89] x [tau_low, 0.8] x [2 lam, 60]`; the analytic small-`tau`
   reduction (`tau <= tau_low`, via `h` strictly decreasing) with its
   crossover constant `tau_low` (suggest `0.2`; normalized slack floor
   measured `+0.0079`); one `x > 60` tail constant.
4. **`lam_split = 0.30`** (W7 regime split) — fixed here, both sides
   validated with `>= 30x` budget headroom; Stage 2 only re-certifies.
5. **Scope decision**: the chain proves `t in (0, 0.8 lam]` (superset of
   the consumed `[lam/2, 0.8 lam]`); keep the larger scope iff the E.5/E.6
   `tau`-certificates cover `tau -> 0` analytically (they do — item 1/3);
   otherwise state `tau in [1/2, 4/5]` and re-run nothing.
6. **Risk register** (honest): the two ~6% bands (W4, W5) are real but
   grid-independent (continuum minima at interior-free top edges, matching
   finite-m to 5e-5 by `m = 2000`); the identity route has NO other thin
   margin — every remaining constant enters linearly against 20x+
   headroom. If Stage 2 finds the E.5 cell table unwieldy near `(20, 0.8)`,
   the fallback is `gamma*(W5) = 0.37` — still 8.8x the `e^{-gamma A/4}`
   decade-gain over `c1` at `A0 = 240.6` — but NO ledger row is known to
   need it; do not spend without checking SL4' first.

**Status recap: SL3' = CONJECTURED (unchanged), with route RESOLVED:
E.1/E.2/E.3 PROVED here; E.4 standard modulo two constants; E.5/E.6
finite certificates fully specified and numerically validated at all band
edges, worst measured points, and `m in {401, 2000, 20000}` (28/28 PASS,
worst margin 5.9%). The truncation-repair route is refuted (hard cap
`2/pi^2 < 0.32`) and closed. Stage 2 = items 1–4 above; no new
mathematics beyond finite certificates and two closed-form constants.**

*End of wave4_sl3p_ROUTE_20260812.md.*
