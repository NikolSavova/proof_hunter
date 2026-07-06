# Paper skeleton — Bruhat-interval log-concavity (Brenti Conjecture 2.11)

> Drafted 2026-07-06 (Sihao session) per PROOF_PLAN.md item 5. Sources: HANDOFF §3,
> `results/*.md` (verification numbers), `theory_probe_gpt55_39009.md` +
> `theory_probe_crossexam_claude_20260704.md` (double-vetted literature scaffold),
> `F2_SPEC.md`. Everything below is LaTeX-ready modulo macros. Gaps for Nikol in §7.
>
> **Tone rule for the whole paper: understate.** Exhaustive tiers are theorems;
> near-top slabs and sampling are *evidence*, never "verification of the conjecture";
> F1 is a conjecture with checked instances, not a result.

---

## 1. Title options

1. *Log-concavity of Bruhat intervals in Weyl groups: extended verification, an
   extremal conjecture, and equality cases*
2. *The tightest Bruhat intervals: on Brenti's log-concavity conjecture for Weyl groups*
3. *Rank sequences of Bruhat intervals: verification beyond rank five, Mahonian
   asymptotics, and an extremal principle*

(Working preference: 1 — states exactly what is delivered, no overclaim.)

Target venues (per prior-art dossier `priorart_gpt55_63405.md`): Electronic J.
Combinatorics, Séminaire Lotharingien de Combinatoire, Experimental Mathematics;
J. Algebraic Combinatorics / JCTA only if F2 (and part of F1) is fully proved.

---

## 2. Draft abstract (~150 words, understated)

> Brenti conjectured that the rank sequence of every Bruhat interval in a finite
> Weyl group is log-concave; the statement is known to fail for the non-crystallographic
> Coxeter group $H_3$. We report an extended computational verification: exhaustive
> checks of all intervals in types $A_2$–$A_7$, $B_2$–$B_6$, $D_4$–$D_6$, $E_6$,
> $F_4$, $G_2$ (over $9\times 10^7$ intervals **[update once A7/B6/E6 land]**), together
> with non-exhaustive evidence in higher ranks: near-top lower-interval sweeps in
> $A_8$–$A_{10}$, $D_7$–$D_8$, $E_7$, and roughly $2.6\times 10^5$ sampled and seeded
> intervals in $B_7$, $B_8$, $D_7$, $E_7$. No violation was found. The data suggest an
> extremal principle: in simply-laced types the minimum log-concavity ratio over all
> intervals appears to be attained by the full interval $[e,w_0]$. In type $A$ this
> minimum is the central ratio of the Mahonian distribution, which we determine
> asymptotically, and we record a classification of the observed equality cases,
> which offers a possible explanation for why Weyl groups avoid the $H_3$ failure.

(150 words. Adjust the interval count and the verified-type list when CI lands.)

---

## 3. Section plan

1. **Introduction.** Brenti's Conjecture 2.11 (OPAC survey); status before this work
   (Brenti's list: $A_n, D_n$ for $n\le 5$, $B_n$ for $n\le 4$, $B_5$ only $\ell\ge 20$,
   $F_4$, dihedral); the $H_3$ counterexample; summary of contributions (i) new
   exhaustive verifications, (ii) Conjecture F1, (iii) Theorem F2, (iv) equality
   classification F3 + crystallographic heuristic. One paragraph on methodology
   and verification artifacts (house style: every claim reproducible).
2. **Preliminaries.** Weyl groups from Cartan data, Bruhat order, length, rank
   sequence $a_k([u,v])$, log-concavity ratio $\rho$, Poincaré polynomial
   $W(q)=\sum_{w\in W} q^{\ell(w)}$, Mahonian numbers $I_m(k)$ and
   $[m]_q!$; the $H_3$ example spelled out (ranks $1,3,5,7,10,10,5,1$; $49<50$).
3. **Computational methodology.** Three independent engines (generic
   Cartan-matrix BFS `weyl.py`/`verify.py`; complement-BFS near-top `scaled.py`/
   `scaled_general.py`; root-action `fast.py`), cross-checks (known $|W|$,
   length $\equiv$ inversion count, Poincaré $\equiv$ degree product, engine-vs-engine
   selftests), exact integer arithmetic, three tiers (exhaustive / near-top slab /
   sampling+seeded), CI reproduction. State precisely what each tier does and does
   NOT establish.
