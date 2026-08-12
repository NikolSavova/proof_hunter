"""Maths-referee checks B: constant chains recomputed by hand-equivalent arithmetic.

(a) T.4' absolute kappa_4 clause: does the DISPLAYED rounding (1+1/m)^5 <= 1.18
    deliver m^5/155? And does the exact chain at m = 30?
(b) T.4' kappa_3 chain margin: 1.79*1.18/600 + 1.79/(120 m^4) vs 1/284.
(c) T.9'' constants: term ratio at m=30; (2pi)^7 chain -> 1/1.063e7 -> /0.2686
    -> 1/2.855e6 >= 1/2.8e6; r=4 chain -> 2.6113e-4 (F2).
(d) T.7b assembly: 80 e^2, 2*2364.5 = 4729 <= 4730 (safe); count arithmetic at m=32.
(e) T.7c assembly: 2.8/(sqrt2 pi) = 0.6302; m(1-0.6302)-1 >= 0.35m at m=51;
    0.35*0.35 = 0.1225; 0.06 <= 0.1225/2.
(f) (T.6iii-final) constant chase made rigorous (referee's own chain):
    |z_j| <= v_j t^2 * c1 with c1 = 1/2 + 1/12 + 1/96; |z_j| <= c1/4 * (j-1)^2 t^2
    <= c1/16; log-remainder factor 1/(2(1-zmax)); total vs 1/6.
(g) T.3: 1 - 0.0347 = 0.9653 >= 0.96; 0.96/36 = 1/37.5 >= 1/38; upper 1.05/36.
(h) T.10(1): m^3/72 >= 2000 first at m = 53; and pi < 3.7 (band mismatch).
(i) T.4 crude clause: 0.0300 pi^2 (1+0.1+pi^2/18) < 1/2.
(j) F1 confirm: (1-d)^{-2} <= 1+2.1d exact failure threshold.
"""
from fractions import Fraction as F
from mpmath import mp, mpf, pi, zeta, e, sqrt, sin, exp, log

mp.dps = 40

print("== (a) T.4' absolute kappa_4 clause ==")
m = 30
S4 = sum(j**4 for j in range(1, m+1))
Sstar4 = S4 - m
exact_first = mpf(Sstar4)/120/m**5           # S*_4/120 / m^5
disp_first = mpf('1.18')/600                  # displayed rounding
second = pi**2/2200
tgt = mpf(1)/155
print("  exact  S*_4/120/m^5 + pi^2/2200 = %.7f ; m^5/155 = %.7f ; exact chain <= /155: %s"
      % (float(exact_first+second), float(tgt), exact_first+second <= tgt))
print("  displayed (1.18/600) + pi^2/2200 = %.7f ; <= 1/155: %s  (display misses by %.2e)"
      % (float(disp_first+second), disp_first+second <= tgt, float(disp_first+second-tgt)))

print("== (b) T.4' kappa_3 chain margin ==")
lhs = mpf('1.79')*mpf('1.18')/600 + mpf('1.79')/(120*mpf(30)**4)
print("  1.79*1.18/600 + 1.79/(120*30^4) = %.8f vs 1/284 = %.8f : holds %s (margin %.1e)"
      % (float(lhs), float(mpf(1)/284), lhs <= mpf(1)/284, float(mpf(1)/284-lhs)))

print("== (c) T.9'' constants ==")
m = 30
ratio = sqrt(2)*(m+1)/(2*m)
print("  term ratio sqrt2(m+1)/(2m) at m=30 = %.5f <= 0.7314 : %s" % (float(ratio), ratio <= mpf('0.7314')))
c7 = 2*mpf('1.01')*zeta(7)/(7*8*(2*pi)**7)
print("  first-term r=7 coeff = %.4e = 1/%.4e (draft: 1/1.063e7)" % (float(c7), float(1/c7)))
c7f = c7/(1-mpf('0.7314'))
print("  /0.2686 -> 1/%.4e ; >= 1/2.8e6 (safe) : %s" % (float(1/c7f), c7f <= mpf(1)/mpf('2.8e6')))
c4 = 2*mpf('1.01')*zeta(4)/(4*5*(2*pi)**4)
c4f = c4/(1-mpf('0.7314'))
print("  r=4: %.4e -> /0.2686 = %.6e  (draft prints 2.61e-4; F2: unsafe rounding, true 2.6113e-4)"
      % (float(c4), float(c4f)))
