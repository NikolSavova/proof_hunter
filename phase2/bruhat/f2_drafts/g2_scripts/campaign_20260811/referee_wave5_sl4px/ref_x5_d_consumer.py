# referee_wave5_sl4px/ref_x5_d_consumer.py
# Consumer-side verification for the wave-5 SL4'-X note:
# [RD1] verbatim reimplementation of the sl4p ledger's X_w6 (n = 60) at
#       (w = 4.30, m = 401, A = m): reproduce the quoted row entry
#       "X = 1.0363" (= Xn + Xd) and the mono flag True.
# [RD2] Corollary X.3 upper-bound property tested against the TRUE integrals
#       (mp.quad, dps 50) at five (w, m) pairs spanning the domain, at both
#       n = 60 and n = 6000: sum >= integral required for totn and totd,
#       and fine-grid sums must sit between the integral and the coarse sums.
# [RD3] Remark R3 guard audit: on all W1 evaluations (and the corners),
#       M > 1 and val > 0 so w6_x's guards (return 0 if M <= 1; max(val,0))
#       are never active: verify w6_x == raw formula exactly there.
# [RD4] the draft's Section 6 consistency-note arithmetic, checked against
#       the wave-4 referee's ARCHIVED [A2] min-dE values.
from mpmath import mp

mp.dps = 50
SQ2PI = mp.sqrt(2*mp.pi)

def w6_x(w, tau, m):   # verbatim from sl4p_nc1_ledger.py
    lam = mp.mpf(w)/m; t = tau*lam
    M = m*mp.sin(t/2); s = mp.sin(t/2)**2; S = mp.sinh(lam/2)**2
    if M <= 1: return mp.mpf(0)
    val = (M-1)/(2*M)*(mp.log(1+s/S) - s/(S*M))
    return max(val, mp.mpf(0))

def w6_x_raw(w, tau, m):  # no guards
    lam = mp.mpf(w)/m; t = tau*lam
    M = m*mp.sin(t/2); s = mp.sin(t/2)**2; S = mp.sinh(lam/2)**2
    return (M-1)/(2*M)*(mp.log(1+s/S) - s/(S*M))

def X_w6(w, m, A, n=60):  # verbatim (n parameterized as in the wave-4 referee)
    lam = mp.mpf(w)/m; tau0 = 2*mp.asin(mp.sinh(lam/2))/lam
    h = (tau0-mp.mpf('0.8'))/n
    totn = totd = mp.mpf(0); mono = True; prev = None
    for i in range(n):
        a = mp.mpf('0.8')+i*h; E = m*w6_x(w, a, m)
        if prev is not None and E < prev: mono = False
        prev = E
        totn += h*lam*((a+h)*lam)**2*mp.e**(-E)
        totd += h*lam*mp.e**(-E)
    s2 = A/lam**2
    Xn = A*SQ2PI/mp.pi*s2**mp.mpf('1.5')*totn
    Xd = A*SQ2PI/mp.pi*mp.sqrt(s2)*totd
    return Xn, Xd, mono, totn, totd

ok_all = True
print("[RD1] ledger X-entry reproduction at (w = 4.30, m = 401, A = m)")
Xn, Xd, mono, _, _ = X_w6('4.30', 401, mp.mpf(401))
entry = Xn + Xd
ok1 = mp.nstr(entry, 5) == '1.0363' and mono
ok_all = ok_all and ok1
print(f"  Xn = {mp.nstr(Xn, 6)}, Xd = {mp.nstr(Xd, 6)}, Xn+Xd = {mp.nstr(entry, 5)} "
      f"(draft/ledger: 1.0363), mono = {mono} : {'OK' if ok1 else '** FAIL **'}")

