# maths referee (gpt-5.6-sol, effort=max) — sol_s3w7sign_20260812.md — 2026-08-12 19:45

> Cross-model referee report (Sol on the reviewed draft). Numeric checks are
> DERIVED, not executed — script them before trusting.

### Hand audit

- **SOL.1:** Correct.  
  \(F'''(t)=t\sinh t\), and
  \[
  3\!\left(\coth y-\frac1y\right)-\tanh y
  =\frac{F(2y)}{y\sinh(2y)}.
  \]
  Hence the claimed strict positivity follows.

- **SOL.2:** Correct on the operative scope \(m\ge2\).  
  The logarithmic derivative
  \[
  \frac{d}{dy}\log h_3(2y)
  =-\left[3\left(\coth y-\frac1y\right)-\tanh y\right]
  \]
  is negative, so \(h_3\) is strictly decreasing and \(B>0\) for \(m\ge2\). The repaired squaring step is then valid provided \(A>0\).

- **SOL.3, analytic algebra only:** The corrected Euler–Maclaurin constant is right. Omitting the \(B_8\) endpoint term gives, up to an irrelevant sign,
  \[
  E_{n,8}
  =\frac{\lambda^8}{8!}\int_0^w
    \bigl(B_8(\{x/\lambda\})-B_8\bigr)h_n^{(8)}(x)\,dx.
  \]
  The extrema of \(B_8\) give
  \[
  \sup|B_8(u)-B_8|=\frac{17}{256},
  \qquad
  K_{\rm EM}=\frac{17}{10321920},
  \]
  and the ratio to the old constant is indeed \(255/128\).

- **SOL.4:** The new W7 argument checks out. In particular:
  - the hyperbolic formulas are correct;
  - the bounds \(h_2>.93\), \(h_4>5\), and \(h_2>.99\) on the stated ranges have the displayed positive rational margins;
  - the coefficient argument proving \(h_4<7\) is valid;
  - the right-Riemann estimate gives \(\lambda\sum h_2(j\lambda)<10/3\);
  - the \(h_4\)-tail argument gives \(K_4<129\);
  - consequently
    \[
    \lambda A>cw-\frac{10}{3},\quad
    0\le\lambda B\le2w,\quad
    \frac CA>5-\frac{129}{w}.
    \]
  The derivative \(U_c'(w)<0\) is correct. The edge split has no gap: \(\lambda=1/10\) is in the first case, while \(\lambda>1/10\) and \(m\ge561\) imply \(w>561/10\). The exact evaluations
  \[
  U_{99/100}(40)=4-\frac{499}{23120}<4
  \]
  and
  \[
  2001(146519)^2-374(336600)^2
  =583067099361>0
  \]
  are correct. Thus the analytic W7 conclusion \(J<4<4.59597\) survives.

- **SOL.5:** Correct. The three hyperbolic expressions have even analytic extensions at zero, so their seventh derivatives vanish there. The termwise derivative estimate at infinity is valid, and the leading \(k=1\) term gives
  \[
  e^x h_n^{(7)}(x)/x^n\to-1.
  \]

The draft therefore repairs the **analytic W7 sign argument**, but it does not presently prove the full S3 statement.

VERDICT: MAJOR_ISSUES

1. **(Lemma SOL.3, final paragraph; Theorem SOL.6, opening hypothesis, “the established exact-arithmetic compact-band certificate … proves W1–W6b”)** — This is the entire S3 conclusion on W1–W6b, merely asserted and then assumed. No checker, output, exact cell inequalities, hashes, rational enclosure table, or cited artifact is supplied. The verification recipe is prospective (“must report”), not evidence that a corrected run occurred. Because \(17/10321920\) is \(255/128\) times the old coefficient, an earlier run using \(1/1209600\) cannot be inherited without an actual rerun. As written, SOL.6 proves only “W1–W6b S3 plus SOL.4 implies all-band S3.”

2. **(Lemma SOL.3, “the certified bound \(|h_n^{(8)}(x)|\le10^{12}\)”)** — This load-bearing continuum bound is also unsupported. No analytic derivation or interval certificate is given. A sampled grid would not certify the supremum. The exact method and output establishing the bound simultaneously for \(n=2,3,4\) on \(x\in[0,40]\) must be supplied.

3. **(Lemma SOL.3 and Theorem SOL.6, compact-certificate scope \(m\ge561\))** — Partitioning \(w\) into cells of width \(1/128\) does not by itself cover the second parameter \(m\), or equivalently \(\lambda=w/m\). The Euler–Maclaurin terms and remainder depend on \(\lambda\). The draft gives no monotonicity argument showing that \(m=561\) is worst, nor an interval variable covering \(1/m\in[0,1/561]\). Thus even a zero-failure \(w\)-cell run at \(m=561\) would not establish the advertised all-\(m\) scope.

4. **(Theorem SOL.6, “\(J\le J_0(W)\) on every band W1–W7”)** — W1–W6b, their exact \(J_0\) rationals, and their open/closed boundary conventions are not stated or cited. Consequently the claimed interface cannot be compared with the composition note’s exact S3 hypothesis. In particular, the draft does not document coverage at \(w=4\), every internal band edge, or the W6b/W7 edge \(w=40\). The analytic W7 lemma itself includes \(w=40\), but the assembled interface remains undefined.

5. **(Opening setup and corrected \((\mathrm{SOL}.12')\), “Thus \(A>0\)” without an \(m\)-restriction)** — False for \(m=1\): then \(A=B=C=0\), so \(r_{31},r_{42}\), and the displayed divisions by \(A\) are undefined. Strict decrease of \(h_2\) gives \(A>0\) only for \(m\ge2\). This does not damage the \(m\ge561\) theorem but requires a scope correction.

6. **(WHAT REMAINS, item 1, “For (S3): no mathematical gap remains”)** — This overstates the result. Until Issues 1–4 are discharged by an auditable corrected certificate with the exact composition interface, only the W7 component has been proved; S3 remains open.