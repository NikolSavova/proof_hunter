# External blocker alphabets: exact energy splitting and the diagonal residue

**Date:** 2026-08-15.  All logarithms are base two and the empty convex
subset is counted.

## Verdict

Restoring the full selected blocker alphabet gives an exact identity, but it
does **not** by itself force the square--linear energy in `(3aa)` below the
required scale.  The alphabet energy is the sum of

1. a diagonal inverse-bank term, which has no completion collision at all;
2. a genuine collision term, every summand of which already fixes one common
   completion face.

For a uniform alphabet of size `D`, random one-letter thinning satisfies

\[
 \boxed{\displaystyle
 \mathbb E_\xi\mathcal E(\xi)
 ={\mathcal J\over D}+{\mathcal C\over D^2},\qquad
 \mathcal E_D=D^2\mathbb E_\xi\mathcal E(\xi)-(D-1)\mathcal J,}
                                                               \tag{1}
\]

where `mathcal E_D=mathcal J+mathcal C` is the full-alphabet energy.
Thus the apparent averaging gain is real only for cross-cell collisions; the
diagonal is thinned by `1/D`, not `1/D^2`.

There is nevertheless a sharp global discharge which was absent from the
one-letter regression.  If `s` distinct source faces each select `D`
blockers, and `X` is the union of the selected labels, then

\[
       |E|=sD,\qquad
       V(P)\ge\max\{s,V(P|X)\}\ge\max\{s,f(D)\}.          \tag{2}
\]

Consequently

\[
 \boxed{\displaystyle
 { |E|\over V(P)}\le
 \min\left\{D,{sD\over f(D)}\right\}.}                   \tag{3}
\]

In particular, for every fixed `epsilon>0`, the desired fixed-power charge

\[
                         |E|\le D^{1-\epsilon}V(P)          \tag{4}
\]

holds whenever

\[
                         s\le {f(D)\over D^\epsilon}.       \tag{5}
\]

Using the established planar bound
`log f(D)>=(1/4-o(1))(log D)^2`, failure of this detached-alphabet discharge
forces

\[
             \log s\ge(1/4-o(1))(\log D)^2
                         -\epsilon\log D.                  \tag{6}
\]

Hence the exact alphabet-aware trichotomy is:

* low pair energy closes by `(3aa)`;
* low source-support entropy closes by the detached face complex of the
  actual selected alphabet;
* the remaining diagonal branch has quadratic source entropy in `log D`,
  while the remaining off-diagonal branch is genuine common-completion
  collision energy.

The last branch can be refined to a fixed completion, blocker, and retained
edge at only a polynomial rank loss.  What is **not** true is that high total
energy alone fixes such a profile.  A scalable planar common-top construction
below has a full cap `D`, pair load one, maximum completion multiplicity one,
and `mathcal E_D>D^2`.  It is nevertheless strongly EIC-valid because its
actual common alphabet contributes the detached shield bank `F(X)` from
`(2)`.  This is the sharp status: the one-letter common-top regression cannot
be promoted to a global counterexample, even after replacing its blocker
cluster by an arbitrary low-face order type.

## 1. Full-alphabet pair energy

Let `c` range over canonical central cells.  Cell `c` has marked source
weight `k_c` and an actual selected alphabet `X_c` of size exactly `D`.
For every `x in X_c`, let

* `Y_(c,x)` be its ordinary completion face;
* `mathcal H_(c,x)` be its marked half-plane bank;
* `B_(c,x)=|mathcal H_(c,x)|>0`.

Write `a=(c,x)` for an alphabet occurrence and put

\[
 \alpha_a(F)={k_c\over B_a}{\bf1}_{F\in\mathcal H_a}.
                                                               \tag{7}
\]

The full selected mass and pair energy are

