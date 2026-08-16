// Anneal the existential arbitrary-point rooted-amortization inequality.
//
// A state is a reduced word for w_0.  For every wire e we delete that wire,
// replay the two scalar reverse matrix products, and evaluate
//
//   rho_e = (Z(1/2) + (n-1) W_e) / (2 V_e),
//
// where V_e and W_e are the unit and half-weight masses of convex faces
// containing e.  The existential RA conjecture says min_e rho_e <= 1.
// Thus a state with min_e rho_e > 1 is an abstract allowable-sequence
// counterexample (which must subsequently be tested for stretchability).

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

using Word = std::vector<int>;
using Roots = std::vector<std::pair<int, int>>;

Word bubble_word(int n) {
  Word w;
  for (int top = 1; top < n; ++top)
    for (int i = top - 1; i >= 0; --i) w.push_back(i);
  return w;
}

Roots roots_from_word(int n, const Word& w) {
  std::vector<int> order(n);
  std::iota(order.begin(), order.end(), 0);
  Roots roots;
  roots.reserve(w.size());
  for (int s : w) {
    int a = order[s], b = order[s + 1];
    if (a > b) std::abort();
    roots.push_back({a, b});
    std::swap(order[s], order[s + 1]);
  }
  return roots;
}

long double trace_at(int n, const Roots& roots, long double z) {
  std::vector<long double> a(n * n, 0), b(n * n, 0);
  for (int i = 0; i < n; ++i) a[i * n + i] = b[i * n + i] = 1;
  for (auto [i, j] : roots)
    for (int c = 0; c < n; ++c) b[j * n + c] += z * b[i * n + c];
  for (auto it = roots.rbegin(); it != roots.rend(); ++it) {
    auto [i, j] = *it;
    for (int c = 0; c < n; ++c) a[j * n + c] += z * a[i * n + c];
  }
  long double q = 0;
  for (int k = 0; k < n * n; ++k) q += a[k] * b[k];
  return q;
}

std::pair<long double, long double> partition(int n, const Roots& roots) {
  long double q1 = trace_at(n, roots, 1.0L);
  long double qh = trace_at(n, roots, 0.5L);
  return {q1 + 1.0L, qh + 1.0L - n / 2.0L};
}

Roots delete_wire(const Roots& roots, int omitted) {
  Roots child;
  child.reserve(roots.size());
  for (auto [i, j] : roots) {
    if (i == omitted || j == omitted) continue;
    if (i > omitted) --i;
    if (j > omitted) --j;
    child.push_back({i, j});
  }
  return child;
}

struct Score {
  long double minimum_ratio = 0;
  long double average_margin = 0;
  int pass_count = 0;
  int minimizer = -1;
};

Score evaluate(int n, const Word& word) {
  Roots roots = roots_from_word(n, word);
  auto [v, w] = partition(n, roots);
  Score score;
  score.minimum_ratio = 1e100L;
  long double margin_sum = 0;
  for (int e = 0; e < n; ++e) {
    Roots child = delete_wire(roots, e);
    auto [vc, wc] = partition(n - 1, child);
    long double ve = v - vc, we = w - wc;
    long double ratio = (w + (n - 1) * we) / (2 * ve);
    long double margin = 2 * ve - w - (n - 1) * we;
    margin_sum += margin;
    if (margin >= 0) ++score.pass_count;
    if (ratio < score.minimum_ratio) {
      score.minimum_ratio = ratio;
      score.minimizer = e;
    }
  }
  score.average_margin = margin_sum / n;
  return score;
}

int main(int argc, char** argv) {
  if (argc < 5) {
    std::cerr << "usage: search_existential_ra n steps seed output [word]\n";
    return 2;
  }
  int n = std::stoi(argv[1]);
  long long steps = std::stoll(argv[2]);
  uint64_t seed = std::stoull(argv[3]);
  std::string output = argv[4];
  Word word;
  if (argc >= 6 && std::string(argv[5]) == "word") {
    word.resize(n * (n - 1) / 2);
    for (int& x : word)
      if (!(std::cin >> x)) return 2;
  } else {
    word = bubble_word(n);
  }
  std::mt19937_64 rng(seed);
  std::uniform_real_distribution<long double> uniform(0, 1);
  Score current = evaluate(n, word), best = current;
  Word best_word = word;
  std::cerr << "start min_ratio=" << std::setprecision(12)
            << (double)current.minimum_ratio << " passes=" << current.pass_count
            << " average_margin=" << (double)current.average_margin << "\n";
  long long evaluated = 0, accepted = 0, commuted = 0;
  for (long long step = 0; step < steps; ++step) {
    std::vector<int> commutations, braids;
    for (int i = 0; i + 1 < (int)word.size(); ++i)
      if (std::abs(word[i] - word[i + 1]) > 1) commutations.push_back(i);
    for (int i = 0; i + 2 < (int)word.size(); ++i)
      if (word[i] == word[i + 2] && std::abs(word[i] - word[i + 1]) == 1)
        braids.push_back(i);
    if (!commutations.empty() && (braids.empty() || (rng() & 3))) {
      int k = commutations[rng() % commutations.size()];
      std::swap(word[k], word[k + 1]);
      ++commuted;
      continue;
    }
    if (braids.empty()) continue;
    int k = braids[rng() % braids.size()];
    int x = word[k], y = word[k + 1];
    word[k] = y; word[k + 1] = x; word[k + 2] = y;
    Score candidate = evaluate(n, word);
    ++evaluated;
    long double phase = (step % 20000) / 19999.0L;
    long double temperature = 0.003L * (1 - phase) + 0.000002L;
    long double difference = candidate.minimum_ratio - current.minimum_ratio;
    bool take = difference >= 0 || uniform(rng) < std::exp(difference / temperature);
    if (take) {
      current = candidate;
      ++accepted;
    } else {
      word[k] = x; word[k + 1] = y; word[k + 2] = x;
    }
    if (current.minimum_ratio > best.minimum_ratio) {
      best = current;
      best_word = word;
      std::cerr << "best step=" << step
                << " min_ratio=" << (double)best.minimum_ratio
                << " passes=" << best.pass_count
                << " avg_margin=" << (double)best.average_margin
                << " minimizer=" << best.minimizer << "\n";
      if (best.minimum_ratio > 1) break;
    }
  }
  std::ofstream out(output);
  out << "{\n  \"n\": " << n
      << ",\n  \"minimum_RA_ratio\": " << std::setprecision(18)
      << (double)best.minimum_ratio
      << ",\n  \"RA_pass_count\": " << best.pass_count
      << ",\n  \"average_margin\": " << (double)best.average_margin
      << ",\n  \"evaluated_braids\": " << evaluated
      << ",\n  \"accepted_braids\": " << accepted
      << ",\n  \"commutations\": " << commuted
      << ",\n  \"word_zero_based\": [";
  for (size_t i = 0; i < best_word.size(); ++i) {
    if (i) out << ',';
    out << best_word[i];
  }
  out << "]\n}\n";
  std::cerr << "final min_ratio=" << (double)best.minimum_ratio
            << " passes=" << best.pass_count << "\n";
}
