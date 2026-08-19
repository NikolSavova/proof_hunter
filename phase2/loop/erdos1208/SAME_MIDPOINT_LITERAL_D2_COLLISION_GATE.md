# A same-midpoint literal \(D^2\) gate for the second collision

## 1. Outcome

Let

\[
 D=A-A,\qquad N=|D|,\qquad S=|D+D|,\qquad K=S/N,
\]

and retain the support-adaptive rich-fibre records and the fixed first
charge from `ADAPTIVE_CROSS_PAIR_D2_CHARGE_GATE.md`.  Write

\[
 \mathcal O_K=\sum_z\lambda(z),\qquad
 M_K=\sum_z\lambda(z)^2,
\]

where a first-charge cell is

\[
 z=(R_1,R_6)=(b,\ell)\in D^2.
\]

This note gives a second, deliberately coarser charge.  For two records
\(\gamma,\gamma'\) in the same first-charge cell, put

\[
 \boxed{
 \Theta_0(\gamma,\gamma')
   =(R_0(\gamma),R_3(\gamma'))\in D^2.}          \tag{1.1}
\]

Let \(\nu=|\Theta_0^{-1}|\).  The following \(K\)-scaled estimate is
sufficient for the cube-root order:

\[
 \boxed{
 \sum_{x,y\in D}\nu(x,y)^2
 \le K N^{o(1)}M_K.}                           \tag{1.2}
\]

Indeed,

\[
 M_K^2\le N^2\sum\nu^2.
\]

Under (1.2), cancellation gives

\[
 M_K\le K N^{2+o(1)}=N^{1+o(1)}S.
\]

The first charge then gives

\[
 \mathcal O_K^2\le N^2M_K
 \le N^{3+o(1)}S,
\]

and \(S\ge N\) yields

\[
 \mathcal O_K\le N^{1+o(1)}S.                 \tag{1.3}
\]

Thus (1.2) closes the same adaptive tail as the endpoint cross-switched
moment theorem.  It allows the much larger average load \(K=S/N\), at the
price of giving up the two cross-switched endpoint heads.

Estimate (1.2) is not proved.  Its empirical separation is strong: its
normalised ratio stays below five on every stored complete-difference
stress through Costas 23, but grows from about \(43\) to more than \(2300\)
on radial transversals of sides four through eight.

## 2. Why the same-role endpoint code is literal

Every nonzero \(d\in D\) has a unique ordered decoration

\[
 d=x_d-y_d,\qquad x_d,y_d\in A.
\]

Use one fixed diagonal decoration for zero and put

\[
 m(d)=x_d+y_d.
\]

For \(d,e\in D\), suppose one stores

\[
 c=m(d)-m(e)                                   \tag{2.1}
\]

together with the head code \(\chi(d,e)\) from
`ENDPOINT_CROSS_SWITCHED_COLLISION_CHARGE.md`.  The code recovers the
ordered heads \((x_d,x_e)\).  Hence it also recovers

\[
 y_d-y_e=c-(x_d-x_e).                           \tag{2.2}
\]

If (2.2) is nonzero, vector-Sidonicity recovers the ordered pair
\((y_d,y_e)\).  If it is zero, record the common tail literally.  In both
cases all four endpoints, and therefore \((d,e)\), are recovered.

The encoding uses at most

\[
 S|A|^2+|A|^3\le3NS                            \tag{2.3}
\]

labelled cells, since \(|A|^2=N-1+|A|\le2N\), \(S\ge N\), and
\(|A|^3\le NS\).  Conversely a literal pair \((d,e)\in D^2\) determines
the encoding.  Thus the same-midpoint endpoint route is merely a labelled
version of (1.1); it does not retain extra endpoint information.

This explains why the successful cross-switched charge uses the midpoint
roles \((R_0,R_3)\) but takes its heads from the complementary roles
\((R_4,R_2)\).  Taking the heads from \((R_0,R_3)\) collapses back to a
literal \(D^2\) pair.

## 3. Exact matrix and overlap form

Let \(\mathcal C_z\) be the record multiset in a first-charge cell \(z\).
Define

\[
 a_z(x)=|\{\gamma\in\mathcal C_z:R_0(\gamma)=x\}|,
 \qquad
 b_z(y)=|\{\gamma\in\mathcal C_z:R_3(\gamma)=y\}|. \tag{3.1}
\]

Then

\[
 \lambda(z)=\sum_xa_z(x)=\sum_yb_z(y)
\]

and the second charge factors exactly as

\[
 \boxed{
 \nu(x,y)=\sum_z a_z(x)b_z(y).}                 \tag{3.2}
\]

If \(\mathbf A=(a_z(x))_{z,x}\) and
\(\mathbf B=(b_z(y))_{z,y}\), then

\[
 (\nu(x,y))_{x,y}=\mathbf A^T\mathbf B,
 \qquad
 \sum\nu^2=\|\mathbf A^T\mathbf B\|_{\mathrm{HS}}^2. \tag{3.3}
\]

Expanding by two cells gives the coupled overlap identity

\[
 \boxed{
 \sum\nu^2
 =\sum_{z,z'}
   \left(\sum_xa_z(x)a_{z'}(x)\right)
   \left(\sum_yb_z(y)b_{z'}(y)\right).}         \tag{3.4}
\]

The missing theorem is therefore a \(K\)-scaled product bound for two
different cross-cell overlaps.  A separate estimate for either factor is
too strong on the stored examples; their coupling is essential.

## 4. Fixed-cell normal form and overlap displacements

For \(z=(b,\ell)\), write a record as in the cross-switched note:

\[
 (R_0,\ldots,R_6)=
 (b+t+Je,\ b,\ b+t,\ \ell+e+t,\ \ell+e,
  \ell+(I+J)t,\ \ell).                         \tag{4.1}
\]

Compare records in cells \((b,\ell)\) and
\((b+\delta,\ell+\varepsilon)\), and let their parameter increments be
\((\tau,\eta)\).

If their \(R_0\) values agree, then

\[
 \delta+\tau+J\eta=0.                          \tag{4.2}
\]

The seven role displacements are exactly

\[
 \boxed{
 (0,\ \delta,\ -J\eta,
 \ \varepsilon+\eta-\delta-J\eta,
 \ \varepsilon+\eta,
 \ \varepsilon-(I+J)\delta+(I-J)\eta,
 \ \varepsilon).}                             \tag{4.3}
\]

If their \(R_3\) values agree, then

\[
 \varepsilon+\eta+\tau=0,                     \tag{4.4}
\]

and the role displacements are

\[
 \boxed{
 (\delta-\varepsilon+(J-I)\eta,
 \ \delta,\ \delta-\varepsilon-\eta,
 \ 0,\ \varepsilon+\eta,
 \ -J\varepsilon-(I+J)\eta,\ \varepsilon).}  \tag{4.5}
\]

Every entry in (4.3)--(4.5) is a difference of two members of \(D\), hence
lies in \(D-D=D+D\).  The two overlap factors in (3.4) use (4.3) and
(4.5) with the same cell displacement \((\delta,\varepsilon)\).  This is
the exact physical-space coupling that a proof of (1.2) must exploit.

## 5. Exact stress profiles

The verifier reports

\[
 (N,S,\mathcal O_K,M_K,|\operatorname{supp}\nu|,
   \sum\nu^2,\max\nu,
   {\sum\nu^2\over K M_K}).
\]

The stored genuine profiles are

\[
\begin{array}{c|r|r|r|r|r|r|r|c}
\text{family}&N&S&\mathcal O_K&M_K&|\supp\nu|&\sum\nu^2&\max\nu&
 \sum\nu^2/(KM_K)\\ \hline
\text{closure }30&871&62273&1420&1496&1438&1620&3&0.01515\\
\text{Costas }11&91&707&2264&4348&1852&21656&22&0.64108\\
\text{Costas }13&133&969&3450&5530&2894&21922&21&0.54411\\
\text{Costas }17&241&2299&20014&46212&14890&405768&45&0.92045\\
\text{Costas }19&307&2927&127002&468768&63670&6956264&69&1.55644\\
\text{Costas }23&463&4513&498674&3020644&167536&139264360&201&4.72995
\end{array}                                     \tag{5.1}
\]

For abstract radially unique transversals, the corresponding rows are

\[
\begin{array}{c|r|r|r|r|r|r|r|c}
\text{side}&N&S&\mathcal O_K&M_K&|\supp\nu|&\sum\nu^2&\max\nu&
 \sum\nu^2/(KM_K)\\ \hline
4&29&121&8330&111622&839&20001502&378&42.9463\\
6&53&253&93290&4120768&2807&8212347978&4369&417.489\\
8&83&431&555948&59454358&6887&719698871404&26158&2331.14
\end{array}                                     \tag{5.2}
\]

Thus (1.2), like the endpoint cross-switched theorem, cannot follow from
radial uniqueness and the affine record identities alone.  Complete
difference endpoint realization must control the coupled product (3.4),
even though the charge itself is written using literal elements of \(D\).

Run

    python3 phase2/loop/erdos1208/verify_same_midpoint_literal_d2_collision_gate.py
    python3 phase2/loop/erdos1208/verify_same_midpoint_literal_d2_collision_gate.py --extended
    python3 phase2/loop/erdos1208/verify_same_midpoint_literal_d2_collision_gate.py --radial-8

for the endpoint recovery, matrix identities, displacement systems, and
exact profiles.
