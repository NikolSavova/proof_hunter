"""Maths-referee checks A: T.8'' (variance-vs-tilt chain) and T.10(2) (overlap claim).

Target: g2_draft_t2_20260803.md PROVED inventory.
(a) T.8'' displayed route: does E X^2 (untruncated geometric) <= (1+1/lam)^2 hold?
    (The draft's chain 'Var U_j <= E U^2 <= untruncated E X^2 <= (1+1/lam)^2' needs it.)
(b) Statement rescue: Var(truncated geom U_j) <= Var(Geom) via the memorylessness
    mixture identity  Var X = Var U_j + (1-alpha)*(mu_U - (j+mu_X))^2 * ... (exact check),
    and Var(Geom) = q/(1-q)^2 <= (1+1/lam)^2.
(c) T.8'' off-by-one: chain delivers m_* >= sqrt(s2/m) - 2, statement claims -1.
    Numerical search for violations of the stated -1 form (exact s2 via (2.3)).
(d) T.10(2): with rho = 1 - 0.04 w0^2, locate w* where the TRUE deficit equals
    1-rho, and compare with w0: disjointness of {|w|<=w0} and {s2 <= rho*lambda}.
(e) (T.4)-upper constant at (w<=1, m>=30): 0.0300(1+3/m+w^2/18) at m=30,w=1
    = 0.034667, NOT the prose's 0.0332.
(f) Repair arithmetic for T.10(2): rho := 1 - 0.022 w0^2 gives a genuine overlap
    annulus [0.9 w0, w0] using only (T.4)'s proved two sides.
All arithmetic mpmath dps=40 except where noted.
"""
from mpmath import mp, mpf, exp, sqrt, findroot

mp.dps = 40

def geom_moments(lam):
    q = exp(-lam)
    EX = q/(1-q)
    EX2 = q*(1+q)/(1-q)**2
    Var = q/(1-q)**2
    return q, EX, EX2, Var

def trunc_moments(lam, j):
    q = exp(-lam)
    ws = [q**i for i in range(j)]
    Z = sum(ws)
    E = sum(i*w for i, w in zip(range(j), ws))/Z
    E2 = sum(i*i*w for i, w in zip(range(j), ws))/Z
    return E, E2 - E*E

print("== (a) EX^2(Geom) vs (1+1/lam)^2 — the displayed T.8'' route ==")
viol = []
for lam100 in range(2, 60):
    lam = mpf(lam100)/100
    q, EX, EX2, Var = geom_moments(lam)
    bound = (1 + 1/lam)**2
    if EX2 > bound:
        viol.append((float(lam), float(EX2), float(bound)))
print("violations of EX2 <= (1+1/lam)^2 (lam, EX2, bound), first/last of %d:" % len(viol))
if viol:
    print("  ", viol[0], " ... ", viol[-1])
lam = mpf(1)/10
q, EX, EX2, Var = geom_moments(lam)
print("  at lam=0.1: EX2 = %.4f  (1+1/lam)^2 = %.4f  Var(Geom) = %.4f" %
      (float(EX2), float((1+1/lam)**2), float(Var)))

print("== (b) statement rescue: Var(U_j) <= Var(Geom) and mixture identity ==")
worst = mpf(0); ok = True
for lam100 in (2, 5, 10, 30, 50, 100, 300):
    lam = mpf(lam100)/100
    q, EX, EX2, VarX = geom_moments(lam)
    for j in (2, 3, 5, 10, 30, 100):
        EU, VarU = trunc_moments(lam, j)
        alpha = 1 - q**j
        # mixture identity: VarX = alpha*VarU + (1-alpha)*VarX
        #                   + alpha*(EU-mu)^2 + (1-alpha)*(j+EX-mu)^2, mu = EX
        mu = EX
        rhs = alpha*VarU + (1-alpha)*VarX + alpha*(EU-mu)**2 + (1-alpha)*(j+EX-mu)**2
        dev = abs(VarX - rhs)/VarX
        worst = max(worst, dev)
        if VarU > VarX + mpf(10)**-30:
            ok = False
            print("  VIOLATION VarU > VarX at", float(lam), j)
print("  mixture identity max rel dev over grid: %.3e   VarU<=VarX everywhere: %s" %
      (float(worst), ok))
lam = mpf(1)/10
q = exp(-lam)
print("  Var(Geom)=q/(1-q)^2 <= (1+1/lam)^2 check at lam=0.1: %.4f <= %.4f : %s" %
      (float(q/(1-q)**2), float((1+1/lam)**2), q/(1-q)**2 <= (1+1/lam)**2))

