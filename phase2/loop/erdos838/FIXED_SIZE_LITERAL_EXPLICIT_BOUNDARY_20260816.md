# Fixed-size literal pooling to the explicit quarter-log boundary

**Date:** 2026-08-16. All logarithms are base two.

## Verdict

Let \(N=4^k\), let \(P\) be an arbitrary \(N\)-point planar set in
general position, and suppose

\[
                    ES(k)\le 2^{k+G_k}                 \tag{1}
\]

for an integer \(G_k\ge0\). Put

\[
              R_k=\left\lfloor {k-G_k\over2}\right\rfloor-3. \tag{2}
\]

Whenever \(R_k\ge1\), every collection of literal temporal histories of
ranks \(1\le r\le R_k\) can be pooled simultaneously into the ordinary
convex \(k\)-faces of \(P\). A rank-\(r\) history receives amplified mass
\(N2^{-r}\), while both the physical output load and the recovery fibre are
at most one.

Holmsen, Nassajian Mojarrad, Pach, and Tardos proved

\[
                    ES(k)\le 2^{k+O(\sqrt{k\log k})}.   \tag{3}
\]

Consequently (2) gives the unconditional range

\[
 r\le {k\over2}-O(\sqrt{k\log k})
   ={1\over4}\log N-O(\sqrt{\log N\log\log N}).        \tag{4}
\]

This sharpens **FIXED_SIZE_LITERAL_QUARTER_LOG_POOLING_GATE_20260815.md**,
which reached only \(r\le(1/2-\delta)k\) for each fixed \(\delta>0\).
Together with the identity code for \(r\ge\log N\), the remaining literal
rank window is now

\[
 {1\over4}\log N-O(\sqrt{\log N\log\log N})
       <r<\log N.                                      \tag{5}
\]

This is a decoder-range theorem, not a supersaturation gain: it does not
improve the unconditional coefficient \(1/4\).

Primary source for (3): Andreas F. Holmsen, Hossein Nassajian Mojarrad,
Janos Pach, and Gabor Tardos,
[Two extensions of the Erdos--Szekeres problem](https://arxiv.org/abs/1710.11415),
*J. Eur. Math. Soc.* **22** (2020), 3981--3995.

## 1. The physical rank-\(k\) reservoir

Write \(t_k=ES(k)\). Double counting a convex \(k\)-face together with a
containing \(t_k\)-set gives

\[
 v_k(P)\ge {\binom Nk\over\binom{t_k}k}.                \tag{6}
\]

The elementary estimates

\[
 \binom Nk\ge(N/k)^k,
 \qquad
 \binom{t_k}k\le(4t_k/k)^k                             \tag{7}
\]

and \(N=4^k\), together with (1), imply

\[
 v_k(P)\ge\left({N\over4t_k}\right)^k
          \ge2^{k(k-G_k-2)}.                            \tag{8}
\]

## 2. All literal demand through rank \(R_k\)

There are at most \(\binom Nr\) literal rank-\(r\) supports. Give every
one

\[
                         q_r=\left\lceil{N\over2^r}\right\rceil \tag{9}
\]

unit slots. As in the preceding pooling theorem, the total number of slots
through rank \(R\le k\) is at most

\[
 2^{D(k,R)},\qquad
 D(k,R)=R(2k+1)+2k+1+\lceil\log R\rceil.               \tag{10}
\]

For \(R=R_k\), equation (2) gives

\[
 R\le{k-G_k\over2}-3.                                  \tag{11}
\]

Since \(R\le k\), substituting (11) into (10) yields

\[
\begin{aligned}
 D(k,R)
 &\le k^2-kG_k-4k-2+{k-G_k\over2}+\lceil\log k\rceil,\\
 k(k-G_k-2)-D(k,R)
 &\ge {3k+G_k\over2}+2-\lceil\log k\rceil>0            \tag{12}
\end{aligned}
\]

for every \(k\ge2\). Thus the reservoir lower bound (8) dominates the
entire ceiling demand (10), not merely each rank separately.

## 3. Decoder

Order literal histories canonically by rank and physical support, and order
the ordinary convex \(k\)-faces canonically. Assign each history its next
\(q_r\) unused faces and place weight

\[
                         {N2^{-r}\over q_r}\le1         \tag{13}
\]

on each assigned face. The blocks are disjoint, hence physical output load
is at most one. The output's position in the public face order identifies
its unique block and therefore recovers its literal support and rank. The
recovery fibre is one.

## 4. Exact scope

The theorem applies only to literal histories: multiple temporal records
with the same physical support still require a separate multiplicity or
incidence bound. It also stops at the quarter-log boundary for a structural
reason. The universal bank (8) has \(k^2-o(k^2)\) bits, whereas the amplified
demand of all rank-\(r\) supports has leading exponent \(2kr\). Crossing
\(r=k/2+o(k)\) therefore requires selected-family sparsity, a larger
configuration-specific bank, or a mixed/profile charge; a better error term
in \(ES(k)\) alone cannot cross it.

## 5. Verification

Run

~~~text
python3 phase2/loop/erdos838/verify_fixed_size_literal_explicit_boundary.py
~~~

The verifier checks the exact exponent inequality for every admissible
integer pair \((k,G_k)\) in a broad range, compares the previous fixed-gap
cutoff with the new boundary, verifies the base-change asymptotics, and
replays exact disjoint block decoders on bounded instances. The external
geometric theorem (3) is cited rather than computationally re-proved.
