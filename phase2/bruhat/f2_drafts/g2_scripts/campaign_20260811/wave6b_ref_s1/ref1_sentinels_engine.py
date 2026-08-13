#!/usr/bin/env python3
# wave6b_ref_s1 / ref1_sentinels_engine.py
# Adversarial numerics referee for sol_s1_20260812.md (gpt-5.6-sol attempt at (S1)).
# INDEPENDENT cumulant engine (written from the tilted-factor definition, not copied
# from any campaign script), validated two ways (brute-force convolution at small m;
# numerical differentiation of log Z), then used for:
#   [A] engine validation
#   [B] V1 sentinel table (m=561, band right edges)
#   [C] V2 geometric values a(0.89), b(0.89) + zeta(2)/e^4 enclosures used by the draft
#   [D] D_n identity (5) spot check + kappa3 >= 0 (SOL.2) spot checks
#   [E] reflection claim of SOL.9 (lambda < 0)
#   [F] SOL.3 envelope at finite m (r31 <= a(lam), r42 <= b(lam)) incl. W7 corners
#   [G] ADVERSARIAL truth-vs-certified-ceiling sweep: off-grid band edges, m=561..,
#       worst plan corners; truth must sit under the SOL.6/SOL.7 certified ceilings
from mpmath import mp, mpf, exp, log, sinh, cosh, coth, zeta, e, diff, fabs

mp.dps = 50

def g2(x): q = exp(-x); return q/(1-q)**2
def g3(x): q = exp(-x); return q*(1+q)/(1-q)**3
def g4(x): q = exp(-x); return q*(1+4*q+q*q)/(1-q)**4

def cumulants(m, lam):
    """kappa_2,3,4 of the lambda-tilted Mahonian (sum of tilted uniforms on {0..j-1})."""
    k2 = m*g2(lam); k3 = m*g3(lam); k4 = m*g4(lam)
    for j in range(1, m+1):
        x = j*lam
        k2 -= j**2*g2(x); k3 -= j**3*g3(x); k4 -= j**4*g4(x)
    return k2, k3, k4

def ratios(m, lam):
    k2, k3, k4 = cumulants(m, lam)
    return lam*k3/k2, lam*lam*k4/k2, k2, k3, k4

print("== [A] ENGINE VALIDATION ==")
# A1: brute-force convolution at m=6, lam=0.3 (exact distribution of inv under tilt)
m0, lam0 = 6, mpf("0.3")
dist = [mpf(1)]
for j in range(1, m0+1):
    w = [exp(-lam0*a) for a in range(j)]
    new = [mpf(0)]*(len(dist)+j-1)
    for i, p in enumerate(dist):
        for a in range(j):
            new[i+a] += p*w[a]
    dist = new
Z = sum(dist)
mu = [sum(p*mpf(i)**r for i, p in enumerate(dist))/Z for r in range(5)]
c2 = mu[2]-mu[1]**2
c3 = mu[3]-3*mu[1]*mu[2]+2*mu[1]**3
c4 = mu[4]-4*mu[1]*mu[3]-3*mu[2]**2+12*mu[1]**2*mu[2]-6*mu[1]**4
k2, k3, k4 = cumulants(m0, lam0)
print(f"  brute-force (m=6, lam=0.3): k2 rel err {float(fabs(k2-c2)/c2):.3e}  "
      f"k3 rel err {float(fabs(k3-c3)/fabs(c3)):.3e}  k4 rel err {float(fabs(k4-c4)/fabs(c4)):.3e}")
ok_bf = fabs(k2-c2)/c2 < mpf('1e-40') and fabs(k3-c3)/fabs(c3) < mpf('1e-40') \
        and fabs(k4-c4)/fabs(c4) < mpf('1e-38')
print(f"  brute-force match (<=1e-38 rel): {ok_bf}")

# A2: numerical differentiation of log Z(lam) = sum_j log((1-e^{-j lam})/(1-e^{-lam}))
def logZ(lam, m=50):
    return sum(log((1-exp(-j*lam))/(1-exp(-lam))) for j in range(1, m+1))
mp.dps = 80
kd = [(-1)**n * diff(lambda t: logZ(t, 50), mpf("0.2"), n) for n in (2, 3, 4)]
mp.dps = 50
ke = cumulants(50, mpf("0.2"))
errs = [fabs(kd[i]-ke[i])/fabs(ke[i]) for i in range(3)]
print(f"  diff-of-logZ (m=50, lam=0.2): rel errs {float(errs[0]):.3e} {float(errs[1]):.3e} {float(errs[2]):.3e}")
ok_diff = all(er < mpf('1e-20') for er in errs)
print(f"  logZ-derivative match (<=1e-20 rel): {ok_diff}")

