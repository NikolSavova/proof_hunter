# Pathwise projection itineraries: exact compression and the fixed-gap slack barrier

**Date:** 2026-08-15. This audits the proposed \(PGL_2\) route out of the
strictly internal child gate in
LINEAR_ENDPOINT_MODULE_ALIGNMENT_BARRIER.md.

## Verdict

The semialgebraic compression claim is correct under its natural fixed
data:

> For one fixed \(N\)-point order type \(X\) and one fixed ordered
> \(h\)-tuple of source directions, all projection-chamber itineraries
> obtained by one \(PGL_2^+\) reparameterization fall into only
> \(O((hN^2)^3)\) classes.

Thus an exact full itinerary costs only
\(O(\log N+\log h)\) bits, not \(h\log N\). At
\(h=\Theta(L/\log L)\) and \(N=2^L\), this is \(O(L)\), a genuinely
subquadratic loss.

This does **not** yet apply to the live branching coherent-ramp residue.
Three separate hypotheses fail:

1. branch paths need not have a common source-direction tuple; after the
   first three directions, their cross-ratios record recursive gauge
   history;
2. the marked children at different ramp levels may be different order
   types, so the exact chamber classes are not shared; and
3. most importantly, only \(O(1)\) recent ancestor queries are
   quantitatively tight at the fixed-gap scale. After two levels, the
   target-scale slack already exceeds the entire
   \(\Theta(L\log L)\) multiplier one is trying to recover.

There is no literal geometric node forgetting: every ancestor direction
does restrict to a direction of the final physical subconfiguration. The
failure is analytic. Old directions coexist, but their inherited
cap/cup upper bounds are too loose to calibrate the descendant profile.

The exact positive statement is therefore conditional:

> If a reservoir consists of projectively equivalent copies of one
> completed child, shares one marked ancestor-direction tuple, and has
> \(h\) genuinely tight endpoint-profile queries, then one exact
> itinerary class retains a \(2^{-O(L)}\) fraction of the reservoir.

The present recursive menu supplies neither the common tuple nor
\(h\) tight queries. This report is a theorem plus a sharp applicability
barrier, not a closure or a counterconstruction.

## 1. Hyperplane itinerary theorem

Fix a planar general-position order type \(X\) on \(N\) labeled points.
Its generic projection chambers on the unoriented projective direction
line are separated by at most

\[
                         K=\binom N2                              \tag{1}
\]

critical pair directions. Fix source directions
\(\Theta=(\theta_1,\ldots,\theta_h)\).

Represent an orientation-preserving projectivity by

\[
             \phi(t)=\frac{at+b}{ct+d},\qquad ad-bc>0.            \tag{2}
\]

For a critical direction \(\lambda\), the event
\(\phi(\theta_s)=\lambda\) is

\[
 \theta_s a+b-\lambda\theta_s c-\lambda d=0.                    \tag{3}
\]

This is a homogeneous hyperplane in the projective three-dimensional
parameter space \([a:b:c:d]\). There are at most \(m=hK\) such walls.
Inside one cell of their complement, every \(\phi(\theta_s)\) stays in
one fixed projection chamber of \(X\). Hence the complete \(h\)-tuple of
projection orders, cap counts, cup counts, endpoint modules, and
orientation-defined tangent states is fixed.

An arrangement of \(m\) hyperplanes in dimension three has
\(O(m^3)\) cells. Restriction to the determinant-positive component and
the finitely many affine coordinate patches changes only the absolute
constant. Thus

\[
 \boxed{\#\{\text{exact itineraries}\}\le
        c_0(1+hN^2)^3}                                           \tag{4}
\]

for an absolute \(c_0\).

Consequently a family of \(M\) copies satisfying the fixed-\(X\),
fixed-\(\Theta\) hypotheses contains an exact-itinerary subfamily of
size at least

\[
                         \frac{M}{c_0(1+hN^2)^3}.                 \tag{5}
\]

When \(N=2^L\), the loss in (5) is \(2^{O(L+\log h)}\).

This proof is simpler than weighted semialgebraic regularity: the query
walls are literally linear in the homogeneous \(PGL_2\) parameters.

## 2. Numeric profile words across different order types

There is a weaker statement which does not require a common order type.
If every child is low-face in the sense

\[
                         H(X)\le2^{K_0L^2},                       \tag{6}
\]

then \(C(\theta),U(\theta)\le H(X)\) in every direction. In base
\(N=2^L\), both endpoint exponents lie in an interval of length
\(O(L)\). Discretizing them into unit base-\(N\) bins gives
\(O(L)\) possibilities per query. Therefore \(h\) queries have at most

\[
                         O(L)^h                                  \tag{7}
\]

numeric bin words. At \(h=\lfloor L/\log_2L\rfloor\),

\[
                         \log_2 O(L)^h=O(L).                      \tag{8}
\]

This confirms the proposed entropy arithmetic.

But (7) forgets the physical order type, endpoint labels, circuit
supports, and projective source tuple. It can support a purely scalar
argument only. The exact scalar first-cap/last-cup ramp already survives
such homogenization, so (7) alone does not advance the internal planar
gate.

