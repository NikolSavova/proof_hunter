#!/usr/bin/env python3
# ref_nw4p_a_rebuild.py -- adversarial numerics referee, wave4_sl4p.
# INDEPENDENT rebuild of the seven ledger rows of wave4_sl4p_20260812.md SS4
# at dps 60, written from the DRAFT TEXT's closed forms (not from the prover's
# script), with: (a) 6-decimal share values vs the quoted 4-decimal ones;
# (b) the W1 crossover integral recomputed at n = 60 (draft) AND n = 6000
# (fine), with a full monotonicity audit of the W.6 exponent on the fine grid;
# (c) exact closed forms for E|He3|, E|He4| (antiderivative -He_{n-1} phi)
# replacing the prover's mp.quad; (d) the efac 'iff' boundary solved exactly;
# (e) A-monotonicity thresholds for every dec-bucket entry on the actual
# [c_A m, m] ranges (attacking the 'A >= 32' claim in Lemma SL4'.8's proof).
import mpmath as mp
mp.mp.dps = 60
SQ2PI = mp.sqrt(2*mp.pi)
KMID = SQ2PI/mp.pi
INFL = mp.mpf('1.10'); QUADF = mp.mpf('0.09')
FAR = mp.mpf('0.0741'); C1T = mp.mpf('0.1317'); C2T = mp.mpf('0.0871')

BANDS = [
 ('W1', 4, 5,   '1.0','0.8','0.28','0.05','0.42'),
 ('W2', 5, 6,   '1.2','1.4','0.35','0.06','0.42'),
 ('W3', 6, 8,   '1.5','2.6','0.42','0.08','0.40'),
 ('W4', 8, 10,  '1.7','3.5','0.52','0.10','0.40'),
 ('W5', 10, 20, '2.0','5.2','0.60','0.15','PROVED'),
 ('W6b',20, 40, '2.1','6.0','0.70','0.25','PROVED'),
 ('W7', 40, 0,  '2.2','6.6','0.85','0.80','PROVED')]   # W7 c_Adag = 0.85

def efac(C5): return (mp.mpf('0.5')/(mp.mpf('0.5')-mp.mpf(C5)/8))**4

def w6_x(w, tau, m):
    lam = mp.mpf(w)/m; t = tau*lam
    M = m*mp.sin(t/2); s = mp.sin(t/2)**2; S = mp.sinh(lam/2)**2
    if M <= 1: return mp.mpf(0)
    return max((M-1)/(2*M)*(mp.log(1+s/S) - s/(S*M)), mp.mpf(0))

def X_w6(w, m, A, n):
    """Left-endpoint-exponent upper Riemann sum, right-endpoint t^2 weight.
    Returns (Xn, Xd, #monotonicity violations on this grid, min increment)."""
    lam = mp.mpf(w)/m; tau0 = 2*mp.asin(mp.sinh(lam/2))/lam
    h = (tau0-mp.mpf('0.8'))/n
    totn = totd = mp.mpf(0); viol = 0; mininc = mp.inf; prev = None
    for i in range(n):
        a = mp.mpf('0.8')+i*h; E = m*w6_x(w, a, m)
        if prev is not None:
            inc = E - prev
            if inc < 0: viol += 1
            mininc = min(mininc, inc)
        prev = E
        totn += h*lam*((a+h)*lam)**2*mp.e**(-E)
        totd += h*lam*mp.e**(-E)
    s2 = A/lam**2
    return (A*SQ2PI/mp.pi*s2**mp.mpf('1.5')*totn,
            A*SQ2PI/mp.pi*mp.sqrt(s2)*totd, viol, mininc)

