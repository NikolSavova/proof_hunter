# A large-star barrier at the actual-codegree normalization boundary

## 1. Verdict

The proposed `Nk^4` bound for the **pre-normalized** third-translation
mass is false.  There are polynomial-height integral distance-Sidon sets
for which one source pair has

\[
 c(p)=\Theta(k^2),\qquad O(p)=\Theta(k^3),\qquad
 T(C)=\Theta(k^2),\qquad W_{r(p),N}=\Theta(k^2).       \tag{1.1}
\]

Consequently

\[
 \boxed{
 \sum_{C\text{ at }p}T(C)W_{r(p),N}=\Theta(k^7),}    \tag{1.2}
\]

whereas `Nk^4=Theta(k^6)`.  The same construction disproves, for every
fixed `ell>=2`,

\[
 \sum_C c(p_C)^{1-\ell}{T(C)\choose\ell}w(C)
 \le m^{o(1)}Nk^4.                                    \tag{1.3}
\]

The obstruction is a single determinant-qualified metric star with
`Theta(k)` arms at the scalar exposed by a dense Golomb clean core.  It
upgrades the previous `Theta(k)` disjoint-wedge weight to the extremal
`Theta(k^2)` endpoint-wedge weight while using only `Theta(k)` points.

The actual outer-translation normalization survives, sharply:

\[
 \boxed{
 \sum_{C\text{ at }p}{T(C)\over c(p)}W_{r(p),N}
 =\Theta(k^5)=\Theta(Nk^3).}                          \tag{1.4}
\]

Thus this is not a counterexample to the lossless `1/c(p)` gate or to the
original scalar aggregate.  It proves that the reciprocal factor must
remain inside the terminal estimate.  If one performs a further
`ell`-pool after the outer normalization, the correct coefficient is
`c(p)^(-ell)`, not `c(p)^(1-ell)`.

## 2. The Golomb source core

Use the dense collinear Golomb construction from
`SYNCHRONIZED_GLOBAL_MULTI_WEDGE_GOLOMB_COUNTEREXAMPLE.md`.  Before adding
metric points, it supplies an ordered source pair `p=(s,t)` and absolute
constants `alpha,beta>0` such that

\[
 c_0(p)\ge\alpha n^2,qquad O_0(p)\ge\beta n^3.       \tag{2.1}
\]

Every old one-role base has at least

\[
 c_0(p)-(15n-36)=\Theta(n^2)                          \tag{2.2}
\]

old fully transverse third translations.  The reverse trivial wedge
bound `O_0(p)=O(nc_0)=O(n^3)` shows that (2.1) has the exact order
`Theta(n^3)`.

Scale the ruler by `6z`.  With `Delta_0=delta(s)-delta(t)` before this
scaling, put

\[
 r=-2z^2\Delta_0.                                     \tag{2.3}
\]

Then `delta(s)-delta(t)=-18r`, and `r` is a nonzero even integer.

## 3. One metric star gives quadratic wedge weight

Let `M=floor(delta n)`, for a sufficiently small absolute `delta>0`.
Choose distinct odd integers `v_1,...,v_M` and define

\[
 X_i={r+v_i^2+1\over2},\qquad
 u_i={r+v_i^2-1\over2}=X_i-1.                         \tag{3.1}
\]

For one common origin `o`, install the `M` first edges

\[
 e_i=\{o,o+(X_i,0)\}.                                 \tag{3.2}
\]

For each `i`, use two fresh points, with an independently chosen centre,
to install a partner edge `f_i` of vector `(u_i,v_i)`.  The exact identity

\[
 \delta(e_i)-\delta(f_i)
 =X_i^2-(u_i^2+v_i^2)=r                               \tag{3.3}
\]

holds for every arm.  Its doubled cross determinant is

\[
 |2\det((X_i,0),(u_i,v_i))|=|2X_iv_i|.                \tag{3.4}
\]

Choose `z` polynomially large enough that (3.4) exceeds the final
`N=binom(n+1+3M,2)` for every `i`.  The determinant-qualified first-edge
graph at scalar `r` contains the star (3.2), hence

\[
 \boxed{W_{r,N}\ge {M\choose2}=\Theta(n^2).}          \tag{3.5}
\]

