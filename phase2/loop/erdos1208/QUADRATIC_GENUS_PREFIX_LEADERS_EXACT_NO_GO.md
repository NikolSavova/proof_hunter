# Exact no-go for the leading genus-bonus prefix candidates

## 1. Verdict

The optimistic million-field screen granted the real quadratic field

\[
 E=\mathbb Q(\sqrt{220110}),\qquad \operatorname{Disc}(E)=880440,
\]

five extra genus dimensions.  At the screened prefix length `t=216` this
predicted generator rank `d=219` and a large positive endpoint margin.  The
exact Kummer calculation shows that none of those five dimensions survives
the chosen prime-ideal prefix:

\[
 \boxed{d=t-2=214\quad(t=216),}                          \tag{1.1}
\]

not `219`.  After this correction, even the relaxation declaring every
available outside prime ideal useful has best margin

\[
 \boxed{-1.67615\ldots}                                 \tag{1.2}
\]

over every prefix length `180<=t<=280`.  Thus `D=880440` cannot improve the
certified `D=821453` exponent `0.49369313` in the prime-prefix construction.

The same exact S-class/ray calculation kills the next four genus-screen
leaders.  This result is deliberately **prefix-only**.  It does not exclude a
nonprefix ramification set chosen to preserve a proper ideal-class subspace.

Run

```text
python3 phase2/loop/erdos1208/verify_quadratic880440_genus_no_go.py
```

with PARI/GP available.

## 2. Where the optimistic rank disappears

PARI unconditionally certifies the BNF of `E`.  Its ordinary and narrow class
groups have

\[
 \mathrm{Cl}(E)\cong C_2^4,
 \qquad
 \dim_{\mathbb F_2}\mathrm{Cl}^+(E)[2]=5.              \tag{2.1}
\]

The second number motivated the genus bonus.  However, Kummer rank for a
fixed set `S` depends on the localized class group, not the original narrow
class group alone.  Let `S_180` be the first 180 odd prime ideals ordered by
norm.  PARI's exact `bnfsunit` calculation gives

\[
 \mathrm{Cl}_{S_{180}}(E)=1.                            \tag{2.2}
\]

It also gives 182 fundamental S-unit squareclass columns.  Their image in the
ray square quotient for

\[
 (4O_E;\text{both real places})                         \tag{2.3}
\]

has rank four; the quotient itself is `C_2^4`.  Consequently

\[
 \dim K(S_{180},2)=182-4=178.                           \tag{2.4}
\]

For every prefix `S_t` with `t>=180`, localization remains class-group
surjective, so `Cl_{S_t}(E)=1`.  Each newly inverted odd prime adds exactly
one S-unit column, while the already-surjective four-condition image remains
rank four.  Hence, exactly,

\[
 \boxed{\dim K(S_t,2)=t+2-4=t-2\qquad(t\ge180).}         \tag{2.5}
\]

This calculation includes both real signs, the complete square-modulo-4
condition, the ordinary S-class group, and the norm-minus-one unit behavior.
It is not an inference from a generic unit-signature formula.

At the original screened length `t=216`, the final prefix ideal has norm
1163 and (2.5) gives `d=214`.  The best exact-rank prefix in the endpoint
audit is instead `t=217`, with `d=215`.

## 3. All-useful endpoint kill

For a prefix of length `t`, put `d=t-2` and grant the favorable quadratic
base relation bound `r_0<=d+1`.  The largest number of Frobenius-square caps
consistent with the strict degree-two Golod--Shafarevich inequality is

\[
 N(t)=\left\lfloor{d^2-1\over4}\right\rfloor-(d+1)-t.  \tag{3.1}
\]

The verifier declares the next `N(t)` prime ideals useful without performing
any mod-3 rejection.  This can only improve the construction.  It then builds
the complete depth-one-to-three divisor frontier and checks all 101 integers
`180<=t<=280` at `alpha=0.49369313`.  The maximum is

\[
\begin{array}{c|c|c|c|c}
t&d&N(t)&w&\text{two-endpoint margin}\\ \hline
217&215&11123&40030.0887\ldots&-1.6761378\ldots
\end{array}                                             \tag{3.2}
\]

The high-precision hostile rerun uses the rational lower disk constant
`11978/10863 < 2 sqrt(3)/pi`; lowering this constant makes the endpoint right
side smaller, so it is the conservative direction for a no-go.  At the unique
cusp where the two endpoint branches agree it
finds

\[
 w=40030.0887324547946077\ldots,
 \qquad M=-1.6761378026886398308\ldots.                  \tag{3.3}
\]

The left derivative there is `+0.00503984...` and the right derivative is
`-0.0127470...`.  Since each endpoint margin is concave, this derivative
bracketing certifies the global maximum.  Independent 90- and 150-digit runs
agree beyond 70 decimal places.  The largest omitted fourth-depth slope is
smaller than every relevant active third-depth frontier slope by the same
local monotonicity used in the positive record certificates; including it
cannot improve the depth-complete frontier.

## 4. The other leading genus candidates

The reusable exact audit was applied to the next four leaders.  In every
case `Cl_{S_180}` is trivial, there are 182 S-unit columns, the ray square
quotient and its image both have rank four, and therefore (2.5) holds.  The
table gives the best result after scanning all prefixes `180..280` and still
declaring every outside ideal useful.

\[
\begin{array}{c|c|c|c|c|r}
D&h_E&\dim\mathrm{Cl}^+[2]&t_{\rm best}&d&
  \text{best margin}\\ \hline
880440&16&5&217&215&-1.6761378\\
963480&32&5&223&221&-1.9991880\\
937365&16&5&223&221&-2.0632359\\
871080&48&5&219&217&-2.1050118\\
552552&16&5&221&219&-2.4321194
\end{array}                                             \tag{4.1}
\]

The exact ordinary 2-rank is four in all five fields.  Some ordinary class
groups have higher 2-power or odd structure (for example `h=48`); this does
not affect the conclusion because the displayed S-class group is already
trivial.

## 5. Exact scope and remaining branch

This theorem closes the five leading **prime-prefix** genus-bonus candidates
from the bounded `D<=10^6` screen.  It does not prove that genus rank is
useless for arbitrary ramification sets.  A nonprefix set could deliberately
choose prime ideals whose classes span a proper subspace of `Cl(E)`, retain
some S-class 2-torsion, and pay larger prime norms/root discriminant in
exchange.  Classifying that rank-versus-cost assignment is the exact
remaining genus branch; no claim about it is made here.