4. **Verification results.** Theorems V1–V3 below + Tables 1–3.
5. **An extremal principle: Conjecture F1.** Statement; evidence (slab sweeps
   $A_7$–$A_9$, $D_7$–$D_8$, $E_7$; exact ties by proper intervals in $A_5$/$A_6$/$D_6$/$A_{10}$);
   why Björner–Ekedahl top-heaviness neither implies nor suggests it; the
   rationally-smooth subclass programme (Carrell–Peterson product formula +
   Hoggar) as a proof target; contrast with the parabolic failure
   (Burrull–Gui–Hu; Stanton's example).
6. **Type $A$: the Mahonian minimum ratio (Theorem F2).** Statement (a)–(c);
   derivation via local CLT / the Canfield–Janson–Zeilberger transfer (their
   Thm 4.6 / eq. (4.11) cited prominently as the source of the technique — our
   contribution is the $S_m$ case, the global minimum, and the explicit constant);
   the predicted-vs-observed table $A_4$–$A_{10}$ including the $\approx 0.91\times$
   second-order offset (flag as Edgeworth term; optional sharpening).
7. **Equality cases: F3.** Precise statement of the dihedral $(1,2,\dots,2,1)$
   pattern; empirical status (exhaustive tier + 204k seeded perturbations, strict
   wall); the crystallographic-restriction argument for why the $H_3$ failure has
   no Weyl analogue ($m=5$ core is non-crystallographic); short-interval
   classification route (arXiv:2110.00862) as future/partial work.
8. **Discussion and open problems.** F1 for $E_8$; a quantitative version of
   Brenti's conjecture (ratio $\ge 1 + c(W)$ with $c$ explicit in simply-laced
   types); relation to equivariant log-concavity of flag-variety cohomology
   (arXiv:2205.05408); equality-case literature (Stanley–Yan, Kahn–Saks) and the
   pre-submission re-sweep.
- **Appendix A.** Full data tables, witness reduced words, reproduction commands
  (per-run dossier files in `results/`).
- **Appendix B.** Engine cross-validation protocol (selftest gauntlet).

---

## 4. Precise statements (LaTeX-ready)

### 4.0 Setup (used by all statements)

For a finite Weyl group $W$ with simple reflections $S$, length $\ell$, Bruhat
order $\le$, and $u \le v$ in $W$, write $[u,v]=\{z : u\le z\le v\}$ and
$$a_k([u,v]) \;=\; \#\{\,z\in[u,v] : \ell(z)=\ell(u)+k\,\},\qquad 0\le k\le \ell(u,v):=\ell(v)-\ell(u).$$
The interval is *rank log-concave* if $a_k^2 \ge a_{k-1}a_{k+1}$ for all
$1\le k\le \ell(u,v)-1$. When all $a_k>0$ (always true for Bruhat intervals) set
$$\rho([u,v]) \;=\; \min_{1\le k\le \ell(u,v)-1}\; \frac{a_k^2}{a_{k-1}\,a_{k+1}}
\qquad (\ell(u,v)\ge 2),$$
so Brenti's Conjecture 2.11 asserts $\rho([u,v])\ge 1$ for every Bruhat interval
of every finite Weyl group. Note $[e,w_0]$ has $a_k = [q^k]\,W(q)$, the
coefficients of the Poincaré polynomial.

### 4.1 Verification theorems

**Theorem V1 (exhaustive tier).**
*Let $W$ be one of the Weyl groups $A_2,\dots,A_7$, $B_2,\dots,B_6$, $D_4,D_5,D_6$,
$E_6$, $F_4$, $G_2$. Then every Bruhat interval $[u,v]\subseteq W$ is rank
log-concave. The verification is exhaustive: all intervals of length $\ge 2$ were
enumerated and checked in exact integer arithmetic (interval counts in Table 1),
totalling $> 9.2\times 10^7$ intervals* **[recount once A7/B6/E6 land — CI pending]**.

