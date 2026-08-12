# ref_mw5x_verify.py -- adversarial MATHS-referee verification for
# wave5_sl4px_20260812.md (Theorem X.1, Corollaries X.2/X.3).
# Written FROM SCRATCH (not copied from the prover's script): the derivative
# dx/dtau is computed from an independently hand-derived closed form and
# cross-checked against mp.diff; probes include the extreme domain corner
# (w = 4, lam = 0.89) that the prover's block [B] did NOT scan.
from mpmath import mp

mp.dps = 50
ALL = True
def rep(label, cond, detail):
    global ALL
    ALL = ALL and bool(cond)
    print(f"  {label}: {detail} : {bool(cond)}")

# --- independent implementation -------------------------------------------
def x_of(m, lam, tau):
    y = tau*lam/2; h = mp.sin(y); M = m*h
    S = mp.sinh(lam/2)**2
    s = h*h
    return (M-1)/(2*M)*(mp.log(1+s/S) - s/(S*M))

def dxdtau_closed(m, lam, tau):
    # hand-derived: x = P(h) g(h), P = (1/2)(1 - 1/(mh)), g = log(1+h^2/S) - h/(mS)
    # dx/dh = P' g + P g',  P' = 1/(2 m h^2),  g' = 2h/(S+h^2) - 1/(mS)
    # dh/dtau = (lam/2) cos(tau lam/2)
    y = tau*lam/2; h = mp.sin(y)
    S = mp.sinh(lam/2)**2
    P  = (mp.mpf(1)/2)*(1 - 1/(m*h))
    Pp = 1/(2*m*h*h)
    g  = mp.log(1+h*h/S) - h/(m*S)
    gp = 2*h/(S+h*h) - 1/(m*S)
    return (Pp*g + P*gp)*(lam/2)*mp.cos(y), g, gp, m*h

print("[V1] closed-form dx/dtau vs mp.diff (independent derivation check)")
pts = [(401, mp.mpf('4.05')/401, mp.mpf('0.9')), (5, mp.mpf('0.8'), mp.mpf('1.0')),
       (mp.mpf(4)/mp.mpf('0.89'), mp.mpf('0.89'), mp.mpf('1.074')),
       (462, mp.mpf('4.001')/462, mp.mpf('0.8'))]
for (m, lam, tau) in pts:
    dc, _, _, _ = dxdtau_closed(m, lam, tau)
    dn = mp.diff(lambda u: x_of(m, lam, u), tau)
    rel = abs(dc-dn)/abs(dn)
    rep("V1", rel < mp.mpf('1e-38'),
        f"m={mp.nstr(mp.mpf(m),8)} lam={mp.nstr(lam,6)} tau={mp.nstr(tau,5)}: "
        f"closed={mp.nstr(dc,10)} vs diff={mp.nstr(dn,10)}, rel={mp.nstr(rel,3)}")

print("[V2] EXTREME corner w=4, lam=0.89 (m=4/0.89=4.4944, unprobed by prover): "
      "full 4001-pt scan of [0.8, 1.074]")
m = mp.mpf(4)/mp.mpf('0.89'); lam = mp.mpf('0.89')
N = 4000
minD = minG = minX = minM = mp.inf
for i in range(N+1):
    tau = mp.mpf('0.8') + (mp.mpf('1.074')-mp.mpf('0.8'))*i/N
    d, g, gp, M = dxdtau_closed(m, lam, tau)
    minD = min(minD, d); minG = min(minG, g)
    minX = min(minX, x_of(m, lam, tau)); minM = min(minM, M)
    if gp <= 0: rep("V2-gp", False, f"g' <= 0 at tau={mp.nstr(tau,8)}"); break
rep("V2", minD > 0 and minG > 0 and minX > 0 and minM > mp.mpf('1.53904'),
    f"min dx/dtau={mp.nstr(minD,6)}, min g={mp.nstr(minG,6)}, min x={mp.nstr(minX,6)}, "
    f"min M={mp.nstr(minM,8)} (floor claim 1.9238*0.8=1.53904; also 1.9238*tau check below)")
# the per-tau floor M >= 1.9238 tau at the corner (tightest place for Lemma X.a)
worstslack = mp.inf
for i in range(N+1):
    tau = mp.mpf('0.8') + (mp.mpf('1.074')-mp.mpf('0.8'))*i/N
    M = m*mp.sin(tau*lam/2)
    worstslack = min(worstslack, M - mp.mpf('1.9238')*tau)
rep("V2b", worstslack > 0, f"min over grid of [M - 1.9238 tau] = {mp.nstr(worstslack,6)} > 0")

print("[V3] random-box scan of D: 3000 quasirandom (w, lam, tau), w in [4, 400], "
      "lam in (0, 0.89], tau in [0.8, 1.074]")
bad = 0; worst = mp.inf
frac = lambda z: z - mp.floor(z)
for i in range(1, 3001):
    w   = 4 + 396*frac(i*mp.sqrt(2))
    lam = mp.mpf('0.89')*(mp.mpf('1e-6') + (1-mp.mpf('1e-6'))*frac(i*mp.sqrt(3)))
    tau = mp.mpf('0.8') + mp.mpf('0.274')*frac(i*mp.sqrt(5))
    m = w/lam
    d, g, gp, M = dxdtau_closed(m, lam, tau)
    worst = min(worst, d)
    if not (d > 0 and g > 0 and M > 1): bad += 1
