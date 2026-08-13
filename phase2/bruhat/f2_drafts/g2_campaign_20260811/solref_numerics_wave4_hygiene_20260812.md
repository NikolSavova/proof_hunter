# numerics referee (gpt-5.6-sol, effort=max) — wave4_hygiene_20260812.md — 2026-08-12 19:11

> Cross-model referee report (Sol on the reviewed draft). Numeric checks are
> DERIVED, not executed — script them before trusting.

## Numerics-referee report

I cannot certify this overlay as written. Much of the bookkeeping is internally consistent, but the claimed verification is largely a parse of pre-existing PASS labels, not an independent verification of C1–C6. Several numerical statements are either false as written, rounded in an unsafe direction, or unsupported by formulas/artifacts in the supplied draft.

I use **FABRICATED-until-sourced** below in the requested forensic sense: the value may be true, but the supplied text does not give enough information to derive or reproduce it.

### A. Exact checks that can be completed from the text

| Claim | Exact calculation | Result |
|---|---:|---:|
| Rows \(4,\dots,481\) | \(481-4+1\) | \(478\) |
| Rows \(482,\dots,560\) | \(560-482+1\) | \(79\) |
| Union \(4,\dots,560\) | \(560-4+1\) | \(557=478+79\) |
| First-launch rows \(482,\dots,495\) | \(495-482+1\) | \(14\) |
| Resume prior count | \(478+14\) | \(492\) |
| Resume rows \(496,\dots,560\) | \(560-496+1\) | \(65\) |
| Fresh rows \(4,\dots,441\) | \(441-4+1\) | \(438\) |
| Sliver interval \(401,\dots,450\) | \(450-401+1\) | \(50\) |
| Rows beyond 450 through 560 | \(560-450\) | \(110\) |
| Consumer interval \(401,\dots,560\) | \(560-401+1\) | \(160\) |
| G4 interval \(401,\dots,536\) | \(536-401+1\) | \(136\) |

Thus the row-count arithmetic is coherent, conditional on the files actually containing exactly the asserted rows.

For the displayed last rows,

\[
N_m=\binom m2.
\]

Hence

\[
N_{559}=155961,\qquad \left\lfloor N_{559}/2\right\rfloor=77980,
\]

and

\[
N_{560}=156520,\qquad N_{560}/2=78260.
\]

Those displayed columns are arithmetically consistent. For \(m=559\), however, the two central indices are \(77980,77981\); the column schema must explain why both displayed integer columns equal \(77980\).

#### The “exact” \(4.04\) calculation is false

Interpreting the terminating decimals exactly,

\[
4.04\left(\frac14+\frac1{401}\right)
=\frac{101}{25}\frac{405}{1604}
=\frac{8181}{8020}
=1.02007481296758\ldots.
\]

It is **not exactly** \(1.020075\). In fact,

\[
1.020075-\frac{8181}{8020}
=\frac{3}{16040000}>0.
\]

The intended safe bound is true:

\[
\frac{8181}{8020}<1.0201,
\qquad
1.0201-\frac{8181}{8020}
=\frac{101}{4010000}>0.
\]

Block [D] must print the exact fraction \(8181/8020\), not say that the rounded decimal is exact.

#### The hyperbolic value is consistent

With \(x=3.925=157/40\),

\[
\frac1{\sinh^2 x}
=\frac{4e^{-2x}}{(1-e^{-2x})^2}
=\frac{4e^{-157/20}}{(1-e^{-157/20})^2}
\approx 0.00156022384.
\]

Thus the displays \(1.560224\times10^{-3}\) and the safe upper bounds

\[
\frac1{\sinh^2(3.925)}<1.5603\times10^{-3}<1.57\times10^{-3}
\]

are consistent. A reproducible check should use directed transcendental intervals, not a binary float alone.

#### E.6.B literal arithmetic

Treating the printed decimals as exact literals,

\[
0.002673-0.001448=0.001225=\frac{49}{40000}.
\]

