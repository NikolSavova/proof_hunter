# Independent audit V4: sparse curvature transport and remapping collision

**Date:** 2026-08-16.

## Verdict: PASS

The sparse hull-root curvature transport identity, its causal layer
decomposition, the native-cap collision, the weighted child-excess gate, and
the post-collision remapping lower bound are correct. Both exact verifier
suites pass on the true nine-point minimizer, Pascal cells, convex polygons,
and vertical substitutions.

The package is a route closure/barrier, not a proof of Erdős 838. It shows
that a successful shelling argument must retain a sparse amount of recurrence
mass carried almost entirely by child excess, or construct a genuinely
larger ordinary-face bank. Remapping the full tagged ledger to ordinary faces
cannot have sub-shelling load.

Audited sources:

- `agent_sparse_curvature_transport/SPARSE_CURVATURE_TRANSPORT_AND_NATIVE_COLLISION.md`;
- `agent_sparse_curvature_transport/verify_sparse_curvature_transport.py`;
- `agent_post_collision_remapping/POST_COLLISION_REMAPPING_MINIMAX.md`;
- `agent_post_collision_remapping/verify_post_collision_remapping.py`.

## 1. Exact transport

For an \(m\)-point state \(A\), put

\[
 E(A)=V(A)-f(m),
 \qquad K_{m-1,1}=f(m)-f(m-1)-1.                        \tag{1}
\]

If \(z\) is extreme and \(B=A-z\), the hull-root identity and envelope
recurrence are

\[
 V(A)=V(B)+1+C(A,z),
 \qquad f(m)=f(m-1)+1+K_{m-1,1}.                        \tag{2}
\]

Subtracting gives the conservation law

\[
 \boxed{E(B)+C(A,z)=K_{m-1,1}+E(A).}                    \tag{3}
\]

Starting at the final singleton and moving upward along any extreme
shelling, partition the child ledger into already assigned lower layers and
an unassigned reservoir of size \(E(B)\). The new transition adds
\(C(A,z)\) tokens. Equation (3) says their union has exactly
\(K_{m-1,1}+E(A)\) elements, so assign any \(K_{m-1,1}\) to the new layer
and export \(E(A)\). This inductively proves the causal decomposition.

For an \(N\)-point minimizer, \(E(P)=0\), and

\[
                    \sum_{m=2}^N K_{m-1,1}=f(N)-N.      \tag{4}
\]

Thus the top layer has exact density

\[
                    {K_{N-1,1}\over f(N)-N}             \tag{5}
\]

inside every shelling ledger. No desired lower bound on \(K\) is assumed;
(3)--(5) are identities.

## 2. Native collision and weighted gate

Let a first root \(z\) of a minimizer have

\[
 C_z=C(P,z),
 \qquad D_z=V(P-z)-f(N-1).                              \tag{6}
\]

Equation (3) at the top reads

\[
                         C_z+D_z=K_{N-1,1}.              \tag{7}
\]

There is no parent residual, so every one of these tokens is forced into the
top layer. In particular, every nonempty subset of the other hull vertices
is a cap in the radial chart. The full hull face is therefore selected once
for every shelling, giving canonical load exactly the total shelling weight
\(W\). This proves the native-cap collision without an averaging estimate.

For arbitrary shelling weights, write \(W_z\) for the weight starting at
\(z\). Suppose a causal selection retains at least
\((1-\eta)WK_{N-1,1}\), and every native ordinary output has load at most
\(\varepsilon W\). Native mass from root \(z\) is at most
\(\varepsilon W C_z\), while child mass is at most \(W_zD_z\). Therefore

\[
 (1-\eta)WK
 \le\varepsilon W\sum_zC_z+\sum_zW_zD_z.               \tag{8}
\]

Substitute \(D_z=K-C_z\) and \(\sum_zW_z=W\) to obtain

\[
 \sum_z{W_z\over W}{C_z\over K}
 \le\eta+\varepsilon{\sum_zC_z\over K}
 \le\eta+\varepsilon|H(P)|.                            \tag{9}
\]

Hence a near-capacity sparse decoder with
\(\eta+\varepsilon|H(P)|=o(1)\) must carry \(1-o(1)\) of its top curvature
through the child excess \(D_z\). This conclusion is conditional only on
the stated sparse selection/load hypothesis; it does not assume the desired
curvature size or decoder.

The direct hull wall is also valid:

\[
                   K_{N-1,1}\ge C_z\ge2^{|H(P)|-1}-1.   \tag{10}
\]

## 3. Why arbitrary remapping cannot repair the collision

Let \(\mathcal S(P)\) be the extreme shellings with total weight \(W\).
In one shelling, assigning each non-singleton ordinary face at the transition
where its first member is deleted gives exactly \(V(P)-n\) tagged symbols.
Thus the full tagged mass is

\[
                           W(V(P)-n).                    \tag{11}
\]

Any deterministic, fractional, future-aware, or globally balanced remapping
of all this mass into the \(V(P)\) ordinary faces has some output of load at
least

\[
 \boxed{W{V(P)-n\over V(P)}.}                           \tag{12}
\]

This is pure mass conservation. If only non-singleton outputs are allowed,
the lower bound is exactly \(W\), attained by the canonical decoder. Since
every set of ranks one, two, and three is ordinary,

\[
 V(P)\ge n+\binom n2+\binom n3,
\]

so (12) is \((1-O(n^{-2}))W\) in every planar configuration.

Reading finitely many future roots does not change (12) if the output must
still be one ordinary face. If the roots remain as metadata, the codomain is
no longer the face family being counted; forgetting them returns to (12).
Thus the barrier concerns the output capacity, not the particular canonical
map.

If only a fraction \(\rho\) of the tagged mass is retained, the same proof
gives load at least

\[
                      \rho W{V(P)-n\over V(P)}.          \tag{13}
\]

Consequently sub-shelling load requires \(\rho=o(1)\), exactly matching the
sparse-layer conclusion in Section 2.

## 4. Exact finite replay

Fresh commands:

~~~text
python3 phase2/loop/erdos838/agent_sparse_curvature_transport/verify_sparse_curvature_transport.py
python3 phase2/loop/erdos838/agent_post_collision_remapping/verify_post_collision_remapping.py
~~~

Outputs:

~~~text
PASS: exact excess-potential curvature transport and forced-native minimax
congestion; n9=6984/6984; pascal6=131/336;
vertical9=2117/64560

PASS: arbitrary-remapping minimax fibre barrier and exact one-next-label
menu optima; n9=6633/6984; pascal6=298/336;
convex_n8=39178/40320; vertical9_lower=62432/64560
~~~

The max-flow calculations strengthen, but are not needed for, the universal
counting bound (12). They show that a generous one-next-root mutation menu
nearly attains the unavoidable full-ledger congestion on the tested order
types.

## 5. Scope

Proved:

- exact causal curvature transport;
- exact top-layer native collision;
- the weighted native-versus-child-excess inequality;
- the universal remapping load lower bound;
- exact finite congestion calibrations.

Not proved:

- that top curvature has the sharp size needed for half;
- that child excess has a sparse geometric decoder;
- that a larger mixed ordinary-face bank exists;
- any improvement to the unconditional coefficient window.

The only live shelling continuation is therefore a child-excess or genuinely
new-output theorem. Full-ledger remapping is closed permanently.
