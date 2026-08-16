# Codimension-three shadow versus the weighted role forest

**Date:** 2026-08-15. All logarithms are base two. Record weights are in
\([0,1]\), and every face below is a literal ordinary face of the same
planar configuration \(P\). Put \(V=V(P)\).

## Verdict

The history-faithful codimension-three theorem is exact, but the current
weighted role forest does **not** supply its low-completion hypothesis.
The forest controls the largest next-label mass conditional on a prefix.
The shadow decoder needs the number of possible values of one coordinate
conditional on **all the other coordinates** (puncture codegree). These are
different statistics.

There is an exact bridge, which is the main positive result of this note.
For three full source words, let \(G\) be the weighted number of omission
triples whose almost-full merged word is ordinary. For any load threshold
\(D\), one of the following occurs:

1. **source-thin:** \(G\) is a small fraction of the \(Wq_1q_2q_3\)
   possible omission incidences;
2. **codimension-three bank:**
   \[
          V\ge {G\over 2D};                                      \tag{1}
   \]
3. **high-completion:** more than \(G/2\) incidence mass lands on actual
   almost-full faces of load greater than \(D\).

If a fixed missing-label triple has residual history mass at most
\(\lambda\), an output of load greater than \(D\) has a physical puncture
extension alphabet larger than \((D/\lambda)^{1/3}\) in at least one of
the three source components. This is a literal source--puncture star. Its
extensions split again into restored ordinary mixed faces or a simple bad
face--face graph. Thus the failure is localized in actual geometry, not in
metadata.

This does not close the live branch. A complete \(d\)-ary product has
maximally uniform role-forest branching, \(Q_{\rm eff}=1\), and puncture
degree \(d\) at every role. Its codimension-three load is exactly \(d^3\),
so the bank has size

\[
                  W{q_1q_2q_3\over d^3}.                         \tag{2}
\]

The rational cyclic construction realizes this sharply in the plane; for
\(q=2,d=3\), the verifier finds \(5,832\) ordinary incidences, \(216\)
outputs, and uniform load \(27\). At the half-scale calibration
\(q_1=q_2=q_3=L/6\), \(d\asymp n/L\), the source mass itself has leading
coefficient \(1/2\), while (2) loses \(n^{3-o(1)}\). This is an exact
applicability barrier, not a low-face construction.

There is also an upstream issue: the live release/three-ear core gives
three individual records and reduced terminal words. It has not yet been
proved that a positive mass of triples shares one literal seam and has
three simultaneously ordinary almost-full words. Consequently neither
the geometric density \(G\) nor the completion load \(D\) required by the
new shadow theorem follows from the present role forest.

## 1. Weighted good-shadow trichotomy

A record \(r\) of weight \(w_r\le1\) carries three words

\[
                 w_r^a=\{x^a_{r,1},\ldots,x^a_{r,q_a}\},
                 \qquad a=1,2,3,                              \tag{3}
\]

on disjoint physical role systems, and a visible seam \(Y_r\). For an
omission triple \(t=(i,j,k)\), write

\[
 O(r,t)=Y_r\cup(w_r^1-\{x^1_{r,i}\})
                 \cup(w_r^2-\{x^2_{r,j}\})
                 \cup(w_r^3-\{x^3_{r,k}\}).                    \tag{4}
\]

Let \(\Gamma_r\) be the set of triples for which (4) is ordinary, put

\[
 W=\sum_rw_r,
 \quad Q=q_1q_2q_3,
 \quad G=\sum_rw_r|\Gamma_r|,                                  \tag{5}
\]

and define the actual weighted output load

\[
                 \ell(O)=\sum_{(r,t):O(r,t)=O}w_r.               \tag{6}
\]

All physical completion and chronology collisions are already included in
\(\ell\).

> **Theorem 1 (good-shadow load trichotomy).** For every \(D>0\),
> \[
> \begin{aligned}
> G_{\le D}&:=\sum_{O:\ell(O)\le D}\ell(O)\le DV,\\
> G_{>D}&:=\sum_{O:\ell(O)>D}\ell(O)=G-G_{\le D}.       \tag{7}
> \end{aligned}
> \]
> Hence, for every \(0<\gamma\le1\), either
> \[
> G<\gamma WQ,                                             \tag{8}
> \]
> or
> \[
> V\ge {\gamma WQ\over2D},                                \tag{9}
> \]
> or more than \(\gamma WQ/2\) good incidence mass lies on
> outputs of load greater than \(D\).

**Proof.** Every good incidence contributes to exactly one literal face,
so summing (6) gives \(G\). There are at most \(V\) outputs, and each term
in \(G_{\le D}\) is at most \(D\), proving (7). If (8) fails, either the
low-load or the high-load part is at least \(G/2\). The former and (7)
give (9); the latter gives the last conclusion. \(\square\)

