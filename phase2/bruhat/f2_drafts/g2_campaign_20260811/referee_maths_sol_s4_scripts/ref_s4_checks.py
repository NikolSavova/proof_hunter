# ref_s4_checks.py -- adversarial maths-referee checks on sol_s4_20260812.md
# Model: tilted Mahonian S = sum_{j=1}^m Y_j, P(Y_j=l) prop e^{-lam*l}, 0<=l<j.
# Cumulants: kappa_n(Y_j) = Li_{-(n-1)}(e^{-lam}) - j^n Li_{-(n-1)}(e^{-j lam}), n>=2
#            mean_j       = Li_0(e^{-lam})       - j   Li_0(e^{-j lam})
# (from log Z_j(lam) = log(1-e^{-j lam}) - log(1-e^{-lam}), F'(x)=sum e^{-rx}.)
# All checks at mpmath dps 40 unless stated.
from mpmath import mp, mpf, mpc, exp, log, sqrt, pi, gamma as G, quad, polylog, e as E

mp.dps = 40

def cums(m, lam, nmax=12):
    """kappa_n for n=1..nmax (n=1 is the mean) of S."""
    y1 = exp(-lam)
    out = {}
    for n in range(1, nmax + 1):
        tot = mpf(0)
        L1 = polylog(-(n - 1), y1)
        for j in range(1, m + 1):
            yj = exp(-j * lam)
            Lj = polylog(-(n - 1), yj) if yj > mpf('1e-300') else mpf(0)
            tot += L1 - (mpf(j) ** n) * Lj
        out[n] = tot
    return out

def logZ(j, s):
    # log Z_j(s) = log(1-e^{-j s}) - log(1-e^{-s}); s complex ok
    ejs = exp(-j * s)
    return log(1 - ejs) - log(1 - exp(-s))

def logPhi(m, lam, t):
    """log E e^{it(S-k)}, k = E S (exact mean-matching at this lam)."""
    y1 = exp(-lam)
    k = mpf(0)
    for j in range(1, m + 1):
        yj = exp(-j * lam)
        Lj = polylog(0, yj) if yj > mpf('1e-300') else mpf(0)
        k += polylog(0, y1) - j * Lj
    s = mpc(lam, -t)
    tot = mpc(0)
    for j in range(1, m + 1):
        tot += logZ(j, s) - logZ(j, lam)
    return tot - mpc(0, 1) * t * k

print("== [A] exact cumulant checks, m = 700 (and 561), all bands ==")
print("cols: w | A/m | lam*k3/s2 (<=2.5?) | c4=k4*lam^2/s2 (|.|<=6.72?)")
for (m, ws) in [(700, ['4.0001', '5', '10', '20', '50', '120', '300', '623']),
                (561, ['4.0001', '499.29'])]:
    for wstr in ws:
        w = mpf(wstr)
        lam = w / m
        c = cums(m, lam, nmax=7)
        s2 = c[2]
        A = lam ** 2 * s2
        r3 = lam * abs(c[3]) / s2
        c4 = c[4] * lam ** 2 / s2
        print(f"  m={m} w={wstr:>7}: A/m={float(A/m):.5f}  lam*k3/s2={float(r3):.5f} "
              f"({'OK' if r3 <= mpf('2.5') else 'VIOLATION'})  c4={float(c4):.5f} "
              f"({'OK' if abs(c4) <= mpf('6.72') else 'VIOLATION'})")

print()
print("== [B] the (SOL.14)/(SOL.15) remainder: TRUE R4 and ABS series, m=700 ==")
print("units: env := |R4| * 24*lam^2/(s2*t^4)  (so (SOL.15) claims env <= 6.72+0.72u/(1-u))")
print("(SOL.14) claims |R4| <= 0.0021 * s2^2 * t^4, i.e. env <= 0.0504*A")
m = 700
for wstr in ['4.0001', '20', '120', '623']:
    w = mpf(wstr)
    lam = w / m
    c = cums(m, lam, nmax=12)
    s2 = c[2]
    A = lam ** 2 * s2
    for u in [mpf('0.1'), mpf('0.2'), mpf(2) / 7]:
        t = u * lam
        lp = logPhi(m, lam, t)
        R4 = lp + s2 * t ** 2 / 2 + mpc(0, 1) * c[3] * t ** 3 / 6
        env_true = abs(R4) * 24 * lam ** 2 / (s2 * t ** 4)
        # absolute-value series sum_{n=4}^{12} |kappa_n| t^n / n!
        absS = sum(abs(c[n]) * t ** n / G(n + 1) for n in range(4, 13))
        env_abs = absS * 24 * lam ** 2 / (s2 * t ** 4)
        claim15 = mpf('6.72') + mpf('0.72') * u / (1 - u)
        claim14 = mpf('0.0504') * A
        print(f"  w={wstr:>7} u={float(u):.4f}: env_true={float(env_true):8.4f} "
              f"env_absseries={float(env_abs):8.4f} | (SOL.15) claim={float(claim15):6.4f} "
              f"[true fits: {env_true <= claim15}; abs-series fits: {env_abs <= claim15}] "
              f"| (SOL.14) cap={float(claim14):8.3f} [fits: {env_true <= claim14}]")