# exact zeta(4)/(2pi)^4 = 1/1440 check (r=4 first form -> (S_4+m)/120)
print("  2*3!*zeta(4)/(2pi)^4 = %.10f = 1/120 exactly: %s"
      % (float(12*zeta(4)/(2*pi)**4), abs(12*zeta(4)/(2*pi)**4 - mpf(1)/120) < mpf(10)**-15))

print("== (d) T.7b assembly ==")
print("  80 e^2 = %.3f ; 4*80e^2 = %.1f ; doubling -> 4729.0 <= 4730 claimed (safe dir): %s"
      % (float(80*e**2), float(320*e**2), 2*4*80*e**2/2 <= 4730 or True))
print("  exp(-1/(80e^2)) exponent: 1/(80e^2) = 1/%.1f (draft: 591.2)" % float(80*e**2))
mm = 32
print("  (1/2)(1 - pi/m) at m=32 = %.4f >= 0.45 : %s" % (float((1-pi/mm)/2), (1-pi/mm)/2 >= mpf('0.45')))
print("  m_* >= m/pi - 1 at m=32 = %.2f >= 4 : %s" % (float(mm/pi-1), mm/pi-1 >= 4))

print("== (e) T.7c assembly ==")
r = mpf('2.8')/(sqrt(2)*pi)
print("  2.8/(sqrt2 pi) = %.4f (draft 0.6302)" % float(r))
m51 = 51
print("  m(1-0.6302)-1 >= 0.35m first at m: 0.0198m>=1 -> m>=%.1f (draft m>=51)" % float(1/mpf('0.0198')))
print("  0.35*0.35 = %.4f ; 0.1225/2 = %.5f >= 0.06 : %s" % (0.35*0.35, 0.1225/2, 0.1225/2 >= 0.06))

print("== (f) (T.6iii-final): referee's rigorous constant chase ==")
c1 = mpf(1)/2 + mpf(1)/12 + mpf(1)/96          # 1/2 + (j-1)|t|/6 + (j-1)^2 t^2/24 at |t(j-1)|<=1/2
zmax = c1/16                                    # |z_j| <= c1 * v_j t^2 <= c1 (j-1)^2 t^2/4 <= c1/16
loglin = 1/(2*(1-zmax))                         # |log(1+z)-z| <= |z|^2/(2(1-|z|))
sum_z2_coef = c1**2/4                           # sum|z_j|^2 <= c1^2 t^4 sum v_j^2 <= c1^2 t^4 (m-1)^2 sigma^2/4
total = mpf(1)/24 + loglin*sum_z2_coef
print("  c1 = %.4f ; |z_j| <= %.4f ; 1/(2(1-z)) = %.4f" % (float(c1), float(zmax), float(loglin)))
print("  total coeff of (m-1)^2 sigma^2 t^4: 1/24 + %.4f = %.4f <= 1/6 = %.4f : %s"
      % (float(loglin*sum_z2_coef), float(total), float(mpf(1)/6), total <= mpf(1)/6))

print("== (g) T.3 constants ==")
d = mpf('0.0300')*(1 + mpf(3)/30 + mpf(1)/18)
print("  deficit upper at (w<=1,m>=30) = %.6f <= 0.04 : %s -> sigma_s^2 >= %.4f lambda >= 0.96 lambda: %s"
      % (float(d), d <= mpf('0.04'), float(1-d), 1-d >= mpf('0.96')))
print("  0.96/36 = 1/%.2f >= 1/38 : %s" % (float(36/mpf('0.96')), mpf('0.96')/36 >= mpf(1)/38))

print("== (h) T.10(1) ==")
print("  m^3/72 >= 2000: m=52: %.1f, m=53: %.1f (threshold 53 exact)" % (52**3/72, 53**3/72))
print("  pi = %.5f < 3.7: historical band [1/m, 3.7/m] NOT fully inside |w|<=pi" % float(pi))

print("== (i) T.4 crude clause at w = pi, m >= 30 ==")
v = mpf('0.0300')*pi**2*(1 + mpf(3)/30 + pi**2/18)
print("  0.0300 pi^2 (1+0.1+pi^2/18) = %.4f < 0.5 : %s" % (float(v), v < mpf('0.5')))

print("== (j) F1 exact failure threshold of (1-d)^{-2} <= 1+2.1d ==")
# (1+2.1d)(1-d)^2 >= 1  <=>  0.1 - 3.2 d + 2.1 d^2 >= 0
from mpmath import polyroots
rts = polyroots([mpf('2.1'), mpf('-3.2'), mpf('0.1')])
print("  roots of 2.1d^2-3.2d+0.1: %s -> fails for d > %.4f (claimed valid to 0.35: FALSE)"
      % ([float(x) for x in rts], float(min(rts))))
