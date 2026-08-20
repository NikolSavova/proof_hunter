#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <queue>
#include <tuple>
#include <utility>
#include <vector>

// Broad floating-point screen for the CM/Eisenstein real-quadratic family.
// The final record field is certified separately with exact integer arithmetic
// and high-precision Decimal endpoint checks.  This program is only a
// reproducible shortlist/dominance audit.

namespace {

constexpr int kDiscriminantLimit = 100000;
constexpr int kNormLimit = 250000;
constexpr double kAlpha = 0.49371148;
constexpr double kPackingConstant = 1.1026577908435840990;  // 2 sqrt(3) / pi

std::vector<int> primes_up_to(int limit) {
  std::vector<bool> is_prime(limit + 1, true);
  is_prime[0] = is_prime[1] = false;
  for (int p = 2; 1LL * p * p <= limit; ++p) {
    if (!is_prime[p]) continue;
    for (int q = p * p; q <= limit; q += p) is_prime[q] = false;
  }
  std::vector<int> primes;
  for (int n = 2; n <= limit; ++n) {
    if (is_prime[n]) primes.push_back(n);
  }
  return primes;
}

bool squarefree(int n, const std::vector<int>& primes) {
  for (int p : primes) {
    if (1LL * p * p > n) break;
    if (n % (p * p) == 0) return false;
  }
  return true;
}

bool positive_fundamental_discriminant(int D,
                                       const std::vector<int>& primes) {
  if (D % 4 == 1) return squarefree(D, primes);
  if (D % 4 != 0) return false;
  const int d = D / 4;
  return (d % 4 == 2 || d % 4 == 3) && squarefree(d, primes);
}

int legendre(int D, int p) {
  int a = D % p;
  if (a == 0) return 0;
  int n = p;
  int answer = 1;
  while (a != 0) {
    while ((a & 1) == 0) {
      a >>= 1;
      const int residue = n & 7;
      if (residue == 3 || residue == 5) answer = -answer;
    }
    std::swap(a, n);
    if ((a & 3) == 3 && (n & 3) == 3) answer = -answer;
    a %= n;
  }
  return n == 1 ? answer : 0;
}

std::vector<int> odd_prime_ideal_norms(int D,
                                       const std::vector<int>& primes) {
  std::vector<int> degree_one;
  std::vector<int> inert_squares;
  for (int p : primes) {
    if (p == 2) continue;
    if (p > kNormLimit) break;
    const int symbol = legendre(D, p);
    if (symbol == 0) {
      degree_one.push_back(p);
    } else if (symbol == 1) {
      degree_one.push_back(p);
      degree_one.push_back(p);
    } else if (1LL * p * p <= kNormLimit) {
      inert_squares.push_back(p * p);
    }
  }
  std::vector<int> ideals;
  ideals.reserve(degree_one.size() + inert_squares.size());
  std::merge(degree_one.begin(), degree_one.end(), inert_squares.begin(),
             inert_squares.end(), std::back_inserter(ideals));
  return ideals;
}

double local_gain(int q, int depth) {
  const double x = 1.0 / (static_cast<double>(q) * q);
  double previous_sum = 1.0;
  double sum = 1.0;
  double power = 1.0;
  for (int j = 1; j <= depth; ++j) {
    previous_sum = sum;
    power *= x;
    sum += power;
  }
  return 0.25 * std::log(((depth + 1.0) / sum) /
                         (depth / previous_sum));
}

struct Frontier {
  std::vector<double> cost{0.0};
  std::vector<double> gain{0.0};

