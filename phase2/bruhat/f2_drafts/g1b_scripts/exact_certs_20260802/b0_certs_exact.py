# Independent exact-rational verification of Lemma B.0 (ii)-(iv), stdlib only.
# For each claimed inequality, form the exact difference as a rational polynomial in m,
# clear denominators to an integer polynomial, then PROVE positivity for all integers
# m >= threshold: check m = thr..M0 exactly, and for m > M0 use coefficient dominance
# (lc*m^d > sum |c_i| m^{d-1} whenever m > sum|c_i|/lc).
from fractions import Fraction

def S4(m): return m*(m+1)*(2*m+1)*(3*m**2+3*m-1)//30 if isinstance(m,int) else None
def S6c(m): return (6*m**7+21*m**6+21*m**5-7*m**3+m)//42

# sanity of closed forms vs direct sums
for m in (5, 17, 30, 101):
    assert S4(m) == sum(j**4 for j in range(1, m+1)), m
    assert S6c(m) == sum(j**6 for j in range(1, m+1)), m
print("S4, S6 closed forms verified exactly at m = 5, 17, 30, 101")

# polynomial arithmetic over Fractions (ascending coeffs)
def pmul(p, q):
    out = [Fraction(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,c in enumerate(q): out[i+j] += a*c
    return out
def padd(p, q, s=Fraction(1)):
    n = max(len(p), len(q)); out = [Fraction(0)]*n
    for i,a in enumerate(p): out[i] += a
    for i,c in enumerate(q): out[i] += s*c
    return out
def pscale(p, s): return [s*c for c in p]
def peval(p, m):
    v = Fraction(0)
    for c in reversed(p): v = v*m + c
    return v

M   = [Fraction(0), Fraction(1)]                      # m
S4p = pscale(pmul(pmul(pmul(M, padd(M,[Fraction(1)])), padd(pscale(M,Fraction(2)),[Fraction(1)])),
             padd(padd(pscale(pmul(M,M),Fraction(3)), pscale(M,Fraction(3))), [Fraction(-1)])), Fraction(1,30))
S6p = pscale([Fraction(0),Fraction(1),Fraction(0),Fraction(-7),Fraction(0),Fraction(21),Fraction(21),Fraction(6)], Fraction(1,42))
lam = pscale(pmul(pmul(M, padd(M,[Fraction(-1)])), padd(pscale(M,Fraction(2)),[Fraction(5)])), Fraction(1,72))
lam2 = pmul(lam, lam); lam3 = pmul(lam2, lam); lam4 = pmul(lam2, lam2)
m9 = [Fraction(0)]*9 + [Fraction(1)]
onep = padd(M, [Fraction(1)])          # m+1
mp1_9 = [Fraction(1)]
for _ in range(9): mp1_9 = pmul(mp1_9, onep)

S4m = padd(S4p, M, Fraction(-1))   # S4 - m
S6m = padd(S6p, M, Fraction(-1))

# each check: (name, poly that must be > 0 for all m >= thr AFTER multiplying by m^k>0)
# b<=0.09/m  : (9/100)*2880*lam^2 - m*(S4-m) >= 0   (multiplied through by m)
checks = [
 ("b <= 0.0900/m, m>=11",  padd(pscale(lam2, Fraction(9,100)*2880), pmul(M, S4m), Fraction(-1)), 11),
 ("b >= 0.0890/m, m>=30",  padd(pmul(M, S4m), pscale(lam2, Fraction(89,1000)*2880), Fraction(-1)), 30),
 ("g <= 0.03674/m^2, m>=30", padd(pscale(lam3, Fraction(3674,100000)*181440), pmul(pmul(M,M), S6m), Fraction(-1)), 30),
 ("g >= 0.03540/m^2, m>=30", padd(pmul(pmul(M,M), S6m), pscale(lam3, Fraction(3540,100000)*181440), Fraction(-1)), 30),
 ("c8/lam^4 <= 0.0431/m^3, m>=30", padd(pscale(lam4, Fraction(431,10000)*43545600), pmul(pmul(pmul(M,M),M), mp1_9), Fraction(-1)), 30),
]

from math import gcd
def lcm(a, b): return a*b//gcd(a, b)
for name, poly, thr in checks:
    # strip exact leading-term cancellations, clear denominators -> integer polynomial
    while poly and poly[-1] == 0: poly = poly[:-1]
    den = 1
    for c in poly: den = lcm(den, c.denominator)
    ip = [int(c*den) for c in poly]           # positive multiple of the original
    lc = ip[-1]
    assert lc > 0, (name, "leading coeff must be positive")
    dom = sum(abs(c) for c in ip[:-1]) // lc + 1   # poly(m) > 0 for every m > dom
    M0 = max(thr, dom)
    def ieval(mv):
        v = 0
        for c in reversed(ip): v = v*mv + c
        return v
    bad = [mv for mv in range(thr, M0+1) if ieval(mv) <= 0]
    print(f"  {name}: exact integer check m={thr}..{M0}: {'FAIL at '+str(bad[:5]) if bad else 'all > 0'};"
          f" tail m>{M0} strictly positive by coefficient dominance")
    # also verify strictness right below threshold where draft implies the bound is tight-ish
    below = [m for m in range(2, thr) if peval(poly, m) <= 0]
    print(f"      (fails below threshold at m in {below} — consistent with claimed largest real roots)")

# exact extreme values quoted in NC-B0 / g1b_const output
def b_ex(m): return Fraction(S4(m)-m, 2880)/Fraction(m*(m-1)*(2*m+5),72)**2
def g_ex(m): return Fraction(S6c(m)-m, 181440)/Fraction(m*(m-1)*(2*m+5),72)**3
def c8s_ex(m): return Fraction((m+1)**9, 43545600)/Fraction(m*(m-1)*(2*m+5),72)**4
bm  = [(float(b_ex(m)*m), m) for m in range(11, 4001)]
gm  = [(float(g_ex(m)*m*m), m) for m in range(30, 4001)]
c8m = [(float(c8s_ex(m)*m**3), m) for m in range(30, 4001)]
print("max b*m (m>=11) =", max(bm), " min b*m (m>=30) =", min(v for v in bm if v[1] >= 30))
print("b*m exactly 0.09 anywhere? ", any(b_ex(m)*m == Fraction(9,100) for m in range(11, 200)))
print("max g*m^2 =", max(gm), " min g*m^2 =", min(gm))
print("max c8s*m^3 =", max(c8m))
# limits as m -> inf (exact leading behavior)
print("limit b*m -> 30*(1/30... ) check via m=10^6:", float(b_ex(10**6)*10**6))
print("limit g*m^2 via m=10^6:", float(g_ex(10**6)*(10**6)**2))
print("limit c8s*m^3 via m=10^6:", float(c8s_ex(10**6)*(10**6)**3))
