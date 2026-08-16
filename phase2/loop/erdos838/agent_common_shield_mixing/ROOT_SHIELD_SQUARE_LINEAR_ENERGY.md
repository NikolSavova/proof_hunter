# The square-to-linear energy gate for marked root--shield banks

## Verdict

The exact missing hypothesis after the marked halfplane theorem is a
normalized pair-collision energy bound.  Let a canonical incidence `c`
have source weight `k_c`, one completion face `Y_c`, and a set `H_c` of
`B_c` marked halfplane faces.  Distribute `k_c/B_c` to every pair
`(Y_c,F)`, `F in H_c`.  If

\[
 \mathcal E=
 \sum_{Y,F}\left(
   \sum_{\substack{c:Y_c=Y\\F\in H_c}}{k_c\over B_c}
              \right)^2,                                  \tag{1}
\]

then

\[
                         \boxed{\sum_ck_c\le V(P)\sqrt{\mathcal E}.}  \tag{2}
\]

Consequently the sharp Cauchy hypothesis for the desired estimate is

\[
                         \mathcal E\le D^{2-2\epsilon}.                \tag{3}
\]

If the completion--halfplane pair decoder has load at most `L`, the
convenient sufficient condition is

\[
             \boxed{
             \sum_c{k_c^2\over B_c}\le{D^{2-2\epsilon}\over L}.}     \tag{4}
\]

The complete middle-layer formula does **not** imply (3) or (4).  There is
both an equality-type abstract regression and a planar common-shield
regression with complete middle layers, pair load one, and arbitrarily
large energy.

## 1. Exact weighted pair theorem

Let `mathcal V` be the ordinary-face family, `|mathcal V|=V`.  A weighted
canonical incidence consists of

\[
             c=(Y_c,H_c,k_c),\qquad
             Y_c\in\mathcal V,\quad
             H_c\subseteq\mathcal V,\quad |H_c|=B_c>0.                \tag{5}
\]

Define the pair load

\[
 \ell(Y,F)=|\{c:Y_c=Y,\ F\in H_c\}|,\qquad
 L=\max_{Y,F}\ell(Y,F).                                  \tag{6}
\]

> **Theorem 1 (sharp square-to-linear energy theorem).**  Equations
> (1)--(2) hold.  Moreover,
> \[
> \mathcal E
> \le\sum_c {k_c^2\over B_c^2}
>            \sum_{F\in H_c}\ell(Y_c,F)
> \le L\sum_c{k_c^2\over B_c}.                           \tag{7}
> \]
> Therefore either (3), or the stronger easily checked condition (4),
> implies
> \[
>                         \sum_ck_c\le D^{1-\epsilon}V.                \tag{8}
> \]

**Proof.**  Put

\[
                 w(Y,F)=
                 \sum_{c:Y_c=Y,\ F\in H_c}{k_c\over B_c}.             \tag{9}
\]

Every incidence distributes total mass `k_c` over its `B_c` pairs, so

\[
                         \sum_ck_c=\sum_{Y,F}w(Y,F).                    \tag{10}
\]

There are at most `V^2` ordered pairs of ordinary faces.  Cauchy--Schwarz
applied to (10) gives (2).

For a fixed pair, Cauchy over its `ell(Y,F)` preimages gives

\[
 w(Y,F)^2
 \le\ell(Y,F)
    \sum_{c:Y_c=Y,\ F\in H_c}{k_c^2\over B_c^2}.          \tag{11}
\]

Sum (11) and reverse the order of summation to obtain the first inequality
in (7); the second follows from `ell<=L`.  Equations (3) or (4) now give
(8).  QED.

The first expression in (7), which uses the actual pair loads rather than
their maximum, is the sharp multiplicity-sensitive sufficient condition.
The still sharper invariant is the exact energy (1) itself.

For a uniform bin with `N` incidences, common weight `k`, common bank size
`B`, and pair load `L`, condition (4) reads

\[
                         N\le {D^{2-2\epsilon}B\over Lk^2}.             \tag{12}
\]

This is the precise additional incidence-multiplicity hypothesis missing
from the marked halfplane bank.

## 2. Sharp abstract regression

Take `V` abstract ordinary faces.  For every `i in [V]`, make one incidence
whose completion is face `i`, whose halfplane bank is the entire same
`V`-face family, and whose weight is `k`.  Then

\[
 B_c=V,\qquad L=1,\qquad
 \sum_ck_c=Vk,\qquad
 \mathcal E=k^2,\qquad
 \sum_c{k_c^2\over B_c}=k^2.                              \tag{13}
\]

Thus (2) and both inequalities in (7) are equalities.  A joint pair decoder
of load one gives no control whatever on `k`; an energy or multiplicity
hypothesis of the scale (3)--(4) is unavoidable under the stated abstract
axioms.

More generally, `N` distinct completions with one common `B`-face bank have

\[
                         \mathcal E={Nk^2\over B}.                       \tag{14}
\]