The theorem is deliberately stated with the **actual** load. It remains
true when histories are correlated across the three components and when
the selected word family is far from Cartesian.

### Low puncture codegree is sufficient

Fix an output \(O\). Its occupancy mask reveals \((i,j,k)\), and its
intersections with the role systems reveal all three punctured words. Let
\(C_a(O)\) be the set of physical labels which occur as the missing label
in component \(a\) among records producing \(O\). Assume that after the
three missing labels are specified, the remaining aggregate history mass
is at most \(\lambda\). Then

\[
                 \ell(O)\le
       \lambda |C_1(O)|\,|C_2(O)|\,|C_3(O)|.                    \tag{10}
\]

This uses no independence: the record support is merely a subset of the
displayed box. In particular, if every good output has
\(|C_a(O)|\le c_a\), Theorem 1 with

\[
                         D=\lambda c_1c_2c_3                    \tag{11}
\]

is exactly the desired bridge to
`HISTORY_FAITHFUL_CODIMENSION_THREE_SOURCE_SHADOW.md`. Constant completion
degrees and \(q_a=\Theta(L)\) return its cubic multiplier with only the
residual history loss.

Conversely, (10) implies

\[
       \ell(O)>D
       \quad\Longrightarrow\quad
       \max_a|C_a(O)|>(D/\lambda)^{1/3}.                         \tag{12}
\]

Thus the third branch of Theorem 1 is a physical high-completion branch.

## 2. The high-completion output is a literal geometric core

For every high-load \(O\), choose canonically a component \(a(O)\) attaining
the maximum in (12). Write \(p_a(O)\) for its punctured word. For every
\(x\in C_a(O)\),

\[
                         A_{O,x}=p_a(O)\cup\{x\}                 \tag{13}
\]

is one of the selected source words and hence is an ordinary face. The
pair \((O,A_{O,x})\) is literal and recovers the missing physical label.

Put

\[
               \mathcal E=\{(O,x):O\text{ high},
                                      x\in C_{a(O)}(O)\}.        \tag{14}
\]

Split it according to whether

\[
                           S_{O,x}=O\cup\{x\}                    \tag{15}
\]

is ordinary.

> **Theorem 2 (restore or bad-core split).** The map
> \((O,x)\mapsto S_{O,x}\) has load at most
> \(q_1+q_2+q_3\) on the ordinary part of (14). Consequently
> \[
>  |\mathcal E_{\rm good}|
>        \le(q_1+q_2+q_3)V.                                    \tag{16}
> \]
> If \(|\mathcal E|>2(q_1+q_2+q_3)V\), the nonordinary pairs contain a
> simple bipartite subgraph on literal faces, with at least
> \(|\mathcal E|/4\) edges and minimum degree at least
> \(|\mathcal E|/(8V)\) on both sides.

**Proof.** Given \(S=S_{O,x}\), guess the restored component and role.
There are \(q_1+q_2+q_3\) choices. The unique label of \(S\) in that role
is \(x\), and deleting it reconstructs \(O\). This proves (16). If the
stated size hypothesis holds, more than half the edges are bad. Repeatedly
delete a left or right vertex of current degree less than
\(|\mathcal E|/(8V)\). Each side has at most \(V\) vertices, so less than
\(|\mathcal E|/8\) is deleted from each side. At least
\(|\mathcal E|/2-|\mathcal E|/4=|\mathcal E|/4\) edges remain, with the
claimed minimum degree. Every remaining union is nonordinary. \(\square\)

The bad graph is of the precise literal face--face type used by the
Rényi/Hall dense-core reductions. There are two scope qualifications:

* (12) only gives a cube-root-sized extension alphabet; a single output may
  carry enormous record mass but only \(O(n)\) distinct physical extensions;
* for fixed \((O,x)\), the other two omitted labels may still have large
  multiplicity. The unweighted simple graph in Theorem 2 is decoder-exact,
  but transferring the full original record mass to its edges requires an
  additional pair-load bound.

Thus high completion has been localized, not paid.

## 3. Why the role-forest statistic does not imply (11)

At a role-forest node, the available statistic is

\[
                     r(v,i)={b\over b_*},                       \tag{17}
\]

where \(b_*\) is the heaviest next-label class. In the low-
\(Q_{\rm eff}\) survivor, almost every deleted large role satisfies
\(r(v,i)\ge d_i/L^{O(1)}\). This is a conditional prefix min-entropy
statement.

Take the complete \(d\)-ary word cube \([d]^q\) with uniform record mass.
Along every fixed prefix,

\[
                      r(v,i)=d,qquad
                      C_{\rm eff}=d^q,qquad Q_{\rm eff}=1.       \tag{18}
\]

