# Tagged two-face Carleson: the local theorem is false, the global coefficient theorem survives

**Date:** 2026-08-14  
**Verdict:** two different reuse targets must be separated.

* A universal rank-local bound `K=2^o(r)` for **all** exterior repair
  records is false.  Balanced Pascal cells force
  \[
                    K\ge n^{2c-o(1)}=2^{\Omega(r)},
  \qquad c=1-{1\over4\ln2}=0.639326\ldots .       \tag{1}
  \]
  This is an information-theoretic obstruction to every two-face decoder,
  even one allowed to use the complete projective order type.
* The weaker coefficient-scale target is compatible with this obstruction.
  A length-`O(L)` **label-faithful** pair history, `L=ceil(log_2 n)`, has
  total inverse multiplicity
  \[
                         2^{O(L\log L)}=2^{o(L^2)}            \tag{2}
  \]
  once every local transition has polynomial inverse multiplicity.  The
  proof is a direct reverse-transcript count; no per-level `2^o(r)` estimate
  is required.

There is also a new exact tag-absorption theorem.  One pair-compatible
endpoint reservoir in **each** output face jointly stores both endpoint
symbols and both first-difference blocker tips.  Unlike the earlier
two-ended construction, the two reservoirs need not lie at nonadjacent
edges of one face and no cross-union is needed.  In the entropy-balanced
case the local decoder fibre is at most four.

These results do not yet finish Erdős 838.  They reduce the global route to
one precise condition: along the first-divergence tree, the sum of endpoint
entropy deficits and genuinely unencoded transition data must be `o(L^2)`.
Long insertion chains must be recursively exposed; projective universality
proves they cannot be discharged from nesting alone.

All logarithms below are base two.  `V(P)` includes the empty face.

## 1. A scalable counterexample to rank-local tagged reuse

Let

\[
                         Q_m=T_{m,m/2}
\]

be the balanced strong-glue Pascal cell, for even `m`.  It has

\[
 n_m={m\choose m/2},\qquad
 \log n_m=m-O(\log m),                                  \tag{3}
\]

maximum convex rank at most `m`, and the audited exact recurrence gives

\[
 \log V(Q_m)=c m^2+O(m\log m),qquad
 c=1-{1\over4\ln2}.                                     \tag{4}
\]

Write `v_r` for its graded face numbers.  Choose a modal rank `r`, taking
the last mode if there is a tie, and let `S` be all `r`-faces.  Then

\[
 |S|=v_r\ge {V\over m+1},qquad v_{r+1}\le v_r.           \tag{5}
\]

Also `r<=m`.  Since `v_r<=binom(n,r)<=n^r`, (3)--(5) imply

\[
                         r\ge(c-o(1))m.                    \tag{6}
\]

For a face `A`, put

\[
 q(A)=|Q_m\setminus\operatorname{conv}(A)|=u(A)+e(A),     \tag{7}
\]

where `u` is its ordinary up-degree and `e` is its exterior blocked degree.
The Bernoulli hull partition is the exact identity

\[
              \sum_{A\text{ face}}p^{|A|}(1-p)^{q(A)}=1. \tag{8}
\]

Restrict (8) to `S`, use Jensen, and optimize `p`.  With
`qbar=E_S q(A)` this gives

\[
 \log|S|\le(r+\bar q)H_2\!\left({r\over r+\bar q}\right)
 \le r\log\left(1+{\bar q\over r}\right)+{r\over\ln2}.  \tag{9}
\]

Consequently

\[
 \bar q\ge r\left({|S|^{1/r}\over e}-1\right)
           \ge2^{cm-O(\log m)}.                            \tag{10}
\]

The cover identity in the hereditary face complex gives

\[
 \sum_{A\in S}u(A)=(r+1)v_{r+1}\le(r+1)|S|.               \tag{11}
\]

Subtracting (11) from (10), and then using (5), proves the following.