def row(b, m, wX=mp.mpf('4.3'), nX=60):
    name,wlo,whi,R31,R42,cAd,C5,gam = b
    R31=mp.mpf(R31); R42=mp.mpf(R42); cAd=mp.mpf(cAd); C5=mp.mpf(C5)
    A0 = cAd*m
    lammax = mp.mpf('0.89') if name=='W7' else mp.mpf(whi)/m
    main = R42/2 + mp.mpf('0.3')*R31**2 + lammax**2/2
    g = C1T if gam=='PROVED' else mp.mpf(gam)
    R5n = 48*SQ2PI/mp.pi*C5*efac(C5)/mp.sqrt(A0)
    R5d = 8*SQ2PI/mp.pi*C5*efac(C5)/mp.sqrt(A0)
    cube = mp.mpf('2.37')*R31**3/mp.sqrt(A0)
    cross = (mp.mpf('2.13')*R31*R42+mp.mpf('0.56')*R42**2)/mp.sqrt(A0)
    midn = KMID*A0**mp.mpf('1.5')/(4*g)*mp.e**(-g*A0/4)*(1+2/(g*A0))
    midd = KMID*mp.sqrt(A0)/g*mp.e**(-g*A0/4)
    dec = main + INFL*(R5n+cube+cross+midn+R5d+midd)
    viol = 0; mininc = None
    if name=='W1':
        Xn, Xd, viol, mininc = X_w6(wX, m, mp.mpf(m), nX)
        inc_X = INFL*(Xn+Xd); dec_X = mp.mpf(0)
    else:
        Xn = KMID*A0**mp.mpf('1.5')*(mp.mpf('0.8')/(2*C2T))*mp.e**(-mp.mpf('0.64')*C2T*A0)\
             *(1+1/(mp.mpf('1.28')*C2T*A0))
        Xd = KMID*mp.sqrt(A0)/(mp.mpf('0.8')*C2T)*mp.e**(-mp.mpf('0.64')*C2T*A0)
        dec_X = INFL*(Xn+Xd); inc_X = mp.mpf(0)
    lamL = mp.mpf(wlo)/m; s2max = m/(4*mp.sinh(lamL/2)**2)
    Fn = 2*SQ2PI*m*s2max**mp.mpf('1.5')*mp.e**(-FAR*m)
    Fd = m*mp.sqrt(2*mp.pi*s2max)*mp.e**(-FAR*m)
    share = (dec+dec_X)/(20*cAd) + (inc_X+INFL*(Fn+Fd))/20
    return share*(1+QUADF), viol, mininc

print("== [A1] independent ledger rebuild, m = 401, dps 60 (draft quotes 4 dp) ==")
QUOTED = {'W1':'0.4579','W2':'0.8601','W3':'0.6584','W4':'0.5899',
          'W5':'0.9891','W6b':'0.8277','W7':'0.9808'}
for b in BANDS:
    tot, viol, _ = row(b, 401)
    q = mp.mpf(QUOTED[b[0]])
    ok = abs(tot-q) < mp.mpf('5e-5')
    print(f"  {b[0]:3s}: rebuilt={mp.nstr(tot,7)}  quoted={QUOTED[b[0]]}  "
          f"|diff|<5e-5: {ok}  PASS(<=1): {tot<=1}")

print("\n== [A2] W1 crossover: n = 60 vs n = 6000, monotonicity audit on fine grid ==")
for (w, m) in [('4.001',401),('4.05',401),('4.10',401),('4.30',401),
               ('4.90',401),('5.0',401),('4.001',462),('4.05',461)]:
    Xn60, Xd60, v60, _ = X_w6(w, m, mp.mpf(m), 60)
    Xn6k, Xd6k, v6k, mi = X_w6(w, m, mp.mpf(m), 6000)
    ub_ok = (Xn60 >= Xn6k) and (Xd60 >= Xd6k)
    print(f"  w={w} m={m}: Xn(60)={mp.nstr(Xn60,6)} Xn(6000)={mp.nstr(Xn6k,6)} "
          f"coarse>=fine: {ub_ok}  viol(6000-grid)={v6k}  min dE={mp.nstr(mi,4)}")

