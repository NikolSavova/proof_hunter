# A polynomial-height multi-wedge counterexample to every fixed synchronized-pooling target

## 1. Verdict and exact scope

The proposed global synchronized-pooling estimate

\[
 \boxed{\mathfrak P_\ell(W_{\cdot,L})
        \le m^{o(1)}N k^{\ell+3}}                     \tag{1.1}
\]

is false for every fixed `ell>=2`.  There are polynomial-height integral
distance-Sidon sets with `k=Theta(n)` and `N=binom(k,2)` for which

\[
 \boxed{\mathfrak P_\ell(W_{\cdot,N})
        =\Omega(n^{2\ell+4}),}                        \tag{1.2}
\]

whereas the right side of (1.1) is `n^(ell+5+o(1))`.  The violation is a
full factor `n^(ell-1-o(1))`.  In particular,

\[
 \mathfrak P_2(W_{\cdot,N})=\Omega(n^8),
 \qquad Nk^5=\Theta(n^7).                             \tag{1.3}
\]

The equality model is the dense Golomb clean core from
`SYNCHRONIZED_FIXED_WEDGE_DYADIC_GOLOMB_COUNTEREXAMPLE.md`, but with
linearly many off-line physical wedges exposing the same scalar shift.
One source pair supplies `Omega(n^3)` one-role bases, each base has a
transverse pool of size `Omega(n^2)`, and `Theta(n)` distinct physical
wedges carry its scalar label.

This has a deliberately narrow consequence.  It disproves the pooled
sufficient theorem (1.1), but does **not furnish a counterexample** to the
original scalar aggregate

\[
 \sum_q\mathcal X_q\le m^{o(1)}Nk^3.                  \tag{1.4}
\]

The binomial amplification from the original high-codegree mass to
`mathfrak P_ell` is one-way and overcounts a pool of size `Theta(n^2)` by
`Theta(n^(ell-1))` after paying back only `k^(ell-1)`.  At the selected
source pair the unamplified one-role contribution is only

\[
 O(p)W_{r,N}=\Theta(n^4),                              \tag{1.5}
\]

below the original `Nk^3=Theta(n^5)` scale.  Its once-amplified transverse
mass is `Theta(n^6)`, exactly the allowed `Nk^4=Theta(n^6)` scale.  Only
the additional binomial pooling produces the false `n^8` demand.  Thus
the original problem and its scalar aggregate remain open; no claim is
made here that the total scalar mass of this family has been bounded.

## 2. The Golomb core supplies one quadratic codegree

Take a dense integer Golomb ruler

\[
 B_n\subset[0,Cn^2],\qquad |B_n|=n,                   \tag{2.1}
\]

and put its marks on the horizontal axis.  The standard Ruzsa finite-field
construction gives such rulers explicitly.  Golomb uniqueness makes both
the squared distances and the unordered pair sums injective on the core.

There are `Theta(n^3)` unordered triples but only `O(n^2)` possible triple
sums.  Cauchy--Schwarz therefore gives `Omega(n^4)` collisions between two
triples.  Distinct equal-sum triples are disjoint: after cancelling a
shared point, pair-sum uniqueness would make the remaining pairs equal.
Distinguishing an endpoint and orienting the two triples turns every such
collision into a literal six-distinct clean start.  Hence

\[
 H:=\sum_qh_q=\Omega(n^4).                             \tag{2.2}
\]

For source starts `s,t`, let

\[
 Q_{s,t}=\{q:s,t\in H_q\},\qquad c(s,t)=|Q_{s,t}|.    \tag{2.3}
\]

The exact switch

\[
 \sum_{s,t}c(s,t)=\sum_qh_q^2                         \tag{2.4}
\]

and Cauchy over the `O(n^2)` active translations give a right side
`Omega(n^6)`.  The diagonal contributes only `H=O(n^4)`, and there are
`O(n^4)` ordered off-diagonal source pairs.  Consequently some ordered
pair `p=(s,t)`, `s!=t`, satisfies

\[
 \boxed{c_0:=c(p)\ge\alpha n^2}                       \tag{2.5}
\]

for an absolute `alpha>0`.

Let `O(p)` be the number of unordered translation pairs in `Q_p` which
meet in exactly one of the two target-edge roles.  The exact endpoint
wedge inequality is

\[
 O(p)\ge {4c_0^2\over n}-2c_0-\rho(p)(\rho(p)-1),
 \qquad \rho(p)\le n-2.                               \tag{2.6}
\]

Thus

\[
 \boxed{O(p)=\Omega(n^3).}                            \tag{2.7}
\]

This is also the correct order.  In a simple graph on `n` vertices each
edge meets at most `2(n-2)` other edges, so the sum of the wedge counts in
the two target roles is `O(nc_0)=O(n^3)`.  Hence
`O(p)=Theta(n^3)`.

For every such base, at most `15n-36` core translations fail the literal
anchor-and-two-target-role transversality predicate.  Therefore every old
base has

\[
 T_p(b)\ge c_0-(15n-36)=\Omega(n^2).                  \tag{2.8}
\]

