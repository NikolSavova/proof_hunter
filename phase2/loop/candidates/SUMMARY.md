# Six counterexample-shaped candidates — prior-art sweep results

*2026-08-13. Sol, effort=max, web_search. Full reports in `sweep_<name>_20260813.md`;
runner `scripts/sweep6.py`. Candidates chosen after the Jacobian conjecture counterexample
(Alpöge/Fable 5, 2026-07-20) for the same shape: counterexample is a short explicit finite
object, cheap to verify once exhibited.*

## Headline

**My knowledge was stale on five of the six.** Three had status changes inside the last twelve
months that I did not know about, and one is outright proved. This is the strongest evidence yet
for the house rule that the kill-search comes first — had we launched attack agents on my initial
ranking, the second-ranked target was already a theorem and the top-ranked search space was
already closed by a theorem I did not know existed.

| Problem | Status | Hunt | What changed |
|---|---|---|---|
| Casas-Alvero | **PROVED** | dead | Ghosh, arXiv:2501.09272v2, rev. March 2026 |
| Crouzeix | OPEN | audit first | Unrefereed proof claim posted 6 days ago |
| Kaplansky zero-divisor | OPEN | marginal | My proposed search space is dead by theorem |
| Lonely runner | OPEN at n=14 | marginal | Frontier moved 7 → 13 runners in 12 months |
| Seymour 2nd neighbourhood | OPEN | marginal, most concrete | Floor now n=19, δ⁺=8 |
| Union-closed sets | OPEN | **hopeless** | My prior was right |

## 1. Casas-Alvero — PROVED, target dead