*Remark.* Relative to the previously recorded frontier (Brenti: $A_n,D_n$, $n\le5$;
$B_n$, $n\le4$; $B_5$ only $\ell(u,v)\ge 20$; $F_4$; dihedral), the cases
$A_6, A_7, B_5\ (\ell<20), B_6, D_6, E_6$ are new.

**Theorem V2 (near-top tier — lower intervals only; NOT exhaustive).**
*Let $(W,c)$ be one of $(A_7,4), (A_8,4), (A_9,3), (D_7,3), (D_8,3), (E_7,2)$.
Then every lower interval $[e,v]$ with $\ell(w_0)-\ell(v)\le c$ is rank
log-concave; moreover the minimum of $\rho([e,v])$ over this slab is attained at
$v=w_0$ (values in Table 2). In $A_{10}$ the interval $[e,w_0]$ and a partial slab
($11$ of $65$ candidates at $c=2$) were checked, all log-concave, with a proper
interval exactly tying $\rho([e,w_0])$.*

*Scope caveat (must appear verbatim in some form):* Theorem V2 checks only lower
intervals in a thin slab below $w_0$; it is evidence for Conjecture 2.11 and for
F1 in these groups, not a verification of either beyond the stated slabs.

**Theorem V3 (sampling tier — NOT exhaustive; coverage statement only).**
*(i) $60{,}000$ Bruhat intervals $[u,v]$ (20{,}000 each in $B_7$, $D_7$, $E_7$),
sampled uniformly from a random-walk ensemble with $4\le\ell(u,v)\le 12$
(seed 7, reproducible), are all rank log-concave.
(ii) $204{,}000$ seeded intervals ($4{,}000$ in $B_7$ seed 3; $100{,}000$ each in
$B_7,B_8$ seed 4) containing an $m=4$ dihedral braid core perturbed by $0$–$10$
extra cover steps are all rank log-concave; every perturbation that destroys the
pure dihedral pattern yields ratio $>1$ (Table 3).*

### 4.2 Conjecture F1 (headline; apparently new — double-vetted)

**Conjecture F1.** *Let $W$ be an irreducible simply-laced finite Weyl group
(type $A_n$, $D_n$, $E_6$, $E_7$, $E_8$) with longest element $w_0$. Then*
$$\min_{\substack{[u,v]\subseteq W\\ \ell(u,v)\ge 2}} \rho([u,v])
\;=\; \rho([e,w_0])
\;=\; \min_{1\le k\le \ell(w_0)-1} \frac{b_k^2}{b_{k-1}b_{k+1}},$$
*where $b_k=[q^k]\,W(q)$ are the coefficients of the Poincaré polynomial of $W$;
i.e. the global minimum of the log-concavity ratio over all Bruhat intervals is
attained by the full interval $[e,w_0]$, at a central index. Proper intervals may
achieve equality with this minimum (observed in $A_5$, $A_6$, $D_6$, $A_{10}$) but
never less.*

*Status.* Verified exhaustively in $A_2$–$A_6$, $D_4$–$D_6$ **[+ $A_7$, $E_6$: CI
pending]**; verified in the near-top slabs of Theorem V2 for $A_7$–$A_9$, $D_7$–$D_8$,
$E_7$ (in every completed sweep, nothing beats $[e,w_0]$). Both independent
literature reads found no statement, precedent, or contradiction (dossiers
2026-07-04). Björner–Ekedahl's top-heaviness inequalities for (parabolic) lower
intervals constrain rank shapes but do not compare ratios across intervals and
neither imply nor suggest F1.

*Proof target (subclass, PROOF_PLAN item 2):* for rationally smooth $v$,
$P_{[e,v]}(q)$ factors as a product of $q$-integers (Carrell–Peterson), hence is
log-concave (Hoggar/Kook), and its central ratio may be compared against the
degree-product formula for $W(q)$ — "F1 holds for rationally smooth lower
intervals" as a provable case.

*Note the simply-laced restriction is necessary:* in $B/F/G$ the global minimum is
$1$, attained by dihedral equality patterns (F3), not by $[e,w_0]$.

### 4.3 Theorem F2 (type $A$ anchor; statement frozen in F2_SPEC.md)

