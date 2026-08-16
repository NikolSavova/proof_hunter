# Amortized pocket reset: the exact forward-or-chain gate

**Date:** 2026-08-14  
**Verdict:** an arbitrarily deep *nested* pocket costs less than one
doubling bit.  More generally, a batch of recursive pockets whose discarded
faces have inclusion width `w` and target-frame overlap `rho` costs at most
`log_2(2 w rho)` bits.  Independently, the full unrooted ear encoding has
sharp multiplicity two.  Thus polynomial width and overlap would prove the
desired `O(log ell)` cumulative loss.

This does not yet close the global statement.  The stretchable product-grid
family is an exact scalable obstruction to the Boolean-pocket part alone:
its discarded faces lose at least `r-3=Theta(ell)` bits.  Its two-ended
tangent pool is larger than that entire weighted loss by a factor at least
`2^r-2`.  Consequently the only surviving gate is genuinely a
**forward-or-chain aggregation theorem**: after all forward tangent pools
are charged, prove that the remaining nested records have polynomial
effective width times overlap.  Neither long nested prefixes nor product
grids contradict this statement; they realize its two opposite branches.

All logarithms are base two.  Every set called a face is in convex position,
so all of its subsets are faces.

## 1. What a cumulative failed bit is

Put

\[
 F_k=\sum_{j\le k}v_j,\qquad \ell=\lceil\log_2 n\rceil,
\]

and define the block-`b` prefix deficit

\[
 s_b(P)=\sup_{q\ge0}
 \left[q-\log {F_{\ell-b}\over F_{\ell-(q+1)b}}\right]_+ .   \tag{1}
\]

Thus `(PT)_(b,s)` in `BLOCK_DOUBLING_ATTACK.md` is exactly the assertion
`s_b(P)<=s`.  That report proves

\[
 \mu\ge\ell-(s_b(P)+3)b.                            \tag{2}
\]

For constant `b`, it is enough to show that at most `O(log ell)` cumulative
doubling bits fail.  A recursive pocket proof represents a rank drop of `h`
by a token of weight `2^h`.  The question is therefore whether the weighted
tokens can be represented by ordinary convex faces with only polynomial
congestion.

There is an even cleaner envelope, proved in
`ear_map/AMORTIZED_RESET.md`:

\[
 K_F=\max_{0\le k<\ell}{2^{\ell-k}F_k\over V},
 \qquad
 \mu\ge\ell-\lceil\log\max(1,K_F)\rceil-1.         \tag{2a}
\]

If `N_r^(24)` counts rank-`r` faces with
`u(A)<=24(r+1)` and
`K_u^(24)=max_(r<ell)2^(ell-r)N_r^(24)/V`, then the exact peak-slice
argument gives

\[
 K_u^{(24)}\le K_F
 \le\max\{2,(24/5)K_u^{(24)}\}.                    \tag{2b}
\]

Thus cumulative amortization and the low-addable Hall gate are equivalent
within an absolute factor.  The cumulative language does not evade the hard
rank slice; it locates it canonically and automatically credits all surplus
growth and all mass above `ell`.

## 2. A whole nested descent costs less than one bit

Let `D_1,...,D_t` be convex faces and define their Boolean demand and target
pool by

\[
 W(\mathcal D)=\sum_{D\in\mathcal D}2^{|D|},\qquad
 U(\mathcal D)=\bigcup_{D\in\mathcal D}2^D.         \tag{3}
\]

> **Theorem 1 (chain-width reset).**  If the inclusion poset `mathcal D`
> has width `w`, then
> \[
> \boxed{W(\mathcal D)<2w\,|U(\mathcal D)|\le2wV(P).}          \tag{4}
> \]

**Proof.**  By Dilworth, partition `mathcal D` into `w` inclusion chains.
In one chain, distinct set sizes strictly increase.  If its largest member
has size `m`, then

\[
 \sum_{D\text{ in the chain}}2^{|D|}
 \le2^m+2^{m-1}+\cdots+1<2^{m+1}.                 \tag{5}
\]

