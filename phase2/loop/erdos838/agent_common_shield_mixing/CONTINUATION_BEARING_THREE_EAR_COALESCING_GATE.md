# Continuation-bearing three-ear coalescing gate

**Date:** 2026-08-15. All record masses are nonnegative, and all
logarithms are base two.

## Verdict

There is an exact conditional coalescing lemma, but the live unordered
release and chronology theorems do not supply its hypothesis.

If \(W_h\) is the mass of ear records carrying literal continuation \(h\),
define the order-three effective continuation count

\[
 K_3=\left({W^3\over\sum_hW_h^3}\right)^{1/2},
 \qquad W=\sum_hW_h.                                      \tag{1}
\]

When every continuation fibre is in the low-repair-depth branch, the mass
of bad triples whose three records carry the **same** \(h\) is at least

\[
                  {(1-\eta)^3W^3\over K_3^2}.            \tag{2}
\]

Thus \(K_3\le2^{O(L\log L)}\) is exactly sufficient for a
continuation-bearing Farkas cage with only \(2^{O(L\log L)}\) aggregate
loss. Retaining the literal \(h\) in the output makes summation over
different fibres free; fixing a canonical physical edge triple costs only
an additional polynomial factor.

However, neither WEIGHTED_POSITION_RELEASE_ENTROPY nor
UNORDERED_COLOUR_LIVE_RELEASE_REFINEMENT bounds \(K_3\). Their one-face
decoder deliberately retains the full pocket/source continuation, which
may have quadratic-exponential alphabet size. The fixed-label chronology
recovers different continuation words exactly; it does not identify them.

The tempting exact nine-point lift through common macro role \(1\) also
does not produce a rich continuation-bearing cage. Role \(1\) is a common
first endpoint, so the same child cap face \(H\) lifts all three sources.
But for \(|H|\ge2\), a consecutive edge of \(H\) is a literal exposed edge
of all three lifted sources. A point infinitesimally across that edge
repairs all three at once. Therefore the rich cap alphabet belongs to the
simultaneous-repair/profile branch, not the bad Farkas branch. Only
singleton \(H\)'s preserve the cage, and their alphabet has merely
polynomial entropy.

Finally, an exact ten-point ear configuration shows that continuation
correlation cannot be inferred from planar ear geometry alone: three
actual continuation singletons are each compatible with exactly one ear
context, the selected ear triple is bad, and no bad triple has a common
continuation. This is a local correlation barrier, not a globally live
fixed-gap construction.

## 1. Exact weighted coalescing lemma

Let \(\Omega\) be a finite weighted family of records. Each
\(\omega\in\Omega\) carries

* one open convex ear chamber \(C_\omega\subset\mathbb R^2\);
* one literal, recoverable continuation \(h(\omega)\); and
* weight \(w_\omega\ge0\).

For a continuation \(h\), put

\[
 W_h=\sum_{\omega:h(\omega)=h}w_\omega,\qquad
 \rho_h={1\over W_h}\sup_x
       \sum_{\substack{\omega:h(\omega)=h\\x\in C_\omega}}w_\omega.
                                                                  \tag{3}
\]

> **Theorem 1 (Rényi-3 continuation coalescing).** If
> \(\rho_h\le\eta\) for every nonempty continuation fibre, then the ordered
> product-weight of triples
> \((\omega_1,\omega_2,\omega_3)\) satisfying
> \[
> h(\omega_1)=h(\omega_2)=h(\omega_3),\qquad
> C_{\omega_1}\cap C_{\omega_2}\cap C_{\omega_3}=\varnothing
>                                                                  \tag{4}
> \]
> is at least the quantity in (2).

**Proof.** Weighted planar fractional Helly, applied inside one \(h\)-fibre,
says that the intersecting-triple weight is at most

\[
                 \bigl(1-(1-\rho_h)^3\bigr)W_h^3.
\]

Hence its bad-triple weight is at least
\((1-\rho_h)^3W_h^3\ge(1-\eta)^3W_h^3\). Sum over \(h\) and use
\(\sum_hW_h^3=W^3/K_3^2\). \(\square\)