rep("V3", bad == 0, f"violations = {bad}; min dx/dtau over sample = {mp.nstr(worst,6)}")

print("[V4] Cor X.2: r(u) = arcsin(sinh u)/u on (0, 0.445] -- monotone? >1? max?")
prev = None; mono = True; rmin = mp.inf
for i in range(1, 2001):
    u = mp.mpf('0.445')*i/2000
    r = mp.asin(mp.sinh(u))/u
    rmin = min(rmin, r)
    if prev is not None and r < prev: mono = False
    prev = r
rmax = mp.asin(mp.sinh(mp.mpf('0.445')))/mp.mpf('0.445')
rep("V4", mono and rmin > 1 and rmax < mp.mpf('1.074'),
    f"nondecreasing={mono}, min r={mp.nstr(rmin,10)} > 1, r(0.445)={mp.nstr(rmax,12)} < 1.074")

print("[V5] Cor X.3 numeric: left-endpoint sums vs true integrals (n=60, three W1 points)")
for (wstr, mm) in [('4.001', 401), ('4.05', 401), ('5.0', 401)]:
    w = mp.mpf(wstr); lam = w/mm
    tau0 = 2*mp.asin(mp.sinh(lam/2))/lam
    n = 60; hstep = (tau0 - mp.mpf('0.8'))/n
    totn = totd = mp.mpf(0)
    for i in range(n):
        a = mp.mpf('0.8') + i*hstep
        E = mm*x_of(mm, lam, a)
        totn += hstep*lam*((a+hstep)*lam)**2*mp.e**(-E)
        totd += hstep*lam*mp.e**(-E)
    In = mp.quad(lambda u: (u*lam)**2*mp.e**(-mm*x_of(mm, lam, u))*lam, [mp.mpf('0.8'), tau0])
    Id = mp.quad(lambda u: mp.e**(-mm*x_of(mm, lam, u))*lam, [mp.mpf('0.8'), tau0])
    rep("V5", In <= totn and Id <= totd,
        f"w={wstr}: integral_n={mp.nstr(In,8)} <= totn={mp.nstr(totn,8)}; "
        f"integral_d={mp.nstr(Id,8)} <= totd={mp.nstr(totd,8)}")

print("[V6] NX constants re-derived independently (dps 50)")
rep("V6a", mp.mpf('1.074')*mp.mpf('0.89')/2 == mp.mpf('0.47793'),
    f"y0 = {mp.nstr(mp.mpf('1.074')*mp.mpf('0.89')/2, 10)} (float check; exactness is Fraction-checked upstream)")
rep("V6b", 1 - mp.mpf('0.47793')**2/6 >= mp.mpf('0.96193'),
    f"1-y0^2/6 = {mp.nstr(1 - mp.mpf('0.47793')**2/6, 12)}")
rep("V6c", mp.mpf('1.9238')*mp.log(mp.mpf('1.64')) - mp.mpf('0.8') >= mp.mpf('0.1516'),
    f"psi(0.8) = {mp.nstr(mp.mpf('1.9238')*mp.log(mp.mpf('1.64')) - mp.mpf('0.8'), 12)}")
f1074 = 2*mp.mpf('1.074')/(1+mp.mpf('1.074')**2)
rep("V6d", min(mp.mpf(40)/41, f1074) >= mp.mpf('0.9756'),
    f"min(40/41, f(1.074)) = {mp.nstr(min(mp.mpf(40)/41, f1074), 12)}")
rep("V6e", mp.mpf('1.9238')*mp.mpf('0.8') > 1/mp.log(2),
    f"1.53904 > 1/log2 = {mp.nstr(1/mp.log(2), 12)}")
r089 = 2*mp.asin(mp.sinh(mp.mpf('0.445')))/mp.mpf('0.89')
rep("V6f", r089 <= mp.mpf('1.0739'), f"tau0(0.89)/0.89 = {mp.nstr(r089, 14)}")
rep("V6g", mp.sinh(mp.mpf('0.445')) < 1, f"sinh(0.445) = {mp.nstr(mp.sinh(mp.mpf('0.445')), 12)}")

print("[V7] hypothesis boundaries are REAL (out-of-domain sanity; record-only)")
# w below 4: does the M > 1 guard region invade [0.8, 1.074]?  At w = 1.6,
# m = 401: M(0.8) = 401 sin(0.8*1.6/401/2) ~ 0.64 < 1 -> W.6 inapplicable.
m = 401; lam = mp.mpf('1.6')/m
M08 = m*mp.sin(mp.mpf('0.8')*lam/2)
rep("V7a", M08 < 1, f"w=1.6, m=401: M(0.8) = {mp.nstr(M08,8)} < 1 (x-formula P<0: floor needed)")
# tau far beyond the interval: h = sin turns over -> x eventually decreases
m = mp.mpf(5); lam = mp.mpf('0.8')  # y = pi/2 at tau = pi/0.8 ~ 3.927; scan beyond
d_min_out = min(dxdtau_closed(m, lam, mp.mpf(ts))[0] for ts in ('4.5','5.0','5.5','6.0'))
rep("V7b", d_min_out < 0,
    f"w=4, m=5, tau in [4.5,6] (outside [0.8,1.074]): min dx/dtau = {mp.nstr(d_min_out,6)} < 0")

print(f"OVERALL: {'PASS' if ALL else 'FAIL'}")
