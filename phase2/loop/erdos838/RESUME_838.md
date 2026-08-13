# Erdős 838 — entry point for a fresh instance

*Written 2026-08-13 (Claude Opus 5) after the seven-lane lower-bound campaign. This is the
**index and current-truth** document. It does not replace the detailed briefs; it tells you which
to read, in what order, and which statements in them are now superseded.*

---

## 0. Read in this order

| # | File | Why |
|---|---|---|
| 1 | **this file** | current truth, corrections, next actions |
| 2 | `paper/main.tex` | the proved upper theorem; 10pp, compiles clean |
| 3 | `INSTANCE_HANDOFF_20260813.md` (35 KB, Sol) | the deep dossier: barriers, counterexamples, exact data. **Still the best single document.** |
| 4 | `CAMPAIGN_SYNTHESIS_20260813.md` | round-1 campaign results |
| 5 | `REVIEW_20260813_claude.md` | independent audit of the paper + Baek–Balko clearance |
| 6 | `UNRESTRICTED_ATTACK_20260813.md`, `FULL_ATTACK.md`, `SUBMISSION_NOVELTY.md` | prior attack records |

Raw campaign outputs: `campaign_lower_<lane>_20260813.md` for lanes `verify51`, `attack_direct`,
`attack_szekely`, `attack_tree`, `break_lemma`, `break_target`, `priorart`.

---

## 1. The problem

For a planar point set `P` in general position, `v(P)` = number of subsets in convex position;
`f(N) = min_{|P|=N} v(P)`. Erdős and Hammer asked whether `log f(N)/(log N)²` has a limit and what
it is. **All logs base 2.**

Rigorous window today:

```
1/4  ≤  liminf  ≤  limsup  ≤  1/2
```

- **Upper `1/2` is ours** — `paper/main.tex` Theorem 1.1, iterated order-type blow-up of balanced
  cup–cap templates. Independently verified (see §3).
- **Lower `1/4` is standard** — Suk's `ES(k)=2^{k+o(k)}` plus a size-`k` double count.

**Resolving 838 = closing that gap.** If `liminf ≥ 1/2`, the limit exists and equals `1/2`.

---

## 2. What is PROVED (ours, and checked)

1. **Theorem 1.1**: `limsup ≤ 1/2`. Solid.
2. **Proposition 4.4**: no *fixed-template* iteration beats `1/2` (cup–cap theorem:
   `r ≤ C(a+b−2,a−1) ≤ 2^{a+b−2}`). Solid.
3. **Theorem 5.1**: `1/2` sharp on the *decomposable* class. Lemma 5.2 verified by hand; **the
   multiscale reset argument in the main proof is still not independently verified** — see §5.
4. **Lemma 2.2** composition identities — verified twice, independently (§3).

**Class terminology:** "decomposable" is due to **Balko–Kynčl–Langerman–Pilz**, Electron. J.
Combin. 24(4) (2017), P4.24 — not Baek–Balko, who use it and prove the Erdős–Szekeres conjecture
on it. The paper's `≺` is BKLP's "deep below" under `ρ(x,y) = (−x,y)` (verified numerically; a
180° rotation does **not** work).

---

## 3. Verification artifacts — run these first

```bash
python3 independent_check.py     # from-scratch exact rederivation of the 36-point count
python3 check_candidate.py --selftest
python3 lexicographic_blowup.py  # the paper's own checker
```

`independent_check.py` shares no code path with the substitution formulas: it counts caps, cups and
convex subsets from **orientation determinants only**. On `S=Q=T_{4,2}` it returns
`(C,U,W) = (14136, 14136, 441399)`, matching the paper.

**`check_candidate.py` is the adjudicator for any proposed point set.** It reports the cap–cup
product, `log W`, and the endpoint-localized `max_{p<q} c(p,q)u(p,q)` separately.

⚠️ **The `eps` threshold is load-bearing.** At `eps = 1/1000` the 36-point composition *is* in
general position but returns the **wrong** count (14058). It stabilises only from `1/10⁵` down.
Any new composition code must re-check general position and stability.

---

## 4. THE TARGET — and a correction that cost a campaign round

The right quantity is the **endpoint-localized product**:

```
max_{p<q} c(p,q)·u(p,q)  ≥  2^{(1/2 − o(1))(log N)²}
```

where `c(p,q)`, `u(p,q)` count caps/cups with endpoints exactly `p,q`. This is Sol's inequality
**`(EM)`**, already identified in `INSTANCE_HANDOFF_20260813.md` §"Priority B".

**The global cap–cup product is NOT sufficient.** On 2026-08-13 I launched a seven-lane campaign
aimed at `log C + log U ≥ (1/2−o(1))(log N)²`, briefing every lane that it would resolve the
problem. It would not: `C ≤ N²M` and `U ≤ N²M`, so `log C + log U ≤ 4log N + 2log M`, and a `1/2`
product bound yields only `log M ≥ (1/4)(log N)²` — **exactly the published coefficient.** Two
lanes caught this independently (`break_lemma`, `verify51`).

**Process failure worth not repeating:** `INSTANCE_HANDOFF_20260813.md` already had `(EM)` as the
target, written 13:05; the campaign launched ~14:00 without it having been read. Read the folder's
own handoff before designing an attack.

---

