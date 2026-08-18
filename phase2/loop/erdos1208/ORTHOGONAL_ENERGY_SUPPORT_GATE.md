# The orthogonal energy--support gate

## 1. Status and exact implication

Let `A` be distance-Sidon, put

\[
 D=A-A,\qquad N=|D|=|A|(|A|-1)+1,
\]

and let `J(x,y)=(-y,x)`.  Write

\[
 S=|D+D|,\qquad T=|D+JD|.                       \tag{1.1}
\]

For `q in D-D`, define

\[
 R_D(q)=|\{(x,y)\in D^2:y-x=q\}|,
\]

and introduce the common orthogonal energy

\[
 \mathcal E_\perp(D)=\sum_qR_D(q)R_D(Jq).        \tag{1.2}
\]

This gives a new scale-perfect sufficient theorem for the full cube-root
upper bound:

\[
 \boxed{\mathcal E_\perp(D)\le N^{1+o(1)}S.}     \tag{1.3}
\]

Indeed, if

\[
 r(t)=|\{(d,e)\in D^2:d+Je=t\}|,
\]

then `sum_t r(t)=N^2`, `supp(r)=D+JD`, and expanding a collision gives

\[
 \sum_t r(t)^2=\mathcal E_\perp(D).              \tag{1.4}
\]

Cauchy--Schwarz therefore yields

\[
 T\ge {N^4\over\mathcal E_\perp(D)}.             \tag{1.5}
\]

Under (1.3), equations (1.1) and (1.5) give

\[
 ST\ge N^{3-o(1)}.                               \tag{1.6}
\]

This is precisely the orthogonal two-support gate.  For
`A subset [m]^2`, both supports are `O(m^2)`, so (1.6) implies

\[
 |A|\le m^{2/3+o(1)},\qquad F_2(n)\le n^{1/3+o(1)}. \tag{1.7}
\]

Estimate (1.3) is not proved.  It is a global density-sensitive replacement
for every maximum-row theorem killed so far.

## 2. Why this energy was previously dismissed too quickly

The same quantity appeared in `TRANSVERSE_SPECTRAL_AUDIT.md` after deleting
the fifth, restricted incidence from the row moment.  On the closure chain it
grows on the `k^5` scale, one power above the `k^4` estimate needed by that
earlier route.  That does **not** contradict (1.3), because the ordinary
support `S=|D+D|` grows well above the quadratic scale on the same examples.

The exact closure profiles are:

\[
\begin{array}{c|r|r|r|c}
k&N&S&\mathcal E_\perp&\mathcal E_\perp/(NS)\\ \hline
20&381&16,097&1,735,609&0.282997\ldots\\
30&871&62,273&16,135,769&0.297489\ldots\\
40&1,561&156,057&76,060,041&0.312226\ldots\\
50&2,451&334,555&231,533,961&0.282360\ldots\\
60&3,541&619,209&581,578,857&0.265243\ldots\\
70&4,831&996,133&1,344,282,105&0.279341\ldots
\end{array}                                      \tag{2.1}
\]

The transformed finite-field parabola at `p=31` has ratio
`0.095204...`; the dense perpendicular-ruler example at `k=40` has ratio
`0.026394...`.  Thus the family which killed the mixed third moment

\[
 \sum_qR_D(q)^2R_D(Jq)
\]

does not threaten (1.3).  Removing one factor of `R_D(q)` and paying for the
ordinary support is exactly the needed change of scale.

## 3. What structure (1.3) must use

The inequality is false for an arbitrary centrally symmetric radially unique
set `D`.  In fact `RADIAL_ORTHOGONAL_PRODUCT_BARRIER.md` proves the stronger
statement that the final product theorem itself is false in that class.
Choosing one representative of every sum-of-two-squares norm in a large
square and adjoining its negative gives `D cap JD={0}` and

\[
 |D+D|\,|D+JD|=|D|^{2+o(1)}.
\]

Thus neither radial uniqueness nor the two-support formulation can replace
the complete-difference hypothesis.

The load-bearing additional fact is

\[
 D=A-A,qquad |D|=|A|(|A|-1)+1,                  \tag{3.1}
\]

so every nonzero vector has one ordered endpoint decoration and all cross
differences between those endpoints are also present in `D`.  Equivalently,
the weighted indicator

\[
 |A|\,1_{\{0\}}+1_{D\setminus\{0\}}
\]

