"""referee_sol_s1_checks.py — adversarial maths-referee verification for
sol_s1_20260812.md (gpt-5.6-sol's (S1) attempt vs the re-architected
targets of wave6_s1_plan_20260812.md).  Wave 6b cross-model refereeing,
F2 campaign, 2026-08-12.

Blocks:
 [A] SOL.1 closed forms: g_2/g_3/g_4 vs direct series; h_n(0) removable
     values; hyperbolic rewrites of h_2/h_3/h_4/a/b; recurrences (18)/(19).
 [B] SOL.1 cumulant representation vs brute-force discrete tilted law
     (small case m=7, lam=0.3) and D_n = lam^{n+1} kappa_n identity.
 [C] SOL.2/SOL.3 sign & monotonicity attacks: h_2' < 0, h_3' < 0, F > 0,
     a' > 0, b' > 0, bracket(y) > 0 on dense grids.
 [D] SOL.5 (17): sup |h_n''| on [0, 40] by dense scan (dps 30) — verify
     M_2 < 1, M_3 < 4, M_4 < 20 and report observed sups.
 [E] SOL.4 (13): G_n(w) series formula vs direct quadrature; the campaign
     guard value G_4(4) = 0.2323483; tail-truncation size at nu = 33.
 [F] SOL.5 (15): representation residual eps_n at three (m, w) points;
     check |eps_n| <= w lam^2 M_n / 12 with the CLAIMED M_n.
 [G] SOL.6 band table corroboration: dense (w, lam) scan of L_2, U_3/L_2,
     U_4/L_2 per band vs the claimed floors/ceilings (falsification scan;
     the claimed table is an interval-certificate claim).
 [H] SOL.8: a(0.89), b(0.89) enclosures (26)/(27) at dps 50; vs plan's
     geometric limits 2.13031 / 6.41126 and targets 2.71 / 8.17.
 [I] V1 sentinels at m = 561: r31/r42 at w = 5/6/8/10/20/40 via exact
     factor sums, vs the draft table AND the plan's block [T] truth line;
     plus the (561, lam=0.89) W7 point vs plan's 2.12402/6.3713.
 [J] Interface & arithmetic: ceilings < targets (all 7 bands), targets
     == plan table, margins, e^{-4} < 1/54, zeta(2) enclosure (24),
     chain closure 0.978293*20 <= 20, fallback W7 targets 2.42/7.28
     also cleared by the proven geometric bound.
 [K] Adversarial truth attack on (S1-new) itself: r31 <= R31*(W),
     r42 <= R42*(W) over an (m, w)-grid incl. band edges and W7.
"""
import mpmath as mp

mp.mp.dps = 30
ALL_OK = True


def chk(label, cond):
    global ALL_OK
    if not cond:
        ALL_OK = False
    print(("  OK  " if cond else "  **FAIL** ") + label)
    return cond


# ---------- core functions (draft's definitions) ----------
def g_series(n, x, terms=400):
    return mp.nsum(lambda nu: nu**(n - 1) * mp.e**(-nu * x), [1, mp.inf])


def g2(x):
    q = mp.e**(-x)
    return q / (1 - q)**2


def g3(x):
    q = mp.e**(-x)
    return q * (1 + q) / (1 - q)**3


def g4(x):
    q = mp.e**(-x)
    return q * (1 + 4*q + q*q) / (1 - q)**4


def h2(x):
    x = mp.mpf(x)
    if x == 0:
        return mp.mpf(1)
    return (x / (2 * mp.sinh(x / 2)))**2


def h3(x):
    x = mp.mpf(x)
    if x == 0:
        return mp.mpf(2)
    return x**3 * mp.cosh(x / 2) / (4 * mp.sinh(x / 2)**3)


def h4(x):
    x = mp.mpf(x)
    if x == 0:
        return mp.mpf(6)
    return x**4 * (mp.cosh(x) + 2) / (8 * mp.sinh(x / 2)**4)


def a_fun(x):
    return x * mp.coth(x / 2)


def b_fun(x):
    return x**2 * (1 + 3 / (2 * mp.sinh(x / 2)**2))


def En(n, x):
    return sum(x**k / mp.factorial(k) for k in range(n + 1))


def G_n(n, w, nu_max=200):
    s = mp.mpf(0)
    for nu in range(1, nu_max + 1):
        t = mp.e**(-nu * w) * En(n, nu * w) / nu**2
        s += t
        if t < mp.mpf(10)**(-(mp.mp.dps + 5)) and nu > 5:
            break
    return mp.factorial(n - 1) * w - mp.factorial(n) * mp.zeta(2) \
        + mp.factorial(n) * s


