# Part I referee — numerics lane (gpt-5.6-sol, effort=max, 2026-08-12 23:56)

> Adversarial, default-to-refutation. Numeric claims made HERE are derived,
> not executed — script them before trusting.

## Referee finding

The numerical harness is materially oversold: block [D] is not a certificate of uniqueness, block [F] is not a test at all, and block [C] passes a weaker threshold than its output claims. Nevertheless, I cannot kill the mathematical result because Lemmas SOL.2 and SOL.5 give a valid, entirely analytic global uniqueness proof.

### 1. Independent recomputations

For
\[
q(t)=e^t+(4t^2-2)e^{-t^2},
\]
\[
q'(t)=e^t+4t(3-2t^2)e^{-t^2}.
\]
The three-interval positivity argument in SOL.2 is correct, so \(q\) is strictly increasing on \([1,2]\). Hence
\[
\inf_{[1,2]}q=q(1)=e+\frac2e.
\]
Numerically,
\[
e+\frac2e
=3.454040710801929878551335011675\ldots
\]
Thus `3.454041` is the correctly rounded six-decimal display, but it is not an exact lower bound.

In particular, the statement in `PROBLEM.md`
\[
h_x''\ge 3.454041
\]
is false if interpreted literally. For example, at \(t=1\) and \(x_2=10^{-8}\),
\[
h_x''(1)
=3.454040710801929\ldots+2\cdot10^{-8}
=3.454040730801929\ldots
<3.454041.
\]
The safe statement is
\[
h_x''(t)>e+\frac2e>3.454,
\]
or simply the proof's exact bound \(h_x''>17/5\).

The rational comparison is also correct:
\[
\frac{41}{12}=3.416666\ldots>\frac{17}{5}=3.4.
\]

For the nonconvexity witness,
\[
\frac{(1,-1)+(2,-4)}2
=\left(\frac32,-\frac52\right),
\]
whereas the arc at first coordinate \(3/2\) is
\[
\left(\frac32,-\frac94\right).
\]
The vertical discrepancy is exactly
\[
-\frac94-\left(-\frac52\right)=\frac14.
\]
This part is exact and correct.

For the constants in block [B],
\[
K(x)=x_1\ln x_1-x_1+x_2\ln x_2-x_2.
\]
Independent values are
\[
\begin{array}{c|c}
x & K(x)\\ \hline
(1,1)&-2\\
(0.05,7.3)&7.011696127849\ldots\\
(9,0.02)&10.676780735917\ldots
\end{array}
\]
matching the archived output. However, the source never actually compares its computed constant with `K(x)`; it only checks constancy in \(t\).

### 2. What happened in block [C]

The discrepancy
\[
3.453673<q(1)=3.454041\text{ (rounded)}
\]
is explained by interval dependency, not by a failure of the formula.

On the first cell
\[
I=\left[1,1+\frac1{4000}\right],
\]
natural interval evaluation can combine:

- the lower value \(e^1\) from \(e^t\),
- the lower coefficient \(4(1)^2-2=2\),
- the lower exponential \(e^{-(1+1/4000)^2}\).

These extrema do not occur at the same \(t\). The resulting lower enclosure is approximately
\[
e+2e^{-(1+1/4000)^2}
=3.45367288\ldots,
\]
which explains the archived `3.453673`.

What is wrong is the interpretation:

- `3.453673` is a conservative lower bound from the cell enclosure, not the value of the infimum.
- The code tests only
  ```python
  good = worst[0] > 3.45
  ```
  but prints that the claim \(h''\ge3.454\) passed.
- Since \(3.453673<3.454\), that run does not certify the printed \(3.454\) threshold.

It does certify a bound around \(q>3.45\), which is more than enough for strict convexity. The analytic proof supplies the stronger exact result anyway.

### 3. Block [D] does not test the claimed theorem

Block [D] is a finite smoke test, not evidence for
\[
\forall x\in(0,\infty)^2,\quad \arg\min_{t\in[1,2]}h_x(t)
\text{ is a singleton}.
\]

Its weaknesses are substantial:

1. It samples only 27 points in an unbounded two-dimensional domain.
2. It checks only 20,001 grid nodes in \(t\), not the continuous interval.
3. It counts only strict interior grid-local minima, excluding endpoints.
4. It accepts `loc <= 1`, including zero.
5. It accepts an “argmin span” below \(10^{-3}\), so two distinct grid minimizers one grid step apart would pass.
6. The two advertised extreme corners,
   \[
   (10^{-4},10^4),\qquad(10^4,10^{-4}),
   \]
   are easy monotone cases forcing endpoint minima, not difficult uniqueness cases.

The hardest omitted points lie on or near the endpoint-transition surfaces, or involve cancellation at very large scales.

