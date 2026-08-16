# Fixed-anchor relocation: exact cancellation and the self-minimal-cell gate

**Date:** 2026-08-15. All logarithms are base two and all face counts are
nonempty.

## Verdict

The one-bit relocation theorem repairs every common-ear extension fibre, but
it does not turn the minimizer endpoint surplus into a new one-face
converter. The obstruction is exact.

Let \(P=Q\cup X\), where \(X\) is a set of \(k\) physical anchors, and
arbitrarily re-embed only \(X\), obtaining \(P'=Q\cup X'\). Every ordinary
output \(F'\) of \(P'\) has the canonical code

\[
                         (F'\cap Q,F'\cap X'),                    \tag{1}
\]

where \(F'\cap Q\) is already an ordinary face of the unchanged base
\(Q\), and the second coordinate has only \(2^k\) values. Thus a decoder of
load \(\Lambda\) into relocated ordinary faces can serve at most

\[
                     \Lambda\,2^k\{V(Q)+1\}                     \tag{2}
\]

records. The comparison back to the original configuration loses exactly
the same factor \(2^k\). Relocation therefore contributes no net capacity
beyond a \(k\)-bit external tag.

There is also a geometric impossibility. If an output after relocation is
required to retain two variable supports \(A,B\subseteq Q\), then

\[
                   A\cup B\subseteq F'\cap Q
       \quad\Longrightarrow\quad A\cup B\text{ is ordinary in }Q. \tag{3}
\]

Consequently fixed anchors cannot repair a genuinely bad cap--cup support
union. They can only decorate a base face which existed before the mutation.

This kills the most literal fixed-anchor reset. In the balanced two-block
Pascal wrapper, spanning endpoint records carry two variable physical
anchors \(y,z\). Fixing or relocating \(k\) anchors on each side reaches at
most

\[
             { (2R+k)^2\over N^2}                                \tag{4}
\]

of the record rectangle when every child cap and cup has rank at most
\(R\). For \(R,k=O(\log N)\), this is \(N^{-2+o(1)}\), far below the
inverse-polylogarithmic density required by the endpoint reset. The family
is rational, stretchable, rank \(O(\log N)\), and scalable at coefficient
one half. It is not a global minimizer; this distinction is essential.

Global minimizers do satisfy a stronger exact statement than the deletion
first moment. If \(Q=P-x\), the actual point \(x\) occupies a **global
minimum cell** of the complete pair-line arrangement of \(Q\): among every
possible one-point extension position \(y\), it minimizes the number of
faces containing that point. Across every adjacent wall it therefore hides
the larger exposed-edge star. This self-minimal-cell theorem subsumes both
singleton cap/cup inequalities, but its sign is anti-converting. No current
argument turns the collection of pointwise minimum cells, whose arrangements
depend on \(x\), into a common two-anchor decoder.

The surviving minimizer-specific question is no longer whether a few
anchors are cheap to move. It is whether self-minimality forces an
inverse-polylogarithmic family of **already ordinary base-support unions**,
or a decreasing multi-point mutation whose decrease is not canceled by
other extension faces.

## 1. Anchor erasure and exact capacity

Let \(Q\) be any planar general-position set. Let \(X\) and \(X'\) be two
labelled \(k\)-point sets such that \(Q\cup X\) and \(Q\cup X'\) are in
general position; the points of \(Q\) are unchanged. Heredity gives

\[
 F'\in\mathcal F(Q\cup X')
       \quad\Longrightarrow\quad F'\cap Q\in\mathcal F(Q).       \tag{5}
\]

> **Theorem 1 (fixed-anchor cancellation).** Let \(\Omega\) be any record
> family, and suppose a map sends every \(\omega\in\Omega\) to an ordinary
> output \(F'_\omega\in\mathcal F(Q\cup X')\) plus one of \(T\) external
> tags. If the complete output has decoder load at most \(\Lambda\), then
> \[
>            |\Omega|\le T\Lambda\,2^k\{V(Q)+1\}.                 \tag{6}
> \]
> Moreover,
> \[
> V(Q\cup X')+1\le2^k\{V(Q)+1\}
>                    \le2^k\{V(Q\cup X)+1\}.                     \tag{7}
> \]

**Proof.** The map (1) injects the output alphabet into

\[
                 \overline{\mathcal F}(Q)\times2^{X'},           \tag{8}
\]

where \(\overline{\mathcal F}(Q)\) includes the empty face. This has size
\(2^k\{V(Q)+1\}\). Multiplying by the tag and decoder loads proves (6).
Summing (5), including the empty output, over all anchor masks proves (7).
\(\square\)

Equation (6) remains true for adaptive, fractional, or first-divergence
routing after replacing \(\Lambda\) by the maximum normalized load. It is
pure output capacity and does not assume that the re-embedding was reached
through adjacent flips.

Suppose a record is a pair \((A,B)\) of variable supports in \(Q\), and a
proposed output literally retains both. Then (5) proves (3). More generally,
if the output does not retain them, all information used to recover the pair
is contained in the pre-existing base face \(F'\cap Q\), its \(k\)-bit
anchor mask, and the external tag. The relocation creates no additional
decoder state.

## 2. Why a common ear alone gives no surplus

Let \(\mathcal A\subseteq\mathcal F(Q)\) be a family sharing a common
exposed edge. The common-ear lemma in
`GAP_BUDGETED_REPAIR_ALPHABET_MUTATION_GATE.md` gives a position \(x'\)
such that

\[
                         A\cup\{x'\}\in\mathcal F(Q+x')
                         \qquad(A\in\mathcal A).                  \tag{9}
\]

The outputs in (9) injectively recover \(A\). After the augmented one-bit
relocation comparison this gives

\[
                         V(Q+x)+1\ge {|\mathcal A|\over2}.         \tag{10}
\]

But every \(A\in\mathcal A\) was already an ordinary face of \(Q\subseteq
Q+x\), so heredity gives the stronger bound \(V(Q+x)\ge|\mathcal A|\)
without moving anything. The repaired anchor extension is useful only if it
participates in a further same-chart product. Theorem 1 says that such a
product must already be encoded by ordinary base faces, up to the anchor
mask.

This is precisely what fails for a bad cap--cup pair: by heredity, adding
external anchors cannot make \(A\cup B\) ordinary when it was not ordinary
in \(Q\).

## 3. The two-block anchor-entropy regression

Let \(Q_L,Q_R\) be rational copies of an \(N\)-point configuration \(Q\),
placed in a genuine vertical strong glue \(P=Q_L\prec Q_R\). Let
\(\mathcal C(Q)\) and \(\mathcal U(Q)\) be its cap and cup complexes, of
sizes \(C,U\). The spanning endpoint records are

\[
 \begin{aligned}
  K(A,z)&=A\cup\{z\}, &&A\in\mathcal C(Q_L),\ z\in Q_R,\\
  L(y,B)&=\{y\}\cup B, &&y\in Q_L,\ B\in\mathcal U(Q_R).
 \end{aligned}                                                    \tag{11}
\]

There are \(NC\) records of the first kind and \(NU\) of the second. The
strong-glue classification gives the exact equivalence

\[
 K(A,z)\cup L(y,B)\text{ ordinary}
 \quad\Longleftrightarrow\quad
 A\cup\{y\}\text{ is a cap and }B\cup\{z\}\text{ is a cup}.    \tag{12}
\]

Let \(E_C\) and \(E_U\) be the numbers of addable cap-anchor and cup-anchor
incidences. The exact endpoint moment identity gives

\[
       E_C=2\sum_{A\in\mathcal C(Q)}|A|-N,\qquad
       E_U=2\sum_{B\in\mathcal U(Q)}|B|-N.                        \tag{13}
\]

If the maximum cap and cup ranks are at most \(R\), then

\[
                              E_C\le2RC,\qquad E_U\le2RU.          \tag{14}
\]

Now re-embed anchor sets \(Y\subseteq Q_L\), \(Z\subseteq Q_R\), with
\(|Y|=k_L\), \(|Z|=k_R\), while leaving every other physical label fixed.
A record pair not using \(Y\cup Z\) has exactly its old status. Even granting
that every record using a moved anchor becomes good, the number of original
record pairs which can be good after the mutation is at most

\[
                  (E_C+k_LC)(E_U+k_RU).                           \tag{15}
\]

> **Theorem 2 (fixed-anchor density ceiling).** The proportion of the full
> \(N^2CU\) spanning rectangle reached by a \((k_L,k_R)\)-anchor mutation is
> at most
> \[
>       { (2R+k_L)(2R+k_R)\over N^2}.                             \tag{16}
> \]

This is deliberately generous: it assumes every moved-anchor incidence is
repairable and ignores the \(k_L+k_R\)-bit relocation loss. Thus even the
best such mutation has density \(N^{-2+o(1)}\) when
\(R,k_L,k_R=N^{o(1)}\).

Take the balanced rational Pascal iterates \(Q_{d}\) used in
`POLYLOG_CAP_CUP_CONVERTER_MUTATION_GATE.md`. They have rank
\(R=O(\log N)\), \(C(Q_d)=U(Q_d)\), and face coefficient tending to one
half. Their genuine wrappers \(Q_d\prec Q_d\) satisfy (11)--(16) at every
finite stage. Hence this is a scalable stretchable obstruction to obtaining
inverse-polylogarithmic density by pigeonholing and moving \(O(\log N)\)
physical anchors.

The family is not claimed to be globally \(V\)-minimal. Indeed the finite
twelve-point wrapper in the verifier is rejected by singleton minimality.
The regression kills the fixed-anchor mechanism; it does not kill an
argument using the full self-minimal-cell condition below.

## 4. Self-minimal one-point extension cells

Fix \(Q\) and let \(c\) be a chamber of its complete pair-line arrangement.
For any point \(y\in c\), define

\[
 L_Q(c)=|\{F\in\mathcal F(Q+y):y\in F\}|.                         \tag{17}
\]

This is well defined because the order type of \(Q+y\) is constant in a
chamber. If \(P\) is globally minimal among all general-position
\(n\)-point configurations, put \(Q=P-x\) and let \(c_x\) be the chamber
containing \(x\).

> **Theorem 3 (self-minimal extension cell).** For every physical label
> \(x\),
> \[
>                       L_{P-x}(c_x)=\min_c L_{P-x}(c).             \tag{18}
> \]
> If a wall \(ab\) bounds \(c_x\), and \(E^{\rm in}_{ab}\) and
> \(E^{\rm out}_{ab}\) are the two exposed-edge stars oriented as in the
> single-flip derivative, then
> \[
>                            E^{\rm hidden}_{ab}
>                              \ge E^{\rm visible}_{ab}.           \tag{19}
> \]

**Proof.** Moving \(x\) to any other chamber gives another realizable
general-position \(n\)-point configuration, while the faces omitting \(x\)
remain exactly \(\mathcal F(P-x)\). Global minimality therefore compares
only the extension terms and proves (18). Applying the exact adjacent-wall
derivative to a neighboring chamber gives (19). \(\square\)

Choosing the two far strong-glue cells in (18) recovers

\[
 L_{P-x}(c_x)\le1+C(P-x),\qquad
 L_{P-x}(c_x)\le1+U(P-x),                                      \tag{20}
\]

the singleton endpoint inequalities. Thus (18) is genuinely stronger than
the deletion first moment: it includes every chamber, not only the two
endpoint cells.

Its sign is the same anti-alignment as local mutation minimality. The actual
cell minimizes ordinary extensions, so a chamber which repairs a large
wrong-extension fibre is allowed, and expected, to have more faces. Also,
the arrangement in (18) is \(\mathcal A(P-x)\); it changes with \(x\).
Pigeonholing physical anchors does not create a common chamber or a common
base arrangement for two labels.

## 5. Exact remaining minimizer input

The fixed-anchor route can succeed only with an ingredient not canceled by
Theorem 1. Equivalent possibilities are:

1. an inverse-polylogarithmic family of cap--cup pairs whose variable base
   union is already ordinary and whose anchor masks give a bounded decoder;
2. a multi-point re-embedding which decreases the total extension count,
   using an interaction not visible in the separate minima (18); or
3. a circuit-elimination theorem converting incompatible minimum-cell wall
   stars into an ordinary base face which retains information from both
   variable supports.

Merely fixing one or two wrong-extension anchors, moving them to universal
ear/far cells, and invoking the one-bit theorem cannot supply the desired
endpoint multiplier.

## 6. Verification

The verifier `verify_fixed_anchor_relocation_cancellation_gate.py` uses
exact rational coordinates. It checks the anchor-erasure rank inequalities
on several relocations, exhausts the twelve-point
\(T(4,2)\prec T(4,2)\) wrapper, verifies (12)--(16), and confirms that with
no moved anchors the exact good spanning count is \(126^2=15876\). It also
checks the true five-point minimizer of
`MINIMIZER_SINGLETON_ENDPOINT_SURPLUS_GATE.md`, whose \(26\) faces attain
the universal five-point minimum, and verifies its pointwise extension
counts.
