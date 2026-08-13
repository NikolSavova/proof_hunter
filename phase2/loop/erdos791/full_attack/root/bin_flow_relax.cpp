#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <queue>
#include <random>
#include <string>
#include <vector>

struct Edge {
  int to, rev;
  double cap;
};

struct Dinic {
  explicit Dinic(int n) : g(n), level(n), it(n) {}
  std::vector<std::vector<Edge>> g;
  std::vector<int> level, it;

  void add_edge(int u, int v, double c) {
    Edge a{v, static_cast<int>(g[v].size()), c};
    Edge b{u, static_cast<int>(g[u].size()), 0.0};
    g[u].push_back(a);
    g[v].push_back(b);
  }

  bool bfs(int s, int t) {
    std::fill(level.begin(), level.end(), -1);
    std::queue<int> q;
    level[s] = 0;
    q.push(s);
    while (!q.empty()) {
      int u = q.front();
      q.pop();
      for (const auto &e : g[u]) {
        if (e.cap > 1e-13 && level[e.to] < 0) {
          level[e.to] = level[u] + 1;
          q.push(e.to);
        }
      }
    }
    return level[t] >= 0;
  }

  double dfs(int u, int t, double f) {
    if (u == t) return f;
    for (int &z = it[u]; z < static_cast<int>(g[u].size()); ++z) {
      Edge &e = g[u][z];
      if (e.cap <= 1e-13 || level[e.to] != level[u] + 1) continue;
      double got = dfs(e.to, t, std::min(f, e.cap));
      if (got > 1e-13) {
        e.cap -= got;
        g[e.to][e.rev].cap += got;
        return got;
      }
    }
    return 0.0;
  }

  double flow(int s, int t) {
    double ans = 0.0;
    while (bfs(s, t)) {
      std::fill(it.begin(), it.end(), 0);
      while (double f = dfs(s, t, 1e100)) ans += f;
    }
    return ans;
  }
};

// For fixed bin masses p, compute the largest c for which c/m units can be
// routed to each target bin.  A pair cell (i,j) can reach target bins i+j and
// i+j+1.  Its normalized unordered-pair supply is p_i p_j (i<j) or p_i^2/2.
double objective(const std::vector<double> &p) {
  const int m = static_cast<int>(p.size());
  struct Cell { int i, j; double supply; };
  std::vector<Cell> cells;
  for (int i = 0; i < m; ++i) {
    for (int j = i; j < m && i + j < m; ++j) {
      double supply = (i == j ? 0.5 * p[i] * p[i] : p[i] * p[j]);
      if (supply > 1e-18) cells.push_back({i, j, supply});
    }
  }
  auto feasible = [&](double d) {
    int source = 0;
    int cell0 = 1;
    int bin0 = cell0 + static_cast<int>(cells.size());
    int sink = bin0 + m;
    Dinic net(sink + 1);
    for (int z = 0; z < static_cast<int>(cells.size()); ++z) {
      const auto &cell = cells[z];
      net.add_edge(source, cell0 + z, cell.supply);
      int s0 = cell.i + cell.j;
      net.add_edge(cell0 + z, bin0 + s0, 1.0);
      if (s0 + 1 < m) net.add_edge(cell0 + z, bin0 + s0 + 1, 1.0);
    }
    for (int s = 0; s < m; ++s) net.add_edge(bin0 + s, sink, d);
    return net.flow(source, sink) >= m * d - 2e-11;
  };
  double lo = 0.0, hi = 0.5 / m;
  for (int z = 0; z < 55; ++z) {
    double mid = (lo + hi) * 0.5;
    if (feasible(mid)) lo = mid; else hi = mid;
  }
  return m * lo;
}

int main(int argc, char **argv) {
  int m = argc > 1 ? std::stoi(argv[1]) : 8;
  int restarts = argc > 2 ? std::stoi(argv[2]) : 40;
  int steps = argc > 3 ? std::stoi(argv[3]) : 20000;
  uint64_t seed = argc > 4 ? std::stoull(argv[4]) : 791;
  std::mt19937_64 rng(seed);
  std::uniform_real_distribution<double> unif(0.0, 1.0);

  std::vector<double> global_p(m, 1.0 / m);
  double global = objective(global_p);
  for (int r = 0; r < restarts; ++r) {
    std::vector<double> p(m);
    double total = 0.0;
    for (double &x : p) {
      x = -std::log(std::max(1e-15, unif(rng)));
      total += x;
    }
    for (double &x : p) x /= total;
    double cur = objective(p);
    double best = cur;
    std::vector<double> best_p = p;
    for (int z = 0; z < steps; ++z) {
      double frac = static_cast<double>(z) / std::max(1, steps - 1);
      double scale = 0.12 * std::pow(1e-4, frac);
      double temp = 0.002 * std::pow(1e-5, frac);
      int i = static_cast<int>(rng() % m);
      int j = static_cast<int>(rng() % (m - 1));
      if (j >= i) ++j;
      double amount = std::min(p[i], scale * unif(rng));
      p[i] -= amount;
      p[j] += amount;
      double next = objective(p);
      bool accept = next >= cur || unif(rng) < std::exp((next - cur) / temp);
      if (accept) {
        cur = next;
        if (cur > best) {
          best = cur;
          best_p = p;
        }
      } else {
        p[j] -= amount;
        p[i] += amount;
      }
    }
    if (best > global) {
      global = best;
      global_p = best_p;
    }
    std::cerr << "restart " << (r + 1) << "/" << restarts
              << " best=" << std::setprecision(12) << global << "\n";
  }

  std::cout << std::setprecision(15);
  std::cout << "{\n  \"bins\": " << m << ",\n  \"heuristic_lower_bound_on_relaxation_optimum\": "
            << global << ",\n  \"masses\": [";
  for (int i = 0; i < m; ++i) {
    if (i) std::cout << ", ";
    std::cout << global_p[i];
  }
  std::cout << "]\n}\n";
}
