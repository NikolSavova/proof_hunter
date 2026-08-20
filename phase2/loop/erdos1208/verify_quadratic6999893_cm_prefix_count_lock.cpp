#include <algorithm>
#include <cassert>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <vector>

// Exhaustive floating-point sweep for the all-square/all-useful norm-prefix
// family over Q(sqrt(6999893)).  The Python companion certifies the exact
// class/ray ranks and recomputes every close numerical decision with Decimal.

namespace {

constexpr int kD = 6999893;
constexpr int kNormLimit = 2500000;
constexpr int kTMin = 50;
constexpr int kTMax = 600;
constexpr int kMaximumDepth = 8;
constexpr long double kAlpha = 0.49368416L;
// A rigorous lower bound for 2 sqrt(3) / pi, favorable to excluded counts.
constexpr long double kPackingConstant = 11978.0L / 10863.0L;

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

int kronecker_odd(int discriminant, int prime) {
  int a = discriminant % prime;
  if (a == 0) return 0;
  int n = prime;
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

std::vector<int> odd_prime_ideal_norms(const std::vector<int>& primes) {
  std::vector<int> degree_one;
  std::vector<int> inert_squares;
  for (int p : primes) {
    if (p == 2) continue;
    const int symbol = kronecker_odd(kD, p);
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
  std::merge(degree_one.begin(), degree_one.end(), inert_squares.begin(),
             inert_squares.end(), std::back_inserter(ideals));
  return ideals;
}

long double local_gain(int norm_q, int depth) {
  const long double q = static_cast<long double>(norm_q);
  const long double x = 1.0L / (q * q);
  long double previous_sum = 1.0L;
  long double sum = 1.0L;
  long double power = 1.0L;
  for (int index = 1; index <= depth; ++index) {
    previous_sum = sum;
    power *= x;
    sum += power;
  }
  return 0.25L * (std::log1pl(1.0L / depth) + std::logl(previous_sum) -
                  std::logl(sum));
}

struct Frontier {
  std::vector<long double> cost{0.0L};
  std::vector<long double> gain{0.0L};
  std::vector<long double> slope;
  long double maximum_omitted_slope = 0.0L;

  std::pair<long double, long double> value_and_slope(long double target) const {
    assert(target > 0.0L && target < cost.back());
    const auto iterator = std::lower_bound(cost.begin(), cost.end(), target);
    const std::size_t index = iterator - cost.begin();
    assert(index > 0 && index < cost.size());
    const long double fraction =
        (target - cost[index - 1]) / (cost[index] - cost[index - 1]);
    return {gain[index - 1] + fraction * (gain[index] - gain[index - 1]),
            slope[index - 1]};
  }
};

Frontier build_frontier(const std::vector<int>& ideals, int start, int count) {
  Frontier frontier;
  std::vector<int> next(kMaximumDepth, start);
  const int end = start + count;
  for (int step = 0; step < kMaximumDepth * count; ++step) {
    int chosen = -1;
    long double chosen_slope = -1.0L;
    for (int depth_index = 0; depth_index < kMaximumDepth; ++depth_index) {
      if (next[depth_index] == end) continue;
      const int q = ideals[next[depth_index]];
      const long double cost = 0.5L * std::logl(q);
      const long double slope = local_gain(q, depth_index + 1) / cost;
      if (slope > chosen_slope) {
        chosen = depth_index;
        chosen_slope = slope;
      }
    }
    assert(chosen >= 0);
    const int q = ideals[next[chosen]++];
    const long double cost = 0.5L * std::logl(q);
    const long double gain = local_gain(q, chosen + 1);
    if (!frontier.slope.empty()) {
      assert(chosen_slope <= frontier.slope.back() + 1e-18L);
    }
    frontier.cost.push_back(frontier.cost.back() + cost);
    frontier.gain.push_back(frontier.gain.back() + gain);
    frontier.slope.push_back(chosen_slope);
  }
  for (int index = start; index < end; ++index) {
    const int q = ideals[index];
    const long double cost = 0.5L * std::logl(q);
    frontier.maximum_omitted_slope = std::max(
        frontier.maximum_omitted_slope,
        local_gain(q, kMaximumDepth + 1) / cost);
  }
  return frontier;
}

struct Endpoint {
  long double margin;
  long double derivative;
  long double active_slope;
};

struct Score {
  int t;
  int d;
  int useful;
  long double anchor;
  Endpoint left;
  Endpoint right;
  long double omitted_slope;
};

Score score_configuration(const std::vector<int>& ideals,
                          const std::vector<long double>& prefix_log_cost,
                          int t) {
  const int d = t - 2;
  const int useful = (d * d - 1) / 4 - (d + 1) - t;
  assert(useful > 0 && t + useful <= static_cast<int>(ideals.size()));
  const long double log_rd =
      0.5L * std::logl(kD) + 0.25L * prefix_log_cost[t];
  const Frontier frontier = build_frontier(ideals, t, useful);

  auto endpoint = [&](long double anchor, int scale) {
    const long double w = scale * anchor;
    const auto [value, slope] =
        frontier.value_and_slope(2.0L * kAlpha * w);
    const long double exponent =
        2.0L * (2.0L * kAlpha - 1.0L) * w - log_rd;
    const long double ratio = std::expl(exponent) / kPackingConstant;
    const long double rhs = std::logl(kPackingConstant) + log_rd +
        (2.0L - 4.0L * kAlpha) * w + std::log1pl(ratio);
    const long double derivative =
        2.0L * kAlpha * scale * slope -
        (2.0L - 4.0L * kAlpha) * scale -
        2.0L * (2.0L * kAlpha - 1.0L) * scale * ratio / (1.0L + ratio);
    return Endpoint{value - rhs, derivative, slope};
  };

  const long double maximum_anchor =
      0.999L * frontier.cost.back() / (4.0L * kAlpha);
  long double low = maximum_anchor / 10000.0L;
  long double high = maximum_anchor;
  auto difference = [&](long double anchor) {
    return endpoint(anchor, 1).margin - endpoint(anchor, 2).margin;
  };
  bool found = false;
  long double previous = low;
  long double previous_difference = difference(previous);
  for (int step = 1; step <= 400; ++step) {
    const long double current = low + (high - low) * step / 400;
    const long double current_difference = difference(current);
    if (previous_difference * current_difference <= 0.0L) {
      low = previous;
      high = current;
      found = true;
      break;
    }
    previous = current;
    previous_difference = current_difference;
  }
  assert(found);
  long double low_difference = difference(low);
  for (int iteration = 0; iteration < 100; ++iteration) {
    const long double middle = (low + high) / 2.0L;
    const long double middle_difference = difference(middle);
    if (low_difference * middle_difference <= 0.0L) {
      high = middle;
    } else {
      low = middle;
      low_difference = middle_difference;
    }
  }
  const long double anchor = (low + high) / 2.0L;
  const Endpoint left = endpoint(anchor, 1);
  const Endpoint right = endpoint(anchor, 2);
  assert(std::fabsl(left.margin - right.margin) < 1e-10L);
  assert(left.derivative > 1e-5L && right.derivative < -1e-5L);
  assert(frontier.maximum_omitted_slope <
         std::min(left.active_slope, right.active_slope));
  return {t, d, useful, anchor, left, right,
          frontier.maximum_omitted_slope};
}

}  // namespace

int main() {
  const auto primes = primes_up_to(kNormLimit);
  const auto ideals = odd_prime_ideal_norms(primes);
  assert(ideals.size() > 90000);
  std::vector<long double> prefix_log_cost(ideals.size() + 1, 0.0L);
  for (std::size_t index = 0; index < ideals.size(); ++index) {
    prefix_log_cost[index + 1] =
        prefix_log_cost[index] + std::logl(ideals[index]);
  }

  std::vector<Score> scores;
  for (int t = kTMin; t <= kTMax; ++t) {
    scores.push_back(score_configuration(ideals, prefix_log_cost, t));
  }
  std::sort(scores.begin(), scores.end(),
            [](const Score& left, const Score& right) {
              return left.left.margin > right.left.margin;
            });

  std::cout << std::setprecision(18);
  std::cout << "range/count: 50..600 / " << scores.size() << "\n";
  for (int index = 0; index < 15; ++index) {
    const Score& score = scores[index];
    std::cout << index + 1 << " T=" << score.t << " d=" << score.d
              << " N=" << score.useful << " margin=" << score.left.margin
              << " anchor=" << score.anchor << " derivatives="
              << score.left.derivative << "," << score.right.derivative
              << " omitted=" << score.omitted_slope << " active="
              << score.left.active_slope << "," << score.right.active_slope
              << "\n";
  }
  const int feasible = std::count_if(
      scores.begin(), scores.end(),
      [](const Score& score) { return score.left.margin >= 0.0L; });
  assert(scores.size() == 551);
  const int expected_leaders[] = {219, 217, 221, 218, 220};
  for (int index = 0; index < 5; ++index) {
    assert(scores[index].t == expected_leaders[index]);
  }
  assert(scores[0].left.margin > 0.0005L);
  assert(scores[1].left.margin < -0.001L);
  assert(scores[2].left.margin < -0.003L);
  assert(feasible == 1);
  std::cout << "feasible count: " << feasible << "\n";
  std::cout << "all-square/all-useful broad prefix count: UNIQUE T=219\n";
}
