# Long-braid switch for the reverse-product trace

**Date:** 2026-08-13
**Status:** exact local theorem plus exhaustive/annealed obstruction report; no
proof of RPR or the mean-size bound.

## Verdict

There is a clean exact theorem: one type-A long braid transfers a single
rank-one polynomial family from the cup endpoint array to the cap endpoint
array.  The two partition functions have a common base and differ only by two
explicit nonnegative switch terms,

\[
 Z_+(z)=Z_0(z)+z^2\Phi(z),\qquad
 Z_-(z)=Z_0(z)+z^2\Psi(z).                         \tag{1}
\]

This is the strongest useful braid-local formula I found.  It does **not**
produce a context-free orientation or a mean-compatible descent:

* already at `n=5`, the same labeled triple prefers opposite trace directions
  in two prefix/suffix contexts;
* at `n=8`, a trace-neutral long braid changes the mean in either direction;
* at `n=9`, a strict trace descent can raise the mean, and the graded profiles
  cross coefficientwise;
* the exact braid graph has many trace-local minima (70 at `n=6`; 982 weak
  minima at `n=7`) rather than a canonical normal form.

Thus fixed packet orientations, sums of fixed oriented-triple weights,
coefficientwise compression, and “descend trace, inherit a mean bound” are all
rigorously obstructed.  The computations do not threaten RPR or
`mu >= log2(n)-O(1)` themselves.  They say that a proof must control the
full prefix/suffix boundary state in (1), or use a genuinely global argument.

## 1. Exact switch theorem

Let the increasing root order be

\[
  \mathcal P,\quad (a,b),(a,c),(b,c),\quad \mathcal S,
  \qquad a<b<c,                                      \tag{2+}
\]

and let the other braid branch replace the local packet by

\[
  (b,c),(a,c),(a,b).                                 \tag{2-}
\]

Write

\[
 F(X)=T_{x_m}\cdots T_{x_1},\qquad
 G(X)=T_{x_1}\cdots T_{x_m}
\]

for a root list `X=(x_1,...,x_m)`, and put

\[
 K=I+z(E_{ba}+E_{ca}+E_{cb}).
\]

Direct multiplication gives the entire local algebra:

\[
 T_{bc}T_{ac}T_{ab}=K+z^2E_{ca},\qquad
 T_{ab}T_{ac}T_{bc}=K.                              \tag{3}
\]

Define the common-base matrices

\[
 A_0=F(\mathcal S)K F(\mathcal P),\qquad
 B_0=G(\mathcal P)K G(\mathcal S),                  \tag{4}
\]

and polynomial boundary vectors

\[
\begin{array}{ll}
 \alpha=F(\mathcal S)e_c,&\beta^T=e_a^TF(\mathcal P),\\
 \gamma=G(\mathcal P)e_c,&\delta^T=e_a^TG(\mathcal S).
\end{array}                                         \tag{5}
\]

Then the full cup/cap endpoint arrays on the two branches are exactly

\[
\begin{array}{c|cc}
 &A\;(\text{cups})&B\;(\text{caps})\\ \hline
 +&A_0+z^2\alpha\beta^T&B_0\\
 -&A_0&B_0+z^2\gamma\delta^T.
\end{array}                                         \tag{6}
\]

This holds with arbitrary prefix and suffix.  In particular, at `z=1` every
cup endpoint entry changes by

\[
 A^+_{ts}-A^-_{ts}=\alpha_t\beta_s,
\]

every cap endpoint entry changes oppositely by

\[
 B^-_{ts}-B^+_{ts}=\gamma_t\delta_s,
\]

and both rank-one rectangles are supported only on `t>=c`, `s<=a`.  The
endpoint-product arrays themselves have the common base

\[
 A_0\odot B_0
\]

and respective additions

\[
 (\alpha\beta^T)\odot B_0,qquad
 A_0\odot(\gamma\delta^T).                          \tag{7}
\]

Taking Frobenius products proves (1), where

