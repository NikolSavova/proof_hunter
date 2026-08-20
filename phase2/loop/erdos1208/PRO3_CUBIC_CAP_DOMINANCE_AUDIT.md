# Pro-3 cubic Frobenius caps: a sound but noncompetitive branch

## 1. Verdict

The proposed pro-3 construction is arithmetically legitimate and really
does have a cubic Golod--Shafarevich budget.  Two unavoidable normalization
losses prevent it from improving the rank-221 pro-2 theorem:

1. a Frobenius cube guarantees residue degree at most three, so the uniform
   local gain is the residue-degree-three gain; and
2. normal layers have degrees `3^j`, so the phase interval is `[w,3w]`, not
   `[w,2w]`.

After both losses, the best scanned safe member is

\[
 d=38,\qquad N=7138,\qquad
 \alpha=0.4952651587\ldots,                              \tag{1.1}
\]

far weaker than the proved pro-2 exponent `0.49371397`.  The exact rounded
certificate `alpha=0.49526518` is checked by
`verify_pro3_cubic_cap_dominance.py`.

Even an impossible relaxation which deletes every base relation from the
Golod--Shafarevich polynomial bottoms near `0.49521810`.  Thus placing the
base relations deeper cannot rescue the branch.  Complete splitting would
change the picture, but imposing it costs degree-two Frobenius relations and
destroys the cubic `Theta(d^3)` cap count.

## 2. Exact tame pro-3 presentation

Let `S` consist of `d` rational primes `p == 1 (mod 3)`, and let `G_S` be
the maximal pro-3 extension of `Q` unramified away from `S`.  Every finite
Galois 3-extension of `Q` is totally real: complex conjugation would give an
element of order two in a group of odd order.

Class field theory gives generator rank `d`.  The tame Koch--Shafarevich
presentation has at most `d` base relations.  Its abelianization is finite,
so abelianizing any minimal pro-3 presentation gives the reverse inequality
`r_0>=d`.  Hence the concrete tame presentation is balanced:

\[
 d(G_S)=r_0(G_S)=d.                                    \tag{2.1}
\]

For each `p in S`, choose a tame inertia generator `tau_p`.  Tame pro-3
inertia is procyclic, and the local relation is

\[
 \sigma_p\tau_p\sigma_p^{-1}=\tau_p^p.                 \tag{2.2}
\]

Because `p == 1 (mod 3)`, imposing `tau_p^3=1` is compatible with (2.2) and
forces `e_p<=3`.  Its normal closure handles every conjugate prime above
`p`.  The relator is in Zassenhaus degree at least three, and tame
discriminant theory gives the root-discriminant factor

\[
 p^{1-1/e_p}\le p^{2/3}.                                \tag{2.3}
\]

Now take unramified rational primes `q == 1 (mod 4)` and impose
`g_q^3=1` on chosen Frobenius elements.  These relators also have degree at
least three and preserve the Frattini rank.  In every retained finite layer,
the residue degree divides three.  The congruence `q == 1 (mod 4)` ensures
that `-1` is already a square in every residue field, as required by the
prime-power norm factorization.

With `N` useful primes, a safe weighted Golod--Shafarevich polynomial is

\[
 P(t)=1-dt+dt^2+(d+N)t^3.                              \tag{2.4}
\]

The maximum cubic coefficient is indeed asymptotic to `4d^3/27`.  More
exactly, maximize

\[
 {dt-1-dt^2\over t^3}                                  \tag{2.5}
\]

over `0<t<1`.  Its relevant stationary point is

\[
 t_d=1-\sqrt{1-3/d}.                                    \tag{2.6}
\]

At `d=38`, `N=7138` is valid; the rational test point `t=403/10000` gives

\[
 1-38t+38t^2+7176t^3<0.                               \tag{2.7}
\]

## 3. Correct local normalization

Suppose a selected rational prime has residue degree `f in {1,3}` in a
layer of degree `m`.  There are `m/f` prime ideals over it, each of norm
`q^f`.  If

\[
 A_k(t)={k+1\over k}{1-t^k\over1-t^{k+1}},              \tag{3.1}
\]

