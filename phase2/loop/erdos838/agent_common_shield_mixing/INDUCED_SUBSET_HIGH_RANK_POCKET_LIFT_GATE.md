# Induced-subset LP and a high-rank pocket-lift bank

**Date:** 2026-08-15. All logarithms are base two. The empty face is
included when convenient; deleting it changes none of the estimates.

## Verdict

The rank-profile linear program from **total** induced-subset counts has a
sharp complete-shelf solution. Even if every induced \(m\)-set is required
to meet the coefficient-one-half lower target, those constraints are
compatible with essentially all parent mass at rank

\[
                         {1\over2}\log n,                         \tag{1}
\]

and no mass above that rank. Thus global \(V\)-minimality plus all scalar
restriction inequalities cannot force a positive fraction of the face
bank to rank \((1-o(1))\log n\). This exactly recovers the entropy floor.

There is, however, a clean genuinely planar replacement which is strong
enough for the **cardinality** side of the \(n/\operatorname{polylog}n\)
pocket lift. Fix any pocket \(X\), put \(Y=P\setminus X\), and choose
\(t\le |Y|\). If \(ES(r)\le t\), then

\[
 \boxed{
 v_r(P[Y])\ge {\binom{|Y|}{r}\over\binom tr}
             \ge \left({|Y|\over t}\right)^r .}                 \tag{2}
\]

This is an exact induced-subset double count. Taking
\(t=2^{L-\Delta}\), where \(L=\log n\), \(\Delta=o(L)\), and using
\(ES(r)=2^{r+o(r)}\), gives

\[
                    r=(1-o(1))L,\qquad
                    \log v_r(P[Y])=(1-o(1))L\Delta.              \tag{3}
\]

If \(|X|=n/2^\delta\), with \(\delta=o(L)\), choose \(\Delta\) tending
to infinity slowly enough that

\[
       \delta+\text{the inverse-ES error}+\log L=o(\Delta).      \tag{4}
\]

Least-counterexample induction inside \(X\), together with (3), then gives

\[
          v_r(P[Y])V(P[X])
             \ge F_C(n)\,2^{(1-o(1))L\Delta}.                   \tag{5}
\]

Here

\[
 F_C(n)=2^{\frac12L^2-CL\log L}.                                \tag{6}
\]

Thus no quantitative rate in the \(o(r)\) term of the modern
Erdős--Szekeres theorem is needed: sampling slightly below the pocket scale
creates enough slack to absorb it. For an \(n/\operatorname{polylog}n\)
pocket, the minimally tuned choice already has
\(n^{\Theta(\log\log n)}\) sources; the slack choice in (4) gives a larger
subquadratic bank while keeping rank \((1-o(1))L\).

One can also fix a literal exposed source edge and its interior side at a
loss of only \(n^2\). If a positive
\(2^{-o(L\Delta)}\) fraction of the resulting source--pocket pairs have
ordinary union, (5) closes the fixed-gap target by an injective union map.
Otherwise almost every pair is bad and has a canonical crossing planar
four-circuit. This is a sharp reduction to a dense fixed-edge circuit
rectangle.

It is not a closure. An exact rational two-cloud construction has
arbitrarily many high-rank source faces sharing one exposed edge and
arbitrarily many pocket faces, while **every** cross union is nonconvex.
The construction's internal Boolean banks are enormous, so it is not a
least-counterexample barrier. It proves that the remaining step must use
the global low-\(V\)/minimizer state to charge those internal banks or force
a circuit cycle; rank, a common edge, and dense cross-circuit incidence do
not suffice.

## 1. The exact all-restrictions rank-profile LP

Let \(v_k=v_k(P)\) and choose a uniformly random \(m\)-subset \(S\) of an
\(n\)-point ground set. A fixed rank-\(k\) face is retained with probability

\[
 p_{m,k}={\binom{n-k}{m-k}\over\binom nm}
        ={\binom mk\over\binom nk}.                               \tag{7}
\]

Therefore

\[
       \mathbb E_{|S|=m}V(P[S])
          =\sum_{k\le m}v_kp_{m,k}.                              \tag{8}
\]

