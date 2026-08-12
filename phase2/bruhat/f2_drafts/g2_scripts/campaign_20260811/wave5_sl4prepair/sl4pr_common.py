#!/usr/bin/env python3
# sl4pr_common.py -- wave-5 SL4' repair: shared row machinery.
#
# PROVENANCE: the functions below are a byte-faithful copy of the prover's
# wave4_sl4p/sl4p_nc1_ledger.py lines 12-103 (constants, entry functions,
# w6_x, X_w6, far_ent, row), which the wave-4 numerics referee independently
# rebuilt from the draft's closed forms and validated to < 5e-5 on all seven
# rows (referee_numerics_wave4_sl4p.md SS1).  Packaged as an importable module
# for the wave-5 repair scripts; the ONLY changes are (a) removal of the
# prover's print blocks [0]-[5], (b) nothing else.  No existing file modified.
import mpmath as mp
mp.mp.dps = 40
SQ2PI = mp.sqrt(2*mp.pi)
INFL  = mp.mpf('1.10')   # Lemma SL4'.6
QUADF = mp.mpf('0.09')   # Lemma SL4'.7
FAREXP = mp.mpf('0.0741')  # A3 far floor q(2,1) >= 0.0741 (wp1-c W.5(ii)+W.3(i), w > 4)
C1T = mp.mpf('0.1317')     # A3 tier-1 (PROVED) Gaussian exponent on [0, 0.8 lam]
C2T = mp.mpf('0.0871')     # A3 tier-2 (PROVED) exponent to 1.074 lam

# name, wlo, whi, R31*, R42*, cA(SL2 stated), cAdag(row constant; W7 = 0.85 <= SL2
# certified floor 0.852716), C5*(SL1'), gam*(SL3'; W5-W7 use PROVED C1T instead)
BANDS = [
 ('W1', 4, 5,   '1.0','0.8','0.28','0.28','0.05','0.42'),
 ('W2', 5, 6,   '1.2','1.4','0.35','0.35','0.06','0.42'),
 ('W3', 6, 8,   '1.5','2.6','0.42','0.42','0.08','0.40'),
 ('W4', 8, 10,  '1.7','3.5','0.52','0.52','0.10','0.40'),
 ('W5', 10, 20, '2.0','5.2','0.60','0.60','0.15','PROVED'),
 ('W6b',20, 40, '2.1','6.0','0.70','0.70','0.25','PROVED'),
 ('W7', 40, 0,  '2.2','6.6','0.80','0.85','0.80','PROVED')]

def efac(C5):   # Lemma SL4'.3(i): (1/2)^4 / (1/2 - C5/8)^4 ; <= e iff C5 <= 4(1-e^{-1/4})
    return (mp.mpf('0.5')/(mp.mpf('0.5')-mp.mpf(C5)/8))**4
def e_R5n(C5,A):  return 48*SQ2PI/mp.pi*mp.mpf(C5)*efac(C5)/mp.sqrt(A)
def e_R5d(C5,A):  return 8*SQ2PI/mp.pi*mp.mpf(C5)*efac(C5)/mp.sqrt(A)
def e_cube(R31,A): return mp.mpf('2.37')*mp.mpf(R31)**3/mp.sqrt(A)
def e_cross(R31,R42,A):
    return (mp.mpf('2.13')*mp.mpf(R31)*mp.mpf(R42)+mp.mpf('0.56')*mp.mpf(R42)**2)/mp.sqrt(A)
def e_midn(g,A):  # Mills from a = lam/2:  K_mid = sqrt(2pi)/pi, /(4g)
    return SQ2PI/mp.pi*A**mp.mpf('1.5')/(4*g)*mp.e**(-g*A/4)*(1+2/(g*A))
def e_midd(g,A):
    return SQ2PI/mp.pi*mp.sqrt(A)/g*mp.e**(-g*A/4)
def e_Xn_tier2(A):  # crossover numerator via A3 tier-2 (PROVED), Mills from 0.8 lam
    return SQ2PI/mp.pi*A**mp.mpf('1.5')*(mp.mpf('0.8')/(2*C2T))*mp.e**(-mp.mpf('0.64')*C2T*A)\
           *(1+1/(mp.mpf('1.28')*C2T*A))