print("\n== [A3] exact E|He3|, E|He4| closed forms vs prover's 1.510/2.801 ==")
phi = lambda z: mp.e**(-z*z/2)/SQ2PI
EHe3 = 2*phi(0) + 8*phi(mp.sqrt(3))
z1 = mp.sqrt(3-mp.sqrt(6)); z2 = mp.sqrt(3+mp.sqrt(6))
He3 = lambda z: z**3-3*z
EHe4 = 4*(He3(z2)*phi(z2) - He3(z1)*phi(z1))
print(f"  E|He3| = 2 phi(0)+8 phi(sqrt3) = {mp.nstr(EHe3,10)}   (prover 1.510)")
print(f"  E|He4| = 4[He3(z2)phi(z2)-He3(z1)phi(z1)] = {mp.nstr(EHe4,10)}   (prover 2.801)")
a3max = max(mp.mpf(b[3])/(6*mp.sqrt(mp.mpf(b[5])*401)) for b in BANDS)
b4max = max(mp.mpf(b[4])/(24*mp.mpf(b[5])*401) for b in BANDS)
theta = mp.mpf(20)/401; dq = 1/(2*mp.mpf('141.7497'))
dHe = a3max*EHe3 + b4max*EHe4
tot5 = theta+dHe+dq
print(f"  exact budget: Theta+dHe+dq = {mp.nstr(tot5,8)} <= 0.09: {tot5 <= mp.mpf('0.09')}"
      f"   1/(1-.) = {mp.nstr(1/(1-tot5),8)} <= 1.10: {1/(1-tot5) <= mp.mpf('1.10')}")

print("\n== [A4] efac 'iff' boundary: efac(C5) <= e  <=>  C5 <= 4(1-e^(-1/4)) ==")
Cstar = 4*(1-mp.e**(mp.mpf('-0.25')))
print(f"  exact boundary = {mp.nstr(Cstar,8)}   (draft claims 0.8464; "
      f"0.8464 <= boundary: {mp.mpf('0.8464') <= Cstar} -> claimed cutoff is SAFE but the 'iff' constant is wrong)")
print(f"  efac(0.8464) = {mp.nstr(efac('0.8464'),8)} <= e: {efac('0.8464') <= mp.e}")
print(f"  efac(0.8848) = {mp.nstr(efac('0.8848'),8)} vs e = {mp.nstr(mp.e,8)}")

print("\n== [A5] A-monotonicity thresholds for dec entries (draft: 'decreasing on A >= 32') ==")
# A^1.5 e^{-cA} decreasing iff A >= 1.5/c. mid: c = g/4 -> A >= 6/g; X-t2: c = 0.64 c2.
for gname, g in [('gam*=0.15 (W4 min)', mp.mpf('0.15')), ('c1 = 0.1317 (tier-1)', C1T)]:
    print(f"  mid[{gname}]: A^1.5 e^(-gA/4) decreasing iff A >= {mp.nstr(6/g,6)}")
print(f"  X-tier2: decreasing iff A >= {mp.nstr(mp.mpf('1.5')/(mp.mpf('0.64')*C2T),6)}")
print(f"  actual minimum A0 used = 0.28*401 = {mp.nstr(mp.mpf('0.28')*401,6)} "
      f"-> all entries decreasing ON THE USED RANGE; the flat 'A >= 32' claim is false for tier-1 mid on [32, 45.6)")

print("\n== [A6] named-constant roundings ==")
print(f"  48 sqrt(2pi)/pi = {mp.nstr(48*KMID,10)} <= 38.2985: {48*KMID <= mp.mpf('38.2985')}")
print(f"  8 sqrt(2pi)/pi = {mp.nstr(8*KMID,10)} <= 6.3831: {8*KMID <= mp.mpf('6.3831')}")
print(f"  cube exact 3840/1296*K = {mp.nstr(mp.mpf(3840)/1296*KMID,10)} <= 2.37: {mp.mpf(3840)/1296*KMID <= mp.mpf('2.37')}")
print(f"  cross exact 384/144*K = {mp.nstr(mp.mpf(384)/144*KMID,10)} <= 2.13: {mp.mpf(384)/144*KMID <= mp.mpf('2.13')}")
print(f"  k4^2-term exact coeff 945/1152 = {mp.nstr(mp.mpf(945)/1152,10)}; "
      f"0.56/sqrt(A) >= 0.8203/A iff A >= {mp.nstr((mp.mpf(945)/1152/mp.mpf('0.56'))**2,6)} (draft says 'A >= 3': safe)")
print(f"  2 sqrt(2pi) = {mp.nstr(2*SQ2PI,10)} <= 5.01326: {2*SQ2PI <= mp.mpf('5.01326')}")
print(f"  m*x(4.05, 0.8, 401) = {mp.nstr(401*w6_x('4.05', mp.mpf('0.8'), 401),6)}   (draft SS5: 7.65)")
