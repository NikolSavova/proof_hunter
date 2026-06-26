# Using OpenEvolve on This Machine

Instructions for AI agents. OpenEvolve is an evolutionary coding agent (open-source
AlphaEvolve): it uses an LLM to iteratively mutate a program and keeps the variants
that score best on an evaluator.

## Where it lives

- **Install:** `/Users/nikolsavova/maths/openevolve` — editable clone in an isolated
  venv at `.venv` (Python 3.14). Already installed and verified working.
- **OpenAI key:** `~/.config/proof_hunter/openai_key.txt` (plaintext `sk-proj-…` key,
  kept OUTSIDE the repo so it is never committed). `env.sh` reads it from there.

## Activate the environment

```bash
cd /Users/nikolsavova/maths/openevolve
source env.sh      # activates the venv AND exports OPENAI_API_KEY from the key file
```

`env.sh` reads the key from the file above, so the secret lives in only one place.

## Run an example

```bash
python openevolve-run.py \
  examples/function_minimization/initial_program.py \
  examples/function_minimization/evaluator.py \
  --config examples/function_minimization/config_openai.yaml \
  --iterations 50
```

Output (including `best/best_program.py`) lands in the example's
`openevolve_output/` folder.

## Provider note

Stock `config.yaml` files in `examples/` default to **Google Gemini**. Use the
`config_openai.yaml` variants (created for this machine) to run on **OpenAI**
(`gpt-5-mini` / `gpt-5-nano`, `api_base: https://api.openai.com/v1`). To make a new
one, copy a `config.yaml` and set `primary_model`, `secondary_model`, and `api_base`.

## Starting a new project

OpenEvolve needs three things:

1. **`initial_program.py`** — the code to evolve. Wrap the region the LLM may change
   with markers:
   ```python
   # EVOLVE-BLOCK-START
   ...code to evolve...
   # EVOLVE-BLOCK-END
   ```
2. **`evaluator.py`** — defines `evaluate(program_path)` returning a dict of metrics
   (higher = better). This is the fitness function that drives evolution.
3. **`config.yaml`** — models, iterations, and evolution settings.

Copy any folder under `examples/` as a template. Run with `openevolve-run.py` as above.

## Tips

- Smoke-test with `--iterations 3` before a long run to confirm the loop and API key work.
- Evolution makes real LLM API calls — each iteration costs tokens/money.
- Full docs: https://github.com/algorithmicsuperintelligence/openevolve
