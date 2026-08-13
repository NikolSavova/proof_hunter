# Prior-art sweep — casas_alvero (gpt-5.6-sol, effort=max, 2026-08-13 08:24)

> Counterexample-shaped target, selected after the Jacobian conjecture
> counterexample (Alpoge/Fable 5, 2026-07-20). Sweep asks BOTH whether the
> problem is already resolved AND where counterexample search is already dead.

# 1. STATUS as of August 13, 2026: **PROVED**

Soham Ghosh’s current preprint proves the **exact characteristic-zero statement in the question**:

- arbitrary characteristic-zero field \(K\);
- every positive degree;
- a potentially **different common root for each derivative**;
- no real-root, same-root, or algebraic-closure restriction.

In characteristic zero, Hasse–Schmidt and ordinary derivatives differ only by the nonzero scalar \(i!\), so Ghosh’s formulation is equivalent to yours. Theorem A covers every \(n\ge3\); degrees \(1\) and \(2\) are elementary. Therefore:

> **Complete proved degree set:** every \(n\in\mathbb Z_{>0}\).  
> **Smallest degree still open:** **none**.

The proof establishes the downward implication “the conjecture in degree \(n+1\) implies it in degree \(n\)” through a regular-sequence reformulation and Koszul homology. Since earlier work supplies arbitrarily large proved degrees, downward induction gives all degrees. ([arxiv.org](https://arxiv.org/abs/2501.09272))

## Main reference

**Soham Ghosh**, “Proof of the Casas-Alvero conjecture,” 2025; current version **v2**, revised March 21, 2026, arXiv preprint, 22 pages.  
- arXiv: **2501.09272v2**  
- DOI: **10.48550/arXiv.2501.09272**  
- URL: https://arxiv.org/abs/2501.09272  
- PDF: https://arxiv.org/pdf/2501.09272  
- Journal venue/ordinary publisher DOI: **none located as of August 13, 2026**; arXiv labels the revision “Major revisions.” ([arxiv.org](https://arxiv.org/abs/2501.09272))

This is not merely an unsupported title claim. Active Casas–Alvero researchers Daniel Schaub and Mark Spivakovsky explicitly added to their February 2025 paper that Ghosh had given a **complete proof**; Ghosh’s revised paper also acknowledges Spivakovsky for carefully reading several drafts. I found no public erratum, withdrawal, or identified gap directed at the March 2026 version. ([arxiv.org](https://arxiv.org/pdf/2312.08742))

**Daniel Schaub and Mark Spivakovsky**, “A note on the Casas-Alvero Conjecture,” 2025 version, arXiv preprint.  
- arXiv: **2312.08742v7**  
- DOI: **10.48550/arXiv.2312.08742**  
- URL: https://arxiv.org/abs/2312.08742  
- PDF: https://arxiv.org/pdf/2312.08742 ([arxiv.org](https://arxiv.org/abs/2312.08742))

## Axis audit and coverage

**Checked:** the precise all-degrees, characteristic-zero, different-root-per-derivative axis.  
**Not treated further:** positive characteristic, coefficient varieties, historical computation bounds, and search parametrizations—because your instructions say to stop once the exact target is proved.

I explicitly searched arXiv-relevant results from August 2024 through August 2026, exact-title publication records, and searches combining the proof with “flaw,” “gap,” “error,” “correction,” and “withdrawn.” I did not have direct closed-index access to MathSciNet, Scopus, or Web of Science, and the proof itself does not yet appear to have a journal publication record; thus the remaining sensible project is an independent proof audit, **not** a counterexample computation.

**VERDICT: PROVED | HOPELESS**

Ghosh’s March 2026 revision proves the exact characteristic-zero conjecture in every degree, so there is no smallest open degree. Unless an error is discovered in this specialist-endorsed but not yet journal-published proof, a characteristic-zero counterexample hunt is dead.