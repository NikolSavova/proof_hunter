# Macro-run endpoint-spectrum width gate

**Date:** 2026-08-15. All face, cap, and cup counts below count nonempty
subsets. This note uses only the exact linear strong-glue recurrence and the
universal cap--cup encoding. It does **not** use the false arbitrary-child
cyclic endpoint-profile factorization.

## Verdict

There is an exact necessary condition for a completed child to support a
coherent \(q\)-role macro ramp. Let the child have \(D\) points, \(H\) ordinary
convex faces, and an attainable menu of endpoint profiles \((C,U)\). After
discarding coordinatewise dominated profiles, put

\[
 c_-:=\min C,\qquad c_+:=\max C,
 \qquad S:=\log_{D+1}\frac{c_+}{c_-}.                       \tag{1}
\]

For every choice of \(q\ge2\) independently recharted physical copies in a
genuine linear strong glue, the first-to-last term alone is at least

\[
                 H(D+1)^{q-2-S}.                           \tag{2}
\]

Consequently a formal ramp with total face count at most \(KqH\) requires

\[
                 S\ge q-2-\log_{D+1}(Kq).                  \tag{3}
\]

Thus a scalar recursively closed ramp needs to regenerate essentially one
fresh power of \(D\) of endpoint-spectrum width per retained macro role.
Endpoint balance in one or two selected charts is not enough.

The fully exhausted 44-point parent of
`PARETO_TWO_LEVEL_RECURSIVE_MENU.md` has

\[
 H=747670,\qquad c_-=15121,\qquad c_+=102449,\qquad
 S=0.5026136708\ldots .                                    \tag{4}
\]

Already for \(q=3\),

\[
 45\,c_-=680445>6c_+=614694,
\]

so (2) is

\[
 \frac{747670\cdot45\cdot15121}{102449}
 =4965868.9996\ldots>6H=4486020.                           \tag{5}
\]

Hence the **full** projection menu of this explicit 44-point child cannot
realize the formal \(W\le2qH\) three-role ramp. This is an exact finite
spectrum-surplus theorem, not sampling evidence.

For the explicit 134-point parent, 512 proposed directions give 448 exact
half-turn orders and 894 distinct profiles. Its sampled lower Pareto menu
has 102 profiles and

\[
 c_-=1118689,\qquad c_+=355504811,\qquad S=1.1745277438\ldots
                                                               \tag{6}
\]

An exact Pareto-state DP over independently recharted sibling copies finds
the values in Table 1. The minimum rebounds from the three-role value and
rises rapidly from \(q=4\) onward. This confirms that the sampled scalar menu
does not contain a long coherent ramp. Because the 134-point projection
spectrum is only sampled, (6) and Table 1 are finite evidence, not a theorem
about its unsampled full menu.

## 1. Exact spectrum-width lemma

### Theorem 1 (first--last spectrum gate)

Let \(X\) be a \(D\)-point planar configuration with \(H=V(X)\). Let

\[
                         \mathcal M\subset\mathbb N^2
\]

be any menu of attainable cap--cup profiles of \(X\), measured in the chart
in which a copy is inserted. Remove a profile if another profile has both
coordinates no larger, and define \(c_-,c_+\) by (1). Take \(q\) disjoint
physical copies of \(X\), allow each copy to choose an arbitrary profile in
\(\mathcal M\), and combine the copies by an ordered linear strong glue.
Then its ordinary face count \(W_q\) obeys (2).

#### Proof

The exact first-cap/last-cup recurrence contains the nonnegative summand

\[
             C_0U_{q-1}(D+1)^{q-2}.                         \tag{7}
\]

For every planar configuration, the standard first/last hull-edge encoding
injects each nonempty ordinary face into a cap--cup pair, so

\[
                         C U\ge H.                           \tag{8}
\]

In particular \(U_{q-1}\ge H/C_{q-1}\). Since
\(C_0\ge c_-\) and \(C_{q-1}\le c_+\), (7) is at least

\[
 H\frac{c_-}{c_+}(D+1)^{q-2}=H(D+1)^{q-2-S}.
\]

All other recurrence terms are nonnegative. This proves (2), and comparing
it with \(KqH\) gives (3). \(\square\)

Coordinatewise Pareto pruning loses nothing when minimizing a future linear
strong-glue recurrence: every occurrence of \(C\) or \(U\) has a
nonnegative coefficient. Notice also that the \(q\) copies are genuinely
independent siblings. The theorem imposes no spurious same-generation
cross-ratio or common-chart constraint.

## 2. Relation to the formal few-run ramp

The exact macro-run recurrence in
`ITERATED_FEW_RUN_LOAD_PROFILE_GATE.md` is

\[
 W_{\rm lin}=\sum_iH_i+
 \sum_{i<j}C_iU_j(D+1)^{j-i-1}.                             \tag{9}
\]

Its algebraic regression chooses

\[
 C_i=D^{b+i},\qquad U_i=D^{h-b-i},\qquad H_i=D^h,            \tag{10}
\]

and obtains \(W_{\rm lin}\le2qH\) when \(D\gg q^2\). The
profiles in (10) have \(C\)-width \(q-1\) powers of \(D\), exactly as
Theorem 1 predicts. More generally, a completed child that exports only
\(S=o(q)\) powers of endpoint width cannot be recycled into this ramp.

An association warning is essential here. The two product-weighted marginal
formulas do not occur simultaneously in one actual comb chart. For the
right-associated comb \(X_0\prec(X_1\prec\cdots)\), equivalently the direct
macro-parabola law, the simultaneous counts are

\[
 C^{\rm R}=\sum_{i=0}^{q-1}\{1+(q-1-i)D\}C_i,\qquad
 U^{\rm R}=\sum_{i=0}^{q-1}(D+1)^iU_i.                     \tag{11}
\]