print("== (c) T.8'' as stated: m_* >= sqrt(s2/m) - 1 — numerical search ==")
def s2_exact(lam, m):
    # (2.3): sigma_lam^2 = sum_j [g'(lam) - j^2 g'(lam j)], -g'(u)=1/u^2-e^u/(e^u-1)^2
    def mgp(u):  # -g'(u)
        if abs(u) < mpf(10)**-8:
            return mpf(1)/12 - u**2/240
        return 1/u**2 - exp(u)/(exp(u)-1)**2
    return sum((j*j*mgp(lam*j) - mgp(lam)) for j in range(1, m+1))
bad = []
import math
for m in (30, 60, 100, 200):
    for lamx in [mpf(x)/1000 for x in (5, 10, 21, 33, 52, 105, 210, 333, 501, 999, 1999)]:
        s2 = s2_exact(lamx, m)
        mstar = min(m, int(mpf(1)/lamx))
        stated = sqrt(s2/m) - 1
        if mstar < stated:
            bad.append((m, float(lamx), mstar, float(stated)))
print("  violations of stated -1 form on grid:", bad if bad else "none (statement holds numerically; chain as displayed gives only -2)")

print("== (d) T.10(2): rho = 1-0.04 w0^2 — where is the true boundary w*? ==")
for m in (60, 100, 200):
    for w0 in (mpf(1)/2, mpf(1)):
        rho_def = mpf('0.04')*w0**2   # 1 - rho
        lam0 = None
        f = lambda w: 1 - s2_exact(w/m, m)/s2_exact(mpf(10)**-12, m) - rho_def
        # deficit(w) = 1 - s2(w/m)/lambda ; lambda = s2 at lam=0
        lamda = s2_exact(mpf(10)**-12, m)
        g = lambda w: 1 - s2_exact(mpf(w)/m, m)/lamda - rho_def
        wstar = findroot(g, float(w0)*mpf('1.1'))
        print("  m=%4d w0=%.1f : w* (deficit = 0.04 w0^2) = %.4f = %.4f*w0  -> sets %s"
              % (m, float(w0), float(wstar), float(wstar/w0),
                 "DISJOINT (w*>w0)" if wstar > w0 else "overlap"))

print("== (e) (T.4)-upper at w<=1, m>=30 ==")
up = mpf('0.0300')*(1 + mpf(3)/30 + mpf(1)/18)
print("  0.0300(1+3/30+1/18) = %.6f   (prose claims 0.0332; script NC-T2 row uses 0.034667)" % float(up))

print("== (f) repair: rho := 1 - 0.022 w0^2 ==")
# need (i) {s2 >= rho*lambda} subset {|w| <= w0}: deficit(w0) >= 1-rho
#   proved lower deficit(w0) >= 0.0285 w0^2 (1 - w0^2/19) >= 0.0270 w0^2 > 0.022 w0^2 (w0<=1) : True
lo_w0 = mpf('0.0285')*(1 - mpf(1)/19)
# need (ii) {|w| >= 0.9 w0} subset {s2 <= rho*lambda}: deficit(0.9 w0) >= 1-rho
lo_09 = mpf('0.0285')*mpf('0.81')*(1 - mpf('0.81')/19)
print("  deficit(w0)  >= %.5f w0^2 > 0.022 w0^2 : %s" % (float(lo_w0), lo_w0 > mpf('0.022')))
print("  deficit(.9w0)>= %.5f w0^2 > 0.022 w0^2 : %s" % (float(lo_09), lo_09 > mpf('0.022')))
print("  -> {s2>=rho*l} in {|w|<=w0}; {|w|>=0.9w0} in {s2<=rho*l}: overlap annulus [0.9w0, w0], rel width 0.1")

print("== (g) numerics-referee F1-repair inequality range check ==")
# (1-d)^{-2} <= 1+2d+3.5 d^2 claimed 'for d <= 0.4'
for d in (mpf('0.05'), mpf('0.1'), mpf('0.107'), mpf('0.12'), mpf('0.2'), mpf('0.4')):
    lhs = (1-d)**-2; rhs = 1 + 2*d + mpf('3.5')*d*d
    print("  d=%.3f: (1-d)^-2 = %.5f vs 1+2d+3.5d^2 = %.5f  -> %s" %
          (float(d), float(lhs), float(rhs), "OK" if lhs <= rhs else "FALSE"))
