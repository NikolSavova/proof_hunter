"""Shared core for the problem-identification pipeline.

DB store, problem-record helpers, rubric loading + composite scoring, and OpenAI
key/client loading. See PROBLEM_ID_PIPELINE.md for the design this implements.
"""
from __future__ import annotations
import json, os, sqlite3, time, pathlib
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parent          # .../proof_hunter/problem-id
AI_MATH = ROOT.parent                                    # .../proof_hunter
DB_PATH = ROOT / "db" / "problems.sqlite"
RUBRIC_PATH = ROOT / "rubric.yaml"
# Secret lives OUTSIDE the repo so it is never committed. Override with $OPENAI_API_KEY
# or $OPENAI_KEY_FILE. Falls back to the in-repo file only for backward compatibility.
KEY_PATH = pathlib.Path(
    os.environ.get("OPENAI_KEY_FILE")
    or pathlib.Path.home() / ".config" / "proof_hunter" / "openai_key.txt"
)

# ---- the durable, append-only problem store (spec §2 principle 6) ----
SCHEMA = """
CREATE TABLE IF NOT EXISTS problems (
    id            TEXT PRIMARY KEY,   -- "src:local-id", stable
    source        TEXT,
    source_url    TEXT,
    title         TEXT,
    statement     TEXT,               -- verbatim problem text
    restatement   TEXT,               -- one-line plain restatement (LLM)
    field         TEXT,               -- json list
    year_posted   INTEGER,
    last_progress TEXT,
    status_claimed TEXT,              -- open|partial|unknown
    tags          TEXT,               -- json list
    formalized    TEXT,               -- lean stmt url | null
    scores        TEXT,               -- json {axis: 1-5}
    detectors     TEXT,               -- json {flag: bool}
    composite     REAL,               -- normalized 0-5 (weights + boosts)
    win_condition TEXT,
    suggested_engine TEXT,            -- A|B|both|none
    killsearch    TEXT,               -- json {still_open, closest_prior, verdict, notes}
    attack_sketch TEXT,
    stage         TEXT,               -- ingested|filtered|triaged|deep|finalist|rejected
    drop_reason   TEXT,
    raw           TEXT,               -- json: source-specific extras
    ingested_at   REAL,
    scored_at     REAL
);
CREATE INDEX IF NOT EXISTS idx_stage  ON problems(stage);
CREATE INDEX IF NOT EXISTS idx_source ON problems(source);
"""

def db() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    con.executescript(SCHEMA)
    return con

def upsert(con: sqlite3.Connection, rec: dict[str, Any]) -> None:
    """Insert or update a problem by id. Append-only in spirit: never deletes,
    preserves ingested_at on update."""
    rec = dict(rec)
    for k in ("field", "tags", "scores", "detectors", "killsearch", "raw"):
        if k in rec and not isinstance(rec[k], str):
            rec[k] = json.dumps(rec[k])
    existing = con.execute("SELECT ingested_at FROM problems WHERE id=?", (rec["id"],)).fetchone()
    if existing:
        rec.setdefault("ingested_at", existing["ingested_at"])
    else:
        rec.setdefault("ingested_at", time.time())
    cols = list(rec.keys())
    placeholders = ",".join("?" for _ in cols)
    updates = ",".join(f"{c}=excluded.{c}" for c in cols if c != "id")
    con.execute(
        f"INSERT INTO problems ({','.join(cols)}) VALUES ({placeholders}) "
        f"ON CONFLICT(id) DO UPDATE SET {updates}",
        [rec[c] for c in cols],
    )
    con.commit()

# ---- rubric / composite ----
def load_rubric() -> dict:
    import yaml
    with open(RUBRIC_PATH) as f:
        return yaml.safe_load(f)

def composite_score(scores: dict[str, int], detectors: dict[str, bool], rubric: dict) -> float:
    """Weighted, weight-normalized to 0-5, plus small detector boosts (capped at 5)."""
    weights = rubric["weights"]
    num = sum(weights[a] * float(scores.get(a, 0)) for a in weights)
    den = sum(weights.values())
    base = num / den if den else 0.0
    boost = sum(rubric.get("detector_boosts", {}).get(d, 0.0)
                for d, on in (detectors or {}).items() if on)
    return round(min(5.0, base + boost), 4)

# ---- OpenAI ----
def load_api_key() -> str:
    key = os.environ.get("OPENAI_API_KEY")
    if key:
        return key.strip()
    return KEY_PATH.read_text().strip()

def openai_client():
    from openai import OpenAI
    return OpenAI(api_key=load_api_key())