Let $I_m(k)=\#\{\sigma\in S_m : \mathrm{inv}(\sigma)=k\}$ (Mahonian numbers), so
$\sum_k I_m(k)q^k=[m]_q!$ and $[e,w_0]\subseteq A_{m-1}$ has $a_k=I_m(k)$. Put
$N=\binom{m}{2}$, $\sigma_m^2=\mathrm{Var}(\mathrm{inv})=\frac{m(m-1)(2m+5)}{72}$,
$r_m(k)=\frac{I_m(k)^2}{I_m(k-1)I_m(k+1)}$, and $r_m=\min_{1\le k\le N-1} r_m(k)$.

**Theorem F2.** *(a) [asymptotic] $r_m = 1+\sigma_m^{-2}\,(1+o(1))$ as
$m\to\infty$; equivalently $r_m-1 \sim 36/m^3$.
(b) [location] The minimum is attained centrally: every minimizing index $k$
satisfies $|k-N/2|\le 1$ (empirically $\mathrm{argmin}=\lfloor N/2\rfloor$ for all
$4\le m\le 40$).
(c) [explicit bound — stretch; downgrade to conjecture if unproved]
$r_m \ge 1 + \tfrac{7}{8}\,\sigma_m^{-2}$ for all $m\ge 5$.*

*Positioning (per cross-exam — mandatory):* log-concavity of $I_m(k)$ is classical
(Bóna; Hoggar/Kook product closure). Canfield–Janson–Zeilberger, Theorem 4.6 /
eq. (4.11), already prove the central-ratio asymptotic
$P(k)^2-P(k-1)P(k+1) = (\sigma^{-2}+O(n^{-4}))P(k)^2$ for the *central Gaussian
binomial* in the central window. F2 must be presented as: the $q$-factorial ($S_m$)
analogue + the *global* minimum statement + the explicit constant, obtained via
CJZ's transfer technique — a corollary-with-new-content of their method, not an
independent discovery. Proof obligations and numeric-check protocol: `F2_SPEC.md`
(ground truth `mahonian.py --mmax 40`: $\sigma_m^2(r_m-1)$ increases
$0.84\to 0.97$ over $4\le m\le 40$).

### 4.4 F3: equality classification (apparently new — double-vetted)

