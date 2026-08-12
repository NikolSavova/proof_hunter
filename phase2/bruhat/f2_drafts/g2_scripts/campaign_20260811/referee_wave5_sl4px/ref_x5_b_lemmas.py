# referee_wave5_sl4px/ref_x5_b_lemmas.py
# Adversarial attack on Theorem X.1 / Lemmas X.a-X.c / Cor X.2 as MATHEMATICAL
# claims: every lemma ingredient is tested pointwise on (i) the corners of the
# box D (including the TRUE extreme corner w = 4, lam = 0.89, m = 4/0.89 --
# absent from the draft's [B] table), (ii) the CL-relevant m = 561 edge,
# (iii) off-grid tau values incl. 0.8+1e-12 and 1.074-1e-12, and (iv) 3000
# random (m, lam, tau) draws with lam log-uniform down to 1e-9. At every
# point we check, at dps 60:
#   c1: M >= 0.96193*(w*tau)/2            (Lemma X.a step 1)
#   c2: M >= 1.9238*tau  and M >= 1.53904 (Lemma X.a floors)
#   c3: X := h^2/S <= tau^2               (Lemma X.b step 1)
#   c4: psi(tau) = 1.9238*log(1+tau^2) - tau > 0        (Lemma X.b core)
#   c5: g = log(1+X) - h/(m*S) > 0        (Lemma X.b conclusion)
#   c6: gp = 2h/(S+h^2) - 1/(m*S) > 0     (Lemma X.c conclusion)
#   c7: Q(h) = h^2 - 2mSh + S < 0 and h_- < h < h_+     (Lemma X.c mechanism)
#   c8: x == P(h)*g(h) (factorization identity, rel err < 1e-40)
#   c9: dx/dtau > 0 by the ANALYTIC formula (P'g + P gp)*(lam/2)cos(y)
#  c10: dx/dtau (analytic) == mp.diff numeric (rel err < 1e-20)
# Cor X.2: r(u) = asin(sinh u)/u on a 4001-pt grid of (0, 0.445]:
#  strictly increasing increments, r > 1, r(0.445) < 1.074.
from mpmath import mp
import random

mp.dps = 60
random.seed(20260812)

def pieces(m, lam, tau):
    y = tau*lam/2
    h = mp.sin(y)
    M = m*h
    S = mp.sinh(lam/2)**2
    X = h*h/S
    g = mp.log(1+X) - h/(m*S)
    gp = 2*h/(S+h*h) - 1/(m*S)
    P = (M-1)/(2*M)
    Pp = 1/(2*m*h*h)
    x_direct = (M-1)/(2*M)*(mp.log(1+X) - h*h/(S*M))
    x_fact = P*g
    dxdtau_analytic = (Pp*g + P*gp)*(lam/2)*mp.cos(y)
    return y, h, M, S, X, g, gp, P, Pp, x_direct, x_fact, dxdtau_analytic

viol = []
tested = 0

def attack(m, lam, tau, tag, do_numdiff=False):
    global tested
    tested += 1
    m = mp.mpf(m); lam = mp.mpf(lam); tau = mp.mpf(tau)
    w = m*lam
    y, h, M, S, X, g, gp, P, Pp, xd, xf, dxa = pieces(m, lam, tau)
    checks = {}
    checks['c1_Mfloor_w'] = M >= mp.mpf('0.96193')*(w*tau)/2
    checks['c2_Mfloor'] = (M >= mp.mpf('1.9238')*tau) and (M >= mp.mpf('1.53904')*mp.mpf('0.999999999999'))
    checks['c3_Xcap'] = X <= tau*tau
    checks['c4_psi'] = mp.mpf('1.9238')*mp.log(1+tau*tau) - tau > 0
    checks['c5_g'] = g > 0
    checks['c6_gp'] = gp > 0
    Q = h*h - 2*m*S*h + S
    disc = mp.sqrt(m*m*S*S - S)
    hm, hp = m*S - disc, m*S + disc
    checks['c7_Q'] = (Q < 0) and (hm < h < hp)
    checks['c8_fact'] = abs(xd - xf) <= mp.mpf('1e-40')*max(abs(xd), mp.mpf('1e-50'))
    checks['c9_dx'] = dxa > 0
    if do_numdiff:
        dnum = mp.diff(lambda u: pieces(m, lam, u)[9], tau)
        checks['c10_diffmatch'] = abs(dnum - dxa) <= mp.mpf('1e-20')*abs(dxa)
    bad = [k for k, v in checks.items() if not v]
    if bad:
        viol.append((tag, float(m), float(lam), float(tau), bad))
        print(f"  ** VIOLATION {tag}: m={mp.nstr(m,8)} lam={mp.nstr(lam,8)} tau={mp.nstr(tau,12)} -> {bad}")

print("[RB] adversarial pointwise attack on Lemmas X.a/X.b/X.c + Theorem X.1")

taus_edge = [mp.mpf('0.8'), mp.mpf('0.8')+mp.mpf('1e-12'), mp.mpf('0.9'),
             mp.mpf('1.0'), mp.mpf('1.05'), mp.mpf('1.074')-mp.mpf('1e-12'), mp.mpf('1.074')]

