# Erdős 791 full attack: analytic compactness and amplification

Date: 2026-08-13

## Verdict

The normalized-limit problem is not closed.  This lane proves two structural
results that sharply locate the obstruction:

1. **All fixed-modulus information is still incomplete.**  A basis sequence
   has a compact limit on `[0,1] times Z-hat` which retains every fixed residue
   class, but the resulting profinite convolution relaxation has exactly the
   same optimum as the ordinary continuous convolution relaxation.
   Consequently, a complete compactness hierarchy must resolve a modulus or
   spatial scale growing with the basis size.
2. **A finite cross-cover is a genuine one-certificate amplifier.**  If a
   finite basis can cover its interval as `V+H` with almost no duplicated role
   cost, one explicit mixed-radix construction amplifies it to arbitrarily
   large bases without losing its normalized ratio.  An `o(k)` cross-cover
   defect along a limsup-extremal sequence would prove existence of the full
   limit.  This defect lemma remains unproved and small extremizers show it is
   not a formal property of all bases.

No conjectural step below is used as a theorem.

## 1. Current status rechecked

For

\[
 R(k)=\max\{n:\exists A\subseteq[0,n],\ |A|\leq k,
                    [0,n]\subseteq A+A\},
\]

put

\[
 \alpha_- = \liminf R(k)/k^2,\qquad
 \alpha_+ = \limsup R(k)/k^2.
\]

The published bounds remain

\[
 \frac{85}{294}\leq\alpha_-\leq\alpha_+\leq0.4585\ldots .
\]

