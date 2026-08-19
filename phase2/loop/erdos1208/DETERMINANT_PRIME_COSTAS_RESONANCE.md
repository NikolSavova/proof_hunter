# Determinant-prime affine resonance in distance-Sidon Costas arrays

## 1. Status

The generic-affine theorem shows that an arbitrary vector-Sidon set can be
made distance-Sidon while eliminating every nonzero simultaneous `q,Jq`
overlap.  That conclusion is deliberately nonuniform: a specially chosen
distance-separating affine map can retain exact quarter-turn resonance.

This note gives a rigorous localization theorem for the first such stress
family found in the search.  It first computes the resonance index for an
arbitrary integral matrix, then specializes to prime determinant.  Let `T`
be integral, let `A_0` be an integral point set, and put

\[
 A=T A_0,\qquad D=A-A.
\]

Every shift contributing to both `R_D(q)` and `R_D(Jq)` pulls back to one
line modulo `p`.  Consequently there are only `O(p)` jointly supported
shifts, even though `D-D` can have `Theta(p^2)` shifts.  Exact Welch--Costas
examples show that this codimension-one tail can have nontrivial
opposite-endpoint charge load after all Euclidean lengths have been
separated.  The size-biased load remains small in every checked example.

This is a new exact easy branch and a sharper adversary.  It is not the
cross-fibre theorem and does not resolve Erdős 1208.

## 2. The resonance lattice

Write

\[
 T=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
 \det T=p,
\]

and put

\[
 T^{\mathsf T}T=
 \begin{pmatrix}w&u\\u&v\end{pmatrix}.
\]

Direct multiplication gives

\[
 T^{-1}JT={1\over p}
 \begin{pmatrix}-u&-v\\w&u\end{pmatrix}
 =:{1\over p}B.                                      \tag{2.1}
\]

Moreover

\[
 \det B=wv-u^2=(\det T)^2=p^2.                       \tag{2.2}
\]

Assume that `(w,u,v)` is not identically zero modulo `p`.  Then `B mod p`
is a nonzero singular two-by-two matrix, hence has rank one.  The subgroup

\[
 \Gamma_T=\{z\in\mathbb Z^2:Bz=0\pmod p\}             \tag{2.3}
\]

therefore has index exactly `p` in `Z^2`.

There is an exact composite version.  For an arbitrary nonzero determinant
`Delta`, retain the definitions of `w,u,v,B` and put

\[
 g=\gcd(w,u,v),\qquad I_T={|\Delta|\over g}.          \tag{2.3a}
\]

Here `g` divides `|Delta|`: since `g^2` divides
`wv-u^2=Delta^2`, this follows prime by prime.  The Smith invariants of `B`
are `g` and `Delta^2/g`.  Reduction modulo `|Delta|` therefore gives

\[
 \boxed{[\mathbb Z^2:\Gamma_T]=I_T.}                \tag{2.3b}
\]

Thus `I_T` is the exact **quarter-turn resonance index** of `T Z^2`.  It is
one in the maximally resonant case and equals `|Delta|` when the Gram matrix
is primitive.

If `Gamma` is any index-`I` sublattice of `Z^2`, Hermite normal form gives

\[
 |\Gamma\cap[-M,M]^2|\ll {M^2\over I}+M+1.          \tag{2.3c}
\]

Indeed a basis `(a,0),(b,c)` has `ac=I`; there are `O(M/c+1)` choices for
the second coefficient and, for each, `O(M/a+1)` choices for the first.
This is the general lattice-counting form of the prime localization below.

### Proposition 2.1: codimension-one joint support

Let `D_0=A_0-A_0`.  If

\[
 R_D(q)R_D(Jq)>0,
\]

then there is a `z in (D_0-D_0) cap Gamma_T` with `q=Tz`.

### Proof

The first positive overlap implies `q in D-D=T(D_0-D_0)`, so write
`q=Tz`.  The second implies `Jq in D-D`, in particular `Jq in T Z^2`.
By (2.1), this is equivalent to `Bz/p in Z^2`, or `z in Gamma_T`.  The same
argument with `p` replaced by `|Delta|` proves the composite version.  QED.

If `A_0 subset [0,p)^2`, then

\[
 D_0-D_0\subset(-2p,2p)^2.                            \tag{2.4}
\]

Each residue vector modulo `p` has at most sixteen lifts in this box, while
the kernel line in (2.3) has exactly `p` residue vectors.  Hence

