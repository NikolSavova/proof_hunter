# A five-channel codegree bound for mixed projected completion keys

## 1. Outcome

The missing off-diagonal role block has an exact scalar normal form.  Fix a
moving-`W` projected key

\[
 \eta_W=(r,B)\in\mathcal T_K^\perp
\]

and a moving-`V` projected key

\[
 \eta_V=(\rho,A)\in\mathcal T_K^\parallel,\qquad C=A+\rho.
\]

Put

\[
 K_0=B+Jr,\quad
 \alpha=A-JK_0,\quad
 \delta=J\rho-K_0,                                      \tag{1.1}
\]

\[
 \chi=-r-JK_0,\quad
 \gamma=J\rho+C,\quad
 \phi=\delta+C.                                         \tag{1.2}
\]

For `e,z in D`, let

\[
 t_B(e)=L^{-1}(B-e)
\]

when this is integral, and define the support

\[
 \mathcal S(\eta_W,\eta_V)=
 \left\{(e,z)\in D^2:
 \begin{array}{l}
 t=t_B(e)\in\mathbb Z^2,\\
 K_0-t,\ z-t,\ Jz+\alpha,\ e+z+\delta\in D
 \end{array}\right\}.                                  \tag{1.3}
\]

Besides the ordinary overlap function

\[
 R(v)=|D\cap(D-v)|,
\]

use the affine `L`-fibre

\[
 R_L^\natural(\omega)=|\{c\in D:\omega-Lc\in D\}|.     \tag{1.4}
\]

Then the common-group codegree of the two fixed projected keys is at most

\[
\boxed{
 \Gamma_{WV}(\eta_W,\eta_V)=
 \sum_{(e,z)\in\mathcal S(\eta_W,\eta_V)}
 \min\!\left\{
 \begin{array}{l}
 R(Jz+\chi),\ R(t_B(e)),\ R(e+\gamma),\\
 R(e+z+\phi),\ R_L^\natural(e+LC)
 \end{array}\right\}.}                                  \tag{1.5}
\]

This is the mixed-role analogue of the three-channel same-role minima.  It
is a genuine reduction: no group centre, switch translation, physical
endpoint, or hidden completion multiplicity remains inside a summand.
Unlike the same-role formula, its irreducible scalar object is a
two-variable support followed by a five-way minimum.  Replacing it by one
unweighted overlap product would discard precisely the endpoint coupling
that distinguishes the mixed block.

## 2. Lossless normal form

Use one common group with fixed original centre `(c,e)` and switch `u`.
For the `W` occurrence write

\[
 q=r+u,\qquad B=e+Lt_1,
\]

and for the `V` occurrence write

\[
 p=\rho+u,\qquad C=c+t_2=A+\rho.
\]

Let

\[
 z=B+Jq=K_0+Ju.                                         \tag{2.1}
\]

Thus `(e,z,c)` recovers the group and both occurrences:

\[
 u=-J(z-K_0),\qquad t_1=L^{-1}(B-e),\qquad t_2=C-c.       \tag{2.2}
\]

The six directed `D`-vectors of the `W` occurrence are

\[
 c-q,\ z,\ c+t_1,\ e,\ z-t_1,\ K_0-t_1,                \tag{2.3}
\]

while those of the `V` occurrence are

\[
 C-p,\ e+Jp,\ c,\ e+Lt_2,\ e+Jp+t_2,\ e+J\rho+t_2.     \tag{2.4}
\]

The four `c`-independent constraints in (2.3)--(2.4) are exactly

\[
 K_0-t_1,\quad z-t_1,\quad Jz+\alpha,\quad
 e+z+\delta\in D,                                      \tag{2.5}
\]

which proves the support (1.3).  For a fixed supported pair `(e,z)`, the
remaining coordinate `c in D` must satisfy all five conditions

\[
\begin{aligned}
 c+(Jz+\chi)&\in D,\\
 c+t_1&\in D,\\
 e-c+\gamma&\in D,\\
 e+z-c+\phi&\in D,\\
 e+LC-Lc&\in D.
\end{aligned}                                           \tag{2.6}
\]

Because `D=-D`, the first four possible `c`-loads are respectively

