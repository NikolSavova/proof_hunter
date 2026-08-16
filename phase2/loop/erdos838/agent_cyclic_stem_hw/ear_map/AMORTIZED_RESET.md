# Erdős 838: amortized cumulative pocket reset

**Date:** 2026-08-14  
**Verdict:** the cumulative-prefix approach can be reduced exactly to one
scale-free statistic.  That statistic is equivalent, within an absolute
factor, to the rankwise low-addable Hall statistic.  Thus cumulative growth
does not bypass the capped exterior-pocket gate, but it gives a cleaner
amortized potential and removes the need to prove doubling at every rank.

The fixed-frame rectangle defect telescopes rigorously along a coherent
singleton-ear recursion.  The obstruction is also exact: deleting an old
tangent marker breaks coherence, and a product construction incurs
`Theta(r)` bits of projection loss per erased singleton coordinate while a
rank drop pays only one bit.  Batched over an unbalanced chain this is
quadratic, not `O(log r)`.  The known two-ended face pool pays this loss in
product cells; proving that an analogous forward release always occurs
before markers are discarded remains the unresolved geometric lemma.

No solution of Erdős 838 is claimed here.  All logarithms are base two.

## 1. One potential captures the total prefix deficit

Put

\[
 F_k=\sum_{j=0}^k v_j,
 \qquad V=\sum_jv_j,
 \qquad \ell=\lceil\log n\rceil,
\]

and define

\[
 \boxed{
 K_F(P)=\max_{0\le k<\ell}{2^{\ell-k}F_k\over V}.}          \tag{1}
\]

The quantity `log K_F` is the worst accumulated deficit from ideal
factor-two prefix growth between a low rank and the global face pool.  It is
strictly weaker than requiring every adjacent or fixed-block doubling
inequality.

> **Theorem 1 (cumulative envelope implies the mean bound).**
> \[
>  \boxed{
>  \mu(P)\ge
>  \ell-\lceil\log \max\{1,K_F(P)\}\rceil-1.}               \tag{2}
> \]

**Proof.**  If `K` is the rank of a uniform random face, (1) gives

\[
 \Pr(K\le\ell-s)={F_{\ell-s}\over V}
 \le\min\{1,K_F2^{-s}\}.                                  \tag{3}
\]

Summing (3) over `s>=1` bounds `E[(ell-K)_+]` by
`ceil(log max{1,K_F})+1`.  Ranks above `ell` only help.  QED.

Consequently

\[
 K_F\le(\log n)^{O(1)}                                    \tag{4}
\]

already yields `mu>=log n-O(log log n)`.  This is the precise meaning of an
`O(log ell)` total prefix-growth deficit.

There is an equivalent adjacent-deficit description.  If

\[
 a_j=\log{F_{j+1}\over F_j},\qquad d_j=(1-a_j)_+,
\]

then for every `q`

\[
 {F_{k-q}\over F_k}
 \le2^{-q+\sum_{j=k-q}^{k-1}d_j}.                         \tag{5}
\]

Thus a bound `sum d_j<=s` implies the same tail conclusion with loss
`s+O(1)`.  Formula (1) is preferable because surplus growth and mass above
`ell` are automatically credited rather than discarded rank by rank.

## 2. Exact equivalence with low-addable rankwise Hall

For a constant `C`, let

\[
 N_r^{(C)}=
 |\{A:|A|=r,\ A\text{ convex},\ u(A)\le C(r+1)\}|,
\]

and

\[
 K_u^{(C)}=\max_{r<\ell}{2^{\ell-r}N_r^{(C)}\over V}.       \tag{6}
\]

> **Theorem 2 (prefix peak produces a low-addable slice).**
> For every planar point set,
> \[
>  \boxed{
>  K_u^{(24)}\le K_F
>  \le\max\left\{2,{24\over5}K_u^{(24)}\right\}.}          \tag{7}
> \]

**Proof.**  The first inequality is immediate from `N_r^(24)<=v_r<=F_r`.
Suppose `K_F>2`, and choose a maximizing rank `k` in (1).  The ranks
`k=0,1,2` each give a value at most two, using `2^ell<=2n` and the complete
rank-three skeleton.  The rank `ell-1` also gives at most two.  Hence

