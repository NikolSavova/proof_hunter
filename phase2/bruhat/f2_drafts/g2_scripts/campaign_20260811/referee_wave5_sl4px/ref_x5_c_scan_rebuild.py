# referee_wave5_sl4px/ref_x5_c_scan_rebuild.py
# Independent rebuild of the draft's block [B] table (11 cases), written from
# the FACTORED form x = P(h) g(h) (not the draft script's direct formula) and
# with the analytic derivative (P'g + P g')(lam/2)cos(y) in place of mp.diff.
# Every printed 6-digit value of the archived out_x_constants_and_scan.txt
# block [B] is compared string-for-string. Then a half-cell-SHIFTED 2000-pt
# grid (pure off-grid points relative to the draft's grid) re-checks strict
# increase, min x, min g at all 11 cases.
from mpmath import mp

mp.dps = 50

def xval_fact(m, lam, tau):     # factored form -- independent path
    y = tau*lam/2
    h = mp.sin(y)
    S = mp.sinh(lam/2)**2
    P = (mp.mpf(1)/2)*(1 - 1/(m*h))
    g = mp.log(1 + h*h/S) - h/(m*S)
    return P*g

def dx_analytic(m, lam, tau):   # analytic derivative -- replaces mp.diff
    y = tau*lam/2
    h = mp.sin(y)
    S = mp.sinh(lam/2)**2
    P = (mp.mpf(1)/2)*(1 - 1/(m*h))
    Pp = 1/(2*m*h*h)
    g = mp.log(1 + h*h/S) - h/(m*S)
    gp = 2*h/(S+h*h) - 1/(m*S)
    return (Pp*g + P*gp)*(lam/2)*mp.cos(y)

def gval(m, lam, tau):
    h = mp.sin(tau*lam/2)
    S = mp.sinh(lam/2)**2
    return mp.log(1 + h*h/S) - h/(m*S)

# the archived block [B] lines, verbatim (value strings to be reproduced)
archived = {
    ('4.001', 401):  ('1.73002e-5', '0.126256', '0.0177814', '0.0947953', '1.6004'),
    ('4.05', 401):   ('1.78994e-5', '0.13063',  '0.0190656', '0.0996335', '1.62'),
    ('4.10', 401):   ('1.84961e-5', '0.134986', '0.0203806', '0.104451',  '1.64'),
    ('4.30', 401):   ('2.07442e-5', '0.151396', '0.0256607', '0.122602',  '1.71999'),
    ('4.90', 401):   ('2.63871e-5', '0.192587', '0.0411826', '0.168163',  '1.95999'),
    ('5.0', 401):    ('2.71959e-5', '0.198491', '0.0436732', '0.174693',  '1.99999'),
    ('4.001', 462):  ('1.73002e-5', '0.126257', '0.0177815', '0.0947955', '1.6004'),
    ('4.05', 461):   ('1.78995e-5', '0.130631', '0.0190657', '0.0996338', '1.62'),
    ('356.89', 401): ('5.84462e-5', '0.426608', '0.223298',  '0.449814',  '139.76'),
    ('4.0', 5):      ('1.56978e-5', '0.114563', '0.0161409', '0.0886363', '1.57283'),
    ('5.0', 2000000):('2.71965e-5', '0.198495', '0.0436741', '0.174696',  '2.0'),
}

N = 2000
lo, hi = mp.mpf('0.8'), mp.mpf('1.074')
ok_all = True
print("[RC] block-[B] independent rebuild (factored form + analytic derivative)")
for (wstr, m), arch in archived.items():
    w = mp.mpf(wstr); lam = w/m
    taus = [lo + (hi-lo)*i/N for i in range(N+1)]
    vals = [xval_fact(m, lam, u) for u in taus]
    gs = [gval(m, lam, u) for u in taus]
    incs = [vals[i+1]-vals[i] for i in range(N)]
    dmin = min(dx_analytic(m, lam, tt) for tt in [lo, mp.mpf('0.9'), mp.mpf('1.0'), hi])
    Mmin = m*mp.sin(lo*lam/2)
    got = (mp.nstr(min(incs), 6), mp.nstr(dmin, 6), mp.nstr(min(vals), 6),
           mp.nstr(min(gs), 6), mp.nstr(Mmin, 6))
    match = all(g == a for g, a in zip(got, arch))
    pos = all(i > 0 for i in incs) and min(vals) > 0 and min(gs) > 0 and dmin > 0
    ok_all = ok_all and match and pos
    print(f"  w={wstr:>7} m={m:>7}: rebuilt {got} | archived {arch} | "
          f"string-match: {match} | all-positive: {pos}")

print()
print("[RC2] half-cell-SHIFTED grid (2000 pts strictly between the draft's grid points)")
for (wstr, m) in archived:
    w = mp.mpf(wstr); lam = w/m
    hcell = (hi-lo)/N
    taus = [lo + hcell/2 + hcell*i for i in range(N)]      # pure off-grid
    vals = [xval_fact(m, lam, u) for u in taus]
    gs = [gval(m, lam, u) for u in taus]
    incs = [vals[i+1]-vals[i] for i in range(N-1)]
    pos = all(i > 0 for i in incs) and min(vals) > 0 and min(gs) > 0
    ok_all = ok_all and pos
    print(f"  w={wstr:>7} m={m:>7}: off-grid strict-increase + positivity: {pos} "
          f"(min x = {mp.nstr(min(vals), 6)}, min g = {mp.nstr(min(gs), 6)})")

print(f"\n[RC] OVERALL: {'ALL OK' if ok_all else '** FAIL **'}")
