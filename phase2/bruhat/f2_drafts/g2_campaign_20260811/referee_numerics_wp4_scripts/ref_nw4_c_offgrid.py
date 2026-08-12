#!/usr/bin/env python3
"""REF-C: adversarial off-grid attacks on the delivered wp4 statements.
 C1: SL2/A2(ii) truth floor A/m >= c_A(W): band-left-edge corners (w = w0 +
     {1e-9, 1e-4, 1e-2}) and W7 deep corner (lam -> 0.89), for
     m in {401, 402, 403, 407, 499, 1000, 5000, 100000}; min margin per m.
 C2: Lemma C.1 (A <= m h(lam) < m): max of A/(m h) over adversarial grid.
 C3: SL2 bonus s2 > m: worst s2/m on W7 incl. lam = 0.89 exactly, m = 401.
 C4: (H1) deep-corner measurement NC-PL1's grid MISSED: R31, R42 at m = 401,
     lam in {0.63, 0.70, 0.75, 0.80, 0.85, 0.88, 0.89} (w in W7) vs the
     architected R31* = 2.2, R42* = 6.6; plus the geometric-limit values.
 C5: Theorem SL3.1 scope attack (claimed for ALL m >= 2): measured
     min -log|phi|/(s2 t^2) on (0, 0.8 lam] vs c1 and on (0, 1.074 lam]
     vs c2, m in {2, 3, 5, 10, 30}, lam in {0.1, 0.45, 0.89}; direct
     complex-sum |phi| (independent of the SL3 scripts' closed form).
 C6: Lemma SL3.D/SL3.A attack: exact eps_j(b) at b = pi/(0.8 lam) and
     b = pi/(1.074 lam) vs the certificate values 0.35 / 0.57 over an
     adversarial (lam, j) sweep incl. j = 2, 3 and j = 2000.
 C7: the composite's refutation-robustness note: honest mid entry at
     gamma = c1 = 0.1317175 (A3's actual constant, not 1/8) at W1.
"""
import math

def q_of(lam): return math.exp(-lam)

def var_uj(j, lam):
    q = q_of(lam)
    if j == 1: return 0.0
    return q / (1 - q) ** 2 - j * j * q ** j / (1 - q ** j) ** 2

def s2_of(m, lam): return sum(var_uj(j, lam) for j in range(1, m + 1))

C_A = [(4, 5, 0.28), (5, 6, 0.35), (6, 8, 0.42), (8, 10, 0.52),
       (10, 20, 0.60), (20, 40, 0.70), (40, float('inf'), 0.80)]

print("C1: SL2 truth floor attack, min (A/m - c_A) per m over corner points")
for m in (401, 402, 403, 407, 499, 1000, 5000, 100000):
    worst = (1e9, None)
    pts = []
    for lo, hi, cA in C_A:
        for dw in (1e-9, 1e-4, 1e-2):
            w = lo + dw
            if w / m <= 0.89:
                pts.append((w, cA))
    # W7 deep corner: lam near 0.89
    for lam in (0.87, 0.88, 0.885, 0.889, 0.89):
        if m * lam > 40:
            pts.append((m * lam, 0.80))
    for w, cA in pts:
        lam = w / m
        A = lam * lam * s2_of(m, lam)
        marg = A / m - cA
        if marg < worst[0]: worst = (marg, w)
    print(f"   m={m:6d}: min margin = {worst[0]:+.5f} at w = {worst[1]:.5f}"
          f"   {'OK' if worst[0] > 0 else 'VIOLATION'}")

print("C2: Lemma C.1 attack: max A/(m h(lam)), h = (lam/2)^2/sinh^2(lam/2)")
mx = (0.0, None)
for m in (401, 500, 1000, 5000):
    for i in range(1, 200):
        lam = 0.89 * i / 199
        if m * lam <= 4: continue
        h = (lam / 2) ** 2 / math.sinh(lam / 2) ** 2
        r = lam * lam * s2_of(m, lam) / (m * h)
        if r > mx[0]: mx = (r, (m, lam))
print(f"   max A/(m h) = {mx[0]:.6f} at (m, lam) = {mx[1]}   (must be <= 1)")

print("C3: s2/m on W7 at m = 401 (bonus min(m,s2) = m margin)")
for lam in (0.0998, 0.2, 0.4, 0.6, 0.8, 0.89):
    s2 = s2_of(401, lam)
    print(f"   lam = {lam:5.4f} (w = {401*lam:7.2f}): s2/m = {s2/401:.4f}")

