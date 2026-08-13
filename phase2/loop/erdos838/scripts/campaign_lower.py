#!/usr/bin/env python3
"""Erdős 838 — the all-in campaign on the LOWER bound. Seven Sol lanes at effort=max.

THE BET. We already own limsup log f(N)/(log N)^2 <= 1/2 (paper/main.tex, Theorem 1.1, verified
independently). If liminf >= 1/2, then the limit EXISTS and EQUALS 1/2, and Erdős problem 838 --
the Erdős-Hammer question -- is completely resolved. One theorem closes the whole problem. No
other target in this repo has that property, which is why this gets the whole budget.

WHERE THE CURRENT LOWER BOUND LEAKS, precisely. The published 1/4 takes t = floor(sqrt N), gets a
convex k-set with k ~ (1/2) log N by Suk's ES(k) = 2^{k+o(k)}, and double counts:
    log( C(N,k) / C(t,k) ) ~ k log(N/t) = (1/2 log N)(1/2 log N) = (1/4)(log N)^2.
It counts ONE SIZE CLASS. But the upper construction's count is a PRODUCT -- W ~ C*U, caps times
cups, each of size 2^{(1/4)(log N)^2}. The lower bound discards exactly the factor the upper bound
is built from. That is the whole gap, and it is a factor of 2 in the exponent.

THE TARGET, stated once and shared by every lane:

    LEMMA (GENERAL CAP-CUP PRODUCT). There is a function o(1) -> 0 such that every N-point planar
    set P in general position satisfies
        log_2 C(P) + log_2 U(P) >= (1/2 - o(1)) (log_2 N)^2,
    where C(P), U(P) are the total numbers of caps and cups of P (all sizes, singletons included).

Since every convex set of size >= 2 is uniquely an upper cap and a lower cup sharing endpoints,
W(P) >= max over endpoint pairs of c(p,q)u(p,q), and the paper's section 5 already converts the
product bound into the count. Lemma 5.2 of main.tex proves EXACTLY this bound with constant 1/2
for DECOMPOSABLE sets. The task is to remove that hypothesis.

Lanes:
  verify51        audit the multiscale reset in Theorem 5.1 -- the prerequisite
  attack_direct   prove the general lemma head-on
  attack_szekely  transfer Székely's 1984 graph argument, which gets the same constant
  attack_tree     canonical tree decompositions of order types as the bridge
  break_lemma     try to REFUTE the general lemma
  break_target    try to beat coefficient 1/2 on the UPPER side -- is 1/2 even the answer?
  priorart        has the lower bound already been improved? Erdősgate gate.

The two break lanes are not decoration. If break_target succeeds the target value is wrong and the
campaign is aimed at the wrong number; that is the single most valuable thing this run could
return, and it is cheaper to learn now.

Usage: ./campaign_lower.py [lane ...]
"""
import json, pathlib, sys, threading, time

import openai

HERE = pathlib.Path(__file__).resolve().parent
BASE = HERE.parent
KEY = (pathlib.Path.home() / ".config/proof_hunter/openai_key.txt").read_text().strip()
MODEL, EFFORT = "gpt-5.6-sol", "max"
IDS = HERE / "campaign_lower_ids.json"
_lock = threading.Lock()


def attach(relpath, cap=120_000):
    """Hand over the ARTIFACT, never a paraphrase of it. Standing rule since 2026-08-12."""
    p = BASE / relpath
    return f"\n\n===== {relpath} =====\n" + p.read_text()[:cap]


PAPER = attach("paper/main.tex")

