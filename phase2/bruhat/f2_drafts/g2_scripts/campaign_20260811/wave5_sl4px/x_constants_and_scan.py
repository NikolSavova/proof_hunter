# wave5_sl4px/x_constants_and_scan.py
# Wave-5 deliverable for Hypothesis SL4'-X (W1 crossover monotonicity).
# Block [A]: the named-constant certificates NX-1..NX-5 quoted in
#   wave5_sl4px_20260812.md (mpmath dps=50; every rounding in the safe
#   direction; NX-1a is exact rational arithmetic).
# Block [B]: RECORD-ONLY sanity scan (not load-bearing; the proof is
#   analytic + block [A]): direct sign check of x and its tau-derivative
#   on a 2001-point grid of [0.8, 1.074] at the numerics referee's 8
#   adversarial (w, m) points plus three corner cases.
from mpmath import mp
from fractions import Fraction

mp.dps = 50

allA = True
def chk(label, cond, detail):
    global allA
    allA = allA and bool(cond)
    print(f"  {label}: {detail} : {bool(cond)}")

print("[A] named-constant certificates (mpmath dps=50)")

# NX-1: cap on t/2 and the sin floor constant 0.96193, hence c = 1.9238
tmax = Fraction(1074, 1000) * Fraction(89, 100)        # tau_max * lam_max, exact
y0 = tmax / 2                                          # (t/2) cap = 0.47793, exact
chk("NX-1a", tmax == Fraction(95586, 100000) and y0 == Fraction(47793, 100000),
    f"1.074*0.89 = {float(tmax)} exactly, (t/2) cap y0 = {float(y0)} exactly (rational)")
y0m = mp.mpf(y0.numerator) / y0.denominator
floorv = 1 - y0m**2 / 6
chk("NX-1b", floorv >= mp.mpf('0.96193'),
    f"1 - y0^2/6 = {mp.nstr(floorv, 12)} >= 0.96193")
chk("NX-1c", 2 * mp.mpf('0.96193') >= mp.mpf('1.9238'),
    f"2*0.96193 = {mp.nstr(2*mp.mpf('0.96193'), 12)} >= c = 1.9238")

# NX-2: psi(0.8) floor, psi(tau) = c log(1+tau^2) - tau, c = 1.9238
psi08 = mp.mpf('1.9238') * mp.log(mp.mpf('1.64')) - mp.mpf('0.8')
chk("NX-2", psi08 >= mp.mpf('0.1516'),
    f"psi(0.8) = 1.9238*log(1.64) - 0.8 = {mp.nstr(psi08, 12)} >= 0.1516")

# NX-3: psi' floor via the endpoint minimum of 2tau/(1+tau^2) on [0.8, 1.074]
f08 = 2 * mp.mpf('0.8') / (1 + mp.mpf('0.8')**2)
f1074 = 2 * mp.mpf('1.074') / (1 + mp.mpf('1.074')**2)
chk("NX-3a", min(f08, f1074) >= mp.mpf('0.9756'),
    f"2tau/(1+tau^2): f(0.8) = {mp.nstr(f08, 10)}, f(1.074) = {mp.nstr(f1074, 10)}, "
    f"min = {mp.nstr(min(f08, f1074), 10)} >= 0.9756")
psip = mp.mpf('1.9238') * mp.mpf('0.9756') - 1
chk("NX-3b", psip >= mp.mpf('0.8768'),
    f"psi' >= 1.9238*0.9756 - 1 = {mp.nstr(psip, 10)} >= 0.8768")

# NX-4: global M floor at tau = 0.8, vs 1 and vs 1/log 2 (remark R2)
Mfloor = mp.mpf('1.9238') * mp.mpf('0.8')
il2 = 1 / mp.log(2)
chk("NX-4", Mfloor >= mp.mpf('1.539') and Mfloor > il2,
    f"c*0.8 = {mp.nstr(Mfloor, 10)} >= 1.539 > 1/log2 = {mp.nstr(il2, 10)}")

