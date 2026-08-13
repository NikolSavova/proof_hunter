# Final adversarial audit of `full_attack2`

Date: 2026-08-13

## Executive verdict

No P0 error was found.  In particular, the typed interpolation/full-closure
implication, the five-role `7/16` obstruction, the two carry-triangle
inclusions, the independent-rounding lower bound, and the exact microtile
factorization theorem survive adversarial checking.

There is one definite P1 mathematical error in the write-up: the finite
general-`r` Turan number in `primal/AMPLIFIER_RESULT.md` (4) is not always the
displayed floor.  This does **not** change its asymptotic consequences (5)--(6)
or the conclusion that seven current-compatible colors are needed to leave
`c=0.4585` unobstructed.  There are also two P1 presentation/reproducibility
gaps: the exact triangle-overlap cardinalities need an actual counting proof,
and the preserved DRAT file needs its CNF/metadata to be a self-contained
artifact.  Exact repairs are below.

### Post-audit repair status

The root lane applied the requested repairs after this audit was delivered:

- equation (4) now uses the exact `t_r(N)` formula, and the finite checker
  computes the balanced-partition Turan number;
- the injective triangle-footprint count is included in the proof;
- `computation/K8_DRAT_AUDIT.json` binds the deterministic CNF command,
  proposition, hashes, and checker transcript to the compressed proof;
- the published-basis source comment now says Tables 1--3.

The generated `TRIANGLE_ROLE_RESULTS.json` genuinely stops at `k=8` and its
scope is therefore already correct; the expanded computation-lane
`EXTREMAL_ROLE_RESULTS.json` contains `k=9` and says so.  No known P1 remains
open after these repairs, subject to the explicitly stated CP-SAT trust scope.

## Issue list

### P1: the claimed exact general-`r` Turan formula is false

In `primal/AMPLIFIER_RESULT.md` (4), with `N=k-d`,

```text
floor((r-1)N^2/(2r))
```

is called the exact `r`-partite Turan bound.  This identity is valid for the
small `r` used earlier (including `r=4`) but not for all `r`.  For example,
`r=8,N=4` makes the display equal to seven, whereas a four-vertex graph has at
most six edges, and the exact Turan number is six.

Exact repair: write `N=ar+s`, `0<=s<r`, and replace the last term of (4) by

```text
T_r(N) = (N^2 - (r-s)a^2 - s(a+1)^2)/2.
```

Alternatively, retain the displayed floor but call it an upper bound rather
than the exact value.  Since

```text
T_r(N) = (r-1)N^2/(2r) + O(r),
```

the normalized calculation is unchanged:

```text
2c-1/2 <= (r-1)/(2r) + x/r - x^2/(2r),
c <= 1/2-1/(4r) when x=o(1).
```

Thus the exact five-role `r=4` formula, `c<=7/16`, and the conclusion `r>=7`
at `c=0.4585` all remain valid.

### P1: overlap cardinalities are asserted, not proved

The two carry-triangle inclusions in `primal/AMPLIFIER_RESULT.md` are proved
correctly.  Section 4 then says “Direct digit counting gives” the three exact
intersection sizes, but supplies only a finite check through `t=100`.  That is
not a proof for all even `t`.

A short complete repair is available.  For the target square `[B,2B-1]`:

- `it+j(t+1)=(i+j)t+j` is injective on the stated ranges, and it lies in the
  target iff `i+j>=t`.  Summing the triangular rows gives `t(t-1)/2`.
- For `it+j(t-1)`, separate `j=0` and `j>0`; for `j>0` its base-`t` quotient
  and remainder are `i+j-1` and `t-j`.  It lies in the target iff
  `i+j>=t+1`, giving another `t(t-1)/2`.
- The map `(i,j) -> i(t+1)+j(t-1)` is injective for even `t`, since
  `gcd(t-1,t+1)=1` and the allowed coordinate differences exclude a nonzero
  kernel vector.  Counting pairs whose value is below `B`, for
  `r=t-1-i`, gives `r+1+floor(2r/(t-1))` admissible `j` for
  `0<=r<=t-2`, and `t+1` for `r=t-1`.  Splitting at `r=t/2` sums to
  `t(t+2)/2`.

Together with the already-proved union inclusion, these give total incidence
`3t^2/2` and overlap excess `t^2/2`.  The later `2/3` and `2/9` statements are
properly scoped to disjoint/local cells and should not be stated as universal
barriers to overlap-sharing constructions.

