#!/usr/bin/env python3
# ref_e_r4_offgrid.py -- REFEREE (numerics, wave-5 sl4pe): adversarial
# OFF-GRID truth probes the prover did not run.  phi-route cumulants (cross-
# validated to 5e-38 against direct moments in ref_e_r3), dps 40.  Checks at
# every point: J <= J0(W) [exact-12-digit], pricing ratio <= 1, REMact <=
# REM*(W), r31 <= R31*, r42 <= R42*, k4 > 0.  Focus: (i) m-direction worst-
# case claim (m = 561 worst on W1/W2), (ii) band right edges at off-prover m,
# (iii) the deep-tilt lam = 0.89 corner at many m, (iv) micro-edges w -> 4+.
import mpmath as mp
mp.mp.dps = 40

def phis(x):
    q = mp.e**(-x); r1 = 1 - q
    return q/r1**2, q*(1+q)/r1**3, q*(1+4*q+q*q)/r1**4
def cums(m, lam):
    p2, p3, p4 = phis(lam)
    s2 = m*p2; k3 = m*p3; k4 = m*p4
    for j in range(1, m+1):
        jl = j*lam
        if jl > 150: break
        q2, q3, q4 = phis(jl)
        s2 -= j**2*q2; k3 -= j**3*q3; k4 -= j**4*q4
    return s2, k3, k4
def He(n, x):
    return {3: x**3-3*x, 4: x**4-6*x*x+3, 6: x**6-15*x**4+45*x*x-15}[n]
def eta_of(s2, k3, k4):
    a = k3/(6*s2**mp.mpf('1.5')); b4 = k4/(24*s2**2); c6 = k3**2/(72*s2**3)
    def qh(d):
        z = d/mp.sqrt(s2)
        return (mp.e**(-d*d/(2*s2))/mp.sqrt(2*mp.pi*s2))*(1 + a*He(3,z) + b4*He(4,z) + c6*He(6,z))
    q0, qm, qp = qh(0), qh(-1), qh(1)
    return s2*((q0*q0 - qm*qp)/(qm*qp)) - 1

BANDS = {'W1': (1.0, 0.8), 'W2': (1.2, 1.4), 'W3': (1.5, 2.6), 'W4': (1.7, 3.5),
         'W5': (2.0, 5.2), 'W6b': (2.1, 6.0), 'W7': (2.2, 6.6)}
def band_of(w):
    w = float(w)
    return ('W1' if w<=5 else 'W2' if w<=6 else 'W3' if w<=8 else
            'W4' if w<=10 else 'W5' if w<=20 else 'W6b' if w<=40 else 'W7')
REM = {'W1': mp.mpf('0.017058068129'), 'W2': mp.mpf('0.029318577604'),
       'W3': mp.mpf('0.059379577439'), 'W4': mp.mpf('0.080548451464'),
       'W5': mp.mpf('0.132066143949'), 'W6b': mp.mpf('0.144939416193'),
       'W7': mp.mpf('0.156030179162')}
J0E = {'W1': mp.mpf('0.682941931871'), 'W2': mp.mpf('1.102681422396'),
       'W3': mp.mpf('1.915620422561'), 'W4': mp.mpf('2.536451548536'),
       'W5': mp.mpf('3.667933856051'), 'W6b': mp.mpf('4.178060583807'),
       'W7': mp.mpf('4.595969820838')}

nfail = 0; npts = 0
def chk(m, w, quiet=False):
    global nfail, npts
    npts += 1
    lam = mp.mpf(w)/m
    assert lam > mp.mpf(4)/m and lam <= mp.mpf('0.89')*(1 + mp.mpf('1e-30'))
    s2, k3, k4 = cums(m, lam)
    A = lam*lam*s2; u = 1/A
    b = band_of(w); R31, R42 = BANDS[b]
    r31 = abs(k3)*lam/s2; r42 = k4*lam*lam/s2
    J = r31**2 - r42/2
    e = eta_of(s2, k3, k4)
    price = mp.mpf(R42)/2 + mp.mpf('0.3')*mp.mpf(R31)**2 + lam*lam/2
    ratio = abs(e)/u/price
    remact = abs(e/u - (lam*lam/2 + r42/2 - r31**2))
    ok = (J <= J0E[b]) and (ratio <= 1) and (remact <= REM[b]) and \
         (r31 <= mp.mpf(R31)) and (r42 <= mp.mpf(R42)) and (k4 > 0)
    if not ok:
        nfail += 1
        print(f"  ** FAIL ** m={m} w={w} [{b}] J={float(J):.4f} ratio={float(ratio):.4f}")
    elif not quiet:
        print(f"  m={m} w={w} [{b}]: J={float(J):.6f} J/J0={float(J/J0E[b]):.4f} "
              f"ratio={float(ratio):.4f} REMact={float(remact):.2e} k4>0:{k4>0}")
    return J, ratio

print("== [i] m-direction: W1 right edge w = 5.0, m = 561..571 + large ==")
prev = None; mono = True
for m in list(range(561, 572)) + [600, 700, 1000, 2000, 20000]:
    J, _ = chk(m, '5.0', quiet=(562 <= m <= 570))
    if prev is not None and J > prev + mp.mpf('1e-30'): mono = False
    prev = J
print(f"  J(w=5.0) nonincreasing in m over the scan: {mono}")

print()
print("== [ii] W2 right edge w = 6.0, m-scan ==")
prev = None; mono2 = True
for m in [561, 562, 563, 600, 1000, 5000]:
    J, _ = chk(m, '6.0', quiet=(m in (562, 563)))
    if prev is not None and J > prev + mp.mpf('1e-30'): mono2 = False
    prev = J
print(f"  J(w=6.0) nonincreasing in m over the scan: {mono2}")

print()
print("== [iii] deep-tilt corner lam = 0.89 exactly, many m ==")
for m in [561, 562, 563, 577, 601, 700, 1077, 2000, 10000]:
    w = mp.mpf('0.89')*m
    chk(m, w)

print()
print("== [iv] micro-edges and off-grid interiors ==")
for (m, w) in [(561,'4.0001'), (561,'4.00001'), (562,'4.0001'), (600,'4.0001'),
               (561,'4.95'), (561,'4.99'), (561,'4.999'), (563,'5.0'),
               (563,'5.25'), (563,'5.75'), (563,'6.5'), (563,'7.5'), (563,'8.5'),
               (563,'9.5'), (563,'12.5'), (563,'17.5'), (563,'25'), (563,'35'),
               (563,'45'), (563,'80'), (563,'150'), (563,'300'), (563,'450'),
               (600,'5.0'), (600,'6.0'), (600,'8.0'), (600,'10.0'), (600,'20.0'),
               (600,'40.0'), (600,'534'), (100000,'5.0')]:
    chk(m, w)

print()
print(f"== TOTALS: {npts} off-grid probes, {nfail} FAILs ==")

print()
print("== [v] fixed-lam geometric limit at lam = 0.89 (draft: J -> ~1.332) ==")
lam = mp.mpf('0.89')
p2, p3, p4 = phis(lam)
r31g = lam*p3/p2; r42g = lam*lam*p4/p2
print(f"  r31_geom = {mp.nstr(r31g, 8)} (STATUS_wave4 quotes 2.1303), "
      f"r42_geom = {mp.nstr(r42g, 8)} (quotes 6.4113)")
print(f"  J_geom = {mp.nstr(r31g**2 - r42g/2, 8)}  (draft: ~1.332; J0(W7) = 4.59597)")
