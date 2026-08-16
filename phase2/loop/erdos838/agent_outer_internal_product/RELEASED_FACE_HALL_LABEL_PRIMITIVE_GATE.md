# Released-face Hall routing ends at a dense face--face core, not automatically at labels

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

The nonprimitive released-face alphabet has an exact global Hall
dichotomy.  Give every record its two actual ordinary targets

\[
                           A_\omega,qquad F_\omega.     \tag{1}
\]

Fractional routing to these targets either charges the entire record mass
with bounded face load, or produces a weighted source--released-face core
of high minimum degree.  After the rank-safe source-internal state is
compressed, a fixed pair `(A,F)` has weight at most

\[
                         |F|\delta\le n\delta,          \tag{2}
\]

where `delta` is the load of one actual `(A,F,x)` label record.  Thus a
core of minimum weight `K` has at least `K/(n delta)` distinct opposite
faces at every vertex.  With

\[
 \delta\le2^{(C_L+o(1))L\log L},qquad
 K=2^{\sigma L\log L},qquad \sigma>C_L,               \tag{3}
\]

this is still a quasipolynomial number of genuine neighbors.

This proves the desired `bounded-overlap released-face bank` branch.  It
does **not** prove that the high branch is label primitive.  Fixing an
actual `F` and one projected label `x in F` leaves a large alphabet of
ordinary **source faces** `A`, not a physical cloud of that many point
labels.  The triangle-tag theorem cannot replace a face alphabet of size
`a` by `{a choose3}` ambient triangles.

The failure is sharp and planar.  Two anti-aligned parabolic `p`-point
clouds, with both alphabets equal to all rank-`r` faces (`r>=3`), give a
complete

\[
                  M\times M,qquad M={p\choose r},      \tag{4}
\]

source--released-face graph.  Every row and column is ordinary, every
mixed union is bad, the Hall density is exactly `M/2`, and every fixed
released face has `M` distinct source neighbors.  The pair load is one and
there is no metadata.  After fixing the released face and its canonical
column label, the remaining `M` objects are still faces supported on only
`p` physical labels.

At `r=Theta(loglog p)`, `M=p^{Theta(loglog p)}`, exactly the terminal
quasipolynomial scale, while the face ranks remain below the rank-safe
cutoff.  The construction exposes detached Boolean cloud banks, so it is
not a hard minimizer counterfamily.  It proves that the strongest exact
global statement currently available is:

> low Hall density charges actual released faces; high density localizes
> to a dense face--face core.  Turning that core into label-primitive
> records requires an additional physical-support/projection theorem, or
> charging a detached/internal face bank with bounded global overlap.

Thus the proposed label-primitive-or-face-bank interface is a valid
three-way gate, not a completed dichotomy.

## 1. Exact two-target fractional Hall theorem

Let `Omega` be a finite weighted record family.  Each record `omega` has
weight `w_omega>=0` and the one- or two-element target set

\[
                     \mathcal B_\omega=\{A_\omega,F_\omega\},    \tag{5}
\]

where duplicate targets are identified.  Both targets are actual ordinary
faces.  Put

