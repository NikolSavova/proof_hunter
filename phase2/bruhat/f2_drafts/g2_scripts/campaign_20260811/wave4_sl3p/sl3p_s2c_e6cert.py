# sl3p_s2c_e6cert.py — Stage-2 SL3': Certificate E.6 (W7 large-lam termwise
# domination): gamma=0.32, lam in [0.30,0.89], tau in (0,0.8]:
#     F(x) <= F(lam) for all x >= 2 lam .
# Part A (tau <= 0.58, ANALYTIC via condition C + lam-cells):
#     C(lam,0.58): (h(lam)-h(2lam))(1-2g-2g*0.58^2) >= h(lam)*0.58^2*lam^2/12
#   certified on lam-cells [l1,l2] (width 0.0025) by
#     (h(l2)-h(2*l1))*(0.36-0.64*0.3364) >= h(l1)*0.3364*l2^2/12 .
# Part B (tau in [0.58,0.8], x in [2*lam, 7.85], 2-D cells x x-cells):
#     F_lb(cell) = log1p(sin^2(t1*l1/2)/sinh^2(l2/2)) - 0.64*t2^2*h(l1)
#     F_ub(cell) = log1p(min(sin2max(u in [t1*x1/2, t2*x1/2])/sinh^2(x1/2),
#                            t2^2*h(x1)))            - 0.64*t1^2*h(x2)
#   (E.3: psi_tau decreasing in x on (0, 2pi/tau) covers x <= 7.85 < 2pi/0.8,
#    so the x-value inside the sin^2 is pinned at x1.)
# Part C (x > 7.85 tail): F(x) <= eps_t = 1/sinh^2(3.925) <= 1.5603e-3;
#   PASS iff min over (lam,tau) cells of F_lb >= eps_t.
# Output: out_sl3p_s2c.txt. 2026-08-12.
import numpy as np

GAM = 0.32
h = lambda x: (x/2.0)**2/np.sinh(x/2.0)**2

print("=== SL3' Stage 2, script C: Certificate E.6 (W7 termwise) ===")

# ---- Part A ----
T0 = 0.58
le = np.arange(0.30, 0.89 + 1e-12, 0.0025)
l1, l2 = le[:-1], le[1:]
lhs = (h(l2) - h(2*l1))*(1 - 2*GAM - 2*GAM*T0**2)
rhs = h(l1)*T0**2*l2**2/12.0
mratio = (lhs/rhs).min(); j = int(np.argmin(lhs/rhs))
print(f"Part A: {len(l1)} lam-cells on [0.30,0.89], tau0={T0}:")
print(f"  min C-margin lhs/rhs = {mratio:.4f} at lam-cell [{l1[j]:.4f},{l2[j]:.4f}]  PASS={mratio>=1.0}")
partA = mratio >= 1.0

# ---- Part B ----  (zoned cell widths: fine near lam=0.30 where slack ~4e-3)
X0 = 7.85
DT = 0.0005
tedges = np.arange(0.58, 0.80 + 1e-12, DT)
t1 = tedges[:-1][:, None]; t2 = tedges[1:][:, None]     # (nt,1)
ledges = np.concatenate([np.arange(0.30, 0.40, 0.0002),
                         np.arange(0.40, 0.60, 0.0005),
                         np.arange(0.60, 0.89 + 1e-12, 0.001)])
GUARD = 1e-6
minslack = 9e9; sloc = None; minFlb = 9e9; nfail = 0
for i in range(len(ledges)-1):
    la, lb = ledges[i], ledges[i+1]
    # x-cells: step 0.005 on [2la, 2la+0.4], 0.01 to 4, 0.02 to X0
    xe = np.concatenate([np.arange(2*la, 2*la+0.4, 0.005),
                         np.arange(2*la+0.4, 4.0, 0.01),
                         np.arange(4.0, X0, 0.02), [X0]])
    x1 = xe[:-1][None, :]; x2 = xe[1:][None, :]          # (1,nx)
    # F_lb per tau-cell (vector over tau)
    Flb = np.log1p(np.sin(t1[:, 0]*la/2.0)**2/np.sinh(lb/2.0)**2) - 2*GAM*t2[:, 0]**2*h(la)
    minFlb = min(minFlb, float(Flb.min()))
    # sin2max over u in [t1*x1/2, t2*x1/2]
    a = t1*x1/2.0; b = t2*x1/2.0
    k = np.ceil((a - np.pi/2)/np.pi)
    crosses = (np.pi/2 + k*np.pi) <= b
    s2m = np.where(crosses, 1.0, np.maximum(np.sin(a)**2, np.sin(b)**2))
    psi_ub = np.minimum(s2m/np.sinh(x1/2.0)**2, t2**2*h(x1))
    Fub = np.log1p(psi_ub) - 2*GAM*t1**2*h(x2)
    slack = Flb - Fub.max(axis=1)
    sm = float(slack.min())
    if sm < minslack: minslack, sloc = sm, (la, float(tedges[int(np.argmin(slack))]))
    nfail += int((slack < GUARD).sum())
print(f"Part B: {len(ledges)-1} lam-rows x {len(tedges)-1} tau-cells, x-cells to {X0}:")
print(f"  min cell slack F_lb - max_x F_ub = {minslack:.6f} at (lam1,tau1)={sloc}  cells<guard({GUARD}): {nfail}")
partB = nfail == 0

# ---- Part C ----
eps_t = float(1/np.sinh(3.925)**2)
print(f"Part C: eps_t = 1/sinh^2(3.925) = {eps_t:.6e}; min F_lb over all part-B cells = {minFlb:.6f}")
print(f"  floor/eps_t = {minFlb/eps_t:.1f}x  PASS={minFlb >= eps_t}")
partC = minFlb >= eps_t

print(f"E.6 CERTIFIED (A and B and C): {partA and partB and partC}")
print("=== end script C ===")