For the left-associated comb \(((X_0\prec X_1)\prec\cdots)\), they are

\[
 C^{\rm L}=\sum_{i=0}^{q-1}(D+1)^{q-1-i}C_i,\qquad
 U^{\rm L}=\sum_{i=0}^{q-1}\{1+iD\}U_i.                   \tag{12}
\]

The tempting pair consisting of the product-weighted \(C^{\rm L}\) and
product-weighted \(U^{\rm R}\) mixes opposite associations and is not an
actual profile. In particular, there is no valid identity
\(U_*=D C_*\) for a single assembly chart. The earlier version of this note
incorrectly asserted that identity; it is retracted.

The correct assembly conclusion goes in the opposite direction. Substituting
the ramp (10) into either (11) or (12) gives

\[
       \log_D\frac{C^{\rm R}U^{\rm R}}{W_{\rm lin}}
       =\log_D\frac{C^{\rm L}U^{\rm L}}{W_{\rm lin}}
       =q-1+O(1/\log D).                                   \tag{13}
\]

Thus the assembly chart has a large endpoint-product surplus. Recursive
survival requires a genuinely different exported chamber where this surplus
drops by roughly \(q\) powers of \(D\), together with the required graded
imbalance. The exact derivation and the two-chart seam-jet Bellman state are
in `COHERENT_RAMP_TWO_CHART_BELLMAN_GATE.md`.

This does not yet prove an all-scale lower bound. A recursive construction
might complete a parent whose **new** projection spectrum is much wider
than the spectra of its children. A recursively closed decorated menu must
therefore track at least:

1. the attainable lower Pareto profile spectrum of the completed parent;
2. the assembly-to-export gauge needed to realize each chosen profile; and
3. enough parent geometry to recompute the next completed spectrum.

The scalar sibling DP below handles the strongest possible independent
choice from one fixed menu, but deliberately does not pretend that it has
computed the completed parent's next menu. Spectrum width is necessary,
not sufficient.

## 3. Exact sampled-menu Pareto DP

The program `explore_macro_run_profile_dp.cpp` reads the combinatorial input
from `LEVEL4_SAMPLED_SPECTRUM_EVIDENCE.md`. All triple orientations are
certified exactly. For each sampled projection order it computes the exact
\((C,U)\) profile, keeps the lower Pareto menu, and iterates the exact strong
glue recurrences

\[
\begin{aligned}
C(A\prec B)&=C(B)+(1+|B|)C(A),\\
U(A\prec B)&=U(A)+(1+|A|)U(B),\\
W(A\prec B)&=W(A)+W(B)+C(A)U(B).                            \tag{14}
\end{aligned}
\]

It keeps an exact three-coordinate Pareto frontier in \((C,U,W)\), with one
singleton at each end. Every arithmetic operation is integer-exact. The
result for the sampled 134-point child, whose face count is
\(11358202734\), is:

| \(q\) | total points | minimum \(W_q\) | normalized coefficient |
|---:|---:|---:|---:|
| 1 | 136 | 11,389,760,938 | 0.665053 |
| 2 | 270 | 1,275,194,558,068 | 0.616446 |
| 3 | 404 | 204,331,272,672,794 | 0.634138 |
| 4 | 538 | 23,657,227,423,060,068 | 0.660982 |
| 5 | 672 | 3,131,204,364,458,925,600 | 0.696491 |
| 6 | 806 | 422,071,623,348,857,647,279 | 0.735056 |
| 8 | 1074 | 7,691,018,288,124,687,967,888,610 | 0.815439 |
| 12 | 1610 | 2,554,573,464,673,018,000,412,974,458,520,672 | 0.977914 |

The three-role line reproduces the denser sampled level-4 candidate exactly.
For \(q=4\), the minimizing word already needs intermediate profiles

\[
 (1118689,355504811), (2517354,34384089),
 (34384089,2517354), (355504811,1118689),                  \tag{15}
\]

and thereafter the extrema are repeatedly reused. The menu has too little
width to keep the corrected potential flat.

## 4. Scope and remaining construction question

What is now ruled out is a recursively asserted scalar ramp based on a
completed child whose full endpoint menu has bounded width. In particular,
the exhaustive 44-point child fails before a third retained role.

What remains open is sharper and geometric: can an actual recursive planar
wrapper regenerate a completed parent with

\[
 S_{\rm parent}\ge q-2-o(1),\qquad q=\Theta(\log\log n),   \tag{16}
\]

at every relevant level while keeping \(H\) at the formal low-face scale?
The level-4 sampling suggests finite rebound, but cannot exclude rare
unsampled extreme profiles. Proving a direction-spectrum inequality of the
form

\[
 \log_{D+1}(c_+/c_-)\le
 O(1)+\text{face surplus}                                  \tag{17}
\]

would close the coherent scalar ramp. Conversely, a construction must give
exact coordinates and a recursively recomputable decorated spectrum; a
list of favorable one-step profiles is not recursively closed.

## 5. Verification

The theorem, the exact 44-point inequality, and the first six sampled DP
values are checked by

~~~text
python3 phase2/loop/erdos838/agent_root_followup/verify_macro_run_profile_spectrum_width_gate.py \
  --input /tmp/level4_sample512.in
~~~

The input is regenerated exactly as described in
`LEVEL4_SAMPLED_SPECTRUM_EVIDENCE.md`. To display the longer DP table, run

~~~text
clang++ -O3 -std=c++17 \
  phase2/loop/erdos838/agent_root_followup/explore_macro_run_profile_dp.cpp \
  -o /tmp/explore_macro_run_dp
/tmp/explore_macro_run_dp 12 < /tmp/level4_sample512.in
~~~
