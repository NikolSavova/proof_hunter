# Endpoint surplus: a projection-uniform balanced-shell barrier

**Date:** 2026-08-15. All counts below are nonempty and all logarithms are
base two. This note answers the endpoint-surplus question raised after
`THREE_CLOUD_CYCLIC_PROFILE_AND_PARTNER_BARRIER.md`.

## Verdict

For a generic projection direction \(\theta\), let \(C_\theta(P)\) and
\(U_\theta(P)\) be the cap and cup counts, let \(V(P)\) be the ordinary
convex-subset count, and put

\[
             \sigma_\theta(P)={C_\theta(P)U_\theta(P)\over V(P)}. \tag{1}
\]

The universal cap--cup encoding gives only

\[
                         \sigma_\theta(P)\ge1.          \tag{2}
\]

This is sharp at the exponent level even when

\[
                  V(P)=2^{\Theta((\log |P|)^2)}.        \tag{3}
\]

There is a scalable rational general-position family \(P_d\), of size
\(N_d\), for which (3) holds and, **simultaneously in every generic
projection chamber**,

\[
                  \sigma_\theta(P_d)\le (\log N_d)^{O(1)}
                                      =N_d^{o(1)}.       \tag{4}
\]

The construction is a nearly regular balanced convex shell of
\(K=\Theta((\log N)^2)\) points around a tiny logarithmic-rank Pascal core.
The shell supplies \(2^K\) ordinary faces. In any projection it has two
balanced boundary chains. A cap meeting the core can use arbitrary shell
labels from only one quarter-chain; using both sides puts a core point
strictly below the relevant shell chord and reverses the cap sign. Cups are
symmetric.

Thus no universal endpoint-surplus theorem, even after optimizing the
projection direction, can give the factor
\(N^{\log_2 3+o(1)}\) required by the three-cloud cyclic inequality. A
positive theorem must use extra live structure excluding a detached
Boolean shell, for example a rank-\(O(\log N)\) support condition together
with a decoder tying most face entropy to the physical cloud rather than
to an exterior convex layer.

This is a barrier to the proposed universal input, not a sub-half
construction: the shell itself is exactly the detached Boolean bank that
pays globally.

## 1. Definitions and the exact universal lower bound

Fix a generic oriented line and order the points by their projection. A
nonempty subset is a cap if every ordered triple has negative orientation,
and a cup if every ordered triple has positive orientation. These are the
conventions in the strong-glue recurrences used elsewhere in the attack.

Every ordinary face has a unique upper/lower boundary decomposition. The
two boundary chains are respectively a cap and a cup and recover the face.
Consequently

\[
                         V(P)\le C_\theta(P)U_\theta(P), \tag{5}
\]

which proves (2). Reflection of the projection swaps \(C_\theta,U_\theta\)
and leaves their product unchanged.

Notice that (5) is direction-by-direction. It does not compare endpoint
profiles from different chambers. The construction below is stronger than
needed to refute a fixed-chart claim: its upper bound holds in every
chamber.

## 2. The balanced-shell counting lemma

The following elementary shell lemma isolates the geometry.

> **Lemma 1 (balanced shell).** For every sufficiently large multiple
> \(K\) of four there is a rational centrally symmetric strictly convex
> \(K\)-set \(S_K\), and a disk \(D_K\) about its centre, with the following
> properties. For every finite general-position set \(Q\subset D_K\) and
> every generic projection \(\theta\):
>
> 1. the number of shell-only caps and shell-only cups is at most
>    \(K^2 2^{K/2+O(1)}\);
> 2. the number of possible shell traces of a cap which also meets \(Q\) is
>    at most \(K^2 2^{K/4+O(1)}\), and the same holds for cups.

**Construction and proof.** Start with a regular \(K\)-gon on a circle,
keep antipodal pairs, and approximate its vertices by rational points on
the rational unit circle so closely that every angular interval of length
\(\pi/2\) contains at most \(K/4+2\) vertices. The rational parametrization

\[
                  t\longmapsto
       \left({1-t^2\over1+t^2},{2t\over1+t^2}\right)     \tag{6}
\]

and the antipodal map give such a centrally symmetric shell. Points on a
strictly convex conic are in general position.

For a fixed projection, its two extrema are antipodal. Hence the two
boundary chains have equal length. A cap is determined by its projected
left and right endpoints; after those are fixed, every other shell label
must lie on the cap-side monotone boundary arc. There are at most
\(K/2+O(1)\) eligible labels. Summing over fewer than \(K^2\) endpoint pairs
proves the first cap bound. The cup proof is identical.

