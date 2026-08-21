# Balanced track rows isolate one heavy weighted-pencil gate

## 1. Outcome

Keep the endpoint assignment and pointed weight from the swap occurrence
reduction.  Thus every high occurrence `o` is assigned an actual endpoint
`x=chi(o)`, has one endpoint-labelled track token

\[
 u_x(o)=(\text{track slot},\text{opposite physical endpoint}),
\]

and carries

\[
 w(o)={r_{C(o)}-1\choose2}.                         \tag{1.1}
\]

For one endpoint `x` and one token `u`, define the weighted row

\[
 B_x(u)=\sum_{\substack{o:\chi(o)=x\\u_x(o)=u}}w(o). \tag{1.2}
\]

Let `T_x` be the set of tokens used by *all* occurrences through `x`, let
`s_x=|T_x|`, and let `a_x(u)` be the number of those occurrences with token
`u`.  The possible partner-token count for row `(x,u)` is

\[
 b_x(u)=s_x-\mathbf 1_{a_x(u)=1}.                  \tag{1.3}
\]

Indeed, every token different from `u` supplies a partner occurrence, while
`u` itself does so exactly when at least two occurrences use it.

The main exact conclusion is that the entire endpoint-pencil mass can be
scheduled so that the row `(x,u)` is distributed as evenly as possible over
its `b_x(u)` two-track keys.  If

\[
 B_x(u)=q_x(u)b_x(u)+r_x(u),\qquad 0\le r_x(u)<b_x(u), \tag{1.4}
\]

then its collision mass is exactly

\[
 Q_x(u)=b_x(u){q_x(u)\choose2}+r_x(u)q_x(u).       \tag{1.5}
\]

This is the minimum possible collision mass for the row.

More importantly, for every `L>=1`,

\[
 \boxed{
 \sum_{B_x(u)\le Lb_x(u)}B_x(u)
 \le144Lk(k-1)^2<144Lk^3.}                         \tag{1.6}
\]

Consequently the direct cube-root support branch is reduced to the single
heavy-row estimate

\[
 \boxed{
 \mathcal H_L=
 \sum_{B_x(u)>Lb_x(u)}B_x(u)
 \le N^{o(1)}m^2}                                  \tag{1.7}
\]

for a subpolynomial cutoff `L=N^{o(1)}`.  Unlike the cyclic schedule, this
statement no longer separates periodic internal collisions from
off-diagonal track reuse: both are absorbed into one weighted fixed-track
row.  A survivor has pointed mass polynomially larger than the *entire*
partner-track support visible at its assigned endpoint.

## 2. Balanced scheduling theorem

Fix a row `(x,u)`.  Its `B=B_x(u)` pointed decorations are distinguishable.
List the `b=b_x(u)` allowed partner tokens cyclically and send consecutive
decorations to consecutive tokens.  For a chosen token `v!=u`, select any
occurrence through `x` using `v`.  For `v=u`, choose an occurrence other
than the first one; this is possible by (1.3).  Thus every decoration is
paired with an actual distinct occurrence through `x`.

The resulting key is

\[
 \kappa=(x,u,v).                                    \tag{2.1}
\]

Exactly `r` keys have load `q+1` and the other `b-r` have load `q`, proving
(1.5).  Convexity of `n\mapsto {n\choose2}` shows that moving one unit from
a bin at least two larger than another strictly lowers the collision count.
Hence (1.5) is also the minimum over every possible distribution of the row
among its allowed keys.

The global key support is sharply controlled.  At `x` there are `s_x`
possible first tokens, each with at most `s_x` partner tokens, so

\[
 \sum_{u\in T_x}b_x(u)\le s_x^2.                  \tag{2.2}
\]

A token specifies one of twelve directed track slots and one of `k-1`
opposite endpoints.  Therefore

\[
 \sum_x\sum_{u\in T_x}b_x(u)
 \le\sum_xs_x^2
 \le144k(k-1)^2.                                  \tag{2.3}
\]

Equation (1.6) follows immediately from `B_x(u)<=Lb_x(u)` and (2.3).

If `M=sum B_x(u)` and `Q_bal=sum Q_x(u)`, the ordinary support identity also
gives

\[
 M^2\le K_{bal}(M+2Q_{bal}),\qquad
 K_{bal}\le144k(k-1)^2.                            \tag{2.4}
\]

But (1.6) is stronger for the low branch: it bounds first moment directly
and forms collisions only inside genuinely heavy rows.

## 3. Geometric meaning of a heavy row

The first token `u` is one literal physical directed track through `x`, in
one fixed role among the six owner tracks.  Every key collision in its row
also fixes a second physical track token `v` through the same endpoint.
Thus the surviving branch retains precisely the data needed by the
anchored rank-five theorem:

* one fixed endpoint;
* one heavily weighted first track;
* one partner track;
* the four-dimensional transverse quotient of the six owner differences;
* the one-dimensional gauge fibre, whose physical wedge load is at most
  `4k`.

The remaining theorem should therefore be attacked as a weighted
fixed-track Carleson estimate, not relaxed to an ambient six-difference
energy.  The normalization by `b_x(u)` is load-bearing: it measures every
partner track actually available at `x`, including same-token partners when
the first track is repeated.

## 4. Genuine stresses

The optimal-core analyzer implements the balanced schedule in addition to
the older cyclic one.

* Transformed Costas `23`, `Lambda=16`: the balanced profile is
  `(mass,support,max,Q)=(204,204,1,0)`, compared with cyclic
  `(204,192,2,12)` and the old amplified
  `(16244,5380,20,33564)`.
* Transformed Costas `29`, `Lambda=16`: the balanced profile is
  `(4857,4645,2,212)`, compared with cyclic
  `(4857,3095,35,8174)`.

Thus the dominant finite double-track collision population was largely a
poor scheduling artefact.  What survives is exactly row imbalance.  The
known dense Golomb, lifted residue-parabola, and rank-flat barriers already
have zero selected same-centre third mass, so they do not challenge (1.7).

## 5. Status

Equations (1.3)--(1.6) are unconditional.  Equation (1.7) is the new direct
gate, not a proved theorem.  It is strictly narrower than the cyclic pair
of a very-rich internal tail and a high-degree off-diagonal tail: those two
phenomena now contribute to the same row only when their combined pointed
mass exceeds the full partner-token capacity by a polynomial factor.

The next binary task is to prove (1.7) from determinant/height packing and
the rank-five quotient, or build a genuine polynomial-height
distance-Sidon family with `H_L` above the `m^2` allowance.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_balanced_track_row.py
```

The verifier exhausts the row-balancing minimum on small compositions and
checks the lossless schedule, distinct partners, support bound, exact
collision formula, Cauchy inequality, and light-row estimate on deterministic
and seeded random endpoint systems.  The optimal-core analyzer independently
checks the two genuine Costas profiles above.
