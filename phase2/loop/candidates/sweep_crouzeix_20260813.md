# Prior-art sweep — crouzeix (gpt-5.6-sol, effort=max, 2026-08-13 08:31)

> Counterexample-shaped target, selected after the Jacobian conjecture
> counterexample (Alpoge/Fable 5, 2026-07-20). Sweep asks BOTH whether the
> problem is already resolved AND where counterexample search is already dead.

# Adversarial prior-art report: Crouzeix’s conjecture  
**Cutoff: August 13, 2026**

## Axis checked

I checked the **scalar polynomial/holomorphic functional-calculus inequality in the spectral \(2\)-norm using the actual numerical range \(W(A)\)**.

I did **not** conflate it with:

- disk spectral-set inequalities for contractions, whose denominator is \(\sup_{\mathbb D}|p|\);
- the stronger complete/matrix-valued conjecture, except where a theorem proves it and hence also proves the scalar case;
- the “level-set Crouzeix conjecture” for compressed shifts, which tests a restricted class of Blaschke products;
- floating-point verification or approximate stationarity, which is evidence but not exclusion.

That distinction is important: several apparent “contraction” and “compressed-shift” results are on the wrong axis for your target.

---

# 1. STATUS: **OPEN**

## Main finding

Under the usual standard—an accepted or independently validated proof—**Crouzeix’s conjecture remains open as of August 13, 2026**.

I explicitly searched arXiv submissions from **August 13, 2024 through August 13, 2026**. The relevant recent papers I found were:

- Malman–Mashreghi–O’Loughlin–Ransford, *On the Crouzeix ratio for \(N\times N\) matrices*, arXiv:2409.14127;
- Schwenninger–de Vries, *The double-layer potential for spectral constants revisited*, arXiv:2409.15954;
- Crouzeix–Greenbaum, *A New Proof that the Numerical Range is a Complete 2-Spectral Set for Weighted Shift Matrices*, arXiv:2508.12768;
- Crouzeix, *Numerical Ranges and Spectral Sets: the unbounded case*, arXiv:2509.19792;
- Crouzeix, *Spectral estimates in the quantum annulus and in the numerical annulus*, arXiv:2512.11813;
- O’Loughlin–Rani, *\(q\)-Numerical Ranges and Spectral Sets*, arXiv:2603.15536.

