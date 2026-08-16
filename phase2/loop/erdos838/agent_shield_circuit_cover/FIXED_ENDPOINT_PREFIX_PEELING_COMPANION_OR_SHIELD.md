# Fixed-endpoint prefix peeling: companion floor or rooted shield

**Date:** 2026-08-15. All logarithms are base two. This continues
`GENERAL_FERRERS_COMPANION_FLOOR_AND_ENDPOINT_BARRIER.md` and
uses the relocation budget from
`agent_outer_internal_product/GAP_BUDGETED_REPAIR_ALPHABET_MUTATION_GATE.md`.

## Verdict

The delta obstruction at one fixed endpoint pair can always be opened
**locally**. A maximum-child descent through the internal-chain prefix trie
has the following exact alternatives:

1. after omitting at most \(R\) common prefix labels, the next internal
   label becomes a genuine variable endpoint whose distribution has an
   order-independent linear tail and hence a polynomial companion floor; or
2. the common cap prefix itself gives an exact rooted Boolean/profile shield.

For a uniform-rank ordered-chain family of size \(H\), let \(h_j\) be the
branching ratio at depth \(j\) along the maximum-child path. Then

\[
                         \prod_{j<s}h_j=H.                        \tag{1}
\]

At depth \(j\), the companion floor exposed by the next-label distribution
is at least

\[
                         1+\min\{M,h_j\}                          \tag{2}
\]

against any \(M\)-column Ferrers rectangle, in **every physical wall order**.
The common prefix gives a rooted Boolean shield of size \(2^j\). Therefore

\[
 \boxed{\displaystyle
 \max_{0\le j<s}\max\{h_j,2^j\}
 \ge
 2^{(\sqrt{1+4\log H}-1)/2}.}                                    \tag{3}
\]

For a rank-at-most-\(R\) family, replace \(H\) in (3) by
\(H/(R+1)\) after fixing the rank. Thus \(H=2^{\Theta((\log n)^2)}\) and
\(R=O(\log n)\) force an \(n^{\Omega(1)}\) local endpoint floor or rooted
shield.

There is, however, a sharp **global conditioning barrier**. A late trie
node can have tiny mass relative to the original fixed-pair fibre. The
rational circle family consisting of all middle-rank subsets of one cap arc
has

\[
 H=\binom{2s}{s},\qquad
 m_j=\binom{2s-j}{s-j},\qquad
 h_j=\frac{2s-j}{s-j},                                           \tag{4}
\]

along its maximum-child path, but

\[
                 \max_j\frac{m_j}{H}h_j=2.                       \tag{5}
\]

So conditional next-endpoint branching never yields a growing
\(H\)-relative one-face gain. The late common-prefix shield has size only
\(2^{s-1}=H^{1/2+o(1)}\). It is a genuine ordinary bank, but promoting it
through a quadratic family of external contexts requires a separated
two-bank/Hall decoder; the trie alone does not provide that decoder.

Accordingly, prefix peeling kills the **local** delta claim but does not by
itself close the global coherent-ramp branch. The exact remaining input is:
either the selected prefix node retains enough actual context mass, or its
rooted Boolean shield must be multiplied by a context/source output which
recovers the erased cap tail.

## 1. Maximum-child prefix identity

Let \(\mathcal A\) be a family of \(s\)-element subsets of a totally ordered
ground set. Read every member as its increasing sequence. Starting with
\(\mathcal A_0=\mathcal A\), suppose the current node has common prefix

\[
                         K_j=(z_0<\cdots<z_{j-1}).                \tag{6}
\]

Partition \(\mathcal A_j\) by the next label \(z\), choose a largest child
\(\mathcal A_{j+1}\), and set

\[
                 m_j=|\mathcal A_j|,\qquad
                 h_j=\frac{m_j}{m_{j+1}}.                         \tag{7}
\]

At depth \(s\), the common prefix is one full member of the set family, so
\(m_s=1\). Telescoping (7) proves (1).

For a nonuniform family of chain rank at most \(R\), first fix a rank class
of size at least \(H/(R+1)\). This is the only rank loss used below.

## 2. Peeling exposes a robust endpoint tail

At node \(j\), let \(m_{j,z}\) be the next-label child sizes and normalize