Also,

\[
0.58^2=0.3364=\frac{841}{2500},
\]

and

\[
0.007921\cdot0.3364
=\frac{7921}{10^6}\frac{841}{2500}
=0.0026646244.
\]

These calculations do **not** certify that \(0.002673\) is the true slack or that \(0.001448\) is the rigorous cell bound; those operands remain unsourced.

There is also an unresolved scale inconsistency. As written,

\[
\coth(0.30/2)\cdot0.002
=\coth(0.15)\cdot0.002
\approx 0.01343318,
\]

not \(0.0033\). The quoted \(0.0033\) is approximately one quarter of this value:

\[
\frac14\coth(0.15)\cdot0.002\approx0.00335830.
\]

The omitted normalization factor must be stated.

### B. Independent Mahonian checks that should replace parse-only validation

For

\[
P_m(q)=\prod_{j=1}^m(1+q+\cdots+q^{j-1})
      =\sum_{k=0}^{N_m}a_m(k)q^k,
\]

an exact independent recurrence is

\[
a_m(k)=\sum_{j=0}^{m-1}a_{m-1}(k-j),
\]

with out-of-range coefficients zero. An efficient running-sum implementation is:

```python
from fractions import Fraction
from math import factorial

def next_poly(a, m):
    oldN = (m-1)*(m-2)//2
    N = m*(m-1)//2
    b = []
    s = 0
    for k in range(N+1):
        if k <= oldN:
            s += a[k]
        if 0 <= k-m <= oldN:
            s -= a[k-m]
        b.append(s)
    assert len(b) == N+1
    assert b == b[::-1]
    assert sum(b) == factorial(m)
    assert all(x > 0 for x in b)
    return b
```

Assuming the campaign's \(r_m(k)\) is the standard local log-concavity ratio,

\[
r_m(k)=\frac{a_m(k)^2}{a_m(k-1)a_m(k+1)},
\]

and

\[
\sigma_m^2=\frac{m(m-1)(2m+5)}{72},
\]

the central fit is

\[
F_m=\sigma_m^2\bigl(r_m(c_m)-1\bigr),
\qquad
c_m=\left\lfloor\frac{N_m}{2}\right\rfloor.
\]

The footer should be regenerated from this exact `Fraction`, not by reading existing PASS rows.

Useful exact anchors are:

- \(m=4\):
  \[
  (a_4(k))=(1,3,5,6,5,3,1).
  \]
  The center gives
  \[
  F_4=\frac{13}{6}\left(\frac{36}{25}-1\right)=\frac{143}{150},
  \]
  but the actual local minimum is at \(k=2,4\):
  \[
  \frac{13}{6}\left(\frac{25}{18}-1\right)=\frac{91}{108}.
  \]
  This reproduces the centrality exception.

- \(m=5\):
  \[
  (a_5(k))=(1,4,9,15,20,22,20,15,9,4,1),
  \]
  so
  \[
  F_5=\frac{25}{6}\left(\frac{121}{100}-1\right)=\frac78.
  \]

- \(m=6\):
  \[
  (a_6(k))=(1,5,14,29,49,71,90,101,101,90,71,49,29,14,5,1),
  \]
  and
  \[
  F_6=\frac{85}{12}\left(\frac{101}{90}-1\right)
      =\frac{187}{216}.
  \]

This independently verifies the claimed equality at \(m=6\).

It also exposes an ambiguity in “strict increase for \(5\le m\le560\)”:

\[
F_5=\frac78>\frac{187}{216}=F_6.
\]

Thus \(F_m\) is not strictly increasing from \(m=5\) to \(m=6\). If C6 means \(F_{m+1}>F_m\) only for \(m\ge6\), that qualifier must appear. If “strict increase” means another quantity, it must be defined.

At \(m=560\),

\[
\sigma_{560}^2
=\frac{560\cdot559\cdot1125}{72}
=4\,891\,250.
\]

