# F1 for rationally smooth elements — side-bet draft

*Blind draft, 2026-07-06. Protocol respected: no other `g1_*` / `g2_*` / `f1smooth_*`
file in `f2_drafts/` was read. Inputs: `F2_PROOF_DRAFT.md` (cited below as [F2] with
its lemma numbers), `F2_SPEC.md`, and the exact harnesses `mahonian.py`, `weyl.py`,
`scaled.py`, `scaled_general.py`. Every quantitative claim carries a NUMERIC CHECK
runnable from `phase2/bruhat/` (self-contained code in Appendices A–E).*

**Task (F1-smooth).** If `v` is rationally smooth in a finite simply-laced Weyl group
`W` (equivalently, by Carrell–Peterson, the rank sequence of `[e,v]` is palindromic),
then `min-ratio([e,v]) >= min-ratio([e,w0])`, where for a rank sequence
`(a_0,...,a_N)` we write `r(a) := min_{1<=k<=N-1} a_k^2/(a_{k-1}a_{k+1})`
(`r := +infinity` when `N < 2`).

---

## 0. Verdict and results at a glance

1. **F1-smooth AS STATED IS FALSE.** Both hypotheses are sharp and a third one is
   missing:
   - *simply-laced is necessary*: in `B3` (and `B4`) the interval
     `[e, (s_{n-1} s_n)^2]` with rank sequence `(1,2,2,2,1)` is rationally smooth and has `r = 1` exactly,
     below `r(w0(B3)) = 8/7` (§2.1);
   - *irreducibility is necessary* (**new counterexample**): in `W = A1 x D4` the
     element `v = (e, w0(D4))` is smooth (not just rationally smooth), and
     `r([e,v]) = 392/345 = 1.13623... < 58/51 = 1.13725... = r([e,w0])` (§2.2).
     This also refutes the unrestricted F1 for reducible simply-laced `W`.
2. **Theorem A (unconditional).** F1-smooth holds, with the minimum attained at
   `v = w0` **only**, for every *irreducible* simply-laced Weyl group of rank <= 6:
   `A1..A6, D4, D5, D6, E6`. Proof: exhaustive exact (integer/Fraction) computation
   over all 7,152 rationally smooth lower intervals in these groups (§3). It also
   holds for every *reducible* simply-laced group of rank <= 6 except `A1 x D4`,
   where `v = (e, w0(D4))` is the unique violation (§2.2).
3. **Theorem B (type A, every rank, modulo one clean conjecture).** For all `m` and
   every rationally smooth `v` in `S_m`, the exponent multiset of `P_v` is a
   **staircase multiset** (gap-free from 2) **dominated** by the degree multiset
   `{2,3,...,m}` — both statements *fully proved* here via chordality of the
   inversion graph (§4). Hence F1-smooth for all of type A, with strictness for
   `v != w0`, follows from Conjecture SD below; and it holds **unconditionally for
   `m <= 17`** (i.e. `A_1..A_16`) because the SD′ instances needed there are a
   finite set, checked exhaustively in exact arithmetic (Corollary B′, NC-9).
4. **Conjecture SD (staircase domination — the single remaining analytic core).**
   If `C, D` are staircase multisets with `|C| <= |D|` and sorted-decreasing
   pointwise `c_(i) <= d_(i)`, then `r(prod [c]_q) >= r(prod [d]_q)`, with equality
   iff `C = D`. Verified exhaustively: 91,355 dominated pairs over the 511 staircase
   multisets with max part <= 12 and length <= 9 — zero violations, zero non-trivial
   equalities (§5); plus all 131,036 pairs of the weaker instance SD′
   (`D = {2..m}`, `m <= 17`) that Theorem B actually needs (Remark 5.0/NC-9).
   SD contains the
   statement "`r` of the Mahonian sequence is strictly decreasing in `m`", i.e. at
   least the difficulty of [F2] Theorem A — an honest **GAP**, not an oversight.
5. Type `D_n (n >= 7)`, `E7`, `E8`: open (GAP-2/GAP-3, §6), with all rank <= 6
   evidence positive and the exceptional degree-product ratios computed exactly.

---

## 1. Setup, known inputs, and one uniqueness lemma

Notation as in `F2_SPEC.md`. For `v in W`, `P_v(q) = sum_{u <= v} q^{ell(u)}`
(rank generating function of `[e,v]`); `P_{w0} = prod_i [d_i]_q` with `d_1,...,d_n`
the fundamental degrees; `[c]_q = 1 + q + ... + q^{c-1}`.

