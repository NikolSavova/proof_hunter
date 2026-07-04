# Theory/prior-art probe: scaled-search findings — gpt-5.5 + web, high effort

## Bottom line

**I found no literature contradicting F1, F2, or F3.** More importantly, I found **no published statement of F1’s “global tightness is attained by \([e,w_0]\)” phenomenon**, and no published **equality classification** like F3. The surrounding results are real and important, but they stop well short of your claims.

Your likely referee-facing positioning should be:

- **F1:** apparently **new empirical/conjectural phenomenon**; not implied by Björner–Ekedahl.
- **F2:** **log-concavity of Mahonian numbers is known**; the normal/variance heuristic is standard/probabilistically natural; but I did **not** find a paper explicitly formulating the **central log-concavity ratio** as \(1+\Theta(m^{-3})\) for \([m]_q!\). If you make it rigorous, cite log-concavity + local CLT/Edgeworth literature and present the ratio estimate as your derivation.
- **F3:** the dihedral source of equality is elementary/folklore, but the **“only these equality cases occur in Weyl Bruhat intervals”** statement appears **not published**.

---

# 1. F1 and Björner–Ekedahl: what is known, and what is not

## Confirmed facts

**Brenti’s conjecture itself is stated as open in the exact form you use:** for a Weyl group \(W\) and \(u\le v\), the Bruhat interval \([u,v]\) should be rank log-concave. Brenti’s recent OPAC/open-problems paper states Conjecture 2.11 and records previous verification only for \(A_n,n\le5\), \(D_n,n\le5\), \(B_n,n\le4\), \(B_5\) with \(\ell(u,v)\ge20\), \(F_4\), and dihedral groups; it also gives an \(H_3\) counterexample showing the statement fails for arbitrary finite Coxeter groups. ([samuelfhopkins.com](https://www.samuelfhopkins.com/OPAC/files/proceedings/brenti.pdf))

**Björner–Ekedahl prove “top-heaviness”/shape inequalities for lower parabolic Bruhat intervals, not log-concavity and not a tightness comparison.** In their notation \(f_i^{w,J}\) counts elements of length \(i\) below \(w\) in \(W^J\). Their headline theorem is that \(f_i^{w,J}\le f_j^{w,J}\) whenever \(0\le i<j\le \ell(w)-i\). They also characterize certain initial/final equalities via Kazhdan–Lusztig polynomial coefficients, prove finite-group growth restrictions, and prove eventual top-end decreasing inequalities for sufficiently long \(w\). ([annals.math.princeton.edu](https://annals.math.princeton.edu/2009/170-2/p09?utm_source=openai))

**Björner–Ekedahl’s results are about lower intervals \([e,w]\) or parabolic lower intervals, not arbitrary intervals \([u,v]\).** Their abstract and setup are explicitly for \(w\in W^J\) and elements below \(w\) in \(W^J\), i.e. parabolic Schubert-variety rank sequences. ([arxiv.org](https://arxiv.org/abs/math/0508022)) This matters because F1 is a statement over **all** Bruhat intervals.

**Their results do not imply F1.** Top-heaviness/unimodality-type inequalities constrain the broad shape of \([e,w]\), but they do not compare the local ratios  
\[
\frac{a_k^2}{a_{k-1}a_{k+1}}
\]
for proper intervals against the central ratio of \([e,w_0]\). They also do not assert log-concavity in general.

**There is a known warning that parabolic analogues can fail.** The recent Burrull–Gui–Hu paper on asymptotic log-concavity of dominant lower Bruhat intervals recalls Brenti’s conjecture, says the parabolic analogue does not hold in general, and cites Stanton’s non-unimodal Grassmannian/Young-lattice example. ([researchgate.net](https://www.researchgate.net/publication/376271151_ASYMPTOTIC_LOG-CONCAVITY_OF_DOMINANT_LOWER_BRUHAT_INTERVALS_VIA_THE_BRUNN-MINKOWSKI_INEQUALITY?utm_source=openai))

## What I did **not** find

I found **no published theorem, conjecture, MathOverflow answer, arXiv preprint, or citation-trail statement** saying anything like:

\[
\min_{[u,v]\subseteq W}\min_k \frac{a_k^2}{a_{k-1}a_{k+1}}
=
\min_k \frac{b_k^2}{b_{k-1}b_{k+1}},
\]
where \(b_k\) are the coefficients of the full Poincaré polynomial \(P_W(q)\).

I also found **no published comparison of “log-concavity tightness” of proper Bruhat intervals versus the full Weyl group** in simply-laced types.

## Assessment of F1

**Status:** apparently **new** as a computational observation/conjectural structural phenomenon.

**Not contradicted:** I found no counterexample or statement in the literature contradicting F1.

**Not implied by Björner–Ekedahl:** Their work is essential background on rank shapes of Bruhat intervals, but it does **not** prove, suggest, or refute F1.

---

# 2. F2: Mahonian numbers, \([m]_q!\), log-concavity, and the \(1+\Theta(m^{-3})\) ratio

Let
\[
[m]_q! = \prod_{i=1}^{m}(1+q+\cdots+q^{i-1})
\]
and let \(M_m(k)\) be the coefficient of \(q^k\), i.e. the number of permutations in \(S_m\) with \(k\) inversions.

## Confirmed published log-concavity

**The coefficient sequence of \([m]_q!\) is log-concave.** This follows immediately from closure of log-concavity under convolution/products: each factor \(1+q+\cdots+q^{i-1}\) has a log-concave coefficient sequence, and the product of log-concave polynomials with nonnegative coefficients and no internal zeros is log-concave. Hoggar’s 1974 paper is a standard source for multiplicative/convolution preservation; Kook’s 2006 note gives an elementary proof and states the product theorem explicitly. ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/0095895674900719?utm_source=openai))

**Bóna gave a direct combinatorial proof for Mahonian log-concavity.** The Electronic Journal of Combinatorics paper states: for fixed \(n\), the sequence \(i(n,k)\) of numbers of permutations of length \(n\) with \(k\) inversions is log-concave. ([combinatorics.org](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v11i2n2?utm_source=openai)) The paper also records the classical generating function
\[
\sum_k i(n,k)x^k=(1+x)(1+x+x^2)\cdots(1+x+\cdots+x^{n-1}).
\]
([combinatorics.org](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v11i2n2/pdf?utm_source=openai))

## q-log-concavity literature you should cite, but distinguish carefully

The Butler–Sagan–Su line is mostly about **q-log-concavity of families indexed by \(k\)**, especially Gaussian polynomials and related triangles, not the coefficientwise log-concavity of a single \([m]_q!\).

- Butler proved q-log-concavity of Gaussian binomial coefficients \(\binom{n}{k}_q\) as a sequence in \(k\). ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/009731659090005H?utm_source=openai))  
- Sagan gave inductive proofs of q-log-concavity for Gaussian polynomials and q-Stirling numbers. ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/0012365X9290377R?utm_source=openai))  
- Su–Wang–Yeh addressed strong q-log-concavity questions for multinomial coefficients and symmetric functions, unifying several known q-binomial/q-Stirling results. ([combinatorics.org](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v18i1p73?utm_source=openai))  

These are important background, but do **not** by themselves state your F2 ratio estimate for Mahonian coefficients.

## Asymptotics and the \(1+\Theta(m^{-3})\) central ratio

The probabilistic model is standard: the inversion number of a uniform random permutation in \(S_m\) has the same distribution as a sum of independent discrete uniforms
\[
X_m=\sum_{j=1}^{m} U_j,\qquad U_j\sim \mathrm{Unif}\{0,1,\ldots,j-1\}.
\]
Hence
\[
\sigma_m^2=\mathrm{Var}(X_m)=\sum_{j=1}^{m}\frac{j^2-1}{12}
=\frac{m(m-1)(2m+5)}{72}
\sim \frac{m^3}{36}.
\]

Canfield–Janson–Zeilberger prove asymptotic normality for the Mahonian distribution on words/q-multinomials and discuss a local limit theorem; they explicitly note that the local limit theorem yields log-concavity of q-multinomial coefficients near the center. ([arxiv.org](https://arxiv.org/abs/0908.2089?utm_source=openai))

Your heuristic
\[
r_{\mathrm{central}}\approx \exp(1/\sigma_m^2)
=1+\frac{1}{\sigma_m^2}+O(\sigma_m^{-4})
=1+\frac{36}{m^3}+O(m^{-4})
\]
is exactly what the local Gaussian model predicts.

## What I did **not** find

I did **not** find a published paper that explicitly states, for Mahonian numbers,
\[
\min_k \frac{M_m(k)^2}{M_m(k-1)M_m(k+1)}
=1+\Theta(m^{-3}),
\]
or that identifies the central ratio with asymptotic \(1+36/m^3+o(m^{-3})\).

So: **the ingredients are published**, but the specific “log-concavity tightness ratio” formulation appears not to be standard.

## Assessment of F2

- **Known:** Mahonian log-concavity; product/convolution proof; Bóna’s direct proof.
- **Known background:** CLT/local-CLT asymptotics for inversion/Mahonian distributions.
- **Apparently not explicitly published:** the central log-concavity ratio asymptotic \(1+\Theta(m^{-3})\), especially as an explanation for the full-group minima in type \(A\).

If you present F2 as a theorem, referees will expect you to prove the ratio estimate from a local CLT/Edgeworth expansion or cite a precise local expansion. If you present it as a heuristic/explanation, cite Bóna, Hoggar/Kook, and Canfield–Janson–Zeilberger.

---

# 3. F3: equality \(r=1\) from dihedral patterns

## Confirmed facts

In a finite dihedral Coxeter group \(I_2(m)\), the full interval has rank sequence
\[
(1,2,2,\ldots,2,1),
\]
with \(m-1\) copies of \(2\) in the middle. For \(m\ge4\), this gives equality
\[
2^2=2\cdot 2
\]
at interior plateau positions, hence log-concavity ratio \(1\). In Weyl rank two, the relevant non-simply-laced cases are \(B_2\) with \(m=4\) and \(G_2\) with \(m=6\). Thus the rank pattern
\[
(1,2,2,2,1)
\]
is the minimal dihedral equality witness.

Brenti’s OPAC/open-problems paper records that Conjecture 2.11 has been verified for dihedral groups, but I found no equality classification there. ([samuelfhopkins.com](https://www.samuelfhopkins.com/OPAC/files/proceedings/brenti.pdf))

## What I did **not** find

I found **no published characterization** saying that equality \(a_k^2=a_{k-1}a_{k+1}\) in Weyl-group Bruhat intervals occurs only through such non-simply-laced dihedral/parabolic patterns.

I also found no follow-up to Brenti’s conjecture that classifies equality cases for rank log-concavity of Bruhat intervals.

## Assessment of F3

- **Folklore/elementary:** dihedral intervals \(I_2(m)\), \(m\ge4\), give equality \(r=1\).
- **Apparently new:** the global Weyl-group equality characterization “only these patterns occur,” if you can state it precisely and verify/prove it.
- **Not contradicted:** I found nothing contradicting F3.

One caution: if your statement quantifies over all intervals including full rank-two groups, then \(G_2\) gives \((1,2,2,2,2,2,1)\), not only \((1,2,2,2,1)\). If your empirical statement is specifically about **proper intervals inside larger non-simply-laced Weyl groups**, then the \((1,2,2,2,1)\) wording is plausible; otherwise state the dihedral family as \((1,2,\ldots,2,1)\) with \(m\ge4\).

---

# 4. What referees will likely consider new vs known

## Likely already known / must cite

1. **The conjecture and previously verified finite cases.** Cite Brenti’s Conjecture 2.11 and his verification list. ([samuelfhopkins.com](https://www.samuelfhopkins.com/OPAC/files/proceedings/brenti.pdf))  
2. **Björner–Ekedahl top-heavy/lower-interval shape results.** Cite them for rank inequalities of lower/parabolic Bruhat intervals, equality via KL-polynomial coefficients, and finite-group growth restrictions. ([annals.math.princeton.edu](https://annals.math.princeton.edu/2009/170-2/p09?utm_source=openai))  
3. **Mahonian log-concavity.** Cite Hoggar/Kook for product preservation and Bóna for the direct combinatorial proof. ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/0095895674900719?utm_source=openai))  
4. **q-log-concavity background.** Cite Butler, Sagan, and Su–Wang–Yeh if you discuss q-log-concavity or strong q-log-concavity. ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/009731659090005H?utm_source=openai))  
5. **Asymptotic normal/local-limit viewpoint.** Cite Canfield–Janson–Zeilberger for Mahonian/q-multinomial asymptotics. ([arxiv.org](https://arxiv.org/abs/0908.2089?utm_source=openai))  
6. **Parabolic cautionary examples.** Cite Burrull–Gui–Hu/Stanton if you mention that parabolic analogues can fail or that parabolic lower intervals need not be log-concave. ([researchgate.net](https://www.researchgate.net/publication/376271151_ASYMPTOTIC_LOG-CONCAVITY_OF_DOMINANT_LOWER_BRUHAT_INTERVALS_VIA_THE_BRUNN-MINKOWSKI_INEQUALITY?utm_source=openai))  

## Likely new in your note

1. **New exhaustive verification cases.** Based on Brenti’s stated list, full/near-full verification in \(A_6,A_7\), \(D_6,D_7\), \(E_6\), and beyond the previously recorded \(B_5\)/\(B_6\) ranges should be new, provided your enumeration protocols are clear. Brenti’s list already includes \(F_4\), all dihedral groups, \(A_n,D_n\le5\), \(B_n\le4\), and partial \(B_5\). ([samuelfhopkins.com](https://www.samuelfhopkins.com/OPAC/files/proceedings/brenti.pdf))  
2. **F1 tightness/minimum-at-\([e,w_0]\).** I found no precedent. Treat as a new computational theorem for your checked types and perhaps a conjecture for all simply-laced Weyl groups.  
3. **F2 ratio-asymptotic formulation.** Log-concavity is known, and normal approximation is known, but the specific central ratio/tightness statement appears new or at least unstated.  
4. **F3 equality characterization.** The dihedral examples are elementary, but a systematic equality classification across finite Weyl Bruhat intervals appears new.

## Suggested wording for the paper

You might write something like:

> The log-concavity of the Mahonian distribution is classical, following for example from closure of log-concavity under products, and also admits a direct combinatorial proof by Bóna. What appears not to have been recorded is the relevance of its **central log-concavity ratio** as the extremal obstruction in simply-laced Bruhat intervals.

And for F1:

> Björner and Ekedahl prove strong top-heaviness results for lower parabolic Bruhat intervals, but their inequalities do not compare local log-concavity ratios across intervals. Our computations suggest a different extremal principle: in simply-laced finite Weyl groups, the smallest log-concavity ratio over all intervals is already attained by the full interval \([e,w_0]\).

And for F3:

> In non-simply-laced types, equality \(r=1\) is forced by rank-two dihedral parabolics of braid order at least four. Our computations suggest that these are the only equality mechanisms.

---

## Final answer to “if you find nothing contradicting”

I found **nothing contradicting F1, F2, or F3**. I also found **no published source that already states F1 or F3**. For F2, the **underlying Mahonian log-concavity and asymptotic normality are known**, but the **specific \(1+\Theta(m^{-3})\) log-concavity-ratio interpretation** appears not to be explicitly recorded in the sources I found.

---
usage: ResponseUsage(input_tokens=114698, input_tokens_details=InputTokensDetails(cached_tokens=4224), output_tokens=9047, output_tokens_details=OutputTokensDetails(reasoning_tokens=5182), total_tokens=123745)