The exact recurrence should reproduce these target rounded strings:

```text
F_534 -> 0.997978810615
F_535 -> 0.997982586007
F_536 -> 0.997986347205
F_537 -> 0.997990094521
F_540 -> 0.998001253256
F_560 -> 0.998072591511
```

and

\[
r_{560}(c)-1=\frac{F_{560}}{4\,891\,250}
\approx2.0405266\times10^{-7},
\]

consistent with the row's `2.0405e-07`.

Using the displayed rounded footer value only,

\[
560(1-0.998072591511)=1.07934875384,
\]

which rounds to `1.07935` and lies below

\[
\frac{27}{25}=1.08
\]

by \(0.00065124616\). This verifies only the displayed arithmetic, not the claimed limit.

The six footer decimals are not “exact Fraction matches”: the footer contains only rounded decimals. The independent script should print each exact numerator and denominator, together with a specified rational rounding rule.

### C. Required exact file audit

The parser must reject malformed non-comment lines and duplicates, not merely search for `FAIL`. The expected assertions are:

```python
assert ms_m540 == list(range(4, 482))
assert len(ms_m540) == 478
assert statuses_m540 == ["PASS"] * 478
assert overall_lines_m540 == []

assert ms_m560 == list(range(482, 561))
assert len(ms_m560) == 79
assert statuses_m560 == ["PASS"] * 79
assert len(overall_lines_m560) == 1
assert overall_lines_m560[0] == EXPECTED_OVERALL_BYTES

assert sorted(ms_m540 + ms_m560) == list(range(4, 561))
assert len(set(ms_m540 + ms_m560)) == 557

assert ms_fresh == list(range(4, 442))
assert len(ms_fresh) == 438
assert statuses_fresh == ["PASS"] * 438
assert overall_lines_fresh == []
```

For the byte-identity claim, compare the complete raw data-line bytes, keyed by \(m\), with no whitespace normalization.

At minimum, an independent recurrence should recompute the discrete seam and corner rows

\[
m=4,5,6,400,401,441,442,450,451,481,482,495,496,534,535,536,537,559,560.
\]

Rows \(442,\dots,481\), forty rows in total, are not covered by the claimed fresh rerun. Unspecified “referee spot-checks beyond” do not discharge a complete provenance debt.

There is also a direct textual contradiction: §1 says the results file “ends with the OVERALL line,” but §2 prints six checkpoint-footer lines after that line. The OVERALL line may occur exactly once, but it is not the end of the file. The §1 extract is therefore not the file's literal tail.

### D. SL3 crossover certificate

For each band, the exact quantity to check is

\[
R(W)=
\frac{q(W)}{b(W)}
\left(\frac1{1+\tau_{\rm start}(W)^2}-2\gamma^*(W)\right).
\]

To certify a lower bound from intervals, the safe substitution is

\[
R_{\rm safe}(W)=
\frac{q_L(W)}{b_U(W)}
\left(
  \frac1{1+\tau_U(W)^2}-2\gamma_U(W)
\right).
\]

Computing exactly with displayed decimal table values is valid only if those decimals are the actual definitions or are outward-rounded in these directions. Exact arithmetic on rounded-to-nearest table displays is not an exact certificate of the underlying constants.

For example, if \(\gamma^*=1/8\) and

\[
\tau_{\rm start}(W7)=0.7275=\frac{291}{400},
\]

then the bracket alone is exactly

\[
\frac1{1+(291/400)^2}-\frac14
=\frac{395319}{978724}
\approx0.40391265.
\]

The omitted exact \(q(W7)\) and \(b(W7)\) are needed to derive the reported \(1.2971\).

The target outputs are

```text
W1  1.4288
W2  1.4409
W3  1.7068
W4  1.7735
W5  1.9243
W6b 1.8653
W7  1.2971
```

but these are presently **FABRICATED-until-sourced** because the table inputs and their rounding directions are absent.

