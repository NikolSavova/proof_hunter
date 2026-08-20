# Adaptive mod-36 supports: global disjoint-translate saturation

## Status

The mod-36 refinement in
`ADAPTIVE_QUOTA_CROSS_RESIDUAL_MOD36_GATE.md` turns a selected occurrence
\(p\) into a normalized Gaussian support

\[
 \mathcal S(p)=\lambda_p+\mathcal D_L(r(p)),\qquad
 a(p)=c+36\lambda_p.                                  \tag{0.1}
\]

The previous barrier produced one top--tail pair with disjoint supports.
This note upgrades it to the full size-biased object.

**Theorem (global disjoint-translate saturation).**  For arbitrarily large
even \(R\), there is a polynomial-height integral distance-Sidon set, one
fixed metric wedge \(w\), and a collection of clean translations \(Q\) with

\[
 k=\Theta(R),\qquad 4k^2\le H_Q<4k^2+N,
 \qquad N={k\choose2},                                 \tag{0.2}
\]

having the following properties.

1. The selected isolated collection consists of exactly \(R\) occurrences
   \(p_0,\ldots,p_{R-1}\), all in one literal translation \(q\), one
   source-area residue modulo \(36\), and one scalar gap \(r\).
2. Their target load is

   \[
    U_N(r)=k,                                           \tag{0.3}
   \]

   with one completion in each occupied signed-area cell.
3. Their normalized supports are pairwise disjoint:

   \[
    \boxed{\mathcal S(p_i)\cap\mathcal S(p_j)=\varnothing
           \quad(i\ne j).}                             \tag{0.4}
   \]
4. The adaptive quota satisfies \(b_q\le R/2\).  Thus every possible
   tie-breaking into \(b_q\) top records and \(R-b_q\) tail records has
   zero top--tail support intersection, while

   \[
    \boxed{X_{36}=(R-b_q)k\ge {Rk\over2}>{H_Q\over200}}\tag{0.5}
   \]

   for all sufficiently large \(R\).
5. The centroid companion sets retain their strongest local endpoint form:
   all \(2R\) companion sets attached to the planted starts form a
   singleton sunflower with core equal to the tail anchor \(b\).  Hence a
   quota-cross pair has four genuine endpoint companion sets, and every
   relevant intersection is exactly the forced singleton.

This is not a counterexample to
\(X_{36}\le m^{o(1)}H_Q\); it saturates its \(H_Q\) scale.  It is a decisive
no-go for finishing that estimate through Gaussian-support intersections.
The entire sharp-scale adaptive mass can lie in pairwise disjoint translates,
even after retaining the same \(q\), the exact centroid companion sets, a
single metric gap, unit cell multiplicity, and an arbitrarily deep common
area sublattice.  A successful theorem must directly charge the disjoint
branch; collision energy can be identically zero on the planted mass.

## 1. The scaled target pencil

Let \(R\) be even, choose a prime \(P\) with \(R\le P\le2R\), and put

\[
 S=2R+1,qquad r=-100S^2.                              \tag{1.1}
\]

Take

\[
 H=8R+P+6                                               \tag{1.2}
\]

horizontal points \((SX_i,0)\), where the \(X_i\) form a polynomial-size
Golomb ruler translated far to the right, and the four vertical points

\[
 (0,0),\ (0,10S),\ (0,24S),\ (0,26S).                \tag{1.3}
\]

For every horizontal point there are two prescribed ordered edge pairs of
squared-distance gap \(r\):

\[
\begin{aligned}
 ((SX_i,0)(0,0),\ (SX_i,0)(0,10S)),\\
 ((SX_i,0)(0,24S),\ (SX_i,0)(0,26S)).                 \tag{1.4}
\end{aligned}
\]

Their normalized doubled areas \(D=d/2\) are, up to the harmless orientation
sign,

\[
 10S^2X_i\quad\hbox{and}\quad2S^2X_i.                 \tag{1.5}
\]

Choose the ruler scale and offset to make these \(2H\) values distinct and
larger than the final determinant cutoff.  The usual finite avoidance
excludes every unintended nonzero-area representation of the gap \(r\).
The collinear vertical subsystem has one additional scalar representation
of the same gap, but its determinant is zero and is therefore excluded.

After the source records and the \(P\)-point filler below are installed, the
final point count is

\[
 k=(H+4)+2+8R+P=16R+2P+12=2H.                         \tag{1.6}
\]

Consequently (1.4) gives exactly \(U_N(r)=2H=k\), every occupied area cell
has multiplicity one, and

\[
 \boxed{\mathcal D_N(r)\subset S^2\mathbf Z.}          \tag{1.7}
\]

The first two horizontal rows and the vertical points at heights zero and
ten give the fixed two-edge wedge \(w\); both of its partner shifts equal
\(r\), and the offset makes the cross determinant exceed \(N\).

## 2. Consecutive source-area translates

Choose distinct anchor points \(a,b\), put \(q=a-b\), and for
\(0\le t<R\) set

\[
 z_t=17+9t,
\quad
 u_t=(900S^2-z_t,z_t+1),
\quad
 u'_t=(900S^2-z_t-1,z_t).                              \tag{2.1}
\]

