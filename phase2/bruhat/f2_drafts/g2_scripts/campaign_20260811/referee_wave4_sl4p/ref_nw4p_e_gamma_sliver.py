#!/usr/bin/env python3
# ref_nw4p_e_gamma_sliver.py -- adversarial numerics referee, wave4_sl4p.
# THE HYPOTHESIS/CERTIFICATION MISMATCH probe.  Theorem SL4' (SS4) assumes
# SL3'-w of SS3, whose displayed levels are gamma* >= 0.25/0.25/0.20/0.15
# (W1..W4).  But the certified ledger (block [1]) and the sliver boundary
# w_dagger(m) (block [2]) were computed at the DEFAULT gamma* =
# 0.42/0.42/0.40/0.40, and block [4]'s 'W1 accepts gamma* = 0.25' was
# evaluated at w = 4.30 only -- NOT on the sliver edge, where the W.6
# crossover entry is ~9x larger.  Under the STATED hypothesis (0.25), the
# W1 row near w = 4.10 changes.  Quantify:
#  [E1] row(W1, 401, w) at gamma* = 0.25 for w = 4.095..4.30;
#  [E2] w_dagger(401) under gamma* = 0.25 / 0.30 / 0.35 / 0.42;
#  [E3] full-band closure m at w -> 4+ under gamma* = 0.25;
#  [E4] same probe for the SL1'-w REMARK 'W1 accepts C5* up to 0.4':
#       row(W1, 401, w = 4.10, C5 = 0.4).
#  [E5] W2-W4 at their weakened gammas (w-independent rows): certified?
import mpmath as mp
mp.mp.dps = 40
SQ2PI = mp.sqrt(2*mp.pi); KMID = SQ2PI/mp.pi
INFL = mp.mpf('1.10'); QUADF = mp.mpf('0.09')
FAR = mp.mpf('0.0741'); C1T = mp.mpf('0.1317'); C2T = mp.mpf('0.0871')

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

def w1row(m, w, g, C5=mp.mpf('0.05')):
    cAd = mp.mpf('0.28'); A0 = cAd*m
    main = mp.mpf('0.8')/2 + mp.mpf('0.3') + (mp.mpf(5)/m)**2/2
    R5n = 48*SQ2PI/mp.pi*C5*efac(C5)/mp.sqrt(A0); R5d = R5n/6
    cube = mp.mpf('2.37')/mp.sqrt(A0)
    cross = (mp.mpf('2.13')*mp.mpf('0.8')+mp.mpf('0.56')*mp.mpf('0.64'))/mp.sqrt(A0)
    midn = KMID*A0**mp.mpf('1.5')/(4*g)*mp.e**(-g*A0/4)*(1+2/(g*A0))
    midd = KMID*mp.sqrt(A0)/g*mp.e**(-g*A0/4)
    dec = main + INFL*(R5n+cube+cross+midn+R5d+midd)
    Xn, Xd = X_w6(w, m, mp.mpf(m))
    lamL = mp.mpf(4)/m; s2max = m/(4*mp.sinh(lamL/2)**2)
    Fn = 2*SQ2PI*m*s2max**mp.mpf('1.5')*mp.e**(-FAR*m)
    Fd = m*mp.sqrt(2*mp.pi*s2max)*mp.e**(-FAR*m)
    share = dec/(20*cAd) + (INFL*(Xn+Xd)+INFL*(Fn+Fd))/20
    return share*(1+QUADF)

print("== [E1] W1 row at m = 401 under STATED SL3'-w gamma* = 0.25 (vs certified-at-0.42) ==")
for wstr in ['4.095','4.10','4.12','4.14','4.16','4.18','4.20','4.25','4.30']:
    t25 = w1row(401, wstr, mp.mpf('0.25'))
    t42 = w1row(401, wstr, mp.mpf('0.42'))
    print(f"  w={wstr}: row(g=0.25)={float(t25):.4f} {'PASS' if t25<=1 else 'FAIL'}   "
          f"row(g=0.42)={float(t42):.4f} {'PASS' if t42<=1 else 'FAIL'}")