Only `1+3M=Theta(n)` new points were used.

## 4. Polynomial-height distance-Sidon realization

The vertical parameters can be chosen with polynomial height while making
the forced first-edge star distance-Sidon.  Take a dense Golomb ruler

\[
 G=\{g_1,\ldots,g_M\}\subset[0,CM^2],                \tag{4.1}
\]

choose an integer `B>10(max G)^2`, and set

\[
 v_i=2(B+g_i)+1.                                      \tag{4.2}
\]

These are odd and polynomially bounded.  The squared marks `v_i^2` form
a Golomb ruler.  Indeed, writing `d=g_i-g_j`, an equality
`v_i^2-v_j^2=v_a^2-v_b^2` becomes

\[
 d(2B+g_i+g_j+1)
 =d'(2B+g_a+g_b+1).                                   \tag{4.3}
\]

If `d!=d'`, the contribution `2B(d-d')` is larger in absolute value than
the remaining `O((max G)^2)` terms, impossible.  Hence `d=d'`, and Golomb
uniqueness gives `(i,j)=(a,b)`.  Since

\[
 X_i-X_j={v_i^2-v_j^2\over2},                         \tag{4.4}
\]

the `M+1` points in (3.2) have all mutual distances distinct.

The forced labels are

\[
 X_i^2,qquad X_i^2-r,qquad (X_i-X_j)^2.             \tag{4.5}
\]

After (4.1)--(4.4), every unwanted equality between two labels in (4.5),
or between one of them and a core label, is a nonzero bounded-degree
polynomial equation in `z`.  There are only `O(n^4)` such equations, so a
polynomial interval contains a value of `z` which avoids them all and
satisfies the determinant cutoff.

Now regard `o` and the `M` partner centres as free integer vectors.  Every
remaining repeated point, pair sum, or squared distance is the zero set of
a nonzero polynomial of degree at most two in these variables.  Add all
unintended equations

\[
 \delta(e)-\delta(f)=r                                \tag{4.6}
\]

to the avoidance list.  Coefficient comparison leaves only the `M`
forced arm relations (3.3).  The grid nonvanishing lemma avoids the union
of these `n^(O(1))` bad hypersurfaces on a grid of polynomial side length.

The resulting set is integral, globally distance-Sidon, and has globally
unique unordered pair sums.  It has height

\[
 m=n^{O(1)}.                                          \tag{4.7}
\]

Moreover the only scalar-`r` distance-gap records are the `M` installed
arms.  The first edges form one star and the partner edges are disjoint,
so

\[
 W_{r,N}={M\choose2},qquad W_{-r,N}=0.               \tag{4.8}
\]

## 5. The old rich bases survive

The `t=1+3M=O(delta n)` new points create at most

\[
 E_{\rm new}
 ={n+t\choose2}-{n\choose2}=O(\delta n^2)            \tag{5.1}
\]

new unordered pair sums.  Let `c_1(p)` be the final common-clean
codegree.  A translation newly entering `Q_p` must use a new target pair
sum in at least one source role, and a target sum fixes that translation
in each role.  Hence

\[
 c_1(p)\le c_0(p)+2E_{\rm new}.                       \tag{5.2}
\]

Choose `delta` so that `2E_new<=c_0/4`.  Every old base retains its old
transverse pool from (2.2), and for large `n`

\[
 T(C)\ge c_0-O(n)\ge {c_1\over2}=\Theta(n^2).        \tag{5.3}
\]

Thus `Theta(n^3)` old one-role bases remain transverse-rich in the final
set.  Possible new clean translations have been paid for explicitly;
they need not be generically excluded.

## 6. Exact exponent bookkeeping

Let `\mathcal C_p` be the surviving old bases and take the symmetric scalar
weight `w(C)=W_(r,N)+W_(-r,N)=Theta(n^2)`.  From
(2.1), (3.5), and (5.3),

