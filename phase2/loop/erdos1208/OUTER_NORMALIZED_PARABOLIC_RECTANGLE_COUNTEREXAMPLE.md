# A polynomial-height parabolic-rectangle counterexample to the direct outer-normalized gate

## 1. Verdict and scope

The last proposed high-codegree endpoint gate,

\[
 \boxed{
 \mathfrak N_{\rm tr}(W)
 =\sum_C{T(C)\over c(p_C)}
   \bigl(W_{r(p_C),N}+W_{-r(p_C),N}\bigr)
 \le m^{o(1)}Nk^3,}                                  \tag{1.1}
\]

is false.  There are polynomial-height integral distance-Sidon sets for
which one Golomb-core source pair alone contributes

\[
 \boxed{\Omega(k^6)}                                  \tag{1.2}
\]

to the left side, while `Nk^3=Theta(k^5)`.

The metric component is a rank-two parabolic rectangle.  With only `4L`
points it realizes `L^2` determinant-qualified records at one scalar gap;
both the first-edge and partner-edge graphs are `K_(L,L)`.  Hence

\[
 U_N(r)=L^2,qquad
 W_{r,N}=W_{-r,N}=L^2(L-1)=\Theta(L^3).               \tag{1.3}
\]

Joining `L=Theta(n)` to the dense Golomb core gives

\[
 c(p)=\Theta(n^2),\quad O(p)=\Theta(n^3),\quad
 {T(C)\over c(p)}=\Theta(1),\quad W_{r,N}=\Theta(n^3),
                                                               \tag{1.4}
\]

which proves (1.2).

This does **not** refute the original scalar aggregate or Erdos Problem
1208.  The raw target-gap multiplicity is only `R_D(r)=Theta(n^2)`, so the
selected source pair contributes

\[
 c(p)R_D(r)=\Theta(n^4)<Nk^3=\Theta(n^5).             \tag{1.5}
\]

The failed factor is exactly the endpoint-wedge amplification from
`R_D(r)` to `W_(r,N)`, which adds a factor `Theta(n)` on the complete
bipartite graph.  The proof architecture must return to the original raw
scalar aggregate rather than any one-role physical-wedge majorant.

## 2. The parabolic rectangle identity

Fix an even nonzero integer `r` and an integer `lambda>=2`.  For a row
parameter `t`, put

\[
 p_t=\bigl(2(\lambda^2-1)t^2-2t,\ 2t\bigr),           \tag{2.1}
\]

and define

\[
\begin{aligned}
 A_t&=(r/2,1)+p_t,\\
 B_t&=(r/2-1,0)+(p_{t,1},\lambda p_{t,2}).             \tag{2.2}
\end{aligned}
\]

For a column parameter `u`, put

\[
 s_u=\bigl(2(\lambda^2-1)u^2-2\lambda u,\ 2\lambda u\bigr),
                                                               \tag{2.3}
\]

and define

\[
 Y_u=s_u,qquad Z_u=(s_{u,1},s_{u,2}/\lambda).        \tag{2.4}
\]

All coordinates are integral.  Let

\[
 R=\begin{pmatrix}1&0\\0&\lambda\end{pmatrix},qquad
 \alpha=(r/2,1),\qquad\beta=(r/2-1,0).               \tag{2.5}
\]

The row choice (2.1) gives

\[
 |\alpha+p_t|^2-|\beta+Rp_t|^2=r,                    \tag{2.6}
\]

because its nonconstant part is

\[
 2p_{t,1}+2p_{t,2}+(1-\lambda^2)p_{t,2}^2=0.         \tag{2.7}
\]

The column choice gives

\[
 |s_u|^2-|R^{-T}s_u|^2
 -2\alpha\mathbin\cdot s_u
 +2\beta\mathbin\cdot R^{-T}s_u=0.                  \tag{2.8}
\]

Finally

\[
 p_t\mathbin\cdot s_u=(Rp_t)\mathbin\cdot(R^{-T}s_u). \tag{2.9}
\]

Adding (2.6)--(2.9) proves the complete rectangle identity

\[
 \boxed{|A_t-Y_u|^2-|B_t-Z_u|^2=r}                   \tag{2.10}
\]

for every pair `(t,u)`.

Choose `L` distinct row parameters and `L` disjoint column parameters.
The first edges `{A_t,Y_u}` form `K_(L,L)`; the partner edges
`{B_t,Z_u}` form another `K_(L,L)`.  Both projections are injective once
the final set is distance-Sidon.  The endpoint-wedge count of `K_(L,L)` is

\[
 2L{L\choose2}=L^2(L-1),                              \tag{2.11}
\]

