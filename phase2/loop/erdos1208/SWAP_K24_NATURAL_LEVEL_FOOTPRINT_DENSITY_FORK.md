# Natural owner depth and perpendicular footprint compression form a two-scale core

## 1. Outcome

The high-load ambient-owner theorem supplies one density parameter: an
owner cell of load `r` automatically has all three swap cells in

\[
 U_{\lfloor2r/3\rfloor}.
\]

The literal perpendicular footprint supplies a second, independent density
parameter.  Let `S` be the parameter set of one owner, `|S|=r`, and put

\[
 \Phi(S)=JS-S,
 \qquad
 R_S(u)=|\{(a,b)\in S^2:a-b=u\}|.
\]

For every integer `L>=1`, exactly one of the following alternatives holds.

1. **Expansive cell:**

   \[
   |\Phi(S)|>{r^2\over8L}.
   \]

2. **Two-scale density cell:** there are at least `5L` nonzero directions
   `u` for which

   \[
   R_S(u)\ge L,
   \qquad R_S(Ju)\ge L.
   \]

For an actual K2,4 owner, translated copies of `-S` and `JS` lie in the six
literal `D` tracks.  Hence every direction in the second alternative is
simultaneously `L`-popular in two perpendicular `D-D` channels.  Combining
this with owner saturation gives the exact certificate

\[
 \boxed{
  \text{small }JS-S
  \Longrightarrow
  \bigl(C,C_a,C_b\in U_{\lfloor2r/3\rfloor}\bigr)
  \ &\
  |\mathcal H_L(S)|\ge5L.}
\]

Thus the polynomial rich tail is no longer an undifferentiated one-cell
problem.  A cell has either a large literal footprint in `D+D`, or a second
popular perpendicular core whose level is quantitatively its footprint
compression.  The remaining aggregate theorem must pack these two density
parameters together.

This is a real narrowing, not a closure.  The expansive branch still needs
an endpoint-sensitive overlap bound, and the compressed branch still needs
a global incidence bound between deep owner stars and perpendicular popular
directions.

## 2. Exact energy calculation

Let

\[
 m_S(z)=|\{(a,b)\in S^2:Jb-a=z\}|.
\]

Then

\[
 \sum_zm_S(z)=r^2
\]

and the equality `Jb-a=Jd-c` is equivalent to
`a-c=J(b-d)`.  Therefore

\[
 \boxed{
 E_\perp(S):=\sum_zm_S(z)^2
 =\sum_uR_S(u)R_S(Ju).}
\]

Cauchy gives

\[
 E_\perp(S)\ge {r^4\over|\Phi(S)|}.             \tag{2.1}
\]

Define

\[
 \mathcal H_L(S)=
 \{u\ne0:R_S(u)\ge L,\ R_S(Ju)\ge L\}.
\]

Outside `H_L`, at least one of the two factors is below `L`.  Splitting
according to which factor is small and allowing double counting gives

\[
 E_\perp(S)
 \le r^2+2Lr(r-1)
   +\sum_{u\in\mathcal H_L(S)}R_S(u)R_S(Ju).     \tag{2.2}
\]

If `8L|Phi(S)|<=r^2`, then (2.1)--(2.2) imply

\[
 \sum_{u\in\mathcal H_L(S)}R_S(u)R_S(Ju)
 \ge5Lr^2.                                      \tag{2.3}
\]

Every summand is at most `r^2`, proving

\[
 \boxed{|\mathcal H_L(S)|\ge5L.}               \tag{2.4}
\]

The constants are intentionally comfortable.  The exact lower bound from
the calculation is `(6L-1)r^2+2Lr`.

Since `Z^2` is torsion-free,

\[
 |JS-S|\ge2r-1.                                 \tag{2.5}
\]

One proof orders both sets by a generic integer linear functional and uses
the `2r-1` strictly increasing boundary sums.  Consequently the compressed
alternative can occur only for `L<r/16+O(1)`: its second density level is
always below, but can be a fixed power of, the owner level.

## 3. Dyadic aggregate inequality

Take a family of genuine owner cells with

\[
 R\le r_C<2R.
\]