**Observation/Conjecture F3 (equality cases).** *Let $W$ be a finite Weyl group
and $[u,v]\subseteq W$ a Bruhat interval with $\ell(u,v)\ge 2$ in which equality
$a_k^2=a_{k-1}a_{k+1}$ holds for some $1\le k\le \ell(u,v)-1$. Then (as observed
in all exhaustive data) the interval has rank sequence*
$$(a_0,\dots,a_{\ell(u,v)}) \;=\; (1,2,2,\dots,2,1)
\qquad\text{($m-1$ interior 2's, $m\ge 4$)},$$
*i.e. $[u,v]$ is isomorphic (as a poset) to the full dihedral interval of
$I_2(m)$, arising from a rank-two dihedral standard parabolic pattern of braid
order $m\ge 4$; equality then holds exactly at the interior plateau positions
$2^2 = 2\cdot 2$. In Weyl groups the realizable cores are $m=4$ (type $B_2/C_2$,
present in $B_n$, $F_4$) and $m=6$ (type $G_2$). In particular no equality occurs
in simply-laced types (where $m\le 3$).*

*Empirical status (state as such — NOT proved):* holds in every exhaustively
checked group (Theorem V1 list): every ratio-$1$ witness recorded has ranks
$(1,2,\dots,2,1)$ (e.g. $B_2$ `1212`; $B_3$ `2323`; $B_4$ `3434`; $B_5$ `4545`;
$F_4$ `2323`; $G_2$ `1212`; sampled $B_7$ `[2432, 24326767]`). The 204k seeded
perturbation probes (Table 3) show the equality wall is *strict*: every
perturbation of an equality interval by extra cover steps that breaks the pure
dihedral pattern raises the ratio (closest non-equality margins $4$–$8$, with
rank-independent extremal shapes resembling the $H_3$ profile).

**The crystallographic heuristic (why Weyl groups dodge $H_3$) — present as an
argument/mechanism, not a theorem.** Brenti's $H_3$ counterexample
($u=s_3$, $v=s_1s_2s_3s_2s_1s_2s_1s_3$, ranks $1,3,5,7,10,10,5,1$; $10^2 = 100 <
105 = 10\cdot ... $ — check: $49<50$ at the failing index, margin $-1$) sits on an
$m=5$ dihedral core: $H_3$ contains the parabolic $I_2(5)$. The crystallographic
restriction confines rank-two parabolics of Weyl groups to $m\in\{2,3,4,6\}$;
$m=5$ is exactly the excluded case. Thus the equality/violation-producing cores
available inside Weyl groups are only $m=4$ and $m=6$, and by F3 + the strict
perturbation wall these sit at ratio exactly $1$ and cannot be pushed below.
This is offered as the candidate mechanism for the simply-laced/crystallographic
dichotomy, not as a proof. **[Nikol: verify the $H_3$ failing-index arithmetic
against Brenti's paper before this paragraph ships — the $49<50$ margin $-1$ is
from our prior-art dossier.]**

---

## 5. Verification tables (assembled from `results/`)

### Table 1 — Exhaustive tier (every Bruhat interval, exact arithmetic)

Source files: `run_A2-A3-A4-A5-A6-B2-B3-B4-B5-D4-D5-D6-G2-F4_64112.md` (+ earlier
partial runs, consistent), `run_D6_63367.md` (independent repeat of $D_6$).

| Group | $|W|$ | #intervals ($\ell\ge2$... as counted) | min ratio | witness $[u,v]$, index $k$ | ranks at witness |
|---|---:|---:|---:|---|---|
| $A_2$ | 6 | 19 | 2.000000 | $[e,\,121]$, $k{=}1$ | $(1,2,2,1)$ |
| $A_3$ | 24 | 213 | 1.388889 | $[e,\,12321]$, $k{=}2$ | $(1,3,5,6,4,1)$ |
| $A_4$ | 120 | 3,781 | 1.210000 | $[e,\,w_0]$, $k{=}5$ | Mahonian $I_5$ |
| $A_5$ | 720 | 98,407 | 1.122222 | $[e,\,12132432154321]$ ($\ell{=}14$, proper — ties $[e,w_0]$), $k{=}7$ | see file |
| $A_6$ | 5,040 | 3,550,919 | 1.079096 | $[e,\,v]$, $\ell(v){=}20$ proper — ties $[e,w_0]$, $k{=}10$ | see file |
| $A_7$ | 40,320 | **[CI pending]** | **[CI pending]** | **[CI pending]** | |
| $B_2$ | 8 | 33 | 1.000000 | $[e,\,1212]$, $k{=}2$ | $(1,2,2,2,1)$ |
| $B_3$ | 48 | 847 | 1.000000 | $[e,\,2323]$, $k{=}2$ | $(1,2,2,2,1)$ |
| $B_4$ | 384 | 40,249 | 1.000000 | $[e,\,3434]$, $k{=}2$ | $(1,2,2,2,1)$ |
| $B_5$ | 3,840 | 3,089,459 | 1.000000 | $[e,\,4545]$, $k{=}2$ | $(1,2,2,2,1)$ |
| $B_6$ | 46,080 | **[CI pending]** | **[CI pending]** | **[CI pending]** | |
| $D_4$ | 192 | 9,817 | 1.136232 | $[e,\,12321421324]$ ($\ell{=}11$), $k{=}5$ | see file |
| $D_5$ | 1,920 | 745,377 | 1.069459 | $[e,\,v]$, $\ell(v){=}19$, $k{=}10$ | see file |
| $D_6$ | 23,040 | 84,339,681 | 1.040703 | $[e,\,v]$, $\ell(v){=}27$ proper — ties $[e,w_0]$, $k{=}15$ | see file |
| $E_6$ | 51,840 | **[CI pending]** | **[CI pending]** | **[CI pending]** | |
| $F_4$ | 1,152 | 396,809 | 1.000000 | $[e,\,2323]$, $k{=}2$ | $(1,2,2,2,1)$ |
| $G_2$ | 12 | 73 | 1.000000 | $[e,\,1212]$, $k{=}2$ | $(1,2,2,2,1)$ |

Running total checked (excluding CI-pending rows): **92,275,684 intervals, zero
violations.** Notes: (i) reported witness is the first minimizer the enumerator
encountered — where it is a proper interval in a simply-laced group its ratio
*equals* $\rho([e,w_0])$ (checked for $A_5,A_6,D_6$; **[Nikol: confirm for
$D_4,D_5$** — the recorded witnesses have $\ell(v)=\ell(w_0)-1$; verify tie vs.
$[e,w_0]$ central ratio before asserting F1's "attained at $[e,w_0]$" in the
exhaustive column]). (ii) All $B/F/G$ minima are the F3 equality pattern.

### Table 2 — Near-top slab tier (lower intervals $[e,v]$, $\ell(w_0)-\ell(v)\le c$; NOT exhaustive)

Source files: `scaled_A7-A8_37169.md`, `fastscan_A9_51808.md`,
`fastscan_D7-D8_A9partial_20260704.md`, `fastscan_E7_2317.md`,
`fastscan_A10_partial_20260705.md`.

| Group | $|W|$ | slab | #candidates checked | min ratio (exact fraction) | attained at | central index $k$ |
|---|---:|---|---:|---|---|---:|
| $A_7$ | 40,320 | cogap $\le 4$ | full slab | 1.054250 $=919681/872356$ | $[e,w_0]$ | 14 |
| $A_8$ | 362,880 | cogap $\le 4$ | full slab | 1.038942 $=854275984/822255625$ | $[e,w_0]$ | 18 |
| $A_9$ | 3,628,800 | cogap $\le 3$ | 209/209 | 1.028950 | $[e,w_0]$ (tail-best proper: 1.031382) | 22 |
| $A_{10}$ | 39,916,800 | cogap $\le 2$ | **11/65 (partial — parked)** | 1.022102 | $[e,w_0]$; one proper interval EXACTLY TIES | 27 |
| $D_7$ | 322,560 | cogap $\le 3$ | 112/112 | 1.025574 | $[e,w_0]$ | 21 |
| $D_8$ | 5,160,960 | cogap $\le 3$ | 156/156 | 1.017122 | $[e,w_0]$ | 28 |
| $E_7$ | 2,903,040 | cogap $\le 2$ | full slab | 1.011829 $=65523/64757$ | $[e,w_0]$ | 31 |

All pass; in every *completed* sweep no proper interval beats $[e,w_0]$
(F1-consistent). $E_7$ appears to be the first log-concavity verification data of
any kind for that group. $A_{10}$ is explicitly partial (resume path documented in
its dossier); do not list it as an F1-verified sweep.

### Table 3 — Sampling / seeded tier (NOT exhaustive; coverage counts)

Source files: `fastsample_B7-D7-E7_43716.md`, `seeded_B7_seed3_44845.md`,
`seeded_B7-B8_seed4_44925.md`.

| Probe | Group | #intervals | design | min ratio | witness / note |
|---|---|---:|---|---|---|
| random sample (seed 7) | $B_7$ | 20,000 | $[u,v]$, $4\le\ell(u,v)\le12$ | 1.000000 | $[2432,\,24326767]$ ranks $(1,2,2,2,1)$ — F3 pattern |
| random sample (seed 7) | $D_7$ | 20,000 | same | 1.157143 $=81/70$ | proper interval, $k{=}4$ |
| random sample (seed 7) | $E_7$ | 20,000 | same | 1.142400 $=14641/12816$ | proper interval, $k{=}5$ |
| seeded wall (seed 3) | $B_7$ | 4,000 | $m{=}4$ core + 0–6 covers | 1.000000 only at pure dihedral ranks | 28 ratio-1 hits, ALL ranks $(1,2,2,2,1)$ |
| seeded wall (seed 4) | $B_7$ | 100,000 | $m{=}4$ core + 0–10 covers | pert$=0$: 1.000000; pert$\ge1$: $\ge 1.079153$ | closest non-equality margins 4–8 |
| seeded wall (seed 4) | $B_8$ | 100,000 | $m{=}4$ core + 0–10 covers | pert$=0$: 1.000000; pert$\ge1$: $\ge 1.087990$ | extremal shapes rank-independent, $H_3$-like |

Total: 264,000 intervals, zero violations, zero equality cases outside the
$(1,2,\dots,2,1)$ pattern.

### Table 4 (for §6) — F2 predicted vs. observed, $[e,w_0]\subset A_{m-1}$

| $m$ | group | $\sigma_m^{-2}$ | observed $r_m-1$ | ratio obs/pred |
|---:|---|---:|---:|---:|
| 5 | $A_4$ | 0.240000 | 0.210000 | 0.875 |
| 6 | $A_5$ | 0.141176 | 0.122222 | 0.866 |
| 7 | $A_6$ | 0.090226 | 0.079096 | 0.877 |
| 8 | $A_7$ | 0.061224 | 0.054250 | 0.886 |
| 9 | $A_8$ | 0.043478 | 0.038942 | 0.896 |
| 10 | $A_9$ | 0.032000 | 0.028950 | 0.905 |
| 11 | $A_{10}$ | 0.024242 | 0.022102 | 0.912 |

Monotone approach to 1 from below ($\approx 0.91\times$ at $m=11$) — the
second-order (Edgeworth) term; matches `mahonian.py` ground truth
$\sigma_m^2(r_m-1)\uparrow$, $0.84\to0.97$ for $m\le 40$.

---

## 6. Citation scaffold (from the two vetted theory-probe dossiers)

1. **F. Brenti**, *Some open problems on Coxeter groups and unimodality* (OPAC
   survey; arXiv:2410.09897) — source of Conjecture 2.11, the prior verification
   list, and the $H_3$ counterexample. Cited: §1, §4, §7.
2. **A. Björner, T. Ekedahl**, *On the shape of Bruhat intervals*, Ann. of Math.
   170 (2009) 799–817 (arXiv:math/0508022) — top-heaviness $f_i\le f_j$
   ($i<j\le\ell(w)-i$) for (parabolic) lower intervals; cited in §1/§5 as the
   strongest prior shape result and explicitly contrasted: it does not compare
   ratios across intervals, so it neither implies nor suggests F1.
3. **E. R. Canfield, S. Janson, D. Zeilberger**, *The Mahonian probability
   distribution on words is asymptotically normal*, Adv. Appl. Math. 46 (2011)
   (arXiv:0908.2089) — **must-cite prominently in §6**: their Thm 4.6/eq. (4.11)
   prove the central ratio $1+\sigma^{-2}$ for the central Gaussian binomial;
   F2 is the $S_m$/global/explicit-constant extension of their technique.
4. **M. Bóna**, *A combinatorial proof of the log-concavity of a famous sequence
   counting permutations*, Electron. J. Combin. 11(2) (2004) #N2 — direct proof
   that Mahonian numbers are log-concave. Cited §6.
5. **S. G. Hoggar**, *Chromatic polynomials and logarithmic concavity*, J. Combin.
   Theory Ser. B 16 (1974) — log-concavity closed under products. Cited §5
   (rationally-smooth route) and §6.
6. **W. Kook** (2006 note) — elementary statement/proof of the product-closure
   theorem. Cited §6 alongside Hoggar.
7. **L. M. Butler**, *The q-log-concavity of q-binomial coefficients*, J. Combin.
   Theory Ser. A 54 (1990) — q-log-concavity background; cited §6 (distinguish:
   indexed-by-$k$ q-log-concavity, not coefficientwise for $[m]_q!$).
8. **B. E. Sagan**, *Inductive proofs of q-log concavity*, Discrete Math. 99
   (1992) — same background role, §6.
9. **Su–Wang–Yeh**, strong q-log-concavity of multinomials/symmetric functions,
   Electron. J. Combin. 18 (2011) #P73 — same background role, §6.
10. **G. Burrull, T. Gui, H. Hu**, *Asymptotic log-concavity of dominant lower
    Bruhat intervals via the Brunn–Minkowski inequality* (arXiv:2311.17980) —
    cited §5/§8: recalls Conj 2.11; the parabolic analogue fails in general.
11. **D. Stanton** — non-unimodal Grassmannian/Young-lattice example (via [10]) —
    cited §5 as the cautionary parabolic failure.
12. **Carrell–Peterson** (rational smoothness; e.g. J. B. Carrell, Proc. Sympos.
    Pure Math. 56 (1994)) — $P_{[e,v]}(q)$ factors into $q$-integers for
    rationally smooth $v$; cited §5 as the F1 subclass proof route.
13. **arXiv:2110.00862** (classification of short Bruhat intervals) — cited §7:
    the route to a *proved* short-interval equality classification for F3.
14. **V. V. Petrov**, *Sums of Independent Random Variables* — Edgeworth/local
    expansion error control in the F2 proof, §6.
15. Related-work near-misses (all checked NOT to contain F1/F2/F3; cite in §8):
    **arXiv:2205.05408** (equivariant log-concavity of flag-variety cohomology —
    exactly the $[e,w_0]$ polynomial, nothing on minimality over intervals);
    **Stanley–Yan** arXiv:2407.19608 and **Kahn–Saks** arXiv:2309.13434 and
    **arXiv:2211.14252** (equality cases of *different* log-concavity/AF-type
    inequalities — the active area triggering the pre-submission re-sweep);
    **arXiv:2003.06710** (rank-symmetric intervals via pattern avoidance, §7).

---

## 7. TODO / gaps for Nikol

1. **[CI pending] Collect $A_7$, $B_6$, $E_6$ exhaustive runs** (your machine /
   `bruhat-scan` CI) and fill the three Table-1 rows + the abstract's totals.
   $B_6$ min should be 1.000000 with an F3 witness — confirm the witness ranks.
2. **F1 wording decisions:** (a) irreducible only, or state for reducible via
   factors? (b) $\ell(u,v)\ge 2$ convention; (c) "ties allowed" phrasing; (d)
   confirm the $D_4$/$D_5$ (and $A_5$) proper-witness ratios exactly tie
   $\rho([e,w_0])$ — needed before claiming "attained at $[e,w_0]$" across the
   exhaustive tier (Table 1 note (i)).
3. **F2 proof** per `F2_SPEC.md` obligations 1–5 (local expansion; CJZ transfer;
   the genuinely-new global/tail argument; centrality; explicit $c=7/8$ if
   achievable). Cross-examine any draft per house rule; every lemma gets a
   `mahonian.py` NUMERIC CHECK line. Decide theorem-vs-conjecture for part (c).
4. **F3 scope call:** empirical observation vs. conjecture vs. partial theorem
   (short intervals via arXiv:2110.00862 — PROOF_PLAN item 3). Also decide
   whether F3 quantifies over all equality *indices* (plateau-local) or asserts
   the whole rank sequence is $(1,2,\dots,2,1)$; current data support the strong
   form but only where witnesses were recorded.
5. **Verify the $H_3$ arithmetic** (ranks $1,3,5,7,10,10,5,1$, failing margin
   $-1$, $49<50$) directly against Brenti's paper, and make the $m=5$-core claim
   precise (exhibit the $I_2(5)$ parabolic inside the counterexample interval).
6. **Methodology section:** write up the three-engine cross-validation protocol
   and what "exhaustive" means operationally (interval enumeration via up/down
   bitsets; exact integers); state random-walk sampling measure honestly.
7. **Rationally-smooth F1 subclass** (PROOF_PLAN item 2): attempt the
   Carrell–Peterson + Hoggar comparison — this is the paper's best shot at a
   *proved* F1 statement.
8. **Pre-submission fresh arXiv sweep** on equality-cases work (Stanley–Yan /
   Kahn–Saks lines are active — cross-exam dossier caveat) + MathSciNet/zbMATH
   pass (neither probe had access).
9. Optional polish: the $0.91\times$ Edgeworth offset (PROOF_PLAN item 4);
   $A_{10}$ slab completion (C/Rust port or CI chunks — parked, not a blocker);
   decide whether to attempt any $E_8$ near-top data; Lean artifact for the key
   F2 lemma if feasible.
10. Venue call (EJC vs. Sém. Lothar. vs. Exp. Math.; upgrade target if F2+F1
    subclass are fully proved) and author/affiliation/license questions from the
    README thread.
