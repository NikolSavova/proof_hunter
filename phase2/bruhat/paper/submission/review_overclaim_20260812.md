# Adversarial review pass: OVERCLAIM / ATTRIBUTION — main.tex F2 upgrade

*Read-only review, 2026-08-12. Target: `paper/submission/main.tex` (post
F2-upgrade) + `change_log_20260812.md`. Checklist = the ABSOLUTE
NO-OVERCLAIM RULES (STATUS_wave5 §4 permitted claim and prohibitions).
Ground truth read in full and in order: `STATUS_wave5.md`,
`CL_composition_20260812.md`, `theoremA_assembly_20260811.md`, plus the
harness artifacts (`harness_m560/results_m560.txt`,
`wave2_repairs/results_m540.txt`) and `wp4_draft_composite.md` §0 (band
partition / tilt-frame source). No file other than this report was
created or modified.*

## Verdict: **MINOR_FINDINGS**

No violation of any hard prohibition was found. The paper does not say
F2(a) is proved; does not call CL proved or nearly proved; states
(S1)–(S4) as genuinely open, all four load-bearing, with the mandated
(S1) 3.7%/3.9% margin caveat stated verbatim and explicitly flagged as
the thinnest in the reduction; contains an explicit "we do not regard
[the sub-4% margin] as grounds for treating any of the four as close to
proved" disclaimer (lines 884–893); keeps all mathematical statements
self-contained in paper notation; and contains no internal process
jargon (grep for wave/STATUS/campaign/referee-names/SL-file-names in the
mathematical sections: clean). The findings below are precision/honesty
polish, not claim violations.

## Abstract check (the mandated special pass)

Hunted specifically for an optimistic adjective. Every load-bearing
phrase of the new F2 sentence (lines 71–78) maps onto the STATUS_wave5
§4 permitted claim: "conditional on a single explicitly stated core
lemma" (= "conditional on the single explicitly-stated core lemma
CL(79,20,0.89)"), "needed only for m>=561" (= "reduced by exact integer
computation to m >= 561"), "itself reduced, with explicit constants
throughout, to four explicitly stated **open** cumulant statements" (=
"an implication from exactly four explicitly-stated open statements
about the cumulants of the tilted Mahonian law ... none yet proved").
"Sharp", "single", "explicit", "exactly" are all licensed verbatim by
the ground-truth documents; the one adjective applied to the four
statements is "open" — the honest one. **No optimistic adjective found;
the abstract is compliant** apart from the m<=560 range-phrasing nit
(Finding 1).

## What was verified correct (spot-checked against ground truth / disk)

