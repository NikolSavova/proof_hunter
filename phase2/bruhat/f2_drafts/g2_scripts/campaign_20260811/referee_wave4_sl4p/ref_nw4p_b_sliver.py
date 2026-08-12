#!/usr/bin/env python3
# ref_nw4p_b_sliver.py -- adversarial numerics referee, wave4_sl4p.
# Attacks the SS5 sliver quantification and the m-/w-monotonicity claims that
# the draft's Theorem SL4' silently relies on:
#  [B1] w_dagger(m) for EVERY integer m in [401, 480] (draft sampled 10 m's);
#       nonincreasing-in-m check of the boundary.
#  [B2] full fine w-scan at m = 401 (step 0.001 on [4.0, 5.0]): verifies
#       PASS is a one-crossing property in w (no re-failure above w_dagger)
#       and pins w_dagger(401) to 3 decimals (draft: 4.10 from a 0.01 grid).
#  [B3] the w -> 4+ closure for m >= 462: the draft's SS8 trapezoid claim
#       'm in [401, 461]' needs row(m, w->4+) PASS for all m >= 462; the
#       prover only checked w = 4.001.  Probe w = 4.0000001 for m = 462..500.
#  [B4] m-monotonicity of all seven shares on the FULL integer grid
#       m = 401..600 plus 600..2000 step 50 (draft block [3] used 5 points).
import mpmath as mp
mp.mp.dps = 40
SQ2PI = mp.sqrt(2*mp.pi); KMID = SQ2PI/mp.pi
INFL = mp.mpf('1.10'); QUADF = mp.mpf('0.09')
FAR = mp.mpf('0.0741'); C1T = mp.mpf('0.1317'); C2T = mp.mpf('0.0871')
BANDS = [
 ('W1', 4, 5,   '1.0','0.8','0.28','0.05','0.42'),
 ('W2', 5, 6,   '1.2','1.4','0.35','0.06','0.42'),
 ('W3', 6, 8,   '1.5','2.6','0.42','0.08','0.40'),
 ('W4', 8, 10,  '1.7','3.5','0.52','0.10','0.40'),
 ('W5', 10, 20, '2.0','5.2','0.60','0.15','PROVED'),
 ('W6b',20, 40, '2.1','6.0','0.70','0.25','PROVED'),
 ('W7', 40, 0,  '2.2','6.6','0.85','0.80','PROVED')]

def efac(C5): return (mp.mpf('0.5')/(mp.mpf('0.5')-mp.mpf(C5)/8))**4

def w6_x(w, tau, m):
    lam = mp.mpf(w)/m; t = tau*lam
    M = m*mp.sin(t/2); s = mp.sin(t/2)**2; S = mp.sinh(lam/2)**2
    if M <= 1: return mp.mpf(0)
    return max((M-1)/(2*M)*(mp.log(1+s/S) - s/(S*M)), mp.mpf(0))

def X_w6(w, m, A):
    lam = mp.mpf(w)/m; tau0 = 2*mp.asin(mp.sinh(lam/2))/lam
    n = 60; h = (tau0-mp.mpf('0.8'))/n
    totn = totd = mp.mpf(0)
    for i in range(n):
        a = mp.mpf('0.8')+i*h; E = m*w6_x(w, a, m)
        totn += h*lam*((a+h)*lam)**2*mp.e**(-E)
        totd += h*lam*mp.e**(-E)
    s2 = A/lam**2
    return A*SQ2PI/mp.pi*s2**mp.mpf('1.5')*totn, A*SQ2PI/mp.pi*mp.sqrt(s2)*totd

