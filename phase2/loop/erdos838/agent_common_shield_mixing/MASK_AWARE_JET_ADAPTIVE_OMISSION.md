# Rich seam jets: adaptive omission closes fixed-base ears, not detached masks

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

Partitioning local faces by their actual first-two/last-two boundary jet
costs only four label tags and therefore preserves every quadratic local
face coefficient.  In a genuine fixed-convex-base ear cycle, this is more
than enough: rich-jet incompatibility with neighboring singleton ears can
always be turned into a one-face bank by deleting precisely the one or two
neighboring ears whose seams fail.  The resulting decoder load is at most
the product of the two neighboring singleton alphabet sizes, hence at most
`D^2`.

Concretely, if `E` is a family of `M` valid full ear words, `m_i` is its
selected trace projection size in cell `i`, and `J_g` is any family of
root-admissible local ear faces in cell `g`, then

\[
 \boxed{
 V(P)\ge {J_gM\over m_gm_{g-1}m_{g+1}}.}               \tag{1}

\]

No compatibility density, Ferrers alignment, cyclic choice of jet classes,
or guard-release assertion is needed.  The operation is **adaptive adjacent
omission**: insert the local face and omit each adjacent selected ear whose
shared-base-vertex turn is bad.

Thus the six-point multi-ear example which defeated deletion of the bad
base vertex is no longer an obstruction at coefficient scale.  Its two
ears are individually root-admissible; omitting the incompatible neighboring
ear leaves the other ordinary ear unchanged.

This does **not** close the detached radial gate.  In a detached occupied
mask there is no permanently retained base edge between macro cells.
Deleting one guard changes the predecessor/successor of the replacement
face and can expose a new, farther seam.  The exact rational `1+3` circuit
from `DOMINANCE_CELL_SEPARATED_ONE_GAP.md` already has:

* a complete singleton product and support redundancy `R=0`;
* a fixed actual two-point replacement jet; and
* a nonconvex output after the prescribed guard is omitted.

Hence fixed-jet localization alone does not prove nonseparated radial
release.  The remaining operation is now precise: either promote the
retained homogeneous singleton container to a fixed-base oriented-ear
system, or prove a mask-aware deletion cascade whose total erased alphabet
has only `2^{o((log D)^2)}` load; otherwise charge the first new bad seam by
a circuit/shield bank.

Within the fixed-base ear branch, the coefficient calculation is complete.
If `q<=kappa log D`, `log M=(a+o(1))(log D)^2`, and the root-admissible local
reservoirs have coefficient `c_0`, then choosing the best rich jet class in
(1) gives

\[
 {\log V(P)\over(\log D)^2}
     \ge a+c_0(a/\kappa)^2-o(1).                        \tag{2}

\]

For `c_0=1/8` and `a=kappa=1/4`, this is `3/8-o(1)`.

## 1. Jet localization loses only four labels

Let `X` be an `L`-point local support with a fixed boundary orientation.
For every nonempty ordinary face `F subseteq X`, record its first two and
last two boundary labels, allowing the two pairs to overlap at ranks two
and three and padding a singleton by one formal symbol.  There are at most

\[
                              (L+1)^4                    \tag{3}

\]

jets.  Therefore any face reservoir `mathcal H` has a jet class
`mathcal J` with

\[
             |\mathcal J|\ge {|\mathcal H|\over(L+1)^4},
 \qquad
 \log|\mathcal J|\ge\log|\mathcal H|-4\log(L+1).       \tag{4}

\]

If

\[
                   \log|\mathcal H|
                     \ge(c_0-o(1))(\log L)^2,           \tag{5}

\]

then the same leading coefficient holds for `mathcal J`.  Once the root
edge and macro side are fixed, whether every face in `mathcal J` is an
admissible ear is determined by its endpoint turns; the internal turns are
already certified by ordinary convexity.  Likewise its seam compatibility
with a neighboring singleton anchor is a fixed orientation inequality,
and varying anchors form a Ferrers threshold after ray ordering.

The qualification “root-admissible” is essential.  A rich detached jet
class may be ordinary by itself while failing when the fixed base is
restored.  Equation (4) does not say that a rich jet class is root-good.
The theorem below applies after a root-good class is found; a root-bad rich
class remains an anchored circuit/shield input.

## 2. Adaptive adjacent-omission theorem

Let

\[
                         B=(b_1,\ldots,b_q)              \tag{6}

\]

