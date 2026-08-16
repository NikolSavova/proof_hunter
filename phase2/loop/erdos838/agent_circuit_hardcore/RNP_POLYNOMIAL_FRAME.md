# RNP: the polynomial-frame branch is rigorously harmless

**Date:** 2026-08-14  
**Verdict:** this is a rigorous branch theorem, not a proof of RNP in full.
It shows that the common-apex/common-onion and swap-frozen counterfamilies
cannot scale toward an RNP counterexample, even when the blocked cloud has
an arbitrary planar order type.  More generally, any source family covered
by `2^{o(r^2)}` ground-set frames of polynomial size satisfies the desired
rankwise inequality with room tending to infinity.  A genuine obstruction
must therefore have quadratic source entropy across its frames; it cannot be
a large fibre over one QuickHull/pocket instance.

The result supplies an actual global Hall allocation in this branch: for
large `r`, the number of demanded source units is smaller than the number of
ordinary convex target faces, so an injective assignment exists.  It is
noncanonical and does not solve the entropy-rich branch.

## 1. RNP notation

Let

\[
 \ell=\lceil\log_2n\rceil,\qquad r=\ell-g,
\]

and let `S subset F_r(P)` be any rank-`r` source family.  RNP asks, for the
near-maximal family in particular, for

\[
 2^g|S|\le (\log n)^{O(1)}V(P).                    \tag{1}
\]

No near-maximal or planar-repair hypothesis is needed for the theorem below;
only the concentration of source labels into small ambient frames is used.

## 2. An explicit all-sizes face lower bound

We first record a self-contained coarse consequence of the classical
Erdős--Szekeres theorem.

> **Lemma 1 (explicit quadratic lower bound).**  Let `Q` be a planar
> general-position set of size `m`, and put
> `L=floor(log_2 m)`.  If `L>=64`, then
> \[
> \boxed{V(Q)\ge 2^{L^2/10}.}                       \tag{2}
> \]

**Proof.**  Put `k=floor(L/4)`.  The classical cup--cap bound says that
every set of

\[
 \binom{2k-4}{k-2}+1\le4^k
\]

points contains a convex `k`-set.  Double-count pairs `(W,C)` in which
`W subset Q`, `|W|=4^k`, and `C subset W` is a convex `k`-set.  This gives

\[
 v_k(Q)\ge{\binom mk\over\binom{4^k}k}.             \tag{3}
\]

The elementary binomial estimates

\[
 \binom mk\ge(m/k)^k,
 \qquad
 \binom{4^k}k\le(e4^k/k)^k
\]

therefore yield

\[
 \log_2V(Q)
 \ge k\{\log_2m-2k-\log_2e\}.                     \tag{4}
\]

Since `k>=L/4-1` and `L-2k>=L/2`, the right side is at least `L^2/10`
for `L>=64`.  QED.

The exact binomial ratio in (3) is appreciably stronger than (2); the
verifier checks both.

## 3. Polynomial-frame theorem

Call `R subset P` a **source frame** when every source assigned to it is a
subset of `R`.  Frames may overlap and impose no geometric condition.

> **Theorem 2 (polynomial-frame RNP).**  Fix a constant `C`.  Suppose a
> rank-`r=ell-g` source family `S` is covered by `T_r` frames, each of size
> at most `r^C`.  If
> \[
> \log_2T_r=o(r^2),                                  \tag{5}
> \]
> then, uniformly over every `g>=1`,
> \[
> \boxed{{2^g|S|\over V(P)}\longrightarrow0}
> \qquad(r\longrightarrow\infty).                  \tag{6}
> \]
> In particular, (1) holds with constant `1` for all sufficiently large
> `r` in this branch.

**Proof.**  The frame cover gives

\[
 |S|\le T_r\binom{r^C}{r}
 \le T_r\left({er^C\over r}\right)^r.              \tag{7}
\]

Choose any one of the frames and delete it from `P`, leaving `Q`.  Since
`n>2^{ell-1}=2^{r+g-1}` while `r^C=o(2^r)`, for all sufficiently large `r`

\[
 |Q|\ge n/2>2^{r+g-2}.
\]

Thus `floor(log_2|Q|)>=r+g-2`, and Lemma 1 plus heredity gives

\[
 \log_2V(P)\ge\log_2V(Q)
 \ge{(r+g-2)^2\over10}.                            \tag{8}
\]

Combining (7)--(8),

