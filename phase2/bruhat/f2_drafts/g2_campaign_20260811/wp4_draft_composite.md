# wp4_draft_composite — the deep-tilt core lemma CL(79, 20, 0.89): assembled state

*Wave-3 ASSEMBLER deliverable, F2 campaign (Mahonian log-concavity, Theorem
A), 2026-08-12. Sources merged: `wp4_plan_20260811.md` (architect) and the
prover deliverables `wp4_sl_SL2.md`, `wp4_sl_SL3.md`, `wp4_sl_SL5.md` (each
self-reported PROVED, none yet refereed), plus the ORPHANED script evidence
`g2_scripts/campaign_20260811/wp4_SL4/sl4_nc1.py` (+ archived
`out_sl4_nc1.txt`) left by an SL4 session that produced no deliverable file.
No SL1 artifact of any kind exists. Assembler's own numeric cross-checks:
`g2_scripts/campaign_20260811/wp4_assembly/wp4asm_chain.py` (SAVED and RUN
2026-08-12, output archived as `out_wp4asm_chain.txt` beside it; quoted
verbatim in §4/§6). No existing file modified.*

**Bottom-line status: PARTIAL.** The target `CL(C_0* = 79, C* = 20,
Lambda* = 0.89)` (verbatim spec of `wp3_draft_a2.md` §6.1) is **PROVED
MODULO exactly two named hypotheses** — (H1) = the architected SL1 (core
cumulant model; no prover artifact exists) and (H4) = the architected SL4
(kernel/inversion assembly; prover session died without a deliverable). The
delivered pieces SL2, SL3, SL5 resolve cleanly into a single chain with all
constant mismatches repaired and recertified (effective constant along the
assembled chain: `C* = 16.91 <= 20` at `m >= 401`; `10.09 <= 136` at
`m >= 1581`; §4). **However** — and this must not be papered over — the
orphaned SL4 script contains a numerically documented refutation-in-progress
of the ARCHITECTED ledger normalization: the honest numerator transfer of
the tail and `R5` slots is larger than the plan's `T_u` pricing by a factor
`~ A` (mid) to `~ s2` (far), so (H4) *as architected* is very likely not
assemblable from SL1–SL3 *as architected*, and the true remaining bridge is
the larger, precisely-stated package of §5.3. The CL statement itself
remains strongly supported by measured truth (17x margin, plan NC-PL3;
none of the wave-3 evidence touches the truth side).

Per-source status ledger (each prover's OWN status; house-rule referees
pending on every wave-3 file including this one):

| piece | file | prover status | assembler's verdict after cross-check |
|---|---|---|---|
| SL1 (core model, `R31*/R42*/C5`) | — none — | **MISSING** (no file, no scripts) | open; and the orphaned SL4 evidence says its architected `C5 = 3/8` is ~16x too weak for an honest assembly (§5.2–5.3) |
| SL2 (band floor `A >= c_A(w) m`) | `wp4_sl_SL2.md` | **PROVED** (strict (i); (ii) `m`-uniform, exact-rational certificates; (iii) + bonus `min(m,s2) = m`) | consumed as delivered; no mismatch (§2 R1) |
| SL3 (Gaussian domination + tail) | `wp4_sl_SL3.md` | **PROVED** (deviations D1–D3 from the architected statement, all flagged, all safe-direction) | consumed as delivered; its sole hypothesis (SL2 form-level) is DISCHARGED by SL2 (§2 R2); D1–D3 adopted (§2 R3–R5) |
| SL4 (ratio law with ledger) | — no deliverable — | **MISSING** (orphaned script + archived output only) | open; the script's Part A *supports* the model algebra, Part B/C *refute the architected slot normalization* (§5.2) |
| SL5 (band arithmetic -> CL) | `wp4_sl_SL5.md` | **PROVED modulo (H1)–(H4)** (+ its own unconditional Lemmas SL5.0/SL5.1; two conclusion-preserving corrections to the plan) | consumed as delivered; its (H2)/(H3) are DISCHARGED by SL2/SL3 after the `3.19 -> 3.192` recompute (§2 R6, §4); its (H1)/(H4) remain the two open hypotheses |

## 0. Standing notation (harmonized; = plan §0)

