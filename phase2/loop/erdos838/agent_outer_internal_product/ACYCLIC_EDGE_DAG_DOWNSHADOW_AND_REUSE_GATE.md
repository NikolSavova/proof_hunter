# Acyclic dispersed edges: exact downshadow payment and the source-reuse gate

**Date:** 2026-08-15.  All logarithms are base two.  This continues
`FACE_DEPENDENT_EDGE_DISPERSION_BOOLEAN_SHIELD_BARRIER.md`.

## Verdict

There is an exact recoverable payment from an acyclic dispersed-edge
family.  A random vertex bipartition retains one orientation of at least a
quarter of the weighted carrier contexts.  Let `Z` be the physical
endpoint support of those edges.  For a retained context `(B,e)`, delete
all other labels of `Z` and use

\[
                 \{e\cup F:F\subseteq B\setminus Z\}.    \tag{1}
\]

Every output is ordinary and recovers its physical edge exactly.  Its
global load is at most the **actual fixed-edge fibre weight**, with no
chronology or carrier-description factor.  If the maximum edge fibre is
`delta W`, and an `alpha` fraction of the total context weight has at
least `r` labels outside `Z`, then

\[
                         V\ge {\alpha 2^r\over4\delta}.   \tag{2}
\]

Dispersion also forces

\[
                         |Z|\ge (2\delta)^{-1/2}-1,       \tag{3}
\]

so least-counterexample induction supplies the standalone endpoint bank
`F_C(|Z|)`.

These conclusions are sharp as load statements, but they do **not** prove
the proposed fixed-gap carrier-multiplication trichotomy.  Both (2) and
(3) are standalone banks: the original carrier/source mass `W` cancels
against the fixed-edge completion load.  A stretchable universal-cage
example admits an arbitrary actual source-face alphabet `A`; the records

\[
                        \mathcal A\times L\times R       \tag{4}
\]

have total mass `W=|A|s^2` and edge density `1/s^2`, while every endpoint
downshadow output forgetting `A` has source load as large as `|A|`.
The endpoint shield and the source bank are real, but they are not
automatically multiplied.

Thus the corrected unconditional statement still needs one extra
hypothesis/conclusion:

* a mixed/return output retaining a recoverable source-face code; or
* a detached shield that contains the carrier/source code, not merely the
  dispersed physical endpoints; or
* a canonical normalization bounding aggregate source reuse per
  `(edge,residual)` output.

Carrier heredity and an acyclic endpoint DAG alone stop at (2)--(3).  The
actual stretchable example below is a local critical-reuse barrier, not a
global low-face counterexample: one-ended child profiles may still pay.
No coefficient-half closure is claimed.

## 1. Exact DAG bipartition

Let `Omega` be a finite weighted family of canonical contexts

\[
                         \omega=(B_\omega,e_\omega,w_\omega),     \tag{5}
\]

where `B_omega` is an ordinary face, `e_omega={u,v}` is a distinguished
boundary edge of it, and `w_omega>=0`.  Put

\[
 W=\sum_\omega w_\omega,\qquad
 W_e=\sum_{\omega:e_\omega=e}w_\omega,
 \qquad \max_e W_e\le\delta W.                          \tag{6}
\]

The edge may already be directed by its child chamber; acyclicity is not
needed for the following constant-loss step.

### Lemma 1 (one oriented bipartite quarter)

There is a partition of the physical endpoint labels into `L,R` and a
subfamily `Omega'` of total weight at least `W/4` such that every selected
edge is directed from `L` to `R`.

**Proof.**  Color every endpoint label independently `L/R`.  A directed
edge has probability `1/4` to have its tail in `L` and head in `R`.
Linearity of expectation gives a coloring retaining weight at least
`W/4`. `square`

If the edge graph is a DAG, a random cut of any fixed topological order
gives the same statement.  No conclusion about a directed cycle follows:
the complete bipartite orientation `L to R` is the equality model.

## 2. Endpoint-excluding downshadow decoder

Fix the partition from Lemma 1 and let

