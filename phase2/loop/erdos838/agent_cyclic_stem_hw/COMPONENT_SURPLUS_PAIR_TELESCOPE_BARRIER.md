# Erdős 838: a component-surplus pair-telescope barrier

**Verdict.**  A pair-valued component recursion cannot be proved from the
entropy split, rank conservation, full prefix tags of
`2^{o(r^2)}` total complexity, and repair-`C_4` counting alone.  Tensor
powers of finite-projective-plane incidence graphs give an exact scalable
countermodel.  At every level a marginal has a genuine entropy-density
surplus, but following it retains only `2/3+o(1)` of the joint quadratic
entropy.  Endpoint pairs and all counted homomorphic `C_4` rectangles also
have only `2/3+o(1)` of the required pair exponent.  The missing factor is
`2^{Theta(r^2)}`, so no subquadratic history tag repairs the loss.

This is an **abstract support-graph countermodel**, not a stretchable planar
counterexample.  It proves that the remaining theorem must use a planar
property absent from the current entropy/Kraft formalism--for example the
cyclic-interval form of hidden ears, tangent compatibility, or a planar
restriction ruling out projective-plane incidence at many levels.  Merely
retaining all branch indices, ranks, orientations, and first-divergence
positions is insufficient.

The near-product part is already closed independently by
`REPAIR_C4_COEFFICIENT_AUDIT.md`.  The barrier here concerns the genuinely
high-mutual-information component branch.

There is also a rigorous positive theorem at the exact barrier exponent.
For every repair support for which endpoint components are ordinary faces
and ordered homomorphic rectangles have a two-face decoder of fibre `K`,

\[
 \boxed{\log_2V(P)\ge {2\over3}\log_2m-{1\over6}\log_2K.}    \tag{0}
\]

For the cross-source decoder `K<=n^2 2^{2r}`, the error in (0) is only
`(log_2n+r)/3`.  The projective-plane tensors below attain the leading
`2/3`, so no argument using just component-face supports and counted
rectangles can improve it.

## 1. The exact one-level support

Let `q` be a prime power and let `PG(2,q)` be the projective plane of order
`q`.  Its point--line incidence graph `G_q` is bipartite and biregular with

\[
 N=q^2+q+1\quad\hbox{vertices on each side},\qquad
 d=q+1,\qquad m=Nd                                             \tag{1}
\]

edges.  Two distinct points lie on exactly one common line.  Therefore the
ordered, side-respecting homomorphic `C_4` count is exactly

\[
 C=N d^2+N(N-1)=N(d^2+N-1).                                  \tag{2}
\]

The first term in (2) has the two point vertices equal.  The second has
distinct point vertices but necessarily the same line twice.  In
particular the graph has no injective `K_{2,2}`.

Under the uniform-edge law `(X,Y)`, both marginals are uniform, so

\[
 H(X)=H(Y)=\log_2N,qquad
 H(X,Y)=\log_2(Nd),qquad
 I(X;Y)=\log_2(N/d).                                          \tag{3}
\]

As `q` grows, these are respectively

\[
 2\log_2q+o(1),\quad 3\log_2q+o(1),\quad
 \log_2q+o(1).                                                \tag{4}
\]

Thus each marginal contains asymptotically two thirds of the joint
entropy, while the mutual information is the remaining third.

This is also the equality-scale obstruction to the entropy--spectral
rectangle lemma.  Equations (1)--(2) give

\[
 C=q^{4+o(1)}=m^{4/3+o(1)},qquad
 {C\over m^2}=m^{-2/3+o(1)}.                                 \tag{5}
\]

## 2. Tensoring makes a rank-compatible full history

Take the `h`-fold categorical tensor power

\[
                     G_{q,h}=G_q^{\otimes h}.                 \tag{6}
\]

A left or right vertex is an `h`-word of projective points or lines, and a
pair is an edge iff incidence holds in every coordinate.  This is precisely
a depth-`h` component history: after a prefix has been exposed, the
remaining suffix is another tensor power of the same support.  All the
counts and entropies tensor exactly:

\[
\begin{aligned}
 |L_h|=|R_h|&=N^h, &m_h&=(Nd)^h, &C_h&=C^h,\\
 H(X_h)=H(Y_h)&=h\log_2N,&&
 I(X_h;Y_h)&=h\log_2(N/d).                                  \tag{7}
\end{aligned}
\]