The lower construction is Kohonen
([arXiv](https://arxiv.org/abs/1606.04770)); the analytic upper bound is Yu
([DOI](https://doi.org/10.1016/j.jnt.2015.04.007)).  Faust--Tait explicitly
state equality of the lower and upper asymptotic constants as open in
[Conjecture 1.5](https://arxiv.org/abs/2507.23627), and Nathanson's May 2026
[structural paper](https://arxiv.org/abs/2605.26425) again describes the
asymptotic program as unsuccessful.  Thus proving `alpha_-=alpha_+`, even
without identifying their common value, would be new relative to these
sources.

## 2. Established: the profinite compactness theorem

Let `Z-hat` be the profinite completion of the integers and let `h` be its
Haar probability measure.  Addition on

\[
 X=[0,1]\times\widehat{\mathbb Z}
\]

is coordinatewise (the real coordinate lands in `[0,2]`).  Write `mu*mu` for
the pushforward of `mu times mu` by this addition map.

### Theorem 2.1 (every basis sequence has a residue-aware limit)

Suppose `A_j` has size `k_j`, covers `[0,N_j]`, and
`(N_j+1)/k_j^2 -> c>0`.  There is a subsequence and a probability measure
`mu` on `X` such that

\[
 \boxed{\mu*\mu\ \geq\
 2c\,\bigl(\lambda|_{(0,1)}\times h\bigr).}                 \tag{P}
\]

This simultaneously retains the limiting coverage demand in every fixed
residue class modulo every fixed integer.

#### Proof

Put `M_j=N_j+1` and embed each integer in `Z-hat`.  Define

\[
 \mu_j=\frac1{k_j}\sum_{a\in A_j}
       \delta_{(a/M_j,\widehat a)}.
\]

Compactness gives a weakly convergent subsequence `mu_j -> mu`.

Select one unordered representation of every `n=0,...,N_j`.  From the
selected pairs make a symmetric submeasure `nu_j` of
`(mu_j times mu_j)/2`: for a selected off-diagonal pair `{a,b}`, take both
ordered atoms with mass `1/(2k_j^2)`; for a selected diagonal pair take its
single ordered atom with mass `1/(2k_j^2)`.  No unordered pair is selected
twice, since its sum is fixed, so indeed

\[
 \nu_j\leq(\mu_j\times\mu_j)/2.                             \tag{2.1}
\]

The addition pushforward of `nu_j` differs in total variation by at most
`1/(2k_j)` from

\[
 \tau_j=\frac1{k_j^2}\sum_{n=0}^{M_j-1}
              \delta_{(n/M_j,\widehat n)},                  \tag{2.2}
\]

because only the at most `k_j` diagonal targets have half weight.

For every continuous real test function and every cylinder
`r mod q`, the corresponding part of (2.2) is a Riemann sum over one fixed
arithmetic progression.  Therefore

\[
 \tau_j\ \longrightarrow\ c(\lambda\times h).              \tag{2.3}
\]

Equivalently, a macro interval of length `L` and one residue modulo `q`
contains `M_j L/q+O_{q}(1)` targets.  This convergence on continuous cylinder
functions determines the product measure.

Take a further weak limit `nu_j -> nu`.  Products also converge weakly, and
(2.1), tested against nonnegative continuous functions, gives
`nu <= (mu times mu)/2`.  Equations (2.2)--(2.3) give
`addition#nu=c(lambda times h)`.  Pushing the domination forward proves (P).

### Theorem 2.2 (profinite fixed-residue data gives no stronger constant)

Define

\[
 C_{\rm prof}=\sup\{c:\exists\mu\in\mathcal P(X),\
       \mu*\mu\geq2c(\lambda|_{(0,1)}\times h)\}
\]

and

\[
 C_{\rm conv}=\sup\{c:\exists\sigma\in\mathcal P([0,1]),\
       \sigma*\sigma\geq2c\lambda|_{(0,1)}\}.
\]

Then

\[
 \boxed{\alpha_+\leq C_{\rm prof}=C_{\rm conv}.}           \tag{2.4}
\]

#### Proof

Theorem 2.1 gives the first inequality.  Projecting a profinite feasible
measure onto `[0,1]` gives a continuous feasible measure, so
`C_prof<=C_conv`.  Conversely, if `sigma` is continuously feasible, take

\[
 \mu=\sigma\times h.
\]

Haar measure is idempotent under convolution, `h*h=h`, and hence

\[
 \mu*\mu=(\sigma*\sigma)\times h.
\]

This proves `C_prof>=C_conv` and therefore equality.

### Consequence

Adding residues modulo `2`, then `4`, and ultimately every *fixed* modulus to
the continuous bin hierarchy cannot recover pointwise lattice coverage.  The
product-Haar lift is an explicit false-positive model for every such fixed
residue hierarchy.  A potentially complete hierarchy must retain a modulus
`q=q(k)->infinity`, a mesh comparable to the lattice spacing, or equivalent
mesoscopic collision/difference information.  This is a theorem about this
class of compact relaxations, not a no-go result for every analytic method.

## 3. Established: a cross-cover amplification theorem

### Definition

For an interval basis `A subset [0,n]`, define its cross-cover cost

\[
 \chi(A,n)=\min\{|V|+|H|:V,H\subseteq A,\ [0,n]\subseteq V+H\}.
\]

An element in both `V` and `H` pays twice.  Coverage of zero forces zero to
belong to both roles.

### Theorem 3.1 (one finite cross-cover amplifies at fixed additive order)

If `[0,n] subset V+H` and `L=|V|+|H|`, then for every integer `q>=1` the set

\[
 B_q=\bigcup_{v\in V}\bigl(vq^2+[0,q-1]\bigr)
 \ \cup\
 \bigcup_{h\in H}\bigl(hq^2+q[0,q-1]\bigr)                 \tag{3.1}
\]

has at most `Lq` elements and covers

\[
 [0,(n+1)q^2-1]\subseteq B_q+B_q.                          \tag{3.2}
\]

Consequently,

\[
 \boxed{\alpha_-\geq\frac{n+1}{L^2}.}                     \tag{3.3}
\]

#### Proof

Every `z in [0,q^2-1]` has a unique expression `z=x+qy` with
`0<=x,y<q`.  Write the macro digit `s in [0,n]` as `s=v+h`.  Then

\[
 sq^2+z=(vq^2+x)+(hq^2+qy),
\]

which proves (3.2).  The two unions in (3.1) contain at most `q|V|` and
`q|H|` elements, and all their elements lie below the endpoint in (3.2).
Finally, for arbitrary `K`, use
`q=floor(K/L)` and monotonicity of `R(K)` to obtain (3.3).

This differs from the ordinary Cartesian product, whose cardinalities
multiply and whose efficiency collapses.  Here the two complementary micro
roles create `q^2` sums from `O(q)` elements while keeping additive order two.

### Corollary 3.2 (a precise sufficient lemma for existence of the limit)

Suppose there is a sequence of bases `A_j`, with sizes `k_j` and ranges `n_j`,
such that

\[
 n_j/k_j^2\to\alpha_+,\qquad
 \chi(A_j,n_j)/k_j\to1.                                    \tag{3.4}
\]

Then

\[
 \boxed{\alpha_- = \alpha_+.}
\]

Indeed, apply (3.3) to each `A_j` and let `j` tend to infinity.  Thus the
following is an exact missing lemma for this amplification route:

> **Cross-cover defect lemma (unproved).** Limsup-extremal bases can be chosen
> with `chi(A,n)=|A|+o(|A|)`.

The condition is sufficient, not claimed necessary for limit existence.

## 4. Adversarial tests of the cross-cover route

The condition is not automatic.

* Exhaustive enumeration of every extremal basis for `1<=k<=7` gives best
  cross-cover costs `2,4,5,8,9,10,11`, while the corresponding ranges are
  `0,2,4,8,12,16,20`.  The unique `k=4` extremizer requires both roles on all
  four elements, so finite extremality alone gives no small defect.
* On the positive side, the elementary family

  ```text
  A_t = [0,t-1] union t[1,t]
  V_t = [0,t-1]
  H_t = t[0,t]
  ```

  has `|A_t|=2t`, cross-cover cost at most `2t+1`, and covers through
  `t^2+t-1`.  It therefore has vanishing relative defect and recovers the
  classical `1/4` asymptotic coefficient by Theorem 3.1.

The exact script `bipartite_blowup.py` checks all small extremizers, constructs
49 literal blow-ups (`q<=7`), and verifies the elementary certificates through
`t=8`.  Its output is `BIPARTITE_BLOWUP_CHECK.json`.

These checks neither prove nor disprove the asymptotic defect lemma.  They show
why it cannot be asserted solely from `A+A` coverage.

## 5. Audit of the carry-bin hierarchy

The root lane's dyadic flow hierarchy was independently checked.  Its factors
are consistent:

* combined off-diagonal unordered capacity is `p_i p_j`;
* diagonal capacity is `p_i^2/2` asymptotically;
* the half-product pushforward gives the factor `2c` in convolution
  domination.

The repaired completeness proof for its *continuous relaxation* is valid.
After trimming each target-bin inflow to `c/m`, symmetrize each off-diagonal
flow atom, pass the fine-cell capacity inequalities to fixed coarse dyadic
rectangles, then use Portmanteau and the monotone-class theorem.  Equal mass
`c/m` in every target bin gives Wasserstein discrepancy at most `1/m` from
`c lambda`.  This proves convergence to the continuous relaxation, but
Theorem 2.2 above proves that adding every fixed congruence cylinder still does
not cross the discrete bridge.

## 6. Failed completeness routes

### Fixed residues / profinite compactness

**Dead as a strengthening:** Theorem 2.2 supplies an explicit product-Haar
lift of every continuous feasible point.  No hierarchy whose limiting data are
only macroscopic position plus all fixed congruences can improve
`C_conv`.

### Independent random discretization

**Dead at quadratic density without a design lemma:** at `N=Theta(k^2)`, a
typical target has only constant expected representation multiplicity.  An
independent rounding therefore leaves a positive density of holes.  Driving a
union bound over `Theta(k^2)` targets requires logarithmic multiplicity and
loses the quadratic constant.  This is a barrier to naive rounding, not a
proof that correlated deterministic rounding is impossible.

### Ordinary product or concatenation

**Dead in normalization:** Cartesian products multiply normalized efficiency
by a factor below one, while serial concatenation grows range only linearly in
the number of blocks.  Neither yields the approximate supermultiplicativity
needed for a Fekete argument.

## 7. Exact minimal missing bridge

There are now two sharply stated options.

1. Prove the cross-cover defect lemma (3.4), or a more flexible typed analogue
   with total micro-role cost `(1+o(1))k`.  Theorem 3.1 would then force
   `alpha_-=alpha_+` immediately.
2. Enrich the analytic hierarchy at a **growing mesoscopic scale** and prove a
   deterministic rounding/design theorem.  Fixed macro bins, all fixed
   residues, and their joint profinite compactification are insufficient by
   Theorem 2.2.

The first option is a finite combinatorial orientation problem; the second is
a two-scale compactness problem.  Neither bridge was proved in this attack, so
no resolution of Erdős 791 is claimed.

## Reproduction

```bash
python3 phase2/loop/erdos791/full_attack/analytic/bipartite_blowup.py
python3 phase2/loop/erdos791/full_attack/analytic/profinite_cylinder_check.py
```

The first command performs exact finite sumset checks.  The second checks over
ten million macro-bin/residue cylinders (`M<=400`, `m<=16`, `q<=19`); the
largest observed discrepancy from `M/(mq)` is below one, while the proof only
requires `o(M)` for fixed `m,q`.
