#!/usr/bin/env python3
# e2_truth_margins.py -- wave-5 SL4'-E: truth-side evidence at the shifted
# threshold m >= 561, plus the NON-DERIVABILITY instance (the delta flag).
# Blocks:
#  [A] implementation guard: reproduce the archived out_sl4p_nc2.txt values
#      at (m=401, w=4.9) and (401, 356.8) with closed-form factor cumulants.
#  [B] m = 561 adversarial probes, all bands: r31, r42, J vs J0(W),
#      |eta|/u vs price, REMactual vs certified REM*(W) (e1 authoritative).
#  [C] scope: m = 1000 and m = 5000 spot probes (incl. deep corner lam=0.89).
#  [D] NON-DERIVABILITY: a parameter point satisfying (E0)+(E1)+(E2)+
#      (kappa_4 >= 0 sign lemma) at an in-band (m, lam) with |eta| > price*u:
#      the interface recorded in STATUS_wave4 does NOT imply the pricing.
#  [E] W1 fine w-scan and W7 lam-scan of J at m = 561 (locate per-band max).
#  [F] the (P3') alternative-route diagnostic: measured max r31 vs sqrt(J0).
import mpmath as mp
mp.mp.dps = 30

S0 = mp.mpf(1122800)/7921
BANDS = {'W1': (mp.mpf('0.28'), mp.mpf('1.0'), mp.mpf('0.8'),  5),
         'W2': (mp.mpf('0.35'), mp.mpf('1.2'), mp.mpf('1.4'),  6),
         'W3': (mp.mpf('0.42'), mp.mpf('1.5'), mp.mpf('2.6'),  8),
         'W4': (mp.mpf('0.52'), mp.mpf('1.7'), mp.mpf('3.5'), 10),
         'W5': (mp.mpf('0.60'), mp.mpf('2.0'), mp.mpf('5.2'), 20),
         'W6b':(mp.mpf('0.70'), mp.mpf('2.1'), mp.mpf('6.0'), 40),
         'W7': (mp.mpf('0.80'), mp.mpf('2.2'), mp.mpf('6.6'), None)}
# certified constants from e1_pricing_certificate.py (exact there; floats here)
REMSTAR = {'W1': mp.mpf('0.0170581'), 'W2': mp.mpf('0.0293186'),
           'W3': mp.mpf('0.0593796'), 'W4': mp.mpf('0.0805485'),
           'W5': mp.mpf('0.132066'),  'W6b': mp.mpf('0.144939'),
           'W7': mp.mpf('0.15603')}
def band_of(w):
    w = float(w)
    return ('W1' if w<=5 else 'W2' if w<=6 else 'W3' if w<=8 else
            'W4' if w<=10 else 'W5' if w<=20 else 'W6b' if w<=40 else 'W7')
def Jstar(b):
    _, R31, R42, _ = BANDS[b]
    return R42/2 + mp.mpf('0.3')*R31**2
def J0(b):
    return Jstar(b) - REMSTAR[b]

# closed-form per-factor cumulants of the truncated geometric (q = e^-x):
#   k_n^{(j)} = phi_n(lam) - j^n phi_n(j lam),
#   phi2 = q/(1-q)^2, phi3 = q(1+q)/(1-q)^3, phi4 = q(1+4q+q^2)/(1-q)^4 .
def phis(x):
    q = mp.e**(-x); r = 1 - q
    return q/r**2, q*(1+q)/r**3, q*(1+4*q+q*q)/r**4
def cums(m, lam):
    p2, p3, p4 = phis(lam)
    s2 = m*p2; k3 = m*p3; k4 = m*p4
    for j in range(1, m+1):
        jl = j*lam
        if jl > 130 and j > 1:   # j^4 e^{-jl} < 1e-48: tail negligible at dps 30
            break
        q2, q3, q4 = phis(jl)
        s2 -= j**2*q2; k3 -= j**3*q3; k4 -= j**4*q4
    return s2, k3, k4

def He(n, x):
    return {3: x**3-3*x, 4: x**4-6*x*x+3, 6: x**6-15*x**4+45*x*x-15}[n]
def qhat(d, s2, k3, k4):
    g = mp.e**(-d*d/(2*s2))/mp.sqrt(2*mp.pi*s2); z = d/mp.sqrt(s2)
    return g*(1 + k3/(6*s2**mp.mpf('1.5'))*He(3,z) + k4/(24*s2**2)*He(4,z)
                + k3**2/(72*s2**3)*He(6,z))
def eta_of(s2, k3, k4):
    q0 = qhat(0, s2, k3, k4); qm = qhat(-1, s2, k3, k4); qp = qhat(1, s2, k3, k4)
    return s2*((q0*q0 - qm*qp)/(qm*qp)) - 1

def probe(m, wstr, verbose=True):
    w = mp.mpf(wstr); lam = w/m
    s2, k3, k4 = cums(m, lam)
    A = lam*lam*s2; u = 1/A
    b = band_of(w); _, R31, R42, _ = BANDS[b]
    r31 = abs(k3)*lam/s2; r42 = k4*lam*lam/s2
    J = r31**2 - r42/2
    e = eta_of(s2, k3, k4)
    price = R42/2 + mp.mpf('0.3')*R31**2 + lam*lam/2
    ratio = abs(e)/u/price
    remact = abs(e/u - (lam*lam/2 + r42/2 - r31**2))
    okJ = J <= J0(b); okP = ratio <= 1; okR = remact <= REMSTAR[b]
    okr31 = r31 <= R31; okr42 = r42 <= R42
    if verbose:
        print(f"  m={m} w={wstr} [{b}]: r31={float(r31):.4f} r42={float(r42):.4f} "
              f"J={float(J):.4f} (J0={float(J0(b)):.4f} {'PASS' if okJ else '** FAIL **'}) "
              f"|eta|/u={float(abs(e)/u):.4f} ratio={float(ratio):.4f} "
              f"{'PASS' if okP else '** VIOLATION **'} k4>0:{k4>0} "
              f"REMact={float(remact):.2e} (<=REM*={float(REMSTAR[b]):.4f}: {okR})")
    return r31, r42, J, ratio, okJ and okP and okR and okr31 and okr42

