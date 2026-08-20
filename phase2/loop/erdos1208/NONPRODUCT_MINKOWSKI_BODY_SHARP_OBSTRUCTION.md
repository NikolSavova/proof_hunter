# Nonproduct Minkowski bodies cannot improve the CM disk constant

## 1. Verdict

Holding the live arithmetic covolume/root-discriminant input fixed, the
product-of-disks choice in the `Q(sqrt(1949))` CM/Eisenstein certificate is
sharp in the entire admissible volume-averaging and coordinatewise
divisor-switch framework.  This remains true if one allows

* an arbitrary bounded Borel body in `C^m`, with correlations between
  different embeddings;
* unequal diameter budgets at the embeddings; and
* an optimally anisotropic version of the one-sided ideal packing lemma.

If `B subset C^m` has volume `V` and coordinate projection diameters `D_j`,
then

\[
 \boxed{\left(\prod_{j=1}^mD_j^2\right)^{1/m}
        \ge {4\over\pi}V^{1/m}.}                    \tag{1.1}
\]

The generalized one-sided ideal packing depends on the body only through
the left side of (1.1).  Consequently, relative to the certificate's safe
covolume normalization, the effective CM constant is always at least

\[
 {4\over\pi}{\sqrt3\over2}={2\sqrt3\over\pi}.       \tag{1.2}
\]

Products of planar disks attain equality.  Thus neither a nonproduct body
nor correlated allocation can improve the exponent `0.49371148` through
this interface.  A further improvement would need genuinely new
field-specific lattice-point information, rather than translate averaging
by volume and norm-only ideal packing.

## 2. The projection-volume obstruction

Let

\[
 \mathcal B\subset\mathbb C^m
\]

be bounded and Borel with positive volume `V`.  Write `P_j(B)` for
its projection to the `j`th complex coordinate and let

\[
 D_j=\operatorname {diam}P_j(\mathcal B).
\]

Since

\[
 \mathcal B\subseteq\prod_{j=1}^mP_j(\mathcal B),
\]

monotonicity of product measure gives

\[
 V\le\prod_{j=1}^m\operatorname {area}P_j(\mathcal B). \tag{2.1}
\]

The planar isodiametric inequality gives

\[
 \operatorname {area}P_j(\mathcal B)
 \le {\pi\over4}D_j^2.                              \tag{2.2}
\]

Multiplying (2.2) and using (2.1) proves (1.1).  Notice that no convexity,
central symmetry, or product assumption was used.

Equality in (1.1) forces equality in both steps: up to null sets the body
fills the product of its projections, and every projection is a disk by
the equality case of the planar isodiametric theorem.  Thus the equality
bodies are products of disks.  Unequal radii are allowed, but they do not
change the geometric-mean constant.  If one insists on a common maximum
diameter instead, equal radii are optimal as well.

## 3. Anisotropic one-sided ideal packing

The preceding obstruction matches the exact arithmetic quantity; it is not
an artifact of using a common coordinate box.

Let `L` be totally real of degree `m`, let `a` be a nonzero integral ideal,
and let `Y_j>0`.  Put

\[
 Y=\left(\prod_{j=1}^mY_j\right)^{1/m},
 \qquad A=N(\mathfrak a)^{1/m}.                    \tag{3.1}
\]

Then

\[
 \boxed{
 |\mathfrak a\cap\prod_j[0,Y_j]|
 \le\left(1+{Y\over A}\right)^m.}                \tag{3.2}
\]

Indeed choose positive cell lengths

\[
 \delta_j={Y_jA\over Y},\qquad
 \prod_j\delta_j=N(\mathfrak a).                  \tag{3.3}
\]

Partition the `j`th interval into fewer than `1+Y_j/delta_j` half-open
cells.  Two ideal points in the same product cell would have nonzero
difference `gamma in a` satisfying

\[
 |N_{L/\mathbb Q}(\gamma)|
 <\prod_j\delta_j=N(\mathfrak a),                  \tag{3.4}
\]

contrary to ideal divisibility.  Since `Y_j/delta_j=Y/A`, (3.2) follows.

This allocation is optimal among all such rectangular partitions.  If
`t_j=Y_j/delta_j`, their product is fixed, and convexity of
`x -> log(1+e^x)` gives