\[
\begin{aligned}
 \sum_{C\in\mathcal C_p}w(C)
 &=\Theta(n^3)\Theta(n^2)=\Theta(n^5),               \tag{6.1}\\
 \sum_{C\in\mathcal C_p}T(C)w(C)
 &=\Theta(n^3)\Theta(n^2)\Theta(n^2)
   =\boxed{\Theta(n^7)},                              \tag{6.2}\\
 \sum_{C\in\mathcal C_p}{T(C)\over c_1(p)}w(C)
 &=\Theta(n^3)\Theta(1)\Theta(n^2)
   =\boxed{\Theta(n^5)}.                              \tag{6.3}
\end{aligned}
\]

The final `k=n+1+3M=Theta(n)` and `N=Theta(n^2)`.  Therefore (6.2)
exceeds `Nk^4=Theta(n^6)` by a factor `n`, proving (1.2), while (6.3)
exactly matches `Nk^3=Theta(n^5)`.

For fixed `ell>=2`, define the pre-normalized and outer-normalized pool
masses at this pair by

\[
\begin{aligned}
 P_\ell^{\rm pre}
 &=\sum_C c_1^{1-\ell}{T(C)\choose\ell}w(C),\\
 P_\ell^{\rm out}
 &=\sum_C c_1^{-\ell}{T(C)\choose\ell}w(C).
                                                               \tag{6.4}
\end{aligned}
\]

Since `T(C)=Theta(c_1)`,

\[
 \boxed{P_\ell^{\rm pre}=\Theta(n^7),\qquad
        P_\ell^{\rm out}=\Theta(n^5).}                \tag{6.5}
\]

Thus `c^(1-ell)` merely normalizes an `ell`-pool back to the already false
once-amplified mass.  Preserving the outer `1/c` changes the coefficient
to `c^(-ell)` and returns the original sharp scale.

The raw scalar-gap multiplicity here is only `R_D(r)=Theta(n)`, so the
selected common-translation product is `c(p)R_D(r)=Theta(n^3)`.  This is
far below `Nk^3=Theta(n^5)`.  The construction disproves the amplified
sufficient theorem, not the original scalar conjecture or Problem 1208.

## 7. Exact certificate

The verifier uses the stored 60-mark Ruzsa core and one 12-arm star.  The
97-point union has all 4,656 squared distances and pair sums distinct.  Its
profile is

\[
\begin{array}{c|r}
\text{quantity}&\text{value}\\ \hline
k,N&97,\ 4,656\\
\#\text{ clean fibres},H&5,112,\ 1,519,236\\
c(p)&326\\
O(p),\ \#\text{ rich bases}&6,369,\ 6,369\\
\min T(C),\max T(C)&185,\ 250\\
\sum_CT(C)&1,387,749\\
\sum_C{T(C)\choose2}&150,763,816\\
\#\text{ qualified first edges at }r&12\\
W_{r,N},W_{-r,N}&66,\ 0\\
R_D(r),R_D(-r)&12,\ 12\\
\sum_Cw(C)&420,354\\
\sum_C(T(C)/c)w(C)&45,795,717/163\\
\sum_CT(C)w(C)&91,591,434\\
P_2^{\rm pre}&4,975,205,928/163\\
P_2^{\rm out}&2,487,602,964/26,569\\
Nk^3&4,249,405,488\\
Nk^4&412,192,332,336.
\end{array}                                           \tag{7.1}
\]

The finite instance is a structural shadow rather than an asymptotic
numerical violation.  It checks the global Sidon conditions, every clean
fibre, the exact source codegree, every one-role/transverse base, all
twelve scalar identities and determinant cutoffs, the forward and reverse
qualified wedge graphs, and all normalized masses in (7.1).

Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_actual_codegree_normalized_large_star_barrier.py
```

## 8. Consequence

The once-amplified `Nk^4` route is irreparable by actual-codegree
normalization applied only after forming the third-translation mass.  A
large metric star makes the common-clean codegree and scalar endpoint
wedge weight simultaneously quadratic, and the two factors are
independent at polynomial height.

The live theorem must be stated directly for the lossless outer-normalized
mass

\[
 \sum_C{1\over c(p_C)}
       \sum_{q_0\in Q_{p_C}}\tau(C,q_0)w(C)           \tag{8.1}
\]

at scale `m^(o(1))Nk^3`, or for an exactly equivalent outer-normalized
pool with coefficient `c(p)^(-ell)`.  The large-star family is the sharp
equality model which any such proof must permit.
