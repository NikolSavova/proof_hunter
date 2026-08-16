# The third cloud and the KK edge-shadow terminal gate

**Date:** 2026-08-15. All logarithms are base two. This continues
'DENSE_CLOUD_CROSS_CIRCUIT_DELETION_FOREST.md'.

## Verdict

Kruskal--Katona removes support density from the deletion-forest gate up to
one exact rank threshold. Let

\[
       a=\log_2 3=1.584962500\ldots,\qquad
       \theta_*=2-a=0.415037499\ldots,\qquad
       \kappa_*={1\over a}=0.630929753\ldots.                    \tag{1}
\]

For a cloud \(X\) of size \(R=2^d\), choose a largest rank layer
\(\mathcal A\) in its induced face complex. If

\[
 |\mathcal A|\ge {F_C(R)\over R+1},\qquad
                    q:=\operatorname{rank}\mathcal A
                    \le(\kappa_*-\varepsilon)d,                  \tag{2}
\]

then the ordinary two-shadow of \(\mathcal A\) has size

\[
                |\partial_2\mathcal A|
                   \ge R^{a+\Omega_\varepsilon(1)-o(1)}.         \tag{3}
\]

Pair this literal edge bank with the \(H\ge F_C(R)\) faces in a second
cloud. Their good unions have load one. Hence they either meet the ambient
target \(K=F_C(N)\), or almost every edge--face pair is bad and the
fixed-label deletion forest reaches a singleton-versus-face \(1+3\)
residue. Thus **support-sparse low-rank layers are not a separate
obstruction**. The survivor is rank-heavy,

\[
                     q>(1/\log_2 3-o(1))\log R,                  \tag{4}
\]

or terminal rank at most one.

The third cloud gives a complementary theorem without a rank hypothesis.
For three disjoint macroscopic clouds \(X_1,X_2,X_3\), every triple

\[
              (x,y,F)\in X_1\times X_2\times\mathcal F(X_3)      \tag{5}
\]

has a canonical candidate face \(\{x,y\}\cup F\), and good candidates
decode (5) with load one. Since

\[
 |X_1||X_2|F_C(R)
       =K\,R^{\,2-\log_2 3-o(1)},                                \tag{6}
\]

only an \(R^{-\theta_*+o(1)}\) good fraction is needed. Failure produces
an almost-complete cross-edge-by-third-face circuit rectangle. Its
canonical circuit has exactly one of two forms:

* one external endpoint plus three labels of \(F\), producing a dense
  singleton--face \(1+3\) relation after a sharp factor-\(R\) projection;
* both external endpoints plus two labels of \(F\), producing a dense
  \(2+2\) edge--internal-pair relation with the literal face \(F\) still
  needed by the decoder.

This trichotomy is exact, but does not close the terminal anti-alignment.
There is a scalable planar saturation: split one anti-aligned parabolic
block into \(X_1,X_2\), and take complete rank-\(q\), \(q\ge3\), faces in
the opposite block \(X_3\). Every one of the \(R^2\binom Rq\) candidates
in (5) is bad. The regression is not live because its three induced
clouds are Boolean. No construction is presently known which realizes
this terminal pattern while keeping the three full induced banks at the
least-counterexample scale.

Therefore the exact live endpoint is now:

\[
\boxed{\begin{array}{c}
\text{a rank-heavy cloud layer above }\kappa_*\log R,\quad\text{or}\\
\text{an almost-complete singleton/edge--face anti-alignment whose}\\
\text{parabolic realization is excluded only by its Boolean cloud banks.}
\end{array}}                                                    \tag{7}
\]

No coefficient-half closure is claimed.

## 1. KK forces a large physical edge shadow

For a \(q\)-uniform family \(\mathcal A\), write

\[
 \partial_2\mathcal A
   =\{e\in{X\choose2}:e\subseteq A
                         \text{ for some }A\in\mathcal A\}.       \tag{8}
\]

Every member is an actual ordinary planar face.

### Theorem 1 (live layer to edge shadow)

Let \(|X|=R=2^d\), and suppose

\[
 |\mathcal A|=M\ge {2^{\Phi_C(d)}\over R+1},
 \qquad \mathcal A\subseteq{X\choose q},\qquad q\le\kappa d.      \tag{9}
\]

Then

\[
 |\partial_2\mathcal A|
    \ge R^{1/\kappa}\,d^{-O_C(1)}.                               \tag{10}
\]

In particular, if \(\kappa\le\kappa_*-\varepsilon\), then for some
\(\varepsilon'=\varepsilon'( \varepsilon)>0\),