`U_j^lam` (`j = 1..m`) independent, `P(U_j = i) = e^{-lam i}/z_j` on
`{0,...,j-1}`; `S_lam = sum_j U_j^lam`; `mu(lam) = E S_lam`;
`s2 = sigma_lam^2 = Var S_lam`; `kappa_r` the cumulants of `S_lam`;
`q := e^{-lam}`; `w := m lam`; `A := lam^2 s2`; `u := 1/A`. Mean-matched
tilt frame `mu(lam(k)) = k` (merged draft Lemma 3.1, cited-PROVED); mirror
`r(N-k) = r(k)`, `lam(N-k) = -lam(k)`, WLOG `lam > 0`. Centered cf
`phi(t) = E e^{it(S_lam - k)}`. Residual band
`B(m) := { lam : 4/m < lam <= 0.89 }`, `m >= 401` (so `w > 4`). `w`-bands
`W1 = (4,5]`, `W2 = (5,6]`, `W3 = (6,8]`, `W4 = (8,10]`, `W5 = (10,20]`,
`W6b = (20,40]`, `W7 = (40,infty)`, each intersected with `lam <= 0.89`;
they partition `{w > 4}` gap-free. `t_0(lam) := 2 arcsin(sinh(lam/2))`.
Split geometry of `[0, pi]`: core `[0, lam/2]`, mid `[lam/2, 0.8 lam]`,
crossover `[0.8 lam, t_0(lam)]`, far `[t_0(lam), pi]`.

Citable-established inventory (STATUS_wave2 §1/§3): wp1-c W.3–W.6; T2
T.6(i)(ii), T.4/T.5-family; merged draft Lemmas 3.1–3.4; wp3-a2 P.6/P.7/P.8;
wp2-b W.1–W.3; g1_draft_b B.5–B.8; the M2 rescue lemma
(`referee_t2_maths.md` M2). T.10(2)/T.8'' not cited by anything below.

## 1. Delivered results, restated (the resolved part of the graph)

The statements below are quoted from the prover files with the §2
harmonizations applied; proofs live in the source files. Statuses are the
provers' own; NONE has yet had its two house-rule referees.

**Theorem A2 (= SL2; `wp4_sl_SL2.md` Thm SL2.5 + Cor SL2.2 + §5). PROVED
(unrefereed).**
(i) `Var(U_{j+1}^lam) > Var(U_j^lam)` for every real `lam`, `j >= 1`.
(ii) For `m >= 401`, `|lam| in B(m)`, `w`-band `Wi`:

```
A = lam^2 s2 >= c_A(Wi) m ,
band:  W1    W2    W3    W4    W5    W6b   W7
c_A:   0.28  0.35  0.42  0.52  0.60  0.70  0.80
```

(certified floors `LBV - UBv = 0.287499 / 0.381808 / 0.462885 / 0.584512 /
0.665138 / 0.831552 / 0.852716`, exact rationals, all strictly above
`c_A`).
(iii) `s2 >= 1122800/7921 = 141.749... > 79` on all of `B(m)` (CL's
`s2 >= C_0* = 79` hypothesis never binds); `A/min(m, s2) >= c_A(w)`;
bonus: `min(m, s2) = m` on `B(m)` (W7 margin only 1.0% — flagged by the
prover as not-to-be-spent).
*Key mechanism:* the exact identity `lam^2 Var(U_j^lam) = v(j lam) - v(lam)`
with `v(x) = 1 - (x/(2 sinh(x/2)))^2`, plus a right-endpoint Riemann
comparison — zero discreteness loss; the plan's `O(lam)` discreteness budget
and W7 anchors were unnecessary.

**Theorem A3 (= SL3; `wp4_sl_SL3.md` Thms SL3.1/SL3.2 + Lemmas
SL3.A–SL3.D). PROVED (unrefereed).**
(i) *(two-tier extended Gaussian domination — valid for ALL `m >= 2`,
`0 < |lam| <= 0.89`)*:

```
|phi_lam(t)| <= exp(-c1 s2 t^2) <= exp(-s2 t^2/8)     on 0 < t <= 0.8|lam| ,  c1 = 0.1317... ;
|phi_lam(t)| <= exp(-c2 s2 t^2) <= exp(-s2 t^2/11.5)  on 0 < t <= 1.074|lam| , c2 = 0.0871... .
```

(ii) *(tail bucket, `T_u := A sqrt(s2/(2pi)) int_{lam/2}^{pi} |phi| dt`)*
On `B(m)`, `m >= 401`, unconditionally:

```
T_u <= P1 + P2 + P3 ,
P1 = 3.192 sqrt(A) e^{-A/32} ,   P2 = 2.87 sqrt(A) e^{-0.0556 A} ,
P3 = 0.3134 m^{5/2} e^{-0.0741 m} <= 1.3e-7  (m >= 401) ,
```

