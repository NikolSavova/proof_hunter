# Polylog cap--cup conversion: an exact load barrier and the minimizer Gibbs gate

**Date:** 2026-08-15.  All logarithms are base two and all face counts are
nonempty.

## Verdict

The parent-upper endpoint surplus from
`PARENT_UPPER_ENDPOINT_RESET_THRESHOLD.md` cannot be converted by a
universal all-pairs decoder, even after retaining the canonical common root
or allowing polylogarithmically many projection charts.

Let \(Q\) be any balanced planar configuration of size \(N\), meaning
\(C(Q)=U(Q)=E\) in one chart, and put

\[
                            P=Q\prec Q.                         \tag{1}
\]

Then

\[
 W(P)=2W(Q)+E^2,\qquad C(P)=U(P)=(N+2)E.                       \tag{2}
\]

Since \(W(Q)\le E^2\), every map from all ordered cap--cup pairs of \(P\)
to tagged ordinary faces has maximum load

\[
 \boxed{\displaystyle
       \Lambda\ge {C(P)U(P)\over T W(P)}
          \ge{(N+2)^2\over3T},}                                \tag{3}
\]

where \(T\) is the number of possible auxiliary tags.  Thus:

* a fixed canonical carrier/root and polylogarithmic metadata leave
  \(\Lambda=N^{2-o(1)}\);
* even one freely varying physical root leaves \(\Lambda=N^{1-o(1)}\); and
* two physical-label degrees of freedom are the first crude tag capacity
  capable of absorbing the obstruction.

The balanced iterated cup--cap upper construction makes (3) a stretchable,
rank-\(O(\log N)\), dense all-delete/common-root obstruction at leading
coefficient \(1/2\).  Hence the desired fixed-gap converter must select a
special inverse-polylogarithmic fraction of endpoint pairs using genuinely
new geometry; it cannot be defined on all pairs and then bounded by a
canonical root decoder.

There is an exact minimizer mutation inequality, but it is weighted and does
not supply that selection.  If \(P\) is globally \(V\)-minimal among
\(n\)-point configurations and \(0<p<1\), define

\[
\begin{aligned}
 G_p(P)&=\sum_{F\in\mathcal F(P)}
       \{p^{|F|}+(1-p)^{|F|}\},\\
 Z_p(P)&=\sum_{\substack{A\in\mathcal C(P),\ B\in\mathcal U(P)\\
                         A\cap B=\varnothing}}
             p^{|A|}(1-p)^{|B|}.                              \tag{4}
\end{aligned}
\]

Then

\[
 \boxed{
 W(P)\le G_p(P)+Z_p(P),\qquad
 Z_p(P)\ge2p(1-p)\{W(P)-n\}.}                                 \tag{5}
\]

At \(p=1/2\), every minimizer therefore satisfies

\[
                 Z_{1/2}(P)\ge{W(P)-n\over2}.                  \tag{6}
\]

Equation (5) is the exact multi-scale endpoint-energy charge furnished by
global mutation.  It is not an unweighted converter: a rank-\((r+s)\) pair is
discounted by \(2^{-(r+s)}\), and the live endpoint surplus is only
polylogarithmic at coefficient one half.  Removing that rank weight costs a
polynomial factor on the established \(O(\log n)\) slice, which is too much.

The precise surviving theorem is therefore:

> In a least fixed-gap counterexample, prove that an inverse-polylogarithmic
> fraction of the endpoint product forced by the parent upper bound admits
> either (i) an ordinary same-configuration union with polylogarithmic load,
> or (ii) one \(V\)-decreasing physical bipartition mutation.  The common
> root/all-delete state and the Gibbs necessity (5) do not imply either
> alternative by themselves.

This is an exact barrier and minimizer reduction, not a half-bound closure.

## 1. Quadratic load lower bound

For every planar \(Q\), upper/lower hull decomposition gives

\[
                              W(Q)\le C(Q)U(Q).                  \tag{7}
\]

If \(C(Q)=U(Q)=E\), equations (2) and (7) imply

\[
 W(P)\le3E^2,\qquad C(P)U(P)=(N+2)^2E^2.                       \tag{8}
\]

Suppose a converter assigns each of the \(C(P)U(P)\) ordered pairs a
target \((F,\tau)\), where \(F\in\mathcal F(P)\) and \(\tau\) lies in a tag
alphabet of size \(T\).  There are at most \(TW(P)\) targets, so pigeonhole
gives (3).  The conclusion is independent of how the map is defined and
therefore also applies to adaptive repair, first-divergence, or Hall routing
once their retained metadata are included in \(T\).

Ordinary convexity is projectively invariant.  Consequently, allowing
\(s\) same-configuration projection charts does not create new target faces;
it merely contributes a chart tag \(T=s\).  A fixed common base and common
root contribute no tag entropy.  If one physical root is allowed to vary,
then \(T\le n\); (3) is still linear in \(N\).  This makes precise why the
earlier two-ended/second-surviving-label operation is qualitatively
different from another rooted one-ended profile.

