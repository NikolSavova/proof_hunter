# Adaptive tail: the two-residual tensor barrier and a sharp quota model

## 1. Outcome

Retain the notation of
`LOW_BAND_ISOLATED_ADAPTIVE_TRANSLATION_QUOTA_GATE.md`.  A decorated tail
record consists of an isolated clean occurrence

\[
 \omega=(p,q),\qquad p=(s,t),
\]

and an ordered determinant-qualified target pair `(v,v')` with

\[
 \delta(v)-\delta(v')=r(p),\qquad |a_v|>L,
 \qquad a_v=2\det(v,v').                              \tag{1.1}
\]

The affine-quadratic and Gaussian identities do hold simultaneously, but
for a fixed occurrence they are a **vertical tensor**, not two independent
constraints on the target completion.  More precisely, define

\[
 \begin{aligned}
 A_\omega
   &=g_q(p)+18r(p)+2q\cdot(\sigma_s-\sigma_t),\\
 G_{\omega,v,v'}&=a_s+18a_v,
 \qquad a_s=2\det(u_s,u_t).
 \end{aligned}                                         \tag{1.2}
\]

Then

\[
 A_\omega=2d_{p,q}\cdot\rho                           \tag{1.3}
\]

is constant through all `U_L(r(p))` decorations of `omega`, whereas

\[
 Z_s+18Z_v=-iG_{\omega,v,v'}                           \tag{1.4}
\]

simply indexes their signed target areas.  The Gaussian divisor theorem
therefore gives

\[
 \boxed{
  \max_{A,G}
  \#\{(v,v'):\Phi_\omega(v,v')=(A,G)\}
  \le m^{o(1)},\qquad
  |\Phi_\omega(D_{r(p),L})|
  \ge U_L(r(p))m^{-o(1)},}                             \tag{1.5}
\]

where `Phi_omega=(A_omega,G_omega)` and `D_(r,L)` is the target completion
set in (1.1).  Thus using both residuals cellwise produces many occupied
cells; it does not reduce the decoration mass.

This is a decisive barrier to the direct two-residual route, not a
counterexample to the desired estimate

\[
 X_{\rm ad}(w)\le m^{o(1)}H_Q.                         \tag{1.6}
\]

In fact there is a genuine polynomial-height distance-Sidon family for
which the adaptive quota leaves a tail and

\[
 \boxed{X_{\rm ad}(w)\ge cH_Q}                         \tag{1.7}
\]

for an absolute `c>0`, while each fixed occurrence occupies a linear
number of distinct joint residual cells.  Consequently (1.6), if true, is
sharp up to its subpolynomial factor.  No power saving below `H_Q` and no
argument that treats joint-cell support as a loss can close the gate.

The remaining live task is a **global packing theorem for the occupied
area cells across the size-biased tail**.  Neither residual supplies that
packing locally.

## 2. Exact vertical-tensor theorem

Canonically orient every edge vector.  For the selected clean source pair
put

\[
 Z_s=(u_s-u_t)\overline{(u_s+u_t)}
     =-18r(p)-ia_s.                                    \tag{2.1}
\]

For an external target completion put

\[
 Z_v=(v-v')\overline{(v+v')}
     =r(p)-ia_v.                                       \tag{2.2}
\]

Adding (2.1) to eighteen times (2.2) cancels the real part and proves
(1.4).  On the clean side, the common-translation row identity gives

\[
 2d_{p,q}\cdot\rho
 =g_q(p)-\bigl(\delta(s)-\delta(t)\bigr)
      +2q\cdot(\sigma_s-\sigma_t).                    \tag{2.3}
\]

The selector says `delta(s)-delta(t)=-18r(p)`, proving (1.3).
Crucially, the right side of (2.3) contains the external completion only
through its already fixed gap `r(p)`.  Hence its value is constant on the
whole target-completion fibre.

For integers `r,d`, let

\[
 n_r(d)=\#\{(v,v'):\delta(v)-\delta(v')=r,
                       2\det(v,v')=d\}.                \tag{2.4}
\]

The Gaussian factorization

\[
 (v-v')\overline{(v+v')}=r-id                         \tag{2.5}
\]

and uniqueness of directed edge vectors in a distance-Sidon set imply

\[
 n_r(d)\le \tau_{\mathbf Z[i]}(r-id)=m^{o(1)}          \tag{2.6}
\]

whenever `(r,d)!=(0,0)`.  In the determinant-qualified branch `d!=0`.
For fixed `omega`, the map

\[
 d\longmapsto (A_\omega,a_s+18d)                      \tag{2.7}
\]

is injective.  Therefore every joint cell has multiplicity `n_r(d)`, and
(1.5) follows by summing the cell multiplicities.

Notice what (1.5) does **not** say.  It gives no bound on the number of
signed areas occupied by one occurrence, and it gives no disjointness of
area supports between different occurrences or translations.  The
adaptive inequality `e_q>b_q` for a surviving translation changes neither
fact.

## 3. An asymptotic model surviving the adaptive quota

Let `p` be a sufficiently large prime and set `M=p`.  Start with the
planted isolated scalar pencil from
`LOW_BAND_ISOLATED_ADAPTIVE_TRANSLATION_QUOTA_GATE.md`, but reserve `p`
additional point slots.  It has

\[
 k=16M+2p+16=18p+16                                   \tag{3.1}
\]

points after the filler is installed.  Its special translation `q_0`
satisfies

\[
 h_{q_0}=2p,qquad e_{q_0}=p,                           \tag{3.2}
\]

and all selected occurrences have the same scalar shift `r`.  The
two-axis target subsystem contains `9p+8` horizontal points and hence

\[
 U_N(r)\ge2(9p+8)=k,qquad N={k\choose2}.               \tag{3.3}
\]

As filler take the finite-field parabola

\[
 B_p=\{(x,x^2\bmod p):0\le x<p\}                      \tag{3.4}
\]

followed by the standard integral lexicographic linear map which makes all
squared distances distinct.  It also has unique pair sums.  There are
`Theta(p^3)` unordered triples, and their integer sums occupy only
`O(p^2)` values.  Cauchy--Schwarz gives `Omega(p^4)` equal-sum pairs of
distinct triples.  Two distinct equal-sum triples are disjoint: if they
shared a point, deleting it would contradict pair-sum uniqueness.  Every
such collision contributes eighteen directed clean starts, so

\[
 \sum_q h_q(B_p)=\Omega(p^4).                           \tag{3.5}
\]

Scale and translate the filler, and specialize all free planted centres,
target endpoints, the scale, and the relative translation by finite
avoidance.  One may simultaneously require that

* the union is distance-Sidon and has unique pair sums;
* the displayed planted and filler clean rows remain present;
* `H_(q_0)` consists exactly of the `2p` planted starts;
* `q_0` is the unique common translation of every planted source pair; and
* no cross-component start is added to a filler translation, and the filler
  scale makes every internal filler distance gap different from the fixed
  selector; hence no filler translation contributes a selected occurrence.

These are the complements of polynomially many unintended linear or
quadratic equalities.  None is an identity: use the independent filler
scale for equalities whose relative translation cancels, and the relative
translation for cross-component equalities.  The product of the bad
polynomials is nonzero.  The grid nonvanishing lemma therefore supplies an
integer specialization of polynomial height.  This is the same
finite-avoidance argument already used for the planted pencil, now with
polynomially many additional constraints.

Choose filler translations greedily until their actual clean mass first
reaches `4k^2`, and call this set `Q_F`.  Since every clean fibre consists
of distinct pair sums,

\[
 h_q\le N.                                              \tag{3.6}
\]

Equation (3.5) ensures that the greedy selection is possible for large
`p`, and

\[
 4k^2\le H_{Q_F}<4k^2+N.                               \tag{3.7}
\]

Take `Q=Q_F union {q_0}`.  The adaptive quota at the planted translation is

\[
 b_{q_0}
 =\left\lceil{k^2(2p)\over H_Q}\right\rceil
 \le\lceil p/2\rceil.                                  \tag{3.8}
\]

At least `floor(p/2)` planted occurrences consequently remain, regardless
of how ties between their equal target loads are ordered.  By (3.3),

\[
 X_{\rm ad}(w)\ge k\lfloor p/2\rfloor.                 \tag{3.9}
\]

On the other hand, (3.6)--(3.7) give `H_Q<5k^2` for large `p`.  Since
`k=18p+16`, (3.9) proves (1.7), for example with any fixed
`c<1/180` once `p` is large enough.

The model has a deliberately important feature: the filler mass which
pays the adaptive quota need not share endpoints, translations, affine
residuals, or signed areas with the surviving planted records.  A proof of
(1.6) must therefore be global and size-biased; it cannot assume a local
geometric bridge from a tail record to the particular clean starts paying
its quota.

## 4. Exact finite certificate

The verifier takes `p=31` and three planted source pairs.  The union has
126 integral points and all 7,875 squared distances and pair sums are
distinct.  It uses all 930 transported filler translations together with
the planted translation.  Clean fibres are reconstructed independently.

\[
\begin{array}{c|r}
\text{quantity}&\text{exact value}\\ \hline
k&126\\
N&7,875\\
\sum_{q\in Q}h_q&58,116\\
h_{q_0},e_{q_0}&6,3\\
b_{q_0},e_{q_0}-b_{q_0}&2,1\\
U_N(-100)&126\\
X_{\rm ad}\text{ from the retained planted record}&126\\
\text{signed target areas}&126\\
\text{largest fixed-area cell}&1\\
\text{joint }(A,G)\text{ cells}&126\\
\text{largest joint cell}&1
\end{array}                                             \tag{4.1}
\]

For the retained occurrence the source doubled area is `-1674` and the
exact affine residual is

\[
 A=11289994816436323502108368.                          \tag{4.2}
\]

The verifier checks (1.3)--(1.4), unique common translation, clean
six-distinct endpoints, isolated target roles, the final determinant
cutoff, transported filler rows, the actual adaptive denominator, and the
full joint-cell histogram.  Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_low_band_adaptive_two_residual_tensor_barrier.py
```

## 5. Verdict

The direct proposal “use both residual identities simultaneously and then
apply a divisor or design bound” is exhausted.  At fixed occurrence the
affine coordinate is horizontal and constant; the Gaussian coordinate is
vertical and ranges over the target area support.  The adaptive quota does
not rotate or compress this tensor.

The live estimate (1.6) remains plausible and is now known to be sharp at
the `H_Q` scale.  A successful next lemma must control the **aggregate
number or reuse of occupied signed-area cells across adaptive-tail
occurrences**, while allowing the clean mass which funds the quota to be
geometrically unrelated filler.  Per-`q` one-free bounds, fixed joint-cell
multiplicity, affine row rank, and any power-saving target below `H_Q` are
all ruled out.
