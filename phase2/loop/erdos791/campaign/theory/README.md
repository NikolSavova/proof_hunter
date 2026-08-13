# Reproduction

> **Audit correction:** `CP_SAT_20_116_RADIUS3.json` is not a valid exclusion;
> `sat_lean.py` normalizes `J/K` inconsistently with its radius seed. The family
> theorem and template enumeration are unaffected. See `THEORY_NOTES.md`.

From the repository root:

```bash
python3 phase2/loop/erdos791/campaign/theory/family_analysis.py --max-ell 100
python3 phase2/loop/erdos791/campaign/theory/prove_family_bound.py
python3 phase2/loop/erdos791/verifier.py \
  phase2/loop/erdos791/campaign/theory/family_20_115.json

c++ -O3 -std=c++17 \
  phase2/loop/erdos791/campaign/theory/template_exhaust.cpp \
  -o /tmp/erdos791_template
/tmp/erdos791_template

c++ -O3 -std=c++17 \
  phase2/loop/erdos791/campaign/theory/structural_search.cpp \
  -o /tmp/erdos791_structural
/tmp/erdos791_structural 2000000 8 791
```

The exact radius-three result requires OR-Tools.  Reuse the campaign SAT
environment if present, or install `requirements-search.txt` in a disposable
virtual environment, then run:

```bash
PY=phase2/loop/erdos791/campaign/sat/.venv/bin/python
$PY phase2/loop/erdos791/campaign/theory/sat_lean.py \
  --m 116 --counts 6 7 7 --h 3 --n 7 --r 1 \
  --radius 3 --seconds 60 --workers 1 --seed 200116
```

See `THEORY_NOTES.md` for the proof, scope, and honest interpretation.