SETUP = r"""ERDŐS PROBLEM 838 (Erdős and Hammer). For a finite planar point set P in general
position, call a subset CONVEX if all its points are vertices of its convex hull, and let v(P) be
the number of convex subsets. Put f(N) = min over |P| = N of v(P). Erdős asked whether

    log f(N) / (log N)^2

has a limit and what it is. ALL LOGARITHMS ARE BASE 2 THROUGHOUT.

CURRENT RIGOROUS WINDOW:  1/4 <= liminf <= limsup <= 1/2.

 * The upper 1/2 is OUR theorem (attached paper, Theorem 1.1). It is proved by an iterated
   order-type blow-up of balanced Erdős-Szekeres cup-cap templates. It has been independently
   verified: the exact composition identities of Lemma 2.2 were re-derived from orientation
   determinants alone on a 36-point instance, reproducing (C,U,W) = (14136,14136,441399).
 * The lower 1/4 is standard: with t = floor(sqrt N) and Suk's ES(k) = 2^{k+o(k)}, every t-point
   set has a convex k-set with k = (1-o(1)) log t = (1/2 - o(1)) log N; double-counting pairs
   (K,T) with |K| = k, |T| = t gives #convex k-subsets >= C(N,k)/C(t,k), whose log is
   ~ k log(N/t) = (1/4)(log N)^2.

WHY THE LOWER BOUND IS LOSSY, AND WHERE THE FACTOR OF 2 LIVES. The double count uses convex
subsets of a SINGLE SIZE k. The upper construction's count is a PRODUCT: W ~ C*U where C and U are
the total numbers of caps and cups, each about 2^{(1/4)(log N)^2}. Every convex set of size >= 2 is
uniquely an upper cap and a lower cup sharing their leftmost and rightmost points, so counting
caps and cups separately and multiplying is what produces the exponent 1/2. The published lower
bound throws away precisely that structure.

THE TARGET LEMMA. Prove, for EVERY N-point planar set P in general position (no decomposability,
no recursive structure, arbitrary order type):

    log C(P) + log U(P) >= (1/2 - o(1)) (log N)^2,

where C(P) and U(P) count ALL caps and ALL cups respectively, of every size, singletons included.
A cap is a set whose increasing triples all have orientation -, a cup + (points ordered by
x-coordinate).

WHY THIS FINISHES THE PROBLEM. Section 5 of the attached paper already converts a cap-cup product
bound into a bound on W(P): with c(p,q), u(p,q) the numbers of caps/cups with endpoints p and q,
    W(P) = |P| + sum over p<q of c(p,q) u(p,q),
and C(P) <= |P| X(P), U(P) <= |P| Y(P), X(P), Y(P) <= |P| M(P), M(P) <= W(P). So a lower bound on
log C + log U of the stated strength forces log W >= (1/2 - o(1))(log N)^2, hence
liminf >= 1/2. Combined with the theorem we already have, THE LIMIT EXISTS AND EQUALS 1/2, and
Erdős 838 is resolved outright.

WHAT IS ALREADY KNOWN ABOUT THE TARGET.
 * Lemma 5.2 of the attached paper proves EXACTLY this bound, with constant 1/2, for DECOMPOSABLE
   point sets (singleton, or a split A < B with both parts decomposable and a strong separation
   between them). Its proof: R = sqrt(C*U) satisfies R(A<B) >= sqrt(|B|+1) R(A) + sqrt(|A|+1) R(B)
   by Cauchy-Schwarz; follow the larger child down to a leaf; a convexity/Bernoulli estimate and
   the telescoping identity sum d_i t_i = ((log s)^2 + sum d_i^2)/2 give the result. THIS IS THE
   TEMPLATE. The task is to remove the decomposability hypothesis.
 * The class of decomposable sets is due to Balko, Kynčl, Langerman and Pilz, Electron. J. Combin.
   24(4) (2017) P4.24; Baek and Balko proved the Erdős-Szekeres conjecture on it.
 * Proposition 4.4 of the paper shows no FIXED-TEMPLATE iteration can beat coefficient 1/2, via
   the Erdős-Szekeres cup-cap theorem: a set with no (a+1)-cap and no (b+1)-cup has at most
   C(a+b-2, a-1) <= 2^{a+b-2} points.
 * L. A. Székely, "On the number of homogeneous subgraphs of a graph", Combinatorica 4 (1984)
   363-372, obtains the SAME normalized constant 1/2 in the graph-theoretic analogue (counting
   complete and independent subgraphs). No transfer between the settings is currently known.

The full current paper is attached. Work from it, not from memory."""

TAIL_MATH = r"""

GROUND RULES.
 * Exhibit real mathematics. A plan, a survey, or a restatement of the problem is worth nothing
   here. If you prove something, prove it; if you cannot, say exactly where the argument dies.
 * Do not fabricate. Every constant, inequality and citation must be one you can justify. If you
   are reasoning rather than citing, mark the sentence as such.
 * A SHARP OBSTRUCTION IS A VALUABLE RESULT. If the route cannot work, identify the precise
   configuration or step that blocks it. That is worth more to us than a hedged partial.
 * Any point set you propose will be checked in exact rational arithmetic against an independent
   verifier that counts caps, cups and convex subsets from orientation determinants only. An
   approximate or unchecked configuration is worthless.

End with: VERDICT: PROVED / PARTIAL (state exactly what) / OBSTRUCTED (state the obstruction) /
FAILED, then the cleanest statement of whatever you did establish."""

