# START HERE — what we are trying to prove, from scratch

> **Audience:** you know linear algebra and group theory (and some algebra), but nothing about
> this field. This file gets you from zero to understanding the conjecture, why it's open, and
> what our code does. The field is **algebraic combinatorics**, subfield **Coxeter group
> combinatorics** (Bruhat order). Reading time ~20 minutes.

---

## 1. The one-sentence version

For every "Weyl group" W and every interval [u,v] in its "Bruhat order", count the elements
level by level; **Brenti's Conjecture 2.11** says this sequence of counts a₀, a₁, …, a_d always
satisfies **aₖ² ≥ aₖ₋₁·aₖ₊₁** (log-concavity). We are hunting a counterexample and, failing
that, verifying every group anyone can exhaustively check — both outcomes are publishable.

---

## 2. The objects, built up from what you know

### Coxeter groups (generalized reflection groups)
A **Coxeter group** W is a group with a chosen finite set of generators S = {s₁,…,sₙ}, subject
ONLY to relations of the form
- sᵢ² = e (each generator is an involution — think "reflection"), and
- (sᵢsⱼ)^{m(i,j)} = e for some integers m(i,j) ≥ 2 (how two reflections interact).

**Concrete example you already know:** the symmetric group Sₙ with sᵢ = the adjacent
transposition (i, i+1). Here (sᵢsᵢ₊₁)³ = e and non-adjacent generators commute. This is the
Coxeter group "of type A_{n−1}".