If \(P\) is a global minimizer, or a least counterexample with inductive
lower targets \(b_m\), then every proper restriction has at least \(b_m\)
faces. The scalar rank-profile LP is

\[
\begin{aligned}
 0\le v_k&\le\binom nk,\\
 \sum_{k\le m}v_kp_{m,k}&\ge b_m\qquad(0\le m\le n),             \tag{9}
\end{aligned}
\]

together with a top total or upper cap on \(\sum_kv_k\). This formulation
uses every induced-subset size simultaneously.

Put

\[
                         B_r(m)=\sum_{k=0}^{\min(r,m)}\binom mk.  \tag{10}
\]

> **Theorem 1 (complete-shelf LP certificate).** The profile
> \[
>                  u_k^{(r)}=\binom nk\mathbf1_{k\le r}           \tag{11}
> \]
> satisfies
> \[
>              \sum_{k\le m}u_k^{(r)}p_{m,k}=B_r(m)              \tag{12}
> \]
> for every \(m\). Consequently, whenever \(b_m\le B_r(m)\) for
> all \(m\), the full LP (9) has a feasible solution with zero mass above
> rank \(r\).

**Proof.** Substitute (7) into the left side of (12): every term becomes
\(\binom nk\binom mk/\binom nk=\binom mk\). \(\square\)

There is an exact fractional form matching a prescribed top total \(H\).
Let \(r\) be least with \(B_r(n)\ge H\) and put

\[
 \theta={H-B_{r-1}(n)\over\binom nr},\qquad
 g_k=\begin{cases}
       \binom nk,&k<r,\\
       \theta\binom nr,&k=r,\\
       0,&k>r.
     \end{cases}                                                \tag{13}
\]

Then

\[
             \sum_kg_k=H,\qquad
             \sum_{k\le m}g_kp_{m,k}
                =B_{r-1}(m)+\theta\binom mr.                     \tag{14}
\]

Moreover (13) minimizes \(\sum k v_k\) among **all** capacity vectors
with total at least \(H\). This is the standard exchange argument: if a
higher occupied level and a lower unfilled level coexist, move mass from
the former to the latter. Iteration gives (13). Hence any restriction
targets lying below (14) do not improve even the optimum mean rank.

### Quadratic-scale solution

Let \(b_m=2^{(\beta-o(1))(\log m)^2}\) and suppose the parent top scale is
\(H=2^{(\beta+o(1))L^2}\). The shelf cutoff is

\[
                              r=(\beta+o(1))L,                    \tag{15}
\]

because

\[
                 \log\binom nr=rL-r\log r+O(r).                  \tag{16}
\]

At \(m=2^{\alpha L}\), the shelf restriction has

\[
                \log B_r(m)=\beta\alpha L^2-o(L^2)
                         \ge\beta\alpha^2L^2-o(L^2).             \tag{17}
\]

Thus every smaller-scale coefficient-\(\beta\) target is satisfied. For
the fixed-gap target (6), solving (16) gives more precisely

\[
                r={1\over2}L-(C-1/2)\log L+O_C(1).               \tag{18}
\]

The exact shelf is not planar when \(r\ge4\): it declares every four-set
ordinary, which by planar four-locality makes the entire ground convex.
But (11)--(18) prove that some genuinely planar input is indispensable.
No manipulation of total restriction counts or global minimality can move
the entropy floor from \(L/2\) to \((1-o(1))L\).

## 2. Planarity supplies a disjoint near-logarithmic bank

The missing planar input can be inserted rankwise rather than as a mass
fraction.

> **Theorem 2 (high-rank bank outside any fixed pocket).** Let
> \(X\subset P\), put \(Y=P\setminus X\), \(N=|Y|\), and choose
> \(t\le N\). If every \(t\)-point planar set contains an ordinary
> rank-\(r\) subset, then
> \[
>        v_r(P[Y])\ge {\binom Nr\over\binom tr}
>                    \ge(N/t)^r.                                \tag{19}
> \]

**Proof.** Count pairs \((S,A)\), where \(S\in\binom Yt\) and
\(A\subseteq S\) is an ordinary \(r\)-set. Every \(S\) contributes at
least one pair. A fixed \(A\) belongs to exactly
\(\binom{N-r}{t-r}\) samples. Hence