LANES = {

"verify51": (SETUP + r"""

YOUR LANE: ADVERSARIAL AUDIT OF THEOREM 5.1. DEFAULT TO REFUTATION.

This is the prerequisite for the whole campaign and it is the one page nobody has checked. Section
5 of the attached paper claims that every N-point DECOMPOSABLE set satisfies
log W(P) >= (1/2)(log N)^2 - O((log N)^{3/2}). Lemma 5.2 (the cap-cup product bound) has been
independently checked and is correct: the Cauchy-Schwarz step, the Bernoulli bound
(m_i/2)^{d_i} <= 1 + d_i(m_i/2 - 1) <= s_i + 1 via d_i <= 2 s_i/m_i, and the identity
sum d_i t_i = ((log s)^2 + sum d_i^2)/2 all verify.

WHAT HAS NOT BEEN CHECKED, and what you must attack, is the MULTISCALE RESET argument in the proof
of Theorem 5.1 itself: the heavy-path descent with the stopping rule n_i < N/2^{4R}, the split into
"fewer than R large levels" versus "at least R large levels", the definition of
Delta = 4R + 2 lambda + 1, the quantity F = (1/2)(L - Delta)^2 - 3L, the introduction of
mu = log M(P) and D = F - mu, the deepest-node bootstrap giving x_B, y_A >= 2D - L, the
per-attachment gain of D in one coordinate with monotone preservation of the other, and the final
counting of q_* >= ceil((R-1)/2) same-direction attachments yielding mu >= (q_*+2)D - 2L.

Attack specifically:
 1. Is the case split exhaustive, and are the two branches' constants consistent?
 2. In the nonlarge branch, the claim that more than (3/2) R L^2 nonlarge levels exist, that at
    least half have their discarded sibling on the same side, and that arbitrary subsets of fixed
    sibling leaves plus a terminal leaf give DISTINCT caps (or cups). Is that independence claim
    correct? Does it really follow "inductively upward from the mixed signs"?
 3. The monotonicity claims (5.x): X, Y, M nondecreasing from child to parent. Verify from the
    recurrences, including the max-structure.
 4. The two-alternative endgame: mu >= (q_*+2)D - 2L and mu >= ((q_*+2)/(q_*+3))F - 2L/(q_*+3).
    Check the algebra and that both alternatives really give (1/2)L^2 - O(L^{3/2}) with
    Delta = O(sqrt L) and q_* = Omega(sqrt L).
 5. Any place a max is silently treated as a sum, or an inequality is used in the wrong direction.

If the theorem is correct, say so and -- this matters more than the verdict -- extract THE REASON
IT WORKS in a form that might survive the removal of decomposability. Which steps use the tree,
and which only use the cap/cup recurrences? That is the seed of the general attack.""", False),

"attack_direct": (SETUP + r"""

YOUR LANE: PROVE THE GENERAL CAP-CUP PRODUCT LEMMA HEAD-ON.

Prove, for arbitrary N-point planar sets in general position:
    log C(P) + log U(P) >= (1/2 - o(1)) (log N)^2.

The decomposable proof (Lemma 5.2) works by descending a decomposition tree. An arbitrary point
set has no such tree, so you need a different engine. Directions worth real effort:

 1. **Iterate the cup-cap theorem instead of a tree.** Erdős-Szekeres: any set with no a-cap and
    no b-cup has at most C(a+b-4, a-2) points. So an N-point set has an a-cap or a b-cup whenever
    C(a+b-4,a-2) < N. Applied repeatedly after deleting the found chain, this yields many chains.
    The difficulty is that deletion destroys the count you are trying to accumulate. Can you set up
    a weighted or entropy version that does not lose the product structure?
 2. **The endpoint refinement.** For p < q let c(p,q), u(p,q) count caps/cups with those endpoints,
    and x(p) = 1 + sum_{q>p} c(p,q), y(q) = 1 + sum_{p<q} u(p,q). The paper's section 5 shows
    W = |P| + sum_{p<q} c(p,q)u(p,q). A lower bound on max_{p<q} c(p,q)u(p,q) suffices. Is there a
    single pair (p,q) that must carry 2^{(1/2 - o(1))(log N)^2} cap-cup pairs?
 3. **Entropy / supermultiplicativity.** The upper bound is a product because the construction is a
    product. Is there a submodularity or entropy inequality forcing log C + log U to be at least
    the value achieved by the extremal product configuration? Compare with how the graph analogue
    is handled.
 4. **Induction on N with a well-chosen split.** An arbitrary set has no strong separation, but it
    has a halving line, a ham-sandwich cut, or a convex-position extreme point. Does any canonical
    geometric split give a recurrence of the shape R(P) >= sqrt(m+1) R(P') that the Lemma 5.2
    telescoping can consume? The obstruction is that a generic split does NOT give the clean
    cap/cup classification that strong separation gives -- caps can use many points on both sides.
    Quantify how much that costs; a lossy split may still give 1/2 if the loss is o((log N)^2).

Prove as much as you can. If the full lemma resists, a bound with any constant strictly greater
than 1/4 for arbitrary sets is already a genuine improvement on the published state of the art and
should be stated cleanly with its exact constant.""" + TAIL_MATH, False),

"attack_szekely": (SETUP + r"""

YOUR LANE: TRANSFER SZÉKELY'S GRAPH ARGUMENT.

L. A. Székely, "On the number of homogeneous subgraphs of a graph", Combinatorica 4 (1984)
363-372, obtains the SAME normalized constant 1/2 for counting complete and independent subgraphs
of an arbitrary graph. Our prior-art file currently records this as an unexplained coincidence and
says "no transfer between the two settings is known". Nobody has actually tried. You are trying.

Do this concretely:
 1. **Get Székely's actual argument.** Find the paper or a faithful account of it. State the exact
    theorem and the exact method (it is a Ramsey-multiplicity-style counting argument). Quote the
    statement; do not paraphrase from memory.
 2. **Identify the dictionary.** Caps and cups in a planar point set behave like cliques and
    independent sets under the Erdős-Szekeres cup-cap theorem, which is the geometric analogue of
    the Ramsey bound R(a,b) <= C(a+b-2,a-1). The correspondence is not a formal reduction --
    3-uniform orientation structure is not a graph -- so say precisely where it holds and where it
    breaks. Baek-Balko's ordered-hypergraph section is relevant: they show a corresponding
    generalization of the Erdős-Szekeres conjecture is FALSE in the abstract 3-uniform setting,
    which is a warning that naive transfer fails.
 3. **Try the transfer anyway, quantitatively.** Does Székely's counting method, run on the
    cap/cup structure with the cup-cap theorem in place of the Ramsey bound, produce
    log C + log U >= (1/2 - o(1))(log N)^2? If it does, that resolves the problem. If it fails,
    identify the exact step that needs graph structure the point set does not supply.
 4. **Explain the coincidence either way.** Two constants agreeing at 1/2 is either a shared
    mechanism or an accident. A referee will ask. Answer it.

This lane may be the highest-value one in the campaign: an existing argument that already reaches
the target constant in a neighbouring category.""" + TAIL_MATH, True),

"attack_tree": (SETUP + r"""

YOUR LANE: THE CANONICAL TREE DECOMPOSITION ROUTE.

We have the target constant for DECOMPOSABLE sets (recursive strong separations). The gap is
arbitrary order types. There is a literature on canonically decomposing order types into trees
that may be exactly the missing bridge, and nobody in this project has read it.

 1. **Read the actual papers.** At least: "A Canonical Tree Decomposition for Chirotopes"
    (SoCG 2024, DROPS/LIPIcs) and "A Canonical Tree Decomposition for Order Types, and Some
    Applications" (SIAM J. Discrete Math.). Also Balko-Kynčl-Langerman-Pilz, Electron. J. Combin.
    24(4) (2017) P4.24, where decomposable sets are defined, and any follow-up on the structure of
    general order types. State what these decompositions actually produce -- the nodes, the leaves,
    what is canonical, what is lost.
 2. **The decisive question.** Does every order type admit a decomposition whose internal nodes
    behave enough like a strong separation that the Lemma 5.2 recurrence
    R(A<B) >= sqrt(|B|+1)R(A) + sqrt(|A|+1)R(B) survives, possibly with a worse constant? If the
    node types are richer (not just "deep below"), work out the cap/cup classification at EACH node
    type and the corresponding recurrence. The campaign only needs the resulting constant to be
    1/2 - o(1); constant-factor losses per node are fatal only if they compound over log N levels.
 3. **If the decomposition is not strong enough**, say precisely which node type breaks the
    recurrence and what the worst case looks like. That is a sharp obstruction and directs the
    rest of the campaign.

Be concrete about what the cited papers actually prove. Do not assume a decomposition exists in the
form we want because it would be convenient.""" + TAIL_MATH, True),

"break_lemma": (SETUP + r"""

YOUR LANE: REFUTE THE GENERAL CAP-CUP PRODUCT LEMMA.

Your job is to build an N-point planar set in general position with
    log C(P) + log U(P) < (1/2 - delta)(log N)^2
for some fixed delta > 0 and arbitrarily large N. If you succeed, the campaign's target lemma is
false and we stop immediately.

Note carefully what you are NOT being asked. You are not asked to beat the coefficient 1/2 for
W(P) -- that is another lane. The product bound could in principle fail while W is still large,
since W is governed by max_{p<q} c(p,q)u(p,q) rather than by the global product. Distinguishing
these two is itself useful: if the product lemma is false but the W bound survives, the campaign
needs to be re-aimed at the endpoint-localized quantity instead.

Where to look:
 * Decomposable sets are excluded -- the paper proves the bound there. So you need genuinely
   non-decomposable order types. What do those look like? Balko-Kynčl-Langerman-Pilz define
   decomposability; sets that are NOT decomposable are the entire search space.
 * Point sets with unusually few caps AND few cups simultaneously. The cup-cap theorem forces one
   of them to be long, but "long" is not "many". Can a set have a long cap yet very few caps?
 * Random point sets, convex position, grids, Horton sets, Valtr's constructions, projective or
   algebraic configurations, and sets built to be far from any recursive separation.
 * Small cases: compute C, U exactly for every order type on up to 8 or 9 points if you can, and
   see whether the minimum of log C + log U tracks (1/2)(log N)^2 or falls below it. Small-case
   data is genuinely informative here and we can verify it exactly.

If after real effort you cannot break it, say so plainly and report WHICH structural feature
proved most robust -- that tells the proving lanes where the strength lies.""" + TAIL_MATH, False),

"break_target": (SETUP + r"""

YOUR LANE: IS 1/2 EVEN THE RIGHT ANSWER? ATTACK THE UPPER SIDE.

The entire campaign assumes the truth is 1/2 and only the lower bound is missing. TEST THAT
ASSUMPTION. Your job is to construct a family of point sets with

    log v(P) <= (1/2 - delta)(log N)^2

for some fixed delta > 0, which would push limsup below 1/2 and prove the campaign is aimed at the
wrong number. This is the most valuable single outcome this run could produce, because it would
stop us wasting the whole budget on a false target.

What already blocks the easy routes, and what it does not cover:
 * Proposition 4.4 of the attached paper: no FIXED-TEMPLATE iteration beats 1/2. The proof is the
   cup-cap theorem, r <= C(a+b-2,a-1) <= 2^{a+b-2}, giving (a+b-2)/(2 log r) >= 1/2. This covers
   only iterations of a single fixed template.
 * Theorem 5.1: no DECOMPOSABLE set beats 1/2 (modulo the audit running in another lane).
 * NEITHER covers: non-stationary iterations with the template growing with the level; blow-ups
   that are not uniform (different Q at different points, as in Baek-Balko's (X,Y)-blow-ups with
   varying x_i, y_i); constructions that are not blow-ups at all; or genuinely non-decomposable
   order types.

So the live space is real. Push on it:
 1. Level-dependent templates S_1, S_2, ... with sizes and cap/cup profiles varying with depth. The
    fixed-template coefficient is (a+b-2)/(2 log r); a varying schedule optimizes a different
    functional. Set it up exactly and minimize.
 2. Non-uniform blow-ups in the style of Baek-Balko Definition 13, where each point is replaced by
    a DIFFERENT cap/cup-extremal set. Derive the analogue of the paper's Lemma 2.2 identities for
    that operation and see what coefficient it can reach.
 3. Horton sets, Valtr's constructions, and any known family with few convex subsets.
 4. Argue in the other direction if you conclude 1/2 is right: give the strongest evidence you can
    that no construction beats 1/2, ideally a general lower bound on log v(P) for ALL blow-up-type
    constructions, not just fixed-template ones. That would materially strengthen the campaign's
    premise.""" + TAIL_MATH, False),

"priorart": (SETUP + r"""

YOUR LANE: PRIOR-ART KILL-SEARCH ON THE LOWER BOUND. Assume it is already done and find where.

House rule: "open in a database" is NOT evidence of open, and this project has repeatedly lost time
to stale status. Today alone: Casas-Alvero was already a theorem when we ranked it second; the
lonely runner frontier had moved 7 -> 13 runners in twelve months; a Seymour bound we planned a
campaign around was broken. Assume the same here.

Find out:
 1. **Has anyone improved the 1/4 lower bound for f(N)?** Any constant above 1/4, any claim that
    the limit exists, any claim about its value. Search Erdős problem 838 and its discussion
    thread, the Morris-Soltan survey and everything citing it, Suk's and Holmsen-Nassajian
    Mojarrad-Pach-Tardos's citation neighbourhoods, and 2024-2026 arXiv.
 2. **Has anyone counted caps and cups the way we need?** A bound of the form
    log C + log U >= c (log N)^2 for arbitrary sets, under any name -- Ramsey multiplicity for
    caps/cups, counting monotone paths, counting convex chains. The ordered-graph and
    monotone-path literature (Moshkovitz-Shapira, Fox-Pach-Sudakov-Suk, Mirzaei-Suk) is the
    natural place.
 3. **Is Székely's constant already known to transfer?** Anyone who has connected homogeneous
    subgraph counting to cap/cup or convex-position counting.
 4. **Erdős 838's own status.** Check the erdosproblems.com entry, its forum thread, and the
    teorth/erdosproblems AI-contributions wiki, which tracks recent AI resolutions. Three further
    Erdős problems were resolved on 2026-08-01 by OpenAI's Astra and the numbers were not
    published in the coverage we saw -- confirm 838 is not among them.
 5. Anything that makes the whole campaign moot.

Report exact references, dates and what each says. State plainly what you could NOT check.
End with: VERDICT: RED (already done -- give the reference) / AMBER (adjacent work we must cite) /
GREEN (nothing found; state your coverage).""", True),
}


