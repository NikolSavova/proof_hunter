# Independent exact recomputation of Lemma B.7's N(y) monomial table, stdlib only.
# Polynomials in y over Q, coefficients organized by monomials b^i g^j.
# P = 1 - b*He4 + g*He6 + (b^2/2)*He8 ;  N = -P''*P + P'^2 - 12*b*He2*P^2.
from fractions import Fraction

# y-polynomials as ascending coeff lists of Fractions
def pmul(p, q):
    out = [Fraction(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, c in enumerate(q):
            out[i + j] += a * c
    return out

def padd(p, q, s=Fraction(1)):
    n = max(len(p), len(q))
    out = [Fraction(0)] * n
    for i, a in enumerate(p): out[i] += a
    for i, c in enumerate(q): out[i] += s * c
    return out

def pdiff(p):
    return [p[i] * i for i in range(1, len(p))] or [Fraction(0)]

# probabilists' Hermite via He_{k+1} = y He_k - k He_{k-1}
He = {0: [Fraction(1)], 1: [Fraction(0), Fraction(1)]}
for k in range(1, 10):
    He[k + 1] = padd(pmul([Fraction(0), Fraction(1)], He[k]), He[k - 1], Fraction(-k))

assert [int(c) for c in He[4]] == [3, 0, -6, 0, 1]
assert [int(c) for c in He[6]] == [-15, 0, 45, 0, -15, 0, 1]
assert [int(c) for c in He[8]] == [105, 0, -420, 0, 210, 0, -28, 0, 1]

# bivariate-in-(b,g) polynomials: dict {(i,j): y-poly}
def bgmul(A, B):
    out = {}
    for (i1, j1), p in A.items():
        for (i2, j2), q in B.items():
            key = (i1 + i2, j1 + j2)
            r = pmul(p, q)
            out[key] = padd(out[key], r) if key in out else r
    return out

def bgadd(A, B, s=Fraction(1)):
    out = {k: list(v) for k, v in A.items()}
    for k, q in B.items():
        out[k] = padd(out[k], q, s) if k in out else [s * c for c in q]
    return out

def bgdiff(A):
    return {k: pdiff(p) for k, p in A.items()}

P = {(0, 0): [Fraction(1)],
     (1, 0): [-c for c in He[4]],
     (0, 1): list(He[6]),
     (2, 0): [c / 2 for c in He[8]]}
Pp = bgdiff(P)
Ppp = bgdiff(Pp)

N = bgadd(bgadd({k: [-c for c in p] for k, p in bgmul(Ppp, P).items()}, bgmul(Pp, Pp)),
          bgmul({(1, 0): [12 * c for c in He[2]]}, bgmul(P, P)), Fraction(-1))

# drop zero entries
def clean(A):
    out = {}
    for k, p in A.items():
        while p and p[-1] == 0: p = p[:-1]
        if any(c != 0 for c in p): out[k] = p
    return out
N = clean(N)

# The draft's table, descending powers of y (only even powers present)
draft = {
 (0,1): [-30,0,180,0,-90],
 (0,2): [6,0,-90,0,540,0,-900,0,1350,0,1350],
 (1,1): [-30,0,456,0,-1620,0,1800,0,90],
 (1,2): [-12,0,372,0,-4140,0,20340,0,-46260,0,45900,0,-18900,0,2700],
 (2,0): [240,0,-1008,0,384],
 (2,1): [29,0,-666,0,5121,0,-16692,0,21195,0,-15930,0,-9945],
 (3,0): [-22,0,510,0,-3588,0,8916,0,-7470,0,-522],
 (3,1): [-12,0,528,0,-8616,0,66240,0,-253440,0,478800,0,-415800,0,151200,0,-18900],
 (4,0): [14,0,-490,0,5946,0,-31830,0,79338,0,-83790,0,48510,0,18270],
 (5,0): [-3,0,171,0,-3780,0,41412,0,-241290,0,750330,0,-1208340,0,926100,0,-297675,0,33075],
}
draft = {k: [Fraction(c) for c in reversed(v)] for k, v in draft.items()}  # ascending

print("monomials found:", sorted(N.keys()))
print("b-linear (1,0) coeff present?", (1, 0) in N, "(draft claims it cancels identically)")
ok = True
for k in sorted(set(N) | set(draft)):
    a = N.get(k, [Fraction(0)])
    d = draft.get(k, [Fraction(0)])
    n = max(len(a), len(d))
    a = a + [Fraction(0)] * (n - len(a)); d = d + [Fraction(0)] * (n - len(d))
    same = a == d
    ok &= same
    print(f"  b^{k[0]} g^{k[1]}: match = {same}")
print("FULL TABLE MATCH:", ok)

# structural fact 2: b^2 coeff == 16 He3^2 + 12 He2 He4 - 28 He6  (collapses to quartic)
q = padd(padd(pmul([16*c for c in He[3]], He[3]), pmul([12*c for c in He[2]], He[4])), [Fraction(-28)*c for c in He[6]])
while q and q[-1] == 0: q = q[:-1]
print("b^2 coeff == 16He3^2+12He2He4-28He6:", q == N[(2, 0)], "; equals quartic 384-1008y^2+240y^4:",
      q == [Fraction(384), Fraction(0), Fraction(-1008), Fraction(0), Fraction(240)])
# center value N(0) = -90 g + 384 b^2 + higher
print("N(0) monomials:", {k: p[0] for k, p in N.items() if p[0] != 0})