For all large `n`, this is at least `c_0/2`, so these bases are precisely
eligible for every synchronized pool of fixed order.

## 3. A linear family of physical wedges at one scalar

Scale the core by `6z`.  If

\[
 \Delta_0=\delta(s)-\delta(t)\ne0                     \tag{3.1}
\]

before scaling, define after scaling

\[
 r=-2z^2\Delta_0.
                                                               \tag{3.2}
\]

Then `delta(s)-delta(t)=-18r`, so the scalar specialization assigns the
weight `V(p)=W_(r,N)`.  Notice that `r` is a nonzero even integer.

For every odd integer `v`, put

\[
 X_v={r+v^2+1\over2},\qquad
 u_v={r+v^2-1\over2}.                                  \tag{3.3}
\]

They are integral and satisfy

\[
 X_v^2-(u_v^2+v^2)=r.                                  \tag{3.4}
\]

Choose `L=floor(delta n)` disjoint pairs `(v_j,w_j)` of odd parameters.
For the `j`-th pair install seven fresh points:

* one origin `o_j` and two first-edge endpoints
  `o_j+(X_(v_j),0)` and `o_j+(X_(w_j),0)`;
* one independently placed partner edge with vector `(u_(v_j),v_j)`;
* one independently placed partner edge with vector `(u_(w_j),w_j)`.

The two first edges meet at `o_j`.  Equation (3.4) says that both have
scalar shift `r` to their partners, and subtracting its two instances
gives the required partner-gap identity.  Moreover the two doubled cross
determinants are

\[
 2X_{v_j}v_j,qquad 2X_{w_j}w_j.                       \tag{3.5}
\]

Choose `z` polynomially large compared with the parameter range.  Then
both absolute values in (3.5) exceed the final cutoff
`N=binom(n+7L,2)`.  The first-edge graph at shift `r` therefore contains
`L` distinct endpoint wedges, so

\[
 \boxed{W_{r,N}\ge L=\Theta(n).}                      \tag{3.6}
\]

## 4. Adding the gadgets does not erase the rich core

There are `t=7L` new points and hence

\[
 E_{\rm new}
 ={n+t\choose2}-{n\choose2}
 =nt+{t\choose2}=O(\delta n^2)                        \tag{4.1}
\]

new unordered pair sums when `delta` is an absolute sufficiently small
constant.

Let `c_1` be the common-clean codegree of the same old pair `p` in the
final set.  Every translation in `Q_p` which was absent from the core must
use a new target pair sum in at least one of its two source roles.  In a
fixed role a target sum determines the translation uniquely.  Therefore

\[
 c_1\le c_0+2E_{\rm new}.                              \tag{4.2}
\]

Choose `delta>0` in terms of the absolute `alpha` in (2.5), so small that
`2E_new<=c_0/4` for all large `n`.  Every old one-role base still has at
least `c_0-(15n-36)` old transverse translations.  Equations (2.5) and
(4.2) then give

\[
 T_p(b)\ge c_0-O(n)\ge {c_1\over2}.                   \tag{4.3}
\]

Thus all `Omega(n^3)` old bases remain transverse-rich in the final set,
and each retains a transverse pool of size `Omega(n^2)`.  This argument
does not assume that the gadgets create no new clean rows; it pays for
all possible new rows using their endpoint pair-sum resource.

## 5. Polynomial-height distance-Sidon realization

It remains to impose global squared-distance and pair-sum injectivity.
This can be done at polynomial height without disturbing any displayed
identity.

First fix `z=n^C`, with an absolute exponent `C` large enough that the
resulting nonzero `|r|` dominates the square of the polynomial parameter
range below, all core labels lie below the four forced long-edge labels,
and (3.5) exceeds `N`.  For a convenient one-parameter choice, take
`w=2v+1`.  The five distance
labels forced before the three free translations of a gadget are

\[
 X_v^2,\quad X_w^2,\quad X_v^2-r,\quad X_w^2-r,
 \quad (X_v-X_w)^2.                                   \tag{5.1}
\]

They are pairwise distinct nonconstant polynomials of degree at most four
in `v` (the two pairs with the same leading term differ by the nonzero
constant `r`).  At stage `j`, equality with any of the `O(n^2+j)` used
labels excludes only `O(n^2+j)` parameter values.  A polynomial interval
therefore supplies `L=Theta(n)` pairs for which all labels in (5.1) are
distinct from one another and from every core label.

Now regard the origin and the two partner-edge centres of every gadget as
free two-dimensional translation variables.  A repeated point, an
unintended repeated pair sum, or an unintended repeated squared distance
is the zero set of a linear or quadratic integer polynomial in these
variables.  Coefficient comparison shows that such a polynomial can
vanish identically only for the same unordered edge/pair or for one of
the five forced comparisons already excluded in (5.1).  There are only
`n^(O(1))` remaining bad polynomials.  The elementary grid nonvanishing
lemma---a nonzero degree-`d` polynomial vanishes on at most
`d|S|^(D-1)` points of `S^D`---gives an integral choice on a grid of
polynomial side length avoiding their union.

