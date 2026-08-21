# Quadratic footprints for all three metric resonances

## 1. Outcome

The global six-gap Jacobian in
`SWAP_DECORATED_KEY_METRIC_TRANSVERSAL_GATE.md` vanishes on three material
populations.  This note proves that none of them is locally support-poor.
After fixing the repeated line coordinate, every resonance exposes a
quadratic-size translated footprint in `D+D`.

Work in one reverse endpoint group `(C,x,u)` and one oriented physical
endpoint role.  Write a reverse record as `(t,X)` and put

\[
 q=c-X,\qquad p=q+t,\qquad
 Y=H-JX+Jt,\qquad Z=H-JX+Lt=Y+t.                 \tag{1.1}
\]

The six vectors `X,X+u,Y,Y-Ju,Z,Z-Ju` lie in `D`, while `q,p,q-u,p-u`
are adaptive-popular.  In a fixed endpoint role, the set of neighbour
directions `t` is an affine image of a subset of the original point set;
it is therefore vector-Sidon.

For any fixed value of one of `q,p,Z`, let `T` be the set of `t` supporting
records with that value and put `h=|T|`.  There are three exact footprints:

\[
\begin{array}{c|c|c}
\text{fixed coordinate}&\text{footprint in }D+D&\text{support bound}\\ \hline
q&JT+LT&\ge h^2/2\\
p&T+T&\ge h^2/2\\
Z&(I-J)T-T&\ge h^2/2.
\end{array}                                        \tag{1.2}
\]

More precisely, the additive energy of every displayed pair of sets is at
most `2h^2-h`.  Thus the constant-`Z` Costas configuration which killed the
naive `Y+Z` support has not killed the resonance: its corrected `X+Y`
footprint is quadratic.

The theorem gives a conditional aggregate charge as well.  Partition
`q`-resonant collision edges into affine lines parallel to `u`; do the same
for `p`, and partition `Z`-resonant edges into lines parallel to `Ju`.
For one such line `ell`, let `h_a` be the multiplicity of a repeated
coordinate value `a`, let `r_ell` be the number of distinct values, and
let `H_ell=sum_a h_a`.  Then

\[
 \boxed{
 |E(\ell)|\le {H_\ell^2\over2}
 \le {r_\ell\over2}\sum_a h_a^2
 \le r_\ell\sum_a|\Phi_a|.}                     \tag{1.3}
\]

Fix `u=g w` with `w` primitive.  The coordinate boxes give

\[
 r_\ell\le1+{4m\over\|w\|_\infty}                \tag{1.4}
\]

for `q,p`, and `1+2m/||w||_infty` for `Z`.  Consequently any family of
resonant groups with this fixed `u` whose footprints have maximum global
depth `Delta_u` has

\[
 \boxed{
 E_{\rm res}
 \le 3\left(1+{4m\over\|\operatorname{prim}u\|_\infty}\right)
       \Delta_u |D+D|.}                            \tag{1.5}
\]

up to the fixed four-role factor if the roles have not already been
separated.  For varying `u`, sum the right side of (1.5) with its individual
`Delta_u`.  Multiple resonances may be counted more than once, which is
harmless for this upper bound.

This does not yet prove the final aggregate estimate: `Delta_u` can in
principle be large, and short primitive `u` gives a large line-capacity
factor.  It does remove local resonance collapse completely.  The remaining
resonant theorem is a depth/short-direction density increment in the same
`D+D` reservoir, rather than three unrelated exceptional cases.

## 2. Fixed `q`

Fixing `q` fixes `X=c-q`.  The formulas (1.1) give translated copies of
`JT` and `LT` inside `D`.  Hence a translate of `JT+LT` lies in `D+D`.
The energy equation is

\[
 Jt_1+Lt_2=Jt_3+Lt_4
 \quad\Longrightarrow\quad
 t_1-t_3=(I-J)(t_4-t_2).                            \tag{2.1}
\]

