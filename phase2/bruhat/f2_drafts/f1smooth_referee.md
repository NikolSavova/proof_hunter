# Adversarial referee report — `f1smooth_draft.md`

*Referee pass, 2026-07-06. Blind protocol respected: no other `g1_*`/`g2_*`/`f1smooth_*`
file in `f2_drafts/` was read. All appendix scripts were re-typed verbatim from the
draft (absolute paths substituted) and re-run by the referee; independent spot-checks
were written by the referee. Ground truth: `mahonian.py`, `weyl.py`, `scaled.py`.*

## 0. Verdict

**MINOR REPAIRS.** Every numbered numeric check re-ran and PASSED except one
off-by-one in NC-3's *stated counts* (the underlying scan and its mathematical
conclusion are correct). Every lemma marked "proved" survived adversarial reading.
The two counterexamples (§2.1 B3/B4, §2.2 A1×D4) are exact and verified
independently of the draft's own scripts. The honest-GAP markers (GAP-1..GAP-4) are
accurate: what the draft says is proved is proved, what it says is open is open.

**Scope note for the parent (not a flaw of the draft):** this draft does **not**
close any gap in the F2 ledger (G1–G5 of `F2_PROOF_DRAFT.md`). It is the F1-smooth
side-bet (PROOF_PLAN.md item 2, "F1 holds for all rationally smooth lower
intervals"), and its own analytic core (Conjecture SD / SD′) is stated — correctly,
in the referee's judgment — to be *at least as hard as* [F2] Theorem A, which is
itself still gapped (G1+G2). Net dependency direction: this draft **consumes**
F2-grade machinery, it does not supply any. Its unconditional content is:
(i) two sharp counterexamples that force a corrected statement (irreducible +
simply-laced), (ii) exhaustive exact verification through rank 6, (iii) a genuinely
proved structural theorem for type A (staircase + domination, Lemmas 4.2/4.3,
Theorem 4.4, modulo the flagged citation package), and (iv) type A through
`m = 17` by finite exact check (Corollary B′).

**Statement fidelity vs the frozen wording.** The draft's rendition of F1-smooth
matches HANDOFF §F1 / PROOF_PLAN item 2 restricted to lower intervals of rationally
smooth elements — no silent strengthening or weakening. It then *disproves* the
statement as frozen and proposes the corrected irreducible version (§7) — the same
legitimate pattern as [F2]'s `c = 7/8 → 187/216` correction, with exact witnesses.

## 1. Numeric checks — all re-run by the referee

| # | What | Referee result |
|---|------|----------------|
| NC-1 | `mahonian.py --mmax 60` + Appendix D block 1 (Mahonian `r_m` strictly decreasing 4..60) | **PASS** — argmin central all m, varfit 0.8426→0.9821; block 1 prints `True` |
| NC-2 | Appendix A on B3, B4 | **PASS** — `B3: r(w0)=8/7 … violations=1 … runner-up=1.000000`, `B4: r(w0)=968/897 … violations=1` (verbatim match) |
| NC-3 | Appendix B reducible scan | **PASS with count error** — `TOTAL violations: 1`, unique in `A1xD4 r(w0)=1.137255`; but there are **27** reducible types (26 clean lines), not the claimed "28 types / 27 clean" — see Flaw F-1 |
| NC-4 | Appendix A on A2..A6, D4, D5, D6, E6 | **PASS** — all nine output lines match the draft's "expected output" **verbatim**, including `E6: r(w0)=13410244/13039321 smooth=2356 violations=0 equalities=0 dom-failures=0 factor-failures=0 runner-up=1.049667`. Runtimes far below the quoted 2/13/40 min on this machine (E6 ≈ 4 min) |
| NC-5 | Appendix C chordal mechanism, S3..S7 + 20,000 random chordal graphs | **PASS** — `smooth=6/22/88/366/1552`, all four failure counters 0, `0 / 20000` (≈3 min) |
| NC-6 | Appendix D block 2, SD box (max ≤ 12, len ≤ 9) | **PASS** — `511 staircase multisets; 91355 pairs; violations: 0 equalities: 0` |
| NC-7 | Appendix D block 3, exceptional/D-chain | **PASS** — `E6 13410244/13039321`, `E7 65523/64757`, `E8 82907598940321/82578730496656`; D4..D15 strictly decreasing, values match to 6 digits |
| NC-8 | Appendix E last block, Lemma 5.1 closed form to a,b ≤ 40 | **PASS** — `NC-8 exceptions: [] [] [Fraction(4, 1), Fraction(2, 1)]` |
| NC-9 | Appendix E final block, SD′ exhaustive m ≤ 17 | **PASS** — `proper = 2^{m-1}-2` for every m (6, 14, …, 65534), `viol=0 eq=0` throughout, `NC-9 PASS`; total proper pairs = 131,036 as claimed |
| §5.1 museum | Appendix E counts | **PASS** — `1286 multisets`, `887 / 574 / 0 / 18443 / 0 / 247` all exactly as claimed |

Referee's independent checks (not in the draft):

- `P_{D4} = [2][4][4][6] = (1,4,9,16,23,28,30,28,23,16,9,4,1)` recomputed from
  scratch; `r = 392/345` exact; `[2]P_{D4}` row and `r = 58/51` exact;
  `392·51 = 19992 < 20010 = 345·58` confirmed. **PASS.**
- B3 witness located directly in `weyl.py`: the **unique** palindromic lower
  interval with `r = 1` in B3 is the element with reduced word `s2 s3 s2 s3 =
  (s_{n-1}s_n)^2`, rank sequence `(1,2,2,2,1)`, exactly as §2.1 claims. **PASS.**
- §2.2's side claims **not covered by any appendix** (see Flaw F-2): referee
  verified `r([2]P_{E6}) = 7273/7072 = 1.0284219 < 1.0284465 = r(P_{E6})` (so
  A1×E6 indeed does *not* violate) and `r([2]P_{D5}) = 1.069231 < 1.069459 =
  r(P_{D5})` (matches the draft's floats). **PASS.**
- Gap arithmetic `58/51 − 392/345 = 6/5865 = 2/1955` confirmed by hand. **PASS.**

## 2. Lemma-by-lemma audit (attack notes)

- **Fact 1.1 / 1.2.** Quoted correctly; honestly downgraded by the draft itself to
  "citation details flagged (GAP-4)" with machine verification on all 7,152
  rank-≤6 smooth intervals (zero `factor-failures`, referee re-run). No circularity.
- **Lemma 1.3 (unique q-integer factorization + greedy correctness).** SOUND.
  Verified the cyclotomic argument line by line: `Phi_c | [c']_q ⟺ c | c'` for
  `c ≥ 2`; hence any dividing `[c]_q` has `c ≤ max c_i`, `[max c_i]_q` genuinely
  divides, the quotient after stripping is again a product, and the downward-
  induction multiplicity count gives uniqueness. The greedy in `qfactor` divides by
  the *largest* dividing q-integer, exactly matching the lemma; "greedy fails ⟹
  not a product" is the correct contrapositive. No hidden assumptions found.
- **Lemma 4.2 (gap-free back-degrees of chordal graphs).** SOUND. Checked:
  (i) PEO-independence via `chi_G(t) = prod (t − b_i)` is legitimate (roots of the
  chromatic polynomial); (ii) `G − x` connected when `x` simplicial — correct
  (neighbors pairwise adjacent, paths reroute); (iii) appending the simplicial
  vertex last is a valid elimination order and adds exactly `{d}`; (iv) the
  `max b(G−x) ≥ d−1` step via the last-ordered vertex of the `d`-clique is correct;
  (v) `d ≤ M′+1` preserves gap-freeness, and the `|G−x| = 1`/empty-multiset edge
  case works (`d = 1`). The disconnected reduction (multiset = union over
  components, each a full initial segment) is right because the multiset is
  order-independent. The MCS test in Appendix C (`back \ {last} ⊆ N(last)`) is the
  standard Tarjan–Yannakakis fill-in test on the MCS visit order, whose reverse is
  a PEO iff chordal — the code is a correct implementation, and its back-degrees
  are elimination degrees, so the `chi` factorization applies. 20,000-graph random
  test re-run: 0 failures.
- **Lemma 4.3 (domination).** SOUND and elementary: `b_i ≤ i−1`, at most `m−1`
  positive entries, counting form checks out for every `t ≥ 2`. The equivalence of
  Definition 1.6's two forms (sorted-pointwise vs counting) was verified by the
  referee in both directions (uses all parts ≥ 2 for the `|C| ≤ |D|` recovery).
- **Theorem 4.4.** Correct given Fact 4.1 (GAP-4). The equality clause
  (`E(v) = {2..m} ⟺ v = w0` via `sum(c−1) = ell(v) = binom(m,2)`) is right.
  Minor edge slop: for `v = e`, `E(v) = ∅` fails Definition 1.5's `min C = 2`
  literally (Flaw F-3, cosmetic; Theorem B routes `ell(v) < 2` around it).
- **Lemma 4.5.** SOUND: `|E(v)| = [q^1] P_v = |supp(v)|` is correct (each
  `[c]_q`, `c ≥ 2`, contributes exactly one `q`), and the rank-2 parabolic case
  analysis in simply-laced types is exhaustive (`A1×A1`, `A2`).
- **Lemma 5.1 (two-factor closed form).** SOUND; referee re-derived the
  cross-multiplications: rising-edge value `(a−1)^2/(a(a−2))` beats the corner
  `a/(a−1)` (difference of cross-products `−a^2+3a−1 < 0` for `a ≥ 3`) and the peak
  `a^2/(a−1)^2` (`−2a^3+6a^2−4a+1 < 0`). NC-8 confirms to 40. The draft's own
  confession that an earlier version had the wrong constant (caught by its NC) is
  the verification protocol working as intended.
- **Lemma 5.2, Lemma 5.3.** Both trivially correct as stated (termwise comparison;
  additivity of the counting form). Lemma 5.2's SD "prediction" is explicitly
  labeled heuristic — no silent use as a proof step anywhere.
- **Theorem A (rank ≤ 6 exhaustion).** The proof *is* the computation; the referee
  re-ran all of it (including E6, 51,840 elements) and got the draft's table
  verbatim, plus `equalities=0` establishing the "minimum at `w0` **only**" clause.
  The engine (`weyl.py`) carries four internal cross-checks, and type A is
  independently re-derived by Appendix C through `scaled.py` — a genuine
  cross-engine check for S3..S7.
- **Theorem B / Corollary B′.** The conditional logic is clean: SD (or the finite
  SD′ check) + Theorem 4.4 + Fact 1.2, strictness from the equality clauses. B′'s
  quantifier structure is honest — NC-9 checks **all** `2^{m−1}−2` staircase
  multisets `⪯ {2..m}` whether realizable or not, so no realizability lemma is
  needed. Note carefully (the draft says this, but it bears repeating): for
  `8 ≤ m ≤ 17` Corollary B′ still rests on the **unverified citation package**
  Fact 4.1 (machine-verified only for `m ≤ 7`); "unconditional" in the §0 summary
  is qualified three lines later, but a hasty reader could over-quote it.
- **Conjecture SD / Remark 5.0.** Stated as a conjecture, never used circularly:
  every unconditional claim (Theorem A, Corollary B′, the counterexamples,
  Lemmas 4.2–4.5, 5.1–5.3) was checked by the referee to be SD-free. The
  difficulty assessment ("contains Mahonian monotonicity, ≥ [F2] Thm A") is fair:
  consecutive-`m` Mahonian comparisons are decided at relative order `m^{−4}`,
  which needs [F2]'s sharp form *with constants* (G1+G2) — i.e., SD is not a
  shortcut around F2's gaps, and the draft never pretends otherwise.

## 3. Interface check vs [F2] (`F2_PROOF_DRAFT.md`)

The draft cites [F2] Lemmas 1.1, 1.3, 1.4, 1.5, 3.1–3.4, Cor. 2.3, NC-1. All exist
under exactly those numbers in the merged draft. Usage audit:

- **No [F2] lemma is load-bearing for any unconditional result here.** All [F2]
  citations sit inside GAP-1's *route sketch* (R1) or the difficulty assessment.
  This is the correct interface discipline: [F2]'s own gapped propositions
  (Prop 2.1/2.2 = G1, Prop 3.5 = G2) are never invoked as proved.
- Cor. 2.3 (used for the `m^{−4}` difficulty estimate) is itself "done modulo G1"
  in [F2] — acceptable, since it feeds only a heuristic difficulty claim, not a
  theorem.
- One route-level caveat the draft under-flags (inside GAP-1, so no verdict
  change): "[F2] L1.3's positive log-series holds verbatim" is true for the
  *identity*, but L1.3(ii)'s remainder-constant proof uses the specific gap-free
  run `j = 2..m` termwise; re-proving `S*_{2r+2} ≤ M^2 S*_{2r}` for a staircase
  multiset **with multiplicities** is easy but not literally "verbatim" (extra
  copies only help the inequality's LHS≤RHS direction — still, it must be
  rewritten). Similarly the L1.4 far-field transfer via `|phi_prod| ≤ |phi_block|`
  is only useful when `max C` is large relative to `sigma_C`; e.g. `C = {2^k}`-type
  staircases with tiny max get nothing from the Mahonian block and need the other
  factors' decay. Both points live squarely inside GAP-1's declared "heavy:
  G1+G2 for a family" and are noted here for the eventual prover.

## 4. Flaws found (ranked; none is fatal, none changes a theorem)

**F-1 (minor, factual miscount — the only failed check).** §2.2 and NC-3 claim
"ALL **28** reducible simply-laced types of rank ≤ 6" and expect "27 lines with
`violations=0`". The referee's enumeration (and the draft's own Appendix B code,
re-run) gives **27** types — by rank: 1 (rank 2) + 2 (3) + 4 (4) + 7 (5) + 13 (6)
— printing **26** clean lines + `A1xD4 … violations=1` + the TOTAL line.
Additionally NC-3's prose says Appendix B prints a "worst = `(1)x(1,4,9,16,…)`"
line; the script as given prints no such line. The scan itself, its uniqueness
conclusion (A1×D4 the only violating group, `(e, w0(D4))` the only violating
element — unique because the violating polynomial pair identifies unique
elements), and every printed number are all correct. Fix: 28→27, 27→26, drop or
implement the "worst" line.

**F-2 (minor, coverage).** §2.2 asserts the construction does not violate in
"`A1 x E6`" — but A1×E6 has rank 7 and is outside NC-3's rank-≤6 scan, so this
claim carries **no runnable NUMERIC CHECK** as written (house rule: every
quantitative claim gets one). Referee verified it independently:
`r([2]P_{E6}) = 7273/7072 = 1.0284219 < 1.0284465 = r(P_{E6})` — the claim is
TRUE. Fix: add the one-liner check or cite it as referee-verified.

**F-3 (cosmetic, definitional edge).** Definition 1.5 requires `min C = 2`, so
the empty multiset (`v = e`) is literally not a staircase multiset, while
Theorem 4.4 asserts "E(v) is a staircase multiset" for *every* rationally smooth
`v`. Harmless (Theorem B separately routes `ell(v) < 2`, and Appendix C's
`staircase()` accepts the empty multiset), but the definition should say
"empty, or min = 2 and gap-free".

**F-4 (cosmetic, wording).** Theorem A's remark "worst relative margin ~1.0% at
A6/D6": the measured margins are A6 ≈ 0.97%, D6 ≈ 1.86%, E6 ≈ 2.06% — the worst
is A6 alone; D6 should not be listed at ~1.0%.

**F-5 (cosmetic, resolved discrepancy).** Remark 3.1: "the E6 exponent-multiset
landscape (83 distinct multisets)". Referee measures **85** distinct `E(v)` over
all 2,356 rationally smooth E6 intervals *including* the two trivial multisets
`∅` (v = e) and `{2}` (length-1); 83 is correct only under the unstated
convention of excluding those two. The runner-up multisets are confirmed exactly:
E6 `{2,5,5,6,8,8}` (r = 1.049667) and D6 `{2,4,5,6,6,8}` (r = 1.060074).

**F-6 (cosmetic).** §0.2/§3 headline "7,152 rationally smooth lower intervals in
these groups" over the list "A1..A6, D4, D5, D6, E6": 7,152 = the table's sum
*excluding* A1's two (trivial) intervals; with A1 it is 7,154. The table's
footnote handles it; the §0 phrasing doesn't.

**No unmarked gaps found.** Every unproven step is carried by an explicit GAP
marker (GAP-1 SD/SD′; GAP-2 type D ≥ 7; GAP-3 E7/E8; GAP-4 citations) or an
explicit "conditional"/"modulo" qualifier in the theorem statement itself. In
particular the draft nowhere uses Conjecture SD, Fact 1.2/4.1 beyond their
declared scope, or any gapped [F2] proposition, in an unconditional claim.

## 5. What the draft establishes (referee-confirmed summary)

1. **F1-smooth as frozen is FALSE** — two independent, exact, referee-reproduced
   counterexample families (B3/B4 dihedral plateau; A1×D4 reducible, `2/1955`
   gap). The corrected statement (§7: irreducible + simply-laced) is the right
   upstream propagation, exactly analogous to [F2]'s `7/8 → 187/216` correction.
2. **Corrected F1-smooth is PROVED for every irreducible simply-laced group of
   rank ≤ 6** (7,152-interval exact exhaustion, minimum uniquely at `w0`),
   and **for type A through `S_17`** modulo only the Fact 4.1 citation package
   (fully machine-verified for `S_3..S_7` by two independent engines).
3. **Genuinely new proved structure:** staircase property (Lemma 4.2, a clean
   chordal-graph induction) + domination (Lemma 4.3) of type-A exponent
   multisets; the false-lemma museum (§5.1) is a valuable negative map with every
   count reproduced.
4. **Open core, honestly priced:** Conjecture SD/SD′ (0 violations in 91,355 +
   131,036 exact instances) is at least F2-Theorem-A-hard; type D ≥ 7 and E7/E8
   need new structure/tooling. This draft does not close any F2-ledger gap and
   does not claim to.

## 6. Checks index (referee re-runs, 2026-07-06)

| Check | Result |
|---|---|
| NC-1 (mahonian --mmax 60 + strict decrease) | PASS |
| NC-2 (B3/B4) | PASS, verbatim |
| NC-3 (reducible scan) | **numbers PASS; stated type/line counts wrong (F-1)** |
| NC-4 (A2..A6, D4..D6, E6 exhaustion) | PASS, all rows verbatim |
| NC-5 (chordal mechanism S3..S7 + 20k random) | PASS |
| NC-6 (SD box 511/91,355) | PASS |
| NC-7 (E6/E7/E8 exact + D4..D15 chain) | PASS |
| NC-8 (Lemma 5.1 to 40) | PASS |
| NC-9 (SD′ exhaustive m ≤ 17, 131,036 pairs) | PASS, `NC-9 PASS` |
| §5.1 museum counts (887/574/0/18443/0/247) | PASS |
| Referee extras: P_D4 row + fractions; B3 witness word `(s2 s3)^2`; A1×E6 and A1×D5 non-violations; gap `= 2/1955`; E6/D6 runner-up multisets | PASS (F-5 convention noted) |

**Referee verdict: accept after the §4 minor repairs.** The unconditional content
is correct and reproducible to the digit; the conditional content is labeled as
such; the counterexamples should be propagated upstream to HANDOFF/PROOF_PLAN
(F1's wording must add *irreducible*, and any F1 proof strategy must avoid
reducible parabolic intermediates — the draft's §2.2 warning is load-bearing).

*End of referee report.*
