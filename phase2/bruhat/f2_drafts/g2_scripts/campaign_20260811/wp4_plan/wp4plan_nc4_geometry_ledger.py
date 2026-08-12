#!/usr/bin/env python3
"""NC-PL4: final split geometry + stated-constant ledger.
Geometry: core [0, lam/2] (model, SL1); mid [lam/2, 0.8lam] (SL3(i), exp(-s2t^2/8));
W.6 on [0.8lam, t0]; W.5(ii) floor on [t0, pi].
(i) C5 at radius 0.5lam; (ii) min -log|phi|/(s2t^2) on [0.5,0.8]lam;
(iii) min W.6 exponent over [0.8lam, t0] (40-pt scan);
(iv) per-band stated ledger vs budget 20*c_A at m = 401.
"""
import mpmath as mp
mp.mp.dps = 30

def factor_stats(j, lam):
    q = mp.e**(-lam)
    ws = [q**i for i in range(j)]
    Z = mp.fsum(ws)
    m1 = mp.fsum([i*w for i, w in enumerate(ws)])/Z
    c2 = mp.fsum([(i-m1)**2*w for i, w in enumerate(ws)])/Z
    c3 = mp.fsum([(i-m1)**3*w for i, w in enumerate(ws)])/Z
    c4 = mp.fsum([(i-m1)**4*w for i, w in enumerate(ws)])/Z - 3*c2**2
    return m1, c2, c3, c4

def phi_log(m, lam, t, stats):
    tot = mp.mpc(0)
    z = mp.mpc(0, t) - lam
    q = mp.e**(-lam)
    for j in range(2, m+1):
        num = (1 - mp.e**(z*j))/(1 - mp.e**z)
        Z = (1 - q**j)/(1 - q)
        tot += mp.log(num/Z*mp.e**(mp.mpc(0, -t*stats[j][0])))
    return tot

def w6_exp(m, lam, t):
    M = m*mp.sin(t/2)
    s = mp.sin(t/2)**2
    S = mp.sinh(lam/2)**2
    return m*((M-1)/(2*M))*(mp.log(1+s/S) - s/(S*M)) if M > 1 else mp.mpf(0)

m = 401
print("(i)-(iii) at m=401:")
for w in ['4.05', '4.2', '5', '7', '356']:
    lam = mp.mpf(w)/m
    stats = {j: factor_stats(j, lam) for j in range(1, m+1)}
    s2 = mp.fsum(st[1] for st in stats.values())
    k3 = mp.fsum(st[2] for st in stats.values())
    k4 = mp.fsum(st[3] for st in stats.values())
    C5 = mp.mpf(0)
    for i in range(1, 11):
        t = mp.mpf('0.5')*lam*i/10
        resid = abs(phi_log(m, lam, t, stats) + s2*t**2/2 + mp.mpc(0, 1)*k3*t**3/6 - k4*t**4/24)
        C5 = max(C5, resid/(s2*t**5/lam**3))
    midmin = min(-mp.re(phi_log(m, lam, lam*(mp.mpf('0.5') + mp.mpf('0.3')*i/6), stats)) /
                 (s2*(lam*(mp.mpf('0.5') + mp.mpf('0.3')*i/6))**2) for i in range(7))
    t0 = 2*mp.asin(mp.sinh(lam/2))
    w6min = min(w6_exp(m, lam, mp.mpf('0.8')*lam + (t0 - mp.mpf('0.8')*lam)*i/39)
                for i in range(40)) if t0 > mp.mpf('0.8')*lam else mp.mpf('inf')
    print(f"  w={w:>6}: C5(0.5lam)={float(C5):7.4f}  mid[.5,.8]min={float(midmin):6.4f} "
          f" W6min[0.8lam,t0]={float(w6min):7.3f}  (t0/lam={float(t0/lam):5.3f})")

print("\n(iv) stated-constant ledger, m=401 (A = c_A*401):")
bands = [('(4,5]', '0.28', '1.0', '0.8'), ('(5,6]', '0.35', '1.2', '1.4'),
         ('(6,8]', '0.42', '1.5', '2.6'), ('(8,10]', '0.52', '1.7', '3.5'),
         ('(10,20]', '0.60', '2.0', '5.2'), ('(20,40]', '0.70', '2.1', '6.0'),
         ('(40,inf)', '0.80', '2.2', '6.6')]
print("band      c_A   A     k4/2  0.3R31^2  R5    I1u   I2u  slop  total  budget  OK")
for name, cA, R31, R42 in bands:
    cA, R31, R42 = mp.mpf(cA), mp.mpf(R31), mp.mpf(R42)
    A = cA*401
    C5 = mp.mpf(8) if name == '(40,inf)' else mp.mpf(3)
    R5 = mp.mpf('6.4')*C5/mp.sqrt(A)
    I1u = mp.mpf('3.19')*mp.sqrt(A)*mp.e**(-A/32)
    I2u, slop, far = mp.mpf('0.2'), mp.mpf(1), mp.mpf('0.01')
    tot = R42/2 + mp.mpf('0.3')*R31**2 + R5 + I1u + I2u + slop + far
    bud = 20*cA
    print(f"{name:9s} {float(cA):.2f} {float(A):6.1f} {float(R42/2):5.2f} {float(mp.mpf('0.3')*R31**2):7.2f} "
          f"{float(R5):6.2f} {float(I1u):5.2f} {float(I2u):5.2f} {float(slop):4.1f} "
          f"{float(tot):6.2f} {float(bud):6.1f}  {'PASS' if tot <= bud else 'FAIL'}")
