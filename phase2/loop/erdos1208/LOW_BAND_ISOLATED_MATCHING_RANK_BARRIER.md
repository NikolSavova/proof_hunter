# The isolated common-translation survivor: path structure and the rank barrier

## 1. Outcome

Fix a determinant-qualified target-rich physical wedge `w` and retain the
exact scalar selector `V_w(p)` from
`LOW_BAND_COMMON_Q_ANCHOR_ISOLATION_DICHOTOMY.md`.  The surviving mass is

\[
 I^Q(w)=\sum_p V_w(p)i_Q(p),                              \tag{1.1}
\]

where `i_Q(p)` counts translations whose directed anchor has head degree one
and tail degree one in the common-translation graph `Q_p`.

There are two further exact structural facts.

1.  The isolated anchors of each `Q_p` are a vertex-disjoint union of
    directed paths and directed cycles.
2.  If `q` is isolated for `p=(s,t)`, then the two clean role targets
    `tau_q(s)` and `tau_q(t)` are vertex-disjoint.  Full matching of `Q_p` is
    not needed: isolation of the single anchor at its head already implies
    this.

The two common-translation rows can consequently be subtracted to produce
an affine design row supported on at most eight physical endpoints.  It
annihilates `1,X,Y` exactly.  This is the strongest unconditional
matching/rank consequence found here, but it does **not** control (1.1).
The scalar selector evaluates a quadratic column, and the corresponding
right side still contains the unconstrained clean-target gap and a
`q`-dependent pair-sum term.  Hence neither path cancellation nor the
ordinary common-translation design matrix preserves the scalar bucket.

This is not a counterexample to the desired estimate

\[
 I^Q(w)\le m^{o(1)}(H_Q/k+k^2).                          \tag{1.2}
\]

No genuine polynomial-height counterexample at that scale was found.  It is
a clean stopping theorem for matching union/rank/projection arithmetic.  On
the principal closure stress, 517 of the 523 isolated occurrences at
`k=50` are already singleton path components; the other six lie in three
two-edge paths.  Thus even perfect use of path/cycle telescoping would leave
the dominant literal-matching mass untouched.

## 2. Isolated anchors form paths and cycles

For a fixed ordered source pair `p`, write the unique directed anchor of
`q in Q_p` as

\[
 q=a_q-b_q.                                               \tag{2.1}
\]

Let `Q_p^iso` contain the anchors for which

\[
 d^+_{Q_p}(a_q)=d^-_{Q_p}(b_q)=1.                        \tag{2.2}
\]

In the directed graph formed only by `Q_p^iso`, every vertex is the head of
at most one edge and the tail of at most one edge.  Its underlying degree is
therefore at most two.  Every weak component is a path or a cycle, and the
orientations are consistent along that component.  If a path has successive
vertices `v_0,...,v_l`, then

\[
 \sum_{j=1}^l q_j=v_l-v_0;                               \tag{2.3}
\]

for a cycle the corresponding sum is zero.

This gives no numerical saving by itself: a literal matching is the special
case in which every component is a one-edge path, and then all anchors are
isolated.

## 3. An isolated anchor forces four distinct role-target endpoints

Let `q=a-b` be isolated for `p=(s,t)`.  Cleanliness gives unique target
edges satisfying

\[
 a+s=b+\tau_q(s),\qquad a+t=b+\tau_q(t),                 \tag{3.1}
\]

where an edge also denotes the sum of its endpoints.

**Proposition 3.1.**

\[
 \boxed{\tau_q(s)\cap\tau_q(t)=\varnothing.}             \tag{3.2}
\]

**Proof.**  Suppose the two target edges are `{x,u}` and `{x,v}`.  Rotating
the distinguished right endpoint in (3.1) from `b` to `x` gives

\[
 s+(a-x)=b+u,\qquad t+(a-x)=b+v.                        \tag{3.3}
\]

The same six-distinct conditions from the original rows show that both
rotated rows are clean.  Hence `a-x in Q_p`, with directed anchor `(a,x)`.
It is different from `(a,b)`, since `x!=b` by cleanliness, and shares its
head `a`.  This contradicts `d^+_{Q_p}(a)=1`.  \(\square\)

The proof sharpens the matching-target lemma in
`LOW_CODEGREE_ANCHOR_MATCHING_TWO_SCALE_BARRIER.md`: it needs neither a full
matching nor tail isolation.  It also shows exactly why it cannot compare
different source pairs `p`: the rotation remains in the same `Q_p` only
because both clean rows use `s` and `t`.

## 4. The affine cancellation row

For a source edge `z in H_q`, put

\[
 r_{z,q}={\bf1}_{\tau_q(z)}-{\bf1}_z.                   \tag{4.1}
\]

The clean pair-sum equation says

\[
 r_{z,q}\cdot {\bf1}=0,\qquad
 r_{z,q}\cdot P=q.                                      \tag{4.2}
\]

For an isolated occurrence `(p,q)`, with `p=(s,t)`, subtract the two role
rows:

\[
 d_{p,q}=r_{s,q}-r_{t,q}.                                \tag{4.3}
\]

Then

\[
 \boxed{
 d_{p,q}\cdot{\bf1}=d_{p,q}\cdot X=d_{p,q}\cdot Y=0.} \tag{4.4}
\]

Proposition 3.1 says that the positive target edge of `r_(s,q)` and the
negative target edge of `r_(t,q)` use four distinct target-role endpoints.
In role-copy columns the row (4.3) is consequently nonzero and has at most
eight nonzero endpoint entries.