print("\n== [E2] w_dagger(401) as a function of the assumed gamma* (w step 0.005) ==")
for gs in ['0.25','0.30','0.35','0.42']:
    g = mp.mpf(gs); wd = None
    for i in range(0, 201):
        w = mp.mpf(4)+i*mp.mpf('0.005')
        if w1row(401, w, g) <= 1: wd = w; break
    print(f"  gamma* = {gs}: w_dagger(401) = {float(wd) if wd else '> 5.00'}")

print("\n== [E3] full-band closure m at w -> 4+ under gamma* = 0.25 (vs 463 at 0.42) ==")
first = None
for m in range(455, 545):
    if w1row(m, mp.mpf('4.0'), mp.mpf('0.25')) <= 1: first = m; break
print(f"  first m with row(m, 4.0; g=0.25) <= 1: {first}")

print("\n== [E4] SL1'-w remark probe: 'W1 accepts C5* up to 0.4' at the sliver edge ==")
for (wstr, c5) in [('4.10','0.05'),('4.10','0.4'),('4.30','0.4'),('4.30','0.05')]:
    t = w1row(401, wstr, mp.mpf('0.42'), C5=mp.mpf(c5))
    print(f"  w={wstr}, C5*={c5}: row = {float(t):.4f} {'PASS' if t<=1 else 'FAIL'}")

print("\n== [E5] W2-W4 at weakened gammas (w-independent rows), m = 401 and m-monotone spot ==")
BANDS234 = [('W2',5,6,'1.2','1.4','0.35','0.06'),('W3',6,8,'1.5','2.6','0.42','0.08'),
            ('W4',8,10,'1.7','3.5','0.52','0.10')]
GAM = {'W2':'0.25','W3':'0.20','W4':'0.15'}
for (name,wlo,whi,R31,R42,cA,C5) in BANDS234:
    R31=mp.mpf(R31); R42=mp.mpf(R42); cAd=mp.mpf(cA); C5=mp.mpf(C5); g=mp.mpf(GAM[name])
    for m in (401, 500, 1000):
        A0 = cAd*m
        main = R42/2 + mp.mpf('0.3')*R31**2 + (mp.mpf(whi)/m)**2/2
        R5n = 48*SQ2PI/mp.pi*C5*efac(C5)/mp.sqrt(A0); R5d = R5n/6
        cube = mp.mpf('2.37')*R31**3/mp.sqrt(A0)
        cross = (mp.mpf('2.13')*R31*R42+mp.mpf('0.56')*R42**2)/mp.sqrt(A0)
        midn = KMID*A0**mp.mpf('1.5')/(4*g)*mp.e**(-g*A0/4)*(1+2/(g*A0))
        midd = KMID*mp.sqrt(A0)/g*mp.e**(-g*A0/4)
        Xn = KMID*A0**mp.mpf('1.5')*(mp.mpf('0.8')/(2*C2T))*mp.e**(-mp.mpf('0.64')*C2T*A0)\
             *(1+1/(mp.mpf('1.28')*C2T*A0))
        Xd = KMID*mp.sqrt(A0)/(mp.mpf('0.8')*C2T)*mp.e**(-mp.mpf('0.64')*C2T*A0)
        dec = main + INFL*(R5n+cube+cross+midn+R5d+midd) + INFL*(Xn+Xd)
        lamL = mp.mpf(wlo)/m; s2max = m/(4*mp.sinh(lamL/2)**2)
        Fn = 2*SQ2PI*m*s2max**mp.mpf('1.5')*mp.e**(-FAR*m)
        Fd = m*mp.sqrt(2*mp.pi*s2max)*mp.e**(-FAR*m)
        tot = (dec/(20*cAd) + INFL*(Fn+Fd)/20)*(1+QUADF)
        print(f"  {name} g={GAM[name]} m={m}: tot = {float(tot):.4f} {'PASS' if tot<=1 else 'FAIL'}")
