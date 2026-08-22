# The selected K2,4 fibre is a three-factor coloured tensor

> **Audit correction.**  The factorized ambient estimate (1.4) below is a
> valid sufficient theorem, but it is quantitatively unsafe: it discards the
> selected physical-centre support.  On transformed Costas 23 its left side
> is `3,031,236`, versus selected mass `204` and
> `k^3+m^2=28,072`.  The live exact gate is the support-restricted tensor
> (1.6), not the ambient product (1.4).  The continuation
> `SWAP_K24_PHYSICAL_OWNER_SUPPORT_NORMAL_FORM.md` proves that this support
> is independent of the cross colour `e`: it is exactly one selected
> physical two-neighbour owner star.  The further continuation
> `SWAP_K24_AMBIENT_OWNER_CORE_SATURATION.md` proves that, above
> `ceil(3t/2)` for dyadic core level `t`, selected-core membership is
> automatic.  The resulting
> ambient support must retain all six owner-cell coordinates; keeping only
> the two incident physical edges is an unnecessarily loose relaxation.

## 1. Outcome

The four-colour key in
`SWAP_SELECTED_CORE_K24_CROSS_SUM_NORMAL_FORM.md` still omitted one
load-bearing part of the optimal-core selection: the four parameter shifts
which must lie in the global adaptive-popular set.  Retaining them gives an
exact three-factor tensor, rather than an arbitrary incidence matrix between
physical gauges and first tracks.

Let `D=(A-A)\{0}` and let `P` be the adaptive-popular shift set used by the
swap graph.  For colours `(a,b,e)` put

\[
\begin{aligned}
 d&=J(b-a-e),\\
 S_e&=\{f:f,f+e\in D\},\\
 Y_{a,b,e}&=\{y:y,y+a,y+d,y+d+b\in D\},\\
 Q_{a,b,e}&=\{q:q,q+a,q-e,q-e+b\in\mathcal P\}.
\end{aligned}                                      \tag{1.1}
\]

For a bare key with first coordinate `z=Z_01`, and for an owner centre whose
first coordinate is `c`, the selected cell load is exactly

\[
\boxed{
 r_{a,b,e}(z,c)
 =|\{f\in S_e:z-Jf\in Y_{a,b,e},\ c-f\in Q_{a,b,e}\}|.} \tag{1.2}
\]

Thus the remaining selected third moment is bounded, up to the four physical
endpoint-role choices, by one explicit coloured tensor.  If

\[
 T_X(h,g)=|X\cap(X-h)\cap(X-g)|,
\]

then

\[
\boxed{
 \sum_{z,c}(r_{a,b,e}(z,c))_3
 =\sum_{\substack{h,g,0\\ \mathrm{pairwise\ distinct}}}
 T_{S_e}(h,g)
 T_{Y_{a,b,e}}(-Jh,-Jg)
 T_{Q_{a,b,e}}(-h,-g).}                          \tag{1.3}
\]

Dropping the physical-centre support gives the sufficient estimate

\[
\boxed{
 \sum_{a,b,e}\ \sum_{\substack{h,g,0\\ \mathrm{pairwise\ distinct}}}
 T_{S_e}(h,g)
 T_{Y_{a,b,e}}(-Jh,-Jg)
 T_{Q_{a,b,e}}(-h,-g)
 \le N^{o(1)}(k^3+m^2).}                         \tag{1.4}
\]

This is sharper than both the bare `K_{2,4}` energy and the arbitrary
gauge-incidence dichotomy, but it still drops one load-bearing factor.
For endpoint roles `epsilon`, let

\[
 \mathcal G_{a,b}^{\epsilon}
 =\{(z,c):\text{an actual selected physical owner has these data}\}.
                                                               \tag{1.5}
\]

Then the exact selected mass is

\[
\boxed{
 C_{\rm center}
 ={1\over2}\sum_{\epsilon,a,b,e}
 \sum_{\substack{h,g,0\\ \mathrm{pairwise\ distinct}}}
 \sum_{\substack{f,f+h,f+g\in S_e\\
                  y,y-Jh,y-Jg\in Y_{a,b,e}\\
                  q,q-h,q-g\in Q_{a,b,e}}}
 1_{\mathcal G_{a,b}^{\epsilon}}(y+Jf,f+q).}    \tag{1.6}
\]

The factor `1/2` converts the falling third factorial to
`3 binom(r,3)`.  Replacing the last indicator by one factorizes the three
inner sums and gives (1.4), up to the harmless four role choices.  Thus the
live theorem is that the right side of (1.6) is
`N^{o(1)}(k^3+m^2)`.  It retains two translated `D`-tracks, four translated
`D`-tracks, four adaptive-popular shifts, and the actual selected physical
centre in the same summand.

## 2. Derivation of the selector

For an owner cell write its centre as `(c,ell)`.  With the notation of the
normal-form note, its two neighbour shifts are `a,b`, and one occurrence has
first track

\[
 f=c-q.                                           \tag{2.1}
\]

The two ordered swap records use parameter pairs

\[
 (q,q+a),\qquad(q-e,q-e+b).                      \tag{2.2}
\]

