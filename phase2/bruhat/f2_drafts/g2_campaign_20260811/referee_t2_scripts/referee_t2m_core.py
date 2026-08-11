#!/usr/bin/env python3
"""Referee re-verification (independent), part 1: dictionary lemmas T.2-T.6 + findings.

Checks (each prints PASS/FAIL/FINDING with numbers):
  A. closed forms (2.2)-(2.5) vs direct truncated-geometric weight cumulants
  B. T.3 two-sided mean displacement, constants 1/38 and 1.05/36
  C. T.4 final two-sided deficit bound (0.0285/0.0300 form)
  D. FINDING check: T.4 side clause `deficit <= w^2/20 for all m>=2, |w|<=pi`
  E. T.4' kappa_3/kappa_4 bounds (w m^4/284, w^2 m^5/2200, m^5/155)
  F. T.5 variance lower bound (k/6)(1+k/m) at m=30,60 (all k), + mixture ineq spot
  G. T.6ii Gaussian domination, T.6iii-final 4th-order remainder
  H. FINDING check: T.8'' chain step E_geom U^2 <= (1+1/lam)^2, and the
     statement-level check Var_trunc <= min(j,1+1/lam)^2
  I. FINDING check: T.10(2) regime-gap demonstration (rho = 1-0.04 w0^2)
All stdlib floats; identities checked to tolerance, inequalities exactly.
"""
import math, cmath

# ---------- exact-ish per-factor machinery ----------
def weights(j, lam):
    return [math.exp(-lam*i) for i in range(j)]

def factor_cumulants(j, lam, order=6):
    """cumulants kappa_1..kappa_order of truncated geometric on {0..j-1}, weights e^{-lam i}."""
    w = weights(j, lam); Z = sum(w)
    raw = [sum(wi*(i**r) for i, wi in enumerate(w))/Z for r in range(order+1)]  # raw moments
    # moment->cumulant recursion: kappa_n = m_n - sum_{k=1}^{n-1} C(n-1,k-1) kappa_k m_{n-k}
    kap = [0.0]*(order+1)
    for n in range(1, order+1):
        s = raw[n]
        for k in range(1, n):
            s -= math.comb(n-1, k-1)*kap[k]*raw[n-k]
        kap[n] = s
    return kap

def g(u):
    if u > 30.0: return 1.0/u
    if abs(u) < 0.05: return 0.5 - u/12.0 + u**3/720.0 - u**5/30240.0 + u**7/1209600.0
    return 1.0/u - 1.0/math.expm1(u)
def gp(u):
    if u > 30.0: return -1.0/u**2
    if abs(u) < 0.05: return -1.0/12.0 + u*u/240.0 - u**4/6048.0 + u**6/172800.0
    E = math.exp(u); D = math.expm1(u)
    return -1.0/u**2 + E/D**2
def gpp(u):
    if u > 30.0: return 2.0/u**3
    if abs(u) < 0.05: return u/120.0 - u**3/1512.0 + u**5/28800.0
    E = math.exp(u); D = math.expm1(u)
    return 2.0/u**3 - E*(E+1.0)/D**3
def gppp(u):
    if u > 30.0: return -6.0/u**4
    if abs(u) < 0.05: return 1.0/120.0 - u*u/504.0 + u**4/5760.0 - u**6/95040.0
    E = math.exp(u); D = math.expm1(u)
    return -6.0/u**4 + E*(E*E + 4.0*E + 1.0)/D**4

def closed_forms(m, lam):
    """(2.2)-(2.5): mu, sigma^2, kappa3, kappa4 of X."""
    mu = sum(j*g(lam*j) - g(lam) for j in range(1, m+1))
    s2 = sum(gp(lam) - j*j*gp(lam*j) for j in range(1, m+1))
    k3 = sum(j**3*gpp(lam*j) - gpp(lam) for j in range(1, m+1))
    k4 = sum(gppp(lam) - j**4*gppp(lam*j) for j in range(1, m+1))
    return mu, s2, k3, k4

def X_cumulants_direct(m, lam, order=6):
    tot = [0.0]*(order+1)
    for j in range(1, m+1):
        kj = factor_cumulants(j, lam, order)
        for r in range(1, order+1):
            tot[r] += kj[r]
    return tot