\[
                         p_z=m_{j,z}/m_j.                         \tag{8}
\]

By maximum-child choice,

\[
                         \max_zp_z=1/h_j.                         \tag{9}
\]

Put the physical next labels in an arbitrary cross-wall order. After any
\(q\) labels have crossed, their total probability is at most \(q/h_j\).
The remaining endpoint tail therefore obeys

\[
                         W(q)\ge(1-q/h_j)_+.                      \tag{10}
\]

The right side is convex. Hence it is also a minorant of the lower-convex
tail envelope used by the general Ferrers theorem. For an \(M\)-column
rectangle,

\[
\begin{aligned}
 F_M(w)
 &\ge\min_{x\ge0}(1+x)\{1+M(1-x/h_j)_+\}\\
 &=1+\min\{M,h_j\}.                                               \tag{11}
\end{aligned}
\]

The equality follows because the displayed quadratic is concave on
\([0,h_j]\), so its minimum occurs at \(0\) or \(h_j\); beyond \(h_j\)
it is \(1+x\). This proves (2), with no log-convexity and no control of the
physical order.

For a fixed-endpoint cap chain

\[
                         u<z_0<\cdots<z_{s-1}<v,                  \tag{12}
\]

omit \(u\) and the common prefix \(K_j\). Every remaining suffix is still a
cap by heredity, the map from the conditional family to suffixes is
injective, and its left endpoint is precisely the next label \(z\).
Thus (8)--(11) are actual planar endpoint profiles, not abstract trie tags.
The cup statement is the reflected one, peeling from the right endpoint.

Omitting the prefix costs nothing when counting faces: every suffix is a
face of the original configuration by heredity (and also of the induced
deletion). If the omitted labels must instead be re-embedded to retain a
parent certificate, the repair set has at most \(j+1\le R\) physical labels.
The repair-alphabet theorem charges the arbitrary relocation by at most
\(j+1\) bits coefficientwise. This is negligible at coefficient scale when
\(R=O(\log n)\), though it is not automatically negligible in a
fixed-power estimate.

## 3. A long common prefix is a rooted Boolean shield

Let \(\mathcal C_e,\mathcal U_e\) be cap and cup families with the same
fixed endpoints \(e=(u,v)\). At trie node \(j\), choose any
\(C\in\mathcal A_j\subseteq\mathcal C_e\) and any \(U\in\mathcal U_e\).
For every subset \(S\subseteq K_j\),

\[
                         U\cup S\subseteq U\cup C.                \tag{13}
\]

The right side is ordinary by the exact cap-cup endpoint factorization.
Heredity therefore gives the load-one rooted bank

\[
                         \mathcal B(K_j,U)
                         =\{U\cup S:S\subseteq K_j\},\qquad
                         |\mathcal B|=2^j.                        \tag{14}
\]

More generally, if an external context \(B\), disjoint from the child
support, satisfies \(B\cup U\cup C\) ordinary, then every
\(B\cup U\cup S\) is ordinary. For fixed \((K_j,U)\) the output literally
recovers \(B\) and \(S\), so varying compatible contexts have decoder load
one.

The qualification “compatible” is essential. If records use different cap
tails \(C\) and a context paired with one tail need not coexist with another,
then erasing \(C-K_j\) may merge all records in the node. The pair of
ordinary outputs

\[
                         \bigl(C,\ B\cup U\cup S\bigr)             \tag{15}
\]

does recover the erased tail and has load one, but this is a separated
two-bank, not a single ordinary face. It yields a Cauchy square root unless
an additional splice is proved.

## 4. Entropy forces one local alternative

Set

\[
                         \Lambda=\max_{j<s}\max\{h_j,2^j\}.       \tag{16}
\]

Since \(2^{s-1}\le\Lambda\), one has

\[
                         s\le1+\log\Lambda.                       \tag{17}
\]

Also every \(h_j\le\Lambda\). By (1),

\[
                         H\le\Lambda^s
                           \le\Lambda^{1+\log\Lambda}.            \tag{18}
\]

Writing \(x=\log\Lambda\), equation (18) gives
\(x^2+x-\log H\ge0\), which is exactly (3).

This argument is insensitive to where the entropy occurs. Early entropy is
a robust next-endpoint spectrum; entropy postponed down a nearly unary path
creates a long literal cap prefix and hence the Boolean bank (14).