This is the equality model for (12).

## 3. Complete middle layers do not control the energy

Suppose a complete core has size `s`, its source weight is

\[
                         k={s\choose\lfloor s/2\rfloor},                \tag{15}
\]

and its marked halfplane bank has only the guaranteed size
`B=2^{ceil((q-1)/2)}`.  Even for one incidence,

\[
 {k^2\over B}
 \ge {2^{2s-\lceil(q-1)/2\rceil}\over(s+1)^2}.            \tag{16}
\]

In the central range `q=s+O(s)`, this is exponentially large.  Completeness
relates `k` to `s`; it neither bounds the number `N` of canonical incidences
nor supplies the inverse-bank energy (4).

The failure persists when the cells are genuine planar root--shield data,
not merely an abstract set system.

## 4. Planar common-shield regression

Fix an integer `a>=1`.  On a rational circle choose

* opposite vertices `u=(-1,0),v=(1,0)` and `z=(0,1)`;
* `2a` lower-arc vertices `L` in symmetric pairs about the vertical axis;
* `2a` additional upper-arc vertices, also in symmetric pairs.

Put

\[
                         Q=\{u,v,z\}\cup L\cup A,\qquad |Q|=4a+3.    \tag{17}
\]

Choose a rational `eta in (0,1)` avoiding the finitely many chords through
`Q`, and set `x=(0,eta)`.  Then the ambient set is in general position and

\[
                         x\in\operatorname{int}\triangle(u,v,z).       \tag{18}
\]

For every `a`-subset `R subseteq L`, define

\[
\begin{aligned}
 B_R&=\{u,v\}\cup R,&Y_R&=B_R\cup\{x\},\\
 U_R&=Q\setminus(B_R\cup\{z\}),& |U_R|&=3a.             \tag{19}
\end{aligned}
\]

Every `Y_R` is convex: all its points other than `x` have nonpositive
vertical coordinate, while `x` has positive coordinate; the old circle
vertices remain exposed because `x in conv(Q)`.  Every complete-layer
source

\[
             B_R\cup\{z\}\cup S,\qquad
             S\in{U_R\choose\lfloor3a/2\rfloor},          \tag{20}
\]

is a subset of the convex polygon `Q`, hence convex.  The common top shield
is exactly `Q`, the retained edge is the common `uv`, and all cells have
the complete middle-layer weight

\[
                         k={3a\choose\lfloor3a/2\rfloor}.               \tag{21}
\]

The line `xz` is vertical and has exactly `2a+1` points of `Q setminus {z}`
on each side.  With a fixed tie break, all cells therefore have the **same**
marked halfplane bank, of size

\[
                         B=2^{2a+1}.                                  \tag{22}
\]

Their completion faces are distinct, so the pair load is one.  There are

\[
                         N={2a\choose a}                                \tag{23}
\]

cells and the exact energy is

\[
 \boxed{
 \mathcal E=\sum_c{k_c^2\over B_c}
 ={\binom{2a}{a}\binom{3a}{\lfloor3a/2\rfloor}^2
   \over2^{2a+1}}.}                                      \tag{24}
\]

In particular,

\[
                         \mathcal E\ge {2^{6a-1}
                          \over(2a+1)(3a+1)^2},             \tag{25}
\]

so it is exponentially unbounded despite complete middle layers and the
best possible pair decoder.

The total marked mass satisfies

\[
 \sum_ck_c
 \ge {2^{5a}\over(2a+1)(3a+1)},                          \tag{26}
\]

whereas the ambient point set has only `4a+4` labels and hence trivially
`V(P)<=2^{4a+4}`.  Thus the marked mass can exceed `V(P)` by
`2^{a-O(log a)}`.  This is an exact planar square-to-linear regression.
It is not by itself a counterexample to EIC': it does not impose the full
external degree-`D` record system.  It proves that complete middle-layer
weights, root geometry, and pair recoverability alone cannot supply (3).

## 5. Consequence for the root--shield program

The marked halfplane theorem supplies a valid pair bank and a polynomial
pair decoder.  To obtain a linear-in-`V` EIC estimate, one must additionally
prove one of the following equivalent-scale facts on the live slice:

1. the exact normalized pair energy (1) is at most `D^{2-2epsilon}`;
2. the load-weighted inverse-bank energy in the first part of (7) has that
   bound;
3. the simpler inverse-bank sum (4) holds; or
4. in a uniform bin, the number of incidences obeys (12).

The planar regression shows that none follows from local convexity,
complete middle layers, or the bounded pair decoder.  A successful proof
must use an additional global prevalence constraint tying the number of
canonical completions to their source weights and halfplane ranks.

## 6. Verification artifact

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_root_shield_square_linear_energy.py
```

The verifier checks the exact weighted identities and Cauchy inequalities,
the equality abstract model, the closed forms (24)--(25), and a rational
`a=2` planar instance including every completion and every complete
middle-layer source.
