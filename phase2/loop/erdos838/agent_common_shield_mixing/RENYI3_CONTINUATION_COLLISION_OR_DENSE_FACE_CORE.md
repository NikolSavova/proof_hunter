# Rényi-3 continuation collision or dense face--face core

**Date:** 2026-08-15. All logarithms are base two. All target faces are
literal ordinary faces in one planar configuration \(P\), and
\(V=V(P)\).

## Verdict

The strongest universal continuation inequality is an exact
collision-versus-bank identity:

\[
 \sum_h d_h^3={W^3\over K_3^2},\qquad
 K_3=\left({W^3\over\sum_hd_h^3}\right)^{1/2}
                       \le|\{h:d_h>0\}|.                         \tag{1}
\]

Here \(d_h\) is the total record mass carrying literal continuation face
\(h\), and \(W=\sum_hd_h\). Low \(K_3\) gives same-continuation triple
collisions. High \(K_3\) gives many literal continuation faces, but no
universal Hölder, Cauchy, or Hall argument multiplies those faces by the
source/context bank.

There is nevertheless a sharp global reduction. Assume each record has a
literal source/context face \(s\), a continuation face \(h\), and aggregate
pair load at most \(\lambda\). Ordinary mixed unions either give a decoded
one-face bank, or the remaining mass contains a weighted bipartite core
with:

* only nonordinary unions \(s\cup h\);
* at least half the bad mass;
* minimum weighted degree at least bad mass divided by \(4V\) on both
  sides;
* minimum distinct degree at least bad mass divided by
  \(4\lambda V\); and
* retained continuation effective count at least a constant multiple of
  the original \(K_3\).

At the live normalization \(W\ge V^2/K_0\), with
\(K_0=2^{O(L\log L)}\), this is a genuinely dense face--face
anti-compatibility core: every surviving face has
\(V/(\lambda K_0)\) incompatible partners up to constants. This is the
precise high-\(K_3\) residue.

The existing normalization does **not** bound \(K_3\) quasipolynomially.
An exact stretchable anti-aligned two-cloud regression has a complete
\(M\times M\) unit-load bad rectangle, \(K_3=M\), and only
\(\Theta(2^p)\) ambient faces while
\(M=\binom p{\lfloor p/2\rfloor}\). Hence
\(W=M^2=V^2/\operatorname{poly}(p)\). It saturates the live incidence
normalization and every inequality below. Its rank is \(\Theta(p)\), so it
is not the live rank-\(O(\log n)\) fixed-gap obstruction; its Boolean cloud
banks visibly pay. A closure must use that rank/internal-bank input on the
dense core, not record normalization alone.

## 1. Literal record matrix and exact loads

Let \(\mathcal S,\mathcal H\subseteq\mathcal F(P)\). Aggregate all records
with targets \((s,h)\) into a nonnegative matrix

\[
                         a_{s,h}\ge0,\qquad
 \sum_{s,h}a_{s,h}=W,\qquad \max_{s,h}a_{s,h}\le\lambda.          \tag{2}
\]

The last inequality is the actual ordered-pair decoder load, including
genuine history multiplicity. Define

\[
                         d_h=\sum_sa_{s,h}.                       \tag{3}
\]

Equation (1) is a definition followed by power mean:

\[
             \left(\sum_hd_h\right)^3
                  \le |\operatorname{supp}d|^2\sum_hd_h^3.       \tag{4}
\]

Thus the universal threshold dichotomy is exact:

* if \(K_3\le K\), the ordered same-continuation collision mass is at least
  \(W^3/K^2\);
* if \(K_3>K\), there are more than \(K\) distinct literal continuation
  faces.

Combining the first branch with fibrewise fractional Helly gives the
continuation-bearing cage theorem in
CONTINUATION_BEARING_THREE_EAR_COALESCING_GATE.md. The second conclusion is
only a one-bank statement.

## 2. Mixed output or dense bad core