Thus every isolated occurrence supplies a sparse affine dependency.  But
ordinary rank is already saturated by genuine quadratic clean fibres: the
role-copy matrices in
`COMMON_TRANSLATION_DESIGN_MATRIX_MATCHING_DEFECT_AUDIT.md` have precisely
the unavoidable affine nullity.  Passing from `r_(z,q)` to (4.3) removes
the common vector `q`; it does not create a new fixed right side.

## 5. Exact failure of the quadratic projection

Let `rho_v=|P_v|^2` be the radial point column, let `sigma_z` be the pair sum
of source edge `z`, and let `delta(z)` denote its squared length.  The
identity

\[
 2\sum_{v\in z}|P_v|^2=\delta(z)+|\sigma_z|^2           \tag{5.1}
\]

gives

\[
 2r_{z,q}\cdot\rho
 =\delta(\tau_q(z))-\delta(z)
   +2q\cdot\sigma_z+|q|^2.                              \tag{5.2}
\]

Consequently

\[
 \boxed{
 2d_{p,q}\cdot\rho
 =\delta(\tau_q(s))-\delta(\tau_q(t))
  -\bigl(\delta(s)-\delta(t)\bigr)
  +2q\cdot(\sigma_s-\sigma_t).}                         \tag{5.3}
\]

The fixed-wedge selector retains exactly

\[
 \delta(s)-\delta(t)=-18r,                               \tag{5.4}
\]

where `r` is a determinant-qualified target-rich shift attached to `w`.
After inserting (5.4), the first and last terms on the right of (5.3) still
depend on `(p,q)`.  Neither cleanliness nor anchor isolation fixes them.
Thus the affine design rows do not lie in a common quadratic hyperplane, and
row rank cannot recover the scalar selector by adjoining `rho`.

This is the exact algebraic obstruction to the most natural projection
argument.  A successful quadratic use of (4.3) must additionally control

\[
 \delta(\tau_q(s))-\delta(\tau_q(t))
      +2q\cdot(\sigma_s-\sigma_t),                       \tag{5.5}
\]

not merely the common translation or the endpoint support.

## 6. The target-rich lift and the missing connection

Let `U_L(r)` be the determinant-qualified target load and assume the selector
retains only `U_L(r)>=T`.  The exact decorated isolated mass is

\[
 \widetilde I^Q(w)
 =\sum_p V_w(p)i_Q(p)U_L(r(p)).                          \tag{6.1}
\]

It obeys

\[
 \boxed{\widetilde I^Q(w)\ge T I^Q(w).}                 \tag{6.2}
\]

At the critical threshold `T=k`, a proof of

\[
 \widetilde I^Q(w)\le m^{o(1)}(H_Q+k^3)                \tag{6.3}
\]

would imply (1.2).  Expanding (6.1) creates one isolated clean occurrence
and one determinant-qualified ordinary edge pair with the same scalar gap.
However, the endpoints in the ordinary pair are external to (3.1)--(4.3).
The common `q` is present only on the clean side.  No switch found here
turns this scalar equality into endpoint cooccurrence while preserving `q`.

This identifies the surviving inverse in a form stronger than “control a
matching”: correlate the quadratic residual (5.5) of many isolated affine
rows with the external determinant-qualified representations of their
selected scalar gaps.  Rank, matching union, and path/cycle projection see
only the first factor of (6.1).

## 7. Exact closure audit

For each prefix, the verifier chooses the physical wedge of maximum exact
rich common-`q` weight at cutoff `L=floor(N/k)` and threshold `T=k`.  It
reports

\[
 (k,H_Q,F_{\max},I,|R_w|,P,C,S,\ell_{\max},D,\widetilde I), \tag{7.1}
\]

where `P,C` are the numbers of isolated path and cycle components, `S` is
the number of isolated occurrences lying in singleton paths, `ell_max` is
the longest component, and `D` is the number of verified disjoint-target
occurrences.

\[
\begin{array}{c|r|r|r|r|r|r|r|r|r|r}
k&H_Q&F_{\max}&I&|R_w|&P&C&S&\ell_{\max}&D&\widetilde I\\ \hline
20&648&10&8&4&8&0&8&1&8&166\\
30&3816&69&57&17&57&0&57&1&57&2535\\
40&12420&312&224&27&222&0&220&2&224&13919\\
50&26532&662&523&43&520&0&517&2&523&43829
\end{array}                                               \tag{7.2}
\]

Thus every one of the 812 audited isolated occurrences satisfies
Proposition 3.1 and (4.4).  There are no isolated cycles.  Only ten
occurrences in total lie outside singleton paths, all in five two-edge
paths.  The closure survivor is therefore more matching-like than the
coarser source-pair classification suggested.

The verifier reconstructs clean fibres independently, checks every rotated
target-disjoint conclusion, evaluates all three affine columns in (4.4),
and checks `widetilde I>=kI` exactly.  Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_low_band_isolated_matching_rank_barrier.py
```

## 8. Verdict

The isolated survivor has now been exhausted at the level of matching
union, ordinary design rank, and affine projection:

* its anchor components are paths/cycles;
* each occurrence has four distinct role-target endpoints;
* subtracting its two clean rows gives an exact sparse affine dependency;
  and
* the quadratic evaluation of that dependency has the variable residual
  (5.5), while determinant-rich witnesses live on external endpoints.

The known polynomial-height literal-matching construction shows that a
single scalar-selected source pair can carry `Theta(k)` isolated clean
translations together with target richness `Theta(k)`.  This is sharp for a
single pair but remains below the allowed local `k^2` term, so it does not
kill (1.2).  A full proof must pool many singleton matching records through
the quadratic residual (5.5), or establish a new endpoint bridge to the
external rich representations.  No current affine-rank or path-packing
argument supplies that bridge.