Nevertheless every punctured word has exactly \(d\) completions. For
three components, every codimension-three output has load \(d^3\).
Thus the strongest possible form of mass-uniform branching is compatible
with the worst completion load allowed by the physical alphabets.

The converse mismatch is equally sharp. Over \(\mathbb F_d\), take

\[
 \mathcal W_{\rm par}
   =\{(x_1,\ldots,x_{q-1},x_1+\cdots+x_{q-1}):x_i\in\mathbb F_d\}. \tag{19}
\]

The first \(q-1\) prefix levels have uniform branching ratio \(d\), while
every puncture has completion degree one. Only the final prefix level is
deterministic, a single \(O(\log d)\) defect which is allowed by the live
\(O(L\log L)\) forest ledger. Prefix entropy therefore cannot distinguish
the positive MDS-like case (19) from the negative complete cube (18).

This also explains why splitting every large role into binary pairs is not
free. Fixing one pair in each of \(\Theta(L)\) roles retains only
\((2/d)^{\Theta(L)}\) of a uniform cube, a quadratic-exponential loss.
Allowing the pair ID to vary puts that ID back into the omitted completion
load and cancels the apparent gain.

## 4. Exact planar and live-scale calibration

The rational cyclic construction used by the root shadow theorem works for
arbitrary finite role count and alphabet. With \(q=2,d=3\), all almost-full
merged outputs are ordinary and exact enumeration gives

\[
\begin{array}{c|r}
\text{complete source triples}&3^{6}=729\\
\text{omission incidences}&729\cdot2^3=5,832\\
\text{distinct ordinary outputs}&216\\
\text{minimum/maximum load}&27/27.
\end{array}                                                       \tag{20}
\]

Hence planarity and simultaneous almost-full compatibility do not lower
puncture codegree.

For the asymptotic calibration, set \(n=2^L\), take

\[
                  q_1=q_2=q_3=L/6,
                  \qquad d=\lfloor n/(3q_1)\rfloor.             \tag{21}
\]

The role supports fit in \(n\) physical labels and the complete record mass
is

\[
              W=d^{3q_1}=2^{(1/2-o(1))L^2}.                     \tag{22}
\]

But the shadow/source ratio is

\[
                  {q_1^3\over d^3}=2^{-3L+O(\log L)}.            \tag{23}
\]

Thus even at the half-scale normalization, the role forest plus complete
almost-full geometry does not provide the missing polylogarithmic gain.
This calibration counts only the selected source/shadow operation. The
explicit children have other face banks, so (21)--(23) are not an upper
construction for Erdős 838.

## 5. Application audit against the live reductions

The current reductions provide the following, exactly:

1. unordered injective colouring turns every rank-\(O(L)\) source into a
   full role word with only \(2^{O(L)}\) loss;
2. the adaptive-release output remembers the retained labels and empty
   roles, while its deleted completion word reconstructs the source;
3. on the low-\(Q_{\rm eff}\) branch, all but \(O(\log L)\) roles are
   deleted and almost all deleted next-label laws are mass-uniform; and
4. the Rényi/Hall reduction produces a dense core of literal source/context
   and continuation faces when continuation collisions do not pay.

They do **not** yet provide:

1. one coalesced record whose three source systems are disjoint and share a
   literal visible seam;
2. a lower bound \(G=\Omega(Wq_1q_2q_3)\) for simultaneous almost-full
   convexity; or
3. a bound \(D=2^{O(L\log L)}\), let alone constant \(D\), for the actual
   three-puncture output load.

In fact item 3 of the provided data points in the opposite direction: the
terminal forest retains only \(O(\log L)\) roles, while (4) retains all but
one role in each component. Heredity lets one delete more labels; it cannot
infer the convexity of these much larger almost-full unions.

Accordingly, the root artifact closes the **almost-full, low-completion**
branch. The exact surviving alternatives are now:

* geometrically source-thin simultaneous words, to be charged by their
  first rooted/cross circuit;
* a high physical puncture-extension star, followed by Theorem 2; or
* residual same-output history multiplicity not controlled by the current
  pair decoder.

No half-coefficient conclusion follows without eliminating these branches.

## 6. Verification

Run

```text
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_codim_three_role_forest_completion_gate.py
```

The verifier:

* exhausts complete \(d\)-ary three-word shadows and checks uniform load
  \(d^3\) and the exact output formula;
* verifies the restored-one-coordinate decoder load \(q\);
* realizes the \(q=2,d=3\) shadow in the exact rational planar cyclic
  gadget and checks convexity of all \(5,832\) incidences;
* compares the complete cube and parity code, checking identical uniform
  early prefix branching but puncture degrees \(d\) and one;
* checks the load trichotomy for several nontrivial good-incidence masks;
  and
* audits the half-scale loss (23).