which gives (1.3), provided the determinant cutoff is met.

## 3. Polynomial-height distance-Sidon specialization

The rectangle relations do not force any equality between two distinct
edge lengths.  This can be seen without a probabilistic or transcendental
specialization.

Treat `lambda`, the `L` row parameters, and the `L` column parameters as
independent variables.  Every squared distance among the four role
families (2.2)--(2.4) is a polynomial of bounded degree.  For two distinct
unordered physical edges:

* if their parameter supports differ, a parameter occurring in only one
  edge occurs to degree four, with nonzero leading coefficient
  `4(lambda^2-1)^2`;
* equal two-parameter supports have only three possible types: row--row,
  column--column, and row--column.  In each type there are four role
  choices.  They are pairwise different polynomials because at the single
  specialization

  \[
   (\lambda,r,x,y)=(2,2,1,3)                         \tag{3.1}
  \]

  their squared-distance values are respectively

  \[
  \begin{array}{c|c}
  \text{support type}&\text{four role values}\\ \hline
  \text{row--row}&1952,1930,2034,2000\\
  \text{column--column}&1664,1604,1700,1616\\
  \text{row--column}&1450,1378,1508,1448.
  \end{array}                                        \tag{3.2}
  \]

  All four entries in each row are distinct.

There is only one physical edge on an equal singleton support (`A_xB_x`
or `Y_xZ_x`), and row and column parameters are independent variables.
Thus (3.1)--(3.2), together with the support argument, cover every pair of
distinct edges for arbitrary `L`.  Notice that the universal rectangle
relation (2.10) is a nonzero **difference** of two lengths, never an
equality.

Thus every unwanted equality of two squared distances is a nonzero
bounded-degree polynomial.  Repeated points and parameter coincidences are
handled by the same argument.  There are only `L^(O(1))` bad polynomials.
The grid nonvanishing lemma supplies distinct integer parameters and an
integer `lambda`, all of size `L^(O(1))`, avoiding their union.

The companion verifier checks the role table (3.2) and also gives an
interpolation stress test.  Squared distances have degree at most two in
`r` and four in `lambda`; evaluation on a `3 by 5` grid therefore
determines them after the row/column parameters are fixed.  For
`L=2,4,8,16,32`, all `binom(4L,2)` evaluation vectors are distinct.  This
finite interpolation is only an audit; the arbitrary-`L` proof is the
independent-parameter support lemma above.

For a forced record in (2.10), the doubled cross determinant is a nonzero
integer polynomial.  One may add its zero set to the avoidance list.  At
the end, globally dilate every point by an integer larger than the final
`N`; this preserves all clean and scalar identities and makes every forced
absolute doubled determinant exceed `N`.  The construction remains at
polynomial height.

## 4. Joining the dense clean core

Take the `n`-point dense Golomb core used in the previous counterexamples.
It supplies an ordered source pair `p=(s,t)` with

\[
 c_0(p)\ge\alpha n^2,qquad O_0(p)\ge\beta n^3,       \tag{4.1}
\]

and every old one-role base has `c_0-O(n)` fully transverse old third
translations.

Scale the core by `6z` and choose the source orientation so that

\[
 r=-{\delta(s)-\delta(t)\over18}                     \tag{4.2}
\]

is the even nonzero scalar used in Section 2.  The factor `6z` makes this
automatic.  The rectangle parameters, `z`, and the relative translation
between the core and rectangle may be chosen simultaneously by finite
avoidance.  Cross-component repeated distances are again nonzero
quadratic equations in the relative translation.  Consequently the whole
union is an integral distance-Sidon set of height

\[
 m=n^{O(1)}.                                          \tag{4.3}
\]

Distance-Sidonicity also gives unordered pair-sum uniqueness: two distinct
equal pair sums would be the opposite sides of a parallelogram and hence
would give two distinct equal edge lengths.

Let `L=floor(delta n)` for a sufficiently small absolute `delta>0`.  The
`4L` rectangle points create

\[
 E_{\rm new}
 ={n+4L\choose2}-{n\choose2}=O(\delta n^2)           \tag{4.4}
\]

new pair sums.  A new common-clean translation for the old source pair
must use one of these sums in at least one target role, so

\[
 c_1(p)\le c_0(p)+2E_{\rm new}.                       \tag{4.5}
\]

Choose `delta` so that `2E_new<=c_0/4`.  Every old base retains at least
`c_0-O(n)>=c_1/2` old transverse translations.  Hence `Theta(n^3)` old
bases remain transverse-rich and obey

\[
 {T(C)\over c_1(p)}\ge{1\over2}.                     \tag{4.6}
\]