\[
\begin{aligned}
 Z_0(z)&=nz+\langle A_0,B_0\rangle_F-n,\\
 \Phi(z)&=\langle\alpha\beta^T,B_0\rangle_F
          =\beta^TB_0^T\alpha,\\
 \Psi(z)&=\langle A_0,\gamma\delta^T\rangle_F
          =\gamma^TA_0\delta.                       \tag{8}
\end{aligned}
\]

All coefficients in `Z_0`, `Phi`, and `Psi` are nonnegative.  This makes the
combinatorial meaning precise: the braid chooses which of two boundary-glued
families is present, but the sizes and endpoint multiplicities of those
families depend on all of the prefix and suffix.

### Specialization and first moment

Use a dot for `d/dz` at `z=1`, and abbreviate evaluated values by the same
letters.  Then

\[
\begin{aligned}
 V_+&=V_0+\Phi,&M_+&=M_0+2\Phi+\dot\Phi,\\
 V_-&=V_0+\Psi,&M_-&=M_0+2\Psi+\dot\Psi,             \tag{9}
\end{aligned}
\]

where `M=Z'(1)` and

\[
 M_0=n+\left.\frac d{dz}\langle A_0,B_0\rangle_F\right|_{z=1}.
\]

Thus

\[
 V_+-V_-=\Phi-\Psi,\qquad
 M_+-M_-=2(\Phi-\Psi)+(\dot\Phi-\dot\Psi).          \tag{10}
\]

For the endpoint arrays, for example,

\[
 \dot A^+-\dot A^-
 =2\alpha\beta^T+\dot\alpha\beta^T+\alpha\dot\beta^T,
                                                               \tag{11}
\]

with the analogous formula for `dot B^- - dot B^+` using `gamma,delta`.
The mean comparison is the exact rational comparison

\[
 \frac{M_0+2\Phi+\dot\Phi}{V_0+\Phi}
 \quad\hbox{versus}\quad
 \frac{M_0+2\Psi+\dot\Psi}{V_0+\Psi}.               \tag{12}
\]

Equation (12), not merely `Phi` versus `Psi`, explains why trace and mean
eventually choose different braid directions.

## 2. Exact small graph census

The verifier in `braid_local_analysis.py` checked (6), (9), and (11) in 431
random exposed contexts before the searches below.  Commutation-class counts
and adjacency use the independently implemented Coxeter-heap enumerator in
`agent_reflection_gate/reflection_order_gate.py`.

| `n` | search | states / braid edges | trace-local behavior |
|---:|---|---:|---|
| 5 | all reduced words | 384 individual braid edges | every one of the 10 labeled triples has both signs of `V_+-V_-` in different contexts |
| 6 | all reduced words | 146432 individual braid edges | trace, first moment, and mean signs agree on every edge |
| 6 | all commutation classes | 908 / 2144 | 70 weak trace minima; `V=44..48`; every profile has top degree 4 |
| 7 | all commutation classes | 24698 / 80360 | 34601 edges each strict direction and 11158 ties; trace, first moment, and mean signs agree |
| 7 | same | — | 136 strict minima, but 982 weak minima; weak-minimum `V=72..83`, degree 4 or 5, `C/U=0.434..2.303` |

The `n=7` agreement is therefore exhaustive, but it is not a theorem: the
larger witnesses below disprove it.

Other natural scalar proxies already disagree with trace at `n=6`.  Among the
2144 undirected class edges, trace direction conflicts with `C+U` on 224,
with `CU` on 376, and with the largest endpoint product on 200; there are
additional ties.  No one of these is a trace-compatible Lyapunov function.

## 3. Minimal explicit obstructions found

### 3.1 No context-free packet orientation (`n=5`)

For the labeled triple `(0,1,2)`, the two words

```text
+ 0102103210   V=31, Phi=4
- 1012103210   V=28, Psi=1
```

prefer the minus branch.  In a second context,

```text
+ 2103210232   V=28, Phi=1
- 2103210323   V=31, Psi=4
```

the same labeled triple prefers the plus branch.  The full `n=5` census shows
this reversal for every labeled triple.

Consequently, no rule assigning a fixed preferred orientation to each triple,
and no sum of fixed oriented-triple weights whose edge direction is meant to
match trace descent, can work.  The prefix/suffix vectors in (5) are
load-bearing.

