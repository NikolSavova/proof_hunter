#!/usr/bin/env python3
"""NC-SL5-2: measurement-side consistency checks for SL5 (floats/mpmath — NOT
proof-bearing; the proof-bearing arithmetic is sl5_nc1_ledger_exact.py).

(a) Lemma SL5.0 truth: A/m <= h(lam) := (lam/2)^2/sinh^2(lam/2) < 1 pointwise
    on a dense grid of the residual band (m in {401, 1000, 1581}), and the
    closed-form Var(U_j^lam) = q/(1-q)^2 - j^2 q^j/(1-q^j)^2 cross-checked
    against direct summation.
(b) NC-PL1 budget-column consistency: per band, min over a dense w-grid of the
    TRUE 20*A/min(m,s2) at m = 401, vs the stated budget 20*c_A (must sit
    uniformly above; architect quoted 6.378..19.36).
(c) Far-entry honesty record: the architect's fallback cap A <= 0.024 m^3
    (B.0(i)) does NOT certify the 0.01/0.05 far entry at m = 401 (value ~221,
    first <= 0.05 only at m ~ 692); the printed '0.36*62*3850*3.2e-7 = 0.028'
    corresponds to A <= 0.024 m^2 (a slip). The SL5.0 route A <= m gives
    9.2e-4 at m = 401. This is the recorded reason SL5 replaces the fallback.
"""
import mpmath as mp
mp.mp.dps = 30

def var_trunc(j, lam):
    q = mp.e ** (-lam)
    return q / (1 - q) ** 2 - j ** 2 * q ** j / (1 - q ** j) ** 2 if j > 1 else mp.mpf(0)

def var_direct(j, lam):
    q = mp.e ** (-lam)
    ws = [q ** i for i in range(j)]
    Z = mp.fsum(ws)
    m1 = mp.fsum(i * w for i, w in enumerate(ws)) / Z
    return mp.fsum((i - m1) ** 2 * w for i, w in enumerate(ws)) / Z

def s2_of(m, lam):
    return mp.fsum(var_trunc(j, lam) for j in range(2, m + 1))

print("(a) closed-form Var vs direct summation (max abs rel diff):")
worst = mp.mpf(0)
for j in (2, 3, 7, 40, 173):
    for lam in ('0.011', '0.1', '0.5', '0.89'):
        a, b = var_trunc(j, mp.mpf(lam)), var_direct(j, mp.mpf(lam))
        worst = max(worst, abs(a - b) / b)
print(f"    {float(worst):.3e}   (identity confirmed to working precision)")

print("(a) A/m vs h(lam) = (lam/2)^2/sinh^2(lam/2), dense band grid:")
viol = 0
maxratio = mp.mpf(0)
maxAm = mp.mpf(0)
for m in (401, 1000, 1581):
    for i in range(1, 241):
        lam = mp.mpf('4.001') / m + (mp.mpf('0.89') - mp.mpf('4.001') / m) * i / 240
        A_over_m = lam ** 2 * s2_of(m, lam) / m
        h = (lam / 2) ** 2 / mp.sinh(lam / 2) ** 2
        maxAm = max(maxAm, A_over_m)
        maxratio = max(maxratio, A_over_m / h)
        if A_over_m > h:
            viol += 1
print(f"    violations of A/m <= h(lam): {viol} / 720 pts ; max A/(m h(lam)) = {float(maxratio):.4f} ; max A/m = {float(maxAm):.4f} < 1")

print("(b) true budget column min over dense w-grid, per band, m=401 (vs 20 c_A):")
bands = [("(4,5]", 4, 5, 0.28), ("(5,6]", 5, 6, 0.35), ("(6,8]", 6, 8, 0.42),
         ("(8,10]", 8, 10, 0.52), ("(10,20]", 10, 20, 0.60),
         ("(20,40]", 20, 40, 0.70), ("(40,inf)", 40, 401 * 0.89, 0.80)]
m = 401
for name, wlo, whi, cA in bands:
    best = mp.mpf('inf')
    for i in range(1, 161):
        w = mp.mpf(wlo) + (mp.mpf(whi) - mp.mpf(wlo)) * i / 160
        lam = w / m
        s2 = s2_of(m, lam)
        A = lam ** 2 * s2
        best = min(best, 20 * A / min(m, s2))
    ok = best >= 20 * cA
    print(f"    {name:9s} min 20A/min(m,s2) = {float(best):7.3f}  vs 20c_A = {20*cA:5.1f}   {'consistent' if ok else 'VIOLATION'}")

print("(c) far-entry honesty record at m=401 (exp(-0.0373*401) = %.4e):" % mp.e ** (-mp.mpf('0.0373') * 401))
A3 = mp.mpf('0.024') * 401 ** 3
print(f"    with A = 0.024 m^3 (B.0(i) fallback): 0.36 sqrt(A) A e^-0.0373m = {float(mp.mpf('0.36')*mp.sqrt(A3)*A3*mp.e**(-mp.mpf('0.0373')*401)):.1f}  (FAILS 0.05)")
A2 = mp.mpf('0.024') * 401 ** 2
print(f"    with A = 0.024 m^2 (the slip):        value = {float(mp.mpf('0.36')*mp.sqrt(A2)*A2*mp.e**(-mp.mpf('0.0373')*401)):.4f}")
for mm in range(401, 1000):
    v = mp.mpf('0.36') * (mp.mpf('0.024') * mm ** 3) ** mp.mpf('1.5') * mp.e ** (-mp.mpf('0.0373') * mm)
    if v <= mp.mpf('0.05'):
        print(f"    fallback route first reaches <= 0.05 at m = {mm} (gap [401, {mm-1}] uncovered by it)")
        break
print(f"    with A <= m (Lemma SL5.0):            value = {float(mp.mpf('0.36')*401**mp.mpf('1.5')*mp.e**(-mp.mpf('0.0373')*401)):.3e}  (<= 0.01 with 10x room)")
