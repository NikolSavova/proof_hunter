# Weighted rooted histories: the homogeneous Hall barrier

**Date:** 2026-08-15

## Verdict

The dense rooted-triple branch lifts exactly to full temporal histories, but
the natural complementary cup/cap Hall decoder has unavoidable polynomial
load.  On the classical stretchable Erdős--Szekeres configuration
\(W=E(k,k)\), add a root whose star has the cup sign.  If
\(U_{k,k}(t)\) is the generating polynomial of all nonempty cups in \(W\),
then the whole rooted endpoint fan has the exact history polynomial

\[
 \boxed{Q_p(t)=tU_{k,k}(t).}                            \tag{1}
\]

Thus this is a genuinely history-valued family of quasipolynomial size; it
is not the polynomial collection of physical triples isolated in the first
fan theorem.

Suppose one tries to route \(nQ_p(1/2)\) units of weighted rooted-history
demand into **all** complementary homogeneous face banks (all cups and all
caps), with capacity \(\Lambda\) per output face.  The full Hall cut forces

\[
 \boxed{
 \Lambda\ge
 \frac{nU_{k,k}(1/2)}{4U_{k,k}(1)}
 \ge\frac{\sqrt m}{8\sqrt{2k-3}}
 =m^{1/2-o(1)},}                                      \tag{2}
\]

where

\[
 m=|E(k,k)|=\binom{2k-4}{k-2},\qquad n=m+1.            \tag{3}
\]

The first bound even allows pooling the two signs and ignores their overlap,
so it applies a fortiori to any decoder using subfaces of the deleted
history, maximum homogeneous extensions, Ramsey/same-type subsets, or the
union of all such homogeneous banks.  No \(n^{o(1)}\)-load lift exists on
this interface.

The obstruction is sharply delimited.  The complementary configuration has
an enormous family of **mixed** cap--cup faces from its separated recursive
composition.  Their cardinality easily passes the full Hall cut.  What is
missing is a local history-retaining coupling from a rooted cup to those
mixed faces.  The existing two-tangent amalgamation theorem already gives
the generated mixed banks globally bounded rank load; it does not force
enough compatible opposite-side history from a coherent one-sided fan.  In
other words, the dense branch cannot be paid by one sign at a time; a
successful theorem must prove the missing local two-sign profile
contraction.

This is not a counterexample to \(H=n^{o(1)}\), and it does not refute a
mixed-face Hall decoder.  It is an exact stretchable barrier to the entire
homogeneous/subface decoder class.

## 1. The exact history lift

Let \(W=(w_1<\cdots<w_m)\) be x-ordered and let \(p<w_1\) satisfy

\[
 \chi(p,w_i,w_j)=+\qquad(i<j).                         \tag{4}
\]

For a nonempty subset

\[
 S=\{w_{i_1}<\cdots<w_{i_r}\},                         \tag{5}
\]

the path

\[
 p,w_{i_1},\ldots,w_{i_r}                              \tag{6}
\]

is forward temporal if and only if every consecutive triple of \(S\) has
positive sign, which is exactly the assertion that \(S\) is a cup.  No
reverse path from \(p\) with two or more edges exists, because its first
packet comparison has the wrong sign.  Pairing (6) with the direct reverse
edge gives a convex face \(\{p\}\cup S\), and every rooted face arises this
way.  Therefore deletion of \(p\) is a rank-preserving bijection

\[
 \{\text{rooted temporal histories/faces containing }p\}
 \longleftrightarrow
 \{\text{nonempty cups in }W\}.                        \tag{7}
\]

The extra root contributes one activity factor, proving (1).  If the
coherent sign is negative, the identical statement holds with caps and the
reverse temporal direction.

Equation (7) also explains why the physical triple promotion is too small.
Its rooted four-faces are only the rank-three coefficient of
\(U_{k,k}\); all higher cup histories are present and must be retained.

## 2. A general weighted Hall cut

Let \(\mathcal H\) be any finite history family with weights \(w(H)\), and
let \(\mathcal O\) be a proposed ordinary-face output family.  A fractional
decoder of demand multiplier \(D\) assigns nonnegative flow from histories
to permitted outputs so that history \(H\) emits total flow \(Dw(H)\), while
each output receives at most \(\Lambda\).

> **Lemma 1 (full-set Hall obstruction).**  Every such decoder satisfies
> \[
>  \boxed{\Lambda|\mathcal O|
>       \ge D\sum_{H\in\mathcal H}w(H).}                \tag{8}
> \]

**Proof.**  Sum the emitted flow over histories and the received flow over
outputs.  They are equal.  The output capacities bound the latter by
\(\Lambda|\mathcal O|\).  \(\square\)

This is only the full Hall cut; smaller history subfamilies can force a
larger load.  Hence failure of (8) is a definitive obstruction independent
of how cleverly individual histories choose outputs.

For the rooted fan, take \(D=n\), history weight
\(w(\{p\}\cup S)=2^{-(|S|+1)}\), and allow as outputs every cup and every cap
in \(W\).  The construction \(E(k,k)\) is sign-symmetric, so the number of
outputs is at most \(2U_{k,k}(1)\); ignoring the nonempty intersection of
the two families only increases the available capacity.  Equations (1) and
(8) give

\[
 \Lambda\ge
 \frac{n\,U_{k,k}(1/2)/2}{2U_{k,k}(1)}
 =\frac{nU_{k,k}(1/2)}{4U_{k,k}(1)}.                  \tag{9}
\]

Any bank formed from subfaces of one deleted cup history is contained in
the cup family, and any maximum cup/cap extension still contributes only
homogeneous outputs.  Thus (9) covers all of these variants simultaneously,
including arbitrary overlap-aware fractional routing.

