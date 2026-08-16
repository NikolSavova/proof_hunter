# Universal-chain wrappers do not give a sub-half construction

**Date:** 2026-08-14  
**Verdict:** no stretchable construction below coefficient `1/2` was found.
The most literal attempt to turn fixed-edge chain universality into an upper
construction is in fact fatal: coherent nesting over the same ordered pair
of tangent directions has an exact boundary recurrence and produces
`2^{Theta(N)}` convex subsets.  This remains true when the recursively
retained core has an arbitrary order type and arbitrarily low finite trace.

Changing the tangent direction at every wrapper avoids this recurrence, but
then the projective-universality map preserves the complete convex-face
profile of the retained core.  Consequently the reset component is again an
arbitrary instance of Erdős 838, and there is no closed upper recurrence.
This is an exact barrier to the coherent multi-pocket route, not a theorem
excluding every nonstationary nonvertical construction.

All counts below include the empty set.  Let `Z(P)` be the number of convex
subsets and let `C_hat(P),U_hat(P)` be the cap and cup counts including the
empty set, in a fixed generic left-to-right order.

## 1. Order-preserving universal-chain embedding

The existing projective-universality theorem can be strengthened without
changing its proof: the strict nesting chain can have the same horizontal
order as the input.

Write the input as `p_i=(a_i,b_i)` with `a_1<...<a_n`.  Choose `M` so that

```text
c_i=b_i+M a_i
```

is also strictly increasing.  Put

```text
L_i=C-a_i,                 R_i=D-c_i
```

with `D>max c_i`.  For sufficiently large `C`, all `L_i,R_i` are positive,
both sequences strictly decrease, and

```text
L_1/R_1 < L_2/R_2 < ... < L_n/R_n.                (1)
```

Indeed, after cross multiplication the coefficient of `C` in the required
inequality for `i<j` is `c_i-c_j<0`, so finitely many pairs are simultaneously
satisfied for large `C`.  Apply

```text
Phi(L,R)=((L-R)/(L+R), 2/(L+R)).                   (2)
```

Equation (1) says the first coordinates of the images increase with `i`.
The two tangent coordinates over

```text
u=(-1,0),                  v=(1,0)
```

are exactly `L_i,R_i`, so the images form a strict dominance chain.  The
homogeneous matrix of (2) has determinant `-4` and positive denominator on
the whole input hull.  Thus it reverses every orientation but preserves every
convex-position subset.  Integer `M,C,D` give rational coordinates.

## 2. Exact two-tangent wrapper recurrence

Let `X` be the image above and put

```text
T(P)={u,v} union X.                                      (3)
```

The points occur in the order `u,x_1,...,x_n,v`.  For `i<j`, direct
determinants give

```text
chi(u,x_i,x_j)=+,       chi(x_i,x_j,v)=-,
chi(u,x_i,v)=-.                                         (4)
```

Partition a face by its intersection with `{u,v}`.

* With neither guard, one has an arbitrary face of `X`, hence `Z(P)`
  possibilities.
* With `u` alone, (4) says precisely that the `X`-part is a cup of `X`.
  With `v` alone it is precisely a cap of `X`.
* With both guards, at most one point of `X` may occur, and every such choice
  is a cap/convex face.  This gives exactly `n+1` faces.

Because (2) reverses signs, caps and cups of the source are exchanged.  The
same four-case classification for boundary chains gives the exact recurrence

```text
n'       = n+2,
Z'       = Z+C_hat+U_hat+n+1,
C_hat'   = 2 U_hat+2(n+1),
U_hat'   = 2 C_hat+n+2.                              (5)
```

The asymmetry in the last two lines is real: `{u,x_i,v}` is a cap, not a cup.
In particular, for `S=C_hat+U_hat`,

```text
S'=2S+3n+4.                                           (6)
```

After `d` coherent wrappers, `n_d=n_0+2d`, while (6) gives

```text
S_d=Theta(2^d),                Z_d=Theta(2^d).        (7)
```