- **Conjecture 6.3 (CL)**: spec (79, 20, 0.89), scope m>=561, tilt band
  (4/m, 0.89], lower-bound-only consumption, s2>=79 never binds
  (1122800/7921 > 141 — matches wp4_composite [A2](iii)), the
  [401,560] discharge phrased as consumer-level ("no CL-type lemma is
  needed there"), all match theoremA_assembly §3 + CL_composition §0/§2.
- **Conjecture 6.7 ((S1)–(S4))**: statements and scope match
  CL_composition §4 statement-for-statement after the documented
  renamings (r31/r42 -> tilde-kappa; w -> omega; W6b -> W_6). Table 4
  constants R_3/R_4/C_5/J_0 verified digit-for-digit against
  CL_composition §4. Band partition (4,5],(5,6],(6,8],(8,10],(10,20],
  (20,40],(40,inf) ∩ {lambda<=0.89} verified against
  wp4_draft_composite §0.
- **Proposition 6.8**: implication + composed constant 18.23 (ledger:
  18.2281 <= 20) match Theorem CL-C.
- **Theorem 6.5 (conditional F2)**: two-sided display with C_A=37997.85
  (closed flavor, valid all m>=401 ⊇ m>=561) and unconditional UB
  1.8/m^2 for m>=180 match theoremA_assembly §2.4; r_m−1 ~ 36/m^3
  consistent with sigma^2 ~ m^3/36.
- **Remark 6.6 (reduction shape)**: region constants 10^5, 1879, 79.5,
  0.72711, log(17/7)<0.89, 1.0293, and the C_A size-honesty note
  (measured analogue ~5) all match theoremA_assembly §2.3/§4/§6.
- **Theorem 6.2 (finite560)**: scope 5<=m<=560 with the m=4 exception
  stated (argmin=2, varfit=91/108); verified on disk:
  `results_m540.txt` rows 4..481 (478 rows, all PASS) +
  `results_m560.txt` rows 482..560, single `# OVERALL: PASS` line
  verbatim, 557 rows total; varfit(560)=0.9980725915 and mfit=1.07935
  match the paper's 0.998072…/1.07935. "One row for every 4<=m<=560,
  all passing" is accurate.
- **187/216 crossover m>=537** (lines 906–912): matches
  theoremA_assembly §4 block B (closed flavor m*=537, "stays beyond:
  True"); the harness (560) covers past it, so the "granting the
  conjecture, every m>=5" chain is sound.
- **Evidence remark 6.9**: (S1) 2.1215/6.3552 vs 2.2/6.6, limits
  2.1303/6.4113, 3.7%/3.9%; (S3) 32.6% at (561, 5.0) + the 43%
  unavoidability point; (S4) 0.89 vs 20/min(m,s^2)<=0.036
  (20/561=0.0357); 260 adversarial indices at m=401/402, 17x — all
  match CL_composition §4/§5.5 (17.1x reported as 17x: understated,
  fine; "260 adversarially chosen" honest, not "every").
- **Prohibited-language grep**: no "nearly/almost/essentially proved",
  no proximity language anywhere in the F2 thread; no stale "150", no
  retired `conj:F2` label.
- **Citations/attribution**: the new F2 material (lines 674–913) adds
  **zero** `\cite` commands and the bibliography is byte-untouched
  (all `\cite` lines are in pre-existing sections). There are NO new
  bib entries, so nothing new to verify against the literature; the
  fabrication risk flagged from the 2026-08-06 review does not recur.

## Findings

### Finding 1 (minor — range phrasing "every m<=560")
- **Where:** main.tex:73 (abstract: "determine the global minimum
  exactly, in integer arithmetic, for every $m\le560$"); main.tex:152
  (intro (iii), same phrase); main.tex:645 ("has been computed exactly
  for every $m\le560$"); main.tex:676 ("Theorem~\ref{thm:finite560}
  settles every $m\le560$ outright").
- **Why wrong:** the computation covers 4<=m<=560 and the companion
  theorem is scoped 5<=m<=560 (m=4 is the known exception; m<=3 appears
  in no log — r_2 is not even defined). "Every m<=560" claims a hair
  more range than the artifacts carry, in the paper's most visible
  sentences.
- **Suggested fix:** "for every $4\le m\le560$" (abstract/intro/line
  645) — or "$5\le m\le560$" where the companion content is what is
  meant — and at line 676 "settles every $m\le560$ in range" -> "settles
  every $5\le m\le560$ outright".

### Finding 2 (minor — (S2) evidence omits the W1 coverage caveat)
- **Where:** main.tex:864–866: "measured remainder ratios lie between
  $0.0083$ and $0.2104$; the slack over $C_5$ ranges from a factor
  $1.6$ to a factor $8$ depending on the band."
- **Why wrong:** CL_composition §4 (S2) qualifies the evidence: "W1's
  slack is `w = 4.30`-class, NOT uniform to the band edge" (inherited
  F4 scoping). Quoting the 1.6–8x slack range without that qualifier
  slightly inflates the evidence coverage for (S2) on the lowest band —
  the same class of nuance the mandate requires stating for (S1).
- **Suggested fix:** append a clause, e.g. "…to a factor $8$ depending
  on the band (the lowest band's slack was measured at interior probe
  points, not uniformly to its edge)."

### Finding 3 (observation — Proposition 6.8's epistemic status; already
flagged in the change log)
- **Where:** main.tex:831–836 (Proposition 6.8) and the following
  paragraph.
- **Status:** NOT an overclaim under the mandate: STATUS_wave5 §4's
  permitted sentence itself asserts the assembled implication, every
  consumed input is two-referee verified, the composed constant is
  machine-re-verified end-to-end, and the paper cites no internal file.
  But the composition note that assembles the implication still owes
  its own unit referee pass (CL_composition §5.4, STATUS_wave5 §3 item
  2), and change_log §7.2 correctly flags this as the one judgment call.
- **Action:** none required in the text; the human ratification step of
  STATUS_wave5 §5 item 1 (read CL_composition §2+§4, confirm the
  surface) should be completed before submission, or the change log's
  proposed hedge adopted.

### Finding 4 (nit — "verification of Conjecture CL itself at m=401, 402")
- **Where:** main.tex:876–878: "Exact verification of
  Conjecture~\ref{conj:CL} itself at $m=401$ and $m=402$…"
- **Why imprecise:** Conjecture 6.3 is stated for m>=561, so m=401/402
  lie outside its stated scope; what was verified is the CL inequality
  (the displayed identity with theta in [-1,1]) at those m. Favorable-
  direction evidence, honestly quantified — just re-word, e.g. "Exact
  verification of the inequality of Conjecture~\ref{conj:CL} at $m=401$
  and $m=402$ (below the conjecture's stated range)…".

## Change-log cross-check

`change_log_20260812.md` accurately describes every edit found in the
file (old/new abstract text, deletions, the new environments and their
numbering, the untouched-list — grep-confirmed). Its §6 build note
honestly documents the toolchain difference (Tectonic vs pdfTeX). Its
§7.2 flags the one judgment call (Finding 3). No discrepancy between the
change log and the actual file was found.

*End of review. Verdict: MINOR_FINDINGS — four items, none a violation
of the no-overclaim rules; Findings 1–2 are one-line text fixes, 3 is a
process/ratification note, 4 is a wording nit.*