### 3.2 Trace tie changes mean (`n=8`)

Two adjacent commutation classes, related by one long braid after exposing it
with short commutations, have profiles

\[
 (8,28,56,20,1),\qquad (8,28,56,21).
\]

Both have `V=113`, but their first moments are respectively `317` and `316`.
The second therefore has

\[
 \mu=316/113=2.796460\ldots,
 \qquad \mu-\log_2 8=-0.2035398\ldots .             \tag{13}
\]

This slightly improves the previous all-reflection-order mean record at
`n=8`.  The word is in `BRAID_CERTIFICATES.json`.  Fixed-`x` stretchability
was not certified, so (13) is not asserted as a point-set record.

### 3.3 Strict trace descent raises mean (`n=9`)

For the exposed triple `(0,6,7)`, an exact pair has

\[
\begin{array}{c|c|c|c}
 &\text{graded profile}&V&M\\ \hline
 +&(9,36,84,62,13)&204&646\\
 -&(9,36,84,64,12)&205&649.
\end{array}
\]

Here

\[
 \mu_+=646/204=323/102=3.166666\ldots
 >649/205=3.165853\ldots=\mu_- .                    \tag{14}
\]

So the strict trace descent `minus -> plus` raises the mean.  The profile
difference is `-2 z^4+z^5`; hence neither branch dominates coefficientwise.
The switch certificate is

```text
V0=200, M0=630,
Phi=4, dot(Phi)=8,
Psi=5, dot(Psi)=9.
```

All words are recorded in `BRAID_CERTIFICATES.json` and independently
recomputed in `random_n9.json`.

Annealed scans saw 98 strict trace/mean sign conflicts among 18741 evaluated
braids at `n=9`, and 53 among 15159 at `n=10`; this is not an isolated wall
case.  At `n=10` the scan also found `V=296`, profile
`(10,45,120,107,14)`, improving the earlier search record 301 over all
reflection orders (with no stretchability claim).

## 4. What remains plausible

Strict trace descent is of course acyclic because `V` is an integer, but it
terminates in a large and heterogeneous collection of sink candidates.  The
exact local-minimum condition supplied by this work is only

\[
 \Phi\le\Psi\quad\text{on a current plus packet},
 \qquad
 \Psi\le\Phi\quad\text{on a current minus packet}.  \tag{15}
\]

The quantities in (15) contain the full matrices in (4), so this is not a
bounded-state structural characterization.  Small minima remain encouraging:
all exact weak minima through `n=7` have mean deficit at least
`-0.16847`, and the searches through `n=10` do not suggest an unbounded
deficit.  But the sparse-profile pattern is not rigid: weak minima already
have degree 5 at `n=7`, and the `n=8` trace-113 plateau contains several
different profiles and means.

The most defensible next use of the switch theorem would be a **global sink
plateau theorem**: sum or amortize (15) over many exposed packets and prove
that every plateau with no outgoing trace descent already has large `V` or
large `mu`.  Nothing in the local algebra alone supplies that summation.  A
cut-based or multiscale invariant retaining the four boundary vectors appears
necessary.

## 5. Verification artifacts

* `braid_local_analysis.py`: exact dual-number implementation of (3)--(11),
  exhaustive class census, all-word direct-context scan, and annealed search.
* `BRAID_CERTIFICATES.json`: compact `n=5`, `n=8`, and `n=9` witnesses.
* `contexts_n5.json`, `contexts_n6.json`: all-word direct-braid scans.
* `classes_local_n6.json`, `classes_local_n7.json`: exact class-graph censuses.
* `random_n8.json`, `random_n9.json`, `random_n10.json`: seeded larger scans.

Reproduce the exact algebra and principal censuses from the repository root:

```sh
python3 phase2/loop/erdos838/agent_braid_potential/braid_local_analysis.py selftest
python3 phase2/loop/erdos838/agent_braid_potential/braid_local_analysis.py contexts 6
python3 phase2/loop/erdos838/agent_braid_potential/braid_local_analysis.py classes 7
```

The first command is fast; the `n=6` all-word and `n=7` class searches take
roughly one minute each on the machine used for this report.
