#!/usr/bin/env python3
# ref_e_r3_truth_direct.py -- REFEREE (numerics, wave-5 sl4pe): independent
# truth-side verification.  Cumulants of S_lam computed by DIRECT tilted-
# uniform moment sums (weights via iterated multiply, dps 40) -- a different
# route from e2_truth_margins.py's closed-form phi_n identities -- at the
# draft's load-bearing points.  Also cross-validates e2's phi-route cums()
# implementation (max relative gap reported).
import mpmath as mp
mp.mp.dps = 40

def direct_cums(m, lam):
    """sum over factors j = 1..m of central moments of the e^{-lam i}-tilted
    uniform on {0..j-1}; k4 via m4 - 3 c2^2 per factor."""
    r = mp.e**(-lam)
    s2 = k3 = k4 = mp.mpf(0)
    for j in range(1, m+1):
        # weights w_i = r^i, i = 0..j-1, built multiplicatively
        Z = mp.mpf(0); m1 = mp.mpf(0); m2 = mp.mpf(0); m3 = mp.mpf(0); m4 = mp.mpf(0)
        w = mp.mpf(1)
        for i in range(j):
            Z += w; m1 += i*w; m2 += i*i*w; m3 += i**3*w; m4 += i**4*w
            w *= r
        m1 /= Z; m2 /= Z; m3 /= Z; m4 /= Z
        c2 = m2 - m1*m1
        c3 = m3 - 3*m1*m2 + 2*m1**3
        c4 = m4 - 4*m1*m3 + 6*m1*m1*m2 - 3*m1**4 - 3*c2*c2
        s2 += c2; k3 += c3; k4 += c4
    return s2, k3, k4

def phi_cums(m, lam):
    """e2's closed-form route, re-typed (full sum, explicit tail cut 1e-60)."""
    def phis(x):
        q = mp.e**(-x); r1 = 1 - q
        return q/r1**2, q*(1+q)/r1**3, q*(1+4*q+q*q)/r1**4
    p2, p3, p4 = phis(lam)
    s2 = m*p2; k3 = m*p3; k4 = m*p4
    for j in range(1, m+1):
        jl = j*lam
        if jl > 150:
            break
        q2, q3, q4 = phis(jl)
        s2 -= j**2*q2; k3 -= j**3*q3; k4 -= j**4*q4
    return s2, k3, k4

def He(n, x):
    return {3: x**3-3*x, 4: x**4-6*x*x+3, 6: x**6-15*x**4+45*x*x-15}[n]

def eta_of(s2, k3, k4):
    a = k3/(6*s2**mp.mpf('1.5')); b4 = k4/(24*s2**2); c6 = k3**2/(72*s2**3)
    def qh(d):
        z = d/mp.sqrt(s2)
        return (mp.e**(-d*d/(2*s2))/mp.sqrt(2*mp.pi*s2)) * \
               (1 + a*He(3,z) + b4*He(4,z) + c6*He(6,z))
    q0, qm, qp = qh(0), qh(-1), qh(1)
    return s2*((q0*q0 - qm*qp)/(qm*qp)) - 1

BANDS = {'W1': (1.0, 0.8), 'W2': (1.2, 1.4), 'W3': (1.5, 2.6), 'W4': (1.7, 3.5),
         'W5': (2.0, 5.2), 'W6b': (2.1, 6.0), 'W7': (2.2, 6.6)}
def band_of(w):
    w = float(w)
    return ('W1' if w<=5 else 'W2' if w<=6 else 'W3' if w<=8 else
            'W4' if w<=10 else 'W5' if w<=20 else 'W6b' if w<=40 else 'W7')
# exact REM*/J0 (verified in ref_e_r1 == archived e1 fractions), 12 digits
REM = {'W1': mp.mpf('0.017058068129'), 'W2': mp.mpf('0.029318577604'),
       'W3': mp.mpf('0.059379577439'), 'W4': mp.mpf('0.080548451464'),
       'W5': mp.mpf('0.132066143949'), 'W6b': mp.mpf('0.144939416193'),
       'W7': mp.mpf('0.156030179162')}
J0E = {'W1': mp.mpf('0.682941931871'), 'W2': mp.mpf('1.102681422396'),
       'W3': mp.mpf('1.915620422561'), 'W4': mp.mpf('2.536451548536'),
       'W5': mp.mpf('3.667933856051'), 'W6b': mp.mpf('4.178060583807'),
       'W7': mp.mpf('4.595969820838')}

print("== referee r3: direct-moment truth verification at load-bearing points ==")
print("  (direct tilted-uniform sums, dps 40; gap = |direct - phi-route|/|direct|)")
maxgap = mp.mpf(0)
for (m, wstr) in [(401,'4.9'), (401,'356.8'), (561,'4.001'), (561,'5.0'),
                  (561,'6.0'), (561,'499.29'), (1000,'5.0'), (1000,'890')]:
    w = mp.mpf(wstr); lam = w/m
    s2d, k3d, k4d = direct_cums(m, lam)
    s2p, k3p, k4p = phi_cums(m, lam)
    gap = max(abs(s2d-s2p)/s2d, abs(k3d-k3p)/abs(k3d), abs(k4d-k4p)/abs(k4d))
    maxgap = max(maxgap, gap)
    A = lam*lam*s2d; u = 1/A
    r31 = abs(k3d)*lam/s2d; r42 = k4d*lam*lam/s2d
    J = r31**2 - r42/2
    e = eta_of(s2d, k3d, k4d)
    b = band_of(w); R31, R42 = BANDS[b]
    price = mp.mpf(R42)/2 + mp.mpf('0.3')*mp.mpf(R31)**2 + lam*lam/2
    ratio = abs(e)/u/price
    remact = abs(e/u - (lam*lam/2 + r42/2 - r31**2))
    print(f"  m={m} w={wstr} [{b}]: r31={float(r31):.4f} r42={float(r42):.4f} "
          f"J={float(J):.4f} (<=J0 {float(J0E[b]):.4f}: {J <= J0E[b]}) "
          f"|eta|/u={float(abs(e)/u):.4f} ratio={float(ratio):.4f} (<=1: {ratio<=1}) "
          f"REMact={float(remact):.2e} (<=REM*: {remact <= REM[b]}) "
          f"k4>0: {k4d>0}  gap={float(gap):.1e}")
print(f"  max direct-vs-phi relative gap over all 8 points: {float(maxgap):.2e}")
print()
print("  expected from draft/e2: (401,4.9) |eta|/u=0.4503 ratio=0.6432 ;")
print("  (401,356.8) 0.9285/0.1804 ; (561,5.0) r31=0.8864 r42=0.6506 J=0.4603")
print("  ratio=0.6576 ; (561,499.29) J=1.3258 ratio=0.1808 ; (1000,890) J=1.3288")
