# The live atom floor survives, but cancels only completion redundancy

**Date:** 2026-08-15.  All logarithms are base two.  This audits the exact
live applicability of `TERMINAL_WEIGHT_FLOOR_EXCESS_RANK_GATE.md`.

## Verdict

In the canonical rank-safe minimizer chain, every nonzero raw record entering
the completion-role forest has weight at least

\[
                              w_0={1\over n}.           \tag{1}
\]

All surviving operations before the dense Hall core either discard whole
atoms, duplicate them without dividing their weights, deterministically
relabel their endpoints, or coalesce them by addition.  The fractional Hall
routing can split atoms, but that routing is used only in the low-density
branch which already closes; the high-density survivor is obtained by
deleting vertices and their incident **original** records.  It is therefore
invalid and unnecessary to feed routed Hall fragments into the role forest.

Run the deterministic role forest separately inside one fixed released-face
fibre \(U\).  If its raw mass is \(M_U\), every terminal path satisfies

\[
 C_{\rm eff}(O)\le {M_U\over\mu(O)}\le nM_U,
 \qquad
 \boxed{\ Q_{\rm eff}(O)\ge{P_0\over nM_U}.\ }         \tag{2}
\]

Since the ordered pair \((A,U)\) has load at most \(\delta\),

\[
                              M_U\le\delta V(P),       \tag{3}
\]

and hence

\[
                  \boxed{\ Q_{\rm eff}(O)
                    \ge {P_0\over n\delta V(P)}.\ }   \tag{4}
\]

This kills the quadratically small weighted-prefix leaf from
`EXCESS_RANK_PREFIX_STAR_COHERENCE_GATE.md`: that abstract calibration uses
terminal weight \(d^{-(s-k)}\), below \(1/n\) as soon as the excess-role
entropy is more than \(L\).

However, (2)--(4) do **not** supply the missing
\(n^{\Theta(\log\log n)}\) multiplier.  In a complete
\(M_D\times H\) source--release rectangle with unit atoms, the effective
forest can have

\[
 C_{\rm eff}=M_D,\qquad Q_{\rm eff}={P_0\over M_D},   \tag{5}
\]

and delete every completion role.  The only actual terminal bank is the
\(H\)-element released family.  Thus the \(Q_{\rm eff}\) saving cancels the
ambient completion redundancy \(P_0/M_D\) and returns the already known
released bank; it does not multiply \(M_D\) by \(H\).

The dense Hall degrees do not change this algebra.  In the rectangle they
are exactly \(H\) on the completion side and \(M_D\) on the released side,
while (5) is equality.  A further gain requires a mixed/profile bank or a
third retained tag, not a stronger atom-floor estimate.

Therefore the floor is a rigorous and useful narrowing:

* **ruled out:** quadratic-depth Kraft weights created by hidden fractional
  normalization;
* **still live:** an atom-preserving, unit-weight all-deletion rectangle whose
  effective saving is exactly its completion redundancy.

The central Pascal common-guard rectangle is the mandatory live planar
calibration of the latter phenomenon (at coefficient above one half).  No
minimizer closure is claimed.

There is also a stronger mass-to-count normalization.  Before pocket
replication, bucket the nonzero source atoms into the at most
\(1+\lceil\log n\rceil\) intervals

\[
                         [2^{-j-1},2^{-j}).             \tag{4a}
\]

One bin retains at least an \(O(1/L)\) fraction of the live weight.  All
later surviving records in that bin have weights in one fixed interval
\([\lambda,2\lambda)\).  At every forest split, effective mass branching
then differs from the corresponding raw-count branching by at most a factor
four.  Along \(s=O(L)\) roles the total discrepancy is at most
\(4^s=2^{O(L)}\), only polynomial.  Thus the final live residue can be
treated as an essentially unit-weight simple rectangle.  This still does not
create cross-role codegrees or mixed faces.

## 1. Atom preservation through the live chain

The initial canonical marked incidence is

\[
 \omega(A,T)={1\over n}
  |\{p:T_A(p)=T\text{ and }(A,p)\text{ is heavy}\}|.   \tag{6}
\]

Every nonzero value in (6) is an integer multiple of \(1/n\), proving the
initial floor.

The subsequent live reductions act as follows.

1. **Rank/root cutoff and position colouring.**  These retain a subset of
   actual sources and leave \(\omega(A,T)\) unchanged.
2. **Pocket replication.**  For each retained source and every pocket face
   \(F\), the raw record \((A,F)\) has weight \(\omega(A,T)\).  The phrase
   “choose \(F\) uniformly” in the entropy proof refers to normalization by
   the total mass \(WH\); it does not replace the raw edge weight by
   \(\omega/H\).  This is confirmed by the downstream raw mass
   \(M_s\ge WH/\Gamma\).
3. **Minimum guard, rank/mask/state buckets, fixed labels, circuit choices,
   and semialgebraic support restrictions.**  These are deterministic maps
   followed by restriction.  They do not split an atom.
4. **High-density Hall core.**  Iterative low-degree deletion keeps original
   weighted records.  Fractional routing belongs to the alternative
   low-density proof and is not part of the surviving core.
