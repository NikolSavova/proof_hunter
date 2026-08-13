# AI-resolved results, 2022–2026, and what they unlock

*Sihao's strategy, 2026-08-13: rather than picking an open problem and attacking it, inventory the
results AI has recently resolved and mine their downstream consequences.*

## Why this is the right shape of bet

Three structural reasons this beats picking a famous open problem:

1. **Recency.** Almost everything below is 2025–2026. The implication chains pointing at these
   statements were written over decades by people who assumed the statements were true (or open).
   Nobody has had time to walk them.
2. **The finders are not the domain experts.** A system that constructs a counterexample does not
   thereby know the fifty papers whose theorems were conditional on it. Consequence-mining is a
   literature-and-implication task, which is the thing a well-read model is actually good at, and
   it is *construction*-shaped rather than *search*-shaped — the lesson of the Seymour dead end.
3. **The gap is documented.** Quanta's 2026-08-03 survey of Erdős problems falling to AI covers
   who solved what and how the field feels about it. It says **nothing** about downstream
   consequences. Neither does most of the coverage.

**The edge is inversely proportional to publicity.** The Jacobian aftermath is being mined right
now by everyone who read Tao's digestion. The quieter results are where the unclaimed work is.

## Inventory

| # | Result | System / people | Date | Type |
|---|---|---|---|---|
| 0 | **Hadamard matrices** for all 12 previously-unknown admissible orders < 2000 | Alpöge, Voinov, Reynolds-Haertle + Claude | ~2026-08-11 | construction — **artifact not locatable** |
| 1 | **Jacobian conjecture** false in dim ≥ 3 | Alpöge + Claude Fable 5 | 2026-07-20 | counterexample |
| 2 | **Erdős unit distance conjecture** false | OpenAI internal model; refined by Will Sawin | 2026-05-20 | counterexample |
| 3 | Unit distance, strongest form | Anthropic system, autonomous | 2026 | counterexample |
| 4 | **Sum–product conjecture variant** false over ℝ | Bloom + 3 others | 2026-05 | disproof |
| 5 | **Kissing number, dim 11** ≥ 593 (was 592) | AlphaEvolve | 2025-11 | construction |
| 6 | **Erdős minimum overlap**, new upper bound | AlphaEvolve | 2025-11 | construction |
| 7 | **Kakeya sets**, new constructions dim 3,4,5 | AlphaEvolve | 2025-11 | construction |
| 8 | ~20% of 67 problems improved | AlphaEvolve (arXiv:2511.02864, w/ Tao) | 2025-11 | constructions |
| 9 | Erdős **1196** (primitive sets) | Price, Barreto, Tao, Lichtman | 2026-05 | proof |
| 10 | Erdős **728** (divisibility of factorials) | Barreto, Price + GPT-5.2 Pro | 2026-01-04 | proof |
| 11 | Three further Erdős problems | OpenAI Astra | 2026-08-01 | unspecified |
| 12 | Erdős **333** | Barreto, Price + GPT-5.2 | 2025-12 | proof — *later found to be Erdős's own, 1977* |

Item 12 is a cautionary entry: an AI "resolution" that turned out to be in the literature already.
It is the Erdősgate failure mode, and it is why every item here needs a sweep before work starts.

## Item 0 — the Hadamard result, and why it is BLOCKED (2026-08-13)

The best-shaped target we have found, and currently unusable.

**The claim.** Alpöge, with Philippe Voinov, Saul Reynolds-Haertle and Claude, posted matrices for
all admissible orders below 2000 that had no known Hadamard matrix — the twelve orders
**668, 716, 892, 1132, 1244, 1388, 1436, 1676, 1772, 1916, 1948, 1964** — moving the smallest
unknown order to 2004 or beyond. Order 668 had been the smallest open case since 428 fell in 2004.

**Why it is the right shape.** It is a CONSTRUCTION, not a counterexample, which inverts the
downstream economics: counterexamples close doors (the Jacobian was a terminal node; unit distance
turned out not to be a hub at all), whereas every theorem of the form "if a Hadamard matrix of
order n exists, then …" now fires for twelve new orders, and that conditional literature in design
theory and coding theory is large and load-bearing. And the central question is unanswered:
**is it an improved search or a general construction?** If general, it need not stop at 2000.

**Why it is blocked.** After four searches I can find **no verifiable artifact**:

- no arXiv preprint;
- no repository or data file;
- Wikipedia states the result with **no citation and no external link**;
- Epoch AI marks it *provisionally* solved, says it was "posted in the form of a puzzle", and
  provides no download;
- TheoremDB's packet still records 668 as unresolved — but that packet was reviewed **2026-07-24**,
  before the announcement, so it is stale rather than contradictory.

**This blocks the whole plan.** The differentiator was local structural analysis of the matrices —
do they factor through Williamson, Goethals–Seidel, Baumert–Hall or Paley arrays, or something
new — and that is what answers "search or construction". Without the matrices there is nothing to
analyse. Note the asymmetry: obtaining them is the hard part; **verifying one is a single matrix
multiply**, `H Hᵀ = 668·I`.

