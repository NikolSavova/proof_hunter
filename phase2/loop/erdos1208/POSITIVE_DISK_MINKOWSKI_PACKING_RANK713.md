# Positive-distance packing and disk averaging: a rank-713 improvement

## 1. Result

The Minkowski-grid sieve can use two pieces of geometry that were absent
from `proof_placewise_depths.md`:

1. every nonzero algebraic squared distance in a totally real field is
   positive in **every** real embedding, so ideal elements lie in a
   one-sided box rather than a symmetric box; and
2. the ambient lattice can be averaged over a product of planar disks,
   rather than a product of coordinate squares.

Together these replace the packing constant `4` in the prime-power master
inequality by

\[
 C=\frac4\pi.                                      \tag{1.1}
\]

Using exactly the existing rank-713 Frobenius-square tower and all-depth
frontier then gives the strict new bound

\[
 \boxed{F_2(n)\ll n^{0.49458516}}.                \tag{1.2}
\]

This improves `0.49458539` and crosses the requested `0.49458525`
threshold.  The finite certificate is
`verify_positive_disk_rank713.py`.

The same audit also gives the exact optimization for a variable-degree
totally real base.  A full rational-prime orbit of bounded residue degree
contributes one normalized local item, not one item per base-field degree.
Thus growing degree does not itself amplify local entropy.  No explicit
variable-degree tower found here beats (1.2); the improvement comes from
the sharper geometric constant.

## 2. One-sided ideal packing

Let `K` be totally real of degree `m`, with embeddings
`sigma_1,...,sigma_m`, and let `a` be a nonzero integral ideal.  Put

\[
 \delta=(N\mathfrak a)^{1/m}.
\]

### Lemma 2.1

For `Y>0`,

\[
 \left|\left\{\eta\in\mathfrak a:
 0<\sigma_j(\eta)\le Y\quad(1\le j\le m)
 \right\}\right|
 \le \left(1+\frac{Y}{\delta}\right)^m.           \tag{2.1}
\]

### Proof

Partition `(0,Y]^m` into half-open coordinate cubes of side `delta`.
If two embedded ideal elements lie in one cube, their nonzero difference
`gamma in a` satisfies

\[
 |N_{K/\mathbb Q}(\gamma)|<\delta^m=N\mathfrak a.
\]

But `(gamma) subset a`, so the positive integer
`|N(gamma)|=N((gamma))` is at least `N a`, a contradiction.  Thus each
small cube contains at most one point.  There are at most
`ceil(Y/delta)^m <= (1+Y/delta)^m` cubes.  QED.

The old symmetric estimate used a coordinate interval of length `2Y` and
gave `(1+2Y/delta)^m`.  Squared distances never require that loss: if

\[
 \eta=u^2+v^2\ne0,
\]

then total reality gives

\[
 \sigma_j(\eta)=\sigma_j(u)^2+\sigma_j(v)^2>0
 \quad\hbox{for every }j.                         \tag{2.2}
\]

## 3. Product-of-disks averaging

Write `Sigma(O_K^2)` for the Minkowski lattice in `R^(2m)`.  Its covolume
is `|Disc K|`.  For a parameter `R`, let `Delta_R` be the planar disk of
area `R^2`, hence radius `R/sqrt(pi)`, and consider

\[
 \mathcal C_R=\prod_{j=1}^m\Delta_R\subset\mathbb R^{2m}. \tag{3.1}
\]

The body has volume `R^(2m)`.  Averaging its translates over a fundamental
domain of the lattice gives a translate containing at least

\[
 \frac{R^{2m}}{|\operatorname{Disc}K|}             \tag{3.2}
\]

lattice points.  Projection to any one real embedding is injective on a
the lattice points in the translated body.  Moreover, if two projected
planar squared distances are equal at the distinguished embedding, then
the corresponding algebraic squared distances are equal in `K`, because
that real embedding is an injective field homomorphism.  Thus a
distance-Sidon subset after projection has the same multiplicity-two
property used by the algebraic divisor switch.

If two points lie in the same translate of `C_R`, then at every embedding
their planar separation is at most the disk diameter.  Therefore their
algebraic squared distance satisfies

\[
 0<\sigma_j(\eta)\le
 \left(\frac{2R}{\sqrt\pi}\right)^2
 =\frac4\pi R^2.                                  \tag{3.3}
\]

Suppose the tower has root discriminant at most `D`.  Taking

\[
 R=\sqrt D\,n^{1/(2m)}                             \tag{3.4}
\]