The theorem concerns a converter defined on **all** cap--cup pairs.  A proof
needs less: if the endpoint product is \(S\) times the desired target, it is
enough to recover a subfamily of density roughly \(1/S\).  At the half
fixed gap, `PARENT_UPPER_ENDPOINT_RESET_THRESHOLD.md` gives
\(S\ge2^{3/2}L^K\).  Therefore the correct positive target is an
inverse-polylogarithmic compatible-pair density, not an all-pairs map.

In the balanced calibration, the canonical matching-endpoint hull pairs
number exactly \(W(P)\), only a \(3/(N+2)^2\) fraction of the full product.
The common rooted all-delete rectangle does not change this count: its
release routing has the exact source cancellation already proved in that
report.

There is an exact geometric strengthening for the endpoint pairs which
create the quadratic factor in (3).  The spanning caps and cups of (1) are

\[
 \mathcal C_{\rm sp}=\{A\cup\{z\}:A\in\mathcal C(Q_L),\ z\in Q_R\},
 \qquad
 \mathcal U_{\rm sp}=\{\{y\}\cup B:y\in Q_L,\ B\in\mathcal U(Q_R)\}.
                                                               \tag{8a}
\]

They have sizes \(NC(Q)\) and \(NU(Q)\).  Suppose every cap and cup of
\(Q\) has rank at most \(R\).  If the union of a pair in (8a) is ordinary,
then its left and right traces are respectively

\[
                         A\cup\{y\}\in\mathcal C(Q_L),
 \qquad B\cup\{z\}\in\mathcal U(Q_R).                         \tag{8b}
\]

For a fixed output trace \(A'\), there are at most \(2|A'|\le2R\) pairs
\((A,y)\) with \(A\cup\{y\}=A'\): after choosing \(y\in A'\), either
\(A=A'\) or \(A=A'\setminus\{y\}\).  The reflected statement holds on the
right.  Hence

\[
 \boxed{
 {\#\{(K,L)\in\mathcal C_{\rm sp}\times\mathcal U_{\rm sp}:
                 K\cup L\text{ ordinary}\}
  \over |\mathcal C_{\rm sp}||\mathcal U_{\rm sp}|}
 \le {4R^2\over N^2}.}                                      \tag{8c}
\]