5. **Cross-circuit chronology and role forest.**  These retain complete
   actual-label classes and delete fixed geometric labels from endpoints;
   record weights are unchanged.
6. **Coalescing and dyadic bookkeeping.**  Coalescing adds atom weights.  The
   stated label-state compression rounds a dyadic layer upward, so it cannot
   lower (1).  Even a symmetric factor-two downward convention would leave
   the harmless floor \(1/(2n)\).

Thus (1) is valid for the literal high-density records.  It need not hold
for formal fractions produced by a max-flow, which is why the branches must
not be conflated.

## 2. Fibrewise forest and decoder

Fix one actual released face \(U\).  It determines its source occupancy mask
and hence its deleted role box in the position-coloured chart.  Run a
separate deterministic forest on all literal records incident with \(U\).
The selected labels may depend on \(U\), because every terminal output
retains its released-ground trace and therefore identifies which forest to
use.  The empty-role mask then reconstructs the selected label history as
before.

Let a terminal path have node masses

\[
                         m_0=M_U,m_1,\ldots,m_t=\mu(O). \tag{7}
\]

At edge \(j\), if \(b_j\le m_j\) is the chosen canonical-role mass, then

\[
                  r_j={b_j\over m_{j+1}}\le{m_j\over m_{j+1}}.   \tag{8}
\]

Multiplication gives the first inequality in (2).  A nonempty terminal
contains at least one unsplit original atom, so \(\mu(O)\ge1/n\), proving
the second inequality and (4).

For (3), group the fibre by its actual completion/source face \(A\).  Every
fixed ordered pair \((A,U)\) has total weight at most \(\delta\), and there
are at most \(V(P)\) possible \(A\).

### 2a. One dyadic bucket converts mass branching to count branching

The initial weights lie in \([1/n,1]\), so (4a) has at most \(L+2\)
nonempty bins.  Pocket replication copies a source atom at the same weight;
hence choosing one source bin before replication retains the complete pocket
product for those sources.  It costs only \(O(\log L)\) bits.

Fix the retained bin, and consider one role split at a later forest node.
Let \(N_z\) and \(b_z\) be the raw count and mass of actual-label class
\(z\), let \(N=\sum_zN_z\), and let \(z_*\) be the mass-heaviest class.
Write \(N_{\max}=\max_zN_z\).  Since

\[
              \lambda N_z\le b_z<2\lambda N_z,        \tag{8a}
\]

mass maximality gives \(N_{z_*}\ge N_{\max}/2\).  Therefore

\[
 {1\over2}{N\over N_{\max}}
       \le r={\sum_zb_z\over b_{z_*}}
       \le4{N\over N_{\max}}.                        \tag{8b}
\]

Multiplying (8b) down a path of length at most \(s\) costs at most \(4^s\).
The same comparison applies after every restriction and Hall-core pruning,
because no surviving atom changes weight.  Hence a mass-uniform survivor is,
up to polynomial loss, a count-uniform survivor.

The unit prefix-star in Section 3 shows the limit: count normalization sends
its thin tail to the correct high-\(Q\) branch, but the resulting saving is
exactly \(P_0/M_D\) and still leaves only the released columns.

## 3. Exact rectangle cancellation

Let \(\mathcal E\) be the unit-weight prefix-star family from
`EXCESS_RANK_PREFIX_STAR_COHERENCE_GATE.md`, let
\(M_D=|\mathcal E|\), and take a released alphabet \(\mathcal H\) of size
\(H\).  Put one unit record on every pair

\[
                         \mathcal E\times\mathcal H.   \tag{9}
\]

For each fixed \(U\in\mathcal H\), follow the zero path.  Its heaviest-class
ratios telescope from \(M_D\) records to one terminal record, so

\[
                  C_{\rm eff}=M_D,qquad
                  Q_{\rm eff}=P_0/M_D.                \tag{10}
\]

If every nonempty completion trace is incompatible with \(U\), all roles
are deleted and the terminal output is just \(U\).  Across the whole
rectangle there are exactly \(H\) terminal faces, one per released column,
although the effective potential is

\[
                    H\cdot1\cdot M_D=M_DH,            \tag{11}
\]

equal to the raw record mass.  This is the exact square-to-linear
cancellation.

The bipartite Hall graph of (9) is complete, with minimum degrees \(H\) and
\(M_D\).  Thus arbitrarily strong two-sided degree lower bounds coexist with
(10)--(11).  The algebra cannot be improved without using an additional
ordinary-face operation.

The construction in this section is an abstract role rectangle.  It has the
standard rational anti-aligned realization, but that realization exposes
Boolean cloud banks and is not live.  The central Pascal common-guard report
provides the live-normalized planar applicability barrier.

## 4. Verification

Run

```text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_live_atom_floor_role_forest_audit.py
```

The verifier checks the \(1/n\) floor under restriction, duplication,
coalescing, and upward dyadic rounding; verifies (2) on exact rational
weighted geometric fibres; and checks the complete prefix-star rectangle
equalities (5), (10)--(11) together with its exact Hall degrees.  It also
exhausts small dyadic-bin class tables and verifies (8b).