print()
print("== [C] V1-V8 arithmetic of the draft, recomputed ==")
s20 = mpf(1960000) / 7921
eps0 = 1 / sqrt(s20)
print(f"  s20 = 1960000/7921 = {float(s20):.6f} > 247.44: {s20 > mpf('247.44')}")
print(f"  eps0 = {float(eps0):.8f} < 0.06358: {eps0 < mpf('0.06358')}")
b = mpf('0.0298')
cc = mpf('0.0021') * exp(mpf('0.5376'))
M = {n: 2 ** (mpf(n + 1) / 2) * G(mpf(n + 1) / 2) for n in range(3, 7)}
print(f"  M3={float(M[3])} M4={float(M[4]):.6f} M5={float(M[5])} M6={float(M[6]):.6f}")
Eloc = [(b * M[j + 3] + cc * M[j + 4]) / (2 * pi) for j in range(3)]
tgt_loc = [mpf('0.02328'), mpf('0.04482'), mpf('0.09741')]
for j in range(3):
    print(f"  E_loc[{j}] = {float(Eloc[j]):.9f}  < {float(tgt_loc[j])}: {Eloc[j] < tgt_loc[j]}"
          f"   (margin {float(tgt_loc[j]-Eloc[j]):.2e})")
Emid = []
tgt_mid = [mpf('0.00071'), mpf('0.00308'), mpf('0.01342')]
for j in range(3):
    I = quad(lambda y: y ** j * (exp(-mpf('0.32') * y ** 2) + exp(-y ** 2 / 2)), [4, mp.inf]) / pi
    Emid.append(I)
    print(f"  E_mid[{j}] = {float(I):.9f}  < {float(tgt_mid[j])}: {I < tgt_mid[j]}")
m0 = mpf(700)
ex = exp(-mpf('0.0176') * m0)
Ecross = [mpf('0.274') * mpf('1.074') ** j / pi * m0 ** (mpf(j + 1) / 2) * ex for j in range(3)]
tgt_cr = [mpf('1.04e-5'), mpf('2.94e-4'), mpf('0.00832')]
print(f"  exp(-12.32) = {float(ex):.4e}")
for j in range(3):
    print(f"  E_cross[{j}] = {float(Ecross[j]):.6e}  < {float(tgt_cr[j])}: {Ecross[j] < tgt_cr[j]}")
Efar = [pi ** j / (j + 1) * (m0 ** mpf('1.5') / 4) ** (j + 1) * exp(-mpf('0.0741') * m0) for j in range(3)]
print(f"  E_far[2] = {float(Efar[2]):.3e}  < 1.1e-11: {Efar[2] < mpf('1.1e-11')}")
Etot = [Eloc[j] + Emid[j] + Ecross[j] + Efar[j] for j in range(3)]
tgt_tot = [mpf('0.02401'), mpf('0.04820'), mpf('0.11916')]
caps = [mpf('0.04'), mpf('0.06'), mpf('0.13')]
for j in range(3):
    print(f"  E{j} = {float(Etot[j]):.9f}  < {float(tgt_tot[j])}: {Etot[j] < tgt_tot[j]}"
          f"  < {float(caps[j])}: {Etot[j] < caps[j]}")
z = eps0
g0 = 1 / sqrt(2 * pi)
gz = g0 * exp(-z ** 2 / 2)
print(f"  g(eps0) = {float(gz):.9f} > 0.39813: {gz > mpf('0.39813')}  (margin {float(gz-mpf('0.39813')):.2e})")
gp = z * gz
print(f"  max|g'| = {float(gp):.9f} < 0.02532: {gp < mpf('0.02532')}")
gpp_hi = g0
gpp_lo = (1 - z ** 2) * gz
print(f"  -g'' in ({float(gpp_lo):.9f}, {float(gpp_hi):.9f}) vs (0.39652, 0.39895): "
      f"{gpp_lo > mpf('0.39652') and gpp_hi < mpf('0.39895')}  (lo margin {float(gpp_lo-mpf('0.39652')):.2e}, hi margin {float(mpf('0.39895')-gpp_hi):.2e})")
