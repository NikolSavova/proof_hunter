# Dense perpendicular rulers kill the orthogonal energy-product gate

## 1. Verdict

The proposed uncertainty inequality

\[
 \mathcal E_+(D)\mathcal E_\perp(D)\le |D|^{5+o(1)}
 \tag{1.1}
\]

is false by a full power, even when `D=A-A` for an integral planar
distance-Sidon set.  There are arbitrarily large such sets for which, with
`N=|D|`,

\[
 \mathcal E_+(D)\gg N^3,
 \qquad
 \mathcal E_\perp(D)\gg N^3.                   \tag{1.2}
\]

Consequently their product is `Omega(N^6)`.  The counterexample is the
already-certified dense perpendicular-ruler family; the earlier
energy-product audit omitted it.

This does **not** disprove the support-sensitive target

\[
 \mathcal E_\perp(D)\le N^{1+o(1)}|D+D|.       \tag{1.3}
\]

The same ruler family has essentially maximal ordinary support, and (1.3)
is of exactly the right scale on it.

## 2. The distance-Sidon family

Fix `s`.  Choose a prime `p` with

\[
 2s\le p<4s
\]

and use the classical Erdos--Turan ruler

\[
 z_i=2pi+(i^2\bmod p),\qquad 0\le i<2s.        \tag{2.1}
\]

The set `Z={z_i}` is Sidon.  Indeed, equality of two unordered sums first
forces equality of the index sums because the residues in (2.1) lie in
`[0,p)`.  Reducing the remaining equality modulo `p` then gives equality of
the index products, so the two unordered index pairs coincide.

Split `Z=X disjoint-union Y`, with `|X|=|Y|=s`.  Since the whole ruler is
Sidon, the positive differences inside `X` and inside `Y` are internally
unique and disjoint from one another.  Also `Z` lies in `[0,L]` with

\[
 L<4ps<16s^2.                                   \tag{2.2}
\]

For an integer `C`, put

\[
 A_C=\{(x,0):x\in X\}\cup\{(0,C+y):y\in Y\}.  \tag{2.3}
\]

Some integer `C` makes `A_C` distance-Sidon.  Internal distances are unique
and mutually disjoint by the ruler property.  A cross squared distance is

\[
 x^2+(C+y)^2.                                   \tag{2.4}
\]

Two different cross edges give different polynomials in `C`: equality of
their linear coefficients gives the same `y`, and equality of the constant
terms then gives the same nonnegative `x`.  A cross polynomial is also not
identically an internal constant.  Only finitely many integers `C` are
therefore forbidden.  Translation places the resulting set in an integer
square.

## 3. Both energies are cubic

Put

\[
 P=X-X,\qquad Q=Y-Y,
 \qquad M=|P|=|Q|=s(s-1)+1.                    \tag{3.1}
\]

The complete difference set `D=A_C-A_C` contains the horizontal and vertical
copies

\[
 P\times\{0\}\subset D,
 \qquad
 \{0\}\times Q\subset D.                     \tag{3.2}
\]

Writing `R_S(t)=|{(u,v) in S^2:u-v=t}|`, (3.2) gives

\[
 R_D((t,0))\ge R_P(t),
 \qquad
 R_D((0,t))\ge R_Q(t).                         \tag{3.3}
\]

Since `P,Q subset [-L,L]`, Cauchy--Schwarz yields

\[
 \sum_tR_P(t)^2
 \ge {M^4\over |P-P|}
 \ge {M^4\over 4L+1},                         \tag{3.4}
\]

and

\[
 \sum_tR_P(t)R_Q(t)
 =E^+(P,Q)
 \ge {M^4\over |P+Q|}
 \ge {M^4\over 4L+1}.                         \tag{3.5}
\]

Equations (3.3)--(3.5) imply

\[
 \mathcal E_+(D),\ \mathcal E_\perp(D)
 \ge {M^4\over4L+1}
 \gg s^6.                                      \tag{3.6}
\]

Here `|A_C|=2s`, and distance-Sidonicity gives

\[
 N=|D|=2s(2s-1)+1=\Theta(s^2).                 \tag{3.7}
\]

Thus (3.6) is exactly (1.2), and

\[
 {\mathcal E_+(D)\mathcal E_\perp(D)\over N^5}
 \gg s^2\asymp N.                              \tag{3.8}
\]

This is an exponent-level counterexample, not a constant-factor defect.

## 4. Correct research consequence

The failed implication used the lower bound
`E_+(D)>=N^4/|D+D|` as if high ordinary energy detected small ordinary
support.  Dense perpendicular rulers show the converse can fail maximally:
`E_+(D)` is cubic even though `|D+D|` is essentially quadratic.

The live global target therefore remains (1.3), or the equivalent two-support
product.  Any replacement for (1.1) must retain `|D+D|` explicitly or use a
truncated/popular energy which cannot be saturated by a small structured
portion of `D` while the rest of `D+D` is large.

Run `verify_orthogonal_energy_product_ruler_barrier.py` for exact ruler,
distance, and energy checks.