> **Theorem 1 (full exterior EIC and local two-face reuse fail).**  The
> exterior repair-record family
> \[
>             \mathcal E_m=\{(A,p):A\in S,\ p
>             \text{ exterior blocked for }A\}
> \]
> satisfies
> \[
>             { |\mathcal E_m|\over V(Q_m)}
>                    \ge n_m^{c-o(1)}.                     \tag{12}
> \]
> Hence every map from ordered pairs `E_m^2` to ordered pairs of ordinary
> convex faces has maximum fibre
> \[
>             K_m\ge {|\mathcal E_m|^2\over V(Q_m)^2}
>                    \ge n_m^{2c-o(1)}=2^{\Omega(r)}.       \tag{13}
> \]

The conclusion is independent of decoder design: there are only `V^2`
ordered face pairs.  Retaining both blocker labels, both hidden ears, all
tangent endpoints, and the complete chirotope cannot beat (13).

This kills the strong form of the tagged Carleson conjecture, not capped
RNP.  Capped Hall is allowed to select only the required number of blockers
over each source, while (12) deliberately uses all exterior incidences.

### Fixed insertion-chain version

The projective map in `INSERTION_CHAIN_UNIVERSALITY.md` preserves exterior
blocked incidences as well as convex faces.  Add its three-point base
triangle `B`.  Every point of the transformed `Q_m` lies in one strict
fixed-edge insertion chain.  The records in (12) remain valid, while

\[
                         V(Q_m\cup B)\le 8V(Q_m),            \tag{14}
\]

because a face is determined by its intersections with `Q_m` and `B`.
Thus the local counterexample survives, up to a factor eight, inside the
long-chain branch itself.

## 2. A symmetric two-output endpoint code

The local obstruction above does not rule out balanced selected records.
The following exact decoder is stronger than the previous product-cell
uncrossing theorem in one useful respect: it needs only one active endpoint
reservoir in each history.

For `i=1,2`, let `Q_i` be a labelled endpoint alphabet of size `q_i`, let
`Y_i` be a blocker alphabet of size `y_i`, and let `R_i` range over an
arbitrary labelled family of inner histories.  Let `C_i` be a
fixed collection of endpoint subsets of size at most two which are
compatible with every history `R_i`, and put
`sigma_i=|C_i|`.  Assume the alphabets are
disjoint from the histories and

\[
 R_i\cup E\text{ is a convex face for every }E\in\mathcal C_i. \tag{15}
\]

The repair records on side `i` are triples

\[
                         (R_i,x_i,p_i),qquad
 x_i\in Q_i,\quad p_i\in Y_i.                             \tag{16}
\]

Put

\[
                         s(q)=1+q+{q\choose2}.              \tag{17}
\]

> **Theorem 2 (symmetric one-endpoint-per-output tag absorption).**  Ordered
> pairs consisting of one record of each type in (16) map to ordered face
> pairs
> \[
>                         (R_1\cup E_1,R_2\cup E_2)          \tag{18}
> \]
> with maximum fibre
> \[
> \boxed{
> K=\left\lceil{q_1q_2y_1y_2\over \sigma_1\sigma_2}\right\rceil.} \tag{19}
> \]

**Proof.**  Enumerate the `q_1q_2y_1y_2` four-symbol tuples
`(x_1,x_2,p_1,p_2)` and the `sigma_1 sigma_2` pairs
`(E_1,E_2)` in `C_1 times C_2`.  Map them as evenly as
possible, giving (19).  Equation (15)
proves that both outputs are faces.  From the outputs recover each inner
history by removing its known endpoint alphabet; the finite code then has
at most `K` preimages for the four missing symbols.  QED.

If each `Q_i` is pair-compatible, then `sigma_i=s(q_i)`.  Since
`s(q)>=q^2/2`,

\[
             K\le\left\lceil{4y_1y_2\over q_1q_2}\right\rceil. \tag{20}
\]

In particular `q_1=q_2=y_1=y_2=M` gives `K<=4`.  More generally the local
logarithmic loss is bounded by

\[
 \left[\log y_1+\log y_2-\log q_1-\log q_2+2\right]_++O(1). \tag{21}
\]

Only pair-compatibility within each `Q_i` is used.  The two endpoint cells
can be adjacent, identical in tangent type, or attached to unrelated
histories, because they occur in different output faces.  Thus neither the
nonadjacent-edge condition nor an opposite-side cross-union is required.

