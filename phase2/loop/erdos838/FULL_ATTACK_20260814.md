# Erdős 838: full-attack state, 2026-08-14

This note is the current proof state for the unrestricted problem.  It is
deliberately sharper than a chronological log: every displayed implication is
either proved in the referenced artifact or explicitly labelled as a target.
All logarithms in asymptotic coefficients are base two unless stated
otherwise.  Convex subsets include the empty set; changing this convention is
asymptotically irrelevant.

## 1. Banked theorem and exact remaining gap

For

\[
 f(n)=\min_{|P|=n}\#\{A\subseteq P:A\text{ is in convex position}\},
\]

the current rigorous window is

\[
 \frac14\leq\liminf_{n\to\infty}
 \frac{\log f(n)}{(\log n)^2}
 \leq\limsup_{n\to\infty}
 \frac{\log f(n)}{(\log n)^2}\leq\frac12.       \tag{1}
\]

The upper bound is an explicit iterated directional blow-up.  Its exact
cap/cup/convex-subset recurrences are verified geometrically and with rational
coordinates.  The lower coefficient `1/2` is also proved for every recursively
mirror-decomposable point set, with error `O((log n)^(3/2))`, and is sharp in
that class.  See `paper/main.tex` and the endpoint-reset audits.

Thus a complete solution at the expected constant is now exactly the
unrestricted lower bound

\[
 \log f(n)\geq\left(\frac12-o(1)\right)(\log n)^2.          \tag{2}
\]

The construction-side escape has also narrowed.  For a macroscopic
heterogeneous vertical composition with a macro-large induced core, child
coefficient `c`, logarithmic macro/child proportions `alpha,beta`, balanced
cap/cup endpoints, and no macro count or mean loss, the exact support
calculus gives

\[
 c_{\rm out}\ge c+(1-2c)\alpha\beta.                         \tag{2a}
\]

Thus every comparable macroscopic regeneration strictly raises a coefficient
`c<1/2`.  A sub-half construction must sustain quadratic directional skew,
low local convex mass, and coloured macro support avoiding every same-skew
induced core (or else suffer a linear macro-mean deficit).  Canonical
Baek--Balko cells and all saved heterogeneous macros fail this test; no
sub-half construction is currently known.  The exact theorem and its
stress tests are in `agent_upper_jump/REPORT.md`.

For a fixed putative gap, say
`log V(P)<=(1/2-delta)(log n)^2`, the structural target is quantitatively
weaker than near-spanning regularization but still well beyond every known
extraction theorem.  The audited strong-tree theorem shows that it would
suffice to extract a mirror-decomposable subset of size `n^(alpha+o(1))`
for some

\[
                         \alpha>\sqrt{1-2\delta}.       \tag{2b}
\]

Conversely any counterexample must have no such extraction.  This remains
true after adjoining three generic enclosing vertices: the resulting set
has a triangular outer hull and one prime canonical module, while its
convex count changes by at most a factor eight and its largest structured
subset by at most three points.  Thus low-count regularization cannot be
reduced to finding a nontrivial top modular split.  Homogeneous vertical
towers are narrower still: a fixed gap forces a macroscopic template mesh
at least
`(3-sqrt(9-8delta))/2`.  These results are proved in
`agent_all_interval_isoperimetry/LOW_V_FIXED_GAP.md`; they remove false
regularization goals but do not provide (2b).

## 2. Two equivalent full-strength targets

Write

\[
 Z_P(t)=\sum_{A\text{ convex}}t^{|A|},\qquad
 H(P)=\frac{nZ_P(1/2)}{Z_P(1)}.                              \tag{3}
\]

If `H(P)=n^o(1)` for every point set (the tested finite strengthening is
`H(P)<=2`), then convex-subset mean size is at least
`(1-o(1))log n`.  Applying the exact deletion identity to a minimizer proves
(2).  This is the **half-weight target**.

There is now a minimizer-only reduction which bypasses a universal
half-weight estimate.  Let `mu` be the mean face rank, `R` the largest face
rank, and

\[
  \Delta=\max_{|T|=3}|\{p:T\cup\{p\}\text{ is nonconvex}\}|.
\]

For every planar configuration,

\[
                  \boxed{\displaystyle
                  \mu\ge {n\over2+\Delta(R-2)}.}          \tag{3a}
\]

Indeed the exact cover balance gives `E b(A)=n-2mu`, where `b(A)` is the
number of non-addable labels over a uniform face.  A rank-`h` face has a
canonical family of at most `h(h-2)` witnessing triples: a fan
triangulation covers interior labels, while a tangent endpoint, the first
hidden neighbor, and the opposite tangent endpoint cover every blocked
exterior label.  Averaging `b(A)<=Delta H(H-2)` proves (3a).

For a minimizer the construction upper bound gives
`R<=(1/2+o(1))(log n)^2`.  Hence, for fixed `epsilon>0`,

\[
 \mu\le(1-\epsilon)\log n
 \quad\Longrightarrow\quad
 \Delta\ge\left({2\over1-\epsilon}-o(1)\right)
                  {n\over(\log n)^3}.                    \tag{3b}
\]

Thus the minimizer mean route is complete unless one triple supports an
almost-linear circuit star.  Pigeonholing the interior role leaves either a
common triangle pocket or a common exterior root cone on
`Omega(n/log^3 n)` labels.  The remaining step is again a marked
one-pocket/shield allocation theorem: a triangle containing `m` labels
contributes only one closed set but Boolean hull-partition weight `2^m`, so
the unrestricted pocket bank cannot simply be changed into the uniform
face law.  See
`agent_outer_internal_product/MINIMIZER_CIRCUIT_CODEGREE_DICHOTOMY.md`.

The obstruction is weighted, not merely one exceptional triple.  For the
canonical tangent triples let `d(T)` be circuit degree and `w(T)` the number
of source faces whose canonical cover uses `T`.  With

\[
 D_0={n-2\mu\over(R-2)\mu},\qquad
 \mathcal H=\{T:d(T)\ge D_0/2\},
\]

one has

\[
 \sum_{T\in\mathcal H}w(T)
     \ge {V(n-2\mu)\over2(n-3)},                         \tag{3c}
\]

and at least

\[
        {V(n-2\mu)\over2(n-3)R(R-2)}                    \tag{3d}
\]

distinct source faces contain a high canonical triple.  Thus a low-mean
minimizer has a `1/O((log n)^4)` fraction of *all* faces carrying a disjoint,
rooted `Omega(n/(log n)^3)` circuit cloud.  The exact residual is to
multiply this weighted face-attached pocket family, or charge the entropy of
diffuse roots.  Existence of one dense root does not imply a decreasing
mutation: the exact nine-point global minimizer has an outer triple of
maximum degree `n-3`, yet all eleven exposed allowable-sequence braid flips
increase `V` by two.  See
`agent_outer_internal_product/WEIGHTED_ROOT_STAR_MINIMIZER_OBSTRUCTION.md`.

The low-rank reduction for this weighted obstruction is now exact.  Assign
each blocked pair `(A,p)` to its first canonical tangent witness `T`, retain
only witnesses with `d(T)>=D_0/2`, and give the resulting `(A,T)` record
weight `1/n`.  If this weight is `omega(A,T)`, then

\[
 \sum_{A,T}\omega(A,T)\ge {n-2\mu\over2n}V,
 \qquad \sum_T\omega(A,T)\le1\quad\hbox{for every }A.   \tag{3d1}
\]

Consequently, for every fixed `K`, the slice `|A|<=Kmu` retains weight at
least

\[
 \left({n-2\mu\over2n}-{1\over K}\right)V.             \tag{3d2}
\]

Thus `K=4+o(1)` leaves genuine `Theta(V)` marked mass at rank `O(log n)`
in a low-mean minimizer.  This corrects the potential `|A|^2` bias of raw
canonical incidences; all marked-release decoders remain valid for the
fractional weights.

There is also an exact global average-cover gate on this slice.  For rooted
complete-product charts `c`, let `P_c` be their external source product,
`H_c` their pocket-face count, `sigma_c(F)` the minimum deleted alphabet
entropy releasing `F`, and `Lambda` the actual aggregate output
multiplicity across all roots and bases.  With

\[
 N=\sum_cP_cH_c,
 \qquad \overline\sigma={1\over N}
        \sum_cP_c\sum_F\sigma_c(F),
\]

the disjoint occupancy masks and Jensen give

\[
                  N2^{-\overline\sigma}\le\Lambda V.   \tag{3d3}
\]

Hence source mass `>=eta V`, pocket count `>=H`, and subquadratic
`Lambda/eta` force
`overline sigma>=log(eta H/Lambda)`.  A quarter-coefficient pocket then
forces mean mandatory-loop entropy at least `(1/8-o(1))(log n)^2`, or mean
fractional `2+2` packing at least `(1/16-o(1))(log n)^2`.  Low rank alone
does not eliminate the loop alternative: an exact rooted cap chart has
`Theta(log n)` occupied roles and quadratic deleted alphabet entropy.  Its
outer cap is a huge convex shield, so it is not a low-mean `Theta(V)`
regression.  Suppressing that shield without creating another profile bank
is exactly the heterogeneous common-guard gate below.  See
`agent_outer_internal_product/MINIMIZER_WEIGHTED_LOOP_COVER_GATE.md`.

The complete-product hypothesis in this *entrance* can now be removed.
Fix one root triple `T` and one source rank `r=O(log n)` in the rank-safe
slice, and put `s=r-3`.  Colour the remaining physical labels uniformly by
`[s]` and retain a source when its nonroot labels receive distinct colours.
Some deterministic colouring retains source weight

\[
 W\ge {s!\over s^s}W_0,
 \qquad \log {V\over W}=O(\log n).                     \tag{3d3a}
\]

The fixed root and rank cost only another polynomial factor.  The surviving
sources are arbitrary selected words, not a Cartesian product, and the
colour order need not be their cyclic order.  Let their disjoint colour
alphabets be `X_i`, let `mathcal H`
be any `H` ordinary faces of the deterministic pocket `X_T`, and for each
pair `(A,F)` choose an arbitrary deletion set `G(A,F) subseteq A` for which

\[
                    U=(A\setminus G(A,F))\cup F
\]

is ordinary.  Put
`sigma(A,F)=sum_{i:\,X_i\cap G(A,F)\ne emptyset}log|X_i|`.
The single output `U` reveals `F`, every retained source label, and the
deletion mask.  Since every source atom has weight at most one, conditional
entropy gives the exact adaptive-release inequality

\[
 \mathbb E\sigma(A,F)
       \ge \log W+\log H-\log V
       \ge \log H-O(\log n).                            \tag{3d3b}
\]

Thus a quarter-scale inductive pocket already forces quadratic *mean*
adaptive cover entropy on the actual selected source family, with no
product extraction, semialgebraic retention, or output-load assumption.
For the rank-at-most-three hypergraph of split four-circuits, threshold
rounding further gives

\[
       \mathbb E\tau^*(A,F)\ge {1\over3}\mathbb E\sigma(A,F),       \tag{3d3c}
\]

where vertex capacities are `log|X_i|`.  This entrance also has an exact
internal split.  Conditional on an output `U`, let `J(U)` be its visible
deletion mask, `D=A_J` the missing completion word,
`Omega_U=prod_{i\in J}X_i`, and
`R_U=log|Omega_U|-H(D\mid U)`.  Since `(U,D)` recovers `(A,F)`, one has

\[
 \mathbb E\sigma=H(A,F)-H(U)+\mathbb E R_U.            \tag{3d3d}
\]

Thus low mean `R_U` produces product-like fixed-`(B,F,J)` completion
fibres to which the redundancy transcript applies, while high mean `R_U`
is exactly a common-base high-redundancy support/downshadow branch that
must retain `(B,F,J)`.  There is no additional abstract overlap variable.

This sharper colouring is valid through unordered four-local projection,
Hall pruning, fixed-label chronology, and the role forest: those arguments
use only distinct colour classes and heredity.  It must stop before an
oriented seam/profile step.  Recovering a common cyclic permutation there
may cost `s!=2^{Theta(L log L)}` and restores the older lower-order loss.
Thus `(3d3a)`--`(3d3b)` genuinely sharpen the cover-entropy entrance and
all-loop forest, but do not silently strengthen polar local-to-global or
cap/cup profile theorems.  See
`agent_outer_internal_product/UNORDERED_COLOUR_LIVE_RELEASE_REFINEMENT.md`.

The low-redundancy half is now a genuine recoverable promotion, not merely
an analogy.  Choose a generic point inside the common root triangle.
Adjacent polar-order predicates and all cyclic consecutive turns are only
`O(r)` bounded-degree predicates; the root makes every angular gap less
than `pi`, so a polar-ordered word with all positive consecutive turns is
a simple convex polygon.  For each fixed `U`, either `U union D` is already
an injectively decoded mixed face, or fix its first bad four-circuit class.
There are at most `Q<=C r^3R_{max}^3` such classes, and conditioning raises
mean completion redundancy by at most `log Q`.  The redundancy transcript
therefore retains decoded good records together with complete product
completion cells of total effective probability at least

\[
              2^{-A(r+\mathbb E R_U+\log Q)}.          \tag{3d3e}
\]

Every bad cell retains the actual ordinary base `U=B union F`, the root,
the visible mask, and one homogeneous actual four-circuit meeting `F`;
every ambient completion in the cell is an ordinary source.  Thus
`E R_U=o((log n)^2)` preserves the quadratic coefficient with no
face-alphabet description loss.  The only branch left at this entrance is
large mean `R_U`, namely a common-`(B,F,J)` high-redundancy completion
support/downshadow family.

That high-redundancy branch has an exact local saving and an exact global
overlap obstruction.  For a release fibre `u`, let `m_u` be its record
weight, `Q_u=union_{i in J_u}X_i`, `N_u=|Q_u|`, `s_u=|J_u|`, and let
`H_u=V(P|Q_u)-1` be its nonempty ambient support-face reservoir.  If
`Lambda_supp` is the actual overlap of these reservoirs, two-bank Cauchy
gives

\[
 \sum_um_u\le
   \sqrt{\Lambda_{supp}\max_u{m_u^2\over H_u}}\,V.     \tag{3d3f}
\]

Weights at most one, disjoint supports, AM--GM, and the universal quarter
theorem give the unconditional rank-tax estimate

\[
 \log{m_u^2\over H_u}
 \le 2s_u\log{N_u\over s_u}-2R_u
      -(1/4-o(1))(\log N_u)^2.                         \tag{3d3g}
\]

Thus high `R_u` is a genuine local gain.  Its support overlap cannot be
discarded.  In a rational common-guard tensor, take a length-`q`,
dimension-`k` Reed--Solomon source code over alphabet `p` and an `h`-role
complete pocket product.  Every source role is a mandatory singleton loop
for every pocket word, while the released output retains only the pocket.
Then

\[
 M=p^k,\qquad K=p^h,\qquad R_u=(q-k)\log p,
 \qquad\Lambda_{supp}=p^h,                              \tag{3d3h}
\]

and the old-source by released-face Hall graph is literally
`K_{p^k,p^h}`.  The scale

\[
 q=(.4+o(1))L,\qquad k=(.2+o(1))L,
 \qquad h=(.3+o(1))L,\qquad\log p=(1+o(1))L            \tag{3d3i}
\]

has record coefficient `1/2`, redundancy `.2L^2`, but separate
support-bank coefficients only `.4` and `.3`.  This is not a low-face
counterexample or a live normalized minimizer fibre--other cap/cup and
profile faces may pay, and its selected code is quadratically sparse
inside an ordinary ambient source box--but it proves
that high redundancy, Hall density, and the two separate face banks do
not finish the argument.  The precise remaining operation is a third
mixed profile/chronology bank cutting `Lambda_supp`.  See
`agent_common_shield_mixing/HIGH_REDUNDANCY_RELEASE_HALL_BARRIER.md`.

The live normalization is substantially sharper.  Let
`P_0=prod_i|X_i|`, `R_src=log P_0-H(A)`, and suppose the aligned source
weight satisfies `log W>=log V-tau`.  Independence of source and pocket,
the identity `(3d3d)`, and `sigma<=log P_0` give

\[
 \mathbb E R_U\le R_{src}+\log(V/H)
 \le r\log(N/r)-\log f(N)+\tau+\log(V/H).             \tag{3d3j}
\]

On a least fixed-gap counterexample, `tau+log(V/H)=O(L log L)` and
induction on the proper source support gives `log f(N)>=c(log N)^2`.
Consequently

\[
 \mathbb E R_U
 \le (r-c\log N)\log N-r\log r+O(L\log L).            \tag{3d3k}
\]

Every rank slice `r<=c log N+O(log L)` is therefore automatically in the
recoverable low-redundancy branch.  Quadratic high redundancy can survive
only in the **excess-rank** window

\[
                         r-c\log N=\Omega(L).          \tag{3d3l}
\]

For the common-guard tensor itself, the ambient source box gives
`V>=p^q` while the selected code has `W=p^k>=V2^{-tau}`, so
`(q-k)log p<=tau=O(L log L)`.  Its quadratic-redundancy parameters in
`(3d3i)` are thus an interface stress, not a live branch; a live tensor
returns to `(3d3e)`.  The genuine unsolved state is nonhomogeneous
excess-rank geometry or many bases reusing the same support reservoir.

There is one final exact split before that reservoir is used.  For a fixed
visible mask `J`, conditional redundancy decomposes as

\[
 \mathbb E(R_U\mid J)
   =\log|\Omega_J|-H(D\mid J)+I(D;U\mid J),             \tag{3d3m}
\]

and pointwise, if `P_u` is the product of the **actual conditional**
coordinate supports,

\[
 R_u=\log{|\Omega_J|\over P_u}
           +\bigl(\log P_u-H(D\mid U=u)\bigr).          \tag{3d3n}
\]

Only the second term is intrinsic correlation on labels that really occur
over `u`; the first is conditional alphabet slack, and the mutual
information in `(3d3m)` may already be carried by the released output.
The full-alphabet estimate `(3d3f)` remains valid for all three terms, but
an overloaded global label absent from a particular fibre cannot be
promoted to a source subface there.

For the intrinsic actual-support branch, put
`K_u=mathcal F(P|Q_u^{act}) setminus {emptyset}` and `k_u=|K_u|`.
Uniform routing and heredity give the physical-label bound

\[
 \Lambda_{act}\le
    \max_x\sum_{u:x\in Q_u^{act}}{m_u\over k_u}.        \tag{3d3o}
\]

Low right-hand side pays globally.  High codegree fixes one physical
deleted label `x`; then both
`E_u=B_u union {x}` and `U_u=B_u union F_u` are ordinary.  Two-target Hall
routing either pays again or leaves a dense fixed-`x` face--face core, and

\[
 (E_u,U_u)\longmapsto(B_u,F_u,J_u,x)                   \tag{3d3p}
\]

is exact after the role colours are fixed.  Thus the live endpoint inside
the intrinsic branch is an excess-rank dense graph between actual faces
`B union {x}` and `B union F`, with only the certified source-internal
description load.  This projected pair does **not** recover the remaining
completion word `D`; its residual load is part of the dense core, not a
free decoder.  The alphabet-slack/output-information branch instead
remains at the original full support-overlap/profile gate.  A rational
anti-aligned diagonal-code example proves that no local ordinary face need
retain `F` and even one support label despite quadratic intrinsic
redundancy; detached Boolean clouds pay it globally.  See
`agent_outer_internal_product/HIGH_REDUNDANCY_RELEASED_PREFIX_BARRIER.md`.

The excess-rank completion ambiguity has a sharp downshadow formulation.
For a rank-`s` bucket of total weight `M_s`, completion `t`-trace averaging
fixes an actual ordinary trace `I` with

\[
 M_I\ge{\binom{s}{t}\over\binom Nt}M_s,\qquad
 \Delta(B\cup I,U)\le\binom{N-t}{s-t}.                \tag{3d3q}
\]

With `s=Theta(L)` and `log N=Theta(L)`, `t=O(log L)` preserves the
quadratic mass but leaves quadratic ambiguity; taking `s-t=O(log L)`
makes the decoder quasipolynomial but costs `Theta(L^2)` bits.  Complete
rank layers attain both losses, so no stronger shadow-only compression is
available.

Keeping the full completion gives the correct Hall endpoint.  The pair
`(D,U)` recovers `B,F,A=B union D`.  If the normalized fixed-gap slice has

\[
 W\ge V/\Xi,\qquad M_s\ge WH/\Gamma,                 \tag{3d3r}
\]

then one actual deleted label `x` occurs in weight at least `sM_s/N`, and
the exact `D`-versus-`U` Hall density on that fibre is at least

\[
             \eta_x\ge {sH\over2N\Gamma\Xi}.          \tag{3d3s}
\]

For `Gamma Xi=2^{O(L log L)}` and
`log H=(c-o(1))L^2`, this is still quadratic-exponential; pruning produces
a dense completion-face by released-face core, not a contradiction.  The
anti-aligned two-cloud rank-layer construction attains `(3d3q)`, but its
detached Boolean banks make `W/V` exponentially too small in the bounded
rank live window.  The precise excess-rank target is therefore to rule out
such a dense incompatible `D`--`U` core under live normalization, or to
extract an additional planar mixed/profile bank.  See
`agent_outer_internal_product/EXCESS_RANK_FIXED_LABEL_DOWNSHADOW_GATE.md`.

The dense core does admit an unconditional physical coordinatization.
After fixing the root and retaining an injective random role-colouring, the
weight loss is only `s!/s^s>=e^{-s}`.  For a weighted source law on
`X_1 times ... times X_s`, put

\[
 P_0=\prod_i|X_i|,\qquad R_w=\log P_0-H(P).             \tag{3d3t}
\]

Every bad ambient completion contains a bad four-set.  If
`beta_{J,K}` is the bad density on roles `J` together with a fixed root
subset `K`, the exact union bound is

\[
 C_0\ge P_0\left(1-\sum_{|J|+|K|=4}\beta_{J,K}\right). \tag{3d3u}
\]

Hence either at least `P_0/2` ambient rooted words are ordinary, or at most
four physical roles and a fixed root subset contain, after only a
polylogarithmic semialgebraic refinement, a complete box of one signed
`1+3` circuit type.  The first alternative and live normalization force
`R_w=O(L log L)`; MDS/strength-four codes therefore complete rather than
survive as sparse modules.

There is a simultaneous exact projection split.  If `G` is the entropy of
ordinary missing-coordinate extensions and `B` the entropy of blocked
extensions, then

\[
                 R_w\le G+B,\qquad {V\over W}\ge2^{G/s}. \tag{3d3v}
\]

If `B>=R_w/2`, one actual source triple blocks
`|X_i|/poly(s)` physical labels on a positive-mass projected-base family.
This eliminates a featureless high-redundancy code, but the one-gap gain
in `(3d3v)` is only fixed-power and can be swallowed by the existing
`2^{O(L log L)}` finite-gap loss.  The remaining need is still to
multiply or sum these rolewise physical banks with the released side.  See
`agent_common_shield_mixing/EXCESS_RANK_FOUR_LOCAL_PROJECTION_DICHOTOMY.md`.

Live Hall normalization transfers to **both** face sides before that
coupling is attempted.  If each literal `(D,U)` pair has weight at most
`delta`, pruning the density `(3d3s)` at half its value gives actual
families `mathcal D_*`, `mathcal U_*` with

\[
 |\mathcal D_*|,|\mathcal U_*|
 \ge {sV\over4N\Gamma\Xi\Theta\delta}
       =V\,2^{-O(L\log L)},                            \tag{3d3w}
\]

provided `H>=V/Theta`.  Every completion contains the already-fixed
physical label `x`; delete it, then apply `(3d3u)` injectively to the
rank-`s-1` ordinary faces.  Quadratic completion redundancy forces a
genuine polynomial-density four-physical-role circuit box; the
ordinary-completion alternative again forces only `O(L log L)`
redundancy.  But neither this box nor the one-gap/blocker split is
guaranteed to coexist with `mathcal U_*`.  In a strongly separated
two-cloud chart the exact mixed bank is only

\[
 |\mathcal D_*\cap\mathcal R(Y)|\,
 |\mathcal U_*\cap\mathcal A(Z)|,                       \tag{3d3x}
\]

and anti-aligned fixed-`x` rank layers make both intersections empty.
Their Boolean clouds violate live normalization, so they are not a live
regression.  The sharp residual is a **live profile-penetration/composition
theorem**: a rank-`O(L)` face family of size `V2^{-O(L log L)}` must
penetrate the actual facing profile, or its avoidance must expose a
globally controlled detached/composition bank.  See
`agent_outer_internal_product/LIVE_DENSE_COMPLETION_PROFILE_GATE.md`.

Even without profile penetration, a live incompatible pair cannot remain
chronology-free.  Let `M` be weighted mass on literal disjoint-ground
completion/release pairs, let every fixed pair have weight at most
`delta`, and put `Lambda_1=2n`.  If

\[
                     {M\over\Lambda_1^{q-1}}>2\delta V,  \tag{3d3y}
\]

then iterative four-locality produces `q` pairwise new physical labels
`z_1,...,z_q` on the completion side.  At step `j`, each retained record
has an actual cross-circuit containing the common `z_j`; the other three
witness labels may vary.  Delete `z_j`; the remaining endpoints stay
ordinary, the retained weight is at least `M/Lambda_1^j`, and the reduced
pair plus the fixed chronology reconstructs the literal original
completion.  The alternative at every step is an ordinary mixed-face bank
of load `delta`.  If the whole actual circuit is also fixed, the same
statement holds with the weaker `Lambda_4=2 binom(n,4)`.

On the live fixed-`x` core, `M>=V^2/2^{O(L log L)}` and
`log V>=cL^2-o(L^2)`, so `(3d3y)` yields

\[
                         q\le(c-o(1))L.               \tag{3d3z}
\]

The fixed-circuit refinement separately retains `(c/4-o(1))L` common
actual circuits.  Thus the two-family residue contains a linear-length
fixed-label chronology with record-by-record genuine circuit witnesses,
while retaining the full decoder; it forces completion rank at least
`(c-o(1))L`.  This is sharp locally: anti-aligned parabolic layers peel
through repeated variable `3+1` witnesses; depending on the prescribed
side, they may have to peel that endpoint all the way to empty.
Those layers are again non-live.  The exact missing statement is now a
live chronology theorem: either witness-triple spread or a long rooted
star must be globally chargeable, or first divergence must create a
detached/cyclic profile bank with subquadratic load.  See
`agent_outer_internal_product/LIVE_CROSS_CIRCUIT_CHRONOLOGY.md`.

The stationary rooted-star alternative is now closed exactly.  Peel the
released side, and at stage `j` let `tau_j` be the minimum transversal
number of the released-side traces of the canonical bad cross-circuits.
If the released rank is at most `R`, the fixed-pair decoder and hereditary
deletion give

\[
 \log {M\over2\delta V}
       \le\sum_{j<t}(1+\log\tau_j),
       \qquad t\le R.                                \tag{3d3z2}
\]

In particular, if one fixed hereditary root `T` of size `h` meets every
remaining trace after every previous deletion, then

\[
                         M\le2\delta V\cdot2^h h!.   \tag{3d3z3}
\]

So a stationary triangle/common cage cannot carry the live mass.  With
`M>=V^2/2^{O(L log L)}`, `R<=CL`, and `log V>=cL^2-o(L^2)`, `(3d3z2)`
forces average transversal entropy at least `(c/C)L-O(log L)`.  A positive
fraction of the levels therefore have

\[
              \tau_j\ge n^\epsilon,
              \qquad \nu(\mathcal H_j)\ge\tau_j/3,    \tag{3d3z4}
\]

where the second inequality is the exact rank-three maximal-matching
bound.  Thus the live residue contains polynomially many pairwise disjoint
actual released-side circuit traces at many chronology levels.  These
traces live on different records and deleting a singleton trace can erase
its branch tag, so routing that first-divergence forest remains open.  See
`agent_outer_internal_product/LIVE_ROOT_TRANSVERSAL_ENTROPY_GATE.md`.

Together with the completion-side rank corollary of `(3d3y)`, the same
inequality gives the symmetric live threshold

\[
       \operatorname{rank}A,\operatorname{rank}U
                    \ge(c-o(1))L.                    \tag{3d3z4a}
\]

At the coefficient-half target the two endpoints therefore use at least
`(1-o(1))L` labels in total.  The remaining capacity problem is genuinely
near-saturated: deleting one whole side can spend essentially the entire
quadratic record entropy, exactly as the Pascal prefix trie does.

There is, however, a decisive live-normalized obstruction to every
**two-family-only** version of that statement.  In the central Pascal top
split `P=Y prec Z`, fix a rank fibre of left ordinary noncap faces `D`
containing one canonical noncap triple, and take all right ordinary noncup
faces `U`.  Both alphabets have size `V(P)2^{-O(L log L)}`, the pair decoder
has load one, and the completion rank satisfies

\[
 |D|\ge(\beta-o(1))L,
 \qquad \beta=1-{1\over4\ln2}=0.639326\ldots .       \tag{3d3z1}
\]

Yet every nonempty left face `A subseteq Y` has `A union U` nonconvex for
every retained `U`; the unique releasing guard is all of `D`.  Hence the
`2n` chronology can peel linearly many labels but cannot create a mixed
face before source exhaustion, and semialgebraic retention sees one
identically bad rectangle.  This is not a sub-half example--the Pascal
cell itself has coefficient `beta>1/2`--but it proves that live
normalization, excess rank, fixed roots, four-local boxes, and exact pair
decoding do not supply the missing coupling.  A successful closure must
use minimizer-specific endpoint/profile balance, a third cyclic role, or a
global charge of the all-loop chronology.  See
`agent_common_shield_mixing/LIVE_PASCAL_COMMON_GUARD_MULTIPLICATION_BARRIER.md`.

Local minimizer mutations do not remove this obstruction.  At an actual
replaceable strong seam `P=Y prec Z`, minimality among the four independent
child reflections forces the facing profiles to be the smaller ones:

\[
 C(Y)\le U(Y),\qquad U(Z)\le C(Z).                    \tag{3d3z5}
\]

Put `e(Q)=(log C(Q)+log U(Q))/2` and
`rho(Q)=(log U(Q)-log C(Q))/2`.  The universal upper/lower-hull injection
gives `e(Q)>=log V(Q)/2`, while the actual seam bank has exact logarithm

\[
 \log(C(Y)U(Z))=e(Y)+e(Z)-\rho(Y)+\rho(Z).            \tag{3d3z6}
\]

The imbalance is therefore a directed potential.  It telescopes on an
actual cycle of profile seams in the same configuration, so some edge
recovers the average endpoint energy and span; on a path, the exact quarter
ramp makes the potential drop cancel the whole span.  Reflected children
are alternative configurations, not internal face banks, so minimality
actually reinforces the local anti-alignment.  The precise extra target is
now an actual same-configuration profile cycle/reset, or repeated realized
direction queries of one physical child whose potential cannot keep
dropping.  See
`agent_common_shield_mixing/MINIMIZER_ALL_LOOP_ENDPOINT_POTENTIAL_GATE.md`.

Nor does a fixed signed all-loop cell force such a seam by geometric
classification.  There is a rational blow-up with `m` source and `k`
target roles of alphabet size `A`, convex transversal banks `A^m,A^k`,
and one fixed signed `1+3` circuit blocking every nonempty partial source
word against every target word.  Nevertheless the three fixed target
anchors straddle the line through every pair of distinct source roles in
every rechart.  Any side-respecting strong-glue extraction retains at most
one source role and therefore at most

\[
                         (1+mA)A^k                         \tag{3d3z7}
\]

outputs, losing `2^{(alpha-o(1))(log n)^2}` from the full rectangle when
`m=alpha log A`.  This is a classification barrier, not a live regression:
its fixed hereditary three-label released root exits immediately through
`(3d3z3)`, so other ambient banks must pay under live normalization.  The
true residue after `(3d3z4)` must retain high released-root transversal
entropy as well as defeat strong separation.  See
`agent_shield_circuit_cover/ALL_LOOP_NONSTRONG_TRANSVERSAL_BARRIER.md`.

High transversal entropy itself still need not create a reset.  Refining
the same live Pascal rectangle to fixed ranks, choose for every nonempty
reduced pocket `U'` the singleton released trace `{min U'}`.  The adaptive
descent is exactly the increasing-prefix trie of the pocket family.  If
`h_j` is the dispersion along a maximum-child branch of uniform rank `s`,
then

\[
               \prod_{j<s}h_j=|\mathcal H|,
               \qquad q_j\ge h_j,                    \tag{3d3z8}
\]

where `q_j` is the literal singleton matching size at level `j`.  Since
`log|H|=(beta-o(1))L^2` and `s<=(1+o(1))L`, for every fixed
`0<epsilon<beta` at least

\[
 \left({\beta-\epsilon\over1-\epsilon}-o(1)\right)L \tag{3d3z9}
\]

levels have `q_j>=n^epsilon`.  Nevertheless the full branch graph is a
DAG: its state is a strictly increasing deleted prefix, every leaf for a
fixed source collapses to `(D,emptyset)` with load `|H|`, and
`D union {z}` is nonconvex for every erased label `z`.  Thus even the exact
high-transversal conclusion `(3d3z4)` does not directly route to a
source-retaining cycle.  The missing operation is **cross-branch storage**:
an ordinary third face/role that retains the source identity and a deleted
prefix label, or a projected-source cycle with a controlled decoder.  This
Pascal example is again above one half, so a minimizer-specific cycle may
still exist.  See
`agent_common_shield_mixing/HIGH_TRANSVERSAL_PASCAL_PREFIX_DAG_BARRIER.md`.

One natural diffuse-root escape is now ruled out exactly.  Suppose a
retained convex carrier has `m` pairwise nonadjacent ear edges; at each
edge there are `A` source labels and `A` vertex-disjoint target triangles,
and every source label lies inside every local target triangle.  Writing a
triangle in boundary order as `(ell,z,r)`, its common interior point and
the two tangent coordinates force every crossed pair `(ell_b,r_c)` to be
an admissible ear.  The nonadjacent carriers commute, so the two endpoint
words give a load-one bank of size

\[
              A^{2m},\qquad M=A^{2m}\le V.             \tag{3d3z9a}
\]

This pays the entire source-word by target-word bad rectangle even though
each chronology level has `A` disjoint released triangles and no fixed
physical root.  Hence a live high-transversal survivor must be
systematically nonseparated from its carrier contexts; same-type singleton
transversals alone do not suffice, by the strong-separation endpoint
counterexample.  The remaining direction-circle task is to retain the
carrier/context mark long enough to extract either this endpoint product
or a decoded cyclic seam bank.  See
`agent_shield_circuit_cover/HIGH_TRANSVERSAL_COMMON_POCKET_ENDPOINT_PRODUCT.md`.

The same geometry has an exact context-load form.  For a literal retained
carrier state `K`, the ordinary faces `K union {ell_b,x_a}` and
`K union {x_a,r_b}` directly encode every source-primitive record.  If the
source/history is not primitive but there are `b_K` triangular ears, the
crossed endpoint pairs still encode up to `b_K^2` records.  Summing over
carrier states costs only the actual carrier decoder load.  Thus the sole
concentrated survivor repeats records over the same literal `(K,x,T)` data,
or has multiplicity beyond the endpoint square; it is not an erased
chamber-name issue.

More importantly, fixing the physical carrier/root fibre `g=(K,x)` with
`b_g` common-pocket triangles gives the rooted module

\[
                  K\cup\{\ell_i,x,r_j\},\qquad i,j\in[b_g],
                                                               \tag{3d3z9b}
\]

of `b_g^2` ordinary faces, retaining the root and decoding both trace
indices.  If `T=sum_g b_g`, `B=sum_g b_g^2`, `S` is the number of actual
old-source faces, `delta` the source--trace pair load, and `lambda` the
rooted-module load, then `M<=delta S T`, `V>=S`, `V>=B/lambda`, and hence

\[
                         M\le\delta\lambda{T\over B}V^2. \tag{3d3z9c}
\]

Thus `b_g>=h` throughout gives the fixed-power saving `1/h`.  The only
carrier residue fragments the high trace dispersion among many distinct
retained `(K,x)` fibres with `b_g=O(1)`; arbitrary/nonprimitive source
history is no longer an obstruction inside one fibre.

Mass-uniform branching and the `1/n` atom floor do not force those fibres
to merge.  If `Z` is the next label and `G` its literal carrier/root state,
`max_z Pr(Z=z)<=kappa/d`, and at least `1-theta` of the mass lies in fibres
of label support at most `h`, then exactly

\[
 I(Z;G\mid\mathrm{low})
       \ge\log{d(1-\theta)\over\kappa h}.              \tag{3d3z9d}
\]

Along a path this gives

\[
 H(G_1,\ldots,G_s)
       \ge\sum_i\log{d_i\over\kappa_i h_i}.           \tag{3d3z9e}
\]

A planar parity-code ear family attains the split: `q-1` roles branch
perfectly uniformly, every atom has exact weight `1/N`, every source and
target has mass one, yet deleting a triangle leaves a carrier which
determines its missing parity label, so every literal `b_g=1`.  The carrier
itinerary stores all the entropy.  The example is nevertheless paid:
deleting its trace-dependent carrier tags recovers one common base and the
rooted modules `K_0 union {ell_b,x_a,r_c}` multiply to `A^{3q}` faces.
Thus the exact geometric target is a recoverable carrier-coarsening theorem,
not another support, mass, or atom-floor pigeonhole.  See
`agent_shield_circuit_cover/MASS_UNIFORM_CARRIER_FRAGMENTATION_GATE.md`.

The bare branch-tag decoder can nevertheless be repaired at no factorial
cost.  Colour the completion endpoint as a transversal of ordered physical
roles `X_1,...,X_s`, `d_i=|X_i|`, and process all bad branches in parallel.
At a node choose the smallest completion role appearing in any surviving
cross-circuit; within each role retain the heaviest actual-label class and
delete that label.  Deletion cannot create a circuit, so roles strictly
increase on every path.  A terminal mixed face reveals its empty-role set,
whose sorted order walks the unique forest branch and reconstructs every
deleted label.  The exact weighted induction gives

\[
 M\le\delta V P_0,
 \qquad P_0=\prod_{i=1}^s d_i.                       \tag{3d3z10}
\]

Thus singleton traces and prefix siblings do admit one global literal
decoder.  If the selected completion family has size `M_D` and redundancy
`R_D=log(P_0/M_D)`, a rectangular mass `M_D H` yields a mixed bank of size
at least

\[
                              H2^{-R_D}.               \tag{3d3z11}
\]

This is sharp when every completion role must be deleted: the output is
only `U`, and the full factor `P_0` is lost.  Consequently low redundancy
recovers another live-normalized pocket bank, not the missing multiplier;
quadratic redundancy returns to the four-local physical-box branch.  The
next quantitative split is whether many terminal outputs retain a
quasipolynomial amount of completion-role entropy, or the all-roles-deleted
mass can be charged to an internal ambient profile bank.  See
`agent_outer_internal_product/ROLE_MONOTONE_MIXED_FACE_FOREST.md`.

The capacity loss in that forest has an exact **mass-entropy** split.  At a
node `v` and its next eligible role `i`, let the actual-label class masses
be `b_z`, put `b=sum_z b_z`, retain a largest class of mass `b_*`, and set
`r(v,i)=b/b_*`.  Thus `r` is the effective branching, not merely the
number of nonempty classes.  For a terminal output `O` put

\[
 C_{\rm eff}(O)=\prod_{(v,i)\in[\mathrm{root},O]}r(v,i),\qquad
 Q_{\rm eff}(O)={P_0\over C_{\rm eff}(O)}.
\]

If `mu(O)` is its routed record weight, the heaviest-child induction and
the literal empty-role decoder give exactly

\[
       \sum_O\mu(O)C_{\rm eff}(O)\ge M,
       \qquad \mu(O)\le\delta,                       \tag{3d3z11a}
\]

and hence, for every `Q_0>=1`,

\[
 \sum_{Q_{\rm eff}(O)\ge Q_0}\mu(O)C_{\rm eff}(O)
       \le {\delta V P_0\over Q_0}.                  \tag{3d3z11b}
\]

Thus any fixed share of terminal potential with
`Q_eff(O)>=n^{B\log\log n}` supplies exactly the missing quasipolynomial
factor.  The complementary branch is rigid because

\[
 Q_{\rm eff}(O)=\prod_{i\ {\rm undeleted}}d_i
       \prod_{(v,i)\ {\rm deleted}}{d_i\over r(v,i)}. \tag{3d3z11c}
\]

If every `d_i>=n^alpha` and `Q_eff(O)<n^{B\log\log n}`, at most
`(B/alpha)log log n` roles remain, while the total branching defect
`sum log(d_i/r(v,i))` is `O((log n)loglog n)`.  Outside an arbitrarily
small fraction of deleted levels,

\[
       \max_z\Pr\{z\mid v,i\}={1\over r(v,i)}
                \le {\operatorname{polylog}n\over d_i}. \tag{3d3z11c1}
\]

Thus the residue is not merely support branching or lost metadata: it is
an almost-all-roles-deleted law with near-uniform conditional **mass along
the selected path**.  This still need not give sibling intersection when
individual record weights decay rapidly with depth.  What remains is
coefficient-specific: couple the mass-uniform path to the physical
four-box/released context, charge the first depth-skewed sibling to an
ambient bank, obtain a mass-to-count cutoff, or force a realized reset
cycle.  See
`agent_outer_internal_product/ROLE_FOREST_TERMINAL_ENTROPY_SPLIT.md` and
`agent_outer_internal_product/EFFECTIVE_BRANCHING_ROLE_FOREST.md`.

There is also an unconditional coefficient narrowing.  For disjoint role
supports of total size `N` and `s=alpha L`,

\[
 \log {P_0\over V}
   \le (\alpha-c)L^2-\alpha L\log L+O(L),
 \qquad \log V=cL^2.                                  \tag{3d3z11d}
\]

Thus the forest already closes with a fixed quadratic gain when
`alpha<c`, and at the critical rank `alpha=c` it supplies the required
`n^{-c\log\log n+O(1)}` factor.  Only the genuine excess-rank regime
`alpha>c` can absorb the quasipolynomial saving; this is exactly the
physical four-local/profile branch isolated earlier, now with the
near-complete all-deletion law attached.

Support branching alone still does not imply sibling coherence.  The exact
prefix-star family

\[
 \mathcal E_{s,k,d}=[d]^k\times\{0\}^{s-k}
  \;\cup\!\bigcup_{i>k,z\ne0}\!\{(0,\ldots,0,z,0,\ldots,0)\}
                                                               \tag{3d3z11e}
\]

has `log|E|=cL^2-cLlogL+O(L)` at `k=cL`, rank `s=alpha L>cL`, and
along its all-zero terminal path every role has all `d` labels in support.
Yet any two nondefault excess-role labels have conditional codegree zero.
A four-role physical bad box can therefore be disjoint from every selected
source while the support statistic is maximal.  With unit weights the
effective ratios telescope to `C_eff=|E|` and the excess tail lands in the
paid high-`Q_eff` branch.  But the weighted tail assignment

\[
 w(0^h)=d^{-h},\qquad
 w(0^{j-1}z0^{h-j})=d^{-j}                            \tag{3d3z11f}
\]

has total mass one per core word, `r(v,i)=d` at every role,
`Q_eff=1`, and still zero codegree between different nondefault tail
siblings.  It uses one record per source and respects the per-source cap.
Hence even effective mass branching needs either a lower weight cutoff,
mass-to-count control, or genuinely planar/minimizer sibling geometry.  See
`agent_outer_internal_product/EXCESS_RANK_PREFIX_STAR_COHERENCE_GATE.md`
and `agent_outer_internal_product/EFFECTIVE_BRANCHING_ROLE_FOREST.md`.

The literal minimizer records do have one useful cutoff, but it must not be
overread.  Before the high-density Hall core every nonzero raw marked atom
has weight at least `1/n`: all live reductions restrict, duplicate without
division, relabel, or coalesce whole records.  Run the role forest separately
inside one actual released-face fibre `U`, of raw mass `M_U`.  Along every
terminal path the telescoping ratios and the atom floor give

\[
 C_{\rm eff}(O)\le {M_U\over\mu(O)}\le nM_U,
 \qquad
 Q_{\rm eff}(O)\ge {P_0\over nM_U}
                   \ge {P_0\over n\delta V}.          \tag{3d3z11g}
\]

This removes the artificial `d^{-Theta(L^2)}` Kraft leaf whenever it would
fall below the genuine atom floor.  It still does **not** close the live
completion--release rectangle.  For a complete `M_D by H` rectangle with
unit atoms, the all-deletion forest has exactly

\[
 C_{\rm eff}=M_D,\qquad Q_{\rm eff}={P_0\over M_D},   \tag{3d3z11h}
\]

and only the `H` released faces survive.  The `Q_eff` saving cancels the
completion redundancy `P_0/M_D` and returns the already-known `H` bank;
two-sided Hall degrees are equalities and add no multiplier.  Thus the floor
is a provenance narrowing, not a proof of sibling coherence.  The surviving
unit-weight rectangle still requires a mixed/profile face or a third
retained tag.  See
`agent_outer_internal_product/LIVE_ATOM_FLOOR_ROLE_FOREST_AUDIT.md` and the
qualified cutoff in
`agent_outer_internal_product/TERMINAL_WEIGHT_FLOOR_EXCESS_RANK_GATE.md`.

In fact the live residue can be made essentially unit-weight.  Before
pocket replication, dyadically bucket the original `m/n` source weights.
One of `O(L)` buckets preserves an `Omega(1/L)` share, and thereafter all
raw atoms lie in one interval `[lambda,2lambda)`.  If `N_z` is the record
count in label class `z`, `N=sum_z N_z`, and `N_max=max_z N_z`, its
effective mass branching satisfies

\[
 {1\over2}{N\over N_{\max}}
       \le r_{\rm mass}\le4{N\over N_{\max}}.         \tag{3d3z11i}
\]

Across `s=O(L)` roles the mass/count discrepancy is at most
`4^s=2^{O(L)}`, so depth-geometric weighting is not the surviving issue.
This still leaves the unit-weight rectangle, but it now converts
near-uniform branching into genuine physical sibling support.

Fix one stripped convex base/chamber cell `B`.  At a rich deleted role `i`
there are at least `r_i` physical sibling labels; pigeonholing by their
actual insertion edge leaves a set `Y_i` with

\[
                         |Y_i|\ge {r_i\over |B|}.      \tag{3d3z11j}
\]

For any `t`, either `t` roles have pairwise nonadjacent heavy edges, in
which case the independent-ear subdivisions commute and give the injective
ordinary bank

\[
             \left|\{B\cup\{z_i:i\in I\}:z_i\in Y_i\}\right|
                    =\prod_{i\in I}|Y_i|,             \tag{3d3z11k}
\]

or fewer than `3t` heavy edges occur and one fixed edge carries at least
`s/(3t)` rich role clouds.  Taking `t=Theta(log L)` and
`r_i>=d_i/polylog(n)` makes the first branch exactly
`n^{Theta(loglog n)}`.  In the fixed-edge branch, the first two rich clouds
either already give many ordinary `B+x+y` faces, or canonical
Caratheodory witnesses and a loss of at most `binom(|B|,2)` produce a dense
labelled circuit box

\[
                             \{u,v,x,y\},
                 \qquad \{u,v\}\subset B.             \tag{3d3z11l}
\]

This is a genuine advance over marginal coherence: the only unresolved
loss is now global.  The base in `(3d3z11k)` must retain the released
carrier/context, or the ear bank can be reused by arbitrarily many columns.
Thus the live alternatives are a bounded-load quasipolynomial ear bank, a
fixed-edge physical circuit tensor, or a high cross-context carrier load.
See
`agent_common_shield_mixing/MASS_UNIFORM_SIBLING_EAR_OR_CIRCUIT_GATE.md`.

The fixed-edge tensor itself has an exact shield telescope.  For singleton
ears `x,y` replacing the same actual edge `uv`, a bad union is equivalent
to one sibling lying strictly inside `triangle(uv,other)`; the witness is
exactly `uvxy` and the resulting containment orientation is a DAG.  For a
marked outer-star state `g`, let `d_g` be its hidden sibling count,
`h_g=V(N_g)-1` the nonempty detached shield bank, `a_g` its weight, and put

\[
 T=\sum_ga_gd_g,\qquad
 Q^2=\max_g{d_g^2\over h_g},\qquad
 \kappa_A=\max_A\sum_{g:A_g=A}a_g,\qquad
 \lambda_H=\max_F\sum_{g:F\in\mathcal H_g}a_g.
\]

Grouping the ordinary carrier and shield outputs and applying Cauchy gives

\[
                    T\le Q\sqrt{\kappa_A\lambda_H}\,V.          \tag{3d3z11l1}
\]

If `mu` is the maximum literal `(carrier,shield)` pair load, then for every
threshold `R` either one shield sees at least `R` distinct carrier faces,
or

\[
                    T\le Q\sqrt{\kappa_A\mu R}\,V.              \tag{3d3z11l2}
\]

For `d_g>=d` on at most `N` physical labels,

\[
             Q\le {N\over\sqrt{f(d)-1}}.                         \tag{3d3z11l3}
\]

Thus `d>=n^gamma/polylog(n)` and the safe
`log f(d)>=(1/8-o(1))log^2d` make `Q` quadratically small: it absorbs a
quasipolynomial `R` and polynomial literal loads.  An unpaid tensor must
therefore expose the desired outer-carrier bank or an enormous actual
carrier/pair multiplicity.  Fixing that pair feeds exactly into the full
source, longest-run downshadow, and surviving-gap banks below; repeated
names of one actual source remain an explicit nongeometric load.  See
`agent_shield_circuit_cover/FIXED_EDGE_CIRCUIT_STAR_SHIELD_TELESCOPE.md`.

Carrier coarsening itself now has a sharp mask/run split.  After the
trace-dependent tags are deleted, suppose `g` compressed gaps survive as
actual boundary gaps of the retained carrier.  Their edge graph has maximum
degree two, so at least `g/3` are vertex-disjoint.  If gap `i` carries
`b_i` common-pocket triangular ears with retained root `x_i`, the rooted
modules commute and give

\[
 B_c=\prod_{i\in I}b_i^2,\qquad |I|\ge g/3,\qquad
                    \sum_c w_cB_c\le\Lambda V.       \tag{3d3z11m}
\]

The output retains the coarsened carrier, roots, and both endpoint labels;
the empty completion roles reconstruct the monotone forest path.  Any
remaining coarsening ambiguity is honestly charged to `Lambda`.  In
particular, if

\[
 \log b_i\ge\beta L-O(\log L),\qquad
 g\ge\left({3\sigma\over2\beta}+o(1)\right)\log L,   \tag{3d3z11n}
\]

then this branch supplies `n^{sigma loglog n}`.  Gaps destroyed by the
pocket do not count; they enter the low-endpoint-entropy/circuit branch.

If the deletion mask has only `O(log L)` cyclic runs, one run instead
contains `Omega(L/log L)` roles and hence an induced physical child of
size

\[
                  m=\Omega\!\left({n\over\log L}\right).         \tag{3d3z11o}
\]

Writing `a=log(n/m)=O(loglog L)`, the exact half-target deficit is

\[
 {L^2-(L-a)^2\over2}=La-{a^2\over2}
       =\Theta(L\loglog L),                         \tag{3d3z11p}
\]

so this extremal run needs only `n^{Theta(logloglog n)}`, rather than the
full `n^{Theta(loglog n)}` multiplier.  Its Boolean downshadow is still too
small.  There is an exact load-one sufficient condition: a physical pair
in the child belongs to a pair-star family `J_R` of size at least
`(V(X_R)-m-1)/binom(m,2)`.  For any marked outside-context family `P`, put

\[
 E=\{(F,S)\in\mathcal J_R\times\mathcal P:F\cup S
                      \text{ is ordinary}\}.
 \quad V\ge|E|.                                      \tag{3d3z11q}
\]

The union decodes both disjoint grounds, so no biclique extraction is
needed.  If the child meets induction, it suffices that the compatibility
density times `|P|` exceed
`binom(m,2)2^{Theta(L loglog L)}`, exactly the smaller
`n^{Theta(logloglog n)}` scale up to a polynomial factor.

A parabolic central-pair regression shows that an arbitrary child
coface family need not splice through the run: one fixed `1+3` circuit can
kill every nonempty run trace against every retained opposite-side point.
An arbitrary `m`-point child can be projectively nested between two macro
arcs, with `q=(1/2+o(1))L` outside roles of size `D=Theta(n/L)`, so every
partial outside word is ordinary, every effective branching ratio is
exactly `D`, the raw marks have weight `1/n`, and the carrier load is one.
Nevertheless for the maximizing pair star `J` and every full outside word
`S`,

\[
       F\cup S\text{ is nonordinary for every }F\in\mathcal J,
       \qquad E=\varnothing,                           \tag{3d3z11r}
\]

because one fixed pair `o,p` satisfies
`p in int triangle(o,a(S),b(S))`.  For
`Phi_C(L)=L^2/2-CLlog L`, the weighted record mass still has the exact live
scale

\[
       M\ge {2^{2\Phi_C(L)}\over n^{(1+o(1))\log\log L}}.        \tag{3d3z11s}
\]

The common circuit or its triangle deletion has load
`|J|D^{q-2}/n`; the word and child projections have loads `|J|/n` and
`D^q/n`.  Only `(F,S)` is injective, and it is a separated two-face state.
This is a sharp **local** calculation, but a least-counterexample re-audit
shows that this planar chart is globally paid: an allowed constant change
in `q` makes `D^q` itself meet the target, and every outside word also
coexists with every child singleton.  Thus `(3d3z11s)` is not a live
planar regression.

An exact four-uniform independence complex shows that the same failure
cannot be removed by abstract heredity, effective branching, the `1/n`
atom floor, or the rank cap alone.  It has `t=(1/6+o(1))L` child colour
classes, at most three selected labels per class, and the same complete
outside sources and fixed `uv` child-pair cage, with

\[
 |\mathcal I|<2^{\Phi_C(L)},\qquad
 M\ge {2^{2\Phi_C(L)}\over n^{(1+o(1))\logloglog n}},
 \qquad \operatorname{rank}_{\rm child}<2L .          \tag{3d3z11s1}
\]

Its entire mixed pair-star incidence graph is empty.  Four-locality now
decisively rules out any planar realization.  Indeed, if disjoint planar
classes `Y_i` have every four-set meeting at least two classes ordinary,
then arbitrary internal faces multiply injectively:

\[
       V(P)\ge\prod_iV(Y_i).                          \tag{3d3z11s2}
\]

For class size `g=n/[Theta(L log L)]`, the safe quarter bound makes just
two such classes contribute
`(1/2)L^2-L(log L+loglog L)+O(L)>Phi_3(L)`; all `t`
classes would give `Theta(L^3)`.  Thus `(3d3z11s1)` is a sharp abstract
warning, not a planar survivor.

The exact planar residue is dense.  For the cross-bad-four hypergraph
`Gamma(Y,Z)`, deleting a vertex cover `K` makes the two internal face
banks multiply.  Hence every live pair of large classes satisfies

\[
       \tau(\Gamma(Y,Z))=\Omega(g),\qquad
       \nu(\Gamma(Y,Z))\ge\tau(\Gamma)/4=\Omega(g),   \tag{3d3z11s3}
\]

so it contains linearly many physically disjoint cross-class circuits.
In the homogeneous fixed-`uv` cage, exact circuit elimination gives an
endpoint XOR: every opposite-side carrier label releases a caged pair
through exactly one of `u,v`, and equal endpoint colours commute.  If
`d_i^e` is the colour-`e` population in role `i`, then the ordinary
partial-transversal banks have physical decoder load one and

\[
       P_e=\prod_i(1+d_i^e),\qquad
       P_uP_v\ge Q:=\prod_i(1+|X_i|),\qquad
       \max(P_u,P_v)\ge\sqrt Q.                       \tag{3d3z11s4}
\]

This does not yet retain an arbitrary rich child face or the omitted
opposite-colour choices.  The normalized long-run gate is therefore a
bounded-history composition of the dense physical circuit matchings with
the rich internal child bank, not the abstract cage itself.  See
`agent_common_shield_mixing/LONG_RUN_LEAST_COUNTEREXAMPLE_REAUDIT.md` and
`agent_common_shield_mixing/PLANAR_CROSS_CLASS_PRODUCT_AND_CAGE_ELIMINATION.md`.

The cover residue has a useful stable form.  With
`h=n/L^{5/2}`, the safe quarter bound gives

\[
  2\psi(\log h)-\Phi_3(L)
   ={1\over2}L\log L-L+{25\over8}(\log L)^2
      +{5\over2}\log L>0,                            \tag{3d3z11s5}
\]

so every cross-bad-four cover leaves fewer than `h` labels on one side.
Choose maximal circuit matchings between `t=Theta(L)` large classes and
orient each pair toward an almost-covered side.  A tournament vertex has
`d>=(t-1)/2` out-neighbours, and the corresponding matchings cover one
common physical core of size

\[
              |Y^*|\ge g-dh=(1-o(1))g.               \tag{3d3z11s6}
\]

Every core label lies in a unique matching circuit against every one of
those partners.  Recording the class occupancy, hidden-point class, and
whether the core label is hidden uses at most `R=12` types.  For every
`k<=d/(2R)`, double counting type-constant partner subsets yields a fixed
`k`-set `I`, one signed type, and

\[
       |Y'|\ge {|Y^*|\over R(2R)^k},
       \qquad \chi(y,j)=\chi_0\quad(y\in Y',j\in I). \tag{3d3z11s7}
\]

Thus `k=Theta(log L)` leaves a near-ambient core and produces synchronized,
label-disjoint circuit matchings of one physical type.  It still does not
make sibling indices independent: the remaining geometric atom is a
first-incoherent-sibling bank, a common-edge circuit elimination, or a
rich-face incidence theorem on this array.  See
`agent_root_followup/STABLE_CROSS_CIRCUIT_TOURNAMENT_CORE.md`.

There is already an exact three-class payment in the reused-pair part of
the `2+2` occupancy branch.  Make a graph whose vertices in class `i` are
physical pairs in `binom(Y_i,2)`, and whose `ij` edges are the selected bad
pair-union circuits.  A tripartite triangle uses six labels.  Each of its
three pair unions is bad, while double counting the fact that every five
planar points contain an ordinary four-set forces at least three ordinary
`2+1+1` seams.  If physical pair-nodes have class-pair degree at most
`Delta`, these seams give

\[
                       V(P)\ge {3T\over\Delta^2};     \tag{3d3z11s8}
\]

for `T` auxiliary triangles.  For the label-disjoint matching inputs,
`Delta=1` and each seam decodes its triangle exactly.

The sharp escape is **pair reset**.  A rational twelve-point configuration
has a directed cycle of three bad class-pair circuits and a Boolean
four-label bank in every class, but uses a different physical pair against
each neighbour; the auxiliary graph is three disjoint edges.  Abstractly,
edge-disjoint one-factorizations give, for `t<=g`,

\[
 \begin{array}{c|c}
 \text{matching size for every class pair}&g/2\\
 \text{circuit occurrences per physical label}&t-1\\
 \text{degree of every physical pair-node}&1\\
 \text{pair-node triangles}&0 .
 \end{array}                                           \tag{3d3z11s9}
\]

This reset is now known to be fully planar and stretchable, not merely an
abstract itinerary.  For every `t>=2` and `m>=t-1` there is an exact
rational general-position configuration with `t` classes of size `2m`, a
size-`m` bad-`2+2` matching on every class pair, and

\[
 \begin{array}{c|c}
 \text{circuit occurrences per physical label}&t-1\\
 \text{degree of every physical pair-node}&1\\
 \text{pair-node triangles}&0\\
 \text{hidden label for }i<j&L_{j,a}.
 \end{array}                                           \tag{3d3z11s9a}
\]

The construction uses rational perturbations of `t` tangent lines to a
parabola and cyclic one-factorizations of each class's left--right labels.
It survives a projective nesting behind one common exposed edge `uv`, so
signed type, coherent radial order, and endpoint XOR still do not force a
reused physical pair.  Its ambient payment is explicit: every class is
Boolean, the cross-class convex `2+2` bank has exact size
`binom(t,2)m^2(m-1)(2m-1)`, and the canonical five-point releases give

\[
 V(P)\ge t(2^{2m}-1)
  +\binom t2m^2(m-1)(2m-1)
  +{2\over3}m^2(t-2)\binom t2.                         \tag{3d3z11s9b}
\]

At `N=2mt` and `t=Theta(log N)`, the first term alone has logarithm
`Omega(N/log N)`, far beyond the live `O((log N)^2)` budget.  Thus
planarity cannot prove partner reuse; the remaining low-face statement
must charge this ambient bank, or show that suppressing it creates a
recoverable chronology/profile seam.  High actual-pair reuse is already
closed by `(3d3z11s8)`.  See
`agent_common_shield_mixing/THREE_CLASS_PAIR_CIRCUIT_TRIANGLE_GATE.md` and
`agent_many_class_partner_reset/SCALABLE_STRETCHABLE_PARTNER_RESET_AND_FACE_AUDIT.md`.

The Boolean payment is not forced locally.  Every macro label of the
tangent construction can be replaced by an independently chosen rational
`D`-point order type, preserving all signed matchings, label load `t-1`,
fresh physical partners, zero pair-node triangles, and common-`uv` nesting.
Within one class the substituted cells do obey the exact strong-comb
recurrence

\[
 \begin{aligned}
 C(Y)&=\sum_iC_i\left(1+\sum_{j>i}n_j\right),\\
 U(Y)&=\sum_jU_j\prod_{k<j}(1+n_k),\\
 W(Y)&=\sum_iW_i+\sum_{i<j}C_iU_j\prod_{i<k<j}(1+n_k).
 \end{aligned}                                             \tag{3d3z11s9c}
\]

Stationary equal children therefore pay

\[
 W(Y)=qW(Q)+C(Q)U(Q){(1+D)^q-1-qD\over D^2};           \tag{3d3z11s9d}
\]

at the live `q=(1/3+o(1))log n` and quarter-scale child reservoir this has
coefficient `7/12>1/2`.  The sharp scalar escape is again a heterogeneous
endpoint ramp.  If `q=(alpha+o(1))log D` and the child profile product has
coefficient `c`, the max-plus optimum is exactly

\[
                              \max\{\alpha,c\};         \tag{3d3z11s9e}
\]

for `(alpha,c)=(1/3,1/4)` it is attained by
`x(t)=min(t,1/4)`.  More quantitatively, if all `W_i>=D^h` but
`W(Y)<=D^p`, then every `i<j` satisfies

\[
 \log_D C_j-\log_D C_i
   \ge h+(j-i-1)\log_D(D+1)-p.                         \tag{3d3z11s9f}
\]

Thus low face count forces an almost full endpoint gradient, but the reset
circuits do not forbid it.  The remaining theorem is precisely exclusion
or recursive payment of this actual heterogeneous ramp, not recovery of
the abstract partner itinerary.  See
`agent_many_class_partner_reset/LOW_FACE_SUBSTITUTION_AND_STRONG_COMB_RAMP.md`.

The exact separated tangent model is nevertheless globally paid by a
different cross-class bank.  Its full three-class words have **no**
ordinary `(1,1,1)` almost-full shadow when `m>=2`: any lower class retaining
both an `L` and an `R` cell and any higher rank-two trace contain a hereditary
bad `2+2` circuit.  But for every `i<j<k` the cell family

\[
                   L_i\cup L_j\cup(L_k\cup R_k)        \tag{3d3z11s9g}
\]

is a cup.  This sign is stable under arbitrary independent `D`-point child
substitutions and under the endpoint ramp, so its transversals give the
disjoint ordinary bank

\[
                         \binom t3D^{4m}.               \tag{3d3z11s9h}
\]

In fact the same determinant proof is global: all `L` cells in classes
`0,...,t-2`, together with all `2m` cells of the top class, form one cup.
Therefore

\[
                         V(P)\ge D^{m(t+1)}.             \tag{3d3z11s9j}
\]

At `N=2mtD` and `t,m~(log N)/6`, its logarithm is
`(1/36+o(1))(log N)^3`.  Thus the exact tangent reset is not merely above
one half: it is violently nonminimal, independently of its endpoint ramp.

After thinning to role lengths `(m,m,2m)`, the codimension-three ledger has

\[
 2m^3D^{4m}\ \hbox{incidences},\qquad
 2m^3D^{4m-3}\ \hbox{outputs},\qquad
 \hbox{load }D^3.                                      \tag{3d3z11s9i}
\]

Relative to the original full histories, erasing the two lower `R` halves
raises the load to `D^{2m+3}`.  Thus this is genuinely the source-thin
branch, but its empty-seam bank already has exponent `2/3+o(1)` at
`N=2mtD`, `t,m~(log N)/6`; it excludes a half-scale low parent without any
profile reset.  What remains possible is a nonseparated fresh-partner
itinerary lacking the uniform cross-class cup, or a nonempty seam that
cannot coexist with it.  See
`agent_many_class_partner_reset/CODIMENSION_THREE_TANGENT_SOURCE_SHADOW_AUDIT.md`.

The arbitrary stretchable reset has an exact support--chronology ledger.
Let every class pair carry a label-disjoint matching of `m` bad `2+2`
circuits, let global pair-node degree be one, and let each physical label be
used in at most `lambda` selected circuits.  If `d_i(x)` is the circuit
load of `x in Y_i`, then

\[
 \sum_{x\in Y_i}d_i(x)=2m(t-1),\qquad
 |Y_i|\ge {2m(t-1)\over\lambda}.                    \tag{3d3z11s9k}
\]

Moreover all five-point releases can be summed globally with decoder load
one.  For `Q` in the `ij` matching and `y in Y_k`, delete the first label
of `Q` making `(Q-z) union {y}` ordinary.  The doubled class trace recovers
the unique pair-node edge `Q`, and the third class recovers `y`; hence

\[
 V(P)\ge
 B_4:=m\sum_{i<j}\sum_{k\notin\{i,j\}}|Y_k|.         \tag{3d3z11s9l}
\]

This is the universal payment, but it is only polynomial.  Stretchability
does **not** force a long coherent endpoint transversal: put one shrunken
rational copy of the exact twelve-point colorful obstruction on every
class triple and every copy index, with gadget centres on a cup--cap
extremal macro set.  Then

\[
 m=r(t-2),\qquad |Y_i|=2m(t-1),\qquad \lambda=1,       \tag{3d3z11s9m}
\]

all physical labels and pair nodes have load one, yet every full endpoint
transversal is bad.  In fact an ordinary partial endpoint trace activates
only `O(log G)` of the `G=r binom(t,3)` gadgets and has rank `O(log G)`.
The exact `t=5,r=1` verifier has 120 rational points, 30 selected circuits,
60 pair nodes, partial endpoint rank at most 25, and 2,160 distinct releases
from `(3d3z11s9l)`.

Thus the broad allowable-sequence/Ramsey synchronization claim is false.
The sole reset regime not covered by this source-inflated construction is
the opposite endpoint: `|Y_i|=(1+o(1))2m`, where `(3d3z11s9k)` forces
almost every physical label to serve almost all `t-1` neighbouring
matchings.  The tangent reset lies there and is paid by `(3d3z11s9j)`.
The remaining reset theorem is therefore a stability statement for
near-perfect common-support/high-reuse matchings, not for arbitrary fresh
partners.  See
`agent_many_class_partner_reset/STRETCHABLE_RESET_LOAD_CHRONOLOGY_DICHOTOMY.md`.

Even exact common support and maximum label reuse do not force the tangent
cup.  There is a rational 252-point base, obtained on the classical
`E(7,7)` cup--cap set, with

\[
 t_0=14,\qquad |Y_i|=18=2m_0,\qquad m_0=9,             \tag{3d3z11s9n}
\]

such that every class pair has a perfect nine-circuit matching, every
label has load 13, and the global physical pair graph has degree one and no
triangles.  Yet the entire base has convex rank at most ten.  Its
lexicographic powers preserve the perfect reset and satisfy

\[
 t=14^h,\qquad |Y_i|=18^h=2m,\qquad d(x)=t-1,\qquad
 \Delta_{\rm pair}=1,\qquad
 R_C=R_U=5h+1,\qquad R_W=10h.                         \tag{3d3z11s9o}
\]

Fresh pair nodes are maintained by suffix-dependent cyclic shifts; the
physical pair itself decodes the neighbour class.  The exact verifier
constructs all 252 rational points, checks 2,635,500 triple states, all 819
base circuits, and 31,590 fresh pair nodes incident with one class at the
second power.

Thus the tangent implication is false even at the exact high-reuse
endpoint, and the monotone-partner fan does not repair it.  The exact rank
is much smaller than the earlier loose `10^h` bound: recursive separated
composition shows that every spanning face has only a cap trace in its
left endpoint cell, a cup trace in its right endpoint cell, and singleton
traces elsewhere.  After replacing each final macro label by a `D`-point
child, the flattened profiles are

\[
\begin{aligned}
 C(P)&=\sum_iA_i(D)C_i,\qquad
 U(P)=\sum_jB_j(D)U_j,\\
 W(P)&=\sum_iW_i+\sum_{i<j}K_{ij}(D)C_iU_j,           \tag{3d3z11s9p}
\end{aligned}
\]

where the degree maxima are `5h,5h,10h-2`.  There is no additional
non-`x` projection reset.  The sharp scalar relaxation is governed by the
four-state max-plus Bellman recurrence

\[
 M_T^{ab}=\max\{M_A^{ab}+b,\ M_B^{ab}+a,
                 M_A^{a1}+M_B^{1b}-x\}.              \tag{3d3z11s9q}
\]

At `D=2^L`, `14^h=L`, and local face budget `L^2/2`, its forced extra
parent logarithm is `Theta_h L`, with `Theta_h/h` between `4.7` and `5.1`
through the eight exact audited powers.  Hence it is

\[
                         \Theta(L\log L)=o(L^2).       \tag{3d3z11s9r}
\]

So multi-point profile arithmetic still does not force a coefficient
above one half.  This is not yet a sub-half planar construction: one must
realize the required many-level cap/cup ramp by genuinely low-face
`D`-point children.  Conversely, a positive proof must exclude or charge
that realizability; reset circuits, representative ranks, and alternative
projection chambers do not do so.  See
`agent_many_class_partner_reset/PERFECT_RESET_LEXICOGRAPHIC_ES_COUNTERREGRESSION.md`
and `agent_many_class_partner_reset/ARBITRARY_CHILD_ES_POWER_PROFILE_BELLMAN.md`.

The construction-side realization problem for that Bellman ramp is now
closed throughout the recursively separated template class.  Expanding
every nonstationary $E(r,s)$ cell, reflected cell, and perfect-reset power,
then grafting at the substituted leaves, produces one ordered full binary
strong-decomposition tree.  The weighted one-turn/reset theorem therefore
gives, for every such heterogeneous recursion,

\[
 \log V(P)\ge {1\over2}(\log |P|)^2
                    -O((\log |P|)^{3/2}).             \tag{3d3z11s9s}
\]

This is sharp within the class.  A fixed macro $S$ of size $m$, maximum
cap rank $a$, and maximum cup rank $b$ has stationary tropical coefficient

\[
 \kappa(S)={a+b-2\over2\log m}\ge {1\over2},          \tag{3d3z11s9t}
\]

because the cup--cap theorem gives $m\le2^{a+b-2}$; balanced $E(k,k)$
macros satisfy

\[
 {k-2\over\log\binom{2k-4}{k-2}}\downarrow {1\over2}. \tag{3d3z11s9u}
\]

The exact nonstationary ledger retains the cap, cup, ordinary-face, and
support-rank polynomials at every level, so `(3d3z11s9s)` is not a scalar
profile relaxation.  Consequently the formal half-ramp can escape this
payment only through genuinely non-strong-decomposable child order types.
Pascal cells and perfect-reset powers cannot realize a sub-half recursive
construction.  See
`agent_many_class_partner_reset/RECURSIVE_ES_RAMP_HALF_CLOSURE.md`.

A genuinely non-strong macro confirms that this conclusion is not merely a
strong-tree artefact, but also identifies the exact missing extension.  An
integral eight-point order type is nondecomposable after exhausting all
$8!$ leaf orders and both mirror signs at every split.  Across all $56$
oriented projection chambers it has $47$ distinct endpoint profiles and

\[
 h(\xi):=\max_i\{\alpha_\xi(i)+\beta_\xi(i)\}\ge4,       \tag{3d3z11s9v}
\]

where $\alpha_\xi(i)$ is the maximum cap reward with macro minimum $i$ and
$\beta_\xi(i)$ is the maximum cup reward with macro maximum $i$.  For an
arbitrary finite chart/child-state grammar, following at each state one
position attaining `(3d3z11s9v)` produces a directed cycle, so the maximum
cap and cup cycle means obey $\rho_C+\rho_U\ge4$.  The exact heterogeneous
recurrence then gives

\[
 \liminf_d{\log V(Q_d)\over(\log|Q_d|)^2}\ge{2\over3}.   \tag{3d3z11s9w}
\]

This is sharp: a two-state grammar has endpoint reward matrices

\[
 M_C=\begin{pmatrix}2&3\\1&2\end{pmatrix},\qquad
 M_U=\begin{pmatrix}2&1\\3&2\end{pmatrix},              \tag{3d3z11s9x}
\]

both with maximum cycle mean $2$, and its exact integer face recurrence
converges to coefficient $2/3$.  Thus arbitrarily many states from this full
non-strong spectrum still cannot populate the half ramp.

The apparent generalization through split polygons is not valid: the
Baek--Balko paths share their **rightmost** endpoint, whereas the vertical
recurrence requires cap-minimum and cup-maximum rewards at the same block.
Nevertheless the required hinged threshold follows directly from the
classical cups--caps theorem.  For an arbitrary generic $x$-ordered
$m$-point set put

\[
 X_{p,q}=\{i:\alpha(i)=p,\ \beta(i)=q\}.
\]

The induced set $X_{p,q}$ has neither a $(p+2)$-cap nor a $(q+2)$-cup:
the leftmost vertex of the former would have full-set cap-minimum reward at
least $p+1$, and the rightmost vertex of the latter would have full-set
cup-maximum reward at least $q+1$.  Hence the exact cups--caps bound gives

\[
              |X_{p,q}|\le {p+q\choose p}.             \tag{3d3z11s9y}
\]

If $h=\max_i(\alpha(i)+\beta(i))$, summing the rank cells by Pascal
diagonals yields the universal hinged floor-log theorem

\[
 m\le\sum_{p+q\le h}{p+q\choose p}=2^{h+1}-1,
 \qquad h\ge\lfloor\log m\rfloor.                     \tag{3d3z11s9z}
\]

Choosing a maximizing position in every state of a finite common-arity
grammar and following the resulting functional digraph produces one
directed cycle on which the two rewards use the **same** transitions.
Consequently its cap and cup maximum cycle means satisfy

\[
                 \rho_C+\rho_U\ge\lfloor\log m\rfloor. \tag{3d3z11s9z1}
\]

The apparent one-bit residue is also removable.  For position $i$, merge
in increasing order the minimum last slopes of cups ending at $i$ and the
minimum first slopes of caps starting at $i$, encoding the two types by
$0$ and $1$.  If $i<j$ and $t$ is the slope of $ij$, let $x$ and $y$ be
the first cup and cap thresholds above $t$.  Appending $ij$ gives
$U_j(x)\le t<U_i(x)$, while prepending it gives
$D_i(y)\le t<D_j(y)$.  In the first $x+y-1$ symbols, the word at $i$
therefore has at most $x-1$ zeros whereas the word at $j$ has at least
$x$ zeros.  The sentinel definitions also give
$x\le\beta(j)$, $y\le\alpha(i)$,
$x-1\le\beta(i)$, and $y-1\le\alpha(j)$, so this distinguishing prefix
exists in both words.  The words are consequently prefix-free, and Kraft's
inequality gives the sharp universal strengthening

\[
              \sum_i2^{-\alpha(i)-\beta(i)}\le1,       \tag{3d3z11s9z2}
\]

and hence $h\ge\lceil\log m\rceil$.  This also closes variable-arity
finite grammars.  Regard every macro position as an edge of the
transition-count multigraph and put $\ell_e=\alpha_e+\beta_e$.  The rowwise
Kraft inequalities are

\[
                 \sum_{e\text{ out of }s}2^{-\ell_e}\le1. \tag{3d3z11s9z3}
\]

On a critical strongly connected component with Perron root $\Lambda$,
the explicit Parry edge law has entropy rate $\log\Lambda$.  Rowwise
cross-entropy and circulation decomposition therefore give one directed
cycle with mean $\ell$ at least $\log\Lambda$.  Hence
$\rho_C+\rho_U\ge\log\Lambda$, while $\Lambda$ is exactly the exponential
size-growth factor.  Thus **every finite transition grammar**, including
variable arities, parallel transitions, arbitrary nonstrong children, and
arbitrary finite chart menus, has recursive coefficient at least $1/2$.
Any construction-side escape must have genuinely growing state complexity
or leave the endpoint recurrence model.  Exact exhaustion of all
$25{,}679$ reflection-order commutation classes through $m=7$, all $720$
arbitrary edge orders at $m=4$, a stretchable eight-point equality example,
and an exact variable-arity Perron regression independently audit the sharp
statement.  See
`agent_nonstrong_ramp_search/HINGED_DIAGONAL_FLOOR_LOG.md`.

Growing chart complexity is not by itself an escape.  Consider a
nonstationary homogeneous substitution with level-$k$ arity $m_k$, common
child size $N_{k-1}$, $q_k=\log m_k$, and
$L_k=\log N_k=\sum_{j\le k}q_j$.  The macro, its order type, its chart menu,
and the chart transition map may all change at every level.  Assume only
that the cap and cup recurrences at a hinged position call the same child
chart, and that the final two-position splice calls one common chart.  If

\[
 E_k:=\min_{\theta}\{\log C_{k,\theta}+\log U_{k,\theta}\},
                                                               \tag{3d3z11s9z4}
\]

then row Kraft in every parent chart gives

\[
                    E_k\ge E_{k-1}+q_kL_{k-1}.           \tag{3d3z11s9z5}
\]

The minimum over charts is essential: it makes the induction valid even
when the menu grows and every transition is changed.  The final common-chart
cap--cup splice and exact telescoping now yield

\[
 \boxed{\log V_d\ge{1\over2}
   \left(L_{d-1}^2-\sum_{k<d}q_k^2\right).}             \tag{3d3z11s9z6}
\]

In particular, for $q_*=\max_{k\le d}q_k$,

\[
 \log V_d\ge {1\over2}L_d^2-{3\over2}q_*L_d+q_*^2.     \tag{3d3z11s9z7}
\]

Thus bounded arity gives a half lower bound with $O(L)$ error, and the
general mesh condition $q_*=o(L_d)$ gives coefficient $1/2-o(1)$, despite
arbitrarily nonstationary macros and unboundedly many charts.  The sharp
residue is heterogeneous child alignment.  For a two-position macro with a
$2^t$-point left child and a singleton right child, row Kraft is equality,
but the left-anchor outer multiplier is only $2$, not $2^t$.  Hence a
leaf-entropy martingale cannot replace sibling-weight incidence.  Any
extension must retain those sibling identities, produce a compatible
one-turn/Ferrers splice, or use an all-tree theorem.  See
`agent_nonstrong_ramp_search/NONSTATIONARY_HOMOGENEOUS_HALF_CLOSURE.md`.

For heterogeneous children there is now an exact martingale reduction.
At a node \(v\), write
\[
 N_v=\sum_i n_i,\quad p_i={n_i\over N_v},\quad
 \Delta_i=\log{N_v\over n_i},\quad \ell_i=\log n_i.       \tag{3d3z11s9z8}
\]
Let \(A_i\) and \(B_i\) be the maximum weighted cap and cup rewards at
position \(i\), where using sibling \(j\) contributes
\(\log(1+n_j)\), and put \(R_i=A_i+B_i\).  The exact local defect and jump
variance are
\[
 d_v=\left[\sum_i p_i\ell_i\Delta_i-\sum_i p_iR_i\right]_+,
 \qquad J_v=\sum_i p_i\Delta_i^2.                         \tag{3d3z11s9z9}
\]
For a uniform random leaf \(X\), the same-target recurrence telescopes to
\[
 \boxed{\log C_{\rm root}+\log U_{\rm root}\ge
 {1\over2}(\log N)^2
 -{1\over2}{\mathbb E}\sum_{v\prec X}J_v
 -{\mathbb E}\sum_{v\prec X}d_v.}                        \tag{3d3z11s9z10}
\]
Thus the half coefficient follows whenever both path sums are
\(o((\log N)^2)\).  In particular, active jumps
\(\Delta_i\le r=o(\log N)\) give
\({\mathbb E}\sum J_v\le r\log N\).  The first natural local candidate was
the zero-defect weighted-hinge inequality
\[
                    \sum_i p_iR_i\ge\sum_i p_i\ell_i\Delta_i. \tag{3d3z11s9z11}
\]
It is now **false**.  A generic integral stretchable five-point chart with
child sizes \((4250,1000,1000,1000,1000)\) has the rigorously certified
defect
\[
 \sum_i p_i\ell_i\Delta_i-\sum_i p_iR_i
       \in(0.00803,0.00804).                            \tag{3d3z11s9z12}
\]
Thus ordinary hinged Kraft and the exact weighted predecessor forests do
not force zero average defect.

The square-corrected statement needed by the deterministic Bellman route
survives.  The strongest currently tested averaged form is
\[
 \boxed{\sum_i p_i\left({1\over2}\ell_i^2+R_i\right)
 \ge {1\over2}(\log N)^2-{1\over2}(\log m)^2.}          \tag{3d3z11s9z13}
\]
Equivalently,
\[
 \sum_i p_iR_i-\sum_i p_i\ell_i\Delta_i
 \ge {1\over2}\left(J_v-(\log m)^2\right).              \tag{3d3z11s9z14}
\]
It implies the pointwise square-mesh Bellman inequality
\[
 \max_i\left\{{1\over2}\ell_i^2+R_i\right\}
 \ge {1\over2}(\log N)^2-{1\over2}(\log m)^2,           \tag{3d3z11s9z15}
\]
which the counterexample satisfies with margin greater than \(0.67\).
Both square statements survive the same \(1.49\) million exact arity-four
and reflection-order arity-five regressions, but remain conjectural.

Two simpler approaches are also closed.  An integral stretchable nonstrong
eight-point macro with child sizes \((128,1,\ldots,1)\) makes the
entropy-only surrogate require \(c>3.283858\ldots\).  And the proposed
nested-threshold uncrossing is false already on four stretchable points:
an induced two-vertex maximum cap need not be contained in the unique full
maximum cap.  Consequently the precise heterogeneous frontier is now
`(3d3z11s9z13)`/`(3d3z11s9z15)` plus control of the
accumulated \(\sum(\log m_v)^2\) mesh loss.  See
`agent_nonstrong_ramp_search/HETEROGENEOUS_WEIGHTED_HINGE_BARRIER.md` and
`agent_nonstrong_ramp_search/WEIGHTED_HINGE_FALSE_SQUARE_SURVIVES.md`.

Even without reused pairs, every single matching circuit has a canonical
quadratic extension bank.  For a bad four-set `Q` in an `AB` matching and
any `y in C`, the five-point theorem makes `(Q-z) union {y}` ordinary for
some `z in Q`.  Choosing the first such deletion is injective because the
third-class label and any retained matching label recover `Q`.  For three
class-pair matchings,

\[
 V(P)\ge H_A+H_B+H_C+
 {m_{AB}|C|+m_{BC}|A|+m_{CA}|B|\over3}.              \tag{3d3z11s10}
\]

The literal history form is
`sum_c m_c|C_c|<=Lambda_hist V`.  This is a real load-tracked mixed bank,
but only `Omega(g^2)`, not `m H_C`.  Rational configurations for every
`m` anti-align the two selected matching supports in each class while
keeping `m=g/4` disjoint circuits per class pair; even perfect abstract
support overlap can be a long cycle.  Thus matching density alone cannot
upgrade `(3d3z11s10)` to the rich-face product.  See
`agent_outer_internal_product/THREE_CLASS_CIRCUIT_MATCHING_EXTENSION_AND_ANTI_ALIGNMENT.md`.

The uniform central-hidden `1+3` type has a still sharper scalable planar
barrier.  For an arbitrary central child `Y={y_a}` and any number of
partner classes, choose record-specific triangles `T_j(a)` which strictly
contain `Y` and are totally nested.  Then

\[
 y_a\in\operatorname{int}\operatorname{conv}T_j(a),\qquad
 E_j(a)=\{y_a\}\cup T_j(a)                           \tag{3d3z11s11}
\]

is a label-disjoint matching for each `j`, but no ordinary face contains
two complete released triangles or one complete triangle plus any nonempty
central face.  Circuit elimination at a shared `y_a` stays on the six
record-specific triangle labels, so it creates no repeated root.  Both the
entire induced bank `F(Y)` and the complete-triangle records remain
load-one, yet they do not mix in one face.  This is not a low-face global
construction—singleton and edge traces of the triangles remain
uncontrolled—but it proves that the next theorem must use partial tangent
profiles/Hall load or exclude the all-loop nesting by minimality.  See
`agent_shield_circuit_cover/FIRST_INCOHERENT_SIBLING_NESTED_TRIANGLE_BARRIER.md`.

Endpoint bits do not supply that partial-profile theorem automatically.
There is an exact integral twelve-point reset, with two physical pair-nodes
per class and the cyclic three bad pair unions, for which all `2^6=64`
choices of one endpoint from every pair-node are nonordinary.  The hull-size
distribution is `(16,32,16,0)` at sizes `3,4,5,6`; four of the six
omit-one-pair banks are empty.  Its full face vector is
`(12,66,220,253,125,30,3)` and `V=709`, so the finite order type is paid
elsewhere rather than being a construction.  It exactly kills a colorful
endpoint-transversal repair of pair reset while leaving the reused-pair
triangle seams and canonical five-point extensions intact.  See
`agent_shield_circuit_cover/COLORFUL_PAIR_ENDPOINT_TRANSVERSAL_BARRIER.md`.

For the surviving nested `1+3` array, partial traces have an exact
load-one recurrence.  If `P_t=P_{t-1} dotcup T_t` and the new triangle
strictly contains the old set, put
`A_t(G)={F in F(P_{t-1}):F union G ordinary}`.  With the empty face
included and `Z_t=|F(P_t)|`, outermost-trace decoding gives

\[
 Z_t=Z_{t-1}+R_t+1,
 \qquad R_t=\sum_{\substack{G\subset T_t\\|G|=1,2}}|A_t(G)|. \tag{3d3z11s12}
\]

The map `(t,G,F)->F union G` is globally injective; a full triangle can
coexist only with the empty old face.  Hence, for
`rho_t=(R_t+1)/Z_{t-1}`,

\[
 {Z_s\over Z_0}=\prod_{t\le s}(1+\rho_t),\qquad
 \log{Z_s\over Z_0}=\sum_{t\le s}\log(1+\rho_t).     \tag{3d3z11s13}
\]

At the long-run scale `k=Theta(loglog n)`, `m=Theta(n/k)`, and
`s=km=Theta(n)`, induction from the central child requires exactly

\[
       \sum_{t\le s}\log(1+\rho_t)
          \ge(1+o(1))L\log\log L.                    \tag{3d3z11s14}
\]

Even perfect compatibility of all six traces with every **original**
central face supplies only `6sZ_0=O(n)Z_0`, so recursive retention of
earlier traces is essential.  The universal floor is merely polynomial:
a new singleton extends every old rank-at-most-two face, and a new edge
extends every old rank-at-most-one face.  Conversely an exact central
triangle face has zero compatibility with all 90 singleton/edge traces of
fifteen nested triangles.  Thus no pointwise Hall lower bound is possible;
the remaining assertion is precisely the aggregate minimizer/profile
potential `(3d3z11s14)`.  See
`agent_common_shield_mixing/NESTED_TRIANGLE_PARTIAL_TRACE_TELESCOPE.md`.

Restoring the whole nested array exposes three macroscopic vertex clouds,
but this improves the scale only to a fixed-power gap.  With `k` partner
classes of `m` triangles, write

\[
 N=m(1+3k),\qquad R=km={N\over3+1/k}.
\]

Each vertex position is an induced `R`-point face bank, so least-
counterexample induction gives the exact ambient floor

\[
 V(P)\ge V(Y)+\sum_{r=0}^2V(Z^r).                    \tag{3d3z11s15}
\]

For the corrected half target `F_C(x)=2^{\Phi_C(\log x)}`, this leaves

\[
 {F_C(N)\over F_C(R)}=N^{\log_2 3-o(1)},             \tag{3d3z11s16}
\]

not the earlier `n^{Theta(logloglog n)}` local deficit.  Canonical ES(5)
deletion also supplies an injective load-one bank of mixed rank-four
faces, giving

\[
 V(P)\ge V(Y)+\sum_{r=0}^2V(Z^r)+km(m-1),            \tag{3d3z11s17}
\]

but the final term is only quadratic and hence negligible.  Projecting
live source mass onto the complete-triangle records forces a
coefficient-half fibre load rather than a product with the cloud bank;
even the optimistic two-output Cauchy estimate is weaker than
`(3d3z11s15)`.  Moreover, granting a linear strong-glue recurrence does
not settle the fixed-power remainder: the exact coherent ramp
`H=B^h`, `C_i=B^{b+i}`, `U_i=B^{h-b-i}` has every cross term `H/B` and
`W_lin<=2kH`.  Thus the remaining assertion is genuinely an aggregate
one-face mixing/profile inequality, not a missing local trace count.  See
`agent_outer_internal_product/NESTED_TRIANGLE_LIVE_NORMALIZATION_AUDIT.md`.

The cloud banks in fact occur **inside** the singleton part of the exact
telescope.  Color \(T_t=\{x_{t,1},x_{t,2},x_{t,3}\}\) arbitrarily and let
\(b_{t,c}\) count cloud-\(c\) faces whose maximum layer is \(t\).  Deleting
that maximum label is a load-one injection into
\(\mathcal A_t(\{x_{t,c}\})\), whence

\[
 \sum_tb_{t,c}=V(X_c),\qquad
 \sum_{t,c}|\mathcal A_t(\{x_{t,c}\})|\ge\sum_cV(X_c). \tag{3d3z11s18}
\]

Thus the polynomial remainder cannot be blamed on failure to accumulate
earlier singleton traces.  For two clouds define \(\mathcal G_{ij}\) to
be the pairs of internal faces with ordinary union.  Physical color
supports make the union map injective, so either
\(|\mathcal G_{ij}|\) reaches the target or

\[
 {|\mathcal G_{ij}|\over V(X_i)V(X_j)}
       \le2^{-(1/2-o(1))L^2}.                            \tag{3d3z11s19}
\]

Every remaining bad cell contains, by planar four-locality, an actual
four-circuit meeting both clouds.  Hence the exact final local normal form
is an almost-complete face-by-face cross-circuit rectangle:

\[
 (F_i,F_j)\notin\mathcal G_{ij}\quad\Longrightarrow\quad
 \exists Q\subset F_i\cup F_j,\ |Q|=4,\ Q\text{ bad},
 \quad Q\cap F_i,Q\cap F_j\ne\varnothing.              \tag{3d3z11s20}
\]

What remains is bounded one-face payment for the projection reuse of
these physical circuit tags; the nested recurrence has already supplied
all free normalization.  See
agent_shield_circuit_cover/NESTED_TRIANGLE_VERTEX_CLOUD_FIXED_GAP_GATE.md.

There is an exact deletion-mask decoder for the bad rectangle.  For a
rank-at-most-\(q\) row family \(\mathcal A\subset\mathcal F(X)\) and any
column family \(\mathcal B\), repeatedly delete the first \(X\)-label in
a canonical surviving cross-circuit.  The terminal unordered mask
\(D\subset X\), together with the ordinary residual union, recovers the
literal pair; chronology is irrelevant.  Consequently

\[
 V(P)\ge {|\mathcal A||\mathcal B|\over
                 \sum_{t=0}^q\binom{|X|}{t}},\qquad
 V(P)\ge {E_{\ge s}\over
                 \sum_{t=0}^{q-s}\binom{|X|}{t}}.       \tag{3d3z11s21}
\]

For a uniform rank-\(q\) layer of density
\(\delta=|\mathcal A|/\binom Rq\), an \(N^{-o(1)}\) fraction terminating
with two row labels yields

\[
             V(P)\gtrsim \delta\,H\,{R^2\over q^{O(1)}}. \tag{3d3z11s22}
\]

Thus \(\delta\ge N^{-(2-\log_2 3)+\varepsilon}\) closes the fixed gap.
The exact survivor is support-sparse, or deletes almost every row to rank
zero or one.  Oppositely oriented parabolic clouds saturate the decoder:
every proper residual row remains bad, so the entire row is deleted.
Their Boolean cloud banks make this a sharp interface barrier rather than
a live low-face example.

The valid three-cloud profile statement is equally exact and equally
conditional.  If cloud \(i\) has recoverable directional profiles
\(A_i,R_i\), \(A_iR_i=H_i\sigma_i\), and every required cross-profile
rectangle is ordinary, then the three load-one gap banks obey

\[
 B_i=R_{i-1}A_{i+1},\qquad
 \max_iB_i\ge(H_1H_2H_3)^{1/3}
                 (\sigma_1\sigma_2\sigma_3)^{1/3}.      \tag{3d3z11s23}
\]

Hence this route needs geometric-mean surplus
\(n^{\log_2 3+o(1)}\); cap--cup injection alone supplies only
\(\sigma_i\ge1\).  Strict nesting does not supply the missing rectangular
seams.  An exact ten-triangle rational array has all \(6075\) cross-cloud
edge pairs ordinary but \(3600\) cyclic \(1+3\) records in which exactly
one partner is good and deletion plus the unused third vertex remains
bad; lexicographic blow-up preserves positive density.

Finally the aggregate telescope itself has the sharp restart inequality

\[
 S:=\sum_t\log(1+\rho_t)\ge
 \log\!\left(1+{3(F_C(R)-1)\over Z_0}\right).           \tag{3d3z11s24}
\]

Thus a genuinely small central \(Z_0\) forces the earlier
\((1-o(1))L\log\log L\) gain, while low \(S\) forces a macroscopic
central restart.  At that restart the exact marginal constraints permit
only
\[
                         S=(\log_2 3+o(1))L.            \tag{3d3z11s25}
\]
A verified formal model meets the deletion identity (mean rank about
\(L/2\)), all six trace floors, the three cloud injections, endpoint
factorization, and total-variation activity at equality.  It is not
claimed stretchable; it proves that the remaining gain must use actual
planar/minimizer coupling.  The nearby triangle-tag exponent
\(\log_2 3-3/2=0.0849625\ldots\) is illusory for face alphabets:
with demand \(e=H^2\), source size \(a=H\), and only
\(\binom n3\) physical tags, the local Cauchy premise would require
\[
                         H^3\le\Gamma n^3,              \tag{3d3z11s26}
\]
which fails exponentially.  Fixing a physical circuit leaves the
residual face alphabet unresolved.

Kruskal--Katona nevertheless removes support sparsity from the low-rank
part of this terminal rectangle.  Set

\[
 a=\log_2 3,
 \qquad \theta_*=2-a=0.415037499\ldots,
 \qquad \kappa_*={1\over a}=0.630929753\ldots .         \tag{3d3z11s27}
\]

If a largest live rank-\(q\) layer \(\mathcal A\) in an \(R\)-point
cloud has \(|\mathcal A|\ge F_C(R)/(R+1)\) and
\(q\le\kappa\log R\), the Lovasz form of Kruskal--Katona gives the
literal ordinary edge shadow

\[
                 |\partial_2\mathcal A|
                    \ge R^{1/\kappa}(\log R)^{-O_C(1)}.          \tag{3d3z11s28}
\]

Thus every fixed gap below
\(q=(\kappa_*-\varepsilon)\log R\) has a fixed-power surplus after
pairing this edge shadow with an opposite live cloud; failure of the
good-union bank canonically descends to a singleton--face \(1+3\)
terminal relation.  A literally small support is not a separate escape:
its complement retains \(F_C(R)R^{-o(1)}\) induced faces.  The literal
edge-shadow argument provisionally leaves the rank-heavy range
\(q>(\kappa_*-o(1))\log R\), or the all-delete terminal anti-alignment;
the higher-shadow descent below removes the former.

The third cloud gives the exact complementary density cutoff.  For
disjoint \(R\)-point clouds, every ordinary candidate
\(\{x,y\}\cup F\), with \(x\in X_1\), \(y\in X_2\), and
\(F\in\mathcal F(X_3)\), decodes the literal triple.  Its total candidate
capacity is

\[
              R^2F_C(R)=F_C(3R)R^{\theta_*-o(1)}.                \tag{3d3z11s29}
\]

Hence a good fraction \(R^{-\theta_*+o(1)}\) closes.  Otherwise canonical
four-circuits split the almost-complete bad rectangle into an endpoint
plus three labels of \(F\) (projection load exactly \(R\)), or both
endpoints plus two labels of \(F\) (a literal \(2+2\) codegree state).
Opposite parabolic clouds saturate both alternatives but are non-live
because their induced cloud banks are Boolean.  At this stage the endpoint
is a rank-heavy layer, or terminal \(1+3/2+2\) anti-alignment, not an
unquantified sparse-support case.

Generalized Kruskal--Katona removes even the rank-heavy **capacity**
exception.  Put \(R=2^d\).  If a largest layer
\(\mathcal A\subseteq\binom Xq\),
\(|\mathcal A|\ge F_C(R)/(R+1)\), has \(q>\kappa_*d\), then for every
fixed \(0<\eta<\kappa_*\), with
\(t=\lfloor(\kappa_* -\eta)d\rfloor\),

\[
 |\partial_t\mathcal A|
       \ge2^{((\kappa_* -\eta)/5)d\log d}
       =R^{\Omega_\eta(\log\log R)}.                    \tag{3d3z11s29a}
\]

The shadow times an opposite \(F_C(R)\)-bank therefore has
quasipolynomial surplus over \(F_C(3R)\).  Good unions close; otherwise
it is another almost-complete bad rectangle with first rank below
\(\kappa_*d\).  Hence the sole capacity endpoint is terminal
anti-alignment.  If the induced cloud law itself had mean \(O(d)\), a
stronger Markov--KK argument would produce a constant-rank shadow:
for \(q=\kappa d\),

\[
 t=\lceil2\kappa(\log_2 3+2\varepsilon)\rceil
 quad\Longrightarrow\quad
 |\partial_t\mathcal A|\ge R^{\log_2 3+\varepsilon}.    \tag{3d3z11s29b}
\]

The ambient mean cannot be substituted here: a cloud bank is only an
\(R^{-\log_2 3+o(1)}\) fraction of the ambient bank.  An exact symmetric
hereditary four-local module complex realizes target entropy
\(\Phi_C(d)+O(d)\), puts \(1-o(1)\) mass at any prescribed rank
\(\kappa d\), \(\kappa\in(\kappa_*,1)\), satisfies the exact per-vertex
deletion ratio, and allows three copies to be completely cross-bad.  It
is not stretchable; it proves the remaining step must use planar signed
rank-three circuit elimination, tangent coherence, or minimizer mutation,
not another scalar rank/downshadow estimate.

Nor can the cyclic surplus \(\sigma_\theta= C_\theta U_\theta/V\) be
made polynomial merely by optimizing the projection.  Its exact universal
lower bound is only \(\sigma_\theta\ge1\).  More sharply, take a rational
Pascal core \(Q_d=T(d,d/2)\) and shrink it inside a nearly regular
centrally symmetric convex shell of
\(K=\Theta(d^2)\) points.  Uniformly in every projection chamber, a cap or
cup meeting the core can use shell labels from only one quarter-chain.
Choosing \(K/4\ge\log M_d+3\log K+10\), where
\(M_d=\sum_{j\le d}\binom{|Q_d|}{j}\), gives

\[
 2^K-1\le V(P_d)\le2^KM_d,\qquad
 C_\theta(P_d),U_\theta(P_d)\le K^{O(1)}2^{K/2}.          \tag{3d3z11s30}
\]

Consequently, for \(N_d=|P_d|\),

\[
 V(P_d)=2^{\Theta((\log N_d)^2)},\qquad
 \sup_\theta{C_\theta(P_d)U_\theta(P_d)\over V(P_d)}
       \le(\log N_d)^{O(1)}=N_d^{o(1)}.                 \tag{3d3z11s31}
\]

The shell is itself a detached Boolean bank and has maximum face rank
\(\Theta((\log N)^2)\), so this is not a live counterexample.  It does
rule out the unconditional endpoint-surplus shortcut: a surviving
positive theorem must use the rank-\(O(\log N)\) live slice or otherwise
tie endpoint entropy to the physical cloud rather than an exterior shell.

There is an exact rank-sensitive refinement in every fixed generic chart.
If \(c_e,u_e\) count cap and cup chains with the same ordered extreme
pair \(e\), then

\[
 C=\sum_ec_e,\qquad U=\sum_eu_e,\qquad V=\sum_ec_eu_e,
 \qquad
 {CU\over V}\ge{V\over\max_ec_eu_e}.                  \tag{3d3z11s31a}
\]

If all faces have rank at most \(r\), a fixed endpoint fibre has size at
most \(B(N,r)=\sum_{j=0}^{r-2}\binom{N-2}{j}\), whence

\[
                  {CU\over V}\ge {V(P)\over B(N,r)}.    \tag{3d3z11s31b}
\]

This closes every near-capacity rank slice satisfying
\(V(P)\ge N^{\log_2 3+\varepsilon}B(N,r)\).  Bare
rank \(O(\log N)\), however, is false in a prescribed chart.  The rational
strong glue

\[
 A_t=T((11/20)t,3(11/20)t/4)\prec B_t=T(t,t/4)          \tag{3d3z11s31c}
\]

has maximum rank \((1.910566+o(1))\log N\), face entropy
\((0.829140+o(1))(\log N)^2\), yet in its construction chart

\[
                    {CU\over V}\le N^{1.55+o(1)}
                                  <N^{\log_2 3}.         \tag{3d3z11s31d}
\]

It is stretchable but already far above the half benchmark, so it is an
interface barrier rather than a minimizer counterexample.  The unresolved
endpoint statement is now specifically optimization over projection
chambers, or a compatible common-edge rechart; a frozen-chart theorem
cannot suffice.

That direction optimization is now exact for this barrier, but does not
yet close it asymptotically.  For
\(T(4,3)\prec T(8,2)\), exhaustive enumeration of all 968 projection
chambers gives

\[
 \min_\theta\log_N{C_\theta U_\theta\over V}=1.5457707\ldots,
 \qquad
 \max_\theta\log_N{C_\theta U_\theta\over V}=1.8046995\ldots.
                                                        \tag{3d3z11s31e}
\]

The diagonal chamber is therefore useful finitely, but a general
reverse-internal shuffle has an exact weighted endpoint-interval form.  If
\(P=A\prec B\), \(\ell_A(z),r_A(z)\) count the \(A\)-labels before and
after \(z\), and
\(\Gamma_{\mathcal U(B)}(p,q)=\sum_{S\in\mathcal U(B)}
p(\max S)q(\min S)\), then

\[
\begin{aligned}
 C_\theta(P)&=U(A)+U(B)+\Gamma_{\mathcal U(B)}(\ell_A,1)
             +\Gamma_{\mathcal U(B)}(1,r_A)
             +\Gamma_{\mathcal U(B)}(\ell_A,r_A),\\
 U_\theta(P)&=C(A)+C(B)+\Gamma_{\mathcal C(A)}(\ell_B,1)
             +\Gamma_{\mathcal C(A)}(1,r_B)
             +\Gamma_{\mathcal C(A)}(\ell_B,r_B).
                                                        \tag{3d3z11s31f}
\end{aligned}
\]

Every mixed diagonal cap uses at most two \(A\)-labels, and every mixed
cup at most two \(B\)-labels, so

\[
 C_\theta(P)\le U(A)+(1+a+a^2)U(B),\qquad
 U_\theta(P)\le C(B)+(1+b+b^2)C(A).                  \tag{3d3z11s31g}
\]

Consequently the diagonal reset has no new quadratic exponent; its finite
gain is polynomial.  In a separated chamber the exact alternative is

\[
\begin{aligned}
 C_\theta(P)&=C_\theta(A)+C_\theta(B)
     +|\mathcal C_A^\uparrow|\,|\mathcal U_B^\downarrow|,\\
 U_\theta(P)&=U_\theta(A)+U_\theta(B)
     +|\mathcal C_A^\downarrow|\,|\mathcal U_B^\uparrow|.
                                                        \tag{3d3z11s31h}
\end{aligned}
\]

This converts the remaining spectrum question into synchronized weighted
inversion mass.  It also has a sharp physical-edge exit: if \(J_A(u,v)\)
natural caps cross their first large adjacent-swap jump at the edge
\(uv\), common-edge dilution gives

\[
 \sup_\theta{C_\theta U_\theta\over V(P)}
          \gtrsim {J_A(u,v)N^2\over C(A)}.             \tag{3d3z11s31i}
\]

Losing half the mass in the first \(K\) swaps therefore pays
\(\gtrsim N^2/K\); all
\(K\le N^{2-\log_2 3-o(1)}\) jumps close.  The sole survivor is diffuse,
coherently anti-aligned endpoint-interval mass, not an arbitrary unknown
projection spectrum.

The Pascal recurrence itself does not realize that survivor.  There is an
explicit rational lex-seam gauge of
\[
 A=T(11t/20,33t/80)\prec B=T(t,t/4)
\]
whose diagonal projection follows reverse binary-prefix order.  Three
literal prefix rectangles give
\[
 C_\theta(P)\ge |G_A|\,U(B),\qquad
 U_\theta(P)\ge |G_B^-|\,|G_B^+|\,C(11t/20-1,33t/80).
                                                        \tag{3d3z11s31j}
\]
The needed polynomial-scale cap ratio is exact: for fixed \(y\in(0,1)\),
\[
 \log {C(d-1,yd)\over C(d,yd)}
    =-K(y)d+o(d),\qquad
 K(y)={-\ln(1-y)-y\over\ln2}.                          \tag{3d3z11s31k}
\]
Stirling and the dominant Pascal path then give
\[
 \sup_\theta{C_\theta(P_t)U_\theta(P_t)\over V(P_t)}
     \ge N_t^{1.6689662610\ldots-o(1)}
     >N_t^{\log_2 3+0.08}.                             \tag{3d3z11s31l}
\]
The exact integer bank already crosses \(\log_2 3\) at \(t=240\).
This is gauge-specific, not a projection-uniform theorem.  It proves that
Pascal cap recurrence is not the obstruction: a survivor must exploit
cross-wall gauge freedom to commute disjoint swaps and prevent the three
prefix banks from coexisting in one chamber.

The correct cross-wall statistic is a bottleneck path, not the minimum over
isolated shuffles.  For the exact finite pair
\(A=T(4,3),B=T(8,2)\), the \(35960\) reverse-internal shuffles include a
pointwise minimum
\[
 (C,U)=(83100,2835),\qquad
 \log_{32}{CU\over V}=1.5419638968\ldots<\log_2 3.     \tag{3d3z11s31m}
\]
Yet dynamic programming on the Young lattice of adjacent \(BA\mapsto AB\)
swaps proves the sharp minimax identity
\[
 \min_{\Pi}\max_{W\in\Pi}C(W)U(W)=491676585,\qquad
 \log_{32}{491676585\over V}=1.7542520037\ldots .      \tag{3d3z11s31n}
\]
An exact \(112\)-swap path attains it.  Thus the finite pair has a genuine
wall-sweep reset even though projection-uniform pointwise surplus is false.

The one-rectangle proof of an asymptotic reset is nevertheless false.  If
\(m_{d,k}(z)\) is the minimum-endpoint distribution of natural Pascal caps
and \(S_{d,k}(q)=\sum_{z\ge q}m_{d,k}(z)\), the exact rooted tail recursion
gives, uniformly for \(k/d\in[3/4,1-o(1)]\),
\[
 \max_q {qS_{d,k}(q)\over C(d,k)}
       \le2^{O(\sqrt d\log d)}.                       \tag{3d3z11s31o}
\]
A rational row-by-row wall zipper therefore keeps the complementary
weighted inversion factors below
\[
        (m+n)2^{O(\sqrt d\log d)}.                    \tag{3d3z11s31p}
\]
For the live \(11t/20\) versus \(t\) Pascal pair this supplies normalized
surplus exponent only \(1.244516\ldots\), below both \(\log_2 3\) and the
corner value \(1.55\).

The two incomparable middle rectangles do, however, synchronize.  If
\(X_1X_2\) is the companion transform on \((B_R,A_R)\) and \(Y_1Y_2\)
the zipper transform on \((B_L,A_L)\), the exact endpoint factorization is
\[
 {C(W)U(W)\over C(A)U(B)}
   \ge2^{-o(t)}X_1(W)X_2(W)Y_1(W)Y_2(W).             \tag{3d3z11s31q}
\]
The convex-envelope companion-floor theorem gives, in every chamber,
\[
 X_1(W)X_2(W)\ge |A_R|\,2^{-o(t)},
\]
while the full sweep and the rooted-tail theorem force some \(W_*\) with
\[
 Y_1(W_*)Y_2(W_*)\ge
 2^{\{H_2(1/4)+11/(80\ln2)\}t-o(t)}.
\]
Consequently every reverse-internal Young path has a chamber satisfying
\[
 {C(W)U(W)\over V(A\prec B)}
  \ge N^{1+11/20+11/(80\ln2\,H_2(1/4))-o(1)}
  =N^{1.7945161063\ldots-o(1)}
  >N^{\log_2 3+\varepsilon}.                         \tag{3d3z11s31r}
\]
This is independent of the realizable wall schedule and closes the exact
opposite-density Pascal cross-wall escape.  It is not yet a global
half-bound: one must still promote a low-count minimizer to these two
dominant endpoint modules in one reverse-internal interval.  Fixing the
varying opposite endpoint would lose the very factor preserved by the
companion floor.

The synchronization argument has an exact abstract form.  For a normalized
endpoint distribution \(w\) on ordered rows, let
\(W(q)=\sum_{i\ge q}w_i\), let \(\underline W\) be its greatest convex
minorant, and define
\[
 F_m(w)=\min_x(1+x)\{1+m\underline W(x)\},\qquad
 G_m(w)=\max_{0\le a\le mr}(1+a/m)
                     \{1+m\underline W(a/m)\}.          \tag{3d3z11s31s}
\]
If two incomparable inversion rectangles \(X,Y\) satisfy the pointwise
factorization \(CU/H\ge\Delta\mathcal I_X\mathcal I_Y\), and the sweep is
complete on \(Y\), then
\[
                 \max_W{C(W)U(W)\over H}
                    \ge\Delta F_{m_X}(w_X)G_{m_Y}(w_Y). \tag{3d3z11s31t}
\]
In particular a harmonic companion tail
\(W_X(q)\ge(1/[L(1+q)]-1/m_X)_+\) and one peak witness
\(W_Y(q_0)\ge\eta\) give the explicit lower bound
\[
                 {\Delta m_Xm_Yq_0\eta\over8L}.         \tag{3d3z11s31u}
\]
This is the minimal robust content of the Pascal proof: ordinary
log-convexity of the endpoint atoms is neither necessary nor sufficient.

The currently localized coherent-ramp modules fail this theorem at exactly
the companion floor.  They fix one physical endpoint pair, so the external
row distribution is a delta atom and \(F_m=2\).  Even the exact geometric
weights \(w_i\propto2^{-i}\), realized by a rational cap chain, have only
\(F_m=O(\log m)\).  A rational circle module can put more than one quarter
of all faces on one endpoint pair while retaining only polynomial
\(CU/H\); its ambient Boolean complex pays, so it is a sharp local rather
than global regression.  Thus physical endpoint localization plus
log-convexity cannot extend \((3d3z11s31r)\).  The missing input is a
minimizer/global-load theorem forcing a harmonic tail in the actual wall
order or charging concentration to an ambient shield.  See
`agent_shield_circuit_cover/GENERAL_FERRERS_COMPANION_FLOOR_AND_ENDPOINT_BARRIER.md`.

The fixed-pair delta atom does admit an exact **local** prefix opening.
Fix a uniform-rank endpoint family of size \(H\), follow a maximum-child
prefix trie, and write \(m_j\) for the node mass and
\(h_j=m_j/m_{j+1}\).  Then
\[
                         \prod_{j<s}h_j=H.              \tag{3d3z11s31u1}
\]
After omitting the root and the common prefix, the next physical endpoint
has maximum conditional atom \(1/h_j\), in every wall order.  Its tail
therefore satisfies \(W(q)\ge(1-q/h_j)_+\), so against an \(M\)-column
Ferrers rectangle the companion floor is at least
\[
                         1+\min\{M,h_j\}.               \tag{3d3z11s31u2}
\]
The same prefix is an actual rooted Boolean shield of size \(2^j\).
Consequently
\[
 \max_{j<s}\max\{h_j,2^j\}
 \ge2^{(\sqrt{1+4\log H}-1)/2}.                         \tag{3d3z11s31u3}
\]
Thus quadratic local entropy and rank \(O(\log n)\) force a fixed-power
endpoint floor or shield after peeling only \(O(\log n)\) labels.

The conditioning factors cannot be discarded.  For the rational circle
family of all \(s\)-subsets of \(2s\) cap labels,
\[
 H={2s\choose s},\qquad m_j={2s-j\choose s-j},\qquad
 h_j={2s-j\over s-j},\qquad
 \max_j{m_j\over H}h_j=2.                              \tag{3d3z11s31u4}
\]
Its last forced prefix shield is only \(2^{s-1}=H^{1/2+o(1)}\).
Hence prefix entropy alone gives no \(Hn^\varepsilon\) one-face gain: the
erased cap tail must be recovered by a compatible external context or a
second Hall/Cauchy output.  The remaining statement is aggregate and
load-sensitive, not another local endpoint inequality.  See
`agent_shield_circuit_cover/FIXED_ENDPOINT_PREFIX_PEELING_COMPANION_OR_SHIELD.md`.

That aggregate routing is now exact.  At a depth-\(j\) node of record mass
\(W_j\), expand by all \(S\subseteq K_j\).  Each expanded record has the
two ordinary targets
\[
                    A=C,\qquad F=B\cup U\cup S,
\]
so, with the literal Hall, shield, and ordered-pair loads,
\[
             2^jW_j\le
       \min\{\eta_jV,\lambda_jV,\delta_jV^2\}.            \tag{3d3z11s31u5}
\]
Along one maximum-child path, put
\[
 \alpha_j={W_j\over W_0},\qquad
 \mathfrak B=\sum_j2^j\alpha_j .
\]
Then
\[
 W_0\mathfrak B\le
  \min\{\eta_\Sigma V,\lambda_\Sigma V,\delta_\Sigma V^2\}.      \tag{3d3z11s31u6}
\]
The pair \((A,F)\) recovers the prefix subset and all fixed roles; only
depth/history remains, giving
\[
                         \delta_\Sigma\le R\delta_{\rm hist}.     \tag{3d3z11s31u7}
\]
Thus a high branch is a dense graph of **actual cap sources** and **actual
rooted shield faces**, not merely chronology names.

This is sharp at half scale.  Take \(a=L\) binary cap roles and
\(b=L/2\) roles of size \(D\asymp n/L\).  The cap-word family has
\[
 \log H=\tfrac12L^2-\tfrac12L\log L+O(L),\qquad
 R=(3/2+o(1))L,                                      \tag{3d3z11s31u8}
\]
but its maximum-child path satisfies
\[
             \max_j\alpha_jh_j\le2,\qquad
             \mathfrak B=L+\sum_{k<b}(2/D)^k=O(L).     \tag{3d3z11s31u9}
\]
It is rationally stretchable with near-uniform role mass and fixed-pair
surplus one.  Convex large children pay ambient Boolean banks; arbitrary
low-face children restore the coherent-ramp problem.  Hence trie/Hall
aggregation alone cannot supply the quasipolynomial gain.  The remaining
operation is either a small true history decoder, a mixed bank from the
dense source--shield core, or an internal profile theorem for the large
roles.  See
`agent_shield_circuit_cover/PREFIX_SHIELD_TWO_TARGET_HALL_AGGREGATE_GATE.md`.

The double-bad endpoint decoder and the prefix expansion can be combined
without pretending that their two faces merge.  For a record
\(r=(A,B,y,z)\), put
\[
 X_r=A\cup B,
 \qquad Y_r=\{a_*(A,y),y,z,b_*(B,z)\}.
\]
Both are ordinary and the ordered pair recovers \(r\).  If \(M\) is record
mass, \(\kappa,\lambda\) are the two marginal loads, \(\delta=1\) is the
pair load, and \(Q_4\) is the number of available seam faces, exact
fractional Hall gives
\[
 M\le\min\left\{\kappa V,\lambda Q_4,\delta VQ_4,
 {\kappa\lambda\over\kappa+\lambda}(V+Q_4)\right\}.    \tag{3d3z11s31u10}
\]
The harmonic load is sharp for complete biregular incidence graphs.
Writing \(\Sigma=CU/V\) and \(M\ge\theta\Sigma V\), the closure threshold is
\[
 \theta\Sigma\le\min\left\{\kappa,{\lambda Q_4\over V},
 \delta Q_4,{\kappa\lambda\over\kappa+\lambda}
                    \left(1+{Q_4\over V}\right)\right\}.       \tag{3d3z11s31u11}
\]
Thus the load-one pair decoder is insufficient at the half fixed gap unless
one actual marginal becomes subpolynomial.

A prefix shield supplies a third ordinary target
\(Z_{r,S}=B\cup S\), but it remains separated:
\[
 X_r\cup Z_{r,S}=X_r,\qquad
 X_r\cup Y_r\notin\mathcal F(P),\qquad
 Y_r\cup Z_{r,S}\notin\mathcal F(P).                 \tag{3d3z11s31u12}
\]
For total expanded mass \(E\), marginal loads \(K_X,K_Y,K_Z\), pair
loads \(\Delta_{XY},\Delta_{XZ},\Delta_{YZ}\), and triple load
\(T_{XYZ}\), one has the exact three-target ledger
\[
\begin{aligned}
E\le\min\{&K_XV,K_YQ_4,K_ZV,
 (K_X^{-1}+K_Y^{-1}+K_Z^{-1})^{-1}(2V+Q_4),\\
 &\Delta_{XY}VQ_4,\Delta_{XZ}V^2,\Delta_{YZ}VQ_4,
 T_{XYZ}V^2Q_4\}.
\end{aligned}                                                   \tag{3d3z11s31u13}
\]
The triple target decodes a fixed-node expansion, but
\(\Delta_{XY}\ge2^j\): the old pair erases the prefix subset and exactly
cancels its multiplier.

Even the literal two-sided merge has an exact profile obstruction.  For
\(S\subseteq A,T\subseteq B\),
\[
 Y_r\cup S\cup T\in\mathcal F(P)
 \Longleftrightarrow
 S\cup\{a_*,y\}\in\mathcal C(L)
 \text{ and }T\cup\{z,b_*\}\in\mathcal U(R).          \tag{3d3z11s31u15}
\]
Opposite far-guard parabola children can make each factor contain only one
actual profile although the two formal prefix cubes have \(2^{2m}\)
choices.  Thus a useful merged target needs internal profile mass, not only
downface entropy.

This threshold is exponent-sharp.  For balanced rational substitutions
\(P=Q_{k,d}\prec Q_{k,d}\), almost all endpoint pairs are double-bad,
all relevant ranks are \(O_k(\log N)\), and
\[
 \theta=1-o(1),\qquad \Sigma=\Theta(N^2),\qquad
 \kappa=(1-o(1))N^2,\qquad {\lambda Q_4\over V}=\Omega(N^2),   \tag{3d3z11s31u14}
\]
while \(\log V/(\log(2N))^2\to1/2\).  The exact twelve-point audit has
\((M,p,q,\kappa,\lambda,\delta)=(3600,625,121,9,108,1)\).
In fact the full two-target graph has fractional Hall density
\[
 \eta_2\ge(1-o(1))N^2,
 \qquad \eta_3\ge\Omega(N^2\mathfrak B)                 \tag{3d3z11s31u16}
\]
after prefix expansion by \(\mathfrak B\), even when every \(X,Y,Z\)
target is allowed.  A fixed physical seam factors into two one-sided
fibres of coefficient tending to \(1/4\); their detached rectangle has
coefficient tending to \(1/2\).  This is the literal quarter-by-quarter
square-root obstruction.
Hence the remaining fixed-gap operation is precisely a subpolynomial
bound on one actual source, seam, shield, or pair projection load using
minimum-cell/tangent history; neither the circuits nor the prefix trie
imply it.  See
`agent_shield_circuit_cover/DOUBLE_BAD_PREFIX_HALL_THRESHOLD_AND_HALF_BARRIER.md`.

Merging **both** one-sided prefix downsets is exact, but still does not
manufacture the missing logarithm.  For a double-bad record
`r=(A,B,y,z)`, marked seam `Y_r={a,y,z,b}`, and prefixes
`K subset A-{a}`, `J subset B-{b}`, put

\[
 \mathcal D^-_{a,y}(K)=\{S:S+\{a,y\}\text{ is a cap}\},\qquad
 \mathcal D^+_{z,b}(J)=\{T:T+\{z,b\}\text{ is a cup}\}.
\]

The strong-glue criterion gives the coefficientwise identity

\[
 Y_r\cup S\cup T\in\mathcal F(P)
 \Longleftrightarrow
 S\in\mathcal D^-_{a,y}(K),\ T\in\mathcal D^+_{z,b}(J),
 \qquad
 \Phi_{m merge}(t)=t^4C_{r,K}(t)U_{r,J}(t).          \tag{3d3z11s31u17}
\]

Thus for weighted surviving records the expanded mass is literally

\[
 E_{\rm merge}=
  \sum_{i,j}\sum_{r\in\Omega_{ij}}w_r c_r(i)u_r(j),   \tag{3d3z11s31u18}
\]

and the two ordinary targets `X_r=A_r union B_r` and `G_r(S,T)` obey

\[
 E_{\rm merge}\le
 \min\{K_XV,K_GV,2K_XK_GV/(K_X+K_G),\Delta_{XG}V^2\}. \tag{3d3z11s31u19}
\]

Requiring `S,T` to meet their last prefix roles makes both depths visible
and leaves only the actual history load in `Delta_XG`.  Nevertheless a
maximum-child path through `a` binary roles followed by roles of size `D`
has, even when both rooted downsets are complete,

\[
 \mathfrak B=a+\sum_{k<b}(2/D)^k\le a+2,\qquad
 \mathfrak B_L\mathfrak B_R=\Theta(L^2),              \tag{3d3z11s31u20}
\]

not the needed `L^3`.  A rational pair of blocker parabolas realizes the
complete-product case exactly while every full source remains double-bad.
With `a=L`, `b=floor(L/4)`, and `D=floor(2^L/L^6)` on each side,

\[
 \log_2M={1\over2}L^2-3L\log_2L+2L+O(L),\qquad
 \operatorname{rank}=O(L),\qquad
 \mathfrak B_L\mathfrak B_R=L^2+O(L).                 \tag{3d3z11s31u21}
\]

The unmarked `L^2` expansion is canceled by depth-pair load; the marked
load-one object is a **pair** of faces and only tests `V^2` capacity.
Hence multiplying the two maximum-child tries is a sharp two-logarithm
operation.  Any successful continuation needs superlinear branching on
one side, a smaller actual merged/history load, a third independent target,
or payment from the internal role-cloud profile.  See
`agent_outer_internal_product/TWO_SIDED_MERGED_DOWNFACE_MAXIMUM_CHILD_GATE.md`.

A third **linear** strong-glue block cannot supply the missing factor:
every intermediate occupied block has rank at most one, and its binary
aggregate is only `sum_(j>=0)(j+1)2^{-j}=4`.  A genuine common-ear third
cloud does produce the formal cubic product.  If its prefix downset is
also complete, then

\[
 E_{\rm cyc}=M\mathfrak B_1\mathfrak B_2\mathfrak B_3,
 \qquad
 (\text{complete source},\text{merged face})
 \text{ has depth-marked load one}.                    \tag{3d3z11s31u22}
\]

For three binary `q`-role tries the exact incidence and output counts are

\[
 M=2^{3q},\qquad
 E_{\rm cyc}=2^{3q-3}(q-1)^3,
 \qquad |\mathcal G_{\rm cyc}|=(2^{q-1}-1)^3.          \tag{3d3z11s31u23}
\]

The displayed count is correct for the **prefix-only** output alphabet,
but it is not a barrier in the complete-word geometry.  Retain the variable
source tails instead.  For a record `r` with three selected words `w_r^a`,
visible seam `Y_r`, and role sets `I_a`, suppose every almost-full union

\[
 O(r;i,j,k)=Y_r\cup(w_r^1-x_{r,i}^1)
                    \cup(w_r^2-x_{r,j}^2)
                    \cup(w_r^3-x_{r,k}^3)             \tag{3d3z11s31u24}
\]

is ordinary.  If `Delta_3` is the actual output load, incidence counting
gives the history-faithful one-face inequality

\[
 W|I_1||I_2||I_3|\le\Delta_3V,
 \qquad
 \Delta_3\le\Lambda_{\rm hist}
       \max_{i,j,k}|X_i^1||X_j^2||X_k^3|.              \tag{3d3z11s31u25}
\]

The output occupancy reveals the three omitted roles and retains every
other physical choice.  Thus three binary simple-history systems give
`V>=Wq_1q_2q_3/8`.  In the exact `q=3` rational cyclic blocker there are
`13,824` such incidences and `1,728` ordinary outputs, every one of load
exactly eight.  So the full-compatible-word construction is a positive
equality model, not a history-load counterexample.

At the fixed-gap scale the same blocker has

\[
 \log_2M={1\over2}L^2-3L\log_2L+3L+O(1),\qquad
 V\ge {ML^3\over8},                                      \tag{3d3z11s31u26}
\]

which is exactly the missing `K=3` multiplier.  The corrected survivor is
therefore narrower: a live rooted complex must be source-thin in at least
one component, or the almost-full outputs must have large physical
completion/history load.  The former exposes a first missing-label
blocker/profile record; the latter is the literal dense face--face core
from the Renyi/Hall reduction.  See
`agent_outer_internal_product/THIRD_CYCLIC_MERGED_DOWNFACE_HISTORY_LOAD_GATE.md`
for the corrected prefix calculation and
`agent_root_followup/HISTORY_FAITHFUL_CODIMENSION_THREE_SOURCE_SHADOW.md`
for the independent exact one-face audit.

This correction does not identify prefix branching with puncture
completion.  Let `G` be the weighted mass of ordinary almost-full omission
triples and `ell(O)` their actual output loads.  For every threshold `D`,

\[
 G_{\le D}\le DV,
 \qquad
 G_{>D}=G-G_{\le D}.                                  \tag{3d3z11s31u27}
\]

Consequently, if `G>=gamma Wq_1q_2q_3`, either

\[
 V\ge{\gamma Wq_1q_2q_3\over2D},                     \tag{3d3z11s31u28}
\]

or more than half this incidence mass has load above `D`.  If specifying
the three missing physical labels leaves history mass at most `lambda`, a
high-load output has a puncture-extension alphabet larger than
`(D/lambda)^{1/3}` in one component.  Restoring one such label maps to an
ordinary face with load at most `q_1+q_2+q_3`; if restoration is bad, exact
degree pruning leaves a literal high-minimum-degree face--face core.

The role forest alone does not make `D` small.  A complete `d`-ary cube has
perfect effective branching and `Q_eff=1`, but puncture degree `d` and
three-shadow load exactly `d^3`; a parity/MDS word family has the same early
prefix branching and puncture degree one.  The planar cyclic gadget realizes
the former sharply: at `q=2,d=3` it has `5,832` good incidences, `216`
outputs, and uniform load `27`.  At the half calibration
`q_1=q_2=q_3=L/6`, `d asymp n/L`,

\[
 W=d^{3q_1}=2^{(1/2-o(1))L^2},
 \qquad {V_{\rm shadow}\over W}={q_1^3\over d^3}
       =2^{-3L+O(\log L)}.                              \tag{3d3z11s31u29}
\]

Thus the corrected live fork is exact but still open upstream: prove
positive simultaneous almost-full mass and low puncture load, or charge a
source-thin first blocker, a physical puncture-extension star, or the dense
bad face--face core.  See
`agent_common_shield_mixing/CODIM_THREE_ROLE_FOREST_COMPLETION_GATE.md`.

For one ordinary source word `W_r` and one ordinary seam `Y_r`, the
source-thin branch has an exact four-local normal form.  Let `H_r` be the
inclusion-minimal word traces of bad four-circuits in `Y_r union W_r`.
Then every trace has rank at most three and

\[
 S\subseteq W_r,\qquad Y_r\cup S\text{ ordinary}
 \quad\Longleftrightarrow\quad
 T\not\subseteq S\quad(T\in\mathcal H_r).              \tag{3d3z11s31u30}
\]

Hence genuine one-label omissions have an all-or-three rigidity: all `q`
work when `H_r` is empty, while otherwise the working roles are
`cap_{T in H_r}T` and number at most three.  Let `tau_r` be the minimum
trace-cover number and `nu_r` a maximum disjoint-trace matching.  Since
`nu_r<=tau_r<=3nu_r`, deleting a canonical cover plus one tag gives
`q-tau_r` seam-retaining shadows, whereas deleting the first role of each
matching trace gives `nu_r` source-retaining shadows.  For weighted mass
`W_0`,

\[
 I_C+3I_B\ge qW_0,
 \qquad
 I_C\le\Delta_CV,\qquad I_B\le\Delta_BV.                \tag{3d3z11s31u31}
\]

With role alphabets at most `d`, completed-source load `Lambda_X`, and
completed `(Y,W)` load `Lambda_Y`, the literal completion bounds are

\[
 \Delta_B\le\Lambda_Xd,
 \qquad
 \Delta_C\le\Lambda_Y
   \max_{r,i\notin J_r}\prod_{j\in J_r\cup\{i\}}d_j.  \tag{3d3z11s31u32}
\]

Equivalently, at threshold `t`,

\[
 V\ge{(q-t)W_{\le t}\over\Lambda_Yd^{t+1}},
 \qquad
 V\ge{(t+1)W_{>t}\over3\Lambda_Xd}.                   \tag{3d3z11s31u33}
\]

These losses are sharp.  The rational two-arc downset has
`H=K_{k,k}`, `tau=nu=k`; for `q=6,d=4,M=4^6`, its blocker bank has
`12,288` incidences, `3,072` outputs, load `4`, while its cover-plus-tag
bank has the same incidences, only `48` outputs, and load `256`.  Pascal
all-delete is the singleton-edge extreme.  Thus the remaining exact gate
is intermediate cover entropy/large role completion, or actual-source
history load—not a missing abstract blocker count.  See
`agent_outer_internal_product/SOURCE_THIN_FOUR_LOCAL_BLOCKER_SHADOW_DICHOTOMY.md`.

The strong singleton-terminal branch has a rigid planar localization.
Fix an ordinary opposite face \(B\), and suppose
\(B\cup\{x\}\) is ordinary for every \(x\in A\), while
\(B\cup\{x,y\}\) is bad for every distinct pair.  Singleton ears on
nonadjacent boundary edges commute, so the insertion edges of all labels
of \(A\) lie in at most two adjacent cells of \(B\) (three when \(B\) is
a triangle).  If a rank-\(q\) terminal layer has density \(\delta\), a
container carrying an \(\eta\)-fraction of it has physical support \(p\)
satisfying

\[
 p\ge(R-q+1)\left({\eta\delta\over |B|}\right)^{1/q}.   \tag{3d3z11s32}
\]

At \(q=(\theta+o(1))\log N\) and
\(\delta\ge N^{-(2-\log_2 3)+\varepsilon}\), Lovasz--Kruskal--Katona
then gives \(N^{2-o(1)}\) actual bad pairs inside one same-edge or
adjacent-edge cell.  Thus a strong terminal column is a dense physical
dominance/circuit tensor, not an arbitrary face-alphabet residue.

Planarity alone still cannot release that tensor.  Given any finite
general-position child \(Q=\{(a_i,b_i)\}\), the orientation-preserving
affine placement

\[
 (a_i,b_i)\longmapsto
 p_i=(\varepsilon a_i,1+3\varepsilon a_i+\varepsilon^2b_i)       \tag{3d3z11s33}
\]

inside the common ear cell of
\(u=(-1,0),v=(1,0),w=(0,-3)\) preserves its entire labelled order type
and makes the tangent coordinates of the \(p_i\) a strict dominance
chain.  Consequently

\[
 \{u,v,w\}\cup S\text{ is ordinary}\quad\Longleftrightarrow\quad
 |S|\le1.                                                       \tag{3d3z11s34}
\]

This is projectively universal and survives arbitrary named cloud
partitions.  It can be amplified against every face in any fixed-edge
carrier alphabet, with no chronology artefact.  The transparent lower
parabola carrier of \(p\) convex labels pays elsewhere exactly through

\[
 H=2^p-1,\qquad U=H,\qquad C=p+\binom p2,\qquad
 {CU\over H}=\Theta(p^2)>p^{\log_2 3}.                           \tag{3d3z11s35}
\]

Hence the remaining assertion is narrower than circuit elimination:
a live, rank-safe, **low-endpoint-surplus** fixed-edge carrier cannot
support this universal common-edge cage without a mixed/shield bank.  The
localization is for the strong all-pair terminal state, not merely one
chosen deletion path.

For a genuinely common physical carrier edge, the critical density is
exact.  If \(\mathcal H\) is a family of \(H\) faces on a \(p\)-label
support, all retaining the same exposed edge \(uv\) on the same side, one
projective chart (fixed by \(uv\), independent of the face) makes every
member of \(\mathcal H\) a cap.  Every pair is a cup, so

\[
                {CU\over V}\ge {H\over V}\binom p2.     \tag{3d3z11s36}
\]

With \(\vartheta=2-\log_2 3\), this gives the sharp implication

\[
 {H\over V}\ge p^{-\vartheta+\varepsilon}
   \quad\Longrightarrow\quad
 {CU\over V}\ge {1\over3}p^{\log_2 3+\varepsilon}.      \tag{3d3z11s37}
\]

Thus rank is irrelevant inside a dense common-edge fibre: low endpoint
surplus forces the exact critical dilution
\(H/V\le p^{-\vartheta+o(1)}\).  This does not pay for choosing one edge
among \(\Theta(p^2)\) face-dependent possibilities, and the bare
inductive comparison permits the still smaller density
\(p^{-\log_2 3+o(1)}\).

The adjacent-cell complement is also exact.  If ears \(x,y\) insert at
\(uz,zv\), respectively, then

\[
                    (B\setminus\{z\})\cup\{x,y\}
                    \quad\hbox{is ordinary}.             \tag{3d3z11s38}
\]

This is load one in a fixed physical \(z\)-fibre; without that mark its
actual missing-vertex load is at most \(p\), and that loss is genuine.

Within one common insertion cell, signed planarity gives an equally sharp
three-cloud dichotomy.  Normalize \(uv=(-1,0)(1,0)\) and put

\[
 L(x)={x_y\over1+x_x},\qquad R(x)={x_y\over1-x_x}.
\]

For singleton ears \(x,y\),

\[
 B\cup\{x,y\}\text{ is ordinary}
 \quad\Longleftrightarrow\quad
 (L(x)-L(y))(R(x)-R(y))<0.                              \tag{3d3z11s39}
\]

Hence the mixed bank is exactly the incomparability graph of two tangent
orders.  For weighted carrier contexts with total candidate mass \(P\),
good incomparable mass \(G\), and literal carrier decoder load
\(\Lambda\),

\[
                         G\le\Lambda V(P).               \tag{3d3z11s40}
\]

At \(P=HR^{2-o(1)}\), \(\Lambda=R^{o(1)}\), failure to reach
\(HR^{\log_2 3+o(1)}\) forces all but
\(R^{-\vartheta+o(1)}\) of the records into one of the two coherent
dominance orientations.  Together with the two-cell theorem, the strong
terminal state is now exhausted: nonadjacent cells give commuting ears;
an equal cell gives a mixed bank or common-edge dominance cage; adjacent
cells give `(3d3z11s38)`.  The affine universal cage realizes zero
incomparability, so the remaining global operation is to prevent critical
mass dilution across face-dependent physical edges/vertices, or charge
that dispersion by a recoverable profile/circuit bank.

Edge dispersion by itself does not force a return cycle.  A rational
stretchable calibration takes three ordered sets \(L,C,R\) on one lower
parabola, with \(|L|=|R|=s\), \(|C|=h\), and carrier faces

\[
                  B(J,\ell,r)=J\cup\{\ell,r\},
       \qquad J\subseteq C,\ \ell\in L,\ r\in R.         \tag{3d3z11s41}
\]

There are \(2^hs^2\) contexts and every physical edge \(\ell r\) has
fibre density exactly \(1/s^2\), below the critical
\(p^{-\vartheta}\) threshold for \(p=h+2s\), \(h=s\).  The universal
affine child cage can be chosen tight enough to be one dominance chain
simultaneously over every \(\ell r\).  The directed physical-edge graph
is the acyclic \(\vec K_{s,s}:L\to R\), with no length-two path, return,
or mixed child pair.

The construction is nevertheless paid, exactly and globally, by the
detached carrier shield:

\[
 {2^{|L|+|C|+|R|}\over2^h s^2}
             ={2^{2s}\over s^2}.                        \tag{3d3z11s42}
\]

Indeed the entire carrier support \(L\cup C\cup R\) is convex.  Thus the
correct dispersed-edge target is a trichotomy: mixed/return module,
**or a detached endpoint shield/profile bank**.  Any surviving cage must
simultaneously destroy that shield while retaining critical edge
dispersion and the common child chamber.

Face-dependent edges can in fact be normalized without an edge
pigeonhole when their cages share one physical root and tangent side.
If \(z=(z_0,h)\) and all carrier labels lie below \(y=h\), the projective
map

\[
        \Psi_z(x,y)=\left({x-z_0\over h-y},{1\over h-y}\right)   \tag{3d3z11s43}
\]

sends \(z\) to infinity.  Every ordinary \(B\cup\{z\}\) becomes one
directional chain whose extreme pair is its own insertion edge.  Thus a
common root/tangent fibre with \(H_z\) carriers on support \(p_z\) obeys

\[
             {C_zU_z\over V_z}\ge {H_z\over V_z}\binom{p_z}{2}. \tag{3d3z11s44}
\]

The individual physical edge fibres may all have density \(p_z^{-2}\);
only the aggregate root density matters.  Across varying roots, the
ordinary faces \(B\cup\{z\}\) give the exact ledger

\[
 W\le\Lambda I\le\Lambda V(P),                           \tag{3d3z11s45}
\]

where \(I\) is the number of physical \((B,z)\) incidences and \(\Lambda\)
is their genuine history multiplicity.

The chart coordinate is load-bearing.  A stretchable cap-by-cup carrier
rectangle with \(s+t=\kappa\log D\) roles and a \(D\)-label omitted root
cell has

\[
 C_0=D^s,\quad U_0=D^t,\quad H=D^{s+t},\quad
 H_g=H/D^2,\quad M_1=DH.                                \tag{3d3z11s46}
\]

Every singleton root is compatible, every root pair is terminal-bad, and
the selected exterior chart has \(C_0U_0/H=1\).  Recharting one fixed root
exposes all \(H\) carriers exactly as `(3d3z11s44)` predicts, but different
root charts need not be simultaneously compatible with the three-cloud
seams.  Hence the final coordinate is no longer edge dispersion itself:
it is a recoverable common-root/history bank, or a theorem synchronizing
the root-to-infinity chart with the other exterior profile directions.

The synchronization shortcut is false exactly.  A projective chart has
one preimage of its line at infinity.  Thus three prescribed root/tangent
normalizations share one chart iff their separating lines coincide; if
the lines are free, three roots can be sent to infinity together iff they
are collinear:

\[
  \ell_1=\ell_2=\ell_3=T^{-1}(L_\infty),\qquad
  z_1,z_2,z_3\in T^{-1}(L_\infty).                 \tag{3d3z11s46a}
\]

This is sharp in the universal dominance cage.  An arbitrary low-rank
root order type \(Q\), split into three macroscopic clouds, can be squeezed
into the omitted carrier role so that

\[
       B\cup S\text{ is ordinary}\quad\Longleftrightarrow\quad |S|\le1
                                                        \tag{3d3z11s46b}
\]

for every complete carrier word \(B\).  All physical singleton incidences
still have load one, while every colourful root triple is noncollinear.
The incompatible charts do, however, expose an exact deletion alternative:
if \(Y,W\) are the two neighbour roles around the omitted cell, then

\[
 \mathcal F_{\ge2\text{ roots}}(P)
       \subseteq\mathcal F(P\setminus Y)\cup\mathcal F(P\setminus W).
                                                        \tag{3d3z11s46c}
\]

At the complete-word interface each branch loses one \(D\)-choice role
and leaves a one-sided cap/cup profile of \(Q\).  Therefore chart
incompatibility does not itself create a cyclic bank: the surviving
operation is a weighted deletion-shield/profile-change descent retaining
the physical \((B,z)\) history.

That descent has an exact square-root barrier.  Deleting only the nearest
neighbour role is insufficient: the nearest remaining labels on the two
carrier sides still cage every root pair.  A face with a non-singleton
root trace must erase one entire side.  If \(R_LR_R=H\) are the complete
one-sided reservoirs, the actual load-one absolute banks are
\[
                         U(Q)R_L,\qquad C(Q)R_R,        \tag{3d3z11s46d}
\]
and hence only
\[
 \max\{U(Q)R_L,C(Q)R_R\}
       \ge\sqrt{V(Q)R_LR_R}=\sqrt{V(Q)H}.              \tag{3d3z11s46e}
\]
For quarter-coefficient carrier mass and a half-coefficient root child,
this is exactly \(3/8\), not \(1/2\).  Even the candidate common infinity
line for two roots cuts the two carrier sides, so a two-root rechart does
not repair it.

Routing full physical \((B,z)\) records is weaker still.  The erased side
appears as the genuine history load
\[
 \Lambda_R^{\rm hist}\le R_Lr_Q\lambda_{B,z},\qquad
 \Lambda_L^{\rm hist}\le R_Rr_Q\lambda_{B,z},          \tag{3d3z11s46f}
\]
and the unrooted inequality \(C(Q)U(Q)\ge V(Q)\) need not persist for a
fixed retained root.  Thus the square-root inequality is an absolute face
bank, not an automatic continuation of the marked mass.

The minimizer deletion identity supplies only first moments.  For physical
roles \(X_1,\ldots,X_q\), with \(k(F)\) occupied roles,
\[
 \sum_{i=1}^qV(P\setminus X_i)
       =V(P)\bigl(q-\mathbb E k(F)\bigr).              \tag{3d3z11s46g}
\]
A central \(q/2\)-layer has maximal balanced role emptiness but a prescribed
empty half-side only with probability
\[
                  \binom q{q/2}^{-1}=2^{-q+O(\log q)}. \tag{3d3z11s46h}
\]
At \(q=\Theta(\log n)\) this is merely polynomial.  The remaining input
must therefore be genuinely high-order: a run/side deletion theorem, or a
nonresetting rooted endpoint/profile potential across physical histories.

The high-order deletion transform is exact, but it exposes a measure gap
rather than supplying that input.  If \(E(F)\) is the set of physical roles
missed by an ordinary face and \(\mathcal A\) is any family of role masks,
then double counting gives
\[
 \sum_{S\in\mathcal A}V\!\left(P\setminus\bigcup_{i\in S}X_i\right)
   =\sum_{F\in\mathcal F(P)}
       |\{S\in\mathcal A:S\subseteq E(F)\}|.          \tag{3d3z11s46i}
\]
For the \(q\) cyclic intervals of length \(k\), this is the literal
long-empty-run moment.  At
\[
 q=\Theta(L),\quad D=\Theta(n/L),\quad
 k=\Theta(L/\log L),\quad kD=\Theta(n/\log L),        \tag{3d3z11s46j}
\]
least-counterexample induction guarantees only a global-face fraction
\[
 2^{-(1/\ln2+o(1))L/\log L}                            \tag{3d3z11s46k}
\]
carrying a prescribed run, whereas the induced run child remains short by
\[
 2^{(1-o(1))L\log\log L}
      =n^{(1-o(1))\log\log\log n}.                    \tag{3d3z11s46l}
\]
Crucially, `(3d3z11s46i)` concerns the unweighted global face law; none of
the localized forest/history measures is known to have positive density in
those deletion children.

Nor can the virtual forest alphabet simply be restored after deletion.
For a terminal state with erased words \(a\), child faces \(G\), and an
output recording only a code \(\pi(a)\) with \(K\) values, the physical
output bank has size at most \(K|\mathcal J|\), and some code fibre has
weighted load at least
\[
                  {\sum_a w_a\over K}.                \tag{3d3z11s46m}
\]
Thus the apparent \(D^k\) forest expansion is cancelled exactly by
\(D^k\) erased-word load unless the output really encodes that many word
classes.  A rational parabolic role system attains equality with one
physical cyclic-run tag, uniform \(D\)-label branching, and atom weight
\(1/n\): it has \(qD^q\) records, \(qD^{q-k}\) outputs, and load
\(D^k/n\).  Nested universal cages moreover reset the rooted state from
\((B_j,z_j)\) to a distinct \((B_{j+1},z_{j+1})\), so the endpoint
potential need not telescope.  The precise remaining alternatives are a
branch-to-global density comparison, at least
\(n^{\Omega(\log\log\log n)}\) recoverable erased-word classes, a rooted
export on live mass, or an actual return cycle in the same physical state.

Even a polynomial branch-to-global comparison does not repair this.  In
the central rational Pascal cell
\[
             P=T(2h,h)=Y\prec Z,\qquad N=\binom{2h}{h},
                                                        \tag{3d3z11s46n}
\]
one can fix a canonical tangent triple \(T\subset Y\), one rank, and an
unordered injectively coloured family \(\mathcal E\) of noncap sources such
that the literal minimizer marks satisfy
\[
 \omega(D,T)\ge\tfrac12,\qquad
 \sum_{D\in\mathcal E}\omega(D,T)\ge {V(P)\over4N^{14}}.
                                                        \tag{3d3z11s46o}
\]
The released noncup family
\(\mathcal H\subseteq\mathcal F(Z)\), and every role-deletion complement,
have at least \(V(P)/(2N^7)\) faces.  Nevertheless strong glue gives the
exact all-delete law
\[
 (D\setminus G)\cup U\text{ ordinary}
       \quad\Longleftrightarrow\quad G=D
       \qquad(D\in\mathcal E,\ U\in\mathcal H),        \tag{3d3z11s46p}
\]
and each terminal \(U\) has load exactly
\(\sum_{D\in\mathcal E}\omega(D,T)\).  Thus polynomial density, the atom
floor, every deletion order, and every cyclic moment still cancel to the
released bank alone.  The chosen top orientation is already minimal among
the four reflection/swap products \(c^2,cu,cu,u^2\).

The decisive scope is that this Pascal parent has
\[
        \log V(P)=\left(1-{1\over4\ln2}+o(1)\right)(\log N)^2,
        \qquad 1-{1\over4\ln2}>\tfrac12.              \tag{3d3z11s46q}
\]
It satisfies all deletion-child lower bounds but violates the proposed
parent fixed-gap upper bound.  Hence no density lemma, even at polynomial
strength and with canonical weights, can finish the proof in isolation;
the parent upper bound must enter a genuinely global mutation/profile
inequality.

There is a sharp standalone payment even without synchronized charts.
Randomly bipartition the used endpoint labels and retain one directed
quarter of the carrier contexts.  Let \(Z\) be their endpoint support and
\(I_\omega=B_\omega\setminus Z\).  If the maximum physical-edge fibre has
weight \(\delta W\), every downshadow output
\(e_\omega\cup F\), \(F\subseteq I_\omega\), recovers its edge from
intersection with \(Z\), so

\[
 V(P)\ge {\sum_{\omega}w_\omega2^{|I_\omega|}
                    \over\delta W}.                      \tag{3d3z11s47}
\]

In particular, \(\alpha\) mass with \(|I_\omega|\ge r\) gives
\(V\ge\alpha2^r/(4\delta)\).  Dispersion also forces

\[
          |Z|\ge(2\delta)^{-1/2}-1,
          \qquad V(P|Z)\ge F_C(|Z|).                    \tag{3d3z11s48}
\]

These banks are standalone; the carrier/source mass really can cancel.
In the stretchable universal cage, let \(\mathcal A\) be all intrinsic
source faces of an arbitrary child \(Q\) of rank at least two, and use
each record \((A,\ell,r)\in\mathcal A\times L\times R\).  Then

\[
 W=|\mathcal A|s^2,\qquad
 \operatorname{load}(\{\ell,r,x\})
       =|\{A\in\mathcal A:x\in A\}|,                  \tag{3d3z11s49}
\]

which equals \(2^{q-1}-1\) for a Boolean \(q\)-child.  Thus acyclicity,
edge dilution, and heredity cannot multiply the source bank without a
source-retaining return output, a carrier-coded shield, or an aggregate
source-reuse bound.

The source-reuse obstruction persists after exact live normalization and
even after counting the whole local complex.  Put a convex \(q=2m\)-gon
\(Q\) inside a universal cage for every cross edge of two \(s\)-point
endpoint clouds \(L,R\), and weight every record
\((A,\ell,r)\), \(|A|\ge2\), by \(1/s^2\).  Then the total mass over all
edges is one for each actual source face and

\[
       W=2^q-q-1,\qquad
       \operatorname{load}(\{\ell,r,x\})={2^{q-1}-1\over s^2}. 
                                                        \tag{3d3z11s50}
\]

Every ordinary output retaining the full edge has source rank at most one.
The best literal two-face repair is the injective pair
\((A,\{\ell,r,x\})\), whose exact count gives only

\[
                    V(P)\ge s\sqrt{q2^{q-1}-q}.          \tag{3d3z11s50a}
\]

At \(q=4s\) this is negligible compared with \(2^q\): retaining the old
source removes codegree only through the fatal square root.
Choosing balanced antipodal endpoint chambers makes each one-ended source
profile at most \(q^2 2^{q/2+O(1)}\), and exhaustive case separation gives

\[
 V(P)\le2^q+(2^s-1)(P_L+P_R)+(q+1)2^{2s}.             \tag{3d3z11s51}
\]

Thus at \(q=4s\),

\[
                         V(P)=(1+o(1))2^q=(1+o(1))W.   \tag{3d3z11s52}
\]

This is a stretchable local/live-normalized barrier, although not a
global sub-half construction because the Boolean source bank itself pays.
It proves that rank-safe endpoint Cauchy, bounded-rank source tags, and the
two one-ended profiles cannot absorb source codegree inside the cage.  A
positive proof must import external history, a minimizer mutation excluding
the balanced Boolean source, or a return component carrying the source in
a different physical part.

The all-rank Boolean barrier does not survive unchanged on the canonical
fixed-rank source slice.  Let \(\mathcal Q\) be distinct ordinary
\(q\)-point carriers, let records use one fixed source rank \(r\), and
retain the per-source mass cap one.  Put
\[
 d_Q={W_Q\over\binom qr},\qquad
 \Lambda_{\rm mid}=
   \max_{\lceil q/3\rceil\le|F|\le\lfloor2q/3\rfloor}
      \sum_{Q\supseteq F}d_Q,
\]
and, for comparison, let
\[
 \Omega_{\rm mid}=\max_{\lceil q/3\rceil\le|F|\le\lfloor2q/3\rfloor}
        |\{Q\in\mathcal Q:F\subseteq Q\}|,
\]
so that \(\Lambda_{\rm mid}\le\Omega_{\rm mid}\).  Then the weighted
nonempty middle Boolean banks give the exact global inequality
\[
 V(P)\ge {W\over\Lambda_{\rm mid}}\,
   {\sum_{t=\lceil q/3\rceil}^{\lfloor2q/3\rfloor}\binom qt
        \over\binom qr}
 \ge {W\over\Omega_{\rm mid}}\,
   {\sum_{t=\lceil q/3\rceil}^{\lfloor2q/3\rfloor}\binom qt
        \over\binom qr}.                                \tag{3d3z11s52a}
\]
Uniformly in \(r\),
\[
 V(P)\ge {W\over\Lambda_{\rm mid}}
       (1-2e^{-q/18})\sqrt{\pi q/2}.                    \tag{3d3z11s52b}
\]
Writing \(\vartheta=2-\log_2 3\), this supplies the required
\(q^\vartheta\) whenever
\[
       \Omega_{\rm mid}\le
       q^{1/2-\vartheta-o(1)}
       =q^{\log_2 3-3/2-o(1)}.                         \tag{3d3z11s52c}
\]
The high branch fixes one actual middle face \(F\) in many distinct
carriers and writes \(Q=F\mathbin{\dot\cup}R_Q\), contracting completion
rank to at most \(2q/3\).  Thus the former arbitrary source-reuse residue
has narrowed to a mask-aware rooted completion iteration over a common
physical core; only that iteration, not the fixed-rank Boolean capacity,
remains open.

The high-core family has two further exact exits.  If a weighted subfamily
\(\mathcal P\) has private completion petals
\(x_Q\in R_Q\setminus\bigcup_{Q'\ne Q}R_{Q'}\), then the banks
\(\{S\subseteq Q:x_Q\in S\}\) are pairwise disjoint and
\[
             V(P)\ge M_{\mathcal P}{2^{q-1}\over\binom qr}
                    \ge M_{\mathcal P}\sqrt{\pi q/8}.  \tag{3d3z11s52d}
\]
If instead a subfamily \(\mathcal S\) four-covers its union support
\(U_{\mathcal S}=\bigcup_{Q\in\mathcal S}Q\), planar four-locality makes
that whole union ordinary.  Global source normalization then gives
\[
       M_{\mathcal S}\le\binom{|U_{\mathcal S}|}{r},\qquad
       V(P)\ge M_{\mathcal S}\sqrt{\pi q/2}.           \tag{3d3z11s52e}
\]
Otherwise a canonical bad four-set \(C\subseteq U_{\mathcal S}\) has a
nonempty trace \(Z=C\setminus F\), \(|Z|\le4\), omitted by every carrier.
Partitioning by the first omitted \(z\in Z\) gives an at-most-four-ary
deletion forest whose support strictly shrinks; every terminal union is
four-covered and convex.  If \(\Lambda_{\rm leaf}\) is the actual overlap
of the terminal Boolean banks, summing the leaf inequalities yields
\[
             V(P)\ge {M_{\mathcal S}\over\Lambda_{\rm leaf}}
                         \sqrt{\pi q/2}.                \tag{3d3z11s52f}
\]
Thus private first differences and convex-union lifts close with the full
square-root gain.  The precise survivor is high overlap among distinct
convex leaf banks after every branch label has been deleted; those labels
cannot be reattached as ordinary decoder tags.  This is the same rooted
history/return obstruction exposed by erased-run conservation, now reached
from the high-midshadow side.

This leaf-overlap residue is genuine even in a rational rank-safe planar
hierarchy.  Let \(P_d\) be depth-\(d\) vertical self-substitution of the
six-point Pascal seed \(T(4,2)\).  Its exact graded recurrences imply

\[
 |P_d|=6^d,\qquad q=4d,\qquad
 v_q(P_d)>0,\qquad V(P_d)<40v_q(P_d).                 \tag{3d3z11s52g}
\]

Thus no universal planar rank-layer anticoncentration
\(V\ge c\sqrt q\,v_q\) is possible, even at rank \(O(\log n)\).  More
directly, take every top face as a distinct carrier/source of weight one.
Then \(W=v_q\ge V/40\), and middle-incidence counting forces

\[
       \Lambda_{\rm mid}\ge {v_q B_q\over V}
                    \ge {B_q\over40}=2^{q-o(q)}.       \tag{3d3z11s52h}
\]

Applying the private-petal/four-cover forest likewise forces

\[
              \Lambda_{\rm leaf}\ge
                    {\sqrt{\pi q/2}\over40}.           \tag{3d3z11s52i}
\]

Hence carrier convexity, fixed source rank, private labels, and planar
four-local union lifts do not control the final overlap: the vertical
Pascal profile word realizes coherent reuse.  A successful return must
retain external root/endpoint history or exploit the recursive strong-glue
chronology itself.

There is nevertheless an exact minimizer-specific closure if this coherent
overlap promotes to one actual ordered strong-decomposition tree on an
induced \(m\)-point support.  The weighted endpoint theorem then gives
\[
             \log V(P)\ge\tfrac12(\log m)^2
                         -O((\log m)^{3/2}).            \tag{3d3z11s52j}
\]
Hence a least fixed-gap counterexample
\(\log V(P)<(\tfrac12-\delta)(\log n)^2\) cannot contain such a tree on
\[
             m\ge n^{\sqrt{1-2\delta}+\varepsilon}.    \tag{3d3z11s52k}
\]
In particular, a same-chart strong-tree promotion on \(n^{1-o(1)}\)
physical labels closes every fixed gap without any carrier decoder.

The coefficient is sharp.  For the balanced templates
\(S_k=T(2k-4,k-2)\), their vertical rational iterates satisfy
\[
 {\log V(Q_d)\over(\log|Q_d|)^2}
   \longrightarrow
 \rho_k={k-2\over\log\binom{2k-4}{k-2}}\downarrow\tfrac12, \tag{3d3z11s52l}
\]
while a rank-\(q_d=\Theta(\log|Q_d|)\) top layer remains a constant fraction
of all faces and has
\(\Lambda_{\rm mid}\ge2^{q_d-o(q_d)}\).  Thus exponentially coherent
overlap gives no uniform super-half margin.  The missing statement is
exactly promotion of the deletion/leaf chronology to a macroscopic
same-chart strong tree, or equality-case rigidity supplied by its retained
root/endpoint state.

In fact the terminal overlap is exponential as well.  Here \(q_d\) is the
ambient maximum face rank, so a convex-union leaf cannot contain two
distinct top-rank carriers: their union would have rank \(>q_d\).  The
forest therefore ends in singleton-carrier leaves, while the common middle
face remains in all their Boolean banks.  Consequently
\[
       \Lambda_{\rm leaf}\ge\Lambda_{\rm mid}
          \ge {B_{q_d}\over K_{S_k}}=2^{q_d-o(q_d)}.   \tag{3d3z11s52m}
\]
This sharpness can be diagonalized: choose \(k_j\to\infty\), then depths
\(d_j\to\infty\) fast enough, to obtain one rational planar sequence
\(P_j\) with
\[
 { \log V(P_j)\over(\log|P_j|)^2}\to\tfrac12,\qquad
 q_j=(1+o(1))\log|P_j|,\qquad
 \Lambda_{\rm mid},\Lambda_{\rm leaf}=2^{q_j-o(q_j)}.
                                                        \tag{3d3z11s52n}
\]
So strong hierarchy plus exponential coherent overlap does not imply even
a qualitative strict improvement over \(1/2\); it supplies exactly the
desired boundary and no more.

The strong-tree closure is stable under the weighted decoder losses that
arise in a genuine promotion.  At a seam \(v=A\prec B\), let the cap, cup,
inherited-face, and forward cap--cup recurrences each be divided by their
actual decoder factors.  If \(G_X,G_Y,G_M\) are the directed max-plus loss
potentials, with
\[
 G_M(v)=\max\{G_M(A)+\ell^M_{v,A},\ G_M(B)+\ell^M_{v,B},
             \ G_X(A)+G_Y(B)+\ell^M_{v,\times}\},                \tag{3d3z11s52o}
\]
and the analogous two-arm recurrences for \(G_X,G_Y\), exact comparison
with the lossless tree gives
\[
 \log M_{\rm app}(T)\ge\tfrac12(\log |T|)^2
       -O((\log |T|)^{3/2})-G_M(T).                              \tag{3d3z11s52p}
\]
Thus the error is a **one-turn Carleson norm**, not the sum over all tree
nodes.  If all seven local logarithmic losses at node \(v\) are at most
\(\gamma_v\), then
\[
              G_M(T)\le2\max_{\pi}\sum_{v\in\pi}\gamma_v,       \tag{3d3z11s52q}
\]
where \(\pi\) ranges over root--leaf paths.  In particular, against a
\((1/2-\delta)\)-counterexample it suffices that
\[
 G_M<\left[\tfrac12\left({\log m\over\log n}\right)^2
              -(\tfrac12-\delta)\right](\log n)^2
              -O((\log n)^{3/2}).                               \tag{3d3z11s52r}
\]
Guard removal is covered either by pruning the physical support or by the
exact local factor
\(\lambda=D(b+1)/(b-g+1)\), whose logarithmic guard cost is at most
\(2g/((b+1)\ln2)\) when \(g\le b/2\).

This robust form isolates rather than solves the promotion.  The
common-core forest has no certified same-chart endpoint seams; the stable
circuit tournament has affordable \(O((\log n)(\log\log n))\) description
budget but the same geometric defect.  Conversely, unmarked Pascal is a
lossless strong tree, while its canonical marked all-delete turn has
decoder load at least \(V/(4N^{14})\), hence logarithmic cost
\((\beta+o(1))(\log N)^2\).  It exhausts the budget in
\((3d3z11s52r)\).  The exact remaining certificate is therefore a
same-chart approximate tree together with a subcritical **marked turn
load**; bounded rank, circuit arity, or entrance density alone controls
neither quantity.

At a genuine two-child strong seam the strict parent upper bound now has
one exact quantitative consequence.  If \(P=A\prec B\),
\(a=|A|,b=|B|\), then the strong-glue identities and
\(W(Q)\le C(Q)U(Q)\) imply
\[
 C(P)U(P)\ge
 \left(\sqrt{(b+1)W(A)}+\sqrt{(a+1)W(B)}\right)^2.     \tag{3d3z11s52s}
\]
For balanced reflected children of size \(m=2^{L-1}\) and face count
\(H\), this reads \(C(P)=U(P)\) and
\(C(P)U(P)\ge4(m+1)H\).  With
\(\Phi_{\beta,K}(L)=\beta L^2-KL\log L\) and the inductive child bound,
\[
 \log(C(P)U(P))-\Phi_{\beta,K}(L)
 \ge(1-2\beta)L+(1+\beta)
   +K\{L\log L-(L-1)\log(L-1)\}.                    \tag{3d3z11s52t}
\]
Thus a fixed \(\beta<1/2\) gap forces a polynomial endpoint surplus;
at \(\beta=1/2\) it forces at least \(2^{3/2}L^K\).  If cap--cup pairs
could be routed to ordinary faces with load \(\Lambda\), the seam would
close whenever
\[
 \log\Lambda<(1-2\beta)L+(1+\beta)
      +K\{L\log L-(L-1)\log(L-1)\}.                  \tag{3d3z11s52u}
\]

This is the first exact use of the parent fixed-gap upper bound, but it
still stops one operation short.  In the dense all-delete rectangle
\(\mathcal D=(\mathcal F(A)\setminus\mathcal C(A))\) and
\(\mathcal H=(\mathcal F(B)\setminus\mathcal U(B))\), every nonempty
\(D'\subseteq D\in\mathcal D\) is incompatible with every
\(F\in\mathcal H\).  Routing \((D,F)\) to \(F\) has load
\(\sum_Dw_D\), cancelling the entire source factor.  Exact integral
scalar profiles attain equality in \((3d3z11s52s)\), and a stretchable
balanced Pascal-iterate calibration has rank \(O(\log n)\), polynomial
canonical-root loss, dense all-delete sides, and coefficient tending to
one half.  Hence the remaining fixed-gap step is precisely a
polylogarithmic-load cap--cup-to-ordinary converter, a same-configuration
profile reset, or an equivalent marked-turn release; endpoint energy,
density, rank, and root degree alone do not supply it.

Nor can least-counterexample arithmetic by itself make that marked turn
cheap.  A fibre of size \(V/n^A\) still has the full quadratic logarithmic
coefficient, while respecting both the per-source mass cap and the mean
rank bound.  There is an exact conditional support--rank exit: if all turn
sources lie on \(s\) physical labels and have rank at most \(r\), then
\[
       \Lambda_{\rm turn}\le\sum_{i\le r}\binom si
                    \le\left({es\over r}\right)^r.               \tag{3d3z11s52v}
\]
Thus \(s\le n^{\sigma+o(1)}\), \(r\le(\kappa+o(1))\log n\), an
approximate-tree support \(m=n^{\alpha+o(1)}\), and other one-turn loss
\((g+o(1))(\log n)^2\) close a \((1/2-\delta)\)-gap whenever
\[
             g+\kappa\sigma
                 <\tfrac12\alpha^2-(\tfrac12-\delta).             \tag{3d3z11s52w}
\]
The deletion identity, however, gives only
\[
        \mu<(2c+o(1))\log n,\qquad
        \kappa\downarrow4c\quad(c=\tfrac12-\delta),               \tag{3d3z11s52x}
\]
because a positive-mass Markov cutoff needs factor \(K>2\).  On a
near-ambient support \((3d3z11s52w)\) would require
\(\kappa<\delta\), while throughout the live range \(c\ge1/4\) one has
\(4c\ge1>\delta\).  Optimizing the rank cutoff therefore cannot pay the
turn.

The canonical Pascal marked fibre saturates this obstruction with
\[
       \Lambda(U)\ge {V(P)\over4N^{14}}
          =2^{(\beta+o(1))(\log N)^2},\qquad
       \beta=1-{1\over4\ln2}>\tfrac12,                            \tag{3d3z11s52y}
\]
and every nonempty retained source trace remains incompatible with \(U\).
The ordered pair of ordinary faces \((D,U)\) decodes the record with load
one but gives only a \(V^2\) state, so it cannot replace the one-face turn
recurrence.  Pascal is not a sub-half minimizer; it proves exactly that the
missing result must be geometric and minimizer-specific: compress the
physical support enough for \((3d3z11s52w)\), produce one ordinary
composable retag with subcritical Carleson load, or unmark the fibre inside
a macroscopic same-chart strong tree.

An all-pairs cap--cup converter cannot be that retag.  If \(Q\) is a
balanced \(N\)-point child with \(C(Q)=U(Q)=E\) and
\(P=Q\prec Q\), then
\[
 W(P)=2W(Q)+E^2\le3E^2,\qquad
 C(P)=U(P)=(N+2)E.                              \tag{3d3z11s52z}
\]
Consequently any assignment of all ordered cap--cup pairs to ordinary
faces with \(T\) auxiliary tags has load
\[
       \Lambda\ge{C(P)U(P)\over TW(P)}
                    \ge{(N+2)^2\over3T}.              \tag{3d3z11s52z1}
\]
A fixed root and polylogarithmically many charts therefore leave quadratic
load; one varying physical anchor still leaves linear load.  More exactly,
for the dominant pairs \((A+z,y+B)\), ordinary union is equivalent to both
\(A+y\) remaining a cap and \(B+z\) remaining a cup.  If endpoint ranks are
at most \(R\), their compatible density is at most \(4R^2/N^2\).  Every
failed left extension has a wrong-sign triple using \(y\) and two labels
of \(A\), which with any right label is a literal rooted \(1+3\) circuit.
Deleting \(y\) releases the face but erases exactly the independent anchor
needed to decode it.

Global fixed-\(n\) minimality does provide a new, exact mutation law.  For
\(0<p<1\), put
\[
 G_p=\sum_{F\in\mathcal F(P)}\{p^{|F|}+(1-p)^{|F|}\},\qquad
 Z_p=\sum_{\substack{A\in\mathcal C(P),\ B\in\mathcal U(P)\\A\cap B=\varnothing}}
             p^{|A|}(1-p)^{|B|}.
\]
Randomly bipartitioning the physical labels and strongly gluing the two
induced order types gives
\[
       W(P)\le G_p+Z_p,\qquad
       Z_p\ge2p(1-p)\{W(P)-n\};                         \tag{3d3z11s52z2}
\]
in particular \(Z_{1/2}\ge(W-n)/2\).  This is genuine same-minimizer
multi-scale endpoint energy, but a rank-\(r+s\) pair is discounted by
\(2^{-(r+s)}\).  Removing that discount on the rank-\(O(\log n)\) slice
costs a fixed power of \(n\), far more than the polylogarithmic seam
surplus.  The exact twelve-point wrapper has
\(G_{1/2}+Z_{1/2}=71761/64>W=1061\) while \(2249\) of its physical
bipartitions actually decrease \(W\); thus the averaged law is necessary,
not sufficient.  The surviving selected-reset statement is now literal:
extract an inverse-polylogarithmic endpoint subfamily with only
\(O(\log\log n)\) anchor entropy, repair its rooted cross-circuits while
retaining both anchors, or exhibit one decreasing physical bipartition.

There is also an exact local mutation which creates the desired one-face
retag, again with the minimizer sign reversed.  Move a blocked singleton
\(x\) through an adjacent exposed source edge \(ab\), changing only
\(\chi(a,b,x)\).  If \(\Phi^\pm_{ab}(z)\) count source faces on the two
sides which expose \(ab\), then coefficientwise
\[
       \Phi_{P^-}(z)-\Phi_{P^+}(z)
          =z\{\Phi^+_{ab}(z)-\Phi^-_{ab}(z)\}.          \tag{3d3z11s52z3}
\]
Every plus-star source \(R\) is blocked by \(x\) in \(P^+\), while
\(R\cup\{x^-\}\) is an injective, full-source-retaining ordinary face in
\(P^-\).  But if \(P^+\) minimizes \(V\), then only
\[
                         E^+_{ab}\ge E^-_{ab}                     \tag{3d3z11s52z4}
\]
follows: the minimizer hides the larger edge star.  Rational caps attain
\(E^+_{ab}=2^{m-2}-1,E^-_{ab}=0\).  A positive use therefore needs three
extra inputs simultaneously: adjacent-wall access for a positive-mass
marked fibre, control of the cumulative mutation increase against a
fixed-gap budget, and stability of the full released endpoint state.
Neither a tangent root nor one singleton release supplies the last two.

The mutation **budget** and adjacency requirements can in fact be removed
completely.  If \(Q\) is fixed and \(x,y\) are arbitrary generic positions
of one new labelled point, heredity gives the coefficientwise comparison
\[
 \Phi_{Q+y}(z)\le(1+z)\Phi_Q(z)
                    \le(1+z)\Phi_{Q+x}(z).             \tag{3d3z11s52z5}
\]
More generally, deleting and arbitrarily re-embedding a physical repair
alphabet \(X\), \(|X|=k\), costs only
\[
                    V(Q\cup X')\le2^kV(Q\cup X).       \tag{3d3z11s52z6}
\]
This pays the entire arrangement-wall fan once through the deletion base;
the number of adjacent flips crossed is irrelevant.  Combining this with
the loss-stable tree theorem, if the relocation produces an \(m\)-label
same-chart approximate strong tree of one-turn loss \(G\), then
\[
 \log V(P)\ge\tfrac12(\log m)^2-O((\log m)^{3/2})-G-k. \tag{3d3z11s52z7}
\]
Thus on \(m=n^{1-o(1)}\), any \(G+k=o((\log n)^2)\) closes every fixed
gap.  In particular \(O(\log n)\) exclusive singleton repairs are free at
coefficient scale; the previous adjacent-wall and cumulative-slack gates
were artefacts of charging the same deletion base repeatedly.

At one marked turn the required geometry is also exact.  If all sources
share one exposed edge \(ab\) on the same side, there is a nonempty open
ear chamber near an interior point of \(ab\) in which relocating the blocked
singleton \(x\) makes every \(R\cup\{x\}\) ordinary, with the source
recovered by deleting \(x\).  Distinct repair labels can be placed
independently.  When one physical label is reused, all its turns can be
repaired iff their convex ear chambers intersect:
\[
                         \bigcap_{v\in I_x}C_v\ne\varnothing.    \tag{3d3z11s52z8}
\]
By planar Helly, failure already has a witness of at most three turns.
Consequently the mutation route has narrowed to a pure promotion theorem:
convert the marked forest into a common-chart certificate with a
subquadratic physical repair alphabet, or charge a two-/three-ear reuse
obstruction.  Re-embedding a whole rank-\(O(\log n)\) released face at each
of \(O(\log n)\) turns can still cost \(\Theta((\log n)^2)\), and the current
one-turn retags do not yet prove the cap, cup, and forward recurrences in
one chart.  See
`agent_outer_internal_product/GAP_BUDGETED_REPAIR_ALPHABET_MUTATION_GATE.md`.

Global minimization supplies a complementary projection-uniform endpoint
surplus.  Put \(\ell_x=V(P)-V(P-x)\), let \(\mu\) be the mean face rank, and
write
\(M_C=\sum_{A\in\mathcal C(P)}|A|\),
\(M_U=\sum_{B\in\mathcal U(P)}|B|\).  Comparing \(P\) with the two
singleton strong-glue mutations of \(P-x\) gives, in every generic chart,
\[
 \ell_x\le1+C(P-x),\qquad \ell_x\le1+U(P-x).            \tag{3d3z11s52z9}
\]
After summing the exact deletion identities,
\[
 \mu V\le n+nC-M_C,\qquad
 \mu V\le n+nU-M_U,                                   \tag{3d3z11s52z10}
\]
and therefore
\[
 C,U\ge{\mu V-n\over n},\qquad
 {CU\over V}\ge{(\mu V-n)^2\over n^2V}.              \tag{3d3z11s52z11}
\]
This is a genuine minimizer-only reset: the balanced twelve-point Pascal
wrapper has \(V=1061\), but its four singleton-extension classes have
\(\ell_x\in\{332,394\}\), whereas the smaller singleton-glue additions are
only \(165\) or \(179\); the corresponding mutations reduce \(V\) to the
range \(832,\ldots,908\).

The unpaid part also has an exact ledger.  The number of addable ordered
cap--anchor incidences is \(E_C=2M_C-n\); if cap rank is at most \(R\), then
\(E_C/(nC)\le2R/n\), and likewise for cups.  Hence on a rank-\(O(\log n)\)
slice almost every anchor is a wrong-sign endpoint extension and, once an
opposite physical anchor is retained, gives a rooted \(1+3\) circuit.
This remains true after deleting the two anchors: if \(B_C,B_U\) are the
bad cap- and cup-anchor counts and \(C_{yz}=C(P-\{y,z\})\) (dually
\(U_{yz}\)), then the bad pairs satisfying simultaneously
\(C_{yz}\ge C/2\) and \(U_{yz}\ge U/2\) have total mass at least
\[
 B_CB_U-8nRCU
   \ge\{(n-2R)^2-8nR\}CU.                              \tag{3d3z11s52z13}
\]
Thus anchor concentration is not the obstruction: a \(1-O(R/n)\) share
retains half of both endpoint reservoirs on the literal deletion base.
Scalar deletion data can saturate all of the inequalities above while the
required all-pairs load diverges.  The remaining operation is therefore
irreducibly planar: eliminate two such anchored circuits into a bounded-load
ordinary output, or align them with a physical bipartition \(R\sqcup B\)
for which
\[
                 V(R)+V(B)+C(R)U(B)<V(P),             \tag{3d3z11s52z12}
\]
contradicting global minimality.  See
`agent_common_shield_mixing/MINIMIZER_SINGLETON_ENDPOINT_SURPLUS_GATE.md`.

Cheap relocation is not itself the two-anchor converter.  If
\(P=Q\cup X\), \(|X|=k\), and only the anchors \(X\) are re-embedded, every
new ordinary output has the canonical code
\[
                         (F\cap Q,F\cap X'),             \tag{3d3z11s52z14}
\]
so a tagged decoder of load \(\Lambda\) serves at most
\[
                         T\Lambda\,2^kV(Q)               \tag{3d3z11s52z15}
\]
records.  The same \(2^k\) is exactly the relocation comparison loss.
Moreover, if an output retains variable supports \(A,B\subseteq Q\),
heredity forces \(A\cup B\) to have been ordinary already.  Thus fixed
anchors add only their mask bits and cannot repair a genuinely bad
variable-support union.  In the balanced two-block endpoint rectangle,
moving \(k_L,k_R\) anchors reaches at most
\[
                      {(2R+k_L)(2R+k_R)\over N^2}        \tag{3d3z11s52z16}
\]
of the spanning pairs.  At \(R,k_L,k_R=O(\log N)\) this is
\(N^{-2+o(1)}\), not inverse-polylogarithmic.

The exact remaining minimizer state is correspondingly stronger than a
single endpoint inequality.  For \(Q=P-x\), the actual position of \(x\)
globally minimizes its one-point extension count over **every** chamber of
the pair-line arrangement of \(Q\):
\[
             L_{P-x}(c_x)=\min_c L_{P-x}(c).             \tag{3d3z11s52z17}
\]
Every adjacent wall therefore hides the larger exposed-edge star.  The
arrangement changes with \(x\), and the sign is anti-converting.  A proof
must now use interactions among two or more minimum cells to create an
already-ordinary base-support union or a genuinely decreasing multipoint
mutation.  See
agent_outer_internal_product/FIXED_ANCHOR_RELOCATION_CANCELLATION_GATE.md.

The one-bit repair theorem also has an exact entropy interface with the
surviving near-uniform role forest.  At a role of alphabet size \(d\), if
every physical label has conditional mass at most \(K/d\), retaining \(s\)
label classes has mass loss \(g\) and relocating the retained labels costs
\(s\) bits.  For \(d/K\ge2\),
\[
                         g+s\ge\log(d/K)+1.             \tag{3d3z11s52z18}
\]
Consequently \(q=\Theta(L)\) disjoint rich roles force
\[
          G+k\ge\sum_{j=1}^q\{\log(d_j/K_j)+1\}
                =\Theta(L^2)-O(L\log L).               \tag{3d3z11s52z19}
\]
Selecting one chronology path keeps \(k=O(L)\) but pays quadratic \(G\);
retaining the forest makes \(G\) small only by making the physical repair
alphabet enormous.  Relocation therefore becomes useful only after the
branches have already been summed through recoverable ordinary/profile
identifiers.

There is a sharp conditional splice.  If turn \(j\) has a distinct repair
label \(z_j\), and its missing banks are literally \(R\cup\{z_j\}\) with
all \(R\) exposing one recovered edge on one side, then the common-ear
lemma repairs all turns for \(k=q\).  A recovered edge menu of size \(t_j\)
adds only
\[
                         G\le G_0+\sum_j\log t_j,        \tag{3d3z11s52z20}
\]
provided all other certified outputs omit the repair alphabet and the
repaired recurrences occupy one chart.  Fixed circuit data alone does not
give this edge localization: an exact rational three-ear gadget has a
fixed inner \(1+3\) circuit at every level, every pair of released ear
chambers intersects, but the intersection of all three is empty.

The weighted form localizes the sole hard survivor.  For the conditional
law \(\nu\) of ear chambers at one fixed physical repair label, put
\(h=\sup_x\nu\{C:x\in C\}\).  Fractional Helly gives
\[
 \Pr[C_1\cap C_2\cap C_3\ne\varnothing]
       \le1-(1-h)^3\le3h.                              \tag{3d3z11s52z21}
\]
Thus with \(\eta=L^{-B}\), either one point repairs \(\eta\) of the turn
mass at total \(O(L\log L)\) selection loss, or \(1-3\eta\) of the weighted
triples are literal same-label Helly obstructions.  The exact remaining
operation is to map this dense marked three-ear family to a
carrier/history-preserving cyclic/profile bank, or use it to produce a
decreasing multipoint mutation.  See
`agent_common_shield_mixing/CHRONOLOGY_ONE_BIT_REPAIR_SPLICE_HELLY_GATE.md`.

Order-two global minimality gives a further exact test, but no automatic
converter.  For \(Q=P-\{x,y\}\), let \(A_Q(u)\) count base traces whose
union with \(u\) is ordinary, and \(J_Q(u,v)\) those whose union with both
anchors is ordinary.  Then
\[
 V(Q+u+v)=V(Q)+A_Q(u)+A_Q(v)+J_Q(u,v),\qquad
 0\le J_Q(u,v)\le V(Q)+1.                              \tag{3d3z11s52z22}
\]
The interaction is only another copy of the base-face reservoir; if its
output retains variable supports \(B,C\subseteq Q\), heredity already
forces \(B\cup C\) ordinary.  Comparing a global minimizer with the three
canonical two-anchor strong glues yields
\[
 V(P)-V(Q)\le3+\min\{3C(Q),3U(Q),C(Q)+U(Q)+n-2\}.      \tag{3d3z11s52z23}
\]
Summing this inequality gives exact cap/cup second-rank-moment bounds, but
only constant-factor improvements after those moments are discarded.

The genuine simultaneous effect is the mixed Hessian
\[
 K_{x,y}(u,v)=J_Q(u,v)-J_Q(u,y)-J_Q(x,v)+J_Q(x,y),      \tag{3d3z11s52z24}
\]
and the pair move decreases \(V\) exactly when
\[
 K_{x,y}(u,v)<-\Delta_x(u\mid y)-\Delta_y(v\mid x).    \tag{3d3z11s52z25}
\]
The two separate costs are nonnegative by self-minimality.  The Hessian
has both signs already on the true five- and nine-point minimizers, but its
negative values are absorbed by those costs; the balanced Pascal wrapper
instead violates the pair bound for every deleted pair and admits a
\(-313\)-face move.  Thus order-two minimality rejects that barrier without
yet converting its endpoint mass.  The live circuit theorem must force a
negative Hessian beyond both first-order costs, or exhibit an
already-ordinary base-support union.  See
`agent_outer_internal_product/MINIMIZER_TWO_POINT_EXTENSION_INTERACTION_GATE.md`.

The bare three-ear version of that hoped-for dichotomy is **false even in
a true global minimizer**.  In the exact nine-point minimizer, one physical
label is hidden in three source triangles with exposed repair edges
\(61,71,38\).  Their open ear chambers \(C_1,C_2,C_3\) satisfy
\[
 C_i\cap C_j\ne\varnothing\quad(i\ne j),\qquad
 C_1\cap C_2\cap C_3=\varnothing,                       \tag{3d3z11s52z26}
\]
while every two-source union and the full source union are nonordinary.
Since this order type is globally minimal with \(V=168\), no two- or
three-label relocation beats the separate costs.  Strict Farkas reduces
every pairwise-feasible, jointly-infeasible triple of planar ear systems to
one boundary inequality from each chamber and positive coefficients
\[
 \lambda_1a_1+\lambda_2a_2+\lambda_3a_3=0,\qquad
 \lambda_1c_1+\lambda_2c_2+\lambda_3c_3\le0.             \tag{3d3z11s52z27}
\]
This is exactly a dual three-line cage, but it supplies no primal face
bank by itself.

Order-three canonical minimality is exact but does not remove the cage.
For \(Q=P-X\), \(|X|=3\), \(N=n-3\),
\[
 V(P)-V(Q)\le7+\min\{6C,6U,3C+U+3N,C+3U+3N\}.           \tag{3d3z11s52z28}
\]
Its four summed third-rank-moment inequalities are weaker than the
singleton bound after rank correlations are dropped.  The highest Möbius
interaction is again nonnegative and at most \(V(Q)+1\).  The nine-point
cage has pointwise slack \(19,\ldots,34\), while every triple of the
balanced Pascal wrapper violates the bound by \(305,\ldots,434\).
Therefore all order-\(\le3\) scalar minimality data and the literal Farkas
cage can coexist:
\[
 \boxed{\text{the next splice must retain additional physical history
 beyond the three ear chambers and their bare source supports.}} \tag{3d3z11s52z29}
\]
See
agent_outer_internal_product/THREE_EAR_MINIMIZER_BARRIER_AND_ORDER_THREE_GATE.md.

In a genuine two-block endpoint chart, the shared-anchor circuit
elimination is also completely classified.  The two rooted circuits
\[
 C_L=\{a_0,a_1,y,z\},\qquad C_R=\{y,z,b_0,b_1\}
\]
have four coarse inner-point types
\[
                  (A,B),\quad(A,z),\quad(y,B),\quad(y,z).         \tag{3d3z11s52z30}
\]
The first has a detached \(2+2\) eliminant; the mixed types lose one
anchor and one endpoint label; in the both-inner type every canonical
single-anchor eliminant remains rooted-bad.  Opposite signs at both shared
anchors therefore do not imply a simultaneous converter.

Strong-glue geometry nevertheless gives, for every \(a\in A,b\in B\),
\[
                    A\cup B\in\mathcal F(P),\qquad
                    \{a,y,z,b\}\in\mathcal F(P),         \tag{3d3z11s52z31}
\]
while adjoining either bad anchor to \(A\cup B\) is nonordinary.  The
ordered pair
\[
                     (A\cup B,\{a,y,z,b\})               \tag{3d3z11s52z32}
\]
decodes \(A,B,y,z\) with load one; neither component is a one-face decoder.
In the exact twelve-point wrapper, all \(3600\) double-bad records map to
only \(121\) anchor seams, with maximum one-face load \(108\), while the
two-face map stays injective.

Nor does the circuit pair force a decreasing physical bipartition: an exact
rational eight-point padding retains both circuits and seams, has \(V=121\),
and all \(256\) bipartition mutations have value at least \(121\).
Consequently the precise missing operation is
\[
 \boxed{\text{merge the load-one two-face tensor into one profile/face,
 or use additional tangent/minimum-cell data to bound its fibre.}}       \tag{3d3z11s52z33}
\]
See
`agent_common_shield_mixing/TWO_ANCHOR_DOUBLE_CIRCUIT_ELIMINATION_GATE.md`.

The nearby-anchor/minimum-cell refinement has an exact one-dimensional
form.  For a fixed extension point \(u\), let \(I_R\subset\mathbb{RP}^1\)
be the projectivized inward tangent interval of each ordinary \(R\cup\{u\}\).
For \(v=u+\varepsilon d\), uniformly for small \(\varepsilon\),
\[
             J_Q(u,v)=A_Q(u)-H_u([d]),                 \tag{3d3z11s52z34}
\]
where \(H_u\) is interval depth.  For a weighted interval family of total
mass \(W\) and maximum depth \(h\),
\[
 \sum_{I\cap J\ne\varnothing}w_Iw_J\le2Wh;             \tag{3d3z11s52z35}
\]
thus low depth gives quadratically many disjoint tangent-cone pairs.

That sign information still does not compose the far supports.  A scalable
rational configuration has a convex \(m\)-point child rooted at \(u\) and
a fixed two-point shield whose tangent cone is disjoint from every
rank-\(\ge2\) child cone, but
\[
 F\cup S\cup\{u\}\text{ is ordinary}\quad\Longleftrightarrow\quad |F|\le1.
                                                                  \tag{3d3z11s52z36}
\]
At \(m=14\), only \(14\) of \(16383\) nonempty child traces compose.  A
barycentric identity hides each smaller child label in a triangle formed
by \(u\), a later child label, and one far shield point.  Hence local root
signs and tangent intervals miss the same global anti-alignment.  A valid
splice must retain an ordinary detached-union certificate, control every
cross-support four-set in a lexicographic seam, or bank the marked hiding
circuit with bounded history load.  See
`agent_common_shield_mixing/NEARBY_ANCHOR_TANGENT_INTERVAL_ANTIALIGNMENT_GATE.md`.

A literal shared carrier removes the geometric Helly obstruction.  Let
\(B\subseteq R_i\) be one ordinary carrier and suppose the repair edge
\(e_i\) is an actual boundary edge of both \(B\) and \(R_i\).  Then
\[
                    \mathcal C(R_i,e_i)\subseteq\mathcal C(B,e_i).
                                                               \tag{3d3z11s52z37}
\]
Distinct edge-ear cells of one convex polygon are disjoint.  Hence a
connected pairwise-feasibility graph forces every \(e_i\) to be one
physical edge \(e\), and an infinitesimal point across the relative
interior of \(e\) repairs all contexts simultaneously.  The nine-point
minimizer cage is outside this theorem: its three sources share only one
physical label, not a common edge-bearing carrier.

Simultaneous repair is not yet source multiplication.  There is a rational
nested family with one triangle \(B\), hidden root \(z\), exposed edge
\(uv\), and \(q\) ordinary contexts \(R_t=B\cup\{a_t\}\), for which one
point \(p\) repairs every context but
\[
             R_s\cup R_t\notin\mathcal F(P)\quad(s\ne t).       \tag{3d3z11s52z38}
\]
The complete \(B\)-retaining ledgers before and after relocation have only
\(q+1\) and \(2q+2\) faces.  The common repaired carrier has load \(q\);
the full repaired context has load one but retains only one source index;
the source-pair decoder remains genuinely two-faced.

The hard fractional-Helly branch does admit an exact polynomial
localization.  If ordered bad ear triples have weight at least \(bW^3\),
canonically choose a strict-Farkas certificate with one oriented physical
boundary edge from every context.  With \(M=n(n-1)\) possible oriented
edge-and-side marks and \(H_e\) the context mass on edge \(e\),
\[
                       \max_e H_e\ge {b^{1/3}W\over M}.          \tag{3d3z11s52z39}
\]
If physical source load is \(\lambda\), the fibre has union support
\(p_e\), and that support has face count \(V_e\), fixed-edge projective
normalization gives
\[
 {C_eU_e\over V_e}\ge {H_e\over\lambda V_e}\binom{p_e}{2}.     \tag{3d3z11s52z40}
\]
Writing \(\vartheta=2-\log_2 3\), the exact endpoint-surplus splice still
requires
\[
                  V_e\le {b^{1/3}W p_e^\vartheta\over M\lambda}.\tag{3d3z11s52z41}
\]
Bare edge localization does not imply this support-face upper bound.  The
nested cage is sharp even with zero localization loss: all \(q\) contexts
share \(uv\), but the \(a_t\) form a convex chain, so \(V_e\ge2^q-1\).
That ambient bank is the correct payment in the example; globally it still
needs a recoverable support-bank charge.  See
`agent_common_shield_mixing/FIXED_CARRIER_THREE_EAR_COLLAPSE_AND_NESTED_CAGE.md`.

The exact nine-point cage also fails to scale into a minimizer-safe
vertical obstruction.  For the seed \(S\), every one of its 37 projection
chambers has maximum cap and cup rank five.  Under homogeneous vertical
substitution \(P_d=S[P_{d-1}]\), the exact recurrence contains the forced
mixed term
\[
                 3N^3C_{d-1}U_{d-1},\qquad N=9^{d-1},          \tag{3d3z11s52z42}
\]
and gives
\[
 \log_2V(P_d)=\left({4\over\log_2 9}+o(1)\right)(\log_2|P_d|)^2,
 \qquad {4\over\log_2 9}=1.2618595\ldots .             \tag{3d3z11s52z43}
\]
The maximum face rank is only \(8d-3=O(\log n)\); low rank does not
remove the profile payment.

Literal lifted cage data remain merely polynomial.  Summed over all nodes,
the numbers of marked ear contexts and generously independent same-label
triples satisfy
\[
                         M_d=n^{4+o(1)},\qquad T_d=n^{10+o(1)}, \tag{3d3z11s52z44}
\]
so both have \(2^{-\Theta((\log n)^2)}\) density at any live half scale.
More decisively, at depth two \((n,V)=(81,61014762)\), every one-, two-,
and three-label deletion violates its necessary minimizer comparison.
All \(37^2\) independent macro/micro recharts fail the singleton inequality
at every label; the best gap is still \(-584054\).

Thus repeating the finite Farkas geometry at \(\Theta(\log n)\) scales is
not the missing history.  A live obstruction must instead be a
**continuation-bearing cage**: after coalescing identical physical cage
geometry, a recoverable source/role/depth continuation \(H\) must survive
with total decoder loss \(2^{O(L\log L)}\) and effective mass
\[
                     W_{\rm cage}\ge V(P)2^{-O(L\log L)}.       \tag{3d3z11s52z45}
\]
Whether one canonical live continuation actually coexists through all
three ears is the remaining marked-history obligation; the isolated
minimizer cage and all of its literal vertical lifts fail it.  See
`agent_outer_internal_product/NINE_POINT_EAR_CAGE_VERTICAL_SUBSTITUTION_GATE.md`.

The natural common-role lift answers this obligation negatively for every
rich continuation.  In the exact shear order
`[1,2,3,6,4,5,7,8,0]`, macro role `1` is indeed the first vertex of all
three nine-point source triangles, so one child cap `H` lifts into all
three contexts.  But as soon as `|H|>=2`, any consecutive edge of `H` is
a literal exposed edge common to the three lifted sources.  An
infinitesimal point across it repairs all three simultaneously.  The exact
rank-two witness preserves the hidden macro label while exhibiting one
common repair.  Therefore rich cap terms belong to the repair/profile
branch; only singleton continuations preserve the Farkas cage and supply
merely `n^{O(1)}` possibilities.

There is an exact conditional replacement.  If `W_h` is the mass carrying
literal continuation `h`, `W=sum_h W_h`, and

\[
 K_3=\left({W^3\over\sum_hW_h^3}\right)^{1/2},          \tag{3d3z11s52z46}
\]

then, whenever every `h`-fibre has maximum common-repair depth at most
`eta`, weighted fractional Helly gives same-continuation bad-triple mass

\[
              \sum_h(1-\eta)^3W_h^3
              ={(1-\eta)^3W^3\over K_3^2}.             \tag{3d3z11s52z47}
\]

Retaining `h` makes cross-fibre summation exact, and fixing the three
oriented physical Farkas edges costs fewer than `n^6` choices.  Thus
`K_3<=2^{O(L log L)}` would close the continuation-bearing cage with the
allowed loss.  The current release, unordered colouring, chronology, and
role-forest decoders do **not** bound this collision entropy: they retain
the full pocket/source word and may have `K_3=2^{Theta(L^2)}`.

This is a real correlation gate.  An exact ten-point configuration has
three continuation singletons, each compatible with exactly its own ear
context; every context pair has feasible repair cells, the three-way
intersection is empty, bad ordered mass is at least `2/9`, and
same-continuation bad mass is zero.  Consequently the surviving operations
are a Renyi-3 collision bound, synchronized high-depth repairs retaining
the literal continuation, or direct payment by the dispersed continuation
profile bank.  See
`agent_common_shield_mixing/CONTINUATION_BEARING_THREE_EAR_COALESCING_GATE.md`.

High Renyi dispersion itself has now been reduced without any bucketing
loss.  Aggregate literal source--continuation records into a matrix
`a_(s,h)` of total mass `W` and pair load at most `lambda`; let `G` be the
mass for which `s union h` is an ordinary decoded output and `B=W-G`.
After iteratively pruning light rows and columns, the all-bad remainder has
mass `C>=B/2`, and every surviving face has weighted degree at least
`B/(4V)` and distinct degree at least

\[
                         {B\over4\lambda V}.             \tag{3d3z11s52z48}
\]

Moreover the continuation collision count is preserved:

\[
 K_3(\mathrm{core})
   \ge\left({B\over2W}\right)^{3/2}K_3,\qquad
 {C\over|\mathcal S_*|+|\mathcal H_*|}\ge{B\over4V}.   \tag{3d3z11s52z49}
\]

Thus at the live normalization `W>=V^2/K_0`, with
`K_0=2^{O(L log L)}` and negligible mixed mass, every core face has
`Omega(V/(lambda K_0))` literal incompatible partners.  The residue is a
genuine dense face--face core, not diffuse metadata.

This is also the universal stopping point of Cauchy, Holder, and Hall.  Two
literal face targets give only

\[
                         W\le\lambda V^2,               \tag{3d3z11s52z50}
\]

and a complete bipartite bad matrix attains it.  Exact anti-aligned
parabolic clouds with rank-`r` layers have
`W=binom(p,r)^2`, `K_3=binom(p,r)`, pair load one, and every cross union
bad.  At `r=floor(p/2)` this is `W=V^2/p^{1+o(1)}`.  The Boolean clouds and
rank `Theta(p)` pay, so it is not a live regression; it identifies the next
input exactly as rank-safe downshadows or an internal cap/cup profile bank
inside the one high-minimum-degree core.  See
`agent_common_shield_mixing/RENYI3_CONTINUATION_COLLISION_OR_DENSE_FACE_CORE.md`.

There is an exact return before a common root is retained.  For a convex
\(q\)-gon \(Q\) and opposite exterior chambers \(z_L,z_R\), their far
boundary chains cover \(Q\), so the singleton compatibility profiles obey

\[
                         P_{z_L}P_{z_R}\ge2^q=V(Q).      \tag{3d3z11s53}
\]

If left and right endpoint children export \(K_L,K_R\) faces coexisting
with the corresponding half-source cubes, the two literal load-one banks
give

\[
                         V(P)\ge\sqrt{2^qK_LK_R}.        \tag{3d3z11s54}
\]

The root qualification is essential.  A rational convex \(m\)-point child
can have \(H=2^m\) while two opposite exports through the same retained
root satisfy

\[
 C,U\le1+m+\binom m2,\qquad
 (C,U)=(86,106),\quad CU=9116<2^{14}\quad(m=14).        \tag{3d3z11s55}
\]

Every singleton transversal is ordinary; every rooted child trace of rank
at least three is killed.  Hence induction on the induced child bank does
not supply a rooted return.  The surviving global alternatives are now
literal: release the common root/base with controlled aggregate load,
prove a minimizer-specific rooted-export product, or store the source in
an external return component.

Nor do the two boundary endpoint profiles repair the loss.  If
`J_e=C_eU_e`, and `A,B` outside contexts attach separately to the cap and
cup sides, the exact decoder yields only

\[
                       V^2\ge ABJ_e.                  \tag{3d3z11t}
\]

To reach a one-face target `J_eT`, this would require
`AB>=J_eT^2`, not the natural `AB~T`; reflection minimality enforces the
anti-alignment `(A-B)(C_e-U_e)<=0`.  With `P=sqrt(T)` contexts per side,
even granting every child face to both one-sided banks, the complete trace
complex satisfies

\[
        V_{\rm tr}\le H(1+2P)+(m+1)P^2\le4H\sqrt T,    \tag{3d3z11u}
\]

while `J_eP^2` is already target-sized up to polynomial loss.  Therefore
the few-run route stops at a genuine nonlocal gate: global minimality must
force an ambient multi-label/profile face outside this trace complex, a
mutation which changes the macro configuration, or a bounded one-face
decoder retaining both child and two-sided context.  The construction is
not a sub-half family because those ambient faces are deliberately
uncontrolled.  See
`agent_shield_circuit_cover/RECOVERABLE_CARRIER_COARSENING_MASK_RUN_GATE.md`,
`agent_common_shield_mixing/LONG_RUN_PAIR_STAR_INCIDENCE_BARRIER.md`, and
`agent_outer_internal_product/NEAR_AMBIENT_PAIR_STAR_DIRECTIONAL_RECTANGLE_BARRIER.md`.

A global normalization audit removes the misleading bounded-load reading
of those regressions.  Before pocket replication, let the canonical source
mass be `W`, let `pi(A)` be its actual outside geometric context, and put

\[
 C_{\rm geo}=|\pi(\operatorname{supp}w)|,\qquad
 \Lambda_{\rm proj}=\max_S\sum_{A:\pi(A)=S}w(A).
\]

Then exactly

\[
                         W\le\Lambda_{\rm proj}C_{\rm geo}.       \tag{3d3z11v}
\]

On the near-ambient live slice, `W>=V/2^{O(L log L)}` and
`V>=V(X_R)>=2^{Phi(L-O(loglog L))}`, so

\[
       \log C_{\rm geo}+\log\Lambda_{\rm proj}
                    \ge {1\over2}L^2-O(L\log L).       \tag{3d3z11w}
\]

Consequently the `P^2=2^{O(L loglog L)}` context alphabet in
`(3d3z11u)` cannot carry the live source mass at bounded projection load;
it forces coefficient-half source/carrier reuse.  Restoring every balanced
transversal is impossible too: for `s=alpha L`,

\[
 \log {P_0\over V}=(\alpha-c)L^2-O(L\log L)>0          \tag{3d3z11x}
\]

throughout the excess-rank window `alpha-c>=epsilon`, contradicting
`P_0<=V`.  Thus complete macro products and sparse bounded-load contexts
are closed.  What genuinely survives is coefficient-half source mass
hidden behind one or a few geometric contexts, after the diffuse-ear and
fixed-edge low-load alternatives have failed.  That high projection load
feeds the source/mask/run descent and returns, in the few-run case, to the
same near-ambient coherent-profile problem; the directional square-root
bank can still be no larger than the known source bank.  No entire ambient
low-face regression for this residue is known.  See
`agent_outer_internal_product/NEAR_AMBIENT_LIVE_CONTEXT_COEFFICIENT_AUDIT.md`.

Iterating the high-load deletion on one fixed cyclic role system creates no
additional entropy.  If

\[
 M_0\subseteq M_1\subseteq\cdots\subseteq M_t
\]

are the successive deleted-role masks, every intermediate gap which
survives is already a boundary of the terminal mask.  A terminal mask with
`g` cyclic components has only `2g` directed boundaries, while one deleted
run has length at least `|M_t|/g`.  Thus horizontal iteration returns
exactly to `(3d3z11m)` or `(3d3z11o)`; it cannot accumulate discarded gaps
from different times.

A restart inside the long run is instead a vertical rechart.  If `W_j` is
the mass entering level `j` and `C_j` the number of retained geometric
contexts, the sharp unconditional ledger is only

\[
 W_t\ge {W_0\over\prod_{j<t}C_j},\qquad
 \sum_{j<t}\{\Phi(L_j)-\Phi(L_{j+1})\}
       =\Phi(L_0)-\Phi(L_t).                         \tag{3d3z11y}
\]

Writing `V=2^{Phi(L_0)-r}` and
`Delta_t=Phi(L_0)-Phi(L_t)`, induction forces `r<=Delta_t`, whereas the
iterated endpoint/source Cauchy bank has exponent only

\[
                 \Phi(L_0)-{r+\Delta_t\over2}-O(L\log L).       \tag{3d3z11z}
\]

It therefore need not improve the source bank.  If the terminal runs do
promote into one genuine linear strong-glue chart, the corrected profile
potential closes unless they form an `O(logloglog n)`-coherent ramp.  The
formal exact menu

\[
 C_i=D^{b+i},\qquad U_i=D^{h-b-i},\qquad H_i=D^h,
 \qquad qH\le W_{\rm lin}\le2qH                       \tag{3d3z11z1}
\]

with `q=Theta(loglog n)` has constant corrected potential and misses the
half target by `(1+o(1))L logloglog n`.  It is not asserted planar.  Hence
the precise endpoint is now coherent macro-run profile regeneration after
vertical resets, rather than another mask-count telescope.  See
`agent_outer_internal_product/ITERATED_FEW_RUN_LOAD_PROFILE_GATE.md`.

There is an exact necessary spectrum-width condition for that regeneration.
For one completed `D`-point child with `H` faces, prune its attainable
endpoint menu to the lower Pareto frontier and put

\[
 c_-=\min C,\qquad c_+=\max C,\qquad
 S=\log_{D+1}(c_+/c_-).
\]

The first-to-last term in every genuine `q`-copy linear strong glue is at
least

\[
              W_q\ge H(D+1)^{q-2-S}.                \tag{3d3z11z2}
\]

Indeed it contains `C_0U_{q-1}(D+1)^{q-2}`, while
`U_{q-1}>=H/C_{q-1}`.  Thus `W_q<=KqH` requires

\[
              S\ge q-2-\log_{D+1}(Kq).              \tag{3d3z11z3}
\]

The full 44-point spectrum has only `S=0.502613...` and already forbids the
formal three-role ramp.  The 448-order exact sample of the 134-point parent
has `S=1.174527...`; exact sibling-profile Pareto DP rebounds sharply from
four roles onward.  The sampled statement is evidence only, but
`(3d3z11z2)` is unconditional.  A surviving same-child scalar recycling
scheme must regenerate essentially `q` fresh powers of endpoint-spectrum
width at every vertical reset.  Heterogeneous siblings can instead export
one prescribed profile each and are governed by the two-chart state below.
See
`agent_root_followup/MACRO_RUN_PROFILE_SPECTRUM_WIDTH_GATE.md`.

The exact same-chart endpoint recurrence makes the required reset still
sharper.  For a perfect ramp

\[
 H_i=D^h,\qquad C_i=D^{a+i},\qquad U_i=D^{h-a-i},
\]

the assembled parent satisfies, uniformly in the shift `a`,

\[
 qD^h\le W^+\le2qD^h,
 \qquad \log_D{C^+U^+\over W^+}
          =q-1+O(1/\log D).                         \tag{3d3z11z4}
\]

Here one must keep the binary association fixed: in the right comb `C`
is linear-weighted and `U` product-weighted, while the left comb swaps
those roles.  The tempting pair of simultaneous product formulas mixes
the two associations and is false.  Exact three-block realizations give
`(C,U,W)=(184,376,1124)` and `(392,184,1124)` respectively; nevertheless
their product surplus is the same, so `(3d3z11z4)` is association-safe.

The next unpaid ramp allows surplus only `O(log q)`.  Hence it must export
a genuinely different chamber `beta` with

\[
 \log_D{C_\beta U_\beta\over W^+}=O(\log q),\qquad
 \log_D{C^+U^+\over C_\beta U_\beta}
          \ge q-O(\log q).                           \tag{3d3z11z5}
\]

Thus recursion needs a `D^{q-O(log q)}` two-chart reset, not merely a wide
one-chart menu.  The smallest exact Bellman state presently known retains
`W`, the cap/cup trace tables indexed by their first two and last two
physical labels in the construction and export charts, and the export
macro chamber.  Consecutive-turn seam tests compose these finite jet tables
exactly.  Scalar `(W,C,U)`, same-chart slope alignment, and spurious
same-generation multiquery constraints do not.  See
`agent_outer_internal_product/COHERENT_RAMP_TWO_CHART_BELLMAN_GATE.md`.

At a genuine strong seam the desired third-face storage has one further
exact cap-load split.  At a fixed prefix node write the source face as its
canonical cap/cup pair `D=A(D) union B(D)` and partition continuations by
their next physical label `z`.  The projected tag
`W(D,z)=A(D) union {z}` is ordinary.  If `lambda_A` is the source cap-fibre
size and `m_z` the next-label class size, then

\[
 |\mathcal W|=a q,
 \qquad \operatorname{load}(A\cup\{z\})=\lambda_A m_z,
 \qquad |\mathcal W|\max_{A,z}\lambda_A m_z\ge M m.  \tag{3d3z12}
\]

Hence diffuse projected tags give the missing bounded-load physical branch
faces.  A concentrated cell fixes `(A,z)` and exposes an injective family
of the opposite cup traces `B(D)` together with the continuing prefix
family.  This is a literal one-chamber recursive state, not metadata.
Pascal again makes it sharp: all projected tags lie in the single bank
`C(Y) times Z`, of only half the parent quadratic coefficient, while one
heavy cap fibre contains the opposite cup profile carrying the other half.
The backward profile becomes usable only after an actual reset/cycle; a
reflection is still a different configuration.  Thus the remaining
storage theorem is precisely

\[
 \text{diffuse realized chambers}\Longrightarrow\text{decoded profile cycle},
 \quad\text{or}\quad
 \text{one chamber}\Longrightarrow\text{lossless opposite-profile recursion}.
                                                               \tag{3d3z13}
\]

See
`agent_common_shield_mixing/PROJECTED_SOURCE_CROSS_BRANCH_STORAGE_GATE.md`.

The word “cycle” in `(3d3z13)` now has a precise same-configuration
meaning.  A chamber edge `sigma to tau` is useful only when an actual
two-ended bank satisfies

\[
 |\mathcal B_e|\ge {C_\sigma(Q)U_\tau(Q)S_e\over\Lambda_e}. \tag{3d3z13a}
\]

Writing `E_sigma=(log C_sigma+log U_sigma)/2` and
`rho_sigma=(log U_sigma-log C_sigma)/2`, the `rho` potential telescopes on
every directed cycle of such literal edges.  Consequently some edge on a
cycle obeys

\[
 \log|\mathcal B_e|\ge {1\over|\mathcal C|}
 \left(2\sum_{\sigma\in\mathcal C}E_\sigma
       +\sum_{f\in\mathcal C}\log S_f
       -\sum_{f\in\mathcal C}\log\Lambda_f\right).    \tag{3d3z13b}
\]

Directed-core pruning closes every nonempty realized two-ended core.  If
the core is empty, the graph is a topologically ranked role forest.  A
rational diffuse out-star has many decoded one-ended chamber tags but no
return edge; its query labels form a convex Boolean bank, so it is a
calibration rather than a live counterexample.  The surviving lemma is
exact: a live near-complete chamber DAG must either upgrade a tag to a
two-ended return module or expose an ambient bank while retaining its
carrier/context.  See
`agent_common_shield_mixing/REALIZED_CHAMBER_CYCLE_OR_FOREST_GATE.md`.

What remains is no longer the average-cover entrance: it is to turn this
high-cost adaptive circuit law, or the high-redundancy branch in `(3d3d)`,
into either a decoded ambient circuit/profile bank or the label-primitive
dense context handled by `(3az30t6d)`--`(3az30t6e)`.  A marked
Reed--Solomon/double-parabola regression shows that the selected words can
have only `O(log log n)` disjoint recoverable modules even while every
source has `Theta(log n)` disjoint singleton traces; its ambient convex
chains pay.  Hence the missing promotion must charge ambient geometry, not
extract a Cartesian module from selected support.  See
`agent_common_shield_mixing/WEIGHTED_POSITION_RELEASE_ENTROPY.md`.

The apparent common-root/diffuse-root overlap in this obstruction can in
fact be removed globally.  For a marked incidence `(A,T)`, choose
deterministically a largest rooted-role pocket `X_T` in the circuit
neighborhood of `T`; then `A` and `X_T` are disjoint.  Let `tau(A,T)` be the
minimum number of source vertices meeting the outer trace of every split
four-circuit between `A` and `X_T`, and put

\[
 L_g={n\choose3}\sum_{i=0}^g{n\choose i},\qquad
 H=\min_T V(P|X_T).
\]

If `b_g(A,T)` counts all pairs consisting of a guard `G subseteq A`,
`|G|<=g`, and a pocket face `F` for which `(A setminus G) union F` is a
face, the output face and the guessed `(T,G)` recover both `A` and `F`.
Consequently

\[
       \sum_{(A,T)}b_g(A,T)\le L_gV,                     \tag{3e}
\]

and, with `alpha=(n-2mu)/(2(n-3))`,

\[
 { |\{(A,T):\tau(A,T)\le g\}|\over |\mathscr I|}
       \le {L_g\over\alpha H}.                          \tag{3f}
\]

Here the guard criterion is exact: deleting `G` releases **every** pocket
face iff `G` covers all split-circuit outer traces.  Using the established
quarter-coefficient bound inside `X_T`, every fixed `gamma<1/4` and
`g=floor(gamma log n)` make the right side of (3f) exponentially small in
`(log n)^2`.  Thus almost every weighted low-mean source has a rank-at-most
three outer-trace hypergraph with transversal number `>gamma log n`, hence a
matching of more than `(gamma/3-o(1))log n` disjoint shield traces.  Root
entropy is therefore only polynomial; the exact minimizer residue is to
multiply these disjoint source shields by the common full pocket repair
alphabet.  See
`agent_outer_internal_product/GLOBAL_MARKED_POCKET_RELEASE.md`.

The matching conclusion is sharp as a local statement.  Three tiny convex
outer arcs can supply `q` disjoint triple traces, while one convex pocket
`X` lies in every transversal triangle.  All `q|X|` split circuits then use
the same actual role-pocket, every guard of size `<q` fails even for one
fixed pocket point, and the natural matched-toggle guards fail except for
the constant words.  Even two pocket banks collapse under union from
`4^m` records to `2^m` outputs with fibre `3^{|U|}`.  Thus (3f) reduces the
minimizer route to **internal** pocket-trace diversity; disjoint outer
shields alone cannot supply the missing power.  This is a regression, not a
global counterexample, and is verified in
`agent_outer_internal_product/DISJOINT_SHIELD_COMMON_POCKET_REGRESSION.md`.

There is nevertheless an exact positive internal-diversity branch.  After
deleting one root label, suppose the remaining split-circuit system has a
`K`-recoverable decomposition into private cells `(O_j,X_j)`: every bad
four-circuit meeting `X_j` is contained in its own `O_j union X_j`.  A mixed
cell may use either its full outer state or any pocket face, while a pure
cell uses any pocket face.  All choices coexist, and the output recovers the
weighted source after guessing one retained root edge, the missing label,
and the profile.  Thus

\[
 \sum_{(A,T)}
   \prod_{O_j\ne\varnothing}(1+V(X_j))
   \prod_{O_j=\varnothing}V(X_j)
       \le n{R\choose2}K,V.                             \tag{3g}
\]

In particular, two private subpockets give their full face-count product,
and `k` private singleton cells give an exact `3^k` toggle bank.  The common
cage is projectively universal, however: an arbitrary child order type can
be shrunk into it while external circuits merge all child pieces into one
mixed cell.  Hence the unresolved alternative is precisely privacy or
alternation forced by the *marked shield history*, not diversity of the
unmarked pocket order type.  See
`agent_outer_internal_product/RECOVERABLE_COMPONENT_TOGGLE_BRANCH.md`.

Nor does the disjoint-trace matching force private cells with positive
frequency.  A reinforced three-arc cage has `q=Theta(log n)` disjoint
transversal traces and an arbitrary common pocket, but after deleting any
root label every surviving shield and pocket label belongs to one circuit
component.  The singleton guard number can be `p>>q`; only two or three
minimum guard profiles occur, shared by every pocket label, and all `3^q`
matched toggles fail when `q<p`.  Its locally guaranteed secondary bank is
only `O(n)`, below the retained-edge decoder cost.  Thus the remaining
minimizer lemma needs a genuinely **global external-codegree/profile-entropy
split across source contexts**; matching-versus-merger prevalence alone is
false.  See
`agent_outer_internal_product/PREVALENCE_COMMON_CAGE_REGRESSION.md`.

The bounded-rank minimizer slice supplies exactly half of that split.  For a
canonical rooted profile `pi=(T,z,G,X)`, let `w_pi` be its source weight,
`g_pi=|G|`, `m_pi=|X|`, and let `mathcal K` be the largest number of profiles
listed for one root.  The carrier bank `(A setminus G) union D`, with
`z in D subseteq G`, contains the full root; the completion bank
`(A setminus G) union {x}`, `x in X`, retains the other root edge.  Their
overlaps are at most `binom(R,3)mathcal K` and
`n binom(R,2)mathcal K`, respectively, so one global Cauchy inequality gives

\[
 \sum_\pi w_\pi\sqrt{2^{g_\pi-1}m_\pi}
 \le \mathcal K
       \sqrt{{R\choose3}\,n{R\choose2}}\,V.             \tag{3h}
\]

Consequently, if a positive fraction of the weighted mass has
`g>=gamma log n`, `m>=n/polylog(n)`, and `R=polylog(n)`, then either the
ordinary-face banks close the branch or one root carries
`mathcal K>=n^{gamma/2-o(1)}` distinct canonical guard profiles.  This also
eliminates the apparent single-cage quadratic-entropy regression on the live
rank-`O(log n)` slice: a fixed carrier of rank `O((log n)^2)` supports only
`2^{O((log n)log log n)}` such sources.  Thus the exact remaining minimizer
atom is **heavy profile entropy**, not one common cage.  The profile faces
and their full guard downsets give a fixed-power absolute reservoir, but a
recoverable multiplication of that reservoir by the ambient source mass is
still open.  See
`agent_outer_internal_product/WEIGHTED_PROFILE_SQUARE_GATE.md`.

For one heavy root, the first divergence of those profiles is also exact.
Let `mathscr B` be the released carriers `B=A setminus G`, let `k_B` be the
number of distinct size-`g` guards over one carrier, and let `m=|X|` be the
common singleton-completion alphabet.  The faces `B union {x}` are injective
in `(B,x)`.  Within one carrier fibre, removing the common root label from
the guards gives a uniform family whose entire downshadow joins the carrier.
If `k_B=binom(x,g-1)` and
`Phi_(g-1)(k_B)=sum_(i<=g-1)binom(x,i)`, Lovasz--Kruskal--Katona yields

\[
 V\ge
 \max\left\{m|\mathscr B|,
       \max_{B\in\mathscr B}\Phi_{g-1}(k_B)\right\}.    \tag{3i}
\]

For `g=gamma log n` and `k_B=n^{kappa+o(1)}`, the shadow has a fixed-power
surplus whenever `kappa<2gamma`; the threshold is sharp.  A rational
bounded-rank regression takes every `r`-subset of an `s`-point convex guard
pool over one carrier.  All `binom(s,r)m` completion records collapse to the
same `m` faces, while the guard bank is exactly

\[
                    \sum_{i\le r}{s\choose i}.          \tag{3j}
\]

With `s,r=Theta(log n)` this realizes polynomially many actual canonical
profiles while keeping source and maximum face rank `O(log n)`.  It does
not carry `Theta(V)` marked mass: a global obstruction would require
quadratically many such carrier fibres without an aggregate completion or
shadow decoder.  This is now the precise heavy-profile summation gate.  See
`agent_outer_internal_product/HEAVY_PROFILE_FIRST_DIVERGENCE.md`.

That summation gate can itself be written with exact global overlaps.  On a
rank-`h` source slice, index carrier fibres by `c=(T,z,B)`, and let `k_c` be
the guard multiplicity, `m_c` the singleton alphabet, and `s_c` the rooted
guard-downshadow size.  The shadow and completion banks have total output
loads at most

\[
 L_S=3{h\choose3}\sum_{i=0}^{g-1}{h-3\choose i},
 \qquad L_C=n{h\choose2}.                               \tag{3k}
\]

Indeed, a shadow output contains the full root and is decoded by guessing its
small deleted guard subset, while a completion output retains the root edge
and is decoded after guessing the missing root label.  One recoverable-cell
Cauchy step, over **all** roots and fibres at once, gives

\[
 \sum_c k_c
 \le
 \sqrt{L_SL_C\max_c {k_c^2\over m_cs_c}}\,V
 \le
 \sqrt{L_SL_C\max_c {k_c^2\over
            m_c\Phi_{g-1}(k_c)}}\,V.                    \tag{3l}
\]

Thus the hard mass is impossible whenever
`m_c Phi_(g-1)(k_c)>=n^eta L_S L_C k_c^2` uniformly on its
fibres.  This is a genuine global telescope: it never spends a separate copy
of `V` per carrier.  For `h=C_0 log n`, `g=gamma log n`,
`m_c>=n/polylog(n)`, and
`Phi(k_c)=k_c n^{delta+o(1)}`, `k_c=n^{kappa+o(1)}`, it closes precisely when

\[
                 \delta>\kappa+C_0H(\gamma/C_0).        \tag{3m}
\]

The apparent complete-layer obstruction admits a further planar lift.  If a
uniform guard family `mathcal F subseteq binom(U,r)`, `r>=4`, covers every
four-subset of its `s`-label support `U`, then four-circuit locality forces the
entire union carrier `B union {z} union U` to be convex.  It is enough that

\[
 |\mathcal F|>{s\choose r}-{s-4\choose r-4},             \tag{3n}
\]

and a complete layer is the special case.  Thus its bank is the full Boolean
cube `2^s`, not merely the truncated KK shadow.  If `b` bounds carrier rank,
`q` bounds union-output rank, and

\[
 L_U=3{q\choose3}\sum_{i=0}^{b-2}{q-3\choose i},
 \qquad L_C=n{b+1\choose2},                              \tag{3o}
\]

then the root/carrier decoders and one global Cauchy step give

\[
 \sum_c k_c\le
 \sqrt{L_UL_C\max_c{k_c^2\over m_c2^{s_c}}}\,V.         \tag{3p}
\]

This closes every four-trace-covering complete core with
`s/log n -> infinity` on the live slice `b=O(log n)`, `r=Theta(log n)`,
`m>=n/polylog(n)`.  It does not close the central logarithmic bin: for
`r=s/2=Theta(log n)`, the square demand `k_c^2/2^s=2^{s-o(s)}` can consume
the whole cube before the explicit decoder loss.  The last complete-layer
obstruction is therefore confined to `s=O(log n)` and still requires a
global prevalence/stability theorem across quadratically many cells.  No
logarithmic-rank planar construction is known that realizes it on `Theta(V)`
weighted mass.  See
`agent_outer_internal_product/COMPLETE_GUARD_LAYER_UNION_LIFT.md` and
`agent_outer_internal_product/GLOBAL_CARRIER_FIBRE_TELESCOPE.md`.

There is an exact stability statement, but it also identifies the limit of
every carrier-local approach.  Project all bad planar four-subsets of
`B union {z} union U` onto their nonempty traces in `U`, obtaining a
rank-at-most-four hypergraph `mathcal H`.  Then

\[
 B\cup\{z\}\cup D\text{ is convex}
 \quad\Longleftrightarrow\quad D\text{ is independent in }\mathcal H.
                                                               \tag{3q}
\]

If `tau_c` is its transversal number, deleting a canonical minimum
transversal releases a full `2^{s_c-tau_c}` cube with the same global
decoder as `(3o)`, and hence

\[
 \sum_c k_c\le
 \sqrt{L_JL_C\max_c{k_c^2\over m_c2^{s_c-\tau_c}}}\,V,
 \qquad \tau_c\le4\nu_c,                                \tag{3r}
\]

where `nu_c` is the maximum number of disjoint geometric circuit traces.
Thus failure forces linearly many disjoint *actual* bad traces, not merely
uncovered combinatorial four-sets.

Even the full cube is not locally sufficient.  A scalable concave-parabola
cell with `s=2r=Theta(log n)` has every rank-`r` guard and the whole `2^s`
carrier/core bank, together with an arbitrary common pocket alphabet `X`,
but every carrier-retaining mixed set containing a nonempty core choice and
a point of `X` is nonconvex.  At the exact decoder scale its local square
factor is at least

\[
                    {\binom{2r}{r}\over2^r}=2^{r-o(r)}.  \tag{3s}
\]

This regression has only polynomial marked mass, so it is not a global
counterexample.  It proves that the last step must be cross-fibre
prevalence/multiplication: no stronger local container, uncovered-trace, or
carrier-retaining mixed-bank lemma can close it.  See
`agent_outer_internal_product/CIRCUIT_TRANSVERSAL_CENTRAL_LAYER_BARRIER.md`.

The first global prevalence step is exact.  In the uniform central model put
`a=4^r`, `k=binom(2r,r)`, and let `d(F)` be the number of released cubes
containing the ordinary face `F`.  If a cell is `Delta`-light when at least
half its cube has degree at most `Delta`, then

\[
 M_{\rm light}\le {2k\Delta\over a}V
       =O\!\left({\Delta\over\sqrt r}\right)V,           \tag{3t}
\]

while the high cells supply genuine ordered cross-fibre collision energy

\[
 \sum_{c\ne c'}|\mathcal A_c\cap\mathcal A_{c'}|
 =\sum_Fd(F)(d(F)-1)
 \ge {\Delta a\over2k}M_{\rm high}.                      \tag{3u}
\]

Thus `Delta=r^(1/3)` removes every positive-mass light slice without a
decoder or per-cell copy of `V`.  Conditional on one fixed anchor face, the
completion decoder also improves from a missing-root factor `n` to
`q binom(b+1,2)`, which would give a fixed-power gain.  The remaining
quantifier is global: `(3u)` gives many polylogarithmic-degree anchors, not
one anchor carrying positive mass.  A multi-root parabola regression
saturates this distinction—more than half of every cube has degree `>r`,
all completion banks coincide, and all carrier-retaining mixed outputs are
nonconvex—yet it has only polynomial marked mass.  The next theorem must use
the anchor/carrier entropy forced by `Theta(V)` mass, not heavy overlap by
itself.  See
`agent_outer_internal_product/GLOBAL_CUBE_PREVALENCE_GATE.md`.

The cross-anchor summation can in fact be completed up to one explicit
overlap exponent.  Group central cells by their ordinary top face
`Q_c=B_c union {z_c} union U_c`.  Let `R` be the maximum number of cells in
one top group, `lambda` the maximum multiplicity of one completion output
inside one group, `rho` the maximum number of distinct top groups sharing a
completion face, and `m` the common completion-alphabet size.  The top faces
themselves form an overlap-one anchor bank.  Within a group the union of its
completion banks has size at least `mN_Q/lambda`; applying Cauchy once over
all groups gives the exact global telescope

\[
                     M\le k\sqrt{{\lambda R\rho\over m}}\,V.  \tag{3v}
\]

No copy of `V` is spent per anchor.  The exact decoder bounds are

\[
 \lambda\le q{b+1\choose2},\qquad
 R\le3{q\choose3}\sum_{i=0}^{b-2}{q-3\choose i},
 \qquad \rho\le n{b+1\choose2}.                         \tag{3w}
\]

Thus if `k=n^{kappa+o(1)}`, `m=n^{1-o(1)}`,
`R=n^{alpha+o(1)}`, and `rho=n^{beta+o(1)}`, the central bin has a fixed
power saving whenever

\[
                            2\kappa+\alpha+\beta<1.       \tag{3x}
\]

For `r=gamma log n`, this reads `4gamma+alpha+beta<1`.
Failure is no longer an amorphous cross-anchor collision.  One completion
face shared by `h` top groups contains, after a polylogarithmic loss, groups
with the same carrier `B`, pocket label `x`, and retained root edge `e`, but
pairwise distinct missing roots `z` and distinct ordinary top shields `Q_z`.
This is a recoverable **root--shield star**.  The multi-root parabola remains
a sharp polynomial-mass local model, but it lies in one top group and does
not refute `(3v)`.  The remaining central theorem is precisely to discharge
a fixed-power cross-top root--shield star, or to show that its entropy
constants cannot support `Theta(V)` marked mass.  See
`agent_outer_internal_product/CROSS_ANCHOR_COMPLETION_TELESCOPE.md`.

Each root--shield star has two further exact linear banks.  For a convex
rank-`q` top `Q_z`, the root-marked downset has `2^{q-1}` faces.  If the
common pocket label `x` lies inside the root triangle, the line `xz` splits
`Q_z-{z}`; on either open side `H`, every set `{x,z} union S`, `S subseteq H`,
is convex.  The richer side therefore supplies at least
`2^{ceil((q-1)/2)}` pocket-retaining faces.  For a disjoint global family of
stars let `omega_D,omega_H` be the maximum cross-star overlaps of these two
banks.  If each root has marked weight `k`, then

\[
 M\le\min\left\{
 {qk\omega_D\over2^{q-1}},
 {qk\omega_H\over2^{\lceil(q-1)/2\rceil}}
 \right\}V.                                             \tag{3y}
\]

For `q=b+1+2r`, `k=binom(2r,r)`, the downset closes whenever
`b/log n` exceeds the overlap exponent; the pocket bank closes when
`b>2r+2log_2omega_H+o(log n)`.  High half-plane reuse has an exact first
divergence: one output fixes `(x,z)`, leaving many pairwise distinct retained
edges, carriers, and top shields.  Thus the central residue is now either a
small-carrier star or fixed-power reuse of one of two explicit ordinary-face
banks.  The polynomial-mass parabola model sits sharply in the small-carrier
case.  See `agent_outer_internal_product/HALFPLANE_ROOT_SHIELD_GATE.md`.

Retaining the completion face removes the remaining *decoder* ambiguity.
For a canonical incidence `(Y=B union {x},Q,z,e)` and one half-plane output
`F`, the pair `(Y,F)` recovers the cell after guessing
`x in Y cap F`, `z in F-Y`, and `e subseteq Y-{x}`.  Therefore

\[
 \sum_c2^{\lceil(|Q_c|-1)/2\rceil}
 \le\left\lfloor{q^2\over4}\right\rfloor{b\choose2}V(P)^2. \tag{3z}
\]

Equivalently, low `(x,z,F)` codegree releases many distinct half-plane
faces, while a high fibre releases many distinct completion faces after only
the `binom(b,2)` retained-edge loss.  Thus no unrecorded history coordinate
survives inside the star.  Equation `(3z)` is still a **two-face square**
bound; converting it to the linear fixed-power EIC charge requires the
marked-source weights to populate the two banks with the correct Cauchy
balance.  See
`agent_common_shield_mixing/ROOT_SHIELD_MARKED_HALFPLANE_BANK.md`.

That balance has an exact sharp potential.  Give incidence `c` marked weight
`k_c`, completion `Y_c`, and a half-plane bank `H_c` of size `B_c`; distribute
`k_c/B_c` on every pair `(Y_c,F)`, `F in H_c`, and put

\[
 \mathcal E=\sum_{Y,F}\left(
   \sum_{c:Y_c=Y,\ F\in H_c}{k_c\over B_c}
 \right)^2.
 \qquad
                         \sum_ck_c\le V\sqrt{\mathcal E}. \tag{3aa}
\]

If the pair decoder has load at most `L`, then

\[
 \mathcal E\le L\sum_c{k_c^2\over B_c};
 \quad
 \sum_c{k_c^2\over B_c}\le {D^{2-2\epsilon}\over L}
 \Longrightarrow \sum_ck_c\le D^{1-\epsilon}V.          \tag{3ab}
\]

Both inequalities are Cauchy-sharp.  Complete middle layers do **not** imply
the energy hypothesis: a rational common-top construction with
`N=binom(2a,a)` carriers, complete weight
`k=binom(3a,floor(3a/2))`, common bank `B=2^{2a+1}`, and pair load one has
`mathcal E=Nk^2/B=2^{6a-O(log a)}`.  Its marked mass exceeds the ambient
face count by a fixed power, although it lacks the full external degree-`D`
record system and is not an EIC counterexample.  Thus local root geometry,
complete guards, and pair recovery are exhausted: the next input must be a
**global prevalence/energy bound tied to the external blocker cap**.  See
`agent_common_shield_mixing/ROOT_SHIELD_SQUARE_LINEAR_ENERGY.md`.

Even the full *formal* bank system does not imply that prevalence bound.
There is a scalable hereditary four-local complex with `b=2`,
`q=2r+3`, `k=binom(2r,r)`, and `m=Theta(n)`, whose cells are indexed by a
carrier edge `e` and a root `z`.  Completion faces `Y_(e,x)` are reused along
the root axis, while marked half-plane faces `F_(z,x,S)` are reused along the
independent carrier axis, yet

\[
             (Y_{e,x},F_{z,x,S})\text{ determines }(e,z,x,S)          \tag{3ac}
\]

with multiplicity one.  Adding an independent four-partite background bank
produces an exact hereditary complex satisfying planar four-locality, with
full cubes and complete middle layers, for which

\[
                              V=(1+o(1))M.              \tag{3ad}
\]

This is not a fake gain from arbitrary mark duplication: for each carrier
edge and each root block, every underlying source has exactly `r+1` possible
root marks, by

\[
 (2r+1){2r\choose r}=(r+1){2r+1\choose r+1}.             \tag{3ae}
\]

Thus the marked-to-unmarked load is only `O(log n)` on the live bounded-rank
scale.

Thus bank cardinalities, aggregate cube degrees, pair injectivity, heredity,
and the rule “a set is convex iff all its four-subsets are convex” still
cannot yield a fixed-power saving.  This particular background-inflated
model is **not** a planar order type.  However, the stronger hope that
planarity forbids the perpendicular rectangle is false.  For fixed blocker
`x` and root `z`, normalize `x=(0,0),z=(0,1)` and write carrier labels on
opposite sides as `u=(-a,b),v=(c,d)`.  Then

\[
 x\in\operatorname{int}\triangle(u,v,z)
 \quad\Longleftrightarrow\quad {b\over a}+{d\over c}<0. \tag{3af}
\]

The carrier graph is therefore Ferrers and an `m`-edge graph contains a
complete bipartite subgraph of area at least `m/H_s`.  The logarithm is not
a fixed-power gain.  More decisively, three short arcs around a triangle
realize complete `L times R` carrier rectangles, arbitrary root blocks of
size `2h+1`, a common blocker alphabet, complete middle weight
`binom(2h,h)`, and the two perpendicular banks with pair load at most
`2h+1`.  An underlying source has exactly `h+1` root marks.  What this
realization necessarily exposes is the detached convex outer shield

\[
                    L\cup R\cup\bigcup W,                \tag{3ag}
\]

with its full Boolean face complex.  Hence the correct planar target is a
**rectangle-or-shield global telescope**, not rectangle exclusion.  See
`agent_outer_internal_product/SQUARE_TO_LINEAR_RECTANGLE_BARRIER.md` and
`agent_common_shield_mixing/EXTERNAL_ALPHABET_ENERGY_TRICHOTOMY.md`.

Restoring the full selected blocker alphabet gives an exact companion
split.  If `mathcal J` is the diagonal inverse-bank energy and `mathcal C`
the genuine common-completion collision energy, then

\[
 \mathcal E_D=\mathcal J+\mathcal C,
 \qquad
 \mathbb E_\xi\mathcal E(\xi)
     ={\mathcal J\over D}+{\mathcal C\over D^2}.         \tag{3ah}
\]

Only `mathcal C` localizes quadratically; the diagonal survives one-letter
thinning at rate `1/D`.  If `s` distinct sources each select `D` blockers,
the actual blocker union supplies the exact fallback

\[
 { |E|\over V(P)}\le
       \min\left\{D,{sD\over f(D)}\right\}.              \tag{3ai}
\]

Thus `s<=f(D)/D^epsilon` already closes EIC'.  Every surviving diagonal
branch has quadratic source entropy in `log D`; every collision-dominated
branch localizes, after only a polynomial rank loss, to a fixed completion,
blocker, and retained edge.  A planar full-cap example shows that diagonal
energy can exceed `D^2` with pair load and completion multiplicity one, but
its detached blocker shield pays by `(3ai)`.  The live branch is exactly
quadratic source entropy **and** high detached-shield reuse across those
sources.

The carrier endpoint alphabet has the same exact cutoff.  If `s` rooted
profiles each use `R` carrier edges, their key-face load is `lambda`, and
`d_R` is least with `binom(d_R,2)>=R`, then

\[
 {sR\over V(P)}\le
       \min\left\{\lambda R,{sR\over f(d_R)}\right\}.    \tag{3aj}
\]

Since `d_R=R^{1/2+o(1)}`, failure of an `R^epsilon` gain forces
`log s>=(1/16-o(1))(log R)^2`; the exact `r+1` root-mark load changes only
the lower-order term.  A convex endpoint union upgrades `f(d_R)` to
`2^{d_R}`.  Thus every easy detached carrier alphabet is discharged
globally, with no copy of `V` per profile.  The residue is quadratically
many overlapping profile contexts.  Their entropy cannot be substituted
for the disjoint macro positions in the upper-jump theorem: a three-cluster
wrapper has `log 3=O(1)` macro scale, large uniform families have only
`2^{O(log n)}` disjoint members, and tiny reflected child substitutions
preserve Ferrers signs while allowing quadratic cap/cup skew.  A coefficient
closure still needs a new positive-log-scale block-core extraction with high
mean and controlled common skew.  See
`agent_outer_internal_product/CARRIER_ALPHABET_SQUARE_GATE.md` and
`agent_outer_internal_product/FERRERS_UPPER_JUMP_APPLICABILITY_GATE.md`.

All currently available rectangle, blocker, Ferrers, half-plane, outer,
one-gap, and anchor banks admit one exact global consolidation.  Give cell
`c` demand `m_c`, let `mathcal B_c` be the union of its ordinary-face banks,
and fractionally route `m_c` over `mathcal B_c`.  If `lambda_*` is the least
possible maximum load on one face, finite LP duality gives

\[
 \lambda_*=
 \max_{\substack{\mu_F\ge0\\\sum_F\mu_F=1}}
 \sum_c m_c\min_{F\in\mathcal B_c}\mu_F
 =\max_{\varnothing\ne\mathcal A\subseteq\mathcal C}
 {\sum_{c\in\mathcal A}m_c\over
  |\bigcup_{c\in\mathcal A}\mathcal B_c|},
 \qquad
 \sum_c m_c\le\lambda_*V(P).                           \tag{3ak}
\]

Thus the rectangle-or-shield theorem needed by EIC' is precisely
`lambda_*<=n^{o(1)}D^{1-epsilon}`.  Failure is stronger than high raw
overlap: one probability pricing `mu` on actual faces makes *every* available
bank expensive in aggregate.  The three-arc and full MARK tensors are not
counterexamples to this statement.  One three-arc context has only linear
source entropy and is super-paid by its blocker/outer shields; the full MARK
tensor either has a small support paid by `f(D)`, or four-locality forces its
whole upper core to be convex.  A genuine obstruction must therefore have
quadratic context entropy and simultaneously reuse all of the banks in
`mathcal B_c`.  See
`agent_common_shield_mixing/GLOBAL_FERRERS_SHIELD_TELESCOPE.md`.

The Hall obstruction can be pruned further.  For singleton records
`(R,x,p)` of source/target rank at most `q`, suppose the bank union contains
the three anchor projections `(R,x)`, `(R,p)`, and `(x,p)`.  If a record
subfamily `mathcal A` has Hall density

\[
 \lambda_{\mathcal A}={|\mathcal A|\over
  |\bigcup_{g\in\mathcal A}\mathcal B_g|},              \tag{3al}
\]

iteratively deleting a projection vertex of degree below
`lambda_A/[4(q+1)]` removes fewer than half the records.  Hence a
remaining half-subfamily has minimum degree at least that threshold in
**all three** projections.  In a fixed retained core/insertion edge, the
ear--blocker graph is the exact two-dimensional dominance relation, so every
surviving component has at least `d` labels on each side and `d^2` records.
This rules out every sparse-star or isolated radial anomaly as a Hall
counterexample.

There is also an exact entropy cutoff for an exposed convex shield `O`.  If
`M` rank-at-most-`q` hidden cores are decoded with fibre `K` from subsets of
`O`, then

\[
             M\le K\sum_{i=0}^{q}{|O|\choose i}.         \tag{3am}
\]

Thus quadratic core entropy at `q=O(log D)` either makes `|O|` a fixed power
of `D` (whose Boolean bank overwhelms the demand), or remains as quadratic
**conditional** entropy in labels outside every exposed shield.  Combined
with `(3al)`, the surviving Hall obstruction is a dense minimum-degree
dominance family with hidden-core quadratic entropy and quadratic directional
cap/cup anti-alignment.  See
`agent_one_sided_reflection/AGGREGATE_CIRCUIT_SHIELD_ANTI_ALIGNMENT.md`.

The quadratic blocker reservoir then removes the remaining global mark and
tangent ambiguity.  If `C` equal-demand-`m` contexts of Hall density `rho`
each supply at least `K` actual marked shield incidences `(p,F)`, with
`|F|<=h`, then double counting the at most `h|mathcal U|` marked face bins
gives one shared mark/face, and after at most `T` tangent states one has

\[
 \max_{p,F,\tau}|\{c:(p,F,\tau)\text{ occurs in }c\}|
       \ge {K\rho\over hmT}.                             \tag{3an}
\]

Thus `K=2^{(a-o(1))(log D)^2}` and polynomial `h,m,T` preserve the full
quadratic coefficient inside one fixed `(p,F,tau)` omitted-petal fibre.
Moreover, an inclusion-minimal Hall maximizer gives every demand-`m_c`
context fewer than `m_c/rho` private targets, so every large
context-decodable splice bank has already exited.  This localization is
best possible from incidence data alone: tensor powers of projective-plane
incidence have quadratic bank degree, no private targets, and unique maximal
Hall density, but no common-bank tensor.  They are non-Ferrers and therefore
not planar regressions.  The remaining input is exactly the planar
first-divergence/Ferrers/circuit structure inside the fixed omitted-petal
fibre.  See `agent_common_shield_mixing/DENSE_HALL_ROOTED_FIBRE.md`.

Ordinary directional skew is not an additional bounded-rank escape.  If
`Q` is a convex `p`-petal and `C(Q),U(Q)` are its two rooted directional
counts, then

\[
 C(Q)U(Q)\ge 2^p-1,\qquad
 \left|{1\over2}\log{U(Q)\over C(Q)}\right|
       \le {p-\log p\over2}.                            \tag{3ao}
\]

Consequently `h` equal-rank petals contain `h/(p+1)` petals in one
unit-width skew bin, and every forward cap--cup product within that bin is
at least `(2^p-1)/2`.  Moreover, if a rank-at-most-`q` completion family has
compatibility maximum degree `Delta`, repeated Erdos--Rado extraction
partitions all but

\[
       (q+1)(\Delta+1)q!(h-1)^q                         \tag{3ap}
\]

members into pairwise-incompatible `h`-sunflowers.  Thus a quadratic-entropy
family with `q=O(log D)` and fixed-power `Delta` is, up to a quadratically
negligible remainder, covered by power-size sunflowers.  If the two endpoint
traces of their petals glue to ordinary faces with global multiplicity
`Lambda`, the resulting bank has size at least

\[
          {M_0h\over8(q+1)^2\Lambda}.                   \tag{3aq}
\]

For `h=D^rho`, this gives a fixed-power gain whenever
`Lambda<=D^(rho-epsilon)`.  Hence neither bounded-rank cap/cup skew nor the
sunflower extraction is the final obstruction.  It is precisely the
recoverable two-ended gluing, or its global reuse, after exposed Boolean
shields have already been charged.  The exact ACP overlap regression has
quadratic untagged reuse but is paid by one convex outer shield, so it is not
Hall-dense.  See
`agent_one_sided_reflection/BOUNDED_RANK_SKEW_SUNFLOWER_GATE.md`.

There is an even cheaper globally decoded test.  For a sunflower
`C_i=K dotcup Q_i`, test every mixed one-label extension
`C_i union {b}`, `b in Q_j`, `i!=j`.  Either the ordinary outputs form a
bank of size at least

\[
             {M_0(h-1)\over4(q+1)},                     \tag{3ar}
\]

or sunflowers covering at least half the completions each have one carrier
triple and a common-role rooted circuit container of size
`(h-1)/(8 binom(q,3))`.  The weighted version is exact but exposes the last
loss: in a dyadic band `w<=w_i<2w`, the good-extension bank is only

\[
       |\mathcal B|\ge
       {W_0(h-1)p\over8w(q+1)}.                          \tag{3as}
\]

The denominator `w` is unavoidable because an ordinary output records a
completion once, not its radial-history multiplicity.  It disappears only
when each unit of reciprocal-capture weight is realized by a coexisting
cap/interval tag with bounded global decoder load.  Thus the weighted KL
demand `(23r10f)` cannot be fed into the sunflower support theorem as a
scalar: the interval reservoir itself must survive in the mixed output.

For the literal reservoir routing this tag can be fixed exactly.  The
normalized load on an interval face `W` is

\[
 \ell(W)={1\over4}\sum_{e,j:W\subseteq I_e}h_{j,e},\qquad
 \sum_jS_j=\mathbb E_{W\sim\pi}\ell(W).                 \tag{3at}
\]

The unqualified maximum here is vacuous because the empty face belongs to
every interval.  The useful quantity is the blocked part: compatible
`W union e` contributes exactly `M=sum_jtau_j` in expectation, whereas

\[
       \mathbb E_\pi\ell_-(W)=\sum_jS_j-M.              \tag{3at1}
\]

Thus fixed-power **excess** fixes an actually blocked target of rank at
least two.

Put `eta_e=sum_(j:W subset I_e)h_(j,e)`,
`H_W=sum_e eta_e`, and `eta_*=max_e eta_e`.  An exact planar split now
gives either at least

\[
                    {H_W\over2\eta_*}                   \tag{3au}
\]

distinct ordinary faces `W union e`, or one canonical bad-circuit cell of
load at least

\[
 {H_W\over16(\binom{|W|}{2}+\binom{|W|}{3})}            \tag{3av}
\]

and endpoint-pair support at least the same quantity divided by `eta_*`.
That support has a star or matching of square-root size; even the sole
degenerate trace-three star either produces another `W`-retaining bank or
a genuinely varying common-role rooted alphabet at polynomial loss.  Thus,
for `|W|=O(log n)`, a large common-target load yields a retaining bank, one
high-history endpoint cell, or a fixed-power rooted circuit alphabet.  The
remaining erasure is exact: the bad branch retains the witness trace
`A subset W`, but reattaching `W-A` can recreate circuits.  One second face
must retain that discarded trace, or its face complex must be charged before
descent.

Even without compatibility, the endpoint support has a detached cubic
shield.  It contains `X` with

\[
 |X|\ge\sqrt{H_W/(2\eta_*)},\qquad
 F_X(1/2)\ge {|X|^3\over288}.                            \tag{3ay}
\]

This capacity pays the full normalized contribution of `W` whenever
`eta_*<=H_W^(1/3)2^(2(|W|+2)/3)/(2\,288^(2/3))`; otherwise one endpoint
cell has the corresponding large radial tilt.  The caveat is global rather
than local: the same detached `X` can be reused by many different `W`, which
is why the circuit trace and its recovery remain necessary.

The same common-`W` fibre passes exactly through the marked Hall
localization with its likelihood weights intact.  If its occurrences have
total weight `H`, actual target-bank union `mathcal U`, at least `K` marked
shield faces of rank at most `b` per occurrence, and at most `T` tangent
states, then either

\[
 H\le D_0^{1-\epsilon}|\mathcal U|,
 \quad\hbox{or some fixed }(p,F,\tau)\hbox{ has weight }
       >{K D_0^{1-\epsilon}\over bT}.                   \tag{3aw}
\]

Thus a quadratic marked reservoir loses no leading coefficient while the
radial demand descends to the fixed omitted-petal atom.  What cannot be done
for free is replace likelihood weight by raw history count.  If
`N_(j,e,r)` is the number of rank-`r` histories and `C_(e,s)` the number of
rank-`s` baseline endpoint faces, then exactly

\[
 {N_{j,e,r}\over C_{e,s}}
 ={q_{j,e,r}\over p_{e,s}}\,2^{r+2j-s}.                 \tag{3ax}
\]

Rank matching makes the tilt a literal Hall density; an `O(log n)` mismatch
can lose a fixed power.  The weighted fibre itself, however, has an exact
global collapse.  A rank-`k` source face `U` contributes at depth `j`

\[
 w_{U,j}={2^{-|T_j(U)|}\over4^jG_{e_j(U)}}
         ={2^{-k}\over G_{e_j(U)}}\le2^{2-k},\qquad
 \sum_jw_{U,j}\le1.                                    \tag{3az}
\]

Therefore any selected canonical-history subfamily has total genuine
weight at most `V(P)` (or `L V(P)` with an already explicit description
load `L`).  In particular every fixed `(W,A,p,F,tau)` weighted fibre is
already below the EIC-style `D_0^(1-epsilon)V` target; `W-A` need not be
reattached.  Globally,

\[
             S\le {V(P)\over4},\qquad
             V(P)\ge4M\,2^{D_{KL}/M}.                  \tag{3az1}
\]

This does **not** prove `S=Mn^{o(1)}` because `V(P)` may itself be
quadratic-exponential.  The sole surviving rank-transfer issue is the later
replacement of genuine likelihood weights by raw multiplicities.  Nor can
complementary downfaces secretly fix it: if `C=W-A`, distributing a rooted
collision fibre among the `2^{|C|}` complementary pairs reduces its square
energy by at most exactly `2^{|C|}`.  The common-target trace erasure is thus
real for raw counts and irrelevant for the weighted EIC fibre.  See
`agent_common_shield_mixing/RADIAL_KL_TO_HALL_BRIDGE.md` and
`agent_common_shield_mixing/WEIGHTED_HISTORY_DOMINATION_AND_COMPLEMENT_NO_GO.md`.

The algebraic part of that raw conversion is now settled as well.  Let
`N_(j,e,r)` count selected depth-`j` histories whose remaining parent has
rank `r` and endpoint pair `e`, and let `C_(e,r)` count all ordinary
rank-`r` endpoint faces in the same cell.  Comparing at the **parent** rank,
rather than at the original source rank, gives

\[
 {N_{j,e,r}\over C_{e,r}}
   =4^j{q_{j,e,r}\over p_{e,r}},\qquad
 4^jh_{j,e}=\sum_r{p_{e,r}\over p_e}
                   {N_{j,e,r}\over C_{e,r}}.           \tag{3az2}
\]

Thus some same-rank raw cell has density at least `4^j h_(j,e)`; the
apparently adverse rank mismatch in `(3ax)` was an artefact of comparing to
the wrong completion rank.  After the external data `(W,A,p,F,tau)` have
been fixed, cells below density `rho` satisfy the exact global bounds

\[
 \sum_{\rm low}N_{j,e,r}\le\rho J V(P),\qquad
 \sum_{\rm low}{q_{j,e,r}\over p_e}
       \le {4\rho\over3}V(P),                           \tag{3az3}
\]

where `J` is the number of active depths.  Every residual cell is therefore
a literal raw Hall atom over its actual endpoint-face bank.

This removes rank algebra but not quadratic entropy.  The denominator
`C_(e,r)` may still equal one.  A rational nested-cap/root-star family has

\[
 F_e=(3/2)^m,\quad
 G_e={1\over4}\left(1+{m\over2}+{{m\choose2}\over4}\right),
 \quad C_{e,2}=1,                                      \tag{3az4}
\]

while one fixed rank-three `W` is blocked and the same-rank density is
arbitrarily large.  Varying `W` can also reuse one endpoint bank
exponentially, with every attempted tagged union nonconvex.  Consequently a
fixed-power density changes `log V` by only `O(log n)` and gives no
unconditional improvement over the `1/4` coefficient.  A coefficient gain
requires the high-cell density itself to have quadratic exponent, an
independent parent/shield family of complementary quadratic exponent, or a
recoverable product of the two.  See
`agent_common_shield_mixing/RAW_RANK_MATCHED_ENDPOINT_DICHOTOMY.md`.

Small endpoint baselines themselves admit a sharp global charge.  In one
cell, a parent `T` with `d` selected peeled petals `Q` supplies every
ordinary face `Q union S`, `S subset T`; retaining the two endpoints costs
only a factor four.  With upstream history multiplicity `mu`, at most `J`
depths and `R` parent ranks, the decoded banks give

\[
 \sum_{j,e,r}2^{r-2}{N_{j,e,r}\over C_{e,r}}
       \le \mu J R V(P).                                \tag{3az5}
\]

In particular a maximum-density rank in `(3az2)`, of original source rank
`k=r+2j`, satisfies

\[
                  V(P)\ge {2^k h_{j,e}\over\mu}.        \tag{3az6}
\]

This completely pays singleton and polynomial parent banks, but the factor
`2^k` is only linear in `log n` and cannot by itself improve the quadratic
coefficient.  A recoverable full radial product does improve it: if it has
`q<=kappa L` clusters, history entropy `aL^2`, and each cluster has local
face coefficient `c_0`, the one-gap profile bank gives

\[
 \log V(P)\ge
  \left[a+c_0(a/\kappa)^2-o(1)\right]L^2.              \tag{3az7}
\]

At the conservative values `a=kappa=1/4`, `c_0=1/8`, this is `3/8-o(1)`.
The exact new target is therefore an extraction theorem: an arbitrary
quadratic-entropy same-parent completion family must expose a recoverable
positive-log-scale radial/module product, or an alternative circuit/anchor
bank.  The explicit product regression verifies the gain but does not prove
the extraction.  See
`agent_shield_circuit_cover/ENDPOINT_BASELINE_SCARCITY.md`.

Kruskal--Katona stability and unoriented four-locality do not provide that
extraction.  In the fixed-tangent radial transversal regression
`mathcal T=X_1*cdots*X_q`, `|X_i|=ell`, one has exactly

\[
 |\mathcal T|=\ell^q,\qquad
 |\partial_k\mathcal T|={q\choose k}\ell^k,\qquad
 |\Delta^*\mathcal T|=(\ell+1)^q-\ell^q.               \tag{3az8}
\]

Every carrier is convex, but the union of any two distinct transversals is
nonconvex.  Hence every common support whose source layer covers all
four-traces contains at most one transversal: a four-cover decomposition
needs `ell^q` tags.  Moreover the rank-`k` Boolean-shadow load is exactly
`ell^(q-k)`, so weighted replication and global shadow charging attain
equality rather than improve it.  At `q=kappa L`, `ell=n^delta`, the whole
proper shadow is only `n^(-delta+o(1))|mathcal T|` despite quadratic source
entropy.  The construction is still paid by its *oriented* one-gap profile.
Thus the live extraction theorem must retain the canonical first-divergence
block and its directional profile; neither small downshadow nor planar
four-locality detects the paying bank.  See
`agent_common_shield_mixing/KK_FOUR_LOCAL_STABILITY_REGRESSION.md`.

Even “extract a Cartesian module system inside the selected sources” is too
strong.  A fixed-parent radial cell can select a length-`2j`, dimension-`j`
Reed--Solomon code.  It has `N=q^j` convex sources and distance `j+1`, so
any Cartesian subfamily has at most one nontrivial varying coordinate block.
Nevertheless both its left and right projection alphabets have size `q^j`,
and every ambient cross-combination is convex.  More generally, whenever a
fixed two-tangent profile has complete left--right cross-completion,

\[
 V(P)\ge
 |\operatorname{proj}_{L}\mathcal E|\,
 |\operatorname{proj}_{R}\mathcal E|\,2^{|T|}.          \tag{3az9}
\]

The rooted-diagonal decoder sums this bank with rank-`k` load at most
`k-1`.  In the code regression `(3az9)` gives `N^2`, hence coefficient
`1/2` from a selected `1/4` family.  The exact surviving alternative is
therefore **ambient cross-completion versus coupling by the larger retained
parent**.  Internal module extraction and sparse-graph rectangle extraction
are both unnecessary and in general false.  See
`agent_outer_internal_product/SAME_PARENT_PROJECTION_PRODUCT_GATE.md`.

The larger parent itself now has an exact coefficient-free localization.
Each left or right petal block replaces one hull edge `g_L,g_R` of the
fixed convex parent `T`.  If the gaps are vertex-disjoint, every cross-pair
is convex.  If they are distinct and adjacent, only the turn at their common
parent vertex is new, so fixing the two petal tangent labels makes the
profile complete.  If they coincide at `g`, then exactly

\[
       T\cup L\cup R\text{ is convex}
       \quad\Longleftrightarrow\quad
       g\cup L\cup R\text{ is convex}.                 \tag{3az9a}
\]

There are only `r^2` gap pairs and the adjacent tangent localization costs
`O(L)` bits.  Hence all genuine parent coupling reduces with its source
mass intact to the one-edge same-side rooted child `(3az9a)`; it cannot be
spread through a large arbitrary core.

The sharp high-rate scaling shows that neither of those selected-family
alternatives alone is general.  For a length `q=(1/4+o(1))L`
Reed--Solomon selection over an alphabet of size `2^{L+o(L)}`, take
codimension `c=Theta(L/log L)`.  Then

\[
 \log|\mathcal E|=(1/4-o(1))L^2,\quad
 d_{\min}=c+1,\quad {q\over d_{\min}}=O(\log L),\quad
 \log{|\operatorname{proj}_L\mathcal E|
             |\operatorname{proj}_R\mathcal E|\over|\mathcal E|}
       =o(L^2).                                         \tag{3az10}
\]

Thus even tangent-fixed thinning yields neither linearly many modules nor a
quadratic rectangle surplus.  The *ambient* radial containers still give
`(3/8-o(1))L^2` faces by the one-gap theorem.  This pins the live statement
down further: extract ambient oriented containers (or a different
circuit/anchor bank) from the geometry, rather than infer them from the
selected incidence family.  See
`agent_shield_circuit_cover/MDS_MODULE_EXTRACTION_BARRIER.md`.

Once a common radial containerization is present, arbitrary sparsity is in
fact completely harmless.  For
`mathcal F subseteq product_i X_i`, let `s_i=log|X_i|`, let
`h_i=H(Z_i|Z_{<i})` under the uniform law on `mathcal F`, let `H_i` be the
nonempty local face count, and let `B_j` be the ambient bank omitting gap
`j`.  The cyclic profile identity and Shannon chain rule give exactly

\[
 \max_j B_j\ge|\mathcal F|2^\Gamma,\qquad
 \Gamma=\sum_i(s_i-h_i)+{1\over q}\sum_i(\log H_i-3s_i),
 \tag{3az11}
\]

and the universal local reservoir implies

\[
 \Gamma\ge { (\log|\mathcal F|)^2\over9q^2}
             -{3\log|\mathcal F|\over q}-O(1).          \tag{3az12}
\]

Thus coding and correlation only add the nonnegative support-redundancy
term `sum(s_i-h_i)`: every quadratic-entropy family in `O(L)` recoverable
radial containers has a quadratic-exponential one-gap multiplier.  All
subfamilies in the same cell are merged before one canonical maximizing gap
is selected, so the bank has load one; weights cost only the maximum
per-source multiplicity.  The remaining issue is no longer sparse-family
entropy but extraction and cross-base recovery of the ambient cyclic cell.
See `agent_common_shield_mixing/ORIENTED_RADIAL_ENTROPY_CHAIN.md`.

That same-cell consolidation does **not** sum automatically across varying
bases.  In an exact radial regression, split the ambient cyclic blocks into
context blocks `Y_1,...,Y_t` absorbed into the bases and petal blocks
`X_1,...,X_q`.  Every context has the same canonical petal gap bank, so its
cross-base overlap is

\[
             \Lambda_G=\prod_{a=1}^t|Y_a|,             \tag{3az13}
\]

which can have quadratic logarithm and exactly cancel `(3az12)`, even though
the source banks are disjoint and every gap output recovers its active petal
pattern.  Nontrivial source--gap unions are all nonconvex in the rational
audit.  Promoting the `Y_a` into the ambient radial cycle restores precisely
the factor `(3az13)`.  Therefore the final geometric target is a
**container-promotion theorem**: high cross-base reuse must either promote
the varying base history into additional recoverable oriented containers,
or yield a bounded-load circuit/outer splice bank.  Output-only
canonicalization is false.  See
`agent_common_shield_mixing/CROSS_BASE_ONE_GAP_REUSE_REGRESSION.md`.

A tempting ordered-hypergraph implementation of that promotion has two
separate exact obstructions.  Even strict interval separation in increasing
left-tangent and decreasing right-tangent coordinates controls only pairs,
whereas convexity of a rooted chain is a three-point turn condition.  There
are two convex rooted triples, lying coordinatewise in the same three
strict reverse-dominance cells, for which a mixed transversal is nonconvex.
Consequently neither ambient transversals nor the broad directional one-gap
bank follow from double interval partitioning.  There is also a sharp scale
loss.  For an `r`-graph with `M=n^alpha` edges the ordered-partition theorem
has extraction constant

\[
 c={(k-1)!(1-2^{k-1-\alpha})
       \over\sum_{j=k}^r{2k-2\choose j}},
 \qquad
 e(H_2)\ge c^2r^{-\alpha}M(m_2/n)^\alpha.              \tag{3az13a}
\]

When `r,alpha,k=Theta(L)`, the displayed prefactor costs only
`2^{O(Llog L)}`, but retaining the quadratic mass forces
`m_2>=n/poly(L)`, which the theorem does not guarantee.  Pigeonholing all
components gives only `2^{Theta(Llog L)}` absolute edges.  A weighted sum
over components is free when every output meets every selected dyadic part,
but an exact finest-scale family without that cover has
`n^{Theta(k)}` components all reusing one face.  Thus neither selection nor
summation repairs the scale problem.  See
`agent_common_shield_mixing/ORDERED_HYPERGRAPH_PROMOTION_AUDIT.md`.

What *does* survive for any
cross-complete trace alphabets `mathcal A_i` is the separated ordered-face
pair bank

\[
 |\mathcal B_g|=H_g\prod_{i\ne g}|\mathcal A_i|,
 \qquad
 \max_g|\mathcal B_g|\ge P_0
       \left(\prod_i{H_i\over|\mathcal A_i|}\right)^{1/k}.
                                                               \tag{3az14}
\]

Its representation is injective, but it lives in `mathcal F(P)^2`.
Therefore the exact standalone conclusion is only

\[
 \log{V(P)\over M}\ge {1\over2}\left[
   \log{P_0\over M}+{1\over k}\sum_i\log{H_i\over|\mathcal A_i|}
                         -\log M\right].                \tag{3az15}
\]

The final negative term is essential: the audited bank has
`M=126`, `B_*=504<M^2`.  Thus a fixed-power surplus over `M` in the pair
bank gives no one-face or coefficient gain.  An exact positive-coordinate
`1+3` circuit also shows that inserting an arbitrary local reservoir, or
even the corresponding broad endpoint profile, into one other-cell face is
false.  See
`agent_outer_internal_product/DOMINANCE_CELL_SEPARATED_ONE_GAP.md`.

In contrast, the retained **fixed parent** contributes no quadratic
coupling.  Two ears on disjoint parent edges commute; ears on adjacent
edges require only the turn at their common parent vertex; and two endpoint
ears using the same empty parent side are compatible exactly when two seam
turns have the parent sign.  Those turns depend on at most four actual ear
labels.  Hence every fixed-parent left--right family partitions into

\[
        O\!\left(|T|^2(1+n^2+n^4)\right)                \tag{3az16}
\]

complete cross-rectangles, and all active rectangles sum with local load
one.  This costs only `O(log n)` bits at bounded rank.  The remaining
container-promotion problem is therefore not hidden in a large parent: it
is a cyclic finite-state problem in the adjacent seam turns.  A positive
proof must multiply the detached local reservoirs through those Ferrers
seams, or charge a heavy seam to an explicit circuit/shield bank.  See
`agent_shield_circuit_cover/PARENT_SEAM_JET_COMPLETION.md`.

That cyclic finite-state problem has an exact first transfer.  In a fixed
oriented parent cell, let `mathcal E` be `M` valid full ear words, let `m_g`
be its projection size at edge `g`, and let `H_g` count local profiles which
are themselves admissible ears at that edge.  Put
`K=max_g H_g/m_g`.  Deleting a maximizing coordinate gives at least
`M/m_g` distinct partial words.  Hence either at least half of the formal
substitutions pass both adjacent seams and form an injective one-face bank,
or one Ferrers seam contains a complete incompatible rectangle.  A dyadic
prefix decomposition loses only a logarithm:

\[
 \boxed{\quad |\mathcal C|\ge {KM\over2}\quad}
 \qquad\hbox{or}\qquad
 \boxed{\quad \text{bad contextual mass}\ge
        {KM\over4(1+\lfloor\log M\rfloor)}.\quad}       \tag{3az17}
\]

Every bad pair has one common parent vertex and an actual four-circuit.
Thus a quadratic admissible-profile surplus cannot diffuse through the
cycle: it pays immediately or reaches one heavy rooted seam with the same
quadratic coefficient.  The second branch is not yet a face bank.  Deleting
the shared parent vertex releases singleton ears, but is false for longer
ears; an exact six-point example still hides the penultimate left-ear
vertex.  Iteration exposes the next four-label jet and can have linear
depth.  See `agent_shield_circuit_cover/CYCLIC_FERRERS_ONE_GAP.md`.

Nor can `H_g` in `(3az17)` be replaced by the total detached reservoir.
For anchored profile multiplicities `a_i(x),r_i(x)` on a valid cyclic word
family `Omega`, the exact positive quantity is the **on-word** mass

\[
 \max_i B_i\ge |\Omega|\,
 \mathbb E_\Omega\!\left[
   \left(\prod_i a_i(X_i)r_i(X_i)\right)^{1/q}\right]
 \ge |\Omega|\,2^{q^{-1}\sum_i\mathbb E\log(a_ir_i)}.  \tag{3az18}
\]

An alternating Ferrers cycle
`x_1<=x_2>=x_3<=cdots>=x_1` has
`2^{Theta(L^2)}` valid words and can place arbitrarily rich formal profiles
on the wrong halves of every threshold, making every enhanced seam bank
zero.  This is an abstract, not yet planar, regression, but it proves that
local reservoir totals and Ferrers monotonicity alone cannot finish the
argument.  The precise remaining invariant is root-admissible/on-word
profile mass, or a summable charge for the long rooted reset created when
that mass vanishes.  See
`agent_common_shield_mixing/CYCLIC_FERRERS_PROFILE_TRANSFER.md`.

The alternating regression is genuinely planar, but it still fails as a
sub-half construction.  Positive tangent coordinates can realize adjacent
compatibility exactly as `R_iL_(i+1)>1`, and alternating rescalings give the
threshold cycle above; arbitrary projective children may replace the
anchors.  Nevertheless, deleting any one cell joins two equal-parity rich
halves.  Under the natural lexicographic child exposure, for alphabet size
`A`, even cycle length `q`, child size `s`, and child face count `H`, the
released bank is load one and

\[
 V(W)\ge\max\left\{(As/2)^q,
        (A/4)^{q-1}s^{q-3}H\right\}.                  \tag{3az18a}
\]

With `q=log A=d`, `log s=beta d`, and child coefficient `c`, this gives

\[
 c_W\ge\max\left\{{1\over1+\beta},
 {1+\beta+c\beta^2\over(1+\beta)^2}\right\}.          \tag{3az18b}
\]

Any recursive fixed point therefore satisfies
`c>=(1+beta)/(1+2beta)>1/2`; the infimum over `beta` is exactly `1/2`.
Thus planar anti-alignment can erase every rich original seam, but the
one-gap exposure restores the half barrier.  The theorem uses genuine
lexicographic exposure; arbitrary nonseparated ears still have the
five-point one-gap obstruction.  See
`agent_shield_circuit_cover/ALTERNATING_FERRERS_PLANAR_WRAPPER.md`.

Standard semialgebraic regularity does not supply that invariant.  There is
nevertheless a useful sharp split.  Applying the fixed-arity
Fox--Pach--Suk density theorem separately to every consecutive orientation
triple gives ambient supports `Y_i` with

\[
 |Y_i|\ge c_0^3|X_i|,
 \qquad c_0={1\over8\,3^{120}},                         \tag{3az19}
\]

on which every consecutive sign is homogeneous; since each coordinate is
touched at most three times, the whole ambient product loses only `O(r)`
bits.  But retention of a selected family is maximally false.  With
`r=3d`, `N=2^d`, take three interleaved parabola colour classes in each of
`d` blocks and select only words using the same index in the three colours.
There are `M=N^d=2^{d^2}` positive convex words, while any product cell
homogeneous on all consecutive triples contains at most one of them.  Thus
`M` cells are necessary.  Here `P_0=M^3`, so the obstruction has projection
redundancy `R=log(P_0/M)=2log M` and is paid by the ambient convex parabola.
The exact growing-arity application only gives

\[
 \log B\ge\log M-(3r-1)R-40r^2\log3-2r\log(r-2),       \tag{3az20}
\]

which loses `Theta(r^2)` even at `R=0`.  Hence the surviving regularity
target had to charge redundancy.  This target is now proved, with the
stronger loss `O(r+R)`.  If
`E subseteq X_1 times ... times X_r` has one prescribed strict sign on
every consecutive triple, `M=|E|`, and
`R=log(prod_i|pi_iE|/M)`, then there are `Y_i subseteq pi_iE` such that all
ambient transversals have those signs and

\[
 |E\cap(Y_1\times\cdots\times Y_r)|
              \ge M2^{-A(r+R)}                         \tag{3az21}
\]

for one absolute constant `A`.  The proof recursively applies a
constant-error fixed-arity semialgebraic partition only inside its
nonhomogeneous product cells.  For a positive orientation-triple law of
total correlation `T`, the terminal rectangle transcript has entropy
`O(1+T)`: a node retaining at most half its mass terminates geometrically,
while a node retaining more than half in an exceptional region of product
mass at most `1/4` spends at least
`(1/2)log(4/3)` bits of KL.  The rectangle-child KL chain rule telescopes.
Finally the consecutive triple correlations satisfy

\[
 \sum_{j=1}^{r-2}TC(X_j,X_{j+1},X_{j+2})
       \le2TC(X_1,\ldots,X_r)\le2R.                    \tag{3az22}
\]

Thus selected-family retention is no longer the obstacle in the
low-redundancy regime.  A bounded cover is still false: already for `r=3`
a constant-redundancy parabola family needs `Omega(N)` homogeneous boxes.
The remaining use must either turn the retained ambient container into new
ordinary faces or charge quadratic `R` to a separate face bank.  See
`agent_common_shield_mixing/SEMIALGEBRAIC_CONSECUTIVE_TRIPLE_AUDIT.md` and
`agent_common_shield_mixing/REDUNDANCY_CHARGED_SEMIALGEBRAIC_RETENTION.md`;
an independent proof/audit, including the conditional-product KL
correction, is in
`agent_shield_circuit_cover/ENTROPY_SEMIALGEBRAIC_TRANSCRIPT.md`.

There is also a geometry-free support bank for the complementary
high-redundancy regime.  If the `M` selected ordinary rank-`r` words use
disjoint coordinate supports `X_i`, put
`N=|union_iX_i|`, `P_0=prod_i|X_i|`, and `R=log(P_0/M)`.  Since the induced
configuration on the union of the supports already has at least `f(N)`
faces,

\[
 {V(P)\over M}\ge
 \max\left\{1,{f(N)2^R\over P_0}\right\},\qquad
 \log{V(P)\over M}\ge
 \left[R+\log f(N)-r\log{N\over r}\right]_+.          \tag{3az22a}
\]

At the critical rank `r=(1/4+o(1))log N`, the known `1/4` theorem cancels
the entire rank tax, so `R>=rho r^2` yields

\[
                         V(P)\ge M2^{(1-o(1))R}.        \tag{3az22b}
\]

At arbitrary rank the same hypothesis still gives the absolute bound
`log V(P)>=(rho^2/4-o(1))r^2`; for
`r=kappa log N` the exact relative threshold is
`R>(kappa-1/4)(log N)^2`.  Thus support statistics fully settle quadratic
redundancy at the critical rank, but not the above-critical low-gain
regime.  See `agent_shield_circuit_cover/HIGH_REDUNDANCY_SUPPORT_BANK.md`.

The application to the live same-parent radial cell is now exact.  Write
`L_i=|X_i|`, `P_0=prod_iL_i`, `M=|E|`, and
`R=log(P_0/M)`, with `q<=kappa log D` cells and `L_i<=D`.  The existing
ambient one-gap identity gives

\[
 \log {\max_j B_j\over M}
 \ge R+{1\over q}\sum_i(\log H_i-3\log L_i)
 \ge R-2\log D.                                      \tag{3az23}
\]

Thus quadratic support redundancy is already a one-face gain.  If instead
`R=o(q^2)`, `(3az21)` retains

\[
                  M'\ge M2^{-O(q+R)}=M2^{-o(q^2)}     \tag{3az24}
\]

selected carriers in a product homogeneous for every consecutive turn and
the fixed endpoint signs.  All singleton transversals in that product are
ordinary, and the parent seam-jet localization removes their residual
coupling with only `O(log D)` bits.  Consequently neither selected-word
correlation, high-rate coding, nor failure of product-module extraction is
still an obstruction.

The remaining implication is strictly stronger and is false without new
geometry.  A one-gap output substitutes a multi-point local face, whose
actual first/last tangent jet can differ from the selected singleton jet.
There is an exact rational complete-product example with `R=0` in which
both singleton transversals are convex but the formal one-gap face has a
`1+3` circuit.  Conditional on compatible mask-aware reservoirs satisfying

\[
 {1\over q}\sum_i\log H_i^\star
       \ge {c_0-o(1)\over q}\sum_i(\log|Y_i|)^2,
\]

the cyclic one-gap bank would give

\[
 {\log V(P)\over(\log D)^2}
       \ge a+c_0(a/\kappa)^2-o(1),                    \tag{3az25}
\]

and hence `3/8-o(1)` from `a=kappa=1/4`, `c_0=1/8`.
The precise finite-state target is therefore a
**compatible-jet-reservoir-or-circuit/shield lemma**.  See
`agent_common_shield_mixing/SAME_PARENT_RETENTION_PROFILE_SPLICE.md`.

That target is now solved for genuine fixed-convex-base ear cycles.  First
partition each local reservoir by its actual first-two/last-two boundary
jet; at most `(L+1)^4` classes occur, so one class keeps the full quadratic
coefficient.  For a valid selected ear word, insert a face from a rich
root-admissible jet class at edge `g`, and omit precisely those of its two
neighboring selected ears whose new seam turn is bad.  Restoring those
fixed base edges creates no further adjacency.  The output is one ordinary
face and forgets at most the two omitted ear values, whence exactly

\[
             V(P)\ge {J_gM\over m_gm_{g-1}m_{g+1}}.   \tag{3az26}
\]

Consequently the conditional bound `(3az25)`, including `3/8-o(1)`, is
unconditional in the fixed-base ear model; Ferrers anti-alignment is
irrelevant there.  The remaining geometry is **nonseparated occupied-mask
geometry**.  Without permanent base edges, omitting a bad neighbor changes
the next predecessor/successor and can expose another bad seam.  The exact
`R=0` rational `1+3` example already has a fixed replacement jet and
survives the prescribed omission.  Thus the next target is a mask-aware
deletion cascade with subquadratic erased-alphabet load, or a charge of its
first newly exposed bad seam.  See
`agent_common_shield_mixing/MASK_AWARE_JET_ADAPTIVE_OMISSION.md`.

The apparent lack of permanent base edges can itself be removed for every
root-good cell.  Fix a parity class of occupied singleton positions
containing the target cell; the complementary positions form a convex
word-dependent base which is retained in the output, while the chosen
parity positions are nonadjacent ears of that base.  Adaptive omission now
forgets the target value and at most its two neighboring parity-ear values,
so for the root-compatible incidence mass `C_g`,

\[
                         V(P)\ge {C_g\over D^3}.       \tag{3az26a}
\]

The base may vary freely because its coordinate values are decoded from
the output.  Hence `(3az25)` and the `3/8` jump hold for arbitrary
nonseparated masks once a quadratic root-good jet class exists.  The exact
half-erasure cascade and the seven-point fixed-jet obstruction both lie in
the complementary homogeneous **root-bad** `1+3` cell.  See
`agent_common_shield_mixing/NONSEPARATED_MASK_PARITY_PROMOTION.md`.

Even without a geometric cascade bound, its erased entropy is now
quantified exactly.  Let `mathcal J` be a local profile family at cell `g`.
For every selected singleton word and `F in mathcal J`, choose any
deterministic deletion mask `D` for which `F` together with the retained
coordinates is ordinary; the empty retained mask always works.  Grouping
by the at most `2^{q-1}` masks gives, for every `T>=1`, the dichotomy

\[
 \#\{(x,F):\prod_{i\in D(x,F)}m_i>T\}>{MJ\over2}
 \quad\hbox{or}\quad
 V(P)\ge {MJ\over2^q m_gT}.                            \tag{3az27}
\]

Indeed the output recovers the mask, `F`, and all retained coordinates;
only `x_g` and the deleted coordinate values are forgotten.  With
`log M=(1/4+o(1))L^2`, `log J=(1/8+o(1))L^2`, the absence of a fixed gain
forces more than half the pairs to erase at least
`(1/8-o(1))L^2` support bits--half of the selected source entropy.  Hence
only a genuinely macroscopic mask cascade survives.  See
`agent_root_followup/MASK_CASCADE_ENTROPY_DICHOTOMY.md`.

The root-admissibility issue inside one local reservoir has also been
localized completely.  A random `t`-role colouring retains `H/t^t` of any
rank-`t=O(log N)` face family on disjoint coordinate supports.  More
generally, for `m` fixed local orientation predicates in which every role
has nonfirst-coordinate degree at most `Delta`, the entropy transcript
retains

\[
             M2^{-O(m+\Delta R)}                       \tag{3az28}
\]

words in a product homogeneous for all predicates.  Thus, after the actual
four-label boundary jet is fixed, either a quadratic root-good class exists,
high support redundancy is paid by `(3az22a)`, or essentially all the local
quadratic mass lies in a homogeneous product of ordinary faces carrying one
fixed root-bad four-circuit.

The last alternative is sharp.  Shrink arbitrary projective children into
the roles of a convex macro polygon surrounding one fixed root; every
transversal is ordinary, the support redundancy is zero, the boundary jet
is fixed, and the same `1+3` circuit makes every word root-bad.  Deleting
the root gives the detached face with load equal to the external context
multiplicity; the canonical load-one code remains two-faced.  Consequently
the live macroscopic-cascade branch is now specifically a one-face
guard-release/Hall summability problem, not a failure of role extraction or
regularity.  See
`agent_shield_circuit_cover/ROLE_COLORED_PROFILE_DICHOTOMY.md`.

Macroscopic guard depth is genuinely possible in that final class.  Put a
root at the centre of `t=2m+1` cyclic role clusters, each of size `A`.
Every full transversal is convex and contains the same rooted `1+3`
circuit, while root plus a partial transversal is convex exactly when its
active roles lie in one `(m+1)`-consecutive semicircle block.  Hence the
minimum deletion depth is exactly `m`, killing the named circuit merely
exposes another, and

\[
 |\mathcal B_{det}|=(A+1)^t,\qquad
 tA^{m+1}\le|\mathcal B_{root}|
                   \le t(A+1)^{m+1}.                  \tag{3az29}
\]

For `K` actual root contexts, every decoder restricted to detached or
one-root partial transversals has load at least

\[
 {1\over2}\min\left\{
 K(A/(A+1))^t,
 {A^t\over t(A+1)^{m+1}}\right\},                    \tag{3az30}
\]

matching the forget-context and retain-a-semicircle operations at leading
exponent.  Arbitrary projective children preserve this barrier.  It still
does not give a sub-half construction: the detached full transversals form
a load-one bank of coefficient `alpha` when `t=(alpha+o(1))log A`; only
their multiplication by quadratic multi-point external contexts is
unresolved.  See
`agent_shield_circuit_cover/CENTRAL_ROOT_DEPTH_GUARD_BARRIER.md`.

The tempting endpoint-profile payment for the central shell is **not
automatic**.  If compatible rooted families of sizes `A_i,R_i` have
already been proved, then the exact conditional identity

\[
 B_j=R_{j-1}A_{j+1}\prod_{i\notin\{j-1,j,j+1\}}L_i,
 \qquad
 \prod_j{B_j\over P_0}=
       \prod_i{A_iR_i\over L_i^3}                       \tag{3az30a}
\]

is valid and gives the advertised coefficient-half calculation when
`A_iR_i>=H_i`.  But the implication `A_iR_i>=H_i` is false for arbitrary
small projective children, even when every singleton transversal has one
fixed cyclic type and the blocks are strongly separated.  In an exact
four-role rational family, one convex `m`-point child has `H_i=2^m-1`,
while a retained nonadjacent singleton hides the middle point of every
child triple after either adjacent omission.  Both endpoint families then
have rank at most two and

\[
             A_iR_i\le\left(m+{m\choose2}\right)^2
                       <2^m-1\qquad(m\ge14).             \tag{3az30b}
\]

Thus `(3az30a)` is only a conditional rooted-profile theorem; scale
separation, zero redundancy, and same-type/strong separation do not supply
its premise.  The counterexample is itself paid by the child's Boolean
bank, so it is not a sub-half construction.  It instead identifies the
live replacement: either the same-block bad circuits have a small set of
external blocker roles whose deletion releases the local face family, or
their blocker traces must force a new crossing/two-ended/outer-shield bank.
See `agent_common_shield_mixing/STRONG_SEPARATION_PROFILE_CLOSURE.md` and
`agent_shield_circuit_cover/STRONG_SEPARATION_ENDPOINT_PROFILE_COUNTEREXAMPLE.md`.

The replacement blocker statement is exact.  For one local face `F` in a
complete same-type product, put a loop on external role `r` for every bad
`3+1` circuit using three points of `F`, and put an edge `rs` for every bad
`2+2` circuit using two points of `F`.  A role set `J` can be deleted so
that `F` coexists with **every** transversal of the remaining roles if and
only if `J` is a vertex cover of this looped graph.  This is just planar
four-locality: a surviving nonconvex union contains a surviving bad
four-set, and same-type convexity excludes a split with fewer than two
points of `F`.

There is no need to pigeonhole a common cover over the local reservoir.
Let `L_r` be the external alphabet sizes,
`P_ext=prod_r L_r`, and choose a canonical minimum-weight cover `J(F)` with

\[
                         w(F)=\sum_{r\in J(F)}\log L_r.
\]

Outputs released using different covers have different occupied-role
masks, while an output with a fixed mask recovers `F` and every retained
label.  Consequently all covers sum with load one and

\[
 |\mathcal B|=P_{ext}\sum_{F\in\mathcal H}2^{-w(F)}
       \ge P_{ext}|\mathcal H|,2^{-\mathbb E_Fw(F)}.   \tag{3az30c}
\]

Thus outer coefficient `a`, local coefficient `c`, and mean deleted
entropy `theta L^2` give coefficient `a+c-theta`.  Failure of this branch
is precisely positive quadratic **average blocker entropy**.  Weighted
vertex-cover duality then forces either comparable mandatory-loop entropy
or a comparable fractional matching of disjoint `2+2` traces.  See
`agent_outer_internal_product/BLOCKER_ROLE_COVER_RELEASE_DICHOTOMY.md`.

The loop alternative is indispensable.  There are exact rational strongly
separated caps with `m` local points and `k` singleton blocker roles in
which every blocker is a mandatory `3+1` loop, the deletion depth is `k`,
and the complete face count is

\[
 V=2^m+\left(1+m+{m\choose2}\right)(2^k-1).             \tag{3az30d}
\]

Hence large cover number need not create even one crossing `2+2` witness,
and the detached local and blocker Boolean reservoirs need not multiply.
This example is not a sub-half construction: its cap bank is exponentially
large in the actual local rank.  See
`agent_shield_circuit_cover/BLOCKER_ROLE_HITTING_SET_BARRIER.md`.

The corresponding construction-shaped reduction is now also exact.  Put
arbitrary projective children `Q_i` behind one common guard edge, with the
children in a convex macro chain.  Guard-retaining faces use at most one
label from each child, while after the guards are removed the full count is
the heterogeneous first-cap/last-cup recurrence

\[
 W(P)=\sum_iW_i+
   \sum_{i<j}C_iU_j\prod_{i<k<j}(1+n_k).                \tag{3az30e}
\]

An exact scalar cap/cup ramp keeps `(3az30e)` at coefficient `1/4`.
Wrapper-local minimizer conditions do not remove it: reflection and
adjacent-swap inequalities sort cup-heavy children to the left and
cap-heavy children to the right.  Exhausting all rooted four-point profile
words gives an exact rational three-child minimum with `V=1561`, and every
one-child replacement, reflection, and permutation is nonimproving.  Thus
first-order minimizer mutations favor the ramp rather than balance it.

Nor may one simply invoke the strong-tree theorem after arbitrary recursive
recharting.  A projective chamber can destroy the child's compatible
ordered decomposition; exact Pascal cells have only two compatible
chambers among 26--198.  The correct conditional reset is coefficient
neutral.  If the actual outer-chart atom states satisfy
`log X_i+log Y_i>=F`, then a `q`-atom strong chain obeys

\[
 \log V\ge
 \min\left\{F-\log N,
 {q\over q+1}F-{2\log N\over q+1}\right\}.             \tag{3az30f}
\]

Compatible strong-tree atoms supply the half-coefficient value of `F`, but
the universal arbitrary-chart input currently supplies only the known
quarter scale.  Applying the strong-tree endpoint lemma to arbitrary atoms
would be a domain error.

Accordingly the recursive state is genuinely two-directional.  For a child
`Q`, write

\[
 \Pi_2(Q)=\{(C_\xi,U_\xi;C_\eta,U_\eta):\xi\ne\eta
             \text{ generic projection chambers}\}.       \tag{3az30f1}
\]

The first chamber is used to assemble the present wrapper and, after an
affine re-embedding, the second can be used at the next reset.  Exact comb
formulae show that every rational generic second chamber can indeed be
re-nested behind a fresh common guard.  Thus a scalar one-chart ramp is not
yet a recursive construction, but neither can arbitrary reset itineraries
be discarded: they escape the inherited ordered strong tree.  The live
construction/proof gate is to control `\Pi_2` under repeated wrappers (or
to extract a mixed-seam bank), not merely to balance one visible pair
`(C_\xi,U_\xi)`.

There is an important limit to that state requirement.  A branching
`q`-role recursion uses `q` independently embedded child copies.  Each
physical copy carries only two marked directions--the present assembly and
one future reset--and `PGL_2` is transitive on ordered distinct pairs.
Therefore the `q` reset profiles may be selected independently from the
child's realizable menu; no same-generation `Pi_q` or four-direction
cross-ratio constraint is forced.  What `Pi_2` still omits is the decorated
embedding gauge and the cross-child pair-direction arrangement, because the
reset profile of the completed parent is not determined by a scalar
recurrence in the child reset counts.  Nor is `Pi_2` automatically a closed
scalar recurrence: if a node exports two charts neither of which is its
construction chart, its children are queried in three charts and
unforgotten marks can accumulate pathwise.  But this is not compulsory.  A
branching construction may build each type in the first chart it exports
and retain only one second chart; then every edge transports one ordered
pair, while historical construction charts are existentially forgotten
because `W` is chart-invariant.  Hence neither a same-generation `Pi_q` nor
a pathwise `Pi_h` condition may be imposed without an explicit state
convention.  The exact finite audit instead builds the decorated parent
coordinates and re-enumerates its reset spectrum.

The local decorated transition is now classified exactly.  Suppose reset
order keeps assembly blocks as intervals.  If a size-`n_i` child reset
permutation has `I_i` inversions relative to assembly, put

\[
 k_i=\min\{I_i,{n_i\choose2}-I_i\}.                       \tag{3az30f2}
\]

For every external point the two repeated-block cross signs occur exactly
`I_i` and `binom(n_i,2)-I_i` times.  Hence the total minority mixed-seam
mass is exactly

\[
              \sum_i(N-n_i)k_i,                            \tag{3az30f3}
\]

while deleting at most `sum_i k_i` child labels makes every reset order
assembly-monotone or reversed.  If reset blocks interleave, that is already
the interval-mixing branch.  Thus every one-step decorated reset gives a
released separated skeleton or an equally quantified supply of mixed
seams.  A 44-point exact bi-chart realization has inversion counts
`(1,9,1)`, exactly 330 minority triples, and actual reset profile
`(14537,106989)`, disproving the formal scalar reverse-comb recurrence.
The theorem is local: released sets and mixed seams still need the marked
context/Hall charge below.  See
`agent_shield_circuit_cover/DECORATED_TWO_MARK_INVERSION_DICHOTOMY.md`.

The marked splice to that charge is exact.  Weight a minority-seam record as
`(c,e,F,z)` whenever its repeated seam label `z` lies in the actual pocket
face `F`.  In the high endpoint-codegree branch below, the attached output
retains `F`; in the low branch the two canonical endpoint circuits both meet
`F`.  Forgetting the mark `z` costs at most `|F|`, in both the output and
circuit decoders, so it is coefficient-free on the bounded-rank slice.  This
condition cannot be omitted: a rational rank-three seam has both endpoints
compatible with the pocket (`g=2`), and seam mass with `z` outside `F` has no
context decoder without a separate load `Delta_out`.  In the clean
strong-comb application the situation is sharper: a minority pair has the
minority sign against every point outside its repeated block.  Whenever
`F` meets another block, choosing the first point of `F` outside the repeated
block deterministically supplies the full matching-by-pocket rectangle with
zero additional decoder load.  The only support residue is therefore `F`
contained wholly in that repeated block, which descends to the child's own
circuit/profile structure.  The more general Hall ledger is needed only
when this uniform external sign law is unavailable.  See
`agent_shield_circuit_cover/INVERSION_ENDPOINT_POCKET_SPLICE.md`.

The genuinely separated branching branch is already closed.  For `q`
cyclic lexicographic child clusters of size `A`, with local face reservoirs
`H_i` and two boundary profile counts satisfying `L_iR_i>=H_i`, the exact
one-gap bank gives

\[
       V(P)\ge A^{q-3}\left(\prod_{i=1}^qH_i\right)^{1/q}. \tag{3az30f4}
\]

At the live values `q=(1/4+o(1))log A` and
`log H_i>=(1/4-o(1))(log A)^2`, this is coefficient `1/2`.  Sibling copies
may synchronize an arbitrary assembly/reset pair while preserving the
linear strong seams, so profile-query entropy supplies no extra saving.
Abstractly, the query ledger grows by one only when a construction chart is
not already exported, and a recycled construction-plus-reset grammar can
stay decorated `Pi_2` at arbitrary depth.  The exact low-face ramp cannot
use that escape twice.  If each rich child has
`Z_i>=D^{q-delta q}` while the completed parent has
`Z(P)<=D^{q+delta q}`, its construction chart satisfies

\[
 \log_D\widehat C(P)\ge q-2\delta q-O(1),\qquad
 \log_D\widehat U(P)\ge q-4\delta q-O(1).                 \tag{3az30f5}
\]

Two roles recycling this chart in the next first/last recurrence therefore
give the one-face forward bank

\[
                    W_{\rm next}\ge D^{2q-6\delta q-O(1)}, \tag{3az30f6}
\]

which is coefficient `1/2-o(1)`.  Thus a quarter-budget parent may recycle
its construction chart in at most one role; the other `q-1` edges genuinely
reset.  In a balanced tree a polylogarithmic fraction of leaves is all-fresh,
but its depth is only `Theta(log n/loglog n)` and the coherent itinerary cost
along a path remains `O((log n)^2/loglog n)`, so this restores mandatory
multi-chart novelty without closing it.  Hence the sole construction-side
survivor is a systematically **nonseparated**, decorated multi-chart/gauge
recursion, not a stationary `Pi_q` phenomenon.  See
`agent_outer_internal_product/BRANCHING_PROFILE_QUERY_DEPTH_GATE.md` and
`agent_outer_internal_product/CONSTRUCTION_CHART_RECYCLING_OBSTRUCTION.md`.

Finite-gap induction still cannot treat the reset children as scalar face
banks.  Even granting an exact guarded linear strong comb with `q` equal
`D`-point children and child scale `R^h`, `R=D+1`, the max-plus optimization
of the full first/last recurrence is

\[
 \min_{1\le x_i\le h-1}\max\{hbox{all recurrence exponents}\}
                         =\max\{h,q\}.                 \tag{3az30f7}
\]

For the weak singleton baseline, `q<=h` is attained by
`x=(1,1,2,...,q-1)`; for `q>h` an initial plateau followed by the same
ramp does.  The genuine planar baseline also counts every pair, so
`C_i,U_i>=D+binom(D,2)`.  In the live slack range `q<=h-2`, the shifted
profile `x=(2,2,3,...,q)` still has envelope exactly `h` while satisfying
this pair baseline and `C_iU_i=W_i=R^h`.  Thus with `D=2^d`,
`q~d/4`, `h~d/2`, the recurrence can remain at the child half scale while
the parent target requires the additional factor

\[
                         2^{(1-o(1))d\log q}.           \tag{3az30f8}
\]

There is a sharp positive remnant: if only `K` integral profile levels
occur, one forward bank gains `R^{ceil(q/K)-2}`.  Hence any
`o(q/log q)`-width menu pays `(3az30f8)`; the scalar survivor requires a
genuinely growing near-unit-slope marked two-chart menu.  This is a
recurrence barrier, not a planar construction--realizing the menu
recursively without importing the unknown low-face primitives remains the
geometric task.  See
`agent_outer_internal_product/FINITE_GAP_STRONG_COMB_RAMP_BARRIER.md`.

Inside a genuine linear strong-glue chart there is a sharper, exact
potential.  Put `D=2^d`, let `C_i,U_i,H_i` be the cap, cup, and nonempty
face counts of role `i`, assume `log H_i>=Phi(d)`, and define

\[
 A_i=\log_D C_i,\qquad y_i=A_i-i,\qquad \ell=\log q.       \tag{3az30f9}
\]

The injective upper/lower-hull encoding gives `H_i<=C_iU_i`, while the
actual first-cap/last-cup bank for `i<j` has
`C_iU_j(1+D)^{j-i-1}` ordinary faces and decoder load one.  Consequently
one pair satisfying

\[
 y_i-y_j\ge
  1+{\Phi(d+\ell)-\Phi(d)\over d}                       \tag{3az30f10}
\]

already supplies `2^{Phi(log(qD))}` faces.  For
`Phi(L)=cL^2-O(L log L)`, the threshold in `(3az30f10)` is only
`(2c+o(1))log q+1=O(loglog n)`.  Thus any downward fluctuation of that
size recovers the *entire* finite-gap deficit.  The exact unpaid scalar
state is much narrower than arbitrary anti-alignment:

\[
       y_j>y_i-\bigl((2c+o(1))\log q+1\bigr)
       \quad\hbox{for every }i<j.                       \tag{3az30f11}
\]

It is an `O(loglog n)`-coherent slope-one cap/cup ramp across
`Theta(log n)` physical children.  The condition is sharp at the scalar
level.  For `c=1/2`, `q=d/4`, and `8|d`, the integer menu

\[
 C_i=D^{d/8+i},\qquad U_i=D^{3d/8-i},\qquad
 H_i=C_iU_i=D^{d/2}                                    \tag{3az30f12}
\]

has constant `y_i=d/8`, satisfies all child and hull-product constraints,
and its complete linear recurrence lies between `qH` and `2qH`; the half
target at `qD` is larger by
`2^{d log q+(log q)^2/2-log q-1}=n^{(1-o(1))loglog n}`.
No planar realization of this menu is known.  Hence the fixed-gap problem
has been reduced to excluding an actual planar coherent ramp or finding
child/cross-role surplus invisible to the scalar recurrence.  See
`agent_shield_circuit_cover/FIXED_GAP_LINEAR_PROFILE_POTENTIAL.md`.

The apparent surplus escape inside that ramp is now localized exactly.
Write

\[
 h_i=\log_DH_i,\qquad
 s_i=\log_D{C_iU_i\over H_i},\qquad
 T=P-h+1,                                             \tag{3az30f13}
\]

where `D^h` is the child target and `D^P` the parent target.  The actual
`i<j` first/last bank has exponent

\[
             h_j+s_j+y_i-y_j-1.                       \tag{3az30f14}
\]

Thus an unpaid family obeys `s_j+y_i-y_j<T` for every `i<j`.  Taking
prefix maxima of `y_i` gives the exact telescope

\[
              \sum_{j=1}^{q-1}(s_j-T)_+<P-1.          \tag{3az30f15}
\]

At the half fixed gap, `T=(1+o(1))log q+1`; hence only
`O(d/log q)=o(q)` roles can have `s_j>=2T`.  Almost every role is therefore
near-surjective for the upper/lower-hull encoding at precisely the missing
quasipolynomial scale.

This near-surjectivity has a physical planar normal form.  For exact
left/right endpoints `e`, let `C_{i,e},U_{i,e}` count nonsingleton rooted
caps and cups.  There is a bijection

\[
        H_i-D=\sum_e C_{i,e}U_{i,e},                  \tag{3az30f16}
\]

because every nonsingleton face has unique upper and lower chains with the
same endpoints, and every such rooted pair has ordinary union.  Since
there are fewer than `D^2` endpoints, each role with `s_i<=2T` has one
actual endpoint `e_i` satisfying

\[
 {C_{i,e_i}\over C_i-D},
 {U_{i,e_i}\over U_i-D}\ge D^{-(2T+3)}.              \tag{3az30f17}
\]

So a planar coherent ramp contains rooted two-ended product modules in
`(1-o(1))q` roles; their unions are injective ordinary faces.  These faces
are already counted in `H_i`, so this still does not close the parent.
The residue is no longer scalar: it is cross-role anti-alignment of actual
endpoint modules and their tangent gauges.  See
`agent_shield_circuit_cover/COHERENT_RAMP_ENDPOINT_MODULE_LOCALIZATION.md`.

Same-chart cross-role alignment is now ruled out as the missing operation.
For arbitrary rational children and arbitrary rational shears `t_i`, the
placement

\[
 (x,y)\in X_i\longmapsto
   (i+\epsilon^2x,\ i^2+\epsilon(y+t_ix))             \tag{3az30f18}
\]

has, for sufficiently small rational `epsilon`, the same labelled linear
strong-glue chirotope for every shear itinerary.  The distinguished module
chords can therefore be made perfectly slope-aligned or arbitrarily
ordered without changing a single face or circuit.  More decisively, the
ordinary-face count is exactly

\[
 W_{lin}=\sum_iH_i+
  \sum_{i<j}C_iU_j\prod_{i<r<j}(1+D_r).                \tag{3az30f19}
\]

Thus no same-chart tangent bin, seam split, or endpoint rerouting can add
the missing `D^{Theta(log q)}` factor: every possible macro face is already
in `(3az30f19)`.  The coherent-ramp gate is strictly internal to a child,
or must compare a genuinely second projection chamber.  The finite
regression realizes arbitrary aligned/anti-aligned module slopes with an
identical chirotope, but deliberately leaves the unknown low-`H`
constant-potential children unbuilt.  See
`agent_shield_circuit_cover/LINEAR_ENDPOINT_MODULE_ALIGNMENT_BARRIER.md`.

Pathwise multi-projection compression is exact but does not yet supply
that second-chamber comparison.  For one fixed `N`-point order type and
one fixed `h`-tuple of source directions, the walls
`phi(theta_s)=lambda_ab` are homogeneous hyperplanes in the projective
three-dimensional parameter space of `PGL_2`.  Hence

\[
 \#\{\text{exact projection itineraries}\}
       \le c_0(1+hN^2)^3,                              \tag{3az30f20}
\]

only `2^{O(log N+log h)}` classes.  Even numeric endpoint-bin words for
arbitrary low-face child types cost only `O(L)^h=2^{O(L)}` when
`h=L/log L`.  The live recursive use nevertheless fails for three exact
reasons: branch direction tuples can have different cross-ratios, child
order types can differ, and old ancestor queries rapidly cease to be tight.
If one level changes log-size by `ell=Theta(log L)`, then after `k` levels
the inherited profile slack is

\[
 \Phi(L)-\Phi(L-k\ell)
   =2ckL\ell-ck^2\ell^2+o(kL\ell),                   \tag{3az30f21}
\]

so already `k=2` exceeds the entire one-level `Theta(L log L)` recovery
budget.  Thus physically coexisting old directions do not give a long
sequence of calibrated profiles; the compression theorem becomes useful
only after a common-type/common-tuple reservoir with many independently
tight queries is produced.  See
`agent_shield_circuit_cover/PATHWISE_PROJECTION_ITINERARY_COMPRESSION_GATE.md`.

The finite all-direction audit is encouraging but not asymptotic.  For the
`V=1561` mutation-minimal wrapper, all 180 genuine reset chambers have

\[
          C_\xi U_\xi\ge157113,
          \qquad \max(C_\xi,U_\xi)\ge397.              \tag{3az30g}
\]

On the other hand, loop and singleton-transversal data do not force the
strong quotient needed in `(3az30f)`: an exact rational three-cluster
example preserves every mandatory `3+1` loop and every macro transversal
while both adjacent `2+1` seams have mixed signs.  Replacing those seams by
the coherent vertical strong-glue placement increases the exact ambient
face count from `5833` to `6508`, so minimization does not automatically
prefer the reset.

Mixed seams now have an exact quantitative state.  For each role `X_i`, put
an edge between two labels when their repeated-role triple has the wrong
strong-glue sign toward some other role, and let `H_i` cover this graph.
Writing `H=union H_i`, `T=|H|`, deletion has the all-direction decoder

\[
 F\longmapsto(F-H,F\cap H),\qquad
 (Z,\widehat C_\xi,\widehat U_\xi)(P)
 \le2^T(Z,\widehat C_\xi,\widehat U_\xi)(P-H).       \tag{3az30h}
\]

Thus a subquadratic seam cover preserves the full `\Pi_2` state.  This is
sharp: there are rational wrappers with every ordered seam nonhomogeneous
but only one bad pair per role, so `T=O(log n)`.  Conversely, under a
fixed-gap induction input, if a linear number of macroscopic roles have
covers leaving `A/(log n)^B` labels, the repaired strong chain preserves
the inductive coefficient with only `O((log n)loglog n)` loss.  The strict
mixed-seam residue therefore has a linear number of roles whose bad-pair
graphs have `Omega(A)` disjoint edges, hence `Omega(n)` label-disjoint
repeated-coordinate defects in the balanced branch.  Turning that linear
planar matching into bounded-overlap rank-four/one-gap faces is the precise
new geometric target.

That matching now has a constant-loss local normal form.  With the two
canonical neighboring representatives fixed, a bad pair either gives an
ordinary rank-four face or one of four rooted circuits according to its
unique interior label.  Pair-inner circuits are exactly fixed-edge
dominance/nesting records; anchor-inner circuits are chords crossing one
fixed rooted fan ray.  Deleting one canonical neighbor always leaves an
ordinary rank-three face retaining both pair labels with constant decoder
load.  Therefore `Theta(log n)` hard roles each retain a polylogarithmic
menu of one common type.

The convex type has an exact geometric promotion under the complete
same-type transversal hypothesis.  If `{l,a,b,r}` is convex for the
canonical neighboring representatives, then `{a,b}` is a genuine two-point
boundary ear: inserting it into the edge `lr` preserves convexity against
every other transversal label.  Ears in any independent set of cyclic roles
commute.  If total matching mass is `eta n`, role sizes are at most `Cn/q`,
and `q>=kappa log n`, the five-way classification leaves either a common
rooted `1+3` type or at least `eta q/(30C)` independent convex-ear roles.
Choosing `K=(log n)^D` pairs in each of the latter gives, for each fixed
context-compatible retained base, the decoded bank

\[
       K^{\eta q/(30C)}
          \ge n^{(\eta\kappa D/(30C))\loglog n},        \tag{3az30j}
\]

divided only by the actual context decoder load.  The affine two-point
insertion proof is global and does not assume infinitesimal clusters.
However, without such a retained base this is only the already available
absolute singleton-transversal scale: choosing one canonical endpoint of
each matching pair also gives `K^{Theta(q)}` faces and identifies every
pair.  It does **not** multiply the independent half-scale pocket/context
bank.  Thus convex ears solve the local compatibility problem but leave the
same context-coexistence/Hall accounting gate.  The genuinely non-ear local
branch consists of the four rooted `1+3` classes; the sparse rational seam
wrapper makes the union of marked circuit pairs from every three roles
nonconvex.  The remaining statement is context-retaining convex-ear
promotion or cross-role dominance/fan-circuit release, not local rank-four
supply.  See
`agent_common_shield_mixing/CONVEX_BAD_PAIR_EAR_PROMOTION.md`.

The context gate itself now has a sharp endpoint-codegree form.  For a
released convex base `C_F=B union F` and a matching edge `e={a_e,b_e}`, put

\[
 g(e,F)=\mathbf 1[C_F\mathbin\cup\{a_e\}\text{ is convex}]
       +\mathbf 1[C_F\mathbin\cup\{b_e\}\text{ is convex}]. \tag{3az30p}
\]

A compatible endpoint identifies its matching edge, so for weighted
contexts `c` the exact global decoder is

\[
 \sum_cw_c\sum_{e,F}g_c(e,F)\le\Lambda V,              \tag{3az30q}
\]

with `Lambda` the actual output load including roots, guards, bases, and
carriers.  If this compatibility is at most a `theta` fraction of all
pair--pocket incidences, at least a `1-theta` fraction have `g=0`.  Each
such cell carries two canonical `1+3` circuits, one through each endpoint,
and each circuit necessarily meets the actual pocket trace `F`: a witness
avoiding the endpoint lies in `B union F`, while one avoiding `F` lies in
`B union {v}`.  The six-point rational cage

\[
 l=(-3,0),\ r=(3,0),\ t=(0,5),\quad
 a=(-2,-1),\ b=(2,-1),\ x=(0,-4)
\]

is sharp.  The pair `{a,b}` is a convex ear over `{l,r,t}`, and
`{l,r,t,x}` is convex, but both endpoints are hidden in `triangle(l,x,r)`.
Thus even the convex-ear class can have zero attached codegree after the
pocket is retained.

There is, however, an exact detached descent.  Put

\[
 h(e,F)=\mathbf 1[F\mathbin\cup\{a_e\}\text{ is convex}]
       +\mathbf 1[F\mathbin\cup\{b_e\}\text{ is convex}],
 \qquad g(e,F)\le h(e,F).                                  \tag{3az30r}
\]

The corresponding global decoder gives

\[
             \sum_cw_c\sum_{e,F}h_c(e,F)\le\Lambda_{\rm det}V, \tag{3az30s}
\]

where `Lambda_det` measures exactly the reuse caused by erasing the carrier
base.  If `h` is also zero, the two canonical circuits lie wholly in
`F union {a_e}` and `F union {b_e}`; after relative circuit-component
factoring this is one detached pocket child.  The displayed cage is sharp
for the middle branch: it has `g=0` but `h=2`.  Consequently the live
trichotomy is now precise: an attached endpoint--pocket bank retaining the
context, a detached bank with explicit context-erasure load `Lambda_det`, or
a double detached endpoint--pocket circuit child.  Before guard release the
high-root geometry is more extreme: every nonempty pocket trace is caged by
the retained root triangle.  See
`agent_common_shield_mixing/ENDPOINT_POCKET_CODEGREE_DICHOTOMY.md`.

In fact the detached branch always has a second ordinary target before any
pair-ear classification:

\[
                  W=F\cup\{v\},\qquad Q=B\cup\{v\}.
\]

The first is detached compatibility and the second is the source-side
compatibility hypothesis.  Fractional Hall routing gives the exact linear
bound

\[
 \eta_*=max_{\varnothing\ne\Omega'\subseteq\Omega}
 {\sum_{\omega\in\Omega'}w_\omega
  \over|\bigcup_{\omega\in\Omega'}\{W_\omega,Q_\omega\}|},
 \qquad H_{\rm det}\le\eta_*V.                         \tag{3az30s1}
\]

Thus a common detached face with many distinct released bases is a harmless
star of load below one.  With disjoint roles `(W,Q)` recovers `v,F,B,e`.
Its parallel-edge multiplicity is exactly the fixed-pair residue below.
The released face `C=B union F` and old source `A=B union G` are also
unconditional ordinary targets.  Hence the still stronger four-target Hall
value

\[
 \lambda_4=max_{\varnothing\ne\Omega'\subseteq\Omega}
 {\sum_{\omega\in\Omega'}w_\omega
  \over|\bigcup_{\omega\in\Omega'}\{W_\omega,Q_\omega,C_\omega,A_\omega\}|}
 \quad\hbox{satisfies}\quad H_{\rm det}\le\lambda_4V.    \tag{3az30s1a}
\]

Role coloring makes `C` decode `(B,F)` and `(A,C)` decode the omitted mask
`G`.  A high four-target core is therefore a genuine old-source by released-
face rectangle, or actual duplicate history over one `(A,C)`, rather than
erased geometry.  The scalable cage realizes an `m by m` rectangle of
density `m^2/(3m+1)`.  A convex-cloud realization is paid by a Boolean
shield, but this is not forced: the guard and pocket clouds may be replaced
independently by arbitrary rational order types inside two tiny open cage
regions, preserving every record and Hall density.  Thus the exact residue
is a global two-separated-cloud composition/profile theorem, not a local
Boolean-support claim.  See
`agent_outer_internal_product/DETACHED_BASE_ENDPOINT_HALL_STRENGTHENING.md`.

The pairwise-convex column itself has an exact circuit-cover dichotomy.
If

\[
 B\cup F,\qquad B\cup\{v\},\qquad F\cup\{v\}
\]

are faces but `B union F union {v}` is not, every bad four-circuit contains
`v`, meets both `B` and `F`, and has role split `2B+1F+v` or
`1B+2F+v`.  Delete `v` from these circuits and let `tau` and `nu` be the
transversal and matching numbers of the resulting 3-uniform trace
hypergraph.  Four-locality gives the exact release criterion and the
standard matching cover bounds

\[
 U-Z\text{ is convex}\quad\Longleftrightarrow\quad
 Z\text{ hits every trace},\qquad \nu\le\tau\le3\nu.   \tag{3az30s1b}
\]

Hence a canonical minimum release has `2^{r-tau}` rooted downfaces
containing `v`, while the union of a maximum disjoint trace matching is a
detached Boolean shield of size at least `2^tau`; locally one reservoir is
at least `2^{r/2-O(1)}`.  Globally the exact statements retain their actual
loads:

\[
 \sum_\omega w_\omega2^{r_\omega-\tau_\omega}
       \le\Lambda_{\rm rel}V,
 \qquad
 \sum_\omega w_\omega(2^{3\nu_\omega}-1)
       \le\Lambda_{\rm tr}V.                           \tag{3az30s1c}
\]

This still does not mix a source row with its released column.  A scalable
same-edge rational rectangle has one unique one-label circuit release in
each column, yet every released face is incompatible with every source
row and even `A union C` is bad; it attains
`lambda_4=m^2/(3m+1)`.  Its singleton row and column marks expose an
injective `m^2` two-point bank, so it is not a global regression.  It shows
that the live counterfamily must combine quadratic row/column entropy with
high reuse of every small projection.  Bad circuits also need not meet the
old tangent neighbors of `v`, so no unproved tangent guard is available.
See
`agent_shield_circuit_cover/PAIRWISE_CONVEX_TRIPLE_CIRCUIT_COVER.md`.

Stripping the common base gives a second exact rectangle-or-shield bank.
Write `A=B union G`, `C=B union F`; heredity makes `G,F` ordinary.  If
`G union F` is bad, every four-circuit meets both sides.  For its
4-uniform circuit hypergraph let `tau` and `nu` be the transversal and
matching numbers.  Then `nu<=tau<=4nu`; a minimum transversal releases a
mixed face of rank `r-tau`, while a maximum matching places at least
`tau/2` labels in one convex side.  Choosing the released downset when
`tau<=2r/3` and the one-side shield otherwise gives the exact global
incidence

\[
 \sum_\omega w_\omega(2^{r_\omega/3}-1)
                    \le\Lambda_{\rm trace}V.           \tag{3az30s1d}
\]

Canonical row/column marks also give an ordinary two-point output, so high
projection reuse fixes one actual mark pair before `(3az30s1d)` is used.
A genuine quadratic product lift with large mark reuse is paid by load-one
mixed traces.  Therefore a surviving lift must simultaneously make almost
all `G union F` bad and force high reuse of both the low-transversal
release and the opposite-side shield.  See
`agent_shield_circuit_cover/QUADRATIC_TRACE_RECTANGLE_OR_SHIELD.md`.

The marginal `Lambda_det` can be exponentially large and should not be
bounded directly.  As a secondary symmetric encoding, there is an exact
two-face recovery.  For a detached
record use

\[
              C=B_c\cup F,\qquad D=F\cup\{v\}.
\]

Both are ordinary faces, and `(C,D)` recovers
`F=C intersect D`, `B_c=C setminus F`, `v`, and the matching edge.  If
`mu_det` is the true residual pair load and `H_det` the weighted record mass,
then

\[
                   H_{\rm det}\le\mu_{\rm det}V^2,\qquad
                   V\ge\sqrt{H_{\rm det}/\mu_{\rm det}}. \tag{3az30s2}
\]

A scalable rational parabola regression shows sharpness: a common pocket
simultaneously destroys `q` pairwise nonadjacent old source gaps and hides
both endpoints, while every detached `F union {v}` remains convex.  Optional
tail masks give `Lambda_det=2^M`, but the released bases distinguish all
`2^M` contexts, the pair load is one, and the tail is itself the erased
Boolean shield.  Thus the multirole theorem below genuinely needs boundary
edges recomputed in the released hull; inherited source gaps are unusable.
See `agent_shield_circuit_cover/DETACHED_LOAD_TWO_BANK_AND_GAP_RESET.md`.

The residual load of one fixed pair `(C,D)` has an exact one-face
description.  It fixes `B,F,v,e`; every remaining record comes from an
ordinary actual source `A=B union G`.  If `kappa_src` is the maximum total
weight over one actual source, then

\[
                         H_{C,D}\le\kappa_{\rm src}V.       \tag{3az30s4}
\]

Thus distinct source completions pay losslessly.  Heredity gives more: if
`R(G)` is a canonical longest cyclic run of the deleted mask, then

\[
 \sum_\omega w_\omega(2^{|R(G_\omega)|}-1)
                 \le\Lambda_{\rm run}V.                    \tag{3az30s5}
\]

In particular, masks of rank at least `t` and at most `s` runs give a
one-face multiplier `2^{ceil(t/s)}-1`.  Many runs create many compressed
source gaps and pass to the released-gap/endpoint-entropy split below; few
runs force one long Boolean run.  The sole leftover is duplicate chronology
over the same actual source.  This cannot be inferred from planarity--named
copies change no face--and is already bounded in the genuine likelihood
normalization by weighted-history domination; a raw-count use needs an
explicit actual-mark multiplicity.  A rational fixed-pair regression attains
`mu_det=2^M`, with exactly `2^M` distinct source faces and a length-`M`
Boolean run bank.  See
`agent_shield_circuit_cover/DETACHED_PAIR_SOURCE_MASK_HALL.md`.

Canonical radial depth is not part of that multiplicity: the ordered source
`A` and its endpoint pair `e` uniquely determine the peel depth and retained
carrier.  If the remaining choice is an actual exterior guard `y`, its
repaired target satisfies `T(A,y) setminus A={y}`.  In a fixed detached-pair
fibre with `s` sources, at most `d` distinct guards per source, and actual
tuple multiplicity `h`, the source and target banks give

\[
                              V\ge\sqrt{H/h}.             \tag{3az30s6}
\]

Thus simultaneous carrier and actual-guard variation already has a
coefficient-half payment for canonical set-valued records (`h=1`).  The
only raw residue is dense cross-source reuse in the full source--target Hall
graph, or nongeometric duplicate metadata over one actual `(A,y)` tuple.

When the old matching edge `e={v,u}` is a genuine convex pair ear over its
source `A`, the square loss in `(3az30s2)` can be replaced by exact linear
Hall routing.  Every record has two ordinary one-face targets

\[
                       W=F\cup\{v\},\qquad E=A\cup e.
\]

For any weighted record family `R`, the optimal fractional load is

\[
 \lambda_*=max_{\varnothing\ne\mathcal R'\subseteq\mathcal R}
 {\sum_{r\in\mathcal R'}w_r
  \over |\{W_r,E_r:r\in\mathcal R'\}|},
 \qquad \sum_r w_r\le\lambda_*V.                       \tag{3az30s3}
\]

Thus one detached face shared across arbitrarily many distinct source ears
is merely a star and routes with load below one.  The ordered pair `(W,E)`
recovers `F,v,u,e,A`; only its actual root/guard/history multiplicity
`Delta` remains.  If `lambda_*>K`, pruning leaves a weighted target graph
of minimum degree greater than `K`, and, when pair multiplicity is at most
`Delta`, more than `K/Delta` distinct neighbors at every vertex.  Hence the
true convex-ear residue is a dense two-sided detached-face by source-ear
core, not a high marginal detached star.  A rational cage realizes the
star sharply and confirms that local mixing can still fail.  See
`agent_outer_internal_product/DETACHED_LOAD_SOURCE_EAR_HALL.md`.

The attached branch has the exact missing multirole scale.  Suppose the
released polygon `C_(c,F)` has `q` named candidate gaps which are actual
consecutive boundary edges, and let `k_i(c,F)` be the number of compatible
endpoints at gap `i`.  Three-coloring the boundary-gap cycle and taking its
heaviest color class gives the threshold-free entropy

\[
                     S(c,F)=\sum_i\log\max\{1,k_i(c,F)\}.
\]

Singleton ears on that independent color class commute, and the weighted
global decoder is

\[
 \sum_{(c,F)\in\mathcal D}w_c\,2^{S(c,F)/3}
             \le\Lambda_{\rm multi}V.                    \tag{3az30t}
\]

There is a stronger role-free form.  Every individually compatible endpoint
has a unique actual insertion edge `g` of the released polygon.  Let
`H_g(C)` count, including the empty choice, all endpoint subsets which form
one rooted convex ear at `g`, and put
`E_root(c,F)=sum_g log H_g(C_(c,F))`.  Rooted ears on nonadjacent edges
commute, so the same three-coloring gives

\[
 \sum_{(c,F)\in\mathcal D}w_c\,2^{E_{\rm root}(c,F)/3}
             \le\Lambda_{\rm root}V.                    \tag{3az30t1}
\]

This automatically merges named roles landing on one actual gap and uses
all higher rooted profiles there.  If a gap has `k_g` singleton endpoints
but only `H_g` rooted subsets, then at least

\[
              {k_g\choose2}-H_g+1+k_g                    \tag{3az30t2}
\]

endpoint pairs give the same-edge rooted four-circuit.  Fixed-edge tangent
dominance and Dilworth further extract a nested chain of length
`k_g/w_g`, where
`binom(w_g,2)<=H_g-1-k_g`.  This conclusion is deliberately pairwise:
an exact six-point example has all three endpoint pairs rooted-convex but
the three-endpoint union nonconvex.  Thus low rooted entropy produces a
common-edge cage/fan alphabet, not a fictitious Boolean rooted bank.

There is nevertheless an exact higher-order sharpening.  Normalize the
root edge and order endpoints by their two tangent coordinates.  For every
integer `D>=2`, either the dominance poset has a nested chain of length
`D`, or Dilworth supplies a reverse-dominance antichain `Y` of size
`w>=k_g/(D-1)`.  All pairs in `Y` are rooted faces.  If `A` is its largest
rooted-cap face and `B` its largest oppositely oriented cup, the classical
cup--cap recurrence gives

\[
 w\le {A+B-2\choose A-1},\qquad
 H_g\ge2^A,\qquad
 B\ge {\log w\over\log(2A)}.                            \tag{3az30t3}
\]

Every triple in the bad cup is a genuine `1+3` circuit with one of the two
fixed root-edge endpoints; pair compatibility rules out a smaller witness.
Taking `D=ceil(sqrt(k_g))`, one actual gap therefore yields one of three
objects: a `sqrt(k_g)` nested fixed-edge cage, rooted entropy already large
enough for `(3az30t1)`, or a homogeneous two-root triple-circuit fan of
length

\[
                 B\ge {\log k_g\over2\log(2\log H_g)}.   \tag{3az30t4}
\]

At `k_g=n^{1-o(1)}`, failure of the required
`log H_g=Omega((log n)loglog n)` multiplier thus leaves a fan of length
`Omega(log n/loglog n)` unless the much larger nested cage occurs.  This
uses cup--cap only after the dominance-antichain reduction and so does not
repeat the false inference that pairwise rooted compatibility is Boolean.

For two role-colored alphabets on a common released base, the same actual-
gap argument combines their reservoirs without choosing names.  If
`H_g^X,H_g^Y` are the two rooted-complex sizes at edge `g`, choose the
richer complex edgewise and then the richest color of a proper 3-coloring
of the boundary cycle.  This gives the load-tracked bank

\[
 R(B;X,Y)\ge
       \left(\prod_gH_g^XH_g^Y\right)^{1/6},\qquad
 \sum_fw_fR_f\le\Lambda_{\rm gap}V.                    \tag{3az30t5}
\]

Thus combined rooted entropy at least
`6 log M+6 sigma(log n)loglog n` pays the missing
`n^{sigma loglog n}` multiplier.  The hypothesis is genuine: the dense
`A by C` Hall targets alone do not say that guards are ears of released
columns.  Even adding every singleton cross compatibility does not force
surplus.  An exact rational construction puts the two clouds on adjacent
base edges as dominance chains; every cross singleton union is convex,
but every same-cloud pair is rooted-bad, both rooted complexes have size
`m+1`, and the entire base-retaining mixed bank is exactly `(m+1)^2`.
Those detached chains are Boolean, so the precise survivor is reuse of
their detached banks across external base/root histories, not a missing
local fan.  See
`agent_outer_internal_product/DENSE_RECTANGLE_ACTUAL_GAP_FAN_GATE.md`.

Nor does the dense rectangle align the two detached cloud profiles after
the base is erased.  There are open common-cage and rooted-fan cells in
which the row and column clouds have independently arbitrary rational order
types, every target `W,Q,C,A,E` is ordinary, `(A,C)` and `(E,W)` have unit
decoder load, and the exact five-target Hall value is
`lambda_5=m^2/(4m+1)`.  In lexicographic placement their detached union has
the exact two-block recurrence

\[
                V(Y\cup Z)=V(Y)+V(Z)+R(Y)A(Z).          \tag{3az30t6}
\]

Oppositely oriented pure parabolic chains have
`V(Y)=V(Z)=2^m-1` but both facing profiles equal only
`m+binom(m,2)`, so every bounded-anchor face meeting both clouds contributes
only polynomial cross mass.  Independent reflections realize all four
products `S^2,ST,TS,T^2` with identical Hall and circuit data.  Therefore
neither density, the five decoded targets, nor the normalized cage/fan
signature implies the missing two-cloud multiplier.  A successful next
step must use an internal-bank Cauchy route with globally summable overlap,
a genuine cyclic third profile cut, or chronology correlating the two
reflections.  See
`agent_common_shield_mixing/DENSE_HALL_TWO_CLOUD_PROFILE_BARRIER.md`.

Crucially, profile anti-alignment does not defeat the **internal-bank**
Cauchy route.  For a context with a simple `a_c by b_c` record core of
size `e_c`, give every record weight `w_c`.  Its five-target bank has
`h_c=2a_c+2b_c+1` faces, while for `a_c,b_c>=6` the two physical clouds
have the order-type-independent triangle bank

\[
                    i_c={a_c\choose3}+{b_c\choose3}.
\]

The exact local inequality `h_ci_c>=(20/27)e_c^2`, followed by one global
Cauchy step, gives

\[
 \sum_cw_ce_c\le {5\over2}\Lambda_HV
   +\sqrt{27\over20}\sqrt{\Lambda_H\Lambda_3},V.      \tag{3az30t6a}
\]

Here `Lambda_H` and `Lambda_3` are the actual weighted overlaps of the
five-target and physical-triangle banks; contexts with a side of size at
most five form the first term.  This survives arbitrary reflections and
the exact parabolic anti-alignment regression.  Failure now fixes an
actual reused triangle together with a reused Hall target, and hence--up
to the true triangle-to-child support degree--one physical child queried
in many contexts.  Only at that point are cyclic profile identities or
coherent multi-direction `PGL_2` itineraries applicable.  Unrecorded
duplicate chronology multiplies demand and both loads equally and is the
sharp abstract obstruction; it must be removed by canonical history or an
actual mark.  See
`agent_common_shield_mixing/DENSE_HALL_INTERNAL_TRIANGLE_CAUCHY.md`.

Separating the base-decoding targets from the common Hall targets sharpens
the localization but does not close it.  With `h_c=a_c+b_c`, base-target
load `Lambda_B`, and physical-triangle load `Lambda_3`, the exact variant is

\[
 \sum_cw_ce_c\le5\Lambda_BV
  +\sqrt{27\over10}\sqrt{\Lambda_B\Lambda_3},V.        \tag{3az30t6b}
\]

On `M` distinct quadratic base words sharing the same `m`-point clouds,
`Lambda_B=1` but `Lambda_3=M`, so this gives only
`V>=sqrt(10/27)sqrt(M)m^2`, asymptotically weaker than the source bank
`V>=M`.  Canonical per-source weight controls the first load, not the
geometric reuse of one triangle across distinct sources.  This is sharp in
one stationary chamber: all `q` base roles can be placed so that every
role label together with every guard- or pocket-cloud triangle is a bad
`1+3` set, while all five targets and actual gaps persist.  Thus any face
retaining one variable role has cloud rank at most two, whereas every
triangle output omits the full word and has load `M`; all queries have one
direction/sign, so neither a four-direction itinerary nor a cyclic profile
is forced.  See
`agent_outer_internal_product/FULL_WORD_TRIANGLE_REUSE_SCALE_BARRIER.md`.

There is still a useful live-weight sharpening before that stationary
atom.  Use each old source once per dyadic record-weight layer rather than
once per release neighbor.  If canonical source-mark weight is at most one
and the upstream description load is `L`, the compressed source load is
`kappa_A<2L`.  Pairing its `a_c` source targets with triangles in the
larger side `t_c=max(a_c,b_c)` uses
`a_c binom(t_c,3)>=(5/54)e_c^2` and gives

\[
 M\le5\kappa_AV+sqrt{54\over5}
            \sqrt{\kappa_A\Lambda_\triangle},V.       \tag{3az30t6c}
\]

Thus failure at multiplier `K` fixes one actual triangle of weight at
least `(5/54)K^2/kappa_A`, preserving the full
`n^{Theta(loglog n)}` scale.  For its retained base `B`, either `B union T`
is a decoded mixed face, or a canonical bad circuit has one of only sixteen
signed `2T+2B`/`3T+1B` classes.  This localization is sharp: a square base
with `2^r` Boolean top-ear contexts and one bottom parabolic triangle gives
distinct genuine sources, the same actual triangle and direction, and
`B_R union T` bad for every `R`.  There is no chronology duplication,
cycle, or fourth query; the example is paid exactly by its Boolean base.
The next operation is therefore a source-downshadow/cyclic payment for a
fixed-triangle one-direction star, not further graph theory.  See
`agent_common_shield_mixing/HIGH_TRIANGLE_QUERY_LOCALIZATION_GATE.md`.

At the actual quasipolynomial scale required by the fixed-gap bootstrap,
that apparent star is already paid.  In each nonempty weighted product
context choose one canonical old-source face `A_c`; let `a_c` be its number
of source targets, `e_c` its record count, and
`i_c=binom(max(a_c,b_c),3)` in the thick branch.  Tag every selected
physical triangle `T` by the ordered pair `(A_c,T)`.  If `kappa_A` is the
dyadically compressed source load, then

\[
 \sum_cw_ca_c\le\kappa_AV,
 \qquad
 \sum_cw_ci_c\le\kappa_AV{n\choose3}.                 \tag{3az30t6d}
\]

Indeed a fixed `(A,T)` pair has weight at most `kappa_A`; no union
`A union T` is asserted to be convex.  The local inequality
`e_c^2<=(54/5)a_ci_c` and one global Cauchy step therefore give

\[
 \sum_cw_ce_c\le
 \kappa_A\left(5+\sqrt{{54\over5}{n\choose3}}\right)V
 \le\kappa_A\left(5+{3\over\sqrt5}n^{3/2}\right)V.    \tag{3az30t6e}
\]

Entering an actual source once in each nonempty dyadic layer, rather than
once per release neighbor, preserves all record edges and gives
`kappa_A<2L` for actual description load `L`.  Thus polynomial `L` costs
only a polynomial factor in `(3az30t6e)`, which is swallowed by the
required `n^{sigma loglog n}` recovery multiplier.  This remains true after
fixing a triangle, circuit signature, direction, SCC, base type, or history
state, and it allows arbitrary low-face/product bases.  It does **not**
prove the fixed-power target `(EIC')`, since the ambient triangle tag costs
`n^(3/2)` after Cauchy.  Its exact scope is to close the later
quasipolynomial fixed-triangle/source-word obstruction once the upstream
reduction has produced these coalesced product contexts.  See
`agent_common_shield_mixing/QUASIPOLY_SOURCE_TRIANGLE_TAG_CLOSURE.md`.

An end-to-end audit prevents turning this terminal estimate into a theorem
prematurely.  Fixed-gap minimality does rigorously give `mu=O(log n)`, a
rank-`O(log n)` marked source family of `Omega(V)` weight and per-source
cap one, a deterministic pocket of size `n/polylog n`, and
`Omega(log n)` disjoint outer circuit traces.  The direct
unordered-release theorem `(3d3a)`--`(3d3e)` now removes the former
complete-product assumption from the cover-entropy entrance and promotes
the low-redundancy half.  Three
downstream promotions are still missing before `(3az30t6d)` applies
uniformly:

1. finish the high-mean `R_U` branch now reduced by `(3d3j)`--`(3d3x)`:
   it occurs only at excess rank, both completion and release sides are
   live-normalized, and quadratic completion redundancy already fixes a
   physical four-role circuit box; the missing statement is profile
   penetration/coexistence with the simultaneously live released side,
   not selected-family Cartesian extraction;
2. send every high-load rooted fan/cage branch either to an already paid
   attached/detached/source-mask bank or to a coalesced label-level dense
   rectangle carrying the required relative mass; and
3. bound all genuinely noncoalescible base/root/tangent/cover/mask/history
   descriptions by an actual polynomial load `L`.

The first is precisely where the marked Reed--Solomon regression rules out
selected-family module extraction: the payment has to come from ambient
geometry.  The new four-local coordinatization supplies the physical box,
but does not make it coexist with the live opposite face family.  The
second is not supplied by endpoint Hall
density or rank-four classification: the commuting ear bank is absolute
unless it coexists with the pocket context.  The third holds inside a fixed
canonical dyadic state but is not automatic across all such states.
Accordingly `(3az30t6d)` closes the terminal dense context, not the
unrestricted half theorem.  See
`agent_common_shield_mixing/END_TO_END_QUASIPOLY_GATE_AUDIT.md`.

Its point-cloud hypothesis is also real.  In the stationary full-word
tensor, a context is one base word, the rows are actual source faces, and
the internal side is a genuine `m`-point cloud, so the triangle tag is
valid and the local inequality is exact at `m=6`.  An arbitrary
face-by-face rectangle is different: `a` source faces are not an
`a`-point cloud.  An exact `q=8` hereditary example has 255 ordinary source
faces but only `binom(8,3)=56` physical triangles, and substituting 255 for
the cloud size makes the local inequality false.  Thus high-projection
face alphabets remain part of promotions 1--2.  Likewise the scalar
finite-gap strong-comb ramp is upstream: its `C_i,U_i` are face counts and
need not generate any excess bipartite record demand.  At the balanced
quarter-word scale its source bank can be exponentially smaller than the
inherited half-scale child bank.  See
`agent_shield_circuit_cover/SOURCE_TRIANGLE_TAG_APPLICABILITY_AUDIT.md` and
`agent_outer_internal_product/QUASIPOLY_SOURCE_TRIANGLE_TAG_INTEGRATION_AUDIT.md`.

There is an exact hereditary extension, but it stops at the same boundary.
If a context exposes `i_c` actual ordinary tags of rank at most `k` and

\[
                         e_c^2\le\Gamma a_ci_c,
\]

then the same source-tag Cauchy argument gives

\[
 \sum_cw_ce_c\le
   \sqrt\Gamma\,\kappa_A
      \sqrt{\sum_{j=0}^k{n\choose j}}\,V.             \tag{3az30t6f}
\]

For a target `n^{sigma loglog n}`, polynomial `Gamma,kappa_A`, this is
free only for `k<=(2sigma-epsilon)loglog n`.  Heredity alone cannot supply
the local reservoir: `b` rank-`r` alphabet faces have at most `b2^r`
individual subface tags, whereas a balanced `m by m` rectangle would need
`i_c>=m^3/Gamma`, forcing `m^2<=Gamma2^r`.  Oppositely oriented parabolic
clouds with alphabets consisting of all rank-`r` faces realize the failure
exactly: every row and column is ordinary, every cross union is bad, and
the full downshadow is far too small.  Their detached Boolean shields show
that this is a promotion barrier rather than a low-face counterexample.
Thus replacing physical triangles by arbitrary small hereditary subfaces
does not solve promotions 1--2.  See
`agent_shield_circuit_cover/HEREDITARY_FACE_TAG_CAUCHY_GATE.md`.

Nor can one detached Boolean side repair the exponent mismatch by itself.
If its actual face-bank load is `Lambda_S` and locally
`e_c^2<=Gamma a_cs_c`, exact two-bank Cauchy gives

\[
              \sum_cw_ce_c\le
                 \sqrt{\Gamma\kappa_A\Lambda_S}\,V.  \tag{3az30t6i}
\]

For a balanced `m by m` hard rectangle the shield reservoir must have
`s>=m^3/Gamma`.  At `m=n^{tau loglog n}` a rank
`k=c loglog n` Boolean subshield needs `c>=3tau`, whereas the source-tag
cost is below a target `n^{sigma loglog n}` only for `c<2sigma`; these are
incompatible when `tau>=sigma`.  Any fixed number of low-rank tag banks has
the analogous Hölder mismatch.  The full shield fixes the local count but
can have load `D^q` across quadratic base words.  Even allowing the output
to retain `h` adaptive base labels leaves load at least

\[
                  {D^{q-h}\over(q+1)2^q};             \tag{3az30t6j}
\]

getting below the Cauchy allowance forces retention of all but
`O(loglog n)` among `q=Theta(log n)` base roles.  The regression preserves
the ACP targets and permits arbitrary low-face side children.  Hence the
missing promotion must produce a genuinely mixed face retaining almost
the full base word, or a separate global composition payment; bounded-rank
shield tags cannot do it.  See
`agent_shield_circuit_cover/DETACHED_BOOLEAN_SHIELD_CONTEXT_REUSE_GATE.md`.

The third prerequisite is now separated from those two geometric ones.
For a fixed rank-`r=O(log n)` actual source, any fixed number of masks,
ordered traces, partitions, matchings, and canonical flags supported on the
source, together with a fixed number of ambient point labels, has only

\[
                  L_{lab}\le C(r+1)^c2^{cr}n^s=n^{O(1)}          \tag{3az30t6g}
\]

states.  Canonical radial depth/carrier adds nothing.  Pooling all distinct
actual column labels in one state and dyadic layer into a simple row star
then gives `kappa_A<2L_lab`.  Even allowing all source-internal
combinatorial data costs at most
`(r+1)^{c_0r}=n^{(c_0kappa+o(1))loglog n}`.  This is still affordable when
the rich-role threshold `(log n)^D` is available with arbitrarily large
fixed `D`: the exact coefficient condition is

\[
                    \sigma>6a+c_0\kappa+C_{ret},       \tag{3az30t6h}
\]

where `a=1/2-delta`, `r<=kappa log n`, the pocket scale loss is
`(6a+o(1))(log n)loglog n`, and `C_ret` records the other certified
retention losses.  Thus polynomial description load is proved for
label-primitive terminal records and can be relaxed to controlled
quasipolynomial source-internal state.

The exception is geometric, not metadata.  A fixed rank-three source,
root, guard, and column label can carry `2^{m-1}` distinct actual released
pocket faces.  Pooling them to one `(A,x)` edge loses that factor; retaining
the face makes the state alphabet exponential.  The example is paid by
the load-one released-face bank itself.  Therefore the remaining upstream
statement is a label-primitive-or-bounded-overlap **face-bank dichotomy**;
rank safety alone does not provide it.  See
`agent_outer_internal_product/POLYNOMIAL_DESCRIPTION_LOAD_FACE_ALPHABET_BARRIER.md`.

The bounded-overlap half of that dichotomy now has an exact global Hall
form.  Give every weighted release record its two actual ordinary targets
`A_omega,F_omega`, and put

\[
 \eta_*=max_{\varnothing\ne\Omega'\subseteq\Omega}
 {\sum_{\omega\in\Omega'}w_\omega\over
  |\bigcup_{\omega\in\Omega'}\{A_\omega,F_\omega\}|}.
\]

Fractional max-flow/min-cut routing gives

\[
                       \sum_\omega w_\omega\le\eta_*V.           \tag{3az30t6k}
\]

If `eta_*>K`, iterative weighted pruning instead produces a nonempty
source--released-face core of minimum weighted degree greater than `K`.
After fixing a projected `x in F` and compressing the source-internal
state with load `delta<=2L_src`, each actual pair `(A,F)` has weight at
most `n delta`; hence every core vertex has more than

\[
                         {K\over n\delta}                         \tag{3az30t6l}
\]

distinct opposite faces.  This preserves quasipolynomial degree when
`K=2^{sigma L log L}` and the certified description exponent is smaller
than `sigma`.  It rigorously closes the bounded-overlap released-face
branch, but the high branch is a dense **face--face** core, not a physical
label rectangle.  Two oppositely oriented parabolic `p`-point clouds with
rows and columns all rank-`r` faces give a complete
`M by M` bad-union graph, `M=binom(p,r)`, Hall density `M/2`, and unit pair
load.  Fixing `(F,x)` still leaves `M` source faces supported on only `p`
labels.  At `r=Theta(log log p)` this is exactly quasipolynomial; detached
Boolean clouds pay it, so it is a sharp promotion barrier, not a minimizer
counterfamily.  The remaining high branch therefore requires a
physical-support/hereditary tag or a detached/internal face bank with
controlled global overlap.  See
`agent_outer_internal_product/RELEASED_FACE_HALL_LABEL_PRIMITIVE_GATE.md`.

The detached-bank overlap can remain quadratic after adding genuine base
entropy.  Take `q` strongly separated base roles of alphabet `D`, so
`M=D^q` base transversals are convex, and attach the same adjacent
double-dominance rectangle to every word.  All five targets and actual-gap
states persist and the exact base-retaining count is only `M(m+1)^2`.
Every detached cloud output is reused over all `M` bases.  Even if a decoder
adaptively augments it by at most `h` selected base labels, pigeonholing
gives an output of load at least

\[
                   {D^{q-h}\over(q+1)2^q}.             \tag{3az30t7}
\]

For `q=Theta(log n)` and `D=n^{1-o(1)}`, making this load
`n^{o(loglog n)}` requires `q-h=o(loglog n)`: essentially the entire base
word must coexist with the detached profile.  Fixed-edge projective
universality lets both reset clouds be arbitrary low-face children, so a
bounded root/tangent/mark history cannot solve the overlap.  This is still
not a low-face construction--the base words and other cross profiles are
ordinary--but it isolates the obstruction faced by a **one-face** detached
bank as a mask-aware coexistence theorem retaining almost every base role,
or a compensating long-run/cyclic bank.  At the later
`n^{Theta(loglog n)}` scale the two-coordinate tag `(3az30t6d)` bypasses
this one-face load; the construction remains a fixed-power applicability
barrier.  See
`agent_outer_internal_product/QUADRATIC_BASE_WORD_DETACHED_REUSE_BARRIER.md`.

The proposed almost-full-word coexistence endpoint is itself false.  Take
`q=2k` tiny role cells of alphabet `D` around a parabolic macro cap, so all
`M=D^q` full transversals are ordinary, and let `Y` be an arbitrary
rational central child.  Pair averaging fixes `o,p in Y` contained in a
coface family

\[
 |\mathcal J|\ge {V(Y)-|Y|-1\over {|Y|\choose2}}.      \tag{3az30t7a}
\]

After an affine placement, `p` lies strictly inside every triangle
`conv{o,a,b}` with `a` from the left base arc and `b` from the right.
Consequently `F union S` is nonordinary for every `F in mathcal J` as soon
as the partial base word `S` meets both arcs.  No such output can retain
more than `q/2` roles: every successful mask deletes one entire consecutive
half-word.  Across all full words, however, the union of the two one-sided
run banks has only

\[
                         2(D+1)^{q/2}-1               \tag{3az30t7b}
\]

distinct base states, with exact rank-`t` load `D^{q-t}`.  Even if every
one-sided union with `F` were ordinary, there would be at most
`|mathcal J|[2(D+1)^{q/2}-1]` outputs.  For `D=Theta(n/q)` this retains
only half the quadratic base exponent: coefficients `a=c=1/4` give at
most `c+a/2=3/8`, not `1/2`.  This is not a global sub-half construction,
because other directional profiles may pay.  It proves that neither an
almost-full mixed face nor the exact longest-run Boolean bank solves the
high face-bank overlap.  The remaining escape must multiply the left and
right directional states, or globally charge their common central `1+3`
circuit family.  See
`agent_shield_circuit_cover/ALMOST_FULL_WORD_MIXED_BANK_BARRIER.md`.

Even that proposed left--right trace multiplication is false for an
arbitrary child.  A fixed-edge projective tangent map preserves any
rational child order type `Y` while placing all its labels in one strict
nesting chain relative to every left--right outer pair.  Put

\[
             P=(D+1)^{q/2}-1,\qquad H=V(Y),\qquad M=D^q.
\]

Among all faces using at most one label from each base role, the *complete*
restricted trace complex then satisfies

\[
              V_{tr}\le H(1+2P)+(|Y|+1)P^2.           \tag{3az30t7c}
\]

Indeed a face meeting both base arcs can retain at most one child label;
the displayed upper bound already grants every child face to both
one-sided banks.  If `log M=(a+o(1))L^2` and
`log H=(c+o(1))L^2`, this gives only

\[
 {\log V_{tr}\over L^2}le\max\{a,a/2+c\}+o(1),       \tag{3az30t7d}
\]

which is `3/8` at `a=c=1/4`.  The common pair-star `mathcal J` does not
repair the loss: its canonical `1+3` circuit has exact load
`D^{q-2}|mathcal J|`; tagging by the full base word leaves load
`|mathcal J|`, tagging by `F` leaves `D^{q-2}`, and only the separated
pair `(B,F)` is injective.  Any ordinary full-word release retains at most
one child label and therefore has load at least

\[
                         {|\mathcal J|\over |Y|+1}.    \tag{3az30t7e}
\]

This still does not upper-bound the ambient construction: multi-label
faces inside base-role cells, other masks, and other directional profiles
remain.  It does decisively remove all operations confined to the
one-label-per-role trace complex.  The surviving theorem must be an
ambient composition bank using those additional faces, or a coupling of
arbitrary one-sided profile spectra.  See
`agent_shield_circuit_cover/CENTRAL_NESTED_CHILD_TWO_SIDED_PRODUCT_BARRIER.md`.

A directed cycle/DAG split supplies no missing geometry before that tag is
used.  A Hall-dense directed context graph has a weighted minimum-degree
core and hence either a directed cycle or a source/sink star.  But three
pairwise-convex cloud unions can form a directed 3-cycle whose full union is
bad by a `1+2+1` circuit.  Likewise degree `d` at one physical cloud yields
four genuinely different projective direction chambers only after an
honest per-chamber load bound `M` with `d>3M`.  An exact rational
`16 by 16` nested-shell product has 256 records, Hall density `256/49`,
mark load 64, minimum-release load 8, downface load 128, shield load 16,
and every query in one strict containment chamber.  Exhausting its 18-point
ground set gives

\[
 V=6023,
 \qquad (v_0,\ldots,v_8)=(1,18,153,816,1880,2008,966,177,4). \tag{3az30t8}
\]

This is a graph/profile applicability barrier, not a low-face example.
In particular, the tempting arbitrary-child central-shell omitted-gap
formula is false: strong separation does not make multi-point endpoint
profiles coexist, as the rank-14 endpoint counterexample already shows.
The exact directed audit therefore leaves the stationary heterogeneous
one-chamber state open at fixed-power scale and makes no arbitrary-child
profile-bank claim.  See
`agent_shield_circuit_cover/DIRECTED_PROFILE_CYCLE_DAG_AUDIT.md`.

Thus `S>=3sigma(log n)loglog n` supplies the required
`n^{sigma loglog n}` scale-recovery multiplier while retaining both the
released base and `F`; it is enough to have `Theta(loglog n)` roles with
polynomial-size endpoint alphabets.  Conversely, if every matching has
size at least `m`, then for every `0<alpha<1` the number of doubly
incompatible pair cells is at least

\[
 \left(q-\frac{S(c,F)}{\alpha\log m}\right)_+(m-m^\alpha). \tag{3az30u}
\]

For `q=Theta(log n)`, `m=n^{Theta(1)}`, and
`S=O((log n)loglog n)`, essentially every actual gap carries essentially
all `m` double circuits.  With detached compatibility these circuits lie
wholly in `F union {v}`.  The scope is essential: old source gaps may
disappear after release, so `(3az30t)` uses the actual released tangent
state.  The remaining promotion tag is exactly whether a target share of
released faces retains this linear family of actual boundary gaps.  See
`agent_common_shield_mixing/MULTIROLE_ENDPOINT_POCKET_TRANSFER.md`.

The double-circuit tensor itself has a polylogarithmic normal form.  For a
detached-bad endpoint `v` against a convex rank-`r` face `F`, its canonical
witness is `v`, one triple of `F`, and the choice of the hidden label.
There are at most `4 binom(r,3)` signed signatures.  Hence every
`m`-edge double-incompatible matching contains a submatching of size

\[
                   \left\lceil\frac{m}{16{r\choose3}^2}\right\rceil
                                                               \tag{3az30v}
\]

with one fixed ordered pair of pocket triples and signed types.  The choice
is made pointwise from `(c,F,role)` and `F` remains in the later output, so
there is no ambient `n^6` name-pigeonhole.  At `r=O(log n)` the loss is only
`O((log n)^6)`.  The residue is therefore one common-cage type (an endpoint
hidden in a fixed pocket triangle) or one rooted-fan type (a fixed pocket
label hidden behind the endpoint and two pocket labels), with both endpoint
marks retained.  Signature counting alone cannot release either realizable
geometry; the next operation must be a common-triple guard release,
cross-role fan product, or cage-to-detached-shield charge.  See
`agent_common_shield_mixing/DOUBLE_ENDPOINT_POCKET_SIGNATURE.md`.

For genuine multiquery histories there is nevertheless an exact coherent
entropy economy.  An `N`-point child queried in `q` fixed ambient directions
has at most

\[
                        O((qN^2)^3)                     \tag{3az30k}
\]

possible chamber itineraries as its single re-embedding varies.  Indeed the
walls `g(w)=d_i` form an arrangement of `q binom(N,2)` hyperplanes in the
three-dimensional projective matrix space.  Thus fixing the whole coherent
`Pi_q` itinerary costs only `O(log N+log q)` bits.  This does not make four
directions independent--cross-ratios remain fixed--but it removes itinerary
entropy as a coefficient-scale loss once one completed copy is localized.
This theorem does **not** couple the independently embedded copies in the
basic branching recursion.

There is also a sharp audit of the narrower **stationary** scheme in which
one completed parent is required to expose all `q` next-ramp chambers.  Let
`Q` have `D` points and suppose, in base-`D` exponents,

\[
 W(Q)\ge D^{q-\epsilon q},\qquad
 W(P)\le D^{q+\epsilon q}.                                \tag{3az30l}
\]

The end-to-end term in `(3az30e)` and the directionwise decoder
`W(Q)+1\le\widehat C_Q(\xi)\widehat U_Q(\xi)` force the assembly cap
profiles of the first and last child copies to differ by at least
`q-2-2\epsilon q-o(1)`.  On the other hand, if the completed parent is to
supply the next ramp at directions `theta_s`, with

\[
 \widehat C_P(\theta_s)\le D^{s+\epsilon q},\qquad
 \widehat U_P(\theta_s)\le D^{q-s+\epsilon q},              \tag{3az30m}
\]

then every child reparameterization `phi_i` is pinned at every calibration
level:

\[
 \log_D\widehat C_Q(\phi_i\theta_s)=s+O(\epsilon q),\qquad
 \log_D\widehat U_Q(\phi_i\theta_s)=q-s+O(\epsilon q).      \tag{3az30n}
\]

In that stationary subclass, a quarter ramp requires `q` projective maps
which agree on `q` calibrated levels but spread across `q-o(q)` levels at
the old assembly direction.  Localizing their assembly width to `o(q)`
gives an end-to-end bank `D^{2q-o(q)}` and hence coefficient `1/2`.
Pairwise or triple profile tests cannot prove that localization: four
explicit source directions and four rational target intervals pass every
three-direction test, while their separated cross-ratio intervals forbid
one projectivity from satisfying all four.  Crossing one critical pair
direction changes each hatted endpoint count by at most a factor two.
These statements are exact but are **not** the final gate for the general
branching construction, which may use different parent copies/types for
the different next-ramp levels.  See
`agent_outer_internal_product/CONTINUUM_PROFILE_COHERENCE_GATE.md`.

Even in that stationary subclass, endpoint variation alone is sharp.  An
exact formal step-profile model has `V=D^q`, mean activity rank `<2q`,
`C(theta)U(theta)=V`, factor-two adjacent changes, and `q` affine
projectivities which agree on every calibrated ramp level but spread across
all `q` assembly levels.  Its cap activity saturates the genuine planar
bound

\[
             \operatorname{TV}C\le2\sum_F|F|=2\mu V.       \tag{3az30o}
\]

The model is not a downward-closed planar face complex, so it is not a
counterconstruction.  It proves that any stationary rigidity theorem must
use subface/circuit coupling rather than only endpoint product, mean rank,
total variation, or cross-ratio coherence.  See
`agent_outer_internal_product/PROJECTIVE_RAMP_ACTIVITY_COUNTERMODEL.md`.

The finite two-direction evidence is stronger than the first scalar audit.
Exhausting all `8^3=512` rooted four-point chirotope words and every one of
their 182 generic reset chambers gives

\[
 \min W=1561,\qquad
 \min_{\xi\ne\xi_0}C_\xi U_\xi=134995,\qquad
 \min_{W=1561,\xi\ne\xi_0}C_\xi U_\xi=157113>100W.    \tag{3az30i}
\]

So the first complete rooted menu does not bootstrap the scalar ramp; this
remains finite evidence, not an all-scale endpoint theorem.  The wrapper is
therefore a rigorous reduction of the loop-heavy branch to one precise
unresolved operation: direction-uniform endpoint energy, a homogeneous
seam-plus-endpoint extraction, or a new bank charged by the linear matching
of mixed seam circuits.  It is not yet a sub-half construction or a
half-coefficient closure.  See
`agent_common_shield_mixing/COMMON_GUARD_PROFILE_RAMP_BARRIER.md`,
`agent_common_shield_mixing/MINIMIZER_COMMON_GUARD_PROFILE_MUTATIONS.md`,
`agent_common_shield_mixing/LOOP_HEAVY_STRONG_GLUE_RESET_AUDIT.md`, and
`agent_root_followup/COMMON_GUARD_ALL_DIRECTION_AUDIT.md`, together with
`agent_shield_circuit_cover/RECHARTED_ALL_LOOP_WRAPPER_GATE.md` for the
two-direction reset state and exact comb identities,
`agent_shield_circuit_cover/DECORATED_TWO_MARK_INVERSION_DICHOTOMY.md` for
`(3az30f2)`--`(3az30f3)`,
`agent_shield_circuit_cover/INVERSION_ENDPOINT_POCKET_SPLICE.md` for the
pocket-labelled mixed-seam decoder,
`agent_outer_internal_product/BRANCHING_PROFILE_QUERY_DEPTH_GATE.md` for
`(3az30f4)` and the exact query ledger,
`agent_outer_internal_product/CONSTRUCTION_CHART_RECYCLING_OBSTRUCTION.md`
for `(3az30f5)`--`(3az30f6)`,
`agent_outer_internal_product/FINITE_GAP_STRONG_COMB_RAMP_BARRIER.md` for
the exact scalar finite-gap barrier `(3az30f7)`--`(3az30f8)`,
`agent_shield_circuit_cover/FIXED_GAP_LINEAR_PROFILE_POTENTIAL.md` for
the exact drop theorem `(3az30f9)`--`(3az30f12)` and coherent-ramp
residue,
`agent_shield_circuit_cover/COHERENT_RAMP_ENDPOINT_MODULE_LOCALIZATION.md`
for the surplus telescope `(3az30f13)`--`(3az30f15)` and rooted endpoint
module `(3az30f16)`--`(3az30f17)`,
`agent_shield_circuit_cover/LINEAR_ENDPOINT_MODULE_ALIGNMENT_BARRIER.md`
for the exact same-chart alignment obstruction `(3az30f18)`--`(3az30f19)`,
`agent_shield_circuit_cover/PATHWISE_PROJECTION_ITINERARY_COMPRESSION_GATE.md`
for the exact itinerary bound `(3az30f20)` and fixed-gap slack barrier
`(3az30f21)`,
`agent_common_shield_mixing/MIXED_SEAM_VERTEX_COVER_PI2_GATE.md` for
`(3az30h)`, and
`agent_common_shield_mixing/BAD_PAIR_RANK4_PIQ_CLASSIFICATION.md` for
the local five-way classification and `(3az30k)`,
`agent_common_shield_mixing/CONVEX_BAD_PAIR_EAR_PROMOTION.md` for
`(3az30j)`, and
`agent_common_shield_mixing/ENDPOINT_POCKET_CODEGREE_DICHOTOMY.md` for
`(3az30p)`--`(3az30s)`, and
`agent_shield_circuit_cover/DETACHED_PAIR_SOURCE_MASK_HALL.md` for the
unconditional Hall bound `(3az30s1)` as well as `(3az30s4)`--`(3az30s5)`,
`(3az30s6)`, and
`agent_outer_internal_product/DETACHED_BASE_ENDPOINT_HALL_STRENGTHENING.md`
for `(3az30s1a)` and the source-by-release core,
`agent_shield_circuit_cover/PAIRWISE_CONVEX_TRIPLE_CIRCUIT_COVER.md` for
`(3az30s1b)`--`(3az30s1c)` and the same-edge release regression,
`agent_shield_circuit_cover/QUADRATIC_TRACE_RECTANGLE_OR_SHIELD.md` for
`(3az30s1d)` and the high-projection trace bank,
`agent_shield_circuit_cover/DETACHED_LOAD_TWO_BANK_AND_GAP_RESET.md` for
`(3az30s2)` and the released-gap regression,
`agent_outer_internal_product/DETACHED_LOAD_SOURCE_EAR_HALL.md` for
`(3az30s3)` and the dense two-sided core,
`agent_common_shield_mixing/MULTIROLE_ENDPOINT_POCKET_TRANSFER.md` for
`(3az30t)`--`(3az30t4)` and `(3az30u)`, and
`agent_outer_internal_product/DENSE_RECTANGLE_ACTUAL_GAP_FAN_GATE.md` for
`(3az30t5)` and the adjacent dominance-chain regression,
`agent_common_shield_mixing/DENSE_HALL_TWO_CLOUD_PROFILE_BARRIER.md` for
`(3az30t6)` and the five-target anti-alignment regression,
`agent_common_shield_mixing/DENSE_HALL_INTERNAL_TRIANGLE_CAUCHY.md` for
`(3az30t6a)` and the internal-bank overlap localization,
`agent_outer_internal_product/FULL_WORD_TRIANGLE_REUSE_SCALE_BARRIER.md`
for `(3az30t6b)` and the stationary common-triangle scale barrier,
`agent_common_shield_mixing/HIGH_TRIANGLE_QUERY_LOCALIZATION_GATE.md` for
`(3az30t6c)` and the dyadically source-compressed fixed-triangle star,
`agent_common_shield_mixing/QUASIPOLY_SOURCE_TRIANGLE_TAG_CLOSURE.md` for
the scale-closing total triangle tag `(3az30t6d)`--`(3az30t6e)`,
`agent_common_shield_mixing/END_TO_END_QUASIPOLY_GATE_AUDIT.md` and
`agent_shield_circuit_cover/SOURCE_TRIANGLE_TAG_APPLICABILITY_AUDIT.md`,
together with
`agent_outer_internal_product/QUASIPOLY_SOURCE_TRIANGLE_TAG_INTEGRATION_AUDIT.md`,
for its exact upstream, physical-cloud, and finite-gap scope,
`agent_common_shield_mixing/WEIGHTED_POSITION_RELEASE_ENTROPY.md` for the
unconditional weighted cover-entropy entrance `(3d3a)`--`(3d3e)`, its
recoverable low-redundancy promotion, and its
marked Reed--Solomon module-extraction barrier,
`agent_outer_internal_product/UNORDERED_COLOUR_LIVE_RELEASE_REFINEMENT.md`
for the sharpened polynomial-loss colouring in `(3d3a)`--`(3d3b)` and its
explicit stop before cyclic seam/profile arguments,
`agent_common_shield_mixing/HIGH_REDUNDANCY_RELEASE_HALL_BARRIER.md` for
the support-reservoir Cauchy/rank-tax bounds `(3d3f)`--`(3d3g)` and the
common-guard overlap tensor `(3d3h)`--`(3d3i)`, together with the live
transfer/excess-rank audit `(3d3j)`--`(3d3l)`,
`agent_outer_internal_product/HIGH_REDUNDANCY_RELEASED_PREFIX_BARRIER.md`
for the redundancy decomposition `(3d3m)`--`(3d3n)`, the intrinsic
physical-label reduction `(3d3o)`--`(3d3p)`, and the released-prefix
counter-regression,
`agent_outer_internal_product/EXCESS_RANK_FIXED_LABEL_DOWNSHADOW_GATE.md`
for the sharp trace-compression tradeoff `(3d3q)`, the full-completion Hall
localization `(3d3r)`--`(3d3s)`, and its non-live equality regression,
`agent_common_shield_mixing/EXCESS_RANK_FOUR_LOCAL_PROJECTION_DICHOTOMY.md`
for unordered role colouring and the four-local/projection split
`(3d3t)`--`(3d3v)`,
`agent_outer_internal_product/LIVE_DENSE_COMPLETION_PROFILE_GATE.md` for
the two-sided live transfer `(3d3w)` and the exact profile interface
`(3d3x)`,
`agent_outer_internal_product/LIVE_CROSS_CIRCUIT_CHRONOLOGY.md` for the
literal circuit peeling `(3d3y)`--`(3d3z)`,
`agent_outer_internal_product/LIVE_ROOT_TRANSVERSAL_ENTROPY_GATE.md` for
the adaptive root-transversal inequalities `(3d3z2)`--`(3d3z4)` and the
symmetric rank threshold `(3d3z4a)`,
`agent_common_shield_mixing/LIVE_PASCAL_COMMON_GUARD_MULTIPLICATION_BARRIER.md`
for the live-normalized all-loop obstruction `(3d3z1)`,
`agent_common_shield_mixing/MINIMIZER_ALL_LOOP_ENDPOINT_POTENTIAL_GATE.md`
for the reflection-minimal profile orientation and cycle potential
`(3d3z5)`--`(3d3z6)`,
`agent_shield_circuit_cover/ALL_LOOP_NONSTRONG_TRANSVERSAL_BARRIER.md`
for the side-respecting strong-glue classification obstruction `(3d3z7)`,
`agent_common_shield_mixing/HIGH_TRANSVERSAL_PASCAL_PREFIX_DAG_BARRIER.md`
for the live high-transversal prefix-DAG obstruction
`(3d3z8)`--`(3d3z9)`,
`agent_shield_circuit_cover/HIGH_TRANSVERSAL_COMMON_POCKET_ENDPOINT_PRODUCT.md`
for the exact nonadjacent-carrier endpoint product and rooted-module
Cauchy saving `(3d3z9a)`--`(3d3z9c)`,
`agent_shield_circuit_cover/MASS_UNIFORM_CARRIER_FRAGMENTATION_GATE.md` for
the exact carrier-itinerary entropy and parity fragmentation barrier
`(3d3z9d)`--`(3d3z9e)`,
`agent_outer_internal_product/ROLE_MONOTONE_MIXED_FACE_FOREST.md` for the
global empty-role decoder and capacity gate `(3d3z10)`--`(3d3z11)`,
`agent_outer_internal_product/ROLE_FOREST_TERMINAL_ENTROPY_SPLIT.md` for
the exact terminal potential, quasipolynomial threshold, and near-complete
all-deletion residue `(3d3z11a)`--`(3d3z11d)`,
`agent_outer_internal_product/EFFECTIVE_BRANCHING_ROLE_FOREST.md` for the
mass-branching refinement `(3d3z11a)`--`(3d3z11c1)` and the exact
unit-weight prefix-star telescope,
`agent_outer_internal_product/EXCESS_RANK_PREFIX_STAR_COHERENCE_GATE.md`
for the support and weighted zero-codegree warnings
`(3d3z11e)`--`(3d3z11f)`,
`agent_outer_internal_product/LIVE_ATOM_FLOOR_ROLE_FOREST_AUDIT.md` for
the preserved raw atom floor, fibrewise telescope, and exact
completion--release cancellation `(3d3z11g)`--`(3d3z11h)`, together with
the qualified root-mass cutoff in
`agent_outer_internal_product/TERMINAL_WEIGHT_FLOOR_EXCESS_RANK_GATE.md`,
`agent_common_shield_mixing/MASS_UNIFORM_SIBLING_EAR_OR_CIRCUIT_GATE.md`
for the dyadic mass-to-count normalization and the physical
ear-or-fixed-edge-circuit split `(3d3z11i)`--`(3d3z11l)`,
`agent_shield_circuit_cover/FIXED_EDGE_CIRCUIT_STAR_SHIELD_TELESCOPE.md`
for the exact same-edge containment DAG and detached shield/carrier
telescope `(3d3z11l1)`--`(3d3z11l3)`,
`agent_shield_circuit_cover/RECOVERABLE_CARRIER_COARSENING_MASK_RUN_GATE.md`
for the decoded rooted-gap product and the near-ambient long-run reduction
`(3d3z11m)`--`(3d3z11q)`,
`agent_common_shield_mixing/LONG_RUN_PAIR_STAR_INCIDENCE_BARRIER.md` for
the local empty-incidence construction `(3d3z11r)`--`(3d3z11s)`, and
`agent_common_shield_mixing/LONG_RUN_LEAST_COUNTEREXAMPLE_REAUDIT.md` for
its global retraction and the abstract nonplanar residue `(3d3z11s1)`,
`agent_common_shield_mixing/PLANAR_CROSS_CLASS_PRODUCT_AND_CAGE_ELIMINATION.md`
for the four-local class product, dense circuit-matching residue, and
fixed-edge endpoint-XOR shield bank `(3d3z11s2)`--`(3d3z11s4)`,
`agent_root_followup/STABLE_CROSS_CIRCUIT_TOURNAMENT_CORE.md` for the
almost-one-side cover, common tournament core, and uniform signed matching
array `(3d3z11s5)`--`(3d3z11s7)`,
`agent_common_shield_mixing/THREE_CLASS_PAIR_CIRCUIT_TRIANGLE_GATE.md` for
the exact pair-node triangle payment and planar partner-reset obstruction
`(3d3z11s8)`--`(3d3z11s9)`,
`agent_many_class_partner_reset/SCALABLE_STRETCHABLE_PARTNER_RESET_AND_FACE_AUDIT.md`
for the full rational many-class partner reset, common-edge nesting, and
ambient Boolean/cross-quadrilateral payment `(3d3z11s9a)`--`(3d3z11s9b)`,
`agent_many_class_partner_reset/LOW_FACE_SUBSTITUTION_AND_STRONG_COMB_RAMP.md`
for arbitrary low-face child substitution, the exact within-class
strong-comb recurrence, and forced endpoint-gradient ramp
`(3d3z11s9c)`--`(3d3z11s9f)`,
`agent_many_class_partner_reset/CODIMENSION_THREE_TANGENT_SOURCE_SHADOW_AUDIT.md`
for the empty full-word shadow, canonical cross-class cup bank, and exact
source-thinning/completion ledger, including the global all-lower cup
`(3d3z11s9g)`--`(3d3z11s9j)`,
`agent_many_class_partner_reset/STRETCHABLE_RESET_LOAD_CHRONOLOGY_DICHOTOMY.md`
for the exact support-inflation/partner-turn ledger, global load-one
five-point release bank, and scalable colorful-gadget synchronization
barrier `(3d3z11s9k)`--`(3d3z11s9m)`,
`agent_many_class_partner_reset/PERFECT_RESET_LEXICOGRAPHIC_ES_COUNTERREGRESSION.md`
for the exact 252-point perfect high-reuse reset and fresh-pair
lexicographic powers; `agent_many_class_partner_reset/ARBITRARY_CHILD_ES_POWER_PROFILE_BELLMAN.md`
for the corrected additive macro ranks, arbitrary-child profile
substitution, and sharp four-state ramp recurrence
`(3d3z11s9n)`--`(3d3z11s9r)`;
`agent_many_class_partner_reset/RECURSIVE_ES_RAMP_HALF_CLOSURE.md`
for the exact grafting closure of every recursively separated ramp, the
nonstationary profile ledger, and sharp half coefficient
`(3d3z11s9s)`--`(3d3z11s9u)`,
`agent_nonstrong_ramp_search/NONSTRONG_FULL_SPECTRUM_FINITE_GRAMMAR_BARRIER.md`
for the exact non-strong eight-point macro, full projection-spectrum
finite-grammar optimum, and sharp two-state coefficient $2/3$
`(3d3z11s9v)`--`(3d3z11s9x)`,
`agent_nonstrong_ramp_search/HINGED_DIAGONAL_FLOOR_LOG.md`
for the universal hinged rank-cell theorem, the sharp prefix-free Kraft
encoding, and the entropy--Perron closure of arbitrary finite variable-arity
transition grammars `(3d3z11s9y)`--`(3d3z11s9z3)`,
`agent_nonstrong_ramp_search/NONSTATIONARY_HOMOGENEOUS_HALF_CLOSURE.md`
for the universal-in-chart homogeneous nonstationary telescope, exact mesh
loss, and the heterogeneous sibling-weight obstruction
`(3d3z11s9z4)`--`(3d3z11s9z7)`,
`agent_nonstrong_ramp_search/HETEROGENEOUS_WEIGHTED_HINGE_BARRIER.md`
for the exact unequal-child martingale, jump-variance and weighted-hinge
defects, the original weighted predecessor/sibling conjecture, and the
stretchable nonstrong entropy-surrogate barrier
`(3d3z11s9z8)`--`(3d3z11s9z11)`,
`agent_nonstrong_ramp_search/WEIGHTED_HINGE_FALSE_SQUARE_SURVIVES.md`
for the exact stretchable refutation of zero defect, the failure of
nested-threshold uncrossing, and the surviving averaged/deterministic
square-mesh targets
`(3d3z11s9z12)`--`(3d3z11s9z15)`,
`agent_outer_internal_product/THREE_CLASS_CIRCUIT_MATCHING_EXTENSION_AND_ANTI_ALIGNMENT.md`
for the canonical third-class extension bank and support anti-alignment
`(3d3z11s10)`,
`agent_shield_circuit_cover/FIRST_INCOHERENT_SIBLING_NESTED_TRIANGLE_BARRIER.md`
for the arbitrary-child nested all-loop array and complete-trace mixing
barrier `(3d3z11s11)`,
`agent_shield_circuit_cover/COLORFUL_PAIR_ENDPOINT_TRANSVERSAL_BARRIER.md`
for the exact endpoint-bit/colorful-cycle kill in the pair-reset order
type,
`agent_common_shield_mixing/NESTED_TRIANGLE_PARTIAL_TRACE_TELESCOPE.md`
for the exact outermost-trace recurrence and recursive six-profile
potential `(3d3z11s12)`--`(3d3z11s14)`,
`agent_outer_internal_product/NESTED_TRIANGLE_LIVE_NORMALIZATION_AUDIT.md`
for the three induced cloud banks, fixed-power normalization gap, and
quadratic ES(5) bank `(3d3z11s15)`--`(3d3z11s17)`,
`agent_shield_circuit_cover/NESTED_TRIANGLE_VERTEX_CLOUD_FIXED_GAP_GATE.md`
for the maximum-layer injection into singleton telescope profiles and the
almost-complete cross-cloud circuit rectangle `(3d3z11s18)`--`(3d3z11s20)`,
`agent_outer_internal_product/DENSE_CLOUD_CROSS_CIRCUIT_DELETION_FOREST.md`
for the load-one unordered-mask decoder and two-label survival threshold
`(3d3z11s21)`--`(3d3z11s22)`,
`agent_shield_circuit_cover/THREE_CLOUD_CYCLIC_PROFILE_AND_PARTNER_BARRIER.md`
for the conditional cyclic surplus bank and the exact nested partner
anti-alignment `(3d3z11s23)`,
`agent_common_shield_mixing/NESTED_TRIANGLE_AGGREGATE_POTENTIAL_RESTART_BARRIER.md`
for the restart inequality, sharp marginal potential, and face-alphabet
triangle-tag failure `(3d3z11s24)`--`(3d3z11s26)`,
`agent_outer_internal_product/THIRD_CLOUD_KK_SINGLETON_TERMINAL_GATE.md`
for the Kruskal--Katona edge-shadow cutoff and the third-cloud terminal
anti-alignment `(3d3z11s27)`--`(3d3z11s29)`,
`agent_outer_internal_product/RANK_HEAVY_GENERALIZED_KK_AND_FOUR_LOCAL_BARRIER.md`
for the quasipolynomial generalized-shadow descent, conditional
constant-rank refinement, and exact nonstretchable four-local scalar
barrier `(3d3z11s29a)`--`(3d3z11s29b)`,
`agent_shield_circuit_cover/ENDPOINT_SURPLUS_BALANCED_SHELL_BARRIER.md`
for the projection-uniform polylogarithmic endpoint-surplus barrier and
its precise detached-shell rank scope `(3d3z11s30)`--`(3d3z11s31)`,
`agent_shield_circuit_cover/RANK_SAFE_ENDPOINT_SURPLUS_GATE.md`
for the exact endpoint-fibre rank bound and the stretchable frozen-chart
Pascal barrier `(3d3z11s31a)`--`(3d3z11s31d)`,
`agent_shield_circuit_cover/PASCAL_STRONG_GLUE_PROJECTION_SPECTRUM_GATE.md`
for the exact Pascal chamber spectrum, reverse-shuffle and separated
formulas, diagonal polynomial barrier, and first-jump common-edge exit
`(3d3z11s31e)`--`(3d3z11s31i)`,
`agent_shield_circuit_cover/PASCAL_WEIGHTED_INVERSION_LEX_SEAM_GATE.md`
for the rational lex-seam prefix banks, dominant-path cap ratio, and
the endpoint-surplus exponent `1.668966...`
`(3d3z11s31j)`--`(3d3z11s31l)`,
`agent_shield_circuit_cover/PASCAL_FERRERS_MINIMAX_ZIPPER_GATE.md`
for the exact Young-lattice wall bottleneck, rooted Pascal tail,
one-rectangle zipper obstruction, and synchronized two-rectangle reset
`(3d3z11s31m)`--`(3d3z11s31r)`,
`agent_shield_circuit_cover/GENERAL_FERRERS_COMPANION_FLOOR_AND_ENDPOINT_BARRIER.md`
for the lower-convex companion floor and sweep peak, harmonic-tail
sufficient condition, and fixed-pair endpoint-spectrum obstruction
`(3d3z11s31s)`--`(3d3z11s31u)`,
`agent_shield_circuit_cover/FIXED_ENDPOINT_PREFIX_PEELING_COMPANION_OR_SHIELD.md`
for the maximum-child prefix telescope, local companion-or-shield gain,
and sharp conditional-mass barrier
`(3d3z11s31u1)`--`(3d3z11s31u4)`,
`agent_shield_circuit_cover/PREFIX_SHIELD_TWO_TARGET_HALL_AGGREGATE_GATE.md`
for the exact two-target Hall aggregate, pathwise decoder, and half-scale
ordered-role barrier
`(3d3z11s31u5)`--`(3d3z11s31u9)`,
`agent_shield_circuit_cover/DOUBLE_BAD_PREFIX_HALL_THRESHOLD_AND_HALF_BARRIER.md`
for the double-circuit harmonic Hall threshold, exact three-target prefix
ledger, and coefficient-half polynomial-load saturation
`(3d3z11s31u10)`--`(3d3z11s31u16)`,
`agent_outer_internal_product/TWO_SIDED_MERGED_DOWNFACE_MAXIMUM_CHILD_GATE.md`
for the exact two-sided rooted-downset product, two-target Hall ledger, and
sharp `Theta((log n)^2)` maximum-child ceiling
`(3d3z11s31u17)`--`(3d3z11s31u21)`,
`agent_outer_internal_product/THIRD_CYCLIC_MERGED_DOWNFACE_HISTORY_LOAD_GATE.md`
for the linear two-profile ceiling, restricted prefix-projection load, and
corrected codimension-three source-shadow bank
`(3d3z11s31u22)`--`(3d3z11s31u26)`,
`agent_root_followup/HISTORY_FAITHFUL_CODIMENSION_THREE_SOURCE_SHADOW.md`
for the independent exact load-eight audit and the source-thin versus
high-completion/history fork `(3d3z11s31u24)`--`(3d3z11s31u26)`,
`agent_common_shield_mixing/CODIM_THREE_ROLE_FOREST_COMPLETION_GATE.md`
for the good-shadow load trichotomy, puncture-extension restore/bad-core
split, and exact prefix-versus-puncture barrier
`(3d3z11s31u27)`--`(3d3z11s31u29)`,
`agent_outer_internal_product/SOURCE_THIN_FOUR_LOCAL_BLOCKER_SHADOW_DICHOTOMY.md`
for the rank-three trace-hypergraph normal form, cover-versus-blocker
shadow inequality, and sharp completion/history loads
`(3d3z11s31u30)`--`(3d3z11s31u33)`,
`agent_common_shield_mixing/PLANAR_SINGLETON_TERMINAL_TWO_CELL_UNIVERSAL_CAGE.md`
for the two-cell terminal localization, dense bad-pair tensor, universal
affine dominance cage, and calibrated high-surplus carrier
`(3d3z11s32)`--`(3d3z11s35)`,
`agent_common_shield_mixing/FIXED_EDGE_CARRIER_ENDPOINT_DILUTION_GATE.md`
for common-edge normalization, the sharp endpoint-density threshold, and
adjacent-vertex release `(3d3z11s36)`--`(3d3z11s38)`,
`agent_outer_internal_product/THREE_CLOUD_COMMON_EDGE_DOMINANCE_TRICHOTOMY.md`
for the exact tangent-order incomparability bank and coherent dominance
cage reduction `(3d3z11s39)`--`(3d3z11s40)`,
`agent_outer_internal_product/FACE_DEPENDENT_EDGE_DISPERSION_BOOLEAN_SHIELD_BARRIER.md`
for the acyclic critically diluted edge-cage regression and its exact
detached Boolean endpoint payment `(3d3z11s41)`--`(3d3z11s42)`,
`agent_common_shield_mixing/CRITICAL_EDGE_DISPERSION_RECHART_LEDGER.md`
for common-root normalization of varying insertion edges, the physical
root/history ledger, and the frozen-chart cap-by-cup regression
`(3d3z11s43)`--`(3d3z11s46)`,
`agent_common_shield_mixing/THREE_ROOT_RECHART_SYNCHRONIZATION_BARRIER.md`
for the exact projective synchronization law, the three-cloud universal
cage, and the two-shield deletion cover
`(3d3z11s46a)`--`(3d3z11s46c)`,
`agent_common_shield_mixing/WEIGHTED_SIDE_DELETION_PROFILE_DESCENT_BARRIER.md`
for the full-side release theorem, exact `3/8` square-root bank, rooted
history load, and first-moment mask barrier
`(3d3z11s46d)`--`(3d3z11s46h)`,
`agent_common_shield_mixing/HIGH_ORDER_DELETION_RUN_ROOTED_RESET_BARRIER.md`
for the complete deletion transform, cyclic-run deficit, erased-alphabet
conservation law, and rooted-state reset
`(3d3z11s46i)`--`(3d3z11s46m)`,
`agent_common_shield_mixing/CANONICAL_SOURCE_ROLE_DELETION_PASCAL_DENSITY_BARRIER.md`
for the polynomial-density canonical Pascal regression, exact all-delete
load cancellation, and parent-upper-bound scope
`(3d3z11s46n)`--`(3d3z11s46q)`,
`agent_outer_internal_product/ACYCLIC_EDGE_DAG_DOWNSHADOW_AND_REUSE_GATE.md`
for the exact endpoint-excluding downshadow decoder, induced endpoint
bank, and stretchable source-reuse cancellation
`(3d3z11s47)`--`(3d3z11s49)`,
`agent_outer_internal_product/SOURCE_REUSE_BALANCED_ONE_ENDED_PROFILE_BARRIER.md`
for the normalized Boolean-source cage and the exact full local-complex
upper bound `(3d3z11s50)`--`(3d3z11s52)`, including the rank-safe
two-face Cauchy loss `(3d3z11s50a)`,
`agent_outer_internal_product/FIXED_RANK_BOOLEAN_SOURCE_MIDSHADOW_GATE.md`
for the fixed-rank middle-bank gain and common-core rank contraction
`(3d3z11s52a)`--`(3d3z11s52c)`,
`agent_outer_internal_product/COMMON_CORE_COMPLETION_PRIVATE_PETAL_TRICHOTOMY.md`
for the private-petal bank, planar four-cover union lift, and bounded-arity
completion-deletion forest `(3d3z11s52d)`--`(3d3z11s52f)`,
`agent_outer_internal_product/PLANAR_RANK_LAYER_SQRT_ANTICONCENTRATION_COUNTEREXAMPLE.md`
for the rational Pascal rank-layer counterexample and exponentially
coherent middle/leaf overlap `(3d3z11s52g)`--`(3d3z11s52i)`,
`agent_outer_internal_product/MINIMIZER_COHERENT_OVERLAP_STRONG_TREE_GATE.md`
for the fixed-gap strong-tree closure and balanced near-half sharpness
`(3d3z11s52j)`--`(3d3z11s52n)`,
`agent_outer_internal_product/ROBUST_WEIGHTED_APPROXIMATE_STRONG_TREE_GATE.md`
for loss-stable approximate seam recurrences, the one-turn Carleson norm,
and the marked-turn-load obstruction
`(3d3z11s52o)`--`(3d3z11s52r)`,
`agent_common_shield_mixing/PARENT_UPPER_ENDPOINT_RESET_THRESHOLD.md`
for the exact parent-upper endpoint surplus, its coefficient-half
threshold, and the polylogarithmic converter gate
`(3d3z11s52s)`--`(3d3z11s52u)`,
`agent_outer_internal_product/MARKED_TURN_MINIMALITY_LOAD_SCALE_GATE.md`
for the support--rank turn-load cap, sharp deletion-mean constants, and
the single-face composable-retag gate
`(3d3z11s52v)`--`(3d3z11s52y)`,
`agent_common_shield_mixing/POLYLOG_CAP_CUP_CONVERTER_MUTATION_GATE.md`
for the quadratic all-pairs load barrier, exact compatible-pair count,
rooted cross-circuit residue, and global bipartition Gibbs inequality
`(3d3z11s52z)`--`(3d3z11s52z2)`,
`agent_outer_internal_product/MARKED_TURN_CIRCUIT_FLIP_MUTATION_GATE.md`
for the coefficientwise adjacent-wall derivative, injective mutated retag,
and minimizer-sign obstruction `(3d3z11s52z3)`--`(3d3z11s52z4)`,
`agent_outer_internal_product/GAP_BUDGETED_REPAIR_ALPHABET_MUTATION_GATE.md`
for the deletion-base one-bit relocation theorem, fixed-gap repair budget,
common-ear singleton repair, and three-chamber Helly obstruction
`(3d3z11s52z5)`--`(3d3z11s52z8)`,
`agent_common_shield_mixing/MINIMIZER_SINGLETON_ENDPOINT_SURPLUS_GATE.md`
for the projection-uniform singleton endpoint moment, wrong-anchor ledger,
Pascal-minimality rejection, and two-anchor circuit/bipartition gate
`(3d3z11s52z9)`--`(3d3z11s52z13)`,
`agent_outer_internal_product/FIXED_ANCHOR_RELOCATION_CANCELLATION_GATE.md`
for exact anchor-mask capacity cancellation, the two-block density ceiling,
and global-minimum one-point extension cells
`(3d3z11s52z14)`--`(3d3z11s52z17)`,
`agent_common_shield_mixing/CHRONOLOGY_ONE_BIT_REPAIR_SPLICE_HELLY_GATE.md`
for the selection--relocation entropy conservation law, the fixed-edge
positive splice, and the dense same-label three-ear Helly residue
`(3d3z11s52z18)`--`(3d3z11s52z21)`,
`agent_outer_internal_product/MINIMIZER_TWO_POINT_EXTENSION_INTERACTION_GATE.md`
for the exact pair-extension Möbius identity, order-two minimizer bound,
second-rank moments, and mixed-Hessian mutation threshold
`(3d3z11s52z22)`--`(3d3z11s52z25)`,
`agent_outer_internal_product/THREE_EAR_MINIMIZER_BARRIER_AND_ORDER_THREE_GATE.md`
for the exact nine-point minimizer Helly cage, its Farkas normal form, and
the order-three mutation/moment gate
`(3d3z11s52z26)`--`(3d3z11s52z29)`,
`agent_common_shield_mixing/TWO_ANCHOR_DOUBLE_CIRCUIT_ELIMINATION_GATE.md`
for the shared-anchor sign classification, load-one two-face decoder, and
partition-minimal ambient barrier
`(3d3z11s52z30)`--`(3d3z11s52z33)`,
`agent_common_shield_mixing/NEARBY_ANCHOR_TANGENT_INTERVAL_ANTIALIGNMENT_GATE.md`
for the exact nearby-anchor interval formula, weighted depth dichotomy,
and scalable far-support anti-alignment
`(3d3z11s52z34)`--`(3d3z11s52z36)`,
`agent_common_shield_mixing/FIXED_CARRIER_THREE_EAR_COLLAPSE_AND_NESTED_CAGE.md`
for literal-carrier Helly collapse, the nested common-repair cage, and the
Farkas-edge/support-density ledger
`(3d3z11s52z37)`--`(3d3z11s52z41)`,
`agent_outer_internal_product/NINE_POINT_EAR_CAGE_VERTICAL_SUBSTITUTION_GATE.md`
for the exact vertical cage recurrence, all-rechart minimizer rejection,
and continuation-bearing live-history threshold
`(3d3z11s52z42)`--`(3d3z11s52z45)`,
`agent_common_shield_mixing/CONTINUATION_BEARING_THREE_EAR_COALESCING_GATE.md`
for the common-role rich-continuation repair collapse, exact Renyi-3
coalescing lemma, and continuation-correlation barrier
`(3d3z11s52z46)`--`(3d3z11s52z47)`,
`agent_common_shield_mixing/RENYI3_CONTINUATION_COLLISION_OR_DENSE_FACE_CORE.md`
for the lossless dense-core pruning, retained Renyi collision count, and
rank-heavy complete-bad normalization barrier
`(3d3z11s52z48)`--`(3d3z11s52z50)`,
`agent_outer_internal_product/OPPOSITE_SINGLETON_RETURN_AND_ROOTED_PROFILE_ANTI_ALIGNMENT_GATE.md`
for the unrooted opposite-profile return and the exact rooted
anti-alignment barrier `(3d3z11s53)`--`(3d3z11s55)`,
`agent_outer_internal_product/NEAR_AMBIENT_PAIR_STAR_DIRECTIONAL_RECTANGLE_BARRIER.md`
for the endpoint square loss, reflection anti-alignment, and restricted
trace bound `(3d3z11t)`--`(3d3z11u)`,
`agent_outer_internal_product/NEAR_AMBIENT_LIVE_CONTEXT_COEFFICIENT_AUDIT.md`
for the global context/projection-load correction and excess-rank box
contradiction `(3d3z11v)`--`(3d3z11x)`,
`agent_outer_internal_product/ITERATED_FEW_RUN_LOAD_PROFILE_GATE.md` for
terminal-mask coalescence, the vertical deficit ledger, and the exact
formal coherent-ramp endpoint `(3d3z11y)`--`(3d3z11z1)`,
`agent_root_followup/MACRO_RUN_PROFILE_SPECTRUM_WIDTH_GATE.md` for the
unconditional first--last width requirement `(3d3z11z2)`--`(3d3z11z3)`
and the exact finite profile-DP rebound,
`agent_outer_internal_product/COHERENT_RAMP_TWO_CHART_BELLMAN_GATE.md` for
the assembly-surplus tax, necessary cross-chamber reset, and exact seam-jet
state `(3d3z11z4)`--`(3d3z11z5)`,
`agent_common_shield_mixing/PROJECTED_SOURCE_CROSS_BRANCH_STORAGE_GATE.md`
for the projected third-face load split and one-chamber recursion
`(3d3z12)`--`(3d3z13)`,
`agent_common_shield_mixing/REALIZED_CHAMBER_CYCLE_OR_FOREST_GATE.md` for
the exact two-ended cycle telescope and acyclic residue
`(3d3z13a)`--`(3d3z13b)`,
`agent_shield_circuit_cover/HEREDITARY_FACE_TAG_CAUCHY_GATE.md` for the
rank-`k` extension `(3az30t6f)` and its sharp face-alphabet barrier,
`agent_shield_circuit_cover/DETACHED_BOOLEAN_SHIELD_CONTEXT_REUSE_GATE.md`
for the shield-load and full-base retention thresholds
`(3az30t6i)`--`(3az30t6j)`,
`agent_outer_internal_product/POLYNOMIAL_DESCRIPTION_LOAD_FACE_ALPHABET_BARRIER.md`
for the label-primitive load theorem `(3az30t6g)`--`(3az30t6h)` and the
released-face exception,
`agent_outer_internal_product/RELEASED_FACE_HALL_LABEL_PRIMITIVE_GATE.md`
for the exact face-bank Hall gate `(3az30t6k)`--`(3az30t6l)` and its dense
face--face regression,
`agent_outer_internal_product/QUADRATIC_BASE_WORD_DETACHED_REUSE_BARRIER.md`
for `(3az30t7)` and the external-history load barrier,
`agent_shield_circuit_cover/ALMOST_FULL_WORD_MIXED_BANK_BARRIER.md` for
the exact failure of almost-full coexistence and the half-word run counts
`(3az30t7a)`--`(3az30t7b)`,
`agent_shield_circuit_cover/CENTRAL_NESTED_CHILD_TWO_SIDED_PRODUCT_BARRIER.md`
for the projectively universal two-sided trace bound
`(3az30t7c)`--`(3az30t7e)`,
`agent_shield_circuit_cover/DIRECTED_PROFILE_CYCLE_DAG_AUDIT.md` for the
corrected one-chamber graph audit `(3az30t8)`,
`agent_common_shield_mixing/DOUBLE_ENDPOINT_POCKET_SIGNATURE.md` for
`(3az30v)`, and
`agent_outer_internal_product/CONTINUUM_PROFILE_COHERENCE_GATE.md` for the
stationary-only audit `(3az30l)`--`(3az30n)`, and
`agent_outer_internal_product/PROJECTIVE_RAMP_ACTIVITY_COUNTERMODEL.md` for
`(3az30o)`, and
`agent_shield_circuit_cover/TWO_DIRECTION_FOUR_POINT_WRAPPER_AUDIT.md` for
`(3az30i)`.  A complementary exact recursive stress in
`agent_root_followup/TWO_LEVEL_RECHART_EXPLORATION.md` builds the optimized
44-point reset from the mutation-minimal 14-point word and a realizable
134-point third level; their finite
normalized coefficients are `0.66515` and `0.66195`.  The decrease is
consistent with the half fixed point, but the second-level spectrum also
shows that a large minimum `CU` does not eliminate highly skewed reset
profiles.  Exhausting the full rooted four-point `(C,U,W)` Pareto menu gives
a better exact 44-point count `747670`, normalized coefficient `0.65465`.
Its whole 1884-chamber spectrum then gives the optimized 134-point count
`11358202734`, whose coefficient rebounds to `0.66900`; admissible gauge
and child-handedness changes move the endpoint spectrum while preserving
the assembly count.  This independently confirms that one favorable finite
reset is not a recursive state.  See
`agent_shield_circuit_cover/PARETO_TWO_LEVEL_RECURSIVE_MENU.md`.
An exact-sign sampled continuation now probes that 134-point parent in 448
distinct certified half-turn orders (894 profiles including reversals).
The sampled fourth-level optimum is

\[
 W_{4,\mathrm{sample}}=204331272672794,
 \qquad {\log W_{4,\mathrm{sample}}\over(\log404)^2}
          =0.634137803896\ldots .
\]

All \(\binom{134}{3}\) signs and every retained projection order are
certified exactly; floating point proposes directions only.  This is a
gauge-specific sampled upper bound, not an exhausted spectrum or an
asymptotic construction theorem.  See
`agent_root_followup/LEVEL4_SAMPLED_SPECTRUM_EVIDENCE.md`.

For the graded version let `v_r(P)` be the number of convex `r`-subsets and

\[
 p_r(P)=\frac{(r+1)v_{r+1}(P)}{(n-r)v_r(P)}.
\]

It is enough to prove, uniformly for
`r<=(1-o(1))log n`,

\[
 p_r(P)\geq2^{-r-o(r)}.                                      \tag{RE}
\]

Indeed `p_r` is the ratio of consecutive normalized densities
`v_r/binom(n,r)`, so multiplying (RE) gives (2).  In boundary notation

\[
 B_r=(n-r)v_r-(r+1)v_{r+1},
\]

the same target is

\[
 B_r\leq(2^{r+o(r)}-1)(r+1)v_{r+1}.                         \tag{4}
\]

Balanced Pascal and vertical towers approach exponent one in (RE), so the
target is sharp rather than an artifact of the proof.

## 3. Exact deletion-path / information formulation

In this section logs are natural.  Put `h=1/2`,

\[
 \mu_t(S)=tZ'_S(t)/Z_S(t),\qquad
 q_t(p\mid S)=\frac{Z_{S-p}(t)}{(m-\mu_t(S))Z_S(t)}.
\]

For the deletion path driven by `q_h`, define

\[
 X=\sum_{S\text{ on path}}
 \log\frac{|S|-\mu_h(S)}{|S|-\mu_1(S)}.
\]

The exact identities proved in `agent_integrated_activity/REPORT.md` are

\[
 \log\frac{Z_P(1)}{Z_P(h)}
 =\mathbb E_hX+D(\mathbb P_h\Vert\mathbb P_1),               \tag{5}
\]

and

\[
 X=\sum_S\int_h^1
 \frac{\operatorname{Var}_t|A|}{|S|-\mu_t(S)}\,d\log t.
\]

The formerly proposed finite strengthening

\[
 \mathbb E_hX\geq\log(n/2)                                  \tag{IDP}
\]

would imply `H(P)<=2` and close the problem.  It is equivalent to the
information-contraction inequality

\[
 D(\mathbb P_h\Vert\mathbb P_1)\leq\log(2/H(P)).             \tag{6}
\]

The exact 58-point configuration with `H(P)>2` now refutes this finite
constant-two form as well: since the KL term in (5) is nonnegative,
`E_hX<=log(Z(1)/Z(h))<log(n/2)`.  Earlier exhaustive tests through seven
points and exact tests through 30 points passed it, explaining why it was a
useful discovery target.  The asymptotic statement

\[
                    \mathbb E_hX\ge(1-o(1))\log n            \tag{IDP*}
\]

remains sufficient and open; it gives `H(P)=n^{o(1)}`.  A pointwise,
every-deletion-order version is already false at 24 and 30 points, so the
expectation in (IDP*) is essential.  A one-state shortcut is also false: on
central Pascal cells `mu_1-mu_(1/2)` tends to zero.  The necessary
compensation is genuinely multiscale.

There is a complementary exact product-measure formulation.  For a convex
face `A`, put `q(A)=|P\setminus conv(A)|`, and let `mu,qbar` be the uniform
face averages of `|A|,q(A)`.  The Bernoulli hull partition and relative
entropy give

\[
 \log_2V=(\mu+\bar q)H_2\!\left({\mu\over\mu+\bar q}\right)
       -D_2(\pi_{\rm unif}\Vert\rho_{\mu/(\mu+\bar q)}).       \tag{6a}
\]

In particular

\[
 \bar q\ge \mu\left(2^{(\log_2V)/\mu}/e-1\right).             \tag{6b}
\]

Combined with the banked coefficient-`1/4` lower bound, (6b) proves that a
low-mean hard state already has the exterior-label supply demanded by the
rankwise Hall reduction; scalar supply is not the missing step.  The same
Bernoulli law has the exact factorial-toggle identity

\[
 \mathbb E_p{O\choose j}=\left({1-p\over p}\right)^j
      \mathbb E_p{H\choose j}+B_j(p),                         \tag{6c}
\]

where `B_j` counts jointly bad omitted clusters.  At `p=1/2`, every defect
contains a relative rooted cluster of size at most four, and the size-four
term is genuinely necessary on a triangle plus one interior point.  Thus an
alternative IDP proof may target the exponentially weighted reuse of rooted
clusters of sizes two through four; first moments or pair-only potentials
cannot suffice.  These identities and exact audits are in
`agent_idp_mean_fresh/PRODUCT_HULL_ENTROPY.md`.

The minimal-root version is sharper.  Over every nonempty closed state, an
inclusion-minimal bad exterior cluster has size at most three; size four
occurs only over the empty state and is exactly a planar four-circuit.  The
positive defect cover is

\[
 \Delta(P)\le\sum_A\sum_{M\in\mathcal M_A}2^{-(|A|+|M|)},     \tag{6d}
\]

while the exact defect is the signed Boolean-Mobius expansion over unions of
the minimal roots.  This does not yield a scalar estimate: a realizable
nested fan has only two-label roots, local defect tending to its maximum,
and exponentially large absolute Mobius mass whose cancellations are
essential.  The empty-state term itself contains the original convex-subset
count.  Hence (6d) reduces the alternative route to a *cross-state*
bounded-reuse theorem; a local root-size bound is circular.  See
`agent_rooted_cluster_weight/ROOTED_CLUSTER_WEIGHT.md`.

## 4. Antimatroid--Tutte formulation

Let `G` be the shelling antimatroid of `P`.  Feasible sets are complements of
closed sets.  If `F=P-C`, its continuation set is exactly
`Gamma(F)=ext(C)`.  Gordon's antimatroid Tutte polynomial therefore gives

\[
 \boxed{Z_P(s)=f_G(s,s^{-1}-1)}.                              \tag{7}
\]

Equivalently,

\[
 Z_P(1/2)=2^{-n}\sum_{S\subseteq P}2^{r_G(S)}.
\]

Thus the finite half-weight conjecture is the planar-shelling inequality

\[
 \boxed{n f_G(1/2,1)\leq2f_G(1,0)}.                          \tag{8}
\]

This exact bridge is verified in `agent_inverse_pair_hw`.  Universal
antimatroid identities cannot prove (8): atomistic Caratheodory-three
abstract convex geometries fail it.  Scalar deletion--contraction cannot
prove it either: a certified planar nine-point parent satisfies (8), while
each of three rooted deletion minors violates it (`H=56/27`).  Any Tutte
proof must keep a bivariate potential through rooted minors and use the
cyclic minimal-feasible-set structure special to planar general position.

## 5. Rooted-circuit / hard-core formulation

Convex subsets are exactly the independent sets of the 4-uniform hypergraph
whose edges are nonconvex quadruples, each rooted at the unique point lying
inside the triangle of the other three.  Hence `Z_P` is a hard-core
partition function of a rank-three rooted-circuit hypergraph.

Generic 4-uniform methods are insufficient.  There are explicit 4-flag
complexes with the complete 3-skeleton, the sharp first-repair bound, and an
Erdős--Szekeres-sized face along every member of a deletion chain, but with
bounded deletion-path activity and with (RE) false.  The proof must use
rank-three circuit elimination/common-endpoint overlap, not merely edge size,
Caratheodory number, or the local repair degree.

The exact planar first-switch theorem is already available.  If `S` is
nonconvex and `|S|>=5`, at most three deletions make `S` convex.  With
`b(A)` the number of blocked points and `u(A)` the number of addable points,
this gives

\[
 (r-1)B_{r+1}\leq
 \sum_{|A|=r,\ A\text{ convex}}b(A)u(A)
 \leq(r+1)B_{r+1}.                                           \tag{9}
\]

Thus all nonmaximal transport is near-regular.  The sole missing part of
(4) is a rank-preserving reset for maximal faces `u(A)=0`.

## 6. The maximal-pocket reset: current sharp gate

The desired statement can be phrased as follows.

> **Tagged maximal-pocket reset (target).**  A blocked/maximal convex
> `r`-face can be transported to an `(r+1)`-face, or to an equivalent amount
> of already-counted global convex mass, using an `r`-bit geometric tag and
> only `2^o(r)` additional inverse histories.

Together with (9), this target proves (4), hence (2).

There is now an exact classification of every repair incidence.  Let `S` be
nonconvex, let `x` be a point for which `A=S-x` is convex, and put
`B=ext(S)` and `I=S-B`.  If `x` is interior, then `I={x}`.  If `x` is a
hull vertex, all points of `I` lie in the open ear at `x`, and in the cyclic
order of `A` they form one consecutive interval replacing `x`; the
complementary interval is `B-x`.  Conversely every such ear replacement is
a repair.  Thus a blocked addition to a convex `r`-gon hides only one cyclic
interval, whose combinatorial tag is its two endpoints (`O(log r)` bits).
The exact graded interior/ear census is proved and checked in
`agent_low_v_structure/NESTED_REPAIR.md`.

This does **not** make the reset finite-state.  An arbitrary planar order
type can be shrunk into a single replacement cone while every one of its
points has the same hidden interval.  The remaining fibre is therefore the
full problem recursively, with two tangent endpoints retained.  The sharp
state is a two-tangent cone/pocket partition function, not merely the two
interval endpoints.

A second genuinely planar input controls the extension side.  For a convex
face `A`, its addable points split among the cyclic edge pockets.  If two
points lie in pockets whose edges are neither equal nor adjacent, then both
can be added simultaneously.  Writing `m_i` for pocket populations,
`u=sum m_i`, and

\[
 M=\max_i(m_{i-1}+m_i+m_{i+1}),
\]

the rank-two link count satisfies

\[
 f_2(\operatorname{link}A)\geq \frac{u(u-M)}2.              \tag{11}
\]

After double counting, (11) says that a bad ratio between two consecutive
`p_r`'s forces extension mass, in the size-biased sense, into three adjacent
tangent pockets.  A pointwise curvature claim is nevertheless false on
fixed-template vertical towers: periodic bad three-rank blocks occur with
positive density.  The live target is therefore a **block-smoothed**
inequality in which repeated three-pocket concentration either recurses in
the retained two-tangent state or is paid by a later good block.

The tempting edge-pocket factorization is **false**.  Individually addable
points do split according to the edge of `A` that they replace, but choices
in two different original edge cones can interfere after both are inserted.
An exact five-point counterexample is

```text
(0,-83154), (1,56327), (2,28007), (3,67474), (4,-91970).
```

For the convex triangle `A={0,2,4}`, point 1 individually replaces edge
`(2,0)` and point 3 individually replaces edge `(4,2)`.  Both one-point
extensions are convex, whereas `A+{1,3}` is not (its hull omits point 2).
All ten determinants are nonzero.  Thus a valid reset must dynamically update
tangencies after every insertion; static pockets are not independent.  This
is the same nonlaminarity phenomenon seen in `agent_pocket_restart`.

The universal complex identity

\[
 Z_P(x+y)=\sum_{A\text{ convex}}x^{|A|}
 Z_{\operatorname{link}(A)}(y),                              \tag{10}
\]

remains exact, but the link needs a dynamic tangent state rather than a
product over the edges of the initial polygon.

An attractive induction interface for the half-weight formulation is exact
but **false as a universal step**.  For a hull vertex `e`, write

\[
 Z_P(s)=Z_{P-e}(s)+sR_e(s),
\]

where `R_e` is the link polynomial of faces containing `e` with `e`
removed.  If

\[
 2Z_{P-e}(1/2)+nR_e(1/2)\leq4R_e(1),                         \tag{RA}
\]

then `H(P-e)<=2` implies `H(P)<=2`.  Small exhaustive tests suggested that
some hull vertex might always satisfy (RA), and the analogous whole-onion
increment `Phi(P)>=Phi(P-hull(P))`, with
`Phi(P)=2Z_P(1)-|P|Z_P(1/2)`, also survived those tests.  Both statements are
false.  There is an exact rational 63-point example consisting of sixty
inner points in convex position inside a large outer triangle for which all
three hull vertices fail (RA) and the onion inequality fails by a factor
`2.8559...`.  A 131-point skinny wrapper around a sharp recursive core gives
the same failure by exact recurrences.  Each outer anchor sees only a
one-sided tangent-chain family, whereas the inner configuration has much
larger unrooted half-weight.  The global half-weight inequality itself has
enormous slack on these examples.  Consequently no scalar hull/onion
potential can supply the reset.

The RA algebra works for deletion of **any** point, not just a hull vertex.
This first suggested the following existential statement:

\[
 \boxed{\text{some }e\in P\text{ has }
 2Z_{P-e}(1/2)+nR_e(1/2)\leq4R_e(1).}               \tag{ERA}
\]

Indeed (ERA) would say that
`Phi(P)>=Phi(P-e)` for `Phi(P)=2Z_P(1)-nZ_P(1/2)`; induction from the empty
set then proves `Phi>=0`, i.e. `H<=2`.

Averaging the margins in (ERA) produces the stronger linear rank inequality

\[
 \boxed{nZ_P(1/2)+\frac{n-1}{2}Z'_P(1/2)\leq2Z'_P(1).}       \tag{APA}
\]

Equivalently (APA) says that `Phi` is superharmonic under uniform deletion.
In ranks, (APA) is

\[
 \sum_k v_k\left[2k-\bigl(n+(n-1)k\bigr)2^{-k}\right]\geq0. \tag{15}
\]

The stronger average is **false even for a stretchable planar set**.  The
exact rational 44-point certificate in `agent_apa_rank` has profile

\[
 (1,44,946,13244,70450,99093,43597,8726,1075,53)
\]

and violates (APA) by `912395/512`; all 13,244 determinants are nonzero.
The half-weight target itself still has slack (`H=1.88599...`), and 21 of
the 44 individual points satisfy (ERA).  But (ERA), the deepest-onion repair,
and the finite conjecture `H<=2` are all false as well.  The exact rational
58-point certificate in `agent_apa_rank` has

\[
 H(P)=\frac{33994061}{16990512}=2.0007673106\ldots>2.
\]

Every one of its 58 deletion children has `H<2`, every individual (ERA)
margin is negative, and its unique deepest onion point fails too.  All
30,856 determinants and all child profiles are checked exactly.  The gadget
does not amplify under ordinary homogeneous vertical composition: its `H`
drops to `0.02769...` at depth two and then rapidly to zero.

The surviving deletion route must therefore allow small local peaks.  A
particularly clean sufficient target is the **activity compensation
property**

\[
 \boxed{H(P)\,[1-(\mu_1-\mu_{1/2})]_+\le C}              \tag{ACP}
\]

for an absolute constant `C` (all current exact data satisfy `C=1`).  The
exact deletion identity gives

\[
 \max_e H(P-e)\ge H(P)\frac{n-1}{n}
       \frac{n-\mu_{1/2}}{n-\mu_1}.
\]

Since a uniform face of any downset has `mu_1<=n/2`, (ACP) implies
`H(P)<=max_e H(P-e)+2C/n`; iteration gives `H(P)=O(log n)=n^{o(1)}` and
hence the full coefficient-one-half lower bound.  More generally it is
enough to prove a nondecreasing `C_n=n^{o(1)}` in the generalized deletion
condition

\[
 C_nV_e\ge Z_P(1/2)+(n-1)W_e
\]

for some point `e`.  These compensated statements, not a monotone constant-2
potential, are the current live induction targets.

There is now an exact information-theoretic reduction of (ACP).  If
`q_1(r)=v_r/Z(1)`, `q_h(r)=2^{-r}v_r/Z(1/2)`, and
`m=log_2(n/H)`, then

\[
 D_2(q_1\Vert q_h)=\mu_1-m,\qquad
 D_2(q_h\Vert q_1)=m-\mu_{1/2}.
\]

Their sum is `delta=mu_1-mu_(1/2)`, and the elementary inequality
`2^delta(1-delta)<=1` on `0<=delta<=1` gives

\[
 \boxed{H[1-\delta]_+\le 2^{\log_2 n-\mu_1}.}          \tag{16}
\]

Thus the full problem follows already from the restricted **peak mean
bound**

\[
 \mu_1(P)\ge \log_2n-O(\log\log n)
\]

for positive-growth maximizers of `H`.  At such a maximizer the deletion
inequalities themselves imply `delta<1`, so (16) applies exactly where it is
needed.  Generic antimatroid, shellability, Cohen--Macaulay, and hull-interval
identities cannot prove this: the simple Caratheodory-three geometry has the
complete rank-three skeleton and violates (ACP) by order `n`.

Passing to a **global restriction record** does give a complete scalar
hierarchy, but it does not improve the exponent.  If `H(Q)<=H(P)` for every
nonempty `Q subseteq P`, put

\[
 \Psi(a)=\log {Z(a)\over Z(a/2)}.
\]

Bernoulli restrictions and activity monotonicity give, for every `0<a<=1`,

\[
 0\le \Psi(1)-\Psi(a)
 \le-\log\left(a+(1-a){\mu_{a/2}\over n}\right),          \tag{16a}
\]

while averaging over every fixed restriction size gives the strictly
stronger factorial-moment family

\[
 {\mathbb E_{q}(n-K)_d\over\mathbb E_{p}(n-K)_d}
       \le {n\over n-d}\qquad(1\le d<n),                  \tag{16b}
\]

where `p` is the uniform face law and `q` its `2^{-K}` tilt.  In particular

\[
 \mu_{1/2}\le\log_2(n/H)\le\mu_1\le\mu_{1/2}+1.          \tag{16c}
\]

Combining this hierarchy with the known coefficient-`1/4` count theorem
recovers only `H<=n^{3/4+o(1)}`.  This scalar ceiling is sharp: complete rank
truncations at rank `(1/4+o(1))log_2 n`, after choosing the restriction that
maximizes `H`, satisfy the entire hierarchy and the correct count scale but
still have `H=n^{3/4+o(1)}` and `mu_1-mu_{1/2}=o(1)`.  They are not planar;
their role is to prove that no combination of scalar restriction curvature,
factorial moments, and the existing count lower bound can close the problem.
A quantitative planar repair theorem is indispensable.  See
`agent_restriction_peak_curvature/REPORT.md`.

Using the entire large-rank profile of every random restriction does not
bypass this shelf.  If `t=n^alpha` and every `t`-restriction has
`2^{(c-o(1))(log t)^2}` faces in ranks at least `lambda log t`, exact
hypergeometric lifting gives

\[
 {\log V(P)\over(\log n)^2}
 \ge c\alpha^2+\lambda\alpha(1-\alpha)-o(1).            \tag{16d}
\]

At `c=1/4`, this improves the quarter coefficient if and only if
`lambda>1/2`; the optimized gain is

\[
 {\lambda^2\over4(\lambda-1/4)}-{1\over4}
 ={(\lambda-1/2)^2\over4(\lambda-1/4)}.                \tag{16e}
\]

The full Erdős--Szekeres rank profile is exactly invariant under this lift:
at internal relative rank `theta`, with `y=alpha theta`, its exponent is

\[
 \alpha^2\theta(1-\theta)
 +\alpha(1-\alpha)\theta=y(1-y)\le {1\over4}.           \tag{16f}
\]

Summing all logarithmically many ranks or inserting further restriction
scales only telescopes the same binomial factors.  Current mean/width input
places the mass near `(1/4)log t`, a factor two below the strict threshold
in `(16e)`.  Thus any sampling improvement requires a genuinely planar
rank-repair/product theorem, not more careful use of the known profile.
See
`agent_common_shield_mixing/TWO_SCALE_FULL_RANK_SAMPLING_BARRIER.md`.

There is nevertheless a different, genuinely planar rank lift which avoids
asking for a large **fraction** of the ambient face law at high rank.  Fix any
pocket `X`, put `Y=P\X`, `N=|Y|`, and choose `t<=N`.  If `ES(r)<=t`, double
counting an ordinary rank-`r` witness in every `t`-subset of `Y` gives the
absolute bank

\[
 v_r(P[Y])\ge {\binom Nr\over\binom tr}\ge(N/t)^r.       \tag{16g}
\]

This is not the hypergeometric lift `(16d)`: the bank is physically disjoint
from the already chosen pocket and is then tested against the pocket face
bank.  Write `|X|=2^{L-delta}` and choose
`t=2^{L-Delta}`, where

\[
 delta+e_L+\log L=o(Delta),\qquad Delta=o(L),             \tag{16h}
\]

and `e_L=o(L)` is the inverse Erdős--Szekeres error.  Then some
`r=(1-o(1))L` satisfies `ES(r)<=t`, and `(16g)` gives

\[
 \log_2K\ge(1-o(1))LDelta.                                \tag{16i}
\]

Least-counterexample induction in `X` therefore yields, for
`F_C(n)=2^{L^2/2-CL\log L}`,

\[
              K\,V(P[X])
       \ge F_C(n)\,2^{(1-o(1))LDelta}.                    \tag{16j}
\]

The slack choice `(16h)` absorbs the unknown quantitative rate in
`ES(r)=2^{r+o(r)}` as well as every polynomial and `2^{O(L\log L)}`
decoder loss.  Conversely, the exact all-restrictions scalar LP really
cannot produce this conclusion: the complete shelf

\[
 v_k=\binom nk\mathbf1_{k\le r},\qquad
 \mathbb E_{|S|=m}V(P[S])=\sum_{k\le r}\binom mk,          \tag{16k}
\]

meets every coefficient-`1/2` restriction target with cutoff
`r=L/2-(C-1/2)\log L+O(1)`.  Thus `(16g)` is exactly the additional planar
input missing from the scalar hierarchy.

Pigeonholing oriented boundary edges loses only `n^2`: a subbank
`A_e` of at least `rK/[N(N-1)]` sources shares one literal exposed edge and
side.  Since source and pocket grounds are disjoint, every ordinary union
`A union F`, `A in A_e`, `F in F(P[X])`, decodes the pair.  Under the
counterexample upper bound, `(16j)` forces the good-pair density to be at
most

\[
 {G\over |A_e|V(P[X])}
       \le2^{-(1-o(1))LDelta}.                           \tag{16l}
\]

Almost every pair therefore contains a canonical crossing planar
four-circuit of type `1+3`, `2+2`, or `3+1`, while retaining the
rank-`(1-o(1))L` source, pocket face, and common exposed edge.  This is a
sharp reduction, not closure: an exact rational anti-aligned two-cloud cage
has `15 x 35=525` bad rank-`4` by rank-`3` pairs sharing one exposed edge.
Its two internal Boolean banks pay globally, so the remaining operation is
precisely a minimizer/internal-bank charge of this dense fixed-edge circuit
rectangle.  See
`agent_common_shield_mixing/INDUCED_SUBSET_HIGH_RANK_POCKET_LIFT_GATE.md`.

Quantitative same-type extraction independently supplies the right
lower-order **absolute** scale.  Partition into `m=ES(k)` equal parts,
apply the planar Bukh--Vasileuski same-type lemma, and keep a convex
`k`-subset of the representative type.  For
`k=alpha log_2 log_2 n` the retained block size satisfies

\[
 s\ge {n\over(\log n)^{5\alpha+o(1)}},\qquad
 V(P)\ge(1+s)^k-1
   =n^{\alpha\log_2\log_2n-o(\log\log n)}.             \tag{16m}
\]

Thus quantitative same-type loss is not the scale obstruction.  The exact
conditional pocket splice is also immediate: if every `F in F_c` coexists
with every transversal of disjoint blocks `Z_{c,i}`, then, with actual
global output load `Lambda`,

\[
 V(P)\ge {1\over\Lambda}
   \sum_c|\mathcal F_c|\prod_i(1+|Z_{c,i}|).           \tag{16n}
\]

But same-type controls triples from three distinct blocks, whereas pocket
coexistence needs signs with two pocket labels.  This is a genuine gap, not
a decoder issue.  An exact rational construction has a convex 14-point
pocket (`16,383` nonempty faces) and three 3-point role clouds: all
`14*3^3=378` singleton transversals have one convex type, yet every pocket
trace of rank at least three is bad with every label of one guard block.
Only `1+14+binom(14,2)=106` pocket traces can coexist, so the formal
`442,341` product incidences collapse to at most `2,862` mixed outputs.
The obstruction persists under additional small same-type role clouds.

Polynomial-fraction mutually avoiding blocks likewise force every selected
`2+2` trace to be ordinary, but not the full union of the two
transversals.  Hence both tools recover `(16m)` but do not replace the
crossing-circuit/minimizer charge after `(16l)`.  The missing quantitative
hypothesis is **anchored same-type** control of the two-pocket-label signs.
See
`agent_outer_internal_product/SAME_TYPE_POSITIVE_FRACTION_POCKET_COEXISTENCE_GATE.md`.

Once rooted good density is present, the anchored promotion is quantitative.
Let `F` have rank `r`, let `e` be one exposed edge, and let
`X_1,...,X_k` be ordered role sets in its ear cell.  If an `epsilon`
fraction of full transversals make `F` together with the transversal
ordinary in the prescribed cyclic order, the Fox--Pach--Suk box theorem
gives `Z_i subseteq X_i` with

\[
 { |Z_i|\over|X_i|}
   \ge {\epsilon^3\over3^{40k}t^2},
 \qquad t\le(r+k)^2.                                \tag{16o}
\]

All partial `Z`-transversals coexist with `F`.  Thus for
`k=alpha log_2log_2n`, `r=O(log n)`, role size
`n/(log n)^B`, and `epsilon>=(log n)^{-C}`, the rooted one-face bank is

\[
          \prod_i(1+|Z_i|)
       =n^{\alpha\log_2\log_2n-o(\log\log n)}.        \tag{16p}
\]

For varying roots the exact weighted statement is

\[
 V(P)\ge {1\over\Lambda}
       \sum_cw_c\prod_i(1+|Z_{c,i}|),                 \tag{16q}
\]

where `Lambda` is the actual rooted-output load; no context disjointness is
assumed.

The positive-density premise is sharp.  A rational fixed triangle `B`
and consecutive role clouds in one ear cell have constant **full rooted
order type**, every singleton `B+x` ordinary, every external
subtransversal ordinary, but `B+S` bad for every `|S|>=2`.  Each bad pair
uses the same fixed-edge `1+3` circuit.  The external support is a convex
chain and contributes its Boolean bank, so this is exactly the paid
zero-density branch of `(16l)`, not a live counterexample.  Hence the
remaining interface has no hidden semialgebraic loss: it is positive rooted
density, closed by `(16o)`--`(16q)`, versus a homogeneous fixed-edge circuit
cage whose absolute support/downshadow bank must be charged with bounded
history.  See
`agent_outer_internal_product/ROOT_AWARE_FIXED_EDGE_SEMIALGEBRAIC_EXTRACTION_GATE.md`.

The homogeneous bad rectangle has an exact deletion normal form.  For a
source--pocket pair `(A,F)`, let `T_Y(A,F)` be the hypergraph of source
traces of all bad crossing four-sets.  Its edges have rank at most three,
and for every `G subseteq A`, planar four-locality gives

\[
 (A\setminus G)\cup F\text{ ordinary}
 \quad\Longleftrightarrow\quad
 G\text{ hits every }T\in\mathcal T_Y(A,F).            \tag{16r}
\]

Therefore the number of literal pairs whose source transversal number is
at most `d` obeys the injective decoder bound

\[
 \#\{(A,F):\tau_Y(A,F)\le d\}
      \le S_d(n)V(P),
 \qquad S_d(n)=\sum_{i\le d}\binom ni.                 \tag{16s}
\]

The output is `(A-G) union F`; it retains the entire pocket face, and the
at most `d` deleted physical labels recover `A`.  Weighted histories add
only the genuine same-`(A,F)` multiplicity.  Allowing deletion on both
sides gives the same bound.

For `F` nonempty and `d<|A|`, these outputs are genuinely mixed, so `V(P)`
in `(16s)` can be replaced exactly by

\[
 V_{\rm mix}=V(P)-V(P[Y])-V(P[X])+1.                  \tag{16s1}
\]

This does use both internal banks rather than charging the ambient total
again.  But at a pocket size `p=n/L^A`, least-counterexample induction and
the parent upper bound save only

\[
 -\log_2{V_{\rm mix}\over F_C(n)}
      \le (A-1)\log_2L+O_C(1),                       \tag{16s2}
\]

whereas the live deficit is `Theta(L log L)`.  Thus subtracting the two
induced banks is exact but does not supply the missing multiplier.

Apply this to the live bank
`|A||H|>=F_C(n)2^{sigma LDelta}` and take
`d=floor(sigma Delta/2)`.  All but a
`2^{-(sigma/2-o(1))LDelta}` fraction of the rectangle then have

\[
 \nu_Y>{\sigma\Delta\over6}-O(1),
 \qquad
 \nu_\times>{\sigma\Delta\over8}-O(1),                \tag{16t}
\]

where `nu_Y` is a source-disjoint rank-three trace matching and
`nu_x` a fully vertex-disjoint crossing-circuit matching.  At most two
members meet the common exposed edge, so every hard pair retains a rooted
toggle bank of size `2^{Omega(Delta)}`.

This last bank is quantitatively insufficient.  At
`Delta=Theta(log L)` it is only polynomial in `L`, while the deficit is
`2^{Theta(L log L)}`; naming `Theta(Delta)` physical circuits costs
`n^{4Theta(Delta)}` and consumes exactly the available slack.  The
anti-aligned parabola realizes the sharp local extreme:

\[
 \tau_Y(A,F)=|A|,\qquad
 \tau_\times(A,F)=|A|+|F|-\max\{|A|,|F|,4\},          \tag{16u}
\]

so only full source deletion releases a rank-at-least-three pocket face.
Its two Boolean clouds pay globally.  Hence the fixed-edge residue is now
precise: prove that concentrating the `Omega(Delta)` disjoint trace
matchings in a low-face planar family forces a
`2^{Omega(LDelta)}` support/downshadow shield, or a rooted positive-density
box already handled by `(16o)`--`(16q)`.  Bare toggles and rank-only
Kruskal--Katona lose the needed factor `L`.  See
`agent_common_shield_mixing/HIGH_RANK_FIXED_EDGE_CIRCUIT_DELETION_MATCHING_GATE.md`.

The disjoint-trace matching itself has a sharp global information ceiling.
If a weighted record carries `s` disjoint source traces of rank at most
three and total record weight over any one actual source is at most `rho`,
then all trace-toggle downfaces satisfy

\[
2^s\sum_\omega w_\omega
       \le \rho S_{3s}(n)V(P).                         \tag{16v}
\]

For fixed rank-`r` sources the exact rank-refined form is

\[
 2^s\sum_\omega w_\omega
  \le\rho\sum_{q=r-3s}^{r}\binom{n-q}{r-q}v_q(P).     \tag{16v1}
\]

At `r=O(L),s=Theta(Delta)` its largest coefficient still costs
`2^{Theta(LDelta)}`, so no rank averaging is hidden in the ceiling.

For a complete source by pocket rectangle, `rho` is exactly the pocket
degree, so it cancels from `(16v)`.  This is not a loose decoder: changing
membership only on the matched trace support gives at most

\[
                         2^{3s}                       \tag{16w}
\]

states per retained source.  With `s=Theta(Delta)`, this has logarithm
`O(Delta)`, not the required `Theta(LDelta)`.

There is one exact promotion.  Suppose ordinary completions `B union U`
over a common retained `B` four-cover a support `Q`, meaning every
rank-at-most-four subset of `Q` lies in some completion trace `U`.
Four-locality then makes `B union Q` ordinary, so all `2^{|Q|}` rooted
subfaces are ordinary.  With actual global output load `Lambda_4`,

\[
             \sum_cw_c2^{|Q_c|}\le\Lambda_4V(P).      \tag{16x}
\]

This reaches the fixed-gap scale only for a recoverable common support of
rank `Theta(LDelta)`; one matching has rank only `O(Delta)`.

The ceiling is stretchably realized at live normalization by the central
Pascal cell: source and pocket alphabets are both `V(P)n^{-O(1)}`, every
source singleton is a trace, a polynomial-loss source subfamily shares one
exposed edge, yet every nonempty source downface is incompatible with every
selected pocket face.  All toggles are reused inside the one left-child
bank and only full source deletion releases the pocket.  Its coefficient
`1-1/(4\ln2)>1/2` means it is not a counterexample parent.  Thus the exact
remaining operation is now a minimizer-specific profile mutation, or a
cross-history theorem assembling the `O(Delta)` local traces into the
`Theta(LDelta)` four-cover support of `(16x)`.  No refinement of the same
local matching enumeration can do this.  See
`agent_outer_internal_product/DISJOINT_TRACE_GLOBAL_SUPPORT_CHARGE_GATE.md`.

This stability obstruction persists arbitrarily close to the half boundary
from above.  For fixed substitution depth $D$, balanced Pascal
self-substitution has coefficient

\[
 \beta_D={1\over2}+{\beta-1/2\over D}+o_k(1),
 \qquad \beta=1-{1\over4\ln2},                         \tag{16x1}
\]

and its top face layer is within $2^{O_D(L\log L)}$ of the full face
count.  After common directed-edge localization and rank projection, one
retains rank $L-O(\log L)$ sources on a literal edge $uv$ with only this
lower-order loss.  A smaller top-layer Pascal pocket of entropy
$B L\log L$, with $B$ above the localization constant, then gives

\[
 { |\mathcal A|\,|\mathcal H|\over V(P)}
          \ge 2^{\Omega(L\log L)}.                    \tag{16x2}
\]

Nevertheless every source--pocket pair has singleton traces at every
source label and $\Omega(\log L)$ fully vertex-disjoint physical $1+3$
circuits.  Thus rank, common-edge localization, four-locality,
Kruskal--Katona, and disjoint circuit matching together still do not force
the missing converter, even at the equality boundary.  The example has
$\beta_D>1/2$, so it does not evade the strict parent upper; it proves that
the remaining step must use that upper in a genuinely minimizer-specific
profile mutation:

\[
 \boxed{\text{local fixed-edge stability alone cannot close }(16x).}
                                                               \tag{16x3}
\]

See
`agent_common_shield_mixing/PASCAL_TOP_LAYER_LIVE_FIXED_EDGE_STABILITY_BARRIER.md`.

Global minimality does rule out the two stored stationary calibrations once
the all-delete state is a **literal strong seam**.  If $P=A\prec B$, write
`W_A,C_A,U_A` and `W_B,C_B,U_B` for the two face/cap/cup profiles.  Replacing
one child while retaining the other shows that `A` and `B` minimize the
weighted functionals

\[
 {\cal J}_A(Q)=V(Q)+U_BC(Q),\qquad
 {\cal J}_B(R)=V(R)+C_AU(R).                           \tag{16y}
\]

This is strictly stronger than separate child minimality.  Summing the two
canonical singleton restorations of every deleted child label gives, with
the evident face-rank means and endpoint-rank moments,

\[
\begin{aligned}
 \mu_AW_A+U_BM_C(A)
   &\le(1+U_B)\{a+aC_A-M_C(A)\},\\
 \mu_AW_A+U_BM_C(A)
   &\le a+aU_A-M_U(A)+U_Ba^2,\\
 \mu_BW_B+C_AM_U(B)
   &\le(1+C_A)\{b+bU_B-M_U(B)\},\\
 \mu_BW_B+C_AM_U(B)
   &\le b+bC_B-M_C(B)+C_Ab^2.                         \tag{16z}
\end{aligned}
\]

In particular

\[
 U_A\ge{\mu_AW_A-a-U_Ba^2\over a},\qquad
 C_B\ge{\mu_BW_B-b-C_Ab^2\over b}.                   \tag{16z1}
\]

These inequalities eliminate the exact integral scalar equality family
behind the parent endpoint-reset bound for every advertised parameter
`m>=3`.  They also eliminate the exact rational central `T(6,3)` Pascal
all-delete seam: a literal singleton reembedding in one child decreases the
parent by between `1,041` and `1,818` faces.  Thus the Pascal state in the
preceding paragraph is an exact interface barrier, but it is not stationary
under the weighted child mutations required of a global minimizer.

When the facing profiles `C_A,U_B` are small, `(16z1)` forces the opposite
mixed bank `U_AC_B` to be large.  Double reflection exposes it in another
configuration, at the exact wall cost

\[
             \Delta_{\rm wall}=U_AC_B-C_AU_B.          \tag{16z2}
\]

If `Delta_wall<F_C(n)-V(P)`, that reflected configuration is still a
counterexample and the induction restarts with the large mixed bank.  The
remaining literal-seam state is therefore exact: a decreasing weighted
child mutation, a near-wall profile reset, or a high-wall/one-sided endpoint
skew.  The parent upper bound does not itself control the slack against
`Delta_wall`; pulling the opposite bank back through a high wall is the next
minimizer-specific operation.  See
`agent_outer_internal_product/STATIONARY_ALL_DELETE_WEIGHTED_PROFILE_MUTATION_GATE.md`.

The literal-seam variational residue admits a sharper exact reduction.  For
an $a$-point order type in a generic chart define

\[
 g_C(a,t)=\min_Q\{V(Q)+tC(Q)\},\qquad
 p(a)=\min\{C_\theta(Q):V(Q)=f(a)\}.                  \tag{16z3}
\]

If a globally minimal seam $P=A\prec B$ has child sizes $a,b$, simultaneous
weighted child optimality gives

\[
 \begin{aligned}
 C_A&\le p(a),& V(A)-f(a)&\le U_B\{p(a)-C_A\},\\
 U_B&\le p(b),& V(B)-f(b)&\le C_A\{p(b)-U_B\}.
 \end{aligned}                                        \tag{16z4}
\]

Thus the high-wall branch is controlled by the directional endpoint
profile of actual ordinary-face minimizers, not by an arbitrary scalar
profile.  The obvious large-penalty regime is nevertheless exponentially
too remote.  With $\ell_a=a+\binom a2$, the all-cup chain becomes the unique
minimizer of $g_C(a,t)$ only beyond

\[
 T_a=\max_{C(Q)>\ell_a}{2^a-1-V(Q)\over C(Q)-\ell_a},
 \qquad 2^{a-3}-1\le T_a\le2^a-1-f(a).                \tag{16z5}
\]

The lower bound is realized by a stretchable one-flip parabola, so this
exponential transition is sharp up to a factor eight.  In the live
near-ambient slice $a\gg L^2$ while the available penalty is at most
$V(P)=2^{O(L^2)}$, hence it cannot reach `(16z5)`.  Finally, if
$V(Q)<H$ and $k=\lceil\log(H+1)\rceil$, planar cap-triple covering gives

\[
 C(Q)\ge \ell_a+
 \left\lceil{\binom a3\over\binom k3}\right\rceil,     \tag{16z6}
\]

but for near-ambient children this improves the seam product only to
polynomial scale.  The remaining literal-seam input is therefore an
asymptotic curvature theorem for $p(a)$, or a physical mutation that crosses
the high wall without paying the full endpoint transition:

\[
 \boxed{\text{control }p(a)\text{ on ordinary-face minimizers.}}\tag{16z7}
\]

See
`agent_outer_internal_product/WEIGHTED_CAP_ENVELOPE_EXPONENTIAL_TRANSITION_GATE.md`.

The strict-parent/equality-stability audit now closes one apparent escape but
also fixes the exact scale of the residue.  The finite Pascal live rectangle
above violates its necessary weighted singleton inequality by a factor
exceeding $2^{716}$; the same is true asymptotically for every fixed-depth
Pascal version.  Hence those examples lie on the genuinely
$V$-decreasing child-mutation branch.  However, strictness of the parent
upper supplies no positive integer wall budget: a boundary counterexample
with $V=T-1$ is destroyed by a mutation of cost one:

\[
 \boxed{\text{strict parent upper gives no positive wall budget.}}\tag{16z8}
\]

If every weighted singleton child mutation is nondecreasing, the full
rank-moment inequalities do force an actual facing bank in the current
chart:

\[
 C_AU_B\ge {1\over4}\max\left\{{\mu_AW_A\over a},
                              {\mu_BW_B\over b}\right\}.    \tag{16z9}
\]

At the balanced coefficient-half scale this is only the parent target times
$L^{K+O(1)}/n^2$, rather than inverse-polylogarithmic density.  An exact
integral scalar survivor satisfies the parent upper, reflection minimality,
endpoint factorization, all four moment inequalities, and the envelope
comparison, while attaining `(16z9)` within a factor $16$ and placing the
opposite bank behind an exponential wall.  Thus the $n^2$ loss is sharp for
the present scalar interface, not an artifact of discarding moments.

The all-delete history obstruction is equally exact.  For a Cartesian
record family $\mathcal A\times\mathcal H$ releasing $H$, every released
face has load $|\mathcal A|$, so division leaves exactly $|\mathcal H|$.
In the finite Pascal ledger the record surplus over the parent has $325$
bits, but the useful history-load deficit exceeds $559$ bits.  Meanwhile
the stored affine gauge of the true nine-point minimizer has no contiguous
literal seam among the $72$ tested affine chambers and $576$ cuts.  This
does **not** exclude a projectively recharted hull-root seam; `(16z18)` below
shows that three such singleton roots exist.  Beside any sibling of size at
least four its all-cup replacement decreases the weighted child objective by
at least $27$.  The surviving theorem is therefore genuinely geometric:

\[
 \boxed{\begin{gathered}
 \text{exclude the scalar Pareto profile for realizable minimizers, or}\\
 \text{convert part of the opposite bank while retaining source history.}
 \end{gathered}}                                             \tag{16z10}
\]

See
`agent_strict_parent_profile_rigidity/STRICT_PARENT_PROFILE_RIGIDITY_GATE.md`.

The endpoint-value part can in fact be solved exactly, and it is not the
obstruction.  Let $m_a(N)$ be the least total cardinality of $N$ distinct
nonempty subsets of an $a$-set.  Summed singleton minimality for an ordinary
minimizer and a chart attaining $p(a)$ gives

\[
 m_a(f(a))+m_a(p(a))\le a\{1+p(a)\}.                 \tag{16z11}
\]

If $f(a)=2^{c(\log a)^2+o((\log a)^2)}$ and $r$ is the first Boolean rank
with $\sum_{j\le r}\binom aj\ge f(a)$, inversion of `(16z11)` yields

\[
 r=(c+o(1))\log a,\qquad
 p(a)\ge(1-o(1)){r f(a)\over a}.                       \tag{16z12}
\]

At the inductive half scale this ordinary-minimizer endpoint product is far
larger than the target.  The genuine high-wall parameter is instead the
Pareto deficit

\[
 \Phi_a(c)=\min_{Q,\theta:C_\theta(Q)\le c}{V(Q)-f(a)\}.
\]

For a literal seam of child sizes $a,b$, the exact scalar closure condition
is the **coupled** envelope inequality

\[
 \min_{\substack{\ell_a\le c\le p(a)\\
                  \ell_b\le u\le p(b)}}
 \{\Phi_a(c)+\Phi_b(u)+cu\}
 \ge F(a+b)-f(a)-f(b).                                  \tag{16z13}
\]

This coupling cannot be replaced by a tangent bound at the ordinary
minimizer.  Exhaustive exact reflection-order scans give

\[
 (V,C)=(113,55),(114,53)\qquad(n=8),                   \tag{16z14}
\]

so for every seam penalty $t\ge1$ the second configuration improves the
weighted child objective by $1-2t<0$.  A stretchable nine-point witness is
even flatter: $(168,82)$ in the stored minimizer versus $(169,76)$ in a
competitor, giving $1-6t<0$.  Higher-order deletion/Mobius and restriction
defect inequalities improve the value bound `(16z12)` only polynomially and
do not control this neighboring configuration's geometry.  Thus `(16z7)`
is superseded precisely by `(16z13)`: prove integrated two-child Pareto
curvature, or use a physical mutation which changes the seam.

Nor can the flat-front competitors be sent back to the solved recursive
template class.  Exhaustive recursion over every leaf order and both mirror
signs at every split proves

\[
 \boxed{(114,53)\text{ and }(169,76)
        \text{ are genuinely nonstrong order types}.}        \tag{16z15}
\]

The searches use respectively $109600$ and $986409$ cached ordered states.
Thus any proof of `(16z13)` must act directly on a nonstrong Pareto frontier;
strong-tree closure is unavailable without a new promotion theorem.

The complete two-child attack shows that even the integrated Pareto
inequality supplies no further universal curvature.  With the exact profile
cost

\[
 \psi_a(c)=\min_{Q,\theta:C_\theta(Q)=c}\{V(Q)-f(a)\},
 \qquad \Phi_a(c)=\min_{d\le c}\psi_a(d),
\]

the minimum over **physical** literal strong glues of child sizes $a,b$ is

\[
 S_{a,b}=f(a)+f(b)+K_{a,b},\qquad
 K_{a,b}=\min_{c,u}\{\Phi_a(c)+\Phi_b(u)+cu\}.        \tag{16z16}
\]

Therefore the only universal absolute floor is

\[
             K_{a,b}\ge f(a+b)-f(a)-f(b),             \tag{16z17}
\]

which is circular for the desired induction and is equality whenever a
global minimizer occurs in the seam class.  There is no hidden mixed
curvature: for $H(c,u)=\Phi_a(c)+\Phi_b(u)+cu$,

\[
 \Delta_c\Delta_uH=(c_0-c_1)(u_0-u_1).               \tag{16z18}
\]

The finite equality is exact and geometrically revealing.  Exhausting all
$1{,}232{,}944$ eight-point reflection-order commutation classes gives

\[
 K_{8,1}=54\text{ at }(V,C)=(114,53),\qquad
 S_{8,1}=113+1+54=168=f(9).                            \tag{16z19}
\]

Each of the three hull vertices of the stored true nine-point minimizer,
after its own projective radial rechart, deletes to precisely that nonstrong
eight-point child.  Thus the parent minimum **selects** the flat frontier;
the earlier affine-cut audit did not see these root charts.  At two
eight-point children the exact seam optimum moves farther left,
$K_{8,8}=1580$, uniquely at two $(255,36)$ profiles, and has total $1806$.
An explicit nonstrong nine-point profile $(172,71)$ beats both displayed
$(168,82)$ and $(169,76)$ profiles beside every integer sibling penalty
$t\ge1$.  Hence arbitrary two-child replacement is exhausted as an
operation: the next input must control a one-child frontier across changing
projective root charts, or mutate outside the literal seam.  See
`agent_coupled_pareto_two_anchor/COUPLED_PARETO_TWO_ANCHOR_GATE.md`.

That one-child frontier has an exact global recurrence.  For a generic
directional chart $\theta$ of an $n$-point realization $Q$, let
$C_\theta(Q)$ be its nonempty cap count.  Deleting a hull vertex and sending
one of its support lines to infinity, and conversely adding a sufficiently
remote singleton in any prescribed chart, give

\[
 \boxed{f(n+1)=1+\min_{|Q|=n,\theta}
                  \{V(Q)+C_\theta(Q)\}.}                \tag{16z20}
\]

Thus, with

\[
 K_{n,1}:=\min_{|Q|=n,\theta}
       \{V(Q)-f(n)+C_\theta(Q)\},                       \tag{16z21}
\]

one has the exact identities

\[
 f(n+1)=f(n)+1+K_{n,1},\qquad
 \log f(N)=\sum_{n<N}\log\!\left(1+{1+K_{n,1}\over f(n)}\right).
                                                               \tag{16z22}
\]

Consequently coefficient one half is exactly the cumulative
Pareto-curvature gate

\[
 \sum_{n<N}\log\!\left(1+{1+K_{n,1}\over f(n)}\right)
 \ge\left({1\over2}-o(1)\right)(\log N)^2.             \tag{16z23}
\]

The sharp pointwise sufficient condition is

\[
 \boxed{K_{n,1}\ge(1-o(1)){\log n\over n}f(n),}         \tag{16z24}
\]

and it is enough for failures to have total
$\sum(\log n)/n=o((\log N)^2)$.  This condition is deliberately not
asserted to be equivalent pointwise.

The hinged Kraft theorem does not itself prove `(16z24)`.  In one chart it
does imply the exact Hölder product

\[
 C_\theta(Q)U_\theta(Q)\kappa_\theta(Q)\ge n^3,
 \qquad
 \kappa_\theta(Q)=\sum_i2^{-\alpha_i-\beta_i}\le1,     \tag{16z25}
\]

but along an extreme shelling flag the dynamic is only

\[
                  V(P_N)=N+\sum_{n<N}C_{\theta_n}(P_n). \tag{16z26}
\]

A scalar profile with $C_n=U_n=\binom{n+1}{2}$ and
$V_n=n+\binom{n+1}{3}$ satisfies the recurrence, endpoint floors, and all
of `(16z25)` for $n\ge20$, yet has only polynomial growth.  The obstruction
is genuinely cross-chart: the exact nine-point minimizer has $6{,}984$
extreme shellings and three equally cheap top root charts, while the same
physical label changes hinged responsibility from $(\alpha,\beta)=(3,1)$
to $(1,3)$.  Arbitrary finite fresh-chart scripts are also stretchably
realizable by successive affine recharting and remote root insertion.
Therefore the exact remaining input at this interface is a chart-coherence
theorem carrying hinged responsibility between roots, or a
shelling-multiplicity decoder turning alternative flags into disjoint faces;
the recurrence plus chartwise Kraft stops at the polynomial barrier.  See
`agent_hull_root_envelope_dynamic/HULL_ROOT_ENVELOPE_AND_CHART_RESET_GATE.md`.

The first half of that alternative does have a universal projective root
code.  If $H(P)$ is the hull of a state $P$, $θ_z$ is the radial chart of
$P-z$, and

\[
 h_z=\max_i\{\alpha_z(i)+\beta_z(i)\},
 \qquad \lambda(P,z)=h_z+\mathbf 1_{\{|P|\le3\}},
\]

then

\[
 \boxed{\sum_{z\in H(P)}2^{-\lambda(P,z)}\le1.}       \tag{16z27}
\]

Indeed, if $r=|H(P)|\ge4$, the other $r-1$ hull vertices form a cap in
the $z$-chart, so $h_z\ge r-2$ and $r2^{-(r-2)}\le1$; the triangle and
bottom states follow from hinged Kraft and the one-bit correction.  The
codes therefore concatenate down the entire extreme-shelling tree:

\[
 \sum_{\sigma\in\mathcal S(P)}
 2^{-\sum_{(A,z)\in\sigma}\lambda(A,z)}\le1.          \tag{16z28}
\]

This is nevertheless exactly the wrong namespace for the inner hinged
symbols.  Writing
$\kappa_z=\sum_i2^{-\alpha_z(i)-\beta_z(i)}$, the unprefixed union law
$\sum_z\kappa_z\le1$ is false: its value is $33/16$ for the true
nine-point minimizer, $1419/256$ for the canonical 36-point Pascal square,
and exactly $m$ for a convex $m$-gon.  Thus the chart prefix must pay the
root entropy.

More decisively, the natural decoder loses *all* shelling entropy.  Give
labelled shellings arbitrary weights $w_\sigma$, put
$W=\sum_\sigma w_\sigma$, and let $\mu(A,z)$ be the total weight of
shellings using transition $A\to A-z$.  The first deleted point of any
non-singleton face $F$ is unique, and root--cap bijection gives the exact
weighted identities

\[
 \boxed{\sum_{(A,z):\,F\subseteq A,\ z\in F}\mu(A,z)=W,}
 \qquad
 \boxed{\sum_{(A,z)}\mu(A,z)C(A,z)=W(V(P)-|P|).}       \tag{16z29}
\]

Every decoded ordinary face therefore has fibre exactly the *total*
shelling weight, for every reweighting.  For uniform weights the true
nine-point minimizer has $6{,}984$ shellings and every one of its 159
non-singleton faces has fibre $6{,}984$.

For an $(n+1)$-point minimizer, put
$C_z=C_{\theta_z}(P-z)$ and use
$V(P-z)-f(n)+C_z=K_{n,1}$.  Combining `(16z27)` with the hinged product
gives only

\[
 \sum_{z\in H(P)}
 {1\over C_z(f(n)+K_{n,1}-C_z)}\le1,
 \qquad
 K_{n,1}(f(n)+K_{n,1})\ge|H(P)|.                       \tag{16z30}
\]

This is weaker than the universal polynomial endpoint floor.  Hence the
cross-chart gate is now exact: construct genuinely new labels after a root
choice, or remap cap symbols to ordinary faces with fibre
$o(W)$ by the amount demanded in `(16z24)`.  Any decoder whose only output
is the canonical face $S\cup\{z\}$ is closed.  See
`agent_shelling_multiplicity_decoder/ROOT_CHART_KRAFT_AND_SHELLING_COLLISION.md`.

In fact no remapping of a positive fraction of the *full* tagged ledger can
do better.  The ledger has weighted mass $W(V(P)-n)$.  Any
mass-preserving deterministic, randomized, future-aware, or globally
optimized map into the $V(P)$ ordinary faces therefore has

\[
 \boxed{\max_G L(G)\ge W{V(P)-n\over V(P)}
 \ge W\left(1-{6\over n^2+5}\right).}                 \tag{16z31}
\]

If only non-singleton outputs are used, the lower bound is exactly $W$ and
the canonical decoder attains it.  More generally, retaining a fraction
$\rho$ of the ledger forces

\[
 \max_G L(G)\ge\rho W{V(P)-n\over V(P)}.               \tag{16z32}
\]

Thus fibre $o(W)$ requires discarding $1-o(1)$ of the tagged mass.
Additional future roots, boundedly many transition labels, endpoint
replacement, randomization, and cap--cup metadata cannot alter this
single-face capacity bound.

Exact integral max-flow on the strongest one-next-label menu confirms that
the obstruction is capacity rather than a poor local rule:

\[
\begin{array}{c|c|c|c}
P&\text{unrestricted floor}&\text{menu optimum}&W\\ \hline
\text{true }n=9&6610&6633&6984\\
T_{4,2}&296&298&336\\
\text{convex }n=8&39056&39178&40320.
\end{array}                                             \tag{16z33}
\]

For the 36-point Pascal square every ordinary-face remapping has load
greater than $0.999918W$.  Consequently the shelling branch has only one
remaining form: select an $o(1)$ fraction of exceptionally valuable tags
and prove that this sparse subledger still carries the full curvature in
(16z23).  Total shelling remapping, even noncanonical and omniscient, is
closed.  See
`agent_post_collision_remapping/POST_COLLISION_REMAPPING_MINIMAX.md`.

The exceptional subledger can itself be isolated exactly.  For an
\(m\)-point state \(A\), put \(E(A)=V(A)-f(m)\).  Every extreme deletion
\(A\to A-z\) obeys the conservation law
\[
 \boxed{E(A-z)+C(A,z)=K_{m-1,1}+E(A).}                 \tag{16z34}
\]
Consequently every shelling ledger has a causal bottom-up partition into
curvature layers \(K_{1,1},\ldots,K_{N-1,1}\), plus residual \(E(P)\).
For an \(N\)-point minimizer the top layer is an exact
\[
                 {K_{N-1,1}\over f(N)-N}              \tag{16z35}
\]
fraction of the ledger.  Thus the desired scale in (16z24) really does
concentrate all current curvature into an \(o(1)\)-mass subledger.

The canonical sparse decoder nevertheless still collides.  If the first
root is \(z\), write
\[
 C_z=C(P,z),\qquad D_z=V(P-z)-f(N-1).
\]
Minimality and (16z34) give \(C_z+D_z=K_{N-1,1}\), so the top layer is
forced to include every current root-cap tag.  In particular the hull face
occurs in every shelling and has fibre exactly \(W\).  Quantitatively, if a
causal selection retains \(1-\eta\) of the top curvature with maximum
canonical load \(\varepsilon W\), then
\[
 \boxed{\sum_z{W_z\over W}{C_z\over K_{N-1,1}}
 \le\eta+\varepsilon{\sum_zC_z\over K_{N-1,1}}
 \le\eta+\varepsilon|H(P)|.}                           \tag{16z36}
\]
Hence a near-capacity low-fibre proof must obtain \(1-o(1)\) of its
curvature from child excess \(D_z\), unless it supplies a genuinely new
geometric decoder.  The complementary high-hull branch is already paid:
\[
                     K_{N-1,1}\ge2^{|H(P)|-1}-1.        \tag{16z37}
\]
Exact max-flow gives native optimum \(W\) on the true nine-point minimizer,
\(131W/336\) on \(T_{4,2}\), and only \(2117W/64560\) on a highly
nonminimal vertical Pascal square, sharply exhibiting the child-excess
escape.  See
`agent_sparse_curvature_transport/SPARSE_CURVATURE_TRANSPORT_AND_NATIVE_COLLISION.md`.

See
`agent_minimizer_endpoint_curvature/MINIMIZER_ENDPOINT_CURVATURE_AND_HIGH_WALL_GATE.md`.

The first-switch theorem also gives a concrete finite Hall target.  Let

\[
 N_r=\#\{A:\ |A|=r,\ A\text{ convex},\ u(A)\le4(r+1)\},\qquad
 \ell=\lceil\log_2n\rceil.
\]

Rank-summing the switch inequality shows that, at activities `1` and `1/2`,
the entire blocked boundary is within a constant factor of this
`O(r)`-extension class.  A separate cover calculation proves that

\[
 \boxed{\sum_{r<\ell}(\ell-r)N_r\le C_nV(P)}          \tag{17}
\]

implies
`mu_1>=log_2 n-2C_n-1/2`.  Consequently a uniform `C_n=O(log log n)`
in (17) closes Erdős 838, and a constant closes it with constant ACP.  This
is the sharpest current formulation of the missing geometry: a weighted
Hall/injection theorem for low-rank faces with only `O(r)` available outer
continuations.  All diffuse and high-extension boundary mass has already
been paid for.

There is a convenient rankwise form.  If, for `g>=1`,

\[
 N_{\ell-g}\le K_n2^{-g}V(P),                              \tag{18}
\]

then splitting the sum in (17) at
`g=2 ceil(log_2(2K_n))` gives `C_n=O(log K_n)`.  Hence the
apparently much weaker allowance `K_n=(log n)^O(1)` is already sufficient:
polynomial congestion in the relevant rank costs only `O(log log n)` in the
mean.  Exact searches kill the normalization `K_n<=1` (a rational
24-point set has ratio `2679/2516`), but find no scalable growth; central,
guarded, and iterated vertical families drive the ratio rapidly downward.

The top rank window is automatic and must be removed from the geometric
discussion.  If `r=ell-o(ell)`, the selected cap itself is
`d=2^(ell-r)=n^o(1)`.  Sending each selected repair record back to its source
face has congestion at most `d`.  More generally, on an arbitrary repair
tree the first-divergence weights telescope, and ordered record pairs sent
to their ordered source-face pair have total fibre at most `d^2`; hence

\[
             \sum_s w_s\le d^2V(P)^2.                         \tag{18a}
\]

This uses no planarity and shows that full-history insertion-chain barriers
are irrelevant in the top window: they repeatedly reuse the same source
states far beyond the allowed cap.  A genuinely hard capped slice must have
linear codimension `ell-r=Omega(ell)`.  Here and below *near-maximal* means
low addable degree, not rank near `ell`.  The exact telescope and exhaustive
audit are in `agent_capped_guard_release/CAPPED_GUARD_RELEASE.md`.

The hard branch has three further proved structural properties.

1. If `delta<1`, the uniform face rank `K` has absolute width:
   `Pr(K<=mu_1-s)<2^(1-s)` and
   `E|K-mu_1|<2+2/ln 2<4.886`.  Thus a counterexample to the peak-mean
   bound has a constant fraction of all faces in `O(1)` ranks and in the
   low-extension class above.
2. Every blocked pair `(A,p)`, `|A|=r`, has at least `2^(r/2)` local convex
   targets containing `p`: take the larger side of a line through an
   interior blocker, or the larger Boolean side of the exact exterior-ear
   replacement.  Local target capacity is therefore ample; simultaneous
   overlap is the issue.
3. The full activity form of the Boolean hull partition is considerably
   stronger than its value at `p=1/2`.  If `S` is any family of rank-`r`
   faces and

   ```text
   q(A)=|P\setminus conv(A)|=u(A)+e(A),
   ```

   then, for every `0<p<1`,

   \[
    \boxed{|S|p^r(1-p)^{\mathbb E_Sq(A)}\le1.}       \tag{19}
   \]

   Indeed the exact hull-event partition is

   \[
    \sum_{A\text{ convex}}p^{|A|}(1-p)^{q(A)}=1,
   \]

   and Jensen applied to the subfamily gives (19).  Optimizing at
   `p=r/(r+qbar)` yields

   \[
    \log_2|S|\le(r+\bar q)H_2\!\left({r\over r+\bar q}\right).
                                                               \tag{20}
   \]

   Consequently, if `log_2|S|>=(c-o(1))L^2` and
   `r<=(alpha+o(1))L`, then

   \[
    \bar q\ge n^{c/\alpha-o(1)}.                    \tag{21}
   \]

   In the present hard branch `c>=1/4`, `alpha<=1`, and `u=O(r)`, so a
   typical low-extension face has on average

   \[
   \boxed{\mathbb E_Se(A)\ge n^{1/4-o(1)}}.         \tag{22}
   \]

   More importantly, at the actual RNP rank `r=(alpha+o(1))L` and with
   `log_2|S|>=(c-o(1))L^2`, the estimate (21) already meets the Hall demand:

   \[
    {c\over\alpha}\ge1-\alpha
    \quad\text{whenever }c\ge\tfrac14,              \tag{22a}
   \]

   because `alpha(1-alpha)<=1/4`.  Hence

   \[
    \mathbb E_Se(A)\ge n^{1-\alpha-o(1)}
      =2^{g-o(L)}.                                  \tag{22b}
   \]

   Thus the hard sources already possess essentially the full number of
   exterior labels required by RNP; the remaining theorem is a congestion
   bound after selecting only the required number of repair incidences from
   each source.

   This has a pointwise tail form, not only an average form.  Using the
   quantitative Erdős--Szekeres error, there is `K_0=n^{o(1)}` such that
   the low-label family

   \[
    \{A\in N_r:q(A)\le2^g/K_0\}
   \]

   already has size at most `n^{o(1)}V/2^g`.  Every unresolved source has
   at least `2^g/n^{o(1)}` exterior blocked labels.  Consequently the
   exterior-incidence capacity bound

   \[
    \boxed{|​\{(A,p):A\text{ unresolved},\ p\text{ exterior blocked}​\}|
           \le n^{o(1)}V(P).}                       \tag{EIC}
   \]

   is a clean sufficient statement: `(EIC)` proves RNP, the peak-mean
   theorem, and the full lower coefficient `1/2`.  It is not equivalent to
   RNP and can be much stronger than necessary.  The actual remaining target
   is the **capped exterior Hall problem**: choose only
   `2^g/n^{o(1)}` exterior blockers above each unresolved source and route
   those selected incidences with `n^{o(1)}` congestion to convex target
   faces.  The optimized label-supply proof and exact tail audit are in
   `agent_cyclic_stem_hw/OPTIMIZED_HULL_ACTIVITY.md`.

   Even capped `n^{o(1)}` congestion is stronger than necessary.  It is
   enough to save **any fixed power** over source projection.  More
   precisely, suppose that for some absolute `epsilon>0`, every simple
   selected exterior-repair family of rank `Theta(log n)` and left cap `h`
   satisfies

   \[
                 |E|\le n^{o(1)}h^{1-\epsilon}V(P).         \tag{EIC'}
   \]

   At a positive-growth peak with a fixed linear mean deficit, the rank-width
   theorem supplies `cV` low-addable sources in one rank
   `r=mu_1+O(1)`.  The optimized hull tail removes only `o(V)` of them and
   leaves

   \[
                h=2^{\ell-r}/n^{o(1)}=n^{\delta+o(1)}
   \]

   exterior labels above every remaining source.  Selecting exactly `h`
   gives both `|E|>=(c-o(1))hV` and `(EIC')`, contradicting
   `h^epsilon=n^{epsilon delta+o(1)}`.  Hence no fixed mean deficit exists,
   so `mu_1=(1-o(1))log n` and ACP closes the problem.  This reduction and a
   complete shield-product case are proved in
   `agent_quadratic_cross_core/FIXED_POWER_SAVING_GATE.md`.  The live
   geometric target is therefore a global fixed-power
   **mixed-product-or-shield-bank** theorem, not a near-injective local map.

   A first fixed-power regime split is now rigorous.  Put
   `r=(alpha+o(1))log n`, `d_0=n/2^r`, and select the pointwise supply
   `D=d_0/n^{o(1)}`.  For `t=floor(r/2)`, proper-downshadow Hall gives

   \[
       K_t\le\left\lceil {D\Lambda_t\over {r\choose t}}\right\rceil,
   \]

   so the desired `d_0^epsilon` saving holds whenever

   \[
       \Lambda_t\le n^{o(1)}{ {r\choose t}\over d_0^\epsilon}.
                                                               \tag{EIC'a}
   \]

   Thus for `alpha>=1/2` the only residue is one explicit heavy central
   prefix and its released half-core complex.  For fixed `alpha<1/2`, let
   `q_ab` be the selected blocker codegree of two singleton-ear sources.
   The exact moment bound

   \[
        \sum_{a\ne b}q_{ab}^2\ge {|S|^2D^4\over4n^2}
   \]

   combines with the global forward-splice decoder as follows: if an
   `n^{-o(1)}` fraction of this square mass has both cross-splice directions
   of `n^{-o(1)}` relative density, then

   \[
        |E|\le n^{\alpha+o(1)}V(P),                         \tag{EIC'b}
   \]

   giving every fixed saving
   `epsilon<(1-2alpha)/(1-alpha)`.  Failure below one half is therefore not
   diffuse: most codegree-square mass lies on nested/incompatible rotations.
   The seam `alpha=1/2` belongs to the heavy-prefix alternative.  This
   global-EIC split (which deliberately uses nonlocal ordinary faces) is
   proved in `agent_linear_codim_capped/FIXED_POWER_EIC_SPLIT.md`.

   The heavy alternatives themselves now have exact local descents.  For a
   canonical central split `A=Q_A dotcup R_A`, `|Q_A|=s`, define the toggle
   bank `{R_A union B:B subset Q_A}` and let `kappa` be its maximum overlap.
   Then

   \[
        2^s|S|\le\kappa V(P),\qquad
        |E|\le\kappa D2^{-s}V(P).                           \tag{EIC'c}
   \]

   With `s=ceil(r/2)` and `alpha>=1/2`, `kappa<=D^{1/4}n^{o(1)}`
   gives a quarter-power saving.  If `kappa` is larger, one actual face `F`
   is common to all colliding sources, every residual `A-F` has rank at most
   `r/2`, and

   \[
       \{B\cup(A-F):B\subseteq F\}
   \]

   is an injective complementary bank of size `2^{|F|}kappa`; hence every
   individual heavy child has a square-root cap saving.  Only reuse *between*
   different children remains.

   On the incompatible-rotation side, weighting records by the second common
   blocker gives a multiset `Omega`.  If `M` is the maximum occurrence weight
   of one marked blocker among its repaired rank-`r` targets, their marked
   downsets satisfy

   \[
                  |\Omega|\le rM2^{1-r}V(P).                \tag{EIC'd}
   \]

   Thus the rotation mass is paid unless one actual blocker label has large
   weighted reuse.  The surviving low-rank atom is correspondingly a
   common-blocker, variable-base child, not an unstructured tangle of
   histories.  These toggle and marked-target theorems are proved in
   `agent_heavy_prefix_rotation/HEAVY_PREFIX_ROTATION_DESCENT.md`.

   Cross-child reuse has an exact second-moment threshold.  If every source
   has `q` toggle-bank faces and `d(F)` sources hit a bank face `F`, put
   `N=q|S|`.  If ordered off-diagonal collisions can be charged to ordinary
   faces with aggregate load `L`, then

   \[
      \sum_F d(F)(d(F)-1)\le LV(P),\qquad
      N\le {1+\sqrt{1+4L}\over2}V(P).                       \tag{EIC'f}
   \]

   Therefore

   \[
       |E|\le {D\over2^{\lceil r/2\rceil}}
             {1+\sqrt{1+4L}\over2}V(P).                    \tag{EIC'g}
   \]

   At `alpha=1/2`, any `L<=D^{1-eta}n^{o(1)}` gives the fixed saving
   `eta/2`; away from the seam the exact saving is
   `alpha/[2(1-alpha)]-(1/2)log_D L`.  This also has an exact chi-square /
   size-biased high-tail form and applies to marked common-blocker downsets.
   Two output faces are insufficient.  The complete quadratic shield gives
   `D^{2-o(1)}` fibres for canonical union/hull outputs, although its full
   shield bank pays nonlocally.  Hence the target is aggregate first-divergence
   charging, not a pointwise hull map.  See
   `agent_cross_child_telescope/CROSS_CHILD_COLLISION_TELESCOPE.md`.

   There is also a fixed-power **circuit-codegree** theorem.  Let `H` be
   the 4-uniform hypergraph of nonconvex quadruples and let `Lambda` be its
   maximum triple codegree on an `m`-point support.  Every convex rank-`r`
   core then has at least

   \[
                  m-r-\Lambda {r\choose3}
   \]

   convex one-point extensions, so a source family `C` contributes at
   least

   \[
          {|C|(m-r-\Lambda {r\choose3})\over r+1}
   \]

   ordinary `(r+1)`-faces.  If `|C|>=d^{\beta r}` and
   `r+Lambda {r\choose3}<=m/3`, this proves `(EIC')` for every
   `epsilon<beta`.  On the hard coefficient-`1/4` slice,
   `beta>=1-o(1)`, so `epsilon=1/3` is available with ample slack.

   The exterior version applies directly to the *selected* repair graph,
   without contamination by points inside source hulls.  Every selected
   exterior blocker has a rooted circuit
   `a in int conv{b,c,x}` with `a,b,c` in the source.  Pigeonholing the
   `3{r\choose3}` source tags and then the ambient rooted triangle loses
   only `2^{O(r)}` records; a `sqrt(r)`-set of common blocker labels can be
   fixed by DRC with only `2^{O(r^{3/2})}=2^{o(r^2)}` entropy loss.
   Hence, **at the quadratic-entropy structural scale**, the
   unbounded-codegree residue is a source family sharing one rooted triangle
   and a growing common exterior blocker fan.  This localization is not yet
   a fixed-power EIC reduction: the ambient-triangle factor `n^3=2^{Theta(r)}`
   is itself load-bearing compared with `d^epsilon`.  A completion must sum
   the rooted cells with controlled overlap instead of simply choosing one.
   The bounded-codegree theorem and this structural localization are proved in
   `agent_quadratic_cross_core/CIRCUIT_CODEGREE_POWER_SAVING.md`.

   The ambient-tag problem is now removed on the wide-fan branch.  Split
   repairs sourcewise into their at most `r^2` canonical oriented tangent
   cells and thin the largest cell to degree `D`.  In a fixed cell the
   blockers form the exact two-dimensional dominance poset

   \[
       x\preceq y\quad\Longleftrightarrow\quad
       L(x)\ge L(y),\ R(x)\ge R(y),
   \]

   and incomparable `x,y` give the ordinary face `R union {x,y}`.  A wide
   row contains an antichain of size at least `sqrt D`.  If `Lambda` is the
   maximum number of hidden intervals sharing one retained core and one
   incomparable blocker pair, summing these pair faces over **all** tangent
   cells gives

   \[
                    E_{\rm wide}\le4(r+1)\Lambda V(P).       \tag{EIC'e}
   \]

   There is no factor depending on `n`: a target face has at most its rank
   many adjacent-pair decompositions.  Hence
   `Lambda<=D^{1-epsilon}` proves the desired fixed saving on every wide
   row.  Dilworth leaves only a blocker chain of length `sqrt D`, or a
   heavy hidden fibre in which more than `D^{1-epsilon}` hidden intervals
   share one core and incomparable blocker pair.  Fixed-outer-cell products
   realize both reuse mechanisms even in the low-addable slice, but their
   internal two-ended complexes pay; the exact remaining theorem must
   recurse into those hidden coordinates.  See
   `agent_quadratic_cross_core/COMMON_ROOT_FAN_SUM.md`.

   The entropy half of that hidden recursion is exact as well.  Split each
   hidden boundary interval canonically into `I=(L,J)`.  If
   `rho=log|H|/|I|`, then for every `zeta` either one half has entropy
   density `>rho+zeta`, or

   \[
       I(L;J)\le\zeta|I|,
   \]

   the product marginal puts mass at least `2^{-zeta|I|}` on compatible
   concatenations, and weighted Cauchy gives compatible rectangles with
   probability at least `2^{-4zeta|I|}`.  This split uses boundary rank and
   pays no ambient midpoint tag.  In the fixed-outer product, the resulting
   two-ended bank has the exact multiplier

   \[
          {\binom M2^2M^{q-2}\over M^q}={(M-1)^2\over4},
   \]

   stronger than any fixed cap power.  The remaining **balanced
   hidden-fibre atom** is geometric: a dense compatible prefix--suffix
   rectangle must either yield recoverable two-ended faces with polynomial
   global overlap, or split into contextual rank-half children while
   preserving blocker weights.  Such a recursion has depth `O(log r)` and
   even a polynomial loss per level totals only
   `2^{O((log r)^2)}=n^{o(1)}`.  Naive marginal recursion is invalid because
   a blocker of `I` need not block either half.

   The common-base geometric half is now proved.  Atomize a weighted
   half-chain extension over a convex base `F` by one canonical nonempty
   edge-pocket component `Q`, retaining all omitted completion/blocker data
   as its weight `beta`.  With threshold `T=r^C`, either heavy atoms carry
   at least half the mass and descend exactly to free rank at most `q/2`, or
   light atoms in nonadjacent pockets have ordered-pair mass `>W^2/8` and

   \[
                  (F,i,Q),(F,j,Q')\longmapsto F\cup Q\cup Q'
   \]

   with weighted load `<r^{2C+4}`; otherwise one three-pocket window carries
   `>W/4` into at most three rooted rank-half laws.  The two tangent chords
   recover `F,Q,Q'`, avoiding the fatal bare `2^q` split fibre.  This local
   recursion loses only a polynomial over `O(log r)` balanced levels.  Its
   exact remaining obstruction is **cross-context base merging**: in a heavy
   step `F union Q` is a base only for that source, so two collision partners
   may lose their common base, and descendant targets from many ancestor
   bases may later merge.  See
   `agent_quadratic_cross_core/BALANCED_HIDDEN_ATOM_POCKET_SPLIT.md`.

   The square bookkeeping inside this descent has now been repaired.  If
   the atom weights in the cyclic pockets are `beta_(i,a)`, then either a
   fixed fraction of their ordered square lies on separated pockets, one
   atom retains a fixed fraction of the diagonal square, or a fixed fraction
   lies on distinct atoms in one three-pocket window.  A protected-window
   face of rank `s` has fewer than `3s^4` such contextual descriptions.
   More generally, if every refined child `c` has two recoverable ordinary
   face banks with

   \[
       |G_c|^2\le K|A_c||B_c|,
   \]

   and global overlaps `L_A,L_B`, one Cauchy step gives

   \[
       \left(\sum_c|G_c|\right)^2
             \le K L_A L_B V(P)^2.                         \tag{EIC'h}
   \]

   Thus exponentially many heavy atoms or descendant bases introduce no
   factor by themselves.  In the factorized flank model, two one-slot
   reservoirs of sizes `q_-,q_+` and a blocker alphabet of size `y` have
   exact paired-code loss

   \[
       K=\left\lceil {q_-q_+y^2\over
          (1+q_-+{q_-\choose2})(1+q_++{q_+\choose2})}
          \right\rceil,
   \]

   which is at most four in the balanced case.  The remaining obstruction
   is therefore not loss of the collision square among many atom labels; it
   is the genuinely one-pocket branch in which no second recoverable
   one-slot reservoir is exposed.  A fixed insertion-edge chain is
   projectively universal, so this last reservoir cannot follow from nesting
   alone.  See `agent_cross_atom_square/CROSS_ATOM_SQUARE_LIFT.md`.

   Requiring both eventual banks to retain the ancestor base is exactly
   false at the seam.  A strict one-pocket chain gives `D` rank-`r` sources,
   `D` blockers per source, atom weights all equal to `D`, but only `2D+1`
   ordinary faces containing the common base.  The parent square is `D^4`,
   the sum of child squares is `D^3`, and every two-bank certificate confined
   to base-retaining faces has

   \[
                         K L_A L_B\ge D^2/9.                \tag{EIC'i}
   \]

   This is not an `(EIC')` counterexample: its source entropy is only linear
   in `r`.  Releasing one bank gives a sharp positive allocation theorem.
   For `C` contexts, a first bank of `2D` rooted atom faces with overlap
   `Lambda`, and a common unguarded internal reservoir of `H` ordinary
   faces, one may choose `b=ceil(D^3/2)` second-bank faces per context with
   overlap

   \[
                    L_B=\left\lceil{Cb\over H}\right\rceil. \tag{EIC'j}
   \]

   The universal lower bound makes every isolated or polynomial-size family
   of contexts harmless.  The sole remaining overload is quantitative:
   quadratically many outer contexts reuse the same released reservoir so
   heavily that `Lambda ceil(CD^3/(2H))` exceeds the seam threshold
   `D^{1-eta}n^{o(1)}`.  The next theorem must multiply outer-context faces
   by internal faces, or charge the cross nonconvexity to a shield complex.
   See
   `agent_cross_context_merge/CROSS_CONTEXT_BASE_RETENTION_BARRIER.md`.

   The universal one-pocket branch also has an unconditional quadratic
   shield reduction.  For each source `A`, apply the banked coefficient
   `1/4` theorem inside its `D` **selected** blockers and choose

   \[
       B=2^{(1/5+o(1))(\log D)^2}
   \]

   blocker-only faces of rank at least `(1/8-o(1))log D`.  If `Lambda` is
   their maximum source overlap, duplicated Hall gives

   \[
       |E|\le {D\Lambda\over B}V(P).                       \tag{EIC'k}
   \]

   Hence either `(EIC')` holds, or one convex shield `J` of rank
   `Omega(log D)` lies wholly in the selected blocker neighbourhoods of
   more than `BD^{-epsilon}=2^{(1/5-o(1))(log D)^2}` actual sources.  On
   the hard slice `|S|>=cV`, all but `D^{-epsilon}V` sources carry such a
   heavy shield, the high-overlap family itself contains `(1-o(1))B`
   distinct shield faces, and some `J` is shared by at least `cB` sources.
   At the
   seam its Boolean bank has size at least `n^{1/16-o(1)}` and its source
   fibre has `2^{(1/20-o(1))(log n)^2}` members.  Thus the last one-pocket
   state is not an arbitrary nested chain: it is a quadratic-entropy source
   family correlated with a macroscopic complete shield.  Coupling those
   two banks, rather than improving the standalone blocker theorem, is the
   remaining task.  See
   `agent_one_pocket_reservoir/ONE_POCKET_RESERVOIR.md`.

   The first global outer--internal multiplication theorem is also exact.
   Suppose there are `C` record cells of size `D^2`, each with an outer
   carrier `R_c`, a first ordinary-face bank of size at least `2D` and
   overlap `Lambda`, and a common internal reservoir `H`.  Let `Omega` be
   the overlap of the context-tagged mixed banks (distinct labelled carriers
   give `Omega=1`).  Put

   \[
      q_c=|\{F\in H:R_c\cup F\text{ is convex}\}|,
      \qquad b=D^3/2,
   \]

   and

   \[
      \bar\delta={1\over C}\sum_c
         \left(1-\min\{1,\sqrt{q_c/b}\}\right).
   \]

   If an actual source occurs in at most `Sigma` cells, the context-tagged
   mixed unions `R_c union F` and one Cauchy allocation give

   \[
      |G|\le\left(\sqrt{\Lambda\Omega}+\Sigma D\bar\delta
                        +\Sigma D^{-1}\right)V(P).          \tag{EIC'l}
   \]

   Thus `q_c>=D^3/2` for every context removes the reservoir overload
   completely, regardless of `C`; more generally
   `bar delta<=n^{o(1)}D^{-epsilon}` proves `(EIC')`.
   Under singleton outer--internal compatibility, every missing mixed union
   has a planar four-circuit of type `2+2` or `1+3`, giving an exact weighted
   defect bound for `|H|-q_c`.  This criterion can fail maximally: a scalable
   rational family has quadratically many outer contexts but only empty and
   singleton mixed unions, with all failures witnessed by one common guard
   pair.  It is not an `(EIC')` counterexample because its released outer
   shield is convex and contributes an enormous Boolean face bank.  Hence the
   residual is now the sharp alternative: context-tagged mixed unions, or a
   shield complex forced by concentrated cross four-circuits.  See
   `agent_outer_internal_product/OUTER_INTERNAL_MIXED_BANK.md`.

   Circuit concentration itself now has an exact cover-or-toggle split.
   For a carrier `R` and internal face reservoir `H`, form the rank-two
   clutter of all nonempty outer traces of bad `2+2` and `1+3` circuits.
   If `G subseteq R` meets every trace, planar Caratheodory gives

   \[
                    (R-G)\cup F\text{ convex}\qquad(F\in H). \tag{EIC'm1}
   \]

   Hence, for distinct contextual carriers with `D^2` records each, if the
   minimum trace transversal has size at most `t`, a singleton carrier bank
   and the fully released reservoir give

   \[
        |E_{\tau\le t}|\le
          D^2\sqrt{{\sum_{i\le t}{n\choose i}\over |H|}}\,V(P). \tag{EIC'm2}
   \]

   The real local square constant here is `D^4/|H|` and may be much smaller
   than one.  If `D>=n^delta`, `|H|>=2^{c(\log D)^2}`, and
   `t=(c delta/2+o(1))log D`, the multiplier in `(EIC'm2)` is eventually
   smaller than one.

   Conversely, a maximum matching of `k` disjoint traces is also a
   transversal of size at most `2k`, and supplies the exact Boolean toggle
   bank

   \[
      \left\{\left(R-\bigcup_{i\in I}P_i\right)\cup\{y\}:
                    I\subseteq[k],\ y\in Y\right\},
      \qquad |\cdot|=D2^k.                              \tag{EIC'm3}
   \]

   If `L_T` is the global overlap of these toggle banks, the two branches
   combine as

   \[
       |E|\le\left(D^2\sqrt{{\sum_{i\le t}{n\choose i}\over |H|}}
                    +L_TD2^{-\lfloor t/2\rfloor-1}\right)V(P). \tag{EIC'm4}
   \]

   Thus subpolynomial toggle overlap completes `(EIC')` with an explicit
   fixed power.  The residual is exactly high contextual toggle overlap.
   A rational sparse family makes every singleton outer vertex a trace and
   has maximal released/toggle overlap, so matching alone is insufficient;
   its unrestricted outer cloud is convex and pays by a huge Boolean shield.
   Heavy toggle overlap has one further exact localization.  If one toggle
   output lies in `Omega` contextual banks, it fixes a common retained outer
   base and canonically produces `Omega` distinct **uniform-rank** completion
   faces `Q_c`, with `m/2<=|Q_c|<=m`, such that both
   `base union Q_c` and `base union Q_c union {x}` are convex for one fixed
   internal label `x`.
   This child has an exact source-downset bank.  In a general cell with base
   `B`, completion family `mathcal Q`, and `D` (possibly completion-dependent)
   repair labels `Y_Q`, all

   \[
       S\cup Q\cup\{y\},\qquad
       S\subseteq B, Q\in\mathcal Q, y\in Y_Q,           \tag{EIC'n1}
   \]

   are ordinary faces.  There are exactly `2^{|B|}` such occurrences per
   actual repair record, so if their global representation overlap is `L`,

   \[
                         |E|\le L2^{-|B|}V(P).              \tag{EIC'n2}
   \]

   Complementary subsets of `B` give a zero-overlap ordered two-face decoder
   and the exact coefficient-scale inequality

   \[
                         2^{|B|}|E|\le V(P)^2.              \tag{EIC'n3}
   \]

   Finally, a heavy middle-layer output fixes `Q`, a half-base `S`, and the
   repair label after the factor
   `{floor(|B|/2)+|Q| choose |Q|}` and the actual repaired-carrier source
   multiplicity `Delta`; the missing halves `B-S` then become distinct
   uniform completions of rank `ceil(|B|/2)` over one common rooted base.
   Thus the sole surviving loss is now a rank-halving **cross-base** overlap,
   not capacity inside a heavy fibre.

   The terminal geometry of this child is also exact.  For a common face
   `F` and completion support `W`, let `mathcal T(F,W)` be the rank-at-most
   four clutter of traces on `W` of bad four-circuits.  A matching of `s`
   disjoint traces gives

   \[
                  I(F,W)\le2^{|W|}(15/16)^s,               \tag{EIC'o1}
   \]

   while the union of a maximal matching has at most `4s` labels and deleting
   it releases the complete joined shield `F union (W-G)`.  Two uniform
   completions either have convex union with `F`, or a four-circuit meets
   both symmetric differences; compatible ordered pairs map to union faces
   with load at most `3^{2q}`.

   In particular, a complete rank-`q` layer (`q>=4`) over `W` forces
   `F union W` convex.  More generally, if a rank-`q` completion family on
   an `m`-point cloud misses a fraction

   \[
                         <((q-3)/m)^4,                      \tag{EIC'o2}
   \]

   then the whole cloud is convex.  Together with the universal blocker
   reservoir, this pays `D^2` per completion for
   `q<=\tfrac12\log D`; small completion families are paid directly by the
   same reservoir.  The only surviving child is therefore a
   quadratic-entropy, far-from-complete rank-`O(log D)` family with heavy
   central overlap at every rank-halving scale.  After one more constant
   thinning, every completion has only `D^{O(1)}` compatible partners;
   almost every pair is incompatible and carries a four-circuit meeting both
   symmetric differences.  Kruskal--Katona alone has no fixed-power
   expansion here, and separate large marginal overlaps need not align;
   exact middle-layer and two-star regressions verify both facts.
   There is a final exact reduction, and a sharp warning about its scope.
   After the compatible-pair bank fails, greedy thinning loses only
   `D^{O(1)}` and leaves a genuinely pairwise-incompatible family.  The
   elementary sunflower theorem then supplies `D^{Omega(1)}` pairwise
   disjoint petals over an enlarged common base, while preserving every
   one-point repair alphabet; every petal pair is crossed by a bad
   four-circuit.  This does **not** force many circuit colours or a small
   trace cover.  A rational nested-ear product with `q` nonadjacent
   `L`-point chains has `L^q` pairwise-incompatible completions but only
   `q {L\choose2}` witness circuits and trace transversal `q(L-1)`.  It is
   in fact harmless for a stronger reason: after deleting the common base,
   every two-point-per-container union is convex.  The coordinate-union
   decoder has load at most `2^q`, so it supplies
   `M(M-1)/2^q` ordinary detached faces.  More generally, detached-compatible
   ordered pairs give `V>=E_det/3^{2q}`, and cyclic two-ended separated
   containers give

   \[
                         V\ge M^{1+2/q}/16.                 \tag{EIC'o3}
   \]

   This detached bank already sums globally when paired with the
   base-retaining source bank.  For cells with `M_c>=M_0` and global bank
   overlaps `Lambda_src,Lambda_det`, recoverable-cell Cauchy gives

   \[
   \sum_cD^2M_c\le
      4D^{3/2}M_0^{-1/q}
      \sqrt{\Lambda_{src}\Lambda_{det}}\,V(P).              \tag{EIC'o4}
   \]

   Hence cyclic cells close whenever
   `M_0^{2/q}>=16 Lambda_src Lambda_det D^{1+2epsilon}`;
   failure is now quantitatively high detached-bank reuse, not missing
   local capacity.

   Thus a further `D^{O(1)}` thinning leaves the strictly narrower residue:
   a quadratic-entropy rank-`O(log D)` family which is pairwise nonconvex
   even after the common base is deleted.  Every witness four-circuit then
   lies wholly in the two completion faces and meets both symmetric
   differences.  The exact remaining operation is to extract a recoverable
   cyclic two-ended coordinate from this detached circuit system, or sum a
   one-pocket unrestricted shield across the erased common-base contexts.
   Thus the final theorem must discharge a rank-`O(log D)` common-base
   completion family, forcing the analogous unrestricted outer shield in
   general.  See
   `agent_outer_internal_product/CIRCUIT_TRANSVERSAL_GUARD_RELEASE.md` and
   `agent_common_shield_mixing/CIRCUIT_TRANSVERSAL_OR_OUTER_TOGGLE.md` and
   `agent_common_shield_mixing/HEAVY_COMMON_BASE_SOURCE_DOWNSET.md`,
   `agent_middle_toggle_fibres/MIDDLE_TOGGLE_FIRST_DIVERGENCE.md`, and
   `agent_outer_internal_product/COMMON_BASE_COMPLETION_SHADOW.md`, and
   `agent_outer_internal_product/PAIRWISE_INCOMPATIBLE_COMPLETION_REGRESSION.md`,
   `agent_detached_pair_union/DETACHED_PAIR_UNION_BANK.md`, and
   `agent_outer_internal_product/DETACHED_SHIELD_TWO_ENDED_PRODUCT.md`.
   A projectively universal replacement of the radial containers does not
   escape: the exact lexicographic recurrence has one-gap banks

   \[
     B_j=R_{j-1}A_{j+1}\prod_{i\notin\{j-1,j,j+1\}}L_i,
     \qquad
     \prod_j{B_j\over\prod_iL_i}
       \ge\prod_i{H_i\over L_i^3}.                         \tag{EIC'o5}
   \]

   The universal local reservoir plus Jensen makes the best `B_j` larger
   than the transversal family by `2^{Omega((log D)^2)}`.  Thus every
   recoverable radial/lexicographic product, even with arbitrary low-face
   children, is closed.  See
   `agent_common_shield_mixing/DETACHED_RADIAL_LEXICOGRAPHIC_PROFILE.md`.

   There is now an exact factorization of the non-containerized remainder.
   Join two completion-support containers whenever one bad four-circuit
   meets both.  If `Z_1,...,Z_s` are the connected components of this circuit
   graph, then planar four-locality gives the simplicial-join identity

   \[
               \mathcal F(Z)=\mathop{*}_a\mathcal F(Z_a),
               \qquad V(Z)=\prod_aV(Z_a).                 \tag{EIC'o6}
   \]

   For a uniform completion law, write `h_a=H(Q cap Z_a)` and `V_a=V(Z_a)`.
   The exact Kraft balance is

   \[
      \log{V(Z)\over M}
       =\Big(\sum_a h_a-\log M\Big)
          +\sum_a(\log V_a-h_a).                          \tag{EIC'o7}
   \]

   Thus failure of a `D^gamma` shield gain forces both total correlation and
   total local shield surplus below `gamma log D`; a weighted density
   averaging lemma then localizes the leading entropy/rank to one
   circuit-connected child without an ambient-label loss.  This is sharp:
   four separated square pockets filled with nested triangles have every
   detached pair incompatible, yet cross-pocket `3+1` and `2+2` circuits
   make the component graph complete.  Moreover the top-rank layer of an
   arbitrary hard order type is already a circuit-connected detached family,
   so recursing only on its unrestricted child complex is circular.  The
   load-bearing datum that must survive `(EIC'o6)`--`(EIC'o7)` is the common
   base together with the `D` one-point repair alphabet.  See
   `agent_detached_pair_union/DETACHED_CIRCUIT_COMPONENT_FACTORING.md`.

   That marked alphabet now gives one further fixed-power exit.  For a
   rank-`q` completion with `D` one-point extensions, one boundary edge
   contains `m>=D/q` extension labels.  In the exact two-dimensional tangent
   poset on that pocket, height times width is at least `m`.  If the height is
   below `m^{1/3}`, a width-`m^{2/3}` antichain produces pair extensions; after
   summing over any `M/2` such completions and using the rank-`q+2` decoder,

   \[
       V(P)\ge {M\over8{q+2\choose2}}
                    \left({D\over q}\right)^{4/3}.        \tag{EIC'o8}
   \]

   For `q=O(log D)`, this is the already-injective `DM` repair-star bank times
   a genuine `D^{1/3-o(1)}` gain.  The complementary case has a nested chain
   of at least `m^{1/3}` repair labels, hence an unrestricted superpolynomial
   shield.  Repeated occurrences of one shield face obey an exact
   splice-or-cross-circuit alternative: after deleting a transversal of every
   bad-circuit trace from each base, two released bases either join the shield
   to one face or a bad four-circuit meets both base differences.  If a
   `theta` fraction of the collision energy splices with output load `L`, then

   \[
       {W\over V(P)}\le {a+\sqrt{a^2+8L/\theta}\over2},
       \qquad a=\alpha+{2\beta\over\theta},               \tag{EIC'o9}
   \]

   where `sum w_i^2<=alpha W` and `beta W` is the exceptional collision
   budget.  Failure localizes, via `(EIC'o6)`, to one circuit-connected
   nested-label child while retaining the repair mark.  This is the sharp
   boundary: surrounding an arbitrary order type `X` by a generic triangle
   makes all maximum-rank bases a connected total-release obstruction while
   `V(X union U)<=8V(X)`.  Thus forgetting the marked extension at this step
   makes the recursion coefficient-equivalent to the original problem.  See
   `agent_common_shield_mixing/GLOBAL_ONE_GAP_COLLISION_RELEASE.md`.

   Pairwise detached incompatibility nevertheless makes the `DM` repaired
   stars themselves injective.  Alphabet diversity also gives

   \[
      V(P)\ge\max\left\{DM,
          h\left(\left\lceil{DM\over\rho}\right\rceil\right)\right\},
      \qquad \rho=\max_y|\{Q:y\text{ repairs }Q\}|.       \tag{EIC'o10}
   \]

   But this cannot be strengthened using only star links or maximality: a
   scalable radial construction has a common `D`-label alphabet, `M=L^q`
   pairwise-incompatible completions, and exactly `DM` maximal full-support
   repair stars, every pair of stars having nonconvex union.  Its detached
   cluster and repair shields pay globally, so it is not an EIC' counterexample;
   it proves that the remaining theorem must multiply or sum those unrooted
   shields across the marked histories.  See
   `agent_outer_internal_product/REPAIR_STAR_CLIQUE_BARRIER.md`.

   Retaining the repair label yields an exact global Carleson criterion.  If
   a weighted star occurrence `e` has mark `p_e` and at least `K` shield
   faces `F` containing that mark, all of rank at most `h`, put

   \[
      I=\sum_e w_e|\mathcal H_e|,
      \qquad
      \Lambda=\max_{p,F}\sum_{e:p_e=p,\,F\in\mathcal H_e}w_e.
   \]

   Since there are at most `hV(P)` marked ordinary faces,

   \[
           I\le\Lambda hV(P),\qquad
           V(P)\ge {DMK\over\Lambda h}.                 \tag{EIC'o11}
   \]

   Thus `K/(Lambda h)>=D^epsilon` is precisely the missing fixed-power
   gain.  There is also a marked version of `(EIC'o9)`: if a `theta` share
   of common-`(p,F)` collision energy splices with load `L`, then

   \[
       {I\over V(P)}\le
       {ha+\sqrt{h^2a^2+8hL/\theta}\over2},
       \qquad a=\alpha+{2\beta\over\theta}.              \tag{EIC'o12}
   \]

   Failure fixes one actual common marked shield `(p,F)` in one connected
   child.  This is again sharp: the radial star-clique barrier can use a
   projectively universal arbitrary-order-type repair block `Y`; every
   `(p,F)` then has fibre exactly `M`, every nontrivial star--shield union is
   nonconvex, and the circuit graph is connected.  Hence the mark alone
   does not make shield overlap summable.  The final atom must also retain
   a completion insertion edge/tangent history, or use a second output that
   records completion information.  See
   `agent_common_shield_mixing/MARKED_NESTED_SHIELD_CARLESON.md`.

   This supersedes the earlier `Omega(r^2)` estimate.  Thus a putative
   counterexample cannot put essentially all of its obstruction into a
   small onion pocket: it has polynomially many exterior ear labels per
   hard face.  The common-apex-cloud examples show that those labels may
   nevertheless be shared by exponentially many sources, so (22) sharpens
   but does not by itself solve the global Hall-overlap problem.

The proposed short endpoint-stack completion is nevertheless false.  An
exact concave-chain/apex family has at least `5^(r-3)` low-extension
rank-`r` sources with the same repaired outer triangle, the same tangent
endpoints, and the same inner pocket; any convex target retaining the apex
contains at most two source-chain vertices.  Consequently a successful map
must write `Omega(r)` source bits into the chosen inner target face.  The
remaining gate is a genuine global capacity allocation theorem, not
recoverability from `O(log r)` tangent/onion states.

There is a rigorous positive result on repeated pockets which uses this
capping freedom.  Suppose `K=2^{o(r^2)}` rooted frames have the same
`m`-point pocket (or a common core with only `m^{o(1)}` extra points), have
distinct exposed outside signatures, and use only ear histories of length
`I=o(r)`.  If at most `d<=m` marks are selected over any base history, then
the selected demand divided by the union of the completed rooted targets
and the ordinary convex faces of the pocket is at most

\[
  2^{O_c(I+\sqrt{\log_2K})}=2^{o(r)}.             \tag{22c}
\]

This follows from the two simultaneous bounds `d` and
`K(I+1)d m^I/V(Q)`, together with
`V(Q)>=2^{c(\log_2m)^2}`.  Thus identical and subpolynomially perturbed
common pockets cannot obstruct the capped Hall statement.  The unresolved
case requires genuinely different crossing pockets with heavily
overlapping unrooted face sets, or target completions from which the outside
signature is not recoverable.  The proof is Theorem 6 and Corollary 7 of
`agent_acp_proof/REPORT.md`.

There is also a rigorous discharge theorem for the opposite,
low-frame-entropy branch.  If the rank-`r` source family is covered by
`T_r=2^{o(r^2)}` ground-set frames, each of size `r^C` for fixed `C`, then

\[
 {2^g|S|\over V(P)}\longrightarrow0,
 \qquad r=\lceil\log_2n\rceil-g.                    \tag{23}
\]

The proof bounds the sources in their frames by
`T_r binom(r^C,r)`, deletes one frame, and applies the explicit classical
bound `V(Q)>=2^{(log_2|Q|)^2/10}` to the remaining
`|Q|>=n-r^C` points.  Thus the common-apex, common-onion, and frozen-swap
families satisfy RNP with growing room, regardless of the order type inside
their blocker cloud.  Contrapositively, a genuine RNP counterexample must
have `2^{Omega(r^2)}` polynomial-frame covering number.  Combined with
(22), the unresolved branch has both quadratic source-frame entropy and
polynomially many exterior blockers per typical source; it cannot be a
large fibre over one fixed pocket instance.

The complementary interval-packing geometry is now exact as well.  For a
convex source `A`, associate to an exterior blocker `p` the cyclic interval
of support edges of `A` violated by `p`.  Among `d` selected blockers and
for any `R`, either `R` intervals are pairwise disjoint, or at most `R`
support edges pierce all intervals and one edge is hit by at least `d/R`
blockers.  Disjoint intervals can be repaired simultaneously, and every
selected blocker remains visible in the resulting convex hull.  This proves
the desired local dispersed-versus-rooted dichotomy.

It does **not** by itself give a global Hall map.  In an exact product grid,
a simultaneous repair batch can erase independent source coordinates and a
single target has fibre
`(M-1)^{Theta(r)}=2^{Theta(r^2)}`.  The missing capacity is nevertheless
present in a genuinely two-ended family.  For ordered pocket cells `Q_i`,
the exact forward count is

\[
 \sum_{i<j}C(Q_i)U(Q_j)\prod_{i<k<j}|Q_k|.          \tag{23a}
\]

In particular, identical `M`-point cells contribute the rank-`r` slice
`binom(M,2)^2M^{r-4}`.  With `M=2^r`, this pays the capped demand of the
entropy-rich product obstruction for every blocker-cloud size: the
two-ended slice handles clouds up to order `M^3`, and above that threshold
the universal coefficient-`1/4` lower bound inside the cloud is already
larger than the entire demand.  The exact proof and rational audit are in
`agent_two_ended_hall/REPORT.md`.

The adjacent-cell geometry has now also been made exact.  For a fixed
directed support chord, two rooted chains on opposite sides glue to a convex
set if and only if their two endpoint tangent parameters satisfy the two
corresponding dominance inequalities.  After fixing the two endpoint
neighbours of the retained chain, compatibility is uniform across the whole
tangent cell.  Completing every compatible rectangle and summing over all
cells costs only `O(r^2)` target multiplicity: a target chooses its directed
root chord, and the two half-planes recover the cell.  Thus, if a cell has
`s_c` hidden chains and `t_c` blocker labels, its selected repair mass obeys

\[
 |E_c|\le \min\{d,s_c,t_c\}\,|\mathcal T_c|.       \tag{23b}
\]

There is a second exact ordered-array calculation.  If the retained
boundaries with fixed inner data form a bipartite support graph `G` with
`m` edges and maximum degrees `Delta_A,Delta_B`, then the number of pairs of
vertex-disjoint boundary choices is at least

\[
 {m\over2}(m+1-\Delta_A-\Delta_B).                 \tag{23c}
\]

When both endpoint pairs are forward, at least half of these pairs give
distinct two-ended convex targets (up to polynomial global recovery).  It
follows that either these targets pay the entire capped demand `dm`, or one
endpoint value occurs on essentially half the boundary variants.  Peeling
that endpoint is weight-neutral because the active rank drops by one while
the cap doubles.  The fully forward adjacent-cell model is therefore
closed.

The last reuse problem is narrower.  A nested endpoint can remain hidden
for an arbitrarily long peeled prefix, so a one-step child recurrence is
false.  For one fixed terminal child after `s` nested peels, however, the
discarded prefixes are ordinary convex faces and the universal lower bound
inside their vertex cloud gives

\[
 e\le 2^{O(\sqrt{s\log n})}V(P).                  \tag{23d}
\]

Taking `s=\sqrt r` makes this `n^{o(1)}`.  Consequently a surviving case
must reuse prefix-cloud faces across many different terminal children.  The
scale is sharper than merely exponential: the capped source-cloud theorem
disposes of every fixed prefix reused by `2^{o(r^2)}` children.  A genuinely
hard class has quadratic child entropy.  This is the current OAI
(ordered-array inheritance) regime, not generic tangent anti-alignment.

Two exact warnings prevent a premature high/medium-row closure.  A word of
only `sqrt(r)` ambient labels has at most
`n^{sqrt(r)}=2^{O(r^{3/2})}` values and cannot encode a quadratic-entropy
terminal core.  Enlarging the word to `Theta(r)` labels makes its recovery
fibre `n^{Theta(r)}=2^{Theta(r^2)}`, too large to absorb.  Moreover, even a
common ordered suffix cannot in general be retained in a two-ended target:
in the vertical product, adding one later common coordinate turns the old
two-point endpoint block into an illegal intermediate block and hides one
of its points.  Thus the all-interval/core-recovery issue is real, rather
than an omitted decoder estimate.

A separate rank-profile attack gives an equivalent compact target.  Put
`F_k=sum_{j<=k}v_j` and `ell=ceil(log_2 n)`.  If for some
`b=O(log ell)` one has

\[
 F_{k+b}\ge2F_k\qquad(k\le\ell-2b),               \tag{23e}
\]

then `mu>=ell-3b`, which closes the mean gate.  Pointwise and cumulative
one-step doubling are both false on exact stretchable examples, but every
known example has block length at most two.  A first failure of (23e)
forces a nearby rank with a positive fraction of faces having addable degree
at most `8(k+1)`, reducing (23e) back to the same capped exterior-ear Hall
problem.  Thus the profile and geometric attacks now meet at OAI rather than
being independent conjectures.

The correct batching invariant is weighted.  Projecting rank `m` to
`m-s` multiplies the new cap by `2^s`; it helps only when the projection
fibre is at most `2^s n^{o(1)}`.  Thus a rank drop alone has the wrong sign.
The remaining theorem must amortize the forward cap--cup state in (23a)
against unrooted pocket capacity while preventing persistent directional
anti-alignment.

### Entropy entry at the exact capped factor

There is now a rigorous entry theorem which removes the candidate-supply,
interior-blocker, and prefix-decoding losses.  Canonically list every
rank-`r` source polygon by its boundary word, beginning at its least label.
For a family `S` of such sources, chain-rule entropy gives a boundary
position whose fresh-successor incidence count is at least

\[
                  S\{S^{1/r}-r\}.                \tag{23f}
\]

Ordering the successor rays from outermost to innermost and using the sharp
entropy bound for a nonnegative integer variable strengthens this to

\[
 S\left\{2^{(\log_2S-2\log_2n)/(r-2)}/e-r-1\right\}.
                                                        \tag{23g}
\]

Every selected successor in (23g) is exterior: it violates the first edge
after a common boundary prefix.  On the near-maximal slice
`u(A)<=4(r+1)`, convex additions are negligible, so essentially all records
are distinct repairable nonfaces.  Their hull targets retain the entire
common prefix and the blocker canonically; only one consecutive suffix ear
is hidden.  At the hard scale
`r=(alpha+o(1))log_2n`, `log_2S>=(c-o(1))(log_2n)^2`, `c>=1/4`, the factor in
(23g) is

\[
                    n^{c/\alpha-o(1)}
                    \ge n^{1-\alpha-o(1)},        \tag{23h}
\]

which is exactly the factor required by capped Hall.

For a repair record put `T=ext(A+p)` and `I=A-T`.  The record maps
injectively, up to the fixed boundary-position tag, to `(T,I)`, and

\[
 H(T)+H(I\mid T)=\log_2|G|,\qquad
 \mathbb E|T|+\mathbb E|I|=r+1.                  \tag{23i}
\]

Thus the entropy per expected rank is preserved by the split.  This is the
strongest positive reduction currently available.  It does not by itself
finish the proof: in the product grid both terms in (23i) are essential and
must be multiplied through compatible two-ended faces, whereas in the long
parabolic-prefix example nearly all entropy belongs to `I` and recursive
descent is correct.  The remaining theorem is precisely an
**entropy-sensitive compatible multiplication** for this ACP-correlated
split.

Three subsequent theorems make that final branch substantially more rigid.
First, independently thinning the hidden ear `I` at rate `theta` gives an
ordinary convex face `F=R union (I intersection S)` and the exact estimates

\[
 H(F)\ge H(R\mid p)+\theta H(I\mid R,p),\qquad
 \mathbb E|F|=\mathbb E|R|+\theta\mathbb E|I|.    \tag{23j}
\]

Thus the full conditional hidden-ear entropy, rather than merely its
alphabet size, survives in the face complex.  This still does not close the
mixed case: an exact singleton-ear product rectangle has `NM^2` repair
records but every thinned-core law and every direct repaired-target law has
only `NM+O(N)` capacity.  The missing factor `M` is genuinely the adjacent
tangent-cell/two-ended term.

Second, let `rho=log_2|G|/(r+1)`.  If neither marginal in (23i) has entropy
density exceeding `rho+epsilon`, then

\[
                  I(T;I)\le\epsilon(r+1).         \tag{23k}
\]

Relative entropy on the support event implies that an independent marginal
cross-pair is a valid record with probability at least
`2^(-epsilon(r+1))`; weighted `C_4`/Sidorenko then gives a valid product
rectangle with probability at least `2^(-4epsilon(r+1))`.  Conversely, a
marginal-density surplus slices to a uniform-rank face family at the same
density up to `O(log r/r)`.  Across at most `r` descents the total slicing
loss is only `O(r log r)=o((log n)^2)`.  Hence sparse support and entropy
bookkeeping are no longer obstructions.

Third, a weighted DRC amplification of (23k) says that for every integer
`t`, either one hidden component already carries a large marginal atom, or
there are `t` distinct hidden ears with a common retained-target
neighbourhood of mass at least `2^{-epsilon rt}/2`.  Taking `t=eta r` when
`epsilon=o(1)` loses only `2^{o(r^2)}`.  The near-product equality branch is
therefore a **linear fan of interchangeable long ears over a
quadratic-entropy target family**.  The product grid realizes the fan
equality and pays through its two-ended pool; the parabolic chain realizes
the fixed-component equality and pays through recursive prefix faces.

The remaining fan cannot be discharged by an absolute count on its label
cloud.  A common-apex product with `Theta(r)` hidden microblocks has
quadratic conditional ear entropy, while even the conjectural coefficient
`1/2` bound applied to the union of all hidden labels can be smaller than
the already-counted source entropy.  Its actual geometry is harmless only
because the oriented two-ended pool has the additional blocker factor.
Accordingly the last theorem must be a *relative oriented surplus* over the
source family, not another absolute `V(Q)` estimate.

Nor does near-product support force that surplus to appear at the **outer**
tangent cell.  There is an exact fixed-cell long-ear product with `a`
retained microblocks, `b` hidden microblocks, and an `M`-point blocker
cluster for which

\[
 |\mathcal G|=M^{a+b+1},\qquad T=(R,p)\perp I,
 \qquad H(T)=(a+1)\log_2M,\quad H(I)=b\log_2M.     \tag{23l}
\]

All root and immediate tangent neighbours are fixed, every record has the
successor-prefix correlation of (23g), and both marginal entropy densities
are sharp.  The missing blocker factor is paid only after recursively
entering the internal coordinates, where descendant two-ended faces appear.
Thus the corrected last branch is genuinely hierarchical: current-scale
forward multiplication, a released nested-prefix complex, **or simultaneous
recursion into the interiors of both split components**.  Proposition 26 of
`agent_acp_proof/REPORT.md` gives the rational realization.

A useful first piece of the corresponding two-record inequality is already
exact.  With one fixed retained core and singleton ears, an ordered pair of
repair records `(x_1,p_1),(x_2,p_2)` maps to the two ordinary faces
`{x_1,x_2}` and `{p_1,p_2}` with fibre at most four.  More generally the
first-onion two-face map proves

\[
              |G_R|^2\le
       4(2s+2)^2 3^{2s}V(P)^2                         \tag{23m}
\]

when the ears have size at most `s` and each pair's first onion remainder,
together with its two blockers, is convex.  Hence singleton ears (fibre
four) and this `s=o(r)` union-compatible branch are discharged.  This
cannot simply be iterated through first onion layers: exact
nested-parabola examples make the proposed remainder-plus-blockers output
nonconvex and reproduce a smaller pocket, so the full nested state really
is load-bearing.

The full product equality case is nevertheless now closed exactly.  Let a
repair cell have an arbitrary retained-core family `R`, hidden blocks
`Q_1,...,Q_b`, and blocker alphabet `Y`, with every transversal a source
face and with the standard two-ended pool allowing at most two choices in
the first and last hidden blocks.  If `q_i=|Q_i|`, `y=|Y|`, and
`s(q)=1+q+binom(q,2)`, then the two-record code gives

\[
 |G|^2\le K V(P)^2,\qquad
 K=\left\lceil{q_1q_by^2\over s(q_1)s(q_b)}\right\rceil .       \tag{23n}
\]

The first output is one source face.  The second retains the other source's
core and middle word, while its two endpoint blocks encode the two omitted
endpoint symbols and both blocker labels.  Thus balanced cells
`q_1=q_b=y=M` have `K<=4`, even with completely arbitrary retained cores.
This discharges the fixed-cell product of (23l), not merely its homogeneous
special case.  The exact theorem and verifier are in
`agent_all_interval_isoperimetry/TWO_RECORD_UNCROSSING.md`.

There is now a stronger **symmetric one-slot** version.  The two coding
reservoirs need not coexist in a single convex face, lie at nonadjacent
edges, or even be distinct cells.  The first output modifies only the first
record, replacing one distinguished symbol by a subset of size at most two
from its own pair-compatible alphabet; the second output does the same for
the second record.  Jointly the two small subsets encode the two omitted
symbols and both blocker labels.  Thus, for alphabets of sizes `q_j,q_k`,

\[
 |G|^2\le K_{j,k}V(P)^2,\qquad
 K_{j,k}=\left\lceil{q_jq_ky^2\over s(q_j)s(q_k)}\right\rceil . \tag{23n'}
\]

In particular the balanced fibre is again at most four.  This removes the
previous adjacent-versus-nonadjacent edge issue.  That removal is essential:
an exact general-position configuration has pair-compatible completion
alphabets on two adjacent edges of a common polygon, but their union remains
nonconvex even after deleting the shared vertex.  Hence no one-output
adjacent-edge surgery is available; the separated two-output code is the
correct local object.

Planarity also supplies the first genuine bridge from an arbitrary endpoint
alphabet to (23n).  For a convex base `B`, group one-point completions by the
unique boundary edge they replace and order a fixed group by
`x<=y` iff `x in conv(B+y)`.  This is a poset, and two points are compatible
with `B` exactly when they are incomparable.  Hence Mirsky partitions a
cell of height `h` into `h` pair-compatible antichains.  By (23n'), no
separation condition between the two chosen cells is required.  Thus if the
relevant insertion heights are `2^{o(r)}`, the product code applies with
only subexponential smoothing loss.

The complementary long-chain branch is not intrinsically simpler than the
original problem.  An explicit projective construction embeds **every**
finite planar order type, preserving its complete convex-subset profile,
inside one strict insertion-edge chain of a fixed triangle.  This has been
verified exactly on the Pascal and the 20/24/30/58-point adversarial records.
Consequently no theorem based only on insertion-poset chain structure can
close the proof.  What is free is merely its prefix accounting: if `e_v`
counts leaves below a prefix-tree node, then

\[
 |\mathcal R|^2=|\mathcal R|+
      \sum_v\left(e_v^2-\sum_{w\text{ child of }v}e_w^2\right), \tag{23n''}
\]

so every pair is charged exactly once at its first divergence.  The missing
content is to absorb the divergence tag into two ordinary convex faces with
subquadratic-exponential global reuse.  See
`agent_cyclic_stem_hw/INSERTION_CHAIN_UNIVERSALITY.md`.

There is also an exact weighted prefix-shadow theorem for this branch.  For
histories with rank-`k` bases `B`, admissible insertion alphabet `X`, and
codimension `t`, put
`Lambda=max_{z,S}|{omega:z in X_omega, S subset B_omega}|`, where
`|S|=k-t`, and let `h=min|X_omega|`.  Duplicated Hall routes histories to
faces `(B-D)+z` with fibre

\[
 K\le\left\lceil{(k-t+1)\Lambda\over
                    h\binom{k}{t}}\right\rceil .       \tag{23n'''}
\]

Taking `t≈sqrt(k)` makes normalized-heavy prefix states subexponential in
`r`; same-edge descent retains the common prefix and its Boolean cube exactly
compensates the increased cap.  The unresolved regime is therefore precise:
the prefix atoms are normalized-light but have large **absolute** collision,
and the insertion alphabets have not yet been partitioned into
`2^{o(r)}` common recoverable reservoirs to which (23n') applies.

A guard-retaining refinement removes edge ambiguity from the collision
branch.  Delete only outside the two endpoints `u,v` of the insertion edge.
In every output `(B-D)+x`, the two cyclic neighbours of `x` are exactly
`u,v`; hence the output recovers the edge and the retained prefix atom.  Its
Hall fibre is

\[
 K_{\rm guard}\le
 \left\lceil{(k-t+1)\Lambda\over\binom{k-2}{t}}\right\rceil, \tag{23n''''}
\]

and applying it separately to the two records squares only this
subexponential loss.  If a later rotation switches to an adjacent edge, the
protected prefix and suffix erode monotonically.  There are at most `r`
switches and at most `3^r=2^{o(r^2)}` root-walk transcripts, with no cycles.
Thus local edge switching is no longer the obstruction.  The last unproved
allocation statement is global: terminal face pairs reached from different
quadratically many outer cores may still coincide, and neither the transcript
nor the local Hall bound yet controls that inter-core reuse.

At the weaker leading-coefficient scale, that last geometric reuse problem
is now closed by a much simpler rectangle decoder.  For a repair rectangle
with all four records `(T_i,I_j)`, write `T_i=R_i+p_i`.  The two cross-sources

\[
                       R_1\cup I_2,\qquad R_2\cup I_1          \tag{23n5}
\]

are ordinary convex faces.  Given them, guessing `p_1,p_2` and the two set
partitions recovers the rectangle, so the global fibre is at most
`n^2 2^{2r}=2^{O(r)}`.  This includes arbitrary variable outer cores and
repeated vertices in the ordered `C_4`; no tangent transcript is needed.

The weighted-to-counted conversion in fact has a sharper exact form.  For a
bipartite record graph with `m` edges, endpoint degrees `d_X,d_Y`, and a
uniform random edge, put

\[
 J=I(X;Y)=\mathbb E\log_2{m\over d_Xd_Y},\qquad M=\log_2m.
\]

The geometric mean of `d_Xd_Y` over the edges is `m2^{-J}`.  Applying
AM--GM to the Rayleigh quotient of the bipartite adjacency matrix, and then
retaining its largest singular value in the fourth spectral moment, gives
the universal inequality

\[
                  \operatorname{hom}(C_4)\ge m^2 2^{-2J}.      \tag{23n6}
\]

ACP Theorem 23 has `J=o(r^2)` and `M=Theta(r^2)`, so (23n5)--(23n6)
prove the desired two-face inequality throughout its stable near-product
branch.  The proof and a 74,938-graph exact audit are in
`agent_cyclic_stem_hw/REPAIR_C4_COEFFICIENT_AUDIT.md`.

The hoped-for lossless weighted-to-counted shortcut is false, although its
entire repeated-endpoint part remains useful.  For a
finite simple bipartite graph with biadjacency `A`, degree diagonals `D,E`,
`m` edges, ordinary ordered `C_4` count
`C=||A||_(S_4)^4`, and degree-weighted count
`W=||D^(1/2)AE^(1/2)||_(S_4)^4`, the proposed inequality was

\[
                         W\le m^2C.                       \tag{23n6c}
\]

This formerly conjectured inequality is now refuted by an elementary
scalable family.  Start with `K_(n,n)` and attach `t` pendant leaves to every
core vertex, on the opposite bipartition side.  With `D=n+t` and
`m=n(n+2t)`, exact counting gives

\[
 C=n^4+4n^2t+2nt^2,
 \qquad
 W=nD^2\bigl(n^3D^2+4ntD+2t^2\bigr).                  \tag{23n6g}
\]

Already `(n,t)=(7,8)` has
`(m,C,W)=(161,4865,127044225)` and `m^2C-W=-938560`.  More
decisively, for `t=n^2`,

\[
 {W\over m^2C}
 ={(n+1)^2(n^3+2n^2+5n+6)\over n(2n+1)^2(2n+5)}
 \sim {n\over8}.                                      \tag{23n6h}
\]

Thus no universal constant-factor replacement exists.  This does not affect
the bucketed counted-rectangle theorem `(23n6)`, but it rules out converting
ACP's weighted `C_4` mass without retaining a degree cap, near-biregularity,
or additional geometric/history structure.  See
`agent_common_shield_mixing/WEIGHTED_C4_SCALABLE_COUNTEREXAMPLE.md`.

The tempting weak Ky--Fan strengthening had already failed.  For the exact `7 times 7`
double-star with `m=13`, the top squared singular values satisfy

\[
 s_1(D^{1/2}AE^{1/2})^2
   ={133+7\sqrt{217}\over2}>117=13s_1(A)^2,              \tag{23n6d}
\]

while `(23n6c)` happens still to hold there:
`(C,W)=(97,14161)` and `W/(m^2C)=14161/16393<1`.  Thus any
spectral proof would have needed compensation across singular modes; the
scalable pendant-core family shows that even such compensation cannot prove
the false universal statement.  The earlier exact audit through `4 times 4`
therefore records a deceptive finite regime rather than evidence for a
theorem.  See
`agent_common_shield_mixing/WEIGHTED_C4_INEQUALITY_AUDIT.md`.

More precisely, put `x_(ij)=d_i e_j/m` on each edge and let `R` be the
edge-compatibility matrix.  For

\[
 h_i=\sum_{l\in N(i)}e_l,\qquad
 g_j=\sum_{k\in N(j)}d_k,
\]

the edgewise slack

\[
 \delta_{ij}=d_i\left(1-{h_i^2\over m^2}\right)
 +e_j\left(1-{g_j^2\over m^2}\right)-1
 +{d_i^2e_j^2\over m^2}\ge0                         \tag{23n6e}
\]

follows from `h_i+g_j<=m+d_i e_j` and convexity.  Summing gives the exact
decomposition

\[
 C-x^TRx=\sum_{ij\in E}\delta_{ij}
 +\!\sum_{\substack{ij,kl\in E:\ i\ne k,\ j\ne l\\
                     il,kj\in E}}(1-x_{ij}x_{kl}).       \tag{23n6f}
\]

Consequently `(23n6c)` *is* a theorem for every ordinary-`C_4`-free support,
and more generally whenever every genuine opposite-edge pair has
`d_i d_k e_j e_l<=m^2`.  This includes all three sharp nonrectangular stress
families.  The exact algebraic residue is only excess degree product on
genuine four-distinct-vertex rectangles.  However, it cannot be charged
after discarding helpful rectangles.  For `K_(3,4)` plus one leaf, with
degrees `(4,4,4,1)` and `(4,3,3,3)`, the positive genuine excess has integer
numerator `828`, exceeding the total `delta` budget `711`; the helpful
genuine deficit has numerator `900`, and the signed identity retains slack
`783`.  Thus a proof must preserve cancellation among genuine rectangles of
different degree profiles; no termwise positive-part statement remains
viable in that branch.  The scalable pendant-core counterexample is stronger:
all genuine rectangles are harmful, their signed deficit exceeds the whole
nonnegative `delta` budget, and `(23n6c)` itself fails.  See
`agent_common_shield_mixing/POSITIVE_GENUINE_CHARGING_COUNTEREXAMPLE.md` and
`agent_common_shield_mixing/DEGENERATE_COMPATIBILITY_SOS.md`.

The sharp repair-relevant replacement is a degree-product cap.  Put
`K=max_(ij in E)d_i e_j`.  Each ordered opposite-edge pair contributing to
`C` has weight at most `K^2`, so exactly

\[
                         C\ge {W\over K^2}.               \tag{23n6i}
\]

This is equality on every biregular graph and remains asymptotically sharp
even when `K/m -> infinity`, so neither `mK` nor any favorable universal
correction in `K/m` is possible.  If `J=E log_2(m/(d_Xe_Y))` and the live
degree-product bucket has
`K=m2^{-J}2^sigma`, weighted DRC and `(23n6i)` give

\[
                         C\ge m^2 2^{-2J-2\sigma}.         \tag{23n6j}
\]

In a dyadic left/right degree bucket `sigma<=2`, hence
`C>=m^2 2^{-2J}/16`.  This removes the polynomial bucketing loss in Theorem
33 but has the same leading `2J` exponent; it saves only `O(log r)` bits in
the quadratic regime and does not improve the fixed-power gate.  See
`agent_common_shield_mixing/CAPPED_WEIGHTED_C4_CONVERSION.md`.

There is also a sharp unconditional `2/3` consequence.  Since both endpoint
supports are ordinary face families, if `v=log_2V(P)` then
`J<=2v-M`.  Combining this with (23n5)--(23n6) yields

\[
       \boxed{v\ge {2\over3}M-{1\over6}\log_2K},             \tag{23n6a}
\]

where `K<=n^2 2^{2r}` is the cross-source decoder fibre.  Thus a planar
repair-history support of entropy at least
`(3/4-o(1))(log_2n)^2` already forces the conjectured coefficient `1/2`.
Tensor powers of projective-plane incidence graphs attain the `2/3`
exponent abstractly, so (23n6a) cannot be improved using marginal face
counts and repair rectangles alone.  They are not planar realizations; the
remaining geometric statement is precisely that cyclic hidden-ear histories
cannot simulate this anti-incidence tensor without releasing extra hybrid
faces.  See `agent_cyclic_stem_hw/COMPONENT_SURPLUS_PAIR_TELESCOPE_BARRIER.md`.

The `3/4` threshold must not be misread as an immediate bootstrap.  For an
ordinary one-step repair graph, every edge is already determined by its
source face and blocker label, so `m<=nV(P)`.  A nontrivial use of (23n6a)
therefore requires a **composite full-history support** whose quadratic
blocker-word entropy has not collapsed, while its two vertex classes are
still face-valued and every homomorphic rectangle still has a two-face
splice.  Constructing precisely that simple support (or proving that its
multiplicity is paid by internal pocket faces) is another equivalent form
of the remaining label-faithful-history gate.

Inside one fixed tangent cell the abstract `2/3` obstruction improves
sharply.  Compatibility of the two rooted boundary chains is a strict
two-dimensional dominance relation.  A dyadic first-coordinate
decomposition into Ferrers cells, the layer-cake identity, and Holder give

\[
 \operatorname{hom}(C_4,G)
 \ge {m^3\over
  2|L||R|\lceil\log_2(|L|+|R|)\rceil^3}.             \tag{23n6b}
\]

Thus a recoverable single cell has a `3/4`, rather than `2/3`,
record-to-face conversion.  The proof and exhaustive audit are in
`agent_root_followup/DOMINANCE_C4_SUPERSATURATION.md`.  This still does not
tensor automatically: a projective-plane support can be partitioned into
recoverable star cells, while its independent conditional neighbor symbols
remain unencoded.  Across many repair levels one needs stacked coexistence
and recovery of the completed cell reservoirs, not merely recovery of the
cell identifiers.

This still does **not** complete the unrestricted proof.  In the
component-surplus alternative, passing to the denser retained or hidden
marginal can discard a constant fraction of the original joint entropy.
The existing density-preserving rank slice preserves entropy *per rank*,
not the full quadratic record mass or the two-output budget.  A complete
argument must give a pair-valued recursion which retains both pieces until
a near-product node is reached, or otherwise charge the discarded piece to
ordinary convex faces.  This is now the exact leading-coefficient gap.

There is an important coefficient-versus-capped qualification.  For a
canonically marked repair record `(R,I,p)`, with source `A=R union I` and
target `T=R union {p}`, the exact projection identity is

\[
 2H(R,I,p)-H(A)-H(T)
   =H(I,p\mid R)-I(I;p\mid R).                       \tag{23n7}
\]

An unequal-alphabet planar lens product has a fixed retained-component
density surplus while the right side of (23n7) is `Theta(r^2)`.  Thus
marginal selection and mixed source--target projection are decisively
insufficient.  On the same example, however, outputting the two original
source faces loses only the two blocker labels, namely `Theta(r)` bits.
Likewise the exact separated endpoint code has fibre `2^{Theta(r)}`.  This
kills a capped `2^{o(r)}` recursion but not a coefficient-scale
`2^{o(r^2)}` history decoder.  The proof and exact scalable audit are in
`agent_all_interval_isoperimetry/COMPONENT_SURPLUS_PAIR.md`.

Accordingly the remaining coefficient problem is global rather than local:
show that linear blocker/cell-tag losses occur on only `o(r)` unpaired
levels, telescope against endpoint reservoirs at the other levels, or are
absorbed by recursively exposed internal pocket complexes.  Paying
`2^{Theta(r)}` independently at `Theta(r)` levels would still lose a leading
quadratic term.

The strongest local version of that proposal is now known to be equivalent
to the original problem.  Projectively embed an arbitrary `N`-point order
type `Q` as one strict fixed-edge insertion chain.  Every
`h=floor(log_2N)` subset of the chain, in chain order, is a valid monotone
repair history with the same outer frame and terminal hull.  Hence there are

\[
                 {N\choose h}=2^{(1-o(1))(\log_2N)^2}       \tag{23n8}
\]

histories.  Adjoining the fixed base and terminal tip changes the ordinary
face count by only a constant factor.  A map of (23n8) into two ordinary
faces with fibre `2^{o((log N)^2)}` therefore implies
`log V(Q)>=(1/2-o(1))(log N)^2`; conversely that lower bound gives an
enumerative pair code.  Thus an unrestricted two-face long-chain decoder is
coefficient-scale equivalent to Erdős 838, not a simpler intermediate
lemma.  See `agent_label_faithful_decoder/LAYERED_CHAIN_LABEL_LOSS.md` and
`agent_recursive_pocket_induction/LONG_CHAIN_MIXED_BRANCH_BARRIER.md`.

The same examples kill several weaker variants.  One protected Boolean
prefix bank cannot be re-used at every comparable layer; two arbitrary
faces from the internal pocket still miss a quadratic history exponent
when the depth exponent exceeds the pocket-size exponent; and summing all
pair-of-level reservoirs adds only a polynomial factor.  The extra capacity
must use the retained outer component and the internal pocket jointly.

Literal retained-outer coexistence is also too strong.  In the universal
chain wrapper, every transition has the full ACP form
`A=(T-p) union I` with a common outer core and outward successor, but any
convex output retaining both tangent guards contains at most one pocket tip.
Requiring both outputs to retain the guards leaves a
`2^{(1-o(1))L^2}` fibre; retaining one guard or splitting the two guards
between the outputs still leaves `2^{(1/2-o(1))L^2}` on the sharp family.
Allowing a quadratic-entropy family of outer cores does not help when each
output literally recovers its core: the outer-family factor cancels.  Thus a
coefficient-scale ancestor telescope must release both guards at universal
chain states and recover the erased outer information elsewhere.  This is a
barrier only for uncapped full histories; (18a) explains why it disappears
for top-window capped records.  See
`agent_stacked_outer_pocket/STACKED_OUTER_POCKET_BARRIER.md`.

After imposing the actual incidence cap, even the linear-codimension
fixed-core chain is harmless.  An immediate repair
`B+x_i -> B+x_j` injects into the ordinary two-face `{x_i,x_j}`.  Two
successors of the same state map with load two to
`(B,{x_i,x_j,x_k})`.  More generally, all ordered pairs of *distinct actual
incidences* sharing a core `B` have a congestion-one code `(B,F_X)`: the
universal coefficient-`1/4` lower bound makes the pocket face codebook
`V(X)` larger than the square of its `O(N^2)` simple arrow set.  Thus every
cap `d<=N`, including `d=n^(1-alpha)`, is closed for a fixed/common outer
core in the global ordinary-face/EIC telescope.  The codebook is
existential and need not lie in a narrower per-incidence local RPH
neighbourhood.  The surviving linear-codimension obstruction must involve
`2^{Omega(r^2)}` genuinely different outer cores whose pocket codebooks are
reused while mixed core--pocket faces are suppressed.  This exact
cross-core boundary is proved and audited in
`agent_linear_codim_capped/LINEAR_CODIM_CAPPED_CHAIN.md`.

There are two important scale corrections to that statement.  First, at the
weak leading-coefficient scale an ordered cross-core pair can always be sent
back to its two actual source faces with fibre at most `d^2=2^{O(r)}`.  This
is already `2^{o(r^2)}` and therefore contains no crossing-core geometry at
all; it is **not** useful for EIC, whose required congestion is
`2^{o(r)}`.  Second, if one deletes `t` source labels while retaining the
insertion edge, the exact proper-downshadow Hall congestion is

\[
 K_t\le \left\lceil {d\Lambda_t\over {r\choose t}}\right\rceil,
                                                               \tag{23n0}
\]

where `Lambda_t` is the maximum global prefix multiplicity.  For
`r=(alpha+o(1))log n`, local source symbols are insufficient when
`alpha<1/2`; when `alpha>=1/2`, the entire issue is the heavy global prefix
reuse.  A rational planar family shows that every fixed-codimension
source-downshadow map can have quadratic congestion even after guard
deletion.  Its complete released lower arc is convex and pays globally, so
this is again an architectural barrier rather than an EIC counterexample.
See `agent_linear_codim_capped/CROSS_CORE_DOWNSHADOW.md`.

The strongest local crossing-core obstruction is now also explicit.  There
are `2^{Theta(r^2)}` distinct rank-`r` cores, one common strict insertion
chain, and a genuine simple linear-codimension selector such that every
record-local face containing the two incidence tips must erase an entire
`Theta(r)`-point side of its own core.  The local inverse fibre is therefore
`2^{Theta(r^2)}` even for ordered pairs based at different cores, and
deleting `o(r)` guards does not help.  However the two shield clouds are
themselves in convex position and supply an exponentially larger unrestricted
face bank.  The exact surviving theorem is consequently global:

\[
 \boxed{\text{mixed core--pocket product, or charge the released shield
 face complex.}}                                             \tag{23n0a}
\]

This construction and its exact capped audit are in
`agent_quadratic_cross_core/QUADRATIC_CROSS_CORE_SHIELD.md`.

At singleton terminal states there is a complementary exact C4 theorem.
Two sources `R_A+x,R_B+y` repaired by common blockers `p,q` splice forward
whenever `R_A+p+y` and `R_B+q+x` are faces; the resulting two-face map has
global fibre at most `2(r+1)^4`.  Summing over all states gives the exact
forward-pair bound

\[
 \sum_\sigma\bigl(|C_A(\sigma)||C_B(\sigma)|
             -|C_A(\sigma)\cap C_B(\sigma)|\bigr)
       \le (r+1)^4V(P)^2 .                            \tag{23o}
\]

Otherwise a positive fraction of blockers rotates into a new repair step.
Exterior rotations strictly enlarge the hull and cannot cycle.  Moreover a
rank-`k` rotation chain `T_0,...,T_m` releases

\[
 \left|\bigcup_i2^{T_i}\right|\ge2^k+m2^{k-1},        \tag{23p}
\]

because every new exterior tip marks `2^{k-1}` previously unseen subfaces.
Exact counterexamples show that two failed cross-splices need not make the
targets comparable, even after one rotation; the recursion must retain its
two-dimensional tangent state.  Thus (23o)--(23p) settle forward terminal
rectangles and individual rotation chains, while global reuse among many
nested chains remains the live gate.

Two broader all-interval statements are now known to be false.  A
ramp--plateau--ramp full product has only a polynomial excess of source
downfaces plus *all* atomic two-ended interval faces, while its capped demand
is exponential.  Even enriching each block by scalar `C_i,U_i,V_i` does not
repair the claim: an exact cap/cup-gradient profile cancels every forward
interval despite large `C_iU_i`.  The correct state must retain the full
two-dimensional tangent distributions or recursively spend the internal
face complex.  The exact vector recurrence and one-level dominance split
are in `agent_all_interval_isoperimetry/REPORT.md`; iterating its dyadic
one-level reset without (23i)'s repair correlation still loses too much.

The unit reflection-order matrix route has an independent exact
localization.  On the strict lower triangle, normalize the squared forward
and reverse endpoint counts to laws `p_t,q_t`.  Their Frobenius angle is
exactly the Hellinger affinity, so

\[
 \log {Q(1)\over Q(1/2)}
 =\frac12\log {E_A(1)E_B(1)\over E_A(1/2)E_B(1/2)}
  -\frac12\bigl(D_{1/2}(p_1\Vert q_1)
                    -D_{1/2}(p_{1/2}\Vert q_{1/2})\bigr).   \tag{23q}
\]

Thus the missing datum is precisely the cross-activity Renyi-alignment
drift.  For an endpoint interval of span `s`, reflection betweenness gives
the coefficientwise cap

\[
             G_{ij}(t)\preceq t^2(1+t)^{s-1}.                \tag{23r}
\]

There is now an exact cellwise recursion behind this cap.  Writing
`a=t+A`, `b=t+B`, one has

\[
       G=t^2+t(A+B)+AB,
\]

where `AB/t^2` is itself a convex trace family in the open interval.  More
generally `C_ij(t)=G_ij(t)/t^2` injects coefficientwise into the full open
interval face polynomial.  If `Z_ij=4G_ij(1/2)`, `m=j-i-1`, and `u_ij` is
the half-weighted trace mean, entropy gives

\[
 \log Z_{ij}+u_{ij}\le m h_2(u_{ij}/m),\qquad
 {G_{ij}(1)\over G_{ij}(1/2)}\ge2^{2+u_{ij}}.              \tag{23r1}
\]

Consequently, with `r_(1/2)` the half-activity endpoint law,

\[
 {Q(1)\over Q(1/2)}\ge
 \sum_{i<j}r_{1/2}(i,j)
 2^{2+\psi_{j-i-1}(4G_{ij}(1/2))}.                        \tag{23r2}
\]

This is a concrete Bellman target rather than a spectral heuristic.  Its
only unproved step is charging the open-interval traces: the same interior
face can be offered to many outer endpoint cells.  Also, `AB` occupies a
large fraction of the exact adversarial test mass, while a one-sided cell
has one polynomial identically equal to `t`; in that case `ij` is a hull
edge of the full interval.  The alternating stretchable family is
one-sided in every cell and has quadratically many crossing homogeneous
intervals, so abundance or crossing of interval edges alone does not solve
the reuse problem; their signs must be coupled.

A tempting Baek--Balko-style repair of that reuse is now ruled out
quantitatively.  Suppose each endpoint is assigned a distinct integer
Ferrers downset and its area is charged to the endpoint rectangles.  If
`A_N` is the minimum total area of `N` distinct finite downsets, then the
partition generating function and the distinct-parts construction give the
sharp scale

\[
                         A_N=\Theta\!\bigl(N(\log N)^2\bigr).       \tag{23r2z}
\]

Thus even a perfect injective state labelling yields only

\[
 \sum_{u<v}R_{uv}(1)B_{uv}(1)
       \ge\Omega\!\bigl(n(\log n)^2\bigr),                       \tag{23r2z1}
\]

which is weaker than the automatic `Theta(n^3)` contribution of ranks at
most three.  Worse, distinctness has no superlinear consequence at activity
one half.  The positive integer path polynomials

\[
                 P_j(t)=t+jt^N,\qquad Q_j(t)=t                   \tag{23r2z2}
\]

are distinct at `t=1`, while the total area of their rectangles at `t=1/2`
is `N/4+o(1)`.  This is an abstract polynomial barrier, not a simultaneous
reflection-order realization, but it proves that positivity, integrality,
and state injection do not imply the required cross-activity dilation.  The
genuine reflection-order interpolation can nevertheless be determined
exactly.  Shortcutting a temporal path preserves its direction, so its
internal-vertex supports form a Boolean downset.  For every downset
`mathcal L` and `0<h<=1`, induction on a label gives

\[
 \sum_{S\in\mathcal L}h^{|S|}
       \ge|\mathcal L|^{\log_2(1+h)}.                         \tag{23r2z3}
\]

Consequently, with `alpha=log_2(3/2)`, every genuine endpoint cell satisfies

\[
 P_{uv}(1/2)\ge\tfrac12P_{uv}(1)^\alpha,
 \qquad G_{uv}(1/2)\ge\tfrac14
       \{R_{uv}(1)B_{uv}(1)\}^\alpha.                       \tag{23r2z4}
\]

This exponent is sharp on a stretchable all-cup order.  Even combining
`(23r2z4)` with `(23r2z)` forces only

\[
                 \Omega\!\bigl(n(\log n)^{2\alpha}\bigr)     \tag{23r2z5}
\]

half-activity mass, again below the universal low-rank baseline.  Thus the
live Coxeter input must couple *different* cells or vertices across
activities, or provide many independently decoded states per endpoint.  See
`agent_coxeter_global_half/DOWNSET_ACTIVITY_BARRIER.md`.

Common endpoints and nested intervals do not provide that coupling.  In a
generic rational strict-cup order, every interval with `d` internal labels
has simultaneously

\[
 R_{uv}(t)=t(1+t)^d,\qquad B_{uv}(t)=t,                    \tag{23r2z6}
\]

so `(23r2z4)` is equality in every cell.  At a fixed right endpoint `v` the
activity-one rectangles are totally nested, yet

\[
 |D_v|=2^{v-1},\qquad
 \sum_{u<v}G_{uv}(1/2)=\tfrac12\{(3/2)^v-1\}.            \tag{23r2z7}
\]

Hence every exponent larger than `alpha` fails exponentially even with a
subexponential loss, both for a shared endpoint and for a fully nested
interval chain.  The family is harmless globally because

\[
 F_n(t)=(1+t)^n,\qquad H(P_n)=n(3/4)^n.                   \tag{23r2z8}
\]

Thus the needed alternative is now exact in kind: local saturation must be
charged to an *unweighted* face bank; no universally stronger half-activity
endpoint inequality exists.  See
`agent_coxeter_global_half/SHARED_ENDPOINT_SATURATION_BARRIER.md`.

The exact cellwise saturation--bank dichotomy is now proved.  For an
endpoint cell $e=(u,v)$ let $x_e,y_e$ be the two temporal-path counts,
$r_e,s_e$ their maximum internal support ranks, and put

\[
 X_e=x_ey_e,\qquad B_e=2^{r_e+s_e},\qquad
 \Delta_e=\log_2{4G_e(1/2)\over X_e^\alpha}.
\]

The active coordinates of the forward and reverse path downsets partition
the open endpoint interval.  Maximum supports are disjoint, and their two
shortcut cubes therefore give $B_e$ distinct ordinary faces with minimum
$u$ and maximum $v$.  In particular these banks are disjoint for distinct
endpoint pairs.  The rank-refined downset inequality

\[
 \sum_{S\in\mathcal L}2^{-|S|}
 \ge \Phi(m,r):=m2^{-r}-1+(3/2)^r                         \tag{23r2z9}
\]

then gives the exact structural companion to `(23r2z4)`:

\[
 \boxed{4G_e(1/2)B_e\ge X_e,\qquad
 B_e\ge X_e^{1-\alpha}2^{-\Delta_e}.}                 \tag{23r2z10}
\]

Thus for every threshold $D$, either the half-activity baseline improves by
$2^D$, or the cell supplies the load-one ordinary bank
$2^{-D}X_e^{1-\alpha}$.  Zero defect is rigid: both path downsets are full
cubes on complementary coordinates, so the cell contains all
$2^{v-u-1}$ endpoint subsets.  The product tradeoff is sharp.  Alternating
stretchable signs have linear shortcut codimension but only constant
defect while $B_e=\Theta(X_e)$; a one-exception stretchable family has
$B_e=2$ and $4G_e(1/2)B_e/X_e\to1$.  Hence the remaining Coxeter operation
is genuinely global amplification or recycling of these disjoint
endpoint-indexed banks, not a stronger local interpolation inequality.  See
`agent_coxeter_global_half/SATURATION_BANK_DICHOTOMY.md`.

Direct globalization of `(23r2z10)` is now exhausted.  For a cell class
$\mathcal C$, write

\[
 S_X=\sum_{e\in\mathcal C}X_e,qquad
 S_G=\sum_{e\in\mathcal C}G_e(1/2),qquad
 S_B=\sum_{e\in\mathcal C}B_e.
\]

Bank disjointness and Cauchy give the exact aggregate inequalities

\[
 S_X\le4\sum_eG_eB_e,qquad
 \left(\sum_e\sqrt{X_e}\right)^2\le4S_GS_B,qquad
 S_B\le F_R(1)-1-n.                                    \tag{23r2z11}
\]

Their direction is wrong for the target.  Indeed
$d_e=X_e/(4G_e)$ satisfies only $1\le d_e\le B_e$, whereas the desired
dilation is the $G$-weighted average of $d_e$ and disjointness controls an
unweighted sum of its upper bounds.  This failure is sharply stretchable.
For the sign order $\chi(i,j,k)=+1$ when $i=0$ and $-1$ otherwise, the
common-left fan $\mathcal W_n=\{(0,v):1\le v<n\}$ has

\[
 S_X={n(n-1)\over2},\qquad
 S_G={(n-1)(n+2)\over16},\qquad
 S_B=2n-3,                                               \tag{23r2z12}
\]

and

\[
 4\sum_{e\in\mathcal W_n}G_eB_e=S_X+n-2,qquad
 {nS_G\over S_X}={n+2\over8}.                            \tag{23r2z13}
\]

Thus even one nested endpoint fan asymptotically saturates the summed local
tradeoff while having a linear bad normalized ratio.  The full order is
harmless only because the complementary vertices $1,\ldots,n-1$ form a
strict cap and contribute $2^{n-1}$ ordinary faces.  The exact surviving
operation is therefore a **cross-endpoint/complementary-vertex charge**;
same-cell multiplication or any separable sum over a localized cell class
cannot work.  The saved 58-wire adversary exercises precisely this branch:
cells of bank dimension at most six carry $86.5483\%$ of half mass and have
restricted normalized statistic $2.101946$, while the selected banks are
only $5.211\%$ of its nontrivial faces.  See
`agent_coxeter_global_half/GLOBAL_BANK_AMPLIFICATION_BARRIER.md`.

The complementary-vertex payment can now be forced exactly for every
sign-coherent rooted fan.  Let $p$ be the common root, let $W$ be its $m$
ordered neighbours with
$\chi(p,w_i,w_j)=\sigma$, and write $T_\sigma(W)$ for the number of triples
of $W$ having sign $\sigma$.  Each such triple is a distinct rooted
four-face, because it is precisely a two-internal temporal support in the
rooted endpoint fan.  On the other hand the $\sigma$-triples form a
3-uniform hypergraph, and independent sampling followed by deletion gives

\[
 \alpha(\mathcal H_\sigma)\ge
       \max_{0\le q\le1}\{qm-q^3T_\sigma(W)\}.          \tag{23r2z14}
\]

Every independent set is an opposite-sign cap or cup.  Consequently, for
every integer $1\le L\le m/2$,

\[
 \boxed{T_\sigma(W)>{m^3\over8L^2}\quad\hbox{or}\quad
        W\text{ contains an external Boolean face bank of size }2^L.}
                                                               \tag{23r2z15}
\]

This recovers the full $2^m$ payment in the one-exception fan directly from
packet signs.  It is also the sharp limit of a single complementary-bank
argument.  Take the classical rational $E(k,k)$ set

\[
 m={2k-4\choose k-2}                                   \tag{23r2z16}
\]

and add a root coherent with its majority triple sign.  Then at least
$\binom m3/2$ rooted four-faces are promoted, but every homogeneous bank has
rank below $k$, every complementary convex bank has rank at most $2k-4$,
and every rooted cell bank has rank at most $2k-5$.  Since

\[
                         2^{2k-4}\le(2k-3)m,             \tag{23r2z17}
\]

each individual bank is only $m\,O(\log m)$ against cubic promoted mass.
Thus the cross-endpoint compensation theorem is real, but its dense branch
requires a multi-bank Hall decoder or a controlled higher-rank iteration;
Ramsey extraction of one complementary bank cannot finish the half-weight
target.  Exact rational $E(k,k)$ realizations through $k=6$ audit both the
promotion and this barrier.  See
`agent_coxeter_global_half/ROOTED_FAN_COMPLEMENT_DICHOTOMY.md`.

The same obstruction persists at the full temporal-history scale.  For a
coherent root $p$ over $W=E(k,k)$, deletion of $p$ is a rank-preserving
bijection between all rooted temporal histories and the nonempty cups of
$W$.  If $U_{k,k}(t)$ is their generating polynomial, then

\[
                         Q_p(t)=tU_{k,k}(t).             \tag{23r2z18}
\]

This is quasipolynomial history mass, not merely the polynomial rank-four
coefficient.  Even an arbitrary fractional Hall routing of demand
$nQ_p(1/2)$ into the union of **all** homogeneous cup and cap outputs has
full-cut load

\[
 \Lambda\ge {nU_{k,k}(1/2)\over4U_{k,k}(1)}
 \ge {\sqrt m\over8\sqrt{2k-3}}
 =m^{1/2-o(1)},
 \qquad m={2k-4\choose k-2}.                            \tag{23r2z19}
\]

Indeed every cup has rank below $k$, so

\[
 U_{k,k}(1/2)\ge2^{-(k-1)}U_{k,k}(1),\qquad
 2^k\le4\sqrt{(2k-3)m}.                                \tag{23r2z20}
\]

The separated recursion

\[
 C_{A\prec B}=C_A(1+|B|t)+C_B,\qquad
 U_{A\prec B}=U_A+U_B(1+|A|t),\qquad
 V_{A\prec B}=V_A+V_B+C_AU_B                         \tag{23r2z21}
\]

shows where the missing capacity actually lies: the mixed cap--cup banks,
not any homogeneous subface or maximum-extension bank.  Thus every
one-sign/Ramsey/same-type history decoder is now excluded even with optimal
fractional routing.  Global overlap of an already compatible mixed pair is
handled by `(23r2g)`--`(23r2i)`; the remaining Coxeter operation is the
**local profile contraction** which forces a coherent one-sided history to
supply a compatible opposite-sign/two-tangent partner.  Mixed-bank capacity
has enormous slack, but capacity alone does not produce that partner.  Exact
rational geometry through $k=6$ and polynomial recurrences through $k=20$
verify the statement.  See
`agent_coxeter_global_half/WEIGHTED_ROOTED_HISTORY_HALL_BARRIER.md`.

Even the local mixed-bank forcing is false history by history.  In the
classical separated recursion for $P_k=E(k,k)$, the left-spine subconfiguration

\[
 S_k=E(k,3),\qquad |S_k|=k-1,                            \tag{23r2z22}
\]

is a strict cup and is inclusion-maximal among **all** ordinary faces of
$P_k$.  Indeed, on climbing one level $A\prec B$, any mixed extension would
force the $A$-trace containing $S_k$ to be a cap, contradicting any positive
triple of $S_k$.  Therefore

\[
 F\in\mathcal V(P_k), S_k\subseteq F
                 \quad\Longrightarrow\quad F=S_k.       \tag{23r2z23}
\]

After adjoining a coherent positive root $p$, the set
$H_k=\{p\}\cup S_k$ is a genuine rank-$k$ temporal history of weight
$2^{-k}$.  Any label-retaining fractional decoder, even into all recursive
mixed cap--cup banks and with polynomially many trace marks, has only the
single underlying target $S_k$.  Hence

\[
 \Lambda\ge {m+1\over2^k}
       \ge {\sqrt m\over4\sqrt{2k-3}}
       =m^{1/2-o(1)},
 \qquad m={2k-4\choose k-2}.                            \tag{23r2z24}
\]

Thus local opposite-sign forcing is decisively false.  The exact surviving
interface is to pool or telescope terminal-history demand before decoding,
or to erase/replace labels while providing an independently bounded recovery
code.  Exact rational $E(k,k)$ geometry through $k=6$ verifies the terminal
cup and zero-extension statement; the load is audited symbolically through
$k=40$.  See
`agent_coxeter_global_half/MAXIMAL_CUP_HISTORY_MIXED_BARRIER.md`.

Label replacement in fact passes this sharp stress family with fibre one.
Use the top split

\[
 P=E(k,k)=A\prec B,\qquad
 A=E(k,k-1),\quad B=E(k-1,k),\quad
 m={2k-4\choose k-2},\quad n=m+1,                       \tag{23r2z25}
\]

and let $\mathcal M$ be all unions of a nonempty cap of $A$ and a
nonempty cup of $B$.  If $W_k=C_{k,k-1}(1)=U_{k-1,k}(1)$, then
$|\mathcal M|=W_k^2$.  Give every coherent-root cup history $S$ demand
and integer token count

\[
 d(S)={n\over2^{|S|+1}},qquad q(S)=\lceil d(S)\rceil. \tag{23r2z26}
\]

The exact separated recurrence proves, for every $k\ge5$,

\[
 \boxed{W_k^2\ge\sum_{S\in\mathcal U(P)}q(S)}.         \tag{23r2z27}
\]

For $5\le k\le15$ this is checked directly.  Uniformly thereafter, one
recursion path gives
$W_k\ge2^{(k-3)(k-2)/2}$, while all histories require at most
$3\cdot4^{k-1}m^2W_k$ tokens, which is at most $W_k^2$ for $k\ge16$.

Order histories and top mixed faces lexicographically and assign history
$S$ the next private block of $q(S)$ faces, placing flow
$d(S)/q(S)\le1$ on each.  The unique top split recovers the cap--cup pair,
its global index recovers its block, and the block recovers $S$.  Hence

\[
 \boxed{\text{output load}\le1,\qquad
        \text{history-recovery fibre}=1.}              \tag{23r2z28}
\]

In particular the maximal terminal cup $E(k,3)$ receives
$\lceil n/2^k\rceil$ private mixed codewords despite having no ordinary
extension.  At $k=5$, exact rational geometry enumerates 1,281 histories,
10,201 mixed faces, and 2,331 used codewords; symbolic verification runs
through $k=40$.  Thus $E(k,k)$ is a barrier to label retention but not to
replacement.  The remaining gate is to construct such a canonical
allocation for an arbitrary reflection order and to control reuse when
different root/endpoint codes draw from the same global mixed reservoir.
See
`agent_coxeter_global_half/LABEL_REPLACING_ES_MIXED_CODE.md`.

The global assembly part of that extension is now exact.  For a genuine
two-sided trace cell $a$, let $\mathcal H_a$ be its weighted histories,
$\Gamma_a(H)$ the compatible ordinary mixed outputs, and give $H$ demand
$D w(H)$.  A fractional local decoder of output load $\lambda$ exists if
and only if every history subfamily satisfies weighted Hall:

\[
 \boxed{D\sum_{H\in X}w(H)
 \le\lambda\left|\bigcup_{H\in X}\Gamma_a(H)\right|
 \quad(X\subseteq\mathcal H_a).}                       \tag{23r2z29}
\]

Recovery fibre is a separate requirement.  In the complete-reservoir
case, the stronger scalar capacity
$|\mathcal B_a|\ge\sum_H\lceil Dw(H)\rceil$ gives the lexicographic
private-block code with local load and fibre one.

Superpose local decoders.  If $\delta(F)$ is the number of reservoirs
containing the ordinary face $F$, then exactly

\[
 \operatorname{load}(F)\le\lambda\delta(F),\qquad
 \operatorname{fibre}(F)\le\rho\delta(F).              \tag{23r2z30}
\]

For the actual rooted-diagonal reservoirs this incidence is controlled by
the output itself.  If $F=\{v_1<\cdots<v_r\}$, nonempty histories on both
sides force its retained trace to be $v_iv_{i+1}$ with
$2\le i\le r-2$.  Consequently

\[
 \boxed{\delta(F)\le r-3,\qquad
 \sum_aL_{a,r}\le\lambda(r-3)v_r(P).}                  \tag{23r2z31}
\]

An alternating rational convex $r$-gon belongs to all $r-3$ such banks,
so the factor is sharp.  Hence any local $n^{o(1)}$-load and
$n^{o(1)}$-fibre trace code globalizes at live rank $O(\log n)$ with only
$n^{o(1)}$ loss.  Global mixed-face reuse is no longer open.

The ownership condition matters.  If $q$ coherent roots sit over one
complement and independently use its same unmarked mixed bank, one face
has

\[
                             \delta(F)=q.               \tag{23r2z32}
\]

Thus root-indexed private codes cannot simply invoke the trace bound; they
must be jointly Hall-allocated or first assigned to trace-owned subbanks.
The sole substantive reflection-order gate is now local: prove the
weighted-Hall condition (23r2z29) plus low-fibre recovery for each
two-tangent profile contraction, or prove the corresponding joint-root
Hall expansion.  See
agent_coxeter_global_half/ABSTRACT_MIXED_HALL_ASSEMBLY.md.

The local Hall hypothesis itself is sharply false.  For every $m$ there is
a rational stretchable matching star with one trace $j<l$, left apices
$x_1,\ldots,x_m$, and right apices $y_1,\ldots,y_m$ such that

\[
 \boxed{\{x_i,j,l,y_k\}\text{ is convex}
        \Longleftrightarrow i+k=m+1.}                  \tag{23r2z33}
\]

The full two-tangent neighbourhood of the rank-three history
$H_i=\{x_i,j,l\}$ is its single matching quadrilateral: any higher
opposite history would delete to two singleton neighbours.  With ambient
size $N=2m+2$ and half-activity weight $1/8$, the singleton Hall cut is

\[
                         \lambda\ge N/8=\Theta(N),      \tag{23r2z34}
\]

and equality is attained.  Thus natural mixed compatibility cannot satisfy
the required local $N^{o(1)}$ expansion even at constant rank.

There is an exact local alternative.  Orient the complete graph on the
left apices as a balanced tournament and let each apex own its singleton
and its outgoing pairs.  Each $x_i$ owns at least

\[
 1+\left\lfloor{m-1\over2}\right\rfloor
 \ge\left\lceil{N\over8}\right\rceil                  \tag{23r2z35}
\]

disjoint rank-one/two ordinary side faces.  They give a fibre-one,
load-one replacement code for $H_i$ relative to the known trace cell.
The right side is identical.

But this code erases the trace.  In the $|J||L|$-trace version of the same
construction, every trace offers the same owned side blocks, so an
unmarked side face has reuse

\[
                              |J||L|.                  \tag{23r2z36}
\]

The reflection-order residue has therefore moved again: mixed trace-owned
codes globalize by (23r2z31), while every local failure has a cheap
detached-side code whose *cross-trace ownership* must be jointly allocated
or telescoped.  See
agent_coxeter_global_half/LOCAL_TRACE_HALL_MATCHING_BARRIER.md.

The cross-trace allocation question has an exact rank threshold on that
stress family.  In the balanced \(q=m\) matching star there are \(2m^3\)
rank-three cell histories, each with demand \(m/2\), so total demand is
\[
                             D_{\rm tot}=m^4.           \tag{23r2z37}
\]
The complete detached rank-at-most-two side bank has only \(m(m+1)\)
faces.  Hence even a fully joint fractional decoder has
\[
 \lambda\ge {m^3\over m+1}=\Theta(N^2);                 \tag{23r2z38}
\]
allowing every ambient rank-at-most-three face still forces
\(\lambda\ge N/256\).  Thus no ownership rule or recovery trick confined
to ranks one through three can telescope this family with subpolynomial
load.

Pooling all record demands *before* assigning outputs supplies the sharp
repair.  If a common ordinary bank \(\mathcal B\) satisfies
\[
 L|\mathcal B|\ge\sum_h\lceil d_h\rceil,                \tag{23r2z39}
\]
lexicographic block allocation gives physical output load and recovery
list at most \(L\); for \(L=1\) the recovery fibre is one.  Since each side
cloud of the matching star is homogeneous, its rank-four bank satisfies
\[
 14\!\left(2\binom m4\right)\ge
 2m^3\left\lceil{m\over2}\right\rceil\qquad(m\ge47),    \tag{23r2z40}
\]
giving load/list at most \(14\).  Rank five satisfies the same inequality
with \(L=1\) for \(m\ge70\).  The block index recovers the side, both trace
endpoints, and the apex, so no external trace mark is being hidden.

The same joint code passes the other sharp stress.  If \(q\le m\) coherent
roots share an \(E(k,k)\) complement, then for every \(k\ge7\) its single
top mixed bank satisfies the full pooled demand and gives
\[
             \boxed{\text{load}=1,\qquad\text{fibre}=1} \tag{23r2z41}
\]
simultaneously for all roots, including terminal maximal cups.  Consequently
the local residue is no longer cross-trace bookkeeping: one must prove that
an arbitrary reflection order exposes enough bounded-rank detached or
mixed physical bank capacity, or else charge the absence of that capacity
to its ordinary-face profile.  See
`agent_coxeter_global_half/JOINT_DETACHED_BANK_RANK_PROMOTION.md`.

In fact the rank-four repair is universal for literal rank-three histories,
not a feature of the matching-star side clouds.  Every five planar points
contain a convex four-set, so double counting gives
\[
                         v_4(P)\ge{1\over5}\binom n4.    \tag{23r2z42}
\]
There are at most \(\binom n3\) literal rank-three histories, each with
half-activity demand \(n/8\).  Since
\[
 {\binom n3\lceil n/8\rceil\over v_4(P)}
 \le {20\lceil n/8\rceil\over n-3}\le10,               \tag{23r2z43}
\]
one global lexicographic block allocation into the ordinary convex
quadrilaterals has output load and recovery list at most ten.  Pooling
literal ranks one through three together gives the same conclusion with
universal factor \(80\).  No local compatibility is used: the output's
global bank index is the replacement code.  Thus every constant-rank
matching-star-type Hall failure is already closed once all histories are
pooled.  The surviving interval is growing rank below \(\log n\), or
nonliteral multiplicity not controlled by physical support.  See
`agent_coxeter_global_half/GLOBAL_RANK_THREE_ES4_REPLACEMENT_CODE.md`.

The same pooled construction reaches genuinely growing rank.  With
\(t_r=ES(r+1)\le4^r+1\), double counting gives
\[
 v_{r+1}(P)\ge{\binom n{r+1}\over\binom{t_r}{r+1}}.     \tag{23r2z44}
\]
Hence all literal rank-\(r\) histories have a joint replacement code of
load/list
\[
 L_r\le1+{4(r+1)\over2^r}\binom{4^r+1}{r+1}
      =2^{O(r^2)}.                                      \tag{23r2z45}
\]
Pooling all \(r\le R=o(\sqrt{\log n})\) costs only \(n^{o(1)}\), whereas
for \(r\ge\log n\) the identity output already has load
\(n2^{-r}\le1\).  Therefore the direct global-bank method narrows the
literal-history gap to
\[
                 \Omega(\sqrt{\log n})\le r<\log n.     \tag{23r2z46}
\]

That exactly-one-sided branch is now closed.  If every endpoint interval is
one-sided, write `s_(ik)` for its common triple sign.  The four-point law

\[
        s_{ac}=s_{bd}\quad\Longrightarrow\quad s_{ad}=s_{ac}
                                                               \tag{23r2a}
\]

identifies the sign system with a `2413,3142`-avoiding permutation of the
adjacent gaps, hence with a signed reduced Schroeder tree; every such system
is rationally stretchable.  If `p,q` are the largest cup and cap sizes, the
shared-pivot induction gives

\[
                  (p-1)(q-1)\ge n-1.                    \tag{23r2b}
\]

Thus one of those convex chains has size at least `1+sqrt(n-1)` and

\[
                       V(P)\ge2^{1+\sqrt{n-1}},           \tag{23r2c}
\]

far beyond the target.  The statement is stable.  If `B` endpoint pairs
are two-sided, Caro--Wei leaves a one-sided core of size at least
`n^2/(n+2B)`.  Since every two-sided cell has
`A_(ik)(1/2)B_(ik)(1/2)>=1/16`, putting

\[
                 E=\sum_{i<k}A_{ik}(1/2)B_{ik}(1/2)
\]

gives

\[
       \log_2V(P)\ge1+\sqrt{{n^2\over n+32E}-1}.          \tag{23r2d}
\]

In particular `E<=n^2/(8(log n)^4)` already proves coefficient one half.
Any unresolved reflection-order configuration must therefore carry a
global two-sided product mass larger than this threshold.  See
`agent_one_sided_reflection/ONE_SIDED_SCHROEDER_TREE.md`.

The complementary dense branch already forces a concrete rank-four star.
Let `r_(ik),s_(ik)` count the intermediate labels on the two sides of chord
`ik`, and let `B` again be the number of pairs with both counts positive.
The coefficient

\[
 T=\sum_{i<k}r_{ik}s_{ik}
    =[t^4]\sum_{i<k}A_{ik}(t)B_{ik}(t)
\]

counts exactly the convex quadrilaterals whose `x`-extreme chord is a
diagonal, with their two-point peeled trace.  Packing the `B` intervals by
length gives

\[
        T\ge {B^2\over2n},\qquad
        E\ge {T\over16}\ge {B^2\over32n}.               \tag{23r2e}
\]

Double counting the peeled pairs then yields some two-point face with

\[
            d(j,l)>{2T\over n^2}\ge {B^2\over n^3}.     \tag{23r2f}
\]

Thus the live residue `B>2n^2/(log n)^4` contains a fixed rank-two trace
with more than `4n/(log n)^8` mixed endpoint extensions, and in fact
`E=Omega(n^3/(log n)^8)`.  This extraction is sharp but not itself a shield:
two arbitrary order types can be compressed on opposite sides of one fixed
trace so that **every** cross pair extends it to a convex quadrilateral.
Even a complete rooted `I times K` grid therefore need not release either
detached cloud.  Higher path compatibility or repeated trace layers remain
essential.  See
`agent_one_sided_reflection/DENSE_TWO_SIDED_TRACE_EXTRACTION.md`.

The higher-history compatibility and its global reuse are now exact.  Fix a
trace `j<l`.  A rooted convex face `X` on one side is summarized, for gluing
purposes, by only its two neighbours `tau_j(X),tau_l(X)` at the root edge;
define the analogous pair for an opposite rooted face `Y`.  If `t(x,y)` is
the coordinate where the line `xy` meets the directed root line `jl`, then

\[
 X\cup\{j,l\}\cup Y\text{ is convex}
 \quad\Longleftrightarrow\quad
 t(\tau_j(X),\tau_j(Y))>0,
 \quad t(\tau_l(X),\tau_l(Y))<1.                    \tag{23r2g}
\]

Thus the full local bank is the exact two-dimensional dominance contraction

\[
 H_{jl}^{\sigma}(z)=z^2\!
 \sum_{p,q,r,s}M^\sigma_{p,q}(z)N^{-\sigma}_{r,s}(z)
 \mathbf1[t(p,r)>0]\mathbf1[t(q,s)<1].              \tag{23r2h}
\]

Summing over every trace has no hidden exponential reuse.  A rank-`k` output
is counted exactly once for each consecutive-in-x pair which is its diagonal,
and hence

\[
 \sum_{j<l,\sigma}[z^k]H_{jl}^{\sigma}(z)
 \le(k-1)v_k(P),
 \qquad
 \sum_{j<l,\sigma}[z^4]H_{jl}^{\sigma}(z)=T.         \tag{23r2i}
\]

The remaining reflection obstruction is therefore local, not a global
decoder problem: force growth of the two-tangent profile contraction beyond
its singleton layer, or charge one detached side complex with an aggregate
telescope.  This cannot follow from `T` alone.  For arbitrary `m,q` there is
a rational four-block configuration with `q^2` root traces, each having the
same `m` mixed extensions, while the outer compatibility graph is a perfect
matching.  No glued outer-cloud face then has rank above four.  Any successful
argument must use further side-profile labels or their ordinary face
complexes.  See
`agent_one_sided_reflection/ROOTED_DIAGONAL_AMALGAMATION.md`.

The local tangent-profile obstruction now has an exact Kraft reset.  For a
one-side cloud `Q` of size `m`, let `H` be the vertices visible from the
root edge and `I(H)` the hidden pocket inside its rooted hull.  Partitioning
all subsets of `Q` by their visible hull gives, coefficientwise,

\[
 (1+z)^m=\sum_H z^{|H|}(1+z)^{|I(H)|},
 \qquad
 \log_2R_Q(z)=\log_2(1+z)\,\mathbb E_\pi[m-|I(H)|]
              +D_2(\pi\Vert\rho).                       \tag{23r2j}
\]

Hence either the rooted-side polynomial is at least `K`, or one canonical
pocket retains more than `m-log_(1+z)K` labels.  At half weight the loss is
`log_(3/2)K`.  Moreover compatible visible hulls on opposite sides expose a
complete singleton grid in their hidden pockets:

\[
 H\cup K\cup\{u,v\}\text{ convex}
 \quad\Longrightarrow\quad |I(H)|\,|I(K)|\le d_{uv},    \tag{23r2k}
\]

where `d_(uv)` is the mixed singleton-extension degree.  The rooted spend
has exact global load one,

\[
 z^2\sum_{j<l,\sigma}\bigl(R^L_{jl,\sigma}(z)-1\bigr)
       =F_{\ge3}(P;z),                                   \tag{23r2l}
\]

and selecting one deepest pocket per directed side state costs at most
`4n^2F(P;z)`.  Taking spend thresholds of order `d^{1+epsilon}` therefore
forces either fixed-power rooted/higher-history mass or two explicit
near-full pockets.  If their size product exceeds `d`, their parents fail a
specific tangent guard; the reset moves both tangent coordinates strictly
toward compatibility and gives a ranked first-divergence child rather than
an unspecified cloud.  The remaining gap is iteration through those failed
guards: a child-pocket face need not coexist with its parent rooted hull, so
the spend/reset cannot yet be telescoped across potentially linear depth.
See `agent_one_sided_reflection/ROOTED_HULL_KRAFT_RESET.md`.

Strict tangent progress alone cannot repair that gap.  An arbitrary rational
child order type can be compressed behind a fixed root edge and wrapped by
`L` nested singleton ears `z_t`, each hiding the entire preceding pocket.
If `R_C` is the child's rooted polynomial, the wrapper has the exact profile

\[
                    R_t(s)=R_C(s)+ts,                    \tag{23r2m}
\]

while every nonempty child face `S` satisfies
`S union {u,v,z_t}` nonconvex.  Thus every reset has codimension one and
makes strict progress in both tangent ranks, yet every parent-child
coexistence product is literally empty.  In the first explicit wrapper the
discarded tips happened to form a strict cap and supplied

\[
                    V(\{z_0,\ldots,z_{L-1}\})=2^L.       \tag{23r2n}
\]

This Boolean payment is special, not structural.  Normalize the roots to
`u=(0,0),v=(1,0)` and write a lower point `z=(x,-h)` in tangent coordinates

\[
 A={x\over h},\qquad B={x-1\over h},
 \qquad z=\left({A\over A-B},-{1\over A-B}\right).       \tag{23r2o}
\]

This is one projective collineation, and

\[
 z_i\in\operatorname{int}\operatorname{conv}\{u,v,z_j\}
 \quad\Longleftrightarrow\quad A_i>A_j, B_i<B_j.        \tag{23r2p}
\]

Any rational planar order type can first be affinely placed with `A_i`
strictly decreasing and `B_i` strictly increasing, then sent through
`(23r2o)`.  Consequently the discarded tips of a full-pocket singleton reset
chain can have **exactly an arbitrary prescribed convex-subset complex**,
while the rooted profile is only `1+Ls` and every nonempty parent--child
coexistence union remains nonconvex.  A detached face `S`, with largest reset
index `m(S)`, has the exact chronology

\[
 \operatorname{mult}(S)=L-m(S),\qquad
 \sum_{t=0}^{L-1}V(Q_t)
 =L+\sum_{\varnothing\ne S\in\mathcal F(Z)}(L-m(S)).     \tag{23r2q}
\]

Thus even full-pocket containment, codimension-one steps, and strict motion
in both tangent ranks do not yield a standalone discarded-layer gain: that
claim is coefficient-equivalent to the original problem.  There is one exact
positive restriction.  At fixed roots both compatibility margins increase
monotonically under upper/lower resets, so each failed guard can heal once
and can never fail again; alternating left/right failures are impossible.
One guard can nevertheless remain failed through all `L` universal levels.
The next viable statement must therefore correlate **multiple reset chains**,
retain the terminal/source/repair law, or obtain a chronology-weighted
improvement unavailable to a face-only decoder.  See
`agent_one_sided_reflection/TANGENT_RESET_CHAIN_BARRIER.md` and
`agent_one_sided_reflection/SINGLETON_RESET_PROJECTIVE_UNIVERSALITY.md`.

Even synchronizing two chains with a common blocker alphabet does not rescue
a history-counted theorem.  The same projective construction can be placed
behind a fixed convex outer base `R` so that for every chain state `x` and
every later/common blocker `p`,

\[
 A=R\cup\{x\}\text{ is convex},\quad
 \operatorname{ext}(A\cup\{p\})=R\cup\{p\},\quad
 I=A-(R\cup\{p\})=\{x\}.                                \tag{23r2r}
\]

Thus every arrow is a genuine outward ACP repair and both chains can share
all terminal blockers, while the tip cloud retains an arbitrary prescribed
order type.  There are `D binom(N,h)` monotone length-`h` histories per chain,
but only `D(N_1+N_2)` distinct terminal repair incidences; chronology revisits
the same selected tuples.  For a fixed retained core the actual support has
the rank-two injection

\[
                    (R\cup\{x\},p)\longmapsto\{x,p\}.    \tag{23r2s}
\]

If retained cores vary and `Lambda=max_(x,p)#\{R:(R,x,p) in E\}`, then

\[
                              |E|\le\Lambda V(P).         \tag{23r2t}
\]

But a heavy fixed mark is stronger than `(23r2t)` suggests.  For all
singleton-ear records sharing one ear label `x`, target-only decoding has
load at most the target rank: given `T`, choosing `p in T` forces
`R=T-{p}` and `A=R union {x}`.  Dually, for all records sharing one blocker
`p`, source-only decoding chooses `x in A` and forces `R,T`.  Hence

\[
             |E_x|\le(r+1)V(P),\qquad |E^p|\le(r+1)V(P).  \tag{23r2u}
\]

If `X,Y` are the two mark alphabets and `D` is the raw selected source
degree, all one-face projections combine to the exact menu

\[
 |E|\le\min\{(r+1)|X|,(r+1)|Y|,\Lambda,D\}\,V(P).       \tag{23r2v}
\]

Thus failure of a `D^{1-epsilon}` charge requires both mark alphabets and
the pair fibre `Lambda` to exceed that scale (up to `r+1`); arbitrary core
incompatibility with either mark fixed is already harmless.

The first genuinely two-mark geometric step is also exact.  Every singleton
record `(R,x,p)` has one insertion edge `uv` of `R`, shared by `x` and `p`,
and

\[
                         x\in\operatorname{int}\triangle(u,v,p). \tag{23r2w}
\]

For a common-core mark rectangle
`{x_1,x_2} times {p_1,p_2}`, either both same-side pairs are
insertion-incomparable, in which case

\[
             R\cup\{x_1,x_2\},\qquad R\cup\{p_1,p_2\}   \tag{23r2x}
\]

are two ordinary faces that recover the rectangle injectively, or one
same-side pair is nested and canonically supplies a rooted `1+3` circuit of
the form `(23r2w)`.  Hence the total number of good common-core rectangles
is at most `V(P)^2`; every excess rectangle is localized to an actual rooted
circuit shadow.

This dichotomy is sharp.  A planar tensor with `M=2^k` Boolean cores and a
complete `a times b` mark fibre attains equality in the three-projection
Loomis--Whitney bound

\[
 (Mab)^2=(Ma)(Mb)(ab),                                  \tag{23r2y}
\]

while every mark rectangle takes the circuit branch.  Its detached core
and mark shields pay, so it is not an EIC' counterexample.  The remaining
singleton theorem is therefore aggregate rooted-circuit core--mark mixing;
projection entropy and another local insertion-chain bound cannot prove it.
See `agent_one_sided_reflection/MARK_C4_ROOT_CIRCUIT.md`.

Moreover two chain fibres with the same marked repaired target `(T,p)` map
to `(T,{x_1,x_2})` with load at most `|T|`, so their total Cartesian mass is
at most `(r+1)V(P)^2`.  Hence the noncircular two-chain residue is not reset
depth, one fixed ear--blocker pair, one common ear, or one common blocker.
It requires simultaneous variation of both marks across different terminal
targets, or hidden ears of rank greater than one.  This is the off-diagonal
quadratic crossing-core atom already present in ACP.  See
`agent_one_sided_reflection/TWO_CHAIN_SYNCHRONIZED_ACP.md`.

Canonical endpoint peeling removes the formal overlap ambiguity.  For a
face `U={v_1<...<v_k}`, peel
`e_j=(v_{j+1},v_{k-j})`.  Let `P` be the true half-Gibbs law on these face
chains and let `Q` repeatedly choose endpoints using the *unconditioned*
half-Gibbs endpoint marginal of the current open interval.  If
`lambda_e=4G_e(1/2)/F_{\rm open(e)}(1/2)`, exact cancellation gives

\[
       {\mathsf Q(U)\over\mathsf P(U)}=\prod_j\lambda_{e_j},
       \qquad
       \mathbb E_{\mathsf P}\sum_j\log{1\over\lambda_{e_j}}
            =D(\mathsf P\Vert\mathsf Q).                   \tag{23r3}
\]

Thus the multiscale capture debt is one KL divergence, not a repeated
union-bound loss.  Radial overlap also has the exact first moment

\[
     \mathbb E_\pi d_j(S)=4^j\Pr_\pi\{|U|\ge2j\}\le4^j,   \tag{23r4}
\]

where `d_j(S)` counts faces whose `j`-times-peeled core is `S`.  The open
matrix gate is now the high-degree tail/geometric incompatibility bound for
this canonical chain.  A general KL is not bounded by source entropy, and
the stronger pointwise cost-versus-surprisal inequality only survives the
main planar exact tests; it is not yet a theorem.  The quantitatively
sufficient target is

\[
   \mu_{1/2}+{D(\mathsf P\Vert\mathsf Q)\over\log_2n}
          \ge(1-o(1))\log_2n,\qquad
   D(\mathsf P\Vert\mathsf Q)=o((\log n)^2).               \tag{23r5}
\]

   Indeed `H>=n^epsilon` forces `mu_(1/2)<=(1-epsilon)log n`, so the first
inequality would force quadratic KL, contradicting the second.  Merely
`D<=H(P)=Theta((log n)^2)` is far too weak.  Also a rank-three hereditary
complex on 23 labels (complete 3-skeleton plus a Boolean middle block and
one nested face) violates the pointwise cost-versus-surprisal inequality
exactly.  Thus any proof of `(23r5)` must use planar reflection signs or
   product faces, not downward closure alone.

The KL upper half also has a sharper exact terminal formulation.  Peel a
rank-`K` face completely and let `B=(K,C)` record its rank and its terminal
empty/median-singleton core.  If `d(B)` is the number of faces in that radial
bucket and `L(U)=prod_j lambda_(e_j)`, then

\[
 D(\mathsf P\Vert\mathsf Q)=H(B)+
   \mathbb E\log{\pi(B)\over L(U)},\qquad
 H(\mathsf P)=H(B)+\mathbb E\log d(B),                    \tag{23r6}
\]

with `H(B)<=2log(n+1)`.  Consequently any constant-per-selected-vertex
radial capture

\[
                 \pi(B(U))\le C^{|U|}n^bL(U)              \tag{23r7}
\]

would give `D=O(mu_(1/2)+log n)` and prove the needed KL upper bound in the
low-mean branch.  Every pointwise failure has an exact first bad peel:

\[
 {d_{j+1}(S_{j+1})\over d_j(S_j)}>C^2\lambda_{e_j},
 \qquad d_{j+1}(S)=\sum_{T:\,\operatorname{peel}_1(T)=S}d_j(T). \tag{23r8}
\]

Thus the KL high tail is literally the same weighted cross-child collision
as `(EIC'f)`.  In fact the full pointwise target `(23r7)` is false for every
fixed `C,b`, already on a stretchable rank-four family.  Take six high points
`u_(+-a)=(+-a,-a^2)`, `a=2,4,6`, and `m` low points on a separated concave
cap `w_1,...,w_m`.  The asymmetric face
`V_m={u_-4,u_-2,w_(m-1),w_m}` has two peeled cells which see essentially the
same Boolean low reservoir.  Because the right endpoint itself lies on the
low cap, any compatible trace contains at most one earlier low point.  With

\[
 B_t=1+{t\over2},
\]

the exact estimates give

\[
 {\pi(B(V_m))\over L(V_m)}
 \ge {1\over16}{(3/2)^{m-10}\over B_{m-1}B_{m-2}}
 =\Omega\!\left({(3/2)^m\over m^2}\right).             \tag{23r8a}
\]

This defeats `C^4n^b`.  The definition-only estimate certifies failure of
`C=8,b=0` at `m=54`; exact matrix evaluation already finds failure at
`m=21` (`n=27`).  The example
does **not** kill the averaged KL target: the bad face has exponentially
small half-Gibbs mass.  It proves that repeated visibility of one common
cage must be aggregated before it is charged.  Canonical KL can also be
`Theta(n)` on the stretchable alternating family, so the low-mean hypothesis
is essential.  See `agent_kl_radial_high_tail/KL_RADIAL_BUCKET_REDUCTION.md`
and `agent_outer_internal_product/RMC_NESTED_CAP_COUNTEREXAMPLE.md`.

The apparently separate high-rank tail is in fact automatic in a
fixed-power bad branch.  If `H>=n^epsilon`, then

\[
       \mathbb E_\pi2^K={Z(1)\over Z(1/2)}={n\over H}
             \le n^{1-\epsilon},
       \qquad \Pr\{K\ge4\log_2n\}\le n^{-3-\epsilon}.       \tag{23r9}
\]

For a selected trace `S` in an interval `I`, its cell mass gives
`lambda_e>=(3/2)^{-(|I|-|S|)}` because every subtrace of `S` is
compatible.  Hence one peel costs less than `n`
bits and an entire face less than `n^2`; the contribution of the event in
`(23r9)` is `o(1)`.  All live radial cores therefore have fewer than
`4log n` labels.  For two immediate radial parents, either both mixed
parents exist, they share an endpoint, or a failed mix has a planar
four-circuit witnessed by two labels of the common core.  The witness costs
only `O((log n)^2)=n^{o(1)}` choices.  Thus the remaining KL target is an
**activity-weighted**, low-rank mixed-product/common-blocker/shield tail;
uniform control over every radial core is false and unnecessary.

More precisely, for peel depth `j` let `N_j` be the exact truncated radial
mass, put `R_T=1/lambda_T`, and in the dyadic band
`2^m<=R_T<2^(m+1)` define the cap-weighted demand

\[
 \mathcal D_{j,m}=\sum_T2^{-|S(T)|}d_j(T)R_T.
\]

If one fixed `delta>0` satisfies the normalized fixed-power estimate

\[
       \mathcal D_{j,m}\le
       n^{o(1)}2^{(1-\delta)m}N_j                         \tag{23r10}
\]

uniformly, then the parent mass in band `m` is at most
`n^{o(1)}2^{-delta m}N_j`; layer-cake summation gives
`D(mathsf P||mathsf Q)=o((log n)^2)`.  Thus `(23r10)` is the exact
activity-weighted handshake between the canonical KL process and `(EIC')`:
the cap is `2^(m+1)`, every history already has its true radial weight, and
no separate high-rank or history-erasure term remains.

There is now also an exact one-depth decomposition which aggregates shared
interval cages before taking logarithms.  Let `q_(j,e)` be the half-Gibbs
activity of endpoint pair `e` at depth `j`, `tau_j=sum_e q_(j,e)`, let
`F_e` be the half-partition function of its open interval, and put

\[
             \mathcal A={1\over4F(P;1/2)}\sum_eF_e.
\]

Normalize `r_e=F_e/(4F mathcal A)`, let `p_e` be the depth-zero endpoint
law with total mass `P_2`, and write `qhat_j=q_j/tau_j`,
`phat=p/P_2`.  There is an exact two-reference identity, followed by the
log-sum/data-processing bound

\[
 {D_j\over\tau_j}=log{\mathcal A\over P_2}
 +D(\widehat q_j\Vert\widehat p)-D(\widehat q_j\Vert r),
 \qquad
 D_j\le \tau_j\log{\mathcal A\over\tau_j}
 +\tau_j\,\mathbb E_{\sigma_j}
       \log{d_j(T)\over4^j},                             \tag{23r10a}
\]

where `sigma_j(T)=pi(T)d_j(T)/(4^j tau_j)` is the size-biased parent law.
The container mass has the exact incidence identity

\[
 4\mathcal A=\mathbb E_\pi N(S),\qquad
 N(S)=\min(S)(n-1-\max(S))                               \tag{23r10b}
\]

for nonempty `S` (and `N(emptyset)=binom n2`).  Hence the first term is a
literal interval-Carleson charge; the second is exactly the radial crowding
moment already represented by cross-child collisions.  The negative
`D(qhat_j||r)` is the exact common-cage cancellation lost by the upper
bound; a sharp proof may compare the radial endpoint tilt toward `phat`
directly with the competing reservoir tilt toward `r`.

Both reference laws have a literal joint interpretation.  On incidences
`(e,S)` with `S` a face in the open interval `I_e`, put

\[
 R(e,S)={2^{-|S|}\over4F\mathcal A}.
\]

If `C` is endpoint compatibility, the ordinary parent Gibbs law is exactly

\[
 P=R(\,\cdot\mid C),\qquad R(C)={P_2\over\mathcal A}.   \tag{23r10e}
\]

Thus `(23r10a)` is the difference of the two conditional-core KL costs
against `R` and `P`; the cancellation is genuine conditioning, not formal
algebra.  More importantly, set

\[
 S_j=\sum_e{q_{j,e}\over\lambda_e},\qquad
 M=\sum_j\tau_j=\mathbb E_\pi\lfloor K/2\rfloor.
\]

Jensen at one depth and log-sum across depths give the exact global bridge

\[
 D_j\le\tau_j\log{S_j\over\tau_j},\qquad
 D\le M\log{\sum_jS_j\over M},\qquad
 \sum_jS_j\ge M\,2^{D/M}.                              \tag{23r10f}
\]

Writing `dbar_(j,e)` for the endpoint-cell half-Gibbs mean radial degree,
the same demand has the three exact forms

\[
 S_j=\sum_e{q_{j,e}\over\lambda_e}
     =\mathcal A\sum_er_eh_{j,e}
     ={1\over4^{j+1}F}\sum_eF_e\,\overline d_{j,e}.     \tag{23r10g}
\]

Equivalently, attach every interval face `W` to every actual depth-`j`
parent occurrence of endpoint `e` with normalized fractional demand
`w2^{-|W|}/Z_e(1/2)`.  Its total demand is exactly `S_j`.  Hence if
`M<=c_0log n` and `D>=delta(log n)^2`, then

\[
                 \sum_jS_j\ge M n^{\delta/c_0}.         \tag{23r10h}
\]

This is the exact handshake from quadratic radial distortion to a
fixed-power Hall obstruction.  Literal transport monotonicity is false: an
exact rational nine-point configuration has
`S_1/tau_1=3203/3109>8335/8101=mathcal A/P_2` and positive divergence
difference `0.000257048570...` bits.  Thus the remaining theorem must be an
asymptotic Hall/first-divergence allocation of the weighted parent--reservoir
records, not ordinary data processing.  See
`agent_outer_internal_product/TWO_REFERENCE_HALL_DEMAND_GATE.md`.

The literal routing has an exact good/bad split.  With `ell_+(W)` from
compatible `e union W` and `ell_-(W)` from blocked pairs,

\[
 \mathbb E_\pi\ell_+(W)=M,
 \qquad
 \mathbb E_\pi\ell_-(W)=\sum_jS_j-M.                   \tag{23r10i}
\]

Thus every excess inverse-capture unit is a blocked parent--interval
record.  Fix a loaded `w`-face `W`, at most `J` active depths, and a
threshold `Theta`.  There is then an exact trichotomy:

\[
 \begin{array}{ll}
 \text{one heavy cell:}&
      d_j(T)>4^{j+1}\Theta\text{ for some actual parent};\\[2pt]
 \text{tagged mixing:}&
      \#\{e:W\cup e\text{ is a face}\}
          \ge\ell(W)/(2J\Theta);\\[2pt]
 \text{one circuit fibre:}&
      \#\{e:\text{one fixed canonical }W\text{-trace/role}\}
          \ge {\ell(W)\over
          2J\Theta(\binom w2+2\binom w3)}.
 \end{array}                                             \tag{23r10j}
\]

Taking `Theta=sqrt(ell(W))` preserves a fixed power when `J,w=n^{o(1)}`.
The mixed faces retain and recover the full interval tag.  The remaining
low-rank atom is one common `W`, one two- or three-point trace, one circuit
role, and fixed-power many endpoint pairs.  Target rank can in fact be
removed from this statement.  If `B_W` is the blocked load,
`eta_*` the maximum endpoint load, and `b_*` the maximum load in one
canonical circuit profile, then exactly

\[
 \#\{\text{profiles}\}\ge B_W/b_*,\qquad
 \max_\rho\#\{e:\rho(e)=\rho\}\ge b_*/\eta_* .         \tag{23r10k}
\]

Consequently either `eta_*>=B_W^(1/3)`, there are at least
`B_W^(1/3)/2` distinct ordinary rank-two/three traces inside `W`, or one
fixed trace and role is shared by at least `B_W^(1/3)` endpoint pairs.
Thus a high-rank target also preserves a cube-root fixed power.  The true
loss is no longer target rank: replacing `W` by the trace erases `W-rho`,
and those erased targets may collide globally.
See `agent_outer_internal_product/LITERAL_INTERVAL_LOAD_DICHOTOMY.md`.

The erased-target statement is now completely resolved for the `2+2`
circuit type.  Prioritize a one-ended `1+3` circuit whenever one exists.
In the remaining branch both `W+ell` and `W+r` are faces.  Their insertion
edges cannot be disjoint or equal, so they meet at one parent vertex `z`;
this is the only bad turn.  Every `2+2` witness trace `A` contains `z`, and
the seam criterion gives the exact repair

\[
             (W-A)\cup\{\ell,r\}\in\mathcal F(P).      \tag{23r10k1}
\]

The output recovers the endpoint pair and, after the fixed trace is added
back, the whole interval face.  Thus for aggregate endpoint tilts `eta_e`,

\[
 H=\sum_e\eta_e\le\eta_*|\mathcal O|
                    \le\eta_*V(P),\qquad
 \eta_*=\max_e\eta_e,                                  \tag{23r10k2}
\]

with only the explicit global state-overlap factor when tags vary.  No
pointwise radial-capture estimate is used.

The surviving `1+3` atom is genuine.  A convex parabola interval `W` and
arbitrarily large rational endpoint clusters can make the same three-point
trace witness every endpoint pair, while `(W-A) union e` remains nonconvex
for all of them.  In fact one endpoint becomes an admissible ear only after
all but two labels of `W` are deleted.  Hence bounded seam iteration cannot
reattach the interval complement; the remaining global problem is exactly
the one-sided blocker/repair Hall bank.  See
`agent_outer_internal_product/SEAM_JET_INTERVAL_COMPLEMENT_DICHOTOMY.md`.

The exact visible-hull reset does not repair this atom either.  Writing
`V_ell(W)` for the visible vertices of `conv(W+ell)` and
`Z_ell(W)=W-V_ell(W)`, one has the coefficientwise Kraft factorization

\[
 (1+z)^m=\sum_H z^{|H|}(1+z)^{|I(H)|},                \tag{23r10k3}
\]

and the pair `(V_ell(W),Z_ell(W))` recovers `W`.  But every nonempty hidden
trace lies inside the rooted visible polygon, so the factorization is a
two-face code, not a mixed ordinary face.  This limitation is sharp for the
literal depth-zero weights.  A rational conic construction gives the full
record rectangle

\[
 L\times R\times {X\choose s}\times {Y\choose s},
 \qquad |X|=|Y|=3s,\quad |L|=|R|=2^s,
\]

with one fixed `1+3` trace.  Arbitrary fractional routing among the
rooted-visible, hidden, full-interval, and endpoint-edge projections has
congestion `Theta(2^{2s})=Theta(n^2)`.  More strongly, the endpoint plus any
three lower-arc labels is a bad four-set, so every ordinary record subface
retaining that endpoint contains at most two lower labels.  Even routing to
*all* ordinary record subfaces has congestion
`Omega(2^s/s)=Omega(n/log n)`.  The hidden child can moreover have an
arbitrary stretchable order type by singleton-reset projective universality.
Thus a projection/deletion-only Kraft telescope is coefficient-circular;
the positive continuation must import an external reservoir face or retain
separately charged source/history data.  See
`agent_outer_internal_product/VISIBLE_HIDDEN_INTERVAL_KRAFT_BARRIER.md`.

The marked shield retained by the KL/Hall descent is not yet a sufficiently
large external alphabet for this atom.  If a base routing has normalized
load `R`, a disjoint `c`-label ordinary face coexists with every base output,
and the product decoder has load `Lambda`, distributing through its downset
improves the load exactly to

\[
                    \Lambda R(3/2)^{-c}.               \tag{23r10k4}
\]

This is a genuine conditional closure theorem, but the constants are
decisive.  The conic `1+3` rectangle forces, even under fictitious perfect
coexistence and a subpower decoder,

\[
 c\ge\left({1\over\log_2(3/2)}-o(1)\right)\log n
       =(1.709511\ldots-o(1))\log n.                  \tag{23r10k5}
\]

The current pocket reservoir supplies only about `(1/4)log n` labels.
Moreover the hard marked-alphabet regression has
`(Q union {p}) union F` nonconvex for every nontrivial marked shield `F`:
the descent retains the name `(p,F,tau)`, but not a geometric product with
the varying interval output.  Thus merely spending the marked shield, even
with perfect bookkeeping, cannot close the `1+3` branch.  What is missing
is a shield-faithful coexistence map recovering the base output, the shield,
and its chosen subface with subpower aggregate load.  See
`agent_outer_internal_product/MARKED_SHIELD_EXTERNAL_ALPHABET_GATE.md`.

Nor does the one-ended circuit hypothesis by itself force the
lexicographic wrapper recurrence which would asymptotically yield
coefficient `1/2`.  The same exact seven-point `1+3` gadget has four strict
reverse-dominance cells and two convex singleton words, but its formal
one-gap cap--cup output is nonconvex even after the root is removed.  Thus
the conditional recurrence from `(3az18a)--(3az18b)` remains valid under
true cyclic separation, but local circuit/Ferrers data do not supply that
exposure.  Projective child skew is still free.  See
`agent_outer_internal_product/ONE_THREE_WRAPPER_APPLICABILITY_BARRIER.md`.

Varying interval faces themselves admit the same support-redundancy split.
After exact rank-role/chain slicing with coefficient-scale loss
`Gamma<=2^{r+1}r^{r+1}`, let `Delta` be the maximum retained endpoint
multiplicity of one interval face.  For disjoint role supports of total
size `N`, product `P_0`, and redundancy `R`, one has

\[
 {V(P)\over|\mathcal R|}\ge {1\over\Gamma\Delta}
    \max\left\{1,{f(N)2^R\over P_0}\right\}.          \tag{23r10k6}
\]

Thus quadratic `R` pays polynomial endpoint reuse at the critical rank.
In the low-`R` ordered/simple-chain branch, transcript retention gives a
homogeneous product `prod_iY_i`, whose exact ordinary partial-transversal
bank has count and half-weight

\[
                 \prod_i(1+|Y_i|),\qquad
                 \prod_i(1+|Y_i|/2).                  \tag{23r10k7}
\]

The original complete-middle-layer conic has natural order-statistic
redundancy `Theta(r log r)`.  More sharply, restricting to one point from
each three-label role block gives a genuine `R=0` product and **still**
defeats every record-subface routing: the symmetric two-arc capacity audit
gives fixed-power load `Omega(s^{-4}(36/25)^s)`.  Nevertheless the complete
Boolean complex on the merged role-support union pays its whole raw and
half-weight demand, by a factor `Theta((81/64)^s)` at half weight.  The
payment uses faces taking multiple labels from a role block and is a global
support charge, not a `W`-recovering routing; different support unions may
reuse the same bank.  The surviving statement is therefore support-union
Hall consolidation across root/interval fibres.
See
`agent_outer_internal_product/SUPPORT_REDUNDANCY_ONE_THREE_FIBRE.md`.

The compatible numerator has one further exact lower bank.  If `a_I(T)` is
the number of addable labels inside the parent interval, heredity supplies
the disjoint one-label cubes

\[
 Z_e(1/2)\ge(3/2)^{|S|}\left(1+{a_I(T)\over2}\right).    \tag{23r10c}
\]

However, simply dropping the negative logarithm from this factor cannot
prove `D=O(mu log(mu+2))`: with

\[
 A_+(U)=\sum_{z:U+z\text{ a face}}
 \min\{|U\cap(-\infty,z)|,|U\cap(z,\infty)|\},
\]

exact deletion reversal gives

\[
 \mathbb E_\pi A_+(U)
 =2\mathbb E_\pi\left\lfloor{(K-1)^2\over4}\right\rfloor. \tag{23r10d}
\]

Thus a first-moment omitted-label proof is intrinsically a second-moment
bound; the negative `log(1+a_I/2)`, higher compatible cubes, or planar
first-divergence must be retained.  In the rank-four
nested-cap kill, the two bad parent states have radial degrees `1` and `8`,
and their **total** activity contribution is at most

\[
 {9\log(3/2)(m-2)\over16(3/2)^m}.
\]

Thus the common Boolean cage is paid once and the pointwise exponential
failure disappears after activity aggregation.  Closing `(23r10a)` now
means partitioning prevalent low-rank occurrences into recoverable interval
groups with subpolynomial effective `mathcal A`, or proving that failure
forces a large radial-crowding/Hall bank.  See
`agent_outer_internal_product/AVERAGED_RADIAL_CARLESON_DECOMPOSITION.md`.

Combining this with the banked universal
`log V>=(1/4-o(1))(log n)^2` shows that any fixed-power violation
`H>=n^epsilon` has all but `2^{-Omega((log n)^2)}` of its half-activity mass
on endpoint spans larger than

\[
 \left({1\over4\log_2(3/2)}-o(1)\right)(\log_2 n)^2
   = (0.4273\ldots-o(1))(\log_2 n)^2.                       \tag{23s}
\]

This removes bounded and merely logarithmic matrix blocks.  It is not a
closure, but the mean constraint sharpens it further.  If `S=n^{o(1)}` then
the half-mass fraction on spans at most `S` is `o(1)`; for fixed `gamma>0`
the fraction on spans at most `n^gamma` is at most
`4gamma(1-epsilon)+o(1)`.  Under the selected-vertex size bias,

\[
       \mathbb E\log_2(\text{span})
       \ge\left({1\over4(1-\epsilon)}-o(1)\right)\log_2n. \tag{23t}
\]

Thus a genuine bad state lives on macroscopic nested endpoint histories.
A stretchable alternating family nevertheless has linear Renyi drift even
after all `O(log n)` spans are deleted, and it can recharge the same direct
root at every ancestor.  Energy growth and alignment must therefore be
coupled on the long intervals.  See
`agent_unit_matrix_asymptotic/REPORT.md` and the operator barriers in
`agent_cyclic_stem_hw/coxeter_matrix/REPORT.md`.

## 7. Killed proof routes

The following cannot close the theorem as stated.

1. **One structured subset.**  Extracting a structured `n^alpha` subset
   squares the exponent loss.  The strong-tree coefficient `1/2` transfers
   as only `alpha^2/2`; preserving `1/2` needs `alpha=1-o(1)`.  This is not
   merely a limitation of known extraction theorems.  The guarded-Pascal
   family in `agent_low_v_structure` has coefficient at most `1/2+epsilon`
   but every exact mirror-decomposable subset has size at most `n^alpha` for
   a fixed `alpha<1` (depending on the fixed guard).  Near-spanning exact
   regularization is therefore false even arbitrarily near the conjectured
   optimum.
2. **Black-box mutually avoiding pairs / same-type transversals.**  The
   known square-root extraction is far too small.  Even a lossless one-level
   same-type transversal pipeline has ceiling `1/4`.
3. **History compression inside the history.**  Hinged histories have the
   full coefficient-one-half mass, but exact rational alternating examples
   force every contained convex output map to have `2^Theta(r^2)` fibres.
   A successful charge must be nonlocal.
4. **Scalar cap/cup marginals.**  Exact heterogeneous compositions can
   anti-align cap mass and cup mass exponentially.  No polynomial or
   `n^o(log n)` comparison `CU/V` is universal.
5. **Finite-state vertical substitution grammars below `1/2`.**  The hinged
   prefix-code/Perron theorem gives the lower barrier `1/2` even with variable
   arities, parallel transitions, arbitrary nonstrong child order types, and
   arbitrary finite chart menus.  Moreover `(3d3z11s9z4)`--`(3d3z11s9z7)`
   close unboundedly growing chart menus and completely nonstationary macros
   whenever child sizes are homogeneous, the hinged arms call one child
   chart, and the final splice does likewise.  An upper escape therefore
   requires heterogeneous sibling weights/chart anti-alignment, a
   macroscopic mesh jump, failure of the endpoint recurrence, or different
   mixed-triple geometry; state proliferation by itself is no longer an
   escape.  In the heterogeneous case `(3d3z11s9z8)`--`(3d3z11s9z10)`
   reduce the issue exactly to accumulated jump variance and weighted
   predecessor/sibling defect.  The entropy-only shortcut with constant
   two is false even on a stretchable nonstrong eight-point macro, and the
   stronger zero-defect hinge `(3d3z11s9z11)` is now false on a
   stretchable five-point chart.  The exact surviving target is the
   square-corrected Bellman inequality
   `(3d3z11s9z13)`/`(3d3z11s9z15)`; literal
   nested-threshold uncrossing is false as well.
6. **Endpoint-only weighted inequalities.**  Constant-loss WES and every
   positive marker-span power are false on explicit rational families.
   The full-interval `m^2` inequality remains open but, alone, cannot improve
   the `1/4` coefficient without a recursive pocket mechanism.
7. **Local activity gap / pointwise deletion path / naive Tutte induction.**
   All have exact planar counterexamples recorded in the agent reports.
8. **Endpoint-stack and source-local shadow expansion.**  Exponentially many
   low-extension sources can share the same repaired triangle, tangent data,
   and inner pocket, so a short endpoint/onion record cannot recover them.
   More strongly, an arbitrarily large exterior apex cloud can leave the
   entire source swap graph equal to a fixed Johnson graph with a large
   one-swap-independent code.  Thus neither local exchanges nor immediate
   shadows can pay for the missing ambient factor; the chosen target face
   must encode source information inside the exterior/interior pocket.
9. **One or subquadratically many polynomial source frames.**  These are not
   counterexamples: the unrooted mass outside a frame proves RNP directly.
   Any surviving obstruction must have quadratic frame entropy.
10. **Uncapped exterior-incidence counting.**  A source may have far more
    than the `2^g` blockers needed by RNP.  Bounding all such incidences is
    an avoidable strengthening and is false for several padded examples.
    Every Hall formulation below is understood with a selected cap of
    `2^g/n^{o(1)}` blockers per unresolved source.
11. **Rank-only interval batching.**  Pairwise disjoint blocker windows do
    generate a local Boolean target cube, but the projection can erase
    `Theta(r^2)` source bits.  A descent of `s` ranks is useful only with
    `2^s` global target expansion; the forward two-ended state cannot be
    discarded.
12. **Atomic or scalar-enriched all-interval recovery.**  Full Cartesian
    products with ramp--plateau--ramp alphabet sizes have only polynomially
    more source downfaces and atomic interval targets than sources, although
    the capped demand is exponential.  Retaining only per-block totals
    `(C,U,V)` still fails on a sharp cap/cup-gradient profile.  A valid
    recurrence must keep tangent-type distributions or the recursively
    usable internal face complex.
13. **Hull-diagonal scalar identities.**  The exact Boolean hull identity
    and Gordon beta reflection admit nonnegative integral formal tables with
    all triples present but mean face size `4-O(1/n)` and half-weight ratio
    `n/16+O(1)`.  Those tables are nonrealizable precisely because they
    suppress higher cyclic/tangent compatibility.  Another scalar
    manipulation of the bivariate diagonal cannot close the planar theorem.
14. **Pure hidden-ear thinning or absolute cloud mass.**  Bernoulli thinning
    retains the exact conditional ear entropy, and fixed-core short ears are
    absorbed by the universal face count, but a genuine product repair cell
    still loses one whole blocker coordinate.  Even applying a hypothetical
    sharp unrestricted theorem to a quadratic-entropy long-ear label cloud
    need not recover that factor.  The needed gain is oriented and relative
    to the retained source family.
15. **Outer-cell-only fan stability or first-layer two-record uncrossing.**
    Quadratic retained and hidden entropy can remain independent inside one
    fixed outer tangent cell; the payment then lives in descendant
    two-ended faces.  Even for two records, taking first onion layers and
    adjoining the two blockers can fail to be convex on an exact nested
    parabola.  A valid recursion must preserve the complete nested component,
    not merely its first hull.
16. **Coherent universal-chain wrappers as an upper construction.**  For an
    arbitrary retained core moved into one fixed-edge chain, the exact wrapper
    recurrence is `Z'=Z+C_hat+U_hat+n+1` and
    `(C_hat+U_hat)'=2(C_hat+U_hat)+3n+4`.  Iteration therefore gives
    `log_2 Z=N/2+O(log N)`, exponentially worse than quasipolynomial.
    Resetting the tangent direction breaks this recurrence but simply preserves
    and reimports an arbitrary core, so no closed sub-half construction results.
    See `agent_subhalf_construction_fresh/CHAIN_WRAPPER_BARRIER.md`.

## 8. Verification map

- Upper and strong-class theorem: `paper/main.tex` and endpoint-reset audits.
- IDP identities/tests: `agent_integrated_activity/`.
- First switch: `agent_tilted_switch/`.
- Rank extension and abstract multiscale barrier:
  `agent_path_asymptotic/`.
- Antimatroid bridge and inverse-pair barriers: `agent_inverse_pair_hw/`.
- Pocket flow and nonlaminarity: `agent_pocket_restart/`.
- Rooted-circuit MFMC limitations: `agent_convex_mfmc_transfer/`.
- Endpoint counterfamilies: `agent_weighted_cupcap/`,
  `agent_endpoint_ladder_proof/`, and `agent_multiscale_short_span/`.
- History obstructions: `agent_geometry/HISTORY_ATTACK.md`.
- Low-count regularization limits:
  `agent_asymptotic/FULL_REGULARIZATION_TRANSFER.md` and
  `agent_low_v_structure/`.
- Peak-mean/Hall reductions and exact regressions:
  `agent_acp_proof/`, `agent_apa_charging/`,
  `agent_generalized_deletion/`, and `agent_onion_hall/`.
- Polynomial-frame discharge: `agent_circuit_hardcore/RNP_POLYNOMIAL_FRAME.md`.
- Capped common-pocket and quadratic-source-entropy discharge:
  `agent_acp_proof/REPORT.md`.
- Cyclic-window dichotomy and exact two-ended product discharge:
  `agent_two_ended_hall/REPORT.md`.
- Macroscopic homogeneous-jump barrier: `agent_upper_jump/`.
- Successor-entropy entry and repair-split conservation:
  `agent_acp_proof/REPORT.md`, Theorems 20--25 and Proposition 21.
- Atomic/scalar all-interval barriers and exact vector recurrence:
  `agent_all_interval_isoperimetry/REPORT.md`.
- Hull-diagonal/beta formal barrier:
  `agent_cyclic_stem_hw/BETA_HULL_DIAGONAL_BARRIER.md`.
- Fixed-gap low-count reductions and the prime regularization barrier:
  `agent_all_interval_isoperimetry/LOW_V_FIXED_GAP.md`.
- Exact entropy--spectral repair rectangles and the projective-plane tensor
  barrier: `agent_cyclic_stem_hw/REPAIR_C4_COEFFICIENT_AUDIT.md` and
  `agent_cyclic_stem_hw/COMPONENT_SURPLUS_PAIR_TELESCOPE_BARRIER.md`.
- Fixed-cell cubic dominance supersaturation:
  `agent_root_followup/DOMINANCE_C4_SUPERSATURATION.md`.
- Label-faithful/universal-chain equivalence and mixed-branch barriers:
  `agent_label_faithful_decoder/LAYERED_CHAIN_LABEL_LOSS.md` and
  `agent_recursive_pocket_induction/LONG_CHAIN_MIXED_BRANCH_BARRIER.md`.
- Product-hull entropy, finite-IDP correction, and rooted-cluster defects:
  `agent_idp_mean_fresh/PRODUCT_HULL_ENTROPY.md` and
  `agent_rooted_cluster_weight/ROOTED_CLUSTER_WEIGHT.md`.
- Retained-outer and capped first-divergence audits:
  `agent_stacked_outer_pocket/STACKED_OUTER_POCKET_BARRIER.md` and
  `agent_capped_guard_release/CAPPED_GUARD_RELEASE.md` and
  `agent_linear_codim_capped/LINEAR_CODIM_CAPPED_CHAIN.md`.
- Coherent chain-wrapper construction barrier:
  `agent_subhalf_construction_fresh/CHAIN_WRAPPER_BARRIER.md`.
- Proper-downshadow and quadratic crossing-core barriers:
  `agent_linear_codim_capped/CROSS_CORE_DOWNSHADOW.md` and
  `agent_quadratic_cross_core/QUADRATIC_CROSS_CORE_SHIELD.md`; fixed-power
  reduction and complete shield bank:
  `agent_quadratic_cross_core/FIXED_POWER_SAVING_GATE.md`; central-prefix /
  forward-codegree regime split:
  `agent_linear_codim_capped/FIXED_POWER_EIC_SPLIT.md`; bounded circuit
  codegree and common-rooted-triangle localization:
  `agent_quadratic_cross_core/CIRCUIT_CODEGREE_POWER_SAVING.md`; heavy-toggle
  and common-blocker descents:
  `agent_heavy_prefix_rotation/HEAVY_PREFIX_ROTATION_DESCENT.md`; summed
  tangent-fan antichain theorem:
  `agent_quadratic_cross_core/COMMON_ROOT_FAN_SUM.md`; common-base balanced
  pocket split:
  `agent_quadratic_cross_core/BALANCED_HIDDEN_ATOM_POCKET_SPLIT.md`; exact
  cross-child collision/Cauchy threshold:
  `agent_cross_child_telescope/CROSS_CHILD_COLLISION_TELESCOPE.md`; square
  lift for many protected atoms:
  `agent_cross_atom_square/CROSS_ATOM_SQUARE_LIFT.md`; exact base-retention
  barrier and released-reservoir allocation:
  `agent_cross_context_merge/CROSS_CONTEXT_BASE_RETENTION_BARRIER.md`.
- One-pocket selected-neighbourhood shield reduction:
  `agent_one_pocket_reservoir/ONE_POCKET_RESERVOIR.md`.
- Global outer--internal mixed-bank theorem and weighted four-circuit defect:
  `agent_outer_internal_product/OUTER_INTERNAL_MIXED_BANK.md`; circuit
  transversal guard release and its exact toggle-overlap residue:
  `agent_outer_internal_product/CIRCUIT_TRANSVERSAL_GUARD_RELEASE.md` and
  `agent_common_shield_mixing/CIRCUIT_TRANSVERSAL_OR_OUTER_TOGGLE.md`;
  heavy common-base Boolean bank and exact rank-half overlap descent:
  `agent_common_shield_mixing/HEAVY_COMMON_BASE_SOURCE_DOWNSET.md`;
  middle-toggle completion traces and dense/full-shield terminal branches:
  `agent_middle_toggle_fibres/MIDDLE_TOGGLE_FIRST_DIVERGENCE.md` and
  `agent_outer_internal_product/COMMON_BASE_COMPLETION_SHADOW.md`; exact
  pairwise-incompatible sunflower reduction and detached-shield regression:
  `agent_outer_internal_product/PAIRWISE_INCOMPATIBLE_COMPLETION_REGRESSION.md`
  and `agent_common_shield_mixing/CROSS_CIRCUIT_SUNFLOWER_NORMAL_FORM.md`;
  detached pair-union and cyclic two-ended product banks:
  `agent_detached_pair_union/DETACHED_PAIR_UNION_BANK.md` and
  `agent_outer_internal_product/DETACHED_SHIELD_TWO_ENDED_PRODUCT.md`;
  projectively universal radial containers and exact one-gap profile
  multiplication:
  `agent_common_shield_mixing/DETACHED_RADIAL_LEXICOGRAPHIC_PROFILE.md`;
  exact bad-circuit component join and entropy/Kraft localization:
  `agent_detached_pair_union/DETACHED_CIRCUIT_COMPONENT_FACTORING.md`;
  independent double-parabola cover stress:
  `agent_shield_circuit_cover/SHIELD_CIRCUIT_COVER.md`.
- Unit-matrix Renyi/span localization:
  `agent_unit_matrix_asymptotic/REPORT.md`; sharp Ferrers-state injection
  ceiling and the activity-half dyadic-collapse barrier:
  `agent_coxeter_global_half/DOWNSET_ACTIVITY_BARRIER.md`
  `(23r2z)`--`(23r2z5)`; exact strict-cup saturation of every shared-endpoint
  and nested-cell interpolation, with its Boolean compensation:
  `agent_coxeter_global_half/SHARED_ENDPOINT_SATURATION_BARRIER.md`
  `(23r2z6)`--`(23r2z8)`; exact cellwise interpolation-defect versus
  disjoint Boolean-bank dichotomy, including its sharp stretchable
  saturation barriers:
  `agent_coxeter_global_half/SATURATION_BANK_DICHOTOMY.md`
  `(23r2z9)`--`(23r2z10)`; exact global sum/Cauchy consequences, their
  sharp common-endpoint-fan saturation, and the complementary-vertex
  compensation residue:
  `agent_coxeter_global_half/GLOBAL_BANK_AMPLIFICATION_BARRIER.md`
  `(23r2z11)`--`(23r2z13)`; exact coherent-root fan promotion versus an
  external Boolean bank, and the dense Erdős--Szekeres obstruction to any
  single complementary-bank charge:
  `agent_coxeter_global_half/ROOTED_FAN_COMPLEMENT_DICHOTOMY.md`
  `(23r2z14)`--`(23r2z17)`; exact lift to quasipolynomial rooted histories,
  the fixed-power Hall-load barrier for every homogeneous output, and the
  surviving local forcing of an opposite-sign/two-tangent partner:
  `agent_coxeter_global_half/WEIGHTED_ROOTED_HISTORY_HALL_BARRIER.md`
  `(23r2z18)`--`(23r2z21)`; exact terminal-cup obstruction to every
  label-retaining mixed-bank promotion, leaving pooled demand or a
  label-replacing recovery code:
  `agent_coxeter_global_half/MAXIMAL_CUP_HISTORY_MIXED_BARRIER.md`
  `(23r2z22)`--`(23r2z24)`; fibre-one label-replacing recovery of every
  coherent-root history in the sharp $E(k,k)$ stress family:
  `agent_coxeter_global_half/LABEL_REPLACING_ES_MIXED_CODE.md`
  `(23r2z25)`--`(23r2z28)`; exact weighted-Hall criterion, fibre-one
  special case, and sharp rank-$(r-3)$ assembly of trace-owned mixed codes:
  `agent_coxeter_global_half/ABSTRACT_MIXED_HALL_ASSEMBLY.md`
  `(23r2z29)`--`(23r2z32)`; stretchable linear-load failure of natural
  two-tangent Hall, its local fibre-one detached-side replacement, and the
  sharp cross-trace ownership residue:
  `agent_coxeter_global_half/LOCAL_TRACE_HALL_MATCHING_BARRIER.md`
  `(23r2z33)`--`(23r2z36)`; exact pooled-bank rank threshold,
  the quadratic obstruction below rank four, constant-load rank-four and
  fibre-one rank-five repair, and simultaneous coherent-root allocation:
  `agent_coxeter_global_half/JOINT_DETACHED_BANK_RANK_PROMOTION.md`
  `(23r2z37)`--`(23r2z41)`; universal global replacement of
  every literal rank-three history by the planar ES(4) quadrilateral bank:
  `agent_coxeter_global_half/GLOBAL_RANK_THREE_ES4_REPLACEMENT_CODE.md`
  `(23r2z42)`--`(23r2z46)`; terminal radial-bucket and
  activity-weighted fixed-power reduction:
  `agent_kl_radial_high_tail/KL_RADIAL_BUCKET_REDUCTION.md`; stretchable
  fixed-rank counterexample to every pointwise radial multiplicity capture:
  `agent_outer_internal_product/RMC_NESTED_CAP_COUNTEREXAMPLE.md`; exact
  averaged endpoint-Carleson/radial-crowding decomposition:
  `agent_outer_internal_product/AVERAGED_RADIAL_CARLESON_DECOMPOSITION.md`;
  exact joint conditioning law, global inverse-capture Hall demand, and the
  finite planar kill of literal transport monotonicity:
  `agent_outer_internal_product/TWO_REFERENCE_HALL_DEMAND_GATE.md`; literal
  common-interval load and its heavy-cell/tagged-mixing/circuit trichotomy:
  `agent_outer_internal_product/LITERAL_INTERVAL_LOAD_DICHOTOMY.md`.
- Global heavy-profile telescopes and the complete-layer four-local lift:
  `agent_outer_internal_product/GLOBAL_CARRIER_FIBRE_TELESCOPE.md` and
  `agent_outer_internal_product/COMPLETE_GUARD_LAYER_UNION_LIFT.md`.
- Rooted tangent amalgamation and the exact hidden-pocket Kraft reset:
  `agent_one_sided_reflection/ROOTED_DIAGONAL_AMALGAMATION.md` and
  `agent_one_sided_reflection/ROOTED_HULL_KRAFT_RESET.md`; exact linear-depth
  coexistence barrier and the projective-universality kill of every standalone
  discarded-layer target, plus the full-ACP synchronized two-chain collapse:
  `agent_one_sided_reflection/TANGENT_RESET_CHAIN_BARRIER.md` and
  `agent_one_sided_reflection/SINGLETON_RESET_PROJECTIVE_UNIVERSALITY.md`,
  `agent_one_sided_reflection/TWO_CHAIN_SYNCHRONIZED_ACP.md`; singleton
  three-projection barrier and common-core mark rectangle/circuit dichotomy:
  `agent_one_sided_reflection/MARK_C4_ROOT_CIRCUIT.md`.
- Central guard circuit-transversal telescope and its carrier-local barrier:
  `agent_outer_internal_product/CIRCUIT_TRANSVERSAL_CENTRAL_LAYER_BARRIER.md`;
  global cube heavy/light prevalence and the cross-anchor completion
  telescope, followed by the two root-shield release banks:
  `agent_outer_internal_product/GLOBAL_CUBE_PREVALENCE_GATE.md` and
  `agent_outer_internal_product/CROSS_ANCHOR_COMPLETION_TELESCOPE.md`,
  `agent_outer_internal_product/HALFPLANE_ROOT_SHIELD_GATE.md`; marked
  completion--half-plane pair decoder and the exact square-to-linear energy
  gate:
  `agent_common_shield_mixing/ROOT_SHIELD_MARKED_HALFPLANE_BANK.md` and
  `agent_common_shield_mixing/ROOT_SHIELD_SQUARE_LINEAR_ENERGY.md`; exact
  four-local carrier--root rectangle barrier, full-alphabet energy split,
  and genuine planar Ferrers/three-arc rectangle:
  `agent_outer_internal_product/SQUARE_TO_LINEAR_RECTANGLE_BARRIER.md` and
  `agent_common_shield_mixing/EXTERNAL_ALPHABET_ENERGY_TRICHOTOMY.md`;
  carrier endpoint-alphabet cutoff and the exact upper-jump applicability
  barrier:
  `agent_outer_internal_product/CARRIER_ALPHABET_SQUARE_GATE.md` and
  `agent_outer_internal_product/FERRERS_UPPER_JUMP_APPLICABILITY_GATE.md`;
  exact global fractional rectangle--shield/Carleson duality:
  `agent_common_shield_mixing/GLOBAL_FERRERS_SHIELD_TELESCOPE.md`; exposed
  shield entropy, exact anti-aligned one-child composition, and hereditary
  three-projection Hall pruning:
  `agent_one_sided_reflection/AGGREGATE_CIRCUIT_SHIELD_ANTI_ALIGNMENT.md`;
  dense-Hall marked shield/tangent localization and projective-plane
  incidence barrier:
  `agent_common_shield_mixing/DENSE_HALL_ROOTED_FIBRE.md`; polynomial
  bounded-rank skew regularization, incompatible-sunflower covering, and the
  recoverable two-ended gluing gate:
  `agent_one_sided_reflection/BOUNDED_RANK_SKEW_SUNFLOWER_GATE.md`; exact
  half-Gibbs radial-to-Hall routing, common-target load, and weighted
  marked-fibre descent:
  `agent_common_shield_mixing/RADIAL_KL_TO_HALL_BRIDGE.md`; genuine-history
  linear domination and the sharp complementary-downface energy limit:
  `agent_common_shield_mixing/WEIGHTED_HISTORY_DOMINATION_AND_COMPLEMENT_NO_GO.md`;
  exact same-parent-rank raw Hall conversion, baseline-scarcity and
  varying-tag barriers:
  `agent_common_shield_mixing/RAW_RANK_MATCHED_ENDPOINT_DICHOTOMY.md`;
  decoded common-parent Boolean payment and the conditional `3/8`
  radial-product jump:
  `agent_shield_circuit_cover/ENDPOINT_BASELINE_SCARCITY.md`;
  relative-mass completion-density bridge and its sharp coefficient-scale
  hypothesis:
  `agent_outer_internal_product/RAW_COMPLETION_DENSITY_BRIDGE.md`.
- Weighted-C4 trace audit, degenerate SOS certificate, signed
  genuine-rectangle barrier, and scalable counterexample to the full weighted
  inequality:
  `agent_common_shield_mixing/WEIGHTED_C4_INEQUALITY_AUDIT.md`,
  `agent_common_shield_mixing/DEGENERATE_COMPATIBILITY_SOS.md`, and
  `agent_common_shield_mixing/POSITIVE_GENUINE_CHARGING_COUNTEREXAMPLE.md`,
  `agent_common_shield_mixing/WEIGHTED_C4_SCALABLE_COUNTEREXAMPLE.md`; sharp
  cap-sensitive replacement:
  `agent_common_shield_mixing/CAPPED_WEIGHTED_C4_CONVERSION.md`.
- Global restriction-peak curvature/factorial hierarchy and its sharp scalar
  rank-truncation barrier:
  `agent_restriction_peak_curvature/REPORT.md`; exact two-scale/full-profile
  hypergeometric recurrence and its sharp quarter-coefficient fixed point:
  `agent_common_shield_mixing/TWO_SCALE_FULL_RANK_SAMPLING_BARRIER.md`;
  exact all-restrictions shelf obstruction, planar high-rank bank outside any
  fixed pocket, and dense common-edge circuit-rectangle reduction:
  `agent_common_shield_mixing/INDUCED_SUBSET_HIGH_RANK_POCKET_LIFT_GATE.md`
  `(16g)`--`(16l)`; unconditional quasipolynomial same-type transversal
  bank, exact anchored coexistence formula, and two-pocket-label barrier:
  `agent_outer_internal_product/SAME_TYPE_POSITIVE_FRACTION_POCKET_COEXISTENCE_GATE.md`
  `(16m)`--`(16n)`; rooted positive-density semialgebraic box extraction,
  exact weighted splice, and homogeneous fixed-edge zero-density cage:
  `agent_outer_internal_product/ROOT_AWARE_FIXED_EDGE_SEMIALGEBRAIC_EXTRACTION_GATE.md`
  `(16o)`--`(16q)`; exact circuit-trace deletion decoder, low-cover versus
  disjoint-crossing-matching split, and the remaining support-shield scale
  gap:
  `agent_common_shield_mixing/HIGH_RANK_FIXED_EDGE_CIRCUIT_DELETION_MATCHING_GATE.md`
  `(16r)`--`(16u)`, including the exact mixed-bank subtraction
  `(16s1)`--`(16s2)`; global matched-trace source charge, exact local-state
  ceiling, four-cover Boolean lift, and the live Pascal all-delete
  calibration:
  `agent_outer_internal_product/DISJOINT_TRACE_GLOBAL_SUPPORT_CHARGE_GATE.md`
  `(16v)`--`(16x)`, including the rank-refined shadow `(16v1)`;
  equality-boundary top-layer Pascal stability, with live common-edge
  sources and logarithmically many disjoint circuits:
  `agent_common_shield_mixing/PASCAL_TOP_LAYER_LIVE_FIXED_EDGE_STABILITY_BARRIER.md`
  `(16x1)`--`(16x3)`; exact
  weighted-child minimizer functionals at a literal all-delete seam,
  exclusion of the scalar/Pascal stationary calibrations, and the surviving
  high reflection-wall branch:
  `agent_outer_internal_product/STATIONARY_ALL_DELETE_WEIGHTED_PROFILE_MUTATION_GATE.md`
  `(16y)`--`(16z2)`; exact weighted cap-envelope reduction to the
  minimizer endpoint parameter, sharp exponential all-cup transition, and
  cap-triple cover:
  `agent_outer_internal_product/WEIGHTED_CAP_ENVELOPE_EXPONENTIAL_TRANSITION_GATE.md`
  `(16z3)`--`(16z7)`; strict-parent elimination of the Pascal live
  rectangle, the sharp facing-bank scale, exact history-load audit, scalar
  Pareto survivor, and nonliteral nine-point minimizer:
  `agent_strict_parent_profile_rigidity/STRICT_PARENT_PROFILE_RIGIDITY_GATE.md`
  `(16z8)`--`(16z10)`; exact endpoint-value moment inversion, deletion
  curvature audit, coupled Pareto closure condition, and stretchable flat
  nonstrong frontiers:
  `agent_minimizer_endpoint_curvature/MINIMIZER_ENDPOINT_CURVATURE_AND_HIGH_WALL_GATE.md`
  `(16z11)`--`(16z15)`; exact physical two-child Pareto envelope, its
  circular sharp floor and bilinear mixed curvature, and the hull-root
  saturation of the true nine-point minimizer:
  `agent_coupled_pareto_two_anchor/COUPLED_PARETO_TWO_ANCHOR_GATE.md`
  `(16z16)`--`(16z19)`; exact global hull-root envelope recurrence,
  cumulative Pareto-curvature target, chartwise hinged-Kraft product, and the
  scalar/fresh-chart reset barriers:
  `agent_hull_root_envelope_dynamic/HULL_ROOT_ENVELOPE_AND_CHART_RESET_GATE.md`
  `(16z20)`--`(16z26)`; universal root-chart Kraft, exact weighted
  shelling-to-face collision, and the resulting sharp remapping gate:
  `agent_shelling_multiplicity_decoder/ROOT_CHART_KRAFT_AND_SHELLING_COLLISION.md`
  `(16z27)`--`(16z30)`; exact minimax obstruction to every positive-mass
  ordinary-face remapping of the full shelling ledger, including optimized
  future-label menus:
  `agent_post_collision_remapping/POST_COLLISION_REMAPPING_MINIMAX.md`
  `(16z31)`--`(16z33)`; exact curvature-layer transport,
  native-cap collision, child-excess escape, and the direct high-hull wall:
  `agent_sparse_curvature_transport/SPARSE_CURVATURE_TRANSPORT_AND_NATIVE_COLLISION.md`
  `(16z34)`--`(16z37)`.

## 9. Recommended live attack order

Before the geometric list, one bookkeeping correction is now definitive.
The likelihood-weighted radial fibre is **not** a live EIC obstruction:
`(3az)` charges every fixed marked/tangent/history fibre by at most `L V(P)`.
The KL route's auxiliary raw-count algebra is also resolved by `(3az2)`--
`(3az3)`: same-parent-rank comparison produces a literal dense endpoint
cell.  Its remaining obstruction is geometric rather than rank-theoretic:
the endpoint baseline can be a singleton and varying interval tags can have
quadratic reuse, as `(3az4)` shows.  Singleton/polynomial baselines are
nevertheless globally charged by `(3az5)`; every extracted radial product
would jump the known coefficient to `3/8` by `(3az7)`.  The sharp auxiliary
target is now extraction of that product/module structure from an arbitrary
dense same-parent completion family.  Failure of product/tag recovery does
not undo the weighted theorem, and it should not be described as a surviving
weighted omitted-petal branch.

1. Prove the fixed-power capped statement `(EIC')`.  It is enough to gain
   `d^epsilon` over source projection for one absolute `epsilon>0`; no
   near-injective local Hall map is required.  The complete two-sided shield
   product already has congestion one, while the exact quadratic shield kills
   every record-local formulation.  The sharp target is therefore a global
   stability/container theorem: an incomplete quadratic-entropy family of
   cores either creates `d^epsilon` mixed core--pocket faces or its released
   shield complex contains `d^epsilon` times as many ordinary faces.  A
   density loss below `((s-3)/M)^4=2^{-Theta(r)}` is already handled; the
   remaining case is genuinely sparse at the fixed-power scale.  The new
   central-downshadow / codegree split disposes of light central prefixes for
   `alpha>=1/2` and of the forward singleton-ear branch for every fixed
   `alpha<1/2`.  It leaves exactly two atoms to join: a heavy released
   half-core, or nested/incompatible rotation mass carrying most of the
   blocker-codegree second moment.  The circuit-codegree theorem closes the
   bounded-codegree part with `epsilon=1/3`.  At coefficient scale its
   complementary atom localizes to one rooted triangle and a growing common
   exterior blocker fan; at fixed-power scale the `n^3` ambient-cell
   pigeonhole cannot be spent.  The immediate stability problem is therefore
   a **summed rooted-cell** theorem: compatible-antichain banks or nested
   insertion-chain complexes must pay across all triangle cells with only
   `n^{o(1)}` aggregate reuse.
   Equivalently, the toggle/marked-downset descent shows that every local
   child already has a fixed saving.  What must now be proved is a single
   planar cross-child Cauchy/telescope: complementary half-core banks and
   common-blocker target downsets cannot both be reused by polynomially many
   children unless their two-ended/shield mixed faces supply the missing
   power.
   The wide-fan half of this summation is now exact in `(EIC'e)`.  The final
   geometric atom is specifically a `sqrt D` nested blocker chain or a
   `D^{1-epsilon}`-heavy hidden fibre over one retained core and one
   incomparable blocker pair.  The balanced entropy/C4 and common-base
   pocket splits now prove the local separated-bank/rank-half alternative,
   and `(EIC'h)` removes the apparent square loss across arbitrarily many
   children whenever two one-slot reservoirs survive.  Both reservoirs
   cannot simply retain the ancestor base: `(EIC'i)` is an exact seam-scale
   counterexample.  Releasing one bank gives the explicit overload
   `(EIC'j)`, and the one-pocket theorem `(EIC'k)` further forces a dense
   incidence layer between quadratic-entropy source faces and
   `(1-o(1))B` macroscopic convex blocker shields.  The final missing
   interface is therefore a global **outer-context times internal-shield**
   theorem: either these correlated banks create `D^epsilon` mixed convex
   faces, or their cross four-circuits generate an unrestricted shield
   complex of that size.  The mixed-union half is now quantified by
   `(EIC'l)`: `D^3/2` compatible internal faces per context remove the entire
   overload, and the deficit is exactly witnessed by weighted `2+2` and
   `1+3` planar circuits.  The circuit-transversal theorem `(EIC'm1)`--
   `(EIC'm4)` now pays every small-cover family using the full reservoir and
   every large-matching family whose contextual toggle overlap is
   subpolynomial.  The last atom is therefore the complementary
   **high toggle overlap implies released outer shield** theorem.  The
   within-fibre source-downset multiplier and complementary two-face decoder
   are exact in `(EIC'n1)`--`(EIC'n3)`; a heavy collision canonically halves
   the variable base rank.  What remains is to sum those rank-half children
   without reusing the same unrestricted outer shield at every base.  The
   completion-trace theorem `(EIC'o1)`--`(EIC'o2)` closes complete,
   near-complete, small-family, and compatible-pair branches.  The exact
   residue is a far-from-complete quadratic-entropy completion family whose
   central overlaps stay heavy through the rank-halving tree.  The required
   off-diagonal load remains exactly `D^{1-eta}n^{o(1)}` at the
   seam; source-only nesting is projectively universal and cannot prove it.
   Polynomial thinning and a sunflower reduction turn this into disjoint
   pairwise-incompatible petals.  Testing the detached union closes every
   constant-density detached-compatible branch and, via `(EIC'o3)`, the
   exact nested-ear/container product; its coordinate Kraft load is only
   `2^q`.  The remaining family is pairwise **detached**-incompatible, so
   each witness circuit lies wholly in the two petals.  The proof must now
   extract a recoverable cyclic two-ended coordinate from those internal
   circuits, or charge a one-pocket unrestricted shield across all erased
   common-base contexts.  Arbitrary low-face radial replacements do not
   evade this: `(EIC'o5)` gives them a quadratic one-gap surplus.  Thus the
   current sharp target is specifically the **non-containerizable**
   detached circuit family, together with global recovery of its local
   shield bank.  The component join `(EIC'o6)`--`(EIC'o7)` removes the
   merely disconnected case: after an entropy-preserving localization the
   residue is one circuit-connected child.  Unrestricted recursion on that
   child is coefficient-equivalent to the original problem, so the next
   theorem must retain and exploit its `D` common-base one-point extensions.
   Pairwise detached incompatibility already makes the `DM` extension stars
   disjoint, paying one factor `D`; the missing statement is a fixed-power
   gain beyond this first star factor, or a shield bank that sums across the
   localized bases.  The wide insertion-pocket case is no longer part of
   this target: `(EIC'o8)` supplies a `D^{1/3-o(1)}` gain, and `(EIC'o9)`
   disposes of every positive share of splice-good collision energy.  The
   strict residue is therefore a nested-label, circuit-connected cross-base
   child carrying the marked repair alphabet, whose local full-support star
   complex can be exactly `DM` as in `(EIC'o10)`.  The next theorem must
   charge its unrestricted repair/completion shields with summable global
   overlap while preserving that mark; deleting the mark is
   coefficient-equivalent to #838.  The marked Carleson and collision bounds
   `(EIC'o11)`--`(EIC'o12)` close every low-codegree or splice-rich marked
   family.  Their exact common-alphabet barrier shows that the strict final
   bin can fix the same actual `(p,F)` across all `M` completions.  Therefore
   the next recoverable state must include a completion insertion edge or
   tangent-history coordinate in addition to `(p,F)`, or spend a second face
   which records that completion information.  The complete tangent cell can
   now be retained without an ambient edge guess.  Protect the five
   consecutive vertices `(a,u,p,v,b)` of a repaired rank-`q+1` star and
   delete `t` of the other `q-4` vertices.  Each history has
   `B_t=binom(q-4,t)` outputs, and the marked output recovers the five-vertex
   cell from cyclic neighbours.  Thus, in a fixed marked-shield bin,

   \[
             W B_t\le\Lambda_tV,\qquad
             V\ge {W B_t\over A},                       \tag{EIC'o13}
   \]

   where `Lambda_t` is guarded-output congestion and `A` is the maximum
   history weight in one tangent cell.  Central `t` gives
   `B_t=2^{q-o(q)}`.  A high-output fibre fixes `(p,F)`, the insertion edge,
   both tangent neighbours, and the retained prefix; every carrier is
   uniquely `Q_D=B union D`, `|D|=t`, and a first incompatibility circuit
   meets both `D-D'` and `D'-D`.  Hence even tangent refinement has an exact
   endpoint: the sole missing coordinate is the omitted completion petal
   `D`.  The radial product realizes quadratic many such petals with one
   fixed tangent state, so the next theorem must act on their central shadow
   or circuit components rather than refine the outer mark again.  See
   `agent_common_shield_mixing/TANGENT_MARKED_SHIELD_DESCENT.md`.
   That next reduction is also exact.  For weighted uniform `t`-petals and
   their `k`-shadows,

   \[
    \sum_Is(I)={t\choose k}W,\qquad
    \sum_Is(I)^2=\sum_{D,D'}w_Dw_{D'}
                       {|D\cap D'|\choose k},             \tag{EIC'o14}
   \]

   and `W binom(t,k)<=Lambda_kV`.  A heavy shadow fixes `I`, enlarges the
   recoverable base to `B union I`, and leaves rank `t-k` residual petals.
   Moreover the face link relative to this base factors exactly as a join
   over the components of the relative bad-circuit graph.  Hence low
   shadow codegree and disconnected residuals are finished.  But a central
   square-preserving descent is false: an `L`-ary transversal fibre has

   \[
           M=L^t,\qquad
           \sum_Id(I)^2=M^2{{t\choose k}\over L^k}.       \tag{EIC'o15}
   \]

   For `k=t/2`, `L=D^delta`, `t=kappa log D`, this loses a leading
   `Theta((log D)^2)` number of bits in one step, even with the actual mark,
   tangent cell, shield, and prefix fixed; its relative circuit graph can be
   connected.  The missing datum is therefore a canonical first-divergence
   container together with its oriented local alphabet profile.  The radial
   example pays precisely through the `L^k` omitted alphabet faces that the
   undirected component graph forgets.  See
   `agent_common_shield_mixing/OMITTED_PETAL_SHADOW_COMPONENT.md`.
   On the low-rank minimizer slice, `(3h)` now rules out the strongest known
   common-cage escape: a positive-mass family with logarithmic guards and an
   almost-linear repair alphabet either pays by the two profile banks, or
   forces `n^{Omega(1)}` canonical guard profiles at one root.  A single
   polylogarithmic-rank carrier cannot support the required quadratic source
   entropy.  Hence a successful first-divergence theorem may assume genuine
   **profile entropy across outer contexts**.  Its sharp task is to turn the
   resulting root/guard face reservoir into a square-preserving bank for the
   omitted alphabet word, or to show that high-profile contexts have enough
   recoverable outer divergence to multiply by the common pocket shields.
   Absolute profile faces alone do not suffice.  The fixed-root
   first-divergence theorem `(3i)` closes diverse carriers and every guard
   fibre below the sharp entropy threshold `kappa=2gamma`; `(3j)` realizes
   the stalled truncated-cube branch with actual logarithmic-rank planar
   sources.  But that regression has only polynomial marked mass.  The final
   global task is therefore to sum quadratically many heavy carrier fibres:
   construct a second recoverable bank for their completion/shadow outputs,
   or prove that their aggregate carrier variation creates the missing mixed
   faces.  The summation itself is now exact in `(3k)`--`(3m)`: one global
   Cauchy step pays all roots and carriers, closing every fibre with enough
   Kruskal--Katona surplus.  The last profile bin is consequently much
   sharper: `Theta(V)` weighted mass spread over high, incomplete logarithmic
   guard layers whose downshadow is essentially no larger than the layer,
   even after the explicit root/guard decoder loss.  Complete and
   four-trace-covering layers are now removed by `(3n)`--`(3p)`: planar
   four-locality lifts them to the full Boolean union bank and the global
   decoder closes every superlogarithmic support.  No bounded-rank planar
   family realizing the remaining central bin is known.  The next theorem
   should prove stability around four-trace coverage, or convert the
   uncovered four-traces of a sparse `s=O(log n)` layer into a second
   recoverable shield/completion bank.  The carrier-local version of that
   proposal is now false by `(3q)`--`(3s)`: even the full cube can have zero
   mixed compatibility with the pocket.  Globally, `(3t)`--`(3u)` removes
   the low-overlap slice and forces cross-fibre collision energy, while
   `(3v)`--`(3x)` now aggregates the fixed-anchor decoder with one global
   Cauchy step.  It closes whenever the top-group and cross-top reuse
   exponents satisfy `2kappa+alpha+beta<1`.  The sharp residue is therefore a
   fixed-power **root--shield star**: many distinct ordinary top shields share
   one completion face, carrier, pocket label, and retained edge but have
   distinct missing roots.  The downset/half-plane release `(3y)` closes
   every low-overlap linear-carrier branch.  Its exact final divergence fixes
   one actual `(x,z)` while varying the retained edge, carrier, and top shield.
   Pairing with the completion face now recovers that entire divergence with
   polynomial fibre by `(3z)`.  The remaining step is quantitative rather
   than descriptive.  The full blocker alphabet splits the normalized
   energy exactly into diagonal and collision pieces by `(3ah)`.  Collision
   dominance fixes a genuine completion/blocker/edge profile at polynomial
   loss; low source entropy is already paid by the detached alphabet through
   `(3ai)`.  Hence the last branch is diagonal-dominated energy spread over
   quadratic-entropy source support.  The complete-layer planar regression
   following `(3ab)` shows that no local carrier, guard, or pair decoder
   statement can close it; `(3ac)`--`(3ae)` show the same even for the full
   formal four-local bank system with only logarithmic source-mark load.
   Planarity does not forbid the perpendicular rectangle: `(3af)`--`(3ag)`
   give a genuine three-arc realization.  Its payment is a full detached
   convex outer shield.  The exact missing theorem is therefore a global
   **rectangle-or-shield telescope**: after quadratic-entropy variation of
   sources and blocker alphabets, either a mixed/forward bank survives with
   bounded aggregate overlap, or the detached outer and blocker shields can
   be charged without spending a fresh copy of `V` per context.
2. Prove the **hierarchical** fan-stability compatible multiplication following
   (23j)--(23k).  The only unresolved family now consists of
   `Theta(r)` interchangeable **long** hidden ears over a
   quadratic-entropy retained-target family, all arising from
   outward-successor repairs `A=(T-p) union I`.  Show that adjacent tangent
   cells release a two-ended oriented surplus relative to the source
   family, that a fixed marginal descends into prefix complexes with only
   `2^{o(r)}` cumulative reuse, or that both interiors recurse while the
   descendant two-ended mass pays.  Short ears, sparse support,
   marginal-density surplus, and absolute cloud counting are already
   settled.  An equivalent sharp target is a two-record/C4 uncrossing whose
   recursively produced pair of convex faces has only `2^{o(r)}` global
   fibre.  The balanced full-product case now has fibre at most four, and
   endpoint incompatibility has been reduced to long insertion-poset chains.
   At leading-coefficient scale, (23n5)--(23n6) already settle actual
   rectangle extraction and terminal-pair reuse.  The stronger weighted
   shortcut `(23n6c)` is proved on every ordinary-`C_4`-free support by
   `(23n6e)`--`(23n6f)`, but is false in general and fails by an unbounded
   factor on the pendant-complete-core family `(23n6g)`--`(23n6h)`.  Any
   replacement must exploit the repair graph's degree cap,
   near-biregularity, or geometric/history structure; no universal
   weighted-to-counted theorem remains.  Helpful low-product rectangles also
   cannot simply be dropped: the `K_(3,4)`-plus-leaf example kills
   positive-part charging against the explicit edgewise `delta` slack.
   The immediate geometric target is
   now a **pair-valued component-surplus recursion**: when one marginal of
   the repair graph has higher entropy per rank, recurse without discarding
   the other marginal's constant fraction of quadratic entropy.  Prove that
   the two pieces can be carried to a later near-product node within the same
   two-face budget, or charge the discarded piece to a convex-face complex.
   Merely selecting the denser marginal is insufficient.  The planar
   unequal-alphabet lens regression shows exactly what remains: a local
   source-pair or endpoint spend costs only `Theta(r)` bits, so it is harmless
   once but not at `Theta(r)` independent levels.  Establish a label-faithful
   full-history decoder with only `o(r)` unpaid levels, a joint endpoint-code
   telescope, or an induction charging long-chain descendants to their
   internal convex-face complexes.  For the stronger capped route, the
   symmetric one-slot code and guarded prefix Hall theorem remain relevant,
   but they are no longer the coefficient-scale bottleneck.
   The universal-chain equivalence (23n8) rules out treating the last clause
   as a purely local chain lemma: even two unrestricted internal-pocket
   outputs already restate the desired coefficient.  A genuinely narrower
   target must exploit a capped ancestor telescope which can **release both
   tangent guards** and later recover the erased outer state.  Literal joint
   coexistence with the retained outer component is false, while the
   top-window cap is automatic by (18a).  The first unresolved scale is
   therefore `r=(alpha+o(1))log n` with fixed `alpha<1`: prove a guard-release
   telescope there, or show that its selected pocket histories are paid by
   ordinary pocket/core faces.  Fixed-core and common-core same-edge chains
   are now closed even at this scale; the exact residual is a
   **quadratic-entropy crossing-core theorem**.
3. Equivalently, prove the peak mean bound
   `mu_1>=log_2 n-O(log log n)`.  The KL identity (16) then completes the
   deletion induction without any finite `H<=2` statement.  The hull-root
   route now has the independent exact target `(16z20)`--`(16z24)`:
   prove the cumulative one-seam Pareto curvature, with the sharp pointwise
   sufficient scale $K_{n,1}\ge(1-o(1))f(n)\log n/n$.  Chartwise hinged
   Kraft cannot supply it.  Root choices themselves do satisfy a universal
   concatenable Kraft law, but `(16z29)` shows that the canonical
   shelling-to-face decoder has exactly total shelling weight on every
   output for every reweighting.  The minimax bound `(16z31)`--`(16z33)`
   closes even omniscient noncanonical remapping of any positive fraction:
   it still has fibre $(1-o(1))W$.  The only surviving shelling operation
   is to select an $o(1)$ fraction of exceptionally valuable tags and prove
   that this sparse subledger carries the full curvature, or to prove the
   curvature directly without a shelling decoder.  Equations
   `(16z34)`--`(16z37)` now construct that sparse curvature layer
   exactly, but show that its native cap portion still has a common hull-face
   collision of load $W$.  The live sparse branch must therefore transport
   almost all curvature through child excess, or replace native cap tags by
   genuinely new geometric outputs; large hulls are already paid directly.
4. In the vector recurrence, retain full two-dimensional tangent ranks and
   the internal block/pocket polynomial.  Scalar `(C,U,V)` profiles and
   atomic all-interval sums are now ruled out, so every proposed Bellman
   inequality must be tested on the sharp gradient and product-grid
   regressions.
5. In parallel, attack the once-per-root unit type-A reflection-order
   matrix inequality in the quantitatively dense two-sided regime.  The
   exactly-one-sided and sparse-defect cases are closed by
   `(23r2a)`--`(23r2d)`, so any counterexample has more than
   `(2-o(1))n^2/(log n)^4` two-sided endpoint pairs and, consequently,
   the much stronger rank-four mass and rooted trace star in
   `(23r2e)`--`(23r2f)`.  Compatible higher histories and their global decoder
   are now completely described by `(23r2g)`--`(23r2i)`: two endpoint tangent
   comparisons are necessary and sufficient, and the total rank-`k` output
   load is at most `k-1`.  The Kraft reset `(23r2j)`--`(23r2l)` further closes
   the local spend-versus-deep-pocket dichotomy with global rooted-face load
   one: every unpaid side resets to an explicit near-full hidden pocket, and
   incompatible opposite resets identify a strictly progressing tangent
   guard.  The open step is therefore no longer a one-level profile
   inequality.  It is to telescope failed-guard resets through potentially
   linear depth while retaining information absent from one chain's face
   complex.  The projective construction `(23r2o)`--`(23r2q)` shows that a
   full-pocket singleton reset chain can encode an arbitrary planar order
   type, with zero parent-child coexistence and face-history load up to `L`;
   the Boolean cap in `(23r2n)` was nongeneric.  Thus a standalone cross-level
   discarded-face theorem is coefficient-equivalent to #838.  The only
   surviving targets must correlate multiple reset chains, preserve the
   terminal/source/repair history, or exploit the monotone
   one-healing-per-guard chronology.  Even two synchronized full-ACP chains
   do not suffice: `(23r2r)`--`(23r2t)` show that their quadratic chronology
   collapses to linear actual incidence support, while `(23r2u)` closes every
   common-ear or common-blocker fibre.  The true residue varies both marks
   across different terminal targets (or has nonsingleton ears).  For
   singleton ears, `(23r2w)`--`(23r2x)` now resolve every common-core mark
   rectangle: it either yields two injectively decoded ordinary faces or one
   canonical rooted `1+3` nesting circuit.  The full tensor `(23r2y)` sends
   every rectangle to the circuit branch and saturates all three projection
   counts, so projection entropy is exhausted.  The live theorem is an
   aggregate rooted-circuit core--mark telescope, exactly parallel to the
   rectangle-or-shield target in item 1.  Positive inverse identities, scalar
   hull diagonals, and `T` alone are likewise insufficient: the matching-star
   regression has `q^2m` repeated rank-four extensions and no higher
   outer-cloud face at all.  The coherent-root audit `(23r2z18)`--`(23r2z24)`
   further excludes every homogeneous/subface Hall lift at the full history
   scale and then excludes local label-retaining promotion even into all
   recursive mixed cap--cup banks: one terminal $E(k,3)$ cup forces
   $m^{1/2-o(1)}$ load.  But `(23r2z25)`--`(23r2z28)` now give the exact
   positive model: the top mixed bank of $E(k,k)$ assigns every history a
   private block with output load and recovery fibre one.  The remaining
   operation cannot be the local weighted-Hall/profile-contraction
   inequality `(23r2z29)`: the matching star `(23r2z33)` forces linear load
   already at rank three.  Every such stress has a fibre-one detached-side
   code `(23r2z35)`, but it erases the trace and can be reused across
   $|J||L|$ cells as in `(23r2z36)`.  Equations
   `(23r2z37)`--`(23r2z41)` settle this stress exactly:
   every rank-at-most-three joint alphabet has polynomial Hall load, whereas
   pooled rank four gives constant load and rank five gives fibre one; the
   same pooled code handles all coherent roots of $E(k,k)$ at once.  The
   remaining operation is therefore an arbitrary-order theorem producing
   enough bounded-rank detached/mixed bank capacity, or a profile charge for
   its absence.  Mixed successes already globalize with the sharp rank
   factor `(23r2z31)`.  The global ES(4) code
   `(23r2z42)`--`(23r2z46)` removes even that capacity
   hypothesis for every literal rank-three history, and more generally
   gives \(n^{o(1)}\) replacement through every
   \(r=o(\sqrt{\log n})\).  Identity handles \(r\ge\log n\).  Hence the
   unresolved local range is
   \(\Omega(\sqrt{\log n})\le r<\log n\), or nonliteral path multiplicity
   not recovered by support.
6. Test every proposed inequality on central Pascal cells, the exact
   20/24/30-point half-weight records, the alternating least-index family,
   and the two-deep-endpoint wrapper before promoting it.

At present, (RE), (IDP*), (16)'s peak-mean hypothesis, (17)--(18), and the
target-face pocket allocation are conjectures.  The full restriction-peak
hierarchy (16a)--(16c) is proved, but its sharp rank-truncation barrier shows
that it cannot replace the planar repair gate.  Claiming the unrestricted
problem solved before one of these gates is proved would be incorrect.
