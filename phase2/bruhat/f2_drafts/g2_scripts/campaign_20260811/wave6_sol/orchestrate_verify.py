#!/usr/bin/env python3
"""Parallel Sol referee orchestrator — runs verify_sol.py passes concurrently at max effort."""
import subprocess, sys, threading, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
PY = "/Users/sihaohuang/Desktop/Coding/proof_hunter/problem-id/.venv/bin/python"


def run(spec):
    target, kind = spec.split(":")
    t0 = time.time()
    p = subprocess.run([PY, str(HERE / "verify_sol.py"), target, kind],
                       capture_output=True, text=True,
                       env={"SOL_EFFORT": "max", "PATH": "/usr/bin:/bin", "HOME": str(Path.home())})
    tail = (p.stdout + p.stderr).strip().splitlines()[-1:] or [""]
    print(f"[{target} {kind}] rc={p.returncode} in {time.time()-t0:.0f}s :: {tail}", flush=True)


if __name__ == "__main__":
    specs = sys.argv[1:]
    print(f"launching {len(specs)} Sol referees at effort=max", flush=True)
    ths = [threading.Thread(target=run, args=(s,)) for s in specs]
    for t in ths:
        t.start(); time.sleep(3)
    for t in ths:
        t.join()
    print("=== referees done ===")
