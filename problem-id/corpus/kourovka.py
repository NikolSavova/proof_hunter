"""Tier-A ingester: The Kourovka Notebook — Unsolved Problems in Group Theory.

The canonical, continuously-maintained list of open problems in group theory, published since
1965 (Novosibirsk) and updated every ~4 years; the 21st issue (2026) is the current one. Every
problem is contributed and vouched-for by a working group theorist and carries the author's name.
Human-curated + format-siloed (a single LaTeX document on arXiv, not indexed as separate problems)
= exactly the low-LLM-saturation ∩ human-vouched-important intersection the thesis targets. Group
theory / algebra is Nikol's lane.

Source = the arXiv e-print (LaTeX) of arXiv:1401.0300 (ar5iv can't render the ~250-page document).
The document is cleanly structured:
  - each problem is a `\\bmp \\textbf{N.M.} <statement> \\hfill {\\sl Author} \\emp` block
    (N = issue number, M = position);
  - the main body (issues 1..21) lists CURRENTLY-OPEN problems; once solved a problem is MOVED to
    the trailing "Archive of solved problems" section. So we cut at the Archive boundary and keep
    only the main body → genuinely-open problems, no solved-marker heuristics needed.

Scope control: a problem open for 60 years is the opposite of a tractable 1-week win, so we DEFAULT
to the recent issues (>= 18, i.e. 2014-2026, ~364 problems — the freshest, least-saturated alpha).
Use --since-issue to widen or --all for every open problem (~1310).

Usage:
    python corpus/kourovka.py                     # issues >= 18 (2014-2026), ~364 problems
    python corpus/kourovka.py --since-issue 20    # only 20th+21st (2022, 2026)
    python corpus/kourovka.py --all               # every open problem in the main body (~1310)
    python corpus/kourovka.py --limit 5           # smoke test (first 5 in range)
"""
from __future__ import annotations
import argparse, io, pathlib, re, sys, tarfile
import requests

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import common  # noqa: E402

SOURCE = "kourovka"
EPRINT = "https://arxiv.org/e-print/1401.0300"
UA = {"User-Agent": "problem-id research pipeline"}
MIN_STATEMENT = 60          # mirror filter.py MIN_STATEMENT_CHARS
DEFAULT_SINCE_ISSUE = 18    # 2014+; the tractable-alpha subset

# Published Kourovka Notebook edition years (stable history).
ISSUE_YEAR = {
    1: 1965, 2: 1966, 3: 1969, 4: 1973, 5: 1976, 6: 1978, 7: 1980, 8: 1982, 9: 1984, 10: 1986,
    11: 1990, 12: 1992, 13: 1995, 14: 1999, 15: 2002, 16: 2006, 17: 2010, 18: 2014, 19: 2018,
    20: 2022, 21: 2026,
}


def fetch_tex() -> str:
    """Download the arXiv e-print tarball and return the largest .tex file's text."""
    r = requests.get(EPRINT, timeout=90, headers=UA)
    r.raise_for_status()
    tf = tarfile.open(fileobj=io.BytesIO(r.content), mode="r:*")
    tex = [m for m in tf.getmembers() if m.isfile() and m.name.endswith(".tex")]
    if not tex:
        raise RuntimeError("no .tex file in the Kourovka e-print tarball")
    biggest = max(tex, key=lambda m: m.size)   # the notebook body, not the .cls
    return tf.extractfile(biggest).read().decode("utf-8", "replace")


def main_body(tex: str) -> str:
    """Everything before the 'Archive of solved problems' section (= currently-open problems).

    NB: an earlier "Archive of solved" appears in a COMMENTED-OUT title-page line, so we anchor on
    the real section's first entry header ("Archive of solved problems (1st ed., 1965)").
    """
    m = re.search(r"Archive of solved problems \(1st ed", tex)
    return tex[: m.start()] if m else tex


# --- LaTeX -> readable-text cleaning (math is left verbatim; the LLM reads TeX math fine) --------
_AUTHOR_RE = re.compile(r"\{+\s*\\sl\s+(.*?)\}+", re.DOTALL)

def _strip_latex(s: str) -> str:
    s = re.sub(r"(?<!\\)%.*", "", s)                      # drop comments
    s = re.sub(r"\\(url|ul)\{([^}]*)\}", r"\2", s)        # \url{X}/\ul{X} -> keep the content
    s = re.sub(r"\\raisebox\{[^}]*\}", "", s)             # \raisebox{-1ex}{..} -> keep inner {..}
    s = re.sub(r"\\makebox\[[^\]]*\]\[[^\]]*\]", "", s)   # \makebox[25pt][r]{(a)} -> keep {(a)}
    s = re.sub(r"\\(begin|end)\{[^}]*\}", " ", s)         # drop enumerate/itemize wrappers
    s = re.sub(r"\\item\b", "; ", s)                      # list bullets -> separators
    s = re.sub(r"\\(hfill|hf|vs|mb|smallskip|medskip|bigskip|par|noindent|phantomsection|linebreak"
               r"|parindent=0pt|raggedbottom|newpage|hfil|flushbottom|thispagestyle|otv|zva|zv)\b", " ", s)
    s = re.sub(r"\\(textbf|textit|textsl|textrm|emph|text|mathrm|mbox|it|sl|bf|rm|em|ul|large|Large"
               r"|displaystyle|centerline)\b", " ", s)
    s = re.sub(r"\\(hskip|vskip|vspace|hspace)\s*\{?[^}\s]*\}?", " ", s)
    s = s.replace("\\,", " ").replace("\\;", " ").replace("\\ ", " ").replace("~", " ")
    s = s.replace("\\&", "&").replace("---", "—").replace("--", "–")
    s = re.sub(r"\{|\}", " ", s)                           # drop stray grouping braces
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{2,}", "\n", s)
    return s.strip()