Soham Ghosh, *Proof of the Casas-Alvero conjecture*, [arXiv:2501.09272v2](https://arxiv.org/abs/2501.09272),
revised 21 March 2026, 22pp. Proves the exact characteristic-zero statement in **every degree**
— arbitrary char-0 field, a possibly different common root per derivative, no real-root or
algebraic-closure restriction. Route: "degree n+1 implies degree n" via a regular-sequence
reformulation and Koszul homology, plus downward induction from the known arbitrarily-large
proved degrees.

Not a bare title claim: Schaub and Spivakovsky, active researchers on the problem, added to their
own [arXiv:2312.08742](https://arxiv.org/abs/2312.08742) that Ghosh gives a complete proof, and
Ghosh thanks Spivakovsky for reading drafts. No erratum or withdrawal found. Not yet journal
published, so the only remaining project here is an independent proof audit — not a search.

**I had ranked this second of six.** It was already a theorem when I proposed it.

## 2. Crouzeix — OPEN, but audit the six-day-old proof claim first

Shanmu Jin, *The Numerical Range Is a 2-Spectral Set*, Preprints.org 202607.1919v4, posted
**7 August 2026**, claims the full conjecture including the holomorphic and spectral-set versions.
Explicitly not peer-reviewed, no public comments, no arXiv posting, no independent validation. The
sweep could not certify or refute its central "positive-real completion theorem".

A second claim (Davis, Zenodo, March 2026) the sweep examined and rejected on the merits: it
controls individual powers `N^k` via numerical-radius inequalities but not arbitrary sums
`Σ a_k N^k`, and the Schur decomposition does not give the claimed monotone comparison.

If a counterexample hunt were to run: first open case is generic **3×3**, roughly a ten-real-
dimensional normalised space, no certified exhaustive search of which exists. Search in
Riemann-map plus degree-≤2 Blaschke coordinates rather than raw polynomial coefficients; floating
point to locate, interval arithmetic to certify. Against it: ~250 million unsuccessful
floating-point trials in the existing literature, and exact known extremisers.

## 3. Kaplansky zero-divisor — OPEN, but my specific plan is dead by theorem

> **Do not search in P.** The Promislow/Hantzsche–Wendt group satisfies the zero-divisor
> conjecture over **every field**, so `F₂[P]` is a domain and zero divisors of **every finite
> support size** are ruled out — not merely up to a computational bound.

`P` is torsion-free virtually abelian, hence polycyclic-by-finite and elementary amenable, and is
covered by Brown/Farkas–Snider in char 0 and Cliff in char p. Gardam *uses* this fact in his unit
counterexample paper. The same argument kills every torsion-free crystallographic/Bieberbach
group. So the crystallographic half of Gardam's precedent does not transfer at all — the unit
conjecture and the zero-divisor conjecture are logically independent in the direction we need
(unit ⟹ zero-divisor ⟹ idempotent, and the failure of the first gives nothing in reverse).

Already dead by theorem: one-sided orderable, unique-product, torsion-free elementary amenable,
polycyclic-by-finite, virtually abelian, residually torsion-free nilpotent, residually torsion-free
elementary amenable, strong Atiyah (over ℂ), torsion-free one-relator. **Still open: torsion-free
CAT(0) groups**, among others.

The real unsolved problem is therefore not the SAT encoding — it is finding and certifying a
small torsion-free ambient group that no existing theorem already covers. That is a different and
harder task than the one I proposed.

Recent activity, none resolving it: Tabei (July 2026, non-unique-product minima in P);
Fisher–Ng (June 2026, new finite-index classes); Garg–Mineyev (rev. Sept 2025, restricted CAT(0)
search, states the conjecture open); Fisher–Sánchez-Peralta (2026, "still wide open").

## 4. Lonely runner — OPEN at 14 runners; my frontier was six years stale

I said "open for n ≥ 8". The actual recent history:

| Date | Result |
|---|---|
| Sep 2025 | Rosenfeld — 8 runners |
| Nov 2025 | Trakulthongchai — 9 and 10 runners |
| Dec 2025 | Rosenfeld, independently — 9 runners |
| Apr 2026 | Sungkawichai–Trakulthongchai — 11, 12 and 13 runners |

So the conjecture is proved through **13 total runners** and the smallest open case is **14
runners = 13 positive relative speeds**, target distance 1/14. Do not spend any compute on 8–13
except as an audit of the computer-assisted proofs (11–13 is an April 2026 preprint with public
code but no journal metadata).

Integer speeds are WLOG. But the best normalisation still leaves roughly **10²⁸⁶** possibilities,
so increasing-box brute force is worthless; only a structure-guided modular search has a chance.
The tight seed to work around is `{1,…,11,13,24}`.

## 5. Seymour second neighbourhood — OPEN, the most concrete target

Search floor is now **n = 19**, and at n = 19 the only live minimum outdegree is **δ⁺ = 8**
(δ⁺ ≥ 9 would force all 171 arcs, i.e. a regular tournament). Combined with the
degree-parametrised finite reduction of Zelenskyi–Darmosiuk–Nalivayko, a minimal counterexample
with δ⁺ = 8 must have

> **19 ≤ n ≤ 36**

which is a genuinely bounded, concrete SAT target — the only one of the six with both endpoints.

Caveat the sweep raises itself: the n ≥ 19 floor depends on two unrefereed 2026 preprints
(Brukhman, and Sadhukhan–Sandeep–Sen's δ⁺ = 7 case via OR-Tools CP-SAT). Peer-reviewed ground
truth is only Kaneko–Locke, δ⁺ ≤ 6. For a production search, independently check Brukhman's
five-page counting proof and rerun the CP-SAT models first.

The largest genuine whole-space brute-force enumeration located is only n = 7, in a withdrawn
2026 preprint.

## 6. Union-closed sets — OPEN but HOPELESS

First genuinely live exact slice is n = 13, m = 51, inside an enormous highly symmetric space with
no reason to contain a witness, and there is no bound on the size of a smallest counterexample —
so the search has no upper endpoint. Accumulated structural constraints plus exhaustive dead zones
make this a poor use of serious compute. My initial ranking of this as weakest was correct.

## Recommendation

Nothing should be launched at Casas-Alvero (proved) or union-closed (hopeless).

The highest-value single task is **auditing Jin's Crouzeix proof claim** — it is cheap, decisive
either way, and if the proof holds the target dies. Of the genuine search targets, **Seymour is
the only one with a bounded search space**; lonely runner needs structure before compute; and
Kaplansky needs a group-theoretic hunt rather than a SAT encoding.
