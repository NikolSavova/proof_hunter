# Full-gap attack on Erdős 1208

## Target and present outcome

The planar problem currently lies between

\[
  n^{1/3}\ll F_2(n)\ll n^{0.49815}.
\]

This note records an attempt to close that power gap.  It does **not** claim a
full solution.  Its useful output is a pair of rigorous method barriers and a
precise description of the new input that either endpoint appears to need.

## 1. A barrier for the prime-power split-prime construction

In the notation of `proof_prime_power.md`, the local parameters are

\[
 M=\prod_iq_i^{K_i},\qquad H=\prod_i(K_i+1),
 \qquad \Lambda=\prod_i(1+q_i^{-1}+\cdots+q_i^{-K_i}),
\]

where every usable rational prime satisfies $q_i\equiv1\pmod4$, hence
$q_i\ge5$, and every $K_i\ge1$.  Since $K+1\le2^K$,

\[
 \frac{\log H}{\log M}
 \le \frac{\log2}{\log5}.                           \tag{1.1}
\]

The optimized construction has

\[
 r=\log y,\qquad 4Dy^2+y=H/\Lambda,qquad
 \varepsilon=\frac{r}{4\log M+2r}.
\]

As $D\ge1$ and $\Lambda\ge1$, we have $y^2<H$, so (1.1) gives

\[
 x:=\frac r{\log M}
 <\frac{\log2}{2\log5}.
\]

Because $x\mapsto x/(4+2x)$ is increasing,

\[
 \varepsilon<
 \frac{\log2/(2\log5)}{4+\log2/\log5}
 =0.0486016697\ldots .                              \tag{1.2}
\]

Thus **no fixed choice of split primes and prime-power depths in the original
one-sieve dyadic optimization can produce an exponent below**

\[
 0.4513983302\ldots .                               \tag{1.3}
\]

In particular it cannot reach $n^{1/3}$.  Equality at the desired exponent
would require $r/\log M=1$, or heuristically $H\asymp M^2$, whereas these
binary isotropic valuation patterns satisfy $H\le M^{\log2/\log5}$.

This is a barrier for the present construction, not for all number-field or
all upper-bound constructions.

There is also a stronger, loss-free barrier for the whole binary local
norm-lattice version of the method.  Work over a discrete valuation ring of
odd residue size $q$ at a split place, and change variables so that the norm
form is $Q(s,t)=st$.  If a lattice $L$ has index $q^K$ and
$Q(L)\subseteq(q^K)$, let its first-coordinate projection be $q^aR$ and the
kernel of that projection be $0\times q^bR$.  Exactness gives $a+b=K$.
Choose $(q^a,u)\in L$.  Then $q^au\in q^KR$, so
$u\in q^{K-a}R=q^bR$.  Subtracting the kernel vector $(0,u)$ gives
$(q^a,0)\in L$, and hence

\[
 L=q^aR\times q^{K-a}R,qquad 0\le a\le K.          \tag{1.4}
\]

Thus the $K+1$ flags used in the prime-power lemma are all the available
maximal-index flags; there is no missing family of congruence patterns.  At
inert or ramified places this split family disappears (in particular, $2$ is
ramified for $x^2+y^2$), and composite moduli only multiply the local counts.

Write $h=\log H$ and $L=\log M$.  Even if root-discriminant and packing
losses are deleted and the degree is allowed to vary continuously, the two
competing terms have exponents $xL$ and $1/2-xh/2$.  Their optimum is

\[
 \frac1{2+h/L}\ge
 \frac1{2+\log2/\log5}
 =0.4114080899\ldots .                              \tag{1.5}
\]

So even an idealized binary norm-lattice sieve for $x^2+y^2$ cannot reach
$1/3$.  With one fixed modulus and dyadic field degrees, the worst phase
compares the increasing branch at $2x$ with the decreasing branch at $x$,
giving the stronger floor (1.3).  Section 7 of `proof_prime_power.md` evades
that particular dyadic loss by choosing among 17 moduli according to the
phase.  A stronger rank-17 tower and a 27-modulus portfolio then improve the
actual explicit exponent from $0.4991$ to $0.49815$.  Neither construction
evades the continuous floor (1.5).

