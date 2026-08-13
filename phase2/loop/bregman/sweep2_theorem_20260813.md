# Prior-art sweep #2 — novelty of the (b)-redundancy THEOREM (gpt-5.6-sol, effort=max, 2026-08-13 02:38)

> Sweep #1 cleared the Part I counterexample. Part II produced a different and
> stronger claim — a strengthening of the published Fact 3.2 — so the Erdosgate
> rule applies to it independently.

# Verdict: **RED**

The substantive theorem is already in:

**Xian-Fa Luo, Li Meng, Ching-Feng Wen, and Jen-Chih Yao**,  
“**Bregman distances without coercive condition: suns, Chebyshev sets and Klee sets**,”  
*Optimization* **68**(8) (2019), 1599–1624, **Theorem 3.12**,  
DOI: `10.1080/02331934.2019.1625898`  
https://doi.org/10.1080/02331934.2019.1625898 ([openurl.ebsco.com](https://openurl.ebsco.com/results?bquery=AU+Luo%2C+Fa&page=1&sid=ebsco%3Aocu_results%3Acache))

## Why this kills the proposed theorem

The right-projection part of Luo–Meng–Wen–Yao, Theorem 3.12, gives—under their standing Bregman/Legendre hypotheses—for a nonempty closed \(C\subset U\):

- convexity of \(\nabla f(C)\);
- the right-Bregman-sun property;
- and, when \(U=X\), the right-\(D_f\)-Chebyshev property,

as equivalent conditions.

Thus, in the direction relevant here,

\[
U=X,\qquad
\overrightarrow P^f_C(x)
=\arg\min_{y\in C}D_f(x,y)\ \text{singleton for every }x\in X
\quad\Longrightarrow\quad
\nabla f(C)\text{ is convex}.
\]

**Their theorem does not require**
\[
\overline{\nabla f(C)}\subset \operatorname{int}\operatorname{dom}f^*.
\]

You are correct that Luo et al. retain the full-domain condition \(U=X\). But the proposed theorem also retains exactly that condition. Consequently, failure to settle the separate “remove full domain” problem does not save the proposed result: **Theorem 3.12 already removes the dual-closure hypothesis that your theorem removes.**