### P1: DRAT artifact is valid but not self-contained, and is ordinary-only

I regenerated the intended CNF with

```text
A={0,1,3,4,9,10,12,13}, target n=26, role cost <=15,
five roles, no carry-triangle clauses.
```

The regenerated DIMACS has 1,587 variables, 5,223 clauses, and SHA-256

```text
9e48179a28b0c33bb66e616919e6c739c75cef36db89da0a16c6cbc7eba44cea.
```

Fresh `drat-trim` verification of
`computation/k8_bad_cost15.drat.gz` against that CNF returned `s VERIFIED`
(93,224 core lemmas and 2,897,307 resolution steps).  Thus, together with the
decoded cost-16 placement in `EXTREMAL_ROLE_RESULTS.json`, it really certifies
ordinary five-role optimum 16 for that basis.

However, neither the CNF nor its metadata/hash is preserved in the directory,
so the DRAT file alone does not identify its proposition.  Preserve the CNF
and metadata (including the above hash and the proof hash) or add a deterministic
regeneration-and-verification command.  Also, `role_cnf.py` has no triangle
clauses: this DRAT proof must **not** be cited as a certificate for the
triangle-enhanced optimum.  The triangle lower bounds and most other optimum
claims currently rely on CP-SAT's `OPTIMAL` result, with decoded feasible
placements independently checked but no proof-producing lower-bound artifact.

### P2: metadata/source-scope cleanups

- `EXTREMAL_ROLE_RESULTS.json` and `primal/TRIANGLE_ROLE_RESULTS.json` say their
  scope is `1<=k<=8` but both contain an additional `k=9` row.  Change the
  scope to `1<=k<=9`, or omit that row.  The prose claim restricted to `k<=8`
  remains true.
- The duplicated sentence at lines 220--221 of the current
  `primal/AMPLIFIER_RESULT.md` should be deleted once.
- `computation/published_role_probe.py` says all bases are from Tables 1 and 2,
  but its cardinality-41/range-536 row is from Table 3.  Say “Tables 1--3.”
  The actual transcriptions and the distinction between global and restricted
  extrema agree with Kohonen's paper.
- Do not summarize all of `PUBLISHED_ROLE_RESULTS.json` as satisfying
  `cost=k+u`: its range-536 row has `k=41`, `u=12`, but ordinary and triangle
  costs 54, one above `k+u=53`.  `ROLE_DEFECT_NOTES.md` carefully restricts
  its equality claim to the tested cardinalities 9 through 21 and separately
  treats the different 41-coordinate/range-509 macro union, so that document
  is currently accurate.

## Theorem-by-theorem verdict

### Typed substitution and full closure: PASS

For a fixed certificate of role cost `L` covering `m` macro squares, the lift
has size at most `L(t+1)` and range at least `mt^2-1`.  For arbitrary large
budget `K`, the largest even `t` with `L(t+1)<=K` has `K<L(t+3)`, so
`(mt^2-1)/K^2 -> m/L^2`.  This proves the liminf bound for every `K`, not only
for a subsequence.  Applying it to each fixed member of a sequence with
`n_r/k_r^2 -> alpha_+` and `L_r/k_r ->1`, with `m=n_r+1`, correctly yields
`alpha_- >= alpha_+`.  Use of `|A|<=K` makes padding unnecessary, though padding
is harmless.

The scalable Kohonen placement also checks out algebraically:
`L_t=42t+8`, the sole inherited overlap gives `k_t=42t+7`, the substituted
510-square certificate supplies the first `510t^2` squares, and the terminal
`137+372=509` `I+K` interaction supplies the extra `t`.  Its limiting density
is only `510/42^2=85/294`, as stated.

### Unique sums and role defect: PASS after the general-`r` repair

Every ordinary or triangle coverage alternative contains one of the nine
current role pairs, whose graph is exactly `K5-L0L1`.  A cost-`k+delta`
assignment has at most `delta` multiply typed coordinates.  Deleting them and
merging `L0,L1` makes the remaining unique-sum graph four-colorable.

For deletion size `d`, the exact `r=4` edge bound (2) is correct.  The
representation count

```text
u >= 2(n+1)-C(k+1,2),
e >= u-k
```

correctly separates at most `k` unique diagonal sums.  Normalization gives