be a fixed strictly convex base in counterclockwise order.  Cell `i`
consists of ears replacing edge `e_i=b_ib_(i+1)`.  Assume the oriented-ear
hypotheses of `CYCLIC_FERRERS_ONE_GAP.md`:

1. each local trace is an individually convex admissible ear at its edge;
2. nonadjacent ears commute; and
3. a word is convex exactly when every pair on adjacent occupied edges has
   the correct turn at their shared base vertex.

Let `mathcal E` be `M` valid full words.  Write `mathcal A_i` for its
projection to cell `i` and `m_i=|mathcal A_i|`.  Fix a cell `g` and any
family `mathcal J_g` of `J_g` admissible ear faces at `e_g`—for example a
rich fixed-jet class from (4).

Delete cell `g` from every selected word and merge duplicates.  The family
`mathcal P_g` of partial words has size `Q_g` with

\[
                              Q_g\ge M/m_g.              \tag{7}

\]

For `(p,F) in mathcal P_g times mathcal J_g`, let

\[
 D(p,F)\subseteq\{g-1,g+1\}                             \tag{8}

\]

contain precisely the neighboring ears whose seam with `F` has the wrong
turn.  Define

\[
 \Phi(p,F)=B\cup F\cup
     \bigcup_{i\ne g,\ i\notin D(p,F)}p_i.              \tag{9}

\]

> **Theorem 1 (adaptive adjacent omission).**  Every output in (9) is one
> ordinary face, and the map has load at most
> 
> \[
>                              m_{g-1}m_{g+1}.            \tag{10}
> \]
> 
> Consequently (1) holds.

**Proof.**  Removing an ear restores its fixed base edge.  It does not make
two previously nonadjacent ear edges adjacent: the intervening base
vertices and edges remain present.  All retained seams not involving `F`
are inherited from the valid partial word `p`.  Every retained seam
involving `F` is good by the definition of `D(p,F)`.  At a deleted seam,
the turns into the two ends of the restored base edge are inherited from
the individually admissible ears on those incident edges (one of them is
`B union F` when the deleted edge neighbors `g`).  The local-to-cyclic turn
criterion therefore makes (9) convex.

Inside the fixed cell system, the output recovers `F`, every retained
coordinate of `p`, and the deletion mask `D(p,F)` by intersection with the
disjoint supports.  Only the values of the at most two deleted neighboring
ears are lost.  There are at most `m_(g-1)m_(g+1)` choices for them, proving
(10).  Equations (7) and (10) give

\[
 |\operatorname{im}\Phi|
  \ge {J_gQ_g\over m_{g-1}m_{g+1}}
  \ge {J_gM\over m_gm_{g-1}m_{g+1}},                   \tag{11}

\]

which is (1).  QED.

The proof does not use Ferrers beyond the geometric fact that a seam can
be tested locally.  Incompatibility is not concentrated or averaged; its
offending selected ear is simply omitted.  This costs at most two alphabet
labels, rather than a positive fraction of the quadratic source entropy.

## 3. Coefficient consequence

Suppose selected traces are singletons, so `m_i=L_i`, and every cell has a
root-admissible reservoir `mathcal H_i`.  Choose a rich jet class
`mathcal J_i` satisfying (4), and put `s_i=log L_i`.  If

\[
             \log|\mathcal H_i|\ge(c_0-o(1))s_i^2,      \tag{12}

\]

then

\[
 \begin{aligned}
 \max_i\log{J_i\over m_i}
 &\ge {1\over q}\sum_i
       \left(\log|\mathcal H_i|-4\log(L_i+1)-s_i\right)\\
 &\ge {c_0-o(1)\over q}\sum_i s_i^2-{5\over q}\sum_i s_i-O(1)\\
 &\ge (c_0-o(1)){(\sum_i s_i)^2\over q^2}
                     -{5\over q}\sum_i s_i-O(1).       \tag{13}
 \end{aligned}

\]

Here the last line is Cauchy--Schwarz.  Since
`sum_i s_i=log P_0>=log M`, equation (1), `m_(g-1)m_(g+1)<=D^2`, and
`sum_i s_i/q<=log D` give

\[
 \log V(P)\ge\log M
       +(c_0-o(1)){(\log M)^2\over q^2}-7\log D-O(1).   \tag{14}

\]

Equation (2) follows.  With `c_0=1/8` and `a=kappa=1/4`, the quadratic
coefficient is exactly