Call a matrix entry geometrically good when \(s\cup h\) is ordinary and
the union output recovers \((s,h)\) with aggregate load at most
\(\Lambda_{\rm mix}\). Let \(G\) be the good record mass. Then

\[
                              G\le\Lambda_{\rm mix}V.             \tag{5}
\]

Put

\[
                         B=W-G,\qquad \alpha={B\over W}.          \tag{6}
\]

The bad matrix \(b\) is obtained by retaining only nonordinary pairs.

> **Theorem 1 (load-tracked dense-core reduction).** If \(B>0\), the bad
> support contains subfamilies
> \(\mathcal S_*\subseteq\mathcal S\),
> \(\mathcal H_*\subseteq\mathcal H\) and a restricted matrix \(c\) such
> that
> \[
> \begin{aligned}
> C:=\sum_{s,h}c_{s,h}&\ge {B\over2},\\
> \sum_hc_{s,h}&\ge {B\over4|\operatorname{supp}_{\mathcal S}b|}
>                         \ge {B\over4V}\quad(s\in\mathcal S_*),\\
> \sum_sc_{s,h}&\ge {B\over4|\operatorname{supp}_{\mathcal H}b|}
>                         \ge {B\over4V}\quad(h\in\mathcal H_*).
>                                                                  \tag{7}
> \end{aligned}
> \]
> Every core pair is bad, every nonzero entry is at most \(\lambda\), and
> hence every core vertex has at least
> \[
>                              {B\over4\lambda V}                  \tag{8}
> \]
> distinct opposite neighbours. Moreover its continuation effective count
> obeys
> \[
> K_3(c):={C^{3/2}\over
>          \left(\sum_h(\sum_sc_{s,h})^3\right)^{1/2}}
>             \ge\left({\alpha\over2}\right)^{3/2}K_3.             \tag{9}
> \]

**Proof.** Let \(S_b,H_b\) be the two bad support sizes. Repeatedly delete a
row of current mass less than \(B/(4S_b)\) or a column of current mass less
than \(B/(4H_b)\). Each vertex is deleted once. Row deletions discard less
than \(S_bB/(4S_b)=B/4\), and column deletions discard less than \(B/4\).
The remaining mass is at least \(B/2\) and has (7). Both target families
consist of literal faces, so \(S_b,H_b\le V\). Dividing weighted degree by
the pair cap \(\lambda\) proves (8).

Let \(c_h=\sum_sc_{s,h}\). Since \(0\le c_h\le d_h\),

\[
                 \sum_hc_h^3\le\sum_hd_h^3={W^3\over K_3^2}.
\]

Together with \(C\ge B/2=\alpha W/2\), this proves (9).
\(\square\)

The whole core has exact fractional Hall density

\[
 {C\over|\mathcal S_*|+|\mathcal H_*|}
                         \ge {B\over4V}.                         \tag{10}
\]

No dyadic bucketing or atom floor is needed.

### Live scale

Suppose

\[
             W\ge {V^2\over K_0},\qquad
             \Lambda_{\rm mix}V\le\varepsilon W.                 \tag{11}
\]

Then \(B\ge(1-\varepsilon)W\), and (8)--(10) give

\[
\begin{aligned}
 \deg_{\rm distinct}(x)&\ge
       {1-\varepsilon\over4\lambda}{V\over K_0}
       \qquad(x\in\mathcal S_*\cup\mathcal H_*),\\
 {C\over|\mathcal S_*|+|\mathcal H_*|}
       &\ge {1-\varepsilon\over4}{V\over K_0},\\
 K_3(c)&\ge
       \left({1-\varepsilon\over2}\right)^{3/2}K_3.               \tag{12}
\end{aligned}
\]

This is the strongest consequence of the present literal targets and
loads. The remaining core is not a sparse metadata artefact.

## 3. Why Cauchy, Hölder, and Hall stop here

The two target faces recover at least \(W/\lambda\) distinct ordered pairs,
but ordered pairs of faces are not themselves ordinary faces. Universally,