The insertion-poset lemma supplies a stronger quantitative version of (15).
Within a fixed insertion edge, compatible pairs are exactly the incomparable
pairs of its dominance poset.  If that poset is `X`, define

\[
 \sigma(X)=1+|X|+\#\{\{x,x'\}:x,x'\text{ incomparable}\}.    \tag{22}
\]

Then all `sigma(X)` endpoint subsets are available in the appropriate
output face.  If `X` has height `h`, ranking by longest chains partitions it
into `h` antichains.  Convexity of `binom(x,2)` gives

\[
                         \sigma(X)\ge {|X|^2\over2h}.        \tag{23}
\]

Thus Theorem 2, without choosing or tagging a largest antichain, yields

\[
 K\le\left\lceil{4h_1h_2y_1y_2\over q_1q_2}\right\rceil.   \tag{24}
\]

This makes the dichotomy exact: small height is a cheap symmetric spend;
large height is the projectively universal nested-chain branch.

## 3. The global full-history fibre theorem

The exact first-divergence identity says that recursion depth costs no pair
mass.  We now bound decoder multiplicity rather than mass.

Call a two-history terminalization **label-faithful** if its two output
faces and local codewords retain both inner child histories and both
entropy-bearing tip symbols at every descent.  On reverse decoding, allow
the following data to be unmarked:

1. the chronology of at most `h` transitions in each history;
2. at most four ordered visible vertices per paired transition--enough for
   the two tangent chords; and
3. one of at most eight transition/orientation types.

The full projective order type is known.  Once these discrete choices and
the retained child histories are fixed, rank-three signs determine the
tangent intervals and validate the unique predecessor records.

> **Theorem 3 (global transcript decoder).**  Suppose `h<=C L`, all active
> faces have at most `L` visible history vertices, and the product of the
> local finite-code fibres is `K_code`.  Then the inverse multiplicity of
> the complete two-history decoder is at most
> \[
> \boxed{
> K_{hist}\le(h!)^2(8L^4)^h K_{code}.}                      \tag{25}
> \]
> In particular, if
> \[
>                         \log K_{code}=o(L^2),              \tag{26}
> \]
> then `K_hist=2^o(L^2)`.  Polynomial local fibres over `O(L)` levels give
> the sharper `K_hist=2^O(L log L)`.

**Proof.**  Guess the two chronological orders, costing at most `(h!)^2`.
Reverse the paired transitions.  At one transition there are at most `L^4`
choices for two ordered tangent chords and eight constant types.  The
retained tips and child histories leave no ambient `n`-point label guess.
Multiply these bounds and the local code fibres.  Since
`h!<=h^h`, `h=O(L)` gives

\[
 \log K_{hist}
 \le2h\log h+h(3+4\log L)+\log K_{code}
 =O(L\log L)+\log K_{code}.                                \tag{27}
\]

This proves the claim.  QED.

The factorials are deliberately robust.  A genuinely recursive decoder
usually recovers the chronology automatically and can omit them.

Theorem 3 is the coefficient-scale Carleson statement requested in the
global attack.  It shows that there is no need to prove `2^o(r)` reuse at
every rank.  The much weaker requirement is

\[
 \sum_{j\le h}\log K_j=o(L^2),                              \tag{28}
\]

where `K_j` is the endpoint/tag code loss at the `j`th first-divergence
cell.  Applying (21), it is enough to control the cumulative positive
endpoint deficit

\[
 \sum_j
 [\log y_{1j}+\log y_{2j}-\log q_{1j}-\log q_{2j}]_+
                         =o(L^2).                           \tag{29}
\]

### Joint coding removes the positive-part loss

Paying `ceil(K_j)` separately is unnecessary.  A full-history encoder can
enumerate all endpoint codewords at once, so surplus capacity at one level
pays a deficit at another.

For each side `a in {1,2}` and level `j<=h`, let the endpoint and blocker
alphabets have sizes `q_(a,j)` and `y_(a,j)`, and let the compatible endpoint
reservoir have size `sigma_(a,j)`.  Assume **stacked compatibility**: for
every tuple of compatible codewords, all its levelwise choices coexist with
the retained inner history in one convex output face on that side, and that
face recovers the inner history and the full codeword tuple.

