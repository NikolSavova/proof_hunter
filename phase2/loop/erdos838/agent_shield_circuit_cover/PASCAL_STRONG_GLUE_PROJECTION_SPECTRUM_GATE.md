# Pascal strong glue under every projection: exact diagonal reduction

**Date:** 2026-08-15. All face and chain counts are nonempty, and all
logarithms are base two. This continues
`RANK_SAFE_ENDPOINT_SURPLUS_GATE.md`.

## Verdict

The low-surplus construction chart of the opposite-density Pascal glue is
not its finite worst case. Exact exhaustion gives

\[
 P=T(4,3)\prec T(8,2),\qquad N=32,\qquad V(P)=1\,125\,297,
\]

and, over all $968$ projection orders,

\[
 \min_\theta {C_\theta U_\theta\over V}=32^{1.5457707\ldots},
 \qquad
 \max_\theta {C_\theta U_\theta\over V}=32^{1.8046995\ldots}.       \tag{1}
\]

The maximizing profile is $(327158,1790)$, up to reversal. A larger exact
diagonal audit gives

\[
 P'=T(7,5)\prec T(12,3),\qquad N=241,
\]

with the two chambers adjacent to the macro tie having surplus exponents

\[
                         1.7366949\ldots,qquad1.7724384\ldots .     \tag{2}
\]

Thus direction optimization beats $\log_2 3$ decisively in these finite
instances.

There is also an exact all-scale reduction. In the diagonal interval the
two child orders are reversed, and every mixed cap or cup is counted by a
weighted endpoint-interval functional. Outside that interval, while the
blocks are separated, the exact count is a product of four monotone
subprofile counts. These formulas prove that the remaining asymptotic
question is a **weighted inversion synchronization theorem**, not an
uncontrolled arbitrary-chamber problem.

They also correct a tempting but invalid extrapolation from (1). In a
reverse-internal diagonal chamber, a mixed cap contains at most two labels
of $A$, and a mixed cup at most two labels of $B$. Hence

\[
 C_\theta(P)\le U(A)+(1+a+a^2)U(B),\qquad
 U_\theta(P)\le C(B)+(1+b+b^2)C(A).                  \tag{3}
\]

For the asymptotic family from `RANK_SAFE_ENDPOINT_SURPLUS_GATE.md`, the
leading quadratic exponent in the diagonal product is therefore the same
as that of $V(P)\sim C(A)U(B)$. The observed reset is polynomial in $N$,
not a new positive quadratic exponent. Proving that its polynomial
exponent remains above $\log_2 3$, or constructing a coherent weighted
anti-alignment, is still open. No projection-uniform counterfamily and no
asymptotic closure is claimed here.

## 1. Reverse-internal shuffle formula

Let $P=A\prec B$ be a genuine binary strong glue in its construction
order. Write $a=|A|$, $b=|B|$. Consider a projection chamber in the
cross-wall interval: the labels of each block occur in the reverse of their
construction order, but the two reversed words may be arbitrarily shuffled.

For a label $z\in B$, let

\[
 \ell_A(z)=|\{x\in A:x\text{ precedes }z\}|,
 \qquad r_A(z)=a-\ell_A(z).                            \tag{4}
\]

For functions $p,q$ on $B$, define the natural-cup endpoint transform

\[
 \Gamma_{\mathcal U(B)}(p,q)
   =\sum_{S\in\mathcal U(B)}p(\max S)q(\min S),        \tag{5}
\]

with the evident singleton convention. Define
$\Gamma_{\mathcal C(A)}$ analogously, and define
$\ell_B,r_B$ on $A$.

> **Theorem 1 (exact diagonal shuffle).** In every reverse-internal shuffle,
> 
> \[
> \begin{aligned}
> C_\theta(P)
>   &=U(A)+U(B)
>     +\Gamma_{\mathcal U(B)}(\ell_A,1)
>     +\Gamma_{\mathcal U(B)}(1,r_A)
>     +\Gamma_{\mathcal U(B)}(\ell_A,r_A),\\
> U_\theta(P)
>   &=C(A)+C(B)
>     +\Gamma_{\mathcal C(A)}(\ell_B,1)
>     +\Gamma_{\mathcal C(A)}(1,r_B)
>     +\Gamma_{\mathcal C(A)}(\ell_B,r_B).
>                                                               \tag{6}
> \end{aligned}
> \]

