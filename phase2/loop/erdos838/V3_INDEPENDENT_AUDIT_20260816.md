# Independent audit V3: minimizer hull-root recurrence and curvature gate

**Date:** 2026-08-16.

## Verdict: PASS

I reconstructed the two load-bearing arguments in V3 without using their
verifier implementations as proofs, and then reran both exact suites. The
hull-root recurrence, the definition of the weighted increment
\(K_{n,1}\), the cumulative half-growth criterion, the minimizer endpoint
moment bound, and the corrected finite \(n=8,9\) calibrations are valid with
the scopes stated below.

This package does **not** prove the half lower bound. It proves an exact
dynamic and identifies the missing Pareto-curvature estimate. In particular,
chartwise hinged Kraft gives only polynomial growth, and the finite flat
frontiers disprove the naive tangent lower bound.

Audited sources:

- `agent_hull_root_envelope_dynamic/HULL_ROOT_ENVELOPE_AND_CHART_RESET_GATE.md`;
- `agent_hull_root_envelope_dynamic/verify_hull_root_envelope.py`;
- `agent_minimizer_endpoint_curvature/MINIMIZER_ENDPOINT_CURVATURE_AND_HIGH_WALL_GATE.md`;
- `agent_minimizer_endpoint_curvature/verify_minimizer_endpoint_curvature.py`.

## 1. Exact hull-root recurrence

Let \(V(P)\) count nonempty ordinary convex subsets and

\[
                         f(n)=\min_{|P|=n}V(P).          \tag{1}
\]

For an \(n\)-point realization \(Q\) in a generic directional chart
\(\theta\), let \(C_\theta(Q)\) be its nonempty cap count. Then

\[
 \boxed{f(n+1)=1+\min_{|Q|=n,\theta}
                   \{V(Q)+C_\theta(Q)\}.}               \tag{2}
\]

### Lower inequality

Take an \((n+1)\)-point minimizer \(P\) and a hull vertex \(z\). A
supporting line through \(z\) misses the other labels. Send that line to
infinity by a projective map and put \(Q=P-z\). Ordinary faces avoiding
\(z\) are exactly the faces of \(Q\). Apart from \(\{z\}\), ordinary faces
containing \(z\) are exactly \(z\) joined to the caps of \(Q\) in the
induced radial chart. Hence

\[
                         V(P)=V(Q)+1+C_\theta(Q),        \tag{3}
\]

which is at least the right side of (2).

### Upper inequality

Conversely, choose any realizable \((Q,\theta)\), make \(\theta\)
horizontal, and order \(Q\) by increasing \(x\). A point \(z=(X,-M)\),
with \(X\) beyond every old point and \(M\) sufficiently large, has the
same strict orientation against every ordered old pair. It is extreme, and
the old subsets extending through \(z\) are precisely the caps in the
chosen chart. Thus (3) is attained, proving (2). This converse is why the
minimum must range over realizations/charts, not only over affine cuts of
one stored realization.

Define

\[
 K_{n,1}=\min_{|Q|=n,\theta}
       \{V(Q)-f(n)+C_\theta(Q)\}.                       \tag{4}
\]

Subtracting \(f(n)\) from (2) gives the exact increment identity

\[
                      f(n+1)=f(n)+1+K_{n,1}.            \tag{5}
\]

No lower-bound conjecture is used in this derivation.

## 2. Cumulative criterion and its normalization

Telescoping (5), with \(f(1)=1\), gives

\[
 \log_2 f(N)=\sum_{n<N}\log_2\!\left(
       1+{1+K_{n,1}\over f(n)}\right).                  \tag{6}
\]

Therefore the desired coefficient \(1/2\) is equivalent to the lower bound

\[
 \sum_{n<N}\log_2\!\left(
       1+{1+K_{n,1}\over f(n)}\right)
 \ge(1/2-o(1))(\log_2N)^2.                              \tag{7}
\]

A pointwise sufficient condition is

\[
 K_{n,1}\ge(1-o(1)){\log_2 n\over n}f(n).              \tag{8}
\]

Indeed, \(K/f=o(1)\) on this scale and

\[
 \sum_{n<N}{1\over\ln2}{\log_2n\over n}
       =(1/2+o(1))(\log_2N)^2.                          \tag{9}
\]

Condition (8) is sufficient, not pointwise equivalent to (7); a sparse set
of failures may be harmless. The audited source states this distinction
correctly.

## 3. Endpoint moment and Pareto reduction

Let \(Q\) be an ordinary \(a\)-point minimizer and choose a chart with the
least possible cap count \(p(a)\). Write