> **Theorem 4 (global symmetric reservoir code).**  Under stacked
> compatibility, all endpoint and blocker symbols in the two histories map
> to the final two output faces with maximum fibre
> \[
> \boxed{
> K_{joint}=
> \left\lceil
> {\prod_{a=1}^2\prod_{j=1}^h q_{a,j}y_{a,j}
>  \over
>  \prod_{a=1}^2\prod_{j=1}^h\sigma_{a,j}}
> \right\rceil.}                                           \tag{G1}
> \]
> If the endpoint insertion poset at `(a,j)` has height `d_(a,j)`, then
> \[
> \log K_{joint}
> \le\left[
>  \sum_{a,j}\bigl(\log y_{a,j}-\log q_{a,j}
>                    +\log(2d_{a,j})\bigr)
> \right]_++O(1).                                          \tag{G2}
> \]

**Proof.**  Enumerate the complete symbol transcripts and the complete
compatible-codeword transcripts, and distribute the former evenly over the
latter.  Stacked compatibility turns each codeword transcript into one
ordinary face on its side and makes it recoverable.  This proves (G1).
Apply (23), namely `sigma_(a,j)>=q_(a,j)^2/(2d_(a,j))`, to every factor and
take one positive part only after multiplying all levels.  QED.

This global rounding is materially stronger than multiplying the local
ceilings in (19).  An exact oscillating audit has local-ceiling fibre of 497
bits but joint fibre of only 17 bits.

There is a useful telescoping corollary.  Suppose the blocker alphabet at
one level hands off to the next endpoint alphabet with multiplicity
`t_(a,j)`:

\[
                         y_{a,j}\le t_{a,j}q_{a,j+1}.       \tag{G3}
\]

Then, on each side,

\[
 \sum_{j=1}^h(\log y_{a,j}-\log q_{a,j})
 \le \log q_{a,h+1}-\log q_{a,1}
       +\sum_{j=1}^h\log t_{a,j}.                          \tag{G4}
\]

If `h=O(L)`, all heights and handoff multiplicities are polynomial in `L`,
and the boundary alphabets have size at most `n`, equations (G2)--(G4) give

\[
                         \log K_{joint}=O(L\log L).         \tag{G5}
\]

Combined with Theorem 3, this is the requested `2^O(L log L)` full-history
decoder.  Its two genuinely geometric hypotheses are now explicit:

1. endpoint codewords selected at different nested levels coexist in one
   final convex face on each side; and
2. a blocker cloud is handed to the next endpoint cloud with only
   polynomial multiplicity.

No sum of local positive deficits is needed if those hypotheses hold.

### Variable outer cores add only slot-recovery entropy

The symmetric code also resolves the apparent global reuse caused merely by
changing the outer core.  Require its codebook to be canonical once the
labelled core, insertion edge, and transition type are fixed.

> **Theorem 5 (aggregate variable-core reuse).**  Suppose each symmetric
> output has the form `F_i=R_i union E_i`, with `|E_i|<=2`, and has rank at
> most `r+2`.  Across **all** labelled outer cores, guessing the two outputs'
> open slots costs at most
> \[
> \left(\sum_{t=0}^2{r+2\choose t}\right)^2=O(r^4).         \tag{V1}
> \]
> After those guesses the cores are forced by `R_i=F_i-E_i`.  If the
> insertion edge, two tangent chords, and constant transition type are left
> unmarked, the total additional terminal-state fibre is still `r^O(1)`.
> Over `h=O(r)` label-faithful descents its aggregate contribution is
> \[
>                         r^{O(h)}(h!)^2=2^{O(r\log r)}.     \tag{V2}
> \]

**Proof.**  Enumerate the at-most-two-element slot subset in each labelled
output face.  Subtraction recovers the two cores, so the number of possible
cores never appears in the fibre.  There are at most `O(r)` boundary edges
and `O(r^2)` directed chords on each recovered core; constant transition
types add a constant.  Multiply these polynomial choices over the reverse
history and use `h!<=h^h`.  QED.

