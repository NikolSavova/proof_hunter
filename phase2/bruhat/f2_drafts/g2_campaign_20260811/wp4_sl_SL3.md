# wp4_sl_SL3 — Extended Gaussian domination + tail integral (SL3 of wp4_plan)

*Wave-3 prover session, 2026-08-12. Assignment: sub-lemma SL3 of
`wp4_plan_20260811.md` (mid-range Gaussian domination extended from `pi/m` to
the `lam`-scale, plus the normalized tail bucket for the CL(79, 20, 0.89)
ledger). Verification scripts:
`g2_scripts/campaign_20260811/wp4_SL3/sl3_nc1_certificates.py` and
`sl3_nc2_sanity.py`, both SAVED and RUN, outputs archived beside them and
quoted verbatim in §8. Exact/high-precision arithmetic (mpmath dps >= 40 for
every certificate; floats only in the measured-truth sanity table, labeled as
such). No existing file modified.*

**Deliverable status: PROVED — with three explicit, flagged deviations from
the architected statement (§7), each in the safe direction for the SL4/SL5
consumers; the architected numeric interface (worst-band tail budget
`<= 1.01 + 0.2 + 0.01` at `m = 401`, each piece decreasing in `m`) is met
with room: my worst-band total is `<= 1.0125 + 0.0592 + 1.3e-7 <= 1.072`.**

Citable inventory used (per STATUS_wave2 §1/§3 and the plan §0):
T2 Lemma T.6(i) (exact per-factor modulus identity) and the (T.6ii) proof
skeleton (`|E e^{itV}|^2 = 1 - 2 E sin^2(t(V-V')/2)`, per-factor,
distribution-free); wp1-c Lemma W.3 (monotonicity of `q(M, r)` in `M`) and
Corollary W.5(ii) (far bound, PROVED); the M2 rescue lemma
(`referee_t2_maths.md` §3 M2: memorylessness mixture
`law(X) = alpha law(U_j) + (1-alpha) law(j + X)`, `alpha = 1 - q^j`, hence
`Var U_j^{lam} <= Var Geom(e^{-lam})`). SL2 is consumed **as a hypothesis,
form-level only** (its statement `A >= c_A(band) m`, plan §SL2), exactly as
the assignment permits. SL1 is not used. wp1-c Clause W.6 is NOT used
(deviation D2, §7 — the architected W.6 route has a gap; my replacement is
strictly stronger).

---

## 0. Notation (plan §0, restated minimally)