  double value(double target) const {
    if (target < 0 || target > cost.back()) {
      return -std::numeric_limits<double>::infinity();
    }
    const auto iterator = std::lower_bound(cost.begin(), cost.end(), target);
    const std::size_t index = iterator - cost.begin();
    if (index == 0 || *iterator == target) return gain[index];
    const double fraction =
        (target - cost[index - 1]) / (cost[index] - cost[index - 1]);
    return gain[index - 1] + fraction * (gain[index] - gain[index - 1]);
  }
};

Frontier build_frontier(const std::vector<int>& ideals, int start, int count) {
  Frontier frontier;
  frontier.cost.reserve(3 * count + 1);
  frontier.gain.reserve(3 * count + 1);
  int next[3] = {start, start, start};
  const int end = start + count;
  for (int step = 0; step < 3 * count; ++step) {
    int chosen = -1;
    double chosen_slope = -1.0;
    for (int depth_index = 0; depth_index < 3; ++depth_index) {
      if (next[depth_index] == end) continue;
      const int q = ideals[next[depth_index]];
      const double cost = 0.5 * std::log(q);
      const double gain = local_gain(q, depth_index + 1);
      const double slope = gain / cost;
      if (slope > chosen_slope) {
        chosen = depth_index;
        chosen_slope = slope;
      }
    }
    assert(chosen >= 0);
    const int q = ideals[next[chosen]++];
    const double cost = 0.5 * std::log(q);
    const double gain = local_gain(q, chosen + 1);
    frontier.cost.push_back(frontier.cost.back() + cost);
    frontier.gain.push_back(frontier.gain.back() + gain);
  }
  return frontier;
}

struct Score {
  double margin;
  double w;
  int ramified_count;
  int generator_rank;
  int useful_count;
};

Score score_configuration(int D, const std::vector<int>& ideals, int t) {
  // Honest-loss screen: two unit generators, four independent sign/dyadic
  // conditions, relation excess one, and every eligible ideal declared useful.
  const int d = t - 2;
  const int base_relations = d + 1;
  const int useful = (d * d - 1) / 4 - base_relations - t;
  if (useful <= 0 || t + useful > static_cast<int>(ideals.size())) {
    return {-std::numeric_limits<double>::infinity(), 0.0, t, d, useful};
  }
  double log_rd = 0.5 * std::log(D);
  for (int index = 0; index < t; ++index) {
    log_rd += 0.25 * std::log(ideals[index]);
  }
  const Frontier frontier = build_frontier(ideals, t, useful);
  auto rhs = [&](double w) {
    const double exponent = 2 * (2 * kAlpha - 1) * w - log_rd;
    const double correction = exponent < -700
                                  ? 0.0
                                  : std::log1p(std::exp(exponent) /
                                               kPackingConstant);
    return std::log(kPackingConstant) + log_rd + (2 - 4 * kAlpha) * w +
           correction;
  };
  auto endpoints = [&](double w) {
    const double left = frontier.value(2 * kAlpha * w) - rhs(w);
    const double right = frontier.value(4 * kAlpha * w) - rhs(2 * w);
    return std::pair<double, double>{left, right};
  };
  double low = 0.0;
  double high = frontier.cost.back() / (4 * kAlpha);
  // The relevant crossing has left-right increasing.  A coarse mesh first
  // guards against endpoint or non-unimodal artifacts.
  double best_margin = -std::numeric_limits<double>::infinity();
  double best_w = 0.0;
  const int mesh = 80;
  for (int step = 1; step < mesh; ++step) {
    const double w = high * step / mesh;
    const auto [left, right] = endpoints(w);
    const double margin = std::min(left, right);
    if (margin > best_margin) {
      best_margin = margin;
      best_w = w;
    }
  }
  const double radius = high / mesh;
  low = std::max(0.0, best_w - radius);
  high = std::min(high, best_w + radius);
  // Golden-section maximization of the lower envelope.
  constexpr double phi = 0.6180339887498948482;
  double x = high - phi * (high - low);
  double y = low + phi * (high - low);
  auto minimum_margin = [&](double w) {
    const auto [left, right] = endpoints(w);
    return std::min(left, right);
  };
  double fx = minimum_margin(x);
  double fy = minimum_margin(y);
  for (int iteration = 0; iteration < 70; ++iteration) {
    if (fx < fy) {
      low = x;
      x = y;
      fx = fy;
      y = low + phi * (high - low);
      fy = minimum_margin(y);
    } else {
      high = y;
      y = x;
      fy = fx;
      x = high - phi * (high - low);
      fx = minimum_margin(x);
    }
  }
  best_w = 0.5 * (low + high);
  best_margin = minimum_margin(best_w);
  return {best_margin, best_w, t, d, useful};
}

}  // namespace

int main() {
  const std::vector<int> primes = primes_up_to(kNormLimit);
  std::vector<std::tuple<double, int, Score>> leaders;
  int discriminant_count = 0;
  int capable_count = 0;
  for (int D = 5; D <= kDiscriminantLimit; ++D) {
    if (!positive_fundamental_discriminant(D, primes)) continue;
    ++discriminant_count;
    const std::vector<int> ideals = odd_prime_ideal_norms(D, primes);
    Score best{-std::numeric_limits<double>::infinity(), 0.0, 0, 0, 0};
    // Broad fixed-rank filter.  A second pass below rescans the leaders at
    // every nearby integer count.
    best = score_configuration(D, ideals, 227);
    if (best.margin >= -1e-7) ++capable_count;
    leaders.emplace_back(best.margin, D, best);
  }
  std::sort(leaders.begin(), leaders.end(),
            [](const auto& left, const auto& right) {
              return std::get<0>(left) > std::get<0>(right);
            });
  // Reconstruct and honestly rescan the 100 strongest broad-filter fields.
  const int finalist_count = std::min<int>(100, leaders.size());
  for (int index = 0; index < finalist_count; ++index) {
    const int D = std::get<1>(leaders[index]);
    const std::vector<int> ideals = odd_prime_ideal_norms(D, primes);
    Score best{-std::numeric_limits<double>::infinity(), 0.0, 0, 0, 0};
    for (int t = 205; t <= 250; ++t) {
      const Score score = score_configuration(D, ideals, t);
      if (score.margin > best.margin) best = score;
    }
    std::get<0>(leaders[index]) = best.margin;
    std::get<2>(leaders[index]) = best;
  }
  std::sort(leaders.begin(), leaders.end(),
            [](const auto& left, const auto& right) {
              return std::get<0>(left) > std::get<0>(right);
            });
  std::cout << std::setprecision(12);
  std::cout << "fundamental discriminants scanned: " << discriminant_count
            << "\n";
  std::cout << "fixed-t=227 all-useful candidates at alpha=" << kAlpha
            << ": " << capable_count << "\n";
  const int output_count = std::min<int>(30, leaders.size());
  for (int index = 0; index < output_count; ++index) {
    const auto& [margin, D, score] = leaders[index];
    std::cout << index + 1 << " D=" << D << " margin=" << margin
              << " t=" << score.ramified_count << " d="
              << score.generator_rank << " useful=" << score.useful_count
              << " w=" << score.w << "\n";
  }
}