**Standing rule applies.** This project ships a verification artifact with every result. We would
be building on an uncited social-media claim. The result is very likely real — Alpöge has the
Jacobian track record — but "likely real" is not the standard, and the failure mode here is the
mirror image of Erdősgate: not missing an existing result, but building on an unverified one.

**The unblocking action is human, not computational.** Someone with X access should retrieve the
post and the puzzle. That is a two-minute task for Sihao and is currently gating everything.

**Related and properly documented, if this stays blocked:** *Generating Hadamard matrices with
transformers*, arXiv:2604.11101 (April 2026), and Cati's *A database of constructions of Hadamard
matrices*, arXiv:2411.18897 — a real database, which is exactly the reference object we would need
to classify the new matrices against.

## Ranked by downstream value

### 1. The unit distance disproof — the richest target, and I think under-mined

Erdős (1946) conjectured that `n` points in the plane determine at most `c·n^{1+o(1)}` unit
distances. **This is now false**: infinite families beat it by an explicit polynomial factor,
`n^1.014` after Sawin's refinement. See arXiv:2605.20695, *Remarks on the disproof of the unit
distance conjecture*, and Gil Kalai's write-up.

The technique is the interesting part: **algebraic number fields and Golod–Shafarevich towers**,
with ideas traceable to Ellenberg–Venkatesh and Hajir–Maire–Ramakrishna. That is a cross-domain
import — class field theory into discrete geometry — and it is exactly the representation shift
that made the Jacobian counterexample findable.

Two independent reasons this is the best target:

**(a) Unit distance bounds are an INPUT to other theorems, not just an output.** A false upper
bound propagates. Everything conditional on `n^{1+o(1)}` needs revisiting, and unlike the Jacobian
case the affected literature is large and applied (incidence geometry, additive combinatorics).

**(b) The Hadwiger–Nelson connection, which I have not seen anyone mention.** The chromatic number
of the plane is *exactly* the chromatic number of the unit-distance graph on ℝ². De Grey's 2018
1581-vertex graph gave χ ≥ 5; the bound has sat at 5 ≤ χ ≤ 7 since. If the new constructions
produce unit-distance graphs that are **denser than anyone believed possible**, they are candidate
substrates for a better lower bound. Denser unit-distance graphs are precisely what you feed a
χ ≥ 6 argument. This is speculative and I may be missing an obstruction — but it is concrete,
checkable, and construction-shaped rather than search-shaped.

Other threads: the Erdős **distinct** distances problem (Guth–Katz), whether the same
Golod–Shafarevich machinery refutes other incidence conjectures, and higher-dimensional unit
distance bounds.

### 2. AlphaEvolve's constructions — quiet, and constructions feed theorems

Items 5–8 got a fraction of the Jacobian's attention, and a new construction is exactly what
unlocks a theorem whose hypothesis it now satisfies.

- **Kakeya, dim 3–5.** The 3D Kakeya conjecture fell to Wang–Zahl (2025). Kakeya connects directly
  to restriction and Bochner–Riesz in harmonic analysis. New constructions with better constants
  bear on those bounds. This is the one I would look at hardest after unit distance.
- **Kissing number dim 11 = 593.** Feeds lattice and code bounds; small but concrete.
- The other ~13 improved constructions among the 67 have had essentially no downstream attention.

### 3. The Jacobian aftermath — already in flight, and probably crowded

Two lanes running (`jacobian/scripts/downstream.py`). My expectation is that Dixmier and the
"X implies JC" corollaries are gone, and the live item is the explicit Bass–Connell–Wright cubic
or Druzkowski counterexample, since that requires computation rather than an observation.

### 4. The Erdős proofs (9, 10, 11) — lowest value

Individually narrow, and Erdős problems are famously self-contained; that is the point of them.
Little propagates.

## Recommendation

**Unit distance first.** It is three months old rather than three weeks, so the initial rush has
passed; the technique is transplantable; and the Hadwiger–Nelson angle is a specific, testable
question rather than a hope. **Kakeya/AlphaEvolve second.**

Sequencing, to respect budget: let the two Jacobian lanes land first, then run one sweep on the
unit distance downstream. Do not fan out across all twelve — item 12 is the reminder that each
one needs a real kill-search, and a broad fan-out would produce twelve shallow sweeps instead of
one useful one.

## Sources

- [Quanta, *Why the Legendary Erdős Problems Are Falling to AI*](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/)
- [Gil Kalai, *Erdős' Unit Distance Problem was Disproved!*](https://gilkalai.wordpress.com/2026/05/21/amazing-erdos-unit-distance-problem-was-disproved-it-was-achieved-by-ai/)
- [*Remarks on the disproof of the unit distance conjecture*, arXiv:2605.20695](https://arxiv.org/abs/2605.20695)
- [OpenAI, remarks PDF](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-remarks.pdf)
- [*Mathematical exploration and discovery at scale*, arXiv:2511.02864](https://arxiv.org/abs/2511.02864)
- [Tao, *Mathematical exploration and discovery at scale*](https://terrytao.wordpress.com/2025/11/05/mathematical-exploration-and-discovery-at-scale/)
- [Tao, *A digestion of the Jacobian conjecture counterexample*](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)
