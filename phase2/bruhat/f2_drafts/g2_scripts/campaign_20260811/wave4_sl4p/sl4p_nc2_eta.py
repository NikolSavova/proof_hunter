#!/usr/bin/env python3
# sl4p_nc2_eta.py -- wave-4 SL4': evidence for the computed-eta pricing (SL4'-E),
#   |eta| <= [ R42*(W)/2 + 0.3 (R31*(W))^2 + lam^2/2 ] u ,
# across ALL bands at m = 401 (the orphan's Part A covered w = 4.5/7/30/200 only)
# and a scope check at m = 601.  Also: sign(kappa_4) > 0 at every point (the
# cancellation mechanism behind the 0.3 coefficient), and the leading-form
# residual in u^2-units.  Model machinery = orphan sl4_nc1.py Part A verbatim
# (Hermite closed forms; closed-vs-quad already verified there to 6.6e-31).
import mpmath as mp
mp.mp.dps = 30

def factor_cums(j, lam):
    ws = [mp.e**(-lam*i) for i in range(j)]
    Z = mp.fsum(ws)
    m1 = mp.fsum(i*w for i, w in enumerate(ws))/Z
    c2 = mp.fsum((i-m1)**2*w for i, w in enumerate(ws))/Z
    c3 = mp.fsum((i-m1)**3*w for i, w in enumerate(ws))/Z
    c4 = mp.fsum((i-m1)**4*w for i, w in enumerate(ws))/Z - 3*c2**2
    return m1, c2, c3, c4

def sum_cums(m, lam):
    mu = k2 = k3 = k4 = mp.mpf(0)
    for j in range(1, m+1):
        a, b, c, d = factor_cums(j, lam)
        mu += a; k2 += b; k3 += c; k4 += d
    return mu, k2, k3, k4

def He(n, x):
    if n == 3: return x**3 - 3*x
    if n == 4: return x**4 - 6*x**2 + 3
    if n == 6: return x**6 - 15*x**4 + 45*x**2 - 15

def qhat(d, s2, k3, k4):
    g = mp.e**(-d*d/(2*s2))/mp.sqrt(2*mp.pi*s2)
    z = d/mp.sqrt(s2)
    a = k3/(6*s2**mp.mpf('1.5')); b4 = k4/(24*s2**2); c6 = k3**2/(72*s2**3)
    return g*(1 + a*He(3, z) + b4*He(4, z) + c6*He(6, z))

def eta_of(s2, k3, k4):
    q0 = qhat(0, s2, k3, k4); qm = qhat(-1, s2, k3, k4); qp = qhat(1, s2, k3, k4)
    return s2*((q0*q0 - qm*qp)/(qm*qp)) - 1

BAND = lambda w: ('W1' if w<=5 else 'W2' if w<=6 else 'W3' if w<=8 else
                  'W4' if w<=10 else 'W5' if w<=20 else 'W6b' if w<=40 else 'W7')
R31S = {'W1':1.0,'W2':1.2,'W3':1.5,'W4':1.7,'W5':2.0,'W6b':2.1,'W7':2.2}
R42S = {'W1':0.8,'W2':1.4,'W3':2.6,'W4':3.5,'W5':5.2,'W6b':6.0,'W7':6.6}

def run(m, ws):
    print(f"== m = {m} ==")
    worst = -mp.inf; ok_all = True; k4pos = True
    for wstr in ws:
        w = mp.mpf(wstr); lam = w/m
        if lam > mp.mpf('0.89'):
            print(f"  w={wstr}: lam={float(lam):.5f} > 0.89 -- out of band, skipped"); continue
        mu, s2, k3, k4 = sum_cums(m, lam)
        A = lam*lam*s2; u = 1/A
        e = eta_of(s2, k3, k4)
        b = BAND(float(w))
        price = R42S[b]/2 + mp.mpf('0.3')*R31S[b]**2 + lam*lam/2
        lead = (s2*(mp.e**(1/s2)-1)-1) + k4/(2*s2**2) - k3**2/s2**3
        ratio = abs(e)/u/price
        worst = max(worst, ratio); ok_all = ok_all and (ratio <= 1); k4pos = k4pos and (k4 > 0)
        print(f"  w={wstr} [{b}]: |eta|/u={float(abs(e)/u):.4f}  price={float(price):.4f}"
              f"  ratio={float(ratio):.4f}  k4>0:{k4>0}"
              f"  ptwise(R42/2+0.3R31^2+lam^2/2)={float(k4*lam*lam/s2/2 + mp.mpf('0.3')*(abs(k3)*lam/s2)**2 + lam*lam/2):.4f}"
              f"  lead-resid/u^2={float(abs(e-lead)/u**2):.4f}")
    print(f"  ALL |eta| <= price*u: {ok_all};  worst ratio = {float(worst):.4f};  kappa_4 > 0 everywhere: {k4pos}")

run(401, ['4.05','4.5','4.9','5.5','7','9','15','30','60','100','200','356.8'])
run(601, ['4.05','7','60','300','534'])