def kappa_n(n, m, lam):
    """m g_n(lam) - sum_j j^n g_n(j lam)  (draft eq. (1)-(3))."""
    g = {2: g2, 3: g3, 4: g4}[n]
    s = mp.mpf(0)
    for j in range(1, m + 1):
        s += mp.mpf(j)**n * g(j * lam)
    return m * g(lam) - s


# ================= [A] closed forms =================
print("[A] SOL.1 closed forms / rewrites / recurrences")
for x in [mp.mpf('0.3'), mp.mpf('1.7'), mp.mpf('5.0'), mp.mpf('0.008913')]:
    e2 = abs(g2(x) - g_series(2, x)) / g2(x)
    e3 = abs(g3(x) - g_series(3, x)) / g3(x)
    e4 = abs(g4(x) - g_series(4, x)) / g4(x)
    chk("g2/g3/g4 closed forms at x=%s (max REL err %.1e)"
        % (x, float(max(e2, e3, e4))), max(e2, e3, e4) < mp.mpf(10)**-22)
# removable values
lim2 = mp.limit(lambda t: t**2 * g2(t), 0)
lim3 = mp.limit(lambda t: t**3 * g3(t), 0)
lim4 = mp.limit(lambda t: t**4 * g4(t), 0)
chk("h2(0)=1, h3(0)=2, h4(0)=6 (got %s, %s, %s)"
    % (mp.nstr(lim2, 8), mp.nstr(lim3, 8), mp.nstr(lim4, 8)),
    abs(lim2 - 1) < 1e-15 and abs(lim3 - 2) < 1e-15 and abs(lim4 - 6) < 1e-15)
# hyperbolic rewrites
for x in [mp.mpf('0.6'), mp.mpf('3.3'), mp.mpf('11.0')]:
    r2 = abs(h2(x) - x**2 * g2(x))
    r3 = abs(h3(x) - x**3 * g3(x))
    r4 = abs(h4(x) - x**4 * g4(x))
    ra = abs(a_fun(x) - h3(x) / h2(x))
    rb = abs(b_fun(x) - h4(x) / h2(x))
    rb2 = abs(b_fun(x) - (x**2 + 6 * h2(x)))
    chk("hyperbolic rewrites of h2/h3/h4, a=h3/h2, b=h4/h2=x^2+6h2 at x=%s"
        % x, max(r2, r3, r4, ra, rb, rb2) < mp.mpf(10)**-22)
# recurrences (18)/(19)
for x in [mp.mpf('0.4'), mp.mpf('2.1'), mp.mpf('7.7')]:
    d2 = mp.diff(h2, x)
    d3 = mp.diff(h3, x)
    r18 = abs(h3(x) - (2 * h2(x) - x * d2))
    r19 = abs(h4(x) - (3 * h3(x) - x * d3))
    chk("(18)/(19) recurrences at x=%s (err %.1e)"
        % (x, float(max(r18, r19))), max(r18, r19) < mp.mpf(10)**-18)

# ================= [B] cumulants vs brute force =================
print("[B] SOL.1 representation vs brute-force law; D_n identity")
m_s, lam_s = 7, mp.mpf('0.3')
# brute-force: convolution of tilted uniforms on {0..j-1}
from itertools import product
# distribution of the sum via dynamic programming
dist = {0: mp.mpf(1)}
for j in range(1, m_s + 1):
    Z = sum(mp.e**(-lam_s * a) for a in range(j))
    new = {}
    for s_val, p in dist.items():
        for a in range(j):
            w_ = p * mp.e**(-lam_s * a) / Z
            new[s_val + a] = new.get(s_val + a, mp.mpf(0)) + w_
    dist = new
mu1 = sum(s * p for s, p in dist.items())
mu2 = sum((s - mu1)**2 * p for s, p in dist.items())
mu3 = sum((s - mu1)**3 * p for s, p in dist.items())
mu4 = sum((s - mu1)**4 * p for s, p in dist.items())
k2_bf, k3_bf, k4_bf = mu2, mu3, mu4 - 3 * mu2**2
k2_f = kappa_n(2, m_s, lam_s)
k3_f = kappa_n(3, m_s, lam_s)
k4_f = kappa_n(4, m_s, lam_s)
chk("kappa_2 formula vs brute force (err %.1e)" % float(abs(k2_f - k2_bf)),
    abs(k2_f - k2_bf) < mp.mpf(10)**-22)