makes (3.2) at least `n`.  Hence an arbitrary `n` points may be retained.
This has exactly the same ambient-size normalization as the old product of
squares, but improves the maximum conjugate squared distance from `2R^2`
to `(4/pi)R^2`.

The planar isodiametric inequality shows that this is optimal among all
product-body replacements controlled only by the area and diameter of the
factor: every planar measurable set of area `R^2` has squared diameter at
least `4R^2/pi`.

## 4. Revised prime-power master inequality

Retain the notation of `proof_placewise_depths.md`.  Thus `M` is an ideal
modulus, `mathcal M=N(M)^(1/m)`, `H` is the number of valuation patterns,
and

\[
 \Lambda=\sum_{\mathfrak b\mid\mathfrak M}
          \frac1{N\mathfrak b}.                   \tag{4.1}
\]

For a switched divisor `b`, put

\[
 x=N(\mathfrak b)^{1/m}\le\mathcal M.
\]

Apply Lemma 2.1 to `a=M b` and use (3.3).  With `C=4/pi`,

\[
\begin{aligned}
 |\mathfrak M\mathfrak b\cap B_K^+(CR^2)|
 &\le\left(1+\frac{CR^2}{\mathcal Mx}\right)^m\\
 &=\left[\frac{R^2}{\mathcal Mx}
   \left(C+\frac{\mathcal Mx}{R^2}\right)\right]^m\\
 &\le\left[\frac{R^2}{\mathcal Mx}
   \left(C+\frac{\mathcal M^2}{R^2}\right)\right]^m.
                                                               \tag{4.2}
\end{aligned}
\]

The divisor switch and distance-Sidon multiplicity are unchanged.  Summing
(4.2) using (4.1), and comparing with the same-coset lower bound, gives

\[
 \boxed{
 |A|\le \mathcal M^m+\sqrt2R^m
 \left[(\Lambda/H)^{1/m}
 \left(C+\frac{\mathcal M^2}{R^2}\right)
 \right]^{m/2}.}                                  \tag{4.3}
\]

This is exactly equation (7) of `proof_placewise_depths.md` with `4`
replaced by `4/pi`.  No arithmetic input changes.

Put

\[
 w=\frac{\log n}{2m},\qquad
 L=\frac1m\log N\mathfrak M,\qquad
 G=\frac1m\log(H/\Lambda).
\]

At target exponent `alpha`, set `L=2 alpha w`.  If `F` denotes the
all-depth fractional frontier, (4.3) is at most `n^alpha` whenever

\[
 F(2\alpha w)\ge
 \log(CD)+(2-4\alpha)w+
 \log\!\left(1+
 \frac{e^{2(2\alpha-1)w}}{CD}\right).             \tag{4.4}
\]

The difference between the two sides remains concave in `w`, so the two
endpoints of a dyadic phase interval certify the whole interval.  The
placewise rounding lemma is unchanged.

## 5. Rank-713 finite certificate

Use the exact arithmetic presentation from
`proof_frobenius_all_depth_rank713.md`:

\[
 d=713,qquad r\le127092,qquad4r=713^2-1.         \tag{5.1}
\]

The ramification set is the first 714 odd rational primes, ending at
`5417`; the 126,379 useful Frobenius-square primes end at `1,685,119`.
The root-discriminant logarithm is

\[
 \log D=
 5304.6399570964594595269993248943299977668422347921\ldots . \tag{5.2}
\]

Take

\[
 \alpha=0.49458516,qquad w_0=1034254.             \tag{5.3}
\]

For a rationally checkable numerical upper bound on `C`, use Machin's
identity and four alternating-series terms:

\[
 \pi=16\arctan(1/5)-4\arctan(1/239)>\frac{333}{106}.
\]

Therefore

\[
 C=\frac4\pi<\frac{424}{333}=:C_* .               \tag{5.4}
\]

The right side of (4.4) is increasing in `C`, so the verifier uses the
larger rational constant `C_*`.  With 90-digit decimal arithmetic, after
subtracting `10^(-25)`, the two endpoint margins are

\[
 0.0158452806652\ldots,qquad
 0.0089012197582\ldots .                           \tag{5.5}
\]

The left boundary uses a fractional first-depth item after 79,943 full
items.  At the right boundary, 157,608 full items precede the fractional
item.  The active right slope is

\[
 0.0158108507322\ldots,
\]

whereas the maximum fourth-depth slope is

\[
 0.0129769833101\ldots .                           \tag{5.6}
\]

