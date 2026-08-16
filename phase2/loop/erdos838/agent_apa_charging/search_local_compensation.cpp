// Heuristic allowable-sequence search for
//
//   H(P) * max(0, 1 - (mu_1(P)-mu_(1/2)(P))).
//
// This quantity controls positive growth in the exact omitted-point
// recurrence.  Braid-moved outputs are not automatically stretchable.

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <utility>
#include <vector>

using Word = std::vector<int>;
using Roots = std::vector<std::pair<int, int>>;

Roots roots_from_word(int n, const Word& word) {
  std::vector<int> wires(n);
  std::iota(wires.begin(), wires.end(), 0);
  Roots roots;
  for (int s : word) {
    int a = wires[s], b = wires[s + 1];
    if (a > b) std::abort();
    roots.push_back({a, b});
    std::swap(wires[s], wires[s + 1]);
  }
  return roots;
}

// Return Z(z) and z Z'(z), including the empty face.
std::pair<long double, long double>
value_moment(int n, const Roots& roots, long double z) {
  std::vector<long double> a(n * n, 0), b(n * n, 0);
  std::vector<long double> da(n * n, 0), db(n * n, 0);
  for (int i = 0; i < n; ++i) a[i * n + i] = b[i * n + i] = 1;
  for (auto [i, j] : roots) {
    for (int c = 0; c < n; ++c) {
      db[j * n + c] += z * (db[i * n + c] + b[i * n + c]);
      b[j * n + c] += z * b[i * n + c];
    }
  }
  for (auto it = roots.rbegin(); it != roots.rend(); ++it) {
    auto [i, j] = *it;
    for (int c = 0; c < n; ++c) {
      da[j * n + c] += z * (da[i * n + c] + a[i * n + c]);
      a[j * n + c] += z * a[i * n + c];
    }
  }
  long double q = 0, m = 0;
  for (int k = 0; k < n * n; ++k) {
    q += a[k] * b[k];
    m += da[k] * b[k] + a[k] * db[k];
  }
  return {1 + n * z + q - n, n * z + m};
}

struct Score {
  long double compensation, h, delta, mu1, muh;
};

Score evaluate(int n, const Word& word) {
  Roots roots = roots_from_word(n, word);
  auto [v, m1] = value_moment(n, roots, 1);
  auto [w, mh] = value_moment(n, roots, 0.5L);
  long double h = n * w / v;
  long double mu1 = m1 / v, muh = mh / w;
  long double delta = mu1 - muh;
  return {h * std::max(0.0L, 1 - delta), h, delta, mu1, muh};
}

int main(int argc, char** argv) {
  if (argc < 6 || std::string(argv[5]) != "word") {
    std::cerr << "usage: search_local_compensation n steps seed output word < generators\n";
    return 2;
  }
  int n = std::stoi(argv[1]);
  long long steps = std::stoll(argv[2]);
  uint64_t seed = std::stoull(argv[3]);
  std::string output = argv[4];
  Word word(n * (n - 1) / 2);
  for (int& x : word) if (!(std::cin >> x)) return 2;
  std::mt19937_64 rng(seed);
  std::uniform_real_distribution<long double> uniform(0, 1);
  Score current = evaluate(n, word), best = current;
  Word best_word = word;
  long long evaluated = 0, accepted = 0, commuted = 0;
  std::cerr << "start comp=" << std::setprecision(12)
            << (double)current.compensation << " H=" << (double)current.h
            << " delta=" << (double)current.delta << "\n";
  for (long long step = 0; step < steps; ++step) {
    std::vector<int> commutations, braids;
    for (int i = 0; i + 1 < (int)word.size(); ++i)
      if (std::abs(word[i] - word[i + 1]) > 1) commutations.push_back(i);
    for (int i = 0; i + 2 < (int)word.size(); ++i)
      if (word[i] == word[i + 2] && std::abs(word[i] - word[i + 1]) == 1)
        braids.push_back(i);
    if (!commutations.empty() && (braids.empty() || (rng() & 1))) {
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
    long double temperature = 0.01L * (1 - phase) + 0.00001L;
    long double difference = candidate.compensation - current.compensation;
    bool take = difference >= 0 || uniform(rng) < std::exp(difference / temperature);
    if (take) {
      current = candidate;
      ++accepted;
    } else {
      word[k] = x; word[k + 1] = y; word[k + 2] = x;
    }
    if (current.compensation > best.compensation) {
      best = current;
      best_word = word;
      std::cerr << "best step=" << step
                << " comp=" << (double)best.compensation
                << " H=" << (double)best.h
                << " delta=" << (double)best.delta << "\n";
    }
  }
  std::ofstream out(output);
  out << "{\n  \"n\": " << n
      << ",\n  \"local_compensation\": " << std::setprecision(18)
      << (double)best.compensation
      << ",\n  \"H\": " << (double)best.h
      << ",\n  \"delta\": " << (double)best.delta
      << ",\n  \"mu_1\": " << (double)best.mu1
      << ",\n  \"mu_half\": " << (double)best.muh
      << ",\n  \"evaluated_braids\": " << evaluated
      << ",\n  \"accepted_braids\": " << accepted
      << ",\n  \"commutations\": " << commuted
      << ",\n  \"word_zero_based\": [";
  for (size_t i = 0; i < best_word.size(); ++i) {
    if (i) out << ',';
    out << best_word[i];
  }
  out << "]\n}\n";
}