def lam_of_k(m, k, lo=1e-12, hi=60.0):
    """solve mu(lam)=k for k <= N/2 (lam >= 0), bisection."""
    N = m*(m-1)//2
    assert 1 <= k <= N//2 + 1
    f = lambda l: sum(j*g(l*j) - g(l) for j in range(1, m+1)) - k
    a, b = lo, hi
    if f(a) < 0:  # mu(lo) approx N/2 >= k always for k <= N/2
        return 0.0
    for _ in range(200):
        mid = 0.5*(a+b)
        if f(mid) > 0: a = mid
        else: b = mid
    return 0.5*(a+b)

print("== A. closed forms (2.2)-(2.5) vs direct weight cumulants ==")
okA = True
for (m, lam) in [(8, 0.3), (8, 1.0), (12, 0.05), (30, 0.1)]:
    mu, s2, k3, k4 = closed_forms(m, lam)
    direct = X_cumulants_direct(m, lam)
    rel = lambda a, b: abs(a-b)/max(1.0, abs(b))
    errs = [rel(mu, direct[1]), rel(s2, direct[2]), rel(k3, direct[3]), rel(k4, direct[4])]
    ok = max(errs) < 1e-9
    okA &= ok
    print(f"  m={m} lam={lam}: rel errs mu,s2,k3,k4 = {errs[0]:.2e} {errs[1]:.2e} {errs[2]:.2e} {errs[3]:.2e} -> {'ok' if ok else 'MISMATCH'}")
# untilted limit vs Lemma 1.2 (use tiny lam):
m = 20; lam = 1e-8
mu, s2, k3, k4 = closed_forms(m, lam)
N = m*(m-1)//2; lamb = m*(m-1)*(2*m+5)/72.0
S4 = sum(j**4 for j in range(1, m+1))
print(f"  untilted limit m=20: mu-N/2={mu-N/2:.3e} s2-lambda={s2-lamb:.3e} k3={k3:.3e} k4+ (S4-m)/120={k4+(S4-m)/120.0:.3e}")
okA &= abs(mu-N/2) < 1e-4 and abs(s2-lamb) < 1e-4 and abs(k4+(S4-m)/120.0) < 1.0
print("A:", "PASS" if okA else "FAIL")

print("== B. T.3 mean displacement, (1/38) w m^2 <= N/2-mu <= (1.05/36) w m^2, 0<w<=1, m>=30 ==")
okB = True
for m in (30, 60, 120):
    N2 = m*(m-1)/4.0
    for w in (0.05, 0.1, 0.3, 0.5, 0.8, 1.0):
        lam = w/m
        mu, s2, k3, k4 = closed_forms(m, lam)
        disp = N2 - mu
        lo, hi = w*m*m/38.0, 1.05*w*m*m/36.0
        ok = lo <= disp <= hi
        okB &= ok
        if not ok or w in (0.3, 1.0):
            print(f"  m={m} w={w}: disp={disp:.4f} in [{lo:.4f},{hi:.4f}] {'ok' if ok else 'VIOLATION'}")
print("B:", "PASS" if okB else "FAIL")

print("== C. T.4 final: 0.0285 w^2(1-w^2/19) <= 1-s2/lambda <= 0.0300 w^2(1+3/m+w^2/18), m>=30, |w|<=pi ==")
okC = True
for m in (30, 60, 120):
    lamb = m*(m-1)*(2*m+5)/72.0
    for w in (0.1, 0.5, 1.0, 2.0, 3.0, math.pi):
        lam = w/m
        _, s2, _, _ = closed_forms(m, lam)
        d = 1.0 - s2/lamb
        lo = 0.0285*w*w*(1-w*w/19.0)
        hi = 0.0300*w*w*(1+3.0/m+w*w/18.0)
        ok = lo <= d <= hi
        okC &= ok
        if not ok or w in (1.0, math.pi):
            print(f"  m={m} w={w:.4f}: deficit={d:.6f} in [{lo:.6f},{hi:.6f}] {'ok' if ok else 'VIOLATION'}")
