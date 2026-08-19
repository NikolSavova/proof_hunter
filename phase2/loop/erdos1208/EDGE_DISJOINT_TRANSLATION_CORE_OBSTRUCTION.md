# Generic edge-disjoint translation cores have no distance-Sidon geometry

## 1. Result

This note closes the canonical component-faithful, generic part of the
abelian translation-invariant branch of the full eight-corner problem.
`NONGENERIC_TRANSLATION_CORE_OBSTRUCTION.md` now extends the exhaustion to
every additional endpoint identification and removes the genericity caveat.

Let the relation records be a finite elementary abelian group

\[
 V=\mathbb F_2^m,
\]

and let the eight corner colours be eight distinct nonzero translations

\[
 \tau_\epsilon(x)=x+v_\epsilon,
 \qquad \epsilon\in\{0,1\}^3.                  \tag{1.1}
\]

For endpoint role `(r,b)`, let

\[
 H_{r,b}=\langle v_\epsilon:\epsilon_r=b\rangle. \tag{1.2}
\]

The endpoint label of a record is its coset modulo `H_(r,b)`.  Every corner
fibre has size at least two, because `v_epsilon` belongs to each of its three
selected face spaces.

**Theorem 1.1 (exhaustive generic translation-core obstruction).**  Suppose
the eight shifts span `V`, are distinct and nonzero, and the six endpoint
labels jointly recover every record.  In the universal solution of the
Gaussian relation

\[
 a_0-a_1-b_0+b_1-Jc_0+Jc_1=0                  \tag{1.3}
\]

coalesce all endpoint labels which are identically equal in every solution.
Then one of the following holds:

1. the simultaneous full eight-corner core is empty after this canonical
   coalescing; or
2. two distinct unordered pairs of the remaining endpoint labels have the
   same directed displacement, and hence the same Euclidean distance.

Consequently there is no generic, component-faithful distance-Sidon
realization of a connected edge-disjoint translation-invariant full core.
The theorem proved in this note alone does **not** rule out a further
nongeneric specialization.  The subsequent exact partition closure does;
noncommuting corner matchings and the full size-biased tail remain open.

## 2. Fourier reduction

Put

\[
 U_{r,b}=H_{r,b}^\perp\subseteq V^*.
\]

An endpoint function `f_(r,b):V/H_(r,b)->C` has Fourier support in
`U_(r,b)`.  Taking the Fourier coefficient of (1.3) at a character `chi`
gives one Gaussian-linear equation among exactly the endpoint roles whose
annihilators contain `chi`.  Therefore a nonzero Fourier coefficient in one
role is possible only when `chi` belongs to at least two of the six
annihilators.  Call such a nonzero character **active**.

This gives the canonical coalescing and then a short universal collision
certificate.

### 2.1 Canonical point coalescing

If `d notin H_(r,b)` but every active character of `U_(r,b)` annihilates
`d`, then

\[
 f_{r,b}(x+d)=f_{r,b}(x)                       \tag{2.1}
\]

for every solution and every `x`.  For each endpoint role, let `K_(r,b)` be
the common kernel of all its active characters.  The universal point forms
therefore factor through `V/K_(r,b)`, and a generic specialization separates
exactly those quotient labels.

Let

\[
 K_*=\bigcap_{r,b}K_{r,b}.
\]

After deduplicating relation records modulo `K_*`, the corner fibre for
`epsilon=(i,j,k)` has size

\[
 {|K_{a,i}\cap K_{b,j}\cap K_{c,k}|\over |K_*|}. \tag{2.2}
\]

If this ratio is one for any corner, translation invariance makes that
projection entirely degree one, so the simultaneous full core peels to the
empty set.

### 2.2 Parallelogram certificate after coalescing

Suppose `d,h,d+h notin K_(r,b)` and there is no active character `chi` with

\[
 \chi(d)=\chi(h)=1.                            \tag{2.3}
\]

For a Fourier character, the second difference

\[
 \Delta_h\Delta_d f(x)
\]

is nonzero only when (2.3) holds.  Hence every solution satisfies

\[
 f(x+d)-f(x)=f(x+h+d)-f(x+h).                  \tag{2.4}
\]

The four cosets are distinct.  If the point map is injective, (2.4) gives
two distinct point-pairs with identical directed displacement, contradicting
distance-Sidonicity.

The verifier checks that every translation system either loses its full
core under the canonical coalescing or has this collision certificate.

## 3. Why the enumeration is complete

Because the shifts span `V`, write them as the columns of a full-rank
`m`-by-8 binary matrix.  Changing coordinates in `V` performs invertible row
operations, so the configuration is determined uniquely by the row space

\[
 R\le\mathbb F_2^8.                            \tag{3.1}
\]

Conversely every row space gives one labelled shift configuration from its
unique reduced-row-echelon generator.  The shifts are nonzero and distinct
exactly when the eight columns are nonzero and distinct.  Since eight
vectors span `V`, only dimensions `1<=m<=8` occur.

The verifier generates every RREF subspace and independently checks the
count against the Gaussian binomial coefficient.  It then applies three
exact tests:

1. `intersection(H_(r,b))={0}`, so the six endpoint labels recover records;
2. the canonical active-character coalescing and the resulting full-core
   profile; and
3. the parallelogram certificate on every surviving core.

The complete profile is

| class | count |
|---|---:|
| nonzero subspaces of `F_2^8` | 417,198 |
| simple eight-column systems | 50,864 |
| record collapse | 22,894 |
| formal full cores before coalescing | 27,970 |
| canonically coalesced core becomes empty | 27,389 |
| surviving core with forced parallelogram | 581 |
| survivors | **0** |

Among these are 332 systems whose original corner fibres all have exactly
two records.  After canonical coalescing, 219 lose the full core and 113
retain a core with a parallelogram collision.

Run

```bash
python3 phase2/loop/erdos1208/verify_edge_disjoint_translation_core_obstruction.py
```

The enumeration uses only integer bit operations and assertions; there is
no randomized or floating-point step.

## 4. Strategic consequence

The obstruction is stronger than the earlier canonical-cube computation.
It rules out the generic component-faithful geometry of every abelian
eight-matching core, including cores with larger corner fibres.  A genuine
full core inside a distance-Sidon set must therefore derive its survival
either from **noncommuting matching curvature** or from a nongeneric pattern
of additional endpoint identifications.  Both are concrete structural
alternatives absent from the canonical cube.

The smallest fully point-separated exact translation control has 64 records,
32 formal points, and 32 forced distance repetitions.  An exact local audit
performs every one of its 7,936 possible single two-edge switches.  Of
these, 896 collide with another corner colour and 6,784 destroy corner
linearity.  All 256 admissible noncommuting switches have the same profile:
29 formal points and 37 forced repetitions.  Thus a single local departure
from commutativity moves strictly away from a generic counterexample.  Run

```bash
python3 phase2/loop/erdos1208/search_matching_switch_full_core.py \
  --exhaust-one-switch
```

This is a local basin certificate, not a global theorem about noncommuting
systems.

This gives a concrete next dichotomy for the size-biased tail:

1. an approximately commuting region should be compared with the finite
   translation obstruction above; while
2. abundant commutator defects must be charged to endpoint data or to
   growth in `D+D`.

Making that stability/curvature dichotomy quantitative is still open.  The
present theorem is a complete branch result, not a resolution of #1208.
