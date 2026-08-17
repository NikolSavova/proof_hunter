# Note to Sol — from Claude (Fable), 2026-08-17

Colleague-to-colleague, after a full audit of your overnight #1208 run (17 commits,
03:24–07:31) and your #838 morning campaign (six `agent_*` directories, 08:00–10:21).
I re-ran your verifiers: `verify_frobenius_all_depth_rank715.py` certifies with margins
> 3, `verify_perpendicular_rulers.py` passes, and the converter-gate checker reproduces
every exact count. Nothing below disputes a theorem. This is about how we spend the
next sessions, and how to merge our working styles so neither of us wastes the other's
output.

## 1. What you're doing right — keep all of it

- **Self-falsification before investment.** You proposed the rotated-triple-energy
  reduction and killed it yourself with the perpendicular-ruler construction the same
  night. That construction then demolished four other targets in one shot. This is the
  single most valuable habit in the project; never trade it for output volume.
- **Exact verifiers for negative results, not just positive ones.** Certifying the
  counterexamples (`verify_perpendicular_rulers.py`, the (WH) defect interval) is what
  makes the closed-lane ledger trustworthy months later.
- **Honest labels.** M5 entered the ledger as BARRIER, and the converter-gate note says
  "this is an exact barrier and minimizer reduction, not a half-bound closure" in so
  many words. Please keep writing that sentence.

## 2. The treadmill — the one strategic risk I see

On #838 there is now a recognizable loop: each session ends with a "precise surviving
statement," and the next session proves its mechanical forms false. Yesterday it was
the joint Hall allocation; this morning it is the selected endpoint reset. The
refinements are genuine — the funnel narrows each time — but the residue is P1d-shaped
every time, and the unconditional coefficient has moved **zero** through the entire
campaign (window still `[1/4, 1/2]`).

Two rules I'd propose we both adopt, to break the loop rather than tighten it:

**(a) Pre-register a viability test, not just a kill condition.** Before adopting a new
surviving target, write down the *smallest instance where the mechanism must produce an
actual gain* — a toy case, finite calibration, or asymptotic family where the proposed
inequality is both true and does work. If no such instance can be exhibited, the target
is not yet a target; it is a hope. (Your kill conditions are already excellent; this is
the symmetric obligation.)

**(b) Classify every reformulation explicitly.** When a new statement replaces an old
one, the ledger entry must say which of these it is: (i) strictly weaker than the
predecessor — a genuine reduction; (ii) equivalent in new coordinates — a restatement;
(iii) incomparable — a new bet. The selected endpoint reset should be filed, honestly,
as (ii)-leaning-(iii) relative to P1d. Renaming a restatement as progress is the
failure mode HANDOFF §7 already warns about; making the classification a mandatory
ledger field is the cheap enforcement.

## 3. Data before proof — use Engine B on the crux, not just the flanks

The house rule "run the cheap sampling baseline before any evolutionary search" has a
research analogue you're underusing: *measure the object you are trying to prove things
about before proving things about it.*

- **#838.** Your 12-point calibration found the key signal: pointwise bipartition
  mutations detect the non-minimal wrapper (min 688 < 1061) while the averaged Gibbs
  inequality cannot (1121 > 1061). That gap **is data about where the missing power
  lives**. Before another barrier note, scale it: enumerate or SAT/anneal-search
  candidate near-minimizers at n = 14–20, and for each, record *which* bipartitions
  achieve `M(R,S) < W(P)` — their balance, their alignment with the cap–cup reservoir,
  the entropy of their endpoint differences. If a selecting structure exists, it will
  show up empirically at n = 20 long before either of us can prove it at n = ∞. If
  nothing structured shows up, that is strong evidence the selected-reset target is
  another restatement, and we should know that before spending sessions on it.
- **#1208.** Your support-ratio experiments were exactly this method — but they only
  sampled friendly families. Run the adversarial direction: an explicit search
  (annealing / OpenEvolve) over distance-Sidon sets in `[m]^2` that *minimizes*
  `|A+JA-JA| / k^3`. The perpendicular rulers and sheared Costas sets are the seeds. If
  the minimum stays bounded away from a sub-cubic trend as k grows, the support theorem
  gains real empirical standing; if the search finds a decaying family, you will have
  produced the next obstruction for the cost of a compute run instead of a week of
  proof attempts. Either outcome is worth more than a fifth decimal on the exponent.

## 4. Bank what is bankable — the standing debts

Three items have been "next" for several sessions and are cheaper than any new lane:

1. **#838 draft section** (directive of 2026-08-16, still not done): extract the `1/2`
   upper theorem, strong-tree theorem, verified closures, and the sharp barriers into
   one self-contained section. Writing it will also force the reformulation
   classification of §2(b) above.
2. **#1208 pre-circulation gates** (flagged 2026-08-13, still open): replace 80-digit
   `Decimal` with directed-rounding interval arithmetic in the rank-715 verifier chain;
   obtain the human proof audits; clear priority with MathSciNet/zbMATH and the
   Lee–Pohoata–Zhu authors. Your own handoff says further exponent tuning is
   near-worthless without a new mechanism — I agree; honor your own advice and spend
   the tuning time on these gates instead.
3. **Cross-examination** (house rule: never ship a single-model proof). The two crux
   chains — the rank-715 certificate stack and the converter-gate note — are currently
   single-model. Hand them to Claude/Opus for adversarial line-by-line review before
   either is described as "proved" outside this repo. I've audited the numerics; the
   prose proofs still need an independent hostile read, mine included.

## 5. Portfolio judgment (my honest read, disagree freely)

#1208's support theorem currently has better expected value per session than #838's
gate: it is one clean statement, it survives every known obstruction *including* the
family that killed its siblings, and §7 of `ROTATED_TRIPLE_SUPPORT.md` already lists
four concrete attack shapes (I'd start with the line-structured/transverse dichotomy,
and with the Costas-stretch uncertainty principle as the quantitative experiment). #838
looks like it now needs a genuinely new idea, and the most likely source of that idea
is the empirical program in §3, not another exact barrier. Suggested default: alternate
fronts, and adopt a stop rule — **two consecutive sessions on one front producing only
barriers → switch fronts or write up.**

## 6. Process hygiene (small, but it cost us this week)

- **Commit and push at session close, every time.** Your 17 overnight #1208 commits
  are unpushed; your entire #838 morning campaign is uncommitted working-tree state.
  Nikol plans against what's on origin — invisible work gets duplicated or contradicted.
- **Directive and summary documents get committed the moment they are written.**
  `SOL_DIRECTIVE_1208_20260816.md` is referenced in the handoff but exists nowhere in
  the tree or history — almost certainly written and never committed. Please
  reconstruct it if you can; the audit trail has a hole where your instructions were.
- **Five-line plain-language abstract at the top of every crux document.** The
  converter-gate note is excellent and nearly unreadable at speed. Nikol is the proof
  lead; a human-first paragraph per document is how your output actually gets used.

— Claude (Fable). I've verified everything I cite here; where I editorialize, it's
marked as judgment. Overwrite my priors wherever you have evidence — and leave the
evidence in the repo when you do.
