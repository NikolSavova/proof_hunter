#!/usr/bin/env python3
# sl4p_nc1_ledger.py -- wave-4 SL4' (kernel-weighted honest ledger).
# Every numeric claim in wave4_sl4p_20260812.md quotes THIS file's output.
#
# Pricing convention (draft SS2): entries in u-units (u = 1/A).  Row criterion is
# the SHARE form (draft Lemma SL4'.8): for A in [cA m, m],
#    share(W,m) = dec_total(A0 = cA m)/(20 cA)  +  inc_total(A = m)/20   <= 1/(1+QUADF)
# dec = A-nonincreasing entries (worst at A = cA m); inc = A-increasing entries
# (W1's W.6-crossover, far, and their den partners; worst at A = m by Lemma C.1).
# QUADF = second-order absorption (Lemma SL4'.7); INFL = denominator/Edgeworth
# normalization inflation (Lemma SL4'.6); both justified in block [5].
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

def efac(C5):   # Lemma SL4'.3(i): (1/2)^4 / (1/2 - C5/8)^4 ; <= e iff C5 <= 0.8464
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

print("== [0] named-constant verification (Gaussian-moment integrals, mp.quad, dps 40) ==")
lam_s, s2_s = mp.mpf('0.011'), mp.mpf('1.0e6')   # sample W1-scale point
A_s = lam_s**2*s2_s
half = mp.mpf('0.5')
# R5: A*s2*sqrt(2pi s2)/pi * int t^2 * C5 s2 t^5/lam^3 * e^{-(1/2-C5/8) s2 t^2} dt  vs  48sq/pi*C5*efac/sqrt(A)
for C5 in (mp.mpf('0.05'), mp.mpf('0.8')):
    I = mp.quad(lambda t: t**7*mp.e**(-(half-C5/8)*s2_s*t*t), [0, 20/mp.sqrt(s2_s)])
    direct = A_s*s2_s*mp.sqrt(2*mp.pi*s2_s)/mp.pi*C5*s2_s/lam_s**3*I
    print(f"  R5 const: C5={float(C5)}: direct={float(direct):.6f} <= "
          f"claimed {float(e_R5n(C5,A_s)):.6f} : {direct <= e_R5n(C5,A_s)*(1+mp.mpf('1e-25'))}"
          f"   [efac={float(efac(C5)):.4f} <= e={float(mp.e):.4f}: {efac(C5)<=mp.e}]")
# cube: k3-cube term (|k3| <= R31 s2/lam), weight t^2, coeff 1/6 of |x3|^3, x3 = k3 t^3/6
R31c = mp.mpf('1')
I = mp.quad(lambda t: t**2*(R31c*s2_s*t**3/(6*lam_s))**3/6*mp.e**(-s2_s*t*t/2),
            [0, 20/mp.sqrt(s2_s)])
direct = A_s*s2_s*mp.sqrt(2*mp.pi*s2_s)/mp.pi*I
print(f"  cube const: direct={float(direct):.6f} <= claimed 2.37/sqrt(A)="
      f"{float(e_cube(R31c,A_s)):.6f} : {direct <= e_cube(R31c,A_s)}")
# cross: k3k4 t^7/144 + k4^2 t^8/1152 terms
R42c = mp.mpf('1')
I1 = mp.quad(lambda t: t**2*(R31c*s2_s/lam_s)*(R42c*s2_s/lam_s**2)*t**7/144
             *mp.e**(-s2_s*t*t/2), [0, 20/mp.sqrt(s2_s)])
I2 = mp.quad(lambda t: t**2*(R42c*s2_s/lam_s**2)**2*t**8/1152
             *mp.e**(-s2_s*t*t/2), [0, 20/mp.sqrt(s2_s)])
direct = A_s*s2_s*mp.sqrt(2*mp.pi*s2_s)/mp.pi*(I1+I2)
print(f"  cross consts: direct={float(direct):.6f} <= claimed (2.13+0.56)/sqrt(A)="
      f"{float(e_cross(R31c,R42c,A_s)):.6f} : {direct <= e_cross(R31c,R42c,A_s)}")
# mid Mills: int_a^inf t^2 e^{-g s2 t^2} <= (a/(2 g s2)) e^{-gA/4}(1+2/(gA)), a = lam/2
g = mp.mpf('0.42')
I = mp.quad(lambda t: t*t*mp.e**(-g*s2_s*t*t), [lam_s/2, 30/mp.sqrt(g*s2_s)+lam_s])
mills = lam_s/(4*g*s2_s)*mp.e**(-g*A_s/4)*(1+2/(g*A_s))
print(f"  mid Mills: direct={mp.nstr(I,6)} <= bound={mp.nstr(mills,6)} : {I <= mills}")
print(f"  K_far = 2*sqrt(2pi) = {float(2*SQ2PI):.5f}; K_mid = sqrt(2pi)/pi = {float(SQ2PI/mp.pi):.5f};"
      f" 48*sqrt(2pi)/pi = {float(48*SQ2PI/mp.pi):.4f}; 8*sqrt(2pi)/pi = {float(8*SQ2PI/mp.pi):.4f}")