If one difference is zero then both are zero, giving `h^2` solutions.  If
it is nonzero, vector-Sidonicity gives at most one ordered right-hand pair
for each ordered left-hand pair, hence at most `h(h-1)` further solutions.
Thus the energy is at most `2h^2-h`, and Cauchy gives (1.2).

## 3. Fixed `p`

Here `q=p-t` and

\[
 X=(c-p)+t,\qquad Y=H-J(c-p),\qquad Z=Y+t.          \tag{3.1}
\]

Therefore a translate of `T+T`, for example the cross-sums `X_{t_1}+Z_{t_2}`,
lies in `D+D`.  Its energy equation is the ordinary Sidon relation

\[
 t_1+t_2=t_3+t_4.                                  \tag{3.2}
\]

The diagonal contributes `h^2`, and every nonzero directed difference has
at most one ordered representation.  Again the energy is at most
`2h^2-h`.

## 4. Fixed `Z`

This is the branch missed by the earlier cross-support.  Solving (1.1)
with `Z` fixed gives

\[
 Y=Z-t,qquad
 X=-J(H-Z)+(I-J)t.                                 \tag{4.1}
\]

Thus a translate of `(I-J)T-T`, realized by the cross-sums
`X_{t_1}+Y_{t_2}`, lies in `D+D`.  Its energy equation is

\[
 (I-J)(t_1-t_3)=t_2-t_4.                           \tag{4.2}
\]

There are `h^2` zero-difference solutions.  For each of the `h(h-1)`
nonzero ordered pairs `(t_1,t_3)`, vector-Sidonicity of `T` gives at most
one ordered pair `(t_2,t_4)` with the required vector difference.  This
again proves the `2h^2-h` energy bound.

## 5. Line aggregation

For the `q` resonance, two records are adjacent only if their `q` values
lie on one affine line parallel to `u`.  All pairs inside the line form an
upper envelope for the actual collision edges, proving the first inequality
in (1.3).  Cauchy gives the second; Sections 2--4 give the third.  The `p`
and `Z` cases are identical.

The shifts `q,p` lie in the box `[-2m,2m]^2`.  Consecutive lattice points
on a line parallel to `u` differ by the primitive vector `w`, proving the
first line-capacity bound in (1.4).  Since `Z in D subset [-m,m]^2`, its
bound has `2m` instead of `4m`.  Summing footprint incidences and using the
maximum depth proves (1.5).

## 6. Exact stress and scope

The recursive collision mass splits by exact resonance mask as follows:

| family | nonresonant | `q` only | `p` only | `D` only | overlaps |
|---|---:|---:|---:|---:|---:|
| Costas 17 | 0 | 0 | 0 | 0 | 4 |
| Costas 23 | 1,520 | 1,032 | 1,116 | 604 | 2,008 |
| Costas 29 | 20,792 | 11,894 | 13,640 | 6,636 | 18,524 |
| Costas 31 | 6,902 | 5,474 | 4,458 | 2,826 | 10,244 |

Here `D` denotes the complete-difference-vector resonance and `overlaps`
collects masks with two active factors.  No stored row has all three
factors zero.  The resonant mass is therefore material, but every part is
covered by the three footprints above.

For the genuine Costas-23 two-record row from the completion-box note,
`Z` is constant.  The failed `Y+Z` support has size two, whereas the
corrected set

\[
 \{X_i+Y_j:1\le i,j\le2\}
\]

has size four, exactly the quadratic footprint predicted by Section 4.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_resonant_line_footprint_packing.py
```

The verifier exhausts the three energy identities on random vector-Sidon
sets, checks the line-class aggregation inequality, verifies the lattice
line-capacity constants, and reproduces the corrected four-point support on
the genuine Costas-23 row.  The optimal-core analyzer independently checks
that the exact resonance-mask masses sum to the recursive collision mass.
