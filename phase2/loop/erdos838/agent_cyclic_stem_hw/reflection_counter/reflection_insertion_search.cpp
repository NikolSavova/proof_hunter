// Exhaustive maximum-H search over one-wire lifts of a supplied reduced word.
//
// The new largest wire starts at the far right.  Deleting it from every
// candidate recovers the supplied word exactly.  Products for z=1 and z=1/2
// are maintained incrementally: appending T updates one row of B=T_k...T_1
// and one column of A=T_1...T_k.  The saved winner is replayed exactly by
// reflection_gadget_search.py; long double is only a discovery score.

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <utility>
#include <vector>

struct PairState {
  int n;
  long double z;
  std::vector<long double> a, b;

  PairState(int size, long double activity)
      : n(size), z(activity), a(size * size, 0), b(size * size, 0) {
    for (int i = 0; i < n; ++i) a[i * n + i] = b[i * n + i] = 1;
  }

  void append(int i, int j) {
    // B <- T B: row_j += z row_i.
    for (int c = 0; c < n; ++c) b[j * n + c] += z * b[i * n + c];
    // A <- A T: column_i += z column_j.
    for (int r = 0; r < n; ++r) a[r * n + i] += z * a[r * n + j];
  }

  void undo(int i, int j) {
    // The source row/column is unchanged by the corresponding update.
    for (int c = 0; c < n; ++c) b[j * n + c] -= z * b[i * n + c];
    for (int r = 0; r < n; ++r) a[r * n + i] -= z * a[r * n + j];
  }

  long double partition() const {
    long double q = 0;
    for (int k = 0; k < n * n; ++k) q += a[k] * b[k];
    return 1 + n * z + q - n;
  }
};

struct Search {
  int old_n, n;
  std::vector<int> old_word;
  std::vector<std::pair<int, int>> old_roots;
  std::vector<int> emitted, best_word;
  PairState one, half;
  uint64_t leaves = 0, nodes = 0;
  long double best_h = -1;

  Search(int size, std::vector<int> word)
      : old_n(size), n(size + 1), old_word(std::move(word)), one(n, 1.0L),
        half(n, 0.5L) {
    std::vector<int> wires(old_n);
    for (int i = 0; i < old_n; ++i) wires[i] = i;
    for (int g : old_word) {
      if (g < 0 || g >= old_n - 1 || wires[g] > wires[g + 1]) {
        throw std::runtime_error("input is not reduced");
      }
      old_roots.push_back({wires[g], wires[g + 1]});
      std::swap(wires[g], wires[g + 1]);
    }
    if ((int)old_word.size() != old_n * (old_n - 1) / 2 ||
        !std::is_sorted(wires.rbegin(), wires.rend())) {
      throw std::runtime_error("input is not a reduced word for w0");
    }
  }

  void push(int generator, int i, int j) {
    if (i > j) std::swap(i, j);
    emitted.push_back(generator);
    one.append(i, j);
    half.append(i, j);
  }

  void pop(int i, int j) {
    if (i > j) std::swap(i, j);
    half.undo(i, j);
    one.undo(i, j);
    emitted.pop_back();
  }

  void visit(int old_step, int new_position, const std::vector<int>& old_perm) {
    ++nodes;
    if (old_step == (int)old_word.size() && new_position == 0) {
      ++leaves;
      const long double f1 = one.partition();
      const long double fh = half.partition();
      const long double h = n * fh / f1;
      if (h > best_h) {
        best_h = h;
        best_word = emitted;
      }
      return;
    }

    if (new_position > 0) {
      const int neighbor = old_perm[new_position - 1];
      push(new_position - 1, neighbor, old_n);
      visit(old_step, new_position - 1, old_perm);
      pop(neighbor, old_n);
    }

    if (old_step < (int)old_word.size()) {
      const int generator = old_word[old_step];
      if (new_position != generator + 1) {
        const int full_generator = generator + (new_position <= generator ? 1 : 0);
        const auto [i, j] = old_roots[old_step];
        push(full_generator, i, j);
        auto next_perm = old_perm;
        std::swap(next_perm[generator], next_perm[generator + 1]);
        visit(old_step + 1, new_position, next_perm);
        pop(i, j);
      }
    }
  }

  void run() {
    std::vector<int> identity(old_n);
    for (int i = 0; i < old_n; ++i) identity[i] = i;
    visit(0, old_n, identity);
  }

  void print() const {
    std::cout << "{\n  \"old_n\": " << old_n << ",\n  \"n\": " << n
              << ",\n  \"candidate_count\": " << leaves
              << ",\n  \"search_node_count\": " << nodes
              << ",\n  \"discovery_H\": " << std::setprecision(20)
              << (double)best_h << ",\n  \"word_zero_based\": [";
    for (size_t k = 0; k < best_word.size(); ++k) {
      if (k) std::cout << ',';
      std::cout << best_word[k];
    }
    std::cout << "]\n}\n";
  }
};

int main(int argc, char** argv) {
  if (argc != 2) {
    std::cerr << "usage: reflection_insertion_search OLD_N < old_word.txt\n";
    return 2;
  }
  const int old_n = std::stoi(argv[1]);
  std::vector<int> word(old_n * (old_n - 1) / 2);
  for (int& generator : word) {
    if (!(std::cin >> generator)) {
      std::cerr << "not enough generators on stdin\n";
      return 2;
    }
  }
  try {
    Search search(old_n, word);
    search.run();
    search.print();
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
}