Assign expected component ranks `tau=kappa=h`, hence total record-rank
parameter `R_0=2h`.  The record density and the left marginal density are

\[
 \rho={\log_2m_h\over2h}={1\over2}\log_2(Nd),qquad
 {H(X_h)\over h}=\log_2N.                                    \tag{8}
\]

Their difference is

\[
 \log_2N-{1\over2}\log_2(Nd)
 ={1\over2}\log_2(N/d)=\left({1\over2}+o(1)\right)\log_2q.  \tag{9}
\]

So this is not a boundary artefact: the marginal-density surplus is
macroscopic at every suffix node.  Proposition 21 would recurse into the
left marginal.  It retains

\[
 {H(X_h)\over H(X_h,Y_h)}longrightarrow {2\over3}            \tag{10}
\]

of the joint entropy and discards the conditional neighbor word, whose
entropy is

\[
 H(Y_h\mid X_h)=h\log_2d={1\over3+o(1)}\log_2m_h.             \tag{11}
\]

Retaining all `h` level numbers and all rank/orientation states costs only
`2^{O(h log h)}`.  It does not retain the `d^h` possible conditional
neighbor words in (11).

The rank bookkeeping can be realized by an ordinary block set system, so
the obstruction is not caused by an impossible number of rank-`h` words.
Take `h` disjoint left symbol blocks and `h` disjoint right symbol blocks,
each of size `N`, and represent a word by the transversal choosing its one
symbol in every block.  Then the ambient label count is `2hN`, every
component has rank `h`, and all `N^h` component words are distinct subsets.
For `q asymptotic 2^h`,

\[
 \log_2(2hN)=(2+o(1))h,
\]

so `R_0=(1+o(1))log_2 n`, exactly the critical rank regime.  What is absent
from this set-system realization is planar convexity, not rank or label
capacity.

For a critical alphabet take, for example, a prime `q_h` between `2^h`
and `2^{h+1}`.  Then

\[
 \log_2m_h=(3+o(1))h^2=Theta(R_0^2).                          \tag{12}
\]

The conditional word in (11) has `Theta(h^2)` bits.  For an ordered pair
of histories the two missing words have `Theta(h^2)` bits each.  They
cannot be restored by a `2^{o(R_0^2)}` transcript.

## 3. Exact failure of the two-face capacity count

Suppose a proposed pair telescope is allowed all of the presently certified
abstract outputs:

1. ordered pairs of left/right component vertices at any suffix level;
2. ordered repair-rectangle outputs, one for every homomorphic `C_4`;
3. a global transcript/state multiplier `K_h=2^{o(h^2)}`.

All suffix-level component pools together have at most

\[
 O(hN^h)                                                       \tag{13}
\]

objects, since the largest depth dominates the geometric sum.  Hence their
ordered two-output capacity is `N^{2h}2^{o(h^2)}`.  The complete counted
rectangle pool has size

\[
 C_h=C^h=q^{4h+o(h)}.                                        \tag{14}
\]

Both have the same leading scale.  But the ordered record-pair count is

\[
 m_h^2=(Nd)^{2h}=q^{6h+o(h)}.                                \tag{15}
\]

Consequently

\[
 {m_h^2\over
  K_h\max\{N^{2h},C^h\}}
 =q^{2h-o(h)}=2^{(2-o(1))h^2}.                               \tag{16}
\]

Thus the proposed decoder needs a **quadratic**, not subquadratic, extra
fibre.  The full first-divergence/Kraft identity does not change (16): it
partitions the record pairs among levels, but the missing neighbor values
remain `h` independent `q`-ary symbols for each history.

The same conclusion can be phrased information-theoretically.  The endpoint
pair has entropy at most `2h log N=(4+o(1))h log q`; the record pair has
entropy `2h log(Nd)=(6+o(1))h log q`.  A state tag of `o(h log q)` bits
cannot bridge their difference.  When `log q=Theta(h)`, that difference is
`Theta(h^2)`.

### The universal `2/3` theorem

Here is the proof of (0).  Put

\[
 M=\log_2m,\qquad a=\max\{H(X),H(Y)\},\qquad v=\log_2V(P).
\]

Both endpoint supports consist of ordinary convex faces, so

\[
                              v\ge a.                        \tag{16a}
\]

Moreover

