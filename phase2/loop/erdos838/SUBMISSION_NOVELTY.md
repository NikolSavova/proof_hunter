# Submission novelty and citation audit: Erdős--Hammer convex-subset counting

**Audit date:** 2026-08-13  
**Object audited:** the candidate theorem
\[
\limsup_{N\to\infty}\frac{\log_2 f(N)}{(\log_2N)^2}\le \frac12,
\]
proved using a directionally specified, iterated order-type blow-up and exact
substitution formulas for caps, cups, and all convex subsets.

## Bottom-line verdict

The theorem is **apparently novel, but the novelty claim must be narrow and
qualified**. The primary sources checked already contain:

- the Erdős--Hammer total-convex-subset problem and its quasipolynomial scale;
- general and iterated order-type blow-ups (Han--Kohayakawa--Sales--Stagni);
- almost-vertical, geometrically realized Erdős--Szekeres blow-ups with
  detailed mixed-cluster control (Baek--Balko);
- fixed-size convex-polygon supersaturation (Bárány--Valtr and successors);
- exact weighted identities enumerating convex polygons by size and number of
  ambient interior points (Huemer--Oliveros--Pérez-Lantero--Torra--Vogtenhuber);
  and
- the same numerical coefficient \(1/2\), after conversion to base-two
  normalization, in Székely's graph analogue.

No source located in the searches below gives the candidate paper's exact
three substitution identities for the **unweighted total number of all
convex subsets**, or derives the geometric base-two upper coefficient
\(1/2\) for the Erdős--Hammer function. In particular, neither Han et al. nor
Baek--Balko counts all convex subsets of an iterated blow-up.

This is evidence of novelty, not a proof of novelty. The remaining material
risk is an unindexed note, thesis, or a result phrased in order-type,
signotope, or convex-geometry language rather than under Erdős problem 838.
A MathSciNet/Zentralblatt citation-and-similarity check by a human geometer is
still advisable before submission.

## Submission-safe novelty statement

The introduction can safely say:

> We use a directional realization of the standard order-type blow-up. The
> novelty is not cluster replacement or iteration, but the prescribed
> orientations of triples meeting exactly two clusters, the resulting exact
> substitution identities for the total numbers of caps, cups, and convex
> subsets, and their asymptotic optimization. These give the base-two bound
> \(\limsup \log_2 f(N)/(\log_2 N)^2\le 1/2\). We are not aware of an earlier
> geometric result containing these identities or this bound.

Use “we are not aware” rather than “the first.” The title
**Counting convex subsets in iterated order-type blow-ups** is appropriately
descriptive and does not overclaim ownership of the blow-up method.

## Primary-source audit

### 1. Original problem: Erdős, 1978

**Verified source.** Paul Erdős, “Some more problems on elementary geometry,”
*Austral. Math. Soc. Gaz.* **5** (1978), no. 2, 52--54.