\[
\begin{aligned}
 M&=D\sum_ck_c
   =\sum_{Y,F}\sum_{a:Y_a=Y}\alpha_a(F),\\
 \mathcal E_D
  &=\sum_{Y,F}\left(\sum_{a:Y_a=Y}\alpha_a(F)\right)^2.
                                                               \tag{8}
\end{aligned}
\]

There are at most `V(P)^2` ordered face pairs, so exactly as in `(3aa)`,

\[
                         M\le V(P)\sqrt{\mathcal E_D}.       \tag{9}
\]

Thus `mathcal E_D<=D^(2-2epsilon)` proves (4).

Expand the square in (8).  The diagonal and collision terms are

\[
\begin{aligned}
 \mathcal J
   &=\sum_a\sum_F\alpha_a(F)^2
     =\sum_{c,x}{k_c^2\over B_(c,x)},\\
 \mathcal C
   &=\sum_{a\ne a':Y_a=Y_(a')}
       {k_ck_(c')|\mathcal H_a\cap\mathcal H_(a')|
        \over B_aB_(a')}.
                                                               \tag{10}
\end{aligned}
\]

Every term is nonnegative and

\[
                         \mathcal E_D=\mathcal J+\mathcal C. \tag{11}
\]

In the root--shield setting, different letters of one cell give different
completion faces `B_c union {x}`.  Choose independently a uniform letter
`xi_c in X_c` in every cell, and let `mathcal E(xi)` be the energy of the
resulting one-letter system.  A diagonal occurrence survives with
probability `1/D`, while a colliding pair necessarily comes from distinct
cells and survives with probability `1/D^2`.  This proves (1).

Equation (1) is the requested exact averaging identity.  It also identifies
its limitation: even when `mathcal C=0`, the full energy is
`mathcal J`, not `D^2` times a collision-controlled quantity.

## 2. Collision energy really does fix the root--shield profile

Assume every completion has rank at most `q`.  An occurrence carries its
actual blocker `x in Y` and retained edge
`e subseteq Y setminus {x}`.  For a fixed completion `Y`, there are at most

\[
                         K=q{q-1\choose2}                   \tag{12}
\]

possible profiles `pi=(x,e)`.  Put

\[
 w(Y,\pi,F)=
   \sum_{a:(Y_a,x_a,e_a)=(Y,\pi)}\alpha_a(F),
 \qquad
 \mathcal E_* =\sum_{Y,\pi,F}w(Y,\pi,F)^2.                \tag{13}
\]

Cauchy within the at most `K` profile classes gives

\[
                         \boxed{\mathcal E_*\ge
                                  {\mathcal E_D\over K}.}   \tag{14}
\]

The diagonal part of `mathcal E_*` is still exactly `mathcal J`.  Therefore
its genuine within-profile collision part `mathcal C_*=mathcal E_*-mathcal J`
obeys

\[
             \boxed{\mathcal C_*\ge
                    {\mathcal C-(K-1)\mathcal J\over K}.}  \tag{15}
\]

In particular, if
`mathcal C>=2(K-1)mathcal J`, then
`mathcal C_*>=mathcal C/(2K)`.  Every term counted by `mathcal C_*` has one
fixed ordinary completion `Y`, one actual blocker `x`, one carrier
`B=Y setminus {x}`, and one retained edge `e`.  Only the missing roots and
top shields vary, so these are precisely the recoverable root--shield stars.

If the hypothesis fails, then

\[
                 \mathcal E_D<(2K-1)\mathcal J,            \tag{16}
\]

which is the diagonal-dominated residue.  Thus no genuine collision is lost
in passing to the profile formulation; the obstruction to localization is
exactly the diagonal term.

## 3. Detached-alphabet/source-projection theorem

> **Theorem 1 (source--alphabet discharge).**  Let `mathcal S` be `s`
> distinct ordinary source faces and let `E` be a simple selected incidence
> graph in which every source has degree exactly `D`.  If `X` is the union
> of its blocker labels, then (2)--(3) hold.  Consequently (5) implies (4).

**Proof.**  The sources themselves are `s` distinct global ordinary faces,
so `V(P)>=s`.  Also `|X|>=D`.  Every convex face of the induced point set
`P|X` is an ordinary face of `P`, whence
`V(P)>=V(P|X)>=f(|X|)>=f(D)`.  The last monotonicity follows by restricting
`X` to any `D` labels.  Since the selected graph is simple and left
`D`-regular, `|E|=sD`.  Divide this identity by the two lower bounds for
`V(P)` to obtain (3).  Condition (5) then gives (4).  QED.

This theorem allows completely variable alphabets `X_c`: only their actual
union is used.  It also makes clear why a one-letter local regression is not
a full selected-cap regression.  Once the other `D-1` labels are restored,
their induced face complex is a legitimate unrestricted shield bank whether
or not it mixes with the carrier.

Combining Theorem 1 with (9), (15), and the established quarter-coefficient
lower bound gives the following rigorous global reduction.

> **Corollary 2 (alphabet-aware energy trichotomy).**  Fix
> `epsilon>0`.  A simple `D`-regular selected system is discharged if either
> `mathcal E_D<=D^(2-2epsilon)` or `s<=f(D)/D^epsilon`.
> Otherwise its source support satisfies (6).  Moreover, if its collision
> term is at least `2(K-1)` times its diagonal term, a `1/(2K)` share of that
> collision energy lies in actual fixed `(Y,x,e)` root--shield profiles.
> The sole unlocalized case is diagonal-dominated **and** has quadratic
> source entropy in `log D`.

This is not a proof of EIC'.  It removes the proposed low-entropy diagonal
counterexample and identifies the genuinely global remainder.

## 4. Full-cap planar common-top regression

The diagonal obstruction is geometrically real.  Fix `a>=2`.  On a rational
circle choose

* `u=(-1,0)`, `v=(1,0)`, and `z=(0,1)`;
* a `2a`-point pool `L` on a short lower-left arc;
* a `3a`-point pool `U` on the right half of the circle.

Put

\[
                         Q=\{u,v,z\}\cup L\cup U,
             \qquad |Q|=5a+3.                             \tag{17}
\]

This is one common convex top shield.  Choose a sufficiently small open disk
`Delta` around a point `(0,eta)`, `0<eta<1`, so that every `x in Delta`
satisfies all of the following open conditions:

1. `x` is strictly inside `triangle(u,v,z)`;
2. for every `R in binom(L,a)`, the completion
   `Y_(R,x)=\{u,v\} union R union \{x\}` is convex;
3. the line `xz` has `L union {u}` on one side and `U union {v}` on the
   other.

Insert in `Delta` a generic positive similarity copy `X` of **any**
`D`-point general-position order type.  Cross-collinearities with `Q` are
avoided by a generic perturbation inside `Delta`.  Take

\[
                         D=2^a,qquad
 N={2a\choose a},qquad
 k={3a\choose\lfloor3a/2\rfloor}.                         \tag{18}
\]

For `R in binom(L,a)` and
`S in binom(U,floor(3a/2))`, define the source

\[
                         A_(R,S)=\{u,v,z\}\cup R\cup S.    \tag{19}
\]

All `Nk` sources are distinct subsets of the convex polygon `Q`, hence are
convex.  Every source selects every `x in X`.  The addition is blocked
because `x` lies inside the retained root triangle, while deleting
`{z} union S` leaves the convex completion `Y_(R,x)`.  Thus this is a simple
selected system of exactly

\[
                         M=DNk                              \tag{20}
\]

records, with the full common alphabet `X`.

For the line `xz`, the richer side is always `U union {v}`, of size
`3a+1`.  The marked half-plane bank therefore has exact size

\[
                         B=2^{3a+1}.                       \tag{21}
\]

The completion `Y_(R,x)` recovers both `R` and `x`, so every ordered
completion--halfplane pair has decoder load one and every completion has
multiplicity one.  Hence `mathcal C=0` and

\[
 \boxed{\displaystyle
 \mathcal E_D=\mathcal J
  ={D\binom{2a}{a}
          \binom{3a}{\lfloor3a/2\rfloor}^{\!2}
      \over2^{3a+1}}.}                                    \tag{22}
\]

Using `binom(m,floor(m/2))>=2^m/(m+1)`,

\[
 \mathcal E_D\ge
 {2^{6a-1}\over(2a+1)(3a+1)^2},                           \tag{23}
\]

so `mathcal E_D>D^2`, and hence
`mathcal E_D>D^(2-2epsilon)`, for every fixed `epsilon>0` and all
sufficiently large `a`.  There is no common completion fibre to extract.

The construction nevertheless cannot threaten EIC'.  Its source support is
only

\[
                         s=Nk\le2^{5a},                    \tag{24}
\]

whereas the actual selected alphabet satisfies

\[
              V(P)\ge V(P|X)\ge
                    2^{(1/4-o(1))a^2}.                    \tag{25}
\]

Since `M<=2^(6a)`, equation (25) implies

\[
                         M\le D^{1-\epsilon}V(P)            \tag{26}
\]

for every fixed `0<epsilon<1` and all sufficiently large `a`.

The selected-cap normalization can be made exact.  Every source in (19) has
rank

\[
                         r=a+\lfloor3a/2\rfloor+3.          \tag{27}
\]

Adjoin generic padding until the ambient size is
`n=D2^r`.  Adding labels changes none of the displayed induced convexity or
circuit statements, and now `n/2^r=D` exactly.  The padding can only add
ordinary faces.  Thus the regression retains the fixed tangent edge `uv`,
the actual marked repair occurrence, one common top shield, and a full
selected cap, but it is forcibly paid by the detached alphabet shield.

In particular, replacing the small cluster by a projectively universal or
otherwise low-face order type does not help: the universal lower bound in
(25) applies to every order type.  The only possible global diagonal
obstruction must therefore have the quadratic source entropy forced by (6),
not the linear-entropy common-top architecture above.

## 5. Actual planar carrier--root rectangles

The formal carrier--root rectangle has one additional planar constraint
which can be stated exactly.  Fix a blocker `x` and root `z`, and make a
graph on possible carrier labels by joining `u,v` when

\[
                         x\in\operatorname{int}
                                  \triangle(u,v,z).         \tag{28}
\]

> **Lemma 3 (rooted carrier graphs are Ferrers).**  The graph in (28) is
> bipartite across the two open sides of the line `xz`.  After ordering the
> two sides appropriately, its adjacency matrix is a Ferrers diagram.  More
> explicitly, apply an affine map with `x=(0,0)` and `z=(0,1)`.  Write
> 
> \[
> u=(-a,b),\quad v=(c,d),\qquad a,c>0.
> \]
> 
> Then
> 
> \[
> x\in\operatorname{int}\triangle(u,v,z)
>       \quad\Longleftrightarrow\quad {b\over a}+{d\over c}<0.       \tag{29}
> \]
> 
> Consequently, if the graph has `m` edges, it contains a complete
> bipartite subgraph with at least
> 
> \[
>                         {m\over H_s}                       \tag{30}
> \]
> 
> edges, where `s` is the smaller side size and
> `H_s=sum_(i=1)^s1/i`.

**Proof.**  A containing triangle must have `u,v` on opposite sides of
`xz`.  The segment `uv` meets the vertical axis at height

\[
                         {cb+ad\over a+c}.
\]

The origin is inside `triangle(u,v,z)` exactly when this intercept is
negative, which is (29).  Sorting the values `b/a` increasingly and `d/c`
increasingly makes every neighbourhood an initial interval, proving the
Ferrers assertion.

If its nonincreasing row degrees are `d_1,...,d_s`, the first `i` rows and
first `d_i` columns form `K_(i,d_i)`.  Put
`R=max_i i d_i`.  Then `d_i<=R/i`, so
`m=sum_i d_i<=R H_s`, proving (30).  QED.

Thus the all-pairs carrier graph in the purely four-local rectangle is not
planar: it contains carrier triangles.  This fact alone gives no fixed
power, however.  Complete bipartite Ferrers graphs retain quadratic size
and are genuinely planar.

> **Proposition 4 (scalable planar carrier--root rectangle with shield).**
> Fix integers `l,r,g,h,m>=1` and put `p=2h+1`.  There is a planar
> general-position configuration with:
> 
> * carrier pools `L,R` of sizes `l,r`, and every `uv in L times R`;
> * `g` disjoint root blocks `W` of size `p`;
> * an `m`-label common blocker alphabet `X`;
> * for every `(u,v,z) in L times R times W` and `x in X`, the rooted
>   circuit `x in int triangle(u,v,z)`;
> * complete middle weight `binom(2h,h)` at every carrier--root cell;
> * completion `\{u,v,x\}` independent of the root and a `2^h` marked
>   one-sided bank independent of the carrier.
> 
> An underlying source has exactly `h+1` possible root marks.  The ordered
> completion--halfplane pair has load at most `p`.  The realization also has
> the detached convex shield
> 
> \[
>                      L\cup R\cup\bigcup W,                \tag{31}
> \]
> 
> and hence at least `2^(l+r+gp)` ordinary faces.

**Construction and proof.**  On a circle take three sufficiently short arcs
around the vertices of a triangle containing an open disk `Delta`: put `L`
on the lower-left arc, `R` on the lower-right arc, and all root blocks on the
upper arc.  Shrink the arcs so that `Delta` lies inside every transversal
triangle `uvz`.  Insert in `Delta` a generic similarity copy of the desired
`m`-point alphabet.

For a root block `W` and `z in W`, the other `2h` roots are split by the line
`xz`; choose the richer side `H_(z,x)`, so `|H_(z,x)|>=h`, and retain a
canonical `h`-subset if it is larger.  Lemma 1 of the marked halfplane bank
shows that

\[
             \{x,z\}\cup S,\qquad S\subseteq H_(z,x),      \tag{32}
\]

is convex.  It is independent of `u,v`.  Conversely the completion
`{u,v,x}` is independent of `z`.  The completion recovers `(u,v,x)`; an
output (32) contains its root mark, so at worst one of the `p` labels in its
block can be the mark.  This proves the pair-load assertion.

For every `z`, use the full middle layer of `W setminus {z}`.  A source with
root set `T in binom(W,h+1)` is represented once for every `z in T`, hence
exactly `h+1` times.  Finally the three outer arcs all lie on the same circle,
so (31) is convex and supplies its full Boolean face complex.  All
containments and general-position conditions are open, so rational
coordinates exist.  QED.

Proposition 4 settles the last proposed alternative at the local level: a
carrier--root circuit rectangle is **not planar-forbidden**.  What planarity
does in the natural realization is expose a detached outer shield.  The
missing global theorem must prove that some comparable shield or forward
two-ended bank survives after quadratic-entropy variation of the three
arcs; four-locality and the logarithmic source-mark load do not do this.

## 6. Verification artifact

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_external_alphabet_energy_trichotomy.py
```

The exact checker verifies (1), (11), and (14)--(15) on a colliding abstract
alphabet system.  It then constructs the rational `a=2,D=4` common-top
instance, exhaustively checks all 120 distinct sources and 480 selected
records, the blocked root triangle, all completions and half-plane faces,
pair load and completion multiplicity one, and the exact diagonal energy
`75>D^2`.  Finally it checks (22)--(24) through `a=100` and the exact cap
padding arithmetic.  A second rational three-arc instance checks (29), a
complete bipartite carrier axis, all carrier--root circuits, the middle-layer
mark load, and the pair decoder in Proposition 4.
