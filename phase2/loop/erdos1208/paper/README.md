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

From the repository root, run the canonical finite certificate with:

```sh
python3 phase2/loop/erdos1208/verify_cm_eisenstein_real_quadratic_11235917.py
```

Run the independent hostile reconstruction with:

```sh
python3 phase2/loop/erdos1208/verify_independent_hostile_quadratic11235917_cm.py
```

Both scripts require PARI/GP. They reconstruct the exact field and Kummer
data, check all selected primes and the Golod--Shafarevich budget, and repeat
the numerical endpoint calculation at high precision.

Before submission:

1. obtain a specialist audit of the tame Shafarevich presentation interface;
2. run a final MathSciNet/zbMATH novelty and citation check;
3. archive the code and record its persistent URL or DOI here;
4. adapt the date and front matter to the target venue.