The 2009 source theorem and the 2010/2011 survey did require
\(\overline{\nabla f(C)}\subset U^*\), and the survey explicitly listed the necessity of full domain and dual closure as open. ([citeseerx.ist.psu.edu](https://citeseerx.ist.psu.edu/document?doi=54ed893b724abdc4885c5123c3652112a3fdc0de&repid=rep1&type=pdf))

---

## The “arbitrary \(C\)” addition does not restore novelty

Luo et al. formulate their theorem for a nonempty closed set. But your projection assumption itself forces those two properties.

### Nonemptiness

If \(\arg\min_{y\in C}D_f(x,y)\) is a singleton for even one \(x\), then it is nonempty, hence \(C\neq\varnothing\).

### Closedness

Suppose \(c_k\in C\) and \(c_k\to c\in X\). Because \(f\) is full-domain Legendre, \(f\) and \(\nabla f\) are continuous on \(X\), so

\[
D_f(c,c_k)
=f(c)-f(c_k)-\langle\nabla f(c_k),c-c_k\rangle
\longrightarrow 0.
\]

Hence
\[
\inf_{y\in C}D_f(c,y)=0.
\]

By the assumed attainment, some \(y\in C\) attains this infimum. For a Legendre function,

\[
D_f(c,y)=0\iff c=y.
\]

Therefore \(c=y\in C\), proving that \(C\) is closed.

In fact, **uniqueness is not needed for closedness; global attainment alone suffices**.

This argument is also the right/full-domain counterpart of **Lemma 7.2** in Bauschke–Wang–Ye–Yuan, which proves an analogous automatic-closedness statement for left Bregman projections when the relevant closure stays inside the Legendre domain. ([citeseerx.ist.psu.edu](https://citeseerx.ist.psu.edu/document?doi=54ed893b724abdc4885c5123c3652112a3fdc0de&repid=rep1&type=pdf))

Consequently, your proposed theorem is the immediate chain

\[
\text{singleton right projections}
\Longrightarrow C\neq\varnothing,\ C\text{ closed}
\overset{\text{Luo et al., Thm.\ 3.12}}{\Longrightarrow}
\nabla f(C)\text{ convex}.
\]

The automatic nonempty/closed wrapper is elementary and does not make the convexity theorem new.

---

# Works examined

## 1. Original theorem and survey

### Bauschke–Wang–Ye–Yuan, 2009

**Heinz H. Bauschke, Xianfu Wang, Jane J. Ye, Xiaoming Yuan**,  
“**Bregman distances and Chebyshev sets**,”  
*Journal of Approximation Theory* **159**(1) (2009), 3–25.  
DOI: `10.1016/j.jat.2008.08.014`  
arXiv:0712.4030  
https://arxiv.org/abs/0712.4030

- Theorem 7.3 is the source of the old right-projection result.
- It assumes full domain, closed \(C\), and
  \(\overline{\nabla f(C)}\subset\operatorname{int}\operatorname{dom}f^*\).
- Lemma 7.2 already records the basic “attainment forces closedness” mechanism, in the left-projection orientation. ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0021904508001652))

### Bauschke–Macklem–Wang, 2010/2011

**Heinz H. Bauschke, Mason S. Macklem, Xianfu Wang**,  
“**Chebyshev Sets, Klee Sets, and Chebyshev Centers with respect to Bregman Distances: Recent Results and Open Problems**,”  
in *Fixed-Point Algorithms for Inverse Problems in Science and Engineering*, Springer, 2011, pp. 1–21.  
arXiv:1003.3127  
https://arxiv.org/abs/1003.3127

- Fact 3.2 repeats the 2009 theorem.
- Problem 2 asks whether full domain and dual closure are essential.
- Luo et al. later remove the dual-closure condition while retaining full domain. ([arxiv.org](https://arxiv.org/pdf/1003.3127))

## 2. Exact killer

### Luo–Meng–Wen–Yao, 2019

Citation above.

- Theorem 3.12 gives the right-Chebyshev/right-sun/\(\nabla f(C)\)-convex equivalence when \(U=X\).
- No ambient dual-closure hypothesis is imposed.
- It therefore contains the nontrivial part of the proposed theorem already.

This is the reference that must be cited prominently, not merely mentioned as work that removed a coercivity condition.

## 3. Closely adjacent Bregman-Chebyshev literature

### Li–Song–Yao, 2010

**Chong Li, Wen Song, Jen-Chih Yao**,  
“**The Bregman distance, approximate compactness and convexity of Chebyshev sets in Banach spaces**,”  
*Journal of Approximation Theory* **162**(6) (2010), 1128–1149.

This treats Banach-space Bregman Chebyshev convexity using approximate-compactness hypotheses. It is important background, but it is not the clean removal of the right-projection dual-closure hypothesis. ([dialnet.unirioja.es](https://dialnet.unirioja.es/ejemplar/245170))

### Bauschke–Macklem–Sewell–Wang, 2010

**Heinz H. Bauschke, Mason S. Macklem, Jason B. Sewell, Xianfu Wang**,  
“**Klee sets and Chebyshev centers for the right Bregman distance**,”  
*Journal of Approximation Theory* **162**(6) (2010), 1225–1244.  
DOI: `10.1016/j.jat.2010.01.001`  
arXiv:0908.2013  
https://arxiv.org/abs/0908.2013

This concerns farthest-point/Klee sets and centers, not the nearest-point dual-closure issue. ([arxiv.org](https://arxiv.org/abs/0908.2013))

### Kan–Song, 2012

**Kan and Song**,  
“**The Moreau envelope function and proximal mapping in the sense of the Bregman distance**,” 2012.

This studies single-valuedness and its relationship with convexity of a regularized function. Its framework uses proper lower-semicontinuous functions; after dualization, taking the indicator of \(S=\nabla f(C)\) generally reintroduces precisely the ambient closedness difficulty. It is adjacent but not the clean target result. ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0362546X11005062))

### Bauschke–Dao–Lindstrom, 2018

**Heinz H. Bauschke, Minh N. Dao, Scott B. Lindstrom**,  
“**Regularizing with Bregman–Moreau envelopes**,”  
*SIAM Journal on Optimization* **28**(4) (2018), 3208–3228.  
arXiv:1705.06019  
https://arxiv.org/abs/1705.06019

This develops left and right Bregman envelopes primarily for proper lower-semicontinuous convex inputs. It does not supply a separate arbitrary-set removal of the dual-closure condition. ([arxiv.org](https://arxiv.org/abs/1705.06019))

## 4. Laude–Ochs–Cremers, 2020

**Emanuel Laude, Peter Ochs, Daniel Cremers**,  
“**Bregman Proximal Mappings and Bregman–Moreau Envelopes under Relative Prox-Regularity**,”  
*Journal of Optimization Theory and Applications* **184** (2020), 724–761.  
arXiv:1907.04306  
https://arxiv.org/abs/1907.04306

- It studies **local** single-valuedness for nonconvex, relatively prox-regular functions.
- Its introduction says that, for indicators of closed sets in finite dimensions, global single-valuedness is equivalent to convexity, citing the 2009 Bauschke et al. paper.
- That introductory sentence suppresses orientation and technical hypotheses; it is not an independent proof of the missing right dual-boundary case.
- Nevertheless, it must be discussed because of its left/right translation machinery and nonconvex-domain framework. ([mop.uni-saarland.de](https://www.mop.uni-saarland.de/pub/LOC20/BregProxReg_arXiv.pdf))

## 5. Themelis–Wang, 2025

**A. Themelis and X. Wang**,  
“**On the natural domain of Bregman operators**,”  
arXiv:2506.00465 (2025).  
https://arxiv.org/abs/2506.00465

This is the most relevant recent adjacent work:

- it explicitly treats natural-domain restrictions;
- develops a direct treatment of right Bregman proximal mappings rather than only converting them into left operators;
- and introduces an epi-composite representation conceptually close to your use of a closure/hull of \(f^*+\iota_S\).

I found no separately stated theorem there saying that global right-Chebyshevness makes \(\overline{\nabla f(C)}\subset U^*\) redundant. But once Luo et al. is taken into account, such a theorem would no longer be new anyway. ([alphaxiv.org](https://www.alphaxiv.org/abs/2506.00465))

## 6. Noll-hosted work on alternating Bregman projections

The manuscript **“Alternating Bregman Projections and Convergence of the EM Algorithm”**, hosted on Dominikus Noll’s Toulouse page, still refers to Bauschke–Wang–Ye–Yuan, Theorem 7.3, when discussing the implication from right Bregman Chebyshevness to convexity of \(\nabla f(A)\). It does not present a new proof of dual-closure redundancy.  
https://www.math.univ-toulouse.fr/~noll/PAPERS/bregman.pdf ([math.univ-toulouse.fr](https://www.math.univ-toulouse.fr/~noll/PAPERS/bregman.pdf))

## 7. Other named collaborator searches

I searched combinations of the relevant terms with **Bauschke, Macklem, Wang, Borwein, Combettes, Noll, Lucet, Moffat, Bolte,** and **Teboulle**. The Bauschke publication list and related searches turned up later work on Bregman envelopes, proximal averages, circumcenters, and nonconvex algorithms, but no later theorem more directly on point than Luo et al. ([bauschke.ca](https://bauschke.ca/publications))

---

# Is the supporting-normal perturbation a named technique?

I found **no standard unique name for exactly your boundary-normal step**. A referee is likely to recognize it as a combination of:

1. a **supporting-hyperplane or normal-cone tilt**;
2. a **linear perturbation/exposed-point argument**; and
3. comparison with the **closed convexification/lower-semicontinuous hull**.

The closest explicitly named framework I found is:

- **J.-B. Hiriart-Urruty, M. López, M. Volle**,  
  “**The epsilon strategy in variational analysis: illustration with the closed convexification of a function**,”  
  *Revista Matemática Iberoamericana* **27** (2011), no. 2;

together with:

- **J. Benoist and J.-B. Hiriart-Urruty**,  
  “**What is the subdifferential of the closed convex hull of a function?**,”  
  *SIAM Journal on Mathematical Analysis* **27**(6) (1996), 1661–1697. ([math.univ-toulouse.fr](https://www.math.univ-toulouse.fr/~jbhu/Volle-JBHU-NA-TMA.pdf))

I would describe your step as a **supporting-normal tilt at a boundary ghost**, not advertise it as an entirely new general technique. The potentially new contribution could be a particularly short application of that device to reprove Luo et al.’s right-Chebyshev implication.

A further item flagged for manual inspection is **M. Volle and J.-B. Hiriart-Urruty, “A characterization of essentially strictly convex …”**, whose indexed text cites the BMW survey and the closed-convexification literature. I could not verify its precise theorem or final bibliographic metadata during this run:
https://www.math.univ-toulouse.fr/~jbhu/Volle-JBHU-NA-TMA.pdf

---

# Search coverage and limitations

## Representative exact searches

I searched, among others:

- `"Fact 3.2" "right D_f-Chebyshev"`
- `"cl C*" "right" Chebyshev Bregman`
- `"right Bregman Chebyshev" closure convex`
- `"right D-Chebyshev" convex "full domain"`
- `"Theorem 3.12" "Bregman distances without coercive condition"`
- `"Bregman distances without coercive condition" citations`
- `arXiv 2506.00465 Chebyshev`
- `arXiv 1907.04306 Bregman`
- exact searches for the 2009, 2019, 2020, and 2025 titles
- author-name combinations for the collaborators listed in the question.

## Sources searched

- arXiv and arXiv full text;
- publisher/index pages for Elsevier, Springer and Taylor & Francis;
- CiteSeerX copies;
- alphaXiv indexed full text;
- author publication pages;
- ordinary web citation/reference searches;
- recent overview manuscripts through **August 13, 2026**.

## What I could not fully check

- Taylor & Francis blocked direct full-text retrieval of the 2019 Luo et al. article in this tool. The decisive item to verify in your own copy is the right-hand equivalence in **Theorem 3.12** and the absence of any \(\overline{\nabla f(C)}\subset U^*\) hypothesis.
- I did not have authenticated access to MathSciNet, zbMATH, Scopus, or Web of Science.
- I could not obtain a reliable exhaustive Google Scholar “cited by” export for Luo et al.
- Some 2025–2026 manuscripts were available only through partially indexed PDFs.
- I therefore cannot claim exhaustive coverage of every thesis or paywalled article. This limitation does **not** affect the RED conclusion because the 2019 theorem itself is the prior art.

# Recommendation

Do **not** claim the displayed theorem as new. At most, frame the result as:

- an explicit observation that right-Chebyshev attainment automatically forces \(C\) to be nonempty and closed; and
- a new, possibly shorter supporting-normal proof of the finite-dimensional specialization of **Luo–Meng–Wen–Yao, Theorem 3.12**.

A genuinely new theorem would need to go beyond Luo et al.—for example by removing \(U=X\), weakening their standing kernel assumptions in a nonautomatic way, or proving an infinite-dimensional boundary-ghost result.