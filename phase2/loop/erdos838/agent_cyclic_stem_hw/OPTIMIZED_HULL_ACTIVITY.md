# Optimized hull activity and the exterior-incidence gate

**Date:** 2026-08-14  
**Verdict:** this does not yet prove Erdős 838, but it removes the scalar
label-supply obstruction in the hard `delta<1` branch.  The full activity
identity gives an optimized entropy bound and, more importantly, a sharp
low-`q` tail bound.  At rank `r`, its exponent matches the RNP demand
`2^(ell-r)` exactly; the unique critical scale is `r=ell/2`.

Consequently, with an `n^o(1)` loss, every low-extension rank splits into

1. a low-exterior-label subfamily which **already satisfies RNP**, and
2. a residual subfamily in which **every source** has
   `2^(ell-r)/n^o(1)` exterior blocked labels.

One sufficient remaining theorem would be a global exterior-incidence
bound, but this is strictly stronger than the capped Hall statement needed
for RNP: only `D_r` blockers per residual source have to be selected and
routed.  The exact Pascal stress test below makes that distinction
important.  Gordon's cyclic stems identify the one-root geometry but do not
supply the required capped capacity estimate.  A fixed-root entropy
reduction is still promising, but its unbalanced singleton-split chain is a
genuine remaining gate.

All logarithms are base two.  A convex face means a subset in convex
position, and

\[
 q(A)=|P\setminus\operatorname{conv}(A)|.
\]

For a convex face `A`, let `u(A)` be its addable degree and let `e(A)` be the
number of exterior points which are blocked for `A`.  Then

\[
 q(A)=u(A)+e(A).                                      \tag{1}
\]

## 1. The exact hull-event partition

> **Theorem 1 (hull activity).**  For every planar point set `P` and every
> `0<p<1`,
> \[
>  \boxed{\sum_{A\text{ convex}}p^{|A|}(1-p)^{q(A)}=1.} \tag{2}
> \]

**Proof.**  Select a random subset `T subset P` by retaining every point
independently with probability `p`, and put

\[
 A=\operatorname{ext}(\operatorname{cl}T).
\]

For a fixed convex face `A`, this event occurs exactly when every point of
`A` is retained, every point outside `conv(A)` is omitted, and the points in
`cl(A)-A` are arbitrary.  Its probability is therefore
`p^|A|(1-p)^q(A)`.  The possible hulls partition the sample space.  QED.

This is the full-activity version of the Boolean interval partition.  It is
valid for arbitrary finite convex geometries; planarity enters only when we
classify the exterior blocked incidences in Section 5.

## 2. Optimizing gives both a mean theorem and a tail theorem

Define

\[
 \Psi(r,Q)=(r+Q)H_2\!\left({r\over r+Q}\right)
 =r\log\left(1+{Q\over r}\right)
  +Q\log\left(1+{r\over Q}\right).                 \tag{3}
\]

The limiting value at `Q=0` is zero.

> **Theorem 2 (optimized hull entropy).**  Let `S` be any family of `M`
> convex rank-`r` faces, and put `qbar=E_S q(A)`.  Then
> \[
>  \boxed{\log M\le\Psi(r,\bar q).}                 \tag{4}
> \]
> More strongly, for every `Q>=0`,
> \[
>  \boxed{
>  M_{r,\le Q}:=|\{A:|A|=r,\ q(A)\le Q\}|
>  \le2^{\Psi(r,Q)}.}                               \tag{5}
> \]

**Proof.**  Restrict (2) to `S`.  Since `x -> (1-p)^x` is convex,

\[
 1\ge Mp^r\mathbb E_S(1-p)^{q(A)}
   \ge Mp^r(1-p)^{\bar q}.                          \tag{6}
\]

The optimum is `p=r/(r+qbar)`, which proves (4).  For (5), every summand
with `q(A)<=Q` is at least `p^r(1-p)^Q`; optimize again at
`p=r/(r+Q)`.  QED.

The elementary estimate

\[
 \Psi(r,Q)\le r\log\!\left(e\left(1+{Q\over r}\right)\right) \tag{7}
\]

follows from `x ln(1+1/x)<=1`.  Inverting it gives the convenient explicit
consequence

