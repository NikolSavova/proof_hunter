# A hybrid endpoint charge for the adaptive seven-incidence tail

## 1. Outcome

Let `A` be distance-Sidon, put

\[
 D=A-A,\qquad N=|D|,\qquad S=|D+D|,
\]

and keep the support-adaptive popular set `P`, rich fibres `Q_K(u,s)`, and
off-diagonal mass

\[
 \mathcal O_K=\sum_{u,s}|Q_K(u,s)|(|Q_K(u,s)|-1)
\]

from `SUPPORT_ADAPTIVE_RICH_FIBRE_GATE.md`.  This note gives every ordered
off-diagonal configuration one charge in a universe of size at most `8NS`.
The charge is injective inside every individual rich fibre.  Unlike the
older opposite-endpoint map, it also uses the canonical endpoint decoration
of the complete difference set.

The remaining cross-fibre load theorem is not proved.  It is, however, a
single theorem which implies the full cube-root order, and all known
polynomial-load impostors are either outside its endpoint domain or have
empty adaptive tail.

## 2. Endpoint switch and antipodal sign

For nonzero `d in D`, write its unique ordered endpoint representation as

\[
 d=x_d-y_d,qquad m(d)=x_d+y_d.
\]

Fix `a_* in A` and put `m(0)=2a_*`.  For all `d,e in D`,

\[
 \sigma_+(d,e)={m(d)-m(e)+d-e\over2}=x_d-x_e,
 \qquad
 \sigma_-(d,e)={m(d)-m(e)-d+e\over2}=y_d-y_e.  \tag{2.1}
\]

Thus both switches belong to `D`.  One is zero exactly when the two
decorated edges share the corresponding endpoint.  If both are nonzero,
their unique endpoint representations recover `(d,e)`.

The midpoint map has exactly the antipodal ambiguity

\[
 m(d)=m(e)\quad\Longrightarrow\quad e=d\text{ or }e=-d.       \tag{2.2}
\]

Indeed equality of the two endpoint sums and additive Sidonicity recover
the unordered endpoint pair.  Fix a sign bit `epsilon(d)` which distinguishes
the two members of every nonzero antipodal pair (lexicographic sign is one
choice), and give zero either bit.  Then `(m(d),epsilon(d))` recovers `d`.

## 3. The charge

Write `L=I+J`.  For a fibre `F=(u,s)`, put `w=s-u`.  An ordered pair
`q!=q' in Q_K(u,s)` has the seven `D`-members

\[
 u,\quad u+q,\quad u+q',\quad
 w-q,\quad w-q',\quad w-Lq,\quad w-Lq'.         \tag{3.1}
\]

Set

\[
 a=u,\qquad c=u+q',\qquad v=w-Lq,
 \qquad h=m(a)-m(c),\qquad t=a-c=-q'.           \tag{3.2}
\]

If `h!=t` and `h!=-t`, define the normal charge

