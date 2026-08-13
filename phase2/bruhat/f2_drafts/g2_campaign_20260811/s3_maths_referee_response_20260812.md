# (S3) — response to the Sol maths-referee pass (verdict FATAL)

*2026-08-12. `solref_maths_sol_s3_20260812.md` is the missing (S3) maths lane
(the one the Fable credit limit killed), run cross-model on gpt-5.6-sol. Verdict:
**FATAL**, six issues. This note triages them against the work done earlier the
same day (`s3_certificate_20260812.md`). Nothing here is a proof; it is a status
reconciliation. The referee's own numeric claims are DERIVED, not executed — the
one that is load-bearing was independently re-verified here (§1).*

## Summary of the triage

| Sol issue | Substance | Status after this session |
|---|---|---|
| 1. EM remainder invalid as stated | **Correct and load-bearing** | **Already repaired** — my certificate ran with the corrected constant (§1) |
| 2. 18.9M-box certificate never run | Correct | **Repaired for W1–W6b** — executed, passes (§2) |
| 3. (SOL.5) and W7 certs unsupported | Correct | **(SOL.5) repaired**; W7 parts still open (§3) |
| 4. `B >= 0` assumed without proof (W7) | **Correct, NEW, not caught by either Claude referee** | **OPEN — real gap** (§4) |
| 5. (SOL.13) half-line B_8 term unjustified | Correct, minor | Open, one lemma (§5) |
| 6. "nothing remains" is false | Correct | Agreed — (S3) is not closed |

**Bottom line: the FATAL verdict is correct as a judgement of the draft as
written, but its three central pillars (issues 1–3) are exactly the items already
repaired for the compact bands earlier today. The damage that survives is
concentrated in the W7 leg — where issue 4 is a genuine mathematical gap, not an
unrun computation.**

## 1. Issue 1 (EM remainder) — correct, and independently confirmed; already repaired

Sol: the expansion retains endpoint terms only through `B_6`, so the advertised
remainder `|E_{n,8}| <= lam^8/1209600 * int_0^w |h_n^(8)|` does not follow; to use
an 8th-derivative remainder with the constant `|B_8|/8! = 1/1209600` one must also
include the `B_8` endpoint term `+ lam^8/1209600 (h_n^(7)(w) - h_n^(7)(0))`, which
is generally nonzero at finite `w`.

**This is the same defect the Claude numerics referee found (its F2), reached by a
different route — genuine cross-model corroboration.** The Claude referee's sharper
form: the 8th-derivative kernel form IS valid without the `B_8` endpoint term,
provided the constant is `(2 - 2^-7)|B_8|/8!`. Verified independently here in exact
rational arithmetic (script output, this session):

```
B_8 = -1/30 ;  B_8(1/2) = (2^(1-8)-1) B_8 = 127/3840
sup |B_8({x}) - B_8| = 17/256 = (2 - 2^-7)|B_8|      (exact match; 2000-pt grid agrees)
valid kernel constant = 17/10321920 = 1.9921875 x (1/1209600)
```

(One integration by parts sends `-int B_7({x})/7! f^(7)` to `int (B_8({x}) - B_8)/8! f^(8)`,
whence the `sup|B_8({x}) - B_8|` constant rather than `|B_8|`.)

**`s3_cert.py` ran with radius `2 * 10^12 * w * lam^8 / 1209600`, i.e. factor
`2 >= 1.9921875`. The executed certificate therefore already satisfies the
corrected bound, and all six bands certify under it.** Sol's issue 1 invalidates
the draft's stated lemma; it does not invalidate the run.

Draft text erratum stands as recorded: (SOL.4)/(SOL.13) must carry the corrected
constant (either `17/10321920`, or the `B_8` endpoint term explicitly), and (SOL.6)
must be re-quoted with it.

## 2. Issue 2 (the unrun certificate) — repaired for the compact bands

Executed 2026-08-12: all six bands W1–W6b certified, zero hard failures, by adaptive
certified interval arithmetic (1,591 leaves against the draft's asserted 18,874,368
uniform boxes), with the corrected constant of §1 and selftests at two precisions
against the Claude referee's independent anchors. Details and honest method caveats:
`s3_certificate_20260812.md` §§1–4.

Sol's sharper sub-point is worth recording: *"the proposed checker would implement
the invalid remainder from issue 1, so even the advertised run would not prove SOL.3
without mathematical repair"* — correct, and precisely why the executed run used the
repaired constant rather than the draft's.

## 3. Issue 3 (unsupported computational assertions) — (SOL.5) repaired; W7 parts open

- `|h_n^(8)| <= 10^12` on `(0,40]`: **CERTIFIED** this session (`sol5_cert.py`;
  Cauchy coefficient bound on `|z| = 6` for `x in [0,1]`, direct Leibniz series for
  `[1,40]`; worst margin 460x). See `s3_certificate_20260812.md` §6.
- `int_0^oo |h_n^(8)| < 10^12`, and the W7 lemmas `h_2 - dT_2 > 9/10`,
  `h_4 - dT_4 > 49/10`, `U_7 <= 12/5`: **still unsupported.** These belong to the W7
  leg, which this session did not touch.

## 4. Issue 4 (`B >= 0`) — NEW, real, and the most serious surviving item

Sol: in (SOL.4), from `B = m h_3(lam) - sum_j h_3(j lam)` and nonnegativity of the
summands one obtains only `B <= m h_3(lam)`, **not** `B >= 0`; yet the bound on
`B^2/A^2` in (SOL.12) needs `|B| <= m h_3`, for which `B >= 0` is load-bearing. No
proof is given, and the W7 verification recipe never checks `T_3`.

**Neither Claude referee caught this.** (The Claude numerics referee's §7 checked
specifically that the forbidden sign-lemma route had not been smuggled back in, and
cleared it — a different question from this one.) Sol proposes the repair direction:
monotonicity of `h_3`, or a certified `h_3 - dT_3 >= 0`. **Not attempted here.**

This is the reason (S3)'s W7 leg cannot be called "computation pending": it has an
unproved hypothesis inside a proof step.

## 5. Issue 5 ((SOL.13) half-line) — minor, unaddressed

On the half-line the `B_8` endpoint term plausibly vanishes because
`h_n^(7)(0) = h_n^(7)(oo) = 0` for `n = 2,3,4` (`h_n` is even, so all odd derivatives
vanish at 0; decay handles infinity), but Sol is right that this must be stated and
proved rather than assumed. One short lemma. Note it does **not** rescue the
finite-`w` case of §1, where `h_n^(7)(w) != 0`.

## 6. Where (S3) actually stands

**Compact bands W1–W6b:** enclosure repaired (§1), certificate executed and passing
(§2), (SOL.5) certified (§3). Remaining: the exact-rational-wording question
(`s3_certificate_20260812.md` §4 item 1) and a maths pass on the *repaired* chain.

**Band W7:** an unproved sign hypothesis (§4), an unjustified half-line step (§5),
and three unrun certificates (§3). **This is now the blocking half of (S3).**

**Therefore: (S3) remains OPEN.** The FATAL verdict is not overturned by this note —
it is triaged. What changed today is that the compact-band half moved from
"asserted" to "executed under a corrected constant", and the surviving obstruction
is now sharply localized in W7, with a named mathematical gap rather than a
computational backlog.
