# The popular-pair rectangle moment gate

## 1. Status and correction

Keep the adaptive popular set `P`, the opposite-endpoint charge `Xi`, and
its load `nu` from `SEVEN_INCIDENCE_OPPOSITE_ENDPOINT_CHARGE.md`.  Regrouping
the charge preimages by their ordered pair of popular shifts produces exact
Cartesian rectangles.  This gives a second, complementary organization of
the off-diagonal count.

There is one important bookkeeping point.  The side associated with the
opposite endpoint is a **fourfold** intersection of translates of `D`, not a
triple intersection.  The fourth membership is the fixed charge coordinate
`v in D`; omitting it discards the seventh complete-difference incidence.
The corrected fourfold intersection is substantially smaller on every hard
complete-difference stress family.

This note proves the exact rectangle decomposition and reduces the missing
off-diagonal theorem to a product of two explicit second moments.  The
second-moment product is not yet bounded in general, so this is a sharper
gate rather than a resolution of Erdős 1208.

## 2. Rectangles indexed by a pair of popular shifts

Put `L=I+J`.  For an ordered pair

\[
 z=(q,q')\in P^2,\qquad q\ne q',                 \tag{2.1}
\]

define

\[
 \begin{split}
 A_z=\{a\in D:\;&a+q\in D,\ a+q'\in D\},\\
 B_z=\{d\in D:\;&d-Jq\in D,\\
                 &d+q-q'\in D,\\
                 &d+q-q'-Jq'\in D\}.
 \end{split}                                      \tag{2.2}
\]

Write `alpha_z=|A_z|` and `beta_z=|B_z|`, and set

\[
 T_z=\{2a+q':a\in A_z\}\subseteq D+D,
 \qquad
 V_z=\{d-Jq:d\in B_z\}\subseteq D.              \tag{2.3}
\]

Both parametrizations in (2.3) are injective, so

\[
 |T_z|=\alpha_z,\qquad |V_z|=\beta_z.            \tag{2.4}
\]

### Proposition 2.1: exact rectangle decomposition

The charge preimages whose ordered shift pair is `z=(q,q')` have image

\[
 \boxed{E_z=V_z\times T_z.}                      \tag{2.5}
\]

Consequently

\[
 \boxed{
 \mathcal O_K=\sum_z\alpha_z\beta_z,
 \qquad
 \nu=\sum_z1_{E_z}.}                            \tag{2.6}
\]

### Proof

For one preimage use the six-form notation

\[
 a=u,\quad b=a+q,\quad c=a+q',\quad d=y_q.
\]

The remaining variable forms and the fixed charge coordinate are

\[
 e=d+q-q',\quad
 f=d+q-q'-Jq',\quad
 v=d-Jq.                                        \tag{2.7}
\]

Thus the seven required memberships are exactly `a in A_z` and `d in B_z`.
The charge is

\[
 (v,t)=(d-Jq,2a+q'),                            \tag{2.8}
\]

which ranges independently over `V_z times T_z`.  Conversely, (2.8)
recovers `a` and `d`, and then (2.7) reconstructs the preimage.  Summing
over `z` proves (2.6).  QED.

Unlike the fibre-indexed sets `E_F`, which are bicliques with their
canonical matching deleted, the popular-pair-indexed sets `E_z` are full
rectangles.  Their overlaps give the exact load moment

\[
 \boxed{
 \sum_{v,t}\nu(v,t)^2
 =\sum_{z,z'}|V_z\cap V_{z'}|\,|T_z\cap T_{z'}|.} \tag{2.9}
\]

In normalized form, let

\[
 K_T(z,z')={|T_z\cap T_{z'}|\over
                   \sqrt{\alpha_z\alpha_{z'}}},\qquad
 K_V(z,z')={|V_z\cap V_{z'}|\over
                   \sqrt{\beta_z\beta_{z'}}},                 \tag{2.10}
\]

and `w_z=sqrt(alpha_z beta_z)`.  Then (2.9) is

\[
 w^T(K_T\circ K_V)w,                            \tag{2.11}
\]

where both `K_T` and `K_V` are positive-semidefinite Gram matrices with
unit diagonal.  Thus a subpolynomial norm bound for their Hadamard product
on the vector `w` would imply the size-biased load theorem.

## 3. Triple correlation versus a four-point `L` pattern

The two rectangle sides have different exact structures.  Define the
triple correlation

\[
 \tau_X(r,s)=|X\cap(X-r)\cap(X-s)|.             \tag{3.1}
\]

Then

\[
 \alpha_{(q,q')}=\tau_D(q,q').                 \tag{3.2}
\]

For the opposite side put

\[
 r=q-q',\qquad s=q-q'-Jq'.                     \tag{3.3}
\]

If

\[
 x_0=d,\quad x_1=d+r,\quad x_3=d-Jq,
 \quad x_2=d+s,
\]

then the fourfold intersection in (2.2) is equivalently

\[
 \boxed{x_2=x_3+L(x_1-x_0).}                   \tag{3.4}
\]

Conversely, (3.4) recovers

\[
 q=J(x_3-x_0),\qquad q'=q-(x_1-x_0).           \tag{3.5}
\]

Thus `beta_z` counts a restricted four-point `L`-parallelogram pattern.
The condition that both reconstructed shifts in (3.5) belong to `P` must
be retained.

For a finite set `X`, define

\[
 \mathcal E_L(X)=\sum_rR_X(r)R_X(Lr).           \tag{3.6}
\]

Equation (3.4) gives

\[
 \sum_z\beta_z\le\mathcal E_L(D),              \tag{3.7}
\]

with equality if the popularity and distinct-shift restrictions are
deleted.

## 4. Exact second-moment identities

For a shift `h`, write

\[
 D_h=D\cap(D-h).                                \tag{4.1}
\]

Squaring the triple correlations in (3.2) and grouping the two base points
by their displacement gives

\[
 \sum_z\alpha_z^2
 =\sum_h\#\{(x_0,x_1,x_2)\in D_h^3:
       x_1-x_0,x_2-x_0\in P\text{ distinct}\}. \tag{4.2}
\]

In particular,

\[
 \sum_z\alpha_z^2
 \le\sum_hR_D(h)^3.                             \tag{4.3}
\]

The corresponding identity for the fourfold side retains the extra
incidence.  Two elements `d,d+h in B_z` give four points satisfying (3.4)
inside the same overlap set `D_h`, and (3.5) reconstructs `z`.  Therefore

\[
 \sum_z\beta_z^2
 =\sum_h\#\{(x_0,x_1,x_3)\in D_h^3:
   x_3+L(x_1-x_0)\in D_h,\ q,q'\in P,\ q\ne q'\},              \tag{4.4}
\]

where `q,q'` are given by (3.5).  Hence

\[
 \boxed{
 \sum_z\beta_z^2\le\sum_h\mathcal E_L(D_h).}  \tag{4.5}
\]

The missing seventh incidence is precisely the requirement that the whole
four-point pattern in (3.4) survive in `D_h`.  A triple-intersection model
would lose this nested-overlap structure.

## 5. A sharper sufficient gate

Cauchy--Schwarz in the `z` variable and (2.6) give

\[
 \mathcal O_K^2
 \le
 \left(\sum_z\alpha_z^2\right)
 \left(\sum_z\beta_z^2\right).                 \tag{5.1}
\]

Consequently the single product estimate

\[
 \boxed{
 \left(\sum_z\alpha_z^2\right)
 \left(\sum_z\beta_z^2\right)
 \le N^{2+o(1)}S^2}                            \tag{5.2}
\]

implies `mathcal O_K<=N^(1+o(1))S`, and therefore the full cube-root order
of Erdős 1208.  A convenient stronger pair of estimates is

\[
 \sum_z\alpha_z^2\le N^{o(1)}S^2,
 \qquad
 \sum_z\beta_z^2\le N^{2+o(1)}.               \tag{5.3}
\]

The two factors in (5.2) are highly asymmetric: the first sees popular
triple correlations, while the second sees nested `L`-energy in the overlap
sets `D_h`.  This is materially more structured than applying Holder to the
six-overlap majorant.

Neither estimate in (5.3) is asserted as a theorem yet.  Abstract radial
transversals violate both by growing powers, so any proof must still use the
complete-difference endpoint factorization.  The point is that (5.2)
isolates exactly where that endpoint input can enter while preserving the
seventh incidence.

## 6. Exact stress profiles

The verifier checks (2.5)--(2.9), (3.4)--(3.5), and (4.2)--(4.4) exactly.
For the two principal complete-difference stresses it obtains

\[
\begin{array}{c|r|r|r|r|c|c}
\text{family}&\#z&\mathcal O_K&\sum\alpha_z^2&\sum\beta_z^2&
 (\sum\alpha_z^2)/S^2&(\sum\beta_z^2)/N^2\\ \hline
\text{closure }40&7110&370516&2744348&104948&
 0.0001127&0.04307\\
\text{determinant-}23\text{ Costas}&1878&498674&2294322&250722&
 0.11265&1.16959
\end{array}                                                     \tag{6.1}
\]

Across the determinant-prime Costas rows through `p=43`, the largest two
normalized factors are respectively `0.12162` and `2.10836`; their product
remains far below one.  By contrast, the abstract radial transversal already
has the two factors `25.38` and `192.13` at side twelve.  Thus the corrected
moments sharply distinguish all stored complete differences from the known
radial impostor.

Run `verify_popular_pair_rectangle_moment_gate.py` for the exact identities
and profiles.
