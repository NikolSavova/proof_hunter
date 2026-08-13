# maths referee (gpt-5.6-sol) — sol_s3_20260812.md — 2026-08-12 17:44

> Cross-model referee report (Sol on the reviewed draft). Numeric checks are
> DERIVED, not executed — script them before trusting.

### Hand recomputation

- **SOL.1:** The cumulant identity is correct. For \(f(x)=\log(1-e^{-x})\),
  \[
  (-1)^n\frac{d^n}{d\lambda^n}\bigl(f(j\lambda)-f(\lambda)\bigr)
  =\phi_n(\lambda)-j^n\phi_n(j\lambda),
  \]
  so the formulas for \(F_n,r_{31},r_{42}\), and \(J\) follow.

- **SOL.2, before Euler–Maclaurin:** The identity for \(G_n\), including
  \[
  \int_0^\infty h_n(x)\,dx=n!\zeta(2)
  \]
  and the polynomials \(P_n\), is correct.

- **SOL.2, Euler–Maclaurin:** The displayed endpoint terms through \(B_6\) have the right coefficients and signs, but the claimed remainder does not follow. This invalidates the enclosures subsequently used in SOL.3.

- **SOL.3:** The box count
  \[
  36\cdot 2048\cdot256=18\,874\,368
  \]
  is correct, and enlarging \(z=561/m\) to \([0,1]\) is harmless. But none of the asserted interval comparisons has actually been produced, and they use the invalid SOL.2 remainder.

- **SOL.4:** The arithmetic
  \[
  \frac1m\le\min\!\left(\frac1{561},\frac{\lambda}{40}\right)
  \]
  and the breakpoint \(L=40/561\) are correct. The passage to \(U_7\), however, silently requires \(B\ge0\), which is neither a consequence of nonnegative summands nor included in the advertised certificate.

- **SOL.5:** Conditional on SOL.3–SOL.4 and the imported exact \(J_0\) floors, all seven final rational comparisons are correct. Band endpoints and the threshold \(m\ge561\) are consistent. Reflection also preserves \(J\).

The theorem is therefore not established: its two load-bearing computational lemmas are unsupported, and the compact-band enclosure is based on an incorrect Euler–Maclaurin remainder.

VERDICT: FATAL

1. **(SOL.2, equations (SOL.3)–(SOL.4), “apply Euler–Maclaurin … through the \(B_6\)-term”), claim:** after retaining endpoint corrections only through \(B_6\), the remainder satisfies
   \[
   |E_{n,8}|\le\frac{\lambda^8}{1209600}\int_0^w|h_n^{(8)}|.
   \]
   **Why wrong:** the standard remainder after truncation through \(B_6\) is controlled at derivative order six, e.g.
   \[
   |R_6|\le \frac{\lambda^6}{30240}\int_0^w|h_n^{(6)}(x)|\,dx.
   \]
   To invoke the \(B_8\)/eighth-derivative remainder with coefficient \(1/1209600\), the \(B_8\) endpoint term must also be included. In \(F_n\) that missing term is
   \[
   +\frac{\lambda^8}{1209600}
     \bigl(h_n^{(7)}(w)-h_n^{(7)}(0)\bigr).
   \]
   It is generally nonzero at finite \(w\). Thus (SOL.3)–(SOL.6) do not enclose the exact \(F_n\), and every SOL.3 box comparison must be recomputed with a valid remainder.

2. **(SOL.3, “The six resulting exact checks are …”; Verification Recipe §4; WHAT REMAINS item 1), claim:** \(18\,874\,368\) exact-rational boxes have already certified the six compact bands.  
   **Why wrong:** no checker, source, output, hashes, maximal interval endpoints, or worst boxes are supplied. The final section expressly says that saving and running the checker still remains. “Expected output” and asserted Boolean tables are not a certificate. Moreover, the proposed checker would implement the invalid remainder from issue 1, so even the advertised run would not prove SOL.3 without mathematical repair and rerunning.

3. **(SOL.2, proof of (SOL.5), and SOL.4 equations (SOL.14)–(SOL.17)), claim:** the derivative bounds, absolute-integral bounds, Taylor enclosures, and final interval inequalities are “certified in exact rational interval arithmetic.”  
   **Why wrong:** these are unsupported computational assertions. The text omits the actual rational intervals, differentiated expressions, Taylor coefficients/remainder formulas, worst cells, and checker output. In particular,
   \[
   |h_n^{(8)}|\le10^{12},\qquad
   \int_0^\infty|h_n^{(8)}|<10^{12},
   \]
   and
   \[
   h_2-dT_2>9/10,\quad h_4-dT_4>49/10,\quad U_7\le12/5
   \]
   are load-bearing lemmas, not reproducible consequences of the prose recipe.

4. **(SOL.4, immediately before (SOL.12), claim \(0\le B\le m h_3\)), claim:** positivity follows in the same way as the surrounding nonnegative-summand estimates.  
   **Why wrong:** from
   \[
   B=m h_3(\lambda)-\sum_{j=1}^m h_3(j\lambda)
   \]
   and nonnegativity one obtains only \(B\le m h_3(\lambda)\), not \(B\ge0\). The upper bound on \(B^2/A^2\) in (SOL.12) requires \(|B|\le m h_3\), for which the asserted \(B\ge0\) is load-bearing. A separate proof—such as monotonicity of \(h_3\), or a certified bound \(h_3-dT_3\ge0\)—is required. Neither appears, and the W7 verification recipe does not check \(T_3\).

5. **(SOL.4, equation (SOL.13), claimed derivation from Euler–Maclaurin), claim:** the same eighth-derivative remainder follows directly while endpoint terms stop at \(B_6\).  
   **Why wrong:** the derivation again omits discussion of the \(B_8\) endpoint term. In this half-line application it may vanish because \(h_n^{(7)}(0)=h_n^{(7)}(\infty)=0\) for \(n=2,3,4\), but that fact must be stated and proved before the eighth-order remainder is legitimate. It does not rescue the finite-interval formula in SOL.2, where \(h_n^{(7)}(w)\) need not vanish.

6. **(SOL.5, Theorem SOL.5, “For the mathematical statement (S3), nothing remains”), claim:** the proof is complete and independent of further work.  
   **Why wrong:** SOL.5 is only a valid final comparison conditional on SOL.3 and SOL.4. SOL.3 uses a false enclosure and has no executed certificate; SOL.4 has an unproved sign hypothesis and likewise no certificate. Repair requires new mathematics in the enclosure, an actual exact checker, archived output, and a complete rerun—not merely process-level refereeing.