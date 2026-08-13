#!/usr/bin/env python3
"""Parallel Sol orchestrator — the Fable-fleet pattern, driven by API calls instead.

Runs several run_sol.py targets concurrently (one thread each, always effort=max per
Sihao's 2026-08-12 policy). Each target journals its response id in ids.json, so a
dropped connection or a killed process loses nothing: rerun and it resumes.

Usage: ./orchestrate.py target [target ...]
"""
import subprocess, sys, threading, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
PY = "/Users/sihaohuang/Desktop/Coding/proof_hunter/problem-id/.venv/bin/python"
results = {}


def run(t):
    t0 = time.time()
    p = subprocess.run([PY, str(HERE / "run_sol.py"), t], capture_output=True, text=True,
                       env={"SOL_EFFORT": "max", "PATH": "/usr/bin:/bin", "HOME": str(Path.home())})
    results[t] = (p.returncode, (p.stdout + p.stderr).strip().splitlines()[-1:] or [""],
                  time.time() - t0)
    print(f"[{t}] rc={p.returncode} in {time.time()-t0:.0f}s :: {results[t][1]}", flush=True)


if __name__ == "__main__":
    targets = sys.argv[1:]
    print(f"launching {len(targets)} Sol agents at effort=max: {', '.join(targets)}", flush=True)
    ths = [threading.Thread(target=run, args=(t,)) for t in targets]
    for th in ths:
        th.start()
        time.sleep(3)
    for th in ths:
        th.join()
    print("=== all done ===")
    for t, (rc, tail, dt) in results.items():
        print(f"  {t:12s} rc={rc} {dt:6.0f}s {tail}")