**Proof.** Reversing the order inside a block turns its natural cups into
caps and its natural caps into cups. Take a mixed cap and suppose its
$B$-trace is nonempty. The strong-glue signs say:

* every selected $B$ lies between every selected pair of $A$'s;
* every selected $A$ lies outside every selected pair of $B$'s.

Consequently the $A$-trace has rank at most two. It is either one label
outside the endpoint interval of the natural $B$-cup, or one label on
each side of that interval. For a cup with natural endpoints $f\le l$,
the number of choices is

\[
             \ell_A(l)+r_A(f)+\ell_A(l)r_A(f).         \tag{7}
\]

Summing (7), then adding the two standalone block complexes, gives the
first identity. Reflection gives the second. The same description gives
(3) immediately. $\square$

This theorem is stronger than a finite chamber audit: it covers every
shuffle allowed by any realization in the cross-wall interval. It is also
the reason the finite value $C=327158>V(T(8,2))$ does **not** imply
$C$ has the quadratic asymptotic exponent of $V(T(t,t/4))$.

## 2. Separated chambers are monotone-subprofile products

Now suppose a chamber puts every $A$-label before every $B$-label, but
allows arbitrary orders $\pi_A,\pi_B$ within the blocks. Let

\[
 \mathcal C_A^\uparrow(\pi_A)
\]

be the natural caps of $A$ whose construction order is increasing in
$\pi_A$, and let $\mathcal C_A^\downarrow$ be those whose construction
order is decreasing. Define
$\mathcal U_B^\uparrow,\mathcal U_B^\downarrow$ similarly.

> **Theorem 2 (exact separated formula).** If $A$ precedes $B$, then
> 
> \[
> \begin{aligned}
> C_\theta(P)
>   &=C_\theta(A)+C_\theta(B)
>     +|\mathcal C_A^\uparrow(\pi_A)|
>      |\mathcal U_B^\downarrow(\pi_B)|,\\
> U_\theta(P)
>   &=U_\theta(A)+U_\theta(B)
>     +|\mathcal C_A^\downarrow(\pi_A)|
>      |\mathcal U_B^\uparrow(\pi_B)|.                \tag{8}
> \end{aligned}
> \]

**Proof.** For two $A$-labels and one $B$-label, the projected triple
has the cap sign exactly when the selected $A$-pair retains construction
order. For one $A$-label and two $B$-labels it has the cap sign exactly
when the selected $B$-pair reverses construction order. The within-block
triple conditions then say precisely natural cap in $A$ and natural cup
in $B$. Every cross-combination is valid, giving the first product.
Reflection gives the second. $\square$

Since $V(P)\sim C(A)U(B)$ in the prescribed asymptotic family, (8) would
close direction optimization if one chamber satisfied

\[
 { |\mathcal C_A^\uparrow||\mathcal C_A^\downarrow|\over C(A)}
 { |\mathcal U_B^\uparrow||\mathcal U_B^\downarrow|\over U(B)}
       \ge N^{\log_2 3+\varepsilon}.                  \tag{9}
\]

Thus the separated part of the spectrum is exactly a synchronized pair of
weighted increasing/decreasing subsequence spectra. The two factors cannot
be selected in independent child charts; they are evaluated at the one
physical direction inherited from the parent.

## 3. What a large spectrum jump buys

The monotone-subprofile formulation connects directly to the common-edge
dilution theorem. Sweep a child from reverse construction order to
construction order by adjacent swaps. At a swap of physical labels $u,v$,
let $J_A(u,v)$ be the number of natural $A$-caps that cease to be
decreasing at that swap.