Let `E_{R,L}` be the expansive cells and let
`Omega_{R,L}` be the union of their translated footprints in `D+D`.  Put

\[
 \Delta_{R,L}=
 \max_z|\{C\in E_{R,L}:z\in\Phi_C\}|.
\]

The selected cubic weight is

\[
 M_C=3{r_C\choose3}={(r_C)_3\over2}.
\]

For an expansive cell,

\[
 {M_C\over|\Phi_C|}<4Lr_C<8LR.
\]

Distributing `M_C` uniformly over its footprint and summing depths gives
the exact support-sensitive bound

\[
 \boxed{
 \sum_{C\in E_{R,L}}M_C
 \le8LR\,\Delta_{R,L}|\Omega_{R,L}|.}           \tag{3.1}
\]

Using the actual union is essential.  Replacing it immediately by the
ambient `O(m^2)` box loses the planted-single-cell `k^3` allowance.

For the complementary compressed cells put

\[
 I_{R,L}=\sum_C|\mathcal H_L(S_C)|.
\]

Equation (2.4) and `M_C<4R^3` give

\[
 \boxed{
 \sum_{C\text{ compressed}}M_C
 \le {4R^3\over5L}I_{R,L}.}                    \tag{3.2}
\]

Every incidence counted by `I_{R,L}` carries simultaneously

* three owner vertices in `U_floor(2R/3)`;
* a nonzero shift `u` with at least `L` representations in one literal
  translated `D` track; and
* the perpendicular shift `Ju` with at least `L` representations in a
  second literal translated `D` track.

Equations (3.1)--(3.2) give the precise next fork.  It is enough to prove,
dyadically and with the physical endpoint and K2,4 colours retained, a
target-scale bound for

\[
 LR\,\Delta_{R,L}|\Omega_{R,L}|
 \quad\text{and}\quad
 {R^3\over L}I_{R,L}.                            \tag{3.3}
\]

This formulation handles isolated large cells correctly: their actual
footprint, rather than the whole ambient square, pays their `Theta(R^3)`
mass.  A failure of the first term means genuine footprint reuse; a failure
of the second means many deep owner stars reuse a perpendicular popular
direction.  Both are endpoint-labelled density increments, rather than
anonymous additive energy.

## 4. Genuine stress and falsified shortcuts

The optimal-core analyzer now stores every selected cell's full and
off-diagonal footprint, exact footprint energy, owner minimum load, physical
endpoint union, footprint-pair codegrees, and all threshold profiles.  The
new profile is reported under
`matching_selected_k24_cross_sum/natural_level_footprint_profiles`.

The low-load footprint graph is not remotely `C4`-free.  At transformed
Costas 31, the load-at-least-three population has maximum footprint-pair
codegree `140`.  Thus a bare Kővári--Sós--Turán argument is already the wrong
theorem.  The concentration falls sharply in the actual top band:

\[
\begin{array}{c|c|c|c|c|c}
p&R&\#\text{cells}&\sum M_C&
 \max\Delta&\max\Delta_{\rm wt}\\ \hline
23&3&68&204&6&18/7\\
29&5&4&120&2&10/3\\
31&6&6&360&3&735/68\\
37&5&4&120&2&60/17
\end{array}
\]

Here `Delta_wt(z)=sum_{C:z in Phi_C}M_C/|Phi_C|`.  These finite values are
evidence for the decorated high-level gate, not a pointwise conjecture:
one cell alone has weighted depth `Omega(R)`, and the known generic-segment
plantings kill footprint-only bounds.  The natural core level and endpoint
owner must stay in (3.3).

## 5. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_k24_natural_level_footprint_fork.py
python3 phase2/loop/erdos1208/analyze_swap_optimal_nested_cores.py --k24-prime=31
```

The standalone verifier exhausts the energy identity and torsion-free
support bound on all subsets of a `3 x 3` box through size six, checks the
compressed alternative nonvacuously on dense boxes, verifies the dyadic
aggregate inequalities, embeds `-S` and `JS` into a literal difference
reservoir, and recomputes the natural owner level from every optimal
orientation of the two-bundle star.