None claims a generally accepted resolution; the March 2026 \(q\)-numerical-range paper still treats the original result as a conjecture. ([arxiv.org](https://arxiv.org/abs/2409.14127))

## Red alert: a six-day-old proof claim

There is, however, a **fresh non-arXiv proof claim that must be audited before spending compute**:

- Shanmu Jin, *The Numerical Range Is a 2-Spectral Set*, Preprints.org manuscript 202607.1919, version 4, posted **August 7, 2026**. It claims the full conjecture, including the holomorphic and spectral-set versions. The host explicitly labels it **not peer-reviewed**; as of the page snapshot it had no public comments. I found no independent validation, journal acceptance, or corresponding arXiv posting. I cannot certify or refute its central “positive-real completion theorem” from this prior-art pass. ([preprints.org](https://www.preprints.org/manuscript/202607.1919))

**Operational recommendation:** pause a large counterexample run until one or two specialists audit Jin’s completion theorem and the simple-spectrum approximation step. If correct, the target is dead.

## Earlier claimed proof that I do not count

Bee Rosa Davis’s March 12, 2026 Zenodo preprint also claims a proof. The argument described in its abstract only controls individual powers \(N^k\) using numerical-radius inequalities, not arbitrary sums \(\sum a_kN^k\); moreover, Schur decomposition \(T=D+N\) does not supply the claimed monotone comparison showing that nilpotents are extremal. Thus the stated steps do not imply the conjecture, and I do not count this as a resolution. ([zenodo.org](https://zenodo.org/records/18976016))

---

# 2. BEST PROVEN CONSTANT

Let

\[
\psi(A)=\sup_{p\ne0}
\frac{\|p(A)\|}{\max_{z\in W(A)}|p(z)|},
\qquad
C_*=\sup_A\psi(A).
\]

The current absolute bounds remain

\[
\boxed{2\le C_*\le 1+\sqrt2=2.414213562\ldots}.
\]

The upper bound is Crouzeix–Palencia, 2017. I found **no smaller explicit dimension-independent constant** established since then. ([arxiv.org](https://arxiv.org/abs/1702.00668))

Two later refinements must not be overstated:

1. For a fixed numerical-range domain \(\Omega\),

   \[
   K(\Omega)\le 1+\sqrt{1+a(\Omega)}<1+\sqrt2,
   \]

   where \(a(\Omega)<1\) is an analytic configuration constant. This gives a strict **domain-dependent** improvement, but there is no known universal gap \(\sup_\Omega a(\Omega)\le1-\varepsilon\). ([arxiv.org](https://arxiv.org/abs/2407.19049))

2. For every fixed matrix dimension \(N\), there exists a constant

   \[
   C_N<1+\sqrt2
   \]

   valid for all \(N\times N\) matrices. The proof is nonquantitative: it gives no useful numerical value even for \(C_3\). Since \(J_2\oplus0_{N-2}\) has ratio \(2\), one has \(2\le C_N<1+\sqrt2\) for every \(N\ge2\). ([arxiv.org](https://arxiv.org/abs/2409.14127))

Thus the answer to “has \(1+\sqrt2\) been improved?” is:

> **Pointwise and fixed-dimension: yes, strictly but non-explicitly.  
> As a published explicit universal absolute constant: no.**

---

# 3. WHERE COUNTEREXAMPLE SEARCH IS ALREADY DEAD

## 3.1 Theorem-level exclusions

| Region | Result | Exact stopping point |
|---|---|---|
| **Normal matrices** | Constant \(1\), by the spectral theorem. | All nonnormal matrices remain. |
| **All \(1\times1\) and \(2\times2\) matrices** | Constant \(2\). | A counterexample can first occur at \(n=3\). |
| **Minimal polynomial of degree \(\le2\)** | Safe in every dimension: compress to the cyclic space \(\operatorname{span}\{x,Ax\}\) generated by a norm-attaining vector and invoke the \(2\times2\) theorem. | Degree \(3\) is not safe in general. |
| **Matrices with disk numerical range** | The disk is a complete \(2\)-spectral set by the Okubo–Ando/Berger theory. | Merely being a contraction is not enough; the disk must be the relevant \(W(A)\). |
| **Jordan blocks \(J_n\)** | Safe for every \(n\), since \(W(J_n)\) is a disk. | Perturbations not belonging to the proved weighted-shift classes remain. |
| **Nilpotent weighted shifts** | Safe for every dimension; their numerical range is a centered disk. | General nilpotents are not weighted shifts. |
| **Scalar translates of cyclic weighted shifts / diagonally scaled perturbed Jordan blocks** | Proved by Choi; Crouzeix–Greenbaum gave a new proof of the stronger complete \(2\)-spectral-set statement in 2025. A standard form is \(aI+D^{-1}(J_n+\gamma e_ne_1^*)D\). | General banded, companion, or Hessenberg matrices are not covered. |
| **All \(3\times3\) nilpotent matrices** | Crouzeix, 2013. | Not all \(4\times4\) nilpotents. |
| **All matrices satisfying \((A-\lambda I)^3=0\)** | Consequence of the previous theorem: compress to \(\operatorname{span}\{x,(A-\lambda I)x,(A-\lambda I)^2x\}\). | Nilpotency index \(4\) is the first general open case. |
| **\(3\times3\) tridiagonal matrices with constant diagonal** | Complete constant \(2\); equivalently, \(3\times3\) matrices whose numerical range is an ellipse centered at an eigenvalue. | Not arbitrary \(3\times3\) tridiagonal matrices; not every elliptic numerical range. |
| **Diagonalizable \(A=V\Lambda V^{-1}\) with \(\kappa_2(V)\le2\)** | Trivial bound \(\|p(A)\|\le\kappa_2(V)\max_{\sigma(A)}|p|\le2\max_{W(A)}|p|\). | Ill-conditioned diagonalizations remain. |
| **Direct sums of safe blocks** | Safe, since \(W(A_1\oplus A_2)=\operatorname{conv}(W(A_1)\cup W(A_2))\). | A minimal counterexample must be unitarily irreducible. |
| **Unitary and affine closures** | The ratio is invariant under unitary similarity and nonconstant affine transformations \(A\mapsto\alpha A+\beta I\), with the polynomial transformed accordingly. | Normalize these symmetries out of any search. |

The \(2\times2\) and \(3\times3\)-nilpotent results go back to Crouzeix; the tridiagonal centered-ellipse result is due to Glader–Kurula–Lindström; the weighted-shift result is due to Choi, with the stronger 2025 proof by Crouzeix–Greenbaum. ([par.nsf.gov](https://par.nsf.gov/servlets/purl/10590073))

Bickel–Corbett–Glenning–Guan–Vollmayr-Lee also prove the full conjecture for several explicitly parametrized \(4\times4\) and \(5\times5\) nilpotent families in Section 3 of their 2024 paper. They do **not** prove it for every nilpotent matrix of those dimensions. ([arxiv.org](https://arxiv.org/abs/2312.04537))

### Important axis warning about their compressed-shift results

Much of that paper concerns the **level-set Crouzeix conjecture**, a weaker assertion for finite Blaschke products applied to model operators \(S_\Theta\). Those level-set theorems—including many \(3\times3\), \(4\times4\), and \(5\times5\) families—do **not** rule out failure of the full polynomial inequality for the same matrix. Only the paper’s explicitly stated full Crouzeix theorems belong in the exclusion list. ([arxiv.org](https://arxiv.org/abs/2312.04537))

## 3.2 What a minimal counterexample must look like

A minimal-dimension counterexample may be assumed to be:

- dimension \(n\ge3\);
- **cyclic**, hence with minimal polynomial of degree \(n\);
- **unitarily irreducible**;
- nonnormal;
- with nonempty, noncircular numerical range;
- with \(\sigma(A)\subset W(A)^\circ\).

The last condition follows because an eigenvalue on \(\partial W(A)\) creates a reducing decomposition. In minimal dimension, the smaller blocks would already satisfy the conjecture. For \(3\times3\), this means a counterexample cannot have any eigenvalue on the boundary of its numerical range. ([arxiv.org](https://arxiv.org/abs/2409.14127))

For \(n=3\), additional exclusions are:

- no minimal-polynomial degree \(\le2\);
- no scalar-plus-nilpotent case;
- no disk numerical range;
- no centered-ellipse case covered by Glader–Kurula–Lindström.

So the genuine first frontier is a **generic cyclic, irreducible \(3\times3\) matrix with interior spectrum and a smooth noncircular numerical range**.

## 3.3 Contractions and power-bounded matrices: not a safe region

A theorem for **all contractions** would be the full conjecture, not a special case. Given arbitrary \(A\), scale it to \(B=\varepsilon A\) with \(\|B\|<1\) and replace \(p\) by \(q(z)=p(z/\varepsilon)\); the Crouzeix ratio is unchanged. The same observation applies to strict contractions and hence power-bounded matrices.

Von Neumann’s inequality and the \(\rho\)-contraction literature use

\[
\sup_{|z|\le1}|p(z)|,
\]

not

\[
\sup_{z\in W(A)}|p(z)|.
\]

They exclude a counterexample only when the comparison disk actually equals the numerical range, or another separate argument relates the two suprema.

## 3.4 Exhaustive or computer-assisted exclusions

### What exists

- **The theorem \(n\le2\)** is the only complete all-matrices exclusion by dimension.
- Greenbaum–Overton’s 2018 search used Chebfun and BFGS and overwhelmingly converged to reciprocal ratio \(0.5\) or \(1\).
- Overton’s 2022 extension reports nearly **500,000 optimization runs** and about **250 million evaluated pairs \((p,A)\)**, with dimensions \(n=2,3,4,5,8,10\) and several polynomial degrees. The smallest reciprocal ratio was always \(0.5\), corresponding to target ratio \(2\), never below \(0.5\). ([arxiv.org](https://arxiv.org/abs/2105.14176))
- Crouzeix–Greenbaum–Li computed upper and lower numerical bounds for the four particular strictly-upper-triangular all-ones matrices \(A_n\), \(n=3,4,5,6\), and reported upper bounds consistent with \(\psi(A_n)\le2\). This is four fixed matrices, not all matrices of those dimensions. ([arxiv.org](https://arxiv.org/abs/2311.13890))
- Some compressed-shift papers use Mathematica to explore parameter intervals. Where the authors call the result “strong numerical evidence” or “suggests,” it is not an exclusion theorem; e.g. suggested ranges for certain \(n=6,7,8\) one-parameter families must not be treated as proved. ([degruyterbrill.com](https://www.degruyterbrill.com/document/doi/10.1515/conop-2024-0004/html?lang=en))

### What I did not find

I found **no**:

- exhaustive enumeration of all \(3\times3\) matrices;
- exhaustive search over a normalized parameter space;
- SAT/SMT encoding covering a nontrivial open region;
- published interval-arithmetic proof that all candidates in a box satisfy the bound;
- certified global optimization over matrix and Blaschke parameters;
- published statement of the form “all matrices below size \(N>2\) have been verified computationally.”

Therefore:

> **Compute below \(n=3\) is dead. Compute at generic \(n=3\) is not already exhausted.**

---

# 4. EXTREMAL AND NEAR-EXTREMAL EXAMPLES

## Exact equality is already known

The concern that numerical searches may plateau strictly below \(2\) is inapplicable globally: **ratio \(2\) is attained exactly**.

The simplest example is

\[
A=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad p(z)=z,
\]

for which \(\|A\|=1\) and \(W(A)\) is the disk of radius \(1/2\).

More generally, the \(n\times n\) Crabb weighted shift

\[
C_n=
\begin{pmatrix}
0&\sqrt2&&&\\
&0&1&&\\
&&\ddots&\ddots&\\
&&&0&\sqrt2\\
&&&&0
\end{pmatrix}
\quad(n\ge3),
\]

with \(C_2=\begin{pmatrix}0&2\\0&0\end{pmatrix}\), satisfies

\[
W(C_n)=\overline{\mathbb D},\qquad
\|C_n^{\,n-1}\|=2.
\]

Thus \(p(z)=z^{n-1}\) gives ratio exactly \(2\) in every dimension. These are unitarily irreducible equality examples, not merely \(2\times2\) direct sums. Overton’s optimization repeatedly recovers Crabb-type configurations. ([arxiv.org](https://arxiv.org/abs/2105.14176))

For the standard Jordan block \(J_n\), the single test \(p(z)=z^{n-1}\) gives

\[
\frac{\|J_n^{n-1}\|}
{\max_{z\in W(J_n)}|z|^{n-1}}
=
\sec^{\,n-1}\!\left(\frac{\pi}{n+1}\right).
\]

This equals \(2\) for \(n=2,3\), is about \(1.88854\) for \(n=4\), \(16/9\) for \(n=5\), and tends to \(1\). This is only the value for that monomial, not a formula for the full Crouzeix ratio of \(J_n\).

## Greenbaum–Overton numerical plateaus

Their optimization minimizes the reciprocal

\[
f(p,A)=\frac{\max_{W(A)}|p|}{\|p(A)\|}.
\]

Thus \(f=0.5\) means target ratio \(2\). Examples of recurrent local minima were:

| Dimension/degree | Reciprocal \(f\) | Target ratio \(1/f\) |
|---|---:|---:|
| \(n=2,m=3\) | \(0.500\) | \(2.000\) |
|  | \(0.713\) | \(1.403\) |
|  | \(0.844\) | \(1.185\) |
|  | \(1.000\) | \(1.000\) |
| \(n=3,m=3\) | \(0.500\) | \(2.000\) |
|  | \(0.698\) | \(1.433\) |
|  | \(0.844\) | \(1.185\) |
|  | \(0.977\) | \(1.024\) |
|  | \(1.000\) | \(1.000\) |

For \(n=4,5,8,10\), many additional local plateaus were found, but the best value remained \(f=0.5\). The searches did **not** display a global plateau below ratio \(2\); they repeatedly converged to exact equality configurations. ([arxiv.org](https://arxiv.org/abs/2105.14176))

This supports the conjecture, but it does not rule out a narrow basin with \(f<0.5\), especially near a nonsmooth equality manifold.

---

# 5. HAS ANYONE USED CERTIFIED/INTERVAL ARITHMETIC?

**I found no published certified interval-arithmetic search for Crouzeix’s conjecture.**

The principal numerical studies use:

- Chebfun approximations of \(\partial W(A)\);
- ordinary floating-point spectral computations;
- BFGS or related nonsmooth optimization;
- approximate subgradient/stationarity tests.

Overton used a BFGS stopping tolerance and approximate stationarity checks, not a proof-producing interval computation. ([arxiv.org](https://arxiv.org/abs/2105.14176))

The Crouzeix–Greenbaum–Li paper reports “numerical bounds” for four KLS matrices, but the accessible source did not expose an interval certificate or directed-rounding proof artifact. I therefore do not count it as a certified exhaustive search.

### Candidate verification is cheap—but not quite just one eigenvalue computation

For an explicit rational or interval matrix-polynomial pair:

- a lower bound for \(\|p(A)\|\) is obtained by certified eigenvalue isolation for \(p(A)^*p(A)\);
- an upper bound for \(\max_{W(A)}|p|\) requires certified global optimization on \(\partial W(A)\).

For smooth boundary pieces,

\[
h_A(\theta)=\lambda_{\max}\!\left(\operatorname{Re}(e^{-i\theta}A)\right)
\]

parametrizes the support lines, and interval eigensolvers can trace the corresponding boundary point. Eigenvalue crossings produce flat segments, where \(|p|^2\) becomes a one-variable polynomial optimization problem. This is still cheap for \(3\times3\) or \(4\times4\), but it is more than merely evaluating one matrix eigenvalue.

---

# 6. WHY IS THE CONJECTURE BELIEVED?

## A. Structural evidence

1. **The constant is forced to be at least \(2\)** by exact low-dimensional and Crabb examples; it was not reverse-engineered from a merely approximate numerical plateau.

2. The Crouzeix–Palencia proof constructs a positive symmetrized boundary calculus and loses the gap from \(2\) to \(1+\sqrt2\) in an abstract operator-norm decoupling step. This makes \(2\) look like the geometric mass naturally present in the double-layer representation, rather than an arbitrary guess. ([arxiv.org](https://arxiv.org/abs/1702.00668))

3. Configuration-constant refinements show that equality in the \(1+\sqrt2\) estimate is never attained for a fixed numerical range, and every fixed dimension has a strict improvement. This is evidence that simultaneous saturation of all inequalities in the general proof is geometrically impossible. ([arxiv.org](https://arxiv.org/abs/2407.19049))

4. The exact conjectured bound holds for disks, all \(2\times2\) matrices, low-index nilpotents, cyclic weighted shifts, and several nontrivial elliptic and compressed-shift classes.

## B. Empirical evidence

- The 2018 searches overwhelmingly found ratio \(2\) or much smaller values.
- The 2022 heavy-tailed search deliberately explored unusual basins and evaluated roughly 250 million pairs, again finding no value above \(2\).
- Family-specific computations and random-matrix investigations continue to support the bound. ([arxiv.org](https://arxiv.org/abs/2105.14176))

## Assessment

The belief is **not purely type (b)**—there is genuine operator-theoretic structure pointing to \(2\). But no known structural invariant presently forces the final inequality, and the numerical evidence is local rather than exhaustive.

My classification is:

> **A real mixture of (a) and (b), with more genuine type-(a) support than in a typical numerically motivated conjecture, but not enough to make a counterexample logically implausible.**

---

# 7. REFORMULATIONS AND REPRESENTATION SHIFTS

## 7.1 Spectral-set formulation

The conjecture says exactly that \(W(A)\) is a \(2\)-spectral set for \(A\):

\[
\|f(A)\|\le2\|f\|_{W(A)}
\]

for rational functions without poles on \(W(A)\), equivalently for suitable holomorphic functions by approximation.

The complete/matrix-valued form is stronger. When a special-case paper proves “complete \(2\)-spectral,” it genuinely excludes a scalar counterexample, but a merely scalar theorem should not automatically be upgraded.

## 7.2 Riemann-map and finite-Blaschke-product reduction

For fixed nonnormal \(A\) with \(W(A)^\circ\ne\varnothing\), choose a Riemann map

\[
\phi_A:W(A)^\circ\to\mathbb D.
\]

Then the optimization becomes an \(H^\infty(\mathbb D)\) functional-calculus problem for \(\phi_A(A)\). Standard finite-dimensional extremal theory allows the extremal disk function to be taken as a **finite Blaschke product of degree at most \(n-1\)**, with limits handling lower degree or degeneracy.

This is the best representation for a search:

\[
B(z)=e^{i\gamma}\prod_{j=1}^{n-1}
\frac{z-a_j}{1-\overline{a_j}z},
\qquad a_j\in\mathbb D,
\]

and evaluate \(\|B(\phi_A(A))\|\). The denominator is then normalized to \(1\), eliminating raw polynomial scaling and boundary maximization during the exploratory phase.

A strict violation for this holomorphic extremal can subsequently be approximated by a polynomial on \(W(A)\).

## 7.3 Cyclic reduction and differentiation operators

O’Loughlin–Virtanen show that it is sufficient to study cyclic matrices, and give an equivalent representation in terms of the differentiation operator on finite-dimensional spaces of entire functions. For \(3\times3\) symmetric matrices, they identify an equivalence with analytic truncated Toeplitz operators rather than a proof of the conjecture. ([arxiv.org](https://arxiv.org/abs/2306.12183))

This representation is conceptually useful, but cyclic matrices are open dense, so it does not drastically shrink the generic search space.

## 7.4 Compressions of shifts

Defect-one contractions are modelled by compressed shifts \(S_\Theta\), with \(\Theta\) a finite Blaschke product. This gives a low-dimensional parameterization and includes Jordan and perturbed-Jordan examples.

But:

- not every matrix is a defect-one compressed shift;
- the “level-set Crouzeix conjecture” is weaker than the full conjecture.

It is a good structured testbed, not a complete search parameterization. ([par.nsf.gov](https://par.nsf.gov/servlets/purl/10590073))

## 7.5 Double-layer/configuration-constant formulation

Crouzeix–Palencia and later work rewrite the problem using the positive double-layer boundary map, a Cauchy-transform companion, and the norm of an analytic Neumann–Poincaré-type operator. This is currently the most promising proof representation, but it does not convert the problem into a finite combinatorial search. ([arxiv.org](https://arxiv.org/abs/2407.19049))

## 7.6 Pick-matrix representation

For fixed \(A\), \(f(A)\) depends only on function values and derivatives at the eigenvalues, according to the Jordan structure. After mapping \(W(A)\) to \(\mathbb D\), feasibility of those interpolation jets with \(\|f\|_\infty\le1\) is a generalized Nevanlinna–Pick positivity condition.

This suggests a nested search:

1. matrix parameters for \(A\);
2. a finite positive-semidefinite Pick matrix describing admissible jets;
3. maximize the largest singular value of the corresponding \(f(A)\).

It is finite-dimensional for fixed \(n\), but not algebraic in \(A\), because \(\phi_A\) generally depends transcendently and nonsmoothly on the moving numerical range.

## 7.7 Dimension reduction from polynomial degree

If a polynomial \(p\) has degree \(d\) and \((A,p)\) is a strict counterexample, choose a norm-attaining vector \(x\) and restrict to

\[
\operatorname{span}\{x,Ax,\ldots,A^dx\}.
\]

This gives a cyclic counterexample of dimension at most \(d+1\).

There is, however, **no known universal polynomial-degree bound**. Reducing \(p\) modulo the minimal polynomial preserves \(p(A)\) but can increase \(\max_{W(A)}|p|\), so ordinary polynomials cannot simply be restricted to degree \(n-1\). The finite degree bound belongs to the Blaschke function after conformal mapping, not directly to the original polynomial.

---

# 8. REALISTIC SIZE OF THE SEARCH SPACE

For generic \(n\times n\) complex matrices:

- \(A\) has \(2n^2\) real parameters;
- unitary similarity removes \(n^2-1\);
- complex affine normalization removes another \(4\).

Thus the generic normalized matrix space has approximately

\[
n^2-3
\]

real parameters.

A degree-\((n-1)\) Blaschke product contributes \(2(n-1)\) real zero parameters; its unimodular prefactor does not affect the norm. The resulting approximate search dimensions are therefore

\[
n^2+2n-5:
\]

| \(n\) | Approximate real dimension |
|---:|---:|
| 3 | 10 |
| 4 | 19 |
| 5 | 30 |

This makes a serious \(3\times3\) global search plausible. It is not a huge combinatorial problem; it is a moderately sized continuous, nonsmooth global optimization problem.

The obstacle is that every evaluation may require:

- constructing or approximating \(\partial W(A)\);
- computing a conformal map;
- evaluating a matrix function;
- navigating eigenvalue crossings and equality manifolds.

No finite rational grid or separation bound is known: a hypothetical violation could exceed \(2\) by an arbitrarily small amount.

---

# 9. RELATED FALSE ANALOGUES AND HARD CASES

## Banach-space analogue is false

For general Banach algebras and algebraic numerical ranges, no universal finite spectral constant exists in broad classes; Blazhko–Homza–Schwenninger–de Vries–Wojtylak construct counterexamples, including shift-type examples. This does **not** transfer to the Hilbert-space spectral norm, but it confirms that Hilbert geometry is essential rather than cosmetic. ([cambridge.org](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/96536D155B032F6C67B750582F5DBF07/S0008414X25000124a.pdf/algebraic_numerical_range_as_a_spectral_set_in_banach_algebras.pdf))

## Hard numerical region

The easy attractors in Greenbaum–Overton are:

- disk numerical ranges and Crabb configurations at ratio \(2\);
- corners or “ice-cream-cone” ranges near ratio \(1\);
- approximately block-diagonal configurations.

The genuinely hard target is likely a smooth, nonelliptic, unitarily irreducible numerical range with several competing boundary maximizers of the extremal function. That is precisely where the objective is most nonsmooth and where local BFGS searches can miss a narrow basin.

## Equality classification remains informative

Exact equality occurs in many dimensions, but classification of all equality cases is not settled. Searching for new equality families can still be useful: a bifurcation away from an equality manifold is a natural place for a ratio \(>2\) to emerge.

---

# 10. WHO IS ACTIVELY WORKING ON IT?

Recent work indicates active participation by:

- **Michel Crouzeix and Anne Greenbaum** — weighted shifts and numerical special families;
- **Bartosz Malman, Javad Mashreghi, Ryan O’Loughlin, Thomas Ransford** — configuration constants, continuity and fixed-dimensional bounds;
- **Felix Schwenninger and Jens de Vries** — double-layer potentials and abstract spectral constants;
- **Kelly Bickel, Pamela Gorkin, and collaborators** — finite Blaschke products, compressed shifts and nilpotent classes;
- **Jani Virtanen** — cyclicity and differentiation-operator reformulations;
- **Michael Overton** — the largest public nonsmooth-optimization studies, though I found no evidence of a currently running 2026 campaign.

The 2025 paper *Mathematical exploration and discovery at scale* by Bogdan Georgiev et al. includes a Crouzeix optimization experiment using **AlphaEvolve**, explicitly aimed at improving the known lower bound \(2\). Thus an AI-guided evolutionary search has already been attempted. The public material I could reach did not provide enough detail to audit the Crouzeix-specific run budget or determine whether an ongoing search remains active. ([arxiv.org](https://arxiv.org/abs/2511.02864))

I found **no public evidence of a currently running interval-certified or formally exhaustive project** with a disclosed compute budget larger than yours.

---

# 11. TRACTABILITY CALL

## Verification

A candidate counterexample really is a small, cheaply certifiable object. For \(3\times3\) or \(4\times4\) rational/interval data, rigorous verification should be inexpensive compared with finding it.

## Search

A raw random search is unattractive:

- 250 million prior floating-point evaluations found nothing above \(2\);
- exact equality manifolds attract local optimization;
- the original polynomial degree is unbounded;
- the objective is nonsmooth at precisely the interesting configurations.

But a representation-shifted search is not hopeless:

1. **First audit Jin’s August 2026 proof claim.**
2. Start at **generic \(3\times3\)** only.
3. Enforce cyclicity, irreducibility, interior spectrum and noncircular \(W(A)\).
4. Normalize unitary and affine symmetries.
5. Search in **Riemann-map plus degree-\(\le2\) Blaschke coordinates**, not raw polynomial coefficients.
6. Use floating point only to locate candidates, followed immediately by interval certification.
7. If feasible, branch-and-bound the roughly ten-dimensional normalized \(n=3\) space; that would be genuinely new prior art even if it only excludes a substantial compact region.

## Single biggest obstacle

The biggest obstacle is **global coverage**, not candidate verification: there is no known finite algebraic parameterization with a uniform separation margin, and the conformal map of a moving numerical range makes interval branch-and-bound technically difficult near eigenvalue crossings and degeneracies.

My call is therefore **MARGINAL** rather than hopeless: the first open dimension is genuinely small and no certified exhaustive search exists, but extensive floating-point searches plus substantial structural evidence make a counterexample unlikely.

---

# Search coverage and limitations

I searched:

- arXiv explicitly for 2024–2026 Crouzeix submissions;
- recent arXiv papers citing the current constant;
- SIAM, ScienceDirect, Springer/De Gruyter and Cambridge abstracts or author manuscripts;
- Overton’s publication/code page and Optimization Online manuscripts;
- Preprints.org and Zenodo for recent proof claims;
- terms including “interval arithmetic,” “certified,” “exhaustive computation,” “numerical optimization,” “Crouzeix ratio,” and “counterexample.”

I could not directly audit closed MathSciNet, Scopus or Web of Science indexes. Some SIAM/ScienceDirect full versions were paywalled, although arXiv or author copies were generally available. I could not recover the detailed numerical table from the KLS-matrix paper or the Crouzeix-specific AlphaEvolve run log, so I have not invented those numbers.

---

# Key references

1. **Michel Crouzeix and César Palencia**, “The Numerical Range is a \((1+\sqrt2)\)-Spectral Set,” *SIAM Journal on Matrix Analysis and Applications* 38(2), 649–655, 2017.  
   arXiv:1702.00668. DOI: 10.1137/17M1116672.  
   URL: https://arxiv.org/abs/1702.00668

2. **Bartosz Malman, Javad Mashreghi, Ryan O’Loughlin, Thomas Ransford**, “On the Crouzeix ratio for \(N\times N\) matrices,” 2024 preprint.  
   arXiv:2409.14127. DOI: 10.48550/arXiv.2409.14127.  
   URL: https://arxiv.org/abs/2409.14127

3. **Bartosz Malman, Javad Mashreghi, Ryan O’Loughlin, Thomas Ransford**, “Double-Layer Potentials, Configuration Constants, and Applications to Numerical Ranges,” *International Mathematics Research Notices* 2025(8), rnaf084, 2025.  
   arXiv:2407.19049. DOI: 10.1093/imrn/rnaf084.  
   URL: https://arxiv.org/abs/2407.19049

4. **Michel Crouzeix**, “Bounds for Analytical Functions of Matrices,” *Integral Equations and Operator Theory* 48(4), 461–477, 2004.  
   No arXiv. DOI was not exposed by the accessible record used here.

5. **Michel Crouzeix**, “Numerical Range and Functional Calculus in Hilbert Space,” *Journal of Functional Analysis* 244(2), 668–690, 2007.  
   DOI: 10.1016/j.jfa.2006.10.013.

6. **Michel Crouzeix**, “Spectral Sets and \(3\times3\) Nilpotent Matrices,” in *Topics in Functional and Harmonic Analysis*, Theta Series in Advanced Mathematics 14, 27–42, 2013.  
   No arXiv/DOI located.

7. **Daeshik Choi**, “A Proof of Crouzeix’s Conjecture for a Class of Matrices,” *Linear Algebra and its Applications* 438(8), 3247–3257, 2013.  
   DOI not recovered from the accessible record.

8. **Michel Crouzeix and Anne Greenbaum**, “A New Proof that the Numerical Range is a Complete 2-Spectral Set for Weighted Shift Matrices,” 2025 preprint.  
   arXiv:2508.12768. DOI: 10.48550/arXiv.2508.12768.  
   URL: https://arxiv.org/abs/2508.12768

9. **Christer Glader, Mikael Kurula, Mikael Lindström**, “Crouzeix’s Conjecture Holds for Tridiagonal \(3\times3\) Matrices with Elliptic Numerical Range Centered at an Eigenvalue,” *SIAM Journal on Matrix Analysis and Applications* 39(1), 346–364, 2018.  
   arXiv:1701.01365. DOI: 10.1137/17M1110663.  
   URL: https://arxiv.org/abs/1701.01365

10. **Ryan O’Loughlin and Jani Virtanen**, “Crouzeix’s Conjecture for Classes of Matrices,” *Linear Algebra and its Applications* 697, 277–292, 2024.  
    arXiv:2306.12183. DOI: 10.1016/j.laa.2023.12.008.  
    URL: https://arxiv.org/abs/2306.12183

11. **Kelly Bickel, Georgia Corbett, Annie Glenning, Changkun Guan, Martin Vollmayr-Lee**, “Crouzeix’s Conjecture, Compressions of Shifts, and Classes of Nilpotent Matrices,” *Concrete Operators* 11(1), Article 20240004, 2024.  
    arXiv:2312.04537. DOI: 10.1515/conop-2024-0004.  
    URL: https://arxiv.org/abs/2312.04537

12. **Anne Greenbaum and Michael L. Overton**, “Numerical Investigation of Crouzeix’s Conjecture,” *Linear Algebra and its Applications* 542, 225–245, 2018.  
    URL: https://optimization-online.org/wp-content/uploads/2016/11/5703.pdf

13. **Michael L. Overton**, “Local Minimizers of the Crouzeix Ratio: A Nonsmooth Optimization Case Study,” *Calcolo* 59, Article 8, 2022.  
    arXiv:2105.14176. DOI: 10.1007/s10092-021-00448-z.  
    URL: https://arxiv.org/abs/2105.14176

14. **Michel Crouzeix, Anne Greenbaum, Kenan Li**, “Numerical Bounds on the Crouzeix Ratio for a Class of Matrices,” 2023 preprint.  
    arXiv:2311.13890. DOI: 10.48550/arXiv.2311.13890.  
    URL: https://arxiv.org/abs/2311.13890

15. **Felix L. Schwenninger and Jens de Vries**, “The Double-Layer Potential for Spectral Constants Revisited,” *Integral Equations and Operator Theory* 97, Article 13, 2025.  
    arXiv:2409.15954. DOI: 10.48550/arXiv.2409.15954.  
    URL: https://arxiv.org/abs/2409.15954

16. **Hanna Blazhko, David Homza, Felix L. Schwenninger, Jens de Vries, Michał Wojtylak**, “The Algebraic Numerical Range as a Spectral Set in Banach Algebras,” *Canadian Journal of Mathematics*, online 2025.  
    DOI: 10.4153/S0008414X25000124.  
    URL: https://doi.org/10.4153/S0008414X25000124

17. **Ryan O’Loughlin and Jyoti Rani**, “\(q\)-Numerical Ranges and Spectral Sets,” 2026 preprint.  
    arXiv:2603.15536. DOI: 10.48550/arXiv.2603.15536.  
    URL: https://arxiv.org/abs/2603.15536

18. **Bogdan Georgiev et al.**, “Mathematical Exploration and Discovery at Scale,” 2025 preprint.  
    arXiv:2511.02864. DOI: 10.48550/arXiv.2511.02864.  
    URL: https://arxiv.org/abs/2511.02864

19. **Shanmu Jin**, “The Numerical Range Is a 2-Spectral Set,” version 4, Preprints.org, August 7, 2026; not peer-reviewed.  
    URL: https://www.preprints.org/manuscript/202607.1919

20. **Bee Rosa Davis**, “The Crouzeix Conjecture: Shift Extremality and the Curvature Budget,” Zenodo preprint, March 12, 2026.  
    DOI: 10.5281/zenodo.18976016.  
    URL: https://doi.org/10.5281/zenodo.18976016

# VERDICT: OPEN | MARGINAL

A counterexample could already occur in a roughly ten-real-dimensional normalized \(3\times3\) search, and no certified exhaustive search of that space exists, so the object is genuinely small and verifiable. However, the fresh August 2026 proof claim must be audited first, and the combination of exact extremizers, strong operator-theoretic structure, and roughly 250 million unsuccessful floating-point trials makes undirected compute unlikely to pay off.