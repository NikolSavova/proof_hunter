# Rank-safe endpoint surplus: exact fibre theorem and a fixed-chart Pascal barrier

**Date:** 2026-08-15. All counts are nonempty and all logarithms are base
two. This continues `ENDPOINT_SURPLUS_BALANCED_SHELL_BARRIER.md`.

## Verdict

There is an exact rank-sensitive endpoint theorem, but maximum rank
\(O(\log N)\) alone does not force the \(N^{\log_2 3}\) surplus required by
the three-cloud cycle in a prescribed chart.

For a generic projection, let \(c_e,u_e\) count caps and cups with the same
ordered extreme pair \(e\), including singleton pairs \(e=(x,x)\). Then

\[
 C=\sum_ec_e,\qquad U=\sum_eu_e,\qquad
 V=\sum_ec_eu_e.                                      \tag{1}
\]

Consequently

\[
 {CU\over V}\ge {\left(\sum_e\sqrt{c_eu_e}\right)^2\over V}
                 \ge {V\over\max_ec_eu_e}.             \tag{2}
\]

If every ordinary face has rank at most \(r\), this gives

\[
 \boxed{\quad
 \sigma(P)={CU\over V}\ge
 {V(P)\over \displaystyle\sum_{j=0}^{r-2}{N-2\choose j}}.
 \quad}                                                 \tag{3}
\]

Thus a rank-safe family closes the three-cloud gap whenever its face count
is within the required polynomial of fixed-endpoint capacity:

\[
 V(P)\ge N^{\log_2 3+\varepsilon}
           \sum_{j=0}^{r-2}{N-2\choose j}.              \tag{4}
\]

This is a useful positive criterion on a dense rank slice. It also explains
exactly why the earlier balanced shell needed rank \(\Theta(\log^2N)\): one
fixed endpoint fibre could then contain the dominant \(2^{\Theta(\log^2N)}\)
Boolean mass.

However, there is a scalable rational strong-glue family with

\[
 \operatorname{rank}(P)\le(1.911+o(1))\log N,\qquad
 V(P)=2^{(0.829+o(1))(\log N)^2},                         \tag{5}
\]

but in its genuine construction chart

\[
                         \sigma(P)\le N^{1.55+o(1)}.     \tag{6}
\]

Since \(1.55<\log_2 3=1.584962\ldots\), a prescribed-chart theorem based
only on rank \(O(\log N)\) is false. The family is an imbalanced glue of two
opposite-density Pascal cells. It is fully planar and stretchable; unlike
the balanced-shell barrier, it has no rank-\(\log^2N\) Boolean layer.

The counterexample does **not** bound \(\sup_\theta\sigma_\theta(P)\) over
all projection directions. Hence the strongest surviving positive question
is precisely direction optimization, or localization to a common exposed
physical edge followed by a compatible projective rechart. The latter is
closed under the dilution hypothesis in
`agent_common_shield_mixing/FIXED_EDGE_CARRIER_ENDPOINT_DILUTION_GATE.md`.

## 1. Exact endpoint-rectangle identity

Order the physical labels by a generic projection. For \(i<j\), let
\(\mathcal C_{ij}\) be the nonempty caps whose first and last labels are
\(i,j\), and define \(\mathcal U_{ij}\) analogously. Put
\(c_{ij}=|\mathcal C_{ij}|\), \(u_{ij}=|\mathcal U_{ij}|\). For a singleton
set put \(c_{ii}=u_{ii}=1\).

> **Theorem 1 (endpoint rectangles).** Equations (1)--(3) hold for every
> planar general-position set and every generic projection.

**Proof.** A face has a unique upper/lower hull decomposition. The two
chains have the same extreme pair. Conversely, the union of any cap and cup
with the same extremes is ordinary, and its two traces recover the pair.
This proves the third identity in (1); the first two are the endpoint
partitions of all caps and cups.

Cauchy--Schwarz gives

