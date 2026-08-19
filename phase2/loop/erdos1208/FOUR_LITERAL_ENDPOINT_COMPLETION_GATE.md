# A four-literal refinement of the endpoint-completion gate

## 1. Outcome

Retain the notation and records of
`SAME_MIDPOINT_LITERAL_D2_COLLISION_GATE.md`.  Thus

\[
 D=A-A,\qquad N=|D|,\qquad S=|D+D|,\qquad K=S/N,
\]

the first-stage cells are (z=(R_1,R_6)), and

\[
 M_K=\sum_z\lambda(z)^2
\]

counts ordered pairs \(\omega=(\gamma,\gamma')\) of records in one cell.
The preceding endpoint refinement records

\[
 (x,y,\alpha,\beta)
 =\bigl(R_0(\gamma),R_3(\gamma'),
        x_{R_4(\gamma)},x_{R_2(\gamma')}\bigr)
\]

and writes its load as \(\sigma(x,y,\alpha,\beta)\).

This note refines the same collision literally:

\[
 \boxed{
 \Lambda(\omega)
 =\bigl(R_0(\gamma),R_3(\gamma'),
        R_4(\gamma),R_2(\gamma')\bigr)
 =:(x,y,d,f)\in D^4.}                         \tag{1.1}
\]

Let \(\tau(x,y,d,f)=|\Lambda^{-1}(x,y,d,f)|\).  The main exact
conclusions are:

1. inside one first-stage cell, each of the projections
   \((R_0,R_4)\) and \((R_3,R_2)\) determines its record uniquely;
2. a fixed literal preimage is parametrized by only two popular shifts
   \((p,q)\), and the other two shifts are an explicit affine transform;
3. the formerly missing endpoint-completion estimate factors through the
   two more localized statements

   \[
    \sum\tau^2\le N^{o(1)}M_K,                 \tag{1.2}
   \]

   and a size-biased tail-diversity estimate stated in Section 3.

Neither remaining estimate is proved here.  The refinement is useful
because its exact genuine moments are substantially flatter than the
head-level moments, while abstract radial transversals still violate
(1.2) by a rapidly growing factor.

## 2. Exact literal parametrization

Put \(L=I+J\).  Fix a literal key \((x,y,d,f)\).  For a preimage let
\((b,\ell)=(R_1,R_6)\) be its first-stage cell and define

\[
 q=b-x,\qquad p=J(\ell-d).                     \tag{2.1}
\]

Equivalently,

\[
 b=x+q,\qquad \ell=d-Jp.                       \tag{2.2}
\]

The first record is then forced to have the seven roles

\[
 \boxed{
 (x,\ x+q,\ x+p,\ d+p-q,\ d,\ d+p-Lq,\ d-Jp).} \tag{2.3}
\]

Define

\[
 C=d+f-x-y,
 \qquad
 p'=p+J(C-q),
 \qquad
 q'=p'+x+q-f.                                  \tag{2.4}
\]

The second record is forced to have roles

\[
 \boxed{
 (f-p',\ x+q,\ f,\ y,\ x+y+q-f,\ y-Jq',\ d-Jp).} \tag{2.5}
\]

In particular the two records in (2.3)--(2.5) share exactly the required
cell \((x+q,d-Jp)\).  The identity for their common last role follows from
(2.4):

\[
 y+q'-Lp'=d-Jp.                                \tag{2.6}
\]

Consequently \(\tau(x,y,d,f)\) is exactly the number of ordered pairs
\((p,q)\) such that

\[
 p,q,p',q'\in\mathcal P_K,
 \qquad p\ne q,quad p'\ne q',                 \tag{2.7}
\]

and every entry of (2.3) and (2.5) belongs to \(D\).  Conversely these
conditions reconstruct the two original records.  There are no hidden
cell variables.

The within-cell injectivity is also immediate.  Given the cell
\((b,\ell)\) and \((R_0,R_4)=(x,d)\), equations (2.1) recover \((p,q)\)
and hence (2.3).  Given the same cell and \((R_3,R_2)=(y,f)\), the normal
form recovers \((p',q')\) and hence (2.5).  Therefore a literal preimage is
equivalently a common cell of two simple cell-incidence systems.

## 3. Exact factorization of endpoint completion

Let \(h(d)=x_d\in A\) denote the canonical head of \(d\in D\), using the
fixed diagonal decoration at zero.  For a head key put

\[
 \mathcal T_{x,y,\alpha,\beta}
 =\{(d,f):\tau(x,y,d,f)>0,
       \ h(d)=\alpha,\ h(f)=\beta\},           \tag{3.1}
\]

and write \(T_{x,y,\alpha,\beta}=|\mathcal T_{x,y,\alpha,\beta}|\).
Then the previous joint endpoint load is exactly

\[
 \sigma(x,y,\alpha,\beta)
 =\sum_{(d,f)\in\mathcal T_{x,y,\alpha,\beta}}
   \tau(x,y,d,f).                               \tag{3.2}
\]

Cauchy--Schwarz inside each head key gives

\[
 \boxed{
 \sum_{x,y,\alpha,\beta}\sigma^2
 \le
 \mathcal U_K
 :=\sum_{x,y,\alpha,\beta}
 T_{x,y,\alpha,\beta}
 \sum_{(d,f)\in\mathcal T_{x,y,\alpha,\beta}}
 \tau(x,y,d,f)^2.}                             \tag{3.3}
\]

Thus the endpoint-completion theorem from equation (6.4) of the preceding
note follows from (1.2) together with

\[
 \boxed{
 \mathcal U_K
 \le N^{o(1)}\sum_{x,y,d,f}\tau(x,y,d,f)^2.}   \tag{3.4}
\]

Equation (1.2) is a four-literal cross-cell completion theorem.  Equation
(3.4) is a size-biased tail-diversity theorem: after both heads and both
outer literals are fixed, it asks that the number of compatible endpoint
tails be subpolynomial on average.  This is strictly more localized than
the original head-completion theorem.

The separate size-biased head-diversity estimate from the preceding note
is still required to finish the full \(K\)-scaled literal gate.  The
present factorization improves the local-completion half of that program;
it does not by itself prove the cube-root result.

## 4. Collision displacements

Compare two literal preimages \((p,q)\) and \((p+r,q+s)\) of the same
key.  Equation (2.4) gives

\[
 p'\mapsto p'+r-Js,
 \qquad
 q'\mapsto q'+r+(I-J)s.                       \tag{4.1}
\]

The role displacements in the first record are

\[
 \boxed{
 (0,\ s,\ r,\ r-s,\ 0,\ r-Ls,\ -Jr),}        \tag{4.2}
\]

and those in the second record are

\[
 \boxed{
 (Js-r,\ s,\ 0,\ 0,\ s,\ -Jr-Ls,\ -Jr).}    \tag{4.3}
\]

Every displayed nonzero vector is therefore realized as a displacement
between a specified pair of elements of the same complete difference set.
At the same time all four shifts in (2.7) remain bidirectionally popular.
Equations (4.1)--(4.3) are the exact inverse data behind (1.2); deleting
the literal common roles returns to radial and affine models already known
to be too large.

## 5. Exact stress profiles

For genuine complete differences, the verifier reports

\[
 (M_K,\ \sum\tau^2,\ \mathcal U_K,
   \max\tau,\ \max T_{x,y,\alpha,\beta}).
\]

The exact rows are

\[
\begin{array}{c|r|r|r|c|c|c|c}
\text{family}&M_K&\sum\tau^2&\mathcal U_K&\max\tau&\max T&
 (\sum\tau^2)/M_K&\mathcal U_K/(\sum\tau^2)\\ \hline
\text{Costas }11&4{,}348&4{,}528&4{,}987&3&3&1.0414&1.1014\\
\text{Costas }13&5{,}530&5{,}770&6{,}600&3&3&1.0434&1.1438\\
\text{Costas }17&46{,}212&51{,}896&64{,}670&4&7&1.1230&1.2461\\
\text{Costas }19&468{,}768&554{,}424&643{,}385&6&5&1.1827&1.1605\\
\text{Costas }23&3{,}020{,}644&4{,}188{,}520&5{,}881{,}823&9&8&1.3866&1.4043\\
\text{Costas }29&11{,}791{,}516&20{,}407{,}716&28{,}848{,}423&14&8&1.7307&1.4136\\
\text{Costas }31&3{,}872{,}958&6{,}992{,}486&8{,}944{,}592&17&8&1.8055&1.2792\\
\text{Costas }37&18{,}630{,}176&28{,}102{,}892&33{,}355{,}193&12&5&1.5085&1.1869
\end{array}                                     \tag{5.1}
\]

The growing pointwise loads show again why a moment theorem is necessary.
Nevertheless both size-biased factors remain small through the largest
stored stress.

The corresponding literal ratios on abstract radial transversals are

\[
\begin{array}{c|r|r|c|c}
\text{side}&M_K&\sum\tau^2&(\sum\tau^2)/M_K&\max\tau\\ \hline
4&111{,}622&328{,}710&2.94485&12\\
6&4{,}120{,}768&35{,}214{,}340&8.54558&36\\
8&59{,}454{,}358&1{,}259{,}626{,}422&21.1864&92
\end{array}                                     \tag{5.2}
\]

Thus the four-literal moment still sharply separates genuine complete
differences from the radial impostors.  The separation is evidence for
(1.2), not a proof.

Run

```bash
python3 phase2/loop/erdos1208/verify_four_literal_endpoint_completion.py
python3 phase2/loop/erdos1208/verify_four_literal_endpoint_completion.py --extended
python3 phase2/loop/erdos1208/verify_four_literal_endpoint_completion.py --radial-8
```

for the exact parametrization, injectivity, displacement identities, and
profiles above.
