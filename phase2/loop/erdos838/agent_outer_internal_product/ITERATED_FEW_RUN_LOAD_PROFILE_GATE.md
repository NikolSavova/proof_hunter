# Iterated few-run load: terminal-mask coalescence or a nested profile reset

**Date:** 2026-08-15. All logarithms are base two. This continues
NEAR_AMBIENT_LIVE_CONTEXT_COEFFICIENT_AUDIT.md at its high-projection-load
endpoint.

## Verdict

Repeated source/mask/run descent on one fixed role colouring does **not**
create a new entropy telescope. All recoverable gaps created at intermediate
times coalesce into the components of the terminal deletion mask.

Let \(X_1,\ldots,X_s\) be the cyclic physical roles and let

\[
                 M_0\subseteq M_1\subseteq\cdots\subseteq M_t
                    \subseteq[s]                              \tag{1}
\]

be the roles deleted along repeated high-load descents. If the terminal mask
\(M_t\) has \(g\) cyclic components, then:

1. every intermediate boundary gap which survives in the terminal carrier
   is a boundary gap of \(M_t\), so there are at most \(2g\) surviving
   directed boundaries and at most \(g\) deleted runs;
2. if \(|M_t|=h\), one terminal run has length at least \(h/g\).

Consequently, on the excess-rank slice

\[
                    s-cL\ge\varepsilon L,              \tag{2}
\]

iteration gives exactly the already known dichotomy. Either
\(g=\Omega(L_2)\), and the actual surviving gaps enter the decoded
rooted-module product, or one terminal run has

\[
            |R|=\Omega(L/L_2),\qquad
            |X_R|=\Omega(n/L_2).                       \tag{3}
\]

Thus horizontal iteration cannot manufacture more gaps than the terminal
mask and cannot improve the \(n/\log\log n\) child scale. If intermediate
gaps are destroyed rather than surviving, they enter the fixed-edge
circuit/shield load; this is the declared geometric alternative, not hidden
entropy.

There is only one way to “iterate inside” the run: re-colour or rechart the
induced child and start a new mask problem there. That is a **vertical
profile reset**. The old external source word can remain in the projection
load unchanged, so no entropy decrement follows merely from nesting.
For arbitrary weighted projection maps \(\pi_j\), if \(W_j\) is the mass
entering level \(j\), \(C_j\) is the number of geometric context states,
and a heaviest fibre of mass \(W_{j+1}\) is retained, the exact statement is
only

\[
               W_{j+1}\ge {W_j\over C_j},\qquad
               W_t\ge {W_0\over\prod_{j<t}C_j}.         \tag{4}
\]

Equality is possible, and if every \(C_j=1\), the coefficient-half load is
unchanged at every depth. Independently, a finite tower of projectively
nested common \(1+3\) cages realizes the geometric nesting half of this
obstruction with arbitrary rational child order types. Coupling the two
facts into a live globally minimizing family is not proved. Its complete
ambient face complex is not controlled; the statement is a sharp
decoder/applicability barrier, not a sub-half construction.

What *does* telescope exactly is the induction deficit. Put

\[
 L_j=\log n_j,\qquad a_j=L_j-L_{j+1},\qquad
 \delta_j=\Phi(L_j)-\Phi(L_{j+1}).                       \tag{5}
\]

Then

\[
       \boxed{\displaystyle
       \sum_{j<t}\delta_j=\Phi(L_0)-\Phi(L_t).}          \tag{6}
\]

For \(n_{j+1}\asymp n_j/L_2\), each
\(a_j=L_3+O(1)\) and \(\delta_j=(1+o(1))L_jL_3\).
If the root counterexample has

\[
 V(P)=2^{\Phi(L_0)-r},                                   \tag{7}
\]

then induction on the terminal child forces

\[
                 r\le\Phi(L_0)-\Phi(L_t)
                    =\sum_{j<t}\delta_j.                \tag{8}
\]

At cumulative deficit \(\Delta_t=\sum_{j<t}\delta_j\), the exact
endpoint/source Cauchy bank has logarithm, up to the certified global
normalization and polynomial endpoint losses,

\[
                 \Phi(L_0)-{r+\Delta_t\over2}.           \tag{9}
\]

Because of (8), (9) need not exceed
\(\log V(P)=\Phi(L_0)-r\). Repeating the child descent does not change this
square-root sign.