\[
 3\le k\le\ell-2.                                          \tag{8}
\]

Maximality at ranks `k-3` and `k+1` gives

\[
 F_{k-3}\le F_k/8,\qquad F_{k+1}\le2F_k.                  \tag{9}
\]

Summing the exact cover identity through rank `k`,

\[
 \sum_{r=0}^k\sum_{|A|=r}u(A)
 =\sum_{s=1}^{k+1}s v_s
 \le(k+1)F_{k+1}\le2(k+1)F_k.                            \tag{10}
\]

At most `F_k/4` faces have `u(A)>8(k+1)`.  At least `7F_k/8`
faces have ranks `k-2,k-1,k`.  Their intersection therefore contains at
least `5F_k/8` faces, so some rank `r in {k-2,k-1,k}` contains at least

\[
 M\ge{5F_k\over24}                                        \tag{11}
\]

of them.  Since `8(k+1)<=24(r+1)`, these faces are counted by
`N_r^(24)`.  Finally

\[
 K_u^{(24)}
 \ge {2^{\ell-r}M\over V}
 \ge {5\over24}{2^{\ell-k}F_k\over V}
 ={5\over24}K_F.                                          \tag{12}
\]

This proves (7).  QED.

The constants are deliberately unoptimized.  The point is structural:
bounding total cumulative deficit is the same problem as bounding one
near-maximal rank slice.  In particular the cumulative route is not a new
escape from RNP; it is an exact repackaging of it.

There are three scope caveats.  First, the exact statement is for threshold
`24(r+1)`, not the earlier RNP threshold `4(r+1)`; no reverse comparison
between those two low-addable families is asserted.  Second, when `K_F<=2`
the right side of (7) is discharged by the constant branch and need not
produce a distinguished slice.  Third, Theorem 2 is exact, but the next
paragraph's use of the optimized exterior-label theorem at threshold 24
requires the routine constant-threshold rerun of that theorem's estimates;
that rerun is not reproduced line by line here.  These qualifications do
not affect the asymptotic target, but they matter if (7) is quoted as an
exact RNP equivalence.

### Interface with optimized exterior-label supply

At the maximizing prefix, (11) gives a rank-`r` family of size comparable
to `F_k`.  The optimized hull-activity tail theorem applies unchanged when
the low-addable threshold is multiplied by an absolute constant.  Its
low-exterior-label part already obeys (7).  Every residual source has

\[
 D_r/n^{o(1)}\quad\text{selected exterior blockers},
 \qquad D_r=2^{\ell-r}.                                    \tag{13}
\]

Because `r>=k-2`, (11) and (1) give

\[
 {M D_r\over V}\ge {5\over24}K_F.                         \tag{14}
\]

The constant-two ear theorem maps the selected incidences to at least

\[
 {K_F V\over n^{o(1)}}                                    \tag{15}
\]

distinct compatible pairs `(I,B)`, up to an absolute factor.  Therefore a
`poly(ell)V` upper capacity for the **selected compatible-pair system** would
prove (4).  The old root-multiplicity loss has disappeared; only conversion
of a pair into globally reusable one-face capacity remains.

## 3. Fixed-frame rectangle defect

Fix a root `p`, tangent endpoints `x,y`, hidden size, and source rank.  For a
source subfamily `S_f`, let `X_f` and `Y_f` be the hidden and retained
projection families.  The fixed-frame rectangle theorem proves that every
cross-union is a distinct convex face, hence

\[
 |S_f|\le|X_f||Y_f|\le v_r.                               \tag{16}
\]

Define its Hartley rectangle defect

\[
 \delta_f=\log{|X_f||Y_f|\over|S_f|}\ge0.                 \tag{17}
\]

If `delta_f>=g`, rectangle completion supplies a factor `2^g` of genuine
rank-preserving capacity inside that frame.  A dense frame has small
`delta_f` and must be continued recursively.

The defects telescope exactly as long as earlier tangent markers survive.