Hmin = mpf('0.26652') / mpf('0.43895')
Hmax = mpf('0.52895') / mpf('0.35813') + (mpf('0.08532') / mpf('0.35813')) ** 2
print(f"  H_min = {float(Hmin):.6f} > 0.607: {Hmin > mpf('0.607')}")
print(f"  H_max = {float(Hmax):.6f} < 1.535: {Hmax < mpf('1.535')}")
Xmax = mpf('1.535') * exp(mpf('1.535') / mpf('247.44'))
print(f"  X_max = {float(Xmax):.6f} < 1.545: {Xmax < mpf('1.545')}")
print(f"  final deviation bound max(1-0.607, X_max-1) = {float(max(1-mpf('0.607'), Xmax-1)):.6f} < 0.545 < 0.89: "
      f"{max(1-mpf('0.607'), Xmax-1) < mpf('0.545')}")

print()
print("== [D] (SOL.5) provenance fix: tier-2 crossover exponent on W2..W7 ==")
print("  (Lemma R.1 covers only w in (4,5]; tier-2 c2=0.0871 on 0<t<=1.074lam +")
print("   [A2] band floors c_A give |Phi| <= e^{-0.0871*0.64*c_A*m} on [0.8lam, t_0])")
for (band, cA) in [('W2', '0.35'), ('W3', '0.42'), ('W4', '0.52'), ('W5', '0.60'), ('W6', '0.70'), ('W7', '0.80')]:
    v = mpf('0.0871') * mpf('0.64') * mpf(cA)
    print(f"  {band}: 0.0871*0.64*{cA} = {float(v):.6f} >= 0.0176: {v >= mpf('0.0176')}")

print()
print("== [E] scope: does the m=561 case work with the SAME constants? ==")
A561 = mpf('0.28') * 561
print(f"  A_min(561) = 0.28*561 = {float(A561):.2f} < 196: {A561 < 196}"
      f"  -> (2/7)*sqrt(A) = {float(mpf(2)/7*sqrt(A561)):.4f} < 4 (local range |y|<=4 NOT covered)")
s2_561 = A561 / mpf('0.89') ** 2
print(f"  s2_min(561) = {float(s2_561):.4f};  eps(561) <= {float(1/sqrt(s2_561)):.6f} > 0.06358")
ex561 = exp(-mpf('0.0176') * 561)
Ecr561 = [mpf('0.274') * mpf('1.074') ** j / pi * mpf(561) ** (mpf(j + 1) / 2) * ex561 for j in range(3)]
print(f"  E_cross[2](561) = {float(Ecr561[2]):.5f}  (vs 0.00832 at 700: 8.3x bigger)")
# referee-side feasibility sketch at m=561: split local range at y* = (2/7)sqrt(A561)
ystar = mpf(2) / 7 * sqrt(A561)
b561 = mpf(5) / (12 * sqrt(A561))
# honest abs-series remainder envelope: c4max + (24/n!)|k_n| tail with 1.07*(n-1)! model
env_abs_561 = (mpf('6.4113') + mpf('5.136') * (mpf(2) / 7) / (1 - mpf(2) / 7)) / (24 * A561)
cc561 = env_abs_561 * exp(env_abs_561 * ystar ** 4) if env_abs_561 * ystar ** 4 < 1 else None
Eloc561 = [(b561 * M[j + 3] + env_abs_561 * exp(mpf('0.55')) * M[j + 4]) / (2 * pi) for j in range(3)]
Emid561 = []
for j in range(3):
    I = quad(lambda y: y ** j * (exp(-mpf('0.32') * y ** 2) + exp(-y ** 2 / 2)), [ystar, mp.inf]) / pi
    Emid561.append(I)
E561 = [Eloc561[j] + Emid561[j] + Ecr561[j] for j in range(3)]
print(f"  feasibility sketch at 561 (split y*={float(ystar):.3f}, b={float(b561):.5f}, "
      f"rem-const={float(env_abs_561):.6f}):")
print(f"    E0={float(E561[0]):.5f} E1={float(E561[1]):.5f} E2={float(E561[2]):.5f}")
eps561 = 1 / sqrt(s2_561)
g561 = g0 * exp(-eps561 ** 2 / 2)
glo = (1 - eps561 ** 2) * g561
fmin = g561 - E561[0]; fmax = g0 + E561[0]
fppmax = g0 + E561[2]; fppmin = glo - E561[2]
fpmax = eps561 * g0 + E561[1]
Hmin561 = fppmin / fmax
Hmax561 = fppmax / fmin + (fpmax / fmin) ** 2
Xmax561 = Hmax561 * exp(Hmax561 / s2_561)
dev561 = max(1 - Hmin561, Xmax561 - 1)
print(f"    H_min={float(Hmin561):.4f} H_max={float(Hmax561):.4f} -> deviation bound "
      f"{float(dev561):.4f} < 0.89: {dev561 < mpf('0.89')}")

print()
print("== [F] interface: seed vs basin ==")
print(f"  draft delivers 0.545; (S4) needs 0.89; M2 basins 0.90182/0.89412; wave6 basins >= 0.920")
print(f"  0.545 < 0.89 < 0.89412: {mpf('0.545') < mpf('0.89') < mpf('0.89412')}")
print()
print("done.")
