# An endpoint cross-switched charge for the second collision moment

## 1. Outcome

Let \(A\) be distance-Sidon, put

\[
D=A-A,\qquad N=|D|,\qquad S=|D+D|,
\]

and retain the adaptive rich-fibre records from
ADAPTIVE_CROSS_PAIR_D2_CHARGE_GATE.md.  The first fixed route charges a
record \(\gamma\) to

\[
\Psi(\gamma)=(u+q,\ w-(I+J)p)\in D^2.
\]

Write \(\lambda\) for its load, let

\[
\mathcal O_K=\sum\lambda,
\qquad
M_K=\sum\lambda^2,
\]

and regard \(M_K\) as the number of ordered pairs
\(\omega=(\gamma,\gamma')\) with \(\Psi(\gamma)=\Psi(\gamma')\), including
the diagonal.

This note gives a second charge

\[
\Theta:\{\omega:\Psi(\gamma)=\Psi(\gamma')\}
\longrightarrow \mathcal Y,                    \tag{1.1}
\]

where

\[
|\mathcal Y|\le6NS.                              \tag{1.2}
\]

It mixes a midpoint difference from one pair of moving forms with an
endpoint-head switch from a different pair.  When the midpoint difference
is zero, the two decorated vectors are equal up to sign; a separate route
stores that literal vector and the sign.  The following size-biased load
estimate is sufficient for the cube-root order:

\[
\boxed{
\sum_{\eta\in\mathcal Y}\mu(\eta)^2\le N^{o(1)}M_K,} \tag{1.3}
\]

where \(\mu=|\Theta^{-1}|\).  Indeed, Cauchy--Schwarz on (1.1) gives

\[
M_K^2\le6NS\sum\mu^2,
\]

so (1.3) implies \(M_K\le N^{1+o(1)}S\).  The first charge then gives

\[
\mathcal O_K^2\le N^2M_K
\le N^{3+o(1)}S.
\]

Since \(S\ge N\),

\[
\mathcal O_K\le N^{3/2+o(1)}S^{1/2}
\le N^{1+o(1)}S,                                \tag{1.4}
\]

which is the missing adaptive-tail estimate.

Estimate (1.3) is not proved.  Its value is that a fixed key recovers two
literal endpoints of \(A\), while the other coordinate retains a
four-endpoint midpoint equation.  Thus it gives a smaller and more explicit
endpoint-sensitive extraction problem than the raw \(D^2\) collision
moment.

## 2. Endpoint decoration

Every nonzero \(d\in D\) has a unique ordered representation

\[
d=x_d-y_d,\qquad x_d,y_d\in A.
\]

Fix \(a_*\in A\), and put \(x_0=y_0=a_*\).  Define

\[
m(d)=x_d+y_d\in A+A.
\]

For an ordered pair \(d,e\in D\), encode its two heads by

\[
\chi(d,e)=
\begin{cases}
(0,x_d-x_e),&x_d\ne x_e,\\
(1,x_d),&x_d=x_e.
\end{cases}                                      \tag{2.1}
\]

The target of \(\chi\) is the labelled disjoint union

\[
\mathcal H=(\{0\}\times D^*)\sqcup(\{1\}\times A).
\]

Most importantly, \(\chi(d,e)\) recovers the ordered pair
\((x_d,x_e)\).  On the first route this is oriented-difference uniqueness;
on the second route the common head is stored literally.  The separate
common-head route is why the maximum loads in the verifier fall sharply.

Also

\[
m(d)-m(e)\in(A+A)-(A+A)=D+D.                    \tag{2.2}
\]

The full second-stage target is the labelled disjoint union

\[
\mathcal Y=
\bigl((D+D)^*\times\mathcal H\bigr)
\sqcup
\bigl(D\times\{+,-\}\times\mathcal H\bigr).      \tag{2.3}
\]

Since

\[
|\mathcal H|=|A|^2=N-1+|A|\le2N
\]

and \(N\le S\), equation (2.3) gives

\[
|\mathcal Y|
\le S|A|^2+2N|A|^2
\le6NS,
\]

as claimed in (1.2).

## 3. The seven roles in a fixed first-stage cell

For a record \(\gamma=(u,s,q,p)\), put \(w=s-u\) and \(L=I+J\).  Arrange
its seven members of \(D\) as

\[
\begin{aligned}
R_0&=u,&
R_1&=u+q,&
R_2&=u+p,\\
R_3&=w-q,&
R_4&=w-p,&
R_5&=w-Lq,&
R_6&=w-Lp.
\end{aligned}                                    \tag{3.1}
\]

The first-stage key is \((R_1,R_6)\).  Fix it as \((b,\ell)\), and use

\[
t=p-q,\qquad e=Jp.
\]

Then a record in this cell has the exact normal form

\[
\boxed{
(R_0,\ldots,R_6)=
(b+t+Je,\ b,\ b+t,\ \ell+e+t,\ \ell+e,\ \ell+Lt,\ \ell).
}                                                 \tag{3.2}
\]

Thus \((R_0,R_4)\) recovers the first record inside the cell, while
\((R_3,R_2)\) recovers the second.  The new charge crosses these two
recovering pairs.

## 4. The cross-switched charge

For an ordered collision

\[
\omega=(\gamma,\gamma'),
\qquad \Psi(\gamma)=\Psi(\gamma'),
\]

put

\[
c=m(R_0(\gamma))-m(R_3(\gamma')),
\qquad
h=\chi(R_4(\gamma),R_2(\gamma')).                \tag{4.1}
\]

If \(c\ne0\), define \(\Theta(\omega)=(0,c,h)\).
If \(c=0\), equality of the two endpoint sums implies

\[
R_3(\gamma')=\sigma R_0(\gamma)
\]

for a sign \(\sigma\in\{+,-\}\); when both vectors are zero, choose
\(\sigma=+\).  Define the zero-midpoint route by

\[
\boxed{
\Theta(\omega)=(1,R_0(\gamma),\sigma,h).
}                                                 \tag{4.2}
\]

Thus the exceptional route recovers both decorated vectors literally,
instead of collapsing all of them at the single midpoint value zero.
Equations (2.1)--(2.3) prove the target claim (1.1).

In the fixed-cell coordinates (3.2), if the two records have parameters
\((t,e)\) and \((T,E)\), then the unrefined pair \((c,h)\) is

\[
\left(
m(b+t+Je)-m(\ell+E+T),
\ \chi(\ell+e,b+T)
\right).                                         \tag{4.3}
\]

Consequently a fixed charge key gives all of the following simultaneously:

1. the ordered heads of \(\ell+e\) and \(b+T\);
2. either one nonzero difference of the endpoint sums decorating
   \(b+t+Je\) and \(\ell+E+T\), or both literal decorated vectors on the
   zero-midpoint route;
3. all fourteen \(D\)-members belonging to the two original records;
4. both adaptive-popular shift pairs.

The route was selected by an exact search over endpoint-midpoint and
endpoint-switch role pairs.  The role choice is not asserted to be uniquely
optimal.  It is distinguished by having very small within-cell
multiplicity on every stored complete-difference stress while keeping the
target at the exact \(NS\) scale.

## 5. Precise remaining theorem

Let \(\mu(\eta)=|\Theta^{-1}(\eta)|\) for \(\eta\in\mathcal Y\).

The new sufficient statement is the following.

> **Endpoint cross-switched collision theorem.**  For every planar
> lattice distance-Sidon set, with the support-adaptive popular set,
> \[
> \sum_{\eta\in\mathcal Y}\mu(\eta)^2
> \le N^{o(1)}\sum_{\eta\in\mathcal Y}\mu(\eta).
> \]

Unlike a raw affine or radial-transversal statement, this theorem cannot
even be formulated without the canonical endpoint decoration of \(D=A-A\).
An excessive fixed-key load must reuse two literal endpoint heads and one
midpoint-difference class at once.  This is the natural interface with
ENDPOINT_FOURIER_COMPENSATION_LEMMA.md: a density increment may now be
localized after two heads have already been recovered, rather than inside
an abstract six-affine-copy system.

## 6. Exact stress profiles

The verifier reports

\[
(N,S,\mathcal O_K,M_K,|\operatorname{supp}\mu|,
\sum\mu^2,\max\mu,\text{within excess},\text{within maximum}).
\]

The exact rows are:

\[
\begin{array}{c|r|r|r|r|r|r|r|r|r}
\text{family}&N&S&\mathcal O_K&M_K&|\operatorname{supp}\mu|
&\sum\mu^2&\max\mu&\text{excess}&\text{max}\\ \hline
\text{closure }30&871&62273&1420&1496&1491&1506&2&0&1\\
\text{Costas }11&91&707&2264&4348&3537&6502&7&58&2\\
\text{Costas }13&133&969&3450&5530&4767&7444&6&103&3\\
\text{closure }40&1561&156057&370516&1139274&
991814&1556038&17&11205&4\\
\text{Costas }17&241&2299&20014&46212&34196&88352&20&727&3\\
\text{Costas }23&463&4513&498674&3020644&
984142&16789428&44&73697&6\\
\text{Costas }31&871&9495&765102&3872958&
1750891&16688816&63&73539&6\\
\text{Costas }37&1261&13917&2939312&18630176&
6564482&95381176&51&137362&4
\end{array}
\]

Thus the size-biased load \((\sum\mu^2)/M_K\) ranges from
\(1.0066\ldots\) to \(5.5582\ldots\) on the displayed rows; it is
\(4.3090\ldots\) at Costas 31 and \(5.1197\ldots\) at Costas 37.  The
zero-midpoint refinement cuts the largest global load from 256 to 63 at
Costas 31.  The maximum global load still grows, so a pointwise theorem is
the wrong target.  The within-cell maximum is at most six on every displayed
row, and all larger multiplicity is cross-cell reuse of the endpoint key.
These are finite diagnostics, not a proof of (1.3).

Run

    python3 phase2/loop/erdos1208/verify_endpoint_cross_switched_collision_charge.py
    python3 phase2/loop/erdos1208/verify_endpoint_cross_switched_collision_charge.py --extended

for the exact identities and profiles.

## 7. Exact Fourier matrix form

The endpoint-head code is actually a bijection

\[
 A^2\longrightarrow\mathcal H.
\]

For unequal heads this is directed-difference uniqueness, and for equal
heads it is the literal common-head route.  Hence

\[
|\mathcal H|=|A|^2=N-1+|A|.                    \tag{7.1}
\]

This makes the Fourier content of the new charge completely explicit.  Let
\(\mathcal Z\subseteq D^2\) be the first-stage charge cells.  For
\(z\in\mathcal Z\), \(\alpha,\beta\in A\), and \(x,y\in A+A\), define

\[
\begin{aligned}
 F_{z,\alpha}(x)
 &=|\{\gamma:\Psi(\gamma)=z,\,
       x_{R_4(\gamma)}=\alpha,\,
       m(R_0(\gamma))=x\}|,\\
 G_{z,\beta}(y)
 &=|\{\gamma:\Psi(\gamma)=z,\,
       x_{R_2(\gamma)}=\beta,\,
       m(R_3(\gamma))=y\}|.
\end{aligned}                                    \tag{7.2}
\]

Before applying the literal zero-midpoint refinement, let
\(\widetilde\mu_{\alpha,\beta}(c)\) denote the load of the pair \((c,h)\),
after identifying the head code with its recovered ordered pair
\((\alpha,\beta)\).  Equation (4.1) becomes the exact convolution

\[
\boxed{
\widetilde\mu_{\alpha,\beta}(c)
=\sum_{z\in\mathcal Z}
  \sum_{x-y=c}F_{z,\alpha}(x)G_{z,\beta}(y).
}                                                 \tag{7.3}
\]

For \(c\ne0\), this is exactly the actual normal-route load.  For \(c=0\),
the charge in (4.2) refines the coefficient by the recovered literal vector
and sign, so it can only decrease its second-moment contribution.

For \(\theta\in\mathbb T^2\), let
\(\mathbf F(\theta)\) and \(\mathbf G(\theta)\) be the
\(\mathcal Z\times A\) matrices with entries
\(\widehat F_{z,\alpha}(\theta)\) and
\(\widehat G_{z,\beta}(\theta)\).  Fourier transformation of (7.3) gives

\[
\widehat{\widetilde\mu}(\theta)
=\mathbf F(\theta)^T\overline{\mathbf G(\theta)}
=\overline{\mathbf F(\theta)^*\mathbf G(\theta)}.
\]

Parseval therefore yields the exact spectral identity

\[
\boxed{
\sum_{c,\alpha,\beta}\widetilde\mu_{\alpha,\beta}(c)^2
=\int_{\mathbb T^2}
 \|\mathbf F(\theta)^*\mathbf G(\theta)\|_{\mathrm{HS}}^2
 \,d\theta.
}                                                 \tag{7.4}
\]

Equivalently, the integrand is

\[
\operatorname{tr}\!\left(
\mathbf F\mathbf F^*
\mathbf G\mathbf G^*
\right).                                         \tag{7.5}
\]

Thus a fixed-power failure of the size-biased theorem produces a frequency
at which the two endpoint-incidence matrices share a large singular mode
on the first-stage cell space.  This is sharper than merely saying that a
rich affine core exists.  The remaining density increment can be stated
precisely:

> Convert a common nontrivial cell singular mode in (7.4) into a weight
> \(0\le g\le1_D\) whose negative endpoint Fourier deficit pays, through
> ENDPOINT_FOURIER_COMPENSATION_LEMMA.md, for the same contribution to
> (7.4).

The trivial operator inequalities

\[
\|\mathbf F^*\mathbf G\|_{\mathrm{HS}}^2
\le
\min\{
\|\mathbf F\|_{\mathrm{op}}^2\|\mathbf G\|_{\mathrm{HS}}^2,\,
\|\mathbf G\|_{\mathrm{op}}^2\|\mathbf F\|_{\mathrm{HS}}^2
\}
\]

show that a size-biased spectral bound for either endpoint-incidence matrix
would suffice.  No such bound is asserted here; (7.4) identifies the exact
operator that must be controlled.