## 3. Fixed-power load on the Erdős--Szekeres family

The set \(E(k,k)\) has no \(k\)-cup and no \(k\)-cap.  Every monomial of
\(U_{k,k}\) therefore has degree at most \(k-1\), and hence

\[
 U_{k,k}(1/2)\ge2^{-(k-1)}U_{k,k}(1).                  \tag{10}
\]

Substituting (10) into (9) gives

\[
 \Lambda\ge\frac{m+1}{2^{k+1}}.                       \tag{11}
\]

Since the central binomial coefficient is at least the average binomial
coefficient,

\[
 m=\binom{2k-4}{k-2}
 \ge\frac{2^{2k-4}}{2k-3}.                             \tag{12}
\]

Equivalently,

\[
 2^k\le4\sqrt{(2k-3)m}.                                \tag{13}
\]

Equations (11)--(13) prove the second inequality in (2).  Since
\(k=\Theta(\log m)\), the required load is
\(m^{1/2-o(1)}\), far above the permitted \(m^{o(1)}\).

The history family is itself at the live quasipolynomial scale.  Under a
high-left/low-right separated composition \(P=A\prec B\), the nonempty cup,
cap, and ordinary-face polynomials obey

\[
\begin{aligned}
 C_P(t)&=C_A(t)(1+|B|t)+C_B(t),\\
 U_P(t)&=U_A(t)+U_B(t)(1+|A|t),\\
 V_P(t)&=V_A(t)+V_B(t)+C_A(t)U_B(t).                  \tag{14}
\end{aligned}
\]

Iterating the second recurrence on \(E(k,k)\) gives

\[
 \log U_{k,k}(1/2)=\Theta(k^2)
 \quad\text{and}\quad
 \log U_{k,k}(1)=\Theta(k^2)=\Theta((\log m)^2).       \tag{15}
\]

Here is a direct bound, included to separate this statement from the
physical-incidence count.  Since every cup has rank at most \(k-1\),

\[
 U_{k,k}(1)\le \sum_{j=1}^{k-1}\binom mj\le k m^{k-1},
                                                               \tag{16}
\]

which gives the upper half of (15) for both activities.  In the recurrence
for \(U_{r,k}\), retain only the second summand while \(r\) runs from \(3\)
to \(k\).  Since

\[
 |E(r,k-1)|=\binom{r+k-5}{r-2},
\]

this gives

\[
 U_{k,k}(1/2)
 \ge \frac12\prod_{r=3}^{k}
       \left(1+\frac12\binom{r+k-5}{r-2}\right)
 =\exp(\Omega(k^2)).                                  \tag{17}
\]

Indeed, for the final \(\lfloor k/2\rfloor\) factors the binomial
coefficient is \(\exp(\Omega(k))\).  Thus (2) concerns the full
high-entropy temporal history reservoir, not \(O(m^4)\) physical
incidences.

## 4. Where sufficient capacity actually lives

The last recurrence in (14) contains the mixed bank

\[
 \mathcal C(A)\times\mathcal U(B).                     \tag{18}
\]

Every pair in (16) has a convex union, and the top separated split recovers
the two factors.  These mixed faces make \(V_{k,k}(1)\) vastly larger than
the union of all homogeneous faces.  For example:

\[
\begin{array}{c|r|r|r|r}
k&m&U(1)/U(1/2)&\text{homogeneous Hall load}&V(1)/U(1)\\ \hline
6&70&17.9071&0.9912&178.096\\
8&924&85.2731&2.7119&8.4227\cdot10^6\\
10&12870&374.7917&8.5854&3.0107\cdot10^{14}\\
12&184756&1585.2403&29.1371&9.3287\cdot10^{24}
\end{array}                                             \tag{19}
\]

Here “homogeneous Hall load” is the exact full-cut lower bound in (9), not
the coarser estimate (2).  The first two small rows can lie below one; the
fixed-power obstruction is asymptotic.

If arbitrary mixed faces are admitted merely as an unstructured output
alphabet, the full Hall cut has enormous slack.  But a decoder must retain
the input rooted history.  A mixed output consists of a cap in one recursive
child and a cup in the other; a general rooted cup can cross those children
and does not canonically specify a compatible cap partner while retaining
all its labels.  Capacity alone is not a geometric map.

This conclusion is consistent with
`agent_one_sided_reflection/ROOTED_DIAGONAL_AMALGAMATION.md`.  Its exact
two-tangent theorem proves that, once compatible rooted histories on both
sides of a trace have been generated, their mixed unions have aggregate
load at most the output rank.  It leaves precisely a local quantitative
profile-contraction alternative: either enough opposite-side histories are
present, or one detached side complex must pay.  The coherent-root
construction supplies only one of those profiles, and (2) rules out
replacing the missing profile by homogeneous deletion/extension alone.

The exact surviving theorem is therefore:

> force or charge compatible opposite-sign weighted histories for the
> two-tangent mixed banks across the separated/trace hierarchy, while
> retaining a decoder for the original coherent-root history.

This is the local forcing input needed by the already exact two-tangent
amalgamation theorem.  The homogeneous rooted-fan theorem cannot supply it.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_coxeter_global_half/verify_weighted_history_hall_barrier.py
```

The checker evaluates the three polynomial recurrences in (14) with exact
rational arithmetic through \(k=20\), verifies (2) and (9)--(13) on every
row, and checks the displayed values.  For \(k\le6\), it constructs the
exact rational point sets, applies a sign-preserving generic perturbation,
adds the coherent root, reconstructs the adjacent-swap reduced word, and
checks the matrix identity (1) at activities one and one-half.  It also
enumerates all cup histories for the small rows against the recurrence.
