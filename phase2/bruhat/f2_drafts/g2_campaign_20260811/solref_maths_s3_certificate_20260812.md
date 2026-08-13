# maths referee (gpt-5.6-sol) — s3_certificate_20260812.md — 2026-08-12 17:48

> Cross-model referee report (Sol on the reviewed draft). Numeric checks are
> DERIVED, not executed — script them before trusting.

### Hand recomputation

- The substitution is correct:
  \[
  z=\frac{561}{m},\qquad \lambda=\frac{wz}{561}=\frac wm.
  \]
  Thus \(m\ge561\) gives \(0<z\le1\). For the six certified bands, \(4\le w\le40\), hence
  \[
  0<\lambda\le \frac{40}{561}\approx0.07130125.
  \]
- The six rectangles cover exactly \(4\le w\le40\): shared endpoints \(5,6,8,10,20\) are harmless because both neighboring certificates include them. The point \(w=40\) is covered by W6b; the unresolved W7 region is \(40<w\le0.89m\).
- The advertised uniform-box count is correct:
  \[
  36\cdot2048\cdot256=18{,}874{,}368.
  \]
  The leaf total is also correct:
  \[
  1310+199+32+15+18+17=1591.
  \]
- The F2 correction arithmetic is correct. Since \(B_8=-1/30\),
  \[
  \frac{(2-2^{-7})|B_8|}{8!}
  =\frac{17}{10321920}
  =\frac{255}{128}\frac1{1209600}.
  \]
  Thus the old constant was understated by \(255/128=1.9921875\), and replacing it by \(2/1209600\) is safe, with only the factor \(256/255\) of extra slack.
- The Cauchy-series summation in §6 is algebraically sound:
  \[
  \sum_{m\ge4}\frac{(2m)!}{(2m-8)!\,6^{2m}}
  =\frac{8!}{2\,6^8}
   \left(\left(1-\frac16\right)^{-9}
        +\left(1+\frac16\right)^{-9}\right)
  \approx0.064929.
  \]
- The F3 implication direction is correct in principle: proving \(J\le J_0^{(5)}\) also proves \(J\le J_0^{(6)}\) if \(J_0^{(5)}\le J_0^{(6)}\) band by band.

These checks do not validate the two computer-assisted certificates themselves.

VERDICT: MAJOR_ISSUES

1. **(§§1–2, “all six bands CERTIFIED”)** The claimed rigorous certificate is not reproducible from the note. No actual Euler–Maclaurin enclosure formulas, interval expression for \(J_{\rm upper}\), global minimum of \(F_2^{\rm lower}\), worst certified box, or checkpoint/root-coverage manifest is given. Leaf counts and a PASS footer do not establish that every leaf satisfies the two load-bearing predicates. The archived script may contain this information, but the mathematical artifact does not expose enough of it for the claimed certificate to be checked lemma by lemma.

2. **(§4.1 and §6, “directed-rounding interval arithmetic is rigorous”)** This is silently assumed, not proved. Precision replication at 30/40/50 digits is a stability test, not a directed-rounding theorem. The note gives no `mpmath` version, backend, operation inventory, or argument that every real and complex transcendental operation used supplies outward-rounded enclosures. This is especially load-bearing in the complex-circle evaluation in §6. Consequently the run does not yet replace the draft’s exact-rational certificate under the stated proof standard.

3. **(§6, “[0,1] — Cauchy coefficient bound”)** The analytic algebra after obtaining \(M_n(6)\) is correct, but the certificate for \(M_n(6)\) is missing. “4000 arc-boxes” does not by itself prove coverage of \(|z|=6\), nor that the rectangular interval evaluations avoid denominator/pole enclosures and bound \(|h_n(z)|\) on every arc. The actual \(M_n(6)\) enclosures are not even reported. Therefore the displayed \(30.4,1360.6,93812.7\) bounds cannot be independently derived from the note.

4. **(§6, “[1,40] — direct Leibniz series”)** The tail proof is absent. The draft does not define the summand, the exponent \(p\), the ratio estimate, or the resulting geometric-tail formula. The runtime assertion \(K\ge2p/x\) is not itself a proof that the omitted tail is bounded by the quantity used in code. For a typical \(k^p e^{-kx}\) term one must explicitly derive
   \[
   \frac{a_{k+1}}{a_k}
   \le e^{p/k-x}\le e^{-x/2},
   \]
   and then account for every polynomial/product-rule term uniformly for \(n=2,3,4\) and \(x\in[1,40]\). Until that calculation is supplied, the claim “(SOL.5) CERTIFIED” is unsupported.

5. **(§1, enlargement to \(z\in[0,1]\))** The original parameter set has \(z>0\), but the interval recursion includes \(z=0\). The note does not prove that the particular normalized \(F_2,F_3,F_4\) Euler–Maclaurin formulas have removable, correctly implemented extensions at \(z=0\), or that the remainder enclosure remains valid there. Analyticity of \(h_n\) at zero is not by itself a proof of continuity of every normalized expression used for \(J\). This endpoint must be justified explicitly or excluded by a limiting argument.

6. **(§3, F3 threshold generation)** The interface with the composition chain is not pinned down. The note says the wave-6 row is “uniformly LARGER” but gives neither that row nor exact bandwise comparisons, and then says to “adopt whichever” row the composition consumes. The composition consumes a fixed exact-rational \(J_0(W)\) interface; a certificate must identify that vector exactly. The six displayed targets plausibly match the wave-5 row, but byte-identical or exact-rational identification is required, not an informal safe-direction statement.

7. **(§3, “Repairs applied”)** The doubled remainder is used only in the new W1–W6b run. The cited source statements (SOL.4), (SOL.6), and (SOL.13) remain unchanged, and the still-unrun W7 argument may invoke those old statements. Downstream use therefore has to cite a formally restated corrected lemma, not merely this prose instruction that the old formulas “must carry” a factor two. Otherwise the composition has two incompatible versions of the remainder bound.

8. **(§4.3 and §5, scope of the result)** This artifact cannot discharge (S3): at \(m=561\), for example, it covers only \(w\le40\), while W7 extends to \(0.89m=499.29\). The note acknowledges this, but its title and repeated “(S3) certificate” language risk interface drift. The proved object, if the numerical issues above are repaired, is only the W1–W6b component of Lemma SOL.3; no consumer may cite it as the full joint-cancellation statement.