Include among the avoided quadratics every unintended equality
`delta(e)-delta(f)=r`.  Consequently the only distance-gap records at
this scalar are the two installed records per gadget; in particular
`R_D(r)=R_D(-r)=2L` and `W_(r,N)=L`.  All coordinates have size
`n^(O(1))`.  Hence the final union is a genuine
integral distance-Sidon set, has globally unique unordered pair sums, and
has height

\[
 m=n^{O(1)}.                                           \tag{5.2}
\]

In particular `m^(o(1))=n^(o(1))`, so it cannot absorb any fixed power of
`n` below.

## 6. Failure of every fixed pooling order

Let `\mathcal C_p` be the `Omega(n^3)` surviving old one-role bases.  For
each `b\in\mathcal C_p`, (4.3) gives `T_p(b)=Omega(n^2)`, while (3.6) gives
the scalar weight

\[
 W_{r,N}+W_{-r,N}\ge W_{r,N}=\Omega(n).               \tag{6.1}
\]

For every fixed `ell>=2`, the contribution of this single ordered source
pair to the exact synchronized-pool mass is therefore

\[
\begin{aligned}
 \mathfrak P_\ell(W_{\cdot,N})
 &\ge \sum_{b\in\mathcal C_p}
        {T_p(b)\choose\ell}W_{r,N}\\
 &=\Omega(n^3)\,\Omega(n^{2\ell})\,\Omega(n)
  =\boxed{\Omega(n^{2\ell+4})}.                       \tag{6.2}
\end{aligned}

Since the final `k=n+7L=Theta(n)` and `N=Theta(n^2)`, the proposed right
side is

\[
 m^{o(1)}Nk^{\ell+3}=n^{\ell+5+o(1)}.                 \tag{6.3}
\]

The ratio of (6.2) to (6.3) is `n^(ell-1-o(1))`, proving the claim.

For comparison, without binomial pooling the same selected pair supplies

\[
\begin{array}{c|c|c}
\text{mass}&\text{construction size}&\text{required scale}\\ \hline
D_{\rm one}(W)\text{ at }p&\Theta(n^4)&Nk^3=\Theta(n^5)\\
\mathfrak T_{\rm rich}(W)&\Theta(n^6)&Nk^4=\Theta(n^6)\\
\mathfrak P_2(W)&\Theta(n^8)&Nk^5=\Theta(n^7).
\end{array}                                            \tag{6.4}
\]

This table isolates the exact failure: replacing `T` by `binom(T,2)/k`
loses a factor `T/k=Theta(n)` on this ultra-high-codegree core.

## 7. Exact certificate

The verifier uses the 60-mark Ruzsa ruler (`p=61`, primitive root `2`),
the stored source pair with codegree `320`, and six seven-point gadgets at
the same scalar `r=-2,673,600`.  The 102-point union has all 5,151 squared
distances and pair sums distinct.  Its exact profile is

\[
\begin{array}{c|r}
\text{quantity}&\text{value}\\ \hline
k,N&102,\ 5,151\\
\#\text{ clean fibres},H&3,990,\ 1,323,216\\
c(p)&320\\
O(p),\ \#\text{ rich bases}&6,169,\ 6,169\\
\min T_p(b),\max T_p(b)&182,\ 245\\
B_2(p)&139,373,896\\
\#\text{ determinant-qualified first edges at }r&12\\
W_{r,N}&6\\
R_D(r),R_D(-r)&12,\ 12\\
c(p)R_D(r)&3,840\\
B_2(p)W_{r,N}&836,243,376\\
Nk^5&56,871,202,172,832\\
\max |\text{coordinate}|&903,272,942,369.
\end{array}                                            \tag{7.1}
\]

The finite instance is a structural certificate, not itself a numerical
violation; fixed constants dominate at `n=60`.  It checks global distance
and pair-sum Sidonicity, every clean fibre, the common codegree, all
one-role and literal transverse-rich predicates, the synchronized mass,
six distinct physical wedges at the same scalar, the determinant cutoff,
and the exact scalar orientation.  The raw gap multiplicity audit
`R_D(plus/minus r)=12` also confirms directly that the example is not an
original-scalar-gate counterexample.

Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_synchronized_global_multi_wedge_golomb_counterexample.py
```

## 8. Consequence for the proof architecture

No fixed synchronized pooling order can be the terminal global estimate.
The problem is not merely one-wedge concentration: `Theta(n)` genuine
physical wedges can expose the same ultra-high-codegree source pair while
preserving distance-Sidonicity at polynomial height.  Increasing `ell`
makes the artificial excess worse.

The surviving route should return to the unpooled or once-amplified mass.
Any use of synchronized cliques must normalize by the actual codegree or
pool size, rather than by the ambient threshold `k`; for example, a
size-biased factor comparable to `T^(1-ell)` would make (6.2) return to the
sharp `Theta(n^6)` scale.  What remains open is precisely an aggregate
endpoint/scalar theorem at the original `Nk^3` scale (or the equivalent
once-amplified `Nk^4` scale), with ultra-high codegrees paid only once.
