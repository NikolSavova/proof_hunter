# Near-ambient live contexts: sparse traces close, high projection load remains

**Date:** 2026-08-15. All logarithms are base two. This is the critical
live-normalization audit of
`NEAR_AMBIENT_PAIR_STAR_DIRECTIONAL_RECTANGLE_BARRIER.md`.

## Verdict

The earlier \(P\times P\) central-nesting regression is **not** a live
sparse-context obstruction. Its

\[
                         P^2=2^{O(L L_3)}                 \tag{1}
\]

geometric outside contexts are exponentially too few to carry the canonical
marked source mass, where

\[
 L=\log n,\qquad L_2=\log L,\qquad L_3=\log L_2.         \tag{2}
\]

The exact statement is a context-count/projection-load dichotomy. Let
\(w(A)\) be canonical source weights of total mass \(W\), with
\(w(A)\le\kappa_A\) for every actual ordinary source face \(A\). Let
\(\pi(A)=S\) be the geometric outside context left after the run/carrier
projection, and put

\[
 \Lambda_{\rm proj}=max_S\sum_{A:\pi(A)=S}w(A),
 \qquad C_{\rm geo}=|\pi(\operatorname{supp}w)|.          \tag{3}
\]

Then, exactly,

\[
 \#\{A:w(A)>0\}\ge {W\over\kappa_A},
 \qquad W\le \Lambda_{\rm proj}C_{\rm geo}.             \tag{4}
\]

On the live near-ambient slice,

\[
 W\ge {V(P)\over2^{O(L L_2)}},\qquad
 V(P)\ge V(X_R)\ge2^{\Phi(L-a)},\qquad a=O(L_3),         \tag{5}
\]

where \(\Phi(L)=L^2/2-O(L L_2)\). Therefore

\[
 \log C_{\rm geo}+\log\Lambda_{\rm proj}
              \ge {1\over2}L^2-O(L L_2).                \tag{6}
\]

Consequently:

* if \(\Lambda_{\rm proj}\le2^{O(L L_2)}\), then
  \(C_{\rm geo}\ge2^{L^2/2-O(L L_2)}\), so (1) is impossible;
* if \(C_{\rm geo}\le2^{O(L L_3)}\), then
  \(\Lambda_{\rm proj}\ge2^{L^2/2-O(L L_2)}\).

Thus the globally live **sparse-context, bounded-load case is closed**. A
small geometric context alphabet can survive only by coalescing a
coefficient-half family of actual sources. That is precisely the high
source/carrier projection load handed to the sibling-ear, fixed-edge shield,
and mask/run gates; it may not be called a load-one incidence family.

The opposite attempt to restore a complete macro trace family is also
impossible in the least-counterexample slice. Suppose \(s=\alpha L+o(L)\)
disjoint roles of total support at most \(n\) are placed so that every
transversal is ordinary and their sizes are balanced. If
\(\log V(P)=cL^2+o(L^2)\), then

\[
 \log P_0=\alpha L^2-\alpha L L_2+O(L),
 \qquad
 \log{P_0\over V(P)}=(\alpha-c)L^2-O(L L_2).            \tag{7}
\]

The surviving role-forest branch has
\(\alpha-c\ge\varepsilon>0\). Hence \(P_0>V(P)\) by a fixed quadratic
factor, contradicting that all \(P_0\) transversals are ordinary. The
complete parabolic macro banks used by the local central-pair regressions
are therefore nonlive for an independent reason.

This audit does **not** close the high-projection-load/few-run endpoint.
After fixing one sparse geometric context, the mass may be stored in many
actual full sources and trace-dependent carrier words. The established
gates give the following rigorous route:

1. diffuse carrier edges produce the decoded
   \(n^{\Theta(\loglog n)}\) rooted-ear bank;
2. concentrated edges produce a fixed-edge circuit tensor, whose detached
   shield telescope either pays or fixes an enormous literal
   carrier--shield load; and
3. fixing that load invokes the full-source/mask/run descent, whose few-run
   residue is the near-ambient child.

The small \(P^2\) regression belongs only to item 3 after the projection
load has become enormous. It proves a local mixing obstruction there, but
not a live counterfamily.

There is an exact lower-order ledger for what remains. Put

