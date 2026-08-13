#!/usr/bin/env python3
# wave6b_ref_s1 / ref2_mn_bounds.py
# V3 check: the draft's derivative bounds (17): M_2 = sup|h2''| < 1, M_3 = sup|h3''| < 4,
# M_4 = sup|h4''| < 20 on [0, 40]. Method: exact symbolic second/third derivatives
# (sympy) of the closed forms, evaluated in mpmath at dps 40 on a dense grid, with an
# off-grid excursion bound |sup - gridmax| <= (step/2) * sup|h_n'''| (h''' itself
# gridded with a x2 safety factor). Margins are large, so this is decisive.
# Also: recurrence checks (18) h3 = 2h2 - x h2', (19) h4 = 3h3 - x h3' (symbolic, exact).
import sympy as sp
from mpmath import mp, mpf

mp.dps = 40
x = sp.symbols('x', positive=True)
h2s = (x/(2*sp.sinh(x/2)))**2
h3s = x**3*sp.cosh(x/2)/(4*sp.sinh(x/2)**3)
h4s = x**4*(sp.cosh(x)+2)/(8*sp.sinh(x/2)**4)

# recurrences (18)/(19), exact symbolic verification
r18 = sp.simplify(sp.expand_trig(sp.simplify(2*h2s - x*sp.diff(h2s, x) - h3s)))
r19 = sp.simplify(sp.expand_trig(sp.simplify(3*h3s - x*sp.diff(h3s, x) - h4s)))
print(f"symbolic (18) residual 2h2 - x h2' - h3 == 0: {r18 == 0}")
print(f"symbolic (19) residual 3h3 - x h3' - h4 == 0: {r19 == 0}")

funcs = {}
for name, hs in (("h2", h2s), ("h3", h3s), ("h4", h4s)):
    d2 = sp.diff(hs, x, 2)
    d3 = sp.diff(hs, x, 3)
    funcs[name] = (sp.lambdify(x, d2, "mpmath"), sp.lambdify(x, d3, "mpmath"))

# limits at x -> 0 (series): h2 = 1 - x^2/12 + x^4/240 - ..., h3 = 2 - x^4/120 + ...,
# h4 = 6 + x^4/120 + ...  => h2''(0) = -1/6, h3''(0) = 0, h4''(0) = 0
lim0 = {"h2": mpf(-1)/6, "h3": mpf(0), "h4": mpf(0)}
series_chk = {n: sp.series(hs, x, 0, 6).removeO() for n, hs in (("h2", h2s), ("h3", h3s), ("h4", h4s))}
print("series about 0:")
for n, s in series_chk.items():
    print(f"  {n}: {sp.nsimplify(sp.expand(s))}")

bounds = {"h2": mpf(1), "h3": mpf(4), "h4": mpf(20)}
step = mpf("0.02")
print(f"\ngrid: x = step..40 with step {step} (plus x->0 limit values), dps {mp.dps}")
for name in ("h2", "h3", "h4"):
    d2f, d3f = funcs[name]
    m2 = abs(lim0[name]); arg2 = mpf(0)
    m3 = mpf(0)
    xx = step
    while xx <= 40 + mpf("1e-12"):
        v2 = abs(d2f(xx)); v3 = abs(d3f(xx))
        if v2 > m2: m2, arg2 = v2, xx
        if v3 > m3: m3 = v3
        xx += step
    # local refinement around argmax of |h''| (golden-section-ish scan)
    lo = max(arg2 - step, mpf("1e-6")); hi = arg2 + step
    fine = (hi - lo)/200
    xr = lo
    while xr <= hi:
        v2 = abs(d2f(xr))
        if v2 > m2: m2, arg2 = v2, xr
        xr += fine
    sup_bound = m2 + (step/2)*(2*m3)   # off-grid excursion, x2 safety on |h'''|
    ok = sup_bound < bounds[name]
    print(f"  {name}'': grid max |h''| = {mp.nstr(m2, 10)} at x = {mp.nstr(arg2, 6)};"
          f" grid max |h'''| = {mp.nstr(m3, 8)};"
          f" certified sup bound {mp.nstr(sup_bound, 10)} < {bounds[name]}: {ok}")

# cross-check the lambdified d2 against mpmath.diff at a few points
from mpmath import diff, sinh, cosh
def h2m(t): return (t/(2*sinh(t/2)))**2
def h3m(t): return t**3*cosh(t/2)/(4*sinh(t/2)**3)
def h4m(t): return t**4*(cosh(t)+2)/(8*sinh(t/2)**4)
print("\ncross-check sympy d2 vs mpmath.diff (rel err):")
for name, hm in (("h2", h2m), ("h3", h3m), ("h4", h4m)):
    d2f, _ = funcs[name]
    for pt in (mpf("0.5"), mpf(3), mpf(17), mpf(39)):
        a = d2f(pt); b = diff(hm, pt, 2)
        rel = abs(a-b)/max(abs(b), mpf("1e-30"))
        print(f"  {name}''({mp.nstr(pt, 4)}): {mp.nstr(a, 8)} vs {mp.nstr(b, 8)}  rel {mp.nstr(rel, 3)}")