is an autocorrelation and hence has nonnegative Fourier transform.  Neither
radial uniqueness nor `D cap JD={0}` alone is sufficient.

At the opposite extreme, if generic independent segment translations create
a concentrated row, they also make `S` essentially maximal, so (1.3) becomes
close to the universal energy bound `E_perp<=N^3`.  A proof must formalize
this compensation: high common energy is allowed, but only when it creates
enough ordinary support.

There is now one rigorous structured branch of this compensation.
`ORTHOGONAL_PRODUCT_PARALLEL_COVER.md` proves directly that if `A` is covered
by `r` parallel lines, then

\[
 |D+D|\,|D+JD|\gg {N^3\over r^2}.               \tag{3.2}
\]

Thus the full product theorem holds whenever `r=N^{o(1)}`.  Its proof uses
the complete difference set essentially: all within-line differences form a
set `H subset D`, and translating **all of `D`** by `JH` gives
`|D+JD|>=|H|^2`.  This is the model for the global charging still missing in
the wide case.

## 4. A pointwise strengthening is false by a full power

It is tempting to prove (1.3) termwise from

\[
 R_D(q)R_D(Jq)\le N^{1+o(1)}.                   \tag{4.1}
\]

This is false; the summation and its support budget are essential.

Let `p` be prime and take the integer finite-field parabola

\[
 P_p=\{(x,x^2\bmod p):0\le x<p\}.               \tag{4.2}
\]

It is vector-Sidon.  Put `C=P_p+P_p`, with unordered sums.  On a fixed
integer first-coordinate line, `C` has `Theta(p)` points for `Theta(p)`
different lines.  Hence

\[
 \sum_h R_C((0,h))=\Theta(p^3).                 \tag{4.3}
\]

The zero shift contributes only `|C|=Theta(p^2)`, and there are `O(p)`
possible vertical shifts.  Thus some nonzero vertical

\[
 q_p=(0,h_p)
\]

satisfies

\[
 R_C(q_p)=\Omega(p^2).                           \tag{4.4}
\]

No nonzero vertical vector lies in `P_p-P_p`, since the first coordinates
of `P_p` are distinct.

Every translated pair of decorated sums in (4.4) gives

\[
 q_p=(a-c)+(b-d),qquad a,b,c,d\in P_p,           \tag{4.5}
\]

and vector-Sidonicity makes this map bounded-to-one (indeed injective after
fixing canonical unordered decorations).  Therefore

\[
 R_{P_p-P_p}(q_p)=\Omega(p^2).                   \tag{4.6}
\]

Take two copies of `P_p`.  Choose generic rational invertible maps `L_1,L_2`
subject only to

\[
 L_2q_p=JL_1q_p.                                 \tag{4.7}
\]

The maps may be chosen so that both copies have distinct internal distances
and their two internal distance spectra are disjoint.  To see that no
equality is forced by (4.7), vary the image of a vector complementary to
`q_p`; no nonzero edge of `P_p` is parallel to `q_p`.  A further generic
translation separates all cross distances.  Avoiding the finitely many
proper polynomial loci gives a rational, and after scaling integral,
distance-Sidon union `A_p` of `2p` points.

With `Q=L_1q_p`, its complete difference set satisfies

\[
 R_D(Q)R_D(JQ)=\Omega(p^4)=\Omega(N^2),          \tag{4.8}
\]

the largest possible power scale.  This does not contradict (1.3): one or a
few `N^2` peaks fit inside the budget `NS`, since always `S>=N`.

The exact verifier gives a 46-point integral example from `p=23` with

\[
 N=2,071,\quad R_D(Q)=R_D(JQ)=252,\quad
 R_D(Q)R_D(JQ)=63,504.                           \tag{4.9}
\]

Its global values are

\[
 S=608,903,\qquad \mathcal E_\perp=7,263,825,
 \qquad {\mathcal E_\perp\over NS}=0.005760\ldots . \tag{4.10}
\]

## 5. Correct restart point

The live theorem is the global energy--support inequality (1.3), or directly
the product inequality (1.6).  The exact missing statement can be phrased as
a tail estimate for the bidirectionally popular sums of `D`:

\[
 \sum_q R_D(q)R_D(Jq)
 \le N^{1+o(1)}|\operatorname{supp}(1_D*1_D)|.   \tag{5.1}
\]

