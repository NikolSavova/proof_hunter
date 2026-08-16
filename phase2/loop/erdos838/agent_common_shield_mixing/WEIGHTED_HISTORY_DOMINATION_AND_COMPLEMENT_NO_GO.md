# Genuine-history domination and the exact limit of complementary downfaces

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The weighted fixed `(p,F,tau)`, common-`W` omitted-petal fibre is already
globally paid.  No reattachment of `W-A` is needed when the occurrences
retain their genuine likelihood weights.

Indeed, let a rank-`k` ordinary face `U` be canonically peeled at depth
`j`, let `T_j(U)` be the remaining parent, and let `e_j(U)` be its endpoint
pair.  The genuine history weight from the radial/Hall bridge is

\[
 w_{U,j}={2^{-|T_j(U)|}\over4^jG_{e_j(U)}}
         ={2^{-k}\over G_{e_j(U)}}.                     \tag{1}
\]

The endpoint edge itself is an ordinary face and contributes `1/4` to
`G_e`.  Consequently

\[
 w_{U,j}\le 2^{2-k},\qquad
 \sum_{0\le j<\lfloor k/2\rfloor}w_{U,j}
 \le \lfloor k/2\rfloor2^{2-k}\le1.                   \tag{2}
\]

Thus every decorated subfamily which merely **selects** canonical
histories--in particular one fixed `W,A,p,F,tau` fibre--has total genuine
weight at most `V(P)`.  If the upstream representation has decoder
multiplicity `L`, the bound is `LV(P)`.  The four-local source/mark decoder
load `L<=k+1` is therefore only a rank factor.  On the bounded-rank slice it
is `D^{o(1)}`, so this is stronger than the required
`D^(1-epsilon)V(P)` estimate for every fixed `epsilon<1` and large `D`.

There is also an exact warning about the proposed complementary-downface
repair.  Put `C=W-A`, `c=|C|`.  The ordinary pair

\[
                         (A\cup I,\ C-I),\qquad I\subseteq C,       \tag{3}
\]

jointly retains `W`, but it carries only `c` Boolean bits.  For any rooted
record map, splitting collisions by (3) can reduce their weighted square
energy by **at most** `2^c`, and uniform routing attains exactly this factor.
It cannot recover an omitted petal or convert likelihood weight into raw
history count beyond those `c` bits.  This sharp no-go explains the earlier
erasure obstruction in raw-count arguments, but it does not affect the
genuinely weighted fibre because (2) pays that fibre before erasure.

## 1. Canonical histories pack into the ordinary face count

Let `mathcal F(P)` be the ordinary convex faces of a finite planar point
set, including the empty face, and put `V(P)=|mathcal F(P)|`.  For an
endpoint pair `e={x,y}`, use the unnormalised endpoint half-weight

\[
 G_e=\sum_{R\in\mathcal F(P):\,\min R=x,\,\max R=y}2^{-|R|}.        \tag{4}
\]

The two-point face `e` occurs in this sum, so

\[
                              G_e\ge2^{-2}.              \tag{5}
\]

For `U={u_1<...<u_k}` and
`0<=j<floor(k/2)`, canonical radial peeling leaves

\[
 T_j(U)=\{u_{j+1},...,u_{k-j}\},\qquad
 e_j(U)=\{u_{j+1},u_{k-j}\}.                            \tag{6}
\]

Since `|T_j(U)|=k-2j`, (1) follows exactly.  The last inequality in (2) is
elementary: it is equality at `k=2`, is `1/2` at `k=3,4`, and decreases
thereafter.

> **Theorem 1 (genuine-history packing).**  Let `Omega` be any weighted
> submultiset of canonical pairs `(U,j)`, with each copy carrying (1).  If
> every geometric pair `(U,j)` occurs with multiplicity at most `L`, then
> 
> \[
>                         \boxed{\sum_{\omega\in\Omega}w_\omega
>                                      \le L V(P).}       \tag{7}
> \]

**Proof.**  Group the histories by `U`, apply (2), multiply by `L`, and sum
over the at most `V(P)` ordinary choices of `U`.  QED.

The statement is stable under every localization used in the live descent.
Conditions such as

* `W subset I_(e_j(U))`;
* a fixed bad-circuit trace and endpoint role;
* one repair mark `p` and one shield face `F`; or
* one tangent state and one omitted-petal rank

only delete histories.  They cannot increase (7).  A marked incidence is
set-valued, so fixing the actual pair `(p,F)` does not duplicate a history.
If the same source face admits several upstream source-mark descriptions,
their already certified decoder load is the `L` in (7).

## 2. Direct consequence for the literal common-face load

The radial likelihood ratio expands exactly as

\[
 h_{j,e}={q_{j,e}\over p_e}
   =\sum_{U:\,e_j(U)=e}{2^{-|U|}\over G_e}.              \tag{8}
\]