## 5. Failure of the outer-normalized gate

For every surviving old base, (2.11) gives

\[
 W_{r,N}+W_{-r,N}\ge2L^2(L-1)=\Theta(n^3).           \tag{5.1}
\]

Combining (4.1), (4.6), and (5.1), the contribution of this single source
pair is

\[
\begin{aligned}
 \mathfrak N_{\rm tr}(W;p)
 &=\sum_{C\text{ old at }p}{T(C)\over c_1(p)}
    \bigl(W_{r,N}+W_{-r,N}\bigr)\\
 &\ge \Omega(n^3)\,{1\over2}\,\Omega(n^3)
  =\boxed{\Omega(n^6)}.                               \tag{5.2}
\end{aligned}
\]

The final `k=n+4L=Theta(n)` and `N=Theta(n^2)`, so

\[
 m^{o(1)}Nk^3=n^{5+o(1)}.                             \tag{5.3}
\]

Equations (5.2)--(5.3) disprove (1.1) by a full factor
`n^(1-o(1))`.  The same example defeats every terminal
`c(p)^(-ell)` synchronized-pool target at `Nk^3`: on a rich base,
`c^(-ell) binom(T,ell)=Theta(1)`, so its contribution still has the
`n^3*n^3=n^6` scale.

## 6. Why the original scalar aggregate survives this attack

The physical endpoint wedge is the source of the false extra factor.  The
rectangle contains only `L^2` ordered distance-gap records at `r`, so

\[
 R_D(r)=\Theta(L^2)=\Theta(n^2),qquad
 W_{r,N}=\Theta(L^3)=\Theta(n^3).                     \tag{6.1}
\]

At the selected Golomb source pair,

\[
 c(p)R_D(r)=\Theta(n^2)\Theta(n^2)=\Theta(n^4),       \tag{6.2}
\]

one factor `n` below `Nk^3=Theta(n^5)`.  In particular, neither this note
nor its verifier claims a counterexample to

\[
 \sum_q\mathcal X_q\le m^{o(1)}Nk^3.                 \tag{6.3}
\]

The endpoint-rich reduction was irreversible: replacing raw scalar-gap
multiplicity by endpoint wedges can cost a full power even after common-q,
codegree, transversality, and reciprocal normalization are all retained.

## 7. Exact certificate

The verifier uses the stored 60-mark Ruzsa core, dilated by `1,000`, and
an 8-by-8 rectangle with `lambda=10` at scalar
`r=-2,673,600,000,000`.  A generic integral translation joins the two
components.  The resulting 92-point set has all 4,186 squared distances
and pair sums distinct.  Its exact profile is

\[
\begin{array}{c|r}
\text{quantity}&\text{value}\\ \hline
k,N&92,\ 4,186\\
\#\text{ clean fibres},H&3,676,\ 1,322,550\\
c(p)&320\\
O(p),\ \#\text{ rich bases}&6,169,\ 6,169\\
\min T(C),\max T(C)&182,\ 245\\
\sum_CT(C)&1,313,335\\
\sum_C{T(C)\choose2}&139,373,896\\
U_N(r),W_{r,N}&64,\ 448\\
U_N(-r),W_{-r,N}&64,\ 448\\
R_D(r),R_D(-r)&64,\ 64\\
W_{r,N}+W_{-r,N}&896\\
\sum_C(W_r+W_{-r})&5,527,424\\
\sum_C(T(C)/c)(W_r+W_{-r})&3,677,338\\
Nk^3&3,259,587,968\\
\max|\text{coordinate}|&537,866,126,862,120.
\end{array}                                           \tag{7.1}
\]

The finite instance is a structural shadow; fixed constants dominate at
`n=60`.  The verifier checks the symbolic distance-polynomial
interpolation, global distance and pair-sum Sidonicity, all 64 forward
scalar identities and determinants, both qualified endpoint graphs, every
clean fibre, and the exact outer-normalized mass.

Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_outer_normalized_parabolic_rectangle_counterexample.py
```

## 8. Consequence for the proof architecture

Every high-codegree route through `W_(r,N)` is now ruled out, including
fixed-wedge localization, global fixed-order pooling, actual-codegree
normalization, terminal outer-normalized pools, and partner-synchronized
complete-bipartite extraction.  The parabolic rectangle is itself the
large synchronized block which the proposed DRC was meant to find, and it
has polynomial height.

The direct attack must restart from the raw scalar identity, where this
example costs `R_D(r)=Theta(k^2)` rather than
`W_(r,N)=Theta(k^3)`.  Any future endpoint decoration must be averaged or
charged without replacing each scalar record by all pairs of records
sharing an endpoint.