with `P1` decreasing in `A` for `A >= 16`, `P2` for `A >= 9`, `P3`
decreasing in `m >= 34`. Combined with Theorem A2(ii) (which discharges
SL3's only hypothesis — §2 R2), the per-band worst case at `m = 401` is
`T_u <= 1.0125 + 0.0592 + 1.3e-7 <= 1.072` (band W1; smaller elsewhere,
decreasing in `m`); the architected three-slot interface
`T_u <= 3.192 sqrt(A) e^{-A/32} + 0.2 + 0.01` holds a fortiori.
*Also delivered:* Lemma SL3.C (`lam <= t_0(lam) <= 1.074 lam` on
`(0, 0.89]`) and Lemma SL3.B = Lemma C.1 below.

**Lemma C.1 (tilt–variance cap; = SL3.B = SL5.0, and a corollary of SL2.0.
PROVED three independent ways (unrefereed).** For every `m >= 1` and real
`lam != 0`:

```
s2 <= m/(4 sinh^2(lam/2)) ,   hence   A = lam^2 s2 <= m h(lam) < m ,
h(lam) := (lam/2)^2 / sinh^2(lam/2) .
```

*Proofs:* (a) M2 rescue lemma + geometric-variance identity
(`wp4_sl_SL3.md` §1); (b) same, with M2 reproved inline in three lines
(`wp4_sl_SL5.md` §1); (c) immediately from SL2's exact identity
`lam^2 Var(U_j) = h(lam) - h(j lam) <= h(lam)` and `h < 1` on `x != 0`
(`wp4_sl_SL2.md` Lemmas SL2.0/SL2.1 — noted here as the shortest route).
New to the campaign, independently useful (it retires crude `A`-caps:
B.0(i) is consumed NOWHERE in wp4 — see §2 R5). Flagged for referee reuse.

**Theorem A5 (= SL5; `wp4_sl_SL5.md` Thms SL5.2/SL5.3 + Lemma SL5.1).
PROVED MODULO (H1)–(H4) (unrefereed); after §2, modulo (H1) and (H4) only.**
Under (H1) [= architected SL1: banded `R31*/R42*` scales and core remainder
`|R5(t)| <= C5 s2 t^5/lam^3` on `[0, lam/2]`, `C5 = 3` (`lam <= 1/2`) / `8`
(`1/2 < lam <= 0.89`)] and (H4) [= architected SL4: for `m >= 401`,
`lam(k) in B(m)`, `s2(r(k)-1) = 1 + theta L(W, A, m) u`, `|theta| <= 1`,
with the seven-slot ledger `L = R42*/2 + 0.3(R31*)^2 + 6.4 C5/sqrt(A) +
midslot + crossslot + 1.0 + farslot`], with the tail slots as delivered by
Theorem A3(ii): for every band and every `m >= 401`, every
`A in [c_A(W) m, m]` (lower end by Theorem A2(ii), upper end by Lemma C.1):

```
L(W, A, m) <= T(W) <= 20 c_A(W) <= 20 A/min(m, s2) ,
```

(certified table recomputed with the harmonized constants in §4 — all seven
rows PASS, worst margin `0.8655` on W1), and hence

```
s2 (r(k) - 1) = 1 + theta' * 20/min(m, s2) ,  |theta'| <= 1 ,
r(k) - 1 >= (1 - 20/min(m, s2))/s2 ,
```

for every interior `k` with `|lam(k)| in (4/m, 0.89]`, `m >= 401` — i.e.
**CL(79, 20, 0.89) verbatim**, both signs via the mirror, the `s2 >= 79`
clause never binding (Theorem A2(iii)).

## 2. Dependency-graph resolution (what plugged into what, and every mismatch)

The architected graph was `SL1, SL2, SL3 (independent) -> SL4 -> SL5 -> CL`.
Resolution of every edge, with each mismatch found and how it is settled:

- **R1 (SL2 -> SL3, SL5): clean.** SL3 consumed exactly
  `A >= c_A(band) m` form-level; SL5 consumed (H2) = SL2(ii)+(iii). SL2
  delivers both verbatim (and strictly more: strict (i), zero-discreteness
  (ii), the `min(m,s2) = m` bonus). *Discharged.*
- **R2 (SL3's hypothesis): discharged.** SL3's per-band table was stated
  "under SL2's hypothesis"; SL2 is delivered, so Theorem A3's band numbers
  are now unconditional on `B(m)`, `m >= 401`.
- **R3 (mid-constant mismatch, D1): repaired by recompute.** SL5's
  certified table used the architected mid constant `3.19`; SL3 proves the
  slot only with `3.192` (`8/sqrt(2pi) = 3.19154 > 3.19`; the architected
  value is unachievable through this integral). Assembler recomputation of
  the full table with `3.192` in exact rationals (§4, script [1]): every
  entry moves by `<= +0.000634` (W1), all seven rows still PASS, worst
  margin `0.8662 -> 0.8655`. *(H3)-as-consumed is thereby replaced by
  (H3)-as-delivered everywhere.*
- **R4 (crossover slot): strengthened.** SL5 consumed the architected W.6
  slot `0.2`; SL3 delivers `P2 <= 0.0592` (worst band) via its new second
  tier + Lemma SL3.C, and wp1-c W.6 is consumed NOWHERE in wp4 anymore
  (SL3's D2: the architected W.6 route needs a band-wise upper `A`-cap no
  sub-lemma supplies, plus its provable corner exponent is 4.9 vs the
  needed 8.4-class). Both the `0.2` form (a fortiori) and the sharper
  per-band column are available; §4 certifies both variants.
- **R5 (far slot): doubly repaired, doubly covered.** The architected far
  display `0.36 sqrt(A) A e^{-0.0373 m}` was wrong twice over — it drops a
  `1/lam` factor (SL3's D3), and its suggested certification route via
  B.0(i)'s cap `A <= 0.024 m^3` evaluates to `221.3` at `m = 401`, not
  `0.028` (SL5's §1.1: the plan's printed numbers trace to `0.024 m^2`, a
  slip; that route only closes from `m = 692`). Both provers independently
  repaired it via Lemma C.1 (`A <= m`): SL5.1(iii) certifies the
  architected-form slot `<= 9.229e-4 <= 0.01` for all `m >= 401`; SL3's
  honest normalization gives `P3 <= 1.3e-7`. The composite uses `0.01`
  (either certification suffices); B.0(i) is dropped from the wp4
  dependency list entirely.
- **R6 (SL5's quantifier correction): adopted.** The plan's SL5(i) clause
  "for all `A >= c_A m`, each `L`-entry nonincreasing in `A`" is false for
  the far entry (increasing in `A`); SL5's corrected quantification
  `A in [c_A(W) m, m]` is adopted, and every actual `(k, m)` pair lies in
  that range (Theorem A2(ii) + Lemma C.1).
- **R7 (duplicate lemma): harmonized.** SL3.B and SL5.0 are the same
  statement, proved independently (and SL2's identity gives a third proof);
  merged as Lemma C.1, single name, all three sources citable.
- **R8 (plan-headroom erratum, from SL2): recorded.** NC-PL1's W1
  band-minimum `0.3189` was a grid artifact (value at `w = 4.2`); the true
  W1 infimum is `~0.2992` as `w -> 4+`, so W1 truth headroom over
  `c_A = 0.28` is 6.4%, not ~14%. `c_A = 0.28` still certified (floor
  `0.287499`). No constant moves; the plan's "10–14% headroom on every
  band" should read "6.4% on W1, 10–14% elsewhere".
- **R9 (scope bonuses, recorded):** Theorem A3(i) holds for ALL `m >= 2`,
  `0 < |lam| <= 0.89` (not just `m >= 401`, `w > 4`); Theorem A2(i) is
  strict and holds for all real `lam`. Nothing downstream needs the larger
  scope, but referees should know the statements are not band-limited.
- **R10 (the two unresolved nodes):** (H1) has NO prover artifact; (H4) has
  no deliverable, only the orphaned script — whose content BEARS ON the
  architected form of (H4) itself. See §5.

Post-resolution graph: `[Thm A2 PROVED] + [Thm A3 PROVED] + [Lemma C.1
PROVED] --> [Thm A5 = CL, PROVED modulo (H1) and (H4)]`, with (H1), (H4)
stated verbatim in §5.1 and their honest prospects in §5.2–5.3.

## 3. The assembled statement and proof

**Theorem CL-composite (conditional).** *Assume (H1) and (H4) of §5.1. Then
for every `m >= 401` and every interior `k` whose mean-matching tilt
satisfies `|lam(k)| in (4/m, 0.89]`:*

```
s2 (r(k) - 1) = 1 + theta * C*/min(m, s2) ,   |theta| <= 1 ,   C* = 20 ,
```

*and in particular `r(k) - 1 >= (1 - 20/min(m, s2))/s2`. Moreover
`s2 >= 141.749 > 79` for every such `k`, so this is the full
`CL(C_0* = 79, C* = 20, Lambda* = 0.89)` of `wp3_draft_a2.md` §6.1 —
two-sided form, lower-bound form included, both tilt signs. Along the
assembled chain the constant actually delivered is `C*_eff = 16.909 < 20`
(§4), i.e. the budget carries 15.5% assembly headroom.*

*Proof.* WLOG `lam = lam(k) > 0` (mirror: `r(N-k) = r(k)`,
`lam(N-k) = -lam(k)`, `s2` invariant — §0 frame; the exact center `lam = 0`
for `N` even sits outside the band and is covered upstream by g1_draft_b
B.8/Cor B.9, per STATUS_wave2 §2b R4-note). Let `W` be the unique `w`-band
containing `w = m lam`. By (H4),
`s2(r(k)-1) = 1 + theta L(W, A, m) u` with `|theta| <= 1`. By Theorem
A2(ii), `A >= c_A(W) m`; by Lemma C.1, `A <= m`; so `A in [c_A(W) m, m]`
and the recertified ledger inequality of §4 (Theorem A5 with (H1)'s
constants, (H3)-as-delivered tail slots, exact-rational certification)
gives `L(W, A, m) <= T(W) <= 20 c_A(W)`. By Theorem A2(iii),
`A >= c_A(W) min(m, s2)`. Chaining,

```
|theta| L u <= 20 c_A(W)/A <= 20 c_A(W)/(c_A(W) min(m, s2)) = 20/min(m, s2) ,
```

which is the display with `theta' = theta L u min(m,s2)/20`, `|theta'| <= 1`.
The variance floor `s2 >= 1122800/7921 > 79` is Theorem A2(iii); the
lower-bound form is the `theta' = -1` worst case. ∎

*(Everything in this proof except (H1) and (H4) is delivered and
script-certified: Theorem A2, Theorem A3, Lemma C.1 are PROVED (unrefereed)
above; the table inequality is recertified in §4 with the harmonized
constants. The proof is Theorem SL5.3's, with citations re-pointed to
delivered results and the recomputed table substituted for SL5's
3.19-flavor table.)*

**Remark C.2 (min(m,s2) = m).** By Theorem A2(iii)-bonus, `min(m, s2) = m`
on the whole band (`s2 > m`, W7 margin 1.0%), so CL may be read with error
term exactly `20/m`; the `min(m, s2)` form is kept because it is the spec
verbatim. Not spendable as headroom (SL2's caution).

**Remark C.3 (P.8-consistency).** The scope `lam <= 0.89` covers everything
Theorem S's R2 row sends: `c = 7/10` clause cap `log(17/7) <= 0.8874 <=
0.89`; for `m >= 1581` the `c = 1` clause caps at `log 2 <= 0.6932`. Both
certified by exact partial-sum comparisons (SL5's NC-SL5-1 [4]). So if
(H1)+(H4) land, Theorem S's last condition is met verbatim and Theorem A =
F2(a) closes per STATUS_wave2 §4 chain.

## 4. The assembled constant chain, recertified end-to-end

Assembler script `wp4_assembly/wp4asm_chain.py` (exact `Fraction`
end-to-end for [1]–[3]; safe-direction rounding: `e^{-x} <= 1/P_140(x)`
partial sums, `sqrt` via exact squaring; output archived,
`out_wp4asm_chain.txt`). Ledger slots: `k4/2 = R42*/2`,
`0.3(R31*)^2`, `R5 = 6.4 C5/sqrt(A0)` [(H1) constants `C5 = 3/8`],
`I1u = 3.192 sqrt(A0) e^{-A0/32}` [Theorem A3, D1-corrected],
`I2u` [architected `0.2` slot, delivered a fortiori by A3; variant 2 uses
A3's sharper `P2`], `slop = 1.0` [(H4)'s own property], `far = 0.01`
[Lemma SL5.1(iii) + Lemma C.1; A3's `P3 <= 1.3e-7` a fortiori]; worst case
`A0 = c_A(W) * 401` justified by SL5.1's monotonicity + Lemma C.1 (§2 R6).
Verbatim output, variant [1] (the composite's operative table):

```
 band          c_A    A0      k4/2   0.3R31^2  R5<=    I1u<=   I2u<=   slop  far<=    total<=   C*c_A   margin   T/c_A
 W1 (4,5]      0.28   112.28  0.400   0.300   1.8120 1.012473 0.200000  1.0     0.01   4.7345    5.60   0.8655  16.909 PASS
 W2 (5,6]      0.35   140.35  0.700   0.432   1.6207 0.470848 0.200000  1.0     0.01   4.4335    7.00   2.5665  12.667 PASS
 W3 (6,8]      0.42   168.42  1.300   0.675   1.4795 0.214543 0.200000  1.0     0.01   4.8790    8.40   3.5210  11.617 PASS
 W4 (8,10]     0.52   208.52  1.750   0.867   1.3297 0.068182 0.200000  1.0     0.01   5.2249   10.40   5.1751  10.048 PASS
 W5 (10,20]    0.60   240.60  2.600   1.200   1.2379 0.026876 0.200000  1.0     0.01   6.2748   12.00   5.7252  10.458 PASS
 W6b (20,40]   0.70   280.70  3.000   1.323   1.1460 0.008292 0.200000  1.0     0.01   6.6873   14.00   7.3127   9.553 PASS
 W7 (40,inf)   0.80   320.80  3.300   1.452   2.8586 0.002532 0.200000  1.0     0.01   8.8231   16.00   7.1769  11.029 PASS
  all rows PASS: True;  effective C* = max_W T(W)/c_A(W) = 16.9088 (exact 4734473/280000)  vs budget 20
```

Variant [2] (SL3's sharper `P2` column + `P3 = 1.3e-7`): all rows PASS,
`C*_eff = 16.3700` (exact `458360713/28000000`). Variant [3] (`m >= 1581`
worst case, relaxed budget `C* <= 136` per wp3-a2 §6.1): all rows PASS,
`C*_eff = 10.0809` vs 136 — 13.5x headroom. D1-impact isolated
(script [1b]): `I1u(3.19) = 1.011838 -> I1u(3.192) = 1.012473`, delta
`+0.000634`, absorbed by W1's `0.8655` margin. **Conclusion: the constant
chain of §3, GRANTED (H1)+(H4), is arithmetically sound with `C*_eff =
16.91 <= 20` — the spec's `C* = 20` is met with margin, and SL5's original
certification survives the `3.19 -> 3.192` repair unchanged in verdict.**

## 5. What remains (the honest part — no papering over)

### 5.1 The two formally missing hypotheses (smallest bridge, as architected)

**(H1) [= SL1, verbatim from the plan; no prover artifact exists].**
*For `m >= 401`, `lam in B(m)`:*
(i) `|kappa_3(lam)| <= R31*(w) s2/lam`, `|kappa_4(lam)| <= R42*(w) s2/lam^2`
with the banded scales `R31* = 1.0/1.2/1.5/1.7/2.0/2.1/2.2`,
`R42* = 0.8/1.4/2.6/3.5/5.2/6.0/6.6` (W1..W7);
(ii) for real `0 <= t <= lam/2`:
`log phi(t) = -s2 t^2/2 - i kappa_3 t^3/6 + kappa_4 t^4/24 + R5(t)`,
`|R5(t)| <= C5 s2 t^5/lam^3`, `C5 = 3` for `lam <= 1/2` (all of W1..W6b at
`m >= 401`), `C5 = 8` for `1/2 < lam <= 0.89`. *Status: CONJECTURED
(plan-level, numerics-verified: NC-PL1 band sups clear (i) with 8–23%
headroom; NC-PL4 measured `C5(0.5 lam) = 0.0083–0.2104` vs stated 3/8).*

**(H4) [= SL4, harmonized form; prover session produced no deliverable].**
*For `m >= 401`, `lam = lam(k) in B(m)`, `k` interior, assuming (H1) +
Theorems A2/A3:*
`s2 (r(k) - 1) = 1 + theta L(W, A, m) u`, `|theta| <= 1`, with

```
L = R42*/2 + 0.3 (R31*)^2 + 6.4 C5/sqrt(A) + 3.192 sqrt(A) e^{-A/32} + 0.2 + 1.0 + 0.01
```

(tail slots = Theorem A3's delivered interface; `1.0` = SL4's own assembly
slop containing the phase-cube expansion, ratio-algebra second order, and
R-extension buckets, with a certified split; the main term `eta` computed,
not bounded, to relative `O(u^2)`). *Status: CONJECTURED — and see §5.2:
the orphaned evidence indicates this exact form is NOT reachable from
(H1) + A3 as stated; the honest bridge is §5.3.*

Formally, §3 + §4 prove: **(H1) & (H4) ==> CL(79, 20, 0.89), with
`C*_eff = 16.91`.** That is the smallest bridging pair under the
architected normalization.

### 5.2 The orphaned SL4 evidence: the architected ledger normalization is refuted

`wp4_SL4/sl4_nc1.py` (+ archived `out_sl4_nc1.txt`, run 2026-08-12, no
accompanying deliverable) is an UNREFEREED mid-session artifact; it is
nevertheless the only SL4 work product, and its Part B is titled
"refutation of the architected ledger normalization". Assembler's reading,
with the key archived output quoted verbatim and re-sized independently in
`wp4asm_chain.py` [4]:

1. **What it supports (Part A).** The Hermite closed forms for the model
   integrals `qhat(d)` and the computed main term `eta` check out
   (`closed-vs-quad qhat rel err max = 6.6e-31`-class at four `w`), with
   measured `|eta|/u = 0.407/0.617/0.892/0.963` at `w = 4.5/7/30/200` —
   all BELOW the plan's `k4/2 + 0.3(R31*)^2` pricing (0.70–4.75 per band).
   The model-algebra core of (H4) is numerically sound.
2. **What it refutes (Part B).** In the numerator transfer of
   `D = p(k)^2 - p(k-1)p(k+1)`, first-order tail errors enter through the
   kernel combination `2 delta_0 - delta_+ - delta_-` — weight
   `s2 (1 - cos t)`-class — NOT at the plan's `T_u` normalization. Honest
   entries (archived output): mid slot at `gamma = 1/8` (= A3's proven
   exponent) is `129.86` at W1 vs the architected `1.012` — "`ratio =
   128.3`", i.e. `~A` times larger (assembler reproduction: `129.86`,
   ratio `128.3`, script [4]); far slot at `w = 4.05, m = 401` is `1191`
   u-units vs the architected `1.37e-4` (`~s2` times larger). The `R5`
   slot similarly transfers at `~16.3x` the architected `6.4 C5/sqrt(A)`
   (assembler script [4]: `29.47` vs `1.81` at `C5 = 3`, W1).
3. **Consequence.** With (H1)'s `C5 = 3/8` and A3's proven `gamma =
   0.1317`, the honest W1 ledger row is `>~ 130` vs budget `5.6`: **(H4)
   in the §5.1 form cannot be assembled from (H1) + A2 + A3 as stated.**
   The orphan's Part C confirms: under the STATED SL1–SL3, no band closes
   by `m = 40000` except W6b (`M* = 34868`).
4. **What still closes (Part C, strengthened-but-true constants).** With
   banded `C5* = 0.05/0.06/0.08/0.10/0.15/0.25/0.80` and mid exponents
   `gamma* = 0.42/0.42/0.40/0.40/0.38/0.34/0.32` (all TRUE per measured
   truth: `C5`-truth `0.0083–0.2104`, mid-exponent truth `0.3794–0.4923` —
   NC-PL4/NC-SL3-2), the honest ledger at `m = 401` PASSes W2–W6b (totals
   `3.75–13.68` vs budgets `7.0–14.0`) and fails exactly:
   - **W1 far sliver**: the honest far entry with the orphan's crude
     exponent floor (`m qW = 20.23` at `w = 4.05`) is `1.19e3`; W1 passes
     only for `w >= 4.51` at `m = 401`, improving to `w >= 4.05` by
     `m = 560` (orphan's grid; the `w -> 4+` edge persists slightly longer
     under that floor — A3's `w`-uniform floor below removes the
     `w`-dependence).
     Assembler re-sizing with A3's SHARPER certified floor
     (`0.0741 m = 29.71` at `m = 401`) shrinks this decisively (script
     [4]): honest far entry `0.32–0.98` at `m = 401` (cap-dependent),
     `<= 0.05` from `m = 432–450`. **The residual hole is a finite
     trapezoid `w in (4, ~4.5], m in [401, ~450]`** (orphan's cruder
     floor: `~560`), closable in principle by a harness extension
     (`~m^3` scaling; the 400-harness took 321 s, so `m ~ 450` is hours,
     not weeks — STATUS_wave2 §2 quoted "minutes" for 540 on part-(c)
     rows; the CL-truth check class is heavier but same scaling).
   - **W7 rebalance**: orphan total `19.171` vs budget `16.0` — but its
     main-term pricing there is the crude `R42/2 + R31^2 + 0.1 = 8.24`;
     with the plan's computed-eta pricing (`k4/2 + 0.3 R31*^2 = 4.75`,
     supported by Part A's measured `|eta|/u <= 0.963`) the row lands
     `~15.7 < 16.0`. Likely recoverable without new constants; needs the
     real SL4 write-up to certify.

### 5.3 The honest smallest bridge (assembler's precise restatement)

In light of §5.2, the bridge that a wave-4 session should actually prove
(statuses: all CONJECTURED, each numerically supported, none contradicted
by any measurement):

**(SL1') Core model, truth-level banded `C5*`.** As (H1), but with
(ii)'s remainder constant banded:
`C5* = 0.05/0.06/0.08/0.10/0.15/0.25/0.80` (W1..W7)
(measured truth `0.0083` at W1 up to `0.2104` at W7 — 3.8x–6x headroom;
the architected route's crude-Cauchy constant `C5 = 3` is ~16x too weak
under the honest normalization at W1, where the measured slack is largest).

**(SL3') Mid-exponent upgrade.** `|phi_lam(t)| <= exp(-gamma*(W) s2 t^2)`
on `[lam/2, 0.8 lam]` with `gamma* = 0.42/0.42/0.40/0.40/0.38/0.34/0.32`
(measured truth `0.4923/0.4904/0.4794/0.4516/~0.45/~0.40/0.3794`; A3's
proven route constant is `0.1317` — the route's per-factor loss
`eps1* = 0.35` must drop to `~0.10`-class on W1–W4, e.g. by keeping the
`sin^2` beyond the first truncation point instead of discarding it, or by
a direct log-convexity argument on the factor product; this is the
genuinely new analysis).

**(SL4') Kernel-weighted assembly.** As (H4) but with the honest slots:

```
L' = eta-price + cube + cross + R5' + mid' + X' + far' + den + quad ,
eta computed (|eta| <= [k4/2 + 0.3 R31*^2 + 1/(2 s2)] u certified);
R5'  = 38.30 C5* e / sqrt(A) ,        mid' = sqrt(2/pi) A^{3/2} e^{-gamma* A/4} (1 + 2/(gamma* A)) / (2 gamma*) ,
far' = sqrt(2pi) m s2max^{3/2} e^{-0.0741 m}  (s2max = min(m/(4 sinh^2(lam/2)), ...)) ,
```

(the orphan's `band_total` shape; exact constants to be fixed by the
prover) with per-band totals `<= 20 c_A(W)` — the orphan's Part C shows
this closes on W2–W6b at `m = 401` and on W1 for `w >= 4.51`, and W7
closes with computed-eta pricing.

**(SL-sliver) The W1 far sliver.** For `w in (4, 4.51]` and
`401 <= m <= ~450` (A3-floor sizing; `~560` under the cruder floor): either
(a) a sharpened far bound on `[t_0(lam), pi]` for `lam ~ 4/m`-class tilts
(this corner is SMALL-tilt: `lam <= 4.51/401`, where T2's T.9-final
machinery and wp2-b's envelopes live — plausibly the bound already exists
in the small-tilt inventory and only needs transfer to the CL normalization),
or (b) an exact-harness extension from 400 to `~450` (same C1–C6 checks;
`m^3` scaling from the 321 s / 400 run), which would close the sliver
FINITELY and shift CL's threshold statement to "analytic for the rest".

**Referee debt (house rule).** Two referees are owed on EACH of:
`wp4_sl_SL2.md`, `wp4_sl_SL3.md`, `wp4_sl_SL5.md`, and this composite.
Thin certified margins flagged by the provers for referee attention:
`t_0(0.89)/0.89 = 1.073724` vs `1.074` (2.8e-4); `c2 = 0.0871362` vs
`1/11.5` (0.2%); SL3's exact `eps_j` slack 4.4% worst; SL2's W7
`min(m,s2) = m` margin 1.0%; SL5's W1 row margin 0.8655 (recomputed).

**What is NOT in doubt:** the truth of CL itself. The plan's exact-integer
ground truth (NC-PL3): `max eps * min(m, s2) = 1.1696 (m = 120), 1.1710
(m = 200)` vs the asked 20 — a 17x margin; nothing in wave 3 (including
the orphaned refutation, which concerns only the ROUTE's normalization)
moves the truth side.

## 6. Script table (assembler's own; all SAVED and RUN, outputs archived)

| # | script (`g2_scripts/campaign_20260811/wp4_assembly/`) | validates | key output (verbatim) |
|---|---|---|---|
| ASM-1 | `wp4asm_chain.py` [1] | §4 operative table: harmonized slots (3.192/0.2/0.01), exact Fractions, `m >= 401` | `all rows PASS: True; effective C* = max_W T(W)/c_A(W) = 16.9088 (exact 4734473/280000) vs budget 20` |
| ASM-2 | same, [2] | sharper SL3 slots (P2-band, 1.3e-7) | `all rows PASS: True; effective C* = 16.3700` |
| ASM-3 | same, [3] | `m >= 1581` worst case vs relaxed budget | `all rows PASS: True; effective C* = 10.0809 vs budget 136` |
| ASM-4 | same, [1b] | D1 (`3.19 -> 3.192`) impact isolation | `I1u(3.19) = 1.011838 -> I1u(3.192) = 1.012473; delta = 0.000634` |
| ASM-5 | same, [4] (labeled ESTIMATES, floats) | sizing of the orphaned SL4 finding under A3's sharper far floor | `honest mid entry, W1 ... gamma=1/8 -> 129.86 (architected slot 1.0125; ratio 128.3, ~A x)`; `honest R5 ... C5=3 ... 29.47 (architected 1.81; ratio 16.3)`; `honest far entry ... w=4.05, m=401 ... 0.3229 / 0.9758` (cap-dependent); `honest-far sliver (<=0.05) closes at m = 432 / 450` |

(Consumed archived outputs quoted above: `wp4_SL2/out_sl2_e*.txt`,
`wp4_SL3/out_sl3_nc*.txt`, `wp4_SL5/out_sl5_nc*.txt`,
`wp4_SL4/out_sl4_nc1.txt`, `wp4_plan/out_wp4plan_nc*.txt` — each quoted as
its own file's claim, per source.)

## 7. Status recap (assembler)

- **CL(79, 20, 0.89): PARTIAL** — PROVED MODULO (H1) + (H4) (§3), with the
  delivered three-fifths of the graph (SL2, SL3, SL5 + Lemma C.1) resolved,
  harmonized, and recertified end-to-end (`C*_eff = 16.91 <= 20` at
  `m >= 401`; `10.08 <= 136` at `m >= 1581`).
- **(H1)/SL1: MISSING** (no artifact). **(H4)/SL4: MISSING** (orphaned
  script only) — and the orphan's evidence means the architected (H1)+(H4)
  pair should be replaced by §5.3's honest bridge (SL1' + SL3' + SL4' +
  SL-sliver) in the next wave's assignments.
- **New independently useful results delivered en route** (flag to
  referees): Lemma C.1 (`A <= m h(lam) < m`, three proofs); Theorem A3(i)
  two-tier Gaussian domination on the `lam`-scale for all `m >= 2`; SL2's
  exact identity `lam^2 Var(U_j^lam) = v(j lam) - v(lam)` (zero-discreteness
  band floors).
- **Nothing in this file is refereed.** House rule: two referees per
  deliverable, still owed on all four wave-3 files.

*End of wp4_draft_composite.md.*