\[
 v_r(P[Y])\binom{N-r}{t-r}\ge\binom Nt,
\]

which is the first inequality in (19). For \(N\ge t\),

\[
 {\binom Nr\over\binom tr}
   =\prod_{j=0}^{r-1}{N-j\over t-j}\ge(N/t)^r.                   \tag{20}
\]

\(\square\)

Take \(r\) maximal with \(ES(r)\le t\). Suk's asymptotic theorem gives

\[
 r\ge\log t-e(t),\qquad
 e(t):=\max\{0,\log t-r\}=o(\log t).                            \tag{21}

\]

Unlike the shelf, (19) is a theorem about actual ordinary faces in the
specified physical complement of \(X\). No averaging over pockets or
source--pocket overlap is hidden.

## 3. Fixed-gap pocket ledger without a quantitative ES error

Let

\[
       |X|=p=2^{L-\delta},\qquad 1\le\delta=o(L),                 \tag{22}
\]

and suppose least-counterexample induction gives

\[
                         H:=V(P[X])\ge F_C(p).                    \tag{23}

\]

Put

\[
 \bar e_L=\sup\{e(2^s):L/2\le s\le L\}=o(L).                    \tag{24}
\]

Choose \(\Delta=\Delta(L)\) so that

\[
 \delta+\bar e_L+\log L=o(\Delta),
 \qquad \Delta=o(L),                                             \tag{25}
\]

and take \(t=2^{L-\Delta}\). Then \(t\le p\le|Y|\) eventually,
and Theorem 2 supplies a rank

\[
                       r\ge L-\Delta-\bar e_L=(1-o(1))L          \tag{26}

\]

bank of size \(K\) satisfying

\[
                  \log K\ge r\log(|Y|/t)
                            =(1-o(1))L\Delta.                     \tag{27}

\]

On the other hand, a direct expansion of (6) gives

\[
 \Phi_C(L)-\Phi_C(L-\delta)
       =L\delta+O_C(\delta^2+\delta\log L).                       \tag{28}

\]

Equations (23), (25), and (27)--(28) prove

\[
 \boxed{
          KH\ge F_C(n)\,2^{(1-o(1))L\Delta}.}                    \tag{29}
\]

The positive exponent in (29) may be weakened to, say,
\(L\Delta/3\) for all sufficiently large \(n\). It absorbs polynomial,
\(2^{O(L\log L)}\), and indeed any \(2^{o(L\Delta)}\) decoder loss.

If one insists on the minimally tuned choice \(t=p=n/s\), (19) gives

\[
              K\ge(s-1)^{(1-o(1))\log p}.                       \tag{30}

\]

For \(s=L^A\), this is
\(K=n^{(A-o(1))\log L}=n^{\Theta(\log\log n)}\). However, the unknown
inverse-ES error in (21) can exceed the \(O((\log L)^2)\) fixed-gap slack.
The deeper sample (25) is what makes (29) rate-independent.

## 4. A common exposed edge costs only a polynomial factor

Every ordinary rank-\(r\) source has \(r\) oriented boundary edges, where
the orientation records the side containing the rest of the polygon.
There are at most \(N(N-1)\) physical edge-and-side states. Double counting
source--boundary-edge incidences gives:

> **Corollary 3 (fixed exposed-edge source bank).** Some literal edge and
> side is shared by at least
> \[
>                         K_e\ge {rK\over N(N-1)}                 \tag{31}
> \]
> of the sources in Theorem 2.

All these sources retain rank \(r=(1-o(1))L\), lie outside the pocket, and
share one actual tangent carrier. The loss in (31) is \(2^{O(L)}\), which
is negligible in (29).

This is stronger than merely marking arbitrary endpoints: the fixed
physical segment is an exposed polygon edge in every selected source, with
the same interior side.

## 5. Injective multiplication or a dense crossing-circuit rectangle

Let \(\mathcal A\) be the fixed-edge source bank and
\(\mathcal H=\mathcal F(P[X])\). Since the grounds are disjoint, the map

\[
                         (A,F)\longmapsto A\cup F                 \tag{32}

\]

is injective on the pairs for which the union is ordinary. Hence if \(G\)
is the number of good pairs,