If the terminal runs occur simultaneously in one genuine **linear strong
glue** chart, there is a positive theorem: the corrected linear-profile
potential closes unless their cap potentials form an
\(O(L_3)\)-coherent ramp. This is the exact remaining macro-run state.
For \(q=\Theta(L_2)\) run children of size \(D=2^d\), where

\[
                  \log q=\Theta(L_3),\qquad d=L-O(L_3),
                                                                    \tag{10}
\]

the scalar menu

\[
 C_i=D^{b+i},\qquad U_i=D^{h-b-i},\qquad H_i=D^h,
 \qquad C_iU_i=H_i                                      \tag{11}
\]

with \(b=(h-q)/2\) has constant corrected potential
\(\log_D C_i-i=b\). Every cross term is exactly \(H_i/D\) at the
monomial level, and the complete linear recurrence obeys

\[
                         qH\le W_{\rm lin}\le2qH          \tag{12}
\]

for \(D\gg q^2\), while the half target at \(qD\) exceeds (12) by

\[
 \Phi(d+\log q)-\Phi(d)-O(\log q)
                    =(1+o(1))L L_3.                    \tag{13}
\]

This is a sharp **formal** barrier: it satisfies endpoint energy,
minimizer reflection anti-alignment, and the corrected linear recurrence.
It is not asserted to be the profile menu of planar induction-minimal
children. Realizing or excluding this coherent macro-run ramp is precisely
the live profile-penetration theorem.

Therefore repeated descent has a rigorous global stopping point:

* on one fixed role system it collapses to the terminal many-gap/one-run
  dichotomy;
* a nested restart preserves external projection load and changes the
  problem into coherent profile regeneration;
* a genuine linear macro chart closes unless the formal ramp (11) survives;
  and
* arbitrary cyclic child factorization is still unavailable.

No coefficient-half closure is claimed.

## 1. Terminal-mask coalescence

View the role indices as vertices of a cycle. A directed boundary of a mask
\(M\) is an adjacent ordered pair \((i,i+1)\) with exactly one endpoint in
\(M\). Suppose it is a boundary of \(M_j\) and survives in the terminal
carrier: the endpoint outside \(M_j\) is never deleted later. Since masks
are monotone, the endpoint inside \(M_j\) remains deleted. Hence it is also
a boundary of \(M_t\).

A nonempty proper cyclic mask with \(g\) components has exactly \(2g\)
directed boundaries and \(g\) deleted runs. This proves the first assertion
after (1). The component lengths sum to \(|M_t|\), so the largest is at
least \(|M_t|/g\), proving the second.

If every role is deleted, there are no terminal boundaries and the whole
cycle is already one run of length \(s\), which belongs directly to the
one-run alternative.

In the balanced role slice, every role has
\(D=\Theta(n/L)\) physical labels. If the descent must remove the excess
rank in (2), then \(|M_t|\ge\varepsilon L\). With
\(g<\rho L_2\), one component has at least
\(\varepsilon L/(\rho L_2)\) roles and physical size at least a constant
times \(n/L_2\), proving (3).

This is already an iterated theorem: deleting the components in any order,
extending an old component, or merging two old components cannot improve
the terminal alternative. Intermediate gaps which do not survive cannot be
used together in one final rooted-module face. Charging them requires their
actual circuit/shield history, exactly as in the fixed-edge telescope.

## 2. Horizontal descent versus a vertical reset

On a fixed role system, a source word assigns one actual label to every
role. Removing a run from the completion trace makes its labels empty in
the mixed output, but the global forest decoder can recover the selected
path labels. Repeating this operation simply enlarges the monotone mask in
(1). There are no new role coordinates and no independent copy of the
source entropy.

A restart inside \(X_R\) is different. It chooses a new role colouring and
new geometric contexts on the child ground. The old outside source word is
not a label of that child. If it is omitted from the new output, all of its
multiplicity is inherited by the new projection load. Thus the only
unconditional mass calculation is (4): grouping \(W_j\) over \(C_j\)
contexts and retaining a largest group. A common context has \(C_j=1\) and
causes no decrease.