\[
 K=2^{\Phi(L)},\qquad
 H=2^{\Phi(L-a)}={K\over T},\qquad
 \Delta=\log T=\Phi(L)-\Phi(L-a)=\Theta(L L_3).         \tag{8}
\]

If the putative ambient counterexample has

\[
                  V(P)={K\over R},\qquad 1\le R\le T,   \tag{9}
\]

then a live full-context family has size
\(M\ge V(P)2^{-O(L L_2)}\), while an endpoint star has
\(J\ge H/n^{O(1)}\). Even if the live contexts factor as
\(A\times B\), the exact two-direction bank gives only

\[
 \max\{AC_e,BU_e\}\ge\sqrt{M J},\qquad C_eU_e=J.       \tag{10}
\]

Ignoring normalization and polynomial losses, its logarithm is

\[
             \Phi(L)-{\log R+\Delta\over2},             \tag{11}
\]

whereas \(\log V(P)=\Phi(L)-\log R\). Since
\(\log R\le\Delta\), (11) need not exceed the already-known source bank.
The common \(1+3\) complement and the ordered two-face decoder likewise
give only the separated product \(MJ\le V(P)^2\). This is an exact
square-root ledger, not a planar upper construction.

So the honest endpoint is:

* **closed:** complete macro traces and sparse geometric contexts of
  bounded global load;
* **still open:** coefficient-half source mass hidden behind one/few
  geometric contexts, after all diffuse-ear and low-load fixed-edge
  alternatives have failed.

A genuine counter-regression for the second item would have to count the
*entire* ambient multi-label face complex and keep it below \(K\). No known
projective nesting or two-cloud construction does that. The current exact
residue is the same live profile-penetration/coherent-ramp problem isolated
in `LIVE_DENSE_COMPLETION_PROFILE_GATE.md`, now at the smaller
\(L L_3\) near-ambient deficit.

## 1. Context cardinality versus projection load

Equation (4) is just grouping source mass by the actual geometric output
of \(\pi\):

\[
 W=\sum_S\sum_{A:\pi(A)=S}w(A)
      \le C_{\rm geo}\Lambda_{\rm proj}.              \tag{12}
\]

