# Mass-uniform branching does not force large literal carrier fibres

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

The effective-branching improvement is real, but near-uniform conditional
label mass does not force the rooted endpoint-module fibre size \(b_g\) to
grow. There is an exact scalable planar parity-code construction in which

* \(q-1=\Theta(\log n)\) successive roles have perfectly uniform mass
  branching over \(A=n^{1-o(1)}\) actual labels;
* every record atom has weight exactly \(1/N\), where \(N\) is the ambient
  point-count parameter;
* every source and every selected target has total incident weight one;
* deleting any one selected triangular trace leaves a literal physical
  carrier which uniquely determines the deleted label, so every fine
  carrier/root fibre has \(b_g=1\); but
* deleting the trace-dependent carrier tags coarsens all fibres to the
  common boundary-ear base, where the rooted module bank has \(A^3\)
  choices per role and pays overwhelmingly.

Thus neither effective mass uniformity nor the \(1/n\) atom floor proves
large \(b_g\) after grouping by the literal carrier. The missing positive
statement is a **recoverable carrier coarsening theorem**: trace-dependent
parts of the carrier must be deleted while preserving the ear chamber and
with bounded decoder load.

The obstruction is not a minimizer counterexample. Its coarsened ambient
bank has size \(A^{3q}\), so it is globally very high-face. It is a sharp
applicability barrier and identifies exactly where the geometry, rather
than the forest entropy, must enter.

## 1. Exact information split

At one forest node, normalize the bad record mass to a probability
distribution. Let \(Z\) be the next actual role label, let \(G\) be its
physical carrier/root fibre, and assume

\[
                         \max_z\Pr[Z=z]\le{\kappa\over d}. \tag{1}
\]

Let \(E\) be the event that the row support of \(G\) has size at most
\(h\), and suppose \(\Pr[E]\ge1-\theta\). Conditioning can increase every
label probability by at most \(1/(1-\theta)\), so

\[
 H(Z\mid E)\ge\log{d(1-\theta)\over\kappa}.              \tag{2}
\]

On \(E\), the label \(Z\) has at most \(h\) possibilities after \(G\) is
known. Hence

\[
 \boxed{\displaystyle
 I(Z;G\mid E)\ge
       \log{d(1-\theta)\over\kappa h}.}                  \tag{3}
\]

This is the exact alternative to a large rooted module: if almost all mass
lies in small fibres, the carrier name stores almost all next-label
entropy.

The pathwise form is equally direct. Suppose at stages \(i=1,\ldots,s\),
conditional on the preceding labels,

\[
 H(Z_i\mid Z_{<i})\ge\log(d_i/\kappa_i),\qquad
 |\operatorname{supp}(Z_i\mid G_i,Z_{<i})|\le h_i.       \tag{4}
\]

Then

\[
\begin{aligned}
 H(G_1,\ldots,G_s)
 &\ge H(Z_1,\ldots,Z_s)-H(Z_1,\ldots,Z_s\mid G_1,\ldots,G_s)\\
 &\ge\sum_{i=1}^s\log{d_i\over\kappa_i h_i}.             \tag{5}
\end{aligned}
\]

If one ordinary output recovered the carrier itinerary with load
\(\Lambda\), (5) would give at least

\[
                \Lambda^{-1}\prod_i{d_i\over\kappa_i h_i} \tag{6}
\]

ambient outputs. The role forest supplies no such itinerary decoder:
terminal deletion can erase every \(G_i\). Formula (5) therefore locates
entropy but does not spend it.

## 2. Parity-code fragmentation

Use the rational nonadjacent-ear construction from
`HIGH_TRANSVERSAL_COMMON_POCKET_ENDPOINT_PRODUCT.md` with \(q\) roles and
\(A\) alternatives in every role. Label the target triangles by
\(\mathbb F_A\), taking \(A\) prime for simplicity, and retain only target
words

\[
 \mathcal C=\{b\in\mathbb F_A^q:
                         b_1+\cdots+b_q=0\}.             \tag{7}
\]

Thus

\[
                              |\mathcal C|=A^{q-1}.      \tag{8}
\]

Under the uniform law on \(\mathcal C\), after any prefix of length
\(i<q-1\), every next label has exactly
\(A^{q-i-2}\) completions. Therefore the effective branching ratios are

\[
                     r_1=\cdots=r_{q-1}=A,\qquad r_q=1, \tag{9}
\]

and

