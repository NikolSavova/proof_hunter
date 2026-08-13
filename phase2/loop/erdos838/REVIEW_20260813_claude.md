# Skeptical review of the 1/2 upper-bound paper — Claude Opus 5, 2026-08-13

*Read the 10:58 version of `paper/main.tex`. Sol was still editing, so line references may have
moved; section and lemma numbers are from that version. I deliberately did not edit `main.tex` —
everything below is a suggestion for whoever owns the file next.*

**Summary: the mathematics holds up under independent check, and the novelty claim survives a
reading of Baek–Balko. There is one serious citation problem that a referee will find on page one,
and one gate that must be cleared before submission.**

---

## 1. What I verified independently

I wrote `independent_check.py` **without reading `verify.py` or `lexicographic_blowup.py`**, so
agreement is evidence rather than a shared bug. It rebuilds `T_{4,2}` from the strong-separation
operation, forms the 36-point composition with exact rational coordinates, and counts caps, cups
and convex subsets **from orientation determinants only** — the substitution formulas never appear
in the counting path.

**Result: the direct count returns exactly `(C,U,W) = (14136, 14136, 441399)`,** matching both
Lemma 2.2's formulas and the value printed in §"Verification artifact".

One incident worth recording, because it validates a hypothesis the paper leans on. My first run
*disagreed*: I had used `eps = 1/97`, which broke general position. That was my bug — but it shows
the "sufficiently small `eps`" condition is load-bearing rather than cosmetic. At `eps = 1/1000`
the set **is** in general position yet gives a different and wrong count (`C = U = 14058`); the
value stabilises only from `1/10^5` downward. If the paper wants a stronger artifact, stating an
explicit threshold for `eps_0` in terms of the template's coordinate separations would close a gap
that currently reads as "choose it small enough".

Also re-derived by hand and confirmed:

- **Lemma 2.1**, rules 3 and 4 — the `−eps·Δy·(z_x − p_x)` term dominating the `eps²` term. Correct.
- **Prop 3.1**, equations (3.5)–(3.9), including the telescoping and the `s = d` dominant-summand
  argument. Correct.
- **The coefficient arithmetic.** With `a = b = k−1` and `r = C(2k−4, k−2)`, the coefficient is
  `(k−2)/log₂ C(2k−4, k−2)`, which decreases to `1/2` **from above**: 0.7737, 0.6526, 0.5860,
  0.5441, 0.5238, 0.5108, 0.5033 at `k = 4, 6, 10, 20, 40, 100, 400`. So `limsup ≤ inf_k = 1/2` is
  valid and never attained at finite `k`. Worth a sentence in the paper — a reader checking `k = 4`
  and seeing 0.77 may think the claim is backwards.
- **Prop 4.4**, the barrier. `r ≤ C(a+b−2, a−1) ≤ 2^{a+b−2}` is the right application of the
  cup–cap theorem with forbidden sizes `a+1, b+1`. Correct, and it is the nicest thing in the paper:
  no fixed-template iteration can beat 1/2.
- **Lemma 4.2** (Pascal cell cap/cup sizes), by induction. Correct.
- **Lemma 5.2**, all three steps: the Cauchy–Schwarz form `√((p+r)(q+t)) ≥ √(pq) + √(rt)`, the
  Bernoulli bound `(m_i/2)^{d_i} ≤ 1 + d_i(m_i/2 − 1) ≤ s_i + 1` via `d_i ≤ 2s_i/m_i`, and the
  identity `Σ d_i t_i = ((log s)² + Σ d_i²)/2`. All correct.

**Not verified:** the multiscale reset argument inside the proof of Theorem 5.1 — the `q_*`
counting and its two alternatives. It is the most intricate page and I did not check it. Theorem 1.1
does not depend on it.

---

## 2. Baek–Balko: the novelty survives

I read the SoCG 2025 version of *The Erdős–Szekeres Conjecture Revisited*
([DROPS, LIPIcs.SoCG.2025.13](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/LIPIcs.SoCG.2025.13/LIPIcs.SoCG.2025.13.pdf)).

**They never count convex subsets.** Their Lemma 14 delivers exactly two things about an
`(X,Y)`-blow-up: that it contains **no `k` points in convex position**, and its **cardinality**,
as a sum of binomials. A full-text search for counting language returns a single hit, and it is a
binomial identity inside an unrelated proof. Nothing in the paper computes, or sets up machinery to
compute, the *total number* of convex subsets.