\[
 \boxed{
 \#\{q:R_D(q)R_D(Jq)>0\}\le16p.}                    \tag{2.5}
\]

The constant is intentionally crude.  The important fact is the power:
the orthogonal tail occupies a codimension-one resonance lattice.

The excluded case `w=u=v=0 mod p` is real, not a technicality.  It occurs
when `T` is a Gaussian multiplication of norm `p`; then the lattice is
quarter-turn invariant and the resonance index is one.  Such a conformal
map cannot repair repeated Euclidean distances already present in the base
array.

## 3. Exact distance-Sidon stress family

For a prime `p`, let

\[
 W_p=\{(i,g^i\bmod p):0\le i<p-1\},                  \tag{3.1}
\]

where `g` is the smallest primitive root modulo `p`.  This is a Welch Costas
array, so its nonzero directed differences are unique.  The raw array is
usually not distance-Sidon.  The matrices below have determinant `p`, and
the exact verifier checks that every transformed array `T W_p` is
distance-Sidon.

For each row, `N=|D|`, `S=|D+D|`, `jnt` is the number of shifts with
`R_D(q)R_D(Jq)>0`, and `ad` is the number surviving the support-adaptive
cutoff.  The final column is the adaptive diagonal tail
`sum_q R_D(q)R_D(Jq)` over those nonzero shifts.

\[
\begin{array}{c|c|r|r|r|r|r}
p&T&N&S&\mathrm{jnt}&\mathrm{ad}&\mathrm{tail}\\ \hline
11&(-3,2;2,-5)&91&707&37&20&8,200\\
13&(-3,7;-1,-2)&133&969&25&12&13,824\\
17&(-7,5;-2,-1)&241&2,299&53&24&56,184\\
19&(-5,-3;3,-2)&307&2,927&81&52&194,752\\
23&(-5,-2;-1,-5)&463&4,513&105&72&565,568\\
29&(-11,9;-2,-1)&757&7,205&77&56&1,431,624\\
31&(-9,-13;1,-2)&871&9,495&49&36&1,148,936\\
37&(-4,-13;1,-6)&1,261&13,917&69&56&3,413,488\\
41&(-16,-7;-1,-3)&1,561&17,875&81&56&5,161,456\\
43&(-5,13;-1,-6)&1,723&19,819&105&88&8,135,424
\end{array}                                         \tag{3.2}
\]

For the first five rows, the exact opposite-endpoint profiles
`(sum nu, |supp nu|, max nu, sum nu^2)` are

\[
\begin{array}{c|rrrr|c}
p&\sum\nu&|\operatorname{supp}\nu|&\max\nu&\sum\nu^2&
 (\sum\nu^2)/(\sum\nu)\\ \hline
11&2,264&1,880&4&3,192&1.4098\ldots\\
13&3,450&2,954&4&4,642&1.3455\ldots\\
17&20,014&15,842&7&31,370&1.5674\ldots\\
19&127,002&87,224&10&242,278&1.9076\ldots\\
23&498,674&287,262&14&1,258,518&2.5237\ldots
\end{array}                                         \tag{3.3}
\]

Thus norm separation does not always collapse the charge to load one.
Nevertheless the surviving load is concentrated on only `O(p)` resonant
shifts, and the size-biased ratio in (3.3) is still tiny compared with every
fixed power of `N` in the checked range.  These finite values are a
falsification test, not asymptotic evidence by themselves.

## 4. Consequence for the full proof strategy

The generic-affine vanishing theorem and Proposition 2.1 now give three
qualitatively distinct affine regimes.

1. For a generic metric there is no nonzero orthogonal tail.
2. For determinant-prime metrics of the type above, the tail is supported
   on a codimension-one congruence lattice.
3. A genuinely hard model must retain a much denser exact `J`-resonance
   lattice, as in a quarter-turn-stable rank-two model.

The complete exact rank-two case already pays the sharp `r^(3/2)` height.
The remaining inverse theorem should therefore preserve a quantitative
**resonance index**: a large index makes the joint tail sparse by the present
argument, while a small index should feed the oblique-lattice height theorem.
The sparse shear examples show that this dichotomy is still false without
the endpoint realization `D=A-A`; that hypothesis remains load-bearing.

## 5. Exact coset-energy reduction and the remaining loss

There is a general identity showing both how the resonance index can help
and why shift counting alone does not prove the target.  Let `Lambda` be a
lattice containing `D`, and put

\[
 \Lambda_0=\Lambda\cap J\Lambda.
\]

This is `J`-stable.  Every `q` with `R_D(q)R_D(Jq)>0` lies in `Lambda_0`.
Decompose

\[
 D=\bigsqcup_{c\in\Lambda/\Lambda_0}D_c,
 \qquad n_c=|D_c|.                                  \tag{5.1}
\]

For `q in Lambda_0`, translation by `q` preserves every coset, so

\[
 R_D(q)=\sum_c R_{D_c}(q),qquad
 \sum_{q\in\Lambda_0}R_D(q)=\sum_c n_c^2.           \tag{5.2}
\]

Since `J` permutes `Lambda_0` and `R_D(q)<=N`, one obtains the exact easy
bound

\[
 \boxed{
 E_\perp(D)
 \le N\sum_c n_c^2.}                               \tag{5.3}
\]

Thus a sufficiently flat coset distribution proves an easy branch.  But it
does not close the determinant-prime Costas examples: there the quotient
has order `p`, `N=Theta(p^2)`, and typical `n_c=Theta(p)`, so the right side
of (5.3) is `Theta(p^5)`, one factor `p` above the observed and desired
`Theta(p^4)` scale.

Endpoint realization gives an additional exact description of these
occupancies.  After translating `A` into `Lambda`, let
`k_g=|A cap (g+Lambda_0)|`.  Oriented difference uniqueness gives

\[
 n_h=\sum_g k_{g+h}k_g\quad(h\ne0),
 \qquad
 n_0=1+\sum_g k_g(k_g-1).                         \tag{5.4}
\]

The final affine-resonant theorem must therefore do more than count
resonant shifts or cosets.  It must control the **paired within-coset
autocorrelations** under `J`, using (5.4), radial uniqueness, and the
complete endpoint labels.  This is the precise small-index continuation of
the opposite-endpoint gate.

Run `verify_determinant_prime_costas_resonance.py` for all arithmetic,
distance, support, and charge checks in (3.2)--(3.3).