Moreover, \(1.2971<1.30\) and \(1.4288<1.43\). If these headlines are meant as certified lower bounds, `1.30x` and `1.43x` are unsafe upward roundings. Use `1.2971x`, or a downward-safe two-decimal bound such as `>1.29x`; similarly use `>1.42x` for W1.

The claimed truth value

\[
\delta_{\rm norm}(40,0.7275)=0.1615
\]

and the claim “\(\sim16\times b(W7)\)” are **FABRICATED-until-sourced**: the definition of \(\delta_{\rm norm}\), truncation/error bound, exact \(b(W7)\), and independent precision comparison are all missing.

### E. The \(10^{-14}\) endpoint sliver is not yet certified

Continuity plus an unspecified `O(1)` derivative is not a quantitative proof that a finite gap is covered.

If \(L\) is the certified margin at the final covered edge, \(\Delta\) is the uncovered width, and

\[
M\ge\sup |\partial_\tau F|,
\]

the needed check is

\[
L-M\Delta>0.
\]

Using the draft's own worst numbers:

- Script B, \(L=2.86\times10^{-2}\), \(\Delta=5.3\times10^{-15}\):
  \[
  M<\frac{0.0286}{5.3\times10^{-15}}
   =5.3962264\times10^{12}.
  \]

- Script C, \(L=1.448\times10^{-3}\), \(\Delta=2.4\times10^{-14}\):
  \[
  M<\frac{0.001448}{2.4\times10^{-14}}
   =6.0333333\times10^{10}.
  \]

These permissive thresholds make the repair likely easy, but the actual derivative formula and certified \(M\) are absent. The clean repair is to append an endpoint above the exact rational \(4/5\) and rerun the last cells with interval arithmetic.

Binary `0.8` is not exactly \(4/5\):

\[
\operatorname{float}(0.8)
=\frac{3602879701896397}{4503599627370496}
=\frac45+\frac1{22517998136852480}.
\]

Thus appending the usual binary `0.8` actually reaches slightly beyond the exact endpoint, which is safe if the cell certificate is valid on the resulting interval. The alleged deficits must nevertheless be recomputed against the exact rational \(4/5\), using `Fraction.from_float(edge)`, not by subtracting displayed floats.

For every top grid, print:

```python
Fraction.from_float(edge)
Fraction(4, 5) - Fraction.from_float(edge)
edge.hex()
```

and check the exact endpoint and its two adjacent floating-point values. The same treatment is required for \(0.3\), \(0.4\), \(0.58\), and every band edge.

### F. Mandatory off-grid and seam probes

Before acceptance, the following probes should be archived.

- **Sliver:** \(m=450,451,560,561\); \(w=4\), `nextafter(4,+inf)`, \(5\), \(4.51\), and the \(w\to\infty\) limit. Print the exact formula establishing the \(0.05\) threshold.
- **Crossover:** every exact band endpoint, one ULP on either side, exact \(\tau_{\rm start}\), one ULP on either side, and exact \(\tau=4/5\).
- **W7 truth probe:** \((w,\tau)=(40,291/400)\), \(w=40\pm1\) ULP, \(\tau=291/400\pm1\) ULP, and the W7 limiting \(w\)-corner.
- **E.6.B:** exact corners
  \[
  (\lambda,\tau)\in
  \left\{\frac3{10},\frac25\right\}
  \times
  \left\{\frac{29}{50},\frac45\right\},
  \]
  plus adjacent floats and the alleged near-degenerate \(\lambda\)-cell.
- **Array integrity:** print all final three edges in hexadecimal, prove `np.diff(edges)>0`, print the minimum cell width, and show that the extra `0.40` cell neither reverses orientation nor enters a division by a tiny width.
- **G4:** exact signed residuals at \(m=534,535,536,537\), not merely footer values.
- **Assembly band 2:** interval-optimize the actual residual at \(m=561\), all continuous band endpoints, and nearby \(m=560,562\). The expected lower bound is \(2.83\times10^{-4}\), but its formula is absent.

