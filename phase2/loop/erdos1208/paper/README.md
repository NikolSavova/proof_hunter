# Paper build and verification

This directory contains the concise paper draft proving

\[
F_2(n)\ll n^{0.49368323}.
\]

Build it with:

```sh
latexmk -pdf main.tex
```

If `latexmk` is unavailable, use:

```sh
tectonic main.tex
```

Run the dependency-closed certificate shipped with the paper:

```sh
python3 certificate/verify_record.py
```

From the repository root, the development copy of the same canonical
certificate is:

```sh
python3 phase2/loop/erdos1208/verify_cm_eisenstein_real_quadratic_11235917.py
```

Run the independent hostile reconstruction with:

```sh
python3 phase2/loop/erdos1208/verify_independent_hostile_quadratic11235917_cm.py
```

All three scripts require PARI/GP. They reconstruct the exact field and
Kummer data, certify `V_T = 0`, check all selected primes and the
Golod--Shafarevich budget, and repeat the numerical endpoint calculation at
high precision. The dependency-closed script also checks the desaturated
fallback exponents stated in the paper.

Revision status:

1. the independent referee pass and all three finite verifiers pass;
2. the tame totally real Shafarevich--Koch theorem is now stated with its
   exact rank formulas, theorem-number citations, and `p = 2` archimedean
   bookkeeping;
3. a final specialist check of that theorem-to-notation mapping remains
   prudent before submission;
4. a final MathSciNet/zbMATH and Erdős Problems forum sweep remains human;
5. deposit `certificate/` in a DOI-backed archive and record the identifier
   below when available;
6. adapt the date and front matter to the target venue.

Immutable certificate snapshot:
https://github.com/NikolSavova/proof_hunter/tree/c6f68c4b8dc458242f317f2c5f3d76ce4df36e5f/phase2/loop/erdos1208/paper/certificate
