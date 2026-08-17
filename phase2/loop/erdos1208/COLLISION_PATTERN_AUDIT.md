# Collision-pattern audit for the rotated triple map

## Plain-language summary

The first `q=5` row-span certificate is algebraically correct but unusable: it
relies on collisions between diagonal and off-diagonal triples, which are
already impossible in every distance-Sidon set and are not forced by small
off-diagonal support.  A search restricted to feasible fibre matchings found a
real off-diagonal forbidden pattern—an alternating three-cycle of
representations—but no extremal theorem forces it.  This closes the original
finite-pattern lead and prevents a false claim that four compressed rows were
progress toward the full theorem.

## 1. Collision rows

Identify the plane with the complex numbers and write

\[
 \Phi(a,b,c)=a+i b-i c.
\]

A collision between triples `t=(r,s,t)` and `t'=(r',s',t')`
gives the Gaussian-linear row

\[
 a_r+i a_s-i a_t-a_{r'}-i a_{s'}+i a_{t'}=0.   \tag{1.1}
\]

Distance uniqueness has two immediate consequences that every pattern search
must enforce:

1. both triples are off-diagonal (`s!=t` and `s'!=t'`) unless both are
   diagonal;
2. within one output fibre, each coordinate projection is injective.

Most importantly, no off-diagonal triple has the same output as a diagonal
triple.  Such an equality would put a nonzero vector in
`(A-A) intersect J(A-A)`.

## 2. Why the original `q=5` certificate is not viable

The stored four rows were

```text
(0,0,0) = (2,4,3)
(0,0,0) = (3,2,1)
(0,0,1) = (4,2,4)
(0,0,2) = (2,3,4)
```

with Gaussian weights

\[
 \frac{-1+3i}{5},\quad
 \frac{-1-3i}{5},\quad
 \frac{-1+2i}{5},\quad
 \frac{2+2i}{5}.
\]

Their weighted sum is exactly

\[
 (a_1-a_0)-i(a_2-a_0)=0.                       \tag{2.1}
\]

Thus the row-span calculation was correct.  But its first and second rows are
each forbidden diagonal/off-diagonal collisions.  The certificate cannot be
extracted from a collection of heavy off-diagonal fibres, and its presence in
a finite-field parabola says nothing about a real distance-Sidon set.  This is
a killed route, not an in-flight lemma.

## 3. A genuine off-diagonal local obstruction

There is a smaller pattern respecting the fibre matching conditions.  Suppose
the following three off-diagonal triples have one common output:

\[
 \Phi(a_0,a_0,a_1)
 =\Phi(a_1,a_2,a_0)
 =\Phi(a_2,a_1,a_2).                             \tag{3.1}
\]

The coordinate lists `(0,1,2)`, `(0,2,1)`, and `(1,0,2)` are separately
injective, so ordinary matching checks do not reject the pattern.  Subtracting
the second and third representations from the first and putting
`x=a_1-a_0`, `y=a_2-a_0` gives

\[
 \begin{pmatrix}
  -1-i&-i\\
  -2i&-1+i
 \end{pmatrix}
 \binom{x}{y}=0.                                  \tag{3.2}
\]

The Gaussian determinant is `4`, hence `x=y=0`.  Distinct points cannot
realize (3.1).

This alternating three-cycle is an exact forbidden configuration inside one
fibre.  It does not bound the fibre size: large tri-coloured matchings can
avoid this particular reuse of the same underlying three labels.  Nor is it
currently forced by a small number of output colours.

## 4. Decision gate

Finite collision patterns remain relevant only if accompanied by an extremal
extraction theorem.  The minimum acceptable next statement is:

> If `|A+JA-JA|<=k^(3-epsilon)`, then the off-diagonal collision colouring
> contains one member of an explicitly listed family of Gaussian row patterns
> which forces a nontrivial equality of Euclidean lengths.

No such statement is proved.  Further row-span searches without this forcing
step are stopped.  The transverse collision gate in
`PARALLEL_LINE_SUPPORT_LEMMA.md` is the active formulation.