# (a) corners of D, incl. the TRUE extreme corner (w=4, lam=0.89) and m=561 edge
corner_cases = [
    (mp.mpf(4)/mp.mpf('0.89'), mp.mpf('0.89'), 'corner w=4 lam=0.89'),
    (mp.mpf(5), mp.mpf('0.8'), 'draft corner w=4 lam=0.8'),
    (mp.mpf(401), mp.mpf('0.89'), 'corner w=356.89'),
    (mp.mpf('4.001')/mp.mpf('0.89'), mp.mpf('0.89'), 'w=4.001 lam=0.89'),
    (mp.mpf(561), mp.mpf('4.001')/561, 'm=561 w=4.001'),
    (mp.mpf(561), mp.mpf('5')/561, 'm=561 w=5'),
    (mp.mpf(561), mp.mpf('4')/561, 'm=561 w=4'),
    (mp.mpf(560), mp.mpf('4.0000001')/560, 'm=560 w=4+'),
    (mp.mpf(562), mp.mpf('4.0000001')/562, 'm=562 w=4+'),
    (mp.mpf('1e9'), mp.mpf('4')/mp.mpf('1e9'), 'm=1e9 w=4'),
    (mp.mpf('1e9'), mp.mpf('0.89'), 'm=1e9 lam=0.89 (huge w)'),
    (mp.mpf(401), mp.mpf('4.001')/401, 'ledger w=4.001'),
    (mp.mpf(401), mp.mpf('5')/401, 'ledger w=5'),
]
for m, lam, tag in corner_cases:
    for tau in taus_edge:
        attack(m, lam, tau, tag, do_numdiff=True)

# (b) dense tau scan (8001 points, off the draft's 2001-grid) at the true
#     extreme corner and at the m=561 sliver edge: strict increase of x
for m, lam, tag in [(mp.mpf(4)/mp.mpf('0.89'), mp.mpf('0.89'), 'corner w=4 lam=0.89'),
                    (mp.mpf(561), mp.mpf('4.001')/561, 'm=561 w=4.001')]:
    N = 8000
    lo, hi = mp.mpf('0.8'), mp.mpf('1.074')
    vals = [pieces(m, lam, lo + (hi-lo)*i/N)[9] for i in range(N+1)]
    incs = [vals[i+1]-vals[i] for i in range(N)]
    mininc = min(incs)
    strict = all(i > 0 for i in incs)
    print(f"  dense-scan {tag}: 8001 pts, min inc = {mp.nstr(mininc, 6)}, strictly increasing: {strict}")
    if not strict:
        viol.append((tag+' dense', float(m), float(lam), None, ['strict']))

# (c) randomized sweep: 3000 draws, lam log-uniform [1e-9, 0.89],
#     w log-uniform [4, 1e5] (10% forced w = 4 exactly), tau uniform [0.8, 1.074]
for i in range(3000):
    lam = mp.mpf(10)**(random.uniform(-9, 0)) * mp.mpf('0.89')**0  # (0,1) scale
    if lam > mp.mpf('0.89'):
        lam = mp.mpf('0.89')
    if random.random() < 0.1:
        w = mp.mpf(4)
    else:
        w = mp.mpf(10)**random.uniform(mp.log(4, 10), 5)
        if w < 4: w = mp.mpf(4)
    m = w/lam
    tau = mp.mpf('0.8') + (mp.mpf('1.074')-mp.mpf('0.8'))*mp.mpf(random.random())
    attack(m, lam, tau, f'rand{i}')

# (d) Cor X.2: r(u) grid audit
print("[RB] Cor X.2 audit: r(u) = asin(sinh u)/u on 4001-pt grid of (0, 0.445]")
N = 4000
us = [mp.mpf('0.445')*(i+1)/(N+1) for i in range(N+1)]
rs = [mp.asin(mp.sinh(u))/u for u in us]
inc_ok = all(rs[i+1] > rs[i] for i in range(N))
gt1 = all(r > 1 for r in rs)
r_max = rs[-1]
print(f"  strictly increasing: {inc_ok} | all r > 1: {gt1} | r(0.445) = {mp.nstr(2*mp.asin(mp.sinh(mp.mpf('0.445')))/mp.mpf('0.89'), 12)} < 1.074: {2*mp.asin(mp.sinh(mp.mpf('0.445')))/mp.mpf('0.89') < mp.mpf('1.074')}")
if not (inc_ok and gt1):
    viol.append(('CorX2', None, None, None, ['grid']))

# (e) record-only: infimum of M(0.8) over D (attained at w=4, lam=0.89)
Minf = (mp.mpf(4)/mp.mpf('0.89'))*mp.sin(mp.mpf('0.8')*mp.mpf('0.89')/2)
print(f"  record: inf over D of M(tau=0.8) = 4 sin(0.356)/0.89 = {mp.nstr(Minf, 8)} "
      f"(floor 1.53904 is {mp.nstr((Minf/mp.mpf('1.53904')-1)*100, 3)}% below)")

print(f"[RB] points tested: {tested}; violations: {len(viol)}")
print(f"[RB] {'ALL OK' if not viol else '** FAILURES: ' + str(viol[:10])}")
