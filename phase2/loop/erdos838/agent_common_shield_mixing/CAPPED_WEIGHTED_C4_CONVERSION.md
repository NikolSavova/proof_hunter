# Sharp capped conversion from weighted to counted `C4`s

## 1. Setup

Let `G` be a finite simple bipartite graph with biadjacency matrix `A`,
`m>=1` edges, left degrees `d_i`, and right degrees `e_j`.  Put

\[
\begin{aligned}
 C&=\sum_{i,k,j,l}A_{ij}A_{il}A_{kj}A_{kl},\\
 W&=\sum_{i,k,j,l}A_{ij}A_{il}A_{kj}A_{kl}
                         d_i d_k e_j e_l,             \tag{1}\\
 z_{ij}&=d_i e_j\quad(ij\in E),\\
 K&=\max_{ij\in E}z_{ij}.
\end{aligned}
\]

Repeated vertices are allowed in `C`, as in ACP Theorem 33.

## 2. The exact cap theorem

> **Theorem 1 (sharp degree-product cap).**
> For every finite simple bipartite graph,
> \[
>                 \boxed{C\ge {W\over K^2}.}           \tag{2}
> \]
> In particular, if the two endpoint degrees are bounded by
> `Delta_L,Delta_R`, then
> \[
>                 C\ge {W\over \Delta_L^2\Delta_R^2}. \tag{3}
> \]

**Proof.**  Regard an ordered `C4` as an ordered compatible pair of
opposite edges

\[
              (ij,kl),\qquad A_{ij}A_{il}A_{kj}A_{kl}=1.
\]

Its weight in `W` is

\[
                 d_i d_k e_j e_l=z_{ij}z_{kl}\le K^2.
\]

Summing over the `C` ordered compatible pairs proves (2), and
`K<=Delta_L Delta_R` proves (3).  QED.

The localized form is sometimes more useful.  If a collection of ordered
compatible pairs has its first edge in a class with `z_e<=K_1` and its
second edge in a class with `z_f<=K_2`, then

\[
             C_{12}\ge {W_{12}\over K_1K_2}.           \tag{4}
\]

Thus only two product-degree bucket labels, one for each opposite edge,
are relevant to the conversion itself.

Theorem 1 is exactly sharp.  In any biregular graph with left degree `D`
and right degree `E`, every ordered `C4` has weight `D^2E^2`, and hence

\[
                       W=(DE)^2C=K^2C.                 \tag{5}
\]

This includes disconnected unions of complete biregular components, so
knowledge of `m` does not improve (2) in the regime `K<=m`.

## 3. Even `K/m -> infinity` gives no improvement

The scalable pendant-core family from the counterexample to `W<=m^2C`
shows that no factor depending favorably on `m/K` can improve (2) when
`K>m` either.

Let `G_{n,t}` be `K_{n,n}` with `t` pendant leaves attached to every core
vertex.  With `D=n+t`, its exact statistics are

\[
\begin{aligned}
 m&=n(n+2t),&K&=D^2,\\
 C&=n^4+4n^2t+2nt^2,\\
 W&=nD^2\bigl(n^3D^2+4ntD+2t^2\bigr).              \tag{6}
\end{aligned}
\]

Set `n=s^3,t=s^4`.  Then

\[
 {K\over m}={(s+1)^2\over2s+1}\longrightarrow\infty, \tag{7}
\]

whereas

\[
 {W\over K^2C}
 ={s^9+2s^8+s^7+4s^3+4s^2+2
   \over s^5(s+1)^2(s^2+2s+4)}
 \longrightarrow1.                                      \tag{8}
\]

The difference is the manifestly positive polynomial

\[
 K^2C-W
 =2s^{17}(s+1)^2(s^4+s^3-1)
                  (s^4+3s^3+2s^2+1).                    \tag{9}
\]

Thus `K^2` is the optimal universal divisor even along a sequence on
which `K/m` diverges.  In particular, tempting replacements such as
`mK` are false.

## 4. Product spread recovers the optimal information exponent

The cap theorem combines cleanly with the weighted dependent-random-choice
inequality used in ACP.  Let a uniform random edge have endpoints `(X,Y)`
and define

\[
 \bar z={1\over m}\sum_{ij\in E}d_i e_j,
 \qquad q={\bar z\over m},
 \qquad J=\mathbb E\log_2{m\over d_Xe_Y}.             \tag{10}
\]

