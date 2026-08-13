# What the posted string actually contains

*2026-08-13. Analysis of the string Sihao supplied for the Alpöge–Voinov–Reynolds-Haertle–Claude
Hadamard announcement (~2026-08-11), which claims matrices for all twelve admissible orders below
2000 that previously had none. Scripts: `find_quads.py`, `scan_all.py`. Raw: `puzzle.txt`.*

## Result

**Five of the twelve claimed orders are present and verified. Seven are not, including 668 —
the headline order.**

| Order | Status | Offset in string | m = n/4 |
|---|---|---|---|
| 892 | **VERIFIED HADAMARD** | 1376 | 223 |
| 1132 | **VERIFIED HADAMARD** | 2268 | 283 |
| 1244 | **VERIFIED HADAMARD** | 3400 | 311 |
| 1948 | **VERIFIED HADAMARD** | 19916 | 487 |
| 1964 | **VERIFIED HADAMARD** | 21864 | 491 |
| 668, 716, 1388, 1436, 1676, 1772, 1916 | not found | — | — |

"Verified" means the full matrix was constructed and `H Hᵀ = n·I` checked in **exact integer
arithmetic**, together with all entries being ±1. No floating point is load-bearing.

## The encoding, and what it says about the construction

Each of the five is a **Williamson-type quadruple** — four ±1 sequences `A,B,C,D` of length
`m = n/4` whose periodic autocorrelations satisfy `P_A(j)+P_B(j)+P_C(j)+P_D(j) = 0` for all
`j ≠ 0` — laid out as four consecutive length-`m` blocks and expanded through a **Goethals–Seidel
array**. The layout is contiguous: each order occupies exactly `n` characters, and the five hits
form two unbroken runs, `[1376, 4644)` covering 892→1132→1244 and `[19916, 23828)` covering
1948→1964, the second ending exactly at the end of the string.

**This answers the question we set out to answer, at least for these five: it is a SEARCH result
inside a classical framework, not a new general construction.** Williamson quadruples and the
Goethals–Seidel array are standard; the work is in *finding* quadruples at
`m = 223, 283, 311, 487, 491`, which is a hard combinatorial search but does not come with a
theorem. The immediate consequence is that **it should not be expected to extend past 2000 for
free** — there is no general mechanism here to extend, only a search that was run to a bound.

That matters for how the result should be described. "Twelve new Hadamard matrices" is a
substantial computational achievement. "Progress toward the Hadamard conjecture" in the sense of
a construction that keeps going is, on this evidence, not what happened.

## The seven that are absent

`scan_all.py` searched **every block length m from 40 to 700 at every offset** — not just the
twelve target lengths — and found exactly six quadruples realising five distinct orders. The seven
missing orders do not appear anywhere in the string as Williamson quadruples.

Of 23828 characters, the quadruples consume 8312. The remaining **15516 are unexplained**: a head
region `[0, 1376)` and a middle region `[4644, 19916)`. Neither decodes as ASCII under 7- or 8-bit
framing at any offset. The middle contains zones of near-exact **period 56** repetition — blocks
of 56 characters repeated four times — around indices 11400–12000 and 13400–14000. Repeated
identical blocks cannot be a Williamson quadruple (`A=B=C=D` would force `P_A(j)=0` for all
`j ≠ 0`, which no ±1 sequence of that length achieves), so that material is something else.

Note `668 + 716 = 1384`, while the head region is `1376` characters — eight short. Suggestive, but
`m = 167` and `m = 179` produce no quadruple anywhere in the string, so the two missing small
orders are not merely misaligned.

## Three explanations, and what would distinguish them

1. **The other seven use a different classical construction.** Entirely plausible — Baumert–Hall
   arrays, T-sequences, base sequences, Turyn sequences and propus constructions all exist and
   none were tested. This is my leading hypothesis and it is cheap to test further.
2. **The string was garbled or truncated reaching us.** It came through a chat paste and was
   re-transcribed by hand. Against this: two perfect contiguous runs, and the final quadruple
   ending exactly at the last character, are strong internal consistency checks. For this to be
   the explanation, the damage would have to be confined to the unexplained regions.
3. **The claim covers more than the artifact does.** Possible, and not to be asserted. Five
   verified new Hadamard matrices is a real result either way.

**The discriminating action is to re-source the string from the original post** rather than a
paste, and to check the character count against 23828. If the original is longer, explanation 2
is confirmed and the analysis simply reruns.

## Caveats on this analysis

- Transcription risk is mine, as above.
- Only the Williamson/Goethals–Seidel family was tested. Absence of a quadruple is **not**
  absence of a Hadamard matrix.
- The five positives are unconditional and do not depend on any of this: those matrices exist and
  are verified, whatever the rest of the string turns out to be.
