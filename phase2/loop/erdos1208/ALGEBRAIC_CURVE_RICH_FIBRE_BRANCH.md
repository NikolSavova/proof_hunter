# Algebraic-curve branch for adaptive rich fibres

## 1. Statement

Keep the notation of `SUPPORT_ADAPTIVE_RICH_FIBRE_GATE.md`.  Thus

\[
 D=A-A,\qquad S=|D+D|,\qquad L=I+J,
\]

and a rich fibre `Q=Q_K(u,s)` supplies the two affine copies

\[
 u+Q\subseteq D,
 \qquad
 w-LQ\subseteq D,
 \qquad w=s-u.                                  \tag{1.1}
\]

### Proposition 1.1

If `Q_0 subseteq Q` has `h` points on a real algebraic plane curve of total
degree `d`, then

\[
 \boxed{S\ge {h^2\over d^2},
 \qquad h\le d\sqrt S.}                       \tag{1.2}
\]

Consequently, if `Q` is covered by `r` curves, each of degree at most `d`,
then their union is a curve of degree at most `rd` and

\[
 \boxed{|Q|\le rd\sqrt S.}                    \tag{1.3}
\]

This contains the collinear branch from
`ADAPTIVE_RICH_FIBRE_STABILITY_LEDGER.md`: take a degree-one curve.

## 2. Proof

By (1.1), `D+D` contains the image of

\[
 \Psi:Q_0\times Q_0\longrightarrow\mathbb C^2,
 \qquad
 \Psi(q,q')=u+w+q-Lq'.                          \tag{2.1}
\]

First suppose `Q_0` lies on an absolutely irreducible component `C` of
degree `d`.  Fix an output `z`.  Any preimage satisfies

\[
 q\in C,
 \qquad
 q\in (z-u-w)+LC.                              \tag{2.2}
\]

The two degree-`d` curves in (2.2) have no common component.  Here is the
short reason this is automatic for a real curve with a one-dimensional real
locus.  A common component would give `C=t+LC`.  The affine map `x -> t+Lx`
has a unique fixed point; translate it to the origin.  If `f` defines `C`,
irreducibility gives `f(Lx)=c f(x)`.  In the complex coordinates
`z=x+iy`, `zbar=x-iy`, the map `L` has eigenvalues `1+i`, `1-i`.  Their
moduli show that every nonzero homogeneous part of `f` must have the same
degree, so `f` is homogeneous.  A homogeneous binary polynomial over the
complex numbers factors into lines.  Irreducibility leaves a line, but `L`
has no real eigenline.  The only real-irreducible exceptional cone has a
zero-dimensional real locus and is handled below.

Bezout's theorem now gives at most `d^2` possible values of `q`, counting
even complex intersections and multiplicities.  Once `q` is fixed, `q'` is
uniquely recovered from (2.1), since `L` is invertible.  Every fibre of
`Psi` consequently has size at most `d^2`, and

\[
 |D+D|\ge |\Psi(Q_0^2)|\ge h^2/d^2.
\]

For a general real degree-`d` curve, factor it into real-irreducible
components of degrees `d_i` and assign each point of `Q_0` to one component.
If a component has a one-dimensional real locus, the preceding argument
gives `h_i<=d_i sqrt(S)`.  Otherwise its real locus has at most `d_i^2`
points by intersection with a conjugate complex component; since
`S>=|u+Q_0|=h`, the same inequality follows.  Summing over the components
gives

\[
 h=\sum_i h_i\le\Bigl(\sum_i d_i\Bigr)\sqrt S
 \le d\sqrt S.
\]

This proves (1.2), and applying it to the product of `r` defining
polynomials proves (1.3).  QED.

## 3. Scope and the remaining obstruction

The theorem is a genuine stability branch, but it does not settle the rich
tail.  A two-dimensional Gaussian-lattice patch can have
`|Q-LQ|=O(|Q|)` and requires algebraic degree growing like `sqrt(|Q|)` to be
interpolated as a curve.  Thus the surviving fibres are precisely the
high-algebraic-complexity, rank-two models already identified by the
seven-incidence reduction.  Proposition 1.1 rules out a low-degree curve
escape; it does not yet rule out an approximate lattice.

## 4. Verification

`verify_algebraic_curve_rich_fibre_branch.py` checks the Cartesian image and
the `d^2` fibre bound on exact integer samples from lines,
parabolas, and cubics.  The mathematical proof is the Bezout argument above;
the script is a regression check on the signs and on the `I+J` transform.