\[
                              G\le V(P).                          \tag{33}

\]

Under a least-counterexample upper bound \(V(P)<F_C(n)\), equations
(29), (31), and (33) imply

\[
 {G\over K_eH}\le2^{-(1-o(1))L\Delta}.                          \tag{34}

\]

Thus almost every source--pocket pair is nonordinary. Since \(A\) and
\(F\) are individually ordinary, every bad union has a nonordinary
four-subset meeting both grounds. Its planar circuit type is necessarily

\[
                 1+3,\qquad2+2,\qquad\text{or }3+1.             \tag{35}

\]

Choosing the first circuit in a fixed physical order gives an exact
canonical dense circuit-decorated rectangle while retaining the pocket
face, the rank-\((1-o(1))L\) source, and its common exposed edge.

Equation (34), not the scalar LP, is the useful global alternative. It
supplies precisely the high-rank source input that a label-deletion or
profile-cycle theorem would need. It does not itself turn the bad pairs
into ordinary outputs.

## 6. Stretchable fixed-edge anti-alignment barrier

The last conversion is not formal. Use the exact rational two-cloud
lexicographic construction from
`DENSE_HALL_TWO_CLOUD_PROFILE_BARRIER.md`. Choose the two parabolic child
charts so their facing profiles contain exactly the singleton and pair
subsets. Then a subset meeting both clouds is ordinary if and only if each
cloud trace has rank at most two.

Inside the first cloud, fix two adjacent parabolic points \(u,v\). Every
rank-\(r\) subset containing them is ordinary and has \(uv\) as an exposed
edge with a common side. Every rank-\(q\) subset of the second cloud is
ordinary. For all \(r,q\ge3\), every one of the

\[
                         \binom{a-2}{r-2}\binom bq                \tag{36}
\]

cross unions is nonordinary.

The verifier's smallest displayed instance has an eight-point source cloud
and a seven-point pocket cloud. It finds

\[
                         15\cdot35=525                             \tag{37}
\]

bad rank-\(4\) by rank-\(3\) pairs, with the same literal exposed edge in
all fifteen sources. All coordinates are rational and every assertion is
checked by exact determinants.

This kills the implication

\[
 \text{near-log rank + common exposed edge + dense crossing circuits}
 \Longrightarrow \text{mixed face bank}.                         \tag{38}
\]

The example is not globally live: each parabolic cloud has a Boolean face
bank of size \(2^{\Theta(a)}\) or \(2^{\Theta(b)}\). Therefore (38) remains
potentially true after adding a least-counterexample/internal-bank charge.
That extra charge is exactly what a successful theorem must use.

## 7. Consequence for the campaign

The global chart machinery is not needed to manufacture high-rank sources.
Theorem 2 and Corollary 3 give them outside any fixed macroscopic pocket,
at more than enough cardinality for a coefficient-one-half or fixed-gap
pocket ledger. Nor can the scalar all-restrictions LP prove more: Theorem 1
is its exact shelf obstruction.

The remaining operation is now sharply isolated:

> In a least counterexample, charge the dense fixed-edge crossing-circuit
> rectangle (34)--(35) either to a bounded-load deletion/profile bank or to
> an internal bank of one of the two physical sides. A two-cloud cage can
> defeat the first alternative only by exposing the second.

This is narrower than complete-product promotion and does not require a
positive fraction of the ambient face law at rank \((1-o(1))L\). It needs
only the absolute source bank (27), whose size is already forced by planar
Erdős--Szekeres multiplicity.

## 8. Verification

Run

```text
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_induced_subset_high_rank_pocket_lift_gate.py
```

The verifier:

* checks 1,381 exact hypergeometric restriction identities for complete
  shelves;
* independently solves 27 small integral rank-capacity LPs and verifies the
  greedy cutoff optimum;
* audits the quadratic half-shelf at five scales and four restriction
  exponents per scale;
* checks 1,323 exact hereditary witness double counts and an exact rational
  planar \(ES(4)=5\) instance;
* checks the high-rank pocket coefficient ledger;
* verifies the exposed-edge pigeonhole count; and
* exhausts the rational fixed-edge anti-aligned cage, obtaining all 525 bad
  cross pairs in (37).
