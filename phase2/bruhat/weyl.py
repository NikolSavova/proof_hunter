"""Generic finite Weyl group construction from a Cartan matrix.

Elements are integer matrices acting on the simple-root basis (tuples of tuples,
hashable). Everything is built from first principles + BFS, with independent
internal cross-checks so no single piece of code needs to be trusted alone:

  1. |W| is asserted against the known order formula per type.
  2. Coxeter length via BFS (Cayley-graph distance) is asserted equal to the
     inversion count #{positive roots sent negative} for EVERY element.
  3. The level sizes (# elements per length) are asserted equal to the
     coefficients of the Poincare polynomial prod_i (q^{d_i}-1)/(q-1) from the
     known degrees d_i per type.
  4. #positive roots is asserted against the known count per type.

Bruhat order is built from covering relations u <| v  iff  v = u*t for a
reflection t with l(v) = l(u)+1 (standard; its transitive closure is Bruhat
order by the chain property).
"""

from math import factorial


# ---------------------------------------------------------------- Cartan data

def cartan(typ: str, n: int):
    """Cartan matrix A with A[i][j] = 2(a_i,a_j)/(a_i,a_i); s_i(a_j) = a_j - A[i][j] a_i."""
    A = [[2 if i == j else 0 for j in range(n)] for i in range(n)]

    def link(i, j, aij=-1, aji=-1):
        A[i][j], A[j][i] = aij, aji

    if typ == "A":
        for i in range(n - 1):
            link(i, i + 1)
    elif typ == "B":  # last simple root short
        for i in range(n - 2):
            link(i, i + 1)
        if n >= 2:
            link(n - 2, n - 1, aij=-1, aji=-2)
    elif typ == "D":
        assert n >= 3
        for i in range(n - 2):
            link(i, i + 1)
        link(n - 3, n - 1)  # fork
    elif typ == "E":
        assert n in (6, 7, 8)
        # Bourbaki numbering: node 1 (idx 1) hangs off idx 2 of the chain 0-2-3-4-...
        # We use: chain 0-2-3-4-5(-6-7), branch node idx 1 attached to idx 3.
        chain = [0, 2, 3, 4, 5, 6, 7][:n - 1]
        for a, b in zip(chain, chain[1:]):
            link(a, b)
        link(1, 3)
    elif typ == "G":
        assert n == 2
        link(0, 1, aij=-1, aji=-3)
    elif typ == "F":
        assert n == 4
        link(0, 1)
        link(1, 2, aij=-2, aji=-1)
        link(2, 3)
    else:
        raise ValueError(typ)
    return A


ORDER = {  # known |W|
    "A": lambda n: factorial(n + 1),
    "B": lambda n: 2 ** n * factorial(n),
    "D": lambda n: 2 ** (n - 1) * factorial(n),
    "E": lambda n: {6: 51840, 7: 2903040, 8: 696729600}[n],
    "G": lambda n: 12,
    "F": lambda n: 1152,
}

NPOS = {  # known #positive roots
    "A": lambda n: n * (n + 1) // 2,
    "B": lambda n: n * n,
    "D": lambda n: n * (n - 1),
    "E": lambda n: {6: 36, 7: 63, 8: 120}[n],
    "G": lambda n: 6,
    "F": lambda n: 24,
}

DEGREES = {  # fundamental degrees d_i (Poincare poly = prod (q^d - 1)/(q - 1))
    "A": lambda n: list(range(2, n + 2)),
    "B": lambda n: list(range(2, 2 * n + 1, 2)),
    "D": lambda n: list(range(2, 2 * n - 1, 2)) + [n],
    "E": lambda n: {6: [2, 5, 6, 8, 9, 12],
                    7: [2, 6, 8, 10, 12, 14, 18],
                    8: [2, 8, 12, 14, 18, 20, 24, 30]}[n],
    "G": lambda n: [2, 6],
    "F": lambda n: [2, 6, 8, 12],
}


# ------------------------------------------------------------- linear algebra

def gen_matrix(A, i, n):
    """Matrix of s_i on the simple-root basis: identity with row i -> delta - A[i]."""
    return tuple(
        tuple((1 if r == c else 0) - (A[i][c] if r == i else 0) for c in range(n))
        for r in range(n)
    )


def matmul(X, Y):
    n = len(X)
    return tuple(
        tuple(sum(X[r][k] * Y[k][c] for k in range(n)) for c in range(n))
        for r in range(n)
    )


def apply(M, v):
    return tuple(sum(M[r][c] * v[c] for c in range(len(v))) for r in range(len(v)))


# ------------------------------------------------------------------ the group

