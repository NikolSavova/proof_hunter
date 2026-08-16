# Global carrier-fibre telescope with exact overlap

**Date:** 2026-08-14.  All logarithms are base two and the empty convex
subset is counted.

## Verdict

The guard-shadow and completion alternatives from
`HEAVY_PROFILE_FIRST_DIVERGENCE.md` admit an exact global Cauchy telescope.
No copy of `V` is spent separately for each carrier fibre.

Let `c=(T,z,B)` range over canonical carrier fibres, let `k_c` be their
weighted source/guard multiplicity, let `m_c` be their singleton completion
alphabet size, and let `s_c` be the size of their rooted guard downshadow.
On a source-rank-`h` slice with uniform guard size at most `g`, put

\[
 L_S=3{h\choose3}\sum_{i=0}^{g-1}{h-3\choose i},qquad
 L_C=n{h\choose2}.                                          \tag{1}
\]

Then

\[
 \boxed{
   \sum_c k_c
   \le
   \sqrt{L_SL_C\,
          \max_c{k_c^2\over m_cs_c}}\;V(P).}                \tag{2}
\]

Using the Lovasz--Kruskal--Katona lower bound `s_c>=Phi_(g-1)(k_c)` gives

\[
 \boxed{
   \sum_c k_c
   \le
   \sqrt{L_SL_C\,
          \max_c{k_c^2\over m_c\Phi_{g-1}(k_c)}}\;V(P).}    \tag{3}
\]

This is a genuine positive gate.  If, on every fibre carrying hard mass,

\[
              m_c\Phi_{g-1}(k_c)
              \ge n^\eta L_SL_C k_c^2,                    \tag{4}
\]

then the total weighted mass is at most `n^(-eta/2)V`, contradicting its
`Omega(V)` lower bound.  Hence that branch gives a fixed-power gain.

The theorem also shows exactly why the full-layer heavy regression survives.
For a high guard layer, `Phi(k_c)` can be only `k_c n^o(1)`; it does not pay
the quadratic `k_c^2` source-pair demand plus the global decoder.  No scalable
planar rank-`O(log n)` construction carrying `Theta(V)` such mass is supplied
here.  The existing full-layer regression carries only polynomial marked
mass.  Thus (2)--(4) are rigorous global progress, not an EIC' closure.

## 1. Canonical carrier fibres

Work on the bounded source-rank slice

\[
                              |A|\le h.                      \tag{5}
\]

A canonical fibre is determined by:

* a marked root triple `T`;
* its deleted label `z in T` and retained edge `e=T setminus {z}`;
* a carrier face `B`, disjoint from the actual role-pocket `X_T`;
* a uniform family `mathcal G_c` of `k_c` distinct guards `G`, each of exact
  size `g`, with `G cap T={z}` and `B union G` a marked convex source;
* a canonical alphabet `X_c subseteq X_T`, `|X_c|=m_c`, such that

\[
                              B\cup\{x\}                     \tag{6}
\]

  is convex for every `x in X_c`.

The fibre data `mathcal G_c,X_c` are deterministic once `(T,z,B)` is known.
Each marked occurrence is assigned to exactly one fibre.

Define the rooted shadow

\[
 \mathcal D_c=
 \{\{z\}\cup D:D\subseteq G\setminus\{z\}
                     \text{ for some }G\in\mathcal G_c\}.   \tag{7}
\]

Its size is `s_c`.  The two ordinary-face banks are

\[
 \mathcal S_c=\{B\cup D:D\in\mathcal D_c\},
 \qquad
 \mathcal C_c=\{B\cup\{x\}:x\in X_c\}.                    \tag{8}
\]

Every shadow output is a subset of a source `B union G`, and every completion
output is convex by (6).  The maps in (8) are injective within one fibre, so

\[
                         |\mathcal S_c|=s_c,qquad
                         |\mathcal C_c|=m_c.                 \tag{9}
\]

## 2. Exact global overlap

> **Lemma 1 (shadow decoder).**  An ordinary face occurs in at most `L_S`
> shadow banks.

**Proof.**  A shadow output `S` contains the full root `T`: `B` contains the
retained edge and every member of `mathcal D_c` contains `z`.  Guess
`T subseteq S` in at most `binom(h,3)` ways and `z in T` in three ways.
The remaining shadow part

\[
                         D=(S\setminus B)\setminus\{z\}      \tag{10}
\]

has size at most `g-1` and avoids `T`.  Guess it among the labels of
`S setminus T`, in at most `sum_(i<=g-1)binom(h-3,i)` ways, then put
`B=S setminus ({z} union D)`.  The tuple `(T,z,B)` determines the fibre;
invalid guesses are discarded.  This proves (1).  QED.

