#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using std::array;
using std::cerr;
using std::cout;
using std::string;
using std::vector;

struct State {
    int target;
    int bound;
    array<vector<int>, 3> x;
    array<vector<uint8_t>, 3> occupied;
    vector<int16_t> ij, ik, jk;
    int covered_count = 0;
    int64_t weighted = 0;

    explicit State(int target_, int bound_) : target(target_), bound(bound_) {
        for (auto &v : occupied) v.assign(bound + 1, 0);
        ij.assign(target, 0);
        ik.assign(target, 0);
        jk.assign(target, 0);
    }

    bool covered(int q) const {
        return ij[q] || ik[q] || (q > 0 && jk[q - 1] && jk[q]);
    }

    int prefix() const {
        int q = 0;
        while (q < target && covered(q)) ++q;
        return q;
    }

    int64_t score() const {
        // Count coverage first; among equal counts, prefer filling early holes.
        return 1000000LL * covered_count + weighted;
    }

    void initialize(const array<vector<int>, 3> &sets) {
        x = sets;
        for (int c = 0; c < 3; ++c) {
            std::fill(occupied[c].begin(), occupied[c].end(), 0);
            for (int p : x[c]) {
                if (p < 0 || p > bound || occupied[c][p]) {
                    cerr << "invalid initial placement\n";
                    std::exit(2);
                }
                occupied[c][p] = 1;
            }
        }
        std::fill(ij.begin(), ij.end(), 0);
        std::fill(ik.begin(), ik.end(), 0);
        std::fill(jk.begin(), jk.end(), 0);
        for (int a : x[0]) for (int b : x[1]) if (a + b < target) ++ij[a + b];
        for (int a : x[0]) for (int b : x[2]) if (a + b < target) ++ik[a + b];
        for (int a : x[1]) for (int b : x[2]) if (a + b < target) ++jk[a + b];
        covered_count = 0;
        weighted = 0;
        for (int q = 0; q < target; ++q) if (covered(q)) {
            ++covered_count;
            weighted += target - q;
        }
    }

    void mark(vector<int> &affected, int q, vector<uint8_t> &seen) const {
        if (0 <= q && q < target && !seen[q]) {
            seen[q] = 1;
            affected.push_back(q);
        }
    }

    void touch_sum(vector<int> &affected, vector<uint8_t> &seen, int kind, int sum) const {
        if (kind < 2) {
            mark(affected, sum, seen);
        } else {
            // jk[sum] can change the consecutive-pair clauses for q=sum,sum+1.
            mark(affected, sum, seen);
            mark(affected, sum + 1, seen);
        }
    }

    bool move(int color, int index, int replacement) {
        if (replacement < 0 || replacement > bound || occupied[color][replacement]) return false;
        int old = x[color][index];
        vector<int> affected;
        vector<uint8_t> seen(target, 0);

        auto register_pair_changes = [&](int other_color, int kind) {
            for (int b : x[other_color]) {
                touch_sum(affected, seen, kind, old + b);
                touch_sum(affected, seen, kind, replacement + b);
            }
        };
        if (color == 0) { register_pair_changes(1, 0); register_pair_changes(2, 1); }
        if (color == 1) { register_pair_changes(0, 0); register_pair_changes(2, 2); }
        if (color == 2) { register_pair_changes(0, 1); register_pair_changes(1, 2); }

        for (int q : affected) if (covered(q)) {
            --covered_count;
            weighted -= target - q;
        }

        auto update_pairs = [&](int other_color, vector<int16_t> &counts) {
            for (int b : x[other_color]) {
                if (old + b < target) --counts[old + b];
                if (replacement + b < target) ++counts[replacement + b];
            }
        };
        if (color == 0) { update_pairs(1, ij); update_pairs(2, ik); }
        if (color == 1) { update_pairs(0, ij); update_pairs(2, jk); }
        if (color == 2) { update_pairs(0, ik); update_pairs(1, jk); }

        occupied[color][old] = 0;
        occupied[color][replacement] = 1;
        x[color][index] = replacement;

        for (int q : affected) if (covered(q)) {
            ++covered_count;
            weighted += target - q;
        }
        return true;
    }
};

struct Options {
    int target = 511;
    int bound = 510;
    array<int, 3> counts{8, 17, 17};
    int64_t steps = 10000000;
    int restarts = 20;
    uint64_t seed = 791;
    string output;
    bool random_start = false;
};

