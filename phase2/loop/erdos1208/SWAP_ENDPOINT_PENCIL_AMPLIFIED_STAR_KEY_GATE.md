# Amplifying the endpoint pencil into two-track star keys

## 1. Outcome

The endpoint-reuse dichotomy reduces the physical-wedge obstruction to

\[
 \mathcal P_\Lambda
 =3\sum_{o=(C,q)\ {m high}}{r_C-1\choose2},      \tag{1.1}
\]

where every high occurrence `o` has been assigned canonically to one point
`x=chi(o)` contained in its six-track endpoint footprint and
`d(x)>=Lambda`.

This note amplifies (1.1) against the other occurrences through `x`.  After
pigeonholing one of the twelve directed-track endpoint slots, every
amplified record has a key consisting of

* the common endpoint `x`;
* the opposite endpoint and slot of the distinguished occurrence; and
* the opposite endpoint and slot of the partner occurrence.

There are fewer than `144k^3` such keys.  Hence the support half of the
endpoint pencil is automatically paid by `k^3`; the sole survivor is
collision mass inside a key that fixes two literal endpoint-labelled
tracks.

Precisely, define the collision quantity `Q_star` in Section 3.  Then

\[
 \boxed{\mathcal Q_\star\le N^{o(1)}(k^3+m^2)}    \tag{1.2}
\]

is sufficient for the full endpoint-pencil gate, and hence for the support
half of the physical-wedge obstruction.

## 2. Pointed triples and endpoint amplification

Let `O` be the occurrence set.  Each occurrence has six nonzero directed
tracks.  Regard the head and tail of each track as two separate slots, so
there are twelve slots.  For an endpoint `x` in an occurrence footprint,
choose the first slot containing `x`; the slot determines both its role and
the opposite endpoint.

For a high occurrence `o=(C,q)`, form one pointed record for every unordered
pair of other parameters in `S_C`.  Thus the number of pointed records above
`o` is

\[
 w(o)={r_C-1\choose2}.                            \tag{2.1}
\]

The harmless outer factor three in (1.1) is kept outside this definition.
For every pointed record above `o`, pair it with every other occurrence
`o'!=o` whose footprint contains `x=chi(o)`.  Since `d(x)>=Lambda`, the
number `mathcal A` of amplified records satisfies

\[
 \boxed{\mathcal A
   =\sum_{o\ {m high}}w(o)(d(\chi(o))-1)
   \ge(\Lambda-1){\mathcal P_\Lambda\over3}.}     \tag{2.2}
\]

## 3. The two-track star key

Let the chosen slot of `o` at `x` have opposite endpoint `y`, and let the
chosen slot of `o'` at `x` have opposite endpoint `y'`.  Define

\[
 \kappa=(x,\sigma,y,\tau,y'),                    \tag{3.1}
\]

where `sigma,tau` are the two slots.  Since `y,y'!=x`,

\[
 K_\star:=|\{\kappa\}|\le144k(k-1)^2<144k^3.    \tag{3.2}
\]

Let `M(kappa)` be the amplified load of one key and put

\[
 \mathcal Q_\star=\sum_\kappa{M(\kappa)\choose2}.\tag{3.3}
\]

Because `sum M=mathcal A`, Cauchy gives the exact inequality

\[
 \boxed{\mathcal A^2
       \le K_\star(\mathcal A+2\mathcal Q_\star).}\tag{3.4}
\]

Put `B_0=k^3+m^2`.  If (1.2) holds with factor `L=N^{o(1)}`, then

\[
 \mathcal A
 \le K_\star+\sqrt{2K_\star\mathcal Q_\star}
 \le N^{o(1)}B_0.                                \tag{3.5}
\]

Equations (2.2) and (3.5), together with the low-endpoint-reuse theorem,
prove `C_center<=N^{o(1)}B_0`.

## 4. Exact meaning of a collision

The key `kappa` fixes two actual directed edges of `A`, including their
common endpoint and their two track roles.  Take two distinct amplified
records with the same key.  Exactly one of the following happens.

1. Their distinguished occurrences differ.  Then the first fixed
   endpoint-labelled track is reused by two owner occurrences.
2. Their partner occurrences differ.  Then the second fixed
   endpoint-labelled track is reused.
3. Both occurrence identities agree.  Then their pointed parameter pairs
   differ inside the same rich owner cell.

The first two branches are literal track-reuse collisions.  Comparing the
two six-track owner records gives six `D-D` differences with one coordinate
equal to zero and with that zero coordinate carrying a fixed physical edge.
This is an endpoint-anchored resonant object.  It is compatible with the
existing completion recursion, but is not automatically covered by the
same-invariant switch: the two coarse invariants and parameter values need
not agree.  Deriving this more general anchored normal form is the next
algebraic task.  The third branch is an internal fourth-parameter collision
inside one rich cell; it should be charged by that cell's perpendicular
footprint or routed to a higher-load density increment.

Thus (1.2) is not another opaque second moment.  Its off-diagonal part has
a fixed repeated physical edge, and its diagonal-occurrence part has four
parameters in one synchronized six-copy block.  These are the two concrete
subproblems to attack next.

## 5. Scope

This amplification uses only the endpoint lift and the rich-cell weight.
It makes no pointwise claim about a fixed invariant, wedge, endpoint, or
track.  The polynomial local planting barrier can create many keys, but the
number of star keys is still `O(k^3)` and is absorbed by (3.4).  A dangerous
planting must now create polynomial collision load while repeatedly using
the same two endpoint-labelled tracks or the same rich cell.

The first genuine nonzero stress is already informative.  At transformed
Costas `23`, with `Lambda=16`, there are `204` pointed records and `16244`
amplified records.  They occupy `5380` two-track keys, have maximum key load
`20`, and collision mass `33564`.  Every contributing cell has load three,
so the internal pointed-pair branch is absent: every collision reuses at
least one endpoint-labelled track.  Thus the anchored track-reuse theorem
is not optional even on the first active row.

The next proof should split `Q_star` according to Section 4, derive the
endpoint-anchored resonant normal form for track reuse, and apply the
rank-two metric-gap map to the internal rich-cell branch while retaining
the fixed endpoint star.

That anchored algebra is now exact.  If `(U,C,A,B,E,Q)` are the six vector
offsets between two arbitrary owner occurrences, their six track
differences have rank five, obey one full-support linear relation, and have
unique kernel `(h,-Jh,0,0,0,h)`.  Once one track is repeated, any four of
the other five differences determine the transverse quotient.  The sole
remaining freedom translates the parameter and the two physical wedge
edges while preserving every track and `R`; its physical wedge fibre has
the sharp bound `4k`.  See
`SWAP_ANCHORED_TRACK_REUSE_RANK_FIVE_GATE.md`.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_endpoint_pencil_amplified_star_key.py
```

The verifier builds arbitrary six-edge occurrence systems, performs the
canonical high-endpoint and slot assignments, expands every pointed record,
checks (2.2)--(3.4), the `144k(k-1)^2` support bound, and the exhaustive
collision trichotomy.