print("\n== [1] share-priced honest ledger, m = 401 (W1 reported at w = 4.30; sliver in [2]) ==")
mono_all = True
for b in BANDS:
    tot, p, mono = row(b, 401)
    mono_all = mono_all and mono
    dep_mid = "SL3'" if b[8] != 'PROVED' else 'A3-t1'
    dep_X = 'W.6cert' if b[0]=='W1' else 'A3-t2'
    print(f" {b[0]:3s}: share*(1+q)={float(tot):.4f} {'PASS' if tot<=1 else 'FAIL'} "
          f"margin={float(1-tot):+.4f} | main={float(p['main']):.3f}[SL1'i+E] "
          f"R5n={float(p['R5n']):.3f}[SL1'ii] cube={float(p['cube']):.3f} cross={float(p['cross']):.3f}[SL1'i] "
          f"mid={float(p['midn']):.2e}[{dep_mid}] X={float(p['X']):.4f}[{dep_X}] "
          f"far={float(p['Fn']):.3g}[A3+C.1] dens={float(p['dens']):.4f}")
print(f"  W.6 exponent monotone-in-tau on all W1 evaluations: {mono_all}")

print("\n== [2] W1 far sliver: w_dagger(m) = least w with W1 row PASS (scan step 0.01) ==")
for m in (401, 410, 420, 430, 440, 445, 450, 460, 480, 500):
    wdag = None
    for i in range(0, 61):
        w = mp.mpf(4)+mp.mpf(i)/100
        tot, _, _ = row(BANDS[0], m, wX=w)
        if tot <= 1: wdag = w; break
    print(f"  m={m}: W1 PASS for w >= {float(wdag) if wdag is not None else 'none <= 4.60'}")
mstar = None
for m in range(401, 601):
    tot, _, _ = row(BANDS[0], m, wX=mp.mpf('4.001'))
    if tot <= 1 and mstar is None: mstar = m
    if mstar and m == mstar: break
print(f"  full-band closure at w = 4.001: first m with W1 PASS = {mstar}")

print("\n== [3] m-monotonicity of the shares (W1 at w = 4.3) ==")
for b in BANDS:
    vals = [row(b, m)[0] for m in (401, 500, 700, 1000, 2000)]
    dec = all(vals[i+1] < vals[i] for i in range(len(vals)-1))
    print(f"  {b[0]:3s}: shares at m=401/500/700/1000/2000 = "
          + "/".join(f"{float(v):.4f}" for v in vals) + f"  nonincreasing: {dec}")

print("\n== [4] minimal sufficient hypotheses per band (one-at-a-time, others at defaults) ==")
GGRID = ['0.1317','0.15','0.20','0.25','0.30','0.35','0.40','0.42']
CGRID = ['3','1.5','0.8','0.4','0.2','0.10','0.05']
for b in BANDS:
    gmin = None
    for gs in GGRID:
        tot, _, _ = row(b, 401, go=gs)
        if tot <= 1: gmin = gs; break
    cmax = None
    for cs in CGRID:
        if mp.mpf(cs) > mp.mpf('0.8464'): continue   # efac finite/e-bounded only there
        tot, _, _ = row(b, 401, C5o=cs)
        if tot <= 1: cmax = cs; break
    print(f"  {b[0]:3s}: min gamma* = {gmin} (0.1317 = PROVED tier-1); max C5* = {cmax}"
          f" (subject to C5* <= 0.8464 for Lemma SL4'.3)")

print("\n== [5] INFL/QUADF self-consistency budget (Lemmas SL4'.6-7) ==")
m = 401
theta = mp.mpf(20)/m
# banded worst |a3| = R31*/(6 sqrt(A0)), |b4| = R42*/(24 A0), A0 = cAdag*401 per band
a3max = max(mp.mpf(b[3])/(6*mp.sqrt(mp.mpf(b[6])*401)) for b in BANDS)
b4max = max(mp.mpf(b[4])/(24*mp.mpf(b[6])*401) for b in BANDS)
EHe3 = mp.quad(lambda z: abs(z**3-3*z)*mp.e**(-z*z/2), [-12,0,12])/SQ2PI
EHe4 = mp.quad(lambda z: abs(z**4-6*z*z+3)*mp.e**(-z*z/2), [-12,0,12])/SQ2PI
dHe = a3max*EHe3 + b4max*EHe4
dq = 1/(2*mp.mpf('141.7497'))
print(f"  total-perturbation bootstrap Theta = 20/m = {float(theta):.4f}")
print(f"  Edgeworth-vs-Gaussian weight correction <= a3*E|He3|+b4*E|He4| = "
      f"{float(a3max):.4f}*{float(EHe3):.3f}+{float(b4max):.4f}*{float(EHe4):.3f} = {float(dHe):.4f}")
print(f"  q-hat offset ratio |q0/q+- - 1| <= 1/(2 s2) <= {float(dq):.5f}  (s2 >= 141.7497, A2(iii))")
need = 1/(1-theta-dHe-dq)
print(f"  needed inflation 1/(1-Theta-dHe-dq) = {float(need):.4f} <= INFL = {float(INFL)}: {need <= INFL}")
print(f"  second-order absorption: (Theta+dHe+dq) = {float(theta+dHe+dq):.4f} <= QUADF = "
      f"{float(QUADF)}: {theta+dHe+dq <= QUADF}")
