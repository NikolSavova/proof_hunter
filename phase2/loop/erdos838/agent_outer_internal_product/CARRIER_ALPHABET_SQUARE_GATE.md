# Carrier alphabets: a global square gate and the exact dense residue

**Date:** 2026-08-15.  All logarithms are base two and the empty face is
counted.

## Verdict

The planar carrier--root rectangle is not locally forbidden.  The exact
three-arc construction in
`agent_common_shield_mixing/EXTERNAL_ALPHABET_ENERGY_TRICHOTOMY.md` realizes
complete bipartite carrier reuse and pays through a detached convex outer
shield.  The strongest unconditional replacement is therefore global.

Suppose `s` rooted profile occurrences each carry `R` distinct carrier
edges, using at most `D` endpoint labels in that profile, and suppose the
carrier layer is quadratically dense:

\[
                         R\ge\eta D^2.                    \tag{1}
\]

Let `A` be the union of all actual carrier endpoints.  Then one profile
already gives `|A|>=d_R`, where

\[
 d_R=\min\{d:{d\choose2}\ge R\}
     =\left\lceil{1+\sqrt{1+8R}\over2}\right\rceil.       \tag{2}
\]

If the profiles project to ordinary faces with load at most `lambda`, the
global record set `mathcal R` satisfies

\[
 \boxed{
 { |\mathcal R|\over V(P)}
 \le\min\left\{\lambda R,
                {sR\over f(d_R)}\right\}.}                \tag{3}
\]

No copy of `V(P)` is spent per root, carrier, or profile.  If the endpoint
union `A` is itself convex, `f(d_R)` in (3) improves to `2^{d_R}`.  This is
exactly the detached shield that discharges the three-arc rectangle.

For arbitrary endpoint order type, the established bound

\[
 \log f(d_R)\ge(1/16-o(1))(\log R)^2                     \tag{4}
\]

shows that failure of an `R^epsilon` saving forces quadratic profile
entropy:

\[
 \log s\ge(1/16-o(1))(\log R)^2-\epsilon\log R.          \tag{5}
\]

The real complete-middle source load is exactly `r+1`, not one.  If `s_0`
counts unmarked source profiles and every one has at most `mu=r+1` root
marks, replace `s` by `mu s_0`; the sufficient condition becomes

\[
 s_0\le {f(d_R)\over (r+1)R^\epsilon}.                   \tag{6}
\]

Thus the logarithmic mark load costs only the explicit subtractive term
`log(r+1)` in (5).  The unresolved case is now sharp: quadratically many
profile contexts, quadratically dense carrier alphabets, and endpoint
order types whose detached reservoirs are globally reused.  A further
fixed-power theorem must multiply those child reservoirs or recover a
common endpoint pocket; planarity alone does not delete the rectangle.

This report is a rigorous gate, not an EIC' closure.

## 1. Global endpoint-alphabet theorem

Let `P` be a planar general-position set and `V(P)` its number of convex
subsets.  Let `Pi` be a set of `s` rooted profile occurrences.  Assume:

1. each `pi in Pi` has an ordinary key face `K_pi`;
2. every ordinary face is the key of at most `lambda` profiles;
3. each profile has a simple carrier graph `G_pi` with exactly `R` edges;
4. every endpoint of every `G_pi` is an actual label of `P`.

Write

\[
 \mathcal R=\{(\pi,e):\pi\in\Pi,\ e\in E(G_\pi)\},
 \qquad |\mathcal R|=sR.                                  \tag{7}
\]

> **Theorem 1 (carrier-alphabet square gate).**  Equation (3) holds.  If
> the global endpoint union is convex, then
> 
> \[
> { |\mathcal R|\over V(P)}
> \le\min\left\{\lambda R,{sR\over2^{d_R}}\right\}.       \tag{8}
> \]

**Proof.**  The key-face map has load `lambda`, so `s<=lambda V(P)`.
This gives the first term of (3).

Choose any profile.  A simple graph with `R` edges has at least `d_R`
vertices, so the global endpoint union `A` has at least `d_R` labels.  Every
convex face of the induced point set `P|A` is an ordinary face of `P`.
Restricting further to any `d_R` labels gives

\[
                         V(P)\ge V(P|A)\ge f(d_R).         \tag{9}
\]