static Options parse(int argc, char **argv) {
    Options o;
    for (int i = 1; i < argc; ++i) {
        string a = argv[i];
        auto next = [&]() -> string { if (++i >= argc) std::exit(2); return argv[i]; };
        if (a == "--target") o.target = std::stoi(next());
        else if (a == "--bound") o.bound = std::stoi(next());
        else if (a == "--counts") {
            string s = next(); std::replace(s.begin(), s.end(), ',', ' ');
            std::istringstream in(s); in >> o.counts[0] >> o.counts[1] >> o.counts[2];
        } else if (a == "--steps") o.steps = std::stoll(next());
        else if (a == "--restarts") o.restarts = std::stoi(next());
        else if (a == "--seed") o.seed = std::stoull(next());
        else if (a == "--output") o.output = next();
        else if (a == "--random-start") o.random_start = true;
        else { cerr << "unknown option " << a << "\n"; std::exit(2); }
    }
    if (o.bound < o.target - 1) o.bound = o.target - 1;
    return o;
}

static array<vector<int>, 3> kohonen_seed() {
    return {{{0, 5, 112, 117, 122, 127, 132, 137},
             {10, 16, 22, 28, 34, 40, 46, 52, 58, 64, 70, 76, 82, 88, 94, 100, 106},
             {0, 1, 2, 3, 4, 224, 225, 226, 227, 228, 229, 367, 368, 369, 370, 371, 372}}};
}

static array<vector<int>, 3> family20_seed() {
    return {{{0, 3, 34, 37, 40, 43},
             {6, 10, 14, 18, 22, 26, 30},
             {0, 1, 2, 68, 69, 70, 71}}};
}

static array<vector<int>, 3> make_initial(const Options &o, std::mt19937_64 &rng) {
    auto sets = o.random_start
        ? array<vector<int>, 3>{{vector<int>{0}, vector<int>{0}, vector<int>{}}}
        : (o.target == 116 && o.counts == array<int, 3>{6, 7, 7}
           ? family20_seed() : kohonen_seed());
    for (int c = 0; c < 3; ++c) {
        while ((int)sets[c].size() > o.counts[c]) {
            std::uniform_int_distribution<int> pick(0, (int)sets[c].size() - 1);
            sets[c].erase(sets[c].begin() + pick(rng));
        }
        std::set<int> used(sets[c].begin(), sets[c].end());
        std::uniform_int_distribution<int> pos(0, o.bound);
        while ((int)sets[c].size() < o.counts[c]) {
            int p = pos(rng);
            if (used.insert(p).second) sets[c].push_back(p);
        }
    }
    return sets;
}

static string json_placement(const array<vector<int>, 3> &sets) {
    std::ostringstream out;
    out << "{\n";
    const char *names[3] = {"I", "J", "K"};
    for (int c = 0; c < 3; ++c) {
        vector<int> sorted = sets[c]; std::sort(sorted.begin(), sorted.end());
        out << "  \"" << names[c] << "\": [";
        for (size_t i = 0; i < sorted.size(); ++i) {
            if (i) out << ", "; out << sorted[i];
        }
        out << "]" << (c == 2 ? "\n" : ",\n");
    }
    out << "}";
    return out.str();
}