chk("kappa_3 formula vs brute force (err %.1e)" % float(abs(k3_f - k3_bf)),
    abs(k3_f - k3_bf) < mp.mpf(10)**-22)
chk("kappa_4 formula vs brute force (err %.1e)" % float(abs(k4_f - k4_bf)),
    abs(k4_f - k4_bf) < mp.mpf(10)**-22)
chk("draft sign convention: kappa_3(lam>0) >= 0 here (k3 = %s)"
    % mp.nstr(k3_f, 8), k3_f >= 0)
# D_n identity at a campaign-scale point
m_t, w_t = 561, mp.mpf(5)
lam_t = w_t / m_t
for n in (2, 3, 4):
    hh = {2: h2, 3: h3, 4: h4}[n]
    D = w_t * hh(lam_t) - lam_t * mp.nsum(lambda j: hh(j * lam_t), [1, m_t],
                                          method='direct')
    K = kappa_n(n, m_t, lam_t)
    rel = abs(D - lam_t**(n + 1) * K) / abs(D)
    chk("D_%d = lam^%d kappa_%d at (561, w=5) (rel err %.1e)"
        % (n, n + 1, n, float(rel)), rel < mp.mpf(10)**-20)

# ================= [C] sign/monotonicity attacks =================
print("[C] SOL.2/SOL.3 monotonicity attacks (dense grids)")
bad = []
x = mp.mpf('0.01')
while x <= 40:
    if mp.diff(h2, x) >= 0:
        bad.append(('h2\'', x))
    if mp.diff(h3, x) >= 0:
        bad.append(('h3\'', x))
    Fx = x * mp.cosh(x) + 2 * x - 3 * mp.sinh(x)
    if Fx <= 0:
        bad.append(('F', x))
    if mp.diff(a_fun, x) <= 0:
        bad.append(('a\'', x))
    if mp.diff(b_fun, x) <= 0:
        bad.append(('b\'', x))
    y = x / 2
    br = 2 * mp.sinh(y)**2 + 3 - 3 * y * mp.coth(y)
    if br <= 0:
        bad.append(('bracket', x))
    x += mp.mpf('0.05') if x < 10 else mp.mpf('0.25')
chk("h2'<0, h3'<0, F>0, a'>0, b'>0, bracket>0 on grid (0.01..40] "
    "(%d violations)" % len(bad), len(bad) == 0)

# ================= [D] second-derivative sups =================
print("[D] SOL.5 (17): sup |h_n''| on [0, 40] (dense scan)")
sup2 = sup3 = sup4 = mp.mpf(0)
arg2 = arg3 = arg4 = None
x = mp.mpf('0.02')
while x <= 40:
    v2 = abs(mp.diff(h2, x, 2))
    v3 = abs(mp.diff(h3, x, 2))
    v4 = abs(mp.diff(h4, x, 2))
    if v2 > sup2:
        sup2, arg2 = v2, x
    if v3 > sup3:
        sup3, arg3 = v3, x
    if v4 > sup4:
        sup4, arg4 = v4, x
    x += mp.mpf('0.02') if x < 12 else mp.mpf('0.1')
print("  observed sup|h2''| = %s at x = %s" % (mp.nstr(sup2, 8), mp.nstr(arg2, 6)))
print("  observed sup|h3''| = %s at x = %s" % (mp.nstr(sup3, 8), mp.nstr(arg3, 6)))
print("  observed sup|h4''| = %s at x = %s" % (mp.nstr(sup4, 8), mp.nstr(arg4, 6)))
chk("M_2 < 1 claim consistent (observed %s)" % mp.nstr(sup2, 6), sup2 < 1)
chk("M_3 < 4 claim consistent (observed %s)" % mp.nstr(sup3, 6), sup3 < 4)
chk("M_4 < 20 claim consistent (observed %s)" % mp.nstr(sup4, 6), sup4 < 20)
chk("h2''(0+) -> -1/6 (got %s)" % mp.nstr(mp.diff(h2, mp.mpf('1e-4'), 2), 8),
    abs(mp.diff(h2, mp.mpf('1e-4'), 2) + mp.mpf(1) / 6) < 1e-6)

