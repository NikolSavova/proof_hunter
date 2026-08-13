# Paper build and verification

This directory contains the submission-oriented draft of the audited
coefficient-`1/2` upper bound for Erd\H{o}s problem 838.

Build the paper with:

```sh
latexmk -pdf main.tex
```

Run the independent finite verification from the parent directory with:

```sh
python lexicographic_blowup.py
python agent_geometry/audit_blowup_classification.py
python agent_asymptotic/endpoint_reset_certificate.py
```

The first program checks the exact substitution formulas against unrelated
dynamic programs, including the reported 36-point count. The second uses a
nonconvex four-point macro-skeleton and exhausts all subsets of an exact
rational 16-point composition. The third exhaustively checks the elementary
reset inequalities on a finite integer box and prints the explicit
asymptotic bound; it does not encode the heavy-path part of the proof.

Before submission:

1. add the authors and affiliations;
2. have a geometer run the final MathSciNet/Zentralblatt similarity check;
3. archive the code and record its persistent URL/DOI here;
4. remove the draft date after venue formatting.
