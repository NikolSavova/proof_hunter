# Adversarial math review — F2 upgrade of main.tex (2026-08-12)

*Read-only review pass, math-vs-ledger, on `main.tex` (post-F2-upgrade) +
`change_log_20260812.md`. Ground truth read in authority order:
`STATUS_wave5.md` (§4 permitted claim, §3 bottom line),
`CL_composition_20260812.md` (Theorem CL-C, §4 verbatim (S1)–(S4)),
`theoremA_assembly_20260811.md` (reduction, constants, frozen CL spec),
`wp4_draft_composite.md` §0 (band/tilt frame), and the harness results
(`harness_m560/results_m560.txt`, `wave2_repairs/results_m540.txt`).
No file other than this report was created or modified; `main.tex` was
compiled only as a copy in the session scratchpad.*

**VERDICT: MINOR_FINDINGS** — no math-vs-ledger discrepancy, no
overclaim, no stale claim, no broken cross-reference. Three minor
wording/scope items below, none touching a constant, bound, or claim
status.

---

## 1. Findings

### F1 (minor — range phrasing): "for every $m\le560$" overstates the computed range at the trivial end
- **Where:** `main.tex:72–73` (abstract: "determine the global minimum
  exactly, in integer arithmetic, for every $m\le560$");
  `main.tex:151–152` (contribution (iii): "determined exactly, in integer
  arithmetic, for every $m\le560$"); `main.tex:643–645` (§6 preamble:
  "has been computed exactly for every $m\le560$").
- **Why wrong (mildly):** the exact computation covers $4\le m\le560$
  (harness header: "m = 4..560"; 557 rows). For $m\le3$ nothing was
  computed, and at $m=2$ the quantity is undefined (no interior index —
  $r_m$ is a min over an empty set). Theorem 6.2 itself is correctly
  scoped ($5\le m\le560$ plus the $m=4$ exception), so this is
  display-level only.
- **Fix:** write "for every $4\le m\le560$" (or "...for every
  $m\le560$ (from $m=4$)") in the three display sentences.

### F2 (nano — wording): "Exact verification of Conjecture CL itself at $m=401$ and $m=402$"
- **Where:** `main.tex:876–878` (inside the (S4) bullet of
  Remark 6.9/`rem:S-evidence`).
- **Why wrong (technically):** Conjecture 6.3 as stated is scoped
  $m\ge561$; what was verified at $m=401/402$ is the conjecture's
  displayed estimate outside its stated scope. Substance is correct and
  honest per the ledger (REF-B: 260 adversarial interior $k$, 0
  violations, 17.1$\times$ margin — the paper's "17$\times$" and "260
  adversarially chosen" are both the safe/honest readings).
- **Fix:** "Exact verification of the estimate of
  Conjecture~\ref{conj:CL} at $m=401$ and $m=402$..." (or "of the
  core-lemma inequality").

### F3 (observation, optional): (S2) slack reported without the W1 non-uniformity caveat
- **Where:** `main.tex:864–866` ("the slack over $C_5$ ranges from a
  factor $1.6$ to a factor $8$ depending on the band").
- **Why noted:** the composition note's §4 carries a fine-grained caveat
  ("W1's slack is $w=4.30$-class, NOT uniform to the band edge"). The
  paper's sentence matches the ledger's own summary-level presentation
  (1.6x–8x), so this is NOT an overclaim; flagged only because the house
  style is maximal honesty. Optional fix: append "as measured at
  interior probe points".

No other findings. In particular the one judgment call the change log
flags (item 7.2: Proposition 6.8 presenting (S1)–(S4) $\Rightarrow$ CL as
established while the composition note still owes its unit referee pass)
is exactly the STATUS_wave5 §4 permitted claim, is disclosed to the
co-authors in the change log, and the paper cites no internal campaign
file — reviewed and accepted as within the mandate.

## 2. Math-vs-ledger verification (all PASS)

Every new mathematical statement checked against ground truth; every
recomputable number recomputed (exact `Fraction` arithmetic where the
source is exact):

1. **Conjecture 6.3 = CL(79, 20, 0.89):** display matches the frozen
   spec (`theoremA_assembly` §3) verbatim in substance —
   $r_m(k)-1 = s^{-2}(1+\theta\,20/\min(m,s^2))$, $|\theta|\le1$; scope
   $m\ge561$, $s^2\ge79$, $4/m<\lambda\le0.89$ matches Theorem CL-C
   (`CL_composition` §2, $|\lambda|\in(4/m,0.89]$ modulo the paper's
   declared WLOG $\lambda\ge0$ mirror frame, which the paper states).
   The follow-up remark's facts check: $1122800/7921 = 141.7498 > 141$
   (composite A2(iii)); lower-bound half only (assembly §3); needed from
   $m\ge401$ with $[401,560]$ discharged by the exact computation — the
   consumer-level discharge, phrased as discharging *the need*, matching
   the composition §0 distinction.
2. **(S1)–(S4) (Conjecture 6.7) vs `CL_composition` §4:** statement for
   statement equivalent. (S1): $\tilde\kappa_3\le R_3$,
   $\tilde\kappa_4\le R_4$ with $\tilde\kappa_3=|\kappa_3|\lambda/s^2$,
   $\tilde\kappa_4=\kappa_4\lambda^2/s^2$ — algebraically identical to
   the ledger's $|\kappa_3|\le R31^*s^2/\lambda$,
   $\kappa_4\le R42^*s^2/\lambda^2$ ($\lambda>0$ on the stated range).
   (S2): the paper's single-inequality form is exactly the ledger's
   $R_5$-form ($R_5 = \log\varphi + s^2t^2/2 + i\kappa_3t^3/6
   - \kappa_4t^4/24$; signs match the standard cumulant expansion), on
   $[0,\lambda/2]$; the added continuous-branch clause is a harmless
   well-definedness addition. (S3): $\tilde\kappa_3^2-\tilde\kappa_4/2
   \le J_0$ = the ledger's $J = r31^2 - r42/2 \le J_0(W)$. (S4):
   $|s^2(r_m(k)-1)-1|\le0.89$, verbatim. Scope $m\ge561$,
   $\lambda\in(4/m,0.89]$ on all four — verbatim.
3. **Table 4 constants:** $R_3$, $R_4$, $C_5$, $J_0$ rows all verbatim
   from `CL_composition` §4 (all 28 entries digit-checked). Consistency
   recompute: $J_0(W) < J^*(W) = R_4/2 + 0.3R_3^2$ on all seven bands
   ($0.7/1.132/1.975/2.617/3.8/4.323/4.752$), matching the composition's
   block [E] identity $J_0 = J^* - REM^*$. Caption's "six-digit displays
   of exact rationals archived" matches the ledger.
4. **Band partition:** $\mathcal W_1$–$\mathcal W_7$ = (4,5], (5,6],
   (6,8], (8,10], (10,20], (20,40], (40,$\infty$), each $\cap\{\lambda\le
   0.89\}$ — verbatim `wp4_draft_composite` §0 (W6b $\to\mathcal W_6$ is
   a pure relabel, same interval). Tilt frame ($P(U_j^\lambda=i)\propto
   e^{-\lambda i}$ on $\{0,\dots,j{-}1\}$, $\mu'=-\mathrm{Var}<0$,
   mean-matching, $\varphi(t)=\mathbb Ee^{it(S_{\lambda(k)}-k)}$, mirror,
   $\omega=m\lambda$) matches the composite frame exactly.
5. **Proposition 6.8:** "(S1)–(S4) imply CL; composed chain delivers
   18.23 in place of 20 for every $m\ge561$" — Theorem CL-C verbatim in
   substance; $20\times0.911407 = 18.22814 \to 18.23$ (correct rounding
   of the chain-verified $C^*(m\ge561)=18.2281\le20$, `ALL CHECKS PASS`
   on disk). The assembly paragraph's role assignment ((S1)+(S3) main
   term, (S2) core remainder, (S4) seed closing with strict contraction)
   matches CL-C proof steps 1–5.
6. **Theorem 6.5 (conditional F2):** matches assembly §0/§2.4. Two-sided
   display with closed-flavor $C_A = 37997.85$ (valid all $m\ge401
   \supset m\ge561$; display rounds the exact 37997.8442 in the safe
   direction), UB $1.8/m^2$ unconditional $m\ge180$, $r_m-1\sim36/m^3$
   ($\sigma^2\sim m^3/36$ — checked). Conditionality: on conj:CL and
   nothing else, exactly the assembly's status marker.
7. **Remark 6.6 (regions):** (a) $\ge10^5$; (b) $\ge1879$; (c)
   $\min(m,s^2)\ge79.5$, $s^2\le0.72711\sigma^2$,
   $\lambda\le\log(17/7)<0.89$ ($\log(17/7)=0.887303$, recomputed), CL
   consumed here and nowhere else, $(1-20/79.5)/0.72711 = 1.029318 \ge
   1.0293$ (recomputed); (d) $1-B_m-C_A/m^2$; regions (a)–(c) exceed
   $1.02>1-B_m$; $K_c$ definition matches Theorem S. $C_A$ size-honesty
   ("one lossy triangle-inequality step; measured analogue about 5")
   matches assembly §6 (truth anchor ~5.04). All per assembly §2.3/§4-C.
   The uniform $\lambda\le\log(17/7)$ covers both bands ($\log2<
   \log(17/7)$), and the $m\ge1581$ band's larger floor (527) only
   strengthens (c) — the paper correctly needs no 136-clause since it
   assumes $C^*=20$ throughout.
8. **Theorem 6.2 (finite range):** scope $5\le m\le560$ + $m=4$
   exception — exactly the STATUS_wave5 "G2 overall" grant (C5 scope per
   the standing erratum; $m=4$ C2/C3 exception). varfit(560) =
   0.998072591511 (checkpoint, verbatim); $560(1-0.998072591511) =
   1.07935$ (recomputed; matches the mfit column); $\mathrm{varfit}(4) =
   91/108 = 0.842593 < 187/216$, argmin $=2$, $N/2=3$ (assembly block
   E). Harness provenance paragraph factually correct: 557 rows total,
   4..481 honored from `results_m540.txt` (478 rows) + 482..560 in
   `results_m560.txt` (79 rows), exactly one `# OVERALL: PASS` line,
   exact integer/Fraction verdicts, floats display-only.
9. **Remark 6.9 (evidence):** (S1) 2.1215/6.3552 vs 2.2/6.6, limits
   2.1303/6.4113, headroom 3.7%/3.9% (recomputed: 3.70%/3.85%) —
   flagged as thinnest margins, as mandated. (S2) 0.0083–0.2104, slack
   1.6–8 (see F3). (S3) 32.6% at $(561,5.0)$; unavoidability (43%
   failure at an (S1)-and-$\kappa_4\ge0$-consistent point) = Prop E.3,
   phrased without jargon. (S4) $20/\min(m,s^2)\le0.036$ — correct:
   $\min(m,s^2)=m$ on the band (composite A2(iii)-bonus) and $20/561 =
   0.03565$; 260 adversarial indices / 17$\times$ (see F2). "Two earlier
   hypotheses proved outright and retired, (S3)/(S4) entered" — matches
   the wave-5 surface delta (SL3'-w, SL4'-X out; (S3), (S4) in).
10. **"Location and explicit constant" remark:** crossover recomputed
    exactly with $C_A = 37997.8442$: $1-B_m-C_A/m^2 - 187/216 =
    -1.4\times10^{-5}$ at $m=536$, $+4.8\times10^{-4}$ at $m=537$ —
    $m^*=537$ confirmed (assembly block B), and $560\ge537$ means the
    harness covers past the crossover, so "granting CL, sharp bound for
    every $m\ge5$, equality only at $m=6$" is sound with no $[401,536]$
    gap. Conditional minimizer localization to $|\lambda|\le4/m$ follows
    from regions (a)–(c) $>1.02$ vs central value $<1$ — sound.
11. **Discussion item 1:** matches STATUS_wave5 §3 ("the only remaining
    mathematics"); "under 4% headroom ... where a proof attempt — or a
    counterexample search — should begin" matches the mandated (S1)
    margin honesty.

## 3. No-overclaim audit (all prohibitions honored)

- Nowhere does the paper say F2(a) is proved; the sharp asymptotic is
  Theorem 6.5, *conditional*, everywhere it appears (abstract,
  contribution (iii), §6, discussion).
- CL is a **Conjecture** (6.3), never "nearly proved"; the claim-scope
  remark (`main.tex:884–893`) explicitly refuses the "close to proved"
  reading of the sub-4% margin.
- (S1)–(S4) are a **Conjecture** (6.7), stated precisely and
  self-containedly in paper notation; all four called open and
  load-bearing ("removing any one leaves no theorem" — STATUS_wave5 §3).
- The (S1) 3.7%/3.9% margins are stated (mandated honesty item).
- Finite companion is an unconditional exact theorem, $5\le m\le560$.
- No internal process jargon (waves/referees-by-name/agents/file names)
  in any mathematical statement; repository references are factual.
- No stale claims: grep confirms zero occurrences of "150", `conj:F2`,
  or "uniformity" in `main.tex`; the single `$m\ge401$` occurrence
  (line 716) is the correct needs-statement.

## 4. Mechanical checks

- **Compile (on a scratchpad copy):** tectonic 0.17.0, clean, exit 0,
  zero undefined references/citations, 13 pages, only the four
  pre-existing overfull-hbox warnings (lines 357–517, sections 3–5) —
  all matching the change log's build note.
- **Numbering:** Theorem 6.1 (G1), Theorem 6.2 (finite560), Conjecture
  6.3 (CL), Remark 6.4, Theorem 6.5 (F2), Remark 6.6, Conjecture 6.7
  (S), Proposition 6.8, Remark 6.9, Table 4 — exactly as the change log
  records.
- **Cross-references:** every `\ref` in the file resolves to a defined
  label (28 labels, 0 dangling).
- **Change log accuracy:** every quoted old/new pair, source citation,
  and build claim spot-checked; no misattribution found.

*End of review. Reviewer verdict: MINOR_FINDINGS (three wording-level
items, §1); the F2 upgrade is faithful to the campaign ledger.*
