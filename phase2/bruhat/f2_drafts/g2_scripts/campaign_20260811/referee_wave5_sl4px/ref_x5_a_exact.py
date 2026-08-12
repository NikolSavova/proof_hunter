# referee_wave5_sl4px/ref_x5_a_exact.py
# Adversarial numerics referee, wave-5 SL4'-X deliverable.
# [RA] Independent re-derivation of the NX-1..NX-6 constants:
#   - exact Fraction arithmetic wherever the quantity is rational
#     (NX-1a/1b/1c, NX-3a f(0.8) & f(1.074), NX-3b, NX-4 left side);
#   - dps-80 mpmath (vs the draft's dps-50) for the transcendental ones,
#     PLUS sign-safe reformulations that avoid log/asin where possible
#     (NX-2 via exp, NX-4 via exp, NX-5 via sin vs sinh);
#   - digit-string comparison against every number printed in the
#     draft's block [A].
from mpmath import mp
from fractions import Fraction as F

mp.dps = 80
ok_all = True
def rep(label, cond, detail):
    global ok_all
    ok_all = ok_all and bool(cond)
    print(f"  {label}: {detail} : {'OK' if cond else '** FAIL **'}")

print("[RA] exact / dps-80 independent re-derivation of NX-1..NX-6")

# --- NX-1a (exact) ---
tmax = F(1074, 1000) * F(89, 100)
y0 = tmax / 2
rep("NX-1a", tmax == F(95586, 100000) and y0 == F(47793, 100000),
    f"1.074*0.89 = {tmax} = 0.95586, y0 = {y0} = 0.47793, both exact")

# --- NX-1b in EXACT rationals: 1 - y0^2/6 >= 96193/100000 ---
floor_exact = 1 - y0*y0/6
rep("NX-1b-exact", floor_exact >= F(96193, 100000),
    f"1 - y0^2/6 = {floor_exact} = {float(floor_exact):.11f} >= 0.96193 (exact rational compare)")
# digit check vs draft's printed 0.96193048585
rep("NX-1b-digits", abs(float(floor_exact) - 0.96193048585) < 5e-12,
    f"printed 0.96193048585 vs exact {float(floor_exact):.11f}")

# --- NX-1c (exact) ---
rep("NX-1c", 2*F(96193,100000) == F(192386,100000) and F(192386,100000) >= F(19238,10000),
    "2*0.96193 = 1.92386 >= 1.9238 (exact)")

# --- NX-2: psi(0.8) = 1.9238 log(1.64) - 0.8 >= 0.1516 ---
# sign-safe form avoiding log: equivalent to  1.64 >= exp((0.8+0.1516)/1.9238)
rhs = mp.e**(( mp.mpf('0.8') + mp.mpf('0.1516') ) / mp.mpf('1.9238'))
psi08 = mp.mpf('1.9238')*mp.log(mp.mpf('1.64')) - mp.mpf('0.8')
rep("NX-2-exp", mp.mpf('1.64') >= rhs,
    f"1.64 >= exp(0.9516/1.9238) = {mp.nstr(rhs, 15)} (log-free reformulation)")
rep("NX-2-digits", abs(psi08 - mp.mpf('0.151696630044')) < mp.mpf('5e-13'),
    f"psi(0.8) = {mp.nstr(psi08, 12)} vs printed 0.151696630044; margin over 0.1516 = {mp.nstr(psi08-mp.mpf('0.1516'),4)}")

# --- NX-3a in EXACT rationals ---
f08 = 2*F(8,10)/(1 + F(8,10)**2)          # = 40/41
f1074 = 2*F(1074,1000)/(1 + F(1074,1000)**2)
rep("NX-3a-exact", f08 == F(40,41) and min(f08, f1074) >= F(9756,10000),
    f"f(0.8) = {f08} = {float(f08):.10f}, f(1.074) = {float(f1074):.10f}, min >= 0.9756 (exact)")
rep("NX-3a-digits", abs(float(f08) - 0.9756097561) < 5e-11 and abs(float(f1074) - 0.9974571344) < 5e-11,
    "printed 0.9756097561 / 0.9974571344 both reproduce")