print("\n[RD2] Cor X.3: left-endpoint sums vs true integrals (mp.quad)")
for wstr, m in [('4.30', 401), ('4.001', 462), ('5.0', 401), ('4.001', 561), ('4.0', 5)]:
    m_ = mp.mpf(m); w = mp.mpf(wstr); lam = w/m_
    tau0 = 2*mp.asin(mp.sinh(lam/2))/lam
    E = lambda tau: m_*w6_x_raw(w, tau, m_)
    In = mp.quad(lambda tau: lam*(tau*lam)**2*mp.e**(-E(tau)), [mp.mpf('0.8'), tau0])
    Id = mp.quad(lambda tau: lam*mp.e**(-E(tau)), [mp.mpf('0.8'), tau0])
    _, _, mono60, tn60, td60 = X_w6(wstr, m, m_, 60)
    _, _, mono6k, tn6k, td6k = X_w6(wstr, m, m_, 6000)
    ok = (tn60 >= tn6k >= In) and (td60 >= td6k >= Id) and mono60 and mono6k
    ok_all = ok_all and ok
    print(f"  w={wstr:>6} m={m:>4}: totn 60/6000/int = {mp.nstr(tn60,6)} >= {mp.nstr(tn6k,6)} >= {mp.nstr(In,6)} | "
          f"totd = {mp.nstr(td60,6)} >= {mp.nstr(td6k,6)} >= {mp.nstr(Id,6)} | mono both: {mono60 and mono6k} : "
          f"{'OK' if ok else '** FAIL **'}")

print("\n[RD3] Remark R3 guard audit (guards never active on w >= 4)")
guard_ok = True
for wstr, m in [('4.001', 401), ('4.30', 401), ('5.0', 401), ('4.001', 462),
                ('4.001', 561), ('4.0', 5), ('356.89', 401)]:
    m_ = mp.mpf(m); w = mp.mpf(wstr); lam = w/m_
    tau0 = 2*mp.asin(mp.sinh(lam/2))/lam
    n = 60; h = (tau0-mp.mpf('0.8'))/n
    for i in range(n):
        a = mp.mpf('0.8')+i*h
        if w6_x(w, a, m_) != w6_x_raw(w, a, m_):
            guard_ok = False
            print(f"  ** guard active at w={wstr}, m={m}, tau={mp.nstr(a,8)}")
ok_all = ok_all and guard_ok
print(f"  guarded == raw at all 60 left endpoints of 7 cases: {guard_ok}")

print("\n[RD4] Section-6 consistency-note arithmetic vs wave-4 referee archive")
minc_405 = mp.mpf('1.78994e-5')                      # draft [B] (4.05, 401)
e_units = 401*minc_405
cell_draft = (mp.mpf('1.074')-mp.mpf('0.8'))/2000
lam405 = mp.mpf('4.05')/401
tau0_405 = 2*mp.asin(mp.sinh(lam405/2))/lam405
cell_ref = (tau0_405 - mp.mpf('0.8'))/6000
ratio = cell_draft/cell_ref
scaled = e_units/ratio
print(f"  m*inc = 401*1.78994e-5 = {mp.nstr(e_units, 4)} (draft: 7.2e-3) | "
      f"draft cell = {mp.nstr(cell_draft, 3)} (draft: 1.37e-4)")
print(f"  referee interval length = {mp.nstr(tau0_405-mp.mpf('0.8'), 6)} (draft: ~0.20) | "
      f"referee cell = {mp.nstr(cell_ref, 4)} (draft: ~3.33e-5) | ratio = {mp.nstr(ratio, 4)} (draft: ~4.1)")
print(f"  scaled prediction = {mp.nstr(scaled, 4)} vs wave-4 referee ARCHIVED min dE at (4.05,401) = 0.001746")
minc_4001 = mp.mpf('1.73002e-5')
lam4001 = mp.mpf('4.001')/401
tau0_4001 = 2*mp.asin(mp.sinh(lam4001/2))/lam4001
scaled2 = 401*minc_4001/(cell_draft/((tau0_4001-mp.mpf('0.8'))/6000))
print(f"  same scaling at (4.001,401): prediction {mp.nstr(scaled2, 4)} vs ARCHIVED 0.001688")
print(f"  NOTE: wave-4 referee report's phrase '>= 1.7e-3' vs its own archived min 0.001688 at (4.001,401):"
      f" {'consistent' if mp.mpf('0.001688') >= mp.mpf('0.0017') else 'REPORT-SIDE MIS-FLOOR (archive value below 1.7e-3)'}")

print(f"\n[RD] OVERALL: {'ALL OK' if ok_all else '** FAIL **'}")