# crude clause s2 >= lambda/2 at w=pi, m>=30:
for m in (30, 53):
    lamb = m*(m-1)*(2*m+5)/72.0
    _, s2, _, _ = closed_forms(m, math.pi/m)
    print(f"  crude: m={m} w=pi: s2/lambda={s2/lamb:.4f} (need >= 0.5): {'ok' if s2 >= lamb/2 else 'VIOLATION'}")
print("C:", "PASS" if okC else "FAIL")

print("== D. FINDING: side clause `1-s2/lambda <= w^2/20 for ALL m>=2, |w|<=pi` ==")
worst = []
for m in (2, 3, 4, 5, 6, 8, 10):
    lamb = m*(m-1)*(2*m+5)/72.0
    bad = None
    for iw in range(1, 315):
        w = iw/100.0
        if w > math.pi: break
        lam = w/m
        _, s2, _, _ = closed_forms(m, lam)
        d = 1.0 - s2/lamb
        if d > w*w/20.0 + 1e-12:
            if bad is None or d - w*w/20.0 > bad[1]:
                bad = (w, d - w*w/20.0, d, w*w/20.0)
    if bad:
        print(f"  m={m}: VIOLATION worst at w={bad[0]}: deficit={bad[2]:.6f} > w^2/20={bad[3]:.6f} (excess {bad[1]:.6f})")
        worst.append(m)
    else:
        print(f"  m={m}: clause holds on the w-grid")
print("D:", "FINDING CONFIRMED (clause false at m in", worst, ")" if worst else "no violation found")

print("== E. T.4': |k3| <= |w| m^4/284; |k4 + S*4/120| <= w^2 m^5/2200; |k4| <= m^5/155 (m>=30,|w|<=pi) ==")
okE = True
for m in (30, 60):
    S4s = sum(j**4 for j in range(2, m+1)) - (m-1)  # S*_4 = sum_{j=1}^m j^4 - m
    S4s = sum(j**4 for j in range(1, m+1)) - m
    r3max = r4max = r4abs = 0.0
    for w in (0.1, 0.5, 1.0, 2.0, 3.0, math.pi):
        lam = w/m
        _, _, k3, k4 = closed_forms(m, lam)
        r3 = abs(k3)/(w*m**4/284.0)
        r4 = abs(k4 + S4s/120.0)/(w*w*m**5/2200.0)
        ra = abs(k4)/(m**5/155.0)
        r3max, r4max, r4abs = max(r3max, r3), max(r4max, r4), max(r4abs, ra)
    ok = r3max <= 1 and r4max <= 1 and r4abs <= 1
    okE &= ok
    print(f"  m={m}: max ratios k3={r3max:.4f} recentred k4={r4max:.4f} abs k4={r4abs:.4f} -> {'ok' if ok else 'VIOLATION'}")
print("E:", "PASS" if okE else "FAIL")