# claim 'min of 2tau/(1+tau^2) on [0.8,1.074] is at an endpoint': derivative
# 2(1-tau^2)/(1+tau^2)^2 is > 0 on [0.8,1), < 0 on (1,1.074] -- verified by a
# 5001-pt dense scan against both endpoints
worst = min(2*t/(1+t*t) for t in [mp.mpf('0.8') + (mp.mpf('1.074')-mp.mpf('0.8'))*i/5000 for i in range(5001)])
rep("NX-3a-scan", worst >= float(f08) - 1e-15,
    f"dense 5001-pt scan min = {mp.nstr(worst, 12)} attained at tau = 0.8 (endpoint-min claim holds)")

# --- NX-3b (exact) ---
psip = F(19238,10000)*F(9756,10000) - 1
rep("NX-3b-exact", psip == F(87685928, 100000000) and psip >= F(8768,10000),
    f"1.9238*0.9756 - 1 = {float(psip):.8f} = 0.87685928 exactly >= 0.8768")

# --- NX-4: 1.53904 >= 1.539 (exact) and > 1/log2 via exp ---
Mfl = F(19238,10000)*F(8,10)
# 1.53904 > 1/log2  <=>  log2 > 1/1.53904  <=>  2 > exp(100000/153904)
rhs4 = mp.e**(mp.mpf(100000)/153904)
il2 = 1/mp.log(2)
rep("NX-4-exact", Mfl == F(153904,100000) and Mfl >= F(1539,1000),
    "c*0.8 = 1.53904 exactly >= 1.539")
rep("NX-4-exp", mp.mpf(2) > rhs4,
    f"2 > exp(1/1.53904) = {mp.nstr(rhs4, 15)} (equiv. 1.53904 > 1/log2 = {mp.nstr(il2, 10)})")

# --- NX-5: tau0(0.89)/0.89 <= 1.0739, sign-safe via sin vs sinh ---
# tau0(0.89)/0.89 <= 1.0739  <=>  arcsin(sinh(0.445)) <= 0.89*1.0739/2 = 0.4778855
#                            <=>  sinh(0.445) <= sin(0.4778855)
lhs5 = mp.sinh(mp.mpf('0.445'))
rhs5 = mp.sin(mp.mpf('0.89')*mp.mpf('1.0739')/2)
tau0max = 2*mp.asin(mp.sinh(mp.mpf('0.89')/2))/mp.mpf('0.89')
rep("NX-5-sin", lhs5 <= rhs5,
    f"sinh(0.445) = {mp.nstr(lhs5, 12)} <= sin(0.4778855) = {mp.nstr(rhs5, 12)} (asin-free reformulation)")
rep("NX-5-digits", abs(tau0max - mp.mpf('1.07372378042')) < mp.mpf('5e-12'),
    f"tau0(0.89)/0.89 = {mp.nstr(tau0max, 15)} vs printed 1.07372378042; < 1.074 margin = {mp.nstr(mp.mpf('1.074')-tau0max, 4)}")

# --- NX-6: geometric bound in EXACT rationals; sinh at dps 80 ---
geo = F(445,1000)/(1 - F(445,1000)**2/6)
sh = mp.sinh(mp.mpf('0.445'))
rep("NX-6-exact", geo <= F(4602,10000),
    f"0.445/(1-0.445^2/6) = {float(geo):.10f} <= 0.4602 (exact rational compare)")
rep("NX-6-sinh", sh <= mp.mpf(geo.numerator)/geo.denominator and sh < 1,
    f"sinh(0.445) = {mp.nstr(sh, 11)} <= geo (margin {mp.nstr(mp.mpf(geo.numerator)/geo.denominator - sh, 4)}) and < 1")
rep("NX-6-digits", abs(sh - mp.mpf('0.4598329599')) < mp.mpf('5e-11') and abs(float(geo) - 0.4601881256) < 5e-11,
    "printed 0.4598329599 / 0.4601881256 both reproduce")
# series-domination check used in the Cor X.2 proof: (2k+1)! >= 6^k, k <= 20
import math
sd = all(math.factorial(2*k+1) >= 6**k for k in range(21))
rep("NX-6-series", sd, "(2k+1)! >= 6^k verified k = 0..20 (induction base+shape)")

print(f"[RA] ALL {'OK' if ok_all else '** SOME FAIL **'}")