Now suppose a cap also contains \(q\in Q\). Apart from the two projection
extrema and \(O(1)\) labels in the tiny central projection band, its
cap-side shell labels cannot occur on both sides of \(q\). Indeed, two
such labels \(x_-<q<x_+\) lie on the same circular boundary semicircle.
Their chord strictly separates the centre from that semicircle, so
\((x_-,q,x_+)\) has the wrong sign for a cap. The only zero-margin chord is
the diameter joining the two projection extrema, which accounts for the
constant exceptions.

Choose \(D_K\) smaller than the minimum positive distance from the centre
to a non-diameter shell chord and smaller than the angular-spacing
projection margin. The eligible labels on either remaining quarter-chain
number at most \(K/4+O(1)\). Endpoint summation proves the second cap
bound. Reflecting the picture proves the cup bound. Since the shell has
only finitely many projection chambers, the one disk works simultaneously
for all generic directions. \(\square\)

The powers \(K^2\) and the additive constants are deliberately loose. A
direct endpoint summation for an exactly balanced convex polygon gives a
constant multiple of \(2^{K/2}\). Polynomial slack is enough here.

## 3. The scalable quasipolynomial family

Take even \(d\), put

\[
                  Q_d=T(d,d/2),\qquad
                  m=|Q_d|={d\choose d/2}.                \tag{7}
\]

The standard rational Pascal-cell realization has no ordinary face of rank
greater than \(d\). In particular, in every projection,

\[
 C_\theta(Q_d),U_\theta(Q_d),V(Q_d)\le
 M_d:=\sum_{j=1}^{d}{m\choose j}\le\left({em\over d}\right)^d. \tag{8}
\]

Choose a multiple \(K\) of four such that

\[
 {K\over4}\ge \log M_d+3\log K+10.                       \tag{9}
\]

Since \(\log m=d-O(\log d)\), one may take \(K=\Theta(d^2)\). Affinely
shrink a rational realization of \(Q_d\) into the disk \(D_K\) of Lemma 1,
and make a generic rational perturbation within the disk if necessary. Put

\[
                          P_d=S_K\cup Q_d.                \tag{10}
\]

The perturbation preserves the core order type, shell separation, and
general position.

For every projection \(\theta\), heredity of caps and Lemma 1 give

\[
\begin{aligned}
 C_\theta(P_d)
 &\le K^2 2^{K/2+O(1)}
      +M_dK^2 2^{K/4+O(1)}\\
 &\le K^{O(1)}2^{K/2},                                   \tag{11}
\end{aligned}
\]

where (9) absorbs the mixed term. The identical estimate holds for
\(U_\theta(P_d)\).

Every nonempty shell subset is ordinary, so

\[
                            V(P_d)\ge2^K-1.               \tag{12}
\]

Conversely, the intersection of an ordinary set with either physical part
is ordinary, because every subset of a convex-position set is again in
convex position. Therefore the trace map is injective and

\[
                       V(P_d)\le (2^K-1)V(Q_d)\le2^KM_d. \tag{13}
\]

Equations (11)--(13) prove

\[
                 \sigma_\theta(P_d)\le K^{O(1)}          \tag{14}
\]

uniformly in \(\theta\). Finally

\[
 N_d=m+K=(1+o(1))m,\qquad
 K=\Theta(d^2)=\Theta((\log N_d)^2),                     \tag{15}
\]

and (8), (12), (13) prove (3)--(4).

## 4. Rank and downset scope

The construction deliberately uses a Boolean shell of rank
\(K=\Theta((\log N)^2)\). Thus it does not refute a theorem with an explicit
maximum-rank hypothesis \(O(\log N)\), nor a theorem asserting that a
positive fraction of the endpoint entropy must use labels from the live
source/core support. It does refute all bounds based only on

* \(N\), \(V(P)=2^{\Theta((\log N)^2)}\), and downset heredity;
* the freedom to optimize over projection chambers; or
* the existence of three macroscopic physical clouds without excluding a
  detached exterior convex layer.

In the three-cloud inequality

\[
 \max_i B_i\ge(H_1H_2H_3)^{1/3}
              (\sigma_1\sigma_2\sigma_3)^{1/3},          \tag{16}
\]

three copies of (14) contribute only \((\log N)^{O(1)}\), whereas closure
requires \(N^{\log_2 3+o(1)}\). Hence endpoint surplus cannot be the
unconditional missing multiplier.

## 5. Exact verification

Run

~~~text
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_endpoint_surplus_balanced_shell_barrier.py
~~~

The verifier uses a rational centrally symmetric octagon plus a rational
three-point central child. It exhausts all 2,047 nonempty subsets and all
41 exact half-turn projection chambers. The ordinary face count is 653,
the cap count ranges from 175 to 205, and
\(C_\theta U_\theta/V<61\) in every chamber. It also checks the exact
integer rank envelope, shell size, absorption inequality, and
quasipolynomial scale for central Pascal cores through \(d=64\).
