#!/usr/bin/env python3
"""wave6b numerics referee for sol_s3_20260812.md — script 4: exact-rational floor checks.

 [C1] parse the archived exact J0(W) fractions (wave-5 Lemma E.2, out_e1_pricing_certificate.txt)
      and confirm the draft's SOL.18 decimal renderings truncate them correctly
 [C2] the draft's rational floors 17/25, 11/10, 19/10, 5/2, 18/5, 41/10, 9/2 <= exact J0 (old table)
 [C3] REM* route: J* = R42*/2 + (3/10) R31*^2 at the OLD targets; REM*_exact := J* - J0_exact;
      check the draft's REM* upper-bound list dominates it, and that J* - ub still clears the floors
 [C4] parse the scout's NEW (grown) exact J0 fractions (out_scout_s1_targets.txt);
      verify OLD J0 < NEW J0 on every band  ==> the draft's stale thresholds are the SAFE direction
 [C5] the draft's seven final comparisons (claimed sup bound vs floor), exact
 [C6] the box-count arithmetic 36*2048*256
"""
import re
from fractions import Fraction

E1 = ("/Users/sihaohuang/Desktop/Coding/proof_hunter/phase2/bruhat/f2_drafts/g2_scripts/"
      "campaign_20260811/wave5_sl4pe/out_e1_pricing_certificate.txt")
SC = ("/Users/sihaohuang/Desktop/Coding/proof_hunter/phase2/bruhat/f2_drafts/g2_scripts/"
      "campaign_20260811/wave6_scout/out_scout_s1_targets.txt")
BANDS = ["W1", "W2", "W3", "W4", "W5", "W6b", "W7"]

def parse_fracs(path, tag):
    txt = open(path).read()
    line = next(l for l in txt.splitlines() if tag in l)
    out = {}
    for b in BANDS:
        mm = re.search(rf"{b}=(\d+)/(\d+)", line)
        out[b] = Fraction(int(mm.group(1)), int(mm.group(2)))
    return out

print("=== [C1] archived exact J0 (old, Lemma E.2) vs the draft's SOL.18 decimals ===", flush=True)
J0_old = parse_fracs(E1, "exact J0:")
draft_dec = {"W1": "0.682942", "W2": "1.10268", "W3": "1.91562", "W4": "2.53645",
             "W5": "3.66793", "W6b": "4.17806", "W7": "4.59597"}
for b in BANDS:
    f = J0_old[b]
    s = f"{float(f):.6f}"
    ok = s.startswith(draft_dec[b][:7]) or abs(float(f) - float(draft_dec[b])) < 1e-5
    print(f"  {b}: exact J0 = {float(f):.10f}  draft prints {draft_dec[b]}...  consistent: {ok}")

print("=== [C2] draft floors <= exact old J0 ===", flush=True)
floors = {"W1": Fraction(17, 25), "W2": Fraction(11, 10), "W3": Fraction(19, 10),
          "W4": Fraction(5, 2), "W5": Fraction(18, 5), "W6b": Fraction(41, 10),
          "W7": Fraction(9, 2)}
allok = True
for b in BANDS:
    ok = floors[b] <= J0_old[b]
    allok &= ok
    print(f"  {b}: {floors[b]} <= J0 exact: {ok}  (slack = {float(J0_old[b]-floors[b]):.6f})")
print(f"  ALL FLOORS VALID: {allok}", flush=True)

print("=== [C3] REM* upper-bound list of the draft ===", flush=True)
R31_old = {"W1": Fraction(1), "W2": Fraction(12, 10), "W3": Fraction(15, 10),
           "W4": Fraction(17, 10), "W5": Fraction(2), "W6b": Fraction(21, 10),
           "W7": Fraction(22, 10)}
R42_old = {"W1": Fraction(8, 10), "W2": Fraction(14, 10), "W3": Fraction(26, 10),
           "W4": Fraction(35, 10), "W5": Fraction(52, 10), "W6b": Fraction(6),
           "W7": Fraction(66, 10)}
rem_ub = {"W1": Fraction(9, 500), "W2": Fraction(3, 100), "W3": Fraction(3, 50),
          "W4": Fraction(81, 1000), "W5": Fraction(133, 1000), "W6b": Fraction(29, 200),
          "W7": Fraction(157, 1000)}
allok = True
for b in BANDS:
    Jstar = R42_old[b]/2 + Fraction(3, 10)*R31_old[b]**2
    rem_exact = Jstar - J0_old[b]
    ok1 = rem_exact <= rem_ub[b]
    ok2 = Jstar - rem_ub[b] >= floors[b]
    allok &= ok1 and ok2
    print(f"  {b}: J* = {float(Jstar):.4f}  REM*_exact = {float(rem_exact):.6f} <= ub {rem_ub[b]}: {ok1}; "
          f"J* - ub >= floor: {ok2}")
print(f"  REM* recovery route valid: {allok}", flush=True)

print("=== [C4] stale-vs-grown J0 (scout recalibration) ===", flush=True)
J0_new = parse_fracs(SC, "exact J0 fractions:")
allok = True
for b in BANDS:
    ok = J0_old[b] < J0_new[b]
    allok &= ok
    print(f"  {b}: J0_old = {float(J0_old[b]):.6f}  J0_new = {float(J0_new[b]):.6f}  old < new: {ok}")
print(f"  DRAFT'S STALE TABLE IS THE SAFE DIRECTION ON EVERY BAND: {allok}")
print("  (the draft proves J <= J0_old; since J0_old < J0_new bandwise, the grown-"
      "threshold form of (S3) follows a fortiori — but the draft nowhere says so)", flush=True)

print("=== [C5] the seven final comparisons (claimed sup vs floor), exact ===", flush=True)
sups = {"W1": Fraction(1, 2), "W2": Fraction(13, 20), "W3": Fraction(9, 10),
        "W4": Fraction(11, 10), "W5": Fraction(3, 2), "W6b": Fraction(17, 10),
        "W7": Fraction(12, 5)}
allok = True
for b in BANDS:
    ok = sups[b] < floors[b]
    allok &= ok
    print(f"  {b}: {sups[b]} < {floors[b]}: {ok}")
print(f"  ALL SEVEN STRICT: {allok}", flush=True)

print("=== [C6] box count ===", flush=True)
print(f"  36*2048*256 = {36*2048*256}  == 18874368: {36*2048*256 == 18874368}")
print("  (band w-lengths 1+1+2+2+10+20 = 36 units, 2048 cells/unit, 256 z-cells)")
print("DONE ref4", flush=True)
