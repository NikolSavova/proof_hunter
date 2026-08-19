# A six-overlap fractional-basis bound for opposite-endpoint collisions

## 1. Status

Keep the opposite-endpoint load `nu(v,t)` from
`SEVEN_INCIDENCE_OPPOSITE_ENDPOINT_CHARGE.md`.  This note gives a new exact
upper bound for the ordered off-diagonal collisions counted by

\[
 \sum_{v,t}\nu(v,t)(\nu(v,t)-1).                    \tag{1.1}
\]

Two preimages of one key force six translated copies of `D`.  The six base
forms have only four vector degrees of freedom.  Thirteen of their fifteen
four-form projections are invertible, and a fractional combination of
those bases gives the symmetric exponent `2/3` on every overlap count.
More importantly, adjoining the two adaptive-popular shifts gives a second
fractional basis in which both popularity overlaps have exponent one and
all six `D`-overlaps have exponent `1/3`.

The result retains all six complete-difference incidences in a charge
collision.  It is strictly sharper structurally than the earlier raw
majorants which discarded the seventh incidence.  Its aggregate sum is
still unproved at the required scale, so this is a new analytic gate, not a
resolution of Erdős 1208.

## 2. The four free forms and six constrained copies

For one charge preimage, use

\[
 a=u,\quad b=x_q,\quad c=x_{q'},\quad d=y_q.         \tag{2.1}
\]

The other two variable `D`-elements are

\[
 e=d+b-c,qquad f=e+J(a-c).                         \tag{2.2}
\]

Thus the six linear forms in the four vector variables `(a,b,c,d)` are

\[
 F_0=a,quad F_1=b,quad F_2=c,quad F_3=d,quad
 F_4=d+b-c,quad F_5=d+b-c+J(a-c).                 \tag{2.3}
\]

Consider a second preimage of the same key and write

\[
 a'=a+\delta,qquad b'=b+\varepsilon.              \tag{2.4}
\]

The fixed key gives

\[
 c'=c-\delta,qquad
 d'=d+J(\varepsilon-\delta).                       \tag{2.5}
\]

Consequently the six form displacements are

\[
\begin{aligned}
 s_0&=\delta,\\
 s_1&=\varepsilon,\\
 s_2&=-\delta,\\
 s_3&=J(\varepsilon-\delta),\\
 s_4&=(I-J)\delta+(I+J)\varepsilon,\\
 s_5&=(I+J)(\delta+\varepsilon).
\end{aligned}                                      \tag{2.6}
\]

These agree with the six-displacement list in the opposite-endpoint note.
Put

\[
 X_s=D\cap(D-s),\qquad |X_s|=R_D(s).                \tag{2.7}
\]

Every ordered charge collision with offset `(delta,epsilon)` therefore
gives a quadruple `(a,b,c,d)` for which

\[
 F_j(a,b,c,d)\in X_{s_j}\quad(0\le j<6).            \tag{2.8}
\]

The popularity and distinct-shift conditions impose additional
restrictions, so deleting them only enlarges the count.

## 3. The exact fractional basis

Let `mathcal B` be the four-subsets of `{0,1,2,3,4,5}` other than

\[
 \{0,2,4,5\},\qquad \{1,2,3,4\}.                  \tag{3.1}
\]

### Proposition 3.1

For every `B in mathcal B`, the map

\[
 (a,b,c,d)\longmapsto(F_j(a,b,c,d))_{j\in B}       \tag{3.2}
\]

is invertible over the rationals.  The two excluded projections have rank
six rather than eight.

This is an eight-by-eight integer rank calculation.  The verifier performs
Gaussian elimination exactly.

For a valid basis `B`, (3.2) injects the configurations in (2.8) into the
Cartesian product of the corresponding four overlap sets.  Hence, if
`C(delta,epsilon)` denotes the number of enlarged configurations in (2.8),

\[
 C(\delta,\varepsilon)
 \le\prod_{j\in B}R_D(s_j)
 \qquad(B\in\mathcal B).                           \tag{3.3}
\]

There is a symmetric fractional combination of these thirteen bounds.  Give
weight `1/10` to

\[
 \{0,1,2,4\},\ \{0,2,3,4\},\
 \{1,2,4,5\},\ \{2,3,4,5\},                      \tag{3.4}
\]

and weight `1/15` to each of the other nine valid bases.  The weights sum
to one, and every index `j` has total incident weight exactly `2/3`.
Taking the weighted geometric mean in (3.3) proves the main bound.

### Theorem 3.2: six-overlap majorant

For every offset `(delta,epsilon)`, the number of ordered charge collisions
with that offset is at most

\[
\boxed{
 \min_{B\in\mathcal B}\prod_{j\in B}R_D(s_j)
 \le
 \prod_{j=0}^5R_D(s_j)^{2/3}.}                    \tag{3.5}
\]

Equivalently, avoiding fractional powers,

\[
 C(\delta,\varepsilon)^3
 \le\prod_{j=0}^5R_D(s_j)^2.                       \tag{3.6}
\]

Since `R_D(-delta)=R_D(delta)`, the right side of (3.5) is

\[
 R_D(\delta)^{4/3}R_D(\varepsilon)^{2/3}
 R_D(J(\varepsilon-\delta))^{2/3}
 R_D(s_4)^{2/3}R_D(s_5)^{2/3}.                    \tag{3.7}
\]

### Theorem 3.3: popularity-refined majorant

Let

\[
 R_P(s)=|P\cap(P-s)|.                               \tag{3.8}
\]

The first preimage has popular shifts

\[
 q=b-a,\qquad q'=c-a.                               \tag{3.9}
\]

For the second preimage these become

\[
 q+(\varepsilon-\delta),qquad q'-2\delta.          \tag{3.10}
\]

Thus `q` lies in a set of size `R_P(epsilon-delta)` and `q'` in a set of
size `R_P(2delta)`.

Adjoin the two forms

\[
 F_6=b-a,qquad F_7=c-a.                             \tag{3.11}
\]

For every

\[
 i\in\{0,1,2\},\qquad j\in\{3,4,5\},               \tag{3.12}
\]

the four-form map `(F_6,F_7,F_i,F_j)` is invertible.  No pair `i,j` within
the same one of the two triples in (3.12) is invertible.  The valid pair
graph is therefore exactly `K_(3,3)`.  Averaging its nine edge bounds gives
weight one to each of `F_6,F_7` and weight `1/3` to each of `F_0,...,F_5`.
Consequently the genuine collision count obeys

\[
\boxed{
 C_P(\delta,\varepsilon)
 \le R_P(\varepsilon-\delta)R_P(2\delta)
       \prod_{j=0}^5R_D(s_j)^{1/3}.}                \tag{3.13}
\]

The pointwise minimum form is stronger:

\[
 C_P(\delta,\varepsilon)
 \le R_P(\varepsilon-\delta)R_P(2\delta)
 \min_{\substack{0\le i\le2\\3\le j\le5}}
       R_D(s_i)R_D(s_j).                            \tag{3.14}
\]

The integer-power certificate corresponding to (3.13) is

\[
 C_P(\delta,\varepsilon)^3
 \le R_P(\varepsilon-\delta)^3R_P(2\delta)^3
       \prod_{j=0}^5R_D(s_j).                       \tag{3.15}
\]

This refinement retains all four adaptive-popularity memberships of the
two colliding preimages, rather than applying popularity only after the
collision count has been estimated.

## 4. Exact aggregate consequence

Let `C_P(delta,epsilon)` count the genuine ordered charge collisions,
including both adaptive-popularity conditions.  Each ordered pair of
distinct preimages has a unique nonzero offset pair, so

\[
 \sum_{v,t}\nu(v,t)^2
 =\mathcal O_K+
  \sum_{(\delta,\varepsilon)\ne(0,0)}
       C_P(\delta,\varepsilon).                    \tag{4.1}
\]

Theorem 3.3 gives the sharper adaptive analytic gate

\[
\boxed{
 \sum_{v,t}\nu(v,t)^2
 \le\mathcal O_K+
 \sum_{(\delta,\varepsilon)\ne(0,0)}
 R_P(\varepsilon-\delta)R_P(2\delta)
 \prod_{j=0}^5R_D(s_j)^{1/3}.}                    \tag{4.2}
\]

The popularity-free Theorem 3.2 supplies the secondary bound with
`prod_j R_D(s_j)^(2/3)`.  Unlike the earlier
`R_D(r)^2R_D((I+J)r)` relaxation, both new bounds remember all six pairs
created by a collision of opposite-endpoint charges.  Bound (4.2) also
retains the two pairs of adaptive popular shifts.  The offset variables are
coupled through three genuinely different linear combinations.

What is still missing is a support-compensated estimate for the sum in
(4.2).  Generic Hölder or Brascamp--Lieb bounds use only global norms of the
two overlap functions and lose fixed powers.  The remaining opportunity is
to combine the adaptive definition of `P` with the endpoint factorization
`D=A-A`.

## 5. Exact stress audit

The verifier reconstructs every genuine charge collision and groups it by
`(delta,epsilon)`.  Its two largest tests give

\[
\begin{array}{c|r|r|r}
\text{family}&\sum\nu(\nu-1)&
 \#\text{ occupied offsets}&\max C_P\\ \hline
\text{closure }40&104,596&8,802&1,224\\
\text{determinant-}23\text{ Costas}&759,844&1,458&19,908
\end{array}                                        \tag{5.1}
\]

Every occupied offset satisfies the popularity-free and refined
minimum-basis bounds and both exact cubed inequalities.  The largest ratios
to the refined minimum-basis bound are exactly `7/517=0.01353...` for the
closure and `6/480=0.0125` for the Costas family.  The popularity-free
ratios are below `5.3*10^(-4)`.  Thus the adaptive forms improve the bound
materially, but the result is still a structural majorant rather than
numerical evidence that a black-box summation will be sharp.

Run `verify_six_overlap_fractional_basis_gate.py` for the exact ranks,
fractional weights, collision identities, and stress profiles.
