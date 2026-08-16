# Common-core completions: private petals, convex union, or deletion forest

**Date:** 2026-08-15. All logarithms are base two. This continues
**FIXED_RANK_BOOLEAN_SOURCE_MIDSHADOW_GATE.md**.

## Verdict

Fix the high-middle-codegree output \(F\). The remaining carrier family has
the form

\[
                         Q=F\mathbin{\dot\cup}R_Q,
             \qquad |Q|=q.                               \tag{1}
\]

There are two exact square-root exits.

1. A weighted positive-mass subfamily with private completion labels has a
   load-one Boolean bank and gains \(\Theta(\sqrt q)\).
2. If the union support of a subfamily is four-covered by its carriers,
   planar four-locality makes that entire union convex; rank-safe source
   normalization again gains \(\Theta(\sqrt q)\).

If neither exit is used, an uncovered bad four-set supplies a deletion
branch of arity at most four. Iterating gives a finite carrier forest whose
leaves all have convex union support. The only remaining global loss is the
overlap of the Boolean banks of distinct leaves. This is a sharper endpoint
than raw high carrier codegree: either a private first-difference decodes
the carrier, or all ambiguity has been moved into a bounded-arity
support-deletion chronology.

The theorem does not yet close that leaf overlap. The branch labels are
absent from surviving carriers, so they cannot simply be adjoined as an
ordinary output tag. A mask-aware rooted/profile return is still required.

## 1. Weighted setup

Let \(\mathcal Q\) be distinct ordinary rank-\(q\) carriers sharing the
ordinary core \(F\). Records below \(Q\) use actual rank-\(r\) source faces
\(A\subseteq Q\), with weights satisfying

\[
              \sum_{\omega:\,A_\omega=A}w_\omega\le1.    \tag{2}
\]

Write \(M_Q\) for the total record weight below \(Q\), and
\(M_{\mathcal S}=\sum_{Q\in\mathcal S}M_Q\). Then

\[
                         M_Q\le {q\choose r}.             \tag{3}
\]

All results below include arbitrary coalesced histories in \(M_Q\).

## 2. Private-petal return

Call \(\mathcal P\subseteq\mathcal Q\) privately tagged if there are labels

\[
                  x_Q\in R_Q\setminus
                       \bigcup_{Q'\in\mathcal P\setminus\{Q\}}R_{Q'}
                       \quad(Q\in\mathcal P).             \tag{4}
\]

For each \(Q\in\mathcal P\), take the ordinary bank

\[
                         \mathcal B_Q
              =\{S\subseteq Q:x_Q\in S\}.                \tag{5}
\]

It has size \(2^{q-1}\). The banks are pairwise disjoint: an output from
\(\mathcal B_Q\) contains \(x_Q\), while \(x_Q\) is absent from every other
carrier in the selected family. Therefore

\[
 \begin{aligned}
 V&\ge|\mathcal P|\,2^{q-1}\\
  &\ge M_{\mathcal P}{2^{q-1}\over{q\choose r}}
   \ge M_{\mathcal P}\sqrt{\pi q/8}.                     \tag{6}
 \end{aligned}
\]

The last inequality is Wallis' central-binomial bound. Since
\(\vartheta=2-\log_2 3<1/2\), any
\(M_{\mathcal P}\ge W/q^{1/2-\vartheta-o(1)}\) supplies the required
\(Wq^\vartheta\) scale. In particular, a positive-mass private sunflower
petal branch closes with room.

## 3. Four-cover union lift

For \(\mathcal S\subseteq\mathcal Q\), put

\[
                   U_{\mathcal S}=\bigcup_{Q\in\mathcal S}Q.           \tag{7}
\]

Suppose every four-subset of \(U_{\mathcal S}\) is contained in at least
one \(Q\in\mathcal S\). Every such four-set is ordinary by heredity.
Planar Carathéodory, equivalently four-locality of convex position, gives

\[
                         U_{\mathcal S}\text{ is ordinary}.           \tag{8}
\]

Thus all \(2^{|U_{\mathcal S}|}\) subsets form an ordinary Boolean bank.
Every actual source below the subfamily is a rank-\(r\) subset of the one
physical support \(U_{\mathcal S}\), so (2) gives

\[
 M_{\mathcal S}\le {|U_{\mathcal S}|\choose r}.
                                                                    \tag{9}
\]

Consequently

\[
 V\ge2^{|U_{\mathcal S}|}
   \ge M_{\mathcal S}\sqrt{\pi|U_{\mathcal S}|/2}
   \ge M_{\mathcal S}\sqrt{\pi q/2}.                    \tag{10}
\]

This argument uses global source normalization across all carriers; the
crude per-carrier bound \(|\mathcal S|\binom qr\) would miss the union
lift.

## 4. The uncovered-circuit deletion branch

If (8) fails, choose canonically a nonordinary four-set
\(C\subseteq U_{\mathcal S}\). Since every carrier \(Q\) is ordinary,
\(C\nsubseteq Q\) for every \(Q\in\mathcal S\). Moreover \(F\subseteq Q\)
for every carrier, so the nonempty trace

\[
                         Z=C\setminus F,\qquad1\le|Z|\le4              \tag{11}
\]

meets \(U_{\mathcal S}\setminus Q\) for every \(Q\). In weighted form,

\[
 \sum_{z\in Z}\ \sum_{\substack{Q\in\mathcal S\\z\notin Q}}M_Q
                         \ge M_{\mathcal S}.             \tag{12}
\]

Hence one label \(z\in Z\) is omitted by carriers of total mass at least
\(M_{\mathcal S}/4\). More usefully, assign every carrier to its first
omitted label in the canonical order on \(Z\). This partitions the entire
node mass into at most four children, and the union support in each child
strictly loses its branch label.

Iterate. Along a branch the union support strictly decreases while every
carrier keeps rank \(q\), so the depth is at most
\(|U_{\mathcal S}|-q\). A terminal node is necessarily four-covered:
otherwise (11)--(12) make another strict deletion. Thus every leaf has the
convex-union bank (10), and the record masses of the leaves sum exactly to
the root mass.

Let \(\Lambda_{\rm leaf}\) be the maximum number of terminal Boolean banks
containing one ordinary output, with weighted leaf multiplicity if the
forest is fractionally split. Summing (10) gives the exact conditional
return

\[
                         V\ge
          {M_{\mathcal S}\over\Lambda_{\rm leaf}}
                         \sqrt{\pi q/2}.                 \tag{13}
\]

Low leaf overlap closes. High leaf overlap fixes one physical ordinary
face shared by many distinct convex terminal supports. The branch words
themselves do not decode those supports, because every branch label was
deleted. This is the precise next rooted-history interface.

## 5. Verification

**verify_common_core_completion_private_petal.py** checks the private-bank
decoder, a five-deletion four-cover family whose union is forced ordinary,
the uncovered-four-set weighted split, and all incidence identities using
exact rational weights.