\[
 \prod_j(1+t_j)\ge
 \left(1+\left(\prod_jt_j\right)^{1/m}\right)^m.  \tag{3.5}
\]

Thus correlated embedding budgets do not expose a hidden improvement in
the ideal-packing step.

## 4. Exact interface with squared distances

For two lattice points `z,z' in B`, put

\[
 \eta=(z-z')\overline{(z-z')}\in O_L.
\]

At the `j`th real embedding,

\[
 0<\sigma_j(\eta)=|z_j-z'_j|^2\le D_j^2.          \tag{4.1}
\]

Apply (3.2) with `Y_j=D_j^2`.  Define

\[
 S=V^{1/m},\qquad
 C_{\mathcal B}={ (\prod_jD_j^2)^{1/m}\over S}.   \tag{4.2}
\]

Then every occurrence of the disk constant in the divisor-switch master
inequality is replaced exactly by `C_B`, while the same-coset term depends
on the body through `V=S^m`.  Equation (1.1) says

\[
 C_{\mathcal B}\ge {4\over\pi}.                   \tag{4.3}
\]

More explicitly, for `a=M b`, with
`Mcal=N(M)^(1/m)` and `x=N(b)^(1/m)`, (3.2) becomes

\[
 |\mathfrak M\mathfrak b\cap\prod_j[0,D_j^2]|
 \le\left[
 {S\over\mathcal Mx}
 \left(C_{\mathcal B}+{\mathcal Mx\over S}\right)
 \right]^m.                                      \tag{4.4}
\]

Since `x<=Mcal`, the existing divisor sum and one-sided switch continue
verbatim with `C_B` in place of `4/pi`.  The right side is increasing in
`C_B`, so (4.3) is a sharp lower obstruction.

For the CM lattice in the live record, the arithmetic certificate supplies
the safe upper bound

\[
 \operatorname {covol}(O_K)^{1/m}
 \le {\sqrt3\over2}D_L.                           \tag{4.5}
\]

Consequently the **certified choice**

\[
 V=\left({\sqrt3\over2}D_L\right)^m n,
 \qquad
 S={\sqrt3\over2}D_L n^{1/m}                         \tag{4.6}
\]

has `V>=n covol(O_K)` and volume averaging guarantees at least `n`
lattice points in some translate.  (An upper bound for the covolume does
not assert that every admissible body must have this volume; (4.6) is the
uniform safe choice made by the live certificate.)  Equivalently one may
work in the explicit suborder `O_L[zeta_3]`, whose covolume is exactly
`((sqrt(3)/2)D_L)^m`.  Combining this fixed arithmetic normalization with
(4.3) gives exactly (1.2).  The product of disks used by the certificate
attains both the projection-volume inequality and the anisotropic packing
normalization.

There is no opportunity to improve by rotating across embeddings: such a
rotation destroys the coordinate identities
`sigma_j(eta)=|z_j-z'_j|^2` required by the norm divisor switch.  Separate
coordinate scalings and permutations remain admissible, but (1.1) is
invariant under them.

## 5. Scope of the obstruction

The theorem closes precisely the proposed shape/allocation refinement.  It
does not rule out an argument using extra information about the actual
Minkowski lattice, for example:

* a translate with many more lattice points than the volume average;
* ideal-lattice successive minima beyond the product norm bound; or
* a counting method retaining correlations of the algebraic conjugates
  rather than enclosing them in a positive coordinate box.

Those would be new arithmetic inputs.  An arbitrary nonproduct body,
without such an input, can only increase the master constant.

In particular, the conclusion holds with the certificate's covolume input
fixed.  A sharper computation of the maximal-order covolume or root
discriminant would be an arithmetic improvement and is not ruled out by
this geometric obstruction.

## 6. Verification

Run

```text
python3 phase2/loop/erdos1208/verify_nonproduct_minkowski_body_obstruction.py
```

The verifier checks rigorous rational brackets for the sharp CM constant,
the exact anisotropic cell-allocation identities and smoothing inequality,
product-disk equality, and strict monotonicity of the endpoint right-hand
side in the shape constant.  Its output ends with

```text
nonproduct/correlated Minkowski-body improvement: SHARPLY OBSTRUCTED
```