then the normalized full-orbit gain of depth increment `k` is

\[
 {1\over f}\log A_k(q^{-f}).                            \tag{3.2}
\]

The degree-three value is a uniform lower bound.  For completeness, put
`t=e^{-x}` and `phi_k(x)=log A_k(e^{-x})`.  The hyperbolic-sine formula for
`A_k` gives

\[
 \phi_k''(x)=
 -{k^2\over4}\operatorname{csch}^2(kx/2)
 +{(k+1)^2\over4}\operatorname{csch}^2((k+1)x/2)<0.    \tag{3.3}
\]

Also `phi_k(0)=0`.  Concavity therefore makes `phi_k(x)/x` decreasing, so

\[
 \log A_k(q^{-1})\ge {1\over3}\log A_k(q^{-3}).         \tag{3.4}
\]

The verifier consequently uses the guaranteed increment

\[
 \Delta_{q,3}(k)={1\over3}\log A_k(q^{-3}).              \tag{3.5}
\]

This is one third, rather than one half, of the asymptotic local entropy per
rational prime.  A cube relator cannot distinguish residue degree one from
three.

## 4. Ternary phase certificate

An infinite finitely generated pro-3 group supplies normal layers of degrees
`3^j`.  For arbitrary `n`, the normalized height parameter must therefore
be certified throughout `[w_0,3w_0]`.  With the disk constant
`C_*=424/333`, the two endpoint conditions are

\[
 F(2\alpha w_0)\ge R_\alpha(w_0),\qquad
 F(6\alpha w_0)\ge R_\alpha(3w_0),                      \tag{4.1}
\]

where

\[
 R_\alpha(w)=\log(C_*D)+(2-4\alpha)w+
 \log\!\left(1+{e^{2(2\alpha-1)w}\over C_*D}\right).  \tag{4.2}
\]

For the first 38 primes `p == 1 (mod 3)`, the last ramified prime is 409 and

\[
 \log D={2\over3}\sum_{p\in S}\log p
 =124.7331189295759\ldots.                              \tag{4.3}
\]

The first 7,138 primes `q == 1 (mod 4)` outside `S` end at 155,797.  Taking

\[
 \alpha=0.49526518,\qquad w_0=29734                         \tag{4.4}
\]

gives strict endpoint margins.  The verifier checks the rational GS
inequality, all prime lists, the product-disk RHS, the globally sorted
depth-1-through-20 frontier, prefix feasibility, and depth-21 exclusion.
Since the marginal gains decrease with depth, the last test excludes every
omitted deeper increment.

## 5. Optimistic dominance tests

The safe scan over every integer rank near the minimum gave

\[
\begin{array}{c|c}
d&\alpha\\ \hline
30&0.49531499\\
34&0.49527681\\
36&0.49526793\\
38&0.49526516\\
40&0.49526656\\
45&0.49528252\\
50&0.49533738
\end{array}                                                \tag{5.1}
\]

Three deliberately favorable relaxations isolate the obstruction:

* deleting every quadratic base relation, while retaining the honest
  residue-degree-three gain and ternary phase, gives best sampled exponent
  `0.49521810` near rank 34;
* replacing ternary phases by binary phases but retaining residue degree
  three gives about `0.49513494`;
* granting complete splitting, hence residue degree one, would give roughly
  `0.4827` even with ternary phases.

The last line explains both the attraction and the failure of the proposal.
To force residue degree one one must impose `g_q=1`.  Such a Frobenius must
first lie in the Frattini subgroup, and killing it is a degree-two relation.
Only `O(d^2)` such relations fit, so the apparent `Theta(d^3)` advantage
vanishes.  The cubic relator `g_q^3` retains the large count precisely because
it permits the degree-three residue branch that causes the local entropy
loss.

## 6. Scope

This audit kills the natural pro-3 analogue of the current tower and every
variant that only moves its base relations deeper.  It is not a universal
no-go for pro-3 arithmetic: a new mechanism giving degree-one residue fields
at cubic Zassenhaus cost would evade it.  No such mechanism is presently
known, and ordinary Frobenius exponent caps do not provide one.
