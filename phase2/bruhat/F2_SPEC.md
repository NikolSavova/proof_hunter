# F2 SPEC (frozen for the blind drafts — do not weaken the statement)

## Objects
I_m(k) = #{sigma in S_m : inv(sigma) = k} (Mahonian numbers), so
sum_k I_m(k) q^k = prod_{i=1}^m (1 + q + ... + q^{i-1}) = [m]_q!.
N = m(m-1)/2 (degree; the sequence is symmetric and log-concave).
sigma_m^2 = Var(inv) = m(m-1)(2m+5)/72  (inv = sum of independent
U_j ~ Unif{0..j-1}).
Log-concavity ratio at k: r_m(k) = I_m(k)^2 / (I_m(k-1) I_m(k+1)), and
r_m = min_{1<=k<=N-1} r_m(k).

## THEOREM F2 (target — prove all three parts)
(a) [asymptotic] r_m = 1 + sigma_m^{-2} (1 + o(1))  as m -> infinity.
    (Equivalently r_m - 1 ~ 36/m^3; the 1/sigma^2 form is the sharp one.)
(b) [location] The minimum is attained centrally: argmin k satisfies
    |k - N/2| <= 1 (empirically EXACT: argmin = floor(N/2) for all
    4 <= m <= 40; see ground truth).
(c) [stretch — attempt, flag if not achieved] A fully explicit
    non-asymptotic bound: r_m >= 1 + c / sigma_m^2 for ALL m >= 5 with an
    explicit constant c (ground truth: sigma^2 (r_m - 1) is increasing in m,
    = 0.875 at m=5, -> 1; so c = 7/8 is plausibly provable).

## Ground truth (exact; MUST be used to check every intermediate claim)
Run:  python3 mahonian.py --mmax 40        (same directory)
Key facts it shows: argmin always central; min ratio == central ratio for
m >= 5; sigma^2 (r_m - 1) increasing 0.84 -> 0.97 (m=4..40).

## Published ingredients (cite precisely; do NOT re-derive as if new)
- Log-concavity of I_m(k): Bona (Electron. J. Combin., direct proof);
  product-closure route: Hoggar 1974 / Kook 2006 (each factor uniform,
  log-concave; products preserve log-concavity).
- inv = sum of independent uniforms; asymptotic normality + LOCAL limit
  theorem: Canfield-Janson-Zeilberger, arXiv:0908.2089 (Adv. Appl. Math.
  2011). CRITICAL: their Theorem 4.6 / eq. (4.11) already proves
  P(k)^2 - P(k-1)P(k+1) = (sigma^{-2} + O(n^{-4})) P(k)^2 for the CENTRAL
  GAUSSIAN BINOMIAL in the central window. Our (a) is the q-factorial
  analogue + (b)/(c) are the global statements they do NOT prove.
- Edgeworth expansions for lattice sums of independent non-iid uniforms
  (any standard source; Petrov) for the error control.

## Proof obligations (what a complete draft must contain)
1. A local expansion of I_m(k) in the central window |k - N/2| <= C sigma
   with explicit error term (local CLT for the sum of uniforms; the
   characteristic function of inv factors exactly — use it).
2. From 1: central ratio = 1 + sigma^{-2} + (error) — the CJZ transfer.
3. The GLOBAL argument: r_m(k) > central value for k outside the window
   (log-concavity gives I(k+1)/I(k) monotone; you need a quantitative
   second-difference statement in the tails — this is the genuinely new
   part; be rigorous or mark GAP).
4. (b): argmin centrality from 2+3 (or an exact symmetric argument).
5. (c) if attempted: explicit constants throughout.

## Rules for the draft
- Numbered lemmas with explicit dependencies; every analytic estimate gets
  a "NUMERIC CHECK:" line saying what to compute with mahonian.py and the
  expected outcome (the referee will run them).
- Mark every unproven step "GAP:" honestly — a draft with honest gaps
  beats a slick wrong proof.
- <= ~6 pages equivalent. Self-contained modulo the cited results.
- Do NOT look at any other draft (blind protocol).
