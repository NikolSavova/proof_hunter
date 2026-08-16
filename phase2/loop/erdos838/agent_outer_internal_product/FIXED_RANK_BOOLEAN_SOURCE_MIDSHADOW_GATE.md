# Fixed-rank Boolean sources: the middle-shadow overlap gate

**Date:** 2026-08-15.  All logarithms are base two.  This corrects the
global scope of `SOURCE_REUSE_BALANCED_ONE_ENDED_PROFILE_BARRIER.md`.

## Verdict

The all-rank local barrier cannot be inserted unchanged into a canonical
fixed-rank source slice.  A rank-\(q\) convex carrier has \(2^q\) Boolean
faces, whereas one fixed source rank uses at most
\(\binom qr\).  Uniformly in \(r\), this leaves a \(\Theta(\sqrt q)\) capacity
surplus.

That surplus can be summed globally without using the empty face.  Let
\(\mathcal Q\) be distinct ordinary rank-\(q\) carriers and let weighted records
under \(Q\) use actual source faces \(A\subseteq Q\) of one fixed rank \(r\).
Assume the rank-safe normalization

\[
       \sum_{\omega:\,A_\omega=A}w_\omega\le1
                  \quad\text{for every actual source }A.             \tag{1}
\]

Put \(W=\sum_\omega w_\omega\) and define the middle-shadow carrier codegree

\[
 \Omega_{\rm mid}:=\max_{F:\,q/3\le |F|\le2q/3}
       |\{Q\in\mathcal Q:F\subseteq Q\}|.               \tag{2}
\]

There is a sharper weighted load which ignores low-mass carriers.  If
\(W_Q\) is the total record weight assigned to carrier \(Q\), put

\[
 d_Q={W_Q\over {q\choose r}},\qquad
 \Lambda_{\rm mid}:=
   \max_{F:\,q/3\le|F|\le2q/3}
      \sum_{Q\supseteq F}d_Q
   \le\Omega_{\rm mid}.                                 \tag{2a}
\]

Then the exact global inequality is

\[
\boxed{
 V\ge {W\over\Lambda_{\rm mid}}
       {\displaystyle\sum_{t=\lceil q/3\rceil}^{\lfloor2q/3\rfloor}
                       {q\choose t}
        \over {q\choose r}}
 \ge {W\over\Omega_{\rm mid}}
       {\displaystyle\sum_{t=\lceil q/3\rceil}^{\lfloor2q/3\rfloor}
                       {q\choose t}
        \over {q\choose r}}.}                           \tag{3}
\]

In particular, uniformly in \(r\),

\[
 V\ge {W\over\Lambda_{\rm mid}}
       \left(1-2e^{-q/18}\right)\sqrt{\pi q/2}.          \tag{4}
\]

For the current missing exponent

\[
        \vartheta=2-\log_2 3=0.415037\ldots,             \tag{5}
\]

the Boolean source closes a \(q^\vartheta\) deficit whenever

\[
 \Lambda_{\rm mid}
   \le q^{1/2-\vartheta-o(1)}
    =q^{\log_2 3-3/2-o(1)}.                              \tag{6}
\]

Thus the exact survivor is not arbitrary source reuse.  It is a common
ordinary middle-rank face contained in more than
\(q^{0.084962\ldots}\) saturated-carrier equivalents (and hence at least
that many distinct convex carriers).  Retaining that face
localizes to the completion family \(Q\setminus F\), whose rank is at most
\(2q/3\).  Turning this localization into an iterated bounded-load return is
still open; (3) alone does not close the high-codegree branch.

This theorem is globally normalized: the ambient \(V\) is spent once, and
coalesced histories under the same physical carrier are included in \(W\).
It also shows the precise limitation of the previous stretchable barrier.
That example used all source ranks, for total mass \(2^q-q-1\); after fixing
one rank its mass is at most \(\binom qr\), and the middle Boolean bank
recovers the missing square-root factor unless (2) is large across
distinct carriers.

## 1. Per-carrier fixed-rank capacity

For \(Q\in\mathcal Q\), let \(W_Q\) be the total weight assigned to that
carrier.  By (1), each rank-\(r\) source subset of \(Q\) contributes total
weight at most one even after all its coalesced contexts are summed.
Therefore