This theorem answers the terminal-pair reuse question across variable outer
cores: variation of a core is harmless when the output keeps that core.
The load-bearing hypothesis is **canonical recoverability**.  One may not
erase a genuine outer-history label and then distinguish exponentially many
state-dependent codebooks which produce the same `R_i union E_i`.  Fully
tagged histories and canonical order-type codebooks satisfy the hypothesis;
an untagged Proposition-26 descent does not.

For a product grid, removing the open endpoint slots recovers the complete
outside word, so Theorem 5 is exact up to its deliberately generous
polynomial overcount.  For a universal insertion chain it still recovers
the variable core, but the compatible reservoir has only `q+1` members.
Thus a single chain terminal can cost `2^O(r)`, which is allowed by (V2),
whereas repeatedly terminating full-height chains can cost `2^Theta(r^2)`.
Those repeated chains must take the tagged Boolean/recursive branch rather
than be repaid as independent symmetric terminals.

## 4. Regression families

### Product grid and ACP Proposition 26

At a balanced product coordinate, each endpoint and blocker alphabet has
size `M`.  Theorem 2 gives local fibre at most four.  Across `O(L)` exposed
coordinates this contributes only `2^O(L)`, and Theorem 3 contributes the
larger but still harmless `2^O(L log L)` transcript factor.  This is a
direct symmetric decoder; the two-ended nonadjacent reservoir is no longer
needed for this equality family.

### Nested parabola

The endpoint poset is one chain, so Theorem 2 does not apply directly.  The
Boolean prefix bank instead has the sharp pair ratio

\[
                    \max_{d\ge0}{(d+1)^2\over2^d}={9\over4}. \tag{30}
\]

The first-divergence Kraft identity charges a pair once, not once per
prefix.  Hence arbitrary nesting depth remains harmless after full outer
tags are kept.

### Insertion-chain universality

Theorem 1 transfers into one fixed insertion chain by (14).  Therefore a
long chain cannot be declared a cheap terminal merely because its carriers
are comparable.  Its internal order type must be recursively exposed.
This does not contradict Theorem 3: the local lower bound in (13) is only
`2^O(L)`, well inside the allowed global `2^o(L^2)` budget.

### Exact `n=58` record

At rank five, the certified low-addable subfamily already has `15,731,969`
exterior repair records, while `V=1,061,907`.  Thus any two-face decoder on
all those records has fibre at least

\[
 \left\lceil{15,731,969^2\over1,061,907^2}\right\rceil=220. \tag{31}
\]

This kills a small constant claim but is negligible at the full-history
scale.  It is therefore a useful finite check that the local and global
statements have genuinely different strength.

## 5. Exact remaining gate

The counting/reconstruction part of the global Carleson route is now
settled under label-faithful terminalization.  What is not yet proved is a
universal geometric construction of that terminalization.

The remaining statement can be phrased sharply:

> **Balanced antichain-or-tagged-chain gate.**  The pair first-divergence
> tree can be covered by symmetric endpoint terminals satisfying (15), and
> tagged comparable descents, so that the uncovered pair mass is negligible,
> the depth is `O(L)`, and the cumulative deficit (29) is `o(L^2)`.  Every
> long comparable cell is entered with its full inner order type and makes
> sufficient logarithmic progress before it can recur.

Theorem 2 handles the antichain terminal exactly.  The exact Kraft identity
handles branching mass.  Theorem 3 handles global reconstruction.  The sole
unresolved issue is progress through projectively universal long chains.
This is substantially weaker than rank-local EIC and avoids the false
claim killed by Theorem 1.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_cyclic_stem_hw/verify_tagged_full_history.py
```

The exact checker:

* computes the central Pascal graded recurrence through parameter 80 and
  verifies the modal-rank activity lower bounds with integer roots;
* evaluates the exact transcript bound `(L!)^2(8L^4)^L` through `L=1024`;
* constructs balanced and unequal symmetric endpoint codes and checks their
  exact maximum fibres;
* compares global joint enumeration with products of local ceilings on
  balanced, successor-handoff, ramp, and oscillating profiles;
* verifies the variable-core open-slot bound through rank 1,024;
* verifies the nested-prefix constant through depth 512;
* imports the exact insertion-chain transfer certificate; and
* checks the `n=58` fibre lower bound (31) from the independently generated
  circuit-enumeration certificate.

Its output is `tagged_full_history_certificate.json`.