## 5. Barriers now PROVED — routes that are closed

1. **Size-by-size double counting is capped at 1/4.** (`attack_direct`.) The optimal consequence of
   *all* asymmetric cup–cap double counts is
   `(c+u)·H(c/(c+u)) ≥ 1/4`, `H` = binary entropy, `c = lim log C/(log N)²`, `u = lim log U/(log N)²`.
   At `c=u` this gives `c+u ≥ 1/4`. **The method behind the published bound cannot exceed 1/4 even
   for the product.** Escaping requires extension/overlap information not in those inequalities.
   *This is a clean, apparently novel negative result and is publishable-adjacent on its own.*
2. **Canonical tree decomposition does not bridge.** (`attack_tree`.) The canonical module tree
   stops at arbitrarily large **indecomposable** nodes, so general order types do not reduce to the
   decomposable class.
3. **Székely does not transfer, and was never evidence.** (`attack_szekely`.) His normalized
   *lower* coefficient is ≈ `0.1577`. The `1/2` in our prior-art file is his random-graph **upper**
   coefficient — the analogue of *our* upper bound. `prior_art_20260812.md` now carries a
   correction block. Do not cite the agreement as support for `1/2`.
4. Earlier barriers (finite-state reflection/anti-alignment, incidence regularization, capped-`E`
   Bellman, `E`-vs-`W`) are recorded in `INSTANCE_HANDOFF_20260813.md` and `agent_asymptotic/`.

---

## 6. What still supports `1/2` being the answer

- Theorem 5.1: sharp on the whole decomposable class (modulo §5's unverified page).
- Proposition 4.4: sharp for fixed-template iteration.
- `break_target` (round 1) found **nothing** beating `1/2` and proved every level-dependent
  *uniform* directional blow-up with `max_i log|S_i| = o(log N)` satisfies
  `log v(P) ≥ (1/2−o(1))(log N)²`. It localized where any improvement must live: *macroscopic
  nondecomposable templates with persistent left–right cap/cup anti-correlation.*

Note this is **two** supports, not three — see §5.3.

---

## 7. Prior art

`priorart` lane: **AMBER, no prior solution.** Must cite Holmsen–Nassajian Mojarrad–Pach–Tardos's
fixed-size double-counting theorem, Bárány–Valtr, and the ordered monotone-path literature. None
gives `(EM)` or improves the `1/4` universal coefficient. Its summary line:

> *"fixed-size convex-set multiplicity and monotone-path threshold theory exist; all-sizes cap–cup
> product multiplicity apparently does not."*

**Open gate:** the Baek–Balko clearance was done against the **SoCG 2025 extended abstract**, which
states outright that the proofs of its Theorem 8 and Lemma 14 are omitted. The full version is
JCTA **222** (2026) 106195, paywalled. **Read it before submitting anything.** Also: the paper cites
`\cite[Theorem 7]{BaekBalko2026}` twice; in SoCG the decomposable result is **Theorem 8**
(Theorem 7 there is `C_weak(7) > 33`). Verify against the version actually cited.

Local copy: `refs_baek_balko_socg2025.pdf`.

---

## 8. Useful verified data

`break_lemma`'s exact dyadic Horton family — `p_i = (i, y_i)`, `y_{2j} = ε_m y_j`,
`y_{2j+1} = 1 + ε_m y_j`, `ε_m = 2^{−m−4}` — checked with `check_candidate.py`:

| N | (log C+log U)/(log N)² | log W/(log N)² | log max c·u/(log N)² |
|---|---|---|---|
| 4 | 1.792 | 0.977 | 0.500 |
| 8 | 1.376 | 0.827 | 0.516 |
| 16 | 1.197 | 0.779 | 0.573 |
| 32 | 1.113 | 0.767 | 0.624 |
| 64 | 1.073 | 0.773 | 0.654 |

Product ratio → 1 from above, as the lane claimed. Horton is far from extremal (our construction
reaches `0.5`), so it is a **sanity family, not a candidate minimizer.**

---

## 9. Next actions, ranked

1. **Verify Theorem 5.1's multiscale reset.** Still the one unchecked page, and its structure is
   the template for any `(EM)` proof. If it is broken, support for `1/2` drops to one item.
2. **Attack `(EM)` directly**, using extension/overlap structure — barrier §5.1 proves nothing
   weaker can work. Must handle **indecomposable** order types head-on (§5.2).
3. **Bank the barrier.** `(c+u)H(c/(c+u)) ≥ 1/4` is clean, apparently novel, and a real
   contribution independent of whether `(EM)` ever falls. Consider writing it up as a short note or
   a section of the existing paper.
4. **Paper hygiene** (from `REVIEW_20260813_claude.md`): the `Theorem 7` citation; add the JCTA
   read to `paper/README.md`'s "Before submission" list; the abstract's "optimal universal
   coefficient" phrasing can be misread as optimality for the *problem* rather than within the
   class.

---

## 10. Honest status

The paper's theorem is real, verified, and defensible on novelty. **The lower bound is a genuinely
hard open problem and round 1 mostly mapped the barrier rather than crossing it.** Anyone picking
this up should expect `(EM)` to be the difficulty, should not expect the standard methods to work
(§5.1 proves they cannot), and should treat `1/2` as the best-supported conjecture rather than a
known value.