So the substitution identities of Lemma 2.2 are not implicit in their work, and extracting a
convex-subset count from their framework would require precisely those identities. **This does not
fall out in three lines.** That was the specific risk worth checking and it does not fire.

---

## 3. The serious problem: the decomposable class is theirs

Baek–Balko, Section 4:

> "A set `P` is **decomposable** if either `|P| = 1` or if `|P| ≥ 2` and `P` can be partitioned into
> two decomposable sets `A` and `B` such that `A` is **deep below** `B`."

`main.tex` §5:

> "Call a point set **strongly decomposable** if it is a singleton, or if it has a realization
> `A ≺ B` in which `A` and `B` are strongly decomposable."

**Same class.** Their "deep below" (`B` above every line through two points of `A`, and `A` below
every line through two points of `B`) is our `≺` up to a 180° rotation: they get *cap = one point of
`A` + cap of `B`*, we get *cap of `A` + one point of `B`*, which is the same condition with caps and
cups and the left–right order both swapped. The class is closed under that rotation.

And they **prove a theorem about it** — their Theorem 8: every decomposable set of more than
`Σ_{i=k−a+2}^{u} C(k−2, i−2)` points contains an `a`-cap, a `u`-cup, or `k` points in convex
position; hence the Erdős–Szekeres conjecture holds on this class.

`main.tex` currently cites them only for "almost-vertical blow-ups tailored to the Erdős–Szekeres
problem" (§1). It does not credit them for the class that Theorem 5.1 is built around.

**Second, smaller instance of the same issue.** The Pascal cells are the classical Erdős–Szekeres
sets. I checked the parameters: `T_{m,i} = P(i+2, m−i+2)`, with `|T_{m,i}| = C(m,i)` matching
`|P(a,u)| = C(a+u−4, a−2)`. Baek–Balko use these by name, denote them `P(a,u)`, and explicitly
observe that they are decomposable. §4 of `main.tex` presents `T_{m,i}` as "the standard cup–cap
examples", which is right in substance but should name them.

### Suggested repairs

1. **Adopt their terminology.** Rename "strongly decomposable" to "decomposable", or if a
   distinction is genuinely intended, state precisely what it is and why a new name is needed.
2. **Credit the class at its definition** in §5, citing Baek–Balko Section 4.
3. **Position Theorem 5.1 against their Theorem 8 explicitly.** These are different statements
   about the same class — theirs bounds the size before a `k`-gon appears, ours bounds the total
   convex-subset count from below. Saying so *strengthens* the paper: it shows the class is
   established and independently interesting, and it makes the contribution legible.
4. **Name `T_{m,i}` as `P(a,u)`** in §4 with the parameter dictionary above.

None of this touches correctness. All of it is embarrassing if a referee finds it first and trivial
if fixed now.

---

## 4. Gate before submission

**I read the SoCG extended abstract, which states "The proof of Theorem 8 is omitted" and "The proof
of Lemma 14 is omitted."** The full version is *J. Combin. Theory Ser. A* **222** (2026) 106195,
paywalled on ScienceDirect.

My clearance is therefore on the conference version only. The omitted proofs are exactly where
blow-up bookkeeping would live, so the journal version must be read before submission. Clearing a
novelty claim against a partial source is what cost this project the Bregman Part II result on the
morning of 2026-08-13; the same mistake is available here and should not be repeated.

---

## 5. Two framing notes

- The paper is honest that it does **not** answer Erdős–Hammer: the window moves from `[1/4, 1]` to
  `[1/4, 1/2]` and existence of the limit stays open. Keep that prominent; it is the paper's main
  defence against overclaiming.
- The **Székely coincidence** (§1, and `prior_art_20260812.md`) is currently recorded as a
  curiosity — "the same base-normalized coefficient occurs … but no transfer between the two
  settings is known". Two constants agreeing at `1/2` in a Ramsey-type counting problem is either a
  shared mechanism or a coincidence, and a referee will ask which. Worth resolving rather than
  noting.

---

## 6. Bottom line

A real theorem, competently proved, with a matching barrier showing the method is exhausted at
`1/2`. The verification artifact reproduces under an independent implementation. The novelty claim
survives the reading of Baek–Balko that mattered.

Fix the citation of the decomposable class, get the JCTA version, and this is a solid short paper.