This is not merely an abstract set-system warning. The projective tangent
coordinates used in the central-nesting barrier accept an arbitrary
rational child order type. Apply the map at level \(t-1\), then regard the
entire rational result as the arbitrary child at level \(t-2\), and so on.
For every fixed depth, sufficiently small rational scales preserve all
earlier strict orientations. At every level, the inner label of a fixed
child pair lies in every triangle formed by its outer partner and the two
local arc labels. Hence all the common \(1+3\) incompatibilities persist
with one stationary external context word.

The construction controls the nested trace operation only. Multi-label
faces in wrapper cells and directional profiles at every level remain in
the ambient complex. It proves that repeated circuit nesting alone does not
decrease \(\Lambda_{\rm proj}\); it does not prove that a least
counterexample contains such a tower.

## 3. Exact target and ambient ledgers

For any function \(\Phi\), (6) is ordinary telescoping. For

\[
                 \Phi(L)={L^2\over2}-C L\log L,          \tag{14}
\]

one step has

\[
\begin{aligned}
 \delta_j
 &=L_ja_j-{a_j^2\over2}\\
 &\quad-C\{L_j\log L_j-(L_j-a_j)\log(L_j-a_j)\}.        \tag{15}
\end{aligned}
\]

If \(a_j=O(L_3)\), this is
\(L_ja_j-O(a_jL_2+a_j^2)\).

The child face bank is an actual induced ambient bank. Therefore (7) and
the inductive lower bound \(V(X_t)\ge2^{\Phi(L_t)}\) give (8). Let a live
source/context family have size \(M\ge V(P)2^{-O(L L_2)}\), and let an
endpoint star in \(X_t\) have size at least
\(2^{\Phi(L_t)-O(L)}\). The two directional outputs have product at least
the product of these two quantities. Cauchy gives (9), with an additional
\(-O(L L_2)\) normalization term. Its difference from \(\log V(P)\) is

\[
                      {r-\Delta_t\over2}-O(L L_2),       \tag{16}
\]

which is nonpositive by (8). This proves the claimed persistence of the
square-root obstruction at every nested depth.

## 4. The exact macro-run profile recurrence

Assume now that \(q\) disjoint terminal runs have been promoted to one
actual ordered linear strong-glue chart. Let their common physical size be
\(D=2^d\), and write \(H_i,C_i,U_i\) for nonempty ordinary, cap, and cup
counts in that chart. The exact face bank is

\[
 W_{\rm lin}=\sum_iH_i+
   \sum_{i<j}C_iU_j(1+D)^{j-i-1}.                       \tag{17}
\]

The corrected potential theorem applies verbatim. A downward fluctuation
of size

\[
 1+{\Phi(d+\log q)-\Phi(d)\over d}=(1+o(1))\log q       \tag{18}
\]

in \(\log_D C_i-i\), or the corresponding endpoint surplus, makes one
term in (17) reach the parent target. If no term closes, the potentials
form the coherent ramp and almost every child has a polynomially localized
common-endpoint cap/cup module.

For the formal regression choose integers \(h,q\) of the same parity with
\(h>3q\) and put \(b=(h-q)/2\). Then every exponent in (11) lies between
zero and \(h\), and

\[
 C_iU_jD^{j-i-1}=D^{h-1}=H/D                       \tag{19}
\]

for all \(i<j\). Since
\((1+D)^k\le2D^k\) for \(k\le q\ll D\), the cross part of (17) is at most
\(q^2H/D\), proving (12) for \(D\ge q^2\). The potential
\(\log_D C_i-i=b\) is exactly constant.

For the scale audit, choose \(h=\Phi(d)/d+O(1)\), adjusting by one so that
\(h\) and \(q\) have the same parity. This changes \(\log H\) by only
\(O(d)=O(L)\). Taking \(q=\Theta(L_2)\) gives
\(\log q=\Theta(L_3)\) and \(d=L-\Theta(L_3)\). Direct expansion of (14)
then proves (13). Thus horizontal
coalescence followed by an honest linear promotion reduces the whole
iteration to one precise question: can planar minimizer children realize
the constant-potential menu, or must their endpoint modules align and pay?

## 5. Verification

Run

~~~text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_iterated_few_run_load_profile_gate.py
~~~

The verifier exhausts monotone cyclic mask chains through ten roles and
checks terminal-boundary coalescence and the largest-component bound. It
checks the projection-load product, the corrected target telescope, the
ambient ledger (8)--(9), and exact formal macro ramps with constant
potential and recurrence at most \(2qH\).