\[
              Z=\bigcup_{\omega\in\Omega'}e_\omega,
              \qquad I_\omega=B_\omega\setminus Z.      \tag{7}
\]

For each selected context form all outputs

\[
                         U(\omega,F)=e_\omega\cup F,
                 \qquad F\subseteq I_\omega.            \tag{8}
\]

### Theorem 2 (recoverable dispersed-edge downshadow)

Every output in (8) is ordinary.  Moreover

\[
                      U\cap Z=e_\omega,                 \tag{9}
\]

so a fixed output has total generating weight at most
`W_{e_omega}<=delta W`.  Consequently

\[
 \boxed{\quad
 V\ge {\sum_{\omega\in\Omega'}w_\omega2^{|I_\omega|}
                  \over\delta W}.
 \quad}                                                  \tag{10}
\]

If selected contexts of total weight at least `alpha W/4` have
`|I_omega|>=r`, then (10) gives (2).

**Proof.**  Each output is a subset of the ordinary face `B_omega`.
Because `F` avoids all of `Z`, (9) recovers the distinguished physical
edge from the output.  Any remaining generator of the same output belongs
to the fixed edge fibre, whose total weight is bounded in (6).  Weighted
incidence counting proves (10). `square`

The deletion of `Z-e_omega` is essential.  If other used endpoints are
allowed to remain, one output need not identify which of its many pairs
was the distinguished edge, introducing an additional rank-squared load.

## 3. The induced endpoint shield

Let `m` be the number of distinct selected physical edges.  The selected
weight is at least `W/4`, while every edge carries at most `delta W`; hence

\[
                         m\ge {1\over4\delta}.            \tag{11}
\]

A simple graph on `z=|Z|` vertices has at most `binom(z,2)` edges, so

\[
 z\ge {1+\sqrt{1+2/\delta}\over2}
       \ge (2\delta)^{-1/2}.                             \tag{12}
\]

As `Z` is an actual induced subset of a least counterexample, induction
gives

\[
                         V(P|Z)\ge F_C(z).                \tag{13}
\]

For the critical density `delta=p^{-theta_*}`, this only says

\[
 z\ge p^{\theta_*/2-o(1)},\qquad
 \log F_C(z)\ge {\theta_*^2\over8}(\log p)^2
                         -O_C((\log p)\log\log p).       \tag{14}
\]

This is a substantial detached endpoint bank, but it is not the product
of that bank with `W`.  When `log W` already has coefficient `1/2`, (14)
is exponentially smaller than `W p^{theta_*}`.  This is the exact scale
at which a source-retaining decoder is still required.

## 4. Stretchable actual-source reuse

The cancellation of `W` in (10) is geometrically real.  Use the rational
carrier endpoints `L,R` and the universal child cage from
`FACE_DEPENDENT_EDGE_DISPERSION_BOOLEAN_SHIELD_BARRIER.md`, but take the
carrier face to be only

\[
                              B_{\ell r}=\{\ell,r\}.      \tag{15}
\]

Let `Q` be any finite rational order type embedded by the universal affine
map, and let `A` be its family of intrinsic ordinary faces of rank at
least two.  For every

\[
                         (A,\ell,r)\in\mathcal A\times L\times R,\tag{16}
\]

the source face `A` is actual and retained before the terminal deletion.
Every singleton `x in A` satisfies

\[
                B_{\ell r}\cup\{x\}\text{ convex},       \tag{17}
\]

whereas every residual `A' subseteq A` of rank at least two satisfies

\[
                B_{\ell r}\cup A'\text{ nonconvex}.       \tag{18}
\]

Thus (16) is an actual, metadata-free terminal record rectangle of size

\[
                         W=|\mathcal A|s^2.              \tag{19}
\]

Each physical edge occurs in exactly `|A|` records, so its fibre density
is exactly `1/s^2`.  The endpoint edge/shield geometry is unchanged, but
an output `B_{ell r} union {x}` has load

\[
                         |\{A\in\mathcal A:x\in A\}|,    \tag{20}
\]

which can be a fixed positive fraction of `|A|` (for a Boolean child it
is exactly `2^{q-1}-1`).  This is precisely the source mass cancelled by
the denominator in (10).

The construction still has the actual intrinsic source bank `|A|` and
the actual detached endpoint bank.  It does not show that *all* one-ended
mixed profiles are small, so it is not a counterexample to a trichotomy
that explicitly includes a recoverable return/profile module.  It is an
exact counterexample to deriving the required carrier-mass multiplier
from endpoint dispersion, acyclicity, heredity, and the two standalone
banks alone.

## 5. Verification

`verify_acyclic_edge_dag_downshadow_reuse.py` checks:

1. the weighted quarter-cut and exact inequalities (10)--(12) on finite
   rational weights;
2. the endpoint-excluding decoder and its exact fibre load;
3. the rational universal-cage source rectangle for `s=3` and a
   seven-label Boolean source; and
4. the exact source codegrees (20), edge density `1/9`, and acyclic
   `K_{3,3}` orientation.

