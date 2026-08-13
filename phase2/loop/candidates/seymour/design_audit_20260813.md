# Seymour campaign — audit (gpt-5.6-sol, effort=max)

**CAMPAIGN OFF AS STATED: the \(n\le 36\) cap is not established. The peer-reviewed Zelenskyi–Darmosiuk–Nalivayko paper contains no such finite reduction, and the actual source of the \(36\) claim has a fatal proof gap.** ([opuscula.agh.edu.pl](https://www.opuscula.agh.edu.pl/vol41/4/art/opuscula_math_4128.pdf))

## Verdict summary

| Claim | Verdict |
|---|---|
| **A. \(f(8)=36\) finite reduction** | **BROKEN** |
| **B. Brukhman \(n\le2\delta+2\)** | **CONFIRMED** |
| **C. Minimum out-degree \(7\)** | **CANNOT TELL** — analytic reduction plausible; computer core not independently verified |
| **D. Absolute upper bound on \(\delta^+\) of a smallest counterexample** | **CONFIRMED: none found** |
| **E. Glover full proof** | **BROKEN** |

---

## A. The alleged \(f(8)=36\) upper bound — **BROKEN**

### A(i) Exact statement and correct source

The statement does **not** occur in Zelenskyi–Darmosiuk–Nalivayko. Their five-page paper proves blow-up results producing counterexamples of arbitrarily low/high density and prescribed diameter. Their construction adds the same \(n\) vertices to both the first and second out-neighbourhood of every old vertex, thereby preserving the strict inequality—but it makes the graph larger, not smaller. ([opuscula.agh.edu.pl](https://www.opuscula.agh.edu.pl/vol41/4/art/opuscula_math_4128.pdf))

The claimed finite reduction actually appears as Corollary 5 of Tyler Seacrest’s arXiv preprint:

> “If there exists a counterexample \(D\) to the SNC with minimum degree \(\delta\), then there exists a counterexample with at most \({\delta+1\choose2}\) vertices.”

Thus the claimed function is

\[
f(\delta)=\binom{\delta+1}{2}.
\]

Guo–Kang–Zwaneveld cite Seacrest, not Zelenskyi–Darmosiuk–Nalivayko, for this statement. ([arxiv.org](https://arxiv.org/abs/1808.06293))

### A(ii) Arithmetic

Formally,

\[
f(8)=\binom{9}{2}=36.
\]

So **36 is the correct evaluation of the claimed formula**. The problem is that the formula has not been proved.

### A(iii) Fatal gaps in the proof

The weight lies in Seacrest’s Lemma 4, which is supposed to show that every nonempty vertex set in an edge-minimal counterexample has a smaller second boundary than first boundary.

There is an incorrect set identity at the start of the proof. Taking \(T=N_1^+(S)\), the paper identifies

\[
N_1^+(T)\setminus S=N_2^+(S).
\]

That is false when there are arcs inside \(T\). For example, with arcs

\[
s\to a,\qquad s\to b,\qquad a\to b,
\]

take \(S=\{s\}\) and \(T=N_1^+(S)=\{a,b\}\). Then \(b\in N_1^+(T)\setminus S\) through \(a\to b\), but \(b\notin N_2^+(S)\), because \(b\) is already a first out-neighbour of \(s\). This invalidates the maximal-set argument used to justify the edge deletion. ([arxiv.org](https://arxiv.org/html/1808.06293v3))

The corollary then applies Lemma 4 to

\[
S=\bigcup_{i=1}^{k-1}N_i^+(v)
\]

and concludes

\[
d_k^+(v)>d_{k+1}^+(v).
\]

That conclusion again silently assumes that the first and second out-boundaries of \(S\) are exactly the next two BFS layers. Internal arcs, back-arcs, and arcs to earlier layers make this false under the paper’s own definition of set distance. The decreasing-layer sequence—and hence the triangular bound—is therefore unsupported. ([arxiv.org](https://arxiv.org/html/1808.06293v3))

These are not cosmetic notation errors: they are precisely the steps from which \(\binom{\delta+1}{2}\) is derived.

### A(iv) A valid replacement: \(63\), with a different quantifier

There is a published result that partially rescues finiteness. Espuny Díaz, Girão, Granet and Kronenberg prove:

\[
\delta^+(D)>\sqrt{|V(D)|}
\]

for every **vertex-minimal counterexample** \(D\). Thus, if a globally vertex-minimal counterexample has \(\delta^+=8\), then

\[
n<8^2=64,\qquad\text{so }n\le63.
\]

I find this proof sound. It does not claim that arbitrary edge deletion preserves all strict margins. Instead, it maintains a partition \(A_i,X_i,B_i\) with no arcs from \(A_i\) to \(B_i\), stops at a Hall-type expansion condition on \(X_i\), and then lifts a Seymour vertex from \(D[A_i]\) to \(D\): every external first neighbour is compensated by a distinct external second neighbour in \(B_i\). That directly addresses the global-margin issue. ([arxiv.org](https://arxiv.org/pdf/2403.02842))

**Important quantifier:** this gives \(n\le63\) for a globally vertex-minimal counterexample whose own minimum out-degree is \(8\). It is not Seacrest’s stronger fixed-degree reduction from an arbitrary \(\delta=8\) counterexample.

---

## B. Brukhman’s dense-case theorem — **CONFIRMED**

The theorem states that an oriented graph with

\[
n=2\delta+2
\]

has a Seymour vertex. Together with Fisher’s tournament theorem at \(n=2\delta+1\), this excludes every \(n\le2\delta+2\). ([arxiv.org](https://arxiv.org/html/2608.11530v1))

### Audit of the counting argument

For a fixed target \(x\), the paper defines:

- a “trap” \(T(x)\) of vertices that do not point to \(x\);
- the slack \(q(x)=|T(x)|-\delta\);
- \(P(x)\), the vertices from which \(x\) is unreachable in at most two steps.

If \(p=|P(x)|>0\), all arcs whose source is in \(P(x)\) must end in \(T(x)\). Therefore:

- there are at least \(\delta p\) such arcs;
- at most \(\binom p2\) end inside \(P(x)\);
- at most \(p(|T(x)|-p)\) end in \(T(x)\setminus P(x)\).

Hence

\[
\delta p\le \binom p2+p(\delta+q(x)-p),
\]

which simplifies exactly to

\[
p\le2q(x)-1.
\]

This step is correct; the orientation condition is used in exactly the required place to bound internal arcs by \(\binom p2\). ([arxiv.org](https://arxiv.org/html/2608.11530v1))

Now let \(L\) be the set of minimum-outdegree vertices and \(\ell=|L|\). Every \(v\in L\) has at most \(\delta-1\) second out-neighbours, so at \(n=2\delta+2\) it has at least two vertices unreachable within two steps. Therefore, if

\[
I=\sum_v|U(v)|=\sum_x|P(x)|,
\]

then

\[
I\ge2\ell.
\]

The fixed-target bound gives

\[
I\le\sum_{q(x)>0}(2q(x)-1)<2Q,
\qquad Q=\sum_xq(x).
\]

Finally,

\[
Q=n(n-1-\delta)-\sum_xd^+(x).
\]

Every vertex outside \(L\) has outdegree at least \(\delta+1\), so

\[
\sum_xd^+(x)\ge \ell\delta+(n-\ell)(\delta+1)
=n(\delta+1)-\ell.
\]

Since \(n=2\delta+2\), this yields \(Q\le\ell\), and hence

\[
2\ell\le I<2Q\le2\ell,
\]

a contradiction. I find no missing case, sign error, or unjustified strict inequality. ([arxiv.org](https://arxiv.org/abs/2608.11530))

**Counterfactual floor if B failed:** conditional on excluding \(\delta=7\), the \(\delta=8\) floor would be \(n=18\), because Fisher excludes only \(n=17=2\delta+1\). Unconditionally, for \(\delta=7\), the order floor would fall from \(17\) to \(16\). ([arxiv.org](https://arxiv.org/html/2608.11530v1))

---

## C. Sadhukhan–Sandeep–Sen, \(\delta^+=7\) — **CANNOT TELL**

### Structural reduction

The top-level case division appears exhaustive.

Starting at a minimum-outdegree vertex gives \(|A|=7\), while its failure to be Seymour gives \(|B|\le6\). After the preliminary reductions, the paper lists exactly:

1. \(|A|=7,\ |B|=5\);
2. \(|A|=7,\ |B|=6,\ |A_1|=3\);
3. \(|A|=7,\ |B|=6,\ |A_1|=2\);
4. \(|A|=7,\ |B|=6,\ |A_1|=1\).

The bound \(|A_1|\le3\) comes from choosing a vertex of minimum internal outdegree in \(A\); when \(|B|=6\), \(|A_1|=0\) cannot supply total outdegree seven. ([arxiv.org](https://arxiv.org/html/2606.30588v1))

In the \(|A_1|=2\) branch, every out-neighbour of \(a_1\) lies in \(A\cup B\). Thus, with two internal out-neighbours and minimum total outdegree seven,

\[
r=|N^+(a_1)\cap B|\in\{5,6\}.
\]

That split is genuinely exhaustive.

### Soundness of the finite models

The model direction is the correct one: the propositions assert that any genuine obstruction induces a feasible finite-model assignment. Therefore, if the model is truly infeasible, the obstruction is impossible. The paper explicitly models orientation, local outdegree requirements, forced two-step paths, witness non-Seymour inequalities, and compressed outside terminals. ([arxiv.org](https://arxiv.org/html/2606.30588v1))

The trimming operation is also plausible: only outgoing arcs of **non-witness** vertices are removed. Witness first out-neighbourhoods are unchanged, while their second out-neighbourhoods can only shrink. Hence witness non-Seymour inequalities survive trimming. This is the right way to avoid the global-margin failure seen in Seacrest and Glover. ([arxiv.org](https://arxiv.org/abs/2606.30588))

One correction to the prior sweep: the computer-assisted portion is not confined to the \(|A_1|=2\) branch. Section 6 treats \(|A_1|=1\) using the same trimming/modeling framework with modified constraints. ([arxiv.org](https://arxiv.org/abs/2606.30588))

### Why I cannot confirm it

The decisive statements are the computational lemmas asserting CP-SAT infeasibility for all residual rows. I did not independently rerun the exact encodings or obtain an independently checkable UNSAT certificate. The printed soundness arguments make the proof **plausible**, and I found no explicit missing top-level case, but the mathematical theorem depends on the correctness of:

- every row-generation bound;
- every transcription into the CP-SAT model;
- every reported infeasibility run;
- the correspondence between the executed model and the printed model.

The preprint reports those infeasibility checks as the final contradiction. Without an independent reproduction, I cannot elevate the result to CONFIRMED. ([arxiv.org](https://arxiv.org/abs/2606.30588))

**Operational consequence:** for a conservative campaign, \(\delta^+=7\) remains live. With B confirmed, its order floor is \(n=17\); at \(n=19\), both degrees \(7\) and \(8\) remain live unless the CP-SAT proof is independently reproduced.

---

## D. Universal upper bound on the minimum out-degree — **CONFIRMED: none found**

Interpreting the question as asking for an absolute bound

\[
\delta^+(D)\le D_0
\]

for a smallest or vertex-minimal counterexample: I found no published result giving such a constant.

There are relevant bounds, but all go in the wrong direction:

- Kaneko–Locke gives the lower bound \(\delta^+\ge7\).
- The Sadhukhan–Sandeep–Sen preprint would raise that to \(8\).
- Espuny Díaz et al. prove the published relative lower bound
  \[
  \delta^+(D)>\sqrt n
  \]
  for a vertex-minimal counterexample.
- Brukhman proves \(n\ge2\delta+3\).

None bounds \(\delta\) by a universal constant. ([arxiv.org](https://arxiv.org/pdf/2403.02842))

Espuny Díaz et al. also construct, from any hypothetical seed counterexample, arbitrarily large strongly connected counterexamples whose minimum outdegree is bounded by a constant depending on that unknown seed. That is not an explicit universal bound and does not reduce the possible degrees of the smallest counterexample to a finite list. ([arxiv.org](https://arxiv.org/pdf/2403.02842))

Therefore a complete UNSAT result for \(\delta=8\) still leaves \(\delta=9,10,\ldots\) untouched. An absolute order bound, an absolute upper bound on \(\delta\), or an explicit reduction to counterexamples of universally bounded minimum outdegree would be required to close this obstacle.

---

## E. Glover v14 — **BROKEN**

The arXiv manuscript reached v14 on May 30, 2026. I found no evidence of withdrawal or peer-reviewed acceptance; current papers, including Brukhman’s August 12 preprint, continue to describe the conjecture as open. ([alphaxiv.org](https://www.alphaxiv.org/zh/overview/2501.00614v14?utm_source=openai))

The fatal issue is the manuscript’s “No Excess Interior Arcs”/arc-minimality step. It argues that an interior arc beyond a locally calculated requirement can be deleted while the graph remains a counterexample. But vertex-minimality gives no such edge-deletion property, and even an edge-minimal choice does not help unless preservation is proved.

Arc deletion is not monotone for the strict margin. For a concrete local configuration, let a root point to \(a,b,c\), and include

\[
a\to b,\qquad a\to c,\qquad c\to b.
\]

Before deleting \(a\to b\),

\[
|N^+(a)|=2,\qquad |N^{++}(a)|=0.
\]

After deleting \(a\to b\),

\[
N^+(a)=\{c\},\qquad N^{++}(a)=\{b\},
\]

so \(a\) becomes a Seymour vertex. Thus an apparently redundant intra-layer arc may be exactly what keeps its source strictly non-Seymour. Local “capacity” does not prove global removability. The paper subsequently uses this deletion claim to impose equal interior degrees and eliminate classes of transitive triangles, so the gap propagates into the main counting contradiction. ([alphaxiv.org](https://www.alphaxiv.org/abs/2501.00614v13?utm_source=openai))

The related elimination of back-arcs is also unsupported: an arc that creates no new BFS-layer vertex can still change the first and exact second out-neighbourhoods of non-root vertices. Optimizing forward expansion from one root is not equivalent to preserving the counterexample condition at every vertex. ([alphaxiv.org](https://www.alphaxiv.org/abs/2501.00614v13?utm_source=openai))

No external refutation is needed to reject the proof: its principal reduction operation has not been shown to preserve the property being minimized.

---

**IS THE SLICE \(\delta^+=8,\ 19\le n\le36\) REAL AND FINITE? NO — \(36\) is unsupported; for a globally vertex-minimal counterexample the rigorous degree-\(8\) tranche is \(19\le n\le63\), while without independently confirming C one must also retain \(\delta=7,\ 17\le n\le48\); in general the smallest-counterexample region is \(\delta\ge7,\ 2\delta+3\le n\le\delta^2-1\), an infinite union over \(\delta\).**