There is also an exact activity-free form.  Let
\[
 M_C=\sum_{A\in\mathcal C(Q)}|A|,\qquad
 M_U=\sum_{B\in\mathcal U(Q)}|B|.
\]
The number of addable pairs \((A,y)\) with
\(A\cup\{y\}\in\mathcal C(Q)\) is
\[
                         E_C=2M_C-N,                           \tag{8d}
\]
because a rank-\(r\ge2\) output cap has \(r\) representations with
\(y\in A\) and \(r\) with \(A=A'\setminus\{y\}\), while a singleton has
only the first representation.  Dually \(E_U=2M_U-N\).  The two block
conditions in (8b) are independent, so the numerator of (8c) is exactly
\[
                              E_CE_U.                          \tag{8e}
\]
Thus (8c) is precisely the statement that both endpoint-complex mean ranks
are at most \(R\), not a loose four-local estimate.

For the live \(R=O(\log N)\) calibration this is \(N^{-2+o(1)}\), far
below the inverse-polylogarithmic density required by the parent upper
bound.  Thus direct union of the dominant endpoint pairs is not the
selected reset.  Almost every such pair is a genuine bad cross-block union
and must be repaired through its physical four-circuit, or used to exhibit
a decreasing mutation.  The two arbitrary singleton anchors \(y,z\) are
exactly the two missing history coordinates.

Indeed, if \(A\cup\{y\}\) is not a cap, a first wrong-sign triple uses
\(y\) and two labels of \(A\).  Appending **any** right-block label makes
that triple plus the right label a bad four-set by the strong-glue
classification.  The bad-pair complement of (8e) is therefore a literal
common-neighbourhood rooted \(1+3\) circuit family.  Deleting \(y\) releases
the spanning cap \(A\cup\{z\}\), but also erases exactly the anchor whose
entropy created the missing factor.  This recovers the all-delete gate in
endpoint language rather than bypassing it.

## 2. Exact random-bipartition mutation

Let \(P[R]\) be the order type induced by \(R\subseteq P\).  For every
bipartition \(P=R\sqcup S\), vertically strongly glue rational realizations
of the two induced order types.  The new \(n\)-point configuration has

\[
              M(R,S)=W(P[R])+W(P[S])+C(P[R])U(P[S])             \tag{9}
\]

ordinary faces.  Hence global \(V\)-minimality gives the pointwise family
of inequalities

\[
                              W(P)\le M(R,S)                    \tag{10}
\]

for every bipartition.  Empty sides cause no problem: the mutation is just
the nonempty induced configuration.

Colour each point red with probability \(p\), independently, and take
\(R\) red and \(S\) blue.  A face \(F\) survives on the red or blue side
with total probability \(p^{|F|}+(1-p)^{|F|}\).  A cap \(A\) and cup \(B\)
contribute to the cross term exactly when they are disjoint and all of
\(A\) is red while all of \(B\) is blue.  Taking expectations in (10) gives
the first inequality in (5).

For a singleton face the two survival probabilities sum to one.  For every
face of rank at least two,

\[
 p^{|F|}+(1-p)^{|F|}\le p^2+(1-p)^2=1-2p(1-p).                 \tag{11}
\]

Therefore

\[
 G_p(P)\le n+\{1-2p(1-p)\}\{W(P)-n\},                         \tag{12}
\]

which proves the second inequality in (5).

This is stronger than a formal reflection mutation: it uses every induced
physical bipartition of the same minimizer.  But it is a **lower** bound on
the weighted disjoint-pair partition function.  To contradict minimality,
one would need an upper bound making \(G_p+Z_p<W(P)\), or a single explicit
partition violating (10).  The canonical all-delete state presently gives
neither.

At \(p=1/2\), the weight of a pair is \(2^{-|A|-|B|}\).  The marked source
slice has rank \(O(\log n)\), so forgetting this weight may cost
\(n^{O(1)}\).  The parent endpoint surplus at the half fixed gap is only
\((\log n)^K\).  This is the exact scale mismatch: the minimizer mutation is
real, but its Gibbs normalization is too severe unless one first proves
that the useful endpoint differences have only \(O(\log\log n)\) bits or
share a recoverable long trace.

## 3. Exact planar calibration

Take \(Q=T(4,2)\), whose exact profile is

\[
                              (C,U,W)=(31,31,50).                \tag{13}
\]

The rational twelve-point wrapper \(P=Q\prec Q\) has

\[
                         (C,U,W)=(248,248,1061).                 \tag{14}
\]

Direct enumeration gives 19 noncap and 19 noncup child faces, and verifies
the complete all-delete rectangle and the common positive-triple witness.
The two spanning endpoint families in (8a) each have 186 members.  Among
their 34596 ordered pairs, exactly 15876 have ordinary union, with exactly
\(961=31^2\) distinct outputs and maximum output load
\(36=4\cdot3^2\), attaining the bound used in (8c).
For this configuration the exact fair-colouring quantities are

\[
                   G_{1/2}={669\over4},\qquad
                   Z_{1/2}={61057\over64},                       \tag{15}
\]

so

\[
                         G_{1/2}+Z_{1/2}
                            ={71761\over64}=1121.265625>1061.    \tag{16}
\]

Thus even the averaged minimizer inequality is compatible with the finite
all-delete wrapper.  The wrapper is not globally minimal: exhaustive
physical bipartitions find

\[
                     \min_{R\sqcup S=P}M(R,S)=688<1061.         \tag{17}
\]

This distinction is useful.  The average Gibbs condition is necessary but
not sufficient for minimizer status; a positive proof must exploit a
specific low mutation, not only its expectation.

For the scalable half calibration, use the balanced iterates
\(Q_{k,d}\) from `PARENT_UPPER_ENDPOINT_RESET_THRESHOLD.md`.  They have

\[
 C(Q_{k,d})=U(Q_{k,d}),\qquad
 {\log W(Q_{k,d})\over(\log |Q_{k,d}|)^2}\to\rho_k,qquad
 \rho_k\downarrow{1\over2}.                                  \tag{18}
\]

Their two-block wrappers are rational, have rank \(O(\log N)\), dense
noncap/noncup sides, and a linear-degree common rooted triple.  Equation
(3) applies exactly at every finite stage.  This is not a least fixed-gap
counterexample, because its subleading term does not satisfy the strict
parent upper bound.  It is a sharp refutation of any proposed converter
which uses only the retained local state and leading coefficient.

## 4. Consequence for the live gate

The parent upper bound now has one rigorously isolated use: it produces the
endpoint surplus \(S\) in (4) of the previous report.  The current note
shows what must happen next.

1. An all-pairs converter is impossible: its load can be quadratic even in
   the exact rank-safe planar normal form.
2. A fixed root, a common carrier, and polylogarithmic chart metadata do not
   change that conclusion.  One varying physical label still leaves linear
   load.
3. Global minimizer status supplies every pointwise mutation inequality
   (10) and the Gibbs consequence (5), but not the required unweighted
   inverse-polylogarithmic compatible density.
4. Therefore the sole viable positive operation is a **selected endpoint
   reset**: use the canonical all-delete/rooted geometry to choose at least
   an \(L^{-O(1)}\) fraction of the endpoint energy whose differences have
   only \(O(\log L)\) entropy, or exhibit one actual bipartition with fewer
   than \(W(P)\) faces.

This selected-density statement is strictly stronger than every currently
banked source-release or one-ended profile theorem and is not implied by
the balanced Pascal calibration.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_polylog_cap_cup_converter_mutation_gate.py
```

The checker uses exact rational coordinates and fractions.  It verifies
the quadratic load inequality, enumerates every cap, cup, and ordinary face
of the twelve-point wrapper, checks the spanning-pair compatibility bound
(8c), checks all \(2^{12}\) physical bipartition mutations, and reproduces
(13)--(17) and the exact random-colouring identity.
