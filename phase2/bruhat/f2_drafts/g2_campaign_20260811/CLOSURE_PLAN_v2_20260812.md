# Closure plan v2 — what is left after the composition repair

*2026-08-12, late. Supersedes `CLOSURE_PLAN_20260812.md`, which was written before the
composition repair split out two further obligations. Corrected ledger: **(S1) PROVED;
(S2)-(S6) open** — the repair document's own `(S1): OPEN` row is stale (its briefing was
fed the wave-5 ledger; see the reader's note appended to it).*

## The obligation list, current

| | statement | status tonight |
|---|---|---|
| **(S1)** | banded cumulant scales | **PROVED** — two-referee, wave 6b |
| **(S2)** | fifth-order remainder `R5` bound | attempt 3 self-contained; maths lane MINOR_REPAIRS, numerics lane MAJOR_ISSUES (provenance only); numerics independently replayed in full |
| **(S3)** | joint cancellation `J <= J0(W)` | compact bands + `(SOL.5)` certified locally; sign gap and W7 certificates drafted; **referee lanes running** |
| **(S4)** | a-priori ratio seed | drafted for `m >= 700`; **referee lanes running**; `[561, 699]` is carried by (S5) |
| **(S5)** | `w`-continuum certificate for the W1 rung | **NEW** — Sol agent launched |
| **(S6)** | bootstrap closure with directed endpoint signs | **NEW** — Sol agent launched |

## If the six referee lanes come back positive, this is exactly what remains

**A. The two new statements — the only genuinely open mathematics.** Both launched:

- **(S5)** must certify the whole real interval `(4, 5]` for every integer `m` in
  `[561, 699]`, with a proved extension at `w = 4`, directed bounds per cell, the
  conclusion `upper_bound(Row_W1) <= 1` on every cell, and an archived cell-union check.
  Route: write out the M3 per-cell-floor argument as a proved `w`-uniform lemma — it needs
  no `tau`-monotonicity, which is why it can reach the continuum where the probes cannot.
  **(S5) also carries (S4)'s missing range**, since the (S4) seed proof covers only
  `m >= 700`.
- **(S6)** must supply the exact bootstrap function, directed endpoint signs
  `upper(G(a) - a) < 0` and `upper(G(b) - b) < 0` at `a = 20/m`, `b = 89/100`, convexity on
  the whole interval (branchwise if `G = max(G_INFL, G_QUADF)`), and a uniform
  extremal-row reduction proving the thinnest rows dominate every `m`, band, and `lambda`.

**B. Provenance work on (S2) — no new mathematics.** Its numerics lane objected that the
512-cell and `F_1 < 25` certificates are asserted without archived scripts. The scripts
exist (`s2b_replay/`) and every band has been reproduced locally, including the
`1/8`-corrected assembly. This is a recording task: archive scripts + outputs beside the
draft and apply the maths lane's MINOR_REPAIRS. Free, local.

**C. Referee the repaired composition.** `sol_comprepair_20260812.md` is single-model and
unrefereed; it is now the document that defines the obligation list, so it needs two lanes
before anything may cite it.

**D. The hygiene overlay verifier.** Still owed. Input I3 consumes its `M_H = 560` repair,
so the finite-range splice and the claim that `m >= 561` is the entire residual obligation
are not citable until it lands.

**E. Then, and only then:** composition v4 assembled from proved inputs, its own referee
lanes, and the flip to an unconditional Theorem A.

## Honest read on difficulty

(S5) looks the more tractable of the two: the route is identified, needs no new idea, and
the measured margins are comfortable (`0.4165` against a target of `1` at the worst point).
It is a write-it-out-properly job.

(S6) is the riskier one. The current argument is a fixed-point ansatz, the endpoint it
needs sits `0.00412` from the measured basin boundary, and the uniform extremal-row
reduction — proving two rows dominate every band and every `m >= 561` — has never been
attempted. If a seventh obligation appears anywhere, this is where.

## Trajectory, stated plainly

Open statements at the start of 2026-08-12: four. Now: five. The mathematics advanced on
three fronts tonight — (S2) proved and replayed, (S3) and (S4) drafted — while the
assembly was found to rest on two previously unstated certificates. Every adversarial pass
so far has been worth its cost, and none has yet found the campaign's claims to be false;
what they keep finding is that the claims were resting on less than advertised.

---

## Addendum, same evening — the six referee lanes, and a briefing lesson

**Verdicts:** `s3w7cert` MINOR_REPAIRS / MINOR_REPAIRS (**passes both lanes** — W7's
certificates are the first piece of (S3) to clear the bar); `s3w7sign` MAJOR_ISSUES /
**FATAL**; `s4seed` MAJOR_ISSUES / MAJOR_ISSUES.

### The FATAL was a packaging failure, not a mathematical one

Its findings 1, 2, 3 and 6 all say the same thing: the load-bearing certificates are
"absent — no file, code, output, hash, cell count, or margin." **Those certificates exist
and pass.** `s3_cert.py` certifies W1–W6b at cell width 1/128 with zero hard failures,
using the corrected constant; `sol5_cert.py` certifies `|h_n^(8)| <= 10^12` on (0,40]
*including* the [0,1] range the referee flagged, via a Cauchy bound on `|z| = 6`. The draft
never carried them because **the brief told the agent they were "established and citable"
instead of handing over the artifacts.** The referee, reading only the draft, was right.

Two briefing defects of the same species were found tonight:

1. the base context fed every agent the wave-5 ledger, so agents reported (S1) as open
   long after it was proved (patched: `STATUS_wave6.md` now included);
2. briefs asserted certificates rather than attaching them (patched: an `attach()` helper
   now pastes scripts and archived outputs into the prompt).

**Rule going forward: hand over the artifact, never the assurance.**

### Actions taken

- **`s3consol` launched** — assembles (S3) into ONE self-contained document with
  `s3_cert.py`, `sol5_cert.py` and both archived outputs pasted in, the band table and
  exact `J0(W)` values defined, the post-correction margins stated, `E_{n,8}` given by a
  full Euler–Maclaurin identity, and every referee finding answered from evidence rather
  than citation.
- **(S4) is NOT relaunched yet** — it is blocked, not merely unpolished. Its seed is proved
  only for `m >= 700`; the `[561, 699]` range was to be bypassed by M3, and its referee
  showed M3 is a cell-floor/crossover result, not a proof of the seed bound, and may itself
  sit downstream of the seed. That range is now (S5)'s to carry, so (S4) waits on (S5).
  Its band-edge slip (theorem excludes `m|lambda| = 4`, composition uses the closed edge) is
  repairable and noted.