A different positive-definite binary norm can make $2$ split.  Locally this
raises $h/L$ toward one, but the continuous barrier merely approaches
$1/3$, while dyadic degrees leave a floor of $0.4$.  It cannot improve the
current rank-16 tower certificate: forcing $2$ to split drops the generator
rank to 15, permitting at most 40 odd Frobenius cuts.  Even granting the 40
smallest certified primes, pretending they are all hyperbolic for one form,
and assigning the optimistically best geometric constant, full depth
optimization gives only $\varepsilon=0.000826134\ldots$, below the present
$0.000925411\ldots$.  Actual discriminant and splitting constraints can
only worsen this relaxation.

## 2. Why the current lower-bound machinery stops at $1/3$

The Clemen--Führer--Roche-Newton conflict hypergraph has a 4-edge for two
disjoint pairs at the same distance.  The Guth--Katz distance-energy input is

\[
 E(P)=O(n^3\log n),
\]

so its average 4-degree is $O(n^2\log n)$.  Both random alteration and the
rank-four term in the Li--Postle independence theorem naturally occur at

\[
 n\left(\frac{\log n}{n^2\log n}\right)^{1/3}
 \asymp n^{1/3}.                                    \tag{2.1}
\]

The richer codegree analysis removes the previous logarithmic loss, but it
does not alter the power in (2.1).  Therefore an argument that treats the
equal-distance quadruples only through total energy plus a general sparse
hypergraph theorem cannot improve the exponent.  A power improvement needs
additional geometric structure, most plausibly an inverse theorem for
point sets whose distance energy is close to cubic.

There is a useful conditional dichotomy.  If for some fixed \(\delta>0\),

\[
 E(P)\ll n^{3-\delta},                              \tag{2.2}
\]

then the same rank-four calculation has scale

\[
 n^{(1+\delta)/3}
\]

before the lower-rank constraints are checked.  The genuinely difficult
case is therefore the high-energy regime.  A complete lower-bound attack
would need to show that a high-energy planar set contains a comparably large
structured portion from which a distance-Sidon set larger than $n^{1/3}$
can be extracted.

A direct alteration calculation makes this precise without invoking the
full sparse-hypergraph theorem.  Let $T(P)$ be the family of unordered
3-subsets having two equal positive pairwise distances, and let $Q(P)$ be the
family of unordered 4-subsets admitting a partition into two equal-length
pairs.  A subset is distance-Sidon exactly when it contains no member of
$T(P)\cup Q(P)$.  Pach--Tardos prove

\[
 T(P)\le n^{\tau+o(1)},\qquad
 \tau=\frac{11e-3}{5e-1}=2.1364646171\ldots .       \tag{2.3}
\]

If $|Q(P)|\le Cn^{3-\delta}$, fix $\zeta>0$, put

\[
 \alpha=\min\left\{\frac{1+\delta}{3},
                    \frac{3-\tau}{2}\right\},
\]

retain every point independently with probability
$p=n^{\alpha-1-\zeta}$, and delete one point from every surviving bad triple
or quadruple.  Comparing

\[
 np,\qquad T(P)p^3,\qquad E_4(P)p^4
\]

and taking the $o(1)$ in (2.3) smaller than $2\zeta$ gives the rigorous
conditional bound

\[
 |S|\gg_{C,\delta,\zeta}n^{\alpha-\zeta}.           \tag{2.4}
\]

The second term is $0.4317676914\ldots$; it becomes the ceiling once
$\delta\ge0.2953030742\ldots$.  Thus every fixed power saving in all-distinct
four-point distance energy would improve $1/3$.  No known result supplies
that saving uniformly, and a square grid has total distance energy of order
$n^3\log n$ (up to the convention for degeneracies), so the high-energy
branch must explicitly accommodate lattice-like sets.

## 3. Stress tests on tempting shortcuts

* Few global distance values are insufficient.  Pigeonholing among $D(P)$
  distances only forces a repeated distance in a subset of size exceeding
  about $\sqrt{D(P)}$, and every planar $n$-point set has nearly linear
  $D(P)$ in the extremal regime.
