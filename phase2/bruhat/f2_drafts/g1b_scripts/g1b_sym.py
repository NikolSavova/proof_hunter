# Exact symbolic computation of the main-term polynomial N(y) for g1_draft_b.
# P(y) = 1 - b*He4 + g*He6 + (b^2/2)*He8
# N := -P''*P + (P')^2 - 12*b*He2*P^2   (so that  -(log P)'' - 12 b He2 = N/P^2)
import sympy as sp

y, b, g = sp.symbols('y b g')
def He(n):
    return sp.simplify(2**sp.Rational(-n,2)*sp.hermite(n, y/sp.sqrt(2)))

He2, He3, He4, He6, He8 = [sp.expand(He(n)) for n in (2,3,4,6,8)]
P  = 1 - b*He4 + g*He6 + sp.Rational(1,2)*b**2*He8
Pp = sp.diff(P, y); Ppp = sp.diff(P, y, 2)
N  = sp.expand(-Ppp*P + Pp**2 - 12*b*He2*P**2)

# collect by monomials in (b,g)
poly = sp.Poly(N, b, g)
print("monomials of N in (b,g):")
for mono, coeff in poly.terms():
    i, j = mono
    c = sp.factor(sp.expand(coeff))
    print(f"  b^{i} g^{j} :", sp.expand(coeff))
# sanity: b^1 coefficient must vanish
print("\ncheck b-linear coeff == 0:", sp.simplify(poly.coeff_monomial(b)) == 0)
# b^2 coefficient vs 16He3^2+12He2He4-28He6
Q = sp.expand(16*He3**2 + 12*He2*He4 - 28*He6)
print("check b^2 coeff == 16He3^2+12He2He4-28He6:", sp.expand(poly.coeff_monomial(b**2) - Q) == 0)
print("Q(0) =", Q.subs(y,0), "   -30*He4(0) =", -30*He4.subs(y,0))