\[
 {1\over4}+{1\over8}\left({1/4\over1/4}\right)^2
                           ={3\over8}.                  \tag{15}

\]

Thus all-rich Ferrers anti-alignment cannot block `3/8` in the fixed-base
ear model.  The rich class at the best single cell suffices; no globally
compatible cyclic choice of jet classes is required.

## 4. The earlier six-point obstruction disappears here

Take the exact example from `CYCLIC_FERRERS_ONE_GAP.md`:

\[
 \begin{aligned}
 B&=\{(-3,0),(3,0),(0,4)\},\qquad z=(3,0),\\
 L&=\{(-10,-16),(-9,-15)\},\qquad R=\{(8,1)\}.
 \end{aligned}                                         \tag{16}

\]

Both `B union L` and `B union R` are admissible ears on adjacent base
edges, while `B union L union R` is nonconvex.  Deleting the bad shared
base vertex `z` also fails: `(-9,-15)` remains hidden.  This killed
automatic guard release even with all seam labels fixed.

Theorem 1 uses a different operation.  The seam between `L` and `R` is
bad, so omit the neighboring ear `R` and restore its base edge.  The output
is exactly the already certified ordinary ear `B union L`.  If `R` ranged
over an alphabet, its value would be the one missing decoder label and
would cost at most its alphabet size.  Hence this counterexample does not
consume any quadratic coefficient after adaptive omission.

## 5. Why detached radial masks remain different

The fixed-base proof uses one property which a detached radial occupied
mask does not have: deleting an ear restores a permanent base edge and
does not change which other ears are adjacent.

In a detached macro cycle, deleting cell `i` makes the preceding and
following **occupied** cells the new directional neighbors.  A replacement
face may therefore pass its old seam test and fail a newly exposed farther
test.  Repeating adaptive deletion can cascade through `Theta(q)` cells,
whose erased alphabet can have quadratic entropy.

The rational broad-cell example makes this failure exact.  With root

\[
                         u=(-1,0),\qquad v=(1,0),        \tag{17}

\]

put

\[
 \begin{aligned}
 q&=(-19/20,1/20),&x&=(-3/40,7/8),\\
 w&=(0,10/11),&z&=(3/40,7/8),&y&=(2/15,8/9).
 \end{aligned}                                         \tag{18}

\]

The singleton cells `X_1={q}`, `X_2={x}`, `X_3={w}` and
`X_4={z,y}` form a complete selected product: both rooted full words are
convex, so `R=0`.  The replacement face `F={z,y}` has one completely fixed
boundary jet.  Nevertheless, after omitting `X_3`, the formal detached
output

\[
                              \{q,x,z,y\}                \tag{19}

\]

is nonconvex, because

\[
 z={3\over230}q+{122\over575}x+{891\over1150}y.         \tag{20}

\]

The obstruction is a strict `1+3` circuit.  Jet localization has no effect:
the bad class already has a single fixed jet.  What fails is the permanent
base-edge hypothesis, not uncertainty about the seam labels.

This example is not a global low-face counterexample; its detached local
faces and other occupied masks may pay.  It proves that Theorem 1 cannot be
quoted for the nonseparated radial model.

## 6. Exact remaining atom

After the present theorem, the live geometry splits cleanly.

* **Fixed convex base, root-admissible ears:** solved at coefficient scale
  by adaptive adjacent omission, with load `D^2`.
* **Root-bad rich jet class:** already an anchored nonconvex/circuit class,
  but it still needs a summable ordinary-face release or shield charge.
* **Detached occupied mask:** one must control the deletion cascade.  A
  sufficient theorem would show that some rich fixed-jet class becomes
  ordinary after erasing neighboring cells of total alphabet entropy
  `o((log D)^2)`.  Otherwise the first newly exposed bad seam must yield a
  recoverable circuit/shield bank of the same incidence coefficient.

The missing history coordinate is therefore the predecessor/successor in
the **current occupied mask** after each deletion.  First-two/last-two face
jets are sufficient only once that mask state is fixed.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_mask_aware_jet_adaptive_omission.py
```

The checker verifies jet-class pigeonholing, an exhaustive finite
fixed-base compatibility system and its exact `m_(g-1)m_(g+1)` decoder
load, the coefficient `3/8`, the strict six-point guard-release failure and
adaptive-ear success, and the rational detached-mask circuit.