\[
 R(Jz+\chi),\quad R(t_1),\quad R(e+\gamma),\quad
 R(e+z+\phi).                                           \tag{2.7}
\]

The fifth is (1.4).  Taking their minimum and then summing over (1.3)
proves (1.5).  Every adaptive-popular constraint was omitted only in the
upper-bound direction, so (1.5) applies unchanged to the live adaptive
population.

## 3. The four physical endpoint orientations

The algebra above is independent of whether the common physical endpoint
is the head or tail of `B` and `C`.  Let

\[
 \sigma_V=\begin{cases}1&\text{the endpoint is the head of }C,\\-1&\text{the tail,}\end{cases}
 \qquad
 \sigma_W=\begin{cases}1&\text{the endpoint is the head of }B,\\-1&\text{the tail.}\end{cases}
\]

All four cases obey the single signed identity

\[
 \sigma_WB-\sigma_VC\in D.                              \tag{3.1}
\]

For a prescribed nonzero value of (3.1) and prescribed roles, directed-
vector Sidonicity fixes the two nonshared endpoints.  The common endpoint
then has at most `k-2` choices.  Thus the physical orientation layer costs
only the same factor `O(k)` as in the diagonal-role theorem; it creates no
additional metric multiplicity.

If `mathcal G_2^{WV}` denotes the ordered mixed pair mass with the `W`
occurrence listed first, then

\[
 \mathcal G_2^{WV}
 \le
 \sum_{\substack{\eta_W,\eta_V\text{ endpoint-compatible}\\
                   \text{in their prescribed roles}}}
 \Gamma_{WV}(\eta_W,\eta_V).                            \tag{3.2}
\]

The reverse ordering has the same mass.  Formula (3.2), together with the
same-role scalar theorem, now covers every endpoint-role block.  The exact
remaining theorem is the global size-biased estimate for the sum in (3.2)
and its same-role analogues.

## 4. Stress verdict

The exact optimal-core analyzer now records the role of every repeated
switch pair.  On the three largest transformed Costas stresses, the
`V`--`W` shares are

\[
 \frac{38128}{71486}=53.34\%,\qquad
 \frac{18984}{29904}=63.48\%,\qquad
 \frac{54560}{88220}=61.84\%                            \tag{4.1}
\]

for sizes `29,31,37`.  Same-oriented-role shares are only `22.96%`,
`17.03%`, and `15.03%`.  The mixed block is therefore the dominant genuine
stress, not a constant-factor cleanup.

The projected-pair codegree profile gives a second, equally important
split.  For the same three rows, the mixed incidence/support/maximum-
codegree/collision quadruples are

\[
 (38128,31830,7,7724),\quad
 (18984,13006,11,10658),\quad
 (54560,47660,6,8014).                            \tag{4.2}
\]

Thus the dominant mixed mass is mostly support: at size `37`, `87.35%` of
its incidences already have a distinct projected-key pair, and the maximum
codegree is six.  The same-type blocks are qualitatively different; on the
same rows the maximum `W`--`W` codegrees are `88,43,40`.  A proof should
therefore use (1.5) as an occupied-support inverse for the mixed block and
reserve the high-reuse density increment for the same-type blocks.  A
single worst-codegree estimate would erase this load-bearing distinction.

Run

```bash
python3 phase2/loop/erdos1208/analyze_swap_optimal_nested_cores.py --larger
```

to reproduce the profiles.

## 5. Verification and next gate

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_projected_key_mixed_codegree_min.py
```

The verifier checks the twelve-vector identities and the inverse (2.2) on
50,000 random integral configurations, exhausts the five-channel minimum on
hundreds of nonempty finite cells, and checks the `k-2` physical endpoint
factor in all four orientations on genuine distance-Sidon sets.

The next proof target is no longer a local inversion.  It is the global
correlation estimate

\[
 \sum_{\eta_W\sim\eta_V}\Gamma_{WV}(\eta_W,\eta_V)
 \le K N^{o(1)}\,\mathcal M,                            \tag{5.1}
\]

with the exact size-biased mass `mathcal M` from the nested-core reduction,
combined with the two same-role convolution sums.  The two-variable support
in (1.3) and the minimum in (1.5) must be retained; all previously tested
one-channel or pointwise replacements admit the known equality models.