def retry(fn, what, tries=60, wait=30):
    for i in range(tries):
        try:
            return fn()
        except (openai.APIConnectionError, openai.APITimeoutError, openai.InternalServerError) as e:
            print(f"  ({what}: {type(e).__name__}, retry {i+1}/{tries})", flush=True)
            time.sleep(wait)
    raise RuntimeError(what)


def run(name):
    prompt, websearch = LANES[name]
    client = openai.OpenAI(api_key=KEY)
    with _lock:
        known = json.loads(IDS.read_text()) if IDS.exists() else {}
    if name in known:
        print(f"{name}: resuming {known[name]}", flush=True)
        resp = retry(lambda: client.responses.retrieve(known[name]), f"{name} retrieve")
    else:
        kw = {"tools": [{"type": "web_search", "search_context_size": "high"}]} if websearch else {}
        resp = retry(lambda: client.responses.create(
            model=MODEL, input=[{"role": "user", "content": prompt + PAPER}],
            reasoning={"effort": EFFORT}, background=True, **kw), f"{name} create")
        with _lock:
            known = json.loads(IDS.read_text()) if IDS.exists() else {}
            known[name] = resp.id
            IDS.write_text(json.dumps(known, indent=1))
        print(f"{name}: submitted ({MODEL}, effort={EFFORT}"
              f"{', web_search' if websearch else ''}), id = {resp.id}", flush=True)
    t0 = time.time()
    while resp.status in ("queued", "in_progress"):
        if time.time() - t0 > 21600:
            raise TimeoutError(name)
        time.sleep(20)
        resp = retry(lambda: client.responses.retrieve(resp.id), f"{name} poll")
    if resp.status != "completed":
        raise RuntimeError(f"{name}: {resp.status}: {getattr(resp, 'error', None)}")
    out = BASE / f"campaign_lower_{name}_20260813.md"
    out.write_text(f"# Erdős 838 lower-bound campaign — {name} ({MODEL}, effort={EFFORT}, "
                   f"{time.strftime('%Y-%m-%d %H:%M')})\n\n"
                   "> Target: log C + log U >= (1/2 - o(1))(log N)^2 for ARBITRARY point sets.\n"
                   "> With Theorem 1.1 already proved, this resolves Erdős 838 outright.\n\n"
                   + resp.output_text)
    print(f"{name}: completed, {len(resp.output_text)} chars -> {out.name}", flush=True)


if __name__ == "__main__":
    names = sys.argv[1:] or list(LANES)
    ths = [threading.Thread(target=run, args=(n,)) for n in names]
    for t in ths:
        t.start()
        time.sleep(3)
    for t in ths:
        t.join()
