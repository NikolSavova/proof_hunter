# A universal two-arm barrier to bilinear edge charges

## 1. Verdict

The natural scalar edge-vector charge does not solve the clean pair-sum
gate.  Fix an integer `C` and orient the canonical edge vectors represented
by `s in H_q` and `t in Sigma` as `u_s,v_t`.  Put

\[
 \mathcal B_C(u,v)
 =u\cdot v+C\det(u,v).                           \tag{1.1}
\]

It has only `O_C(m^2)` possible integer values, so a near-diagonal second
moment would imply the cube-root bound exactly as for the metric scalar
charge.  Nevertheless, for every fixed `C` there are arbitrarily large
integral distance-Sidon sets, a realized clean fibre of constant positive
size, and a charge fibre containing `Theta(k^2)` records.  Its normalized
energy is `Omega(k^2)`.

Thus retaining an edge direction through one fixed bilinear functional is
not enough.  This barrier does **not** apply to
`delta(s)+C delta(t)`: the latter separates the Golomb-ruler edge lengths.

## 2. A fixed clean gadget

Use the six integer points

\[
\begin{aligned}
 a&=(0,2),&b&=(2,31),\\
 c&=(17,25),&d&=(70,14),\\
 e&=(39,9),&f&=(46,1).
\end{aligned}                                    \tag{2.1}
\]

They form a distance-Sidon set: their fifteen squared distances are

\[
 845,818,5044,1570,2117,261,4913,1853,2836,2930,
 740,1417,986,745,113,
\]

which are pairwise distinct.  Moreover

\[
 q=a-b=(-2,-29),qquad
 c+d+q=e+f,                                      \tag{2.2}
\]

and all six labels are distinct.  Hence `s=c+d` is a clean member of
`H_q`.  Orient its source edge as

\[
 u=c-d=(-53,11).                                 \tag{2.3}
\]

For the fixed coefficient `C`, define

\[
 v_C=(u_y+Cu_x,-u_x+Cu_y)
     =(11-53C,53+11C).                           \tag{2.4}
\]

A direct calculation gives

\[
 \mathcal B_C(u,v_C)=0.                          \tag{2.5}
\]

## 3. Add a large null-direction ruler

Let `R={r_1,...,r_s}` be an integral Golomb ruler and add an affine copy

\[
 P_j=T w+Lr_jv_C.                               \tag{3.1}
\]

The integer parameters `L,w,T` can be chosen so that

1. the union of (2.1) and (3.1) is distance-Sidon; and
2. the only clean `q`-start is the fixed gadget start in (2.2).

Here is a complete finite-avoidance argument.  First choose `L` outside the
finite set for which an internal ruler distance collides with a gadget
distance or a cross pair-sum differs by `q`.  The vector `v_C` is never
parallel to `q`, since

\[
 \det(q,v_C)=213-1559C\ne0
\]

for integral `C`; hence no two ruler pair sums differ by `q`.  Next choose
an integral `w` outside the finitely many lines on which two prospective
cross-distance polynomials have the same linear coefficient.  Finally all
remaining forbidden distance collisions and pair-sum relations exclude
only finitely many values of `T`.  An integral `T` outside this set gives
both assertions.

Every one of the `binom(s,2)` ruler edges has oriented vector equal, up to
sign, to a nonzero integer multiple of `v_C`.  Equations (2.5) and
bilinearity put all records formed from the fixed clean source and these
ruler edges into the charge key zero.  The complete set has `k=s+6` points
and `N=Theta(s^2)` unordered edges, while `|H_q|=1`.  Therefore

\[
 \max_z|\mathcal B_C^{-1}(z)|\ge\binom s2,
\]

and

\[
 {\sum_z|\mathcal B_C^{-1}(z)|^2\over |H_q|N}
 \gg {s^4\over s^2}=s^2=\Theta(k^2).            \tag{3.2}
\]

This disproves the required near-diagonal estimate by a full quadratic
factor.

## 4. Exact finite certificates

The verifier instantiates the construction for `C=1,3,18,43` with an
eight-mark Erdős--Turán ruler.  In every row the resulting 14-point set is
distance-Sidon, the distinguished fibre has exactly one clean start, and

\[
 (|H_q|N,\mathcal E_C,\max\nu_C)=(91,1183,28).
\]

Thus the normalized energy is exactly `13`, already far from diagonal at
this small size.

Run

```text
python3 phase2/loop/erdos1208/verify_bilinear_edge_charge_barrier.py
```

## 5. Consequence

Do not replace the live metric scalar charge by a fixed dot, determinant,
or linear combination of the two.  A finite collection of such charges can
be defeated by adding the corresponding finite collection of ruler arms;
that construction then lies in the already-solved subpolynomial
parallel-line branch.  Any adaptive version would therefore need a genuine
many-direction dichotomy, not another fixed bilinear moment.
