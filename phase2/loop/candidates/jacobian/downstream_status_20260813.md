# Jacobian aftermath — status (gpt-5.6-sol, effort=max, 2026-08-13 09:25)

> The counterexample is three weeks old. This sweep is about finding what is
> ALREADY TAKEN, not about admiring the result.

## Bottom line

**Search cutoff: August 13, 2026.** Alpöge’s post was made on **July 20, 2026 UTC**—July 19 in some American accounts—and Tao’s digestion appeared July 21. ([zzhang-iu.github.io](https://zzhang-iu.github.io/papers/direct-consequences-jacobian/index.html))

The blunt version:

- **Your proposed \(A_2\) Dixmier corollary is invalid.** The implication goes the wrong way for that deduction.
- **An explicit \(A_3\) Dixmier counterexample is already gone**—posted within roughly a day.
- **The Mathieu fallout is gone**, including an explicit and stronger \(SU(2)\) counterexample.
- **Ordinary degree-three and cubic-homogeneous reductions are gone.**
- **The explicit Drużkowski \(x+(Ax)^{*3}\) endpoint is the major remaining mechanical prize.**
- **The broad family/moduli follow-up is gone.**
- **Several direct obstructions to transplanting the construction to \(\mathbb C^2\) are gone**, but the plane case itself is completely open.
- **Minimal total degree in dimension three is still open:** current bounds are \(4\le d_{\min}(3)\le7\).
- **Paul Lezeau’s Lean formalization is real and already taken.**

Here **TAKEN** means a dated public artifact exists, not that it has passed peer review. Most July 2026 follow-ups are still unrefereed.

---

# 1. Dixmier: exact direction and consequences

Belov-Kanel–Kontsevich’s exact abstract statement is:

> “We prove that the Jacobian conjecture in dimension \(2n\) implies the Dixmier conjecture in rank \(n\).”

Thus the fixed-rank implications are

\[
\boxed{\mathrm{JC}_{2n}\Longrightarrow \mathrm D_n}
\qquad\text{and}\qquad
\boxed{\mathrm D_n\Longrightarrow \mathrm{JC}_n}.
\]

It is **not** a fixed-rank biconditional \(\mathrm D_n\Longleftrightarrow\mathrm{JC}_{2n}\). What is equivalent is the **stable/all-dimensional package**: all Jacobian conjectures hold iff all Dixmier conjectures hold. ([arxiv.org](https://arxiv.org/abs/math/0512171))

Your \(A_2\) inference is a logical error:

\[
\mathrm{JC}_4\Rightarrow \mathrm D_2,\qquad \neg\mathrm{JC}_4
\]

says **nothing** about \(\mathrm D_2\). Denying the antecedent is invalid. The contrapositive is

\[
\neg\mathrm D_2\Rightarrow\neg\mathrm{JC}_4,
\]

not the converse.

On the other hand,

\[
\mathrm D_3\Rightarrow\mathrm{JC}_3
\]

does give, by contraposition,

\[
\neg\mathrm{JC}_3\Rightarrow\neg\mathrm D_3.
\]

### Status

| Item | Status | Record |
|---|---|---|
| Claim that the Alpöge map makes \(\mathrm D_2\) false | **NOT VALID** | No consequence for \(A_2\); serious follow-up notes explicitly flag this mistake. \(\mathrm D_2\) remains open. ([zenodo.org](https://zenodo.org/records/21514514)) |
| Explicit nonautomorphism of \(A_2\) | **UNCLAIMED / OPEN** | None found. It does not follow from the stabilized four-variable Keller map. |
| Explicit nonautomorphism of \(A_3\) | **TAKEN — July 20–21** | Secret Blogging Seminar gave the same-rank construction; independent Omniscience, AGNT, Giannini and Mayner artifacts followed. ([omniscienceproject.com](https://omniscienceproject.com/papers/an-explicit-counterexample-to-the-dixmier-conjecture-in-a-3-jfLENtXF)) |
| \(\mathrm D_n\) for \(n\ge3\) | **FALSE** | Tensor/stabilize the \(A_3\) example upward. |
| Lean proof of the \(A_3\) Weyl-algebra argument | **UNCLAIMED** | The polynomial counterexample is formalized, but the Weyl-algebra lift and non-surjectivity argument have not, in the material found, been kernel-checked. ([zenodo.org](https://zenodo.org/records/21514514)) |

The explicit \(A_3\) endomorphism is standard and short to state. Let \(J=DF\), \(B=J^{-1}\), which is polynomial because \(\det J=-2\). For Weyl generators satisfying \([D_i,X_j]=\delta_{ij}\), set

\[
\Phi(X_i)=F_i(X),\qquad
\Phi(D_i)=\sum_j B_{ji}(X)D_j.
\]

The inverse-Jacobian vector fields commute and have \(\delta_i(F_j)=\delta_{ij}\), so these assignments preserve the Weyl relations. Full expanded operators and machine checks are public. ([agnt.gg](https://agnt.gg/whitepapers/machine-verified-corollary-mining-jacobian-conjecture.html))

**Verdict:** forget \(A_2\). The correct immediate casualty is \(A_3\), and that was claimed almost immediately.

---

# 2. Mathieu, Zhao, Image, Gaussian moments and related casualties

There is no single standard conjecture universally called “the Mathieu–Zhao conjecture.” There are several conjectures asserting that particular kernels or images are Mathieu–Zhao subspaces.

## Standard implication network

| Conjecture/result | Exact downstream status | Public record |
|---|---|---|
| Mathieu conjecture for \(SU(3)\) | **TAKEN — July 20** | Mathieu’s fixed-dimensional argument gives \(\mathrm{MC}(SU(N))\Rightarrow\mathrm{JC}(N)\). Zhang explicitly recorded that \(\mathrm{MC}(SU(3))\) is false. This is initially existential, not an explicit pair of functions. ([zzhang-iu.github.io](https://zzhang-iu.github.io/papers/direct-consequences-jacobian/index.html)) |
| Original universal compact-group Mathieu conjecture | **TAKEN, explicitly** | Christopher D. Long gave explicit regular functions on \(SU(2)\), hence a stronger direct refutation. The preprint is arXiv:2607.19012, posted in the July 21 batch. ([arxiv-troller.com](https://arxiv-troller.com/?q=paper%3A+2605.03683)) |
| Duistermaat–van der Kallen theorem | **SURVIVES** | It proves the torus/connected-abelian case of Mathieu’s conjecture. It does **not** imply the full Jacobian conjecture by itself and is not refuted. ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0022404924002445)) |
| Gaussian Moments Conjecture | **TAKEN — July 20** | Zhang first recorded existential failure. Long then gave explicit \(P,Q\) in three Gaussian variables with \(\mathbb E(P^m)=0\) and \(\mathbb E(QP^m)=m!\), so GMC fails in every dimension \(n\ge3\). arXiv:2607.18186, submitted July 20 at 17:24 UTC. ([zzhang-iu.github.io](https://zzhang-iu.github.io/papers/direct-consequences-jacobian/index.html)) |
| Zhao’s Vanishing Conjecture | **TAKEN** | Zhao proved equivalence of the all-dimensional VC and JC. Zhang recorded the immediate existential failure on July 20. ([zzhang-iu.github.io](https://zzhang-iu.github.io/papers/direct-consequences-jacobian/index.html)) |
| Explicit Vanishing-Conjecture witness | **TAKEN†** | A subsequent consequence-cascade artifact starts from a cubic-homogeneous map and produces an explicit 48-variable homogeneous quartic Hessian-nilpotent polynomial over \(\mathbb Q(i)\), with 382 monomials, witnessing failure. ([zenodo.org](https://zenodo.org/records/21503372)) |
| Image Conjecture | **TAKEN existentially — July 20** | Image Conjecture \(\Rightarrow\) Vanishing Conjecture \(\Leftrightarrow\) JC, so it fails in some finite dimension. Zhang stated this explicitly. ([zzhang-iu.github.io](https://zzhang-iu.github.io/papers/direct-consequences-jacobian/index.html)) |
| Small explicit Image-Conjecture witness | **UNCLAIMED** | I found no public coefficient-level element \(a,b\) exhibiting the failed MZ property. This is still a very concrete target. |
| Special Image Conjecture | **FALSE in some dimension** | Its fixed-dimensional implication for cubic-homogeneous Keller maps is used in the Gaussian-moments literature. ([alphaxiv.org](https://www.alphaxiv.org/abs/2607.18186)) |
| \(xz\)-conjecture / associated MZ-kernel statement | **TAKEN, explicitly** | Long gives a three-term Laurent polynomial counterexample and lifts it to \(SU(2)\). ([arxiv-troller.com](https://arxiv-troller.com/?q=paper%3A+2605.03683)) |

For reference, Long’s explicit \(SU(2)\) functions are reported as

\[
F=(1+c)(ad+b),\qquad G=-c,
\]

with all pure moments of \(F\) zero and

\[
\int_{SU(2)}F^nG\,dg=\frac{(-1)^{n-1}}{n+1}\ne0.
\]

So the compact-group Mathieu conjecture is not merely dead by contraposition from \(\mathrm{JC}_3\); it has an explicit low-rank corpse. ([arxiv-troller.com](https://arxiv-troller.com/?q=paper%3A+2605.03683))

### Important non-casualties

Do **not** declare every result containing the words “Mathieu–Zhao” false.

- Duistermaat–van der Kallen remains a theorem.
- Low-dimensional LND/LNED results remain valid.
- “Arose from the study of JC” is not the same as “implies JC.”
- The failure of the full Image Conjecture does not automatically refute restricted conjectures about images of locally nilpotent derivations.

---

# 3. Cubic reductions

This target is partly gone.

## What has actually been executed

| Normal form | Status | Dimension/public record |
|---|---|---|
| Arbitrary map of total degree at most \(3\) | **TAKEN — July 20** | A mechanical BCW reduction with carrier sharing gives a 19-variable map, computed in 17 elementary steps with 16 auxiliaries. It is cubic but **not cubic homogeneous**. ([rhicksrad.github.io](https://rhicksrad.github.io/jacobian-degree3/)) |
| \(X+H\), with \(H\) consisting of quadratic and cubic terms | **TAKEN — July 21** | AGNT gives a 22-variable, 68-monomial map with \(H(0)=JH(0)=0\), \(\det J=1\), and an explicit three-point collision. Again, **not homogeneous**. ([agnt.gg](https://agnt.gg/whitepapers/machine-verified-corollary-mining-jacobian-conjecture.html)) |
| Cubic-homogeneous \(X+H_3\) | **TAKEN** | Long tracks a conservative standard reduction landing in 79 variables. A later Zenodo cascade reports an independently checked explicit “Thompson” form in 24 variables; I did not recover the primary Thompson posting, so treat 24 as public priority evidence but not yet clean bibliographic history. ([arxiv.org](https://arxiv.org/abs/2607.18186)) |
| Symmetric cubic-homogeneous form | **TAKEN†** | The 48-variable Hessian/gradient construction gives the symmetric cubic-homogeneous version through a quartic potential. ([zenodo.org](https://zenodo.org/records/21503372)) |
| Drużkowski \(X+(AX)^{*3}\) | **UNCLAIMED RESULT; ACTIVE RACE** | Multiple July 21 reports explicitly leave this as future work. No completed matrix \(A\), collision certificate and determinant/nilpotency certificate were found through August 13. ([agnt.gg](https://agnt.gg/whitepapers/machine-verified-corollary-mining-jacobian-conjecture.html)) |
| Minimal dimension for a cubic counterexample | **IN PROGRESS / OPEN** | Current explicit dimensions include 19, 22, 24, 48 and 79 for different normal forms. The 19-variable author explicitly records the open gap \(4\le n\le18\). ([rhicksrad.github.io](https://rhicksrad.github.io/jacobian-degree3/)) |

## Blunt assessment

**The generic BCW computation you identified is already gone.** It was done within a day.

**THE EXPLICIT DRUŻKOWSKI COUNTEREXAMPLE IS STILL AVAILABLE.**

That is now the cleanest mechanical construction project:

1. start from the public 24- or 48-variable cubic-homogeneous artifact;
2. execute Drużkowski’s cubic-linear reduction;
3. publish the matrix \(A\);
4. certify the Keller condition, usually via the appropriate nilpotency identities;
5. transport and print an exact collision;
6. then optimize rank, sparsity and dimension.

It is sufficiently obvious that I would expect someone to take it very soon.

---

# 4. The plane case

\[
\boxed{\mathrm{JC}_2\text{ remains open as of August 13, 2026.}}
\]

No accepted proof or complex two-dimensional counterexample was found. Tao states this explicitly, as do the later arXiv papers. ([terrytao.wordpress.com](https://terrytao.wordpress.com/?blogsub=confirming))

## What was done after July 20

| Plane item | Status | Record |
|---|---|---|
| Direct marked-root/\((L,Q)\) descent | **TAKEN — obstruction proved** | An exact audit proves that no affine two-plane of binary forms, of any degree, can reproduce the marked-projective-root construction in the same chart. The identity \(D(w)J(A,B)=s\,s_x\) forces a rational-square contradiction. “The third free coefficient in dimension three is essential.” ([nasqret.github.io](https://nasqret.github.io/jacobian-counterexample/book/plane-descent-obstructions.html)) |
| “Linear in the extra variable” descent | **TAKEN — obstruction proved** | If one coordinate of a plane Keller map is affine-linear in one source variable, the map is triangular up to a shear and hence an automorphism. This pinpoints why the rich \(z\)-linear threefold ansatz becomes trivial in dimension two. ([nasqret.github.io](https://nasqret.github.io/jacobian-counterexample/book/plane-descent-obstructions.html)) |
| Graded/torus-equivariant plane mechanism | **TAKEN — July 22** | Shaska’s arXiv:2607.20210 classifies graded Keller maps in \(\mathbb C^2\): they are automorphisms. This blocks the direct weighted mechanism, not arbitrary plane counterexamples. ([github.com](https://github.com/dasjoms/jacobian-conjecture-counterexample-exploration?utm_source=openai)) |
| Mirror-equivariant first ansatz | **TAKEN† — July 20** | Giannini’s note gives a no-go theorem for its first mirror-equivariant plane class. ([zenodo.org](https://zenodo.org/records/21461572)) |
| \((72,108)\) plane frontier | **TAKEN† — July 21** | Helali published an exact computer-assisted exclusion, followed by independent proofs. This eliminates one specific frontier configuration; it does not prove \(\mathrm{JC}_2\). ([github.com](https://github.com/wstrinz/plane-jacobian-72-108)) |
| General proof that no version of the geometry can occur in dimension two | **UNCLAIMED** | Only the marked-root, graded, affine-linear and other bounded/mechanism-specific classes are excluded. |

So the intuition in your question has now been written down in several precise forms:

> The direct factorization/marked-root mechanism genuinely uses a third free coefficient.

But there is **no theorem that every possible plane counterexample would have to arise by that mechanism**. A genuinely non-toric, non-graded construction remains untouched.

---

# 5. Minimality and families

A crucial distinction is needed between:

- **total polynomial degree**, and
- **geometric degree**, the cardinality of a generic fiber.

Several new papers say “degree four” while meaning geometric degree four, not a quartic polynomial map.

| Question | Status | Answer |
|---|---|---|
| Is dimension \(3\) minimal? | **Least known dimension, not proved absolute minimum** | Dimension one is true; dimension two remains open; dimension three is the least dimension with a known counterexample. |
| Minimum generic-fiber degree | **TAKEN** | It is exactly \(3\). Degree \(2\) is Galois and forces invertibility; every geometric degree \(d\ge3\) now occurs in \(\mathbb C^3\). ([jacobiantheorems.com](https://jacobiantheorems.com/)) |
| Minimum total polynomial degree in all dimensions | **TAKEN** | Exactly \(3\): degree \(\le2\) Keller maps are invertible, while explicit degree-three examples now exist in higher dimension. ([agnt.gg](https://agnt.gg/whitepapers/machine-verified-corollary-mining-jacobian-conjecture.html)) |
| Minimum total polynomial degree in dimension \(3\) | **UNCLAIMED** | Alpöge has degree \(7\). Cubic counterexamples in dimension three are classically excluded, leaving the current range \(\boxed{4\le d_{\min}(3)\le7}\). No total-degree \(4,5,\) or \(6\) example or exclusion was found. ([rhicksrad.github.io](https://rhicksrad.github.io/jacobian-degree3/)) |
| Infinite families | **TAKEN — July 20 onward** | Gallagher produced examples of every geometric degree \(n\ge3\); generalized-weight factories and Gao’s tangent-sweep construction followed. ([arxiv.org](https://arxiv.org/abs/2608.00222)) |
| New genuinely higher-dimensional families | **TAKEN** | Gao gives nontrivial examples in dimensions \(4\) and \(5\), not merely identity stabilizations, and arbitrary large geometric degree in every \(n>2\). arXiv:2608.00222, submitted July 31. ([arxiv.org](https://arxiv.org/abs/2608.00222)) |
| Is Alpöge’s map rigid? | **PARTIAL / IN PROGRESS** | It is not globally isolated—the broad mechanism has many families. Capped first- and second-order deformation calculations suggest local rigidity modulo composition/equivariant moves at the founding example, but no uncapped global classification exists. ([jacobiantheorems.com](https://jacobiantheorems.com/)) |
| Fixed-total-degree moduli up to polynomial equivalence | **UNCLAIMED/PARTIAL** | The existence of families across fiber degrees is settled; a clean moduli classification at fixed total degree and fixed geometric degree is not. |

**Your “find a family” follow-up is already gone in the broad sense.** The sharper remaining question is classification: which families are equivalent, what are the moduli at fixed invariants, and are all three-dimensional examples tangent sweeps or twisted lifts?

---

# 6. Other downstream items

| Item | Status | Assessment |
|---|---|---|
| Canonical Poisson analogue of Dixmier | **TAKEN** | The same inverse-Jacobian construction gives an explicit nonautomorphic rank-three Poisson endomorphism. Public audits write it down directly. ([github.com](https://github.com/shadybrook/jacobian-counterexample-research/blob/main/paper/main.md)) |
| Hessian Conjecture | **TAKEN — July 24** | arXiv:2607.22198 gives an explicit five-variable counterexample. Current status: true for \(n\le3\), false for \(n\ge5\), open only for \(n=4\); \(\mathrm{HC}_4\Rightarrow\mathrm{JC}_2\). ([arxiv.org](https://arxiv.org/abs/2607.22198)) |
| Full fiber structure, \(S_3\) monodromy and nonproperness locus | **TAKEN** | Multiple same-week analyses found the inverse cubic, full \(S_3\) closure, exact missing/nonproperness loci and fiber census. ([arxiv.org](https://arxiv.org/abs/2608.00222)) |
| Tangent-sweep geometric explanation | **TAKEN — Speyer July 23; Gao July 31** | Gao’s arXiv paper gives a self-contained tangent-line/duality account and higher-dimensional generalization. ([arxiv.org](https://arxiv.org/abs/2608.00222)) |
| Formal verification of the base counterexample | **TAKEN** | Paul Lezeau’s Formal Conjectures PR #4474 proves a rescaled determinant-one form; independent Lean formalizations verify the original determinant \(-2\) map and full three-point fiber. ([ithub.global.ssl.fastly.net](https://ithub.global.ssl.fastly.net/jyh/jacobian-verify)) |
| Formalization in core mathlib | **NOT FOUND** | The work is in Formal Conjectures and standalone mathlib-based projects, not, from what I found, a theorem merged into core mathlib. |
| Formalization of the geometry/fiber classification | **UNCLAIMED** | Existing Lean artifacts certify determinant and collision, not the incidence geometry, monodromy, image or nonproperness analysis. |
| Tame versus wild automorphisms | **NOT IMPLICATED** | The counterexample is not an automorphism, so it is neither tame nor wild. Pre/post-composition by Nagata or another automorphism creates equivalent specimens but settles no tame/wild question. |
| Nagata automorphism | **NO NEW CONSEQUENCE FOUND** | Its known wildness is unaffected. A few repositories experiment with Nagata conjugation, but no new theorem was located. |
| Zariski cancellation | **NO DIRECT CONSEQUENCE FOUND** | No implication from the failed Jacobian statement to ordinary or Poisson cancellation was located. |
| LND/LNED/LFED conjectures | **NOT AUTOMATICALLY REFUTED** | They concern restricted classes of derivations or \(E\)-derivations. The full Image Conjecture’s failure does not by itself identify a locally nilpotent witness. No post-counterexample refutation was found. |
| Deformation quantization | **ONLY THE WEYL/POISSON LIFT IS TAKEN** | The explicit rank-three Poisson endomorphism and its Weyl quantization are concrete. No new consequence for existence/classification of star products or Kontsevich’s automorphism-group conjecture was located. |
| van den Essen monograph casualty audit | **UNCLAIMED** | No chapter-by-chapter audit of *Polynomial Automorphisms and the Jacobian Conjecture* was found. The obvious casualties are JC, same-rank Dixmier/Poisson in ranks \(\ge3\), and normal-form conjectures; many other statements are reductions or independent theorems and survive. |
| Characteristic-\(p\) analogues | **TAKEN, but separate** | arXiv:2608.02634 gives a dimension-two counterexample to a separable Jacobian formulation in characteristic two. This does not settle complex \(\mathrm{JC}_2\). ([arxiv.org](https://arxiv.org/abs/2608.02634)) |

---

# Requested venue audit

| Venue | What I found |
|---|---|
| **arXiv math.AC/AG/RA/QA** | Long on Gaussian moments; Shaska on graded maps; the five-variable Hessian counterexample; Gao’s general tangent-sweep construction; characteristic-two work, among others. |
| **Tao** | *A digestion of the Jacobian conjecture counterexample*, July 21. ([terrytao.wordpress.com](https://terrytao.wordpress.com/?blogsub=confirming)) |
| **Secret Blogging Seminar** | *The new counterexample to the Jacobian conjecture*, July 20; includes the same-rank \(A_3\) consequence. ([zenodo.org](https://zenodo.org/records/21514514)) |
| **Xena** | Kevin Buzzard’s immediate AI/formalization reaction, July 20. ([xenaproject.wordpress.com](https://xenaproject.wordpress.com/)) |
| **Scott Aaronson** | No indexed relevant post found through August 13. |
| **MathOverflow** | Same-day inverse cubic/\(S_3\) monodromy question; geometric-degree discussion; plane-frontier and stabilization questions. ([mathoverflow.net](https://mathoverflow.net/questions/513387/galois-structure-of-the-new-counterexample-to-the-jacobian-conjecture-an-explic)) |
| **n-Category Café** | No indexed Café post found. **nLab**, however, was updated July 22 with the counterexample and Dixmier discussion. ([ncatlab.org](https://ncatlab.org/nlab/show/Jacobian%20conjecture)) |
| **Mathstodon** | No reliably indexed public thread found. Decentralized/deleted posts cannot be excluded. |
| **DeepMind Formal Conjectures** | Paul Lezeau PR #4474: taken. ([ithub.global.ssl.fastly.net](https://ithub.global.ssl.fastly.net/jyh/jacobian-verify)) |
| **Lean Zulip** | Discussion is referenced, but I found no separately citable completed Weyl-algebra or full-geometry formalization there. |
| **Independent Lean repositories** | At least two: Grossi’s Zenodo artifact and Jason Hickey’s verbatim original-map verification. ([zenodo.org](https://zenodo.org/records/21514514)) |

---

# Ranking of the remaining projects

## By mathematical value

1. **Determine the minimum total degree in \(\mathbb C^3\)**  
   Find degree \(4,5,\) or \(6\), or exclude them. This is the cleanest new invariant question left by the example.

2. **Obtain a structure/classification theorem for three-dimensional Keller counterexamples**  
   Are all of them tangent sweeps/twisted torus lifts? Is the generic-degree spectrum theorem part of a complete classification?

3. **Push the plane obstructions beyond graded and marked-root mechanisms**  
   A theorem forcing any hypothetical \(\mathbb C^2\) counterexample into—or out of—one of these geometric classes would be major.

4. **Produce and optimize the explicit Drużkowski counterexample**  
   Less conceptually deep, but it closes the most famous classical reduction chain with an actual matrix.

5. **Find small explicit Zhao/Image witnesses**  
   Reduce the 48-variable Vanishing witness and produce an actual explicit Image-Conjecture MZ failure.

6. **Formalize the \(A_3\) Dixmier and Poisson counterexamples in Lean**  
   The polynomial part is done; the noncommutative lift is the conspicuous formal gap.

7. **Audit the van den Essen monograph and the broader implication graph**  
   Useful and citable, but mostly scholarship rather than new mathematics.

## By likelihood someone else takes it quickly

1. **Explicit Drużkowski matrix** — likely days to weeks.  
2. **Lean \(A_3\) Dixmier/Poisson formalization** — likely days to weeks.  
3. **Explicit Image-Conjecture witness from the 48-variable VC artifact** — likely weeks.  
4. **Chapter-by-chapter monograph casualty ledger** — could be done in days.  
5. **Dimension/rank optimization of cubic-homogeneous and Drużkowski maps** — active race, likely weeks to months.  
6. **Degree \(4\)–\(6\) search/exclusion in \(\mathbb C^3\)** — high competition, but substantially harder.  
7. **Global moduli/classification** — months or longer.  
8. **A genuinely general plane obstruction** — highest payoff, least likely to be settled quickly.

## My blunt recommendation

If you want a **fast priority claim**, do the **Drużkowski conversion immediately** and ship:

- the complete matrix \(A\);
- exact nilpotency/Keller certificates;
- explicit colliding points;
- a replay script in two independent CASs;
- dimensions/rank/sparsity comparisons against the 19-, 22-, 24- and 48-variable artifacts.

If you want the **best serious mathematics**, attack the dimension-three total-degree gap \(4,5,6\).

Do **not** spend time on:

- deriving \(A_2\) Dixmier from \(\neg\mathrm{JC}_4\)—that implication is invalid;
- merely producing “a cubic map”—already done;
- merely producing an infinite family—already done;
- merely observing Mathieu/Zhao/Image fallout—already done on July 20.