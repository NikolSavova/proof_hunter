# Prior-art check: Brenti Conj 2.11 — gpt-5.5 + web, high effort

## Executive summary

**I found no public proof, disproof, or Weyl-group counterexample to Brenti’s Conjecture 2.11 as of July 3, 2026.** The verification frontier you stated matches the published statement in Brenti’s OPAC survey:  
\[
A_n\ (n\le 5),\quad D_n\ (n\le 5),\quad B_n\ (n\le 4),\quad B_5\text{ for }\ell(u,v)\ge 20,\quad F_4,\quad \text{and dihedral groups}.
\]
I also found **no public claim** that \(A_6\), short \(B_5\) intervals, \(B_6\), \(D_6\), or \(E_6\) have been exhaustively verified. The non-crystallographic warning is also exactly as you stated: Brenti gives an explicit \(H_3\) interval whose rank generating polynomial is
\[
1+3t+5t^2+7t^3+10t^4+10t^5+5t^6+t^7,
\]
which fails log-concavity at \(k=3\), since \(7^2=49<5\cdot 10=50\). ([samuelfhopkins.com](https://www.samuelfhopkins.com/OPAC/files/proceedings/brenti.pdf))

---

## 1. STATUS: open / solved / counterexamples?

### Confirmed facts

**Brenti’s Conjecture 2.11 is stated as open in Brenti’s 2024 OPAC proceedings article / arXiv survey.** The relevant passage says: “Let \(W\) be a Weyl group, and \(u,v\in W\). Then \([u,v]\) is rank log-concave,” followed immediately by the finite list of computational verifications and the \(H_3\) counterexample to the corresponding finite-Coxeter-group statement. ([samuelfhopkins.com](https://www.samuelfhopkins.com/OPAC/files/proceedings/brenti.pdf))

**I found no public Weyl-group counterexample.** The only explicit counterexample I found in Brenti’s text is in non-crystallographic type \(H_3\), so it does **not** disprove the Weyl-group conjecture. ([samuelfhopkins.com](https://www.samuelfhopkins.com/OPAC/files/proceedings/brenti.pdf))

**I found no public proof.** Brenti’s own posted “Updates for Some open problems on Coxeter groups and unimodality” lists updates to other conjectures/problems in the same article—Problem 1.1 and Conjectures 1.4, 1.6, 1.7—but says nothing about Conjecture 2.11. This is not a proof of openness, but it is good circumstantial evidence that Brenti was not aware of a resolution when that update was prepared. ([mat.uniroma2.it](https://www.mat.uniroma2.it/~brenti/update.pdf))

### My conclusion

**Status as of mid-2026: still open, publicly.**  
I found **nothing** contradicting your understanding: no proof, no Weyl counterexample, no published exhaustive verification beyond Brenti’s stated frontier.

Caveat: this is a literature/web search conclusion, not a certificate that no private computation or unpublished note exists.

---

## 2. VERIFICATION FRONTIER

### Published / public frontier

Brenti states the following exact verification frontier:

> “The conjecture has been verified if \(W\) is of type \(A_n\) and \(n\le 5\), or \(D_n\) and \(n\le 5\), or \(B_n\) and \(n\le 4\), or \(B_5\) and \(\ell(u,v)\ge 20\), or \(F_4\), and for the dihedral groups.” ([samuelfhopkins.com](https://www.samuelfhopkins.com/OPAC/files/proceedings/brenti.pdf))

So your frontier is **confirmed**:

| Type | Publicly stated verified cases | Notes |
|---|---:|---|
| \(A_n\) | \(n\le 5\) | Type \(A_5\) means \(S_6\). No public \(A_6\) verification found. |
| \(B_n\) | \(n\le 4\) | Complete through \(B_4\). |
| \(B_5\) | only \(\ell(u,v)\ge 20\) | Short intervals \(\ell(u,v)<20\) are **not** stated as verified. |
| \(D_n\) | \(n\le 5\) | No public \(D_6\) verification found. |
| \(F_4\) | complete | Stated verified. |
| Dihedral groups | complete | Brenti says “for the dihedral groups.” |
| \(E_6,E_7,E_8\) | no verification found | No public exhaustive \(E_6\) computation found. |
| \(G_2\) | covered by dihedral | \(G_2\cong I_2(6)\). |
| Non-crystallographic \(H_3\) | counterexample | Not a Weyl-group counterexample. |

### Attribution / “by whom?”

The verification statement is published in **Francesco Brenti’s** OPAC proceedings article, *Some open problems on Coxeter groups and unimodality*, published in *Open Problems in Algebraic Combinatorics*, Proceedings of Symposia in Pure Mathematics 110, and also posted as arXiv:2410.09897. ([art.torvergata.it](https://art.torvergata.it/handle/2108/392404?utm_source=openai))

I did **not** find a separate paper giving full computational details or raw data for the Conjecture 2.11 verifications. Brenti’s acknowledgments say that “some of the computations for the research presented in this paper” used Maple packages for Coxeter systems and posets developed by **Pietro Mongelli** and **John Stembridge**. This is the only public computational attribution I found in the article. ([samuelfhopkins.com](https://www.samuelfhopkins.com/OPAC/files/proceedings/brenti.pdf))

So the most accurate phrasing is:

> The verification frontier is publicly reported by Brenti in the 2024 OPAC proceedings article; some computations in that article used Maple packages by Mongelli and Stembridge. I found no separate verification paper, repository, or dataset for Conjecture 2.11.

### \(H_3\) counterexample

Brenti’s \(H_3\) example is:

- \(W\) of type \(H_3\),
- \(u=s_3\),
- \(v=s_1s_2s_3s_2s_1s_2s_1s_3\),
- Coxeter parameters \(m(s_1,s_2)=5\), \(m(s_2,s_3)=3\),
- rank generating polynomial:
  \[
  1+3t+5t^2+7t^3+10t^4+10t^5+5t^6+t^7.
  \]

This is unimodal but **not** log-concave, because \(7^2<5\cdot 10\). ([samuelfhopkins.com](https://www.samuelfhopkins.com/OPAC/files/proceedings/brenti.pdf))

---

## 3. RECENT WORK, 2024–2026

### Directly relevant: Burrull–Gui–Hu

The main recent paper I found is:

**Gaston Burrull, Tao Gui, Hongsheng Hu, “Asymptotic Log-concavity of Dominant Lower Bruhat Intervals via Brunn–Minkowski Inequality,” arXiv:2311.17980.** It was first submitted November 29, 2023 and revised to v3 on August 2, 2025. The paper studies parabolic lower Bruhat intervals in affine Weyl groups and proves an **asymptotic** log-concavity statement after dilation; the limiting density is log-concave by Brunn–Minkowski. ([arxiv.org](https://arxiv.org/abs/2311.17980))

There is also a FPSAC 2024 extended abstract in *Séminaire Lotharingien de Combinatoire* 91B, Article 94, 12 pp. ([mat.univie.ac.at](https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2024/94.html?utm_source=openai))

Important distinction: this does **not** prove Brenti’s finite-Weyl-group conjecture. It is about affine Weyl groups, dominant lower **parabolic** intervals, and asymptotic behavior under dilation. The authors themselves state Brenti’s conjecture as background and then prove an asymptotic analogue for their setting. ([mat.univie.ac.at](https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2024/94.pdf?utm_source=openai))

Also relevant: the same paper/abstract notes that the parabolic analogue of Brenti’s finite-Weyl conjecture fails; for example, the Betti numbers of the Schubert variety \(X(8,8,4,4)\) in \(\mathrm{Gr}(4,12)\) give a non-unimodal sequence. This is **not** a counterexample to Brenti’s ordinary Bruhat-interval conjecture. ([mat.univie.ac.at](https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2024/94.pdf?utm_source=openai))

### Related but not a resolution: top-heaviness

Björner–Ekedahl’s 2009 Annals paper remains the main structural result on the “shape” of Bruhat intervals: for crystallographic Coxeter groups and parabolic quotients, their rank numbers satisfy a top-heaviness / weak-increase inequality up to the middle. ([annals.math.princeton.edu](https://annals.math.princeton.edu/2009/170-2/p09?utm_source=openai))

I also found a 2023 seminar listing by Tao Gui on “Top-heaviness of lower Bruhat intervals,” saying that Björner–Ekedahl’s top-heaviness can be proved for general Coxeter groups using Soergel bimodules and Elias–Williamson Hodge theory. This is about top-heaviness, not log-concavity, and I found no corresponding paper resolving Brenti 2.11. ([math.ac.cn](https://www.math.ac.cn/xshd/xsbg/ytbbg/2023/202604/t20260421_832734.html?utm_source=openai))

### Search for new computations

I searched for public claims involving \(A_6\), \(A_7\), \(B_5\) short intervals, \(B_6\), \(D_6\), \(E_6\), GitHub repositories, MathOverflow posts, and announcements. I found **no** public verification or announcement for:

- \(A_6\) or \(A_7\),
- the remaining short \(B_5\) intervals,
- \(B_6\),
- \(D_6\),
- \(E_6\),
- any Weyl-group counterexample.

MathOverflow searches turned up related Bruhat-interval questions, but nothing directly about Brenti’s rank-log-concavity conjecture or new computational frontiers. ([mathoverflow.net](https://mathoverflow.net/questions/32833/how-linearly-independent-are-the-obvious-combinatorial-invariants-of-a-bruhat-in?utm_source=openai))

### Bottom line for 2024–2026

I found **one substantial recent line** touching log-concavity of Bruhat-type rank sequences: Burrull–Gui–Hu’s asymptotic Brunn–Minkowski work. I found **nothing** newer that appears to advance the finite-Weyl verification frontier beyond Brenti’s list.

---

## 4. VALUE / publishability of new verification or counterexample

### If someone finds a Weyl-group counterexample

A Weyl-group counterexample would be **clearly publishable**, even as a short note, because it would settle Brenti’s Conjecture 2.11 negatively. The note should give:

1. the Coxeter type,
2. explicit \(u,v\), preferably in simple-reflection word form and in a standard realization,
3. the rank generating polynomial,
4. the failed log-concavity inequality,
5. independently reproducible code.

A counterexample in \(E_6\), \(D_6\), \(B_6\), \(A_6\), etc. would be significant.

### If someone completes new exhaustive verification

A computational verification would likely be publishable **if** it is a meaningful extension and reproducible. In my judgment:

- **Completing \(B_5\)**, including all short intervals, is a modest but useful note.
- **Verifying \(A_6\)** alone might be publishable if accompanied by a robust algorithm, certified data, and comparison with Brenti’s frontier; otherwise it may be seen as incremental.
- **Verifying \(A_6,A_7\), \(B_5,B_6\), \(D_6\), and \(E_6\)** would be much stronger and very plausibly publishable as an experimental algebraic-combinatorics paper.
- **Verifying \(E_6\)** would be especially valuable because it moves into exceptional Weyl groups beyond \(F_4\) and is large enough that naïve interval enumeration is nontrivial.

### What would make the computation credible

For a verification note, I would recommend including:

- exact algorithms for Bruhat comparison and interval rank-vector computation;
- independent implementations, e.g. Sage + GAP/CHEVIE or Sage + custom C++/Rust;
- bitset or inversion-set based methods where applicable;
- counts of intervals tested by type and by length;
- hash/certificate files for rank vectors, deposited on Zenodo or GitHub;
- explicit handling of symmetries: inversion, \(w_0\)-duality, left/right multiplication reductions, parabolic decompositions if used;
- exact integer arithmetic only;
- enough code for complete rerun on commodity or documented HPC hardware.

### Likely venues

For a concise computational verification / counterexample note:

- **Electronic Journal of Combinatorics**,
- **Séminaire Lotharingien de Combinatoire**,
- **Enumerative Combinatorics and Applications**,
- **Experimental Mathematics**.

For a paper with a new algorithm, broader Coxeter-theoretic insight, or large-scale exceptional computations:

- **Journal of Algebraic Combinatorics**,
- **Algebraic Combinatorics**,
- **Advances in Applied Mathematics**,
- possibly **Journal of Combinatorial Theory, Series A** if there is substantial new theory.

For preliminary dissemination:

- arXiv,
- FPSAC extended abstract,
- Sage/GAP/CHEVIE-focused computational appendix or repository.

---

## Final answer to your four questions

1. **STATUS:** I found no proof, no Weyl-group counterexample, and no public disproof. The conjecture appears still open as of July 3, 2026.

2. **VERIFICATION FRONTIER:** Your stated frontier is correct: \(A_n\) for \(n\le5\), \(D_n\) for \(n\le5\), \(B_n\) for \(n\le4\), \(B_5\) for \(\ell(u,v)\ge20\), \(F_4\), and dihedral groups. This is stated by Brenti in the OPAC proceedings paper. The \(H_3\) counterexample is also exactly as you described. ([samuelfhopkins.com](https://www.samuelfhopkins.com/OPAC/files/proceedings/brenti.pdf))

3. **RECENT WORK:** The main relevant 2024–2026 work I found is Burrull–Gui–Hu on asymptotic log-concavity of dominant lower affine Bruhat intervals, with arXiv v3 in August 2025 and a FPSAC 2024/SLC extended abstract. I found no public \(A_6\), \(B_5\)-short, \(B_6\), \(D_6\), or \(E_6\) verification or announcement. ([arxiv.org](https://arxiv.org/abs/2311.17980))

4. **VALUE:** A Weyl counterexample would definitely be publishable. A broad, reproducible exhaustive verification extending the frontier—especially through \(A_7\), \(B_6\), \(D_6\), or \(E_6\)—would also likely be publishable, particularly if accompanied by reusable code/certificates or algorithmic improvements. A single small incremental verification is less certain but still potentially suitable as a short computational note if made fully reproducible.

---
usage: ResponseUsage(input_tokens=112401, input_tokens_details=InputTokensDetails(cached_tokens=4224), output_tokens=7734, output_tokens_details=OutputTokensDetails(reasoning_tokens=4238), total_tokens=120135)
