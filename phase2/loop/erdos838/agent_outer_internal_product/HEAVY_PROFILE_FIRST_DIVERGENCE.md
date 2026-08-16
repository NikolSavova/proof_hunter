# Heavy-profile first divergence: carrier bank versus guard shadow

**Date:** 2026-08-14.  All logarithms are base two and the empty convex
subset is counted.

## Verdict

For one heavy marked root, canonical guards have an exact first-divergence
dichotomy.

* If the released carriers `B=A setminus G` are diverse, the singleton
  completion bank is the injective product `B times X_T`.
* If many profiles have the same carrier, all singleton completions may
  collapse completely, but the guards contribute their full
  Kruskal--Katona downshadow, joined to that carrier.

This gives a rigorous positive theorem, but it does not close the global
heavy-profile branch.  The shadow alternative can be tight, and there is an
exact planar bounded-rank regression in which `binom(s,r)` actual canonical
profiles share one carrier, all completion records collapse to `|X_T|`
faces, and the carrier bank is exactly the downset of the complete `r`th
layer on `s` guard labels.

The regression has source rank `O(log n)`, maximum face rank `O(log n)`, and
therefore uniform mean `O(log n)` when the inserted child has maximum convex
rank `O(log n)`.  It carries `n^{Theta(1)}` marked profiles, matching the
fixed-power entropy forced by `WEIGHTED_PROFILE_SQUARE_GATE.md`.  It does
**not** carry `Theta(V)` marked mass when `log V=Theta((log n)^2)`; doing that
would require quadratically many distinct carrier fibres.  The remaining
global summation problem is therefore explicit and is not claimed solved.

## 1. Fixed-root carrier fibres

Fix a marked root `T`, a deleted root label `z in T`, and the retained edge
`e=T setminus {z}`.  Let `X subseteq X_T` be a common singleton completion
alphabet of size `m`.  Consider a canonical occurrence family

\[
 \Omega=\{(A,G):G\subseteq A,\ G\cap T=\{z\},\ |G|=g,
       \ (A\setminus G)\cup\{x\}\text{ convex for every }x\in X\}.
                                                               \tag{1}
\]

Assign at most one guard to a given pair `(A,T)`; duplicate descriptions can
always be canonically discarded.  Put

\[
                         B(A,G)=A\setminus G.                 \tag{2}
\]

Let `mathscr B` be the set of distinct carriers, and for `B in mathscr B`
let

\[
 \mathcal G_B=\{G:(B\cup G,G)\in\Omega\},\qquad
 k_B=|\mathcal G_B|.                                        \tag{3}
\]

The guards in one fibre are distinct because `A=B union G`.

## 2. Exact completion bank

> **Lemma 1 (carrier--label product).**  The faces
>
> \[
>                           B\cup\{x\},qquad
>                           B\in\mathscr B,\ x\in X          \tag{4}
> \]
>
> are all distinct.  Hence
>
> \[
>                              V(P)\ge m|\mathscr B|.         \tag{5}
> \]

**Proof.**  Every set in (4) is convex by (1).  Since every marked carrier is
disjoint from `X_T`, intersection with `X` recovers `x`; removing it recovers
`B`.  QED.

Thus guard profiles only cause completion collisions after their sources
have the same exact released carrier.  If `W=|Omega|` and
`k=max_B k_B`, then

\[
                  |\mathscr B|\ge W/k,qquad
                  V(P)\ge mW/k.                              \tag{6}
\]

In particular, a fixed root carrying `W>=beta_T V` occurrences must have a
carrier fibre of size at least `beta_T m`.

## 3. Exact guard-union bank

Fix a carrier `B`.  Remove the common label `z` from its guards and put

\[
                  \mathcal F_B=\{G\setminus\{z\}:G\in\mathcal G_B\}
                    \subseteq {P\setminus\{z\}\choose g-1}. \tag{7}
\]

Let `downarrow mathcal F_B` denote all subsets of members of this uniform
family.

> **Lemma 2 (guard-shadow bank).**  The map
>
> \[
>                  D\longmapsto B\cup\{z\}\cup D,
>                  \qquad D\in\downarrow\mathcal F_B        \tag{8}
> \]
>
> is an injection into the ordinary convex faces.  Consequently
>
> \[
>                         V(P)\ge|\downarrow\mathcal F_B|.    \tag{9}
> \]

**Proof.**  Choose `G` with `D subseteq G setminus {z}`.  The output in (8)
is a subset of the convex source `B union G`, hence is convex.  The fixed
carrier and labels make (8) injective.  QED.

Kruskal--Katona makes (9) quantitative.  Write `r=g-1`, and let `x>=r` be the
unique real number with

\[
                              k_B={x\choose r}.               \tag{10}
\]

The Lovasz form of the theorem gives, at every level `0<=i<=r`,

\[
              |\{D\in\downarrow\mathcal F_B:|D|=i\}|
                         \ge{x\choose i}.                    \tag{11}
\]

