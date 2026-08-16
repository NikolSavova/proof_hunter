# Local weighted Hall fails sharply on a matching star

**Date:** 2026-08-15

## Verdict

The sole local hypothesis in `ABSTRACT_MIXED_HALL_ASSEMBLY.md` is false for
arbitrary two-tangent trace profiles, already at constant live rank.

For every \(m\ge2\) there is an exact stretchable configuration with one
trace \(j<l\), left apices \(x_1,\ldots,x_m\), and right apices
\(y_1,\ldots,y_m\), such that

\[
 \boxed{
 \{x_i,j,l,y_k\}\text{ is convex}
 \iff i+k=m+1.}                                        \tag{1}
\]

Thus the two-tangent compatibility graph between the rank-three side
histories \(H_i=\{x_i,j,l\}\) and opposite singleton histories is a
perfect matching.  Moreover, no higher opposite-side history can glue to
\(H_i\): deletion would give two distinct singleton neighbours, contradicting
(1).  If \(N=2m+2\) is the ambient size, then \(H_i\) has half-activity
weight \(2^{-3}\), so its desired demand is \(N/8\).  The singleton Hall
cut forces

\[
 \boxed{\lambda\ge N/8=\Theta(N).}                     \tag{2}
\]

This is attained by putting all flow on the unique quadrilateral, so the
failure is exact.  Hence no \(N^{o(1)}\) weighted Hall expansion theorem can
hold for natural two-tangent compatibility, even for rank-three inputs and
rank-four outputs.

There is, however, an exact local alternative-side charge.  Drop the trace
labels but retain the apex.  A balanced orientation of the complete graph
on \(X=\{x_1,ldots,x_m\}\), together with the singleton \(\{x_i\}\), gives
each \(x_i\) at least

\[
 1+\left\lfloor\frac{m-1}{2}\right\rfloor
 \ge \left\lceil\frac{N}{8}\right\rceil               \tag{3}
\]

pairwise disjoint owned side faces of rank one or two.  Sending the demand
of \(H_i\) equally to that many owned faces gives load one and recovery
fibre one: the owner of the side face recovers \(x_i\), and the known cell
recovers \(j,l\).  The same construction applies independently on \(Y\).

So the exact local dichotomy on the matching-star test is

\[
 \boxed{\text{mixed Hall load }\Theta(N)
 \quad\text{but detached-side load/fibre }1.}           \tag{4}
\]

The side charge does not automatically globalize.  In the \(q^2\)-trace
matching-star construction, the same side face can be offered by all
\(q^2\) traces.  Its cell-free recovery list can therefore have size
\(q^2\).  A trace selection, ancestor telescope, or one joint Hall
allocation over all traces is still required.  This is precisely the
detached-side overlap problem left outside the trace-owned assembly theorem.

The two other required regressions agree with this conclusion:

- the terminal \(E(k,3)\) cup has one label-retaining output and forces
  load \((m+1)/2^k=m^{1/2-o(1)}\);
- the full \(E(k,k)\) top mixed bank passes only after making compatibility
  complete by a label-replacing block code, which has load and fibre one.

Thus local natural compatibility can fail by a fixed power.  The viable
routes are an alternative side-bank charge with a global telescope, or an
explicit label-replacing recovery code whose bank is jointly allocated.

This is a barrier to the local decoder strategy, not a counterexample to
the half-weight conjecture.

## 1. Exact stretchable realization

Set

\[
 \delta=\frac1{100m},\qquad c=\frac\delta4,
 \qquad \varepsilon=\frac1{10^4m^4}.                   \tag{5}
\]

Before an arbitrarily small rational generic perturbation, take

\[
\begin{aligned}
 x_i&=(-2+\varepsilon i,\ i+\varepsilon i^2),\\
 y_k&=( 2+\varepsilon k,\ k-m-1-\varepsilon k^2),\\
 j&=(-\delta,c),\qquad l=(\delta,c),
 \qquad 1\le i,k\le m.                                \tag{6}
\end{aligned}
\]

The x-order is \(X<j<l<Y\).  The \(X\)-cloud is a strict cup and the
\(Y\)-cloud a strict cap.  Indeed, for \(a<b<d\), direct expansion gives
orientation sign \(+\varepsilon^2(b-a)(d-b)(d-a)\) on \(X\) and its
negative on \(Y\).

At \(\varepsilon=0\), the line \(x_i y_k\) has height

\[
 \frac{i+k-m-1}{2}                                     \tag{7}
\]

at abscissa zero.  If \(i+k=m+1\), it meets the horizontal trace line at
abscissa

\[
 -\frac{2c}{i}\in(-\delta,\delta).                     \tag{8}
\]

Otherwise (7) has absolute value at least \(1/2\); throughout the trace
window the unperturbed line remains more than \(0.49\) away from height
\(c\).  The coordinate perturbation in (6) changes the line height in that
window by less than \(\delta/8\).  Thus the first case still intersects the
open segment \(jl\), and the second remains disjoint.  For four points in
the block order \(x_i<j<l<y_k\), the segments \(x_i y_k\) and \(jl\)
intersect exactly when all four are in convex position.  This proves (1).