## 3. Branch histories do not share one source tuple

For siblings embedded in one fixed parent, the parent and higher
ancestor directions are common. Along different depth-\(h\) branches,
however, the intermediate construction/reset charts are chosen at
different nodes. Their ordered direction tuples need not lie in one
\(PGL_2\) orbit.

The obstruction begins at four directions. For example,

\[
 \Theta=(0,1,2,3),\qquad \Theta'=(0,1,2,4)                       \tag{9}
\]

have cross-ratios

\[
 [0,1;2,3]=\frac43,\qquad [0,1;2,4]=\frac32.                    \tag{10}
\]

No projectivity maps one marked tuple to the other. A final leaf
embedding acts by only one \(PGL_2\) map, so it cannot erase these
branch-history cross-ratios.

Thus (4) can be used inside a reservoir with one fixed ancestor tuple,
but not across the full recursive tree without first paying for or
controlling the tuple history. The number of possible histories is not
bounded by the one-tuple arrangement count.

## 4. The decisive fixed-gap slack calculation

Even on one physical ancestry path, the old queries are not all tight.
Write the logarithmic size at one level as \(L\), let one fixed-gap step
decrease it by

\[
                         \ell=\Theta(\log L),                     \tag{11}
\]

and take the coefficient-\(c\) target

\[
                         \Phi(L)=cL^2+o(L^2).                     \tag{12}
\]

A descendant \(k\) levels lower has logarithmic size approximately
\(L-k\ell\). The difference between the ancestor endpoint-product
budget and the descendant face lower bound is at least

\[
\begin{aligned}
 S_k
 &=\Phi(L)-\Phi(L-k\ell)\\
 &=2ckL\ell-ck^2\ell^2+o(kL\ell).                               \tag{13}
\end{aligned}
\]

The entire one-level multiplier that the fixed-gap argument must recover
is

\[
 G=\Phi(L)-\Phi(L-\ell)
   =2cL\ell-c\ell^2+o(L\ell).                                   \tag{14}
\]

Already

\[
                         S_2>G                                  \tag{15}
\]

for large \(L\). More generally \(S_k=(k-o(k))G\) while
\(k=o(L/\ell)\).

Why this is the relevant slack: a cap or cup contained in a descendant
is also a cap or cup of every ancestor in the induced direction.
Ancestor profile bounds therefore give upper bounds on the descendant
counts. To pin the two descendant counts, one subtracts their product
lower bound \(H_{\rm desc}\ge2^{\Phi(L-k\ell)}\) from the two inherited
upper bounds. Equation (13) is unavoidable even if the ancestor
endpoint product is otherwise perfectly tight.

Hence only \(O(1)\) most recent ancestors can calibrate a descendant to
the \(O(G)\) accuracy relevant to the missing multiplier. A path of
length

\[
                         h=\Theta(L/\log L)                       \tag{16}
\]

does provide \(h\) geometric directions, but it does not provide
\(h\) calibrated profile constraints. Beyond constant depth, the upper
bounds allow essentially the full coherent-ramp width.

This is the main failure of the proposed pathwise \(\Pi_h\) promotion.

## 5. Differing completed child types

The live branching menu may build a different marked completed type
\[
                         (X_k;\alpha_k,\beta_k)                   \tag{17}
\]
for each desired ramp level. Formula (4) compresses embeddings of one
fixed \(X_k\); it does not pigeonhole the \(X_k\)'s themselves.

Numeric bins can be homogenized using (7), but selecting one common word
also selects one profile level and discards the width needed by the
ramp. A circuit or endpoint-module theorem needs common physical labels
or a uniform geometric statement valid across the differing types.
Neither is supplied by itinerary counting.

This is exactly the distinction between a stationary recursion and the
branching decorated two-mark menu. The stationary subclass may still be
attacked by (4); the general menu is not reduced to it.

## 6. What remains usable

The compression theorem is worth retaining. It can be invoked without
quadratic entropy loss once another argument produces all three of:

1. a common completed child order type (or a uniform theorem independent
   of that type);
2. a common marked ancestor-direction tuple up to \(PGL_2\); and
3. more than constantly many tight profile constraints on the same
   physical child.

Under those hypotheses, (5) preserves every fixed-power and
coefficient-scale bank in the current proof.

Without them, the internal residue from
COHERENT_RAMP_ENDPOINT_MODULE_LOCALIZATION.md remains:
many low-surplus rooted endpoint products, possibly carried by different
completed child types and queried tightly in only their current assembly
and one reset chart.

## 7. Verification

Run

    python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_pathwise_projection_itinerary_compression_gate.py

The exact verifier:

* checks the homogeneous wall identity (3) on 452 rational
  determinant-positive projectivities;
* records 110 sampled exact itineraries, below the dimension-three
  arrangement bound 1351;
* verifies the incompatible cross-ratios in (10);
* checks the exact quadratic slack (13)--(15) at
  \(L=32,64,128,256\); and
* checks that the numeric word entropy in (8) is about \(L\) bits at
  \(L=64,256,1024,4096\).

Expected output begins:

    PASS: PGL2 query walls are linear, sampled itineraries obey the RP3 region bound