\[
       CU=\left(\sum_ec_e\right)\left(\sum_eu_e\right)
          \ge\left(\sum_e\sqrt{c_eu_e}\right)^2.        \tag{7}
\]

Writing \(f_e=c_eu_e\) and \(M=\max_ef_e\),

\[
        \sum_e\sqrt{f_e}\ge {\sum_ef_e\over\sqrt M}
                            ={V\over\sqrt M},            \tag{8}
\]

which proves (2). If all faces have rank at most \(r\), a face with fixed
distinct endpoints chooses at most \(r-2\) further labels, so

\[
                   f_e\le\sum_{j=0}^{r-2}{N-2\choose j}. \tag{9}
\]

Singleton fibres have size one. Substitution proves (3). \(\square\)

The first expression in (2) is the exact Rényi-effective number of endpoint
rectangles. No semialgebraic regularity theorem is needed: the face image is
already a disjoint union of complete Cartesian rectangles
\(\mathcal C_e\times\mathcal U_e\). If (2) is small, the obstruction is a
small collection of genuinely heavy common-endpoint rectangles, not an
irregular compatibility graph.

## 2. Near-capacity positive regime

Let

\[
                      B(N,r)=\sum_{j=0}^{r-2}{N-2\choose j}. \tag{10}
\]

Theorem 1 says exactly that the endpoint multiplier is at least \(V/B\).
For \(r=\rho\log N\),

\[
 \log B(N,r)=r\log(N/r)+O(r)
             =\rho(\log N)^2-\rho(\log N)\log\log N+O(\log N). \tag{11}
\]

Therefore a rank slice whose entropy is within
\((\log_2 3+\varepsilon)\log N\) of the full fixed-endpoint capacity closes
by (4). This is the exact place where a deletion-mean or rank-density input
can be used; the statement \(r=O(\log N)\) without density information is
not enough.

There is a compatible common-edge strengthening. If a live subfamily
\(\mathcal H\) shares one exposed physical edge \(uv\), the projective
normalization in `FIXED_EDGE_CARRIER_ENDPOINT_DILUTION_GATE.md` makes every
member one directional profile, so

\[
                  C\ge|\mathcal H|,\qquad
                  U\ge {N\choose2},\qquad
 \sigma\ge { |\mathcal H|{N\choose2}\over V}.           \tag{12}
\]

That theorem closes whenever \(V/|\mathcal H|\) has dilution smaller than
\(N^{2-\log_2 3}\). Its extra hypothesis is real: in the general endpoint
partition the heavy edge can depend on the face, and its projective chart
may be incompatible with frozen exterior context.

## 3. A rank-\(O(\log N)\) prescribed-chart counterfamily

Use the standard rational Pascal cells \(T(d,i)\). Put

\[
 x={1\over4},\qquad \eta={11\over20},\qquad
 B_t=T(t,t/4),\qquad
 A_t=T(\eta t,3\eta t/4),                              \tag{13}
\]

along multiples of eighty, and form the genuine vertical strong glue

\[
                              P_t=A_t\prec B_t.          \tag{14}
\]

Let \(a=|A_t|\), \(b=|B_t|\). Since binary entropy is symmetric,

\[
 \log a=(\eta H_2(1/4)+o(1))t,\qquad
 \log b=(H_2(1/4)+o(1))t,                              \tag{15}
\]

so \(a=b^{\eta+o(1)}\) and \(N=a+b=b^{1+o(1)}\).

The exact Pascal cap recurrence has the uniform asymptotic

\[
 \log C(T(d,yd))=(A(y)+o(1))d^2,                        \tag{16}
\]

where

\[
 A(y)={-y(1-y)-y^2\ln y-(1-y)(1+y)\ln(1-y)\over2\ln2}. \tag{17}
\]

Reflection gives the cup rate \(A(1-y)\), and the top strong-glue term plus
the cap--cup upper injection gives

\[
 \log V(T(d,yd))=(A(y)+A(1-y)+o(1))d^2.                 \tag{18}
\]

The numerical constants are