```text
2c-1/2 <= 3/8+x/4-x^2/8,
x >= 1-sqrt(8-16c),
```

so near-lossless five-role typing forces `c<=7/16`; at `c=0.4585` the stated
defect lower bound `0.185138...` is correct.  For a finite non-asymptotic
statement one may take `d<=min(delta,k)`; the current use is in the
`delta/k` regime.

The structured bipartite-representation-selection sufficient condition is
also correct: color off-diagonal chosen edges `I/J` and duplicate precisely
the vertices used by selected diagonal representations.

### Carry triangle: PASS, with the overlap proof addition above

Both parity case splits for inclusions (A) and (B) have valid parameter bounds
and exhaust their residual cases.  The abstract clauses agree exactly with
`triangle_predicate.py`, `phased_role_model.py`, and
`triangle_role_batch.py`.  Independent randomized comparison of the bitset
and set-based predicates on 5,000 placements passed for both ordinary and
triangle coverage; the existing literal regressions also pass.

### Analytic rounding and absorption: PASS

For a fixed target, its non-diagonal representation pairs are vertex-disjoint.
The two no-coverage events are decreasing, so Harris--FKG has the stated
direction.  The logarithmic product bounds, diagonal factor, global budgets
`sum theta<=dk` and `sum lambda<=k^2/2`, and Jensen averaging produce
`exp(-1/(2c))`.  The expectation-to-constant-probability step in Corollary 2.2
is valid because `0<=H<=M`; the repair-capacity inequality then forces a
linear repair.

The logarithmic sufficient alteration proposition and its pair-budget
impossibility are correct.  The block absorber is correct, including the
conditional `o(k)` closure statement.  The growing aggregate-residue
relaxation equality follows by projection and tensoring with Haar-uniform
measure; the document properly says it does not retain carry-tied lattice
information.

### Exact microtile factorization: PASS

With `q^2` cross-pairs and `q^2` required consecutive sums, the sum map is
bijective and there can be no outside sums.  Normalization gives
`P_XP_Y=G_q`.  For any fixed normalized `P_X`, its partner is the unique
quotient; squarefreeness of `G_q` excludes a self-partner.  Hence, after
identifying translations, the exact-type interaction graph is a matching.
For prime `q`, the two irreducible cyclotomic factors force the fine/coarse
pair.  The caveats for approximate, phased, and multi-pair tiles are essential
and are already present.  Without identifying translations, the raw graph is
a bipartite blow-up/subgraph of this matching, not literally a matching.

### Computation probes: PASS with solver/proof scope stated

- **K5:** the displayed range-38 set is a basis, and the ten sums on
  `{0,1,9,14,24}` are uniquely represented.  The CP model encodes exactly an
  interval basis plus a marked clique.  The “first through range 40” result is
  CP-SAT evidence rather than proof-producing global minimality, exactly as
  the notes already say.
- **Diagonal counterexample:** enumeration covers every subset of `[0,n]`
  (with forced `0,1` for `n>0`) in increasing `n`; it first reaches
  `{0,1,3,4,5}` at `n=9`, where cost at most seven is infeasible.  A fresh
  triangle-enabled solve returned optimum eight and its decoded placement
  covers `[0,9]`.  The two saved diagonal JSON files differ only in runtime.
- **Published bases:** all saved sets cover their advertised intervals.  The
  two range-46 sets and the restricted rows match Kohonen's Tables 1--3.  The
  restricted/global qualifications are correct.  `OPTIMAL` means exact under
  CP-SAT solver trust; feasibility is independently checkable from the saved
  placements where placements are retained.
- **CNF predicate:** ordered representation witnesses are intentional because
  role pairs are directed.  AND/OR channels and the unary at-most counter are
  bidirectional and consistent with the ordinary five-role predicate.  The
  CNF generator currently omits the carry-triangle alternatives.

## Bottom line for synthesis

Safe to synthesize as established: the conditional full-closure theorem, the
five-role `7/16` obstruction and its asymptotic general-`r` version, the exact
carry-triangle inclusions, the independent-rounding/repair barrier, the block
absorber, and the exact microtile matching theorem.  None resolves Erdős 791.
Before treating the directory as publication-grade, correct the finite
general-`r` Turan formula, insert the overlap count, and bind each machine
lower-bound claim to a reproducible proof artifact or explicitly retain the
CP-SAT-trust qualification.