\[
 \log_2{2^g|S|\over V(P)}
 \le g+\log_2T_r
   +r\{\log_2e+(C-1)\log_2r\}
   -{(r+g-2)^2\over10}.                            \tag{9}
\]

For `r>=8`, the right side as a function of `g>=1` is maximized at `g=1`.
Under (5), its quadratic negative term dominates both `o(r^2)` and
`O_C(r log r)`, proving (6).  QED.

The same calculation gives a useful non-polynomial version.

> **Corollary 3 (general frame-entropy criterion).**  Suppose `S` is
> covered by `T_r` frames of size at most `s_r`, where
> \[
>  \log_2T_r+r\log_2\left({e s_r\over r}\right)=o(r^2). \tag{9a}
> \]
> Then `2^g|S|/V(P)->0`, uniformly in `g>=1`.

**Proof.**  The left side of (9a) is an upper bound for `log_2|S|`.
Moreover, (9a) implies `log_2(s_r/r)=o(r)`, so
`s_r=r2^{o(r)}=o(2^r)<=o(n)`.  Deleting one frame still leaves at least
`n/2` points, and (8) applies unchanged.  Its negative quadratic term
dominates (9a).  QED.

Thus frames may have subexponential, rather than merely polynomial, size.
This is useful for unbalanced QuickHull histories: a fixed history frame can
grow much faster than a power of `r` and remain harmless, provided the
number of such frames has subquadratic entropy.

The proof is deliberately insensitive to the order type on `P-R`.  That
set need not be a literal interior pocket, and its faces need not be
compatible with a source.  RNP is a global counting statement; its own
convex faces already provide the necessary target capacity.

## 4. Exact consequence for the known obstructions

In the common-apex/common-onion and swap-frozen families, every source lies
on the same strictly concave chain of `5r` points.  The apex cloud can have
arbitrary size and arbitrary internal order type.  Taking `C=2`, `T_r=1`
in Theorem 2 proves

\[
 {2^gN_r\over V(P)}\to0                           \tag{10}
\]

uniformly in the size of that cloud.

Using the actual frame size gives the sharper explicit estimate

\[
 N_r\le\binom{5r}{r}\le(5e)^r.                    \tag{11}
\]

For example, using the exact lower bound (3), the certified upper bounds on
the base-two logarithm of the RNP ratio at `g=1` are

```text
r=64:  -300.15
r=80:  -534.56
r=128: -1621.63
r=192: -3966.91
r=256: -7336.10.
```

Increasing `g` only improves these margins.  Thus the arbitrarily large
blocked cloud which freezes all swaps is the opposite of a scalable RNP
obstruction: once it is large enough to create ambient demand, it creates
far more unrooted target faces than that demand.

This does not rescue a source-local swap proof.  It instead supplies the
correct global branch rule:

* if many sources share one polynomial-size exterior frame / QuickHull
  instance, discharge the entire class using the unrooted face mass outside
  the frame;
* only recurse geometrically when the source family is spread over
  quadratically many distinct frames.

## 5. A necessary entropy condition for any counterexample

The same calculation can be read contrapositively.  Suppose at ranks tending
to infinity that

\[
 2^gN_r>r^D V(P)                                    \tag{12}
\]

for some fixed `D`.  Then the near-maximal sources cannot be covered by
`2^{o(r^2)}` frames of size `r^C`, for any fixed `C`.  Their polynomial-frame
covering number is

\[
 2^{\Omega(r^2)}.                                   \tag{13}
\]

So the remaining Hall gate is no longer compatible with the standard
one-frame counterexamples.  A bad family must simultaneously have:

1. the bounded rank width and constant-density rank slice from the ACP hard
   branch;
2. average `Omega(r^2)` blocked exterior labels;
3. the local three-pocket/ear-replacement structure; and
4. `Omega(r^2)` bits of variation in the actual source frames.

Items 2--4 together suggest the surviving recursion should charge frame
entropy, rather than endpoint names or source-local shadows.  What remains
unproved is a theorem converting that frame entropy into distinct faces
when the exterior pockets cross and their QuickHull instances vary.

## 6. Verification

Run

```bash
python3 -m py_compile \
  phase2/loop/erdos838/agent_circuit_hardcore/verify_rnp_polynomial_frame.py

python3 \
  phase2/loop/erdos838/agent_circuit_hardcore/verify_rnp_polynomial_frame.py
```

The script writes `rnp_polynomial_frame_certificate.json`.  It checks the
exact double-count lower bound (3), verifies the `L^2/10` corollary through
`L=256`, and certifies the displayed common-apex margins.
