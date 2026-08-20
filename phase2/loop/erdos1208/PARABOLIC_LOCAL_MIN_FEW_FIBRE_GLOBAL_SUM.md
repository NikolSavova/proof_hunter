# Parabolic local-min envelope: the few-fibre global sum

## Status

For a primitive direction $w$, let

\[
 a_r=|A_r|,
 \qquad A_r=\{x\in A:\det(w,x)=r\},
 \qquad R_w=|\{r:a_r>0\}|,
\]

and, for a transverse shift $c$, put

\[
 b_r^{(c)}=a_ra_{r+c}.                              \tag{0.1}
\]

The exact three-level endpoint-product bound from
`PARABOLIC_ENDPOINT_PRODUCT_SINGER_AMBIENT_SHARPNESS.md` leads to the
local-min envelope

\[
 \mathcal S_w=
 \sum_c\sum_{r_1<r_2<r_3}
 \min_{i<j} b_{r_i}^{(c)}b_{r_j}^{(c)}.              \tag{0.2}
\]

For $c=0$, clean nonzero correspondences are counted by
$b_r^{(0)}=a_r(a_r-1)$, rather than $a_r^2$.

This note proves two exact estimates.

**Fixed-direction convolution bound.**  For every finite $A$,

\[
 \boxed{\mathcal S_w\le |A|^4/6.}                   \tag{0.3}
\]

**Few-fibre global bound.**  If $A\subset[m]^2$ is distance-Sidon,
$k=|A|$, and $k\ge2R_0$, then

\[
 \boxed{
 \sum_{w:\,R_w\le R_0}\mathcal S_w
 \le {32\over3}R_0^2(m-1)^2H_{m-1}.}               \tag{0.4}
\]

Here $w$ runs over unoriented primitive integer directions and $H_n$
is the $n$-th harmonic number.  Consequently every collection of
directions on which $A$ occupies at most $m^{o(1)}$ parallel fibres
already has the required $m^{2+o(1)}$ aggregate bound.

This rigorously absorbs the Singer sharpness construction: its relevant
direction has only six ambient source fibres (and only three active fibres
for the chosen shift), while its contribution is $\Theta(m^2)$.

The remaining gate is now sharply localized.  One must control directions
with $R_w=m^{\Omega(1)}$, including graph-like directions for which every
fibre is a singleton.  The integer parabola shows that the latter cannot be
charged to the parallel-pair energy used in (0.4): one such direction has
zero parallel-pair energy but local-min envelope
$2\binom{k}{4}=\Theta(k^4)$.  At height $m=k^2$, this is again exactly
ambient scale.  Thus (0.4) is a genuine global branch, not a full solution
of the parabolic gate.

## 1. The local product envelope

For nonnegative $x,y,z$,

\[
 \min\{xy,yz,zx\}\le (xyz)^{2/3}.                  \tag{1.1}
\]

Indeed, after arranging $x\le y\le z$, the left side is $xy$, and
$xy\le z^2$.

It follows that, for any finite nonnegative sequence $b$,

\[
 \sum_{i<j<\ell}\min\{b_ib_j,b_jb_\ell,b_\ell b_i\}
 \le {1\over6}\left(\sum_i b_i^{2/3}\right)^3.     \tag{1.2}
\]

The factor $1/6$ is harmless but useful: expanding the cube on the right
counts every three-distinct-index monomial six times, in addition to
nonnegative repeated-index terms.

## 2. A sharp convolution estimate in one direction

Fix $w$ and set $f(r)=a_r^{2/3}$.  For $c\ne0$, (0.1) and (1.2)
give

\[
 \mathcal S_{w,c}
 \le {1\over6}\left(\sum_r f(r)f(r+c)\right)^3.    \tag{2.1}
\]

For $c=0$, clean correspondences satisfy
$a_r(a_r-1)\le a_r^2$, so (2.1) remains valid.  Hence

\[
 \mathcal S_w\le {1\over6}\|f*\widetilde f\|_3^3,
 \qquad \widetilde f(r)=f(-r).                       \tag{2.2}
\]

Discrete Young convolution gives

\[
 \|f*\widetilde f\|_3
 \le \|f\|_{3/2}\|\widetilde f\|_{3/2}
 =\left(\sum_r a_r\right)^{4/3}=k^{4/3}.            \tag{2.3}
\]

Equations (2.2)--(2.3) prove (0.3).  Notice that no metric hypothesis was
used here; this is an exact endpoint-product inequality.

## 3. The directional Golomb budget

Let

\[
 e_w=\sum_r\binom{a_r}{2}.                           \tag{3.1}
\]

This counts unordered pairs of points of $A$ parallel to $w$.  Write
$q=\|w\|_\infty$ and $M=m-1$.  Such a pair has difference
$tw$ for an integer $1\le t\le M/q$.  For a fixed $t$, two pairs
with difference $tw$ would have the same Euclidean distance.  Therefore
distance-Sidonicity gives the one-dimensional Golomb bound