Together with `|mathcal R|=sR`, this gives the second term of (3).  If `A`
is convex, all its subsets are ordinary faces and (9) strengthens to
`V(P)>=2^|A|>=2^{d_R}`, proving (8).  QED.

The theorem also holds when every degree is only at least `R`: select the
first `R` carrier edges canonically in each profile.  Dyadic degree and
endpoint-rank bins cost only `n^o(1)` on the logarithmic-rank slice.

## 2. Exact entropy consequence

For every fixed positive `epsilon`, the second term in (3) gives

\[
                         |\mathcal R|\le R^{1-\epsilon}V(P)          \tag{10}
\]

whenever

\[
                         s\le {f(d_R)\over R^\epsilon}.    \tag{11}
\]

Since `d_R=R^(1/2+o(1))`, the quarter-coefficient lower bound for `f`
becomes (4), and negating (11) gives (5).  If profiles arise by marking
unmarked sources with at most `mu` roots, then `s<=mu s_0`; condition (6)
is sufficient.

In a complete middle layer on `W setminus {z}`, `|W|=2r+1`, the mark load
is not merely bounded but exact.  The identity

\[
 (2r+1){2r\choose r}=(r+1){2r+1\choose r+1}              \tag{12}
\]

says that each unmarked root set of size `r+1` is represented once for
each of its `r+1` possible distinguished roots.  Therefore

\[
 \log s_0\ge(1/16-o(1))(\log R)^2
              -\epsilon\log R-\log(r+1)                 \tag{13}
\]

is necessary for this global detached-alphabet discharge to fail.

## 3. What planarity adds, and what it does not

For one fixed actual `(x,z)` profile, put `x=(0,0)`, `z=(0,1)`, and write
carrier endpoints on opposite sides of `xz` as

\[
                         u=(-a,b),\qquad v=(c,d),qquad a,c>0.
\]

Then

\[
 x\in\operatorname{int}\triangle(u,v,z)
                 \quad\Longleftrightarrow\quad {b\over a}+{d\over c}<0.
                                                               \tag{14}
\]

Thus the **full geometric availability graph** is Ferrers after sorting
the two ratios.  If it has `m` edges and smaller side size `t`, it contains
a complete bipartite rectangle with at least `m/H_t` edges.

This conclusion must be used carefully.  A canonical central-cell family
may select an arbitrary subgraph of the availability graph because the top
shield and history conditions vary.  An arbitrary subgraph of a Ferrers
graph need not itself be Ferrers and need not contain a large biclique.
Hence (14) yields a large recoverable rectangle only in a carrier-complete
fibre, or after a separate density/completion argument proves that most
available edges are present.

In the carrier-complete case, the alternatives are exact:

* the extracted endpoint union is convex, and its full Boolean shield pays
  by (8);
* it is not convex, but its induced face complex still pays `f(d_R)` by
  (3);
* if that global bank is too heavily reused, (13) forces quadratic profile
  entropy and the problem localizes to the endpoint child order type.

The three-arc construction realizes the first alternative.  Projective
substitution into its endpoint arcs shows why the second and third cannot
be replaced by a universal local mixed-face claim.

## 4. Relation to the live weighted mass

Theorem 1 counts simple profile--carrier records.  In a uniform weighted
bin, if every such record carries weight `w`, multiply the right-hand sides
of (3), (8), and (10) by `w`.  Equivalently one may expand integer weights
into labelled marked occurrences.  For the central complete layer it is
usually cleaner to index unmarked sources and take the explicit root-mark
factor `mu=r+1` from (12).

Applying the theorem end-to-end therefore still requires a canonical map
from the live marked cells to profile--carrier records with bounded key
load `lambda`.  The completion--half-plane decoder supplies the relevant
polynomial guesses once `(x,z)` is retained, but this report does not assume
that all top/history selections form the full Ferrers availability graph.
Those are the two honest remaining gates: global key load and selected-edge
completion.

## 5. Verification artifact

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_carrier_alphabet_square_gate.py
```

The verifier checks the minimal endpoint formula, both global capacity
bounds on a finite loaded-key system, the exact `r+1` identity, and the
Ferrers rectangle extraction inequality on exhaustive monotone degree
sequences.
