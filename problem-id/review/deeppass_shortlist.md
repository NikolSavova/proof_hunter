# Deep-pass COMBINED shortlist — all 45 finalists (Nikol + Sihao runs merged)

_Rendered from the DB `deeppass` column (25 Sihao + 20 Nikol backfilled, no overwrites)._
_Source dossiers preserved: deeppass_run2.md, deeppass_run2_sihao.md, deeppass_remaining.md._

**Totals: 7 GO · 18 MAYBE · 20 NO-GO**


## GO (7)

- **[arxiv-openproblem:1712.01960v1]** (comp 4.9357, eng both) — Determine the worst-case minimal distortion required to embed an n-point diversity into 
    - *why open:* It survived because the asymptotic problem is genuinely hard, but the small-n certificate problem falls between communities: metric-embedding people w
    - *day-1:* Day 1: implement the fixed-δ rational LP: minimize D subject to δ(A) ≤ Σ_U w_U δ_U(A) ≤ D·δ(A) for every |A|≥2, w_U≥0, using one representative of U a
- **[arxiv-openproblem:2410.09897v1#13]** (comp 4.7143, eng B) — Conjecture: For any Weyl group W and any Bruhat interval [u,v] (u <= v), the rank sequen
    - *why open:* It survived for a real reason but not an impossible one: geometry gives top-heaviness and many palindromic/smooth-interval phenomena, not the local se
    - *day-1:* Day 1: build a standalone C++/Rust bitset verifier, with Sage/Macaulay2 only as cross-check or oracle, not as the certificate. Generate finite Weyl gr
- **[arxiv-openproblem:2307.06787v1#4]** (comp 4.6143, eng both) — For univariate (d=1) integration/approximation tasks with randomized/universal methods (
    - *why open:* It survived because the asymptotic theory is already crowded while the remaining problem is a constants-and-regimes problem: valuable but messy, norm-
    - *day-1:* Day 1: freeze two precise benchmark spaces and one error criterion, then prove and code the periodic certificate first. For periodic Korobov/Sobolev H
- **[arxiv-openproblem:2406.00790v2#7]** (comp 4.5857, eng both) — For each nonnegative integer w, determine W(w) := sup { ρ(Γ) | 0pt(Γ) = w }, where Γ ran
    - *why open:* It survived because the real open problem is the all-w structural inequality, while the fixed-small-w version is an unglamorous hybrid: one must combi
    - *day-1:* Day 1: write a 50-line GAP/Python driver. For each w in {6,7,8} initially, loop over all offset sets A with {0,w} subset A subset {0,...,w}; loop m=1,
- **[erdos:838]** (comp 4.4214, eng both) — Let f(n) be the maximum, over n-point sets in R^2 with no three collinear, of the number
    - *why open:* It survived because the standard upper bound throws away almost all geometry: no convex (n+2)-gon only gives sum_{j<n+2} C(N,j)=2^{(1+o(1))(log2 N)^2}
    - *day-1:* Day 1: implement the Pascal-row generator and the exact DP/upper-bound audit. Use N[n][i]=C(n,i); Cap[n][i] <= Cap[n-1][i]+(1+N[n-1][i])Cap[n-1][i-1];
- **[erdos:112]** (comp 4.3857, eng both) — Determine k(n,m), the minimal number of vertices k such that every directed graph on k v
    - *why open:* It survived because the finite case is just beyond hand proof but not because the instance is huge: avoiding I3 forces the nonedge graph to be triangl
    - *day-1:* Day 1: encode SAT for existence of an (I3,L4)-free oriented graph on N vertices for N=21,22,23,24. Use two Boolean variables per unordered pair: edge-
- **[arxiv-openproblem:2511.01306v1]** (comp 4.2857, eng both) — Produce explicit new optimal ternary cyclic codes (parameters and generator polynomials)
    - *why open:* The exact problem is still genuinely open, but the surviving gap is narrow because the standard route is already known: reduce d=4 to Q1/Q2/Q3 finite-
    - *day-1:* Day 1: write and verify the lemma “for every m>1, h=m−1, C(1,e) is not optimal,” with e=(3^m+1)/2. Proof skeleton: invoke Lemma 2.5/Q1–Q3; for even m,

## MAYBE (18)

- **[arxiv-openproblem:2406.00790v2#2]** (comp 4.8429, eng both) — For integers e,m with 3 ≤ e < m, determine R(e,m) := sup{ ρ(Γ) | edim(Γ) = e+1, mult(Γ) 
    - *why open:* The global problem is genuinely open, but the easy computational niche is narrower than the win condition suggests. For user e=3, the conjectural form
    - *day-1:* Day 1: do not enumerate numerical semigroups. Encode the post-2025 reduced problem: staircase Kunz nilsemigroup/order-ideal certificates. For fixed us
- **[arxiv-openproblem:2511.18217v1#2]** (comp 4.7643, eng B) — Let M be the boundary of the R-neighborhood of a segment (an R-stadium). For a given r>0
    - *why open:* The easy win is already used: any explicit non-horseshoe stadium with R/r<1.75 is prior art. What remains is hard because the upper-bound side require
    - *day-1:* Normalize r=1 and attack only the lower-bound direction C>1.75. On Day 1, implement a periodic two-parallel-lines/stadium-core evaluator: parameterize
- **[arxiv-openproblem:2511.18217v1#7]** (comp 4.6786, eng both) — For a finite rational-point set M ⊂ ℝ^2 of size n, determine how complicated (algebraica
    - *why open:* It survives because the easy algebra is not the hard part. For a fixed combinatorial type, the contact/Steiner conditions are algebraic and eliminable
    - *day-1:* Day 1: fix r=1 and implement an exact n=4 disk-network topology enumerator. Start with the path topology D1--P2--P3--D4, where P2∈∂B(m2,1) and P3∈∂B(m
- **[erdos:791]** (comp 4.6714, eng B) — Let g(n) be the minimal size of A ⊆ {0,...,n} such that A+A contains every integer 0,...
    - *why open:* If open, it survived because the asymptotic problem is not a single finite postage-stamp computation: small exact examples do not improve the asymptot
    - *day-1:* Day 1: build an independent verifier and optimizer for Kohonen’s finite placement problem. Variables: binary I_p,J_p,K_p for p∈[0,M], fixed counts |I|
- **[arxiv-openproblem:1705.04055v1#3]** (comp 4.6714, eng both) — For the pattern p = abXbcYcaZbaTac, which is avoidable over a 4-letter alphabet but not 
    - *why open:* If the intended problem is the canonical BMT pattern ABXBAYACZCAWBC, much of the structure is already known and the fixed-point construction has unifo
    - *day-1:* Day 1: freeze the target by checking BMT/Currie/Néraud against the exact pattern; then run two tracks in parallel. Track B: implement a pattern-occurr
- **[arxiv-openproblem:1512.03038v2]** (comp 4.5857, eng B) — Given a finite abelian group G and integer h>=1, determine minimum possible sizes of hA 
    - *why open:* The surviving gap is real but narrow: exact restricted minima in composite cyclic groups require ruling out all non-coset configurations, while the po
    - *day-1:* Day 1: target a self-certifying finite value, not the whole survey. Start with rho-hat(Z_42,8,3): the explicit set A={0,6,12,18,24,30,36,1} has |3^A|=
- **[arxiv-openproblem:2505.15351v1#12]** (comp 4.5857, eng both) — Create and release a large, realistic, and reproducible dataset of diffraction images (i
    - *why open:* It survived because the mathematical guarantee is easy but the object is sociotechnical: “realistic” means defensible object priors, physically plausi
    - *day-1:* Day 1: freeze a minimal but defensible v0.1 spec before coding: 256×256 CDI single-shot benchmark; object family = mixtures of blob/nanoparticle/vesic
- **[arxiv-openproblem:1905.01736v1]** (comp 4.5714, eng B) — For general Markov Modulated Poisson Processes (MMPPs) the authors conjecture that (IV) 
    - *why open:* The SCV/moment part collapsed to M-matrix inverse and majorization arguments; the survival-order part is much stronger: it asks positivity of an expon
    - *day-1:* Day 1 should be a counterexample engine, not a proof attempt: implement a high-precision Julia/Python evaluator for f(t)=(π−πD/(πD1)) exp((Q−D)t) 1, w
- **[arxiv-openproblem:2206.06472v4]** (comp 4.5571, eng both) — The paper lists ~20 mostly open problems about counting trimer (3-omino) tilings/coverin
    - *why open:* The surviving cases are exactly where the compression/dimer machinery stops being automatic: with all three bone orientations allowed, the squarificat
    - *day-1:* Day 1: ignore the solved two-bone lanes and build a certificate-oriented solver for Problem 6 only. Encode the (n,2n−3)-benzel in Propp’s barycentric 
- **[arxiv-openproblem:2411.10046v1#2]** (comp 4.5429, eng B) — Does there exist a finite graph G for which the list-packing number χ_ℓ^★(G) exceeds the
    - *why open:* The obvious low-parameter routes are fenced off. For χ_ℓ=2, the classical 2-choosable/theta-graph world is very constrained, and related K4-minor-free
    - *day-1:* Day 1: build the fixed-instance SAT checker for “given G,L,k, no L-packing of size k” via the list-coloring instance on G □ K_k, with DRAT/LRAT UNSAT 
- **[arxiv-openproblem:2406.00790v2#8]** (comp 4.5429, eng B) — For any numerical semigroup Γ with minimal generators g1<...<ge, form its interval compl
    - *why open:* It survives because the associated graded/tangent-cone ideal I*_Γ is much less combinatorial than the toric ideal I_Γ: the survey explicitly notes tha
    - *day-1:* Day 1: build a two-backend counterexample evaluator b1TC(gens) in Singular/Macaulay2: compute the toric ideal ker(k[x_i]→k[t], x_i↦t^{g_i}), compute a
- **[arxiv-openproblem:1907.04349v1#3]** (comp 4.5429, eng both) — Find a connected bipartite graph whose adjacency matrix has exactly four distinct eigenv
    - *why open:* It survived because the graph phrasing hides a hard design-realizability problem. Once written as NN^T=dI+αα^T, row degrees and pairwise intersections
    - *day-1:* Day 1: implement the van Dam–Spence parameter generator and SAT/exact-cover backend for square 0/1 matrices N. Enumerate feasible (v,d,δ; multipliciti
- **[erdos:934]** (comp 4.5, eng both) — For fixed integers t >=1 and degree bound d, h_t(d) is the least number of edges such th
    - *why open:* The asymptotic lower-bound route is basically blocked for t=3: projective planes plus one subdivision already give the conjectured extremal value alon
    - *day-1:* Day 1: target h_3(4)=54 only. Prove and implement the reduction for a hypothetical 54-edge graph with max degree 4 and line-graph diameter <=3: a BFS 
- **[arxiv-openproblem:2110.09638v3#2]** (comp 4.5, eng both) — For a multiple-access channel with n symmetric transmitters who only receive limited fee
    - *why open:* It survived because the natural exact problem is a decentralized partially observed team problem, not an ordinary MDP: after a ternary collision, tran
    - *day-1:* Day 1: narrow brutally to “known n, ternary feedback, stationary one-step private-memory policies.” Encode the policy by p for the homogeneous state a
- **[erdos:261]** (comp 4.3714, eng B) — For which positive integers n does there exist t≥2 and distinct integers a1,...,at≥1 wit
    - *why open:* The gap is genuine but computationally treacherous. The finite-certificate route is not derivable on sight from TUZ20; no public extension beyond n≤10
    - *day-1:* Day 1: write two independent implementations of the exact TUZ/Borwein–Loring greedy recurrence S(x) for x=n/2^n, plus a streaming verifier. First repr
- **[erdos:776]** (comp 4.3286, eng B) — For fixed r≥2 let n0(r) be the least n0 such that for all n>n0 there exists a family A1,
    - *why open:* The first-order asymptotic is essentially killed already; the remaining publishable gap is a near-threshold finite/additive problem. He--Tang’s lower 
    - *day-1:* Day 1: ignore asymptotics and attack exact r=4. Build a bitset CNF/SAT model for n=11 and n=12: variables y_{t,S} for choosing a t-subset S; cardinali
- **[erdos:1055]** (comp 4.3143, eng B) — Erdős/Selfridge prime-classification: primes classified by the property that every prime
    - *why open:* It is not a hard primality/factorisation problem; P=764276710625653 would be easy to certify once found, since P+1=2*382138355312827. The surviving di
    - *day-1:* Day 1: write a deterministic PARI/GP or C++ generator/verifier for classes 14+ through 19+ using the recurrence p=2*k*q-1, sorted class lists, determi
- **[erdos:811]** (comp 4.3, eng B) — For a fixed graph G with m = e(G), determine whether for all sufficiently large n ≡ 1 (m
    - *why open:* Because the easy algebraic/product mechanisms have mostly been mined. The Axenovich--Clemen route is tied to 1-factorization/Sidon/perfect-difference-
    - *day-1:* Day 1: attack K5, not C6. Encode a balanced 10-colouring of K21 as ten 2-regular spanning colour classes: variables x_{uv,c}; constraints sum_c x_{uv,