> **Lemma 3 (coherent rectangle chain).**  Suppose families
> `S_0,...,S_h` and disjoint coordinate pools `Q_1,...,Q_h` satisfy
> \[
>  S_{j-1}\subseteq Q_j\times S_j,qquad
>  \delta_j=\log{|Q_j||S_j|\over|S_{j-1}|}.                 \tag{18}
> \]
> Assume every descendant rectangle completion remains a valid retained
> face for every ancestor frame, with its coordinates recoverable.  Then
> the recursion produces
> \[
>  T_0=|S_0|\,2^{\delta_1+\cdots+\delta_h}                 \tag{19}
> \]
> distinct convex faces.

**Proof.**  Put `T_h=|S_h|`.  Coherence permits every member of `Q_j` to be
glued to every one of the `T_j` completed descendants, and recoverability
makes the unions distinct.  Thus `T_(j-1)=|Q_j|T_j`.  Multiplying (18)
telescopes to (19).  QED.

This gives a rigorous scalar potential:

\[
 \Delta(\text{history})=\sum_j\delta_j.                    \tag{20}
\]

A history with `Delta>=log K_F` is discharged by its own rectangle
completion.  The difficult histories have dense projection relations at
almost every step.

The tangent endpoints need not be pigeonholed after the root is fixed.

> **Lemma 4 (aggregate fixed-root rectangle bound).**  Fix a root `p` and
> source rank `r`.  Partition any family of `p`-blocked sources into frames
> `f` by tangent pair and hidden size.  Put
> \[
>  e_f=|S_f|,\qquad T_f=|X_f||Y_f|,
>  \qquad\delta_f=\log(T_f/e_f).
> \]
> Then
> \[
>  \boxed{\sum_fT_f\le v_r.}                               \tag{FR}
> \]
> Consequently, for every `sigma>=0`,
> \[
>  \boxed{
>  \sum_{f:\delta_f\ge\sigma}e_f
>  \le2^{-\sigma}v_r.}                                    \tag{FR-tail}
> \]

**Proof.**  Every rectangle completion `C=I union R` is a convex rank-`r`
face.  Moreover, adding the fixed root recovers the repair exactly:

\[
 \operatorname{ext}(C+p)=R+p,
 \qquad C-\operatorname{ext}(C+p)=I.                      \tag{recover}
\]

Indeed, `R+p` is the repaired convex hull and every point of `I` lies
strictly inside its ear triangle `pxy`; hence adjoining `I` does not alter
that hull.  Therefore `C` and `p` recover `I`, `R`, the two neighbours
`x,y` of `p` on the hull, and the hidden size.  Completed rectangles from
different fixed-`p` frames are disjoint.  Their union is a subfamily of the
rank-`r` faces, proving (FR).  On frames with defect at least `sigma`,
`e_f=T_f2^(-delta_f)<=2^(-sigma)T_f`; sum and use (FR).  QED.

This removes endpoint bookkeeping entirely after the root is fixed.  It
also gives a sharp density tail: after fixing one root, only
`2^(-sigma)v_r` sources can lie in frames whose rectangle completion gains
`sigma` bits.  The root itself still costs `log n` bits, and dense
unbalanced frames remain the hard case.

## 4. Why coherence fails: the marker-deletion gate

The gluing proof for an ancestor frame uses its two tangent endpoints.  A
deeper ear replacement may delete one of them.  The resulting completed
descendant is then no longer in the ancestor's retained pool, so the
induction `T_(j-1)=|Q_j|T_j` is invalid.  This is not a formal nuisance.

The exact two-deep-endpoint wrapper proves that no positive power of a
pocket's span can be paid by faces required to retain either old marker.
The compensating `2^M` faces abandon both.  Consequently, augmenting (20)
by a fixed reward for preserving one endpoint cannot yield a universal
telescoping potential.  A successful reset must allow both markers to be
dropped while carrying a replacement two-ended state.

There is a convenient abstract flow statement for the required accounting.

> **Lemma 5 (log-loss flow tree).**  Consider a recursive routing tree.  On
> an edge `e`, suppose normalized demand can increase by a factor `lambda_e`
> because of projection fibre divided by rank credit.  Suppose target pools
> used at leaves have overlap at most `R`.  If every root-to-leaf path obeys
> \[
>  \sum_{e\text{ on path}}\log\lambda_e\le s,               \tag{21}
> \]
> then the full routing has congestion at most `R2^s`.

