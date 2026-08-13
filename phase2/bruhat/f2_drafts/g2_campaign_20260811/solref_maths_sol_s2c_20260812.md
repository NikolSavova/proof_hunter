# maths referee (gpt-5.6-sol, effort=max) — sol_s2c_20260812.md — 2026-08-12 19:10

> Cross-model referee report (Sol on the reviewed draft). Numeric checks are
> DERIVED, not executed — script them before trusting.

I found no load-bearing algebraic error or circular dependence on (S1), (S3), or (S4). Subject to independent validation of the exact-rational computations, the argument proves a bound stronger than the composition’s stated (S2).

### Algebraic audit

- **SOL.1:** The derivative signs are correct:
  \[
  L_m^{(n)}=(-1)^n\!\left(mA_{n-1}-\sum j^nA_{n-1}(j\lambda)\right),
  \]
  and hence \(L_m^{(5)}=\sum j^5A_4-mA_4\). The Taylor coefficients, the factor \(1/4!\), and the \(E_4\)-representation all agree.

- **SOL.2:** The scaling is correct:
  \[
  D_m(h)=h^2s_2,\qquad N_m(h,a)=h^5L_m^{(5)}(ha).
  \]
  Substitution therefore gives exactly
  \[
  \frac{h^3|R_5|}{s_2t^5}
  \le \frac1{24D_m(h)}\int_0^1(1-u)^4|N_m(h,a_u)|\,du.
  \]

- **SOL.3:** The Mittag–Leffler signs and factors \(24\) are correct. The \(F_a''\) and \(G''\) formulas and their termwise integral identities check out. The local coefficient evaluates to approximately
  \[
  \frac{240(9/8)(509/500)}{6.2^6}=0.004839\ldots<\frac1{200}.
  \]
  The proof of \(1-G(y)\le y^2/12\), \(\int G=\pi^2/3\), and the exact \(G(0.89)\) comparison is correct.

- **SOL.4:** The W7 calculation is correct:
  \[
  |R_5|\le \frac{50m}{120\lambda^5}t^5,
  \qquad
  \frac{D_m(\lambda)}m>
  0.93649-\frac{3.29}{40}
  =\frac{5339}{6250},
  \]
  giving
  \[
  \frac{\lambda^3|R_5|}{s_2t^5}
  <\frac{15625}{32034}
  =0.487762\ldots<0.50.
  \]

- **SOL.5:** The corrected \(L^1\) trapezoid constant \(1/8\), endpoint signs, and powers of \(h\) are correct. In particular,
  \[
  hN_m=P+w(F_a(0)-F_a(h))
       +\frac h2(F_a(w)-F_a(0))+\varepsilon_F
  \]
  and
  \[
  hD_m=H+w(G(h)-1)+\frac h2(1-G(w))-\varepsilon_G.
  \]
  The \(E_b/120\) term in SOL.5.7 is also correct.

- **SOL.6:** The coefficient factor is correctly
  \[
  \frac{(n+5)!}{n!}=(n+5)Q_n,
  \]
  and \(24\binom{n+4}{4}=Q_n\). The beta integral produces precisely SOL.6.4. The Cauchy majorant is below \(1.010\times10^6\), and the resulting tail is about \(1.09\times10^{-5}\), below the asserted \(11\times10^{-6}\). The \(r\ge65\) geometric-tail factor \(13000/8977\) also recomputes correctly. The reported 512-cell outputs remain a load-bearing matter for the numerics referee.

- **SOL.7:** The \(2w\) term is correctly generated only after weighted \(u\)-integration. The derivatives of \(J_4,J_5\) have the stated signs. At \(w=14\),
  \[
  (24w)^2=112896<6(138.6)^2=115259.76,
  \]
  so the angular improvement is valid. The monotonicity numerator satisfies
  \[
  (24-F_1)H-N(1-G)>121.055-w>0
  \]
  throughout \(14\le w\le40\).

- **SOL.8 and scope:** Recalculation gives approximately
  \[
  0.02594,\ 0.01890,\ 0.03786,\ 0.09100,\ 0.14377,\ 0.17610,
  \]
  as claimed. At \(m=561,w=40\), \(h=40/561\), exactly within SOL.3B; W7 starts strictly at \(w>40\). The assignments
  \[
  (4,5],(5,6],(6,8],(8,10],(10,20],(20,40],(40,0.89m]
  \]
  leave no gap, and all shared endpoints are covered by the stronger left-band estimate.

The exact-grid, scalar-tail, and 512-cell values still require the separate numerics pass; this mathematics verdict only confirms that they are used in the proof with the correct formulas, directions, and normalization.

VERDICT: MINOR_REPAIRS

1. **(Opening boxed table and Theorem SOL.8, claim: the displayed strengthened table is the composition’s fixed \(C_5^*\) table and therefore literally “Statement (S2),” why wrong: the governing interface records a pre-existing \(C_5^*\) table whose range extends through \(0.80\), whereas this draft redefines the same symbol with a stronger terminal value \(0.50\) and uses the \(W_{6b}\) label. The stronger theorem does imply the consumed hypothesis, but the interface should not be silently redefined. Rename the strengthened table, quote the composition table verbatim, and add the componentwise implication \(\widetilde C_5(W)\le C_5^*(W)\).)**

2. **(Lemma SOL.3B, claim: the displayed bounds justify \(|a|h<2/25\), why wrong: the coarse bound \(|a|<9/8\) alone gives \((9/8)(40/561)=15/187>2/25\). The desired inequality is nevertheless true from the sharper bound:
   \[
   |a|h\le\frac{\sqrt5}{2}\frac{40}{561}
   =\frac{20\sqrt5}{561}<\frac2{25},
   \]
   since \(1{,}250{,}000<1{,}258{,}884\). Insert this exact comparison before using the \(6.2n\) denominator.)**