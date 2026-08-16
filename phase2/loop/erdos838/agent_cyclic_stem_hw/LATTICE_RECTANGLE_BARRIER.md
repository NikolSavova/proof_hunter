# Erdős 838: a nested planar closure-rectangle barrier

**Date:** 2026-08-14  
**Verdict:** a dense, even complete, lower--upper comparability rectangle in
the planar closure lattice need not create product-many intermediate closed
sets or common-frame two-ended faces.  There is an exact scalable
general-position construction in which `M^2` singleton-ear repair records
live over one chain of only `2M+1` relevant closed sets.  At a low constant
rank density it also defeats any interval-restricted capped Hall theorem with
`2^{o(r)}` fibres.

This is a barrier to the proposed *local lattice* implication, not a
counterexample to Erdős 838, ACP, or capped Hall with arbitrary global target
faces.  A successful theorem must use faces outside the common interval, or
use the component-density alternative in ACP Theorem 23 before entering the
rectangle.

All logarithms are base two.

## 1. Closure-lattice translation of an exterior repair

For a general-position planar set `P`, write

\[
 \operatorname{cl}(S)=P\cap\operatorname{conv}(S).
\]

Convex-position faces and closed sets are in bijection by

\[
 A\longleftrightarrow K=\operatorname{cl}(A),\qquad
 K\longleftrightarrow \operatorname{ext}K.
\]

Suppose `A` is a convex face and an exterior point `p` hides a consecutive
ear `I` of `A`.  If

\[
 K=\operatorname{cl}(A),\qquad
 K'=\operatorname{cl}(A+p),
\]

then `K subset K'`, `p` is extreme in `K'`, and

\[
 \operatorname{ext}K'= (A\setminus I)+p.
\]

It is therefore tempting to hope that a large rectangle of compatible
lower hulls and repaired upper hulls forces many elements in the intervals
`[K,K']`.  The theorem below shows that planarity and general position do not
give such a statement by themselves.

## 2. The nested-chain construction

> **Theorem 1 (complete planar repair rectangle over a thin interval).**
> For every `s>=2` and `M>=1`, there is a general-position planar point set
> containing a common convex face `R` of size `s`, lower points
> `x_1,...,x_M`, and exterior blockers `p_1,...,p_M` with the following
> properties.
>
> 1. `A_i=R+x_i` and `T_j=R+p_j` are convex faces.
> 2. For every `(i,j)`, insertion of `p_j` into `A_i` hides exactly the
>    singleton ear `{x_i}` and leaves `T_j` as the extreme set:
>    \[
>      \operatorname{ext}\operatorname{cl}(A_i+p_j)=T_j.
>    \]
>    Thus the repair support is the complete rectangle `[M] times [M]`.
> 3. Put `K_0=cl(R)` and enumerate
>    \[
>      y_1,...,y_{2M}=x_1,...,x_M,p_1,...,p_M.
>    \]
>    Then
>    \[
>      K_t:=\operatorname{cl}(R+y_t)
>          =R\cup\{y_1,...,y_t\},
>    \]
>    and the entire closure-lattice interval is the chain
>    \[
>      [K_0,K_t]=\{K_0,K_1,...,K_t\}.                 \tag{1}
>    \]
> 4. A convex face containing `R` contains at most one `y_t`.  Consequently
>    there is no common-frame two-ended face, and the union of all relevant
>    intervals/faces has only `2M+1` members.

**Exact realization.**  Put

\[
 B=10(M+s)^3,
\]

take `z` from `{-B,1,2,...,s-2,B}`, and set

\[
 R=\{(z,z^2-B^2)\},\qquad y_t=(t^2,t)\quad(1\le t\le2M).       \tag{2}
\]

The two endpoint points of `R` are `u=(-B,0)` and `v=(B,0)`.

**Proof.**  First, (2) is in general position.  Three `y` points lie on the
strict parabola `x=y^2`, and three points of `R` lie on the strict parabola
`y=x^2-B^2`, so neither type contains a collinear triple.  The line through
`y_t,y_q` has equation

\[
 x=(t+q)y-tq.                                             \tag{3}
\]

At an internal `R` abscissa `1<=z<=s-2`, its right side is negative because
`y=z^2-B^2<0`, whereas its left side is positive.  At `z=B` it is `-tq`,
and at `z=-B` equality would require `B=tq`, impossible since
`B>4M^2`.  Thus two `y` points and one `R` point are never collinear.

The line through two `R` abscissae `a,b` is

\[
 y=(a+b)x-ab-B^2.                                        \tag{4}
\]

At `(t^2,t)`, the right side is strictly negative if `a,b` are both
internal, or if exactly one is an endpoint, because `B>4M^2+s`; for the two
endpoints it is zero.  It can therefore never equal `t>0`.  This completes
the general-position check.

For `t<q`, the horizontal section at height `t` of the triangle
`uvy_q` has centre `tq` and half-width `B(q-t)/q`.  Since

\[
 |t^2-tq|=t(q-t)<{B(q-t)\over q}
 \quad\Longleftrightarrow\quad tq<B,                    \tag{5}
\]

and `tq<=4M^2<B`, the point `y_t` is strictly inside `uvy_q`.  Conversely,
`y_q` lies above every point of `conv(R+y_t)` when `q>t`.