print("\n== [B] V1 SENTINELS (m=561, lam=w/561) vs draft table ==")
draft_sent = {5: ("0.88636", "0.65065"), 6: ("1.0739", "1.2058"), 8: ("1.3485", "2.3075"),
              10: ("1.5184", "3.1636"), 20: ("1.8036", "4.8206"), 40: ("1.9114", "5.4653")}
allB = True
for w, (s31, s42) in draft_sent.items():
    lam = mpf(w)/561
    r31, r42, *_ = ratios(561, lam)
    m31 = fabs(r31-mpf(s31)) < mpf('5e-6') if len(s31) > 6 else fabs(r31-mpf(s31)) < mpf('5e-5')
    m42 = fabs(r42-mpf(s42)) < mpf('5e-6') if len(s42) > 6 else fabs(r42-mpf(s42)) < mpf('5e-5')
    allB = allB and m31 and m42
    print(f"  w={w:3d}: r31={mp.nstr(r31, 8)} (draft {s31}, match {m31})   "
          f"r42={mp.nstr(r42, 8)} (draft {s42}, match {m42})")
print(f"  ALL SENTINELS MATCH: {allB}")

print("\n== [C] V2 GEOMETRIC VALUES + enclosures the draft uses ==")
a089 = mpf("0.89")*coth(mpf("0.445"))
b089 = mpf("0.89")**2*(1+3/(2*sinh(mpf("0.445"))**2))
print(f"  a(0.89) = {mp.nstr(a089, 20)}   in (2.1302, 2.1304): {mpf('2.1302') < a089 < mpf('2.1304')}   < 2.71: {a089 < mpf('2.71')}")
print(f"  b(0.89) = {mp.nstr(b089, 20)}   in (6.4111, 6.4114): {mpf('6.4111') < b089 < mpf('6.4114')}   < 8.17: {b089 < mpf('8.17')}")
z2 = zeta(2)
print(f"  zeta(2) = {mp.nstr(z2, 25)}   in (1.6449340668482264, 1.6449340668482265): "
      f"{mpf('1.6449340668482264') < z2 < mpf('1.6449340668482265')}")
print(f"  e^-4 = {mp.nstr(exp(-4), 12)} < 1/54 = {mp.nstr(mpf(1)/54, 12)}: {exp(-4) < mpf(1)/54}")

print("\n== [D] D_n identity (5) + kappa3 >= 0 spot checks ==")
def h2(x): return (x/(2*sinh(x/2)))**2
def h3(x): return x**3*cosh(x/2)/(4*sinh(x/2)**3)
def h4(x): return x**4*(cosh(x)+2)/(8*sinh(x/2)**4)
for (m, w) in [(561, 20), (561, 5), (1000, 8)]:
    lam = mpf(w)/m
    k2, k3, k4 = cumulants(m, lam)
    D2 = w*h2(lam) - lam*sum(h2(j*lam) for j in range(1, m+1))
    D3 = w*h3(lam) - lam*sum(h3(j*lam) for j in range(1, m+1))
    D4 = w*h4(lam) - lam*sum(h4(j*lam) for j in range(1, m+1))
    e2 = fabs(D2-lam**3*k2)/fabs(D2); e3 = fabs(D3-lam**4*k3)/fabs(D3); e4 = fabs(D4-lam**5*k4)/fabs(D4)
    print(f"  (m={m}, w={w}): |D2-lam^3 k2|/D2={float(e2):.2e}  |D3-lam^4 k3|/D3={float(e3):.2e}  "
          f"|D4-lam^5 k4|/D4={float(e4):.2e}  k3>0: {k3 > 0}")

print("\n== [E] REFLECTION (SOL.9): lam -> -lam ==")
okE = True
for lam_s in ["0.03", "0.5", "0.89"]:
    lam = mpf(lam_s)
    k2p, k3p, k4p = cumulants(561, lam)
    k2n, k3n, k4n = cumulants(561, -lam)
    t = (fabs(k2p-k2n)/k2p, fabs(k3p+k3n)/fabs(k3p), fabs(k4p-k4n)/fabs(k4p))
    okE = okE and all(x < mpf('1e-40') for x in t)
    print(f"  lam=+/-{lam_s}: k2 even {float(t[0]):.1e}, k3 odd {float(t[1]):.1e}, k4 even {float(t[2]):.1e}")
print(f"  reflection identities hold to 1e-40: {okE}")

print("\n== [F] SOL.3 ENVELOPE AT FINITE m (r31 <= a(lam), r42 <= b(lam)) ==")
def a_fun(x): return x*coth(x/2)
def b_fun(x): return x*x + 6*h2(x)
okF = True
probes = [(561, mpf("0.89")), (561, mpf("0.5")), (561, mpf("0.2")), (561, mpf(41)/561),
          (1581, mpf("0.89")), (5000, mpf("0.89")), (100000, mpf("0.89")), (561, mpf("0.889"))]