\[
                         W_Q\le {q\choose r},
       \qquad W\le |\mathcal Q|{q\choose r}.             \tag{7}
\]

No lower atom-weight assumption is used.

Every subset of an ordinary carrier is ordinary.  Define its middle bank

\[
 \mathcal D_{\rm mid}(Q)=
   \{F\subseteq Q:\lceil q/3\rceil\le |F|
                         \le\lfloor2q/3\rfloor\}.       \tag{8}
\]

Its exact size is

\[
 B_q:=|\mathcal D_{\rm mid}(Q)|
       =\sum_{t=\lceil q/3\rceil}^{\lfloor2q/3\rfloor}{q\choose t}.
                                                                    \tag{9}
\]

Unlike the full Boolean downset, (8) contains neither the empty face nor
any fixed low-rank tag.  Thus its global overlap is the literal physical
codegree (2), not automatically \(|\mathcal Q|\).

## 2. Global incidence count

First count weighted incidences \((Q,F)\), giving every incidence from
carrier \(Q\) weight \(d_Q\).  Their total weight is exactly

\[
 \sum_Qd_QB_q={B_q\over{q\choose r}}\sum_QW_Q
              ={B_q\over{q\choose r}}W.                 \tag{9a}
\]

Every output \(F\) is an ordinary face of the ambient configuration, and
its weighted load is at most \(\Lambda_{\rm mid}\).  Thus (9a) is at most
\(\Lambda_{\rm mid}V\), proving the first inequality in (3).

For comparison, the unweighted incidence set has exactly
\(|\mathcal Q|B_q\) members, while each output occurs for at most
\(\Omega_{\rm mid}\) carriers.  Hence

\[
                         |\mathcal Q|B_q
                       \le\Omega_{\rm mid}V.             \tag{10}
\]

Combining (7) and (10) proves the second inequality in (3).  The carrier \(Q\) is physical and
distinct; metadata duplicates have already been coalesced into \(W_Q\).

If \(X\) is binomial with parameters \((q,1/2)\), Hoeffding gives

\[
 \Pr(|X-q/2|\ge q/6)\le2e^{-q/18},                      \tag{11}
\]

so \(B_q\ge2^q(1-2e^{-q/18})\).  Wallis' central-binomial bound gives

\[
 {q\choose r}\le {q\choose\lfloor q/2\rfloor}
       \le2^q\sqrt{2/(\pi q)}.                          \tag{12}
\]

Substitution proves (4), and (5)--(6) follow arithmetically.

## 3. The exact high-codegree descent

If (6) fails, there is an actual ordinary face \(F\), of rank between
\(q/3\) and \(2q/3\), with
\(\sum_{Q\supseteq F}W_Q/\binom qr\) large.  In particular it is contained
in many distinct positive-mass carriers.  Write

\[
                         Q=F\mathbin{\dot\cup}R_Q.       \tag{13}
\]

The output \(F\) fixes a common physical core, and the completions \(R_Q\) are
distinct subsets of the remaining labels of rank between \(q/3\) and
\(2q/3\).  This is a genuine rank contraction, not a fixed-label/history
pigeonhole.

What (3) does not prove is that the completion carriers \(R_Q\) are
ordinary by themselves in a common rooted chart, or that their next
middle banks have bounded overlap after \(F\) is retained.  Heredity makes
each \(R_Q\) ordinary as a subset of \(Q\), but mixed outputs needed by the
endpoint/root context may still be anti-aligned.  Therefore an iteration
needs a mask-aware decoder retaining \(F\), or a circuit-release theorem
coupling the completions to the endpoint side.

The positive gain and the remaining obstruction are now separated
exactly:

* low middle codegree pays the desired fixed-rank source multiplier;
* high middle codegree supplies a common physical core and shrinks carrier
  rank by a constant factor;
* only the rooted completion/mask decoder is external.

## 4. Verification

`verify_fixed_rank_boolean_source_midshadow.py` checks (3) exactly on
disjoint and high-common-core carrier systems, verifies rank-safe weighted
coalescing, the middle-bank incidence identity, and the numerical exponent
\(1/2-\vartheta=\log_2(3)-3/2\).