# NX-5: tau_0(lam)/lam at the extreme lam = 0.89 (its max over (0, 0.89] by Cor X.2)
tau0max = 2 * mp.asin(mp.sinh(mp.mpf('0.89') / 2)) / mp.mpf('0.89')
chk("NX-5", tau0max <= mp.mpf('1.0739'),
    f"tau0(0.89)/0.89 = {mp.nstr(tau0max, 12)} <= 1.0739 < 1.074")

# NX-6: arcsin domain for Cor X.2 -- sinh(0.445) < 1, incl. the elementary
# geometric-domination bound sinh(u) <= u/(1 - u^2/6) used in the text
geo = mp.mpf('0.445') / (1 - mp.mpf('0.445')**2 / 6)
sh = mp.sinh(mp.mpf('0.445'))
chk("NX-6", sh <= geo and geo <= mp.mpf('0.4602') and sh < 1,
    f"sinh(0.445) = {mp.nstr(sh, 10)} <= 0.445/(1-0.445^2/6) = {mp.nstr(geo, 10)} <= 0.4602 < 1")

print(f"[A] ALL PASS: {allA}")
print()

print("[B] record-only sanity scan (2001-pt grid of [0.8, 1.074] per case; dps=50)")

def xval(m, lam, tau):
    t = tau * lam
    h = mp.sin(t / 2)
    M = m * h
    s = h**2
    S = mp.sinh(lam / 2)**2
    return (M - 1) / (2 * M) * (mp.log(1 + s / S) - s / (S * M))

def gval(m, lam, tau):
    h = mp.sin(tau * lam / 2)
    S = mp.sinh(lam / 2)**2
    return mp.log(1 + h**2 / S) - h / (m * S)

cases = [  # referee_numerics_wave4_sl4p [A2]'s 8 adversarial (w, m) points:
    ('4.001', 401), ('4.05', 401), ('4.10', 401), ('4.30', 401),
    ('4.90', 401), ('5.0', 401), ('4.001', 462), ('4.05', 461),
    # corners of the THEOREM's full domain (w >= 4, lam <= 0.89):
    ('356.89', 401),    # lam = 0.89 exactly (full-tilt corner)
    ('4.0', 5),         # lam = 0.8, w = 4 boundary (M-floor nearly tight)
    ('5.0', 2000000),   # lam = 2.5e-6 (deep small-lam corner)
]
N = 2000
lo, hi = mp.mpf('0.8'), mp.mpf('1.074')
allB = True
for wstr, m in cases:
    w = mp.mpf(wstr)
    lam = w / m
    taus = [lo + (hi - lo) * i / N for i in range(N + 1)]
    vals = [xval(m, lam, u) for u in taus]
    gs = [gval(m, lam, u) for u in taus]
    incs = [vals[i + 1] - vals[i] for i in range(N)]
    dmin = min(mp.diff(lambda u: xval(m, lam, u), tt)
               for tt in [lo, mp.mpf('0.9'), mp.mpf('1.0'), hi])
    Mmin = m * mp.sin(lo * lam / 2)
    ok = (all(i > 0 for i in incs) and min(vals) > 0 and min(gs) > 0
          and dmin > 0 and Mmin > mp.mpf('1.539'))
    allB = allB and ok
    print(f"  w={wstr:>7} m={m:>7}: min inc = {mp.nstr(min(incs), 6)} > 0 | "
          f"min dx/dtau = {mp.nstr(dmin, 6)} > 0 | min x = {mp.nstr(min(vals), 6)} > 0 | "
          f"min g = {mp.nstr(min(gs), 6)} > 0 | M(0.8) = {mp.nstr(Mmin, 6)} > 1.539 : {ok}")
print(f"[B] ALL PASS: {allB}")
print()
print(f"OVERALL: {'PASS' if (allA and allB) else 'FAIL'}")
