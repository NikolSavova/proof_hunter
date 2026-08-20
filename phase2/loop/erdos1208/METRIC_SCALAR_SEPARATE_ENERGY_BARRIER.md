# Why separate additive-energy bounds cannot prove the metric scalar gate

## 1. The tempting Cauchy step

In `METRIC_SCALAR_PAIR_SUM_CHARGE.md`, write

\[
 B=\delta(H_q),\qquad D=\delta(\Sigma),
 \qquad |B|=h,\quad |D|=N=\binom k2.
\]

For fixed nonzero integer `C`, the scalar collision energy is

\[
 \mathcal M_{q,C}
 =\sum_r r_{B-B}(Cr)r_{D-D}(-r).                \tag{1.1}
\]

Cauchy--Schwarz gives

\[
 \mathcal M_{q,C}
 \le \sqrt{E^+(B)E^+(D)},                      \tag{1.2}
\]

where dropping the divisibility restriction in the first factor only
weakens the bound.  It is tempting to seek

\[
 E^+(B)\le h^2m^{o(1)},\qquad
 E^+(D)\le N^2m^{o(1)}.                        \tag{1.3}
\]

The second inequality is impossible at the cube-root scale for a purely
numerical reason.

## 2. Range forces a polynomial excess

Every squared distance lies in `[1,2m^2]`, so

\[
 |D-D|\le4m^2+1.
\]

Since `sum_r r_(D-D)(r)=N^2`, Cauchy gives the unconditional lower bound

\[
 \boxed{
 E^+(D)=\sum_r r_{D-D}(r)^2
 \ge {N^4\over4m^2+1}.}                        \tag{2.1}
\]

At the conjectural critical scale `k=m^(2/3+o(1))`, one has
`N=m^(4/3+o(1))`, and therefore

\[
 {E^+(D)\over N^2}\ge m^{2/3-o(1)}.            \tag{2.2}
\]

Thus the full distance-label set necessarily has polynomially large
ordinary additive energy even in the regime one is trying to rule out.
No low-rank squared-distance-matrix theorem can establish (1.3), because
(2.1) uses only the number and numerical range of its distinct entries.

This does **not** disprove the coupled scalar estimate (1.1).  It shows
that the dilation-specific correlation between `B-B` and `C(D-D)` must be
bounded directly.  Replacing it by the two separate energies in (1.2)
throws away exactly the transversality needed for a cube-root proof.

## 3. Research consequence

The surviving options are therefore endpoint-sensitive coupled charges:

1. the scalar difference correlation (1.1) itself;
2. the pair-sum dilation charge `s+3(I+J)t`; or
3. the canonically oriented edge-vector charge
   `u(s)+3(I+J)u(t)` in `GAUSSIAN_EDGE_VECTOR_CHARGE.md`.

Ordinary additive energy of all distance labels, bounded-rank distance
matrices, and a black-box Fourier Cauchy step are closed lanes unless they
retain one of these couplings.
