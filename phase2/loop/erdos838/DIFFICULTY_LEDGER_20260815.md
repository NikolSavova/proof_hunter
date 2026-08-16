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
| C2 | Threshold square-mesh Bellman inequality with harmonic loss | local bound loses only `O(log N log log(m+1))`; a controlled global sum would close a wider nonstrong construction class | ROUTE, not unrestricted gain | Local theorem proved; accumulated loss/geometric promotion open; `(WH)` is false | Bank local theorem; attack only a genuine global charge, not witness nesting |
| M1 | Universal/minimizer half-weight `H(P)=n^{o(1)}` | full coefficient `1/2` | EQUIVALENT/FULL | Open | Park as headline, not active reduction |
| M2 | Peak mean `mu >= log_2 n-O(log log n)` for minimizers | full coefficient `1/2` | EQUIVALENT/FULL | Open | Park as headline, not active reduction |
| M3 | Hull-root Pareto curvature at the sharp cumulative scale | full coefficient `1/2` | Near-full; exact recurrence known | AUDIT + open curvature | Verify recurrence; attack only a strict sparse subcase |
| M3a | Hull-root increment rank-moment floor | `K_(n,1)>=ceil(m_n(f(n))/n)+n-1`, asymptotically `(c+o(1))f(n)log n/n` at coefficient `c` | STRICT exact increment theorem, but quantitatively below half | Proved after V3 audit | Bank; any continuation must add cross-chart/profile correlation rather than another scalar deletion sum |
| M4 | Strict minimizer mean gain: either `mu(P)>=(1/2+epsilon)log_2 n` for every large minimizer, or the low-mean closure inequality `E B<=(1-delta)mu(P)^2+o(mu(P)^2)` for some fixed `epsilon,delta>0`, where `B` is the number of exterior labels blocked from one-label face extension | The first form gives unrestricted coefficient `1/4+epsilon/2`; the second combines `log_2 V<=2mu+E B` with deletion to give coefficient at least `1/[4(1-delta)]>1/4` | STRICT, direct GAIN if proved; strictly weaker than the full mean target M2 | Parked after the two-reduction stop rule: exact `n=44,58` rational records kill the universal blocked bound with ratios `1.1002,1.3501`; minimizer relocation has the opposite first-order sign.  The low-mean variance version requires average variance above `1/(2 ln2)`, but its hereditary rank-concentration step is P1d | Preserve the exact stress verifier and threshold.  Reopen only with a genuinely multi-point minimizer inequality or an already-averaged positive-rank-interval theorem; see `STRICT_MINIMIZER_MEAN_GAIN_AUTOPSY_20260816.md` |
| E1 | Fixed-power EIC/product extraction | conditional `3/8-o(1)` route | STRICT at entry | Many subcases closed; final residue became EQUIVALENT | Park equivalent residue; retain proved subcases |
| D1 | Local natural two-tangent Hall decoder | hoped-for subpolynomial load | BARRIER | False by matching-star examples | Closed permanently |
| D2 | Global pooled Hall assembly | converts local codes to global codes with rank load | ROUTE | Internal proof + exact verifier | Independent audit |
| D3 | Global literal-history code; fixed-size pooled extension through `r<=1/4 log n-O(sqrt(log n log log n))` | closes the literal range to an explicit sublinear distance from the universal capacity boundary | STRICT range theorem | V5 independently audited; explicit boundary proved | `V5_INDEPENDENT_AUDIT_20260815.md`; `FIXED_SIZE_LITERAL_EXPLICIT_BOUNDARY_20260816.md` |
| D4 | Intermediate literal ranks `1/4 log n-O(sqrt(log n log log n))<r<log n` | would complete the current literal decoder coverage | STRICT local target, not by itself a coefficient gain | Open, explicitly narrowed; campaign parked | Do not attack in isolation. The universal rank-`k` bank has a structural capacity ceiling at `r=(1/4+o(1))log n`; reopen only as part of a new direct gain theorem |
| R1 | Unrestricted reset-chain/rectangle-or-shield telescope | intended full decoder | EQUIVALENT in surviving branches | Open | Stop branch; preserve barriers |
| P1 | At canonical size `4^k`, fixed-size supersaturation with any `eta>0` | improves unrestricted lower coefficient from `1/4` to `(1+eta)/4` by the exact bridge | STRICT, direct GAIN | Open, bounded campaign parked | The bridge remains valid, but the 2026-08-15 bounded attack hit its two-candidate stop rule. Reopen only with a genuinely new positive-rank-interval or direct rank-`k` theorem; see `FIXED_SIZE_BOUNDED_ATTACK_AUTOPSY_20260816.md` |
| P1a | Strong-tree fixed-rank diffuse branch | removes all diffuse heavy-path trees from P1; survivor has a `4^k/poly(k)` by `4^k/poly(k)` seam | STRICT construction-class reduction | Proved | `STRONG_TREE_FIXED_RANK_COMB_OR_SEAM_GATE.md`; exact verifier PASS |
| P1b | Near-full strong-seam graded profile alignment | would prove the `3/2` diagonal for all strong trees | STRICT construction-class gain | Open, narrowed | The unordered finite-size error is now removed by `R_k(T)>=b_k(n-2^(k-2))_+^k`; the exact plane endpoint formula is proved, but the same shifted plane constant is false on the 256-leaf alternating comb. A shifted/excess orientation comparison remains open (`UNIFORM_GROWING_RANK_ROOTED_CATERPILLAR_THEOREM_20260816.md`) |
| P1c | Standard fixed-size literature mechanisms | hoped-for gain in P1 from fixed-`k` counts, one positive-fraction box, or scalar weighted polygon identities | BARRIER | Audited: all have coefficient-one ceiling or admit a zero-high-rank fake ledger | Do not revisit without a cross-rank geometric compatibility input; see `FIXED_SIZE_SUPERSATURATION_PRIOR_ART_AUDIT_20260816.md` |
| P1d | Successive-rank convex-density decay on `alpha k<=j<k` at `N=4^k` | decay constant `c<2` gives `eta=(1-c/2)(1-alpha^2)>0` and unrestricted coefficient `1/4+eta/4` | STRICT, direct GAIN if proved | Exact implication and stress audit proved; geometric inequality open | Valid but parked with P1 after P1e failed. Do not replace it by another local/threshold surrogate; reopen only with a theorem that already averages a positive rank interval. See `SUCCESSIVE_RANK_DENSITY_GAIN_GATE_20260816.md` |
| P1e | Adjacent-layer balance at one **fixed certified** upper sequence `ES(j+1)<=q_j=2^(j+o(j))`: require `v_j<=2^((lambda+o(1))j)v_(j+1)` with fixed `lambda<1` | would imply P1d with `c=1+lambda<2`, hence unrestricted coefficient `1/4+(1-lambda)(1-alpha^2)/8` | BARRIER / CLOSED | False at the exact prescribed size: a rational central-Pascal core strongly glued to an induced skew `T(41,27)` padding tower has `log(v_j/v_(j+1)) >= (1-1/(4 ln 2)-41/70-o(1))j^2`, with positive constant `0.053611954...` | Closed permanently. Preserve the exact averaging theorem as a conditional tool, but do not pursue any one-layer threshold surrogate. See `FIXED_THRESHOLD_ADJACENT_LAYER_COUNTEREXAMPLE_20260816.md` |
| P1f | Concentrated-pocket replacement after deleting at most half of a rank-`r` source | at `r=k/2`, deletion `r/2` would give fixed-size exponent `19/16>1` | BARRIER / CLOSED as a local lemma | Exact rational 12-point witness: a convex four-point pocket lies in one common addable source-edge pocket, yet its union with every nonempty source trace is nonconvex | Do not pursue a better local deletion fraction. The survivor is the existing pooled all-delete/rooted-pocket Hall or minimizer-mutation gate; see `P1D_CONCENTRATED_POCKET_REPLACEMENT_BARRIER_20260816.md` |

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
