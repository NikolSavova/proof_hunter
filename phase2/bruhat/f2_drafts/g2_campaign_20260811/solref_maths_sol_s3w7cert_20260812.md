# maths referee (gpt-5.6-sol, effort=max) — sol_s3w7cert_20260812.md — 2026-08-12 19:47

> Cross-model referee report (Sol on the reviewed draft). Numeric checks are
> DERIVED, not executed — script them before trusting.

### Hand audit

- **SOL.1–SOL.2:** The kernel formulas and cumulant reduction are correct. For  
  \(g_a(u)=\log(1-e^{-au})\),
  \[
  \frac{d^n}{dt^n}g_a(\lambda-t)\big|_{t=0}
  =-a^n\operatorname{Li}_{1-n}(e^{-a\lambda}),
  \]
  giving
  \[
  \lambda^n\kappa_n
  =m h_n(\lambda)-\sum_{j=1}^m h_n(j\lambda)=mH_n.
  \]
  The definitions of \(r_{31},r_{42},J\) then follow without a missing factor or sign.

- **SOL.4:** The Euler–Maclaurin normalization is correct. Absorbing the omitted \(B_8\)-endpoint term into the usual periodic remainder produces the kernel
  \(B_8(\{x/\lambda\})-B_8\). The claimed extremum is true:
  \[
  B_7(t)=t\Bigl(t-\frac12\Bigr)(t-1)
  \left[t^2(1-t)^2+t(1-t)+\frac13\right],
  \]
  so \(B_8\) increases to \(t=\frac12\) and then decreases. Hence
  \[
  \sup_{[0,1]}|B_8(t)-B_8|
  =B_8(1/2)-B_8=\frac{17}{256},
  \]
  and
  \[
  \mathfrak c_8=\frac{17}{256\cdot8!}
  =\frac{17}{10321920}.
  \]

- **SOL.6–SOL.13:** The Bernoulli expansion, mass identities, derivative-tail exponents, and \(h_4\) identity check out. In particular,
  \[
  C_2=114,\qquad C_3=1118,\qquad C_4=10456,
  \]
  and the local-plus-tail bounds imply the stated \(K_n\). The expansion
  \[
  zp(z)+6p(z)^2-6
  =z^2\left(\frac1{120}-\frac z{504}+\frac{z^2}{9600}
  -\frac{z^3}{120960}+\frac{z^4}{6096384}\right)
  \]
  is also correct.

- **SOL.14:** The split at \(\lambda_0=40/561\) is arithmetically correct. At \(\lambda=\lambda_0\), the second-regime endpoint equals the first-regime loss. Recalculation gives approximately
  \[
  L_{2,0}=0.08273658,\quad L_{2,1}=0.072629,
  \]
  \[
  L_{4,0}=0.987755103,\quad L_{4,1}\approx0.1155.
  \]
  Thus \(L_2=L_{2,0}<0.09\) and \(L_4=L_{4,0}<0.99\).

- **SOL.15–SOL.17:** The monotonicity argument is correctly signed. It yields \(B\ge0\), while \(A>0.91\), \(A<1\), and \(C>5.01\). Consequently
  \[
  U_7=\frac2{1-L_2}\approx2.180399,
  \]
  and
  \[
  U_7^2-\frac{6-L_4}{2}\approx2.248016<\frac94.
  \]
  There is no use of (S1), (S2), or (S4), and no bootstrap circularity. SOL.3 and SOL.5 are not used in the W7 argument.

The analytic core therefore works. The remaining defects are formal interface/self-containment defects rather than failed inequalities.

VERDICT: MINOR_REPAIRS

1. **(SOL.17 final paragraph and WHAT REMAINS 1–2, claim: “Hence \(J<J_0(W7)\)” and “No mathematical W7 gap remains,” why wrong):** The exact \(J_0(W7)=p_7/q_7\) consumed by the composition is neither stated nor tied to an archived row. The draft explicitly leaves \(2p_7>9q_7\) unchecked, so its final interface is not yet formally closed. If the archive really contains \(459597/100000\), record that identity and the exact check \(2p_7-9q_7=19194>0\).

2. **(Opening scope, SOL.3, and SOL.17, claim: this is the W7 replacement, why wrong):** The analytic theorem covers only \(40<m\lambda\), while the document does not state whether the boundary \(m\lambda=40\) belongs to W6b or W7 in the composition’s band convention. Either cite the exact W6b closed endpoint or strengthen the statement to \(40\le m\lambda\); the same estimates remain valid at equality.

3. **(SOL.4 proof, claim: the document is self-contained and the Bernoulli extremum is “established,” why wrong):** The load-bearing extremum \(\sup|B_8(t)-B_8|=17/256\) is asserted without proof or citation. Insert the factorization of \(B_7\) given above, or cite the exact prior certificate. Similarly, SOL.12 should cite the standard bound \(\pi<22/7\) used to justify \(484/49>\pi^2\).