// Exploratory segmented-sieve search for explicit pro-2 tower certificates.
// Usage: ./search_split_primes DIMENSION LIMIT TARGET
// The ramification set is the first DIMENSION+1 odd primes.  The square-class
// basis consists of each p=1 mod 4 and 3p for every p>3 with p=3 mod 4.

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

using u64 = std::uint64_t;
using u128 = __uint128_t;

static u64 mul_mod(u64 a, u64 b, u64 m) {
  return static_cast<u64>((static_cast<u128>(a) * b) % m);
}

static u64 pow_mod(u64 a, u64 e, u64 m) {
  u64 answer = 1;
  while (e) {
    if (e & 1) answer = mul_mod(answer, a, m);
    a = mul_mod(a, a, m);
    e >>= 1;
  }
  return answer;
}

static std::vector<int> first_odd_primes(int count) {
  std::vector<int> answer;
  for (int n = 3; static_cast<int>(answer.size()) < count; n += 2) {
    bool prime = true;
    for (int p : answer) {
      if (1LL * p * p > n) break;
      if (n % p == 0) {
        prime = false;
        break;
      }
    }
    if (prime) answer.push_back(n);
  }
  return answer;
}

int main(int argc, char** argv) {
  if (argc != 4) return 2;
  const int dimension = std::atoi(argv[1]);
  const u64 limit = std::strtoull(argv[2], nullptr, 10);
  const int target = std::atoi(argv[3]);

  const auto ramified = first_odd_primes(dimension + 1);
  std::vector<u64> radicands;
  for (int p : ramified) {
    if (p % 4 == 1) radicands.push_back(p);
  }
  for (int p : ramified) {
    if (p > 3 && p % 4 == 3) radicands.push_back(3ULL * p);
  }
  if (static_cast<int>(radicands.size()) != dimension) return 3;

  const int root = static_cast<int>(std::sqrt(static_cast<long double>(limit))) + 1;
  std::vector<bool> composite(root + 1, false);
  std::vector<int> base_primes;
  for (int p = 2; p <= root; ++p) {
    if (composite[p]) continue;
    base_primes.push_back(p);
    if (1LL * p * p <= root) {
      for (int j = p * p; j <= root; j += p) composite[j] = true;
    }
  }

  constexpr u64 block_size = 1'000'000;
  std::vector<bool> marked(block_size);
  std::vector<u64> found;
  for (u64 low = 2; low <= limit && static_cast<int>(found.size()) < target;
       low += block_size) {
    const u64 high = std::min(limit + 1, low + block_size);
    std::fill(marked.begin(), marked.end(), false);
    for (int p : base_primes) {
      if (1ULL * p * p >= high && static_cast<u64>(p) >= high) break;
      u64 start = std::max<u64>(1ULL * p * p, ((low + p - 1) / p) * p);
      for (u64 x = start; x < high; x += p) marked[x - low] = true;
    }
    for (u64 q = low; q < high; ++q) {
      if (marked[q - low] || q % 4 != 1) continue;
      bool split = true;
      for (u64 a : radicands) {
        if (a % q == 0 || pow_mod(a % q, (q - 1) / 2, q) != 1) {
          split = false;
          break;
        }
      }
      if (split) {
        found.push_back(q);
        std::cout << q << (static_cast<int>(found.size()) == target ? '\n' : ' ');
      }
    }
  }
  std::cerr << "dimension=" << dimension << " found=" << found.size()
            << " last=" << (found.empty() ? 0 : found.back()) << '\n';
  return static_cast<int>(found.size()) == target ? 0 : 1;
}
