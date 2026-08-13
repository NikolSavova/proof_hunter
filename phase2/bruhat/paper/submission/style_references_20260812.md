# Style references for the copyediting pass

*Assembled 2026-08-12 from primary sources, per Sihao's instruction: research the best
mathematicians' writing guides, pull Tao's papers as a register reference, then copyedit.*

## Sources consulted (primary, not summaries)

- Terence Tao, ["On writing"](https://terrytao.wordpress.com/advice-on-writing-papers/)
  (his advice-page tree; read this session).
- Dimitri Bertsekas (MIT), ["Ten Simple Rules for Mathematical
  Writing"](https://www.mit.edu/~dimitrib/Ten_Rules.pdf) (slides read pp. 1–11, incl. the
  small/broad/composition-rule taxonomy and its bibliography: Halmos, Knuth et al.
  *Mathematical Writing*, Krantz, Higham).
- Paul Halmos, "How to Write Mathematics" (1970), via
  [MAA Mathematical Communication](https://mathcomm.org/paul-halmos-on-writing-mathematics/).
- Terence Tao, *The Erdős discrepancy problem*
  ([arXiv:1509.05363](https://arxiv.org/abs/1509.05363)) — register reference: the closest
  match to our paper (combinatorial, computation-adjacent, one headline theorem plus
  supporting structure). Abstract and introduction read this session.

## The distilled rulebook for OUR copyedit

### From Halmos (organization and honesty)
1. Say something: every section should have one identifiable point.
2. Write for a specific reader — for us: a combinatorialist who has not followed this
   project. Tao's version: write for your own past self of a year ago.
3. Arrange to minimize the reader's resistance: the common case before the exception,
   the statement before the machinery.
4. "Down with the irrelevant and the trivial" — cut what the reader does not need.
5. "Honesty is the best policy" — do not paper over a gap with prose; say what is open.
   (Our paper's conditional-status framing already follows this; the copyedit must not
   erode it.)
6. Notation deserves design: consistent, minimal, no symbol used once.

### From Bertsekas (verifiable sentence-level rules)
7. **2-3-4 rule**: consider splitting any sentence over 2 lines, any sentence with more
   than 3 verbs, any paragraph with more than 4 long sentences.
8. **Readable mathspeak**: "Let $k$ be a positive integer", not "Let $k>0$ be an
   integer"; "the function $f$ is continuous", never a sentence that OPENS with a bare
   symbol.
9. Active voice; "we" over "one" and over the agentless passive.
10. Minimize symbols in running text; prose between consecutive displayed formulas.
11. Watch "very / trivial / easy / clearly / obviously" — either justified or deleted.

### From Tao's advice pages (document level)
12. The introduction sells the key points — accurately. Motivation first, then results.
13. Structure modularly: lemmas encapsulate; a reader should be able to use a lemma
    without reading its proof ("information hiding").
14. Use English where English is clearer than symbols.
15. Don't over-optimize: past a point, polishing has diminishing returns; ship.

### From Tao's own prose (1509.05363), the register to imitate
16. **Variable sentence length** — terse for definitions and statements, longer with
    parentheticals for discussion; not uniformly short.
17. **Theorem statements carry descriptive bracket titles** ("Erdős discrepancy problem,
    vector-valued case") so the reader can navigate by statement.
18. **Hedging is explicit and calm**: "it seems reasonable to conjecture", "we do not
    know" — confidence is graded in plain declarative phrases, never with intensifiers.
19. **Credit is specific**: named people and projects for ideas, numbered citations for
    results; no vague "it is known that".
20. **The result comes immediately**: abstract states the theorem in its first sentence;
    the introduction defines, states the main theorem, and only then discusses context.

### Anti-rules (things this pass must NOT do)
- No mathematical content changes: statements, constants, numerals, labels, scopes are
  frozen.
- Do not weaken the honesty apparatus (conditional framing, open-statement list, the
  AI-assistance disclosure).
- Do not homogenize sentence length into choppiness (rule 16 cuts both ways).
- Halmos: "Defend your style" — apply rules with judgment, not mechanically; where the
  existing sentence is already the best version, leave it.
