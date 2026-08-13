# Prior-art sweep — lonely_runner (gpt-5.6-sol, effort=max, 2026-08-13 08:29)

> Counterexample-shaped target, selected after the Jacobian conjecture
> counterexample (Alpoge/Fable 5, 2026-07-20). Sweep asks BOTH whether the
> problem is already resolved AND where counterexample search is already dead.

# Bottom line

**STATUS as of August 13, 2026: OPEN.**

Your “proved through 7 runners; 8 is open” belief is now substantially out of date. The current proof record is:

- **8 runners:** Rosenfeld, September 2025.
- **9 and 10 runners:** Trakulthongchai, November 2025; Rosenfeld independently proved 9 runners in December 2025.
- **11, 12 and 13 runners:** Sungkawichai–Trakulthongchai, April 2026.

Therefore, in your convention, the conjecture is proved through **13 total runners**, i.e. through **12 positive relative speeds**. The **smallest open case is 14 total runners**, corresponding to **13 speeds** and target distance \(1/14\). ([arxiv.org](https://arxiv.org/abs/2509.14111))

**Provenance warning:** the 11–13-runner result is presently an arXiv computer-assisted preprint, submitted April 26, 2026. I found no withdrawal or correction, and its code and logs are public, but I did not find journal metadata for it and did not independently rerun the computation. For prior-art allocation I would treat \(n\leq13\) as dead, while separately flagging \(n=11,12,13\) as “preprint-proved/computer-assisted” rather than formally verified. ([arxiv.org](https://arxiv.org/abs/2604.23906))

## Axis audit

I checked the following axis:

- **Ordinary Lonely Runner Conjecture:** all runners start together and have constant speeds.
- **Runner convention:** your \(n\) is total runners; much of the literature writes \(k\) for the number of nonzero relative speeds, so \(n=k+1\).
- **Finite-case frontier:** ordinary LRC, not the shifted, spectrum, function-field or time-dependent variants.
- **Computational scope:** whether papers enumerate speed vectors up to a coordinate bound versus exhaust finite modular residue/sieve instances.
- **Finite-reduction axis:** the hypothesis removed is “arbitrarily large speeds,” via a bound on a normalized minimal counterexample.

I did **not** conflate these with:

- **Shifted LRC**, where runners have different starting phases; this is now false in general.
- **Loneliness Spectrum Conjecture**, also false in its original form.
- **Time-dependent velocities**, which is a different and much less rigid problem.
- The graph-flow consequence of LRC, which is not an equivalent counterexample parametrization.

Also note an important symmetry distinction: adding a constant to **all original runner speeds** is a symmetry, but after fixing one runner at speed zero, adding a constant only to the listed relative speeds is **not known** to preserve the instance. Dilation and sign changes are safe; translation in the stationary formulation is not. ([arxiv.org](https://arxiv.org/html/2409.20160))

---

# 1. STATUS AND THE RECENT arXiv CHECK

I explicitly checked arXiv work from the last 24 months, through August 13, 2026. The status-changing papers are:

| Date | Result |
|---|---|
| Sep. 17, 2025 | Matthieu Rosenfeld proves **8 runners**. |
| Nov. 27, 2025 | Tanupat Trakulthongchai proves **9 and 10 runners**. |
| Dec. 1, 2025 | Rosenfeld gives an independent proof for **9 runners**. |
| Apr. 26, 2026 | Touch Sungkawichai and Trakulthongchai prove **11, 12 and 13 runners**. |

No arXiv paper through August 13, 2026 that I found proves 14 runners, gives a full proof, or supplies a counterexample. The May 2026 “mixed thresholds” paper and July 2026 time-dependent-velocity paper do not change the ordinary LRC frontier. ([arxiv.org](https://arxiv.org/abs/2509.14111))

Thus:

\[
\boxed{\text{smallest open total runner count}=14}
\]

and the counterexample object to search for is a normalized set

\[
0<v_1<\cdots<v_{13},\qquad \gcd(v_1,\ldots,v_{13})=1,
\]

with

\[
\max_t\min_i\|tv_i\|<\frac1{14}.
\]

Equality \(=1/14\) is only a tight example, not a counterexample.

---

# 2. WHERE COUNTEREXAMPLE SEARCH IS ALREADY DEAD

## 2.1 Entire runner counts

All integer or real speed vectors are ruled out for:

\[
n\leq13\quad\text{total runners}.
\]

This is much stronger than an exhaustive check up to a speed bound. Do not spend counterexample compute on 8, 9, 10, 11, 12 or 13 runners except as an independent audit of the computer-assisted proofs. ([arxiv.org](https://arxiv.org/abs/2509.14111))

## 2.2 Integer speeds are without loss of generality

Yes. The real-speed formulation reduces to rational and then integer speeds, using Kronecker-type approximation together with dimension reduction. This does **not** say that every real vector is a scalar multiple of an integer vector; rather, a failure over the reals would yield a failure in a rational/integer lower-dimensional or same-dimensional instance. Signs may be removed because \(\|t(-v)\|=\|tv\|\), and a minimal counterexample can be assumed to have distinct positive absolute speeds. ([arxiv.org](https://arxiv.org/html/2409.20160))

Dilation is an exact symmetry, so a minimal integer counterexample may be normalized to

\[
\gcd(v_1,\ldots,v_k)=1.
\]

## 2.3 There is now an explicit finite bound for a minimal 14-runner counterexample

Malikiosis, Santos and Schymura proved the decisive finite-reduction theorem. For \(k\) nonzero speeds, assuming the \(k\)-runner lower case, a normalized counterexample must satisfy

\[
G(V):=\sum_{S\subseteq[k]}\gcd(v_i:i\in S)
\leq \binom{k+1}{2}^{k-1},
\]

with the empty-set term understood as zero. In particular,

\[
\sum_i v_i\leq \binom{k+1}{2}^{k-1},
\qquad
\max_i v_i\leq \binom{k+1}{2}^{k-1}.
\]

This improves Tao’s earlier \(k^{O(k^2)}\) bound to roughly \(k^{2k}\). ([arxiv.org](https://arxiv.org/html/2411.06903))

For the first open case, \(k=13\):

\[
\boxed{
\sum_{i=1}^{13}v_i
\leq
\binom{14}{2}^{12}
=
91^{12}
=
322{,}475{,}487{,}413{,}604{,}782{,}665{,}681
}
\]

and hence every speed is at most approximately \(3.225\times10^{23}\).

The product corollary used by all recent computer proofs gives

\[
\prod_{i=1}^{13}v_i
<
\left(\frac{91^{12}}{13}\right)^{13}
\approx 1.35\times10^{291}.
\]

So the 14-runner case is a genuinely finite search—but not remotely a direct-enumeration-sized one. The rough number of unordered positive 13-tuples under the sum bound is on the order of

\[
\frac{(91^{12})^{13}}{(13!)^2}\approx 10^{286},
\]

before useful structural pruning. ([arxiv.org](https://arxiv.org/html/2509.14111))

## 2.4 Elementary arithmetic exclusions for any 14-runner counterexample

Rosenfeld’s lemmas imply that a normalized \(k\)-speed counterexample must satisfy:

1. **Every \((k-1)\)-subset has gcd one.**  
   If all but one speed share a nontrivial common divisor, the lower-dimensional LRC plus a “pre-jump” argument supplies a witness.

2. **For every \(j=2,\ldots,k+1\), at least one speed is divisible by \(j\).**  
   Otherwise \(t=1/j\) is already a witness.

Consequently, for 14 runners,

\[
\operatorname{lcm}(2,3,\ldots,14)=360360
\]

must divide \(\prod_i v_i\), and every 12-element subset of the 13 speeds must be primitive. ([arxiv.org](https://arxiv.org/html/2509.14111))

These conditions are weak compared with the recent prime sieves, but they are nearly free pruning rules.

## 2.5 Deterministic special families already ruled out

Using \(k\) for the number of moving speeds:

- **Lacunary sets:** if \(v_{i+1}\geq2v_i\) for every \(i\), LRC holds for every \(k\).
- For sufficiently large \(k\), much weaker growth,
  \[
  v_{i+1}\geq\left(1+\frac{22\log k}{k}\right)v_i,
  \]
  suffices; related spaced-growth criteria apply for \(k\geq32\).
- **Arithmetic progressions:** all arithmetic progressions satisfy LRC, with explicit stronger bounds.
- More generally, any \(k\)-set contained in an arithmetic progression of length at most \(2k-3\), other than the exceptional ambient progression beginning at 1 with difference 1, is covered by Pandey’s theorem.
- Exact formulas are known for several “dense interval with holes” families, including \([m]\) with an arithmetic progression or a suitable interval removed. ([arxiv.org](https://arxiv.org/html/2409.20160))

For the 14-runner search, this means all 13-speed subsets of nontrivial arithmetic progressions of length at most \(23\), all 2-lacunary sets, and numerous dense near-interval families are dead.

Random vectors are not a deterministic exclusion, but they are a terrible place to hunt: for fixed \(k\), a random \(k\)-subset of \([N]\) has loneliness gap tending to \(1/2\), not \(1/(k+1)\), as \(N\to\infty\). Any counterexample should therefore be highly arithmetically structured. ([arxiv.org](https://arxiv.org/html/2409.20160))

## 2.6 What the recent exhaustive computations actually checked

They did **not** enumerate all speed sets with \(\max v_i\leq N\). Instead they combined:

1. the finite product bound above;
2. exact exhaustive searches over residue tuples modulo \((k+1)p\), often with intermediate lifts;
3. a theorem saying that emptiness of a certain modular bad-set forces \(p\mid\prod_i v_i\);
4. enough forced prime divisors to make the product exceed its theoretical upper bound.

Thus each result excludes **all integer speeds**, not merely a coordinate box.

### Quantitative record

| Total runners | Moving speeds \(k\) | Computational certificate |
|---:|---:|---|
| 8 | 7 | Rosenfeld showed \(\prod v_i<7.4\times10^{54}\). Exact backtracking verified the relevant modular cover condition for \(p=31,37,43,\ldots,163\); together with \(\operatorname{lcm}(2,\ldots,8)\), the forced divisor is about \(1.82\times10^{55}\), a contradiction. |
| 9 | 8 | Trakulthongchai used a multilevel modular sieve; Rosenfeld supplied an independent prime-power sieve. The generic product ceiling is \(C_8<10^{80}\). |
| 10 | 9 | Trakulthongchai used the explicit lift sequence \(1\to2,5\to10\). The product ceiling is \(C_9<10^{111}\). |
| 11 | 10 | Sungkawichai–Trakulthongchai’s refined solver completed this case in about **45 minutes** on a 10-core Apple M4. |
| 12 | 11 | Computation was split over machines and versions; the paper’s normalized estimate is approximately **40 hours** on the same 10-core machine. |
| 13 | 12 | Normalized estimate approximately **40 days** on the same machine. The exact prime sets are in Table 1 and extend into the 700s. |

The latest implementation reproduces \(k=8\) in 2 seconds rather than 15 minutes and \(k=9\) in 41 seconds rather than 23 hours. Source, logs and exact arithmetic certificates are linked from the 2026 paper. ([arxiv.org](https://arxiv.org/html/2509.14111))

For Rosenfeld’s independent nine-runner proof, the checked moduli include a power of every prime at most 191 other than 7; for example, the more expensive displayed runs include \(25\) at 5,974 seconds, \(64\) at 4,115 seconds and \(127\) at 15,367 seconds. ([arxiv.org](https://arxiv.org/html/2512.01912))

### Direct answer to the critical bound question

**I found no published ordinary-LRC computation giving a theorem of the form “all 13-speed vectors with \(\max v_i\leq N\) have been exhaustively checked” for the open 14-runner case.**

The existing record computations are modular global proofs for \(n\leq13\), not reusable lower bounds on the maximum speed of a 14-runner counterexample. I also found no published SAT search with a nontrivial complete coordinate cutoff for 14 runners. The public nonacademic site `https://lonelyrunner.fun/` reports bounded 14-runner probes and exact-rational logs, but its indexed page states no theorem-level exhaustive cutoff \(N\). ([lonelyrunner.fun](https://lonelyrunner.fun/))

## 2.7 Related but different computation

For the **shifted** LRC with four moving speeds, Alcántara, Criado and Santos exhaustively checked **2,133,561** relevant 3-dimensional shifted-LR zonotopes after reducing to total speed at most 195. This proves that shifted case and identifies exactly three shifted-tight vectors:

\[
(1,2,3,4),\quad(1,3,4,7),\quad(1,3,4,6).
\]

The last is tight only in the shifted problem. This is a useful demonstration of a fully auditable finite zonotope enumeration, but it is not a coordinate bound for ordinary 14-runner LRC. ([arxiv.org](https://arxiv.org/html/2411.06903))

---

# 3. WHY IS IT BELIEVED?

## Type (a): structural evidence

There is significant genuine structural evidence:

- The conjectured constant is sharp because \(\{1,2,\ldots,k\}\) has gap exactly \(1/(k+1)\).
- Counterexamples reduce to finite, primitive integer vectors.
- Both major extremes are understood: compressed/dense/AP-like sets and rapidly growing/lacunary sets satisfy LRC.
- Random sets satisfy a vastly stronger bound, close to \(1/2\).
- Known exact extremals form arithmetic families rather than isolated numerical accidents.
- The recent prime sieves show that a counterexample must obey an increasingly rigid collection of incompatible divisibility conditions.
- The zonotope proof reduces high-volume instances to lower dimension, giving a genuine inductive geometric mechanism rather than merely a search result. ([arxiv.org](https://arxiv.org/html/2409.20160))

## Type (b): computational evidence

The proofs for 8–13 runners are heavily computational. They do not amount to “we sampled a lot and saw nothing”; they are exhaustive finite certificates inside a theorem. Nevertheless, their success is evidence only for finitely many dimensions, and the algorithmic workload grows quickly. ([arxiv.org](https://arxiv.org/html/2604.23906))

## Honest assessment

The belief is **mixed but predominantly structural**, not merely type (b). However, there is no known global invariant forcing the required overlaps among the forbidden time intervals. The best general asymptotic gap is still only slightly above the trivial \(1/(2k)\), roughly half the conjectured \(1/(k+1)\), so present general theory remains far from the target. ([arxiv.org](https://arxiv.org/html/2411.06903))

Two cautionary facts matter:

1. The original Loneliness Spectrum Conjecture—an attractive rigidity prediction about values near the threshold—was false.
2. The shifted LRC, a natural robustness extension allowing different initial positions, is false in general as of 2026.

So this is not a case where every nearby generalization reinforces the conjecture.

---

# 4. REFORMULATIONS AND REPRESENTATION SHIFTS

| Formulation | Exact status | Search value |
|---|---|---|
| **One-dimensional optimization** \(\kappa(V)=\max_t\min_i\|tv_i\|\) | Equivalent | Best for evaluating/scoring a proposed vector. Exact maxima occur at rational breakpoints \(t=\ell/(v_i+v_j)\). |
| **Discrete modular form** \(\kappa_N(V)\) | Equivalent via a finite maximum over \(N=v_i+v_j\) | Best current basis for exact backtracking, SAT/CP-SAT or set-cover search. |
| **Cusick view obstruction** | Equivalent | Geometric intuition: a ray must hit a periodic array of centered cubes. Less convenient for raw enumeration. |
| **Billiard trajectory in a cube** | Equivalent | Visualization and shifted variants; not presently the best counterexample representation. |
| **Lonely-runner polyhedron** | Equivalent integer-point problem for a fixed speed vector | Potential MILP/lattice formulation, but coefficients grow with speeds. |
| **Lattice zonotope/covering radius** | Equivalent | Best for finite bounds, dimension reduction and classification up to unimodular equivalence. |
| **Volume vector/Gale duality** | Equivalent for LR zonotopes | Parametrizes normalized speed vectors as the unique integer dependence among zonotope generators. Useful for structural generation, but high-dimensional equivalence testing is expensive. |
| **Circulant/distance graph colouring** | Closely connected; used in the seven-runner proof | Natural SAT/graph-colouring encoding, but current record computations are faster in modular-cover form. |
| **Nowhere-zero flows** | Consequence/application, not a full equivalence | Wrong axis for direct counterexample search. |
| **Fourier/Bohr-set/Riesz-product methods** | Analytic reformulations and bounds | Strong for random, lacunary and asymptotic cases; weak for enumerating a single finite counterexample. |

The exact one-dimensional formula implies that a fixed \(V\) can be verified in \(O(k^2v_{\max})\) arithmetic operations by the direct method. This is polynomial in the numerical speeds but only pseudopolynomial in their bit length. At the theoretical 14-runner bound, \(v_{\max}\) can be \(3\times10^{23}\), so “compact one-dimensional optimization” does **not** automatically mean cheap worst-case verification. ([arxiv.org](https://arxiv.org/html/2409.20160))

The view-obstruction, billiard, graph-flow and zonotope formulations are summarized in the recent survey; the flow result of Bienia–Goddyn–Gvozdjak–Sebő–Tarsi is an implication from LRC to a bounded-value flow theorem, not an equivalence that parametrizes all possible speed counterexamples. ([arxiv.org](https://arxiv.org/html/2409.20160))

## Best representation for a machine search

I would use a hybrid:

1. **Outer exact search:** modular residue classes and lifted “proper/improper” tuples, represented as bitsets or SAT/set-cover clauses.
2. **Symmetry quotient:** sort speeds; enforce gcd one; quotient signs, permutations and multiplication by units modulo the active modulus.
3. **Heuristic seed generator:** mutate known tight speed sets and modular orbits surviving the first sieve.
4. **Exact candidate scorer:** compute \(\kappa(V)\) from rational breakpoints.
5. **Geometric pruning:** use the sum-of-gcd/zonotope volume bound and, where practical, classify low-width or highly structured zonotopes.

This closely follows the only approach that has scaled from seven to thirteen runners. Direct coordinate enumeration is several hundred orders of magnitude too large.

## The new 2026 algebraic sieve and its limitation at 14 runners

Sungkawichai–Trakulthongchai prove that if both \(k+1\) and \(p>k^2+k\) are odd primes, then any normalized tuple satisfying

\[
(v_1,\ldots,v_k)\equiv(1,2,\ldots,k)\pmod p
\]

already has the LR property. This removes the modular orbit corresponding to the standard tight tuple, which had survived earlier sieves. ([arxiv.org](https://arxiv.org/html/2604.23906))

But for the first open case \(k=13\),

\[
k+1=14
\]

is not prime. Therefore this polynomial theorem does **not** directly dispose of the 14-runner hard orbit. The 2026 paper explicitly identifies computing the initial set \(I(13,p,1)\) as the main bottleneck for extending the method. ([arxiv.org](https://arxiv.org/html/2604.23906))

---

# 5. NEAR MISSES, TIGHT CASES AND FALSE ANALOGUES

## 5.1 Tight ordinary-LRC families

Write \(k\) for the number of moving speeds. Tight means

\[
\kappa(V)=\frac1{k+1}.
\]

Known tight sets include:

- Every dilation of
  \[
  \{1,2,\ldots,k\}.
  \]
- The sporadic examples
  \[
  \{1,3,4,7\},\quad
  \{1,3,4,5,9\},\quad
  \{1,2,3,4,5,7,12\}.
  \]
- Goddyn–Wong examples
  \[
  \{1,4,5,6,7,11,13\},
  \]
  \[
  \{1,2,\ldots,11,13,24\},
  \]
  \[
  \{1,2,\ldots,17,19,36\}.
  \] ([arxiv.org](https://arxiv.org/html/2409.20160))

The second Goddyn–Wong vector is especially important:

\[
\boxed{\{1,2,\ldots,11,13,24\}}
\]

has 13 speeds and is therefore a **tight 14-runner instance**, exactly at the first open runner count.

It belongs to the infinite family

\[
V_k=\{1,2,\ldots,k-2,k,2(k-1)\}
\]

whenever \(k=6t+1\). At \(k=13\) this gives \(\{1,\ldots,11,13,24\}\). This and \([13]\) are the two most obvious starting seeds for a local counterexample hunt. ([arxiv.org](https://arxiv.org/html/2409.20160))

Goddyn and Wong give a broader “accelerated runners” construction: under explicit common-factor conditions, sets of the form

\[
\{m_1,2m_2,\ldots,km_k\}
\]

remain tight. Tight-instance classification is still incomplete even in relatively small dimensions. ([arxiv.org](https://arxiv.org/html/2409.20160))

## 5.2 Almost-tight spectrum families

Kravitz observed that

\[
\{1,2,\ldots,k-1,ks\}
\]

has gap

\[
\frac{s}{sk+1}.
\]

These provide explicit points in the loneliness spectrum between \(1/(k+1)\) and \(1/k\). They are good controlled mutations of the standard tight vector, although for \(s>1\) their gap increases rather than moving toward a counterexample. ([arxiv.org](https://arxiv.org/html/2409.20160))

The recent modular computations report that almost all residue tuples disappear after only a few lifts; the main survivors project to the standard tight orbit \((1,2,\ldots,k)\). This is strong evidence that the computationally hard cases are extremal/tight structures rather than random vectors. ([researchgate.net](https://www.researchgate.net/publication/404248980_Eleven_twelve_and_thirteen_lonely_runners))

## 5.3 False related conjecture: the spectrum

Ho Tin Fan and Alec Sun disproved the original Loneliness Spectrum Conjecture for four moving speeds by an infinite family, then proposed an amended version. These are not LRC counterexamples—their loneliness gaps remain above the LRC threshold—but they show that plausible classifications of “all values near tightness” can fail. ([combinatorics.org](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i1p38/pdf/))

## 5.4 False stronger analogue: shifted starting positions

The March 2026 preprint *Coloopless zonotopes and counterexamples to the Shifted Lonely Runner Conjecture*, arXiv:2603.24784, gives counterexamples to the shifted variant. The axis being changed is the starting positions, not the constant speeds or the common-start ordinary LRC; it therefore does not disprove the target but is a serious warning against robustness heuristics. ([arxiv.org](https://arxiv.org/abs/2603.24784))

## 5.5 False time-dependent analogue

For time-dependent velocities, Hyunwoo Lee showed that the extreme runners have only the sharp guarantee \(2^{-n+1}\), while intermediate runners can remain arbitrarily close to another runner at all times. Again, this changes the constant-speed axis and does not bear directly on ordinary LRC, but it shows how quickly the phenomenon fails when rigidity is relaxed. ([arxiv.org](https://arxiv.org/abs/2607.16082))

---

# 6. WHO IS ACTIVELY WORKING ON IT?

The most directly active ordinary-LRC computational group is:

- **Matthieu Rosenfeld**, LIRMM/Université de Montpellier/CNRS: 8- and 9-runner proofs and the original prime-divisibility backtracker.
- **Tanupat Trakulthongchai**, St John’s College, Oxford: 9- and 10-runner sieve.
- **Touch Sungkawichai** and Trakulthongchai: 11–13-runner solver, polynomial hard-orbit theorem and public logs. ([arxiv.org](https://arxiv.org/html/2509.14111))

The main geometric/finite-reduction group is:

- **Romanos Diogenes Malikiosis**
- **Francisco Santos**
- **Matthias Schymura**

Their zonotope bound is what makes the recent global computer proofs possible. ([arxiv.org](https://arxiv.org/abs/2411.06903))

Other current activity includes:

- **David Alcántara, Francisco Criado and Francisco Santos:** exhaustive shifted-LRC zonotope computation.
- **Vikram Giri and Noah Kravitz:** loneliness spectra and structural questions.
- **Ho Tin Fan and Alec Sun:** amended spectrum.
- **Vanshika Jain and Noah Kravitz:** relative spectra.
- **Alathea Jensen:** mixed-threshold/Fourier formulations.
- **Guillem Perarnau and Oriol Serra:** current survey and structural programme. ([cambridge.org](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6C8CF8635B7AD8470B1A0104914BA041/S0305004125101497a.pdf/structure_of_lonely_runner_spectra.pdf))

## AI or automated efforts

I found:

- Public exact C++ backtracking/sieve implementations associated with the proof papers.
- A public automated experiment at `https://lonelyrunner.fun/`, which says it forks the 13-runner solver, publishes exact-rational verification code and logs bounded 14-runner probes.
- Machine-generated reviews of the recent proofs, but those are audits, not counterexample searches. ([lonelyrunner.fun](https://lonelyrunner.fun/))

I found **no disclosed academic AI/ML/LLM-assisted counterexample programme**, and no public statement that the proof authors are currently running a full 14-runner computation. The obvious people to contact before committing substantial compute are Sungkawichai, Trakulthongchai and Rosenfeld. Their latest paper already identifies the exact \(k=13\) bottleneck, so duplication risk is real.

---

# 7. TRACTABILITY CALL

## Is the object small?

In descriptive size, yes: 13 positive integers, each requiring at most about 79 bits under the current finite bound. The entire raw object is roughly a kilobit.

## Is it cheaply verifiable?

Only if the speeds are moderate or a compressed certificate is supplied.

For a fixed vector, the exact objective is one-dimensional and rational, but the direct algorithm takes \(O(k^2v_{\max})\) time. A candidate near the theoretical bound could therefore require on the order of \(10^{25}\) elementary breakpoint operations. The verifier is cheap in the numerical value of the speeds, not necessarily in their bit length. ([arxiv.org](https://arxiv.org/html/2409.20160))

A successful project should require any candidate generator to output one of:

- an exact rational interval-cover certificate;
- the relevant modular \(\kappa_N\) computations;
- a compressed union-of-arithmetic-progressions certificate;
- or independently reproducible exact code and logs.

## Realistic search-space size

- Direct normalized vector space under the best sum bound: roughly \(10^{286}\).
- Direct maximum-coordinate box: even larger, around \(10^{296}\) unordered possibilities at the same scale.
- Modular sieve space: dramatically smaller, but current scaling is still severe. The latest authors estimate the bad-set computation roughly grows like
  \[
  \frac{p^{(k+1)/2}}{k2^k},
  \]
  and specifically identify the initial \(k=13\) sieve as the obstruction. ([arxiv.org](https://arxiv.org/html/2604.23906))

## Recommended compute allocation

Do **not** enumerate integer vectors in increasing maximum speed except as a small calibration run.

A serious search should instead:

1. Start with the two target-dimensional tight seeds
   \[
   [13]\quad\text{and}\quad\{1,\ldots,11,13,24\}.
   \]
2. Generate divisor-preserving and divisor-breaking mutations around the accelerated tight families.
3. Search modular unit/permutation orbits that survive the first \(I(13,p,1)\) sieve.
4. Use learned branch ordering or reinforcement learning only to guide an exact backtracker; never let the AI decide pruning soundness.
5. Try CP-SAT/SAT encodings of the modular set-cover condition alongside the current bitset solver.
6. Record not merely “no counterexample” but reusable exclusions: surviving residue orbits, minimum gap achieved, and exact symmetry-reduced counts.
7. Treat a faster exhaustive **proof search** for \(k=13\) as at least as plausible an outcome as finding a counterexample.

## Overall call

**MARGINAL.**

The object is finite and structurally simple, and the first open dimension has explicit tight seeds and a public exact solver. But random search is overwhelmingly misdirected, the rigorous finite region still contains about \(10^{286}\) normalized candidates, the latest algebraic theorem misses \(k=13\) because \(14\) is composite, and there is no theorem suggesting that a minimal counterexample—if one exists—has small speeds.

The single largest obstacle is **the absence of a practically small counterexample bound or a classification of the modular orbits surviving the initial \(k=13\) sieve**, not the final one-dimensional verification.

---

# Search coverage and limitations

- I explicitly searched recent arXiv records from September 2024 through August 13, 2026, including direct records for the 2025–2026 finite-case proofs.
- I reached the arXiv full text for the principal reduction and computer-assisted papers, including implementation and runtime sections.
- I did not independently compile or rerun the proof code.
- I did not have closed-index access to MathSciNet, zbMATH reviews, Scopus or private referee reports.
- I found no paywall blocking the core arXiv papers, but I did not establish the journal/refereeing status of the April 2026 11–13-runner preprint.
- I found no theorem-level published coordinate cutoff for a 14-runner brute-force search; unpublished or private computations could exist.

# Core references

1. **Guillem Perarnau, Oriol Serra**, “The Lonely Runner Conjecture turns 60,” *Computer Science Review* (2025), article 100798. arXiv:2409.20160. DOI: `10.1016/j.cosrev.2025.100798`.  
   URLs: `https://arxiv.org/abs/2409.20160`, `https://doi.org/10.1016/j.cosrev.2025.100798`.

2. **Romanos Diogenes Malikiosis, Francisco Santos, Matthias Schymura**, “Linearly-exponential checking is enough for the Lonely Runner Conjecture and some of its variants,” *Forum of Mathematics, Sigma* 13 (2025); arXiv:2411.06903. ArXiv DOI: `10.48550/arXiv.2411.06903`.  
   URL: `https://arxiv.org/abs/2411.06903`.

3. **Matthieu Rosenfeld**, “The lonely runner conjecture holds for eight runners,” arXiv preprint (2025), arXiv:2509.14111v2. DOI: `10.48550/arXiv.2509.14111`.  
   URL: `https://arxiv.org/abs/2509.14111`.

4. **Tanupat Trakulthongchai**, “Nine and ten lonely runners,” arXiv preprint (2025; v2 2026), arXiv:2511.22427. DOI: `10.48550/arXiv.2511.22427`.  
   URL: `https://arxiv.org/abs/2511.22427`.

5. **Matthieu Rosenfeld**, “The lonely runner conjecture holds for nine runners,” arXiv preprint (2025; v2 2026), arXiv:2512.01912. DOI: `10.48550/arXiv.2512.01912`.  
   URL: `https://arxiv.org/abs/2512.01912`.

6. **Touch Sungkawichai, Tanupat Trakulthongchai**, “Eleven, twelve, and thirteen lonely runners,” arXiv preprint (2026), arXiv:2604.23906v1. DOI: `10.48550/arXiv.2604.23906`.  
   URL: `https://arxiv.org/abs/2604.23906`.

7. **Javier Barajas, Oriol Serra**, “The lonely runner with seven runners,” *Electronic Journal of Combinatorics* 15 (2008), R48. arXiv:0710.4495. ArXiv DOI: `10.48550/arXiv.0710.4495`.  
   URL: `https://arxiv.org/abs/0710.4495`.

8. **Luis Goddyn, Edward B. Wong**, “Tight instances of the lonely runner,” *Integers* 6 (2006), A38. No arXiv ID or DOI was listed in the accessible survey record.

9. **David Alcántara, Francisco Criado, Francisco Santos**, “Covering radii of 3-zonotopes and the shifted Lonely Runner Conjecture,” arXiv preprint (2025), arXiv:2506.13379. DOI: `10.48550/arXiv.2506.13379`.  
   URL: `https://arxiv.org/abs/2506.13379`.

10. **Ho Tin Fan, Alec Sun**, “Amending the Lonely Runner Spectrum Conjecture,” *Electronic Journal of Combinatorics* 33(1) (2026), P1.38. DOI: `10.37236/13840`.  
    URL: `https://doi.org/10.37236/13840`.

11. **Vikram Giri, Noah Kravitz**, “The structure of Lonely Runner spectra,” *Mathematical Proceedings of the Cambridge Philosophical Society* 180(2) (2026), 343–361. DOI: `10.1017/S0305004125101497`; arXiv:2304.01462.  
    URLs: `https://arxiv.org/abs/2304.01462`, `https://doi.org/10.1017/S0305004125101497`.

12. **Alathea Jensen**, “Mixed thresholds in the Lonely Runner Conjecture,” arXiv preprint (2026), arXiv:2605.27941. DOI: `10.48550/arXiv.2605.27941`.  
    URL: `https://arxiv.org/abs/2605.27941`.

**VERDICT: OPEN | MARGINAL**

The ordinary common-start conjecture is proved through 13 total runners in the current 2025–2026 computer-assisted proof record, making 14 runners and the tight seed \(\{1,\ldots,11,13,24\}\) the correct target. A counterexample is finite but the best bound leaves roughly \(10^{286}\) normalized possibilities, so only a structure-guided modular search—not increasing-box brute force—has a credible chance.