**Weyl groups** are the Coxeter groups that arise as symmetry groups of *crystallographic root
systems* (equivalently: they preserve a lattice — they're the reflection groups of Lie theory).
The complete list of irreducible ones:

| Type | Concrete description | Order |
|------|----------------------|-------|
| Aₙ | symmetric group S_{n+1} | (n+1)! |
| Bₙ (=Cₙ) | signed permutations of {1..n} | 2ⁿ·n! |
| Dₙ | signed permutations, even # of sign changes | 2^{n−1}·n! |
| E₆, E₇, E₈, F₄, G₂ | exceptional | 51840, 2903040, 696729600, 1152, 12 |

Non-examples (Coxeter but NOT Weyl): the symmetry groups H₃ (icosahedron), H₄, and most
dihedral groups. **This distinction is the heart of the problem** — see §4.

### Length
For w ∈ W, the **length** ℓ(w) = the least number of generators needed to write w. In Sₙ this
is exactly the number of inversions of the permutation. A shortest expression is a **reduced
word** (our files print elements this way: "121" means s₁s₂s₁).

### Bruhat order
A partial order ≤ on W. The cleanest definition: **u ≤ v iff some reduced word of v contains a
reduced word of u as a subword** (delete letters, keep order). Intuition: v "dominates" u —
you can get from v down to u by breaking it at reflections, dropping length each time. It is
graded by ℓ. (Where it comes from: containment of Schubert cells in flag varieties — this
geometric origin is why people care, but you don't need it to work on the problem.)

### The interval and its rank sequence
For u ≤ v, the **Bruhat interval** is [u,v] = {z : u ≤ z ≤ v}, and its **rank sequence** is

    aₖ = #{ z ∈ [u,v] : ℓ(z) − ℓ(u) = k },   k = 0, 1, …, d = ℓ(v) − ℓ(u).

So (a₀,…,a_d) counts the interval level by level; always a₀ = a_d = 1.

**Worked example (S₃ = A₂):** the full interval [e, w₀] contains all 6 elements, with lengths
0,1,1,2,2,3 → rank sequence (1,2,2,1). Log-concave: 2² ≥ 1·2. ✓

### Log-concavity
A sequence is **log-concave** if aₖ² ≥ aₖ₋₁·aₖ₊₁ for all interior k. Stronger than unimodality
(rises then falls) for positive sequences. Log-concavity results are a major theme in modern
combinatorics (June Huh's 2022 Fields Medal was for exactly this kind of statement in matroid
theory) — which is part of why a resolution here would find an audience.

---

## 3. The conjecture (our target)

> **Conjecture 2.11** (F. Brenti, *Some open problems on Coxeter groups and unimodality*,
> OPAC / Proc. Sympos. Pure Math. 110; restated as Problem #13 in his survey arXiv:2410.09897).
> **Let W be a Weyl group and u ≤ v in W. Then the rank sequence of [u,v] is log-concave.**

Open for 20+ years. **Known before us** (all by Brenti, via Maple, reported in the OPAC paper):
Aₙ (n≤5), Dₙ (n≤5), Bₙ (n≤4), B₅ only for intervals of length ≥ 20, F₄, dihedral groups.

**Our new results (this repo, 2026-07):** exhaustively verified — **A₆, A₇, B₅ (complete),
D₆**, with **B₆, E₆** in progress. All pass so far. Every result file is in `results/`.

---

## 4. Why "Weyl" matters: the conjecture is FALSE just outside

For general finite Coxeter groups the statement **fails**: Brenti gives an explicit interval
in **H₃** (icosahedral symmetry — not crystallographic, so not Weyl) with rank sequence

    (1, 3, 5, 7, 10, 10, 5, 1):   7² = 49 < 5·10 = 50.  ✗

It fails **by exactly 1**. Two lessons: (a) any proof must actually use the crystallographic /
lattice property, not just reflection-group formalities; (b) failures, if they exist in Weyl
groups, will be hairline — which tells us *how* to hunt (see §5).

**Our sharpest empirical finding so far** (`results/`): in non-simply-laced Weyl groups
(B, F₄, G₂ — those with m(i,j) ≥ 4) the inequality is achieved with **exact equality** (rank
sequence (1,2,2,2,1) inside dihedral-type sub-intervals). In simply-laced groups (A, D, E — all
m(i,j) ≤ 3) the minimum of aₖ²/(aₖ₋₁aₖ₊₁) **decays toward 1 like a power law in the rank**:
A-series 1.389 → 1.210 → 1.122 → 1.079 → 1.054 (A₃…A₇); D-series 1.136 → 1.069 → 1.041
(D₄…D₆); E₆ ≤ 1.0285 (partial run). The minimizing intervals are always lower intervals [e,v]
with "staircase"-shaped v. **Either this decay never crosses 1 (then proving a quantitative
bound ratio ≥ 1 + c/n^α is a real theorem), or it dips below 1 at some rank just beyond
exhaustive reach (then there is a findable counterexample).** Deciding which is the game.

---

## 5. Our attack (and where each of us fits)

1. **Exhaustive tier (done/finishing, Claude):** check EVERY interval in every Weyl group up to
   |W| ≈ 50k. One trusted ~50-line checker + a generic group builder with four independent
   internal cross-checks (`weyl.py`, `verify.py` — see §7). A single failed inequality = a
   counterexample = a complete self-certifying result (just the pair (u,v) + a recount).
2. **Scaled hunt (Sihao):** beyond exhaustion (A₈–A₁₂, D₇–D₉, E₇), *search* instead of
   enumerate: sample lower intervals [e,v] with staircase-shaped v, minimize the log-concavity
   ratio (OpenEvolve/heuristics). Fitness < 1 = result.
3. **Structural tier (Nikol):** (a) prove the equality-case characterization (equality ⇔
   the (1,2,2,2,1) dihedral pattern ⇔ non-simply-laced — looks provable directly); (b) attack
   the quantitative version on the explicit staircase family from §4. Even a partial result
   here upgrades the computational note into a real paper.
4. **Writeup:** verification note (new frontier + code + certificates) with the structural
   section; venues suggested by the prior-art dossier: Electron. J. Combin., Sém. Lothar.
   Combin., Experimental Math.

**Prior-art status (checked fresh 2026-07-03, two independent web sweeps — see
`results/priorart_gpt55_63405.md`):** open; nobody has claimed any of our new cases; closest
recent work is asymptotic (Burrull–Gui–Hu, arXiv:2311.17980, affine setting, Brunn–Minkowski).

---

## 6. Learning resources, in order (assuming your background)

1. **Federico Ardila — "Coxeter Groups" video course** (YouTube, free). Gentlest real entry;
   from zero through Bruhat order. Watch the first ~10 lectures alongside item 2.
2. **J. Humphreys, *Reflection Groups and Coxeter Groups*** (CUP). Standard first book;
   Part I needs only linear algebra + group theory. Chapters 1, 5 matter most for us.
3. **A. Björner & F. Brenti, *Combinatorics of Coxeter Groups*** (Springer GTM 231). THE
   reference for this exact problem. **Chapter 2 (Bruhat order) is the core reading**; Ch. 1
   for foundations. Everything `weyl.py` computes is defined here.
4. **F. Brenti, survey arXiv:2410.09897** — where our conjecture lives (and the source our
   pipeline extracted it from). Short; read after 1–3.
5. Context on why log-concavity is a big deal: **J. Huh, "Combinatorics and Hodge theory"**
   (ICM 2022 address, free PDF) and **R. Stanley, "Log-concave and unimodal sequences in
   algebra, combinatorics, and geometry"** (classic survey).
6. Hands-on: **Sage** has all of this built in —
   `W = WeylGroup(['A',3]); [len(W.bruhat_interval(u,v)) ...]` — poking at real intervals makes
   Björner–Brenti Ch. 2 click. Our `weyl.py` is a readable from-first-principles implementation
   of the same definitions (and is cross-checked against known formulas four different ways).

---

## 7. Map of this directory

| File | What it is |
|------|-----------|
| `START_HERE.md` | this file |
| `weyl.py` | builds any Weyl group from its Cartan matrix: elements, lengths, reflections, Bruhat order (up/down-sets as bitsets). Four independent self-checks: known group order, BFS-length ≡ inversion-count, level sizes ≡ Poincaré polynomial, known root count. |
| `verify.py` | the actual checker: enumerates all intervals, tests aₖ² ≥ aₖ₋₁aₖ₊₁, reports violations + the two near-miss statistics (min margin, min ratio). `--from-u N` resumes a killed run; `--progress K` prints checkpoints. |
| `priorart_check.py` | one-off gpt-5.5+web prior-art sweep (the Erdősgate rule: always re-check before writing up). |
| `results/` | append-only run outputs — one file per run, never overwritten. `priorart_gpt55_63405.md` is the full prior-art dossier. |
| `logs/` | (gitignored) live logs of long detached runs. |

**House rules that apply here:** a counterexample triggers an immediate 5-minute prior-art
re-check, then independent re-verification (separately written code + Sage) before anyone says
the word "result". Never ship a single-model claim. All outputs append-only.
