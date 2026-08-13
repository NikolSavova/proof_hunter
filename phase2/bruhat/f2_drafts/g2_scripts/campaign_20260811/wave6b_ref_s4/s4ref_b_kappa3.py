# s4ref_b_kappa3.py -- adversarial check of (SOL.12): lam*|kappa_3| <= (5/2) s2,
# via the termwise closed forms (SOL.9)/(SOL.10), which are also validated here
# against numerical derivatives of the per-factor cgf.
# Termwise ratio rho(lam, j) = lam * kappa_{3,j} / v_j ; if kappa_{3,j} >= 0 for
# all j and sup rho <= 2.5, then (SOL.12) holds at sum level.
import mpmath as mp
mp.mp.dps = 40

def csch(x): return 1/mp.sinh(x)
def v_j(lam, j):
    a = lam/2; b = j*lam/2
    return (csch(a)**2 - j*j*csch(b)**2)/4
def k3_j(lam, j):
    a = lam/2; b = j*lam/2
    return (csch(a)**2*mp.coth(a) - j**3*csch(b)**2*mp.coth(b))/4

# [0] validate (SOL.9)/(SOL.10) against numerical derivatives of
#     K_j(s) = log[(1 - e^{-(lam-s) j})/(1 - e^{-(lam-s)})]  at s = 0
print("== [0] identity validation (SOL.9)/(SOL.10) vs mp.diff ==")
for (lam, j) in [(mp.mpf("0.89"), 7), (mp.mpf("0.05"), 40), (mp.mpf("0.4"), 3)]:
    K = lambda s: mp.log((1 - mp.e**(-(lam-s)*j))/(1 - mp.e**(-(lam-s))))
    d2 = mp.diff(K, 0, 2); d3 = mp.diff(K, 0, 3)
    e2 = abs(d2 - v_j(lam, j)); e3 = abs(d3 - k3_j(lam, j))
    print(f"  lam={float(lam)}, j={j}: |d2 - v_j| = {mp.nstr(e2,3)}, |d3 - k3_j| = {mp.nstr(e3,3)}"
          f"  {'PASS' if e2 < 1e-25 and e3 < 1e-25 else 'FAIL'}")

# [1] termwise scan: lam in (0, 0.89], j >= 2 (j = 1 is the degenerate 0/0 term)
print("== [1] termwise ratio scan: rho = lam*k3_j/v_j, positivity of k3_j ==")
lams = [mp.mpf(x) for x in
        "0.89 0.85 0.8 0.7 0.6 0.5 0.4 0.3 0.2 0.15 0.1 0.07 0.05 0.03 0.02 0.01 0.005 0.002 0.001".split()]
js = [2,3,4,5,6,8,10,13,17,22,30,40,60,90,140,220,350,600,1000,2000,5000,20000,100000]
worst = mp.mpf(0); worst_at = None; neg_found = False
for lam in lams:
    for j in js:
        v = v_j(lam, j); k3 = k3_j(lam, j)
        if k3 < 0:
            neg_found = True
            print(f"  NEGATIVE kappa_3 term at lam={float(lam)}, j={j}: {mp.nstr(k3,6)}")
        rho = lam*k3/v
        if rho > worst: worst, worst_at = rho, (float(lam), j)
print(f"  grid sup rho = {mp.nstr(worst, 10)} at (lam, j) = {worst_at}")
print(f"  any negative kappa_3 term: {neg_found}")

# refine near the grid max: lam near 0.89, j large; also the analytic j->inf limit
print("== [2] j -> infinity limit rho_inf(lam) = lam coth(lam/2), sup over (0, 0.89] ==")
rinf = lambda lam: lam*mp.coth(lam/2)
sup_inf = rinf(mp.mpf("0.89"))
print(f"  rho_inf(0.89) = {mp.nstr(sup_inf, 10)}  (this is the campaign's W7 geometric limit r31geo)")
# rho_inf is increasing in lam (derivative check on a grid)
incr = all(rinf(mp.mpf("0.89")*i/60) < rinf(mp.mpf("0.89")*(i+1)/60) for i in range(1, 60))
print(f"  rho_inf increasing on (0, 0.89] (grid): {incr}")
# fine local refinement around the reported grid max
lam0, j0 = worst_at
best = worst
for dl in [x*mp.mpf("0.001") for x in range(-5, 1)]:
    lam = mp.mpf(str(lam0)) + dl
    if lam <= 0 or lam > mp.mpf("0.89"): continue
    for j in range(max(2, j0//2), j0*2 + 2, max(1, j0//50)):
        rho = lam*k3_j(lam, j)/v_j(lam, j)
        if rho > best: best = rho
print(f"  refined sup rho = {mp.nstr(best, 10)}")
print(f"  CHECK termwise sup <= 2.5: {'PASS' if best <= mp.mpf('2.5') else 'FAIL'}"
      f"  (headroom {mp.nstr((mp.mpf('2.5')-best)/mp.mpf('2.5')*100, 4)}%)")

# [3] sum-level check at adversarial (m, lam) corners
print("== [3] sum-level lam*|kappa_3|/s2 at corners ==")
def sums(m, lam):
    s2 = mp.mpf(0); k3 = mp.mpf(0)
    for j in range(2, m+1):
        s2 += v_j(lam, j); k3 += k3_j(lam, j)
    return s2, k3
corners = [(700, mp.mpf("0.89")), (700, mp.mpf("4.001")/700), (700, mp.mpf("10")/700),
           (561, mp.mpf("0.89")), (561, mp.mpf("4.001")/561), (2000, mp.mpf("0.89")),
           (700, mp.mpf("40.0001")/700), (700, mp.mpf("0.2"))]
ok = True
for m, lam in corners:
    s2, k3 = sums(m, lam)
    ratio = lam*abs(k3)/s2
    good = ratio <= mp.mpf("2.5")
    ok = ok and good
    print(f"  m={m}, lam={mp.nstr(lam,6)} (w={mp.nstr(lam*m,6)}): lam|k3|/s2 = {mp.nstr(ratio, 8)}"
          f"  {'PASS' if good else 'FAIL'}")
print(f"  (SOL.12) sum-level at all corners <= 2.5: {ok}")