For cap and cup families simultaneously, apply (3) to fixed-rank slices of
both. If neither side takes its shield alternative and their peeled endpoint
rectangles satisfy the pointwise two-rectangle factorization (3) of
`GENERAL_FERRERS_COMPANION_FLOOR_AND_ENDPOINT_BARRIER.md`, then
(11) supplies the companion floor on one side and (10) supplies a peak on
the other. Concretely, for branch ratios \(h_C,h_U\ge2\),

\[
 \max_Q\frac{C(Q)U(Q)}H
 \ge\frac{\Delta}{8}\,
       \min\{M_C,h_C\}\,M_Uh_U.                                  \tag{19}
\]

This is an exact synchronized reset **under the stated pointwise physical
factorization**. The current coherent-ramp localization does not itself
prove that two simultaneously peeled endpoint rectangles survive in one
parent chart; (19) must not be invoked without that geometric input. In
particular, \(\Delta\) must include the exact conditional-mass fractions
\(m_j/|\mathcal C_e|\) and \(m_k/|\mathcal U_e|\). Dropping those factors
is precisely the error exposed by the regression below.

## 5. Stretchable mass-loss barrier

Take \(2s\) rational points on the upper arc of a circle, together with the
two horizontal endpoints \(u,v\), and let

\[
 \mathcal A=\{\{u,v\}\cup S:S\in\tbinom{[2s]}s\}.                 \tag{20}
\]

Every member is a cap with exact endpoint pair \((u,v)\). Add any fixed cup
\(U\) on the lower arc. Then every union in (13)--(14) is an ordinary face,
so the construction is stretchable and realizes the shield alternative
literally.

The maximum child at every node appends the first still available upper-arc
label. Hence (4) holds. Define the branch's mass-aware relative gain by

\[
                         \Gamma_j=\frac{m_j}{H}h_j.               \tag{21}
\]

For \(m=2s\), direct cancellation of binomial coefficients gives
\(\Gamma_0=2\), and the sequence is nonincreasing; equivalently,

\[
 \frac{\Gamma_{j+1}}{\Gamma_j}
 =\frac{(s-j)^2(2s-j-1)}
        {(2s-j)^2(s-j-1)}\le1\qquad(0\le j<s-1).                 \tag{22}
\]

This proves (5). The last nontrivial prefix has size \(s-1\), so its rooted
shield has \(2^{s-1}\) faces, while Stirling gives

\[
                         2^{s-1}=H^{1/2+o(1)}.                    \tag{23}
\]

Thus a theorem claiming that trie entropy alone yields an
\(Hn^\varepsilon\) one-face bank is false even for a rational convex
configuration. The lost conditional mass must be stored in a second output,
an independently decodable context, or a genuinely compatible external
profile bank. The ambient circle is Boolean and pays globally, so this is
an applicability barrier rather than a sub-half construction.

## 6. Exact residual

Prefix peeling reduces the fixed-pair delta residue to the following
load-sensitive statement:

> Given many actual parent records whose child caps enter one fixed-pair
> trie, either find a high-branch node whose conditional mass times its
> external context degree remains large, or show that the rooted prefix
> shields (14), paired with the erased source/cap outputs as in (15), have
> sufficiently small aggregate Hall/Cauchy load.

Pure rank, trie entropy, low endpoint surplus, and arbitrary relocation of
\(O(R)\) labels are now accounted for. What is missing is cross-context
recovery of the erased tail, not a further local prefix inequality.

## 7. Verification

Run

    python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_fixed_endpoint_prefix_peeling_companion_or_shield.py

The exact verifier:

1. exhausts every nonempty rank-two uniform family on five ordered labels
   and checks the maximum-child product identity and (3);
2. tests every physical ordering of every next-label distribution and
   checks (10)--(11) through the exact lower-convex envelope;
3. realizes the cap/cup peeling and every rooted Boolean union on rational
   circle coordinates; and
4. checks (4)--(5) and the square-root shield scale for middle layers through
   \(2s=32\).

Expected output:

    PASS: fixed-endpoint prefix peeling; families=1023, order_tests=5033, circle=(6, 3, 20, 4), middle=(32, 601080390, 2, 32768)