The theorem is decoder-exact. If a later geometric output retains \(h\),
outputs from different \(h\)-fibres cannot collide merely because the
physical ear geometry agrees. If a strict-Farkas certificate is chosen
canonically, its ordered edge-and-side triple has at most

\[
                         \left(2\binom n2\right)^3<n^6           \tag{5}
\]

values. Fixing it is only an \(O(L)\)-bit loss. Thus the total coalescing
loss is \(K_3^2n^6\), which is \(2^{O(L\log L)}\) under the stated bound
on \(K_3\).

The high-\(\rho_h\) alternative is fibrewise only. It supplies a repair
point depending on \(h\). One physical repair label cannot occupy many
such positions simultaneously. Therefore a valid global use must either
fix a heavy \(h\)-fibre, synchronize the repair positions, or route the
different \(h\)'s to disjoint ordinary outputs. The one-bit relocation
theorem does not make this synchronization automatic.

## 2. Why the live release data do not bound \(K_3\)

In the adaptive release theorem, an output \(U\) reveals the full pocket
face \(F\), the undeleted source labels, and the empty-role mask. The
deleted completion word reconstructs the full source. This is why the
entropy decoder has low load even when the continuation alphabet itself
has size \(2^{\Theta(L^2)}\).

Consequently:

1. unordered colouring costs only \(2^{O(L)}\), but it creates no equality
   relation between continuations on three different ear records;
2. fixing the cyclic role permutation later costs at most
   \(2^{O(L\log L)}\), but still does not reduce \(K_3\);
3. fixed-label chronology reattaches each branch's literal deleted labels,
   so different continuation words remain different by design; and
4. the effective role forest controls conditional next-label min-entropy,
   not the third collision moment \(\sum_hW_h^3\).

Thus a continuation alphabet uniformly spread over
\(2^{\Theta(L^2)}\) literal faces has \(K_3=2^{\Theta(L^2)}\), and (2)
loses the full quadratic coefficient. This is not a decoder defect:
retaining \(F\) or the source word is precisely what made the earlier
one-face decoder exact.

## 3. Audit of the common-role nine-point lift

Use the exact nine-point coordinates

\[
\begin{array}{c|rrrrrrrrr}
i&0&1&2&3&4&5&6&7&8\\ \hline
x_i&62614&2922&10209&20660&33336&30137&15334&14934&10934\\
y_i&7322&4014&14386&24299&29017&33324&45211&55621&61521.
\end{array}                                                     \tag{6}
\]

For the generic projection

\[
                         \pi(x,y)=x+{49495\over57507}y,           \tag{7}
\]

the physical order is

\[
                         [1,2,3,6,4,5,7,8,0].                    \tag{8}
\]

In particular role \(1\) is first in all three source triangles

\[
 [1,6,0],\qquad[1,7,0],\qquad[1,3,8].                            \tag{9}
\]

Heterogeneous vertical composition therefore does allow one common child
cap \(H\) in role \(1\), with singleton choices in the other macro roles.
Strict margins keep the hidden label in role \(2\) blocked.

This does **not** preserve the triple-ear obstruction for rich \(H\).
Every consecutive edge of a rank-at-least-two cap \(H\) lies on the same
exposed child boundary arc of each lifted source. Applying the literal
fixed-carrier theorem to any such edge gives a common open repair cell.

There is already an exact rank-two witness. Replace macro point \(p_1\) by

\[
                  h_-=(2922,4013),\qquad h_+=(2922,4015),        \tag{10}
\]

and retain the two other macro vertices from each triangle in (9). All
three resulting four-point sources are ordinary, and \(p_2\) remains
strictly hidden in each. Nevertheless

\[
                         q=\left(2922-{1\over10},4014\right)     \tag{11}
\]

is inserted through the common edge \(h_-h_+\), and adjoining \(q\) makes
all three sources ordinary simultaneously.

Therefore a lifted count of the form

\[
                    C_{\rm child}\,N^{O(1)}                       \tag{12}
\]