\[
 I(X;Y)=H(X)+H(Y)-M\le2a-M\le2v-M.                          \tag{16b}
\]

The entropy--spectral lemma in `REPAIR_C4_COEFFICIENT_AUDIT.md` and the
assumed decoder give

\[
 m^2 2^{-2I(X;Y)}le\operatorname{hom}(C_4,G)\le K V(P)^2.
                                                                    \tag{16c}
\]

Taking logarithms and using (16b),

\[
 v\ge M-I(X;Y)-{1\over2}\log_2K
   \ge2M-2v-{1\over2}\log_2K.
\]

Rearranging proves (0).  For projective-plane tensor powers,
`a=(2/3+o(1))M` and `hom(C4)=2^{(4/3+o(1))M}`, so both inputs to this proof
are simultaneously sharp.

One useful corollary is that a repair-history support with

\[
 \log_2m\ge\left({3\over4}-o(1)\right)(\log_2n)^2           \tag{16d}
\]

already forces the desired coefficient-`1/2` face lower bound (at critical
rank `r=Theta(log n)`).  Thus a full proof does not need a lossless
pair-telescope once its accumulated record entropy reaches the threshold
in (16d).  Below that threshold, however, the `2/3` theorem alone is
insufficient.

## 4. What this kills, and what it does not

The construction rigorously kills each of the following proposed abstract
steps:

* “Follow the higher-entropy-per-rank marginal and remember only the
  recursion path.”
* “The sum of `O(h)` prefix/rank/orientation tags is subquadratic, therefore
  the discarded conditional components are free.”
* “Endpoint pairs plus ACP counted `C_4`s always have enough pair capacity
  after a component-density surplus.”
* “Apply the first-divergence Kraft equality at all levels; its exact
  telescoping alone yields a two-face decoder.”

The model does **not** prove that Erdős 838 is false and does not kill a
theorem using planar convexity.  In an actual repair history, extra ordinary
faces might absorb the two conditional neighbor words.  The point is that
their existence cannot follow from the current entropy and graph axioms.
Indeed, in the critical parametrization `q asymptotic 2^h` the marginal
pool `N^h=2^{(2+o(1))h^2}` already has coefficient `1/2` relative to
`log_2 n=(2+o(1))h`.  Thus the countermodel is compatible with the expected
Erdős 838 lower bound; it refutes only the stronger claim that the *entire*
record-pair entropy must telescope through two outputs.

The exact remaining planar statement can now be written as follows.

> **Planar anti-incidence gate.**  A depth-`Theta(r)` prefix-correlated
> planar repair hierarchy cannot simulate
> `G_q^{tensor Theta(r)}` with `log q=Theta(r)` while exposing only
> `2^{(2/3+o(1))M}` ordinary convex faces.  Quantitatively, either a positive
> fraction of the conditional neighbor words is absorbed into two
> cross-compatible cyclic-interval faces, or the union of discarded
> prefix/pocket complexes contributes `2^{(1-o(1))M}` distinct faces.

This is a genuinely geometric assertion.  Fixed-edge singleton repair
supports are two-dimensional dominance graphs, already far more ordered
than projective-plane incidence.  The open task is to show that the same
anti-incidence phenomenon survives variable outer cores and long hidden
ears.  A successful proof would be the missing pair-valued component
recursion; a stretchable realization of the tensor model would refute it.

## 5. Relation to the exact `C_4` closure

For completeness, the entropy--spectral lemma gives

\[
 C_h\ge m_h^2 2^{-2I(X_h;Y_h)}.                              \tag{17}
\]

Here `I=(1/3+o(1))log m_h`, so the right side has exponent
`(4/3+o(1))log m_h`, exactly the scale in (14).  Thus no improvement of the
weighted-to-unweighted calculation can repair the component branch.  The
projective-plane tensor is an equality-scale test for any proposed stronger
information inequality.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_cyclic_stem_hw/verify_component_surplus_barrier.py
```

The verifier constructs `PG(2,q)` over prime fields for `q=2,3,5,7`, checks
all incidence degrees and common-neighbor counts, verifies (1)--(3) and the
exact `C_4` formula, and audits the tensor formulas with Python integers.
It then takes the least prime `q_h>=2^h` and verifies that even the generous
history budget `(2h+1)^{4h}=2^{O(h log h)}` leaves the predicted quadratic
pair-capacity deficit.
