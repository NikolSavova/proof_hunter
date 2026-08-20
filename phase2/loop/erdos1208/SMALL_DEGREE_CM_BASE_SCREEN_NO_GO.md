# Small degree CM-base screen: two optimistic cubics, both killed exactly

## 1. Verdict

An exact-prime-ideal screen was run on the first 200 totally real cubic
fields and the first 200 totally real quartic fields in increasing absolute
discriminant in the LMFDB.  The endpoints of the lists are respectively

\[
 |\operatorname {Disc}E|\le 5624\quad(s=3),\qquad
 |\operatorname {Disc}E|\le 29237\quad(s=4).       \tag{1.1}
\]

The screen was launched against the then-live `Q(sqrt(1949))` exponent
`0.49371148`.  During the audit that record was superseded by the
`Q(sqrt(43133))` exponent

\[
                         \boxed{0.49369772}.       \tag{1.2}
\]

All comparisons below distinguish these thresholds.  The screen
deliberately overpaid every field:

* if `h` is the 2-rank of the narrow class group and `t` prime ideals are
  ramified, it granted generator rank `d=t+h`;
* it charged only `d` base relations, instead of the safe Shafarevich
  allowance `d+s-1`;
* it declared every odd unramified prime ideal useful; and
* it used the complete depth frontier and the Eisenstein-CM disk constant.

On the competitive grid `190 <= t <= 250`, `t=0 mod 5`, only two fields
beat the **old** exponent `0.49371148` even in this optimistic model:

\[
 \begin{array}{c|c|c|c}
 \operatorname {Disc}E&f_E(x)&\mathrm {Cl}^+(E)&
     \hbox{optimistic margin}\\ \hline
 4729&x^3-19x-29&C_2&+0.9894\ldots\\
 5521&x^3-13x-11&C_2&+0.8041\ldots
 \end{array}                                      \tag{1.3}
\]

The best quartic had discriminant `27792` and optimistic margin
`-1.1722...` at the old threshold.  The especially close earlier cubic of
discriminant `1489` has fine-grid optimistic maximum `-0.0044...`; it does
not cross even that old endpoint after receiving the narrow-class bonus
and zero relation excess.  The endpoint obstruction strengthens when
`alpha` is decreased in this range, so every old-threshold failure also
fails the current threshold (1.2).

Both apparent winners in (1.3) fail the exact Kummer audit.  They have
class number one and 2 inert, and their combined three sign conditions and
three dyadic squareclass conditions have rank six.  There are only `t+3`
S-unit columns.  Hence the actually constructed totally positive,
dyadically unramified Kummer rank is

\[
                 \boxed{d=t-3},                   \tag{1.4}
\]

not the optimistic `t+1`.  Restoring (1.4) and the safe cubic relation
excess `+2`, while still declaring every remaining prime ideal useful,
gives best endpoint margins at the current exponent (1.2)

\[
 \begin{array}{c|c|c}
 \operatorname {Disc}E&t&\hbox{all-useful safe margin}\\ \hline
 4729&222&-6.1050\ldots\\
 5521&210&-6.1540\ldots
 \end{array}                                      \tag{1.5}
\]

For reference, at the superseded exponent the corresponding maxima were
`-4.0324...` and `-4.2325...`, at `t=234` and `t=224`.

Thus no useful-prime Frobenius audit is needed: both candidates are dead
before usefulness is imposed.  The screened small cubic/quartic family
does not improve the actual live `Q(sqrt(43133))` CM exponent.

## 2. The optimistic envelope

Let `E` be totally real of degree `s`.  Order its odd prime ideals by norm,
with multiplicity.  For a ramification prefix `T` of length `t`, order-two
inertia gives

\[
 \log D_T={\log|\operatorname {Disc}E|\over s}
       +{1\over2s}\sum_{\mathfrak p\in T}\log N\mathfrak p. \tag{2.1}
\]

Put `h=dim_F2 Cl^+(E)[2]`.  Restriction to inertia gives the general upper
bound

\[
 d\le t+h,                                        \tag{2.2}
\]

because a quadratic character in the kernel is unramified at every finite
prime and is controlled by the narrow ray/class contribution.  The screen
uses equality in (2.2).  It also grants the favorable base relation count
`r_0=d`, so the Frobenius-square budget is

\[
 N=\left\lfloor{d^2-1\over4}\right\rfloor-d-t.   \tag{2.3}
\]

Every one of the next `N` odd ideals is declared useful.  For an ideal of
norm `Q`, the depth-`k` item is

\[
 c_{Q,k}={\log Q\over s},\qquad
 g_{Q,k}={1\over2s}\log\left(
 {k+1\over k}{1-Q^{-2k}\over1-Q^{-2k-2}}
 \right).                                        \tag{2.4}
\]

The fractional-knapsack frontier from these items is inserted into the two
exact dyadic endpoint inequalities with `C=2sqrt(3)/pi`.  The slow screen
reproduces the old-threshold candidate discovery; the fast finalist audit
checks both the old threshold and current `0.49369772`.  Depth slopes are
strictly decreasing for each ideal; the verifier retains six depths and
checks that the active slopes dominate the first omitted depth.

The prefix assignment is not a heuristic restriction.  The all-depth
exchange proof in `ARBITRARY_PRIME_ASSIGNMENT_DOMINANCE.md` depends only on
the ordered norm variable, so it applies unchanged to a multiset of prime
ideal norms (prime powers included).  Its two derivative hypotheses have
large slack in the competitive cells.  Therefore the ramification prefix
and the following useful prefix maximize the relaxed endpoint margins for
fixed `(E,t,N)`.

## 3. Exact Kummer kill for the two finalists

For each polynomial in (1.3), PARI certifies:

* field discriminant `4729` or `5521` and three real embeddings;
* ordinary class number one and narrow class group `C_2`;
* 2 is inert;
* the displayed fundamental units have signature rank two; and
* every prime ideal in the prefix is principal.

Work in the integral basis returned by `nfinit`.  Since 2 is inert,
`O_E/2` is `F_8`, so the 56 units of `O_E/4` have seven squares and

\[
 |(O_E/4)^\times/((O_E/4)^\times)^2|=8.           \tag{3.1}
\]

Thus there are three dyadic bits.  The verifier enumerates the 64 residue
classes, reconstructs multiplication from the exact integral-basis table,
and forms the six-row matrix consisting of the three real signs and the
three bits in (3.1).  Its rank is six for every prefix `180<=t<=280`.
With three unit columns and `t` principal-prime columns this proves (1.4).

For the standard safe tame totally-real presentation over a cubic base,

\[
 r_0\le d+2.                                      \tag{3.2}
\]

Adding `t` inertia squares and the remaining Frobenius squares gives the
budget used in (1.5).  Since even the all-useful relaxation is strongly
negative, exceptional Frobenius functionals cannot rescue either field.

## 4. Scope and verification

This is a rigorous kill of the only candidates exposed by the stated
finite field/rank screen; it is not a theorem over all cubic or quartic
fields or all ranks.  In particular, fields after the first 200, a
different arithmetic presentation, or genuinely non-prefix ramification
outside the verified exchange hypotheses remain separate questions.

Run

```text
python3 phase2/loop/erdos1208/verify_small_degree_cm_base_screen.py
```

for the exact finalist/Kummer/no-go audit.  Passing `--full-screen`
downloads the two discriminant-ordered 200-field lists from the LMFDB API,
recomputes all prime-ideal norm streams with PARI, and reproduces the
optimistic coarse screen at its original `0.49371148` threshold.  The
default check is network-independent and additionally checks the current
`0.49369772` endpoint.
