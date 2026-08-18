# The support-adaptive rich-fibre gate

## 1. Exact selector-free factorization of the rich tail

Keep the notation of `SUPPORT_ADAPTIVE_POPULAR_OVERLAP_GATE.md`:

\[
 D=A-A,\quad N=|D|,\quad S=|D+D|,\quad K=S/N,
\]

and

\[
 \mathcal P_K=\{q\ne0:R_D(q)>K,\ R_D(Jq)>K\}.
\]

For `u in D` and `s in D+D`, define

\[
 \begin{split}
 Q_K(u,s)=\{q\in\mathcal P_K:\;&u+q\in D,\\
 &s-u-q\in D,\\
 &s-u-(I+J)q\in D\},
 \end{split}                                      \tag{1.1}
\]

and put `g_K(u,s)=|Q_K(u,s)|`.  Then the adaptive rich tail has the exact
factorization

\[
 \boxed{
 \sum_{q\in\mathcal P_K}R_D(q)R_D(Jq)
 =\sum_{u\in D}\sum_{s\in D+D}g_K(u,s).}          \tag{1.2}
\]

To prove this, choose `u,u+q in D` and `v,v+Jq in D`, and set

\[
 s=(u+q)+(v+Jq).
\]

Then

\[
 v+Jq=s-u-q,
 \qquad
 v=s-u-(I+J)q,                                   \tag{1.3}
\]

so `q in Q_K(u,s)`.  Conversely (1.1) recovers `v` from (1.3), giving a
bijection.

There are at most `NS` labels `(u,s)`.  Hence either one of

\[
 \max_{u,s}g_K(u,s)le N^{o(1)}                  \tag{1.4}
\]

or

\[
 \sum_{u,s}g_K(u,s)^2\le N^{1+o(1)}S            \tag{1.5}
\]

would prove the adaptive tail estimate and therefore resolve the cube-root
order in Erdős 1208.  The moment formulation (1.5) is weaker and should be
preferred if a pointwise obstruction appears.

## 2. The exact structure of one rich fibre

Fix a label `(u,s)`, let `Q=Q_K(u,s)`, and put `w=s-u`.  Formula (1.1)
gives three simultaneous affine copies inside the complete difference set:

\[
 u+Q\subseteq D,
 \qquad
 w-Q\subseteq D,
 \qquad
 w-(I+J)Q\subseteq D.                            \tag{2.1}
\]

It follows immediately that

\[
 Q-Q\subseteq(D-D)\cap(I+J)^{-1}(D-D).          \tag{2.2}
\]

This is already stronger than an arbitrary heavy switching fibre: every
element of `Q` is simultaneously a popular translation of `D` in its own
direction and in the quarter-turned direction.

There is also an elementary translate-amplification lemma.  Write

\[
 D_q=\{z\in D:z+q\in D\}.
\]

If `h=|Q|`, then some `z,e in D` and some `Q' subseteq Q` satisfy

\[
 |Q'|>{hK^2\over N^2}                            \tag{2.3}
\]

and

\[
 z+Q'\subseteq D,
 \qquad
 e+JQ'\subseteq D.                              \tag{2.4}
\]

Indeed

\[
 \sum_{q\in Q}|D_q||D_{Jq}|>hK^2.
\]

Expanding the left side and pigeonholing over the `N^2` pairs `(z,e)` proves
(2.3)--(2.4).  Together with (2.1), a large rich fibre therefore creates
five prescribed affine images of one common set `Q'` inside `D`.

Because `D=A-A` is distance-Sidon, every one of these images has injective
squared norm up to its antipodal pair.  A proof of (1.4) or (1.5) must turn
the simultaneous affine-copy structure, the popularity lower bound, and
this radial constraint into either ordinary support growth or parallel-line
concentration.

## 3. Exact calibration

The verifier expands the rich tail into the labels from (1.2).  Its profiles
are

\[
\begin{array}{c|r|r|r|r}
\text{family}&\sum g_K&|\operatorname{supp}g_K|&\max g_K&\sum g_K^2\\ \hline
\text{closure }30&58,800&58,100&3&60,220\\
\text{closure }40&1,634,032&1,481,835&13&2,004,548\\
\text{radial side }8&89,528&18,069&18&645,476\\
\text{radial side }12&693,008&79,157&35&9,209,244
\end{array}                                      \tag{3.1}
\]

The complete-difference closure has average rich load close to one.  The
abstract radial transversals already have average loads `4.95` and `8.75`,
with second-moment-to-mass ratios `7.21` and `13.29`.  The previously
constructed maximum-fibre gadgets have empty adaptive tails because their
generic cross differences make `S` essentially maximal.

An independent algebraic stress test uses Welch Costas permutations followed
by the smallest integral shear/stretch which separates their Euclidean
lengths.  For sizes 10, 16, 22, and 30, the rich-fibre maxima are respectively
2, 2, 4, and 3; the second-moment-to-mass ratios are at most `1.158`.  Thus
the near-injectivity is not peculiar to the relation-closure construction.

This does not prove (1.4): the stored families are finite diagnostics.  It
does show that the support-adaptive restriction removes exactly the known
pointwise counterexamples, while the selector-free labels retain a strong
experimental separation between complete differences and radial impostors.

## 4. Literature audit of the inverse step

The standard additive-combinatorial machinery stops one step short of the
needed conclusion.

* Shkredov's *Energies and structure of additive sets*
  (<https://arxiv.org/abs/1405.3132>) develops Katz--Koester and popular-
  difference structure, including lower bounds for `|D+D_q|` and
  decompositions into small-doubling pieces.
* *On common energies and sumsets* and its sequel
  (<https://arxiv.org/abs/2408.08113>,
  <https://arxiv.org/abs/2502.20702>) give polynomial and subexponential
  criteria connecting common energy and small doubling.

These theorems are automorphism-blind: their conclusions retain an additive
model but not the simultaneous `q,Jq` popularity, the five affine copies in
(2.1)--(2.4), or the unique endpoint decoration of every nonzero element of
`D`.  The radial transversal counterexample has exactly the generic additive
statistics and violates the desired conclusion.  Thus a black-box
Balog--Szemeredi--Gowers or common-energy substitution cannot finish the
argument.  It can only supply the approximate additive model; a new
Euclidean stability lemma must then show that a sufficiently large model
supporting all five affine copies either lies in few parallel layers or
contains two non-antipodal vectors of the same norm.

Run `verify_support_adaptive_popular_overlap_gate.py` for (1.2) and the
profiles in (3.1).