All four parameters must belong to the adaptive-popular set `P`.  This is
exactly the condition `q in Q_{a,b,e}` in (1.1).  The six moving `D`-forms
are, by the complete-invariant theorem,

\[
 f, f+e, y, y+a, y+d, y+d+b,qquad y=z-Jf. \tag{2.3}
\]

Conditions (2.2)--(2.3) are necessary and sufficient for the two swap
records.  Substituting `q=c-f` proves (1.2).

This also explains the first nonrectangular genuine fibres.  On transformed
Costas 29, a row predicted from only `q,q-e in P` has one extra first track.
For that track `q+a=0`, and zero is excluded from `P`.  Once all four shifts
in (2.2) are retained, the selector is exact.

## 3. The tensor identity

Expand the falling factorial on the left of (1.3).  Choose one base first
track `f` and write the other two as `f+h,f+g`, where
`h,g,0` are pairwise distinct.  The common `z` condition forces the three
positive starts to be

\[
 y,\quad y-Jh,\quad y-Jg,
\]

and the common centre coordinate `c` forces the three popular starts to be

\[
 q,\quad q-h,\quad q-g.
\]

The numbers of possible `f,y,q` are respectively the three factors on the
right of (1.3).  This correspondence is reversible, so (1.3) is an identity.

The colour totals are also lossless:

\[
 \sum_e|S_e|=|D|^2,\qquad
 \sum_{a,b,e}|Y_{a,b,e}|=|D|^4,\qquad
 \sum_{a,b,e}|Q_{a,b,e}|=|\mathcal P|^4.        \tag{3.1}
\]

An ordered pair or quadruple determines its displayed colours uniquely.
Equation (3.1) shows why separating the three factors is too expensive; the
shared colours and the same two translations `(h,g)` are the entire source
of possible compression.

## 4. Relation to the selected physical cells

For fixed endpoint roles, `(a,b,e,z,c)` determines at most one physical
owner.  Indeed `R=z+L b`, then

\[
 V=c+a,\qquad W=R-JV,\qquad \ell=W-Lb.         \tag{4.1}
\]

Distance-Sidonicity recovers the endpoints of the directed edges `V,W`, and
the fixed roles determine their common endpoint.  Therefore summing (1.2)
over actual selected owners is at most four times the unrestricted sum over
`z,c`.  Combining this fact with (1.3) proves that (1.4) is sufficient for
the selected rich-cell Carleson gate.

The unrestricted sum is only an upper envelope, and the loss is already
large on the first nonzero genuine row.  On transformed Costas 23,

\[
 (C_{\rm center},\ \mathfrak T_{\rm ambient},\ k^3+m^2)
 =(204,\ 3{,}031{,}236,\ 28{,}072).              \tag{4.2}
\]

Thus the ambient tensor is `14,858` times the selected mass and `108.0`
times the target.  Its maximum individual `(z,c)` load is only six; the
loss comes from support, not a few rich ambient cells.  On Costas 29, the
eight largest colour factors alone contribute `7,227,048`, already `56.4`
times `k^3+m^2`; the full ambient tensor is larger.  These finite data do
not constitute an asymptotic counterexample to an `N^{o(1)}` estimate, but
they rule out treating (1.4) as a quantitatively faithful closing gate.
The physical contact and chosen nested-core support in (1.6) must remain.

## 5. What remains

The next proof should dyadically decompose the common triple intersections

\[
 T_{S_e}(h,g),\quad T_{Y_{a,b,e}}(-Jh,-Jg),\quad
 T_{Q_{a,b,e}}(-h,-g)                            \tag{5.1}
\]

without separating their colours **or** deleting the support indicator in
(1.6).  A threatening band makes the same
noncollinear parameter triangle simultaneously popular in a two-track
`D` fibre, a four-track quarter-turned `D` fibre, and a four-shift adaptive
fibre, while the base pair `(y+Jf,f+q)` is an actual selected physical
centre.  This is a considerably narrower density-increment object than the
previous physical-wedge tail and avoids the factor-`10^4` support loss seen
in (4.2).

The support in (1.6) is now explicit.  If `C=(c,ell)`, then
`z=ell+J(c+a)` and the two neighbours are

\[
 (c+a,\ell+La),\qquad(c+b,\ell+Lb).
\]

Their physical edges are `c+a` and `ell+Lb`; membership in
`mathcal G^epsilon_{a,b}` says precisely that these edges meet at the
prescribed endpoint roles and that the three cells form an actual selected
owner star.  In particular the support is independent of `e`.  Summing `e`
last recovers the exact cross-third energy between the two parallel-copy
fibres of this owner.

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_k24_adaptive_popular_tensor.py
python3 phase2/loop/erdos1208/verify_swap_k24_physical_owner_support.py
python3 phase2/loop/erdos1208/analyze_swap_optimal_nested_cores.py --k24-prime=23 --k24-tensor
python3 phase2/loop/erdos1208/analyze_swap_optimal_nested_cores.py --k24-prime=29
```

The symbolic verifier checks (1.2)--(1.3), the three colour totals, and an
explicit nonzero tensor.  The genuine analyzer reconstructs all four popular
parameters for every selected row and asserts the selector identity.
