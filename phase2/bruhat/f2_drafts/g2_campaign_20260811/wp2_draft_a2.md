# wp2-a2 — the kernel-transfer + denominator bucket Delta_ker, with explicit constants, and the merged closed-form T.9

*Work package wp2-a2 (wave 2, 2026-08-11): the never-landed wp2-a of the
campaign plan — the one missing piece of T2 §8 item 4 (STATUS.md §5.1) — plus
the merge of Theorem W.7 + Delta_ker + wp1-c's W.4(i) into a closed-form
Theorem T.9-final.*

*Provenance and reading note. Written after (in order): STATUS.md,
`F2_PROOF_DRAFT.md`, `g1_draft_b.md` (refereed; B.0–B.9 citable),
`g2_draft_t2_20260803.md` (T2), `wp1_draft_c.md` + `wp2_draft_b.md` (wave 1,
both double-refereed MINOR_REPAIRS) and all four of their referee reports,
`g2_item4_bucket_notes_20260805.md`, and the wave-2 files that postdate
STATUS.md: `referee_t2_maths.md` (the T2 maths referee HAS now run:
MINOR_REPAIRS; T.9'' confirmed sound — the T2 PROVED inventory this draft
consumes is on two-referee footing), `repairs_20260811.md` (wave-1 repair
lists §2a/§2b/§3 all applied as errata + fixed script copies), and
`harness_m200_20260811.md` (exact harness extended to m = 400).
`g2_draft_t1_20260803.md` was NOT read (kept blind). No existing file was
modified (no-erasing rule).*

*Inherited-scripts disclosure. On starting, the script directory
`g2_scripts/campaign_20260811/wp2_a2/` already contained three files
(`wp2a2_lib.py`, `wp2a2_nc1_model_err.py`, `wp2a2_nc2_buckets.py`, timestamps
2026-08-11 18:14–18:17) from an earlier wave-2 session on this same package
that died before writing any draft (no `wp2_draft_a2*.md` existed). Per the
no-erasing rule they were left untouched; I audited every line against my own
independent derivation (§2–§6 record the mathematics they implement), ran
them myself, and quote only outputs of my own runs. Their crude first-pass
bound is kept as a comparison (NC-A2, §6); the refined construction and the
merge (`wp2a2_lib2.py`, `wp2a2_nc3_refined.py`, `wp2a2_nc4_truth.py`,
`wp2a2_nc5_merge.py`) are new files written this session. NC-A2's FAIL
verdict is a real, reported finding about the crude route (§6), not an
error.*

*Scripts (all under `g2_scripts/campaign_20260811/wp2_a2/`, each RUN
2026-08-11/12, CPython 3, stdlib + mpmath; verbatim outputs in §8):
`wp2a2_nc1_model_err.py` (NC-A1), `wp2a2_nc2_buckets.py` (NC-A2),
`wp2a2_nc3_refined.py` (NC-A3), `wp2a2_nc4_truth.py` (NC-A4),
`wp2a2_nc5_merge.py` (NC-A5).*

---

## 0. What this package delivers, and its honest status

Theorem W.7 (wp2-b) left `T.9 = Prop 3.5(ii)` as an EXACT decomposition with
one pending term: with `u := r(k) - 1`, `v := F(0) - 1` (the 6-term-model
ratio at the tilted mean),

```
Delta_ker(k) := s2 [ log(1+u) - log(1+v) ]
```

— everything that changes when the true tilted pmf values `P_0, P_{+-1}` are
replaced by the model values `phat(0), phat(+-1)`. This draft:

1. **Bounds `Delta_ker` in closed form** (Theorem D.5): for `K in {1, 2, 4}`
   and `m >= M(K) = 180 / 181 / 367`, every interior `k` with
   `0 < |lam(k)| <= K/m` has
   ```
   |Delta_ker(k)| <= C_ker(K) / m^2 ,
   C_ker(1) = 30.89 ,  C_ker(2) = 209.03 ,  C_ker(4) = 37811 ,
   ```
   with `C_ker(K, m)` explicit, certified DECREASING in `m` on the stated
   range (unit-step to 3000, spot-checked to 10^4), assembled from: a
   kernel box bucket (the B.6 analogue for the 6-term tilted model, with the
   two odd rows handled by a real-part split — item 2 below), the far bucket
   via wp1-c's W.4(i) exponents `c_1(K) = 0.2259 / 0.1802 / 0.1019`, a model
   tail bucket, and a denominator bucket. Truth anchor (wp2-b NC-W4(6),
   referee re-verified; independently reproduced here, NC-A4): true size
   `~1.39 / 4.07 / 5.04` — the proved constants sit 22x / 51x / 7502x above
   (see §9 for where the slack lives; the K = 4 inflation is the same
   triangle-inequality phenomenon as wp2-b's `PW_closed(4) = 187` vs 4.9).

2. **Finds and fixes the odd-cube bucket-placement trap** (§6): the naive
   modulus route (first pass, NC-A2) keeps the exponential-Taylor remainder's
   `|z|^3/6 ~ alpha^3 t^9/6` row, which enters the kernel bucket at order
   `K^3 m^{-3/2}` — NOT `O(m^{-2})` — making the assembled "constant"
   grow like `sqrt(m)` (NC-A2 verdict FAIL on monotonicity, kept as the
   record). But `D`, `P_{+-1}`, `phat` are all REAL, and the `alpha^3` term
   is purely imaginary at leading order: tracking real and imaginary parts
   separately (Lemma D.1'/D.3') the surviving real contributions are
   `alpha^4`-class, order restored to `O(m^{-2})` with every row decaying.
   This is the bucket-level realization of the odd-cancellation that T2 §4
   Step 3 (b1) proved at the mean, and the tilted-frame sibling of the
   item-4 notes' bare `-36 a^2` finding.

3. **Performs the merge** (Theorem T.9-final, §7): W.7 + Theorem D.5 +
   wp1-c W.4(i) give, for `m >= M(K)` and `0 < |lam(k)| <= K/m`,
   ```
   s2 log r(k)  = 1 - B_m (1 + theta_1 c_w(K) w^2) + theta_2 C_R(K)/m^2 ,
   s2 (r(k)-1)  = same + theta_3 Lin(K, m)   [m^2 Lin = 0.2308/0.2571/0.3719 at 180] ,
   |theta_i| <= 1 ,   c_w = (0.407, 0.466, 1) ,
   C_R(K) = PW + T + C_ker = 41.17 / 230.09 / 37998   (closed flavor, all m >= M(K))
          = 32.44 / 213.12 / 37815                     (PW-grid flavor, m <= 2000) ,
   ```
   with Lemma W.5's conditionality DISCHARGED (`H(K, M(K)) = 0.0097 / 0.0241
   / 0.3321 <= 1/2`, decreasing in `m` — NC-A5). No proxy threshold
   criterion is used anywhere: the far bucket sits INSIDE `C_ker` with its
   own prefactors, and `M(K)` is where its contribution drops below the
   campaign's 0.2 tolerance.

4. **Coverage**: `M(K) <= 400` for every `K <= 4` (`K = 3` via the `K = 4`
   row), and the exact harness is now certified to `m = 400`
   (`harness_m200_20260811.md`): **no uncovered `m` remains for any
   `K <= 4`** — every `m >= 4` is covered by exact computation (`m <= 400`)
   or by Theorem T.9-final (`m >= M(K)`), with overlap.

**Status: T2 §8 item 4 is CLOSED (modulo referee) by this draft together
with wp2-b; Prop 3.5(ii) is closed modulo referee and modulo the
grid-certificate statuses inherited from its inputs (itemized in §1 and
§10). Prop 3.5(i) [T.8], the deep-tilt core model, and the region-2 handoff
are NOT touched (STATUS §4 items 4a–c).**

---

## 1. Inputs and their statuses

Notation as in the merged draft, T2, and wp2-b: `lambda = sigma^2 =
m(m-1)(2m+5)/72`, `S_r = sum_{j=1}^m j^r`, tilt `lam`, `w = lam m`, `lam(k)`
the tilted-mean solution (`mu(lam(k)) = k`), `s2 = sigma_{lam(k)}^2`,
`kappa_r(lam)` the tilted cumulants, WLOG `lam >= 0`. Model coefficients
`alpha = kappa_3/6, beta = -kappa_4/24, delta = kappa_5/120, gamma =
kappa_6/720`; scaled `a, b, d, g` (divide by `s2^{3/2}, s2^2, s2^{5/2},
s2^3`); `h = s2^{-1/2}`, `t_1 = sqrt(2) pi/m`.

Every input consumed, with its status flag (house rules):

| input | statement | status |
|---|---|---|
| T.1(ii) (tilt invariance), (T.8a) (kernel identity at the mean) | T2 §1, §4 | PROVED, two-referee (referee_t2_maths §2.1, §2.10) |
| T.9''(b) | `|R_7(t)| <= (m+1)^8 |t|^7 / 2.8e6` on `|t| <= t_1`, all real `lam`, `m >= 30` | PROVED, two-referee (referee_t2_maths §2.12; chain gives 2.8549e6) |
| wp2-b W.0 | model polynomial `P(y)`, `phat = Z P`; `N(0) = -36a^2 + N0_resid` | PROVED (sympy-exact; both referees) |
| wp2-b W.3 boxes | `|kappa_3| <= lam(S_4+m)/120`, `|kappa_4| <= (S_4+m)/120`, `|kappa_5| <= C5(S_5+m)`, `|kappa_6| <= C6(S_6+m)`, `C5 <= 5.08266e-3`, `C6 = 1/252 <= 3.96835e-3`, on `|w| <= 4`, `m >= 30` | PROVED (both referees; repairs B5 closed the certificate tails) |
| wp2-b W.1 floors | `s2 >= c_K lambda`: `c_1 = 0.967`, `c_2 = 0.868` | W.1(i) PROVED for all `m >= 30` (repair B5 / referee V2) |
| wp2-b W.1(ii) floor | `c_4 = 0.60` | **grid-certified** (repair B4: exhaustive integer `m in [30, 400]` x 200-pt `w`-grid, max 0.379644 <= 0.40; Sturm-able) |
| wp2-b W.4, W.7 | Taylor bucket `T(K)`; the exact `Delta_ker` decomposition | PROVED / exact-by-definition (both referees) |
| wp2-b W.5 | Lin bucket, conditional on `|s2 log r - 1| <= 1/2` | PROVED conditional — condition discharged in §7 |
| wp2-b W.6 (+ repair B2) | `c_w(1) = 0.407, c_w(2) = 0.466, c_w(4) = 1` | **grid-certified** (referee F2: relabeled; worst-at-180 confirmed by fine scan + m->infinity limit) |
| wp2-b PW buckets | `PW_grid = 1.5491/4.0889/4.9126` (m <= 2000; K=4 exceeded +0.22% beyond, repair B3); `PW_closed = 10.278/21.063/187.414` (all m >= 180) | grid-certified / PROVED-given-W.1–W.3 |
| wp1-c W.4(i) | `|phi_lam(t)| <= exp(-c_1(K) m)` on `t_1 <= |t| <= pi`, `|lam| <= K/m`, `K <= m/4`, `m >= 30`; `c_1(1) = 0.2259, c_1(2) = 0.1802, c_1(4) = 0.1019` (safe-rounded down, margins >= 9.1e-6, repair A1) | PROVED, both referees |
| merged draft L.3.2 | `s2 <= lambda` | PROVED |
| Bona (ambient) | `r(k) >= 1`, i.e. `u >= 0` | citation (as in wp2-b W.5) |
| harness | exact ground truth `4 <= m <= 400` | PROVED (exact integer run, `harness_m200_20260811.md`) |

Everything below is elementary given these: closed-form Gaussian moments,
one exponential-Taylor remainder with integral form, and triangle
inequalities. The only genuinely new analytic content is the real/imaginary
SPLIT of the model error (Lemma D.1') that rescues the order of the odd
rows.

---

## 2. Lemma D.1: the tilted model function, coefficient boxes, and the two majorants

Fix `K in {1, 2, 4}`, `m >= 30`, an interior `k` with `0 < lam = lam(k) <=
K/m`, and write `phi(t) := phi_lam^c(t) = E_lam e^{it(X - k)}` (centered at
the mean `mu(lam) = k`). By T.9'' (analyticity + 6th-order remainder), on
`|t| <= t_1`:

```
phi(t) = e^{-s2 t^2/2} e^{-z(t)} ,     z := U_0 - R_7 ,
U_0 := i alpha t^3 + beta t^4 - i delta t^5 + gamma t^6 ,   |R_7(t)| <= A7 |t|^7 ,
```

and the MODEL function whose Fourier transform is wp2-b's `Z(y) P(y)` is

```
phihat(t) := e^{-s2 t^2/2} Q(t) ,   Q := 1 - U_0 + U_0^2/2 - D_2 ,
D_2 := (the degree 9..12 part of U_0^2/2)
     = i(beta delta - alpha gamma) t^9 + (delta^2/2 - beta gamma) t^10
       + i delta gamma t^11 - ... (exact signs immaterial below; moduli:)
|Re D_2| <= (A4 A6 + A5^2/2) t^10 + (A6^2/2) t^12 ,
|Im D_2| <= (A3 A6 + A4 A5) t^9  + (A5 A6) t^11 .
```

(NC-A1(d) verifies `phihat`'s transform equals `Z P` to 41 digits, and the
model kernel identity to 38 digits — the model IS wp2-b's `F(0)` object.)

**Coefficient boxes** (from W.3 + T.9''(b); `S_r` exact):

```
|alpha| <= A3 := (K/m)(S_4+m)/720          |beta|  <= A4 := (S_4+m)/2880
|delta| <= A5 := C5 (S_5+m)/120            |gamma| <= A6 := C6 (S_6+m)/720
A7 := (m+1)^8 / 2.8e6 ,                    s2 >= s2min := c_K lambda .
```

### Lemma D.1 (Gaussian domination and the crude majorant).
Define

```
eps = eps_K(m) := [ A4 t_1^4 + A6 t_1^6 + A7 t_1^7 ] / ( s2min t_1^2 / 2 ) ,
a_box := (1 - eps) s2min / 2 .
```

Then for `|t| <= t_1` (values of `eps`: NC-A1(a); e.g. `eps <= 0.1735 /
0.1932 / 0.2796` at `m >= 180` for `K = 1/2/4`, decreasing in `m`):

(i) `|phi(t)| <= e^{-a_box t^2}`;

(ii) `|phi(t) - phihat(t)| <= e^{-a_box t^2} W_A(t)`, where, with the
majorant polynomials `UB := A3 t^3 + A4 t^4 + A5 t^5 + A6 t^6` (for
`|U_0|`), `VZ := UB + A7 t^7` (for `|z|`),

```
W_A := VZ^3/6 + A7 t^7 (1 + UB + A7 t^7/2) + |D_2|-majorant .
```

*Proof.* Each of `A4 t^4, A6 t^6, A7 t^7` is `t^2` times a nondecreasing
function of `t`, so on `|t| <= t_1`: `Re z >= -(A4 t^4 + A6 t^6 + A7 t^7)
>= -eps (s2min/2) t^2`, and `|e^{-z}| = e^{-Re z} <= e^{eps s2min t^2/2}`,
giving (i) via `s2 >= s2min`. For (ii): `phi - phihat = e^{-s2 t^2/2}
[e^{-z} - Q]` and

```
e^{-z} - Q = [ e^{-z} - (1 - z + z^2/2) ] + [ (1 - z + z^2/2) - (1 - U_0 + U_0^2/2) ] + D_2 ,
```

the middle bracket being exactly `R_7 - U_0 R_7 + R_7^2/2` (substitute `z =
U_0 - R_7`). The exponential-Taylor remainder in integral form,

```
e^{-z} - (1 - z + z^2/2) = -(z^3/2) int_0^1 (1 - tau)^2 e^{-tau z} dtau ,   (D.1a)
```

has modulus `<= (|z|^3/6) sup_tau e^{-tau Re z} <= (VZ^3/6) e^{eps s2min
t^2/2}`; the other two brackets are bounded by their coefficient moduli
(and `1 <= e^{eps s2min t^2/2}`). Collect. ∎

NC-A1(b,c): truth check against exact `phi` (mpmath dps 40, `m in {30, 60,
120} x K in {1, 2, 4} x w in {K/4, K/2, K}`, 48-pt `t`-grids): max ratio
(i) `0.999312`, (ii) `0.191026` — both `<= 1`. **PASS.**

### Lemma D.1' (the real/imaginary split — the odd-row rescue).
Write `phi - phihat = e^{-s2 t^2/2} (DC(t) + i DS(t))` (`DC, DS` real) and

```
ZR := A4 t^4 + A6 t^6 + A7 t^7      (majorant of |Re z|) ,
ZI := A3 t^3 + A5 t^5 + A7 t^7      (majorant of |Im z|) ,
R7X := A7 t^7 (1 + UB) + A7^2 t^14 / 2 ,
WR := (ZR^3 + 3 ZR ZI^2)/6 + (3 ZR^2 ZI^2 + ZI^4)/24 + R7X + |Re D_2|-maj ,
WI := (ZR + ZI)^3/6 + R7X + |Im D_2|-maj ,
VE := A4 t^4 + (A6 + A3^2/2) t^6 + (A4^2/2 + A3 A5) t^8   ( >= |Re Q - 1| ) ,
VO := A3 t^3 + A5 t^5 + A3 A4 t^7                          ( >= |Im Q| ) .
```

Then on `|t| <= t_1`, with `EE(t) := e^{eps s2min t^2/2}`:

```
|DC| <= EE * WR ,   |DS| <= EE * WI ,   |Re e^{-z}| <= EE ,   |Im e^{-z}| <= EE * ZI .
```

**Every monomial of `WR` and `VE` either has even total degree in the
odd-coefficient boxes `(A3, A5)` or carries at least one factor `A7`
(`R_7`'s split is unknown, so `A7` sits in both `ZR` and `ZI`; every
`A7`-monomial is itself of strictly negative net `m`-order in the §6
exponent audit). In particular the bare `alpha^3` monomial — `A3^3`, no
`A7` — lives only in `WI`,** and §4 shows `WI` only ever multiplies another
odd-family factor inside the real-part kernel bucket.

*Proof.* `Re(1 - z + z^2/2) = 1 - Re z + ((Re z)^2 - (Im z)^2)/2` and
`Im(1 - z + z^2/2) = -Im z + Re z Im z`, so the `Q`-comparison brackets
split as in D.1 with real/imag moduli as displayed (`Re Q - 1` collects
`-beta t^4, (-gamma - alpha^2/2) t^6, (beta^2/2 + alpha delta) t^8`; `Im Q`
collects `-alpha t^3, delta t^5, alpha beta t^7` — read off `Q`). For the
cube remainder, take real and imaginary parts of (D.1a) with `z^3 =
(zR^3 - 3 zR zI^2) + i (3 zR^2 zI - zI^3)` and `e^{-tau z} = e^{-tau zR}
(cos(tau zI) - i sin(tau zI))`:

```
Re[.] = -(1/2) int (1-tau)^2 e^{-tau zR} [ (zR^3 - 3 zR zI^2) cos(tau zI) + (3 zR^2 zI - zI^3) sin(tau zI) ] dtau .
```

Bound `|cos| <= 1` on the first term (`int (1-tau)^2 = 1/3`) and `|sin(tau
zI)| <= tau |zI|` on the second (`int (1-tau)^2 tau = 1/12`): `|Re[cube]|
<= EE [ (ZR^3 + 3 ZR ZI^2)/6 + (3 ZR^2 ZI + ZI^3) ZI / 24 ]` — the odd cube
`zI^3` picks up the extra `|zI|` and becomes even. The imaginary part uses
`|sin|, |cos| <= 1` throughout: `|Im[cube]| <= EE (ZR + ZI)^3/6`. Finally
`e^{-z} = e^{-zR}(cos zI - i sin zI)` gives `|Re e^{-z}| <= e^{-zR} <= EE`
and `|Im e^{-z}| <= e^{-zR} |sin zI| <= EE * ZI`. ∎

NC-A3(1): truth of all three split bounds on the same grids: max ratios
`WR 0.085`, `WI 0.191`, `ZI 0.943` — all `<= 1`. **PASS.**

---

## 3. Lemma D.2: kernel identities at the tilted mean

Let `P_j := P_lam(X = k + j)` for `j in {-1, 0, 1}`; by tilt invariance
(T.1(ii)), `r(k) = P_0^2/(P_{-1} P_1)`, so `u = D/(P_{-1} P_1)` with
`D := P_0^2 - P_{-1} P_1`.

### Lemma D.2.
(i) *(true side — this is (T.8a), cited)*
```
D = (1/4pi^2) intint_{[-pi,pi]^2} phi(s) phi(t) (1 - cos(s-t)) ds dt ,
P_{-1} P_1 = (1/4pi^2) intint phi(s) phi(t) cos(s-t) ds dt .
```

(ii) *(model side — new, 3 lines; no evenness of `psi` needed at `x = 0`)*
For any `psi in L^1(R)` with `q(x) := (1/2pi) int psi(t) e^{-itx} dt`:
```
q(0)^2 - q(1) q(-1) = (1/4pi^2) intint_{R^2} psi(s) psi(t) (1 - cos(s-t)) ds dt .
```
In particular, with `psi = phihat`: `Dhat := phat(0)^2 - phat(1) phat(-1)`
equals the model kernel integral, and (wp2-b W.4 Step 1, exact)
`1 + v = phat(0)^2/(phat(1) phat(-1))`, i.e. `v = Dhat/(phat(1) phat(-1))`.

*Proof of (ii).* `q(0)^2 = (1/4pi^2) intint psi(s) psi(t) ds dt`, and
`q(1) q(-1) = (1/4pi^2) intint psi(s) psi(t) e^{i(s-t)} ds dt`. Under the
swap `s <-> t` the factor `psi(s)psi(t)` is symmetric while `e^{i(s-t)}`
maps to its conjugate; averaging the two labelings replaces `e^{i(s-t)}` by
`cos(s-t)`. Subtract. ∎ (Lemma B.5 is the even-`psi`, general-`x` version;
at the tilted mean only `x = 0` is needed, so complex `psi` costs nothing —
exactly as in (T.8a)'s derivation for the true `phi`.)

NC-A1(d): (ii) verified for `psi = phihat` at `(m, w) = (30, 1), (60, 2)`
by independent 1-D quadratures (`q(1)q(-1) = [(int psi cos)^2 + (int psi
sin)^2]/4pi^2`): rel. deviation `<= 6.2e-38`, `Im = 0` to 30 digits, and
`q(0) = Z(0) P(0)` to 41 digits. **PASS.**

**Consequently** (the exact B.8-step-3 chain in the tilted frame): with
`DeltaD := D - Dhat`, `w~ := DeltaD/(phat(1) phat(-1))` and `1 + delta :=
(P_{-1} P_1)/(phat(1) phat(-1))`:

```
u = (v + w~)/(1 + delta) ,      Delta_ker = s2 log( (1+u)/(1+v) ) = s2 log(1 + zeta) ,
zeta = ( w~ - delta v ) / ( (1 + delta)(1 + v) ) .
```

*Proof:* `u = D/(P_{-1}P_1) = (Dhat + DeltaD)/(phat_1 phat_{-1}(1+delta))
= (v + w~)/(1+delta)`; then `1 + u = (1 + delta + v + w~)/(1+delta)`, and
`(1+delta+v+w~) - (1+delta)(1+v) = w~ - delta v`, so `(1+u)/(1+v) = 1 +
(w~ - delta v)/((1+delta)(1+v))`. ∎ (Identical in shape to g1_draft_b B.8
step 3; only the frame is tilted and `x = 0`.)

---

## 4. Lemma D.3: the kernel-transfer remainder Delta D

Notation for closed-form moments (all elementary):

```
J(n, a) := int_R |t|^n e^{-a t^2} dt = Gamma((n+1)/2) / a^{(n+1)/2} ,
tail(n, t_0, c) >= int_{t_0}^inf t^n e^{-c t^2} dt :
   n = 2k+1 odd:  exact,  e^{-c t_0^2} k! / (2 c^{k+1}) * sum_{j<=k} (c t_0^2)^j / j! ;
   n even:        tail(n+1, t_0, c) / t_0     (t^n <= t^{n+1}/t_0 on t >= t_0) .
```

For a majorant polynomial `p = sum_n p_n |t|^n`, write `Jp(p, a; shift) :=
sum_n p_n J(n + shift, a)`. Split `[-pi, pi]^2 = B union (complement)`,
`B := [-t_1, t_1]^2`, and correspondingly (Lemma D.2)

```
DeltaD = intint_B (phi phi - phihat phihat) k(s,t)  +  intint_{[-pi,pi]^2 \ B} phi phi k
         -  intint_{R^2 \ B} phihat phihat k ,          k(s,t) := (1 - cos(s-t))/(4 pi^2) ,
|DeltaD| <= D_box + D_out + D_tail .
```

### Lemma D.3 (the three pieces; refined box). With `a := a_box`, `cT :=
s2min/2`, `far := 2 (pi - t_1) e^{-c_1(K) m}`, and `VQ := UB + A3^2/2 t^6 +
A3 A4 t^7 + (A4^2/2 + A3 A5) t^8` (the `|Q - 1|` majorant):

**(i) box, refined (real-part route).** Since `D` and `Dhat` are real, only
`Re[phi(s)phi(t) - phihat(s)phihat(t)]` contributes on `B`. Writing `phi =
e^{-s2 t^2/2}(C + iS)`, `phihat = e^{-s2 t^2/2}(Chat + iShat)`:

```
Re[phi phi - phihat phihat](s, t)
  = e^{-s2(s^2+t^2)/2} [ DC(s) C(t) - DS(s) S(t) + Chat(s) DC(t) - Shat(s) DS(t) ] ,
```

and by Lemma D.1' (`|C| <= EE`, `|S| <= EE ZI`, `|Chat| <= 1 + VE`,
`|Shat| <= VO`), with all `EE`-factors absorbed into `a`:

```
|Re[...]| <= e^{-a(s^2+t^2)} [ WR(s) * 1 + (1 + VE(s)) WR(t) + WI(s) ZI(t) + VO(s) WI(t) ] .
```

The kernel obeys `1 - cos(s-t) <= (s-t)^2/2 = (s^2+t^2)/2 - st`, and every
majorant above is a function of `|s|, |t|`, so each `st`-cross integral
vanishes by oddness. Hence, with `pair(p, q) := (1/2)[ Jp(p,a;2) Jp(q,a;0)
+ Jp(p,a;0) Jp(q,a;2) ]`:

```
D_box <= [ pair(WR, 1) + pair(1 + VE, WR) + pair(WI, ZI) + pair(VO, WI) ] / (4 pi^2) .
```

**The bare `alpha^3` monomial (in `WI`) meets only the odd-family slots
`ZI` and `VO` (both `O(A3 t^3)`): its lowest surviving product is
`alpha^4`-class, restoring every row to a nonpositive net power of `m`
after the `m^2` scaling of §6.** (The crude flavor replaces the bracket by
`pair(W_A, 1) + pair(1 + VQ, W_A)`-type rows — Lemma D.1(ii); it is what
NC-A2 assembles, and §6 records why it is NOT acceptable as the theorem.)

**(ii) out (true `phi` off the box).** The complement of `B` in
`[-pi,pi]^2` is covered by the two strips `{t_1 <= |s| <= pi} x {|t| <=
pi}` and its transpose; `1 - cos <= 2`; wp1-c W.4(i) bounds `int_{t_1 <=
|s| <= pi} |phi| <= far` (hypotheses `|lam| <= K/m`, `K <= m/4`, `m >= 30`
hold on our range), and `int_{-pi}^{pi} |phi| <= J(0, a) + far` (Lemma
D.1(i) on the box). Hence

```
D_out <= (1/pi^2) * far * ( sqrt(pi/a) + far ) .
```

**(iii) tail (model off the box).** `|phihat| <= e^{-s2 t^2/2} (1 + VQ)`
and the same two-strip cover of `R^2 \ B`:

```
D_tail <= (2/pi^2) * Ttail * ( J(0, cT) + Jp(VQ, cT; 0) ) ,
Ttail := tail(0, t_1, cT) + sum_n VQ_n tail(n, t_1, cT)    ( >= int_{t_1}^inf |phihat| ) .
```

*Proof.* (i): the displayed pointwise bound integrates term-by-term over
`R^2 >= B` (all integrands nonnegative); `pair` is the exact value of
`intint p(|s|) q(|t|) (s^2+t^2)/2 e^{-a(s^2+t^2)}`. (ii), (iii): as
displayed; the strip covers double-count the corner squares, in the safe
direction. ∎ (This is g1_draft_b Lemma B.6's proof verbatim, with: the
tilted 6-term model in place of the even 3-term one; W.4(i) replacing
Lemma 1.4 + Mills on the far strips — note there is NO Mills annulus at
all, since W.4(i) starts exactly at `t_1`; and the real-part split of (i)
as the new ingredient handling the odd rows.)

---

## 5. Lemma D.4: pointwise error at x = +-1, denominators, and v > 0

### Lemma D.4. With the objects of §2–§4 and `P0min, Pmin` the wp2-b W.4
Step-4 floors of `P(0)` and `min_J P` (`J = [-h, h]`), evaluated at the
boxed coefficients:

(i) *(pointwise error, refined)* For `j in {-1, +1}`:
```
|P_j - phat(j)| <= E_pt := (1/2pi) [ Jp(WR, a; 0) + Jp(WI, a; 1) ] + far/(2pi) + Ttail/pi .
```

(ii) *(denominators)* `phat(+-1) = Z(-+h) P(-+h) >= (2 pi lambda)^{-1/2}
e^{-1/(2 s2min)} Pmin > 0`, hence
```
|delta| <= 2 dbar + dbar^2 ,   dbar := sqrt(2 pi lambda) e^{1/(2 s2min)} E_pt / Pmin .
```

(iii) *(v > 0 and its size)* Let `core := 12 b + 36 a^2 / P0min^2 +
PW_closed/m^2 + T/m^2` (scaled boxes; wp2-b W.0 + W.4). If `LFlow := 1 -
core > 0` then
```
0 < v <= vS2 / s2 ,    vS2 := (1 + core) e^{(1 + core)/s2min} .
```
(NC-A4(3): `LFlow >= 0.9224` at every `(K, m)` the theorem uses.)

*Proof.* (i) `P_j - phat(j)` is a difference of two REAL numbers, and
`P_j - phat(j) = (1/2pi)[ int_B (phi - phihat) e^{-itj} dt + int_{t_1 <=
|t| <= pi} phi e^{-itj} dt - int_{|t| >= t_1} phihat e^{-itj} dt ]`. Take
the real part of the box integrand: `Re[(phi - phihat) e^{-itj}] =
e^{-s2 t^2/2} [ DC cos(tj) + DS sin(tj) ]` and `|sin(tj)| <= |t|` for
`j = +-1` — the odd factor `DS` (which carries the bare `alpha^3`) picks up
one power of `|t|`; bound by Lemma D.1' and integrate. The far and tail
pieces are bounded in modulus as in D.3(ii),(iii) (one-dimensional, no
kernel). (ii) `Z(-+h) = (2 pi s2)^{-1/2} e^{-h^2/2}`, `s2 <= lambda`
(merged Lemma 3.2), `h^2 = 1/s2 <= 1/s2min`, `P(-+h) >= Pmin` (wp2-b W.4
Step 4, the referee-verified coefficient rows). (iii) wp2-b W.4 + W.0 give
`s2 log F(0) = 1 - B_lam + N(0)/P(0)^2 + theta_T T`, and `|B_lam| = 12|b|`,
`|N(0)/P(0)^2| <= 36 a^2/P0min^2 + PW_closed/m^2` (the `-36 a^2` split plus
the closed-form residual bucket), so `s2 log F(0) in [1 - core, 1 + core]`.
`LFlow > 0` forces `log F(0) > 0`, i.e. `v = F(0) - 1 > 0`; and `s2 v = s2
(e^{log F} - 1) <= s2 log F e^{log F} <= (1 + core) e^{(1+core)/s2min}`. ∎

*(Clause (iii) closes the `v > 0` gap that wp2-b's referee flagged (F6) and
that the inherited first-pass lib left unverified; it is also exactly the
bound on `s2 v` that the `delta v` term of `zeta` needs.)*

---

## 6. Theorem D.5: the Delta_ker bound — and the odd-cube finding

### Theorem D.5.
Fix `K in {1, 2, 4}` and let `M(K) := 180 / 181 / 367`. For every
`m >= M(K)` and every interior `k` with `0 < |lam(k)| <= K/m`:

```
|Delta_ker(k)| <= C_ker(K) / m^2 ,
C_ker(1) = 30.89 ,   C_ker(2) = 209.03 ,   C_ker(4) = 37811 ,
```

where `C_ker(K) = C_ker(K, M(K))` and, for all `m` in range,

```
C_ker(K, m) := m^2 ( s2wf + (2 dbar + dbar^2) vS2 ) / ( (1 - 2 dbar - dbar^2)(1 - zbar) ) ,
s2wf := 2 pi lambda^2 e^{1/s2min} (D_box + D_out + D_tail) / Pmin^2   ( >= s2 |w~| ) ,
zbar := ( s2wf/s2min + (2 dbar + dbar^2) vS2/s2min ) / (1 - 2 dbar - dbar^2)   ( >= |zeta| ) ,
```

with every ingredient from Lemmas D.1'–D.4. **Scope note (honest).** The
`m`-dependent form `|Delta_ker| <= C_ker(K, m)/m^2` is a theorem for EVERY
`m >= M(K)` outright. The constant flavor (`C_ker(K) := C_ker(K, M(K))`)
additionally uses `C_ker(K, m) <= C_ker(K, M(K))`, which is CERTIFIED
decreasing on `[M(K), 3000]` (unit step to 1000, step 10 beyond; NC-A3(3))
and at `10^4` (NC-A5(3)) — grid-certificate status for `m > 3000`. The
exponent audit behind it: writing each box row's net power of `m` as
`2 + n_c + n_q - (p+q)/2` (coefficient factors `A_i` have `deg_m = `
`t`-power `+ 1`), every row has a NEGATIVE net exponent except the pure-
`alpha` quartic rows (`ZI^4`-class), whose exponent is 0 — explicit
rational functions of `m` decreasing to positive limits; a Sturm pass would
upgrade the tail to proof grade (flagged, §10). `M(K)` is the first
`m >= max(180, .)` at which the far + tail pieces contribute `<= 0.2` to
`C_ker` (NC-A3(4): far+tail crosses 0.2 at `m = 136 / 181 / 367`; the 180
floor is wp2-b's bucket scope).

*Proof.* By D.2, `Delta_ker = s2 log(1 + zeta)`, `zeta = (w~ - delta v)/
((1+delta)(1+v))`. By D.4(iii), `1 + v >= 1`; by D.4(ii), `|1 + delta| >=
1 - 2dbar - dbar^2 > 0`; so `|zeta| <= (|w~| + |delta| v)/(1 - 2dbar -
dbar^2) <= zbar` (using `s2 >= s2min` on both numerator terms and D.4(iii)
for `s2 v <= vS2`). `zbar` is of size `C_ker/(m^2 s2min)` — below `1e-6`
everywhere used — so `|Delta_ker| <= s2 |zeta|/(1 - |zeta|) <= (s2wf +
(2dbar + dbar^2) vS2)/((1 - 2dbar - dbar^2)(1 - zbar))`. The numerator
pieces are Lemmas D.3 (refined box + out + tail, with `s2^2 <= lambda^2`,
`e^{h^2} <= e^{1/s2min}`, `phat_1 phat_{-1} >= (2 pi lambda)^{-1}
e^{-1/s2min} Pmin^2`) and D.4. ∎

**Per-piece table** (NC-A3(2), `m^2`-scaled; `den` = the `(2dbar +
dbar^2) vS2`-piece):

| m | K | box | tail | far | den | **C_ker(K, m)** |
|---|---|---|---|---|---|---|
| 180 | 1 | 27.39 | 1.7e-10 | 5.2e-05 | 3.50 | **30.886** |
| 181 | 2 | (191.6 at 180) | 5.4e-08 | (0.209 at 180) | 17.65 | **209.022** |
| 367 | 4 | (35802 at 379) | 1.0e-13 | (0.070 at 379) | 1381 | **37810.044** |
| 400 | 1 | 18.68 | 1.2e-33 | 2.4e-24 | 2.40 | 21.081 |
| 400 | 2 | 148.21 | 1.5e-28 | 2.3e-16 | 13.79 | 162.017 |
| 400 | 4 | 35394 | 4.6e-15 | 1.2e-02 | 1364 | 37050.299 |
| 2000 | 1 | 12.44 | — | — | 1.56 | 14.005 |
| 2000 | 4 | 30161 | — | — | 1167 | 31336.430 |

### The odd-cube finding (why the crude route is rejected).
The first-pass assembly (inherited `wp2a2_lib.delta_ker_bound`, NC-A2) uses
the MODULUS majorant `W_A` (Lemma D.1(ii)) throughout. Its box bucket then
carries the bare cube row `VZ^3/6 ⊇ (A3 t^3)^3/6 = alpha^3 t^9/6`, whose
kernel entry scales as `K^3 m^{-3/2}` — NOT `O(m^{-2})`: the assembled
"constant" GROWS like `K^3 sqrt(m)` (NC-A2(3): `C_ker` increasing at
`m = 787 (K=1) / 256 (K=2) / 368 (K=4)`; verdict FAIL, kept on the record),
and at `K = 4` reaches `~6.0e4`. The TRUE `Delta_ker` has no such
component: `m^2 |Delta_ker|` is measured FLAT at `1.374–1.386` over
`m = 30..140` (wp2-b NC-W4(6); NC-A4 here). Mechanism: `-z^3/6 =
+ i alpha^3 t^9/6 + ...` is purely imaginary at leading order, while every
consumed quantity (`D`, `P_{+-1}`, `phat`) is REAL. Lemma D.1'/D.3'
implement exactly this cancellation: in the real-part bucket the odd-cube
survives only against another odd factor (`alpha^4`-class), and in the
pointwise bucket it picks up `|sin(tj)| <= |t|`. Result: every row decays
in `m`, and the assembled constants drop `53.4 -> 30.9` (K=1), `394 -> 210`
(K=2), `6.0e4 -> 3.8e4` (K=4), with monotonicity restored. *(This is the
kernel-bucket sibling of the item-4 notes' bare `-36 a^2` finding: in the
tilted frame, each odd-cumulant object must be placed by its REAL order,
not its modulus order.)*

---

## 7. Theorem T.9-final: the merge (closes Prop 3.5(ii) modulo referee)

### Theorem T.9-final.
Fix `K in {1, 2, 4}` (for `K = 3` use the `K = 4` row: `{|w| <= 3} subset
{|w| <= 4}`). For every `m >= M(K) = 180 / 181 / 367` and every interior
`k` with `0 < |lam(k)| <= K/m` (`w = lam(k) m`):

```
s2 log r(k) = 1 - B_m ( 1 + theta_1 c_w(K) w^2 ) + theta_2 C_R(K) / m^2 ,
s2 (r(k) - 1) = 1 - B_m ( 1 + theta_1 c_w(K) w^2 ) + theta_2 C_R(K) / m^2 + theta_3 Lin(K) ,
|theta_i| <= 1 ,      c_w(1) = 0.407 ,  c_w(2) = 0.466 ,  c_w(4) = 1 ,
```

with `Lin(K) = Lin(K, m)` the wp2-b W.5 bucket — an `O(1/m^3)` object whose
`m^2`-scaled entries are `m^2 Lin = 0.2308 / 0.2571 / 0.3719` at `m = 180`,
decreasing — and the closed-form constant

```
C_R(K) := PW(K) + T(K) + C_ker(K) :
   closed flavor (valid for ALL m >= M(K)):   41.17 / 230.09 / 37998 ;
   PW-grid flavor (PW grid-certified, m <= 2000; K = 4 row per repair B3):
                                              32.44 / 213.12 / 37815 .
```

*Proof.* Theorem W.7 (wp2-b, exact decomposition) + Prop W.6 with the
repaired envelope constants (repair B2) + Lemma W.4 give
`s2 log r(k) = 1 - B_m(1 + theta_1 c_w(K) w^2) + theta [PW + T]/m^2 +
Delta_ker(k)`; Theorem D.5 bounds `|Delta_ker| <= C_ker(K)/m^2`; triangle.
For the `(r-1)` form, Lemma W.5 requires `|s2 log r - 1| <= 1/2`: by the
log-form just proved, `|s2 log r - 1| <= H(K, m) := B_m (1 + c_w(K) K^2) +
C_R(K)/m^2 <= (1.080/m)(1 + c_w K^2) + C_R/m^2` (B.0(ii) for `B_m`), and

```
H(K, M(K)) = 0.0097 / 0.0241 / 0.3321 <= 1/2      (NC-A5(2)) ,
```

each piece decreasing in `m` (B_m-term manifestly; `C_R(K)/m^2` since
`C_ker(K, m)` decreases and PW, T decrease — wp2-b + NC-A3(3)). So the
hypothesis is discharged unconditionally on the stated range. ∎

**Coverage (with the harness extension).** `M(K) <= 400` for every
`K <= 4`, and `harness_m200_20260811.md` certifies the exact ground truth
(argmin central, min = central ratio, `varfit >= 187/216` with equality
only at `m = 6`, strict increase) for ALL `4 <= m <= 400`. Hence **for
every `K <= 4` there is no uncovered `m`**: the exact range `[4, 400]` and
the analytic range `[M(K), infinity)` overlap (`M(K) <= 400`). In
particular, for Theorem A's region-3 handoff (which needs `w_0 <= 1`,
i.e. `K = 1`): the analytic refined law holds for `m >= 180` with
`C_R(1) = 41.17` and `c_w(1) = 0.407 <= 1/2`, and everything below 180 is
exact. **This closes T2 §8 item 4 and, modulo referee and the flagged
grid-certificate inputs, Prop 3.5(ii).** *(T.9's original `c_w = 1/2`
survives at `K = 1, 2`; at `K = 4` the statement carries `c_w(4) = 1`,
per wp2-b W.6 + repair B2. Note the `w^2`-envelope caveat wp2-b's referee
F5 raised — "the final envelope can be fixed only after Delta_ker lands,
since it may carry its own `w^2/m` dependence" — is resolved here in the
clean direction: Theorem D.5's bound is `w`-uniform on `|w| <= K`, all of
its `w`-dependence having been boxed into the `K`-dependent constants, so
the merged envelope IS W.6's, unchanged.)*

**Downstream arithmetic (unchanged claims, now with constants).** For the
G4/part-(c) center-margin chase, region 3 consumes `K = 1`:
`1 - 1.080/m - C'/m^2` with `C' <= C_R(1) + m^2 Lin(1) <= 41.17 + 0.24 <
42`. Against the NC-13 tolerance analysis (`C' <= 20` gives `m >= 17`),
`C' = 42` moves the center-margin crossover only to `m ~ 27 << 400`: the
finite side is already done by the harness. The binding constraint for
part (c) remains the far-region / region-2 structure of Prop 3.5(i), not
these constants.

---

## 8. Numeric checks (verbatim outputs)

| # | script | validates | verdict |
|---|---|---|---|
| NC-A1 | `wp2a2_nc1_model_err.py` (inherited; run by me) | Lemma D.1 (eps table, Gaussian domination, crude majorant truth at dps 40), Lemma D.2(ii) (model kernel identity, 38 digits), lib-vs-mpmath cumulants | **PASS** |
| NC-A2 | `wp2a2_nc2_buckets.py` (inherited; run by me) | the CRUDE assembly — documents the odd-cube failure: non-monotone `C_ker`, `K=4 ~ 6.0e4` | **FAIL (by design of the check; kept as the record — §6)** |
| NC-A3 | `wp2a2_nc3_refined.py` (new) | Lemma D.1' split-majorant truth; refined per-piece table; monotone decrease; thresholds `M(K)`; crude-vs-refined-vs-truth | **PASS** |
| NC-A4 | `wp2a2_nc4_truth.py` (new) | ports vs wp2-b certified values; ground truth `m^2|Delta_ker|` (FULL k-scan at m=60 reproduces wp2-b NC-W4(6): 1.386/4.070/5.022); measured <= bound; `v > 0` (measured min 1.288e-05; proved clause LFlow > 0) | **PASS** |
| NC-A5 | `wp2a2_nc5_merge.py` (new) | merged `C_R(K)` table; Lin discharge `H <= 1/2`; large-m safety at 10^4; coverage `M(K) <= 400`; honesty ratios | **PASS** |

NC-A1 (trimmed):

```
(a) eps_K(m):  m=180: 0.1735 0.1932 0.2796   (m=30: 0.1873 0.2087 0.3019; all < 1)
    V_Re/(s2min t^2/2) nondecreasing on (0, t1] (m=30, K=4): True
(b,c) GLOBAL max ratios: (A.1a) 0.999312  (A.1b) 0.191026   (PASS iff <= 1)
    lib-vs-mp cumulant rel devs (m=60, w=2): max = 1.33e-12
(d) (m,w)=(30,1): |Dhat_1D - (q0^2-q1q-1)|/|.| = 3.21e-38 ; q(0) vs Z*P rel dev = 1.25e-41 ; Im ~ 0: True
    (m,w)=(60,2): 6.19e-38 ; 5.01e-41 ; True
NC-A1 VERDICT: PASS
```

NC-A2 (trimmed; the crude-route record):

```
    180  1   0.1735   47.4418 ...  53.4047   |  180  4  ... 449739.9956  (far 3.62e+05)
(2) K=1: far piece <= 0.2 first at m = 136 | K=2: 181 | K=4: 367
(3) K=1 NOT decreasing at m=787 | K=2 NOT at m=256 | K=4 NOT at m=368
NC-A2 VERDICT: FAIL
```

NC-A3 (trimmed):

```
(1) GLOBAL max ratios: WR 0.085347  WI 0.191037  ZI 0.943412
(2)   m  K    m2*box    m2*tail     m2*far      dbar    m2*den     m2*Cker2
    180  1   27.3882   1.66e-10   5.23e-05  5.35e-05    3.4951     30.8863
    180  2  191.6123   5.42e-08   2.09e-01  2.69e-04   17.6507    209.5757
    379  4  35801.7005  1.04e-13   6.99e-02  4.59e-03  1380.6310  37514.9161
    400  1   18.6796   1.16e-33   2.44e-24  7.48e-06    2.4011     21.0810
   2000  1   12.4421  2.18e-213  9.07e-177  1.95e-07    1.5627     14.0048
(4) K=1: mker = 136 | K=2: mker = 181 | K=4: mker = 367
(3) K=1: decreasing on [180, 3000]: True | K=2 on [181, 3000]: True | K=4 on [367, 3000]: True
(5)   K   M(K)   C_ker2(M)   crude C_ker(M)   truth anchor
      1    180     30.8863         53.4047       1.39   (bound/truth = 22.2x)
      2    181    209.0224        393.7193       4.07   (bound/truth = 51.4x)
      4    367   37810.0442      60055.3420       5.04   (bound/truth = 7502.0x)
NC-A3 VERDICT: PASS
```

NC-A4 (trimmed):

```
(1) K=1: T = 0.00035 (0.00035)  PW = 10.277 (10.278)  Lin = 0.2308 (0.2308)  match: True
    K=2: ... match: True   K=4: T/Lin exact; PW = 187.265 (187.414, port -0.08%, safe)  match: True
(2) m= 60 K=1 (step 1, 101 pts): measured = 1.386 (wp2-b anchor 1.386)  bound = 25268.2   True
    m= 60 K=2 (step 1, 197 pts): measured = 4.070 (anchor 4.070)   True
    m= 60 K=4 (step 1, 357 pts): measured = 5.022 (anchor 5.022)   True
    m=140 K=1 (step 8,  68 pts): measured = 1.354 (anchor 1.386)  bound = 36.4   True
    m=140 K=2: 4.054 (4.059)  bound = 293.8  True | m=140 K=4: 5.038 (5.038)  True
    min measured v over all scans: 1.288e-05  (> 0: True)
(3) LFlow: m=180: 0.99248/0.98696/0.92237 ; m=367: .../0.96388 ; m=1000: 0.99869/0.99775/0.98716  all > 0
NC-A4 VERDICT: PASS
```

NC-A5 (trimmed):

```
(1)   K  M(K)   C_ker2(M)   C_R grid(m<=2000)   C_R closed(all m>=M)
      1   180     30.8863            32.4358               41.1647
      2   181    209.0224           213.1123              230.0864
      4   367   37810.0442         37814.9708            37997.4722
(2) K=1: H(180) = 0.0097 <= 1/2 | K=2: H(181) = 0.0241 | K=4: H(367) = 0.3321 <= 1/2: True
(3) C_ker2(3000) > C_ker2(10000): 13.20 > 11.75 | 130.70 > 126.18 | 30909.94 > 30283.47  (all True)
(4) M(K) = 180/181/367, all <= 400: True
(5) provided C_R_closed = 118x / 657x / 108564x the worst measured need (0.35)
NC-A5 VERDICT: PASS
```

NC-A6 (`wp2a2_nc6_zbar.py`, new): the §6 `zbar < 1e-6` claim —
`max zbar = 3.394e-07` over `(K, m) in {(1,180), (2,181), (4,367)} x
{M(K), 400, 1000, 3000}`. **PASS.**

---

## 9. Sanity: measured truth vs proved constants

The assignment's sanity anchor: `Delta_ker`'s true measured size is
`~1.39 / 4.07 / 5.04` C_R units (K = 1/2/4), stable over `m = 30..140`.
Reproduced here INDEPENDENTLY (NC-A4: exact integer Mahonian rows, exact
`u` in Fractions, Newton `lam(k)`-solve, full k-scan at `m = 60`):
`1.386 / 4.070 / 5.022` — identical to wp2-b's NC-W4(6) row to all printed
digits. Against that truth:

| K | truth | C_ker (proved) | ratio | where the slack lives (per-piece, NC-A3(2)) |
|---|---|---|---|---|
| 1 | 1.39 | 30.89 | 22x | box 27.39 (the `A7 t^7` row — T.9''(b)'s `R_7` — plus `alpha^4`-class rows), denominator 3.50 |
| 2 | 4.07 | 209.03 | 51x | box 191.6-class, denominator 17.7 (`A3 ∝ K`: quartic rows x16) |
| 4 | 5.04 | 37811 | 7502x | box ~3.6e4, denominator ~1.4e3 (`A3`-quartics x256, with `c_4 = 0.60` moment powers) |

Comparison precedents inside the campaign: wp2-b's closed-form PW flavor is
6.6x / 5.2x / 38x above ITS grid truth for the same structural reason
(triangle inequality on `a`-heavy monomials; its K = 4 entry 187.4 vs 4.9);
g1_draft_b's `C_2(y_0 = 3) = 3940` vs measured 59 (67x). The K = 1 and
K = 2 rows here are in that established honesty class; K = 4 is worse
because the kernel bucket's monomials reach degree 4 in `alpha` (vs W.7's
degree <= 2 at the same `y = 0` point) and each `alpha` carries a factor
`K`. Two further honest notes:

1. The `Delta_ker` truth itself is a cancellation: wp2-b §8 measured the
   SIGNED sum of the pointwise and kernel buckets at `needed_env <= 0.35`
   while each bucket alone is `~1.4-5`; no triangle-inequality route can
   see that. The 22x here multiplies a quantity that is itself ~4-70x
   above the signed need — total honest distance from need: 118x-1e5x
   (NC-A5(5)). Downstream (§7) nothing breaks: the constants are consumed
   at `K = 1` against `m^2`-scaled margins with orders of headroom.
2. The refined route's remaining leading row is `A7 t^7` — i.e. T.9''(b)'s
   remainder constant `(m+1)^8/2.8e6`, which NC-T9b measured at ratio
   0.212 of truth; a 6th-to-8th-order model push (T.9'' gives all
   cumulants) would cut the K = 1 constant roughly in half. Not needed at
   current targets.

---

## 10. What remains

1. **Referee passes on this draft** (house rule: two). Special attention
   invited to: the real/imaginary split proofs (Lemma D.1'/D.3'/D.4(i) —
   the only new analytic content), the `EE`-absorption bookkeeping (`eps`
   into `a_box`, applied per variable), and the inherited scripts (audited
   and re-run by me, but originally written by the earlier dead session).
2. **Grid-certificate statuses inherited** (flag propagates into Theorem
   T.9-final, same class as (T.7b-cert)): wp2-b's `c_4 = 0.60` floor
   (repair B4: exhaustive `m in [30, 400]`, sampled beyond; Sturm-able),
   the `c_w(K)` envelope (repair B2 relabeled it grid-certified;
   monotonicity-provable per its referee), and the PW grid flavor
   (`m <= 2000`; the closed flavor is theorem-grade given W.1–W.3).
   A referee wanting Theorem T.9-final fully grid-free uses the closed
   PW flavor and needs only `c_4` and `c_w` upgraded (one page of
   monotonicity each, per wp2-b's referees). This draft's OWN
   grid-certificate item is single: the constant-flavor monotonicity
   `C_ker(K, m) <= C_ker(K, M(K))` beyond `m = 3000` (D.5 scope note;
   unit-step to 1000, step 10 to 3000, spot 10^4; the band (3000, 10^4)
   is sampled only at its endpoints; Sturm-able via the exponent audit —
   the `m`-dependent flavor of D.5 needs none of this).
3. **K = 4's constant is crude** (7502x truth). Two identified, mechanical
   sharpenings, neither needed at current targets: (a) cap the split
   majorants by their trivial bounds (`|DS| <= EE(1 + |Q|)`-class) and
   split the box integral at the radius where `ZI = 1` — the incomplete-
   moment machinery (`tail`) is already in the lib; (b) push the model to
   8th order (T.9''(a) supplies `kappa_7, kappa_8` bounds), halving the
   `A7` row. Also (c): a Cor-B.9-style two-sided corner rectangle for
   `(alpha, delta)` — the same refinement wp2-b §9 item 4 lists for PW.
4. **`m` in `[150, M(K))` is covered by the harness, not by the analytic
   law** — fine for every current consumer (they consume the harness's
   exact statements), but a future user wanting the analytic SHAPE
   (`1 - B_m(1 + ...)`) below 180 must extend the bucket evaluations
   downward (all pieces are `m`-decreasing, so this is evaluation, not new
   proof — wp2-b §9 item 2's same note).
5. **Untouched (STATUS §4 items 4a-c)**: Prop 3.5(i)/T.8 (deep-tilt core
   model; the `C = 600` bucket assembly; region-2 handoff `C_0`) — the
   remaining open mathematics of G2. Also untouched: G3, G4 (except the
   §7 note that part (c)'s center margin now has explicit region-3
   constants), and the T2 repair-application session for the maths
   referee's M1/M2 items (`t2_repairs` file, still pending per
   referee_t2_maths §5 — none of its items touches anything consumed
   here: T.10(2) and T.8'' are not inputs to this draft).
6. **Statement scope**: `K in {1, 2, 4}` (K = 3 via K = 4). A dedicated
   K = 3 row would need wp1-c's `c_1(3) = 0.1361` (exists) plus a `c_3`
   variance floor (does not exist in wp2-b; one band-refinement run).

*End of wp2_draft_a2. Blind protocol maintained (`g2_draft_t1` unread); no
existing file modified; every quoted number from a saved script run in this
session.*
