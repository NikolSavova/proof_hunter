# The full directional positive-definite relaxation is too weak

## 1. Verdict

The scalar Bessel average is not the only positive-definite relaxation that
fails at the exponent level.  Even if one retains every lattice direction,
the exact total autocorrelation mass, the support box, and the constraint of
at most two directed differences on each squared-radius shell, the linear
positive-semidefinite relaxation admits

\[
 k=m^{1-o(1)}.                                                   \tag{1.1}
\]

Thus no linear program using only

\[
 h\ge0,quad \widehat h\ge0,quad h(0)=k,quad
 \sum h=k^2,quad
 \sum_{|d|^2=s}h(d)\le2                                      \tag{1.2}
\]

can prove the desired `k<=m^(2/3+o(1))`.  A successful Fourier or SDP proof
must use the zero-one/nonzero-integrality of the autocorrelation, or its
nonlinear factorization `h=1_A circ 1_A` by one actual endpoint set.

## 2. A fractional autocorrelation from the full grid

Let

\[
 X=\{0,\ldots,m\}^2,\qquad M=|X|=(m+1)^2,                     \tag{2.1}
\]

and write

\[
 g(d)=|X\cap(X+d)|.
\]

Then `g=1_X circ 1_X`, so `g>=0`, it is supported on
`[-m,m]^2`, and

\[
 \widehat g=|\widehat {1_X}|^2\ge0,qquad
 g(0)=M,qquad \sum_dg(d)=M^2.                                \tag{2.2}
\]

Let

\[
 R_m=\max_{1\le s\le2m^2}
   |\{d\in[-m,m]^2:|d|^2=s\}|,                               \tag{2.3}
\]

and choose any integer `k>=2` satisfying

\[
 k(k-1)R_m\le M-1.                                            \tag{2.4}
\]

Put

\[
 c={k(k-1)\over M(M-1)}                                      \tag{2.5}
\]

and define

\[
 h(0)=k,qquad h(d)=c g(d)\quad(d\ne0).                       \tag{2.6}

## 3. Every linear constraint is satisfied

Nonnegativity, symmetry, and the support box are immediate.  The total mass
is exact:

\[
 \sum_dh(d)
 =k+c(M^2-M)=k+k(k-1)=k^2.                                   \tag{3.1}

For every nonzero squared radius `s`, (2.3) and `g(d)<=M` give

\[
 \sum_{|d|^2=s}h(d)
 \le cMR_m
 ={k(k-1)R_m\over M-1}\le1<2.                               \tag{3.2}

Finally,

\[
 \widehat h
 =c\widehat g+(k-cM).                                     \tag{3.3}

The first term is nonnegative by (2.2), while

\[
 k-cM=k-{k(k-1)\over M-1}ge0                                \tag{3.4}

because `k<=M`.  Hence `h` is positive definite in the full two-dimensional
sense, not merely after rotation averaging.

## 4. The exponent is almost linear

The classical two-squares bound gives

\[
 R_m\le\max_{s\le2m^2}r_2(s)
 \le4\max_{s\le2m^2}\tau(s)=m^{o(1)}.                        \tag{4.1}

Taking

\[
 k=\left\lfloor\sqrt{(M-1)/R_m}\right\rfloor                \tag{4.2}

(and decreasing it by one if needed to ensure (2.4)) produces
`k=m^(1-o(1))`.  This is polynomially larger than the cube-root target
`m^(2/3+o(1))`.

The obstruction is deliberately fractional: the nonzero values `c g(d)`
are not required to be zero or one, and `h` need not factor as the
autocorrelation of an indicator.  Those are therefore the load-bearing
conditions left to exploit.

`verify_full_direction_psd_relaxation.py` checks (2.1)--(3.4) exactly for a
range of grid sizes using rational arithmetic and records the resulting
near-linear feasible values of `k`.