### G. FABRICATED-until-sourced register

The following numerical groups lack derivations or inspectable artifacts in the submitted text:

- File-content claims: 96 lines, line numbers 5 and 21, 429.6 seconds, exact raw tail, exactly one OVERALL line, all PASS statuses, and byte identity through 441.
- All six footer values, until exact fractions are independently regenerated and printed.
- The definitions and per-row checks of C1–C6.
- Sliver values \(m_0=450\), \(0.05\), \(4.56\times10^{-5}\), and “1097x-class.”
- The ORPHAN/ASM closure values \(4.05,432,450,560\).
- G4 crossovers “535/537” and the inference that exact coverage alone closes part (c).
- The crossover ratio list, `ana = 0.012768`, the 7.96x cell margin, and the \(0.1615\) truth value.
- The true E.6.B slack \(0.002673\), certified bound \(0.001448\), and coarse loss \(0.0033\).
- All floating endpoint deficits, the \(2.86\times10^{-2}\) and \(1.45\times10^{-3}\) margins, the \(10^{-6}\) guard, endpoint artifacts \(0.999645/1.000021\), and the 1192-edge claim.
- The flip-time margin \(2.83\times10^{-4}\).

A filename or quoted PASS line is provenance, not a derivation. The script, exact input files, SHA-256 hashes, Python/NumPy versions, and exact constants must be supplied.

There is also an unsafe sliver-headroom rounding: from only

\[
H_{561}\le4.56\times10^{-5}
\]

one obtains

\[
\frac{0.05}{H_{561}}
\ge\frac{0.05}{4.56\times10^{-5}}
=\frac{62500}{57}
=1096.4912\ldots,
\]

not a certified lower bound of \(1097\). “1097x-class” must be explicitly approximate or replaced by a downward-safe bound.

VERDICT: MAJOR_ISSUES

1. The claimed exact identity \(4.04(1/4+1/401)=1.020075\) is false; the exact value is \(8181/8020=1.0200748129\ldots\).
2. Block [A] only parses existing PASS labels, and block [E] recomputes six footer fields; this does not justify “completed-run audit re-verified from scratch” or independently verify C1–C6 for all 557 rows.
3. C1–C6 are not defined in the overlay, exact fractions are not printed, and the referenced scripts/results lack hashes or inspectable content; the principal finite-closure claim is therefore not reproducible from the submission.
4. The \(O(10^{-14})\) endpoint repair is incomplete: continuity plus an unspecified `O(1)` derivative does not quantitatively cover the missing interval. Append the exact endpoint and rerun, or supply an explicit derivative bound satisfying \(L-M\Delta>0\).
5. “Exact-rational” crossover calculations on displayed decimal table constants are not certificates unless those decimals are exact definitions or directed bounds. Their provenance and safe rounding directions are missing.
6. The certified-margin headlines round upward: \(1.2971<1.30\), \(1.4288<1.43\), and the stated sliver data imply only \(1096.49\)-class headroom. Consumer-facing lower bounds must round downward.
7. If “strict increase” refers to the central fit \(F_m\), its unqualified scope \(5\le m\le560\) is false because \(F_5=7/8>187/216=F_6\). The intended \(m\ge6\) qualifier or alternative quantity must be stated.
8. The E.6.B operands \(0.002673\) and \(0.001448\) are merely rounded assertions, while the displayed formula \(\coth(0.15)\,0.002\) gives \(0.013433\), not \(0.0033\); the omitted normalization and rigorous truth interval are required.
9. The file cannot both “end with the OVERALL line” and contain the six displayed footer lines after it. The §1 extract is not the literal file tail and must be relabeled.
10. The sliver, G4, assembly, continuous-band, and floating-grid claims have not been attacked at the exact endpoints, adjacent floating values, resume seams, or limiting \(w\)-corners listed above; their numerical values remain FABRICATED-until-sourced.