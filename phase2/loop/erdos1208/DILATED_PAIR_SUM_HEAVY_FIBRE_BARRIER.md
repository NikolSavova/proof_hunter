# Dilated pair-sum support gate and a sharp heavy-fibre barrier

## 1. A second exact route to the cube-root bound

Let `A` be a finite distance-Sidon subset of the integer plane, let

\[
 k=|A|,\qquad J(x,y)=(-y,x),\qquad L=I+J,
\]

and put

\[
 U_A=2A-LA=\{a_1+a_2-La_3:a_1,a_2,a_3\in A\}.
\]

If `A` lies in an `m` by `m` grid, then `|U_A|=O(m^2)`.  Consequently the
support estimate

\[
 \boxed{|2A-(I+J)A|\ge k^{3-o(1)}}                 \tag{1.1}
\]

would imply

\[
 k\le m^{2/3+o(1)},
\]

which is the expected square-grid upper order and would close the direct
route to Erdos #1208.  Exact tests on Costas permutations, additive
closures, and perpendicular Golomb-ruler families give support of constant
order `k^3`; this is evidence only, not a proof of (1.1).

The natural energy proof of (1.1) would try to control collisions of

\[
 (a_1,a_2,a_3)\longmapsto a_1+a_2-La_3.
\]

Writing `D=A-A`, every collision satisfies

\[
 x+y=Ld,\qquad x,y,d\in D.                         \tag{1.2}
\]

A tempting local substitute is a subquadratic pointwise bound for the
dilated overlap

\[
 R_D(Ld)=|D\cap(D+Ld)|.
\]

The theorem below rules out that substitute as strongly as possible.

## 2. Quadratic heavy fibres occur in genuine distance-Sidon sets

**Theorem 2.1 (diagonal ruler plus one popular horizontal edge).** There
are arbitrarily large integral planar distance-Sidon sets `A`, with
`k=|A|`, and nonzero `d in D=A-A` for which

\[
 R_D((I+J)d)=\Omega(k^2).                           \tag{2.1}
\]

At the same time these examples contain an explicitly injective family of
`Theta(k^3)` triples in `2A-(I+J)A`.

**Proof.** Let `R` be an `s`-mark integral Golomb ruler of length
`O(s^2)`.  Thus all its nonzero ordered differences are distinct, and

\[
 P=R-R,
 \qquad |P|=s(s-1)+1=\Theta(s^2).
\]

For `h in Z`, write

\[
 r_P(h)=|\{(x,y)\in P^2:x-y=h\}|.
\]

The support `P-P` lies in an interval of length `O(s^2)`, whereas

\[
 \sum_{h\ne0}r_P(h)=|P|^2-|P|=\Theta(s^4).
\]

Hence some nonzero `h` satisfies `r_P(h)=Omega(s^2)`.  Replacing `h` by
`-h` if necessary, take `h>0`.

For an integer `C` to be selected, define

\[
 A_C=\{(0,0),(h,0)\}
     \cup\{(C+r,C+r):r\in R\}.                     \tag{2.2}
\]

All diagonal-diagonal squared distances are `2(r-r')^2` and are distinct,
because `R` is a Golomb ruler.  The horizontal squared distance is `h^2`,
which cannot equal `2q^2` for a nonzero integer `q`.  A cross squared
distance from `(e,0)`, where `e in {0,h}`, to `(C+r,C+r)` is

\[
 f_{e,r}(C)=(C+r-e)^2+(C+r)^2.                     \tag{2.3}
\]

These quadratic polynomials are pairwise distinct.  For the same `e`, the
linear coefficient recovers `r`.  For different endpoints, equality of
the linear coefficients would force `r'=r+h/2`; after substitution the
constant coefficients differ by `h^2/2`.  No cross polynomial is constant.
Therefore all unwanted equalities exclude only finitely many values of
`C`, and an integral `C` can be chosen so that `A_C` is distance-Sidon.

Now `(h,0)=d in D`, and

\[
 Ld=(h,h).
\]

For every representation `x-y=h` with `x,y in P`, the two diagonal
differences `(x,x),(y,y)` belong to `D` and differ by `(h,h)`.  Thus

\[
 R_D(Ld)\ge r_P(h)=\Omega(s^2)=\Omega(k^2),
\]

proving (2.1).

The same example nevertheless has cubic pair-sum support.  Put
`T=(C,C)` and `g_r=T+(r,r)`.  For `r_1,r_2,r_3 in R`,

\[
 g_{r_1}+g_{r_2}-Lg_{r_3}
 =2T-LT+(r_1+r_2,\ r_1+r_2-2r_3).                 \tag{2.4}
\]

The first coordinate recovers `r_1+r_2`, which recovers the unordered pair
`{r_1,r_2}` by the Sidon property of `R`; the second coordinate then
recovers `r_3`.  Hence (2.4) gives exactly

\[
 |R\mathbin{\oplus}R|\,|R|
 =\frac{s^2(s+1)}2=\Theta(k^3)                    \tag{2.5}
\]

distinct elements of `2A_C-LA_C`.  This completes the proof.

## 3. Consequence for the live #1208 attack

The theorem separates two notions which a naive energy proof conflates:

* an individual dilation fibre can be fully quadratic, even for a genuine
  integral distance-Sidon set; but
* the same structured piece can make a cubic contribution to the image
  support.

Therefore no pointwise estimate of the form

\[
 R_D((I+J)d)\le k^{2-\epsilon}
\]

can prove (1.1), for any fixed `epsilon>0`.  A viable proof must compensate
heavy fibres by transverse image growth, or use a size-biased/averaged
endpoint charge.  This agrees with the current swap-cell gate: maximum
degree is too strong, while the orientation-energy inequality can tolerate
small dense cores if they carry little total mass.

The companion verifier constructs five exact finite members, checks the
distance-Sidon property, the quadratic overlap, the full support, and the
exact cubic diagonal injection.
