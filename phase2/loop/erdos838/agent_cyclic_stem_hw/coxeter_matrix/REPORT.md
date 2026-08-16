# Coxeter-matrix barriers for the half-weight and graded-ratio routes

**Date:** 2026-08-14  
**Verdict:** the unit, once-per-root type-`A` reflection-order cases of HW2
and the graded-ratio conjecture remain open.  This pass does not prove or
disprove either one.  It does give three theorem-level barriers inside the
exact target class, rather than in a relaxed inverse-pair class:

1. the half-activity face law need not be negatively associated, even for a
   stretchable five-point unit reflection order;
2. the natural cross operator `A(1)^T B(1)` is neither a positive operator nor
   even spectrally real in general;
3. the separate Schatten-2 data of `A(t)` and `B(t)` at both relevant
   activities do not determine their cross trace or the half-weight ratio.
4. there is a universal total-count-capped alignment inequality, but the
   scalable alternating family makes it sharp at exponential scale.

Thus ordinary strong-Rayleigh/log-Sobolev machinery, determinant-one
PSD/Loewner arguments, and separate-norm interpolation cannot close HW2 as
stated.  A surviving matrix proof must retain the **relative alignment** of
the forward and reverse temporal networks, or equivalently their common
endpoint histories.

The fourth item is the asymptotic conclusion of this lane.  It converts bad
Frobenius angle into large total face mass, but cannot by itself compare
activities `1/2` and `1`; hence it does not prove `H<=n^{o(1)}`.

All claims below are checked in exact rational arithmetic by
`verify_coxeter_matrix_barriers.py`.

## 1. Setup and claim boundary

For a reduced word for the longest element of `S_n`, let `R` be its positive
root sequence.  For each root `(i,j)`, `i<j`, put

\[
 T_{ij}(t)=I+tE_{j,i},\qquad
 B_R(t)=\prod_R T_{ij}(t),\qquad
 A_R(t)=\prod_{R^{\rm rev}}T_{ij}(t).
\]

Every positive root occurs exactly once and every factor has unit weight.
The all-faces partition polynomial is

\[
 F_R(t)=1+nt+\langle A_R(t),B_R(t)\rangle_F-n.       \tag{1}
\]

The two live conjectures are:

> **HW2 (conjecture).** For every type-`A` reflection order,
> \[
> H(R):=\frac{nF_R(1/2)}{F_R(1)}\le 2.
> \]

> **Graded ratio (conjecture, asymptotic form).** If
> `F_R(t)=sum_r v_r t^r` and
> \[
> p_r=\frac{(r+1)v_{r+1}}{(n-r)v_r},
> \]
> then `p_r >= 2^{-r-o(r)}` in the relevant range
> `r <= (1-o(1))log_2 n`.

Nothing below changes their status.  Every certificate below satisfies HW2.

## 2. The half-activity law is not negatively associated

### Theorem 1 (exact stretchable counterexample to negative association)

Take the reduced word

```text
0,1,2,1,0,1,3,2,1,0
```

in `S_5`.  Its root sequence is

```text
01,02,03,23,13,12,04,14,24,34.
```

This is a complete unit type-`A_4` reflection order.  It is stretchable: the
integral points

\[
 (0,0),(1,-6),(2,-5),(3,-6),(4,0)                 \tag{2}
\]

give the same root order modulo commuting disjoint equal-slope edges.  The
verifier checks every orientation determinant and every incident slope
comparison exactly.

Its empty-inclusive face profile is

\[
 F(t)=1+5t+10t^2+10t^3+3t^4.                     \tag{3}
\]

Equivalently, among all `2^5` subsets the only minimal nonfaces are
`{0,1,2,3}` and `{1,2,3,4}`.  Under the half-activity law

\[
 \nu_{1/2}(S)=\frac{2^{-|S|}}{F(1/2)},\qquad F(1/2)=\frac{119}{16},
\]

the endpoint indicators satisfy

\[
 \Pr(0\in S)=\Pr(4\in S)=\frac{39}{119},\qquad
 \Pr(0,4\in S)=\frac{13}{119}.
\]

Therefore

