# From-scratch exact check of the model constants via the Mahonian generating function
# prod_{j=1}^m (1+q+...+q^{j-1})  (equivalently prod (1-q^j)/(1-q)).
# Verifies, in exact rational arithmetic:
#   variance  kappa_2 = lambda = m(m-1)(2m+5)/72
#   kappa_4   = -(S4 - m)/120      (so beta := -kappa_4/24 = (S4-m)/2880 > 0)
#   kappa_6   =  (S6 - m)/252      (so gamma := kappa_6/720 = (S6-m)/181440 > 0)
# and the draft's B_m = 12b numbers.
import sys
from fractions import Fraction
sys.path.insert(0, "/Users/nikolsavova/Documents/GitHub/proof_hunter/phase2/bruhat")
from mahonian import mahonian
from math import factorial

for m in (6, 10, 20, 35):
    a = mahonian(m)
    N = m*(m-1)//2
    tot = factorial(m)
    assert sum(a) == tot
    mean = Fraction(sum(k*a[k] for k in range(N+1)), tot)
    assert mean == Fraction(N, 2)
    mu = {r: Fraction(sum(a[k]*(Fraction(k) - mean)**r for k in range(N+1)), tot) for r in (2, 3, 4, 5, 6)}
    assert mu[3] == 0 and mu[5] == 0  # symmetry
    k2 = mu[2]
    k4 = mu[4] - 3*mu[2]**2
    k6 = mu[6] - 15*mu[4]*mu[2] + 30*mu[2]**3
    lam = Fraction(m*(m-1)*(2*m+5), 72)
    S4 = sum(j**4 for j in range(1, m+1)); S6 = sum(j**6 for j in range(1, m+1))
    print(f"m={m}:")
    print("   kappa2 == m(m-1)(2m+5)/72        :", k2 == lam)
    print("   kappa4 == -(S4-m)/120            :", k4 == -Fraction(S4-m, 120))
    print("   kappa6 ==  (S6-m)/252            :", k6 == Fraction(S6-m, 252))
    b = Fraction(S4-m, 2880)/lam**2
    g = Fraction(S6-m, 181440)/lam**3
    print(f"   b*m = {float(b*m):.6f}   g*m^2 = {float(g*m*m):.6f}   B_m*m = 12*b*m = {float(12*b*m):.6f}")

# asymptotic center residual: (-90g + 384 b^2) * m^2 -> ?
m = 10**6
lam = Fraction(m*(m-1)*(2*m+5), 72)
S4 = m*(m+1)*(2*m+1)*(3*m**2+3*m-1)//30
S6 = (6*m**7+21*m**6+21*m**5-7*m**3+m)//42
b = Fraction(S4-m, 2880)/lam**2; g = Fraction(S6-m, 181440)/lam**3
print("asymptotic m^2*(-90g+384b^2) =", float((-90*g + 384*b*b)*m*m))