The first inequality in (4) is the equally elementary bound
\(W=\sum_Aw(A)\le\kappa_A\#\{A:w(A)>0\}\). Thus if the advertised
\(P^2\) contexts are themselves full actual sources, they fail live
normalization immediately. If they are only projections of many actual
sources, the missing multiplicity is exactly \(\Lambda_{\rm proj}\).

The canonical marked-source construction has
\(\sum_{\text{marks on }A}w(A,\text{mark})\le1\). Rank, root, role-colour,
dyadic, and chronology localization may add a certified
\(2^{O(L L_2)}\) description load; absorb it either into \(\kappa_A\) or
\(\Lambda_{\rm proj}\). It cannot turn the context count (1) into the
coefficient-half lower bound in (6).

If pocket replication copies one source over many released faces, then
either that released face is retained in \(S\), creating distinct geometric
contexts, or it is erased and its replica multiplicity is part of
\(\Lambda_{\rm proj}\). Equation (4) is unchanged; one may not count the
replicated child reservoir in both \(W\) and the later factor \(J\).

From (5),

\[
 \log W\ge\Phi(L-a)-O(L L_2)
          ={1\over2}L^2-O(L L_2),                      \tag{13}
\]

because \(a=O(L_3)=o(L_2)\). Combining (12)--(13) proves (6) and both
alternatives following it.

This corrects a tempting but invalid multiplication. The quantity
\(J P^2\) can be \(K/n^{O(1)}\), because \(J\) is the large **detached
child face reservoir**. It does not imply that the pre-replication marked
source mass is live: that mass is controlled by \(P^2\), not by
\(JP^2\). Pocket replication copies source atoms across \(J\); it does not
raise their source marginal.

## 2. Complete role products violate \(\alpha>c\)

For balanced roles of total support \(N\le n\), put
\(d=N/s\). Their complete transversal count is

\[
 P_0=d^s,qquad
 \log P_0=s(\log N-\log s)
      =\alpha L^2-\alpha L L_2+O(L).                  \tag{14}
\]

If every transversal is ordinary, then \(V(P)\ge P_0\). But on the
excess-rank role-forest slice,

\[
 s-cL\ge\varepsilon L,qquad c={\log V(P)\over L^2},   \tag{15}
\]

and (14)--(15) give

\[
 \log P_0-\log V(P)
       \ge\varepsilon L^2-O(L L_2)>0.                 \tag{16}
\]

Unequal roles only lower the complete box volume by AM--GM, so (16) is a
contradiction specifically for the balanced alphabet regime used in the
parabolic macro regressions. It is not a claim that every role box has
large \(P_0\); the live completion extraction already supplies the
polynomially balanced slice before this audit is invoked.

If one keeps only \(k=\Theta(L_3)\) active macro roles, their complete
trace bank has logarithm \(O(L L_3)\) and avoids (16), but then (6) forces
coefficient-half projection load. These are exactly the two sides of the
audit; there is no intermediate complete-macro counterexample.

## 3. Splice to the geometric gates

At a low-\(Q_{\rm eff}\) terminal, all but \(o(L)\) deleted roles have
effective branching \(d_i/\operatorname{polylog}n\). The mass-uniform
sibling theorem turns this into physical label clouds. Its exact
alternatives are:

\[
 \text{decoded diffuse-ear bank}quad\text{or}\quad
 \text{one fixed actual edge carrying a dense circuit tensor}.  \tag{17}
\]

The first bank has \(2^{\Theta(L L_2)}\) outputs per recoverable cell. Its
literal carrier/context load is explicit; bounded load closes after the
live mass normalization. In the second branch, the fixed-edge shield
telescope has

\[
 T_{\rm edge}\le Q
       \sqrt{\kappa_A\lambda_H}\,V(P),
 \qquad
 Q\le {n\over\sqrt{f(d)-1}}.                           \tag{18}
\]

For \(d=n^{\gamma-o(1)}\), the safe lower bound on \(f(d)\) makes \(Q\)
quadratically small. Thus an unpaid tensor has enormous literal
carrier/shield reuse. Fixing that actual pair leaves full source/mask
variation, to which the recoverable carrier coarsening and mask/run theorem
applies.

Nothing in (17)--(18) bounds the final projection load by
\(2^{O(L L_2)}\); high reuse is their declared residual. Hence the sparse
case is closed exactly up to, but not through, the few-run high-load branch.
Calling (1) a live counterfamily would erase this load and double-count the
child reservoir.

## 4. Exact residual ledger

For clarity, suppress the common \(2^{O(L L_2)}\) normalization losses and
the polynomial endpoint loss. Let

\[
 \log K=\Phi,quad \log H=\Phi-\Delta,quad
 \log V=\Phi-r,quad 0\le r\le\Delta.                 \tag{19}
\]

Take a live context bank \(M=V\), a balanced formal split \(AB=M\), and
an endpoint star \(C_eU_e=J=H\). Then the currently certified banks have
logarithms

\[
\begin{array}{c|c}
\text{bank}&\text{logarithm}\ \hline
\text{source contexts}&\Phi-r\\
\text{detached child}&\Phi-\Delta\\
\text{larger directional bank}&\ge
                  \Phi-(r+\Delta)/2\\
\text{two-output records}&2\Phi-r-\Delta
                  \quad\text{inside }V^2.
\end{array}                                                     \tag{20}
\]

The directional lower bound in (20) is no larger than the source line
when \(r\le\Delta\). The last line is no larger than \(2\log V\) for the
same reason. Thus none of the exact inequalities forces an ordinary bank
larger than \(V\). This numerical feasibility is realized by the local
two-cloud/profile operations, but no known construction realizes it while
also controlling every ambient face on \(n\) labels.

This is why the result is a closure of the sparse/low-load branch and a
rigorous applicability boundary, not a claimed proof of the coefficient-half
theorem.

## 5. Verification

Run

```text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_near_ambient_live_context_coefficient_audit.py
```

The verifier checks (4), the sparse-context/high-load split, the balanced
complete-box contradiction for \(\alpha-c>0\), the corrected half-target
near-ambient scale, and every line of the residual ledger for a grid of
\(r/\Delta\) values.