\[
 e_w\le \left\lfloor{M\over q}\right\rfloor.        \tag{3.2}
\]

There are at most $4q$ unoriented primitive directions with
$\|w\|_\infty=q$.  Consequently

\[
 \sum_w e_w^2
 \le\sum_{q=1}^{M}4q\left({M\over q}\right)^2
 =4M^2H_M.                                           \tag{3.3}
\]

This is the ambient $m^2\log m$ reservoir that pays for Singer-type
few-fibre cells.

## 4. From few fibres to squared directional energy

Suppose $R_w\le R_0$ and $k\ge2R_0$.  Cauchy--Schwarz gives

\[
 2e_w+k=\sum_r a_r^2\ge {k^2\over R_w}\ge{k^2\over R_0}.
\]

More precisely, using $k\ge2R_w$,

\[
 e_w\ge {1\over2}\left({k^2\over R_w}-k\right)
 \ge {k^2\over4R_w}.                                \tag{4.1}
\]

Combining (0.3) and (4.1),

\[
 \mathcal S_w\le{k^4\over6}
 \le {8\over3}R_w^2e_w^2
 \le {8\over3}R_0^2e_w^2.                          \tag{4.2}
\]

Summing (4.2) and applying (3.3) proves (0.4).

The same proof is dyadic: directions with $R_w\asymp R$ contribute at
most $O(R^2m^2\log m)$.  This is useful only while $R=m^{o(1)}$, but in
that range it is already the full ambient-scale estimate.

## 5. Sharpness and the graph-like residual

### 5.1 Singer cells

In the lifted Singer construction, $A$ lies on six horizontal rows.
For the horizontal direction $w$, $R_w=6$, while
$e_w=\Theta(k^2)$.  The selected three-level endpoint-product cell has
local-min envelope $\Theta(k^4)=\Theta(m^2)$.  Thus its order is exactly
$e_w^2$, and (3.3) supplies precisely the correct global reservoir.

### 5.2 A rigorous obstruction to an $e_w^2$-only theorem

Let

\[
 A_k=\{(i,i^2):1\le i\le k\}\subset[k^2]^2.         \tag{5.1}
\]

This is distance-Sidon.  Indeed, the squared distance associated with
$i<j$ is

\[
 h^2(1+s^2),\qquad h=j-i,\quad s=i+j.                \tag{5.2}
\]

If two such values with $h=ga<h'=gb$, $(a,b)=1$, were equal, then

\[
 (as-bs')(as+bs')=b^2-a^2.                           \tag{5.3}
\]

The first factor must be positive.  But $s\ge ga+2$ and
$s'\ge gb+2$, so the second factor is strictly larger than
$b^2-a^2$, contradicting (5.3).  Hence $h=h'$, and then $s=s'$,
which identifies the pair.

Take $w=(0,1)$.  The fibres are the $k$ singleton vertical levels
$r=-i$, so $e_w=0$ and $R_w=k$.  For each nonzero shift $c$ with
$|c|<k$, exactly $k-|c|$ values of $b_r^{(c)}$ are equal to one.
Therefore

\[
 \mathcal S_w
 =2\sum_{j=3}^{k-1}\binom j3
 =2\binom k4.                                        \tag{5.4}
\]

Thus no estimate $\mathcal S_w\ll e_w^2m^{o(1)}$ can hold, even for
genuine distance-Sidon sets.  Formula (5.4) also shows that (0.3) has the
correct $k^4$ order.

## 6. Exact remaining gate

The parabolic local-min summation problem has split into two regimes.

1. **Few-fibre / row-heavy directions:** $R_w=m^{o(1)}$.  These are
   closed by (0.4), including the ambient-sharp Singer family.
2. **Many-fibre / graph-like directions:** $R_w=m^{\Omega(1)}$.  Here
   $e_w$ can vanish and the convolution energy in (2.2) can be
   $\Theta(k^4)$ for one direction.  A finish must charge the projection
   difference correlations themselves to the ambient lattice range,
   rather than to parallel pairs inside fibres.

The natural next quantity is the cubic projection-correlation energy

\[
 \sum_{w:\,R_w\text{ large}}\sum_c
 \left(\sum_r a_r^{2/3}a_{r+c}^{2/3}\right)^3.       \tag{6.1}
\]

One needs an $m^{o(1)}(k^3+m^2)$ bound for the endpoint-realized portion
of (6.1), or a further decomposition that uses the longitudinal
coordinates discarded by (6.1).  The few-fibre theorem shows that no
Singer-type bounded-row obstruction remains in this residual.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_parabolic_local_min_few_fibre_global_sum.py
```

The verifier exhausts small occupancy arrays for the exact inequality
$6\mathcal S_w\le k^4$, checks the parabola identity (5.4) and its
distance-Sidon property, verifies (3.2) on several genuine examples, and
prints the Singer/few-fibre scaling audit.