Thus, in terms of final cardinality `N`,

```text
log_2 Z_N = N/2+O(log N).                            (8)
```

This is exponentially larger than the desired `O((log N)^2)` trace.  The
conclusion does not assume any structure or lower bound on the retained
core: the seed may be an exact finite low-trace record, a sharp coefficient-
half construction, or an alleged better construction.

Adding a third generic point below `uv` only adds faces, so the same lower
barrier applies to actual triangular pockets.  More generally, any coherent
multi-pocket construction obtained by several applications of (3) is just a
longer run of (5); grouping wrappers into levels cannot change (8).

## 3. Why direction resets are not a construction yet

There is one exact loophole.  Before the next wrapper one may choose a new
generic projection order.  The old `C_hat,U_hat` bank then need not be the
new directional bank, so (5) no longer iterates.  However the projective map
still preserves `Z` rank by rank.  A reset therefore takes an arbitrary
retained order type `Q`, moves that same order type into a pocket, and adds
guards; it does not manufacture a new low-trace core.

Consequently a direction-reset scheme needs a separate theorem showing that
all the mixed faces created by `Theta(N)` incompatible wrapper directions
remain quasipolynomial.  No such recurrence is present in the universal-chain
geometry.  If only `o(N)` guard points are added, the retained core is
near-spanning and its normalized coefficient is inherited unchanged.  If a
linear number are added, the uncharged direction resets are precisely the
global cross-pocket compatibility problem which the lower decoder could not
compress.  Invoking low `Z` for every retained reset component simply assumes
the desired upper family at the new scale.

As a finite stress test, the verifier exhausts every generic projection
chamber at each of three successive levels and greedily chooses the direction
minimizing `C_hat+U_hat`.  Starting from the nine-point record, it obtains

```text
(n,Z,min(C_hat+U_hat)) =
  (9,169,199), (11,378,367), (13,757,614), (15,1385,1002).
```

Thus resets do weaken the coherent doubling, as they must, but the best exact
finite trajectory remains above coefficient `1/2` and gives no stationary
recurrence.  These four rows are evidence only; the all-depth theorem in this
note is (5)--(8), not an extrapolation of the reset search.

This also clarifies the macroscopic-mean escape in `agent_upper_jump`.  For a
genuine vertical split with logarithmic proportions `alpha,beta`, child
coefficient `c`, and induced-macro mean ratio `kappa=mu/log r`, the exact
support lower calculus contains

```text
c_out >= c(alpha^2+beta^2)+kappa alpha beta
       = c+(kappa-2c)alpha beta.                   (9)
```

A fixed point below `1/2` therefore requires the adversarial macro cores to
have a persistent linear deficit `kappa<=2c<1`.  Producing a scalable,
stretchable sequence with the needed full activity polynomial and endpoint
profiles is not achieved by the chain wrapper: coherent wrappers satisfy
(8), while direction resets return to an arbitrary core.  No candidate with
those properties was found.

## 4. Exact audit

Run

```bash
python3 phase2/loop/erdos838/agent_subhalf_construction_fresh/verify_chain_wrapper.py
```

The script starts from the exact rational nine-point trace minimizer
(`Z=169` including the empty set), constructs every wrapper with integer
`M,C,D`, checks all determinants and all nesting relations, recomputes the
full face profile by the independent reflection-order matrix evaluator, and
checks (5) through eight levels.  The first rows are

| depth | `n` | `Z` | `C_hat` | `U_hat` |
|---:|---:|---:|---:|---:|
| 0 | 9 | 169 | 116 | 91 |
| 1 | 11 | 386 | 202 | 243 |
| 2 | 13 | 843 | 510 | 417 |
| 4 | 17 | 3697 | 2102 | 1741 |
| 8 | 25 | 62061 | 34038 | 28341 |

It also audits the more permissive three-guard wrapper from the original
universality construction.  Those finite rows are not used for the all-depth
claim; the theorem is the symbolic recurrence (5)--(8).
