# Adaptive quota-cross residuals: a mod-36 refinement and a disjoint-support barrier

## Status

This note retains the exact top-versus-tail pairing from
`ADAPTIVE_CENTROID_SINGLETON_CROSS_PAIR_GATE.md` and the Gaussian signed-area
support of every occurrence.  It gives one positive reduction and one
genuine geometric no-go.

**Positive reduction.**  Every source doubled area and every target doubled
area is even.  Hence the Gaussian residual

\[
 G(p;v,v')=a(p)+18d(v,v')                               \tag{0.1}
\]

satisfies

\[
 \boxed{G(p;v,v')\equiv a(p)\pmod {36}.}                \tag{0.2}
\]

One may therefore partition the isolated occurrences in each translation
by \(a(p)\bmod36\), discard the largest \(b_q\) loads in **each** residue
class, and pay fewer than \(36k^2\) occurrences in total.  Every retained
occurrence then has \(b_q\) top witnesses in the same translation and the
same residual congruence class.  The adaptive implication becomes

\[
 \boxed{
 I^Q(w)<36k^2+{X_{36}(w)\over T}.}                      \tag{0.3}
\]

Thus proving \(X_{36}\le m^{o(1)}H_Q\) is sufficient for the local gate.
This removes the elementary congruence obstruction from every top--tail
comparison at only a constant cost.

**Exact collision gate.**  After dividing out the common modulus, an
occurrence has a normalized residual support \(\mathcal S(p)\subset\mathbb
Z\) of size at least \(U_L(r(p))m^{-o(1)}\).  An intersection
\(\mathcal S(p)\cap\mathcal S(p')\) is exactly a full complex Gaussian
collision between the two decorated occurrences, not merely equality of
their scalar gaps.

**No-go.**  Congruence compatibility does not force such an intersection.
There are polynomial-height integral distance-Sidon sets with two isolated
occurrences sharing the same literal \(q\), the same scalar gap, target load
at least \(k\), and the same source area modulo \(36\), but with disjoint
normalized residual supports.  The finite certificate has

\[
 k=176,\quad h_q=20,\quad U_N(-100)=176,                \tag{0.4}
\]

and two source areas \(-1730,-1478\), whose difference is \(252=7\cdot36\).
All target doubled areas are divisible by four, so the two normalized
supports have opposite parity.

The asymptotic planted-pencil plus full parabola filler makes the same two
records an actual top--tail pair after the residue-refined quota.  It does
not violate \(X_{36}\le m^{o(1)}H_Q\): the filler mass is much larger than
the planted lift.  It decisively rules out the proposed local finish
"same residue plus common \(q\) forces an equal Gaussian residual."  The
remaining theorem must charge disjoint shifted area supports globally, or
use the centroid/affine endpoint coordinates in addition to them.

## 1. Residue-refined adaptive deletion

For an isolated occurrence \(\omega=(p,q)\), with canonically oriented
source edge vectors \(u_s,u_t\), put

\[
 a(p)=2\det(u_s,u_t).                                    \tag{1.1}
\]

For each even residue \(c\pmod {36}\), let

\[
 \Omega_{q,c}=\{p\in\Omega_q:a(p)\equiv c\pmod {36}\}. \tag{1.2}
\]

There are only eighteen possible residues.  In every \(\Omega_{q,c}\),
order occurrences by decreasing target load and discard its first \(b_q\),
where

\[
 b_q=\left\lceil {k^2h_q\over H_Q}\right\rceil.        \tag{1.3}
\]

Call the remaining collection \(\Omega^{\rm tail,36}_q\), and define

\[
 X_{36}=\sum_q\sum_{p\in\Omega^{\rm tail,36}_q}U_L(r(p)). \tag{1.4}
\]

The previous quota calculation gives

\[
 \sum_qb_q<2k^2.                                        \tag{1.5}
\]

At most \(18b_q\) occurrences are removed from one translation, whence

\[
 \sum_q|\Omega_q\setminus\Omega^{\rm tail,36}_q|
 <36k^2.                                                 \tag{1.6}
\]

Every retained occurrence is target-rich, so (1.6) proves (0.3).

The exact quota-cross identity survives inside every residue.  If
\(U_{q,c,1}\ge\cdots\ge U_{q,c,e}\), then

\[
 \boxed{
 \sum_{j>b_q}U_{q,c,j}
 ={1\over b_q}
  \sum_{\substack{i\le b_q\\j>b_q}}
     \min(U_{q,c,i},U_{q,c,j}).}                         \tag{1.7}
\]

Thus each tail record may be compared only with top records whose Gaussian
residuals are arithmetically capable of agreeing.

## 2. Normalized signed-area supports

For an external determinant-qualified ordered edge pair, write

\[
 d(v,v')=2\det(v,v')=2D(v,v'),\qquad D(v,v')\in\mathbb Z. \tag{2.1}
\]

If \(p\in\Omega_{q,c}\), write

\[
 a(p)=c+36\lambda_p.                                    \tag{2.2}
\]

For its scalar gap \(r=r(p)\), define

\[
 \begin{aligned}
 n_r(2D)&=\#\{(v,v'):\delta(v)-\delta(v')=r,
                         d(v,v')=2D,\ |2D|>L\},\\
 \mathcal D_L(r)&=\{D:n_r(2D)>0\},\\
 \boxed{\mathcal S(p)&=\lambda_p+\mathcal D_L(r).}
                                                               \tag{2.3}
 \end{aligned}
\]

Gaussian factorization gives

\[
 n_r(2D)\le G(m)=m^{o(1)},                              \tag{2.4}
\]

and therefore

\[
 \boxed{|\mathcal S(p)|\ge U_L(r(p))/G(m).}             \tag{2.5}
\]

Let

\[
 Z_p=(u_s-u_t)\overline{(u_s+u_t)}=-18r(p)-ia(p),       \tag{2.6}
\]

and for an external completion let

\[
 Z_v=(v-v')\overline{(v+v')}=r(p)-i2D.                 \tag{2.7}
\]

Then

\[
 Z_p+18Z_v=-i(c+36(\lambda_p+D)).                       \tag{2.8}
\]

Consequently, for two occurrences \(p,p'\) in the same residue class,

\[
 x\in\mathcal S(p)\cap\mathcal S(p')                  \tag{2.9}
\]

if and only if there are determinant-qualified completions satisfying the
full complex equality

\[
 \boxed{
 Z_p+18Z_v=Z_{p'}+18Z_{v'}=-i(c+36x).}                  \tag{2.10}
\]

For fixed \(p,x\), the number of completions in (2.10) is at most
\(G(m)\), since \(D=x-\lambda_p\) is fixed.  For fixed \(p,p',x\), the
number of paired completions is at most \(G(m)^2\).

Equation (2.10) is the strongest collision produced by the quota-cross
Gaussian route.  It retains the two scalar gaps and two signed target areas;
the common translation and centroid singleton structure remain available on
the clean side.

## 3. Same residue does not force support intersection

Use the planted isolated scalar pencil with ten source records.  Its special
translation \(q\) has

\[
 h_q=20                                                   \tag{3.1}
\]

and is the unique common clean translation of every planted source pair.
The two source vectors in record \(j\) are

\[
 u_j=(900-z_j,z_j+1),\qquad
 u'_j=(899-z_j,z_j),\qquad z_j=17+7j.                   \tag{3.2}
\]

They obey

\[
 |u_j|^2-|u'_j|^2=1800=-18(-100),                       \tag{3.3}
\]

while their source doubled area is

\[
 a_j=2\det(u_j,u'_j)=-1730+28j.                         \tag{3.4}
\]

In particular

\[
 a_9-a_0=252=7\cdot36,qquad a_0\equiv a_9\equiv34
 \pmod {36}.                                            \tag{3.5}
\]

The perpendicular target subsystem uses the six vertical marks

\[
 \{0,10,24,26,35,55\}.                                  \tag{3.6}
\]

For every horizontal point it supplies the two gap-\(-100\) records

\[
 (H_iO,H_iY_{10}),\qquad(H_iY_{24},H_iY_{26}).          \tag{3.7}
\]

Their doubled areas are multiples of \(20\) and \(4\), respectively.
Finite avoidance excludes every unintended determinant-qualified record at
that fixed gap.  Hence every normalized target area \(D=d/2\) is even.

The normalized source shifts of records zero and nine differ by

\[
 \lambda_9-\lambda_0={a_9-a_0\over36}=7.               \tag{3.8}
\]

It follows immediately that

\[
 \boxed{\mathcal S(p_0)\cap\mathcal S(p_9)=\varnothing:} \tag{3.9}
\]

one support consists of one parity of integers and the other support of the
opposite parity.

All prescribed point relations are affine identities.  Every unwanted
point, pair-sum, triple-sum, distance, or fixed-gap identity is a nonzero
polynomial of degree at most two in the free centres and endpoints.  The
grid nonvanishing lemma therefore gives integral distance-Sidon
specializations at polynomial height for all record counts.

To make (3.9) occur inside the actual residue-refined tail, adjoin the full
finite-field parabola filler as in
`LOW_BAND_ADAPTIVE_TWO_RESIDUAL_TENSOR_BARRIER.md`, reserve enough
horizontal points that \(U_N(-100)\ge k\) after the union, and take all
filler translations in \(Q\).  Their clean mass is \(\Omega(P^4)\), while
the final point count is \(O(P)\).  For a planted record count comparable to
\(P\), (1.3) is therefore \(b_q=1\) for large \(P\).  Records \(p_0,p_9\)
lie in the same residue class; ties may be ordered with \(p_0\) on top and
\(p_9\) in the tail.  The filler scale and relative translation exclude all
unintended selected records without changing (3.9).

This family has \(H_Q=\Omega(P^4)\) and only \(O(P^2)\) planted decorated
mass, so it respects the desired adaptive estimate by a wide margin.  Its
purpose is exact: even a genuine top--tail pair with every presently
retained local condition can have no equal Gaussian residual.

## 4. Consequence

The mod-36 deletion is a valid strengthening of the adaptive reduction and
should be retained.  It removes an avoidable congruence mismatch and turns
support intersections into the exact collision equation (2.10).

But intersection cannot be the solution gate.  The perpendicular-pencil
family realizes the complementary branch

\[
 \mathcal S(p_{\rm top})\cap\mathcal S(p_{\rm tail})
 =\varnothing                                             \tag{4.1}
\]

at polynomial height, even for the same \(q\), same \(r\), same residual
class, and target load \(k\).  Requiring one more fixed congruence does not
repair this: scaling the perpendicular subsystem produces arbitrarily deep
fixed divisibility.

A viable continuation must therefore sum the **incidence mass** of the
shifted supports, allowing both intersections and disjoint translates.  It
must couple that mass to the four centroid companion sets of a quota-cross
pair, or aggregate reuse across many comparable fibres.  A theorem based
only on forced support overlap, even after bounded congruence refinement,
is closed.

## 5. Verification

Run

```bash
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_adaptive_quota_cross_residual_mod36_gate.py
```

The verifier:

* exhausts the residue-refined quota and exact top--tail minimum identity on
  small profiles and checks two thousand larger deterministic random
  profiles;
* builds a 176-point integral distance-Sidon set with all 15,400 distances
  and pair sums distinct;
* checks the exact 20-start planted fibre and unique common translation for
  records zero and nine;
* enumerates all determinant-qualified gap-\(-100\) records, finding exactly
  176 distinct area cells, all divisible by four; and
* verifies the source area congruence and the empty intersection (3.9).