> **Lemma 2 (completion decoder).**  An ordinary face occurs in at most
> `L_C` completion banks.

**Proof.**  A completion output contains `e`.  Guess `e subseteq C` in at
most `binom(h,2)` ways and the missing label `z` in at most `n` ways.  This
determines `T`.  Since every marked source is disjoint from `X_T`, a valid
guess has

\[
                         \{x\}=C\cap X_T,qquad B=C\setminus\{x\}.
                                                               \tag{11}
\]

Thus `(T,z,B)` and the fibre are forced.  QED.

These bounds include all roots, carriers, guards, and source contexts.  There
is no uncharged number of fibres.

## 3. Recoverable-cell Cauchy telescope

> **Theorem 3 (global carrier-fibre telescope).**  Equation (2) holds.

**Proof.**  Put

\[
                         K=\max_c{k_c^2\over m_cs_c}.         \tag{12}
\]

Then, exactly for every cell,

\[
                         k_c^2\le K
                         |\mathcal S_c||\mathcal C_c|.       \tag{13}
\]

Sum square roots and apply Cauchy together with Lemmas 1--2:

\[
\begin{aligned}
 \sum_ck_c
 &\le\sqrt K\sum_c\sqrt{|\mathcal S_c||\mathcal C_c|}\\
 &\le\sqrt{K
       \left(\sum_c|\mathcal S_c|\right)
       \left(\sum_c|\mathcal C_c|\right)}\\
 &\le\sqrt{K L_SL_C}\,V(P).
\end{aligned}                                               \tag{14}
\]

This proves (2).  The Lovasz shadow theorem applied to
`{G setminus {z}:G in mathcal G_c}` gives
`s_c>=Phi_(g-1)(k_c)`, and hence (3).  Equation (4) substituted into (2)
proves the fixed-power branch.
QED.

For nonuniform guard ranks, split into `O(h)` exact-rank classes.  This costs
only a polylogarithmic factor on the live `h=O(log n)` slice and avoids the
padding convention.

## 4. Exponent audit

Let

\[
 h=C_0L+O(1),\quad g=\gamma L+O(1),\quad
 m_c\ge n/L^a.                                             \tag{15}
\]

The decoder exponents are

\[
 \log L_C=L+o(L),qquad
 \log L_S\le
 C_0H\!\left({\gamma\over C_0}\right)L+o(L).               \tag{16}
\]

Suppose a fibre has `k_c=n^(kappa+o(1))` and

\[
                  \Phi_{g-1}(k_c)=k_c n^{\delta+o(1)}.       \tag{17}
\]

Then the factor multiplying `V` in (3) has exponent

\[
 {1\over2}\left(
       \kappa-\delta+C_0H(\gamma/C_0)\right)+o(1).          \tag{18}
\]

The `m_c` exponent cancels the missing-root exponent in `L_C`, exactly as in
the preceding profile square gate.  Therefore the global telescope closes
with a fixed power precisely when

\[
                    \delta>
                    \kappa+C_0H(\gamma/C_0).                 \tag{19}
\]

Moderately overlapping guard families can satisfy (19).  Complete high
layers have `delta=0` and fail it maximally.  Equation (19), rather than an
informal count of fibres, is the exact remaining quantitative gate.

## 5. Why the known regression is not yet global

The full-layer oval regression has one fibre with

\[
 k={s\choose r},\qquad
 s_c=\sum_{i=0}^r{s\choose i}.                              \tag{20}
\]

Taking `s,r=Theta(L)` gives `k=n^Theta(1)` and maximum face rank, hence mean,
`O(L)`.  Repeating a constant or polynomial number of recoverably marked
fibres preserves this local collision.  But the total marked mass remains
only `n^O(1)`, whereas the live hard family has `Theta(V)` mass with
`log V=Theta(L^2)`.

Producing `Theta(V)` mass would require `2^Theta(L^2)` fibre occurrences.
If their carrier or root markers are recoverable, Lemmas 1--2 and Theorem 3
sum them and may force (19).  If they are not recoverable, one must realize
quadratically many oval layers whose shadow and completion outputs collide
far beyond the explicit bounds (1); that would contradict the decoders.
No such planar construction is known here.

Thus the bounded-rank regression is an exact local sharpness example, not a
global weighted counterexample.  Conversely, Theorem 3 is a correct global
summation theorem, not by itself a proof that every heavy fibre has enough KK
surplus.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_global_carrier_fibre_telescope.py
```

The exact rational checker builds two distinct carrier fibres for one marked
root.  Each has the complete `2`nd guard layer on five labels: ten source
occurrences, shadow size sixteen, and completion size four.  It audits the
decoders, all cross-fibre overlaps, the exact local square constant
`k^2/(ms)=25/16`, and the global Cauchy inequality without spending the face
count separately for either fibre.