Here `q` is exactly the probability that independently sampled degree-law
endpoints form an edge.  Two applications of Cauchy--Schwarz give

\[
                 {W\over m^4}\ge q^4,
 \qquad\text{or equivalently}\qquad W\ge\bar z^4.      \tag{11}
\]

For completeness, if `p_i=d_i/m`, `r_j=e_j/m`, and
`b(j,l)=sum_i p_i A_{ij}A_{il}`, then

\[
 \mathbb E_{j,l}b(j,l)^2
 \ge(\mathbb E_{j,l}b(j,l))^2
 \ge(\mathbb E_{i,j}A_{ij})^4=q^4,
\]

and the left side is `W/m^4`.

Combining (2) and (11) gives two equivalent spread-sensitive forms.  If

\[
 \Lambda_A={K\over\bar z},
 \qquad
 g=2^{\mathbb E\log_2z_{XY}}=m2^{-J},
 \qquad
 \Lambda_G={K\over g},                                  \tag{12}
\]

then

\[
 \boxed{
 C\ge {\bar z^4\over K^2}
      ={m^2q^2\over\Lambda_A^2}
      \ge {m^2 2^{-2J}\over\Lambda_G^2}.}              \tag{13}
\]

The last step also follows directly from Jensen,
`bar z>=g=m2^{-J}`.  Equivalently, if

\[
 K=m2^{-J}2^\sigma,
\]

then the exact loss supplied by the cap conversion is

\[
                       C\ge m^2 2^{-2J-2\sigma}.         \tag{14}
\]

The excess `sigma>=0` is the missing degree-product-spread coordinate.

## 5. Dyadic near-biregularity

Suppose every nonisolated left degree lies in
`[D_L,lambda_L D_L]` and every nonisolated right degree lies in
`[D_R,lambda_R D_R]`.  Then the edge products vary by a factor at most
`Lambda=lambda_L lambda_R`, so `Lambda_A,Lambda_G<=Lambda`.  Therefore

\[
 \boxed{
 C\ge {W\over
       \lambda_L^2\lambda_R^2D_L^2D_R^2},
 \qquad
 C\ge {m^2 2^{-2J}\over\lambda_L^2\lambda_R^2}.}       \tag{15}
\]

For ordinary dyadic endpoint buckets, `lambda_L=lambda_R=2`, and hence

\[
                       C\ge {m^2 2^{-2J}\over16}.       \tag{16}
\]

The conversion factor in (2) is still sharp inside an exactly biregular
bucket: (5) is equality.  The factor `16` in the information-only version
records the worst possible two-coordinate dyadic spread, not a defect of
the weighted-to-counted step.

## 6. Comparison with ACP Theorem 33

Theorem 33 works without a degree cap.  Its proof is valid for every
threshold `a>J`.  At `a=J+1`, its displayed bound becomes

\[
 C\ge {m^2 2^{-2J}
       \over64(M+J+1)^4(M+1)^8},
 \qquad M=\log_2m.                                      \tag{17}
\]

Thus (13) is stronger precisely when

\[
 \Lambda_G<8(M+J+1)^2(M+1)^4.                           \tag{18}
\]

For one dyadic near-biregular bucket, (16) improves (17) by the explicit
factor

\[
                  4(M+J+1)^4(M+1)^8.                    \tag{19}
\]

This is only a polynomial improvement.  Both the sharp cap theorem and
Theorem 33 have the same leading information loss `2J`.  In the ACP
coefficient regime `M=Theta(r^2)`, the difference is only `O(log r)`
bits.  It therefore does **not** improve the quadratic coefficient or a
fixed-power gate whose scale is `2^{Theta(r)}`.  It does remove a
polylogarithmic loss when a cap or a near-biregular bucket is already
available.

If `Lambda_G` is larger than the threshold (18), Theorem 33 is stronger.
Moreover, its edge-count bucket is not guaranteed to contain a controlled
fraction of the global weighted mass `W`; that would be an additional
hypothesis.  Hence the cap theorem is a sharp local replacement, not a
cap-free improvement of Theorem 33.

## 7. Verification artifact

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_capped_weighted_c4_conversion.py
```

The verifier exhausts all nonzero bipartite matrices through `4x4`, checks
the cap inequality and the exact integer form of weighted DRC, verifies
equality on complete biregular graphs, and checks the asymptotically sharp
`G_{s^3,s^4}` family using exact integer arithmetic.