\[
             C_{\rm eff}=A^{q-1},\qquad Q_{\rm eff}=A.  \tag{10}
\]

This is the true low-\(Q_{\rm eff}\), mass-uniform regime.

Fix a role \(i\) and delete its selected triangle \(T_{i,b_i}\). The
literal carrier retains all other target triangles, hence all coordinates
\((b_j)_{j\ne i}\). Equation (7) uniquely determines \(b_i\). Consequently

\[
                  b_g=1\quad\text{for every literal
                  carrier/root fibre }g.                \tag{11}
\]

No weighted regrouping argument can turn (9) into a large fine-fibre
degree: the missing label entropy has been copied into the other physical
carrier roles.

## 3. The atom floor survives

Let \(N\) be the ambient point-count parameter and assume
\(|\mathcal C|\ge N\). Choose \(|\mathcal C|\) source words and put an
\(N\)-regular bipartite graph between those sources and the target words
in \(\mathcal C\), for example the cyclic graph

\[
                         s\sim c
       \quad\Longleftrightarrow\quad c-s\in\{0,\ldots,N-1\}
       \pmod{|\mathcal C|}.                              \tag{12}
\]

Give every selected edge weight \(1/N\). Then

\[
\begin{array}{c|c}
\text{quantity}&\text{exact value}\\ \hline
\text{atom weight}&1/N\\
\text{mass at every source}&1\\
\text{mass at every target}&1\\
\text{total mass}&|\mathcal C|.
\end{array}                                             \tag{13}
\]

The target marginal is uniform, so (9)--(11) are unchanged. Every source
word is convex, every target word is convex, and every selected pair is
bad through the source singleton inside the selected target triangle in
each role. Thus the construction is planar and respects both the atom floor
and the per-source mass cap.

The floor gives only

\[
                 \#\{\text{positive atoms}\}\le NM,      \tag{14}
\]

which is attained up to equality in (12)--(13). It supplies no upper bound
on the mass of one singleton carrier fibre and no cross-fibre decoder.

## 4. Why the construction is nevertheless paid

The fine carrier in (11) contains trace-dependent triangles from all the
other roles. Delete those tags and retain only the common convex base
\(K_0\). Every source mark \(x_{i,a}\) lies inside every triangle
\(T_{i,b}\), so the exact tangent lemma gives

\[
              K_0\cup\{\ell_{i,b},x_{i,a},r_{i,c}\}
                  \in\mathcal F(P)                       \tag{15}
\]

for all \(a,b,c\in[A]\). Nonadjacent ears commute, producing

\[
                              A^{3q}                     \tag{16}
\]

ordinary rooted-module faces. The selected record support in (12) has only
\(N A^{q-1}\) atoms and weighted mass \(A^{q-1}\). Hence (16) pays by an
enormous margin.

This payment does not follow from (1), (9), or the atom floor. It uses the
geometric fact that the trace-dependent portion of the carrier can be
removed without destroying the common ear chart. In a general pocket the
same deletion can merge gaps, hide old carrier vertices, or erase the
context decoder. Those are precisely the mask/run and seam obstructions.

## 5. Exact remaining theorem

At the mass-uniform forest endpoint, one now has a rigorous trichotomy.

1. Large same-\((K,x)\) trace fibres are paid by the rooted-module
   inequality
   \[
        M\le\delta\lambda
          {\sum_gb_g\over\sum_gb_g^2}V(P)^2.
   \]
2. Small fibres force the carrier itinerary entropy (3)--(5).
3. The parity construction shows that this entropy may be stored entirely
   in trace-dependent carrier roles, even with atom weight \(1/N\) and
   source mass one.

Therefore a closure must either recover the carrier itinerary in ordinary
outputs, or canonically erase its trace-dependent coordinates and prove
that the resulting coarsened pockets still support a rooted module. A
support or mass pigeonhole without this geometric coarsening is false.

## 6. Verification

Run

~~~text
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_mass_uniform_carrier_fragmentation_gate.py
~~~

The verifier checks the parity family at \(q=5,A=5\), all prefix masses,
the effective product and \(Q_{\rm eff}\), injectivity after deleting one
coordinate, the \(N\)-regular \(1/N\)-weighted incidence with unit source
and target masses, and the exact bank exponents. It also reuses the exact
rational two-ear configuration to check the planar \(q=2,A=3\) parity
slice, singleton literal fibres, and every coarsened rooted-module face.

