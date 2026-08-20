# Real-cubic pro-2 towers: optimistic dominance audit

## 1. Verdict

Let

\[
 E=\mathbb Q(\zeta_7)^+
\]

and ramify at the three primes of `E` over each of `s` rational primes that
split completely in `E`.  The honest Kummer and Shafarevich inputs do not
produce an improvement over the rational rank-713 tower.  More strongly, an
arithmetic relaxation which dominates the honest construction is still
weaker:

* grant generator rank `d=3s`, before any dyadic loss;
* grant a balanced base presentation with `r_0=d`;
* allow **every** rational prime split in `E` as a useful prime, without the
  safe condition `q=1 mod 4` or a Frattini-parity test;
* spend the full GS budget one prime ideal at a time, so partial Galois orbits
  are allowed; and
* globally sort all local prime-power depths.

The best sampled member is near `s=243`, and its continuous dyadic threshold
is

\[
 \alpha_{\rm cubic,opt}=0.49459142\ldots .          \tag{1.1}
\]

This is worse than the current rational certificate `0.49458525`.  The
verifier uses the slightly easier historical target `0.49458539`; even
there the optimized two-endpoint margin for `s=243` is about `-10.55`.
Failure at that larger exponent implies failure at the current smaller one.
Thus neither the exact dyadic Kummer loss nor the `+2` Shafarevich relation
allowance is responsible for the failure.

This is a verified numerical barrier, not a theorem optimizing over every
integer `s`.  The verifier checks a broad rank profile and the full local
frontier at the competitive point.  It is enough to reject the proposed
parameters and explains why the apparent threefold prime supply does not
translate into a gain.

## 2. Exact arithmetic of the cubic base

Put `theta=2 cos(2 pi/7)`.  Its minimal polynomial is

\[
 f(X)=X^3+X^2-2X-1,\qquad \operatorname{disc}(f)=49. \tag{2.1}
\]

Minkowski's bound is

\[
 \frac{3!}{3^3}\sqrt{49}=\frac{14}{9}<2,
\]

so `E` has class number one.  The roots lie respectively in
`(-2,-1),(-1,0),(1,2)`.  The three units `-1,theta,theta+1` have independent
signature vectors, so the unit signature map has full rank three.  Hence the
narrow class group is also trivial.

The polynomial `f` is irreducible modulo two, so `2` is inert and the unique
dyadic completion has degree three over `Q_2`.  A rational prime `p!=7`
splits completely in `E` exactly when

\[
 p\equiv\pm1\pmod7.                                \tag{2.2}
\]

## 3. Kummer dimensions

Let `S` contain all `3s` primes above the chosen split rational ramification
primes.  Class number one gives

\[
 \dim_{\mathbb F_2}
 \{a:v_{\mathfrak p}(a)\equiv0\ (\mathfrak p\notin S)\}/E^{\times2}
 =3s+3.                                             \tag{3.1}
\]

Full unit-signature rank shows that the totally positive subspace has exact
dimension `3s`.  Since all radicands have even dyadic valuation, their local
classes lie in the four-dimensional unit squareclass space at the inert
dyadic place.  The unramified local line has dimension one.  Therefore
requiring dyadic unramifiedness costs at most three conditions and gives

\[
 3s-3\le d(G_S)\le3s.                              \tag{3.2}
\]

Requiring the dyadic prime to split, rather than merely remain unramified,
costs at most four conditions and gives the weaker lower bound `3s-4`.

The standard tame totally-real Shafarevich estimate used in the conservative
construction is

\[
 r(G_S)\le d(G_S)+2,                               \tag{3.3}
\]

the `2` being the unit rank of `E`.  The numerical relaxation uses the more
favorable values `d=3s` and `r_0=d`, so it dominates (3.2)--(3.3).

## 4. Frobenius cost and local normalization

If a useful rational prime `q` splits in `E`, write

\[
 q\mathcal O_E=\mathfrak q_1\mathfrak q_2\mathfrak q_3.
\]

To force residue degree at most two at all three base primes, one must impose
the three relations

\[
 \operatorname{Frob}_{\mathfrak q_j}^{2}=1
 \quad(j=1,2,3).                                   \tag{4.1}

\]

Conjugacy over `E` does not identify these three Frobenius elements; the
conjugating automorphisms lie in `Gal(E/Q)`, outside the pro-2 group over `E`.
A `Gal(E/Q)`-stable quotient must therefore impose the whole orbit.

The verifier grants the still stronger option of imposing (4.1) separately.
One capped base prime contributes one third of the rational local item:

\[
 c_q=\frac13\log q,
 \qquad
 g_{q,k}=\frac16\log\left(
  \frac{k+1}{k}\frac{1-q^{-2k}}{1-q^{-2(k+1)}}
 \right).                                         \tag{4.2}

Three copies recover exactly the residue-degree-two item in the rational
tower.  If `d=3s`, the strict GS budget contains at most

\[
 R_s=\left\lfloor\frac{d^2-1}{4}\right\rfloor-d  \tag{4.3}

individual Frobenius-square relators.  The useful list is therefore the
first `R_s` prime-ideal copies ordered by (4.2).

The key cancellation is now visible.  Three prime ideals give three times
the generator supply, but a useful rational prime costs three relations and
its three normalized local contributions sum to only one rational item.
The sparser split-prime sequence then loses the small constant comparison.

## 5. Root discriminant and layer degrees

Since `disc(E)=49`, the tame root-discriminant bound is

\[
 D_s=49^{1/3}\prod_{i\le s}p_i,                   \tag{5.1}

where the `p_i` are the chosen split rational ramification primes.  Indeed,
the product of the norms of the three primes above `p_i`, followed by the
`1/[E:Q]` normalization, contributes exactly `p_i`.

Finite pro-2 layers over `E` have absolute degrees

\[
 [K:\mathbb Q]=3\cdot2^j.                         \tag{5.2}

The extra factor three is fixed, so successive layers still double and the
same interval `[w_0,2w_0]` argument applies without a phase change.

At the competitive optimistic point `s=243`, the exact finite parameters are

\[
 d=729,\quad R_s=132131,
\]

with last ramified split prime `5573`.  There are 44,043 complete useful
rational-prime orbits and two additional prime-ideal copies; the last useful
rational prime is `1767919`.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_real_cubic_pro2_optimistic_dominance.py
```

The verifier checks (2.1), the unit norms and signatures, inertness of two,
the split-prime lists, the exact GS count, the root-discriminant expression,
the globally sorted local frontier, the failure at `0.49458539`, and a coarse
rank profile on both sides of the optimum.
