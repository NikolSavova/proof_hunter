# Closure plan — from here to an unconditional Theorem A

*2026-08-12, written as the Sol closure fleet launched. This is the ordered path from the
current state to Theorem A = F2(a) proved unconditionally, with every gap named. Fable
fleets are off (budget policy); all model work runs on gpt-5.6-sol at `effort=max`, all
verification runs locally and free.*

## The dependency chain (what "closed" has to mean)

```
Brenti Conj 2.11  (OPEN — not claimed, not attempted)
  └─ F2  (paper's quantitative contribution)
       └─ F2(a) = THEOREM A          <-- the target
            ├─ G1  ...................... CLOSED (refereed 2026-08-02, repairs verified)
            └─ G2 = Prop 3.5
                 ├─ 3.5(ii) ............. CLOSED (wave 2: Delta_ker + T.9-final)
                 └─ 3.5(i) .............. reduced gap-free by Theorem S to:
                      └─ CL(79, 20, 0.89)
                           ├─ m in [5, 560] ... CLOSED by exact computation (harness)
                           └─ m >= 561 ........ needs (S1)+(S2)+(S3)+(S4)
                                ├─ (S1) ....... PROVED (two-referee, wave 6b)
                                ├─ (S2) ....... attempt 3 complete; referee lanes running
                                ├─ (S3) ....... W1-W6b + SOL.5 certified; W7 in flight
                                └─ (S4) ....... reduced to the seed lemma; in flight
```

## Phase 1 — close the three remaining statements *(RUNNING)*

| agent | target | why it is smaller than it looks |
|---|---|---|
| `s3w7sign` | (S3)'s `B >= 0` + half-line B_8 lemma | reduced to `3(coth y - 1/y) > tanh y`; series gives `(4/15)y^3 > 0`, numerics confirm on the whole half-line |
| `s3w7cert` | (S3)'s W7 certificates (SOL.16/17 + four scalars) | the other two of referee F1's three certificates are already done |
| `s4seed` | (S4)'s seed `\|s2(r-1)-1\| <= 0.89`, `m >= 700` | bootstrap closure already supplied by its referee; `[561,699]` already killed; target is loose by ~30x |
| `s2c` ✔ | (S2) maths lane | **landed** — self-contained proof, all five briefed defects fixed |

## Phase 2 — adversarial referee lanes *(RUNNING)*

Nothing counts until two lanes pass it (house rule). Launched:
`sol_s2c` maths + numerics; `CL_composition_v2` maths (outstanding debt);
`wave4_hygiene` numerics (outstanding debt). Phase-1 outputs get the same treatment as
they land.

## Phase 3 — local verification of everything (free, no API)

Each artifact gets its numerical spine independently replayed from its own stated
formulas, copying no number from it — the pattern already applied to (S2) attempts 2/3 and
to (S3)'s certificates. **Standing item: the exact-rational redo.** Both certificates are
currently "rigorous modulo `mpmath.iv` providing outward rounding", which is the ordinary
computer-assisted-proof standard but not the "all operations are rational" the drafts
advertise. Margins are wide (worst 0.052% on `G(0.89)`, now exactly certified; the cell
certificates clear by 0.1-0.3%), so a coarse rational envelope for `exp`/`cos`/`sin`
suffices. This is the last standing methodological objection.

## Phase 4 — composition v3

Reassemble CL from the four statements as finally proved, re-verify the chain constant
end to end (`<= 20` on `[561, 1580]`, `<= 136` beyond; wave-6 scout's re-architected
constants give 19.5659). Then its own referee lane. **No flip until this passes.**

## Phase 5 — the flip

Execute the flip instruction in the already-refereed `theoremA_assembly` document:
`theoremA_final` = unconditional Theorem A, with the complete file-level dependency chain,
every referee status, the end-to-end constant ledger, the aggregated outstanding-repairs
appendix, and an honest "what this does NOT prove" (F1 in full, Brenti 2.11, G3).

## Phase 6 — paper and humans *(cannot be automated)*

1. **Nikol + Sihao read `main.pdf` end to end.** Still owed from 2026-08-06 and now more
   so — the F2 section changed twice today.
2. Update the paper: Theorem 6.5 loses its conditional clause; Conjecture 6.3 (= CL)
   becomes a theorem; Conjecture 6.7 ((S1)-(S4)) is retired. Marking (S1) proved is
   available immediately and moves no other constant (STATUS_wave6 checked this).
3. Fill the repository-URL placeholders; the licence is decided (MIT + arXiv
   non-exclusive) and in the repo.
4. Fresh pre-submission kill-search (house rule, Erdosgate).
5. Venue call: EJC / Sem. Lothar. / Experimental Math — and if Theorem A lands
   unconditionally, the JCTA tier is back in scope.

## Honest risk register

- **(S4)'s seed is the least-explored item.** It has never had a serious attempt; the
  0.89 target is loose but "weak-CL-shaped", and the upper side is the real work.
- **(S3)'s W7 certificates are unattempted at scale** — W7 runs to `w = 499` at `m = 561`,
  far beyond the compact-band cell method.
- **Thin margins persist** in (S2): W7 at 2.44%, W5 at 4.0%. Any later constant revision
  must be rechecked against these specifically.
- **Everything is machine-refereed.** Cross-model review has repeatedly earned its keep
  today — it caught fabricated-free but wrong claims, an invalid trapezoid constant, and a
  resolution spec error — but it is not a human mathematician's read, and the house bar
  still ends with Nikol.
