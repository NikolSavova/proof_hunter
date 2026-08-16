# Quadratic base-word entropy defeats detached-cloud recovery

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

**Scale update.**  `FULL_WORD_TRIANGLE_REUSE_SCALE_BARRIER.md` proves the
exact split-overlap internal-triangle Cauchy theorem.  On this tensor it
gives only `V>=Omega(sqrt(M)m^2)`, which is asymptotically weaker than the
existing source bank `V>=M` when `log M=Theta((log n)^2)`.  Thus the
quadratic-word construction remains a valid overlap/applicability barrier;
it is not closed by canonical per-source weights alone.

The adjacent double-dominance residue can be tensored with a
quadratic-entropy family of actual convex bases while reusing exactly the
same two detached clouds.  For `q` base roles with `D` choices each there
are

\[
                              M=D^q                              \tag{1}
\]

base words.  Every word supports the full `m by m` source--release
rectangle and preserves all targets `W,Q,C,A,E`, the two adjacent actual
gaps, and every singleton guard--pocket cross face.  Yet:

* the complete base-retaining two-cloud bank has exactly
  `M(m+1)^2` faces, only the marked rectangular scale;
* any output lying wholly in the detached guard/pocket clouds is reused by
  all `M` base words; and
* even if a detached output is augmented by at most `h` selected base-role
  labels, some output has load at least

\[
 \boxed{\displaystyle
 {D^{q-h}\over(q+1)2^q}.}                               \tag{2}
\]

With `q=Theta(log n)` and `log D=(1-o(1))log n`, reducing (2) to
`n^{o(loglog n)}` requires

\[
                           q-h=o(\log\log n).            \tag{3}
\]

Thus a bounded-overlap detached profile bank must retain essentially the
entire base word, not one root, carrier edge, tangent state, or a bounded
number of marks.

The rooted clouds can independently have arbitrary prescribed rational
order types, by the fixed-edge projective-universality theorem.  Therefore
their detached face complexes need not be Boolean and may be chosen as
arbitrary low-face children.  This is a scalable planar barrier to any
rectangle-only detached-bank theorem.  It is not a global low-face
counterexample: the base transversals themselves supply `M` ordinary
faces, and additional cross-profile faces may exist.  A positive proof
must use history which recovers almost every base role, or a new global
composition theorem beyond the listed banks.

## 1. A quadratic family of convex base words

Fix

\[
                 l=(-3,0),\qquad r=(3,0),\qquad t=(0,5).           \tag{4}
\]

For `1<=k<=q`, put `s_k=k/(q+1)` and

\[
 z_k=(-3+3s_k-s_k(1-s_k),\ 5s_k+s_k(1-s_k)).            \tag{5}
\]

The points `z_k` lie, in order, on a strictly convex rational arc from
`l` to `t`, outside the edge `tl` of the triangle `lrt`.  Hence

\[
                         l,r,t,z_q,z_{q-1},\ldots,z_1              \tag{6}
\]

is a strictly convex cyclic word.

Around every `z_k` choose a sufficiently small rational open disk and put
inside it a `D`-point role cell `Z_k`.  The cells may have independently
arbitrary rational order types.  Strict separation at the macro polygon
implies that every transversal

\[
 B_\omega=\{l,r,t\}\cup\{z_{k,\omega_k}:1\le k\le q\},
 \qquad \omega\in[D]^q,                                 \tag{7}
\]

is convex in the same cyclic order.  The two literal edges `lr` and `rt`
remain consecutive in every word.  Generic rational perturbations inside
the disks remove all cross-cell collinearities without changing these
strict signs.  Different words retain different role labels, so (7)
already gives exactly `M=D^q` distinct ordinary faces.

Taking `q=kappa log n` and `D=Theta(n/q)` uses `Theta(n)` labels and gives

\[
                  \log M=(\kappa-o(1))(\log n)^2.        \tag{8}
\]

Thus the source/base context family has the live quadratic entropy rather
than merely polynomial size.

## 2. Common adjacent rooted clouds

Put

\[
                              v=(-2,-1),\qquad u=(2,-1). \tag{9}
\]

Choose an `m`-point pocket cloud `X` in a tiny ear cell below `lr`, and an
`m`-point guard cloud `G` in a tiny ear cell exterior to `rt`, with the
following strict reset property:

\[
\begin{array}{ll}
 B_\omega\cup\{x\},\ B_\omega\cup\{g\},\
 B_\omega\cup\{g,x\}\text{ are convex},& g\in G, x\in X,\\
 B_\omega\cup\{x,x'\},\ B_\omega\cup\{g,g'\}
       \text{ are nonconvex},&x\ne x',\ g\ne g'.       \tag{10}
\end{array}
\]

These properties hold uniformly over all words because the role disks in
(7) are chosen after the fixed strict cage margins.

There are two equivalent exact constructions of the clouds.

1. The explicit rational double chains (14)--(15) of
   `DENSE_RECTANGLE_ACTUAL_GAP_FAN_GATE.md` satisfy (10).
2. More strongly, apply Theorem 2 of
   `SINGLETON_RESET_PROJECTIVE_UNIVERSALITY.md` independently at roots
   `lr` and `rt`.  To see the required localization explicitly, first
   apply its affine order-type map in tangent coordinates and then replace
   `(A_i,B_i)` by `(A_0,B_0)+epsilon(A_i,B_i)`.  For sufficiently small
   positive rational `epsilon`, the inverse projective map places the
   entire cloud in an arbitrarily small neighborhood of the prescribed
   ear point while preserving all strict dominance signs and the detached
   order type.  Full containment makes every
   same-cloud rooted pair bad.  Smallness and openness preserve every
   cross union in the first line of (10).