# ================= [E] G_n formula =================
print("[E] SOL.4 (13): G_n series vs quadrature; guard G_4(4)")
for (n, w) in [(2, 4), (2, 20), (3, 5), (3, 40), (4, 4), (4, 10)]:
    direct = mp.factorial(n - 1) * w - mp.quad(
        {2: h2, 3: h3, 4: h4}[n], [0, w])
    series = G_n(n, mp.mpf(w))
    chk("G_%d(%d): series vs quadrature (err %.1e)"
        % (n, w, float(abs(direct - series))),
        abs(direct - series) < mp.mpf(10)**-18)
G44 = G_n(4, mp.mpf(4))
chk("campaign guard G_4(4) = 0.2323483 (got %s)" % mp.nstr(G44, 8),
    abs(G44 - mp.mpf('0.2323483')) < mp.mpf('5e-8'))
tail = mp.nsum(lambda nu: mp.e**(-4 * nu) * En(4, 4 * nu) / nu**2, [33, mp.inf])
print("  tail sum_{nu>=33} e^{-4nu}E_4(4nu)/nu^2 = %s (negligible)"
      % mp.nstr(tail, 4))
chk("nu=32 truncation harmless (tail < 1e-40)", tail < mp.mpf(10)**-40)

# ================= [F] representation residuals =================
print("[F] SOL.5 (15): residual eps_n vs claimed w lam^2 M_n / 12")
M_claim = {2: 1, 3: 4, 4: 20}
for (m_, w_) in [(561, mp.mpf(5)), (561, mp.mpf(40)), (1000, mp.mpf(17))]:
    lam_ = w_ / m_
    for n in (2, 3, 4):
        hh = {2: h2, 3: h3, 4: h4}[n]
        D = w_ * hh(lam_) - lam_ * mp.nsum(lambda j: hh(j * lam_), [1, m_],
                                           method='direct')
        main = G_n(n, w_) + w_ * (hh(lam_) - mp.factorial(n - 1)) \
            - lam_ / 2 * (hh(w_) - mp.factorial(n - 1))
        eps = D - main
        bound = w_ * lam_**2 * M_claim[n] / 12
        chk("(m=%d, w=%s) n=%d: |eps|=%.2e <= claimed bound %.2e"
            % (m_, mp.nstr(w_, 4), n, float(abs(eps)), float(bound)),
            abs(eps) <= bound)

# ================= [G] band-table falsification scan =================
print("[G] SOL.6 table: dense (w, lam) scan of L_2, U_3/L_2, U_4/L_2")
bands = [
    (mp.mpf(4),  mp.mpf(5),  mp.mpf('1.15'),  mp.mpf('0.900'), mp.mpf('0.680'), mp.mpf('1/512')),
    (mp.mpf(5),  mp.mpf(6),  mp.mpf('1.90'),  mp.mpf('1.090'), mp.mpf('1.250'), mp.mpf('1/512')),
    (mp.mpf(6),  mp.mpf(8),  mp.mpf('2.75'),  mp.mpf('1.370'), mp.mpf('2.400'), mp.mpf('1/256')),
    (mp.mpf(8),  mp.mpf(10), mp.mpf('4.65'),  mp.mpf('1.550'), mp.mpf('3.260'), mp.mpf('1/256')),
    (mp.mpf(10), mp.mpf(20), mp.mpf('6.60'),  mp.mpf('1.850'), mp.mpf('4.980'), mp.mpf('1/64')),
    (mp.mpf(20), mp.mpf(40), mp.mpf('16.50'), mp.mpf('1.970'), mp.mpf('5.650'), mp.mpf('1/64')),
]
mp.mp.dps = 25
for (wlo, whi, L2f, c31, c42, step) in bands:
    minL2 = mp.mpf('1e50')
    max31 = mp.mpf('-1e50')
    max42 = mp.mpf('-1e50')
    arg31 = arg42 = argL2 = None
    w = wlo
    while w <= whi + step / 2:
        wc = min(w, whi)
        Gv2, Gv3, Gv4 = G_n(2, wc), G_n(3, wc), G_n(4, wc)
        h2w, h3w, h4w = h2(wc), h3(wc), h4(wc)
        lam_max = wc / 561
        for frac in (0, mp.mpf(1)/3, mp.mpf(2)/3, 1):
            lam = lam_max * frac
            h2l = h2(lam) if lam > 0 else mp.mpf(1)
            h3l = h3(lam) if lam > 0 else mp.mpf(2)
            h4l = h4(lam) if lam > 0 else mp.mpf(6)
            L2 = Gv2 + wc * (h2l - 1) - lam / 2 * (h2w - 1) - wc * lam**2 / 12
            U3 = Gv3 + wc * (h3l - 2) - lam / 2 * (h3w - 2) + wc * lam**2 / 3
            U4 = Gv4 + wc * (h4l - 6) - lam / 2 * (h4w - 6) + 5 * wc * lam**2 / 3
            if L2 < minL2:
                minL2, argL2 = L2, (wc, lam)
            if U3 / L2 > max31:
                max31, arg31 = U3 / L2, (wc, lam)
            if U4 / L2 > max42:
                max42, arg42 = U4 / L2, (wc, lam)
        w += step
    print("  band [%s, %s]: min L2 = %s (at w=%s), max U3/L2 = %s, "
          "max U4/L2 = %s" % (mp.nstr(wlo, 4), mp.nstr(whi, 4),
                              mp.nstr(minL2, 8), mp.nstr(argL2[0], 6),
                              mp.nstr(max31, 8), mp.nstr(max42, 8)))
    chk("    claimed floor %s <= observed min L2" % mp.nstr(L2f, 6),
        L2f <= minL2)
    chk("    observed max U3/L2 < claimed ceiling %s (margin %.2f%%)"
        % (mp.nstr(c31, 6), float((c31 - max31) / max31 * 100)), max31 < c31)
    chk("    observed max U4/L2 < claimed ceiling %s (margin %.2f%%)"
        % (mp.nstr(c42, 6), float((c42 - max42) / max42 * 100)), max42 < c42)