Any proof must allow isolated quadratic peaks such as Section 4 and charge
them to support created elsewhere.  Maximum-row, maximum-translation, and
termwise Fourier estimates are all too strong.  Plausible mechanisms are:

1. a dyadic popular-sum decomposition in which a high orthogonal pair of
   fibres forces many new sums through their uniquely decorated endpoints;
2. a positivity argument using that the weighted indicator of `D` is the
   autocorrelation of `A`; or
3. an inverse theorem: simultaneous common energy and small `D+D` force a
   quarter-turn-stable rank-two model, whose endpoint decoration then creates
   a repeated Euclidean norm.

No existing generic common-energy theorem located in the literature includes
the complete-difference/radial constraint needed for (5.1).

There is now a useful unconditional restriction on where (5.1) is needed.
`ORTHOGONAL_RUZSA_HIGH_SUPPORT_BRANCH.md` proves

\[
 |D+JD|^2\ge N|D+D|.
\]

Consequently the full product theorem already holds if
`|D+D|>=N^(5/3-o(1))`.  The energy--support attack may therefore assume from
the outset that `D` has doubling below `N^(2/3-o(1))`, in addition to being
outside the subpolynomial parallel-cover branch.

There is now a more endpoint-aware organization of the same residual.
`ORTHOGONAL_SWITCHING_RICH_TAIL_GATE.md` assigns every collision in (1.2)
to its longest decorated edge and the ordinary sum of the opposite
representation.  A second-moment bound for these switching loads implies
(5.1) by Cauchy.  Crucially, the corresponding maximum-load statement is
false by the largest possible power: a generic complete-bipartite gadget
gives a distance-Sidon set with one switching fibre of size `Omega(N)`.
The exact 18-point certificate has a fibre of 32 ordered collisions.  Thus
resume with an averaged rich-tail or multi-corner load-balancing theorem,
not a pointwise switching injection.

The same note derives a cleaner preferred map with no selector:
`(x,y,u,v)->(u,x+y)`.  Its second moment has the exact seven-incidence
expansion (1.8) there and is only `0.48509... N|D+D|` on the 20-point
closure.  Do not discard the seventh condition `u in D`; the resulting raw
`(I+J)`-dilation moment already fails by a factor greater than 88 on the
transformed parabola.

The selector-free moment's diagonal and all subpolynomial fibres can be
absorbed.  Its canonical endpoint-midpoint charge is nevertheless false
without a support hypothesis: `ENDPOINT_MIDPOINT_SIDON_RULER_BARRIER.md`
constructs a heavy fibre with average charge load `Omega(N)`.  The same
family forces `|D+D|=Omega(N^2)`, so it is already in the Ruzsa high-support
branch.  Any continuation must prove a support-compensated rich-tail
dichotomy in the live low-support regime.

The following briefly proposed global sufficient condition is false.  If it
held,

\[
 \mathcal E_+(D)\mathcal E_\perp(D)\le N^{5+o(1)},
\]

then Cauchy's lower bound
`E_+(D)>=N^4/|D+D|` gives the present energy--support gate immediately.
However `ORTHOGONAL_ENERGY_PRODUCT_RULER_BARRIER.md` constructs integral
distance-Sidon sets with both factors `Omega(N^3)`, so their product is
`Omega(N^6)`.  Ordinary energy does not distinguish small ordinary support
from a dense structured component inside a set having nearly maximal
support.  The present support-sensitive inequality and the support-compensated
switching expansion remain the live targets.

There is now an exact support-adaptive localization of the live target.  Put
`K=|D+D|/N` and retain only nonzero shifts satisfying both
`R_D(q)>K` and `R_D(Jq)>K`.  The zero shift and the two complementary low
parts contribute at most `3N|D+D|` in total, so it is enough to prove

\[
 \sum_{\substack{q\ne0\\R_D(q)>K,\ R_D(Jq)>K}}
 R_D(q)R_D(Jq)\le N^{1+o(1)}|D+D|.
\]

Read `SUPPORT_ADAPTIVE_POPULAR_OVERLAP_GATE.md`.  Its exact verifier shows
that this nonzero tail is empty on the ruler, parabola, and quadratic-fibre
obstructions, is below `0.007N|D+D|` on the stored closure chain, and grows
past `16N|D+D|` on the abstract radial transversals.  This is the current
sharpest restart point.