def row(b, m, wX=mp.mpf('4.3')):
    name,wlo,whi,R31,R42,cAd,C5,gam = b
    R31=mp.mpf(R31); R42=mp.mpf(R42); cAd=mp.mpf(cAd); C5=mp.mpf(C5)
    A0 = cAd*m
    lammax = mp.mpf('0.89') if name=='W7' else mp.mpf(whi)/m
    main = R42/2 + mp.mpf('0.3')*R31**2 + lammax**2/2
    g = C1T if gam=='PROVED' else mp.mpf(gam)
    ent = lambda: (48*SQ2PI/mp.pi*C5*efac(C5)/mp.sqrt(A0),
                   8*SQ2PI/mp.pi*C5*efac(C5)/mp.sqrt(A0))
    R5n, R5d = ent()
    cube = mp.mpf('2.37')*R31**3/mp.sqrt(A0)
    cross = (mp.mpf('2.13')*R31*R42+mp.mpf('0.56')*R42**2)/mp.sqrt(A0)
    midn = KMID*A0**mp.mpf('1.5')/(4*g)*mp.e**(-g*A0/4)*(1+2/(g*A0))
    midd = KMID*mp.sqrt(A0)/g*mp.e**(-g*A0/4)
    dec = main + INFL*(R5n+cube+cross+midn+R5d+midd)
    if name=='W1':
        Xn, Xd = X_w6(wX, m, mp.mpf(m)); inc_X = INFL*(Xn+Xd); dec_X = mp.mpf(0)
    else:
        Xn = KMID*A0**mp.mpf('1.5')*(mp.mpf('0.8')/(2*C2T))*mp.e**(-mp.mpf('0.64')*C2T*A0)\
             *(1+1/(mp.mpf('1.28')*C2T*A0))
        Xd = KMID*mp.sqrt(A0)/(mp.mpf('0.8')*C2T)*mp.e**(-mp.mpf('0.64')*C2T*A0)
        dec_X = INFL*(Xn+Xd); inc_X = mp.mpf(0)
    lamL = mp.mpf(wlo)/m; s2max = m/(4*mp.sinh(lamL/2)**2)
    Fn = 2*SQ2PI*m*s2max**mp.mpf('1.5')*mp.e**(-FAR*m)
    Fd = m*mp.sqrt(2*mp.pi*s2max)*mp.e**(-FAR*m)
    share = (dec+dec_X)/(20*cAd) + (inc_X+INFL*(Fn+Fd))/20
    return share*(1+QUADF)

print("== [B1] w_dagger(m) on the FULL integer grid m = 401..480 (w step 0.01, scan to 5.00, re-failure check) ==")
prev = None; mono_ok = True; refail = 0
for m in range(401, 481):
    wdag = None; failed_after = False
    for i in range(0, 101):
        w = mp.mpf(4)+mp.mpf(i)/100
        tot = row(BANDS[0], m, wX=w)
        if tot <= 1 and wdag is None: wdag = w
        if tot > 1 and wdag is not None: failed_after = True
    if failed_after: refail += 1
    if prev is not None and wdag > prev: mono_ok = False
    prev = wdag
    if m <= 410 or m % 10 == 0 or failed_after:
        print(f"  m={m}: w_dagger={float(wdag):.2f}  refail-above: {failed_after}")
print(f"  w_dagger nonincreasing over m=401..480: {mono_ok};  rows with re-failure above w_dagger: {refail}")

print("\n== [B2] fine w-scan, m = 401, step 0.001 ==")
wd = None; refail = False; last_fail = None
for i in range(0, 1001):
    w = mp.mpf(4)+mp.mpf(i)/1000
    tot = row(BANDS[0], 401, wX=w)
    if tot <= 1 and wd is None: wd = w
    if tot > 1:
        last_fail = w
        if wd is not None: refail = True
print(f"  w_dagger(401) to 3 dp = {float(wd)};  last failing w = {float(last_fail)};  re-failure above: {refail}")
print(f"  row(401, 4.099) = {float(row(BANDS[0],401,wX=mp.mpf('4.099'))):.4f}  "
      f"row(401, 4.100) = {float(row(BANDS[0],401,wX=mp.mpf('4.100'))):.4f}")

print("\n== [B3] w -> 4+ closure for m >= 462 (probe w = 4.0000001; draft checked only w = 4.001) ==")
bad = []
for m in range(462, 501):
    tot = row(BANDS[0], m, wX=mp.mpf('4.0000001'))
    if tot > 1: bad.append((m, float(tot)))
print(f"  m in [462, 500] at w = 4.0000001: failures = {bad if bad else 'NONE'}")
for m in (462, 465, 470, 480):
    t1 = row(BANDS[0], m, wX=mp.mpf('4.0000001'))
    t2 = row(BANDS[0], m, wX=mp.mpf('4.001'))
    print(f"  m={m}: row(4.0000001)={float(t1):.4f}  row(4.001)={float(t2):.4f}")
t461 = row(BANDS[0], 461, wX=mp.mpf('4.0000001'))
print(f"  control m=461: row(4.0000001) = {float(t461):.4f} (expected FAIL > 1: {t461 > 1})")

print("\n== [B4] m-monotonicity, full integer grid 401..600 + 600..2000/50 (W1 at w = 4.3) ==")
for b in BANDS:
    ms = list(range(401, 601)) + list(range(650, 2001, 50))
    prev = None; viol = []
    for m in ms:
        v = row(b, m)
        if prev is not None and v > prev*(1+mp.mpf('1e-30')): viol.append(m)
        prev = v
    print(f"  {b[0]:3s}: violations of nonincreasing-in-m: {len(viol)}{'' if not viol else ' at '+str(viol[:5])}")