\[
 M_F=\sum_{F\in\mathcal F(Q)}|F|,
 \qquad M_C=\sum_{A\in\mathcal C(Q)}|A|.                \tag{10}
\]

Delete a label \(x\), then restore it on the cap side of the inherited
chart. Minimality gives

\[
 V(Q)-V(Q-x)\le1+C(Q-x).                                \tag{11}
\]

Summing (11), using

\[
 \sum_x[V(Q)-V(Q-x)]=M_F,
 \qquad \sum_xC(Q-x)=a p(a)-M_C,                        \tag{12}
\]

gives

\[
                         M_F+M_C\le a(1+p(a)).          \tag{13}
\]

If \(m_a(t)\) is the minimum rank sum of \(t\) distinct nonempty subsets
of an \(a\)-set, then \(M_F\ge m_a(f(a))\) and
\(M_C\ge m_a(p(a))\). Hence

\[
                 m_a(f(a))+m_a(p(a))\le a(1+p(a)).      \tag{14}
\]

When \(\log_2f(a)=c(\log_2a)^2+o((\log a)^2)\), Boolean
layer inversion makes the cutoff rank \(r=(c+o(1))\log_2a\), and (14)
implies

\[
                   p(a)\ge(1-o(1)){r f(a)\over a}.      \tag{15}
\]

Thus the endpoint value itself has the right quasipolynomial size. The
missing datum is its cost under a weighted child penalty.

Define

\[
 \Phi_a(c)=\min_{Q,\theta:C_\theta(Q)\le c}
                 [V(Q)-f(a)].                            \tag{16}
\]

For a literal strong seam \(P=A\prec B\), exact child replacement makes the
left and right children minimize their weighted objectives. Consequently
\(C(A)\le p(a)\), \(U(B)\le p(b)\), and

\[
 V(P)\ge f(a)+f(b)+
  \Phi_a(C(A))+\Phi_b(U(B))+C(A)U(B).                   \tag{17}
\]

Taking the minimum over the two endpoint ranges yields exactly the stated
two-child Pareto gate. It is a sufficient reduction, not an assertion that
every minimizer has a literal strong seam.

## 4. Finite corrections and reset certificate

The full \(B(8,2)\) scan gives

\[
                         f(8)=113,\qquad p(8)=55.        \tag{18}
\]

There is a stretchable neighboring profile \((V,C)=(114,53)\), so the
frontier can trade one ordinary face for two caps. This refutes any universal
unit tangent bound.

For the stored true nine-point minimizer, \(V=168\). Its three hull roots
each delete to an eight-point child with \((V,C)=(114,53)\), giving

\[
                         168=114+1+53.                   \tag{19}
\]

Thus \(K_{8,1}=54\), agreeing with (5). These are projective hull-root
charts; an affine contiguous-cut scan is not an exhaustive substitute.

The same exact order type has 168 reachable deletion states, 483 hull-root
transitions, 6,984 extreme shellings, and 23 distinct root-cost sequences.
All sequences telescope to \(168-9=159\). A fixed physical label swaps its
cap/cup responsibility between two equally cheap root charts, so chartwise
Kraft cannot simply be concatenated along a shelling.

The conservative universal statement at nine points remains
\(72\le p(9)\le82\): the stored minimizer has minimum 82 across its 72
chambers, but the full realizable \(B(9,2)\) has not been enumerated. None of
the curvature obstruction relies on equality here.

## 5. Verifier replay

Commands:

~~~text
python3 phase2/loop/erdos838/agent_minimizer_endpoint_curvature/verify_minimizer_endpoint_curvature.py
python3 phase2/loop/erdos838/agent_hull_root_envelope_dynamic/verify_hull_root_envelope.py
~~~

Fresh outputs:

~~~text
PASS: minimizer endpoint moment/Mobius bounds, restriction-defect curvature,
exact B(5,2)/B(8,2) scans, n=9 stretchable flat-frontier witness, and
high-wall obstruction; p={5:17,8:55,9_stored:82};
lambda={5:2,8:1/2,9_witness:1/6};
nonstrong_cache_misses={8:109600,9:986409}

PASS: exact hull-root envelope/flag identities;
weighted increments=[1,3,6,11,17,27,40,54];
n9=6984 shellings, 23 cost sequences, 483 root charts;
sharp hinged n8 (V,C,U)=(130,65,65)
~~~

Both suites use exact integer/rational orientation and subset enumeration.
The numerical asymptotic checks support algebra already proved above; they
are not used as evidence for the still-open curvature inequality.