Every such trace contains $u,v$ consecutively in its natural cap chain:
they were adjacent in the ambient permutation at the swap, and the whole
trace was decreasing immediately before it. Hence $uv$ is an exposed
physical edge of every trace. Crossing each trace with an arbitrary natural
cup of $B$ produces

\[
                         J_A(u,v)U(B)                   \tag{10}
\]

ordinary parent faces sharing the same exposed edge. Therefore
`FIXED_EDGE_CARRIER_ENDPOINT_DILUTION_GATE.md` gives

\[
 \sup_\theta \sigma_\theta(P)
 \ge {J_A(u,v)U(B)\binom N2\over V(P)}
 \sim {J_A(u,v)N^2\over C(A)}.                         \tag{11}
\]

There is a reflected bound

\[
 \sup_\theta \sigma_\theta(P)
 \gtrsim {J_B(u,v)N^2\over U(B)}                       \tag{12}
\]

for a jump in the natural-cup spectrum of $B$.

This makes the remaining gap quantitative. If half the $A$-mass is lost
in the first $K$ swaps, one swap has
$J_A\ge C(A)/(2K)$, and (11) yields

\[
                         \sup_\theta\sigma_\theta(P)
                         \gtrsim {N^2\over K}.          \tag{13}
\]

Thus jumps within $K\le N^{2-\log_2 3-o(1)}$ already close. For later,
diffuse loss, one needs (9) or the weighted interval product in (6).
Equation (13) is exactly where common-edge dilution stops; it cannot by
itself turn the finite data into an asymptotic theorem.

## 4. Exact finite spectra

For $T(4,3)\prec T(8,2)$, the verifier obtains

\[
 \begin{array}{c|c|c}
 & (C,U) & CU/V\\ \hline
 \text{minimum product} &(28091,8498)&32^{1.5457707198\ldots}\\
 \text{maximum product} &(327158,1790)&32^{1.8046995008\ldots}.
 \end{array}                                                     \tag{14}
\]

It checks (6) independently in all $112$ reverse-internal shuffle
chambers.

For $T(7,5)\prec T(12,3)$,

\[
 V=10\,085\,586\,308\,253\,842.                       \tag{15}
\]

The chambers immediately below and above slope $-1/2$ have profiles

\[
 (32878891214924,4203595),\qquad
 (36975789791508,4547389),                              \tag{16}
\]

which give (2). The chain counts use the exact Pascal chirotope, not
floating-point orientations.

These values are strong evidence that the canonical rational realization
has a useful diagonal reset. They are not an asymptotic certificate: (6)
shows that the only missing information is the growth of its weighted
endpoint-interval transforms, and finite normalized exponents need not be
monotone.

## 5. Exact surviving statement

For the asymptotic parameters

\[
 A=T(11t/20,33t/80),\qquad B=T(t,t/4),                 \tag{17}
\]

the quadratic exponents are

\[
 \log C(A)=0.1267404\ldots\,t^2,\qquad
 \log U(B)=0.4189766\ldots\,t^2,\qquad
 \log V(P)=0.5457170\ldots\,t^2+o(t^2).             \tag{18}
\]

Theorem 1 bounds the diagonal profiles by polynomial multiples of the first
two quantities. Therefore a complete proof must establish a fixed-power
lower bound for the product of the two transforms in (6), uniformly along
the actual cross-wall path. Equivalently, Theorem 2 asks for (9) somewhere
along the separated child sweep. A large failure jump is already paid by
(11)--(13); the sole survivor is diffuse, coherently anti-aligned weighted
endpoint mass.

This is narrower than arbitrary two-direction spectrum optimization, and
it retains the actual physical-edge decoder needed by the global argument.
It is also the honest point at which the current proof stops.

## 6. Verification

Run

```text
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_pascal_strong_glue_projection_spectrum_gate.py
```

Expected output begins

```text
PASS: Pascal strong-glue projection spectrum; N=32 V=1125297,
```

and reports the exponents in (1)--(2). The script uses exact rational wall
orders and exact integer chain dynamic programs. It also independently
checks (6) in every applicable chamber.