mp.mp.dps = 30

# ================= [H] W7 geometric values =================
print("[H] SOL.8: a(0.89), b(0.89) enclosures")
mp.mp.dps = 50
a89 = a_fun(mp.mpf('0.89'))
b89 = b_fun(mp.mpf('0.89'))
print("  a(0.89) = %s" % mp.nstr(a89, 20))
print("  b(0.89) = %s" % mp.nstr(b89, 20))
chk("(26): 2.1302 < a(0.89) < 2.1304",
    mp.mpf('2.1302') < a89 < mp.mpf('2.1304'))
chk("(27): 6.4111 < b(0.89) < 6.4114",
    mp.mpf('6.4111') < b89 < mp.mpf('6.4114'))
chk("plan geo limits 2.13031/6.41126 consistent",
    abs(a89 - mp.mpf('2.13031')) < mp.mpf('5e-6')
    and abs(b89 - mp.mpf('6.41126')) < mp.mpf('5e-6'))
chk("a(0.89) < 2.71 target", a89 < mp.mpf('2.71'))
chk("b(0.89) < 8.17 target", b89 < mp.mpf('8.17'))
mp.mp.dps = 30

# ================= [I] sentinels =================
print("[I] V1 sentinels at m = 561 (exact factor sums, dps 30)")
sentinels = [(5, '0.88636', '0.65065'), (6, '1.0739', '1.2058'),
             (8, '1.3485', '2.3075'), (10, '1.5184', '3.1636'),
             (20, '1.8036', '4.8206'), (40, '1.9114', '5.4653')]
m0 = 561
for (w_, s31, s42) in sentinels:
    lam = mp.mpf(w_) / m0
    k2 = kappa_n(2, m0, lam)
    k3 = kappa_n(3, m0, lam)
    k4 = kappa_n(4, m0, lam)
    r31 = lam * abs(k3) / k2
    r42 = lam**2 * k4 / k2
    e31 = abs(r31 - mp.mpf(s31))
    e42 = abs(r42 - mp.mpf(s42))
    print("  w=%2d: r31 = %s (table %s), r42 = %s (table %s)"
          % (w_, mp.nstr(r31, 7), s31, mp.nstr(r42, 7), s42))
    chk("    matches draft/plan to quoted digits", e31 < mp.mpf('5e-5')
        and e42 < mp.mpf('5e-5'))
# W7 finite-m point vs plan
lam = mp.mpf('0.89')
k2 = kappa_n(2, m0, lam)
k3 = kappa_n(3, m0, lam)
k4 = kappa_n(4, m0, lam)
r31_w7 = lam * abs(k3) / k2
r42_w7 = lam**2 * k4 / k2
print("  (561, lam=0.89): r31 = %s (plan 2.12402), r42 = %s (plan 6.3713)"
      % (mp.nstr(r31_w7, 7), mp.nstr(r42_w7, 7)))
chk("  W7 finite-m point matches plan", abs(r31_w7 - mp.mpf('2.12402')) < mp.mpf('5e-5')
    and abs(r42_w7 - mp.mpf('6.3713')) < mp.mpf('5e-4'))
chk("  W7 finite-m below geometric limit (SOL.3/SOL.8 domination)",
    r31_w7 < a89 and r42_w7 < b89)

