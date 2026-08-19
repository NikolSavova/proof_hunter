# The swap-coupled six-anchor charge

> **Update (2026-08-19).**  This remains the strongest endpoint-normal
> fallback.  `ADAPTIVE_CROSS_PAIR_D2_CHARGE_GATE.md` gives a newer uniform
> charge of all configurations into `D^2`, with the larger permissible load
> `K=S/N`; it is now the preferred direct gate.

## 1. Outcome

This note strengthens the normal part of
`HYBRID_ENDPOINT_OPPOSITE_CHARGE_GATE.md`.  Every ordered normal
configuration occurs together with the configuration obtained by swapping
its two popular shifts.  Using both endpoint decorations, and two additional
head anchors, gives six candidate charges rather than the previous two.

The resulting charge is still injective in every rich fibre.  If `lambda_6`
is its normal load, then

\[
 \sum\lambda_6^2\le \mathcal B_6\le \mathcal B_N,             \tag{1.1}
\]

where `B_N` is the old balanced two-anchor degree moment and `B_6` is the
new six-anchor degree envelope defined below.  Thus this is an unconditional
sharpening of the exact reduction, not a new hypothesis.

The theorem

\[
 \boxed{\mathcal B_6\le N^{o(1)}|C_N|}                         \tag{1.2}
\]

together with analogous size-biased bounds for the existing common-endpoint
routes would prove the cube-root upper bound.  Neither remaining bound is
proved.

## 2. Six anchors from the swap involution

Write `L=I+J`.  A normal configuration in the fibre `(u,s)`, with
`w=s-u`, consists of ordered distinct popular shifts `(q,p)` and the seven
members

\[
 u,\ u+q,\ u+p,\ w-q,\ w-p,\ w-Lq,\ w-Lp\in D.                \tag{2.1}
\]

Put `a=u`, `b=a+q`, and `c=a+p`.  The two endpoint labels are

\[
 \omega_p=(\epsilon(c),m(a)-m(c)),\qquad
 \omega_q=(\epsilon(b),m(a)-m(b)).                              \tag{2.2}
\]

The original and swapped anchor pairs are

\[
 (\ell_q,z_q)=(w-Lq,w-q),\qquad
 (\ell_p,z_p)=(w-Lp,w-p).                                      \tag{2.3}
\]

The second pair is exactly the primary pair of the swapped ordered
configuration `(p,q)`, which is present in the same fibre.  Four candidates
therefore come from endpoint degrees:

\[
 (\omega_p,\ell_q),\ (\omega_p,z_q),\
 (\omega_q,\ell_p),\ (\omega_q,z_p).                           \tag{2.4}
\]

There are also two head candidates

\[
 (\omega_p,b),\qquad(\omega_q,c).                              \tag{2.5}
\]

For each labelled cell, let its degree be the number of normal
configurations occupying it.  Charge the configuration to a candidate of
minimum degree, using a fixed lexicographic tie rule.  If `omega_q` is a
common-endpoint degeneracy, omit its three candidates; `omega_p` is normal
by the branch definition, so three candidates remain.

Every route is fibrewise injective.  On the original routes, `omega_p`
recovers `(a,c)` and hence `p`; an anchor in (2.3), or the head `b`, then
recovers `q`.  The swapped routes have the same proof with `p,q`
interchanged.  Route labels are disjoint.

## 3. The exact degree envelope

For a normal configuration `gamma`, let `d_1(gamma),...,d_6(gamma)` be the
available cell degrees in (2.4)--(2.5), and put

\[
 \mathcal B_6=\sum_{\gamma\in C_N}\min_i d_i(\gamma).          \tag{3.1}
\]

The load of a chosen charge is at most the full degree of its cell.  Summing
over configurations proves the first inequality in (1.1).  Since the old
left and right cells are among the candidates,

\[
 \min_i d_i(\gamma)\le
 \min\{d(\omega_p,\ell_q),d(\omega_p,z_q)\},                   \tag{3.2}
\]

which proves `B_6<=B_N`.

The six route universes have total size at most `12NS`.  The unchanged
common-endpoint singleton and resonance routes use at most `4NS+2N^2`, so
the complete charge lands in at most

\[
 18NS.                                                         \tag{3.3}
\]

This constant is immaterial.  A size-biased `N^{o(1)}` load bound still
gives `O_K<=N^{1+o(1)}S` by Cauchy--Schwarz.

## 4. Fixed-head collision system

The four fixed `w`-anchor collision systems are the two systems already
recorded in the hybrid note and their images under `p<->q`.  The head
routes give a third exact system.  Fix the original head `b=a+q`.  The seven
forms are

\[
 a,\ b,\ c,\ w-q,\ w-p,\ w-Lq,\ w-Lp.                         \tag{4.1}
\]

For two preimages define

\[
 \rho=q_2-q_1,\qquad \pi=p_2-p_1,\qquad
 \kappa=w_2-w_1.                                               \tag{4.2}
\]

Their seven displacements are exactly

\[
 -\rho,\ 0,\ \pi-\rho,\ \kappa-\rho,\ \kappa-\pi,
 \ \kappa-L\rho,\ \kappa-L\pi.                              \tag{4.3}
\]

The swapped head has the same list after interchanging `p` and `q`.
The exact verifier checks (4.1)--(4.3) and all four fixed-anchor systems.

## 5. Stress results

The stored exact suite gives the following complete-charge profiles
`(mass,image,second moment,max load)`:

| family | profile | second moment / mass |
|---|---:|---:|
| closure 40 | `(370516,369663,372254,4)` | `1.00469076` |
| closure 80 | `(357094,356998,357286,2)` | `1.00053767` |
| Costas 23 | `(498674,493947,508164,3)` | `1.01903047` |
| Costas 37 | `(2939312,2900964,3016296,3)` | `1.02619116` |
| Costas 41 | `(4629690,4525615,4843428,4)` | `1.04616681` |
| Costas 43 | `(8451318,8271632,8815150,4)` | `1.04305033` |

For comparison, the two-anchor Costas-43 profile had normalized load
`1.22230095` and maximum load `7`; the original one-anchor version had
about `1.7644` and maximum `12`.  These are diagnostics only.  They do not
prove (1.2), and the remaining asymptotic obstruction could be absent from
all finite families tested.

Run

```bash
python3 phase2/loop/erdos1208/verify_hybrid_endpoint_opposite_charge.py \
  --extended --literal-max
python3 phase2/loop/erdos1208/analyze_balanced_anchor_parallel.py
```

The conceptual change is that arbitrary high arboricity in one endpoint
graph is no longer by itself the final obstruction.  A failure of (1.2)
must survive the involution `p<->q` and remain simultaneously dense across
two endpoint labels, two paired `w`-anchors, and the associated heads.
That coupled endpoint theorem is the current shortest direct route.