\[
 \boxed{\Psi(F,q,q')=(0,\epsilon(c),v,h)}
 \in\{0\}\times\{0,1\}\times D\times(D+D).     \tag{3.3}
\]

If `h=t` or `h=-t`, one switch in (2.1) is zero.  Put

\[
 x=a+q\in D,\quad y=w-Lq'\in D,\quad
 H=m(c)-m(y)\in D+D.                            \tag{3.4}
\]

Let

\[
 \Theta_F(q,q')=(\delta(a,c),\epsilon(y),x,H).  \tag{3.5}
\]

Here `delta(a,c)` records which switch vanishes.  If this candidate key has
multiplicity one inside `F`, charge the configuration to
`(1,Theta_F(q,q'))`.  If its local multiplicity is greater than one, route
it instead to the resonance charge

\[
 \boxed{\Psi(F,q,q')=(2,\delta(a,c),x,y)}
 \in\{2\}\times\{0,1\}\times D^2.              \tag{3.6}
\]

Thus every fallback configuration carries a distinct same-fibre midpoint
mate as an additional affine-resonance witness.

The three labelled targets have total size at most

\[
 2NS+4NS+2N^2\le8NS.                            \tag{3.7}
\]

### Proposition 3.1: fibrewise injectivity

For fixed `F=(u,s)`, the charge `Psi` is injective on ordered distinct pairs
in `Q_K(u,s)^2`.

### Proof

On the normal route, the first geometric coordinate gives `v=w-Lq`, hence
recovers `q`; the last coordinate gives `m(c)=m(u)-h`, and the sign bit and
(2.2) recover `c` and then `q'=c-u`.  The singleton candidate route is
injective by its definition.  On the resonance route, `x=u+q` recovers
`q`, while `y=w-Lq'` recovers `q'` because `L` is injective.  The route
labels are disjoint.  QED.

Let `lambda` be the charge load.  Proposition 3.1 gives

\[
 \mathcal O_K=\sum\lambda,
 \qquad
 \sum\lambda^2
 =\mathcal O_K+\sum_{F\ne G}|\Psi(F)\cap\Psi(G)|.              \tag{3.8}
\]

Every residual collision is therefore purely cross-fibre.

## 4. The one sufficient theorem

The following statement resolves the adaptive tail:

> **Hybrid cross-fibre theorem.**  For the charge (3.3)--(3.6),
> \[
>  \sum\lambda^2\le N^{o(1)}\sum\lambda.         \tag{4.1}
> \]

Indeed, Cauchy--Schwarz and (3.7) give

\[
 \mathcal O_K^2
 \le8NS\sum\lambda^2
 \le N^{1+o(1)}S\mathcal O_K,
\]

and hence

\[
 \mathcal O_K\le N^{1+o(1)}S.                  \tag{4.2}
\]

This is exactly the missing off-diagonal estimate in
`ADAPTIVE_RICH_FIBRE_STABILITY_LEDGER.md`; that ledger then gives
`E_perp(D)<=N^(1+o(1))S`, the two-support product, and
`|A|<=m^(2/3+o(1))` for `A subset [m]^2`.

The pointwise strengthening `max lambda=N^o(1)` is sufficient as well, but
it is deliberately **not** the working conjecture.  The largest loads in
the Costas stresses grow from `3` to `12`, and present data do not distinguish
slow unbounded growth from a fixed bound.  Only the averaged form (4.1) is
the essential target.

## 5. Exact fixed-key system

Fix a normal key `(epsilon,v,h)`.  For a preimage, let `p=q'`.  Equation
(2.1) gives the two nonzero switches

\[
 P_p={h-p\over2},\qquad Q_p={h+p\over2}.         \tag{5.1}
\]

Their endpoint decorations, together with the recorded sign, recover

\[
 (a,c)=T(P_p,Q_p),\qquad c=a+p,                 \tag{5.2}
\]

where `T` denotes the inverse endpoint switch on its nonzero domain.  The
second popular shift `q` is the remaining vector variable.  The six variable
members of (3.1) are exactly

\[
 a,\quad a+q,\quad c,\quad
 v+Jq,\quad v+a+Lq-c,\quad v+L(q-p).            \tag{5.3}
\]

Both `p,q` must lie in `P` and be distinct.  Thus a normal fixed-key load is
an endpoint-forced six-affine-copy system in two popular shifts, not a free
radial or approximate-group model.

For two preimages put

\[
 \rho=q_2-q_1,\qquad \pi=p_2-p_1,
 \qquad \eta=a_2-a_1,                           \tag{5.4}
\]

where `eta` is forced by the common `h` through (5.1)--(5.2).  The six form
displacements are

\[
 \boxed{
 \eta,\quad\eta+\rho,\quad\eta+\pi,\quad
 J\rho,\quad L\rho-\pi,\quad L(\rho-\pi).}      \tag{5.5}
\]

Equations (5.1)--(5.5) are the exact restart point for proving (4.1).  The
endpoint-forced `eta`, both adaptive popular shifts, and all six `D`
memberships must remain present.

## 6. The common-endpoint route is an endpoint-forced corner system

Write `p=q'` and `r=q-p`.  Because the decorated edges `a` and `c=a+p`
share an endpoint, `p` itself belongs to `D`.  In terms of the literal
`x=a+q` and the vector `y=w-Lp`, the seven members of (3.1) are exactly

\[
 x-p-r,\quad x-r,\quad x,\quad
 y+Jp-r,\quad y+Jp,\quad y-Lr,\quad y.          \tag{6.1}
\]

Here `p,p+r` are distinct adaptive-popular shifts, and the first two members
share the endpoint recorded by `delta`.

On the singleton midpoint route, a fixed key gives `x,H,epsilon(y)`.  Once
`r` is chosen, `c=x-r` is known and

\[
 m(y)=m(c)-H;                                   \tag{6.2}
\]

the sign bit and (2.2) therefore force `y`.  Thus the two free shifts are
`p,r`, while `y=Y_H(r)` is endpoint-forced.  For two preimages put
`pi=p_2-p_1`, `tau=r_2-r_1`, and `kappa=y_2-y_1`.  The seven form
displacements are

\[
 -(\pi+\tau),\quad-\tau,\quad0,\quad
 \kappa+J\pi-\tau,\quad \kappa+J\pi,
 \quad\kappa-L\tau,\quad\kappa.                \tag{6.3}
\]

The vector `kappa` is not free: (6.2) forces it through the decorated
endpoints of `c_1,c_2,y_1,y_2`.

If a candidate midpoint key repeats inside one fibre, then `u,w,x,q` are
fixed while `p` changes by some nonzero `pi`.  Its internal resonance mate
satisfies

\[
 \tau=-\pi,\qquad \kappa=-L\pi,                 \tag{6.4}
\]

and has the same value of `H`.  Such configurations alone use the literal
fallback `(delta,x,y)`.  For two global preimages of one fallback key,
`kappa=0`, and (6.3) reduces to

\[
 -(\pi+\tau),\quad-\tau,\quad0,\quad
 J\pi-\tau,\quad J\pi,\quad-L\tau,\quad0.       \tag{6.5}
\]

Each of those preimages additionally possesses a nonzero internal witness
(6.4).  The verifier checks (6.1)--(6.5).  This isolates the ordinary
common-endpoint mass into an endpoint-forced singleton route and a strictly
more structured local-resonance route.

There is a stronger exact description of a whole local resonance class.
If `delta` is the shared-tail case, write `u=X_0-Y_0`.  Then every parameter
`p` in the class forces all three points

\[
 X_0+p,\qquad R_0-{Jp\over2},\qquad
 S_0+{(2I+J)p\over2}                            \tag{6.6}
\]

to lie in `A`, for two fixed translations `R_0,S_0`.  Indeed the first point
is the moving head of `c=u+p`; the other two are the endpoints of
`y=w-Lp`, obtained from `m(y)=m(c)-H`.  In the shared-head case the three
copies instead have linear parts

\[
 -I,\qquad-{(2I+J)\over2},\qquad {J\over2}.      \tag{6.7}
\]

Consequently, for two parameters separated by `pi`, the unique-distance set
`D` contains vectors of squared norms

\[
 |\pi|^2,\qquad {|\pi|^2\over4},\qquad
 {5|\pi|^2\over4}.                              \tag{6.8}
\]

In particular `pi` is even in the lattice coordinates.  The resonance
fallback therefore comes with three exact affine copies in `A` and a rigid
`1:1/4:5/4` squared-distance pattern; it is not an arbitrary literal-load
exception.  Its remaining difficulty is to combine this pattern with the
adaptive popularity of `p` and the common shift `q`.

## 7. Exact stress profiles

`verify_hybrid_endpoint_opposite_charge.py` checks the charge, fibrewise
injectivity, fixed-key reconstruction, and collision displacements.  The
main profiles `(mass,image,second moment,max load)` are

\[
\begin{array}{c|r|r|r|r}
\text{family}&\text{mass}&\text{image}&\sum\lambda^2&\max\lambda\\ \hline
\text{closure }30&1,420&1,420&1,420&1\\
\text{closure }40&370,516&351,178&413,258&6\\
\text{Costas }23&498,674&395,006&760,732&7\\
\text{Costas }31&765,102&619,320&1,142,994&8\\
\text{Costas }41&4,629,690&3,497,414&7,698,540&12\\
\text{Costas }43&8,451,318&6,145,754&14,911,698&12
\end{array}                                      \tag{7.1}
\]

The corresponding size-biased loads are `1.0000,1.1154,1.5255,1.4939,
1.6629,1.7644`.  The optional extended verifier checks the rows through
`p=43`.
The dense perpendicular-ruler family has empty adaptive tail.  Abstract
radial transversals have no canonical endpoint map and are outside the
charge's domain.

There is also a useful negative diagnostic.  A fixed pair of fibres can
share more normal charges than any one charge has preimages: the largest
observed pairwise intersections for Costas sizes `22,30,36,40` are respectively
`11,18,32,25`.  For the size-36 extremizer, 32 collisions arise from one
fixed base `u`, one fixed translation between the two `w` labels, and many
unchanged second shifts `q'`.  Consequently a proof of (4.1) cannot bound
each fibre-pair intersection by an absolute constant.  It must average the
overlaps over the charge or fibre-pair distribution.

These profiles do not prove (4.1), but the hybrid map has removed all known
polynomial-load mechanisms while retaining the exact target budget.

No stored stress activates the resonance fallback: every local degenerate
midpoint key is already unique through closure size 80 and Costas `p=43`.
This is not a proof that the fallback is empty in general; its purpose is to
make the charge unconditionally fibre-injective while preserving the extra
resonance witness whenever uniqueness fails.

## 8. A tempting literal descent is false

One can avoid midpoints entirely by retaining `v=w-Lq` and then recording
the largest-radius member among

\[
 u+q',\qquad w-q',\qquad w-Lq'.                 \tag{8.1}
\]

The role and selected literal recover `q'` inside a fixed fibre, so this is
a fibre-injective charge into only three labelled copies of `D^2`.  It looks
stronger because the selected literal is maximal.  It is nevertheless a
bad global compression: its exact Costas-23 profile is

\[
 (498674,80916,30378306,326),                   \tag{8.2}
\]

with size-biased load `60.918...`, versus `1.526...` for the hybrid midpoint
charge.  At Costas-43 the exploratory profile has size-biased load
`176.215...` and maximum load `1330`.  Thus radial maximality does not
replace the endpoint midpoint coordinate.  Run the verifier with
`--literal-max` for the exact certificate (8.2).