For any ordinary interval target `W`, define

\[
 H_W=\sum_{j,e:\,W\subset I_e}h_{j,e}.                  \tag{9}
\]

Equations (8) and (1) identify `H_W` with the total genuine weight of the
corresponding selected canonical histories.  Theorem 1 with `L=1` gives

\[
                              \boxed{H_W\le V(P).}       \tag{10}
\]

This holds before or after the good/bad circuit split, and hence also after
fixing `A subset W`.  Since the literal normalized load is
`ell(W)=H_W/4`, every target obeys `ell(W)<=V(P)/4`.  In particular, for the
cap-weighted parent demand `S=E_pi ell(W)`,

\[
                              \boxed{S\le V(P)/4}.       \tag{11}
\]

Combining this with the already proved Jensen lower bound
`S>=M2^(D_KL/M)` yields the clean global implication

\[
                       \boxed{V(P)\ge4M2^{D_{KL}/M}.}    \tag{12}
\]

No Hall allocation or rank matching is needed for this **weighted**
conclusion.  Rank matching remains necessary only when a later argument
asks to replace (8) by unweighted multiplicities.

The scale of this statement is important.  Equation (11) does **not** say
that `S=M n^{o(1)}` or otherwise make the KL term small: `V(P)` itself may
be quadratic-exponential in `log n`.  What (7), (10), and (11) close is the
EIC-style linear benchmark for a fixed weighted fibre--namely a target of
the form `D^(1-epsilon)V(P)`--and (12) converts a large KL term into a lower
bound on `V(P)`.  They do not replace any argument which needs an absolute
subpower upper bound on `S` independent of `V(P)`.

## 3. Complementary downfaces: optimal energy, but only `c` bits

Fix a decomposition `W=A dotcup C`, with `|C|=c`, and an arbitrary rooted
record map `r:Omega->mathcal R`.  Put

\[
 s_R=\sum_{\omega:r(\omega)=R}w_\omega,\qquad
 E_0=\sum_Rs_R^2.                                       \tag{13}
\]

Every subset of `W` is ordinary.  Choosing `I subset C` produces the
two-face record (3), from which `I` and the whole of `W` are recovered.

> **Theorem 2 (sharp Boolean energy limit).**  Suppose each history is
> assigned one `I_omega subset C`, possibly depending on the history, and
> collisions are binned by `(r(omega),I_omega)`.  If `E_C` is the resulting
> weighted square energy, then
> 
> \[
>                              \boxed{E_C\ge2^{-c}E_0.}  \tag{14}
> \]
> 
> If instead every history is routed uniformly to all `2^c` choices with
> weight `w_omega/2^c`, equality holds in (14).

**Proof.**  Inside one rooted fibre `R`, the `2^c` loads `s_(R,I)` sum to
`s_R`.  Cauchy gives

\[
              \sum_{I\subset C}s_{R,I}^2\ge{s_R^2\over2^c}.       \tag{15}
\]

Sum over `R`.  Under uniform fractional routing every bin has load
`s_R/2^c`, so (15) is equality.  QED.

The same proof shows a max-load lower bound

\[
               \max_I s_{R,I}\ge s_R/2^c.              \tag{16}
\]

Hence complementary downfaces can never reveal more than `c` bits of an
omitted-petal history.  In particular, when `c=o(log D)` they cannot supply
a fixed-power raw-count saving.  When `c=Theta(log D)` they supply exactly
the visible Boolean factor and nothing more; a claim that they also
transfer the hidden `q/G` normalization would require an additional
history-dependent ordinary output.

## 4. Sharp planar audit and scalable interface barrier

The verifier enumerates an exact rational nine-point planar configuration
with `449` ordinary faces.  It constructs every endpoint reservoir `G_e`,
every canonical history `(U,j)`, and checks (1), (2), (8), and (10) with
rational arithmetic.  It then finds an actual blocked common interval face
`W` of rank strictly larger than its canonical `2+2` or `1+3` trace `A`,
forms `C=W-A`, and checks the equality case of (14) on the genuine history
weights in that fixed `(W,A)` fibre.

The energy obstruction is scalable, not an artefact of the nine-point
example.  In the exact radial repair-star product from
`TANGENT_MARKED_SHIELD_DESCENT.md`, deleting all active petals sends
`L^(q-4)` distinct completions to one common tangent-guarded rooted record.
For any fixed convex guarded `W=A dotcup C`, Theorem 2 applies to those
arbitrary positive genuine weights and gives exactly the factor `2^c` under
uniform complementary routing.  The configuration is paid by its radial
one-gap banks, so this is an interface barrier rather than an EIC'
counterexample.

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_weighted_history_domination.py
```

The conclusion is therefore asymmetric but complete for the requested
atom: the common-`W` trace erasure is a real raw-count decoder obstruction,
while the genuine weighted fibre has already collapsed to the linear face
bound (7).
