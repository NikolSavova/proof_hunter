# Stable cross-circuit tournament core

**Date:** 2026-08-15. All logarithms are base two. This note sharpens the
dense residue in `PLANAR_CROSS_CLASS_PRODUCT_AND_CAGE_ELIMINATION.md`.

## Verdict

In a fixed-gap least counterexample, a vertex cover of the cross-bad-four
hypergraph between two near-ambient classes must contain almost an entire
class. Orienting each class pair toward such an almost-covered side produces
a tournament. One class then has a near-full physical core which is covered
by disjoint bad-circuit matchings against half of all other classes.

After retaining only `k=Theta(loglog n)` partner classes, a polynomial-loss
pigeonhole makes the circuit occupancy/hidden-point type identical across
the whole rectangular incidence array. Thus the remaining long-run gate is
not scarcity of circuits: it is coherence of the sibling matchings when
their central labels are independently recombined.

## 1. Stable cover theorem

Put

\[
 L=\log n,\qquad L_2=\log L,\qquad
 \Phi_3(L)={1\over2}L^2-3LL_2,
\]

and use the campaign-safe bound

\[
 \log f(s)\ge\psi(\log s),\qquad
 \psi(x)={1\over4}x^2-{1\over2}x.                    \tag{1}
\]

Let `Y,Z` be disjoint planar point classes, and let `Gamma(Y,Z)` consist
of the nonconvex four-sets meeting both classes.

> **Theorem 1 (almost-one-side cover).** Suppose
> `V(P)<2^{Phi_3(L)}`. If `K` meets every member of `Gamma(Y,Z)`, then,
> for all sufficiently large `n`,
> \[
>       \min\{|Y\setminus K|,|Z\setminus K|\}
>          < h:={n\over L^{5/2}}.                    \tag{2}
> \]

**Proof.** If both residual classes have at least `h` labels, their
arbitrary internal faces multiply by planar four-locality. Hence

\[
 \begin{aligned}
  \log V(P)&\ge2\psi(\log h)\\
   &={1\over2}L^2-{5\over2}LL_2+{25\over8}L_2^2
       -L+{5\over2}L_2\\
   &=\Phi_3(L)+{1\over2}LL_2-L+{25\over8}L_2^2
       +{5\over2}L_2>\Phi_3(L),
 \end{aligned}                                      \tag{3}
\]

a contradiction. \(\square\)

If `|Y|,|Z|>=g`, Theorem 1 says every cover contains at least `g-h`
labels of one side. In the live application

\[
             g={n\over\Theta(LL_2)},\qquad {h\over g}=o(1).   \tag{4}
\]

## 2. Tournament and common physical core

Let `Y_1,...,Y_t` be classes of size at least `g`. For each pair choose a
maximal matching `M_ij` in its cross-bad-four hypergraph. The vertices of a
maximal matching form a cover. Orient `i -> j` when `V(M_ij)` contains at
least `g-h` labels of `Y_i`; Theorem 1 ensures that at least one direction
is available, and ties are arbitrary.

> **Theorem 2 (common matched core).** Some class `Y_0` has a set `J` of
> at least `(t-1)/2` out-neighbours and a core
> \[
>        Y^*=Y_0\cap\bigcap_{j\in J}V(M_{0j}),\qquad
>        |Y^*|\ge g-|J|h.                             \tag{5}
> \]
> For every `y in Y*` and `j in J`, there is a unique matching circuit
> `E_j(y) in M_0j` containing `y`; for fixed `j` these circuits are
> pairwise label-disjoint as `y` varies.

**Proof.** A tournament has a vertex of outdegree at least `(t-1)/2`.
The union bound gives (5). Uniqueness and disjointness are the definition
of a matching. \(\square\)

For `t=Theta(L)` and (4), `|J|h/g=O(L_2/sqrt L)=o(1)`.

## 3. A uniform signed circuit array at polynomial loss

For every incidence `(y,j)`, record a circuit type `chi(y,j)` consisting
of the class occupancy, the hidden-point class, and whether `y` is the
hidden point. There are at most `R=12` types.

> **Theorem 3 (uniform partner subarray).** If
> `k<=|J|/(2R)`, there are `I subset J`, `|I|=k`, one type `chi_0`, and
> `Y' subset Y*` such that
> \[
>    \chi(y,j)=\chi_0\quad(y\in Y',j\in I),\qquad
>    |Y'|\ge {|Y^*|\over R(2R)^k}.                    \tag{6}
> \]

**Proof.** For each `y`, one type occurs on at least `|J|/R` partners,
so `y` contributes at least `binom(floor(|J|/R),k)` pairs `(chi,I)`.
There are at most `R binom(|J|,k)` possible pairs. Averaging and

\[
 {\binom{\lfloor |J|/R\rfloor}{k}\over\binom{|J|}{k}}
       \ge(2R)^{-k}                                  \tag{7}
\]

give (6). \(\square\)

Taking `k=Theta(L_2)` costs only `L^{O(1)}` labels, so `Y'` remains
`n^{1-o(1)}`. We obtain `k` synchronized, label-disjoint physical circuit
matchings of one signed type, each indexed by the same large central core.

This theorem does **not** make the sibling indices independent. A diagonal
array may have no selected cross-combinations. The exact remaining planar
operation is therefore one of:

1. a first-incoherent-sibling bank that stores two independently chosen
   central indices in an ordinary face;
2. circuit elimination producing a fixed-edge/common-pocket product; or
3. a proof that the rich internal face bank of `Y_0` intersects enough of
   these matching traces to pay the required multiplier.