def e_Xd_tier2(A):
    return SQ2PI/mp.pi*mp.sqrt(A)/(mp.mpf('0.8')*C2T)*mp.e**(-mp.mpf('0.64')*C2T*A)

def w6_x(w, tau, m):   # wp1-c W.6 exponent / m at t = tau*lam, lam = w/m (orphan verbatim)
    lam = mp.mpf(w)/m; t = tau*lam
    M = m*mp.sin(t/2); s = mp.sin(t/2)**2; S = mp.sinh(lam/2)**2
    if M <= 1: return mp.mpf(0)
    val = (M-1)/(2*M)*(mp.log(1+s/S) - s/(S*M))
    return max(val, mp.mpf(0))

def X_w6(w, m, A):     # W1 crossover via W.6 exponent; left endpoints; t^2 kernel weight
    lam = mp.mpf(w)/m; tau0 = 2*mp.asin(mp.sinh(lam/2))/lam
    n = 60; h = (tau0-mp.mpf('0.8'))/n
    totn = totd = mp.mpf(0); mono = True; prev = None
    for i in range(n):
        a = mp.mpf('0.8')+i*h; E = m*w6_x(w, a, m)
        if prev is not None and E < prev: mono = False
        prev = E
        totn += h*lam*((a+h)*lam)**2*mp.e**(-E)   # int t^2 e^{-E} dt, left-endpoint E
        totd += h*lam*mp.e**(-E)
    s2 = A/lam**2
    Xn = A*SQ2PI/mp.pi*s2**mp.mpf('1.5')*totn
    Xd = A*SQ2PI/mp.pi*mp.sqrt(s2)*totd
    return Xn, Xd, mono

def far_ent(wcap, m):  # at A = m (worst; C.1); s2 cap = m/(4 sinh^2(lam/2)) at band-left lam
    lam = mp.mpf(wcap)/m; s2max = m/(4*mp.sinh(lam/2)**2)
    Fn = 2*SQ2PI*m*s2max**mp.mpf('1.5')*mp.e**(-FAREXP*m)   # K_far = 2 sqrt(2pi)
    Fd = m*mp.sqrt(2*mp.pi*s2max)*mp.e**(-FAREXP*m)
    return Fn, Fd

def row(b, m, wX=None, C5o=None, go=None):
    name,wlo,whi,R31,R42,cA,cAd,C5,gam = b
    if C5o is not None: C5 = C5o
    if go is not None: gam = go
    cAd = mp.mpf(cAd); A0 = cAd*m
    lammax = mp.mpf('0.89') if name=='W7' else mp.mpf(whi)/m
    main = mp.mpf(R42)/2 + mp.mpf('0.3')*mp.mpf(R31)**2 + lammax**2/2   # SL1'(i)+E-pricing
    g = C1T if gam=='PROVED' else mp.mpf(gam)
    dec = main + INFL*(e_R5n(C5,A0)+e_cube(R31,A0)+e_cross(R31,R42,A0)
                       +e_midn(g,A0)+e_R5d(C5,A0)+e_midd(g,A0))
    mono = True
    if name == 'W1':     # W.6-certificate crossover, priced at A = m, worst w in row
        w_use = wX if wX is not None else mp.mpf('4.3')
        Xn, Xd, mono = X_w6(w_use, m, mp.mpf(m))
        inc_X = INFL*(Xn+Xd)
        dec_X = mp.mpf(0)
    else:                # PROVED tier-2 route: A-decreasing class, joins dec at A0
        dec_X = INFL*(e_Xn_tier2(A0)+e_Xd_tier2(A0))
        inc_X = mp.mpf(0)
    Fn, Fd = far_ent(wlo, m)
    share = (dec+dec_X)/(20*cAd) + (inc_X+INFL*(Fn+Fd))/20
    tot = share*(1+QUADF)
    parts = dict(main=main, R5n=e_R5n(C5,A0), cube=e_cube(R31,A0),
                 cross=e_cross(R31,R42,A0), midn=e_midn(g,A0),
                 X=(inc_X/INFL if name=='W1' else dec_X/INFL),
                 Fn=Fn, dens=e_R5d(C5,A0)+e_midd(g,A0)+Fd)
    return tot, parts, mono