\[
                         W\le\lambda
                           |\mathcal S|\,|\mathcal H|
                         \le\lambda V^2.                          \tag{13}
\]

A complete bipartite matrix attains equality. Hall pruning can route mass
to one endpoint bank, but both endpoint banks were already counted in
\(V\). Hölder gives exactly (1): lowering third collisions increases the
literal continuation support, without producing mixed unions.

In particular, the tempting estimate

\[
       \text{large }K_3
          \quad\Longrightarrow\quad
       \text{source bank}\times\text{continuation bank}
          \text{ ordinary}
\]

is false. The missing operation is geometric compatibility, not overlap
accounting.

## 4. Exact stretchable normalization regression

Use the two infinitesimal parabolic clouds from
DENSE_HALL_TWO_CLOUD_PROFILE_BARRIER.md. Let \(Y,Z\) each have \(p\)
points. Reflect their local charts so the two directional profiles facing
one another consist exactly of the singleton and pair subsets. Put

\[
                    T_p=2^p-1,\qquad
                    S_p=p+\binom p2.                              \tag{14}
\]

Both clouds have \(T_p\) nonempty ordinary faces, and the exact two-block
recurrence is

\[
                         V(Y\cup Z)=2T_p+S_p^2.                    \tag{15}
\]

Fix \(r\ge3\), and take

\[
              \mathcal S={Y\choose r},\qquad
              \mathcal H={Z\choose r},\qquad
              M=\binom pr.                                       \tag{16}
\]

Every target is a literal ordinary face. Every cross union is nonordinary,
because both traces have rank at least three. Put one unit record on every
pair. Then

\[
                  W=M^2,\qquad\lambda=1,\qquad
                  d_h=M,\qquad K_3=M.                             \tag{17}
\]

The bad graph is complete, its Hall density is \(M/2\), and Theorem 1 is
sharp up to its harmless constants.

For \(r=\lfloor p/2\rfloor\),

\[
 M={2^{p+o(p)}\over\sqrt p},\qquad
 V(Y\cup Z)=2^{p+1+o(p)},\qquad
 W={V(Y\cup Z)^2\over p^{1+o(1)}}.                               \tag{18}
\]

Thus even a polynomial-loss version of the live quadratic normalization
does not bound \(K_3\).

This is a scope-sharp regression, not a least-counterexample construction.
Its selected rank is \(\Theta(p)\), and the two Boolean child banks
\(T_p\) visibly pay. If instead \(r=O(\log p)\), the selected layer is
quadratic-logarithmic but negligible compared with \(T_p\). Therefore the
remaining live question is precisely:

> can a rank-\(O(L)\), low-\(V\) realization support the dense bad core
> (12) without creating a summable internal/profile bank?

That is stronger and narrower than bounding \(K_3\) from the current
normalization.

## 5. Consequence for the campaign

The global Rényi gate now has an exact three-way form.

1. **Mixed branch:** \(G\) in (5) is large and decoded ordinary unions pay.
2. **Collision branch:** \(K_3\le2^{O(L\log L)}\), so
   same-continuation fractional-Helly/Farkas triples survive with
   quasipolynomial loss.
3. **Dense face-core branch:** \(K_3\) is high and (12) supplies a
   continuation-rich, high-minimum-degree bipartite family of literal
   source and continuation faces whose every union is nonordinary.

Existing Cauchy/Hall identities cannot eliminate branch 3. The next valid
input must use rank-safe downshadows, fixed-edge circuit traces, or an
internal cap/cup profile bank **inside this one core**, with its pair load
\(\lambda\) retained.

## 6. Verification

The exact verifier
verify_renyi3_continuation_collision_or_dense_face_core.py exhausts small
integer weighted matrices, checks (1) and the pruning theorem, and verifies
the rational anti-aligned two-cloud recurrence and complete rank-layer
regression through cloud size seven.