* A robust upper theorem strong enough to force the $n^{1/3}$ endpoint
  would, when applied to the whole constructed set, force a single distance
  to occur on the order of $n^{4/3}$ times.  That saturates the classical
  planar unit-distance upper scale and is far beyond known constructions.
  A full upper solution need not be robust in this sense, but the observation
  rules out simply tuning the present robust theorem.
* The square grid already exhibits essentially the same obstruction: known
  lower constructions of distance-Sidon subsets are at the $n^{1/3}$
  scale, while known general upper bounds for grid subsets remain near
  $n^{1/2}$.  Closing the planar problem through grids alone would require a
  major advance on this arithmetic subproblem.  The exact energy/codegree
  calculation and its random-hypergraph comparison are recorded in
  `HIGH_ENERGY_GRID.md`.
* Purely combinatorial rainbow-clique theorems are sharp at the same scale.
  Alon--Jiang--Miller--Pritikin show that the threshold for a rainbow $K_t$
  in an $m$-locally bounded edge-colouring is
  $\Theta(mt^3/\log t)$.  Babai's construction, quoted in their proof, gives
  a proper colouring of $K_n$ whose largest rainbow clique has order only
  $O((n\log n)^{1/3})$.  Properness already eliminates every isosceles
  triple.  Consequently, any improvement based only on local colour
  multiplicity needs a specifically Euclidean input that arbitrary proper
  colourings lack.
* High distance energy is not additive energy.  Equality of norms of two
  displacement vectors is weaker than equality of the vectors, so the
  Balog--Szemerédi--Gowers theorem does not apply.  A regular polygon already
  has cubic distance energy but only essentially quadratic additive energy.
  Nor does cubic energy imply few distances: adjoining algebraically generic
  points to a regular polygon retains the cubic contribution while creating
  quadratically many new distance values.
* Tensoring the norm construction preserves squared distances only in an
  orthogonal direct sum, which moves from the plane to four dimensions.  A
  planar scale-separated encoding introduces cross terms.  Higher-degree
  norm forms similarly require more variables, while every planar rational
  Euclidean metric is binary.

## 4. Failed planar upper-design shortcuts

Several attempts to replace the binary congruence entropy by a genuinely
three-way planar collision mechanism also fail for structural reasons.

* A translation-invariant distance colouring on a finite group would make
  left translations act isometrically on the affine span.  A finite group
  with a transitive non-collinear planar orbit is cyclic or dihedral, reducing
  the construction to a regular-polygon orbit; its rainbow subsets have the
  ordinary square-root Sidon scale.
* On a concentric polar grid one has the exact swap collision
  $d((i,a),(j,b))=d((j,a),(i,b))$.  A distance-Sidon subset is therefore
  $C_4$-free in the radius-angle incidence graph.  The Kővári--Sós--Turán
  bound yields only $S\sqrt L+L$ points when the ambient grid has $SL=n$, at
  best an $n^{2/3}$ obstruction rather than the desired cube-root one.
* Exact three-factor coordinate swaps would supply cube-root entropy, but
  require three mutually orthogonal factor directions.  The plane supports
  only two.  Scale-separated encodings introduce cross terms and destroy the
  exact distance identities.
* Taking generic far-translates of Minkowski grids makes cross-distances
  essentially unique and adds their independent-set sizes; aligning the
  translates merely recreates a larger binary grid.

These failures point to a shared-vertex statistic: a useful upper
construction would need cubic isosceles or equal-distance supersaturation,
not just the pair multiplicity controlled by the present sieve.

## 5. Concrete remaining targets

Two sharply formulated advances would move the frontier.

1. **High-energy inverse/extraction lemma.**  Prove that whenever
   $|Q(P)|>n^{3-\delta}$, the set $P$ has a distance-Sidon subset of size
   $n^{1/3+c(\delta)}$.  Coupled with the low-energy hypergraph argument,
   this would improve the universal lower exponent.
2. **Non-binary local amplification.**  Replace the two isotropic factors of
   $u^2+v^2$ by a planar realizable mechanism whose number $H$ of useful
   collision patterns grows essentially like $M^2$, without an equally
   large divisor/packing loss.  The calculation above says exactly why the
   existing valuation-pattern mechanism cannot do this.

Neither target is supplied by the current literature or by this attack.
