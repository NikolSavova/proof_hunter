#!/usr/bin/env python3
"""Reproduce the finite 134-point sampled-spectrum W4 audit."""

import argparse
import math
from pathlib import Path
import subprocess
import tempfile


HERE = Path(__file__).resolve().parent
EXPECTED = (
    "sampled_profiles=894 min_CU=(2562123,33305052) "
    "product=85331639745396\n"
    "W4_sample=204331272672794 "
    "witnesses=(1118689,355504811) (3842402,27715665) "
    "(355504811,1118689)\n"
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        help="reuse a previously generated 512-direction combinatorial input",
    )
    args = parser.parse_args()

    if args.input:
        data = args.input.read_bytes()
    else:
        generated = subprocess.run(
            [
                "python3",
                str(HERE / "generate_level4_sampled_input.py"),
                "--samples",
                "512",
            ],
            check=True,
            stdout=subprocess.PIPE,
        )
        data = generated.stdout

    with tempfile.TemporaryDirectory(prefix="proof_hunter_w4_") as tmp:
        binary = Path(tmp) / "sample_w4"
        subprocess.run(
            [
                "clang++",
                "-O3",
                "-std=c++17",
                str(HERE / "explore_level4_sampled_spectrum.cpp"),
                "-o",
                str(binary),
            ],
            check=True,
        )
        result = subprocess.run(
            [str(binary)], input=data, check=True, stdout=subprocess.PIPE
        )
    output = result.stdout.decode()
    assert output == EXPECTED, output

    coefficient = math.log2(204331272672794) / math.log2(404) ** 2
    assert abs(coefficient - 0.6341378038955277) < 1e-15
    print(
        "PASS: exact sampled profiles=894; "
        "W4_sample=204331272672794; n=404 coefficient=%.12f"
        % coefficient
    )


if __name__ == "__main__":
    main()