class WeylGroup:
    def __init__(self, typ: str, n: int):
        self.typ, self.n = typ, n
        self.name = f"{typ}{n}"
        A = cartan(typ, n)
        gens = [gen_matrix(A, i, n) for i in range(n)]
        ident = tuple(tuple(1 if r == c else 0 for c in range(n)) for r in range(n))

        # --- BFS over the Cayley graph: elements, lengths, one reduced word each
        length = {ident: 0}
        word = {ident: ()}
        frontier = [ident]
        while frontier:
            nxt = []
            for w in frontier:
                for i, g in enumerate(gens):
                    ws = matmul(w, g)
                    if ws not in length:
                        length[ws] = length[w] + 1
                        word[ws] = word[w] + (i + 1,)  # 1-indexed letters
                        nxt.append(ws)
            frontier = nxt
        assert len(length) == ORDER[typ](n), f"|W({self.name})| mismatch"

        # --- roots: orbit of simple roots; positive = all coords >= 0
        simple = [tuple(1 if k == i else 0 for k in range(n)) for i in range(n)]
        roots = set(simple)
        frontier = list(simple)
        while frontier:
            nxt = []
            for r in frontier:
                for g in gens:
                    gr = apply(g, r)
                    if gr not in roots:
                        roots.add(gr)
                        nxt.append(gr)
            frontier = nxt
        pos = [r for r in roots if all(c >= 0 for c in r)]
        assert len(pos) == NPOS[typ](n), f"#pos roots({self.name}) mismatch"
        assert len(roots) == 2 * len(pos)

        # --- cross-check: BFS length == inversion count, for every element
        for w in length:
            inv = sum(1 for r in pos if any(c < 0 for c in apply(w, r)))
            assert inv == length[w], f"length mismatch in {self.name}"

        # --- cross-check: level sizes == Poincare polynomial coefficients
        poincare = [1]
        for d in DEGREES[typ](n):
            poincare = [sum(poincare[k - j] for j in range(min(d, k + 1))
                            if 0 <= k - j < len(poincare))
                        for k in range(len(poincare) + d - 1)]
        maxlen = max(length.values())
        levels = [0] * (maxlen + 1)
        for w in length:
            levels[length[w]] += 1
        assert levels == poincare, f"Poincare mismatch in {self.name}"

        # --- index elements 0..N-1 (sorted by length for readability)
        elems = sorted(length, key=lambda w: (length[w], word[w]))
        idx = {w: i for i, w in enumerate(elems)}
        N = len(elems)

        # --- reflections: all conjugates of generators (== one per positive root)
        invs = {ident: ident}
        for w in elems:  # inverse via reversed reduced word
            m = ident
            for letter in reversed(word[w]):
                m = matmul(m, gens[letter - 1])
            invs[w] = m
        T = set()
        for w in elems:
            for g in gens:
                T.add(matmul(matmul(w, g), invs[w]))
        assert len(T) == len(pos), f"#reflections({self.name}) mismatch"

        # --- Bruhat covers:  u <| u*t  when l(u*t) = l(u)+1
        covers_up = [[] for _ in range(N)]  # covers_up[u] = list of v covering u
        for w in elems:
            lu, u = length[w], idx[w]
            for t in T:
                wt = matmul(w, t)
                if length[wt] == lu + 1:
                    covers_up[u].append(idx[wt])

        # --- up-sets / down-sets as int bitsets (order ideals via DP over levels)
        up = [0] * N
        for u in range(N - 1, -1, -1):
            m = 1 << u
            for v in covers_up[u]:
                m |= up[v]
            up[u] = m
        covers_down = [[] for _ in range(N)]
        for u in range(N):
            for v in covers_up[u]:
                covers_down[v].append(u)
        down = [0] * N
        for v in range(N):  # increasing length: covered elements already done
            m = 1 << v
            for u in covers_down[v]:
                m |= down[u]
            down[v] = m
        levelmask = [0] * (maxlen + 1)
        for w in elems:
            levelmask[length[w]] |= 1 << idx[w]

        self.N, self.maxlen = N, maxlen
        self.elems, self.idx = elems, idx
        self.length = [length[w] for w in elems]
        self.word = [word[w] for w in elems]
        self.up, self.down, self.levelmask = up, down, levelmask

    def rank_sequence(self, u: int, v: int):
        """Rank sequence (a_0..a_d) of the Bruhat interval [u,v]; None if u !<= v."""
        if not (self.up[u] >> v) & 1:
            return None
        mask = self.up[u] & self.down[v]
        lu, lv = self.length[u], self.length[v]
        return [(mask & self.levelmask[l]).bit_count() for l in range(lu, lv + 1)]