def parse_block(block: str) -> dict | None:
    """block = text between \\bmp and \\emp. Return a problem record or None."""
    m = re.match(r"\s*\\textbf\{\s*(\d+)\.(\d+)([a-z]?)\.?\s*\}", block)
    if not m:
        return None
    issue, pos = int(m.group(1)), m.group(2)
    number = f"{issue}.{pos}{m.group(3)}"
    body = block[m.end():]

    authors = _AUTHOR_RE.findall(body)
    author = _strip_latex(authors[-1]).replace("\n", " ").strip() if authors else None
    body_wo_author = _AUTHOR_RE.sub(" ", body)            # remove author tag from statement

    # `\otv` (a star) introduces an editorial ANSWER added after the problem was posed. A few
    # main-body problems were answered post-2022 but not yet moved to the Archive — split the
    # answer off, keep it labelled, and flag status so nothing answered masquerades as open.
    status, answer = "open", None
    if "\\otv" in body_wo_author:
        stmt_part, answer_part = body_wo_author.split("\\otv", 1)
        answer = _strip_latex(answer_part)
        if len(answer) > 15:
            status, body_wo_author = "partially-solved", stmt_part

    statement = _strip_latex(body_wo_author)
    if len(statement) < MIN_STATEMENT:
        return None
    if answer and status == "partially-solved":
        statement = f"{statement}\n\n[Kourovka editorial note / answer: {answer[:1500]}]"
    year = ISSUE_YEAR.get(issue)
    # Title carries the problem's CONTENT (first sentence), not "Kourovka N.M (Author)": the latter
    # collapses under the Stage-1 lexical dedup (norm_tokens drops the number, so same-author
    # problems become identical tokens -> false duplicates). Author/number live in id + raw.
    first = re.split(r"(?<=[.?;])\s", statement.replace("\n", " "))[0].strip()
    title = (first if len(first) >= 25 else statement.replace("\n", " ").strip())[:200]
    return {
        "id": f"{SOURCE}:{number}",
        "source": SOURCE,
        "source_url": f"https://arxiv.org/abs/1401.0300",
        "title": title[:300],
        "statement": statement[:8000],
        "field": ["group-theory", "algebra"],
        "year_posted": year,
        "status_claimed": status,
        "tags": ["tier-a", "low-saturation", "group-theory", "kourovka",
                 "human-curated", "single-problem"],
        "stage": "ingested",
        "raw": {"issue": issue, "number": number, "author": author, "status": status},
    }


def extract_problems(tex: str, since_issue: int) -> list[dict]:
    body = main_body(tex)
    out, seen = [], set()
    for block in re.split(r"\\bmp\b", body)[1:]:
        block = block.split("\\emp", 1)[0]               # up to end-of-problem
        rec = parse_block(block)
        if not rec:
            continue
        if rec["raw"]["issue"] < since_issue:
            continue
        if rec["id"] in seen:                            # de-dup repeated numbers defensively
            continue
        seen.add(rec["id"])
        out.append(rec)
    return out


def ingest(since_issue=DEFAULT_SINCE_ISSUE, all_issues=False, limit=None) -> int:
    con = common.db()
    since = 1 if all_issues else since_issue
    print(f"[kourovka] fetching e-print {EPRINT} ...")
    tex = fetch_tex()
    recs = extract_problems(tex, since)
    if limit:
        recs = recs[:limit]
    print(f"[kourovka] {len(recs)} open problems (issues >= {since}) from the main body")
    n = 0
    for rec in recs:
        common.upsert(con, rec); n += 1
        print(f"  + {rec['id']:16} [{rec['year_posted']}] {rec['statement'][:64].replace(chr(10),' ')}")
    print(f"[kourovka] ingested {n} group-theory problems -> {common.DB_PATH}")
    return n


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--since-issue", type=int, default=DEFAULT_SINCE_ISSUE,
                    help="lowest issue number to ingest (default 18 = 2014+)")
    ap.add_argument("--all", action="store_true", help="ingest every open problem (~1310)")
    ap.add_argument("--limit", type=int, default=None)
    a = ap.parse_args()
    ingest(a.since_issue, a.all, a.limit)