`m >= 2`; tilt `lam > 0` WLOG (all bounds depend on `|phi_lam|`, which is even
in `lam` and in `t` — wp1-c §0); `q := e^{-lam}`; `w := m lam`.
`U_j = U_j^{lam}` (`j = 1..m`) independent, `P(U_j = i) = q^i (1-q)/(1-q^j)`
on `{0, ..., j-1}` (truncated geometric); `S_lam = sum_j U_j`;
`s2 = sigma_lam^2 = Var S_lam = sum_j v_j`, `v_j := Var U_j`;
`phi(t) = phi_lam(t) := E e^{it(S_lam - mu(lam))}`, so
`|phi(t)| = prod_j |nu_j(t)|`, `nu_j(t) := E e^{it U_j}`.
`A := lam^2 s2` (the plan's error currency: `u = 1/A`).
`t_0(lam) := 2 arcsin(sinh(lam/2))` (defined for `lam <= 1.7627`).
Residual band `B(m) := {lam : 4/m < lam <= 0.89}`, `m >= 401` (so `w > 4`).
Geometric reference `X ~ Geom(q)`: `P(X = i) = (1-q) q^i`, `i >= 0`,
`Var X = q/(1-q)^2`.

Named constants of this note (all certified in NC-SL3-1, §8):

```
x1 := 3.9269  ( <= pi/0.8    = 3.9269908... )
x2 := 2.9251  ( <= pi/1.074  = 2.9251323... )
eps1* := 0.35 ,   c1 := (2/pi^2)(1 - eps1*) = 0.1317175... >= 1/8
eps2* := 0.57 ,   c2 := (2/pi^2)(1 - eps2*) = 0.0871362... >= 1/11.5
K_mid := 8/sqrt(2 pi)          = 3.1915382... <= 3.192
K_cro := 11.5/(1.6 sqrt(2 pi)) = 2.8673974... <= 2.87
0.64/11.5 = 0.0556521... >= 0.0556
K_far := sqrt(pi/2)/4          = 0.3133285... <= 0.3134
q(2, 1) = 0.0741265... >= 0.0741      (wp1-c W.3 notation)
t_0(0.89)/0.89 = 1.0737237... <= 1.074
```

## 1. Lemma SL3.B (tilt–variance cap `A <= m`) — PROVED

**Lemma SL3.B.** For every `m >= 1` and every real `lam != 0`:

```
s2 <= m / (4 sinh^2(lam/2)) ,        hence      A = lam^2 s2 <= m .
```

*Proof.* WLOG `lam > 0`. By the M2 rescue lemma (memorylessness mixture,
`referee_t2_maths.md` §3 M2 — supplied and script-verified there):
`Var U_j <= Var X = q/(1-q)^2` for every `j`. The identity
`(1-q)^2/q = (e^{lam/2} - e^{-lam/2})^2 = 4 sinh^2(lam/2)` gives
`Var X = 1/(4 sinh^2(lam/2))`; summing over `j = 1..m` gives the first
display. Then `A = lam^2 s2 <= m (lam/2)^2 / sinh^2(lam/2) <= m` since
`sinh y >= y` for `y >= 0`. ∎

*(Remark: this replaces the plan's suggested crude cap via B.0(i) — B.0(i)
bounds the UNTILTED variance `lambda`, and `s2 <= lambda` is not in the
citable inventory; SL3.B is self-contained, sharper on the band, and is the
`A <= m` monotone-normalization fact SL5's far column needs. Sanity: NC-PL1's
measured `A/m` band values `0.30–0.92` are all `< 1`. Checked on grids in
NC-SL3-2 (§8): 0 violations.)*

## 2. Lemma SL3.D (per-factor truncated quadratic domination) — PROVED

The engine of both tiers. Fix `lam in (0, 0.89]`, `j >= 2`; let `V, V'` be
iid copies of `U_j` and `D := V - V'`. Fix a real truncation point `b` with
`b >= x0/lam` for a constant `x0 in {x1, x2}` (in particular `b lam >= 2`).

**Lemma SL3.D.** With `eps_j(b) := E[D^2 ; |D| > b] / E[D^2]`,

```
eps_j(b) <= Eps(lam, x0)
         := e^{-x0} [ (x0/lam)^2 (1-q)^2/(q(1+q)) + 2 (x0/lam)(1-q)/(1+q) + 1 ] ,
```

uniformly in `j` (and in `m`).

*Proof.* Step 1 (exact difference law). `D` is symmetric; for `1 <= d <= j-1`,

```
P(D = d) = sum_{i=0}^{j-1-d} P(V = i+d) P(V' = i)
         = c_j^2 q^d (1 - q^{2(j-d)}) / (1 - q^2) ,     c_j := (1-q)/(1-q^j) ,
```

and `P(D = d) = 0` for `d >= j`. Hence `P(D = d) = K_j q^d g_j(d)` for all
`d >= 1`, with `K_j := c_j^2/(1-q^2) > 0` and
`g_j(d) := max(1 - q^{2(j-d)}, 0)`, which is **nonnegative and nonincreasing
in `d`** (as `d` grows, `q^{2(j-d)}` grows; for `d >= j` the max clips to 0,
matching `P(D = d) = 0`).

Step 2 (weight-domination / Chebyshev pairing). Let `mu(d) := d^2 q^d`. For
any `b >= 1`,

```
sum_{d > b} mu(d) g_j(d) / sum_{d >= 1} mu(d) g_j(d)
    <= sum_{d > b} mu(d) / sum_{d >= 1} mu(d) .
```

Indeed, cross-multiplying, the difference LHS-numerator x RHS-denominator
minus RHS-numerator x LHS-denominator equals
`sum_{d1 > b, d2 >= 1} mu(d1) mu(d2) [g_j(d1) - g_j(d2)]`; the sub-sum over
`d2 > b` vanishes by antisymmetry, and for `d2 <= b < d1` each bracket is
`<= 0` because `g_j` is nonincreasing. (Denominators are positive for
`j >= 2`: `g_j(1) > 0`.) Since `E[D^2; |D| > b] = 2 sum_{d > b} mu(d) K_j
g_j(d)` and `E D^2 = 2 sum_{d >= 1} mu(d) K_j g_j(d)`, this gives

```
eps_j(b) <= rho(b, q) := sum_{d > b} d^2 q^d / sum_{d >= 1} d^2 q^d .
```

Step 3 (geometric tail, real-argument monotone extension). Exactly (standard
geometric sums), `sum_{d >= 1} d^2 q^d = q(1+q)/(1-q)^3`, and for every
integer `n >= 1`,

```
sum_{d >= n} d^2 q^d = T(n) ,
T(n) := q^n [ n^2/(1-q) + 2 n q/(1-q)^2 + q(1+q)/(1-q)^3 ]      (real n >= 0).
```

`T` is nonincreasing on `{n real : lam n >= 2}`: `T'(n) = q^n [ -lam F(n) +
F'(n) ]` with `F(n)` the bracket and `F'(n) = 2n/(1-q) + 2q/(1-q)^2`, and
`lam n >= 2` gives `lam n^2/(1-q) >= 2n/(1-q)` and `2 lam n q/(1-q)^2 >=
2 q/(1-q)^2`, while `lam q(1+q)/(1-q)^3 >= 0`. The tail `sum_{d > b}` starts
at the smallest integer `n_0 > b`; since `n_0 > b >= x0/lam` and
`x0 >= x2 = 2.9251 > 2`, monotonicity applies on `[x0/lam, n_0]`:

```
sum_{d > b} d^2 q^d = T(n_0) <= T(x0/lam)
  = e^{-x0} [ (x0/lam)^2/(1-q) + 2 (x0/lam) q/(1-q)^2 + q(1+q)/(1-q)^3 ] .
```

Dividing by `q(1+q)/(1-q)^3` gives `rho(b, q) <= Eps(lam, x0)` as displayed. ∎

## 3. Lemma SL3.A (the two eps-certificates) — PROVED

**Lemma SL3.A.** For all `lam in (0, 0.89]`:

```
(i)  Eps(lam, x1) <= 0.35  = eps1* ,        x1 = 3.9269 ;
(ii) Eps(lam, x2) <= 0.57  = eps2* ,        x2 = 2.9251 .
```

*Proof.* Write `Eps(lam, x0) = e^{-x0} [ x0^2 phi1(lam)^2 psi(lam)
+ 2 x0 phi1(lam) chi(lam) + 1 ]` with `phi1(lam) := (1 - e^{-lam})/lam`,
`psi(lam) := 1/(q(1+q))`, `chi(lam) := 1/(1+q)`. Elementary monotonicity:
`phi1` is decreasing on `(0, infty)` (power series of `(1-e^{-x})/x` has
alternating decreasing... standard: `phi1(lam) = int_0^1 e^{-lam u} du`,
manifestly decreasing), with `phi1(0+) = 1`; `q = e^{-lam}` is decreasing,
so `psi` and `chi` are increasing. Partition `(0, 0.89]` into 890 intervals
`(a_i, a_{i+1}]`, `a_i = 0.001 i`. On each interval,

```
Eps(lam, x0) <= E_i(x0) := e^{-x0} [ x0^2 phi1(a_i)^2 psi(a_{i+1})
                          + 2 x0 phi1(a_i) chi(a_{i+1}) + 1 ]
```

(with `phi1(a_0) = phi1(0) := 1`). NC-SL3-1 (§8) evaluates every `E_i` at
mpmath dps 40 and certifies

```
max_i E_i(x1) = 0.32257... <= 0.35      (attained on the top interval),
max_i E_i(x2) = 0.54890... <= 0.57      (attained on the top interval),
```

a finite chain of point evaluations of `exp` at displayed arguments, rounded
in the safe direction — the house-approved certificate class (cf. wp1-c §0
"point evaluations of log/arctan"; no grid-sampling of a continuum claim is
involved: the monotone-factor bound is rigorous on each whole interval). ∎

*(Margins: 7.8% on (i), 3.7% on (ii). The continuum (`lam -> 0`) values are
`0.2490` and `0.4402` (NC-SL3-1); the certified sup sits at `lam = 0.89`.)*

## 4. Theorem SL3.1 (two-tier extended Gaussian domination) — PROVED

**Theorem SL3.1.** For every `m >= 2` and every real `lam` with
`0 < |lam| <= 0.89` (no lower bound on `|lam|`, no condition tying `t` to
`pi/m`):

```
(i)   |phi_lam(t)| <= exp( - c1 s2 t^2 )  <= exp( - s2 t^2 / 8 )
                                 for 0 < t <= 0.8 |lam| ,   c1 = 0.1317... ;
(i')  |phi_lam(t)| <= exp( - c2 s2 t^2 )  <= exp( - s2 t^2 / 11.5 )
                                 for 0 < t <= 1.074 |lam| ,  c2 = 0.0871... .
```

Part (i) is the architected SL3(i) (with `m >= 401`, `lam in B(m)` relaxed to
the above); part (i') is the second tier that §6 uses on the crossover zone.

*Proof.* WLOG `lam > 0`. Fix `t` in the stated range and set `b := pi/t`.

Per factor `j` (T.6ii skeleton, citable): with `V, V'` iid `~ U_j`,
`D = V - V'`, `|nu_j(t)|^2 = E cos(tD) = 1 - 2 E sin^2(tD/2)`. On the event
`|D| <= b = pi/t` we have `|tD/2| <= pi/2`, where `sin u >= (2/pi) u`
(concavity), so `sin^2(tD/2) >= t^2 D^2/pi^2`; dropping the complementary
event (`sin^2 >= 0`),

```
E sin^2(tD/2) >= (t^2/pi^2) E[ D^2 ; |D| <= b ]
             >= (t^2/pi^2) (1 - eps_j(b)) E[D^2]
             =  (t^2/pi^2) (1 - eps_j(b)) 2 v_j .
```

Tier (i): `t <= 0.8 lam` gives `b = pi/t >= pi/(0.8 lam) >= x1/lam` (since
`x1 <= pi/0.8`), so Lemmas SL3.D + SL3.A(i) give `eps_j(b) <= 0.35`, whence
`|nu_j(t)|^2 <= 1 - (4/pi^2)(0.65) v_j t^2 <= exp(-(4/pi^2)(0.65) v_j t^2)`
(using `1 - z <= e^{-z}`). Multiplying over `j = 1..m` (the `j = 1` factor is
`nu_1 = 1`, `v_1 = 0`, trivially conformal) and taking square roots:

```
|phi(t)| <= exp( - (2/pi^2)(0.65) s2 t^2 ) = exp( - c1 s2 t^2 ) ,
```

and `c1 = 0.1317175... >= 1/8` (certified). Tier (i'): identically with
`t <= 1.074 lam`, `b >= pi/(1.074 lam) >= x2/lam`, `eps_j <= 0.57` by
SL3.A(ii), `c2 = (2/pi^2)(0.43) = 0.0871362... >= 1/11.5` (certified). ∎

*(Measured truth, NC-SL3-2: min over the (i) range of `-log|phi|/(s2 t^2)`
is `0.3794–0.4923` across the band at `m = 401` — 2.9x–3.7x above `c1`; on
the (i') zone `[0.8 lam, 1.074 lam]` the min is `0.3219–0.4861` — 3.7x–5.6x
above `c2`. The pressure is in the route constant, as the plan said:
`c1/(1/8) = 1.054`, a 5.4% route margin; `c2/(1/11.5) = 1.002`, 0.2% — but
the certificate side of (i') carries 3.8%, and the consumer (§6) uses (i')
only through Mills where 8x headroom sits above it.)*

## 5. Lemma SL3.C (crossover geometry) — PROVED

**Lemma SL3.C.** For `0 < lam <= 0.89`:
`lam <= t_0(lam) = 2 arcsin(sinh(lam/2)) <= 1.074 lam`.

*Proof.* Lower: `arcsin y >= y` and `sinh y >= y` give `t_0 >= lam`. Upper:
`f(y) := arcsin(sinh y)` on `[0, 0.445]` is the composition of the convex
increasing `arcsin` (on `[0, 1)`: `arcsin'' = y (1-y^2)^{-3/2} >= 0`) with
the convex increasing `sinh`, hence convex (`(g o k)'' = g''(k) k'^2 +
g'(k) k'' >= 0`), with `f(0) = 0`; therefore `f(y)/y` is nondecreasing, so
`t_0(lam)/lam = f(lam/2)/(lam/2)` is maximal at `lam = 0.89`:
`t_0(0.89)/0.89 = 1.0737237... <= 1.074` (certified, NC-SL3-1; margin
`2.76e-4` — a single point evaluation at dps 40). Note
`sinh(0.445) = 0.4598... <= 1`, so `t_0` is defined, and
`t_0(0.89) = 0.9556... < pi`. ∎

## 6. Theorem SL3.2 (the tail bucket in u-units) — PROVED

**Theorem SL3.2.** Let `m >= 401` and `lam in B(m)` (so `w > 4`,
`4/m < lam <= 0.89`). Set

```
T_u := A sqrt(s2/(2 pi)) int_{lam/2}^{pi} |phi_lam(t)| dt .
```

Then, unconditionally on the band,

```
T_u <= P1 + P2 + P3 ,
P1 := 3.192 sqrt(A) exp(-A/32)          [mid,       [lam/2, 0.8 lam] ]
P2 := 2.87  sqrt(A) exp(-0.0556 A)      [crossover, [0.8 lam, t_0]   ]
P3 := 0.3134 m^{5/2} exp(-0.0741 m)     [far,       [t_0, pi]        ] ,
```

with the monotonicity facts: `P1` is decreasing in `A` for `A >= 16`; `P2`
is decreasing in `A` for `A >= 9`; `P3` is decreasing in `m` for `m >= 34`;
and `P3 <= 1.3e-7` for all `m >= 401`. Consequently, **under SL2's
hypothesis** (`A >= c_A(band) m`, `c_A >= 0.28` on every band — consumed
form-level), for every band and every `m >= 401`:

```
T_u <= 3.192 sqrt(A0) e^{-A0/32} + 2.87 sqrt(A0) e^{-0.0556 A0} + 1.3e-7
                                     at A0 = c_A(band) * 401 ,  and per band:
band      c_A    A0      P1         P2        P3        total
(4,5]     0.28  112.28  1.0125     0.0592    1.3e-7    1.0717
(5,6]     0.35  140.35  0.4709     0.0139    1.3e-7    0.4848
(6,8]     0.42  168.42  0.2146     0.0032    1.3e-7    0.2178
(8,10]    0.52  208.52  0.0682     0.0004    1.3e-7    0.0686
(10,20]   0.60  240.60  0.0269     0.0001    1.3e-7    0.0270
(20,40]   0.70  280.70  0.0083     0.0001    1.3e-7    0.0083
(40,inf)  0.80  320.80  0.0026     0.0001    1.3e-7    0.0026
```

(safe-rounded up, NC-SL3-1; each column decreasing in `m` at fixed band).
The worst band's total `1.0717` sits inside the architected budget
`1.01 + 0.2 + 0.01 = 1.22` with 12% room; the architected THREE-SLOT form
also holds piecewise in the corrected form `(3.192, 0.2, 0.01)` — see §7.

*Proof.* Split `[lam/2, pi] = [lam/2, 0.8 lam] u [0.8 lam, t_0] u [t_0, pi]`
(valid: `0.8 lam < lam <= t_0 <= 1.074 lam < pi` by SL3.C).

**Mid.** By SL3.1(i), on `[lam/2, 0.8 lam]` the integrand is
`<= e^{-s2 t^2/8}`; extend the (Gaussian) integral to `+infty` and apply
Mills (`int_c^infty e^{-a t^2} dt <= int_c^infty (t/c) e^{-a t^2} dt
= e^{-a c^2}/(2 a c)`, elementary) with `a = s2/8`, `c = lam/2`:
`a c^2 = (s2/8)(lam^2/4) = A/32` and `2 a c = 2 (s2/8)(lam/2) = s2 lam/8`.
Hence, using `lam sqrt(s2) = sqrt(A)`,

```
A sqrt(s2/(2pi)) int_{lam/2}^{0.8 lam} |phi| dt
   <= A sqrt(s2/(2pi)) * 8 e^{-A/32} / (s2 lam)
    = (8/sqrt(2pi)) sqrt(A) e^{-A/32}  <=  3.192 sqrt(A) e^{-A/32} = P1
```

(`8/sqrt(2pi) = 3.19153... <= 3.192`, certified).

**Crossover.** By SL3.C, `[0.8 lam, t_0] c (0, 1.074 lam]`, where SL3.1(i')
gives integrand `<= e^{-s2 t^2/11.5}`. Mills with `a = s2/11.5`,
`c = 0.8 lam`: `a c^2 = 0.64 A/11.5 >= 0.0556 A` (so
`e^{-a c^2} <= e^{-0.0556 A}`, safe direction) and
`1/(2 a c) = 11.5/(1.6 s2 lam)`:

```
A sqrt(s2/(2pi)) int_{0.8 lam}^{t_0} |phi| dt
   <= (11.5/(1.6 sqrt(2pi))) sqrt(A) e^{-0.0556 A}
   <= 2.87 sqrt(A) e^{-0.0556 A} = P2
```

(`11.5/(1.6 sqrt(2pi)) = 2.86739... <= 2.87`, certified).

**Far.** On the band, `pi/m < 4/m < lam <= 0.89 <= 1.7627`, and
`t in [t_0(lam), pi]` is exactly Corollary W.5(ii)'s scope (wp1-c, PROVED):
`|phi(t)| <= exp(-m q(M_1, 1))`, `M_1 := m sinh(lam/2)`. Here
`M_1 >= m lam/2 = w/2 > 2` (`sinh y >= y`, `w > 4`), and `q(., 1)` is
nondecreasing in `M` (Lemma W.3(i), PROVED), so
`q(M_1, 1) >= q(2, 1) = 0.074126... >= 0.0741` (certified). Hence

```
A sqrt(s2/(2pi)) int_{t_0}^{pi} |phi| dt
   <= A sqrt(s2/(2pi)) * pi * e^{-0.0741 m}
    = sqrt(pi/2) (A^{3/2}/lam) e^{-0.0741 m}
   <= sqrt(pi/2)/4 * m^{5/2} e^{-0.0741 m}
   <= 0.3134 m^{5/2} e^{-0.0741 m} = P3 ,
```

using `A sqrt(s2) = A^{3/2}/lam`, then `1/lam < m/4` (band) and
`A <= m` (Lemma SL3.B), and `sqrt(pi/2)/4 = 0.31332... <= 0.3134`
(certified).

**Monotonicity + numerics.** `d/dA [ (1/2) log A - A/32 ] = 1/(2A) - 1/32
< 0` iff `A > 16`; `d/dA [ (1/2) log A - 0.0556 A ] < 0` iff
`A > 1/0.1112 = 8.99`; `d/dm [ (5/2) log m - 0.0741 m ] < 0` iff
`m > 33.74`. At `m = 401`: `P3 <= 0.3134 * 401^{5/2} e^{-29.7141}
= 1.27e-7 <= 1.3e-7` (certified), and `P3` decreases in `m` thereafter.
Under SL2's `A >= c_A(band) m >= c_A(band) * 401 >= 112.28`, the `P1`/`P2`
columns of the table follow by evaluating the (A-decreasing) bounds at
`A0 = c_A(band) * 401` (NC-SL3-1, safe-rounded up), and they decrease in `m`
at fixed band because `A0(m) = c_A m` increases in `m` while the bounds
decrease in `A` (thresholds 16 and 9 both `< 112.28`). ∎

*(Measured truth, NC-SL3-2(e), floats, labeled sanity: the true `T_u` at
`m = 401` is below `1e-5` at every sampled `w` — the analytic bound is
5–6 orders above truth at this exact geometry. That is expected: the bound
prices the integrand at its left-endpoint Gaussian envelope; the plan's
NC-PL3 exact-integer truth margin (17x on the FULL CL target) already said
the ledger only needs to land under budget, not be sharp.)*

## 7. Interface to the architected statement (deviations D1–D3, all flagged)

The architected SL3 reads: *(i) `|phi| <= exp(-s2 t^2/8)` on
`0 < t <= 0.8 lam`; (ii) `T_u <= 3.19 sqrt(A) e^{-A/32} + 0.2 +
0.36 sqrt(A) A e^{-0.0373 m}` (mid / W.6 / far), each decreasing in `m`; at
`m = 401` worst band `<= 1.01 + 0.2 + 0.01`.* What is delivered:

**(i) is PROVED as architected — on a strictly larger scope** (all `m >= 2`,
all `0 < |lam| <= 0.89`; no `w > 4` needed), by the suggested route (T.6ii
skeleton + truncated difference + M2-pattern tail domination). The route's
per-factor loss came out `eps1* = 0.35` exactly as the plan's Laplace-tail
heuristic predicted (`e^{-x}(x^2+2x+2)/2 = 0.2490` at `x = 3.927` in the
continuum; the discrete sup over `lam <= 0.89` is `0.3226`, certified
`<= 0.35`), and `(2/pi^2)(0.65) = 0.13171 > 1/8` — the plan's 6% route
margin is confirmed at 5.4% (on the constant) plus 7.8% (on the
certificate).

**(ii) is PROVED in a corrected and stronger form.** Three deviations:

- **D1 (micro-correction, mid constant).** The Mills constant is
  `8/sqrt(2pi) = 3.19154 > 3.19`; the architected `3.19` is unachievable by
  any route through this integral. Restated with `3.192`; the worst-band
  value moves `1.01 -> 1.0125` (`A0 = 0.28*401 = 112.28`). Downstream: SL5's
  W1 row total moves `+0.0025` against `0.87` of recorded slack — absorbed.

- **D2 (route replacement, crossover slot).** The architected `0.2` via
  wp1-c W.6 sup*length is NOT proved here, because the suggested route has
  a gap I could not close as specified: (a) its arithmetic
  (`0.15 A^{1.5} e^{-7.6} = 0.089` at `A = 112.3`) evaluates the prefactor
  at SL2's LOWER band bound of `A`, where an UPPER bound on `A` is what the
  inequality needs — no sub-lemma in the plan supplies band-wise upper
  bounds `A <= a_hi(w) m` (only `A <= m` is available, SL3.B, and with it
  the same arithmetic gives `0.1117 m^{1.5} e^{-E}`, needing exponent
  `E >= 8.4` at `m = 401`); and (b) the provable W.6 corner exponent I
  could extract on `[0.8 lam, t_0]` at `w -> 4+` is
  `m (1/2)(1 - 2.656/w)(0.4491 - 1.506/w) = 4.9` at `m = 401` — the
  measured `7.645` is truth, not route. Instead of repairing W.6's corner, I
  prove the SECOND TIER SL3.1(i') of the same new lemma (valid to
  `1.074 lam >= t_0(lam)`, Lemma SL3.C) and take Mills from `0.8 lam`:
  `P2 = 2.87 sqrt(A) e^{-0.0556 A} <= 0.0592` under SL2 (`<= 0.2` already
  for `A >= 90`). This is strictly below the architected `0.2` slot on the
  whole scope, so every SL4/SL5 row consuming the slot is safe (indeed
  improves by `~0.14`). wp1-c W.6 is consumed NOWHERE in this note.

- **D3 (correction, far piece).** The architected far display
  `0.36 sqrt(A) A e^{-0.0373 m}` drops a `1/lam` factor: the normalized far
  integrand is `A sqrt(s2/(2pi)) * pi = sqrt(pi/2) A^{3/2}/lam`, and
  `1/lam` is as large as `m/4` on the band (the plan's own §SL5 arithmetic
  `0.36*62*3850*3.2e-7 = 0.028` inserts `A ~ 0.024 m^2`, which no cited
  lemma provides). Repaired far piece: `P3 = 0.3134 m^{5/2} e^{-0.0741 m}`,
  using (1) the honest normalization with `1/lam < m/4`, (2) `A <= m`
  (SL3.B, new), and (3) the band-improved W.5(ii) floor
  `q(M_1, 1) >= q(2, 1) >= 0.0741` (valid since `w > 4` gives `M_1 > 2`;
  the plan's `0.0373` floor would NOT survive the lost `1/lam` factor —
  `0.3134 m^{5/2} e^{-0.0373*401} m-profile` peaks at `2.6e+0`-class — the
  doubled exponent is what restores 4+ orders of headroom).
  `P3 <= 1.3e-7 <= 0.01` for all `m >= 401`, decreasing. The architected
  far VALUE (`<= 0.01`) therefore stands; only its displayed formula needed
  repair.

**Net interface guarantee for SL4/SL5** (what may be cited from this note):
for `m >= 401`, `lam in B(m)`, under SL2's `A >= c_A(band) m`:

```
T_u <= 3.192 sqrt(A) e^{-A/32} + 0.2 + 0.01        (architected three-slot form)
T_u <= 1.072                                        (worst band, m = 401; decreasing in m)
```

both PROVED here; the sharper `P2`, `P3` displays above may be used instead,
band-wise, with the table of §6. SL5's ledger with row entries
`I1u = 3.192-column`, `I2u = 0.0592-column`, far `= 0.0000`-column has every
band total LOWER than the plan's table except W1 (`4.73 -> 4.73 + 0.0025
- 0.1408 - 0.01 = 4.58`), i.e. every row still PASSes with more room.

## 8. Scripts and verbatim outputs

Both scripts live in `g2_scripts/campaign_20260811/wp4_SL3/`; outputs
archived beside them (`out_sl3_nc1.txt`, `out_sl3_nc2.txt`), run 2026-08-12.

| # | script | validates | key output (verbatim) |
|---|---|---|---|
| NC-SL3-1 | `sl3_nc1_certificates.py` (mpmath dps 40) | every named constant of §0; Lemma SL3.A (890-interval monotone-factor certificate, both tiers); Lemma SL3.C endpoint; SL3.2 monotonicity thresholds, `P3(401)`, the band table, worst-band and three-slot roundings; the two D2 gap-documentation numbers | `SL3.A(i): max piece bound Eps(.,x1) <= 0.35  max = 0.32257... on (0.889, 0.890)`; `SL3.A(ii): ... <= 0.57  max = 0.54890... on (0.889, 0.890)`; `t0(0.89)/0.89 <= 1.074  ratio = 1.073723..., margin = 0.000276...`; `q(2,1) = 0.074126...`; `P3(401) = 1.2568e-7 <= 1.3e-7`; `W1: P1 = 1.012472... <= 1.0125`; `W1: P2 = 0.059133... <= 0.0592`; `P2 <= 0.2 already at A = 90 (= 0.18272...)`; band table as §6; `D2 note: exponent needed with A<=m only: E >= 8.408... (measured W6min = 7.645)`; `D2 note: provable W.6 corner exponent at w=4, m=401: 4.891`; final line `ALL CERTIFICATES PASS` |
| NC-SL3-2 | `sl3_nc2_sanity.py` (floats, labeled sanity) | (a) truncated-geometric variance closed form (max rel dev `2.0e-13`); (b) SL3.B `A <= m` on `m in {401, 900} x lam-grid` (`0 violations, max A/m = 0.9810`); (c) SL3.1 truth margins; (d) exact `eps_j` vs `Eps` (18 rows, all `True`); (e) true `T_u` vs bound (all bound-side) | `m=401 w=4.05: tier1 min=0.4923 ... tier2 min=0.4861` through `w=356.89: tier1 min=0.3794 ... tier2 min=0.3219` (all `>= c1`/`>= c2` True; tier1 col matches plan NC-PL4's 0.4923/0.4904/0.4794/0.4516/0.3794 exactly); `lam=0.10 j=401: eps1=0.2455<=Eps1=0.2567 True | eps2=0.4345<=Eps2=0.4517 True` (worst measured slack 4.4%); `w=4.05: T_u(true)=0.0000 bound=0.8155` (bound-side by >= 5 orders) |

*(Note on (e): the printed `bound` there evaluates P1+P2+P3 at each sample's
own `A` — e.g. `0.8155` at `w = 4.05` where `A = 121.97 > 112.28` — while
§6's table evaluates at the band's SL2 floor `A0`; both are the same bound,
the table is the band-uniform worst case.)*

## 9. Status recap

- **Lemma SL3.B** (`s2 <= m/(4 sinh^2(lam/2))`, `A <= m`): **PROVED**
  (M2 rescue lemma + one identity; all `m >= 1`, all `lam != 0`).
- **Lemma SL3.D** (per-factor truncated quadratic domination): **PROVED**
  (exact difference law + Chebyshev pairing + monotone geometric tail).
- **Lemma SL3.A** (eps-certificates `0.35`/`0.57` on `lam <= 0.89`):
  **PROVED** (finite monotone-factor interval certificate, NC-SL3-1;
  point-evaluation class, no continuum grid sampling).
- **Lemma SL3.C** (`lam <= t_0(lam) <= 1.074 lam` on `(0, 0.89]`):
  **PROVED** (convexity + one endpoint evaluation).
- **Theorem SL3.1** (i) `|phi| <= e^{-s2 t^2/8}` on `(0, 0.8 lam]`,
  (i') `|phi| <= e^{-s2 t^2/11.5}` on `(0, 1.074 lam]` — for ALL `m >= 2`,
  `0 < |lam| <= 0.89`: **PROVED**. (i) is the architected SL3(i) on a larger
  scope; (i') is new (the W.6-slot replacement).
- **Theorem SL3.2** (tail bucket `T_u <= P1 + P2 + P3`, band table,
  monotonicities; architected three-slot form `3.192/0.2/0.01` and worst-band
  total `1.0717 <= 1.22`): **PROVED**, with SL2 consumed as a form-level
  hypothesis (`A >= c_A(band) m`) exactly where per-band numbers are stated;
  the `P1/P2/P3` displays themselves are unconditional on `B(m)`, `m >= 401`.
- **Deviations from the architected statement**: D1 (mid constant
  `3.19 -> 3.192`), D2 (W.6 route replaced by tier (i') — the architected
  route as written needs an unstated band-wise `A`-upper bound; documented
  with certificates), D3 (far display corrected — missing `1/lam` factor;
  repaired via `A <= m` + the improved floor `q(2,1) = 0.0741`). All three
  are absorbed by the consumers; no SL4/SL5 row moves adversely by more than
  `+0.0025` and every row gains `>= 0.14` of new slack from D2.

*End of wp4_sl_SL3.md.*