Therefore

\[
 \boxed{
 V(P)\ge \Phi_r(k_B):=\sum_{i=0}^r{x\choose i}.}            \tag{12}
\]

Equations (5) and (12) are the exact first-divergence alternative:

\[
 \boxed{
 V(P)\ge
 \max\left\{m|\mathscr B|,\ \max_{B\in\mathscr B}\Phi_{g-1}(k_B)
      \right\}.}                                            \tag{13}
\]

No source or guard overlap is suppressed in (13).

## 4. Quantitative regimes

Put `g=gamma L+O(1)` and suppose a carrier fibre has
`k_B=n^{kappa+o(1)}` guards.  Write `x=(gamma+tau)L+o(L)`, so (10) becomes

\[
       (\gamma+\tau)
       H\!\left({\gamma\over\gamma+\tau}\right)=\kappa,    \tag{14}
\]

where `H` is binary entropy.

If `tau<gamma`, then `r>x/2` and (12) has exponent

\[
                         \log\Phi_r(k_B)
                         =(\gamma+\tau+o(1))L.               \tag{15}
\]

This is a fixed-power gain over the `k_B=n^kappa` source profiles because
`H(gamma/(gamma+tau))<1`.  If `tau>=gamma`, the truncated cube is below its
middle layer and

\[
                         \log\Phi_r(k_B)
                         =(\kappa+o(1))L;                    \tag{16}
\]

the shadow may have no fixed-power surplus over the number of guards.  The
transition is `kappa=2gamma`.

Thus first divergence closes moderately heavy carrier fibres
`k_B<=n^{2gamma-o(1)}` but genuinely stalls for very high guard entropy.  The
full-layer regression below attains this stall.

## 5. Bounded-rank full-layer regression

Use the oval geometry from the positive verifier in
`RECOVERABLE_COMPONENT_TOGGLE_BRANCH.md`.  Choose two fixed labels `a,b`, a
point `z` outside one side of the oval, and a short guard arc `U` on the
opposite side.  Put a child `X` in a small region inside

\[
                              T=\{a,b,z\}                     \tag{17}
\]

such that `B={a,b}` together with each singleton `x in X` is convex.  The
whole guard arc is in convex position with `a,b,z`, and `az` remains an edge
of every source.

Fix integers `s>=r`.  For every `R in {U choose r}`, define

\[
                    G_R=\{z\}\cup R,qquad
                    A_R=B\cup G_R.                           \tag{18}
\]

Then:

1. all `A_R` are convex source faces of rank `r+3`;
2. `T` is canonical in every source;
3. `N(T)=X` in the role where `x` is interior;
4. every profile has the same carrier `A_R setminus G_R=B`;
5. all `binom(s,r)m` completion records collapse to the same `m` faces
   `B union {x}`;
6. the carrier-shadow bank is exactly

\[
                         \{B\cup\{z\}\cup D:D\subseteq U,
                             |D|\le r\},                     \tag{19}
\]

   of size `sum_{i<=r}binom(s,i)`.

This is the colex/full-layer extremizer behind (12).  Take
`s=sigma log n`, `r=gamma log n`, and insert as `X` any known order type with
maximum convex rank `O(log n)`.  Every convex face of the full configuration
uses at most `s+O(log n)=O(log n)` labels, so

\[
                              \mu(P)=O(\log n).               \tag{20}
\]

The number of actual marked profiles is
`binom(s,r)=n^{sigma H(gamma/sigma)+o(1)}`.  Hence the regression realizes
arbitrary fixed-power profile entropy on the bounded-rank slice and proves
that neither completion first-divergence nor guard shadows alone settle the
heavy branch.

However, with `s=O(L)` it supplies only `2^{O(L)}` marked occurrences.  It
cannot represent the required `Theta(V)=2^{Theta(L^2)}` global marked mass.
Making that final summation fail would require quadratically many such
carrier fibres without creating a recoverable completion bank; constructing
or excluding that arrangement remains open.

## 6. Global overlap warning

Theorem (13) is deliberately fixed-root.  Across roots, a completion output
retains only the edge `T setminus {z}`; decoding the missing root costs
`n binom(R,2)`.  The square gate of the preceding report is the rigorous way
to sum those banks.  One may not sum (5) independently over roots.

Likewise, carrier shadows from different `B` can overlap.  Equation (12)
uses one fibre at a time and makes no global disjointness claim.  A closure
requires either a decoder for the carrier fibre or a second Cauchy bank which
pays its overlap.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_heavy_profile_first_divergence.py
```

The exact rational checker takes `s=5`, `r=2`, and `m=4`.  It verifies ten
canonical marked profiles of rank five, the common carrier, complete collapse
of forty completion records to four outputs, and the exact full-layer shadow
of size `1+5+10=16`.  It also audits every forbidden pointwise guard/completion
union.