print("C4: (H1) W7 deep corner, m = 401 (NC-PL1's m=401 grid stops at w=250)")
def cums(m, lam):
    s2 = k3 = k4 = 0.0
    for j in range(1, m + 1):
        q = math.exp(-lam)
        ws = [q ** i for i in range(j)]
        Z = sum(ws)
        m1 = sum(i * t for i, t in enumerate(ws)) / Z
        c2 = sum((i - m1) ** 2 * t for i, t in enumerate(ws)) / Z
        c3 = sum((i - m1) ** 3 * t for i, t in enumerate(ws)) / Z
        c4 = sum((i - m1) ** 4 * t for i, t in enumerate(ws)) / Z - 3 * c2 * c2
        s2 += c2; k3 += c3; k4 += c4
    return s2, k3, k4
for lam in (0.63, 0.70, 0.75, 0.80, 0.85, 0.88, 0.89):
    s2, k3, k4 = cums(401, lam)
    R31 = abs(k3) * lam / s2
    R42 = abs(k4) * lam * lam / s2
    print(f"   lam = {lam:.2f} (w = {401*lam:6.1f}): R31 = {R31:.4f} (vs 2.2), "
          f"R42 = {R42:.4f} (vs 6.6)  headroom R42: {(6.6/R42-1)*100:.1f}%")
q89 = math.exp(-0.89)
print(f"   geometric limits at lam=0.89: R31_G = {(1+q89)*0.89/(1-q89):.4f}, "
      f"R42_G = {(1+4*q89+q89*q89)*0.89**2/(1-q89)**2:.4f}")

print("C5: SL3.1 scope attack (all m >= 2 claim): min -log|phi|/(s2 t^2)")
def absphi_direct(m, lam, t):
    # direct complex per-factor sums (independent implementation)
    tot = 0.0
    q = math.exp(-lam)
    for j in range(2, m + 1):
        re = im = Z = 0.0
        for i in range(j):
            wgt = q ** i
            Z += wgt
            re += wgt * math.cos(t * i)
            im += wgt * math.sin(t * i)
        tot += 0.5 * math.log((re * re + im * im) / (Z * Z))
    return tot  # = log |phi|
c1, c2 = 0.1317175, 0.0871362
bad = 0
for m in (2, 3, 5, 10, 30):
    for lam in (0.1, 0.45, 0.89):
        s2 = s2_of(m, lam)
        mn1 = mn2 = 1e9
        for i in range(1, 201):
            t = 0.8 * lam * i / 200
            mn1 = min(mn1, -absphi_direct(m, lam, t) / (s2 * t * t))
            t = 1.074 * lam * i / 200
            mn2 = min(mn2, -absphi_direct(m, lam, t) / (s2 * t * t))
        ok = mn1 >= c1 and mn2 >= c2
        bad += 0 if ok else 1
        print(f"   m={m:2d} lam={lam:4.2f}: tier1 min = {mn1:.4f} (>= c1 {c1}: {mn1>=c1}), "
              f"tier2 min = {mn2:.4f} (>= c2 {c2}: {mn2>=c2})")
print(f"   scope-attack violations: {bad}")

print("C6: exact eps_j vs 0.35/0.57 over adversarial (lam, j) sweep")
def eps_exact(j, lam, b):
    q = q_of(lam)
    num = den = 0.0
    for d in range(1, j):
        p = q ** d * (1 - q ** (2 * (j - d)))
        den += d * d * p
        if d > b: num += d * d * p
    return num / den if den > 0 else 0.0
worst1 = worst2 = (0.0, None)
for lam in (0.001, 0.01, 0.05, 0.2, 0.45, 0.65, 0.89):
    for j in (2, 3, 5, 8, 20, 100, 401, 2000):
        e1 = eps_exact(j, lam, math.pi / (0.8 * lam))
        e2 = eps_exact(j, lam, math.pi / (1.074 * lam))
        if e1 > worst1[0]: worst1 = (e1, (lam, j))
        if e2 > worst2[0]: worst2 = (e2, (lam, j))
print(f"   max eps_j(pi/(0.8lam))  = {worst1[0]:.4f} at (lam,j)={worst1[1]}  (cert 0.35)")
print(f"   max eps_j(pi/(1.074lam))= {worst2[0]:.4f} at (lam,j)={worst2[1]}  (cert 0.57)")

print("C7: refutation robustness: honest W1 mid entry at gamma = c1 (not 1/8)")
A1 = 0.28 * 401
for gam in (0.125, 0.1317175):
    v = math.sqrt(2 * math.pi) / math.pi * A1 ** 1.5 / (2 * gam) * math.exp(-gam * A1 / 4) * (1 + 2 / (gam * A1))
    print(f"   gamma = {gam:.7f}: honest mid entry = {v:.2f}  (architected T_u slot 1.0125)")
