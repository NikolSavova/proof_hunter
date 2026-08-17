# A local positive-semidefinite barrier for the split-prime sieve

## 1. The tempting improvement

At a split residue place, make the unit-determinant change of variables which
turns the binary norm into

\[
  Q(s,t)=st
\]

over \(\mathbb F_q\).  A difference has norm zero precisely when it lies on
one of the two coordinate axes.  The squarefree sieve sums the two equivalence
relations “same first coordinate” and “same second coordinate.”  A nonzero
isotropic difference is counted once, while the zero difference is counted
twice.  That extra multiplicity is the local source of the divisor factor
\(1+q^{-1}\).

It is natural to try to count the *union* of the axes, giving the zero
difference weight one rather than two.  The union adjacency is not positive
semidefinite, so it has no uniform Cauchy--Schwarz lower bound for arbitrary
subsets.  The following calculation shows that this is not an accident.

## 2. Optimal symmetric PSD kernel

Consider a translation-invariant kernel on \(\mathbb F_q^2\), invariant under
independent nonzero scaling of the two coordinates and under swapping them,
and supported on the union of the coordinate axes.  It necessarily has the
form

\[
 K(0,0)=a,qquad
 K(s,0)=K(0,t)=b\quad(s,t\ne0),qquad
 K(s,t)=0\quad(st\ne0).                          \tag{1}
\]

Its Fourier eigenvalues have three types:

\[
\begin{array}{c|c}
 (\xi,\eta)&\widehat K(\xi,\eta)\\ \hline
 (0,0)&a+2b(q-1),\\
 \text{exactly one of }\xi,\eta\text{ zero}&a+b(q-2),\\
 \xi\eta\ne0&a-2b.
\end{array}                                      \tag{2}
\]

Therefore, for \(b\ge0\), positive semidefiniteness forces

\[
  a\ge2b.                                        \tag{3}
\]

The usual sum of the two coordinate-equivalence kernels has \(a=2\) and
\(b=1\), so it attains equality in (3).  Among symmetric
translation-invariant PSD kernels giving unit weight to every nonzero
isotropic difference, the existing sieve has the smallest possible weight at
the zero difference.

Equivalently, the union kernel has \(a=b=1\), and its last eigenvalue in (2)
is \(-1\).  This is the spectral obstruction behind the failure of a direct
union-count Cauchy inequality.

## 3. Consequence for pattern thinning and coding

Selecting a subfamily of the two local branches across many residue places
can reduce the multiplicity of highly divisible differences, but it also
reduces the entropy in the pair lower bound.  A random binary code of rate
\(R\) illustrates the exact tradeoff.  A valuation pattern with \(z\) free
coordinates meets the code in at most the schematic quantity

\[
  1+2^{z-(1-R)d+o(d)}.
\]

The first term limits the gain to \(R\log2\); the second reproduces the full
divisor factor.  Optimizing \(R\) cannot beat the original local ratio.  The
PSD lemma explains why no choice of nonnegative Cauchy weights can evade this
minimum: removing the diagonal excess introduces a negative Fourier mode.

This does not rule out an argument using a genuinely higher-order statistic
or detailed information about the chosen subset.  It does rule out the most
direct proposed repair of the pair sieve—replace the sum of branch lattices
by a universally supersaturated union kernel—and identifies the divisor loss
as structural rather than a loose packing estimate.
