# The local transverse-overlap gate for Erdős #1208

## 1. Why this is a sharper target

Let `A` be a distance-Sidon set of `k` points in the plane, let

\[
 D=A-A,\qquad J(x,y)=(-y,x),
\]

and let `G_tr` be the transverse part of the translate-block collision graph
from `PARALLEL_LINE_SUPPORT_LEMMA.md`.  Its vertices are the elements of `D`.
Two different vertices `d,d'` are adjacent when

\[
 J(d'-d)\in D
\]

and `d,d'` are not collinear with the origin.

For `d in D`, define the local transverse overlap

\[
 m_{\rm tr}(d)=
 \big|\{e\in D\setminus\{0\}:d-Je\in D, d\mathbin\cdot e\ne0\}\big|.       \tag{1.1}
\]

The substitution `d'=d-Je` is bijective, and

\[
 \det(d,d-Je)=-d\mathbin\cdot e.                                  \tag{1.2}
\]

Consequently

\[
 \boxed{2E_{\rm tr}(A)=\sum_{d\in D}m_{\rm tr}(d).}                 \tag{1.3}
\]

Since `|D|=k^2-k+1`, the local estimate

\[
 \boxed{\max_{d\in D}m_{\rm tr}(d)\le k^{1+o(1)}}                 \tag{1.4}
\]

would imply `E_tr(A)<=k^(3+o(1))` immediately.  Thus (1.4) is a
strictly sharper sufficient target than the total transverse gate.  It also
removes the known obstruction cleanly: the quadratic local overlaps in the
perpendicular-ruler construction have `d dot e=0`, so their transverse local
overlap is zero.

Equation (1.4) is **not proved**.  It is the main new bet isolated in this
note.

## 2. Quarter-turn interpretation

For fixed `d`, put

\[
 T_d(e)=d-Je.                                                       \tag{2.1}
\]

This is rotation through `-90` degrees about

\[
 c_d=\frac{d-Jd}{2},
\]

and `T_d^4` is the identity.  Thus `m_tr(d)` counts points of `D` that
are carried back into `D` by one fixed quarter-turn, after deleting exactly
the pairs for which the corresponding vertices `d,T_d(e)` of the collision
graph lie on a line through the origin.

After rotating coordinates so `d=(r,0)`, write `e=(x,y)`.  Then

\[
 T_d(e)=(r+y,-x),\qquad d\mathbin\cdot e=rx.                        \tag{2.2}
\]

The excluded parallel solutions are precisely `x=0`.  A transverse
solution is therefore a pair of realized edge vectors

\[
 (x,y),\quad(r+y,-x)                                                \tag{2.3}
\]

with `x!=0`, where `(r,0)` is itself a realized edge vector.

This formulation exposes why the naive tensor construction fails.  If one
tries to realize quadratically many pairs by taking all differences `x-y`
between two reused endpoint sets and defining the second family by
`d-J(x-y)`, then the endpoint sets in the second family are quarter-turned
copies of the first ones.  Any two reused endpoints then give a second edge
of exactly the same Euclidean length.  Fresh endpoints avoid that collision,
but spend a linear number of points per batch and produce only linear local
overlap.  This is motivation for (1.4), not a proof of it.

## 3. An exact structured-case bound

Suppose `A` is contained in `r` lines parallel to a fixed direction.  Choose
orthonormal coordinates in which those lines have second coordinates in a
set `H` with `|H|=r`.  Write

\[
 d=(d_1,d_2),\quad e=(e_1,e_2),\quad f=d-Je=(d_1+e_2,d_2-e_1).
\]

If `e,f in D`, then both

\[
 e_2\in H-H,\qquad f_2=d_2-e_1\in H-H.                             \tag{3.1}
\]

The ordered pair `(e_2,f_2)` determines `e_1=d_2-f_2`, and hence determines
`e`.  Therefore, for every `d`,

\[
 \boxed{m_{\rm tr}(d)\le |H-H|^2\le r^4.}                          \tag{3.2}
\]

The same bound holds before the transverse restriction.  It is weaker than
the cubic support lemma when `r=k^(o(1))`, but it is useful evidence that the
local gate interacts correctly with the line-structured branch rather than
reintroducing the perpendicular-ruler obstruction.

## 4. A secondary four-cycle gate

Let `N=|D|`, `E=|E(G_tr)|`, and let `Q` be the number of (unlabelled) copies
of `C_4` in `G_tr`.  If `c(x,y)` is the common-neighbour count and

\[
 P=\sum_v\binom{\deg(v)}2=\sum_{x<y}c(x,y),
\]

then

\[
 P^2\le\binom N2\sum_{x<y}c(x,y)^2
     =\binom N2(P+4Q).                                             \tag{4.1}
\]

Together with

\[
 P\ge \frac{2E^2}{N}-E,                                           \tag{4.2}
\]

this gives

\[
 E=O\big(N^{3/2}+NQ^{1/4}\big).                                   \tag{4.3}
\]

Consequently the four-cycle estimate

\[
 Q\le k^{4+o(1)}                                                   \tag{4.4}
\]

would also imply `E_tr(A)<=k^(3+o(1))`.  The graph is not `C_4`-free:
the stored witnesses have many transverse four-cycles.  Thus (4.4), not a
forbidden-cycle claim, is the honest secondary target.

This gate is weaker than (1.4), but it may be more amenable to a
supersaturation-plus-geometry argument.  A fixed forbidden biclique is not
available; the constructions in `CROSS_TRANSLATION_OVERLAP.md` already warn
that bounded local patterns can be realized by spending fresh endpoints.

## 5. Exact computational audit

`verify_transverse_local_gate.py` checks (1.2), (1.3), `T_d^4=id`, the line
cover bound (3.2), and the exact transverse `C_4` count.  On the five fixed
adversarial witnesses it gives:

| `k` | `E_tr` | `max_d m_tr(d)` | `max/k` | transverse `C_4`s |
|---:|---:|---:|---:|---:|
| 12 | 656 | 17 | 1.417 | 2,416 |
| 16 | 1,546 | 24 | 1.500 | 6,315 |
| 20 | 3,220 | 35 | 1.750 | 19,733 |
| 24 | 4,940 | 38 | 1.583 | 25,280 |
| 28 | 7,402 | 38 | 1.357 | 35,326 |

The perpendicular-ruler controls have `m_tr(d)=0` for every `d` tested.
These finite values support (1.4) and (4.4), but they are not asymptotic
evidence strong enough to establish either statement.

A targeted simulated-annealing search then maximized `max_d m_tr(d)` itself,
subject to the exact distance-Sidon constraint.  The exact retained witnesses
are in `verify_transverse_search_witnesses.py`:

| `k` | `E_tr` | `max_d m_tr(d)` | `max/k` | transverse `C_4`s |
|---:|---:|---:|---:|---:|
| 12 | 492 | 22 | 1.833 | 796 |
| 16 | 926 | 31 | 1.938 | 1,917 |
| 20 | 3,220 | 35 | 1.750 | 19,733 |

Thus the search increased the local maximum for `k=12,16`, but did not find
even a weak superlinear trend.  This is only finite falsification evidence.
The search code supports `local`, `edges`, and `c4` objectives so that both
gates can be attacked directly.

One tempting proof shortcut also fails.  For a fixed `d`, writing every
solution `e=x-y`, `d-Je=u-v` as a linear equation in the coordinates of the
endpoints produces many dependent equations: on the fixed witnesses, the
constraint rank is essentially `k-2` while the number of local solutions can
be a larger constant multiple of `k`.  Hence linear independence of the
coordinate equations cannot prove (1.4) by itself.  The still-missing input
must use equality of lengths, not just the affine relations.

## 6. Kill conditions and next proof task

The local route is killed by a family of distance-Sidon sets with

\[
 \max_d m_{\rm tr}(d)\ge k^{1+\epsilon}
\]

for a fixed `epsilon>0`.  The four-cycle route is killed by a family with
`Q>=k^(4+epsilon)`.  Searches should maximize these two quantities directly,
not merely minimize total support.

The proof task is to exploit *global endpoint reuse*.  A solution of
`d-Je in D` pairs two edges of the complete geometric graph on `A`.  A single
batch of `s^2` prescribed pairs can be realized with `Theta(s^2)` fresh
endpoints, so no fixed-pattern exclusion suffices.  A proof of (1.4) must show
that reusing only `k` endpoints in superlinearly many transverse pairs forces
two non-antipodal realized differences to have the same Euclidean norm.