int main(int argc, char **argv) {
    Options o = parse(argc, argv);
    std::mt19937_64 rng(o.seed);
    std::uniform_real_distribution<double> unit(0.0, 1.0);
    auto began = std::chrono::steady_clock::now();
    int global_best_count = -1, global_best_prefix = -1;
    int64_t global_best_score = -1;
    array<vector<int>, 3> global_best;
    int64_t evaluated = 0, accepted = 0;

    for (int restart = 0; restart < o.restarts; ++restart) {
        State state(o.target, o.bound);
        state.initialize(make_initial(o, rng));

        // Later restarts kick the seed into a different basin before cooling.
        for (int kick = 0; kick < restart % 13; ++kick) {
            int c = rng() % 3, idx = rng() % state.x[c].size(), p = rng() % (o.bound + 1);
            state.move(c, idx, p);
        }
        int64_t local_steps = (o.steps + o.restarts - 1) / o.restarts;
        for (int64_t step = 0; step < local_steps && evaluated < o.steps; ++step, ++evaluated) {
            int64_t before = state.score();
            struct Change { int c, idx, old; };
            vector<Change> changes;
            // Min-conflicts component: explicitly propose a representation for
            // one current hole. This is mixed with unguided moves so the chain
            // can still cross barriers and redesign the block architecture.
            if (unit(rng) < 0.38 && state.covered_count < o.target) {
                vector<int> holes;
                for (int q = 0; q < o.target; ++q) if (!state.covered(q)) holes.push_back(q);
                int q = holes[rng() % holes.size()];
                int route = rng() % 6;
                int c, other, required;
                if (route == 0) { c = 0; other = 1; required = q; }
                else if (route == 1) { c = 1; other = 0; required = q; }
                else if (route == 2) { c = 0; other = 2; required = q; }
                else if (route == 3) { c = 2; other = 0; required = q; }
                else if (route == 4) { c = 1; other = 2; required = q - (rng() & 1); }
                else { c = 2; other = 1; required = q - (rng() & 1); }
                int idx = rng() % state.x[c].size();
                int partner = state.x[other][rng() % state.x[other].size()];
                int replacement = required - partner;
                int old = state.x[c][idx];
                if (o.random_start && c < 2 && old == 0) continue;
                if (state.move(c, idx, replacement)) changes.push_back({c, idx, old});
            }
            int number = changes.empty() ? 1 : 0;
            if (unit(rng) < 0.15) number += unit(rng) < 0.25 ? 2 : 1;
            for (int z = 0; z < number; ++z) {
                int c = rng() % 3;
                int idx = rng() % state.x[c].size();
                int old = state.x[c][idx];
                if (o.random_start && c < 2 && old == 0) continue;
                int p;
                if (unit(rng) < 0.68) {
                    int radius = 1 + (int)(-std::log(std::max(1e-12, unit(rng))) * 12.0);
                    p = old + (unit(rng) < 0.5 ? -radius : radius);
                } else p = rng() % (o.bound + 1);
                if (state.move(c, idx, p)) changes.push_back({c, idx, old});
            }
            if (changes.empty()) continue;
            int64_t after = state.score();
            double fraction = (double)step / std::max<int64_t>(1, local_steps - 1);
            double temperature = 3500000.0 * std::pow(800.0 / 3500000.0, fraction);
            bool take = after >= before || unit(rng) < std::exp((double)(after - before) / temperature);
            if (!take) {
                for (auto it = changes.rbegin(); it != changes.rend(); ++it) {
                    if (!state.move(it->c, it->idx, it->old)) {
                        cerr << "failed to undo move\n"; return 3;
                    }
                }
            } else ++accepted;

            int pref = state.prefix();
            if (state.covered_count > global_best_count ||
                (state.covered_count == global_best_count && pref > global_best_prefix) ||
                (state.covered_count == global_best_count && pref == global_best_prefix && state.score() > global_best_score)) {
                global_best_count = state.covered_count;
                global_best_prefix = pref;
                global_best_score = state.score();
                global_best = state.x;
            }
            if (state.covered_count == o.target) {
                cout << "FOUND at proposal " << evaluated << "\n";
                goto finished;
            }
        }
        cerr << "restart " << restart + 1 << "/" << o.restarts
             << " best coverage=" << global_best_count << "/" << o.target
             << " prefix=" << global_best_prefix << "\n";
    }

finished:
    double seconds = std::chrono::duration<double>(std::chrono::steady_clock::now() - began).count();
    std::ostringstream result;
    result << "{\n"
           << "  \"status\": \"" << (global_best_count == o.target ? "FOUND" : "NO_SOLUTION_FOUND") << "\",\n"
           << "  \"target\": " << o.target << ",\n"
           << "  \"bound\": " << o.bound << ",\n"
           << "  \"counts\": [" << o.counts[0] << ", " << o.counts[1] << ", " << o.counts[2] << "],\n"
           << "  \"seed\": " << o.seed << ",\n"
           << "  \"random_start\": " << (o.random_start ? "true" : "false") << ",\n"
           << "  \"proposals\": " << evaluated << ",\n"
           << "  \"accepted\": " << accepted << ",\n"
           << "  \"elapsed_seconds\": " << seconds << ",\n"
           << "  \"best_target_coverage\": " << global_best_count << ",\n"
           << "  \"best_prefix\": " << global_best_prefix << ",\n"
           << "  \"placement\": " << json_placement(global_best) << ",\n"
           << "  \"scope_warning\": \"Heuristic search; failure is not nonexistence.\"\n"
           << "}\n";
    cout << result.str();
    if (!o.output.empty()) { std::ofstream file(o.output); file << result.str(); }
    return global_best_count == o.target ? 0 : 1;
}