for m, lam in probes:
    r31, r42, *_ = cumulants_r = ratios(m, lam)
    A, B = a_fun(lam), b_fun(lam)
    ok = (r31 <= A) and (r42 <= B)
    okF = okF and ok
    print(f"  (m={m}, lam={mp.nstr(lam, 6)}, w={mp.nstr(m*lam, 6)}): r31={mp.nstr(r31, 8)} <= a={mp.nstr(A, 8)}; "
          f"r42={mp.nstr(r42, 8)} <= b={mp.nstr(B, 8)}: {ok}")
print(f"  envelope holds at all probes: {okF}")

print("\n== [G] ADVERSARIAL TRUTH SWEEP vs the SOL.6/SOL.7 CERTIFIED CEILINGS ==")
# Certified ceilings (the draft's proved constants, tighter than targets):
bands = [(4, 5, mpf("0.900"), mpf("0.680")), (5, 6, mpf("1.090"), mpf("1.250")),
         (6, 8, mpf("1.370"), mpf("2.400")), (8, 10, mpf("1.550"), mpf("3.260")),
         (10, 20, mpf("1.850"), mpf("4.980")), (20, 40, mpf("1.970"), mpf("5.650"))]
targets31 = [mpf(x) for x in "1.19 1.44 1.82 2.04 2.38 2.56".split()]
targets42 = [mpf(x) for x in "0.87 1.62 3.11 4.27 6.38 7.33".split()]
ws_off = {  # off-grid + edge + interior adversarial w per band
    0: ["4.0001", "4.03125", "4.5", "4.999", "4.9998779296875", "5"],
    1: ["5.0001", "5.5", "5.9231", "6"], 2: ["6.0001", "6.71875", "7.5", "8"],
    3: ["8.0001", "9.0313", "9.999", "10"], 4: ["10.0001", "13.7", "19.4141", "20"],
    5: ["20.0001", "27.31", "39.999", "40"]}
ms = [561, 562, 563, 599, 700, 1000, 2500]
worst = {}
okG = True
for bi, (wa, wb, c31, c42) in enumerate(bands):
    wmax31 = wmax42 = mpf(-1); arg31 = arg42 = None
    for ws in ws_off[bi]:
        w = mpf(ws)
        for m in ms:
            lam = w/m
            r31, r42, *_ = ratios(m, lam)
            if r31 > wmax31: wmax31, arg31 = r31, (ws, m)
            if r42 > wmax42: wmax42, arg42 = r42, (ws, m)
            if r31 > c31 or r42 > c42:
                okG = False
                print(f"  ** VIOLATION band {bi}: w={ws}, m={m}: r31={mp.nstr(r31,8)} vs {c31}, r42={mp.nstr(r42,8)} vs {c42}")
    print(f"  band ({wa},{wb}]: max r31={mp.nstr(wmax31, 7)} @ {arg31} (ceil {c31}, target {targets31[bi]});"
          f" max r42={mp.nstr(wmax42, 7)} @ {arg42} (ceil {c42}, target {targets42[bi]})")
print(f"  truth <= certified ceilings at ALL sampled adversarial points: {okG}")

# W7 adversarial: w just above 40 and the deep corner region
print("  -- W7 (ceilings 2.71 / 8.17 via a(0.89), b(0.89)) --")
okW7 = True
for (m, lam) in [(561, mpf("40.0001")/561), (561, mpf("0.089")), (561, mpf("0.6")),
                 (561, mpf("0.89")), (562, mpf("0.89")), (1581, mpf("0.89")),
                 (5000, mpf("0.89")), (50000, mpf("0.89")), (561, mpf("0.88999"))]:
    r31, r42, *_ = ratios(m, lam)
    ok = r31 <= mpf("2.71") and r42 <= mpf("8.17") and r31 <= a089 + mpf('1e-30') and r42 <= b089 + mpf('1e-30')
    okW7 = okW7 and ok
    print(f"    (m={m}, lam={mp.nstr(lam, 6)}): r31={mp.nstr(r31, 8)}  r42={mp.nstr(r42, 8)}  ok={ok}")
print(f"  W7 truth under 2.71/8.17 (and under a(0.89)/b(0.89)) at all probes: {okW7}")

print("\n== SUMMARY flags ==")
print(f"  A(engine) {ok_bf and ok_diff}  B(sentinels) {allB}  E(reflection) {okE}  "
      f"F(envelope) {okF}  G(truth<=ceilings) {okG and okW7}")