All `2^m` subsets of the largest member belong to `U(mathcal D)`.  Bound
each chain by twice the *whole* union and sum over the `w` chains.  Every
member of `U(mathcal D)` is a convex face, giving the last inequality. QED.

In particular, the successive discarded prefixes in the parabolic example
(84)--(85) of `agent_acp_proof/REPORT.md` form one chain.  For prefix sizes
`0,1,...,s`, their exact demand is

\[
 1+2+\cdots+2^s=2^{s+1}-1<2\,2^s,                 \tag{6}
\]

while the largest discarded prefix alone supplies its full `2^s`-face
cube.  The depth `s` is irrelevant: the amortized loss is less than one bit.
This formally proves that the long nested-prefix example is not an
amortized-reset obstruction.

There is also an exact entropy version.  Choose a pair `(D,J)` uniformly
from all pairs with `D in mathcal D` and `J subseteq D`.  Then

\[
 \log W(\mathcal D)=H(J)+H(D\mid J)
 \le\log V(P)+H(D\mid J).                          \tag{7}
\]

Thus the loss is precisely conditional *reuse* entropy.  For the full
prefix chain `D_t={1,...,t}`, `0<=t<=s`, this conditional entropy increases
to only

\[
 \sum_{h\ge1}{h\over2^{h+1}}\log h
 =1.2885312757\ldots,                              \tag{8}
\]

even though the geometric exposure depth tends to infinity.  The direct
cardinality bound (6), rather than the entropy estimate, is what gives the
sharper one-bit result.

## 3. The fixed-tangent version

Fix one two-tangent frame.  Let `X` be its hidden faces and `Y` its retained
faces.  The planar rectangle-completion theorem says

\[
 I\cup R\text{ is convex for every }(I,R)\in X\times Y.       \tag{9}
\]

The frame separates the hidden and retained sides, so the decomposition of
`J union R` into `J subseteq I` and `R` is recoverable.  Let
`G subseteq X times Y` be any collection of active pocket records, and let
`w_R` be the inclusion width of the hidden neighborhood `N_G(R)`.

> **Theorem 2 (local tangent reset).**  If `w=max_R w_R`, then
> \[
> \boxed{
>  \sum_{(I,R)\in G}2^{|I|}\le2wV(P).}             \tag{10}
> \]

**Proof.**  For fixed `R`, apply Theorem 1 to `N_G(R)`.  Every target
`J union R`, `J subseteq I`, is convex by (9).  Targets belonging to
different `R` or different `J` are distinct because the two sides of the
fixed frame recover both pieces.  Sum (4) over `R`; the disjoint target
pools together contain at most `V(P)` faces. QED.

In fact the tangent-frame overlap disappears completely after one fixes the
exterior root `p`.  Partition all `p`-blocked rank-`r` sources by tangent
pair and hidden size.  For a full rectangle completion `C=I union R`,

\[
 \operatorname{ext}(C+p)=R+p,
 \qquad C-\operatorname{ext}(C+p)=I.                       \tag{10a}
\]

Thus `C` and `p` recover `I,R`, the tangent pair, and the frame.  Hence

\[
 \boxed{\sum_f|X_f||Y_f|\le v_r.}                         \tag{10b}
\]

For Boolean subtargets `J union R`, the same recovery finds `J,R` and the
tangent pair; the only forgotten datum is which active superset `I`
contained `J`.  If the inclusion width of those supersets is at most `w`,
Theorem 2 therefore holds after summing **all** fixed-`p` frames, with no
endpoint or hidden-size pigeonhole loss.

Now forget `p`.  The sharp planar ear encoding maps a *full* exterior
incidence to its pair `(I,B)` with multiplicity at most two:

\[
 E_{r,i}\le2v_i v_{r-i+1}.                         \tag{11}
\]

This removes the old root multiplicity from the full-pair census.  It does
not by itself bound the root multiplicity of a smaller Boolean target
`J union R`, since that target no longer remembers the full `I`.  Let `rho`
denote the actual global recovery multiplicity of the chain target pools,
including this cross-root reuse.  Summing (10) gives