\[
 \boxed{
 \bar q\ge r\left({2^{\log M/r}\over e}-1\right).} \tag{8}
\]

For a low-extension family, (1) further gives

\[
 \mathbb E_S e(A)\ge
 r\left({2^{\log M/r}\over e}-1\right)-4(r+1).     \tag{9}
\]

Unlike the earlier `Omega(r^2)` lemma, (8) is exponential in
`(log M)/r`.  Unlike a mean-only statement, (5) can discard every source
with too few labels.

## 3. The exponent matches RNP, with one critical scale

Put

\[
 L=\log n,\qquad \ell=\lceil L\rceil,
 \qquad D_r=2^{\ell-r}.                             \tag{10}
\]

The current Erdős--Szekeres bound implies

\[
 \log V(P)\ge {L^2\over4}-E(L),
 \qquad E(L)=O(L^{3/2}\sqrt{\log L})=o(L^2).        \tag{11}
\]

For completeness, take `k=floor(L/2)` and let `m=ES(k)`.  Every `m`-set
contains a convex `k`-set, so double counting gives

\[
 v_k(P)\ge{\binom nk\over\binom mk}\ge(n/m)^k.    \tag{12}
\]

The bound `log ES(k)<=k+O(sqrt(k log k))` now gives (11).  One source for
the Erdős--Szekeres estimate is Holmsen--Mojarrad--Pach--Tardos,
[*Two extensions of the Erdős--Szekeres problem*](https://arxiv.org/abs/1710.11415).

In the `delta<1` hard branch, the existing rank-width theorem supplies a
constant-density low-extension slice `S subset N_r`, with

\[
 |S|\ge c_0V(P),\qquad r=\mu_1+O(1).                \tag{13}
\]

Apply (8), (11), and (13).  Up to lower-order factors,

\[
 \log\mathbb E_S q
 \ge {L^2\over4r}-{E(L)\over r}+\log r-O(1).        \tag{14}
\]

The main exponent is never below the RNP demand exponent because

\[
 \boxed{
 {L^2\over4r}-(L-r)={\left(r-L/2\right)^2\over r}\ge0.} \tag{15}
\]

Thus, for `r=rho L`, the label exponent is `1/(4rho)` while the demand
exponent is `1-rho`.  Equality occurs only at `rho=1/2`; away from this
scale (15) gives an exponential surplus.  At the critical scale, the error
in (11) costs only

\[
 2^{O(\sqrt{L\log L})}=n^{o(1)}.                   \tag{16}
\]

In particular,

\[
 \mathbb E_Sq(A)\ge {D_r\over n^{o(1)}}.           \tag{17}
\]

This is the scale-correct version of the label-supply theorem.  The weaker
`n^(1/4-o(1))` statement loses the crucial comparison with `D_r`.

## 4. Pointwise tail upgrade: half of RNP is now proved

The following makes the `n^o(1)` loss explicit enough to audit.

> **Theorem 3 (low-label RNP).**  Suppose (11) holds with `E(L)=o(L^2)`.
> Put
> \[
>  t=8(E(L)/L+1),\quad K_0=2^t,
>  \quad K=16(L+1)K_0.                              \tag{18}
> \]
> For all sufficiently large `n` and every `1<=r<ell`, the family
> \[
>  \mathcal L_r=
>  \{A\in N_r:q(A)\le D_r/K_0\}
> \]
> satisfies
> \[
>  \boxed{|\mathcal L_r|\le K{V(P)\over D_r}.}     \tag{19}
> \]
> If `D_r>K`, every source in the complementary family
> `H_r=N_r-L_r` has
> \[
>  \boxed{e(A)>{D_r\over2K_0}.}                    \tag{20}
> \]

**Proof.**  If `D_r<=K`, (19) is the trivial bound `|L_r|<=V`.  Otherwise
put `Q=D_r/K_0`; then `Q>16(L+1)>=r`.  By (5) and (7), with
`c=log(2e)`,

\[
 \log|\mathcal L_r|
 \le r(\ell-r-t-\log r+c).                         \tag{21}
\]

On the other hand,

\[
 \log(KV/D_r)
 \ge {L^2\over4}-E(L)-\ell+r+t+4+\log(L+1).        \tag{22}
\]

Subtracting (21) from (22), and using `0<=ell-L<1`, leaves at least

\[
 (r-L/2)^2+r(t-c)-E(L)-L+O(t+\log L).              \tag{23}
\]

The minimum of the first two terms over real `r>=0` is
`(t-c)L/2-(t-c)^2/4` when `t-c<L`.  With (18), this exceeds
`E(L)+L-O(t+log L)` for all sufficiently large `L`; if `t-c>=L`, the
square term alone is stronger.  This proves (19).

For a complementary source, `q(A)>Q`.  Since `u(A)<=4(r+1)` and
`Q>16(L+1)`, (1) gives `e(A)>Q-4(r+1)>Q/2`, proving (20).  QED.

With the quantitative error in (11), both `K_0` and `K` are
`2^O(sqrt(L log L))=n^o(1)`.  Thus the only unresolved part of rankwise
near-maximality is the family in (20).  There is no longer an average-label
or low-label-tail gap.

An `n^o(1)` version of RNP is sufficient for Erdős 838: the standard split
of the near-maximal potential gives `NPM/V=O(log K)=o(L)`, hence
`mu_1>=L-o(L)` in the hard branch, and the activity-compensation/deletion
argument then gives the desired `n^o(1)` half-weight envelope.

## 5. A sufficient stronger gate: full exterior-incidence capacity

Let

\[
 \mathcal I_r=\{(A,p):A\in\mathcal H_r, p\text{ is exterior and blocked
 for }A\}.
\]

Theorem 3 gives

\[
 |\mathcal I_r|>{D_r\over2K_0}|\mathcal H_r|.       \tag{24}
\]

Therefore the following stronger statement would complete RNP (and hence
the asymptotic problem):

\[
 \boxed{|\mathcal I_r|\le n^{o(1)}V(P)}             \tag{EIC}
\]

or, equivalently, a map from **all** exterior incidences to ordinary convex
target faces with `n^o(1)` maximum inverse load.  Combining `(EIC)` with (24)
gives `|H_r|<=n^o(1)V/D_r`.

The converse is false as a matter of logic.  RNP may discard all but about
`D_r` labels at a source with `e(A)>>D_r`; its selected incidence graph can
have low congestion even when the sum in `(EIC)` is enormous.  Thus a
counterexample to full `(EIC)` redirects the attack to capped Hall routing
but does not refute the optimized reduction.

The planar ear theorem gives an exact two-face encoding.  For
`(A,p) in I_r`, put

\[
 I=A\setminus\operatorname{ext}(A+p),\qquad
 B=\operatorname{ext}(A+p).
\]

Then `I` is a nonempty cyclic interval, `B=(A-I)+p`, both `I` and `B` are
convex, and

\[
 |I|+|B|=r+1.                                      \tag{25}
\]

Moreover `(A,p)->(I,B,p)` is injective.  Hence

\[
 |\mathcal I_r|
 \le\sum_{i=1}^{r-2}(r-i+1)v_i v_{r-i+1}.          \tag{26}
\]

This is not yet `(EIC)`: it encodes an incidence by a **pair** of faces,
and replacing one factor by `V` loses another factor of `V`.  Gordon's
minimal feasible sets and complement-of-adjacent-stems theorem provide the
correct cyclic one-root reset, but their expected-rank formula is under the
hull-event weights `p^r(1-p)^q`.  For fixed `r`, every nonnegative mixture
of these weights decreases with `q`; it proves low-`q` upper tails such as
(5), not an upper bound on the unweighted high-`q` incidence mass (24).
This is why one-root expected rank does not finish the argument.

### Fixed-root entropy remains a plausible recursion

Averaging (24) over the `n` exterior labels gives a point `p` shared by at
least

\[
 {D_r|\mathcal H_r|\over2K_0n}                     \tag{27}
\]

sources.  Losing the root identity costs only `L` bits.  Fixing the split
size in (25) costs `O(log r)` further bits (and fixing tangent endpoints,
if desired, costs only `O(L)` bits).  At a hard constant-density slice,
the resulting fixed-root family still has `Theta(L^2)-O(L)` bits.

This produces the following rigorous entropy interface: for some `i`, a
quadratically large fixed-root source family injects into pairs

\[
 (I,B),\qquad |I|=i,\quad |B|=r-i+1,\quad p\in B. \tag{28}
\]

More explicitly, let `X_i(p)` and `Y_i(p)` be the two projection families
of hidden intervals `I` and retained faces `B-p`, respectively.  Since
`|I|+|B-p|=r`, (24), pigeonholing over `p` and `i`, and injectivity give

\[
 \boxed{
 \log|X_i(p)|+\log|Y_i(p)|
 \ge \log|\mathcal H_r|+\log D_r
      -\log(2K_0)-L-\log r.}                       \tag{29}
\]

Since `log D_r=L-r+O(1)`, the root-label cost cancels and (29) becomes

\[
 \log|X_i(p)|+\log|Y_i(p)|
 \ge\log|\mathcal H_r|-r-o(L).                     \tag{30}
\]

This is the exact source-coding reason the route remains plausible: a
high-entropy node pays only its current rank, not `L`, to choose a common
outside label.  If this cancellation can be repeated at every descendant
node, then the accumulated unbalanced cost is
`r+(r-1)+...=r^2/2+O(r)`, the desired quadratic scale.

A balanced sequence of such splits is compatible with a quadratic-potential
induction, because `i^2+(r-i)^2` drops by `Theta(r^2)`.  The obstruction is
an unbalanced chain, especially `i=1`: it is a rank-preserving swap, and an
ambient singleton can carry `L` bits.  Repeating `Theta(L)` such steps can
lose `Theta(L^2)` bits, exactly the scale that matters.  The arbitrary
replacement-cone lemma shows this is not a bookkeeping artefact: one
tangent cell can contain an arbitrary smaller planar order type.

There is also an exact reset at the worst singleton split.  If `I={a}`, then

\[
 S=A+p=B+a
\]

has hull `B` and unique interior point `a`.  For fixed `(B,a)`, at most two
hull vertices `p` can repair `S` once `r>=4`: a nonconvex planar set of size
at least five has at most three repairs, and `a` is already its unique
interior repair.  Therefore the singleton exterior-incidence mass obeys

\[
 \boxed{
 E_r^{(1)}\le2\sum_{B\in\mathcal F_r(P)}
 |P\cap\operatorname{int}(\operatorname{conv}B)|.} \tag{31}
\]

Thus a singleton ear chain does not remain purely exterior: it resets, with
constant multiplicity, to the **interior-cage incidence problem** on the
target rank.  Gordon's cyclic stems describe each one-root cage exactly.
What is still absent is a multi-root bound on the right side of (31) for the
part of the rank carrying near-maximal entropy.  The Boolean hull partition
weights a cage by `2^i`; under the uniform face law that change of measure
can be exponentially large, so the one-root formula alone does not bound
(31).

Equations (29)--(31) isolate the recursive proof obligation more sharply:
balanced ears use the two-face entropy split, while singleton ears must be
amortized through a cyclic interior pocket before another `L`-bit point
identity is spent.

Thus the sharp recursive target is now:

> **Unbalanced pocket-chain theorem.**  Along a chain of singleton or
> `o(r)` ear replacements sharing a cyclic tangent pocket, either the
> same-rank target shadow expands by the product of the supplied exterior
> degrees, or the retained pocket contributes enough ordinary convex faces
> to pay the accumulated `O(L)` root losses, with total loss `n^o(1)`.

This is a genuine multi-root statement.  The existing common-apex and
common-ear examples kill an endpoint-only proof, but they do not kill the
theorem: their arbitrary pocket is precisely where the target face must
store the source bits.

## 6. Adversarial finite tests

The verifier checks (2) exactly at `p=1/3,1/2,2/3` on the exact `f(9)=169`
minimizer and on a 20-point exact integer macro.  It reconstructs every
convex face and closure, and checks (5) with exact rational arithmetic at
every integral cutoff.  There are 13 nonempty tail checks at `n=9` and 55
at `n=20`.

For the 20-point macro, the actual versus entropy-required omitted means
include

| rank | face count | actual `qbar` | required by (4) |
|---:|---:|---:|---:|
| 3 | 1,140 | 14.9500 | 10.0616 |
| 4 | 2,508 | 11.9856 | 8.4777 |
| 5 | 1,122 | 11.8654 | 5.1331 |

The exact inequality is comfortably valid but not vacuous.

The same census independently computes `u(A)` and `e(A)`.  Its largest
finite exterior-incidence ratio

\[
 {1\over V}\sum_{A\in N_r}e(A)
\]

is `4.74205...` (at rank four) on the 20-point macro and `1.59764...`
(at rank three) on the nine-point minimizer.  Thus these exact configurations
are consistent with `(EIC)` with a small constant; this is evidence only,
not a scalable theorem.

The saved hard profiles give the following modal-rank tests.  These use only
the rank counts, so the reported `q` is the universal minimum forced by
(4), not a reconstruction of the configuration's actual closures.

| `n` | modal `r` | `log V` | required `qbar` | `D_r` | ratio |
|---:|---:|---:|---:|---:|---:|
| 20 | 4 | 12.2213 | 8.3804 | 2 | 4.1902 |
| 24 | 4 | 13.4042 | 10.6544 | 2 | 5.3272 |
| 30 | 4 | 15.0004 | 14.0411 | 2 | 7.0205 |
| 58 | 5 | 20.0182 | 22.1545 | 2 | 11.0773 |

The 58-point record is not a minimizer; it is included only as an
adversarial planar profile.  Central Pascal cells are the known universal
QMS adversaries, but they lie in the high-mean branch.  At the last rank
below `ell` their tests are

| Pascal parameter | `n` | `r=ell-1` | `log v_r` | required `qbar/D_r` |
|---:|---:|---:|---:|---:|
| 16 | 12,870 | 13 | 115.436 | 1.123e3 |
| 32 | 601,080,390 | 29 | 540.723 | 2.188e6 |
| 64 | 1,832,624,140,942,590,534 | 60 | 2349.418 | 6.765e12 |

For `(EIC)` itself, exact rooted-circuit tables were recomputed with the
full nonconvex-quadruple condition (including exterior points that hide an
old vertex).  The maximum value of
`sum_(A in N_r)e(A)/V` on the small central Pascal cells is

| Pascal parameter | `n` | maximizing `r` | exact incidence ratio |
|---:|---:|---:|---:|
| 4 | 6 | -- | 0 |
| 5 | 10 | 3 | 0.558511 |
| 6 | 20 | 4 | 1.896640 |
| 7 | 35 | 5 | 3.953191 |

The ratio grows at these small sizes, so a universal constant `(EIC)` is
not suggested by this family.  A new exact strong-glue dynamic program now
pushes the actual up-degree census much farther.  A cap state records

```text
(rank, directional cap degree, ordinary up-degree),
```

with the reflected cup state and `(rank,ordinary up-degree)` for ordinary
faces.  These states close exactly under strong glue.  For the low-degree
census, directional degree can be truncated because it never decreases;
ordinary cap/cup degree needs only one overflow state because it may reset
when a point is taken from the other block.  This reduces the central
`m=40` calculation to a finite polynomial-size table.

For each last rank `r=ell-1`, let `N` be the exact number of faces with
`u<=4(r+1)` and let `U=sum_(A in N)u(A)`.  Put
`K=floor(N^(1/r))`.  The elementary optimized hull bound and the numerical
constant `mathrm e<3` give the
fully exact rational certificate

\[
 {1\over V}\sum_{A\in N}e(A)
 >{N r(K-3)-3U\over3V}.                            \tag{39}
\]

No floating entropy inversion is needed for (39).  The results are:

| Pascal `m` | `n` | `r` | `log(N/V)` | exact coarse `sum e/V` lower | optimized numerical lower |
|---:|---:|---:|---:|---:|---:|
| 12 | 924 | 9 | -5.525 | 5.0449 | 5.7508 |
| 16 | 12,870 | 13 | -6.624 | 19.613 | 21.778 |
| 20 | 184,756 | 17 | -7.650 | 68.409 | 75.586 |
| 24 | 2,704,156 | 21 | -8.530 | 250.25 | 276.25 |
| 28 | 40,116,600 | 25 | -9.372 | 913.16 | 1,007.84 |
| 32 | 601,080,390 | 29 | -10.155 | 3,411.34 | 3,764.92 |
| 36 | 9,075,135,300 | 33 | -10.862 | 13,262.82 | 14,637.38 |
| 40 | 137,846,528,820 | 37 | -11.518 | 52,950.80 | 58,438.54 |

This is a scalable finite obstruction to treating full `(EIC)` as a small
or constant-congestion theorem.  The observed exponent
`log(sum e/V)/log n` rises from `0.237` at `m=12` to `0.424` at `m=40` and
strongly suggests `n^(1/2-o(1))`.  The table alone does **not** prove an
asymptotic counterexample to an arbitrary `n^o(1)` allowance; that would
require an asymptotic analysis of the exact recurrence.  It does show why
the proof target should be capped Hall, and it is not evidence against a
low-mean or actual-minimizer-specific EIC theorem: central Pascal cells are
in the high-mean branch.

Thus neither central Pascal cells nor the saved `n=20,24,30,58` profiles
threaten the optimized inequality.  The tests also verify (15) exactly at
`L=64,128,256` and `r/L=1/4,1/2,3/4,1`.

### Audit correction: `q` is not the addable degree

This pass found an important regression in the earlier
`agent_generalized_deletion/low_addable_audit.py`.  Its rooted-circuit OR
marks precisely the points lying inside `conv(A)`.  The complement therefore
has size

\[
 n-|A|-i(A)=q(A)=u(A)+e(A),
\]

not `u(A)`.  An exterior point may hide an old vertex, so being outside
`conv(A)` does not make it addable.  The four-point exact regression

```text
A = {(-1,0),(0,1),(1,0)},  p=(0,3)
```

has `q(A)=1`, `u(A)=0`, and `e(A)=1`: adding `p` hides `(0,1)`.
Accordingly, the earlier low-addable censuses computed by that script are
actually low-`q` censuses.  For example, on the central Pascal `m=6`
configuration at rank three, that script reports 704, while direct exact
convexity gives all 1,140 faces as low-addable.  The profile-only upper
bounds and the 24-point rank-four record remain valid (the rank-four
threshold there is vacuous), but the reported exact `N_r` values at
nonvacuous ranks should not be used as RNP evidence until recomputed.

The new verifier computes `u` by testing `A+p` directly and records the
four-point regression in `optimized_hull_certificate.json`.

A second exact verifier recomputes the key records with the corrected full
nonconvex-quadruple mask:

| record | `n` | corrected RNP `K` | corrected `NPM/V` | max `sum e/V` |
|---|---:|---:|---:|---:|
| optimized RNP coordinates | 24 | 1.064785 | 0.934618 | 6.850755 |
| half-weight record | 58 | 0.807487 | 0.792657 | 14.814827 |
| central `T_(4,2)` vertical square | 36 | 0.470865 | 0.408990 | 3.467920 |
| guarded `k=3` vertical square | 49 | 0.062581 | 0.036488 | 0.563759 |

In particular, the earlier claim that the 58-point record has RNP ratio
`0.034237` is an artefact of counting low `q`; its actual low-addable RNP
ratio is `0.807487`.  It still does not threaten RNP, but it is no longer a
tiny-margin example.  The exterior-incidence ratio `14.8...` also rules out
treating a very small universal EIC constant as plausible.  The central and
guarded directional squares themselves give no scalable EIC counterexample:
one has a modest ratio `3.47...`, and the guarded near-half iterate
suppresses the rigorous profile upper bound below one and then rapidly
toward zero.  The central Pascal family, by contrast, is now the serious
full-EIC stress test quantified in (39).

## 7. DRC plus cyclic intervals: an exact capped concentration lemma

Full EIC is too rigid, but the capped source--blocker graph admits a useful
dependent-random-choice reduction.  Let `S` be a family of `M` sources and
select exactly `D` exterior blockers at every source.  For an integer
`1<=t<=D`, double counting pairs `(A,T)` with
`T subset N(A), |T|=t` gives a fixed `t`-set `T` of blockers with common
source family `X` satisfying

\[
 |X|\ge M{\binom Dt\over\binom nt}
     \ge M\left({D-t+1\over n}\right)^t.          \tag{40}
\]

This is the exact distinct-blocker form of DRC; no independence heuristic
is used.  At the critical capped scale `D=n/(2^r n^o(1))`, choose
`t=floor(sqrt(r))`.  Then

\[
 log|X|\ge\log M-r^{3/2}-o(r^{3/2}).              \tag{41}
\]

Thus a quadratic-entropy source family remains quadratic-entropy after the
blockers themselves have been fixed.

For every `A in X`, represent the fixed blockers by their violated cyclic
support intervals.  Put `R=floor(sqrt(t))`.  The exact cyclic interval
packing theorem gives either `R` disjoint intervals, or one support edge
contained in at least `t/R>=R` intervals.  Pigeonholing the outcome, the
chosen `R`-subset of `T`, and in the second case the support edge, costs at
most

\[
 1+\log\binom tR+2\log n=O(r).                    \tag{42}
\]

We obtain the following rigorous dichotomy on a family of size at least

\[
 {M\binom Dt/\binom nt\over2n^2\binom tR}:        \tag{43}
\]

* a fixed `R=r^(1/4+o(1))` batch has pairwise disjoint repair windows for
  every remaining source; or
* a fixed root edge is violated by the same fixed `R` blockers for every
  remaining source.

The entropy loss in (43) is `o(r^2)`.  This is the cleanest bridge found
between capped blocker incidence and the cyclic-stem/common-pocket
structure.  It does not itself close Hall.  In the disjoint case,
simultaneous repair can erase independent source coordinates and have
quadratic-entropy inverse fibres; the missing charge is a forward
two-ended cap--cup product.  In the rooted case, the common-pocket theorem
controls a literal common core, but iterating small batches without reusing
that capacity is still the crossing-pocket gate.

## 8. Verification

Run

```bash
python3 \
  phase2/loop/erdos838/agent_cyclic_stem_hw/verify_optimized_hull_activity.py
```

It writes `optimized_hull_certificate.json`.  Coordinates, convexity,
closures, activity sums, and all finite tail inequalities are checked with
integer or rational arithmetic.  Entropy inversions are numerical only
after the exact census has passed; large Pascal logarithms are evaluated
from leading integer bits to avoid floating overflow.

For the corrected actual-addability/RNP/EIC censuses, run

```bash
python3 \
  phase2/loop/erdos838/agent_cyclic_stem_hw/verify_corrected_addability.py
```

It writes `corrected_addability_certificate.json` and independently checks
the cover identity `sum_A u(A)=(r+1)v_(r+1)` at every audited rank.

The exact strong-glue up-degree recurrence is implemented in
`central_pascal_updegree_dp.py`.  The scalable bounded-state regression is

```bash
python3 \
  phase2/loop/erdos838/agent_cyclic_stem_hw/verify_pascal_eic_scaling.py \
  --verbose
```

It writes `pascal_eic_scaling_certificate.json`.  Every coarse lower bound
in (39) is a ratio of displayed integers.  The verifier also matches the
independent coordinate/circuit near-maximal counts for Pascal parameters
`4,5,6,7`; its optimized entropy columns are explicitly marked numerical.

## 9. Recommended next attack

1. Target **capped Hall** on the residual hard slice.  Use (40)--(43) to
   enter either a fixed disjoint-window batch or a fixed rooted pocket while
   retaining quadratic source entropy.
2. In the disjoint branch, charge to a forward two-ended cap--cup pool; a
   Boolean simultaneous-repair cube alone has exponentially large inverse
   fibres.  The missing statement is an amortized forward-alignment theorem
   across crossing pockets.
3. In the rooted/unbalanced branch, keep the full target pocket face.
   Endpoint states alone lose linear source entropy.  The pocket's own
   convex-face count must pay that entropy before the same tangent cell is
   reused too many times.
4. Retain EIC only as a low-mean/minimizer-specific possible shortcut.
   Central Pascal cells are high-mean, but their exact growth makes an
   unrestricted full-incidence theorem a poor primary gate.  A one-root
   Gordon expectation or positive mixture of hull activities cannot control
   the high-`q` residual by itself.