Define
\[
A(t)=e^t-2te^{-t^2}.
\]
Since \(h_x'\) is strictly increasing, the exact classification is
\[
t_x=1
\iff x_1\le A(1)+2x_2,
\]
\[
t_x=2
\iff x_1\ge A(2)+4x_2,
\]
with a unique interior zero otherwise. Here
\[
A(1)=e-\frac2e=1.982522946116\ldots,
\]
\[
A(2)=e^2-4e^{-4}=7.315793543376\ldots.
\]

Adversarial points missing from [D] include:

- Exact left transition:
  \[
  x=\left(e-\frac2e+2,\,1\right)
  \approx(3.9825229461,1),
  \]
  for which \(h_x'(1)=0\) and \(t=1\) is still uniquely minimizing.

- Exact right transition:
  \[
  x=(e^2-4e^{-4}+4,\,1)
  \approx(11.3157935434,1),
  \]
  for which \(h_x'(2)=0\) and \(t=2\) is uniquely minimizing.

- Exact interior minimum at \(t=3/2\):
  \[
  x=\left(e^{3/2}-3e^{-9/4}+3,\,1\right)
  \approx(7.1654913967,1).
  \]

- Near-boundary but interior:
  \[
  x_2=\varepsilon,\qquad
  x_1=e^{3/2}-3e^{-9/4}+3\varepsilon,
  \]
  which keeps the minimizer exactly at \(3/2\) as \(\varepsilon\downarrow0\).

- Large-scale cancellation:
  \[
  x_2=M,\qquad
  x_1=3M+e^{3/2}-3e^{-9/4},
  \]
  which keeps the minimizer at \(3/2\) as \(M\to\infty\). Testing this numerically requires precision exceeding the scale of \(M\).

For wildly separated scales,
\[
x=(\varepsilon,M)\implies t_x=1,\qquad
x=(M,\varepsilon)\implies t_x=2
\]
for sufficiently large \(M/\varepsilon\). Thus uniqueness does hold at all these corners, but because of the analytic curvature proof—not because block [D] sampled them.

### 4. Exact allocation of support

**Supported by the archived executed computation:**

- Two pointwise checks of the generalized-KL formula in [A].
- Nine pointwise checks that \(D(x,c(t))-h_x(t)\) is constant in \(t\) in [B].
- An interval lower bound of approximately \(3.4536729\) for \(q\), hence a bound \(q>3.45\), in [C].
- A discrete-grid observation for 27 sampled \(x\)'s in [D].
- Numerical arithmetic for the midpoint witness and its \(0.25\) gap in [E].

**Supported by analytic argument, not by the executed harness:**

- Legendre status, conjugate, domains, and \(U^*=\mathbb R^2\).
- Compactness and closedness of \(C\) and \(C^*\).
- The exact identity \(D_f(x,c(t))=K(x)+h_x(t)\).
- The exact curvature identity \(h_x''=q+2x_2\).
- Strict increase of \(q\) and the exact value \(\inf q=e+2/e\).
- Global uniqueness for every \(x\in U\), including endpoint minimizers.
- Nonconvexity of \(C^*\).
- The optional claims that \(C\) is nonconvex and \(f\) is supercoercive.

Block [F] contributes no executed verification: it merely prints conclusions and unconditionally returns `True`. Block [A] likewise prints the surjectivity and \(U^*\) claims without testing them.

**Supported by neither attached executed output nor a valid numerical claim:**

- `PROBLEM.md`'s assertion that the minimum was “verified to 30 digits this session.” The archive prints neither \(q(1)\) nor 30 digits. This is **FABRICATED-until-sourced** as a claim about executed verification.
- The literal inequality \(h_x''\ge3.454041\), which is false.
- The description of [D] as “exhaustive brute-force minimisation” establishing the actually claimed uniqueness property.
- Any implication that the displayed SymPy recipe was executed: it is source only, with no archived output. Its identities are nevertheless correctly established by the written algebra.

### 5. Scope and published-theorem check

The final theorem is appropriately narrow: it claims an explicit compact set that is globally right Chebyshev, has nonconvex gradient image, and satisfies the closure condition. It expressly disclaims priority for negative-entropy nonconvex examples and does not claim to settle hypothesis (b). I find no novelty overstatement in `proof_part1`.

I also find no contradiction with the cited Luo–Meng–Wen–Yao theorem: their full-domain condition \(U=X\) fails here because \(U=\mathbb R^2_{++}\).

The numerical package therefore needs correction, but the analytic proof survives independently.

VERDICT: MINOR_REPAIRS

1. **Location:** `PROBLEM.md`, Candidate Answer, curvature bullet. **Claim:** \(h_x''\ge3.454041\). **Why wrong:** \(e+2/e=3.4540407108\ldots\), and sufficiently small positive \(x_2\) gives \(h_x''(1)<3.454041\). **Suggested fix:** State \(h_x''>e+2/e>3.454\), or retain the exact \(17/5\) certificate.

2. **Location:** `verify.py:block_C` and archived block [C]. **Claim:** The interval run establishes the infimum as `3.453673` and passes the `3.454` bound. **Why wrong:** `3.453673` is only a dependency-inflated cell lower bound, and the code tests `>3.45`, not `>=3.454`. **Suggested fix:** Label it “certified lower bound \(>3.45\),” or refine the subdivision and test the advertised threshold; do not print it as the infimum.

3. **Location:** `verify.py:block_D`, its docstring, and archived block [D]. **Claim:** The grid scan directly verifies uniqueness/the property actually claimed. **Why wrong:** It examines finitely many \(x\)'s and \(t\)-nodes, omits endpoint local-minimum counting, and even permits multiple nearby grid argmins. **Suggested fix:** Relabel [D] as a smoke test and rely on SOL.2–SOL.5 for the universal certificate; add transition and scale-balanced points only as diagnostics.

4. **Location:** `verify.py` blocks [A], [B], [F]. **Claim:** These blocks computationally verify all model and hypothesis bookkeeping. **Why wrong:** [A] merely prints surjectivity, [B] does not compare the constant with \(K(x)\), and [F] unconditionally returns `True`. **Suggested fix:** Add actual symbolic/numeric assertions where possible, or clearly mark these statements as analytically proved rather than executed checks.

5. **Location:** `PROBLEM.md`, “verified to 30 digits this session.” **Claim:** An attached run produced a 30-digit minimum. **Why wrong:** No attached archived output contains that evaluation. **Suggested fix:** Delete the execution claim or archive an explicit high-precision evaluation; until then it is FABRICATED-until-sourced.