Realize \(u_t,u'_t\) as two source edges at independent generic centres.
For each source edge add a fresh target edge whose pair sum is its source
pair sum plus \(q\).  Thus each record consumes eight fresh points and both
starts lie in \(H_q\).  Direct calculation gives

\[
 |u_t|^2-|u'_t|^2=1800S^2=-18r                         \tag{2.2}
\]

and

\[
 a_t:=2\det(u_t,u'_t)
 =-1800S^2+70+36t.                                     \tag{2.3}
\]

All records therefore lie in the same mod-36 source-area class
\(c=34\).  If \(a_t=c+36\lambda_t\), then

\[
 \lambda_t=\lambda_0+t.                               \tag{2.4}
\]

Equations (1.7) and (2.4) prove the promised disjointness: every element of
\(\mathcal S(p_t)\) is congruent to \(\lambda_0+t\pmod{S^2}\), and

\[
 0<|t-t'|<R<S^2.                                       \tag{2.5}
\]

Hence the \(R\) normalized supports are pairwise disjoint.  Notice that
this is much stronger than defeating one bounded congruence refinement:
the target sublattice has index \(S^2\to\infty\).

The generic centres and target endpoints may simultaneously be chosen so
that

* the planted clean fibre is exactly the displayed \(2R\) starts;
* each \(p_t\) has \(q\) as its unique common clean translation;
* the only global edge-label pairs with gap \(-18r\) are the \(R\)
  displayed source pairs; and
* every displayed centroid class has exactly the two intended triples.

The last item makes the companion set of a start exactly

\[
 \{b,\text{the two endpoints of its target edge}\}.    \tag{2.6}
\]

All target endpoints are fresh, so these \(2R\) sets form a singleton
sunflower with core \(\{b\}\).  Thus the disjoint-support phenomenon is not
caused by dropping the centroid endpoint structure.

## 3. Funding the adaptive quota

Adjoin the standard \(P\)-point finite-field parabola filler

\[
 B_P=\{(x,x^2\bmod P):0\le x<P\}                      \tag{3.1}
\]

after the integral lexicographic map, a generic scale, and a generic
translation.  It has unique pair sums and can be made distance-Sidon.  Its
\(\Theta(P^3)\) triples occupy \(O(P^2)\) sum values, so Cauchy--Schwarz
gives \(\Omega(P^4)\) ordered clean-start mass.  Equal-sum distinct triples
are disjoint because pair sums are unique.

As in `LOW_BAND_ADAPTIVE_TWO_RESIDUAL_TENSOR_BARRIER.md`, choose the filler
scale, its relative translation, and all planted free endpoints by finite
avoidance.  Besides distance and pair-sum uniqueness, impose the exact
conditions at the end of Section 2, preserve all filler rows, and forbid
the filler and cross edges from realizing either selected scalar gap.
These are complements of polynomially many nonzero polynomials of degree at
most two.  The grid nonvanishing lemma gives an integral specialization in
a square of side \(R^{O(1)}\).

Begin with the planted translation \(q\), and add transported filler
translations until the actual total mass first reaches \(4k^2\).  This is
possible because \(P\asymp R\) and the available filler mass is
\(\Omega(P^4)\).  Since every fibre contains at most \(N\) distinct starts,

\[
 4k^2\le H_Q<4k^2+N.                                  \tag{3.2}
\]

The planted fibre has \(h_q=2R\), so

\[
 b_q=\left\lceil{k^2h_q\over H_Q}\right\rceil
 \le\left\lceil{R\over2}\right\rceil={R\over2}.      \tag{3.3}
\]

There are no selected occurrences in the filler fibres.  All \(R\)
planted loads are tied at \(k\) and lie in one residue class.  Whatever
tie-breaking is used, at least \(R/2\) occurrences survive, which proves

\[
 X_{36}\ge {Rk\over2}.                                 \tag{3.4}
\]

Since \(k\le20R+12\) and \(H_Q<(9/2)k^2\), (3.4) implies
\(X_{36}>H_Q/200\) for large \(R\).  On the other hand, every normalized
support in the top--tail cross product is disjoint from every other one.
Thus the sharp-scale mass in (3.4) produces no Gaussian collision at all.

## 4. Exact finite certificate

The verifier uses

\[
 R=4,\qquad P=47,\qquad S=11.                          \tag{4.1}
\]

It constructs a 170-point integral distance-Sidon set and checks the actual
filler fibres rather than a formal denominator.  The exact profile is

\[
\begin{array}{c|r}
 k&170\\
 N&14,365\\
 h_q&8\\
 U_N(-12,100)&170\\
 \text{filler translations available}&2,162\\
 \text{filler clean-start mass}&300,798\\
 \text{translations used in }Q_F&615\\
 H_Q&115,680\\
 b_q&2\\
 \text{tail records}&2\\
 X_{36}\text{ from the planted tail}&340
\end{array}                                             \tag{4.2}
\]

All 170 target area cells are distinct multiples of \(S^2\); the four
source shifts are consecutive; all six possible pairs of normalized
supports are disjoint.  The verifier also reconstructs every relevant
centroid class and confirms that all eight companion sets form the claimed
singleton sunflower.

Run

```bash
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_adaptive_mod36_global_disjoint_translate_saturation.py
```

## 5. Consequence for the live gate

The exact sufficient estimate

\[
 X_{36}\le m^{o(1)}H_Q                                \tag{5.1}
\]

remains live and is again sharp.  What is now closed is the whole family of
arguments that seeks to convert a positive fraction of quota-cross mass
into intersections of the shifted Gaussian supports.  Even a global
size-biased version sees zero intersections on a contribution
\(X_{36}\asymp H_Q\).

The remaining disjoint branch is not repaired by the ambient residual
range: the construction places \(\Theta(k^2)\) distinct occupied cells in a
polynomial-height square without difficulty.  A viable continuation must
charge disjoint cells using additional metric reuse across different gaps,
or prove that any excess \(X_{36}\gg m^{o(1)}H_Q\) forces structure absent
from this sharp family.  The common translation and the four centroid
companion sets alone do not do so.
