# maths referee (gpt-5.6-sol, effort=max) — sol_s4seed_20260812.md — 2026-08-12 19:48

> Cross-model referee report (Sol on the reviewed draft). Numeric checks are
> DERIVED, not executed — script them before trusting.

## Hand recomputation

### SOL.1: curvature algebra

The identity is correct:
\[
p_{-1}p_1=(p_0-C+B)(p_0-C-B)=(p_0-C)^2-B^2,
\]
hence
\[
D=2p_0C-C^2+B^2.
\]

The Fourier bound also has the correct constant. After taking absolute values,
\[
\frac12\iint |\phi(t)\phi(s)|(t-s)^2\,dt\,ds=I_0I_2,
\]
because \(|\phi|\) is even and the mixed term vanishes. Thus
\[
|D|\le \frac{I_0I_2}{4\pi^2}.
\]
Positivity of \(D\) follows either from log-concavity or later from the quantitative \(C\)-bound.

### SOL.2: variance scale

From the Riemann-sum estimate,
\[
\frac{H^2}{m}
\ge h(\lambda)-\frac{\pi^2}{3m\lambda}.
\]
The two advertised endpoint computations are valid:
\[
1-\frac{0.1^2}{12}-\frac{\pi^2}{12}
   \approx0.176699>0.176,
\]
and
\[
1-\frac{0.89^2}{12}-\frac{\pi^2}{210}
   \approx0.88699.
\]
Consequently
\[
H^2\ge0.176m,\qquad
S_*=\frac{123.2}{0.89^2}\approx155.5359,\qquad
\delta_*=\frac5{616}\approx0.00811688.
\]
The threshold arithmetic for \(m\ge700\) is sound.

### SOL.3: moment estimates

For \(j\ge2\), the rearrangement argument gives the stated finite-support ratio, and extending the support to all \(d\ge1\) increases the average of \(d^{r-2}\). The resulting formulas are correct:
\[
R_3(q)=\frac{1+4q+q^2}{1-q^2},
\qquad
R_4(q)=\frac{1+10q+q^2}{(1-q)^2}.
\]
At \(\lambda=0.89\),
\[
\lambda R_3\approx3.009<3.05,\qquad
\lambda^2R_4\approx12.03<12.5.
\]
Thus the constants \(6.10\) and \(25\) are safe.

### SOL.4: characteristic-function bounds

The quartic envelope is algebraically correct:
\[
\log|\phi(t)|
\le-\frac{\sigma^2t^2}{2}
  +\frac{25\sigma^2t^4}{48\lambda^2}.
\]
The local constants recompute to
\[
\alpha\approx0.461952110,\qquad
\beta=\frac{71}{192}\approx0.369791667.
\]

For the first middle range,
\[
\frac{71}{768}\frac{22}{125}
   =0.016270833\ldots>\frac{13}{800}.
\]
Using \(1.179\) in the selected-factor bound gives decay rates approximately \(0.02648\) and \(0.0532\), so the advertised \(0.0264\) and \(0.052\) are safe, albeit not generous.

The integral arithmetic is also consistent:
\[
J_0\approx2.6401<2.641,\qquad
J_2\approx3.1573<3.160.
\]
At \(m=700\), the middle second-moment contribution is about \(0.2126<0.213\), and the far contribution is about \(9.6\times10^{-4}<0.001\). Hence \(U_0=2.642\) and \(U_2=3.374\) are valid.

### SOL.5: \(p_0\) and \(C\)

The local parameters recompute as
\[
\varepsilon\approx0.0021377,\qquad
\gamma\approx0.09398.
\]
The point-mass central lower estimate is about \(2.28927\) before the outer subtraction, so the conclusion
\[
2\pi\sigma p_0>2.2005
\]
is numerically plausible and consistent with the displayed bounds.

For \(C\), the moments are approximately
\[
M_2=1.85124,\quad M_4=3.3883,\quad
M_6=8.2802,\quad M_8=23.316.
\]
The central contribution exceeds \(0.864\). Also,
\[
2\int_2^3z^2e^{-\alpha z^2}\,dz\approx0.7235<0.725,
\]
and the \(\beta\)-tail is below \(0.335\). Thus
\[
C>\frac{0.227}{2\pi\sigma^3}>
\frac{0.0355}{\sigma^3}
\]
is arithmetically consistent.

### SOL.6: final ratio algebra