print("== [A] implementation guard vs archived out_sl4p_nc2.txt (m = 401) ==")
for wstr, ref_eu, ref_ratio in [('4.9', '0.4503', '0.6432'), ('356.8', '0.9285', '0.1804')]:
    w = mp.mpf(wstr); lam = w/401
    s2, k3, k4 = cums(401, lam)
    e = eta_of(s2, k3, k4); u = 1/(lam*lam*s2)
    b = band_of(w); _, R31, R42, _ = BANDS[b]
    price = R42/2 + mp.mpf('0.3')*R31**2 + lam*lam/2
    print(f"  w={wstr}: |eta|/u={float(abs(e)/u):.4f} (archived {ref_eu})  "
          f"ratio={float(abs(e)/u/price):.4f} (archived {ref_ratio})")

print()
print("== [B] m = 561 adversarial probes (band edges + interiors + deep corner) ==")
allok = True; worstJmarg = {}; worstratio = mp.mpf(0)
probes = ['4.001','4.05','4.3','4.5','4.9','5.0','5.001','5.5','6.0','6.001','7','8',
          '8.001','9','10','10.001','15','20','20.001','30','40','40.001','60','100',
          '200','350','499.29']
for wstr in probes:
    r31, r42, J, ratio, ok = probe(561, wstr)
    allok = allok and ok
    b = band_of(mp.mpf(wstr))
    worstJmarg[b] = max(worstJmarg.get(b, mp.mpf(-1)), J/J0(b))
    worstratio = max(worstratio, ratio)
print(f"  ALL checks PASS at m = 561: {allok};  worst pricing ratio = {float(worstratio):.4f}")
print("  worst J/J0 by band: " + "  ".join(f"{b}={float(worstJmarg[b]):.4f}" for b in
      ['W1','W2','W3','W4','W5','W6b','W7']))

print()
print("== [C] scope: m = 1000 and m = 5000 ==")
for m, wstr in [(1000,'5.0'),(1000,'890'),(5000,'5.0'),(5000,'4450')]:
    probe(m, wstr)

print()
print("== [D] NON-DERIVABILITY of the pricing from (E0)+(E1)+(E2)+sign lemma ==")
m = 561; w = mp.mpf('4.5'); lam = w/m
A0 = mp.mpf('0.28')*m               # A2 floor, W1
s2x = A0/lam**2                     # s2 = A0/lam^2 >= S0 (huge)
k3x = s2x/lam                       # |k3| = R31*(W1) s2/lam  (E1 with equality)
k4x = mp.mpf(0)                     # (E2) holds; sign lemma k4 >= 0 holds
e = eta_of(s2x, k3x, k4x); u = 1/(lam*lam*s2x)
price = mp.mpf('0.4') + mp.mpf('0.3') + lam*lam/2
print(f"  point: m=561, w=4.5 (W1), s2={float(s2x):.4e} (>= S0: {s2x>=S0}), "
      f"A={float(lam*lam*s2x):.2f} in [c_A m, m]: {A0 <= m}, k3=R31* s2/lam, k4=0")
print(f"  eta/u = {float(e/u):.6f}   price = {float(price):.6f}   "
      f"|eta|/(price*u) = {float(abs(e)/u/price):.4f}  ** > 1: pricing FAILS at this "
      f"hypothesis-consistent point **")

print()
print("== [E] J-max location: W1 fine w-scan and W7 scan, m = 561 ==")
best = (mp.mpf(-1), '')
for k in range(0, 21):
    wstr = mp.nstr(4 + mp.mpf(k)/20, 6)
    r31, r42, J, ratio, ok = probe(561, wstr, verbose=False)
    if J > best[0]: best = (J, wstr)
print(f"  W1 grid w = 4.00(0.05)5.00: max J = {float(best[0]):.4f} at w = {best[1]} "
      f"(J0(W1) = {float(J0('W1')):.4f}; margin {float(1-best[0]/J0('W1'))*100:.1f}%)")
best7 = (mp.mpf(-1), '')
for wstr in ['40.001','45','50','60','80','100','150','200','250','300','350','400','450','480','499.29']:
    r31, r42, J, ratio, ok = probe(561, wstr, verbose=False)
    if J > best7[0]: best7 = (J, wstr)
print(f"  W7 scan to lam = 0.89: max J = {float(best7[0]):.4f} at w = {best7[1]} "
      f"(J0(W7) = {float(J0('W7')):.4f}; margin {float(1-best7[0]/J0('W7'))*100:.1f}%)")

print()
print("== [F] (P3') alternative-route diagnostic: max measured r31 vs sqrt(J0(W)) ==")
edge = {'W1':'5.0','W2':'6.0','W3':'8.0','W4':'10.0','W5':'20.0','W6b':'40.0','W7':'499.29'}
for b in ['W1','W2','W3','W4','W5','W6b','W7']:
    r31, r42, J, ratio, ok = probe(561, edge[b], verbose=False)
    lim = mp.sqrt(J0(b))
    verdict = 'VIABLE' if r31 <= lim else 'DEAD (joint (E3) form required)'
    print(f"  {b:3s}: r31(right edge) = {float(r31):.4f} vs sqrt(J0) = {float(lim):.4f} -> {verdict}")