# ================= [J] interface & arithmetic =================
print("[J] interface with the re-architected chain")
targets31 = [mp.mpf(t) for t in
             ('1.19', '1.44', '1.82', '2.04', '2.38', '2.56', '2.71')]
targets42 = [mp.mpf(t) for t in
             ('0.87', '1.62', '3.11', '4.27', '6.38', '7.33', '8.17')]
ceil31 = [mp.mpf(t) for t in
          ('0.900', '1.090', '1.370', '1.550', '1.850', '1.970')] + [a89]
ceil42 = [mp.mpf(t) for t in
          ('0.680', '1.250', '2.400', '3.260', '4.980', '5.650')] + [b89]
names = ['W1', 'W2', 'W3', 'W4', 'W5', 'W6b', 'W7']
for i in range(7):
    chk("%s: proved ceilings (%s, %s) < targets (%s, %s)"
        % (names[i], mp.nstr(ceil31[i], 6), mp.nstr(ceil42[i], 6),
           mp.nstr(targets31[i], 4), mp.nstr(targets42[i], 4)),
        ceil31[i] < targets31[i] and ceil42[i] < targets42[i])
chk("e^{-4} < 1/54 (e^4 = %s)" % mp.nstr(mp.e**4, 8), mp.e**4 > 54)
z_lo = mp.mpf(16449340668482264) / mp.mpf(10)**16
z_hi = mp.mpf(16449340668482265) / mp.mpf(10)**16
chk("(24): zeta(2) enclosure valid", z_lo < mp.zeta(2) < z_hi)
chk("chain: 0.978293 * 20 = 19.56586 -> 19.5659 <= 20",
    abs(mp.mpf('0.978293') * 20 - mp.mpf('19.56586')) < mp.mpf('1e-10')
    and mp.mpf('0.978293') * 20 <= 20)
chk("chain (m>=1581): 0.75839 * 20 = 15.1678 <= 136",
    abs(mp.mpf('0.75839') * 20 - mp.mpf('15.1678')) < mp.mpf('1e-10'))
chk("(S2)-fallback W7 targets 2.42/7.28 ALSO cleared by geometric bound",
    a89 < mp.mpf('2.42') and b89 < mp.mpf('7.28'))

# ================= [K] direct truth attack on (S1-new) =================
print("[K] adversarial truth attack on (S1-new) itself")
mp.mp.dps = 25
viol = 0
tested = 0


def band_index(w):
    if w <= 5:
        return 0
    if w <= 6:
        return 1
    if w <= 8:
        return 2
    if w <= 10:
        return 3
    if w <= 20:
        return 4
    if w <= 40:
        return 5
    return 6


ws = [mp.mpf(t) for t in ('4.001', '4.5', '5', '5.5', '6', '7', '8', '9',
                          '10', '15', '20', '30', '40')]
for m_ in (561, 562, 599, 700, 1000, 2500):
    for w_ in ws:
        lam = w_ / m_
        k2 = kappa_n(2, m_, lam)
        k3 = kappa_n(3, m_, lam)
        k4 = kappa_n(4, m_, lam)
        r31 = lam * abs(k3) / k2
        r42 = lam**2 * k4 / k2
        i = band_index(w_)
        tested += 1
        if r31 > targets31[i] or r42 > targets42[i]:
            viol += 1
            print("  VIOLATION at m=%d, w=%s: r31=%s, r42=%s"
                  % (m_, mp.nstr(w_, 5), mp.nstr(r31, 8), mp.nstr(r42, 8)))
# W7 attacks (large lam)
for m_ in (561, 1000, 3000):
    for lam_s in ('0.3', '0.5', '0.7', '0.89'):
        lam = mp.mpf(lam_s)
        if m_ * lam <= 40:
            continue
        k2 = kappa_n(2, m_, lam)
        k3 = kappa_n(3, m_, lam)
        k4 = kappa_n(4, m_, lam)
        r31 = lam * abs(k3) / k2
        r42 = lam**2 * k4 / k2
        tested += 1
        if r31 > targets31[6] or r42 > targets42[6]:
            viol += 1
            print("  VIOLATION at m=%d, lam=%s: r31=%s, r42=%s"
                  % (m_, lam_s, mp.nstr(r31, 8), mp.nstr(r42, 8)))
chk("(S1-new) truth attack: 0 violations in %d probes" % tested, viol == 0)

print()
print("ALL CHECKS OK:", ALL_OK)