The points of `R` form the strict lower convex chain of the parabola in
(2), and `y_t` lies above its endpoint chord.  Hence every point of `R` and
`y_t` is extreme in `R+y_t`; all earlier `y` points are interior by (5),
and all later ones are outside by height.  This proves

\[
 \operatorname{ext}K_t=R+y_t,
 \qquad K_t=R\cup\{y_1,...,y_t\}.                    \tag{6}
\]

In particular, for `i<=M<M+j`, the later point `p_j=y_(M+j)` hides
`x_i=y_i`, proving the complete repair rectangle.

Finally let `C` be closed with `K_0 subset C subset K_t`.  If `q` is the
largest index for which `y_q in C`, then (6) gives `K_q subset C`, while
maximality gives `C subset K_q`.  Thus `C=K_q`; if no such point exists,
`C=K_0`.  This proves (1).  The same strict containment (5) says that
`R+y_a+y_b` is not in convex position for `a<b`, proving the last claim.
QED.

## 3. Exact capped-Hall obstruction for interval-only routing

Fix `d<=M` blockers and retain all `M d` source--blocker records.  The union
of their common-frame intervals has at most

\[
 M+d+1                                                   \tag{7}
\]

closed-set/face targets.  Every decoder into those targets therefore has a
fibre of size at least

\[
 \left\lceil{Md\over M+d+1}\right\rceil.              \tag{8}
\]

This is not merely a full-incidence obstruction.  Let the source rank be

\[
 r=s+1,
\]

choose `M=2^(3r)`, and put `n=s+2M`.  At the natural capped scale

\[
 d=\left\lfloor {n\over2^r}\right\rfloor=2^{2r+1}.     \tag{9}
\]

Equation (8) is at least `2^(2r)`.  Even after multiplying each rank-`r`
record by its half-weight `2^(-r)`, some interval target receives load at
least `2^r`.  Thus no universal theorem of the form

> a dense planar comparability rectangle can be routed, with `2^{o(r)}`
> congestion, to intermediate closed sets or common-frame two-ended faces

is true.  The failure occurs at rank density `r/log n -> 1/3`.  If instead
`r=log n-o(log n)`, then the cap `n/2^r` is already `2^{o(r)}` and this
particular obstruction is harmless.  Any viable positive statement must
therefore include the rank-density/entropy hypothesis explicitly.

## 4. Exact equality in ACP Theorem 23

Under the uniform law on the symmetric `M^2` repair records, write

\[
 T=T_j=R+p_j,\qquad I=\{x_i\}.
\]

The support is a literal Cartesian product, so

\[
 I(T;I)=0,
\]

the independent-marginal support probability is one, and the weighted
`C_4` probability in Theorem 23 is also one.  This alone is the strongest
possible product-support conclusion, but the symmetric instance need not
satisfy the two marginal *density* hypotheses of that theorem.

The same construction has an asymmetric specialization which does satisfy
those hypotheses with equality.  The proof of Theorem 1 did not use equality
of the two alternative-family sizes: take `L` first nested points as ears
and `U` later nested points as blockers.  Let the source/target rank be
`r=s+1`, choose

\[
 L=a,\qquad U=a^r,
\]

and put the uniform law on all `a^(r+1)` repair records.  In the notation of
ACP Theorem 23,

\[
 \kappa=1,\quad\tau=r,\quad R_0=r+1,\quad
 \rho={\log_2 a^{r+1}\over r+1}=\log_2a.
\]

Therefore

\[
 H_2(I)=\log_2a=\rho\kappa,
 \qquad H_2(T)=r\log_2a=\rho\tau.                 \tag{10}
\]

Thus `epsilon=0`, `I(T;I)=0`, and both support probabilities are exactly
one, while the number of common-frame closed hulls/faces is only

\[
                         a+a^r+1                 \tag{11}
\]

against `a^(r+1)` records.  This is genuine near-product equality with no
component-density surplus.  It proves that even the full equality case of
Theorem 23 does not imply compatible two-ended multiplication inside one
closure interval.  The exact `r=3`, `a=2,3` instances are independently
checked in `lattice_rectangle_counter/verify_lattice_rectangle_counter.py`.

There is still no contradiction with Theorem 23: the theorem promises a
product support, and this is a product support.  What fails is the extra
geometric inference from a same-side product to product-many target faces.
This is the exact lattice form of the outward singleton-ear product barrier
identified after ACP Theorem 23.

## 5. What survives

The counterexample leaves a narrower plausible interval theorem:

1. first remove any marginal with entropy density above the record density;
2. only in the entropy-balanced branch use weighted `C_4` rectangles;
3. allow targets outside the common closure interval, so that cross-cell
   forward pairs can become genuine two-ended faces;
4. if all alternatives remain nested, charge the high-density child
   component rather than the interval itself.

In particular, a theorem based only on comparability in the
meet-distributive lattice cannot close the residual (137) of the ACP report.
The cyclic boundary order must enter through **cross-cell variation** or an
amortized child-cloud recurrence, not through interval richness.

## 6. Exact verification

Run

```bash
python3 phase2/loop/erdos838/agent_cyclic_stem_hw/lattice_rectangle_barrier.py
```

The verifier uses integer determinants and exact convex-hull predicates.  It
checks general position, all `64^2` repair pairs in a 136-point instance, all
closure-chain identities, and exhaustively enumerates every subset in the
relevant intervals of a smaller instance.  It also checks the exact capped
arithmetic in (9) at rank eight.