\[
 \eta_*=max_{\varnothing\ne\Omega'\subseteq\Omega}
   {\sum_{\omega\in\Omega'}w_\omega\over
    |\bigcup_{\omega\in\Omega'}\mathcal B_\omega|}.    \tag{6}
\]

> **Theorem 1 (source--released-face Hall routing).**  The record weights
> admit a fractional routing to their targets with maximum face load
> `eta_*`.  Consequently
>
> \[
>                       \sum_\omega w_\omega\le\eta_*V(P).       \tag{7}
> \]

**Proof.**  Use a source-to-record-to-target-to-sink flow network.  Give
record `omega` incoming capacity `w_omega`, its target arcs infinite
capacity, and every target-to-sink arc capacity `eta`.  The max-flow/min-cut
conditions are exactly the inequalities in (6).  At `eta=eta_*` all
weight routes.  There are at most `V(P)` actual target faces, proving (7).
QED.

This theorem uses one global `V(P)`, not one copy per source, root, state,
or released face.

## 2. High-density core and the exact pair cap

If a subfamily `Omega'` has total weight greater than `K` times the number
of its target vertices, repeatedly delete a target vertex of current
incident weight at most `K`, together with its incident records.  Charge a
record when its first target is deleted.  If every vertex disappeared, the
total charge would be at most `K` times the original number of vertices, a
contradiction.

> **Lemma 2 (weighted dense core).**  If `eta_*>K`, some nonempty induced
> record core has minimum weighted target degree greater than `K`.

Now suppose every released face carries a canonically selected projected
column label `x_omega in F_omega`.  After fixing one actual triple
`(A,F,x)`, all remaining source-internal states are those counted in
`POLYNOMIAL_DESCRIPTION_LOAD_FACE_ALPHABET_BARRIER.md`.  Let

\[
 \delta=\max_{A,F,x}
    \sum_{\omega:(A_\omega,F_\omega,x_\omega)=(A,F,x)}w_\omega.   \tag{8}
\]

The exact dyadic state theorem gives

\[
                  \delta\le2L_{src},qquad
                  \log L_{src}\le(C_L+o(1))L\log L,    \tag{9}
\]

provided no further actual external face word remains.  Since `x in F`,
there are at most `|F|` choices for `x`, and therefore

\[
 \sum_{\omega:(A_\omega,F_\omega)=(A,F)}w_\omega
                         \le |F|\delta\le n\delta.      \tag{10}
\]

> **Corollary 3 (distinct-face expansion).**  A core of minimum weighted
> degree greater than `K` has more than `K/(n delta)` distinct opposite
> face neighbors at every source and every released-face vertex.

This is just (10).  It is nevertheless the exact scale-preserving form of
the Hall branch: (3) leaves

\[
 {K\over n\delta}
       =2^{(\sigma-C_L+o(1))L\log L}                  \tag{11}
\]

neighbors whenever `sigma>C_L`.

There is also a precise fixed-face localization.  If `F` is a core vertex,
partition its incident records by the at most `|F|<=n` projected labels.
For some `x in F`, the fixed `(F,x)` fibre has weight greater than `K/n`
and more than `K/(n delta)` distinct actual source faces.  The variable
released-face word is now gone.  What remains is a source-**face**
alphabet; it is label primitive only if an additional bounded-projection
map from these faces to physical source labels has been proved.

## 3. Why fixing `F` does not create a physical cloud

For the source--triangle tag theorem, a context with `a` source rows needs
either a physical support of comparable size or some other ordinary tag
reservoir `i` satisfying

\[
                              e^2\le\Gamma a i.         \tag{12}
\]

If a fixed-`F` fibre has `a` distinct source faces and `e=a` records, the
source bank itself handles that one star.  The difficulty is summing many
such stars when the same source faces recur across many released faces.
Replacing the `a` faces by one representative point each can have
arbitrarily high projection load; their physical support may contain only
`p=O(log a)` labels.

The hereditary rank-`k` tag theorem is an exact conditional exit, but it
does not follow from facehood.  A family of `a` rank-`r` faces has at most
`a2^r` tags in the union of all of its individual downsets, whereas a
balanced `a by a` rectangle needs order `a^3` tags in (12).  Thus the
fixed-face localization does not by itself close the dense core.

## 4. Exact anti-aligned face-core regression

Use two tiny parabolic clouds `Y,Z`, each of size `p`, in the anti-aligned
two-block chart from
`agent_common_shield_mixing/DENSE_HALL_TWO_CLOUD_PROFILE_BARRIER.md`.
Every nonempty subset of either cloud is ordinary.  Orient the clouds so
that both directional profiles facing the other block contain exactly the
singletons and pairs.  Hence a subset meeting both clouds is ordinary only
if each nonempty trace has rank at most two.

Fix `r>=3` and take

\[
                 \mathcal A={Y\choose r},\qquad
                 \mathcal F={Z\choose r},\qquad
                 M={p\choose r}.                       \tag{13}
\]

For every `(A,F)` in `mathcal A times mathcal F`, make one unit record and
let `x(F)` be the least labelled point of `F`.  Then:

* `A` and `F` are actual ordinary faces;
* `A union F` is nonconvex;
* the pair `(A,F)` has load one;
* the complete record graph has `M^2` edges and `2M` target vertices; and
* a fixed `F` (and therefore fixed `(F,x(F))`) has exactly `M` distinct
  source-face neighbors.

For any subrectangle with `a` source vertices and `b` released vertices,
the Hall ratio is at most `ab/(a+b)`, increasing in both variables.
Therefore

\[
                              \eta_*={M\over2}.         \tag{14}
\]

The number of physical source labels remains only `p`.  In particular,
fixing `F` does not turn the `M` source faces into an `M`-point cloud.

At `p=7,r=3`,

\[
              M=35,qquad |E|=1225,qquad\eta_*={35\over2}.      \tag{15}
\]

The verifier checks every mixed union and the exact Hall maximum.  At
`r=(gamma+o(1))loglog p`, Stirling gives

\[
                         M=p^{(\gamma+o(1))\log\log p}.           \tag{16}
\]

This is a scalable high-fixed-`F` obstruction with low face ranks and
unit geometric record load.  It is not a hard global counterexample: the
two convex-position clouds expose Boolean banks of size `2^p`, exactly the
detached/internal-bank exit which a complete proof must charge.

## 5. The strongest exact global gate

Given a nonprimitive terminal family, apply the following canonical
sequence.

1. Compress every source-internal state at cost (9).  If another actual
   unbounded-rank face word remains, retain it as part of `F`; do not call
   it chronology.
2. Apply Theorem 1 to the ordinary targets `(A,F)`.  If `eta_*` is below
   the required recovery multiplier, (7) closes the family with one global
   face bank.
3. Otherwise pass to the core in Lemma 2.  Equation (11) gives a genuinely
   dense simple graph of actual source and released faces.
4. If one side has a physical-support or hereditary tag reservoir
   satisfying (12), the source-tag Cauchy theorem closes it.  Without such
   a reservoir, the anti-aligned regression proves that no label-primitive
   conclusion follows from Hall density and facehood alone.

The remaining operation is therefore a bounded-overlap charge to the
detached/internal face banks, or a new marked physical-support extraction.
The released-face Hall step itself is complete.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_released_face_hall_label_primitive.py
```

Expected output:

```text
PASS: released-face Hall/core, pair cap, and anti-aligned fixed-face regression
```