\[
 \boxed{\operatorname{Cov}_{\nu_{1/2}}(1_{0\in S},1_{4\in S})
       =\frac{26}{14161}>0.}                       \tag{4}
\]

This is a theorem, not a numerical observation.

### Consequence and limit of the consequence

The multivariate face measure is not pairwise negatively associated and hence
is not strongly Rayleigh.  Thus the standard stable-polynomial route to
negative dependence cannot simply be imported for the half-activity measure.
Strongly Rayleigh measures imply the relevant negative-dependence properties;
see Borcea--Branden--Liggett,
[Negative dependence and the geometry of polynomials](https://arxiv.org/abs/0707.2340).

This does **not** rule out every log-Sobolev inequality.  It rules out the
direct route in which negative association, stochastic covering, or real
stability supplies the needed entropy contraction.  A valid entropy proof
would have to exploit a different, history-sensitive Markov kernel such as
the deletion-path law isolated elsewhere in the campaign.

## 3. The cross matrix is not a positive operator

### Theorem 2a (nonreal cross spectrum in type `A_2`)

For the lexicographic root order `01,02,12`, exact multiplication gives

\[
 A(1)^TB(1)=
 \begin{pmatrix}
 4&2&1\\3&2&1\\2&1&1
 \end{pmatrix}.                                      \tag{5}
\]

Its characteristic polynomial is

\[
 \lambda^3-7\lambda^2+5\lambda-1,
\]

whose discriminant is `-44`.  Hence the cross matrix has one real eigenvalue
and a nonreal conjugate pair.  It cannot be treated as a positive-spectrum
determinant-one matrix.

### Theorem 2b (indefinite symmetric part in type `A_3`)

For the lexicographic root order in `S_4`, let `M=A(1)^TB(1)` and
`S=(M+M^T)/2`.  The leading three-by-three principal submatrix of `2S` is

\[
 \begin{pmatrix}
 16&11&8\\11&8&5\\8&5&4
 \end{pmatrix}.                                      \tag{6}
\]

Its leading principal minors are exactly

\[
 16,\quad 7,\quad -4.                                \tag{7}
\]

Thus `S` is indefinite.  In particular
`x^TA(1)^TB(1)x` is not a positive quadratic form.

### Consequence and limit of the consequence

The identity `det A=det B=1` cannot be combined with an eigenvalue AM--GM or a
Loewner monotonicity argument on `A^TB`: the necessary positivity is already
false in the first nontrivial ranks.  This also explains why ordinary total
positivity of the endpoint matrices was the wrong object in the inverse-pair
audit.

This does **not** rule out all noncommutative inequalities.  It says that any
Schatten or operator proof must be formulated in singular-value/Gram terms
while explicitly retaining the relative left/right singular vectors; it
cannot replace the Frobenius cross term by the trace of a positive operator.

## 4. Separate Schatten-2 endpoint data lose the decisive alignment

### Theorem 3 (exact norm collision in type `A_5`)

There are two complete, unit reflection orders `R_1,R_2` in `S_6` such that,
at both `t=1` and `t=1/2`, the separate squared Frobenius norms of their
forward and reverse products agree exactly:

\[
\begin{aligned}
 \|A_{R_1}(1)\|_F^2=\|A_{R_2}(1)\|_F^2&=59,\\
 \|B_{R_1}(1)\|_F^2=\|B_{R_2}(1)\|_F^2&=66,\\
 \|A_{R_1}(1/2)\|_F^2=\|A_{R_2}(1/2)\|_F^2&=\frac{837}{64},\\
 \|B_{R_1}(1/2)\|_F^2=\|B_{R_2}(1/2)\|_F^2&=\frac{223}{16}.
                                                               \tag{8}
\end{aligned}
\]

Nevertheless their cross traces are different:

\[
\begin{array}{c|cc}
 &t=1&t=1/2\\\hline
R_1&50&409/32\\
R_2&49&51/4.
\end{array}                                                   \tag{9}
\]

The reduced words, each checked to end at `w_0`, are

```text
R1 = 2,1,0,1,2,4,3,2,1,0,4,3,2,1,3
R2 = 2,1,0,2,1,3,4,3,2,1,0,3,2,1,4.
```

Their empty-inclusive profiles and half-weight ratios are

\[
\begin{array}{c|c|c}
 & (v_0,v_1,\ldots)&H=6F(1/2)/F(1)\\\hline
R_1&(1,6,15,20,8,1)&345/272\\
R_2&(1,6,15,20,8)&129/100.
\end{array}                                                   \tag{10}
\]

Both satisfy HW2, but the ratios are unequal despite all four separate
Schatten-2 endpoint data in (8) being identical.

### Exact polarization diagnosis

Put

\[
 \mathcal S_R(t)=\|A_R(t)\|_F^2+\|B_R(t)\|_F^2,
 \qquad
 \mathcal D_R(t)=\|A_R(t)-B_R(t)\|_F^2.
\]

Then the load-bearing cross term is exactly

\[
 \boxed{\langle A_R(t),B_R(t)\rangle_F
 =\frac{\mathcal S_R(t)-\mathcal D_R(t)}2.}          \tag{11}
\]

For the collision above, the common `S` data hide distinct alignment
defects:

\[
\begin{array}{c|cc}
 &\mathcal D(1)&\mathcal D(1/2)\\\hline
R_1&25&93/64\\
R_2&27&97/64.
\end{array}                                                   \tag{12}
\]

Equation (1) can be rewritten without loss as

\[
 F_R(t)=1+nt-n+\frac{\mathcal S_R(t)-\mathcal D_R(t)}2.       \tag{13}
\]

So a sharp matrix proof must control `D` relative to `S` over the activity
interval.  Separate Schatten-2 interpolation controls only `S` and discards
exactly the quantity that distinguishes (10).

The theorem is deliberately narrow: it proves insufficiency of **separate
Schatten-2 endpoint data**.  It does not claim that all Schatten-`p` data, the
full singular-vector flags, or the entire functions `A(t),B(t)` are
insufficient.

## 5. A universal capped-alignment theorem, sharp in exponent

The exponential alternating-family loss does admit one rigorous repair.  It
is a same-activity cap by the total cross mass.

For `i<j`, abbreviate the off-diagonal entries by

\[
 a_{ij}=A_{ji}(z),\qquad b_{ij}=B_{ji}(z),
\]

and put

\[
 Q^\circ(z)=\sum_{i<j}a_{ij}b_{ij},\qquad
 E_A(z)=\sum_{i<j}a_{ij}^2,\qquad
 E_B(z)=\sum_{i<j}b_{ij}^2,
\]

so that

\[
 \kappa(z)=\frac{Q^\circ(z)}{\sqrt{E_A(z)E_B(z)}}.
\]

### Theorem 4 (total-count-capped alignment)

For every once-per-root unit factorization containing all positive roots, at
every `z>0`,

\[
 \boxed{Q^\circ(z)\,\kappa(z)\ge z^2.}              \tag{14}
\]

Equivalently,

\[
 \boxed{(Q^\circ(z))^4\ge z^4E_A(z)E_B(z).}         \tag{15}
\]

Consequently, for every `eta>0`,

\[
 \kappa(z)\le\eta
 \quad\Longrightarrow\quad
 F(z)\ge 1+nz+\frac{z^2}{\eta}.                    \tag{16}
\]

**Proof.**  Root completeness and unit normalization put the direct path
`z` in both entries for every endpoint pair, so `a_ij,b_ij >= z`.  Hence

\[
 Q^\circ\ge z\sum a_{ij},\qquad
 Q^\circ\ge z\sum b_{ij}.                          \tag{17}
\]

Because the arrays are nonnegative,

\[
 \sqrt{E_A}\le\sum a_{ij}\le Q^\circ/z,
 \qquad
 \sqrt{E_B}\le\sum b_{ij}\le Q^\circ/z.           \tag{18}
\]

Multiplying (18) proves (15), hence (14).  Finally
`F(z)=1+nz+Q^circ(z)`, which gives (16).  No asymptotic estimate or
unstated positivity is used.  \(\square\)

Reflection betweenness is not needed for this theorem; completeness and unit
weights are.  That is consistent with the weighted complete counterexample
in the inverse-pair report: if direct-edge weights can approach zero, the
uniform lower bound in (17) disappears.

### Exponent-sharpness on a stretchable reflection family

For the scalable alternating family with chirotope
`chi(i,j,k)=(-1)^i`, the exact rich-entry formula from
`../REFLECTION_FROBENIUS_BARRIER.md` gives, for fixed `z>0` and `q=1+z`,

\[
 Q^\circ(z)=\Theta_z(q^{n/2}),\qquad
 E_A(z),E_B(z)=\Theta_z(q^n),\qquad
 \kappa(z)=\Theta_z(q^{-n/2}).                     \tag{19}
\]

Therefore

\[
 \boxed{Q^\circ(z)\kappa(z)=\Theta_z(1).}          \tag{20}
\]

This is a scalable, stretchable, unit, complete type-`A` family.  Thus no
universal strengthening of (14) to
`Q^circ*kappa >= n^c` for any fixed `c>0` is possible.  The cap is optimal at
the exponential scale.  The verifier independently replays the exact rich
entry formula through `n=80`, checks (15) rationally at both activities, and
checks a uniform constant upper bound for the capped invariant on those
rows; the all-`n` `Theta` statement follows directly from the geometric sum
in the displayed rich-entry formula.

This theorem is the promised precise dichotomy:

* good angle may support an aligned matrix argument;
* exponentially bad angle forces reciprocal total cross mass.

But it still does **not** prove asymptotic HW2.  It is a same-activity
statement.  It permits `kappa(1)` and `kappa(1/2)` to rotate by exponentially
different amounts, and only says that each rotation is paid at its own
activity.  Even under a quasipolynomial cap on `F(1)`, (14) allows
`kappa(1)=2^{-Theta((log n)^2)}`.  A full proof needs a cross-activity or
history-retaining comparison.

## 6. What remains plausible

The exact barriers and Theorem 4 point to one honest residual matrix target:

> **Relative-alignment target (conjectural programme, not a theorem).** Find
> an activity-integrated inequality for
> `S_R(t)-D_R(t)=2<A_R(t),B_R(t)>_F` which uses the unit, once-per-root
> factorization to amortize changes of the relative singular-vector/endpoint
> bases over `1/2 <= t <= 1`.

This is not merely wording.  Variable root weights already break HW2, and the
collision (8)--(12) shows where unit normalization would have to enter: it
must constrain the evolution of the angle `D`, not only the size of each
network.  In path language, `D` measures the imbalance between increasing-
time and decreasing-time path enumerators with the same endpoints.  A useful
theorem therefore has to pair or switch those endpoint histories globally.

Writing the exact cross-activity identity as

\[
 \frac{Q^\circ(1)}{Q^\circ(1/2)}
 =\frac{\kappa(1)}{\kappa(1/2)}
  \sqrt{\frac{E_A(1)E_B(1)}{E_A(1/2)E_B(1/2)}}             \tag{21}
\]

makes the remaining gate explicit.  Marginal energy dilation and angular
loss cannot be bounded separately; the alternating family has exponential
terms in both which cancel by half their exponents.  One must prove the
product in (21) is `n^{1-o(1)}` (with the low-degree correction required by
HW2), or charge the angular loss to disjoint internal face mass along a
multiscale history.

The graded-ratio target has the same lesson.  Coefficientwise positivity of
`A` and `B`, their inverse relation, and their separate norms do not control
adjacent degrees of the cross product.  Any proof of
`p_r >= 2^{-r-o(r)}` must use common-endpoint alignment or rank-three circuit
elimination.

## 7. Reproduction

From the repository root:

```bash
python3 \
  phase2/loop/erdos838/agent_cyclic_stem_hw/coxeter_matrix/verify_coxeter_matrix_barriers.py
```

Expected first line:

```text
exact Coxeter-matrix barriers: PASS
```

The verifier is dependency-free.  It independently reconstructs root
sequences from reduced words, checks completeness and reflection betweenness,
forms every transvection product over `Fraction`, reconstructs the graded face
profiles, checks the stretchable coordinate realization, enumerates the
five-point face law, and verifies the operator minors and norm collision.
