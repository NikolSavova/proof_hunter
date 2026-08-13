# status6_afortiori_check.py — STATUS_wave6 editor arithmetic check (2026-08-12)
#
# Question: do Theorem SOL.9's CERTIFIED per-band ceilings (as re-certified by
# the numerics referee's certificate of record, referee_numerics_sol_s1.md §4
# table / ref3, and the W7 interval enclosures a(0.89) < 2.1304, b(0.89) <
# 6.4114) ALSO clear the paper's Table-4 constants — i.e. the WAVE-5 (old)
# (S1) targets R_3 = 1.0/1.2/1.5/1.7/2.0/2.1/2.2, R_4 =
# 0.8/1.4/2.6/3.5/5.2/6.0/6.6 (STATUS_wave5 §2 / CL_composition_20260812 §4)?
# If yes, the OLD (S1) is discharged a fortiori by the same refereed
# certificate, and the paper's existing Prop 6.8 chain (18.2281 <= 20) needs
# no constant-table change to record (S1) as proved.
#
# All inputs below are transcribed from refereed artifacts:
#   ceilings r31: sol_s1 SOL.6/SOL.7 table, certified in referee_numerics_sol_s1
#   ceilings r42: same
#   W7: interval enclosures (26)/(27) upper ends, certified twice
#   old targets: STATUS_wave5.md section 2 item 1 / CL_composition_20260812 section 4
#   new targets: wave6_s1_plan_20260812.md section 2

ceil_r31 = [0.900, 1.090, 1.370, 1.550, 1.850, 1.970, 2.1304]
ceil_r42 = [0.680, 1.250, 2.400, 3.260, 4.980, 5.650, 6.4114]
old_R31 = [1.0, 1.2, 1.5, 1.7, 2.0, 2.1, 2.2]
old_R42 = [0.8, 1.4, 2.6, 3.5, 5.2, 6.0, 6.6]
new_R31 = [1.19, 1.44, 1.82, 2.04, 2.38, 2.56, 2.71]
new_R42 = [0.87, 1.62, 3.11, 4.27, 6.38, 7.33, 8.17]
bands = ["W1", "W2", "W3", "W4", "W5", "W6b", "W7"]

ok_old = True
ok_new = True
worst_old = None
for i, b in enumerate(bands):
    c31, c42 = ceil_r31[i], ceil_r42[i]
    o31, o42 = old_R31[i], old_R42[i]
    n31, n42 = new_R31[i], new_R42[i]
    m31 = (o31 - c31) / o31
    m42 = (o42 - c42) / o42
    ok_old &= (c31 < o31) and (c42 < o42)
    ok_new &= (c31 < n31) and (c42 < n42)
    for tag, mar in (("r31", m31), ("r42", m42)):
        if worst_old is None or mar < worst_old[2]:
            worst_old = (b, tag, mar)
    print(f"  {b:3s}: ceil r31 {c31} < old {o31}: {c31 < o31}  (margin {m31*100:.2f}%)"
          f" | ceil r42 {c42} < old {o42}: {c42 < o42}  (margin {m42*100:.2f}%)")
print(f"  certified ceilings clear ALL 14 OLD (wave-5/Table-4) targets: {ok_old}")
print(f"  certified ceilings clear ALL 14 NEW (wave-6) targets: {ok_new}")
b, tag, mar = worst_old
print(f"  worst old-target margin: {mar*100:.2f}% ({b} {tag})")