counts valid source continuations, but its rank-at-least-two terms do not
count bad continuation-bearing Farkas cages. They have already entered the
simultaneous-repair/common-profile branch. The only terms which can retain
the original cage by this common-role mechanism are singleton child faces,
of which there are only \(N\). Even after all other singleton transversal
choices, this contributes only \(N^{O(1)}=2^{O(L)}\), not a quadratic
logarithmic coefficient.

The cap alphabet may still be useful as an endpoint bank. In a balanced
low-surplus state it has roughly a quarter coefficient rather than a half
coefficient, so a separate product or minimizer argument is needed. It
must not simultaneously be counted as a bad Farkas cage.

## 4. Exact continuation-incompatibility ear calibration

Let

\[
\begin{array}{lll}
a=(0,0),&b=(6,0),&c=(0,6),\\
d=(3,-10),&e=(13,3),&f=(-10,13),\\
z=(1,2),&
h_0=(70,-97),&h_1=(68,79),\quad h_2=(-81,34).
\end{array}                                                     \tag{13}
\]

Put

\[
\begin{aligned}
 R_0&=\{a,b,c,d\},&S_0&=R_0\cup\{h_0\},\\
 R_1&=\{a,b,c,e\},&S_1&=R_1\cup\{h_1\},\\
 R_2&=\{a,b,c,f\},&S_2&=R_2\cup\{h_2\}.
\end{aligned}                                                     \tag{14}
\]

The ten displayed points are in general position. Every \(S_i\) is
ordinary, while \(S_i\cup\{z\}\) is nonordinary through the common
triangle \(abc\). The continuation compatibility matrix is exactly

\[
                         R_j\cup\{h_i\}\text{ ordinary}
                              \quad\Longleftrightarrow\quad i=j. \tag{15}
\]

Exact Fourier--Motzkin enumeration finds three feasible pairs of ear cells
for each pair \(S_i,S_j\), but zero simultaneously feasible choices for
all three polygons. Thus this is a genuine physical continuation-bearing
three-ear obstruction, except that its three continuations are necessarily
different.

Choose any deterministic ear cell \(C_i\) of \(S_i\) and give the three
records \((S_i,C_i,h_i)\) equal weight. Since no triple of ear-cell choices
for \(S_0,S_1,S_2\) has common intersection, the ordered bad-triple
probability is at least

\[
                              {3!\over3^3}={2\over9}.             \tag{16}
\]

Every same-continuation triple repeats one record and is feasible, so its
bad mass is zero. Moreover (15) prevents relabelling one of the actual
continuation singletons into the other two contexts.

Small disjoint rational perturbation clouds around the \(h_i\) preserve
all strict signs, giving arbitrarily many simple, distinct singleton
continuation records of each type. This calibration does not itself have
the low global repair depth required by the live hard branch; it proves
only that planarity and exact history decoding do not create continuation
collisions.

At the abstract fractional-Helly level the obstruction can be arbitrarily
strong: take \(K\) pairwise disjoint open convex chambers with distinct
continuations and equal weights. Then maximum repair depth is \(1/K\),
bad-triple probability is \(1-1/K^2\), and same-continuation bad mass is
zero. Hence some physical correlation beyond convexity is indispensable.

## 5. Exact remaining gate

A continuation-bearing cage follows with quasipolynomial loss under either
of these explicit additional inputs:

1. the Rényi collision bound \(K_3\le2^{O(L\log L)}\) together with
   fibrewise low repair depth;
2. a common physical repair position for the high-depth continuation
   fibres, with an output retaining \(h\); or
3. a mixed/profile bank which pays the high-dispersion continuation
   alphabet directly.

The current release/colouring/chronology/forest chain proves none of these.
The common role-\(1\) lift supplies (3), not (1): a rich common cap
continuation exposes a shared repair edge and exits the bad-cage branch.

## 6. Verification

The exact verifier
verify_continuation_bearing_three_ear_coalescing_gate.py checks:

* the shear order (8);
* the rank-two common-child lift, hidden label, and simultaneous repair;
* general position and the exact compatibility matrix (15);
* all \(5^3\) augmented ear-cell triples and all pair-cell counts; and
* the weighted \(2/9\) lower bound and the finite Rényi identity.