**Proof.**  Push one unit of root demand down the tree.  Along a path its
possible inverse load is multiplied by at most the product of the
`lambda_e`, which is at most `2^s`.  At a leaf, at most `R` pools reuse one
target.  Sum over the disjoint routing branches.  QED.

Thus the hoped-for amortized theorem is exactly `s=O(log ell)` with
`R=poly(ell)`.  Lemma 3 pays part of the recursion through rectangle release.  The
remaining question is whether every marker-deleting step either has small
normalized fibre or releases a forward two-ended pool before such losses
accumulate.

## 5. Exact obstruction from an unbalanced singleton chain

The product-grid regression gives the sharp audit.  Let `s` disjoint
singleton windows each contain a source choice among `M-1` points.  Replacing
all chosen coordinates by fixed blockers sends

\[
 (M-1)^s                                                   \tag{22}
\]

sources to one target.  A descent of `s` ranks would permit only the credit
`2^s`; a rank-preserving switch permits even less.  Hence the normalized
loss is at least

\[
 \lambda={ (M-1)^s\over2^s},\qquad
 \log\lambda=s(\log(M-1)-1).                               \tag{23}
\]

At `M=2^r`,

\[
 \log\lambda\ge s(r-2).                                   \tag{24}
\]

For one batch `s=sqrt(r)` this is `Theta(r^(3/2))`; repeating the batch down
a linear singleton chain reaches `Theta(r^2)`, not `O(log r)`.  Moreover the
source relations in the independent cells are full products, so every local
rectangle defect is zero.  A scalar potential using only rank drop and
rectangle density therefore cannot see the loss.

The finite rational instance has `r=8`, `M=3`, three disjoint windows, and
inverse fibre eight.  The scalable formula (22) is exact for every `M`.

This obstruction is not a counterexample to the desired Hall theorem.  Its
missing capacity is the exact two-ended family

\[
 \binom M2^2M^{r-4}.                                      \tag{25}
\]

Thus (23) identifies the term which a correct potential must debit, while
(25) identifies the forward cap--cup credit which pays it in a product
cell.  The unresolved general theorem is precisely that comparable credit
is released across arbitrary crossing tangent pockets before the losses in
(21) become quadratic.

## 6. What has and has not been reduced

The amortized route now has a short rigorous skeleton.

1. `log K_F` is the total prefix deficit and directly controls the mean.
2. A large `K_F` creates one constant-density, near-top low-addable slice.
3. Optimized hull activity gives the required capped exterior labels.
4. The constant-two ear map turns them into compatible pairs without a
   rank factor.
5. Sparse fixed frames release rectangle capacity exactly; after fixing the
   root their completed rectangles are disjoint across tangent frames.
6. Coherent dense singleton chains telescope by Lemma 3.

The only surviving branch consists of dense frames whose recursion deletes
old tangent markers.  Lemma 5 shows the exact required bound; (23) proves
that small rank loss or endpoint bookkeeping cannot establish it.  A full
proof needs a universal forward two-ended release inequality that dominates
the accumulated normalized fibres.  This is the same forward-alignment gate
found independently by the interval-batching and product-cell attacks, now
derived from the cumulative-prefix potential rather than assumed.

## 7. Verification

Run

```bash
python3 \
  phase2/loop/erdos838/agent_cyclic_stem_hw/ear_map/verify_amortized_reset.py
python3 \
  phase2/loop/erdos838/agent_cyclic_stem_hw/ear_map/verify_ear_map.py
```

It writes `amortized_reset_certificate.json` and checks:

* the exact cumulative envelope on the 17-point crossing configuration;
* the cover identity and the low-addable top-three-rank slice using integral
  geometry;
* the cumulative envelope on all 60 deduplicated saved profiles; and
* the exact finite product fibre together with the scalable loss formula
  (23); and
* on an exact 14-point configuration, disjointness of completed rectangles
  across all fixed-root frames, and hence (FR), in addition to every
  individual cross completion.

Theorems 1--2 and Lemmas 3--4 are symbolic; the finite computations are
regressions, not substitutes for their proofs.
