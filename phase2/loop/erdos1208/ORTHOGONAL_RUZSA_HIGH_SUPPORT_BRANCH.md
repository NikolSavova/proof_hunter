# The Ruzsa high-support branch of the orthogonal product gate

## 1. Exact inequality

Let `D` be any finite centrally symmetric subset of a torsion-free abelian
group, let `J` be an automorphism, and put

\[
 N=|D|,\qquad S=|D+D|,\qquad T=|D+JD|.
\]

Then

\[
 \boxed{T^2\ge NS.}                              \tag{1.1}
\]

This does not use radial uniqueness or the representation `D=A-A`; it is a
direct instance of Ruzsa's triangle inequality.  Apply

\[
 |Y|\,|X-Z|\le |X-Y|\,|Y-Z|                    \tag{1.2}
\]

with

\[
 X=D,\qquad Y=JD,\qquad Z=-D.
\]

Since `D=-D` and hence `JD=-JD`, the three difference sets in (1.2) are

\[
 X-Z=D+D,\qquad X-Y=D+JD,\qquad Y-Z=JD+D.
\]

This proves (1.1).

For completeness, the underlying injection can be written explicitly.
For each `s in D+D`, fix one representation

\[
 s=d_s-(-e_s),\qquad d_s,e_s\in D.
\]

The map

\[
 (j,s)\longmapsto(d_s-j,\ j+e_s),
 \qquad (j,s)\in JD\times(D+D),                 \tag{1.3}
\]

lands in `(D-JD) x (JD+D)`, whose two factors both have cardinality `T`.
The sum of the two outputs is `s`, after which the fixed representation of
`s` recovers `d_s,e_s` and the first output recovers `j`.  Thus (1.3) is
injective and proves (1.1) without any black-box sumset theorem.

## 2. Consequence for Erdos 1208

Now let `A` be a planar distance-Sidon set of size `k` and put

\[
 D=A-A,\qquad N=k(k-1)+1.
\]

The live orthogonal product theorem asks for

\[
 ST\ge N^{3-o(1)}.                               \tag{2.1}
\]

Equation (1.1) gives the unconditional lower bound

\[
 ST\ge N^{1/2}S^{3/2}.                           \tag{2.2}
\]

Consequently (2.1) already holds whenever

\[
 \boxed{S\ge N^{5/3-o(1)}.}                     \tag{2.3}
\]

More quantitatively, if `S>=N^(1+sigma-o(1))`, then

\[
 ST\ge N^{2+3\sigma/2-o(1)}.                    \tag{2.4}
\]

For `A subset [m]^2`, both supports are `O(m^2)`.  Combining this ambient
upper bound with (2.4) gives

\[
 k\le m^{4/(4+3\sigma)+o(1)}
      =n^{2/(4+3\sigma)+o(1)},\qquad n=m^2.      \tag{2.5}
\]

At `sigma=2/3`, formula (2.5) is exactly the desired `n^(1/3+o(1))` bound.

Thus the full problem has a sharper surviving branch than the unrestricted
energy formulation alone suggests:

> It is enough to control distance-Sidon complete difference sets satisfying
> `|D+D|<N^(5/3-o(1))`.

The generic independent-segment constructions which kill maximum-fibre
statements lie in the already-solved high-support branch.  Their ordinary
support is essentially quadratic in `N`.  The transformed finite-field
parabola and dense ruler models remain in the low-support branch; there the
quarter-turned support, rather than (1.1), supplies the missing growth.

## 3. Relation to the parallel-cover theorem

The two rigorous branches now read

\[
 \begin{array}{ll}
 |D+D|\ge N^{5/3-o(1)}
   &\Longrightarrow |D+D||D+JD|\ge N^{3-o(1)},\\[2mm]
 A\text{ covered by }r=k^{o(1)}\text{ parallel lines}
   &\Longrightarrow |D+D||D+JD|\ge N^{3-o(1)}.
 \end{array}                                     \tag{3.1}
\]

The remaining configuration is simultaneously additively compressed and
wide: it has `|D+D|<N^(5/3-o(1))` and requires a fixed positive power of `k`
parallel layers in every direction to which the existing cover argument is
applied.  This is the correct domain for the common-energy inverse theorem or
the decorated-parallelogram moment estimate.

## 4. Verification

`verify_orthogonal_ruzsa_high_support.py` checks (1.1)--(2.4) exactly on the
closure, transformed-parabola, dense perpendicular-ruler, and exhaustive
small-grid distance-Sidon families.  The computation is only a regression
test; the proof is the injection (1.3).