The final constants recompute to
\[
K_D=\frac{2.642\cdot3.374}{4\pi^2}
   \approx0.22580<0.226,
\]
\[
A_*=\frac{0.226}{0.349^2}\approx1.85549,
\qquad
\frac{A_*}{1-A_*/S_*}\approx1.8779<1.879.
\]
For the lower endpoint,
\[
2(0.349)(0.0355)-\frac{0.269^2}{S_*}
   \approx0.0243137>0.02431,
\]
and division by \(0.421^2\) gives approximately \(0.13718>0.137\).

Thus the analytic argument does appear to establish the seed bound on its actual stated tail range \(m\ge700\), subject to the local proof repairs below. It does **not**, however, establish the campaign’s full named statement (S4).

VERDICT: MAJOR_ISSUES

1. **(SOL.6 final paragraph; “Together with the established M3 closure on \(561\le m\le699\), no seed input remains”; why wrong)** The proof establishes the ratio seed only for \(m\ge700\). The formal (S4) consumed by the current composition is stated on the whole deep-tilt range \(m\ge561\). In the supplied ledger, M3 is an \(R.1\) cell-floor/crossover result and an SL4′-X-free alternative on the grid rung; it is not stated as a proof of  
   \[
   \left|s_2(r(k)-1)-1\right|\le0.89,
   \]
   nor is it stated to bypass every use of INFL/QUADF or (S4). Invoking M3 therefore does not fill \(561\le m\le699\), and may itself sit downstream of the seed. Either prove the seed on that finite range or supply a revised, dependency-audited composition theorem proving that the finite rung never consumes S4.

2. **(Opening “Seed theorem,” SOL.6.4, and WHAT REMAINS items 1/5; claim that this “closes (S4)”; why wrong)** The opening theorem is presented without its actual \(m\)- and \(m|\lambda|\)-scope, while the restrictions appear only at the end. What has been proved is a tail sublemma, not the named campaign statement S4. The status language must say “S4 for \(m\ge700\)” until Issue 1 is resolved.

3. **(SOL.6 final theorem; \(4/m<|\lambda(k)|\); why wrong)** The composition bands use the closed edge \(m|\lambda|\ge4\). The displayed theorem excludes \(m|\lambda|=4\). Nothing in the proof requires strictness—every relevant estimate was derived under \(m\lambda\ge4\)—so this is repairable by changing the theorem to \(4/m\le|\lambda(k)|\), but the current formal statement leaves a band-edge gap.

4. **(SOL.6 final paragraph; “\(0.88<0.89412\)” and automatic invocation of the M2 iteration; why wrong)** No exact theorem with basin endpoint \(0.89412\), its hypotheses, and its \(m,\lambda\)-scope is quoted. The supplied ledger records only rounded basin information and a composition-level adoption of the chord/iteration repair. The draft must cite the exact landed iteration statement and verify that it consumes only this seed, rather than silently relying on an unlanded referee repair or on M3. The extra precision \(0.89412\) is unsupported here, although \(0.88<0.894\) would already suffice if the interface were properly stated.

5. **(SOL.3.1; direct passage from the decreasing finite-length factor to sums over all \(d\ge1\); why incomplete)** Rearrangement first compares with the unweighted ratio on the same finite support \(1\le d\le j-1\). A second argument is needed to show that extending the support to infinity increases the weighted average of \(d^{r-2}\). Also \(j=1\) has zero denominator and must be removed as a deterministic summand. Both repairs are elementary, but they are absent.

6. **(SOL.3.4; “Since \(h(\lambda)\le1-\lambda^2/24\)”; why incomplete)** This stronger upper bound was not established in SOL.2, which only recorded \(h\le1\). It is load-bearing for the constant \(12.5\). It is true and can be repaired in one line: with \(x=\lambda/2\), use \(\sinh x/x\ge1+x^2/6\) and, on \(x\le0.445\), \((1+x^2/6)^{-2}\le1-x^2/6=1-\lambda^2/24\).

7. **(SOL.5.3; multiplication of the modulus and cosine lower bounds; why incomplete)** Near \(z=5/2\), the quadratic cosine lower bound \(1-\gamma^2z^6/2\) is negative. One cannot blindly multiply a lower bound for \(|\phi|\) by a negative lower bound for \(\cos(\arg\phi)\). The displayed inequality is salvageable because \(|\arg\phi|<\pi/2\): where the proposed right-hand side is negative, \(\Re\phi>0\) makes it trivial; where it is nonnegative, the multiplication is legitimate. That case split and the continuous choice of argument must be stated.