- [Author's collected-paper PDF](https://users.renyi.hu/~p_erdos/1978-44.pdf)
- [Rényi Institute Erdős publication index](https://users.renyi.hu/~p_erdos/Erdos.html)

On p. 52 Erdős attributes the question to a conversation with J. Hammer and
defines the largest guaranteed number of convex subsets of an \(n\)-point
set. This is equivalent to the minimum-over-point-sets definition used in the
candidate paper. On p. 53 he derives quasipolynomial upper and lower bounds
and speculates that the normalized logarithm has a limit.

**Required attribution.** Call it the **Erdős--Hammer problem**, or say
“Erdős recorded a question posed with Hammer.” Do not say that Erdős and
Szekeres posed this counting problem. The Erdős--Szekeres theorem and
construction are ingredients, not the authorship of the counting question.

**Claim boundary.** Erdős did not prove existence of the limit. The new
theorem is a limsup upper bound, not a solution of the limit problem.

### 2. Classical survey: Morris--Soltan, 2000

**Verified source.** Walter Morris and Valeriu Soltan, “The Erdős--Szekeres
problem on points in convex position---a survey,” *Bull. Amer. Math. Soc.
(N.S.)* **37** (2000), no. 4, 437--458.

- [Publisher DOI](https://doi.org/10.1090/S0273-0979-00-00877-6)
- [Accessible article PDF](https://www.cs.umd.edu/~gasarch/COURSES/752/S22/slides/erdos-szek-convex.pdf)

Section 5.1, especially p. 450, is the direct survey predecessor. It first
discusses the minimum number of convex \(k\)-gons for fixed \(k\), then records
the Erdős--Hammer all-sizes function (there denoted \(s(r)\)), its
\(r^{a\log r}<s(r)<r^{b\log r}\) bounds, and Erdős's limit speculation.

**Recommendation.** Keep this citation immediately after the problem
statement. It supports the historical framing and separates the fixed-\(k\)
enumeration problem from the all-sizes function.

### 3. General iterated order-type blow-ups: Han et al., 2019

**Verified source.** Jie Han, Yoshiharu Kohayakawa, Marcelo T. Sales, and
Henrique Stagni, “Extremal and probabilistic results for order types,” in
*Proceedings of the Thirtieth Annual ACM--SIAM Symposium on Discrete
Algorithms (SODA 2019)*, 426--435.

- [SIAM publisher page](https://epubs.siam.org/doi/10.1137/1.9781611975482.27)
- DOI: [10.1137/1.9781611975482.27](https://doi.org/10.1137/1.9781611975482.27)
- [Author-uploaded full text](https://www.researchgate.net/publication/330100547_Extremal_and_probabilistic_results_for_order_types)

Section 3.3 defines a blow-up into equal clusters: every transversal has the
skeleton order type, and a \(C\)-blow-up additionally gives each cluster order
type \(C\). It constructs such blow-ups in sufficiently small neighborhoods
of the skeleton points and explicitly defines iterated products
\(\bigotimes_{i=1}^d X_i\).

**Collision.** “Order-type blow-up,” cluster replacement, small-neighborhood
realization, and iteration are all prior art. The paper must not claim to
introduce any of them.

**Non-collision.** Han et al.'s abstract product fixes triples within one
cluster and triples in three distinct clusters. It does not prescribe the two
orientations for triples having a \(2+1\) cluster pattern, and it gives no
cap/cup/total-convex-subset substitution formula. The directional
\((\varepsilon^2,\varepsilon)\) realization and its enumerative use are a
legitimate additional structure.

The SIAM page currently exposes two citing articles. Title, abstract, and
targeted title/citation searches revealed no descendant paper using this
product to count all convex subsets. That publisher list is not guaranteed to
be a complete citation graph, so it should not be described as exhaustive.

### 4. Almost-vertical Erdős--Szekeres blow-ups: Baek--Balko, 2025/2026

**Journal source.** Jineon Baek and Martin Balko, “The Erdős--Szekeres
Conjecture Revisited,” *Journal of Combinatorial Theory, Series A* **222**
(2026), article 106195.

- [ScienceDirect article](https://www.sciencedirect.com/science/article/pii/S0097316526000385)
- DOI: [10.1016/j.jcta.2026.106195](https://doi.org/10.1016/j.jcta.2026.106195)

The full open-access journal text, not only the conference version, was
checked on 2026-08-13.  The relevant existence result is Theorem 7 in the
journal numbering (Theorem 8 in the preliminary version), with its proof in
Section 7.  The full proof of Lemma 14 is also present.

**Preliminary conference version.** *41st International Symposium on
Computational Geometry (SoCG 2025)*, LIPIcs 332, article 13, pp. 13:1--13:15.

- [Dagstuhl record and official metadata](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2025.13)
- [Open conference PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/LIPIcs.SoCG.2025.13/LIPIcs.SoCG.2025.13.pdf)
- DOI: [10.4230/LIPIcs.SoCG.2025.13](https://doi.org/10.4230/LIPIcs.SoCG.2025.13)

Definition 13 of the conference version is an \((X,Y)\)-blow-up obtained by
replacing skeleton points with rotated, almost-vertical Pascal-type clusters
in small neighborhoods. Lemma 14 controls the largest possible convex subset
and gives an exact formula for the **number of points** in the constructed
set. Its full journal proof contains the endpoint-cluster classification that
underlies our count: the occupied macro points are convex, intermediate
clusters contribute at most one point, and only the first and last occupied
clusters can contribute chains with more than one point. The paper says that
known \(2^{k-2}\)-point constructions arise as special cases.

The decomposable class itself predates Baek--Balko.  Balko, Kynčl,
Langerman, and Pilz, “Induced Ramsey-Type Results and Binary Predicates for
Point Sets,” *Electron. J. Combin.* **24**(4) (2017), P4.24, introduced the
recursive left/deep-below definition.  Our \(A\prec B\) convention is its
mirror under \(\rho(x,y)=(-x,y)\), with the child order reversed.  The paper
now credits the 2017 source at the class definition and positions its
total-count theorem against Baek--Balko's Theorem 7.

**Collision.** Almost-vertical cluster replacement tailored to the
Erdős--Szekeres problem is emphatically prior art. Baek--Balko is the closest
geometric citation and should be discussed, not merely listed.

**Non-collision.** Their objective is to maximize the size of a point set
with no \(k\) points in convex position. Their exact formula counts points;
it is not an enumerator for all convex subsets. Lemma 14 supplies an important
structural precursor to the crossing term, but the journal paper does not sum
all endpoint-chain choices, state the \(C,U,W\) recurrences, or derive the
base-two \(1/2\) total-count bound.

**Bibliographic recommendation.** Cite the 2026 journal article as the main
source and identify SoCG 2025 as the preliminary version if desired. Do not
present them as two independent results. The current shorthand “SoCG 2025 /
JCTA 2026” is factually fine but should be normalized in the bibliography.

### 5. Fixed-size convex-polygon counts: Bárány--Valtr, 1998

**Verified source.** Imre Bárány and Pavel Valtr, “A positive fraction
Erdős--Szekeres theorem,” *Discrete Comput. Geom.* **19** (1998), no. 3,
335--342.

- [Author PDF](https://www.renyi.hu/~barany/cikkek/72.pdf)
- DOI: [10.1007/PL00009350](https://doi.org/10.1007/PL00009350)

For every fixed \(k\), the positive-fraction theorem yields many convex
\(k\)-gons through large blocks whose transversals are convex. This is the
standard supersaturation predecessor cited by Morris--Soltan.

**Non-collision.** Its constants depend on fixed \(k\), and it neither treats
the sum over all \(k\) nor analyzes \(k\asymp\log N\) sharply enough to give
the candidate theorem. Cite it if the introduction discusses enumerative
predecessors; it need not carry the blow-up novelty discussion.

### 6. Exact weighted polygon enumeration: Huemer et al., 2022

**Verified source.** Clemens Huemer, Deborah Oliveros, Pablo
Pérez-Lantero, Ferran Torra, and Birgit Vogtenhuber, “On Weighted Sums of
Numbers of Convex Polygons in Point Sets,” *Discrete Comput. Geom.* **68**
(2022), 448--476.

- [Springer article](https://link.springer.com/article/10.1007/s00454-022-00395-8)
- DOI: [10.1007/s00454-022-00395-8](https://doi.org/10.1007/s00454-022-00395-8)

If \(X_{k,\ell}\) counts convex \(k\)-gons having exactly \(\ell\) ambient
points in their interior, the paper proves the exact generating identity
\[
 \sum_{k=3}^N\sum_{\ell=0}^{N-k}
 x^k(1+x)^\ell X_{k,\ell}
 =(1+x)^N-1-xN-x^2\binom N2.
\]
This is genuine exact convex-polygon enumeration and should be acknowledged
if the submission uses a broad phrase such as “exact enumerator.”

**Non-collision.** The desired unweighted total is
\(\sum_{k,\ell}X_{k,\ell}\). The displayed identity supplies a weighted sum
(at \(x=1\), weight \(2^\ell\)), which does not determine that total and can
be dominated by polygons containing many ambient points. The paper does not
give a blow-up substitution identity or an \(\exp(\Theta(\log^2 N))\)
extremal bound.

**Required wording correction.** Avoid “the first exact enumeration of
convex polygons.” A safe claim is “exact substitution identities for these
three statistics under our directional composition.”

### 7. Recent fixed-\(k\) work: Mackey--Subercaseaux, 2024

**Verified preprint.** John Mackey and Bernardo Subercaseaux, “Pentagon
Minimization without Computation,” arXiv:2409.17098 (2024).

- [arXiv record and PDF](https://arxiv.org/abs/2409.17098)

This studies the minimum number \(\mu_k(n)\) of convex \(k\)-gons, with its
new result focused on \(k=5\), and records a standard supersaturation
reduction. No journal publication was located as of the audit date, so cite
it only as a preprint. It does not address growing \(k\), the all-sizes sum,
or iterated blow-up enumeration.

This citation is optional unless the paper surveys recent fixed-\(k\) counts.

### 8. Numerical precedent in the graph analogue: Székely, 1984

**Verified source.** L. A. Székely, “On the number of homogeneous subgraphs
of a graph,” *Combinatorica* **4** (1984), 363--372.

- [Springer article](https://link.springer.com/article/10.1007/BF02579149)
- DOI: [10.1007/BF02579149](https://doi.org/10.1007/BF02579149)

Székely's abstract records an upper exponent
\(\exp(0.7214(\log n)^2)\). With natural logarithms, the exact constant
\(1/(2\ln2)=0.721347\ldots\) becomes coefficient \(1/2\) in the normalization
\(\log_2 G(n)/(\log_2n)^2\).

**Novelty consequence.** Do not write “the constant \(1/2\) appears for the
first time.” The safe claim is “the first such geometric bound known to us,”
or, better, simply state the result without a priority superlative. The graph
theorem is an instructive analogue but supplies no geometric blow-up
recurrence or transfer theorem.

### 9. Modern Erdős--Szekeres estimates and the lower-window context

If the submission states the currently derivable base-two lower coefficient
\(1/4\), cite the modern convex-polygon bounds from which the standard
double-counting argument follows:

- Andrew Suk, “On the Erdős--Szekeres convex polygon problem,” *J. Amer.
  Math. Soc.* **30** (2017), no. 4, 1047--1053,
  [DOI 10.1090/jams/869](https://doi.org/10.1090/jams/869),
  [arXiv:1604.08657](https://arxiv.org/abs/1604.08657).
- Andreas F. Holmsen, Hossein Nassajian Mojarrad, János Pach, and Gábor
  Tardos, “Two extensions of the Erdős--Szekeres problem,” *J. Eur. Math.
  Soc.* **22** (2020), no. 12, 3981--3995,
  [publisher page](https://ems.press/journals/jems/articles/17088),
  [DOI 10.4171/JEMS/1000](https://doi.org/10.4171/JEMS/1000).

The coefficient \(1/4\) is a corollary obtained by choosing
\(k=(1/2-o(1))\log_2N\) and double-counting, not a theorem explicitly stated
in either paper. If used, prove the short corollary in the submission rather
than attributing that exact normalized statement to them.

### 10. Status page, not scholarly prior art

The [Erdős Problems entry 838](https://www.erdosproblems.com/838) still marks
the problem open, attributes it to Erdős and Hammer, and records only
quasipolynomial bounds. The [discussion thread](https://www.erdosproblems.com/forum/thread/838)
contains a 2026 comment deriving the lower coefficient \(1/4\) and discussing
an upper coefficient \(1\). This is useful for status and priority checking,
but the original paper and peer-reviewed sources should carry the
mathematical citations. If the database is cited, include an access date of
2026-08-13.

## Exact overclaim audit of the current draft

The following present claims are sound or can be made sound with small
changes:

1. **“Erdős recorded a question posed with Hammer.”** Correct.
2. **“General blow-ups and their iteration appear in Han et al.”** Correct,
   and important.
3. **“Almost-vertical blow-ups tailored to Erdős--Szekeres appear in
   Baek--Balko.”** Correct. Prefer the JCTA 2026 citation, with the SoCG paper
   identified as preliminary.  Credit Balko--Kynčl--Langerman--Pilz (2017)
   for the decomposable class and Baek--Balko Lemma 14 for the endpoint-cluster
   structure.
4. **“The feature used here is a prescribed orientation for triples meeting
   exactly two clusters.”** Defensible relative to the sources checked.
5. **“Those orientations give the exact enumerator ...; iterating it produces
   \(1/2\).”** Defensible if “enumerator” is locally defined as the composition
   identities, not as the first exact convex-polygon enumeration of any kind.

The following formulations should be avoided or qualified:

| Risky formulation | Why risky | Submission-safe replacement |
|---|---|---|
| “We introduce order-type blow-ups” | Han et al. already define and iterate them. | “We use a directionally specified realization of an order-type blow-up.” |
| “We introduce almost-vertical blow-ups” | Baek--Balko already use them centrally. | “Our anisotropic realization prescribes the two mixed-cluster signs needed for counting.” |
| “First exact enumeration of convex polygons/subsets” | Huemer et al. prove exact weighted polygon identities. | “Exact substitution identities for caps, cups, and total convex subsets under this composition.” |
| “The first occurrence of the \(1/2\) constant” | Székely's graph analogue has the same base-normalized coefficient. | Omit priority, or say “the first geometric bound of this form known to us.” |
| “We solve Erdős problem 838” | The theorem is only an upper limsup; existence/value of the limit and the lower bound remain open. | “We improve the upper coefficient in the Erdős--Hammer problem.” |
| “The previous best published upper constant was \(1\)” | The coefficient-\(1\) estimate is standard and appears publicly, but this audit did not locate a paper whose headline theorem records that exact normalized constant. | “A standard estimate for the classical construction gives coefficient \(1\); we improve it to \(1/2\).” Include the estimate or a citation. |
| “The current published window is \([1/4,1/2]\)” | The \(1/4\) statement is a short corollary of modern Erdős--Szekeres bounds and is also in a forum comment, not located verbatim as a published theorem. | Prove the corollary and say “combining this with the standard double-counting consequence gives the window \([1/4,1/2]\).” |
| Treating SoCG 2025 and JCTA 2026 as independent works | The latter is the journal version of the former. | Cite JCTA 2026; parenthetically identify the SoCG preliminary version. |

One additional clarity improvement is advisable in the abstract. Replace
“the classical construction gives
\(\log_2 f(N)\le(1+o(1))(\log_2N)^2\)” by either a proved one-line estimate or
“a standard counting estimate applied to the classical construction gives
...”. This avoids implying that the precise normalized constant was a named
published theorem in one of the cited sources.

## Search coverage and residual risk

The audit checked, through primary publisher or author sources where
available:

- the 1978 original and the 2000 survey;
- Han et al.'s publisher record, full text, visible citation list, and
  title/citation searches combined with “convex subset,” “convex position,”
  “enumeration,” and “blow-up”;
- both versions of Baek--Balko and their blow-up section;
- fixed-\(k\), supersaturation, and weighted-enumeration literature identified
  in those sources and by targeted searches;
- the official problem page and thread; and
- searches for the symbolic constants \(1/2\) and \(1/(2\ln2)\), including
  the homogeneous-subgraph analogue.

No hit contained the candidate mixed-sign \(C,U,W\) recurrences or the
geometric \(1/2\) theorem. The audit was not a complete paid-database review,
and publisher “cited by” lists are incomplete. Before arXiv submission, send
the statement and Lemma 2.2 to at least one specialist in Erdős--Szekeres
constructions and run exact-title/formula searches in MathSciNet and
Zentralblatt.

## Concise BibTeX-ready bibliography

The first seven entries are the recommended core bibliography. The remaining
entries are useful if the submission discusses fixed-\(k\) enumeration, the
lower window, or the graph analogy.

```bibtex
@article{Erdos1978MoreProblems,
  author  = {Erd{\H{o}}s, Paul},
  title   = {Some more problems on elementary geometry},
  journal = {Austral. Math. Soc. Gaz.},
  volume  = {5},
  number  = {2},
  year    = {1978},
  pages   = {52--54},
  url     = {https://users.renyi.hu/~p_erdos/1978-44.pdf}
}

@article{MorrisSoltan2000Survey,
  author  = {Morris, Walter and Soltan, Valeriu},
  title   = {The {E}rd{\H{o}}s--{S}zekeres problem on points in convex position---a survey},
  journal = {Bull. Amer. Math. Soc. (N.S.)},
  volume  = {37},
  number  = {4},
  year    = {2000},
  pages   = {437--458},
  doi     = {10.1090/S0273-0979-00-00877-6}
}

@inproceedings{HanKohayakawaSalesStagni2019,
  author    = {Han, Jie and Kohayakawa, Yoshiharu and Sales, Marcelo T. and Stagni, Henrique},
  title     = {Extremal and probabilistic results for order types},
  booktitle = {Proceedings of the Thirtieth Annual ACM--SIAM Symposium on Discrete Algorithms},
  editor    = {Chan, Timothy M.},
  publisher = {Society for Industrial and Applied Mathematics},
  year      = {2019},
  pages     = {426--435},
  doi       = {10.1137/1.9781611975482.27}
}

@article{BaekBalko2026Revisited,
  author  = {Baek, Jineon and Balko, Martin},
  title   = {The {E}rd{\H{o}}s--{S}zekeres Conjecture Revisited},
  journal = {J. Combin. Theory Ser. A},
  volume  = {222},
  year    = {2026},
  pages   = {106195},
  doi     = {10.1016/j.jcta.2026.106195}
}

@article{BaranyValtr1998PositiveFraction,
  author  = {B{\'a}r{\'a}ny, Imre and Valtr, Pavel},
  title   = {A positive fraction {E}rd{\H{o}}s--{S}zekeres theorem},
  journal = {Discrete Comput. Geom.},
  volume  = {19},
  number  = {3},
  year    = {1998},
  pages   = {335--342},
  doi     = {10.1007/PL00009350}
}

@article{HuemerEtAl2022WeightedSums,
  author  = {Huemer, Clemens and Oliveros, Deborah and P{\'e}rez-Lantero, Pablo and Torra, Ferran and Vogtenhuber, Birgit},
  title   = {On Weighted Sums of Numbers of Convex Polygons in Point Sets},
  journal = {Discrete Comput. Geom.},
  volume  = {68},
  year    = {2022},
  pages   = {448--476},
  doi     = {10.1007/s00454-022-00395-8}
}

@article{Szekely1984Homogeneous,
  author  = {Sz{\'e}kely, L{\'a}szl{\'o} A.},
  title   = {On the number of homogeneous subgraphs of a graph},
  journal = {Combinatorica},
  volume  = {4},
  year    = {1984},
  pages   = {363--372},
  doi     = {10.1007/BF02579149}
}

@article{Suk2017ConvexPolygon,
  author  = {Suk, Andrew},
  title   = {On the {E}rd{\H{o}}s--{S}zekeres convex polygon problem},
  journal = {J. Amer. Math. Soc.},
  volume  = {30},
  number  = {4},
  year    = {2017},
  pages   = {1047--1053},
  doi     = {10.1090/jams/869},
  eprint  = {1604.08657},
  archivePrefix = {arXiv}
}

@article{HolmsenEtAl2020Extensions,
  author  = {Holmsen, Andreas F. and Nassajian Mojarrad, Hossein and Pach, J{\'a}nos and Tardos, G{\'a}bor},
  title   = {Two extensions of the {E}rd{\H{o}}s--{S}zekeres problem},
  journal = {J. Eur. Math. Soc.},
  volume  = {22},
  number  = {12},
  year    = {2020},
  pages   = {3981--3995},
  doi     = {10.4171/JEMS/1000}
}

@misc{MackeySubercaseaux2024Pentagon,
  author        = {Mackey, John and Subercaseaux, Bernardo},
  title         = {Pentagon Minimization without Computation},
  year          = {2024},
  eprint        = {2409.17098},
  archivePrefix = {arXiv},
  primaryClass  = {math.CO},
  url           = {https://arxiv.org/abs/2409.17098}
}

@inproceedings{BaekBalko2025RevisitedPreliminary,
  author    = {Baek, Jineon and Balko, Martin},
  title     = {The {E}rd{\H{o}}s--{S}zekeres Conjecture Revisited},
  booktitle = {41st International Symposium on Computational Geometry (SoCG 2025)},
  series    = {Leibniz International Proceedings in Informatics (LIPIcs)},
  volume    = {332},
  year      = {2025},
  pages     = {13:1--13:15},
  publisher = {Schloss Dagstuhl--Leibniz-Zentrum f{\"u}r Informatik},
  doi       = {10.4230/LIPIcs.SoCG.2025.13},
  note      = {Preliminary version of the JCTA 2026 article}
}
```