All relevant inequalities are strict.  A sufficiently small rational
perturbation can therefore remove any remaining collinearity or repeated
slope while preserving the x-order, the cup/cap signs, and (1).  Hence the
configuration is a genuine stretchable reduced-word example.

## 2. Full two-tangent neighbourhood of a singleton side history

Fix \(H_i=\{x_i,j,l\}\).  By (1), it has exactly one compatible singleton
on the other side, namely \(y_{m+1-i}\).  Suppose a rooted right side face
\(Y'\) with at least two vertices glued to \(H_i\).  Deleting all but one
vertex of \(Y'\) from the resulting convex face would show

\[
 \{x_i,j,l,y\}\text{ convex}\qquad(y\in Y').           \tag{9}
\]

This gives at least two neighbours of \(x_i\) in (1), impossible.  Thus

\[
 \Gamma(H_i)=
 \bigl\{\{x_i,j,l,y_{m+1-i}\}\bigr\}.                 \tag{10}
\]

The history has rank three, hence weight \(w(H_i)=1/8\).  Applying the
weighted Hall condition to \(\{H_i\}\) gives

\[
 \frac N8\le\lambda|\Gamma(H_i)|=\lambda,              \tag{11}
\]

which proves (2).  Since the matching outputs are distinct for different
\(i\), routing each history entirely to its unique output attains load
exactly \(N/8\).

## 3. Exact detached-side decoder

Every singleton and pair of labels is an ordinary convex face, independent
of the order type.  Orient the edges of the complete graph on \(X\) as a
balanced tournament (for even \(m\), use an almost-regular tournament).
Every vertex owns at least \(\lfloor(m-1)/2\rfloor\) incident pairs, and it
also owns its singleton.

Put

\[
 q=\left\lceil\frac N8\right\rceil
  =\left\lceil\frac{m+1}{4}\right\rceil.               \tag{12}
\]

For \(m\ge2\),

\[
 q\le1+\left\lfloor\frac{m-1}{2}\right\rfloor.         \tag{13}
\]

Assign to \(H_i\) its singleton and any \(q-1\) pairs owned by \(x_i\).
Ownership makes these blocks disjoint.  Put flow \((N/8)/q\le1\) on every
assigned output.  The total emitted flow is \(N/8\), every side face is
used by at most one history, and its owner recovers \(x_i\).  Relative to
the known trace cell, this recovers all of \(H_i\).  Thus local load and
fibre are exactly at most one.  Apply the same tournament construction to
the \(Y\)-cloud for the opposite histories.

This charge uses only rank-one and rank-two ordinary side faces.  The much
larger Boolean banks supplied by the strict cup/cap clouds are unnecessary.

## 4. Why the side charge needs a telescope

The robust conditions in Section 1 persist if \(j\) is replaced by a small
cloud \(J\) and \(l\) by a small cloud \(L\).  Every one of the
\(|J||L|\) traces has the same matching graph (1).  Its local side decoder
can therefore offer the same owned singleton/pair blocks of \(X\) and
\(Y\).

If those decoders are built independently, one owned side face can be used
once for every trace, giving load and unmarked recovery fibre

\[
 |J||L|.                                                 \tag{14}
\]

Unlike a mixed output, the detached side face contains neither trace
endpoint, so the \(r-3\) consecutive-trace incidence theorem does not
apply.  Any global use of the side alternative must select few traces per
side bank, telescope through a recursive ancestor, or solve a joint Hall
allocation with all trace demands present.

## 5. E-family and terminal-cup audit

Let \(M_k=\binom{2k-4}{k-2}\).  For the terminal coherent-root history over
\(E(k,3)\), natural label-retaining compatibility has one output, and the
singleton Hall cut is

\[
 \lambda\ge\frac{M_k+1}{2^k}
 =M_k^{1/2-o(1)}.                                       \tag{15}
\]

This is the logarithmic-rank version of (11).  Conversely, if compatibility
is explicitly replaced by the complete relation to the top mixed bank of
\(E(k,k)\), `LABEL_REPLACING_ES_MIXED_CODE.md` proves

\[
 |\mathcal M_k|\ge
 \sum_{S\in\mathcal U(E(k,k))}
 \left\lceil\frac{M_k+1}{2^{|S|+1}}\right\rceil,        \tag{16}
\]

and the block decoder has load/fibre one.  Equations (15)--(16) show that
the issue is genuinely compatibility expansion, not scalar mixed capacity.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_coxeter_global_half/verify_local_trace_hall_matching_barrier.py
```

The checker constructs the rational coordinates (5)--(6), applies an exact
sign-preserving generic perturbation, reconstructs the reduced word, and
checks every rank-three side history and the full matching graph for
\(2\le m\le30\).  It verifies that every singleton history has exactly one
full two-tangent output, constructs the balanced-tournament side decoder,
and checks its emission, load, ownership recovery, and (12)--(13).  It also
constructs a 25-trace exact matching star and checks the predicted detached
side-face overlap, then audits the terminal-cup load and the complete
\(E(k,k)\) block-code capacity through \(k=20\).