All omitted later depths are still below the active cutoff by the
all-depth monotonicity theorem.  Concavity proves (4.4) for every
`w in [w_0,2w_0]`; dyadic layers and placewise rounding then prove (1.2).

Run

```bash
python3 phase2/loop/erdos1208/verify_positive_disk_rank713.py
```

The verifier reconstructs the squareclass rank, all prime sets, relation
budget, globally sorted depth frontier, rational lower bound for `pi`, both
endpoint margins, and fourth-depth exclusion.  It prints

```text
target F_2(n) << n^0.49458516: CERTIFIED
```

## 6. Exact variable-degree arithmetic optimization

For completeness, let `E` be any totally real base of degree `s`.  Let its
tame totally-real pro-2 presentation have generator and relation ranks
`d_E,r_E`.  If a set `Q` of prime ideals receives Frobenius-square caps,
the exact ordinary Golod--Shafarevich budget is

\[
 |\mathcal Q|<\frac{d_E^2}{4}-r_E.                \tag{6.1}
\]

For a capped ideal `q` of norm `Q`, its depth-`k` marginal item is

\[
 c_{\mathfrak q,k}=\frac{log Q}{s},\qquad
 g_{\mathfrak q,k}=\frac1{2s}\log A_k(Q^{-2}).    \tag{6.2}
\]

The exact normalized frontier is the prefix-constrained knapsack

\[
 \begin{split}
 F_E(L)=\max\;&\frac1{2s}
  \sum_{\mathfrak q}\sum_{k\ge1}
  x_{\mathfrak q,k}\log A_k((N\mathfrak q)^{-2})\\
 \text{subject to }&\frac1s\sum_{\mathfrak q}\sum_{k\ge1}
  x_{\mathfrak q,k}\log N\mathfrak q\le L,\\
 &1\ge x_{\mathfrak q,1}\ge x_{\mathfrak q,2}\ge\cdots\ge0,\\
 &|\{\mathfrak q:x_{\mathfrak q,1}>0\}|
  \le\left\lfloor\frac{d_E^2-1}{4}\right\rfloor-r_E.
                                                               \tag{6.3}
 \end{split}
\]

Fractional `x` are realized across high-degree Galois layers, as in the
existing placewise rounding argument.  The disk master inequality is (4.4)
with

\[
 D_E=\operatorname{rd}(E)
 \prod_{\mathfrak p\in T}(N\mathfrak p)^{1/s}.     \tag{6.4}
\]

This formulation retains both relation cost and prime-ideal density.

There is an exact orbit cancellation.  Suppose a rational prime `q` has
residue degree `f` throughout a Galois base layer of degree `s`.  It has
`s/f` prime ideals, each of norm `q^f`.  Capping the full orbit gives total
normalized cost

\[
 \frac{s}{f}\frac{\log q^f}{s}=\log q             \tag{6.5}
\]

per depth, and guaranteed gain

\[
 \frac{s}{f}\frac1{2s}\log A_k(q^{-2f})
 =\frac1{2f}\log A_k(q^{-2f}).                    \tag{6.6}
\]

For `f=1`, this is exactly one rational-prime item; for `f>1`, it is weaker.
There is no factor `s`.  A growing-degree base can still help through a
genuinely unusual combination of bounded root discriminant, large
`d_E^2/4-r_E`, and exceptionally many cheap bounded-residue orbits, but
degree multiplication alone cannot do so.

Two useful necessary diagnostics follow immediately:

* if `d_E=o(s^(1/2))` and `r_E>=0`, (6.1) permits only `o(s)` capped ideals,
  so no positive normalized mass of a bounded-norm prime orbit can be used;
* a full bounded-residue rational orbit contributes (6.5)--(6.6), so even
  when `d_E` is linear in `s`, its local entropy is governed by the number
  and norms of rational orbits, not by the field degree.

No available explicit variable-degree family improves the rank-713 disk
certificate.  Establishing a universal dominance theorem for varying
fields would require uniform discriminant-versus-small-splitting or
2-class-rank input beyond the present argument.

## 7. Scope

The new mathematical input is elementary: one-sided ideal packing,
Minkowski averaging over a product of disks, and the planar isodiametric
constant.  The arithmetic presentation and local all-depth inequalities
are unchanged from the already audited rank-713 proof.

The constant `4/pi` is optimal for the product-body/diameter version of
this argument.  A further geometric improvement would have to retain more
than coordinatewise diameter and positivity, for example a genuinely
cross-embedding trace constraint.  No such stronger count is asserted
here.