\[
\begin{aligned}
 H_2(1/4)&=0.8112781244\ldots,\\
 A(1/4)&=0.1217961677\ldots,\\
 A(3/4)&=0.4189766366\ldots,\\
 \eta^2A(3/4)&=0.1267404326\ldots>A(1/4),\\
 A(3/4)&>\eta^2A(1/4)=0.0368433407\ldots .             \tag{19}
\end{aligned}
\]

Thus, for all sufficiently large \(t\), the desired cap mass of \(A_t\)
dominates the opposite cap mass of \(B_t\), and the desired cup mass of
\(B_t\) dominates that of \(A_t\).

The exact strong-glue recurrences are

\[
\begin{aligned}
 C(P_t)&=C(B_t)+(b+1)C(A_t),\\
 U(P_t)&=U(A_t)+(a+1)U(B_t),\\
 V(P_t)&=V(A_t)+V(B_t)+C(A_t)U(B_t).                    \tag{20}
\end{aligned}
\]

Hence eventually

\[
 C(P_t)\le2(b+1)C(A_t),\qquad
 U(P_t)\le2(a+1)U(B_t),\qquad
 V(P_t)\ge C(A_t)U(B_t),                               \tag{21}
\]

and therefore

\[
 \boxed{\quad
 \sigma(P_t)\le4(a+1)(b+1)=N^{1+\eta+o(1)}
                         =N^{1.55+o(1)}.
 \quad}                                                 \tag{22}
\]

All faces in a Pascal cell have rank at most its depth, and restriction of
a face to either strong-glue block is ordinary. Thus

\[
 \operatorname{rank}(P_t)\le(1+\eta)t
       =\left({1.55\over H_2(1/4)}+o(1)\right)\log N
       =(1.910566+o(1))\log N.                           \tag{23}
\]

The cross term in (20) gives

\[
 \log V(P_t)=\left(
 { (1+\eta^2)A(3/4)\over H_2(1/4)^2}+o(1)
 \right)(\log N)^2
 =(0.829140+o(1))(\log N)^2,                            \tag{24}
\]

proving (5)--(6).

The constants are not optimized. Taking opposite densities \(x,1-x\) and
depth ratio just above

\[
                         \sqrt{A(x)/A(1-x)}              \tag{25}
\]

gives prescribed-chart surplus exponent arbitrarily close to
\(1+\sqrt{A(x)/A(1-x)}\). As \(x\to0\), this approaches one, while the
implicit constant in the rank bound grows. Thus no fixed exponent greater
than one can follow from the bare phrase \(r=O(\log N)\) in a frozen chart.

## 4. Exact surviving question

The counterfamily is evaluated in the vertical strong-glue chart. Rotating
the projection changes the cap/cup profiles of both Pascal cells, and this
note does not bound

\[
                         \sup_\theta\sigma_\theta(P_t). \tag{26}
\]

Therefore the following routes remain honest:

1. prove that every rank-\(O(\log N)\) configuration has **some** direction
   with surplus at least \(N^{\log_2 3+o(1)}\);
2. show that the live construction supplies a common exposed edge and that
   the projective rechart in (12) preserves the frozen exterior context; or
3. prove that the actual deletion-mean slice satisfies the near-capacity
   condition (4), which bypasses direction optimization.

A generic semialgebraic rectangle lemma does not by itself improve this
menu. Equation (1) already supplies exact rectangles. The issue is whether
one heavy endpoint rectangle has a globally usable physical edge/chart, or
whether the endpoint mass is diffuse enough for (2) to pay.

## 5. Verification

Run

~~~text
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_rank_safe_endpoint_surplus_gate.py
~~~

The verifier exhausts random rational configurations through nine points
and checks (1)--(3) exactly. It then evaluates the exact Pascal and
strong-glue integer recurrences at \(t=80,160,240\). At \(t=160,240\) the
normalized surplus exponents are respectively \(1.53989\) and \(1.54264\),
both below \(\log_2 3\), while the face coefficients are \(0.83437\) and
\(0.83300\).
