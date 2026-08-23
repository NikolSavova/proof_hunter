# Certificate for the explicit Erdős 1208 exponent

`verify_record.py` is the dependency-closed, single-field verifier shipped
with the paper. It uses only the Python standard library and PARI/GP. It was
tested with Python 3.13 and PARI/GP 2.17.4.

Run from this directory:

```sh
python3 verify_record.py
```

The run takes roughly two minutes on an Apple M-series laptop. A successful
run ends with:

```text
CM quadratic-11235917 F_2(n) << n^0.49368323: CERTIFIED
```

The full reference transcript is in `expected_output.txt`.

The script checks, rather than assumes:

- the certified BNF, ordinary and narrow class groups, and localized class
  group (`bnfcertify = 1`, hence no GRH);
- the exact 215-dimensional sign/modulo-4 Kummer kernel;
- rank four of the 4-by-217 local-character matrix, hence `V_T = 0`;
- all 11,123 useful primes and the saturated integer relation budget;
- the full local frontier and endpoint inequalities at 100 and 150 digits;
- the fallback exponents under relation bounds `r_0 <= d+2` and
  `r_0 <= d+6`.

The repository-level hostile verifier remains a structurally independent
reconstruction. This directory is intended to be deposited unchanged with
the paper and assigned an immutable URL or DOI.
