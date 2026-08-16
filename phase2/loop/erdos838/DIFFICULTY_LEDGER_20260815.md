# Erdős 838: difficulty ledger and reduction stop rules

This ledger is additive.  It does not delete or supersede the full attack.
Its purpose is to prevent a renamed equivalent problem from being counted as
progress.

## Status vocabulary

- **GAIN:** proves a new unconditional coefficient, exponent, or range.
- **STRICT:** a quantitatively weaker target than the unrestricted half lower
  bound, with a written implication to a gain.
- **ROUTE:** closes one branch but does not itself improve the theorem.
- **EQUIVALENT:** coefficient-equivalent to the original lower-bound problem.
- **BARRIER:** a counterexample or impossibility result.
- **CONJECTURAL:** supported by tests only.
- **AUDIT:** proved internally, awaiting independent reconstruction.

## Ledger

| ID | Statement/route | Quantitative consequence | Difficulty | Current status | Action |
|---|---|---|---|---|---|
| U1 | Explicit iterated upper construction | `limsup <= 1/2` | GAIN | Proved and previously audited | Bank/publish |
| S1 | Strong-tree/decomposable lower theorem | coefficient `1/2` for that class | GAIN on a proper class | Proved and previously audited | Bank/publish |
| C1 | Hinged Kraft plus finite/variable-menu grammar closure | rules out broad recursive sub-half constructions | ROUTE | Internal proof + exact verifier | Independent audit; no deeper reduction |
| C2 | Square-mesh Bellman inequality with controlled accumulated loss | would close a wider nonstrong construction class | ROUTE, not unrestricted gain | CONJECTURAL; `(WH)` is false | One bounded attack only; kill if loss cannot telescope |
| M1 | Universal/minimizer half-weight `H(P)=n^{o(1)}` | full coefficient `1/2` | EQUIVALENT/FULL | Open | Park as headline, not active reduction |
| M2 | Peak mean `mu >= log_2 n-O(log log n)` for minimizers | full coefficient `1/2` | EQUIVALENT/FULL | Open | Park as headline, not active reduction |
| M3 | Hull-root Pareto curvature at the sharp cumulative scale | full coefficient `1/2` | Near-full; exact recurrence known | AUDIT + open curvature | Verify recurrence; attack only a strict sparse subcase |
| E1 | Fixed-power EIC/product extraction | conditional `3/8-o(1)` route | STRICT at entry | Many subcases closed; final residue became EQUIVALENT | Park equivalent residue; retain proved subcases |
| D1 | Local natural two-tangent Hall decoder | hoped-for subpolynomial load | BARRIER | False by matching-star examples | Closed permanently |
| D2 | Global pooled Hall assembly | converts local codes to global codes with rank load | ROUTE | Internal proof + exact verifier | Independent audit |
| D3 | Global literal-history code; fixed-size pooled extension through `r<=1/4 log n-O(sqrt(log n log log n))` | closes the literal range to an explicit sublinear distance from the universal capacity boundary | STRICT range theorem | V5 independently audited; explicit boundary proved | `V5_INDEPENDENT_AUDIT_20260815.md`; `FIXED_SIZE_LITERAL_EXPLICIT_BOUNDARY_20260816.md` |
| D4 | Intermediate literal ranks `1/4 log n-O(sqrt(log n log log n))<r<log n` | would complete the current literal decoder coverage | STRICT local target, not by itself a coefficient gain | Open, explicitly narrowed | Attack only through `P1`; the universal rank-`k` bank has a structural capacity ceiling at `r=(1/4+o(1))log n` |
| R1 | Unrestricted reset-chain/rectangle-or-shield telescope | intended full decoder | EQUIVALENT in surviving branches | Open | Stop branch; preserve barriers |
| P1 | At canonical size `4^k`, fixed-size supersaturation with any `eta>0` | improves unrestricted lower coefficient from `1/4` to `(1+eta)/4` by the exact bridge | STRICT, direct GAIN | Open | Sole primary proof target; bridge proved in `FIXED_SIZE_GAIN_BRIDGE_20260815.md` |
| P1a | Strong-tree fixed-rank diffuse branch | removes all diffuse heavy-path trees from P1; survivor has a `4^k/poly(k)` by `4^k/poly(k)` seam | STRICT construction-class reduction | Proved | `STRONG_TREE_FIXED_RANK_COMB_OR_SEAM_GATE.md`; exact verifier PASS |
| P1b | Near-full strong-seam graded profile alignment | would prove the `3/2` diagonal for all strong trees | STRICT construction-class gain | Open, narrowed | Exact plane one-turn caterpillar formulation; fixed-`k` unordered inducibility has the right main exponent but nonuniform error and wrong orientation (`FIXED_RANK_STRONG_TREE_CATERPILLAR_AUDIT_20260815.md`) |

## Mandatory rule for new entries

Every proposed lemma must be entered above or in a dated successor ledger
before a new attack starts.  Its entry must contain:

1. the exact implication to a coefficient, exponent, or rank range;
2. why it is strictly weaker than its parent target;
3. a counterexample class it must survive;
4. a kill condition.

If the implication invokes the unrestricted lower bound on a comparably sized
arbitrary point set, mark it **EQUIVALENT** and stop.  If a branch reaches
three successive reductions without a quantitative improvement, park it and
write an autopsy.  Existing names should be reused; no new metaphorical object
name is introduced merely for a residual case.