**Fact 1.1 (Carrell–Peterson criterion).** `v` is rationally smooth iff `P_v` is
palindromic. *(Carrell, Proc. Sympos. Pure Math. 56 (1994); the criterion of
Carrell–Peterson.)* In simply-laced types rationally smooth = smooth
(Peterson's theorem; Carrell–Kuttler, J. Algebraic Geom. 12 (2003)).

**Fact 1.2 (factorization into q-integers).** If `v` is rationally smooth then
`P_v(q) = prod_{i=1}^{s} [e_i + 1]_q` for positive integers `e_i` ("the exponents
of `v`"). *Type A: Gasharov, "Factoring the Poincaré polynomial of the Bruhat
interval", J. Combin. Theory Ser. A 83 (1998). General type: Akyildiz–Carrell
(IMRN 2012-ish) and, via free inversion arrangements, Slofstra (rationally smooth
Schubert varieties and inversion hyperplane arrangements). Citation details flagged
for the prior-art pass (GAP-4); the fact itself is machine-verified below on every
rationally smooth interval in all ten groups of §3 — 7,152 intervals, zero
failures.*

**Lemma 1.3 (the exponent multiset is well defined, and greedy factoring is
correct).** A product of q-integers determines its factor multiset uniquely;
moreover if `P` is such a product and `M` is the largest `c` with `[c]_q | P`,
then `M = max` of the multiset, so greedy division by the largest dividing
q-integer recovers the multiset (and certifies "not a product" otherwise).

*Proof.* `[c]_q = prod_{d | c, d > 1} Phi_d(q)` (cyclotomics). If `[c]_q | P =
prod [c_i]_q` then `Phi_c | P`, forcing `c | c_i` for some `i`, so `c <= max c_i`;
and `[max c_i]_q` does divide `P`. Induct after stripping one factor of size
`max c_i`. Uniqueness: the multiplicity of `Phi_c` in `P` is `#{i : c | c_i}`;
downward induction on `c` recovers all multiplicities. ∎

**Definition 1.4.** `E(v) :=` the multiset `{e_i + 1}` of Fact 1.2 (well defined by
Lemma 1.3), called the *factor multiset*; `D(W) := {d_1,...,d_n}` the degree
multiset. `sum (c - 1) over E(v) = ell(v)`; `E(w0) = D(W)`.

**Definition 1.5.** A multiset `C` of integers `>= 2` is a **staircase multiset**
if `min C = 2` and its value support has no gaps: every integer in
`[2, max C]` occurs in `C`. (Examples: `{2,3,4,4,6}` is not; `{2,2,3,3,4}` is.)

**Definition 1.6 (domination).** For multisets `C, D` sorted decreasingly:
`C ⪯ D` iff `|C| <= |D|` and `c_(i) <= d_(i)` for `1 <= i <= |C|`.
Equivalently `#{c in C : c >= t} <= #{d in D : d >= t}` for every `t`.

NUMERIC CHECK (NC-1, ground truth anchor): `python3 mahonian.py --mmax 60` —
reproduces [F2] NC-1's table (argmin central, `varfit` 0.84→0.97...); and the
Mahonian min-ratio `r_m` is **strictly decreasing** for `4 <= m <= 60`
(Appendix D, first block prints `True`). This is the `C = {2..m}, D = {2..m+1}`
instance of Conjecture SD.

---

## 2. The two counterexamples (hypotheses are sharp)

### 2.1 Non-simply-laced: FALSE in B3 and B4.

In `B_n (n>=3)` the parabolic `<s_{n-1}, s_n>` is dihedral of order 8; `v = w0` of
that parabolic has `P_v = [2]_q [4]_q`, rank sequence `(1,2,2,2,1)`, palindromic
(rationally smooth), with `r = 2^2/(2*2) = 1` exactly on the plateau. Meanwhile
`r(w0(B3)) = 8/7`, `r(w0(B4)) = 968/897 > 1`. So F1-smooth fails in `B3, B4`.
The mechanism — a dihedral `I_2(m), m >= 4` parabolic creating a factor pair
`{2, m}` with gap `>= 2`, hence a flat plateau — is exactly what the simply-laced
hypothesis excludes: in simply-laced `W` a rank-2 parabolic is `A1 x A1` or `A2`,
so no element of length 4 has 2-element support (see Lemma 4.5).

NUMERIC CHECK (NC-2): Appendix A, `python3 appA_verify.py B3 B4` →
`B3: ... violations=1 ... runner-up=1.000000`, `B4: ... violations=1 ...`.

### 2.2 Reducible simply-laced: FALSE in `A1 x D4` (new).

`P_{D4} = [2][4][4][6] = (1,4,9,16,23,28,30,28,23,16,9,4,1)`, and
`r(P_{D4}) = 28^2/(23*30) = 392/345 = 1.1362318...` at `k = 5`.
`P_{w0(A1 x D4)} = [2] P_{D4} = (1,5,13,25,39,51,58,58,51,39,25,13,5,1)`, and
`r = 58^2/(51*58) = 58/51 = 1.1372549...` at the central pair.
The element `v = (e, w0(D4))` is smooth (its Schubert variety is a point times the
full flag variety of `D4`), `[e,v] ≅ D4`, and

```
r([e,v]) = 392/345  <  58/51 = r([e,w0]),      gap = 6/5865 = 2/1955 = 0.0010230...
```

So **convolving with `[2]_q` can strictly increase the min-ratio of a Weyl Poincaré
polynomial**, and F1 (smooth or not) fails for reducible simply-laced groups.
This is sporadic: the same construction does *not* violate in `A1 x D5`
(`r([2]P_{D5}) = 1.06923 < r(P_{D5}) = 1.06946`), `A1 x E6`, or `A1 x A1 x D4`,
and an exhaustive scan of ALL 28 reducible simply-laced types of rank <= 6
(all tuples of lower intervals, palindromic products filtered — note a palindromic
product need not have palindromic factors, so we filter on the product) found
`A1 x D4` to be the **only** violating group, with `(e, w0(D4))` its only violating
element.

NUMERIC CHECK (NC-3): Appendix B → 28 lines, `violations=0` on 27 of them,
`A1xD4 ... violations=1`, worst = `(1)x(1,4,9,16,23,28,30,...)`; and the exact
fractions above from the 6-line snippet at the end of Appendix B.

**Warning for future provers (structural corollary).** Any proof strategy that
reduces `v` to its parabolic support `W_J` via the chain
"`r([e,v]) >= r(P_{W_J}) >= r(P_W)`" is **unsound**. Concretely, `A1 x D4` is a
parabolic of `D6` (delete the second node of the tail), and for the smooth element
`v` = (longest element of the `D4` sub-factor) the first link fails:
`r([e,v]) = 392/345 < 58/51 = r(P_{W_J})` — even though the composite conclusion
`r([e,v]) >= r(P_{D6}) = 1.0407...` is true (Theorem A). Comparisons must go
directly from `E(v)` to `D(W)`, never through a reducible intermediate group.

---

## 3. Theorem A — exhaustive verification, irreducible rank <= 6

**Theorem A.** Let `W` be an irreducible simply-laced Weyl group of rank <= 6
(`A1..A6, D4, D5, D6, E6`). For every rationally smooth `v in W`:
`r([e,v]) >= r([e,w0])`, with equality iff `v = w0`. Moreover `E(v) ⪯ D(W)`
(Definition 1.6) in every case, and `P_v` factored into q-integers in every case.

*Proof.* Exact enumeration in integer/Fraction arithmetic — a legitimate finite
proof step (same ethos as [F2] Theorem C's `m <= 150` reduction). For each group,
every lower interval's rank sequence is computed from the `weyl.py` bitset engine
(itself internally cross-checked four ways: order formula, inversion count = BFS
length, level sizes = Poincaré coefficients, positive-root count), palindromicity
filtered, `r` minimized exactly, `E(v)` extracted by Lemma 1.3's greedy algorithm.
Results:

| W | `r(w0)` exact | = float | # rat. smooth | runner-up smooth `r` | violations |
|---|---|---|---|---|---|
| A2 | `2` | 2.000000 | 6 | 4.000000 | 0 |
| A3 | `25/18` | 1.388889 | 22 | 1.666667 | 0 |
| A4 | `121/100` | 1.210000 | 88 | 1.266667 | 0 |
| A5 | `101/90` | 1.122222 | 366 | 1.144402 | 0 |
| A6 | `191/177` | 1.079096 | 1552 | 1.089570 | 0 |
| D4 | `392/345` | 1.136232 | 108 | 1.266667 | 0 |
| D5 | `44944/42025` | 1.069459 | 490 | 1.115136 | 0 |
| D6 | `925444/889249` | 1.040703 | 2164 | 1.060074 | 0 |
| E6 | `13410244/13039321` | 1.028446 | 2356 | 1.049667 | 0 |

(A1 is trivial: both intervals have length < 2, `r = +inf`.) In all 7,152 smooth
intervals: zero factorization failures, zero domination failures, zero ratio
violations, zero equalities besides `v = w0`. The runner-up column shows the
margin is never thin (worst relative margin ~1.0% at A6/D6). ∎

NUMERIC CHECK (NC-4): Appendix A. `python3 appA_verify.py A2 A3 A4 A5 D4 D5`
runs in ~1 min and prints exactly the corresponding rows;
`python3 appA_verify.py A6 D6 E6` takes ~2/13/40 min (E6 builds 51840 elements).
Expected output lines are reproduced verbatim in Appendix A.

**Remark 3.1.** The E6 exponent-multiset landscape (83 distinct multisets) contains
non-staircase multisets like `{2,4,4,6}`-extensions and `{2,5,5,6,8,8}`; type A
produces staircase multisets only (§4). The runner-up in E6 is
`E(v) = {2,5,5,6,8,8}` with `r = 1.049667`.

---

## 4. Type A for every rank: staircase + domination (proved), Theorem B

Throughout `W = S_m` (type `A_{m-1}`), degrees `D = {2,3,...,m}`. The **inversion
graph** `G_v` has vertices `1..m` and edges `{i,j}` (`i<j`) with `v(i) > v(j)`.

**Fact 4.1 (arrangement package).** For smooth `v` (avoid 3412, 4231;
Lakshmibai–Sandhya):
(i) `P_v(q) = R_v(q)`, the distance enumerator of the regions of the inversion
arrangement `A_v` (Oh–Postnikov–Yoo, JCTA 2008 / arXiv:0709.3259);
(ii) `A_v` is the graphical arrangement of `G_v`, and it is free/supersolvable iff
`G_v` is **chordal** (Stanley, supersolvable lattices; Edelman–Reiner), which holds
for smooth `v` (OPY);
(iii) for a chordal graph with perfect elimination order (PEO) `v_1,...,v_m` and
*back-degrees* `b_i = #{j < i : v_j ~ v_i}`, the exponents are `{b_i}` and
`R(q) = prod_i [b_i + 1]_q` (Björner–Edelman–Ziegler factorization for
supersolvable arrangements; `chi_G(t) = prod (t - b_i)`).
Combining with Lemma 1.3: **`E(v) = {b_i + 1 : b_i > 0}` as multisets.**
*Citations flagged for the prior-art pass (GAP-4); the composite statement is
machine-verified for every smooth `v` in `S_3..S_7` — 2,034 permutations, zero
mismatches (NC-5).*

NUMERIC CHECK (NC-5): Appendix C, `python3 appC_chordal.py` →
`S3..S7: smooth=6/22/88/366/1552, nonchordal=0, factor/backdeg mismatches=0,
staircase failures=0, domination failures=0`, and
`random connected chordal graphs: 0 gap-free failures / 20000`.

**Lemma 4.2 (gap-free back-degrees; fully proved).** Let `G` be a chordal graph.
The multiset of positive back-degrees (independent of the PEO, since
`chi_G(t) = prod (t - b_i)`) is gap-free: if some `b_i >= k >= 2` then some
`b_j = k - 1`. Hence it contains every value `1, ..., max b`.

*Proof.* It suffices to treat `G` connected (each component contributes its own
gap-free multiset starting at 1 — the second vertex of a component's PEO has
back-degree exactly 1 by connectivity — and a union of multisets each equal to a
full initial segment `{1..M_c}` with multiplicity is gap-free). Induct on `|G|`.
Pick a simplicial vertex `x` (exists, chordal), `d := deg x`; its neighborhood is a
`d`-clique. `G - x` is connected (neighbors of a simplicial vertex are pairwise
adjacent, so removing `x` breaks no path) and chordal, and placing `x` last in a
PEO of `G - x` gives `multiset(G) = multiset(G-x) ∪ {d}`. The `d`-clique
`N(x) ⊆ G - x`: in any PEO of `G - x`, its last-ordered vertex has at least `d - 1`
back-neighbors, so `max b(G-x) >= d - 1`. By induction `multiset(G-x)` is gap-free
with max `M' >= d-1`; adding `d <= M' + 1` preserves gap-freeness. Base `|G| = 1`
trivial. ∎

**Lemma 4.3 (domination; fully proved).** For any graph `G` on `m` vertices and
any vertex order, the multiset `{b_i + 1 : b_i > 0}` is dominated (Def. 1.6) by
`{2, 3, ..., m}`.

*Proof.* `b_i <= i - 1` (position `i` has `i-1` predecessors), and there are at
most `m - 1` positive entries (the first vertex has `b_1 = 0`). For any `t >= 2`:
`#{i : b_i + 1 >= t} <= #{i : i - 1 >= t - 1} = m - t + 1 = #{d in {2..m} : d >= t}`.
This is exactly Definition 1.6's counting form. ∎

**Theorem 4.4 (type-A structure; fully proved modulo Fact 4.1's citations).**
For every rationally smooth `v in S_m` (any `m`), the factor multiset `E(v)` is a
staircase multiset (Lemma 4.2: gap-free, and it contains a 2 whenever it is
nonempty since some `b_i = 1`) with `E(v) ⪯ {2,...,m}` (Lemma 4.3), and
`E(v) = {2,...,m}` iff `v = w0` (degree count: `sum (c-1) = ell(v) = binom(m,2)`
forces `v = w0`). ∎

**Lemma 4.5 (why simply-laced kills the plateau; fully proved, all types).**
In any simply-laced `W`, no rationally smooth interval has `E(v)` containing a
2-element sub-multiset `{2, c}` with `c >= 4` *as its entire multiset*: `|E(v)|`
equals the coefficient of `q` in `P_v`, i.e. `|supp(v)|`, so `|E(v)| = 2` forces
`v` into a rank-2 parabolic, which in simply-laced types is `A1 x A1` or `A2`
(max length 2 or 3), while `E(v) = {2,c}` requires `ell(v) = c >= 4`. (Contrast
`B_n`: `I_2(4)` parabolics realize `{2,4}` = the §2.1 counterexample.) ∎

**Theorem B (type A, conditional).** Assume Conjecture SD (§5). Then for every `m`
and every rationally smooth `v in S_m`: `r([e,v]) >= r([e,w0])`, strictly unless
`v = w0`.

*Proof.* If `ell(v) < 2`, `r = +inf`. Otherwise `P_v = prod_{c in E(v)} [c]_q`
(Fact 1.2), `E(v)` staircase and `E(v) ⪯ {2..m}` (Theorem 4.4), `{2..m}` is
staircase, and `P_{w0} = prod_{c in {2..m}} [c]_q`. Apply SD; strictness from
SD's equality clause plus `E(v) = {2..m} ⟺ v = w0`. ∎

**Corollary B′ (type A, `m <= 17`, unconditional modulo Fact 4.1's citations).**
For every `m <= 17` and every rationally smooth `v in S_m`:
`r([e,v]) >= r([e,w0])`, strictly unless `v = w0` — no conjecture needed.

*Proof.* By Theorem 4.4, `E(v)` ranges inside the set of staircase multisets
`⪯ {2..m}`; NC-9 checks the SD′ inequality for **all** `2^{m-1} - 2` proper such
multisets by exact computation for `m <= 17` (whether realizable or not), so the
appeal to Conjecture SD in Theorem B is replaced by a finite verified check. (For
`m <= 7` this is independently confirmed by the direct interval enumeration of
Theorem A, which bypasses Fact 4.1 entirely.) ∎ Type A is thus open only for
`m >= 18`, and the check extends mechanically (cost `~2^m` polynomial
convolutions of degree `< binom(m,2)`; `m <= 17` took ~4 min single-core).

---

## 5. Conjecture SD, the false-lemma museum, and what is proved around it

### 5.1 What is FALSE (do not attempt these as lemmas)

Exhaustive scan over all 1,286 multisets with parts in `[2,9]`, length <= 5
(Appendix E; increments/additions are counted per *move*, i.e. per
(multiset, position) pair):

- **Single-increment monotonicity** ("replace `c` by `c+1` ⟹ `r` decreases"):
  **887 violations**. Smallest: `{2,4}: r=1 → {3,4}: r=4/3`. Restricting to
  multisets containing a 2 does not help (574 violations, e.g.
  `{2,2,4}: 4/3 → {2,3,4}: 25/18`).
- **Unrestricted domination** (`C ⪯ D`, same length ⟹ `r(C) >= r(D)`):
  **18,443 violations** (`C = {2,4}, D = {3,4}` again).
- **Adding a factor `c >= max`** decreases `r`: **247 violations**
  (`{3} + [3] : 1 → 4/3`; note `§2.2` is the depth-2 version of this phenomenon:
  `{2,4,4,6} + [2]` increases `r`).
- **Convolution decreases min-ratio**: false — `[3] * [2]`: `1 → 2`. ([F2] §6.1's
  discarded one-step lemma is the same beast from the other side.)

The common mechanism of every violation found: a **gap** (plateau or near-plateau
from factor pairs `{c, c'}, c' >= c+2`) that the increment/domination move *fills
in*. Staircase multisets have no gaps to fill:

- **Increment within the staircase class** (both sides staircase): **0 violations**
  in the `[2,9] x len<=5` box.
- **Domination within the staircase class**: **0 violations**.

### 5.2 The conjecture

**Conjecture SD.** Let `C, D` be staircase multisets (Def. 1.5) with `C ⪯ D`
(Def. 1.6, cross-length allowed). Then `r(prod_{c in C} [c]_q) >=
r(prod_{d in D} [d]_q)`, with equality iff `C = D`.

NUMERIC CHECK (NC-6): Appendix D, second block. Over all **511** staircase
multisets with max part <= 12 and length <= 9: **91,355** dominated pairs,
**0 violations, 0 equalities** with `C != D`. (Smaller box max<=10/len<=7:
127 multisets, 6,180 pairs, same — rerun by changing `staircases(12,9)` to
`staircases(10,7)`.) Exact `Fraction` arithmetic throughout.

**Remark 5.0 (SD′ — the weaker statement Theorem B actually needs).** Theorem B
only ever invokes SD with `D = {2,3,...,m}` (each degree once). Call this
instance **SD′**: *if `C` is staircase and `C ⪯ {2..m}` then
`r(prod_C [c]_q) > r_m` unless `C = {2..m}`.* SD′ still contains
Mahonian-monotonicity (`C = {2..m} ⪯ {2..m+1}`), so the difficulty class is
unchanged, but any prover should target SD′ first. Two structural bonuses:
the staircase multisets `⪯ {2..m}` number exactly `2^{m-1} - 1` (verified
computationally for `m <= 17`, NC-9), and every staircase multiset `C` with
max `M` decomposes as `C = {2,3,...,M} ∪ C'` with `C'` an arbitrary
sub-multiset of values in `[2, M]` — i.e. `P_C` = (the Mahonian polynomial
of `S_M`) × (a product of q-integers each `<= M`). One full Mahonian block
is always present: the [F2] Fourier/tilting machinery's natural habitat
(in particular [F2] Lemma 1.4's far-field bound applies verbatim to the
Mahonian block and hence, by `|phi_prod| <= |phi_block|`, to `P_C`).

NUMERIC CHECK (NC-9): for every `4 <= m <= 17`, ALL staircase `C ⪯ {2..m}`
(counts `6, 14, 30, ..., 65534 = 2^{m-1} - 2` proper ones — the count itself
confirms the `2^{m-1} - 1` enumeration) satisfy `r(P_C) > r_m` strictly:
**131,036 pairs, 0 violations, 0 equalities** (Appendix D's `rof` + the
domination filter over multiplicity vectors; run 2026-07-06, exact
`Fraction`s; `m = 17` involves polynomials of degree up to 136).

**Honest difficulty assessment (GAP-1).** SD restricted to
`C = {2..m}, D = {2..m+1}` says the Mahonian min-ratio is strictly decreasing —
verified exactly for `m <= 60` here (NC-1) and consistent with [F2] NC-1 to
`m = 150`, but *proving* it inherits everything [F2] fought: by [F2] Cor. 2.3 the
central ratio is `1 + sigma^{-2}(1 - (27/25)m^{-1} + O(m^{-2}))`, so consecutive-`m`
comparisons are decided at relative order `m^{-4}` — the same precision class as
[F2]'s G1/G2. SD is *harder* than F2(a) and should be attacked with the same
machinery, not ad hoc. Two concrete routes:
- **R1 (Fourier/tilting, systematic).** Every structural lemma of [F2] §1–§3 is
  per-factor and holds verbatim for arbitrary products of uniforms
  (`[F2] L1.1` factorization of the cf, `L1.3`'s positive log-series with
  `S*_{2r} = sum (c_i^{2r} - 1)`, `L3.1–3.4` tilting; the staircase hypothesis
  supplies `c_i`-density needed for the far-field bound `L1.4` analogue: a
  staircase multiset with max `M` contains `{2..M}`, so the Mahonian bound applies
  to a sub-product). One would prove `r(C) = 1 + sigma_C^{-2}(1 - B_C + err)` with
  `sigma_C^2 = sum (c^2-1)/12`, `B_C = (sum (c^4-1)/240)/(2 sigma_C^4)`, uniformly
  over staircase `C` with explicit `err`, then reduce SD to a finite check via
  Lemma 5.3. Heavy: this is [F2]'s G1+G2 for a family.
- **R2 (exact/injective).** Unknown. The `q`-integer structure is so rigid that a
  Cauchy–Binet / lattice-path injection may exist for the single-increment
  staircase move; nothing in the four [F2] blind drafts rules it out. The
  second-difference kernel `[F2] L1.5` holds verbatim for any product and is the
  right identity to difference *inside*.

### 5.3 What IS proved around SD

**Lemma 5.1 (two-factor closed form; proved by direct computation).** For
`2 <= a <= b`, the coefficients of `[a]_q[b]_q` rise `1,2,...,a`, plateau at `a`
(length `b-a+1`), and fall. By symmetry the distinct interior ratios are: the
rising-edge ratios `(k+1)^2/(k(k+2))` (`1 <= k <= a-2`, strictly decreasing in
`k`), the rise/plateau corner `a/(a-1)` (present iff `b > a`), the peak
`a^2/(a-1)^2` (present iff `b = a`), and plateau-interior ratios equal to `1`
(present iff `b >= a+2`). For `a >= 3` the smallest of the non-plateau
candidates is the rising-edge value at `k = a-2`, namely
`(a-1)^2/(a(a-2)) = (a-1)^2/((a-1)^2 - 1)` (cross-multiplication against the
corner and peak values). Hence `r = 1` iff `b >= a+2` (plateau of length
`>= 3`), and for `b in {a, a+1}`:
`r([2][2]) = 4`, `r([2][3]) = 2`, and `r([a][b]) = (a-1)^2/(a(a-2))` for
`a >= 3` (the same value for `b = a` and `b = a+1`). In particular the only
2-factor staircase multisets, `{2,2}` and `{2,3}`, have `r = 4, 2`: SD's rank-2
instances hold with slack. ∎ *(An earlier version of this lemma claimed
`r([a][a+1]) = a/(a-1)` — that is only the corner ratio and is wrong for
`a >= 3`; caught by NC-8.)*

NUMERIC CHECK (NC-8): exact scan `2 <= a <= b <= 40`: `r = 1 ⟺ b >= a+2`, zero
exceptions; `r([a][a]) = r([a][a+1]) = (a-1)^2/(a(a-2))` for `3 <= a <= 40`
(and `4, 2` at `a = 2`), zero mismatches (Appendix E, last block; re-run
2026-07-06).

**Lemma 5.2 (variance monotonicity; proved, exact).** `sigma^2(C) :=
Var(sum U_c) = sum_{c in C} (c^2 - 1)/12`. If `C ⪯ D` then
`sigma^2(C) <= sigma^2(D)`, strictly unless `C = D`. *Proof:* termwise on the
sorted lists; missing factors contribute `(c^2-1)/12 >= 1/4 > 0`. ∎
(This is the task's "variance monotonicity" made exact; with the heuristic
`r ≈ 1 + (1 - B)/sigma^2` it *predicts* SD, and the `B`-correction is why the
prediction needs R1-grade error control rather than being a proof.)

**Lemma 5.3 (product/merge stability; proved).** If `C1 ⪯ D1` and `C2 ⪯ D2` then
`C1 ∪ C2 ⪯ D1 ∪ D2`. *Proof:* the counting form of Def. 1.6 adds. ∎
(So SD is closed under taking products of groups — relevant for reducible parabolic
supports inside an irreducible `W`; NB by §2.2 the *conclusion* for reducible
top-groups can still only be reached through SD's staircase hypothesis, which
`D(A1 x D4) = {2,2,4,4,6}` fails — SD does not even see the §2.2 counterexample.
Consistency, not luck.)

---

## 6. Type D and exceptional types (partial results + data)

- **Enumerated (Theorem A):** D4, D5, D6, E6 — F1-smooth TRUE, minimum uniquely at
  `w0`, `E(v) ⪯ D(W)` always (0 domination failures), factorization always exists.
- **Observed structure in type D/E:** `E(v)` is *not* staircase in general (it
  cannot be — `D(W)` itself has gaps, e.g. `D(D4) = {2,4,4,6}`). Observed
  multisets look like "degree multisets of parabolic-type subsystems + staircase
  padding" (e.g. D6 runner-up `{2,4,5,6,6,8}`, E6 runner-up `{2,5,5,6,8,8}`), but I
  have **no characterization theorem** (GAP-2). The natural conjecture, via
  Slofstra's inversion-arrangement theorem, is that `E(v)` = exponent multiset of a
  free sub-arrangement of the `D_n`/`E_n` reflection arrangement, and that the
  right SD-analogue restricts to the class of such multisets; the signed-graph
  chordality theory needed to mimic §4 exists only partially in the literature.
- **Exceptional degree products (exact):**
  `r(E6) = 13410244/13039321 = 1.028446` (k=18),
  `r(E7) = 65523/64757 = 1.011829` (k=31),
  `r(E8) = 82907598940321/82578730496656 = 1.003982` (k=60).
  `r(D_n)` strictly decreasing on `4 <= n <= 15` (NC-7). E7/E8 smooth-interval
  enumeration is finite but out of scope here (GAP-3): `weyl.py`'s global bitsets
  do not scale to `|W| = 2.9M`; the per-interval engine `scaled_general.py` does,
  but a smooth-candidate *generator* (e.g. via Billey–Postnikov/Richmond–Slofstra
  staircase-diagram decompositions) is needed instead of a full sweep.

NUMERIC CHECK (NC-7): Appendix D, third block → the three exceptional fractions
above and `D4..D15` ratios `1.136232, 1.069459, 1.040703, 1.025574, 1.017122,
1.012034, 1.008783, 1.006607, 1.005095, 1.004012, 1.003216, 1.002617` (strictly
decreasing).

---

## 7. GAP ledger

| # | Gap | Severity | Blocks | Notes / best route |
|---|-----|----------|--------|--------------------|
| **GAP-1** | Conjecture SD (staircase domination); the sufficient instance is SD′ (`D = {2..m}`, Remark 5.0). | **major** — the analytic core; contains Mahonian-monotonicity, i.e. >= [F2] Thm A difficulty | Theorem B beyond the NC-6/NC-9 boxes; type A for `m >= 18` | Route R1 (§5.2): generalize [F2] §1–§3 to staircase products (all structural lemmas already hold per-factor; one full Mahonian block is always present, Remark 5.0); or R2 exact injection. |
| **GAP-2** | Type `D_n, n >= 7`: characterization of `E(v)` (signed-graph analogue of §4) and the matching SD-analogue. | major | type D beyond rank 6 | Slofstra's free-inversion-arrangement theorem + a signed-graphic chordality/PEO theory; Lemmas 4.2/4.3 are graph-theoretic and their proofs were *designed* to transplant (simplicial-vertex induction, position bound). |
| **GAP-3** | E7, E8 finite checks. | minor-in-principle (finite), blocked on tooling | exceptional types | smooth-candidate generator + `scaled_general.py`; the degree-product ratios (NC-7) and rank<=6 pattern leave little doubt. |
| **GAP-4** | Citation verification for Facts 1.2/4.1 (Gasharov; OPY; Stanley/Edelman–Reiner; BEZ; Akyildiz–Carrell; Slofstra — all quoted from memory). | minor (each classical; composite claim machine-verified `m <= 7`, all groups rank <= 6) | publication hygiene only | prior-art pass; [house rule: kill-search before shipping]. |

**Corrected theorem to propagate upstream (replaces the frozen F1-smooth):**
*Let `W` be a finite **irreducible** simply-laced Weyl group and `v in W`
rationally smooth. Then `r([e,v]) >= r([e,w0])`, with equality iff `v = w0`.*
Status: proved for rank <= 6 (Theorem A); type A proved through rank 16
(`m <= 17`, Corollary B′ — finite exact check replacing the conjecture, modulo
only the Fact 4.1 citation package), all ranks modulo SD/SD′ (Theorem B);
`D_{>=7}, E7, E8` open. Both the irreducibility and simply-laced hypotheses are
necessary (§2), and the reducible failure `A1 x D4` is unique among reducible
simply-laced types of rank <= 6.

---

## Appendix A — irreducible-group verifier (tested; run from `phase2/bruhat/`)

Save as `appA_verify.py` and run e.g. `python3 appA_verify.py A2 A3 A4 A5 D4 D5`.

```python
import sys
sys.path.insert(0, ".")
from fractions import Fraction
from weyl import WeylGroup, DEGREES

def qdiv(P, c):                      # exact division by [c]_q; None if not divisible
    P = P[:]
    if len(P) < c: return None
    Q = [0]*(len(P)-c+1)
    for i in range(len(Q)-1, -1, -1):
        q = P[i+c-1]; Q[i] = q
        for j in range(c): P[i+j] -= q
    return Q if not any(P) else None

def qfactor(P):                      # greedy-largest; sound+complete by Lemma 1.3
    fac = []
    while len(P) > 1:
        for c in range(len(P), 1, -1):
            Q = qdiv(P, c)
            if Q is not None:
                fac.append(c); P = Q; break
        else:
            return None
    return sorted(fac, reverse=True)

def minr(a):
    return min(Fraction(a[k]*a[k], a[k-1]*a[k+1]) for k in range(1, len(a)-1))

def verify(typ, n):
    W = WeylGroup(typ, n)
    degs = sorted(DEGREES[typ](n), reverse=True)
    w0 = max(range(W.N), key=lambda i: W.length[i])
    rW = minr(W.rank_sequence(0, w0))
    nsm = viol = eq = dom = fact = 0
    second = None
    for i in range(W.N):
        a = W.rank_sequence(0, i)
        if a != a[::-1]: continue
        nsm += 1
        E = qfactor(a[:])
        if E is None: fact += 1; continue
        if len(E) > len(degs) or any(c > d for c, d in zip(E, degs)): dom += 1
        if len(a) < 3: continue
        r = minr(a)
        if r < rW: viol += 1
        elif r == rW and i != w0: eq += 1
        if i != w0 and (second is None or r < second): second = r
    print(f"{typ}{n}: r(w0)={rW}  smooth={nsm}  violations={viol}  "
          f"equalities={eq}  dom-failures={dom}  factor-failures={fact}  "
          f"runner-up={float(second):.6f}")

for g in sys.argv[1:]:
    verify(g[0].upper(), int(g[1:]))
```

Expected output (verbatim, re-run by the author 2026-07-06):

```
A2: r(w0)=2  smooth=6  violations=0  equalities=0  dom-failures=0  factor-failures=0  runner-up=4.000000
A3: r(w0)=25/18  smooth=22  violations=0  equalities=0  dom-failures=0  factor-failures=0  runner-up=1.666667
A4: r(w0)=121/100  smooth=88  violations=0  equalities=0  dom-failures=0  factor-failures=0  runner-up=1.266667
A5: r(w0)=101/90  smooth=366  violations=0  equalities=0  dom-failures=0  factor-failures=0  runner-up=1.144402
D4: r(w0)=392/345  smooth=108  violations=0  equalities=0  dom-failures=0  factor-failures=0  runner-up=1.266667
D5: r(w0)=44944/42025  smooth=490  violations=0  equalities=0  dom-failures=0  factor-failures=0  runner-up=1.115136
A6: r(w0)=191/177  smooth=1552  violations=0  equalities=0  dom-failures=0  factor-failures=0  runner-up=1.089570
D6: r(w0)=925444/889249  smooth=2164  violations=0  equalities=0  dom-failures=0  factor-failures=0  runner-up=1.060074
E6: r(w0)=13410244/13039321  smooth=2356  violations=0  equalities=0  dom-failures=0  factor-failures=0  runner-up=1.049667
B3: r(w0)=8/7  smooth=34  violations=1  equalities=0  dom-failures=0  factor-failures=0  runner-up=1.000000
B4: r(w0)=968/897  smooth=142  violations=1  equalities=0  dom-failures=0  factor-failures=0  runner-up=1.000000
```

## Appendix B — reducible-group check (tested)

Save as `appB_products.py`; runs all 28 reducible simply-laced types of rank <= 6.

```python
import sys
sys.path.insert(0, ".")
from fractions import Fraction
from itertools import product as iproduct, combinations_with_replacement as cwr
from weyl import WeylGroup

RANK = {"A1":1,"A2":2,"A3":3,"A4":4,"A5":5,"D4":4,"D5":5}
def polymul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out
def minr(a):
    if len(a)<3: return None
    return min(Fraction(a[k]*a[k],a[k-1]*a[k+1]) for k in range(1,len(a)-1))
def polys_of(name):
    W=WeylGroup(name[0],int(name[1:])); out={}
    for i in range(W.N):
        a=tuple(W.rank_sequence(0,i)); out[a]=out.get(a,0)+1
    return out
cache={n:polys_of(n) for n in RANK}
combos=set()
for k in range(2,7):
    for c in cwr(sorted(RANK),k):
        if sum(RANK[x] for x in c)<=6: combos.add(c)
total=0
for c in sorted(combos,key=lambda t:(len(t),t)):
    w0=[1]
    for n in c: w0=polymul(w0,list(max(cache[n],key=len)))
    rW=minr(w0); viol=0
    for tup in iproduct(*[list(cache[n]) for n in c]):
        P=[1]
        for a in tup: P=polymul(P,list(a))
        if P!=P[::-1]: continue          # rationally smooth iff product palindromic
        r=minr(P)
        if r is not None and r<rW: viol+=1
    print("x".join(c), f"r(w0)={float(rW):.6f} violations={viol}")
    total+=viol
print("TOTAL violations:", total)      # expected: 1, all in A1xD4
```

Expected: 27 lines with `violations=0`; `A1xD4 r(w0)=1.137255 violations=1`;
`TOTAL violations: 1`. Exact fractions of the counterexample (hand-checkable):
`P_{D4} = (1,4,9,16,23,28,30,28,23,16,9,4,1)`, `r = 28^2/(23*30) = 392/345`;
`[2]P_{D4} = (1,5,13,25,39,51,58,58,51,39,25,13,5,1)`, `r = 58/51`;
`392/345 < 58/51` since `392*51 = 19992 < 20010 = 345*58`.

## Appendix C — type-A chordal mechanism check (tested)

Save as `appC_chordal.py`. Verifies for every rationally smooth `v` in `S_3..S_7`:
inversion graph chordal (Tarjan–Yannakakis MCS test: with MCS **visit order**
`v_1..v_n`, chordal iff each `v_i`'s earlier neighbours form a clique);
`E(v) = {backdeg+1 : backdeg>0}`; staircase; domination. Then 20,000 random
connected chordal graphs (n <= 12, built by gluing onto random sub-cliques) for
Lemma 4.2. Uses `scaled.py`'s independent permutation engine (not `weyl.py` —
cross-engine check for free).

```python
import sys, random
from itertools import permutations
sys.path.insert(0, ".")
from scaled import rank_seq_lower, poincare_A

def qdiv(P, c):                      # as in Appendix A
    P = P[:]
    if len(P) < c: return None
    Q = [0]*(len(P)-c+1)
    for i in range(len(Q)-1, -1, -1):
        q = P[i+c-1]; Q[i] = q
        for j in range(c): P[i+j] -= q
    return Q if not any(P) else None

def qfactor(P):
    fac = []
    while len(P) > 1:
        for c in range(len(P), 1, -1):
            Q = qdiv(P, c)
            if Q is not None:
                fac.append(c); P = Q; break
        else:
            return None
    return sorted(fac, reverse=True)

def mcs_backdegs(adj, n):
    w=[0]*n; placed=[False]*n; order=[]
    for _ in range(n):
        u=max((i for i in range(n) if not placed[i]), key=lambda i: w[i])
        placed[u]=True; order.append(u)
        for x in adj[u]:
            if not placed[x]: w[x]+=1
    pos={v:i for i,v in enumerate(order)}; bd=[]
    for i,v in enumerate(order):
        back=[x for x in adj[v] if pos[x]<i]; bd.append(len(back))
        if back:
            last=max(back,key=lambda x:pos[x])
            if any(x!=last and x not in adj[last] for x in back):
                return None
    return bd

def staircase(ms):
    s=sorted(ms)
    return (not ms) or (s[0]==2 and all(b-a<=1 for a,b in zip(s,s[1:])))

for m in range(3,8):
    pA=poincare_A(m-1); bad=[0]*4; nsm=0
    for v in permutations(range(m)):
        a=rank_seq_lower(v,pA)
        if a!=a[::-1]: continue
        nsm+=1; fac=qfactor(a[:])
        adj={i:set() for i in range(m)}
        for i in range(m):
            for j in range(i+1,m):
                if v[i]>v[j]: adj[i].add(j); adj[j].add(i)
        bd=mcs_backdegs(adj,m)
        if bd is None: bad[0]+=1; continue
        if sorted((d+1 for d in bd if d>0),reverse=True)!=fac: bad[1]+=1
        if not staircase(fac): bad[2]+=1
        degs=list(range(m,1,-1))
        if len(fac)>len(degs) or any(c>d for c,d in zip(fac,degs)): bad[3]+=1
    print(f"S{m}: smooth={nsm} nonchordal={bad[0]} mismatch={bad[1]} "
          f"nonstaircase={bad[2]} domfail={bad[3]}")

random.seed(1); fails=0
for _ in range(20000):
    n=random.randint(2,12); adj={0:set()}; cliques=[[0]]
    for v in range(1,n):
        K=random.choice(cliques); sub=random.sample(K,random.randint(1,len(K)))
        adj[v]=set(sub)
        for w2 in sub: adj[w2].add(v)
        cliques.append(sub+[v])
    bd=mcs_backdegs(adj,n); pos=sorted(d for d in bd if d>0)
    if pos and not (pos[0]==1 and all(b-a<=1 for a,b in zip(pos,pos[1:]))): fails+=1
print("random connected chordal gap-free failures:", fails, "/ 20000")
```

Expected: `S3: smooth=6 ... S7: smooth=1552`, all failure counters 0; final line
`0 / 20000`.

## Appendix D — SD box test, Mahonian/D-chain monotonicity (tested)

```python
from fractions import Fraction
from functools import lru_cache
def conv(a,c):
    out=[0]*(len(a)+c-1); run=0
    for k in range(len(out)):
        if k<len(a): run+=a[k]
        if k-c>=0: run-=a[k-c]
        out[k]=run
    return out
@lru_cache(maxsize=None)
def rof(C):
    a=[1]
    for c in C: a=conv(a,c)
    if len(a)<3: return Fraction(10**9)
    return min(Fraction(a[k]*a[k],a[k-1]*a[k+1]) for k in range(1,len(a)-1))

# block 1: Mahonian min-ratio strictly decreasing, 4 <= m <= 60  (NC-1)
prev=None; ok=True
for m in range(4,61):
    r=rof(tuple(range(2,m+1)))
    if prev is not None and not r<prev: ok=False
    prev=r
print("Mahonian r_m strictly decreasing 4..60:", ok)          # -> True

# block 2: Conjecture SD box  (NC-6)
def staircases(maxsize,maxlen):
    out=set()
    for M in range(2,maxsize+1):
        k=M-1
        if k>maxlen: break
        def go(i,rem,mults):
            if i==k:
                ms=[]
                for v,mu in zip(range(2,M+1),mults): ms+=[v]*mu
                out.add(tuple(sorted(ms,reverse=True))); return
            for mu in range(1,rem-(k-i-1)+1): go(i+1,rem-mu,mults+[mu])
        go(0,maxlen,[])
    return sorted(out)
S=staircases(12,9); viol=eq=pairs=0
for D in S:
    rD=rof(D)
    for C in S:
        if C==D or len(C)>len(D) or any(c>d for c,d in zip(C,D)): continue
        pairs+=1; rC=rof(C)
        if rC<rD: viol+=1
        elif rC==rD: eq+=1
print(len(S),"staircase multisets;",pairs,"pairs; violations:",viol,"equalities:",eq)
# -> 511 staircase multisets; 91355 pairs; violations: 0 equalities: 0

# block 3: exceptional/D-chain ratios  (NC-7)
for name,D in [("E6",(2,5,6,8,9,12)),("E7",(2,6,8,10,12,14,18)),
               ("E8",(2,8,12,14,18,20,24,30))]:
    print(name, rof(D), float(rof(D)))
prev=None
for n in range(4,16):
    r=rof(tuple(list(range(2,2*n-1,2))+[n]))
    print(f"D{n}: {float(r):.6f}", "" if prev is None or r<prev else "NOT DECREASING")
    prev=r
```

Expected: `True`; `511 ... 91355 ... violations: 0 equalities: 0`;
`E6 13410244/13039321 1.028446...`, `E7 65523/64757 1.011829...`,
`E8 82907598940321/82578730496656 1.003982...`; `D4..D15` strictly decreasing
(`1.136232` down to `1.002617`).

## Appendix E — false-lemma museum (§5.1) and Lemma 5.1 / NC-8 (tested)

Save as `appE_museum.py`; needs `conv`/`rof` from Appendix D (copy the first
15 lines). Counting convention: one violation per *move* `(C, i)`.

```python
from fractions import Fraction
from itertools import combinations_with_replacement as cwr
# ... conv(a,c) and rof(C) as in Appendix D (rof: min-ratio, inf if deg<2) ...

def staircase(C):
    s = sorted(C)
    return s[0] == 2 and all(y - x <= 1 for x, y in zip(s, s[1:]))

multis = [tuple(sorted(ms)) for L in range(1, 6) for ms in cwr(range(2, 10), L)]
print(len(multis), "multisets")                       # -> 1286
bad_M = [(C, C[:i] + (c + 1,) + C[i + 1:]) for C in multis
         for i, c in enumerate(C) if c < 9
         and rof(tuple(sorted(C[:i] + (c + 1,) + C[i + 1:]))) > rof(C)]
print("increment violations:", len(bad_M))            # -> 887
print("  with a 2 present:", len([b for b in bad_M if 2 in b[0]]))   # -> 574
print("  staircase->staircase:", len([b for b in bad_M
      if staircase(b[0]) and staircase(tuple(sorted(b[1])))]))       # -> 0
by_len = {}
for C in set(multis): by_len.setdefault(len(C), []).append(C)
v = sum(1 for L in by_len for D in by_len[L] for C in by_len[L]
        if C != D and all(c <= d for c, d in zip(C, D)) and rof(C) < rof(D))
print("same-length domination violations:", v)        # -> 18443
stairs = [C for C in set(multis) if staircase(C)]
vs = sum(1 for D in stairs for C in stairs if C != D and len(C) <= len(D)
         and all(c <= d for c, d in zip(sorted(C, reverse=True),
                                        sorted(D, reverse=True)))
         and rof(C) < rof(D))
print("staircase domination violations:", vs)         # -> 0
vA = sum(1 for C in multis if len(C) < 5 for c in range(max(C), 10)
         if rof(tuple(sorted(C + (c,)))) > rof(C))
print("add-factor (c >= max) violations:", vA)        # -> 247
# NC-8 (Lemma 5.1):
bad1 = [(a, b) for a in range(2, 41) for b in range(a, 41)
        if (rof((a, b)) == 1) != (b >= a + 2)]
bad2 = [a for a in range(3, 41)
        if [rof((a, a)), rof((a, a + 1))] != [Fraction((a-1)**2, a*(a-2))]*2]
print("NC-8 exceptions:", bad1, bad2, [rof((2, 2)), rof((2, 3))])
# -> [] [] [Fraction(4, 1), Fraction(2, 1)]
```

Final block — **NC-9 / Corollary B′** (SD′ exhaustive, `m <= 17`; ~4 min):

```python
def stair_dominated(m):                 # all staircase C ⪯ {2..m}
    out, D = [], list(range(m, 1, -1))
    def go(t, M, ms):
        if t > M:
            s = sorted(ms, reverse=True)
            if len(s) <= len(D) and all(c <= d for c, d in zip(s, D)):
                out.append(tuple(s))
            return
        for mu in range(1, len(D) - len(ms) + 1):
            go(t + 1, M, ms + [t] * mu)
    for M in range(2, m + 1):
        go(2, M, [])
    return out

for m in range(4, 18):
    D = tuple(range(m, 1, -1)); rD = rof(D)
    cs = [C for C in stair_dominated(m) if C != D]
    v = sum(1 for C in cs if rof(C) < rD)
    e = sum(1 for C in cs if rof(C) == rD)
    print(f"m={m}: proper={len(cs)} viol={v} eq={e}")
    assert len(cs) == 2 ** (m - 1) - 2 and v == 0 and e == 0
print("NC-9 PASS")
```

---

## Citations

- Carrell (with Peterson), Proc. Sympos. Pure Math. 56 (1994) — palindromic
  criterion for rational smoothness. Carrell–Kuttler, J. Algebraic Geom. 12
  (2003) — rationally smooth = smooth in simply-laced types.
- Lakshmibai–Sandhya (1990) — 3412/4231 pattern avoidance.
- Gasharov, JCTA 83 (1998) — q-integer factorization, type A.
- Oh–Postnikov–Yoo, JCTA 115 (2008), arXiv:0709.3259 — inversion hyperplane
  arrangement, `P_v = R_v` for smooth `v`.
- Stanley, Algebra Universalis 2 (1972) (supersolvable lattices); Edelman–Reiner
  (free graphic arrangements ⟺ chordal); Björner–Edelman–Ziegler, Discrete
  Comput. Geom. 5 (1990) (factorization of the distance enumerator).
- Akyildiz–Carrell (factorization for rationally smooth, general type); Slofstra
  (inversion arrangements of rationally smooth elements, general type);
  Billey–Postnikov (2005); Richmond–Slofstra (staircase diagrams) — structure for
  GAP-2/GAP-3 routes.
- [F2] = `phase2/bruhat/f2_drafts/F2_PROOF_DRAFT.md` — Lemmas 1.1/1.3/1.5,
  3.1–3.4, Cor. 2.3, NC-1: the machinery Conjecture SD should be attacked with.

*All external citations quoted from memory — GAP-4; every mathematical claim taken
from them is independently machine-verified in the stated finite ranges.*

*End of draft.*