Thus `G` and `X` may be arbitrary rational low-face children; dominance
nesting constrains only their relation to the fixed roots, not their
detached convex-subset complexes.

For every `(omega,i,j)` define

\[
\begin{aligned}
 A_{\omega,i}&=B_\omega\cup\{g_i\},&
 C_{\omega,j}&=B_\omega\cup\{x_j\},\\
 W_j&=\{x_j,v\},&Q_\omega&=B_\omega\cup\{v\},\\
 E_{\omega,i}&=B_\omega\cup\{g_i,v,u\}.                \tag{11}
\end{aligned}
\]

All five targets are ordinary.  Also

\[
                     B_\omega\cup\{g_i,x_j,v\}
                     \text{ is nonconvex},              \tag{12}
\]

because `v` lies strictly inside `triangle(l,x_j,r)`.  Hence this is an
actual detached record, not an attached one.  The guard insertion edge is
`rt` in every released column and the pocket insertion edge is `lr` in
every source row.  The pair ear `E` and the actual-gap states are therefore
preserved exactly.

There are `Mm^2` records.  Their named target counts are

\[
 |\{W\}|=m,\quad |\{Q\}|=M,\quad
 |\{A\}|=|\{C\}|=|\{E\}|=Mm.                           \tag{13}
\]

The large Hall density is not a formal duplicate: `(A,C)` recovers
`(B_omega,g_i,x_j)` and has unit multiplicity.

## 3. Exact base-retaining classification

Convex position is hereditary.  Hence the bad same-cloud pairs in (10)
remain bad after adding labels from the other cloud.  Conversely every
choice using at most one label from each cloud is covered by the first
line of (10).  Therefore

\[
 B_\omega\cup S_G\cup S_X\text{ is convex}
 \quad\Longleftrightarrow\quad |S_G|\le1, |S_X|\le1.   \tag{14}
\]

For one word this gives `(m+1)^2` base-retaining faces; role labels recover
the word, so over all words it gives exactly

\[
                              M(m+1)^2.                  \tag{15}
\]

This includes the complete row and column actual-gap fan banks.  It is
only a constant-factor enlargement of the `Mm^2` marked records and has no
`n^{Theta(loglog n)}` surplus.

The arbitrary-order-type upgrade does not alter (14): if two labels lie
in one reset cloud, the earlier is in the root triangle of the later and
is hidden regardless of the other labels.  Therefore (15) is exact even
when the detached child face complexes themselves are arbitrary.

## 4. Detached recovery needs almost the full base word

Let `U` be any ordinary output depending only on labels in the common
detached clouds `G union X` and on the fixed anchors `l,r,t,u,v`.  In the
full detached profile bank the same `U` is generated over every word
`omega`, so its base-history load is exactly `M`.  Choosing only one
different `U` per word can encode history, but discards the profile-bank
multiplier; the statement here concerns the summed bank in which every
available detached output is generated over every base word.

Suppose a proposed decoder augments `U` by at most `h` labels from the
chosen base transversal.  A base label records both its role `k` and its
value `omega_k`.  The number of possible augmented marks is at most

\[
                 S_h=\sum_{s=0}^h{q\choose s}D^s
                    \le(q+1)2^qD^h.                    \tag{16}
\]

There are `M=D^q` word occurrences of the fixed detached output.  By the
pigeonhole principle:

> **Theorem 1 (external decoder lower bound).**  Any routing which emits
> one such augmentation per base word has an output of word load at least
> (2).  If the retained positions are a fixed set of `h` roles, the exact
> load is `D^(q-h)`.

No geometric assumption enters this count.  It remains valid if the
choice of up to `h` retained roles depends arbitrarily on the full word,
the detached face, or the chronology.

Under the asymptotic choice in (8), taking logarithms in (2) gives

\[
 \log\operatorname{load}
    \ge(q-h)\log D-q-\log(q+1).                         \tag{17}
\]

For this to be `o((log n)loglog n)`, equation (3) is necessary.  Retaining
one root or tangent state, `O(1)` carrier labels, or even
`q-Omega(loglog n)` base roles leaves at least the forbidden
`n^{Omega(loglog n)}` load.

This is the exact missing coexistence/decoder condition.  A useful
detached-cloud theorem must either attach almost all of `B_omega`, which
returns to the baseline classification (14), or exploit external history
which already encodes almost the entire base word at subpower cost.

## 5. Scope

The construction is an exact scalable regression against the proposed
bounded-overlap detached chain/profile bank.  It carries quadratic source
entropy, actual source faces, releases, pair ears, detached endpoints, and
actual-gap states.  It also permits arbitrary low-face children in every
base role and in both reset clouds.

It does not provide an upper bound on all ordinary faces of the complete
point set and therefore is not claimed as an EIC counterexample.  In
particular, strong composition among the `q` base-role cells may create
additional ordinary faces.  The theorem proved here is the sharp decoder
barrier: those extra faces, rather than the named detached or rooted
banks, are necessary for any unconditional closure.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_quadratic_base_word_reuse.py
```

Expected output:

```text
PASS: quadratic base words, all target/gap states, exact baseline bank, and decoder load
```