\[
 |\partial_2\mathcal A|\ge R^{a+\varepsilon'}.                   \tag{11}
\]

#### Proof

Choose the unique real \(x\ge q\) such that

\[
                               M={x\choose q}.                    \tag{12}
\]

The Lovasz form of Kruskal--Katona gives

\[
                         |\partial_2\mathcal A|\ge{x\choose2}.    \tag{13}
\]

The standard generalized-binomial estimate
\(\binom xq\le(ex/q)^q\) gives

\[
\begin{aligned}
 \log x
 &\ge {\log M\over q}+\log q-\log e\\
 &\ge {d\over2\kappa}-O_C(\log d).                    \tag{14}
\end{aligned}
\]

Here \(\log M\ge\Phi_C(d)-d-O(1)\). Equations (13)--(14) prove (10).
If \(\kappa<1/a\), then \(1/\kappa>a\), proving (11). \(\square\)

The estimate is independent of the density
\(M/\binom Rq\). A layer which looks sparse in the full \(R\)-point
support still has a large actual two-shadow. This is precisely the
Kruskal--Katona input missing from the raw deletion-mask bound.

### Proposition 2 (a literal small support creates a complement bank)

Suppose, more strongly, that a face family \(\mathcal A\) is supported on
an actual set \(S\subset X\), \(|S|=s\), and put \(T=X\setminus S\).
Least-counterexample induction gives

\[
                         V(T)\ge F_C(R-s).                       \tag{14a}
\]

For

\[
 \mathcal G_{S,T}
  =\{(A,B)\in\mathcal A\times\mathcal F(T):
                                      A\cup B\in\mathcal F(P)\},  \tag{14b}
\]

the union map is injective. Thus either \(|\mathcal G_{S,T}|\ge K\), or
the two disjoint support banks form another dense bad face rectangle.

If \(s=o(R)\), direct target expansion gives

\[
 \log{F_C(R)\over F_C(R-s)}
       =O\!\left((\log R){s\over R}\right)=o(\log R),              \tag{14c}
\]

so the complement bank is \(F_C(R)R^{-o(1)}\). If both \(S\) and \(T\)
have fixed positive density, it is still \(F_C(R)/R^{O(1)}\). Hence a
small support carrying an \(H/R^{o(1)}\)-scale selected family does not
hide the mass: it exposes a second, disjoint \(H/R^{o(1)}\)-scale bank.

Applying the deletion forest to an unpaid \(\mathcal A\times\mathcal F(T)\)
rectangle either releases a proper trace of \(A\), or orients the whole
support \(S\) behind a complement face through the all-delete branch.
If this localization repeats on disjoint supports
\(S_1,\ldots,S_t\), every \(S_i\) carries its own selected \(H\)-scale
bank while the unpeeled remainder retains an induced \(H/R^{o(1)}\) bank,
provided \(\sum_i|S_i|=o(R)\).

This is the exact complement-induction consequence. It does not by itself
make mixed unions ordinary. The all-delete orientations define a directed
support system, but disjointness alone does not prove that the supports
occur as one ordered strong glue or a realized direction cycle. Such a
geometric promotion would invoke the existing linear-profile
potential/cycle telescope and would close; it remains an additional
hypothesis.

### Corollary 3 (edge-shadow face rectangle)

Let \(\mathcal B\subseteq\mathcal F(Y)\) be any family on a disjoint
cloud, and define

\[
 \mathcal G(\partial_2\mathcal A,\mathcal B)
 =\{(e,B):e\cup B\in\mathcal F(P)\}.                              \tag{15}
\]

The union map is injective on \(\mathcal G\). Therefore either
\(|\mathcal G|\ge K\), or, whenever
\(|\partial_2\mathcal A||\mathcal B|\gg K\), a \(1-o(1)\) fraction of
the edge--face rectangle is bad.

For \(R=(1-o(1))N/3\), \(|\mathcal B|\ge F_C(R)\), and (2), equations
(3) and

\[
                         {F_C(N)\over F_C(R)}
                              =R^{a+o(1)}                         \tag{16}
\]

show that the product capacity exceeds \(K\) by a fixed power. Applying
Theorem 1 of the deletion-forest report with row rank two reduces every
bad cell to a terminal singleton--face or empty-row state. The empty-row
state returns only the already counted \(\mathcal B\) bank; the singleton
state is the unresolved geometric branch.

If the largest layer in the cloud complex has rank above (4), (10) no
longer guarantees a target-sized edge shadow. This is the honest
rank-heavy exception.

## 2. The exact third-cloud polynomial gate

Let \(X_1,X_2,X_3\) be disjoint physical clouds, and let
\(\mathcal H_3\subseteq\mathcal F(X_3)\). Define

\[
 \mathcal T_{\rm good}
 =\{(x,y,F)\in X_1\times X_2\times\mathcal H_3:
                        \{x,y\}\cup F\in\mathcal F(P)\}.           \tag{17}
\]

### Theorem 4 (two singletons plus a third-cloud face)

The map

\[
                    (x,y,F)\longmapsto\{x,y\}\cup F              \tag{18}
\]

is injective on \(\mathcal T_{\rm good}\). If
\(|X_1|,|X_2|=(1-o(1))N/3\) and
\(|\mathcal H_3|\ge F_C((1-o(1))N/3)\), then

\[
 |\mathcal T_{\rm good}|\ge
       R^{-\theta_*+o(1)}
             |X_1||X_2||\mathcal H_3|                            \tag{19}
\]

already implies \(V(P)\ge F_C(N)\).

**Proof.** The three physical color classes recover \(x,y,F\) from (18),
so the load is one. The full rectangle has size
\((1-o(1))R^2F_C(R)\). Divide the target-to-cloud ratio (16) by \(R^2\);
the required density is \(R^{a-2+o(1)}=R^{-\theta_*+o(1)}\).
\(\square\)

Suppose (19) fails. Every bad candidate contains a bad four-set meeting
the external edge and \(F\). Choose one canonically. Because the external
trace has rank two and \(F\) is ordinary, its occupancy is one of

\[
                    1+3,\quad 1+3,\quad 2+2,                     \tag{20}
\]

according as it retains only \(x\), only \(y\), or both. One type carries
at least one third of the bad records.

In an \(x\)-only branch, projection

\[
                         (x,y,F)\longmapsto(x,F)                  \tag{21}
\]

has load at most \(|X_2|\). Hence \(T\) records give at least
\(T/|X_2|\) distinct singleton--face bad pairs, each with an actual
\(1+3\) witness. The \(y\)-only case is symmetric.

In the \(2+2\) branch the canonical witness is

\[
                         \{x,y\}\cup f,\qquad f\in{F\choose2}.     \tag{22}
\]

The literal state \((\{x,y\},f,F)\) recovers the record with load one.
Dropping \(F\) incurs exactly the codegree

\[
 \Lambda_2=\max_{e,f}
   |\{F\in\mathcal H_3:f\subseteq F,\
               e\cup f\text{ is the canonical circuit}\}|.       \tag{23}
\]

Thus the branch is either diffuse in actual pair tags or fixes one
physical \(2+2\) circuit with a large third-face fibre. The circuit itself
is bad; its ordinary three-subsets do not retain \(F\), so (23) is a
localization, not a payment.

## 3. Sharp planar three-cloud anti-alignment

Use the exact two-block parabolic construction from
'DENSE_HALL_TWO_CLOUD_PROFILE_BARRIER.md'. Put \(2R\) points in its first
parabolic block, with the orientation whose facing right profiles are
exactly ranks one and two, and split them into two \(R\)-point physical
colors \(X_1,X_2\). Put \(R\) points in the opposite parabolic block, with
the orientation whose facing left profiles are exactly ranks one and two;
call it \(X_3\).

For \(q\ge3\), take

\[
                            \mathcal H_3={X_3\choose q}.            \tag{24}
\]

Every \(\{x,y\}\), \(x\in X_1,y\in X_2\), is a facing rank-two profile
of the first block, but no \(F\in\mathcal H_3\) is a facing profile of
the second block. The exact two-block recurrence therefore gives

\[
                    \{x,y\}\cup F\notin\mathcal F(P)              \tag{25}
\]

for all \(R^2\binom Rq\) choices. Even singleton deletion does not help:
\(\{x\}\cup F\) and \(\{y\}\cup F\) remain bad because \(F\) is still
outside its facing profile.

This realizes zero good density in (19) and saturates the rank-one
terminal alternative of the deletion forest. For

\[
 q={1\over2}\log R-\left(C-{1\over2}+o(1)\right)\log\log R,        \tag{26}
\]

the selected third-face alphabet has size \(F_C(R)2^{o(d\log d)}\).
However every parabolic block is convex position, so its full induced bank
is Boolean. The example is a sharp planar selected-family barrier, not a
live least-counterexample array.

The nested-triangle incidence supplies three physical clouds but no proved
separation of their direction spectra. Conversely, the projective
universality constructions preserve the selected anti-alignment but have
not controlled all ambient faces at the live normalization. This is the
precise construction/proof gap after Theorems 1 and 3.

## 4. Decoder and coefficient ledger

All positive banks above use physical outputs:

* an edge-shadow good union recovers \(e,B\) by cloud intersection;
* a third-cloud good union recovers \(x,y,F\) by three-color intersection;
* the singleton projection (21) has the explicit and sharp load
  \(|X_2|\);
* the \(2+2\) state has load one only while the full \(F\) is retained,
  and otherwise has the literal codegree (23).

If several source contexts share the same three physical clouds, their
additional history multiplicity is not removed by these decoders. The
nested-array application has one fixed physical cloud triple; a global
sum over several roots must include its context load separately.

The two critical exponents are now transparent:

\[
\begin{array}{c|c}
\text{quantity}&\text{power of }R\\ \hline
K/H&a=\log_2 3,\\
\text{cross-singleton-pair capacity}&2,\\
\text{density needed in (19)}&-(2-a)=-\theta_*,\\
\text{KK rank cutoff}&\kappa_*=1/a.
\end{array}                                                     \tag{27}
\]

No argument in this report converts the terminal \(1+3\) or \(2+2\)
rectangle into the final fixed-power bank. That conversion is the sole
remaining geometric step in the rank-bounded branch.

## 5. Verification

Run

~~~text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_third_cloud_kk_singleton_terminal_gate.py
~~~

The verifier checks Lovasz--KK edge shadows on exhaustive/random small
families, audits the threshold constants and scale inequalities, and
exhausts the exact three-cloud parabolic saturation together with every
canonical circuit occupancy.