print("== F. T.5: s2 >= (k/6)(1+k/m) for all interior k<=N/2 (m=30,60) ==")
okF = True
for m in (30, 60):
    N = m*(m-1)//2
    ratios = []
    for k in range(1, N//2 + 1):
        lam = lam_of_k(m, k)
        _, s2, _, _ = closed_forms(m, max(lam, 1e-12))
        bound = (k/6.0)*(1+k/m)
        ratios.append(s2/bound)
    okF &= min(ratios) >= 1.0
    print(f"  m={m}: min s2/[(k/6)(1+k/m)] = {min(ratios):.4f} (draft: 2.6376/2.6455)")
# mixture inequality (**) spot: adversarial nonincreasing weight vectors
import random
random.seed(7)
okmix = True
for trial in range(500):
    j = random.randint(2, 12)
    steps = sorted([random.random() for _ in range(j)], reverse=True)
    Z = sum(steps); p = [s/Z for s in steps]
    EU = sum(i*pi for i, pi in enumerate(p)); EU2 = sum(i*i*pi for i, pi in enumerate(p))
    var = EU2 - EU*EU
    if var < EU*EU/3.0 + EU/3.0 - 1e-12: okmix = False
print(f"  mixture ineq (**) on 500 random nonincreasing laws: {'holds' if okmix else 'VIOLATION'}")
print("F:", "PASS" if (okF and okmix) else "FAIL")

print("== G. T.6ii and T.6iii-final ==")
def phi_lam(m, lam, t):
    """centered tilted cf"""
    tot = 0.0 + 0.0j
    mu = 0.0
    val = 1.0 + 0.0j
    for j in range(1, m+1):
        w = weights(j, lam); Z = sum(w)
        mu_j = sum(i*wi for i, wi in enumerate(w))/Z
        mu += mu_j
        val *= sum(wi*cmath.exp(1j*t*i) for i, wi in enumerate(w))/Z
    return val*cmath.exp(-1j*t*mu)
okG = True
for (m, lam) in [(30, 0.001), (30, 0.1), (30, 0.5), (12, 1.5)]:
    _, s2, k3, _ = closed_forms(m, lam)
    bad2 = 0.0
    for it in range(1, 101):
        t = it/100.0*math.pi/m
        r = abs(phi_lam(m, lam, t))/math.exp(-s2*t*t/5.0)
        bad2 = max(bad2, r)
    okG &= bad2 <= 1.0 + 1e-12
    print(f"  T.6ii m={m} lam={lam}: max |phi|/exp(-s2 t^2/5) on (0,pi/m] = {bad2:.6f}")
for (m, lam) in [(30, 0.05), (30, 0.001)]:
    _, s2, k3, _ = closed_forms(m, lam)
    badr = 0.0
    for it in range(1, 51):
        t = it/50.0/(2*m)
        lp = cmath.log(phi_lam(m, lam, t))
        resid = abs(lp + s2*t*t/2.0 + 1j*k3*t**3/6.0)
        badr = max(badr, resid/((m-1)**2*s2*t**4/6.0))
    okG &= badr <= 1.0
    print(f"  T.6iii m={m} lam={lam}: max resid/[(m-1)^2 s2 t^4/6] on (0,1/(2m)] = {badr:.4f}")
print("G:", "PASS" if okG else "FAIL")

print("== H. FINDING: T.8'' chain -- E_geom U^2 <= (1+1/lam)^2 ?  and statement Var<=min(j,1+1/lam)^2 ==")
for lam in (0.05, 0.1, 0.2, 0.5):
    q = math.exp(-lam)
    EU2 = q*(1+q)/(1-q)**2
    claim = (1+1/lam)**2
    tag = "ok" if EU2 <= claim else "VIOLATION (chain step false)"
    print(f"  lam={lam}: E_geom U^2 = {EU2:.2f} vs (1+1/lam)^2 = {claim:.2f}: {tag}")
# statement level: Var_trunc <= min(j, 1+1/lam)^2 ? and <= 2*min(...)^2 ?
viol1 = viol2 = 0; worstr = 0.0
for j in (2, 3, 5, 10, 20, 50, 100):
    for lam in (0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0):
        kj = factor_cumulants(j, lam, 2)
        var = kj[2]
        b = min(j, 1+1/lam)**2
        worstr = max(worstr, var/b)
        if var > b: viol1 += 1
        if var > 2*b: viol2 += 1
print(f"  statement check: max Var/min(j,1+1/lam)^2 = {worstr:.4f}; violations of stated bound: {viol1}, of 2x bound: {viol2}")
print("H: FINDING -- chain step is false; statement itself", "survives numerically" if viol1 == 0 else "ALSO FALSE")

print("== I. FINDING: T.10(2) with rho=1-0.04 w0^2 leaves a gap (claimed 'overlap') ==")
m, w0 = 200, 1.0
lamb = m*(m-1)*(2*m+5)/72.0
rho = 1 - 0.04*w0*w0
for w in (1.02, 1.05, 1.09):
    lam = w/m
    _, s2, _, _ = closed_forms(m, lam)
    in_refined = (w <= w0)
    in_crude = (s2 <= rho*lamb)
    print(f"  m={m} w={w}: deficit={1-s2/lamb:.6f} (1-rho={1-rho}); in refined regime: {in_refined}; in crude regime: {in_crude}"
          + ("   <-- IN NEITHER REGIME" if not (in_refined or in_crude) else ""))
print("I: FINDING CONFIRMED if any row shows 'IN NEITHER REGIME'")