\[
 \boxed{
  W_{\rm pocket}\le2w\rho\,V(P),\qquad
  \log(W_{\rm pocket}/V)\le1+\log w+\log\rho.}    \tag{12}
\]

This is the promised conditional cumulative reset.  If the low-addable
families produced by all cumulative failures admit such a decomposition
with `w rho=ell^{O(1)}`, only `O(log ell)` bits can fail.  The first-failure
lemma in `BLOCK_DOUBLING_ATTACK.md` supplies at least `F_k/(4b)` sources in
one of the last `2b` ranks with up-degree at most `8(k+1)`; optimized hull
activity supplies their capped blockers.  Equations (10)--(12) pay all of
those blockers except the records for which `w rho` is superpolynomial.

The qualification in the last sentence is essential: (12) is an exact
accounting theorem, not yet a proof that the global effective `w rho` is
polynomial.

## 4. Product grids kill a Boolean-only reset

Use the stretchable product-block configuration from
`agent_entropy_spread/REPORT.md`.  Put `b=r-2`, let every one of the `b`
internal blocks have `M` choices, and write

\[
 S=M^b                                                    \tag{13}
\]

for the number of full transversals.  The hidden faces `I_a` all have size
`b`.  Counting their Boolean cubes with multiplicity gives demand

\[
 W_{\rm bool}=2^bM^b,                                    \tag{14}
\]

but their union is only the partial-transversal pool

\[
 B_{\rm bool}=(M+1)^b.                                   \tag{15}
\]

Take `M=2^r`.  Since `b=r-2<=(M+1)/2`, Bernoulli's inequality gives

\[
 {W_{\rm bool}\over B_{\rm bool}}
 =2^b\left(1-{1\over M+1}\right)^b
 \ge2^{b-1}.                                             \tag{16}
\]

Thus Boolean hidden-pocket targets alone lose at least

\[
 b-1=r-3=\Theta(\ell)                                   \tag{17}
\]

bits.  Any assertion that the Boolean or nested part *universally* loses
only `O(log ell)` bits is false on a rational planar order type.  In poset
language, the `M^b` equal-sized hidden transversals form an antichain of
width `M^b`; Theorem 1 correctly refuses to help.

The same configuration displays the missing payment.  Its two-ended
microblock pool has size

\[
 T_2={M\choose2}^2M^{b-2}
 ={(M-1)^2\over4}S.                                      \tag{18}
\]

For `M=2^r` and `b=r-2`, comparison with (14) is exact:

\[
 {T_2\over W_{\rm bool}}
 ={(M-1)^2\over4\,2^b}
 ={(M-1)^2\over M}
 \ge M-2.                                                \tag{19}
\]

So the forward two-ended pool more than pays all `Theta(ell)` missing
Boolean bits.  This is not a counterexample to cumulative reset; it is a
counterexample to deleting the forward alternative from the statement.

At the ambient scale

\[
 n=(r-1)2^r+2,\qquad
 \ell-r=\Theta(\log r)=\Theta(\log\ell),           \tag{20}
\]

the source rank itself is short of `ell` by exactly the allowable order.
Thus the product construction is consistent with, and shows the natural
sharpness of, an `O(log ell)` final mean loss.

The full configuration is substantially better than its Boolean subpool.
The exact vertical-composition recurrence in
`block_search/PREFIX_PRODUCT_STRESS.md` computes every coefficient needed
by `(PT)` for `M=2^r` through `r=64` (`n=1162144876643701751810`,
`ell=70`).  Every tested block has slack zero.  The same is true for all
parabolic nested-prefix examples through depth 256.  These exact results are
consistent with the accounting above: nested faces pay the chain branch,
and the extra microblock faces pay the product branch.

## 5. Exact remaining lemma

The strongest statement that survives both adversarial families is:

> **Forward-or-chain aggregation (open).**  Apply the first-failure
> low-addable reduction and the capped blocker selection.  Decompose the
> exterior records into tangent frames.  Charge every family of
> width-superpolynomial hidden antichains to completed two-ended tangent
> pools; after those charges, the remaining nested records have
> `w rho=ell^{O(1)}` in (12).

Together with (12), this gives `s_b(P)=O(log ell)` for constant `b`, hence
`mu>=ell-O(log ell)` by (2).  It is also the exact planar content missing
from the ordered-array inequality `(OAI)` in `agent_acp_proof/REPORT.md`.

The two standard stress tests now have clean, opposite answers.

* **Long nested prefix:** `w=1`; arbitrary depth costs less than one bit.
* **Product grid:** `w=M^b`; Boolean capacity loses `Theta(ell)` bits, but
  the explicit two-ended pool exceeds the entire weighted demand by
  `M-2`.

What remains unproved is global overlap: the same forward face can arise
under several outer frames, and the same hidden antichain can be split
among them.  The fixed-frame rectangle theorem and the constant-two ear
encoding eliminate all local congestion; only this cross-frame alignment
remains.

## 6. Audit of the batch-word Turan closure

There is a tempting way to finish the last paragraph.  Take a batch of
`s=ceil(sqrt(ell))` levels, encode each surviving source by two ordered
words, put an edge between sources when one word has a cap--cup crossing,
and use the single-crossing theorem.  If the joint encoding is injective,
the proposed independence bound is

\[
 \alpha\le A:=(n+1)^2.                                  \tag{21}
\]

Suppose additionally that every forward edge gives a convex target and
every target decodes at most `K=n^{O(s)}` source pairs.  Turan's bound gives

\[
 |E|\ge {S\over2}\left({S\over A}-1\right).              \tag{22}
\]

Consequently either `S<=(2dK+1)A`, or the number of distinct targets is
larger than `dS`.  In the small case,

\[
 \log S=O(\log d+\log n+s\log n)=O(\ell^{3/2}),          \tag{23}
\]

so the global source-cloud theorem discharges it with `n^{o(1)}` loss.  In
the large case the forward targets pay the selected cap directly.  Combined
with the cumulative-envelope/low-addable equivalence proved in
`ear_map/AMORTIZED_RESET.md`, these assumptions would indeed give

\[
 \mu\ge\ell-o(\ell).                                     \tag{24}
\]

The algebra is sound, but the two italicized assumptions are not presently
theorems.  There are three concrete gaps.

1. Two length-`s` projected words need not determine the source; its
   rank-`r-O(s)` retained core may still vary.  The independence bound in
   (21) must be multiplied by the largest joint-encoding fibre unless that
   core is fixed or carried.
2. A crossing in one projected word is not automatically a valid
   two-ended target.  The ordered-array construction requires the two
   endpoint pairs to be forward in one compatible rooted state.  If the
   other junction or the retained state varies, its union need not be
   convex.
3. Even when a target exists, it can forget the outside word.  A product
   grid gives `M_0^{Theta(r)}` source-pair preimages for one forward interval,
   exceeding `n^{O(s)}` when only `s=sqrt(ell)` coordinates are recorded.
   Fixing the complete outside signature restores the decoder, but can
   create up to `V(P)` signature classes; the small-class source-cloud
   estimate cannot be summed once per class.

Thus (21)--(24) are a useful **conditional closure**, not a proof.  Making
the `n^{O(s)}` decoder global is precisely the all-interval Kraft/KIC
problem: forgotten outside entropy must be charged once to its actual
prefix/suffix faces, rather than paid separately in every signature class.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_cyclic_stem_hw/verify_amortized_pocket.py
```

The checker uses integer arithmetic for the chain demand, all product-grid
comparisons (14)--(19), and finite tangent-neighborhood instances.  It also
audits the exact conditional-reuse distribution of nested prefix chains and
writes `amortized_pocket_certificate.json`.  The scalable inequalities are
proved above rather than inferred from the finite audit.
